"""Validate researched profiles, then seal readable reports and a local archive."""

from html import escape
from pathlib import Path
from urllib.parse import urlparse

from .discovery import OSI_LICENSES
from .configuration import load_config
from .coverage import verify_search
from .storage import ROOT, edition_revision, locked, now, read_json, report_date, sha256, write_json, write_text

SECTIONS = ("introduction", "good_for", "demo", "installation", "usage", "requirements", "license", "quality", "limitations")
LABELS = {"introduction": "Introduction", "good_for": "What it is good for", "demo": "Demo & examples",
          "installation": "Install", "usage": "First project", "requirements": "Hardware & software",
          "license": "License, model weights & costs", "quality": "Why it merits attention", "limitations": "Limitations"}


def safe_url(value):
    if not isinstance(value, str):
        raise ValueError("Source links must be strings")
    url = urlparse(value)
    if url.scheme != "https" or not url.hostname or url.username or url.password:
        raise ValueError("Sources and tool links must be HTTPS URLs without embedded credentials")
    return value


def category_names(config, discovery=None):
    names = {c["id"]: c["name"] for c in config["categories"]}
    names.update({c["id"]: c["name"] for c in (discovery or {}).get("categories", [])})
    return names


def validate_ai_relevance(entry, sources):
    value = entry.get("ai_relevance", {})
    if (not isinstance(value.get("text"), str) or len(value["text"].strip()) < 30
            or not value.get("source_urls") or not set(value["source_urls"]).issubset(sources)):
        raise ValueError("Explain the concrete creative AI use and cite declared primary sources")


def validate_license_review(candidate, sources, config):
    if not config.get("scope", {}).get("require_license_review"):
        return
    review = candidate.get("license_review", {})
    if (review.get("reviewed_spdx") != candidate["code_license"] or not review.get("sha256")
            or not review.get("path") or len(review.get("note", "").strip()) < 30
            or review.get("url") not in sources):
        raise ValueError("Archive and cite the complete reviewed software license before publishing a profile or lead")


