from __future__ import annotations

import math
import unittest

from c10s_f5_beta_binomial_mcse_profile import (
    F5ProfileError,
    f5_beta_binomial_mcse_profile_loglik,
    f5_beta_binomial_mcse_profile_confidence_set,
    _bisect_profile_crossing,
)


ROWS = (
    (1, 0, 1, 0),
    (1, 1, 0, 0),
    (1, 1, 1, 0),
    (0, 0, 0, 1),
    (1, 0, 0, 0),
    (1, 1, 0, 1),
)


class F5BetaBinomialProfileTests(unittest.TestCase):
    def test_interior_target_returns_finite_profile(self):
        result = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5, target_mcse=0.05,
        )
        self.assertTrue(math.isfinite(result.profile_loglik))
        self.assertIn(result.maximizing_branch, {"MU_PLUS", "MU_MINUS"})
        self.assertIn(
            result.boundary_status,
            {"FINITE_CONCENTRATION_OPTIMUM", "CONCENTRATION_BOUNDARY_LIMIT"},
        )

    def test_both_mean_branches_are_retained(self):
        result = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5, target_mcse=0.05,
        )
        self.assertNotEqual(result.branch_loglik_plus, -math.inf)
        self.assertNotEqual(result.branch_loglik_minus, -math.inf)

    def test_world_permutation_invariance(self):
        permuted = tuple(reversed(ROWS))
        a = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5, target_mcse=0.05,
        )
        b = f5_beta_binomial_mcse_profile_loglik(
            permuted, target_m=10, target_r=5, target_mcse=0.05,
        )
        self.assertAlmostEqual(a.profile_loglik, b.profile_loglik, places=9)

    def test_maximum_target_uses_kappa_zero_boundary(self):
        result = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5,
            target_mcse=1.0 / (2.0 * math.sqrt(10.0)),
        )
        self.assertEqual(result.boundary_status, "KAPPA_TO_ZERO_LIMIT")
        self.assertIsNone(result.maximizing_concentration)

    def test_target_above_parameter_space_is_rejected_as_infeasible(self):
        result = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5, target_mcse=0.2,
        )
        self.assertEqual(result.boundary_status, "TARGET_OUTSIDE_PARAMETER_SPACE")
        self.assertEqual(result.profile_loglik, -math.inf)

    def test_all_zero_data_and_zero_target_have_boundary_likelihood(self):
        all_zero = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
        result = f5_beta_binomial_mcse_profile_loglik(
            all_zero, target_m=10, target_r=5, target_mcse=0.0,
        )
        self.assertEqual(result.profile_loglik, 0.0)
        self.assertEqual(result.boundary_status, "CONCENTRATION_BOUNDARY_LIMIT")

    def test_profile_lr_inversion_retains_components_and_hull(self):
        result = f5_beta_binomial_mcse_profile_confidence_set(
            ROWS, target_m=10, target_r=5,
            likelihood_ratio_cutoff=3.841458820694124,
            scan_grid_points=21,
        )
        self.assertIsNotNone(result.confidence_hull)
        self.assertGreaterEqual(len(result.confidence_components), 1)
        for lower, upper in result.confidence_components:
            self.assertGreaterEqual(lower, 0.0)
            self.assertGreater(upper, lower)
            self.assertLessEqual(upper, 1.0 / (2.0 * math.sqrt(10.0)))
        self.assertEqual(
            result.confidence_hull,
            (result.confidence_components[0][0], result.confidence_components[-1][1]),
        )

    def test_profile_lr_inversion_rejects_unselected_or_invalid_cutoff(self):
        with self.assertRaises(F5ProfileError):
            f5_beta_binomial_mcse_profile_confidence_set(
                ROWS, target_m=10, target_r=5,
                likelihood_ratio_cutoff=0.0,
            )

    def test_profile_reports_both_numerical_grid_resolutions(self):
        result = f5_beta_binomial_mcse_profile_confidence_set(
            ROWS, target_m=10, target_r=5,
            likelihood_ratio_cutoff=3.841458820694124,
            scan_grid_points=21, concentration_grid_points=81,
        )
        self.assertEqual(result.scan_grid_points, 21)
        self.assertEqual(result.concentration_grid_points, 81)

    def test_profile_rejects_underresolved_concentration_grid(self):
        with self.assertRaises(F5ProfileError):
            f5_beta_binomial_mcse_profile_loglik(
                ROWS, target_m=10, target_r=5, target_mcse=0.05,
                concentration_grid_points=40,
            )

    def test_endpoint_refinement_handles_nonfinite_outside_support(self):
        root = _bisect_profile_crossing(
            lambda x: -math.inf if x < 0.25 else x - 0.25,
            0.0, 1.0,
        )
        self.assertAlmostEqual(root, 0.25, places=10)

    def test_rejects_non_bernoulli_rows(self):
        with self.assertRaises(F5ProfileError):
            f5_beta_binomial_mcse_profile_loglik(
                ((0, 1, 2), (1, 0, 1)),
                target_m=10, target_r=5, target_mcse=0.05,
            )


if __name__ == "__main__":
    unittest.main()
