"""Deterministic constructor for the TGCV Rust Ω-primary observational U_t.

This module is intentionally independent from historical EXT-1.1 identity
recovery and has no network/live-registry dependency.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Callable, Iterable, Mapping, Sequence


TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
CONSTRUCTION_VERSION = "RUST_OMEGA_U_CONSTRUCTOR_v0.1"


@dataclass(frozen=True)
class Candidate:
    tau: tuple[int, int, int]
    snapshot_time: str
    provenance: tuple[str, str]
    coverage_state: str
    resolution_status: str


def _canonical_tau(origin_version_id: int, target_package_id: int, target_version_id: int) -> tuple[int, int, int]:
    return (origin_version_id, target_package_id, target_version_id)


def _stable_payload(records: Sequence[Mapping[str, object]]) -> str:
    return json.dumps(list(records), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _output_hash(records: Sequence[Mapping[str, object]]) -> str:
    return sha256(_stable_payload(records).encode("utf-8")).hexdigest()


def build_u_t(
    versions: Iterable[Mapping[str, object]],
    dependencies: Iterable[Mapping[str, object]],
    *,
    cutoff: str,
    target_selector: Callable[
        [Mapping[str, object], Mapping[str, object], Sequence[Mapping[str, object]]],
        Iterable[Mapping[str, object]],
    ],
) -> dict[str, object]:
    """Build deterministic observational U_t from primitive structural records.

    target_selector must itself be frozen and outcome-blind. It receives only
    primitive source/dependency/version records whose created_at is <= cutoff.
    No resolver is embedded here so that target-release semantics cannot be
    silently changed by this constructor.
    """
    version_rows = [dict(row) for row in versions]
    dependency_rows = [dict(row) for row in dependencies]
    by_id: dict[int, Mapping[str, object]] = {}

    for idx, row in enumerate(version_rows):
        try:
            vid = int(row["id"])
            package_id = int(row["package_id"])
            version_str = str(row["version_str"])
            created_at = str(row["created_at"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"invalid package_versions row {idx}: {exc}") from exc
        if not created_at:
            continue
        if vid in by_id:
            raise ValueError(f"duplicate package version id: {vid}")
        by_id[vid] = {
            "id": vid,
            "package_id": package_id,
            "version_str": version_str,
            "created_at": created_at,
        }

    eligible_versions = [
        row for row in by_id.values() if str(row["created_at"]) <= cutoff
    ]
    eligible_by_package: dict[int, list[Mapping[str, object]]] = {}
    for row in eligible_versions:
        eligible_by_package.setdefault(int(row["package_id"]), []).append(row)
    for bucket in eligible_by_package.values():
        bucket.sort(key=lambda r: (str(r["created_at"]), int(r["id"]), str(r["version_str"])))

    seen: dict[tuple[int, int, int], Candidate] = {}
    unresolved = 0
    skipped_out_of_scope = 0

    for d_idx, dep in enumerate(dependency_rows):
        try:
            depending_version = int(dep["depending_version"])
            target_package = int(dep["depending_on_package"])
            str(dep["semver_str"])
        except (KeyError, TypeError, ValueError) as exc:
            unresolved += 1
            continue

        source = by_id.get(depending_version)
        if source is None or str(source["created_at"]) > cutoff:
            skipped_out_of_scope += 1
            continue

        targets = list(target_selector(source, dep, tuple(eligible_by_package.get(target_package, []))))
        for target in targets:
            try:
                target_id = int(target["id"])
                target_pkg = int(target["package_id"])
                target_time = str(target["created_at"])
            except (KeyError, TypeError, ValueError):
                unresolved += 1
                continue
            if target_pkg != target_package or target_time > cutoff:
                unresolved += 1
                continue
            tau = _canonical_tau(depending_version, target_package, target_id)
            cand = Candidate(
                tau=tau,
                snapshot_time=cutoff,
                provenance=(f"package_dependencies.csv:row:{d_idx}", f"package_versions.csv:id:{target_id}"),
                coverage_state="OBSERVED_PRESENT",
                resolution_status="RESOLVED",
            )
            previous = seen.get(tau)
            if previous is None or cand.provenance < previous.provenance:
                seen[tau] = cand

    records = [
        {
            "tau": list(candidate.tau),
            "snapshot_time": candidate.snapshot_time,
            "provenance": list(candidate.provenance),
            "coverage_state": candidate.coverage_state,
            "resolution_status": candidate.resolution_status,
            "construction_version": CONSTRUCTION_VERSION,
            "temporal_rule": TEMPORAL_RULE_ID,
        }
        for _, candidate in sorted(seen.items(), key=lambda item: item[0])
    ]

    return {
        "U_t": records,
        "u_count": len(records),
        "unresolved_count": unresolved,
        "skipped_out_of_scope_count": skipped_out_of_scope,
        "construction_version": CONSTRUCTION_VERSION,
        "temporal_rule": TEMPORAL_RULE_ID,
        "cutoff": cutoff,
        "output_sha256": _output_hash(records),
    }
