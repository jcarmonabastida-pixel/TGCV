from __future__ import annotations

from dataclasses import replace
import unittest

from c10s_nested_mr_comparative_inference_engine import (
    C0_METHOD_ID,
    ComparativeEngineError,
    TruthTargets,
    adjudicate_matched_datasets,
    compare_dataset,
)


def f1_rows():
    return (
        (-2.0, -1.0, 0.0, 1.0),
        (-1.0, 0.0, 1.0, 2.0),
        (0.0, 1.0, 2.0, 3.0),
        (1.0, 2.0, 3.0, 4.0),
        (2.0, 3.0, 4.0, 5.0),
        (3.0, 4.0, 5.0, 6.0),
    )


def f5_rows():
    return (
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


class ComparativeInferenceEngineTests(unittest.TestCase):
    def _f1(self, dataset_id="F1-DATA-001"):
        return compare_dataset(
            f1_rows(), dataset_id=dataset_id, family="F1",
            target_m=20, target_r=8,
            baseline_bootstrap_replicates=100, baseline_bootstrap_seed=19,
        )

    def _f5(self, dataset_id="F5-DATA-001"):
        return compare_dataset(
            f5_rows(), dataset_id=dataset_id, family="F5",
            target_m=10, target_r=5,
            baseline_bootstrap_replicates=100, baseline_bootstrap_seed=23,
            bootstrap_replicates=60, bootstrap_seed=20261119,
        )

    def test_f1_routes_to_c1_and_preserves_frozen_c0_interval_baseline(self):
        result = self._f1()
        self.assertEqual(result.family, "F1")
        self.assertEqual(result.dataset_id, "F1-DATA-001")
        self.assertEqual(result.baseline.method_id, C0_METHOD_ID)
        self.assertIsNotNone(result.baseline.within_interval)
        self.assertIsNotNone(result.baseline.between_interval)
        self.assertIn(("protocol_version", "002"), result.baseline.provenance)
        self.assertIn(("common_estimand_reconciliation", "PASS_V002_POINT_TARGETS"), result.baseline.provenance)
        self.assertIn(("bootstrap_law", "frozen_v002_two_stage_outer_cluster_then_inner_R"), result.baseline.provenance)
        self.assertEqual(len(result.candidates), 1)
        self.assertEqual(result.candidates[0].method_id, "C1_F1_EXACT_PIVOTAL_1.0")
        self.assertIn(("independent_oracle_reconciliation", "PASS_FORMULA_AGREEMENT"), result.candidates[0].diagnostics)

    def test_f1_requires_explicit_c0_seed_and_replicates(self):
        with self.assertRaises(TypeError):
            compare_dataset(
                f1_rows(), dataset_id="F1-DATA-001", family="F1",
                target_m=20, target_r=8,
                baseline_bootstrap_replicates=100,
            )

    def test_f5_requires_explicit_candidate_bootstrap_and_seed(self):
        with self.assertRaisesRegex(ComparativeEngineError, "EXPLICIT_C5"):
            compare_dataset(
                f5_rows(), dataset_id="F5-DATA-001", family="F5",
                target_m=10, target_r=5,
                baseline_bootstrap_replicates=100, baseline_bootstrap_seed=23,
            )

    def test_f5_routes_to_fitted_candidate_but_abstains_on_mcse_joint_interval(self):
        result = self._f5()
        self.assertEqual(result.family, "F5")
        self.assertEqual(result.baseline.method_id, C0_METHOD_ID)
        candidate = result.candidates[0]
        self.assertEqual(candidate.method_id, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0")
        self.assertIn(("bootstrap_seed", "20261119"), candidate.comparison.provenance)
        self.assertIsNotNone(candidate.comparison.within_interval)
        self.assertIsNotNone(candidate.comparison.between_interval)
        self.assertIsNone(candidate.comparison.mcse_interval)
        self.assertEqual(
            candidate.comparison.abstention_reason,
            "F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED",
        )
        self.assertIn(("mcse_interval_status", "NOT_IMPLEMENTED_BOUNDARY_AWARE_JOINT_INFERENCE"), candidate.diagnostics)
        self.assertTrue(any(
            key == "mcse_profile_optimizer_adjudication"
            for key, _ in candidate.diagnostics
        ))
        self.assertTrue(any(
            key == "mcse_profile_optimizer_loglik_tolerance"
            for key, _ in candidate.diagnostics
        ))

    def test_adjudication_reports_all_denominators_and_wilson_limits(self):
        record = self._f1()
        truth = TruthTargets(
            dataset_id=record.dataset_id, within=1.0, between=1.0, mcse=0.25,
        )
        metrics = adjudicate_matched_datasets((record,), (truth,))
        c0_within = next(x for x in metrics if x.method_id == C0_METHOD_ID and x.target == "within")
        c1_within = next(x for x in metrics if x.method_id.startswith("C1_") and x.target == "within")
        self.assertEqual(c0_within.n_datasets, 1)
        self.assertEqual(c0_within.interval_emission_rate, 1.0)
        self.assertIsNotNone(c0_within.interval_emission_wilson_95)
        self.assertIsNotNone(c0_within.coverage_wilson_95)
        self.assertIsNotNone(c0_within.unconditional_cover_wilson_95)
        self.assertIsNotNone(c0_within.point_emission_wilson_95)
        self.assertEqual(c0_within.unconditional_cover_rate, c0_within.conditional_coverage)
        self.assertEqual(c1_within.interval_emission_rate, 1.0)

    def test_adjudication_rejects_dataset_truth_mismatch_and_duplicate_ids(self):
        record = self._f1()
        with self.assertRaisesRegex(ComparativeEngineError, "ID_MISMATCH"):
            adjudicate_matched_datasets(
                (record,),
                (TruthTargets("OTHER-ID", 1.0, 1.0, 0.2),),
            )
        with self.assertRaisesRegex(ComparativeEngineError, "DUPLICATE"):
            adjudicate_matched_datasets(
                (record, record),
                (TruthTargets(record.dataset_id, 1.0, 1.0, 0.2),
                 TruthTargets(record.dataset_id, 1.0, 1.0, 0.2)),
            )

    def test_adjudication_rejects_incomplete_method_roster(self):
        record = self._f1()
        malformed = replace(record, candidates=())
        with self.assertRaisesRegex(ComparativeEngineError, "ROSTER"):
            adjudicate_matched_datasets(
                (malformed,),
                (TruthTargets(record.dataset_id, 1.0, 1.0, 0.2),),
            )

    def test_adjudication_rejects_mixed_families_and_target_designs(self):
        f1 = self._f1()
        f5 = self._f5()
        with self.assertRaises(ComparativeEngineError):
            adjudicate_matched_datasets(
                (f1, f5),
                (TruthTargets(f1.dataset_id, 1.0, 1.0, 0.2),
                 TruthTargets(f5.dataset_id, 0.2, 0.05, 0.1)),
            )
        other_target = replace(f1, dataset_id="F1-DATA-002", target_m=30)
        with self.assertRaisesRegex(ComparativeEngineError, "DESIGNS"):
            adjudicate_matched_datasets(
                (f1, other_target),
                (TruthTargets(f1.dataset_id, 1.0, 1.0, 0.2),
                 TruthTargets(other_target.dataset_id, 1.0, 1.0, 0.2)),
            )

    def test_rejects_unsupported_family_and_invalid_truth(self):
        with self.assertRaises(ComparativeEngineError):
            compare_dataset(
                ((0, 1), (1, 0)), dataset_id="X", family="F3",
                target_m=5, target_r=5,
                baseline_bootstrap_replicates=100, baseline_bootstrap_seed=1,
            )
        record = self._f1()
        with self.assertRaisesRegex(ComparativeEngineError, "NONNEGATIVE"):
            adjudicate_matched_datasets(
                (record,),
                (TruthTargets(record.dataset_id, -1.0, 1.0, 0.2),),
            )


if __name__ == "__main__":
    unittest.main()
