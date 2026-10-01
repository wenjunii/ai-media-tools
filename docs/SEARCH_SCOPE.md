# Open-ended search scope

The scope is **only open-source AI tools**, for **any digital media or creative
workflow**. The user's examples are starting points, not an eligibility boundary.
A promising tool may be an application, plugin, library, workflow engine, local
model runner, browser tool, installation component, or usable research release.
Its actual AI contribution and creative use must be documented.

The 30 configured starter fields cover images, film, sound, 3D, web, XR, creative
coding, immersive/live work, fabrication, games, motion capture, avatars, VFX,
spatial/volumetric media, scanning, post-production, vector graphics, typography,
storytelling, publishing, photography, data art, physical installations, stage
media, fashion, accessibility, mobile creation, learning, and preservation.
**Emerging fields can be added at runtime without changing Python code.**

## Discovery breadth and evidence

- GitHub: 63 starter queries, recent activity and newly-created lanes; 100
  results per page and two pages per query by default. There is no minimum-star
  filter. A daily plan can add queries and request deeper pagination.
- Hugging Face: 13 model-task searches, up to 50 leads per task. A model update
  remains a lead until its code, weight terms and useful creative workflow are
  checked.
- Web research: search beyond repositories, including GitLab, Codeberg,
  SourceHut, package registries, creative host/plugin ecosystems, project sites,
  official releases/demos, and primary research with released software.
  Community directories and announcements are discovery aids; recommendations
  require primary evidence.
- Adaptive research: pursue newly observed terminology, adjacent practices,
  non-English projects, unfamiliar host ecosystems and cross-disciplinary uses.
  A project does not have to fit a starter field to qualify.
- History: keep all collected metadata in `state/discovery_catalog.json`; preserve
  complete daily observations, reviewed profiles and the pending-review queue.

Each GitHub query records pages retrieved, total matches, incomplete results,
truncation and failures. If a query is too broad, split it by dates, topic,
platform or workflow in the daily plan, or add pages up to the source's search
limit. Do not describe bounded results as an exhaustive inventory. Source limits
and research time are real constraints; no tool count is a quality target.

## Add new fields and queries

Before discovery, the research agent can save
`research/YYYY-MM-DD/search-plan.json`:

```json
{
  "report_date": "YYYY-MM-DD",
  "additional_categories": [
    {"id": "haptics", "name": "Tactile and haptic AI media", "queries": ["AI haptic art"]}
  ],
  "queries": [
    {"category": "haptics", "terms": "generative tactile media", "window": "pushed", "sort": "updated", "pages": 3},
    {"category": "frontier", "terms": "AI creative toolkit", "window": "created", "sort": "updated"}
  ]
}
```

Run `python3 -m media_scout discover --date YYYY-MM-DD --plan research/YYYY-MM-DD/search-plan.json`.
The observation archives the effective plan and configuration. Include one sourced
coverage finding for every observed field, including the new categories. Do not
rewrite a day's existing observation or sealed edition to change its scope.

## Projects outside GitHub

The researcher reads official documentation and the complete software license,
then saves both as UTF-8 snapshots under that day's evidence folder. Register the
project with `python3 -m media_scout add-project --date YYYY-MM-DD --metadata PATH.json`.
Example metadata:

```json
{
  "name": "Project name",
  "project_url": "https://gitlab.com/owner/project",
  "categories": ["frontier"],
  "code_license": "MIT",
  "ai_relevance": "Specific documented use of an AI model in a creative workflow.",
  "overview": {
    "path": "research/YYYY-MM-DD/evidence/project.md",
    "url": "https://gitlab.com/owner/project"
  },
  "license": {
    "path": "research/YYYY-MM-DD/evidence/project-LICENSE.txt",
    "url": "https://gitlab.com/owner/project/-/blob/main/LICENSE",
    "reviewed": true,
    "note": "Explain the actual reviewed license and any additional restrictions."
  }
}
```

This command archives evidence; it does not fetch arbitrary URLs or execute
software. Source snapshots must stay inside the daily evidence folder. Do not
register a non-commercial or proprietary code license as open source. Treat
model weights, required paid APIs and proprietary hosts separately.

## Complete profiles and additional discoveries

There is **no fixed maximum number of full profiles or screened discoveries**.
Write as many complete, well-supported profiles as the research supports. Full
profiles retain the original installation, first-use, demos, requirements and
quality checks, plus a cited `ai_relevance` explanation.

Use an optional `leads` appendix for additional projects already screened for
creative AI relevance and an open-source software license, with archived primary
evidence. Explain which installation, hardware or quality checks remain pending.
The appendix is not a list of equally verified recommendations. Every pending
lead is retained in `state/review_queue.json` and shown in the library; continue
its review in later editions. Unchanged pending leads are not re-listed daily.

Large editions include the complete HTML and Markdown as email attachments, with
a short inline summary. The complete report and archive are never reduced to a
fixed number of tools. The delivery reservation and one-email-per-day safeguards
still apply.
