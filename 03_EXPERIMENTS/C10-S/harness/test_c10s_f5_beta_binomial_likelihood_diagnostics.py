from __future__ import annotations

import json
import math
import unittest
from dataclasses import asdict
from types import SimpleNamespace
from unittest.mock import patch

from c10s_beta_binomial_variance_oracles import beta_binomial_f5_reference
from c10s_f5_beta_binomial_likelihood_diagnostics import (
    F5LikelihoodDiagnosticError,
    beta_binomial_extended_boundary_likelihoods,
    beta_binomial_loglik_score_hessian,
    audit_beta_binomial_count_fit,
    beta_binomial_profile_log_concentration,
    beta_binomial_profiled_boundary_likelihoods,
    build_beta_binomial_profile_audit_record,
    beta_binomial_profile_numerical_stability,
)


COUNTS = (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
R = 5


class F5BetaBinomialLikelihoodDiagnosticTests(unittest.TestCase):
    def test_analytic_score_matches_central_finite_differences(self):
        eta, xi, h = 0.17, math.log(3.4), 2e-5

        def ll(a, b):
            return beta_binomial_loglik_score_hessian(
                COUNTS, R, mean_logit=a, log_concentration=b,
            ).log_likelihood

        result = beta_binomial_loglik_score_hessian(
            COUNTS, R, mean_logit=eta, log_concentration=xi,
        )
        score_eta = (ll(eta + h, xi) - ll(eta - h, xi)) / (2 * h)
        score_xi = (ll(eta, xi + h) - ll(eta, xi - h)) / (2 * h)
        self.assertAlmostEqual(result.score_mean_logit, score_eta, delta=2e-6)
        self.assertAlmostEqual(result.score_log_concentration, score_xi, delta=2e-6)

    def test_analytic_hessian_matches_finite_difference_of_score(self):
        eta, xi, h = -0.23, math.log(1.7), 1e-4

        def score(a, b):
            value = beta_binomial_loglik_score_hessian(
                COUNTS, R, mean_logit=a, log_concentration=b,
            )
            return value.score_mean_logit, value.score_log_concentration

        result = beta_binomial_loglik_score_hessian(
            COUNTS, R, mean_logit=eta, log_concentration=xi,
        )
        plus_eta, minus_eta = score(eta + h, xi), score(eta - h, xi)
        plus_xi, minus_xi = score(eta, xi + h), score(eta, xi - h)
        h_ee = (plus_eta[0] - minus_eta[0]) / (2 * h)
        h_xe = (plus_eta[1] - minus_eta[1]) / (2 * h)
        h_ex = (plus_xi[0] - minus_xi[0]) / (2 * h)
        h_xx = (plus_xi[1] - minus_xi[1]) / (2 * h)
        self.assertAlmostEqual(result.hessian_mean_logit, h_ee, delta=2e-5)
        self.assertAlmostEqual(result.hessian_cross, h_ex, delta=2e-5)
        self.assertAlmostEqual(result.hessian_cross, h_xe, delta=2e-5)
        self.assertAlmostEqual(result.hessian_log_concentration, h_xx, delta=2e-5)

    def test_hessian_is_symmetric_by_construction_and_finite(self):
        result = beta_binomial_loglik_score_hessian(
            COUNTS, R, mean_logit=0.4, log_concentration=math.log(0.8),
        )
        self.assertTrue(all(math.isfinite(v) for v in (
            result.log_likelihood, result.score_mean_logit,
            result.score_log_concentration, result.hessian_mean_logit,
            result.hessian_cross, result.hessian_log_concentration,
        )))

    def test_invalid_counts_and_parameters_fail_closed(self):
        with self.assertRaisesRegex(F5LikelihoodDiagnosticError, "COUNTS_MUST"):
            beta_binomial_loglik_score_hessian(
                (0, 1.5, 2), 5, mean_logit=0.0, log_concentration=0.0,
            )
        with self.assertRaisesRegex(F5LikelihoodDiagnosticError, "PARAMETERS"):
            beta_binomial_loglik_score_hessian(
                COUNTS, R, mean_logit=float("nan"), log_concentration=0.0,
            )

    def test_two_point_limit_is_zero_for_any_interior_count(self):
        result = beta_binomial_extended_boundary_likelihoods(
            (0, 5, 2), 5, mean_probability=0.4, concentration=2.0,
        )
        self.assertEqual(result.two_point_mixing_limit_log_likelihood, -math.inf)
        self.assertTrue(math.isfinite(result.binomial_limit_log_likelihood))
        self.assertTrue(math.isfinite(result.finite_log_likelihood))

    def test_all_endpoint_counts_have_finite_two_point_limit(self):
        result = beta_binomial_extended_boundary_likelihoods(
            (0, 5, 0, 5), 5, mean_probability=0.4, concentration=0.7,
        )
        expected = 2 * math.log(0.6) + 2 * math.log(0.4)
        self.assertAlmostEqual(result.two_point_mixing_limit_log_likelihood, expected)

    def test_optimizer_audit_retains_all_starts_and_independent_fit(self):
        audit = audit_beta_binomial_count_fit(
            (0, 0, 1, 4, 5, 5, 2, 3, 0, 5), 5,
        )
        self.assertEqual(len(audit.starts), 3)
        self.assertTrue(all(item.message for item in audit.starts))
        self.assertIsNotNone(audit.selected_log_likelihood)
        self.assertIsNotNone(audit.selected_score_norm)
        self.assertEqual(len(audit.hessian_eigenvalues), 2)
        self.assertEqual(len(audit.selected_score_components), 2)
        self.assertEqual(len(audit.observed_hessian), 2)
        self.assertEqual(len(audit.observed_hessian[0]), 2)
        self.assertEqual(len(audit.hessian_eigenvectors), 2)
        self.assertEqual(len(audit.hessian_eigenvectors[0]), 2)
        self.assertTrue(all(
            math.isfinite(value)
            for row in audit.observed_hessian for value in row
        ))
        self.assertTrue(all(
            math.isfinite(value)
            for row in audit.hessian_eigenvectors for value in row
        ))
        self.assertIsNotNone(audit.profile_minus_binomial_limit)
        self.assertAlmostEqual(
            audit.profile_minus_binomial_limit,
            audit.selected_log_likelihood - audit.binomial_limit_log_likelihood,
            delta=1e-12,
        )
        self.assertIsNone(audit.profile_minus_two_point_limit)
        self.assertTrue(audit.independent_optimizer_message)
        self.assertIn(audit.status, (
            "OPTIMIZER_CONCORDANT",
            "OPTIMIZER_DISCORDANT",
            "INDEPENDENT_OPTIMIZER_UNRESOLVED",
            "LIKELIHOOD_CONCORDANT_PARAMETER_DISAGREEMENT",
        ))

    def test_profile_concentration_curvature_is_nuisance_adjusted_schur_complement(self):
        audit = audit_beta_binomial_count_fit(COUNTS, R)
        self.assertIsNotNone(audit.selected_mean_logit)
        self.assertIsNotNone(audit.selected_log_concentration)
        self.assertIsNotNone(audit.profile_log_concentration_curvature)
        selected = beta_binomial_loglik_score_hessian(
            COUNTS, R,
            mean_logit=audit.selected_mean_logit,
            log_concentration=audit.selected_log_concentration,
        )
        self.assertNotEqual(selected.hessian_mean_logit, 0.0)
        expected = (
            selected.hessian_log_concentration
            - selected.hessian_cross ** 2 / selected.hessian_mean_logit
        )
        self.assertAlmostEqual(
            audit.profile_log_concentration_curvature, expected, delta=1e-12,
        )
        # This raw local curvature is not folded into optimizer-concordance
        # status and does not introduce an identification/selection threshold.
        self.assertIn(audit.status, (
            "OPTIMIZER_CONCORDANT",
            "OPTIMIZER_DISCORDANT",
            "INDEPENDENT_OPTIMIZER_UNRESOLVED",
            "LIKELIHOOD_CONCORDANT_PARAMETER_DISAGREEMENT",
        ))

    def test_finite_r_count_likelihood_matches_independent_exact_pmf_oracle(self):
        alpha, beta, r = 2.0, 2.0, 5
        reference = beta_binomial_f5_reference(
            alpha=alpha, beta=beta, m=10, r=r,
        )
        for count, expected in enumerate(reference.pmf_cluster_count):
            result = beta_binomial_loglik_score_hessian(
                (count, count), r,
                mean_logit=math.log(alpha / beta),
                log_concentration=math.log(alpha + beta),
            )
            observed = math.exp(result.log_likelihood / 2.0)
            self.assertAlmostEqual(observed, expected, delta=2e-14)
        self.assertAlmostEqual(sum(reference.pmf_cluster_count), 1.0, places=14)

    def test_boundary_adjacent_score_remains_finite_and_matches_differences(self):
        for eta, xi in ((-4.0, math.log(0.2)), (4.0, math.log(1e3))):
            with self.subTest(eta=eta, xi=xi):
                h = 1e-5
                def ll(a, b):
                    return beta_binomial_loglik_score_hessian(
                        COUNTS, R, mean_logit=a, log_concentration=b,
                    ).log_likelihood
                result = beta_binomial_loglik_score_hessian(
                    COUNTS, R, mean_logit=eta, log_concentration=xi,
                )
                score_eta = (ll(eta + h, xi) - ll(eta - h, xi)) / (2 * h)
                score_xi = (ll(eta, xi + h) - ll(eta, xi - h)) / (2 * h)
                self.assertTrue(math.isfinite(result.score_mean_logit))
                self.assertTrue(math.isfinite(result.score_log_concentration))
                self.assertAlmostEqual(result.score_mean_logit, score_eta, delta=2e-5)
                self.assertAlmostEqual(result.score_log_concentration, score_xi, delta=2e-5)

    def test_two_point_limit_is_the_low_concentration_limit(self):
        counts = (0, 5, 0, 5, 5, 0)
        result = beta_binomial_extended_boundary_likelihoods(
            counts, 5, mean_probability=0.4, concentration=1e-7,
        )
        self.assertTrue(math.isfinite(result.finite_log_likelihood))
        self.assertAlmostEqual(
            result.finite_log_likelihood,
            result.two_point_mixing_limit_log_likelihood,
            delta=2e-5,
        )

    def test_binomial_limit_is_the_high_concentration_limit(self):
        counts = (0, 1, 3, 5, 4, 2)
        result = beta_binomial_extended_boundary_likelihoods(
            counts, 5, mean_probability=0.37, concentration=1e5,
        )
        self.assertAlmostEqual(
            result.finite_log_likelihood,
            result.binomial_limit_log_likelihood,
            delta=0.02,
        )


    def test_profile_trace_records_nuisance_profile_and_local_curvature(self):
        center = math.log(3.4)
        h = 1e-2
        points = beta_binomial_profile_log_concentration(
            COUNTS, R, (center - h, center, center + h),
        )
        self.assertEqual(len(points), 3)
        self.assertTrue(all(
            point.status == "NUMERICAL_PROFILE_UNCERTIFIED"
            and not point.mean_profile_at_bound
            and math.isfinite(point.profiled_log_likelihood)
            and abs(point.nuisance_score) < 2e-5
            for point in points
        ))
        finite_difference_curvature = (
            points[0].profiled_log_likelihood
            - 2.0 * points[1].profiled_log_likelihood
            + points[2].profiled_log_likelihood
        ) / (h * h)
        self.assertIsNotNone(points[1].profile_log_concentration_curvature)
        self.assertAlmostEqual(
            points[1].profile_log_concentration_curvature,
            finite_difference_curvature,
            delta=3e-2,
        )

    def test_profile_trace_rejects_unsorted_or_duplicate_concentrations(self):
        with self.assertRaisesRegex(
            F5LikelihoodDiagnosticError, "STRICTLY_INCREASING",
        ):
            beta_binomial_profile_log_concentration(
                COUNTS, R, (0.0, 0.2, 0.2),
            )

    def test_profiled_boundary_models_optimize_their_own_mean(self):
        result = beta_binomial_profiled_boundary_likelihoods(COUNTS, R)
        expected_mean = sum(COUNTS) / (len(COUNTS) * R)
        self.assertAlmostEqual(result.binomial_profile_mean, expected_mean)
        self.assertTrue(math.isfinite(result.binomial_profile_log_likelihood))
        self.assertEqual(result.interior_count_observations, 8)
        self.assertIsNone(result.two_point_profile_log_likelihood)
        self.assertEqual(result.two_point_boundary_status, "ZERO_PROBABILITY_INTERIOR_COUNTS")
        self.assertIsNone(result.two_point_profile_mean)

    def test_two_point_profile_boundary_uses_endpoint_mixture_mle(self):
        counts = (0, 5, 0, 5, 5, 0)
        result = beta_binomial_profiled_boundary_likelihoods(counts, 5)
        self.assertEqual(result.interior_count_observations, 0)
        self.assertAlmostEqual(result.two_point_profile_mean, 0.5)
        self.assertAlmostEqual(
            result.two_point_profile_log_likelihood,
            3 * math.log(0.5) + 3 * math.log(0.5),
        )


    def test_profile_likelihood_is_invariant_to_world_count_permutation(self):
        grid = (math.log(0.2), math.log(0.7), math.log(2.0), math.log(20.0))
        original = beta_binomial_profile_log_concentration(COUNTS, R, grid)
        permuted = beta_binomial_profile_log_concentration(
            tuple(reversed(COUNTS)), R, grid,
        )
        for left, right in zip(original, permuted):
            self.assertAlmostEqual(
                left.profiled_log_likelihood,
                right.profiled_log_likelihood,
                delta=1e-12,
            )
            self.assertAlmostEqual(
                left.profiled_mean_logit, right.profiled_mean_logit, delta=5e-8,
            )

    def test_endpoint_only_fixture_retains_finite_two_point_profile_limit(self):
        counts = (0, 5, 0, 5, 5, 0)
        boundary = beta_binomial_profiled_boundary_likelihoods(counts, 5)
        self.assertEqual(boundary.interior_count_observations, 0)
        self.assertAlmostEqual(boundary.two_point_profile_mean, 0.5)
        self.assertTrue(math.isfinite(boundary.two_point_profile_log_likelihood))
        trace = beta_binomial_profile_log_concentration(
            counts, 5, (math.log(0.2), 0.0, math.log(5.0)),
        )
        self.assertTrue(all(
            point.status == "NUMERICAL_PROFILE_UNCERTIFIED" for point in trace
        ))

    def test_low_dispersion_fixture_retains_own_binomial_profile_mean(self):
        counts = (2, 2, 2, 2, 2, 2, 2, 2)
        boundary = beta_binomial_profiled_boundary_likelihoods(counts, 5)
        self.assertAlmostEqual(boundary.binomial_profile_mean, 0.4)
        self.assertTrue(math.isfinite(boundary.binomial_profile_log_likelihood))
        self.assertIsNone(boundary.two_point_profile_log_likelihood)
        self.assertEqual(boundary.two_point_boundary_status, "ZERO_PROBABILITY_INTERIOR_COUNTS")


    def test_profile_audit_keeps_optimizer_boundary_and_identification_separate(self):
        optimizer = audit_beta_binomial_count_fit(COUNTS, R)
        grid = (math.log(0.2), math.log(0.7), math.log(2.0), math.log(20.0))
        profile = beta_binomial_profile_log_concentration(COUNTS, R, grid)
        boundary = beta_binomial_profiled_boundary_likelihoods(COUNTS, R)
        record = build_beta_binomial_profile_audit_record(
            optimizer, profile, boundary,
        )
        self.assertEqual(
            record.optimizer_convergence_status, optimizer.status,
        )
        self.assertEqual(record.identification_status, "INDETERMINATE")
        self.assertEqual(record.profile_status, "NUMERICAL_PROFILE_UNCERTIFIED")
        self.assertEqual(record.profile_point_count, len(grid))
        self.assertTrue(math.isfinite(record.profile_minus_binomial_boundary))
        self.assertIsNone(record.profile_minus_two_point_boundary)
        self.assertEqual(
            record.two_point_boundary_status, "ZERO_PROBABILITY_INTERIOR_COUNTS",
        )
        self.assertEqual(
            len(record.profile_curvature_values), len(profile),
        )
        json.dumps(asdict(record), allow_nan=False)
        json.dumps(asdict(boundary), allow_nan=False)

    def test_profile_audit_rejects_empty_or_unordered_profile(self):
        optimizer = audit_beta_binomial_count_fit(COUNTS, R)
        boundary = beta_binomial_profiled_boundary_likelihoods(COUNTS, R)
        with self.assertRaisesRegex(
            F5LikelihoodDiagnosticError, "REQUIRES_POINTS",
        ):
            build_beta_binomial_profile_audit_record(optimizer, (), boundary)
        points = beta_binomial_profile_log_concentration(
            COUNTS, R, (0.0, 0.2, 0.4),
        )
        with self.assertRaisesRegex(
            F5LikelihoodDiagnosticError, "STRICTLY_INCREASING",
        ):
            build_beta_binomial_profile_audit_record(
                optimizer, tuple(reversed(points)), boundary,
            )


    def test_failed_nuisance_refinement_is_not_misreported_as_boundary(self):
        with patch(
            "c10s_f5_beta_binomial_likelihood_diagnostics.minimize_scalar",
            return_value=SimpleNamespace(success=False, fun=1e9, x=0.0),
        ):
            points = beta_binomial_profile_log_concentration(
                COUNTS, R, (math.log(0.5), 0.0, math.log(2.0)),
            )
        self.assertTrue(all(not point.mean_profile_at_bound for point in points))
        self.assertTrue(all(
            not point.nuisance_refinement_succeeded for point in points
        ))
        self.assertTrue(all(
            point.status == "NUISANCE_PROFILE_OPTIMIZER_UNRESOLVED"
            and point.profile_log_concentration_curvature is None
            for point in points
        ))


    def test_profile_numerical_stability_retains_grid_and_bound_sensitivities(self):
        result = beta_binomial_profile_numerical_stability(
            COUNTS, R, (-0.7, 0.0, 0.7),
            mean_logit_bounds=(-8.0, 8.0),
            expanded_mean_logit_bounds=(-12.0, 12.0),
            mean_grid_size=33,
            refined_mean_grid_size=65,
        )
        self.assertEqual(result.status, "NUMERICAL_STABILITY_NOT_ADJUDICATED")
        self.assertEqual(result.identification_status, "INDETERMINATE")
        self.assertEqual(result.profile_point_count, 3)
        self.assertEqual(result.reference_mean_grid_size, 33)
        self.assertEqual(result.refined_mean_grid_size, 65)
        self.assertEqual(
            tuple(point.log_concentration for point in result.points),
            (-0.7, 0.0, 0.7),
        )
        self.assertTrue(all(
            math.isfinite(point.refined_minus_reference_log_likelihood)
            and math.isfinite(point.expanded_minus_reference_log_likelihood)
            and math.isfinite(point.refined_minus_reference_mean_logit)
            and math.isfinite(point.expanded_minus_reference_mean_logit)
            for point in result.points
        ))
        json.dumps(asdict(result), allow_nan=False)

    def test_profile_numerical_stability_rejects_invalid_control_relationships(self):
        with self.assertRaisesRegex(
            F5LikelihoodDiagnosticError, "INVALID_STABILITY_GRID_SIZES",
        ):
            beta_binomial_profile_numerical_stability(
                COUNTS, R, (-0.7, 0.0, 0.7),
                mean_grid_size=65, refined_mean_grid_size=65,
            )
        with self.assertRaisesRegex(
            F5LikelihoodDiagnosticError, "EXPANDED_BOUNDS_MUST_STRICTLY_CONTAIN",
        ):
            beta_binomial_profile_numerical_stability(
                COUNTS, R, (-0.7, 0.0, 0.7),
                mean_logit_bounds=(-8.0, 8.0),
                expanded_mean_logit_bounds=(-7.0, 9.0),
                mean_grid_size=33, refined_mean_grid_size=65,
            )


    def test_profile_audit_fixture_matrix_keeps_three_likelihood_regimes_separate(self):
        fixtures = (
            (
                "ENDPOINT_ONLY",
                (0, 5, 0, 5, 5, 0),
                "FINITE_ENDPOINT_MIXTURE_PROFILE",
                0,
                True,
            ),
            (
                "LOW_DISPERSION",
                (2, 2, 2, 2, 2, 2, 2, 2),
                "ZERO_PROBABILITY_INTERIOR_COUNTS",
                8,
                False,
            ),
            (
                "INTERIOR_COUNTS",
                COUNTS,
                "ZERO_PROBABILITY_INTERIOR_COUNTS",
                8,
                False,
            ),
        )
        grid = (math.log(0.2), 0.0, math.log(5.0))
        for name, counts, expected_boundary_status, expected_interior, has_two_point in fixtures:
            with self.subTest(fixture=name):
                profile = beta_binomial_profile_log_concentration(
                    counts, R, grid, mean_grid_size=65,
                )
                boundary = beta_binomial_profiled_boundary_likelihoods(counts, R)
                record = build_beta_binomial_profile_audit_record(
                    SimpleNamespace(status="FIXTURE_OPTIMIZER_STATUS"),
                    profile,
                    boundary,
                )
                self.assertEqual(boundary.interior_count_observations, expected_interior)
                self.assertEqual(boundary.two_point_boundary_status, expected_boundary_status)
                self.assertTrue(math.isfinite(boundary.binomial_profile_log_likelihood))
                self.assertEqual(
                    boundary.two_point_profile_log_likelihood is not None,
                    has_two_point,
                )
                if has_two_point:
                    self.assertTrue(math.isfinite(boundary.two_point_profile_log_likelihood))
                else:
                    self.assertIsNone(boundary.two_point_profile_log_likelihood)
                self.assertEqual(record.optimizer_convergence_status, "FIXTURE_OPTIMIZER_STATUS")
                self.assertEqual(record.identification_status, "INDETERMINATE")
                self.assertEqual(record.profile_point_count, len(grid))
                self.assertEqual(
                    record.profile_max_log_likelihood,
                    max(point.profiled_log_likelihood for point in profile),
                )
                self.assertAlmostEqual(
                    record.profile_minus_binomial_boundary,
                    record.profile_max_log_likelihood
                    - boundary.binomial_profile_log_likelihood,
                    delta=1e-12,
                )
                if has_two_point:
                    self.assertAlmostEqual(
                        record.profile_minus_two_point_boundary,
                        record.profile_max_log_likelihood
                        - boundary.two_point_profile_log_likelihood,
                        delta=1e-12,
                    )
                else:
                    self.assertIsNone(record.profile_minus_two_point_boundary)
                self.assertEqual(len(record.profile_curvature_values), len(grid))
                self.assertEqual(
                    record.profile_status,
                    "NUMERICAL_PROFILE_UNCERTIFIED"
                    if all(point.status == "NUMERICAL_PROFILE_UNCERTIFIED" for point in profile)
                    else "PROFILE_HAS_BOUNDARY_OR_UNRESOLVED_POINTS",
                )
                json.dumps(asdict(record), allow_nan=False)


if __name__ == "__main__":
    unittest.main()
