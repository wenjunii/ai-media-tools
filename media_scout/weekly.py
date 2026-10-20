"""Read-only weekly coverage across every published tool and quality tier."""

from datetime import date, timedelta
from pathlib import Path

from .configuration import load_config
from .quality import CHECKS, REVIEW_ACTIONS, TIERS, public_quality_library, review_item
from .storage import report_date


def weekly_quality(root, day=None):
    """Plan source rechecks; dates describe recorded work, not source truth."""
    root = Path(root).resolve()
    config = load_config(root)
    day = report_date(day, config["timezone"])
    settings = config.get("weekly_quality_review", {})
    enabled = settings.get("enabled", False)
    start = settings.get("starts_on")
    today = date.fromisoformat(day)
    monday = (today - timedelta(days=today.weekday())).isoformat()
    window = max(monday, start) if start else monday
    active = enabled and day >= window
    data = public_quality_library(root)
    items, reviewed, future = [], [], []
    for tool in data["tools"]:
        latest = tool["versions"][0]
        if latest["date"] > day:
            raise ValueError("Weekly review date cannot predate the current library")
        assessment = tool["quality_assessment"]
        checked = assessment["checked_on"]
        source_review = assessment["method"] == "source-review"
        has_sources = bool(assessment["sources"])
        if checked and checked > day:
            future.append(tool["id"])
        # A historical record audit, missing date or future date never earns
        # weekly coverage. assess_entry already checks the latest-record binding.
        if (active and source_review and has_sources and checked
                and window <= checked <= day):
            reviewed.append(tool)
            continue
        item = review_item(tool)
        item["last_source_review_on"] = checked if source_review and has_sources and checked and checked <= day else None
        item["review_reason"] = (
            "future_assessment_date" if checked and checked > day else
            "source_review_needed" if not source_review or not has_sources or not checked else
            "weekly_refresh_due"
        )
        # Recheck all six, including previously verified evidence. The ordinary
        # backlog lists only gaps and omits Recommended tools.
        item["refresh_checks"] = [
            {"check": key, "label": label, "action": REVIEW_ACTIONS[key],
             "previous_status": assessment["checks"][key]["status"],
             "source_urls": assessment["checks"][key]["source_urls"]}
            for key, label in CHECKS.items()
        ]
        items.append(item)
    items.sort(key=lambda row: (row["last_source_review_on"] or "", row["profile_date"], row["id"]))
    if not enabled:
        state = "disabled"
    elif not active:
        state = "scheduled"
    elif not data["tools"]:
        state = "empty"
    else:
        state = "due" if items else "complete"
    next_start = (date.fromisoformat(window) + timedelta(days=7)).isoformat() if active else window
    return {
        "as_of": day, "state": state, "due": active and bool(items),
        "timezone": config["timezone"], "daily_run_time": config.get("daily_time", "08:00"),
        "starts_on": start, "week_start": window, "next_week_start": next_start,
        "total": len(data["tools"]), "reviewed_this_week": len(reviewed),
        "remaining": len(items), "quality_counts": data["quality_counts"],
        "remaining_by_tier": {tier: sum(row["tier"] == tier for row in items) for tier in TIERS},
        "future_assessment_ids": future,
        "refresh_checks": CHECKS,
        "note": (
            "Coverage uses dated, cited source-review assessments for the latest published records. "
            "It does not prove source truth, passed checks or hands-on testing. "
            "Every tier and screened lead is included; only explicit evidence reviews can change labels. "
            "Recheck all six criteria and archive sources before recording the actual review date. "
            "Unfinished tools remain pending on later daily runs; no tool quota or GitHub requests here."
        ),
        "items": items,
    }
