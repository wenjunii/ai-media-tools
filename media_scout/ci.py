"""Conservative CI scope detection using the complete local Git diff, without API calls."""

import json
import os
from pathlib import Path
import re
import subprocess


PUBLIC_FILES = {"public/index.html", "public/README.md", "public/library.json",
                "public/.nojekyll", "public/assets/library.js", "public/assets/library.css"}


def content_only(path):
    """Only generated publication files and ordinary documentation can skip tests."""
    if path in PUBLIC_FILES or path in {"README.md", "config/quality_reviews.json"}:
        return True
    if re.fullmatch(r"docs/[A-Za-z0-9_./-]+\.md", path) and ".." not in path.split("/"):
        return True
    return bool(re.fullmatch(
        r"public/reports/\d{4}-\d{2}-\d{2}/(?:updates/r[1-9]\d*/)?"
        r"(?:report\.(?:html|md|json)|publication\.json)", path))


def classify(root, event_name, event, expected_head):
    # A missing/unavailable base, unknown event, manual dispatch or empty diff
    # chooses all tests. A shallow clone may reduce efficiency, never assurance.
    fallback = {"full": True, "reason": "Source changes or an unverified diff require all tests."}
    try:
        if event_name == "pull_request":
            base = event["pull_request"]["base"]["sha"]
        elif event_name == "push":
            base = event["before"]
        else:
            return fallback
        if not all(isinstance(sha, str) and re.fullmatch(r"[a-f0-9]{40,64}", sha)
                   and set(sha) != {"0"} for sha in (base, expected_head)):
            return fallback
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, stderr=subprocess.DEVNULL).decode().strip()
        if head != expected_head:
            return fallback
        # --no-renames lists both old and new paths, so moving source into docs
        # cannot hide it. NUL delimiters preserve filenames containing newlines.
        raw = subprocess.check_output(
            ["git", "diff", "--no-renames", "--name-only", "-z", base, head, "--"],
            cwd=root, stderr=subprocess.DEVNULL)
        paths = [p.decode("utf-8") for p in raw.split(b"\0") if p]
        if paths and all(content_only(path) for path in paths):
            return {"full": False, "reason": "Only publication data or documentation changed.",
                    "changed_files": len(paths)}
    except (KeyError, TypeError, OSError, ValueError, subprocess.CalledProcessError):
        pass
    return fallback


def main():
    try:
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    except (KeyError, OSError, ValueError):
        event = {}
    result = classify(Path.cwd(), os.environ.get("GITHUB_EVENT_NAME"), event,
                      os.environ.get("GITHUB_SHA"))
    print(json.dumps(result))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            stream.write("full=" + str(result["full"]).lower() + "\n")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
            stream.write(result["reason"] + "\n\nArchive integrity and browser checks run for every commit.\n")


if __name__ == "__main__":
    main()
