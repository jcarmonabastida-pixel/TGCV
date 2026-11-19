from __future__ import annotations

import unittest

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
        self.assertFalse(first.fit.boundary)
        self.assertEqual(first.comparison.within_interval, second.comparison.within_interval)
        self.assertEqual(first.comparison.between_interval, second.comparison.between_interval)
        self.assertEqual(first.comparison.mcse_interval, second.comparison.mcse_interval)
        self.assertIsNotNone(first.comparison.within_interval)
        self.assertIsNotNone(first.comparison.between_interval)
        self.assertGreaterEqual(first.valid_mcse_rate, 0.90)
        self.assertEqual(first.comparison.method_id, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0")

    def test_all_zero_and_all_one_worlds_abstain_with_typed_boundary(self):
        for value in (0, 1):
            rows = tuple(tuple(value for _ in range(5)) for _ in range(8))
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=10, target_r=5, bootstrap_replicates=50,
                bootstrap_seed=19,
            )
            self.assertIsNone(result.fit)
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
