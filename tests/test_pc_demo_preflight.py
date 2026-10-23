"""Readiness and early failure checks, with no real app or network in tests."""
import contextlib
import copy
import io
import os
import pathlib
import shutil
import struct
import sys
import tempfile
import unittest
import zlib
from unittest.mock import patch
from pc_demo.common import read_json, sha256, write_json
from pc_demo.library import inspect_library
from pc_demo.preflight import inspect_preflight, format_preflight, require_pass, MIN_FREE_BYTES

try:
    from PIL import Image
except ImportError:
    Image = None

PROJECT = pathlib.Path(__file__).resolve().parents[1]


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name) / 'pc_demo'
        self.local = self.root / '.local'
        self.root.mkdir()
        self.story = read_json(PROJECT / 'pc_demo/storyboard.json')
        for name in ('storyboard.json', 'storyboard-artwork.json'):
            write_json(self.root / name, self.story)
        self.lock = {'app': {'library_id': 'github:xinntao/real-esrgan', 'extract': ['tool.exe', 'model.bin']},
                     'pillow': {'version': '11.3.0'},
                     'sources': [{'name': 'license.txt', 'url': 'https://example.invalid/LICENSE'}]}
        write_json(self.root / 'runtime.lock.json', self.lock)
        app = self.local / 'apps/realesrgan-20220424'
        app.mkdir(parents=True)
        for name in self.lock['app']['extract']:
            (app / name).write_bytes(b'synthetic fixture, never executable')
        sources = self.local / 'sources'
        sources.mkdir()
        (sources / 'license.txt').write_bytes(b'synthetic license fixture')
        media = {}
        for name in ('ffmpeg', 'ffprobe'):
            path = self.local / (name + '.exe')
            path.write_bytes(b'synthetic media tool, never executable')
            media[name] = {'path': str(path), 'sha256': sha256(path)}
        self.receipt = {'files': {name: sha256(app / name) for name in self.lock['app']['extract']},
                        'runtime_lock_sha256': sha256(self.root / 'runtime.lock.json'),
                        'sources': [{**self.lock['sources'][0], 'sha256': sha256(sources / 'license.txt')}],
                        'hardware': {'media_tools': media}}
        write_json(self.local / 'setup.json', self.receipt)
        self.library = {'tools': [{'id': 'github:xinntao/real-esrgan', 'versions': [{
            'kind': 'profile', 'edition_id': '2026-10-01-r2',
            'profile': {field: 'fixture evidence' for field in
                        ('introduction', 'installation', 'usage', 'requirements', 'license', 'limitations', 'sources')}
        }]}]}
        write_json(self.root.parent / 'public/library.json', self.library)
        patches = {
            'pc_demo.preflight.ROOT': self.root, 'pc_demo.preflight.LOCAL': self.local,
            'pc_demo.setup_runtime.ROOT': self.root, 'pc_demo.setup_runtime.LOCAL': self.local,
            'pc_demo.library.ROOT': self.root,
        }
        for target, value in patches.items():
            patcher = patch(target, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        for target, result in (
            ('pc_demo.preflight.environment', {'python': 'fixture'}),
            ('pc_demo.preflight.powershell', {'path': 'fixture'}),
            ('pc_demo.preflight.storyboard_check', {'scenes': 6}),
            ('pc_demo.preflight.shutil.disk_usage', shutil._ntuple_diskusage(10 * MIN_FREE_BYTES, 0, 10 * MIN_FREE_BYTES)),
        ):
            patcher = patch(target, return_value=result)
            patcher.start()
            self.addCleanup(patcher.stop)
        for target in ('urllib.request.urlopen', 'subprocess.run', 'subprocess.Popen'):
            patcher = patch(target, side_effect=AssertionError('Preflight must not fetch or execute'))
            patcher.start()
            self.addCleanup(patcher.stop)

    def snapshot(self):
        return {str(p.relative_to(self.root.parent)): p.read_bytes()
                for p in self.root.parent.rglob('*') if p.is_file()}

    def test_readiness_preserves_all_files_without_creating_runs_or_requesting_network(self):
        before = self.snapshot()
        result = inspect_preflight()
        self.assertTrue(result['passed'], result)
        self.assertEqual(before, self.snapshot())
        self.assertFalse((self.local / 'runs').exists())
        self.assertIn('2026-10-01-r2', format_preflight(result))
        self.assertIn('no live freshness check', format_preflight(result))
        self.assertIn('Vulkan', ' '.join(result['not_tested']))
        require_pass(result)

    def test_independent_failures_are_all_reported_and_no_repairs_happen(self):
        (self.local / 'ffprobe.exe').write_bytes(b'changed dependency')
        (self.local / 'sources/license.txt').unlink()
        (self.root.parent / 'public/library.json').write_bytes(b'invalid JSON')
        before = self.snapshot()
        with patch('pc_demo.preflight.shutil.disk_usage', return_value=shutil._ntuple_diskusage(100, 99, 1)):
            result = inspect_preflight(input_image=self.local / 'absent.png')
        failures = {item['name'] for item in result['checks'] if not item['passed']}
        self.assertEqual(failures, {'ffprobe', 'reviewed_sources', 'library_profile', 'workspace_storage', 'input_artwork'})
        self.assertFalse(result['passed'])
        self.assertEqual(before, self.snapshot())
        with self.assertRaisesRegex(ValueError, 'Preflight failed:'):
            require_pass(result)
        self.assertIn('Fix:', format_preflight(result))

    def test_corrupt_app_and_missing_receipt_do_not_hide_other_checks(self):
        (self.local / 'apps/realesrgan-20220424/model.bin').write_bytes(b'changed model')
        result = inspect_preflight()
        self.assertEqual([item['name'] for item in result['checks'] if not item['passed']], ['installed_runtime'])
        (self.local / 'setup.json').unlink()
        result = inspect_preflight()
        passed = {item['name'] for item in result['checks'] if item['passed']}
        self.assertIn('library_profile', passed)
        self.assertIn('workspace_storage', passed)
        self.assertFalse(result['passed'])

    def test_source_url_change_is_detected_even_when_bytes_still_match(self):
        self.receipt['sources'][0]['url'] += '/changed'
        write_json(self.local / 'setup.json', self.receipt)
        result = inspect_preflight()
        self.assertEqual([item['name'] for item in result['checks'] if not item['passed']], ['reviewed_sources'])

    def test_explicit_snapshot_is_read_only_and_malformed_profiles_are_explained(self):
        alternate = self.local / 'reference with spaces.json'
        altered = copy.deepcopy(self.library)
        altered['tools'][0]['versions'][0]['edition_id'] = '2026-10-23'
        write_json(alternate, altered)
        before = self.snapshot()
        result = inspect_preflight(library_file=alternate)
        self.assertTrue(result['passed'])
        self.assertIn('2026-10-23', format_preflight(result))
        self.assertEqual(before, self.snapshot())
        altered['tools'][0]['versions'][0]['profile'] = []
        write_json(alternate, altered)
        with self.assertRaisesRegex(ValueError, 'invalid profile structure'):
            inspect_library('github:xinntao/real-esrgan', alternate)

    def test_invalid_storyboard_file_has_an_actionable_blocker(self):
        bad = self.local / 'missing-story.json'
        result = inspect_preflight(storyboard=bad)
        item = next(item for item in result['checks'] if item['name'] == 'storyboard_file')
        self.assertFalse(item['passed'])
        self.assertIn('local storyboard', item['fix'])

    @unittest.skipIf(Image is None, 'Image decoding requires Pillow')
    def test_oversized_png_header_is_reported_without_allocating_or_creating_a_run(self):
        stream = io.BytesIO()
        Image.new('RGB', (64, 64), 'red').save(stream, format='PNG')
        raw = bytearray(stream.getvalue())
        raw[16:24] = struct.pack('>II', 30000, 30000)
        raw[29:33] = struct.pack('>I', zlib.crc32(raw[12:29]))
        source = self.local / 'oversized-header.png'
        source.write_bytes(raw)
        result = inspect_preflight(input_image=source)
        failures = [item for item in result['checks'] if not item['passed']]
        self.assertEqual([item['name'] for item in failures], ['input_artwork'])
        self.assertIn('decompression bomb', failures[0]['error'].lower())
        self.assertFalse((self.local / 'runs').exists())

    @unittest.skipIf(Image is None, 'Pipeline entry needs the reviewed Pillow dependency')
    def test_changed_ffprobe_blocks_before_gpu_and_preserves_failure_and_latest_draft(self):
        from pc_demo.pipeline import run_demo
        source = self.local / 'input.png'
        Image.new('RGB', (64, 64), 'red').save(source)
        write_json(self.local / 'latest-run.json', {'run': 'existing draft'})
        pointer = (self.local / 'latest-run.json').read_bytes()
        (self.local / 'ffprobe.exe').write_bytes(b'changed dependency')
        with patch('pc_demo.pipeline.LOCAL', self.local), patch('pc_demo.pipeline.execute',
                side_effect=AssertionError('GPU must not run')):
            with self.assertRaisesRegex(ValueError, 'Preflight failed: ffprobe'):
                run_demo(input_image=source)
        run, = (self.local / 'runs').iterdir()
        self.assertEqual(read_json(run / 'manifest.json')['status'], 'failed')
        self.assertFalse(read_json(run / 'qa/preflight.json')['passed'])
        self.assertEqual((run / 'inputs/source.png').read_bytes(), source.read_bytes())
        self.assertTrue((run / 'storyboard.json').is_file())
        self.assertTrue((run / 'logs/failure.txt').is_file())
        self.assertFalse((run / 'logs/inference.command.json').exists())
        self.assertEqual((self.local / 'latest-run.json').read_bytes(), pointer)

    def test_revision_dependency_failure_happens_before_narration_and_records_check(self):
        from pc_demo.pipeline import finish_draft
        run = self.local / 'revision'
        write_json(run / 'storyboard.json', self.story)
        (self.local / 'ffmpeg.exe').unlink()
        with patch('pc_demo.pipeline.execute', side_effect=AssertionError('Narration must not run')):
            with self.assertRaisesRegex(ValueError, 'Preflight failed: ffmpeg'):
                finish_draft(run, {}, self.receipt)
        self.assertFalse(read_json(run / 'qa/render-preflight.json')['passed'])

    def test_cli_json_uses_nonzero_exit_when_blocked(self):
        from pc_demo.__main__ import main
        (self.local / 'setup.json').unlink()
        with patch.object(sys, 'argv', ['pc_demo', 'preflight', '--json']), contextlib.redirect_stdout(io.StringIO()) as stdout:
            with self.assertRaises(SystemExit) as error:
                main()
        self.assertEqual(error.exception.code, 2)
        self.assertIn('"passed": false', stdout.getvalue())


@unittest.skipUnless(os.name == 'nt' and Image is not None, 'Layout measures the production Windows fonts')
class WindowsLayoutTests(unittest.TestCase):
    def test_both_templates_fit_and_long_lines_name_the_scene_and_field(self):
        from pc_demo.render import validate_layout
        for filename in ('storyboard.json', 'storyboard-artwork.json'):
            story = read_json(PROJECT / 'pc_demo' / filename)
            self.assertEqual(validate_layout(story)['scenes'], 6)
        for field in ('title', 'caption', 'eyebrow'):
            story = read_json(PROJECT / 'pc_demo/storyboard.json')
            story['segments'][1][field] = 'W' * 80 if field == 'eyebrow' else ['W' * 80]
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'Scene 2 ' + field + ' exceeds safe width'):
                validate_layout(story)

    def test_missing_font_is_a_failed_layout_check(self):
        from pc_demo.preflight import check, storyboard_check
        with patch('pc_demo.render.font', side_effect=OSError('cannot open font resource')):
            result = check('storyboard_layout', lambda: storyboard_check(read_json(PROJECT / 'pc_demo/storyboard.json')), 'Restore fonts.')
        self.assertFalse(result['passed'])
        self.assertIn('font resource', result['error'])
