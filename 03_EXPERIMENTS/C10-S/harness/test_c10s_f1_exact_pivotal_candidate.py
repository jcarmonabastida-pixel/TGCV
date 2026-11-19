from __future__ import annotations

import math
import unittest

from c10s_f1_exact_pivotal_candidate import (
    F1PivotalError,
    f1_exact_pivotal_result,
)


class F1ExactPivotalCandidateTests(unittest.TestCase):
    def test_returns_three_intervals_and_preserves_raw_estimate(self):
        rows = (
            (0.0, 1.0, 2.0, 1.0),
            (1.0, 2.0, 3.0, 2.0),
            (2.0, 3.0, 4.0, 3.0),
            (3.0, 4.0, 5.0, 4.0),
        )
        result = f1_exact_pivotal_result(
            rows, target_m=20, target_r=8,
        )
        self.assertEqual(result.method_id, "C1_F1_EXACT_PIVOTAL_1.0")
        self.assertIsNotNone(result.within_interval)
        self.assertIsNotNone(result.between_interval)
        self.assertIsNotNone(result.mcse_interval)
        self.assertLess(result.within_interval[0], result.within_interval[1])
        self.assertLess(result.between_interval[0], result.between_interval[1])
        self.assertLessEqual(result.mcse_interval[0], result.mcse_interval[1])
        self.assertIn(("model_scope", "F1_BALANCED_GAUSSIAN_RANDOM_INTERCEPT"), result.provenance)

    def test_negative_raw_between_interval_endpoint_is_not_clipped(self):
        rows = (
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
        )
        result = f1_exact_pivotal_result(rows, target_m=10, target_r=5)
        self.assertLess(result.between_interval[0], 0.0)
        self.assertTrue(math.isfinite(result.between_interval[0]))

    def test_rejects_non_f1_family(self):
        with self.assertRaises(F1PivotalError):
            f1_exact_pivotal_result(
                ((0.0, 1.0), (1.0, 2.0), (2.0, 3.0)),
                target_m=10, target_r=5, family="F5",
            )

    def test_rejects_too_few_outer_worlds(self):
        with self.assertRaises(F1PivotalError):
            f1_exact_pivotal_result(
                ((0.0, 1.0), (1.0, 2.0)),
                target_m=10, target_r=5,
            )

    def test_rejects_invalid_target_design(self):
        with self.assertRaises(F1PivotalError):
            f1_exact_pivotal_result(
                ((0.0, 1.0), (1.0, 2.0), (2.0, 3.0)),
                target_m=1, target_r=5,
            )


if __name__ == "__main__":
    unittest.main()