def validate(editorial, discovery, config, catalog, queue=None):
    if editorial.get("report_date") != discovery["report_date"]:
        raise ValueError("Editorial date does not match the source observation")
    if not isinstance(editorial.get("summary"), str) or not editorial["summary"].strip():
        raise ValueError("A daily summary is required")
    categories = set(category_names(config, discovery))
    coverage = editorial.get("category_notes", [])
    if len(coverage) != len(categories) or {note.get("category") for note in coverage} != categories:
        raise ValueError("Include one coverage note for every creative field, even when no tool qualifies")
    for note in coverage:
        if not note.get("text") or not note.get("source_urls"):
            raise ValueError("Each coverage note needs a finding and source links")
        for url in note["source_urls"]:
            safe_url(url)
    ecosystems = config.get("scope", {}).get("required_ecosystems", [])
    checks = editorial.get("ecosystem_checks", [])
    if (not isinstance(checks, list) or any(not isinstance(c, dict) or not isinstance(c.get("ecosystem"), str)
                                          or not c["ecosystem"].strip() for c in checks)):
        raise ValueError("Web ecosystem checks need named source groups")
    checked = {c["ecosystem"] for c in checks}
    if len(checked) != len(checks) or not set(ecosystems).issubset(checked):
        raise ValueError("Record a searched finding or explicit gap for every required web ecosystem")
    for check in checks:
        if (check.get("status") not in {"searched", "gap"} or not check.get("finding")
                or check.get("checked_on") != editorial["report_date"]):
            raise ValueError("Web ecosystem checks need today's date, searched/gap status and a finding")
        if check["status"] == "searched" and not check.get("source_urls"):
            raise ValueError("Searched ecosystems need primary-source links")
        for url in check.get("source_urls", []):
            safe_url(url)
    watchlist = editorial.get("watchlist", [])
    if not isinstance(watchlist, list):
        raise ValueError("Excluded/watchlist findings must be a list")
    for finding in watchlist:
        if (not isinstance(finding, dict) or not finding.get("name") or not finding.get("reason")
                or finding.get("status") not in {"excluded", "needs-license-review"}
                or finding.get("checked_on") != editorial["report_date"] or not finding.get("source_urls")):
            raise ValueError("Watchlist findings need a name, reason, status, date and primary sources")
        for url in finding["source_urls"]:
            safe_url(url)
    tools = editorial.get("tools", [])
    maximum = config.get("max_profiles")
    if not isinstance(tools, list) or (maximum is not None and len(tools) > maximum):
        raise ValueError("Invalid tools list or configured profile limit exceeded")
    candidates = {item["id"]: item for item in discovery["candidates"]}
    seen = set()
    for tool in tools:
        key = tool.get("id")
        if key in seen or key not in candidates:
            raise ValueError(f"Duplicate or uncollected repository: {key}")
        seen.add(key)
        candidate = candidates[key]
        if candidate.get("archived"):
            raise ValueError(f"Archived repository cannot be a featured recommendation: {key}")
        if not candidate.get("readme_sha256") or not candidate.get("source_fingerprint"):
            raise ValueError(f"Archive the official README before profiling {key}")
        if candidate["code_license"] not in OSI_LICENSES:
            raise ValueError(f"Software license needs verification before featuring {key}: {candidate['code_license']}")
        if not tool.get("name") or not tool.get("categories") or not set(tool["categories"]).issubset(categories):
            raise ValueError(f"Invalid name or categories for {key}")
        if tool.get("checked_on") != editorial["report_date"]:
            raise ValueError(f"Profile must disclose today's documentation check: {key}")
        source_urls = {safe_url(source["url"]) for source in tool.get("sources", [])}
        if len(source_urls) < 2:
            raise ValueError(f"Use at least two primary-source pages for {key}")
        validate_license_review(candidate, source_urls, config)
        if config.get("scope", {}).get("require_ai_relevance"):
            validate_ai_relevance(tool, source_urls)
        for section in SECTIONS:
            value = tool.get(section)
            if not isinstance(value, dict) or not isinstance(value.get("text"), str) or not value["text"].strip():
                raise ValueError(f"Missing {section} for {key}; explicitly state unreported facts")
            if not value.get("source_urls") or not set(value["source_urls"]).issubset(source_urls):
                raise ValueError(f"Every {section} must cite declared primary sources for {key}")
        for field in ("hardware", "software", "platforms"):
            if not isinstance(tool["requirements"].get(field), str) or not tool["requirements"][field].strip():
                raise ValueError(f"Missing requirements.{field} for {key}")
        if tool["license"].get("code") != candidate["code_license"]:
            raise ValueError(f"License contradicts observed GitHub SPDX metadata for {key}")
        for field in ("weights", "commercial", "cost"):
            if not tool["license"].get(field):
                raise ValueError(f"Missing license.{field} for {key}")
        if not isinstance(tool["quality"].get("hands_on_tested"), bool):
            raise ValueError("Disclose whether the tool was actually run")
        if not tool["installation"].get("steps") or not tool["usage"].get("steps"):
            raise ValueError(f"Install and first-use steps are required for {key}")
        if tool.get("novelty", {}).get("kind") != candidate.get("novelty"):
            raise ValueError(f"Novelty label must match the observed history for {key}")
        if not tool["novelty"].get("text"):
            raise ValueError("Explain what is new, or label the initial baseline")
        previous = catalog.get(key, {})
        if (previous.get("last_featured") and previous["last_featured"] != editorial["report_date"]
                and previous.get("source_fingerprint") == candidate["source_fingerprint"]):
            raise ValueError(f"Already featured without a source change: {key}")
        for link in tool.get("links", {}).values():
            safe_url(link)
    leads = editorial.get("leads", [])
    if not isinstance(leads, list):
        raise ValueError("Pending leads must be a list")
    for lead in leads:
        key = lead.get("id")
        if key in seen or key not in candidates:
            raise ValueError(f"Duplicate or uncollected pending lead: {key}")
        seen.add(key)
        candidate = candidates[key]
        if (candidate.get("archived") or not candidate.get("readme_sha256")
                or not candidate.get("source_fingerprint")
                or candidate.get("code_license") not in OSI_LICENSES
                or lead.get("code_license") != candidate["code_license"]):
            raise ValueError("Pending leads need archived evidence and a matching open-source license")
        if (not lead.get("name") or not lead.get("good_for") or not lead.get("review_status")
                or lead.get("checked_on") != editorial["report_date"]
                or not lead.get("categories") or not set(lead["categories"]).issubset(categories)):
            raise ValueError("Pending leads need today's check, creative use, fields and review status")
        sources = {safe_url(source["url"]) for source in lead.get("sources", [])}
        if len(sources) < 2:
            raise ValueError("Pending leads need official documentation and license sources")
        validate_license_review(candidate, sources, config)
        validate_ai_relevance(lead, sources)
        previous = (queue or {}).get(key, {})
        if (previous.get("last_listed") and previous["last_listed"] != editorial["report_date"]
                and previous.get("source_fingerprint") == candidate["source_fingerprint"]):
            raise ValueError("Already listed as a pending lead without a source change")
    return editorial


