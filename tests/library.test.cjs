const test = require("node:test");
const assert = require("node:assert/strict");
const {matches, searchText, primaryVersion, sortTools, coverageText} = require("../media_scout/ui/library.js");
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
