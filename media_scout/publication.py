"""Publishable report exports and verified GitHub checkpoints before email.

Git commits, pull requests and merges are performed by the research agent. These
commands export only finished reports and verify the actual remote commit and CI;
an edited local receipt alone cannot authorize delivery.
"""

import hashlib
import json
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess

from .configuration import load_config
from .library import library_files, make_library, write_library_files
from .report import verify_report
from .storage import ROOT, edition_revision, locked, now, read_json, report_date, write_json, write_text

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
    if manifest.get("revision", 1) > 1:
        public_manifest["revision"] = edition_revision(manifest["revision"])
    contents[f"{prefix}/publication.json"] = _json_bytes(public_manifest)
    return contents


def _public_editions(root):
    directory = _safe_path(root, "public/reports")
    if not directory.exists():
        return {}
    if not directory.is_dir():
        raise ValueError("The public report archive must be a directory")
    editions = {}
    for folder in sorted(directory.iterdir(), reverse=True):
        if folder.name == ".DS_Store":
            continue
        _safe_path(root, str(folder.relative_to(root)))
        try:
            day = report_date(folder.name)
        except ValueError as error:
            raise ValueError("Public edition directories must use YYYY-MM-DD dates") from error
        expected_names = set(REPORT_FILES) | {"publication.json"}
        actual_names = {p.name for p in folder.iterdir() if p.name != ".DS_Store"} if folder.is_dir() else set()
        if not folder.is_dir() or actual_names - {"updates"} != expected_names:
            raise ValueError("Public edition is missing required files or contains extra material")
        editions[day] = _verify_public_folder(root, folder, day)
        if "updates" in actual_names:
            updates = _safe_path(root, str((folder / "updates").relative_to(root)))
            if not updates.is_dir():
                raise ValueError("Public updates must be a directory of revision folders")
            for update in sorted(updates.iterdir()):
                if update.name == ".DS_Store":
                    continue
                match = re.fullmatch(r"r([0-9]+)", update.name)
                if not match or int(match[1]) < 2 or update.name != f"r{int(match[1])}":
                    raise ValueError("Public update directories must use revisions r2 and above")
                key = f"{day}/updates/{update.name}"
                editions[key] = _verify_public_folder(root, update, day, int(match[1]))
    return editions


def _verify_public_folder(root, folder, day, revision=1):
    _safe_path(root, str(folder.relative_to(root)))
    expected_names = set(REPORT_FILES) | {"publication.json"}
    actual_names = {p.name for p in folder.iterdir() if p.name != ".DS_Store"} if folder.is_dir() else set()
    if actual_names - ({"updates"} if revision == 1 else set()) != expected_names:
        raise ValueError("Public edition is missing required files or contains extra material")
    for name in expected_names:
        if not _safe_path(root, str((folder / name).relative_to(root))).is_file():
            raise ValueError("Public edition files must be regular files")
    metadata = read_json(folder / "publication.json")
    fields = {"report_date", "sealed_at", "profile_count", "lead_count", "sha256"}
    if revision > 1:
        fields.add("revision")
    if (not isinstance(metadata, dict) or set(metadata) != fields or metadata["report_date"] != day
            or edition_revision(metadata.get("revision", 1)) != revision):
        raise ValueError("Public publication metadata has an invalid date or schema")
    for name in ("profile_count", "lead_count"):
        value = metadata[name]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Public edition counts must be nonnegative integers")
    try:
        sealed = metadata["sealed_at"]
        if not isinstance(sealed, str) or datetime.fromisoformat(sealed.replace("Z", "+00:00")).tzinfo is None:
            raise ValueError("Invalid timestamp")
    except ValueError as error:
        raise ValueError("Public edition seal time must include a valid time-zone offset") from error
    hashes = metadata["sha256"]
    if not isinstance(hashes, dict) or set(hashes) != set(REPORT_FILES):
        raise ValueError("Public publication hashes must cover exactly the finished report files")
    for name, expected in hashes.items():
        if not isinstance(expected, str) or not re.fullmatch(r"[a-f0-9]{64}", expected):
            raise ValueError("Public publication hashes must be SHA-256 digests")
        if _digest((folder / name).read_bytes()) != expected:
            raise ValueError("Public report content does not match its publication hash")
    report = read_json(folder / "report.json")
    if (not isinstance(report, dict) or report.get("report_date") != day
            or edition_revision(report.get("revision", 1)) != revision
            or not isinstance(report.get("tools"), list) or not isinstance(report.get("leads", []), list)
            or len(report["tools"]) != metadata["profile_count"]
            or len(report.get("leads", [])) != metadata["lead_count"]):
        raise ValueError("Public report date or profile counts disagree with publication metadata")
    return metadata


