"""Source-contract tests for the M1 challenger path; not executed by authoring."""
from dataclasses import replace
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from c10s_nested_mr_comparative_inference_engine import (
    C0_METHOD_ID, CandidateOutput, DatasetComparison, TruthTargets,
)
from c10s_variance_comparison_interface import observed_nested_mr_result
import c10s_nested_mr_comparative_inference_engine_1_2_m1 as m


ROWS = ((0, 1), (1, 1))
C5 = m.C5_METHOD_ID
M1 = m.M1_METHOD_ID


def fake_m1(status="EMITTED", within=(0.1, 0.4), between=(0.0, 0.2),
            point_within=0.25, point_between=0.05, failed=0):
    original_admissible = status != "ABSTAINED_ORIGINAL_FIT"
    return SimpleNamespace(
        method_id=M1, status=status, fit_contract_id=m.M1_FIT_CONTRACT_ID,
        target_m=2, target_r=2,
        original_fit=SimpleNamespace(
            status="PRIMARY_ANALYTIC_INTERIOR_FIT" if original_admissible else "NO_ADMISSIBLE_PRIMARY_FIT",
            failure_reason=None if original_admissible else "NO_FINITE_SUCCESSFUL_ANALYTIC_GRADIENT_START",
        ),
        bootstrap_replicates=20, valid_replicates=(20-failed) if original_admissible else 0,
        failed_replicates=failed if original_admissible else 0,
        replicate_records=tuple({} for _ in range(20)) if original_admissible else (),
        point_within=point_within if original_admissible else None,
        point_between=point_between if original_admissible else None,
        within_interval=within if status == "EMITTED" else None,
        between_interval=between if status == "EMITTED" else None,
        global_mle_certificate_used=False, failure_counts=(("FIT_FAIL", failed),) if failed else (),
    )


def record(dataset_id="d1", m1_status="EMITTED", interval=(0.1, 0.4)):
    common = observed_nested_mr_result(ROWS, target_m=2, target_r=2)
    baseline = replace(common, method_id=C0_METHOD_ID,
                       within_interval=(0.0, 1.0), between_interval=(0.0, 1.0),
                       mcse_interval=(0.0, 1.0))
    c5_result = replace(common, method_id=C5,
                        within_interval=(0.0, 0.8), between_interval=(0.0, 0.8),
                        mcse_interval=(0.0, 0.8))
    legacy = DatasetComparison(
        engine_id="C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.1",
        dataset_id=dataset_id, family="F5", input_m=2, input_r=2,
        target_m=2, target_r=2, baseline=baseline,
        candidates=(CandidateOutput(C5, c5_result),), unavailable_methods=("C2", "C3", "C4"),
    )
    result = fake_m1(status=m1_status, within=interval, between=(0.0, 0.2),
                     failed=2 if m1_status != "EMITTED" else 0)
    m1_comparison = replace(
        common, method_id=M1, mcse_estimate=None,
        within_interval=result.within_interval,
        between_interval=result.between_interval,
        mcse_interval=None,
        abstention_reason="M1_MCSE_INTERVAL_NOT_IMPLEMENTED" if m1_status == "EMITTED" else "M1_" + m1_status,
    )
    return m.M1ChallengerDatasetComparison(
        engine_id=m.ENGINE_ID, dataset_id=dataset_id, family="F5",
        input_m=2, input_r=2, target_m=2, target_r=2,
        legacy_record=legacy, m1_comparison=m1_comparison,
        m1_result=result, m1_diagnostics=m._m1_diagnostics(result),
    )


