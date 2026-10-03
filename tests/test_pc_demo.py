"""PC guardrails only: no app downloads, inference, credentials or media in CI."""
import hashlib
import io
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.audit import validate_index_entry
from pc_demo.common import download, execute, read_json, select_profile


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
