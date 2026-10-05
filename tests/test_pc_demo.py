"""PC guardrails only: no app downloads, inference, credentials or media in CI."""
import hashlib
import copy
import io
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.audit import validate_index_entry
from pc_demo.common import download, execute, read_json, resolve_run, select_profile, sha256, write_json
from pc_demo.setup_runtime import verified_runtime
from pc_demo.status import VERIFIED_ARTIFACTS, draft_status, local_status, review_state
from pc_demo.storyboard import validate_storyboard
from pc_demo.revisions import prepare_revision, revise_demo
from pc_demo.history import local_history, format_history
from pc_demo.verify import verify_run


class ProfileSelectionTests(unittest.TestCase):
    def test_only_complete_profiles_are_executable_candidates(self):
        library={'tools':[{'id':'github:a/b','versions':[{'kind':'screened','profile':{}}]}]}
        with self.assertRaisesRegex(ValueError,'no complete profile'):
            select_profile(library,'github:a/b')

    def test_incomplete_profile_is_rejected(self):
        library={'tools':[{'id':'github:a/b','versions':[{'kind':'profile','profile':{'name':'B'}}]}]}
        with self.assertRaisesRegex(ValueError,'required sections'):
            select_profile(library,'github:a/b')

    def test_real_library_profile_and_safe_defaults(self):
        root=pathlib.Path(__file__).resolve().parents[1]
        version=select_profile(read_json(root/'public/library.json'),'github:xinntao/real-esrgan')
        self.assertEqual(version['kind'],'profile')
        settings=read_json(root/'pc_demo/runtime.lock.json')
        self.assertIs(settings['social_publishing_enabled'],False)
        self.assertIs(settings['daily_schedule_enabled'],False)
        self.assertFalse(any('input' in name or name.endswith('.mp4') for name in settings['app']['extract']))


class DownloadAndEvidenceTests(unittest.TestCase):
    def test_rejects_insecure_download(self):
        with self.assertRaisesRegex(ValueError,'HTTPS'):
            download('http://example.invalid/x',pathlib.Path('unused'))

    def test_hash_mismatch_preserves_previous_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=pathlib.Path(tmp)/'app.zip'
            target.write_bytes(b'previous')
            response=io.BytesIO(b'changed')
            response.url='https://example.invalid/app.zip'
            with patch('urllib.request.urlopen',return_value=response):
                with self.assertRaisesRegex(ValueError,'Checksum mismatch'):
                    download(response.url,target,hashlib.sha256(b'expected').hexdigest())
            self.assertEqual(target.read_bytes(),b'previous')
            self.assertEqual(target.with_suffix('.zip.partial').read_bytes(),b'changed')

    def test_matching_cache_needs_no_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=pathlib.Path(tmp)/'app.zip'
            target.write_bytes(b'pinned')
            with patch('urllib.request.urlopen',side_effect=AssertionError('Network should not be used')):
                download('https://example.invalid/app.zip',target,hashlib.sha256(b'pinned').hexdigest())

    def test_failed_execution_keeps_exit_code_and_logs(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)
            with self.assertRaisesRegex(RuntimeError,'exit code 7'):
                execute([sys.executable,'-c','import sys; print("failure evidence"); sys.exit(7)'],path,'test')
            record=read_json(path/'test.command.json')
            self.assertEqual(record['returncode'],7)
            self.assertIn('failure evidence',(path/'test.stdout.log').read_text())
            self.assertIn('elapsed_seconds',record)

    def test_missing_executable_is_an_explicit_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(OSError):
                execute([str(pathlib.Path(tmp)/'absent-program')],tmp,'missing')
            record=read_json(pathlib.Path(tmp)/'missing.command.json')
            self.assertIn('error',record)
            self.assertNotIn('returncode',record)


