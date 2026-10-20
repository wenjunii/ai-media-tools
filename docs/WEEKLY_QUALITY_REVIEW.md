# Weekly review of the whole library

The existing Mac chat automation starts a new review week every **Monday at
8:00 AM America/New_York**, beginning **October 26, 2026**. It continues unfinished
reviews during later daily runs. There is one scheduler and no new GitHub Actions
schedule. Research starts at that time; a completed full-library review is not
promised at 8:00 AM.

Review **every published library entry**, including full profiles, screened leads,
Recommended, Ready to try, Quality unverified and Experimental tools, on every
platform and from every source host. New eligible discoveries join automatically.
Unscreened raw candidates still belong to the separate discovery/eligibility queue.
There is no weekly tool quota or fixed sample.

## Inspect coverage before work

Read today's `status` first and follow the daily delivery/resume rules. Then run:

```sh
python3 -m media_scout weekly-quality
python3 -m media_scout weekly-quality --full
# Explicit local date for reproducible inspection:
python3 -m media_scout weekly-quality --date YYYY-MM-DD --full
```

These commands are read-only, make no network requests and do not assign labels.
They recompute coverage from the complete published library and the current bound
quality reviews, including changes not yet published. `state` is `scheduled` before
the first Monday, `due` while tools remain, `complete` when every current record has
a cited source review dated within the current Monday-to-Sunday week, `empty`
for an empty library, or `disabled` if the schedule is off. The CLI uses the
configured local date, so daylight-saving changes do not shift the review weekday.

`total`, `reviewed_this_week`, `remaining` and `remaining_by_tier` cover all tools.
The full output lists all pending tools in oldest-source-review order, with exact
record bindings, current labels and **all six checks to refresh**, including checks
previously marked verified. This differs from `quality-backlog`, which focuses on
evidence gaps and excludes Recommended entries.

A correctly bound, cited source review completed during this week's daily research
already counts; do not repeat it just to produce a weekly record. Published-record
audits, uncited assessments, missing dates, future dates and stale bindings never
earn coverage. `future_assessment_ids` requires investigation, not a date change
without research. Updating a date alone is not a source check.

Coverage counts describe recorded assessments, not proof that all six checks
passed or that an app was run. An honest review can finish with unresolved gaps
and retain Quality unverified. An unavailable source must be documented as such,
with affected checks left unknown and dated attempts archived. An entry that has
not actually been reviewed remains pending. Never report the whole library checked
while `remaining` is nonzero. A new Monday makes older reviews due again; unfinished
tools remain in the queue, ordered ahead of more recently reviewed tools.

## Review the evidence and record supported labels

1. Read [QUALITY_POLICY.md](QUALITY_POLICY.md). Recheck the current full software
   license, scoped creative results, installation/first-use instructions,
   maintenance/support, independent first-hand use and model/service/cost terms.
   Check the cited Experimental reason in its current context. Preserve platform
   limits and distinguish software terms from weights, datasets and paid hosts.
2. Review live primary sources plus independent use evidence. Archive dated
   snapshots, source URLs, findings and failed attempts under ignored
   `state/quality_research/YYYY-MM-DD/`. Reuse freshly validated evidence from
   this week's daily research where it actually covers the same workflow.
   Use the existing conditional GitHub cache for supported API reads; an
   unchanged push date or star count never substitutes for the checks.
   Avoid repeating full discovery just for quality maintenance.
3. Explicitly select a supported label. Recommended needs all six verified checks
   and a full profile. Ready to try needs the five non-results checks and a full
   profile; results remain unknown or documented. Both need independent use.
   Other evidence gaps remain Quality unverified. Experimental needs current,
   cited prototype, instability or unfinished-work evidence. Our own demo is
   unnecessary. Do not install or execute discovered applications.
4. Prepare complete assessments in the existing
   [review batch format](QUALITY_POLICY.md#applying-reviewed-assessments), bound to
   each latest published record. Use the actual review date. Include upgrades,
   downgrades, reopened checks and unchanged labels where a fresh review supports
   them. Retain specific scope and caveats; never mark every check verified merely
   to finish the queue.

```sh
python3 -m media_scout record-quality-reviews --file state/quality_research/DATE/reviews.json
# Inspect proposed labels, dates, citations and reopened/closed checks, then:
python3 -m media_scout record-quality-reviews --file state/quality_research/DATE/reviews.json --apply
python3 -m media_scout build-library
python3 -m media_scout verify-public-archive
python3 -m media_scout weekly-quality --full
```

The source-review agent checks evidence truth; the commands validate structure
and record bindings. Preserve a before/after coverage summary locally. Report the
number reviewed, remaining, labels changed, important regressions and source gaps.
Continue the pending set on later daily runs without silently treating a partial
pass as complete.

## Publish with the existing daily flow

When a new daily edition is being prepared, perform the weekly review before its
protected publication and include the reviewed curation and regenerated library
in that same PR. This avoids an additional weekly deployment when the work can
share the daily publication. Verify the archive, full Git index, exact PR-head CI,
merged-main push CI and Pages; refresh and verify the edition's sync checkpoint.
Email remains after verified publication, exactly once.

If today's report is already sent, skip discovery, report building and email.
Due weekly work may continue as library maintenance and use the same protected
publication checks against the existing edition. Resolve unfinished publication
or uncertain delivery through the existing runbook before changing its state;
never resend an edition for a quality update. Sealed reports and sent receipts
remain unchanged. Current labels, evidence and dates appear in the local library
and GitHub Pages after publication.

If all weekly work is current and the daily report is already complete, verify
and stop quietly. Surface partial coverage, meaningful findings, failures or
required action; never claim that scheduling a task has completed its review.

The public `weekly_quality_review` configuration contains `enabled` and a Monday
`starts_on` date. It is a due-work gate for the existing chat automation, not a
standalone background process. It does not add email recipients or authorize
separate weekly email delivery.
