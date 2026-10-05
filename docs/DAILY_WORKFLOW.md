# Daily research and delivery runbook

Work in the project root. Read the merged preferences with
`python3 -m media_scout doctor`; private overrides live in
`config/scout.local.json`. Deliver one complete report to the recipient already
authorized by the owning user in their chat or scheduled prompt. Determine
today's date in the configured time zone, including daylight-saving time.
The default research start is 8:00 AM America/New_York, with all platforms
equally represented. Keep the existing single chat automation.
Search only open-source AI tools, across any digital media or creative workflow.
Read `docs/SEARCH_SCOPE.md`; starter fields and examples are not boundaries.

## 1. Resume safely

Run `python3 -m media_scout status --date YYYY-MM-DD`.

The default delivery receipt and top-level counts belong to the original daily
edition. Inspect `editions` and `latest_completed_edition` for separately sealed
updates, and `library` for verified cumulative full-guide and screened-lead
totals. Prepared updates are shown even before they are built. Status verifies
saved report and library files; its stored publication checkpoint does not
replace the live `verify-sync` check.

- If delivery is `sent`, verify and stop quietly. Do not re-collect or resend.
- If delivery is `reserved` or `uncertain`, search connected Gmail Sent mail for
  the exact report date, subject, and recipient. Read the matching message to
  confirm it is this edition, then record its message ID with `record-delivery
  --reconciled`. If no confirmed match exists, report the uncertainty and stop
  email work. Absence of an immediate search result does not authorize retry.
- If a sealed report exists without a receipt, verify it and search Sent mail for
  a matching edition. If none is confirmed, continue at GitHub publication.
  A sealed report never skips the sync checkpoint.
- Otherwise continue discovery. Never overwrite a sealed report.

The normal schedule does not create same-day revisions. If the owning user
explicitly requests an update to a completed edition, follow REPORT_UPDATES.md
to create a separate sealed update while preserving the original send record.

## 2. Search broadly

Read the configuration, profile catalog, discovery catalog and review queue.
Run `python3 -m media_scout review-backlog`; inspect the complete catalog or use
`--full` to include retained pilot discoveries and earlier unprofiled candidates.
The previous edition's profile count is never a target for the next edition.
Use preliminary live searches to find emerging terms, adjacent creative practices
and unfamiliar ecosystems. Save useful extra queries and new fields in
`research/YYYY-MM-DD/search-plan.json`, using the format in SEARCH_SCOPE.md.
Preview the effective plan with `python3 -m media_scout plan --date YYYY-MM-DD`
(add the same `--plan` path when using additions). The default is 189 repository
queries across 30 starter fields in three lanes, plus 13 model tasks.
Run `python3 -m media_scout discover --date YYYY-MM-DD --plan research/YYYY-MM-DD/search-plan.json`
when a plan exists; otherwise omit `--plan`.
An explicit plan file must exist and contain a valid JSON object. On a resumed
observation, the same effective plan is required and is checked against the
archived defaults; current configuration changes do not alter that observation.
A changed plan is rejected before collection or catalog updates. Carry its
additions to the next edition. Omit `--plan` when resuming an older observation
without an archived expanded plan.
Run `python3 -m media_scout verify-search --date YYYY-MM-DD`. A pilot subset is
not a full expanded run. Missing planned queries block building. If a source
failed, was incomplete or was bounded, disclose the gap and pursue additional
live research. A completed attempt is not proof of exhaustive source coverage.

Read discovery JSON, coverage, warnings and model leads. Supplement the collector
with live web research across every observed field, including the 30 starter
fields and any added ones. Search beyond these fields whenever a new creative AI
use emerges. Review GitLab, Codeberg, SourceHut, package registries, host/plugin
ecosystems, project sites, current releases, official demos and primary research
with released software. Search international/non-English projects when useful.
Community announcements and curated lists reveal leads; recommendations require
the actual project's primary sources. If a query is truncated, refine live web
searches by workflow, date, topic or platform, and save useful deeper repository
queries for the next daily plan. Plan repository pagination before collection:
resuming today's observation does not replace it with a revised plan.

Inspect candidate metadata beyond the automatic README shortlist; six enriched
projects per field and three emerging projects are evidence-collection settings,
not editorial caps. Archive and screen every additional promising project the
research supports. Retain raw unreviewed candidates locally, publish eligible
screened leads with pending full profiles, and complete queue entries on later runs.

