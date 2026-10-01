"""Publication integrity and GitHub-before-email checks using real local Git."""

import json
import copy
from pathlib import Path
import subprocess
import shutil
import tempfile
import unittest
from unittest.mock import patch

import test_workflow
from media_scout import delivery, publication
from media_scout.storage import read_json, sha256, write_json, write_text


def report_fixture(test):
    fixture = test_workflow.WorkflowTests()
    fixture.setUp()
    test.addCleanup(fixture.doCleanups)
    fixture.config["recipient"] = None
    fixture.config["github_sync"] = {"repository": "example/scout", "branch": "main",
                                     "ci_workflow": "ci.yml", "required_before_email": True}
    write_json(fixture.root / "config/scout.json", fixture.config)
    write_json(fixture.root / "config/scout.local.json", {"recipient": "recipient@example.com"})
    return fixture


class PublicationExportTests(unittest.TestCase):
    def setUp(self):
        self.fixture = report_fixture(self)
        self.root, self.day = self.fixture.root, self.fixture.day

    def test_export_keeps_finished_files_exact_and_excludes_private_manifest(self):
        manifest = self.fixture.build()
        before = {name: sha256(self.root / name) for name in manifest["sha256"]}
        manifest_hash = sha256(self.root / "reports" / self.day / "manifest.json")
        result = publication.export_report(self.day, self.root)
        for name in publication.REPORT_FILES:
            self.assertEqual((self.root / "reports" / self.day / name).read_bytes(),
                             (self.root / "public/reports" / self.day / name).read_bytes())
        for name in result["files"]:
            self.assertNotIn("recipient@example.com", (self.root / name).read_text())
        self.assertFalse((self.root / "public/reports" / self.day / "manifest.json").exists())
        self.assertNotIn("../reports/", (self.root / "public/index.html").read_text())
        self.assertIn(f"reports/{self.day}/report.md", (self.root / "public/README.md").read_text())
        self.assertEqual(before, {name: sha256(self.root / name) for name in before})
        self.assertEqual(manifest_hash, sha256(self.root / "reports" / self.day / "manifest.json"))

    def test_existing_public_edition_is_never_overwritten(self):
        self.fixture.build()
        publication.export_report(self.day, self.root)
        target = self.root / "public/reports" / self.day / "report.md"
        write_text(target, "Unexpected edit")
        with self.assertRaisesRegex(ValueError, "preserve"):
            publication.export_report(self.day, self.root)
        self.assertEqual(target.read_text(), "Unexpected edit")

    def test_private_recipient_in_report_blocks_export_before_writing(self):
        self.fixture.editorial["summary"] = "Do not publish recipient@example.com"
        write_json(self.fixture.editorial_path, self.fixture.editorial)
        self.fixture.build()
        with self.assertRaisesRegex(ValueError, "private"):
            publication.export_report(self.day, self.root)
        self.assertFalse((self.root / "public").exists())

    def test_credential_in_report_blocks_export_without_echoing_it(self):
        token = "ghp_" + "a" * 40
        self.fixture.editorial["summary"] = token
        write_json(self.fixture.editorial_path, self.fixture.editorial)
        self.fixture.build()
        with self.assertRaisesRegex(ValueError, "credential") as raised:
            publication.export_report(self.day, self.root)
        self.assertNotIn(token, str(raised.exception))
        self.assertFalse((self.root / "public").exists())

    def test_symlinked_export_directory_is_rejected(self):
        self.fixture.build()
        target = self.root / "unrelated"
        target.mkdir()
        (self.root / "public").symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinks"):
            publication.export_report(self.day, self.root)
        self.assertEqual(list(target.iterdir()), [])


