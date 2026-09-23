#!/usr/bin/env python3
"""TR-131 VisitAll run-output persistence wrapper.

Execution wrapper only. It captures the runner's exact JSON stdout without
modifying the scientific payload or authorizing execution.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "TR131_VISITALL_DYNAMIC_SPACE_RUNNER_001.py"
OUTPUT_DIR = ROOT / "results"
OUTPUT = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
META = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.sha256"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(RUNNER)],
        cwd=str(ROOT),
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.decode("utf-8", errors="replace"))
        return result.returncode

    raw = result.stdout
    payload = json.loads(raw.decode("utf-8"))

    if payload.get("scientific_execution_authorized") is not True:
        raise RuntimeError("SCIENTIFIC_EXECUTION_NOT_AUTHORIZED")

    if payload.get("scientific_execution_performed") is not True:
        raise RuntimeError("SCIENTIFIC_EXECUTION_NOT_PERFORMED")

    digest = hashlib.sha256(raw).hexdigest()
    OUTPUT.write_bytes(raw)
    META.write_text(digest + "  " + OUTPUT.name + "\n", encoding="utf-8")

    print(json.dumps({
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_PERSISTENCE",
        "status": "PERSISTED",
        "output": str(OUTPUT.relative_to(ROOT)),
        "captured_stdout_sha256": digest,
        "wrapper_exit_code": result.returncode,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
