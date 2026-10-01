# Additional-discovery appendix

Add an optional `leads` list beside `tools` in editorial JSON. Every entry needs
an archived candidate, a matching recognized open-source software license, two
primary sources, a concrete cited creative AI use, and today's check date.
There is no count cap. A lead must not duplicate a full profile or repeat an
unchanged lead from an earlier edition.
For new editions, the candidate must also include an archived complete software
license review, even if the GitHub SPDX label is recognized. Use `review-license`
after reading the complete terms and cite its license URL below. `add-project`
provides the equivalent review for projects outside GitHub.

```json
{
  "id": "github:owner/repository",
  "name": "Project name",
  "categories": ["frontier"],
  "checked_on": "YYYY-MM-DD",
  "code_license": "MIT",
  "good_for": "A specific digital media or artistic workflow.",
  "ai_relevance": {
    "text": "Explain the actual documented AI model contribution to that workflow.",
    "source_urls": ["https://github.com/owner/repository"]
  },
  "review_status": "Installation and hardware review pending; output quality not tested.",
  "sources": [
    {"title": "Official overview", "url": "https://github.com/owner/repository"},
    {"title": "Reviewed license", "url": "https://github.com/owner/repository/blob/main/LICENSE"}
  ]
}
```

Unknown/custom/non-commercial software licenses do not qualify for this appendix.
Unscreened raw search candidates stay in the discovery catalog. A pending lead
is not presented as a fully verified recommendation. The builder stores eligible
leads in `state/review_queue.json` and exposes them in the library for follow-up.
