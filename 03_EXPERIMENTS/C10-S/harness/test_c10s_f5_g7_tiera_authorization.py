from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import validate_c10s_f5_g7_tiera_authorization as validator


class F5G7AuthorizationTests(unittest.TestCase):
    def test_validator_targets_v1_1_protocol(self):
        self.assertEqual(validator.PROTOCOL_VERSION, "1.1")

    def test_validator_rejects_draft_authorization(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "auth.json"
            path.write_text(json.dumps({
                "schema": validator.AUTH_SCHEMA,
                "status": "DRAFT",
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                validator.validate(
                    path, Path(directory), "a" * 40,
                    validator.BRANCH_PREFIX + "C10S-F5-G7-20261120-001",
                )

    def test_validator_requires_dedicated_branch(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "auth.json"
            path.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "dedicated F5 G7"):
                validator.validate(path, Path(directory), "a" * 40, "research/other")


if __name__ == "__main__":
    unittest.main()