class LocalStatusTests(unittest.TestCase):
    def test_latest_run_requires_a_valid_local_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            local = pathlib.Path(tmp) / '.local'
            with patch('pc_demo.common.LOCAL', local):
                with self.assertRaisesRegex(ValueError, 'No completed local draft'):
                    resolve_run()
                for record in ([], {}, {'run': ''}, {'run': tmp}):
                    write_json(local / 'latest-run.json', record)
                    with self.subTest(record=record), self.assertRaises(ValueError):
                        resolve_run()
                run = local / 'runs/first'
                run.mkdir(parents=True)
                write_json(local / 'latest-run.json', {'run': str(run)})
                self.assertEqual(resolve_run(), run.resolve())

    def test_fresh_checkout_status_needs_no_downloads_or_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            local = pathlib.Path(tmp) / '.local'
            with patch('pc_demo.status.LOCAL', local), patch(
                    'urllib.request.urlopen', side_effect=AssertionError('Unexpected network')):
                result = local_status()
            self.assertFalse(result['installed'])
            self.assertFalse(result['draft_environment_exists'])
            self.assertIsNone(result['latest_run'])
            self.assertFalse(local.exists())

    def test_saved_review_only_applies_to_exact_video_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = pathlib.Path(tmp)
            record = {'video_sha256': 'reviewed', 'browser': {'ended': True},
                      'visual_review': 'passed: captions and output inspected'}
            write_json(run / 'qa/manual-review.json', record)
            original = (run / 'qa/manual-review.json').read_bytes()
            current = review_state(run, 'reviewed')
            self.assertIn('passed', current['browser_playback'])
            self.assertEqual(current['manual_review'], record)
            stale = review_state(run, 'changed')
            self.assertEqual(stale['browser_playback'], 'pending')
            self.assertEqual(stale['visual_review'], 'pending')
            self.assertIn('stale', stale['saved_review_status'])
            self.assertEqual((run / 'qa/manual-review.json').read_bytes(), original)

    def test_missing_or_malformed_review_is_not_a_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = pathlib.Path(tmp)
            self.assertEqual(review_state(run, 'video')['saved_review_status'], 'absent')
            for record in ([], {'video_sha256': 'video', 'browser': {'ended': False}}):
                write_json(run / 'qa/manual-review.json', record)
                self.assertEqual(review_state(run, 'video')['browser_playback'], 'pending')

    def test_modified_video_invalidates_previous_automated_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            local = pathlib.Path(tmp)
            run = local / 'runs/first'
            write_json(local / 'latest-run.json', {'run': str(run)})
            write_json(run / 'manifest.json', {'status': 'draft_verified', 'video_sha256': 'old'})
            write_json(run / 'qa/verification.json', {'automated_pass': True, 'video_sha256': 'old'})
            (run / 'draft.mp4').write_bytes(b'new video')
            with patch('pc_demo.status.LOCAL', local), patch('pc_demo.common.LOCAL', local):
                result = local_status()['latest_run']
            self.assertFalse(result['video_matches_manifest'])
            self.assertFalse(result['automated_checks_passed'])

    def test_incomplete_or_modified_runtime_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            local = root / '.local'
            app = local / 'apps/realesrgan-20220424'
            app.mkdir(parents=True)
            (app / 'tool.exe').write_bytes(b'pinned executable')
            (app / 'model.bin').write_bytes(b'pinned model')
            write_json(root / 'runtime.lock.json', {'app': {'extract': ['tool.exe', 'model.bin']}})
            receipt = {'runtime_lock_sha256': sha256(root / 'runtime.lock.json'), 'files': {}}
            write_json(local / 'setup.json', receipt)
            with patch('pc_demo.setup_runtime.ROOT', root), patch('pc_demo.setup_runtime.LOCAL', local):
                with self.assertRaisesRegex(RuntimeError, 'missing required'):
                    verified_runtime()
                receipt['files'] = {name: sha256(app / name) for name in ('tool.exe', 'model.bin')}
                write_json(local / 'setup.json', receipt)
                self.assertEqual(verified_runtime()[0], app)
                (app / 'model.bin').write_bytes(b'modified model')
                with self.assertRaisesRegex(RuntimeError, 'integrity failure'):
                    verified_runtime()


class StoryboardTests(unittest.TestCase):
    def setUp(self):
        self.story = read_json(pathlib.Path(__file__).resolve().parents[1] / 'pc_demo/storyboard.json')

    def test_valid_narration_and_caption_edits_are_supported(self):
        self.story['segments'][0]['narration'] = 'A revised opening line.'
        self.story['segments'][0]['caption'] = ['Actual preserved app output.']
        self.assertEqual(validate_storyboard(self.story), self.story)

    def test_unsupported_timing_layout_and_missing_limitation_are_rejected(self):
        changes = [lambda s: s.update(duration_seconds=60),
                   lambda s: s.update(fps=30.0),
                   lambda s: s['segments'][2].update(start=16),
                   lambda s: s['segments'][5].update(kind='result'),
                   lambda s: s['segments'][0].update(title=['one', 'two', 'three']),
                   lambda s: s['segments'][0].update(caption=['line\nbreak']),
                   lambda s: s['segments'][0].update(narration='')]
        for change in changes:
            story = copy.deepcopy(self.story)
            change(story)
            with self.subTest(story=story), self.assertRaises(ValueError):
                validate_storyboard(story)


class RevisionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.local = pathlib.Path(self.temporary.name) / '.local'
        self.source = self.local / 'runs/20261003-source'
        for name in ('inputs', 'outputs', 'logs', 'evidence', 'qa'):
            (self.source / name).mkdir(parents=True)
        root = pathlib.Path(__file__).resolve().parents[1]
        self.lock = read_json(root / 'pc_demo/runtime.lock.json')
        self.story = read_json(root / 'pc_demo/storyboard.json')
        write_json(self.source / 'storyboard.json', self.story)
        (self.source / 'inputs/input.jpg').write_bytes(b'original input')
        (self.source / 'outputs/actual-output.png').write_bytes(b'actual app output')
        self.command = {'returncode': 0, 'elapsed_seconds': 2.0,
                        'argv': ['reviewed-app.exe', '-i', 'input.jpg', '-o', 'actual-output.png']}
        write_json(self.source / 'logs/inference.command.json', self.command)
        for name in ('stdout', 'stderr'):
            (self.source / f'logs/inference.{name}.log').write_bytes(b'original log')
        write_json(self.source / 'evidence/setup.json', {'hardware': {}})
        write_json(self.source / 'evidence/library.json', {'original': True})
        self.manifest = {'status': 'failed', 'app': self.lock['app'], 'inference': self.command,
                         'settings': {'model': self.lock['app']['model'], 'scale': 4, 'input_size': [256, 256]},
                         'input_sha256': sha256(self.source / 'inputs/input.jpg'),
                         'output_sha256': sha256(self.source / 'outputs/actual-output.png'),
                         'failures': [{'stage': 'narration', 'error': 'too long'}]}
        write_json(self.source / 'manifest.json', self.manifest)
        write_json(self.source / 'qa/manual-review.json', {'visual_review': 'old review'})
        write_json(self.local / 'latest-run.json', {'run': str(self.source)})
        for target in ('pc_demo.common.LOCAL', 'pc_demo.revisions.LOCAL',
                       'pc_demo.pipeline.LOCAL', 'pc_demo.history.LOCAL'):
            patcher = patch(target, self.local)
            patcher.start()
            self.addCleanup(patcher.stop)
        patcher = patch('pc_demo.pipeline.snapshot_source', return_value='test-commit')
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_revision_preserves_source_and_reuses_successful_inference_after_edit_failure(self):
        original = {str(p.relative_to(self.source)): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        self.story['segments'][0]['narration'] = 'New narration for the preserved app output.'
        custom = self.local / 'storyboard.local.json'
        write_json(custom, self.story)
        with patch('urllib.request.urlopen', side_effect=AssertionError('Unexpected download')), patch(
                'pc_demo.pipeline.execute', side_effect=AssertionError('Unexpected app execution')):
            run, manifest, _ = prepare_revision(self.source, custom)
        self.assertNotEqual(run, self.source)
        self.assertEqual(manifest['parent_run'], self.source.name)
        self.assertTrue(manifest['reused_inference'])
        self.assertEqual(manifest['inherited_failures'], self.manifest['failures'])
        self.assertEqual(manifest['failures'], [])
        self.assertFalse((run / 'qa/manual-review.json').exists())
        self.assertFalse((run / 'draft.mp4').exists())
        self.assertEqual(read_json(run / 'storyboard.json'), self.story)
        self.assertEqual(read_json(run / 'logs/inference.command.json'), self.command)
        self.assertEqual(read_json(run / 'evidence/inference/library.json'), {'original': True})
        for name, content in original.items():
            self.assertEqual((self.source / name).read_bytes(), content)

    def test_changed_app_output_is_rejected_without_creating_a_revision(self):
        (self.source / 'outputs/actual-output.png').write_bytes(b'substitute')
        with self.assertRaisesRegex(ValueError, 'Source integrity failure'):
            prepare_revision(self.source)
        self.assertEqual(list((self.local / 'runs').iterdir()), [self.source])

    def test_failed_inference_cannot_be_reused(self):
        self.command['returncode'] = 7
        write_json(self.source / 'logs/inference.command.json', self.command)
        with self.assertRaisesRegex(ValueError, 'successful inference'):
            prepare_revision(self.source)

    def test_invalid_storyboard_is_rejected_before_new_run(self):
        self.story['segments'][0]['start'] = 1
        path = self.local / 'bad-story.json'
        write_json(path, self.story)
        with self.assertRaisesRegex(ValueError, 'timing'):
            prepare_revision(self.source, path)
        self.assertEqual(list((self.local / 'runs').iterdir()), [self.source])

    def test_revision_of_revision_keeps_flat_original_evidence(self):
        first, _, _ = prepare_revision(self.source)
        second, manifest, _ = prepare_revision(first)
        self.assertEqual(manifest['parent_run'], first.name)
        self.assertEqual(manifest['inference_origin_run'], self.source.name)
        self.assertTrue((second / 'evidence/inference/library.json').is_file())
        self.assertFalse((second / 'evidence/inference/inference').exists())

    def test_render_failure_is_saved_without_moving_latest_pointer(self):
        pointer = (self.local / 'latest-run.json').read_bytes()
        with patch('pc_demo.pipeline.finish_draft', side_effect=RuntimeError('speech is too long')):
            with self.assertRaisesRegex(RuntimeError, 'speech is too long'):
                revise_demo(self.source)
        runs = [p for p in (self.local / 'runs').iterdir() if p != self.source]
        self.assertEqual(len(runs), 1)
        self.assertEqual(read_json(runs[0] / 'manifest.json')['status'], 'failed')
        self.assertIn('speech is too long', (runs[0] / 'logs/failure.txt').read_text())
        self.assertEqual((self.local / 'latest-run.json').read_bytes(), pointer)

    def test_history_shows_failures_and_survives_a_malformed_run(self):
        broken = self.local / 'runs/20261004-broken'
        broken.mkdir()
        write_json(broken / 'manifest.json', [])
        history = local_history()
        self.assertEqual(history['total_runs'], 2)
        self.assertEqual(history['runs'][0]['status'], 'unavailable or invalid')
        self.assertEqual(history['runs'][1]['status'], 'failed')
        self.assertIn('too long', format_history(history))
        self.assertEqual(local_history(limit=1)['shown'], 1)


class VerificationStateTests(unittest.TestCase):
    def test_a_failed_recheck_invalidates_old_pass_and_preserves_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = pathlib.Path(tmp)
            old = {'automated_pass': True, 'video_sha256': 'old'}
            write_json(run / 'qa/verification.json', old)
            with patch('pc_demo.verify._verify_run', side_effect=ValueError('changed input')):
                with self.assertRaisesRegex(ValueError, 'changed input'):
                    verify_run(run)
            record = read_json(run / 'qa/verification.json')
            self.assertFalse(record['automated_pass'])
            self.assertEqual(record['status'], 'failed')
            history = list((run / 'qa/verification-history').glob('*.json'))
            self.assertEqual(len(history), 1)
            self.assertEqual(read_json(history[0]), old)

    def test_changed_storyboard_invalidates_pass_even_when_video_is_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = pathlib.Path(tmp)
            for relative in VERIFIED_ARTIFACTS:
                path = run / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(relative.encode())
            video_hash = sha256(run / 'draft.mp4')
            write_json(run / 'manifest.json', {'status': 'automated_checks_passed',
                       'video_sha256': video_hash, 'input_sha256': sha256(run / 'inputs/input.jpg'),
                       'output_sha256': sha256(run / 'outputs/actual-output.png')})
            write_json(run / 'qa/verification.json', {'automated_pass': True, 'video_sha256': video_hash,
                       'checked_artifact_sha256': {name: sha256(run / name) for name in VERIFIED_ARTIFACTS}})
            self.assertTrue(draft_status(run)['automated_checks_passed'])
            (run / 'storyboard.json').write_bytes(b'changed narration')
            self.assertFalse(draft_status(run)['automated_checks_passed'])

    def test_empty_history_creates_no_local_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            local = pathlib.Path(tmp) / 'absent'
            with patch('pc_demo.history.LOCAL', local):
                self.assertEqual(local_history(), {'total_runs': 0, 'shown': 0, 'runs': []})
                with self.assertRaises(ValueError):
                    local_history(0)
            self.assertFalse(local.exists())


class PcGitBoundaryTests(unittest.TestCase):
    def test_windows_checkout_preserves_runtime_lock_checksum(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            repo = pathlib.Path(tmp) / 'source'
            (repo / 'pc_demo').mkdir(parents=True)
            (repo / '.gitattributes').write_bytes((root / '.gitattributes').read_bytes())
            original = b'{"reviewed_release": "pinned"}\n'
            (repo / 'pc_demo/runtime.lock.json').write_bytes(original)
            destination = pathlib.Path(tmp) / 'checkout'
            for args in (['init', '-q'], ['add', '.gitattributes', 'pc_demo/runtime.lock.json'],
                         ['checkout-index', '--all', '--prefix=' + destination.as_posix() + '/']):
                subprocess.run(['git', '-c', 'core.autocrlf=true', *args], cwd=repo,
                               capture_output=True, check=True)
            self.assertEqual((destination / 'pc_demo/runtime.lock.json').read_bytes(), original)

    def test_models_and_media_cannot_be_staged_as_pc_source(self):
        for name in ('pc_demo/.local/model.bin','pc_demo/model.safetensors','pc_demo/draft.mp4',
                     'pc_demo/token.local.json','pc_demo/.venv/pyvenv.cfg','pc_demo/tool.exe'):
            with self.subTest(name=name),self.assertRaises(ValueError):
                validate_index_entry(name,100)

    def test_reviewed_small_source_is_allowed_and_large_json_is_not(self):
        validate_index_entry('pc_demo/runtime.lock.json',1024)
        with self.assertRaisesRegex(ValueError,'large'):
            validate_index_entry('pc_demo/blob.json',2*1024*1024)


if __name__=='__main__':
    unittest.main()
