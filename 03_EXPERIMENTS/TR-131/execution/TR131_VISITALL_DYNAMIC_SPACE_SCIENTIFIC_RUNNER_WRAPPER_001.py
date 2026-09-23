#!/usr/bin/env python3
"""TR-131 VisitAll scientific-run persistence wrapper.

Runs the frozen Executor-1 runner and persists its exact JSON stdout locally.
This wrapper does not alter experiment semantics or authorize execution.
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "TR131_VISITALL_DYNAMIC_SPACE_RUNNER_001.py"
OUTPUT_DIR = ROOT / "results"
OUTPUT = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
META = OUTPUT_DIR / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.sha256"


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


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
    digest = sha256_bytes(raw)

    # Validate JSON before persistence.
    import json
    payload = json.loads(raw.decode("utf-8"))
    payload["execution_persistence"] = {
        "wrapper": "TR131_VISITALL_DYNAMIC_SPACE_SCIENTIFIC_RUNNER_WRAPPER_001.py",
        "captured_stdout_sha256": digest,
        "persisted_at_utc": datetime.now(timezone.utc).isoformat(),
    }

    # Persist the exact runner payload plus deterministic persistence metadata.
    OUTPUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "
",
        encoding="utf-8",
    )
    META.write_text(digest + "  " + OUTPUT.name + "
", encoding="utf-8")

    print(json.dumps({
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_PERSISTENCE",
        "status": "PERSISTED",
        "scientific_execution_performed": payload.get("scientific_execution_performed"),
        "output": str(OUTPUT.relative_to(ROOT)),
        "captured_stdout_sha256": digest,
        "wrapper_exit_code": result.returncode,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
