import os
import platform
import shutil
import sys
import venv
import zipfile
from .common import ROOT, LOCAL, download, execute, read_json, sha256, stamp, write_json


def doctor():
    LOCAL.mkdir(parents=True, exist_ok=True)
    ps = shutil.which('powershell.exe')
    if not ps:
        raise RuntimeError('This MVP requires Windows PowerShell and CPython 3.10 x64')
    execute([ps, '-NoProfile', '-File', ROOT / 'hardware.ps1'], LOCAL / 'logs', 'hardware')
    inventory = read_json(LOCAL / 'logs/hardware.stdout.log')
    inventory['python'] = {'version': sys.version, 'executable': sys.executable}
    inventory['media_tools'] = {}
    for name in ('ffmpeg', 'ffprobe'):
        path = shutil.which(name)
        if not path:
            raise RuntimeError(f'{name} must be available on PATH; no global installer is run')
        execute([path, '-version'], LOCAL / 'logs', name + '-version')
        inventory['media_tools'][name] = {
            'path': path, 'sha256': sha256(path),
            'version': (LOCAL / f'logs/{name}-version.stdout.log').read_text(encoding='utf-8', errors='replace').splitlines()[0],
        }
    write_json(LOCAL / 'hardware.json', inventory)
    return inventory


def setup():
    if os.name != 'nt' or sys.version_info[:2] != (3, 10) or platform.machine().lower() not in ('amd64', 'x86_64'):
        raise RuntimeError('Pinned wheel requires CPython 3.10 x64 on Windows')
    lock = read_json(ROOT / 'runtime.lock.json')
    hardware = doctor()
    if shutil.disk_usage(LOCAL).free < 2 * 1024**3:
        raise RuntimeError('At least 2 GiB free workspace storage required for this demo')
    cached = LOCAL / 'downloads/portable-windows.zip'
    reviewed = LOCAL / 'review/portable-windows.zip'
    if not cached.exists() and reviewed.exists() and sha256(reviewed) == lock['app']['sha256']:
        cached.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(reviewed, cached)
    download(lock['app']['url'], cached, lock['app']['sha256'])
    app = LOCAL / 'apps/realesrgan-20220424'
    app.mkdir(parents=True, exist_ok=True)
    files = {}
    with zipfile.ZipFile(cached) as archive:
        for name in lock['app']['extract']:
            target = app / name
            if not target.resolve().is_relative_to(app.resolve()):
                raise ValueError('Unsafe archive path')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(name))
            files[name] = sha256(target)
    sources = []
    for source in lock['sources']:
        path = download(source['url'], LOCAL / 'sources' / source['name'])
        sources.append({**source, 'sha256': sha256(path)})
    wheel = lock['pillow']
    download(wheel['url'], LOCAL / 'downloads' / wheel['filename'], wheel['sha256'])
    env = LOCAL / 'venv'
    if not (env / 'Scripts/python.exe').exists():
        venv.EnvBuilder(with_pip=True).create(env)
    python = env / 'Scripts/python.exe'
    execute([python, '-m', 'pip', 'install', '--no-index', '--no-deps', '--disable-pip-version-check',
             LOCAL / 'downloads' / wheel['filename']], LOCAL / 'logs', 'pillow-install')
    execute([python, '-m', 'pip', 'freeze', '--all'], LOCAL / 'logs', 'environment-freeze')
    receipt = {'created_utc': stamp(), 'runtime_lock_sha256': sha256(ROOT / 'runtime.lock.json'),
               'app': str(app), 'files': files, 'sources': sources, 'hardware': hardware,
               'isolation': 'Portable app and Python venv; not a security sandbox'}
    write_json(LOCAL / 'setup.json', receipt)
    print('Setup complete. App, model, wheel and receipts are local and ignored.', flush=True)


def verified_runtime():
    receipt = read_json(LOCAL / 'setup.json')
    lock = read_json(ROOT / 'runtime.lock.json')
    if sha256(ROOT / 'runtime.lock.json') != receipt['runtime_lock_sha256']:
        raise RuntimeError('Runtime lock changed; run setup again')
    if not isinstance(receipt.get('files'), dict) or set(receipt['files']) != set(lock['app']['extract']):
        raise RuntimeError('Setup receipt is missing required app/model files; run setup again')
    app = LOCAL / 'apps/realesrgan-20220424'
    for name, digest in receipt['files'].items():
        if sha256(app / name) != digest:
            raise RuntimeError(f'Installed app integrity failure: {name}')
    return app, receipt
