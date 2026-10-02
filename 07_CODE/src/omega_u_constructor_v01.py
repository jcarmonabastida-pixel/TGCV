"""Deterministic constructor for the TGCV Rust Ω-primary observational U_t.
Independent from historical EXT-1.1 identity recovery and live registries.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Iterable, Mapping, Sequence

TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
CONSTRUCTION_VERSION = "RUST_OMEGA_U_CONSTRUCTOR_v0.6"
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


def build_u_t_from_sqlite(conn, dependencies, *, cutoff, complete_target_packages=()):
    """Build U_t from a disk-backed SQLite version index."""
    def fetch_version(vid):
        return conn.execute("SELECT id,package_id,version_str,created_at FROM versions WHERE id=?", (vid,)).fetchone()
    def adjacent_target(package_id, source_time):
        return conn.execute(
            "SELECT id,package_id,version_str,created_at FROM versions "
            "WHERE package_id=? AND created_at>? AND created_at<=? "
            "ORDER BY created_at,id,version_str LIMIT 1",
            (package_id, source_time, cutoff),
        ).fetchone()
    seen = {}
    coverage_counts = {state: 0 for state in COVERAGE_STATES}
    complete_targets = {int(x) for x in complete_target_packages}
    unresolved = 0
    for d_idx, dep in enumerate(dependencies):
        try:
            source_id, target_package = int(dep["depending_version"]), int(dep["depending_on_package"])
            str(dep["semver_str"])
        except (KeyError, TypeError, ValueError):
            unresolved += 1
            coverage_counts["UNKNOWN_MISSING"] += 1
            continue
        source = fetch_version(source_id)
        if source is None or str(source[3]) > cutoff:
            coverage_counts["OUT_OF_SCOPE"] += 1
            continue
        target = adjacent_target(target_package, str(source[3]))
        if target is None:
            coverage_counts["OBSERVED_ABSENT_COMPLETE" if target_package in complete_targets else "UNKNOWN_MISSING"] += 1
            continue
        tau = _canonical_tau(source_id, target_package, int(target[0]))
        cand = Candidate(tau=tau, snapshot_time=cutoff,
            provenance=(f"package_versions.csv:id:{source_id}", f"package_dependencies.csv:row:{d_idx}", f"package_versions.csv:id:{int(target[0])}"),
            coverage_state="OBSERVED_PRESENT", resolution_status="RESOLVED")
        previous = seen.get(tau)
        if previous is None or cand.provenance < previous.provenance:
            seen[tau] = cand
    coverage_counts["OBSERVED_PRESENT"] = len(seen)
    records = [{"tau":list(c.tau),"snapshot_time":c.snapshot_time,"provenance":list(c.provenance),
                "coverage_state":c.coverage_state,"resolution_status":c.resolution_status,
                "construction_version":CONSTRUCTION_VERSION,"temporal_rule":TEMPORAL_RULE_ID}
               for c in (seen[k] for k in sorted(seen))]
    return {"U_t":records,"u_count":len(records),"unresolved_count":unresolved,
            "coverage_counts":coverage_counts,"coverage_states":list(COVERAGE_STATES),
            "construction_version":CONSTRUCTION_VERSION,"temporal_rule":TEMPORAL_RULE_ID,
            "cutoff":cutoff,"output_sha256":_output_hash(records)}


def build_u_t_from_sqlite_disk(conn, dependencies, *, cutoff, complete_target_packages=()):
    """Construct U_t into SQLite with constant RAM usage and return metadata only."""
    conn.execute("DROP TABLE IF EXISTS u_records")
    conn.execute(
        "CREATE TABLE u_records ("
        "origin_version_id INTEGER NOT NULL,"
        "target_package_id INTEGER NOT NULL,"
        "target_version_id INTEGER NOT NULL,"
        "snapshot_time TEXT NOT NULL,"
        "provenance_source TEXT NOT NULL,"
        "provenance_dependency TEXT NOT NULL,"
        "provenance_target TEXT NOT NULL,"
        "coverage_state TEXT NOT NULL,"
        "resolution_status TEXT NOT NULL,"
        "construction_version TEXT NOT NULL,"
        "temporal_rule TEXT NOT NULL,"
        "PRIMARY KEY(origin_version_id,target_package_id,target_version_id)"
        ")"
    )
    def fetch_version(vid):
        return conn.execute(
            "SELECT id,package_id,version_str,created_at FROM versions WHERE id=?",
            (vid,),
        ).fetchone()
    def adjacent_target(package_id, source_time):
        return conn.execute(
            "SELECT id,package_id,version_str,created_at FROM versions "
            "WHERE package_id=? AND created_at>? AND created_at<=? "
            "ORDER BY created_at,id,version_str LIMIT 1",
            (package_id, source_time, cutoff),
        ).fetchone()

    coverage_counts = {state: 0 for state in COVERAGE_STATES}
    complete_targets = {int(x) for x in complete_target_packages}
    unresolved = 0

    for d_idx, dep in enumerate(dependencies):
        try:
            source_id = int(dep["depending_version"])
            target_package = int(dep["depending_on_package"])
            str(dep["semver_str"])
        except (KeyError, TypeError, ValueError):
            unresolved += 1
            coverage_counts["UNKNOWN_MISSING"] += 1
            continue

        source = fetch_version(source_id)
        if source is None or str(source[3]) > cutoff:
            coverage_counts["OUT_OF_SCOPE"] += 1
            continue

        target = adjacent_target(target_package, str(source[3]))
        if target is None:
            state = "OBSERVED_ABSENT_COMPLETE" if target_package in complete_targets else "UNKNOWN_MISSING"
            coverage_counts[state] += 1
            continue

        target_id = int(target[0])
        tau = _canonical_tau(source_id, target_package, target_id)
        provenance = (
            f"package_versions.csv:id:{source_id}",
            f"package_dependencies.csv:row:{d_idx}",
            f"package_versions.csv:id:{target_id}",
        )
        cur = conn.execute(
            "INSERT OR IGNORE INTO u_records VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (
                source_id, target_package, target_id, cutoff,
                provenance[0], provenance[1], provenance[2],
                "OBSERVED_PRESENT", "RESOLVED",
                CONSTRUCTION_VERSION, TEMPORAL_RULE_ID,
            ),
        )
        if cur.rowcount:
            coverage_counts["OBSERVED_PRESENT"] += 1

    conn.commit()
    h = sha256()
    first = True
    for row in conn.execute(
        "SELECT origin_version_id,target_package_id,target_version_id,snapshot_time,"
        "provenance_source,provenance_dependency,provenance_target,coverage_state,"
        "resolution_status,construction_version,temporal_rule "
        "FROM u_records ORDER BY origin_version_id,target_package_id,target_version_id"
    ):
        record = {
            "tau": [row[0], row[1], row[2]],
            "snapshot_time": row[3],
            "provenance": [row[4], row[5], row[6]],
            "coverage_state": row[7],
            "resolution_status": row[8],
            "construction_version": row[9],
            "temporal_rule": row[10],
        }
        payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        if not first:
            h.update(b",")
        first = False
        h.update(payload.encode("utf-8"))

    output_hash = sha256(b"[" + (b"" if coverage_counts["OBSERVED_PRESENT"] == 0 else b"") + b"]").hexdigest()
    # Recompute exact list hash without materialising it: the loop above hashed record payloads.
    # The list wrapper is added by rebuilding the digest state from the same ordered stream.
    h2 = sha256()
    h2.update(b"[")
    first = True
    for row in conn.execute(
        "SELECT origin_version_id,target_package_id,target_version_id,snapshot_time,"
        "provenance_source,provenance_dependency,provenance_target,coverage_state,"
        "resolution_status,construction_version,temporal_rule "
        "FROM u_records ORDER BY origin_version_id,target_package_id,target_version_id"
    ):
        record = {
            "tau": [row[0], row[1], row[2]],
            "snapshot_time": row[3],
            "provenance": [row[4], row[5], row[6]],
            "coverage_state": row[7],
            "resolution_status": row[8],
            "construction_version": row[9],
            "temporal_rule": row[10],
        }
        if not first:
            h2.update(b",")
        first = False
        h2.update(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    h2.update(b"]")

    return {
        "u_count": coverage_counts["OBSERVED_PRESENT"],
        "unresolved_count": unresolved,
        "coverage_counts": coverage_counts,
        "coverage_states": list(COVERAGE_STATES),
        "construction_version": CONSTRUCTION_VERSION,
        "temporal_rule": TEMPORAL_RULE_ID,
        "cutoff": cutoff,
        "output_sha256": h2.hexdigest(),
    }
