# Automatic local cleanup

Cleanup is part of the existing 8:00 AM Eastern chat workflow. Run it after a
completed, verified daily delivery or the verified already-sent/weekly-maintenance
path. It never researches, publishes, prepares email or sends a message.

```sh
# Preview: no files are removed.
python3 -m media_scout cleanup
# Include individual paths and retained-source proofs.
python3 -m media_scout cleanup --full
# Apply the same bounded policy while Scout is idle.
python3 -m media_scout cleanup --apply
```

The command removes only:

- Python bytecode and Finder metadata in source/test trees older than one day.
- Abandoned `.scout-xxxxxxxx` atomic-write temporary files older than one day in
  the local state/cache directories.
- Recognized HTTP-cache entries unused for 60 days. Validated cache reads refresh
  their access timestamp, preserving frequently reused ETags and GitHub savings.
- Redundant, unsealed `*metadata*.json` working copies directly in a completed
  edition's research directory. The edition must be at least seven days old,
  have a sent receipt and a synced publication checkpoint, and the working copy
  must have been untouched for a day. Every repository record must match a record
  in that edition's retained, SHA-256-verified sealed query files. Only raw arrays,
  repository maps and recognized count-only wrappers qualify. Unique annotations,
  unfamiliar formats and unproven copies are kept.

All tracked files and all paths in every local report manifest are excluded.
Sealed reports, source evidence, discovery observations, query archives, catalogs,
review queues, quality research, delivery/outbox records, publication history,
settings, Git history, local libraries and PC runtimes/media remain on disk.
Cleanup does not rewrite archive files, follow symlinks or remove hardlinks.

The idle lock prevents overlap with a Scout operation. Reserved/uncertain sends
and unfinished dated research or sealed editions/publications block cleanup. Corrupt manifests or
changed query evidence also block it. Apply recomputes the plan under the lock,
rechecks source provenance and verifies each candidate's identity and hash before
unlinking it. A changed candidate is kept and reported; partial cleanup exits 1.

Each applied run keeps a private journal under `state/cleanup/`, containing the
candidate paths, hashes, retained-source proofs, deletion totals and any errors.
It records an in-progress plan before deletion, checkpoints progress and records
the final result. These journals never enter Git or the public site. A preview
creates no cleanup journal. Byte totals describe removed file contents; actual
free disk space can differ because of filesystem allocation and snapshots.

An additional private cache remembers only keep decisions, bound to the working
copy and manifest hashes. It avoids repeating expensive comparisons of unchanged
unproven files. This cache can never authorize a deletion; changed files are
examined again.

Unknown files are retained deliberately. Large research archives can continue to
grow: they support citations, license decisions, recovery and sealed-report
verification. Do not use broad directory deletion or a generic Git clean command
to reduce that archive. No additional scheduler, GitHub workflow, retention rule
for reports, or email is introduced.
