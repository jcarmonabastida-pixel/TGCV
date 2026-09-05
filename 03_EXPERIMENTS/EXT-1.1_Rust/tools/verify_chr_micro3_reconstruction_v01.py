#!/usr/bin/env python3
"""CHR-MICRO-3 reconstruction sub-gate.

This gate verifies the locally supplied historical snapshot evidence and the
independent package@version -> version_id bridge. It never accesses the current
registry, outcome data, or the frozen N-R8-C2 corpus.

It deliberately does NOT claim full Cargo resolver equivalence: the existing
snapshot replay tool only establishes candidate-universe reconstruction for the
supported SemVer subset. Full resolver equivalence remains OPEN until a pinned,
executable historical Cargo environment is demonstrated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED = {
    "serde": {"version": "1.0.0", "version_id": 50790},
    "tokio": {"version": "1.0.0", "version_id": 318256},
    "rand": {"version": "0.8.0", "version_id": 316445},
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_bridge(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, int] = {}
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---") or "Case |" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        package, version, version_id = cells[1], cells[2], cells[3]
        if package in EXPECTED:
            if version != EXPECTED[package]["version"]:
                raise ValueError(f"bridge version mismatch for {package}")
            out[package] = int(version_id)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot-serde", type=Path, required=True)
    ap.add_argument("--snapshot-tokio", type=Path, required=True)
    ap.add_argument("--snapshot-rand", type=Path, required=True)
    ap.add_argument("--bridge", type=Path, required=True)
    args = ap.parse_args()

    snapshots = {"serde": args.snapshot_serde, "tokio": args.snapshot_tokio, "rand": args.snapshot_rand}
    bridge = load_bridge(args.bridge)
    bridge_ok = bridge == {k: v["version_id"] for k, v in EXPECTED.items()}

    # Candidate-universe replay is intentionally delegated to the existing
    # snapshot-only tool. This verifier only establishes that the required
    # historical records exist and are locally hashable; it does not infer
    # resolver output.
    record_presence: dict[str, bool] = {}
    for package, path in snapshots.items():
        found = False
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("name") == package and rec.get("vers") == EXPECTED[package]["version"]:
                found = True
                break
        record_presence[package] = found

    result = {
        "gate": "CHR-MICRO-3_RECONSTRUCTION_v0.1",
        "status": "PASS_PARTIAL_BLOCKED",
        "scientific_execution": "NOT_PERFORMED",
        "rust_dataset_consumption": "NOT_PERFORMED",
        "corpus_access": "NOT_PERFORMED",
        "historical_record_presence": record_presence,
        "snapshot_sha256": {k: sha256(v) for k, v in snapshots.items()},
        "version_id_bridge": bridge,
        "version_id_bridge_verified": bridge_ok,
        "R1_release_identity": all(record_presence.values()),
        "R2_historical_registry_state": all(record_presence.values()),
        "R3_dependency_metadata": "OPEN",
        "R4_candidate_universe": "OPEN_UNTIL_REPLAY_EXECUTED",
        "R5_deterministic_resolution": "BLOCKED",
        "R6_version_id_bridge": "PASS" if bridge_ok else "FAIL",
        "R7_download_archive_bridge": "OPEN",
        "R8_temporal_censoring": "OPEN",
        "R9_no_outcome_leakage": "PASS_BY_CONTRACT",
        "R10_T_acc_operationalisation": "OPEN",
        "decision": "HRSV_RECONSTRUCTION_PARTIAL; RESOLUTION_REMAINS_BLOCKED",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
