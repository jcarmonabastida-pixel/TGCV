"""CLI serialization contract tests for the one-use holdout authorization validator."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_c10s_nested_mr_comparative_holdout_authorization as validator


class HoldoutAuthorizationValidatorCliTests(unittest.TestCase):
    def test_cli_output_is_valid_json_with_real_newline(self):
        expected = {
            "authorization_id": "C10S-HOLDOUT-TEST-001",
            "approved_code_commit": "a" * 40,
            "scope": "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_ONLY",
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "validated-authorization.json"
            argv = [
                "validator",
                "--authorization", str(Path(directory) / "authorization.json"),
                "--root", directory,
                "--workflow-commit", "b" * 40,
                "--branch", "research/c10s-nested-mr-comparative-auth-test",
                "--output-json", str(output),
            ]
            with (
                patch("sys.argv", argv),
                patch.object(validator, "validate", return_value=expected),
            ):
                self.assertEqual(validator.main(), 0)

            raw = output.read_text(encoding="utf-8")
            self.assertTrue(raw.endswith("\n"))
            self.assertFalse(raw.endswith("\\\\n"))
            self.assertEqual(json.loads(raw), expected)


if __name__ == "__main__":
    unittest.main()
