"""Validate the supported editorial template before narration or rendering."""
from .common import read_json

KINDS = ('result', 'input', 'compare', 'process', 'use', 'limitation')


def validate_storyboard(story):
    if not isinstance(story, dict):
        raise ValueError('Storyboard must be a JSON object')
    expected = {'duration_seconds': 45, 'width': 1080, 'height': 1920, 'fps': 30}
    if any(type(story.get(key)) is not int or story[key] != value
           for key, value in expected.items()):
        raise ValueError('This template requires integer settings: 45 seconds, 1080x1920 and 30 fps')
    if not isinstance(story.get('title'), str) or not story['title'].strip():
        raise ValueError('Storyboard needs a title')
    segments = story.get('segments')
    if not isinstance(segments, list) or len(segments) != len(KINDS):
        raise ValueError('Storyboard requires six scenes, from result through limitation')
    for index, (segment, kind) in enumerate(zip(segments, KINDS)):
        if not isinstance(segment, dict) or segment.get('kind') != kind:
            raise ValueError(f'Scene {index + 1} must use kind {kind}')
        for key, expected_time in (('start', index * 7.5), ('end', (index + 1) * 7.5)):
            if type(segment.get(key)) not in (int, float) or segment[key] != expected_time:
                raise ValueError(f'Scene {index + 1} must keep its original 7.5-second timing')
        for field in ('eyebrow', 'narration'):
            if not isinstance(segment.get(field), str) or not segment[field].strip():
                raise ValueError(f'Scene {index + 1} needs {field} text')
        for field in ('title', 'caption'):
            lines = segment.get(field)
            if (not isinstance(lines, list) or not 1 <= len(lines) <= 2
                    or any(not isinstance(line, str) or not line.strip() or '\n' in line
                           or '\r' in line for line in lines)):
                raise ValueError(f'Scene {index + 1} {field} must have one or two nonempty lines')
    return story


def load_storyboard(path):
    return validate_storyboard(read_json(path))
