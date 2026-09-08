"""RUST-DYN-EXEC-1 real-data executor v0.1."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from rstar_v02 import resolve_edge

VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1
DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
RSTAR_SHA256 = "669d4f01131af518f32b1b4b3da27f676ae4ae55"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def parse_created_at(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def canonical_tacc(items: list[tuple[int, int, int, str]]) -> list[tuple[int, int, int, str]]:
    out = sorted(items, key=lambda x: (x[0], x[1], x[2], x[3]))
    if len(out) != len(set(out)):
        raise RuntimeError("duplicate canonical transformation")
    return out


def tacc_hash(items: list[tuple[int, int, int, str]]) -> str:
    payload = "\n".join(f"{a}|{b}|{c}|{d}" for a, b, c, d in items).encode()
    return hashlib.sha256(payload).hexdigest()


def read_rows(zf: zipfile.ZipFile, member: str) -> list[dict[str, str]]:
    names = {n.replace("\\", "/") for n in zf.namelist()}
    if member not in names:
        raise RuntimeError(f"required archive member missing: {member}")
    with zf.open(member) as raw:
        return list(csv.DictReader((line.decode("utf-8-sig") for line in raw)))


def build_real_model(dataset: Path):
    with zipfile.ZipFile(dataset, "r") as zf:
        versions = read_rows(zf, VERSIONS_MEMBER)
        deps = read_rows(zf, DEPENDENCIES_MEMBER)

    required_v = {"id", "package_id", "version_str", "created_at"}
    required_d = {"depending_version", "depending_on_package", "semver_str"}
    if not versions or set(versions[0]) != required_v:
        raise RuntimeError("package_versions schema mismatch")
    if not deps or set(deps[0]) != required_d:
        raise RuntimeError("package_dependencies schema mismatch")

    by_id = {}
    by_package = defaultdict(list)
    for r in versions:
        oid = int(r["id"])
        if oid in by_id:
            raise RuntimeError("duplicate origin id")
        created = parse_created_at(r["created_at"])
        row = {"version_id": oid, "package_id": int(r["package_id"]),
               "version_str": r["version_str"], "created_at": created}
        by_id[oid] = row
        by_package[row["package_id"]].append(row)

    dep_map = defaultdict(list)
    for r in deps:
        dep_map[int(r["depending_version"])].append(
            (int(r["depending_on_package"]), r["semver_str"])
        )

    tacc_by_origin = {}
    for o in by_id.values():
        transformations = []
        origin_created_at = o["created_at"].isoformat()
        for target_package_id, requirement in dep_map.get(o["version_id"], []):
            target_versions = [
                (v["version_id"], v["version_str"], v["created_at"].isoformat())
                for v in by_package.get(target_package_id, [])
            ]
            resolved = resolve_edge(
                origin_id=o["version_id"],
                origin_name=str(o["version_id"]),
                origin_created_at=origin_created_at,
                target_package_id=target_package_id,
                target_name=str(target_package_id),
                requirement=requirement,
                target_versions=target_versions,
            )
            selected_id = resolved["selected_version_id"]
            selected_version = resolved["selected_version"]
            if selected_id is None:
                continue
            transformations.append((
                o["version_id"],
                target_package_id,
                selected_id,
                selected_version,
            ))
        tacc_by_origin[o["version_id"]] = canonical_tacc(transformations)

    pairs = []
    tie_origin_count = 0
    excluded_origin_count = 0
    for package_id, rows in by_package.items():
        rows = sorted(rows, key=lambda r: r["created_at"])
        tied = set()
        for a, b in zip(rows, rows[1:]):
            if a["created_at"] == b["created_at"]:
                tied.add(a["version_id"])
                tied.add(b["version_id"])
        tie_origin_count += len(tied)
        excluded_origin_count += len(tied)
        eligible = [r for r in rows if r["version_id"] not in tied]
        pairs.extend(zip(eligible, eligible[1:]))

    return by_id, tacc_by_origin, pairs, tie_origin_count, excluded_origin_count, len(by_package)


def reach_h1(origin_id: int, tacc: dict[int, list[tuple[int, int, int, str]]]) -> set[int]:
    return {target_id for _, _, target_id, _ in tacc.get(origin_id, []) if target_id != origin_id}


def trajectory_h1(origin_id: int, tacc: dict[int, list[tuple[int, int, int, str]]]) -> tuple[int, ...]:
    return tuple(sorted(reach_h1(origin_id, tacc)))


def execute(dataset: Path) -> dict:
    actual = sha256_file(dataset)
    if actual != DATASET_SHA256:
        raise RuntimeError("dataset SHA-256 mismatch")
    by_id, tacc, pairs, tie_count, excluded_count, package_count = build_real_model(dataset)

    class_counts = {"PERSISTENCE": 0, "EXPANSION": 0, "CONTRACTION": 0, "RECONFIGURATION": 0}
    pair_rows = []
    for a, b in pairs:
        ta, tb = set(tacc[a["version_id"]]), set(tacc[b["version_id"]])
        added, removed = tb - ta, ta - tb
        if not added and not removed:
            cls = "PERSISTENCE"
        elif added and not removed:
            cls = "EXPANSION"
        elif removed and not added:
            cls = "CONTRACTION"
        else:
            cls = "RECONFIGURATION"
        class_counts[cls] += 1
        ra = reach_h1(a["version_id"], tacc)
        rb = reach_h1(b["version_id"], tacc)
        tr_a = trajectory_h1(a["version_id"], tacc)
        tr_b = trajectory_h1(b["version_id"], tacc)
        pair_rows.append({
            "package_id": a["package_id"],
            "origin_a": a["version_id"], "origin_b": b["version_id"],
            "tacc_a_count": len(ta), "tacc_b_count": len(tb),
            "tacc_a_hash": tacc_hash(sorted(ta)), "tacc_b_hash": tacc_hash(sorted(tb)),
            "delta_tacc": bool(ta != tb),
            "delta_tacc_added_count": len(added), "delta_tacc_removed_count": len(removed),
            "class": cls,
            "reach_a_h1_count": len(ra), "reach_b_h1_count": len(rb),
            "trajectory_a_h1": list(tr_a), "trajectory_b_h1": list(tr_b),
        })

    return {
        "MODE": "REAL_DATASET_EXECUTION",
        "pass": True,
        "dataset_sha256": actual,
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "horizon": HORIZON,
        "origin_count": len(by_id),
        "package_count": package_count,
        "timestamp_tie_origin_count": tie_count,
        "excluded_origin_count_due_to_ties": excluded_count,
        "temporal_pair_count": len(pairs),
        "classification_counts": class_counts,
        "pairs": pair_rows,
        "firewall": {
            "outcome_read": False,
            "future_activity_read": False,
            "predictive_metrics": False,
            "sampling": False,
            "post_origin_metadata": False,
            "reach_used_to_construct_tacc": False,
            "trajectory_used_to_construct_tacc": False,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    dataset = Path(args.dataset)
    if not dataset.is_file():
        raise SystemExit("dataset not found")
    result = execute(dataset)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({
        "MODE": result["MODE"], "pass": result["pass"],
        "dataset_sha256": result["dataset_sha256"],
        "temporal_pair_count": result["temporal_pair_count"],
        "classification_counts": result["classification_counts"],
        "HORIZON": result["horizon"],
        "REAL_DATASET_EXECUTION": True,
        "EXECUTION_AUTHORIZATION": True,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
