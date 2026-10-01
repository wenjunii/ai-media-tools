"""Publication integrity and GitHub-before-email checks using real local Git."""

import json
from pathlib import Path
import subprocess
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

        self.addCleanup(patch.stopall)
        patch("media_scout.publication._run", side_effect=local_git_and_ci).start()

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
        write_text(self.root / "README.md", "A reviewed project improvement\n")
        self.git("add", "README.md")
        self.git("commit", "-m", "Improve project")
        self.git("push", "origin", "main")
        with self.assertRaisesRegex(ValueError, "stale"):
            delivery.prepare(self.day, self.root)
        self.assert_unreserved()
        refreshed = publication.record_sync(self.day, self.root)
        self.assertNotEqual(original["commit"], refreshed["commit"])
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
        with self.assertRaisesRegex(ValueError, "complete current report"):
            publication.record_sync(self.day, self.root)

    def test_a_staged_private_settings_file_is_blocked_before_push(self):
        self.git("add", "-f", "config/scout.local.json")
        with self.assertRaisesRegex(ValueError, "Private operational"):
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
