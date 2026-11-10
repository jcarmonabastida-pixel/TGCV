import json
import tempfile
import unittest
from pathlib import Path

from trajectory_recommendation_audit_001 import (
    RecommendationAuditError,
    append_recommendation,
    verify_ledger,
)


def recommendation(label="baseline"):
    return {
        "output_kind": "HEURISTIC_RANKING_NOT_PREDICTION",
        "selector_version": "trajectory-selector-001",
        "scenario_id": label,
        "input_sha256": "a" * 64,
        "config_sha256": "b" * 64,
        "ranked_trajectories": [{"trajectory_id": "t1", "rank": 1}],
    }


class RecommendationAuditTests(unittest.TestCase):
    def test_append_records_pre_execution_event_and_chain(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recommendations.jsonl"
            first = append_recommendation(path, recommendation(), created_at="2026-10-26T10:00:00Z")
            second = append_recommendation(path, recommendation("other"), created_at="2026-10-26T10:01:00Z")
            self.assertEqual(first["event_sequence"], 1)
            self.assertEqual(second["event_sequence"], 2)
            self.assertEqual(second["previous_event_sha256"], first["event_sha256"])
            self.assertEqual(first["phase"], "PRE_EXECUTION")
            self.assertTrue(verify_ledger(path)["valid"])
            self.assertEqual(verify_ledger(path)["event_count"], 2)

    def test_modified_record_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recommendations.jsonl"
            append_recommendation(path, recommendation(), created_at="2026-10-26T10:00:00Z")
            record = json.loads(path.read_text(encoding="utf-8"))
            record["recommendation"]["scenario_id"] = "tampered"
            path.write_text(json.dumps(record) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(RecommendationAuditError, "event hash mismatch"):
                verify_ledger(path)

    def test_invalid_recommendation_is_rejected_without_creating_event(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recommendations.jsonl"
            with self.assertRaisesRegex(RecommendationAuditError, "output_kind"):
                append_recommendation(path, {"scenario_id": "baseline"})
            self.assertFalse(path.exists())

    def test_non_json_recommendation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recommendations.jsonl"
            with self.assertRaises(RecommendationAuditError):
                append_recommendation(path, {
                    "output_kind": "HEURISTIC_RANKING_NOT_PREDICTION",
                    "not_json": object(),
                })
            self.assertFalse(path.exists())

    def test_recommendation_digest_is_checked_separately(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recommendations.jsonl"
            append_recommendation(path, recommendation(), created_at="2026-10-26T10:00:00Z")
            record = json.loads(path.read_text(encoding="utf-8"))
            record["recommendation_sha256"] = "f" * 64
            # Recompute the outer event digest to isolate the inner snapshot-digest check.
            import hashlib
            import json as json_module
            payload = dict(record)
            payload.pop("event_sha256", None)
            canonical = json_module.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
            record["event_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            path.write_text(json.dumps(record) + "\\n", encoding="utf-8")
            with self.assertRaisesRegex(RecommendationAuditError, "recommendation hash mismatch"):
                verify_ledger(path)


if __name__ == "__main__":
    unittest.main()
