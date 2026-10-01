"""Full-plan execution, historical lead retention and honest report coverage."""

import copy
from pathlib import Path
import tempfile
import unittest

from media_scout.client import SourceError
from media_scout.coverage import plan_summary, review_backlog, verify_search
from media_scout.discovery import collect
from media_scout.planning import plan_digest, search_plan
from media_scout.report import build, validate
from media_scout.storage import ROOT, read_json, sha256, write_json, write_text


class PublicSources:
    def __init__(self, fail_created=False):
        self.fail_created = fail_created
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(url)
        if "/search/repositories?" in url:
            if self.fail_created and "created%3A" in url:
                raise SourceError("HTTP 403 from api.github.com/search/repositories; source not collected")
            return {"total_count": 1, "items": [{"full_name": "example/art", "name": "Art",
                "html_url": "https://github.com/example/art", "license": {"spdx_id": "MIT"},
                "stargazers_count": 0, "created_at": "2026-01-01T00:00:00Z"}]}
        if "huggingface.co/api/models" in url:
            return [{"id": "example/image-model", "lastModified": "2026-10-01T00:00:00Z"}]
        if url.endswith("/readme"):
            return {"download_url": "https://raw.githubusercontent.com/example/art/main/README.md",
                    "html_url": "https://github.com/example/art/blob/main/README.md", "sha": "readme"}
        if "raw.githubusercontent.com" in url:
            return "Official documentation: local AI inference generates editable creative images."
        if "/commits?" in url:
            return [{"sha": "head", "html_url": "https://github.com/example/art/commit/head"}]
        return []


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.day = "2026-10-02"
        self.config = {"timezone": "America/New_York", "recipient": None,
            "lookback_days": 30, "items_per_query": 100, "pages_per_query": 2,
            "categories": [{"id": "images", "name": "Images", "queries": ["AI image"], "seeds": []}],
            "huggingface_pipelines": ["text-to-image"], "max_profiles": None,
            "scope": {"require_expanded_search": True}}
        write_json(self.root / "config/scout.json", self.config)

    def collect(self, fail_created=False):
        return collect(self.day, self.root, PublicSources(fail_created))

    def snapshot(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def editorial(self):
        return {"report_date": self.day, "summary": "Full search; detailed review continues.", "tools": [],
                "category_notes": [{"category": "images", "text": "A creative AI source awaits full review.",
                                    "source_urls": ["https://github.com/example/art"]}]}

    def test_default_configuration_executes_all_three_lanes_for_all_starter_terms(self):
        plan = search_plan(read_json(ROOT / "config/scout.json"), self.day)
        self.assertEqual(plan_summary(plan)["github_queries"], 189)
        self.assertEqual(plan_summary(plan)["query_lanes"], {"pushed": 63, "created": 63, "any": 63})
        self.assertEqual(plan_summary(plan)["fields"], 30)
        self.assertEqual(plan_summary(plan)["model_tasks"], 13)
        for category in plan["categories"]:
            for term in category["queries"]:
                self.assertEqual({q["window"] for q in plan["queries"]
                    if q["category"] == category["id"] and q["terms"] == term}, {"pushed", "created", "any"})

    def test_daily_plan_can_increase_existing_query_pages_and_add_model_tasks(self):
        plan = search_plan(self.config, self.day, {"additional_pipelines": ["audio-to-audio"],
            "queries": [{"category": "images", "terms": "AI image", "window": "pushed", "pages": 5}]})
        self.assertEqual(len(plan["queries"]), 3)
        self.assertEqual(plan["queries"][0]["pages"], 5)
        self.assertEqual(plan["huggingface_pipelines"], ["text-to-image", "audio-to-audio"])

    def test_resume_rejects_a_changed_explicit_plan_before_source_or_state_updates(self):
        self.collect()
        plan_path = self.root / "plan.json"
        write_json(plan_path, {"queries": [{"category": "images", "terms": "AI image", "pages": 5}]})
        before, source = self.snapshot(), PublicSources()
        with self.assertRaisesRegex(ValueError, "next edition"):
            collect(self.day, self.root, source, plan_path)
        self.assertEqual(source.calls, [])
        self.assertEqual(self.snapshot(), before)

    def test_matching_plan_resumes_against_archived_defaults_without_recollection(self):
        plan_path = self.root / "plan.json"
        write_json(plan_path, {"queries": [{"category": "images", "terms": "AI image", "pages": 5}]})
        original = collect(self.day, self.root, PublicSources(), plan_path)
        changed = dict(self.config, pages_per_query=7, huggingface_pipelines=["audio-to-audio"],
                       categories=[{"id": "haptics", "name": "Tactile AI", "queries": ["AI haptics"]}],
                       scope={"require_expanded_search": True, "new_preference": True})
        write_json(self.root / "config/scout.json", changed)
        before, source = self.snapshot(), PublicSources()
        self.assertEqual(collect(self.day, self.root, source, plan_path), original)
        self.assertEqual(collect(self.day, self.root, source), original)
        self.assertEqual(source.calls, [])
        self.assertEqual(self.snapshot(), before)

    def test_resume_rejects_a_tampered_archive_before_state_updates(self):
        self.collect()
        plan_path = self.root / "plan.json"
        write_json(plan_path, {})
        archive_path = self.root / "research" / self.day / "queries/search-plan.json"
        archived = read_json(archive_path)
        archived["queries"].pop()
        write_json(archive_path, archived)
        before, source = self.snapshot(), PublicSources()
        with self.assertRaisesRegex(ValueError, "integrity check"):
            collect(self.day, self.root, source, plan_path)
        self.assertEqual(source.calls, [])
        self.assertEqual(self.snapshot(), before)

    def test_resume_requires_both_archived_plan_and_config_for_explicit_plan(self):
        self.collect()
        plan_path = self.root / "plan.json"
        write_json(plan_path, {})
        for name in ("search-plan.json", "config-snapshot.json"):
            path = self.root / "research" / self.day / "queries" / name
            contents = path.read_bytes()
            path.unlink()
            before, source = self.snapshot(), PublicSources()
            with self.subTest(missing=name), self.assertRaisesRegex(ValueError, "omit --plan"):
                collect(self.day, self.root, source, plan_path)
            self.assertEqual(source.calls, [])
            self.assertEqual(self.snapshot(), before)
            path.write_bytes(contents)

    def test_legacy_observation_resumes_without_claiming_a_new_plan_was_applied(self):
        original = {"report_date": self.day, "candidates": [], "model_watchlist": []}
        write_json(self.root / "research" / self.day / "discovery.json", original)
        source = PublicSources()
        self.assertEqual(collect(self.day, self.root, source), original)
        plan_path = self.root / "plan.json"
        write_json(plan_path, {})
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "no archived expanded plan"):
            collect(self.day, self.root, source, plan_path)
        self.assertEqual(source.calls, [])
        self.assertEqual(self.snapshot(), before)

    def test_missing_or_nonobject_plan_is_rejected_before_new_source_collection(self):
        plan_path, source = self.root / "plan.json", PublicSources()
        with self.assertRaisesRegex(ValueError, "JSON object"):
            collect(self.day, self.root, source, plan_path)
        write_json(plan_path, None)
        with self.assertRaisesRegex(ValueError, "JSON object"):
            collect(self.day, self.root, source, plan_path)
        self.assertEqual(source.calls, [])
        self.assertFalse((self.root / "research" / self.day).exists())

    def test_full_collection_is_verified_and_baseline_has_no_age_or_star_floor(self):
        observation = self.collect()
        summary = verify_search(self.day, self.root)
        self.assertEqual(summary["attempted_github_queries"], 3)
        self.assertEqual(summary["source_candidates"], 1)
        self.assertEqual(summary["model_candidates"], 1)
        self.assertEqual(summary["attempted_model_queries"], 1)
        baseline = observation["coverage"][2]["query"]
        self.assertNotIn("created:", baseline)
        self.assertNotIn("pushed:", baseline)
        self.assertNotIn("stars:", baseline)

    def test_omitted_query_blocks_report_before_artifact_creation(self):
        observation = self.collect()
        observation["coverage"].pop(0)
        write_json(self.root / "research" / self.day / "discovery.json", observation)
        path = self.root / "editorial.json"
        write_json(path, self.editorial())
        with self.assertRaisesRegex(ValueError, "every planned repository query"):
            build(path, self.root)
        self.assertFalse((self.root / "reports" / self.day / "report.json").exists())

    def test_changing_the_archived_plan_cannot_relabel_a_pilot_as_full(self):
        self.collect()
        path = self.root / "research" / self.day / "queries/search-plan.json"
        plan = read_json(path)
        plan["queries"].pop()
        write_json(path, plan)
        with self.assertRaisesRegex(ValueError, "differs"):
            verify_search(self.day, self.root)

    def test_missing_model_task_is_not_silently_ignored(self):
        observation = self.collect()
        observation["coverage"] = [c for c in observation["coverage"] if c["provider"] != "huggingface"]
        with self.assertRaisesRegex(ValueError, "every planned model task"):
            verify_search(self.day, self.root, observation)

    def test_a_self_consistent_pilot_plan_still_cannot_omit_configured_searches(self):
        observation = self.collect()
        path = self.root / "research" / self.day / "queries/search-plan.json"
        plan = read_json(path)
        plan["queries"].pop(0)
        observation["coverage"].pop(0)
        observation["search_plan_sha256"] = plan_digest(plan)
        write_json(path, plan)
        with self.assertRaisesRegex(ValueError, "omits configured"):
            verify_search(self.day, self.root, observation)

    def test_false_query_identity_is_rejected(self):
        observation = self.collect()
        observation["coverage"][0]["query"] = "unrelated pilot query"
        with self.assertRaisesRegex(ValueError, "contradicts"):
            verify_search(self.day, self.root, observation)

    def test_failed_sources_remain_visible_in_complete_search_and_report(self):
        self.collect(fail_created=True)
        path = self.root / "editorial.json"
        write_json(path, self.editorial())
        build(path, self.root)
        report = read_json(self.root / "reports" / self.day / "report.json")
        self.assertEqual(report["search_coverage"]["failed_github_queries"], 1)
        self.assertEqual(report["search_coverage"]["attempted_github_queries"], 3)
        self.assertEqual(report["search_coverage"]["full_profiles"], 0)
        for extension in ("html", "md"):
            text = (self.root / "reports" / self.day / ("report." + extension)).read_text()
            self.assertIn("3/3 repository queries attempted", text)
            self.assertIn("1 failed repository queries", text)
            self.assertIn("not verified recommendations", text)

    def test_web_ecosystems_need_evidence_or_an_explicit_collection_gap(self):
        observation = self.collect()
        config = copy.deepcopy(self.config)
        config["scope"]["required_ecosystems"] = ["gitlab", "packages"]
        editorial = self.editorial()
        with self.assertRaisesRegex(ValueError, "every required web ecosystem"):
            validate(editorial, observation, config, {})
        editorial["ecosystem_checks"] = [
            {"ecosystem": "gitlab", "status": "searched", "checked_on": self.day,
             "finding": "Official project documentation inspected.", "source_urls": ["https://gitlab.com/example/art"]},
            {"ecosystem": "packages", "status": "gap", "checked_on": self.day,
             "finding": "Registry was unavailable; no complete package research claimed.", "source_urls": []}]
        self.assertIs(validate(editorial, observation, config, {}), editorial)
        editorial["ecosystem_checks"].append({"ecosystem": "new-creative-source", "status": "gap",
            "checked_on": self.day, "finding": "Newly noticed source group awaits research.", "source_urls": []})
        self.assertIs(validate(editorial, observation, config, {}), editorial)
        editorial["ecosystem_checks"][0]["source_urls"] = []
        with self.assertRaisesRegex(ValueError, "primary-source links"):
            validate(editorial, observation, config, {})

    def test_metadata_only_license_cannot_promote_a_candidate_to_a_screened_lead(self):
        observation = self.collect()
        config = copy.deepcopy(self.config)
        config["scope"]["require_license_review"] = True
        candidate = observation["candidates"][0]
        url = "https://github.com/example/art"
        license_url = url + "/blob/main/LICENSE"
        editorial = self.editorial()
        editorial["leads"] = [{"id": candidate["id"], "name": "Art", "categories": ["images"],
            "checked_on": self.day, "code_license": "MIT", "good_for": "Editable image generation",
            "review_status": "Installation, requirements and output quality pending.",
            "sources": [{"title": "Official docs", "url": url}, {"title": "License", "url": license_url}],
            "ai_relevance": {"text": "Local AI model inference assists editable digital image creation.", "source_urls": [url]}}]
        with self.assertRaisesRegex(ValueError, "complete reviewed software license"):
            validate(editorial, observation, config, {})
        path = self.root / "research" / self.day / "evidence/LICENSE.txt"
        write_text(path, "Complete test fixture license text.")
        candidate["license_review"] = {"reviewed_spdx": "MIT", "path": str(path.relative_to(self.root)),
            "sha256": sha256(path), "url": license_url, "note": "Complete software terms reviewed; no additional use restriction."}
        self.assertIs(validate(editorial, observation, config, {}), editorial)
        write_json(self.root / "config/scout.json", config)
        write_json(self.root / "research" / self.day / "discovery.json", observation)
        write_text(path, "Tampered terms.")
        editorial_path = self.root / "editorial.json"
        write_json(editorial_path, editorial)
        with self.assertRaisesRegex(ValueError, "match the archived"):
            build(editorial_path, self.root)

    def test_legacy_observation_is_preserved_and_never_claimed_as_expanded(self):
        legacy = {"report_date": self.day, "coverage": [], "candidates": []}
        with self.assertRaisesRegex(ValueError, "predates"):
            verify_search(self.day, self.root, legacy)
        self.assertEqual(verify_search(self.day, self.root, legacy, False)["tracking"], "legacy")

    def test_historical_pilot_candidates_survive_without_becoming_recommendations(self):
        items = {f"github:example/{name}": {"first_seen": "2026-10-01", "last_seen": "2026-10-01",
            "candidate": {"id": f"github:example/{name}", "name": name,
                          "url": f"https://github.com/example/{name}", "stars": 0,
                          "categories": ["unfamiliar-field"], "code_license": "UNKNOWN"}}
            for name in ("raw-pilot", "screened", "profiled")}
        write_json(self.root / "state/discovery_catalog.json", items)
        write_json(self.root / "state/catalog.json", {"github:example/profiled": {}})
        write_json(self.root / "state/review_queue.json", {"github:example/screened": {}})
        backlog = review_backlog(self.root)
        self.assertEqual(backlog["unprofiled_candidates"], 2)
        self.assertEqual(backlog["items"][0]["review"], "profile-pending")
        self.assertEqual(backlog["items"][1]["review"], "eligibility-not-established")
        self.assertEqual(backlog["items"][1]["categories"], ["unfamiliar-field"])
