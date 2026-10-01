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
from .publication import audit_publication, export_report, record_sync, verify_sync
from .report import build, verify_report
from .storage import ROOT, read_json, report_date


def main():
    parser = argparse.ArgumentParser(description="Open-ended open-source AI discovery for all digital media")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("discover", "status", "verify", "export-report", "record-sync", "verify-sync", "prepare-email", "mark-uncertain"):
        command = sub.add_parser(name)
        command.add_argument("--date")
        if name == "discover":
            command.add_argument("--plan", type=Path, help="Additional daily fields and queries")
    command = sub.add_parser("build")
    command.add_argument("--editorial", required=True, type=Path)
    command = sub.add_parser("record-delivery")
    command.add_argument("--date")
    command.add_argument("--message-id", required=True)
    command.add_argument("--reconciled", action="store_true")
    sub.add_parser("doctor")
    sub.add_parser("audit-publication")
    command = sub.add_parser("add-repository")
    command.add_argument("repository")
    command.add_argument("--categories", nargs="+", required=True)
    command.add_argument("--date")
    command = sub.add_parser("review-license")
    command.add_argument("repository")
    command.add_argument("--spdx", required=True)
    command.add_argument("--note", required=True)
    command.add_argument("--date")
    command = sub.add_parser("add-project")
    command.add_argument("--metadata", type=Path, required=True)
    command.add_argument("--date")
    args = parser.parse_args()
    config = load_config()
    day = report_date(getattr(args, "date", None), config["timezone"])
    try:
        if args.command == "discover":
            result = collect(day, plan_path=args.plan)
            output = {"report_date": day, "repositories": len(result["candidates"]),
                      "model_candidates": len(result["model_watchlist"]), "warnings": result["warnings"],
                      "discovery_file": str(ROOT / "research" / day / "discovery.json")}
        elif args.command == "build":
            output = build(args.editorial)
        elif args.command == "verify":
            output = verify_report(day)
        elif args.command == "export-report":
            output = export_report(day)
        elif args.command == "audit-publication":
            output = audit_publication()
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
            item = add_repository(args.repository, args.categories, day)
            output = {key: item.get(key) for key in ("id", "repository", "code_license", "readme_path", "novelty")}
        elif args.command == "review-license":
            output = review_license(args.repository, args.spdx, args.note, day)
        elif args.command == "add-project":
            item = add_project(args.metadata, day)
            output = {key: item.get(key) for key in ("id", "url", "code_license", "readme_path", "novelty")}
        elif args.command == "status":
            observation = read_json(ROOT / "research" / day / "discovery.json")
            manifest = read_json(ROOT / "reports" / day / "manifest.json")
            receipt = read_json(ROOT / "state/deliveries" / (day + ".json"))
            publication = read_json(ROOT / "state/publications" / (day + ".json"))
            if manifest:
                verify_report(day)
            output = {"report_date": day, "discovered": bool(observation), "built": bool(manifest),
                      "delivery": receipt, "publication": publication,
                      "profile_count": manifest.get("profile_count") if manifest else None,
                      "warnings": observation.get("warnings", []) if observation else []}
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