class M1ChallengerContractTests(unittest.TestCase):
    def test_01_exact_three_method_roster(self):
        m._validate_roster(record())

    def test_02_c0_and_c5_legacy_records_are_preserved(self):
        item = record()
        before = item.legacy_record
        m._validate_roster(item)
        self.assertIs(item.legacy_record, before)
        self.assertEqual(item.legacy_record.baseline.method_id, C0_METHOD_ID)
        self.assertEqual(item.legacy_record.candidates[0].method_id, C5)

    def test_03_m1_intervals_are_copied_without_transformation(self):
        item = record(interval=(0.123456789012345, 0.987654321098765))
        self.assertEqual(item.m1_comparison.within_interval,
                         (0.123456789012345, 0.987654321098765))

    def test_04_common_point_fields_remain_raw_between(self):
        item = record()
        common = observed_nested_mr_result(ROWS, target_m=2, target_r=2)
        self.assertEqual(item.m1_comparison.within_estimate, common.within_estimate)
        self.assertEqual(item.m1_comparison.between_estimate_raw, common.between_estimate_raw)

    def test_05_model_points_remain_auxiliary_and_separate(self):
        item = record()
        self.assertEqual(item.m1_result.point_within, 0.25)
        self.assertEqual(item.m1_result.point_between, 0.05)
        self.assertNotEqual(item.m1_result.point_between,
                            item.m1_comparison.between_estimate_raw)
        self.assertEqual(dict(item.m1_diagnostics)["m1_point_between"], "0.050000000000000003")

    def test_06_original_fit_abstention_has_no_interval(self):
        item = record(m1_status="ABSTAINED_ORIGINAL_FIT")
        self.assertIsNone(item.m1_comparison.within_interval)
        self.assertEqual(item.m1_comparison.abstention_reason, "M1_ABSTAINED_ORIGINAL_FIT")
        self.assertEqual(dict(item.m1_diagnostics)["m1_model_point_status"], "UNAVAILABLE_ORIGINAL_FIT")
        self.assertEqual(dict(item.m1_diagnostics)["m1_point_between"], "")

    def test_07_bootstrap_failure_abstains_at_dataset_level(self):
        item = record(m1_status="ABSTAINED_BOOTSTRAP_FIT_FAILURE")
        self.assertIsNone(item.m1_comparison.between_interval)
        self.assertEqual(item.m1_result.failed_replicates, 2)

    def test_08_truth_dataset_id_mismatch_fails_closed(self):
        with self.assertRaises(m.M1ChallengerError):
            m.adjudicate_m1_challenger((record("d1"),),
                                       (TruthTargets("other", 0.2, 0.1, 0.1),))

    def test_09_duplicate_dataset_or_truth_ids_fail_closed(self):
        with self.assertRaises(m.M1ChallengerError):
            m.adjudicate_m1_challenger(
                (record("d1"), record("d1")),
                (TruthTargets("d1", .2, .1, .1), TruthTargets("d2", .2, .1, .1)),
            )

    def test_10_interval_emission_uses_all_datasets(self):
        items = (record("d1"), record("d2", "ABSTAINED_BOOTSTRAP_FIT_FAILURE"))
        truths = (TruthTargets("d1", 0.2, 0.1, 0.1),
                  TruthTargets("d2", 0.2, 0.1, 0.1))
        metrics = m.adjudicate_m1_challenger(items, truths)
        within = next(x for x in metrics if x.method_id == M1 and x.target == "within")
        self.assertEqual(within.n_datasets, 2)
        self.assertEqual(within.interval_emission_rate, 0.5)

    def test_11_conditional_coverage_uses_emitted_intervals(self):
        items = (record("d1"), record("d2", "ABSTAINED_BOOTSTRAP_FIT_FAILURE"))
        truths = (TruthTargets("d1", 0.2, 0.1, 0.1),
                  TruthTargets("d2", 0.2, 0.1, 0.1))
        within = next(x for x in m.adjudicate_m1_challenger(items, truths)
                      if x.method_id == M1 and x.target == "within")
        self.assertEqual(within.conditional_coverage, 1.0)

    def test_12_unconditional_cover_rate_uses_all_datasets(self):
        items = (record("d1"), record("d2", "ABSTAINED_BOOTSTRAP_FIT_FAILURE"))
        truths = (TruthTargets("d1", 0.2, 0.1, 0.1),
                  TruthTargets("d2", 0.2, 0.1, 0.1))
        within = next(x for x in m.adjudicate_m1_challenger(items, truths)
                      if x.method_id == M1 and x.target == "within")
        self.assertEqual(within.unconditional_cover_rate, 0.5)

    def test_13_different_designs_are_not_pooled(self):
        first = record("d1")
        second = record("d2")
        changed_legacy = replace(second.legacy_record, input_m=3)
        changed_m1 = SimpleNamespace(**vars(second.m1_result))
        changed_m1.target_m = 3
        second = replace(second, input_m=3, legacy_record=changed_legacy,
                         m1_result=changed_m1)
        with self.assertRaisesRegex(m.M1ChallengerError, "STRATIFY_DIFFERENT_INPUT_OR_TARGET_DESIGNS"):
            m.adjudicate_m1_challenger(
                (first, second),
                (TruthTargets("d1", .2, .1, .1), TruthTargets("d2", .2, .1, .1)),
            )

    def test_14_seed_arguments_are_passed_to_separate_methods(self):
        item = record()
        with patch.object(m, "compare_legacy_dataset", return_value=item.legacy_record) as legacy, \
             patch.object(m, "fitted_functional_refit_percentile_bootstrap",
                          return_value=item.m1_result) as challenger:
            m.compare_f5_dataset(
                ROWS, dataset_id="d1", target_m=2, target_r=2,
                c0_bootstrap_replicates=100, c0_bootstrap_seed=11,
                c5_bootstrap_replicates=100, c5_bootstrap_seed=22,
                m1_bootstrap_replicates=20, m1_bootstrap_seed=33,
            )
        self.assertEqual(legacy.call_args.kwargs["bootstrap_seed"], 22)
        self.assertFalse(legacy.call_args.kwargs["include_profile_diagnostics"])
        self.assertEqual(challenger.call_args.kwargs["bootstrap_seed"], 33)
        with self.assertRaises(m.M1ChallengerError):
            m.compare_f5_dataset(
                ROWS, dataset_id="d1", target_m=2, target_r=2,
                c0_bootstrap_replicates=100, c0_bootstrap_seed=11,
                c5_bootstrap_replicates=100, c5_bootstrap_seed=11,
                m1_bootstrap_replicates=20, m1_bootstrap_seed=33,
            )

    def test_15_m1_mcse_is_explicitly_unavailable(self):
        item = record()
        self.assertIsNone(item.m1_comparison.mcse_estimate)
        self.assertIsNone(item.m1_comparison.mcse_interval)
        self.assertEqual(item.m1_comparison.abstention_reason,
                         "M1_MCSE_INTERVAL_NOT_IMPLEMENTED")

    def test_16_m1_interval_provenance_mismatch_fails_closed(self):
        item = record()
        changed_result = SimpleNamespace(**vars(item.m1_result))
        changed_result.within_interval = (0.2, 0.3)
        changed = replace(item, m1_result=changed_result)
        with self.assertRaises(m.M1ChallengerError):
            m._validate_roster(changed)

    def test_17_c0_remains_an_explicit_point_only_baseline(self):
        item = record()
        metrics = m.adjudicate_m1_challenger(
            (item,), (TruthTargets("d1", 0.2, 0.1, 0.1),)
        )
        within = next(x for x in metrics if x.method_id == C0_METHOD_ID and x.target == "within")
        self.assertEqual(within.interval_emission_rate, 0.0)
        self.assertEqual(within.abstention_reasons,
                         (("POINT_ONLY_BASELINE_NO_INTERVAL", 1),))

    def test_18_m1_cannot_overwrite_c5_identity(self):
        item = record()
        self.assertEqual(item.legacy_record.candidates[0].method_id, C5)
        self.assertEqual(item.m1_comparison.method_id, M1)
        self.assertNotEqual(item.m1_comparison.method_id, C5)


if __name__ == "__main__":
    unittest.main()
