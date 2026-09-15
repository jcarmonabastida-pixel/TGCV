#!/usr/bin/env python3
"""Validate the TGCV Evidence-to-Claim Matrix publication chain.

Read-only validator. It never changes governance artifacts.
The publication invariant is:
  versioned matrix == CURRENT == pointer version == CANONICAL_STATE claim_matrix
and the current version must preserve all material evidence section headings
from its immediate predecessor.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
POINTER = ROOT / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md"
STATE = ROOT / "CANONICAL_STATE.json"
PATTERN = re.compile(r"^EVIDENCE_TO_CLAIM_MATRIX_v(\d+(?:\.\d+)?)\.md$")
VERSION_RE = re.compile(r"Current v(\d+(?:\.\d+)?)")
MATERIAL_HEADING_RE = re.compile(r"^#{1,6} .*Material .*evidence.*$", re.I)


def version_key(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def discover() -> list[tuple[str, Path]]:
    out = []
    for path in ROOT.glob("EVIDENCE_TO_CLAIM_MATRIX_v*.md"):
        match = PATTERN.match(path.name)
        if match:
            out.append((match.group(1), path))
    return sorted(out, key=lambda item: version_key(item[0]))


def material_headings(text: str) -> set[str]:
    return {line.strip() for line in text.splitlines() if MATERIAL_HEADING_RE.match(line.strip())}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    versions = discover()
    if not versions:
        fail("no versioned Evidence-to-Claim Matrix found")

    version, source = versions[-1]
    source_bytes = source.read_bytes()
    if not CURRENT.exists():
        fail("CURRENT matrix is missing")
    if CURRENT.read_bytes() != source_bytes:
        fail(f"CURRENT is not byte-identical to {source.name}")

    current_text = source.read_text(encoding="utf-8")
    header = VERSION_RE.search(current_text[:1000])
    if not header or header.group(1) != version:
        fail(f"matrix header version does not match {source.name}")

    if not POINTER.exists():
        fail("CURRENT_POINTER is missing")
    pointer = POINTER.read_text(encoding="utf-8")
    if f"**Current version:** v{version}" not in pointer:
        fail(f"CURRENT_POINTER does not identify v{version}")
    if f"EVIDENCE_TO_CLAIM_MATRIX_v{version}.md" not in pointer:
        fail(f"CURRENT_POINTER does not identify the v{version} artifact")

    if not STATE.exists():
        fail("CANONICAL_STATE.json is missing")
    try:
        state = json.loads(STATE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"CANONICAL_STATE.json is invalid JSON: {exc}")
    actual = state.get("current_versions", {}).get("claim_matrix")
    if actual != f"v{version}":
        fail(f"CANONICAL_STATE claim_matrix={actual!r}; expected v{version}")

    if len(versions) >= 2:
        previous_version, previous = versions[-2]
        previous_headings = material_headings(previous.read_text(encoding="utf-8"))
        missing = sorted(previous_headings - material_headings(current_text))
        if missing:
            fail(
                "current matrix does not preserve predecessor material-evidence headings: "
                + "; ".join(missing)
            )
        print(f"PASS: predecessor v{previous_version} material-evidence headings preserved")

    print(f"PASS: publication chain coherent at v{version}")
    print(f"PASS: {source.name} == CURRENT")
    print("PASS: CURRENT_POINTER == current version")
    print("PASS: CANONICAL_STATE.claim_matrix == current version")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
