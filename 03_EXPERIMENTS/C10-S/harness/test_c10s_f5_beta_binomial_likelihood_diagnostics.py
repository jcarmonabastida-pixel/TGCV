from __future__ import annotations

import math
import unittest

from c10s_beta_binomial_variance_oracles import beta_binomial_f5_reference
from c10s_f5_beta_binomial_likelihood_diagnostics import (
    F5LikelihoodDiagnosticError,
    beta_binomial_extended_boundary_likelihoods,
    beta_binomial_loglik_score_hessian,
    audit_beta_binomial_count_fit,
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
        self.assertTrue(audit.independent_optimizer_message)
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


if __name__ == "__main__":
    unittest.main()
