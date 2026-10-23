"""Editorial video rendering from the preserved input and actual app output."""
import math
import os
import pathlib
import subprocess
import time
import wave
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont
from .common import ROOT, execute, read_json, sha256, stamp, write_json
from .storyboard import load_storyboard
from .inputs import input_relative, validate_size
from .captions import write_captions

W, H = 1080, 1920
INK, PAPER, MUTED, ACCENT = '#111c20', '#f4eddc', '#9db4b6', '#d6f780'
FONT_ROOT = pathlib.Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'


@lru_cache(None)
def font(size, bold=False, mono=False):
    name = 'consola.ttf' if mono else ('segoeuib.ttf' if bold else 'segoeui.ttf')
    return ImageFont.truetype(str(FONT_ROOT / name), size)


def label(draw, xy, text, size=30, color=MUTED, bold=False, mono=False):
    draw.text(xy, text, fill=color, font=font(size,bold,mono))


def cover(image, size):
    width, height = size
    factor=max(width/image.width,height/image.height)
    resized=image.resize((round(image.width*factor),round(image.height*factor)),Image.Resampling.LANCZOS)
    x,y=(resized.width-width)//2,(resized.height-height)//2
    return resized.crop((x,y,x+width,y+height))


def crop_pair(before, after, box):
    # Normalized coordinates enforce the identical crop for both versions.
    def one(im):
        return im.crop(tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box)))
    return one(before), one(after)


