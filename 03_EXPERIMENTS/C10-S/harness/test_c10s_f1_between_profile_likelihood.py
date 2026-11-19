from __future__ import annotations

import math
import unittest
from unittest.mock import patch

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_profile_between_confidence_set,
    f1_profile_loglik,
    f1_profile_nuisance_optimizer_diagnostic,
    f1_profile_nuisance_stability_diagnostic,
    _scan_score_stationary_points,
    f1_score_polynomial_diagnostic,
    _positive_quadratic_roots_diagnostic,
    _normalize_scaled_polynomial,
    _restore_polynomial_scale,
    _score_polynomial_coefficients_exact,
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
            family="F1",
            ROWS, likelihood_ratio_cutoff=3.841458820694124,
        )
        low, high = result.confidence_components[0]
        self.assertGreaterEqual(low, 0.0)
        self.assertGreater(high, low)
        self.assertTrue(math.isfinite(high))
        self.assertGreaterEqual(result.mle_between_variance, low)
        self.assertLessEqual(result.mle_between_variance, high)
        self.assertEqual(result.status, "PROFILE_LR_INTERVAL_ROOT_SOLVED")
        self.assertEqual(result.nuisance_certification_status, "OPTIMIZATION_CONCORDANT")
        self.assertEqual(result.topology_status, "ANALYTIC_CONNECTEDNESS_ARGUMENT_APPLIED")

    def test_solved_endpoints_satisfy_lr_equation(self):
        cutoff = 3.841458820694124
        result = f1_profile_between_confidence_set(
            family="F1",
            ROWS, likelihood_ratio_cutoff=cutoff,
        )
        maximum = result.max_profile_loglik
        for endpoint in result.confidence_components[0]:
            value = f1_profile_loglik(ROWS, between_variance=endpoint)
            self.assertAlmostEqual(2.0 * (maximum - value), cutoff, places=7)

    def test_nonincluded_zero_boundary_has_positive_lower_endpoint(self):
        result = f1_profile_between_confidence_set(
            family="F1",
            ROWS, likelihood_ratio_cutoff=0.05,
        )
        self.assertFalse(result.lower_boundary_included)
        self.assertGreater(result.confidence_components[0][0], 0.0)

    def test_profile_interval_rejects_non_f1_family(self):
        with self.assertRaisesRegex(
            F1ProfileError, "REQUIRES_EXPLICIT_F1_FAMILY",
        ):
            f1_profile_between_confidence_set(
                ROWS, family="F5", likelihood_ratio_cutoff=2.0,
            )

    def test_caller_supplied_cutoff_is_preserved(self):
        result = f1_profile_between_confidence_set(
            family="F1",
            ROWS, likelihood_ratio_cutoff=2.0,
        )
        self.assertEqual(result.likelihood_ratio_cutoff, 2.0)

    def test_zero_boundary_can_be_included(self):
        result = f1_profile_between_confidence_set(
            family="F1",
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
            family="F1",
            ROWS, likelihood_ratio_cutoff=cutoff,
        )
        base_low, base_high = base.confidence_components[0]
        for factor in (1e-4, 1e-2, 1e2, 1e4):
            scaled = tuple(tuple(factor * value for value in row) for row in ROWS)
            result = f1_profile_between_confidence_set(
            family="F1",
                scaled, likelihood_ratio_cutoff=cutoff,
            )
            low, high = result.confidence_components[0]
            scale2 = factor * factor
            # Compare in the invariant variance coordinate. The solver
            # now uses xtol in tau/reference_scale, so this bound is independent
            # of the observation units and remains tighter than the former
            # places=6 assertion that exposed the absolute-tolerance defect.
            self.assertAlmostEqual(
                low / scale2, base_low, delta=1e-8,
            )
            self.assertAlmostEqual(
                high / scale2, base_high, delta=1e-8,
            )
            self.assertAlmostEqual(
                result.mle_between_variance / scale2,
                base.mle_between_variance, delta=1e-10,
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

    def test_tau_zero_records_removed_extraneous_factor_and_returns_reduced_polynomial(self):
        diagnostic = f1_score_polynomial_diagnostic(
            ROWS, between_variance=0.0,
        )
        self.assertEqual(diagnostic.removed_zero_factor_multiplicity, 2)
        self.assertNotEqual(diagnostic.coefficients_ascending[0], 0.0)
        self.assertTrue(all(root > 0.0 for root in diagnostic.positive_roots))

    def test_score_polynomial_diagnostic_is_cubic_and_matches_score_scan(self):
        polynomial = f1_score_polynomial_diagnostic(
            ROWS, between_variance=0.25,
        )
        scan = f1_profile_nuisance_optimizer_diagnostic(
            ROWS, between_variance=0.25,
        )
        self.assertLessEqual(polynomial.degree, 3)
        self.assertGreaterEqual(polynomial.degree, 1)
        self.assertEqual(polynomial.status, "POLYNOMIAL_ROOTS_ISOLATED")
        self.assertEqual(len(polynomial.positive_roots), scan.stationary_points)
        self.assertFalse(scan.polynomial_scan_discordant)
        self.assertEqual(scan.polynomial_root_count, len(polynomial.positive_roots))
        for root, log_root in zip(
            polynomial.positive_roots, scan.stationary_points_log_scale,
        ):
            self.assertAlmostEqual(math.log(root), log_root, places=6)

    def test_exact_score_coefficient_construction_detects_underflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "COEFFICIENT_0_UNDERFLOW",
        ):
            _score_polynomial_coefficients_exact(
                r=2, df_w=2, df_b=2, ssw=1.0,
                s2_means=1.0, tau=1e-200,
            )

    def test_exact_score_coefficient_construction_detects_overflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "COEFFICIENT_0_OVERFLOW",
        ):
            _score_polynomial_coefficients_exact(
                r=2, df_w=2, df_b=2, ssw=1e308,
                s2_means=1.0, tau=1e308,
            )

    def test_exact_score_coefficients_match_exact_binary_input_formula(self):
        from fractions import Fraction
        tau = 1.0 + 2.0 ** -27
        observed = _score_polynomial_coefficients_exact(
            r=2, df_w=2, df_b=2, ssw=1.0,
            s2_means=1.0, tau=tau,
        )
        exact_c1 = -Fraction(2) * Fraction(tau) ** 2 + Fraction(tau)
        self.assertEqual(observed[1], float(exact_c1))

    def test_polynomial_scale_rejects_power_overflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "SCALE_POWER_UNREPRESENTABLE",
        ):
            _normalize_scaled_polynomial((1.0, 1.0, 1.0), 1e200)

    def test_polynomial_scale_rejects_power_underflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "SCALE_POWER_UNREPRESENTABLE",
        ):
            _normalize_scaled_polynomial((1.0, 1.0, 1.0), 1e-200)

    def test_polynomial_normalization_rejects_erased_small_coefficient(self):
        with self.assertRaisesRegex(
            F1ProfileError, "NORMALIZATION_ERASED_COEFFICIENT",
        ):
            _normalize_scaled_polynomial((1e308, 1e-308), 1.0)

    def test_polynomial_root_restore_rejects_underflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "ROOT_SCALE_UNREPRESENTABLE",
        ):
            _restore_polynomial_scale(
                (1e-300,), 1e-100, label="ROOT_SCALE",
            )

    def test_polynomial_root_restore_rejects_overflow(self):
        with self.assertRaisesRegex(
            F1ProfileError, "ROOT_SCALE_UNREPRESENTABLE",
        ):
            _restore_polynomial_scale(
                (1e100,), 1e300, label="ROOT_SCALE",
            )

    def test_score_polynomial_rejects_nonfinite_raw_coefficients(self):
        with patch(
            "c10s_f1_between_profile_likelihood._sufficient_statistics",
            return_value=(2, 4, 2, 1e308, 1.0, 1e308),
        ):
            with self.assertRaisesRegex(
                F1ProfileError, "COEFFICIENT_0_OVERFLOW",
            ):
                f1_score_polynomial_diagnostic(
                    ROWS, between_variance=1e308,
                )

    def test_quadratic_critical_solver_finds_two_distinct_positive_roots(self):
        roots, status = _positive_quadratic_roots_diagnostic(1.0, -3.0, 2.0)
        self.assertEqual(status, "RESOLVED")
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 2.0)

    def test_quadratic_critical_solver_resolves_exact_double_root(self):
        roots, status = _positive_quadratic_roots_diagnostic(1.0, -2.0, 1.0)
        self.assertEqual(status, "RESOLVED")
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1.0)

    def test_quadratic_critical_solver_abstains_on_discriminant_overflow(self):
        roots, status = _positive_quadratic_roots_diagnostic(
            1e308, 1e308, 1e308,
        )
        self.assertEqual(roots, ())
        self.assertEqual(status, "DISCRIMINANT_UNRESOLVED")

    def test_linear_critical_solver_abstains_on_nonfinite_root(self):
        roots, status = _positive_quadratic_roots_diagnostic(
            0.0, 1e-308, -1e308,
        )
        self.assertEqual(roots, ())
        self.assertEqual(status, "DISCRIMINANT_UNRESOLVED")

    def test_quadratic_critical_solver_abstains_on_nonfinite_coefficients(self):
        roots, status = _positive_quadratic_roots_diagnostic(
            float("inf"), -2.0, 1.0,
        )
        self.assertEqual(roots, ())
        self.assertEqual(status, "DISCRIMINANT_UNRESOLVED")

    def test_quadratic_critical_solver_abstains_near_discriminant_zero(self):
        roots, status = _positive_quadratic_roots_diagnostic(
            1.0, -2.0, 1.0 - 1e-15,
        )
        self.assertEqual(roots, ())
        self.assertEqual(status, "DISCRIMINANT_UNRESOLVED")

    def test_score_polynomial_diagnostic_handles_zero_between_boundary(self):
        result = f1_score_polynomial_diagnostic(
            ROWS, between_variance=0.0,
        )
        self.assertLessEqual(result.degree, 3)
        self.assertEqual(result.status, "POLYNOMIAL_ROOTS_ISOLATED")
        self.assertTrue(all(root > 0.0 for root in result.positive_roots))

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

    def test_score_scan_flags_near_tangency_without_confirming_a_root(self):
        roots, kinds, tangencies, unresolved = _scan_score_stationary_points(
            lambda x: (x - 0.125) ** 2 + 1e-9,
            lambda x: 2.0 * (x - 0.125),
            lo=-1.0, hi=1.0, grid_points=81,
        )
        self.assertEqual(roots, ())
        self.assertEqual(kinds, ())
        self.assertEqual(tangencies, 0)
        self.assertEqual(unresolved, 1)

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
        self.assertEqual(len(result.polynomial_degrees), 9)
        self.assertEqual(len(result.polynomial_root_counts), 9)
        self.assertEqual(len(result.polynomial_statuses), 9)
        self.assertEqual(len(result.critical_point_solver_statuses), 9)
        self.assertEqual(len(result.polynomial_scan_discordances), 9)
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
            family="F1",
                ROWS, likelihood_ratio_cutoff=0.0,
            )

    def test_zero_within_sum_of_squares_is_explicitly_unresolved(self):
        degenerate = ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0))
        with self.assertRaisesRegex(F1ProfileError, "ZERO_WITHIN_SUM"):
            f1_profile_loglik(degenerate, between_variance=0.2)


if __name__ == "__main__":
    unittest.main()
