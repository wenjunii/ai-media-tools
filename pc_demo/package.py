"""Create a portable local review handoff from an already verified draft."""
import html
import json
import re
import shutil
import uuid
from datetime import datetime, timezone
from .common import ROOT, LOCAL, checked_run_path, read_json, sha256, stamp, write_json
from .captions import caption_text, write_captions
from .creator_review import review_identity
from .status import draft_status
from .storyboard import load_storyboard

PACKAGE_FILES = ('draft.mp4', 'captions.srt', 'captions.vtt', 'transcript.txt', 'review.html', 'README.md')


def export_package(run):
    run = checked_run_path(run)
    state = draft_status(run)
    if not state['automated_checks_passed']:
        raise ValueError('Package requires current automated checks; run verify first')
    identity = review_identity(run, state['video_sha256'])
    story = load_storyboard(run / 'storyboard.json')
    verification = read_json(run / 'qa/verification.json')
    package = LOCAL / 'packages' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-review')
    package.mkdir(parents=True, exist_ok=False)
    try:
        shutil.copyfile(run / 'draft.mp4', package / 'draft.mp4')
        if sha256(package / 'draft.mp4') != identity['video_sha256']:
            raise ValueError('Copied video differs from the verified draft')
        # Derive text from the verified storyboard, never from an unverified sidecar.
        write_captions(package, story, webvtt=True)
        data = {'schema_version': 1, **identity, 'title': story['title'],
                'creator_review_status': state['creator_review']['status'],
                'subtitles': caption_text(story, webvtt=True)}
        template = (ROOT / 'review-template.html').read_text(encoding='utf-8')
        replacements = {'__TITLE__': html.escape(story['title']),
                        '__REVIEW_DATA__': json.dumps(data, ensure_ascii=True).replace('<', '\\u003c')}
        page = re.sub(r'__TITLE__|__REVIEW_DATA__', lambda match: replacements[match.group()], template)
        (package / 'review.html').write_text(page, encoding='utf-8')
        (package / 'README.md').write_text(
            '# Local creator review package\n\n'
            'Open review.html in a browser, or play draft.mp4 directly. The package uses only local files. '
            'Optional spoken subtitles are included as SRT and WebVTT, alongside the transcript. '
            'The MP4 is copied without re-encoding.\n\n'
            'Watch the entire video, inspect the result and captions, and listen to the narration. '
            'Mark only checks you actually completed, choose a result and save review.json. '
            'The download stays on your computer; it does not update the source run automatically.\n\n'
            'Import your review from PowerShell at the repository root:\n\n'
            '```powershell\n.\\pc_demo\\demo.ps1 review -ReviewFile "C:\\path\\to\\review.json"\n```\n\n'
            'This defaults to the latest completed run. For an older draft, add -RunDirectory with '
            'its directory from the history command. Different video/storyboard bytes are rejected.\n\n'
            'This folder excludes original images, runtime files, model weights, raw logs and machine inventory. '
            'The video, title, subtitles and transcript still contain your creative material; inspect them before sharing. '
            'Preserve package.json to check file hashes.\n\n'
            'This is a local draft, not a post. A completed creator review does not authorize publishing or establish asset/model rights. '
            'Instagram/X need authorized integrations; TikTok needs an approved route or a creator upload step. '
            'Check the project license review and your asset permissions before use.\n', encoding='utf-8')
        if review_identity(run) != identity or not draft_status(run)['automated_checks_passed']:
            raise ValueError('Source draft changed during packaging; verify it again')
        receipt = {key: value for key, value in data.items() if key != 'subtitles'}
        receipt.update({'status': 'complete', 'created_utc': stamp(),
                   'social_publishing_enabled': False, 'schedule_enabled': False,
                   'media': {key: verification.get(key) for key in
                             ('duration_seconds', 'dimensions', 'video_codec', 'audio_codec')},
                   'builder_source_sha256': {name: sha256(ROOT / name) for name in
                                             ('package.py', 'captions.py', 'review-template.html')},
                   'files': {name: sha256(package / name) for name in PACKAGE_FILES}})
        write_json(package / 'package.json', receipt)
        pointer = LOCAL / ('latest-package-' + uuid.uuid4().hex + '.partial')
        write_json(pointer, {'directory': str(package), 'run': str(run)})
        pointer.replace(LOCAL / 'latest-package.json')
    except Exception as error:
        write_json(package / 'failure.json', {'status': 'failed', 'created_utc': stamp(), 'error': str(error)})
        raise
    return {'directory': str(package), 'review_page': str(package / 'review.html'),
            'creator_review_status': state['creator_review']['status'], 'social_publishing_enabled': False}
