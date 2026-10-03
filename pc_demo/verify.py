import os
import re
from PIL import Image,ImageChops,ImageStat
from .common import execute,read_json,sha256,stamp,write_json
from .status import review_state


def verify_run(run):
    manifest=read_json(run/'manifest.json')
    setup=read_json(run/'evidence/setup.json')
    ffmpeg=setup['hardware']['media_tools']['ffmpeg']['path']
    ffprobe=setup['hardware']['media_tools']['ffprobe']['path']
    for name,path in (('ffmpeg',ffmpeg),('ffprobe',ffprobe)):
        if sha256(path)!=setup['hardware']['media_tools'][name]['sha256']:
            raise ValueError(f'{name} changed since the run setup')
    # Check the bytes actually consumed by the compositor, not just a label.
    render=read_json(run/'logs/render.command.json')
    expected={'inputs/input.jpg':manifest['input_sha256'],
              'outputs/actual-output.png':manifest['output_sha256'],
              'draft.mp4':manifest['video_sha256']}
    for path,digest in expected.items():
        if sha256(run/path)!=digest:
            raise ValueError(f'Provenance mismatch: {path}')
    if render['source_output_sha256']!=manifest['output_sha256'] or render['returncode']!=0:
        raise ValueError('Rendered video does not match the successful app output')
    inference=read_json(run/'logs/inference.command.json')
    if inference['returncode']!=0:
        raise ValueError('Inference did not succeed')
    execute([ffprobe,'-v','error','-show_streams','-show_format','-of','json',run/'draft.mp4'],run/'qa','probe')
    probe=read_json(run/'qa/probe.stdout.log')
    video=next(x for x in probe['streams'] if x['codec_type']=='video')
    audio=next(x for x in probe['streams'] if x['codec_type']=='audio')
    duration=float(probe['format']['duration'])
    if not (30<=duration<=60 and (video['width'],video['height'])==(1080,1920)):
        raise ValueError('Video fails duration or vertical dimensions')
    if video['codec_name']!='h264' or video['pix_fmt']!='yuv420p' or audio['codec_name']!='aac':
        raise ValueError('Video does not use the expected playback codecs')
    if int(audio['sample_rate'])!=48000 or audio['channels']!=2:
        raise ValueError('Audio must be 48 kHz stereo')
    execute([ffmpeg,'-v','error','-xerror','-i',run/'draft.mp4','-f','null',os.devnull],run/'qa','full-decode',timeout=180)
    execute([ffmpeg,'-hide_banner','-i',run/'draft.mp4','-af','volumedetect','-vn','-f','null',os.devnull],run/'qa','volume')
    log=(run/'qa/volume.stderr.log').read_text(encoding='utf-8',errors='replace')
    mean=float(re.search(r'mean_volume: ([-\d.]+) dB',log).group(1))
    peak=float(re.search(r'max_volume: ([-\d.]+) dB',log).group(1))
    if not (-30<mean<-9 and -6<peak<-.1):
        raise ValueError(f'Audio levels outside usable draft range: mean {mean}, peak {peak}')
    execute([ffmpeg,'-hide_banner','-i',run/'draft.mp4','-af','ebur128=peak=true','-vn','-f','null',os.devnull],run/'qa','loudness')
    # Decode the finished video and compare its art area against the same composed
    # source frame. Compression is permitted; a substituted output is not.
    from .render import Composer
    composer=Composer(run)
    pixel_errors=[]
    for index in range(6):
        timestamp=index*7.5+3
        frame=run/f'qa/decoded-{index+1:02d}.png'
        execute([ffmpeg,'-y','-v','error','-ss',str(timestamp),'-i',run/'draft.mp4','-frames:v','1',frame],run/'qa',f'extract-{index}')
        decoded=Image.open(frame).convert('RGB')
        expected_frame=composer.frame(timestamp)
        diff=ImageChops.difference(decoded,expected_frame)
        error=sum(ImageStat.Stat(diff).mean)/3
        if error>8:
            raise ValueError('Encoded visual content does not match the recorded compositor')
        pixel_errors.append(round(error,3))
    result={'verified_utc':stamp(),'automated_pass':True,'duration_seconds':duration,
            'dimensions':[video['width'],video['height']],'video_codec':video['codec_name'],
            'pixel_format':video['pix_fmt'],'frame_rate':video['r_frame_rate'],
            'audio_codec':audio['codec_name'],'audio_sample_rate':audio['sample_rate'],
            'audio_mean_dbfs':mean,'audio_peak_dbfs':peak,'full_decode':'passed',
            'actual_app_output_provenance':'hashes and decoded video comparisons passed',
            'scene_mean_absolute_pixel_error':pixel_errors,
            'caption_font_pixels':42,'caption_safe_bounds':[78,1410,958,1532],
            'subjective_listening':'not established by automated checks; creator review before upload',
            'video_sha256':sha256(run/'draft.mp4')}
    result.update(review_state(run, result['video_sha256']))
    write_json(run/'qa/verification.json',result)
    return result
