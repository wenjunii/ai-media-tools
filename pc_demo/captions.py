"""Text sidecars derived from the saved, validated storyboard."""
import html
import textwrap
from .storyboard import validate_storyboard


def timestamp(value, separator=','):
    millis = round(value * 1000)
    return f'{millis//3600000:02d}:{millis//60000%60:02d}:{millis//1000%60:02d}{separator}{millis%1000:03d}'


def caption_text(story, webvtt=False):
    validate_storyboard(story)
    lines = ['WEBVTT', ''] if webvtt else []
    for index, segment in enumerate(story['segments']):
        separator = '.' if webvtt else ','
        narration = textwrap.wrap(segment['narration'], width=48)
        if webvtt:
            narration = [html.escape(line) for line in narration]
        lines += [str(index + 1),
                  f'{timestamp(segment["start"], separator)} --> {timestamp(segment["end"], separator)}',
                  *narration, '']
    return '\n'.join(lines)


def transcript_text(story):
    validate_storyboard(story)
    return '\n\n'.join(segment['narration'] for segment in story['segments']) + '\n'


def write_captions(directory, story, webvtt=False):
    (directory / 'captions.srt').write_text(caption_text(story), encoding='utf-8')
    (directory / 'transcript.txt').write_text(transcript_text(story), encoding='utf-8')
    if webvtt:
        (directory / 'captions.vtt').write_text(caption_text(story, webvtt=True), encoding='utf-8')
