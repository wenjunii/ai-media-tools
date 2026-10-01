"""A portable, cumulative library derived from finished daily reports."""

from html import escape
import json
from pathlib import Path
import re

from .report import LABELS, SECTIONS, safe_url
from .storage import edition_key, edition_revision, read_json, report_date, sha256, write_text

UI = Path(__file__).with_name("ui")
ASSETS = ("library.css", "library.js")
SECTION_FIELDS = {"text", "source_urls", "steps", "commands", "hardware", "software",
                  "platforms", "code", "weights", "commercial", "cost", "hands_on_tested"}
PLATFORMS = {"macOS": r"\b(?:macos|mac|apple silicon|os x)\b",
             "Windows": r"\bwindows\b", "Linux": r"\blinux\b",
             "Browser": r"\b(?:browser|webgpu|webgl|wasm|webassembly)\b",
             "XR / headset": r"\b(?:headset|webxr|vr|xr|visionos)\b",
             "Cloud": r"\b(?:cloud|colab|hosted)\b"}
SEARCH_COUNTS = ("fields", "planned_github_queries", "attempted_github_queries",
                 "successful_github_queries", "failed_github_queries", "partial_github_queries",
                 "truncated_github_queries", "planned_model_queries", "attempted_model_queries",
                 "failed_model_queries", "source_candidates", "model_candidates",
                 "full_profiles", "screened_leads", "ecosystems_searched", "ecosystem_gaps")


def _text(value):
    if not isinstance(value, str):
        raise ValueError("Library profile text must be a string")
    return value


def _profile(source, kind):
    """Keep only published creative guidance; never copy operational fields."""
    if not isinstance(source, dict):
        raise ValueError("Library profiles must be objects")
    output = {name: _text(source[name]) for name in ("id", "name", "checked_on")}
    report_date(output["checked_on"])
    categories = source.get("categories")
    if not isinstance(categories, list) or not categories or any(not isinstance(c, str) for c in categories):
        raise ValueError("Library profiles need creative fields")
    output["categories"] = categories
    output["sources"] = [{"title": _text(s["title"]), "url": safe_url(s["url"])} for s in source["sources"]]
    output["links"] = {name: safe_url(url) for name, url in source.get("links", {}).items()}
    if "ai_relevance" in source:
        output["ai_relevance"] = {"text": _text(source["ai_relevance"]["text"]),
                                  "source_urls": [safe_url(u) for u in source["ai_relevance"]["source_urls"]]}
    if kind == "screened":
        for name in ("good_for", "code_license", "review_status"):
            output[name] = _text(source[name])
        return output
    output["maturity"] = _text(source.get("maturity", "Documentation reviewed"))
    output["novelty"] = {name: _text(source["novelty"][name]) for name in ("kind", "text")}
    for name in SECTIONS:
        section = source[name]
        output[name] = {key: value for key, value in section.items() if key in SECTION_FIELDS}
        _text(output[name]["text"])
        output[name]["source_urls"] = [safe_url(u) for u in section["source_urls"]]
        for key in ("steps", "commands"):
            if key in section:
                output[name][key] = [_text(value) for value in section[key]]
        for key, value in output[name].items():
            if key not in {"text", "source_urls", "steps", "commands", "hands_on_tested"}:
                _text(value)
    return output


