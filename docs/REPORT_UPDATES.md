# Requested same-day report updates

Use this workflow only when the owning user requests an update to a completed
edition. Keep the original local and public report files, source evidence and
delivery receipt. Each update receives its own seal and immutable public folder;
it joins the existing library, repository and scheduler.

Prepare revision 2 (the first update) from the current research configuration and
history. The workspace lives under ignored `state/report_updates/YYYY-MM-DD/r2/`.
Preparation is resumable and copies no delivery or outbox state.

```sh
python3 -m media_scout prepare-update --date YYYY-MM-DD --revision 2
python3 -m media_scout plan --date YYYY-MM-DD --revision 2
python3 -m media_scout discover --date YYYY-MM-DD --revision 2
python3 -m media_scout verify-search --date YYYY-MM-DD --revision 2
```

Research the full expanded plan and retained backlog. `--plan` can add terms
before collection; the normal frozen-plan checks apply after collection starts.
Use `add-repository`, `review-license`, `add-project`, and `review-backlog` with
the same date and revision. Keep editorial JSON and additional evidence inside
that workspace. Follow DAILY_WORKFLOW.md for creative AI relevance, complete
software licenses, requirements, source-group checks and honest search gaps.
Do not recycle unchanged recommendations merely to increase the count.

```sh
python3 -m media_scout build --revision 2 --editorial state/report_updates/YYYY-MM-DD/r2/research/YYYY-MM-DD/editorial.json
python3 -m media_scout verify --date YYYY-MM-DD --revision 2
python3 -m media_scout export-update --date YYYY-MM-DD --revision 2
python3 -m media_scout verify-public-archive
```

The workspace declares its revision; the builder and exporter check it. The
exporter requires the original public edition and appends
`public/reports/YYYY-MM-DD/updates/r2/`. It refreshes the cumulative library,
review queue and source catalog, preserving earlier editions and source paths.
An existing update cannot be overwritten; use the next revision for another
explicitly requested update.

Stage only reviewed code/documentation, new finished exports and derived public
library files. Follow GITHUB_SYNC.md: audit, protected PR, exact PR-head CI,
normal merge, exact merged-main CI and successful Pages deployment. Then refresh
the original edition's `record-sync` and `verify-sync`; the checkpoint also covers
all published update files. Preserve previous checkpoints in local history.

Research revision flags are not available on delivery commands. Publishing an
update does not reset the one-email-per-day reservation or original send receipt.
Do not automatically resend a report that is already sent.
