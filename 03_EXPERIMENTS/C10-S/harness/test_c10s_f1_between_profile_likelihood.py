from __future__ import annotations

import math
import unittest

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_profile_between_confidence_set,
    f1_profile_loglik,
    f1_profile_nuisance_optimizer_diagnostic,
    f1_profile_nuisance_stability_diagnostic,
    _scan_score_stationary_points,
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

    def test_independent_nuisance_score_scan_agrees_with_bounded_optimizer(self):
        result = f1_profile_nuisance_optimizer_diagnostic(
            ROWS, between_variance=0.25,
        )
        self.assertEqual(result.status, "OPTIMIZATION_CONCORDANT")
        self.assertGreaterEqual(result.stationary_points, 1)
        self.assertIsNotNone(result.absolute_loglik_difference)
        self.assertLessEqual(result.absolute_loglik_difference, 1e-7)

    def test_score_scan_detects_tangential_root_without_sign_change(self):
        roots, kinds, tangencies, unresolved = _scan_score_stationary_points(
            lambda x: (x - 0.125) ** 2,
            lambda x: 2.0 * (x - 0.125),
            lo=-1.0, hi=1.0, grid_points=81,
        )
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 0.125, places=9)
        self.assertEqual(kinds, ("TANGENTIAL_STATIONARY_NO_LOCAL_EXTREMUM",))
        self.assertEqual(tangencies, 1)
        self.assertEqual(unresolved, 0)

    def test_score_scan_classifies_local_maximum_and_minimum(self):
        roots, kinds, tangencies, unresolved = _scan_score_stationary_points(
            lambda x: (x + 0.4) * (0.3 - x),
            lambda x: -2.0 * x - 0.1,
            lo=-1.0, hi=1.0, grid_points=101,
        )
        self.assertEqual(len(roots), 2)
        self.assertEqual(kinds, ("LOCAL_MINIMUM", "LOCAL_MAXIMUM"))
        self.assertEqual(tangencies, 0)
        self.assertEqual(unresolved, 0)

    def test_multi_resolution_stability_records_full_grid_span_cross_product(self):
        result = f1_profile_nuisance_stability_diagnostic(
            ROWS, between_variance=0.25,
            grid_resolutions=(241, 481, 961),
            log_spans=(30.0, 36.0, 42.0),
        )
        self.assertEqual(len(result.configurations), 9)
        self.assertEqual(len(result.stationary_point_counts), 9)
        self.assertEqual(len(result.optimizer_statuses), 9)
        self.assertEqual(len(result.stationary_point_type_signatures), 9)
        self.assertEqual(len(result.tangential_score_root_counts), 9)
        self.assertEqual(len(result.unresolved_tangential_candidate_counts), 9)
        self.assertIsNotNone(result.maximum_stationary_location_spread)
        self.assertIn(
            result.status,
            {
                "OPTIMIZATION_CONCORDANT", "OPTIMIZATION_DISCORDANT",
                "OPTIMIZATION_INSUFFICIENT", "OPTIMIZATION_BOUNDARY_SENSITIVE",
            },
        )

    def test_multi_resolution_stability_rejects_invalid_resolution(self):
        with self.assertRaisesRegex(F1ProfileError, "GRID_RESOLUTIONS"):
            f1_profile_nuisance_stability_diagnostic(
                ROWS, between_variance=0.25, grid_resolutions=(40, 241),
            )

    def test_multi_resolution_stability_rejects_invalid_log_span(self):
        with self.assertRaisesRegex(F1ProfileError, "LOG_SPANS"):
            f1_profile_nuisance_stability_diagnostic(
                ROWS, between_variance=0.25, log_spans=(30.0, 0.0),
            )

    def test_nuisance_diagnostic_rejects_underresolved_grid(self):
        with self.assertRaisesRegex(F1ProfileError, "NUISANCE_GRID_POINTS"):
            f1_profile_nuisance_optimizer_diagnostic(
                ROWS, between_variance=0.25, grid_points=40,
            )

    def test_nuisance_diagnostic_rejects_invalid_log_span(self):
        with self.assertRaisesRegex(F1ProfileError, "NUISANCE_LOG_SPAN"):
            f1_profile_nuisance_optimizer_diagnostic(
                ROWS, between_variance=0.25, log_span=0.0,
            )

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
