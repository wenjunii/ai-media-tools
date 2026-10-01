"""Requested same-day updates retain the original edition and email receipt."""

import copy
from pathlib import Path

from .configuration import load_config
from .report import verify_report
from .storage import ROOT, locked, now, read_json, report_date, sha256, write_json, write_text


def revision_number(value):
    if not isinstance(value, int) or isinstance(value, bool) or value < 2:
        raise ValueError("An updated edition needs an integer revision of at least 2")
    return value


def update_workspace(day, revision, root=ROOT):
    root = Path(root).resolve()
    day, revision = report_date(day), revision_number(revision)
    workspace = root / "state/report_updates" / day / f"r{revision}"
    if any(p.is_symlink() for p in [workspace, *workspace.parents]):
        raise ValueError("Update workspaces cannot use symbolic links")
    marker = read_json(workspace / "update.json")
    if (not isinstance(marker, dict) or marker.get("report_date") != day
            or marker.get("revision") != revision):
        raise ValueError("Prepare this update workspace before researching it")
    verify_report(day, root)
    if marker.get("original_manifest_sha256") != sha256(root / "reports" / day / "manifest.json"):
        raise ValueError("The original edition changed; preserve it before updating")
    return workspace


def prepare_update(day, revision=2, root=ROOT):
    root = Path(root).resolve()
    day, revision = report_date(day), revision_number(revision)
    with locked(root):
        verify_report(day, root)
        workspace = root / "state/report_updates" / day / f"r{revision}"
        if any(p.is_symlink() for p in [workspace, *workspace.parents]):
            raise ValueError("Update workspaces cannot use symbolic links")
        if (workspace / "update.json").exists():
            return update_workspace(day, revision, root)
        if workspace.exists() and any(workspace.iterdir()):
            raise ValueError("An unregistered update workspace already exists; preserve it")
        config = read_json(root / "config/scout.json")
        load_config(root)
        write_json(workspace / "config/scout.json", dict(config, edition_revision=revision))
        local = root / "config/scout.local.json"
        if local.exists():
            write_text(workspace / "config/scout.local.json", local.read_text())
        for name in ("catalog.json", "review_queue.json", "discovery_catalog.json"):
            write_json(workspace / "state" / name, read_json(root / "state" / name, {}))
        write_json(workspace / "update.json", {"report_date": day, "revision": revision,
                   "prepared_at": now(), "original_manifest_sha256":
                   sha256(root / "reports" / day / "manifest.json")})
        return workspace


def export_update(day, revision=2, root=ROOT):
    from .library import library_files, write_library_files
    from .publication import (_check_public_content, _finished_files, _public_editions,
                              _public_library_contents, _safe_path, verify_public_archive)
    root = Path(root).resolve()
    day, revision = report_date(day), revision_number(revision)
    with locked(root):
        workspace = update_workspace(day, revision, root)
        manifest = verify_report(day, workspace)
        if manifest.get("revision") != revision:
            raise ValueError("The sealed update must declare its prepared revision")
        config = load_config(root)
        if day not in _public_editions(root):
            raise ValueError("Publish the original edition before exporting its update")
        prefix = f"public/reports/{day}/updates/r{revision}"
        source = _finished_files(day, workspace, manifest)
        contents = {prefix + "/" + Path(name).name: value for name, value in source.items()}
        for name, content in contents.items():
            _check_public_content(content, root, config)
            _check_public_content(content, workspace, config)
            path = _safe_path(root, name)
            if path.exists() and path.read_bytes() != content:
                raise ValueError("An existing updated edition differs; preserve it and use a new revision")
        for name, content in contents.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        data, library = _public_library_contents(root, config)
        for name, content in library.items():
            _check_public_content(content, root, config)
            _safe_path(root, name)
        for name, content in library.items():
            write_text(_safe_path(root, name), content.decode("utf-8"))
        write_library_files(root / "site", library_files(data, "../public/reports/"))
        # Reuse the normal history-aware catalog operations; no delivery state is copied.
        from .discovery import update_discovery_catalog
        from .report import update_catalog, update_queue
        report = read_json(workspace / "reports" / day / "report.json")
        discovery = read_json(workspace / "research" / day / "discovery.json")
        catalog = read_json(root / "state/catalog.json", {})
        update_catalog(catalog, report, discovery, day)
        update_queue(root, report, discovery, day)
        write_json(root / "state/catalog.json", catalog)
        candidates = copy.deepcopy(discovery["candidates"])
        evidence_prefix = str(workspace.relative_to(root)) + "/"
        for candidate in candidates:
            if candidate.get("readme_path"):
                candidate["readme_path"] = evidence_prefix + candidate["readme_path"]
            if candidate.get("license_review", {}).get("path"):
                candidate["license_review"]["path"] = evidence_prefix + candidate["license_review"]["path"]
        update_discovery_catalog(root, day, candidates)
        verify_report(day, root)
        verify_report(day, workspace)
        verify_public_archive(root)
        return {"report_date": day, "revision": revision, "status": "exported",
                "profile_count": manifest["profile_count"], "lead_count": manifest.get("lead_count", 0),
                "files": list(contents) + list(library),
                "note": "Publish through the protected PR flow; the original email receipt remains unchanged"}
