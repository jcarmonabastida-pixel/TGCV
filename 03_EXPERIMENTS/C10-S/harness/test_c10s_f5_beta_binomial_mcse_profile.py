from __future__ import annotations

import math
import unittest

from scipy.special import digamma

from c10s_f5_beta_binomial_mcse_profile import (
    F5ProfileError,
    f5_beta_binomial_mcse_profile_loglik,
    f5_beta_binomial_mcse_profile_confidence_set,
    _bisect_profile_crossing,
    f5_beta_binomial_mcse_profile_grid_convergence,
    _optimizer_adjudication,
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

    def test_asymmetric_beta_binomial_point_is_bounded_by_profile(self):
        # Independent direct log-likelihood using math.lgamma, not the
        # production betaln/gammaln implementation.
        mu, concentration = 0.23, 3.7
        target_m, target_r = 10, 5
        mcse = math.sqrt(
            mu * (1.0 - mu) * (1.0 + concentration / target_r)
            / (target_m * (1.0 + concentration))
        )
        counts = [sum(row) for row in ROWS]
        observed_r = len(ROWS[0])
        alpha = mu * concentration
        beta = (1.0 - mu) * concentration

        def log_beta(a, b):
            return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)

        direct = 0.0
        for count in counts:
            log_choose = (
                math.lgamma(observed_r + 1)
                - math.lgamma(count + 1)
                - math.lgamma(observed_r - count + 1)
            )
            direct += log_choose + log_beta(
                count + alpha, observed_r - count + beta,
            ) - log_beta(alpha, beta)

        profiled = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=target_m, target_r=target_r,
            target_mcse=mcse, concentration_grid_points=801,
        )
        self.assertGreaterEqual(profiled.profile_loglik, direct - 1e-7)

    def test_beta_binomial_analytic_scores_match_independent_finite_differences(self):
        mu, concentration = 0.23, 3.7
        r = len(ROWS[0])
        counts = [sum(row) for row in ROWS]
        alpha, beta = mu * concentration, (1.0 - mu) * concentration

        score_mu = sum(
            concentration * (
                digamma(x + alpha) - digamma(r - x + beta)
                - digamma(alpha) + digamma(beta)
            )
            for x in counts
        )
        score_kappa = sum(
            mu * digamma(x + alpha)
            + (1.0 - mu) * digamma(r - x + beta)
            - digamma(r + concentration)
            - mu * digamma(alpha)
            - (1.0 - mu) * digamma(beta)
            + digamma(concentration)
            for x in counts
        )

        def independent_loglik(m, k):
            a, b = m * k, (1.0 - m) * k

            def lb(u, v):
                return math.lgamma(u) + math.lgamma(v) - math.lgamma(u + v)

            total = 0.0
            for x in counts:
                choose = (
                    math.lgamma(r + 1) - math.lgamma(x + 1)
                    - math.lgamma(r - x + 1)
                )
                total += choose + lb(x + a, r - x + b) - lb(a, b)
            return total

        eps = 1e-6
        numeric_mu = (
            independent_loglik(mu + eps, concentration)
            - independent_loglik(mu - eps, concentration)
        ) / (2.0 * eps)
        numeric_kappa = (
            independent_loglik(mu, concentration + eps)
            - independent_loglik(mu, concentration - eps)
        ) / (2.0 * eps)

        self.assertAlmostEqual(score_mu, numeric_mu, delta=2e-5)
        self.assertAlmostEqual(score_kappa, numeric_kappa, delta=2e-5)

    def test_optimizer_adjudication_all_four_states(self):
        self.assertEqual(
            _optimizer_adjudication((9, 8), (1e-9, 1e-8), boundary_sensitive=False),
            "OPTIMIZATION_CONCORDANT",
        )
        self.assertEqual(
            _optimizer_adjudication((9, 8), (1e-9, 1e-4), boundary_sensitive=False),
            "OPTIMIZATION_DISCORDANT",
        )
        self.assertEqual(
            _optimizer_adjudication((9, 2), (1e-9, 1e-8), boundary_sensitive=False),
            "OPTIMIZATION_INSUFFICIENT",
        )
        self.assertEqual(
            _optimizer_adjudication((9, 8), (1e-9, 1e-8), boundary_sensitive=True),
            "OPTIMIZATION_BOUNDARY_SENSITIVE",
        )

    def test_optimizer_adjudication_rejects_malformed_diagnostics(self):
        with self.assertRaisesRegex(F5ProfileError, "TWO_BRANCHES"):
            _optimizer_adjudication((9,), (1e-9,), boundary_sensitive=False)
        with self.assertRaisesRegex(F5ProfileError, "NONNEGATIVE"):
            _optimizer_adjudication((9, -1), (1e-9, 1e-8), boundary_sensitive=False)
        with self.assertRaisesRegex(F5ProfileError, "GAPS"):
            _optimizer_adjudication((9, 8), (float("nan"), 1e-8), boundary_sensitive=False)

    def test_profile_exposes_branch_local_maxima_diagnostics(self):
        result = f5_beta_binomial_mcse_profile_loglik(
            ROWS, target_m=10, target_r=5, target_mcse=0.05,
            concentration_grid_points=161,
        )
        diagnostics = dict(result.optimizer_diagnostics)
        for key in (
            "mu_plus_grid_local_maxima_count",
            "mu_minus_grid_local_maxima_count",
            "mu_plus_grid_local_maxima_kappa",
            "mu_minus_grid_local_maxima_kappa",
            "mu_plus_top_two_local_maxima_loglik_gap",
            "mu_minus_top_two_local_maxima_loglik_gap",
            "mu_plus_independent_multistart_successes",
            "mu_minus_independent_multistart_successes",
            "mu_plus_independent_optimizer_gap",
            "mu_minus_independent_optimizer_gap",
            "optimizer_adjudication",
            "optimizer_loglik_tolerance",
            "optimizer_min_successful_starts_per_branch",
        ):
            self.assertIn(key, diagnostics)
        self.assertGreaterEqual(int(diagnostics["mu_plus_grid_local_maxima_count"]), 0)
        self.assertGreaterEqual(int(diagnostics["mu_minus_grid_local_maxima_count"]), 0)

    def test_adversarial_cluster_count_patterns_keep_both_mean_branches(self):
        # Boundary-heavy, strongly asymmetric, and interior-heavy empirical
        # cluster-count patterns. Every row is a world; columns are Bernoulli
        # inner replicates. This is a deterministic shape stress test, not a
        # Monte Carlo coverage experiment.
        fixtures = {
            "all_zero": tuple((0, 0, 0, 0, 0) for _ in range(8)),
            "all_one": tuple((1, 1, 1, 1, 1) for _ in range(8)),
            "endpoint_mixture": (
                *((0, 0, 0, 0, 0) for _ in range(5)),
                *((1, 1, 1, 1, 1) for _ in range(3)),
            ),
            "asymmetric_endpoints": (
                *((0, 0, 0, 0, 0) for _ in range(7)),
                *((1, 1, 1, 1, 1) for _ in range(1)),
            ),
            "interior_heavy": (
                *((1, 1, 0, 0, 0) for _ in range(5)),
                *((1, 1, 1, 0, 0) for _ in range(3)),
            ),
            "mixed_extremes_and_interior": (
                (0, 0, 0, 0, 0), (1, 1, 1, 1, 1),
                (1, 1, 0, 0, 0), (1, 0, 1, 0, 1),
                (0, 1, 0, 1, 0), (1, 1, 1, 0, 0),
            ),
        }
        target_m, target_r = 12, 5
        g_max = 1.0 / (2.0 * math.sqrt(target_m))
        for fixture_name, rows in fixtures.items():
            for fraction in (0.1, 0.35, 0.7, 0.95):
                result = f5_beta_binomial_mcse_profile_loglik(
                    rows, target_m=target_m, target_r=target_r,
                    target_mcse=fraction * g_max,
                    concentration_grid_points=161,
                )
                self.assertTrue(
                    math.isfinite(result.profile_loglik),
                    msg=f"{fixture_name} at fraction={fraction}: {result}",
                )
                self.assertIn(result.maximizing_branch, {"MU_PLUS", "MU_MINUS"})
                self.assertTrue(
                    math.isfinite(result.branch_loglik_plus),
                    msg=f"{fixture_name}: μ+ branch was not finite",
                )
                self.assertTrue(
                    math.isfinite(result.branch_loglik_minus),
                    msg=f"{fixture_name}: μ- branch was not finite",
                )

    def test_adversarial_lr_sets_never_escape_parameter_space(self):
        fixtures = (
            tuple((0, 0, 0, 0, 0) for _ in range(6))
            + tuple((1, 1, 1, 1, 1) for _ in range(2)),
            tuple((1, 1, 0, 0, 0) for _ in range(5))
            + tuple((1, 1, 1, 0, 0) for _ in range(3)),
        )
        upper = 1.0 / (2.0 * math.sqrt(12))
        for rows in fixtures:
            result = f5_beta_binomial_mcse_profile_confidence_set(
                rows, target_m=12, target_r=5,
                likelihood_ratio_cutoff=3.841458820694124,
                scan_grid_points=31, concentration_grid_points=81,
            )
            for lower, high in result.confidence_components:
                self.assertGreaterEqual(lower, 0.0)
                self.assertGreater(high, lower)
                self.assertLessEqual(high, upper + 1e-12)
            if result.confidence_components:
                self.assertEqual(
                    result.confidence_hull,
                    (result.confidence_components[0][0],
                     result.confidence_components[-1][1]),
                )

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

    def test_nested_grid_convergence_reports_resolution_differences(self):
        result = f5_beta_binomial_mcse_profile_grid_convergence(
            ROWS, target_m=10, target_r=5,
            likelihood_ratio_cutoff=3.841458820694124,
            coarse_scan_grid_points=21, fine_scan_grid_points=41,
            coarse_concentration_grid_points=81,
            fine_concentration_grid_points=161,
            tolerance=0.1,
        )
        self.assertGreaterEqual(result.maximum_loglik_difference, 0.0)
        self.assertTrue(
            result.endpoint_maximum_difference is None
            or result.endpoint_maximum_difference >= 0.0
        )
        self.assertIsInstance(result.component_count_stable, bool)
        self.assertIsInstance(result.within_tolerance, bool)

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

    def test_profile_rejects_noninteger_or_boolean_concentration_grid(self):
        for invalid in (40.0, True, 80.5):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(F5ProfileError, "CONCENTRATION_GRID_POINTS"):
                    f5_beta_binomial_mcse_profile_loglik(
                        ROWS, target_m=10, target_r=5, target_mcse=0.05,
                        concentration_grid_points=invalid,
                    )

    def test_convergence_rejects_noninteger_grid_contracts(self):
        with self.assertRaisesRegex(F5ProfileError, "CONVERGENCE_GRID_POINTS_MUST_BE_INTEGERS"):
            f5_beta_binomial_mcse_profile_grid_convergence(
                ROWS, target_m=10, target_r=5,
                likelihood_ratio_cutoff=3.841458820694124,
                coarse_scan_grid_points=21, fine_scan_grid_points=41.5,
                coarse_concentration_grid_points=81,
                fine_concentration_grid_points=161,
            )
        with self.assertRaisesRegex(F5ProfileError, "CONCENTRATION_GRID_POINTS"):
            f5_beta_binomial_mcse_profile_grid_convergence(
                ROWS, target_m=10, target_r=5,
                likelihood_ratio_cutoff=3.841458820694124,
                coarse_scan_grid_points=21, fine_scan_grid_points=41,
                coarse_concentration_grid_points=40,
                fine_concentration_grid_points=161,
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
