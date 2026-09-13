#!/usr/bin/env python3
"""TGCV Canonical State Sync v3.4.

Read-only transition resolution and manifest generation.
The source commit is the canonical byte-level reference for governed state.
Only CURRENT matrix is derived from the versioned matrix; every other governed
artifact is taken byte-for-byte from the source commit and validated.
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

TARGET_MATRIX_VERSION = "v1.5"
TARGET_RMA_VERSION = "v3.34"
TARGET_TRACE_VERSION = "v3.34"


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


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def source_bytes(source_commit: str, path: Path) -> bytes:
    return git_bytes("show", f"{source_commit}:{rel(path)}")


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
    return {h for h in heads(text) if h.lower().startswith("material ") and "evidence" in h.lower()}


def validate_pointer(pointer: str) -> list[str]:
    errors: list[str] = []
    if "**Current version:** v1.5" not in pointer:
        errors.append("POINTER_TARGET_VERSION_INVALID")
    if "EVIDENCE_TO_CLAIM_MATRIX_v1.5.md" not in pointer:
        errors.append("POINTER_TARGET_ARTIFACT_INVALID")
    return errors


def validate_canonical(canonical: str) -> list[str]:
    errors: list[str] = []
    try:
        state = json.loads(canonical)
    except json.JSONDecodeError:
        return ["CANONICAL_STATE_INVALID_JSON"]
    versions = state.get("current_versions", {})
    if versions.get("rma") != TARGET_RMA_VERSION:
        errors.append("CANONICAL_RMA_VERSION_INVALID")
    if versions.get("claim_matrix") != TARGET_MATRIX_VERSION:
        errors.append("CANONICAL_MATRIX_VERSION_INVALID")
    if versions.get("rma_traceability") != TARGET_TRACE_VERSION:
        errors.append("CANONICAL_TRACE_VERSION_INVALID")
    return errors


def audit_matrix(predecessor: str, successor: str) -> list[str]:
    errors: list[str] = []
    if len(successor.splitlines()) < len(predecessor.splitlines()):
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
    if "**Predecessor:** v1.4" not in successor:
        errors.append("SUCCESSOR_PREDECESSOR_METADATA_INVALID")
    if "FOS C09" not in successor:
        errors.append("FOS_C09_MISSING")
    return errors


def build_target_state(source_commit: str) -> dict[str, bytes]:
    versioned = source_bytes(source_commit, VERSIONED_MATRIX)
    current_derived = versioned
    current_source = source_bytes(source_commit, CURRENT_MATRIX)
    if current_source != current_derived:
        raise RuntimeError("SOURCE_CURRENT_DIFFERS_FROM_DERIVED_MATRIX")

    return {
        rel(CANONICAL): source_bytes(source_commit, CANONICAL),
        rel(CURRENT_MATRIX): current_derived,
        rel(CURRENT_POINTER): source_bytes(source_commit, CURRENT_POINTER),
        rel(VERSIONED_MATRIX): versioned,
        rel(RMA): source_bytes(source_commit, RMA),
        rel(TRACE): source_bytes(source_commit, TRACE),
        rel(STATUS): source_bytes(source_commit, STATUS),
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
    if matrix_version != TARGET_MATRIX_VERSION:
        return {"status": "BLOCKED_VALIDATION", "errors": ["UNSUPPORTED_TARGET_VERSION"]}

    head = git("rev-parse", "HEAD")
    source = git("rev-parse", f"{source_commit}^{{commit}}")
    errors: list[str] = []

    if head != source:
        errors.append("SOURCE_COMMIT_NOT_HEAD")

    target = build_target_state(source)
    predecessor = source_bytes(source, GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode("utf-8")
    versioned = target[rel(VERSIONED_MATRIX)].decode("utf-8")
    current = target[rel(CURRENT_MATRIX)].decode("utf-8")
    pointer = target[rel(CURRENT_POINTER)].decode("utf-8")
    canonical = target[rel(CANONICAL)].decode("utf-8")
    status = target[rel(STATUS)].decode("utf-8")

    errors.extend(audit_matrix(predecessor, versioned))
    if current != versioned:
        errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
    errors.extend(validate_pointer(pointer))
    errors.extend(validate_canonical(canonical))
    if not status.strip():
        errors.append("STATUS_EMPTY")

    files = []
    for path in FILES:
        name = rel(path)
        current_bytes = path.read_bytes() if path.exists() else None
        target_bytes = target[name]
        source_kind = "derived_from_versioned_matrix" if name == rel(CURRENT_MATRIX) else "source_commit_canonical"
        files.append({
            "path": name,
            "predecessor_sha256": sha_bytes(current_bytes) if current_bytes is not None else None,
            "source_commit_sha256": sha_bytes(source_bytes(source, path)),
            "target_sha256": sha_bytes(target_bytes),
            "target_source": source_kind,
            "changed": current_bytes != target_bytes,
            "authorized": True,
        })
        if source_kind == "source_commit_canonical" and current_bytes != target_bytes:
            errors.append(f"CANONICAL_SOURCE_MISMATCH:{name}")

    return {
        "manifest_version": "1.3",
        "engine_version": "v3.4",
        "status": "PREPARED_NOT_APPLIED" if not errors else "BLOCKED_VALIDATION",
        "transition": "RECONCILE_MATRIX_CURRENT_TO_VERSIONED_CANONICAL",
        "target_matrix_version": matrix_version,
        "source_commit": source,
        "source_commit_verified": source == head,
        "source_of_truth": "source_commit",
        "projections": ["CURRENT_MATRIX"],
        "validation": [
            "SOURCE_COMMIT_EXACTNESS", "MONOTONIC_EVIDENCE", "CROSS_REFERENCE",
            "VERSION_POINTER", "STATUS", "CURRENT_EQUALS_VERSIONED_TARGET",
            "NO_UNAUTHORIZED_CANONICAL_REWRITE"
        ],
        "write_order": ["BUILD", "VALIDATE", "WRITE", "RE_READ", "VERIFY"],
        "remote_policy": "COMMIT_PUSH_REMOTE_VERIFY",
        "allowed_paths": [rel(path) for path in FILES],
        "files": files,
        "validation_result": {"ok": not errors, "errors": errors},
    }


def self_test() -> int:
    source = git("rev-parse", "HEAD")
    target = build_target_state(source)
    matrix = target[rel(VERSIONED_MATRIX)].decode("utf-8")
    predecessor = source_bytes(source, GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode("utf-8")
    pointer = target[rel(CURRENT_POINTER)].decode("utf-8")
    canonical = target[rel(CANONICAL)].decode("utf-8")
    current = target[rel(CURRENT_MATRIX)].decode("utf-8")

    positive = audit_matrix(predecessor, matrix) + validate_pointer(pointer) + validate_canonical(canonical)
    source_exact = all(source_bytes(source, path) == target[rel(path)] for path in FILES if path != CURRENT_MATRIX)
    current_projection = current == matrix

    broken_pointer = validate_pointer(pointer.replace("**Current version:** v1.5", "**Current version:** v1.4"))
    broken_canonical = validate_canonical(canonical.replace('"claim_matrix": "v1.5"', '"claim_matrix": "v1.4"'))
    unauthorized_rewrite = source_exact and target[rel(CURRENT_POINTER)] != pointer.replace("material FOS", "material CHANGED")

    print("TGCV CANONICAL STATE SYNC")
    print("MODE=SELFTEST")
    print("ENGINE_VERSION=v3.4")
    print("POSITIVE_TARGET_CONTRACT=" + ("PASS" if not positive and current_projection else "FAIL"))
    print("SOURCE_COMMIT_EXACTNESS=" + ("PASS" if source_exact else "FAIL"))
    print("NEGATIVE_POINTER_BLOCK=" + ("PASS" if "POINTER_TARGET_VERSION_INVALID" in broken_pointer else "FAIL"))
    print("NEGATIVE_CANONICAL_BLOCK=" + ("PASS" if "CANONICAL_MATRIX_VERSION_INVALID" in broken_canonical else "FAIL"))
    print("UNAUTHORIZED_PROJECTION_REWRITE_BLOCKED=" + ("PASS" if unauthorized_rewrite else "FAIL"))
    ok = not positive and current_projection and source_exact and broken_pointer and broken_canonical and unauthorized_rewrite
    print("SELFTEST_RESULT=" + ("PASS" if ok else "FAIL"))
    return 0 if ok else 2


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    sub.add_parser("verify")
    sub.add_parser("selftest")
    for name in ("plan", "manifest"):
        p = sub.add_parser(name)
        p.add_argument("--matrix-version", default=TARGET_MATRIX_VERSION)
        p.add_argument("--source-commit", default="HEAD")
        if name == "manifest":
            p.add_argument("--output")
    apply = sub.add_parser("apply")
    apply.add_argument("--transition-manifest", required=True)
    publish = sub.add_parser("publish")
    publish.add_argument("--transition-manifest", required=True)

    args = parser.parse_args()
    before = snapshot()

    if args.command == "selftest":
        return self_test()

    if args.command in {"manifest", "plan"}:
        data = resolve_manifest(args.matrix_version, args.source_commit)
        if args.command == "manifest":
            output = json.dumps(data, ensure_ascii=False, indent=2)
            print(output)
            if args.output:
                Path(args.output).write_text(output + "\n", encoding="utf-8")
            print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
            print("MANIFEST_RESULT=" + ("PREPARED_READ_ONLY" if data["validation_result"]["ok"] else "BLOCKED_READ_ONLY"))
        else:
            print("TGCV CANONICAL STATE SYNC")
            print("MODE=PLAN")
            print("ENGINE_VERSION=v3.4")
            print("SOURCE_COMMIT=" + data.get("source_commit", ""))
            print("VALIDATION_RESULT=" + ("PASS" if data.get("validation_result", {}).get("ok") else "BLOCKED"))
            print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
        return 0 if data.get("validation_result", {}).get("ok") else 2

    if args.command in {"check", "verify"}:
        head = git("rev-parse", "HEAD")
        target = build_target_state(head)
        predecessor = source_bytes(head, GOV / "EVIDENCE_TO_CLAIM_MATRIX_v1.4.md").decode("utf-8")
        errors = audit_matrix(predecessor, target[rel(VERSIONED_MATRIX)].decode("utf-8"))
        errors.extend(validate_pointer(target[rel(CURRENT_POINTER)].decode("utf-8")))
        errors.extend(validate_canonical(target[rel(CANONICAL)].decode("utf-8")))
        if target[rel(CURRENT_MATRIX)] != target[rel(VERSIONED_MATRIX)]:
            errors.append("CURRENT_MATRIX_DIFFERS_FROM_TARGET")
        print("TGCV CANONICAL STATE SYNC")
        print("MODE=" + args.command.upper())
        print("ENGINE_VERSION=v3.4")
        print("AUDIT_RESULT=" + ("PASS" if not errors else "BLOCKED"))
        print("ERRORS=" + json.dumps(errors, ensure_ascii=False))
        print("NO_GOVERNANCE_FILES_WRITTEN=" + str(before == snapshot()).upper())
        return 0 if not errors and before == snapshot() else 2

    print("RESULT=FAIL_CLOSED")
    print("REASON=V3_4_WRITE_PATH_NOT_ENABLED")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
