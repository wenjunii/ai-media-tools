"""Classify real Git diffs, including deletes, renames, and multi-commit pushes."""

from pathlib import Path
import subprocess
import tempfile
import unittest

from media_scout.ci import classify


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-b", "main")
        self.git("config", "user.email", "ci@example.test")
        self.git("config", "user.name", "CI Test")
        self.commit("source.py")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def commit(self, path):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("change\n")
        self.git("add", ".")
        self.git("commit", "-m", "fixture")

    def scope(self, event="push", before=None, head=None):
        base = before or self.base
        return classify(self.root, event, {"before": base, "pull_request": {"base": {"sha": base}}},
                        head or self.git("rev-parse", "HEAD"))

    def test_publication_and_docs_only_skip_platform_tests_on_pr_and_push(self):
        self.commit("public/reports/2026-10-21/report.json")
        self.commit("public/library.json")
        self.commit("config/quality_reviews.json")
        self.commit("docs/GITHUB_SYNC.md")
        self.assertFalse(self.scope()["full"])
        self.assertFalse(self.scope("pull_request")["full"])
        self.assertEqual(self.scope()["changed_files"], 4)

    def test_earlier_source_change_in_a_multicommit_push_is_not_hidden_by_docs_tip(self):
        self.commit("media_scout/client.py")
        self.commit("README.md")
        self.assertTrue(self.scope()["full"])

    def test_source_deletion_and_rename_into_docs_still_run_all_tests(self):
        (self.root / "source.py").rename(self.root / "README.md")
        self.git("add", "-A")
        self.git("commit", "-m", "rename")
        self.assertTrue(self.scope()["full"])

    def test_manual_empty_missing_base_wrong_head_and_malformed_events_run_all_tests(self):
        self.assertTrue(self.scope()["full"])
        self.commit("README.md")
        for event, before, head in [("workflow_dispatch", None, None),
                                     ("push", "0" * 40, None), ("push", "1" * 40, None),
                                     ("push", None, self.base), ("unknown", None, None)]:
            with self.subTest(event=event, before=before, head=head):
                self.assertTrue(self.scope(event, before, head)["full"])
        self.assertTrue(classify(self.root, "pull_request", {}, self.git("rev-parse", "HEAD"))["full"])

    def test_unknown_public_files_and_workflow_or_pc_changes_are_not_exempt(self):
        for path in ("public/extra.js", ".github/workflows/ci.yml", "pc_demo/README.md",
                     "tests/test_ci.py", "media_scout/ui/library.js", "config/scout.json",
                     "docs/misleading.md\nscript.py"):
            self.commit(path)
            self.assertTrue(self.scope()["full"])
            self.base = self.git("rev-parse", "HEAD")


if __name__ == "__main__":
    unittest.main()
