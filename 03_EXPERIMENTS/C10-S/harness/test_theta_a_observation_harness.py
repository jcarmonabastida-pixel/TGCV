import unittest
from decimal import Decimal

from theta_a_observation_harness import ThetaAEvidenceCandidate, ThetaASealer


class ThetaASealerSupportTests(unittest.TestCase):
    def test_sparse_realized_arm_is_sealed_for_analyzer_abstention(self):
        row = {
            "run_id": "run-1",
            "unit_id": "u0",
            "history_ref": "h0",
            "assignment_bundle_sha256": "assignment-sha",
            "q_x_sha256": "qx-sha",
            "g_a0_sha256": "g-a0-sha",
            "g_a1_sha256": "g-a1-sha",
            "r_common_sha256": "r-common-sha",
            "assigned_arm": 0,
            "assignment_probability": 0.5,
            "assigned_vector_sha256": "vector-sha",
            "policy_fingerprint": "policy-sha",
            "r_common_fingerprint": "r-common-fingerprint",
            "history_id": "history-0",
            "observation_id": "observation-0",
            "observation_time": Decimal("0"),
            "capture_time": Decimal("0.1"),
            "ingestion_time": Decimal("0.2"),
            "enabled_observed": True,
            "admission_behavior_observed": "ADMIT",
            "profile_value_observed": "STANDARD",
            "enabled_status": "OBSERVED",
            "admission_status": "OBSERVED",
            "profile_status": "OBSERVED",
            "profile_config_id": "profile",
            "profile_config_version": "1",
            "s3_config_id": "s3",
            "s3_config_version": "1",
            "temporal_resolution": "POINT_SAMPLE",
        }
        sealed = ThetaASealer().seal(ThetaAEvidenceCandidate("run-1", (row,)))
        self.assertEqual(sealed.run_id, "run-1")
        self.assertEqual(len(sealed.rows), 1)
        self.assertEqual(sealed.rows[0]["assigned_arm"], 0)


if __name__ == "__main__":
    unittest.main()
