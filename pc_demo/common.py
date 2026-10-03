import hashlib
import json
import pathlib
import subprocess
import time
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent
LOCAL = ROOT / '.local'


def read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, value):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def sha256(path):
    with pathlib.Path(path).open('rb') as stream:
        digest = hashlib.sha256()
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def download(url, target, expected=None):
    """Pinned HTTPS downloads; atomic replacement, never execute remote text."""
    if not url.startswith('https://'):
        raise ValueError('Only HTTPS sources are allowed')
    target = pathlib.Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and expected and sha256(target) == expected:
        return target
    partial = target.with_suffix(target.suffix + '.partial')
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Media-Scout-PC/0.1'})
    with urllib.request.urlopen(req, timeout=120) as response, partial.open('wb') as out:
        if not response.url.startswith('https://'):
            raise ValueError('Download redirected away from HTTPS')
        for chunk in iter(lambda: response.read(1024 * 1024), b''):
            out.write(chunk)
    if expected and sha256(partial) != expected:
        raise ValueError(f'Checksum mismatch: {target.name}; partial retained for inspection')
    partial.replace(target)
    return target


def execute(args, directory, label, timeout=300, cwd=None):
    """Always keep command evidence, including exceptions and timeouts."""
    directory = pathlib.Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    metadata = {'argv': [str(x) for x in args], 'started_utc': stamp(), 'cwd': str(cwd or ROOT.parent)}
    start = time.perf_counter()
    try:
        with (directory / f'{label}.stdout.log').open('wb') as stdout, (directory / f'{label}.stderr.log').open('wb') as stderr:
            result = subprocess.run(metadata['argv'], cwd=cwd or ROOT.parent, stdout=stdout,
                                    stderr=stderr, timeout=timeout, check=False)
        metadata['returncode'] = result.returncode
        if result.returncode:
            raise RuntimeError(f'{label} failed with exit code {result.returncode}; see {directory}')
    except Exception as error:
        metadata['error'] = str(error)
        raise
    finally:
        metadata['elapsed_seconds'] = round(time.perf_counter() - start, 3)
        metadata['finished_utc'] = stamp()
        write_json(directory / f'{label}.command.json', metadata)
    return metadata


def checked_run_path(value):
    path = pathlib.Path(value).resolve()
    if not path.is_relative_to((LOCAL / 'runs').resolve()) or not path.is_dir():
        raise ValueError('Run must be an existing directory inside pc_demo/.local/runs')
    return path


def select_profile(library, tool_id):
    matches = [t for t in library['tools'] if t['id'] == tool_id]
    if len(matches) != 1:
        raise ValueError('Selected tool is absent or duplicated in the library')
    versions = [v for v in matches[0]['versions'] if v['kind'] == 'profile']
    if not versions:
        raise ValueError('Selected tool has no complete profile')
    profile = versions[0]['profile']
    required = ('introduction', 'installation', 'usage', 'requirements', 'license', 'limitations', 'sources')
    if any(not profile.get(field) for field in required):
        raise ValueError('Selected profile is missing required sections')
    return versions[0]
