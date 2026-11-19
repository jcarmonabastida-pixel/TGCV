from __future__ import annotations

import math
import unittest
from types import SimpleNamespace

import numpy as np
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


def constructed_repeated_score_root_rows():
    """Exact-statistic construction with a double positive F1 score-polynomial root.

    For M=R=4, tau=1 and desired repeated root s=1, solve P(s)=P'(s)=0
    for SSW and the sample variance of world means. The resulting cubic is
    -0.9375*(s-1)^2*(s-4.72), up to floating representation.
    """
    tau = 1.0
    repeated_root = 1.0
    ssw = 4.425
    world_mean_variance = 17.03125
    world_offset = math.sqrt(3.0 * world_mean_variance / 4.0)
    within_pattern = (-1.5, -0.5, 0.5, 1.5)
    within_scale = math.sqrt(ssw / (4.0 * sum(x * x for x in within_pattern)))
    means = (-world_offset, -world_offset, world_offset, world_offset)
    rows = tuple(
        tuple(float(mean + within_scale * deviation) for deviation in within_pattern)
        for mean in means
    )
    return rows, tau, repeated_root


def frozen_six_cell_rows():
    """Fresh deterministic Gaussian fixtures for the six frozen F1 cells."""
    regimes = (
        ("balanced", 1.0, 1.0),
        ("low_between", 1.0, 0.05),
        ("high_between", 0.25, 2.0),
    )
    designs = ((10, 5), (30, 20))
    fixtures = []
    for regime_index, (regime, sigma_w2, sigma_b2) in enumerate(regimes):
        for design_index, (m, r) in enumerate(designs):
            seed = 2026111900 + 100 * regime_index + design_index
            rng = np.random.Generator(np.random.PCG64(seed))
            world = rng.normal(0.0, math.sqrt(sigma_b2), size=(m, 1))
            noise = rng.normal(0.0, math.sqrt(sigma_w2), size=(m, r))
            rows = tuple(
                tuple(float(value) for value in row)
                for row in world + noise
            )
            fixtures.append((regime, m, r, sigma_w2, sigma_b2, seed, rows))
    return tuple(fixtures)


