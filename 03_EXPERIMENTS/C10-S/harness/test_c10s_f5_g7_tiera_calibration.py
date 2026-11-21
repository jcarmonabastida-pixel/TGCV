from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_f5_g7_tiera_calibration import (
    EXPECTED_CELLS,
    HOLDOUT_NAMESPACE,
    RESOURCE_NAMESPACE,
    adjudicate_g7_metrics,
    derive_seed,
    run_cell,
    run_resource_preflight,
    validate_seed_separation,
)


class F5G7CalibrationTests(unittest.TestCase):
    def test_frozen_scope_and_new_seed_namespaces(self):
        self.assertEqual(EXPECTED_CELLS, ("F5_beta22_M10_R5", "F5_beta22_M30_R20"))
        self.assertNotEqual(HOLDOUT_NAMESPACE, RESOURCE_NAMESPACE)
        self.assertNotEqual(
            derive_seed(HOLDOUT_NAMESPACE, "dataset", EXPECTED_CELLS[0], 0),
            derive_seed(RESOURCE_NAMESPACE, "dataset", EXPECTED_CELLS[0], 0),
        )
        validate_seed_separation(k=20)

    def test_f5_cell_uses_global_certificate_and_adjudicates_only_when_requested(self):
        spec = next(s for s in tier_a_specs() if s.cell_id == EXPECTED_CELLS[0])
        fake = {
            "status": "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
            "winner": {
                "kind": "INTERIOR_STATIONARY_ROOT",
                "parameter_box": ((0, 1), (0, 1)),
            },
            "globality_basis": "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS",
            "census": {"input_provenance": {"source_revision": "d" * 40}},
        }
        with patch.dict(os.environ, {"GITHUB_SHA": "d" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=fake,
        ):
            result = run_cell(
                spec, k=3, c0_b=100, c5_b=100,
                seed_namespace=HOLDOUT_NAMESPACE, adjudicate=True,
            )
        self.assertEqual(result["datasets_completed"], 3)
        self.assertEqual(len(result["metrics"]), 4)
        self.assertTrue(all(
            dict(record["comparison"]["candidates"][0]["comparison"]["provenance"])[
                "global_mle_certificate_status"
            ] == "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED"
            for record in result["records"]
        ))

    def test_resource_only_path_does_not_adjudicate(self):
        spec = next(s for s in tier_a_specs() if s.cell_id == EXPECTED_CELLS[0])
        fake = {
            "status": "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
            "winner": {
                "kind": "INTERIOR_STATIONARY_ROOT",
                "parameter_box": ((0, 1), (0, 1)),
            },
            "globality_basis": "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS",
            "census": {"input_provenance": {"source_revision": "e" * 40}},
        }
        with patch.dict(os.environ, {"GITHUB_SHA": "e" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=fake,
        ), patch("run_c10s_f5_g7_tiera_calibration.adjudicate_matched_datasets", side_effect=AssertionError):
            result = run_cell(
                spec, k=2, c0_b=100, c5_b=100,
                seed_namespace=RESOURCE_NAMESPACE, adjudicate=False,
            )
        self.assertEqual(result["metrics"], [])
        self.assertEqual(result["coverage_adjudication"], "NOT_PERFORMED_RESOURCE_ONLY")


    def test_resource_preflight_failure_returns_timing_evidence_before_stop(self):
        with patch("run_c10s_f5_g7_tiera_calibration.validate_seed_separation"), patch(
            "run_c10s_f5_g7_tiera_calibration.run_cell",
            return_value={"records": [], "datasets_completed": 100},
        ), patch(
            "run_c10s_f5_g7_tiera_calibration.time.perf_counter",
            side_effect=[0.0, 900.0],
        ):
            result = run_resource_preflight()
        self.assertEqual(result["status"], "RESOURCE_PREFLIGHT_FAIL")
        self.assertEqual(
            result["failure_reason"],
            "G7_RESOURCE_PREFLIGHT_PROJECTS_OVER_4_5_HOURS",
        )
        self.assertEqual(result["elapsed_seconds"], 900.0)
        self.assertEqual(result["projected_primary_plus_replay_seconds"], 18000.0)
        self.assertEqual(result["coverage_adjudication"], "NOT_PERFORMED")

    def test_g7_acceptance_is_no_pooling_and_requires_all_four_c5_components(self):
        summary = {}
        for cell_id in EXPECTED_CELLS:
            summary[cell_id] = {
                "datasets_completed": 1000,
                "metrics": [
                    {
                        "method_id": "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0",
                        "target": target,
                        "n_datasets": 1000,
                        "conditional_coverage": 0.95,
                        "coverage_wilson_95": [0.94, 0.96],
                        "interval_emission_rate": 0.99,
                        "abstention_count": 10,
                    }
                    for target in ("within", "between")
                ],
            }
        self.assertEqual(adjudicate_g7_metrics(summary)["status"], "PASS")
        summary[EXPECTED_CELLS[1]]["metrics"][1]["conditional_coverage"] = 0.90
        decision = adjudicate_g7_metrics(summary)
        self.assertEqual(decision["status"], "NOT_VALIDATED")
        self.assertFalse(decision["components"][-1]["pass"])


if __name__ == "__main__":
    unittest.main()
