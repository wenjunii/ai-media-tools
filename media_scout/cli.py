"""Composable commands for the daily research agent and local inspection."""

import argparse
import json
from pathlib import Path
import shutil
import sys

from . import delivery
from .discovery import add_repository, collect, review_license
from .external import add_project
from .configuration import load_config
from .coverage import plan_summary, review_backlog, verify_search
from .planning import read_search_plan, search_plan
from .publication import audit_publication, export_report, rebuild_library, record_sync, verify_public_archive, verify_sync
from .report import build, verify_report
from .status import report_status
from .storage import ROOT, read_json, report_date
from .updates import export_update, prepare_update, update_workspace
from .quality import audit_existing, quality_backlog


def main():
    parser = argparse.ArgumentParser(description="Open-ended open-source AI discovery for all digital media")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("plan", "discover", "verify-search", "status", "verify", "export-report", "record-sync", "verify-sync", "prepare-email", "mark-uncertain"):
        command = sub.add_parser(name)
        command.add_argument("--date")
        if name in {"plan", "discover"}:
            command.add_argument("--plan", type=Path, help="Additional daily fields and queries")
        if name == "plan":
            command.add_argument("--full", action="store_true")
        if name in {"plan", "discover", "verify-search", "status", "verify"}:
            help_text = "Inspect a prepared or published update revision" if name == "status" else "Prepared same-day update revision"
            command.add_argument("--revision", type=int, help=help_text)
    for name in ("prepare-update", "export-update"):
        command = sub.add_parser(name)
        command.add_argument("--date")
        command.add_argument("--revision", type=int, default=2)
    command = sub.add_parser("review-backlog")
    command.add_argument("--full", action="store_true")
    command.add_argument("--date")
    command.add_argument("--revision", type=int)
    command = sub.add_parser("quality-backlog", help="Evidence gaps across published tools, including full profiles")
    command.add_argument("--full", action="store_true")
    command = sub.add_parser("audit-existing-quality", help="Reassess published records without changing dated editions")
    command.add_argument("--date", required=True)
    command = sub.add_parser("build")
    command.add_argument("--editorial", required=True, type=Path)
    command.add_argument("--revision", type=int)
    command = sub.add_parser("record-delivery")
    command.add_argument("--date")
    command.add_argument("--message-id", required=True)
    command.add_argument("--reconciled", action="store_true")
    sub.add_parser("doctor")
    sub.add_parser("audit-publication")
    sub.add_parser("verify-public-archive")
    sub.add_parser("build-library")
    command = sub.add_parser("add-repository")
    command.add_argument("repository")
    command.add_argument("--categories", nargs="+", required=True)
    command.add_argument("--date")
    command.add_argument("--revision", type=int)
    command = sub.add_parser("review-license")
    command.add_argument("repository")
    command.add_argument("--spdx", required=True)
    command.add_argument("--note", required=True)
    command.add_argument("--date")
    command.add_argument("--revision", type=int)
    command = sub.add_parser("add-project")
    command.add_argument("--metadata", type=Path, required=True)
    command.add_argument("--date")
    command.add_argument("--revision", type=int)
    args = parser.parse_args()
    try:
        config = load_config(ROOT)
        requested_day = getattr(args, "date", None)
        if args.command == "build":
            requested_day = read_json(args.editorial)["report_date"]
        day = report_date(requested_day, config["timezone"])
        root = ROOT
        if getattr(args, "revision", None) is not None and args.command not in {"prepare-update", "export-update", "status"}:
            root = update_workspace(day, args.revision, ROOT)
            config = load_config(root)
        if args.command == "plan":
            plan = search_plan(config, day, read_search_plan(args.plan) if args.plan else None)
            output = plan if args.full else plan_summary(plan)
        elif args.command == "review-backlog":
            output = review_backlog(root)
            if not args.full:
                output.pop("items")
                output["candidate_catalog"] = str(root / "state/discovery_catalog.json")
        elif args.command == "verify-search":
            output = verify_search(day, root)
        elif args.command == "audit-existing-quality":
            output = audit_existing(root, day)
        elif args.command == "quality-backlog":
            output = quality_backlog(root)
            if not args.full:
                output["pending"] = len(output.pop("items"))
        elif args.command == "discover":
            result = collect(day, root=root, plan_path=args.plan)
            output = {"report_date": day, "repositories": len(result["candidates"]),
                      "model_candidates": len(result["model_watchlist"]), "warnings": result["warnings"],
                      "discovery_file": str(root / "research" / day / "discovery.json")}
            output["search_coverage"] = verify_search(day, root, discovery=result, require_expanded=False)
        elif args.command == "build":
            output = build(args.editorial, root)
        elif args.command == "verify":
            output = verify_report(day, root)
        elif args.command == "prepare-update":
            output = {"report_date": day, "revision": args.revision,
                      "workspace": str(prepare_update(day, args.revision))}
        elif args.command == "export-update":
            output = export_update(day, args.revision)
        elif args.command == "export-report":
            output = export_report(day)
        elif args.command == "audit-publication":
            output = audit_publication()
        elif args.command == "verify-public-archive":
            output = verify_public_archive()
        elif args.command == "build-library":
            output = rebuild_library()
        elif args.command == "record-sync":
            output = record_sync(day)
        elif args.command == "verify-sync":
            output = verify_sync(day)
        elif args.command == "prepare-email":
            output = delivery.prepare(day)
        elif args.command == "record-delivery":
            output = delivery.record(day, args.message_id, reconciled=args.reconciled)
        elif args.command == "mark-uncertain":
            output = delivery.uncertain(day)
        elif args.command == "add-repository":
            item = add_repository(args.repository, args.categories, day, root)
            output = {key: item.get(key) for key in ("id", "repository", "code_license", "readme_path", "novelty")}
        elif args.command == "review-license":
            output = review_license(args.repository, args.spdx, args.note, day, root)
        elif args.command == "add-project":
            item = add_project(args.metadata, day, root)
            output = {key: item.get(key) for key in ("id", "url", "code_license", "readme_path", "novelty")}
        elif args.command == "status":
            output = report_status(day, ROOT, args.revision)
        else:
            output = {"python": sys.version.split()[0], "github_cli_available": bool(shutil.which("gh")),
                      "recipient": config["recipient"], "timezone": config["timezone"],
                      "daily_time": config["daily_time"], "categories": len(config["categories"]),
                      "scope": config.get("scope"), "max_profiles": config.get("max_profiles"),
                      "github_sync": config.get("github_sync"),
                      "synthesis": "Codex research agent; no additional model API key required",
                      "delivery": "Connected Gmail plugin; no password stored in this project"}
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, RuntimeError, OSError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
