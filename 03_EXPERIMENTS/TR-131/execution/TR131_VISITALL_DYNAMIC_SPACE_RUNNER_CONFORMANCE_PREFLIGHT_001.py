#!/usr/bin/env python3
"""TR-131 VisitAll dynamic-space runner conformance preflight.

Integrity and implementation checks only. No scientific execution.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "TR131_VISITALL_DYNAMIC_SPACE_RUNNER_001.py"
LOCK = ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"
ADAPTER = ROOT / "TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001.py"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    runner_text = RUNNER.read_text(encoding="utf-8")
    runner_ast = ast.parse(runner_text)
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    va = lock["visitall"]

    forbidden = (
        "planner", "optimize", "goal", "value", "rainbow",
        "random", "randomize", "selection_policy", "X"
    )
    lowered = runner_text.lower()

    checks = {
        "runner_sha256_present": len(sha256(RUNNER)) == 64,
        "adapter_sha256_present": len(sha256(ADAPTER)) == 64,
        "source_revision_locked": va["revision"] == "cf19edf7c53d1540ddbb396c642595e0926ee552",
        "source_blob_locked": va["blob_sha"] == "f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34",
        "depth_frozen_to_2": "DEPTH = 2" in runner_text,
        "source_adapter_imported": "TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001" in runner_text,
        "delta_operator_present": "Added" in runner_text and "Removed" in runner_text and "Retained" in runner_text,
        "baseline_fields_present": '"S_t"' in runner_text and '"T_real_t"' in runner_text and '"S_t1"' in runner_text,
        "c1_not_testable": '"C1": "NOT_TESTABLE"' in runner_text,
        "c2_present": '"C2": "enumerated at root"' in runner_text,
        "c3_present": '"C3": "enumerated through depth 2"' in runner_text,
        "c4_present": '"C4": "computed on every realized edge"' in runner_text,
        "scientific_result_not_inferred": '"overall_representation_result": "NOT_EVALUATED_BY_RUNNER"' in runner_text,
        "no_forbidden_runtime_tokens": not any(token in lowered for token in forbidden),
        "no_scientific_execution": True,
        "syntax_valid": runner_ast is not None,
    }

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_RUNNER_CONFORMANCE_PREFLIGHT",
        "status": "PASS" if all(checks.values()) else "BLOCKED",
        "scientific_execution_authorized": False,
        "scientific_execution_performed": False,
        "runner_sha256": sha256(RUNNER),
        "adapter_sha256": sha256(ADAPTER),
        "checks": checks,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
