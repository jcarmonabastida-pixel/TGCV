from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

MASTER_SEED = 20260930
REPLICATES = 1000
EFFECTS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0)
NS = (1728, 2304, 3456, 5184, 6912)
EXPECTED_CELLS = {(n, e) for n in NS for e in EFFECTS}

def seed_hash(label, n):
    seeds = [
        int.from_bytes(hashlib.sha256(
            f"{MASTER_SEED}|{label}|{n}|{r}|{r}".encode()
        ).digest()[:8], "big")
        for r in range(REPLICATES)
    ]
    return hashlib.sha256(json.dumps(seeds).encode()).hexdigest()

def result_hash(obj):
    payload = dict(obj)
    payload.pop("result_sha256", None)
    return hashlib.sha256(json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--source-run-id", type=int, required=True)
    args = ap.parse_args()

    files = sorted(args.artifact_root.rglob(
        "TI001_V012_NEXT4_POWER_SIMULATION_CELL_N*_E*.json"
    ))
    seen = {}
    serialization_normalizations = 0
    for path in files:
        raw_text = path.read_text(encoding="utf-8")
        # Frozen scientific artifacts may contain a literal \\n suffix from serialization.
        if raw_text.endswith("\\\\n"):
            raw_text = raw_text[:-2]
            serialization_normalizations += 1
        obj = json.loads(raw_text)
        key = (int(obj["N"]), float(obj["effect_size"]))
        if key in seen:
            raise SystemExit(f"Duplicate cell artifact: {key}")
        checks = [
            obj.get("artifact") == "TI001_V012_NEXT4_POWER_SIMULATION_CELL_RESULT_001",
            obj.get("model") == "TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R",
            obj.get("engine") == "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py",
            obj.get("dgp") == "TI001_V012_NEXT4_DGP_SPECIFICATION_002",
            obj.get("master_seed") == MASTER_SEED,
            obj.get("replicates") == REPLICATES,
            obj.get("convergence_count") == REPLICATES,
            obj.get("valid_fit_count") == REPLICATES,
            obj.get("scientific_execution") is True,
            obj.get("provider_api_calls") is False,
            obj.get("adaptive_stopping") is False,
            obj.get("parameter_tuning_after_results") is False,
            obj.get("diagnostics", {}).get("seed_replay_hash") == seed_hash(obj["effect_label"], key[0]),
            obj.get("result_sha256") == result_hash(obj),
            len(obj.get("replicates_detail", [])) == REPLICATES,
        ]
        if not all(checks):
            raise SystemExit(f"Cell audit failed: {key}")
        seen[key] = obj

    if set(seen) != EXPECTED_CELLS:
        raise SystemExit(
            f"Cell coverage mismatch: missing={sorted(EXPECTED_CELLS-set(seen))}, "
            f"unexpected={sorted(set(seen)-EXPECTED_CELLS)}"
        )

    cells = []
    for n in NS:
        for effect in EFFECTS:
            obj = seen[(n, effect)]
            cells.append({
                "N": n, "effect_size": effect, "effect_label": obj["effect_label"],
                "replicates": obj["replicates"],
                "rejection_count": obj["rejection_count"],
                "empirical_rejection_rate": obj["empirical_rejection_rate"],
                "mean_estimate": obj["mean_estimate"],
                "sd_estimate": obj["sd_estimate"],
                "mean_se": obj["mean_se"],
                "result_sha256": obj["result_sha256"],
            })

    out = {
        "artifact": "TI001_V012_NEXT4_POWER_SIMULATION_40_CELL_AGGREGATION_AUDIT_001",
        "source_run_id": args.source_run_id,
        "master_seed": MASTER_SEED,
        "replicates_per_cell": REPLICATES,
        "expected_cell_count": 40,
        "observed_cell_count": len(cells),
        "coverage_pass": True,
        "cell_integrity_pass": True,
        "cells": cells,
    }
    raw = json.dumps(out, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    out["audit_result_sha256"] = hashlib.sha256(raw).hexdigest()
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "observed_cell_count": len(cells),
        "output": str(args.output),
        "audit_result_sha256": out["audit_result_sha256"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