def contain(image, size, background=INK):
    factor=min(size[0]/image.width,size[1]/image.height)
    fitted=image.resize((round(image.width*factor),round(image.height*factor)),Image.Resampling.LANCZOS)
    canvas=Image.new('RGB',size,background)
    canvas.paste(fitted,((size[0]-fitted.width)//2,(size[1]-fitted.height)//2))
    return canvas


def poster(after, custom=False):
    result=Image.new('RGB',(760,1040),PAPER)
    d=ImageDraw.Draw(result)
    label(d,(38,22),'YOUR' if custom else 'NIGHT',100,INK,True)
    label(d,(36,119),'ARTWORK' if custom else 'GARDEN',100,INK,True)
    art=contain(after,(688,688),PAPER) if custom else after.resize((688,688),Image.Resampling.LANCZOS)
    result.paste(art,(36,252))
    label(d,(39,970),'LAYOUT STUDY / ACTUAL OUTPUT' if custom else 'BOTANICAL STUDY / No. 001',25,INK,False,True)
    return result


def title_size(line):
    return 75 if len(line) > 19 else 82


def validate_layout(story):
    """Measure the real render fonts without requiring an inference output."""
    from .storyboard import validate_storyboard
    validate_storyboard(story)
    draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    # Also load the monospaced face used by fixed labels and the process card.
    font(25, mono=True)
    for index, segment in enumerate(story['segments'], 1):
        lines = [('eyebrow', segment['eyebrow'], 27, True, 924)]
        lines += [('title', line, title_size(line), True, 875) for line in segment['title']]
        lines += [('caption', line, 42, False, 880) for line in segment['caption']]
        for field, line, size, bold, limit in lines:
            if '\n' in line or '\r' in line:
                raise ValueError(f'Scene {index} {field} must use separate single lines')
            width = draw.textlength(line, font=font(size, bold))
            if width > limit:
                raise ValueError(f'Scene {index} {field} exceeds safe width ({width:.0f} > {limit} px); shorten this line')
    return {'scenes': len(story['segments']), 'fonts': ['Segoe UI', 'Segoe UI Bold', 'Consolas'],
            'caption_safe_width_px': 880}


class Composer:
    def __init__(self, run):
        self.run=run
        self.story=load_storyboard(run/'storyboard.json')
        validate_layout(self.story)
        self.manifest=read_json(run/'manifest.json')
        self.custom=bool(self.manifest.get('source_asset'))
        self.input_file=input_relative(self.manifest)
        self.input_size=validate_size(self.manifest['settings']['input_size'])
        self.after=Image.open(run/'outputs/actual-output.png').convert('RGB')
        with Image.open(run/self.input_file) as original:
            if original.size!=self.input_size or self.after.size!=tuple(value*4 for value in self.input_size):
                raise ValueError('Image dimensions do not match the recorded 4x inference')
            self.before=original.convert('RGB').resize(self.after.size,Image.Resampling.BICUBIC)
        self.poster=poster(self.after,self.custom)
        box=(.12,.33,.60,.81)
        if self.custom:
            side=min(self.after.size)*.6
            dx,dy=side/self.after.width/2,side/self.after.height/2
            box=(.5-dx,.5-dy,.5+dx,.5+dy)
        self.detail_before,self.detail_after=crop_pair(self.before,self.after,box)
        self.full_art={}
        if self.custom:
            for kind,source in (('input',self.before),('result',self.after)):
                art=Image.new('RGB',(870,870),INK)
                art.paste(contain(source,(870,798)),(0,72))
                self.full_art[kind]=art
        self.cards=[]
        for segment in self.story['segments']:
            base=Image.new('RGB',(W,H),INK)
            d=ImageDraw.Draw(base)
            d.line((78,143,1002,143),fill='#415053',width=2)
            label(d,(78,92),'AI MEDIA SCOUT',26,PAPER,True)
            label(d,(758,92),'PC TEST / 001',23,MUTED,False,True)
            label(d,(78,192),segment['eyebrow'],27,ACCENT,True)
            for j,line in enumerate(segment['title']):
                # Long hook gets a slightly smaller font so it fits the safe width.
                size=title_size(line)
                label(d,(72,249+j*92),line,size,PAPER,True)
            for j,line in enumerate(segment['caption']):
                label(d,(78,1410+j*61),line,42,PAPER)
            label(d,(78,1656),'REAL APP OUTPUT / LOCAL DRAFT',23,MUTED,False,True)
            self.cards.append(base)

    def frame(self,t):
        index=min(int(t/7.5),5)
        segment=self.story['segments'][index]
        progress=(t-segment['start'])/(segment['end']-segment['start'])
        im=self.cards[index].copy()
        d=ImageDraw.Draw(im)
        kind=segment['kind']
        if kind in ('result','input'):
            source=self.after if kind=='result' else self.before
            # Editorial camera motion only; the app creates a still PNG.
            edge=870
            extra=int(18*progress)
            if self.custom:
                # Keep the entire artwork visible without stretching or cropping.
                art=self.full_art[kind]
            else:
                art=source.resize((edge+extra,edge+extra),Image.Resampling.LANCZOS)
                art=art.crop((extra//2,extra//2,extra//2+edge,extra//2+edge))
            im.paste(art,(78,480))
            d=ImageDraw.Draw(im)
            width,height=self.after.size if kind=='result' else self.input_size
            text=f'ACTUAL OUTPUT  /  {width} x {height}' if kind=='result' else f'INPUT  /  {width} x {height}  /  BICUBIC PREVIEW'
            d.rectangle((78,480,948,536),fill=INK)
            label(d,(96,490),text,24,ACCENT,False,True)
        elif kind in ('compare','limitation'):
            left=self.detail_before.resize((870,870),Image.Resampling.LANCZOS)
            right=self.detail_after.resize((870,870),Image.Resampling.LANCZOS)
            # Reveal actual output right-to-left, then hold a fair split comparison.
            position=(0.95-0.9*min(progress/.8,1)) if kind=='compare' else .5
            split=int(870*position)
            im.paste(right,(78,480))
            im.paste(left.crop((0,0,split,870)),(78,480))
            d=ImageDraw.Draw(im)
            d.line((78+split,480,78+split,1350),fill=ACCENT,width=4)
            d.rectangle((78,480,948,542),fill=INK)
            label(d,(98,492),'BICUBIC',26,PAPER,True)
            label(d,(647,492),'AI OUTPUT',26,ACCENT,True)
            if kind=='limitation':
                d.rectangle((98,1234,928,1318),fill=INK)
                label(d,(120,1255),'Inspect edges and fine texture.' if self.custom else 'Notice the softened fine texture.',34,PAPER)
        elif kind=='process':
            d.rounded_rectangle((78,490,948,1328),radius=24,fill='#1c2c31',outline='#415053',width=2)
            heading='ORIGINAL RUN / REUSED OUTPUT' if self.manifest.get('reused_inference') else 'RECORDED EXECUTION'
            label(d,(110,526),heading,27,ACCENT,True)
            label(d,(110,596),'realesrgan-ncnn-vulkan.exe',35,PAPER,False,True)
            for j,line in enumerate((f'-i {pathlib.PurePosixPath(self.input_file).name}  -o actual-output.png','-n realesrgan-x4plus-anime','-s 4  -t 256',f'-g {self.manifest["settings"]["gpu_id"]}' if self.manifest['settings']['gpu_id']>=0 else 'GPU: automatic selection')):
                label(d,(110,668+j*53),line,29,PAPER,False,True)
            d.line((110,918,910,918),fill='#415053',width=2)
            seconds=self.manifest['inference']['elapsed_seconds']
            label(d,(110,954),f'{seconds:.2f}s',76,ACCENT,True)
            label(d,(110,1056),'MEASURED WALL TIME / THIS INPUT',24,MUTED,False,True)
            width,height=self.input_size
            label(d,(110,1123),f'{width} x {height}  >  {width*4} x {height*4}',36,PAPER,True)
            label(d,(110,1224),'Log-derived card; not a screen recording.',26,MUTED)
        elif kind=='use':
            p=self.poster.resize((610,835),Image.Resampling.LANCZOS)
            d.rounded_rectangle((190,512,836,1371),radius=18,fill='#071013')
            im.paste(p,(174,491))
            d=ImageDraw.Draw(im)
        # A quiet timeline kept above the bottom platform UI area.
        d.line((78,1578,948,1578),fill='#3d4b4e',width=4)
        d.line((78,1578,78+870*t/45,1578),fill=ACCENT,width=4)
        for i in range(6):
            x=78+i*174
            if x<=948:
                d.ellipse((x-4,1574,x+4,1582),fill=ACCENT if i<=index else MUTED)
        return im


def make_audio(run, ffmpeg):
    story=read_json(run/'storyboard.json')
    concat=[]
    timings=[]
    overlong=[]
    for index,segment in enumerate(story['segments']):
        with wave.open(str(run/f'audio/voice-{index:02d}.wav'),'rb') as wav:
            duration=wav.getnframes()/wav.getframerate()
        if duration>segment['end']-segment['start']-.35:
            overlong.append(f'{index}: {duration:.2f}s')
    if overlong:
        raise ValueError('Shorten narration segments instead of truncating speech: '+', '.join(overlong))
    for index,segment in enumerate(story['segments']):
        source=run/f'audio/voice-{index:02d}.wav'
        with wave.open(str(source),'rb') as wav:
            duration=wav.getnframes()/wav.getframerate()
        allocated=segment['end']-segment['start']
        if duration>allocated-.35:
            raise ValueError(f'Narration {index} is {duration:.2f}s; shorten text instead of truncating speech')
        target=run/f'audio/segment-{index:02d}.wav'
        execute([ffmpeg,'-y','-i',source,'-af',f'apad,atrim=duration={allocated},afade=t=out:st={allocated-.15}:d=0.15',
                 '-ar','48000','-ac','2','-c:a','pcm_s16le',target],run/'logs',f'audio-{index}')
        concat.append(f"file 'segment-{index:02d}.wav'")
        timings.append({'index':index,'speech_seconds':duration,'allocated_seconds':allocated})
    (run/'audio/concat.txt').write_text('\n'.join(concat)+'\n',encoding='utf-8')
    execute([ffmpeg,'-y','-f','concat','-safe','0','-i','concat.txt','-af','loudnorm=I=-16:TP=-1.5:LRA=11',
             '-ar','48000','-ac','2','-c:a','pcm_s16le',run/'audio/narration.wav'],run/'logs','audio-master',cwd=run/'audio')
    write_json(run/'audio/timings.json',timings)


def render_video(run,ffmpeg):
    composer=Composer(run)
    (run/'qa').mkdir(exist_ok=True)
    for index in range(6):
        composer.frame(index*7.5+3).save(run/f'qa/scene-{index+1:02d}.png')
    sheet=Image.new('RGB',(1080,1280),INK)
    for index in range(6):
        panel=composer.frame(index*7.5+3).resize((360,640),Image.Resampling.LANCZOS)
        sheet.paste(panel,((index%3)*360,(index//3)*640))
    sheet.save(run/'qa/contact-sheet.jpg',quality=95)
    fps=composer.story['fps']
    args=[ffmpeg,'-y','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s','1080x1920',
          '-r',str(fps),'-i','pipe:0','-i',str(run/'audio/narration.wav'),'-map','0:v:0','-map','1:a:0',
          '-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k',
          '-ar','48000','-movflags','+faststart','-t','45',str(run/'draft.mp4')]
    start=time.perf_counter()
    meta={'argv':args,'started_utc':stamp(),'source_output_sha256':sha256(run/'outputs/actual-output.png'),
          'source_input_sha256':sha256(run/composer.input_file),'editorial_motion':True,'screen_recording':False}
    try:
        with (run/'logs/render.stderr.log').open('wb') as log:
            process=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=log)
            try:
                for index in range(45*fps):
                    process.stdin.write(composer.frame(index/fps).tobytes())
                    if index%(fps*5)==0:
                        print(f'Rendered {index//fps}/45 seconds',flush=True)
                process.stdin.close()
                code=process.wait(timeout=180)
            except BaseException:
                process.kill()
                process.wait()
                raise
        meta['returncode']=code
        if code:
            raise RuntimeError('Video encoding failed; see render.stderr.log')
    except Exception as error:
        meta['error']=str(error)
        raise
    finally:
        meta['elapsed_seconds']=round(time.perf_counter()-start,3)
        write_json(run/'logs/render.command.json',meta)
    # Portable caption sidecar in addition to burned-in on-screen captions.
    write_captions(run,composer.story)
    write_json(run/'qa/font-provenance.json', {name:sha256(FONT_ROOT/name) for name in ('segoeui.ttf','segoeuib.ttf','consola.ttf')})
