# Quality confidence and broad discovery

The library explores open-source AI across all creative media. Discovery has no
minimum star count or fixed quota. Inclusion establishes a documented creative AI
use and reviewed open-source software license. It does not establish output quality.
**Review depth and quality confidence are separate.** A complete installation guide
can still have unverified quality; a small project can earn a recommendation.

## Three labels

| Label | Meaning |
| --- | --- |
| Recommended | A complete profile with all six evidence checks verified for an explicit creative workflow, with citations and caveats. |
| Quality unverified | Eligible discovery with incomplete quality evidence. This is not a claim that the tool is poor. |
| Experimental | Research, prototype, alpha/beta or other explicitly assessed experimental software. Suitable for exploration; quality and production readiness are not established. |

Research/prototype tools remain Experimental. Do not promote a tool merely because
it has many stars, recent commits, a recognized SPDX badge, an attractive README,
working project-page CI, or a complete profile. Low stars alone do not exclude it.
Default search shows every eligible tool; the Quality confidence filter narrows it.

## Evidence required for Recommended

1. **License:** read and archive the complete open-source software license. Resolve
   material contradictions with the documented distribution and selected workflow.
2. **Results:** inspect concrete creative outputs or a primary evaluation with
   methods, limitations and enough context to judge the claimed use. A demo link
   or promotional promise alone is only documented evidence.
3. **Setup:** identify reproducible installation, versions, dependencies, models
   and a first workflow. Cite demonstrated reproduction or an independent working
   integration; do not equate a command snippet with a working installation.
4. **Maintenance:** review substantive release/fix/support history and unresolved
   blockers for the scoped workflow. A push date, release count or stars alone
   does not pass. State relevant age and support limitations.
5. **Independent use:** cite first-hand creative use, reproduction or an actual
   integration by someone other than the tool's maintainer. Direct user evidence
   or another project's implementation/documentation can qualify. Directories,
   reposted announcements, stars and anonymous popularity counts do not.
6. **Dependencies:** establish the selected model-weight terms, required services,
   proprietary hosts, access and material costs. An open client license does not
   establish its backend's terms or availability. Resolve blocking unknowns or
   narrow the recommendation to a fully documented workflow.

Each check has `verified`, `documented`, `unknown` or `failed` status, a specific
note and citations. `verified` means the cited evidence supports the check; it
does not mean AI Media Scout executed the app. The Mac research workflow never
installs discovered tools. `quality.hands_on_tested` remains a separate disclosure.
Recommendations must state scope, review date and limitations. All platforms
remain equally eligible; do not invent compatibility or hardware requirements.

## New profiles and pending leads

`scope.require_quality_assessment` requires a `quality_assessment` on every new
profile and screened lead. All six checks must be addressed, even when unknown.
The assessment has its own declared HTTPS source list. Non-unknown checks require
citations from that list. Recommended requires all checks verified, a full
profile, `method: source-review`, and `source_kind: independent` on independent use.
The builder rejects missing assessments and unsupported recommendation labels.

Example conservative assessment (replace dates, notes and sources with actual
review evidence; do not turn unknowns into passes to finish an edition):

```json
{
  "tier": "unverified",
  "checked_on": "2026-10-10",
  "method": "source-review",
  "summary": "Creative relevance is documented; output reliability and independent reproduction need review.",
  "scope": "The documented image-editing workflow; no local execution.",
  "caveats": ["Installation and creative output were not tested by AI Media Scout."],
  "sources": [{"title": "Official documentation", "url": "https://official.example/docs"}],
  "checks": {
    "license": {"status": "unknown", "note": "Recommendation-specific distribution terms need a complete review.", "source_urls": []},
    "results": {"status": "documented", "note": "The maintainer documents an example; its output quality has not been assessed.", "source_urls": ["https://official.example/docs"]},
    "setup": {"status": "unknown", "note": "Independent installation reproduction has not been established.", "source_urls": []},
    "maintenance": {"status": "unknown", "note": "Substantive maintenance and unresolved blockers need review.", "source_urls": []},
    "independent_use": {"status": "unknown", "note": "Independent first-hand creative use has not been established.", "source_urls": []},
    "dependencies": {"status": "unknown", "note": "The selected model and service terms have not been fully resolved.", "source_urls": []}
  }
}
```

This quality assessment supplements, and never replaces, the existing creative
relevance and complete software-license eligibility checks. Unknown quality is
allowed; unverified software licensing is not eligible for the library.

## Existing editions and ongoing review

The October 10, 2026 retrospective audit covers all **486 existing library tools**.
It reassesses their published evidence, not their installed behavior. No existing
record establishes all six new checks, so none was automatically recommended.
Explicit research/prototype/experimental/alpha/beta maturity descriptions receive
Experimental; remaining entries receive Quality unverified. 3D AR Studio also has
a fresh, cited Experimental reassessment of its client, demo and backend caveats.
These labels do not claim 486 fresh source audits or runtime tests.

`config/quality_reviews.json` contains recipient-free curation metadata. `audits`
records the date, edition identity and SHA-256 of each latest published record.
`reviews` can add a full cited assessment using the same binding plus `assessment`.
Use `media_scout.quality.record_binding(version)` on the latest version to bind a
review. Archive fresh source snapshots under ignored `state/quality_research/DATE/`
during maintenance, or that new edition's evidence folder during daily research.
Never put raw research, credentials or private paths in the registry.

```sh
python3 -m media_scout quality-backlog --full
# Only when a retrospective record audit is intended:
python3 -m media_scout audit-existing-quality --date YYYY-MM-DD
python3 -m media_scout build-library
python3 -m media_scout verify-public-archive
```

The audit command conservatively records coverage, never promotes recommendations,
and preserves manual reviews. Repeating it on unchanged records does not change
their audit dates. A newer or changed published record invalidates an older manual
assessment's binding; the library uses the new record's assessment or an unverified
fallback. Even a later screened mention invalidates an old recommendation.

Use `quality-backlog --full` alongside `review-backlog` on subsequent runs. It
includes full profiles with missing quality evidence. Review promising workflows
and older gaps, not only popular projects. Update library curation when evidence
improves; do not repeat unchanged tools in a daily report just to change a label.

The library's current `quality_assessment` sits outside preserved `versions`.
Cards, filters, comparisons and downloaded research notes use it and disclose
the assessment date. Selecting an older edition retains that dated guide while
showing the separately labeled current assessment. Sealed HTML/Markdown/JSON
editions, sent emails and delivery receipts remain byte-for-byte unchanged.
`verify-public-archive` recomputes the library from editions, curation and UI source,
including in a clean public clone. Publish through the protected GitHub flow;
quality maintenance does not send another email or change the daily schedule.
