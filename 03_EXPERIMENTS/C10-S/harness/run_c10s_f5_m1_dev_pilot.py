"""Bounded fresh-seed M1-PCT implementation pilot; never a Tier-A run."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import time

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_nested_mr_comparative_holdout import generate_holdout_dataset
from run_c10s_post_holdout_f5_b2_b3_development_calibration import (
    _historical_seed_values,
    derive_seed as derive_b2_seed,
)
from run_c10s_f5_g7_tiera_calibration import (
    HOLDOUT_NAMESPACE as G7_HOLDOUT_NAMESPACE,
    RESOURCE_NAMESPACE as G7_RESOURCE_NAMESPACE,
    derive_seed as derive_g7_seed,
)
from c10s_f5_functional_refit_bootstrap import (
    METHOD_ID,
    FIT_CONTRACT_ID,
    _replicate_seed,
    fitted_functional_refit_percentile_bootstrap,
)

SCHEDULE_ID = "C10S_F5_M1_DEV_PILOT_SEEDS_1.0"
SEED_NAMESPACE = "c10s_f5_m1_dev_pilot_v1"
F5_CELLS = ("F5_beta22_M10_R5", "F5_beta22_M30_R20")
K_PER_CELL = 50
BOOTSTRAP_B = 100


class M1PilotError(RuntimeError):
    pass


def derive_m1_seed(stream: str, cell_id: str, index: int) -> int:
    if stream not in {"dataset", "bootstrap"} or cell_id not in F5_CELLS:
        raise M1PilotError("INVALID_M1_PILOT_SEED_STREAM_OR_CELL")
    if type(index) is not int or index < 0:
        raise M1PilotError("INVALID_M1_PILOT_INDEX")
    payload = f"{SCHEDULE_ID}|{SEED_NAMESPACE}|{stream}|{cell_id}|{index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def historical_seed_roster() -> set[int]:
    values = set(_historical_seed_values())
    b2_streams = (
        "f5_optimizer_calibration_dataset", "f5_optimizer_validation_dataset",
        "f5_c0_bootstrap", "f5_c5_bootstrap",
        "f5_endpoint_sensitivity_b1000", "f5_endpoint_sensitivity_b4000",
    )
    for cell in F5_CELLS:
        for i in range(5000):
            for stream in b2_streams:
                values.add(derive_b2_seed(stream, cell, i))
        for i in range(1000):
            for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
                values.add(derive_g7_seed(G7_HOLDOUT_NAMESPACE, stream, cell, i))
        for i in range(100):
            for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
                values.add(derive_g7_seed(G7_RESOURCE_NAMESPACE, stream, cell, i))
    return values


def build_seed_roster(historical: set[int]) -> dict:
    new_values = set()
    rows = []
    for cell in F5_CELLS:
        for i in range(K_PER_CELL):
            dataset_seed = derive_m1_seed("dataset", cell, i)
            bootstrap_seed = derive_m1_seed("bootstrap", cell, i)
            seeds = [dataset_seed, bootstrap_seed]
            seeds.extend(_replicate_seed(bootstrap_seed, b) for b in range(BOOTSTRAP_B))
            if len(seeds) != len(set(seeds)):
                raise M1PilotError("M1_PILOT_INTERNAL_SEED_COLLISION")
            if any(seed in historical or seed in new_values for seed in seeds):
                raise M1PilotError("M1_PILOT_HISTORICAL_OR_CROSS_STREAM_SEED_COLLISION")
            new_values.update(seeds)
            rows.append((cell, i, dataset_seed, bootstrap_seed))
    return {
        "rows": rows,
        "audit": {
            "status": "PASS",
            "historical_seed_values_checked": len(historical),
            "new_seed_values_checked": len(new_values),
            "new_unique_seed_values": len(new_values),
            "collision_count": 0,
            "schedule_id": SCHEDULE_ID,
            "seed_namespace": SEED_NAMESPACE,
        },
    }


def run_pilot(output_path: Path) -> dict:
    historical = historical_seed_roster()
    roster = build_seed_roster(historical)
    specs = {spec.cell_id: spec for spec in tier_a_specs()}
    results = []
    for cell, index, dataset_seed, bootstrap_seed in roster["rows"]:
        spec = specs[cell]
        started = time.perf_counter()
        rows = generate_holdout_dataset(spec, index, seed_override=dataset_seed)
        counts = [int(round(sum(row))) for row in rows]
        result = fitted_functional_refit_percentile_bootstrap(
            counts, r=spec.r, bootstrap_replicates=BOOTSTRAP_B,
            bootstrap_seed=bootstrap_seed,
        )
        elapsed = time.perf_counter() - started
        emitted = result.status == "EMITTED"
        results.append({
            "cell_id": cell, "dataset_index": index,
            "dataset_seed": dataset_seed, "bootstrap_seed": bootstrap_seed,
            "counts_sha256": hashlib.sha256(
                json.dumps(counts, separators=(",", ":")).encode()
            ).hexdigest(),
            "status": result.status, "elapsed_seconds": elapsed,
            "point_within": result.point_within,
            "point_between": result.point_between,
            "within_interval": result.within_interval,
            "between_interval": result.between_interval,
            "valid_replicates": result.valid_replicates,
            "failed_replicates": result.failed_replicates,
            "failure_counts": result.failure_counts,
            "original_fit": result.original_fit,
            "replicate_records": result.replicate_records,
            "truth_within": spec.true_within,
            "truth_between": spec.true_between,
            "emitted": emitted,
        })
    summaries = {}
    for cell in F5_CELLS:
        cell_rows = [row for row in results if row["cell_id"] == cell]
        emitted = [row for row in cell_rows if row["emitted"]]
        summaries[cell] = {
            "datasets": len(cell_rows),
            "emitted": len(emitted),
            "emission_rate": len(emitted) / len(cell_rows),
            "within_conditional_coverage_descriptive": (
                sum(row["within_interval"][0] <= row["truth_within"] <= row["within_interval"][1]
                    for row in emitted) / len(emitted) if emitted else None
            ),
            "between_conditional_coverage_descriptive": (
                sum(row["between_interval"][0] <= row["truth_between"] <= row["between_interval"][1]
                    for row in emitted) / len(emitted) if emitted else None
            ),
            "mean_runtime_seconds": sum(row["elapsed_seconds"] for row in cell_rows) / len(cell_rows),
            "failed_bootstrap_replicates": sum(row["failed_replicates"] for row in cell_rows),
            "abstention_status_counts": {
                status: sum(row["status"] == status for row in cell_rows)
                for status in sorted({row["status"] for row in cell_rows if row["status"] != "EMITTED"})
            },
        }
    payload = {
        "schema": "C10S-F5-M1-PCT-DEV-PILOT-1.0",
        "scope": "DEVELOPMENT_ONLY_SMOKE_PILOT_NOT_TIER_A_NOT_CONFIRMATORY",
        "method_id": METHOD_ID, "fit_contract_id": FIT_CONTRACT_ID,
        "schedule_id": SCHEDULE_ID, "seed_namespace": SEED_NAMESPACE,
        "k_per_cell": K_PER_CELL, "bootstrap_B": BOOTSTRAP_B,
        "seed_collision_audit": roster["audit"],
        "coverage_adjudication": "NOT_PERFORMED",
        "method_selection": "NOT_PERFORMED",
        "summaries": summaries, "datasets": results,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-development-pilot", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.execute_development_pilot:
        raise M1PilotError("EXPLICIT_DEVELOPMENT_PILOT_FLAG_REQUIRED")
    result = run_pilot(args.output)
    print(json.dumps({
        "schema": result["schema"], "scope": result["scope"],
        "seed_collision_audit": result["seed_collision_audit"],
        "summaries": result["summaries"],
        "coverage_adjudication": result["coverage_adjudication"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
