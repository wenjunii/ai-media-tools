# Searchable tool library and GitHub Pages

Live site: **https://wenjunii.github.io/ai-media-tools/**

The web UI and its downloadable `library.json` are generated from every finished
edition under `public/reports/`. They include complete researched profiles and
the report's screened open-source AI discoveries. Unreviewed collector results
and private research remain in the local discovery catalog and review queue.

## Search and compare

- Search names, creative uses, hardware/software requirements, install commands,
  model/license terms, and older reviews. Words combine; quotes match a phrase.
- Combine creative-field, platform-mention, software-license, review-depth,
  and daily-edition filters. Platform mentions do not certify platform support.
- Sort by latest detailed review, first appearance, or name.
- Open a tool for its introduction, practical uses, demos, installation, first
  project, requirements, licenses/costs, quality assessment, limitations and sources.
- Choose a version in Review history. Profiles disclose their documentation-check
  date. A brief subsequent mention does not replace a complete guide.
- Copy a profile link to return to the tool and chosen review. Search/filter
  settings are also represented in the URL.
- Browse preserved editions through Daily reports, or download the cumulative
  library JSON for your own analysis.

One library entry is kept per stable tool ID. Every published dated review remains
in `versions`; profile completion promotes a screened lead without duplicating it.
New category labels are included in future reports. Older editions keep their
original bytes. Results load 24 at a time, with no fixed collection size limit.
The initial October 1 edition's 12 guides predate expanded-search tracking.
The UI identifies that fact. New daily editions execute the entire expanded
plan and display field/query counts, raw source/model candidates and source gaps
on their report cards. Library totals represent complete guides and screened
discoveries; raw candidates await eligibility checks and remain local.
Each daily export publishes all eligible profiles and screened leads from that
edition. Later full reviews replace pending status while preserving earlier versions.

## Local use and regeneration

```sh
python3 -m media_scout build-library
python3 -m media_scout verify-public-archive
python3 -m http.server 8766 --bind 127.0.0.1
# Open http://127.0.0.1:8766/site/
```

`build-library` refreshes `public/index.html`, `public/library.json`,
`public/assets/`, `public/.nojekyll`, `public/README.md`, and the local `site/`
view. It reads existing public editions and never recollects research, rebuilds
a report, prepares an email, or changes a delivery receipt. It works in a fresh
clone without private evidence, configuration overrides, or GitHub access.

Daily `build` prepares a local preview from sealed editions. Daily `export-report`
updates the cumulative public and local library after adding the finished edition.
A fresh checkout retains older public tools even when its private catalog is empty.
The library uses relative URLs and embedded data, so it works at a GitHub Pages
project path and from local files. There is no remote search API, database,
analytics tracker, external font service or JavaScript build dependency.

The editable UI source is `media_scout/ui/`; cumulative data logic is in
`media_scout/library.py`. After changes, regenerate the derived library, run
Python tests and `node --test tests/library.test.cjs`, then verify the archive.
The public verifier recomputes all derived files and rejects stale data or missing
assets before publication.

## GitHub Pages deployment

Set the repository's Pages publishing source to **GitHub Actions**. This project
uses the [official custom-workflow approach](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
The destination is a project site at `https://OWNER.github.io/REPOSITORY/`.
For a fork, update `github_sync.repository`, the documented live-site links,
and enable Pages in that repository.

The existing `ci.yml` workflow checks pull requests and main. After a main push:

1. Python 3.10 and 3.13 pass regression, compilation, archive and search checks.
2. The Pages job uploads **only `public/`**, using pinned official actions.
3. The `github-pages` environment deploys the static library.
4. The successful main CI run permits `record-sync` and `verify-sync`.
5. The existing daily workflow can then send its report email once.

Use the `github-pages` environment with deployment restricted to protected
branches, including protected main. PRs never deploy. A failed deploy leaves
the prior live site intact and blocks the current publication checkpoint/email.
After repairing setup, rerun the failed main-push workflow; a passing manual
dispatch alone does not replace the required main-push CI record.

No second research scheduler or Pages branch is needed. Each reviewed main sync
publishes the library automatically; private preferences, research, catalogs,
outbox payloads and receipts are excluded from both Git and the Pages artifact.
