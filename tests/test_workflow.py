"""Regression checks for the report integrity and external-send boundary."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from urllib.request import Request

from media_scout import delivery
from media_scout.client import SafeRedirect
from media_scout.discovery import fingerprint, novelty
from media_scout.report import SECTIONS, build, render_html, safe_url, validate, verify_report
from media_scout.storage import read_json, report_date, write_json, write_text


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.day = "2026-10-01"
        self.config = {"recipient": "recipient@example.com", "timezone": "America/New_York",
                       "max_profiles": 12, "categories": [{"id": "images", "name": "Images"}]}
        self.candidate = {"id": "github:test/art", "repository": "test/art", "code_license": "MIT",
                          "readme_path": "research/2026-10-01/evidence/art.md", "readme_sha256": "source",
                          "source_fingerprint": "fingerprint", "novelty": "first-profile", "stars": 5}
        self.discovery = {"report_date": self.day, "completed_at": "2026-10-01T12:00:00Z", "window_days": 30,
                          "warnings": [], "candidates": [self.candidate], "note": "Bounded search"}
        urls = ["https://github.com/test/art", "https://github.com/test/art/blob/main/LICENSE"]
        tool = {"id": "github:test/art", "name": "Art <script>alert(1)</script>", "categories": ["images"],
                "checked_on": self.day, "maturity": "Emerging", "novelty": {"kind": "first-profile", "text": "Initial baseline"},
                "sources": [{"title": "README", "url": urls[0]}, {"title": "License", "url": urls[1]}],
                "links": {"repository": urls[0]}}
        for section in SECTIONS:
            tool[section] = {"text": "Documentation-backed explanation", "source_urls": urls}
        tool["installation"].update(steps=["Use the official installer"], commands=["example --help"])
        tool["usage"].update(steps=["Open the first example"])
        tool["requirements"].update(hardware="Not documented", software="Browser", platforms="All browser platforms")
        tool["license"].update(code="MIT", weights="Model-specific", commercial="Check model terms", cost="Local use free")
        tool["quality"].update(hands_on_tested=False)
        self.editorial = {"report_date": self.day, "summary": "Daily edition", "tools": [tool],
                          "category_notes": [{"category": "images", "text": "One reviewed tool", "source_urls": urls}]}
        write_json(self.root / "config/scout.json", self.config)
        write_json(self.root / "research" / self.day / "discovery.json", self.discovery)
        write_text(self.root / self.candidate["readme_path"], "Official source")
        self.editorial_path = self.root / "editorial.json"
        write_json(self.editorial_path, self.editorial)

    def build(self):
        return build(self.editorial_path, self.root)

    def test_build_and_repeated_build_preserve_artifacts(self):
        manifest = self.build()
        self.assertEqual(manifest, self.build())
        self.assertEqual(manifest, verify_report(self.day, self.root))

    def test_restricted_findings_remain_notes_without_entering_library(self):
        self.editorial["watchlist"] = [{"name": "Restricted <tool>", "status": "excluded",
            "checked_on": self.day, "reason": "Software has non-commercial terms.",
            "source_urls": ["https://github.com/test/restricted/blob/main/LICENSE"]}]
        write_json(self.editorial_path, self.editorial)
        self.build()
        html = (self.root / "reports" / self.day / "report.html").read_text()
        self.assertIn("Restricted &lt;tool&gt;", html)
        self.assertIn("Excluded and unresolved findings", html)
        library = read_json(self.root / "site/library.json")
        self.assertEqual(library["counts"]["tools"], 1)
        self.assertNotIn("Restricted", json.dumps(library))

    def test_tampered_source_or_report_blocks_delivery(self):
        self.build()
        write_text(self.root / self.candidate["readme_path"], "Changed source")
        with self.assertRaisesRegex(ValueError, "changed"):
            delivery.prepare(self.day, self.root)

    def test_rebuilding_repairs_missing_library_after_a_crash(self):
        manifest = self.build()
        (self.root / "site/index.html").unlink()
        (self.root / "state/catalog.json").unlink()
        self.assertEqual(self.build(), manifest)
        self.assertTrue((self.root / "site/index.html").exists())
        self.assertTrue((self.root / "state/catalog.json").exists())

    def test_secondary_documentation_is_also_sealed(self):
        source = self.root / "research" / self.day / "evidence" / "requirements.md"
        write_text(source, "Official secondary requirements")
        self.build()
        write_text(source, "Modified after sealing")
        with self.assertRaisesRegex(ValueError, "changed"):
            verify_report(self.day, self.root)

    def test_nested_source_evidence_is_sealed_and_tampering_blocks_email(self):
        evidence = self.root / "research" / self.day / "evidence"
        nested = evidence / "primary" / "project"
        source = nested / "README.md"
        license_file = nested / "LICENSE.txt"
        write_text(source, "Official project documentation")
        write_text(license_file, "Complete software terms")
        (evidence / "empty").mkdir()

        manifest = self.build()
        self.assertIn(str(source.relative_to(self.root)), manifest["sha256"])
        self.assertIn(str(license_file.relative_to(self.root)), manifest["sha256"])
        self.assertNotIn(str(nested.relative_to(self.root)), manifest["sha256"])
        self.assertNotIn(str((evidence / "empty").relative_to(self.root)), manifest["sha256"])
        self.assertEqual(manifest, verify_report(self.day, self.root))

        write_text(license_file, "Terms changed after sealing")
        with self.assertRaisesRegex(ValueError, "Sealed evidence/artifact changed"):
            delivery.prepare(self.day, self.root)
        self.assertFalse((self.root / "state/deliveries" / (self.day + ".json")).exists())

    def test_reserved_delivery_blocks_second_send(self):
        self.build()
        first = delivery.prepare(self.day, self.root)
        self.assertEqual(first["status"], "reserved")
        with self.assertRaisesRegex(RuntimeError, "Reconcile"):
            delivery.prepare(self.day, self.root)

    def test_private_recipient_is_sealed_without_changing_public_defaults(self):
        self.config["recipient"] = None
        write_json(self.root / "config/scout.json", self.config)
        write_json(self.root / "config/scout.local.json", {"recipient": "approved@example.com"})
        manifest = self.build()
        self.assertEqual(manifest["recipient"], "approved@example.com")
        self.assertIsNone(read_json(self.root / "config/scout.json")["recipient"])

    def test_unconfigured_recipient_does_not_reserve_or_prepare_email(self):
        self.config["recipient"] = None
        write_json(self.root / "config/scout.json", self.config)
        self.build()
        with self.assertRaisesRegex(ValueError, "Configure the authorized recipient"):
            delivery.prepare(self.day, self.root)
        self.assertFalse((self.root / "state/deliveries" / (self.day + ".json")).exists())
        self.assertFalse((self.root / "state/outbox" / (self.day + ".json")).exists())

    def test_sent_delivery_is_idempotent_and_records_report_hash(self):
        manifest = self.build()
        delivery.prepare(self.day, self.root)
        receipt = delivery.record(self.day, "gmail-message-123", self.root)
        self.assertEqual(receipt["report_sha256"], manifest["sha256"][f"reports/{self.day}/report.html"])
        self.assertEqual(delivery.prepare(self.day, self.root)["status"], "already-sent")
        with self.assertRaisesRegex(ValueError, "different message"):
            delivery.record(self.day, "gmail-message-456", self.root)

    def test_uncertain_send_cannot_be_automatically_retried(self):
        self.build()
        delivery.prepare(self.day, self.root)
        delivery.uncertain(self.day, self.root)
        with self.assertRaises(RuntimeError):
            delivery.prepare(self.day, self.root)
        receipt = delivery.record(self.day, "reconciled-id", self.root, reconciled=True)
        self.assertTrue(receipt["reconciled"])

    def test_license_mismatch_or_custom_license_blocks_feature(self):
        changed = copy.deepcopy(self.editorial)
        changed["tools"][0]["license"]["code"] = "Apache-2.0"
        with self.assertRaisesRegex(ValueError, "License contradicts"):
            validate(changed, self.discovery, self.config, {})
        self.candidate["code_license"] = "CC-BY-NC-SA-4.0"
        with self.assertRaisesRegex(ValueError, "license needs verification"):
            validate(self.editorial, self.discovery, self.config, {})

    def test_uncited_hardware_claim_blocks_feature(self):
        self.editorial["tools"][0]["requirements"]["source_urls"] = ["https://invented.example.com/specs"]
        with self.assertRaisesRegex(ValueError, "cite declared"):
            validate(self.editorial, self.discovery, self.config, {})

    def test_unchanged_tool_cannot_be_repeated_as_new(self):
        catalog = {self.candidate["id"]: {"last_featured": "2026-09-30", "source_fingerprint": "fingerprint"}}
        with self.assertRaisesRegex(ValueError, "Already featured"):
            validate(self.editorial, self.discovery, self.config, catalog)

    def test_empty_daily_edition_is_valid_with_coverage(self):
        self.editorial["tools"] = []
        self.assertIs(validate(self.editorial, self.discovery, self.config, {}), self.editorial)
        self.editorial["category_notes"] = []
        with self.assertRaisesRegex(ValueError, "coverage note"):
            validate(self.editorial, self.discovery, self.config, {})

    def test_untrusted_profile_text_is_escaped(self):
        output = render_html(self.editorial, self.discovery, self.config)
        self.assertNotIn('<script>alert(1)</script>', output)
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', output)

    def test_external_profile_does_not_claim_github_stars(self):
        self.assertIn("5 GitHub stars", render_html(self.editorial, self.discovery, self.config))
        key = "external:https://gitlab.com/example/art"
        self.candidate["id"] = key
        self.editorial["tools"][0]["id"] = key
        output = render_html(self.editorial, self.discovery, self.config)
        self.assertNotIn("GitHub stars", output)
        self.assertIn("Docs checked 2026-10-01", output)

    def test_sources_reject_unsafe_urls_and_credentials(self):
        for url in ("javascript:alert(1)", "http://example.com", "https://password@github.com"):
            with self.assertRaises(ValueError):
                safe_url(url)

    def test_cross_host_redirect_removes_authorization(self):
        request = Request("https://api.github.com/repos/a/b", headers={"Authorization": "Bearer secret"})
        redirected = SafeRedirect().redirect_request(request, None, 302, "Found", {}, "https://raw.githubusercontent.com/a/b")
        self.assertIsNone(redirected.get_header("Authorization"))

    def test_novelty_requires_changed_content_or_release(self):
        item = {"readme_sha256": "a", "code_license": "MIT", "latest_release": {"tag": "v1"}}
        item["source_fingerprint"] = fingerprint(item)
        previous = {"last_featured": "2026-09-30", "source_fingerprint": item["source_fingerprint"], "release_tag": "v1"}
        self.assertEqual(novelty(item, previous, "2026-09-01"), "unchanged")
        item["latest_release"]["tag"] = "v2"
        item["source_fingerprint"] = fingerprint(item)
        self.assertEqual(novelty(item, previous, "2026-09-01"), "new-release")

    def test_missing_license_review_is_pending_instead_of_a_source_change(self):
        reviewed = {"readme_sha256": "readme", "code_license": "MIT", "head_sha": "head",
                    "latest_release": {"tag": "v1"}, "license_review": {"sha256": "license"}}
        previous = {"last_featured": "2026-09-30", "source_fingerprint": fingerprint(reviewed),
                    "head_sha": "head", "release_tag": "v1"}
        observed = {key: value for key, value in reviewed.items() if key != "license_review"}
        observed["source_fingerprint"] = fingerprint(observed)
        self.assertEqual(novelty(observed, previous, "2026-09-01"), "source-comparison-pending")
        observed["license_review"] = {"sha256": "license", "note": "A fresh review", "checked_at": "later"}
        observed["source_fingerprint"] = fingerprint(observed)
        self.assertEqual(novelty(observed, previous, "2026-09-01"), "unchanged")

    def test_confirmed_commit_and_release_changes_remain_review_signals(self):
        item = {"readme_sha256": "readme", "code_license": "MIT", "head_sha": "head",
                "latest_release": {"tag": "v1"}}
        previous = {"last_featured": "2026-09-30", "source_fingerprint": "reviewed-fingerprint",
                    "head_sha": "head", "release_tag": "v1"}
        for field, value, expected in [
                ("head_sha", "new-head", "source-changed-review-required"),
                ("latest_release", {"tag": "v2"}, "new-release")]:
            changed = dict(item, **{field: value})
            changed["source_fingerprint"] = fingerprint(changed)
            with self.subTest(field=field):
                self.assertEqual(novelty(changed, previous, "2026-09-01"), expected)

    def test_incomplete_or_missing_evidence_cannot_claim_an_update(self):
        previous = {"last_featured": "2026-09-30", "source_fingerprint": "old",
                    "head_sha": "head", "release_tag": "v1"}
        partial = {"readme_sha256": "readme", "code_license": "MIT", "head_sha": "new-head",
                   "latest_release": {"tag": "v2"}, "license_review": {"sha256": "license"},
                   "collection_warning": "Commit API unavailable"}
        partial["source_fingerprint"] = fingerprint(partial)
        self.assertEqual(novelty(partial, previous, "2026-09-01"), "source-comparison-pending")
        self.assertEqual(novelty({}, {"last_featured": "2026-09-30"}, "2026-09-01"),
                         "source-comparison-pending")

    def test_reviewed_license_text_change_is_detected_even_with_same_spdx(self):
        item = {"readme_sha256": "readme", "code_license": "MIT", "head_sha": "head",
                "license_review": {"sha256": "old-license"}}
        previous = {"last_featured": "2026-09-30", "source_fingerprint": fingerprint(item),
                    "head_sha": "head"}
        item["license_review"] = {"sha256": "changed-license"}
        item["source_fingerprint"] = fingerprint(item)
        self.assertEqual(novelty(item, previous, "2026-09-01"), "source-changed-review-required")

    def test_adding_license_evidence_to_legacy_history_is_not_an_update(self):
        item = {"readme_sha256": "readme", "code_license": "MIT", "head_sha": "head"}
        previous = {"last_featured": "2026-09-30", "source_fingerprint": fingerprint(item),
                    "head_sha": "head"}
        item["license_review"] = {"sha256": "first-license-review"}
        item["source_fingerprint"] = fingerprint(item)
        self.assertEqual(novelty(item, previous, "2026-09-01"), "source-comparison-pending")

    def test_pending_comparison_cannot_repeat_a_previously_featured_tool(self):
        self.candidate["novelty"] = "source-comparison-pending"
        self.editorial["tools"][0]["novelty"]["kind"] = "source-comparison-pending"
        previous = {self.candidate["id"]: {"last_featured": "2026-09-30", "source_fingerprint": "old"}}
        with self.assertRaisesRegex(ValueError, "comparison is pending"):
            validate(self.editorial, self.discovery, self.config, previous)

    def test_invalid_dates_cannot_escape_report_directory(self):
        for value in ("../report", "2026-1-1", "2026-10-01/../../"):
            with self.assertRaises(ValueError):
                report_date(value)

    def test_unlimited_profiles_can_exceed_the_previous_twelve(self):
        self.config["max_profiles"] = None
        self.discovery["candidates"], self.editorial["tools"] = [], []
        for index in range(20):
            candidate = copy.deepcopy(self.candidate)
            candidate["id"] = f"github:test/tool-{index}"
            tool = copy.deepcopy(read_json(self.editorial_path)["tools"][0])
            tool.update(id=candidate["id"], name=f"Creative tool {index}")
            self.discovery["candidates"].append(candidate)
            self.editorial["tools"].append(tool)
        write_json(self.root / "config/scout.json", self.config)
        write_json(self.root / "research" / self.day / "discovery.json", self.discovery)
        write_json(self.editorial_path, self.editorial)
        self.assertEqual(self.build()["profile_count"], 20)

    def test_expanded_scope_requires_cited_creative_ai_relevance(self):
        self.config["scope"] = {"require_ai_relevance": True}
        with self.assertRaisesRegex(ValueError, "creative AI"):
            validate(self.editorial, self.discovery, self.config, {})
        tool = self.editorial["tools"][0]
        tool["ai_relevance"] = {"text": "Uses a local image model for editable creative image generation.",
                                "source_urls": [tool["sources"][0]["url"]]}
        self.assertIs(validate(self.editorial, self.discovery, self.config, {}), self.editorial)

    def test_additional_discoveries_are_preserved_in_the_review_queue(self):
        tool = self.editorial["tools"][0]
        self.editorial["tools"] = []
        self.editorial["leads"] = [{"id": tool["id"], "name": "Emerging creative AI", "categories": ["images"],
            "checked_on": self.day, "code_license": "MIT", "good_for": "Editable image ideas",
            "review_status": "Hardware and installation review pending", "sources": tool["sources"],
            "ai_relevance": {"text": "A local generative image model assists creative image authoring.",
                             "source_urls": [tool["sources"][0]["url"]]}}]
        self.candidate["url"] = tool["links"]["repository"]
        write_json(self.root / "research" / self.day / "discovery.json", self.discovery)
        write_json(self.editorial_path, self.editorial)
        manifest = self.build()
        self.assertEqual(manifest["lead_count"], 1)
        self.assertIn(tool["id"], read_json(self.root / "state/review_queue.json"))
        html = (self.root / "reports" / self.day / "report.html").read_text()
        self.assertIn("Additional open-source AI discoveries", html)
        self.assertIn("Hardware and installation review pending", html)

    def test_large_editions_preserve_complete_content_as_email_attachments(self):
        self.editorial["summary"] = "A complete expanded report. " * 5000
        write_json(self.editorial_path, self.editorial)
        self.build()
        reserved = delivery.prepare(self.day, self.root)
        mime = read_json(Path(reserved["payload_path"]))["payload"]
        self.assertEqual(mime["mime_type"], "multipart/mixed")
        attachments = [part for part in mime["parts"] if part.get("content_disposition") == "attachment"]
        self.assertEqual(len(attachments), 2)
        self.assertEqual(attachments[0]["body"]["content"], (self.root / "reports" / self.day / "report.html").read_text())
        self.assertEqual(attachments[1]["body"]["content"], (self.root / "reports" / self.day / "report.md").read_text())

    def test_scope_changes_preserve_an_already_sent_edition(self):
        manifest = self.build()
        delivery.prepare(self.day, self.root)
        receipt = delivery.record(self.day, "original-message", self.root)
        self.config["categories"].append({"id": "haptics", "name": "Haptic media"})
        self.config["max_profiles"] = None
        write_json(self.root / "config/scout.json", self.config)
        self.assertEqual(self.build(), manifest)
        self.assertEqual(read_json(self.root / "state/deliveries" / (self.day + ".json")), receipt)

    def test_new_daily_field_survives_into_report_and_library(self):
        self.discovery["categories"] = [{"id": "images", "name": "Images"},
                                         {"id": "haptics", "name": "Tactile AI media"}]
        self.editorial["tools"][0]["categories"].append("haptics")
        self.editorial["category_notes"].append({"category": "haptics", "text": "A new creative AI use.",
            "source_urls": [self.editorial["tools"][0]["sources"][0]["url"]]})
        write_json(self.root / "research" / self.day / "discovery.json", self.discovery)
        write_json(self.editorial_path, self.editorial)
        self.build()
        self.assertIn("Tactile AI media", (self.root / "site/index.html").read_text())

    def test_older_archive_rebuild_preserves_a_more_recent_pending_review(self):
        self.build()
        tool = self.editorial["tools"][0]
        newer = {"id": tool["id"], "name": "New version awaiting review", "categories": ["images"],
                 "last_listed": "2026-10-02", "code_license": "MIT", "good_for": "Updated image generation",
                 "review_status": "New hardware review pending", "sources": tool["sources"]}
        write_json(self.root / "state/review_queue.json", {tool["id"]: newer})
        self.build()
        self.assertEqual(read_json(self.root / "state/review_queue.json")[tool["id"]], newer)


if __name__ == "__main__":
    unittest.main()
