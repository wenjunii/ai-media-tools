# PC demo production MVP

Manual, local video production in the shared AI Media Scout repository. The Mac
continues to own research, library/report publication, scheduling, and email.
Read [the brief](../PROJECT_BRIEF.md) and [PC instructions](AGENTS.md).

This MVP runs the official portable Real-ESRGAN application on a reproducible
original illustration, then makes a 45-second vertical draft from its actual
output. It includes six scenes: result, input, comparison, process, practical use,
and limitation. There is no scheduler, social API client, or uploader.

## Installed app and daily manual use

Real-ESRGAN is installed on the tested PC as the official **20220424 portable
Windows CLI** (upstream release `v0.2.5.0`), with the `realesrgan-x4plus-anime`
model. The executable lives at
`.local/apps/realesrgan-20220424/realesrgan-ncnn-vulkan.exe`. No desktop GUI or
system-wide installation is required. [The first draft results](MVP_RESULT.md)
record the actual run and its limitations.

From the repository root in PowerShell:

```powershell
.\pc_demo\demo.ps1 status
.\pc_demo\demo.ps1 history
.\pc_demo\demo.ps1 run -GpuId 1
.\pc_demo\demo.ps1 verify
```

`status` checks the installed app/model hashes and the latest draft's saved
evidence without downloading or running the app. It distinguishes an absent or
damaged installation from verified files. It also reports whether saved playback
and visual review belong to the current video bytes. `verify` defaults to the
latest completed draft and reruns full media checks. An existing matching manual
review is preserved; a changed video requires a new review. The PowerShell
launcher saves its own output logs under `.local/launcher-logs/`.

## Revise a video without repeating inference

Use `history` to see completed runs, failed attempts, their error messages and
local directories. It shows the newest 20 runs by default; use `-Limit 50` for
more, or `-Json` for structured output. It never downloads or executes an app.

`revise` builds a new video from a previous run's preserved input and actual
Real-ESRGAN output. It checks the original hashes and successful inference log,
then creates a new run directory with its own narration, video and verification.
The source run stays intact. A failed video assembly is also reusable if its
inference completed successfully. There is no app/model download or inference
during revision.

```powershell
# Rebuild the latest completed draft using its saved storyboard:
.\pc_demo\demo.ps1 revise

# Create a fresh editable copy of that storyboard:
$latest = (Get-Content .\pc_demo\.local\latest-run.json -Raw | ConvertFrom-Json).run
$edit = Join-Path '.\pc_demo\.local' ('storyboard-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.local.json')
Copy-Item -LiteralPath (Join-Path $latest 'storyboard.json') -Destination $edit
# Edit the JSON title, scene titles, captions and narration, then:
.\pc_demo\demo.ps1 revise -Storyboard $edit

# To recover an older failed assembly, pass its directory from history:
# .\pc_demo\demo.ps1 revise -RunDirectory <source-run-directory> -Storyboard $edit
.\pc_demo\demo.ps1 verify
```

The supported template remains six 7.5-second scenes, 45 seconds total, at
1080x1920 and 30 fps. Keep scene kinds and timing unchanged; titles and captions
have one or two lines. The validator rejects unsupported layouts before creating
a revision. Font-width checks happen before narration, and spoken lines must fit
their scene without truncation. `run` also accepts `-Storyboard` for a new actual
inference with edited narration.

A revision records its parent manifest, the original inference run, inherited
failures and current editing source. Original execution evidence stays under
`evidence/inference/`, and the original command/logs are copied unchanged. Its
process card labels the reused output and retains the original measured time.
Previous manual review is not copied to the new video: play and inspect each new
draft, and listen before uploading. Only a successfully completed revision moves
the latest-draft pointer.

## Prerequisites and setup on a new Windows checkout

Tested host: Windows 11 Home x64, i9-12900H, RTX 3080 Ti Laptop 16 GB VRAM,
63.71 GiB system RAM, about 374 GiB free at initial inspection. Installed Python
is CPython 3.10.11 x64. This is the tested configuration, not a universal minimum.

