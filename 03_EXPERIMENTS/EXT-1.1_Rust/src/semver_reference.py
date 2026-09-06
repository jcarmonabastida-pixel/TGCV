"""Minimal deterministic SemVer predicate used for EXT-1.1 fixtures.

This is intentionally a reference implementation, not a replacement for the
Rust/Cargo resolver. It implements exactly the restricted requirement grammar
frozen by R* v0.2. It is a fixture/test helper only; the normative resolver is
rstar_v02.py.
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
    if re.fullmatch(r"=\d+\.\d+\.\d+", req):
        return v == Version.parse(req[1:])
    if re.fullmatch(r"\^\d+(?:\.\d+){1,2}", req):
        base = Version.parse(req[1:])
        if base.major > 0:
            upper = Version(base.major + 1, 0, 0)
        elif base.minor > 0:
            upper = Version(0, base.minor + 1, 0)
        else:
            upper = Version(0, 0, base.patch + 1)
        return v >= base and v < upper
    if re.fullmatch(r"\d+\.\d+\.\d+", req):
        base = Version.parse(req)
        if base.major > 0:
            upper = Version(base.major + 1, 0, 0)
        elif base.minor > 0:
            upper = Version(0, base.minor + 1, 0)
        else:
            upper = Version(0, 0, base.patch + 1)
        return v >= base and v < upper
    raise ValueError(f"unsupported requirement: {requirement}")


def accessible_versions(versions, requirement):
    return {v for v in versions if satisfies(v, requirement)}
