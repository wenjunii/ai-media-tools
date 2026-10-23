const test = require("node:test");
const assert = require("node:assert/strict");
const {matches, searchText, primaryVersion, sortTools, coverageText, savedIds,
       comparisonSelection, comparisonRows, shortlistJSON, importShortlist,
       researchNotes, queryTerms, searchIndex, searchDetails, librarySearch, deferredAction} = require("../media_scout/ui/library.js");
const tool = {
  id: "github:example/paint", name: "Café Paint", categories: ["images", "video"],
  platform_mentions: ["Linux", "Browser"], review: "profile", profile_date: "2026-10-02", first_seen: "2026-10-01",
  versions: [
    {date: "2026-10-02", kind: "profile", profile: {name: "Café Paint", categories: ["video"], license: {code: "Apache-2.0"}, requirements: {platforms: "Browser", hardware: "8 GB"}, installation: {commands: ["paint --animate"]}}},
    {date: "2026-10-01", kind: "profile", profile: {name: "Café Paint", categories: ["images"], license: {code: "MIT"}, requirements: {platforms: "Linux"}, introduction: {text: "Original texture workflow"}}}
  ]
};
test("search includes installation, hardware and historical creative uses", () => {
  for (const q of ["paint --animate", '"8 GB"', "original texture", "cafe"]) assert.ok(matches(tool, {q}));
  assert.equal(matches(tool, {q: "paint absent"}), false);
  assert.equal(matches(tool, {q: "   "}), true);
});
test("combined filters use the selected edition's actual review", () => {
  assert.ok(matches(tool, {edition: "2026-10-01", field: "images", platform: "Linux", license: "MIT", review: "profile"}));
  assert.equal(matches(tool, {edition: "2026-10-01", field: "video"}), false);
  assert.equal(matches(tool, {edition: "2026-10-02", platform: "Linux"}), false);
  assert.equal(matches(tool, {edition: "2026-10-03"}), false);
  assert.equal(matches(tool, {license: "MIT"}), false);
});
test("cached full text produces the same results as live text", () => {
  assert.equal(matches(tool, {q: "original"}, searchText(tool)), matches(tool, {q: "original"}));
});
test("edition-scoped search cannot match another review even with an all-review cache", () => {
  assert.equal(matches(tool, {edition: "2026-10-02", q: "original texture"}, searchText(tool)), false);
  assert.equal(matches(tool, {edition: "2026-10-01", q: '"8 GB"'}, searchText(tool)), false);
  assert.equal(matches(tool, {edition: "2026-10-02", q: '"8 GB"'}), true);
  assert.equal(matches(tool, {edition: "2026-10-01", q: "original texture"}), true);
  assert.equal(matches(tool, {q: "original texture"}), true);
});
test("browsing without a query does not inspect full-text sections", () => {
  const profile = {...tool.versions[0].profile};
  Object.defineProperty(profile, "introduction", {enumerable: true, get() { throw new Error("Full-text index was read"); }});
  const browse = {...tool, versions: [{...tool.versions[0], profile}]};
  const find = librarySearch([browse]);
  assert.deepEqual(find({q: "", platform: "Browser", sort: "name"}).results.map(t => t.id), [tool.id]);
  assert.deepEqual(find({q: "  ", platform: "Windows"}).results, []);
});
test("repeated searches reuse results without leaking an old edition or filter", () => {
  const find = librarySearch([tool], new Map([["images", "Still artwork"]]));
  const filters = {q: "original texture", sort: "relevance"}, first = find(filters);
  assert.deepEqual(first.results.map(t => t.id), [tool.id]);
  assert.equal(first.details.get(tool.id).edition, "2026-10-01");
  assert.equal(find({...filters}), first);
  assert.deepEqual(find({...filters, edition: "2026-10-02"}).results, []);
  assert.deepEqual(find({...filters, quality: "recommended"}).results, []);
  assert.equal(find({q: '"Still artwork"', edition: "2026-10-01"}).details.get(tool.id).edition, "2026-10-01");
  assert.deepEqual(find({q: "missing"}).results, []);
  assert.equal(find({q: "", sort: "name"}).results.length, 1);
});
test("saved-only search responds to changes in the same saved Set", () => {
  const second = {...tool, id: "github:example/second", name: "Another tool"};
  const find = librarySearch([tool, second]), selected = new Set([tool.id]), filters = {q: "paint", sort: "name"};
  assert.deepEqual(find(filters, selected).results.map(t => t.id), [tool.id]);
  selected.add(second.id);
  assert.deepEqual(find(filters, selected).results.map(t => t.id), [second.id, tool.id]);
  selected.clear();
  assert.deepEqual(find(filters, selected).results, []);
  assert.equal(find(filters, null).results.length, 2);
});
test("typing bursts use the latest query; Enter flushes and reset cancels delayed work", () => {
  let now = 0, serial = 0, query = "", seen = [];
  const jobs = new Map(), timers = {
    setTimeout(fn, delay) { const id = serial++; jobs.set(id, {at: now + delay, fn}); return id; },
    clearTimeout(id) { jobs.delete(id); }
  };
  function advance(ms) {
    now += ms;
    for (const [id, job] of jobs) if (job.at <= now) { jobs.delete(id); job.fn(); }
  }
  const schedule = deferredAction(() => seen.push(query), 150, timers);
  query = "b"; schedule(); advance(100);
  query = "blender"; schedule(); advance(149);
  assert.deepEqual(seen, []);
  advance(1); assert.deepEqual(seen, ["blender"]);
  query = "music"; schedule(); schedule.flush(); advance(200);
  assert.deepEqual(seen, ["blender", "music"]);
  query = "old"; schedule(); schedule.cancel(); query = ""; advance(200);
  assert.deepEqual(seen, ["blender", "music"]);
  schedule.flush(); assert.equal(seen.length, 2);
});
test("saved tools restore only known unique IDs and recover from invalid browser data", () => {
  assert.deepEqual(savedIds(JSON.stringify([tool.id, tool.id, "github:missing/tool", null, {}]), [tool]), [tool.id]);
  for (const invalid of [null, "broken JSON", "{}", '"a string"']) assert.deepEqual(savedIds(invalid, [tool]), []);
  const many = Array.from({length: 50}, (_, i) => ({...tool, id: "github:example/tool" + i}));
  assert.equal(savedIds(JSON.stringify(many.map(t => t.id)), many).length, 50);
});
test("shortlists transfer every save between libraries and merge without replacing existing saves", () => {
  const many = Array.from({length: 60}, (_, i) => ({...tool, id: "github:example/tool" + i}));
  const transfer = shortlistJSON(new Set(many.map(t => t.id)), many);
  const current = new Set([tool.id, many[0].id]);
  const result = importShortlist(transfer, current, [tool, ...many]);
  assert.equal(result.added, 59);
  assert.equal(result.existing, 1);
  assert.equal(result.ids.length, 61);
  assert.deepEqual(result.missing, []);
  assert.deepEqual(Array.from(current), [tool.id, many[0].id]);
  assert.deepEqual(Object.keys(JSON.parse(transfer)), ["format", "version", "tool_ids"]);
  assert.equal(importShortlist(transfer, result.ids, [tool, ...many]).added, 0);
});
test("shortlist imports report missing tools, count duplicates once, and never accept imported profiles", () => {
  const payload = {format: "ai-media-scout-shortlist", version: 1,
    tool_ids: [tool.id, tool.id, "github:missing/tool", "github:missing/tool"],
    profiles: [{...tool, name: "An imported replacement"}]};
  const before = JSON.stringify(tool);
  const result = importShortlist(JSON.stringify(payload), [], [tool]);
  assert.deepEqual(result, {ids: [tool.id], added: 1, existing: 0, missing: ["github:missing/tool"]});
  assert.equal(JSON.stringify(tool), before);
});
test("malformed and unsupported shortlist imports fail without mutating saves", () => {
  const current = new Set([tool.id]);
  for (const value of ["broken", "null", "[]", JSON.stringify({format_version: 1, tools: [tool]}),
      ...[2, "1"].map(version => JSON.stringify({format: "ai-media-scout-shortlist", version, tool_ids: [tool.id]})),
      ...[[tool.id, null], [tool.id, {}], [tool.id, " "]].map(tool_ids => JSON.stringify({format: "ai-media-scout-shortlist", version: 1, tool_ids}))]) {
    assert.throws(() => importShortlist(value, current, [tool]), /shortlist/i);
    assert.deepEqual(Array.from(current), [tool.id]);
  }
  assert.deepEqual(importShortlist(shortlistJSON([], [tool]), current, [tool]).ids, [tool.id]);
});
test("research notes preserve dated full guidance, commands and citations instead of a later brief mention", () => {
  const full = {...tool.versions[0], edition_id: "2026-10-02-r2", revision: 2, profile: {...tool.versions[0].profile,
    checked_on: "2026-10-02", quality: {text: "Review scope", hands_on_tested: false},
    installation: {text: "Developer instructions", steps: ["Install Python"], commands: ["paint --animate"], source_urls: ["https://example.com/install"]},
    license: {code: "Apache-2.0", weights: "Research-only weights", commercial: "Review separate model terms", cost: "Optional paid host"},
    sources: [{title: "Install docs", url: "https://example.com/install"}], links: {demo: "https://example.com/demo"}}};
  const revised = {...tool, versions: [{date: "2026-10-03", kind: "screened", profile: {name: "Later mention"}}, full]};
  const labels = {installation: "Install", requirements: "Hardware & software", license: "License", quality: "Quality"};
  const notes = researchNotes([tool.id], [revised], labels);
  for (const value of ["2026-10-02-r2", "Documentation checked: 2026-10-02", "8 GB", "Browser", "Apache-2.0",
      "Research-only weights", "Review separate model terms", "Optional paid host", "Install Python", "paint --animate", "https://example.com/install", "https://example.com/demo"]) {
    assert.ok(notes.includes(value), value);
  }
  assert.ok(notes.includes("**Software:** Not documented"));
  assert.match(notes, /not independently tested/);
  assert.doesNotMatch(notes, /Later mention/);
});
test("research notes export only saved tools and keep pending requirements and testing claims explicit", () => {
  const lead = {id: "github:example/lead", name: "Audio lead", versions: [{date: "2026-10-02", kind: "screened", profile: {
    name: "Audio lead", checked_on: "2026-10-02", good_for: "Voice editing", code_license: "MIT", review_status: "Needs installation review",
    ai_relevance: {text: "Neural voice editing", source_urls: ["https://example.com/ai"]},
    sources: [{title: "License", url: "https://example.com/license"}]}}]};
  const notes = researchNotes([lead.id], [tool, lead], {});
  assert.match(notes, /1 saved tool\./);
  assert.match(notes, /full profile pending/);
  assert.match(notes, /model-weight terms, commercial use and costs: not reviewed yet/);
  assert.match(notes, /Neural voice editing/);
  assert.match(notes, /https:\/\/example.com\/license/);
  assert.doesNotMatch(notes, /Café Paint|paint --animate/);
  const tested = {...tool, versions: [{...tool.versions[0], profile: {...tool.versions[0].profile, quality: {hands_on_tested: true}}}]};
  assert.match(researchNotes([tested.id], [tested], {}), /Hands-on testing recorded; see the quality review for its scope/);
});
test("exported research text cannot break out of Markdown command fences or insert raw HTML", () => {
  const hostile = {...tool, versions: [{...tool.versions[0], profile: {...tool.versions[0].profile,
    name: "<img src=x> [untrusted]", installation: {text: "<script>untrusted</script>", commands: ["echo hello\n```\n# still a command"]}}}]};
  const notes = researchNotes([tool.id], [hostile], {installation: "Install"});
  assert.doesNotMatch(notes, /<img|<script>/);
  assert.ok(notes.includes("\\[untrusted\\]"));
  assert.ok(notes.includes("````text\necho hello\n```\n# still a command\n````"));
});
test("shared comparisons preserve exact review identities and reject missing or duplicated entries", () => {
  const second = {...tool, id: "github:example/second", versions: [
    {...tool.versions[0], date: "2026-10-01", revision: 2, edition_id: "2026-10-01-r2"}
  ]};
  const entries = [
    {id: tool.id, edition: "2026-10-01"}, {id: tool.id, edition: "2026-10-02"},
    {id: second.id, edition: "2026-10-01"}, {id: second.id, edition: "2026-10-01-r2"},
    {id: "github:missing/tool", edition: "2026-10-01"}, null
  ];
  assert.deepEqual(comparisonSelection(JSON.stringify(entries), [tool, second]), [
    {id: tool.id, edition: "2026-10-01"}, {id: second.id, edition: "2026-10-01-r2"}
  ]);
  for (const invalid of [null, "broken JSON", "{}"]) assert.deepEqual(comparisonSelection(invalid, [tool]), []);
  const many = Array.from({length: 6}, (_, i) => ({...tool, id: "github:example/tool" + i}));
  assert.equal(comparisonSelection(JSON.stringify(many.map(t => ({id: t.id, edition: "2026-10-02"}))), many).length, 4);
});
test("comparison distinguishes unknown requirements, pending reviews and software/model terms", () => {
  const p = {...tool.versions[0].profile, good_for: {text: "Animated paintings"},
    license: {code: "Apache-2.0", weights: "A separate research-only model", commercial: "Check model terms", cost: "Optional paid host", source_urls: ["https://example.com/license"]},
    quality: {hands_on_tested: false}};
  const rows = comparisonRows({kind: "profile", profile: p});
  const value = label => rows.find(row => row.label === label);
  assert.equal(value("Hardware").text, "8 GB");
  assert.equal(value("Software").text, "Not documented");
  assert.equal(value("Software license").text, "Apache-2.0");
  assert.equal(value("Model weights").text, "A separate research-only model");
  assert.deepEqual(value("Model weights").source_urls, ["https://example.com/license"]);
  assert.match(value("Review evidence").text, /not independently tested/);
  const leadRows = comparisonRows({kind: "screened", profile: {good_for: "Audio editing", code_license: "MIT",
    sources: [{title: "Complete software license", url: "https://example.com/license"}]}});
  assert.equal(leadRows.find(row => row.label === "Software license").text, "MIT");
  assert.deepEqual(leadRows.find(row => row.label === "Software license").source_urls, ["https://example.com/license"]);
  assert.match(leadRows.find(row => row.label === "Hardware").text, /full profile pending/);
  assert.match(leadRows.find(row => row.label === "Model weights").text, /full profile pending/);
});
test("later screened mention retains the complete guide as primary", () => {
  const later = {...tool, versions: [{date: "2026-10-03", kind: "screened", profile: {categories: ["audio"], code_license: "MIT"}}, ...tool.versions]};
  assert.equal(primaryVersion(later).date, "2026-10-02");
  assert.equal(primaryVersion(later, "2026-10-03").kind, "screened");
});
test("sort is deterministic and preserves the source library", () => {
  const older = {...tool, name: "Alpha", first_seen: "2026-09-01", profile_date: "2026-09-02"};
  const input = [older, tool];
  assert.equal(sortTools(input, "updated")[0], tool);
  assert.equal(sortTools(input, "added")[0], tool);
  assert.equal(sortTools(input, "name")[0], older);
  assert.equal(input[0], older);
});
test("best match puts a named tool before recent incidental mentions regardless of popularity or quality", () => {
  const mention = {...tool, id: "github:example/new", name: "Recent Editor", profile_date: "2026-10-17", stars: 100000,
    quality_assessment: {tier: "recommended"}, versions: [{date: "2026-10-17", kind: "profile", profile: {
      name: "Recent Editor", introduction: {text: "Use Café Paint as one of many alternatives. ".repeat(100)},
      license: {code: "MIT"}}}]};
  const input = [mention, tool], before = JSON.stringify(input);
  assert.equal(sortTools(input, "relevance", {q: '"cafe paint"'})[0], tool);
  assert.equal(sortTools(input, "updated", {q: "cafe paint"})[0], mention);
  assert.equal(sortTools(input, "relevance", {q: "  "})[0], mention);
  assert.equal(JSON.stringify(input), before);
});
test("creative uses rank above an incidental requirements mention without dropping either result", () => {
  const make = (id, fields) => ({...tool, id, versions: [{date: "2026-10-02", kind: "profile", profile: {
    name: "Editor", license: {code: "MIT"}, ...fields}}]});
  const use = make("github:example/use", {good_for: {text: "Designing textile patterns"}});
  const incidental = make("github:example/incidental", {requirements: {software: "Optional textile importer"}});
  const results = [incidental, use].filter(t => matches(t, {q: "textile"}));
  assert.deepEqual(sortTools(results, "relevance", {q: "textile"}), [use, incidental]);
  assert.deepEqual(searchDetails(use, {q: "textile"}).sections, ["Creative uses"]);
});
test("query parsing preserves accents, phrases and installation flags with no invented operators", () => {
  assert.deepEqual(queryTerms('Café cafe "8 GB" --animate'), ["cafe", "8 gb", "--animate"]);
  assert.ok(matches(tool, {q: '"8 GB" --animate'}, searchIndex(tool)));
  assert.ok(matches(tool, {q: "paint --animate"}, searchIndex(tool)));
  assert.equal(matches(tool, {q: '"GB 8"'}, searchIndex(tool)), false);
  assert.equal(searchDetails(tool, {q: "  "}).scope, "none");
});
test("match context identifies historical and same-day reviews without using another edition's evidence", () => {
  const revised = {...tool, versions: [
    {...tool.versions[0], date: "2026-10-01", revision: 2, edition_id: "2026-10-01-r2"}, tool.versions[1]
  ]}, index = searchIndex(revised);
  const older = searchDetails(revised, {q: "original texture"}, index);
  assert.equal(older.edition, "2026-10-01");
  assert.deepEqual(older.sections, ["Introduction"]);
  assert.equal(searchDetails(revised, {q: '"8 GB"'}, index).edition, "2026-10-01-r2");
  assert.equal(matches(revised, {q: "original texture", edition: "2026-10-01-r2"}, index), false);
  assert.equal(matches(revised, {q: '"8 GB"', edition: "2026-10-01"}, index), false);
  assert.equal(searchDetails(revised, {q: "paint", edition: "2026-10-01"}, index).edition, "2026-10-01");
});
test("queries spanning reviews disclose combined history and rank below a single matching review", () => {
  const query = {q: 'original "8 GB"'}, match = searchDetails(tool, query);
  assert.ok(matches(tool, query, searchIndex(tool)));
  assert.equal(match.scope, "history");
  assert.equal(match.edition, null);
  const complete = {...tool, id: "github:example/complete", versions: [{...tool.versions[0], profile: {
    ...tool.versions[0].profile, introduction: {text: "An original workflow with 8 GB"}}}]};
  assert.deepEqual(sortTools([tool, complete], "relevance", query), [complete, tool]);
});
test("current assessment matches are identified separately and cannot leak into edition searches", () => {
  const assessed = {...tool, quality_assessment: {tier: "unverified", checked_on: "2026-10-17",
    summary: "Independent provenance awaits confirmation."}}, query = {q: "provenance"}, index = searchIndex(assessed);
  assert.ok(matches(assessed, query, index));
  assert.equal(searchDetails(assessed, query, index).scope, "assessment");
  assert.equal(searchDetails(assessed, query, index).edition, null);
  assert.equal(matches(assessed, {...query, edition: "2026-10-01"}, index), false);
});
test("category names remain searchable within their actual edition and other filters still apply", () => {
  const index = searchIndex(tool, new Map([["images", "Still artwork"], ["video", "Moving picture"]]));
  assert.ok(matches(tool, {q: '"Still artwork"', edition: "2026-10-01", license: "MIT"}, index));
  assert.equal(matches(tool, {q: '"Still artwork"', edition: "2026-10-02"}, index), false);
  assert.equal(matches(tool, {q: '"Still artwork"', edition: "2026-10-01", license: "Apache-2.0"}, index), false);
  assert.deepEqual(searchDetails(tool, {q: '"Still artwork"'}, index).sections, ["Creative field"]);
});
test("cached match details preserve ordering, full guides win tied mentions and IDs break final ties", () => {
  const later = {...tool, versions: [{date: "2026-10-17", kind: "screened", profile: {name: tool.name}}, ...tool.versions]};
  assert.equal(searchDetails(later, {q: "cafe paint"}).edition, "2026-10-02");
  const second = {...tool, id: "github:example/zpaint"}, input = [second, tool], filters = {q: "paint"};
  const details = new Map(input.map(t => [t.id, searchDetails(t, filters, searchIndex(t))]));
  assert.deepEqual(sortTools(input, "relevance", filters, details), [tool, second]);
  assert.deepEqual(sortTools(input, "relevance", filters), [tool, second]);
  assert.equal(input[0], second);
});
test("legacy editions do not claim a completed expanded search", () => {
  assert.match(coverageText({}), /predates expanded search tracking/);
});
test("query attempts, raw candidates and source gaps remain distinct from profiles", () => {
  const text = coverageText({search_coverage: {fields: 30, attempted_github_queries: 189,
    planned_github_queries: 189, source_candidates: 2345, model_candidates: 100,
    failed_github_queries: 2, partial_github_queries: 1, failed_model_queries: 0,
    ecosystem_gaps: 1, truncated_github_queries: 5}});
  assert.match(text, /189\/189 repository queries attempted/);
  assert.match(text, /2,345 source candidates/);
  assert.match(text, /4 source gaps/);
  assert.match(text, /5 bounded repository queries/);
  assert.match(text, /Candidates require review/);
});

