"""Broad discovery, explicit coverage, and archived primary-source evidence."""

from datetime import date, timedelta
import hashlib
import math
from pathlib import Path
from urllib.parse import urlencode

from .client import Client, SourceError
from .configuration import load_config
from .planning import plan_digest, repository_query, search_id, search_plan
from .storage import ROOT, locked, now, read_json, report_date, write_json, write_text

# Conservative allowlist: unrecognized/custom licenses require an editorial check.
OSI_LICENSES = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "BSD-3-Clause-Clear",
    "ISC", "MPL-2.0", "GPL-2.0", "GPL-2.0-only", "GPL-2.0-or-later",
    "GPL-3.0", "GPL-3.0-only", "GPL-3.0-or-later", "LGPL-2.1", "LGPL-3.0",
    "LGPL-2.1-only", "LGPL-2.1-or-later", "LGPL-3.0-only", "LGPL-3.0-or-later",
    "AGPL-3.0", "AGPL-3.0-only", "AGPL-3.0-or-later", "Unlicense", "Zlib",
    "Artistic-2.0", "BSL-1.0", "EPL-2.0", "OFL-1.1", "CC0-1.0",
}


def normalize_repo(repo):
    full_name = repo["full_name"]
    license_id = (repo.get("license") or {}).get("spdx_id", "UNKNOWN")
    return {
        "id": "github:" + full_name.lower(), "name": repo.get("name", full_name),
        "repository": full_name, "url": repo["html_url"],
        "description": repo.get("description") or "", "homepage": repo.get("homepage"),
        "stars": repo.get("stargazers_count", 0), "forks": repo.get("forks_count", 0),
        "created_at": repo.get("created_at"), "pushed_at": repo.get("pushed_at"),
        "updated_at": repo.get("updated_at"), "default_branch": repo.get("default_branch", "main"),
        "archived": bool(repo.get("archived")), "fork": bool(repo.get("fork")),
        "topics": repo.get("topics", []), "code_license": license_id,
        "license_status": "recognized-open-source" if license_id in OSI_LICENSES else "needs-review",
        "categories": [], "discovered_by": [], "evidence": [],
    }


def priority_score(item):
    """Shortlisting signal only. This does not grade creative output quality."""
    score = min(25, 5 * math.log10(1 + item.get("stars", 0)))
    score += 15 if item.get("license_status") == "recognized-open-source" else 0
    score += 10 if item.get("homepage") else 0
    score += 10 if item.get("latest_release") else 0
    score += 10 if item.get("readme_path") else 0
    score -= 40 if item.get("archived") else 0
    score -= 10 if item.get("fork") else 0
    return round(max(0, score), 1)


def fingerprint(item):
    value = "|".join([item.get("readme_sha256", ""), item.get("code_license", ""), item.get("head_sha", ""),
                      (item.get("latest_release") or {}).get("tag", "")])
    if item.get("license_review", {}).get("sha256"):
        value += "|" + item["license_review"]["sha256"]
    return hashlib.sha256(value.encode()).hexdigest()


def novelty(item, previous, cutoff):
    if not previous or not previous.get("last_featured"):
        created = (item.get("created_at") or "")[:10]
        if created and created >= cutoff:
            return "recently-created"
        return "first-profile"
    if item.get("source_fingerprint") == previous.get("source_fingerprint"):
        return "unchanged"
    latest_tag = (item.get("latest_release") or {}).get("tag")
    if latest_tag and latest_tag != previous.get("release_tag"):
        return "new-release"
    return "source-changed-review-required"


def repository_search(client, spec, cutoff, folder, query_index, per_page):
    """Archive each page and disclose incomplete or truncated search coverage."""
    if not isinstance(per_page, int) or not 1 <= per_page <= 100:
        raise ValueError("GitHub results per page must be between 1 and 100")
    query = repository_query(spec, cutoff)
    record = {"provider": "github", "category": spec["category"], "query": query,
              "search_id": search_id(spec),
              "checked_at": now(), "sampled": 0, "pages_collected": 0,
              "pages_requested": spec["pages"], "incomplete_results": False}
    items = []
    for page in range(1, spec["pages"] + 1):
        url = "https://api.github.com/search/repositories?" + urlencode({
            "q": query, "sort": spec["sort"], "order": "desc",
            "per_page": per_page, "page": page})
        if page == 1:
            record["url"] = url
        try:
            payload = client.get(url)
            write_json(folder / "queries" / f"{spec['category']}-{query_index}-page-{page}.json", payload)
            batch = payload.get("items", [])
            items.extend(repo for repo in batch if not repo.get("private"))
            record["total_matches"] = payload.get("total_count", 0)
            record["incomplete_results"] |= bool(payload.get("incomplete_results"))
            record["pages_collected"] += 1
            record["sampled"] += len(batch)
            if len(batch) < per_page or record["sampled"] >= min(1000, record["total_matches"]):
                break
        except SourceError as error:
            record["error"] = str(error)
            break
    record["truncated"] = record["sampled"] < record.get("total_matches", 0)
    record["status"] = ("failed" if record.get("error") and not record["pages_collected"] else
                        "partial" if record.get("error") or record["incomplete_results"] else "ok")
    return record, items


