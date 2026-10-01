"""Audit the executed search plan and expose counts without publishing raw leads."""

from pathlib import Path

from .planning import plan_digest, repository_query, search_id, search_plan
from .storage import ROOT, read_json, report_date


def plan_summary(plan):
    return {"report_date": plan["report_date"], "fields": len(plan["categories"]),
            "github_queries": len(plan["queries"]),
            "query_lanes": {lane: sum(q["window"] == lane for q in plan["queries"])
                            for lane in ("pushed", "created", "any")},
            "model_tasks": len(plan["huggingface_pipelines"])}


def coverage_summary(discovery, plan=None):
    records = discovery.get("coverage", [])
    github = [r for r in records if r["provider"] == "github"]
    models = [r for r in records if r["provider"] == "huggingface"]
    return {"tracking": "expanded" if plan else "legacy",
            "fields": len(discovery.get("categories", [])),
            "planned_github_queries": len(plan["queries"]) if plan else None,
            "attempted_github_queries": len(github),
            "successful_github_queries": sum(r["status"] == "ok" for r in github),
            "failed_github_queries": sum(r["status"] == "failed" for r in github),
            "partial_github_queries": sum(r["status"] == "partial" for r in github),
            "truncated_github_queries": sum(bool(r.get("truncated")) for r in github),
            "planned_model_queries": len(plan["huggingface_pipelines"]) if plan else None,
            "attempted_model_queries": len(models),
            "failed_model_queries": sum(r["status"] == "failed" for r in models),
            "source_candidates": len(discovery["candidates"]),
            "model_candidates": len(discovery.get("model_watchlist", []))}


def verify_search(day, root=ROOT, discovery=None, require_expanded=True):
    """Require every archived planned query to have an honest execution record.

    Failed, incomplete and truncated sources remain explicit gaps; an omitted
    query is a different error and must never masquerade as the full daily plan.
    """
    root = Path(root)
    day = report_date(day)
    discovery = discovery or read_json(root / "research" / day / "discovery.json")
    if not discovery:
        raise ValueError("Collect source evidence before verifying search coverage")
    if discovery.get("report_date") != day:
        raise ValueError("Observation date does not match the requested search date")
    if discovery.get("plan_version") != 2:
        if require_expanded:
            raise ValueError("This observation predates full expanded-search tracking; preserve it")
        return coverage_summary(discovery)
    plan = read_json(root / "research" / day / "queries/search-plan.json")
    if (not plan or plan.get("report_date") != day or plan.get("version") != 2
            or plan_digest(plan) != discovery.get("search_plan_sha256")):
        raise ValueError("Archived search plan is missing or differs from the collected plan")
    snapshot = read_json(root / "research" / day / "queries/config-snapshot.json")
    if not snapshot:
        raise ValueError("Archived configuration is required to verify the full expanded plan")
    defaults = search_plan(snapshot, day)
    def query_key(spec):
        return tuple(spec[key] for key in ("category", "terms", "window", "sort"))
    effective = {query_key(spec): spec["pages"] for spec in plan["queries"]}
    if (any(effective.get(query_key(spec), 0) < spec["pages"] for spec in defaults["queries"])
            or not set(defaults["huggingface_pipelines"]).issubset(plan["huggingface_pipelines"])):
        raise ValueError("Expanded plan omits configured starter queries or model tasks")
    expected = {search_id(spec): spec for spec in plan["queries"]}
    github = [r for r in discovery["coverage"] if r["provider"] == "github"]
    if (len(github) != len(expected) or {r.get("search_id") for r in github} != set(expected)):
        raise ValueError("Full expanded search is incomplete: every planned repository query must be attempted")
    for record in github:
        spec = expected[record["search_id"]]
        if (record["query"] != repository_query(spec, discovery["window_start"])
                or record["category"] != spec["category"]
                or record["pages_requested"] != spec["pages"]
                or record["status"] not in {"ok", "partial", "failed"}):
            raise ValueError("Repository execution record contradicts its planned query")
    models = [r for r in discovery["coverage"] if r["provider"] == "huggingface"]
    if (len(models) != len(plan["huggingface_pipelines"])
            or {r["category"] for r in models} != set(plan["huggingface_pipelines"])
            or any(r["status"] not in {"ok", "failed"} for r in models)):
        raise ValueError("Full expanded search is incomplete: every planned model task must be attempted")
    if discovery.get("categories") != [{"id": c["id"], "name": c["name"]} for c in plan["categories"]]:
        raise ValueError("Observed creative fields contradict the archived search plan")
    if len({c["id"] for c in discovery["candidates"]}) != len(discovery["candidates"]):
        raise ValueError("Source candidates must have distinct canonical IDs")
    return coverage_summary(discovery, plan)


def review_backlog(root=ROOT):
    """Return all retained candidates without a full profile, including pilot leads.

    No stars, field quota or metadata-only license label determines eligibility.
    Archived and irrelevant candidates still need an editorial decision.
    """
    root = Path(root)
    pool = read_json(root / "state/discovery_catalog.json", {})
    catalog = read_json(root / "state/catalog.json", {})
    queue = read_json(root / "state/review_queue.json", {})
    items = []
    for key, observation in pool.items():
        if key in catalog:
            continue
        item = observation["candidate"]
        items.append({"id": key, "name": item["name"], "url": item["url"],
                      "categories": item.get("categories", []), "code_license": item.get("code_license", "UNKNOWN"),
                      "first_seen": observation["first_seen"], "last_seen": observation["last_seen"],
                      "review": "profile-pending" if key in queue else "eligibility-not-established"})
    items.sort(key=lambda item: (item["review"] != "profile-pending", item["first_seen"], item["id"]))
    return {"retained_candidates": len(pool), "unprofiled_candidates": len(items),
            "screened_profile_pending": len(queue), "items": items}
