from __future__ import annotations

import math
import unittest

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_profile_between_confidence_set,
    f1_profile_loglik,
)


ROWS = (
    (0.0, 1.0, 2.0, 1.0),
    (1.0, 2.0, 3.0, 2.0),
    (2.0, 3.0, 4.0, 3.0),
    (3.0, 4.0, 5.0, 4.0),
)


class F1BetweenProfileLikelihoodTests(unittest.TestCase):
    def test_profile_loglik_is_finite_on_physical_parameter_space(self):
        value = f1_profile_loglik(ROWS, between_variance=0.25)
        self.assertTrue(math.isfinite(value))

    def test_grid_inversion_returns_diagnostic_components(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=3.841458820694124,
            grid_points=101,
        )
        self.assertEqual(result.grid_points, 101)
        self.assertTrue(math.isfinite(result.max_profile_loglik))
        self.assertGreaterEqual(result.mle_tau_grid, 0.0)
        self.assertTrue(result.accepted_components)
        self.assertIn(result.status, {
            "GRID_SET_APPROXIMATION", "GRID_SET_UPPER_TRUNCATED",
        })

    def test_caller_supplied_cutoff_is_preserved(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=2.0, grid_points=51,
        )
        self.assertEqual(result.likelihood_ratio_cutoff, 2.0)

    def test_rejects_negative_tau(self):
        with self.assertRaises(F1ProfileError):
            f1_profile_loglik(ROWS, between_variance=-0.1)

    def test_rejects_invalid_cutoff(self):
        with self.assertRaises(F1ProfileError):
            f1_profile_between_confidence_set(
                ROWS, likelihood_ratio_cutoff=0.0,
            )

    def test_zero_within_sum_of_squares_is_explicitly_unresolved(self):
        degenerate = ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0))
        with self.assertRaisesRegex(F1ProfileError, "ZERO_WITHIN_SUM"):
            f1_profile_loglik(degenerate, between_variance=0.2)


if __name__ == "__main__":
    unittest.main()
