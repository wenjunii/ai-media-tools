"""Offline readiness checks. No downloads, app execution, synthesis or repairs."""
import os
import pathlib
import platform
import shutil
import sys
from .common import ROOT, LOCAL, read_json, sha256, stamp
from .inputs import load_custom_input
from .library import inspect_library
from .setup_runtime import verified_runtime
from .storyboard import load_storyboard

MIN_FREE_BYTES = 2 * 1024**3  # Wrapper policy, not an upstream hardware minimum.
NOT_TESTED = [
    'Vulkan device availability, GPU selection and successful inference',
    'Installed speech voices, spoken duration and subjective listening quality',
    'Media-tool execution, final video decode and creator approval',
]
CHECK_ERRORS = (OSError, ValueError, RuntimeError, KeyError, TypeError, AttributeError, ImportError)


def check(name, operation, fix):
    try:
        return {'name': name, 'passed': True, 'details': operation()}
    except Exception as error:
        # Decoder-specific errors are blockers too; diagnostics must fail closed.
        return {'name': name, 'passed': False, 'error': str(error), 'fix': fix}


def report(checks):
    return {'schema_version': 1, 'checked_utc': stamp(),
            'passed': all(item['passed'] for item in checks), 'checks': checks,
            'mode': 'local files only; no downloads or app execution',
            'not_tested': NOT_TESTED, 'social_publishing_enabled': False,
            'schedule_enabled': False}


def environment():
    import PIL
    lock = read_json(ROOT / 'runtime.lock.json')
    if (os.name != 'nt' or platform.python_implementation() != 'CPython'
            or sys.version_info[:2] != (3, 10) or sys.maxsize <= 2**32
            or platform.machine().lower() not in ('amd64', 'x86_64')):
        raise ValueError('Production requires Windows CPython 3.10 x64')
    if PIL.__version__ != lock['pillow']['version']:
        raise ValueError(f'Pillow must match the reviewed version {lock["pillow"]["version"]}')
    if pathlib.Path(sys.prefix).resolve() != (LOCAL / 'venv').resolve():
        raise ValueError('Use the isolated pc_demo/.local/venv Python through demo.ps1')
    return {'python': sys.version.split()[0], 'pillow': PIL.__version__}


def media_tool(name, receipt):
    entry = receipt['hardware']['media_tools'][name]
    path = pathlib.Path(entry['path'])
    if sha256(path) != entry['sha256']:
        raise ValueError(f'{name} changed since setup; review the dependency before recording a new setup')
    return {'path': str(path), 'sha256': entry['sha256']}


def powershell():
    path = shutil.which('powershell.exe')
    if not path:
        raise ValueError('Narration requires Windows PowerShell on PATH')
    return {'path': path, 'speech_voice': 'not tested until narration'}


def storage():
    # A fresh checkout need not have .local yet. Query its nearest existing parent.
    path = LOCAL
    while not path.exists() and path != path.parent:
        path = path.parent
    free = shutil.disk_usage(path).free
    if free < MIN_FREE_BYTES:
        raise ValueError(f'Only {free / 1024**3:.2f} GiB free; the demo wrapper requires at least 2 GiB')
    return {'free_bytes': free, 'minimum_free_bytes': MIN_FREE_BYTES,
            'policy': 'Workspace reserve; not a guarantee of enough space for every run'}


def source_evidence(receipt):
    lock = read_json(ROOT / 'runtime.lock.json')
    if receipt['runtime_lock_sha256'] != sha256(ROOT / 'runtime.lock.json'):
        raise ValueError('Reviewed source receipt belongs to a different runtime lock')
    saved = receipt['sources']
    if not isinstance(saved, list) or len(saved) != len(lock['sources']):
        raise ValueError('Reviewed source receipt is incomplete')
    for source in lock['sources']:
        matches = [entry for entry in saved if isinstance(entry, dict)
                   and entry.get('name') == source['name'] and entry.get('url') == source['url']]
        if len(matches) != 1 or sha256(LOCAL / 'sources' / source['name']) != matches[0].get('sha256'):
            raise ValueError(f'Reviewed source is missing or changed: {source["name"]}')
    return {'documents_checked': len(saved)}


