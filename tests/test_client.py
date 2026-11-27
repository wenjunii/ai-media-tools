"""Fresh conditional reads, complete document bodies, and cache failure boundaries."""

import base64
from contextlib import contextmanager
import hashlib
from http.client import HTTPResponse, IncompleteRead, RemoteDisconnected, responses
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError
from urllib.request import Request

from media_scout.client import Client, MAX_RESPONSE_BYTES, SafeRedirect, SourceError, repository_document


class Reply(io.BytesIO):
    def __init__(self, url, raw, etag='"v1"'):
        super().__init__(raw)
        self.url, self.headers = url, {"ETag": etag}

    def geturl(self):
        return self.url


def http_response(status, body=b"", **headers):
    headers.setdefault("Content-Length", str(len(body)))
    head = f"HTTP/1.1 {status} {responses[status]}\r\n"
    head += "".join(f"{name}: {value}\r\n" for name, value in headers.items())
    socket = Mock()
    socket.makefile.return_value = io.BytesIO(head.encode("ascii") + b"\r\n" + body)
    response = HTTPResponse(socket)
    response.begin()
    return response


def https_connection(*responses):
    connection = Mock(sock=None)

    def send(*args, **kwargs):
        connection.sock = Mock()

    connection.request.side_effect = send
    connection.getresponse.side_effect = responses
    return connection


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cache = Path(self.temp.name) / "http-cache"
        self.url = "https://api.github.com/repos/example/art/readme"
        self.raw = b'{"content":"documentation"}'
        self.requests = []

    def client(self, *responses):
        with patch.dict("os.environ", {"GITHUB_TOKEN": "private-token-for-test-only"}):
            client = Client(cache_dir=self.cache)
        values = iter(responses)
        def open_response(request, timeout):
            self.requests.append(request)
            value = next(values)
            if isinstance(value, Exception):
                raise value
            return value
        client.opener = Mock(open=open_response)
        return client

    def warm(self):
        self.client(Reply(self.url, self.raw)).get(self.url)

    @contextmanager
    def persistent_client(self, *connections, proxies=None):
        with patch.dict("os.environ", {"GITHUB_TOKEN": "private-token-for-test-only"}), \
                patch("urllib.request.getproxies", return_value=proxies or {}), \
                patch("media_scout.client.HTTPSConnection", side_effect=connections) as connect:
            client = Client(cache_dir=self.cache, reuse_github_connection=True)
            try:
                yield client, connect
            finally:
                client.close()

    def test_direct_github_reads_reuse_the_connection_through_a_fresh_304(self):
        new = b'{"content":"updated documentation"}'
        connection = https_connection(http_response(200, self.raw, ETag='"v1"'),
                                      http_response(304),
                                      http_response(200, new, ETag='"v2"'))
        with self.persistent_client(connection) as (client, connect):
            self.assertEqual(client.get(self.url), json.loads(self.raw))
            self.assertEqual(client.get(self.url), json.loads(self.raw))
            self.assertEqual(client.get(self.url), json.loads(new))
            calls = connection.request.call_args_list
            self.assertEqual(calls[1].kwargs["headers"]["If-none-match"], '"v1"')
            connect.assert_called_once()
            self.assertEqual(client.usage["network_requests"], 3)
            self.assertEqual(client.usage["github_connection_reuses"], 2)
            self.assertEqual(client.usage["not_modified"], 1)
        connection.close.assert_called_once()

    def test_failed_or_incomplete_persistent_reads_discard_the_connection(self):
        self.warm()
        for failure in (
                RemoteDisconnected("disconnected"),
                http_response(429, b"rate limited"),
                http_response(200, b"{}", **{"Content-Length": "10"}),
                http_response(200, b"x" * (MAX_RESPONSE_BYTES + 1)),
        ):
            with self.subTest(failure=failure):
                connection = https_connection(failure)
                new = b'{"content":"live result"}'
                next_connection = https_connection(http_response(200, new, ETag='"v2"'))
                with self.persistent_client(connection, next_connection) as (client, connect):
                    with self.assertRaises(SourceError):
                        client.get(self.url)
                    self.assertEqual(client.usage["network_requests"], 1)
                    self.assertEqual(client.usage["not_modified"], 0)
                    self.assertEqual(connect.call_count, 1)
                    connection.close.assert_called_once()
                    self.assertEqual(client.get(self.url), json.loads(new))
                    self.assertEqual(connect.call_count, 2)

    def test_persistent_redirect_keeps_cross_host_credentials_and_validators_off_target(self):
        self.warm()
        destination = "https://raw.githubusercontent.com/example/art/main/README.md"
        connection = https_connection(http_response(302, b"redirect", Location=destination))
        response = http_response(200, b'{"content":"redirected"}')
        response.url = destination
        with self.persistent_client(connection) as (client, _), \
                patch("media_scout.client.HTTPSHandler.https_open", return_value=response) as standard_open:
            self.assertEqual(client.get(self.url), {"content": "redirected"})
            request = standard_open.call_args.args[0]
            self.assertEqual(request.full_url, destination)
            self.assertIsNone(request.get_header("Authorization"))
            self.assertIsNone(request.get_header("If-none-match"))

    def test_persistent_client_uses_the_standard_https_handler_for_a_proxy(self):
        response = http_response(200, self.raw)
        response.url = self.url
        with self.persistent_client(proxies={"https": "http://proxy.example:3128"}) as (client, connect), \
                patch("urllib.request.proxy_bypass", return_value=False), \
                patch("media_scout.client.HTTPSHandler.https_open", return_value=response) as standard_open:
            self.assertEqual(client.get(self.url), json.loads(self.raw))
            connect.assert_not_called()
            self.assertEqual(standard_open.call_args.args[0].host, "proxy.example:3128")

    def test_persistent_client_leaves_search_on_the_standard_paced_path(self):
        url = "https://api.github.com/search/repositories?q=AI"
        responses = [http_response(200, b"{}"), http_response(200, b"{}")]
        for response in responses:
            response.url = url
        with self.persistent_client() as (client, connect), \
                patch("media_scout.client.HTTPSHandler.https_open", side_effect=responses) as standard_open, \
                patch("media_scout.client.time.sleep") as sleep:
            client.get(url)
            client.get(url)
            self.assertEqual(sleep.call_count, 2)
            self.assertEqual(standard_open.call_count, 2)
            connect.assert_not_called()

    def test_fresh_304_reuses_verified_body_across_processes_without_storing_credentials(self):
        self.warm()
        self.assertNotIn("private-token", next(self.cache.glob("*.json")).read_text())
        client = self.client(HTTPError(self.url, 304, "Not modified", {}, None))
        self.assertEqual(client.get(self.url), json.loads(self.raw))
        self.assertEqual(self.requests[-1].get_header("If-none-match"), '"v1"')
        self.assertEqual(client.usage["network_requests"], 1)
        self.assertEqual(client.usage["not_modified"], 1)
        self.assertEqual(client.usage["downloaded_bytes"], 0)

    def test_changed_response_replaces_cache_and_next_request_uses_new_validator(self):
        self.warm()
        new = b'{"content":"new documentation"}'
        client = self.client(Reply(self.url, new, '"v2"'), HTTPError(self.url, 304, "", {}, None))
        self.assertEqual(client.get(self.url), json.loads(new))
        self.assertEqual(client.get(self.url), json.loads(new))
        self.assertEqual(self.requests[-1].get_header("If-none-match"), '"v2"')

    def test_verified_cache_use_refreshes_retention_without_changing_its_bytes(self):
        self.warm()
        path = next(self.cache.glob("*.json"))
        before = path.read_bytes()
        os.utime(path, (1, 1))
        client = self.client(HTTPError(self.url, 304, "Not modified", {}, None))
        self.assertEqual(client.get(self.url), json.loads(self.raw))
        self.assertGreater(path.stat().st_mtime, 1)
        self.assertEqual(path.read_bytes(), before)

    def test_network_http_and_missing_errors_never_use_stale_evidence(self):
        self.warm()
        for error in [URLError("offline"), TimeoutError(), HTTPError(self.url, 403, "", {}, None),
                      HTTPError(self.url, 429, "", {}, None), HTTPError(self.url, 500, "", {}, None)]:
            with self.subTest(error=type(error).__name__), self.assertRaises(SourceError):
                self.client(error).get(self.url)
        self.assertIsNone(self.client(HTTPError(self.url, 404, "", {}, None)).get(self.url, allow_missing=True))
        with self.assertRaises(SourceError):
            self.client(HTTPError(self.url, 404, "", {}, None)).get(self.url)

    def test_corrupt_wrong_url_and_injected_validator_cache_is_refetched(self):
        self.warm()
        path = next(self.cache.glob("*.json"))
        valid = json.loads(path.read_text())
        for change in [{"sha256": "wrong"}, {"url": self.url + "/other"}, {"body": "invalid base64!"},
                       {"etag": '"v1"\r\nAuthorization: stolen'}, {"version": 99}]:
            path.write_text(json.dumps(dict(valid, **change)))
            client = self.client(Reply(self.url, self.raw))
            self.assertEqual(client.get(self.url), json.loads(self.raw))
            self.assertIsNone(self.requests[-1].get_header("If-none-match"))
            self.assertEqual(client.usage["cache_errors"], 1)

    def test_interrupted_connections_are_source_gaps_without_retry_or_stale_fallback(self):
        self.warm()
        cache_path = next(self.cache.glob("*.json"))
        before = cache_path.read_bytes()
        for phase in ("open", "read"):
            for error in (RemoteDisconnected("private response detail"),
                          IncompleteRead(b"private partial body", 100),
                          ConnectionResetError("private connection detail")):
                with self.subTest(phase=phase, error=type(error).__name__):
                    response = error
                    if phase == "read":
                        response = Reply(self.url, self.raw)
                        response.read = Mock(side_effect=error)
                    client = self.client(response)
                    with self.assertRaises(SourceError) as caught:
                        client.get(self.url, allow_missing=True)
                    self.assertIn(type(error).__name__, str(caught.exception))
                    self.assertNotIn("private", str(caught.exception))
                    self.assertEqual(client.usage["network_requests"], 1)
                    self.assertEqual(client.usage["not_modified"], 0)
                    self.assertEqual(cache_path.read_bytes(), before)

    def test_cache_write_failure_preserves_live_response(self):
        client = self.client(Reply(self.url, self.raw))
        with patch("media_scout.client.write_json", side_effect=OSError("read-only")):
            self.assertEqual(client.get(self.url), json.loads(self.raw))
        self.assertEqual(client.usage["cache_errors"], 1)

    def test_searches_and_nonrepository_hosts_are_always_live(self):
        for url in ["https://api.github.com/search/repositories?q=AI",
                    "https://huggingface.co/api/models",
                    "https://api.github.com/repos/example/art/readme?secret=private",
                    "https://api.github.com/repos/example/art/issues"]:
            client = self.client(Reply(url, b"{}"), Reply(url, b"{}"))
            with patch("media_scout.client.time.sleep"):
                client.get(url)
                client.get(url)
            self.assertIsNone(self.requests[-1].get_header("If-none-match"))
        self.assertFalse(self.cache.exists())

    def test_invalid_json_or_oversize_body_cannot_enter_cache(self):
        for raw in (b"not JSON", b"x" * (MAX_RESPONSE_BYTES + 1)):
            with self.assertRaises(SourceError):
                self.client(Reply(self.url, raw)).get(self.url)
            self.assertFalse(self.cache.exists())

    def test_unexpected_304_or_redirected_validator_is_not_accepted(self):
        with self.assertRaises(SourceError):
            self.client(HTTPError(self.url, 304, "", {}, None)).get(self.url)
        self.warm()
        other = "https://api.github.com/repos/new/art/readme"
        with self.assertRaises(SourceError):
            self.client(HTTPError(other, 304, "", {}, None)).get(self.url)
        request = Request(self.url, headers={"Authorization": "secret", "If-None-Match": '"v1"'})
        result = SafeRedirect().redirect_request(request, None, 302, "", {},
                                                "https://raw.githubusercontent.com/example/art/README.md")
        self.assertIsNone(result.get_header("Authorization"))
        self.assertIsNone(result.get_header("If-none-match"))

    def test_complete_contents_avoids_raw_download_and_checks_size_and_blob_hash(self):
        raw = b"Full LICENSE or README\n"
        metadata = {"encoding": "base64", "content": base64.encodebytes(raw).decode(),
                    "size": len(raw),
                    "download_url": "https://raw.githubusercontent.com/example/art/main/LICENSE"}
        # Compute using the byte count, so fixtures also work after text edits.
        metadata["sha"] = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        client = self.client()
        self.assertEqual(repository_document(client, metadata), raw.decode())
        self.assertEqual(self.requests, [])
        self.assertEqual(client.usage["inline_documents"], 1)
        for changed in [{"sha": "incorrect"}, {"size": len(raw) + 1}, {"content": "invalid!"}]:
            fallback = self.client(Reply(metadata["download_url"], b"live fallback"))
            self.assertEqual(repository_document(fallback, dict(metadata, **changed)), "live fallback")
        with self.assertRaises(SourceError):
            repository_document(client, {"encoding": "none"})


if __name__ == "__main__":
    unittest.main()
