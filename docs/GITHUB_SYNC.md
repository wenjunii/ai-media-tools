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
downloaded and opened locally; this workflow does not configure website hosting.

The original `reports/`, raw `research/`, local `site/`, private configuration,
catalogs, outbox payloads, and delivery/sync receipts remain ignored. The public
index uses report links relative to `public/`. When importing older local history,
export its verified editions before publishing an index that links to them.

## Publish through the protected branch

1. Inspect the report's status and preserve any sealed edition. Reconcile a
   reserved or uncertain email with confirmed Sent mail before further email work.
   An already-sent report must never be sent again. Check the current Git branch,
   working tree, configured destination, and any pending publication PR.
2. Export the finished report:

   ```sh
   python3 -m media_scout export-report --date YYYY-MM-DD
   ```

3. Start from current main, or resume the existing publication branch/PR. Use a
   branch such as `scout/report-YYYY-MM-DD` for a new edition. Preserve unrelated
   changes. Include public exports and only reviewed, authorized source/doc changes;
   stage those paths explicitly. Never force-add ignored research or state.

   ```sh
   git add public
   python3 -m media_scout audit-publication
   git diff --cached --check
   ```

   The audit checks the entire Git index for private operational paths, the local
   recipient/project path, known access-token patterns, and private-key material.
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

`prepare-email` repeats publication verification before creating its outbox and
send reservation. It records the verified GitHub commit and public report URL in
the local delivery receipt. Continue the Gmail delivery step in
`DAILY_WORKFLOW.md`, sending the exact complete reserved payload once.

A failed export, push, merge, CI run, or verification blocks email. Recover the
unfinished publication without rebuilding or recollecting a sealed report.
An uncertain Gmail result still requires mailbox reconciliation; a successful
GitHub sync never authorizes an email retry or alternate transport.
