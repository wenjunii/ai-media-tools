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
  function primaryVersion(tool, edition) {
    return (edition && tool.versions.find(function (v) { return v.date === edition; })) ||
      tool.versions.find(function (v) { return v.kind === "profile"; }) || tool.versions[0];
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
    if (filters.edition && !tool.versions.some(function (v) { return v.date === filters.edition; })) return false;
    if (filters.field && !(filters.edition ? profile.categories : tool.categories).includes(filters.field)) return false;
    if (filters.platform && !(filters.edition ? platformMentions(profile) : tool.platform_mentions).includes(filters.platform)) return false;
    if (filters.review && (filters.edition ? version.kind : tool.review) !== filters.review) return false;
    const license = version.kind === "profile" ? profile.license.code : profile.code_license;
    if (filters.license && license !== filters.license) return false;
    const tokens = Array.from(fold(filters.q || "").matchAll(/"([^"]+)"|(\S+)/g), function (m) { return m[1] || m[2]; });
    const haystack = text === undefined ? searchText(tool) : text;
    return tokens.every(function (token) { return haystack.includes(token); });
  }
  function sortTools(tools, sort) {
    return tools.slice().sort(function (a, b) {
      if (sort === "name") return a.name.localeCompare(b.name);
      const field = sort === "added" ? "first_seen" : "profile_date";
      return b[field].localeCompare(a[field]) || a.name.localeCompare(b.name);
    });
  }
  if (typeof module !== "undefined" && module.exports) {
    module.exports = {matches: matches, searchText: searchText, primaryVersion: primaryVersion, sortTools: sortTools};
  }
  if (typeof document === "undefined") return;
  const data = JSON.parse(document.getElementById("library-data").textContent);
  const byId = new Map(data.tools.map(function (tool) { return [tool.id, tool]; }));
  const names = new Map(data.categories.map(function (field) { return [field.id, field.name]; }));
  const cache = new Map(data.tools.map(function (tool) { return [tool.id, searchText(tool) + " " + tool.categories.map(function (c) { return fold(names.get(c) || c); }).join(" ")]; }));
  const prefix = document.body.dataset.reportPrefix;
  function reportPath(day, extension) {
    const edition = data.editions.find(function (e) { return e.report_date === day; });
    return (edition && edition.report_path || prefix + day + "/") + "report." + extension;
  }
  const controls = {q: "search", field: "field-filter", platform: "platform-filter", license: "license-filter",
                    review: "review-filter", edition: "edition-filter", sort: "sort"};
  const $ = function (id) { return document.getElementById(id); };
  let visible = 24, currentView = "library", activeTool = null, activeVersion = null;
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
  function card(tool, values) {
    const version = primaryVersion(tool, values.edition), p = version.profile, full = version.kind === "profile";
    const node = element("article", "tool-card"); node.dataset.toolId = tool.id;
    node.append(element("div", "card-category", p.categories.map(function (c) { return names.get(c) || c; }).join(" · ")));
    const title = element("h3");
    title.append(button("title-button", p.name, function () { openProfile(tool.id, version.date); }));
    node.append(title);
    node.append(element("p", "card-description", full ? p.introduction.text : p.ai_relevance.text));
    const badges = element("div", "badge-row");
    badges.append(element("span", "badge license", full ? p.license.code : p.code_license));
    badges.append(element("span", "badge" + (full ? "" : " pending"), full ? "Detailed profile" : "Profile pending"));
    node.append(badges);
    const use = element("p", "card-use"); use.append(element("strong", "", "Good for: "), document.createTextNode(full ? p.good_for.text : p.good_for));
    node.append(use);
    const bottom = element("div", "card-bottom");
    bottom.append(element("span", "card-date", "Reviewed " + date(p.checked_on)));
    bottom.append(button("profile-button", "Explore tool ↗", function () { openProfile(tool.id, version.date); }));
    node.append(bottom); return node;
  }
  function render() {
    const values = filters();
    const results = sortTools(data.tools.filter(function (tool) { return matches(tool, values, cache.get(tool.id)); }), values.sort);
    $("result-count").textContent = results.length + (results.length === 1 ? " tool" : " tools") + " found" +
      (results.length > visible ? " · showing " + visible : "");
    $("cards").replaceChildren.apply($("cards"), results.slice(0, visible).map(function (tool) { return card(tool, values); }));
    $("empty").hidden = results.length !== 0; $("load-more").hidden = results.length <= visible;
    updateURL();
  }
  function reset() {
    Object.keys(controls).forEach(function (name) { $(controls[name]).value = name === "sort" ? "updated" : ""; });
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
  function openProfile(id, versionDate) {
    const tool = byId.get(id); if (!tool) return;
    const version = primaryVersion(tool, versionDate), p = version.profile, full = version.kind === "profile";
    activeTool = id; activeVersion = version.date;
    const header = element("header", "profile-header");
    header.append(element("p", "card-category", p.categories.map(function (c) { return names.get(c) || c; }).join(" · ")));
    const title = element("h2", "", p.name); title.id = "profile-title"; header.append(title);
    const badges = element("div", "badge-row");
    badges.append(element("span", "badge license", full ? p.license.code : p.code_license),
                  element("span", "badge" + (full ? "" : " pending"), full ? p.maturity : "Screened · full profile pending"));
    header.append(badges);
    header.append(element("p", "profile-meta", "Documentation checked " + date(p.checked_on) +
      " · First found " + date(tool.first_seen) + " · " + tool.versions.length + (tool.versions.length === 1 ? " preserved review" : " preserved reviews")));
    const links = element("div", "profile-links");
    Object.entries(p.links || {}).forEach(function (entry) {
      links.append(link(entry[0].replace(/_/g, " ").replace(/^./, function (c) { return c.toUpperCase(); }) + " ↗", entry[1], "", true));
    });
    links.append(link("Daily report ↗", reportPath(version.date, "html"), "", true));
    const shareStatus = element("span", "share-status");
    links.append(button("profile-button", "Copy profile link", async function () {
      try { await navigator.clipboard.writeText(location.href); shareStatus.textContent = "Link copied"; }
      catch (error) { shareStatus.textContent = "Copy the address from your browser."; }
    }), shareStatus);
    header.append(links);
    const versionControl = element("div", "version-control"), versionLabel = element("label", "", "Review history");
    versionLabel.htmlFor = "version-select";
    const select = element("select"); select.id = "version-select";
    tool.versions.forEach(function (v) {
      const option = element("option", "", date(v.date) + (v.kind === "profile" ? " · Detailed profile" : " · Screened discovery"));
      option.value = v.date; select.append(option);
    });
    select.value = version.date;
    select.addEventListener("change", function () { openProfile(id, select.value); $("version-select").focus(); });
    versionControl.append(versionLabel, select); header.append(versionControl);
    const body = element("div", "profile-body");
    body.append(element("p", "profile-notice", full ?
      (p.quality.hands_on_tested ? "Hands-on testing is recorded in this review. Read its scope and limitations below." :
        "Documentation review; installation and output were not independently tested. Check the dated requirements and model terms before production use.") :
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
    updateURL();
  }
  function renderEditions() {
    data.editions.forEach(function (edition) {
      const node = element("article", "edition-card");
      node.append(element("span", "eyebrow", "DAILY FIELD REPORT"), element("h3", "", date(edition.report_date)));
      node.append(element("p", "", edition.summary));
      node.append(element("span", "badge", edition.profile_count + " profiles · " + edition.lead_count + " screened discoveries"));
      const links = element("div", "edition-links");
      [["Read report ↗", "html"], ["Markdown", "md"], ["JSON", "json"]].forEach(function (item) {
        links.append(link(item[0], reportPath(edition.report_date, item[1]), "", true));
      }); node.append(links); $("edition-list").append(node);
    });
    if (!data.editions.length) $("edition-list").append(element("p", "reports-intro", "The first finished edition will appear here."));
  }
  options("field-filter", data.categories.map(function (c) { return [c.id, c.name]; }));
  options("platform-filter", Array.from(new Set(data.tools.flatMap(function (t) { return t.platform_mentions; }))).sort().map(function (p) { return [p, p]; }));
  const licenses = data.tools.flatMap(function (tool) { return tool.versions.map(function (v) { return v.kind === "profile" ? v.profile.license.code : v.profile.code_license; }); });
  options("license-filter", Array.from(new Set(licenses)).sort().map(function (license) { return [license, license]; }));
  options("edition-filter", data.editions.map(function (e) { return [e.report_date, date(e.report_date)]; }));
  $("profile-total").textContent = data.counts.profiles; $("screened-total").textContent = data.counts.screened;
  $("edition-total").textContent = data.counts.editions;
  if (data.editions.length) {
    const latest = data.editions[0]; $("latest-date").textContent = date(latest.report_date);
    $("latest-summary").textContent = latest.summary.length > 105 ? latest.summary.slice(0, 102) + "…" : latest.summary;
    $("latest-report").href = reportPath(latest.report_date, "html"); $("latest-report").hidden = false;
  }
  const params = new URLSearchParams(location.search);
  Object.keys(controls).forEach(function (name) { if (params.has(name)) $(controls[name]).value = params.get(name); });
  if (!$("sort").value) $("sort").value = "updated";
  Object.keys(controls).forEach(function (name) {
    $(controls[name]).addEventListener(name === "q" ? "input" : "change", function () { visible = 24; render(); });
  });
  $("reset").addEventListener("click", reset); $("empty-reset").addEventListener("click", reset);
  $("load-more").addEventListener("click", function () { visible += 24; render(); });
  $("library-tab").addEventListener("click", function () { showView("library"); });
  $("reports-tab").addEventListener("click", function () { showView("reports"); });
  $("close-profile").addEventListener("click", function () { $("profile-dialog").close(); });
  $("profile-dialog").addEventListener("close", function () { activeTool = null; activeVersion = null; updateURL(); });
  renderEditions(); render(); showView(params.get("view") === "reports" ? "reports" : "library");
  if (params.get("tool")) openProfile(params.get("tool"), params.get("version"));
}());
