"""Gate 194-I companion-verifier adversarial tests. Authored only; not executed."""
import base64
import hashlib
import json
import unittest

import rfc8785

from vcont_package_v2_verify import (
    ANALYSIS_CONTRACTS_SCHEMA_ID,
    ANALYSIS_CONTRACTS_SCHEMA_VERSION,
    ANALYSIS_CONTRACT_BOOL_FIELDS,
    ANALYSIS_CONTRACT_NULLABLE_FIELDS,
    ANALYZER_VERSION,
    AUTHORITATIVE_SCENARIO_IDS,
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
    _reconcile_configuration_companions,
    PackageVerificationError,
)


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
    assignment_rows = [{"assignment": i} for i in range(26)]
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
        "design/benchmark_design.json": {"configuration_fingerprint": aggregate_digest},
    }
    decoded_report = {"report": {"design": report_design}}
    return files, decoded_report, matrix


class ConfigurationCompanionVerifierTests(unittest.TestCase):
    def test_positive_13_26_28_reconciliation(self):
        files, report, matrix = _fixture()
        self.assertEqual(_reconcile_configuration_companions(files, report, matrix), (13, 26, 28))

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

    def test_rejects_aggregate_declaration_mismatch(self):
        files, report, matrix = _fixture()
        files["provenance/configuration_fingerprints.json"]["aggregate"]["source_design_declaration"] = (
            "design/analysis_contracts.json#/configuration_fingerprint"
        )
        with self.assertRaises(PackageVerificationError):
            _reconcile_configuration_companions(files, report, matrix)


if __name__ == "__main__":
    unittest.main()
