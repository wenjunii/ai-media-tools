"""Local housekeeping: remove disposable files, never the research archive."""

from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import time
import uuid
from urllib.parse import urlparse

from .storage import ROOT, locked, read_json, report_date, sha256, write_json

DAY = 86_400
METADATA_DAYS = 7
CACHE_DAYS = 60
TEMP_DAYS = 1
COUNTERS = {"unique_metadata", "observed", "unpublished", "observed_count",
            "observed_unique", "matched", "count", "total", "total_count"}
COLLECTIONS = {"records", "candidates", "matches", "items", "repos", "repositories"}


def _relative(value):
    if not isinstance(value, str):
        raise ValueError("Unsafe path in a sealed manifest; cleanup refused")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("Unsafe path in a sealed manifest; cleanup refused")
    return path.as_posix()


def _regular(root, path, *, single_link=True):
    """Never follow a symlink or remove a multiply linked file."""
    try:
        rel = path.relative_to(root)
        if any((root / Path(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1)):
            return None
        info = path.lstat()
        return info if stat.S_ISREG(info.st_mode) and (not single_link or info.st_nlink == 1) else None
    except FileNotFoundError:
        return None


def _identity(info):
    return [info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns]


def _sealed(root):
    protected, editions, manifests = {}, {}, {}
    reports = root / "reports"
    if reports.is_symlink():
        raise ValueError("Symlinked report archive; cleanup refused")
    for folder, dirs, names in os.walk(reports, followlinks=False):
        if any((Path(folder) / d).is_symlink() for d in dirs):
            raise ValueError("Symlinked report archive; cleanup refused")
        if "manifest.json" not in names:
            continue
        path = Path(folder) / "manifest.json"
        if not _regular(root, path, single_link=False):
            raise ValueError("Unsafe sealed manifest; cleanup refused")
        raw = path.read_bytes()
        value = json.loads(raw)
        hashes = value.get("sha256")
        if not isinstance(hashes, dict) or not hashes:
            raise ValueError("Incomplete sealed manifest; cleanup refused")
        rel = path.relative_to(root).as_posix()
        manifests[rel] = hashlib.sha256(raw).hexdigest()
        protected[rel] = manifests[rel]
        for name, digest in hashes.items():
            name = _relative(name)
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ValueError("Invalid sealed hash; cleanup refused")
            if name in protected and protected[name] != digest:
                raise ValueError("Conflicting sealed hashes; cleanup refused")
            protected[name] = digest
        day = value.get("report_date")
        if path == root / "reports" / str(day) / "manifest.json":
            report_date(day)
            editions[day] = (rel, hashes)
    return protected, editions, manifests


def _tracked(root):
    if not (root / ".git").exists():
        return set()
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, timeout=30)
    if result.returncode:
        raise RuntimeError("Cannot inspect the Git index; cleanup refused")
    return set(result.stdout.decode("utf-8").split("\0")) - {""}


def _record_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")).encode()).hexdigest()


def _records(value):
    """Recognize raw metadata copies, rejecting annotations and unknown wrappers."""
    if isinstance(value, list):
        rows = value
    elif isinstance(value, dict):
        keys = set(value) & COLLECTIONS
        if len(keys) == 1 and set(value) - keys <= COUNTERS:
            if not all(isinstance(value[k], int) and not isinstance(value[k], bool)
                       and value[k] >= 0 for k in set(value) - keys):
                return None
            rows = value[next(iter(keys))]
            if isinstance(rows, dict) and rows and all(
                    isinstance(v, dict) and isinstance(v.get("full_name"), str)
                    and k.casefold() == v["full_name"].casefold() for k, v in rows.items()):
                rows = list(rows.values())
        elif value and all(isinstance(v, dict) and isinstance(v.get("full_name"), str)
                           and k.casefold() == v["full_name"].casefold() for k, v in value.items()):
            rows = list(value.values())
        else:
            return None
    else:
        return None
    if not isinstance(rows, list) or not rows or not all(
            isinstance(v, dict) and isinstance(v.get("full_name"), str) for v in rows):
        return None
    return rows


def _source_records(root, day, hashes):
    records, sources = set(), {}
    prefix = f"research/{day}/queries/"
    for rel, expected in hashes.items():
        if not rel.startswith(prefix) or not rel.endswith(".json"):
            continue
        path = root / rel
        info = _regular(root, path, single_link=False)
        if info is None or sha256(path) != expected:
            raise ValueError("Sealed query changed; cleanup refused")
        value = read_json(path)
        if isinstance(value, dict) and isinstance(value.get("items"), list):
            for item in value["items"]:
                if isinstance(item, dict) and isinstance(item.get("full_name"), str):
                    records.add(_record_digest(item))
            sources[rel] = expected
    return records, sources


