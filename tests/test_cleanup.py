"""Deletion boundaries, recovery provenance and concurrent-work protection."""

import hashlib
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

from media_scout import cleanup as housekeeping
from media_scout.storage import locked, sha256, write_json, write_text


class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.day, self.edition = "2026-11-06", "2026-10-20"
        self.stamp = time.time()
        self.row = {"id": 1, "full_name": "owner/art", "description": "Creative AI tool",
                    "license": {"spdx_id": "MIT"}, "stargazers_count": 8}
        self.query = self.root / "research" / self.edition / "queries/images-0-page-1.json"
        write_json(self.query, {"items": [self.row]})
        self.manifest = self.root / "reports" / self.edition / "manifest.json"
        self.hashes = {self.query.relative_to(self.root).as_posix(): sha256(self.query)}
        self.seal()
        write_json(self.root / f"state/deliveries/{self.edition}.json", {"status": "sent"})
        write_json(self.root / f"state/publications/{self.edition}.json", {"status": "synced"})

    def seal(self):
        write_json(self.manifest, {"report_date": self.edition, "sha256": self.hashes})

    def old(self, rel, data="temporary"):
        path = self.root / rel
        write_text(path, data)
        os.utime(path, (self.stamp - 70 * housekeeping.DAY,) * 2)
        return path

    def metadata(self, value=None, name="query-metadata-union.json"):
        return self.old(f"research/{self.edition}/{name}",
                        json.dumps([self.row] if value is None else value))

    def run_cleanup(self, apply=False):
        return housekeeping.cleanup(self.day, self.root, apply=apply, stamp=self.stamp)

    def test_preview_then_apply_removes_only_proven_copy_and_journals_recovery(self):
        path = self.metadata()
        before = self.query.read_bytes()
        plan = self.run_cleanup()
        self.assertEqual(plan["candidate_files"], 1)
        self.assertTrue(path.exists())
        self.assertFalse((self.root / "state/cleanup").exists())
        result = self.run_cleanup(apply=True)
        self.assertEqual(result["deleted_files"], 1)
        self.assertFalse(path.exists())
        self.assertEqual(self.query.read_bytes(), before)
        journal = json.loads((self.root / result["receipt"]).read_text())
        self.assertEqual(journal["status"], "applied")
        self.assertIn(self.query.relative_to(self.root).as_posix(),
                      next(iter(journal["proofs"].values()))["source_queries"])
        self.assertEqual(self.run_cleanup()["candidate_files"], 0)

    def test_raw_map_and_counter_wrappers_are_recoverable_but_annotations_are_kept(self):
        for value in [{"owner/art": self.row}, {"unique_metadata": 1, "records": [self.row]},
                      {"observed": 4, "unpublished": 1, "candidates": [self.row]},
                      {"unique_metadata": 1, "records": {"owner/art": self.row}}]:
            path = self.metadata(value)
            self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 1)
            self.assertFalse(path.exists())
        for value in [{"candidates": [self.row], "note": "Unique research judgment"},
                      [dict(self.row, research_note="Keep this assessment")],
                      [{"full_name": "owner/other"}], {"records": [self.row], "count": "annotated"}]:
            path = self.metadata(value)
            self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
            self.assertTrue(path.exists())

    def test_protected_and_tracked_files_are_never_candidates(self):
        path = self.metadata()
        self.hashes[path.relative_to(self.root).as_posix()] = sha256(path)
        bytecode = self.old("media_scout/__pycache__/proof.pyc")
        self.hashes[bytecode.relative_to(self.root).as_posix()] = sha256(bytecode)
        self.seal()
        tracked = self.old("tests/__pycache__/tracked.pyc")
        with patch.object(housekeeping, "_tracked", return_value={tracked.relative_to(self.root).as_posix()}):
            self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        self.assertTrue(all(p.exists() for p in [path, bytecode, tracked]))

    def test_active_unsealed_recent_and_pc_runtime_work_are_kept(self):
        path = self.metadata()
        os.utime(path, (self.stamp,) * 2)
        runtime = self.old("pc_demo/.local/runtime/__pycache__/model.pyc")
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        self.assertTrue(all(p.exists() for p in [path, runtime]))

    def test_unfinished_research_preserves_atomic_recovery_files(self):
        atomic = self.old("state/.scout-abcdefgh")
        self.old("research/2026-11-05/queries/in-progress.json", "{}")
        with self.assertRaisesRegex(RuntimeError, "Unfinished dated research"):
            self.run_cleanup(apply=True)
        self.assertTrue(atomic.exists())

    def test_pending_send_or_unfinished_publication_blocks_all_deletions(self):
        path = self.old("media_scout/__pycache__/old.pyc")
        receipt = self.root / f"state/deliveries/{self.edition}.json"
        for status in ["reserved", "uncertain"]:
            write_json(receipt, {"status": status})
            with self.assertRaisesRegex(RuntimeError, "reconciliation"):
                self.run_cleanup(apply=True)
            self.assertTrue(path.exists())
        write_json(receipt, {"status": "sent"})
        (self.root / f"state/publications/{self.edition}.json").unlink()
        with self.assertRaisesRegex(RuntimeError, "Unfinished"):
            self.run_cleanup(apply=True)
        self.assertTrue(path.exists())

    def test_tampered_provenance_blocks_before_any_deletion(self):
        metadata = self.metadata()
        bytecode = self.old("tests/__pycache__/old.pyc")
        self.query.write_text('{"items": []}')
        with self.assertRaisesRegex(ValueError, "Sealed query changed"):
            self.run_cleanup(apply=True)
        self.assertTrue(metadata.exists())
        self.assertTrue(bytecode.exists())

    def test_changed_candidate_is_kept_and_partial_status_is_recorded(self):
        path = self.metadata()
        original = housekeeping._plan
        def changed(*args):
            plan = original(*args)
            path.write_text("new work after planning")
            return plan
        with patch.object(housekeeping, "_plan", side_effect=changed):
            result = self.run_cleanup(apply=True)
        self.assertEqual(result["status"], "partial")
        self.assertEqual(path.read_text(), "new work after planning")

    def test_source_changed_after_plan_also_blocks_deletion(self):
        path = self.metadata()
        original = housekeeping._plan
        def changed(*args):
            plan = original(*args)
            self.query.write_text("changed source")
            return plan
        with patch.object(housekeeping, "_plan", side_effect=changed), \
                self.assertRaisesRegex(ValueError, "Sealed query changed"):
            self.run_cleanup(apply=True)
        self.assertTrue(path.exists())

    def test_keep_cache_skips_repeat_analysis_but_never_authorizes_deletion(self):
        path = self.metadata([dict(self.row, unique_note="Retain this research")])
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        with patch.object(housekeeping, "_source_records", side_effect=AssertionError("repeat source scan")):
            self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        self.assertTrue(path.exists())
        self.metadata()  # Changed bytes invalidate the keep decision.
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 1)

    def test_symlinked_journal_directory_blocks_all_removals(self):
        path = self.old("tests/__pycache__/old.pyc")
        (self.root / "elsewhere").mkdir()
        (self.root / "state/cleanup").symlink_to(self.root / "elsewhere", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Unsafe cleanup state"):
            self.run_cleanup(apply=True)
        self.assertTrue(path.exists())

    def test_symlinks_hardlinks_and_unknown_temporary_names_are_kept(self):
        outside = self.old("keep.txt")
        link = self.root / "media_scout/__pycache__/link.pyc"
        link.parent.mkdir(parents=True)
        link.symlink_to(outside)
        hardlink = link.parent / "hard.pyc"
        os.link(outside, hardlink)
        temp = self.old("state/.scout-important-backup")
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        self.assertTrue(outside.exists() and link.is_symlink() and hardlink.exists() and temp.exists())

    def test_hardlinked_archives_are_valid_provenance_but_are_never_removed(self):
        path = self.metadata()
        os.link(self.manifest, self.root / "manifest-backup.json")
        os.link(self.query, self.root / "query-backup.json")
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 1)
        self.assertFalse(path.exists())
        self.assertEqual(sha256(self.query), self.hashes[self.query.relative_to(self.root).as_posix()])

    def test_only_unused_recognized_cache_and_old_atomic_temps_are_removed(self):
        url = "https://api.github.com/repos/owner/art/readme"
        name = hashlib.sha256(url.encode()).hexdigest() + ".json"
        cached = self.old("state/http-cache/" + name, json.dumps(
            {"version": 1, "url": url, "etag": '"v1"', "sha256": "hash", "body": "data"}))
        atomic = self.old("state/.scout-abcdefgh")
        current = self.old("state/http-cache/" + "a" * 64 + ".json", "{}")
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 2)
        self.assertFalse(cached.exists() or atomic.exists())
        self.assertTrue(current.exists())

    def test_reused_cache_and_recently_completed_metadata_are_retained(self):
        url = "https://api.github.com/repos/owner/art/readme"
        name = hashlib.sha256(url.encode()).hexdigest() + ".json"
        cached = self.old("state/http-cache/" + name, json.dumps(
            {"version": 1, "url": url, "etag": '"v1"', "sha256": "hash", "body": "data"}))
        os.utime(cached, (self.stamp - housekeeping.DAY,) * 2)
        self.assertEqual(self.run_cleanup(apply=True)["deleted_files"], 0)
        self.assertTrue(cached.exists())
        # A complete new edition remains within the seven-day working window.
        path = self.metadata()
        result = housekeeping.cleanup("2026-10-21", self.root, apply=True, stamp=self.stamp)
        self.assertEqual(result["deleted_files"], 0)
        self.assertTrue(path.exists())

    def test_lock_and_invalid_manifest_refuse_cleanup(self):
        path = self.old("tests/__pycache__/old.pyc")
        with locked(self.root), self.assertRaisesRegex(RuntimeError, "active"):
            self.run_cleanup(apply=True)
        self.hashes["../outside"] = "0" * 64
        self.seal()
        with self.assertRaisesRegex(ValueError, "Unsafe path"):
            self.run_cleanup(apply=True)
        self.assertTrue(path.exists())

    def test_symlinked_report_directory_cannot_hide_a_manifest(self):
        path = self.old("tests/__pycache__/old.pyc")
        (self.root / "reports/alias").symlink_to(self.manifest.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlinked report"):
            self.run_cleanup(apply=True)
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
