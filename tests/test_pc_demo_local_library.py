"""Local reference and setup-cache behavior; no network or app downloads."""
import copy
import pathlib
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.common import read_json, sha256, write_json
from pc_demo.library import archive_library
from pc_demo.setup_runtime import prepare_sources


class LocalLibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.run = self.root / 'new run'
        self.source = self.root / 'public/library.json'
        self.library = {'tools': [{'id': 'github:example/reviewed-app', 'versions': [{
            'kind': 'profile', 'date': '2026-10-03', 'edition_id': '2026-10-03',
            'profile': {field: 'Reviewed reference text' for field in
                        ('introduction', 'installation', 'usage', 'requirements', 'license', 'limitations', 'sources')}
        }]}]}
        write_json(self.source, self.library)
        patcher = patch('pc_demo.library.ROOT', self.root / 'pc_demo')
        patcher.start()
        self.addCleanup(patcher.stop)
        network = patch('urllib.request.urlopen', side_effect=AssertionError('No network permitted'))
        network.start()
        self.addCleanup(network.stop)

    def test_default_uses_local_bytes_and_discloses_snapshot_freshness(self):
        raw = b'\xef\xbb\xbf' + self.source.read_bytes()
        self.source.write_bytes(raw)
        result = archive_library(self.run, 'github:example/reviewed-app')
        self.assertEqual((self.run / 'evidence/library.json').read_bytes(), raw)
        self.assertEqual(result['library_sha256'], sha256(self.source))
        self.assertEqual(result['profile_edition'], '2026-10-03')
        self.assertEqual(result['library_access']['network_requests'], 0)
        self.assertIn('no live freshness', result['library_access']['freshness'])
        self.assertEqual(read_json(self.run / 'evidence/library-origin.json'), result['library_access'])
        self.source.write_bytes(b'new local edition')
        self.assertEqual((self.run / 'evidence/library.json').read_bytes(), raw)

    def test_explicit_local_file_preserves_the_repository_library(self):
        original = self.source.read_bytes()
        supplied = self.root / 'Mac export/library.json'
        self.library['tools'][0]['versions'][0]['edition_id'] = '2026-10-20-update-01'
        write_json(supplied, self.library)
        result = archive_library(self.run, 'github:example/reviewed-app', supplied)
        self.assertEqual(result['profile_edition'], '2026-10-20-update-01')
        self.assertEqual(result['library_source'], str(supplied.resolve()))
        self.assertEqual((self.run / 'evidence/library.json').read_bytes(), supplied.read_bytes())
        self.assertEqual(self.source.read_bytes(), original)

    def test_missing_snapshot_does_not_download_a_replacement(self):
        with self.assertRaisesRegex(ValueError, 'demos do not download'):
            archive_library(self.run, 'github:example/reviewed-app', self.root / 'absent.json')
        self.assertFalse(self.run.exists())

    def test_invalid_json_is_retained_as_failure_evidence(self):
        self.source.write_bytes(b'not JSON')
        with self.assertRaises(ValueError):
            archive_library(self.run, 'github:example/reviewed-app')
        self.assertEqual((self.run / 'evidence/library.json').read_bytes(), b'not JSON')
        self.assertFalse((self.run / 'evidence/selected-profile.json').exists())

    def test_invalid_profiles_cannot_authorize_execution(self):
        version = self.library['tools'][0]['versions'][0]
        cases = [[], {'tools': [None]}, {'tools': []},
                 {'tools': [{'id': 'github:example/reviewed-app', 'versions': [{**version, 'kind': 'screened'}]}]},
                 {'tools': [{'id': 'github:example/reviewed-app', 'versions': [{**version, 'profile': {}}]}]},
                 {'tools': self.library['tools'] * 2}]
        for index, library in enumerate(cases):
            write_json(self.source, library)
            with self.subTest(library=library), self.assertRaises(ValueError):
                archive_library(self.root / str(index), 'github:example/reviewed-app')

    def test_snapshot_limit_and_existing_evidence_are_protected(self):
        with patch('pc_demo.library.MAX_LIBRARY_BYTES', 8):
            with self.assertRaisesRegex(ValueError, 'snapshot limit'):
                archive_library(self.run, 'github:example/reviewed-app')
        self.assertFalse(self.run.exists())
        archive_library(self.run, 'github:example/reviewed-app')
        first = (self.run / 'evidence/library.json').read_bytes()
        with self.assertRaises(FileExistsError):
            archive_library(self.run, 'github:example/reviewed-app')
        self.assertEqual((self.run / 'evidence/library.json').read_bytes(), first)


class SetupSourceCacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.local = self.root / '.local'
        self.source = {'name': 'reviewed-license.txt', 'url': 'https://example.invalid/pinned/LICENSE'}
        self.lock = {'sources': [self.source]}
        write_json(self.root / 'runtime.lock.json', self.lock)
        self.path = self.local / 'sources' / self.source['name']
        self.path.parent.mkdir(parents=True)
        self.path.write_bytes(b'reviewed terms')
        self.receipt = {'runtime_lock_sha256': sha256(self.root / 'runtime.lock.json'),
                        'sources': [{**self.source, 'sha256': sha256(self.path)}]}
        write_json(self.local / 'setup.json', self.receipt)
        for name, value in (('ROOT', self.root), ('LOCAL', self.local)):
            patcher = patch('pc_demo.setup_runtime.' + name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_matching_reviewed_source_reuses_without_download_or_receipt_mutation(self):
        receipt = (self.local / 'setup.json').read_bytes()
        with patch('pc_demo.setup_runtime.download', side_effect=AssertionError('Unexpected download')):
            sources = prepare_sources(self.lock)
        self.assertTrue(sources[0]['reused_verified_copy'])
        self.assertEqual(sources[0]['sha256'], sha256(self.path))
        self.assertEqual((self.local / 'setup.json').read_bytes(), receipt)

    def test_missing_or_changed_cached_bytes_require_a_new_source_read(self):
        def download(url, target):
            self.assertEqual(url, self.source['url'])
            target.write_bytes(b'fresh official response')
            return target
        for exists in (True, False):
            if exists:
                self.path.write_bytes(b'changed local file')
            else:
                self.path.unlink()
            with self.subTest(exists=exists), patch('pc_demo.setup_runtime.download', side_effect=download) as fetch:
                sources = prepare_sources(self.lock)
            fetch.assert_called_once()
            self.assertFalse(sources[0]['reused_verified_copy'])
            self.assertEqual(sources[0]['sha256'], sha256(self.path))

    def test_wrong_lock_url_or_receipt_structure_cannot_reuse_source(self):
        wrong_url = copy.deepcopy(self.receipt)
        wrong_url['sources'][0]['url'] += '?different'
        duplicated = copy.deepcopy(self.receipt)
        duplicated['sources'] *= 2
        cases = [wrong_url, duplicated, [], {},
                 {**self.receipt, 'runtime_lock_sha256': 'changed'},
                 {**self.receipt, 'sources': 'invalid'}]
        for record in cases:
            write_json(self.local / 'setup.json', record)
            with self.subTest(record=record), patch('pc_demo.setup_runtime.download', return_value=self.path) as fetch:
                self.assertFalse(prepare_sources(self.lock)[0]['reused_verified_copy'])
            fetch.assert_called_once_with(self.source['url'], self.path)
        (self.local / 'setup.json').write_text('invalid JSON')
        with patch('pc_demo.setup_runtime.download', return_value=self.path) as fetch:
            self.assertFalse(prepare_sources(self.lock)[0]['reused_verified_copy'])
        fetch.assert_called_once()


try:
    from PIL import Image
except ImportError:
    Image = None


@unittest.skipIf(Image is None, 'Pipeline entry requires the existing PC Pillow dependency')
class PipelineLocalLibraryTests(unittest.TestCase):
    def test_invalid_library_fails_before_artwork_or_inference_and_retains_run(self):
        from pc_demo.pipeline import run_demo
        with tempfile.TemporaryDirectory() as tmp:
            local = pathlib.Path(tmp)
            source = local / 'invalid library.json'
            source.write_text('{}')
            with patch('pc_demo.pipeline.LOCAL', local), patch('pc_demo.pipeline.verified_runtime', return_value=(None, {})), patch(
                    'pc_demo.pipeline.execute', side_effect=AssertionError('App must not run')), patch(
                    'urllib.request.urlopen', side_effect=AssertionError('No network permitted')):
                with self.assertRaisesRegex(ValueError, 'tools array'):
                    run_demo(library_file=source)
            run, = (local / 'runs').iterdir()
            self.assertEqual(read_json(run / 'manifest.json')['status'], 'failed')
            self.assertEqual(list((run / 'inputs').iterdir()), [])
            self.assertEqual((run / 'evidence/library.json').read_bytes(), source.read_bytes())
            self.assertTrue((run / 'logs/failure.txt').is_file())
