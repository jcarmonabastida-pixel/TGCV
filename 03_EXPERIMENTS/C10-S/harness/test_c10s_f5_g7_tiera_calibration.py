from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_f5_g7_tiera_calibration import (
    EXPECTED_CELLS,
    HOLDOUT_NAMESPACE,
    RESOURCE_NAMESPACE,
    derive_seed,
    run_cell,
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


if __name__ == "__main__":
    unittest.main()