def update_discovery_catalog(root, day, items):
    pool = read_json(root / "state/discovery_catalog.json", {})
    for item in items:
        previous = pool.get(item["id"], {})
        if previous.get("last_seen", "") > day:
            continue
        pool[item["id"]] = {"first_seen": previous.get("first_seen", day),
                            "last_seen": day, "candidate": item}
    write_json(root / "state/discovery_catalog.json", pool)


def collect(day=None, root=ROOT, client=None, plan_path=None):
    root = Path(root).resolve()
    config = load_config(root)
    day = report_date(day, config["timezone"])
    folder = root / "research" / day
    with locked(root):
        existing = read_json(folder / "discovery.json")
        if existing:
            update_discovery_catalog(root, day, existing["candidates"])
            return existing  # Resume the same observation; do not silently refresh it.
        if (root / "reports" / day / "manifest.json").exists():
            raise ValueError("This day's report is sealed; restore its original observation instead of recollecting")
        plan = search_plan(config, day, read_json(plan_path) if plan_path else None)
        categories = plan["categories"]
        write_json(folder / "queries" / "search-plan.json", plan)
        write_json(folder / "queries" / "config-snapshot.json", config)
        client = client or Client()
        started_at = now()
        cutoff = (date.fromisoformat(day) - timedelta(days=config["lookback_days"])).isoformat()
        candidates, coverage, warnings = {}, [], []

        def merge(repo, category, discovery):
            item = normalize_repo(repo)
            key = item["id"]
            if key not in candidates:
                candidates[key] = item
            target = candidates[key]
            if category not in target["categories"]:
                target["categories"].append(category)
            if discovery not in target["discovered_by"]:
                target["discovered_by"].append(discovery)

        for index, spec in enumerate(plan["queries"]):
            record, repos = repository_search(client, spec, cutoff, folder, index, config["items_per_query"])
            for repo in repos:
                merge(repo, spec["category"], record["query"])
            if record.get("error"):
                warnings.append(f"{spec['category']}: {record['error']}")
            if record["truncated"] or record["incomplete_results"]:
                warnings.append(f"{spec['category']}: bounded or incomplete query: {record['query']} "
                                f"({record['sampled']} of {record.get('total_matches', 0)} matches sampled)")
            coverage.append(record)

        # Baselines are checked separately; mature tools needn't have been created this month.
        catalog = read_json(root / "state/catalog.json", {})
        queue = read_json(root / "state/review_queue.json", {})
        for category in categories:
            repositories = list(category.get("seeds", []))
            for key, previous in {**queue, **catalog}.items():
                if key.startswith("github:") and category["id"] in previous.get("profile", previous).get("categories", []):
                    repositories.append(key.removeprefix("github:"))
            for repository in dict.fromkeys(repositories):
                key = "github:" + repository.lower()
                if key in candidates:
                    merge({"full_name": repository, "html_url": candidates[key]["url"]}, category["id"], "watchlist")
                    continue
                try:
                    repo = client.get("https://api.github.com/repos/" + repository)
                    merge(repo, category["id"], "watchlist")
                except SourceError as error:
                    warnings.append(f"Watchlist {repository}: {error}")

        models = []
        for pipeline in plan["huggingface_pipelines"]:
            url = "https://huggingface.co/api/models?" + urlencode({
                "pipeline_tag": pipeline, "sort": "lastModified", "direction": -1,
                "limit": config.get("model_items_per_pipeline", 10), "full": "true", "cardData": "true",
            })
            record = {"provider": "huggingface", "category": pipeline, "url": url, "checked_at": now()}
            try:
                payload = client.get(url)
                write_json(folder / "queries" / f"hf-{pipeline}.json", payload)
                for model in payload:
                    modified = model.get("lastModified") or model.get("last_modified") or ""
                    if modified[:10] < cutoff:
                        continue
                    models.append({"id": model.get("id"), "url": "https://huggingface.co/" + model["id"],
                                   "pipeline": pipeline, "last_modified": modified,
                                   "downloads": model.get("downloads", 0), "likes": model.get("likes", 0),
                                   "license": (model.get("cardData") or {}).get("license", "unknown"),
                                   "gated": model.get("gated", False),
                                   "status": "model-card-and-software-license-review-required"})
                record.update(status="ok", sampled=len(payload))
            except SourceError as error:
                record.update(status="failed", error=str(error), sampled=0)
                warnings.append(f"Hugging Face {pipeline}: {error}")
            coverage.append(record)

        enriched = set()
        for category in categories:
            pool = sorted([item for item in candidates.values() if category["id"] in item["categories"]],
                          key=priority_score, reverse=True)
            enriched.update(item["id"] for item in pool[:config.get("enrichment_per_category", 3)])
            enriched.update("github:" + seed.lower() for seed in category.get("seeds", []))
            # Keep emerging projects even when established repositories have more stars.
            emerging = [item for item in pool if (item.get("created_at") or "")[:10] >= cutoff]
            enriched.update(item["id"] for item in emerging[:config.get("emerging_per_category", 1)])
        enriched.update(key for key in {**queue, **catalog} if key in candidates)

        catalog = read_json(root / "state/catalog.json", {})
        for key in sorted(enriched):
            if key not in candidates:
                continue
            item = candidates[key]
            repository = item["repository"]
            base = "https://api.github.com/repos/" + repository
            try:
                readme = client.get(base + "/readme", allow_missing=True)
                if readme and readme.get("download_url"):
                    value = client.get(readme["download_url"], json_response=False)
                    path = folder / "evidence" / (repository.replace("/", "__") + ".md")
                    write_text(path, value)
                    item["readme_path"] = str(path.relative_to(root))
                    item["readme_sha256"] = hashlib.sha256(value.encode()).hexdigest()
                    item["evidence"].append({"title": "Official README", "url": readme["html_url"],
                                             "blob_sha": readme.get("sha"), "checked_at": now()})
                releases = client.get(base + "/releases?per_page=1")
                releases = [release for release in releases if not release.get("draft")]
                if releases:
                    release = releases[0]
                    item["latest_release"] = {"tag": release.get("tag_name"), "name": release.get("name"),
                                              "published_at": release.get("published_at"),
                                              "prerelease": release.get("prerelease", False),
                                              "url": release["html_url"], "notes": (release.get("body") or "")[:16000]}
                    item["evidence"].append({"title": "Most recent published release (may be prerelease)",
                                             "url": release["html_url"], "checked_at": now()})
                commits = client.get(base + "/commits?per_page=1")
                if commits:
                    item["head_sha"] = commits[0]["sha"]
                    item["evidence"].append({"title": "Latest default-branch commit", "url": commits[0]["html_url"], "checked_at": now()})
                item["source_fingerprint"] = fingerprint(item)
                item["novelty"] = novelty(item, catalog.get(key), cutoff)
            except SourceError as error:
                item["collection_warning"] = str(error)
                warnings.append(f"Evidence {repository}: {error}")

        for item in candidates.values():
            item["discovery_priority"] = priority_score(item)
            item.setdefault("novelty", "not-yet-reviewed")
        ordered = sorted(candidates.values(), key=lambda item: item["discovery_priority"], reverse=True)
        result = {"report_date": day, "started_at": started_at, "completed_at": now(),
                  "plan_version": plan["version"], "search_plan_sha256": plan_digest(plan),
                  "window_start": cutoff, "window_days": config["lookback_days"],
                  "categories": [{"id": c["id"], "name": c["name"]} for c in categories],
                  "scope": plan["scope"],
                  "coverage": coverage, "warnings": warnings,
                  "candidates": ordered, "model_watchlist": models,
                  "note": "Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades."}
        write_json(folder / "discovery.json", result)
        update_discovery_catalog(root, day, ordered)
        return result


