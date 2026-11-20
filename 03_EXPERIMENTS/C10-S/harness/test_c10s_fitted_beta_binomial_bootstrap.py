from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np

from c10s_fitted_beta_binomial_bootstrap import (
    BetaBinomialFitError,
    fit_beta_binomial_counts,
    fitted_beta_binomial_parametric_bootstrap,
)


class FittedBetaBinomialBootstrapTests(unittest.TestCase):
    def test_mle_recovers_finite_interior_fit_for_overdispersed_counts(self):
        fit = fit_beta_binomial_counts((0, 0, 1, 4, 5, 5, 2, 3, 0, 5), 5)
        self.assertTrue(fit.converged)
        self.assertFalse(fit.boundary)
        self.assertGreater(fit.alpha, 0.0)
        self.assertGreater(fit.beta, 0.0)
        self.assertGreater(fit.concentration, 0.0)
        self.assertTrue(float("-inf") < fit.log_likelihood < float("inf"))

    def test_fitted_bootstrap_is_reproducible_and_returns_all_three_intervals(self):
        rows = (
            (0, 0, 0, 0, 0),
            (0, 0, 0, 0, 1),
            (0, 1, 0, 1, 0),
            (1, 1, 1, 0, 1),
            (1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1),
            (0, 0, 1, 1, 1),
            (0, 1, 1, 1, 1),
            (0, 0, 0, 1, 1),
            (1, 0, 1, 1, 1),
        )
        kwargs = dict(
            target_m=10, target_r=5, bootstrap_replicates=250,
            bootstrap_seed=20261119,
        )
        first = fitted_beta_binomial_parametric_bootstrap(rows, **kwargs)
        second = fitted_beta_binomial_parametric_bootstrap(rows, **kwargs)
        self.assertIsNotNone(first.fit)
        self.assertIsNotNone(first.optimizer_audit)
        self.assertEqual(len(first.optimizer_audit.starts), 3)
        self.assertIn(dict(first.comparison.provenance)["optimizer_audit_status"], (
            "OPTIMIZER_CONCORDANT", "OPTIMIZER_DISCORDANT",
            "INDEPENDENT_OPTIMIZER_UNRESOLVED",
            "LIKELIHOOD_CONCORDANT_PARAMETER_DISAGREEMENT",
            "DIAGNOSTIC_UNAVAILABLE",
        ))
        self.assertFalse(first.fit.boundary)
        self.assertEqual(first.comparison.within_interval, second.comparison.within_interval)
        self.assertEqual(first.comparison.between_interval, second.comparison.between_interval)
        self.assertEqual(first.comparison.mcse_interval, second.comparison.mcse_interval)
        self.assertIsNotNone(first.comparison.within_interval)
        self.assertIsNotNone(first.comparison.between_interval)
        self.assertGreaterEqual(first.valid_mcse_rate, 0.90)
        self.assertEqual(first.comparison.method_id, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0")

    def test_production_fit_retains_all_starts_and_direct_analytic_reconciliation(self):
        from c10s_fitted_beta_binomial_bootstrap import build_production_analytic_reconciliation
        from c10s_f5_beta_binomial_likelihood_diagnostics import audit_beta_binomial_count_fit

        counts = (0, 0, 1, 4, 5, 5, 2, 3, 0, 5)
        production = fit_beta_binomial_counts(counts, 5)
        analytic = audit_beta_binomial_count_fit(counts, 5)
        self.assertEqual(len(production.production_starts), 3)
        self.assertIn(production.selected_start_index, (0, 1, 2))
        self.assertEqual(
            production.log_likelihood,
            -production.production_starts[production.selected_start_index].negative_log_likelihood,
        )
        record = build_production_analytic_reconciliation(production, analytic)
        self.assertEqual(record["schema"], "C10S_F5_PRODUCTION_ANALYTIC_RECONCILIATION_1.0")
        self.assertEqual(record["status"], "RAW_COMPARISON_RECORDED_NO_ADJUDICATION_THRESHOLD")
        self.assertEqual(record["adjudication"].split(";")[0], "NOT_THRESHOLDED")
        self.assertEqual(len(record["production_fit"]["starts"]), 3)
        self.assertEqual(len(record["analytic_fit"]["starts"]), 3)
        direct = record["direct_comparison"]
        self.assertAlmostEqual(
            direct["log_likelihood_difference_production_minus_analytic"],
            production.log_likelihood - analytic.selected_log_likelihood,
            places=12,
        )
        self.assertAlmostEqual(
            direct["alpha_difference_production_minus_analytic"],
            production.alpha - (
                (1.0 / (1.0 + __import__("math").exp(-analytic.selected_mean_logit))
                 if analytic.selected_mean_logit >= 0
                 else __import__("math").exp(analytic.selected_mean_logit)
                 / (1.0 + __import__("math").exp(analytic.selected_mean_logit)))
                * __import__("math").exp(analytic.selected_log_concentration)
            ),
            places=10,
        )
        self.assertEqual(
            record["independent_optimizer_scope"],
            "LOCAL_BFGS_CHECK_INITIALIZED_FROM_ANALYTIC_FIT_NOT_GLOBAL_SEARCH",
        )

    def test_reconciliation_is_typed_when_production_or_analytic_fit_is_missing(self):
        from c10s_fitted_beta_binomial_bootstrap import build_production_analytic_reconciliation
        self.assertEqual(
            build_production_analytic_reconciliation(None, None)["status"],
            "PRODUCTION_FIT_NOT_AVAILABLE",
        )
        fit = fit_beta_binomial_counts((0, 0, 1, 4, 5, 5, 2, 3, 0, 5), 5)
        missing = build_production_analytic_reconciliation(fit, None, audit_error="INJECTED")
        self.assertEqual(missing["status"], "ANALYTIC_AUDIT_UNAVAILABLE")
        self.assertIsNone(missing["direct_comparison"])
        self.assertEqual(missing["audit_error"], "INJECTED")

    def test_failed_production_multistart_outcomes_are_retained_for_reconciliation(self):
        from c10s_fitted_beta_binomial_bootstrap import build_production_analytic_reconciliation

        failed = SimpleNamespace(
            x=np.asarray([0.1, 0.2]), success=False,
            message="precision loss", fun=12.5,
            jac=np.asarray([1e-7, -1e-7]),
        )
        with patch(
            "c10s_fitted_beta_binomial_bootstrap.minimize",
            side_effect=[failed, failed, failed],
        ):
            with self.assertRaises(BetaBinomialFitError) as caught:
                fit_beta_binomial_counts((0, 0, 1, 4, 5, 5, 2, 3, 0, 5), 5)
        self.assertEqual(len(caught.exception.production_starts), 3)
        self.assertTrue(all(not item.success for item in caught.exception.production_starts))
        record = build_production_analytic_reconciliation(
            None, None, production_starts=caught.exception.production_starts,
        )
        self.assertEqual(record["status"], "PRODUCTION_OPTIMIZATION_NO_ADMISSIBLE_FIT")
        self.assertEqual(len(record["production_fit"]["starts"]), 3)
        self.assertIsNone(record["production_fit"]["selected_log_likelihood"])
        self.assertIsNone(record["direct_comparison"])

    def test_all_zero_and_all_one_worlds_abstain_with_typed_boundary(self):
        for value in (0, 1):
            rows = tuple(tuple(value for _ in range(5)) for _ in range(8))
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=10, target_r=5, bootstrap_replicates=50,
                bootstrap_seed=19,
            )
            self.assertIsNone(result.fit)
            self.assertIsNotNone(result.optimizer_audit)
            self.assertEqual(len(result.optimizer_audit.starts), 3)
            self.assertIn("ALL_ZERO_OR_ALL_ONE_BOUNDARY", result.failure_reason)
            self.assertEqual(result.comparison.abstention_reason, result.failure_reason)

    def test_non_bernoulli_input_is_rejected(self):
        rows = ((0.0, 0.5), (1.0, 0.0), (0.0, 1.0))
        with self.assertRaises(BetaBinomialFitError):
            fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=5, target_r=3, bootstrap_replicates=50,
                bootstrap_seed=19,
            )

    def test_no_between_cluster_count_variation_is_not_misreported_as_finite_fit(self):
        with self.assertRaisesRegex(
            BetaBinomialFitError, "NO_BETWEEN_CLUSTER_COUNT_VARIATION_BOUNDARY",
        ):
            fit_beta_binomial_counts((2, 2, 2, 2, 2), 5)

    def test_invalid_count_support_fails_closed(self):
        for counts, r in (((0, 1), 1), ((0, 3), 2), ((0.5, 1), 2), ((0,), 2)):
            with self.subTest(counts=counts, r=r), self.assertRaises(BetaBinomialFitError):
                fit_beta_binomial_counts(counts, r)


if __name__ == "__main__":
    unittest.main()
