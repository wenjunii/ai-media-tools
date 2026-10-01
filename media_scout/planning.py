"""Compile an extensible daily search plan without a star-count eligibility floor."""

import re

from .storage import report_date

CATEGORY_ID = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")


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
    queries = []
    for category in categories:
        for index, terms in enumerate(category.get("queries", [])):
            queries.append({"category": category["id"], "terms": terms,
                            "window": "pushed" if index % 2 == 0 else "created",
                            "sort": "stars" if index % 2 == 0 else "updated"})
    queries.extend(extra.get("queries", []))
    seen, normalized = set(), []
    for query in queries:
        terms = query.get("terms")
        if (query.get("category") not in known or not isinstance(terms, str)
                or not terms.strip() or len(terms) > 250 or "\n" in terms):
            raise ValueError("Search queries need a known field and nonempty terms")
        window, sort = query.get("window", "pushed"), query.get("sort", "updated")
        if window not in {"pushed", "created"} or sort not in {"stars", "updated"}:
            raise ValueError("Use pushed/created windows and stars/updated sorting")
        pages = query.get("pages", config.get("pages_per_query", 1))
        if not isinstance(pages, int) or isinstance(pages, bool) or not 1 <= pages <= 10:
            raise ValueError("Repository search pages must be between 1 and 10")
        key = (query["category"], terms.strip(), window, sort)
        if key in seen:
            continue
        seen.add(key)
        normalized.append({"category": query["category"], "terms": terms.strip(),
                           "window": window, "sort": sort, "pages": pages})
    return {"report_date": report_date(day), "categories": categories, "queries": normalized,
            "scope": config.get("scope", {"mode": "open-ended"})}