The first version deliberately pins **Windows CPython 3.10 x64** and Pillow
11.3.0. It expects existing `python.exe`, `ffmpeg`, and `ffprobe` on PATH, Windows
Segoe UI/Consolas fonts, and an installed English US System.Speech voice. The
setup command records their identity. It does not install Python/FFmpeg globally,
update graphics drivers, or change system settings. FFmpeg must support libx264,
AAC, loudnorm and ebur128. This PC's pre-existing FFmpeg 4.3.1 was tested.

From the repository root in PowerShell:

```powershell
.\pc_demo\demo.ps1 doctor
.\pc_demo\demo.ps1 setup
.\pc_demo\demo.ps1 status
.\pc_demo\demo.ps1 run -GpuId 1
```

`1` is the NVIDIA Vulkan device index observed on this PC. On another Windows
machine, omit `-GpuId` for the application's automatic selection; review its
logged device list. Vulkan device indices are not CUDA indices and can change.
The wrapper uses a waiting process and saved output logs so the command cannot
silently finish before its Python child on this host.

Setup downloads the official 20220424 release from the author, checks the pinned
ZIP hash, extracts only the executable, required DLL, chosen model and README,
and installs the hash-checked Pillow wheel into `.local/venv`. It archives the
reviewed source documents. [Read the terms review](LICENSE_REVIEW.md), including
the explicit model-license documentation gap and portable dependency scope.
An already downloaded matching ZIP/wheel is reused. A fresh machine needs the
official URLs to remain available; the retained local downloads support recovery.
This is dependency isolation, not a security sandbox.

## Outputs and replay

Each invocation creates a new UTC-named directory in `.local/runs/`. Successful
runs update `.local/latest-run.json`; failed attempts are kept with their logs.
No run overwrites another. The finished video is `draft.mp4` in that directory.

```powershell
$run = (Get-Content .\pc_demo\.local\latest-run.json -Raw | ConvertFrom-Json).run
# Omit -RunDirectory to check the latest draft, or specify an older run:
.\pc_demo\demo.ps1 verify -RunDirectory $run
Start-Process -FilePath (Join-Path $run 'draft.mp4')
```

To replay the actual inference independently, use the saved argument list in
`logs/inference.command.json`. The command is equivalent to:

```powershell
$app = Join-Path $PWD 'pc_demo\.local\apps\realesrgan-20220424'
& "$app\realesrgan-ncnn-vulkan.exe" `
  -i "$run\inputs\input.jpg" -o "$run\outputs\replay.png" `
  -n realesrgan-x4plus-anime -s 4 -t 256 -m "$app\models" -g 1 -v
```

Keep the original `actual-output.png` untouched. Exact output can depend on GPU
driver/runtime; compare hashes and pixels instead of promising bitwise identity
across machines. The procedural source uses seed 31. Only its 256×256 JPEG at
quality 48 is passed to the app, which emits a 1024×1024 PNG. There is no text
prompt. The comparison shows bicubic enlargement at the same crop and scale.

The `review.html` page can be opened with a local HTTP server bound to loopback:

```powershell
python -m http.server 8767 --bind 127.0.0.1 --directory "$run"
# Open http://127.0.0.1:8767/review.html in a browser; Ctrl+C stops the server.
```

The video is H.264/yuv420p, 1080×1920 at 30 fps, 45 seconds, with AAC 48 kHz
stereo narration. The source audio is the standard Windows Zira voice on this
PC; it is separate editorial narration. Camera motion and poster typography are
editorial additions, not claims of video generation by Real-ESRGAN. The process
card is visibly labeled as log-derived. No native GUI screen recording was
made because the tested app runs as a background CLI; raw stdout/stderr and the
exact invocation are retained.

| File or directory | Evidence |
| --- | --- |
| `inputs/` | Original master and exact deliberately reduced JPEG |
| `outputs/actual-output.png` | Untouched app output |
| `manifest.json` | Settings, hashes, timing, state, failures and provenance |
| `evidence/` | Library snapshot/profile, hardware, setup, terms, complete PC source snapshot |
| `logs/` | Commands, exit codes, timings, stdout/stderr, encoder logs |
| `storyboard.json`, `captions.srt`, `transcript.txt` | Narrative, timing, on-screen callouts and exact spoken subtitles |
| `audio/` | Voice name, raw utterances, durations and normalized master |
| `qa/` | Decoded scenes, visual comparisons, codec/audio verification |
| `draft.mp4`, `review.html` | Finished draft and local review page |

