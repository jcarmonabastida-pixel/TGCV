"""Minimal deterministic SemVer predicate used for EXT-1.1 fixtures.

This is intentionally a reference implementation, not a replacement for the
Rust/Cargo resolver. It supports the operators needed to validate the frozen
set semantics before wiring the historical index.
"""
import re
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int = 0
    patch: int = 0

    @classmethod
    def parse(cls, value: str):
        m = re.fullmatch(r"(\d+)\.(\d+)(?:\.(\d+))?", value.strip())
        if not m:
            raise ValueError(f"unsupported version: {value}")
        return cls(int(m.group(1)), int(m.group(2)), int(m.group(3) or 0))


def satisfies(version: str, requirement: str) -> bool:
    v = Version.parse(version)
    req = requirement.strip()
    if req == "*":
        return True
    if req.startswith("^"):
        base = Version.parse(req[1:])
        if base.major > 0:
            upper = Version(base.major + 1, 0, 0)
        elif base.minor > 0:
            upper = Version(0, base.minor + 1, 0)
        else:
            upper = Version(0, 0, base.patch + 1)
        return v >= base and v < upper
    if req.startswith(">="):
        return v >= Version.parse(req[2:])
    if req.startswith(">"):
        return v > Version.parse(req[1:])
    if req.startswith("<="):
        return v <= Version.parse(req[2:])
    if req.startswith("<"):
        return v < Version.parse(req[1:])
    return v == Version.parse(req)


def accessible_versions(versions, requirement):
    return {v for v in versions if satisfies(v, requirement)}
