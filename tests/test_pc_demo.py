"""PC guardrails only: no app downloads, inference, credentials or media in CI."""
import hashlib
import io
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.audit import validate_index_entry
from pc_demo.common import download, execute, read_json, resolve_run, select_profile, sha256, write_json
from pc_demo.setup_runtime import verified_runtime
from pc_demo.status import local_status, review_state


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


class PcGitBoundaryTests(unittest.TestCase):
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
