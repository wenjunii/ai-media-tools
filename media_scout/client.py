"""Bounded public-source reads. Credentials stay in memory and on GitHub's host."""

import json
import os
import shutil
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


class SourceError(RuntimeError):
    pass


class SafeRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected and urlparse(req.full_url).netloc != urlparse(newurl).netloc:
            redirected.remove_header("Authorization")
        return redirected


class Client:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not self.token and shutil.which("gh"):
            result = subprocess.run(["gh", "auth", "token", "--hostname", "github.com"],
                                    capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.token = result.stdout.strip()
        self.last_search = 0.0
        self.opener = build_opener(SafeRedirect())

    def get(self, url, json_response=True, allow_missing=False):
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in {
            "api.github.com", "raw.githubusercontent.com", "huggingface.co"
        }:
            raise SourceError("Collector only reads allowlisted HTTPS source hosts")
        headers = {"User-Agent": "AI-Media-Scout/0.1 (creator research)",
                   "Accept": "application/vnd.github+json" if parsed.hostname == "api.github.com" else "application/json"}
        if parsed.hostname == "api.github.com":
            headers["X-GitHub-Api-Version"] = "2022-11-28"
            if self.token:
                headers["Authorization"] = "Bearer " + self.token
            if parsed.path.startswith("/search/"):
                interval = 2.2 if self.token else 6.2
                time.sleep(max(0, interval - (time.monotonic() - self.last_search)))
                self.last_search = time.monotonic()
        try:
            with self.opener.open(Request(url, headers=headers), timeout=20) as response:
                raw = response.read(2_000_001)
                if len(raw) > 2_000_000:
                    raise SourceError("Source response exceeded the 2 MB collection limit")
                value = raw.decode("utf-8", errors="replace")
                return json.loads(value) if json_response else value
        except HTTPError as error:
            if allow_missing and error.code == 404:
                return None
            raise SourceError(f"HTTP {error.code} from {parsed.hostname}{parsed.path}; source not collected") from None
        except (URLError, TimeoutError, ValueError) as error:
            raise SourceError(f"Could not read {parsed.hostname}{parsed.path}: {type(error).__name__}") from None
