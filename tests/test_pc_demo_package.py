"""Local handoff and creator feedback tests; no app execution or network."""
import json
import pathlib
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.common import read_json, sha256, write_json
from pc_demo.captions import caption_text, transcript_text
from pc_demo.creator_review import creator_review_state, import_creator_review, review_identity, validate_review
from pc_demo.package import PACKAGE_FILES, export_package
from pc_demo.status import VERIFIED_ARTIFACTS, draft_status


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.local = pathlib.Path(self.temp.name) / '.local'
        self.run = self.local / 'runs/20261017-fixture'
        for name in VERIFIED_ARTIFACTS:
            path = self.run / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(name.encode())
        self.story = read_json(pathlib.Path(__file__).resolve().parents[1] / 'pc_demo/storyboard.json')
        write_json(self.run / 'storyboard.json', self.story)
        write_json(self.run / 'manifest.json', {
            'status': 'automated_checks_passed', 'video_sha256': sha256(self.run / 'draft.mp4'),
            'input_sha256': sha256(self.run / 'inputs/input.jpg'),
            'output_sha256': sha256(self.run / 'outputs/actual-output.png'),
            'inference': {'argv': ['C:/Private/tool.exe', 'private-runtime-detail']}})
        write_json(self.run / 'evidence/setup.json', {'machine': 'private-runtime-detail'})
        write_json(self.run / 'qa/manual-review.json', {'video_sha256': sha256(self.run / 'draft.mp4'),
                   'browser': {'ended': True}, 'visual_review': 'passed by automated test agent'})
        self.verify_fixture()
        for target in ('pc_demo.common.LOCAL', 'pc_demo.package.LOCAL'):
            patcher = patch(target, self.local)
            patcher.start()
            self.addCleanup(patcher.stop)

    def verify_fixture(self):
        # These are deliberately fake media bytes for file-boundary tests only.
        write_json(self.run / 'qa/verification.json', {
            'automated_pass': True, 'video_sha256': sha256(self.run / 'draft.mp4'),
            'checked_artifact_sha256': {name: sha256(self.run / name) for name in VERIFIED_ARTIFACTS},
            'duration_seconds': 45.022, 'dimensions': [1080, 1920], 'video_codec': 'h264', 'audio_codec': 'aac'})

    def package(self):
        with patch('urllib.request.urlopen', side_effect=AssertionError('No network permitted')), patch(
                'subprocess.run', side_effect=AssertionError('No app execution permitted')):
            return pathlib.Path(export_package(self.run)['directory'])

    def record(self, **changes):
        result = {'schema_version': 1, **review_identity(self.run), 'reviewed_utc': '2026-10-17T12:00:00Z',
                  'checks': {'playback': True, 'visual': True, 'captions': True, 'audio': True},
                  'decision': 'passed', 'notes': 'Synthetic fixture review for automated tests only'}
        result.update(changes)
        return result

    def import_record(self, record):
        path = self.local / 'downloaded review.json'
        write_json(path, record)
        return import_creator_review(self.run, path)

    def test_package_copies_video_and_allowlisted_materials_without_mutating_run(self):
        original = {p.relative_to(self.run): p.read_bytes() for p in self.run.rglob('*') if p.is_file()}
        package = self.package()
        self.assertEqual({p.name for p in package.iterdir()}, set(PACKAGE_FILES) | {'package.json'})
        self.assertEqual((package / 'draft.mp4').read_bytes(), original[pathlib.Path('draft.mp4')])
        receipt = read_json(package / 'package.json')
        self.assertFalse(receipt['social_publishing_enabled'])
        self.assertEqual(receipt['creator_review_status'], 'pending')
        for name, digest in receipt['files'].items():
            self.assertEqual(sha256(package / name), digest)
        for name in ('package.json', 'review.html', 'README.md'):
            self.assertNotIn('private-runtime-detail', (package / name).read_text())
            self.assertNotIn(str(self.run), (package / name).read_text())
        self.assertEqual(original, {p.relative_to(self.run): p.read_bytes() for p in self.run.rglob('*') if p.is_file()})

    def test_packages_are_distinct_and_latest_pointer_moves_only_after_success(self):
        first = self.package()
        first_receipt = (first / 'package.json').read_bytes()
        second = self.package()
        self.assertNotEqual(first, second)
        self.assertEqual(read_json(self.local / 'latest-package.json')['directory'], str(second))
        self.assertEqual((first / 'package.json').read_bytes(), first_receipt)

    def test_modified_draft_is_rejected_before_export(self):
        (self.run / 'draft.mp4').write_bytes(b'changed video')
        with self.assertRaisesRegex(ValueError, 'current automated checks'):
            self.package()
        self.assertFalse((self.local / 'packages').exists())

    def test_failed_copy_preserves_last_package_and_failure_evidence(self):
        self.package()
        pointer = (self.local / 'latest-package.json').read_bytes()
        with patch('pc_demo.package.shutil.copyfile', side_effect=OSError('disk full')):
            with self.assertRaisesRegex(OSError, 'disk full'):
                self.package()
        self.assertEqual((self.local / 'latest-package.json').read_bytes(), pointer)
        failed = list((self.local / 'packages').glob('*/failure.json'))
        self.assertEqual(len(failed), 1)
        self.assertEqual(read_json(failed[0])['status'], 'failed')

    def test_source_change_during_copy_is_detected(self):
        real_copy = shutil.copyfile
        def copy_then_change(source, target):
            real_copy(source, target)
            (self.run / 'storyboard.json').write_text('{}')
        with patch('pc_demo.package.shutil.copyfile', side_effect=copy_then_change):
            with self.assertRaisesRegex(ValueError, 'changed during packaging'):
                self.package()
        self.assertFalse((self.local / 'latest-package.json').exists())

    def test_pointer_write_failure_keeps_previous_package_selected(self):
        self.package()
        pointer = (self.local / 'latest-package.json').read_bytes()
        def fail_pointer(path, value):
            if path.suffix == '.partial':
                path.write_text('{')
                raise OSError('pointer write failed')
            write_json(path, value)
        with patch('pc_demo.package.write_json', side_effect=fail_pointer):
            with self.assertRaisesRegex(OSError, 'pointer write failed'):
                self.package()
        self.assertEqual((self.local / 'latest-package.json').read_bytes(), pointer)

    def test_sidecars_are_derived_from_verified_story_not_unbound_run_text(self):
        (self.run / 'captions.srt').write_text('unverified private edit')
        package = self.package()
        self.assertEqual((package / 'captions.srt').read_text(), caption_text(self.story))
        self.assertEqual((package / 'transcript.txt').read_text(), transcript_text(self.story))
        self.assertIn('00:00:07.500 --> 00:00:15.000', (package / 'captions.vtt').read_text())
        self.assertNotIn('unverified private edit', (package / 'captions.srt').read_text())

    def test_title_and_subtitle_markup_are_escaped_in_review_page(self):
        self.story['title'] = '__REVIEW_DATA__ </script><script>alert("x")</script>'
        self.story['segments'][0]['narration'] = 'A <b>line</b> & another line.'
        write_json(self.run / 'storyboard.json', self.story)
        self.verify_fixture()
        page = (self.package() / 'review.html').read_text()
        self.assertNotIn('</script><script>alert', page)
        payload = re.search(r'<script type="application/json" id="review-data">(.*?)</script>', page, re.S).group(1)
        data = json.loads(payload)
        self.assertEqual(data['title'], self.story['title'])
        self.assertIn('&lt;b&gt;line&lt;/b&gt;', data['subtitles'])

    def test_agent_playback_review_never_becomes_creator_approval(self):
        state = draft_status(self.run)
        self.assertTrue(state['automated_checks_passed'])
        self.assertIn('passed', state['browser_playback'])
        self.assertEqual(state['creator_review'], {'status': 'pending', 'complete': False})

    def test_webvtt_wrap_does_not_split_escaped_entities(self):
        self.story['segments'][0]['narration'] = '&' * 50
        text = caption_text(self.story, webvtt=True)
        self.assertIn('&amp;' * 48 + '\n' + '&amp;' * 2, text)

    def test_explicit_reviews_are_imported_and_previous_versions_retained(self):
        manual = (self.run / 'qa/manual-review.json').read_bytes()
        self.import_record(self.record())
        self.assertTrue(draft_status(self.run)['creator_review']['complete'])
        first = (self.run / 'qa/creator-review.json').read_bytes()
        record = self.record(decision='needs_changes')
        record['checks']['audio'] = False
        self.import_record(record)
        self.assertEqual(creator_review_state(self.run)['status'], 'needs_changes')
        self.assertFalse(creator_review_state(self.run)['complete'])
        history = list((self.run / 'qa/creator-review-history').glob('*.json'))
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].read_bytes(), first)
        self.assertEqual((self.run / 'qa/manual-review.json').read_bytes(), manual)

    def test_wrong_draft_or_incomplete_pass_cannot_be_imported(self):
        for change in ({'video_sha256': 'wrong'}, {'storyboard_sha256': 'wrong'}, {'run_id': 'another'},
                       {'checks': {'playback': True, 'visual': True, 'captions': True, 'audio': False}}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.import_record(self.record(**change))
        self.assertFalse((self.run / 'qa/creator-review.json').exists())

    def test_existing_creator_review_becomes_stale_after_story_changes(self):
        self.import_record(self.record())
        (self.run / 'storyboard.json').write_text('{}')
        self.assertEqual(creator_review_state(self.run), {'status': 'stale', 'complete': False})

    def test_review_requires_current_automated_pass(self):
        record = self.record()
        write_json(self.run / 'qa/verification.json', {'status': 'failed', 'automated_pass': False})
        with self.assertRaisesRegex(ValueError, 'Run verify'):
            self.import_record(record)

    def test_review_validation_is_strict_and_oversized_files_are_rejected(self):
        identity = review_identity(self.run)
        for change in ({'schema_version': True}, {'decision': 'approved'}, {'reviewed_utc': 'yesterday'},
                       {'notes': 'x' * 2001}, {'checks': dict.fromkeys(('playback','visual','captions','audio'), 'true')}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_review(self.record(**change), identity)
        path = self.local / 'large.json'
        path.write_bytes(b'x' * 65537)
        with self.assertRaisesRegex(ValueError, '64 KiB'):
            import_creator_review(self.run, path)
