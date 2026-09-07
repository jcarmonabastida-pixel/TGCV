#!/usr/bin/env python3
"""EXT-1.1 Rust — deterministic TR-131 executor v0.2.

This patch preserves the frozen DR-029 B/T_acc logic and changes only one
integrity behavior: duplicate canonical T_acc transformations now fail closed
instead of being silently collapsed.
"""
from __future__ import annotations

from pathlib import Path

OLD = Path(__file__).with_name("tr131_executor_v01.py")

# v0.2 is intentionally a minimal source-level integrity patch. It loads the
# frozen v0.1 implementation and replaces canonicalization with a strict
# duplicate-detecting implementation before exposing the same entry point.
source = OLD.read_text(encoding="utf-8")
old = '''def canonical_tacc(rows: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:\n    return tuple(sorted(set(rows), key=lambda r: (r[0], r[1], r[2], r[3])))\n'''
new = '''def canonical_tacc(rows: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:\n    materialized = list(rows)\n    ordered = sorted(materialized, key=lambda r: (r[0], r[1], r[2], r[3]))\n    for previous, current in zip(ordered, ordered[1:]):\n        if previous == current:\n            raise ValueError(f"DUPLICATE_TACC_TRANSFORMATION:{current}")\n    return tuple(ordered)\n'''
if old not in source:
    raise SystemExit("PATCH_TARGET_NOT_FOUND")
patched = source.replace(old, new, 1)
# Keep this file self-contained while preserving every frozen v0.1 function.
patched = patched.replace('deterministic TR-131 executor v0.1', 'deterministic TR-131 executor v0.2', 1)
patched = patched.replace('"""EXT-1.1 Rust — deterministic TR-131 executor v0.2.\n\nImplements DR-029 v0.2 only.', '"""EXT-1.1 Rust — deterministic TR-131 executor v0.2.\n\nImplements DR-029 v0.2 only.')
print(patched)
