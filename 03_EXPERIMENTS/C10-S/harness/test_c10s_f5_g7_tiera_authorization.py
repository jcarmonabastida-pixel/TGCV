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
        self.assertEqual(len(execution), 34)
        self.assertEqual(len(rows), len({row["path"] for row in rows}))
        self.assertTrue(all("compute_path" in row["roles"] for row in rows if row["path"] in compute))
        self.assertEqual(set(execution.values()), {row["path"] for row in rows if "execution_source" in row["roles"]})
        self.assertEqual(validator.SOURCE_HASH_PATHS, execution)

    def test_inventory_manifests_are_deterministic_and_bind_git_tree_bytes(self):
        import subprocess
        import c10s_f5_g7_source_inventory as inventory
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "tgcv-test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "TGCV inventory test"], cwd=root, check=True)
            repo_root = Path(__file__).resolve().parents[3]
            for row in inventory.load_inventory()["paths"]:
                target = root / row["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                if row["path"] in {
                    "03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.json",
                    "03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.py",
                }:
                    target.write_bytes((repo_root / row["path"]).read_bytes())
                else:
                    target.write_text("frozen:" + row["path"], encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "inventory snapshot"], cwd=root, check=True)
            commit1 = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            first = inventory.build_manifests(root, commit1)
            second = inventory.build_manifests(root, commit1)
            self.assertEqual(first, second)
            self.assertEqual(len(first["compute_path"]["entries"]), 12)
            self.assertEqual(len(first["execution_source"]["entries"]), 34)
            changed_path = first["compute_path"]["entries"][0]["path"]
            (root / changed_path).write_text("changed", encoding="utf-8")
            subprocess.run(["git", "add", changed_path], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "change compute source"], cwd=root, check=True)
            commit2 = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            changed = inventory.build_manifests(root, commit2)
            self.assertNotEqual(first["compute_path"]["root_sha256"], changed["compute_path"]["root_sha256"])
            self.assertNotEqual(first["execution_source"]["root_sha256"], changed["execution_source"]["root_sha256"])

    def test_execution_manifest_rejects_stale_hashes_and_unbound_inventory(self):
        from validate_c10s_f5_g7_tiera_authorization import validate_source_manifest_hashes
        import c10s_f5_g7_source_inventory as inventory
        rows = inventory.load_inventory()["paths"]
        self.assertIn("03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.json",
                      {row["path"] for row in rows if "execution_source" in row["roles"]})
        self.assertIn("03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.py",
                      {row["path"] for row in rows if "execution_source" in row["roles"]})
        entries = [{"path": path, "sha256": "a" * 64} for path in validator.SOURCE_HASH_PATHS.values()]
        execution = {"root_sha256": "b" * 64, "entries": entries}
        compute = {"content_sha256": "c" * 64}
        source_manifests = {"execution_source": execution, "compute_path": compute}
        valid = {key: "a" * 64 for key in validator.SOURCE_HASH_PATHS}
        valid.update({"execution_source_manifest_sha256": "b" * 64, "compute_path_content_sha256": "c" * 64})
        validate_source_manifest_hashes(valid, source_manifests)
        stale = dict(valid)
        stale[next(iter(validator.SOURCE_HASH_PATHS))] = "0" * 64
        with self.assertRaisesRegex(ValueError, "immutable Git tree"):
            validate_source_manifest_hashes(stale, source_manifests)
        stale_inventory = dict(valid, execution_source_manifest_sha256="0" * 64)
        with self.assertRaisesRegex(ValueError, "execution_source_manifest_sha256"):
            validate_source_manifest_hashes(stale_inventory, source_manifests)

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