def _readme_for_editions(editions):
    lines = ["# Daily reports", "", "Finished AI Media Scout editions, with full profiles and primary-source citations.",
             "", "[Searchable HTML library](index.html). Browse with GitHub Pages or open locally.", "",
             "| Date | Full profiles | Additional discoveries | Editions |",
             "| --- | ---: | ---: | --- |"]
    for day, metadata in sorted(editions.items(), reverse=True):
        profiles, leads = metadata["profile_count"], metadata["lead_count"]
        links = " · ".join(f"[{label}](reports/{day}/{name})" for label, name in
                           (("Markdown", "report.md"), ("HTML", "report.html"), ("JSON", "report.json")))
        label = metadata["report_date"] + (f" · Update {metadata['revision'] - 1}" if metadata.get("revision", 1) > 1 else "")
        lines.append(f"| {label} | {profiles} | {leads} | {links} |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _archive_readme(root):
    return _readme_for_editions(_public_editions(root))


def _public_library_contents(root, config=None):
    editions = _public_editions(root)
    documents = [read_json(root / "public/reports" / day / "report.json") for day in editions]
    data = make_library(documents, config or load_config(root))
    contents = {"public/" + name: value for name, value in library_files(data).items()}
    contents["public/README.md"] = _readme_for_editions(editions)
    return data, contents


def rebuild_library(root=ROOT):
    """Refresh derived local/public views; never rebuild or export a sealed report."""
    root = Path(root).resolve()
    with locked(root):
        config = load_config(root)
        data, contents = _public_library_contents(root, config)
        for name, content in contents.items():
            _safe_path(root, name)
            _check_public_content(content, root, config)
        for name, content in contents.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        write_library_files(root / "site", library_files(data, "../public/reports/"))
        return {"status": "built", "tools": data["counts"]["tools"],
                "editions": data["counts"]["editions"], "files": list(contents),
                "note": "Derived library refreshed; sealed reports and delivery records preserved"}


class _ReportLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == "href" and value and value.lower().startswith(("reports/", "../reports/")):
                self.targets.append(value)


def verify_public_archive(root=ROOT):
    """Validate every public edition without local research, GitHub access or writes."""
    root = Path(root).resolve()
    editions = _public_editions(root)
    readme = _safe_path(root, "public/README.md")
    index = _safe_path(root, "public/index.html")
    if editions or readme.exists():
        if not readme.is_file() or readme.read_bytes() != _readme_for_editions(editions):
            raise ValueError("Public archive README does not match the verified editions")
    if editions and not index.is_file():
        raise ValueError("The public archive is missing its searchable index")
    if index.exists():
        if not index.is_file():
            raise ValueError("The public searchable index must be a regular file")
        parser = _ReportLinks()
        parser.feed(index.read_text())
        for target in parser.targets:
            match = re.fullmatch(r"reports/(\d{4}-\d{2}-\d{2}(?:/updates/r[0-9]+)?)/(report\.(?:html|md|json))", target)
            if not match or match[1] not in editions:
                raise ValueError("The public searchable index links to an unpublished or invalid edition")
    data, contents = _public_library_contents(root)
    for name, expected in contents.items():
        path = _safe_path(root, name)
        if not path.is_file() or path.read_bytes() != expected:
            raise ValueError("Published library differs from finished editions; run build-library")
    return {"status": "passed", "editions": len(editions), "report_files_checked": len(editions) * len(REPORT_FILES),
            "library_tools": data["counts"]["tools"]}


def export_report(day, root=ROOT):
    root = Path(root).resolve()
    day = report_date(day)
    with locked(root):
        manifest = verify_report(day, root)
        config = load_config(root)
        contents = _finished_files(day, root, manifest)
        for name, content in contents.items():
            _check_public_content(content, root, config)
            path = _safe_path(root, name)
            if path.exists() and path.read_bytes() != content:
                raise ValueError("An existing public edition differs from the sealed report; preserve it")
        for name, content in contents.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        data, library = _public_library_contents(root, config)
        for name, content in library.items():
            _safe_path(root, name)
            _check_public_content(content, root, config)
        for name, content in library.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        contents.update(library)
        write_library_files(root / "site", library_files(data, "../public/reports/"))
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
    archive = verify_public_archive(root)
    prior = set(_run(["git", "ls-tree", "-r", "--name-only", "HEAD", "--", "public/reports"], root).decode().splitlines())
    indexed = set(filter(None, names))
    for name in prior:
        if name not in indexed or _run(["git", "show", "HEAD:" + name], root) != _run(["git", "show", ":" + name], root):
            raise ValueError("Published editions are immutable; preserve existing files when syncing")
    return {"status": "passed", "tracked_files_checked": count, "public_editions_checked": archive["editions"]}


def _github_settings(config):
    settings = config.get("github_sync", {})
    repository = settings.get("repository", "")
    branch = settings.get("branch", "main")
    workflow = settings.get("ci_workflow", "ci.yml")
    if not isinstance(repository, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*/[A-Za-z0-9][A-Za-z0-9._-]*", repository):
        raise ValueError("Configure github_sync.repository as OWNER/REPO")
    if not isinstance(branch, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", branch) or ".." in branch:
        raise ValueError("Configure a valid GitHub publication branch")
    if not isinstance(workflow, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*\.ya?ml", workflow):
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
    _, library = _public_library_contents(root, config)
    contents.update(library)
    for key, metadata in _public_editions(root).items():
        if metadata.get("revision", 1) > 1:
            contents.update({f"public/reports/{key}/{name}": (root / "public/reports" / key / name).read_bytes()
                             for name in REPORT_FILES + ("publication.json",)})
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
        path = root / "state/publications" / (day + ".json")
        prior = read_json(path)
        if prior and prior.get("commit") != receipt["commit"]:
            previous = path.read_bytes()
            history = root / "state/publication_history" / day / (_digest(previous) + ".json")
            if history.exists() and history.read_bytes() != previous:
                raise ValueError("Publication history conflicts with the existing checkpoint; preserve it")
            write_text(history, previous.decode("utf-8"))
        write_json(path, receipt)
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