test("same-day updates have independent filters and preserved original reviews", () => {
  const revised = {...tool, versions: [
    {...tool.versions[0], date: "2026-10-01", revision: 2, edition_id: "2026-10-01-r2"}, tool.versions[1]
  ]};
  assert.equal(primaryVersion(revised, "2026-10-01-r2").profile.license.code, "Apache-2.0");
  assert.equal(primaryVersion(revised, "2026-10-01").profile.license.code, "MIT");
  assert.ok(matches(revised, {edition: "2026-10-01-r2", field: "video"}));
  assert.equal(matches(revised, {edition: "2026-10-01", field: "video"}), false);
  assert.equal(matches(revised, {edition: "2026-10-01-r3"}), false);
});

test("quality confidence is separate from guide depth and follows current curation", () => {
  const experimental = {...tool, quality_assessment: {tier: "experimental", checked_on: "2026-10-10",
    summary: "The maintainer describes an unfinished prototype.", sources: [], checks: {}, caveats: []}};
  assert.ok(matches(experimental, {review: "profile", quality: "experimental"}));
  assert.equal(matches(experimental, {quality: "recommended"}), false);
  assert.ok(matches(experimental, {quality: "experimental", edition: "2026-10-01"}));
  assert.ok(matches(tool, {quality: "unverified"}));
  assert.equal(matches(tool, {quality: "recommended"}), false);
});
test("comparison and saved notes disclose current quality separately from preserved reviews", () => {
  const assessed = {...tool, quality_assessment: {tier: "unverified", checked_on: "2026-10-10",
    summary: "Reproduction and independent use remain unverified.", scope: "Stored documentation review only.",
    checks: {independent_use: {status: "unknown", note: "No direct evidence of independent creative use.", source_urls: []}},
    sources: [{title: "Reviewed source", url: "https://example.com/quality"}], caveats: ["No runtime testing was performed."]}};
  const rows = comparisonRows(primaryVersion(assessed, "2026-10-01"), assessed);
  const quality = rows.find(row => row.label === "Current quality assessment");
  assert.match(quality.text, /Quality unverified.*2026-10-10/);
  assert.deepEqual(quality.source_urls, ["https://example.com/quality"]);
  const notes = researchNotes([assessed.id], [assessed], {});
  for (const value of ["Current library quality assessment", "2026-10-10", "Stored documentation review only.", "No runtime testing was performed."])
    assert.ok(notes.includes(value));
  assert.match(notes, /Edition: 2026-10-02/);
});
test("missing-evidence filters combine with quality and historical editions using current assessment gaps", () => {
  const assessed = {...tool, evidence_gaps: ["results", "independent_use"],
    quality_assessment: {tier: "unverified"}};
  const before = JSON.stringify(assessed);
  assert.ok(matches(assessed, {evidence: "independent_use", quality: "unverified", edition: "2026-10-01", field: "images"}));
  assert.ok(matches(assessed, {evidence: "results", q: "paint"}));
  assert.equal(matches(assessed, {evidence: "setup"}), false);
  assert.equal(matches(assessed, {evidence: "results", quality: "recommended"}), false);
  assert.equal(matches(assessed, {evidence: "results", edition: "2026-10-03"}), false);
  assert.equal(matches(assessed, {evidence: "unknown-check"}), false);
  assert.equal(JSON.stringify(assessed), before);
});
test("evidence filtering uses backend provenance decisions and never infers gaps from stars or guide length", () => {
  const provenanceGap = {...tool, evidence_gaps: ["independent_use"], stars: 100000,
    quality_assessment: {tier: "unverified", checks: {independent_use: {status: "verified", source_kind: "maintainer"}}}};
  assert.ok(matches(provenanceGap, {evidence: "independent_use", review: "profile"}));
  assert.equal(matches({...provenanceGap, evidence_gaps: []}, {evidence: "independent_use"}), false);
  assert.ok(matches({...tool, evidence_gaps: []}, {evidence: ""}));
  assert.equal(matches(tool, {evidence: "results"}), false); // Older exported data cannot invent an assessment.
});
test("ready to try can be filtered while comparison and notes disclose pending creative results", () => {
  const assessed = {...tool, quality_assessment: {tier: "ready_to_try", checked_on: "2026-10-10",
    summary: "The five other checks have cited evidence.", scope: "Source review of an image-editing workflow.",
    checks: {results: {status: "unknown", note: "Creative results have not yet been reviewed.", source_urls: []}},
    sources: [], caveats: ["Output quality is still pending review."]}};
  assert.ok(matches(assessed, {quality: "ready_to_try", review: "profile", edition: "2026-10-01"}));
  assert.equal(matches(assessed, {quality: "recommended"}), false);
  assert.equal(matches(tool, {quality: "ready_to_try"}), false);
  const row = comparisonRows(primaryVersion(assessed, "2026-10-01"), assessed)
    .find(item => item.label === "Current quality assessment");
  const notes = researchNotes([assessed.id], [assessed], {});
  for (const text of [row.text, notes]) {
    assert.match(text, /Ready to try.*2026-10-10/);
    assert.match(text, /creative-result review pending/);
    assert.match(text, /Our own demo is not required/);
  }
  assert.match(notes, /results.*unknown/);
  assert.match(notes, /Edition: 2026-10-02/);
});

test("experimental reasons remain visible and cited in comparisons and exported notes", () => {
  const reason = {text: "The project format is unstable; <prototype> text is not markup.",
    source_urls: ["https://example.com/release-notes"]};
  const assessed = {...tool, quality_assessment: {tier: "experimental", checked_on: "2026-10-10",
    summary: "An unfinished export pipeline is documented.", scope: "Current prototype release.",
    experimental_reason: reason, checks: {}, caveats: ["No local execution."],
    sources: [{title: "Maintainer release notes", url: reason.source_urls[0]}]}};
  const row = comparisonRows(primaryVersion(assessed), assessed)
    .find(item => item.label === "Current quality assessment");
  assert.match(row.text, /Why Experimental: The project format is unstable/);
  assert.ok(row.source_urls.includes(reason.source_urls[0]));
  const notes = researchNotes([assessed.id], [assessed], {});
  assert.match(notes, /### Why Experimental/);
  assert.ok(notes.includes(reason.source_urls[0]));
  assert.match(notes, /&lt;prototype&gt;/);
  assert.ok(!notes.includes("<prototype>"));
});
