from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import validate_c10s_f5_g7_tiera_authorization as validator


class F5G7AuthorizationTests(unittest.TestCase):
    def test_validator_targets_v1_1_protocol(self):
        self.assertEqual(validator.PROTOCOL_VERSION, "1.1")

    def test_authorization_manifest_path_matches_pinned_fixture(self):
        self.assertEqual(
            validator.RESOURCE_PROFILE_MANIFEST_PATH,
            "03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json",
        )

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

    def test_g7_workflow_requires_manual_dispatch_and_protected_environment(self):
        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\\n  push:", workflow)
        self.assertIn("name: c10s-f5-g7-tiera-v1-1", workflow)
        self.assertIn("G7_ENVIRONMENT_REQUIRED_REVIEWERS_NOT_CONFIGURED", workflow)
        self.assertIn("I_APPROVE_C10S_F5_G7_TIERA_V1_1_ON_THIS_COMMIT", workflow)

if __name__ == "__main__":
    unittest.main()