def _plan(root, day, stamp):
    protected, editions, manifests = _sealed(root)
    protected.update({p: None for p in _tracked(root)})
    deliveries = root / "state/deliveries"
    if deliveries.is_symlink():
        raise ValueError("Unsafe delivery directory; cleanup refused")
    for receipt in deliveries.glob("*.json"):
        if not _regular(root, receipt, single_link=False):
            raise ValueError("Unsafe delivery receipt; cleanup refused")
        if read_json(receipt).get("status") in {"reserved", "uncertain"}:
            raise RuntimeError("Pending delivery reconciliation; cleanup refused")
    for edition in editions:
        receipt = root / "state/deliveries" / (edition + ".json")
        publication = root / "state/publications" / (edition + ".json")
        if (not _regular(root, receipt, single_link=False) or not _regular(root, publication, single_link=False)
                or read_json(receipt).get("status") != "sent"
                or read_json(publication).get("status") != "synced"):
            raise RuntimeError("Unfinished sealed edition/publication; cleanup refused")
    research = root / "research"
    if research.is_symlink():
        raise ValueError("Symlinked research archive; cleanup refused")
    for folder in research.glob("????-??-??"):
        if folder.is_symlink():
            raise ValueError("Symlinked research observation; cleanup refused")
        if folder.is_dir() and folder.name not in editions and any(folder.iterdir()):
            raise RuntimeError("Unfinished dated research; cleanup refused")
    cache_path = root / "state/cleanup/kept-metadata.json"
    try:
        cached = read_json(cache_path, {}) if _regular(root, cache_path) else {}
    except (ValueError, UnicodeError):
        cached = {}
    kept = cached.get("files", {}) if isinstance(cached, dict) and cached.get("version") == 1 else {}
    kept = kept if isinstance(kept, dict) else {}
    entries, proofs, skipped = [], {}, 0

    def add(path, kind, minimum_age, **extra):
        rel = path.relative_to(root).as_posix()
        info = _regular(root, path)
        if rel in protected or info is None or stamp - info.st_mtime < minimum_age * DAY:
            return False
        entries.append(dict(path=rel, kind=kind, bytes=info.st_size,
                            identity=_identity(info), sha256=sha256(path), **extra))
        return True

    # These trees contain generated caches only. Never scan PC runtimes,
    # virtual environments, archived evidence, report updates or Git storage.
    for base in [root / "media_scout", root / "tests", root / "pc_demo"]:
        if base.is_symlink():
            continue
        for folder, dirs, files in os.walk(base, followlinks=False):
            dirs[:] = [d for d in dirs if d not in {".local", ".venv", "node_modules"}
                       and not (Path(folder) / d).is_symlink()]
            for name in files:
                path = Path(folder) / name
                if path.parent.name == "__pycache__" and path.suffix == ".pyc":
                    add(path, "python-bytecode", TEMP_DAYS)
                elif name == ".DS_Store":
                    add(path, "finder-metadata", TEMP_DAYS)
    add(root / ".DS_Store", "finder-metadata", TEMP_DAYS)
    cache = root / "state/http-cache"
    if not cache.is_symlink():
        for path in cache.glob("*.json"):
            if re.fullmatch(r"[0-9a-f]{64}\.json", path.name):
                info = _regular(root, path)
                if info and info.st_size <= 3_000_000 and stamp - info.st_mtime >= CACHE_DAYS * DAY:
                    try:
                        entry = read_json(path)
                        url = entry.get("url")
                        parsed = urlparse(url) if isinstance(url, str) else None
                        if (entry.get("version") == 1 and isinstance(url, str)
                                and set(entry) == {"version", "url", "etag", "sha256", "body"}
                                and parsed.scheme == "https" and parsed.netloc == "api.github.com"
                                and re.fullmatch(r"/repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
                                                 r"(?:/readme|/license|/releases|/commits)?", parsed.path)
                                and parsed.query in {"", "per_page=1"} and not parsed.fragment
                                and path.stem == hashlib.sha256(url.encode()).hexdigest()):
                            add(path, "unused-http-cache", CACHE_DAYS)
                    except (ValueError, AttributeError, UnicodeError):
                        pass
    for base in [root / "state", cache]:
        if not base.is_symlink():
            for path in base.glob(".scout-*"):
                if re.fullmatch(r"\.scout-[a-z0-9_]{8}", path.name):
                    add(path, "abandoned-atomic-write", TEMP_DAYS)

    # Delete only complete copies of raw repository metadata whose every record
    # is independently present in this edition's hash-verified sealed queries.
    for edition, (manifest, hashes) in sorted(editions.items()):
        if (date.fromisoformat(day) - date.fromisoformat(edition)).days < METADATA_DAYS:
            continue
        receipt = root / "state/deliveries" / (edition + ".json")
        publication = root / "state/publications" / (edition + ".json")
        if (not _regular(root, receipt, single_link=False) or not _regular(root, publication, single_link=False)
                or read_json(receipt).get("status") != "sent"
                or read_json(publication).get("status") != "synced"):
            continue
        folder = root / "research" / edition
        if folder.is_symlink():
            continue
        candidates = [p for p in folder.glob("*metadata*.json")
                      if p.relative_to(root).as_posix() not in protected
                      and _regular(root, p) and stamp - p.stat().st_mtime >= TEMP_DAYS * DAY]
        if not candidates:
            continue
        records, sources = None, None
        for path in candidates:
            rel = path.relative_to(root).as_posix()
            signature = {"sha256": sha256(path), "manifest_sha256": manifests[manifest]}
            # This cache can only retain a file. A stale or forged entry can
            # never authorize deletion or replace a source-provenance check.
            if kept.get(rel) == signature:
                skipped += 1
                continue
            try:
                rows = _records(read_json(path))
            except (ValueError, UnicodeError):
                rows = None
            if not rows:
                skipped += 1
                kept[rel] = signature
                continue
            if records is None:
                records, sources = _source_records(root, edition, hashes)
            if not all(_record_digest(row) in records for row in rows):
                skipped += 1
                kept[rel] = signature
                continue
            kept.pop(rel, None)
            if add(path, "redundant-query-metadata", TEMP_DAYS, edition=edition, records=len(rows)):
                proofs[manifest] = {"manifest_sha256": manifests[manifest], "source_queries": sources}
    return entries, proofs, manifests, skipped, kept


