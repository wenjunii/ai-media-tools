"""Check the separation between public defaults and private delivery settings."""

from pathlib import Path
import tempfile
import unittest

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


if __name__ == "__main__":
    unittest.main()
