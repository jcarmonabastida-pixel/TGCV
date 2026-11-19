from __future__ import annotations

import unittest

from c10s_nested_mr_comparative_inference_engine import (
    ComparativeEngineError,
    TruthTargets,
    adjudicate_matched_datasets,
    compare_dataset,
)


class ComparativeInferenceEngineTests(unittest.TestCase):
    def test_f1_routes_only_to_f1_pivotal_candidate(self):
        rows = (
            (0.0, 1.0, 2.0, 1.0),
            (1.0, 2.0, 3.0, 2.0),
            (2.0, 3.0, 4.0, 3.0),
            (3.0, 4.0, 5.0, 4.0),
        )
        result = compare_dataset(
            rows, family="F1", target_m=20, target_r=8,
        )
        self.assertEqual(result.family, "F1")
        self.assertEqual(len(result.candidates), 1)
        self.assertEqual(result.candidates[0].method_id, "C1_F1_EXACT_PIVOTAL_1.0")
        self.assertIn("C2", result.unavailable_methods)
        self.assertIn(("independent_oracle_reconciliation", "PASS_FORMULA_AGREEMENT"), result.candidates[0].diagnostics)

    def test_f5_requires_explicit_replicate_count_and_seed(self):
        rows = ((0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 1, 0, 1, 0),
                (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1),
                (0, 0, 1, 1, 1), (0, 1, 1, 1, 1), (0, 0, 0, 1, 1),
                (1, 0, 1, 1, 1))
        with self.assertRaisesRegex(ComparativeEngineError, "EXPLICIT_BOOTSTRAP"):
            compare_dataset(rows, family="F5", target_m=10, target_r=5)

    def test_f5_routes_to_fitted_candidate_with_seeded_provenance(self):
        rows = ((0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 1, 0, 1, 0),
                (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1),
                (0, 0, 1, 1, 1), (0, 1, 1, 1, 1), (0, 0, 0, 1, 1),
                (1, 0, 1, 1, 1))
        result = compare_dataset(
            rows, family="F5", target_m=10, target_r=5,
            bootstrap_replicates=60, bootstrap_seed=20261119,
        )
        self.assertEqual(result.family, "F5")
        self.assertEqual(len(result.candidates), 1)
        self.assertEqual(result.candidates[0].method_id, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0")
        self.assertIn(("bootstrap_seed", "20261119"), result.candidates[0].comparison.provenance)

    def test_adjudication_exposes_conditional_and_unconditional_coverage(self):
        rows = (
            (0.0, 1.0, 2.0, 1.0),
            (1.0, 2.0, 3.0, 2.0),
            (2.0, 3.0, 4.0, 3.0),
            (3.0, 4.0, 5.0, 4.0),
        )
        record = compare_dataset(rows, family="F1", target_m=20, target_r=8)
        truth = TruthTargets(within=1.25, between=0.5, mcse=0.1)
        metrics = adjudicate_matched_datasets((record,), (truth,))
        c1_within = next(x for x in metrics if x.method_id.startswith("C1_") and x.target == "within")
        self.assertEqual(c1_within.n_datasets, 1)
        self.assertEqual(c1_within.interval_emission_rate, 1.0)
        self.assertIn(c1_within.conditional_coverage, (0.0, 1.0))
        self.assertEqual(c1_within.unconditional_cover_rate, c1_within.conditional_coverage)
        self.assertIsNotNone(c1_within.coverage_mcse)
        self.assertIsNotNone(c1_within.coverage_wilson_95)
        self.assertLessEqual(c1_within.coverage_wilson_95[0], c1_within.coverage_wilson_95[1])

    def test_adjudication_counts_abstentions_and_rejects_unpaired_data(self):
        rows = (
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
            (0.0, 1.0, 0.0, 1.0),
        )
        record = compare_dataset(rows, family="F1", target_m=10, target_r=5)
        metrics = adjudicate_matched_datasets(
            (record,), (TruthTargets(within=0.25, between=0.0, mcse=0.1),)
        )
        c1_mcse = next(x for x in metrics if x.method_id.startswith("C1_") and x.target == "mcse")
        self.assertEqual(c1_mcse.interval_emission_rate, 0.0)
        self.assertEqual(c1_mcse.abstention_count, 1)
        self.assertIn(("EMPTY_FEASIBLE_JOINT_CONFIDENCE_SET", 1), c1_mcse.abstention_reasons)
        with self.assertRaises(ComparativeEngineError):
            adjudicate_matched_datasets((record,), ())
        with self.assertRaises(ComparativeEngineError):
            adjudicate_matched_datasets(
                (record,), (TruthTargets(within=-1.0, between=0.0, mcse=0.1),)
            )

    def test_rejects_unsupported_family(self):
        with self.assertRaises(ComparativeEngineError):
            compare_dataset(((0, 1), (1, 0)), family="F3", target_m=5, target_r=5)


if __name__ == "__main__":
    unittest.main()
