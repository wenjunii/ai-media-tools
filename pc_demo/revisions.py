"""Create a new edit from preserved inference; never download or rerun the app."""
import copy
import shutil
from datetime import datetime, timezone
from .common import ROOT, LOCAL, checked_run_path, read_json, sha256, stamp, write_json
from .storyboard import load_storyboard


def reusable_inference(run):
    manifest = read_json(run / 'manifest.json')
    lock = read_json(ROOT / 'runtime.lock.json')
    if not isinstance(manifest, dict):
        raise ValueError('Source run has no valid manifest')
    app, settings = manifest.get('app', {}), manifest.get('settings', {})
    if (not isinstance(app, dict) or not isinstance(settings, dict)
            or app.get('library_id') != lock['app']['library_id']
            or app.get('sha256') != lock['app']['sha256']
            or settings.get('model') != lock['app']['model'] or settings.get('scale') != 4
            or settings.get('input_size') != [256, 256]):
        raise ValueError('Source is not a supported reviewed Real-ESRGAN illustration run')
    command = read_json(run / 'logs/inference.command.json')
    recorded = manifest.get('inference', {})
    if (not isinstance(command, dict) or not isinstance(recorded, dict)
            or command.get('returncode') != 0 or recorded.get('returncode') != 0
            or not command.get('argv') or command.get('argv') != recorded.get('argv')):
        raise ValueError('Source run has no matching successful inference record')
    for relative, field in (('inputs/input.jpg', 'input_sha256'),
                            ('outputs/actual-output.png', 'output_sha256')):
        if sha256(run / relative) != manifest.get(field):
            raise ValueError(f'Source integrity failure: {relative}')
    for name in ('inference.stdout.log', 'inference.stderr.log'):
        if not (run / 'logs' / name).is_file():
            raise ValueError(f'Source inference log is missing: {name}')
    return manifest


def prepare_revision(source, storyboard=None):
    """Copy verified inputs/evidence to a distinct run; old drafts stay untouched."""
    source = checked_run_path(source)
    original = reusable_inference(source)
    story = load_storyboard(storyboard or source / 'storyboard.json')
    inference_evidence = source / ('evidence/inference' if original.get('reused_inference') else 'evidence')
    receipt = read_json(inference_evidence / 'setup.json')
    run = LOCAL / 'runs' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-realesrgan-revision')
    run.mkdir(parents=True, exist_ok=False)
    for name in ('inputs', 'outputs', 'logs', 'audio', 'qa', 'evidence'):
        (run / name).mkdir()
    manifest = copy.deepcopy(original)
    for field in ('video_sha256', 'finished_utc', 'human_review'):
        manifest.pop(field, None)
    manifest.update(created_utc=stamp(), status='running', operation='revision', reused_inference=True,
                    parent_run=source.name, inference_origin_run=original.get('inference_origin_run', source.name),
                    inherited_failures=original.get('inherited_failures', []) + original.get('failures', []),
                    failures=[], social_publishing_enabled=False, schedule_enabled=False)
    write_json(run / 'manifest.json', manifest)
    from .pipeline import record_failure, snapshot_source
    try:
        shutil.copyfile(source / 'manifest.json', run / 'evidence/parent-manifest.json')
        manifest['parent_manifest_sha256'] = sha256(run / 'evidence/parent-manifest.json')
        # Flatten the original inference evidence across repeated revisions.
        shutil.copytree(inference_evidence, run / 'evidence/inference')
        shutil.copyfile(inference_evidence / 'setup.json', run / 'evidence/setup.json')
        for relative in ('inputs/input.jpg', 'outputs/actual-output.png',
                         'logs/inference.command.json', 'logs/inference.stdout.log', 'logs/inference.stderr.log'):
            shutil.copyfile(source / relative, run / relative)
        if (source / 'inputs/source-artwork.png').is_file():
            shutil.copyfile(source / 'inputs/source-artwork.png', run / 'inputs/source-artwork.png')
        write_json(run / 'storyboard.json', story)
        manifest['source_git_commit'] = snapshot_source(run)
        manifest['source_snapshot'] = 'evidence/source/pc_demo (current edit); evidence/inference/source (original app run)'
        write_json(run / 'manifest.json', manifest)
        reusable_inference(run)  # Recheck copied bytes, including a concurrent source edit.
    except Exception as error:
        record_failure(run, manifest, error, 'revision-copy')
        raise
    return run, manifest, receipt


def revise_demo(source, storyboard=None):
    from .pipeline import finish_draft, record_failure
    run, manifest, receipt = prepare_revision(source, storyboard)
    try:
        print(f'Reusing preserved app output from {manifest["inference_origin_run"]}', flush=True)
        finish_draft(run, manifest, receipt)
    except Exception as error:
        record_failure(run, manifest, error, 'revision-render')
        raise
    return run
