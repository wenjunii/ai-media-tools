"""Archive primary evidence for open-source AI projects hosted beyond GitHub.

The research agent reads the official sources and saves snapshots first.
This command performs no network reads or execution of discovered software.
"""

import hashlib
from pathlib import Path
from urllib.parse import urlparse, urlunparse

from .discovery import OSI_LICENSES, fingerprint, novelty, priority_score, update_discovery_catalog
from .configuration import load_config
from .report import safe_url
from .storage import ROOT, locked, now, read_json, report_date, sha256, write_json


def evidence_file(root, day, value):
    path = (root / value).resolve()
    evidence = (root / "research" / day / "evidence").resolve()
    if not path.is_relative_to(evidence) or not path.is_file() or path.stat().st_size > 2_000_000:
        raise ValueError("External evidence must be an existing daily evidence file under 2 MB")
    if not path.read_text(encoding="utf-8").strip():
        raise ValueError("Source evidence must not be empty")
    return path


def add_project(metadata_path, day=None, root=ROOT):
    root = Path(root).resolve()
    config = load_config(root)
    day = report_date(day, config["timezone"])
    meta = read_json(metadata_path)
    if not isinstance(meta, dict):
        raise ValueError("Read an external-project metadata JSON file")
    parsed = urlparse(safe_url(meta["project_url"]))
    if parsed.query or parsed.fragment:
        raise ValueError("Use a canonical project URL without tracking queries or fragments")
    url = urlunparse(parsed._replace(netloc=parsed.netloc.lower(), path=parsed.path.rstrip("/")))
    if parsed.hostname in {"github.com", "www.github.com"}:
        raise ValueError("Use add-repository for GitHub projects")
    if (not meta.get("name") or meta.get("code_license") not in OSI_LICENSES
            or len(meta.get("ai_relevance", "").strip()) < 30):
        raise ValueError("Require a name, reviewed open-source SPDX license, and concrete creative AI use")
    with locked(root):
        if (root / "reports" / day / "manifest.json").exists():
            raise ValueError("This day's source observation is sealed")
        observation_path = root / "research" / day / "discovery.json"
        observation = read_json(observation_path)
        if not observation:
            raise ValueError("Run discover first")
        categories = meta.get("categories", [])
        known = {c["id"] for c in observation.get("categories", config["categories"])}
        if not categories or not set(categories).issubset(known):
            raise ValueError("Use category IDs from this day's search plan")
        overview, license_info = meta["overview"], meta["license"]
        overview_path = evidence_file(root, day, overview["path"])
        license_path = evidence_file(root, day, license_info["path"])
        if license_info.get("reviewed") is not True or len(license_info.get("note", "").strip()) < 30:
            raise ValueError("Read the complete license and record a substantive review")
        overview_url, license_url = safe_url(overview["url"]), safe_url(license_info["url"])
        key = "external:" + url
        item = {"id": key, "name": meta["name"], "repository": url, "url": url,
                "description": meta.get("description", ""), "categories": categories,
                "ai_relevance": meta["ai_relevance"], "code_license": meta["code_license"],
                "license_status": "open-source-license-reviewed", "stars": 0,
                "archived": False, "fork": False, "created_at": meta.get("created_at"),
                "readme_path": str(overview_path.relative_to(root)), "readme_sha256": sha256(overview_path),
                "discovered_by": ["supplementary-primary-source-web-research"],
                "evidence": [{"title": "Official project documentation", "url": overview_url, "checked_at": now()},
                             {"title": "Reviewed software license", "url": license_url, "checked_at": now()}],
                "license_review": {"original_spdx": "UNKNOWN", "reviewed_spdx": meta["code_license"],
                                   "note": license_info["note"], "url": license_url, "checked_at": now(),
                                   "path": str(license_path.relative_to(root)), "sha256": sha256(license_path)}}
        if meta.get("latest_release"):
            release = dict(meta["latest_release"])
            safe_url(release["url"])
            if not release.get("tag"):
                raise ValueError("A release observation needs its actual version tag")
            item["latest_release"] = release
        item["source_fingerprint"] = fingerprint(item)
        catalog = read_json(root / "state/catalog.json", {})
        item["novelty"] = novelty(item, catalog.get(key), observation["window_start"])
        item["discovery_priority"] = priority_score(item)
        digest = hashlib.sha256(url.encode()).hexdigest()[:16]
        write_json(root / "research" / day / "evidence" / ("external-" + digest + ".json"), meta)
        observation["candidates"] = [c for c in observation["candidates"] if c["id"] != key] + [item]
        observation["supplemented_at"] = now()
        write_json(observation_path, observation)
        update_discovery_catalog(root, day, [item])
        return item
