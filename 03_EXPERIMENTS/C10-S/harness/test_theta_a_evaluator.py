import unittest
from types import SimpleNamespace

from theta_a_observation_harness import SealedThetaAEvidence, _hash
from theta_a_analyzer import (ThetaAObservationAnalysisContract, ThetaAObservationAnalyzer,
                              ThetaAObservationAnalysisResult, _canonical_hash,
                              ThetaAStructuralSupportRow, ThetaAStructuralSupportContract,
                              adjudicate_theta_a_structural_support)
from theta_a_evaluator import ThetaAObservationEvaluator, _result_payload
from c10s_synthetic_components import ContractError


class ThetaAObservationEvaluatorTests(unittest.TestCase):
    def setUp(self):
        rows = ({"history_ref": "h0", "history_id": "eh0", "unit_id": "u0",
                 "assignment_bundle_sha256": "ab", "q_x_sha256": "qx",
                 "g_a0_sha256": "ga0", "g_a1_sha256": "ga1",
                 "r_common_sha256": "rc", "r_common_fingerprint": "r",
                 "assigned_arm": 0, "assignment_probability": 0.5,
                 "assigned_vector_sha256": "v0", "policy_fingerprint": "p0"},)
        manifest = {"run_id": "run-1", "schema": "test"}
        self.evidence = SealedThetaAEvidence("run-1", rows, manifest,
                                            _hash({"manifest": manifest, "rows": rows}))
        self.truth = SimpleNamespace(
            evaluator_only=True, outcome_id="V_CONT", estimand_id="THETA_A_QX_GA_RCOMMON_VCONT",
            estimand_version="1.0", q_x_fingerprint="qx", g_a0_fingerprint="ga0",
            g_a1_fingerprint="ga1", theta_a_truth=0.3,
            contributions=(SimpleNamespace(history_ref="h0", r_common_fingerprint="r"),))
        self.truth_bundle = SimpleNamespace(
            validate=lambda: None, theta_a_truth=self.truth,
            event_history_manifest=(("h0", "vec", "regime", "eh0", "content-sha"),))
        self.assignment_bundle = SimpleNamespace(
            result_sha256="ab", q_x_sha256="qx", g_a0_sha256="ga0",
            g_a1_sha256="ga1", r_common_sha256="rc",
            assignments=(SimpleNamespace(
                unit_id="u0", history_ref="h0", assigned_arm=0,
                probability_a0=0.5, probability_a1=0.5,
                assigned_vector_sha256="v0", policy_fingerprint="p0",
                r_common_fingerprint="r"),))
        self.contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 1.0),), q_x_sha256="qx",
            assignment_bundle_sha256="ab", g_a0_sha256="ga0", g_a1_sha256="ga1",
            r_common_sha256="rc", estimand_id="THETA_A_QX_GA_RCOMMON_VCONT",
            estimand_version="1.0")

    def make_result(self, *, status="PARTIALLY_IDENTIFIED", estimate=None,
                    lower=-1.0, upper=1.0, input_sha=None):
        provisional = ThetaAObservationAnalysisResult(
            "run-1", "THETA_A_QX_GA_RCOMMON_VCONT", "1.0", status, estimate, lower, upper,
            1.0, (), (1, 1), "POINT_SAMPLE", "STRICT_VCONT_NOT_OBSERVED",
            input_sha or self.evidence.sha256, "")
        return ThetaAObservationAnalysisResult(
            provisional.run_id, provisional.estimand_id, provisional.estimand_version,
            provisional.identification, provisional.point_estimate,
            provisional.lower_bound, provisional.upper_bound,
            provisional.target_q_x_coverage, provisional.missing_target_histories,
            provisional.assigned_arm_unit_counts, provisional.temporal_resolution,
            provisional.abstention_reason, provisional.input_sha256,
            _canonical_hash(_result_payload(provisional)))

    def test_noninformative_bounds_cover_reserved_truth_but_are_not_informative(self):
        result = self.make_result()
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.assignment_bundle, self.contract, tolerance=0.01)
        self.assertTrue(report.truth_within_bounds)
        self.assertFalse(report.informative_bounds)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "BOUNDS_COVER_TRUTH")

    def test_bounds_excluding_reserved_truth_are_rejected_as_incorrect_adjudication(self):
        result = self.make_result(lower=-1.0, upper=0.1)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.assignment_bundle, self.contract, tolerance=0.01)
        self.assertFalse(report.truth_within_bounds)
        self.assertFalse(report.correct_adjudication)
        self.assertEqual(report.disposition, "INVALID_BOUNDS_EXCLUDE_TRUTH")

    def test_identified_point_estimate_is_scored_against_reserved_truth(self):
        result = self.make_result(status="IDENTIFIED", estimate=0.28, lower=0.2, upper=0.4)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.assignment_bundle, self.contract, tolerance=0.05)
        self.assertAlmostEqual(report.absolute_error, 0.02)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "POINT_RECOVERED")

    def test_indeterminate_abstention_still_requires_bounds_to_cover_reserved_truth(self):
        result = self.make_result(status="INDETERMINATE", lower=-1.0, upper=0.1)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.assignment_bundle, self.contract, tolerance=0.01)
        self.assertFalse(report.truth_within_bounds)
        self.assertFalse(report.correct_adjudication)
        self.assertEqual(report.disposition, "ABSTENTION_BOUNDS_EXCLUDE_TRUTH")

    def test_result_bound_to_different_evidence_is_rejected(self):
        result = self.make_result(input_sha="different")
        with self.assertRaises(ContractError):
            ThetaAObservationEvaluator().evaluate(
                self.truth_bundle, self.evidence, result, self.assignment_bundle, self.contract, tolerance=0.01)

    def test_evaluator_accepts_assignment_positivity_nonidentification_distinct_from_target_gap(self):
        row = dict(self.evidence.rows[0], assignment_probability=1.0)
        manifest = self.evidence.manifest
        evidence = SealedThetaAEvidence(
            self.evidence.run_id, (row,), manifest,
            _hash({"manifest": manifest, "rows": (row,)}),
        )
        support = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "qx", "qx",
            (ThetaAStructuralSupportRow("h0", 1.0, 1.0, True, True, True, 0.0),),
        )
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 1.0),), q_x_sha256="qx",
            assignment_bundle_sha256="ab", g_a0_sha256="ga0", g_a1_sha256="ga1",
            r_common_sha256="rc", probability_a1_by_history=(("h0", 0.0),),
            structural_support_contract=support,
        )
        assignment_bundle = SimpleNamespace(
            result_sha256="ab", q_x_sha256="qx", g_a0_sha256="ga0",
            g_a1_sha256="ga1", r_common_sha256="rc",
            assignments=(SimpleNamespace(
                unit_id="u0", history_ref="h0", assigned_arm=0,
                probability_a0=1.0, probability_a1=0.0,
                assigned_vector_sha256="v0", policy_fingerprint="p0",
                r_common_fingerprint="r"),),
        )
        result = ThetaAObservationAnalyzer().analyze(evidence, contract)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, evidence, result, assignment_bundle, contract, tolerance=0.01)
        self.assertEqual(result.abstention_reason, "SOURCE_ASSIGNMENT_POSITIVITY_FAILURE")
        self.assertEqual(result.assignment_positivity_failure_histories, ("h0",))
        self.assertEqual(result.missing_target_histories, ())
        self.assertTrue(report.truth_within_bounds)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "CORRECT_ABSTENTION")

    def test_evaluator_accepts_correct_structural_nonidentification_with_distinct_target_source(self):
        source_rows = tuple(dict(row, q_x_sha256="source-qx") for row in self.evidence.rows)
        manifest = self.evidence.manifest
        evidence = SealedThetaAEvidence(
            self.evidence.run_id, source_rows, manifest,
            _hash({"manifest": manifest, "rows": source_rows}),
        )
        support = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx", "source-qx",
            (
                ThetaAStructuralSupportRow("h0", 0.4, 1.0, True, True, True, 0.5),
                ThetaAStructuralSupportRow("h1", 0.6, 0.0, True, True, True, None),
            ),
        )
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.6)),
            q_x_sha256="target-qx", source_q_x_sha256="source-qx",
            assignment_bundle_sha256="ab", g_a0_sha256="ga0",
            g_a1_sha256="ga1", r_common_sha256="rc",
            estimand_id="THETA_A_QX_GA_RCOMMON_VCONT", estimand_version="1.0",
            structural_support_contract=support,
        )
        self.truth.q_x_fingerprint = "target-qx"
        self.assignment_bundle.q_x_sha256 = "source-qx"
        provisional = ThetaAObservationAnalysisResult(
            run_id="run-1", estimand_id=contract.estimand_id,
            estimand_version=contract.estimand_version, identification="NOT_IDENTIFIED",
            point_estimate=None, lower_bound=-1.0, upper_bound=1.0,
            target_q_x_coverage=0.4, missing_target_histories=("h1",),
            assigned_arm_unit_counts=(1, 0), temporal_resolution="POINT_SAMPLE",
            abstention_reason="TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
            input_sha256=evidence.sha256, output_sha256="",
            structural_support_sha256=adjudicate_theta_a_structural_support(support).contract_sha256,
        )
        result = ThetaAObservationAnalysisResult(
            **{**provisional.__dict__, "output_sha256": _canonical_hash(_result_payload(provisional))}
        )
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, evidence, result, self.assignment_bundle, contract, tolerance=0.01)
        self.assertTrue(report.truth_within_bounds)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "CORRECT_ABSTENTION")

if __name__ == "__main__":
    unittest.main()