"""Pure V_cont package-v2 file canonicalizer and deterministic TAR writer.

This module accepts already materialized evidence payloads and captured
snapshots. It never invokes Generator, Sealer, Analyzer, Evaluator, producers,
seed generation or calibration. It assembles only the two Gate 194 configuration
companions and checks their immediate source bindings; the independent verifier
separately reconstructs those claims from archive content.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import io
import json
import tarfile
import unicodedata
from typing import Any, Mapping

import rfc8785
from vcont_benchmark_protocol import SCENARIO_IDS, SeedAssignment
from vcont_integrated_harness import AnalysisContract, Analyzer, RunManifest


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
GENERATED_COMPANION_PATHS = frozenset({
    "design/analysis_contracts.json",
    "provenance/configuration_fingerprints.json",
})
COMPANION_PATHS = frozenset(PACKAGE_PATHS) - {
    "manifest.json",
    "report/report.json",
    "design/scenario_estimand_matrix.json",
} - GENERATED_COMPANION_PATHS

class PackageBuildError(ValueError):
    """Raised when a package input is incomplete or violates the wire contract."""


@dataclass(frozen=True)
class VContPackageCompanionsV2:
    """Caller-materialized non-capture payloads; two configuration companions are derived here."""
    files: Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class PackageBuildResult:
    schema_id: str
    schema_version: str
    capture_id: str
    benchmark_export_id: str
    file_paths: tuple[str, ...]
    file_inventory: tuple[tuple[str, int, str], ...]
    manifest_sha256: str
    package_id: str
    archive_bytes: bytes
    archive_sha256: str


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _jcs_json(value: Any) -> bytes:
    try:
        encoded = rfc8785.dumps(value)
    except Exception as exc:
        raise PackageBuildError(f"payload is not RFC 8785 serializable: {exc}") from exc
    if not isinstance(encoded, bytes):
        raise PackageBuildError("RFC 8785 implementation did not return bytes")
    return encoded + b"\n"



def _design_identity(design: Any) -> dict[str, Any]:
    versions = tuple(design.scenario_versions)
    return {
        "scenario_versions": [
            {"scenario_id": sid, "scenario_version": version}
            for sid, version in versions
        ],
        "N": design.n_units,
        "M": design.outer_replicates,
        "R": design.repeated_assignments,
        "matrix_fingerprint": design.matrix_fingerprint,
        "metric_targets": _jcs_safe_source(design.metric_targets),
        "seed_bank_label": design.seed_bank_label,
        "seed_bank_fingerprint": design.seed_bank_fingerprint,
        "executable_commit": design.executable_commit,
        "configuration_fingerprint": design.configuration_fingerprint,
    }


def _uint64_wire(value: int) -> dict[str, str]:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= (1 << 64) - 1:
        raise PackageBuildError("seed source is not an exact uint64 integer")
    return {"$type": "uint64", "decimal": str(value)}


def _jcs_safe_source(value: Any) -> Any:
    """Independent exact source-to-JSON conversion used by capture identity v2."""
    from dataclasses import asdict, is_dataclass
    from enum import Enum
    import math
    if is_dataclass(value) and not isinstance(value, type):
        return _jcs_safe_source(asdict(value))
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise PackageBuildError("capture identity requires string object keys")
        return {key: _jcs_safe_source(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jcs_safe_source(item) for item in value]
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, int):
        if abs(value) > (1 << 64) - 1:
            raise PackageBuildError("capture identity source integer exceeds uint64 domain")
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise PackageBuildError("capture identity rejects NaN and infinity")
        return value
    raise PackageBuildError(f"unsupported capture identity source type: {type(value).__name__}")


def _legacy_report_fingerprint(manifest_payload: Any) -> str:
    import json
    from dataclasses import asdict
    normalized = json.loads(json.dumps(manifest_payload, default=asdict, sort_keys=True))
    payload = json.dumps(normalized, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return _sha256(payload)


def _decode_report_uint64(value: Any) -> Any:
    if isinstance(value, dict):
        if "$type" in value:
            if set(value) != {"$type", "decimal"} or value.get("$type") != "uint64":
                raise PackageBuildError("report contains a malformed typed uint64 wrapper")
            decimal = value.get("decimal")
            if (not isinstance(decimal, str) or not decimal.isascii()
                    or not decimal.isdigit() or (len(decimal) > 1 and decimal.startswith("0"))):
                raise PackageBuildError("report contains a noncanonical uint64 decimal")
            number = int(decimal)
            if number > (1 << 64) - 1:
                raise PackageBuildError("report uint64 wrapper exceeds the source domain")
            return number
        return {key: _decode_report_uint64(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_decode_report_uint64(item) for item in value]
    return value


def _recompute_capture_id(captured: Any, design_identity: dict[str, Any]) -> str:
    bundles = tuple(captured.outer_world_bundles)
    ordered = sorted(
        bundles,
        key=lambda item: (
            SCENARIO_IDS.index(item.scenario_id),
            int(item.outer_replicate_id.split("-")[-1]),
        ),
    )
    if tuple(item["scenario_id"] for item in design_identity["scenario_versions"]) != tuple(SCENARIO_IDS):
        raise PackageBuildError("capture design scenario order is not canonical")
    if len(ordered) != len(SCENARIO_IDS) * design_identity["M"]:
        raise PackageBuildError("capture outer-world bundle cardinality mismatch")
    expected_pairs = {
        (sid, f"outer-{m:06d}")
        for sid in SCENARIO_IDS for m in range(design_identity["M"])
    }
    observed_pairs = {(item.scenario_id, item.outer_replicate_id) for item in ordered}
    if observed_pairs != expected_pairs:
        raise PackageBuildError("capture outer-world bundle keys are missing, duplicated or noncanonical")

    assignment_rows = []
    bundle_digests = []
    declared_versions = {row["scenario_id"]: row["scenario_version"]
                         for row in design_identity["scenario_versions"]}
    for bundle in ordered:
        if (bundle.scenario_id not in declared_versions
                or bundle.scenario_version != declared_versions[bundle.scenario_id]
                or bundle.n_units != design_identity["N"]):
            raise PackageBuildError("outer-world bundle scenario/version/N differs from design identity")
        run_bundles = (bundle.run_bundle,) + tuple(bundle.repeated_bundles)
        if len(run_bundles) != 1 + design_identity["R"]:
            raise PackageBuildError("outer-world RUN/R bundle cardinality mismatch")
        snapshot_records = []
        for run in run_bundles:
            assignment = run.assignment.restore(SeedAssignment)
            assignment_rows.append({
                "bank": assignment.bank,
                "scenario_id": assignment.scenario_id,
                "scenario_version": assignment.scenario_version,
                "n_units": assignment.n_units,
                "replicate": assignment.replicate,
                "outer_replicate_id": assignment.outer_replicate_id,
                "assignment_role": assignment.assignment_role,
                "world_seed": _uint64_wire(assignment.world_seed),
                "z_assignment_seed": _uint64_wire(assignment.z_assignment_seed),
                "g_assignment_seed": _uint64_wire(assignment.g_assignment_seed),
            })
            snapshot_records.append({
                field: {"type_id": getattr(run, field).type_id, "sha256": getattr(run, field).sha256}
                for field in (
                    "assignment", "scenario_config", "run_manifest", "truth_projection",
                    "evidence_candidate", "sealed_evidence", "analysis_contract",
                    "analyzer_result", "evaluation_report",
                )
            })
        projection = {
            "scenario_id": bundle.scenario_id,
            "scenario_version": bundle.scenario_version,
            "n_units": bundle.n_units,
            "outer_replicate_id": bundle.outer_replicate_id,
            "world_id": bundle.world_id,
            "world_version": bundle.world_version,
            "world_seed": _uint64_wire(bundle.world_seed),
            "run_and_repeated_snapshot_records": snapshot_records,
            "repeated_assignment_report": {
                "type_id": bundle.repeated_assignment_report.type_id,
                "sha256": bundle.repeated_assignment_report.sha256,
            },
        }
        bundle_digests.append(_sha256(rfc8785.dumps(projection)))

    evidence_rows = [
        {"scenario_id": sid, "outer_replicate_id": outer_id, "world_id": world_id}
        for sid, outer_id, world_id in captured.evidence_index
    ]
    expected_evidence = [
        {"scenario_id": item.scenario_id, "outer_replicate_id": item.outer_replicate_id,
         "world_id": item.world_id}
        for item in ordered
    ]
    if evidence_rows != expected_evidence:
        raise PackageBuildError("capture evidence_index does not match ordered outer-world bundles")
    assignment_digest = _sha256(rfc8785.dumps({"rows": assignment_rows}))
    identity = {
        "schema_id": "TGCV-C10S-VCONT-BENCHMARK-CAPTURE-IDENTITY",
        "schema_version": "2.0.0",
        "design_identity": design_identity,
        "matrix_full_sha256": captured.matrix_capture.full_matrix_sha256,
        "evaluation_seed_manifest_sha256": assignment_digest,
        "outer_world_bundle_digests": bundle_digests,
        "report_snapshot_sha256": captured.report_snapshot.sha256,
        "evidence_index": evidence_rows,
    }
    return _sha256(rfc8785.dumps(identity))

def _validate_path(path: str) -> None:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        raise PackageBuildError("package path must be a nonempty relative POSIX path")
    if unicodedata.normalize("NFC", path) != path:
        raise PackageBuildError("package path is not NFC-normalized")
    parts = path.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise PackageBuildError("package path contains an empty, dot or parent component")
    if any(ord(ch) < 32 for ch in path):
        raise PackageBuildError("package path contains a control character")


def build_deterministic_tar_v2(files: Mapping[str, bytes]) -> bytes:
    """Build an uncompressed, normalized USTAR archive from exact file bytes."""
    if not isinstance(files, Mapping) or not files:
        raise PackageBuildError("archive input must be a nonempty path-to-bytes mapping")
    normalized: dict[str, bytes] = {}
    folded: set[str] = set()
    for path, payload in files.items():
        _validate_path(path)
        if path in normalized or path.casefold() in folded:
            raise PackageBuildError("duplicate or case-colliding normalized archive path")
        if not isinstance(payload, bytes):
            raise PackageBuildError("archive payloads must be immutable bytes")
        normalized[path] = payload
        folded.add(path.casefold())
    output = io.BytesIO()
    try:
        with tarfile.open(fileobj=output, mode="w", format=tarfile.USTAR_FORMAT) as archive:
            for path in sorted(normalized):
                info = tarfile.TarInfo(path)
                info.size = len(normalized[path])
                info.mtime = 0
                info.uid = 0
                info.gid = 0
                info.uname = ""
                info.gname = ""
                info.mode = 0o644
                info.type = tarfile.REGTYPE
                info.pax_headers = {}
                archive.addfile(info, io.BytesIO(normalized[path]))
    except (tarfile.TarError, ValueError, OSError) as exc:
        raise PackageBuildError(f"deterministic USTAR construction failed: {exc}") from exc
    return output.getvalue()



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


def _digest_jcs(value: Any) -> str:
    return _sha256(rfc8785.dumps(value))


def _analysis_contract_payload_digest(
    scenario_id: str, scenario_version: str, n_units: int,
    analyzer_version: str, contract_payload: Mapping[str, Any],
) -> str:
    payload = {
        "schema_id": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
        "schema_version": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
        "scenario_id": scenario_id,
        "scenario_version": scenario_version,
        "n_units": n_units,
        "analyzer_version": analyzer_version,
        "analysis_contract": dict(contract_payload),
    }
    return _digest_jcs(payload)


def _assemble_analysis_contracts_v1(
    captured: Any, design: Any, run_records: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the 13/26 companion from retained RUN/R snapshots, not caller declarations."""
    versions = tuple(design.scenario_versions)
    if tuple(row[0] for row in versions) != tuple(SCENARIO_IDS):
        raise PackageBuildError("analysis-contract source design is not in authoritative scenario order")
    M, R, n_units = design.outer_replicates, design.repeated_assignments, design.n_units
    records = run_records.get("run_evidence_records")
    if not isinstance(records, list) or len(records) != len(SCENARIO_IDS) * M * (1 + R):
        raise PackageBuildError("analysis-contract assembly requires the exact RUN/R record universe")
    bundles = tuple(captured.outer_world_bundles)
    ordered = sorted(
        bundles,
        key=lambda item: (SCENARIO_IDS.index(item.scenario_id), int(item.outer_replicate_id.split("-")[-1])),
    )
    if len(ordered) != len(SCENARIO_IDS) * M:
        raise PackageBuildError("analysis-contract source bundle cardinality mismatch")
    source_rows = []
    applicability = []
    for s, (scenario_id, scenario_version) in enumerate(versions):
        scenario_bundles = [b for b in ordered if b.scenario_id == scenario_id]
        if len(scenario_bundles) != M:
            raise PackageBuildError("analysis-contract source lacks an exact scenario/M bundle set")
        source_contract = None
        for m, bundle in enumerate(scenario_bundles):
            if (bundle.scenario_version, bundle.n_units, bundle.outer_replicate_id) != (
                scenario_version, n_units, f"outer-{m:06d}"
            ):
                raise PackageBuildError("analysis-contract source bundle key/order mismatch")
            run_bundles = (bundle.run_bundle,) + tuple(bundle.repeated_bundles)
            if len(run_bundles) != 1 + R:
                raise PackageBuildError("analysis-contract source RUN/R cardinality mismatch")
            for r_index, run_bundle in enumerate(run_bundles):
                assignment = run_bundle.assignment.restore(SeedAssignment)
                expected_role, expected_index = ("RUN", -1) if r_index == 0 else ("REPEATED_ASSIGNMENT", r_index - 1)
                if isinstance(assignment.replicate, bool) or not isinstance(assignment.replicate, int):
                    raise PackageBuildError("captured SeedAssignment replicate must be an exact integer")
                if isinstance(assignment.n_units, bool) or not isinstance(assignment.n_units, int) or assignment.n_units < 1:
                    raise PackageBuildError("captured SeedAssignment n_units must be an exact positive integer")
                if assignment.bank != "evaluation":
                    raise PackageBuildError("captured AnalysisContract source is not from the evaluation bank")
                if (assignment.scenario_id, assignment.scenario_version, assignment.n_units,
                    assignment.outer_replicate_id, assignment.assignment_role, assignment.assignment_index) != (
                    scenario_id, scenario_version, n_units, f"outer-{m:06d}", expected_role, expected_index
                ):
                    raise PackageBuildError("captured AnalysisContract source does not match its full RUN/R assignment key")
                contract_snapshot = run_bundle.analysis_contract
                if contract_snapshot.type_id != "vcont_integrated_harness.AnalysisContract":
                    raise PackageBuildError("captured AnalysisContract snapshot type_id mismatch")
                contract = run_bundle.analysis_contract.restore(AnalysisContract)
                contract_payload = asdict(contract)
                if source_contract is None:
                    source_contract = contract_payload
                elif contract_payload != source_contract:
                    raise PackageBuildError("AnalysisContract differs across RUN/R snapshots for one scenario")
                record_index = s * M * (1 + R) + m * (1 + R) + r_index
                record = records[record_index]
                manifest = run_bundle.run_manifest.restore(RunManifest)
                key = record.get("key") if isinstance(record, Mapping) else None
                if not isinstance(key, Mapping) or (
                    key.get("scenario_id"), key.get("scenario_version"), key.get("N"),
                    key.get("outer_replicate_id"), key.get("assignment_role"),
                    key.get("assignment_index"), key.get("run_id")
                ) != (
                    scenario_id, scenario_version, n_units, f"outer-{m:06d}",
                    expected_role, expected_index, manifest.run_id
                ):
                    raise PackageBuildError("RUN/R record order/key does not bind to captured AnalysisContract snapshot")
                refs = record.get("snapshot_refs")
                ref = refs.get("analysis_contract") if isinstance(refs, Mapping) else None
                if not isinstance(ref, Mapping) or (
                    ref.get("type_id"), ref.get("serialization_id"), ref.get("sha256")
                ) != (
                    contract_snapshot.type_id, "TGCV-FROZEN-SNAPSHOT-1", contract_snapshot.sha256
                ):
                    raise PackageBuildError("RUN/R AnalysisContract snapshot reference differs from retained source bytes")
        if source_contract is None:
            raise PackageBuildError("scenario has no source AnalysisContract")
        digest = _analysis_contract_payload_digest(
            scenario_id, scenario_version, n_units, Analyzer.version, source_contract
        )
        source_rows.append({
            "scenario_id": scenario_id,
            "scenario_version": scenario_version,
            "n_units": n_units,
            "analyzer_version": Analyzer.version,
            "analysis_contract": source_contract,
            "contract_payload_digest": digest,
        })
        for run_family in ("RUN", "REPEATED_ASSIGNMENT"):
            applicability.append({
                "scenario_id": scenario_id,
                "scenario_version": scenario_version,
                "n_units": n_units,
                "run_family": run_family,
                "contract_payload_digest": digest,
            })
    return {
        "schema_id": ANALYSIS_CONTRACTS_SCHEMA_ID,
        "schema_version": ANALYSIS_CONTRACTS_SCHEMA_VERSION,
        "benchmark_export_id": captured.capture_id,
        "source_contracts": source_rows,
        "applicability": applicability,
    }