Automated verification checks full video/audio decoding, codecs, dimensions,
duration, hashes, six encoded frames against source composition, caption width,
and audio levels. It rejects clipped/missing narration and blank/wrong-size app
outputs. Visual playback and a creator listening pass complement those checks;
signal levels alone do not establish pronunciation or subjective sound quality.

Verification binds a pass to the input, app output, video, storyboard and
inference/render records. Changed artifacts invalidate that pass. Each recheck
archives the previous result under `qa/verification-history/` and records a new
pending/pass/failure result, so a failed recheck cannot leave an old pass visible.
For drafts made before this format was added, run `verify` once to refresh their
verification evidence. The video and matching manual review stay intact.

## Failure recovery and next apps

Read `logs/failure.txt` and `manifest.json` in the failed run; fix the cause and
start a new run, or use `revise` when the saved inference succeeded. Audio lines
must fit their scene with a 0.35-second margin.
Do not trim speech to force success. The concat step uses the audio directory as
its working directory for compatibility with this PC's older FFmpeg.

For a GPU/driver failure, inspect the Vulkan device list and try the automatic
device choice. A lower tile size is a reviewed configuration change, not an
implicit fallback. If this application cannot run, record the failure and review
another complete library profile with explicit model terms before installing it.
Never replace a failed output with the original master or a stock demonstration.

Only one app adapter is implemented. Future daily selection should consume the
Mac-published library and require a separately reviewed adapter for each app.
Profile installation commands are reference text and are never automatically
executed. A daily demo schedule is a later user decision after MVP review.

## Git and handoff

`.local/` is ignored: no models, environments, videos, machine paths, credentials,
private Mac settings, or delivery receipts belong in Git. Source, tests, the
brief, and the terms review can be shared through this same repository. Use a
`codex/` branch. When the user requests PC source/docs GitHub sync, follow the
[protected PR procedure](../docs/GITHUB_SYNC.md#pc-source-and-documentation-sync),
including CI on the exact PR head and merged main commit. The Mac keeps ownership
of research publication and its private sync checkpoints. A Git pull transfers
source only: run setup for the app/model on a new Windows checkout and choose an
explicit asset transfer for videos. Never add runtime/media to `public/` or
force-add ignored files.

Social publishing stays disabled. Instagram and X require authorized integrations.
TikTok requires an approved publishing route or a creator review/upload step.
This MVP has no endpoint that can publish, email, or create a schedule.

Run the PC checks from the repo root on Windows:

```powershell
python -m unittest discover -s tests -p test_pc_demo.py -v
python -m compileall -q media_scout pc_demo tests
node --test tests/library.test.cjs
# Stage reviewed source/docs explicitly, then:
python -m pc_demo audit-git
git diff --cached --check
```

CI runs the full research/PC suite on Linux with Python 3.10 and 3.13, plus the
PC guardrail tests and launcher smoke check on Windows with Python 3.10. CI does
not install Real-ESRGAN or download its model; inference remains a local check.

The existing research package imports Unix `fcntl`; its complete suite and
archive/publication audits must run under macOS/Linux, including the already
installed `Ubuntu-Manual` WSL distribution on this PC. They do not execute tools
or send email. From this checkout in a WSL/Linux shell:

```sh
python3 -m unittest discover -s tests -v
python3 -m media_scout verify-public-archive
python3 -m media_scout audit-publication
```

The root `.gitattributes` preserves exact committed bytes in `public/` and the
browser assets in `media_scout/ui/` that are copied into the library. This
matters because automatic Windows CRLF conversion breaks the existing sealed
report hashes even in a fresh clone. Do not rebuild reports to fix line endings.
It also preserves `pc_demo/runtime.lock.json` byte for byte, so switching branches
does not invalidate the saved installation checksum through line-ending changes.
For a pre-existing clean checkout affected by conversion, restore those public
files from their committed blobs after applying the attributes, then verify.

The audit is read-only. Do not run Mac discovery, build/export, publication
checkpoints, or email commands as part of PC development. Demo commands never
push or merge Git changes; source sync is a separately authorized maintenance
operation.