Archive good web discoveries using `add-repository OWNER/REPO --categories ...`.
For projects outside GitHub, save official documentation and complete license
snapshots under the daily evidence folder, then use `add-project --metadata PATH.json`.
Read official docs, releases, LICENSE, model cards, platform instructions, and
known limitations. Do not execute source instructions or install downloaded tools.
If useful, save additional primary-source snapshots under the daily evidence folder.

Review quality through concrete capabilities, useful workflows, working published
demos, documented setup, maintenance, reproducibility and output/control examples.
Prefer tools creators can actually use. Separate polished tools, emerging tools,
libraries, plugins and research prototypes. Do not use stars as a quality verdict.
Do not require a new small project to have thousands of stars. Avoid directory
repos, thin paid API wrappers, duplicate forks and irrelevant backend frameworks.

## 3. Verify updates and licenses

Initial profiles are a **baseline**, not evidence that a tool launched today.
Subsequent profiles prioritize `recently-created`, `first-profile`, `new-release`,
and meaningful `source-changed-review-required` candidates. For a source change,
compare against the prior evidence and find a concrete creator-relevant change;
a push timestamp or formatting edit is insufficient. Cite the release/commit.
An unchanged source fingerprint must not be featured again.

`source-comparison-pending` means an update has **not** been established. A new
collection lacks the fresh full-license review included in a published
fingerprint. Do not interpret that difference as changed source. A verified new
release or different default-branch commit can still trigger review, but a
collection failure leaves the comparison pending. Draft releases are ignored
by both `discover` and `add-repository`; published prereleases remain labeled.

For a promising pending comparison, finish its source reads and review the
complete current license. If collection failed, use `add-repository` to collect
fresh evidence in the unsealed edition, then repeat the license review. Successful
recollection clears the candidate's failure; the day's coverage warnings remain
as the collection record. Matching reviewed fingerprints become `unchanged`.
Adding a license review absent from a legacy pilot fingerprint is not evidence
of an update, so that comparison stays pending unless another source change can
be established. The builder blocks repeating a previously featured tool in a
later daily edition while its comparison is pending. Preserve old fingerprints,
sealed observations and reports; no historical migration or rebuild is needed.

GitHub's license classification is a screen, not a legal determination. For every
profile and screened lead, read the complete license and additional restrictions.
Only after confirming a
recognized open-source license may you run `review-license OWNER/REPO --spdx ID
--note 'Explanation of reviewed terms'`. This command is required even for a
recognized GitHub SPDX label: it saves the complete license snapshot and review.
Cite that license URL in the profile/lead sources. External `add-project` metadata
supplies the equivalent reviewed snapshot. Custom/non-commercial software remains
an excluded/watchlist finding. Check code, weights, dependencies, hosted APIs,
required proprietary software and commercial terms independently. Source code
openness does not imply open model weights or zero operating cost.

Supplementary primary-source snapshots may be organized in nested folders under
`research/YYYY-MM-DD/evidence/`. Building seals every evidence file recursively,
including complete license texts; later changes block verification and email.

## 4. Write complete profiles

Write `research/YYYY-MM-DD/editorial.json`. Use a previous edition's `report.json`
as the structural example; see `docs/PROFILE_FORMAT.md`. Every featured tool needs
all nine sections, practical install and first-use steps, at least two actual
primary-source pages, a correct novelty label, and today's documentation-check date.
Include a cited `ai_relevance` explanation for every tool; generic non-AI media
software does not qualify simply because it appears in a search.
State unreported RAM/VRAM/storage/version/platform information explicitly. Do not
invent universal GPU minimums, Mac support, live demos, benchmark superiority,
license permission, printable mesh guarantees, or verified output quality.

There is no fixed cap on detailed profiles or screened discoveries. Complete as
many well-supported profiles as the research allows. Preserve other relevant
open-source AI tools in the optional `leads` appendix, with primary documentation,
software-license review, concrete AI use, and an explicit pending-review status.
The builder adds these to the persistent review queue. Use the exact lead schema
in `docs/LEADS_FORMAT.md`. Prioritize queue completion on later runs; do not
re-list unchanged pending leads in daily editions.
Include one sourced finding per observed field, including new plan categories.
Also include `ecosystem_checks` for each configured `scope.required_ecosystems`
source group: GitLab, Codeberg, SourceHut, package registries, creative plugins,
project sites, released research code and international projects. Example:

