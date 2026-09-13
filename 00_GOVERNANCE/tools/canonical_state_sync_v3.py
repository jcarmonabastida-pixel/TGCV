#!/usr/bin/env python3
"""TGCV Canonical State Sync v3.1.

Read-only transition resolution and manifest generation.  The engine treats the
versioned evidence matrix as the authoritative matrix target and CURRENT as a
projection.  It never writes governance state in this version.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GOV = ROOT / "00_GOVERNANCE"
VERSIONED_MATRIX = GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.5.md"
CURRENT_MATRIX = GOV / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
CURRENT_POINTER = GOV / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md"
CANONICAL = GOV / "CANONICAL_STATE.json"
RMA = GOV / "rma" / "TGCV_RMA_current.md"
TRACE = GOV / "rma" / "TGCV_RMA_traceability_current.csv"
STATUS = ROOT / "STATUS.md"
FILES = [CANONICAL, CURRENT_MATRIX, CURRENT_POINTER, VERSIONED_MATRIX, RMA, TRACE, STATUS]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True,
        encoding="utf-8", errors="replace"
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def heads(text: str) -> list[str]:
    return [line.lstrip("#").strip() for line in text.splitlines() if line.startswith("#")]


def columns(text: str) -> list[str]:
    for line in text.splitlines():
        if line.startswith("| ID") or line.startswith("|ID"):
            return [item.strip() for item in line.strip("|").split("|")]
    return []


def claims(text: str) -> list[str]:
    return [line.split("|")[1].strip() for line in text.splitlines() if line.startswith("| C") and "|" in line]


def evidence_sections(text: str) -> set[str]:
    return {h for h in heads(text) if "evidence" in h.lower()}


def audit_transition(predecessor: str, successor: str, current: str, target_version: str) -> list[str]:
    errors: list[str] = []
    predecessor_lines = predecessor.splitlines()
    successor_lines = successor.splitlines()

    if len(successor_lines) < len(predecessor_lines):
        errors.append("SUCCESSOR_MATRIX_SHRINKS_IN_LINES")
    if not set(claims(predecessor)) <= set(claims(successor)):
        errors.append("SUCCESSOR_LOSES_CLAIMS")
    if columns(predecessor) != columns(successor):
        errors.append("SUCCESSOR_COLUMNS_CHANGED")
    if not evidence_sections(predecessor) <= evidence_sections(successor):
        errors.append("SUCCESSOR_LOSES_EVIDENCE_SECTIONS")
    required_boundaries = {
        "Claim boundary", "Current methodological routing",
        "Current scientific position", "Gate state", "Interpretation boundary"
    }
    if not required_boundaries <= set(heads(successor)):
        errors.append("SUCCESSOR_LOSES_GOVERNANCE_BOUNDARIES")
    if f"**Predecessor:** {target_version.replace('v1.5', 'v1.4')}" not in successor:
        errors.append("SUCCESSOR_PREDECESSOR_METADATA_INVALID")
    if "FOS C09" not in successor:
        errors.append("FOS_C09_MISSING")

    # The target projection must be exactly the versioned target, not an edited copy.
    if current != successor:
        errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
    if target_version not in read(CURRENT_POINTER):
        errors.append("CURRENT_POINTER_NOT_TARGET_VERSION")
    if target_version not in read(CANONICAL):
        errors.append("CANONICAL_STATE_NOT_TARGET_VERSION")

    return errors


def build_target_state() -> dict[str, bytes]:
    """Construct the deterministic read-only target for the current v1.5 repair."""
    if not VERSIONED_MATRIX.exists():
        raise RuntimeError("TARGET_MATRIX_MISSING")

    target_matrix = VERSIONED_MATRIX.read_bytes()
    target_pointer = CURRENT_POINTER.read_text(encoding="utf-8")
    target_canonical = CANONICAL.read_text(encoding="utf-8")
    target_status = STATUS.read_text(encoding="utf-8")

    # CURRENT is a pure projection of the versioned matrix.
    return {
        rel(CURRENT_MATRIX): target_matrix,
        rel(CURRENT_POINTER): target_pointer.encode("utf-8"),
        rel(CANONICAL): target_canonical.encode("utf-8"),
        rel(STATUS): target_status.encode("utf-8"),
        rel(VERSIONED_MATRIX): target_matrix,
        rel(RMA): RMA.read_bytes(),
        rel(TRACE): TRACE.read_bytes(),
    }


def snapshot() -> dict[str, dict[str, int | str | None]]:
    result = {}
    for path in FILES:
        result[rel(path)] = {
            "sha256": sha(path) if path.exists() else None,
            "bytes": path.stat().st_size if path.exists() else None,
        }
    return result


def resolve_manifest(matrix_version: str, source_commit: str) -> dict:
    if matrix_version != "v1.5":
        return {"status": "BLOCKED_VALIDATION", "errors": ["UNSUPPORTED_TARGET_VERSION"]}

    head = git("rev-parse", "HEAD")
    source = git("rev-parse", f"{source_commit}^{{commit}}")
    target = build_target_state()

    predecessor_path = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_v1.4.md"
    predecessor = read(predecessor_path)
    successor = target[rel(VERSIONED_MATRIX)].decode("utf-8")
    current = target[rel(CURRENT_MATRIX)].decode("utf-8")
    errors = audit_transition(predecessor, successor, current, matrix_version)

    files = []
    for path in FILES:
        name = rel(path)
        current_bytes = path.read_bytes() if path.exists() else None
        target_bytes = target[name]
        files.append({
            "path": name,
            "predecessor_sha256": sha_bytes(current_bytes) if current_bytes is not None else None,
            "target_sha256": sha_bytes(target_bytes),
            "target_source": "deterministically_built_projection" if name != rel(VERSIONED_MATRIX) else "versioned_canonical_matrix",
            "changed": current_bytes != target_bytes,
            "authorized": True,
        })

    return {
        "manifest_version": "1.1",
        "engine_version": "v3.1",
        "status": "PREPARED_NOT_APPLIED" if not errors else "BLOCKED_VALIDATION",
        "transition": "RECONCILE_MATRIX_CURRENT_TO_VERSIONED_CANONICAL",
        "target_matrix_version": matrix_version,
        "source_commit": source,
        "source_commit_verified": source == head,
        "source_of_truth": rel(CANONICAL),
        "projections": ["RMA", "MATRIX", "STATUS"],
        "validation": [
            "MONOTONIC_EVIDENCE", "CROSS_REFERENCE", "VERSION_POINTER",
            "STATUS", "CURRENT_EQUALS_VERSIONED_TARGET", "NO_UNAUTHORIZED_LOSS"
        ],
        "write_order": ["BUILD", "VALIDATE", "WRITE", "RE_READ", "VERIFY"],
        "remote_policy": "COMMIT_PUSH_REMOTE_VERIFY",
        "allowed_paths": [rel(path) for path in FILES],
        "files": files,
        "validation_result": {"ok": not errors, "errors": errors},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    sub.add_parser("verify")
    plan = sub.add_parser("plan")
    plan.add_argument("--matrix-version", default="v1.5")
    plan.add_argument("--source-commit", default="HEAD")
    manifest = sub.add_parser("manifest")
    manifest.add_argument("--matrix-version", default="v1.5")
    manifest.add_argument("--source-commit", default="HEAD")
    manifest.add_argument("--output")
    apply = sub.add_parser("apply")
    apply.add_argument("--transition-manifest", required=True)
    publish = sub.add_parser("publish")
    publish.add_argument("--transition-manifest", required=True)

    args = parser.parse_args()
    before = snapshot()

    if args.command in {"manifest", "plan"}:
        manifest_data = resolve_manifest(args.matrix_version, args.source_commit)
        if args.command == "manifest":
            output = json.dumps(manifest_data, ensure_ascii=False, indent=2)
            print(output)
            if args.output:
                Path(args.output).write_text(output + "\n", encoding="utf-8")
            print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
            print("MANIFEST_RESULT=" + ("PREPARED_READ_ONLY" if manifest_data.get("validation_result", {}).get("ok") else "BLOCKED_READ_ONLY"))
            return 0 if manifest_data.get("validation_result", {}).get("ok") else 2

        print("TGCV CANONICAL STATE SYNC")
        print("MODE=PLAN")
        print("ENGINE_VERSION=v3.1")
        print("TRANSITION=RECONCILE_MATRIX_CURRENT_TO_VERSIONED_CANONICAL")
        print("SOURCE_COMMIT=" + manifest_data.get("source_commit", ""))
        print("VALIDATION_RESULT=" + ("PASS" if manifest_data.get("validation_result", {}).get("ok") else "BLOCKED"))
        print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
        return 0 if manifest_data.get("validation_result", {}).get("ok") else 2

    if args.command in {"check", "verify"}:
        target = build_target_state()
        predecessor = read(GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.4.md")
        successor = target[rel(VERSIONED_MATRIX)].decode("utf-8")
        current_actual = read(CURRENT_MATRIX)
        errors = audit_transition(predecessor, successor, current_actual, "v1.5")
        print("TGCV CANONICAL STATE SYNC")
        print("MODE=" + args.command.upper())
        print("ENGINE_VERSION=v3.1")
        print("AUDIT_RESULT=" + ("PASS" if not errors else "BLOCKED"))
        print("ERRORS=" + json.dumps(errors, ensure_ascii=False))
        print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
        return 0 if not errors and before == snapshot() else 2

    print("RESULT=FAIL_CLOSED")
    print("REASON=V3_1_WRITE_PATH_NOT_ENABLED")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