def _decode_assignment_uint64_wire(value: Any) -> int:
    if not isinstance(value, Mapping) or set(value) != {"$type", "decimal"} or value.get("$type") != "uint64":
        raise PackageBuildError("evaluation SeedAssignment contains a malformed uint64 wire value")
    decimal = value.get("decimal")
    if (not isinstance(decimal, str) or not decimal.isascii() or not decimal.isdigit()
            or (len(decimal) > 1 and decimal.startswith("0"))):
        raise PackageBuildError("evaluation SeedAssignment contains a noncanonical uint64 decimal")
    number = int(decimal)
    if number > (1 << 64) - 1:
        raise PackageBuildError("evaluation SeedAssignment uint64 exceeds its source domain")
    return number


def _recompute_seed_derivation(assignments: Mapping[str, Any], rows: Any) -> None:
    """Recompute every evaluation seed from the frozen Gate 181 descriptor."""
    descriptor = assignments.get("seed_derivation")
    required = {"algorithm", "hash", "output_rule", "namespace"}
    if (not isinstance(descriptor, Mapping) or set(descriptor) != required
            or descriptor.get("algorithm") != "TGCV-C10S-VCONT-SEED-v3"
            or descriptor.get("hash") != "SHA-256"
            or descriptor.get("output_rule") != "first_8_digest_bytes_unsigned_big_endian"
            or not isinstance(descriptor.get("namespace"), str)
            or not descriptor["namespace"].strip()):
        raise PackageBuildError("evaluation seed_derivation descriptor is invalid")
    if not isinstance(rows, list) or not rows:
        raise PackageBuildError("seed derivation requires nonempty evaluation assignment rows")
    namespace = descriptor["namespace"]

    def derive(row: Mapping[str, Any], stream: str, role: str, replicate: int) -> int:
        payload = (
            f"TGCV-C10S-VCONT-SEED-v3|{namespace}|{row['bank']}|{row['scenario_id']}|"
            f"{row['scenario_version']}|{row['n_units']}|{row['outer_replicate_id']}|"
            f"{role}|{replicate}|{stream}"
        )
        return int.from_bytes(hashlib.sha256(payload.encode("utf-8")).digest()[:8], "big")

    for index, row in enumerate(rows):
        if not isinstance(row, Mapping):
            raise PackageBuildError("seed derivation assignment row must be an object")
        role, replicate = row.get("assignment_role"), row.get("replicate")
        if role not in ("RUN", "REPEATED_ASSIGNMENT"):
            raise PackageBuildError("seed derivation assignment role is invalid")
        if isinstance(replicate, bool) or not isinstance(replicate, int):
            raise PackageBuildError("seed derivation replicate must be an exact integer")
        if (role == "RUN" and replicate != -1) or (role == "REPEATED_ASSIGNMENT" and replicate < 0):
            raise PackageBuildError("seed derivation role/replicate identity is invalid")
        expected = {
            "world_seed": derive(row, "world", "RUN", -1),
            "z_assignment_seed": derive(row, "z", role, replicate),
            "g_assignment_seed": derive(row, "g", role, replicate),
        }
        for field, value in expected.items():
            actual = _decode_assignment_uint64_wire(row.get(field))
            if actual != value:
                raise PackageBuildError(
                    f"evaluation seed derivation mismatch at row {index}: {field}"
                )


