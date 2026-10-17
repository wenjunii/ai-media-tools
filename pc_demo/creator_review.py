"""Explicit creator feedback, kept separate from automated/agent playback checks."""
import json
import pathlib
import shutil
import uuid
from datetime import datetime
from .common import checked_run_path, read_json, sha256, stamp, write_json

CHECKS = ('playback', 'visual', 'captions', 'audio')


def review_identity(run, video_sha256=None):
    return {'run_id': run.name, 'video_sha256': video_sha256 or sha256(run / 'draft.mp4'),
            'storyboard_sha256': sha256(run / 'storyboard.json')}


def validate_review(record, identity):
    if not isinstance(record, dict) or type(record.get('schema_version')) is not int or record['schema_version'] != 1:
        raise ValueError('Creator review must use schema_version 1')
    if any(record.get(key) != value for key, value in identity.items()):
        raise ValueError('Creator review belongs to a different run, video or storyboard')
    checks = record.get('checks')
    if not isinstance(checks, dict) or set(checks) != set(CHECKS) or any(type(v) is not bool for v in checks.values()):
        raise ValueError('Creator review requires explicit playback, visual, captions and audio checkboxes')
    decision = record.get('decision')
    if decision not in ('passed', 'needs_changes') or (decision == 'passed' and not all(checks.values())):
        raise ValueError('A passed creator review requires all four checks; otherwise choose needs_changes')
    notes = record.get('notes', '')
    if not isinstance(notes, str) or len(notes) > 2000:
        raise ValueError('Review notes must be text with at most 2000 characters')
    reviewed = record.get('reviewed_utc')
    try:
        date = datetime.fromisoformat(reviewed.replace('Z', '+00:00')) if isinstance(reviewed, str) else None
        if date is None or date.utcoffset() is None:
            raise ValueError()
    except ValueError as error:
        raise ValueError('Creator review needs a timestamp with a time zone') from error
    return {'schema_version': 1, **identity, 'checks': checks, 'decision': decision,
            'notes': notes, 'reviewed_utc': reviewed}


def creator_review_state(run, video_sha256=None):
    result = {'status': 'pending', 'complete': False}
    path = run / 'qa/creator-review.json'
    if not path.is_file():
        return result
    try:
        identity = review_identity(run, video_sha256)
        record = read_json(path)
        if isinstance(record, dict) and any(record.get(key) != value for key, value in identity.items()):
            return {'status': 'stale', 'complete': False}
        record = validate_review(record, identity)
        return {'status': record['decision'], 'complete': record['decision'] == 'passed',
                'checks': record['checks'], 'notes': record['notes'], 'reviewed_utc': record['reviewed_utc']}
    except (OSError, ValueError, TypeError, KeyError) as error:
        return {'status': 'invalid', 'complete': False, 'error': str(error)}


def import_creator_review(run, source):
    from .status import draft_status
    run = checked_run_path(run)
    state = draft_status(run)
    if not state['automated_checks_passed']:
        raise ValueError('Run verify successfully for the current draft before importing a creator review')
    identity = review_identity(run, state['video_sha256'])
    with pathlib.Path(source).open('rb') as stream:
        raw = stream.read(65537)
    if len(raw) > 65536:
        raise ValueError('Creator review file exceeds 64 KiB')
    record = validate_review(json.loads(raw.decode('utf-8-sig')), identity)
    # Recheck before writing, including edits while the selected file was read.
    if review_identity(run) != identity or not draft_status(run)['automated_checks_passed']:
        raise ValueError('Draft changed while importing the review; review the current draft again')
    record['imported_utc'] = stamp()
    target = run / 'qa/creator-review.json'
    if target.is_file():
        history = run / 'qa/creator-review-history'
        history.mkdir(exist_ok=True)
        shutil.copyfile(target, history / (uuid.uuid4().hex + '.json'))
    pending = target.with_name('creator-review-' + uuid.uuid4().hex + '.partial')
    write_json(pending, record)
    pending.replace(target)
    return {'run': str(run), 'creator_review': creator_review_state(run), 'social_publishing_enabled': False}