def make_library(documents, config):
    """Deduplicate tools by stable ID while retaining every published version."""
    names = {c["id"]: c["name"] for c in config["categories"]}
    tools, editions, dates, identities = {}, [], set(), set()
    for report in sorted(documents, key=lambda r: (r["report_date"], edition_revision(r.get("revision", 1)))):
        day = report_date(report["report_date"])
        revision = edition_revision(report.get("revision", 1))
        identity = edition_key(day, revision)
        if identity in identities:
            raise ValueError("Library editions must have unique dates and revisions")
        identities.add(identity)
        dates.add(day)
        names.update(report.get("category_labels", {}))
        editions.append({"report_date": day, "summary": _text(report["summary"]),
                         "profile_count": len(report["tools"]), "lead_count": len(report.get("leads", []))})
        if revision > 1:
            editions[-1].update(revision=revision, edition_id=identity,
                                report_directory=f"{day}/updates/r{revision}/")
        if report.get("search_coverage"):
            counts = {key: report["search_coverage"][key] for key in SEARCH_COUNTS}
            if any(not isinstance(v, int) or isinstance(v, bool) or v < 0 for v in counts.values()):
                raise ValueError("Published search coverage must contain nonnegative counts")
            editions[-1]["search_coverage"] = counts
        seen = set()
        for kind, profiles in (("profile", report["tools"]), ("screened", report.get("leads", []))):
            for source in profiles:
                profile = _profile(source, kind)
                key = profile["id"]
                if key in seen:
                    raise ValueError("A library edition contains a duplicate tool")
                seen.add(key)
                entry = tools.setdefault(key, {"id": key, "first_seen": day, "last_seen": day, "versions": []})
                entry["last_seen"] = day
                entry["versions"].insert(0, {"date": day, "kind": kind, "profile": profile})
                if revision > 1:
                    entry["versions"][0].update(revision=revision, edition_id=identity)
    for entry in tools.values():
        # A later brief mention never replaces an existing complete installation guide.
        primary = next((v for v in entry["versions"] if v["kind"] == "profile"), entry["versions"][0])
        profile = primary["profile"]
        entry.update(name=profile["name"], review=primary["kind"], profile_date=primary["date"],
                     license=profile["license"]["code"] if primary["kind"] == "profile" else profile["code_license"],
                     categories=sorted({c for v in entry["versions"] for c in v["profile"]["categories"]}))
        platform_text = " ".join(v["profile"].get("requirements", {}).get("platforms", "")
                                 for v in entry["versions"])
        entry["platform_mentions"] = [label for label, pattern in PLATFORMS.items()
                                      if re.search(pattern, platform_text, re.I)]
        for category in entry["categories"]:
            names.setdefault(category, category.replace("_", " ").replace("-", " ").title())
    used = {c for entry in tools.values() for c in entry["categories"]}
    profiles = sum(entry["review"] == "profile" for entry in tools.values())
    return {"format_version": 1, "latest_edition": max(dates) if dates else None,
            "counts": {"tools": len(tools), "profiles": profiles, "screened": len(tools) - profiles,
                       "editions": len(editions)},
            "categories": [{"id": c, "name": names[c]} for c in sorted(used, key=lambda c: names[c].casefold())],
            "section_labels": LABELS, "tools": sorted(tools.values(), key=lambda t: t["id"]),
            "editions": list(reversed(editions))}


def library_files(data, report_prefix="reports/"):
    """Return deterministic static files; relative URLs also work on project Pages."""
    serialized = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    # Source text is data, including literal HTML and command snippets.
    embedded = serialized.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    fallback = "<ul>" + "".join(
        '<li><a href="' + e.get("report_path", report_prefix + e.get("report_directory", e["report_date"] + "/")) + 'report.html">' +
        escape(e["report_date"] + (f" · Update {e['revision'] - 1}" if e.get("revision", 1) > 1 else "")) +
        " — " + str(e["profile_count"]) + " full profiles</a></li>"
        for e in data["editions"]) + "</ul>"
    html = (UI / "library.html").read_text().replace("{{LIBRARY_JSON}}", embedded)
    html = html.replace("{{REPORT_PREFIX}}", report_prefix).replace("{{REPORT_LINKS}}", fallback)
    output = {"index.html": html.encode("utf-8"), "library.json": serialized.encode("utf-8"),
              ".nojekyll": b""}
    output.update({"assets/" + name: (UI / name).read_bytes() for name in ASSETS})
    return output


def write_library_files(folder, files):
    for name, content in files.items():
        path = folder / name
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
            raise ValueError("Library output cannot use symbolic links")
        write_text(path, content.decode("utf-8"))


def write_local_library(root, config):
    """Update a local view from sealed reports plus previously public editions."""
    from .publication import _public_editions
    reports, paths = {}, {}
    for directory, metadata in _public_editions(root).items():
        identity = edition_key(metadata["report_date"], metadata.get("revision", 1))
        reports[identity] = read_json(root / "public/reports" / directory / "report.json")
        paths[identity] = "../public/reports/" + directory + "/"
    for path in sorted((root / "reports").glob("*/manifest.json")):
        manifest = read_json(path)
        day = report_date(path.parent.name)
        if manifest["report_date"] != day:
            raise ValueError("Local library report date disagrees with its seal")
        for name in ("report.html", "report.md", "report.json"):
            report_path = path.parent / name
            if sha256(report_path) != manifest["sha256"].get(f"reports/{day}/{name}"):
                raise ValueError("Local library report differs from its seal")
        identity = edition_key(day, manifest.get("revision", 1))
        reports[identity] = read_json(path.parent / "report.json")
        paths[identity] = "../reports/" + day + "/"
    data = make_library(list(reports.values()), config)
    for edition in data["editions"]:
        identity = edition_key(edition["report_date"], edition.get("revision", 1))
        edition["report_path"] = paths[identity]
    write_library_files(root / "site", library_files(data, "../reports/"))
    return data
