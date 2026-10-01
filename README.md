# AI Media Scout

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

The **Python collector** searches GitHub in recent-activity and newly-created
lanes across all fields, checks an established-tool watchlist, and scans recent
Hugging Face model updates. It archives responses, READMEs, release information,
source fingerprints, and collection failures. Search results are bounded samples,
not an exhaustive inventory. Star counts help shortlist candidates; they do not
establish creative quality.
GitHub searches now use up to 100 results per page and two pages per query,
without a minimum-star filter. The default plan has 63 queries; the research
agent can add queries, categories, and deeper pagination each day. Hugging Face
searches cover 13 model tasks with up to 50 leads per task. Collected metadata
is retained for subsequent review.

The **Codex research agent** supplements discovery with broad live web searches,
checks official documentation, model cards and licenses, and writes structured
profiles. This is an agent-assisted workflow: the collector itself does not
invent installation instructions or call an additional LLM API. Profiles must cite
their sources, and unsupported facts remain unknown.

The **report builder** validates the profiles, produces HTML/Markdown/JSON,
seals artifacts with SHA-256 hashes, and updates a searchable static archive.
The research agent exports the finished edition to `public/`, synchronizes code,
documentation and reports through a protected GitHub pull request, and checks
CI on the merged main commit. A verified sync checkpoint is required for email.
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

Ask Codex to schedule the workflow in this checkout with your approved recipient
and preferred time. The schedule and Gmail connection belong to your local
Codex app; cloning the repository does not create them. Configure the recipient
before building an edition intended for email, because a sealed edition keeps
its original delivery settings.

From the project root:

```sh
python3 -m media_scout doctor
python3 -m media_scout status
python3 -m media_scout discover
# Optional: discover --plan research/YYYY-MM-DD/search-plan.json
# The research agent now writes research/YYYY-MM-DD/editorial.json.
python3 -m media_scout build --editorial research/YYYY-MM-DD/editorial.json
python3 -m media_scout verify --date YYYY-MM-DD
python3 -m media_scout export-report --date YYYY-MM-DD
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
or stale. `status`, `verify`, and `verify-sync` are read-only checks; the last one
contacts GitHub to check the actual commit and CI.

Supplementary repositories found on the web can be archived before sealing:

```sh
python3 -m media_scout add-repository OWNER/REPO --categories video interactive
```

If GitHub cannot classify a license, read its full LICENSE and review any extra
terms before using `review-license`. An open-source claim in a README is not enough.
Non-commercial source licenses cannot be relabeled as open source.

## Library and files

Open `site/index.html` for the searchable tool library, or serve the folder locally:

```sh
python3 -m http.server 8766 --bind 127.0.0.1
# http://127.0.0.1:8766/site/
```

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
| `site/index.html` | filterable local library and report archive |
| `state/catalog.json` | previous profiles and update tracking |
| `state/discovery_catalog.json` | collected source candidates across days |
| `state/review_queue.json` | screened discoveries awaiting complete profiles |
| `state/deliveries/YYYY-MM-DD.json` | Gmail message ID and delivery state |
| `state/publications/YYYY-MM-DD.json` | ignored verified GitHub sync checkpoint |

Private settings, raw research, original reports, and operational state are ignored by Git. Keep or
back up these folders to retain history and delivery safeguards. Changing a
time in the JSON does not change an existing Codex schedule; update the existing
automation through the app and keep the config consistent.

## Verification

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q media_scout
```

Regression checks cover integrity, missing citations/coverage, license conflicts,
HTML escaping, safe links, cross-host credential handling, unchanged profiles,
and duplicate or uncertain email delivery. A successful Gmail message ID records
acceptance by Gmail; it does not independently prove inbox placement.
Checks also cover pagination, partial source failures, zero-star candidates,
new daily fields, external-project evidence, creative AI eligibility, editions
above 12 profiles, and complete large-report attachments.
Publication checks cover report byte integrity, private-data screening, actual
Git commit agreement, current main CI, stale checkpoints, and blocking email
before reservation when publication is incomplete.

## License

AI Media Scout is licensed under the [MIT License](LICENSE).
