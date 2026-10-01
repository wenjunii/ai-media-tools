"""Check the separation between public defaults and private delivery settings."""

from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from unittest.mock import patch

from media_scout import cli
from media_scout.configuration import load_config, require_recipient
from media_scout.storage import write_json


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.defaults = self.root / "config/scout.json"
        self.local = self.root / "config/scout.local.json"
        write_json(self.defaults, {"recipient": None, "timezone": "America/New_York",
            "daily_time": "08:00", "hardware_preference": "All platforms equally",
            "categories": [{"id": "images", "name": "Images"}]})

    def test_local_preferences_leave_public_defaults_unchanged(self):
        before = self.defaults.read_bytes()
        write_json(self.local, {"recipient": "recipient@example.com", "timezone": "Europe/London",
            "daily_time": "09:30", "hardware_preference": "Linux"})
        config = load_config(self.root)
        self.assertEqual(config["recipient"], "recipient@example.com")
        self.assertEqual(config["timezone"], "Europe/London")
        self.assertEqual(config["daily_time"], "09:30")
        self.assertEqual(config["hardware_preference"], "Linux")
        self.assertEqual(config["categories"][0]["id"], "images")
        self.assertEqual(self.defaults.read_bytes(), before)

    def test_missing_local_settings_allow_research_but_require_an_email_recipient(self):
        config = load_config(self.root)
        self.assertIsNone(config["recipient"])
        with self.assertRaisesRegex(ValueError, "Configure the authorized recipient"):
            require_recipient(config["recipient"])

    def test_local_settings_cannot_hide_credentials_or_override_research_scope(self):
        for field in ("github_token", "categories"):
            write_json(self.local, {field: "private-value"})
            with self.assertRaises(ValueError) as raised:
                load_config(self.root)
            self.assertNotIn("private-value", str(raised.exception))

    def test_recipient_rejects_missing_multiple_and_header_injection_values(self):
        for value in (None, "", "address", "a@example.com,b@example.com", "a@example.com\nBcc: b@example.com"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                require_recipient(value)
        self.assertEqual(require_recipient("recipient@example.com"), "recipient@example.com")

    def test_malformed_local_preferences_fail_with_safe_errors(self):
        values = ({"timezone": []}, {"timezone": "Unknown/Private_Value"},
                  {"daily_time": None}, {"daily_time": "25:00"}, {"daily_time": 800},
                  {"recipient": False}, {"recipient": "missing-address"},
                  {"hardware_preference": []}, {"hardware_preference": " "})
        for value in values:
            with self.subTest(field=next(iter(value))):
                write_json(self.local, value)
                with self.assertRaises(ValueError) as raised:
                    load_config(self.root)
                self.assertNotIn("Private_Value", str(raised.exception))

    def test_github_options_require_an_object_and_a_boolean_gate(self):
        for settings in (None, "repository", {"required_before_email": "false"}):
            defaults = {"recipient": None, "timezone": "America/New_York", "github_sync": settings}
            write_json(self.defaults, defaults)
            with self.subTest(settings=settings), self.assertRaises(ValueError):
                load_config(self.root)

    def test_cli_configuration_error_is_json_without_traceback(self):
        output, errors = StringIO(), StringIO()
        with patch("sys.argv", ["media-scout", "doctor"]), \
                patch.object(cli, "load_config", side_effect=ValueError("Configure valid preferences")), \
                redirect_stdout(output), redirect_stderr(errors):
            self.assertEqual(cli.main(), 1)
        self.assertEqual(output.getvalue(), "")
        self.assertEqual(errors.getvalue().strip(), '{"error": "Configure valid preferences"}')

    def test_cli_invalid_date_is_json_without_traceback(self):
        output, errors = StringIO(), StringIO()
        config = load_config(self.root)
        with patch("sys.argv", ["media-scout", "verify", "--date", "../outside"]), \
                patch.object(cli, "load_config", return_value=config), \
                redirect_stdout(output), redirect_stderr(errors):
            self.assertEqual(cli.main(), 1)
        self.assertEqual(output.getvalue(), "")
        self.assertIn('"error"', errors.getvalue())
        self.assertNotIn("Traceback", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
