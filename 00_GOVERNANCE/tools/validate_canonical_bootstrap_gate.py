#!/usr/bin/env python3
"""TGCV canonical bootstrap gate.

Read-only integration gate for session continuity. It validates the canonical
current-state contract first and then validates the ChatGPT bootstrap against
that same local checkout. It never writes governance artifacts.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRENT_VALIDATOR = ROOT / "00_GOVERNANCE" / "tools" / "validate_current_state.py"
BOOTSTRAP_VALIDATOR = ROOT / "00_GOVERNANCE" / "tools" / "validate_chatgpt_bootstrap.py"


def run_validator(path: Path) -> tuple[int, str]:
    if not path.is_file():
        return 2, f"MISSING_VALIDATOR:{path.relative_to(ROOT).as_posix()}"
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def main() -> int:
    current_rc, current_out = run_validator(CURRENT_VALIDATOR)
    bootstrap_rc, bootstrap_out = run_validator(BOOTSTRAP_VALIDATOR)

    print("TGCV CANONICAL BOOTSTRAP GATE")
    print("MODE=READ_ONLY")
    print("CURRENT_STATE_VALIDATOR=" + ("PASS" if current_rc == 0 else "FAIL"))
    print("BOOTSTRAP_VALIDATOR=" + ("PASS" if bootstrap_rc == 0 else "FAIL"))
    print("CANONICAL_ENTRYPOINT=" + ("PASS" if current_rc == 0 and bootstrap_rc == 0 else "BLOCKED"))

    if current_rc != 0:
        print("--- CURRENT_STATE_VALIDATOR_OUTPUT ---")
        print(current_out)
    if bootstrap_rc != 0:
        print("--- BOOTSTRAP_VALIDATOR_OUTPUT ---")
        print(bootstrap_out)

    if current_rc == 0 and bootstrap_rc == 0:
        print("RESULT=PASS")
        print("FAIL_CLOSED=TRUE")
        print("GOVERNANCE_FILES_WRITTEN=FALSE")
        return 0

    print("RESULT=BLOCKED")
    print("FAIL_CLOSED=TRUE")
    print("GOVERNANCE_FILES_WRITTEN=FALSE")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
