"""Bounded public-source reads. Credentials stay in memory and on GitHub's host."""

import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .storage import write_json

MAX_RESPONSE_BYTES = 2_000_000


class SourceError(RuntimeError):
    pass


class SafeRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected and urlparse(req.full_url).netloc != urlparse(newurl).netloc:
            redirected.remove_header("Authorization")
            redirected.remove_header("If-none-match")
        return redirected


class Client:
    def __init__(self, cache_dir=None):
        self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not self.token and shutil.which("gh"):
            result = subprocess.run(["gh", "auth", "token", "--hostname", "github.com"],
                                    capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.token = result.stdout.strip()
        self.last_search = 0.0
        self.opener = build_opener(SafeRedirect())
        self.cache_dir = Path(cache_dir) if cache_dir is not None else None
        self.usage = {"network_requests": 0, "conditional_requests": 0,
                      "not_modified": 0, "downloaded_bytes": 0,
                      "inline_documents": 0, "cache_errors": 0}

    def _cache_path(self, url, json_response):
        # Discovery queries are always live. Cache only known repository reads;
        # never persist request headers, tokens, or arbitrary API URL parameters.
        parsed = urlparse(url)
        if (self.cache_dir is None or not json_response or parsed.netloc != "api.github.com"
                or not re.fullmatch(r"/repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
                                    r"(?:/readme|/license|/releases|/commits)?", parsed.path)
                or parsed.query not in {"", "per_page=1"} or parsed.fragment):
            return None
        return self.cache_dir / (hashlib.sha256(url.encode()).hexdigest() + ".json")

    def _cached(self, path, url):
        if path is None:
            return None
        try:
            with path.open("rb") as stream:
                stored = stream.read(3_000_001)
            if len(stored) > 3_000_000:
                raise ValueError("Oversize cache")
            entry = json.loads(stored)
            etag = entry["etag"]
            if (entry["version"] != 1 or entry["url"] != url or not isinstance(etag, str)
                    or not re.fullmatch(r'(?:W/)?"[\x21\x23-\x7e]{1,512}"', etag)):
                raise ValueError("Invalid cache metadata")
            raw = base64.b64decode(entry["body"], validate=True)
            if len(raw) > MAX_RESPONSE_BYTES or hashlib.sha256(raw).hexdigest() != entry["sha256"]:
                raise ValueError("Invalid cache body")
            # Check JSON before making a conditional request; a bad cache becomes
            # an ordinary live fetch, never a stale-data fallback.
            value = json.loads(raw.decode("utf-8", errors="replace"))
            return etag, value
        except FileNotFoundError:
            return None
        except (OSError, ValueError, KeyError, TypeError):
            self.usage["cache_errors"] += 1
            return None

    def _save_cache(self, path, url, raw, etag):
        if path is None or not isinstance(etag, str) or not re.fullmatch(
                r'(?:W/)?"[\x21\x23-\x7e]{1,512}"', etag):
            return
        try:
            write_json(path, {"version": 1, "url": url, "etag": etag,
                             "sha256": hashlib.sha256(raw).hexdigest(),
                             "body": base64.b64encode(raw).decode("ascii")})
        except OSError:
            # A cache is disposable; failure to save it does not invalidate the
            # live response that was just received.
            self.usage["cache_errors"] += 1

    def get(self, url, json_response=True, allow_missing=False):
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.username or parsed.password or parsed.hostname not in {
            "api.github.com", "raw.githubusercontent.com", "huggingface.co"
        }:
            raise SourceError("Collector only reads allowlisted HTTPS source hosts")
        headers = {"User-Agent": "AI-Media-Scout/0.1 (creator research)",
                   "Accept": "application/vnd.github+json" if parsed.hostname == "api.github.com" else "application/json"}
        cache_path = self._cache_path(url, json_response)
        cached = self._cached(cache_path, url)
        if cached:
            headers["If-None-Match"] = cached[0]
            self.usage["conditional_requests"] += 1
        if parsed.hostname == "api.github.com":
            headers["X-GitHub-Api-Version"] = "2022-11-28"
            if self.token:
                headers["Authorization"] = "Bearer " + self.token
            if parsed.path.startswith("/search/"):
                interval = 2.2 if self.token else 6.2
                time.sleep(max(0, interval - (time.monotonic() - self.last_search)))
                self.last_search = time.monotonic()
        try:
            self.usage["network_requests"] += 1
            with self.opener.open(Request(url, headers=headers), timeout=20) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
                self.usage["downloaded_bytes"] += len(raw)
                if len(raw) > MAX_RESPONSE_BYTES:
                    raise SourceError("Source response exceeded the 2 MB collection limit")
                value = raw.decode("utf-8", errors="replace")
                result = json.loads(value) if json_response else value
                # A redirected response's validator belongs to the other URL.
                if response.geturl() == url:
                    self._save_cache(cache_path, url, raw, response.headers.get("ETag"))
                return result
        except HTTPError as error:
            if error.code == 304 and cached and error.filename == url:
                self.usage["not_modified"] += 1
                return cached[1]
            if allow_missing and error.code == 404:
                return None
            raise SourceError(f"HTTP {error.code} from {parsed.hostname}{parsed.path}; source not collected") from None
        except (URLError, TimeoutError, ValueError) as error:
            raise SourceError(f"Could not read {parsed.hostname}{parsed.path}: {type(error).__name__}") from None


def repository_document(client, metadata):
    """Use the complete Contents API body when its Git blob hash verifies."""
    if metadata.get("encoding") == "base64" and isinstance(metadata.get("content"), str):
        try:
            raw = base64.b64decode("".join(metadata["content"].split()), validate=True)
            blob = b"blob " + str(len(raw)).encode() + b"\0" + raw
            if (len(raw) <= MAX_RESPONSE_BYTES and metadata.get("size") == len(raw)
                    and metadata.get("sha") == hashlib.sha1(blob).hexdigest()):
                if hasattr(client, "usage"):
                    client.usage["inline_documents"] += 1
                return raw.decode("utf-8", errors="replace")
        except ValueError:
            pass
    url = metadata.get("download_url")
    if not url:
        raise SourceError("Complete repository document was not available")
    return client.get(url, json_response=False)
