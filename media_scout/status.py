"""Read-only inspection of original reports, updates and the public library."""

from pathlib import Path
import re

from .publication import REPORT_FILES, _public_editions, verify_public_archive
from .report import verify_report
from .storage import ROOT, edition_key, edition_revision, read_json, report_date
from .updates import revision_number, update_workspace


def _local_updates(day, root):
    directory = root / "state/report_updates" / day
    if any(path.is_symlink() for path in [directory, *directory.parents]):
        raise ValueError("Update workspaces cannot use symbolic links")
    if not directory.exists():
        return {}
    if not directory.is_dir():
        raise ValueError("Local updates must be a directory of prepared revisions")
    workspaces = {}
    for path in directory.iterdir():
        if path.name == ".DS_Store":
            continue
        match = re.fullmatch(r"r([0-9]+)", path.name)
        if not match or int(match[1]) < 2 or path.name != f"r{int(match[1])}" or not path.is_dir():
            raise ValueError("Local update directories must use revisions r2 and above")
        revision = int(match[1])
        workspaces[revision] = update_workspace(day, revision, root)
    return workspaces


def _edition_status(day, revision, workspace, metadata, root):
    observation = read_json(workspace / "research" / day / "discovery.json") if workspace else None
    manifest_path = workspace / "reports" / day / "manifest.json" if workspace else None
    manifest = verify_report(day, workspace) if manifest_path and manifest_path.exists() else None
    if manifest and (manifest.get("report_date") != day
                     or edition_revision(manifest.get("revision", 1)) != revision):
        raise ValueError("The sealed edition must match its report date and prepared revision")
    if manifest and metadata and any(
            manifest["sha256"].get(f"reports/{day}/{name}") != metadata["sha256"][name]
            for name in REPORT_FILES):
        raise ValueError("Local and public editions differ; preserve the sealed reports")
    counts = manifest or metadata or {}
    directory = day if revision == 1 else f"{day}/updates/r{revision}"
    report_path = workspace / "reports" / day / "report.json" if manifest else None
    if not report_path and metadata:
        report_path = root / "public/reports" / directory / "report.json"
    report = read_json(report_path) if report_path else {}
    return {"report_date": day, "revision": revision, "edition_id": edition_key(day, revision),
            "prepared": revision > 1 and workspace is not None,
            "discovered": bool(observation), "built": bool(manifest), "exported": bool(metadata),
            "profile_count": counts.get("profile_count"),
            "lead_count": counts.get("lead_count", 0) if counts else None,
            "public_report": f"public/reports/{directory}/report.html" if metadata else None,
            "search_coverage": report.get("search_coverage"),
            "warnings": observation.get("warnings", []) if observation else []}


def report_status(day, root=ROOT, revision=None):
    """Verify saved artifacts without collecting, writing or contacting GitHub.

    Top-level counts describe the selected edition (the original by default).
    The latest completed edition and cumulative published library are explicit.
    Publication receipts are stored checkpoints, not fresh remote verification.
    """
    root, day = Path(root).resolve(), report_date(day)
    if revision is not None:
        revision = revision_number(revision)
    public_editions = _public_editions(root)
    library = None
    if (root / "public").exists():
        verify_public_archive(root)
        data = read_json(root / "public/library.json")
        library = dict(data["counts"], latest_report_date=data["latest_edition"],
                       source="public", verified=True)
    metadata = {value.get("revision", 1): value for value in public_editions.values()
                if value["report_date"] == day}
    workspaces = _local_updates(day, root)
    revisions = sorted({1, *metadata, *workspaces})
    editions = [_edition_status(day, value, root if value == 1 else workspaces.get(value),
                               metadata.get(value), root) for value in revisions]
    selected = next((edition for edition in editions if edition["revision"] == (revision or 1)), None)
    if selected is None:
        raise ValueError("Prepare this update workspace or restore its published edition before inspecting it")
    completed = [edition for edition in editions if edition["built"] or edition["exported"]]
    return {"report_date": day, "revision": selected["revision"], "edition_id": selected["edition_id"],
            "discovered": selected["discovered"], "built": selected["built"],
            "delivery": read_json(root / "state/deliveries" / (day + ".json")) if revision is None else None,
            "publication": read_json(root / "state/publications" / (day + ".json")),
            "publication_remote_checked": False,
            "profile_count": selected["profile_count"], "lead_count": selected["lead_count"],
            "warnings": selected["warnings"], "editions": editions,
            "latest_completed_edition": completed[-1] if completed else None, "library": library}
