from __future__ import annotations

import unittest
from types import SimpleNamespace

from theta_a_nested_mc_precision import (
    NestedPrecisionError,
    analyze_nested_precision,
)


class NestedPrecisionTests(unittest.TestCase):
    def _summary(self, rows, metric="identification_rate"):
        contributions = tuple(
            (f"outer-{index:06d}", sum(row) / len(row))
            for index, row in enumerate(rows)
        )
        return SimpleNamespace(
            metric=metric,
            mean=sum(value for _, value in contributions) / len(contributions),
            outer_world_contributions=contributions,
        )

    def test_balanced_components_and_legacy_mcse_reconcile(self):
        rows = ((0.0, 2.0), (2.0, 4.0), (4.0, 6.0))
        result = analyze_nested_precision(
            metric="identification_rate",
            replicate_contributions=rows,
            summary_metric=self._summary(rows),
            outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
            projections=((3, 2), (6, 4)),
            bootstrap_replicates=500,
            bootstrap_seed=19,
        )
        self.assertAlmostEqual(result.within_ms, 2.0)
        self.assertAlmostEqual(result.between_raw, 3.0)
        self.assertAlmostEqual(result.observed_world_mean_variance, 4.0)
        self.assertAlmostEqual(result.observed_mcse, (4.0 / 3.0) ** 0.5)
        self.assertGreater(result.valid_bootstrap_replicates, 0)
        self.assertLess(result.valid_bootstrap_replicates, 500)

    def test_between_raw_is_preserved_when_negative(self):
        rows = ((0.0, 2.0), (0.0, 2.0), (0.0, 2.0))
        result = analyze_nested_precision(
            metric="identification_rate",
            replicate_contributions=rows,
            summary_metric=self._summary(rows),
            outer_world_sampling_mode="UNVERIFIED",
            projections=((3, 2),),
            bootstrap_replicates=500,
        )
        self.assertAlmostEqual(result.within_ms, 2.0)
        self.assertLess(result.between_raw, 0.0)
        self.assertEqual(result.status, "DESCRIPTIVE_ONLY")
        self.assertIsNone(result.observed_mcse)

    def test_zero_within_component_is_finite_and_degenerate(self):
        rows = ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0))
        result = analyze_nested_precision(
            metric="identification_rate",
            replicate_contributions=rows,
            summary_metric=self._summary(rows),
            outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
            projections=((3, 2),),
            bootstrap_replicates=500,
        )
        self.assertEqual(result.within_ms, 0.0)
        self.assertAlmostEqual(result.between_raw, 1.0)

    def test_rejects_incomplete_or_unbalanced_r(self):
        rows = ((0.0, 1.0), (1.0,))
        with self.assertRaises(NestedPrecisionError):
            analyze_nested_precision(
                metric="identification_rate",
                replicate_contributions=rows,
                summary_metric=self._summary(((0.0, 1.0), (1.0, 1.0))),
                outer_world_sampling_mode="UNVERIFIED",
                projections=((2, 2),),
            )

    def test_rejects_nonfinite_values(self):
        rows = ((0.0, float("nan")), (1.0, 1.0))
        with self.assertRaises(NestedPrecisionError):
            analyze_nested_precision(
                metric="identification_rate",
                replicate_contributions=rows,
                summary_metric=self._summary(((0.0, 1.0), (1.0, 1.0))),
                outer_world_sampling_mode="UNVERIFIED",
                projections=((2, 2),),
            )

    def test_rejects_contributions_that_do_not_reconcile(self):
        rows = ((0.0, 2.0), (2.0, 4.0))
        summary = self._summary(((0.0, 0.0), (2.0, 2.0)))
        with self.assertRaises(NestedPrecisionError):
            analyze_nested_precision(
                metric="identification_rate",
                replicate_contributions=rows,
                summary_metric=summary,
                outer_world_sampling_mode="UNVERIFIED",
                projections=((2, 2),),
            )

    def test_bootstrap_is_reproducible_for_explicit_seed(self):
        rows = ((0.0, 2.0), (2.0, 4.0), (4.0, 6.0))
        kwargs = dict(
            metric="identification_rate",
            replicate_contributions=rows,
            summary_metric=self._summary(rows),
            outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
            projections=((3, 2),),
            bootstrap_replicates=500,
            bootstrap_seed=123,
        )
        self.assertEqual(analyze_nested_precision(**kwargs), analyze_nested_precision(**kwargs))


    def test_two_outer_worlds_abstain_from_projection(self):
        rows = ((0.0, 2.0), (2.0, 4.0))
        result = analyze_nested_precision(
            metric="identification_rate",
            replicate_contributions=rows,
            summary_metric=self._summary(rows),
            outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
            projections=((2, 2),),
            bootstrap_replicates=500,
            bootstrap_seed=4,
        )
        self.assertEqual(result.status, "INSUFFICIENT_OUTER_SUPPORT")
        self.assertEqual(result.projections[0][-1], "INSUFFICIENT_OUTER_SUPPORT")
        self.assertIsNone(result.projections[0][2])

    def test_rmse_uses_mse_contributions_and_legacy_delta_mcse(self):
        rows = ((0.01, 0.09), (0.04, 0.16), (0.09, 0.25))
        world_mse = tuple(sum(row) / len(row) for row in rows)
        summary = SimpleNamespace(
            metric="point_rmse",
            mean=(sum(world_mse) / len(world_mse)) ** 0.5,
            mcse=0.0123,
            outer_world_contributions=tuple(
                (f"outer-{index:06d}", value)
                for index, value in enumerate(world_mse)
            ),
        )
        result = analyze_nested_precision(
            metric="point_rmse",
            replicate_contributions=rows,
            summary_metric=summary,
            outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
            projections=((3, 2),),
            bootstrap_replicates=500,
            bootstrap_seed=8,
        )
        self.assertAlmostEqual(result.observed_mcse, 0.0123)
        self.assertAlmostEqual(result.between_raw + result.within_ms / 2,
                               result.observed_world_mean_variance)


if __name__ == "__main__":
    unittest.main()
