"""Deterministic constructor for the TGCV Rust Ω-primary observational U_t.
Independent from historical EXT-1.1 identity recovery and live registries.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Iterable, Mapping, Sequence

TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
CONSTRUCTION_VERSION = "RUST_OMEGA_U_CONSTRUCTOR_v0.5"
COVERAGE_STATES = ("OBSERVED_PRESENT", "OBSERVED_ABSENT_COMPLETE", "UNKNOWN_MISSING", "OUT_OF_SCOPE")

@dataclass(frozen=True)
class Candidate:
    tau: tuple[int, int, int]
    snapshot_time: str
    provenance: tuple[str, str, str]
    coverage_state: str
    resolution_status: str

def _canonical_tau(origin_version_id: int, target_package_id: int, target_version_id: int) -> tuple[int, int, int]:
    return (origin_version_id, target_package_id, target_version_id)

def _stable_payload(records: Sequence[Mapping[str, object]]) -> str:
    return json.dumps(list(records), ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def _output_hash(records: Sequence[Mapping[str, object]]) -> str:
    return sha256(_stable_payload(records).encode("utf-8")).hexdigest()

def _adjacent_target(source: Mapping[str, object], targets: Sequence[Mapping[str, object]], cutoff: str) -> Mapping[str, object] | None:
    source_time = str(source["created_at"])
    later = [t for t in targets if str(t["created_at"]) > source_time and str(t["created_at"]) <= cutoff]
    if not later:
        return None
    return min(later, key=lambda r: (str(r["created_at"]), int(r["id"]), str(r["version_str"])))

def build_u_t(versions: Iterable[Mapping[str, object]], dependencies: Iterable[Mapping[str, object]], *, cutoff: str, complete_target_packages: Iterable[int] = ()) -> dict[str, object]:
    version_rows = [dict(row) for row in versions]
    dependency_rows = dependencies
    by_id: dict[int, Mapping[str, object]] = {}
    for idx, row in enumerate(version_rows):
        try:
            vid, package_id = int(row["id"]), int(row["package_id"])
            version_str, created_at = str(row["version_str"]), str(row["created_at"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"invalid package_versions row {idx}: {exc}") from exc
        if not created_at:
            raise ValueError(f"missing created_at at row {idx}")
        if vid in by_id:
            raise ValueError(f"duplicate package version id: {vid}")
        by_id[vid] = {"id": vid, "package_id": package_id, "version_str": version_str, "created_at": created_at}
    eligible = [r for r in by_id.values() if str(r["created_at"]) <= cutoff]
    by_pkg: dict[int, list[Mapping[str, object]]] = {}
    for r in eligible:
        by_pkg.setdefault(int(r["package_id"]), []).append(r)
    for b in by_pkg.values():
        b.sort(key=lambda r: (str(r["created_at"]), int(r["id"]), str(r["version_str"])))
    seen: dict[tuple[int,int,int], Candidate] = {}
    coverage_counts = {state: 0 for state in COVERAGE_STATES}
    complete_targets = {int(x) for x in complete_target_packages}
    unresolved = 0
    for d_idx, dep in enumerate(dependency_rows):
        try:
            source_id, target_package = int(dep["depending_version"]), int(dep["depending_on_package"])
            str(dep["semver_str"])
        except (KeyError, TypeError, ValueError):
            unresolved += 1
            coverage_counts["UNKNOWN_MISSING"] += 1
            continue
        source = by_id.get(source_id)
        if source is None or str(source["created_at"]) > cutoff:
            coverage_counts["OUT_OF_SCOPE"] += 1
            continue
        target = _adjacent_target(source, by_pkg.get(target_package, ()), cutoff)
        if target is None:
            if target_package in complete_targets:
                coverage_counts["OBSERVED_ABSENT_COMPLETE"] += 1
            else:
                coverage_counts["UNKNOWN_MISSING"] += 1
            continue
        tau = _canonical_tau(source_id, target_package, int(target["id"]))
        cand = Candidate(
            tau=tau,
            snapshot_time=cutoff,
            provenance=(
                f"package_versions.csv:id:{source_id}",
                f"package_dependencies.csv:row:{d_idx}",
                f"package_versions.csv:id:{int(target['id'])}",
            ),
            coverage_state="OBSERVED_PRESENT",
            resolution_status="RESOLVED",
        )
        previous = seen.get(tau)
        if previous is None or cand.provenance < previous.provenance:
            seen[tau] = cand
    coverage_counts["OBSERVED_PRESENT"] = len(seen)
    records = [{
        "tau": list(c.tau),
        "snapshot_time": c.snapshot_time,
        "provenance": list(c.provenance),
        "coverage_state": c.coverage_state,
        "resolution_status": c.resolution_status,
        "construction_version": CONSTRUCTION_VERSION,
        "temporal_rule": TEMPORAL_RULE_ID,
    } for c in (seen[k] for k in sorted(seen))]
    return {
        "U_t": records,
        "u_count": len(records),
        "unresolved_count": unresolved,
        "coverage_counts": coverage_counts,
        "coverage_states": list(COVERAGE_STATES),
        "construction_version": CONSTRUCTION_VERSION,
        "temporal_rule": TEMPORAL_RULE_ID,
        "cutoff": cutoff,
        "output_sha256": _output_hash(records),
    }
