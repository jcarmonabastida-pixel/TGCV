#!/usr/bin/env python3
"""Deterministic, snapshot-only SemVer candidate-universe replay scaffold.

This tool intentionally does NOT consult crates.io, downloads, current index state,
or outcome data. It consumes only a local newline-delimited crates.io index snapshot
and emits candidate releases satisfying a declared requirement.

It is a gate-support tool, not a claim that Cargo's full resolver has been reproduced.
Full resolver equivalence requires a pinned Cargo version and an executable historical
registry environment; that remains an explicit empirical step in HRSV.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


def parse_version(v: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(?:-[0-9A-Za-z.-]+)?", v)
    if not m:
        raise ValueError(f"Unsupported version syntax: {v}")
    return tuple(map(int, m.groups()))


def satisfies_caret(version: tuple[int, int, int], req: tuple[int, int, int]) -> bool:
    # Cargo caret compatibility: for major > 0, upper bound is next major;
    # for 0.y.z, upper bound is next minor when y > 0; for 0.0.z, next patch.
    if req[0] > 0:
        upper = (req[0] + 1, 0, 0)
    elif req[1] > 0:
        upper = (0, req[1] + 1, 0)
    else:
        upper = (0, 0, req[2] + 1)
    return version >= req and version < upper


def iter_records(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}") from exc


def candidates(path: Path, package: str, requirement: str) -> list[str]:
    if not requirement.startswith("^"):
        raise ValueError("v0.1 supports caret requirements only")
    req = parse_version(requirement[1:])
    out: list[str] = []
    for rec in iter_records(path):
        if rec.get("name") != package or rec.get("yanked", False):
            continue
        version = parse_version(rec["vers"])
        if satisfies_caret(version, req):
            out.append(rec["vers"])
    return sorted(out, key=parse_version)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("snapshot_file", type=Path)
    ap.add_argument("package")
    ap.add_argument("requirement")
    args = ap.parse_args()
    result = {
        "snapshot_file": str(args.snapshot_file),
        "package": args.package,
        "requirement": args.requirement,
        "candidate_versions": candidates(args.snapshot_file, args.package, args.requirement),
        "source_policy": "local_snapshot_only",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
