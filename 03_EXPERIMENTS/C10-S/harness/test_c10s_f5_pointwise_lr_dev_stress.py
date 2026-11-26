from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from c10s_f5_rational_score_polynomials import _c10s_root_progress_event
from run_c10s_f5_pointwise_lr_dev_stress import (
    K_PER_CELL,
    TARGETS,
    build_seed_audit,
    derive_stress_seed,
    _append_event,
    _write_checkpoint,
)


class F5PointwiseLRDevelopmentStressTests(unittest.TestCase):
    def test_seed_derivation_is_stable_and_uint64(self):
        first = derive_stress_seed("F5_beta22_M10_R5", 0)
        second = derive_stress_seed("F5_beta22_M10_R5", 0)
        other = derive_stress_seed("F5_beta22_M10_R5", 1)
        self.assertEqual(first, second)
        self.assertNotEqual(first, other)
        self.assertGreaterEqual(first, 0)
        self.assertLess(first, 2**64)

    def test_predeclared_seed_roster_is_disjoint_from_history(self):
        rows, audit = build_seed_audit()
        self.assertEqual(len(rows), 2 * K_PER_CELL)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["new_unique_seed_values"], len(rows))
        self.assertEqual(audit["collision_count"], 0)
        self.assertGreater(audit["historical_unique_seed_values_checked"], 100000)

    def test_targets_are_exact_f5_beta22_functionals(self):
        self.assertEqual(str(TARGETS["W"]), "1/5")
        self.assertEqual(str(TARGETS["B"]), "1/20")

    def test_progress_events_are_flushed_jsonl(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "progress.jsonl"
            _append_event(path, "PROFILE_START", cell_id="M30R20", component="W")
            record = json.loads(path.read_text(encoding="utf-8").splitlines()[0])
            self.assertEqual(record["event"], "PROFILE_START")
            self.assertEqual(record["component"], "W")
            self.assertIn("utc", record)

    def test_checkpoint_is_atomically_persisted_with_partial_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            _write_checkpoint(
                path, source_revision="a" * 40,
                seed_audit={"status": "PASS"}, results=[],
                completed_stage="SEED_AUDIT", complete=False,
            )
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertFalse(payload["complete"])
            self.assertEqual(payload["completed_stage"], "SEED_AUDIT")
            self.assertFalse(path.with_suffix(".json.tmp").exists())

    def test_root_isolation_telemetry_is_opt_in_and_jsonl(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "roots.jsonl"
            previous = os.environ.get("TGCV_C10S_ROOT_PROGRESS_PATH")
            try:
                os.environ["TGCV_C10S_ROOT_PROGRESS_PATH"] = str(path)
                _c10s_root_progress_event({"phase": "TEST", "degree": 4})
            finally:
                if previous is None:
                    os.environ.pop("TGCV_C10S_ROOT_PROGRESS_PATH", None)
                else:
                    os.environ["TGCV_C10S_ROOT_PROGRESS_PATH"] = previous
            record = json.loads(path.read_text(encoding="utf-8").splitlines()[0])
            self.assertEqual(record["event"]["phase"], "TEST")
            self.assertEqual(record["event"]["degree"], 4)


if __name__ == "__main__":
    unittest.main()
