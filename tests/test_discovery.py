"""Broad discovery tests use fake public APIs, without credentials or mail sends."""

from pathlib import Path
import tempfile
import unittest
from urllib.parse import parse_qs, urlparse

from media_scout.client import SourceError
from media_scout.discovery import collect, repository_search
from media_scout.external import add_project
from media_scout.planning import search_plan
from media_scout.report import build
from media_scout.storage import read_json, write_json, write_text


class FakeSearch:
    def __init__(self, pages):
        self.pages, self.calls = pages, []

    def get(self, url):
        self.calls.append(url)
        value = self.pages[int(parse_qs(urlparse(url).query)["page"][0]) - 1]
        if isinstance(value, Exception):
            raise value
        return value


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.spec = {"category": "frontier", "terms": "creative AI", "window": "created",
                     "sort": "updated", "pages": 2}

    def test_pagination_reaches_low_star_projects_on_later_pages(self):
        api = FakeSearch([
            {"total_count": 3, "items": [{"full_name": "a/one", "stargazers_count": 1},
                                        {"full_name": "b/two", "stargazers_count": 0}]},
            {"total_count": 3, "items": [{"full_name": "c/three", "stargazers_count": 0}]}])
        coverage, repos = repository_search(api, self.spec, "2026-09-01", self.root, 0, 2)
        self.assertEqual(len(repos), 3)
        self.assertEqual(coverage["pages_collected"], 2)
        self.assertFalse(coverage["truncated"])
        self.assertNotIn("stars:>", coverage["query"])
        self.assertIn("is:public", coverage["query"])
        self.assertEqual(len(list((self.root / "queries").glob("*.json"))), 2)

    def test_a_later_page_failure_keeps_first_page_and_reports_partial_coverage(self):
        api = FakeSearch([{"total_count": 4, "items": [{"full_name": "a/one"}, {"full_name": "b/two"}]},
                          SourceError("HTTP 403; source not collected")])
        coverage, repos = repository_search(api, self.spec, "2026-09-01", self.root, 0, 2)
        self.assertEqual(len(repos), 2)
        self.assertEqual(coverage["status"], "partial")
        self.assertTrue(coverage["truncated"])
        self.assertIn("403", coverage["error"])

    def test_search_stops_when_results_are_exhausted_and_omits_private_repositories(self):
        api = FakeSearch([{"total_count": 2, "items": [{"full_name": "a/public"},
                                                      {"full_name": "b/private", "private": True}]}])
        coverage, repos = repository_search(api, self.spec, "2026-09-01", self.root, 0, 100)
        self.assertEqual(len(api.calls), 1)
        self.assertEqual(len(repos), 1)

    def test_daily_plan_can_add_a_field_outside_the_starter_taxonomy(self):
        config = {"categories": [{"id": "images", "name": "Images", "queries": ["AI image"], "seeds": []}],
                  "pages_per_query": 2}
        extra = {"report_date": "2026-10-01",
                 "additional_categories": [{"id": "haptics", "name": "Tactile AI media",
                                             "queries": ["AI haptic art"]}],
                 "queries": [{"category": "haptics", "terms": "generative tactile media", "pages": 3}]}
        plan = search_plan(config, "2026-10-01", extra)
        self.assertEqual(len(plan["categories"]), 2)
        self.assertEqual(len(plan["queries"]), 7)
        self.assertEqual(plan["queries"][-1]["pages"], 3)
        self.assertEqual(len(config["categories"]), 1)

    def test_malformed_or_mismatched_daily_plan_is_rejected(self):
        config = {"categories": [{"id": "frontier", "name": "Frontier", "queries": []}]}
        with self.assertRaisesRegex(ValueError, "date"):
            search_plan(config, "2026-10-01", {"report_date": "2026-10-02"})
        with self.assertRaisesRegex(ValueError, "unique safe"):
            search_plan(config, "2026-10-01", {"additional_categories": [{"id": "../private", "name": "Bad"}]})

    def test_effective_plan_is_collected_deduplicated_archived_and_resumable(self):
        repo = {"full_name": "test/creative-ai", "html_url": "https://github.com/test/creative-ai",
                "name": "Creative AI", "license": {"spdx_id": "MIT"}, "stargazers_count": 0,
                "created_at": "2026-09-20T00:00:00Z"}
        class Source:
            def __init__(self):
                self.calls = []
            def get(self, url, **kwargs):
                self.calls.append(url)
                if "/search/repositories?" in url:
                    return {"total_count": 1, "items": [repo]}
                if url.endswith("/readme"):
                    return {"download_url": "https://raw.githubusercontent.com/test/creative-ai/main/README.md",
                            "html_url": "https://github.com/test/creative-ai/blob/main/README.md", "sha": "readme001"}
                if "raw.githubusercontent.com" in url:
                    return "Official documentation of local creative AI inference."
                if "/commits?" in url:
                    return [{"sha": "head001", "html_url": "https://github.com/test/creative-ai/commit/head001"}]
                return []
        source = Source()
        config = {"timezone": "America/New_York", "recipient": "example@example.com", "lookback_days": 30,
                  "items_per_query": 100, "pages_per_query": 2, "max_profiles": None,
                  "categories": [{"id": "frontier", "name": "Creative AI", "queries": ["creative AI"], "seeds": []}],
                  "huggingface_pipelines": []}
        write_json(self.root / "config/scout.json", config)
        plan_path = self.root / "search-plan.json"
        write_json(plan_path, {"report_date": "2026-10-01",
            "additional_categories": [{"id": "haptics", "name": "Tactile AI", "queries": ["AI haptic"]}]})
        observation = collect("2026-10-01", self.root, source, plan_path)
        self.assertEqual(len(observation["candidates"]), 1)
        self.assertEqual(set(observation["candidates"][0]["categories"]), {"frontier", "haptics"})
        self.assertEqual(len(read_json(self.root / "state/discovery_catalog.json")), 1)
        calls = len(source.calls)
        self.assertEqual(collect("2026-10-01", self.root, source, plan_path), observation)
        self.assertEqual(len(source.calls), calls)
        editorial_path = self.root / "editorial.json"
        write_json(editorial_path, {"report_date": "2026-10-01", "summary": "No fully reviewed tools today.",
                    "tools": [], "category_notes": [{"category": c["id"], "text": "Research lead pending.",
                         "source_urls": ["https://github.com/test/creative-ai"]} for c in observation["categories"]]})
        self.assertEqual(build(editorial_path, self.root)["profile_count"], 0)


class ExternalProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.day = "2026-10-01"
        write_json(self.root / "config/scout.json", {"timezone": "America/New_York",
                    "categories": [{"id": "frontier", "name": "Emerging media"}]})
        write_json(self.root / "research" / self.day / "discovery.json",
                   {"report_date": self.day, "window_start": "2026-09-01", "candidates": []})
        overview = f"research/{self.day}/evidence/project.md"
        license_path = f"research/{self.day}/evidence/license.txt"
        write_text(self.root / overview, "Official model-based creative image application documentation.")
        write_text(self.root / license_path, "Fixture for a complete MIT license reviewed by the researcher.")
        self.meta = {"name": "External creative model tool", "project_url": "https://gitlab.com/example/art",
                     "categories": ["frontier"], "code_license": "MIT",
                     "ai_relevance": "Uses local image-model inference to create editable digital artwork.",
                     "overview": {"path": overview, "url": "https://gitlab.com/example/art"},
                     "license": {"path": license_path, "url": "https://gitlab.com/example/art/-/blob/main/LICENSE",
                                 "reviewed": True, "note": "Reviewed the complete MIT terms; no extra non-commercial restriction."}}
        self.path = self.root / "metadata.json"

    def add(self):
        write_json(self.path, self.meta)
        return add_project(self.path, self.day, self.root)

    def test_non_github_project_retains_canonical_identity_and_license_evidence(self):
        item = self.add()
        self.assertEqual(item["id"], "external:https://gitlab.com/example/art")
        self.assertEqual(item["code_license"], "MIT")
        self.assertTrue((self.root / item["license_review"]["path"]).exists())
        self.assertEqual(len(read_json(self.root / "research" / self.day / "discovery.json")["candidates"]), 1)

    def test_external_evidence_cannot_escape_daily_evidence_folder(self):
        write_text(self.root / "private.txt", "Private unrelated file")
        self.meta["overview"]["path"] = "private.txt"
        with self.assertRaisesRegex(ValueError, "daily evidence"):
            self.add()

    def test_noncommercial_software_cannot_be_registered_as_open_source(self):
        self.meta["code_license"] = "CC-BY-NC-SA-4.0"
        with self.assertRaisesRegex(ValueError, "open-source SPDX"):
            self.add()


if __name__ == "__main__":
    unittest.main()
