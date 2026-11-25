from __future__ import annotations

import base64
import hashlib
import io
import json
import tempfile
import subprocess
import zipfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from pathlib import Path

import validate_c10s_f5_g7_resource_profile as validator
import profile_c10s_f5_g7_resource_preflight_parallel as profiler
import run_c10s_f5_g7_tiera_calibration as g7


class F5G7ResourceProfileTests(unittest.TestCase):
    def test_resource_profile_json_digest_is_hash_bound(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "profile.json"
            manifest = root / "manifest.json"
            profile.write_text(json.dumps({"schema": "not-the-profile"}), encoding="utf-8")
            manifest.write_text(json.dumps({
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-003",
                "profile_json_sha256": "0" * 64,
                "profile_source_commit": "a" * 40,
                "profile_run_id": 45000000001,
                "profile_artifact_id": 14799999999,
                "profile_artifact_archive_sha256": "b" * 64,
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "JSON_DIGEST_MISMATCH"):
                validator.validate(profile, manifest, root)

    def test_shard_plan_uses_immutable_original_v1_1_profile_artifact_and_manifest(self):
        """Run the official dimensioner against the exact archived profile and manifest."""
        fixture_dir = (
            Path(__file__).resolve().parents[1]
            / "fixtures"
            / "g7_resource_profile_v1_1"
        )
        profile_zip = base64.b64decode(
            (fixture_dir / "profile_artifact.zip.b64").read_text(encoding="ascii")
        )
        self.assertEqual(
            hashlib.sha256(profile_zip).hexdigest(),
            "14e317a6f38d9934dc0903b4b038da5ffc580c9bb076d26dbcc6e47cfe568e21",
        )
        with zipfile.ZipFile(io.BytesIO(profile_zip)) as archive:
            profile_bytes = archive.read("c10s-f5-g7-resource-profile.json")
        manifest_path = fixture_dir / "manifest.json"
        manifest_bytes = manifest_path.read_bytes()
        self.assertEqual(
            hashlib.sha256(manifest_bytes).hexdigest(),
            "470d2b77eb3a6a64a14cd68459bc4ab534a36eb53b1f54c1942f784498a2a639",
        )
        profile = json.loads(profile_bytes)
        manifest = json.loads(manifest_bytes)
        self.assertEqual(
            hashlib.sha256(profile_bytes).hexdigest(),
            manifest["profile_json_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(profile_zip).hexdigest(),
            manifest["profile_artifact_archive_sha256"],
        )
        self.assertEqual(manifest["profile_run_id"], 45365559253)
        self.assertEqual(manifest["profile_artifact_id"], 14908914198)
        self.assertEqual(profile["K_per_cell"], 100)
        self.assertEqual(profile["C0_B"], 1000)
        self.assertEqual(profile["C5_B"], 1000)
        self.assertEqual(profile["coverage_adjudication"], "NOT_PERFORMED")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile_path = root / "profile.json"
            staged_manifest_path = root / "manifest.json"
            profile_path.write_bytes(profile_bytes)
            staged_manifest_path.write_bytes(manifest_bytes)
            fake_entries = [{"path": path, "sha256": "a" * 64} for path in validator.PROFILE_SOURCE_PATHS]
            fake_manifest = {"entries": fake_entries, "root_sha256": "b" * 64, "content_sha256": "c" * 64}
            with patch.object(
                validator.subprocess, "run", return_value=SimpleNamespace(returncode=0)
            ), patch.object(
                validator.subprocess, "check_output", return_value=b"frozen-compute-path"
            ), patch.object(
                validator, "build_manifests", return_value={"compute_path": fake_manifest}
            ):
                result = validator.validate(profile_path, staged_manifest_path, root)

        self.assertEqual(result["datasets_per_shard"], 8)
        self.assertEqual(result["shard_tasks_per_phase"], 250)
        self.assertEqual(result["matrix_job_count"], 250)
        self.assertEqual(result["job_topology"], "ONE_MATRIX_JOB_EXECUTES_PRIMARY_AND_CLEAN_SOURCE_REPLAY_SEQUENTIALLY")
        self.assertEqual(result["max_parallel_jobs"], 20)
        self.assertEqual(len(result["shard_matrix"]), 250)
        for cell_id in ("F5_beta22_M10_R5", "F5_beta22_M30_R20"):
            self.assertEqual(
                sum(1 for item in result["shard_matrix"] if item["cell_id"] == cell_id),
                125,
            )
        slow = result["selected_shard_projection"]["per_cell"]["F5_beta22_M30_R20"]
        self.assertAlmostEqual(
            slow["max_observed_primary_replay_job_runtime_seconds"],
            8491.11420136,
            places=5,
        )
        self.assertLessEqual(
            slow["max_observed_primary_replay_job_runtime_seconds"],
            validator.JOB_BUDGET_SECONDS,
        )
        self.assertEqual(slow["shards"], 125)
        self.assertAlmostEqual(
            slow["aggregate_primary_replay_compute_seconds"],
            125 * 8491.11420136,
            places=4,
        )
        by_size = {
            item["datasets_per_shard"]: item
            for item in result["candidate_shard_projections"]
        }
        self.assertTrue(by_size[10]["safe_primary_replay_pair_under_150_minute_job_budget"])
        for size in (10, 20, 25, 40, 50, 100):
            self.assertFalse(by_size[size]["safe_primary_replay_pair_under_150_minute_job_budget"])
        fast_job = 2 * (8 * 7.966771501000004 + 900)
        slow_job = 2 * (8 * 418.194637585 + 900)
        total_runner_compute = 125 * fast_job + 125 * slow_job
        expected_primary_replay = (
            total_runner_compute / validator.MAX_PARALLEL
            + (1 - 1 / validator.MAX_PARALLEL) * slow_job
        )
        self.assertAlmostEqual(
            result["primary_plus_replay_conservative_wall_seconds"],
            expected_primary_replay,
            places=5,
        )
        selected = result["selected_shard_projection"]
        self.assertAlmostEqual(
            selected["primary_replay_aggregate_compute_hours"],
            total_runner_compute / 3600,
            places=8,
        )
        self.assertAlmostEqual(
            selected["shared_matrix_wall_workload_lower_bound_seconds"],
            total_runner_compute / validator.MAX_PARALLEL,
            places=5,
        )
        self.assertAlmostEqual(
            selected["shared_matrix_list_scheduling_tail_bound_seconds"],
            (1 - 1 / validator.MAX_PARALLEL) * slow_job,
            places=5,
        )
        self.assertEqual(result["coverage_adjudication"], "NOT_PERFORMED")
        self.assertEqual(result["job_setup_overhead_status"], "ENGINEERING_RESERVE_NOT_EMPIRICALLY_MEASURED")
        sensitivity = {item["per_phase_setup_allowance_seconds"]: item for item in result["job_setup_overhead_sensitivity"]}
        self.assertTrue(sensitivity[300]["within_150_minute_job_budget"])
        self.assertTrue(sensitivity[600]["within_150_minute_job_budget"])
        self.assertTrue(sensitivity[900]["within_150_minute_job_budget"])
        self.assertEqual(result["resource_sample_k_per_cell"], 100)
        self.assertAlmostEqual(
            result["probability_sample_max_exceeds_true_p99_under_iid_assumption"],
            1 - (0.99 ** 100),
            places=12,
        )
        self.assertEqual(
            result["runtime_extrapolation_status"],
            "CONDITIONAL_K100_SAMPLE_MAX_IS_NOT_A_K1000_HARD_BOUND",
        )

    def test_resource_profile_rejects_unexpected_schema_before_compatibility_check(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "profile.json"
            manifest = root / "manifest.json"
            profile_bytes = json.dumps({"schema": "wrong"}).encode()
            profile.write_bytes(profile_bytes)
            manifest.write_text(json.dumps({
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-003",
                "profile_json_sha256": hashlib.sha256(profile_bytes).hexdigest(),
                "profile_source_commit": "a" * 40,
                "profile_run_id": 45000000001,
                "profile_artifact_id": 14799999999,
                "profile_artifact_archive_sha256": "b" * 64,
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "PROTOCOL_MISMATCH"):
                validator.validate(profile, manifest, root)


    def test_v1_1_resource_profile_records_timing_only_and_never_inspects_outcomes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "profile.json"
            specs = [
                SimpleNamespace(cell_id="F5_beta22_M10_R5"),
                SimpleNamespace(cell_id="F5_beta22_M30_R20"),
            ]

            def fake_run_cell(spec, *, k, c0_b, c5_b, seed_namespace, adjudicate):
                for replicate in range(k):
                    g7.compare_dataset(
                        ((0.0, 1.0),),
                        dataset_id=f"{seed_namespace}:{spec.cell_id}:{replicate}",
                    )
                return {
                    "datasets_completed": k,
                    "coverage_adjudication": "NOT_PERFORMED_RESOURCE_ONLY",
                }

            with patch.object(g7, "f5_specs", return_value=specs), patch.object(
                g7, "RESOURCE_K_PER_CELL", 2
            ), patch.object(g7, "K_PER_CELL", 10), patch.object(
                g7, "validate_seed_separation"
            ), patch.object(g7, "run_cell", side_effect=fake_run_cell), patch.object(
                g7, "compare_dataset", return_value=object()
            ):
                result = profiler.profile(output)

            self.assertEqual(result["coverage_adjudication"], "NOT_PERFORMED")
            self.assertEqual(result["scope"], validator.PROFILE_SCOPE)
            for cell in result["cells"]:
                self.assertNotIn("certificate_status_counts", cell)
                self.assertNotIn("interval_emission_counts", cell)
                self.assertEqual(cell["datasets_completed"], 2)
            for rows in result["dataset_timings"].values():
                self.assertEqual(len(rows), 2)
                self.assertTrue(all(set(row) == {"dataset_id", "wall_seconds"} for row in rows))
            self.assertIn("No certificate status", result["interpretation"])
            self.assertNotIn("interval_emission_counts", json.dumps(result))


    def test_real_git_repository_ancestry_and_compute_path_identity(self):
        import c10s_f5_g7_source_inventory as inventory
        fixture_dir = Path(__file__).resolve().parents[1] / "fixtures" / "g7_resource_profile_v1_1"
        profile_zip = base64.b64decode((fixture_dir / "profile_artifact.zip.b64").read_text(encoding="ascii"))
        with zipfile.ZipFile(io.BytesIO(profile_zip)) as archive:
            profile = json.loads(archive.read("c10s-f5-g7-resource-profile.json"))
        original_manifest = json.loads((fixture_dir / "manifest.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "tgcv-test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "TGCV integration test"], cwd=root, check=True)
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
                    target.write_bytes(("frozen:" + row["path"]).encode("utf-8"))
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "profile source snapshot"], cwd=root, check=True)
            source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            profile["source_commit"] = source_commit
            profile_bytes = json.dumps(profile, sort_keys=True, indent=2).encode("utf-8")
            manifest = dict(original_manifest, profile_source_commit=source_commit,
                            profile_json_sha256=hashlib.sha256(profile_bytes).hexdigest())
            profile_path, manifest_path = root / "profile.json", root / "manifest.json"
            profile_path.write_bytes(profile_bytes)
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            (root / "unrelated.txt").write_text("descendant", encoding="utf-8")
            subprocess.run(["git", "add", "unrelated.txt"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "descendant execution snapshot"], cwd=root, check=True)
            result = validator.validate(profile_path, manifest_path, root)
            self.assertEqual(result["profile_json_sha256"], hashlib.sha256(profile_bytes).hexdigest())
            changed = root / validator.PROFILE_SOURCE_PATHS[0]
            changed.write_bytes(b"modified compute path")
            subprocess.run(["git", "add", str(changed.relative_to(root))], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "compute path drift"], cwd=root, check=True)
            with self.assertRaisesRegex(ValueError, "COMPUTE_PATH_CHANGED"):
                validator.validate(profile_path, manifest_path, root)

    def test_consumer_discovers_exact_filename_published_by_producer(self):
        repo_root = Path(__file__).resolve().parents[3]
        consumer = (repo_root / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml").read_text(encoding="utf-8")
        producer = (repo_root / ".github/workflows/c10s-f5-g7-resource-profile.yml").read_text(encoding="utf-8")
        canonical_name = "c10s-f5-g7-resource-profile.json"
        self.assertIn("name '" + canonical_name + "'", consumer)
        self.assertIn(canonical_name, producer)
        self.assertNotIn("c10s-f5-g7-resource-parallel-profile.json", consumer)


    def test_production_download_contract_uses_shared_fail_closed_verifier(self):
        repo_root = Path(__file__).resolve().parents[3]
        workflow = (repo_root / ".github/workflows/c10-s-f5-g7-tiera-calibration.yml").read_text(encoding="utf-8")
        self.assertIn("actions/artifacts/$PROFILE_ARTIFACT_ID/zip", workflow)
        self.assertIn("gh api", workflow)
        self.assertIn("python verify_c10s_f5_g7_resource_profile_artifact.py", workflow)
        self.assertIn("working-directory: 03_EXPERIMENTS/C10-S/harness", workflow)
        self.assertIn("--manifest fixtures/g7_resource_profile_v1_1/manifest.json", workflow)
        self.assertIn("--artifact-metadata", workflow)
        self.assertIn("--extract-profile", workflow)
        self.assertNotIn("unzip -q", workflow)
        self.assertNotIn("ACTUAL_ARCHIVE_SHA", workflow)


if __name__ == "__main__":
    unittest.main()
