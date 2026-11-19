import unittest
from dataclasses import replace

from theta_a_observation_harness import SealedThetaAEvidence, _hash
from theta_a_analyzer import (
    ThetaAObservationAnalysisContract, ThetaAObservationAnalyzer,
    ThetaAStructuralSupportRow, ThetaAStructuralSupportContract,
    adjudicate_theta_a_structural_support,
)
from c10s_synthetic_components import ContractError


class ThetaAObservationAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.evidence = SealedThetaAEvidence(
            run_id="run-1",
            rows=(
                {"unit_id": "u0", "history_ref": "h0", "assigned_arm": 0,
                 "assignment_probability": 0.5, "assigned_vector_sha256": "v0",
                 "policy_fingerprint": "p0", "r_common_fingerprint": "r",
                 "history_id": "eh0", "assignment_bundle_sha256": "ab", "q_x_sha256": "qx", "g_a0_sha256": "ga0",
                 "g_a1_sha256": "ga1", "r_common_sha256": "rc"},
                {"unit_id": "u1", "history_ref": "h1", "assigned_arm": 1,
                 "assignment_probability": 0.5, "assigned_vector_sha256": "v1",
                 "policy_fingerprint": "p1", "r_common_fingerprint": "r",
                 "history_id": "eh1", "assignment_bundle_sha256": "ab", "q_x_sha256": "qx", "g_a0_sha256": "ga0",
                 "g_a1_sha256": "ga1", "r_common_sha256": "rc"},
            ),
            manifest={"run_id": "run-1", "schema": "test"},
            sha256=_hash({"manifest": {"run_id": "run-1", "schema": "test"},
                          "rows": (
                              {"unit_id": "u0", "history_ref": "h0", "assigned_arm": 0,
                               "assignment_probability": 0.5, "assigned_vector_sha256": "v0",
                               "policy_fingerprint": "p0", "r_common_fingerprint": "r",
                               "history_id": "eh0", "assignment_bundle_sha256": "ab",
                               "q_x_sha256": "qx", "g_a0_sha256": "ga0",
                               "g_a1_sha256": "ga1", "r_common_sha256": "rc"},
                              {"unit_id": "u1", "history_ref": "h1", "assigned_arm": 1,
                               "assignment_probability": 0.5, "assigned_vector_sha256": "v1",
                               "policy_fingerprint": "p1", "r_common_fingerprint": "r",
                               "history_id": "eh1", "assignment_bundle_sha256": "ab",
                               "q_x_sha256": "qx", "g_a0_sha256": "ga0",
                               "g_a1_sha256": "ga1", "r_common_sha256": "rc"}
                          )}))
        self.contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.6)),
            q_x_sha256="qx", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc")

    def test_point_samples_return_trivial_sharp_bounds_and_no_point_estimate(self):
        result = ThetaAObservationAnalyzer().analyze(self.evidence, self.contract)
        self.assertEqual(result.identification, "PARTIALLY_IDENTIFIED")
        self.assertIsNone(result.point_estimate)
        self.assertEqual((result.lower_bound, result.upper_bound), (-1.0, 1.0))
        self.assertEqual(result.target_q_x_coverage, 1.0)
        self.assertEqual(result.temporal_resolution, "POINT_SAMPLE")

    def test_qx_fingerprint_mismatch_is_rejected(self):
        bad = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.6)),
            q_x_sha256="wrong", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc")
        with self.assertRaises(ContractError):
            ThetaAObservationAnalyzer().analyze(self.evidence, bad)

    def test_missing_target_history_is_reported_without_fabricating_point_estimate(self):
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.4), ("h2", 0.2)),
            q_x_sha256="qx", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc")
        result = ThetaAObservationAnalyzer().analyze(self.evidence, contract)
        self.assertEqual(result.missing_target_histories, ("h2",))
        self.assertAlmostEqual(result.target_q_x_coverage, 0.8)
        self.assertEqual(result.identification, "INDETERMINATE")
        self.assertEqual(result.abstention_reason, "TARGET_QX_SUPPORT_INCOMPLETE")
        self.assertIsNone(result.point_estimate)
        self.assertEqual((result.lower_bound, result.upper_bound), (-1.0, 1.0))

    def test_missing_realized_arm_returns_indeterminate_not_sealer_or_analyzer_crash(self):
        rows = (dict(self.evidence.rows[0], q_x_sha256="source-qx"),)
        manifest = {"run_id": "run-1", "schema": "test"}
        sparse = SealedThetaAEvidence(
            "run-1", rows, manifest,
            _hash({"manifest": manifest, "rows": rows}))
        result = ThetaAObservationAnalyzer().analyze(sparse, replace(self.contract, source_q_x_sha256="source-qx"))
        self.assertEqual(result.identification, "INDETERMINATE")
        self.assertEqual(result.abstention_reason, "REALIZED_GA_ARM_SUPPORT_MISSING")
        self.assertIsNone(result.point_estimate)
        self.assertEqual((result.lower_bound, result.upper_bound), (-1.0, 1.0))

    def test_qx_masses_must_sum_to_one(self):
        bad = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.5)),
            q_x_sha256="qx", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc")
        with self.assertRaises(ContractError):
            ThetaAObservationAnalyzer().analyze(self.evidence, bad)


    def test_structural_target_history_outside_source_support_is_not_identified(self):
        contract = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx-sha", "source-qx-sha",
            (
                ThetaAStructuralSupportRow("h0", 0.7, 0.7, True, True, True, 0.5),
                ThetaAStructuralSupportRow("h1", 0.3, 0.0, True, True, True, None),
            ),
        )
        result = adjudicate_theta_a_structural_support(contract)
        self.assertEqual(result.status, "NOT_IDENTIFIED")
        self.assertEqual(result.reason, "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT")
        self.assertEqual(result.unsupported_target_histories, ("h1",))
        self.assertTrue(result.contract_sha256)

    def test_structural_support_sufficient_is_not_confused_with_realized_arm_support(self):
        contract = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx-sha", "source-qx-sha",
            (ThetaAStructuralSupportRow("h0", 1.0, 1.0, True, True, True, 0.5),),
        )
        result = adjudicate_theta_a_structural_support(contract)
        self.assertEqual(result.status, "STRUCTURAL_SUPPORT_SUFFICIENT")
        self.assertEqual(result.unsupported_target_histories, ())

    def test_combined_target_gap_and_assignment_positivity_preserve_both_causes(self):
        contract = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx-sha", "source-qx-sha",
            (
                ThetaAStructuralSupportRow("h0", 0.6, 0.6, True, True, True, 0.0),
                ThetaAStructuralSupportRow("h1", 0.4, 0.0, True, True, True, None),
            ),
        )
        result = adjudicate_theta_a_structural_support(contract)
        self.assertEqual(result.status, "NOT_IDENTIFIED")
        self.assertEqual(
            result.reason,
            "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT+SOURCE_ASSIGNMENT_POSITIVITY_FAILURE",
        )
        self.assertEqual(result.unsupported_target_histories, ("h1",))
        self.assertEqual(result.assignment_positivity_failure_histories, ("h0",))

    def test_undefined_or_infeasible_policy_is_contract_error_not_nonidentification(self):
        for row in (
            ThetaAStructuralSupportRow("h0", 1.0, 0.0, False, True, True, None),
            ThetaAStructuralSupportRow("h0", 1.0, 0.0, True, False, True, None),
            ThetaAStructuralSupportRow("h0", 1.0, 0.0, True, True, False, None),
        ):
            contract = ThetaAStructuralSupportContract(
                "support-fixture", "1.0", "target-qx-sha", "source-qx-sha", (row,),
            )
            with self.assertRaises(ContractError):
                adjudicate_theta_a_structural_support(contract)

    def test_structural_assignment_positivity_failure_is_not_identified_separately(self):
        contract = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx-sha", "source-qx-sha",
            (ThetaAStructuralSupportRow("h0", 1.0, 1.0, True, True, True, 0.0),),
        )
        result = adjudicate_theta_a_structural_support(contract)
        self.assertEqual(result.status, "NOT_IDENTIFIED")
        self.assertEqual(result.reason, "SOURCE_ASSIGNMENT_POSITIVITY_FAILURE")
        self.assertEqual(result.unsupported_target_histories, ())
        self.assertEqual(result.assignment_positivity_failure_histories, ("h0",))

    def test_source_assignment_positivity_failure_reaches_analyzer_as_distinct_nonidentification(self):
        rows = (
            dict(self.evidence.rows[0], assignment_probability=1.0, q_x_sha256="source-qx"),
            dict(self.evidence.rows[1], q_x_sha256="source-qx"),
        )
        manifest = {"run_id": "run-1", "schema": "test"}
        evidence = SealedThetaAEvidence(
            "run-1", rows, manifest,
            _hash({"manifest": manifest, "rows": rows}),
        )
        support = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "target-qx", "source-qx",
            (
                ThetaAStructuralSupportRow("h0", 0.4, 0.4, True, True, True, 0.0),
                ThetaAStructuralSupportRow("h1", 0.6, 0.6, True, True, True, 0.5),
            ),
        )
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.6)),
            q_x_sha256="target-qx", source_q_x_sha256="source-qx",
            assignment_bundle_sha256="ab", g_a0_sha256="ga0",
            g_a1_sha256="ga1", r_common_sha256="rc",
            probability_a1_by_history=(("h0", 0.0), ("h1", 0.5)),
            structural_support_contract=support,
        )
        result = ThetaAObservationAnalyzer().analyze(evidence, contract)
        self.assertEqual(result.identification, "NOT_IDENTIFIED")
        self.assertEqual(result.abstention_reason, "SOURCE_ASSIGNMENT_POSITIVITY_FAILURE")
        self.assertEqual(result.missing_target_histories, ())
        self.assertEqual(result.assignment_positivity_failure_histories, ("h0",))
        self.assertAlmostEqual(result.target_q_x_coverage, 1.0)
        self.assertIsNone(result.point_estimate)

    def test_structural_target_source_support_reaches_analyzer_not_identified(self):
        rows = (dict(self.evidence.rows[0], q_x_sha256="source-qx"),)
        manifest = {"run_id": "run-1", "schema": "test"}
        sparse = SealedThetaAEvidence(
            "run-1", rows, manifest,
            _hash({"manifest": manifest, "rows": rows}),
        )
        support = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "qx", "source-qx",
            (
                ThetaAStructuralSupportRow("h0", 0.4, 1.0, True, True, True, 0.5),
                ThetaAStructuralSupportRow("h1", 0.6, 0.0, True, True, True, None),
            ),
        )
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.6)),
            q_x_sha256="qx", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc",
            structural_support_contract=support, source_q_x_sha256="source-qx",
        )
        result = ThetaAObservationAnalyzer().analyze(sparse, contract)
        self.assertEqual(result.identification, "NOT_IDENTIFIED")
        self.assertEqual(result.abstention_reason, "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT")
        self.assertEqual(result.missing_target_histories, ("h1",))
        self.assertAlmostEqual(result.target_q_x_coverage, 0.4)
        self.assertIsNone(result.point_estimate)
        self.assertTrue(result.structural_support_sha256)

    def test_structural_support_target_fingerprint_must_bind_analysis_qx(self):
        support = ThetaAStructuralSupportContract(
            "support-fixture", "1.0", "wrong-qx", "source-qx",
            (ThetaAStructuralSupportRow("h0", 1.0, 1.0, True, True, True, 0.5),),
        )
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 1.0),), q_x_sha256="qx",
            assignment_bundle_sha256="ab", g_a0_sha256="ga0",
            g_a1_sha256="ga1", r_common_sha256="rc",
            structural_support_contract=support, source_q_x_sha256="source-qx",
        )
        with self.assertRaises(ContractError):
            ThetaAObservationAnalyzer().analyze(self.evidence, contract)
if __name__ == "__main__":
    unittest.main()