"""Adapter from historical crates.io index records to EXT-1.1 structures.

The adapter is intentionally format-focused: it parses one crates.io index
JSON record at a time and never consults current APIs or outcome data.
"""
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class VersionRecord:
    package: str
    version: str
    yanked: bool
    dependencies: tuple[tuple[str, str, bool, str | None], ...]
    checksum: str | None


def parse_record(package: str, record: dict[str, Any], cutoff: str | None = None) -> VersionRecord:
    version = record["vers"]
    deps = []
    for dep in record.get("deps", []):
        deps.append(
            (
                dep["name"],
                dep["req"],
                bool(dep.get("optional", False)),
                dep.get("kind"),
            )
        )
    return VersionRecord(
        package=package,
        version=version,
        yanked=bool(record.get("yanked", False)),
        dependencies=tuple(deps),
        checksum=record.get("cksum"),
    )


def parse_records(package: str, records: list[dict[str, Any]]) -> list[VersionRecord]:
    """Parse historical records preserving source order and identity."""
    parsed = [parse_record(package, r) for r in records]
    identities = [(r.package, r.version) for r in parsed]
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate canonical package/version identity")
    return parsed