def search_coverage_text(value):
    text = (f"{value['fields']} creative fields; "
            f"{value['attempted_github_queries']}/{value['planned_github_queries']} repository queries attempted; "
            f"{value['attempted_model_queries']}/{value['planned_model_queries']} model-task queries attempted. "
            f"{value['source_candidates']} distinct source candidates and {value['model_candidates']} model leads. "
            f"{value['full_profiles']} detailed profiles and {value['screened_leads']} additional screened discoveries.")
    text += (f" Source gaps: {value['failed_github_queries']} failed repository queries, "
             f"{value['partial_github_queries']} partial repository queries, "
             f"{value['truncated_github_queries']} bounded repository queries, "
             f"{value['failed_model_queries']} failed model-task queries and "
             f"{value['ecosystem_gaps']} web ecosystem gaps. "
             "Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; "
             "they are not verified recommendations.")
    return text


def refs_html(section, sources):
    indices = {source["url"]: index + 1 for index, source in enumerate(sources)}
    return " ".join(f'<a href="{escape(url, quote=True)}">[{indices[url]}]</a>' for url in section["source_urls"])


def card_html(tool, candidate, category_names):
    out = [f'<article class="tool" data-categories="{escape(" ".join(tool["categories"]))}">',
           f'<div class="eyebrow">{escape(" · ".join(category_names[c] for c in tool["categories"]))}</div>',
           f'<h2>{escape(tool["name"])}</h2>',
           f'<p class="badge">{escape(tool.get("maturity", "Documentation reviewed"))} · {escape(tool["license"]["code"])} · {escape(tool["novelty"]["kind"])}</p>',
           f'<p class="change">{escape(tool["novelty"]["text"])}</p>']
    release = candidate.get("latest_release") or {}
    meta = f'Docs checked {tool["checked_on"]} · {candidate.get("stars", 0):,} GitHub stars'
    if release:
        meta += f' · Release {release["tag"]} ({(release.get("published_at") or "date unreported")[:10]})'
    out.append(f'<p class="meta">{escape(meta)} · {"Hands-on tested" if tool["quality"]["hands_on_tested"] else "Documentation review; installation not tested"}</p>')
    if tool.get("ai_relevance"):
        out.append('<section><h3>How it uses AI</h3><p>' + escape(tool["ai_relevance"]["text"]) + ' ' + refs_html(tool["ai_relevance"], tool["sources"]) + '</p></section>')
    for name in SECTIONS:
        section = tool[name]
        out.append(f'<section><h3>{LABELS[name]}</h3><p>{escape(section["text"])} {refs_html(section, tool["sources"])}</p>')
        if name == "requirements":
            out.append('<dl class="requirements">')
            for field in ("hardware", "software", "platforms"):
                out.append(f'<dt>{field.capitalize()}</dt><dd>{escape(section[field])}</dd>')
            out.append('</dl>')
        if name == "license":
            out.append('<ul>')
            for field in ("weights", "commercial", "cost"):
                out.append(f'<li><strong>{field.capitalize()}:</strong> {escape(section[field])}</li>')
            out.append('</ul>')
        if section.get("steps"):
            out.append('<ol>' + ''.join(f'<li>{escape(step)}</li>' for step in section["steps"]) + '</ol>')
        for command in section.get("commands", []):
            out.append(f'<pre><code>{escape(command)}</code></pre>')
        out.append('</section>')
    out.append('<p class="links">' + ' · '.join(f'<a href="{escape(url, quote=True)}">{escape(label.replace("_", " ").title())}</a>' for label, url in tool.get("links", {}).items()) + '</p>')
    out.append('<h3>Primary sources</h3><ol class="sources">' + ''.join(f'<li><a href="{escape(source["url"], quote=True)}">{escape(source["title"])}</a></li>' for source in tool["sources"]) + '</ol></article>')
    return '\n'.join(out)


