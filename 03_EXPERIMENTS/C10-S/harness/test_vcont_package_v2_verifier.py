"""Pure tests for the independent package-v2 verifier primitives."""
import unittest
import base64
import hashlib
import json

import rfc8785
from vcont_package_v2 import COMPANION_PATHS, GENERATED_COMPANION_PATHS
from vcont_package_v2_verify import (
    PACKAGE_PATHS,
    PackageVerificationError,
    _check_registered_uint64,
    _check_report,
    _safe_archive_path,
    _strict_json,
    _uint64,
    _historical_fingerprint,
    decode_frozen_snapshot_ref,
    _assert_snapshot_seed_relations,
    _logical_run_key,
    _reconcile_matrix_pair_ledger,
    _resolve_outer_world_run_reference,
    _assert_report_snapshot_projection,
    _register_unique_run_record,
    _assert_sealed_provenance_identity,
    AUTHORITATIVE_SCENARIO_IDS,
    AUTHORITATIVE_ESTIMAND_IDS,
    _reconcile_benchmark_export_identity,
    _reconcile_effective_scenario_config_rows,
    EFFECTIVE_CONFIG_STRUCTURAL_FIELDS,
    EFFECTIVE_CONFIG_SEED_POLICY,
    ANALYSIS_CONTRACTS_SCHEMA_ID,
    ANALYSIS_CONTRACTS_SCHEMA_VERSION,
    ANALYSIS_CONTRACT_BOOL_FIELDS,
    ANALYSIS_CONTRACT_NULLABLE_FIELDS,
    ANALYZER_VERSION,
    CONFIGURATION_FINGERPRINTS_SCHEMA_ID,
    CONFIGURATION_FINGERPRINTS_SCHEMA_VERSION,
    EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
    EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
    EFFECTIVE_CONFIG_SCHEMA_ID,
    EFFECTIVE_CONFIG_SCHEMA_VERSION,
    MATRIX_SCHEMA_ID,
    MATRIX_SCHEMA_VERSION,
    _SNAPSHOT_TYPE_FIELDS,
    _analysis_contract_payload_digest,
    _configuration_digest,
    _reconcile_configuration_companions
)


