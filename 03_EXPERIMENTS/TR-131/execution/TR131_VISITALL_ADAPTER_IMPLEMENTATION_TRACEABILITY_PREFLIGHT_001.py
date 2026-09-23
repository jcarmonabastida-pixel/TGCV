#!/usr/bin/env python3
"""TR-131 VisitAll source-defined adapter implementation traceability preflight.

Integrity/precondition checks only. No scientific execution.
"""
from __future__ import annotations

import hashlib
import json
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ADAPTER = ROOT / "TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001.py"
LOCK = ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"

def load_adapter():
    spec = importlib.util.spec_from_file_location("tr131_visitall_adapter", ADAPTER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    adapter = load_adapter()
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    va = lock["visitall"]

    connected = {
        ("loc-x2-y2","loc-x1-y2"),
        ("loc-x2-y2","loc-x3-y2"),
        ("loc-x2-y2","loc-x2-y1"),
        ("loc-x2-y2","loc-x2-y3"),
        ("loc-x1-y2","loc-x0-y2"),
        ("loc-x1-y2","loc-x2-y2"),
        ("loc-x1-y2","loc-x1-y1"),
        ("loc-x1-y2","loc-x1-y3"),
        ("loc-x3-y2","loc-x2-y2"),
        ("loc-x3-y2","loc-x4-y2"),
        ("loc-x3-y2","loc-x3-y1"),
        ("loc-x3-y2","loc-x3-y3"),
    }

    s0 = {"at-robot":"loc-x2-y2", "visited":["loc-x2-y2"]}
    t0 = adapter.applicable_moves(s0, connected)

    expected_tacc = set(va["t_acc"]["transformations"])
    actual_tacc = {m.identity for m in t0}

    checks = {
        "source_revision": va["revision"] == "cf19edf7c53d1540ddbb396c642595e0926ee552",
        "source_blob": va["blob_sha"] == "f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34",
        "adapter_file_sha_present": len(sha256(ADAPTER)) == 64,
        "initial_state_matches_lock": s0["at-robot"] == va["initial_state"]["at_robot"],
        "tacc_cardinality": len(t0) == va["t_acc"]["cardinality"],
        "tacc_identity_match": actual_tacc == expected_tacc,
        "precondition_enforced": False,
        "effects_source_shape": False,
        "non_applicable_rejected": False,
        "no_scientific_execution": True,
    }

    successor = adapter.apply_move(
        s0, adapter.Move("loc-x2-y2","loc-x1-y2"), connected
    )
    checks["effects_source_shape"] = (
        successor["at-robot"] == "loc-x1-y2"
        and successor["visited"] == ["loc-x1-y2","loc-x2-y2"]
    )

    try:
        adapter.apply_move(
            s0, adapter.Move("loc-x2-y2","loc-x4-y4"), connected
        )
    except ValueError:
        checks["non_applicable_rejected"] = True

    try:
        adapter.apply_move(
            {"at-robot":"loc-x1-y2","visited":["loc-x2-y2"]},
            adapter.Move("loc-x2-y2","loc-x1-y2"),
            connected,
        )
    except ValueError:
        checks["precondition_enforced"] = True

    report = {
        "record_type":"TGCV_TR131_VISITALL_ADAPTER_IMPLEMENTATION_TRACEABILITY_PREFLIGHT",
        "status":"PASS" if all(checks.values()) else "BLOCKED",
        "scientific_execution_authorized":False,
        "scientific_execution_performed":False,
        "adapter_sha256":sha256(ADAPTER),
        "checks":checks,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