STYLE = """
:root {color-scheme:light;--ink:#18312d;--muted:#526560;--paper:#f5f4ef;--line:#d7dfd8;--accent:#176a58}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
main{max-width:980px;margin:auto;padding:40px 24px 72px}a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}
header{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:24px}.eyebrow{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);font-weight:700}
h1{font-size:clamp(30px,5vw,52px);line-height:1.12;letter-spacing:-.035em;margin:12px 0}h2{font-size:28px;line-height:1.25;margin:8px 0}h3{font-size:16px;margin:18px 0 6px}
p{margin:8px 0 16px}.meta,.sources{font-size:13px;color:var(--muted)}.badge{font-size:12px;font-weight:700;color:var(--accent)}.change{padding:12px 16px;background:#edf3ec;border-left:3px solid var(--accent)}
.tool{background:white;border:1px solid var(--line);border-radius:14px;padding:28px;margin:24px 0;overflow-wrap:anywhere}.tool section{border-top:1px solid #edf0eb}
.stats{display:flex;gap:24px;flex-wrap:wrap;margin:16px 0}.stats strong{font-size:24px;display:block}.stats span{font-size:12px;color:var(--muted)}
.requirements{display:grid;grid-template-columns:110px 1fr;gap:8px;font-size:14px}.requirements dt{font-weight:700}.requirements dd{margin:0}
pre{white-space:pre-wrap;overflow-wrap:anywhere;border:1px solid var(--line);padding:14px;background:#f7f8f4;border-radius:8px;font:13px/1.6 ui-monospace,monospace}
.notice{background:#fff3d9;border:1px solid #e0cf9e;padding:14px 18px;border-radius:8px}.coverage{font-size:14px}table{width:100%;border-collapse:collapse}td,th{border-bottom:1px solid var(--line);padding:10px 6px;text-align:left;vertical-align:top}
.filter-bar{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0}input{width:100%;padding:12px;border:1px solid var(--line);border-radius:8px;font:inherit}
button{border:1px solid var(--line);background:white;padding:8px 12px;border-radius:20px;color:var(--ink);cursor:pointer}button[aria-pressed=true]{background:var(--accent);color:white}select{width:100%;padding:12px;border:1px solid var(--line);border-radius:8px;font:inherit;background:white;color:var(--ink);margin:8px 0 12px}
footer{margin-top:32px;font-size:13px;color:var(--muted)}[hidden]{display:none!important}@media(max-width:550px){main{padding:24px 14px}.tool{padding:20px}.requirements{grid-template-columns:1fr;gap:2px}.requirements dd{margin-bottom:10px}}
"""


