"""Synthesize and master the storyboard's narration with local tools."""
import shutil
import wave

from .common import ROOT, execute, write_json
from .storyboard import load_storyboard

SAMPLE_RATE = 48000
SPEECH_MARGIN = 0.35


def make_audio(run, ffmpeg):
    story = load_storyboard(run / 'storyboard.json')
    audio = run / 'audio'
    timings = []
    inputs = []
    for index, segment in enumerate(story['segments']):
        source = audio / f'voice-{index:02d}.wav'
        try:
            with wave.open(str(source), 'rb') as wav:
                duration = wav.getnframes() / wav.getframerate()
        except (OSError, EOFError, wave.Error) as error:
            raise ValueError(f'Cannot read narration for scene {index + 1} ({segment["kind"]}): {source.name}') from error
        allocated = segment['end'] - segment['start']
        timings.append({'index': index, 'kind': segment['kind'], 'speech_seconds': duration,
                        'allocated_seconds': allocated, 'max_speech_seconds': allocated - SPEECH_MARGIN,
                        'fits': 0 < duration <= allocated - SPEECH_MARGIN})
        inputs.extend(['-i', source])
    write_json(audio / 'timings.json', timings)

    failed = [scene for scene in timings if not scene['fits']]
    if failed:
        details = ', '.join(
            f'scene {scene["index"] + 1} ({scene["kind"]}): '
            f'{scene["speech_seconds"]:.2f}s (limit {scene["max_speech_seconds"]:.2f}s)'
            for scene in failed
        )
        if any(scene['speech_seconds'] == 0 for scene in failed):
            raise ValueError(f'Narration includes empty audio. Check the voice and these scenes: {details}')
        raise ValueError(f'Shorten narration in {details}')

    # Pad each clip to its scene boundary, then normalize the whole timeline.
    # Doing this in one process also avoids intermediate padded WAVs on disk.
    filters = []
    for scene in timings:
        index = scene['index']
        seconds = scene['allocated_seconds']
        filters.append(f'[{index}:a]aformat=sample_fmts=s16:sample_rates={SAMPLE_RATE}:channel_layouts=stereo,'
                       f'apad,atrim=duration={seconds},afade=t=out:st={seconds - .15}:d=0.15[a{index}]')
    clips = ''.join(f'[a{scene["index"]}]' for scene in timings)
    filters.append(f'{clips}concat=n={len(timings)}:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11[master]')
    master = audio / 'narration.wav'
    execute([ffmpeg, '-nostdin', '-xerror', '-y', *inputs, '-filter_complex', ';'.join(filters), '-map', '[master]',
             '-ar', str(SAMPLE_RATE), '-ac', '2', '-c:a', 'pcm_s16le', master], run / 'logs', 'audio-master')
    with wave.open(str(master), 'rb') as wav:
        if wav.getparams()[:4] != (2, 2, SAMPLE_RATE, story['duration_seconds'] * SAMPLE_RATE):
            raise ValueError('Narration master must be 48 kHz stereo PCM and span the entire storyboard')


def prepare_narration(run, ffmpeg):
    powershell = shutil.which('powershell.exe')
    if not powershell:
        raise RuntimeError('Narration requires Windows PowerShell')
    execute([powershell, '-NoProfile', '-File', ROOT / 'narrate.ps1', '-RunDirectory', run],
            run / 'logs', 'narration')
    make_audio(run, ffmpeg)
