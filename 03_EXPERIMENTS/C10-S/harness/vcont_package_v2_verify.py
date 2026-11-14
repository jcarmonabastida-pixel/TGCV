"""Independent structural verifier for TGCV C10-S V_cont package v2.

This module deliberately does not import or call vcont_package_v2. It verifies
archive integrity, JCS, the frozen inventory, report/matrix schemas, registered
uint64 occurrences and independent RUN/R snapshot/source joins. Full Gate159
derivation, calibration disjointness, source-execution reconciliation,
technical-test provenance and external authentication remain separate layers.
"""
from __future__ import annotations

from dataclasses import dataclass
import base64
import hashlib
import io
import json
import re
import tarfile
from typing import Any, Mapping

import rfc8785


PACKAGE_SCHEMA_ID = "TGCV-C10S-VCONT-MC-PACKAGE"
PACKAGE_SCHEMA_VERSION = "2.0.0"
REPORT_SCHEMA_ID = "TGCV-C10S-VCONT-REPORT-SNAPSHOT"
REPORT_SCHEMA_VERSION = "2.1.0"
REPORT_PAYLOAD_TYPE = "TGCV-C10S-VCONT-BENCHMARK-REPORT"
MATRIX_SCHEMA_ID = "TGCV-C10S-VCONT-MATRIX-CAPTURE"
MATRIX_SCHEMA_VERSION = "1.0.0"
PACKAGE_PATHS = (
    "manifest.json",
    "report/report.json",
    "design/benchmark_design.json",
    "design/scenario_estimand_matrix.json",
    "design/effective_scenario_configs.json",
    "design/analysis_contracts.json",
    "seeds/evaluation_seed_assignments.json",
    "seeds/calibration_seed_manifest.json",
    "runs/temporal_manifest.json",
    "runs/run_records.json",
    "provenance/source_execution.json",
    "provenance/configuration_fingerprints.json",
    "validation/reconciliation_results.json",
    "validation/test_evidence.json",
)
DATA_PATHS = tuple(path for path in PACKAGE_PATHS if path != "manifest.json")
UINT64_MAX = (1 << 64) - 1

ANALYZER_VERSION = "c10s-vcont-analyzer-0.1"
ANALYSIS_CONTRACTS_SCHEMA_ID = "TGCV-C10S-ANALYSIS-CONTRACTS"
ANALYSIS_CONTRACTS_SCHEMA_VERSION = "1.0.0"
EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID = "TGCV-C10S-EFFECTIVE-ANALYSIS-CONTRACT"
EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION = "1.0.0"
CONFIGURATION_FINGERPRINTS_SCHEMA_ID = "TGCV-C10S-CONFIGURATION-FINGERPRINTS"
CONFIGURATION_FINGERPRINTS_SCHEMA_VERSION = "1.0.0"
AGGREGATE_FINGERPRINT_SCHEMA_ID = "TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT"
AGGREGATE_FINGERPRINT_SCHEMA_VERSION = "1.0.0"
ANALYSIS_CONTRACT_DIGEST_ALGORITHM = "TGCV-C10S-ANALYSIS-CONTRACT-PAYLOAD-JCS-SHA256-1"
DGP_CONFIG_DIGEST_ALGORITHM = "TGCV-C10S-EFFECTIVE-SCENARIO-CONFIG-JCS-SHA256-1"
EVALUATION_ASSIGNMENT_DIGEST_ALGORITHM = "TGCV-C10S-EVALUATION-ASSIGNMENT-MANIFEST-JCS-SHA256-1"
AGGREGATE_FINGERPRINT_ALGORITHM = "TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT-JCS-SHA256-1"
SOURCE_DESIGN_DECLARATION = "design/benchmark_design.json#/configuration_fingerprint"
ANALYSIS_CONTRACT_BOOL_FIELDS = frozenset({
    "randomized_z", "randomized_g", "positivity", "no_interference",
    "measurement_identified", "version_consistency", "focal_direct_path_absent",
    "common_nonfocal_regime", "z_effect_invariant_across_g",
})
ANALYSIS_CONTRACT_NULLABLE_FIELDS = frozenset({
    "transportability_id", "transportability_version", "transportability_scope",
    "transportability_outcome_id", "transportability_basis",
})

# Frozen Gate 166/benchmark-protocol registry; duplicated here intentionally so
# the verifier does not import the producer's scenario/matrix registry.
AUTHORITATIVE_SCENARIO_IDS = (
    "R0_FOCAL_POSITIVE", "R0_FOCAL_NULL", "R0_FOCAL_ADVERSE",
    "R0_DIRECT_G", "R0_DIRECT_Z", "R1_ALTERNATIVE_BASELINE",
    "R2_ALTERNATIVE_AFFECTED", "R3_PROVISION_FAILURE",
    "R0_MEASUREMENT_ADVERSE", "R0_INTERFERENCE", "R0_SUPPORT_FAILURE",
    "R0_HETEROGENEITY", "R2_SUPPORT_FAILURE_ZG_INTERACTION",
)
AUTHORITATIVE_ESTIMAND_IDS = (
    "ITT_Z_RUN_CONDITIONAL_VCONT",
    "ITT_Z_MECHANISM_MARGINAL_VCONT",
    "ITT_Z_REFERENCE_REGIME_VCONT",
    "ITT_G_Z0_VCONT",
)

EFFECTIVE_CONFIG_SCHEMA_ID = "TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION"
EFFECTIVE_CONFIG_SCHEMA_VERSION = "2.0.0"
EFFECTIVE_CONFIG_STRUCTURAL_FIELDS = frozenset({
    "profile", "mechanism", "n_intervals", "window_start",
    "last_transition_support", "follow_up", "enabled_probability",
    "baseline_conformity", "focal_access_effect", "package_direct_effect",
    "focal_direct_effect", "collateral_effect", "provision_probability",
    "alternative_probability", "heterogeneity", "interference_effect",
    "measurement_sensitivity", "measurement_specificity", "missing_probability",
    "randomized_z", "randomized_g", "positivity", "no_interference",
    "measurement_identified", "version_consistency", "zg_interaction_effect",
})
EFFECTIVE_CONFIG_SEED_POLICY = {
    "mode": "EXPLICIT_ASSIGNMENT_STREAMS_REQUIRED",
    "source": "SeedAssignment",
    "streams": ["world_seed", "z_assignment_seed", "g_assignment_seed"],
    "fallback": "FORBIDDEN",
    "algorithm": "TGCV-C10S-VCONT-SEED-v3",
}
EFFECTIVE_CONFIG_EXCLUDED_SOURCE_FIELDS = frozenset({
    "seed", "world_seed", "z_assignment_seed", "g_assignment_seed",
    "replicate_id", "outer_replicate_id", "assignment_role", "assignment_index",
})



class PackageVerificationError(ValueError):
    """The archive or one of its mandatory structural contracts is invalid."""


@dataclass(frozen=True)
class PackageVerificationResult:
    package_schema_id: str
    package_schema_version: str
    profile: str
    archive_sha256: str
    manifest_sha256: str
    package_id: str
    file_count: int
    integrity_status: str
    schema_status: str
    completeness_status: str
    run_r_reconciliation_status: str
    identity_reconciliation_status: str
    source_execution_provenance_status: str
    technical_test_evidence_status: str
    external_authentication_status: str
    limitations: tuple[str, ...]


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _reject_constant(value: str):
    raise PackageVerificationError(f"non-JSON numeric constant rejected: {value}")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PackageVerificationError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def _strict_json(payload: bytes, path: str) -> tuple[Any, bytes]:
    if not isinstance(payload, bytes) or payload.startswith(b"\xef\xbb\xbf"):
        raise PackageVerificationError(f"{path}: JSON must be UTF-8 bytes without BOM")
    if not payload.endswith(b"\n") or payload.endswith(b"\n\n") or payload.endswith(b"\r\n"):
        raise PackageVerificationError(f"{path}: exactly one trailing LF is required")
    raw = payload[:-1]
    try:
        decoded = raw.decode("utf-8", errors="strict")
        value = json.loads(
            decoded, object_pairs_hook=_unique_object, parse_constant=_reject_constant
        )
        canonical = rfc8785.dumps(value)
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"{path}: invalid UTF-8/JSON/JCS value: {exc}") from exc
    if canonical != raw:
        raise PackageVerificationError(f"{path}: bytes are not RFC 8785 canonical JSON")
    return value, canonical


def _safe_archive_path(path: str) -> None:
    if (not isinstance(path, str) or not path or path.startswith("/")
            or "\\" in path or path.startswith("./")
            or any(part in ("", ".", "..") for part in path.split("/"))):
        raise PackageVerificationError("archive contains an unsafe/noncanonical path")
    try:
        path.encode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise PackageVerificationError("archive path is not valid UTF-8") from exc


def _uint64(value: Any, label: str) -> int:
    if not isinstance(value, dict) or set(value) != {"$type", "decimal"}:
        raise PackageVerificationError(f"{label}: uint64 wrapper must have exactly two members")
    if value["$type"] != "uint64" or not isinstance(value["decimal"], str):
        raise PackageVerificationError(f"{label}: malformed uint64 wrapper type")
    decimal = value["decimal"]
    if not re.fullmatch(r"(0|[1-9][0-9]*)", decimal, flags=re.ASCII):
        raise PackageVerificationError(f"{label}: uint64 decimal is not canonical ASCII unsigned decimal")
    number = int(decimal)
    if number > UINT64_MAX:
        raise PackageVerificationError(f"{label}: uint64 value exceeds 2^64-1")
    return number


