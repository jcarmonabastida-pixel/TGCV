from __future__ import annotations

import unittest

from c10s_variance_comparison_interface import (
    ComparisonInputError,
    observed_nested_mr_result,
)


class NestedMRComparisonInterfaceTests(unittest.TestCase):
    def test_f1_components_match_balanced_hand_calculation(self):
        rows = (
            (0.0, 2.0, 0.0),
            (1.0, 3.0, 1.0),
            (2.0, 4.0, 2.0),
        )
        result = observed_nested_mr_result(rows, target_m=10, target_r=6)
        self.assertAlmostEqual(result.within_estimate, 4.0 / 3.0)
        self.assertAlmostEqual(result.observed_world_variance, 1.0)
        self.assertAlmostEqual(result.between_estimate_raw, 5.0 / 9.0)
        self.assertIsNotNone(result.mcse_estimate)
        self.assertIsNone(result.abstention_reason)
        self.assertIsNone(result.within_interval)

    def test_negative_raw_between_is_preserved_and_projection_abstains(self):
        rows = (
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
        )
        result = observed_nested_mr_result(rows, target_m=10, target_r=8)
        self.assertAlmostEqual(result.within_estimate, 1.0 / 3.0)
        self.assertAlmostEqual(result.observed_world_variance, 0.0)
        self.assertAlmostEqual(result.between_estimate_raw, -1.0 / 12.0)
        self.assertIsNone(result.mcse_estimate)
        self.assertEqual(result.abstention_reason, "NONPOSITIVE_PROJECTED_VARIANCE")
        self.assertIn("BETWEEN_NEGATIVE_RAW", result.boundary_flags)

    def test_input_is_not_mutated(self):
        rows = [[0.0, 1.0], [1.0, 2.0], [2.0, 3.0]]
        before = [row[:] for row in rows]
        observed_nested_mr_result(rows, target_m=5, target_r=3)
        self.assertEqual(rows, before)

    def test_zero_components_are_typed(self):
        result = observed_nested_mr_result(
            ((0.5, 0.5), (0.5, 0.5)), target_m=4, target_r=2,
        )
        self.assertEqual(result.within_estimate, 0.0)
        self.assertEqual(result.between_estimate_raw, 0.0)
        self.assertEqual(result.mcse_estimate, 0.0)
        self.assertIn("WITHIN_ZERO", result.boundary_flags)
        self.assertIn("BETWEEN_ZERO", result.boundary_flags)
        self.assertIn("MCSE_ZERO_DEGENERATE", result.boundary_flags)

    def test_invalid_shapes_and_values_fail_closed(self):
        invalid = (
            ((1.0,), (2.0,)),
            ((1.0, 2.0),),
            ((1.0, 2.0), (3.0,)),
            ((1.0, float("nan")), (2.0, 3.0)),
            ((1.0, True), (2.0, 3.0)),
        )
        for rows in invalid:
            with self.subTest(rows=rows), self.assertRaises(ComparisonInputError):
                observed_nested_mr_result(rows)
        with self.assertRaises(ComparisonInputError):
            observed_nested_mr_result(((1.0, 2.0), (2.0, 3.0)), target_m=3)
        with self.assertRaises(ComparisonInputError):
            observed_nested_mr_result(((1.0, 2.0), (2.0, 3.0)), target_m=1, target_r=2)


if __name__ == "__main__":
    unittest.main()