def _legacy_seed_bank_fingerprint_from_wire_rows(rows: Any, design: Any) -> str:
    required = {
        "bank", "scenario_id", "scenario_version", "n_units", "replicate",
        "outer_replicate_id", "assignment_role", "world_seed",
        "z_assignment_seed", "g_assignment_seed",
    }
    if not isinstance(rows, list) or not rows:
        raise PackageBuildError("historical seed-bank fingerprint requires nonempty evaluation rows")
    versions = dict(design.scenario_versions)
    expected_order = [
        (sid, versions[sid], design.n_units, f"outer-{m:06d}", role, index)
        for sid in SCENARIO_IDS for m in range(design.outer_replicates)
        for role, index in ([("RUN", -1)] + [
            ("REPEATED_ASSIGNMENT", r) for r in range(design.repeated_assignments)
        ])
    ]
    payload = []
    observed_order = []
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != required or row.get("bank") != "evaluation":
            raise PackageBuildError("historical seed-bank fingerprint row field/bank mismatch")
        if (not isinstance(row["scenario_id"], str) or not row["scenario_id"]
                or not isinstance(row["scenario_version"], str) or not row["scenario_version"]
                or isinstance(row["n_units"], bool) or not isinstance(row["n_units"], int) or row["n_units"] < 1
                or isinstance(row["replicate"], bool) or not isinstance(row["replicate"], int)
                or not isinstance(row["outer_replicate_id"], str) or not row["outer_replicate_id"]
                or row["assignment_role"] not in ("RUN", "REPEATED_ASSIGNMENT")):
            raise PackageBuildError("historical seed-bank fingerprint identity field types are invalid")
        observed_order.append((
            row["scenario_id"], row["scenario_version"], row["n_units"],
            row["outer_replicate_id"], row["assignment_role"], row["replicate"],
        ))
        payload.append({
            "bank": row["bank"],
            "scenario_id": row["scenario_id"],
            "scenario_version": row["scenario_version"],
            "n_units": row["n_units"],
            "outer_replicate_id": row["outer_replicate_id"],
            "assignment_role": row["assignment_role"],
            "replicate": row["replicate"],
            "world_seed": _decode_assignment_uint64_wire(row["world_seed"]),
            "z_assignment_seed": _decode_assignment_uint64_wire(row["z_assignment_seed"]),
            "g_assignment_seed": _decode_assignment_uint64_wire(row["g_assignment_seed"]),
        })
    if observed_order != expected_order:
        raise PackageBuildError("historical seed-bank rows are not in frozen scenario/M/R order")
    return _sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8"))

