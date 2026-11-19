from __future__ import annotations

import itertools
import math
import unittest

import numpy as np

from c10s_beta_binomial_variance_oracles import (
    BetaBinomialOracleError,
    beta_binomial_f5_reference,
)


class BetaBinomialVarianceOracleTests(unittest.TestCase):
    def test_beta22_matches_frozen_f5_population_components(self):
        result = beta_binomial_f5_reference(alpha=2, beta=2, m=10, r=5)
        self.assertAlmostEqual(result.true_within, 0.20, places=14)
        self.assertAlmostEqual(result.true_between, 0.05, places=14)
        self.assertAlmostEqual(result.observed_world_mean_variance, 0.09, places=14)
        self.assertAlmostEqual(
            result.expected_raw_between_estimator, 0.05, places=14,
        )
        self.assertAlmostEqual(result.true_mcse, math.sqrt(0.09 / 10), places=14)

    def test_beta_binomial_count_pmf_is_normalized_and_nonnegative(self):
        result = beta_binomial_f5_reference(alpha=2, beta=2, m=10, r=5)
        self.assertEqual(len(result.pmf_cluster_count), 6)
        self.assertAlmostEqual(sum(result.pmf_cluster_count), 1.0, places=14)
        self.assertTrue(all(p >= 0.0 for p in result.pmf_cluster_count))

    def test_finite_sample_estimator_moments_match_exhaustive_count_enumeration(self):
        m, r, alpha, beta = 3, 2, 2.0, 2.0
        result = beta_binomial_f5_reference(alpha=alpha, beta=beta, m=m, r=r)
        pmf = result.pmf_cluster_count
        outcomes = []
        for counts in itertools.product(range(r + 1), repeat=m):
            probability = math.prod(pmf[x] for x in counts)
            q = np.asarray(counts, dtype=float) / r
            within = np.asarray(counts, dtype=float) * (r - np.asarray(counts, dtype=float)) / (r * (r - 1))
            msw = float(np.mean(within))
            s2 = float(np.var(q, ddof=1))
            raw_between = s2 - msw / r
            outcomes.append((probability, msw, s2, raw_between))
        mean_w = sum(p * w for p, w, _, _ in outcomes)
        mean_s2 = sum(p * s for p, _, s, _ in outcomes)
        mean_raw = sum(p * z for p, _, _, z in outcomes)
        var_w = sum(p * (w - mean_w) ** 2 for p, w, _, _ in outcomes)
        var_s2 = sum(p * (s - mean_s2) ** 2 for p, _, s, _ in outcomes)
        cov_ws2 = sum(p * (w - mean_w) * (s - mean_s2) for p, w, s, _ in outcomes)
        var_raw = sum(p * (z - mean_raw) ** 2 for p, _, _, z in outcomes)
        self.assertAlmostEqual(result.expected_within_estimator, mean_w, places=13)
        self.assertAlmostEqual(result.expected_observed_world_variance, mean_s2, places=13)
        self.assertAlmostEqual(result.expected_raw_between_estimator, mean_raw, places=13)
        self.assertAlmostEqual(result.variance_within_estimator, var_w, places=13)
        self.assertAlmostEqual(result.variance_observed_world_variance_estimator, var_s2, places=13)
        self.assertAlmostEqual(result.covariance_within_observed_world_variance, cov_ws2, places=13)
        self.assertAlmostEqual(result.variance_raw_between_estimator, var_raw, places=13)

    def test_asymmetric_beta_parameters_are_supported(self):
        result = beta_binomial_f5_reference(alpha=0.5, beta=3.0, m=7, r=4)
        self.assertGreater(result.true_within, 0.0)
        self.assertGreater(result.true_between, 0.0)
        self.assertGreater(result.true_mcse, 0.0)

    def test_invalid_parameters_fail_closed(self):
        for args in (
            {"alpha": 0, "beta": 2, "m": 10, "r": 5},
            {"alpha": 2, "beta": float("nan"), "m": 10, "r": 5},
            {"alpha": 2, "beta": 2, "m": 1, "r": 5},
            {"alpha": 2, "beta": 2, "m": 10, "r": 1},
        ):
            with self.subTest(args=args), self.assertRaises(BetaBinomialOracleError):
                beta_binomial_f5_reference(**args)


if __name__ == "__main__":
    unittest.main()
