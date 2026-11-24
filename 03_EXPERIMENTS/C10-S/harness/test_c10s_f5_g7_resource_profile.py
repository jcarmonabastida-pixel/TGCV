from __future__ import annotations

import base64
import hashlib
import io
import json
import tempfile
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
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002",
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
            "4c15aba0fffbed1d2ad9fea5e85f60a1cfa52253a96c2e56f47f362b694d52c7",
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
            for relative in validator.PROFILE_SOURCE_PATHS:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b"frozen-compute-path")
            profile_path = root / "profile.json"
            staged_manifest_path = root / "manifest.json"
            profile_path.write_bytes(profile_bytes)
            staged_manifest_path.write_bytes(manifest_bytes)
            with patch.object(
                validator.subprocess, "run", return_value=SimpleNamespace(returncode=0)
            ), patch.object(
                validator.subprocess, "check_output", return_value=b"frozen-compute-path"
            ):
                result = validator.validate(profile_path, staged_manifest_path, root)

        self.assertEqual(result["datasets_per_shard"], 10)
        self.assertEqual(result["shard_tasks_per_phase"], 200)
        self.assertEqual(result["matrix_job_count"], 200)
        self.assertEqual(result["job_topology"], "ONE_MATRIX_JOB_EXECUTES_PRIMARY_AND_CLEAN_SOURCE_REPLAY_SEQUENTIALLY")
        self.assertEqual(result["max_parallel_jobs"], 20)
        self.assertEqual(len(result["shard_matrix"]), 200)
        for cell_id in ("F5_beta22_M10_R5", "F5_beta22_M30_R20"):
            self.assertEqual(
                sum(1 for item in result["shard_matrix"] if item["cell_id"] == cell_id),
                100,
            )
        slow = result["selected_shard_projection"]["per_cell"]["F5_beta22_M30_R20"]
        self.assertAlmostEqual(
            slow["max_observed_primary_replay_job_runtime_seconds"],
            8963.8927517,
            places=5,
        )
        self.assertLessEqual(
            slow["max_observed_primary_replay_job_runtime_seconds"],
            validator.JOB_BUDGET_SECONDS,
        )
        self.assertEqual(slow["shards"], 100)
        self.assertEqual(slow["waves"], 5)
        by_size = {
            item["datasets_per_shard"]: item
            for item in result["candidate_shard_projections"]
        }
        self.assertTrue(by_size[10]["safe_primary_replay_pair_under_150_minute_job_budget"])
        for size in (20, 25, 40, 50, 100):
            self.assertFalse(by_size[size]["safe_primary_replay_pair_under_150_minute_job_budget"])
        expected_primary_replay = (
            5 * 2 * (10 * 7.966771501000004 + 300)
            + 5 * 2 * (10 * 418.194637585 + 300)
        )
        self.assertAlmostEqual(
            result["primary_plus_replay_conservative_wall_seconds"],
            expected_primary_replay,
            places=5,
        )
        self.assertEqual(result["coverage_adjudication"], "NOT_PERFORMED")

    def test_resource_profile_rejects_unexpected_schema_before_compatibility_check(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "profile.json"
            manifest = root / "manifest.json"
            profile_bytes = json.dumps({"schema": "wrong"}).encode()
            profile.write_bytes(profile_bytes)
            manifest.write_text(json.dumps({
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002",
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



if __name__ == "__main__":
    unittest.main()
