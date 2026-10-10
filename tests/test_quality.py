"""Recommendations require evidence; historical reports remain immutable."""

import copy
import json
import unittest

import test_workflow
from media_scout.library import make_library
from media_scout.publication import export_report, rebuild_library, verify_public_archive
from media_scout.quality import (CHECKS, audit_existing, baseline_assessment, quality_backlog,
                                 is_experimental, read_reviews, record_binding, validate_assessment)
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

    def test_new_editions_require_assessments_without_breaking_legacy_reads(self):
        self.config["scope"] = {"require_quality_assessment": True}
        with self.assertRaisesRegex(ValueError, "Every new profile"):
            validate(self.report, self.fixture.discovery, self.config, {})
        self.report["tools"][0]["quality_assessment"] = self.assessment()
        validate(self.report, self.fixture.discovery, self.config, {})
        self.report["tools"][0]["maturity"] = "Research prototype"
        with self.assertRaisesRegex(ValueError, "Experimental"):
            validate(self.report, self.fixture.discovery, self.config, {})
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

    def test_research_labels_and_unknown_registry_ids_are_not_silently_ignored(self):
        for maturity in ("Research toolkit", "Prototype", "Experimental", "Alpha application", "Beta plugin"):
            self.report["tools"][0]["maturity"] = maturity
            data = make_library([self.report], self.config)
            self.assertEqual(data["tools"][0]["quality_assessment"]["tier"], "experimental")
        registry = self.registry(self.assessment())
        registry["reviews"]["typo"] = registry["reviews"].pop(self.version["profile"]["id"])
        with self.assertRaisesRegex(ValueError, "unknown published tool"):
            make_library([self.report], self.config, registry)

    def test_research_only_model_terms_do_not_classify_the_software_as_experimental(self):
        self.assertFalse(is_experimental({"review_status": "Model weights allow only non-commercial research; full profile pending."}))
        self.assertTrue(is_experimental({"review_status": "MIT research code; full profile pending."}))

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
        self.report["tools"][0]["quality_assessment"] = self.assessment()
        for text in (render_html(self.report, self.fixture.discovery, self.config),
                     render_markdown(self.report, self.fixture.discovery, self.config)):
            self.assertIn("Quality assessment: Recommended", text)
            self.assertIn("Independent use", text)
            self.assertIn("https://independent.example/first-hand-workflow", text)


if __name__ == "__main__":
    unittest.main()
