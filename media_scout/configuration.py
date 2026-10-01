"""Merge public defaults with ignored, workspace-local delivery preferences."""

from pathlib import Path
import re
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

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
    tz = config.get("timezone")
    if not isinstance(tz, str) or not tz:
        raise ValueError("Configure timezone as a valid IANA time-zone name")
    try:
        ZoneInfo(tz)
    except (ZoneInfoNotFoundError, ValueError) as error:
        raise ValueError("Configure timezone as a valid IANA time-zone name") from error
    if "daily_time" in config:
        time = config["daily_time"]
        if not isinstance(time, str) or not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", time):
            raise ValueError("Use a daily_time formatted HH:MM")
    if config.get("recipient") is not None:
        require_recipient(config["recipient"])
    if "hardware_preference" in config:
        preference = config["hardware_preference"]
        if not isinstance(preference, str) or not preference.strip():
            raise ValueError("Use a nonempty hardware_preference description")
    if "github_sync" in config:
        settings = config["github_sync"]
        if not isinstance(settings, dict):
            raise ValueError("Use a github_sync object in the public configuration")
        if "required_before_email" in settings and not isinstance(settings["required_before_email"], bool):
            raise ValueError("github_sync.required_before_email must be true or false")
    return config


def require_recipient(value):
    if not isinstance(value, str) or not re.fullmatch(r"[^\s@,;<>]+@[^\s@,;<>]+\.[^\s@,;<>]+", value):
        raise ValueError("Configure the authorized recipient in ignored config/scout.local.json before preparing email")
    return value
