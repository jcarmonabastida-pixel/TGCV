#!/usr/bin/env python3
"""IT-METH-I FAA AMOC Blind Executor-2 control harness v0.4.

DRY-RUN CONTROL ONLY.

Verifies declared-input integrity, output separation, control sequencing and
seal capability. It does NOT claim filesystem isolation or executor
independence; those require an external execution boundary and governance
assignment respectively.
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


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


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
    hits: list[str] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace").upper()
    except OSError:
        return hits
    for term in FORBIDDEN_TERMS:
        if term in text:
            hits.append(term)
    return hits


def symlink_paths(root: Path) -> list[str]:
    if not root.exists() or not root.is_dir():
        return []
    return [str(p) for p in sorted(root.rglob("*")) if p.is_symlink()]


def read_declared_manifest(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("declared evidence manifest must be a non-empty JSON list")
    out: list[dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            raise ValueError("manifest entries must contain exactly path and sha256")
        p = resolved(Path(item["path"]))
        digest = str(item["sha256"]).lower()
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError(f"invalid sha256 for {p}")
        out.append({"path": str(p), "sha256": digest})
    if len({e["path"] for e in out}) != len(out):
        raise ValueError("duplicate manifest path")
    return sorted(out, key=lambda x: x["path"])


def verify_manifest(entries: list[dict[str, str]], evidence: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for entry in entries:
        p = resolved(Path(entry["path"]))
        if p.is_symlink() or not p.is_file():
            errors.append(f"manifest file unavailable or symlinked: {p}")
            continue
        if not is_within(p, evidence):
            errors.append(f"manifest path outside evidence root: {p}")
            continue
        if sha256_file(p) != entry["sha256"]:
            errors.append(f"manifest hash mismatch: {p}")
    return not errors, errors


def dependency_inventory() -> list[str]:
    return sorted(
        f"{d.metadata['Name']}=={d.version}"
        for d in importlib.metadata.distributions()
        if d.metadata.get("Name")
    )


def control(args: argparse.Namespace) -> dict:
    package = resolved(args.package)
    evidence = resolved(args.evidence)
    output = resolved(args.output)
    manifest_path = resolved(args.evidence_manifest)
    sequence = [{"event": "control_start", "timestamp_utc": now()}]

    result: dict[str, object] = {
        "PACKAGE_ID": PACKAGE_ID,
        "CASE_ID": CASE_ID,
        "EXECUTION_MODE": "DRY_RUN_CONTROL",
        "CONTROL_SEQUENCE": sequence,
        "CONTROL_TIMESTAMP_UTC": sequence[0]["timestamp_utc"],
    }

    package_hash = sha256_file(package) if package.is_file() and not package.is_symlink() else None
    result["PACKAGE_SHA256_OBSERVED"] = package_hash
    result["PACKAGE_INTEGRITY"] = "PASS" if package_hash == args.expected_package_sha256.lower() else "FAIL"
    result["PACKAGE_METADATA_ROLE"] = "OBSERVED_PACKAGE_METADATA_ONLY"
    result["PACKAGE_METADATA"] = {"path": str(package), "sha256": package_hash}

    try:
        declared = read_declared_manifest(manifest_path)
        manifest_ok, manifest_errors = verify_manifest(declared, evidence)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        declared, manifest_ok, manifest_errors = [], False, [f"manifest validation error: {exc}"]
    result["DECLARED_EVIDENCE_MANIFEST"] = declared
    result["EVIDENCE_MANIFEST_STATUS"] = "PASS" if manifest_ok else "FAIL"
    result["EVIDENCE_MANIFEST_ERRORS"] = manifest_errors

    evidence_symlinks = symlink_paths(evidence)
    package_hits = scan_declared_file(package) if package.is_file() else []
    evidence_hits = [
        {"path": e["path"], "terms": scan_declared_file(Path(e["path"]))}
        for e in declared
        if scan_declared_file(Path(e["path"]))
    ]
    result["CONTENT_SCAN_SUPPLEMENTARY"] = {"package": package_hits, "evidence": evidence_hits}
    result["DECLARED_EVIDENCE_BOUNDARY_STATUS"] = "PASS" if manifest_ok and not evidence_symlinks else "FAIL"
    result["DECLARED_EVIDENCE_BOUNDARY_BASIS"] = "externally supplied frozen manifest + hash verification + symlink rejection"
    result["RUNTIME_FILESYSTEM_ISOLATION_STATUS"] = "NOT_VERIFIED"
    result["RECONSTRUCTION_001_ACCESS_STATUS"] = "NOT_VERIFIED"
    result["RECONSTRUCTION_001_ACCESS_EVIDENCE"] = "No filesystem isolation claim is made by this harness."

    output_preexisting_symlink = output.is_symlink()
    result["OUTPUT_BOUNDARY_STATUS"] = (
        "PASS"
        if not output_preexisting_symlink and roots_disjoint(output, package) and roots_disjoint(output, evidence)
        else "FAIL"
    )
    output_before = str(output)
    output.mkdir(parents=True, exist_ok=True)
    result["OUTPUT_PATH_IDENTITY_STATUS"] = "PASS" if resolved(output) == output else "FAIL"
    result["OUTPUT_PATH_IDENTITY"] = output_before

    sequence.append({"event": "preseal_control", "timestamp_utc": now()})
    probe = output / ".it_meth_i_seal_capability_probe.tmp"
    probe_hash = None
    try:
        probe.write_text("IT-METH-I SEAL CAPABILITY PROBE\nPACKAGE_ID=" + PACKAGE_ID + "\n", encoding="utf-8")
        probe_hash = sha256_file(probe)
        seal_ok = len(probe_hash) == 64
    except OSError:
        seal_ok = False
    finally:
        if probe.exists():
            probe.unlink()
    sequence.append({"event": "seal_capability_probe_complete", "timestamp_utc": now()})
    result["SEAL_MECHANISM_CAPABILITY_STATUS"] = "PASS" if seal_ok else "FAIL"
    result["SEAL_MECHANISM_CAPABILITY_PROBE_SHA256"] = probe_hash
    result["ACTUAL_RECONSTRUCTION_SEAL_STATUS"] = "NOT_EXECUTED"

    sequence_ok = all(sequence[i]["timestamp_utc"] <= sequence[i + 1]["timestamp_utc"] for i in range(len(sequence) - 1))
    result["CONTROL_SEQUENCE_STATUS"] = "PASS" if sequence_ok else "FAIL"
    result["TEMPORAL_ORDERING_STATUS"] = result["CONTROL_SEQUENCE_STATUS"]

    config = {
        "package": str(package),
        "evidence_root": str(evidence),
        "output": str(output),
        "manifest": str(manifest_path),
        "mode": args.mode,
    }
    config_text = json.dumps(config, sort_keys=True).upper()
    config_hits = [t for t in FORBIDDEN_TERMS if t in config_text]
    manifest_path_hits = [t for t in FORBIDDEN_TERMS if any(t in e["path"].upper() for e in declared)]
    result["COMPARISON_TARGET_DECLARATION_STATUS"] = "PASS" if not config_hits and not manifest_path_hits else "FAIL"
    result["COMPARISON_TARGET_VERIFICATION_BASIS"] = {
        "configuration_scan": config_hits,
        "manifest_path_scan": manifest_path_hits,
        "scope": "declared control inputs only; not global filesystem isolation",
    }
    result["COMPARISON_PRESEAL_STATUS"] = result["COMPARISON_TARGET_DECLARATION_STATUS"]

    result["ENVIRONMENT_FINGERPRINT"] = {
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "script_sha256": sha256_file(Path(__file__).resolve()),
        "local_dependency_inventory": dependency_inventory(),
        "dependency_inventory_role": "OBSERVATIONAL_HOST_METADATA_ONLY",
    }

    technical = [
        result["PACKAGE_INTEGRITY"] == "PASS",
        result["EVIDENCE_MANIFEST_STATUS"] == "PASS",
        result["DECLARED_EVIDENCE_BOUNDARY_STATUS"] == "PASS",
        result["OUTPUT_BOUNDARY_STATUS"] == "PASS",
        result["OUTPUT_PATH_IDENTITY_STATUS"] == "PASS",
        result["SEAL_MECHANISM_CAPABILITY_STATUS"] == "PASS",
        result["CONTROL_SEQUENCE_STATUS"] == "PASS",
        result["COMPARISON_TARGET_DECLARATION_STATUS"] == "PASS",
    ]
    result["OVERALL_CONTROL_STATUS"] = "PASS" if all(technical) else "BLOCKED"
    result["EXECUTOR_2_DISTINCT"] = "NOT_ESTABLISHED"
    result["GOVERNANCE_AUTHORIZATION_STATUS"] = "NOT_AUTHORIZED"
    result["INDEPENDENCE_STATUS"] = "NOT_DEMONSTRATED"
    result["RECONSTRUCTION_002_STATUS"] = "NOT_EXECUTED"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="IT-METH-I blind executor control harness")
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--evidence-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-package-sha256", required=True)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--mode", choices=("DRY_RUN_CONTROL", "EXECUTION"), default="DRY_RUN_CONTROL")
    args = parser.parse_args()
    if args.mode != "DRY_RUN_CONTROL":
        print("BLOCKED: EXECUTION mode is not implemented/authorized by v0.4.")
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
