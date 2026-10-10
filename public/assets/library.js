/* Search is entirely local. Profile text is rendered as text, never executed. */
(function () {
  "use strict";
  function fold(value) {
    return String(value).normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
  }
  function searchText(value) {
    if (Array.isArray(value)) return value.map(searchText).join(" ");
    if (value && typeof value === "object") return Object.values(value).map(searchText).join(" ");
    return typeof value === "string" ? fold(value) : "";
  }
  function editionKey(entry) { return entry.edition_id || entry.report_date || entry.date; }
  function primaryVersion(tool, edition) {
    return (edition && tool.versions.find(function (v) { return editionKey(v) === edition; })) ||
      tool.versions.find(function (v) { return v.kind === "profile"; }) || tool.versions[0];
  }
  const qualityLabels = {recommended: "Recommended", ready_to_try: "Ready to try", unverified: "Quality unverified", experimental: "Experimental"};
  const readyToTryNote = "Five checks verified; creative-result review pending. Our own demo is not required.";
  function qualityOf(tool) {
    return tool && tool.quality_assessment || {tier: "unverified", checked_on: null,
      summary: "Quality evidence has not been assessed.", checks: {}, caveats: [], sources: []};
  }
  function qualityText(tool) {
    const value = qualityOf(tool);
    return qualityLabels[value.tier] + " · " + (value.checked_on ? "assessed " + value.checked_on : "assessment pending") +
      ". " + (value.tier === "ready_to_try" ? readyToTryNote + " " : "") + value.summary;
  }
  function savedIds(serialized, tools) {
    try {
      const ids = JSON.parse(serialized), known = new Set(tools.map(function (tool) { return tool.id; }));
      return Array.isArray(ids) ? Array.from(new Set(ids.filter(function (id) { return typeof id === "string" && known.has(id); }))) : [];
    } catch (error) { return []; }
  }
  function shortlistJSON(ids, tools) {
    return JSON.stringify({format: "ai-media-scout-shortlist", version: 1,
      tool_ids: savedIds(JSON.stringify(Array.from(ids)), tools).sort()}, null, 2) + "\n";
  }
  function importShortlist(serialized, currentIds, tools) {
    let payload;
    try { payload = JSON.parse(serialized); }
    catch (error) { throw new Error("This is not valid JSON. Use a shortlist exported by AI Media Scout."); }
    if (!payload || payload.format !== "ai-media-scout-shortlist" || payload.version !== 1 ||
        !Array.isArray(payload.tool_ids) || payload.tool_ids.some(function (id) { return typeof id !== "string" || !id.trim(); })) {
      throw new Error("This is not a supported shortlist. Use Download shortlist or Copy shortlist in AI Media Scout.");
    }
    const known = new Set(tools.map(function (tool) { return tool.id; })), merged = new Set(currentIds);
    const missing = []; let added = 0, existing = 0;
    Array.from(new Set(payload.tool_ids)).forEach(function (id) {
      if (!known.has(id)) missing.push(id);
      else if (merged.has(id)) existing++;
      else { merged.add(id); added++; }
    });
    return {ids: Array.from(merged), added: added, existing: existing, missing: missing};
  }
  function researchNotes(ids, tools, sectionLabels) {
    function md(value) {
      return String(value || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
        .replace(/([\\`*_{}\[\]#!|])/g, "\\$1");
    }
    function url(value) { return "<" + String(value).replace(/[<>\s]/g, function (char) { return encodeURIComponent(char); }) + ">"; }
    function commands(value) {
      const runs = String(value).match(/`+/g) || [], fence = "`".repeat(Math.max(3, ...runs.map(function (run) { return run.length + 1; })));
      return fence + "text\n" + value + "\n" + fence;
    }
    const selected = new Set(ids), chosen = sortTools(tools.filter(function (tool) { return selected.has(tool.id); }), "name");
    const lines = ["# AI Media Scout — saved research notes", "",
      chosen.length + (chosen.length === 1 ? " saved tool." : " saved tools.") + " Each entry uses its latest available detailed review, or its latest screened discovery when a full guide is pending.", "",
      "These are dated research notes. Documentation review does not establish that a tool was installed or tested. Requirements, model terms and source links should be checked before use.", ""];
    function section(title, value, fields) {
      value = value || {};
      lines.push("### " + md(title), "", md(value.text || "Not documented"), "");
      (fields || []).forEach(function (field) {
        lines.push("- **" + md(field[1]) + ":** " + md(value[field[0]] || "Not documented"));
      });
      if (fields && fields.length) lines.push("");
      (value.steps || []).forEach(function (step, index) { lines.push((index + 1) + ". " + md(step)); });
      if (value.steps && value.steps.length) lines.push("");
      (value.commands || []).forEach(function (command) { lines.push(commands(command), ""); });
      if (value.source_urls && value.source_urls.length) {
        lines.push("Sources: " + value.source_urls.map(url).join(" · "), "");
      }
    }
    chosen.forEach(function (tool) {
      const version = primaryVersion(tool), p = version.profile, full = version.kind === "profile";
      lines.push("## " + md(p.name), "", "Tool ID: " + md(tool.id), "",
        "Edition: " + md(editionKey(version)) + " · Documentation checked: " + md(p.checked_on || "Not documented"), "",
        full ? (p.quality && p.quality.hands_on_tested ? "Hands-on testing recorded; see the quality review for its scope." :
          "Documentation review; installation and output were not independently tested by AI Media Scout.") : "Screened discovery — full profile pending.", "");
      Object.entries(p.links || {}).forEach(function (entry) { lines.push("- " + md(entry[0].replace(/_/g, " ")) + ": " + url(entry[1])); });
      lines.push("");
      const assessment = qualityOf(tool);
      lines.push("### Current library quality assessment", "", md(qualityText(tool)), "",
        "This assessment is separate from the dated guide below.", "", md(assessment.scope || "Evidence review pending"), "");
      Object.entries(assessment.checks).forEach(function (entry) {
        const check = entry[1];
        lines.push("- **" + md(entry[0].replace(/_/g, " ")) + " · " + md(check.status) + ":** " + md(check.note) +
          " " + (check.source_urls || []).map(url).join(" · "));
      });
      lines.push("", ...assessment.caveats.map(md), "");
      if (p.ai_relevance) section("How it uses AI", p.ai_relevance);
      if (full) {
        section("Why it appeared in this edition", p.novelty);
        if (p.maturity) lines.push("Maturity: " + md(p.maturity), "");
        Object.entries(sectionLabels).forEach(function (entry) {
          const fields = entry[0] === "requirements" ? [["hardware", "Hardware"], ["software", "Software"], ["platforms", "Platforms and limitations"]] :
            entry[0] === "license" ? [["code", "Software license"], ["weights", "Model weights"], ["commercial", "Commercial use"], ["cost", "Costs and services"]] : [];
          section(entry[1], p[entry[0]], fields);
        });
      } else {
        lines.push("### What it is good for", "", md(p.good_for), "", "Software license: " + md(p.code_license), "",
          "Installation, hardware, software, platforms, model-weight terms, commercial use and costs: not reviewed yet; full profile pending.", "",
          md(p.review_status), "");
      }
      lines.push("### Primary sources", "");
      (p.sources || []).forEach(function (source, index) { lines.push((index + 1) + ". " + md(source.title) + ": " + url(source.url)); });
      lines.push("", "---", "");
    });
    return lines.join("\n");
  }
  function comparisonSelection(serialized, tools) {
    try {
      const entries = JSON.parse(serialized), byId = new Map(tools.map(function (tool) { return [tool.id, tool]; })), seen = new Set();
      if (!Array.isArray(entries)) return [];
      return entries.filter(function (entry) {
        if (!entry || typeof entry.id !== "string" || typeof entry.edition !== "string" || seen.has(entry.id)) return false;
        const tool = byId.get(entry.id);
        if (!tool || !tool.versions.some(function (v) { return editionKey(v) === entry.edition; })) return false;
        seen.add(entry.id); return true;
      }).slice(0, 4).map(function (entry) { return {id: entry.id, edition: entry.edition}; });
    } catch (error) { return []; }
  }
  function comparisonRows(version, tool) {
    const p = version.profile, full = version.kind === "profile", pending = "Not reviewed yet · full profile pending";
    function row(label, value, source) {
      return {label: label, text: typeof value === "string" && value.trim() ? value : (full ? "Not documented" : pending),
              source_urls: source && source.source_urls || []};
    }
    const requirements = p.requirements || {}, license = p.license || {};
    return [
      row("Current quality assessment", qualityText(tool), {source_urls: qualityOf(tool).sources.map(function (s) { return s.url; })}),
      row("Good for", full ? p.good_for && p.good_for.text : p.good_for, full ? p.good_for : p.ai_relevance),
      row("Hardware", full ? requirements.hardware : null, requirements),
      row("Software", full ? requirements.software : null, requirements),
      row("Platforms and limitations", full ? requirements.platforms : null, requirements),
      row("Software license", full ? license.code : p.code_license, full ? license :
        {source_urls: (p.sources || []).map(function (source) { return source.url; })}),
      row("Model weights", full ? license.weights : null, license),
      row("Commercial use", full ? license.commercial : null, license),
      row("Costs and services", full ? license.cost : null, license),
      row("Maturity", full ? p.maturity : null),
      row("Review evidence", full ? (p.quality && p.quality.hands_on_tested ? "Hands-on testing recorded; see its scope in the profile" :
        "Documentation review; installation and output not independently tested by AI Media Scout") : "Creative AI use and software license screened; full review pending", p.quality)
    ];
  }
  function platformMentions(profile) {
    const text = profile.requirements ? profile.requirements.platforms : "";
    const patterns = {
      "macOS": /\b(macos|mac|apple silicon|os x)\b/i, "Windows": /\bwindows\b/i,
      "Linux": /\blinux\b/i, "Browser": /\b(browser|webgpu|webgl|wasm|webassembly)\b/i,
      "XR / headset": /\b(headset|webxr|vr|xr|visionos)\b/i, "Cloud": /\b(cloud|colab|hosted)\b/i
    };
    return Object.keys(patterns).filter(function (name) { return patterns[name].test(text || ""); });
  }
  function matches(tool, filters, text) {
    const version = primaryVersion(tool, filters.edition), profile = version.profile;
    if (filters.edition && !tool.versions.some(function (v) { return editionKey(v) === filters.edition; })) return false;
    if (filters.field && !(filters.edition ? profile.categories : tool.categories).includes(filters.field)) return false;
    if (filters.platform && !(filters.edition ? platformMentions(profile) : tool.platform_mentions).includes(filters.platform)) return false;
    if (filters.review && (filters.edition ? version.kind : tool.review) !== filters.review) return false;
    if (filters.quality && qualityOf(tool).tier !== filters.quality) return false;
    const license = version.kind === "profile" ? profile.license.code : profile.code_license;
    if (filters.license && license !== filters.license) return false;
    const tokens = Array.from(fold(filters.q || "").matchAll(/"([^"]+)"|(\S+)/g), function (m) { return m[1] || m[2]; });
    // An edition filter must not match requirements or uses from another review.
    const haystack = filters.edition ? searchText({id: tool.id, date: version.date, profile: profile}) :
      (text === undefined ? searchText(tool) : text);
    return tokens.every(function (token) { return haystack.includes(token); });
  }
  function sortTools(tools, sort) {
    return tools.slice().sort(function (a, b) {
      if (sort === "name") return a.name.localeCompare(b.name);
      const field = sort === "added" ? "first_seen" : "profile_date";
      return b[field].localeCompare(a[field]) || a.name.localeCompare(b.name);
    });
  }
  function coverageText(edition) {
    const c = edition.search_coverage;
    if (!c) return "This edition predates expanded search tracking. Its tool count reflects the published reviews; new editions use the full expanded search.";
    const gaps = c.failed_github_queries + c.partial_github_queries + c.failed_model_queries + c.ecosystem_gaps;
    return c.fields + " fields · " + c.attempted_github_queries + "/" + c.planned_github_queries +
      " repository queries attempted · " + c.source_candidates.toLocaleString("en-US") + " source candidates · " +
      c.model_candidates.toLocaleString("en-US") + " model leads. " + gaps + " source gaps; " +
      c.truncated_github_queries + " bounded repository queries. Candidates require review.";
  }
  if (typeof module !== "undefined" && module.exports) {
    module.exports = {matches: matches, searchText: searchText, primaryVersion: primaryVersion, sortTools: sortTools,
                      coverageText: coverageText, editionKey: editionKey, savedIds: savedIds,
                      qualityOf: qualityOf, qualityText: qualityText,
                      comparisonSelection: comparisonSelection, comparisonRows: comparisonRows,
                      shortlistJSON: shortlistJSON, importShortlist: importShortlist, researchNotes: researchNotes};
  }
  if (typeof document === "undefined") return;
  const data = JSON.parse(document.getElementById("library-data").textContent);
  const byId = new Map(data.tools.map(function (tool) { return [tool.id, tool]; }));
  const names = new Map(data.categories.map(function (field) { return [field.id, field.name]; }));
  const cache = new Map(data.tools.map(function (tool) { return [tool.id, searchText(tool) + " " + tool.categories.map(function (c) { return fold(names.get(c) || c); }).join(" ")]; }));
  const prefix = document.body.dataset.reportPrefix;
  function reportPath(day, extension) {
    const edition = data.editions.find(function (e) { return editionKey(e) === day; });
    return (edition && edition.report_path || prefix + (edition && edition.report_directory || day + "/")) + "report." + extension;
  }
  const controls = {q: "search", field: "field-filter", platform: "platform-filter", license: "license-filter",
                    review: "review-filter", quality: "quality-filter", edition: "edition-filter", sort: "sort"};
  const $ = function (id) { return document.getElementById(id); };
  const savedKey = "ai-media-scout.saved.v1";
  let saved = new Set(), storageAvailable = true;
  try { saved = new Set(savedIds(localStorage.getItem(savedKey), data.tools)); }
  catch (error) { storageAvailable = false; }
  let visible = 24, currentView = "library", activeTool = null, activeVersion = null, comparison = [];
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function button(className, text, action) {
    const node = element("button", className, text);
    node.type = "button"; node.addEventListener("click", action);
    return node;
  }
  function link(text, href, className, external) {
    const node = element("a", className, text); node.href = href;
    if (external) { node.target = "_blank"; node.rel = "noopener noreferrer"; }
    return node;
  }
  function date(day) {
    return new Date(day + "T12:00:00Z").toLocaleDateString("en-US", {month: "short", day: "numeric", year: "numeric", timeZone: "UTC"});
  }
  function options(id, entries) {
    entries.forEach(function (entry) {
      const option = element("option", "", entry[1]); option.value = entry[0]; $(id).append(option);
    });
  }
  function filters() {
    const values = {};
    Object.keys(controls).forEach(function (name) { values[name] = $(controls[name]).value; });
    return values;
  }
  function updateURL() {
    const values = filters(), params = new URLSearchParams();
    Object.keys(values).forEach(function (name) {
      if (values[name] && !(name === "sort" && values[name] === "updated")) params.set(name, values[name]);
    });
    if ($("saved-only").checked) params.set("saved", "1");
    if (comparison.length) params.set("compare", JSON.stringify(comparison));
    if ($("compare-dialog").open) params.set("comparing", "1");
    if (currentView === "reports") params.set("view", "reports");
    if (activeTool) { params.set("tool", activeTool); params.set("version", activeVersion); }
    const query = params.toString();
    history.replaceState(null, "", location.pathname + (query ? "?" + query : ""));
  }
  function showView(view) {
    currentView = view; $("library").hidden = view !== "library"; $("reports").hidden = view !== "reports";
    ["library", "reports"].forEach(function (name) {
      $(name + "-tab").classList.toggle("active", name === view);
      $(name + "-tab").setAttribute("aria-pressed", String(name === view));
    });
    updateURL();
  }
  function persistSaved() {
    try { localStorage.setItem(savedKey, JSON.stringify(Array.from(saved))); storageAvailable = true; }
    catch (error) { storageAvailable = false; }
  }
  function download(text, type, name) {
    const objectURL = URL.createObjectURL(new Blob([text], {type: type})), anchor = link("", objectURL);
    anchor.download = name; document.body.append(anchor); anchor.click(); anchor.remove();
    window.setTimeout(function () { URL.revokeObjectURL(objectURL); }, 10000);
  }
  function receiveShortlist(text) {
    try {
      const result = importShortlist(text, saved, data.tools);
      saved = new Set(result.ids); persistSaved(); render();
      $("shortlist-status").textContent = "Added " + result.added + "; already saved " + result.existing +
        "; not in this library " + result.missing.length + "." +
        (result.missing.length ? " Missing tools were skipped. Try importing again after your library updates." : "") +
        (!storageAvailable ? " Browser storage is unavailable; these saves last for this tab only. Download a backup before closing it." : "");
      $("shortlist-status").dataset.error = "false";
    } catch (error) {
      $("shortlist-status").textContent = error.message + " Your saved tools have not changed.";
      $("shortlist-status").dataset.error = "true";
    }
  }
  function personalButton(action, tool, version) {
    const node = button("personal-button", "", function () {
      if (action === "save") {
        if (saved.has(tool.id)) saved.delete(tool.id); else saved.add(tool.id);
        persistSaved();
      } else {
        const index = comparison.findIndex(function (entry) { return entry.id === tool.id; });
        if (index >= 0) comparison.splice(index, 1);
        else if (comparison.length < 4) comparison.push({id: tool.id, edition: editionKey(version)});
      }
      render();
      if (!node.isConnected) {
        const replacement = Array.from(document.querySelectorAll("[data-personal-action]")).find(function (candidate) {
          return candidate.dataset.personalAction === action && candidate.dataset.toolId === tool.id && candidate.getClientRects().length;
        });
        (replacement || $("saved-only")).focus();
      }
    });
    node.dataset.personalAction = action; node.dataset.toolId = tool.id;
    return node;
  }
  function updatePersonalControls() {
    $("saved-count").textContent = saved.size;
    $("saved-storage-note").hidden = storageAvailable;
    $("shortlist-count").textContent = saved.size + (saved.size === 1 ? " saved tool" : " saved tools") + " in this browser.";
    ["download-shortlist", "copy-shortlist", "download-notes"].forEach(function (id) { $(id).disabled = saved.size === 0; });
    document.querySelectorAll("[data-personal-action]").forEach(function (node) {
      const id = node.dataset.toolId, action = node.dataset.personalAction, tool = byId.get(id);
      const selected = action === "save" ? saved.has(id) : comparison.some(function (entry) { return entry.id === id; });
      node.textContent = action === "save" ? (selected ? "Saved" : "Save") : (selected ? "Comparing" : "Compare");
      node.setAttribute("aria-pressed", String(selected));
      node.setAttribute("aria-label", action === "save" ? (selected ? "Unsave " : "Save ") + tool.name :
        (selected ? "Remove " + tool.name + " from comparison" : "Add " + tool.name + " to comparison"));
      node.disabled = action === "compare" && !selected && comparison.length >= 4;
      node.title = node.disabled ? "Remove a tool from the comparison to add another." : "";
    });
    $("comparison-bar").hidden = comparison.length === 0;
    $("compare-selected").textContent = "Compare " + comparison.length + (comparison.length === 1 ? " tool" : " tools");
    $("compare-selected").disabled = comparison.length < 2;
    $("comparison-items").replaceChildren.apply($("comparison-items"), comparison.map(function (entry) {
      const tool = byId.get(entry.id), version = primaryVersion(tool, entry.edition);
      const chip = button("comparison-chip", version.profile.name + " ×", function () {
        comparison = comparison.filter(function (candidate) { return candidate.id !== entry.id; }); render();
        if (comparison.length >= 2) $("compare-selected").focus();
        else if (comparison.length) $("comparison-items").firstElementChild.focus();
        else $("search").focus();
      });
      chip.setAttribute("aria-label", "Remove " + version.profile.name + " from comparison"); return chip;
    }));
  }
  function card(tool, values) {
    const version = primaryVersion(tool, values.edition), p = version.profile, full = version.kind === "profile";
    const node = element("article", "tool-card"); node.dataset.toolId = tool.id;
    node.append(element("div", "card-category", p.categories.map(function (c) { return names.get(c) || c; }).join(" · ")));
    const title = element("h3");
    title.append(button("title-button", p.name, function () { openProfile(tool.id, editionKey(version)); }));
    node.append(title);
    node.append(element("p", "card-description", full ? p.introduction.text : p.ai_relevance.text));
    const badges = element("div", "badge-row");
    badges.append(qualityBadge(tool));
    badges.append(element("span", "badge license", full ? p.license.code : p.code_license));
    badges.append(element("span", "badge" + (full ? "" : " pending"), full ? "Detailed profile" : "Profile pending"));
    node.append(badges);
    const use = element("p", "card-use"); use.append(element("strong", "", "Good for: "), document.createTextNode(full ? p.good_for.text : p.good_for));
    node.append(use);
    const actions = element("div", "card-actions");
    actions.append(personalButton("save", tool, version), personalButton("compare", tool, version)); node.append(actions);
    const bottom = element("div", "card-bottom");
    bottom.append(element("span", "card-date", "Reviewed " + date(p.checked_on)));
    bottom.append(button("profile-button", "Explore tool ↗", function () { openProfile(tool.id, editionKey(version)); }));
    node.append(bottom); return node;
  }
  function render() {
    const values = filters();
    const results = sortTools(data.tools.filter(function (tool) {
      return (!$("saved-only").checked || saved.has(tool.id)) && matches(tool, values, cache.get(tool.id));
    }), values.sort);
    $("result-count").textContent = results.length + (results.length === 1 ? " tool" : " tools") + " found" +
      (results.length > visible ? " · showing " + visible : "");
    $("cards").replaceChildren.apply($("cards"), results.slice(0, visible).map(function (tool) { return card(tool, values); }));
    $("empty").hidden = results.length !== 0; $("load-more").hidden = results.length <= visible;
    $("search-scope").textContent = values.edition ? "Search this edition" : "Search every review";
    $("search-label").textContent = values.edition ? "Search profiles in the selected edition" : "Search all profiles and review history";
    $("empty-message").textContent = values.quality === "recommended" && !data.quality_counts.recommended ?
      "No tools have met all recommendation checks yet. Choose All quality tiers to explore the library and its documented evidence gaps." :
      values.quality === "ready_to_try" && !data.quality_counts.ready_to_try ?
      "No tools have completed the five checks for Ready to try yet. Creative-result review can wait; licensing, setup, maintenance, independent use and dependencies still need verified evidence. Choose All quality tiers to explore the library." : $("saved-only").checked ?
      (saved.size ? "Your saved tools do not match these filters. Try fewer words or clear the filters." :
        "Save a tool from the library to start your shortlist, then return here.") :
      "Try fewer words, another creative field, or clear your filters.";
    updatePersonalControls();
    updateURL();
  }
  function reset() {
    Object.keys(controls).forEach(function (name) { $(controls[name]).value = name === "sort" ? "updated" : ""; });
    $("saved-only").checked = false;
    visible = 24; render();
  }
  function refs(section, profile) {
    const node = element("div", "source-refs");
    (section.source_urls || []).forEach(function (url) {
      const index = profile.sources.findIndex(function (source) { return source.url === url; });
      node.append(link("Source " + (index < 0 ? "" : index + 1), url, "", true));
    });
    return node;
  }
  function section(label, value, profile) {
    const node = element("section", "profile-section");
    node.append(element("h3", "", label), element("p", "", value.text));
    if (value.hardware || value.code) {
      const list = element("dl");
      (value.hardware ? ["hardware", "software", "platforms"] : ["code", "weights", "commercial", "cost"]).forEach(function (field) {
        list.append(element("dt", "", field[0].toUpperCase() + field.slice(1)), element("dd", "", value[field] || "Not documented"));
      }); node.append(list);
    }
    if (value.steps && value.steps.length) {
      const steps = element("ol"); value.steps.forEach(function (step) { steps.append(element("li", "", step)); }); node.append(steps);
    }
    (value.commands || []).forEach(function (command) {
      const pre = element("pre"); pre.append(element("code", "", command)); node.append(pre);
    });
    node.append(refs(value, profile)); return node;
  }
  function qualityBadge(tool) {
    const value = qualityOf(tool), badge = element("span", "badge quality-" + value.tier, qualityLabels[value.tier]);
    badge.title = qualityText(tool); return badge;
  }
  function qualityPanel(tool) {
    const value = qualityOf(tool), panel = element("section", "quality-panel");
    panel.append(element("h3", "", "Current quality assessment"), qualityBadge(tool),
      element("p", "", value.summary), element("p", "profile-meta",
        (value.checked_on ? "Assessed " + date(value.checked_on) + " · " : "Assessment pending · ") +
        (data.quality_methods[value.method] || "Evidence review pending")),
      element("p", "", "Scope: " + (value.scope || "Evidence review pending")),
      element("p", "profile-meta", "This current library assessment is separate from the preserved review selected below. Verified checks refer to cited evidence, not our own runtime testing."));
    if (value.tier === "ready_to_try") panel.append(element("p", "", readyToTryNote));
    const details = element("details"), summary = element("summary", "", "Evidence and remaining gaps");
    details.append(summary);
    Object.entries(value.checks).forEach(function (entry) {
      const check = entry[1], item = element("div", "quality-check");
      item.append(element("h4", "", data.quality_checks[entry[0]] + " · " + check.status),
        element("p", "", check.note), refs(check, value)); details.append(item);
    });
    const caveats = element("ul"); value.caveats.forEach(function (note) { caveats.append(element("li", "", note)); });
    details.append(caveats); panel.append(details); return panel;
  }
  function openProfile(id, versionDate) {
    const tool = byId.get(id); if (!tool) return;
    const version = primaryVersion(tool, versionDate), p = version.profile, full = version.kind === "profile";
    activeTool = id; activeVersion = editionKey(version);
    const header = element("header", "profile-header");
    header.append(element("p", "card-category", p.categories.map(function (c) { return names.get(c) || c; }).join(" · ")));
    const title = element("h2", "", p.name); title.id = "profile-title"; header.append(title);
    const badges = element("div", "badge-row");
    badges.append(qualityBadge(tool));
    badges.append(element("span", "badge license", full ? p.license.code : p.code_license),
                  element("span", "badge" + (full ? "" : " pending"), full ? p.maturity : "Screened · full profile pending"));
    header.append(badges);
    header.append(element("p", "profile-meta", "Documentation checked " + date(p.checked_on) +
      " · First found " + date(tool.first_seen) + " · " + tool.versions.length + (tool.versions.length === 1 ? " preserved review" : " preserved reviews")));
    const links = element("div", "profile-links");
    Object.entries(p.links || {}).forEach(function (entry) {
      links.append(link(entry[0].replace(/_/g, " ").replace(/^./, function (c) { return c.toUpperCase(); }) + " ↗", entry[1], "", true));
    });
    links.append(link("Daily report ↗", reportPath(editionKey(version), "html"), "", true));
    const shareStatus = element("span", "share-status");
    links.append(button("profile-button", "Copy profile link", async function () {
      try { await navigator.clipboard.writeText(location.href); shareStatus.textContent = "Link copied"; }
      catch (error) { shareStatus.textContent = "Copy the address from your browser."; }
    }), shareStatus);
    links.append(personalButton("save", tool, version), personalButton("compare", tool, version));
    header.append(links);
    const versionControl = element("div", "version-control"), versionLabel = element("label", "", "Review history");
    versionLabel.htmlFor = "version-select";
    const select = element("select"); select.id = "version-select";
    tool.versions.forEach(function (v) {
      const option = element("option", "", editionLabel(v) + (v.kind === "profile" ? " · Detailed profile" : " · Screened discovery"));
      option.value = editionKey(v); select.append(option);
    });
    select.value = editionKey(version);
    select.addEventListener("change", function () { openProfile(id, select.value); $("version-select").focus(); });
    versionControl.append(versionLabel, select); header.append(versionControl);
    const body = element("div", "profile-body");
    body.append(qualityPanel(tool));
    body.append(element("p", "profile-notice", full ?
      (p.quality.hands_on_tested ? "Hands-on testing is recorded in this review. Read its scope and limitations below." :
        "Documentation review; installation and output were not independently tested by AI Media Scout. Check the dated requirements and model terms before production use.") :
      "Creative AI use and the software license were screened. A full installation, requirements and quality review is still pending."));
    if (tool.last_seen > version.date) body.append(element("p", "profile-meta", "This tool also appeared in a later edition on " + date(tool.last_seen) + ". Choose a review above to compare."));
    if (full) body.append(section("Why it appeared in this edition", {text: p.novelty.text}, p));
    if (p.ai_relevance) body.append(section("How it uses AI", p.ai_relevance, p));
    if (full) Object.keys(data.section_labels).forEach(function (name) { body.append(section(data.section_labels[name], p[name], p)); });
    else {
      body.append(element("h3", "", "What it is good for"), element("p", "", p.good_for), element("p", "", p.review_status));
    }
    const sources = element("section", "profile-section"); sources.append(element("h3", "", "Primary sources"));
    const list = element("ol", "source-list");
    p.sources.forEach(function (source) { const item = element("li"); item.append(link(source.title, source.url, "", true)); list.append(item); });
    sources.append(list); body.append(sources);
    $("profile-content").replaceChildren(header, body);
    if (!$("profile-dialog").open) $("profile-dialog").showModal();
    updatePersonalControls();
    updateURL();
  }
  function openComparison() {
    if (comparison.length < 2) return;
    const selected = comparison.map(function (entry) {
      const tool = byId.get(entry.id), version = primaryVersion(tool, entry.edition);
      return {tool: tool, version: version, rows: comparisonRows(version, tool)};
    });
    const table = element("table", "comparison-table"), caption = element("caption", "sr-only", "Dated tool reviews, requirements, licenses and costs");
    table.style.minWidth = (155 + selected.length * 250) + "px";
    const head = element("thead"), header = element("tr"), label = element("th", "", "What matters"); label.scope = "col"; header.append(label);
    selected.forEach(function (item) {
      const cell = element("th"); cell.scope = "col";
      const p = item.version.profile;
      cell.append(button("title-button", p.name, function () {
        $("compare-dialog").close(); openProfile(item.tool.id, editionKey(item.version));
      }), element("p", "profile-meta", "Reviewed " + date(p.checked_on)),
        element("span", "badge" + (item.version.kind === "profile" ? "" : " pending"), item.version.kind === "profile" ? "Detailed profile" : "Profile pending"));
      const links = element("div", "comparison-links");
      Object.entries(p.links || {}).forEach(function (entry) {
        if (["repository", "homepage", "demo", "documentation"].includes(entry[0])) links.append(link(entry[0].replace(/^./, function (c) { return c.toUpperCase(); }) + " ↗", entry[1], "", true));
      });
      if (item.version.kind === "screened") (p.sources || []).forEach(function (source) {
        links.append(link(source.title + " ↗", source.url, "", true));
      });
      links.append(link("Dated report ↗", reportPath(editionKey(item.version), "html"), "", true)); cell.append(links); header.append(cell);
    });
    head.append(header); const body = element("tbody");
    selected[0].rows.forEach(function (row, index) {
      const tr = element("tr"), heading = element("th", "", row.label); heading.scope = "row"; tr.append(heading);
      selected.forEach(function (item) {
        const value = item.rows[index], cell = element("td");
        cell.append(element("p", "", value.text), refs(value, item.version.profile)); tr.append(cell);
      }); body.append(tr);
    });
    table.append(caption, head, body); $("comparison-content").replaceChildren(table);
    $("comparison-share-status").textContent = "";
    if (!$("compare-dialog").open) $("compare-dialog").showModal();
    layoutComparison(); updateURL();
  }
  function layoutComparison() {
    if (!$("compare-dialog").open) return;
    const region = $("comparison-content"), table = region.querySelector("table");
    const labelWidth = window.matchMedia("(max-width:760px)").matches ? 130 : 155;
    // Keep one complete tool column readable beside the sticky labels on phones.
    const columnWidth = Math.max(120, Math.min(250, region.clientWidth - labelWidth));
    table.style.minWidth = (labelWidth + comparison.length * columnWidth) + "px";
    $("comparison-scroll-hint").hidden = table.scrollWidth <= region.clientWidth;
  }
  function editionLabel(edition) {
    return date(edition.report_date || edition.date) + (edition.revision > 1 ? " · Update " + (edition.revision - 1) : "");
  }
  function renderEditions() {
    data.editions.forEach(function (edition) {
      const node = element("article", "edition-card");
      node.append(element("span", "eyebrow", "DAILY FIELD REPORT"), element("h3", "", editionLabel(edition)));
      node.append(element("p", "", edition.summary));
      node.append(element("p", "filter-note", coverageText(edition)));
      node.append(element("span", "badge", edition.profile_count + " profiles · " + edition.lead_count + " screened discoveries"));
      const links = element("div", "edition-links");
      [["Read report ↗", "html"], ["Markdown", "md"], ["JSON", "json"]].forEach(function (item) {
        links.append(link(item[0], reportPath(editionKey(edition), item[1]), "", true));
      }); node.append(links); $("edition-list").append(node);
    });
    if (!data.editions.length) $("edition-list").append(element("p", "reports-intro", "The first finished edition will appear here."));
  }
  options("field-filter", data.categories.map(function (c) { return [c.id, c.name]; }));
  options("platform-filter", Array.from(new Set(data.tools.flatMap(function (t) { return t.platform_mentions; }))).sort().map(function (p) { return [p, p]; }));
  const licenses = data.tools.flatMap(function (tool) { return tool.versions.map(function (v) { return v.kind === "profile" ? v.profile.license.code : v.profile.code_license; }); });
  options("license-filter", Array.from(new Set(licenses)).sort().map(function (license) { return [license, license]; }));
  options("edition-filter", data.editions.map(function (e) { return [editionKey(e), editionLabel(e)]; }));
  $("profile-total").textContent = data.counts.profiles; $("screened-total").textContent = data.counts.screened;
  $("edition-total").textContent = data.counts.editions;
  $("quality-totals").textContent = Object.entries(qualityLabels).map(function (entry) {
    return (data.quality_counts[entry[0]] || 0) + " " + entry[1].toLowerCase();
  }).join(" · ") + ". Quality unverified means evidence is incomplete; no tools are hidden by default.";
  if (data.editions.length) {
    const latest = data.editions[0]; $("latest-date").textContent = editionLabel(latest);
    $("latest-summary").textContent = latest.summary.length > 105 ? latest.summary.slice(0, 102) + "…" : latest.summary;
    $("latest-coverage").textContent = coverageText(latest);
    $("latest-report").href = reportPath(editionKey(latest), "html"); $("latest-report").hidden = false;
  }
  const params = new URLSearchParams(location.search);
  comparison = comparisonSelection(params.get("compare"), data.tools);
  $("saved-only").checked = params.get("saved") === "1";
  Object.keys(controls).forEach(function (name) { if (params.has(name)) $(controls[name]).value = params.get(name); });
  if (!$("sort").value) $("sort").value = "updated";
  Object.keys(controls).forEach(function (name) {
    $(controls[name]).addEventListener(name === "q" ? "input" : "change", function () { visible = 24; render(); });
  });
  $("reset").addEventListener("click", reset); $("empty-reset").addEventListener("click", reset);
  $("saved-only").addEventListener("change", function () { visible = 24; render(); });
  $("manage-shortlist").addEventListener("click", function () {
    $("shortlist-status").textContent = ""; $("shortlist-dialog").showModal();
  });
  $("close-shortlist").addEventListener("click", function () { $("shortlist-dialog").close(); });
  $("download-shortlist").addEventListener("click", function () {
    download(shortlistJSON(saved, data.tools), "application/json", "ai-media-scout-shortlist.json");
  });
  $("download-notes").addEventListener("click", function () {
    download(researchNotes(saved, data.tools, data.section_labels), "text/markdown;charset=utf-8", "ai-media-scout-research-notes.md");
  });
  $("copy-shortlist").addEventListener("click", async function () {
    const text = shortlistJSON(saved, data.tools);
    try { await navigator.clipboard.writeText(text); $("shortlist-status").textContent = "Shortlist copied. Paste it into Move saved tools on the other device."; }
    catch (error) {
      $("shortlist-json").value = text; $("shortlist-paste").open = true; $("shortlist-json").focus(); $("shortlist-json").select();
      $("shortlist-status").textContent = "Copy the selected shortlist text, or use Download shortlist.";
    }
    $("shortlist-status").dataset.error = "false";
  });
  $("import-shortlist").addEventListener("change", async function () {
    const file = this.files[0]; if (!file) return;
    try { receiveShortlist(await file.text()); }
    catch (error) { $("shortlist-status").textContent = "The file could not be read. Your saved tools have not changed."; $("shortlist-status").dataset.error = "true"; }
    this.value = "";
  });
  $("import-pasted-shortlist").addEventListener("click", function () { receiveShortlist($("shortlist-json").value); });
  $("compare-selected").addEventListener("click", openComparison);
  $("clear-comparison").addEventListener("click", function () { comparison = []; render(); $("search").focus(); });
  $("close-comparison").addEventListener("click", function () { $("compare-dialog").close(); });
  $("compare-dialog").addEventListener("close", updateURL);
  window.addEventListener("resize", layoutComparison);
  $("copy-comparison").addEventListener("click", async function () {
    try { await navigator.clipboard.writeText(location.href); $("comparison-share-status").textContent = "Comparison link copied"; }
    catch (error) { $("comparison-share-status").textContent = "Copy the address from your browser."; }
  });
  window.addEventListener("storage", function (event) {
    if (event.key === savedKey || event.key === null) {
      saved = new Set(savedIds(event.key === null ? null : event.newValue, data.tools)); render();
    }
  });
  $("load-more").addEventListener("click", function () { visible += 24; render(); });
  $("library-tab").addEventListener("click", function () { showView("library"); });
  $("reports-tab").addEventListener("click", function () { showView("reports"); });
  $("close-profile").addEventListener("click", function () { $("profile-dialog").close(); });
  $("profile-dialog").addEventListener("close", function () { activeTool = null; activeVersion = null; updateURL(); });
  renderEditions(); render(); showView(params.get("view") === "reports" ? "reports" : "library");
  if (params.get("tool")) openProfile(params.get("tool"), params.get("version"));
  else if (params.get("comparing") === "1") openComparison();
}());
