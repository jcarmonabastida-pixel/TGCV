#!/usr/bin/env python3
"""TR-131 VisitAll Executor-2 reconstruction preflight.

Checks implementation and independence constraints only. No reconstruction run.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXECUTOR2 = ROOT / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.py"
LOCK = ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    text = EXECUTOR2.read_text(encoding="utf-8")
    tree = ast.parse(text)

    imports = []
    calls = []
    literals = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            literals.append(node.value)

    checks = {
        "syntax_valid": True,
        "executor2_sha256_present": len(sha256(EXECUTOR2)) == 64,
        "source_lock_referenced": "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json" in literals,
        "depth_frozen_to_2": "DEPTH = 2" in text,
        "source_adapter_referenced": "TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001" in text,
        "tacc_reconstructed": "applicable_moves" in text and "def tacc" in text,
        "delta_reconstructed": "def delta_tacc" in text,
        "baseline_reconstructed": '"baseline"' in text,
        "independence_declared": '"independent": True' in text,
        "no_executor1_reference": "EXECUTOR_1" not in text and "EXECUTOR-1" not in text,
        "no_result_file_reference": "RESULT" not in text and "result.json" not in text.lower(),
        "no_random_import": "random" not in imports,
        "no_planner_import": "planner" not in imports,
        "authorization_gate_present": "TGCV_TR131_SCIENTIFIC_AUTHORIZED" in text and "return 3" in text,
        "authorized_flags_consistent": '"scientific_execution_authorized": authorized' in text and '"scientific_execution_performed": True' in text,
        "no_scientific_authorization": '"scientific_execution_authorized": False' in text,
        "no_scientific_execution": '"scientific_execution_performed": False' in text,
    }

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_PREFLIGHT",
        "status": "PASS" if all(checks.values()) else "BLOCKED",
        "executor": "EXECUTOR_2",
        "scientific_execution_authorized": False,
        "scientific_execution_performed": False,
        "executor2_sha256": sha256(EXECUTOR2),
        "checks": checks,
    }
    import json
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
