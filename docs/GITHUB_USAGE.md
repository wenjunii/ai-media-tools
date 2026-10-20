# Reducing GitHub usage

Research, scheduling, the local library and email run on the Mac. GitHub remains
a research source, the public source/report archive and the GitHub Pages host.
The full expanded search, protected publication and publish-before-email order
are unchanged. This mode does not add a service, subscription or scheduler.

## Evidence reads

The first successful repository metadata, README, license, release or commit API
read can save a response body and ETag in ignored `state/http-cache/`. Subsequent
reads send `If-None-Match`. Only a fresh `304 Not Modified` response for that URL
permits reuse of a hash-checked body. A changed response replaces the cache.
No requests are skipped based on repository age, stars or a previous push date.

Authenticated 304 responses do not consume GitHub's primary REST rate limit.
They still make network requests and remain subject to other limits.
See [GitHub's conditional-request guidance](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#use-conditional-requests).
Savings depend on how many responses remain unchanged; the first run warms the
cache and is not expected to have the same benefit as later runs.

Search requests and Hugging Face queries always run live, with the same fields,
lanes and pagination. All per-query coverage records remain required.
A failed watchlist read is attempted once per repository in an observation;
other fields record that same failure explicitly. It is tried again in the next
new observation. This does not suppress failures or turn them into empty results.

GitHub's Contents API often includes the complete README or license. The collector
uses that body after validating its byte count and Git blob hash, avoiding a
second raw-file download. Missing, partial or invalid inline content falls back
to the official download URL. Every new profile or screened lead still needs the
complete archived license and an explicit editorial review.

Cache files contain response bodies, URLs, hashes and validators, never tokens or
request headers. A corrupt/unreadable cache causes an ordinary live request.
Cache write failures do not discard a successful live response. Timeouts,
authorization failures, rate limits, 404s and server errors never authorize stale
evidence. The cache can be removed while Scout is idle; it will repopulate.
It is separate from archived evidence and never enters Git or a public report.

## Publication CI

Every PR and main push runs `publication-checks`: public archive hashes, complete
derived library consistency and browser regression tests. A local Git diff selects
whether the Python 3.10/3.13 matrix and Windows PC suite are also needed.

| Change | Validation |
| --- | --- |
| Only known generated public files, quality-review data, README or Markdown docs | Publication checks |
| Source, tests, workflows, dependencies, PC files or an unknown path | Publication checks and full platform suites |
| Manual run, unavailable comparison base, empty/unverified diff | Publication checks and full platform suites |

The comparison covers all changed paths, including deletions, both sides of
renames and every commit in a push. A two-commit fetch normally contains the
comparison base for protected merges. If it does not, the full suite runs.
There is no GitHub API call to determine the changed-file list, no path-filtered
workflow that can leave required checks pending, and no change to branch protection.

Report-only publication uses **three runner jobs across PR and main**: PR
publication checks, main publication checks, and Pages deployment. The former
workflow used seven. Skipped platform jobs are visibly skipped, not described as
tests that ran. Source changes retain the full suites plus publication checks.
Local maintenance validation still runs the full regression suite.

New commits cancel superseded runs of the same PR. Main publication runs are
never automatically cancelled by that rule. Every merged main commit still
deploys the verified `public/` tree to Pages. The Pages upload has an explicit
one-day artifact retention period; Git history and the report archive persist.

`record-sync` and `verify-sync` check both the successful exact-main workflow and
its successful `deploy-pages` job. A skipped, missing or failed Pages job blocks
the checkpoint and email, even if the workflow summary is green.

## Measure the effect

For new observations, `discover` prints `request_usage`, also stored in
`research/YYYY-MM-DD/discovery.json`:

- `network_requests`: direct client requests across all collector source hosts;
  redirects can cause additional HTTP exchanges.
- `conditional_requests`: repository requests sent with a validated ETag.
- `not_modified`: successful fresh 304 validations, included in network requests.
- `downloaded_bytes`: response body bytes read by the client.
- `inline_documents`: complete document bodies used without a raw-file download.
- `watchlist_reuses`: repeated failed watchlist reads avoided within the observation.
- `cache_errors`: invalid/unreadable or unwritable cache entries.

These are collector-only counters; supplemental research, later `add-repository`
or `review-license` commands, publication and browser traffic are not included.
Older sealed observations have no counters and are not rewritten. CI run summaries
explain the selected validation path. Do not claim a measured percentage saving
before comparing real runs.

Standard GitHub-hosted runner minutes are free for public repositories. This
project's `ubuntu-latest` and `windows-latest` jobs use standard runners.
Artifact/cache storage and API limits are different resources.
See [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
Keeping the public repo and GitHub Pages necessarily retains some GitHub use.