class F1BetweenProfileLikelihoodTests(unittest.TestCase):
    def test_constructed_real_data_fixture_resolves_a_double_score_root(self):
        rows, tau, repeated_root = constructed_repeated_score_root_rows()
        polynomial = f1_score_polynomial_diagnostic(
            rows, between_variance=tau,
        )
        self.assertEqual(polynomial.status, "POLYNOMIAL_ROOTS_ISOLATED")
        self.assertEqual(polynomial.critical_point_solver_status, "RESOLVED")
        self.assertEqual(len(polynomial.tangential_roots), 1)
        self.assertAlmostEqual(
            polynomial.tangential_roots[0], repeated_root, delta=1e-7,
        )
        self.assertEqual(len(polynomial.positive_roots), 2)
        self.assertTrue(any(
            abs(root - repeated_root) <= 1e-7
            for root in polynomial.positive_roots
        ))
        nuisance = f1_profile_nuisance_optimizer_diagnostic(
            rows, between_variance=tau,
        )
        self.assertEqual(nuisance.tangential_score_roots, 1)
        self.assertEqual(nuisance.unresolved_tangential_candidates, 0)
        self.assertIn(
            "TANGENTIAL_STATIONARY_NO_LOCAL_EXTREMUM",
            nuisance.stationary_point_types,
        )

    def test_actual_interval_profile_accepts_resolved_tangency_without_misclassifying_it(self):
        rows, tau, repeated_root = constructed_repeated_score_root_rows()
        from c10s_f1_between_profile_likelihood import brentq as original_brentq

        # Probe only the interval's dimensionless LR callback. Polynomial
        # root-isolation calls to brentq remain completely unmodified.
        from c10s_variance_comparison_interface import observed_nested_mr_result
        observed = observed_nested_mr_result(rows)
        within = observed.within_estimate
        scale = max(within, observed.observed_world_variance)
        def probe_then_solve(function, left, right, *args, **kwargs):
            if getattr(function, "__name__", "") == "lr_excess_scaled":
                function(tau / scale)
            return original_brentq(function, left, right, *args, **kwargs)

        with patch(
            "c10s_f1_between_profile_likelihood.brentq",
            side_effect=probe_then_solve,
        ):
            result = f1_profile_between_confidence_set(
                rows, family="F1",
                likelihood_ratio_cutoff=3.841458820694124,
            )
        self.assertEqual(result.status, "PROFILE_LR_INTERVAL_ROOT_SOLVED")
        self.assertEqual(result.nuisance_certification_status,
                         "POLYNOMIAL_SCORE_BOUNDED_OPTIMIZER_CONCORDANT")
        self.assertEqual(len(result.confidence_components), 1)

    def test_score_polynomial_matches_independent_finite_difference_of_nuisance_loglik(self):
        # Independent oracle: differentiate the explicit Gaussian nuisance
        # log-likelihood numerically in log(s), without calling production
        # score helpers or reusing their coefficient construction.
        fixtures = [
            (ROWS, 0.25),
            (*constructed_repeated_score_root_rows()[:2],),
        ]
        repeated_rows, repeated_tau = constructed_repeated_score_root_rows()[:2]
        fixtures[1] = (repeated_rows, repeated_tau)
        for rows, tau in fixtures:
            m = len(rows)
            r = len(rows[0])
            means = [sum(row) / r for row in rows]
            grand = sum(means) / m
            ssw = sum(
                (value - mean) ** 2
                for row, mean in zip(rows, means) for value in row
            )
            s2_means = sum((mean - grand) ** 2 for mean in means) / (m - 1)
            df_w = m * (r - 1)
            df_b = m - 1

            def independent_loglik(log_s):
                s = math.exp(log_s)
                q = tau + s / r
                return (
                    -0.5 * df_w * (math.log(2.0 * math.pi) + log_s)
                    -0.5 * ssw / s
                    -0.5 * df_b * (math.log(2.0 * math.pi) + math.log(q))
                    -0.5 * df_b * s2_means / q
                )

            polynomial = f1_score_polynomial_diagnostic(
                rows, between_variance=tau,
            )
            for s in (0.17, 0.43, 0.91, 1.37, 3.2, 8.1):
                h = 2e-5
                numeric_score = (
                    independent_loglik(math.log(s) + h)
                    - independent_loglik(math.log(s) - h)
                ) / (2.0 * h)
                q = tau + s / r
                polynomial_score = (
                    sum(coef * s ** index
                        for index, coef in enumerate(polynomial.coefficients_ascending))
                    / (2.0 * s * q * q)
                )
                self.assertAlmostEqual(
                    numeric_score, polynomial_score, delta=2e-7,
                )

    def test_score_polynomial_repeated_root_has_zero_independent_likelihood_derivative(self):
        rows, tau, repeated_root = constructed_repeated_score_root_rows()
        m, r = len(rows), len(rows[0])
        means = [sum(row) / r for row in rows]
        grand = sum(means) / m
        ssw = sum(
            (value - mean) ** 2
            for row, mean in zip(rows, means) for value in row
        )
        s2_means = sum((mean - grand) ** 2 for mean in means) / (m - 1)
        df_w, df_b = m * (r - 1), m - 1

        def independent_loglik(log_s):
            s = math.exp(log_s)
            q = tau + s / r
            return (
                -0.5 * df_w * (math.log(2.0 * math.pi) + log_s)
                -0.5 * ssw / s
                -0.5 * df_b * (math.log(2.0 * math.pi) + math.log(q))
                -0.5 * df_b * s2_means / q
            )

        h = 1e-4
        derivative = (
            independent_loglik(math.log(repeated_root) + h)
            - independent_loglik(math.log(repeated_root) - h)
        ) / (2.0 * h)
        self.assertAlmostEqual(derivative, 0.0, delta=1e-8)

    def test_profile_interval_path_covers_all_six_frozen_f1_cells(self):
        fixtures = frozen_six_cell_rows()
        self.assertEqual(len(fixtures), 6)
        observed = []
        for regime, m, r, sigma_w2, sigma_b2, seed, rows in fixtures:
            with self.subTest(regime=regime, m=m, r=r, seed=seed):
                self.assertEqual(len(rows), m)
                self.assertTrue(all(len(row) == r for row in rows))
                self.assertTrue(all(
                    math.isfinite(value) for row in rows for value in row
                ))
                try:
                    result = f1_profile_between_confidence_set(
                        rows, family="F1",
                        likelihood_ratio_cutoff=3.841458820694124,
                    )
                except F1ProfileError as exc:
                    self.assertTrue(str(exc))
                    observed.append((regime, m, r, "TYPED_ABSTENTION"))
                else:
                    low, high = result.confidence_components[0]
                    self.assertGreaterEqual(low, 0.0)
                    self.assertGreater(high, low)
                    self.assertLessEqual(low, result.mle_between_variance)
                    self.assertGreaterEqual(high, result.mle_between_variance)
                    observed.append((regime, m, r, result.status))
        self.assertEqual(len(observed), 6)

    def test_interval_path_abstains_when_nuisance_scan_has_unresolved_tangency(self):
        from c10s_f1_between_profile_likelihood import (
            f1_profile_nuisance_optimizer_diagnostic as original_diagnostic,
        )
        actual = original_diagnostic(ROWS, between_variance=0.25)
        unresolved = SimpleNamespace(
            status="OPTIMIZATION_INSUFFICIENT",
            bounded_optimizer_loglik=actual.bounded_optimizer_loglik,
            independent_loglik=actual.independent_loglik,
            absolute_loglik_difference=actual.absolute_loglik_difference,
            stationary_points=actual.stationary_points,
            stationary_points_log_scale=actual.stationary_points_log_scale,
            stationary_point_types=actual.stationary_point_types,
            tangential_score_roots=1,
            unresolved_tangential_candidates=1,
            polynomial_degree=actual.polynomial_degree,
            polynomial_root_count=actual.polynomial_root_count,
            polynomial_status=actual.polynomial_status,
            critical_point_solver_status=actual.critical_point_solver_status,
            polynomial_scan_discordant=False,
            independent_boundary_sensitive=False,
            optimizer_error=None,
        )
        with patch(
            "c10s_f1_between_profile_likelihood.f1_profile_nuisance_optimizer_diagnostic",
            return_value=unresolved,
        ):
            with self.assertRaisesRegex(
                F1ProfileError, r"PROFILE_NUISANCE_CERTIFICATION_FAILED:.*unresolved=1",
            ):
                f1_profile_between_confidence_set(
                    ROWS, family="F1",
                    likelihood_ratio_cutoff=3.841458820694124,
                )

    def test_interval_path_abstains_when_polynomial_critical_points_are_unresolved(self):
        from dataclasses import replace
        from c10s_f1_between_profile_likelihood import (
            f1_score_polynomial_diagnostic as original_polynomial_diagnostic,
        )
        actual = original_polynomial_diagnostic(ROWS, between_variance=0.25)
        unresolved = replace(
            actual,
            status="POLYNOMIAL_CRITICAL_POINTS_UNRESOLVED",
            critical_point_solver_status="DISCRIMINANT_UNRESOLVED",
            unresolved_critical_candidates=(1.0,),
        )
        with patch(
            "c10s_f1_between_profile_likelihood.f1_score_polynomial_diagnostic",
            return_value=unresolved,
        ):
            with self.assertRaisesRegex(
                F1ProfileError, "PROFILE_NUISANCE_CERTIFICATION_FAILED",
            ):
                f1_profile_between_confidence_set(
                    ROWS, family="F1",
                    likelihood_ratio_cutoff=3.841458820694124,
                )

    def test_profile_loglik_is_finite_on_physical_parameter_space(self):
        value = f1_profile_loglik(ROWS, between_variance=0.25)
        self.assertTrue(math.isfinite(value))

    def test_root_inversion_returns_ordered_finite_interval(self):
        result = f1_profile_between_confidence_set(
            ROWS,
            family="F1", likelihood_ratio_cutoff=3.841458820694124,
        )
        low, high = result.confidence_components[0]
        self.assertGreaterEqual(low, 0.0)
        self.assertGreater(high, low)
        self.assertTrue(math.isfinite(high))
        self.assertGreaterEqual(result.mle_between_variance, low)
        self.assertLessEqual(result.mle_between_variance, high)
        self.assertEqual(result.status, "PROFILE_LR_INTERVAL_ROOT_SOLVED")
        self.assertEqual(result.nuisance_certification_status, "POLYNOMIAL_SCORE_BOUNDED_OPTIMIZER_CONCORDANT")
        self.assertEqual(result.topology_status, "ANALYTIC_CONNECTEDNESS_ARGUMENT_APPLIED")

    def test_solved_endpoints_satisfy_lr_equation(self):
        cutoff = 3.841458820694124
        result = f1_profile_between_confidence_set(
            ROWS,
            family="F1", likelihood_ratio_cutoff=cutoff,
        )
        maximum = result.max_profile_loglik
        for endpoint in result.confidence_components[0]:
            value = f1_profile_loglik(ROWS, between_variance=endpoint)
            self.assertAlmostEqual(2.0 * (maximum - value), cutoff, places=7)

    def test_nonincluded_zero_boundary_has_positive_lower_endpoint(self):
        result = f1_profile_between_confidence_set(
            ROWS,
            family="F1", likelihood_ratio_cutoff=0.05,
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
            ROWS,
            family="F1", likelihood_ratio_cutoff=2.0,
        )
        self.assertEqual(result.likelihood_ratio_cutoff, 2.0)

    def test_zero_boundary_can_be_included(self):
        result = f1_profile_between_confidence_set(
            ROWS,
            family="F1", likelihood_ratio_cutoff=9.0,
        )
        self.assertTrue(result.lower_boundary_included)
        self.assertEqual(result.confidence_components[0][0], 0.0)

    def test_extreme_lr_cutoff_abstains_when_nuisance_certification_is_unresolved(self):
        with self.assertRaisesRegex(
            F1ProfileError, "PROFILE_NUISANCE_CERTIFICATION_FAILED",
        ):
            f1_profile_between_confidence_set(
                ROWS, family="F1", likelihood_ratio_cutoff=100.0,
            )

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
            ROWS,
            family="F1", likelihood_ratio_cutoff=cutoff,
        )
        base_low, base_high = base.confidence_components[0]
        for factor in (1e-4, 1e-2, 1e2, 1e4):
            scaled = tuple(tuple(factor * value for value in row) for row in ROWS)
            result = f1_profile_between_confidence_set(
            scaled,
                family="F1", likelihood_ratio_cutoff=cutoff,
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
                ROWS, family="F1", likelihood_ratio_cutoff=0.0,
            )

    def test_near_zero_within_sum_fails_closed_before_unbounded_diagnostic_expansion(self):
        means = (-1.0, -1.0, 1.0, 1.0)
        deviations = (-1.5, -0.5, 0.5, 1.5)
        rows = tuple(
            tuple(mean + 1e-150 * value for value in deviations)
            for mean in means
        )
        with self.assertRaisesRegex(
            F1ProfileError, "PROFILE_NUISANCE_DIAGNOSTIC_RANGE_EXCEEDS_LIMIT",
        ):
            f1_profile_between_confidence_set(
                rows, family="F1", likelihood_ratio_cutoff=3.841458820694124,
            )

    def test_upper_endpoint_requires_a_bracket_and_abstains_when_expansion_budget_is_exhausted(self):
        with self.assertRaisesRegex(
            F1ProfileError, "UPPER_PROFILE_ENDPOINT_NOT_BRACKETED",
        ):
            f1_profile_between_confidence_set(
                ROWS, family="F1", likelihood_ratio_cutoff=1e100,
                max_bracket_expansions=1,
            )

    def test_nuisance_search_boundary_contact_is_a_typed_abstention(self):
        actual = f1_profile_nuisance_optimizer_diagnostic(
            ROWS, between_variance=1.0,
        )
        forced = dict(actual.__dict__)
        forced["independent_boundary_sensitive"] = True
        with patch(
            "c10s_f1_between_profile_likelihood.f1_profile_nuisance_optimizer_diagnostic",
            return_value=SimpleNamespace(**forced),
        ):
            with self.assertRaisesRegex(
                F1ProfileError, "PROFILE_NUISANCE_CERTIFICATION_FAILED",
            ):
                f1_profile_between_confidence_set(
                    ROWS, family="F1", likelihood_ratio_cutoff=3.841458820694124,
                )

    def test_zero_within_sum_of_squares_is_explicitly_unresolved(self):
        degenerate = ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0))
        with self.assertRaisesRegex(F1ProfileError, "ZERO_WITHIN_SUM"):
            f1_profile_loglik(degenerate, between_variance=0.2)


if __name__ == "__main__":
    unittest.main()
