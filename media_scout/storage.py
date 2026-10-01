"""Small atomic stores, report-date validation, and process locks."""

from contextlib import contextmanager
from datetime import date, datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def read_json(path, default=None):
    path = Path(path)
    return json.loads(path.read_text()) if path.exists() else default


def write_text(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".scout-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(value)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path, value):
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def report_date(value=None, tz="America/New_York"):
    value = value or datetime.now(ZoneInfo(tz)).date().isoformat()
    if date.fromisoformat(value).isoformat() != value:
        raise ValueError("Use a report date formatted YYYY-MM-DD")
    return value


@contextmanager
def locked(root=ROOT):
    path = Path(root) / "state/scout.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("Another Scout process is active") from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)