class PublicArchiveTests(unittest.TestCase):
    def setUp(self):
        self.fixture = report_fixture(self)
        self.root, self.day = self.fixture.root, self.fixture.day
        self.fixture.build()
        publication.export_report(self.day, self.root)
        self.folder = self.root / "public/reports" / self.day

    def test_public_archive_verification_needs_no_private_artifacts_and_does_not_write(self):
        before = {str(path): sha256(path) for path in (self.root / "public").rglob("*") if path.is_file()}
        for name in ("reports", "research", "state", "site"):
            shutil.rmtree(self.root / name)
        (self.root / "config/scout.local.json").unlink()
        self.assertEqual(publication.verify_public_archive(self.root),
                         {"status": "passed", "editions": 1, "report_files_checked": 3, "library_tools": 1})
        self.assertEqual(before, {str(path): sha256(path) for path in (self.root / "public").rglob("*") if path.is_file()})

    def test_changed_published_content_fails_its_hash_check(self):
        write_text(self.folder / "report.html", "Incomplete report")
        with self.assertRaisesRegex(ValueError, "publication hash"):
            publication.verify_public_archive(self.root)

    def test_missing_public_file_fails_verification(self):
        (self.folder / "report.md").unlink()
        with self.assertRaisesRegex(ValueError, "missing required files"):
            publication.verify_public_archive(self.root)

    def test_invalid_metadata_does_not_authorize_an_archive(self):
        path = self.folder / "publication.json"
        original = read_json(path)
        changes = ({"report_date": "2026-09-30"}, {"recipient": "private@example.com"},
                   {"profile_count": True}, {"profile_count": -1}, {"profile_count": 50},
                   {"sealed_at": None}, {"sealed_at": "2026-10-01T08:00:00"},
                   {"sha256": {"report.md": "../outside"}})
        for change in changes:
            with self.subTest(field=next(iter(change))):
                write_json(path, dict(copy.deepcopy(original), **change))
                with self.assertRaises(ValueError):
                    publication.verify_public_archive(self.root)

    def test_report_json_cannot_change_its_date_by_updating_a_public_hash(self):
        path = self.folder / "report.json"
        report = read_json(path)
        report["report_date"] = "2026-09-30"
        write_json(path, report)
        metadata = read_json(self.folder / "publication.json")
        metadata["sha256"]["report.json"] = sha256(path)
        write_json(self.folder / "publication.json", metadata)
        with self.assertRaisesRegex(ValueError, "disagree"):
            publication.verify_public_archive(self.root)

    def test_index_cannot_link_to_an_unpublished_edition(self):
        path = self.root / "public/index.html"
        write_text(path, path.read_text() + '<a href="reports/1999-01-01/report.html">Missing edition</a>')
        with self.assertRaisesRegex(ValueError, "unpublished or invalid"):
            publication.verify_public_archive(self.root)

    def test_index_cannot_link_back_into_the_private_report_directory(self):
        path = self.root / "public/index.html"
        write_text(path, path.read_text().replace("reports/", "../reports/"))
        with self.assertRaisesRegex(ValueError, "unpublished or invalid"):
            publication.verify_public_archive(self.root)

    def test_readme_cannot_silently_drop_an_edition(self):
        write_text(self.root / "public/README.md", "Empty archive")
        with self.assertRaisesRegex(ValueError, "README"):
            publication.verify_public_archive(self.root)

    def test_library_data_cannot_drop_a_previously_published_tool(self):
        path = self.root / "public/library.json"
        data = read_json(path)
        data["tools"] = []
        write_json(path, data)
        with self.assertRaisesRegex(ValueError, "Published library differs"):
            publication.verify_public_archive(self.root)

    def test_a_missing_browser_asset_blocks_publication(self):
        (self.root / "public/assets/library.js").unlink()
        with self.assertRaisesRegex(ValueError, "Published library differs"):
            publication.verify_public_archive(self.root)

    def test_library_can_be_rebuilt_in_a_clone_without_private_research(self):
        before = {name: sha256(self.folder / name) for name in publication.REPORT_FILES}
        for name in ("reports", "research", "state", "site"):
            shutil.rmtree(self.root / name)
        (self.root / "config/scout.local.json").unlink()
        result = publication.rebuild_library(self.root)
        self.assertEqual(result["tools"], 1)
        self.assertTrue((self.root / "site/assets/library.js").is_file())
        self.assertEqual(before, {name: sha256(self.folder / name) for name in publication.REPORT_FILES})
        publication.verify_public_archive(self.root)


class PublicationCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.fixture = report_fixture(self)
        self.root, self.day = self.fixture.root, self.fixture.day
        self.manifest = self.fixture.build()
        publication.export_report(self.day, self.root)
        write_text(self.root / ".gitignore", "/state/\n/research/\n/reports/\n/site/\n/editorial.json\nconfig/*.local.json\n")
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test Publisher")
        self.git("config", "user.email", "publisher@users.noreply.github.com")
        self.git("add", ".gitignore", "config/scout.json", "public")
        self.git("commit", "-m", "Publish fixture")
        self.remote_temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.remote_temp.cleanup)
        self.bare = Path(self.remote_temp.name) / "remote.git"
        subprocess.run(["git", "init", "--bare", str(self.bare)], capture_output=True, check=True)
        self.git("remote", "add", "origin", str(self.bare))
        self.git("push", "-u", "origin", "main")
        self.remote_url = "https://github.com/example/scout.git"
        self.ci_status, self.ci_conclusion = "completed", "success"
        self.include_older_success = False
        actual_run = publication._run

        def local_git_and_ci(args, root):
            if args[:4] == ["git", "remote", "get-url", "origin"]:
                return self.remote_url.encode()
            if args[:3] == ["gh", "run", "list"]:
                head = self.git("rev-parse", "HEAD").decode().strip()
                result = [{"headSha": head, "databaseId": 10, "status": self.ci_status,
                           "conclusion": self.ci_conclusion, "url": "https://github.com/example/scout/actions/runs/10"}]
                if self.include_older_success:
                    old = dict(result[0], databaseId=9, status="completed", conclusion="success")
                    result.append(old)
                return json.dumps(result).encode()
            return actual_run(args, root)

        runner_patch = patch("media_scout.publication._run", side_effect=local_git_and_ci)
        self.addCleanup(runner_patch.stop)
        runner_patch.start()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, check=True).stdout

    def assert_unreserved(self):
        self.assertFalse((self.root / "state/deliveries" / (self.day + ".json")).exists())
        self.assertFalse((self.root / "state/outbox" / (self.day + ".json")).exists())

    def test_missing_sync_checkpoint_blocks_email_before_reservation(self):
        with self.assertRaisesRegex(ValueError, "sync checkpoint"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()

    def test_verified_remote_and_ci_allow_exactly_one_email_reservation(self):
        receipt = publication.record_sync(self.day, self.root)
        self.assertEqual(receipt, publication.verify_sync(self.day, self.root))
        self.assertEqual(delivery.prepare(self.day, self.root)["status"], "reserved")
        delivery_receipt = read_json(self.root / "state/deliveries" / (self.day + ".json"))
        self.assertEqual(delivery_receipt["github_commit"], receipt["commit"])
        self.assertEqual(delivery_receipt["github_report_url"], receipt["report_url"])
        with self.assertRaisesRegex(RuntimeError, "Reconcile"):
            delivery.prepare(self.day, self.root)

    def test_failed_latest_ci_cannot_use_an_older_success(self):
        publication.record_sync(self.day, self.root)
        self.ci_conclusion, self.include_older_success = "failure", True
        with self.assertRaisesRegex(RuntimeError, "CI"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()

    def test_pending_ci_blocks_a_sync_checkpoint(self):
        self.ci_status, self.ci_conclusion = "in_progress", ""
        with self.assertRaisesRegex(RuntimeError, "CI"):
            publication.record_sync(self.day, self.root)
        self.assertFalse((self.root / "state/publications" / (self.day + ".json")).exists())

    def test_wrong_repository_does_not_authorize_delivery(self):
        publication.record_sync(self.day, self.root)
        self.remote_url = "https://github.com/other/scout.git"
        with self.assertRaisesRegex(ValueError, "origin"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()

    def test_changed_commit_needs_a_fresh_checkpoint(self):
        original = publication.record_sync(self.day, self.root)
        original_bytes = (self.root / "state/publications" / (self.day + ".json")).read_bytes()
        write_text(self.root / "README.md", "A reviewed project improvement\n")
        self.git("add", "README.md")
        self.git("commit", "-m", "Improve project")
        self.git("push", "origin", "main")
        with self.assertRaisesRegex(ValueError, "stale"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()
        refreshed = publication.record_sync(self.day, self.root)
        self.assertNotEqual(original["commit"], refreshed["commit"])
        history = list((self.root / "state/publication_history" / self.day).glob("*.json"))
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].read_bytes(), original_bytes)
        self.assertEqual(delivery.prepare(self.day, self.root)["status"], "reserved")

    def test_uncommitted_project_change_blocks_email(self):
        publication.record_sync(self.day, self.root)
        write_text(self.root / "README.md", "Not synchronized\n")
        with self.assertRaisesRegex(ValueError, "not fully committed"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()

    def test_committed_report_tampering_is_detected_despite_matching_git_refs(self):
        target = self.root / "public/reports" / self.day / "report.md"
        write_text(target, "Incomplete edition\n")
        self.git("add", "public")
        self.git("commit", "-m", "Unexpected publication change")
        self.git("push", "origin", "main")
        with self.assertRaisesRegex(ValueError, "publication hash"):
            publication.record_sync(self.day, self.root)

    def test_a_staged_private_settings_file_is_blocked_before_push(self):
        self.git("add", "-f", "config/scout.local.json")
        with self.assertRaisesRegex(ValueError, "Private operational"):
            publication.audit_publication(self.root)

    def test_staging_a_resealed_old_edition_is_blocked_before_push(self):
        path = self.root / "public/reports" / self.day / "report.md"
        write_text(path, "Changed historical content")
        metadata_path = path.parent / "publication.json"
        metadata = read_json(metadata_path)
        metadata["sha256"]["report.md"] = sha256(path)
        write_json(metadata_path, metadata)
        self.git("add", "public")
        with self.assertRaisesRegex(ValueError, "immutable"):
            publication.audit_publication(self.root)

    def test_a_staged_source_leak_is_blocked_without_echoing_the_value(self):
        secret = "github_pat_" + "a" * 50
        write_text(self.root / "README.md", secret)
        self.git("add", "README.md")
        with self.assertRaisesRegex(ValueError, "credential") as raised:
            publication.audit_publication(self.root)
        self.assertNotIn(secret, str(raised.exception))

    def test_already_sent_receipt_survives_new_sync_requirements(self):
        original = {"status": "sent", "message_id": "existing-message"}
        path = self.root / "state/deliveries" / (self.day + ".json")
        write_json(path, original)
        self.assertEqual(delivery.prepare(self.day, self.root),
                         {"status": "already-sent", "message_id": "existing-message"})
        self.assertEqual(read_json(path), original)


if __name__ == "__main__":
    unittest.main()