class IndependentVerifierPrimitiveTests(unittest.TestCase):
    def test_exact_fourteen_path_inventory_is_unique(self):
        self.assertEqual(len(PACKAGE_PATHS), 14)
        self.assertEqual(len(set(PACKAGE_PATHS)), 14)

    def test_strict_json_accepts_canonical_payload_with_one_lf(self):
        raw = rfc8785.dumps({"a": 1, "b": [True, None]}) + b"\n"
        value, canonical = _strict_json(raw, "fixture.json")
        self.assertEqual(value, {"a": 1, "b": [True, None]})
        self.assertEqual(canonical, raw[:-1])

    def test_strict_json_rejects_duplicate_keys(self):
        with self.assertRaises(PackageVerificationError):
            _strict_json(b'{"a":1,"a":2}\n', "duplicate.json")

    def test_strict_json_rejects_noncanonical_whitespace_and_missing_lf(self):
        for raw in (b'{ "a":1}\n', b'{"a":1}'):
            with self.subTest(raw=raw), self.assertRaises(PackageVerificationError):
                _strict_json(raw, "noncanonical.json")

    def test_strict_json_rejects_bom_and_nonfinite_constants(self):
        for raw in (b"\xef\xbb\xbf{}\n", b'{"x":NaN}\n'):
            with self.subTest(raw=raw), self.assertRaises(PackageVerificationError):
                _strict_json(raw, "invalid.json")

    def test_uint64_exact_boundary_roundtrips(self):
        for value in (0, (1 << 53) - 1, 1 << 53, (1 << 64) - 1):
            wrapper = {"$type": "uint64", "decimal": str(value)}
            self.assertEqual(_uint64(wrapper, "boundary"), value)

    def test_uint64_rejects_bool_float_and_noncanonical_decimal(self):
        invalid = (
            True, 1.0, -1, (1 << 64),
            {"$type": "uint64", "decimal": "00"},
            {"$type": "uint64", "decimal": "+1"},
            {"$type": "uint64", "decimal": "١"},
            {"$type": "uint64", "decimal": "1e2"},
            {"$type": "uint64", "decimal": "1", "extra": 0},
        )
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(PackageVerificationError):
                _uint64(value, "invalid")

    def test_archive_path_rejects_parent_absolute_and_backslash(self):
        for path in ("../escape", "/absolute", "a/../b", "a\\b", "a//b"):
            with self.subTest(path=path), self.assertRaises(PackageVerificationError):
                _safe_archive_path(path)

    def test_report_accepts_complete_legacy_fingerprint_and_duplicate_views(self):
        temporal = [
            {"world_seed": 10 + m, "z_assignment_seed": 20 + m, "g_assignment_seed": 30 + m}
            for _ in range(13) for m in range(2) for _r in range(2)
        ]
        pair_ledger = [
            {"contributions": [
                {"world_seed": 10 + m} for m in range(2)
            ]}
            for _ in range(52)
        ]
        manifest = {
            "scenario_versions": [[f"S{i:02d}", "v1"] for i in range(13)],
            "N": 1, "M": 2, "R": 1,
            "temporal_manifest": temporal,
            "pair_ledger": pair_ledger,
        }
        fingerprint = _historical_fingerprint(manifest)
        scenario_reports = {}
        for i in range(13):
            sid = f"S{i:02d}"
            scenario_reports[sid] = {
                "scenario_id": sid,
                "per_outer_replicate": [
                    {"outer_replicate_id": f"outer-{m:06d}", "run": [
                        {"seed": 100 + m}, {}, {},
                        {"world_seed": 10 + m, "z_assignment_seed": 20 + m, "g_assignment_seed": 30 + m},
                    ]}
                    for m in range(2)
                ],
            }
        report = {
            "manifest": manifest,
            "report_fingerprint": fingerprint,
            "temporal_manifest": temporal,
            "pair_ledger": pair_ledger,
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "scenario_reports": scenario_reports,
        }
        _check_report({
            "schema_id": "TGCV-C10S-VCONT-REPORT-SNAPSHOT",
            "schema_version": "2.1.0",
            "payload_type": "TGCV-C10S-VCONT-BENCHMARK-REPORT",
            "legacy_report_fingerprint": fingerprint,
            "legacy_fingerprint_algorithm": "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1",
            "report": report,
        })

    def test_report_rejects_root_nested_manifest_divergence(self):
        fingerprint = _historical_fingerprint({"temporal_manifest": [], "pair_ledger": []})
        report = {
            "manifest": {"temporal_manifest": [], "pair_ledger": []},
            "report_fingerprint": fingerprint,
            "temporal_manifest": [{"run_id": "different"}],
            "pair_ledger": [],
            "coverage": {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13},
            "scenario_reports": {},
        }
        with self.assertRaises(PackageVerificationError):
            _check_report({
                "schema_id": "TGCV-C10S-VCONT-REPORT-SNAPSHOT",
                "schema_version": "2.1.0",
                "payload_type": "TGCV-C10S-VCONT-BENCHMARK-REPORT",
                "legacy_report_fingerprint": fingerprint,
                "legacy_fingerprint_algorithm": "legacy",
                "report": report,
            })

    def test_registered_seed_pointers_require_typed_wrappers(self):
        wrapper = {"$type": "uint64", "decimal": "0"}
        files = {
            "seeds/evaluation_seed_assignments.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "seeds/calibration_seed_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "runs/temporal_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
            }]},
            "report/report.json": {"report": {
                "temporal_manifest": [{"world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper}],
                "manifest": {
                    "temporal_manifest": [{"world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper}],
                    "pair_ledger": [{"contributions": [{"world_seed": wrapper}]}],
                },
                "pair_ledger": [{"contributions": [{"world_seed": wrapper}]}],
                "scenario_reports": {
                    "S": {"per_outer_replicate": [{"run": [
                        {"seed": wrapper}, {}, {}, {
                            "world_seed": wrapper, "z_assignment_seed": wrapper, "g_assignment_seed": wrapper,
                        }
                    ]}]}
                },
            }},
            "runs/run_records.json": {"outer_world_evidence_records": [{"key": {"world_seed": wrapper}}]},
        }
        counts = _check_registered_uint64(files)
        self.assertEqual(len(counts), 5)
        self.assertTrue(all(count > 0 for count in counts))

    def test_unregistered_uint64_wrapper_is_rejected(self):
        files = {
            "seeds/evaluation_seed_assignments.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "seeds/calibration_seed_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "runs/temporal_manifest.json": {"row_count": 1, "rows": [{
                "world_seed": {"$type": "uint64", "decimal": "0"},
                "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                "g_assignment_seed": {"$type": "uint64", "decimal": "2"},
            }]},
            "report/report.json": {"report": {
                "temporal_manifest": [{"world_seed": {"$type": "uint64", "decimal": "0"},
                                       "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                                       "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}],
                "manifest": {
                    "temporal_manifest": [{"world_seed": {"$type": "uint64", "decimal": "0"},
                                           "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                                           "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}],
                    "pair_ledger": [{"contributions": [{"world_seed": {"$type": "uint64", "decimal": "0"}}]}],
                },
                "pair_ledger": [{"contributions": [{"world_seed": {"$type": "uint64", "decimal": "0"}}]}],
                "scenario_reports": {"S": {"per_outer_replicate": [{"run": [
                    {"seed": {"$type": "uint64", "decimal": "0"}}, {}, {},
                    {"world_seed": {"$type": "uint64", "decimal": "0"},
                     "z_assignment_seed": {"$type": "uint64", "decimal": "1"},
                     "g_assignment_seed": {"$type": "uint64", "decimal": "2"}}
                ]}]}},
                "unexpected": {"seed": {"$type": "uint64", "decimal": "7"}},
            }},
            "runs/run_records.json": {"outer_world_evidence_records": [{"key": {"world_seed": {"$type": "uint64", "decimal": "0"}}}]},
        }
        with self.assertRaises(PackageVerificationError):
            _check_registered_uint64(files)


    def _seed_assignment_snapshot_ref(self):
        type_id = "vcont_benchmark_protocol.SeedAssignment"
        payload = {
            "$dataclass": type_id,
            "fields": {
                "bank": "evaluation",
                "scenario_id": "S01",
                "n_units": 700,
                "replicate": -1,
                "world_seed": 111,
                "z_assignment_seed": 222,
                "g_assignment_seed": 333,
                "scenario_version": "v1",
                "outer_replicate_id": "outer-000000",
                "assignment_role": "RUN",
            },
        }
        raw = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        return {
            "type_id": type_id,
            "encoding": "base64",
            "media_type": "application/vnd.tgcv.typed-snapshot+json",
            "serialization_id": "TGCV-FROZEN-SNAPSHOT-1",
            "canonical_bytes_base64": base64.b64encode(raw).decode("ascii"),
            "sha256": hashlib.sha256(raw).hexdigest(),
        }

    def test_frozen_snapshot_decoder_accepts_exact_seed_assignment(self):
        reference = self._seed_assignment_snapshot_ref()
        decoded = decode_frozen_snapshot_ref(
            reference, expected_type_id="vcont_benchmark_protocol.SeedAssignment"
        )
        self.assertEqual(decoded.type_id, reference["type_id"])
        self.assertEqual(decoded.serialization_id, "TGCV-FROZEN-SNAPSHOT-1")
        self.assertEqual(decoded.canonical_bytes, base64.b64decode(reference["canonical_bytes_base64"]))
        self.assertEqual(decoded.sha256, reference["sha256"])

    def test_frozen_snapshot_decoder_rejects_digest_and_root_type_divergence(self):
        reference = self._seed_assignment_snapshot_ref()
        bad_digest = dict(reference, sha256="0" * 64)
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(bad_digest)
        bad_type = dict(reference, type_id="vcont_integrated_harness.TruthBundle")
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(bad_type)

    def test_frozen_snapshot_decoder_rejects_missing_fields_and_bad_base64(self):
        reference = self._seed_assignment_snapshot_ref()
        raw = base64.b64decode(reference["canonical_bytes_base64"])
        payload = json.loads(raw.decode("utf-8"))
        del payload["fields"]["world_seed"]
        changed = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        malformed = dict(
            reference,
            canonical_bytes_base64=base64.b64encode(changed).decode("ascii"),
            sha256=hashlib.sha256(changed).hexdigest(),
        )
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(malformed)
        bad_base64 = dict(reference, canonical_bytes_base64="%%%")
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(bad_base64)

    def test_frozen_snapshot_decoder_rejects_duplicate_keys_and_unknown_tags(self):
        duplicate = b'{"$dataclass":"vcont_benchmark_protocol.SeedAssignment","fields":{},"fields":{}}'
        duplicate_ref = self._seed_assignment_snapshot_ref()
        duplicate_ref["canonical_bytes_base64"] = base64.b64encode(duplicate).decode("ascii")
        duplicate_ref["sha256"] = hashlib.sha256(duplicate).hexdigest()
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(duplicate_ref)

        reference = self._seed_assignment_snapshot_ref()
        raw = base64.b64decode(reference["canonical_bytes_base64"])
        payload = json.loads(raw.decode("utf-8"))
        payload["fields"]["scenario_id"] = {"$mystery": "S01"}
        changed = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        malformed = dict(
            reference,
            canonical_bytes_base64=base64.b64encode(changed).decode("ascii"),
            sha256=hashlib.sha256(changed).hexdigest(),
        )
        with self.assertRaises(PackageVerificationError):
            decode_frozen_snapshot_ref(malformed)



    def test_seed_domains_remain_distinct_when_truth_seed_differs_from_world_seed(self):
        assignment = {
            "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        config = {
            "seed": 17, "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        manifest = {
            "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        truth_projection = {"seed": 17}
        _assert_snapshot_seed_relations(assignment, config, manifest, truth_projection)
        self.assertNotEqual(truth_projection["seed"], manifest["world_seed"])

    def test_seed_domain_reconciliation_rejects_truth_config_and_stream_divergence(self):
        assignment = {
            "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        config = {
            "seed": 17, "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        manifest = {
            "world_seed": 101, "z_assignment_seed": 202, "g_assignment_seed": 303,
        }
        with self.assertRaises(PackageVerificationError):
            _assert_snapshot_seed_relations(assignment, config, manifest, {"seed": 101})
        with self.assertRaises(PackageVerificationError):
            _assert_snapshot_seed_relations(
                assignment, dict(config, z_assignment_seed=999), manifest, {"seed": 17}
            )
        with self.assertRaises(PackageVerificationError):
            _assert_snapshot_seed_relations(
                assignment, config, dict(manifest, g_assignment_seed=999), {"seed": 17}
            )

    def test_logical_run_key_rejects_noncanonical_role_index_and_extra_fields(self):
        valid = {
            "scenario_id": "S01", "scenario_version": "v1", "N": 700,
            "outer_replicate_id": "outer-000000", "assignment_role": "RUN",
            "assignment_index": -1, "run_id": "run-001",
        }
        self.assertEqual(_logical_run_key(valid, "fixture")[-1], "run-001")
        with self.assertRaises(PackageVerificationError):
            _logical_run_key(dict(valid, assignment_index=0), "bad-run-index")
        with self.assertRaises(PackageVerificationError):
            _logical_run_key(dict(valid, unexpected="field"), "extra-field")



    def _matrix_pair_fixture(self):
        matrix_rows = []
        pair_rows = []
        for scenario_index, sid in enumerate(AUTHORITATIVE_SCENARIO_IDS):
            for estimand_index, estimand_id in enumerate(AUTHORITATIVE_ESTIMAND_IDS):
                estimand_version = "001"
                evaluation_class = ("EVALUABLE", "STATUS_ONLY", "NOT_IDENTIFIABLE", "NOT_EVALUABLE")[estimand_index]
                truth_status = ("DEFINED", "UNDEFINED", "NOT_MATERIALIZED", "DEFINED")[estimand_index]
                matrix_rows.append({
                    "key": {
                        "scenario_id": sid, "scenario_version": "v1",
                        "estimand_id": estimand_id, "estimand_version": estimand_version,
                    },
                    "evaluation_class": evaluation_class,
                    "truth_status": truth_status,
                    "dgp_truth_field": "truth",
                    "analyzer_output_field": "estimate",
                    "aggregation_field": "mean",
                    "identification_expectation": "IDENTIFIED",
                    "abstention_expectation": False,
                    "tolerance_id": "TOL-001",
                    "reason": "fixture",
                    "run_evaluation_class": evaluation_class,
                    "repeated_evaluation_class": evaluation_class,
                })
                pair_rows.append({
                    "key": [sid, "v1", estimand_id, estimand_version, "MONTE_CARLO"],
                    "evaluation_class": evaluation_class,
                    "truth_status": truth_status,
                })
        scenario_versions = [[sid, "v1"] for sid in AUTHORITATIVE_SCENARIO_IDS]
        return {"rows": matrix_rows}, {
            "report": {"design": {"scenario_versions": scenario_versions}, "pair_ledger": pair_rows}
        }

    def test_matrix_capture_and_pair_ledger_exact_52_pair_join(self):
        matrix, report = self._matrix_pair_fixture()
        _reconcile_matrix_pair_ledger(matrix, report)

    def test_matrix_pair_join_rejects_wrong_scenario_estimand_version_and_order(self):
        mutations = (
            lambda row: row["key"].__setitem__(0, "S99"),
            lambda row: row["key"].__setitem__(2, "E99"),
            lambda row: row["key"].__setitem__(3, "999"),
        )
        for mutate in mutations:
            matrix, report = self._matrix_pair_fixture()
            mutate(report["report"]["pair_ledger"][0])
            with self.subTest(mutate=mutate), self.assertRaises(PackageVerificationError):
                _reconcile_matrix_pair_ledger(matrix, report)
        matrix, report = self._matrix_pair_fixture()
        report["report"]["pair_ledger"][0], report["report"]["pair_ledger"][1] = (
            report["report"]["pair_ledger"][1], report["report"]["pair_ledger"][0]
        )
        with self.assertRaises(PackageVerificationError):
            _reconcile_matrix_pair_ledger(matrix, report)

    def test_matrix_pair_join_rejects_classification_drift_and_duplicate_identity(self):
        matrix, report = self._matrix_pair_fixture()
        report["report"]["pair_ledger"][0]["evaluation_class"] = "NOT_EVALUABLE"
        with self.assertRaises(PackageVerificationError):
            _reconcile_matrix_pair_ledger(matrix, report)
        matrix, report = self._matrix_pair_fixture()
        matrix["rows"][1]["key"] = dict(matrix["rows"][0]["key"])
        with self.assertRaises(PackageVerificationError):
            _reconcile_matrix_pair_ledger(matrix, report)



    def _outer_world_reference_fixture(self):
        base = ("S01", "v1", 700, "outer-000000")
        run_key = (*base, "RUN", -1, "run-designated")
        repeated_key = (*base, "REPEATED_ASSIGNMENT", 0, "run-repeat-0")
        run_map = {run_key: {"record": "designated"}, repeated_key: {"record": "repeat"}}
        decoded = {
            run_key: {"run_manifest": {
                "run_id": "run-designated", "world_id": "world-01",
                "world_version": "v1", "world_seed": 101,
            }},
            repeated_key: {"run_manifest": {
                "run_id": "run-repeat-0", "world_id": "world-01",
                "world_version": "v1", "world_seed": 101,
            }},
        }
        return base, run_key, repeated_key, run_map, decoded, ("world-01", "v1", 101)

    def test_outer_world_reference_resolves_exact_designated_run_and_repetition(self):
        base, run_key, repeated_key, run_map, decoded, world = self._outer_world_reference_fixture()
        resolved, manifest = _resolve_outer_world_run_reference(
            dict(zip(
                ("scenario_id", "scenario_version", "N", "outer_replicate_id",
                 "assignment_role", "assignment_index", "run_id"), run_key
            )),
            "designated", base, "RUN", -1, run_map, decoded, world,
        )
        self.assertEqual(resolved, run_key)
        self.assertEqual(manifest["run_id"], "run-designated")
        repeated, _ = _resolve_outer_world_run_reference(
            dict(zip(
                ("scenario_id", "scenario_version", "N", "outer_replicate_id",
                 "assignment_role", "assignment_index", "run_id"), repeated_key
            )),
            "repeated", base, "REPEATED_ASSIGNMENT", 0, run_map, decoded, world,
        )
        self.assertEqual(repeated, repeated_key)

    def test_outer_world_reference_rejects_cross_world_and_run_id_divergence(self):
        base, run_key, _, run_map, decoded, world = self._outer_world_reference_fixture()
        ref = dict(zip(
            ("scenario_id", "scenario_version", "N", "outer_replicate_id",
             "assignment_role", "assignment_index", "run_id"), run_key
        ))
        decoded[run_key]["run_manifest"]["world_id"] = "world-OTHER"
        with self.assertRaises(PackageVerificationError):
            _resolve_outer_world_run_reference(
                ref, "cross-world", base, "RUN", -1, run_map, decoded, world
            )
        decoded[run_key]["run_manifest"]["world_id"] = "world-01"
        decoded[run_key]["run_manifest"]["run_id"] = "run-diverged"
        with self.assertRaises(PackageVerificationError):
            _resolve_outer_world_run_reference(
                ref, "run-id-divergence", base, "RUN", -1, run_map, decoded, world
            )

    def test_outer_world_reference_rejects_repetition_mapped_to_designated_run(self):
        base, run_key, _, run_map, decoded, world = self._outer_world_reference_fixture()
        ref = dict(zip(
            ("scenario_id", "scenario_version", "N", "outer_replicate_id",
             "assignment_role", "assignment_index", "run_id"), run_key
        ))
        with self.assertRaises(PackageVerificationError):
            _resolve_outer_world_run_reference(
                ref, "repeated-as-run", base, "REPEATED_ASSIGNMENT", 0,
                run_map, decoded, world,
            )

    def test_outer_world_reference_rejects_orphaned_run(self):
        base, run_key, _, _, decoded, world = self._outer_world_reference_fixture()
        ref = dict(zip(
            ("scenario_id", "scenario_version", "N", "outer_replicate_id",
             "assignment_role", "assignment_index", "run_id"), run_key
        ))
        with self.assertRaises(PackageVerificationError):
            _resolve_outer_world_run_reference(
                ref, "orphan", base, "RUN", -1, {}, decoded, world
            )



    def test_duplicate_logical_run_key_is_rejected_at_registration(self):
        run_map, decoded = {}, {}
        key = ("S01", "v1", 700, "outer-000000", "RUN", -1, "run-1")
        _register_unique_run_record(run_map, decoded, key, {"record": 1}, {"snapshot": 1})
        with self.assertRaises(PackageVerificationError):
            _register_unique_run_record(run_map, decoded, key, {"record": 2}, {"snapshot": 2})

    def test_structurally_valid_but_semantically_false_report_projection_is_rejected(self):
        captured = {
            "run_id": "run-1",
            "estimate": 1.25,
            "diagnostics": ("ok", "stable"),
        }
        valid_projection = {
            "run_id": "run-1",
            "estimate": 1.25,
            "diagnostics": ["ok", "stable"],
        }
        false_projection = {
            "run_id": "run-OTHER",
            "estimate": 1.25,
            "diagnostics": ["ok", "stable"],
        }
        _assert_report_snapshot_projection(valid_projection, captured, "positive fixture")
        with self.assertRaises(PackageVerificationError):
            _assert_report_snapshot_projection(false_projection, captured, "false provenance fixture")



    def _sealed_provenance_fixture(self):
        assignment = {
            "outer_replicate_id": "outer-000000",
            "assignment_role": "RUN",
            "replicate": -1,
        }
        config = {
            "scenario_id": "S01", "version": "v1", "replicate_id": "replicate-000",
        }
        manifest = {
            "world_id": "world-01", "world_version": "v1",
            "g_assignment_mechanism_id": "G-MECH",
            "g_assignment_mechanism_version": "1",
            "g_assignment_mechanism_hash": "g-hash",
            "z_assignment_mechanism_id": "Z-MECH",
            "z_assignment_mechanism_version": "1",
            "z_assignment_mechanism_hash": "z-hash",
            "g_reference_regime_id": "G-REF",
            "g_reference_regime_version": "1",
            "z_assignment_vector_hash": "z-vector",
            "g_assignment_vector_hash": "g-vector",
        }
        provenance = {
            "run_id": "run-1",
            "scenario_id": "S01",
            "scenario_version": "v1",
            "world_id": "world-01",
            "world_version": "v1",
            "replicate_id": "replicate-000",
            "outer_replicate_id": "outer-000000",
            "assignment_role": "RUN",
            "assignment_index": -1,
            "g_assignment_mechanism_id": "G-MECH",
            "g_assignment_mechanism_version": "1",
            "g_assignment_mechanism_hash": "g-hash",
            "z_assignment_mechanism_id": "Z-MECH",
            "z_assignment_mechanism_version": "1",
            "z_assignment_mechanism_hash": "z-hash",
            "g_reference_regime_id": "G-REF",
            "g_reference_regime_version": "1",
            "z_assignment_vector_hash": "z-vector",
            "g_assignment_vector_hash": "g-vector",
        }
        digest = hashlib.sha256(json.dumps(
            provenance, sort_keys=True, separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")).hexdigest()
        manifest["provenance_sha256"] = digest
        analyzer = {"provenance_sha256": digest}
        return assignment, config, manifest, provenance, analyzer

    def test_sealed_provenance_is_bound_to_run_manifest_and_analyzer(self):
        assignment, config, manifest, provenance, analyzer = self._sealed_provenance_fixture()
        digest = _assert_sealed_provenance_identity(
            provenance, "run-1", assignment, config, manifest, analyzer
        )
        self.assertEqual(digest, analyzer["provenance_sha256"])

    def test_sealed_provenance_rejects_cross_world_and_wrong_run_identity(self):
        assignment, config, manifest, provenance, analyzer = self._sealed_provenance_fixture()
        with self.assertRaises(PackageVerificationError):
            _assert_sealed_provenance_identity(
                dict(provenance, world_id="world-OTHER"),
                "run-1", assignment, config, manifest, analyzer,
            )
        with self.assertRaises(PackageVerificationError):
            _assert_sealed_provenance_identity(
                provenance, "run-OTHER", assignment, config, manifest, analyzer,
            )

    def test_sealed_provenance_rejects_analyzer_digest_divergence(self):
        assignment, config, manifest, provenance, analyzer = self._sealed_provenance_fixture()
        with self.assertRaises(PackageVerificationError):
            _assert_sealed_provenance_identity(
                provenance, "run-1", assignment, config, manifest,
                dict(analyzer, provenance_sha256="0" * 64),
            )



    def _benchmark_export_identity_fixture(self):
        export_id = "a" * 64
        return {
            "runs/run_records.json": {
                "schema_id": "TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE",
                "schema_version": "2.0.0",
                "benchmark_export_id": export_id,
            },
            "validation/reconciliation_results.json": {
                "schema_id": "TGCV-C10S-VCONT-GATE159-RECONCILIATION",
                "schema_version": "1.0.0",
                "benchmark_export_id": export_id,
            },
        }

    def test_benchmark_export_id_matches_between_run_and_gate159_companions(self):
        files = self._benchmark_export_identity_fixture()
        self.assertEqual(_reconcile_benchmark_export_identity(files), "a" * 64)

    def test_benchmark_export_id_reconciliation_rejects_gate159_divergence(self):
        files = self._benchmark_export_identity_fixture()
        files["validation/reconciliation_results.json"]["benchmark_export_id"] = "b" * 64
        with self.assertRaises(PackageVerificationError):
            _reconcile_benchmark_export_identity(files)

    def test_benchmark_export_id_reconciliation_rejects_malformed_or_missing_identity(self):
        files = self._benchmark_export_identity_fixture()
        files["runs/run_records.json"]["benchmark_export_id"] = "A" * 64
        with self.assertRaises(PackageVerificationError):
            _reconcile_benchmark_export_identity(files)
        files = self._benchmark_export_identity_fixture()
        del files["validation/reconciliation_results.json"]["benchmark_export_id"]
        with self.assertRaises(PackageVerificationError):
            _reconcile_benchmark_export_identity(files)

    def test_benchmark_export_id_reconciliation_rejects_wrong_gate159_contract(self):
        files = self._benchmark_export_identity_fixture()
        files["validation/reconciliation_results.json"]["schema_version"] = "2.0.0"
        with self.assertRaises(PackageVerificationError):
            _reconcile_benchmark_export_identity(files)



    def _effective_config_fixture(self):
        design = {
            "scenario_versions": [[sid, "v1"] for sid in AUTHORITATIVE_SCENARIO_IDS],
            "n_units": 20, "outer_replicates": 2, "repeated_assignments": 1,
        }
        rows = []
        decoded_runs = []
        for scenario_index, sid in enumerate(AUTHORITATIVE_SCENARIO_IDS):
            projection = {
                name: (
                    f"value-{scenario_index}" if name in {"profile", "mechanism"}
                    else False if name in {
                        "randomized_z", "randomized_g", "positivity", "no_interference",
                        "measurement_identified", "version_consistency",
                    }
                    else float(scenario_index + 1) if name in {
                        "window_start", "last_transition_support", "follow_up",
                        "enabled_probability", "baseline_conformity", "focal_access_effect",
                        "package_direct_effect", "focal_direct_effect", "collateral_effect",
                        "provision_probability", "alternative_probability", "heterogeneity",
                        "interference_effect", "measurement_sensitivity",
                        "measurement_specificity", "missing_probability", "zg_interaction_effect",
                    }
                    else 5
                )
                for name in EFFECTIVE_CONFIG_STRUCTURAL_FIELDS
            }
            rows.append({
                "scenario_id": sid, "scenario_version": "v1", "n_units": 20,
                "generator_version": "generator-v1",
                "seed_policy": dict(EFFECTIVE_CONFIG_SEED_POLICY),
                "config": projection,
            })
            for m in range(2):
                for role, index in [("RUN", -1), ("REPEATED_ASSIGNMENT", 0)]:
                    key = (sid, "v1", 20, f"outer-{m:06d}", role, index,
                           f"run-{scenario_index:02d}-{m:06d}-{role}-{index}")
                    config = {
                        "scenario_id": sid, "version": "v1", "n_units": 20,
                        **projection,
                        "seed": 1000 + scenario_index + m,
                        "world_seed": 2000 + scenario_index + m,
                        "z_assignment_seed": 3000 + scenario_index + m,
                        "g_assignment_seed": 4000 + scenario_index + m,
                        "replicate_id": f"rep-{scenario_index}-{m}-{index}",
                        "outer_replicate_id": f"outer-{m:06d}",
                        "assignment_role": role, "assignment_index": index,
                    }
                    decoded_runs.append({
                        "key": key, "config": config, "generator_version": "generator-v1",
                    })
        effective = {
            "schema_id": "TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION",
            "schema_version": "2.0.0",
            "rows": rows,
        }
        return effective, design, decoded_runs

    def test_effective_config_rows_join_to_every_run_repetition_snapshot(self):
        effective, design, decoded_runs = self._effective_config_fixture()
        self.assertEqual(
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs), 13
        )

    def test_effective_config_rejects_structural_snapshot_drift(self):
        effective, design, decoded_runs = self._effective_config_fixture()
        decoded_runs[0]["config"]["focal_access_effect"] = 999.0
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)

    def test_effective_config_rejects_seed_or_run_identity_in_structural_projection(self):
        effective, design, decoded_runs = self._effective_config_fixture()
        effective["rows"][0]["config"]["world_seed"] = 1
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)
        effective, design, decoded_runs = self._effective_config_fixture()
        effective["rows"][0]["seed_policy"]["fallback"] = "ALLOW"
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)

    def test_effective_config_rejects_generator_version_divergence(self):
        effective, design, decoded_runs = self._effective_config_fixture()
        decoded_runs[0]["generator_version"] = "generator-other"
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)

    def test_effective_config_rejects_wrong_order_duplicate_and_missing_run_consumption(self):
        effective, design, decoded_runs = self._effective_config_fixture()
        effective["rows"][0], effective["rows"][1] = effective["rows"][1], effective["rows"][0]
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)
        effective, design, decoded_runs = self._effective_config_fixture()
        effective["rows"][1] = dict(effective["rows"][0])
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)
        effective, design, decoded_runs = self._effective_config_fixture()
        decoded_runs.pop()
        with self.assertRaises(PackageVerificationError):
            _reconcile_effective_scenario_config_rows(effective, design, decoded_runs)



