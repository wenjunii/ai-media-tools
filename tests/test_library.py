"""Cumulative library history, safe data export and clone portability."""

import copy
import json
import unittest

import test_workflow
from media_scout.library import SEARCH_COUNTS, library_files, make_library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_workflow.WorkflowTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.config = self.fixture.config
        self.report = copy.deepcopy(self.fixture.editorial)

    def later(self, day="2026-10-02"):
        report = copy.deepcopy(self.report)
        report["report_date"] = day
        for tool in report["tools"]:
            tool["checked_on"] = day
        return report

    def lead(self, day):
        tool = self.report["tools"][0]
        return {"id": tool["id"], "name": tool["name"], "categories": tool["categories"],
                "checked_on": day, "good_for": "Interactive creative AI workflows",
                "code_license": "MIT", "review_status": "Full profile pending",
                "sources": tool["sources"], "ai_relevance": {"text": "An AI-assisted creative workflow",
                                                            "source_urls": [tool["sources"][0]["url"]]}}

    def test_every_dated_review_is_kept_with_one_entry_per_tool(self):
        later = self.later()
        later["tools"][0]["requirements"]["hardware"] = "A newly documented 8 GB GPU"
        data = make_library([later, self.report], self.config)
        self.assertEqual(data["counts"], {"tools": 1, "profiles": 1, "screened": 0, "editions": 2})
        entry = data["tools"][0]
        self.assertEqual(entry["first_seen"], "2026-10-01")
        self.assertEqual(entry["profile_date"], "2026-10-02")
        self.assertEqual([v["date"] for v in entry["versions"]], ["2026-10-02", "2026-10-01"])
        self.assertEqual(entry["versions"][1]["profile"]["requirements"]["hardware"], "Not documented")

    def test_a_screened_discovery_becomes_a_complete_profile_without_duplication(self):
        earlier = dict(self.report, tools=[], leads=[self.lead("2026-10-01")])
        data = make_library([earlier, self.later()], self.config)
        self.assertEqual(data["counts"]["tools"], 1)
        self.assertEqual(data["tools"][0]["review"], "profile")
        self.assertEqual(data["tools"][0]["versions"][1]["kind"], "screened")

    def test_a_later_brief_mention_does_not_replace_a_complete_guide(self):
        later = dict(self.later(), tools=[], leads=[self.lead("2026-10-02")])
        entry = make_library([self.report, later], self.config)["tools"][0]
        self.assertEqual(entry["review"], "profile")
        self.assertEqual(entry["profile_date"], "2026-10-01")
        self.assertEqual(entry["last_seen"], "2026-10-02")
        self.assertIn("installation", entry["versions"][1]["profile"])

    def test_future_creative_fields_keep_their_published_names(self):
        self.report["tools"][0]["categories"] = ["tactile"]
        self.report["category_labels"] = {"tactile": "Tactile AI media"}
        data = make_library([self.report], self.config)
        self.assertEqual(data["categories"], [{"id": "tactile", "name": "Tactile AI media"}])

    def test_operational_or_unrecognized_profile_fields_are_not_copied(self):
        self.report["recipient"] = "private@example.com"
        self.report["tools"][0]["private_notes"] = "private@example.com"
        self.report["tools"][0]["installation"]["private_notes"] = "private@example.com"
        data = make_library([self.report], self.config)
        self.assertNotIn("private@example.com", json.dumps(data))

    def test_report_search_counts_are_preserved_without_private_research_metadata(self):
        self.report["search_coverage"] = {name: 0 for name in SEARCH_COUNTS}
        self.report["search_coverage"].update(source_candidates=540, full_profiles=1,
                                            private_notes="private@example.com")
        data = make_library([self.report], self.config)
        self.assertEqual(data["editions"][0]["search_coverage"]["source_candidates"], 540)
        self.assertNotIn("private@example.com", json.dumps(data))
        self.report["search_coverage"]["source_candidates"] = "private@example.com"
        with self.assertRaisesRegex(ValueError, "nonnegative counts"):
            make_library([self.report], self.config)

    def test_inline_source_text_cannot_break_out_of_the_data_script(self):
        data = make_library([self.report], self.config)
        html = library_files(data)["index.html"].decode()
        embedded = html.split('<script id="library-data" type="application/json">', 1)[1].split("</script>", 1)[0]
        self.assertNotIn("<", embedded)
        self.assertEqual(json.loads(embedded), data)
        self.assertIn('src="assets/library.js"', html)

    def test_repeated_generation_is_deterministic_and_keeps_relative_links(self):
        data = make_library([self.report], self.config)
        self.assertEqual(library_files(data), library_files(data))
        local = library_files(data, "../reports/")["index.html"].decode()
        self.assertIn('data-report-prefix="../reports/"', local)
        self.assertIn('href="../reports/2026-10-01/report.html"', local)

    def test_duplicate_tool_or_edition_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unique dates"):
            make_library([self.report, self.report], self.config)
        self.report["tools"].append(copy.deepcopy(self.report["tools"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate tool"):
            make_library([self.report], self.config)


if __name__ == "__main__":
    unittest.main()
