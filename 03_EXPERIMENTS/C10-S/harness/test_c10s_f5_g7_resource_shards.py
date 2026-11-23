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


if __name__ == "__main__":
    unittest.main()
