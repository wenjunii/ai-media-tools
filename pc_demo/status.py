"""Inspect local installation and draft evidence without running or downloading apps."""
from .common import ROOT, LOCAL, read_json, resolve_run, sha256
from .setup_runtime import verified_runtime


def review_state(run, video_sha256):
    result = {'browser_playback': 'pending', 'visual_review': 'pending',
              'saved_review_status': 'absent'}
    path = run / 'qa/manual-review.json'
    if not path.exists():
        return result
    try:
        review = read_json(path)
        if not isinstance(review, dict):
            raise ValueError('Manual review must be a JSON object')
        if review.get('video_sha256') != video_sha256:
            result['saved_review_status'] = 'stale: reviewed video hash differs'
            return result
        result['saved_review_status'] = 'matches current video'
        result['manual_review'] = review
        browser = review.get('browser', {})
        if isinstance(browser, dict) and browser.get('ended') is True:
            result['browser_playback'] = 'passed: saved playback review for these video bytes'
        if isinstance(review.get('visual_review'), str):
            result['visual_review'] = review['visual_review']
    except (OSError, ValueError) as error:
        result['saved_review_status'] = f'unreadable: {error}'
    return result


def local_status():
    lock = read_json(ROOT / 'runtime.lock.json')
    app = lock['app']
    result = {
        'app': app['name'], 'release': app['release'], 'model': app['model'],
        'installed': False, 'installation_state': 'not installed',
        'draft_environment_exists': (LOCAL / 'venv/Scripts/python.exe').is_file(),
        'latest_run': None, 'social_publishing_enabled': False,
        'daily_schedule_enabled': False,
    }
    if (LOCAL / 'setup.json').exists():
        try:
            directory, _ = verified_runtime()
            result.update(installed=True, installation_state='verified against saved hashes',
                          executable=str(directory / app['executable']))
        except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
            result.update(installation_state='needs setup or repair', installation_error=str(error))
    if (LOCAL / 'latest-run.json').exists():
        try:
            run = resolve_run()
            manifest = read_json(run / 'manifest.json')
            if not isinstance(manifest, dict):
                raise ValueError('Run manifest must be a JSON object')
            video = run / 'draft.mp4'
            digest = sha256(video)
            verification_path = run / 'qa/verification.json'
            verification = read_json(verification_path) if verification_path.is_file() else {}
            if not isinstance(verification, dict):
                raise ValueError('Verification record must be a JSON object')
            result['latest_run'] = {
                'directory': str(run), 'video': str(video), 'status': manifest['status'],
                'video_sha256': digest, 'video_matches_manifest': digest == manifest.get('video_sha256'),
                'automated_checks_passed': verification.get('automated_pass') is True
                    and digest == verification.get('video_sha256') == manifest.get('video_sha256'),
                **review_state(run, digest),
            }
        except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
            result['latest_run'] = {'status': 'unavailable or invalid', 'error': str(error)}
    return result
