from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np

from c10s_fitted_beta_binomial_bootstrap import (
    BetaBinomialFitError,
    fit_beta_binomial_counts,
    fitted_beta_binomial_parametric_bootstrap,
    _vectorized_bernoulli_bootstrap_components,
)
from c10s_variance_comparison_interface import observed_nested_mr_result


class FittedBetaBinomialBootstrapTests(unittest.TestCase):
    def test_vectorized_bootstrap_kernel_matches_scalar_nested_estimands(self):
        rng = np.random.Generator(np.random.PCG64(20261121))
        counts_star = rng.integers(0, 6, size=(257, 10), endpoint=False)
        within, between, valid_mcse = _vectorized_bernoulli_bootstrap_components(
            counts_star, 5, 10, 5,
        )
        scalar_within = []
        scalar_between = []
        scalar_valid = 0
        for counts in counts_star:
            rows = tuple(
                tuple([1.0] * int(count) + [0.0] * (5 - int(count)))
                for count in counts
            )
            result = observed_nested_mr_result(
                rows, target_m=10, target_r=5,
            )
            scalar_within.append(result.within_estimate)
            scalar_between.append(result.between_estimate_raw)
            scalar_valid += int(result.mcse_estimate is not None)
        np.testing.assert_allclose(within, scalar_within, rtol=1e-13, atol=1e-15)
        np.testing.assert_allclose(between, scalar_between, rtol=1e-13, atol=1e-15)
        self.assertEqual(valid_mcse, scalar_valid)

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
        self.assertIn(first.optimizer_audit.status, (
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
        self.assertEqual(first.comparison.method_id, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.1")

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



    def test_global_mle_certificate_gate_accepts_optimizer_inside_certified_box(self):
        import os
        from unittest.mock import patch

        rows = tuple(
            tuple([1.0] * count + [0.0] * (5 - count))
            for count in (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
        )
        counts = [sum(row) for row in rows]
        from c10s_fitted_beta_binomial_bootstrap import fit_beta_binomial_counts
        fit = fit_beta_binomial_counts(counts, 5)
        fitted_t = fit.concentration / (1.0 + fit.concentration)
        fake = {
            "status": "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
            "winner": {
                "kind": "INTERIOR_STATIONARY_ROOT",
                "parameter_box": (
                    (fit.mean_probability - 1e-4, fit.mean_probability + 1e-4),
                    (fitted_t - 1e-4, fitted_t + 1e-4),
                ),
            },
            "globality_basis": "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS",
            "census": {"input_provenance": {"source_revision": "b" * 40}},
        }
        with patch.dict(os.environ, {"GITHUB_SHA": "b" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=fake,
        ):
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=10, target_r=5, bootstrap_replicates=20,
                bootstrap_seed=12345, require_global_mle_certificate=True,
            )
        self.assertEqual(result.global_mle_certificate["status"], "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED")
        self.assertEqual(result.global_mle_certificate["canonical_fit_rule"], "RATIONAL_MIDPOINT_OF_EXACT_KRAWCZYK_ROOT_BOX")
        self.assertEqual(dict(result.comparison.provenance)["global_mle_certificate_status"], "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED")

    def test_global_mle_certificate_unresolved_forces_typed_abstention(self):
        import os
        from unittest.mock import patch

        rows = tuple(
            tuple([1.0] * count + [0.0] * (5 - count))
            for count in (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
        )
        fake = {"status": "NUMERICAL_INTERVAL_CERTIFICATE_UNRESOLVED", "census": {}}
        with patch.dict(os.environ, {"GITHUB_SHA": "c" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=fake,
        ):
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=10, target_r=5, bootstrap_replicates=20,
                bootstrap_seed=12345, require_global_mle_certificate=True,
            )
        self.assertIsNone(result.comparison.within_interval)
        self.assertIsNone(result.comparison.between_interval)
        self.assertIn("F5_GLOBAL_MLE_NOT_CERTIFIED", result.comparison.abstention_reason)


    def test_actual_global_certificate_contains_production_fit_on_m10_r5_fixture(self):
        import os
        from collections import Counter
        from unittest.mock import patch
        from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate
        from c10s_fitted_beta_binomial_bootstrap import fit_beta_binomial_counts

        counts = (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
        fit = fit_beta_binomial_counts(counts, 5)
        with patch.dict(os.environ, {"GITHUB_SHA": "f" * 40}):
            certificate = beta_binomial_global_mle_certificate(
                5, Counter(counts), source_revision="f" * 40,
            )
        self.assertEqual(certificate["status"], "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED")
        bounds = certificate["winner"]["parameter_box"]
        fitted_t = fit.concentration / (1.0 + fit.concentration)
        self.assertTrue(float(bounds[0][0]) <= fit.mean_probability <= float(bounds[0][1]))
        self.assertTrue(float(bounds[1][0]) <= fitted_t <= float(bounds[1][1]))


    def test_global_boundary_certificate_precedes_and_overrules_optimizer(self):
        import os
        from unittest.mock import patch

        rows = tuple(
            tuple([1.0] * count + [0.0] * (5 - count))
            for count in (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
        )
        events = []
        boundary = {
            "status": "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
            "winner": {"kind": "BOUNDARY_SUPREMUM"},
            "census": {"input_provenance": {"source_revision": "e" * 40}},
        }
        def certificate(*args, **kwargs):
            events.append("certificate")
            return boundary
        def forbidden_optimizer(*args, **kwargs):
            events.append("optimizer")
            raise AssertionError("optimizer must not run before/against boundary certificate")
        with patch.dict(os.environ, {"GITHUB_SHA": "e" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            side_effect=certificate,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.minimize",
            side_effect=forbidden_optimizer,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.audit_beta_binomial_count_fit",
            side_effect=forbidden_optimizer,
        ):
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=10, target_r=5, bootstrap_replicates=20,
                bootstrap_seed=12345, require_global_mle_certificate=True,
            )
        self.assertEqual(events, ["certificate"])
        self.assertIsNone(result.fit)
        self.assertIn("GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED", result.failure_reason)
        self.assertIsNone(result.comparison.within_interval)

    def test_certified_midpoint_fit_is_independent_of_optimizer_termination(self):
        import os
        from types import SimpleNamespace
        from unittest.mock import patch

        rows = tuple(
            tuple([1.0] * count + [0.0] * (5 - count))
            for count in (0, 1, 2, 4, 5, 3, 1, 4, 2, 3)
        )
        box = ((0.4, 0.4002), (0.6, 0.6002))
        certificate = {
            "status": "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
            "winner": {"kind": "INTERIOR_STATIONARY_ROOT", "parameter_box": box},
            "globality_basis": "EXACT_TEST_CERTIFICATE",
            "census": {"input_provenance": {"source_revision": "f" * 40}},
        }
        failed = SimpleNamespace(
            x=np.asarray([0.1, 0.2]), success=False, message="ABNORMAL_TERMINATION",
            fun=12.5, jac=np.asarray([1e-7, -1e-7]),
        )
        succeeded = SimpleNamespace(
            x=np.asarray([0.3, 0.4]), success=True, message="CONVERGENCE",
            fun=11.5, jac=np.asarray([1e-9, -1e-9]),
        )
        kwargs = dict(
            target_m=10, target_r=5, bootstrap_replicates=50,
            bootstrap_seed=12345, require_global_mle_certificate=True,
        )
        with patch.dict(os.environ, {"GITHUB_SHA": "f" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=certificate,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.audit_beta_binomial_count_fit",
            return_value=None,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.minimize",
            side_effect=[failed, failed, failed],
        ):
            first = fitted_beta_binomial_parametric_bootstrap(rows, **kwargs)
        with patch.dict(os.environ, {"GITHUB_SHA": "f" * 40}), patch(
            "c10s_fitted_beta_binomial_bootstrap.beta_binomial_global_mle_certificate",
            return_value=certificate,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.audit_beta_binomial_count_fit",
            return_value=None,
        ), patch(
            "c10s_fitted_beta_binomial_bootstrap.minimize",
            side_effect=[succeeded, succeeded, succeeded],
        ):
            second = fitted_beta_binomial_parametric_bootstrap(rows, **kwargs)
        self.assertIsNotNone(first.fit)
        self.assertIsNotNone(second.fit)
        self.assertEqual(first.fit.mean_probability, second.fit.mean_probability)
        self.assertEqual(first.fit.concentration, second.fit.concentration)
        self.assertEqual(first.fit.alpha, second.fit.alpha)
        self.assertEqual(first.fit.beta, second.fit.beta)
        self.assertEqual(first.comparison.within_interval, second.comparison.within_interval)
        self.assertEqual(first.comparison.between_interval, second.comparison.between_interval)
        self.assertEqual(first.comparison.provenance, second.comparison.provenance)
        self.assertEqual(
            first.fit.mean_probability,
            float((__import__("fractions").Fraction(0.4) + __import__("fractions").Fraction(0.4002)) / 2),
        )
        self.assertEqual(
            first.production_analytic_reconciliation["production_fit"]["fit_origin"],
            "EXACT_GLOBAL_CERTIFICATE_KRAWCZYK_BOX_MIDPOINT",
        )




if __name__ == "__main__":
    unittest.main()
