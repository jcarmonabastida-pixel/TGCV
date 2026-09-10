#!/usr/bin/env python3
"""IT-METH-I FAA AMOC Blind Executor-2 control harness v0.3.

DRY-RUN CONTROL ONLY.

The harness verifies technical boundary, provenance, sequencing and sealing
controls for a proposed blind execution context. It does not perform
reconstruction 002 and cannot establish executor independence by itself.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ID = "IT-METH-I-AMOC-BLIND-EXEC-001"
CASE_ID = "IT-G1-I-AMOC-US-91-12-10-7K0-18-00734"
FORBIDDEN_TERMS = (
    "RECONSTRUCTION_001",
    "IT-G4_I_FAA_AMOC_UTILITY_EXECUTION_RESULT_001",
    "IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_001",
    "COMPARISON",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def iter_files(root: Path):
    if not root.exists() or not root.is_dir():
        return
    for p in sorted(root.rglob("*")):
        if p.is_file() and not p.is_symlink():
            yield p


def resolved(path: Path) -> Path:
    return path.resolve(strict=False)


def is_within(path: Path, root: Path) -> bool:
    try:
        resolved(path).relative_to(resolved(root))
        return True
    except ValueError:
        return False


def roots_disjoint(a: Path, b: Path) -> bool:
    return not is_within(a, b) and not is_within(b, a)


def scan_declared_file(path: Path) -> list[str]:
    """Supplementary content scan; absence of hits is not proof of isolation."""
    hits: list[str] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace").upper()
    except (OSError, UnicodeError):
        return hits
    for term in FORBIDDEN_TERMS:
        if term in text:
            hits.append(term)
    return hits


def symlink_paths(root: Path) -> list[str]:
    if not root.exists() or not root.is_dir():
        return []
    return [str(p) for p in sorted(root.rglob("*")) if p.is_symlink()]


def exact_manifest(path: Path) -> dict[str, str]:
    return {"path": str(resolved(path)), "sha256": sha256_file(path)}


def evidence_manifest(root: Path) -> list[dict[str, str]]:
    return [exact_manifest(p) for p in iter_files(root)]


def local_dependency_inventory() -> list[str]:
    return sorted(
        f"{d.metadata['Name']}=={d.version}"
        for d in importlib.metadata.distributions()
        if d.metadata.get("Name")
    )


def read_declared_manifest(path: Path) -> list[dict[str, str]]:
    """Read an externally supplied frozen evidence manifest.

    Required shape: JSON list of objects with absolute/resolveable 'path' and
    64-hex 'sha256'. This is a declaration supplied by the custodian; the
    harness does not manufacture a frozen manifest and then validate itself.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("declared evidence manifest must be a non-empty JSON list")
    normalised: list[dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            raise ValueError("manifest entries must contain exactly path and sha256")
        p = resolved(Path(item["path"]))
        digest = str(item["sha256"]).lower()
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError(f"invalid sha256 for {p}")
        normalised.append({"path": str(p), "sha256": digest})
    return sorted(normalised, key=lambda x: x["path"])


def verify_declared_manifest(entries: list[dict[str, str]], evidence_root: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        p = resolved(Path(entry["path"]))
        if str(p) in seen:
            errors.append(f"duplicate manifest path: {p}")
        seen.add(str(p))
        if not p.is_file() or p.is_symlink():
            errors.append(f"manifest file unavailable or symlinked: {p}")
            continue
        if not is_within(p, evidence_root):
            errors.append(f"manifest path outside evidence root: {p}")
            continue
        observed = sha256_file(p)
        if observed != entry["sha256"]:
            errors.append(f"manifest hash mismatch: {p}")
    return not errors, errors


def control(args: argparse.Namespace) -> dict:
    package = resolved(args.package)
    evidence = resolved(args.evidence)
    output = resolved(args.output)
    declared_manifest_path = resolved(args.evidence_manifest)

    checks: dict[str, object] = {
        "PACKAGE_ID": PACKAGE_ID,
        "CASE_ID": CASE_ID,
        "EXECUTION_MODE": "DRY_RUN_CONTROL",
        "CONTROL_SEQUENCE": [],
        "CONTROL_TIMESTAMP_UTC": utc_now(),
    }
    checks["CONTROL_SEQUENCE"].append({"event": "control_start", "timestamp_utc": utc_now()})

    # H1: package integrity is mandatory and compared with an externally
    # supplied frozen digest.
    package_hash = sha256_file(package) if package.is_file() else None
    checks["PACKAGE_SHA256_OBSERVED"] = package_hash
    checks["PACKAGE_INTEGRITY"] = (
        "PASS"
        if package.is_file() and package_hash == args.expected_package_sha256.lower()
        else "FAIL"
    )

    # H7: package provenance is the exact package file, never its containing
    # directory. The frozen evidence boundary is independently manifested.
    checks["PACKAGE_MANIFEST_ENTRY"] = exact_manifest(package) if package.is_file() else None
    try:
        declared = read_declared_manifest(declared_manifest_path)
        manifest_valid, manifest_errors = verify_declared_manifest(declared, evidence)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        declared = []
        manifest_valid = False
        manifest_errors = [f"manifest read/validation error: {exc}"]
    checks["DECLARED_EVIDENCE_MANIFEST"] = declared
    checks["EVIDENCE_MANIFEST_STATUS"] = "PASS" if manifest_valid else "FAIL"
    checks["EVIDENCE_MANIFEST_ERRORS"] = manifest_errors

    # H2: boundary control is based on an explicit declared-root/manifest
    # model. Filename/content scans are supplementary only.
    evidence_symlinks = symlink_paths(evidence)
    package_forbidden = scan_declared_file(package) if package.is_file() else []
    evidence_forbidden: list[dict[str, object]] = []
    for entry in declared:
        p = Path(entry["path"])
        hits = scan_declared_file(p) if p.is_file() else []
        if hits:
            evidence_forbidden.append({"path": str(p), "terms": hits})
    checks["CONTENT_SCAN_SUPPLEMENTARY"] = {
        "package": package_forbidden,
        "evidence": evidence_forbidden,
    }
    checks["RECONSTRUCTION_001_ACCESS_STATUS"] = (
        "PASS" if manifest_valid and not evidence_symlinks else "FAIL"
    )
    checks["RECONSTRUCTION_001_ACCESS_EVIDENCE"] = {
        "boundary_basis": "declared evidence manifest + symlink rejection",
        "supplementary_forbidden_term_hits": evidence_forbidden,
    }

    # H3: output must be disjoint from package and evidence boundaries in both
    # directions; an output child of an input root is therefore rejected.
    checks["OUTPUT_BOUNDARY_STATUS"] = (
        "PASS"
        if roots_disjoint(output, package) and roots_disjoint(output, evidence)
        else "FAIL"
    )

    checks["DECLARED_INPUT_BOUNDARY"] = {
        "package_root": str(package),
        "evidence_root": str(evidence),
        "manifest_root": str(declared_manifest_path),
        "output_root": str(output),
        "model": "exact package file + externally frozen evidence manifest",
    }
    checks["INPUT_BOUNDARY_STATUS"] = (
        "PASS"
        if package.is_file()
        and evidence.is_dir()
        and declared_manifest_path.is_file()
        and manifest_valid
        and roots_disjoint(output, package)
        and roots_disjoint(output, evidence)
        else "FAIL"
    )

    # H4: this is explicitly a capability probe, not an actual execution seal.
    seal_probe = output / ".it_meth_i_seal_capability_probe.tmp"
    seal_hash = None
    seal_capability = "FAIL"
    try:
        output.mkdir(parents=True, exist_ok=True)
        seal_probe.write_text(
            "IT-METH-I DRY-RUN SEAL CAPABILITY PROBE\nPACKAGE_ID=" + PACKAGE_ID + "\n",
            encoding="utf-8",
        )
        seal_hash = sha256_file(seal_probe)
        seal_capability = "PASS" if len(seal_hash) == 64 else "FAIL"
    finally:
        if seal_probe.exists():
            seal_probe.unlink()
    checks["SEAL_MECHANISM_CAPABILITY_STATUS"] = seal_capability
    checks["SEAL_MECHANISM_CAPABILITY_PROBE_SHA256"] = seal_hash
    checks["ACTUAL_RECONSTRUCTION_SEAL_STATUS"] = "NOT_EXECUTED"

    # H5: derive sequence status from observed event timestamps, rather than a
    # hard-coded PASS. The dry-run sequence ends at capability verification.
    checks["CONTROL_SEQUENCE"].append({"event": "preseal_check", "timestamp_utc": utc_now()})
    checks["CONTROL_SEQUENCE"].append({"event": "seal_capability_probe_complete", "timestamp_utc": utc_now()})
    sequence = checks["CONTROL_SEQUENCE"]
    checks["TEMPORAL_SEQUENCE_STATUS"] = (
        "PASS"
        if all(sequence[i]["timestamp_utc"] <= sequence[i + 1]["timestamp_utc"] for i in range(len(sequence) - 1))
        else "FAIL"
    )
    checks["TEMPORAL_ORDERING_STATUS"] = checks["TEMPORAL_SEQUENCE_STATUS"]

    # H6: verify that no comparison material is present in the declared
    # configuration/manifest. No comparison target is ever loaded by v0.3.
    config_text = json.dumps(
        {
            "package": str(package),
            "evidence_root": str(evidence),
            "output": str(output),
            "manifest": str(declared_manifest_path),
            "mode": args.mode,
        },
        sort_keys=True,
    ).upper()
    comparison_terms = [term for term in FORBIDDEN_TERMS if term in config_text]
    manifest_path_terms = [
        term for term in FORBIDDEN_TERMS if any(term in e["path"].upper() for e in declared)
    ]
    comparison_verified = not comparison_terms and not manifest_path_terms
    checks["COMPARISON_PRESEAL_STATUS"] = "PASS" if comparison_verified else "FAIL"
    checks["COMPARISON_TARGET_CONFIGURED"] = False
    checks["COMPARISON_TARGET_VERIFICATION_BASIS"] = {
        "configuration_scan": "PASS" if not comparison_terms else "FAIL",
        "manifest_path_scan": "PASS" if not manifest_path_terms else "FAIL",
        "target_loaded": False,
    }

    checks["ENVIRONMENT_FINGERPRINT"] = {
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "script_sha256": sha256_file(Path(__file__).resolve()),
        "local_dependency_inventory": local_dependency_inventory(),
        "dependency_inventory_role": "OBSERVATIONAL_HOST_METADATA_ONLY",
    }

    technical = [
        checks["PACKAGE_INTEGRITY"] == "PASS",
        checks["EVIDENCE_MANIFEST_STATUS"] == "PASS",
        checks["RECONSTRUCTION_001_ACCESS_STATUS"] == "PASS",
        checks["INPUT_BOUNDARY_STATUS"] == "PASS",
        checks["OUTPUT_BOUNDARY_STATUS"] == "PASS",
        checks["SEAL_MECHANISM_CAPABILITY_STATUS"] == "PASS",
        checks["TEMPORAL_SEQUENCE_STATUS"] == "PASS",
        checks["COMPARISON_PRESEAL_STATUS"] == "PASS",
    ]
    checks["OVERALL_CONTROL_STATUS"] = "PASS" if all(technical) else "BLOCKED"

    # Non-promotable governance fields.
    checks["EXECUTOR_2_DISTINCT"] = "NOT_ESTABLISHED"
    checks["GOVERNANCE_AUTHORIZATION_STATUS"] = "NOT_AUTHORIZED"
    checks["INDEPENDENCE_STATUS"] = "NOT_DEMONSTRATED"
    checks["RECONSTRUCTION_002_STATUS"] = "NOT_EXECUTED"
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="IT-METH-I blind executor control harness")
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--evidence-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-package-sha256", required=True)
    parser.add_argument("--result", type=Path)
    parser.add_argument(
        "--mode",
        choices=("DRY_RUN_CONTROL", "EXECUTION"),
        default="DRY_RUN_CONTROL",
    )
    args = parser.parse_args()

    if args.mode != "DRY_RUN_CONTROL":
        print("BLOCKED: EXECUTION mode is not implemented/authorized by v0.3.")
        return 2

    result = control(args)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    print(payload, end="")

    if args.result:
        args.result.parent.mkdir(parents=True, exist_ok=True)
        args.result.write_text(payload, encoding="utf-8")

    return 0 if result["OVERALL_CONTROL_STATUS"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
