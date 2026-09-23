#!/usr/bin/env python3
"""TR-131 VisitAll Dynamic Transformation Space package freeze/integrity audit.

Audit only. No scientific execution.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FILES = {
    "construction_spec": ROOT / "TR131_VISITALL_DYNAMIC_SPACE_PACKAGE_CONSTRUCTION_SPEC_001.md",
    "adapter": ROOT / "TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001.py",
    "adapter_preflight": ROOT / "TR131_VISITALL_ADAPTER_IMPLEMENTATION_TRACEABILITY_PREFLIGHT_001.py",
    "runner": ROOT / "TR131_VISITALL_DYNAMIC_SPACE_RUNNER_001.py",
    "runner_preflight": ROOT / "TR131_VISITALL_DYNAMIC_SPACE_RUNNER_CONFORMANCE_PREFLIGHT_001.py",
    "executor2": ROOT / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.py",
    "executor2_preflight": ROOT / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_PREFLIGHT_001.py",
    "source_lock": ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    missing = [name for name, path in FILES.items() if not path.exists()]
    if missing:
        raise SystemExit("MISSING_FILES: " + ",".join(missing))

    lock = json.loads(FILES["source_lock"].read_text(encoding="utf-8"))
    va = lock["visitall"]

    checks = {
        "all_required_files_present": not missing,
        "source_revision_pinned": va["revision"] == "cf19edf7c53d1540ddbb396c642595e0926ee552",
        "source_problem_pinned": va["problem"] == "grid-5",
        "source_blob_pinned": va["blob_sha"] == "f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34",
        "construction_depth_2": "depth-2" in FILES["construction_spec"].read_text(encoding="utf-8"),
        "construction_no_rainbow": "Rainbow is excluded" in FILES["construction_spec"].read_text(encoding="utf-8"),
        "adapter_preflight_pass_recorded": "PASS" in FILES["adapter_preflight"].read_text(encoding="utf-8"),
        "runner_preflight_pass_recorded": "PASS" in FILES["runner_preflight"].read_text(encoding="utf-8"),
        "executor2_preflight_pass_recorded": "PASS" in FILES["executor2_preflight"].read_text(encoding="utf-8"),
        "runner_no_x_policy": "selection_policy" not in FILES["runner"].read_text(encoding="utf-8"),
        "executor2_no_executor1_reference": "EXECUTOR_1" not in FILES["executor2"].read_text(encoding="utf-8"),
        "scientific_execution_not_authorized": all(
            '"scientific_execution_authorized": False' in FILES[name].read_text(encoding="utf-8")
            for name in ("runner", "executor2")
        ),
    }

    manifest = {
        name: {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
        }
        for name, path in FILES.items()
    }

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_PACKAGE_FREEZE_INTEGRITY_AUDIT",
        "status": "PASS" if all(checks.values()) else "BLOCKED",
        "package_frozen": all(checks.values()),
        "scientific_execution_authorized": False,
        "scientific_execution_performed": False,
        "checks": checks,
        "manifest": manifest,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
