"""Pure fixture tests for Gate 185 capture primitives; never invoke producers."""
from dataclasses import replace
import copy
import json
import hashlib
import math
import unittest
from types import SimpleNamespace

import rfc8785

from vcont_benchmark_protocol import (
    SCENARIO_IDS, build_scenario_estimand_matrix, scenario_matrix_fingerprint,
)
from vcont_evidence_export import (
    CapturedBenchmark, ContractError, capture_matrix, freeze_report_snapshot,
)


class CaptureV2Tests(unittest.TestCase):
    def setUp(self):
        self.versions = tuple((sid, "VCONT-SYNTH-001") for sid in SCENARIO_IDS)
        self.matrix = build_scenario_estimand_matrix(dict(self.versions))
        self.design = SimpleNamespace(
            scenario_versions=self.versions,
            n_units=32,
            outer_replicates=2,
            repeated_assignments=2,
            matrix_fingerprint=scenario_matrix_fingerprint(self.matrix),
        )

    def report_fixture(self):
        temporal = [{
            "scenario_id": "R0_FOCAL_POSITIVE",
            "scenario_version": "VCONT-SYNTH-001",
            "N": 32,
            "outer_replicate_id": "outer-000000",
            "assignment_role": "RUN",
            "assignment_index": -1,
            "run_id": "run-0001",
            "world_id": "world-0001",
            "world_seed": 18446744073709551615,
            "z_assignment_seed": 9007199254740993,
            "g_assignment_seed": 17,
        }]
        pair_ledger = [{
            "key": ["R0_FOCAL_POSITIVE", "VCONT-SYNTH-001",
                    "ITT_Z_RUN_CONDITIONAL_VCONT", "001", "MONTE_CARLO"],
            "contributions": [{
                "outer_replicate_id": "outer-000000",
                "world_id": "world-0001",
                "run_id": "run-0001",
                "world_seed": 18446744073709551615,
            }],
        }]
        manifest = {
            "scenario_versions": self.versions,
            "N": 32, "M": 2, "R": 2,
            "matrix_fingerprint": self.design.matrix_fingerprint,
            "seed_bank_label": "evaluation",
            "seed_bank_fingerprint": "a" * 64,
            "executable_commit": "c" * 40,
            "configuration_fingerprint": "b" * 64,
            "metric_targets": (),
            "temporal_manifest": copy.deepcopy(temporal),
            "pair_ledger": copy.deepcopy(pair_ledger),
        }
        return {
            "design": {
                "scenario_versions": self.versions, "n_units": 32,
                "outer_replicates": 2, "repeated_assignments": 2,
                "matrix_fingerprint": self.design.matrix_fingerprint,
                "metric_targets": (), "seed_bank_label": "evaluation",
                "seed_bank_fingerprint": "a" * 64, "executable_commit": "c" * 40,
                "configuration_fingerprint": "b" * 64,
            },
            "temporal_manifest": temporal,
            "pair_ledger": pair_ledger,
            "manifest": manifest,
            "scenario_reports": {},
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "report_fingerprint": hashlib.sha256(
                json.dumps(
                    json.loads(json.dumps(manifest, default=lambda value: value.__dict__, sort_keys=True)),
                    sort_keys=True, separators=(",", ":"), allow_nan=False,
                ).encode("utf-8")
            ).hexdigest(),
        }

    def test_matrix_capture_has_exact_52_rows_and_recomputable_digest(self):
        capture = capture_matrix(self.matrix, self.design)
        payload = capture.to_payload()
        self.assertEqual(capture.row_count, 52)
        self.assertEqual(len(payload["rows"]), 52)
        digest_input = {
            "schema_id": "TGCV-C10S-VCONT-MATRIX-CAPTURE",
            "schema_version": "1.0.0",
            "row_count": 52,
            "rows": payload["rows"],
        }
        self.assertEqual(
            capture.full_matrix_sha256,
            __import__("hashlib").sha256(rfc8785.dumps(digest_input)).hexdigest(),
        )
        self.assertEqual(capture.full_matrix_digest_algorithm,
                         "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1")

    def test_matrix_capture_rejects_permutation_even_when_pair_set_is_unchanged(self):
        with self.assertRaises(ContractError):
            capture_matrix((self.matrix[1], self.matrix[0]) + self.matrix[2:], self.design)

    def test_tolerance_id_changes_full_digest_but_not_legacy_fingerprint(self):
        changed = (replace(self.matrix[0], tolerance_id="TOLERANCE-REVISION-2"),) + self.matrix[1:]
        self.assertEqual(scenario_matrix_fingerprint(changed), self.design.matrix_fingerprint)
        changed_capture = capture_matrix(changed, self.design)
        baseline = capture_matrix(self.matrix, self.design)
        self.assertNotEqual(changed_capture.full_matrix_sha256, baseline.full_matrix_sha256)

    def test_report_snapshot_wraps_uint64_and_is_immutable_from_compatibility_dict(self):
        report = self.report_fixture()
        snapshot = freeze_report_snapshot(report)
        original_bytes = snapshot.canonical_bytes
        report["coverage"]["observed_pairs"] = 0
        self.assertEqual(snapshot.canonical_bytes, original_bytes)
        envelope = json.loads(snapshot.canonical_bytes.decode("utf-8"))
        self.assertEqual(envelope["schema_version"], "2.0.0")
        self.assertEqual(envelope["payload_type"], "TGCV-C10S-VCONT-BENCHMARK-REPORT")
        temporal = envelope["report"]["temporal_manifest"][0]
        self.assertEqual(temporal["world_seed"],
                         {"$type": "uint64", "decimal": "18446744073709551615"})
        self.assertEqual(temporal["z_assignment_seed"],
                         {"$type": "uint64", "decimal": "9007199254740993"})
        nested = envelope["report"]["manifest"]["temporal_manifest"][0]
        self.assertEqual(temporal, nested)
        self.assertEqual(snapshot.sha256,
                         __import__("hashlib").sha256(snapshot.canonical_bytes).hexdigest())

    def test_report_snapshot_rejects_root_nested_manifest_disagreement(self):
        report = self.report_fixture()
        report["manifest"]["temporal_manifest"][0]["world_seed"] = 1
        normalized = json.loads(json.dumps(
            report["manifest"], default=lambda value: value.__dict__, sort_keys=True
        ))
        report["report_fingerprint"] = hashlib.sha256(json.dumps(
            normalized, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")).hexdigest()
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)


    def test_report_snapshot_rejects_tampered_legacy_fingerprint(self):
        report = self.report_fixture()
        report["report_fingerprint"] = "e" * 64
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)

    def test_report_snapshot_rejects_non_uint64_seed_and_unknown_top_level_field(self):
        report = self.report_fixture()
        report["temporal_manifest"][0]["world_seed"] = -1
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["temporal_manifest"][0]["z_assignment_seed"] = 1 << 64
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["temporal_manifest"][0]["g_assignment_seed"] = True
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)
        report = self.report_fixture()
        report["unexpected"] = True
        with self.assertRaises(ContractError):
            freeze_report_snapshot(report)

    def test_rfc8785_known_canonicalization_vectors(self):
        self.assertEqual(rfc8785.dumps({"b": 2, "a": 1}), b'{"a":1,"b":2}')
        self.assertEqual(
            rfc8785.dumps({"numbers": [333333333.33333329, 1e30, 4.50, 2e-3, 1e-27]}),
            b'{"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27]}',
        )
        self.assertEqual(rfc8785.dumps({"a": None, "b": []}), b'{"a":null,"b":[]}')

    def test_rfc8785_rejects_non_finite_numbers_and_unsafe_integers(self):
        with self.assertRaises(Exception):
            rfc8785.dumps({"x": math.nan})
        with self.assertRaises(Exception):
            rfc8785.dumps({"x": 9007199254740992})

    def test_three_argument_legacy_constructor_remains_compatible(self):
        captured = CapturedBenchmark({}, (), ())
        self.assertIsNone(captured.matrix_capture)
        self.assertIsNone(captured.report_snapshot)
        self.assertIsNone(captured.capture_id)
        self.assertIsNone(captured.benchmark_export_id)


if __name__ == "__main__":
    unittest.main()
