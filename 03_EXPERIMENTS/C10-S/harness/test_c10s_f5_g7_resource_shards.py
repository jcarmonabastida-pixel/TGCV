from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import aggregate_c10s_f5_g7_resource_shards as aggregator
import run_c10s_f5_g7_resource_shard as shard
import run_c10s_f5_g7_tiera_calibration as g7


class ResourceShardTests(unittest.TestCase):
    def test_shard_preserves_global_replicate_indices_and_only_timing(self):
        spec = type("Spec", (), {"cell_id": g7.EXPECTED_CELLS[0]})()
        fake_result = {"datasets_completed": 2}
        observed = []
        def fake_compare(*args, **kwargs):
            observed.append(kwargs["dataset_id"])
            return object()
        def fake_run_cell(spec_arg, **kwargs):
            self.assertEqual(kwargs["replicate_start"], 20)
            self.assertEqual(kwargs["k"], 2)
            g7.compare_dataset(None, dataset_id=f"1.1:{g7.RESOURCE_NAMESPACE}:{spec_arg.cell_id}:000020")
            g7.compare_dataset(None, dataset_id=f"1.1:{g7.RESOURCE_NAMESPACE}:{spec_arg.cell_id}:000021")
            return fake_result
        with tempfile.TemporaryDirectory() as d, patch.object(g7, "f5_specs", return_value=[spec]), patch.object(
            g7, "run_cell", side_effect=fake_run_cell
        ), patch.object(g7, "compare_dataset", side_effect=fake_compare):
            result = shard.execute(spec.cell_id, 20, 2, Path(d) / "shard.json")
        self.assertEqual(result["datasets_completed"], 2)
        self.assertEqual([x["dataset_id"].rsplit(":", 1)[-1] for x in result["dataset_timings"]], ["000020", "000021"])
        self.assertNotIn("comparison", json.dumps(result))
        self.assertNotIn("truth", json.dumps(result))

    def test_aggregator_rejects_missing_shard_roster(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "ROSTER_INCOMPLETE"):
                aggregator.aggregate(Path(d), Path(d) / "profile.json")

    def test_complete_roster_emits_validator_required_profile_fields(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for cell in g7.EXPECTED_CELLS:
                for start in range(0, 100, 10):
                    timings = [
                        {"dataset_id": f"1.1:{g7.RESOURCE_NAMESPACE}:{cell}:{i:06d}", "wall_seconds": 1.0}
                        for i in range(start, start + 10)
                    ]
                    payload = {
                        "schema": "C10S-F5-G7-RESOURCE-SHARD-001",
                        "protocol_version": g7.PROTOCOL_VERSION,
                        "seed_schedule_id": g7.SEED_SCHEDULE_ID,
                        "seed_namespace": g7.RESOURCE_NAMESPACE,
                        "cell_id": cell,
                        "replicate_start": start,
                        "replicate_count": 10,
                        "datasets_completed": 10,
                        "wall_elapsed_seconds": 10.0,
                        "process_cpu_seconds": 9.0,
                        "peak_rss_kib": 100000,
                        "shard_started_at_utc": "2026-11-23T10:00:00+00:00",
                        "shard_completed_at_utc": "2026-11-23T10:00:10+00:00",
                        "source_commit": "a" * 40,
                        "dataset_timings": timings,
                        "coverage_adjudication": "NOT_PERFORMED",
                        "retained_scope": "TIMING_AND_REPLICA_IDENTITY_ONLY",
                    }
                    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
                    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
                    (root / f"{cell}-{start}.json").write_text(json.dumps(payload), encoding="utf-8")
            result = aggregator.aggregate(root, root / "profile.json")
            self.assertEqual(result["dataset_count"], 200)
            self.assertEqual(result["shards_verified"], 20)
            self.assertEqual(result["source_commit"], "a" * 40)
            self.assertGreater(result["wall_elapsed_seconds"], 0)
            self.assertGreater(result["process_cpu_seconds"], 0)
            self.assertGreater(result["peak_rss_kib"], 0)
            self.assertEqual(len(result["dataset_timings"][g7.EXPECTED_CELLS[0]]), 100)


if __name__ == "__main__":
    unittest.main()
