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
