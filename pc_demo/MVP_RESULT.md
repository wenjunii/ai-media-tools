# First PC draft: measured result

Completed 2026-10-03. App: Real-ESRGAN, official Windows portable release
20220424 (`v0.2.5.0`), `realesrgan-x4plus-anime`, 4×, tile 256, Vulkan GPU 1.
The PC's GPU 1 was the NVIDIA RTX 3080 Ti Laptop with 16 GB VRAM.

Final local run: `.local/runs/20261003T135644361362Z-realesrgan/`.
Open its `draft.mp4`, or see `review.html`. Use `.local/latest-run.json` after
making subsequent drafts. These assets are intentionally absent from Git.

The app transformed a deliberately reduced 256×256 original illustration JPEG
into a 1024×1024 PNG in **2.276 seconds** measured wall time. The source master
was never passed to the model. The output hash matched the earlier successful
run on this same device. This is one controlled illustration test, not a general
restoration-quality or performance benchmark.

The draft is **45 seconds, 1080×1920, 30 fps, H.264/yuv420p with AAC stereo**.
The MP4 container reports 45.022 seconds including audio padding; the browser
reports 45 seconds. It starts with the actual output, shows a fair same-crop
bicubic comparison, explains the logged process, makes a poster mockup, and
states that detail is inferred and can change. Poster type, camera movement,
and Windows synthetic narration are editorial additions.

Checks performed:

- Full video/audio decode, required codecs/dimensions/duration, nonblank 4× app
  output, input/output/video hashes, and six decoded scenes against the original
  composition passed. Captions fit their safe area at 42 pixels.
- Audio: approximately −16.2 LUFS integrated, −1.5 dBFS true peak, −20.3 dBFS
  mean sample level. Every utterance fits its scene without truncation. This is
  signal/timing verification, not a claim of human listening. Creator listening
  review remains appropriate before upload.
- The first completed draft played through to 45 seconds in the Codex browser;
  final draft review evidence is stored alongside the video in `qa/`.
- 133 Python regression tests passed under the existing `Ubuntu-Manual` WSL
  distribution, including 10 new PC guardrail tests. The same 10 PC tests passed
  natively on Windows. All 18 browser-library tests and compile checks passed.
- Public archive verification passed: four editions, 12 report files, 209 tools.
  No published report, research source, or library content was changed.

## Honest failure history

The first four assembly attempts rejected narration that exceeded the allocated
scene duration (7.78, 7.29, 7.96 and 7.21 seconds). The text was shortened, and
validation now reports all overlong segments together. No speech was truncated.
The next attempt hit FFmpeg 4.3.1's handling of a concat list with a Windows
absolute path. Running concat from the audio directory fixed the resolution.
All five failed runs, their real app outputs and error logs remain under `.local/`.
Real-ESRGAN inference succeeded in every attempt; no fallback app was necessary.

The existing research suite could not import Unix `fcntl` under native Windows;
it was run unchanged in the PC's existing Ubuntu environment. The initial clone
also converted sealed public files and copied UI assets to CRLF. Those files were
restored to their exact committed bytes, without rebuilding anything. A root
`.gitattributes` now prevents those conversions on subsequent Windows clones.

No native app screen recording was made: this adapter runs a background CLI.
The exact command and raw logs are preserved, and the video explicitly identifies
its process card as log-derived. The selected model's separate license grant is
not explicit in the reviewed bundle; see [the recorded terms gap](LICENSE_REVIEW.md).

## Handoff boundary

The PC implementation was prepared on branch `codex/pc-demo-mvp` in the shared
repository. The first build was kept local. The user's subsequent request to
update scripts, README and GitHub sync authorizes reviewed source/docs/tests to
go through the protected PR flow. Follow-up checks add installation status,
preserve review evidence by video hash, and exercise the launcher in Windows CI.
Local follow-up validation passed all 139 Python tests under WSL, all 16 PC tests
natively on Windows, all 18 browser tests, compile checks and the public archive
audit. Reverification of the existing draft preserved its video hash and saved
manual review.
The first switch to merged main exposed Git's CRLF conversion of the runtime
lock, which invalidated its saved checksum despite unchanged app/model files.
The original lock bytes were restored, and an explicit Git attribute plus a
Windows-conversion regression test now preserve them across checkouts.
The checkout repair passed 140 regression tests and 17 native Windows PC tests.
No research automation, email, social upload, or daily demo schedule was created.
The Mac keeps its existing research workflow, credentials and private records.

Reproduce with `./pc_demo/demo.ps1 setup`, then `./pc_demo/demo.ps1 run -GpuId 1`
from PowerShell at the repository root. See [the complete run guide](README.md).
On the installed PC, use `./pc_demo/demo.ps1 status` to check the saved runtime
and latest draft, and `./pc_demo/demo.ps1 verify` to rerun media verification.

## Editorial reuse check: 2026-10-05

`revise` produced `.local/runs/20261005T173133809048Z-realesrgan-revision/`
from the original completed run, with edited narration, opening titles and
captions. It reused the exact input and untouched app output without another
inference or app/model download. The new 45-second, 1080x1920 video passed full
decode, provenance, frame/caption and audio checks, and reached the end in browser
playback. All six scenes were visually inspected. Creator listening is still
appropriate; subjective human audio review is not claimed.

