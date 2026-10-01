# Editorial JSON structure

The builder validates this structure; the research agent supplies the content.
All URLs must use HTTPS. Each section's source URLs must appear in `sources`.
Use actual source facts and mark unknowns. Use the candidate's canonical `id`,
observed software SPDX license, and exact `novelty` value from discovery.
The expanded scope requires a cited `ai_relevance` explanation. Cover all fields
from the effective daily plan, including added categories. There is no fixed
profile limit. Projects outside GitHub use their collected `external:https://...`
ID and actual primary-source URLs.

```json
{
  "report_date": "YYYY-MM-DD",
  "summary": "What the day offers creators, with accurate novelty and limitations.",
  "category_notes": [
    {"category": "images", "text": "Finding or explicit gap.", "source_urls": ["https://official.example/docs"]}
  ],
  "tools": [
    {
      "id": "github:owner/repository",
      "name": "Tool name",
      "categories": ["images", "web"],
      "maturity": "Established application / emerging tool / research prototype / developer library",
      "checked_on": "YYYY-MM-DD",
      "novelty": {"kind": "first-profile", "text": "Initial baseline, or concrete verified update."},
      "ai_relevance": {
        "text": "Explain the actual AI contribution to a concrete digital media workflow.",
        "source_urls": ["https://github.com/owner/repository"]
      },
      "sources": [
        {"title": "Official README", "url": "https://github.com/owner/repository"},
        {"title": "License", "url": "https://github.com/owner/repository/blob/main/LICENSE"}
      ],
      "introduction": {"text": "What it does.", "source_urls": ["https://github.com/owner/repository"]},
      "good_for": {"text": "Specific creative work it supports.", "source_urls": ["https://github.com/owner/repository"]},
      "demo": {"text": "Verified demo or published examples; clarify if no live demo exists.", "source_urls": ["https://github.com/owner/repository"]},
      "installation": {
        "text": "Recommended route and relevant platform alternatives.",
        "steps": ["Download the official release for your platform.", "Follow the documented setup."],
        "commands": [],
        "source_urls": ["https://github.com/owner/repository"]
      },
      "usage": {
        "text": "Practical first project.",
        "steps": ["Load an example.", "Change one input.", "Generate and export."],
        "source_urls": ["https://github.com/owner/repository"]
      },
      "requirements": {
        "text": "Qualify model-specific or undocumented limits.",
        "hardware": "Documented CPU, GPU, VRAM, RAM and storage, or not documented.",
        "software": "Documented versions, dependencies, models and keys.",
        "platforms": "Confirmed operating systems, browser/headset support, cloud alternatives.",
        "source_urls": ["https://github.com/owner/repository"]
      },
      "license": {
        "text": "Separate software and dependent components.",
        "code": "MIT",
        "weights": "Model-specific terms, with exact source if known.",
        "commercial": "Source-backed permissions and limits, or unverified.",
        "cost": "Local costs, paid services and hosts; avoid uncited current prices.",
        "source_urls": ["https://github.com/owner/repository/blob/main/LICENSE"]
      },
      "quality": {"text": "Concrete rationale for inclusion, distinguish observed facts from assessment.", "hands_on_tested": false, "source_urls": ["https://github.com/owner/repository"]},
      "limitations": {"text": "Known constraints and untested claims.", "source_urls": ["https://github.com/owner/repository"]},
      "links": {"repository": "https://github.com/owner/repository", "documentation": "https://official.example/docs"}
    }
  ]
}
```

Include all ten configured categories in `category_notes`. An edition with no
qualified new tools uses `"tools": []` and still includes its coverage findings.
