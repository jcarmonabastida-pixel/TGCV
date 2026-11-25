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
        self.assertEqual(len(compute), 20)
        self.assertEqual(len(execution), 55)
        self.assertEqual(len(rows), len({row["path"] for row in rows}))
        self.assertTrue(all("compute_path" in row["roles"] for row in rows if row["path"] in compute))
        self.assertEqual(set(execution.values()), {row["path"] for row in rows if "execution_source" in row["roles"]})
        self.assertEqual(validator.SOURCE_HASH_PATHS, execution)
        self.assertIn("03_EXPERIMENTS/C10-S/design/C10S_F5_G7_INTEGRATED_GATE_CLOSURE_SPECIFICATION_001.md", set(execution.values()))

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
            self.assertEqual(len(first["compute_path"]["entries"]), 20)
            self.assertEqual(len(first["execution_source"]["entries"]), 55)
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

    def test_authorization_rejects_profile_compute_path_drift(self):
        import c10s_f5_g7_source_inventory as inventory
        from validate_c10s_f5_g7_tiera_authorization import validate_source_manifest_hashes
        entries = [{"path": path, "sha256": "a" * 64} for path in validator.SOURCE_HASH_PATHS.values()]
        source = {
            "execution_source": {"root_sha256": "b" * 64, "entries": entries},
            "compute_path": {"content_sha256": "c" * 64},
        }
        auth = {key: "a" * 64 for key in validator.SOURCE_HASH_PATHS}
        auth.update({"execution_source_manifest_sha256": "b" * 64, "compute_path_content_sha256": "c" * 64})
        validate_source_manifest_hashes(auth, source)
        auth["compute_path_content_sha256"] = "d" * 64
        with self.assertRaisesRegex(ValueError, "compute_path_content_sha256"):
            validate_source_manifest_hashes(auth, source)

    def test_inventory_covers_workflow_sources_and_g7_compute_import_closure(self):
        import ast
        import re
        import c10s_f5_g7_source_inventory as inventory
        repo_root = Path(__file__).resolve().parents[3]
        harness = repo_root / "03_EXPERIMENTS/C10-S/harness"
        rows = inventory.load_inventory()["paths"]
        execution = {row["path"] for row in rows if "execution_source" in row["roles"]}
        compute = {row["path"] for row in rows if "compute_path" in row["roles"]}

        workflow_paths = {
            ".github/workflows/c10-s-f5-g7-tiera-calibration.yml",
            ".github/workflows/c10-s-nested-mr-calibration-comparator-static.yml",
            ".github/workflows/c10s-f5-exact-certification-tests.yml",
            ".github/workflows/c10s-f5-g7-resource-profile.yml",
        }
        self.assertTrue(workflow_paths <= execution)
        fixture_directory = repo_root / "03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1"
        fixture_paths = {path.relative_to(repo_root).as_posix() for path in fixture_directory.iterdir() if path.is_file()}
        self.assertTrue(fixture_paths <= execution, "unhashed G7 profile fixtures: " + repr(sorted(fixture_paths - execution)))


        validation_workflow = (repo_root / ".github/workflows/c10s-f5-exact-certification-tests.yml").read_text(encoding="utf-8")
        compile_command = validation_workflow.split("python -m py_compile", 1)[1].split("\n      - name:", 1)[0]
        compiled = set(re.findall(r"([A-Za-z0-9_.-]+\.py)", compile_command))
        matrix_modules = set(re.findall(r"^\s+-\s+module:\s+([A-Za-z0-9_]+)\s*$", validation_workflow, re.MULTILINE))
        matrix_tests = {module + ".py" for module in matrix_modules}
        for filename in compiled | matrix_tests:
            self.assertIn("03_EXPERIMENTS/C10-S/harness/" + filename, execution, filename)

        for workflow_path in (
            ".github/workflows/c10s-f5-g7-resource-profile.yml",
            ".github/workflows/c10-s-f5-g7-tiera-calibration.yml",
        ):
            workflow_text = (repo_root / workflow_path).read_text(encoding="utf-8")
            referenced = set(re.findall(r"python\s+(?:03_EXPERIMENTS/C10-S/harness/)?([A-Za-z0-9_.-]+\.py)", workflow_text))
            for filename in referenced:
                self.assertIn("03_EXPERIMENTS/C10-S/harness/" + filename, execution, filename)

        pending = [harness / "run_c10s_f5_g7_tiera_calibration.py"]
        visited = set()
        while pending:
            current = pending.pop()
            relative = current.relative_to(repo_root).as_posix()
            if relative in visited:
                continue
            visited.add(relative)
            tree = ast.parse(current.read_text(encoding="utf-8"), filename=relative)
            for node in ast.walk(tree):
                modules = []
                if isinstance(node, ast.Import):
                    modules.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                    modules.append(node.module)
                for module in modules:
                    candidate = harness / (module.replace(".", "/") + ".py")
                    if candidate.is_file():
                        pending.append(candidate)
        self.assertTrue(visited <= compute, "missing compute-path imports: " + repr(sorted(visited - compute)))

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

    def test_g7_dispatch_guard_rejects_reuse_and_allows_only_current_run(self):
        import os
        import subprocess
        import sys
        import textwrap

        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        marker = 'gh api "repos/$GITHUB_REPOSITORY/actions/workflows/c10-s-f5-g7-tiera-calibration.yml/runs?branch=$WORKFLOW_BRANCH&event=workflow_dispatch&per_page=100"'
        self.assertIn(marker, workflow)
        after_query = workflow.split(marker, 1)[1]
        script = after_query.split("          python - <<'PY'\n", 1)[1].split("\n          PY", 1)[0]
        script = textwrap.dedent(script)

        with tempfile.TemporaryDirectory() as directory:
            payload = Path(directory) / "prior-g7-runs.json"
            env = dict(os.environ, RUNNER_TEMP=directory, RUN_ID="22", WORKFLOW_SHA="a" * 40, WORKFLOW_BRANCH="research/c10s-f5-g7-auth-C10S-F5-G7-20261125-008")

            payload.write_text(json.dumps({"workflow_runs": [
                {"id": 22, "head_sha": "a" * 40, "head_branch": env["WORKFLOW_BRANCH"], "event": "workflow_dispatch"}
            ]}), encoding="utf-8")
            current_only = subprocess.run([sys.executable, "-c", script], env=env, capture_output=True, text=True)
            self.assertEqual(current_only.returncode, 0, current_only.stderr)

            payload.write_text(json.dumps({"workflow_runs": [
                {"id": 21, "head_sha": "b" * 40, "head_branch": env["WORKFLOW_BRANCH"], "event": "workflow_dispatch"},
                {"id": 22, "head_sha": "a" * 40, "head_branch": env["WORKFLOW_BRANCH"], "event": "workflow_dispatch"}
            ]}), encoding="utf-8")
            reused = subprocess.run([sys.executable, "-c", script], env=env, capture_output=True, text=True)
            self.assertNotEqual(reused.returncode, 0)
            self.assertIn("ONE_USE_AUTHORIZATION_ALREADY_CONSUMED", reused.stderr)

            payload.write_text(json.dumps({"workflow_runs": [
                {"id": 21, "head_sha": "b" * 40, "head_branch": "research/other-auth", "event": "workflow_dispatch"},
                {"id": 22, "head_sha": "a" * 40, "head_branch": env["WORKFLOW_BRANCH"], "event": "workflow_dispatch"}
            ]}), encoding="utf-8")
            other_commit = subprocess.run([sys.executable, "-c", script], env=env, capture_output=True, text=True)
            self.assertEqual(other_commit.returncode, 0, other_commit.stderr)

    def test_g7_workflow_requires_owner_dispatch_and_records_attestation(self):
        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\n  push:", workflow)
        self.assertIn('test "$EVENT_ACTOR" = "$REPOSITORY_OWNER"', workflow)
        self.assertIn("I_APPROVE_C10S_F5_G7_TIERA_V1_1_ON_THIS_COMMIT", workflow)
        self.assertIn("TGCV-C10S-G7-DISPATCH-ATTESTATION-001", workflow)
        self.assertIn("g7-dispatch-attestation.json", workflow)
        self.assertIn('indent=2) + "\\n"', workflow)
        self.assertIn("GITHUB_WORKFLOW_DISPATCH", workflow)
        self.assertIn("concurrency:", workflow)
        self.assertIn("group: c10s-f5-g7-one-use-${{ github.ref }}", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn('test "$RUN_ATTEMPT" = "1"', workflow)
        self.assertIn("ONE_USE_AUTHORIZATION_ALREADY_CONSUMED", workflow)
        self.assertIn('run.get("head_branch") == current_branch', workflow)
        self.assertIn('run.get("event") == "workflow_dispatch"', workflow)
        self.assertIn("actions/workflows/c10-s-f5-g7-tiera-calibration.yml/runs", workflow)
        rerun_guard = "if: needs.authorization.outputs.approved == 'true' && github.run_attempt == 1"
        self.assertEqual(workflow.count(rerun_guard), 3)
        validator_source = Path(__file__).with_name("validate_c10s_f5_g7_tiera_authorization.py").read_text(encoding="utf-8")
        self.assertIn('auth.get("approval_channel") != "GITHUB_WORKFLOW_DISPATCH"', validator_source)
        self.assertNotIn("environment:", workflow)
        self.assertNotIn("deployments:", workflow)
        self.assertNotIn("required_reviewers", workflow)
        self.assertNotIn("prevent_self_review", workflow)
        authorization_checkout = workflow.split("Checkout one-use authorization commit", 1)[1].split("Set up pinned Python", 1)[0]
        self.assertIn("fetch-depth: 0", authorization_checkout)
        self.assertIn("EXPECTED_REPOSITORY_ID:", workflow)
        self.assertIn("--expected-repository-id", workflow)

if __name__ == "__main__":
    unittest.main()
