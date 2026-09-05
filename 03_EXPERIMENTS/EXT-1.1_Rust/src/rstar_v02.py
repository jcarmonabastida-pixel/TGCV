"""EXT-1.1 Rust restricted resolver R* v0.2.

Operates only on the retained Rust dataset schema. It is deliberately not a
historical Cargo resolver. Unsupported requirement syntax fails closed.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, order=True)
class SemVer:
    major: int
    minor: int
    patch: int

    @classmethod
    def parse(cls, value: str) -> "SemVer":
        m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", value.strip())
        if not m:
            raise ValueError(f"UNSUPPORTED_VERSION:{value}")
        return cls(*(int(x) for x in m.groups()))


def requirement_kind(req: str) -> str:
    req = req.strip()
    if re.fullmatch(r"=\d+\.\d+\.\d+", req):
        return "EXACT"
    if re.fullmatch(r"\^\d+(?:\.\d+){1,2}", req):
        return "CARET"
    if re.fullmatch(r"\d+\.\d+\.\d+", req):
        return "CARET"
    return "UNSUPPORTED"


def satisfies(version: str, req: str) -> bool:
    kind = requirement_kind(req)
    if kind == "UNSUPPORTED":
        raise ValueError(f"UNSUPPORTED_REQUIREMENT:{req}")
    v = SemVer.parse(version)
    raw = req.strip()
    base = SemVer.parse(raw[1:] if raw.startswith("^") or raw.startswith("=") else raw)
    if kind == "EXACT":
        return v == base
    if base.major > 0:
        upper = SemVer(base.major + 1, 0, 0)
    elif base.minor > 0:
        upper = SemVer(0, base.minor + 1, 0)
    else:
        upper = SemVer(0, 0, base.patch + 1)
    return base <= v < upper


def eligible_versions(
    target_versions: Iterable[tuple[int, str, str]],
    origin_created_at: str,
    req: str,
) -> tuple[list[tuple[int, str, str]], str | None]:
    """Return temporally eligible candidates and an exclusion reason."""
    if requirement_kind(req) == "UNSUPPORTED":
        return [], "UNSUPPORTED"
    candidates = []
    seen = set()
    for version_id, version_str, created_at in target_versions:
        if version_id in seen:
            raise ValueError(f"DUPLICATE_VERSION_ID:{version_id}")
        seen.add(version_id)
        if created_at <= origin_created_at and satisfies(version_str, req):
            candidates.append((version_id, version_str, created_at))
    return candidates, None if candidates else "NO_ELIGIBLE_CANDIDATE"


def select_max(candidates: Iterable[tuple[int, str, str]]):
    rows = list(candidates)
    if not rows:
        return None
    ordered = sorted(rows, key=lambda r: (SemVer.parse(r[1]), r[0]))
    return ordered[-1]


def resolve_edge(
    origin_id: int,
    origin_name: str,
    origin_created_at: str,
    target_package_id: int,
    target_name: str,
    requirement: str,
    target_versions: Iterable[tuple[int, str, str]],
) -> dict:
    candidates, exclusion = eligible_versions(target_versions, origin_created_at, requirement)
    selected = select_max(candidates)
    return {
        "origin_version_id": origin_id,
        "origin_name": origin_name,
        "target_package_id": target_package_id,
        "target_name": target_name,
        "constraint": requirement,
        "candidate_count": len(candidates),
        "selected_version_id": selected[0] if selected else None,
        "selected_version": selected[1] if selected else None,
        "origin_created_at": origin_created_at,
        "selected_created_at": selected[2] if selected else None,
        "exclusion_reason": exclusion if selected is None else None,
    }
