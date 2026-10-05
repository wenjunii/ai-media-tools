"""Read local run history, including failed runs; no app execution or network."""
from .common import LOCAL, checked_run_path, read_json
from .status import draft_status


def local_history(limit=20):
    if not isinstance(limit, int) or limit < 1:
        raise ValueError('History limit must be a positive integer')
    root = LOCAL / 'runs'
    candidates = sorted((p for p in root.iterdir() if p.is_dir()),
                        key=lambda path: path.name, reverse=True) if root.is_dir() else []
    runs = []
    for path in candidates[:limit]:
        row = {'run': path.name, 'directory': str(path)}
        try:
            path = checked_run_path(path)
            manifest = read_json(path / 'manifest.json')
            if not isinstance(manifest, dict):
                raise ValueError('Run manifest must be a JSON object')
            if not isinstance(manifest.get('failures', []), list):
                raise ValueError('Run failure history must be a JSON array')
            row.update(created_utc=manifest.get('created_utc'), status=manifest.get('status', 'unknown'),
                       operation=manifest.get('operation', 'inference'),
                       failures=manifest.get('failures', []), parent_run=manifest.get('parent_run'))
            if (path / 'draft.mp4').is_file():
                draft = draft_status(path)
                row.update(video=draft['video'], automated_checks_passed=draft['automated_checks_passed'],
                           verification_state=draft['verification_state'],
                           saved_review_status=draft['saved_review_status'])
        except (OSError, ValueError, RuntimeError, KeyError, TypeError) as error:
            row.update(status='unavailable or invalid', error=str(error))
        runs.append(row)
    return {'total_runs': len(candidates), 'shown': len(runs), 'runs': runs}


def format_history(history):
    lines = [f'Local demo history: {history["shown"]} of {history["total_runs"]} runs']
    for run in history['runs']:
        checks = run.get('verification_state', 'no completed video')
        lines.append(f'\n{run["run"]} | {run["status"]} | checks: {checks}')
        if run.get('parent_run'):
            lines.append(f'  Revised from: {run["parent_run"]}')
        for failure in run.get('failures', []):
            if isinstance(failure, dict):
                lines.append(f'  {failure.get("stage", "failure")}: {failure.get("error", "unknown")}')
        if run.get('error'):
            lines.append(f'  {run["error"]}')
        lines.append(f'  {run["directory"]}')
    return '\n'.join(lines)
