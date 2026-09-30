"""Audit and aggregate the frozen NEXT4 Monte Carlo cell artifacts.

This audit consumes artifacts from a completed GitHub Actions Monte Carlo run.
It does not rerun scientific cells and does not tune parameters.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

MASTER_SEED = 20260930
REPLICATES = 1000
EFFECTS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0)
NS = (1728, 2304, 3456, 5184, 6912)
EXPECTED_CELLS = {(n, e) for n in NS for e in EFFECTS}


def expected_seed_replay_hash(effect_label: str, n: int) -> str:
    seeds = []
    for r in range(REPLICATES):
        seeds.append(
            int.from_bytes(
                hashlib.sha256(
                    f"{MASTER_SEED}|{effect_label}|{n}|{r}|{r}".encode()
                ).digest()[:8],
                "big",
            )
        )
    return hashlib.sha256(json.dumps(seeds).encode()).hexdigest()


def result_sha_without_result_sha(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("result_sha256", None)
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--source-run-id", type=int, required=True)
    args = ap.parse_args()

    files = sorted(
        args.artifact_root.rglob(
            "TI001_V012_NEXT4_POWER_SIMULATION_CELL_N*_E*.json"
        )
    )
    seen = {}
    checks = []
    for path in files:
        obj = json.loads(path.read_text(encoding="utf-8"))
        n = int(obj["N"])
        effect = float(obj["effect_size"])
        key = (n, effect)
        checks.append(
            {
                "path": str(path),
                "cell": [n, effect],
                "schema": obj.get("artifact") == "TI001_V012_NEXT4_POWER_SIMULATION_CELL_RESULT_001",
                "model": obj.get("model") == "TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R",
                "engine": obj.get("engine") == "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py",
                "dgp": obj.get("dgp") == "TI001_V012_NEXT4_DGP_SPECIFICATION_002",
                "master_seed": obj.get("master_seed") == MASTER_SEED,
                "replicates": obj.get("replicates") == REPLICATES,
                "convergence_count": obj.get("convergence_count") == REPLICATES,
                "valid_fit_count": obj.get("valid_fit_count") == REPLICATES,
                "scientific_execution": obj.get("scientific_execution") is True,
                "provider_api_calls": obj.get("provider_api_calls") is False,
                "adaptive_stopping": obj.get("adaptive_stopping") is False,
                "parameter_tuning_after_results": obj.get("parameter_tuning_after_results") is False,
                "seed_replay_hash": obj.get("diagnostics", {}).get("seed_replay_hash")
                    == expected_seed_replay_hash(obj["effect_label"], n),
                "result_sha256": obj.get("result_sha256")
                    == result_sha_without_result_sha(obj),
                "detail_count": len(obj.get("replicates_detail", [])) == REPLICATES,
            }
        )
        if key in seen:
            raise SystemExit(f"Duplicate cell artifact: {key}")
        seen[key] = obj

    missing = sorted(EXPECTED_CELLS - set(seen))
    unexpected = sorted(set(seen) - EXPECTED_CELLS)
    if missing or unexpected:
        raise SystemExit(
            f"Cell coverage mismatch: missing={missing}, unexpected={unexpected}"
        )

    for check in checks:
        if not all(v for k, v in check.items() if k not in ("path", "cell")):
            raise SystemExit(f"Cell audit failed: {check}")

    cells = []
    for n in NS:
        for effect in EFFECTS:
            obj = seen[(n, effect)]
            cells.append(
                {
                    "N": n,
                    "effect_size": effect,
                    "effect_label": obj["effect_label"],
                    "replicates": obj["replicates"],
                    "rejection_count": obj["rejection_count"],
                    "empirical_rejection_rate": obj["empirical_rejection_rate"],
                    "mean_estimate": obj["mean_estimate"],
                    "sd_estimate": obj["sd_estimate"],
                    "mean_se": obj["mean_se"],
                    "result_sha256": obj["result_sha256"],
                }
            )

    out = {
        "artifact": "TI001_V012_NEXT4_POWER_SIMULATION_40_CELL_AGGREGATION_AUDIT_001",
        "source_run_id": args.source_run_id,
        "master_seed": MASTER_SEED,
        "replicates_per_cell": REPLICATES,
        "expected_cell_count": 40,
        "observed_cell_count": len(cells),
        "coverage_pass": len(cells) == 40,
        "cell_integrity_pass": True,
        "cells": cells,
    }
    raw = json.dumps(out, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    out["audit_result_sha256"] = hashlib.sha256(raw).hexdigest()
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "
", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "observed_cell_count": len(cells),
        "output": str(args.output),
        "audit_result_sha256": out["audit_result_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