The original manifest, video, input, output, inference logs and manual review
remained byte-for-byte unchanged. A fresh manual review belongs to the revision.
Rechecking the original draft upgraded its verification format while archiving
the previous result. Unit tests cover recovery after successful inference and
failed editing, rejection of changed output, preservation of prior runs, and
invalidation of an older pass after a failed recheck.

Validation: 162 full Python regression tests, 29 native Windows PC tests, all 18
browser tests and compile checks passed. Run artifacts and the edited storyboard
remain ignored local files; see the README for `history` and `revise` commands.

## Custom artwork check: 2026-10-12

The Windows launcher accepted an original procedural landscape PNG from a path
containing spaces. The existing reviewed app/model enlarged **320×192 to
1280×768 in 3.205 seconds** on Vulkan GPU 1. This is another controlled fixture,
not a claim about restoration of someone else's artwork or photographs.

The first assembly rejected its input-scene narration at 7.56 seconds. The failed
run is preserved at `.local/runs/20261013T022415247288Z-realesrgan/` (UTC naming).
After shortening that line, `revise` reused the successful output and produced
`.local/runs/20261013T022452579458Z-realesrgan-revision/`. No inference was repeated
for the revision. The original and normalized PNGs, actual output, logs, source
snapshots and failure history remain in those ignored run directories.

The 45-second, 1080×1920 H.264/AAC draft passed full decode, original-to-input
normalization, provenance hashes, six scene comparisons, caption-width and audio
checks. Mean/peak sample levels were −20.3/−1.5 dBFS; all speech fit its scenes.
The browser played to 45 seconds without an error, unmuted. All six scenes were
visually inspected: the landscape art keeps its proportions, labels show the
actual dimensions and the process card identifies reused inference. A fresh
hash-bound review is saved in `qa/manual-review.json`. Subjective human listening
is not claimed; the creator should listen before upload.

Replay this exact input on the installed PC:

```powershell
.\pc_demo\demo.ps1 run -GpuId 1 -InputImage .\pc_demo\.local\runs\20261013T022452579458Z-realesrgan-revision\inputs\source.png
```

Validation passed: 202 full Python regression tests under WSL, including all
image tests; 43 native Windows PC tests; 24 browser tests; compile checks; and
archive verification for 13 editions, 39 report files and 550 library tools.
Reverification of the original October 3 video also passed with its existing
video/input/output hashes and manual review intact. Windows CI now runs the image
tests with the already reviewed, hash-pinned Pillow wheel, without app/model
downloads. See the README for supported input limits and color/metadata handling.

## Creator handoff check: 2026-10-17

`package` exported the saved October 12 artwork revision to
`.local/packages/20261017T184708189727Z-review/`. It copied the existing 45-second
MP4 without inference or re-encoding. Its SHA-256 remains
`5e557d2f8b2e8fdb5458904708a13ed51dc51249bf8d9837ee510a3a4b28b14a`.
Reverification passed full decode, provenance, scene/caption and audio checks;
the earlier verification record was archived. The package contains only the
video, SRT/WebVTT subtitles, transcript, review page, instructions and hashes.

The review page was tested through a loopback-only server restricted to the
package directory. Playback reached 45 seconds without error, unmuted. Spoken
subtitles rendered, incomplete passing reviews stayed
blocked, and a separate synthetic fixture downloaded valid feedback. The Windows
launcher rejected that synthetic feedback for the real draft, including when
the review file path contained spaces. Unit tests also exercise valid synthetic
imports, preserved prior reviews, stale identities, failed exports, changed source
artifacts and safe title/subtitle escaping. The actual creator review remains
**pending**; agent playback checks do not claim creator listening or approval.

Direct opening from disk was blocked by the browser tool's URL policy, so that
route remains unverified. The README includes the tested loopback preview command.
No source inputs, models, raw logs or machine inventory are included in the
package. Review packages, downloads and browser evidence remain ignored local
files. No research, email, social upload or schedule operation was run.

Validation passed: 223 full Python tests under WSL, 58 native Windows PC tests,
32 library browser tests, compile checks, and archive verification for 18 editions,
54 report files and 756 library tools. The PC index audit and staged publication
audit passed under WSL. Native Git subprocess startup failed twice during the PC
index audit; the same read-only audit was completed successfully under WSL.

Reproduce with `./pc_demo/demo.ps1 package`. Open its `review.html`, complete your
checks, download `review.json`, then import with
`./pc_demo/demo.ps1 review -ReviewFile "C:\path\to\review.json"`. Use `status` or
`history` to inspect recorded creator feedback; a revision requires a fresh review.

## Local library and cached setup check: 2026-10-20

Installed demos now use the checkout's published `public/library.json`, or an
explicit `-LibraryFile`, without downloading the library. Each run preserves the
exact reference bytes, selected profile, edition, hash and local origin. Missing
or invalid references stop before inference. Explicit setup can reuse its reviewed
documents only when their source URLs, content hashes and saved runtime lock match.

