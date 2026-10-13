"""Recommendations require evidence; historical reports remain immutable."""

import copy
from contextlib import redirect_stdout
from io import StringIO
import json
import unittest
from unittest.mock import patch

import test_workflow
from media_scout import cli
from media_scout.library import make_library
from media_scout.publication import export_report, rebuild_library, verify_public_archive
from media_scout.quality import (CHECKS, audit_existing, baseline_assessment, evidence_gaps, quality_backlog,
                                 read_reviews, record_binding, review_item, validate_assessment)
from media_scout.report import render_html, render_markdown, validate
from media_scout.storage import write_json


class QualityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_workflow.WorkflowTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.report = copy.deepcopy(self.fixture.editorial)
        self.config = copy.deepcopy(self.fixture.config)
        self.version = make_library([self.report], self.config)["tools"][0]["versions"][0]

    def assessment(self):
        value = baseline_assessment(self.version, self.fixture.day)
        value.update(tier="recommended", method="source-review", summary="Results and adoption evidence reviewed for the scoped creative workflow.")
        independent = "https://independent.example/first-hand-workflow"
        value["sources"].append({"title": "Independent first-hand integration", "url": independent})
        for check in value["checks"].values():
            check.update(status="verified", note="Concrete cited evidence reviewed for this criterion.",
                         source_urls=[value["sources"][0]["url"]])
        value["checks"]["independent_use"].update(source_kind="independent", source_urls=[independent])
        return value

    def registry(self, assessment):
        return {"format_version": 1, "audits": {}, "reviews": {self.version["profile"]["id"]:
                {**record_binding(self.version), "checked_on": self.fixture.day, "assessment": assessment}}}

    def ready_assessment(self):
        value = self.assessment()
        value.update(tier="ready_to_try", summary="Five checks verified; creative-result review remains pending.")
        value["checks"]["results"].update(status="unknown", source_urls=[],
                                         note="Creative output quality has not yet been assessed.")
        return value

    def test_stars_complete_guides_and_mature_labels_cannot_grant_recommendation(self):
        p = self.report["tools"][0]
        p.update(stars=100000, maturity="Established application")
        a = make_library([self.report], self.config)["tools"][0]["quality_assessment"]
        self.assertEqual(a["tier"], "unverified")
        self.assertEqual(a["method"], "unassessed")
        self.assertIsNone(a["checked_on"])
        self.assertFalse(any(c["status"] == "verified" for c in a["checks"].values()))

    def test_every_check_and_independent_provenance_are_required(self):
        good = self.assessment()
        self.assertEqual(validate_assessment(good)["tier"], "recommended")
        for key in CHECKS:
            for status in ("unknown", "documented", "failed"):
                value = copy.deepcopy(good)
                value["checks"][key]["status"] = status
                with self.subTest(key=key, status=status), self.assertRaisesRegex(ValueError, "Recommended requires"):
                    validate_assessment(value)
        value = copy.deepcopy(good)
        value["checks"]["independent_use"]["source_kind"] = "maintainer"
        with self.assertRaisesRegex(ValueError, "independent use"):
            validate_assessment(value)
        with self.assertRaisesRegex(ValueError, "full profile"):
            validate_assessment(good, "screened")
        value = copy.deepcopy(good)
        value["method"] = "published-record-audit"
        with self.assertRaisesRegex(ValueError, "Recommended requires"):
            validate_assessment(value)

    def test_missing_citations_dates_and_unsafe_urls_fail_closed(self):
        good = self.assessment()
        for urls in ([], ["https://uncited.example/"]):
            value = copy.deepcopy(good)
            value["checks"]["results"]["source_urls"] = urls
            with self.assertRaisesRegex(ValueError, "cite declared"):
                validate_assessment(value)
        for url in ("javascript:alert(1)", "https://user:secret@example.com/"):
            value = copy.deepcopy(good)
            value["sources"][0]["url"] = url
            with self.assertRaisesRegex(ValueError, "HTTPS"):
                validate_assessment(value)
        with self.assertRaisesRegex(ValueError, "edition date"):
            validate_assessment(good, expected_date="2026-10-02")

    def test_ready_to_try_allows_pending_results_without_claiming_runtime_testing(self):
        for status in ("unknown", "documented"):
            value = self.ready_assessment()
            value["checks"]["results"]["status"] = status
            if status == "documented":
                value["checks"]["results"]["source_urls"] = [value["sources"][0]["url"]]
            with self.subTest(status=status):
                self.assertEqual(validate_assessment(value)["tier"], "ready_to_try")
                self.report["tools"][0]["quality_assessment"] = value
                validate(self.report, self.fixture.discovery, self.config, {})
                self.assertFalse(self.report["tools"][0]["quality"]["hands_on_tested"])
                value["tier"] = "recommended"
                with self.assertRaisesRegex(ValueError, "all six"):
                    validate_assessment(value)

    def test_ready_to_try_retains_five_checks_independent_evidence_and_profile_requirements(self):
        good = self.ready_assessment()
        for key in set(CHECKS) - {"results"}:
            for status in ("unknown", "documented", "failed"):
                value = copy.deepcopy(good)
                value["checks"][key]["status"] = status
                with self.subTest(key=key, status=status), self.assertRaisesRegex(ValueError, "five non-results"):
                    validate_assessment(value)
        for provenance in (None, "maintainer"):
            value = copy.deepcopy(good)
            value["checks"]["independent_use"].pop("source_kind")
            if provenance:
                value["checks"]["independent_use"]["source_kind"] = provenance
            with self.assertRaisesRegex(ValueError, "independent use"):
                validate_assessment(value)
        with self.assertRaisesRegex(ValueError, "full profile"):
            validate_assessment(good, "screened")
        value = copy.deepcopy(good)
        value["method"] = "published-record-audit"
        with self.assertRaisesRegex(ValueError, "Ready to try requires"):
            validate_assessment(value)
        self.report["tools"][0].update(quality_assessment=good, maturity="Research prototype")
        validate(self.report, self.fixture.discovery, self.config, {})  # Historical maturity text cannot override cited evidence.

    def test_ready_to_try_cannot_hide_failed_or_completed_result_review(self):
        for status in ("failed", "verified"):
            value = self.ready_assessment()
            value["checks"]["results"].update(status=status, source_urls=[value["sources"][0]["url"]])
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "review to be pending"):
                validate_assessment(value)
        value = self.ready_assessment()
        del value["checks"]["results"]
        with self.assertRaisesRegex(ValueError, "all six evidence checks"):
            validate_assessment(value)

    def test_ready_library_counts_and_backlog_keep_results_pending_until_reviewed(self):
        self.fixture.build()
        export_report(self.fixture.day, self.root)
        registry = self.registry(self.ready_assessment())
        write_json(self.root / "config/quality_reviews.json", registry)
        rebuild_library(self.root)
        verify_public_archive(self.root)
        backlog = quality_backlog(self.root)
        self.assertEqual(backlog["counts"]["ready_to_try"], 1)
        self.assertEqual(backlog["counts"]["recommended"], 0)
        self.assertEqual(backlog["items"][0]["missing_checks"], ["results"])
        registry["reviews"][self.version["profile"]["id"]]["assessment"] = self.assessment()
        write_json(self.root / "config/quality_reviews.json", registry)
        backlog = quality_backlog(self.root)
        self.assertEqual(backlog["counts"]["recommended"], 1)
        self.assertEqual(backlog["counts"]["ready_to_try"], 0)
        self.assertEqual(backlog["items"], [])

    def test_evidence_gaps_require_independent_provenance_without_changing_the_assessment(self):
        assessment = self.assessment()
        assessment["tier"] = "unverified"
        assessment["checks"]["independent_use"]["source_kind"] = "maintainer"
        before = copy.deepcopy(assessment)
        self.assertEqual(evidence_gaps(assessment), ["independent_use"])
        library = make_library([self.report], self.config, self.registry(assessment))
        tool = library["tools"][0]
        self.assertEqual(tool["evidence_gaps"], ["independent_use"])
        item = review_item(tool)
        self.assertEqual(item["next_steps"][0]["requirement"], "independent_use")
        self.assertIn("independent of the maintainer", item["next_steps"][0]["action"])
        self.assertEqual(item["next_steps"][0]["source_urls"], assessment["checks"]["independent_use"]["source_urls"])
        self.assertEqual(assessment, before)
        self.assertEqual(tool["quality_assessment"]["tier"], "unverified")
        self.assertEqual(evidence_gaps({}), list(CHECKS))

    def test_backlog_prioritizes_failures_then_results_and_fewer_gaps_without_star_ranking(self):
        base = make_library([self.report], self.config)["tools"][0]
        def tool(name, assessment):
            return {**copy.deepcopy(base), "id": name, "name": name, "quality_assessment": assessment}
        ready = tool("ready", self.ready_assessment())
        failed = tool("failed", self.assessment())
        failed["quality_assessment"]["tier"] = "unverified"
        failed["quality_assessment"]["checks"]["results"]["status"] = "failed"
        near = tool("near", self.ready_assessment())
        near["quality_assessment"]["tier"] = "unverified"
        near["quality_assessment"]["checks"]["setup"]["status"] = "documented"
        far = tool("far", baseline_assessment(self.version))
        far["stars"] = 1000000
        screened = tool("screened", baseline_assessment(self.version))
        screened["versions"][0]["kind"] = "screened"
        experimental = tool("experimental", baseline_assessment(self.version))
        experimental["quality_assessment"].update(tier="experimental", experimental_reason={
            "text": "The current export pipeline is explicitly unfinished.", "source_urls": ["https://example.com/status"]})
        recommended = tool("recommended", self.assessment())
        items = [experimental, screened, far, near, ready, failed, recommended]
        data = {"tools": items, "quality_counts": {"recommended": 1, "ready_to_try": 1, "unverified": 4, "experimental": 1}}
        before = copy.deepcopy(data)
        with patch("media_scout.quality.public_quality_library", return_value=data):
            result = quality_backlog(self.root)
            self.assertEqual([item["id"] for item in result["items"]], ["failed", "ready", "near", "far", "screened", "experimental"])
            self.assertEqual(result["pending"], 6)
            self.assertEqual(result["matching"], 6)
            self.assertEqual(result["queue_counts"]["results_review"], 1)
            self.assertEqual(result["items"][0]["failed_checks"], ["results"])
            self.assertIn("Resolve the cited failure", result["items"][0]["next_steps"][0]["action"])
            self.assertIn("our own demo is not required", result["items"][1]["next_steps"][0]["action"])
            filtered = quality_backlog(self.root, check="setup", tier="unverified")
            self.assertEqual([item["id"] for item in filtered["items"]], ["near", "far", "screened"])
            self.assertEqual(filtered["matching"], 3)
            for field in ("counts", "pending", "gap_counts", "queue_counts"):
                self.assertEqual(filtered[field], result[field])
            oldest = quality_backlog(self.root, sort="oldest")
            self.assertEqual(oldest["items"][0]["id"], "experimental")  # Unassessed first; deterministic ID tie-break.
            self.assertEqual(quality_backlog(self.root, tier="recommended")["items"], [])
        self.assertEqual(data, before)

    def test_review_tasks_use_latest_record_and_keep_experimental_evidence(self):
        tool = make_library([self.report], self.config)["tools"][0]
        latest = copy.deepcopy(tool["versions"][0])
        latest.update(kind="screened", revision=2, edition_id=self.fixture.day + "-r2")
        tool["versions"].insert(0, latest)
        tool["quality_assessment"] = baseline_assessment(latest)
        item = review_item(tool)
        self.assertEqual(tool["review"], "profile")
        self.assertTrue(item["needs_profile"])
        self.assertTrue(item["needs_source_review"])
        self.assertEqual(item["basis_edition"], self.fixture.day + "-r2")
        self.assertEqual(item["queue"], "profile_needed")
        self.assertEqual(item["next_steps"][0]["requirement"], "full_profile")
        reason = {"text": "The current scene editor cannot save projects yet.", "source_urls": ["https://example.com/editor"]}
        tool["quality_assessment"].update(tier="experimental", experimental_reason=reason)
        item = review_item(tool)
        self.assertEqual(item["queue"], "experimental_review")
        self.assertEqual(item["next_steps"][0]["note"], reason["text"])
        self.assertEqual(item["next_steps"][0]["source_urls"], reason["source_urls"])

    def test_complete_checks_still_need_an_explicit_tier_review(self):
        assessment = self.assessment()
        assessment["tier"] = "unverified"
        tool = make_library([self.report], self.config, self.registry(assessment))["tools"][0]
        item = review_item(tool)
        self.assertEqual(item["missing_checks"], [])
        self.assertEqual(item["tier"], "unverified")
        self.assertEqual(item["next_steps"][0]["requirement"], "assessment")

    def test_backlog_filters_are_read_only_and_cli_summary_keeps_global_counts(self):
        self.fixture.build()
        export_report(self.fixture.day, self.root)
        write_json(self.root / "config/quality_reviews.json", self.registry(self.ready_assessment()))
        rebuild_library(self.root)
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        for extra, matching in (([], 1), (["--check", "setup"], 0), (["--check", "results", "--full"], 1)):
            output = StringIO()
            with patch.object(cli, "ROOT", self.root), redirect_stdout(output), \
                    patch("sys.argv", ["media-scout", "quality-backlog", "--tier", "ready_to_try", *extra]):
                self.assertEqual(cli.main(), 0)
            result = json.loads(output.getvalue())
            self.assertEqual(result["pending"], 1)
            self.assertEqual(result["matching"], matching)
            self.assertEqual(result["gap_counts"]["results"], 1)
            self.assertEqual("items" in result, "--full" in extra)
        after = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_backlog_rejects_unknown_filters_instead_of_silently_hiding_tools(self):
        for options in ({"check": "unknown"}, {"tier": "unknown"}, {"sort": "stars"}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                quality_backlog(self.root, **options)

    def test_new_editions_require_assessments_without_breaking_legacy_reads(self):
        self.config["scope"] = {"require_quality_assessment": True}
        with self.assertRaisesRegex(ValueError, "Every new profile"):
            validate(self.report, self.fixture.discovery, self.config, {})
        self.report["tools"][0]["quality_assessment"] = self.assessment()
        validate(self.report, self.fixture.discovery, self.config, {})
        self.report["tools"][0]["maturity"] = "Research prototype"
        validate(self.report, self.fixture.discovery, self.config, {})  # Historical maturity text cannot override cited evidence.
        legacy = make_library([self.fixture.editorial], self.config)
        self.assertEqual(legacy["quality_counts"]["unverified"], 1)

    def test_pending_leads_also_require_quality_assessments(self):
        p = self.report["tools"][0]
        lead = {k: p[k] for k in ("id", "name", "checked_on", "categories", "sources")}
        lead.update(good_for="Creative AI images", code_license="MIT", review_status="Full profile pending",
                    ai_relevance={"text": "Neural image generation for creative painting workflows.", "source_urls": [p["sources"][0]["url"]]})
        self.report.update(tools=[], leads=[lead])
        self.config["scope"] = {"require_quality_assessment": True}
        with self.assertRaisesRegex(ValueError, "Every new profile"):
            validate(self.report, self.fixture.discovery, self.config, {})
        lead["quality_assessment"] = baseline_assessment({"kind": "screened", "profile": lead}, self.fixture.day)
        validate(self.report, self.fixture.discovery, self.config, {})

    def test_reassessment_is_bound_to_latest_record_and_preserves_history(self):
        original = copy.deepcopy(self.report)
        registry = self.registry(self.assessment())
        data = make_library([self.report], self.config, registry)
        self.assertEqual(data["quality_counts"]["recommended"], 1)
        self.assertNotIn("quality_assessment", data["tools"][0]["versions"][0]["profile"])
        self.assertEqual(self.report, original)
        later = copy.deepcopy(self.report)
        later["report_date"] = later["tools"][0]["checked_on"] = "2026-10-02"
        data = make_library([self.report, later], self.config, registry)
        self.assertEqual(data["tools"][0]["quality_assessment"]["tier"], "unverified")
        self.assertIn("not carried forward", " ".join(data["tools"][0]["quality_assessment"]["caveats"]))
        changed = copy.deepcopy(self.report)
        changed["tools"][0]["requirements"]["hardware"] = "Changed requirements"
        self.assertEqual(make_library([changed], self.config, registry)["quality_counts"]["recommended"], 0)

    def test_retrospective_audit_preserves_sealed_reports_and_is_repeatable(self):
        self.fixture.build()
        export_report(self.fixture.day, self.root)
        paths = list((self.root / "reports").rglob("*")) + list((self.root / "public/reports").rglob("*"))
        before = {p: p.read_bytes() for p in paths if p.is_file()}
        self.assertEqual(audit_existing(self.root, self.fixture.day)["new_record_audits"], 1)
        self.assertEqual(audit_existing(self.root, self.fixture.day)["new_record_audits"], 0)
        rebuild_library(self.root)
        verify_public_archive(self.root)
        self.assertEqual({p: p.read_bytes() for p in before}, before)
        backlog = quality_backlog(self.root)
        self.assertEqual(len(backlog["items"]), 1)
        self.assertEqual(set(backlog["items"][0]["missing_checks"]), set(CHECKS))
        self.assertEqual(backlog["items"][0]["checked_on"], self.fixture.day)
        self.assertEqual(backlog["counts"]["ready_to_try"], 0)

    def test_research_labels_and_unknown_registry_ids_are_not_silently_ignored(self):
        for maturity in ("Research toolkit", "Prototype", "Experimental", "Alpha application", "Beta plugin"):
            self.report["tools"][0]["maturity"] = maturity
            data = make_library([self.report], self.config)
            self.assertEqual(data["tools"][0]["quality_assessment"]["tier"], "unverified")
        registry = self.registry(self.assessment())
        registry["reviews"]["typo"] = registry["reviews"].pop(self.version["profile"]["id"])
        with self.assertRaisesRegex(ValueError, "unknown published tool"):
            make_library([self.report], self.config, registry)

    def test_experimental_needs_current_cited_evidence_not_a_keyword(self):
        value = baseline_assessment(self.version, self.fixture.day)
        value.update(tier="experimental", method="source-review")
        with self.assertRaisesRegex(ValueError, "Experimental requires"):
            validate_assessment(value)
        value["experimental_reason"] = {"text": "The maintainer documents an unfinished export pipeline and unstable project format.",
                                        "source_urls": [value["sources"][0]["url"]]}
        self.assertIn("experimental_reason", validate_assessment(value))
        for urls in ([], ["https://uncited.example/"], [{}], [None]):
            broken = copy.deepcopy(value)
            broken["experimental_reason"]["source_urls"] = urls
            with self.assertRaisesRegex(ValueError, "Experimental requires"):
                validate_assessment(broken)
        value["tier"] = "unverified"
        with self.assertRaisesRegex(ValueError, "Resolve experimental"):
            validate_assessment(value)

    def test_cited_reassessment_overrides_historical_research_label_without_rewriting_it(self):
        self.report["tools"][0]["maturity"] = "Experimental research toolkit"
        self.version = make_library([self.report], self.config)["tools"][0]["versions"][0]
        original = copy.deepcopy(self.report)
        data = make_library([self.report], self.config, self.registry(self.ready_assessment()))
        tool = data["tools"][0]
        self.assertEqual(tool["quality_assessment"]["tier"], "ready_to_try")
        self.assertEqual(tool["versions"][0]["profile"]["maturity"], "Experimental research toolkit")
        self.assertEqual(self.report, original)

    def test_experimental_reason_is_cited_and_escaped_in_new_report_rendering(self):
        value = baseline_assessment(self.version, self.fixture.day)
        url = value["sources"][0]["url"]
        value.update(tier="experimental", method="source-review",
                     experimental_reason={"text": "The export pipeline is unfinished; <unsafe> markup stays text.",
                                          "source_urls": [url]})
        self.report["tools"][0]["quality_assessment"] = value
        validate(self.report, self.fixture.discovery, self.config, {})
        html = render_html(self.report, self.fixture.discovery, self.config)
        markdown = render_markdown(self.report, self.fixture.discovery, self.config)
        for text in (html, markdown):
            self.assertIn("Why Experimental", text)
            self.assertIn(url, text)
        self.assertNotIn("<unsafe>", html)
        self.assertIn("&lt;unsafe&gt;", html)

    def test_a_newer_brief_mention_invalidates_a_full_profile_recommendation(self):
        p = self.report["tools"][0]
        lead = {k: p[k] for k in ("id", "name", "categories", "sources")}
        lead.update(checked_on="2026-10-02", good_for="Creative AI images", code_license="MIT", review_status="Full profile pending")
        later = dict(self.report, report_date="2026-10-02", tools=[], leads=[lead])
        data = make_library([self.report, later], self.config, self.registry(self.assessment()))
        self.assertEqual(data["tools"][0]["review"], "profile")
        self.assertEqual(data["quality_counts"]["recommended"], 0)

    def test_inline_assessment_is_part_of_the_exact_record_binding(self):
        changed = copy.deepcopy(self.version)
        changed["profile"]["quality_assessment"] = self.assessment()
        self.assertNotEqual(record_binding(changed), record_binding(self.version))

    def test_registry_validation_strips_unrecognized_private_fields(self):
        assessment = self.assessment()
        assessment["private_notes"] = "private@example.com"
        self.assertNotIn("private@example.com", json.dumps(validate_assessment(assessment)))
        registry = self.registry(assessment)
        write_json(self.root / "config/quality_reviews.json", registry)
        read_reviews(self.root)
        registry["reviews"][self.version["profile"]["id"]]["record_sha256"] = "bad"
        write_json(self.root / "config/quality_reviews.json", registry)
        with self.assertRaisesRegex(ValueError, "record binding"):
            read_reviews(self.root)

    def test_new_reports_show_quality_separately_from_profile_depth(self):
        for assessment, label in ((self.assessment(), "Recommended"), (self.ready_assessment(), "Ready to try")):
            self.report["tools"][0]["quality_assessment"] = assessment
            for text in (render_html(self.report, self.fixture.discovery, self.config),
                         render_markdown(self.report, self.fixture.discovery, self.config)):
                self.assertIn("Quality assessment: " + label, text)
                self.assertIn("Independent use", text)
                self.assertIn("https://independent.example/first-hand-workflow", text)


if __name__ == "__main__":
    unittest.main()
