# Searchable tool library and GitHub Pages

Live site: **https://wenjunii.github.io/ai-media-tools/**

The web UI and its downloadable `library.json` are generated from every finished
edition under `public/reports/`, with current quality curation from
`config/quality_reviews.json`. They include complete researched profiles and
the report's screened open-source AI discoveries. Unreviewed collector results
and private research remain in the local discovery catalog and review queue.

## Search and compare

- Search names, creative uses, hardware/software requirements, install commands,
  model/license terms, and older reviews. Words combine; quotes match a phrase.
  Selecting a daily edition limits the dated profile filters and search text to that
  edition's review. Clear the edition to search all preserved reviews again.
- Combine creative-field, platform-mention, software-license, review-depth,
  and daily-edition filters. Platform mentions do not certify platform support.
- **Quality confidence** filters Recommended, Ready to try, Quality unverified and
  Experimental. Ready to try verifies the five checks other than creative results;
  result review remains pending and our own demo can happen later.
  It always uses the current assessment, even with an older edition selected.
  Cards show quality separately from review depth. The profile's **Evidence and
  remaining gaps** lists all six checks, citations, method, date and limitations.
  A detailed guide does not automatically earn a recommendation. See
  [QUALITY_POLICY.md](QUALITY_POLICY.md) for the criteria and retrospective audit.
- Sort by latest detailed review, first appearance, or name.
- Open a tool for its introduction, practical uses, demos, installation, first
  project, requirements, licenses/costs, quality assessment, limitations and sources.
- Choose a version in Review history. Profiles disclose their documentation-check
  date. A brief subsequent mention does not replace a complete guide.
- Copy a profile link to return to the tool and chosen review. Search/filter
  settings are also represented in the URL.
- Select **Save** on a card or profile to build a shortlist. **Saved tools**
  filters the library to that shortlist and works with the other filters.
  Saves persist in the browser on the same site; the local and Pages sites,
  different browsers and different devices keep separate shortlists. Saves
  have no collection-size limit. If browser storage is unavailable, the UI
  keeps the shortlist for the current tab and explains that it will not persist.
- Use **Move saved tools** to transfer all saves between browsers or devices.
  Download the shortlist JSON file, or copy it, then import it in the other
  library. Import merges matching tool IDs with existing saves, skips duplicates,
  and reports tools missing from that library. Update an older library and import
  again to recover missing tools. Invalid files leave existing saves unchanged.
  Transfer files contain only the format/version and tool IDs; importing cannot
  inject profiles, source links or installation instructions into the library.
- **Download research notes** exports all saved tools to Markdown, regardless of
  the current search filters. Each entry uses its latest available detailed guide,
  or latest screened discovery if no complete profile exists. The notes preserve
  edition IDs, documentation-check dates, installation/first-use steps, documented
  hardware/software/platform requirements, software and model terms, costs,
  testing disclosures, limitations and primary-source citations. Unknown values
  and pending research remain labeled. This is useful context for planning a PC
  experiment; it does not install a tool or claim it was tested.
  The current quality assessment is included separately from the dated guide.
- Select **Compare** on 2–4 cards or profiles, then use **Compare tools**.
  The table shows creative uses, hardware, software, platforms, software
  licenses, model terms, commercial-use notes, costs, maturity and review
  evidence, with source links. Missing published requirements stay **Not
  documented**; screened leads show **full profile pending** for unreviewed
  details. Comparison does not treat a platform mention as verified support.
  Each selection retains its dated review when you change filters.
  A separate current-quality row identifies the assessment date and evidence;
  it is not a claim about the quality label at the selected historical date.
- **Copy comparison link** includes the selected tool IDs and review editions
  so it opens the same comparison on another browser. Comparisons are encoded
  in the URL and do not require an account or a remote service. Saved-tool
  lists stay in browser storage and are not included in comparison links.
- Browse preserved editions through Daily reports, or download the cumulative
  library JSON for your own analysis.

Shortlist transfer is manual, not automatic device synchronization. Downloads
and imports run entirely in the browser. The transfer JSON selects tools, while
research notes capture the dated guidance available when exported; neither file
changes published reports. A later import uses the destination library's existing
reviews. Use a comparison link when you need to share specific review editions.

One library entry is kept per stable tool ID. Every published dated review remains
in `versions`; profile completion promotes a screened lead without duplicating it.
Requested same-day updates have separate edition IDs and are labeled “Update 1”,
“Update 2”, and so on. The original report and reviews remain accessible; filters,
profile links and report downloads select the requested revision.
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
cd /path/to/ai-media-tools
python3 -m media_scout build-library
python3 -m media_scout verify-public-archive
python3 -m http.server 8766 --bind 127.0.0.1
# Open http://127.0.0.1:8766/site/
```

Leave the terminal running and open the URL in a browser. Ctrl+C stops the
server. If port 8766 already serves this checkout, use its existing `/site/` URL.

`build-library` refreshes `public/index.html`, `public/library.json`,
`public/assets/`, `public/.nojekyll`, `public/README.md`, and the local `site/`
view. It reads existing public editions and never recollects research, rebuilds
a report, prepares an email, or changes a delivery receipt. It works in a fresh
clone without private evidence, configuration overrides, or GitHub access.
It also reads the public curation registry. Reassessments are bound to the exact
latest published record; a newer or changed record invalidates an older binding.
Current assessments sit outside preserved `versions` in library JSON. Use
`quality-backlog --full` for evidence gaps in existing profiles and leads, and
`audit-existing-quality --date YYYY-MM-DD` only for an intended conservative audit
of published records. Neither command manufactures recommendations or runtime tests.

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
