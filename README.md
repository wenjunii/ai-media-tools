# AI Media Scout

For the Windows PC's separate local demo-production project, see
[`pc_demo/README.md`](pc_demo/README.md) and the shared
[`PROJECT_BRIEF.md`](PROJECT_BRIEF.md). The Mac retains research, scheduling,
library/report publication and email ownership. The tested PC adapter uses
Real-ESRGAN to create a 45-second vertical draft from actual image upscaling.
Check this PC with `./pc_demo/demo.ps1 status`; see the PC guide for setup on a
new machine. PC demo media and runtimes stay local; social publishing and daily
demo scheduling are disabled. Explicitly requested PC source-code sync follows
the [protected GitHub workflow](docs/GITHUB_SYNC.md#pc-source-and-documentation-sync).

A daily field guide to high-quality open-source AI tools for artists, designers,
filmmakers, musicians, creative coders, immersive-media makers, and game creators.
The scope includes **any digital media or creative workflow**. The user's examples
and configured fields are starting points, not boundaries. The focus remains
**only open-source AI tools**, with concrete creative AI use verified.

The default research schedule is **8:00 AM Eastern**, every day. Reports go to
the authorized recipient in your local settings through the connected Gmail
plugin. Hardware advice covers Mac, Windows, Linux, browser, headset, and cloud
options equally.

Daily order: **generate and verify → sync GitHub → send email**. Finished reports
are published in the [public report archive](public/README.md). Private settings,
raw research, and delivery records remain local.

Corrections discovered after an edition is sealed are listed in
[report corrections](docs/REPORT_CORRECTIONS.md), preserving the original archive.

**[Search the live tool library](https://wenjunii.github.io/ai-media-tools/)**.
The same web UI runs locally, with full-text search, filters, detailed profiles,
dated review history, saved tools, and side-by-side comparisons. Save promising
tools to a browser shortlist, or choose 2–4 tools to compare requirements,
platforms, software/model terms, costs and review evidence. Copy the comparison
link to revisit or share those exact dated reviews. Published profiles and
screened discoveries accumulate
without a fixed count limit. An edition with no qualifying discoveries preserves
the existing collection.

Use **Move saved tools** to transfer a shortlist between your Mac, PC, local
library and GitHub Pages. Download or copy its JSON and import it in the other
browser; matching tools are merged into that browser's existing saves. You can
also download **research notes** in Markdown with the saved tools' dated guides,
installation steps, requirements, software/model terms and sources for planning
your next experiment. Transfers are manual and require no account.

The October 1 initial edition contains **12 detailed profiles**. The later scope
pilot retained additional raw candidates, which are not verified recommendations.
Every newly collected edition now runs the **full expanded plan**, rather than a
pilot subset. Existing reports and delivery receipts remain preserved.

The [October 1 expanded update](public/reports/2026-10-01/updates/r2/report.md)
adds **27 detailed guides and 38 screened discoveries**. The cumulative library
contained **77 tools as of that October 1 update**, including the original 12
guides. Current totals are shown in the live library; pending discoveries remain
clearly labeled until their complete profiles are finished.

## What an edition contains

Every featured tool includes an introduction, useful creative workflows, demos,
where to download it, installation and first-use steps, documented hardware and
software requirements, platform support, license/model-weight terms, costs,
maturity, limitations, and primary-source citations. The first edition establishes
a baseline. Later editions prioritize newly discovered projects and meaningful
updates to previously featured tools; unchanged tools stay in the library.

Each edition reports findings across 30 starter fields plus any newly added
fields. There is no fixed daily profile limit. The original examples below are
part of the expanded scope:

| Field | Examples |
| --- | --- |
| Images and design | generation, editing, inpainting, compositing |
| Video and animation | film workflows, video generation, motion |
| Audio, music, voice | composition, sound design, speech |
| 3D | reconstruction, textures, meshes, assets |
| Web | browser inference, WebGPU, media applications |
| WebXR, VR, AR | spatial interfaces, headset experiences |
| Computational art | creative coding, shaders, generative systems |
| Interactive and immersive | live video, installations, performance |
| Fabrication | generative CAD and 3D printing |
| Gaming | Blender automation and asset-production pipelines |

Additional starter fields include motion capture, avatars, VFX, spatial audio,
neural rendering, typography, publishing, storytelling, photography, visualization,
kinetic installations, stage media, fashion, accessibility, mobile creation,
learning, and preservation. See [`docs/SEARCH_SCOPE.md`](docs/SEARCH_SCOPE.md)
for adaptive search plans, projects beyond GitHub, and the review queue.

## How it works

The **Python collector** searches every GitHub term in recent-activity,
newly-created, and established-project lanes across all fields, checks a tool
watchlist, and scans recent
Hugging Face model updates. It archives responses, READMEs, release information,
source fingerprints, and collection failures. Search results are bounded samples,
not an exhaustive inventory. Star counts help shortlist candidates; they do not
establish creative quality.

Update detection distinguishes observed changes from **comparison pending**.
A fresh collection has not repeated the full license review yet, so a different
fingerprint alone does not establish an update. Published releases and changed
commits remain review signals; draft releases are ignored in both collection
paths. Failed source reads and incomplete comparisons stay pending. Before a
previously featured tool appears in a later daily report, complete the comparison
and confirm a useful creative change. Rechecking the same license, or adding
license evidence missing from an old pilot profile, is not itself a tool update.

GitHub searches now use up to 100 results per page and two pages per query,
without a minimum-star filter. The default plan has **63 terms × 3 lanes = 189
repository queries**. Recent activity and creation searches sort by updates;
the established-project lane has no age filter. The research agent can add
queries, categories, model tasks and deeper pagination each day. Hugging Face
searches cover 13 model tasks with up to 50 leads per task. Collected metadata
is retained for subsequent review, including earlier pilot discoveries.
`plan` previews the full plan without collecting sources; `verify-search` checks
that every planned GitHub query and model task was attempted. Missing attempts
block new report builds. Failed, partial and truncated sources are explicitly
counted as coverage gaps; an attempted query is not proof of complete results.
Reports and the library distinguish raw candidates, screened discoveries and
complete profiles.

Daily plan files must contain a JSON object, with lists for added categories,
queries and model tasks. Missing files or malformed entries fail with a clear
JSON error before source collection. Re-running `discover` preserves the original
observation. If you supply `--plan` again, its effective plan must match the
archived plan, using that day's archived defaults. A changed plan is rejected;
save the new scope for the next edition. Omit `--plan` to resume older observations
that have no archived expanded plan. See the [plan format](docs/SEARCH_SCOPE.md).

The **Codex research agent** supplements discovery with broad live web searches,
checks official documentation, model cards and complete software licenses, and writes structured
profiles. This is an agent-assisted workflow: the collector itself does not
invent installation instructions or call an additional LLM API. Profiles must cite
their sources, and unsupported facts remain unknown. Each new edition records
research or explicit gaps for GitLab, Codeberg, SourceHut, package registries,
creative plugin ecosystems, project sites, released research code and
international projects. These source groups are starting points too.
`review-backlog` exposes all retained candidates without a full profile, with
screened leads first; the automatic evidence shortlist is never a profile quota.

The **report builder** validates the profiles, produces HTML/Markdown/JSON,
seals artifacts with SHA-256 hashes, and updates a searchable static archive.
The research agent exports the finished edition to `public/`, synchronizes code,
documentation and reports through a protected GitHub pull request, and checks
CI on the merged main commit. A verified sync checkpoint is required for email.
That main CI run also deploys the verified `public/` library to GitHub Pages.
The **Gmail plugin** then sends the complete edition. A persistent reservation and
receipt block duplicate automatic sends, including after an interrupted run.
There is no 12-tool cap. Detailed profiles remain fully cited; additional projects
screened for open-source licensing and creative AI use can appear in a labeled
appendix and persistent review queue. Large editions attach the complete HTML
and Markdown with a short inline email summary.

The daily Codex automation uses the workflow in
[`docs/DAILY_WORKFLOW.md`](docs/DAILY_WORKFLOW.md). For local scheduled work the
computer must be awake and the desktop app running; network and Gmail access must
be available. The 8:00 AM schedule is the research start time, so email follows
when research and validation finish. [Official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app).

## Run and inspect

Python **3.10+** is sufficient on macOS/Linux. The project has no third-party
runtime dependencies. GitHub authentication from an existing `gh` login is used
in memory, or supply `GITHUB_TOKEN`/`GH_TOKEN` through your environment. No token
is written into reports. Unauthenticated GitHub access has lower rate limits;
source failures remain visible in the edition. Delivery needs the connected
Gmail plugin in the Codex chat.

Publication also requires Git, the GitHub CLI (`gh`), and write access to the
configured repository. For your own fork, update `github_sync.repository` in
`config/scout.json`. See [GitHub publication instructions](docs/GITHUB_SYNC.md).

Clone the project and create your private settings file:

```sh
git clone https://github.com/wenjunii/ai-media-tools.git
cd ai-media-tools
cp config/scout.local.json.example config/scout.local.json
```

Edit `config/scout.local.json` to set your authorized email recipient. It can
also override the time zone, research time, and hardware preference. Keep tokens
and passwords out of this file; credentials come from the environment or the
connected app. This file is ignored by Git, and the public defaults have no
email recipient.

Settings are validated when a command starts. Use a valid IANA time-zone name
such as `America/New_York`, a 24-hour `HH:MM` research time, and a valid recipient
address. Invalid settings produce a clear JSON error and exit without continuing.
The `github_sync.required_before_email` option must be a JSON boolean.

Ask Codex to schedule the workflow in this checkout with your approved recipient
and preferred time. The schedule and Gmail connection belong to your local
Codex app; cloning the repository does not create them. Configure the recipient
before building an edition intended for email, because a sealed edition keeps
its original delivery settings.

From the project root:

```sh
python3 -m media_scout doctor
python3 -m media_scout status
python3 -m media_scout plan
python3 -m media_scout review-backlog
python3 -m media_scout discover
# Optional: discover --plan research/YYYY-MM-DD/search-plan.json
python3 -m media_scout verify-search
# The research agent now writes research/YYYY-MM-DD/editorial.json.
python3 -m media_scout build --editorial research/YYYY-MM-DD/editorial.json
python3 -m media_scout verify --date YYYY-MM-DD
python3 -m media_scout export-report --date YYYY-MM-DD
python3 -m media_scout verify-public-archive
# Follow docs/GITHUB_SYNC.md: audit, commit, push, merge the PR, and wait for main CI.
python3 -m media_scout record-sync --date YYYY-MM-DD
python3 -m media_scout verify-sync --date YYYY-MM-DD
python3 -m media_scout prepare-email --date YYYY-MM-DD
# Send the returned outbox JSON once with the connected Gmail send_email tool.
python3 -m media_scout record-delivery --date YYYY-MM-DD --message-id GMAIL_ID
```

The date defaults to today in the configured time zone. `discover` resumes an existing
daily observation. `build` resumes the same sealed edition. Neither command
silently refreshes a completed report. `prepare-email` only creates a send
reservation and MIME payload; it does not send mail. Never call it as a casual
preview. It blocks before reservation when GitHub sync or CI is missing, failed,
or stale. `status`, `verify`, `verify-public-archive`, and `verify-sync` are read-only
checks; the last one contacts GitHub to check the actual commit and CI.
`verify-public-archive` checks the published files without private research,
delivery settings, or GitHub access, so it also works in a fresh clone.

`status` now shows every original and updated edition for the requested date,
including prepared, built and exported state, full-guide counts, screened-lead
counts and available search coverage. Its top-level counts describe the original
edition by default; `latest_completed_edition` identifies the newest built or
exported revision. `library` gives the verified, deduplicated totals from all
finished public editions, separating full guides from pending discoveries.
For October 1, these totals are 77 tools: 39 full guides and 38 screened leads.

```sh
python3 -m media_scout status --date YYYY-MM-DD
# Inspect an existing first update without preparing or rebuilding it:
python3 -m media_scout status --date YYYY-MM-DD --revision 2
```

Status verifies local seals, update identities, matching local/public report bytes
and the public library. A fresh clone can inspect published revisions without
private research; `built: false` means no local seal, while `exported: true` means
the verified public files exist. A prepared, unfinished revision is not counted
as the latest completed edition. The default status retains the original email
receipt; revision-specific status does not imply a separate send. Its publication
checkpoint is a saved record, and `publication_remote_checked` is always false.
Use `verify-sync` to check the actual GitHub commit and CI. Inspection never
collects sources, writes artifacts, reserves email or contacts GitHub.

An explicitly requested same-day update can add a separately sealed edition
without replacing the original report or resetting its email receipt. Use
`prepare-update`, the research commands with `--revision 2`, and `export-update`;
see [the update workflow](docs/REPORT_UPDATES.md). Both editions enter the searchable
library with distinct filters, review history and report links. Updates follow
the same expanded search, license review and protected GitHub publication checks.

Supplementary repositories found on the web can be archived before sealing:

```sh
python3 -m media_scout add-repository OWNER/REPO --categories video interactive
```

For every new full profile or screened lead, read its complete LICENSE and any
extra terms, then archive the review with `review-license OWNER/REPO --spdx ID
--note 'A substantive account of the reviewed terms'`. GitHub's recognized SPDX
label alone does not fulfill this requirement. Cite the archived license URL.
An open-source claim in a README is not enough.
Non-commercial source licenses cannot be relabeled as open source.

## Library and files

The [GitHub Pages library](https://wenjunii.github.io/ai-media-tools/) lets anyone
search the collection. Search covers introductions, creative uses, requirements,
installation commands, licenses, and earlier reviews. Combine creative-field,
platform-mention, software-license, review-depth, and daily-edition filters.
Open a tool to read its full guide, choose a dated review, or copy a profile link.
The Daily reports view provides HTML, Markdown, and JSON editions.
New editions also show executed-search counts, raw source/model candidates,
review counts and collection gaps. The initial edition predates this tracking;
the web UI labels it accordingly instead of claiming expanded research was done.

The library deduplicates tools by ID while keeping every published profile and
screened discovery. A completed guide remains available when a later edition
mentions the tool briefly. Pending profiles stay clearly labeled. New creative
fields are retained. There is no fixed library size limit; results load in batches.
See [library and Pages instructions](docs/LIBRARY.md).

Refresh the derived library from the finished public reports without collecting,
rebuilding, or sending a daily report:

```sh
python3 -m media_scout build-library
python3 -m media_scout verify-public-archive
```

Daily `export-report` refreshes it automatically. A fresh clone can rebuild the
complete public library without private research or email settings.
Open `site/index.html` for the local web UI, or serve the checkout locally:

```sh
cd /path/to/ai-media-tools
python3 -m http.server 8766 --bind 127.0.0.1
# http://127.0.0.1:8766/site/
```

Keep that terminal running. Stop it with Ctrl+C. If the library is already
running, open the URL instead of starting another server. A fresh clone needs
`build-library` once to create `site/` from its public editions.

| Path | Purpose |
| --- | --- |
| `config/scout.json` | public defaults, fields, discovery queries |
| `config/scout.local.json.example` | template for private delivery preferences |
| `config/scout.local.json` | ignored local recipient, time zone, time, hardware preference |
| `research/YYYY-MM-DD/discovery.json` | candidates and exact source coverage |
| `research/YYYY-MM-DD/evidence/` | archived primary-source material |
| `research/YYYY-MM-DD/editorial.json` | researched, cited tool profiles |
| `reports/YYYY-MM-DD/report.html` | complete readable edition and email body |
| `reports/YYYY-MM-DD/report.md` | portable text edition |
| `reports/YYYY-MM-DD/report.json` | structured profiles |
| `reports/YYYY-MM-DD/manifest.json` | immutable artifact hashes |
| `public/reports/YYYY-MM-DD/` | published finished editions and recipient-free hashes |
| `public/README.md` | browsable daily report list on GitHub |
| `public/index.html` | public searchable library, with corrected report links |
| `public/library.json` | cumulative tool data with every published review |
| `public/assets/` | dependency-free library styles and browser search |
| `site/index.html` | filterable local library and report archive |
| `state/catalog.json` | previous profiles and update tracking |
| `state/discovery_catalog.json` | collected source candidates across days |
| `state/review_queue.json` | screened discoveries awaiting complete profiles |
| `state/deliveries/YYYY-MM-DD.json` | Gmail message ID and delivery state |
| `state/publications/YYYY-MM-DD.json` | ignored verified GitHub sync checkpoint |
| `state/publication_history/YYYY-MM-DD/` | ignored copies of prior sync checkpoints when main changes |

Private settings, raw research, original reports, and operational state are ignored by Git. Keep or
back up these folders to retain history and delivery safeguards. Changing a
time in the JSON does not change an existing Codex schedule; update the existing
automation through the app and keep the config consistent.

## Verification

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q media_scout tests
python3 -m media_scout verify-public-archive
node --test tests/library.test.cjs
```

Regression checks cover integrity, missing citations/coverage, license conflicts,
HTML escaping, safe links, cross-host credential handling, unchanged profiles,
and duplicate or uncertain email delivery. A successful Gmail message ID records
acceptance by Gmail; it does not independently prove inbox placement.
Update-detection checks cover fresh license reviews, legacy fingerprints,
changed README/license text, commit and release signals, ignored drafts,
failed source reads and recovery, and blocked repeat profiles while a comparison
is pending. Existing fingerprint formats and sealed editions are preserved.
Library checks cover shortlist transfer, merge/deduplication, malformed imports,
missing tools, and research-note exports with dated evidence and pending details.
Checks also cover pagination, partial source failures, zero-star candidates,
new daily fields, external-project evidence, creative AI eligibility, editions
above 12 profiles, and complete large-report attachments.
Expanded-search checks cover all three lanes, omitted queries/model tasks,
altered plan identities, deeper-page overrides, source-gap disclosure,
historical pilot candidates, archived license evidence and web ecosystem coverage.
Plan validation and resume checks cover malformed input, missing plan files,
changed daily plans, archived-default consistency, and preservation of observations
and catalogs when a resume is rejected.
Publication checks cover report byte integrity, private-data screening, actual
Git commit agreement, current main CI, stale checkpoints, and blocking email
before reservation when publication is incomplete.
The public archive check validates each edition's files, hashes, dates, counts,
publication metadata, report list, and library links. It also reconstructs the
cumulative library and checks its complete data, HTML and browser assets.
CI runs this check alongside the regression suite on Python 3.10 and 3.13 and
the browser search checks using the runner's Node.js. Node is only needed for
those development tests; the library requires no backend or JavaScript build step.
The publication audit also rejects
changes or removal of previously committed editions, even if their metadata is
changed to match. Publish new findings in a new dated edition or an explicitly
requested, separately sealed update.

For code or documentation maintenance, run these checks, stage the reviewed
changes explicitly, and run `python3 -m media_scout audit-publication`. Follow the
protected PR and exact-commit CI steps in [the sync guide](docs/GITHUB_SYNC.md),
then refresh `record-sync` and check `verify-sync` for the existing edition. Keep
completed reports, research, delivery receipts, private settings, and the existing
schedule intact. Maintenance does not require discovery, rebuilding or exporting
a report, or preparing or sending email. Updating the sync checkpoint preserves
its previous bytes in the local publication history. When deliberately changing
the library UI or its data format, run `build-library` to update the derived
files before staging; the dated report files remain immutable.

## License

AI Media Scout is licensed under the [MIT License](LICENSE).
