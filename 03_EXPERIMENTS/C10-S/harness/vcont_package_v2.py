"""Pure V_cont package-v2 file canonicalizer and deterministic TAR writer.

This module accepts already materialized evidence payloads. It never invokes
Generator, Sealer, Analyzer, Evaluator, producers, seed generation or calibration.
It does not independently validate scientific/provenance joins; the verifier is
a separate implementation and must recompute those claims from archive content.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import io
import tarfile
import unicodedata
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
COMPANION_PATHS = frozenset(PACKAGE_PATHS) - {
    "manifest.json",
    "report/report.json",
    "design/scenario_estimand_matrix.json",
}

class PackageBuildError(ValueError):
    """Raised when a package input is incomplete or violates the wire contract."""


@dataclass(frozen=True)
class VContPackageCompanionsV2:
    """Actual independently materialized JSON payloads for all non-capture files."""
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


def serialize_package_files_v2(
    captured: Any,
    design: Any,
    companions: VContPackageCompanionsV2,
    *,
    profile: str,
) -> Mapping[str, bytes]:
    """Serialize the exact 13 data files; manifest and TAR are added by builder.

    Companion payloads are supplied as actual records, never synthesized here.
    This boundary validates presence, top-level shape and schema identity only.
    Semantic joins and evidence status require independent verification.
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
    if not isinstance(matrix, object) or matrix is None or not callable(getattr(matrix, "to_payload", None)):
        raise PackageBuildError("immutable MatrixCapture is required")
    if (getattr(matrix, "schema_id", None) != MATRIX_SCHEMA_ID
            or getattr(matrix, "schema_version", None) != MATRIX_SCHEMA_VERSION
            or getattr(matrix, "row_count", None) != 52):
        raise PackageBuildError("MatrixCapture schema or cardinality mismatch")
    matrix_bytes = getattr(matrix, "canonical_bytes", None)
    if not isinstance(matrix_bytes, bytes) or _sha256(matrix_bytes) == "":
        raise PackageBuildError("MatrixCapture canonical bytes are absent")
    if not isinstance(report, object) or report is None:
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
        report_envelope = __import__("json").loads(report_bytes.decode("utf-8"))
        matrix_payload = matrix.to_payload()
    except Exception as exc:
        raise PackageBuildError(f"capture snapshot cannot be decoded: {exc}") from exc
    if (not isinstance(report_envelope, dict)
            or report_envelope.get("schema_id") != REPORT_SCHEMA_ID
            or report_envelope.get("schema_version") != REPORT_SCHEMA_VERSION
            or report_envelope.get("payload_type") != REPORT_PAYLOAD_TYPE):
        raise PackageBuildError("report snapshot envelope differs from the declared v2.1 schema")
    if report_envelope.get("legacy_report_fingerprint") != getattr(report, "legacy_report_fingerprint", None):
        raise PackageBuildError("report snapshot legacy fingerprint metadata mismatch")
    if (not isinstance(matrix_payload, dict)
            or matrix_payload.get("schema_id") != MATRIX_SCHEMA_ID
            or matrix_payload.get("schema_version") != MATRIX_SCHEMA_VERSION
            or matrix_payload.get("row_count") != 52):
        raise PackageBuildError("MatrixCapture payload envelope mismatch")

    payloads: dict[str, Mapping[str, Any]] = {
        "report/report.json": report_envelope,
        "design/scenario_estimand_matrix.json": matrix_payload,
    }
    for path in sorted(COMPANION_PATHS):
        value = companions.files[path]
        if not isinstance(value, Mapping):
            raise PackageBuildError(f"{path} must be a materialized JSON object")
        if path == "design/benchmark_design.json":
            declared = value.get("capture_id")
            if declared != capture_id:
                raise PackageBuildError("benchmark design companion must bind the exact capture_id")
        if path == "runs/run_records.json":
            if value.get("benchmark_export_id") != capture_id:
                raise PackageBuildError("RUN export envelope must bind benchmark_export_id to capture_id")
            if value.get("schema_version") != "2.0.0":
                raise PackageBuildError("RUN export envelope must be v2.0.0")
        payloads[path] = value

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
