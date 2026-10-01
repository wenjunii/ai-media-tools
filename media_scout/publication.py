"""Publishable report exports and verified GitHub checkpoints before email.

Git commits, pull requests and merges are performed by the research agent. These
commands export only finished reports and verify the actual remote commit and CI;
an edited local receipt alone cannot authorize delivery.
"""

import hashlib
import json
from pathlib import Path
import re
import subprocess

from .configuration import load_config
from .report import verify_report
from .storage import ROOT, locked, now, read_json, report_date, write_json, write_text

REPORT_FILES = ("report.html", "report.md", "report.json")
SECRET_PATTERNS = (
    r"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})",
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
)


def _run(args, root):
    try:
        result = subprocess.run(args, cwd=root, capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise RuntimeError(f"{args[0]} is unavailable or timed out; GitHub sync is unverified") from error
    if result.returncode:
        # Git errors may contain credential-bearing URLs; never echo stderr.
        raise RuntimeError(f"{args[0]} verification failed; inspect GitHub publication before email")
    return result.stdout


def _digest(content):
    return hashlib.sha256(content).hexdigest()


def _json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _safe_path(root, name):
    path = root / name
    ancestors = [root.joinpath(*path.relative_to(root).parts[:index])
                 for index in range(1, len(path.relative_to(root).parts) + 1)]
    if any(item.is_symlink() for item in ancestors) or not path.resolve().is_relative_to(root):
        raise ValueError("Public export paths must stay inside this checkout without symlinks")
    return path


def _check_public_content(content, root, config):
    text = content.decode("utf-8")
    recipient = config.get("recipient")
    if (recipient and recipient.casefold() in text.casefold()) or str(root) in text:
        raise ValueError("Public content contains private delivery settings or a local project path")
    if any(re.search(pattern, text) for pattern in SECRET_PATTERNS):
        raise ValueError("Public content contains credential material; publication is blocked")


def _finished_files(day, root, manifest):
    prefix = f"public/reports/{day}"
    contents = {f"{prefix}/{name}": (root / "reports" / day / name).read_bytes()
                for name in REPORT_FILES}
    public_manifest = {
        "report_date": day, "sealed_at": manifest["sealed_at"],
        "profile_count": manifest["profile_count"], "lead_count": manifest.get("lead_count", 0),
        "sha256": {Path(name).name: _digest(value) for name, value in contents.items()},
    }
    contents[f"{prefix}/publication.json"] = _json_bytes(public_manifest)
    return contents


def _archive_readme(root):
    lines = ["# Daily reports", "", "Finished AI Media Scout editions, with full profiles and primary-source citations.",
             "", "[Searchable HTML library](index.html) (download or open locally).", "",
             "| Date | Full profiles | Additional discoveries | Editions |",
             "| --- | ---: | ---: | --- |"]
    for path in sorted((root / "public/reports").glob("*/publication.json"), reverse=True):
        day = report_date(path.parent.name)
        metadata = read_json(path)
        profiles, leads = int(metadata["profile_count"]), int(metadata.get("lead_count", 0))
        editions = " · ".join(f"[{label}](reports/{day}/{name})" for label, name in
                              (("Markdown", "report.md"), ("HTML", "report.html"), ("JSON", "report.json")))
        lines.append(f"| {day} | {profiles} | {leads} | {editions} |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def export_report(day, root=ROOT):
    root = Path(root).resolve()
    day = report_date(day)
    with locked(root):
        manifest = verify_report(day, root)
        config = load_config(root)
        contents = _finished_files(day, root, manifest)
        archive = root / "site/index.html"
        if not archive.is_file():
            raise ValueError("Build the searchable archive before exporting the report")
        public_archive = archive.read_text().replace("../reports/", "reports/").encode("utf-8")
        for name, content in contents.items():
            _check_public_content(content, root, config)
            path = _safe_path(root, name)
            if path.exists() and path.read_bytes() != content:
                raise ValueError("An existing public edition differs from the sealed report; preserve it")
        _check_public_content(public_archive, root, config)
        for name, content in contents.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        contents["public/index.html"] = public_archive
        contents["public/README.md"] = _archive_readme(root)
        for name in ("public/index.html", "public/README.md"):
            _check_public_content(contents[name], root, config)
            write_text(_safe_path(root, name), contents[name].decode("utf-8"))
        verify_report(day, root)
        return {"report_date": day, "status": "exported", "files": list(contents),
                "note": "Commit and merge these exports through a pull request, then record-sync before email"}


def audit_publication(root=ROOT):
    """Check the complete Git index before a public commit or push."""
    root = Path(root).resolve()
    config = load_config(root)
    names = _run(["git", "ls-files", "-z"], root).decode().split("\0")
    count = 0
    for name in filter(None, names):
        path = Path(name)
        if (path.parts[0] in {"state", "research", "reports", "site", ".venv"}
                or path.name.startswith(".env") or path.name.endswith(".local.json")
                or path.name == "AGENTS.local.md"):
            raise ValueError("Private operational files are staged or tracked; publication is blocked")
        _safe_path(root, name)
        _check_public_content(_run(["git", "show", ":" + name], root), root, config)
        count += 1
    return {"status": "passed", "tracked_files_checked": count}


def _github_settings(config):
    settings = config.get("github_sync", {})
    repository = settings.get("repository", "")
    branch = settings.get("branch", "main")
    workflow = settings.get("ci_workflow", "ci.yml")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*/[A-Za-z0-9][A-Za-z0-9._-]*", repository):
        raise ValueError("Configure github_sync.repository as OWNER/REPO")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", branch) or ".." in branch:
        raise ValueError("Configure a valid GitHub publication branch")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*\.ya?ml", workflow):
        raise ValueError("Configure a CI workflow filename")
    return repository, branch, workflow


def _verified_remote(day, root, manifest, config):
    repository, branch, workflow = _github_settings(config)
    remote_url = _run(["git", "remote", "get-url", "origin"], root).decode().strip()
    allowed = {f"https://github.com/{repository}", f"https://github.com/{repository}.git",
               f"git@github.com:{repository}.git", f"ssh://git@github.com/{repository}.git"}
    if remote_url.casefold() not in {url.casefold() for url in allowed}:
        raise ValueError("origin does not match the configured GitHub repository")
    if _run(["git", "branch", "--show-current"], root).decode().strip() != branch:
        raise ValueError("Return to the configured main branch after merging the publication")
    if _run(["git", "status", "--porcelain"], root).strip():
        raise ValueError("Project changes are not fully committed and synchronized; email is blocked")
    head = _run(["git", "rev-parse", "HEAD"], root).decode().strip()
    tracking = _run(["git", "rev-parse", f"origin/{branch}"], root).decode().strip()
    remote_lines = _run(["git", "ls-remote", "origin", f"refs/heads/{branch}"], root).decode().split()
    if not remote_lines or head != tracking or head != remote_lines[0]:
        raise ValueError("Local, tracking and GitHub commits do not match; email is blocked")
    audit_publication(root)
    contents = _finished_files(day, root, manifest)
    contents["public/index.html"] = (root / "site/index.html").read_text().replace("../reports/", "reports/").encode("utf-8")
    contents["public/README.md"] = _archive_readme(root)
    for name, expected in contents.items():
        _check_public_content(expected, root, config)
        actual = _run(["git", "show", head + ":" + name], root)
        if actual != expected:
            raise ValueError("The GitHub commit does not contain the complete current report and archive")
    runs = json.loads(_run(["gh", "run", "list", "--repo", repository, "--branch", branch,
        "--workflow", workflow, "--commit", head, "--event", "push", "--limit", "20",
        "--json", "databaseId,headSha,status,conclusion,url"], root))
    matches = [run for run in runs if run.get("headSha") == head]
    if not matches or matches[0].get("status") != "completed" or matches[0].get("conclusion") != "success":
        raise RuntimeError("GitHub CI has not succeeded for the synchronized main commit; email is blocked")
    final_remote = _run(["git", "ls-remote", "origin", f"refs/heads/{branch}"], root).decode().split()
    if (not final_remote or final_remote[0] != head
            or _run(["git", "rev-parse", "HEAD"], root).decode().strip() != head
            or _run(["git", "status", "--porcelain"], root).strip()):
        raise ValueError("The project or GitHub changed during verification; email is blocked")
    return {"repository": repository, "branch": branch, "commit": head,
            "ci_run_id": matches[0]["databaseId"], "ci_url": matches[0]["url"],
            "public_files_sha256": {name: _digest(value) for name, value in contents.items()}}


def record_sync(day, root=ROOT):
    root = Path(root).resolve()
    day = report_date(day)
    with locked(root):
        manifest = verify_report(day, root)
        verified = _verified_remote(day, root, manifest, load_config(root))
        verify_report(day, root)
        receipt = dict(verified, report_date=day, status="synced", verified_at=now(),
            report_sha256=manifest["sha256"][f"reports/{day}/report.html"],
            report_url=f'https://github.com/{verified["repository"]}/blob/{verified["branch"]}/public/reports/{day}/report.md')
        write_json(root / "state/publications" / (day + ".json"), receipt)
        return receipt


def verify_sync(day, root=ROOT):
    """Read-only verification; caller may hold the process lock before delivery."""
    root = Path(root).resolve()
    day = report_date(day)
    manifest = verify_report(day, root)
    receipt = read_json(root / "state/publications" / (day + ".json"))
    if not receipt or receipt.get("status") != "synced":
        raise ValueError("No verified GitHub sync checkpoint for this report; run record-sync before email")
    if receipt.get("report_sha256") != manifest["sha256"][f"reports/{day}/report.html"]:
        raise ValueError("GitHub sync checkpoint belongs to a different report")
    verified = _verified_remote(day, root, manifest, load_config(root))
    for field in ("repository", "branch", "commit", "public_files_sha256"):
        if receipt.get(field) != verified[field]:
            raise ValueError("GitHub sync checkpoint is stale; verify and record the current publication")
    verify_report(day, root)
    return receipt