def _assemble_configuration_fingerprints_v1(
    benchmark_export_id: str,
    design: Any,
    effective_configs: Mapping[str, Any],
    analysis_contracts: Mapping[str, Any],
    matrix: Mapping[str, Any],
    assignments: Mapping[str, Any],
    benchmark_design: Mapping[str, Any],
    run_records: Mapping[str, Any],
) -> dict[str, Any]:
    """Derive the 28 semantic components and aggregate from source companions."""
    effective_rows = effective_configs.get("rows")
    source_contracts = analysis_contracts.get("source_contracts")
    assignment_rows = assignments.get("rows")
    run_rows = run_records.get("run_evidence_records")
    if not isinstance(effective_rows, list) or len(effective_rows) != 13:
        raise PackageBuildError("fingerprint assembly requires exactly 13 effective ScenarioConfig rows")
    if (effective_configs.get("schema_id"), effective_configs.get("schema_version")) != (
        "TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION", "2.0.0"
    ):
        raise PackageBuildError("effective ScenarioConfig source schema/version mismatch")
    if (analysis_contracts.get("schema_id"), analysis_contracts.get("schema_version"),
        analysis_contracts.get("benchmark_export_id")) != (
        ANALYSIS_CONTRACTS_SCHEMA_ID, ANALYSIS_CONTRACTS_SCHEMA_VERSION, benchmark_export_id
    ):
        raise PackageBuildError("AnalysisContract companion schema/version/export identity mismatch")
    if design.configuration_fingerprint != benchmark_design.get("configuration_fingerprint"):
        raise PackageBuildError("source design object and benchmark_design companion declarations differ")
    _recompute_seed_derivation(assignments, assignment_rows)
    legacy_seed_fingerprint = _legacy_seed_bank_fingerprint_from_wire_rows(assignment_rows, design)
    if (legacy_seed_fingerprint != design.seed_bank_fingerprint
            or legacy_seed_fingerprint != benchmark_design.get("seed_bank_fingerprint")
            or legacy_seed_fingerprint != assignments.get("seed_bank_fingerprint_legacy")):
        raise PackageBuildError("historical source-typed seed_bank_fingerprint does not recompute")
    if not isinstance(source_contracts, list) or len(source_contracts) != 13:
        raise PackageBuildError("fingerprint assembly requires exactly 13 source AnalysisContract rows")
    if not isinstance(assignment_rows, list) or not assignment_rows:
        raise PackageBuildError("fingerprint assembly requires ordered evaluation assignment rows")
    if not isinstance(run_rows, list):
        raise PackageBuildError("fingerprint assembly requires RUN evidence records")
    components = []
    for index, row in enumerate(effective_rows):
        if not isinstance(row, Mapping):
            raise PackageBuildError("effective ScenarioConfig row is not an object")
        sid, version, n_units = row.get("scenario_id"), row.get("scenario_version"), row.get("n_units")
        source = source_contracts[index]
        if (sid, version, n_units) != (
            source.get("scenario_id"), source.get("scenario_version"), source.get("n_units")
        ) or sid != SCENARIO_IDS[index]:
            raise PackageBuildError("effective ScenarioConfig and AnalysisContract scenario scopes diverge")
        scope = [sid, version, n_units]
        components.append({
            "component_id": f"dgp-generator:{sid}:{version}:{n_units}",
            "component_type": "DGP_GENERATOR_CONFIG",
            "scope_key": scope,
            "source_ref": f"design/effective_scenario_configs.json#/rows/{index}",
            "payload_schema_id": "TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION",
            "payload_schema_version": "2.0.0",
            "algorithm_id": DGP_CONFIG_DIGEST_ALGORITHM,
            "digest_sha256": _digest_jcs(row),
        })
    for index, row in enumerate(source_contracts):
        if not isinstance(row, Mapping):
            raise PackageBuildError("source AnalysisContract row is not an object")
        sid, version, n_units = row.get("scenario_id"), row.get("scenario_version"), row.get("n_units")
        if sid != SCENARIO_IDS[index]:
            raise PackageBuildError("source AnalysisContract rows are not in authoritative scenario order")
        scope = [sid, version, n_units]
        run_index = index * design.outer_replicates * (1 + design.repeated_assignments)
        if run_index >= len(run_rows):
            raise PackageBuildError("derived representative RUN AnalysisContract source index is out of range")
        record = run_rows[run_index]
        key = record.get("key") if isinstance(record, Mapping) else None
        if not isinstance(key, Mapping) or (
            key.get("scenario_id"), key.get("scenario_version"), key.get("N"),
            key.get("outer_replicate_id"), key.get("assignment_role"), key.get("assignment_index")
        ) != (sid, version, n_units, "outer-000000", "RUN", -1):
            raise PackageBuildError("derived representative RUN AnalysisContract source index is not the canonical source row")
        expected_contract_digest = _analysis_contract_payload_digest(
            sid, version, n_units, row.get("analyzer_version"), row.get("analysis_contract")
        )
        if row.get("analyzer_version") != Analyzer.version or expected_contract_digest != row.get("contract_payload_digest"):
            raise PackageBuildError("AnalysisContract semantic digest/version does not recompute")
        components.append({
            "component_id": f"analyzer-contract:{sid}:{version}:{n_units}",
            "component_type": "ANALYZER_EFFECTIVE_CONTRACT",
            "scope_key": scope,
            "source_ref": f"runs/run_records.json#/run_evidence_records/{run_index}/snapshot_refs/analysis_contract",
            "payload_schema_id": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_ID,
            "payload_schema_version": EFFECTIVE_ANALYSIS_CONTRACT_SCHEMA_VERSION,
            "algorithm_id": ANALYSIS_CONTRACT_DIGEST_ALGORITHM,
            "digest_sha256": row.get("contract_payload_digest"),
        })
    if (matrix.get("schema_id"), matrix.get("schema_version")) != (MATRIX_SCHEMA_ID, MATRIX_SCHEMA_VERSION):
        raise PackageBuildError("MatrixCapture source schema/version mismatch during fingerprint assembly")
    components.append({
        "component_id": "scenario-estimand-matrix",
        "component_type": "SCENARIO_ESTIMAND_MATRIX",
        "scope_key": benchmark_export_id,
        "source_ref": "design/scenario_estimand_matrix.json#",
        "payload_schema_id": MATRIX_SCHEMA_ID,
        "payload_schema_version": MATRIX_SCHEMA_VERSION,
        "algorithm_id": "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1",
        "digest_sha256": matrix.get("full_matrix_sha256"),
    })
    if (assignments.get("schema_id"), assignments.get("schema_version"), assignments.get("bank")) != (
        "TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS", "2.0.0", "evaluation"
    ):
        raise PackageBuildError("evaluation assignment source schema/version/bank mismatch")
    components.append({
        "component_id": "evaluation-seed-bank",
        "component_type": "EVALUATION_SEED_BANK",
        "scope_key": benchmark_export_id,
        "source_ref": "seeds/evaluation_seed_assignments.json#/rows",
        "payload_schema_id": assignments["schema_id"],
        "payload_schema_version": assignments["schema_version"],
        "algorithm_id": EVALUATION_ASSIGNMENT_DIGEST_ALGORITHM,
        "digest_sha256": _digest_jcs({"rows": assignment_rows}),
    })
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
    aggregate_digest = _digest_jcs(aggregate_input)
    declared = benchmark_design.get("configuration_fingerprint")
    if declared != aggregate_digest:
        raise PackageBuildError("recomputed aggregate configuration fingerprint differs from benchmark design declaration")
    return {
        "schema_id": CONFIGURATION_FINGERPRINTS_SCHEMA_ID,
        "schema_version": CONFIGURATION_FINGERPRINTS_SCHEMA_VERSION,
        "benchmark_export_id": benchmark_export_id,
        "components": components,
        "aggregate": {
            "algorithm_id": AGGREGATE_FINGERPRINT_ALGORITHM,
            "digest_sha256": aggregate_digest,
            "source_design_declaration": SOURCE_DESIGN_DECLARATION,
        },
    }