def add_repository(repository, categories, day=None, root=ROOT, client=None):
    """Archive an official repository found through additional web research."""
    root = Path(root)
    config = load_config(root)
    day = report_date(day, config["timezone"])
    if len(repository.split("/")) != 2 or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._/" for ch in repository):
        raise ValueError("Use owner/repository")
    with locked(root):
        if (root / "reports" / day / "manifest.json").exists():
            raise ValueError("This day's source observation is sealed")
        folder = root / "research" / day
        discovery = read_json(folder / "discovery.json")
        if not discovery:
            raise ValueError("Run discover first")
        known = {c["id"] for c in discovery.get("categories", config["categories"])}
        if not categories or not set(categories).issubset(known):
            raise ValueError("Specify category IDs from this day's search plan")
        client = client or Client()
        base = "https://api.github.com/repos/" + repository
        item = normalize_repo(client.get(base))
        previous = next((c for c in discovery["candidates"] if c["id"] == item["id"]), {})
        item["categories"] = list(dict.fromkeys(previous.get("categories", []) + categories))
        item["discovered_by"] = ["supplementary-primary-source-web-research"]
        readme = client.get(base + "/readme")
        text = client.get(readme["download_url"], json_response=False)
        path = folder / "evidence" / (item["repository"].replace("/", "__") + ".md")
        write_text(path, text)
        item.update(readme_path=str(path.relative_to(root)), readme_sha256=hashlib.sha256(text.encode()).hexdigest())
        item["evidence"].append({"title": "Official README", "url": readme["html_url"], "blob_sha": readme["sha"], "checked_at": now()})
        releases = client.get(base + "/releases?per_page=1")
        if releases:
            release = releases[0]
            item["latest_release"] = {"tag": release["tag_name"], "name": release.get("name"),
                                      "published_at": release.get("published_at"), "prerelease": release.get("prerelease", False),
                                      "url": release["html_url"], "notes": (release.get("body") or "")[:16000]}
        commits = client.get(base + "/commits?per_page=1")
        if commits:
            item["head_sha"] = commits[0]["sha"]
        item["source_fingerprint"] = fingerprint(item)
        catalog = read_json(root / "state/catalog.json", {})
        item["novelty"] = novelty(item, catalog.get(item["id"]), discovery["window_start"])
        item["discovery_priority"] = priority_score(item)
        discovery["candidates"] = [c for c in discovery["candidates"] if c["id"] != item["id"]] + [item]
        discovery["supplemented_at"] = now()
        write_json(folder / "discovery.json", discovery)
        update_discovery_catalog(root, day, [item])
        return item