if __name__ == "__main__":
    unittest.main()


def _contract_payload():
    names = _SNAPSHOT_TYPE_FIELDS["vcont_integrated_harness.AnalysisContract"]
    return {
        name: (False if name in ANALYSIS_CONTRACT_BOOL_FIELDS
               else None if name in ANALYSIS_CONTRACT_NULLABLE_FIELDS
               else "source-value")
        for name in names
    }


def _snapshot_ref(contract):
    tagged = {
        "$dataclass": "vcont_integrated_harness.AnalysisContract",
        "fields": contract,
    }
    raw = json.dumps(
        tagged, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")
    return {
        "type_id": "vcont_integrated_harness.AnalysisContract",
        "encoding": "base64",
        "media_type": "application/vnd.tgcv.typed-snapshot+json",
        "serialization_id": "TGCV-FROZEN-SNAPSHOT-1",
        "canonical_bytes_base64": base64.b64encode(raw).decode("ascii"),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def _fixture():
    export_id = "a" * 64
    n_units, M, R = 25, 1, 1
    versions = [(sid, "v1") for sid in AUTHORITATIVE_SCENARIO_IDS]
    source_rows, applicability, run_records = [], [], []
    contracts = {}
    for s, (sid, version) in enumerate(versions):
        contract = _contract_payload()
        contracts[sid] = contract
        digest = _analysis_contract_payload_digest(
            sid, version, n_units, ANALYZER_VERSION, contract
        )
        source_rows.append({
            "scenario_id": sid,
            "scenario_version": version,
            "n_units": n_units,
            "analyzer_version": ANALYZER_VERSION,
            "analysis_contract": contract,
            "contract_payload_digest": digest,
        })
        for family in ("RUN", "REPEATED_ASSIGNMENT"):
            applicability.append({
                "scenario_id": sid,
                "scenario_version": version,
                "n_units": n_units,
                "run_family": family,
                "contract_payload_digest": digest,
            })
        for role, assignment_index in (("RUN", -1), ("REPEATED_ASSIGNMENT", 0)):
            run_id = f"run-{s:02d}-{role}"
            run_records.append({
                "key": {
                    "scenario_id": sid,
                    "scenario_version": version,
                    "N": n_units,
                    "outer_replicate_id": "outer-000000",
                    "assignment_role": role,
                    "assignment_index": assignment_index,
                    "run_id": run_id,
                },
                "analysis_contract_sha256": _snapshot_ref(contract)["sha256"],
                "snapshot_refs": {"analysis_contract": _snapshot_ref(contract)},
            })

    effective_rows = []
    for sid, version in versions:
        effective_rows.append({
            "scenario_id": sid,
            "scenario_version": version,
            "n_units": n_units,
            "generator_version": "c10s-vcont-generator-0.1",
            "seed_policy": {
                "mode": "EXPLICIT_ASSIGNMENT_STREAMS_REQUIRED",
                "source": "SeedAssignment",
                "streams": ["world_seed", "z_assignment_seed", "g_assignment_seed"],
                "fallback": "FORBIDDEN",
                "algorithm": "TGCV-C10S-VCONT-SEED-v3",
            },
            "config": {},
        })
    effective = {
        "schema_id": EFFECTIVE_CONFIG_SCHEMA_ID,
        "schema_version": EFFECTIVE_CONFIG_SCHEMA_VERSION,
        "rows": effective_rows,
    }
    matrix_rows = [{"row_id": f"matrix-{i}"} for i in range(52)]
    matrix = {
        "schema_id": MATRIX_SCHEMA_ID,
        "schema_version": MATRIX_SCHEMA_VERSION,
        "row_count": 52,
        "rows": matrix_rows,
    }
    matrix["full_matrix_sha256"] = _configuration_digest({
        "schema_id": MATRIX_SCHEMA_ID,
        "schema_version": MATRIX_SCHEMA_VERSION,
        "row_count": 52,
        "rows": matrix_rows,
    })
    assignment_rows = []
    legacy_seed_rows = []
    for s, (sid, version) in enumerate(versions):
        world_seed = 1000 + s
        for role, replicate in (("RUN", -1), ("REPEATED_ASSIGNMENT", 0)):
            z_seed = 2000 + 2 * s + (0 if role == "RUN" else 1)
            g_seed = 3000 + 2 * s + (0 if role == "RUN" else 1)
            source_row = {
                "bank": "evaluation",
                "scenario_id": sid,
                "scenario_version": version,
                "n_units": n_units,
                "replicate": replicate,
                "outer_replicate_id": "outer-000000",
                "assignment_role": role,
                "world_seed": world_seed,
                "z_assignment_seed": z_seed,
                "g_assignment_seed": g_seed,
            }
            legacy_seed_rows.append(source_row)
            assignment_rows.append({
                **{key: value for key, value in source_row.items()
                   if key not in {"world_seed", "z_assignment_seed", "g_assignment_seed"}},
                "world_seed": {"$type": "uint64", "decimal": str(world_seed)},
                "z_assignment_seed": {"$type": "uint64", "decimal": str(z_seed)},
                "g_assignment_seed": {"$type": "uint64", "decimal": str(g_seed)},
            })
    legacy_seed_fingerprint = hashlib.sha256(
        json.dumps(legacy_seed_rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assignments = {
        "schema_id": "TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS",
        "schema_version": "2.0.0",
        "bank": "evaluation",
        "row_count": len(assignment_rows),
        "rows": assignment_rows,
    }
    contract_file = {
        "schema_id": ANALYSIS_CONTRACTS_SCHEMA_ID,
        "schema_version": ANALYSIS_CONTRACTS_SCHEMA_VERSION,
        "benchmark_export_id": export_id,
        "source_contracts": source_rows,
        "applicability": applicability,
    }
    components = []
    for i, row in enumerate(effective_rows):
        sid, version = row["scenario_id"], row["scenario_version"]
        components.append({
            "component_id": f"dgp-generator:{sid}:{version}:{n_units}",
            "component_type": "DGP_GENERATOR_CONFIG",
            "scope_key": [sid, version, n_units],
            "source_ref": f"design/effective_scenario_configs.json#/rows/{i}",
            "payload_schema_id": EFFECTIVE_CONFIG_SCHEMA_ID,
            "payload_schema_version": EFFECTIVE_CONFIG_SCHEMA_VERSION,
            "algorithm_id": "TGCV-C10S-EFFECTIVE-SCENARIO-CONFIG-JCS-SHA256-1",
            "digest_sha256": _configuration_digest(row),
        })
    for i, row in enumerate(source_rows):
        run_index = i * (1 + R)
        components.append({
            "component_id": f"analyzer-contract:{row['scenario_id']}:{row['scenario_version']}:{n_units}",
            "component_type": "ANALYZER_EFFECTIVE_CONTRACT",
            "scope_key": [row["scenario_id"], row["scenario_version"], n_units],
            "source_ref": f"runs/run_records.json#/run_evidence_records/{run_index}/snapshot_refs/analysis_contract",
            "payload_schema_id": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
            "payload_schema_version": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
            "algorithm_id": "TGCV-C10S-ANALYSIS-CONTRACT-PAYLOAD-JCS-SHA256-1",
            "digest_sha256": row["contract_payload_digest"],
        })
    components.append({
        "component_id": "scenario-estimand-matrix",
        "component_type": "SCENARIO_ESTIMAND_MATRIX",
        "scope_key": export_id,
        "source_ref": "design/scenario_estimand_matrix.json#",
        "payload_schema_id": MATRIX_SCHEMA_ID,
        "payload_schema_version": MATRIX_SCHEMA_VERSION,
        "algorithm_id": "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1",
        "digest_sha256": matrix["full_matrix_sha256"],
    })
    components.append({
        "component_id": "evaluation-seed-bank",
        "component_type": "EVALUATION_SEED_BANK",
        "scope_key": export_id,
        "source_ref": "seeds/evaluation_seed_assignments.json#/rows",
        "payload_schema_id": assignments["schema_id"],
        "payload_schema_version": assignments["schema_version"],
        "algorithm_id": "TGCV-C10S-EVALUATION-ASSIGNMENT-MANIFEST-JCS-SHA256-1",
        "digest_sha256": _configuration_digest({"rows": assignment_rows}),
    })
    aggregate_input = {
        "schema_id": "TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT",
        "schema_version": "1.0.0",
        "components": [{
            name: row[name] for name in (
                "component_id", "component_type", "scope_key", "payload_schema_id",
                "payload_schema_version", "algorithm_id", "digest_sha256"
            )
        } for row in components],
    }
    aggregate_digest = _configuration_digest(aggregate_input)
    fingerprints = {
        "schema_id": CONFIGURATION_FINGERPRINTS_SCHEMA_ID,
        "schema_version": CONFIGURATION_FINGERPRINTS_SCHEMA_VERSION,
        "benchmark_export_id": export_id,
        "components": components,
        "aggregate": {
            "algorithm_id": "TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT-JCS-SHA256-1",
            "digest_sha256": aggregate_digest,
            "source_design_declaration": "design/benchmark_design.json#/configuration_fingerprint",
        },
    }
    report_design = {
        "scenario_versions": [[sid, version] for sid, version in versions],
        "n_units": n_units,
        "outer_replicates": M,
        "repeated_assignments": R,
        "configuration_fingerprint": aggregate_digest,
        "seed_bank_fingerprint": legacy_seed_fingerprint,
    }
    files = {
        "runs/run_records.json": {
            "benchmark_export_id": export_id,
            "run_evidence_records": run_records,
        },
        "design/analysis_contracts.json": contract_file,
        "provenance/configuration_fingerprints.json": fingerprints,
        "design/effective_scenario_configs.json": effective,
        "seeds/evaluation_seed_assignments.json": assignments,
        "design/benchmark_design.json": {
            "configuration_fingerprint": aggregate_digest,
            "seed_bank_fingerprint": legacy_seed_fingerprint,
        },
    }
    decoded_report = {"report": {"design": report_design}}
    return files, decoded_report, matrix


class ConfigurationCompanionVerifierTests(unittest.TestCase):
    def test_positive_13_26_28_reconciliation(self):
        files, report, matrix = _fixture()
        self.assertEqual(_reconcile_configuration_companions(files, report, matrix), (13, 26, 28))

    def test_writer_generates_both_configuration_companions(self):
        self.assertEqual(
            GENERATED_COMPANION_PATHS,
            frozenset({
                "design/analysis_contracts.json",
                "provenance/configuration_fingerprints.json",
            }),
        )
        self.assertTrue(GENERATED_COMPANION_PATHS.isdisjoint(COMPANION_PATHS))

    def test_rejects_twelve_source_contract_rows(self):
        files, report, matrix = _fixture()
        files["design/analysis_contracts.json"]["source_contracts"].pop()
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_run_snapshot_crossed_to_another_scenario(self):
        files, report, matrix = _fixture()
        files["runs/run_records.json"]["run_evidence_records"][0]["key"]["scenario_id"] = (
            AUTHORITATIVE_SCENARIO_IDS[1]
        )
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_analyzer_version_drift(self):
        files, report, matrix = _fixture()
        files["design/analysis_contracts.json"]["source_contracts"][0]["analyzer_version"] = "other-version"
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_matrix_digest_drift(self):
        files, report, matrix = _fixture()
        matrix["full_matrix_sha256"] = "0" * 64
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_missing_applicability_relation(self):
        files, report, matrix = _fixture()
        files["design/analysis_contracts.json"]["applicability"].pop()
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_circular_or_wrong_analyzer_source_reference(self):
        files, report, matrix = _fixture()
        files["provenance/configuration_fingerprints.json"]["components"][13]["source_ref"] = (
            "design/analysis_contracts.json#/source_contracts/0"
        )
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_semantic_snapshot_divergence_even_with_valid_snapshot_digest(self):
        files, report, matrix = _fixture()
        ref = files["runs/run_records.json"]["run_evidence_records"][0]["snapshot_refs"]["analysis_contract"]
        tagged = json.loads(base64.b64decode(ref["canonical_bytes_base64"]).decode("utf-8"))
        tagged["fields"]["estimand_id"] = "different-semantic-contract"
        raw = json.dumps(tagged, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ref["canonical_bytes_base64"] = base64.b64encode(raw).decode("ascii")
        ref["sha256"] = hashlib.sha256(raw).hexdigest()
        files["runs/run_records.json"]["run_evidence_records"][0]["analysis_contract_sha256"] = ref["sha256"]
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_dgp_component_digest_drift(self):
        files, report, matrix = _fixture()
        files["provenance/configuration_fingerprints.json"]["components"][0]["digest_sha256"] = "0" * 64
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_historical_seed_bank_fingerprint_mismatch(self):
        files, report, matrix = _fixture()
        files["design/benchmark_design.json"]["seed_bank_fingerprint"] = "0" * 64
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_reordered_evaluation_seed_rows(self):
        files, report, matrix = _fixture()
        rows = files["seeds/evaluation_seed_assignments.json"]["rows"]
        rows[0], rows[1] = rows[1], rows[0]
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

    def test_rejects_aggregate_declaration_mismatch(self):
        files, report, matrix = _fixture()
        files["provenance/configuration_fingerprints.json"]["aggregate"]["source_design_declaration"] = (
            "design/analysis_contracts.json#/configuration_fingerprint"
        )
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)

