#!/usr/bin/env python3
"""EXT-1.1 Rust — deterministic TR-131 executor v0.2.

Compatibility wrapper around the frozen v0.1 executor. The analytical
specification is unchanged. The only implementation change is strict
fail-closed detection of duplicate canonical T_acc transformations.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Iterable

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import tr131_executor_v01 as _v01


def canonical_tacc(rows: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:
    materialized = list(rows)
    ordered = sorted(materialized, key=lambda r: (r[0], r[1], r[2], r[3]))
    for previous, current in zip(ordered, ordered[1:]):
        if previous == current:
            raise ValueError(f"DUPLICATE_TACC_TRANSFORMATION:{current}")
    return tuple(ordered)


# Patch the frozen module's canonicalization symbol so every v0.1 analytical
# path (synthetic suite, loader, comparison, and hashing) uses strict v0.2
# duplicate handling. No B/T_acc definition or comparison rule is changed.
_v01.canonical_tacc = canonical_tacc


def canonical_sha256(tacc: Iterable[tuple[int, int, int, str]]) -> str:
    h = hashlib.sha256()
    for origin_id, target_pid, target_vid, target_version in canonical_tacc(tacc):
        h.update(f"{origin_id}|{target_pid}|{target_vid}|{target_version}\n".encode("utf-8"))
    return h.hexdigest()


_v01.canonical_sha256 = canonical_sha256


if __name__ == "__main__":
    raise SystemExit(_v01.main())
