"""Archive local research references without contacting GitHub or other hosts."""
import json
import pathlib
from .common import ROOT, select_profile, sha256, stamp, write_json

MAX_LIBRARY_BYTES = 64 * 1024 * 1024


def archive_library(run, tool_id, source=None):
    path = pathlib.Path(source).resolve() if source is not None else ROOT.parent / 'public/library.json'
    try:
        with path.open('rb') as stream:
            raw = stream.read(MAX_LIBRARY_BYTES + 1)
    except OSError as error:
        raise ValueError('Cannot read the local library snapshot. Sync it when needed or pass '
                         '-LibraryFile with a local JSON file; demos do not download the library.') from error
    if len(raw) > MAX_LIBRARY_BYTES:
        raise ValueError('Local library exceeds the 64 MiB snapshot limit')
    evidence = run / 'evidence'
    evidence.mkdir(parents=True, exist_ok=True)
    # Preserve supplied bytes, including an invalid JSON file, in this new run.
    snapshot = evidence / 'library.json'
    with snapshot.open('xb') as stream:
        stream.write(raw)
    origin = {'mode': 'local_snapshot', 'source': str(path), 'captured_utc': stamp(),
              'sha256': sha256(snapshot), 'bytes': len(raw), 'network_requests': 0,
              'freshness': 'Saved local snapshot; no live freshness check was performed'}
    write_json(evidence / 'library-origin.json', origin)
    try:
        library = json.loads(raw.decode('utf-8-sig'))
        if not isinstance(library, dict) or not isinstance(library.get('tools'), list):
            raise ValueError('Local library must contain a tools array')
        version = select_profile(library, tool_id)
        edition = version.get('edition_id') or version['date']
        if not isinstance(edition, str) or not edition:
            raise ValueError('Selected profile must identify its edition')
    except (KeyError, TypeError, UnicodeError) as error:
        raise ValueError('Local library has an invalid profile structure or encoding') from error
    write_json(evidence / 'selected-profile.json', version)
    return {'library_source': str(path), 'library_sha256': origin['sha256'],
            'library_access': origin, 'profile_edition': edition}
