from __future__ import annotations

import hashlib
import json
import tempfile
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

    def test_shard_plan_minimizes_conservative_wall_time_without_budget_reduction(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in validator.PROFILE_SOURCE_PATHS:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b"frozen-compute-path")
            cells = [
                {
                    "cell_id": "F5_beta22_M10_R5",
                    "datasets_completed": 100,
                    "latency_seconds": {
                        "mean": 0.373, "p95": 0.413,
                        "p99": 0.961, "max": 7.967,
                    },
                },
                {
                    "cell_id": "F5_beta22_M30_R20",
                    "datasets_completed": 100,
                    "latency_seconds": {
                        "mean": 208.420, "p95": 285.521,
                        "p99": 400.000, "max": 418.195,
                    },
                },
            ]
            profile = {
                "schema": validator.PROFILE_SCHEMA,
                "scope": validator.PROFILE_SCOPE,
                "seed_namespace": "c10s_f5_g7_resource_v1_1",
                "K_per_cell": 100,
                "C0_B": 1000,
                "C5_B": 1000,
                "wall_elapsed_seconds": 2469.193131086,
                "process_cpu_seconds": 2636.456402654,
                "peak_rss_kib": 251028,
                "cells": cells,
                "coverage_adjudication": "NOT_PERFORMED",
            }
            profile_path = root / "profile.json"
            profile_path.write_text(json.dumps(profile), encoding="utf-8")
            profile_bytes = profile_path.read_bytes()
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps({
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002",
                "profile_run_id": 45000000001,
                "profile_artifact_id": 14799999999,
                "profile_source_commit": "a" * 40,
                "profile_json_sha256": hashlib.sha256(profile_bytes).hexdigest(),
                "profile_artifact_archive_sha256": "b" * 64,
            }), encoding="utf-8")
            with patch.object(
                validator.subprocess, "run", return_value=SimpleNamespace(returncode=0)
            ), patch.object(
                validator.subprocess, "check_output", return_value=b"frozen-compute-path"
            ):
                result = validator.validate(profile_path, manifest_path, root)
            self.assertEqual(result["datasets_per_shard"], 20)
            self.assertEqual(result["shard_jobs_per_phase"], 100)
            self.assertEqual(result["max_parallel_jobs"], 20)
            self.assertLess(result["end_to_end_conservative_wall_seconds"], 30 * 3600)
            self.assertLessEqual(
                result["selected_shard_projection"]["per_cell"]["F5_beta22_M30_R20"]["max_observed_shard_runtime_seconds"],
                9000,
            )
            self.assertEqual(result["selected_shard_projection"]["per_cell"]["F5_beta22_M30_R20"]["shards"], 50)
            self.assertFalse(next(item for item in result["candidate_shard_projections"] if item["datasets_per_shard"] == 25)["safe_under_150_minute_job_budget"])

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