def render_html(editorial, discovery, config):
    names = category_names(config, discovery)
    candidates = {item["id"]: item for item in discovery["candidates"]}
    day = editorial["report_date"]
    revision = edition_revision(editorial.get("revision", 1))
    edition = day + (f" · Update {revision - 1}" if revision > 1 else "")
    out = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
           f'<title>AI Media Scout · {edition}</title><style>{STYLE}</style></head><body><main>',
           f'<header><div class="eyebrow">The daily field guide for digital media</div><h1>AI Media Scout</h1><p>{edition} · All platforms · Open-source software</p>',
           f'<p>{escape(editorial["summary"])}</p><div class="stats"><div><strong>{len(editorial["tools"])}</strong><span>Researched profiles</span></div>',
           f'<div><strong>{len(names)}</strong><span>Creative fields searched</span></div><div><strong>{len(discovery["candidates"])}</strong><span>Source candidates</span></div></div></header>']
    if discovery["warnings"]:
        out.append('<div class="notice"><strong>Collection limitations</strong><ul>' + ''.join(f'<li>{escape(warning)}</li>' for warning in discovery["warnings"]) + '</ul></div>')
    if editorial.get("search_coverage"):
        out.append('<section><h2>Search and review counts</h2><p>' +
                   escape(search_coverage_text(editorial["search_coverage"])) + '</p></section>')
    out.append('<div class="notice">Profiles are based on current primary documentation. Creative quality and performance claims are attributed to the developers unless hands-on testing is explicitly recorded. Unknown hardware requirements stay unknown. Code, model weights, hosted services, and required proprietary hosts can have different terms.</div>')
    out.append('<h2 style="margin-top:28px">Today’s field coverage</h2><table class="coverage"><thead><tr><th scope="col">Field</th><th scope="col">Finding</th></tr></thead><tbody>')
    for note in editorial["category_notes"]:
        out.append(f'<tr><td>{escape(names[note["category"]])}</td><td>{escape(note["text"])} ' + ' '.join(f'<a href="{escape(url, quote=True)}">Source {index+1}</a>' for index, url in enumerate(note["source_urls"])) + '</td></tr>')
    out.append('</tbody></table>')
    if editorial.get("ecosystem_checks"):
        out.append('<h2>Research beyond GitHub</h2><ul>')
        for check in editorial["ecosystem_checks"]:
            out.append('<li><strong>' + escape(check["ecosystem"]) + '</strong> · ' +
                       escape(check["status"] + ': ' + check["finding"]) + ' ' +
                       ' '.join('<a href="' + escape(url, quote=True) + '">Source</a>'
                                for url in check.get("source_urls", [])) + '</li>')
        out.append('</ul>')
    for tool in editorial["tools"]:
        out.append(card_html(tool, candidates[tool["id"]], names))
    if editorial.get("leads"):
        out.append('<h2>Additional open-source AI discoveries</h2><p>These projects have been screened for creative AI relevance and software licensing. Full setup, requirements and quality profiles are pending; they are not equivalent to the detailed recommendations above.</p><table><thead><tr><th>Tool</th><th>Creative use and review status</th></tr></thead><tbody>')
        for lead in editorial["leads"]:
            candidate = candidates[lead["id"]]
            out.append(f'<tr><td><a href="{escape(candidate["url"], quote=True)}">{escape(lead["name"])}</a><br>{escape(lead["code_license"])}</td><td>{escape(lead["good_for"])}<br>{escape(lead["ai_relevance"]["text"])}<br><em>{escape(lead["review_status"])}</em> ' +
                       ' '.join(f'<a href="{escape(source["url"], quote=True)}">{escape(source["title"])}</a>' for source in lead["sources"]) + '</td></tr>')
        out.append('</tbody></table>')
    if editorial.get("watchlist"):
        out.append('<h2>Excluded and unresolved findings</h2><p>These findings are retained as research notes and are not part of the eligible tool library.</p><ul>')
        for finding in editorial["watchlist"]:
            out.append('<li><strong>' + escape(finding["name"]) + '</strong> · ' +
                       escape(finding["status"] + ': ' + finding["reason"]) + ' ' +
                       ' '.join('<a href="' + escape(url, quote=True) + '">Source</a>'
                                for url in finding["source_urls"]) + '</li>')
        out.append('</ul>')
    out.append(f'<footer>Observed {escape(discovery["completed_at"])} · {discovery["window_days"]}-day discovery window · Bounded samples, with a separate established-tool watchlist. No downloaded tool was installed or run by this workflow.</footer></main></body></html>')
    return '\n'.join(out)


