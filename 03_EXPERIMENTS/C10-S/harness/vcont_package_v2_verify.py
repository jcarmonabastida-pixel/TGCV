"""Independent structural verifier for TGCV C10-S V_cont package v2.

This module deliberately does not import or call vcont_package_v2. It verifies
archive integrity, JCS, the frozen inventory, report/matrix schemas and all
registered uint64 wire occurrences. Semantic RUN/R snapshot joins, full Gate159
derivation, source-execution reconciliation, technical-test provenance and
external authentication remain explicitly separate status layers.
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


def _snapshot_legacy_sealed_digest(sealed: dict[str, Any]) -> str:
    if set(sealed) != {"run_id", "rows", "manifest", "sha256"}:
        raise PackageVerificationError("SealedEvidence decoded fields are incomplete")
    payload = json.dumps(
        {"manifest": sealed["manifest"], "rows": sealed["rows"]},
        sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return _sha256(payload)


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
    scenario_order = [row[0] for row in scenario_versions
                      if isinstance(row, list) and len(row) == 2]
    versions = {row[0]: row[1] for row in scenario_versions
                if isinstance(row, list) and len(row) == 2}
    if len(scenario_order) != 13 or len(set(scenario_order)) != 13:
        raise PackageVerificationError("report design scenario registry is not unique")
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
    if run_file["benchmark_export_id"] != files["manifest.json"].get("benchmark_export_id", run_file["benchmark_export_id"]):
        # The package manifest has no export ID in v2; this branch only guards malformed explicit values.
        raise PackageVerificationError("RUN export identity is inconsistent with package context")

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
        assignment_seeds = (assignment["world_seed"], assignment["z_assignment_seed"],
                            assignment["g_assignment_seed"])
        config_seeds = (config["world_seed"], config["z_assignment_seed"], config["g_assignment_seed"])
        manifest_seeds = (manifest["world_seed"], manifest["z_assignment_seed"], manifest["g_assignment_seed"])
        if any(value is None for value in config_seeds) or assignment_seeds != config_seeds or assignment_seeds != manifest_seeds:
            raise PackageVerificationError("SeedAssignment/ScenarioConfig/RunManifest stream equality failed")
        if len(set(assignment_seeds)) != 3:
            raise PackageVerificationError("world/Z/G seed streams are not distinct within assignment")
        if (truth["run_id"], truth["outer_replicate_id"], truth["assignment_role"],
            truth["assignment_index"], truth["seed"]) != (
            key[6], key[3], key[4], key[5], config["seed"]
        ):
            raise PackageVerificationError("MatrixTruthProjection identity/seed differs from ScenarioConfig")
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
        if record["scenario_config_structural_sha256"] != refs["scenario_config"]["sha256"] and not re.fullmatch(
            r"[0-9a-f]{64}", str(record["scenario_config_structural_sha256"])
        ):
            raise PackageVerificationError("ScenarioConfig structural digest declaration is malformed")
        sealed_digest = _snapshot_legacy_sealed_digest(sealed)
        if sealed_digest != sealed["sha256"] or analyzer["input_sha256"] != sealed_digest:
            raise PackageVerificationError("SealedEvidence legacy digest differs from AnalyzerResult.input_sha256")
        if candidate["rows"] != sealed["rows"] or candidate["provenance"] != sealed["manifest"].get("provenance"):
            raise PackageVerificationError("EvidenceCandidate and SealedEvidence rows/provenance diverge")
        if sealed["manifest"].get("row_count") != len(sealed["rows"]):
            raise PackageVerificationError("SealedEvidence row_count differs from retained rows")
        provenance = sealed["manifest"].get("provenance", {})
        provenance_digest = _sha256(json.dumps(
            provenance, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8"))
        if sealed["manifest"].get("provenance_sha256") != provenance_digest:
            raise PackageVerificationError("SealedEvidence provenance digest does not recompute")
        if key[4] == "RUN" and key[5] != -1:
            raise PackageVerificationError("designated RUN must use assignment_index -1")
        if key[4] == "REPEATED_ASSIGNMENT" and key[5] < 0:
            raise PackageVerificationError("repeated assignment index must be nonnegative")
        if key in run_map:
            raise PackageVerificationError("duplicate run key")
        run_map[key] = record
        decoded_by_key[key] = decoded

    if len(run_map) != expected_runs or set(run_map) != {
        (sid, versions[sid], n_units, f"outer-{m:06d}", role, idx, None)
        for sid in [] for m in []
        for role, idx in []
    }:
        # The exact run_id universe is derived from the independently decoded RunManifest set below.
        if len(run_map) != expected_runs:
            raise PackageVerificationError("run record cardinality mismatch")
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
        world_seed = _uint64(key["world_seed"], f"outer_world_evidence_records[{index}].key.world_seed")
        outer_key = (key["scenario_id"], key["scenario_version"], key["N"],
                     key["outer_replicate_id"], key["world_id"])
        if outer_key in outer_map:
            raise PackageVerificationError("duplicate outer-world logical key")
        if outer["bank"] != "evaluation":
            raise PackageVerificationError("outer-world record bank must be evaluation")
        base = (key["scenario_id"], key["scenario_version"], key["N"], key["outer_replicate_id"])
        run_key_obj = outer["run_record_key"]
        run_key = _logical_run_key(run_key_obj, "outer_world.run_record_key")
        if run_key[:6] != (*base, "RUN", -1):
            raise PackageVerificationError("outer-world RUN reference does not identify its designated RUN")
        run_record = run_map.get(run_key)
        if run_record is None:
            raise PackageVerificationError("outer-world RUN reference is orphaned")
        run_decoded = decoded_by_key[run_key]
        run_manifest = run_decoded["run_manifest"]
        if (run_manifest["world_id"], run_manifest["world_version"], run_manifest["world_seed"]) != (
            key["world_id"], key["world_version"], world_seed
        ):
            raise PackageVerificationError("outer-world key differs from designated RUN RunManifest")
        repeated_keys = outer["repeated_run_record_keys"]
        if not isinstance(repeated_keys, list) or len(repeated_keys) != R:
            raise PackageVerificationError("outer-world repeated RUN references differ from R")
        expected_repeated = []
        for repeat_index, ref_key in enumerate(repeated_keys):
            parsed_key = _logical_run_key(ref_key, f"outer_world.repeated_run_record_keys[{repeat_index}]")
            if parsed_key[:6] != (*base, "REPEATED_ASSIGNMENT", repeat_index):
                raise PackageVerificationError("outer-world repeated reference index/order mismatch")
            if parsed_key not in run_map:
                raise PackageVerificationError("outer-world repeated RUN reference is orphaned")
            repeated_manifest = decoded_by_key[parsed_key]["run_manifest"]
            if (repeated_manifest["world_id"], repeated_manifest["world_version"],
                repeated_manifest["world_seed"]) != (key["world_id"], key["world_version"], world_seed):
                raise PackageVerificationError("repeated assignment is crossed into another world")
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
            _snapshot_source_value(decoded_by_key[parsed_key]["evaluation_report"])
            for parsed_key in expected_repeated
        )
        if (repeated_report["world_id"] != key["world_id"]
                or repeated_report["replicate_count"] != R
                or tuple(repeated_report["per_run_reports"]) != repeated_evaluations):
            raise PackageVerificationError("RepeatedAssignmentReport does not match exact ordered R evaluation reports")
        outer_map[outer_key] = {
            "run_key": run_key, "repeated_keys": tuple(expected_repeated),
            "world_seed": world_seed, "repeated_report": repeated_report,
        }
    expected_outer_keys = {
        (sid, versions[sid], n_units, f"outer-{m:06d}", None)
        for sid in [] for m in []
    }
    if len(outer_map) != expected_outers:
        raise PackageVerificationError("outer-world record cardinality differs from 13 x M")
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
        for contribution in contributions:
            outer_id = contribution.get("outer_replicate_id")
            if outer_id in seen_m:
                raise PackageVerificationError("pair ledger duplicates an M contribution")
            seen_m.add(outer_id)
            scenario_id = pair["key"][0]
            base = (scenario_id, versions[scenario_id], n_units, outer_id)
            outer = outer_by_base.get(base)
            if outer is None or contribution.get("world_seed") != outer["world_seed"]:
                raise PackageVerificationError("pair-ledger contribution world_seed differs from its outer-world RUN")
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
            for report_obj, snapshot_obj, label in (
                (analyzer_report, analyzer_snapshot, "AnalyzerResult"),
                (contract_report, contract_snapshot, "AnalysisContract"),
                (manifest_report, manifest_snapshot, "RunManifest"),
            ):
                if report_obj != _snapshot_source_value(snapshot_obj):
                    raise PackageVerificationError(f"report RUN {label} differs from captured snapshot")
            if row.get("run_report") != _snapshot_source_value(decoded["evaluation_report"]):
                raise PackageVerificationError("report RUN evaluation summary differs from EvaluationReport snapshot")
            repeated_reports = [
                _snapshot_source_value(decoded_by_key[key]["evaluation_report"])
                for key in outer["repeated_keys"]
            ]
            if row.get("repeated_report") != _snapshot_source_value(outer["repeated_report"]):
                raise PackageVerificationError("report repeated aggregate differs from RepeatedAssignmentReport snapshot")
            if len(repeated_reports) != R:
                raise PackageVerificationError("repeated report source cardinality differs from R")

    # Evidence index is an exact, ordered one-to-one projection of outer-world keys.
    evidence_index = run_file["evidence_index"]
    if not isinstance(evidence_index, list) or len(evidence_index) != expected_outers:
        raise PackageVerificationError("RUN evidence_index cardinality differs from 13 x M")
    expected_index = [
        {"scenario_id": sid, "outer_replicate_id": f"outer-{m:06d}",
         "world_id": outer_by_base[(sid, versions[sid], n_units, f"outer-{m:06d")]["run_key"][6]}
        for sid in [] for m in []
    ]
    # The evidence_index world_id is compared to the corresponding outer key, not to run_id.
    consumed_index = set()
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
    if consumed_index != expected_bases:
        raise PackageVerificationError("evidence_index does not consume every outer-world key exactly once")
    return len(run_map), len(outer_map)



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
    if len(set(declared_ids)) != 13 or set(scenarios) != set(declared_ids):
        raise PackageVerificationError("report scenario reports differ from declared scenario registry")
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
    reconciled_run_count, reconciled_outer_count = _reconcile_run_records(parsed, decoded_report)
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
        "RUN/R FrozenSnapshot decoding and exact source joins are not implemented in this verifier slice.",
        "Calibration/evaluation seed disjointness and Gate159 derived-status recomputation are not implemented.",
        "Source-execution metadata has not been independently resolved against GitHub.",
        "Technical-test evidence has not been independently bound to a trusted workflow run/artifact.",
        "External attestation/signature verification is not implemented; package is NOT_AUTHENTICATED.",
    )
    return PackageVerificationResult(
        PACKAGE_SCHEMA_ID, PACKAGE_SCHEMA_VERSION, manifest["profile"],
        archive_sha, manifest_sha, package_id, len(extracted),
        "PASS", "PARTIAL", "STRUCTURAL_ONLY", "NOT_VERIFIED",
        "NOT_VERIFIED", "NOT_VERIFIED", "NOT_AUTHENTICATED", limitations,
    )