def serialize_package_files_v2(
    captured: Any,
    design: Any,
    companions: VContPackageCompanionsV2,
    *,
    profile: str,
) -> Mapping[str, bytes]:
    """Serialize the exact 13 data files; manifest and TAR are added by builder.

    All other companion payloads are supplied as materialized records. The two
    configuration companions are rebuilt from captured snapshots and source files;
    independent verification remains a separate implementation.
    """
    if profile != "CONFIRMATORY":
        raise PackageBuildError("Gate 191 defines only the CONFIRMATORY package profile")
    if captured is None or design is None or companions is None:
        raise PackageBuildError("capture, design and companion evidence are mandatory")
    capture_id = getattr(captured, "capture_id", None)
    matrix = getattr(captured, "matrix_capture", None)
    report = getattr(captured, "report_snapshot", None)
    if not isinstance(capture_id, str) or len(capture_id) != 64:
        raise PackageBuildError("capture_id is absent or malformed")
    if matrix is None or not callable(getattr(matrix, "to_payload", None)):
        raise PackageBuildError("immutable MatrixCapture is required")
    if (getattr(matrix, "schema_id", None) != MATRIX_SCHEMA_ID
            or getattr(matrix, "schema_version", None) != MATRIX_SCHEMA_VERSION
            or getattr(matrix, "row_count", None) != 52):
        raise PackageBuildError("MatrixCapture schema or cardinality mismatch")
    matrix_bytes = getattr(matrix, "canonical_bytes", None)
    if not isinstance(matrix_bytes, bytes) or _sha256(matrix_bytes) == "":
        raise PackageBuildError("MatrixCapture canonical bytes are absent")
    if report is None:
        raise PackageBuildError("FrozenReportSnapshot is required")
    if (getattr(report, "schema_id", None) != REPORT_SCHEMA_ID
            or getattr(report, "schema_version", None) != REPORT_SCHEMA_VERSION
            or getattr(report, "payload_type", None) != REPORT_PAYLOAD_TYPE):
        raise PackageBuildError("package v2.0.0 requires FrozenReportSnapshot v2.1.0")
    report_bytes = getattr(report, "canonical_bytes", None)
    report_digest = getattr(report, "sha256", None)
    if not isinstance(report_bytes, bytes) or not isinstance(report_digest, str):
        raise PackageBuildError("FrozenReportSnapshot bytes/digest are absent")
    if _sha256(report_bytes) != report_digest:
        raise PackageBuildError("FrozenReportSnapshot digest does not match retained bytes")
    if getattr(captured, "benchmark_export_id", None) != capture_id:
        raise PackageBuildError("benchmark_export_id must be the exact capture_id alias")
    if not isinstance(companions, VContPackageCompanionsV2) or not isinstance(companions.files, Mapping):
        raise PackageBuildError("companions must be a VContPackageCompanionsV2 mapping")
    if set(companions.files) != COMPANION_PATHS:
        missing = sorted(COMPANION_PATHS - set(companions.files))
        extra = sorted(set(companions.files) - COMPANION_PATHS)
        raise PackageBuildError(f"companion inventory mismatch; missing={missing}; extra={extra}")

    try:
        import json
        report_envelope = json.loads(report_bytes.decode("utf-8"))
        matrix_payload = matrix.to_payload()
        matrix_canonical = rfc8785.dumps(matrix_payload)
        expected_matrix_digest = hashlib.sha256(rfc8785.dumps({
            "schema_id": MATRIX_SCHEMA_ID,
            "schema_version": MATRIX_SCHEMA_VERSION,
            "row_count": 52,
            "rows": matrix_payload.get("rows"),
        })).hexdigest()
        design_identity = _design_identity(design)
        rebuilt_capture_id = _recompute_capture_id(captured, design_identity)
    except Exception as exc:
        raise PackageBuildError(f"capture/source identity reconciliation failed: {exc}") from exc
    if matrix_canonical != matrix.canonical_bytes:
        raise PackageBuildError("MatrixCapture retained bytes differ from its JCS payload")
    if expected_matrix_digest != matrix.full_matrix_sha256:
        raise PackageBuildError("MatrixCapture full-matrix digest does not recompute")
    expected_matrix_design_identity = {
        "scenario_versions": design_identity["scenario_versions"],
        "N": design_identity["N"],
        "M": design_identity["M"],
        "R": design_identity["R"],
        "legacy_matrix_fingerprint": design_identity["matrix_fingerprint"],
    }
    if matrix_payload.get("design_identity") != expected_matrix_design_identity:
        raise PackageBuildError("MatrixCapture design identity differs from the exact declared matrix design projection")
    if rebuilt_capture_id != capture_id:
        raise PackageBuildError("capture_id does not recompute from the retained source evidence")
    if (not isinstance(report_envelope, dict)
            or set(report_envelope) != {
                "schema_id", "schema_version", "payload_type", "legacy_report_fingerprint",
                "legacy_fingerprint_algorithm", "report",
            }
            or report_envelope.get("schema_id") != REPORT_SCHEMA_ID
            or report_envelope.get("schema_version") != REPORT_SCHEMA_VERSION
            or report_envelope.get("payload_type") != REPORT_PAYLOAD_TYPE
            or report_envelope.get("legacy_fingerprint_algorithm") != (
                "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1"
            )
            or report_envelope.get("legacy_fingerprint_algorithm") != getattr(report, "legacy_fingerprint_algorithm", None)):
        raise PackageBuildError("report snapshot envelope/legacy algorithm differs from the exact v2.1 schema")
    if report_envelope.get("legacy_report_fingerprint") != getattr(report, "legacy_report_fingerprint", None):
        raise PackageBuildError("report snapshot legacy fingerprint metadata mismatch")
    report_payload = report_envelope.get("report")
    if not isinstance(report_payload, dict) or not isinstance(report_payload.get("manifest"), dict):
        raise PackageBuildError("FrozenReportSnapshot lacks the complete legacy manifest payload")
    recomputed_legacy_fingerprint = _legacy_report_fingerprint(_decode_report_uint64(report_payload["manifest"]))
    if (recomputed_legacy_fingerprint != report_envelope.get("legacy_report_fingerprint")
            or recomputed_legacy_fingerprint != report_payload.get("report_fingerprint")):
        raise PackageBuildError("historical Evaluator report fingerprint does not recompute from source-domain manifest")
    if rfc8785.dumps(report_envelope) != report_bytes:
        raise PackageBuildError("FrozenReportSnapshot bytes are not canonical RFC 8785 JCS")
    if (not isinstance(matrix_payload, dict)
            or set(matrix_payload) != {
                "schema_id", "schema_version", "design_identity", "row_count", "rows",
                "legacy_matrix_fingerprint", "full_matrix_digest_algorithm", "full_matrix_sha256",
            }
            or matrix_payload.get("schema_id") != MATRIX_SCHEMA_ID
            or matrix_payload.get("schema_version") != MATRIX_SCHEMA_VERSION
            or matrix_payload.get("row_count") != 52
            or matrix_payload.get("full_matrix_digest_algorithm") != "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1"):
        raise PackageBuildError("MatrixCapture payload field/schema/digest-algorithm mismatch")

    payloads: dict[str, Mapping[str, Any]] = {
        "report/report.json": report_envelope,
        "design/scenario_estimand_matrix.json": matrix_payload,
    }
    for path in sorted(COMPANION_PATHS):
        value = companions.files[path]
        if not isinstance(value, Mapping):
            raise PackageBuildError(f"{path} must be a materialized JSON object")
        if path == "design/benchmark_design.json" and not value:
            raise PackageBuildError("benchmark design companion must contain the declared design payload")
        if path == "seeds/evaluation_seed_assignments.json":
            if (value.get("schema_id") != "TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS"
                    or value.get("schema_version") != "2.0.0" or value.get("bank") != "evaluation"
                    or not isinstance(value.get("rows"), list)
                    or value.get("row_count") != len(value["rows"])):
                raise PackageBuildError("evaluation seed assignment envelope is not the exact v2.0.0 rows schema")
        if path == "seeds/calibration_seed_manifest.json":
            if (value.get("schema_id") != "TGCV-C10S-VCONT-CALIBRATION-BANK-MANIFEST"
                    or value.get("schema_version") != "1.0.0" or value.get("bank") != "calibration"
                    or not isinstance(value.get("rows"), list)
                    or value.get("row_count") != len(value["rows"])):
                raise PackageBuildError("calibration seed manifest is not the exact v2.0.0 rows schema")
        if path == "runs/temporal_manifest.json":
            if (value.get("schema_id") != "TGCV-C10S-VCONT-TEMPORAL-MANIFEST"
                    or value.get("schema_version") != "2.0.0"
                    or not isinstance(value.get("rows"), list)
                    or value.get("row_count") != len(value["rows"])):
                raise PackageBuildError("temporal manifest is not the exact v2.0.0 rows schema")
        if path == "runs/run_records.json":
            if (value.get("schema_id") != "TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE"
                    or value.get("schema_version") != "2.0.0"
                    or value.get("benchmark_export_id") != capture_id):
                raise PackageBuildError("RUN export envelope schema/version/identity mismatch")
        if path == "validation/reconciliation_results.json":
            if (value.get("schema_id") != "TGCV-C10S-VCONT-GATE159-RECONCILIATION"
                    or value.get("schema_version") != "1.0.0"
                    or value.get("benchmark_export_id") != capture_id):
                raise PackageBuildError("Gate159 reconciliation companion schema/identity mismatch")
        payloads[path] = value

    try:
        run_records_payload = payloads["runs/run_records.json"]
        analysis_contracts_payload = _assemble_analysis_contracts_v1(captured, design, run_records_payload)
        payloads["design/analysis_contracts.json"] = analysis_contracts_payload
        payloads["provenance/configuration_fingerprints.json"] = _assemble_configuration_fingerprints_v1(
            capture_id,
            design,
            payloads["design/effective_scenario_configs.json"],
            analysis_contracts_payload,
            matrix_payload,
            payloads["seeds/evaluation_seed_assignments.json"],
            payloads["design/benchmark_design.json"],
            run_records_payload,
        )
    except PackageBuildError:
        raise
    except Exception as exc:
        raise PackageBuildError(f"configuration companion assembly failed: {exc}") from exc
    if set(payloads) != set(PACKAGE_PATHS) - {"manifest.json"}:
        raise PackageBuildError("internal package inventory is not the exact 13 data paths")
    return {path: _jcs_json(payloads[path]) for path in sorted(payloads)}


