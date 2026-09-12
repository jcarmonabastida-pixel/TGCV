"""IT-G1 frozen case-evidence SHA-256 audit.

Governance boundary:
- GitHub is the canonical source for this script and all canonical evidence.
- This script is inspection-only; it never modifies evidence, manifests, Git state, or AWS.
- It must be executed only after synchronizing local main from origin/main.
- It audits the SHA-256 values recorded in the frozen manifest against the exact
  local working-tree bytes of the canonical evidence files.
- It does not repair, rewrite, or infer any expected hash.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST = REPO_ROOT / "00_GOVERNANCE/INDUSTRIAL_TRACK/execution/IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_EVIDENCE_MANIFEST_FROZEN_001.md"
OUT = REPO_ROOT / "03_EXPERIMENTS/IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_SHA_AUDIT_001.json"

HASH_RE = re.compile(r"`([0-9A-Fa-f]{64})`")
PATH_RE = re.compile(r"`(IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_[^`]+\.md)`")
CASE_RE = re.compile(r"\|\s*(CASE-\d{3})\s*\|(.+?)\|\s*([0-9A-Fa-f` ;]+)\s*\|")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    if not MANIFEST.exists():
        raise SystemExit(f"MANIFEST_MISSING={MANIFEST}")

    text = MANIFEST.read_text(encoding="utf-8")
    results = []
    current_case = None

    for line in text.splitlines():
        m = CASE_RE.match(line)
        if not m:
            continue
        case_id, evidence_cell, hashes_cell = m.groups()
        paths = PATH_RE.findall(evidence_cell)
        hashes = HASH_RE.findall(hashes_cell)
        if len(paths) != len(hashes):
            raise SystemExit(
                f"MANIFEST_SCHEMA_ERROR={case_id}: paths={len(paths)} hashes={len(hashes)}"
            )
        for path_text, expected in zip(paths, hashes):
            path = REPO_ROOT / "00_GOVERNANCE/INDUSTRIAL_TRACK/execution" / path_text
            actual = sha256(path) if path.exists() else None
            results.append(
                {
                    "case_id": case_id,
                    "path": path_text,
                    "expected_sha256": expected.upper(),
                    "actual_sha256": actual,
                    "status": "PASS" if actual == expected.upper() else "FAIL",
                    "exists": path.exists(),
                }
            )

    if not results:
        raise SystemExit("MANIFEST_SCHEMA_ERROR=NO_CASE_EVIDENCE_ROWS")

    failures = [r for r in results if r["status"] != "PASS"]
    unique_paths = sorted({r["path"] for r in results})
    output = {
        "audit": "IT-G1-CASE-EVIDENCE-SHA-AUDIT-001",
        "mode": "READ_ONLY_CANONICAL_WORKTREE_AUDIT",
        "manifest": str(MANIFEST.relative_to(REPO_ROOT)),
        "manifest_sha256": sha256(MANIFEST),
        "cases": len({r["case_id"] for r in results}),
        "evidence_references": len(results),
        "unique_evidence_files": len(unique_paths),
        "failures": len(failures),
        "status": "PASS" if not failures else "FAIL",
        "execution_authorization": "NONE",
        "aws_mutation": False,
        "results": results,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    sys.exit(main())
