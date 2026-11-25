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

    def test_compute_and_execution_hash_lists_derive_from_one_typed_inventory(self):
        import c10s_f5_g7_source_inventory as inventory
        rows = inventory.load_inventory()["paths"]
        compute = inventory.compute_path_paths()
        execution = inventory.execution_source_hash_paths()
        self.assertEqual(len(compute), 12)
        self.assertEqual(len(execution), 32)
        self.assertEqual(len(rows), len({row["path"] for row in rows}))
        self.assertTrue(all("compute_path" in row["roles"] for row in rows if row["path"] in compute))
        self.assertEqual(set(execution.values()), {row["path"] for row in rows if "execution_source" in row["roles"]})
        self.assertEqual(validator.SOURCE_HASH_PATHS, execution)

    def test_source_inventory_rejects_duplicate_or_unclassified_paths(self):
        import c10s_f5_g7_source_inventory as inventory
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            valid = {"schema": "TGCV-C10S-F5-G7-SOURCE-INVENTORY-001", "paths": [
                {"path": "a.py", "roles": ["compute_path"], "authorization_hash_key": None},
                {"path": "a.py", "roles": ["execution_source"], "authorization_hash_key": "a_sha256"}
            ]}
            path.write_text(json.dumps(valid), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "DUPLICATE_PATH"):
                inventory.load_inventory(path)
            valid["paths"] = [{"path": "a.py", "roles": [], "authorization_hash_key": None}]
            path.write_text(json.dumps(valid), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "ROLE_INVALID"):
                inventory.load_inventory(path)

    def test_g7_workflow_requires_manual_dispatch_and_protected_environment(self):
        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\n  push:", workflow)
        self.assertIn("name: c10s-f5-g7-tiera-v1-1", workflow)
        self.assertIn("G7_ENVIRONMENT_REQUIRED_REVIEWERS_NOT_CONFIGURED", workflow)
        self.assertIn("I_APPROVE_C10S_F5_G7_TIERA_V1_1_ON_THIS_COMMIT", workflow)

if __name__ == "__main__":
    unittest.main()
