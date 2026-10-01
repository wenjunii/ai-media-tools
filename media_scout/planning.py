"""Compile an extensible daily search plan without a star-count eligibility floor."""

import hashlib
import json
import re

from .storage import report_date

CATEGORY_ID = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
SEARCH_WINDOWS = ("pushed", "created", "any")


def search_id(query):
    return hashlib.sha256(json.dumps(query, sort_keys=True).encode()).hexdigest()[:20]


def plan_digest(plan):
    return hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()


def repository_query(spec, cutoff):
    window = "" if spec["window"] == "any" else f" {spec['window']}:>={cutoff}"
    return f"{spec['terms']}{window} is:public fork:false archived:false"


def search_plan(config, day, extra=None):
    extra = extra or {}
    if extra.get("report_date", day) != day:
        raise ValueError("Search plan date must match the observation date")
    categories = [dict(category) for category in config["categories"]]
    known = {category["id"] for category in categories}
    for category in extra.get("additional_categories", []):
        if (not CATEGORY_ID.fullmatch(category.get("id", ""))
                or category["id"] in known or not category.get("name")):
            raise ValueError("Additional categories need unique safe IDs and names")
        categories.append(dict(category, queries=category.get("queries", []),
                               seeds=category.get("seeds", [])))
        known.add(category["id"])
    windows = config.get("search_windows", list(SEARCH_WINDOWS))
    if (not isinstance(windows, list) or not windows
            or any(not isinstance(window, str) or window not in SEARCH_WINDOWS for window in windows)
            or len(set(windows)) != len(windows)):
        raise ValueError("Search windows must be unique pushed/created/any lanes")
    queries = []
    for category in categories:
        for terms in category.get("queries", []):
            for window in windows:
                queries.append({"category": category["id"], "terms": terms,
                                "window": window,
                                "sort": "stars" if window == "any" else "updated"})
    queries.extend(extra.get("queries", []))
    seen, normalized = {}, []
    for query in queries:
        terms = query.get("terms")
        if (query.get("category") not in known or not isinstance(terms, str)
                or not terms.strip() or len(terms) > 250 or "\n" in terms):
            raise ValueError("Search queries need a known field and nonempty terms")
        window, sort = query.get("window", "pushed"), query.get("sort", "updated")
        if window not in SEARCH_WINDOWS or sort not in {"stars", "updated"}:
            raise ValueError("Use pushed/created/any windows and stars/updated sorting")
        pages = query.get("pages", config.get("pages_per_query", 1))
        if not isinstance(pages, int) or isinstance(pages, bool) or not 1 <= pages <= 10:
            raise ValueError("Repository search pages must be between 1 and 10")
        key = (query["category"], terms.strip(), window, sort)
        if key in seen:
            normalized[seen[key]]["pages"] = max(normalized[seen[key]]["pages"], pages)
            continue
        seen[key] = len(normalized)
        normalized.append({"category": query["category"], "terms": terms.strip(),
                           "window": window, "sort": sort, "pages": pages})
    pipelines = config.get("huggingface_pipelines", [])
    additions = extra.get("additional_pipelines", [])
    if (not isinstance(pipelines, list) or not isinstance(additions, list)
            or any(not isinstance(p, str) or not re.fullmatch(r"[a-z][a-z0-9-]{0,79}", p)
                   for p in pipelines + additions)):
        raise ValueError("Model tasks must use safe pipeline IDs")
    pipelines = list(dict.fromkeys(pipelines + additions))
    return {"version": 2, "report_date": report_date(day), "categories": categories,
            "queries": normalized, "huggingface_pipelines": pipelines,
            "scope": config.get("scope", {"mode": "open-ended"})}
