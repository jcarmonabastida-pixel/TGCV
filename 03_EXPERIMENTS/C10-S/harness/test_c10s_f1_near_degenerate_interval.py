"""Deterministic near-degenerate F1 interval-path fixtures.

These tests exercise realizable nested rows close to a repeated nuisance-score
root. They are software-contract tests, not calibration or coverage evidence.
"""
from __future__ import annotations

import math
import unittest

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_profile_between_confidence_set,
    f1_score_polynomial_diagnostic,
)


def _repeated_root_rows():
    # M=R=4, tau=1 gives P(s)=-0.9375(s-1)^2(s-4.72).
    ssw = 4.425
    mean_variance = 17.03125
    offset = math.sqrt(3.0 * mean_variance / 4.0)
    pattern = (-1.5, -0.5, 0.5, 1.5)
    scale = math.sqrt(ssw / (4.0 * sum(x*x for x in pattern)))
    means = (-offset, -offset, offset, offset)
    return tuple(
        tuple(float(mean + scale * d) for d in pattern)
        for mean in means
    )


def _perturb_within_deviations(rows, multiplier):
    means = tuple(sum(row) / len(row) for row in rows)
    return tuple(
        tuple(mean + multiplier * (value - mean)
              for value in row)
        for row, mean in zip(rows, means)
    )


class F1NearDegenerateIntervalTests(unittest.TestCase):
    def test_realizable_near_double_root_is_resolved_as_two_close_positive_roots(self):
        rows = _perturb_within_deviations(_repeated_root_rows(), 1.0 - 5e-6)
        diagnostic = f1_score_polynomial_diagnostic(
            rows, between_variance=1.0,
        )
        self.assertEqual(diagnostic.status, "POLYNOMIAL_ROOTS_ISOLATED")
        self.assertEqual(diagnostic.critical_point_solver_status, "RESOLVED")
        close_roots = sorted(
            root for root in diagnostic.positive_roots
            if 0.99 < root < 1.01
        )
        self.assertEqual(len(close_roots), 2)
        self.assertLess(close_roots[1] - close_roots[0], 1e-3)
        self.assertGreater(close_roots[1], close_roots[0])

    def test_near_double_root_rows_reach_interval_boundary_or_typed_abstention(self):
        rows = _perturb_within_deviations(_repeated_root_rows(), 1.0 - 5e-6)
        try:
            result = f1_profile_between_confidence_set(
                rows, family="F1",
                likelihood_ratio_cutoff=3.841458820694124,
            )
        except F1ProfileError as exc:
            self.assertIn("PROFILE_", str(exc))
        else:
            self.assertEqual(result.status, "PROFILE_LR_INTERVAL_ROOT_SOLVED")
            low, high = result.confidence_components[0]
            self.assertTrue(math.isfinite(low) and math.isfinite(high))
            self.assertGreaterEqual(low, 0.0)
            self.assertGreater(high, low)
            self.assertLessEqual(low, result.mle_between_variance)
            self.assertGreaterEqual(high, result.mle_between_variance)


if __name__ == "__main__":
    unittest.main()
