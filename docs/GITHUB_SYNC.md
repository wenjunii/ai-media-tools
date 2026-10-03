# GitHub publication before daily email

The daily order is **build and verify the report → synchronize GitHub → send email**.
The user authorizes public code, documentation, and finished daily reports. The
destination is `github_sync.repository` and `github_sync.branch` in
`config/scout.json`. Use the existing repository and chat schedule.

## Public exports and local records

`export-report` copies the sealed HTML, Markdown, and JSON report byte for byte to
`public/reports/YYYY-MM-DD/`. Its `publication.json` contains the date, counts,
seal time, and report hashes, with no recipient or delivery state. Public reports
are immutable. The command also updates `public/index.html` and `public/README.md`.
The latter provides a browsable list of Markdown editions on GitHub. HTML can be
downloaded and opened locally. Main CI publishes the searchable library to GitHub
Pages after verification; see `LIBRARY.md`.

The original `reports/`, raw `research/`, local `site/`, private configuration,
catalogs, outbox payloads, and delivery/sync receipts remain ignored. The public
index uses report links relative to `public/`. When importing older local history,
export its verified editions before publishing an index that links to them.

`python3 -m media_scout verify-public-archive` checks every published edition's
files, hashes, dates, profile/lead counts, and publication metadata, then checks
the report list and the public library's report links. It is read-only and needs
no private evidence or GitHub access. CI runs it on both supported Python versions.
It also checks that the full cumulative library data, HTML, and browser assets
match all finished public editions and the current UI source.

## Publish through the protected branch

1. Inspect the report's status and preserve any sealed edition. Reconcile a
   reserved or uncertain email with confirmed Sent mail before further email work.
   An already-sent report must never be sent again. Check the current Git branch,
   working tree, configured destination, and any pending publication PR.
   Date-wide `status` includes separately sealed updates and cumulative library
   counts. It verifies saved artifacts, but the stored checkpoint is not a fresh
   GitHub check; use `verify-sync` after publication to verify the remote commit
   and exact-commit CI.
2. Export the finished report:

   ```sh
   python3 -m media_scout export-report --date YYYY-MM-DD
   ```

3. Start from current main, or resume the existing publication branch/PR. Use a
   branch such as `codex/report-YYYY-MM-DD` for a new edition. Preserve unrelated
   changes. Include public exports and only reviewed, authorized source/doc changes;
   stage those paths explicitly. Never force-add ignored research or state.

   ```sh
   git add public
   python3 -m media_scout audit-publication
   git diff --cached --check
   ```

   The audit checks the entire Git index for private operational paths, the local
   recipient/project path, known access-token patterns, and private-key material.
   It also verifies the public archive and rejects staged changes or removal of
   existing dated report exports, even when revised metadata matches their bytes.
   The library and report list can grow as new editions are added.
   Review the staged diff as well. Use the checkout's GitHub noreply commit email.
4. Commit and push the publication branch. Open a PR to the configured main branch,
   using a file for the multiline PR body. Describe the final edition and relevant
   validation. Attach every created PR with the Codex `attach_artifact` tool, even
   when the PR was created by `gh`. Reuse a matching open PR instead of creating a
   duplicate after an interruption. If the exact export is already on main, skip
   creating a no-change commit/PR and continue to verification.
5. Check that the PR head matches the pushed commit and wait for its CI to pass.
   Merge normally with `gh pr merge --merge --match-head-commit COMMIT_SHA` and the
   checkout's noreply author email. Respect required reviews, checks, and protection;
   never use an administrative bypass. If GitHub requires user action, leave the
   concrete PR for review and stop email work.
6. Fetch origin, return to main, and fast-forward to `origin/main`. Wait for the
   configured CI workflow on the exact merged main commit, using `gh run list`
   with `--commit`, `--workflow`, `--branch`, and `--event push`, then watch that run.
   A passing PR run alone does not establish successful main CI. Clean up the
   completed publication branch after it is merged.
   The main CI run deploys only `public/` to GitHub Pages after all checks pass.
   PRs validate the site but do not deploy it. See `LIBRARY.md` for Pages setup.

## Verify the checkpoint, then deliver

