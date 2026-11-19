from __future__ import annotations

from dataclasses import replace
import json
import math
import unittest

from c10s_nested_mr_comparative_inference_engine import (
    C0_METHOD_ID,
    ComparativeEngineError,
    TruthTargets,
    adjudicate_matched_datasets,
    adjudicate_profile_diagnostics,
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

    def test_profile_diagnostics_can_be_disabled_without_changing_candidate_intervals(self):
        f1 = compare_dataset(
            f1_rows(), dataset_id="F1-NO-PROFILE", family="F1",
            target_m=20, target_r=8,
            baseline_bootstrap_replicates=100, baseline_bootstrap_seed=19,
            include_profile_diagnostics=False,
        )
        f1_diagnostics = dict(f1.candidates[0].diagnostics)
        self.assertNotIn("between_profile_status", f1_diagnostics)
        self.assertIsNotNone(f1.candidates[0].comparison.within_interval)
        self.assertIsNotNone(f1.candidates[0].comparison.between_interval)

        f5 = compare_dataset(
            f5_rows(), dataset_id="F5-NO-PROFILE", family="F5",
            target_m=10, target_r=5,
            baseline_bootstrap_replicates=100, baseline_bootstrap_seed=23,
            bootstrap_replicates=60, bootstrap_seed=20261119,
            include_profile_diagnostics=False,
        )
        f5_diagnostics = dict(f5.candidates[0].diagnostics)
        self.assertNotIn("mcse_profile_status", f5_diagnostics)
        self.assertIsNotNone(f5.candidates[0].comparison.within_interval)
        self.assertIsNotNone(f5.candidates[0].comparison.between_interval)
        self.assertIsNone(f5.candidates[0].comparison.mcse_interval)

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
        diagnostic_map = dict(candidate.diagnostics)
        audit = json.loads(diagnostic_map["likelihood_optimizer_audit_json"])
        self.assertEqual(len(audit["starts"]), 3)
        self.assertTrue(all(item["message"] for item in audit["starts"]))
        self.assertIn(audit["status"], (
            "OPTIMIZER_CONCORDANT", "OPTIMIZER_DISCORDANT",
            "INDEPENDENT_OPTIMIZER_UNRESOLVED",
            "LIKELIHOOD_CONCORDANT_PARAMETER_DISAGREEMENT",
        ))
        self.assertIn("two_point_limit_log_likelihood", audit)
        self.assertIn("profile_log_concentration_curvature", audit)
        self.assertIsNotNone(audit["profile_log_concentration_curvature"])
        self.assertTrue(math.isfinite(audit["profile_log_concentration_curvature"]))
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
        diagnostic_map = dict(candidate.diagnostics)
        self.assertIn(
            diagnostic_map["mcse_profile_inference_eligibility"],
            {
                "PROFILE_DIAGNOSTIC_ELIGIBLE_NOT_COVERAGE_CERTIFIED",
                "ABSTAIN_PROFILE_INFERENCE",
            },
        )
        if diagnostic_map["mcse_profile_inference_eligibility"] == "ABSTAIN_PROFILE_INFERENCE":
            self.assertNotEqual(diagnostic_map["mcse_profile_abstention_reason"], "NONE")
        else:
            self.assertEqual(diagnostic_map["mcse_profile_abstention_reason"], "NONE")
        # This policy governs only the experimental F5 profile diagnostic;
        # it must not suppress or rewrite the independent C5 bootstrap outputs.
        self.assertIsNotNone(candidate.comparison.within_interval)
        self.assertIsNotNone(candidate.comparison.between_interval)
        self.assertIsNone(candidate.comparison.mcse_interval)

    def test_f5_profile_diagnostic_roster_is_separate_from_c5_coverage(self):
        record = self._f5()
        metrics, = adjudicate_profile_diagnostics((record,))
        self.assertEqual(metrics.family, "F5")
        self.assertEqual(metrics.diagnostic, "MCSE_PROFILE_OPTIMIZATION")
        self.assertEqual(metrics.n_datasets, 1)
        self.assertEqual(
            metrics.eligible_count + metrics.abstained_count + metrics.not_evaluated_count,
            metrics.n_datasets,
        )
        self.assertEqual(metrics.eligible_rate, metrics.eligible_count / metrics.n_datasets)
        # Profile diagnostics have no truth or coverage field by design.
        self.assertFalse(hasattr(metrics, "conditional_coverage"))
        self.assertFalse(hasattr(metrics, "unconditional_cover_rate"))
        # C5's MCSE interval remains independently unavailable.
        self.assertIsNone(record.candidates[0].comparison.mcse_interval)

    def test_f1_profile_diagnostic_roster_is_separate_from_coverage(self):
        record = self._f1()
        metrics, = adjudicate_profile_diagnostics((record,))
        self.assertEqual(metrics.family, "F1")
        self.assertEqual(metrics.diagnostic, "BETWEEN_VARIANCE_PROFILE_LOG_LIKELIHOOD")
        self.assertEqual(metrics.n_datasets, 1)
        self.assertEqual(
            metrics.eligible_count + metrics.abstained_count + metrics.not_evaluated_count,
            metrics.n_datasets,
        )
        self.assertEqual(metrics.eligible_rate, metrics.eligible_count / metrics.n_datasets)
        candidate = record.candidates[0]
        diagnostic_map = dict(candidate.diagnostics)
        self.assertIn(
            diagnostic_map["between_profile_inference_eligibility"],
            {
                "PROFILE_DIAGNOSTIC_ELIGIBLE_NOT_COVERAGE_CERTIFIED",
                "ABSTAIN_PROFILE_INFERENCE",
            },
        )
        self.assertIn(
            diagnostic_map["between_profile_optimizer_adjudication_status"],
            {
                "OPTIMIZATION_CONCORDANT", "OPTIMIZATION_DISCORDANT",
                "OPTIMIZATION_INSUFFICIENT", "OPTIMIZATION_BOUNDARY_SENSITIVE",
            },
        )
        self.assertIn("between_profile_root_adjudication_status", diagnostic_map)
        self.assertIn(
            diagnostic_map["between_profile_root_adjudication_status"],
            {"ROOTS_AGREE", "ROOTS_DISCREPANT", "ROOTS_UNRESOLVED"},
        )
        self.assertIn("between_profile_root_adjudication_reason", diagnostic_map)
        self.assertIn("between_profile_root_adjudication_f1_count", diagnostic_map)
        self.assertIn("between_profile_root_adjudication_sturm_count", diagnostic_map)
        self.assertIn("between_profile_root_adjudication_matched_count", diagnostic_map)
        self.assertIn("between_profile_root_adjudication_domain", diagnostic_map)
        self.assertEqual(
            diagnostic_map["between_profile_root_adjudication_domain"],
            "(0,+infinity)",
        )
        self.assertIn(
            "between_profile_root_adjudication_removed_zero_factor_multiplicity",
            diagnostic_map,
        )
        self.assertIn("between_profile_root_adjudication_boundary_roots", diagnostic_map)
        self.assertIn("between_profile_root_adjudication_exact_intervals", diagnostic_map)
        if diagnostic_map["between_profile_root_adjudication_status"] != "ROOTS_AGREE":
            self.assertEqual(
                diagnostic_map["between_profile_inference_eligibility"],
                "ABSTAIN_PROFILE_INFERENCE",
            )
        self.assertIn("between_profile_optimizer_stationary_point_counts", diagnostic_map)
        self.assertIn("between_profile_optimizer_stationary_point_types", diagnostic_map)
        self.assertIn("between_profile_optimizer_tangential_score_root_counts", diagnostic_map)
        self.assertIn("between_profile_optimizer_unresolved_tangential_candidate_counts", diagnostic_map)
        self.assertIn("between_profile_optimizer_polynomial_degrees", diagnostic_map)
        self.assertIn("between_profile_optimizer_polynomial_root_counts", diagnostic_map)
        self.assertIn("between_profile_optimizer_polynomial_statuses", diagnostic_map)
        self.assertIn("between_profile_optimizer_critical_point_solver_statuses", diagnostic_map)
        self.assertIn("between_profile_optimizer_polynomial_scan_discordances", diagnostic_map)
        self.assertIn("between_profile_optimizer_grid_span_configurations", diagnostic_map)
        self.assertIn("between_profile_optimizer_loglik_spread", diagnostic_map)
        self.assertIn("between_profile_optimizer_stationary_location_spread", diagnostic_map)
        self.assertEqual(
            len(diagnostic_map["between_profile_optimizer_stationary_point_counts"].split(",")),
            9,
        )
        self.assertEqual(
            len(diagnostic_map["between_profile_optimizer_grid_span_configurations"].split(";")),
            9,
        )
        if diagnostic_map["between_profile_inference_eligibility"] == "ABSTAIN_PROFILE_INFERENCE":
            self.assertNotEqual(diagnostic_map["between_profile_abstention_reason"], "NONE")
        else:
            self.assertEqual(diagnostic_map["between_profile_abstention_reason"], "NONE")
        self.assertEqual(
            diagnostic_map["between_profile_interval"],
            "NOT_EMITTED_NO_LR_CUTOFF_SELECTED",
        )
        self.assertFalse(hasattr(metrics, "conditional_coverage"))

    def test_profile_diagnostic_roster_rejects_unsupported_family_and_mixed_designs(self):
        f5 = self._f5()
        unsupported = replace(f5, family="F3")
        with self.assertRaisesRegex(ComparativeEngineError, "ONE_FAMILY_F1_OR_F5"):
            adjudicate_profile_diagnostics((unsupported,))
        other = replace(f5, dataset_id="F5-DATA-002", target_m=11)
        with self.assertRaisesRegex(ComparativeEngineError, "STRATIFY"):
            adjudicate_profile_diagnostics((f5, other))

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