def render_markdown(editorial, discovery, config):
    names = category_names(config, discovery)
    revision = edition_revision(editorial.get("revision", 1))
    edition = editorial["report_date"] + (f" · Update {revision - 1}" if revision > 1 else "")
    out = [f'# AI Media Scout — {edition}', '', editorial["summary"], '',
           'Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.', '',
           '## Coverage', '', '| Field | Finding |', '| --- | --- |']
    for note in editorial["category_notes"]:
        references = ' '.join(f'[Source {i+1}]({url})' for i, url in enumerate(note["source_urls"]))
        out.append(f'| {names[note["category"]]} | {note["text"].replace("|", "/")} {references} |')
    if editorial.get("search_coverage"):
        out += ['', '## Search and review counts', '', search_coverage_text(editorial["search_coverage"])]
    if editorial.get("ecosystem_checks"):
        out += ['', '## Research beyond GitHub', '']
        for check in editorial["ecosystem_checks"]:
            out.append(('- **' + check["ecosystem"] + '** · ' + check["status"] + ': ' + check["finding"] + ' ' +
                        ' '.join(f'[Source]({url})' for url in check.get("source_urls", []))).rstrip())
    if discovery["warnings"]:
        out += ['', '## Collection limitations', ''] + ['- ' + warning for warning in discovery["warnings"]]
    for tool in editorial["tools"]:
        out += ['', f'## {tool["name"]}', '', ' · '.join(names[c] for c in tool["categories"]), '', tool["novelty"]["text"], '']
        if tool.get("ai_relevance"):
            out += ['### How it uses AI', '', tool["ai_relevance"]["text"] + ' ' +
                    ' '.join(f'[Source]({url})' for url in tool["ai_relevance"]["source_urls"]), '']
        for name in SECTIONS:
            section = tool[name]
            refs = ' '.join(f'[Source {i+1}]({url})' for i, url in enumerate(section["source_urls"]))
            out += [f'### {LABELS[name]}', '', section["text"] + ' ' + refs, '']
            if name == "requirements":
                out += [f'- **{field.capitalize()}:** {section[field]}' for field in ("hardware", "software", "platforms")] + ['']
            if name == "license":
                out += [f'- **{field.capitalize()}:** {section[field]}' for field in ("code", "weights", "commercial", "cost")] + ['']
            out += [f'{index+1}. {step}' for index, step in enumerate(section.get("steps", []))]
            for command in section.get("commands", []):
                out += ['', '```sh', command, '```', '']
        out += ['### Get the tool', ''] + [f'- [{label.replace("_", " ").title()}]({url})' for label, url in tool["links"].items()]
    if editorial.get("leads"):
        out += ['', '## Additional open-source AI discoveries', '',
                'Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.', '']
        for lead in editorial["leads"]:
            out += [f'### {lead["name"]} · {lead["code_license"]}', '', lead["good_for"],
                    lead["ai_relevance"]["text"], lead["review_status"], '']
            out += [f'- [{source["title"]}]({source["url"]})' for source in lead["sources"]]
    if editorial.get("watchlist"):
        out += ['', '## Excluded and unresolved findings', '',
                'Research notes only; these do not enter the eligible tool library.', '']
        for finding in editorial["watchlist"]:
            out.append('- **' + finding["name"] + '** · ' + finding["status"] + ': ' + finding["reason"] + ' ' +
                       ' '.join(f'[Source]({url})' for url in finding["source_urls"]))
    out += ['', f'Source collection completed: {discovery["completed_at"]}', discovery["note"], '']
    return '\n'.join(out)


def verify_report(day, root=ROOT):
    root = Path(root).resolve()
    day = report_date(day)
    folder = root / "reports" / day
    manifest = read_json(folder / "manifest.json")
    if not manifest:
        raise ValueError("No sealed report for this date")
    for filename, expected in manifest["sha256"].items():
        path = root / filename
        if not path.exists() or sha256(path) != expected:
            raise ValueError(f"Sealed evidence/artifact changed: {filename}")
    return manifest