def build_package_v2(
    captured: Any,
    design: Any,
    companions: VContPackageCompanionsV2,
    *,
    profile: str = "CONFIRMATORY",
) -> PackageBuildResult:
    """Build deterministic v2 archive from complete, pre-materialized evidence."""
    files = dict(serialize_package_files_v2(captured, design, companions, profile=profile))
    inventory = tuple(
        (path, len(payload), _sha256(payload))
        for path, payload in sorted(files.items())
    )
    report_envelope = __import__("json").loads(files["report/report.json"].decode("utf-8"))
    manifest = {
        "schema_id": PACKAGE_SCHEMA_ID,
        "schema_version": PACKAGE_SCHEMA_VERSION,
        "profile": profile,
        "canonicalization": "RFC8785-JCS-UTF8-TRAILING-LF",
        "archive_profile": "POSIX-USTAR-UNCOMPRESSED-NORMALIZED-METADATA",
        "report_schema": {
            "schema_id": REPORT_SCHEMA_ID,
            "schema_version": REPORT_SCHEMA_VERSION,
            "payload_type": REPORT_PAYLOAD_TYPE,
        },
        "legacy_report_fingerprint": report_envelope["legacy_report_fingerprint"],
        "package_id_derivation": "SHA256(JCS({schema_id,schema_version,manifest_sha256}))",
        "files": [
            {"path": path, "byte_length": length, "sha256": digest}
            for path, length, digest in inventory
        ],
    }
    manifest_bytes = _jcs_json(manifest)
    manifest_sha = _sha256(manifest_bytes)
    package_id_payload = {
        "schema_id": PACKAGE_SCHEMA_ID,
        "schema_version": PACKAGE_SCHEMA_VERSION,
        "manifest_sha256": manifest_sha,
    }
    package_id = _sha256(rfc8785.dumps(package_id_payload))
    files["manifest.json"] = manifest_bytes
    if tuple(sorted(files)) != tuple(sorted(PACKAGE_PATHS)):
        raise PackageBuildError("final archive inventory differs from frozen 14-path contract")
    archive_bytes = build_deterministic_tar_v2(files)
    return PackageBuildResult(
        PACKAGE_SCHEMA_ID, PACKAGE_SCHEMA_VERSION,
        captured.capture_id, captured.capture_id,
        tuple(sorted(files)),
        tuple((path, len(files[path]), _sha256(files[path])) for path in sorted(files)),
        manifest_sha, package_id, archive_bytes, _sha256(archive_bytes),
    )
