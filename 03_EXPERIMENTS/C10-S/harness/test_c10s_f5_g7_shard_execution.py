from __future__ import annotations

import os
import unittest
from unittest.mock import patch

import run_c10s_f5_g7_tiera_calibration as g7
from c10s_nested_mr_fixtures import tier_a_specs
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
                "parameter_box": ((0, 1), (0, 1)),
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
        self.assertEqual(shard["records"], monolithic["records"])
        self.assertEqual(shard["records_digest"], records_digest(monolithic["records"]))
        self.assertEqual(
            adjudicate_serialized_records(shard["records"]),
            monolithic["metrics"],
        )
        self.assertEqual(shard["coverage_adjudication"], "NOT_PERFORMED_SHARD_LEVEL")

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

    def test_serialized_adjudicator_rejects_duplicate_dataset_ids(self):
        with self.assertRaisesRegex(ValueError, "MISSING_OR_DUPLICATE"):
            adjudicate_serialized_records([
                {"dataset_id": "same", "comparison": {}, "truth": {}},
                {"dataset_id": "same", "comparison": {}, "truth": {}},
            ])


if __name__ == "__main__":
    unittest.main()
