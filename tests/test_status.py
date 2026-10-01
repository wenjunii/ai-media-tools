"""Inspection includes updates without changing reports or delivery state."""

import copy
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
import shutil
import unittest
from unittest.mock import patch

import test_publication
from media_scout import cli
from media_scout.publication import export_report
from media_scout.report import build
from media_scout.status import report_status
from media_scout.storage import read_json, sha256, write_json, write_text
from media_scout.updates import export_update, prepare_update


class StatusTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_publication.report_fixture(self)
        self.root, self.day = self.fixture.root, self.fixture.day
        self.fixture.build()
        export_report(self.day, self.root)
        self.receipt = {"status": "sent", "message_id": "original", "profile_count": 1}
        write_json(self.root / "state/deliveries" / (self.day + ".json"), self.receipt)
        write_json(self.root / "state/publications" / (self.day + ".json"), {"status": "synced"})

    def update(self, export=True):
        workspace = prepare_update(self.day, 2, self.root)
        discovery = copy.deepcopy(self.fixture.discovery)
        discovery["candidates"][0].update(id="github:test/update", repository="test/update")
        write_json(workspace / "research" / self.day / "discovery.json", discovery)
        write_text(workspace / self.fixture.candidate["readme_path"], "New official source")
        editorial = copy.deepcopy(self.fixture.editorial)
        editorial["tools"][0].update(id="github:test/update", name="Updated tool")
        path = workspace / "research" / self.day / "editorial.json"
        write_json(path, editorial)
        build(path, workspace)
        if export:
            export_update(self.day, 2, self.root)
        return workspace

    def snapshot(self):
        return {str(path.relative_to(self.root)): sha256(path)
                for path in self.root.rglob("*") if path.is_file()}

    def test_status_includes_all_editions_and_unique_library_counts_without_writing(self):
        self.update()
        before = self.snapshot()
        with patch("media_scout.publication._run", side_effect=AssertionError("No remote calls")):
            status = report_status(self.day, self.root)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(status["delivery"], self.receipt)
        self.assertEqual([edition["revision"] for edition in status["editions"]], [1, 2])
        self.assertEqual(status["latest_completed_edition"]["edition_id"], self.day + "-r2")
        self.assertEqual(status["library"], {"tools": 2, "profiles": 2, "screened": 0,
            "editions": 2, "source": "public", "verified": True, "latest_report_date": self.day})
        self.assertFalse(status["publication_remote_checked"])

    def test_prepared_update_is_not_presented_as_a_completed_report(self):
        self.update()
        prepare_update(self.day, 3, self.root)
        status = report_status(self.day, self.root)
        self.assertEqual(status["latest_completed_edition"]["revision"], 2)
        pending = status["editions"][-1]
        self.assertTrue(pending["prepared"])
        self.assertFalse(pending["built"])
        self.assertIsNone(pending["profile_count"])

    def test_unexported_update_does_not_inflate_the_public_library(self):
        self.update(export=False)
        status = report_status(self.day, self.root)
        self.assertEqual(status["library"]["tools"], 1)
        self.assertEqual(status["latest_completed_edition"]["revision"], 2)
        self.assertFalse(status["latest_completed_edition"]["exported"])

    def test_public_clone_reports_editions_without_claiming_local_research_or_delivery(self):
        self.update()
        for folder in ("state", "reports", "research", "site"):
            shutil.rmtree(self.root / folder)
        before = self.snapshot()
        status = report_status(self.day, self.root, revision=2)
        self.assertFalse(status["built"])
        self.assertFalse(status["discovered"])
        self.assertIsNone(status["delivery"])
        self.assertEqual(status["profile_count"], 1)
        self.assertTrue(status["latest_completed_edition"]["exported"])
        self.assertEqual(before, self.snapshot())

    def test_changed_update_evidence_blocks_status_even_when_original_is_valid(self):
        workspace = self.update()
        write_text(workspace / self.fixture.candidate["readme_path"], "Changed evidence")
        with self.assertRaisesRegex(ValueError, "changed"):
            report_status(self.day, self.root)

    def test_wrong_sealed_revision_is_rejected(self):
        workspace = self.update()
        path = workspace / "reports" / self.day / "manifest.json"
        manifest = read_json(path)
        manifest["revision"] = 3
        write_json(path, manifest)
        with self.assertRaisesRegex(ValueError, "prepared revision"):
            report_status(self.day, self.root)

    def test_different_local_and_public_update_is_rejected(self):
        workspace = self.update()
        report = workspace / "reports" / self.day / "report.html"
        write_text(report, "Different local report")
        path = workspace / "reports" / self.day / "manifest.json"
        manifest = read_json(path)
        manifest["sha256"][f"reports/{self.day}/report.html"] = sha256(report)
        write_json(path, manifest)
        with self.assertRaisesRegex(ValueError, "Local and public editions differ"):
            report_status(self.day, self.root)

    def test_stale_library_counts_fail_instead_of_being_reported(self):
        self.update()
        path = self.root / "public/library.json"
        library = read_json(path)
        library["counts"]["tools"] = 999
        write_json(path, library)
        with self.assertRaisesRegex(ValueError, "Published library differs"):
            report_status(self.day, self.root)

    def test_cli_revision_inspection_uses_owning_root_and_keeps_original_receipt(self):
        self.update()
        before = self.snapshot()
        output, errors = StringIO(), StringIO()
        with patch.object(cli, "ROOT", self.root), \
                patch("sys.argv", ["media-scout", "status", "--date", self.day, "--revision", "2"]), \
                redirect_stdout(output), redirect_stderr(errors):
            self.assertEqual(cli.main(), 0)
        self.assertEqual(errors.getvalue(), "")
        status = json.loads(output.getvalue())
        self.assertEqual(status["edition_id"], self.day + "-r2")
        self.assertIsNone(status["delivery"])
        self.assertEqual(status["publication"]["status"], "synced")
        self.assertEqual(before, self.snapshot())

    def test_missing_or_invalid_revision_fails_without_creating_a_workspace(self):
        before = self.snapshot()
        for revision in (True, 1, 0, -2, "2", 2):
            with self.subTest(revision=revision), self.assertRaises(ValueError):
                report_status(self.day, self.root, revision)
        self.assertEqual(before, self.snapshot())

    def test_new_day_does_not_claim_the_previous_days_reports_or_delivery(self):
        self.update()
        status = report_status("2026-10-02", self.root)
        self.assertFalse(status["built"])
        self.assertIsNone(status["delivery"])
        self.assertIsNone(status["latest_completed_edition"])
        self.assertIsNone(status["profile_count"])
        self.assertEqual(status["library"]["tools"], 2)