def _pointer_occurrences(value: Any, path: str = ""):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = path + "/" + str(key).replace("~", "~0").replace("/", "~1")
            yield child_path, child
            yield from _pointer_occurrences(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = path + "/" + str(index)
            yield child_path, child
            yield from _pointer_occurrences(child, child_path)


def _registered_pattern(path: str) -> bool:
    patterns = (
        r"/rows/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)",
        r"/report/temporal_manifest/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)",
        r"/report/manifest/temporal_manifest/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)",
        r"/report/pair_ledger/[0-9]+/contributions/[0-9]+/world_seed",
        r"/report/manifest/pair_ledger/[0-9]+/contributions/[0-9]+/world_seed",
        r"/report/scenario_reports/[^/]+/per_outer_replicate/[0-9]+/run/0/seed",
        r"/report/scenario_reports/[^/]+/per_outer_replicate/[0-9]+/run/3/(world_seed|z_assignment_seed|g_assignment_seed)",
        r"/outer_world_evidence_records/[0-9]+/key/world_seed",
    )
    return any(re.fullmatch(pattern, path) is not None for pattern in patterns)


def _check_registered_uint64(files: Mapping[str, Any]) -> tuple[int, ...]:
    expected_paths = {
        "seeds/evaluation_seed_assignments.json": (
            r"/rows/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)", 3
        ),
        "seeds/calibration_seed_manifest.json": (
            r"/rows/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)", 3
        ),
        "runs/temporal_manifest.json": (
            r"/rows/[0-9]+/(world_seed|z_assignment_seed|g_assignment_seed)", 3
        ),
        "report/report.json": (
            r"/report/(?:temporal_manifest/[0-9]+/(?:world_seed|z_assignment_seed|g_assignment_seed)|"
            r"manifest/temporal_manifest/[0-9]+/(?:world_seed|z_assignment_seed|g_assignment_seed)|"
            r"pair_ledger/[0-9]+/contributions/[0-9]+/world_seed|"
            r"manifest/pair_ledger/[0-9]+/contributions/[0-9]+/world_seed|"
            r"scenario_reports/[^/]+/per_outer_replicate/[0-9]+/run/0/seed|"
            r"scenario_reports/[^/]+/per_outer_replicate/[0-9]+/run/3/(?:world_seed|z_assignment_seed|g_assignment_seed))", 1
        ),
        "runs/run_records.json": (
            r"/outer_world_evidence_records/[0-9]+/key/world_seed", 1
        ),
    }
    counts = []
    for file_path, (pattern, minimum_per_group) in expected_paths.items():
        value = files[file_path]
        found = []
        for pointer, child in _pointer_occurrences(value):
            key = pointer.rsplit("/", 1)[-1]
            if key in {"seed", "world_seed", "z_assignment_seed", "g_assignment_seed"} and not _registered_pattern(pointer):
                raise PackageVerificationError(f"{file_path}{pointer}: direct seed field is outside the frozen registry")
            if re.fullmatch(pattern, pointer):
                _uint64(child, file_path + pointer)
                found.append(pointer)
            if isinstance(child, dict) and "$type" in child and not _registered_pattern(pointer):
                raise PackageVerificationError(f"{file_path}{pointer}: uint64 wrapper appears at an unregistered pointer")
        if not found or len(found) % minimum_per_group != 0:
            raise PackageVerificationError(f"{file_path}: registered uint64 pointers are missing or incomplete")
        counts.append(len(found))

    # Cardinality and per-row consumption checks for every direct row registry.
    for file_path in (
        "seeds/evaluation_seed_assignments.json",
        "seeds/calibration_seed_manifest.json",
        "runs/temporal_manifest.json",
    ):
        envelope = files[file_path]
        rows = envelope.get("rows") if isinstance(envelope, dict) else None
        if (not isinstance(rows, list) or not rows
                or envelope.get("row_count") != len(rows)):
            raise PackageVerificationError(f"{file_path}: row_count/rows envelope is incomplete")
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                raise PackageVerificationError(f"{file_path}/rows/{index}: row is not an object")
            fields = (("world_seed", "z_assignment_seed", "g_assignment_seed")
                      if file_path != "runs/temporal_manifest.json"
                      else ("world_seed", "z_assignment_seed", "g_assignment_seed"))
            for field in fields:
                _uint64(row.get(field), f"{file_path}/rows/{index}/{field}")

    report_envelope = files["report/report.json"]
    report_payload = report_envelope.get("report") if isinstance(report_envelope, dict) else None
    if not isinstance(report_payload, dict):
        raise PackageVerificationError("report/report.json: FrozenReportSnapshot report payload is missing")
    temporal = report_payload.get("temporal_manifest")
    report_manifest = report_payload.get("manifest")
    if not isinstance(report_manifest, dict):
        raise PackageVerificationError("report/report.json: nested legacy manifest is not an object")
    nested_temporal = report_manifest.get("temporal_manifest")
    pairs = report_payload.get("pair_ledger")
    nested_pairs = report_manifest.get("pair_ledger")
    if not all(isinstance(rows, list) for rows in (temporal, nested_temporal, pairs, nested_pairs)):
        raise PackageVerificationError("report/report.json: registered duplicate seed-bearing arrays are missing")
    if temporal != nested_temporal or pairs != nested_pairs:
        raise PackageVerificationError("report/report.json: duplicate seed-bearing report views diverge")
    for collection_name, rows, field_names in (
        ("temporal_manifest", temporal, ("world_seed", "z_assignment_seed", "g_assignment_seed")),
        ("pair_ledger", pairs, ()),
    ):
        for index, row in enumerate(rows):
            if collection_name == "temporal_manifest":
                for field in field_names:
                    _uint64(row.get(field), f"report/{collection_name}/{index}/{field}")
            else:
                contributions = row.get("contributions") if isinstance(row, dict) else None
                if not isinstance(contributions, list) or not contributions:
                    raise PackageVerificationError(f"report/pair_ledger/{index}: contributions missing")
                for j, contribution in enumerate(contributions):
                    if not isinstance(contribution, dict):
                        raise PackageVerificationError(f"report/pair_ledger/{index}/contributions/{j}: not an object")
                    _uint64(contribution.get("world_seed"), f"report/pair_ledger/{index}/contributions/{j}/world_seed")
    scenarios = report_payload.get("scenario_reports")
    if not isinstance(scenarios, dict) or len(scenarios) != 13:
        raise PackageVerificationError("report scenario_reports must contain exactly 13 scenarios")
    for scenario_id, scenario in scenarios.items():
        outer_rows = scenario.get("per_outer_replicate") if isinstance(scenario, dict) else None
        if not isinstance(outer_rows, list) or not outer_rows:
            raise PackageVerificationError(f"report/scenario_reports/{scenario_id}: per_outer_replicate missing")
        for index, outer in enumerate(outer_rows):
            run = outer.get("run") if isinstance(outer, dict) else None
            if not isinstance(run, list) or len(run) != 4:
                raise PackageVerificationError(f"report/scenario_reports/{scenario_id}/{index}: RUN tuple malformed")
            if not isinstance(run[0], dict) or not isinstance(run[3], dict):
                raise PackageVerificationError(f"report/scenario_reports/{scenario_id}/{index}: source tuple objects malformed")
            _uint64(run[0].get("seed"), f"report/scenario_reports/{scenario_id}/{index}/run/0/seed")
            for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
                _uint64(run[3].get(field), f"report/scenario_reports/{scenario_id}/{index}/run/3/{field}")

    run_records = files["runs/run_records.json"]
    outer_records = run_records.get("outer_world_evidence_records") if isinstance(run_records, dict) else None
    if not isinstance(outer_records, list) or not outer_records:
        raise PackageVerificationError("run_records outer_world_evidence_records is missing")
    for index, outer in enumerate(outer_records):
        key = outer.get("key") if isinstance(outer, dict) else None
        _uint64(key.get("world_seed") if isinstance(key, dict) else None,
                f"runs/run_records.json/outer_world_evidence_records/{index}/key/world_seed")
    # No wrapper may occur in any package JSON outside a registered path.
    for file_path, value in files.items():
        if file_path in expected_paths:
            continue
        for pointer, child in _pointer_occurrences(value):
            key = pointer.rsplit("/", 1)[-1]
            if key in {"seed", "world_seed", "z_assignment_seed", "g_assignment_seed"}:
                raise PackageVerificationError(f"{file_path}{pointer}: direct seed field is prohibited outside the frozen registry")
            if isinstance(child, dict) and "$type" in child:
                raise PackageVerificationError(f"{file_path}{pointer}: typed wrapper is prohibited at this path")
    return tuple(counts)


def _decode_registered(value: Any) -> Any:
    if isinstance(value, dict):
        if "$type" in value:
            return _uint64(value, "registered pointer")
        return {key: _decode_registered(child) for key, child in value.items()}
    if isinstance(value, list):
        return [_decode_registered(child) for child in value]
    return value



@dataclass(frozen=True)
class DecodedFrozenSnapshot:
    """Strictly decoded view plus the immutable original snapshot bytes."""
    type_id: str
    serialization_id: str
    canonical_bytes: bytes
    sha256: str
    value: Any


_SNAPSHOT_TYPE_FIELDS = {
    "vcont_benchmark_protocol.SeedAssignment": frozenset({
        "bank", "scenario_id", "n_units", "replicate", "world_seed",
        "z_assignment_seed", "g_assignment_seed", "scenario_version",
        "outer_replicate_id", "assignment_role",
    }),
    "vcont_integrated_harness.AnalysisContract": frozenset({
        "estimand_id", "estimand_version", "randomized_z", "randomized_g",
        "positivity", "no_interference", "measurement_identified",
        "version_consistency", "focal_direct_path_absent", "common_nonfocal_regime",
        "target_regime_id", "target_regime_version", "outcome_id", "outcome_version",
        "z_effect_invariant_across_g", "transportability_id", "transportability_version",
        "transportability_scope", "transportability_evidence_status",
        "g_assignment_mechanism_hash", "z_assignment_mechanism_hash",
        "g_assignment_mechanism_id", "g_assignment_mechanism_version",
        "z_assignment_mechanism_id", "z_assignment_mechanism_version",
        "reference_regime_id", "reference_regime_version", "transportability_outcome_id",
        "transportability_basis", "run_conditional_estimand_id",
        "run_conditional_estimand_version", "mechanism_marginal_estimand_id",
        "mechanism_marginal_estimand_version", "reference_regime_estimand_id",
        "reference_regime_estimand_version", "g_assignment_estimand_id",
        "g_assignment_estimand_version",
    }),
    "vcont_integrated_harness.AnalyzerResult": frozenset({
        "run_id", "estimand_id", "package_status", "g_assignment_status",
        "package_itt", "g_assignment_effect", "first_stage_delta_t_acc",
        "package_se", "g_assignment_se", "abstention_reasons", "input_sha256",
        "output_sha256", "target_regime_id", "target_regime_version", "outcome_id",
        "outcome_version", "reference_regime_status", "reference_regime_id",
        "reference_regime_version", "g_assignment_mechanism_hash",
        "z_assignment_mechanism_hash", "transportability_id",
        "transportability_version", "transportability_scope",
        "transportability_evidence_status", "estimand_version",
        "g_assignment_mechanism_id", "g_assignment_mechanism_version",
        "z_assignment_mechanism_id", "z_assignment_mechanism_version",
        "provenance_sha256", "transportability_outcome_id", "transportability_basis",
        "reference_regime_itt", "run_conditional_estimand_id",
        "run_conditional_estimand_version", "reference_regime_estimand_id",
        "reference_regime_estimand_version", "g_assignment_estimand_id",
        "g_assignment_estimand_version", "outer_replicate_id",
        "assignment_role", "assignment_index",
    }),
    "vcont_integrated_harness.EvaluationReport": frozenset({
        "run_id", "package_abs_error", "g_assignment_abs_error", "package_recovered",
        "g_assignment_recovered", "expected_abstention_respected", "notes",
        "reference_regime_status_correct", "reference_regime_estimate_present",
    }),
    "vcont_integrated_harness.EvidenceCandidate": frozenset({
        "run_id", "rows", "provenance",
    }),
    "vcont_integrated_harness.RepeatedAssignmentReport": frozenset({
        "world_id", "replicate_count", "mean_run_estimate", "mechanism_truth",
        "marginal_abs_error", "marginal_recovered", "per_run_reports",
        "reference_truth", "reference_estimate_mean", "reference_abs_error",
        "reference_recovered", "reference_identification_status",
        "mechanism_marginal_estimand_id", "mechanism_marginal_estimand_version",
        "reference_regime_estimand_id", "reference_regime_estimand_version",
    }),
    "vcont_integrated_harness.RunManifest": frozenset({
        "run_id", "scenario_id", "version", "n_units", "n_intervals",
        "window_start", "window_end", "interval_width", "generator_version",
        "world_id", "world_version", "replicate_id", "g_assignment_mechanism_id",
        "g_assignment_mechanism_version", "g_assignment_mechanism_hash",
        "z_assignment_mechanism_id", "z_assignment_mechanism_version",
        "z_assignment_mechanism_hash", "g_reference_regime_id",
        "g_reference_regime_version", "z_assignment_vector_hash",
        "g_assignment_vector_hash", "g_assignment_probability_by_stratum",
        "world_seed", "z_assignment_seed", "g_assignment_seed",
        "outer_replicate_id", "assignment_role", "assignment_index",
    }),
    "vcont_integrated_harness.ScenarioConfig": frozenset({
        "scenario_id", "version", "profile", "mechanism", "n_units", "n_intervals",
        "seed", "window_start", "last_transition_support", "follow_up",
        "enabled_probability", "baseline_conformity", "focal_access_effect",
        "package_direct_effect", "focal_direct_effect", "collateral_effect",
        "provision_probability", "alternative_probability", "heterogeneity",
        "interference_effect", "measurement_sensitivity", "measurement_specificity",
        "missing_probability", "randomized_z", "randomized_g", "positivity",
        "no_interference", "measurement_identified", "version_consistency",
        "zg_interaction_effect", "world_seed", "z_assignment_seed",
        "g_assignment_seed", "replicate_id", "outer_replicate_id",
        "assignment_role", "assignment_index",
    }),
    "vcont_integrated_harness.SealedEvidence": frozenset({
        "run_id", "rows", "manifest", "sha256",
    }),
    "vcont_integrated_harness.TruthBundle": frozenset({
        "run_id", "potential_v", "potential_interval_truth", "potential_enabled_truth",
        "potential_profile_truth", "potential_delta_t_acc", "itt_z_truth",
        "itt_g_z0_truth", "theta_a_truth", "seed", "itt_z_run_truth",
        "itt_z_mechanism_truth", "itt_z_reference_truth",
        "transportability_invariant_truth", "transportability_scope_truth",
        "g_reference_regime_id", "g_reference_regime_version",
        "g_assignment_mechanism_hash", "z_assignment_mechanism_hash",
        "outer_replicate_id", "assignment_role", "assignment_index",
    }),
    "vcont_evidence_export.MatrixTruthProjection": frozenset({
        "run_id", "itt_z_run_truth", "itt_g_z0_truth", "itt_z_mechanism_truth",
        "itt_z_reference_truth", "outer_replicate_id", "assignment_role",
        "assignment_index", "g_reference_regime_id", "g_reference_regime_version",
        "g_assignment_mechanism_hash", "z_assignment_mechanism_hash", "seed",
        "theta_a_truth",
    }),
}
_SNAPSHOT_ENUM_VALUES = {
    "vcont_benchmark_protocol.EvaluationClass": frozenset({
        "EVALUABLE", "STATUS_ONLY", "NOT_IDENTIFIABLE", "NOT_EVALUABLE",
    }),
    "vcont_benchmark_protocol.TruthStatus": frozenset({
        "DEFINED", "UNDEFINED", "NOT_MATERIALIZED",
    }),
}


def _validate_snapshot_node(value: Any, label: str) -> Any:
    """Validate the closed historical tagged grammar without importing its codec."""
    if isinstance(value, dict):
        if set(value) == {"$dataclass", "fields"}:
            type_id, fields = value["$dataclass"], value["fields"]
            if (not isinstance(type_id, str) or type_id not in _SNAPSHOT_TYPE_FIELDS
                    or not isinstance(fields, dict)):
                raise PackageVerificationError(f"{label}: unknown dataclass type or malformed fields")
            expected = _SNAPSHOT_TYPE_FIELDS[type_id]
            if set(fields) != expected:
                missing, extra = sorted(expected - set(fields)), sorted(set(fields) - expected)
                raise PackageVerificationError(
                    f"{label}: {type_id} field allowlist mismatch; missing={missing}; extra={extra}"
                )
            return {
                "$dataclass": type_id,
                "fields": {
                    key: _validate_snapshot_node(child, f"{label}.{type_id}.{key}")
                    for key, child in fields.items()
                },
            }
        if set(value) == {"$enum", "value"}:
            enum_id, enum_value = value["$enum"], value["value"]
            if (not isinstance(enum_id, str) or enum_id not in _SNAPSHOT_ENUM_VALUES
                    or not isinstance(enum_value, str)
                    or enum_value not in _SNAPSHOT_ENUM_VALUES[enum_id]):
                raise PackageVerificationError(f"{label}: unknown enum identity or value")
            return {"$enum": enum_id, "value": enum_value}
        if set(value) == {"$tuple"} or set(value) == {"$list"}:
            tag = "$tuple" if "$tuple" in value else "$list"
            items = value[tag]
            if not isinstance(items, list):
                raise PackageVerificationError(f"{label}: {tag} payload must be an array")
            return {tag: [
                _validate_snapshot_node(child, f"{label}.{tag}[{index}]")
                for index, child in enumerate(items)
            ]}
        if set(value) == {"$map"}:
            items = value["$map"]
            if not isinstance(items, dict) or list(items) != sorted(items):
                raise PackageVerificationError(f"{label}: $map must have string keys in canonical sorted order")
            return {"$map": {
                key: _validate_snapshot_node(child, f"{label}.$map[{key!r}]")
                for key, child in items.items()
            }}
        raise PackageVerificationError(f"{label}: untagged or unknown object in FrozenSnapshot grammar")
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        import math
        if not math.isfinite(value):
            raise PackageVerificationError(f"{label}: non-finite snapshot number")
        return value
    raise PackageVerificationError(f"{label}: unsupported FrozenSnapshot value type")


def decode_frozen_snapshot_ref(
    reference: Any, *, expected_type_id: str | None = None
) -> DecodedFrozenSnapshot:
    """Independently validate a Gate 174 snapshot envelope and preserve its exact bytes."""
    required = {
        "type_id", "encoding", "media_type", "serialization_id",
        "canonical_bytes_base64", "sha256",
    }
    if not isinstance(reference, dict) or set(reference) != required:
        raise PackageVerificationError("FrozenSnapshot reference field allowlist mismatch")
    type_id = reference["type_id"]
    if (not isinstance(type_id, str) or type_id not in _SNAPSHOT_TYPE_FIELDS
            or (expected_type_id is not None and type_id != expected_type_id)):
        raise PackageVerificationError("FrozenSnapshot reference has an unknown or unexpected type_id")
    if (reference["encoding"], reference["media_type"], reference["serialization_id"]) != (
        "base64", "application/vnd.tgcv.typed-snapshot+json", "TGCV-FROZEN-SNAPSHOT-1"
    ):
        raise PackageVerificationError("FrozenSnapshot encoding/media_type/serialization_id mismatch")
    encoded = reference["canonical_bytes_base64"]
    if not isinstance(encoded, str):
        raise PackageVerificationError("FrozenSnapshot base64 payload must be a string")
    try:
        snapshot_bytes = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise PackageVerificationError(f"FrozenSnapshot base64 payload is invalid: {exc}") from exc
    if base64.b64encode(snapshot_bytes).decode("ascii") != encoded:
        raise PackageVerificationError("FrozenSnapshot base64 payload is not canonical")
    digest = reference["sha256"]
    if (not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)
            or _sha256(snapshot_bytes) != digest):
        raise PackageVerificationError("FrozenSnapshot exact-byte SHA-256 mismatch")
    try:
        raw = snapshot_bytes.decode("utf-8", errors="strict")
        parsed = json.loads(
            raw, object_pairs_hook=_unique_object, parse_constant=_reject_constant
        )
        canonical = json.dumps(
            parsed, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"FrozenSnapshot strict JSON decode failed: {exc}") from exc
    if canonical != snapshot_bytes:
        raise PackageVerificationError("FrozenSnapshot bytes are not canonical historical serialization")
    if (not isinstance(parsed, dict) or set(parsed) != {"$dataclass", "fields"}
            or parsed.get("$dataclass") != type_id):
        raise PackageVerificationError("FrozenSnapshot root dataclass identity mismatch")
    decoded = _validate_snapshot_node(parsed, "FrozenSnapshot")
    return DecodedFrozenSnapshot(
        type_id=type_id,
        serialization_id="TGCV-FROZEN-SNAPSHOT-1",
        canonical_bytes=snapshot_bytes,
        sha256=digest,
        value=decoded,
    )



