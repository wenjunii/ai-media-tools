"""Same-day publication keeps sealed history and never creates a second send."""

import copy
import shutil
import unittest

import test_publication
from media_scout.library import make_library
from media_scout.publication import export_report, verify_public_archive
from media_scout.report import build, verify_report
from media_scout.storage import read_json, sha256, write_json, write_text
from media_scout.updates import export_update, prepare_update, update_workspace


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_publication.report_fixture(self)
        self.root, self.day = self.fixture.root, self.fixture.day
        self.fixture.build()
        export_report(self.day, self.root)
        write_json(self.root / "state/deliveries" / (self.day + ".json"), {"status": "sent", "message_id": "original"})
        self.preserved = {str(p): sha256(p) for folder in ("reports", "research", "public/reports", "state/deliveries")
                          for p in (self.root / folder).rglob("*") if p.is_file()}

    def updated(self):
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
        return workspace

    def assert_preserved(self):
        self.assertEqual(self.preserved, {name: sha256(name) for name in self.preserved})

    def test_prepare_is_idempotent_and_copies_no_delivery_receipt(self):
        workspace = prepare_update(self.day, 2, self.root)
        self.assertEqual(prepare_update(self.day, 2, self.root), workspace)
        self.assertFalse((workspace / "state/deliveries").exists())
        self.assert_preserved()

    def test_export_adds_a_searchable_update_without_changing_original_files(self):
        workspace = self.updated()
        self.assertEqual(verify_report(self.day, workspace)["revision"], 2)
        result = export_update(self.day, 2, self.root)
        self.assertEqual(result["profile_count"], 1)
        self.assertEqual(verify_public_archive(self.root)["editions"], 2)
        library = read_json(self.root / "public/library.json")
        self.assertEqual(library["counts"]["tools"], 2)
        self.assertEqual(library["editions"][0]["edition_id"], self.day + "-r2")
        self.assertIn("updates/r2/report.html", (self.root / "site/index.html").read_text())
        self.assert_preserved()

    def test_updates_work_in_a_public_clone_without_private_evidence(self):
        self.updated()
        export_update(self.day, 2, self.root)
        for name in ("reports", "research", "state", "site"):
            shutil.rmtree(self.root / name)
        self.assertEqual(verify_public_archive(self.root)["library_tools"], 2)

    def test_updated_editions_are_also_immutable(self):
        self.updated()
        export_update(self.day, 2, self.root)
        path = self.root / "public/reports" / self.day / "updates/r2/report.md"
        write_text(path, "Unexpected update")
        with self.assertRaisesRegex(ValueError, "preserve|publication hash"):
            export_update(self.day, 2, self.root)
        self.assert_preserved()

    def test_update_export_requires_the_original_public_edition(self):
        self.updated()
        shutil.rmtree(self.root / "public/reports" / self.day)
        with self.assertRaisesRegex(ValueError, "original edition"):
            export_update(self.day, 2, self.root)
        self.assertFalse((self.root / "public/reports" / self.day / "updates").exists())

    def test_workspace_requires_valid_identity_and_an_unchanged_original(self):
        for revision in (True, 1, 0, -2, "2"):
            with self.subTest(revision=revision), self.assertRaises(ValueError):
                prepare_update(self.day, revision, self.root)
        workspace = prepare_update(self.day, 2, self.root)
        marker = read_json(workspace / "update.json")
        marker["original_manifest_sha256"] = "bad"
        write_json(workspace / "update.json", marker)
        with self.assertRaisesRegex(ValueError, "original edition changed"):
            update_workspace(self.day, 2, self.root)

    def test_same_day_review_history_uses_distinct_edition_ids(self):
        original = copy.deepcopy(self.fixture.editorial)
        updated = copy.deepcopy(original)
        updated["revision"] = 2
        updated["tools"][0]["requirements"]["hardware"] = "Updated documented requirement"
        data = make_library([updated, original], self.fixture.config)
        self.assertEqual(data["counts"]["tools"], 1)
        versions = data["tools"][0]["versions"]
        self.assertEqual(versions[0]["edition_id"], self.day + "-r2")
        self.assertNotIn("edition_id", versions[1])
        self.assertEqual(versions[1]["profile"]["requirements"]["hardware"], "Not documented")