def cleanup(day=None, root=ROOT, *, apply=False, stamp=None):
    """Preview by default; apply recomputes the plan under Scout's idle lock."""
    root = Path(root).resolve()
    day = report_date(day)
    stamp = time.time() if stamp is None else stamp
    if (root / "state").is_symlink() or (root / "state/cleanup").is_symlink():
        raise ValueError("Unsafe cleanup state directory; cleanup refused")
    with locked(root):
        entries, proofs, manifests, skipped, kept = _plan(root, day, stamp)
        output = {"status": "applied" if apply else "preview", "as_of": day,
                  "retention_days": {"metadata": METADATA_DAYS, "unused_cache": CACHE_DAYS,
                                     "temporary": TEMP_DAYS},
                  "candidate_files": len(entries), "candidate_bytes": sum(p["bytes"] for p in entries),
                  "unproven_metadata_kept": skipped, "deleted_files": 0, "deleted_bytes": 0,
                  "candidates": entries, "proofs": proofs, "errors": []}
        if not apply:
            return output
        # Recheck provenance before any removal. An interrupted or uncertain
        # delivery is never a reason to change recovery files or retry a send.
        for rel, digest in manifests.items():
            if not _regular(root, root / rel, single_link=False) or sha256(root / rel) != digest:
                raise ValueError("Sealed manifest changed during cleanup planning")
        for proof in proofs.values():
            for rel, digest in proof["source_queries"].items():
                if not _regular(root, root / rel, single_link=False) or sha256(root / rel) != digest:
                    raise ValueError("Sealed query changed during cleanup planning")
        journal = root / "state/cleanup" / (
            datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:12] + ".json")
        output["receipt"] = journal.relative_to(root).as_posix()
        output["status"] = "in-progress"
        write_json(journal, output)
        for number, entry in enumerate(entries, 1):
            path = root / entry["path"]
            try:
                info = _regular(root, path)
                if info is None or _identity(info) != entry["identity"] or sha256(path) != entry["sha256"]:
                    raise RuntimeError("Candidate changed; kept")
                path.unlink()
                entry["deleted"] = True
                output["deleted_files"] += 1
                output["deleted_bytes"] += entry["bytes"]
            except (OSError, RuntimeError) as error:
                output["errors"].append({"path": entry["path"], "reason": str(error)})
            if number % 25 == 0 or output["errors"]:
                write_json(journal, output)
        output["status"] = "partial" if output["errors"] else "applied"
        write_json(journal, output)
        write_json(root / "state/cleanup/kept-metadata.json", {"version": 1, "files": kept})
        return output
