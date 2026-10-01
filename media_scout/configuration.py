"""Merge public defaults with ignored, workspace-local delivery preferences."""

from pathlib import Path
import re
from zoneinfo import ZoneInfo

from .storage import ROOT, read_json

LOCAL_FIELDS = {"recipient", "timezone", "daily_time", "hardware_preference"}


def load_config(root=ROOT):
    root = Path(root)
    config = read_json(root / "config/scout.json")
    if not isinstance(config, dict):
        raise ValueError("Read the project's config/scout.json defaults")
    local = read_json(root / "config/scout.local.json", {})
    if not isinstance(local, dict) or set(local) - LOCAL_FIELDS:
        raise ValueError("Local settings may only override recipient, timezone, daily_time and hardware_preference")
    config = dict(config, **local)
    if config.get("timezone"):
        ZoneInfo(config["timezone"])
    if config.get("daily_time") and not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", config["daily_time"]):
        raise ValueError("Use a daily_time formatted HH:MM")
    return config


def require_recipient(value):
    if not isinstance(value, str) or not re.fullmatch(r"[^\s@,;<>]+@[^\s@,;<>]+\.[^\s@,;<>]+", value):
        raise ValueError("Configure the authorized recipient in ignored config/scout.local.json before preparing email")
    return value
