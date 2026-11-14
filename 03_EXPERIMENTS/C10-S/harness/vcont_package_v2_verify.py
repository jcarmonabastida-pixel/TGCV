"""Independent structural verifier for TGCV C10-S V_cont package v2.

This module deliberately does not import or call vcont_package_v2. It verifies
archive integrity, JCS, the frozen inventory, report/matrix schemas and all
registered uint64 wire occurrences. Semantic RUN/R snapshot joins, full Gate159
derivation, source-execution reconciliation, technical-test provenance and
external authentication remain explicitly separate status layers.
"""
from __future__ import annotations

from dataclasses import dataclass
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
    report = parsed["report/report.json"]
    _check_registered_uint64(parsed)
    decoded_report = _decode_registered(report)
    _check_report(decoded_report)
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
