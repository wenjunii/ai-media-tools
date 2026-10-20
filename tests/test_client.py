"""Fresh conditional reads, complete document bodies, and cache failure boundaries."""

import base64
import hashlib
import io
import json
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
