import unittest
from types import SimpleNamespace

from theta_a_observation_harness import SealedThetaAEvidence, _hash
from theta_a_analyzer import (ThetaAObservationAnalysisContract,
                              ThetaAObservationAnalysisResult, _canonical_hash)
from theta_a_evaluator import ThetaAObservationEvaluator, _result_payload
from c10s_synthetic_components import ContractError


class ThetaAObservationEvaluatorTests(unittest.TestCase):
    def setUp(self):
        rows = ({"history_ref": "h0", "history_id": "eh0", "unit_id": "u0",
                 "assignment_bundle_sha256": "ab", "q_x_sha256": "qx"},)
        manifest = {"run_id": "run-1", "schema": "test"}
        self.evidence = SealedThetaAEvidence("run-1", rows, manifest,
                                            _hash({"manifest": manifest, "rows": rows}))
        self.truth = SimpleNamespace(
            evaluator_only=True, outcome_id="V_CONT", estimand_id="THETA_A_QX_GA_RCOMMON_VCONT",
            estimand_version="1.0", q_x_fingerprint="qx", theta_a_truth=0.3)
        self.truth_bundle = SimpleNamespace(
            validate=lambda: None, theta_a_truth=self.truth,
            event_history_manifest=(("h0", "vec", "regime", "eh0", "content-sha"),))
        self.contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 1.0),), q_x_sha256="qx",
            assignment_bundle_sha256="ab", estimand_id="THETA_A_QX_GA_RCOMMON_VCONT",
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
            self.truth_bundle, self.evidence, result, self.contract, tolerance=0.01)
        self.assertTrue(report.truth_within_bounds)
        self.assertFalse(report.informative_bounds)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "BOUNDS_COVER_TRUTH")

    def test_bounds_excluding_reserved_truth_are_rejected_as_incorrect_adjudication(self):
        result = self.make_result(lower=-1.0, upper=0.1)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.contract, tolerance=0.01)
        self.assertFalse(report.truth_within_bounds)
        self.assertFalse(report.correct_adjudication)
        self.assertEqual(report.disposition, "INVALID_BOUNDS_EXCLUDE_TRUTH")

    def test_identified_point_estimate_is_scored_against_reserved_truth(self):
        result = self.make_result(status="IDENTIFIED", estimate=0.28, lower=0.2, upper=0.4)
        report = ThetaAObservationEvaluator().evaluate(
            self.truth_bundle, self.evidence, result, self.contract, tolerance=0.05)
        self.assertAlmostEqual(report.absolute_error, 0.02)
        self.assertTrue(report.correct_adjudication)
        self.assertEqual(report.disposition, "POINT_RECOVERED")

    def test_result_bound_to_different_evidence_is_rejected(self):
        result = self.make_result(input_sha="different")
        with self.assertRaises(ContractError):
            ThetaAObservationEvaluator().evaluate(
                self.truth_bundle, self.evidence, result, self.contract, tolerance=0.01)


if __name__ == "__main__":
    unittest.main()