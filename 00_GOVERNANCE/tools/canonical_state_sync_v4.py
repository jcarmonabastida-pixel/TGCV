#!/usr/bin/env python3
"""TGCV canonical-state sync v4.

Discovers the highest versioned Evidence-to-Claim Matrix and makes
EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md an exact byte-for-byte copy.
It never invents, edits, deletes, or downgrades evidentiary content.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_DIR = ROOT
CURRENT = MATRIX_DIR / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
PATTERN = re.compile(r"^EVIDENCE_TO_CLAIM_MATRIX_v(\d+(?:\.\d+)?)\.md$")


def version_key(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def discover() -> tuple[Path, str]:
    candidates = []
    for p in MATRIX_DIR.glob("EVIDENCE_TO_CLAIM_MATRIX_v*.md"):
        m = PATTERN.match(p.name)
        if m:
            candidates.append((version_key(m.group(1)), p, m.group(1)))
    if not candidates:
        raise SystemExit("ERROR: no versioned Evidence-to-Claim Matrix found")
    _, path, version = max(candidates, key=lambda x: x[0])
    return path, version


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sync", action="store_true")
    args = ap.parse_args()
    if not args.check and not args.sync:
        args.check = True

    source, version = discover()
    source_bytes = source.read_bytes()
    current_bytes = CURRENT.read_bytes() if CURRENT.exists() else None

    if args.check:
        if current_bytes != source_bytes:
            print(f"MISMATCH: CURRENT != {source.name}")
            return 1
        print(f"PASS: CURRENT is byte-identical to {source.name}")
        return 0

    if current_bytes == source_bytes:
        print(f"PASS: CURRENT already synchronized to {source.name}")
        return 0

    CURRENT.write_bytes(source_bytes)
    print(f"SYNCED: CURRENT <- {source.name} (v{version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
