import unittest

from theta_a_observation_harness import SealedThetaAEvidence
from theta_a_analyzer import (ThetaAObservationAnalysisContract,
                              ThetaAObservationAnalyzer)
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
            manifest={}, sha256="sealed-hash")
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
        self.assertIsNone(result.point_estimate)
        self.assertEqual((result.lower_bound, result.upper_bound), (-1.0, 1.0))

    def test_qx_masses_must_sum_to_one(self):
        bad = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("h0", 0.4), ("h1", 0.5)),
            q_x_sha256="qx", assignment_bundle_sha256="ab",
            g_a0_sha256="ga0", g_a1_sha256="ga1", r_common_sha256="rc")
        with self.assertRaises(ContractError):
            ThetaAObservationAnalyzer().analyze(self.evidence, bad)


if __name__ == "__main__":
    unittest.main()