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

    def test_root_inversion_returns_ordered_finite_interval(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=3.841458820694124,
        )
        low, high = result.confidence_components[0]
        self.assertGreaterEqual(low, 0.0)
        self.assertGreater(high, low)
        self.assertTrue(math.isfinite(high))
        self.assertGreaterEqual(result.mle_between_variance, low)
        self.assertLessEqual(result.mle_between_variance, high)
        self.assertEqual(result.status, "PROFILE_LR_INTERVAL_ROOT_SOLVED")

    def test_solved_endpoints_satisfy_lr_equation(self):
        cutoff = 3.841458820694124
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=cutoff,
        )
        maximum = result.max_profile_loglik
        for endpoint in result.confidence_components[0]:
            value = f1_profile_loglik(ROWS, between_variance=endpoint)
            self.assertAlmostEqual(2.0 * (maximum - value), cutoff, places=7)

    def test_nonincluded_zero_boundary_has_positive_lower_endpoint(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=0.05,
        )
        self.assertFalse(result.lower_boundary_included)
        self.assertGreater(result.confidence_components[0][0], 0.0)

    def test_caller_supplied_cutoff_is_preserved(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=2.0,
        )
        self.assertEqual(result.likelihood_ratio_cutoff, 2.0)

    def test_zero_boundary_can_be_included(self):
        result = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=100.0,
        )
        self.assertTrue(result.lower_boundary_included)
        self.assertEqual(result.confidence_components[0][0], 0.0)

    def test_profile_loglik_is_equivariant_to_observation_scale(self):
        tau = 0.25
        base = f1_profile_loglik(ROWS, between_variance=tau)
        df_total = len(ROWS) * (len(ROWS[0]) - 1) + len(ROWS) - 1
        for factor in (1e-6, 1e-3, 1e3, 1e6):
            scaled = tuple(tuple(factor * value for value in row) for row in ROWS)
            scaled_value = f1_profile_loglik(
                scaled, between_variance=tau * factor * factor,
            )
            expected = base - df_total * math.log(factor * factor) / 2.0
            self.assertAlmostEqual(scaled_value, expected, places=7)

    def test_profile_interval_is_equivariant_to_observation_scale(self):
        cutoff = 3.841458820694124
        base = f1_profile_between_confidence_set(
            ROWS, likelihood_ratio_cutoff=cutoff,
        )
        base_low, base_high = base.confidence_components[0]
        for factor in (1e-4, 1e-2, 1e2, 1e4):
            scaled = tuple(tuple(factor * value for value in row) for row in ROWS)
            result = f1_profile_between_confidence_set(
                scaled, likelihood_ratio_cutoff=cutoff,
            )
            low, high = result.confidence_components[0]
            scale2 = factor * factor
            self.assertAlmostEqual(low / scale2, base_low, places=6)
            self.assertAlmostEqual(high / scale2, base_high, places=6)
            self.assertAlmostEqual(
                result.mle_between_variance / scale2,
                base.mle_between_variance, places=7,
            )

    def test_zero_tau_profile_is_finite_across_scales(self):
        for factor in (1e-6, 1.0, 1e6):
            scaled = tuple(tuple(factor * value for value in row) for row in ROWS)
            value = f1_profile_loglik(scaled, between_variance=0.0)
            self.assertTrue(math.isfinite(value))

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
