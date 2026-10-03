import pathlib
import shutil
import subprocess
import traceback
from datetime import datetime, timezone
from PIL import Image
from .common import ROOT, LOCAL, download, execute, read_json, select_profile, sha256, stamp, write_json
from .setup_runtime import verified_runtime


def run_demo(gpu_id=-1):
    app,receipt=verified_runtime()
    lock=read_json(ROOT/'runtime.lock.json')
    run=LOCAL/'runs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-realesrgan')
    run.mkdir(parents=True,exist_ok=False)
    for name in ('inputs','outputs','logs','audio','qa','evidence'):
        (run/name).mkdir()
    manifest={'schema_version':1,'created_utc':stamp(),'status':'running',
              'app':lock['app'],'social_publishing_enabled':False,'schedule_enabled':False,
              'settings':{'model':lock['app']['model'],'scale':4,'tile':256,'gpu_id':gpu_id,'prompt':None,
                          'input_size':[256,256],'jpeg_quality':48,'input_seed':31},
              'failures':[],'source_artwork':'Original procedural geometry, created for this controlled test',
              'screen_recording':{'created':False,'reason':'App is a background CLI. Raw execution logs retained; process card explicitly labeled as log-derived.'},
              'audio':'Separate Windows synthetic narration; Real-ESRGAN produces a still image',
              'isolation':'Portable app + Python virtual environment, not OS sandbox'}
    write_json(run/'manifest.json',manifest)
    try:
        try:
            download(lock['library_url'],run/'evidence/library.json')
            manifest['library_source']=lock['library_url']
        except Exception as error:
            manifest['failures'].append({'stage':'library-download','error':str(error),'fallback':'repository public/library.json'})
            shutil.copyfile(ROOT.parent/'public/library.json',run/'evidence/library.json')
            manifest['library_source']='repository public/library.json (offline fallback)'
        version=select_profile(read_json(run/'evidence/library.json'),lock['app']['library_id'])
        write_json(run/'evidence/selected-profile.json',version)
        manifest['profile_edition']=version.get('edition_id',version['date'])
        manifest['library_sha256']=sha256(run/'evidence/library.json')
        shutil.copyfile(LOCAL/'setup.json',run/'evidence/setup.json')
        shutil.copyfile(LOCAL/'hardware.json',run/'evidence/hardware.json')
        shutil.copyfile(ROOT/'runtime.lock.json',run/'evidence/runtime.lock.json')
        shutil.copyfile(ROOT/'storyboard.json',run/'storyboard.json')
        snapshot=run/'evidence/source/pc_demo'
        snapshot.mkdir(parents=True)
        source_hashes={}
        for path in ROOT.iterdir():
            if path.is_file() and path.suffix in ('.py','.ps1','.json','.md') and not path.name.endswith('.local.json'):
                shutil.copyfile(path,snapshot/path.name)
                source_hashes[path.name]=sha256(path)
        write_json(run/'evidence/source/hashes.json',source_hashes)
        manifest['source_git_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT.parent,text=True).strip()
        manifest['source_snapshot']='evidence/source/pc_demo (includes current uncommitted source if any)'
        if (ROOT/'LICENSE_REVIEW.md').exists():
            shutil.copyfile(ROOT/'LICENSE_REVIEW.md',run/'evidence/LICENSE_REVIEW.md')
        for source in receipt['sources']:
            shutil.copyfile(LOCAL/'sources'/source['name'],run/'evidence'/source['name'])
        from .artwork import make_artwork
        make_artwork(run/'inputs')
        args=[app/lock['app']['executable'],'-i',run/'inputs/input.jpg','-o',run/'outputs/actual-output.png',
              '-n',lock['app']['model'],'-s','4','-t','256','-m',app/'models','-v']
        if gpu_id>=0:
            args += ['-g',str(gpu_id)]
        manifest['inference']=execute(args,run/'logs','inference',timeout=300,cwd=app)
        with Image.open(run/'outputs/actual-output.png') as output:
            if output.size!=(1024,1024):
                raise ValueError('App did not produce the required 4x PNG')
            if max(channel[1]-channel[0] for channel in output.convert('RGB').getextrema())<32:
                raise ValueError('App output is unexpectedly blank')
        manifest['input_sha256']=sha256(run/'inputs/input.jpg')
        manifest['output_sha256']=sha256(run/'outputs/actual-output.png')
        print(f'Real app inference completed in {manifest["inference"]["elapsed_seconds"]:.3f}s',flush=True)
        write_json(run/'manifest.json',manifest)
        ps=shutil.which('powershell.exe')
        execute([ps,'-NoProfile','-File',ROOT/'narrate.ps1','-RunDirectory',run],run/'logs','narration')
        ffmpeg=receipt['hardware']['media_tools']['ffmpeg']['path']
        if sha256(ffmpeg)!=receipt['hardware']['media_tools']['ffmpeg']['sha256']:
            raise RuntimeError('FFmpeg changed since setup; rerun setup to record current dependency')
        from .render import make_audio,render_video
        make_audio(run,ffmpeg)
        render_video(run,ffmpeg)
        manifest['status']='rendered'
        manifest['video_sha256']=sha256(run/'draft.mp4')
        write_json(run/'manifest.json',manifest)
        from .verify import verify_run
        verify_run(run)
        manifest['status']='automated_checks_passed'
        manifest['finished_utc']=stamp()
        manifest['human_review']='Visual and browser playback review pending; listening review is not inferred from audio metrics'
        write_json(run/'manifest.json',manifest)
        write_json(LOCAL/'latest-run.json',{'run':str(run),'video':str(run/'draft.mp4')})
        write_review_page(run)
        return run
    except Exception as error:
        manifest['status']='failed'
        manifest['failures'].append({'stage':'pipeline','error':str(error)})
        write_json(run/'manifest.json',manifest)
        (run/'logs/failure.txt').write_text(traceback.format_exc(),encoding='utf-8')
        print(f'FAILED RUN PRESERVED: {run}',flush=True)
        raise


def write_review_page(run):
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Media Scout — local draft review</title><style>
body{margin:0;background:#111c20;color:#f4eddc;font:17px system-ui}main{max-width:1160px;margin:36px auto;padding:0 28px;display:grid;grid-template-columns:360px 1fr;gap:40px}video{width:100%;max-height:82vh;background:black;border-radius:12px}h1{font-size:38px}a{color:#d6f780}p{line-height:1.6}img{max-width:100%}.compare{display:grid;grid-template-columns:1fr 1fr;gap:16px}button{padding:12px 20px;font:inherit;background:#d6f780;border:0;border-radius:8px;cursor:pointer}@media(max-width:720px){main{display:block}video{max-height:70vh}}
</style><main><section><video id="draft" controls preload="metadata" playsinline src="draft.mp4"></video>
<p><button onclick="document.querySelector('video').play()">Play draft</button></p><p id="status">Local review only</p></section><section>
<p>AI MEDIA SCOUT / PC DEMO 001</p><h1>Small file.<br>Bigger possibilities.</h1><p>45 seconds · 1080 × 1920 · real Real-ESRGAN output · captions + synthetic narration.</p>
<p>This is a controlled test using an original illustration deliberately reduced to 256 × 256. The model receives only that JPEG. Camera motion, poster typography and process cards are editorial additions. The process card is derived from saved CLI logs.</p>
<div class="compare"><figure><img src="inputs/input.jpg" alt="Actual low resolution input"><figcaption>256 × 256 input</figcaption></figure><figure><img src="outputs/actual-output.png" alt="Actual untouched Real-ESRGAN output"><figcaption>1024 × 1024 actual output</figcaption></figure></div>
<p><a href="draft.mp4" download>Download MP4</a> · <a href="captions.srt">Captions</a> · <a href="manifest.json">Run record</a> · <a href="qa/verification.json">Verification</a></p>
<p>Publishing disabled. Limitation: inferred details can change edges or smooth texture. Keep the original. The footage is an edited still-image demo, not AI-generated video.</p></section></main>
<script>const v=document.querySelector('video'),s=document.querySelector('#status');v.ontimeupdate=()=>s.textContent=`Playback: ${v.currentTime.toFixed(1)} / ${v.duration.toFixed(1)} seconds`;v.onerror=()=>s.textContent='Playback error: '+v.error?.message;</script></html>'''
    (run/'review.html').write_text(page,encoding='utf-8')
