"""Evidence-based quality labels, independent of popularity and profile length."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlparse

from .storage import read_json, report_date, write_json, locked

TIERS = {"recommended": "Recommended", "ready_to_try": "Ready to try",
         "unverified": "Quality unverified", "experimental": "Experimental"}
CHECKS = {"license": "Open-source software license", "results": "Creative results",
          "setup": "Reproducible setup", "maintenance": "Maintenance and support",
          "independent_use": "Independent use", "dependencies": "Models, services and costs"}
METHODS = {"source-review": "Source review; no local execution implied",
           "published-record-audit": "Reassessment of existing published evidence",
           "unassessed": "Evidence review pending"}
REVIEW_ACTIONS = {
    "license": "Review and archive the complete current software license for the scoped workflow.",
    "results": "Review cited creative outputs and their limitations for this workflow; our own demo is not required.",
    "setup": "Check current installation and first-use instructions, versions and documented platform requirements.",
    "maintenance": "Review current releases, support responses and unresolved issues affecting this workflow.",
    "independent_use": "Find and review first-hand use or integration by someone independent of the maintainer.",
    "dependencies": "Verify required models, weight terms, proprietary hosts, paid services and costs separately.",
}
REVIEW_QUEUES = {
    "failed_checks": "Resolve documented failed checks",
    "results_review": "Review creative results",
    "evidence_review": "Complete evidence review",
    "profile_needed": "Complete the latest profile",
    "experimental_review": "Reassess the cited experimental limitation",
}


def _text(value, minimum=1):
    if not isinstance(value, str) or len(value.strip()) < minimum:
        raise ValueError("Quality assessments require meaningful text")
    return value


def _url(value):
    if not isinstance(value, str):
        raise ValueError("Quality sources must be HTTPS URLs")
    url = urlparse(value)
    if url.scheme != "https" or not url.hostname or url.username or url.password:
        raise ValueError("Quality sources must be HTTPS URLs without credentials")
    return value


def validate_assessment(value, kind="profile", expected_date=None):
    """Reject unsupported recommendations; return only public review fields."""
    if not isinstance(value, dict) or value.get("tier") not in TIERS:
        raise ValueError("Quality assessment needs a recognized tier")
    if value.get("method") not in {"source-review", "published-record-audit"}:
        raise ValueError("Quality assessment needs an explicit review method")
    day = report_date(_text(value.get("checked_on")))
    if expected_date and day != expected_date:
        raise ValueError("Quality assessment must be checked on the edition date")
    output = {key: _text(value.get(key)) for key in ("tier", "method", "checked_on", "summary", "scope")}
    caveats = value.get("caveats")
    if not isinstance(caveats, list) or not caveats:
        raise ValueError("Quality assessment must disclose its testing scope and limitations")
    output["caveats"] = [_text(note) for note in caveats]
    sources = value.get("sources")
    if not isinstance(sources, list):
        raise ValueError("Quality assessment needs a source list")
    output["sources"] = [{"title": _text(s.get("title")), "url": _url(s.get("url"))}
                         for s in sources if isinstance(s, dict)]
    if len(output["sources"]) != len(sources):
        raise ValueError("Invalid quality source")
    urls = {s["url"] for s in output["sources"]}
    if value["tier"] == "experimental":
        reason = value.get("experimental_reason")
        if (not isinstance(reason, dict) or not isinstance(reason.get("source_urls"), list)
                or not reason["source_urls"]
                or any(not isinstance(u, str) or u not in urls for u in reason["source_urls"])):
            raise ValueError("Experimental requires a cited reason about prototype status, instability or unfinished functionality")
        output["experimental_reason"] = {"text": _text(reason.get("text"), 30), "source_urls": reason["source_urls"]}
    elif value.get("experimental_reason"):
        raise ValueError("Resolve experimental evidence before assigning another quality tier")
    checks = value.get("checks")
    if not isinstance(checks, dict) or set(checks) != set(CHECKS):
        raise ValueError("Quality assessment must address all six evidence checks")
    output["checks"] = {}
    for name, check in checks.items():
        if not isinstance(check, dict) or check.get("status") not in {"verified", "documented", "unknown", "failed"}:
            raise ValueError("Invalid quality evidence status")
        cited = check.get("source_urls")
        if (not isinstance(cited, list) or any(not isinstance(u, str) or u not in urls for u in cited)
                or (check["status"] != "unknown" and not cited)):
            raise ValueError("Quality evidence must cite declared sources")
        cleaned = {"status": check["status"], "note": _text(check.get("note"), 15), "source_urls": cited}
        if "source_kind" in check:
            if check["source_kind"] not in {"maintainer", "independent"}:
                raise ValueError("Invalid quality source provenance")
            cleaned["source_kind"] = check["source_kind"]
        output["checks"][name] = cleaned
    if value["tier"] in {"recommended", "ready_to_try"}:
        required = [name for name in CHECKS if value["tier"] == "recommended" or name != "results"]
        if (kind != "profile" or value["method"] != "source-review"
                or any(checks[name]["status"] != "verified" for name in required)
                or checks["independent_use"].get("source_kind") != "independent"):
            label = TIERS[value["tier"]]
            evidence = "all six" if value["tier"] == "recommended" else "the five non-results"
            raise ValueError(f"{label} requires a full profile and {evidence} verified checks, including independent use")
        if value["tier"] == "ready_to_try" and checks["results"]["status"] not in {"unknown", "documented"}:
            raise ValueError("Ready to try requires creative-result review to be pending (unknown or documented), not failed or verified")
    return output


def require_assessment(entry, kind, config, day):
    value = entry.get("quality_assessment")
    if value is None:
        if config.get("scope", {}).get("require_quality_assessment"):
            raise ValueError("Every new profile and lead needs a quality_assessment; unknown evidence stays unverified")
        return
    validate_assessment(value, kind, day)


def record_binding(version):
    """Bind a reassessment to the exact latest published record, not its popularity."""
    basis = deepcopy(version)
    digest = hashlib.sha256(json.dumps(basis, sort_keys=True, ensure_ascii=False,
                                      separators=(",", ":")).encode()).hexdigest()
    return {"basis_edition": version.get("edition_id", version["date"]), "record_sha256": digest}


def read_reviews(root):
    path = root / "config/quality_reviews.json"
    registry = read_json(path) if path.exists() else {"format_version": 1, "audits": {}, "reviews": {}}
    if not isinstance(registry, dict) or registry.get("format_version") != 1:
        raise ValueError("Unsupported quality review registry")
    for group in ("audits", "reviews"):
        if not isinstance(registry.get(group), dict):
            raise ValueError("Quality registry needs audits and reviews")
        for key, row in registry[group].items():
            if (not isinstance(key, str) or not isinstance(row, dict)
                    or not isinstance(row.get("record_sha256"), str)
                    or not re.fullmatch(r"[a-f0-9]{64}", row["record_sha256"])
                    or not isinstance(row.get("basis_edition"), str)):
                raise ValueError("Quality registry needs a published record binding")
            report_date(_text(row.get("checked_on")))
            if group == "reviews":
                validate_assessment(row.get("assessment"), expected_date=row["checked_on"])
    return registry


def baseline_assessment(version, checked_on=None):
    """A conservative record audit never manufactures a verified quality claim."""
    p = version["profile"]
    assessment = {"tier": "unverified", "checked_on": checked_on,
                  "method": "published-record-audit" if checked_on else "unassessed",
                  "summary": "The published record does not establish all six recommendation checks.",
                  "scope": "Existing creative guidance; no new installation or output testing.",
                  "caveats": ["A detailed profile describes a tool; it does not certify its quality.",
                              "Stars, recent commits and a license badge do not establish reliable creative results."],
                  "sources": deepcopy(p["sources"]), "checks": {}}
    sections = {"license": "license", "results": "demo", "setup": "installation", "dependencies": "license"}
    for name in CHECKS:
        section = p.get(sections.get(name, ""), {})
        urls = section.get("source_urls", []) if isinstance(section, dict) else []
        note = ("The dated profile cites documentation for this topic; the recommendation check has not been verified."
                if urls else "This check has no separately verified evidence in the published record.")
        if name == "independent_use":
            note = "Independent first-hand use or integration has not been established by this record audit."
        if name == "maintenance":
            note = "A recent commit or discovery score does not establish substantive maintenance or support."
        assessment["checks"][name] = {"status": "documented" if urls else "unknown", "note": note, "source_urls": urls}
    return assessment


def assess_entry(entry, registry):
    latest = entry["versions"][0]
    binding = record_binding(latest)
    review = registry.get("reviews", {}).get(entry["id"])
    audit = registry.get("audits", {}).get(entry["id"])

    def matches(row):
        return row and all(row.get(k) == v for k, v in binding.items()) and row["checked_on"] >= latest["date"]

    if matches(review):
        assessment = validate_assessment(review["assessment"], latest["kind"], review["checked_on"])
    elif latest["profile"].get("quality_assessment"):
        assessment = validate_assessment(latest["profile"]["quality_assessment"], latest["kind"], latest["profile"]["checked_on"])
    else:
        assessment = baseline_assessment(latest, audit["checked_on"] if matches(audit) else None)
    if review and not matches(review):
        assessment["caveats"].append("An earlier library reassessment applies to a different published record and was not carried forward.")
    return {**assessment, **binding}


def public_quality_library(root):
    from .configuration import load_config
    from .library import make_library
    from .publication import _public_editions
    root = Path(root).resolve()
    documents = [read_json(root / "public/reports" / directory / "report.json") for directory in _public_editions(root)]
    return make_library(documents, load_config(root), read_reviews(root))


def audit_existing(root, day):
    """Record a repeatable audit of existing evidence without editing any edition."""
    root = Path(root).resolve()
    day = report_date(day)
    with locked(root):
        data, registry = public_quality_library(root), read_reviews(root)
        changed = 0
        for tool in data["tools"]:
            binding = record_binding(tool["versions"][0])
            if day < tool["versions"][0]["date"]:
                raise ValueError("Quality audit cannot predate a published record")
            previous = registry["audits"].get(tool["id"], {})
            if all(previous.get(k) == v for k, v in binding.items()):
                continue
            registry["audits"][tool["id"]] = {**binding, "checked_on": day}
            changed += 1
        write_json(root / "config/quality_reviews.json", registry)
    return {"tools": len(data["tools"]), "new_record_audits": changed,
            "note": "Published evidence reassessed; no fresh runtime tests or automatic recommendations. Run build-library to refresh views."}


def evidence_gaps(assessment):
    """Use the promotion criteria, including independent provenance, for gap views."""
    checks = assessment.get("checks", {})
    return [key for key in CHECKS if checks.get(key, {}).get("status") != "verified"
            or (key == "independent_use" and checks[key].get("source_kind") != "independent")]


def review_item(tool):
    """Describe review work without assigning or changing a quality tier."""
    assessment = tool["quality_assessment"]
    latest = tool["versions"][0]
    missing = evidence_gaps(assessment)
    failed = [key for key in missing if assessment["checks"][key]["status"] == "failed"]
    needs_profile = latest["kind"] != "profile"
    needs_source_review = assessment["method"] != "source-review"
    if failed:
        queue = "failed_checks"
    elif assessment["tier"] == "experimental":
        queue = "experimental_review"
    elif needs_profile:
        queue = "profile_needed"
    elif missing == ["results"] and not needs_source_review:
        queue = "results_review"
    else:
        queue = "evidence_review"
    steps = []
    if assessment["tier"] == "experimental":
        reason = assessment["experimental_reason"]
        steps.append({"requirement": "experimental_reason", "action": REVIEW_QUEUES["experimental_review"],
                      "note": reason["text"], "source_urls": reason["source_urls"]})
    if needs_profile:
        steps.append({"requirement": "full_profile", "action":
                      "Complete a detailed profile for the latest record; an older guide does not qualify this assessment."})
    if needs_source_review:
        steps.append({"requirement": "source_review", "action":
                      "Review live sources for a dated assessment; a published-record audit alone cannot grant a higher tier."})
    for key in sorted(missing, key=lambda key: key not in failed):
        check = assessment["checks"][key]
        action = REVIEW_ACTIONS[key]
        if key in failed:
            action = "Resolve the cited failure before considering a higher tier. " + action
        steps.append({"requirement": key, "action": action, "status": check["status"],
                      "note": check["note"], "source_urls": check["source_urls"]})
    if not steps:
        steps.append({"requirement": "assessment", "action":
                      "Review the current scope and citations, then explicitly record the supported tier; labels never promote automatically."})
    return {"id": tool["id"], "name": tool["name"], "tier": assessment["tier"],
            "profile_date": tool["profile_date"], "checked_on": assessment["checked_on"],
            "basis_edition": latest.get("edition_id", latest["date"]),
            "scope": assessment["scope"], "queue": queue,
            "needs_profile": needs_profile, "needs_source_review": needs_source_review,
            "missing_checks": missing, "failed_checks": failed, "next_steps": steps}


def quality_backlog(root, *, check=None, tier=None, sort="priority"):
    if check is not None and check not in CHECKS:
        raise ValueError("Unknown quality evidence check")
    if tier is not None and tier not in TIERS:
        raise ValueError("Unknown quality tier")
    if sort not in {"priority", "oldest"}:
        raise ValueError("Unknown quality backlog order")
    data = public_quality_library(root)
    pending = [review_item(tool) for tool in data["tools"] if tool["quality_assessment"]["tier"] != "recommended"]
    items = [item for item in pending if (check is None or check in item["missing_checks"])
             and (tier is None or item["tier"] == tier)]
    def order(item):
        oldest = (item["checked_on"] or "", item["profile_date"], item["id"])
        if sort == "oldest":
            return oldest
        return (list(REVIEW_QUEUES).index(item["queue"]),
                len(set(item["missing_checks"]) - {"results"}), len(item["missing_checks"]), *oldest)
    return {"counts": data["quality_counts"], "pending": len(pending), "matching": len(items),
            "gap_counts": {key: sum(key in item["missing_checks"] for item in pending) for key in CHECKS},
            "queue_counts": {key: sum(item["queue"] == key for item in pending) for key in REVIEW_QUEUES},
            "queue_labels": REVIEW_QUEUES, "filters": {"check": check, "tier": tier}, "sort": sort,
            "note": "Work order only, not a quality score. Counts cover the complete pending library; filters narrow items. No automatic tier changes or own-demo requirement.",
            "items": sorted(items, key=order)}