def _snapshot_source_value(value: Any) -> Any:
    """Convert a validated tagged snapshot tree to source-domain values for comparisons."""
    if isinstance(value, dict):
        if set(value) == {"$dataclass", "fields"}:
            return {key: _snapshot_source_value(child)
                    for key, child in value["fields"].items()}
        if set(value) == {"$enum", "value"}:
            return _snapshot_source_value(value["value"])
        if set(value) == {"$tuple"}:
            return tuple(_snapshot_source_value(child) for child in value["$tuple"])
        if set(value) == {"$list"}:
            return [_snapshot_source_value(child) for child in value["$list"]]
        if set(value) == {"$map"}:
            return {key: _snapshot_source_value(child) for key, child in value["$map"].items()}
        raise PackageVerificationError("snapshot source conversion encountered an untagged object")
    return value


def _snapshot_fields(decoded: DecodedFrozenSnapshot, expected_type: str) -> dict[str, Any]:
    if decoded.type_id != expected_type:
        raise PackageVerificationError(
            f"snapshot type mismatch: expected {expected_type}, got {decoded.type_id}"
        )
    root = decoded.value
    if not isinstance(root, dict) or set(root) != {"$dataclass", "fields"}:
        raise PackageVerificationError("decoded snapshot root is not a dataclass")
    return _snapshot_source_value(root)


def _logical_run_key(value: Any, label: str) -> tuple[Any, ...]:
    required = (
        "scenario_id", "scenario_version", "N", "outer_replicate_id",
        "assignment_role", "assignment_index", "run_id",
    )
    if not isinstance(value, dict) or set(value) != set(required):
        raise PackageVerificationError(f"{label}: exact logical RUN key fields required")
    key = tuple(value[name] for name in required)
    if (not isinstance(key[0], str) or not key[0]
            or not isinstance(key[1], str) or not key[1]
            or isinstance(key[2], bool) or not isinstance(key[2], int) or key[2] < 1
            or not isinstance(key[3], str) or not key[3]
            or key[4] not in ("RUN", "REPEATED_ASSIGNMENT")
            or isinstance(key[5], bool) or not isinstance(key[5], int)
            or not isinstance(key[6], str) or not key[6]):
        raise PackageVerificationError(f"{label}: malformed logical RUN key values")
    if (key[4], key[5]) == ("RUN", -1):
        pass
    elif key[4] == "REPEATED_ASSIGNMENT" and key[5] >= 0:
        pass
    else:
        raise PackageVerificationError(f"{label}: role/index pair is not canonical")
    return key




