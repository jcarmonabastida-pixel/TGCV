import unittest
from dataclasses import replace
from unittest.mock import patch

import numpy as np

from c10s_f5_functional_refit_bootstrap import (
    F5FunctionalFitRecord,
    F5FunctionalBootstrapError,
    beta_binomial_functionals,
    fitted_functional_refit_percentile_bootstrap,
    _fit_count_vector,
)


class F5FunctionalRefitBootstrapTests(unittest.TestCase):
    def test_population_functionals_match_beta22_truth(self):
        within, between = beta_binomial_functionals(0.5, 4.0)
        self.assertAlmostEqual(within, 0.20, places=14)
        self.assertAlmostEqual(between, 0.05, places=14)
        self.assertAlmostEqual(within + between, 0.25, places=14)

    def test_functional_identity_across_parameter_values(self):
        for mean, concentration in ((0.2, 0.5), (0.5, 4.0), (0.8, 20.0)):
            within, between = beta_binomial_functionals(mean, concentration)
            self.assertAlmostEqual(
                within + between, mean * (1.0 - mean), places=14,
            )
            self.assertGreaterEqual(within, 0.0)
            self.assertGreaterEqual(between, 0.0)
            self.assertLessEqual(within, 0.25)
            self.assertLessEqual(between, 0.25)

    def test_invalid_functional_parameters_are_rejected(self):
        for mean, concentration in ((0.0, 4.0), (1.0, 4.0), (0.5, 0.0), (0.5, float("inf"))):
            with self.subTest(mean=mean, concentration=concentration):
                with self.assertRaises(F5FunctionalBootstrapError):
                    beta_binomial_functionals(mean, concentration)

    def test_primary_fit_is_analytic_gradient_multistart_and_retains_audit(self):
        rng = np.random.Generator(np.random.PCG64(2026))
        probabilities = rng.beta(2.0, 2.0, size=30)
        counts = rng.binomial(5, probabilities).astype(int).tolist()
        fit = _fit_count_vector(counts, 5)
        self.assertEqual(fit.status, "PRIMARY_ANALYTIC_INTERIOR_FIT")
        self.assertEqual(len(fit.starts), 3)
        self.assertTrue(np.isfinite(fit.mean_probability))
        self.assertTrue(np.isfinite(fit.concentration))
        self.assertTrue(np.isfinite(fit.score_norm))
        self.assertEqual(len(fit.hessian_eigenvalues), 2)
        self.assertTrue(all(value < 0.0 for value in fit.hessian_eigenvalues))
        self.assertIsInstance(fit.audit_status, str)
        self.assertIsInstance(fit.independent_optimizer_success, bool)

    def test_refit_bootstrap_is_reproducible_and_retains_every_replicate(self):
        rng = np.random.Generator(np.random.PCG64(2026))
        probabilities = rng.beta(2.0, 2.0, size=30)
        counts = rng.binomial(5, probabilities).astype(int).tolist()
        first = fitted_functional_refit_percentile_bootstrap(
            counts, r=5, bootstrap_replicates=20, bootstrap_seed=991827,
        )
        second = fitted_functional_refit_percentile_bootstrap(
            counts, r=5, bootstrap_replicates=20, bootstrap_seed=991827,
        )
        self.assertEqual(first.original_fit.status, "PRIMARY_ANALYTIC_INTERIOR_FIT")
        self.assertEqual(first.status, second.status)
        self.assertEqual(first.replicate_records, second.replicate_records)
        self.assertEqual(first.within_interval, second.within_interval)
        self.assertEqual(first.between_interval, second.between_interval)
        if first.status == "EMITTED":
            self.assertEqual(first.valid_replicates, 20)
            self.assertEqual(first.failed_replicates, 0)
            self.assertIsNotNone(first.within_interval)
            self.assertIsNotNone(first.between_interval)
        else:
            self.assertEqual(first.status, "ABSTAINED_BOOTSTRAP_FIT_FAILURE")
            self.assertEqual(first.valid_replicates + first.failed_replicates, 20)
            self.assertIsNone(first.within_interval)
            self.assertIsNone(first.between_interval)

    def test_any_failed_replicate_abstains_without_complete_case_dropping(self):
        valid = F5FunctionalFitRecord(
            status="PRIMARY_ANALYTIC_INTERIOR_FIT",
            mean_probability=0.5, concentration=4.0,
            within_functional=0.2, between_functional=0.05,
            log_likelihood=-10.0, score_norm=1e-9,
            hessian_eigenvalues=(-2.0, -1.0),
            profile_log_concentration_curvature=-1.0,
            profile_minus_binomial_limit=1.0,
            profile_minus_two_point_limit=None,
            audit_status="INDEPENDENT_OPTIMIZER_UNRESOLVED",
            independent_optimizer_success=False,
            independent_optimizer_message="test diagnostic only",
            independent_log_likelihood=None, independent_score_norm=None,
            starts=({"success": True},), failure_reason=None,
        )
        failed = replace(
            valid, status="NO_ADMISSIBLE_PRIMARY_FIT",
            failure_reason="INJECTED_TEST_FAILURE",
        )
        calls = {"n": 0}

        def fake_fit(counts, r):
            calls["n"] += 1
            if calls["n"] == 1:
                return valid
            if calls["n"] == 8:
                return failed
            return valid

        with patch(
            "c10s_f5_functional_refit_bootstrap._fit_count_vector",
            side_effect=fake_fit,
        ):
            result = fitted_functional_refit_percentile_bootstrap(
                [0, 1, 2, 3, 4, 5, 1, 2, 3, 4], r=5,
                bootstrap_replicates=20, bootstrap_seed=17,
            )
        self.assertEqual(result.status, "ABSTAINED_BOOTSTRAP_FIT_FAILURE")
        self.assertEqual(len(result.replicate_records), 20)
        self.assertEqual(result.failed_replicates, 1)
        self.assertEqual(result.valid_replicates, 19)
        self.assertIsNone(result.within_interval)
        self.assertIsNone(result.between_interval)
        self.assertEqual(result.failure_counts, (("NO_ADMISSIBLE_PRIMARY_FIT", 1),))

    def test_original_fit_failure_abstains_before_bootstrap(self):
        result = fitted_functional_refit_percentile_bootstrap(
            [0] * 10, r=5, bootstrap_replicates=20, bootstrap_seed=23,
        )
        self.assertEqual(result.status, "ABSTAINED_ORIGINAL_FIT")
        self.assertEqual(result.replicate_records, ())
        self.assertIsNone(result.within_interval)
        self.assertIsNone(result.between_interval)

    def test_bootstrap_input_contract(self):
        with self.assertRaises(F5FunctionalBootstrapError):
            fitted_functional_refit_percentile_bootstrap(
                [0, 1, 2], r=1, bootstrap_replicates=20, bootstrap_seed=1,
            )
        with self.assertRaises(F5FunctionalBootstrapError):
            fitted_functional_refit_percentile_bootstrap(
                [0, 1, 2], r=5, bootstrap_replicates=10, bootstrap_seed=1,
            )
        with self.assertRaises(F5FunctionalBootstrapError):
            fitted_functional_refit_percentile_bootstrap(
                [0, 1, 2], r=5, bootstrap_replicates=20, bootstrap_seed=-1,
            )


if __name__ == "__main__":
    unittest.main()
