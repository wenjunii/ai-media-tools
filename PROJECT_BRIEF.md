# AI Media Scout: PC demo production

User brief, saved 2026-10-03 (America/New_York).

## Shared project and ownership

Mac and Windows PC share https://github.com/wenjunii/ai-media-tools.
The Mac owns daily research, reports, the searchable library, GitHub publication,
and email. Preserve that workflow and its one existing research scheduler.
Do not copy private Mac settings, credentials, research state, or delivery receipts.

Library: https://wenjunii.github.io/ai-media-tools/
Data: https://wenjunii.github.io/ai-media-tools/library.json
The library includes only open-source AI tools for all digital media and creative
workflows, with no fixed discovery limit. PC work consumes complete profiles as
reference and records hands-on results separately; it does not rewrite research.

## PC objective

Eventually select one library app daily, run a real creative demonstration, and
produce a short video for Instagram, TikTok, and X. Begin with local video drafts.
Use a separate execution project, `pc_demo/`, within this shared repository.
The research project remains configured not to install or run discovered tools.

## First working version

1. Inspect Windows version, GPU/VRAM, RAM, and available storage.
2. Read the library JSON and repository documentation as reference.
3. Select a compatible, well-documented app with a complete profile and a
   compelling demonstration. Review software and selected model terms separately.
4. Install from reviewed official sources into an isolated local environment.
   Preserve exact working versions, checksums, and reusable setup instructions.
5. Run a real demonstration. Preserve original inputs, prompts/settings, outputs,
   execution logs, and useful screen recordings when available.
6. Produce a 30–60 second vertical MP4: finished result first, brief process,
   readable captions, a practical use, and one honest limitation.
7. Verify playback, fidelity to actual app output, caption readability, and audio.
8. Deliver one finished draft and reproducible run instructions. Record failures
   honestly and select a fallback if necessary.

Model downloads, environments, credentials, and large generated assets stay out
of Git. Keep research scheduling and email on the Mac. Build and test the local
MVP before considering a daily demo schedule; do not add one in this phase.

Social publishing starts disabled. Instagram and X require authorized
integrations. TikTok requires an approved publishing route or a creator
review/upload step. This brief does not authorize social uploads or messages.

## Initial implementation boundary

Commit-worthy PC source, tests, configuration, license review, and instructions
live under `pc_demo/`. All downloads and run artifacts live in its ignored
`.local/` directory. Isolation means a portable application directory and a Python
virtual environment, not an operating-system security sandbox.
Code is prepared on a `codex/` branch for the Mac-owned GitHub publication flow.