```sh
python3 -m media_scout record-sync --date YYYY-MM-DD
python3 -m media_scout verify-sync --date YYYY-MM-DD
python3 -m media_scout verify --date YYYY-MM-DD
python3 -m media_scout prepare-email --date YYYY-MM-DD
```

`record-sync` checks the actual origin destination, main branch, clean working
tree, local/tracking/remote commit agreement, complete public edition and library,
and the latest matching main CI run. It writes an ignored checkpoint in
`state/publications/YYYY-MM-DD.json`. `verify-sync` repeats those checks and rejects
a checkpoint for different content, repository, or commit. If a later reviewed
project update changes main, verify and record the current publication again.
When the commit changes, `record-sync` preserves the previous checkpoint's exact
bytes in `state/publication_history/YYYY-MM-DD/` before replacing the current
checkpoint. This history remains local and does not change any delivery receipt.
The checkpoint covers the cumulative library JSON, HTML, styles and browser
code as well as the current edition. Main CI must finish its Pages deployment
before the sync can authorize email.

Explicitly requested same-day updates use [REPORT_UPDATES.md](REPORT_UPDATES.md).
Their separately sealed exports are also checked against the actual main commit
and included in the refreshed checkpoint. The original report and its delivery
receipt remain unchanged.

`prepare-email` repeats publication verification before creating its outbox and
send reservation. It records the verified GitHub commit and public report URL in
the local delivery receipt. Continue the Gmail delivery step in
`DAILY_WORKFLOW.md`, sending the exact complete reserved payload once.

A failed export, push, merge, CI run, or verification blocks email. Recover the
unfinished publication without rebuilding or recollecting a sealed report.
An uncertain Gmail result still requires mailbox reconciliation; a successful
GitHub sync never authorizes an email retry or alternate transport.

## Code and documentation maintenance

Preserve completed reports, research, local catalogs, delivery records, private
settings, and scheduler configuration. Run the regression suite, compile checks,
and `verify-public-archive`; stage only the reviewed source and documentation
changes, then run `audit-publication`. Use the protected PR flow above and wait
for CI on the exact PR head and merged main commit.

On the owning Mac, after returning to a clean, current main, run `record-sync` and `verify-sync` for
the existing published edition. This updates the publication checkpoint and
retains its prior version locally. Do not run discovery, build, export, email
preparation, or email delivery as part of source maintenance.
If the requested change affects the library UI or data schema, use
`build-library` to refresh only the derived views before staging. It preserves
all dated report files, source evidence and delivery records.

## PC source and documentation sync

An explicit user request to sync PC source/docs authorizes a protected PR from
the Windows checkout. This is separate from the Mac's daily publication flow.
Preserve public reports, the library, private Mac settings, delivery receipts,
research schedules and publication checkpoints. Do not run research discovery,
build/export, `record-sync`, `verify-sync`, or email commands on the PC.

1. Fetch current main and inspect the working tree and any existing matching PR.
   Use or resume a `codex/` branch, preserving unrelated changes.
2. Run the PC tests and launcher on Windows. Run the full regression suite,
   compile checks, browser tests and `verify-public-archive`. The research Python
   package requires Unix `fcntl`; use the already installed WSL distribution for
   its tests and audits. See [PC validation commands](../pc_demo/README.md).
3. Stage only reviewed source/docs/tests explicitly. Run `python -m pc_demo audit-git`
   and `git diff --cached --check`, plus `python3 -m media_scout audit-publication`
   under WSL. Models, executables, environments, media, machine
   paths and run evidence must remain in ignored `pc_demo/.local/`.
4. Commit with the GitHub noreply identity, push the branch, and create or update
   a PR to main. Use a body file with validation evidence and attach the PR to
   the owning chat. Verify the exact head SHA and its Linux and Windows CI jobs.
5. Merge normally with the matching head commit, respecting required reviews and
   checks. Fetch and fast-forward local main; verify the CI run on that exact
   merged commit, including the existing Pages deployment. Never bypass branch
   protection or force-push. Remove the completed branch after the merge.

Main CI continues to deploy only `public/`; PC sources do not become website
assets. Source sync does not transfer ignored app installations or video drafts.
The Mac refreshes its own existing edition checkpoint when it next handles
publication maintenance. No PC research or demo scheduler is created by sync.
