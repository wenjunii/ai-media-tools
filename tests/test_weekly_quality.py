"""Weekly coverage includes every tier without manufacturing quality evidence."""

from copy import deepcopy
from contextlib import redirect_stdout
from io import StringIO
import json
import unittest
from unittest.mock import patch

import test_quality
from media_scout import cli
from media_scout.configuration import load_config
from media_scout.library import make_library
from media_scout.publication import export_report
from media_scout.quality import CHECKS, TIERS, read_reviews, record_quality_reviews
from media_scout.storage import read_json, write_json
from media_scout.weekly import weekly_quality


class WeeklyQualityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_quality.QualityTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.fixture.fixture.build()
        export_report(self.fixture.fixture.day, self.root)
        self.config_path = self.root / "config/scout.json"
        config = read_json(self.config_path)
        config["weekly_quality_review"] = {"enabled": True, "starts_on": "2026-10-26"}
        write_json(self.config_path, config)

    def record_review(self, day, *, method="source-review", sources=True):
        assessment = self.fixture.ready_assessment()
        assessment.update(tier="unverified", checked_on=day, method=method)
        if not sources:
            assessment["sources"] = []
            for check in assessment["checks"].values():
                check.update(status="unknown", source_urls=[])
        path, batch = self.fixture.review_batch(assessment)
        next(iter(batch["reviews"].values()))["checked_on"] = day
        write_json(path, batch)
        record_quality_reviews(self.root, path, apply=True)

    def test_first_monday_gate_and_read_only_planning(self):
        before = {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        with patch("urllib.request.urlopen", side_effect=AssertionError("No network for planning")):
            scheduled = weekly_quality(self.root, "2026-10-25")
            due = weekly_quality(self.root, "2026-10-26")
        self.assertEqual(scheduled["state"], "scheduled")
        self.assertFalse(scheduled["due"])
        self.assertEqual(scheduled["week_start"], "2026-10-26")
        self.assertEqual(due["state"], "due")
        self.assertEqual(due["remaining"], due["total"])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_every_tier_and_screened_lead_get_all_six_rechecks(self):
        data = make_library([self.fixture.report], self.fixture.config)
        prototype = data["tools"][0]
        tools = []
        for index, tier in enumerate(TIERS):
            tool = deepcopy(prototype)
            tool["id"] = f"github:owner/tool-{index}"
            assessment = self.fixture.assessment()
            assessment["tier"] = tier
            if tier == "ready_to_try":
                assessment = self.fixture.ready_assessment()
            if tier == "experimental":
                assessment["experimental_reason"] = {
                    "text": "The scoped export workflow is explicitly unfinished in the current documentation.",
                    "source_urls": [assessment["sources"][0]["url"]],
                }
            tool["quality_assessment"] = assessment
            tools.append(tool)
        screened = deepcopy(tools[-1])
        screened["id"] = "gitlab:independent/creative-tool"
        screened["versions"][0]["kind"] = "screened"
        tools.append(screened)
        data["tools"] = tools
        data["quality_counts"] = {tier: sum(t["quality_assessment"]["tier"] == tier for t in tools) for tier in TIERS}
        with patch("media_scout.weekly.public_quality_library", return_value=data):
            result = weekly_quality(self.root, "2026-10-26")
        self.assertEqual(result["total"], 5)
        self.assertEqual(result["remaining"], 5)
        self.assertEqual(result["remaining_by_tier"]["recommended"], 1)
        self.assertTrue(next(row for row in result["items"] if row["id"] == screened["id"])["needs_profile"])
        for row in result["items"]:
            self.assertEqual([check["check"] for check in row["refresh_checks"]], list(CHECKS))

    def test_current_cited_review_counts_without_promoting_its_label(self):
        self.record_review("2026-10-26")
        before = read_reviews(self.root)
        result = weekly_quality(self.root, "2026-10-26")
        self.assertEqual(result["state"], "complete")
        self.assertEqual(result["reviewed_this_week"], 1)
        self.assertEqual(result["remaining"], 0)
        self.assertEqual(result["quality_counts"]["unverified"], 1)
        self.assertEqual(before, read_reviews(self.root))

    def test_record_audit_and_uncited_review_never_count_as_current_source_checks(self):
        for method, sources in (("published-record-audit", True), ("source-review", False)):
            self.record_review("2026-10-26", method=method, sources=sources)
            with self.subTest(method=method, sources=sources):
                result = weekly_quality(self.root, "2026-10-26")
                self.assertEqual(result["reviewed_this_week"], 0)
                self.assertEqual(result["items"][0]["review_reason"], "source_review_needed")

    def test_future_assessment_is_explicitly_pending(self):
        self.record_review("2026-10-27")
        result = weekly_quality(self.root, "2026-10-26")
        self.assertEqual(result["reviewed_this_week"], 0)
        self.assertEqual(result["future_assessment_ids"], [result["items"][0]["id"]])
        self.assertEqual(result["items"][0]["review_reason"], "future_assessment_date")

    def test_daily_resume_and_monday_reset_across_daylight_saving(self):
        result = weekly_quality(self.root, "2026-10-27")
        self.assertEqual(result["week_start"], "2026-10-26")
        self.assertTrue(result["due"])
        self.record_review("2026-10-27")
        sunday = weekly_quality(self.root, "2026-11-01")
        self.assertEqual(sunday["state"], "complete")
        self.assertEqual(sunday["week_start"], "2026-10-26")
        monday = weekly_quality(self.root, "2026-11-02")
        self.assertEqual(monday["state"], "due")
        self.assertEqual(monday["next_week_start"], "2026-11-09")

    def test_latest_record_replaces_an_old_binding_even_in_the_same_week(self):
        self.record_review("2026-10-26")
        report = deepcopy(self.fixture.report)
        report["report_date"] = "2026-10-26"
        for tool in report["tools"]:
            tool["checked_on"] = "2026-10-26"
        data = make_library([report], self.fixture.config, read_reviews(self.root))
        with patch("media_scout.weekly.public_quality_library", return_value=data):
            result = weekly_quality(self.root, "2026-10-27")
        self.assertEqual(result["reviewed_this_week"], 0)
        self.assertEqual(result["items"][0]["basis_edition"], "2026-10-26")
        self.assertTrue(result["items"][0]["needs_source_review"])

    def test_empty_library_is_not_a_completed_review(self):
        data = make_library([], self.fixture.config)
        with patch("media_scout.weekly.public_quality_library", return_value=data):
            result = weekly_quality(self.root, "2026-10-26")
        self.assertEqual(result["state"], "empty")
        self.assertFalse(result["due"])
        self.assertEqual(result["total"], 0)

    def test_disabled_and_missing_schedule_are_not_due(self):
        for schedule in (None, {"enabled": False, "starts_on": "2026-10-26"}):
            config = read_json(self.config_path)
            config.pop("weekly_quality_review", None)
            if schedule is not None:
                config["weekly_quality_review"] = schedule
            write_json(self.config_path, config)
            self.assertEqual(weekly_quality(self.root, "2026-10-26")["state"], "disabled")
            self.assertFalse(weekly_quality(self.root, "2026-10-26")["due"])

    def test_invalid_schedule_is_rejected_without_coercion(self):
        bad = [None, [], {}, {"enabled": "yes", "starts_on": "2026-10-26"},
               {"enabled": True, "starts_on": None}, {"enabled": True, "starts_on": ""},
               {"enabled": True, "starts_on": "2026-10-27"},
               {"enabled": True, "starts_on": "2026-02-30"},
               {"enabled": True, "starts_on": "2026-10-26", "extra": "ignored?"}]
        for settings in bad:
            config = read_json(self.config_path)
            config["weekly_quality_review"] = settings
            write_json(self.config_path, config)
            with self.subTest(settings=settings), self.assertRaises(ValueError):
                load_config(self.root)

    def test_cannot_claim_historical_coverage_before_current_library_exists(self):
        with self.assertRaisesRegex(ValueError, "predate the current library"):
            weekly_quality(self.root, "2026-09-30")

    def test_summary_and_full_cli_share_unfiltered_counts(self):
        for args in ([], ["--full"]):
            output = StringIO()
            with patch.object(cli, "ROOT", self.root), redirect_stdout(output), \
                    patch("sys.argv", ["media-scout", "weekly-quality", "--date", "2026-10-26", *args]):
                self.assertEqual(cli.main(), 0)
            result = json.loads(output.getvalue())
            self.assertEqual(result["total"], 1)
            self.assertEqual(result["remaining"], 1)
            self.assertEqual("items" in result, bool(args))


if __name__ == "__main__":
    unittest.main()
