#!/usr/bin/env python3
"""TR-131 VisitAll Executor-2 reconstruction persistence wrapper.

Captures the independent Executor-2 reconstruction stdout verbatim and
persists its byte hash. The reconstruction itself remains responsible for
scientific authorization and execution semantics.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXECUTOR2 = ROOT / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.py"
OUTPUT_DIR = ROOT / "results"
OUTPUT = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"
META = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.sha256"

FROZEN_EXECUTOR2_SHA256 = "e4aff5ea034ae316ae43b8d7dda93b58cdecf7d6032293d17c1d3d15b103ca49"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    actual = sha256(EXECUTOR2)
    if actual != FROZEN_EXECUTOR2_SHA256:
        raise SystemExit(
            "FROZEN_EXECUTOR2_HASH_MISMATCH: "
            + actual + " != " + FROZEN_EXECUTOR2_SHA256
        )
    OUTPUT_DIR.mkdir(exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(EXECUTOR2)],
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
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RUN_PERSISTENCE",
        "status": "PERSISTED",
        "output": str(OUTPUT.relative_to(ROOT)),
        "captured_stdout_sha256": digest,
        "wrapper_exit_code": result.returncode,
        "executor2_sha256": actual,
    }, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
