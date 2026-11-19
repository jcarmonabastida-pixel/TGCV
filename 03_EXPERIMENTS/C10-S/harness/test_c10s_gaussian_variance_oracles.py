from __future__ import annotations

import math
import unittest

from c10s_gaussian_variance_oracles import (
    GaussianOracleError,
    gaussian_constrained_mle,
    gaussian_f1_reference,
    gaussian_mcse_profile_lr,
    gaussian_profile_loglik_mcse,
)


class GaussianVarianceOracleTests(unittest.TestCase):
    def test_f1_exact_and_joint_pivot_intervals_are_ordered(self):
        result = gaussian_f1_reference(
            m=10, r=5, msw=1.0, world_mean_variance=1.2,
        )
        self.assertEqual(result.within_df, 40)
        self.assertEqual(result.between_df, 9)
        self.assertLess(result.within_interval[0], result.within_interval[1])
        self.assertLess(result.tau_interval[0], result.tau_interval[1])
        self.assertLess(
            result.between_raw_conservative_interval[0],
            result.between_raw_conservative_interval[1],
        )

    def test_between_interval_is_not_silently_truncated(self):
        result = gaussian_f1_reference(
            m=10, r=5, msw=1.0, world_mean_variance=0.01,
        )
        self.assertLess(result.between_raw_conservative_interval[0], 0.0)

    def test_constrained_mle_respects_zero_between_boundary(self):
        within, between, loglik = gaussian_constrained_mle(
            m=10, r=5, msw=1.0, world_mean_variance=0.01,
        )
        self.assertGreater(within, 0.0)
        self.assertEqual(between, 0.0)
        self.assertTrue(math.isfinite(loglik))

    def test_interior_mle_matches_anova_components(self):
        within, between, loglik = gaussian_constrained_mle(
            m=10, r=5, msw=1.0, world_mean_variance=1.2,
        )
        self.assertAlmostEqual(within, 1.0)
        self.assertAlmostEqual(between, 1.0)
        self.assertTrue(math.isfinite(loglik))

    def test_profile_mcse_and_lr_are_finite_at_positive_target(self):
        lr = gaussian_mcse_profile_lr(
            m=10, r=5, msw=1.0, world_mean_variance=1.2,
            target_m=10, target_r=5, mcse=math.sqrt(1.2 / 10),
        )
        self.assertTrue(math.isfinite(lr))
        self.assertGreaterEqual(lr, 0.0)

    def test_profile_mcse_rejects_invalid_target_support(self):
        with self.assertRaises(GaussianOracleError):
            gaussian_profile_loglik_mcse(
                m=10, r=5, msw=1.0, world_mean_variance=1.2,
                target_m=1, target_r=5, mcse=0.1,
            )

    def test_invalid_component_statistics_fail_closed(self):
        with self.assertRaises(GaussianOracleError):
            gaussian_f1_reference(
                m=2, r=5, msw=1.0, world_mean_variance=1.2,
            )


if __name__ == "__main__":
    unittest.main()
