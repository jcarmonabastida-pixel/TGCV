from __future__ import annotations

import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_c10s_f5_g7_tiera_calibration as g7
from c10s_nested_mr_fixtures import tier_a_specs
from aggregate_c10s_f5_g7_tiera_shards import aggregate
from c10s_f5_g7_shard_execution import (
    adjudicate_serialized_records,
    records_digest,
    run_cell_shard,
)


class F5G7ShardExecutionTests(unittest.TestCase):
    def setUp(self):
        self.spec = next(
            spec for spec in tier_a_specs()
            if spec.cell_id == "F5_beta22_M10_R5"
        )
        self.fake_certificate = {
            "status": "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
            "winner": {
                "kind": "INTERIOR_STATIONARY_ROOT",
                "parameter_box": ((0.4, 0.4000000001), (0.4, 0.4000000001)),
            },
            "globality_basis": (
                "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS"
            ),
            "census": {"input_provenance": {"source_revision": "d" * 40}},
        }

    def _patches(self):
        return (
            patch.dict(os.environ, {"GITHUB_SHA": "d" * 40}),
            patch(
                "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
                return_value=self.fake_certificate,
            ),
            patch.object(g7, "C0_B", 100),
            patch.object(g7, "C5_B", 100),
        )

    def test_shard_zero_matches_monolithic_cell_records_and_adjudication(self):
        env_patch, cert_patch, c0_patch, c5_patch = self._patches()
        with env_patch, cert_patch, c0_patch, c5_patch:
            monolithic = g7.run_cell(
                self.spec, k=3, c0_b=100, c5_b=100,
                seed_namespace=g7.HOLDOUT_NAMESPACE, adjudicate=True,
            )
            shard = run_cell_shard(
                self.spec, phase="primary", replicate_start=0,
                replicate_count=3, c0_b=100, c5_b=100,
                source_commit="d" * 40,
            )
        expected_records = json.loads(json.dumps(monolithic["records"]))
        for record in expected_records:
            for candidate in record["comparison"]["candidates"]:
                candidate["diagnostics"] = []
        self.assertEqual(shard["records"], expected_records)
        self.assertEqual(shard["records_digest"], records_digest(expected_records))
        self.assertEqual(len(shard["optimizer_diagnostics"]), len(expected_records))
        from c10s_f5_g7_shard_execution import diagnostics_digest
        self.assertEqual(
            shard["optimizer_diagnostics_digest"],
            diagnostics_digest(shard["optimizer_diagnostics"]),
        )
        self.assertEqual(
            adjudicate_serialized_records(shard["records"]),
            monolithic["metrics"],
        )
        self.assertEqual(shard["coverage_adjudication"], "NOT_PERFORMED_SHARD_LEVEL")

    def test_primary_replay_pair_is_exact_on_same_runner(self):
        env_patch, cert_patch, c0_patch, c5_patch = self._patches()
        with env_patch, cert_patch, c0_patch, c5_patch, patch.object(
            g7, "HOLDOUT_NAMESPACE", "c10s_f5_g7_determinism_test_v1",
        ):
            primary = run_cell_shard(
                self.spec, phase="primary", replicate_start=0,
                replicate_count=2, c0_b=100, c5_b=100,
                source_commit="d" * 40,
            )
            replay = run_cell_shard(
                self.spec, phase="replay", replicate_start=0,
                replicate_count=2, c0_b=100, c5_b=100,
                source_commit="d" * 40,
            )
        self.assertEqual(primary["records"], replay["records"])
        self.assertEqual(primary["records_digest"], replay["records_digest"])
        self.assertEqual(
            primary["optimizer_diagnostics_digest"],
            replay["optimizer_diagnostics_digest"],
        )

    def test_nonzero_shard_uses_global_replicate_ids_and_seed_schedule(self):
        env_patch, cert_patch, c0_patch, c5_patch = self._patches()
        with env_patch, cert_patch, c0_patch, c5_patch:
            shard = run_cell_shard(
                self.spec, phase="replay", replicate_start=7,
                replicate_count=2, c0_b=100, c5_b=100,
                source_commit="d" * 40,
            )
        self.assertEqual(
            [row["dataset_id"].rsplit(":", 1)[-1] for row in shard["records"]],
            ["000007", "000008"],
        )
        for row, replicate in zip(shard["records"], (7, 8)):
            self.assertEqual(
                row["dataset_seed"],
                g7.derive_seed(g7.HOLDOUT_NAMESPACE, "dataset", self.spec.cell_id, replicate),
            )
            self.assertEqual(
                row["C0_bootstrap_seed"],
                g7.derive_seed(g7.HOLDOUT_NAMESPACE, "C0_bootstrap", self.spec.cell_id, replicate),
            )
            self.assertEqual(
                row["C5_bootstrap_seed"],
                g7.derive_seed(g7.HOLDOUT_NAMESPACE, "C5_bootstrap", self.spec.cell_id, replicate),
            )

    def test_shard_rejects_out_of_range_and_wrong_bootstrap_contract(self):
        with self.assertRaisesRegex(ValueError, "EXCEEDS_FROZEN_K"):
            run_cell_shard(
                self.spec, phase="primary", replicate_start=999,
                replicate_count=2, c0_b=1000, c5_b=1000,
                source_commit="d" * 40,
            )
        with self.assertRaisesRegex(ValueError, "MUST_MATCH_FROZEN_PROTOCOL"):
            run_cell_shard(
                self.spec, phase="primary", replicate_start=0,
                replicate_count=1, c0_b=100, c5_b=100,
                source_commit="d" * 40,
            )

    def test_full_aggregator_reuses_complete_primary_replay_shards(self):
        source_commit = "d" * 40
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {"GITHUB_SHA": "d" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=self.fake_certificate,
        ), patch.object(g7, "K_PER_CELL", 2):
            root = Path(temporary)
            primary_dir = root / "primary-shards"
            replay_dir = root / "replay-shards"
            primary_dir.mkdir()
            replay_dir.mkdir()
            for phase, directory in (("primary", primary_dir), ("replay", replay_dir)):
                for spec in g7.f5_specs():
                    shard = run_cell_shard(
                        spec, phase=phase, replicate_start=0,
                        replicate_count=2, c0_b=g7.C0_B, c5_b=g7.C5_B,
                        source_commit=source_commit,
                    )
                    filename = f"{spec.cell_id}-000000.json"
                    (directory / filename).write_text(
                        json.dumps(shard, sort_keys=True, indent=2) + "\n",
                        encoding="utf-8",
                    )
            profile = {
                "schema": "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002",
                "scope": "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT",
                "seed_namespace": g7.RESOURCE_NAMESPACE,
                "K_per_cell": 100,
                "C0_B": g7.C0_B,
                "C5_B": g7.C5_B,
                "coverage_adjudication": "NOT_PERFORMED",
                "cells": [
                    {"cell_id": cell_id, "datasets_completed": 100}
                    for cell_id in g7.EXPECTED_CELLS
                ],
            }
            profile_path = root / "resource-profile.json"
            profile_path.write_text(json.dumps(profile), encoding="utf-8")
            profile_manifest_path = root / "resource-profile-manifest.json"
            profile_manifest_path.write_text(json.dumps({
                "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-003",
                "profile_run_id": 44926453920,
                "profile_artifact_id": 123456789,
                "profile_source_commit": source_commit,
                "profile_json_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
                "profile_artifact_archive_sha256": "b" * 64,
            }), encoding="utf-8")
            result = aggregate(
                primary_dir=primary_dir,
                replay_dir=replay_dir,
                preflight_path=profile_path,
                preflight_manifest_path=profile_manifest_path,
                output_dir=root / "result",
                source_commit=source_commit,
                authorization_id="G7-TEST-0001",
            )
            self.assertEqual(result["shards"], 4)
            self.assertEqual(
                result["status"],
                "G7_NOT_VALIDATED_PRIMARY_REPLAY_EXACT_MATCH",
            )
            self.assertTrue((root / "result" / "g7_result.json").is_file())
            self.assertTrue((root / "result" / "run_manifest.json").is_file())


    def test_optimizer_diagnostics_are_separate_from_scientific_record_digest(self):
        from c10s_f5_g7_shard_execution import diagnostics_digest
        records = [{"dataset_id": "d1", "comparison": {"interval": [0.1, 0.2]}}]
        first_diagnostics = [{"dataset_id": "d1", "method_id": "F5", "items": [["optimizer", "CONVERGED"]]}]
        second_diagnostics = [{"dataset_id": "d1", "method_id": "F5", "items": [["optimizer", "ABNORMAL_TERMINATION"]]}]
        self.assertEqual(records_digest(records), records_digest(records))
        self.assertNotEqual(
            diagnostics_digest(first_diagnostics),
            diagnostics_digest(second_diagnostics),
        )



if __name__ == "__main__":
    unittest.main()