def storyboard_check(story):
    from .render import validate_layout
    return validate_layout(story)


def production_checks(story, receipt, include_sources=False):
    """Shared by preflight, new inference and editorial revisions."""
    checks = [
        check('python_environment', environment, 'Run setup with Windows CPython 3.10 x64, then use demo.ps1.'),
        check('ffmpeg', lambda: media_tool('ffmpeg', receipt), 'Restore the recorded media tool or review it and rerun setup.'),
        check('ffprobe', lambda: media_tool('ffprobe', receipt), 'Restore the recorded media tool or review it and rerun setup.'),
        check('powershell', powershell, 'Use Windows PowerShell for local narration.'),
        check('workspace_storage', storage, 'Free space or move the local checkout; runs are never deleted automatically.'),
    ]
    if story is not None:
        checks.insert(4, check('storyboard_layout', lambda: storyboard_check(story),
                              'Shorten the named line or restore the required Segoe UI/Consolas fonts; keep the six-scene template.'))
    if include_sources:
        checks.append(check('reviewed_sources', lambda: source_evidence(receipt),
                            'Run explicit setup to recover reviewed official source evidence.'))
    return checks


def require_pass(result):
    failures = [item for item in result['checks'] if not item['passed']]
    if failures:
        raise ValueError('Preflight failed: ' + '; '.join(
            f'{item["name"]}: {item["error"]}. {item["fix"]}' for item in failures))


def inspect_preflight(storyboard=None, input_image=None, library_file=None):
    """Aggregate independent blockers without creating or changing any run."""
    checks = []
    receipt, story = {}, None
    try:
        # Keep dependency diagnostics useful even when installed app hashes fail.
        receipt = read_json(LOCAL / 'setup.json')
    except CHECK_ERRORS:
        pass

    def runtime():
        app, _ = verified_runtime()
        return {'path': str(app), 'integrity': 'App/model files match the saved setup hashes'}

    checks.append(check('installed_runtime', runtime, 'Run explicit setup to install or repair the reviewed runtime.'))
    story_path = pathlib.Path(storyboard) if storyboard else ROOT / (
        'storyboard-artwork.json' if input_image else 'storyboard.json')
    try:
        story = load_storyboard(story_path)
    except CHECK_ERRORS as error:
        checks.append({'name': 'storyboard_file', 'passed': False, 'error': str(error),
                       'fix': 'Choose a valid local storyboard using the supported six-scene template.'})
    checks += production_checks(story, receipt, include_sources=True)

    def artwork():
        if input_image is None:
            return {'kind': 'controlled illustration', 'input_size': [256, 256]}
        _, _, details = load_custom_input(input_image)
        return {'kind': 'custom artwork', 'input_size': details['input_size'],
                'source_sha256': details['sha256'], 'normalization': details['normalization']}

    checks.append(check('input_artwork', artwork, 'Choose an opaque PNG/JPEG, 64-1024 pixels per side and at most 20 MiB.'))
    checks.append(check('library_profile', lambda: inspect_library(
        read_json(ROOT / 'runtime.lock.json')['app']['library_id'], library_file),
        'Choose a local library snapshot containing the complete reviewed Real-ESRGAN profile.'))
    return report(checks)


def format_preflight(result):
    lines = ['Preflight ' + ('passed' if result['passed'] else 'blocked') + ' (local checks only).']
    for item in result['checks']:
        if item['passed']:
            detail = item.get('details', {})
            suffix = f' - profile edition {detail["profile_edition"]}; no live freshness check' if 'profile_edition' in detail else ''
            lines.append(f'PASS {item["name"]}{suffix}')
        else:
            lines.append(f'FAIL {item["name"]}: {item["error"]}\n  Fix: {item["fix"]}')
    lines.append('Not tested: ' + '; '.join(result['not_tested']) + '.')
    return '\n'.join(lines)
