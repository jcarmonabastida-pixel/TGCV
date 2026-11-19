"""Static contracts for the new bounded F1/F5 resource-only preflight."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import run_c10s_post_holdout_f1_f5_resource_preflight as preflight
import validate_c10s_post_holdout_resource_preflight_authorization as authorization


class PostHoldoutResourcePreflightTests(unittest.TestCase):
    def test_authorization_validator_rejects_draft(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authorization.json"
            path.write_text(json.dumps({
                "schema": authorization.AUTH_SCHEMA,
                "status": "DRAFT",
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                authorization.validate(
                    path, Path(directory), "a" * 40,
                    authorization.BRANCH_PREFIX + "draft-authorization-001",
                )

    def test_execution_requires_explicit_validated_authorization(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, "ONE_USE_AUTHORIZATION"):
                preflight.run_preflight(Path(directory))

    def test_seed_streams_are_reproducible_and_disjoint(self):
        self.assertEqual(
            preflight.derive_seed("dataset", "F1_balanced_M30_R20", 0),
            preflight.derive_seed("dataset", "F1_balanced_M30_R20", 0),
        )
        values = {
            preflight.derive_seed(stream, cell, index)
            for cell in preflight.REPRESENTATIVE_CELLS
            for index in range(10)
            for stream in (
                ("dataset", "C0_bootstrap")
                if cell.startswith("F1_")
                else ("dataset", "C0_bootstrap", "C5_bootstrap_B1000", "C5_bootstrap_B4000")
            )
        }
        self.assertEqual(len(values), 10 * (2 + 4))

    def test_seed_collision_guard_covers_historical_schedules(self):
        result = preflight.validate_seed_separation()
        self.assertEqual(result["status"], "PASS")
        self.assertGreater(result["historical_seed_values_checked"], 0)
        self.assertEqual(result["historical_replicates_per_cell_checked"], 1000)
        self.assertEqual(result["historical_cell_count"], 8)
        self.assertIn("C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0", result["historical_schedules"])

    def test_preflight_is_resource_only_and_keeps_exact_rosters(self):
        original_k = preflight.K_PER_CELL
        preflight.K_PER_CELL = 1

        def fake_compare(rows, **kwargs):
            family = kwargs["family"]
            method = (
                "C1_F1_EXACT_PIVOTAL_1.0" if family == "F1"
                else "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0"
            )
            diagnostics = (("fit_status", "INTERIOR"), ("failure_reason", "NONE"))
            return SimpleNamespace(
                baseline=SimpleNamespace(method_id="C0_FROZEN_V002_NESTED_PERCENTILE_1.2"),
                candidates=(SimpleNamespace(method_id=method, diagnostics=diagnostics),),
            )

        def fake_profile(*args, **kwargs):
            return SimpleNamespace(
                status="BENCHMARK_ONLY", topology_status="ANALYTIC_CONNECTEDNESS_ARGUMENT_APPLIED",
                nuisance_certification_status="CERTIFIED",
            )

        with tempfile.TemporaryDirectory() as directory:
            try:
                with patch.object(preflight, "compare_dataset", side_effect=fake_compare) as compare, \
                     patch.object(preflight, "generate_holdout_dataset", return_value=((0.1, 0.2), (0.3, 0.4))), \
                     patch.object(preflight, "f1_profile_loglik", return_value=-1.0), \
                     patch.object(preflight, "f1_profile_between_confidence_set", side_effect=fake_profile), \
                     patch(\n                         "c10s_fitted_beta_binomial_bootstrap.fitted_beta_binomial_parametric_bootstrap",\n                         return_value=SimpleNamespace(fit=None, failure_reason="MOCKED"),\n                     ):
                    result = preflight.run_preflight(Path(directory), execution_authorized=True)
                self.assertEqual(compare.call_count, 2)
                self.assertEqual(result["total_datasets"], 2)
                self.assertEqual(result["coverage_adjudication"], "NOT_RUN")
                self.assertFalse(result["coverage_metrics_emitted"])
                self.assertFalse(result["calibration_or_validation_data_generated"])
                self.assertFalse(result["scientific_c10_execution"])
                self.assertEqual(
                    {cell["cell_id"] for cell in result["cells"]},
                    set(preflight.REPRESENTATIVE_CELLS),
                )
                persisted = json.loads(
                    (Path(directory) / "post_holdout_resource_preflight.json").read_text()
                )
                serialized = json.dumps(persisted).lower()
                self.assertNotIn("coverage_rate", serialized)
                self.assertNotIn("conditional_coverage", serialized)
                self.assertNotIn("coverage_results", serialized)
                self.assertEqual(len(persisted["records"]), 2)
                self.assertIn("total_projected_hours", persisted["resource_projection"])
                self.assertTrue(all(record["rows_sha256"] for record in persisted["records"]))
            finally:
                preflight.K_PER_CELL = original_k

    def test_f1_benchmark_cutoff_is_explicitly_non_calibrated(self):
        self.assertEqual(
            preflight.F1_PROFILE_BENCHMARK_CUTOFF, 3.841458820694124,
        )
        self.assertNotEqual(
            preflight.PREFLIGHT_ID, "C10S-NESTED-MR-COMPARATIVE-RESOURCE-PREFLIGHT-001",
        )


if __name__ == "__main__":
    unittest.main()
