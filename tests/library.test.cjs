const test = require("node:test");
const assert = require("node:assert/strict");
const {matches, searchText, primaryVersion, sortTools, coverageText, savedIds,
       comparisonSelection, comparisonRows, shortlistJSON, importShortlist,
       researchNotes} = require("../media_scout/ui/library.js");
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
    summary: "Independent output evidence is missing.", sources: [], checks: {}, caveats: []}};
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