The real Windows run at `.local/runs/20261020T171031618376Z-realesrgan/` succeeded
while Python network access was blocked by the validation harness. All five
reviewed setup documents were reused without fetching them. This was a Python
network guard, not an operating-system firewall test; the reviewed application,
model and media tools were already installed.

Real-ESRGAN enlarged the controlled illustration from **256×256 to 1024×1024 in
3.064 seconds** on Vulkan GPU 1. Its actual output hash matched the earlier
successful illustration run. The saved reference profile came from edition
`2026-10-01-r2`; this run makes no claim of a live research refresh.

The new **45-second, 1080×1920 H.264/AAC** draft passed full decode, output
provenance, six scene comparisons, caption-fit and audio checks. Mean/peak sample
levels were −20.3/−1.5 dBFS. All six contact-sheet frames were visually inspected.
Browser playback and creator listening/approval remain pending for this new video;
previous drafts' reviews do not apply to it. Its SHA-256 is
`cab6b0dd1b9ed224fadd28fd16729a5924930790748c03d9fb84680767232e74`.
The existing model-license documentation gap remains unchanged.

Reproduce on this installed PC without a library download:

```powershell
.\pc_demo\demo.ps1 run -GpuId 1
```

To replay with exactly this run's research reference:

```powershell
.\pc_demo\demo.ps1 run -GpuId 1 -LibraryFile .\pc_demo\.local\runs\20261020T171031618376Z-realesrgan\evidence\library.json
```

Validation passed: 261 full Python regression tests under WSL, 68 native Windows
PC tests, 32 browser-library tests, compile checks, and archive verification for
21 editions, 63 report files and 891 library tools. Logs and the offline validation
harness remain under ignored `.local/oct20-usage/`. This implementation was first
saved locally on `codex/pc-local-library`. The user's subsequent October 20 request
authorizes this batch for protected GitHub source sync. Future routine PC work
still stays local until sync is requested. The Mac retains its existing research,
public-library publication and email workflow.

## Offline preflight and recovery check: 2026-10-23

The new `preflight` command reports local readiness without downloading,
running the app or creating a run. It validates the runtime, isolated Python,
media-tool hashes, source evidence, storage, chosen artwork/library and the same
font widths used by rendering. New inference and revisions automatically apply
the relevant production checks. The Windows launcher also accepts `-Json`,
`-InputImage`, `-Storyboard` and `-LibraryFile` for preflight, including missing
paths so independent blockers can be reported together.

On this PC all ten default checks passed. A deliberately oversized caption
failed both standalone preflight and the automatic production gate. The rejected
run `.local/runs/20261023T113136756656Z-realesrgan/` retains its input, storyboard,
library and failure evidence; no inference command was invoked and the previous
latest-draft pointer was preserved. A launcher check from a different working
directory correctly reported that caption plus two missing local inputs.

The real run `.local/runs/20261023T113137136490Z-realesrgan/` enlarged the controlled
illustration from **256x256 to 1024x1024 in 2.419 seconds** on Vulkan GPU 1. FFmpeg
then exited with code `3221225794` while starting audio segment 3. The first
recovery, `.local/runs/20261023T113324786980Z-realesrgan-revision/`, hit the same
code at audio segment 1. Both attempts remain failed with their command records.
Subsequent FFmpeg launch probes passed; the startup failure's cause is unresolved.
Preflight checks file integrity, not successful native-process execution.

A second revision succeeded at
`.local/runs/20261023T113451060035Z-realesrgan-revision/`. It reused the actual
inference output byte-for-byte, preserved every file in the failed source run,
and made a **45-second, 1080x1920 H.264/AAC** draft. Full decode, six scene
comparisons, provenance, caption fit and audio checks passed. Mean/peak sample
levels were -20.3/-1.5 dBFS. The six contact-sheet frames were visually inspected;
browser playback and creator listening/approval remain pending for this draft.
Its video SHA-256 is
`a29b840ca2174ff9cc11ff072b67298b287469861aabba3c4c2a807781243fe8`.

The run and recovery used a Python network guard, not an OS firewall. The saved
library profile remains edition `2026-10-01-r2`, with no live freshness claim.
Source/model terms and the documented model-license gap are unchanged.

Reproduce the readiness check and a new inference run:

```powershell
.\pc_demo\demo.ps1 preflight
.\pc_demo\demo.ps1 run -GpuId 1
```

Reproduce the successful recovery without another inference:

```powershell
.\pc_demo\demo.ps1 revise -RunDirectory .\pc_demo\.local\runs\20261023T113137136490Z-realesrgan
```

Validation passed: 273 full Python tests under WSL (two Windows-font checks
skipped there), all 80 native Windows PC tests including those font checks,
32 library browser tests, compile checks and public archive verification for
21 editions, 63 report files and 891 library tools. Validation scripts, launch
diagnostics and reports are retained under ignored `.local/oct23-preflight/`.
This improvement stays local on `codex/pc-preflight` for an explicit later sync.
No GitHub request, research/email operation, schedule or social upload was made.
