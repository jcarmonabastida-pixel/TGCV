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
        self.assertEqual(len(compute), 19)
        self.assertEqual(len(execution), 56)
        self.assertEqual(len(rows), len({row["path"] for row in rows}))
        self.assertTrue(all("compute_path" in row["roles"] for row in rows if row["path"] in compute))
        self.assertEqual(set(execution.values()), {row["path"] for row in rows if "execution_source" in row["roles"]})
        manifest_generator = "03_EXPERIMENTS/C10-S/harness/create_c10s_f5_g7_resource_profile_manifest.py"
        self.assertNotIn(manifest_generator, compute)
        self.assertIn(manifest_generator, execution.values())
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
            self.assertEqual(len(first["compute_path"]["entries"]), 19)
            self.assertEqual(len(first["execution_source"]["entries"]), 56)
            changed_path = first["compute_path"]["entries"][0]["path"]
            (root / changed_path).write_text("changed", encoding="utf-8")
            subprocess.run(["git", "add", changed_path], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "change compute source"], cwd=root, check=True)
            commit2 = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            changed = inventory.build_manifests(root, commit2)
            self.assertNotEqual(first["compute_path"]["root_sha256"], changed["compute_path"]["root_sha256"])
            self.assertNotEqual(first["execution_source"]["root_sha256"], changed["execution_source"]["root_sha256"])

    def test_authorization_manifest_builder_matches_validator_canonical_manifests(self):
        import subprocess
        import c10s_f5_g7_source_inventory as inventory
        from build_c10s_f5_g7_authorization_manifest import build_authorization_manifest_bindings
        from validate_c10s_f5_g7_tiera_authorization import validate_source_manifest_hashes

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "tgcv-test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "TGCV manifest builder test"], cwd=root, check=True)
            repo_root = Path(__file__).resolve().parents[3]
            canonical_files = {
                "03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.json",
                "03_EXPERIMENTS/C10-S/harness/c10s_f5_g7_source_inventory.py",
                "03_EXPERIMENTS/C10-S/harness/build_c10s_f5_g7_authorization_manifest.py",
            }
            for row in inventory.load_inventory()["paths"]:
                target = root / row["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                if row["path"] in canonical_files:
                    target.write_bytes((repo_root / row["path"]).read_bytes())
                else:
                    target.write_text("frozen:" + row["path"], encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "manifest builder fixture"], cwd=root, check=True)
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()

            manifests = inventory.build_manifests(root, commit)
            bindings = build_authorization_manifest_bindings(root, commit)

            self.assertEqual(bindings["approved_code_commit"], commit)
            self.assertEqual(
                bindings["execution_source_manifest_sha256"],
                manifests["execution_source"]["root_sha256"],
            )
            self.assertEqual(
                bindings["compute_path_content_sha256"],
                manifests["compute_path"]["content_sha256"],
            )
            self.assertEqual(len(bindings["source_hashes"]), 56)
            auth = dict(bindings["source_hashes"])
            auth["execution_source_manifest_sha256"] = bindings["execution_source_manifest_sha256"]
            auth["compute_path_content_sha256"] = bindings["compute_path_content_sha256"]
            validate_source_manifest_hashes(auth, manifests)

    def test_manifest_builder_only_generates_draft_authorizations(self):
        from build_c10s_f5_g7_authorization_manifest import (
            BINDINGS_SCHEMA,
            build_draft_authorization,
        )

        bindings = {
            "schema": BINDINGS_SCHEMA,
            "approved_code_commit": "a" * 40,
            "execution_source_manifest_sha256": "b" * 64,
            "compute_path_content_sha256": "c" * 64,
            "source_hashes": {"sample_sha256": "d" * 64},
        }
        draft = build_draft_authorization({"status": "DRAFT", "authorization_id": "draft-only"}, bindings)
        self.assertEqual(draft["status"], "DRAFT")
        self.assertEqual(draft["approved_code_commit"], "a" * 40)
        self.assertEqual(draft["sample_sha256"], "d" * 64)
        with self.assertRaisesRegex(ValueError, "MUST_BE_DRAFT"):
            build_draft_authorization({"status": "APPROVED"}, bindings)

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

    def test_g7_dispatch_gate_allows_retry_after_non_consuming_preflight_failure(self):
        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration-v3.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        authorization = workflow.split("  authorization:", 1)[1].split("  resource_preflight_validation:", 1)[0]
        preflight = workflow.split("  resource_preflight_validation:", 1)[1].split("  consume_authorization:", 1)[0]
        consumption = workflow.split("  consume_authorization:", 1)[1].split("  primary_bank:", 1)[0]
        self.assertNotIn("prior-g7-runs.json", authorization)
        self.assertNotIn("ONE_USE_AUTHORIZATION_ALREADY_CONSUMED", authorization)
        self.assertNotIn("Permanently consume authorization", authorization)
        self.assertIn("test \"$RUN_ATTEMPT\" = \"1\"", authorization)
        self.assertIn("MANIFEST=\"$REPO_ROOT/03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json\"", preflight)
        self.assertIn('--manifest "$MANIFEST"', preflight)
        self.assertNotIn("--manifest fixtures/g7_resource_profile_v1_1/manifest.json", preflight)
        self.assertIn("needs: [authorization, resource_preflight_validation]", workflow.split("  consume_authorization:",1)[1].split("  primary_bank:",1)[0])
        self.assertIn("needs.resource_preflight_validation.result == 'success'", consumption)
        self.assertIn("TGCV-C10S-G7-AUTHORIZATION-CONSUMED-002", consumption)
        self.assertIn("resource_profile_sha256", consumption)
        self.assertIn('gh api --method PUT "repos/$GITHUB_REPOSITORY/contents/$MARKER_PATH"', consumption)
        self.assertIn('test "$PARENT_SHA" = "$WORKFLOW_SHA"', consumption)
        self.assertNotIn("contents: write", authorization)

    def test_g7_workflow_requires_owner_dispatch_and_records_attestation(self):
        workflow_path = Path(__file__).resolve().parents[3] / ".github/workflows/c10-s-f5-g7-tiera-calibration-v3.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn('test "$EVENT_ACTOR" = "$REPOSITORY_OWNER"', workflow)
        self.assertIn("I_APPROVE_C10S_F5_G7_TIERA_V1_1_ON_THIS_COMMIT", workflow)
        self.assertIn("TGCV-C10S-G7-DISPATCH-ATTESTATION-001", workflow)
        self.assertIn("g7-dispatch-attestation.json", workflow)
        self.assertIn("concurrency:", workflow)
        self.assertIn("group: c10s-f5-g7-one-use-${{ github.ref }}", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn('test "$RUN_ATTEMPT" = "1"', workflow)
        self.assertNotIn("ONE_USE_AUTHORIZATION_ALREADY_CONSUMED", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("consume_authorization:", workflow)
        self.assertIn("Permanently consume authorization", workflow) if "Permanently consume authorization" in workflow else self.assertIn("Atomically consume authorization after successful preflight", workflow)
        self.assertIn("TGCV-C10S-G7-AUTHORIZATION-CONSUMED-002", workflow)
        self.assertIn('gh api --method PUT "repos/$GITHUB_REPOSITORY/contents/$MARKER_PATH"', workflow)
        self.assertIn('test "$PARENT_SHA" = "$WORKFLOW_SHA"', workflow)
        self.assertIn("dispatch_workflow_git_blob_sha", workflow)
        self.assertIn("WORKFLOW_COMMIT: ${{ github.sha }}", workflow)
        self.assertIn("?ref=$WORKFLOW_COMMIT", workflow)
        rerun_guard = "if: needs.authorization.outputs.approved == 'true' && github.run_attempt == 1"
        self.assertGreaterEqual(workflow.count(rerun_guard), 3)
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

    def test_non_authorizing_draft_identity_is_fresh_and_commit_bound(self):
        repo_root = Path(__file__).resolve().parents[3]
        workflow = (repo_root / ".github/workflows/c10s-f5-exact-certification-tests.yml").read_text(encoding="utf-8")
        self.assertIn('AUTHORIZATION_ID="C10S-F5-G7-${GITHUB_SHA:0:12}"', workflow)
        self.assertIn('AUTHORIZATION_BRANCH="research/c10s-f5-g7-auth-${AUTHORIZATION_ID}"', workflow)
        self.assertIn('"authorization_id": os.environ["AUTHORIZATION_ID"]', workflow)
        self.assertIn('"authorization_branch": os.environ["AUTHORIZATION_BRANCH"]', workflow)
        self.assertNotIn('"authorization_id": "C10S-F5-G7-20261126-001"', workflow)
        self.assertNotIn('"authorization_branch": "research/c10s-f5-g7-auth-C10S-F5-G7-20261126-001"', workflow)

if __name__ == "__main__":
    unittest.main()