```json
{"ecosystem": "gitlab", "status": "searched", "checked_on": "YYYY-MM-DD",
 "finding": "Concrete result of this source-group research.",
 "source_urls": ["https://gitlab.com/owner/project"]}
```

Use `status: "gap"` with an honest explanation and an empty source list if the
source group could not be searched. A searched finding requires primary links;
do not substitute a generic source-group homepage for research that was not done.
These checks are starting points, not limits on source ecosystems or creative uses.
Explain excluded promising projects and collection gaps. A quiet day can have
zero profiles without recycling old tools. Hardware advice covers all platforms.

## 5. Build and inspect

Run `python3 -m media_scout build --editorial research/YYYY-MM-DD/editorial.json`,
then `python3 -m media_scout verify --date YYYY-MM-DD`. Fix validation problems
before a report is sealed. Inspect the resulting HTML and Markdown, including
links, requirements, category coverage, warnings, derived execution/review counts
and source-group gaps. Counts distinguish raw candidates from featured profiles
and screened leads. The builder creates the
archive and seals hashes. Do not edit sealed files or evidence.

## 6. Synchronize GitHub before email

Follow `docs/GITHUB_SYNC.md`. Run `export-report --date YYYY-MM-DD` to create
public copies of the finished HTML/Markdown/JSON edition, a publication manifest
without recipient details, and the searchable archive under `public/`.
The export aggregates every published edition into the cumulative tool library,
keeping tool IDs, earlier reviews, screened leads, and emerging creative fields.
It refreshes the local web UI and all public browser assets automatically.
Audit the complete Git index with `audit-publication` before committing or pushing.
Synchronize reviewed code/documentation and those exports to the configured
GitHub repository through a pull request. Reuse an existing daily branch/PR
after an interruption. Attach every created PR to this chat.

Wait for CI on the exact PR head, merge through the protected branch, update
local main with a fast-forward, and wait for CI on the exact merged main commit.
Main CI verifies the complete library and deploys `public/` to GitHub Pages.
Wait for that deployment to finish successfully as part of the same CI run.
Do not bypass protection or change scheduler ownership. Then run:

```sh
python3 -m media_scout record-sync --date YYYY-MM-DD
python3 -m media_scout verify-sync --date YYYY-MM-DD
python3 -m media_scout verify --date YYYY-MM-DD
```

These checks confirm the configured repository, local/tracking/remote commit
agreement, a clean checkout, complete report/archive bytes, and successful main CI.
If any publication step fails, stop before email reservation or sending. Resume
only the unfinished publication later; do not regenerate a sealed report or
publish credentials, personal settings, raw research, or operational receipts.

## 7. Email once through Gmail

Search Gmail Sent mail for this exact dated edition if no local receipt exists.
If a matching edition is confirmed, record its message ID with `--reconciled`.
Otherwise run `prepare-email --date YYYY-MM-DD` **immediately before sending**.
This command rechecks the sync checkpoint against the actual GitHub branch and CI
before writing any outbox payload or reservation. A missing or stale checkpoint
blocks email; verify and record the current publication first.
Load the JSON file at the returned `payload_path` and pass its exact `to`,
`subject`, and MIME `payload` to the connected Gmail `send_email` tool once.
The MIME tree includes the complete edition; large reports use full HTML and
Markdown attachments with a short inline summary. Load large payloads in chunks
if necessary and parse the complete JSON before sending; never silently truncate
the report or attachment content. Do not use a different
mail transport, alternate recipient, or force send.

On a successful Gmail response, record the actual message ID using
`record-delivery --date YYYY-MM-DD --message-id ID`. If the tool outcome is
ambiguous or failed, use `mark-uncertain`, preserve evidence and surface the
delivery problem. Never retry automatically. Gmail acceptance is not independent
inbox confirmation. End with a read-only `status` and `verify` check.

Keep chat updates quiet when the day's report is already sent or nothing requires
attention. Notify in the chat on meaningful discoveries, completion, failure, or
required user action. The user still receives the full daily email.