def _exact_source_uint64(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= UINT64_MAX:
        raise PackageVerificationError(f"{label}: source value is not an exact uint64 integer")
    return value


def _assert_snapshot_seed_relations(
    assignment: dict[str, Any], config: dict[str, Any],
    manifest: dict[str, Any], truth_projection: dict[str, Any],
) -> None:
    """Enforce the four source-specific seed equalities without conflating domains."""
    config_seed = _exact_source_uint64(config.get("seed"), "ScenarioConfig.seed")
    truth_seed = _exact_source_uint64(truth_projection.get("seed"), "MatrixTruthProjection.seed")
    if truth_seed != config_seed:
        raise PackageVerificationError("MatrixTruthProjection.seed differs from ScenarioConfig.seed")
    assignment_streams = tuple(
        _exact_source_uint64(assignment.get(name), f"SeedAssignment.{name}")
        for name in ("world_seed", "z_assignment_seed", "g_assignment_seed")
    )
    config_streams = tuple(
        _exact_source_uint64(config.get(name), f"ScenarioConfig.{name}")
        for name in ("world_seed", "z_assignment_seed", "g_assignment_seed")
    )
    manifest_streams = tuple(
        _exact_source_uint64(manifest.get(name), f"RunManifest.{name}")
        for name in ("world_seed", "z_assignment_seed", "g_assignment_seed")
    )
    if assignment_streams != config_streams or assignment_streams != manifest_streams:
        raise PackageVerificationError("SeedAssignment/ScenarioConfig/RunManifest stream equality failed")
    if len(set(assignment_streams)) != 3:
        raise PackageVerificationError("world/Z/G seed streams are not distinct within assignment")


def _snapshot_report_projection(value: Any) -> Any:
    """Match the report's source-safe projection: tuples become JSON arrays."""
    if isinstance(value, dict):
        return {key: _snapshot_report_projection(child) for key, child in value.items()}
    if isinstance(value, tuple):
        return [_snapshot_report_projection(child) for child in value]
    if isinstance(value, list):
        return [_snapshot_report_projection(child) for child in value]
    return value


def _snapshot_encode_source(value: Any) -> Any:
    """Reproduce the historical tagged encoder for a plain source-domain value."""
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise PackageVerificationError("snapshot source mapping contains a non-string key")
        return {"$map": {key: _snapshot_encode_source(value[key]) for key in sorted(value)}}
    if isinstance(value, tuple):
        return {"$tuple": [_snapshot_encode_source(item) for item in value]}
    if isinstance(value, list):
        return {"$list": [_snapshot_encode_source(item) for item in value]}
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        import math
        if not math.isfinite(value):
            raise PackageVerificationError("snapshot source contains a non-finite number")
        return value
    raise PackageVerificationError("snapshot source contains an unsupported value")


def _snapshot_source_digest(value: Any) -> str:
    payload = json.dumps(
        _snapshot_encode_source(value), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")
    return _sha256(payload)



def _assert_sealed_provenance_identity(
    provenance: Any, run_id: str, assignment: dict[str, Any],
    config: dict[str, Any], manifest: dict[str, Any], analyzer: dict[str, Any],
) -> str:
    """Bind the internally hashed sealed provenance to this exact captured RUN/R source."""
    if not isinstance(provenance, dict):
        raise PackageVerificationError("SealedEvidence provenance must be an object")
    expected = {
        "run_id": run_id,
        "scenario_id": config["scenario_id"],
        "scenario_version": config["version"],
        "world_id": manifest["world_id"],
        "world_version": manifest["world_version"],
        "replicate_id": config["replicate_id"],
        "outer_replicate_id": assignment["outer_replicate_id"],
        "assignment_role": assignment["assignment_role"],
        "assignment_index": assignment["replicate"],
        "g_assignment_mechanism_id": manifest["g_assignment_mechanism_id"],
        "g_assignment_mechanism_version": manifest["g_assignment_mechanism_version"],
        "g_assignment_mechanism_hash": manifest["g_assignment_mechanism_hash"],
        "z_assignment_mechanism_id": manifest["z_assignment_mechanism_id"],
        "z_assignment_mechanism_version": manifest["z_assignment_mechanism_version"],
        "z_assignment_mechanism_hash": manifest["z_assignment_mechanism_hash"],
        "g_reference_regime_id": manifest["g_reference_regime_id"],
        "g_reference_regime_version": manifest["g_reference_regime_version"],
        "z_assignment_vector_hash": manifest["z_assignment_vector_hash"],
        "g_assignment_vector_hash": manifest["g_assignment_vector_hash"],
    }
    if any(provenance.get(name) != value for name, value in expected.items()):
        raise PackageVerificationError("SealedEvidence provenance identity differs from its RUN/R source objects")
    digest = _sha256(json.dumps(
        provenance, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8"))
    if manifest.get("provenance_sha256") != digest:
        raise PackageVerificationError("SealedEvidence provenance digest does not recompute")
    if analyzer.get("provenance_sha256") != digest:
        raise PackageVerificationError("AnalyzerResult provenance_sha256 differs from SealedEvidence provenance")
    return digest


def _snapshot_legacy_sealed_digest(sealed: dict[str, Any]) -> str:
    if set(sealed) != {"run_id", "rows", "manifest", "sha256"}:
        raise PackageVerificationError("SealedEvidence decoded fields are incomplete")
    payload = json.dumps(
        {"manifest": sealed["manifest"], "rows": sealed["rows"]},
        sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return _sha256(payload)




def _assert_report_snapshot_projection(report_value: Any, snapshot_value: Any, label: str) -> None:
    """Reject a structurally valid report object that is not the captured source projection."""
    if report_value != _snapshot_report_projection(snapshot_value):
        raise PackageVerificationError(f"{label} report projection differs from independently decoded snapshot")


def _register_unique_run_record(
    run_map: dict[tuple[Any, ...], Any], decoded_by_key: dict[tuple[Any, ...], Any],
    key: tuple[Any, ...], record: Any, decoded: Any,
) -> None:
    if key in run_map or key in decoded_by_key:
        raise PackageVerificationError("duplicate run key")
    run_map[key] = record
    decoded_by_key[key] = decoded


def _resolve_outer_world_run_reference(
    reference: Any, label: str, base: tuple[Any, ...], role: str, index: int,
    run_map: Mapping[tuple[Any, ...], Any], decoded_by_key: Mapping[tuple[Any, ...], Any],
    expected_world: tuple[Any, Any, Any],
) -> tuple[tuple[Any, ...], dict[str, Any]]:
    """Resolve one full RUN/R key and bind it to the designated outer-world identity."""
    parsed_key = _logical_run_key(reference, label)
    if parsed_key[:6] != (*base, role, index):
        raise PackageVerificationError(f"{label} does not identify the expected RUN/R assignment")
    if parsed_key not in run_map:
        raise PackageVerificationError(f"{label} is an orphaned RUN/R reference")
    manifest = decoded_by_key[parsed_key]["run_manifest"]
    if manifest.get("run_id") != parsed_key[6]:
        raise PackageVerificationError(f"{label} run_id differs from its decoded RunManifest")
    observed_world = (
        manifest.get("world_id"), manifest.get("world_version"), manifest.get("world_seed"),
    )
    if observed_world != expected_world:
        raise PackageVerificationError(f"{label} is bound to a different outer-world identity")
    return parsed_key, manifest




def _reconcile_effective_scenario_config_rows(
    effective_file: Any, report_design: Any, decoded_runs: list[dict[str, Any]],
) -> int:
    """Reconcile the Gate 181 structural config rows against every decoded RUN/R config snapshot."""
    if not isinstance(effective_file, dict):
        raise PackageVerificationError("effective ScenarioConfig companion must be an object")
    if (effective_file.get("schema_id"), effective_file.get("schema_version")) != (
        EFFECTIVE_CONFIG_SCHEMA_ID, EFFECTIVE_CONFIG_SCHEMA_VERSION
    ):
        raise PackageVerificationError("effective ScenarioConfig projection schema/version mismatch")
    rows = effective_file.get("rows")
    if not isinstance(rows, list) or len(rows) != len(AUTHORITATIVE_SCENARIO_IDS):
        raise PackageVerificationError("effective ScenarioConfig projection must contain exactly 13 rows")
    if "row_count" in effective_file and (
        isinstance(effective_file["row_count"], bool)
        or not isinstance(effective_file["row_count"], int)
        or effective_file["row_count"] != len(rows)
    ):
        raise PackageVerificationError("effective ScenarioConfig projection row_count mismatch")
    if not isinstance(report_design, dict):
        raise PackageVerificationError("report design is required for effective ScenarioConfig reconciliation")
    scenario_versions = report_design.get("scenario_versions")
    n_units = report_design.get("n_units")
    M, R = report_design.get("outer_replicates"), report_design.get("repeated_assignments")
    if (not isinstance(scenario_versions, list)
            or tuple(row[0] for row in scenario_versions
                     if isinstance(row, list) and len(row) == 2) != AUTHORITATIVE_SCENARIO_IDS
            or isinstance(n_units, bool) or not isinstance(n_units, int)
            or isinstance(M, bool) or not isinstance(M, int)
            or isinstance(R, bool) or not isinstance(R, int)):
        raise PackageVerificationError("report design is malformed for effective ScenarioConfig reconciliation")
    versions = {row[0]: row[1] for row in scenario_versions}
    row_fields = {
        "scenario_id", "scenario_version", "n_units", "generator_version",
        "seed_policy", "config",
    }
    expected_order = [(sid, versions[sid], n_units) for sid in AUTHORITATIVE_SCENARIO_IDS]
    row_map: dict[tuple[Any, ...], dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != row_fields:
            raise PackageVerificationError(f"effective ScenarioConfig row {index} field allowlist mismatch")
        if (not isinstance(row["scenario_id"], str) or not row["scenario_id"]
                or not isinstance(row["scenario_version"], str) or not row["scenario_version"]
                or isinstance(row["n_units"], bool) or not isinstance(row["n_units"], int)
                or row["n_units"] < 1):
            raise PackageVerificationError(f"effective ScenarioConfig row {index} identity values are invalid")
        key = (row["scenario_id"], row["scenario_version"], row["n_units"])
        if key != expected_order[index]:
            raise PackageVerificationError(f"effective ScenarioConfig row {index} differs from authoritative scenario/version/N order")
        if key in row_map:
            raise PackageVerificationError("effective ScenarioConfig projection contains a duplicate row key")
        if not isinstance(row["generator_version"], str) or not row["generator_version"]:
            raise PackageVerificationError(f"effective ScenarioConfig row {index} generator_version is invalid")
        if row["seed_policy"] != EFFECTIVE_CONFIG_SEED_POLICY:
            raise PackageVerificationError(f"effective ScenarioConfig row {index} seed_policy differs from Gate 181")
        config_projection = row["config"]
        if not isinstance(config_projection, dict) or set(config_projection) != EFFECTIVE_CONFIG_STRUCTURAL_FIELDS:
            raise PackageVerificationError(f"effective ScenarioConfig row {index} structural config field allowlist mismatch")
        row_map[key] = row

    expected_runs = len(AUTHORITATIVE_SCENARIO_IDS) * M * (1 + R)
    if len(decoded_runs) != expected_runs:
        raise PackageVerificationError("effective ScenarioConfig join input cardinality differs from 13 x M x (1+R)")
    seen_run_keys = set()
    generator_versions: dict[str, set[str]] = {sid: set() for sid in AUTHORITATIVE_SCENARIO_IDS}
    consumed: dict[tuple[Any, ...], int] = {key: 0 for key in row_map}
    for item in decoded_runs:
        if not isinstance(item, dict) or set(item) != {"key", "config", "generator_version"}:
            raise PackageVerificationError("decoded effective-config RUN input field allowlist mismatch")
        key = item["key"]
        if not isinstance(key, tuple) or len(key) != 7 or key in seen_run_keys:
            raise PackageVerificationError("effective-config RUN input key is malformed or duplicated")
        seen_run_keys.add(key)
        scenario_key = (key[0], key[1], key[2])
        row = row_map.get(scenario_key)
        if row is None:
            raise PackageVerificationError("RUN/R config snapshot has no effective ScenarioConfig row")
        config = item["config"]
        if not isinstance(config, dict):
            raise PackageVerificationError("decoded ScenarioConfig snapshot is not an object")
        if (config.get("scenario_id"), config.get("version"), config.get("n_units")) != scenario_key:
            raise PackageVerificationError("ScenarioConfig snapshot identity differs from effective projection row key")
        structural = {
            name: value for name, value in config.items()
            if name not in EFFECTIVE_CONFIG_EXCLUDED_SOURCE_FIELDS
        }
        expected_structural = {
            "scenario_id": row["scenario_id"],
            "version": row["scenario_version"],
            "n_units": row["n_units"],
            **row["config"],
        }
        if structural != expected_structural:
            raise PackageVerificationError("effective structural config differs from one or more exact RUN/R snapshots")
        generator_version = item["generator_version"]
        if generator_version != row["generator_version"]:
            raise PackageVerificationError("effective ScenarioConfig generator_version differs from RunManifest")
        generator_versions[key[0]].add(generator_version)
        consumed[scenario_key] += 1
    if any(count != M * (1 + R) for count in consumed.values()):
        raise PackageVerificationError("effective ScenarioConfig row was not consumed by every expected RUN/R snapshot")
    if any(len(values) != 1 for values in generator_versions.values()):
        raise PackageVerificationError("Generator.version differs across RUN/R snapshots within a scenario")
    return len(rows)


def _reconcile_effective_scenario_configs(files: Mapping[str, Any], decoded_report: Any) -> int:
    effective_file = files.get("design/effective_scenario_configs.json")
    run_file = files.get("runs/run_records.json")
    report = decoded_report.get("report") if isinstance(decoded_report, dict) else None
    design = report.get("design") if isinstance(report, dict) else None
    if not isinstance(run_file, dict) or not isinstance(run_file.get("run_evidence_records"), list):
        raise PackageVerificationError("RUN evidence records are missing for effective ScenarioConfig reconciliation")
    decoded_runs = []
    for index, record in enumerate(run_file["run_evidence_records"]):
        if not isinstance(record, dict) or not isinstance(record.get("snapshot_refs"), dict):
            raise PackageVerificationError(f"RUN record {index} lacks snapshot refs for effective ScenarioConfig reconciliation")
        key = _logical_run_key(record.get("key"), f"effective-config run record {index}")
        refs = record["snapshot_refs"]
        config = _snapshot_fields(
            decode_frozen_snapshot_ref(
                refs.get("scenario_config"),
                expected_type_id="vcont_integrated_harness.ScenarioConfig",
            ),
            "vcont_integrated_harness.ScenarioConfig",
        )
        manifest = _snapshot_fields(
            decode_frozen_snapshot_ref(
                refs.get("run_manifest"),
                expected_type_id="vcont_integrated_harness.RunManifest",
            ),
            "vcont_integrated_harness.RunManifest",
        )
        decoded_runs.append({
            "key": key,
            "config": config,
            "generator_version": manifest.get("generator_version"),
        })
    return _reconcile_effective_scenario_config_rows(effective_file, design, decoded_runs)


def _reconcile_benchmark_export_identity(files: Mapping[str, Any]) -> str:
    """Reconcile the capture identity across every companion that declares it by contract."""
    run_file = files.get("runs/run_records.json")
    gate159 = files.get("validation/reconciliation_results.json")
    if not isinstance(run_file, dict):
        raise PackageVerificationError("RUN export companion is missing for benchmark_export_id reconciliation")
    if not isinstance(gate159, dict):
        raise PackageVerificationError("Gate159 companion is missing for benchmark_export_id reconciliation")
    export_id = run_file.get("benchmark_export_id")
    if not isinstance(export_id, str) or not re.fullmatch(r"[0-9a-f]{64}", export_id):
        raise PackageVerificationError("RUN export benchmark_export_id is not a lowercase SHA-256 identity")
    if (gate159.get("schema_id"), gate159.get("schema_version")) != (
        "TGCV-C10S-VCONT-GATE159-RECONCILIATION", "1.0.0"
    ):
        raise PackageVerificationError("Gate159 companion schema/version differs from its frozen contract")
    if gate159.get("benchmark_export_id") != export_id:
        raise PackageVerificationError("Gate159 benchmark_export_id differs from RUN export capture identity")
    return export_id


def _reconcile_run_records(files: Mapping[str, Any], decoded_report: Any) -> tuple[int, int]:
    """Rebuild RUN/R and outer-world joins from the package's independent sources."""
    run_file = files["runs/run_records.json"]
    root_fields = {
        "schema_id", "schema_version", "benchmark_export_id", "declared_cardinality",
        "ordering_profile", "join_key_profile", "run_evidence_records",
        "outer_world_evidence_records", "evidence_index",
    }
    if not isinstance(run_file, dict) or set(run_file) != root_fields:
        raise PackageVerificationError("RUN export envelope exact root field allowlist mismatch")
    if (run_file["schema_id"], run_file["schema_version"]) != (
        "TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE", "2.0.0"
    ):
        raise PackageVerificationError("RUN export envelope schema/version mismatch")
    if (not isinstance(run_file["benchmark_export_id"], str)
            or not re.fullmatch(r"[0-9a-f]{64}", run_file["benchmark_export_id"])
            or not isinstance(run_file["ordering_profile"], str) or not run_file["ordering_profile"]
            or not isinstance(run_file["join_key_profile"], str) or not run_file["join_key_profile"]):
        raise PackageVerificationError("RUN export identity/order/join profile declarations are malformed")
    report = decoded_report.get("report") if isinstance(decoded_report, dict) else None
    design = report.get("design") if isinstance(report, dict) else None
    if not isinstance(design, dict):
        raise PackageVerificationError("report design identity is missing for RUN/R reconciliation")
    scenario_versions = design.get("scenario_versions")
    n_units, M, R = design.get("n_units"), design.get("outer_replicates"), design.get("repeated_assignments")
    if (not isinstance(scenario_versions, list) or len(scenario_versions) != 13
            or isinstance(n_units, bool) or not isinstance(n_units, int)
            or isinstance(M, bool) or not isinstance(M, int)
            or isinstance(R, bool) or not isinstance(R, int)):
        raise PackageVerificationError("report design dimensions/scenario registry are malformed")
    if (any(not isinstance(row, list) or len(row) != 2
            or not all(isinstance(value, str) and value for value in row)
            for row in scenario_versions)
            or tuple(row[0] for row in scenario_versions) != AUTHORITATIVE_SCENARIO_IDS):
        raise PackageVerificationError("report design scenario registry differs from frozen authoritative order")
    scenario_order = [row[0] for row in scenario_versions]
    versions = {row[0]: row[1] for row in scenario_versions}
    report_manifest = report.get("manifest")
    if (not isinstance(report_manifest, dict)
            or report_manifest.get("scenario_versions") != scenario_versions
            or report_manifest.get("N") != n_units
            or report_manifest.get("M") != M
            or report_manifest.get("R") != R
            or report_manifest.get("matrix_fingerprint") != design.get("matrix_fingerprint")):
        raise PackageVerificationError("report design and legacy manifest identities/dimensions diverge")
    expected_runs = 13 * M * (1 + R)
    expected_outers = 13 * M
    declared = run_file["declared_cardinality"]
    if declared != {
        "scenario_count": 13, "pair_count": 52, "outer_world_count": expected_outers,
        "run_record_count": expected_runs, "repeated_report_count": expected_outers,
    }:
        raise PackageVerificationError("RUN export declared cardinalities differ from report design")
    records = run_file["run_evidence_records"]
    outer_records = run_file["outer_world_evidence_records"]
    if (not isinstance(records, list) or len(records) != expected_runs
            or not isinstance(outer_records, list) or len(outer_records) != expected_outers):
        raise PackageVerificationError("RUN/R source record cardinality differs from 13 x M x (1+R)")

    assignment_file = files["seeds/evaluation_seed_assignments.json"]
    temporal_file = files["runs/temporal_manifest.json"]
    for label, envelope, schema_id in (
        ("evaluation assignments", assignment_file, "TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS"),
        ("temporal manifest", temporal_file, "TGCV-C10S-VCONT-TEMPORAL-MANIFEST"),
    ):
        if (not isinstance(envelope, dict) or envelope.get("schema_id") != schema_id
                or envelope.get("schema_version") != "2.0.0"
                or not isinstance(envelope.get("rows"), list)
                or envelope.get("row_count") != len(envelope["rows"])):
            raise PackageVerificationError(f"{label}: exact v2 rows envelope is invalid")

    def decode_wire_seed_row(row: dict[str, Any], label: str) -> dict[str, Any]:
        if not isinstance(row, dict):
            raise PackageVerificationError(f"{label}: row must be an object")
        result = dict(row)
        for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
            result[field] = _uint64(row.get(field), f"{label}.{field}")
        return result

    assignment_rows = [decode_wire_seed_row(row, f"evaluation assignments[{i}]")
                       for i, row in enumerate(assignment_file["rows"])]
    temporal_rows = [decode_wire_seed_row(row, f"temporal manifest[{i}]")
                     for i, row in enumerate(temporal_file["rows"])]
    assignment_map: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in assignment_rows:
        required = {"bank", "scenario_id", "scenario_version", "n_units", "replicate",
                    "outer_replicate_id", "assignment_role", "world_seed",
                    "z_assignment_seed", "g_assignment_seed"}
        if set(row) != required or row["bank"] != "evaluation":
            raise PackageVerificationError("evaluation SeedAssignment row field/bank mismatch")
        if (not isinstance(row["scenario_id"], str) or not row["scenario_id"]
                or not isinstance(row["scenario_version"], str) or not row["scenario_version"]
                or isinstance(row["n_units"], bool) or not isinstance(row["n_units"], int) or row["n_units"] < 1
                or isinstance(row["replicate"], bool) or not isinstance(row["replicate"], int)
                or not isinstance(row["outer_replicate_id"], str) or not row["outer_replicate_id"]
                or row["assignment_role"] not in ("RUN", "REPEATED_ASSIGNMENT")):
            raise PackageVerificationError("evaluation SeedAssignment identity field types are invalid")
        key = (row["scenario_id"], row["scenario_version"], row["n_units"],
               row["outer_replicate_id"], row["assignment_role"], row["replicate"])
        if key in assignment_map:
            raise PackageVerificationError("duplicate evaluation SeedAssignment logical key")
        assignment_map[key] = row
    temporal_map: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in temporal_rows:
        required = {"scenario_id", "scenario_version", "N", "outer_replicate_id",
                    "assignment_role", "assignment_index", "run_id", "world_id",
                    "world_seed", "z_assignment_seed", "g_assignment_seed"}
        if set(row) != required:
            raise PackageVerificationError("temporal RunManifest projection field allowlist mismatch")
        if (not isinstance(row["scenario_id"], str) or not row["scenario_id"]
                or not isinstance(row["scenario_version"], str) or not row["scenario_version"]
                or isinstance(row["N"], bool) or not isinstance(row["N"], int) or row["N"] < 1
                or not isinstance(row["outer_replicate_id"], str) or not row["outer_replicate_id"]
                or row["assignment_role"] not in ("RUN", "REPEATED_ASSIGNMENT")
                or isinstance(row["assignment_index"], bool) or not isinstance(row["assignment_index"], int)
                or not isinstance(row["run_id"], str) or not row["run_id"]
                or not isinstance(row["world_id"], str) or not row["world_id"]):
            raise PackageVerificationError("temporal RunManifest identity field types are invalid")
        key = (row["scenario_id"], row["scenario_version"], row["N"],
               row["outer_replicate_id"], row["assignment_role"], row["assignment_index"])
        if key in temporal_map:
            raise PackageVerificationError("duplicate temporal manifest logical key")
        temporal_map[key] = row
    expected_keys = {
        (sid, versions[sid], n_units, f"outer-{m:06d}", role, index)
        for sid in scenario_order for m in range(M)
        for role, index in ([("RUN", -1)] + [
            ("REPEATED_ASSIGNMENT", r) for r in range(R)
        ])
    }
    if set(assignment_map) != expected_keys or set(temporal_map) != expected_keys:
        raise PackageVerificationError("assignment/temporal key sets differ from exact report design RUN/R universe")
    expected_order = [
        (sid, versions[sid], n_units, f"outer-{m:06d}", role, index)
        for sid in scenario_order for m in range(M)
        for role, index in ([("RUN", -1)] + [
            ("REPEATED_ASSIGNMENT", repeat_index) for repeat_index in range(R)
        ])
    ]
    assignment_order = [
        (row["scenario_id"], row["scenario_version"], row["n_units"],
         row["outer_replicate_id"], row["assignment_role"], row["replicate"])
        for row in assignment_rows
    ]
    temporal_order = [
        (row["scenario_id"], row["scenario_version"], row["N"],
         row["outer_replicate_id"], row["assignment_role"], row["assignment_index"])
        for row in temporal_rows
    ]
    if assignment_order != expected_order or temporal_order != expected_order:
        raise PackageVerificationError("assignment/temporal rows are not in canonical scenario/M/R order")

    run_map: dict[tuple[Any, ...], dict[str, Any]] = {}
    decoded_by_key: dict[tuple[Any, ...], dict[str, dict[str, Any]]] = {}
    snapshot_fields = {
        "assignment": "vcont_benchmark_protocol.SeedAssignment",
        "scenario_config": "vcont_integrated_harness.ScenarioConfig",
        "run_manifest": "vcont_integrated_harness.RunManifest",
        "truth_projection": "vcont_evidence_export.MatrixTruthProjection",
        "evidence_candidate": "vcont_integrated_harness.EvidenceCandidate",
        "sealed_evidence": "vcont_integrated_harness.SealedEvidence",
        "analysis_contract": "vcont_integrated_harness.AnalysisContract",
        "analyzer_result": "vcont_integrated_harness.AnalyzerResult",
        "evaluation_report": "vcont_integrated_harness.EvaluationReport",
    }
    record_required = {
        "key", "bank", "snapshot_refs", "scenario_config_structural_sha256",
        "analysis_contract_sha256", "sealed_evidence_legacy_sha256",
        "snapshot_validation_status",
    }
    for index, record in enumerate(records):
        if not isinstance(record, dict) or set(record) != record_required:
            raise PackageVerificationError(f"run_evidence_records[{index}]: exact record field allowlist mismatch")
        key = _logical_run_key(record["key"], f"run_evidence_records[{index}].key")
        if key in run_map:
            raise PackageVerificationError("duplicate logical RUN/R key in run_evidence_records")
        if record["bank"] != "evaluation":
            raise PackageVerificationError("confirmatory RUN/R record is not in evaluation bank")
        refs = record["snapshot_refs"]
        if not isinstance(refs, dict) or set(refs) != set(snapshot_fields):
            raise PackageVerificationError("run record snapshot_refs field allowlist mismatch")
        decoded = {}
        for name, type_id in snapshot_fields.items():
            decoded[name] = _snapshot_fields(
                decode_frozen_snapshot_ref(refs[name], expected_type_id=type_id), type_id
            )
        assignment = decoded["assignment"]
        config = decoded["scenario_config"]
        manifest = decoded["run_manifest"]
        truth = decoded["truth_projection"]
        candidate = decoded["evidence_candidate"]
        sealed = decoded["sealed_evidence"]
        contract = decoded["analysis_contract"]
        analyzer = decoded["analyzer_result"]
        evaluation = decoded["evaluation_report"]
        if (not isinstance(assignment["scenario_id"], str) or not assignment["scenario_id"]
                or not isinstance(assignment["scenario_version"], str) or not assignment["scenario_version"]
                or isinstance(assignment["n_units"], bool) or not isinstance(assignment["n_units"], int)
                or isinstance(assignment["replicate"], bool) or not isinstance(assignment["replicate"], int)
                or not isinstance(assignment["outer_replicate_id"], str)
                or not isinstance(config["n_units"], int) or isinstance(config["n_units"], bool)
                or not isinstance(config["assignment_index"], int) or isinstance(config["assignment_index"], bool)
                or not isinstance(manifest["n_units"], int) or isinstance(manifest["n_units"], bool)
                or not isinstance(manifest["assignment_index"], int) or isinstance(manifest["assignment_index"], bool)):
            raise PackageVerificationError("snapshot assignment/config/manifest identity field types are invalid")
        identity = (assignment["scenario_id"], assignment["scenario_version"], assignment["n_units"],
                    assignment["outer_replicate_id"], assignment["assignment_role"],
                    assignment["replicate"])
        expected_key = (key[0], key[1], key[2], key[3], key[4], key[5])
        if identity != expected_key or assignment["bank"] != record["bank"]:
            raise PackageVerificationError("SeedAssignment identity/bank differs from run record key")
        if key[6] != manifest["run_id"]:
            raise PackageVerificationError("run record key run_id differs from RunManifest")
        if (config["scenario_id"], config["version"], config["n_units"],
            config["outer_replicate_id"], config["assignment_role"], config["assignment_index"]) != expected_key:
            raise PackageVerificationError("ScenarioConfig identity differs from full RUN/R key")
        if (manifest["scenario_id"], manifest["version"], manifest["n_units"],
            manifest["outer_replicate_id"], manifest["assignment_role"],
            manifest["assignment_index"]) != expected_key:
            raise PackageVerificationError("RunManifest identity differs from full RUN/R key")
        if manifest["run_id"] != key[6] or config["replicate_id"] != manifest["replicate_id"]:
            raise PackageVerificationError("RunManifest/config replicate or run_id identity mismatch")
        if manifest["world_version"] != config["version"]:
            raise PackageVerificationError("RunManifest world_version differs from ScenarioConfig version")
        expected_window_end = config["last_transition_support"] + config["follow_up"]
        expected_interval_width = (expected_window_end - config["window_start"]) / config["n_intervals"]
        if (manifest["n_intervals"], manifest["window_start"], manifest["window_end"],
            manifest["interval_width"]) != (
            config["n_intervals"], config["window_start"], expected_window_end, expected_interval_width
        ):
            raise PackageVerificationError("RunManifest temporal design differs from ScenarioConfig")
        _assert_snapshot_seed_relations(assignment, config, manifest, truth)
        if (truth["run_id"], truth["outer_replicate_id"], truth["assignment_role"],
            truth["assignment_index"]) != (key[6], key[3], key[4], key[5]):
            raise PackageVerificationError("MatrixTruthProjection run/M/role/index identity differs from key")
        if any(obj.get("run_id") != key[6] for obj in (candidate, sealed, analyzer, evaluation)):
            raise PackageVerificationError("run-scoped evidence/analyzer/evaluation object run_id mismatch")
        if (analyzer["outer_replicate_id"], analyzer["assignment_role"], analyzer["assignment_index"]) != (
            key[3], key[4], key[5]
        ):
            raise PackageVerificationError("AnalyzerResult RUN/R identity differs from logical key")
        if (contract["estimand_id"], contract["estimand_version"]) != (
            analyzer["estimand_id"], analyzer["estimand_version"]
        ):
            raise PackageVerificationError("AnalysisContract/AnalyzerResult estimand identity mismatch")
        if (contract["target_regime_id"], contract["target_regime_version"],
            contract["outcome_id"], contract["outcome_version"]) != (
            analyzer["target_regime_id"], analyzer["target_regime_version"],
            analyzer["outcome_id"], analyzer["outcome_version"]
        ):
            raise PackageVerificationError("AnalysisContract/AnalyzerResult target/outcome identity mismatch")
        contract_result_fields = (
            "run_conditional_estimand_id", "run_conditional_estimand_version",
            "reference_regime_estimand_id", "reference_regime_estimand_version",
            "g_assignment_estimand_id", "g_assignment_estimand_version",
            "transportability_id", "transportability_version", "transportability_scope",
            "transportability_evidence_status", "transportability_outcome_id", "transportability_basis",
        )
        if any(contract[name] != analyzer[name] for name in contract_result_fields):
            raise PackageVerificationError("AnalysisContract/AnalyzerResult transportability or estimand identity mismatch")
        if (contract["g_assignment_mechanism_id"], contract["g_assignment_mechanism_version"],
            contract["g_assignment_mechanism_hash"], contract["z_assignment_mechanism_id"],
            contract["z_assignment_mechanism_version"], contract["z_assignment_mechanism_hash"],
            contract["reference_regime_id"], contract["reference_regime_version"]) != (
            analyzer["g_assignment_mechanism_id"], analyzer["g_assignment_mechanism_version"],
            analyzer["g_assignment_mechanism_hash"], analyzer["z_assignment_mechanism_id"],
            analyzer["z_assignment_mechanism_version"], analyzer["z_assignment_mechanism_hash"],
            analyzer["reference_regime_id"], analyzer["reference_regime_version"]
        ):
            raise PackageVerificationError("AnalysisContract/AnalyzerResult mechanism identity mismatch")
        contract_manifest_fields = (
            "g_assignment_mechanism_id", "g_assignment_mechanism_version",
            "g_assignment_mechanism_hash", "z_assignment_mechanism_id",
            "z_assignment_mechanism_version", "z_assignment_mechanism_hash",
            "reference_regime_id", "reference_regime_version",
        )
        manifest_fields = (
            "g_assignment_mechanism_id", "g_assignment_mechanism_version",
            "g_assignment_mechanism_hash", "z_assignment_mechanism_id",
            "z_assignment_mechanism_version", "z_assignment_mechanism_hash",
            "g_reference_regime_id", "g_reference_regime_version",
        )
        if tuple(contract[name] for name in contract_manifest_fields) != tuple(
            manifest[name] for name in manifest_fields
        ):
            raise PackageVerificationError("AnalysisContract mechanism/reference identity differs from RunManifest")
        if (record["analysis_contract_sha256"] != refs["analysis_contract"]["sha256"]
                or record["sealed_evidence_legacy_sha256"] != sealed["sha256"]):
            raise PackageVerificationError("run record declared contract/sealed digest differs from decoded source")
        structural_config = {
            name: value for name, value in config.items()
            if name not in {
                "seed", "world_seed", "z_assignment_seed", "g_assignment_seed",
                "replicate_id", "outer_replicate_id", "assignment_role", "assignment_index",
            }
        }
        if record["scenario_config_structural_sha256"] != _snapshot_source_digest(structural_config):
            raise PackageVerificationError("ScenarioConfig structural digest does not recompute")
        sealed_digest = _snapshot_legacy_sealed_digest(sealed)
        if sealed_digest != sealed["sha256"] or analyzer["input_sha256"] != sealed_digest:
            raise PackageVerificationError("SealedEvidence legacy digest differs from AnalyzerResult.input_sha256")
        if candidate["rows"] != sealed["rows"] or candidate["provenance"] != sealed["manifest"].get("provenance"):
            raise PackageVerificationError("EvidenceCandidate and SealedEvidence rows/provenance diverge")
        if sealed["manifest"].get("row_count") != len(sealed["rows"]):
            raise PackageVerificationError("SealedEvidence row_count differs from retained rows")
        provenance = sealed["manifest"].get("provenance", {})
        _assert_sealed_provenance_identity(
            provenance, key[6], assignment, config, manifest, analyzer
        )
        if key[4] == "RUN" and key[5] != -1:
            raise PackageVerificationError("designated RUN must use assignment_index -1")
        if key[4] == "REPEATED_ASSIGNMENT" and key[5] < 0:
            raise PackageVerificationError("repeated assignment index must be nonnegative")
        _register_unique_run_record(run_map, decoded_by_key, key, record, decoded)

    if len(run_map) != expected_runs:
        raise PackageVerificationError("run record cardinality mismatch")
    run_ids = [key[6] for key in run_map]
    if len(set(run_ids)) != len(run_ids):
        raise PackageVerificationError("run_id is duplicated across distinct logical RUN/R keys")
    observed_run_order = [key[:6] for key in run_map]
    if observed_run_order != expected_order:
        raise PackageVerificationError("run_evidence_records are not in canonical scenario/M/R order")
    # Each assignment/temporal key must map to one unique run record and exact run_id.
    key6_to_run = {}
    for key, record in run_map.items():
        base = key[:6]
        if base in key6_to_run:
            raise PackageVerificationError("more than one run record consumes a logical assignment key")
        key6_to_run[base] = (key, record)
        assignment = assignment_map[base]
        temporal = temporal_map[base]
        manifest = decoded_by_key[key]["run_manifest"]
        for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
            if assignment[field] != manifest[field] or temporal[field] != manifest[field]:
                raise PackageVerificationError("assignment/temporal/RunManifest seed stream join failed")
        if temporal["run_id"] != key[6] or temporal["world_id"] != manifest["world_id"]:
            raise PackageVerificationError("temporal manifest run_id/world_id differs from RunManifest")
    if set(key6_to_run) != expected_keys:
        raise PackageVerificationError("one-to-one RUN/R assignment to run-record consumption failed")

    outer_map = {}
    expected_outer_order = [
        (sid, versions[sid], n_units, f"outer-{m:06d}")
        for sid in scenario_order for m in range(M)
    ]
    observed_outer_order = []
    for index, outer in enumerate(outer_records):
        required = {"key", "run_record_key", "repeated_run_record_keys",
                    "repeated_assignment_report", "bank"}
        if not isinstance(outer, dict) or set(outer) != required:
            raise PackageVerificationError(f"outer_world_evidence_records[{index}] field allowlist mismatch")
        key = outer["key"]
        if not isinstance(key, dict) or set(key) != {
            "scenario_id", "scenario_version", "N", "outer_replicate_id",
            "world_id", "world_version", "world_seed",
        }:
            raise PackageVerificationError("outer-world key field allowlist mismatch")
        if (not isinstance(key["scenario_id"], str) or not key["scenario_id"]
                or not isinstance(key["scenario_version"], str) or not key["scenario_version"]
                or isinstance(key["N"], bool) or not isinstance(key["N"], int) or key["N"] < 1
                or not isinstance(key["outer_replicate_id"], str) or not key["outer_replicate_id"]
                or not isinstance(key["world_id"], str) or not key["world_id"]
                or not isinstance(key["world_version"], str) or not key["world_version"]):
            raise PackageVerificationError("outer-world key identity field types are invalid")
        world_seed = _uint64(key["world_seed"], f"outer_world_evidence_records[{index}].key.world_seed")
        outer_key = (key["scenario_id"], key["scenario_version"], key["N"],
                     key["outer_replicate_id"], key["world_id"])
        if outer_key in outer_map:
            raise PackageVerificationError("duplicate outer-world logical key")
        if outer["bank"] != "evaluation":
            raise PackageVerificationError("outer-world record bank must be evaluation")
        base = (key["scenario_id"], key["scenario_version"], key["N"], key["outer_replicate_id"])
        run_key, run_manifest = _resolve_outer_world_run_reference(
            outer["run_record_key"], "outer_world.run_record_key", base, "RUN", -1,
            run_map, decoded_by_key, (key["world_id"], key["world_version"], world_seed),
        )
        repeated_keys = outer["repeated_run_record_keys"]
        if not isinstance(repeated_keys, list) or len(repeated_keys) != R:
            raise PackageVerificationError("outer-world repeated RUN references differ from R")
        expected_repeated = []
        for repeat_index, ref_key in enumerate(repeated_keys):
            parsed_key, repeated_manifest = _resolve_outer_world_run_reference(
                ref_key, f"outer_world.repeated_run_record_keys[{repeat_index}]",
                base, "REPEATED_ASSIGNMENT", repeat_index, run_map, decoded_by_key,
                (key["world_id"], key["world_version"], world_seed),
            )
            expected_repeated.append(parsed_key)
        repeated_z, repeated_g = set(), set()
        for parsed_key in [run_key] + expected_repeated:
            assignment = decoded_by_key[parsed_key]["assignment"]
            if assignment["world_seed"] != world_seed:
                raise PackageVerificationError("RUN/R assignment world_seed differs from outer-world key")
            if assignment["z_assignment_seed"] in repeated_z or assignment["g_assignment_seed"] in repeated_g:
                raise PackageVerificationError("Z/G assignment streams are not unique within outer world")
            repeated_z.add(assignment["z_assignment_seed"])
            repeated_g.add(assignment["g_assignment_seed"])
        repeated_report = _snapshot_fields(
            decode_frozen_snapshot_ref(
                outer["repeated_assignment_report"],
                expected_type_id="vcont_integrated_harness.RepeatedAssignmentReport",
            ),
            "vcont_integrated_harness.RepeatedAssignmentReport",
        )
        repeated_evaluations = tuple(
            decoded_by_key[parsed_key]["evaluation_report"]
            for parsed_key in expected_repeated
        )
        if (repeated_report["world_id"] != key["world_id"]
                or repeated_report["replicate_count"] != R
                or tuple(repeated_report["per_run_reports"]) != repeated_evaluations):
            raise PackageVerificationError("RepeatedAssignmentReport does not match exact ordered R evaluation reports")
        outer_map[outer_key] = {
            "run_key": run_key, "repeated_keys": tuple(expected_repeated),
            "world_seed": world_seed, "world_id": key["world_id"],
            "repeated_report": repeated_report,
        }
        observed_outer_order.append(outer_key[:4])
    if len(outer_map) != expected_outers:
        raise PackageVerificationError("outer-world record cardinality differs from 13 x M")
    if observed_outer_order != expected_outer_order:
        raise PackageVerificationError("outer-world evidence records are not in canonical scenario/M order")
    outer_by_base = {
        (key[0], key[1], key[2], key[3]): value for key, value in outer_map.items()
    }
    expected_bases = {
        (sid, versions[sid], n_units, f"outer-{m:06d}")
        for sid in scenario_order for m in range(M)
    }
    if set(outer_by_base) != expected_bases:
        raise PackageVerificationError("outer-world keys do not cover exact scenario/M universe")
    # RUN/R world identity and world seed are constant within each outer-world cluster.
    for base, outer in outer_by_base.items():
        run_key = outer["run_key"]
        run_assignment = decoded_by_key[run_key]["assignment"]
        if run_assignment["world_seed"] != outer["world_seed"]:
            raise PackageVerificationError("designated RUN assignment world_seed differs from outer-world key")
        for repeated_key in outer["repeated_keys"]:
            if decoded_by_key[repeated_key]["assignment"]["world_seed"] != outer["world_seed"]:
                raise PackageVerificationError("repeated assignment world_seed differs from outer-world key")

    # Temporal rows and report's duplicated temporal views must consume each run once.
    report_temporal = report.get("temporal_manifest")
    if not isinstance(report_temporal, list) or len(report_temporal) != expected_runs:
        raise PackageVerificationError("report temporal manifest cardinality differs from RUN/R universe")
    report_temporal_map = {}
    for row in report_temporal:
        key = (row["scenario_id"], row["scenario_version"], row["N"],
               row["outer_replicate_id"], row["assignment_role"], row["assignment_index"])
        if key in report_temporal_map:
            raise PackageVerificationError("duplicate report temporal key")
        report_temporal_map[key] = row
    if set(report_temporal_map) != expected_keys:
        raise PackageVerificationError("report temporal manifest does not cover exact RUN/R universe")
    for base, (key, _) in key6_to_run.items():
        temporal = temporal_map[base]
        report_row = report_temporal_map[base]
        if report_row != temporal:
            raise PackageVerificationError("report temporal row differs from runs/temporal_manifest row")
        manifest = decoded_by_key[key]["run_manifest"]
        if report_row["run_id"] != key[6] or report_row["world_id"] != manifest["world_id"]:
            raise PackageVerificationError("report temporal row run/world identity differs from snapshot")

    # Pair ledger contributions must consume each outer-world RUN world seed once per pair.
    pair_rows = report.get("pair_ledger")
    if not isinstance(pair_rows, list) or len(pair_rows) != 52:
        raise PackageVerificationError("report pair ledger must retain 52 rows")
    for pair_index, pair in enumerate(pair_rows):
        contributions = pair.get("contributions") if isinstance(pair, dict) else None
        if not isinstance(contributions, list) or len(contributions) != M:
            raise PackageVerificationError(f"pair ledger[{pair_index}] contribution count differs from M")
        seen_m = set()
        observed_contribution_order = []
        for contribution in contributions:
            outer_id = contribution.get("outer_replicate_id")
            if outer_id in seen_m:
                raise PackageVerificationError("pair ledger duplicates an M contribution")
            seen_m.add(outer_id)
            scenario_id = pair["key"][0]
            base = (scenario_id, versions[scenario_id], n_units, outer_id)
            outer = outer_by_base.get(base)
            if (outer is None or contribution.get("world_seed") != outer["world_seed"]
                    or contribution.get("world_id") != outer["world_id"]
                    or contribution.get("run_id") != outer["run_key"][6]):
                raise PackageVerificationError("pair-ledger contribution identity/world seed differs from its designated RUN")
            observed_contribution_order.append(outer_id)
        if observed_contribution_order != [f"outer-{m:06d}" for m in range(M)]:
            raise PackageVerificationError("pair-ledger contributions are not in canonical M order")
        if seen_m != {f"outer-{m:06d}" for m in range(M)}:
            raise PackageVerificationError("pair ledger does not consume every M contribution exactly once")

    # The report RUN tuple and aggregate report rows are independently compared with snapshots.
    scenarios = report.get("scenario_reports")
    if not isinstance(scenarios, dict) or set(scenarios) != set(scenario_order):
        raise PackageVerificationError("scenario_reports registry differs from design")
    for sid in scenario_order:
        scenario = scenarios[sid]
        if (scenario.get("scenario_id"), scenario.get("scenario_version")) != (sid, versions[sid]):
            raise PackageVerificationError("scenario report identity differs from design")
        if scenario.get("n_units") != n_units or scenario.get("outer_replicate_count") != M:
            raise PackageVerificationError("scenario report N/M dimensions differ from design")
        per_outer = scenario.get("per_outer_replicate")
        if not isinstance(per_outer, list) or len(per_outer) != M:
            raise PackageVerificationError("scenario report per_outer_replicate cardinality mismatch")
        for m, row in enumerate(per_outer):
            outer_id = f"outer-{m:06d}"
            base = (sid, versions[sid], n_units, outer_id)
            outer = outer_by_base[base]
            run_key = outer["run_key"]
            decoded = decoded_by_key[run_key]
            run_tuple = row.get("run")
            if not isinstance(run_tuple, list) or len(run_tuple) != 4:
                raise PackageVerificationError("scenario report RUN tuple must have four ordered objects")
            truth, analyzer_report, contract_report, manifest_report = run_tuple
            if not isinstance(truth, dict):
                raise PackageVerificationError("scenario report TruthBundle projection is missing")
            truth_snapshot = decoded["truth_projection"]
            analyzer_snapshot = decoded["analyzer_result"]
            contract_snapshot = decoded["analysis_contract"]
            manifest_snapshot = decoded["run_manifest"]
            if (truth.get("run_id"), truth.get("outer_replicate_id"),
                truth.get("assignment_role"), truth.get("assignment_index"), truth.get("seed")) != (
                run_key[6], outer_id, "RUN", -1, decoded["scenario_config"]["seed"]
            ):
                raise PackageVerificationError("report TruthBundle identity/seed differs from captured RUN")
            if truth_snapshot["seed"] != decoded["scenario_config"]["seed"]:
                raise PackageVerificationError("MatrixTruthProjection.seed differs from ScenarioConfig.seed")
            if any(truth.get(name) != value for name, value in truth_snapshot.items()):
                raise PackageVerificationError("report TruthBundle fields diverge from retained MatrixTruthProjection")
            for report_obj, snapshot_obj, label in (
                (analyzer_report, analyzer_snapshot, "AnalyzerResult"),
                (contract_report, contract_snapshot, "AnalysisContract"),
                (manifest_report, manifest_snapshot, "RunManifest"),
            ):
                _assert_report_snapshot_projection(report_obj, snapshot_obj, f"report RUN {label}")
            _assert_report_snapshot_projection(
                row.get("run_report"), decoded["evaluation_report"], "report RUN EvaluationReport"
            )
            _assert_report_snapshot_projection(
                row.get("repeated_report"), outer["repeated_report"], "report RepeatedAssignmentReport"
            )

    # Evidence index is an exact, ordered one-to-one projection of outer-world keys.
    evidence_index = run_file["evidence_index"]
    if not isinstance(evidence_index, list) or len(evidence_index) != expected_outers:
        raise PackageVerificationError("RUN evidence_index cardinality differs from 13 x M")
    # The evidence_index world_id is compared to the corresponding outer key, not to run_id.
    consumed_index = set()
    observed_index_order = []
    for row in evidence_index:
        if not isinstance(row, dict) or set(row) != {"scenario_id", "outer_replicate_id", "world_id"}:
            raise PackageVerificationError("evidence_index row field allowlist mismatch")
        base = (row["scenario_id"], versions.get(row["scenario_id"]), n_units, row["outer_replicate_id"])
        outer_key = next((k for k in outer_map if k[:4] == base), None)
        if outer_key is None or row["world_id"] != outer_key[4]:
            raise PackageVerificationError("evidence_index row does not resolve to exact outer-world identity")
        if base in consumed_index:
            raise PackageVerificationError("evidence_index duplicates an outer-world key")
        consumed_index.add(base)
        observed_index_order.append(base)
    if observed_index_order != expected_outer_order:
        raise PackageVerificationError("evidence_index is not in canonical scenario/M order")
    if consumed_index != expected_bases:
        raise PackageVerificationError("evidence_index does not consume every outer-world key exactly once")
    return len(run_map), len(outer_map)




def _reconcile_matrix_pair_ledger(matrix: Any, decoded_report: Any) -> None:
    """Join each ordered pair-ledger row to its exact MatrixCapture identity."""
    if not isinstance(matrix, dict) or not isinstance(matrix.get("rows"), list) or len(matrix["rows"]) != 52:
        raise PackageVerificationError("MatrixCapture must contain exactly 52 rows for pair-ledger reconciliation")
    report = decoded_report.get("report") if isinstance(decoded_report, dict) else None
    if not isinstance(report, dict) or not isinstance(report.get("pair_ledger"), list):
        raise PackageVerificationError("report pair ledger is missing for MatrixCapture reconciliation")
    ledger = report["pair_ledger"]
    if len(ledger) != 52:
        raise PackageVerificationError("pair ledger must contain exactly 52 rows for MatrixCapture reconciliation")
    expected_matrix_fields = {
        "key", "evaluation_class", "truth_status", "dgp_truth_field",
        "analyzer_output_field", "aggregation_field", "identification_expectation",
        "abstention_expectation", "tolerance_id", "reason",
        "run_evaluation_class", "repeated_evaluation_class",
    }
    report_design = report.get("design")
    scenario_versions = report_design.get("scenario_versions") if isinstance(report_design, dict) else None
    if (not isinstance(scenario_versions, list)
            or tuple(row[0] for row in scenario_versions
                     if isinstance(row, list) and len(row) == 2) != AUTHORITATIVE_SCENARIO_IDS):
        raise PackageVerificationError("MatrixCapture join lacks authoritative scenario order")
    expected_matrix_identities = [
        (sid, version, estimand_id, "001")
        for sid, version in scenario_versions
        for estimand_id in AUTHORITATIVE_ESTIMAND_IDS
    ]
    if len(expected_matrix_identities) != 52:
        raise PackageVerificationError("frozen scenario/estimand universe is not exactly 52 pairs")
    seen_matrix_keys = set()
    seen_pair_keys = set()
    for index, (matrix_row, pair_row) in enumerate(zip(matrix["rows"], ledger)):
        if not isinstance(matrix_row, dict) or set(matrix_row) != expected_matrix_fields:
            raise PackageVerificationError(f"MatrixCapture row {index} field allowlist mismatch")
        key = matrix_row["key"]
        if not isinstance(key, dict) or set(key) != {
            "scenario_id", "scenario_version", "estimand_id", "estimand_version",
        }:
            raise PackageVerificationError(f"MatrixCapture row {index} identity field allowlist mismatch")
        identity = tuple(key[name] for name in (
            "scenario_id", "scenario_version", "estimand_id", "estimand_version",
        ))
        if any(not isinstance(value, str) or not value for value in identity):
            raise PackageVerificationError(f"MatrixCapture row {index} identity values are invalid")
        if identity != expected_matrix_identities[index]:
            raise PackageVerificationError(f"MatrixCapture row {index} differs from frozen 13 x 4 scenario/estimand order")
        if identity in seen_matrix_keys:
            raise PackageVerificationError("MatrixCapture contains a duplicate scenario/estimand identity")
        seen_matrix_keys.add(identity)
        if matrix_row["evaluation_class"] not in (
            "EVALUABLE", "STATUS_ONLY", "NOT_IDENTIFIABLE", "NOT_EVALUABLE",
        ) or matrix_row["truth_status"] not in ("DEFINED", "UNDEFINED", "NOT_MATERIALIZED"):
            raise PackageVerificationError(f"MatrixCapture row {index} class/status is invalid")
        if not isinstance(pair_row, dict) or not isinstance(pair_row.get("key"), list):
            raise PackageVerificationError(f"pair ledger row {index} key is not an ordered identity list")
        expected_pair_key = [*identity, "MONTE_CARLO"]
        if pair_row["key"] != expected_pair_key:
            raise PackageVerificationError(f"pair ledger row {index} key/order differs from MatrixCapture")
        pair_identity = tuple(pair_row["key"])
        if pair_identity in seen_pair_keys:
            raise PackageVerificationError("pair ledger contains a duplicate scenario/estimand identity")
        seen_pair_keys.add(pair_identity)
        if (pair_row.get("evaluation_class"), pair_row.get("truth_status")) != (
            matrix_row["evaluation_class"], matrix_row["truth_status"],
        ):
            raise PackageVerificationError(f"pair ledger row {index} evaluation/truth classification differs from MatrixCapture")


def _historical_fingerprint(manifest_payload: Any) -> str:
    # Gate 181's historical source-domain two-stage Python JSON algorithm.
    normalized = json.loads(json.dumps(manifest_payload, sort_keys=True))
    body = json.dumps(normalized, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return _sha256(body)


def _check_report(report_envelope: Any) -> None:
    if not isinstance(report_envelope, dict) or set(report_envelope) != {
        "schema_id", "schema_version", "payload_type", "legacy_report_fingerprint",
        "legacy_fingerprint_algorithm", "report",
    }:
        raise PackageVerificationError("FrozenReportSnapshot envelope field allowlist mismatch")
    if (report_envelope["schema_id"], report_envelope["schema_version"],
            report_envelope["payload_type"]) != (
        REPORT_SCHEMA_ID, REPORT_SCHEMA_VERSION, REPORT_PAYLOAD_TYPE
    ):
        raise PackageVerificationError("package v2 requires FrozenReportSnapshot v2.1.0")
    if report_envelope["legacy_fingerprint_algorithm"] != (
        "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1"
    ):
        raise PackageVerificationError("unknown historical report fingerprint algorithm")
    report = report_envelope["report"]
    if not isinstance(report, dict) or not isinstance(report.get("manifest"), dict):
        raise PackageVerificationError("report payload/legacy manifest is missing")
    if _historical_fingerprint(report["manifest"]) != report_envelope["legacy_report_fingerprint"]:
        raise PackageVerificationError("historical Evaluator report fingerprint mismatch")
    manifest = report["manifest"]
    if report.get("report_fingerprint") != report_envelope["legacy_report_fingerprint"]:
        raise PackageVerificationError("report root fingerprint differs from the frozen envelope")
    if report.get("temporal_manifest") != manifest.get("temporal_manifest"):
        raise PackageVerificationError("root/nested temporal manifest copies diverge")
    if report.get("pair_ledger") != manifest.get("pair_ledger"):
        raise PackageVerificationError("root/nested pair-ledger copies diverge")
    coverage = report.get("coverage")
    if coverage != {"required_pairs": 52, "observed_pairs": 52, "scenario_count": 13}:
        raise PackageVerificationError("report coverage is not exactly 52 pairs / 13 scenarios")
    n_units, outer_replicates, repeated_assignments = (
        manifest.get("N"), manifest.get("M"), manifest.get("R")
    )
    for label, value, minimum in (
        ("N", n_units, 1), ("M", outer_replicates, 2), ("R", repeated_assignments, 1)
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
            raise PackageVerificationError(f"report manifest {label} is outside its declared integer domain")
    scenarios = report.get("scenario_reports")
    scenario_versions = manifest.get("scenario_versions")
    if (not isinstance(scenarios, dict) or len(scenarios) != 13
            or not isinstance(scenario_versions, list) or len(scenario_versions) != 13):
        raise PackageVerificationError("report must retain exactly 13 declared scenario reports")
    declared_ids = []
    for pair in scenario_versions:
        if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(x, str) and x for x in pair):
            raise PackageVerificationError("report scenario_versions manifest is malformed")
        declared_ids.append(pair[0])
    if (tuple(declared_ids) != AUTHORITATIVE_SCENARIO_IDS
            or set(scenarios) != set(declared_ids)):
        raise PackageVerificationError("report scenario reports differ from frozen authoritative scenario registry")
    temporal = report.get("temporal_manifest")
    pairs = report.get("pair_ledger")
    expected_temporal_count = 13 * outer_replicates * (1 + repeated_assignments)
    if not isinstance(temporal, list) or len(temporal) != expected_temporal_count:
        raise PackageVerificationError("report temporal manifest cardinality differs from 13 x M x (1+R)")
    if not isinstance(pairs, list) or len(pairs) != 52:
        raise PackageVerificationError("report pair ledger must contain exactly 52 ordered pairs")
    for row in temporal:
        if not isinstance(row, dict):
            raise PackageVerificationError("report temporal row is not an object")
        for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
            if type(row.get(field)) is not int or not 0 <= row[field] <= UINT64_MAX:
                raise PackageVerificationError(f"report temporal {field} is not a decoded uint64")
    for pair in pairs:
        contributions = pair.get("contributions") if isinstance(pair, dict) else None
        if not isinstance(contributions, list) or len(contributions) != outer_replicates:
            raise PackageVerificationError("pair ledger contribution cardinality differs from M")
        for contribution in contributions:
            if type(contribution.get("world_seed")) is not int or not 0 <= contribution["world_seed"] <= UINT64_MAX:
                raise PackageVerificationError("pair contribution world_seed is not a decoded uint64")
    for scenario_id, scenario in scenarios.items():
        if (not isinstance(scenario, dict)
                or scenario.get("scenario_id") != scenario_id
                or not isinstance(scenario.get("per_outer_replicate"), list)
                or len(scenario["per_outer_replicate"]) != outer_replicates):
            raise PackageVerificationError(f"scenario report {scenario_id} identity/cardinality mismatch")
        for index, row in enumerate(scenario["per_outer_replicate"]):
            if not isinstance(row, dict) or row.get("outer_replicate_id") != f"outer-{index:06d}":
                raise PackageVerificationError(f"scenario report {scenario_id} has noncanonical M ordering")
            run = row.get("run")
            if not isinstance(run, list) or len(run) != 4 or not all(isinstance(item, dict) for item in run):
                raise PackageVerificationError(f"scenario report {scenario_id} RUN tuple must contain four ordered objects")
            if type(run[0].get("seed")) is not int or not 0 <= run[0]["seed"] <= UINT64_MAX:
                raise PackageVerificationError("scenario report TruthBundle.seed is not a decoded uint64")
            for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
                if type(run[3].get(field)) is not int or not 0 <= run[3][field] <= UINT64_MAX:
                    raise PackageVerificationError(f"scenario report RunManifest.{field} is not a decoded uint64")


def _independent_tar_rebuild(files: Mapping[str, bytes]) -> bytes:
    """Rebuild the normative USTAR byte stream without calling the writer."""
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w", format=tarfile.USTAR_FORMAT) as archive:
        for path in sorted(files):
            info = tarfile.TarInfo(path)
            info.size = len(files[path])
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mode = 0o644
            info.type = tarfile.REGTYPE
            info.pax_headers = {}
            archive.addfile(info, io.BytesIO(files[path]))
    return buffer.getvalue()



def _configuration_digest(value: Any) -> str:
    try:
        return _sha256(rfc8785.dumps(value))
    except Exception as exc:
        raise PackageVerificationError(f"configuration digest input is not JCS serializable: {exc}") from exc


def _analysis_contract_payload_digest(
    scenario_id: str, scenario_version: str, n_units: int,
    analyzer_version: str, contract_payload: Mapping[str, Any],
) -> str:
    return _configuration_digest({
        "schema_id": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
        "schema_version": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
        "scenario_id": scenario_id,
        "scenario_version": scenario_version,
        "n_units": n_units,
        "analyzer_version": analyzer_version,
        "analysis_contract": dict(contract_payload),
    })


def _validate_analysis_contract_types(payload: Any, label: str) -> dict[str, Any]:
    expected = _SNAPSHOT_TYPE_FIELDS["vcont_integrated_harness.AnalysisContract"]
    if not isinstance(payload, dict) or set(payload) != set(expected):
        raise PackageVerificationError(f"{label}: AnalysisContract exact 37-field allowlist mismatch")
    for name, value in payload.items():
        if name in ANALYSIS_CONTRACT_BOOL_FIELDS:
            if type(value) is not bool:
                raise PackageVerificationError(f"{label}.{name}: expected exact boolean")
        elif name in ANALYSIS_CONTRACT_NULLABLE_FIELDS:
            if value is not None and not isinstance(value, str):
                raise PackageVerificationError(f"{label}.{name}: expected nullable string")
        elif not isinstance(value, str):
            raise PackageVerificationError(f"{label}.{name}: expected non-null string")
    return payload


def _reconcile_configuration_companions(
    files: Mapping[str, Any], decoded_report: Any, matrix: Mapping[str, Any],
) -> tuple[int, int, int]:
    """Independently reconstruct 13 contracts, 26 applicability rows and 28 digests."""
    run_file = files.get("runs/run_records.json")
    contract_file = files.get("design/analysis_contracts.json")
    fingerprint_file = files.get("provenance/configuration_fingerprints.json")
    effective_file = files.get("design/effective_scenario_configs.json")
    assignment_file = files.get("seeds/evaluation_seed_assignments.json")
    benchmark_design = files.get("design/benchmark_design.json")
    report = decoded_report.get("report") if isinstance(decoded_report, dict) else None
    report_design = report.get("design") if isinstance(report, dict) else None
    if not all(isinstance(item, dict) for item in (
        run_file, contract_file, fingerprint_file, effective_file,
        assignment_file, benchmark_design, report_design
    )):
        raise PackageVerificationError("configuration companion source objects are missing or malformed")
    export_id = run_file.get("benchmark_export_id")
    for label, value, schema_id in (
        ("analysis_contracts", contract_file, ANALYSIS_CONTRACTS_SCHEMA_ID),
        ("configuration_fingerprints", fingerprint_file, CONFIGURATION_FINGERPRINTS_SCHEMA_ID),
    ):
        if set(value) != ({"schema_id", "schema_version", "benchmark_export_id", "source_contracts", "applicability"}
                          if label == "analysis_contracts" else
                          {"schema_id", "schema_version", "benchmark_export_id", "components", "aggregate"}):
            raise PackageVerificationError(f"{label}: exact root field allowlist mismatch")
        expected_version = (ANALYSIS_CONTRACTS_SCHEMA_VERSION if label == "analysis_contracts"
                            else CONFIGURATION_FINGERPRINTS_SCHEMA_VERSION)
        if (value.get("schema_id"), value.get("schema_version"), value.get("benchmark_export_id")) != (
            schema_id, expected_version, export_id
        ):
            raise PackageVerificationError(f"{label}: schema/version/benchmark_export_id mismatch")
    if not isinstance(export_id, str) or not re.fullmatch(r"[0-9a-f]{64}", export_id):
        raise PackageVerificationError("configuration companions are not bound to a valid capture identity")

    scenario_versions = report_design.get("scenario_versions")
    n_units, M, R = report_design.get("n_units"), report_design.get("outer_replicates"), report_design.get("repeated_assignments")
    if (not isinstance(scenario_versions, list) or len(scenario_versions) != 13
            or tuple(row[0] for row in scenario_versions if isinstance(row, list) and len(row) == 2)
            != AUTHORITATIVE_SCENARIO_IDS
            or any(not isinstance(row, list) or len(row) != 2 for row in scenario_versions)
            or any(not isinstance(row[1], str) or not row[1] for row in scenario_versions)
            or isinstance(n_units, bool) or not isinstance(n_units, int)
            or isinstance(M, bool) or not isinstance(M, int) or M < 1
            or isinstance(R, bool) or not isinstance(R, int) or R < 1):
        raise PackageVerificationError("configuration companion design dimensions/scenario order are invalid")
    versions = {row[0]: row[1] for row in scenario_versions}
    expected_contract_keys = [(sid, versions[sid], n_units) for sid in AUTHORITATIVE_SCENARIO_IDS]

    source_rows = contract_file["source_contracts"]
    applicability = contract_file["applicability"]
    if not isinstance(source_rows, list) or len(source_rows) != 13:
        raise PackageVerificationError("analysis_contracts must contain exactly 13 source rows")
    if not isinstance(applicability, list) or len(applicability) != 26:
        raise PackageVerificationError("analysis_contracts must contain exactly 26 applicability rows")
    expected_source_fields = {
        "scenario_id", "scenario_version", "n_units", "analyzer_version",
        "analysis_contract", "contract_payload_digest",
    }
    source_map = {}
    for index, row in enumerate(source_rows):
        if not isinstance(row, dict) or set(row) != expected_source_fields:
            raise PackageVerificationError(f"analysis_contracts source row {index} field allowlist mismatch")
        key = (row["scenario_id"], row["scenario_version"], row["n_units"])
        if key != expected_contract_keys[index] or key in source_map:
            raise PackageVerificationError("analysis_contracts source rows are duplicate or not in canonical scenario order")
        if row["analyzer_version"] != ANALYZER_VERSION:
            raise PackageVerificationError("AnalysisContract Analyzer.version differs from frozen source version")
        contract = _validate_analysis_contract_types(row["analysis_contract"], f"analysis_contracts.source_contracts[{index}]")
        digest = _analysis_contract_payload_digest(*key, row["analyzer_version"], contract)
        if row["contract_payload_digest"] != digest:
            raise PackageVerificationError("AnalysisContract semantic JCS digest does not recompute")
        if not isinstance(row["contract_payload_digest"], str) or not re.fullmatch(r"[0-9a-f]{64}", row["contract_payload_digest"]):
            raise PackageVerificationError("AnalysisContract semantic digest is not lowercase SHA-256 hex")
        source_map[key] = row

    expected_applicability = []
    for sid, version, count in expected_contract_keys:
        digest = source_map[(sid, version, count)]["contract_payload_digest"]
        for family in ("RUN", "REPEATED_ASSIGNMENT"):
            expected_applicability.append({
                "scenario_id": sid, "scenario_version": version, "n_units": count,
                "run_family": family, "contract_payload_digest": digest,
            })
    expected_app_fields = {"scenario_id", "scenario_version", "n_units", "run_family", "contract_payload_digest"}
    if any(not isinstance(row, dict) or set(row) != expected_app_fields for row in applicability):
        raise PackageVerificationError("analysis_contracts applicability row field allowlist mismatch")
    if applicability != expected_applicability:
        raise PackageVerificationError("analysis_contracts applicability is incomplete, duplicated, reordered or cross-linked")

    run_records = run_file.get("run_evidence_records")
    expected_run_count = 13 * M * (1 + R)
    if not isinstance(run_records, list) or len(run_records) != expected_run_count:
        raise PackageVerificationError("AnalysisContract source reconciliation RUN/R cardinality mismatch")
    representative_refs = {}
    consumed_contracts = {key: 0 for key in expected_contract_keys}
    for run_index, record in enumerate(run_records):
        if not isinstance(record, dict) or not isinstance(record.get("snapshot_refs"), dict):
            raise PackageVerificationError("RUN/R record lacks AnalysisContract snapshot reference")
        key = _logical_run_key(record.get("key"), f"AnalysisContract RUN/R record {run_index}")
        scope = (key[0], key[1], key[2])
        if scope not in source_map:
            raise PackageVerificationError("RUN/R AnalysisContract snapshot references unknown scenario contract")
        contract_ref = record["snapshot_refs"].get("analysis_contract")
        decoded = decode_frozen_snapshot_ref(
            contract_ref, expected_type_id="vcont_integrated_harness.AnalysisContract"
        )
        contract_fields = _snapshot_fields(decoded, "vcont_integrated_harness.AnalysisContract")
        contract_fields = _validate_analysis_contract_types(contract_fields, f"RUN/R snapshot {run_index}")
        source = source_map[scope]
        if contract_fields != source["analysis_contract"]:
            raise PackageVerificationError("RUN/R historical AnalysisContract snapshot differs from scenario source contract")
        if record.get("analysis_contract_sha256") != decoded.sha256:
            raise PackageVerificationError("RUN/R AnalysisContract legacy digest differs from exact snapshot bytes")
        expected_role = "RUN" if key[4] == "RUN" else "REPEATED_ASSIGNMENT"
        applicability_key = (scope[0], scope[1], scope[2], expected_role)
        if not any((row["scenario_id"], row["scenario_version"], row["n_units"], row["run_family"])
                   == applicability_key and row["contract_payload_digest"] == source["contract_payload_digest"]
                   for row in applicability):
            raise PackageVerificationError("RUN/R snapshot has no unique matching applicability relation")
        consumed_contracts[scope] += 1
        if key[3] == "outer-000000" and key[4] == "RUN":
            representative_refs[scope] = run_index
    if any(count != M * (1 + R) for count in consumed_contracts.values()):
        raise PackageVerificationError("each scenario contract was not consumed by every RUN/R snapshot exactly once")
    if len(representative_refs) != 13:
        raise PackageVerificationError("representative RUN AnalysisContract source references are incomplete")

    effective_rows = effective_file.get("rows")
    if (effective_file.get("schema_id"), effective_file.get("schema_version")) != (
        EFFECTIVE_CONFIG_SCHEMA_ID, EFFECTIVE_CONFIG_SCHEMA_VERSION
    ) or not isinstance(effective_rows, list) or len(effective_rows) != 13:
        raise PackageVerificationError("effective ScenarioConfig source schema/cardinality mismatch")
    components = []
    expected_component_fields = {
        "component_id", "component_type", "scope_key", "source_ref",
        "payload_schema_id", "payload_schema_version", "algorithm_id", "digest_sha256",
    }
    for index, row in enumerate(effective_rows):
        if not isinstance(row, dict):
            raise PackageVerificationError("effective ScenarioConfig row is not an object")
        sid, version, count = row.get("scenario_id"), row.get("scenario_version"), row.get("n_units")
        if (sid, version, count) != expected_contract_keys[index]:
            raise PackageVerificationError("DGP fingerprint source row scope/order differs from authoritative design")
        components.append({
            "component_id": f"dgp-generator:{sid}:{version}:{count}",
            "component_type": "DGP_GENERATOR_CONFIG",
            "scope_key": [sid, version, count],
            "source_ref": f"design/effective_scenario_configs.json#/rows/{index}",
            "payload_schema_id": EFFECTIVE_CONFIG_SCHEMA_ID,
            "payload_schema_version": EFFECTIVE_CONFIG_SCHEMA_VERSION,
            "algorithm_id": DGP_CONFIG_DIGEST_ALGORITHM,
            "digest_sha256": _configuration_digest(row),
        })
    for index, key in enumerate(expected_contract_keys):
        source = source_map[key]
        run_index = representative_refs[key]
        components.append({
            "component_id": f"analyzer-contract:{key[0]}:{key[1]}:{key[2]}",
            "component_type": "ANALYZER_EFFECTIVE_CONTRACT",
            "scope_key": [key[0], key[1], key[2]],
            "source_ref": f"runs/run_records.json#/run_evidence_records/{run_index}/snapshot_refs/analysis_contract",
            "payload_schema_id": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
            "payload_schema_version": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
            "algorithm_id": ANALYSIS_CONTRACT_DIGEST_ALGORITHM,
            "digest_sha256": source["contract_payload_digest"],
        })
    if matrix.get("schema_id") != MATRIX_SCHEMA_ID or matrix.get("schema_version") != MATRIX_SCHEMA_VERSION:
        raise PackageVerificationError("MatrixCapture source schema/version mismatch")
    matrix_digest = _configuration_digest({
        "schema_id": MATRIX_SCHEMA_ID, "schema_version": MATRIX_SCHEMA_VERSION,
        "row_count": 52, "rows": matrix.get("rows"),
    })
    if matrix_digest != matrix.get("full_matrix_sha256"):
        raise PackageVerificationError("MatrixCapture component digest does not recompute")
    components.append({
        "component_id": "scenario-estimand-matrix",
        "component_type": "SCENARIO_ESTIMAND_MATRIX",
        "scope_key": export_id,
        "source_ref": "design/scenario_estimand_matrix.json#",
        "payload_schema_id": MATRIX_SCHEMA_ID,
        "payload_schema_version": MATRIX_SCHEMA_VERSION,
        "algorithm_id": "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1",
        "digest_sha256": matrix_digest,
    })
    assignment_rows = assignment_file.get("rows")
    if (assignment_file.get("schema_id"), assignment_file.get("schema_version"), assignment_file.get("bank")) != (
        "TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS", "2.0.0", "evaluation"
    ) or not isinstance(assignment_rows, list) or assignment_file.get("row_count") != len(assignment_rows):
        raise PackageVerificationError("evaluation assignment source schema/order envelope mismatch")
    assignment_digest = _configuration_digest({"rows": assignment_rows})
    components.append({
        "component_id": "evaluation-seed-bank",
        "component_type": "EVALUATION_SEED_BANK",
        "scope_key": export_id,
        "source_ref": "seeds/evaluation_seed_assignments.json#/rows",
        "payload_schema_id": assignment_file["schema_id"],
        "payload_schema_version": assignment_file["schema_version"],
        "algorithm_id": EVALUATION_ASSIGNMENT_DIGEST_ALGORITHM,
        "digest_sha256": assignment_digest,
    })

    component_rows = fingerprint_file.get("components")
    if not isinstance(component_rows, list) or len(component_rows) != 28:
        raise PackageVerificationError("configuration_fingerprints must contain exactly 28 components")
    if any(not isinstance(row, dict) or set(row) != expected_component_fields for row in component_rows):
        raise PackageVerificationError("configuration_fingerprints component row field allowlist mismatch")
    if component_rows != components:
        raise PackageVerificationError("configuration fingerprint component rows differ from independently recomputed sources")

    aggregate_input = {
        "schema_id": AGGREGATE_FINGERPRINT_SCHEMA_ID,
        "schema_version": AGGREGATE_FINGERPRINT_SCHEMA_VERSION,
        "components": [{
            name: component[name] for name in (
                "component_id", "component_type", "scope_key", "payload_schema_id",
                "payload_schema_version", "algorithm_id", "digest_sha256"
            )
        } for component in components],
    }
    aggregate_digest = _configuration_digest(aggregate_input)
    aggregate = fingerprint_file.get("aggregate")
    if not isinstance(aggregate, dict) or set(aggregate) != {
        "algorithm_id", "digest_sha256", "source_design_declaration"
    }:
        raise PackageVerificationError("configuration_fingerprints aggregate exact field allowlist mismatch")
    if (aggregate.get("algorithm_id"), aggregate.get("digest_sha256"),
        aggregate.get("source_design_declaration")) != (
        AGGREGATE_FINGERPRINT_ALGORITHM, aggregate_digest, SOURCE_DESIGN_DECLARATION
    ):
        raise PackageVerificationError("aggregate design fingerprint declaration does not recompute")
    if benchmark_design.get("configuration_fingerprint") != aggregate_digest:
        raise PackageVerificationError("aggregate fingerprint differs from source design declaration")
    if report_design.get("configuration_fingerprint") not in (None, aggregate_digest):
        raise PackageVerificationError("aggregate fingerprint differs from FrozenReportSnapshot design declaration")
    return 13, 26, 28

def verify_package_v2(
    archive_bytes: bytes,
    *,
    expected_profile: str | None = None,
    trust_policy: Any = None,
) -> PackageVerificationResult:
    """Verify package integrity and schema independently of the package writer.

    Unimplemented semantic/provenance/authentication layers are returned as
    NOT_VERIFIED/NOT_AUTHENTICATED, never promoted from package-declared flags.
    """
    if not isinstance(archive_bytes, bytes) or not archive_bytes:
        raise PackageVerificationError("archive_bytes must be nonempty immutable bytes")
    if expected_profile not in (None, "CONFIRMATORY"):
        raise PackageVerificationError("unsupported expected package profile")
    extracted: dict[str, bytes] = {}
    seen_folded: set[str] = set()
    try:
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            members = archive.getmembers()
            if len(members) != 14:
                raise PackageVerificationError("archive must contain exactly 14 members")
            if [member.name for member in members] != sorted(PACKAGE_PATHS):
                raise PackageVerificationError("archive members are not in canonical lexical path order")
            for member in members:
                _safe_archive_path(member.name)
                if member.name in extracted or member.name.casefold() in seen_folded:
                    raise PackageVerificationError("duplicate or case-colliding archive member")
                seen_folded.add(member.name.casefold())
                if (not member.isfile() or member.type != tarfile.REGTYPE
                        or member.mode != 0o644 or member.uid != 0 or member.gid != 0
                        or member.uname != "" or member.gname != "" or member.mtime != 0
                        or member.pax_headers):
                    raise PackageVerificationError(f"{member.name}: noncanonical TAR member metadata/type")
                stream = archive.extractfile(member)
                if stream is None:
                    raise PackageVerificationError(f"{member.name}: archive member payload unavailable")
                data = stream.read()
                if len(data) != member.size:
                    raise PackageVerificationError(f"{member.name}: TAR size does not match extracted bytes")
                extracted[member.name] = data
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"invalid TAR archive: {exc}") from exc

    if set(extracted) != set(PACKAGE_PATHS):
        missing = sorted(set(PACKAGE_PATHS) - set(extracted))
        extra = sorted(set(extracted) - set(PACKAGE_PATHS))
        raise PackageVerificationError(f"archive inventory mismatch; missing={missing}; extra={extra}")

    if _independent_tar_rebuild(extracted) != archive_bytes:
        raise PackageVerificationError("archive bytes differ from independently rebuilt canonical USTAR stream")

    parsed: dict[str, Any] = {}
    canonical_bytes: dict[str, bytes] = {}
    for path in PACKAGE_PATHS:
        parsed[path], canonical_bytes[path] = _strict_json(extracted[path], path)

    manifest = parsed["manifest.json"]
    required_manifest_fields = {
        "schema_id", "schema_version", "profile", "canonicalization", "archive_profile",
        "report_schema", "legacy_report_fingerprint", "package_id_derivation", "files",
    }
    if not isinstance(manifest, dict) or set(manifest) != required_manifest_fields:
        raise PackageVerificationError("package manifest field allowlist mismatch")
    if (manifest["schema_id"], manifest["schema_version"]) != (PACKAGE_SCHEMA_ID, PACKAGE_SCHEMA_VERSION):
        raise PackageVerificationError("package schema ID/version mismatch")
    if manifest["profile"] != "CONFIRMATORY" or (expected_profile and manifest["profile"] != expected_profile):
        raise PackageVerificationError("package profile mismatch")
    if (manifest["canonicalization"], manifest["archive_profile"]) != (
        "RFC8785-JCS-UTF8-TRAILING-LF", "POSIX-USTAR-UNCOMPRESSED-NORMALIZED-METADATA"
    ):
        raise PackageVerificationError("package canonicalization/archive profile mismatch")
    if manifest["report_schema"] != {
        "schema_id": REPORT_SCHEMA_ID,
        "schema_version": REPORT_SCHEMA_VERSION,
        "payload_type": REPORT_PAYLOAD_TYPE,
    }:
        raise PackageVerificationError("package manifest does not declare the exact report v2.1.0 dependency")
    if manifest["package_id_derivation"] != "SHA256(JCS({schema_id,schema_version,manifest_sha256}))":
        raise PackageVerificationError("package ID derivation declaration mismatch")
    expected_file_records = []
    for path in DATA_PATHS:
        payload = extracted[path]
        expected_file_records.append({
            "path": path,
            "byte_length": len(payload),
            "sha256": _sha256(payload),
        })
    expected_file_records.sort(key=lambda row: row["path"])
    if manifest["files"] != expected_file_records:
        raise PackageVerificationError("manifest file inventory/length/digest records do not recompute")

    if trust_policy is not None:
        raise PackageVerificationError("external trust_policy verification is not implemented in this verifier version")
    if manifest["legacy_report_fingerprint"] != parsed["report/report.json"].get("legacy_report_fingerprint"):
        raise PackageVerificationError("manifest legacy report fingerprint differs from report snapshot")
    report = parsed["report/report.json"]
    _check_registered_uint64(parsed)
    decoded_report = _decode_registered(report)
    _check_report(decoded_report)
    try:
        reconciled_run_count, reconciled_outer_count = _reconcile_run_records(parsed, decoded_report)
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"RUN/R semantic reconciliation failed closed: {exc}") from exc
    try:
        _reconcile_benchmark_export_identity(parsed)
        _reconcile_effective_scenario_configs(parsed, decoded_report)
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"companion identity/config reconciliation failed closed: {exc}") from exc
    matrix = parsed["design/scenario_estimand_matrix.json"]
    if (not isinstance(matrix, dict) or set(matrix) != {
            "schema_id", "schema_version", "design_identity", "row_count", "rows",
            "legacy_matrix_fingerprint", "full_matrix_digest_algorithm", "full_matrix_sha256",
        } or matrix.get("schema_id") != MATRIX_SCHEMA_ID
            or matrix.get("schema_version") != MATRIX_SCHEMA_VERSION
            or matrix.get("row_count") != 52 or not isinstance(matrix.get("rows"), list)
            or len(matrix["rows"]) != 52
            or matrix.get("full_matrix_digest_algorithm") != "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1"):
        raise PackageVerificationError("MatrixCapture schema/cardinality/digest-algorithm mismatch")
    matrix_digest = _sha256(rfc8785.dumps({
        "schema_id": MATRIX_SCHEMA_ID,
        "schema_version": MATRIX_SCHEMA_VERSION,
        "row_count": 52,
        "rows": matrix["rows"],
    }))
    if matrix_digest != matrix.get("full_matrix_sha256"):
        raise PackageVerificationError("MatrixCapture full-matrix digest mismatch")
    report_design = decoded_report["report"]["design"]
    expected_matrix_identity = {
        "scenario_versions": [
            {"scenario_id": sid, "scenario_version": version}
            for sid, version in report_design["scenario_versions"]
        ],
        "N": report_design["n_units"],
        "M": report_design["outer_replicates"],
        "R": report_design["repeated_assignments"],
        "legacy_matrix_fingerprint": report_design["matrix_fingerprint"],
    }
    if matrix.get("design_identity") != expected_matrix_identity:
        raise PackageVerificationError("MatrixCapture design identity differs from FrozenReportSnapshot design")
    _reconcile_matrix_pair_ledger(matrix, decoded_report)
    try:
        _reconcile_configuration_companions(parsed, decoded_report, matrix)
    except PackageVerificationError:
        raise
    except Exception as exc:
        raise PackageVerificationError(f"configuration companion reconciliation failed closed: {exc}") from exc

    if (decoded_report["report"]["temporal_manifest"]
            != decoded_report["report"]["manifest"]["temporal_manifest"]
            or decoded_report["report"]["pair_ledger"]
            != decoded_report["report"]["manifest"]["pair_ledger"]):
        raise PackageVerificationError("decoded report duplicate views diverge")

    manifest_bytes = extracted["manifest.json"]
    manifest_sha = _sha256(manifest_bytes)
    package_id = _sha256(rfc8785.dumps({
        "schema_id": PACKAGE_SCHEMA_ID,
        "schema_version": PACKAGE_SCHEMA_VERSION,
        "manifest_sha256": manifest_sha,
    }))
    archive_sha = _sha256(archive_bytes)

    # trust_policy is intentionally not used to infer authentication. A
    # governed attestation verifier and trusted signer configuration are absent.
    limitations = (
        "RUN/R snapshots, assignments, temporal rows, outer-world records, report tuples, pair contributions, AnalysisContract applicability, 13/26 companion rows and all 28 configuration fingerprints were reconciled independently.",
        "Calibration/evaluation seed disjointness and Gate159 derived-status recomputation are not implemented.",
        "Source-execution metadata has not been independently resolved against GitHub.",
        "Technical-test evidence has not been independently bound to a trusted workflow run/artifact.",
        "External attestation/signature verification is not implemented; package is NOT_AUTHENTICATED.",
    )
    return PackageVerificationResult(
        PACKAGE_SCHEMA_ID, PACKAGE_SCHEMA_VERSION, manifest["profile"],
        archive_sha, manifest_sha, package_id, len(extracted),
        "PASS", "PARTIAL", "STRUCTURAL_ONLY", "RECONCILED",
        "RECONCILED", "NOT_VERIFIED", "NOT_VERIFIED", "NOT_AUTHENTICATED", limitations,
    )