def review_license(repository, spdx, note, day=None, root=ROOT, client=None):
    """Store a human/agent review of an ambiguous GitHub license classification.

    The researcher must read the actual LICENSE first. Custom restrictions must
    never be rewritten into an OSI label merely because a README says 'open'.
    """
    if spdx not in OSI_LICENSES or len(note.strip()) < 30:
        raise ValueError("Use a recognized SPDX license and a substantive review note")
    root = Path(root)
    config = load_config(root)
    day = report_date(day, config["timezone"])
    with locked(root):
        if (root / "reports" / day / "manifest.json").exists():
            raise ValueError("This day's source observation is sealed")
        path = root / "research" / day / "discovery.json"
        discovery = read_json(path)
        item = next((c for c in discovery["candidates"] if c["repository"].lower() == repository.lower()), None)
        if not item:
            raise ValueError("Collect this repository first")
        client = client or Client()
        license_data = client.get("https://api.github.com/repos/" + item["repository"] + "/license")
        license_text = client.get(license_data["download_url"], json_response=False)
        evidence_path = root / "research" / day / "evidence" / (item["repository"].replace("/", "__") + "__LICENSE.txt")
        write_text(evidence_path, license_text)
        item["license_review"] = {"original_spdx": item["code_license"], "reviewed_spdx": spdx, "note": note,
                                  "url": license_data["html_url"], "checked_at": now(),
                                  "path": str(evidence_path.relative_to(root)), "sha256": hashlib.sha256(license_text.encode()).hexdigest()}
        item.update(code_license=spdx, license_status="open-source-license-reviewed")
        item["source_fingerprint"] = fingerprint(item)
        catalog = read_json(root / "state/catalog.json", {})
        item["novelty"] = novelty(item, catalog.get(item["id"]), discovery["window_start"])
        write_json(path, discovery)
        update_discovery_catalog(root, day, [item])
        return item["license_review"]