def build(editorial_path, root=ROOT):
    from .library import write_local_library
    root = Path(root).resolve()
    editorial = read_json(editorial_path)
    config = load_config(root)
    day = report_date(editorial["report_date"], config["timezone"])
    revision = edition_revision(config.get("edition_revision", 1))
    if edition_revision(editorial.get("revision", revision)) != revision:
        raise ValueError("Editorial revision does not match its prepared workspace")
    folder = root / "reports" / day
    with locked(root):
        if (folder / "manifest.json").exists():
            manifest = verify_report(day, root)
            if manifest["editorial_sha256"] != sha256(editorial_path):
                raise ValueError("A report for this date is already sealed; preserve it")
            # Recover a crash between sealing and publishing the derived local index.
            discovery = read_json(root / "research" / day / "discovery.json")
            catalog = read_json(root / "state/catalog.json", {})
            update_catalog(catalog, editorial, discovery, day)
            update_queue(root, editorial, discovery, day)
            write_json(root / "state/catalog.json", catalog)
            write_local_library(root, config)
            return manifest
        discovery = read_json(root / "research" / day / "discovery.json")
        if not discovery:
            raise ValueError("Collect source evidence before building the report")
        catalog = read_json(root / "state/catalog.json", {})
        queue = read_json(root / "state/review_queue.json", {})
        search_coverage = None
        if config.get("scope", {}).get("require_expanded_search") or discovery.get("plan_version") == 2:
            search_coverage = verify_search(day, root, discovery)
        validate(editorial, discovery, config, catalog, queue)
        report = dict(editorial, source_observation=discovery["completed_at"], source_warnings=discovery["warnings"],
                      category_labels=category_names(config, discovery))
        if revision > 1:
            report["revision"] = revision
        if search_coverage:
            report["search_coverage"] = dict(search_coverage, full_profiles=len(editorial["tools"]),
                screened_leads=len(editorial.get("leads", [])),
                ecosystems_searched=sum(c["status"] == "searched" for c in editorial.get("ecosystem_checks", [])),
                ecosystem_gaps=sum(c["status"] == "gap" for c in editorial.get("ecosystem_checks", [])))
        if config.get("scope", {}).get("require_license_review"):
            candidates = {c["id"]: c for c in discovery["candidates"]}
            for entry in editorial["tools"] + editorial.get("leads", []):
                review = candidates[entry["id"]]["license_review"]
                path = (root / review["path"]).resolve()
                evidence = (root / "research" / day / "evidence").resolve()
                if evidence not in path.parents or sha256(path) != review["sha256"]:
                    raise ValueError("Reviewed license must match the archived daily evidence")
        write_json(folder / "report.json", report)
        write_text(folder / "report.html", render_html(report, discovery, config))
        write_text(folder / "report.md", render_markdown(report, discovery, config))
        artifacts = [folder / name for name in ("report.json", "report.html", "report.md")]
        artifacts.append(root / "research" / day / "discovery.json")
        evidence_files = (root / "research" / day / "evidence").rglob("*")
        artifacts.extend(sorted(path for path in evidence_files if path.is_file()))
        artifacts.extend(sorted((root / "research" / day / "queries").glob("*.json")))
        artifacts.append(Path(editorial_path).resolve())
        candidates = {item["id"]: item for item in discovery["candidates"]}
        for tool in editorial["tools"] + editorial.get("leads", []):
            item = candidates[tool["id"]]
            artifacts.append(root / item["readme_path"])
            if item.get("license_review"):
                artifacts.append(root / item["license_review"]["path"])
        update_catalog(catalog, editorial, discovery, day)
        manifest = {"report_date": day, "sealed_at": now(), "recipient": config["recipient"],
                    "profile_count": len(editorial["tools"]), "editorial_sha256": sha256(editorial_path),
                    "lead_count": len(editorial.get("leads", [])),
                    "subject": f'[AI Media Scout] {day} — {len(editorial["tools"])} researched tools',
                    "sha256": {str(path.relative_to(root)): sha256(path) for path in artifacts}}
        if revision > 1:
            manifest["revision"] = revision
        write_json(folder / "manifest.json", manifest)
        update_queue(root, editorial, discovery, day)
        write_json(root / "state/catalog.json", catalog)
        write_local_library(root, config)
        verify_report(day, root)
        return manifest


def update_catalog(catalog, editorial, discovery, day):
    candidates = {item["id"]: item for item in discovery["candidates"]}
    for tool in editorial["tools"]:
        item = candidates[tool["id"]]
        previous = catalog.get(tool["id"], {})
        # Rebuilding an older report must not replace a more recent library profile.
        if previous.get("last_featured", "") > day:
            continue
        catalog[tool["id"]] = {
            "first_featured": previous.get("first_featured", day), "last_featured": day,
            "source_fingerprint": item["source_fingerprint"],
            "release_tag": (item.get("latest_release") or {}).get("tag"),
            "head_sha": item.get("head_sha"), "name": tool["name"], "profile": tool,
            "category_labels": {c["id"]: c["name"] for c in discovery.get("categories", [])},
        }


def update_queue(root, editorial, discovery, day):
    candidates = {item["id"]: item for item in discovery["candidates"]}
    queue = read_json(root / "state/review_queue.json", {})
    for tool in editorial["tools"]:
        if queue.get(tool["id"], {}).get("last_listed", "") <= day:
            queue.pop(tool["id"], None)
    for lead in editorial.get("leads", []):
        previous = queue.get(lead["id"], {})
        if previous.get("last_listed", "") > day:
            continue
        queue[lead["id"]] = {**lead, "first_listed": previous.get("first_listed", day),
                             "last_listed": day, "source_fingerprint": candidates[lead["id"]]["source_fingerprint"],
                             "category_labels": {c["id"]: c["name"] for c in discovery.get("categories", [])}}
    write_json(root / "state/review_queue.json", queue)
