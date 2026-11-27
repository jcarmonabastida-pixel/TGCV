"""Single-cell, development-only M1-PCT check for F5 M30/R20 raw-between."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_nested_mr_comparative_holdout import generate_holdout_dataset
from run_c10s_f5_m1_dev_pilot import historical_seed_roster, derive_m1_seed
from c10s_f5_functional_refit_bootstrap import (
    _replicate_seed, fitted_functional_refit_percentile_bootstrap,
)

CELL = "F5_beta22_M30_R20"
SCHEDULE_ID = "C10S_F5_M1_M30R20_RAWBETWEEN_DEV_001"
SEED_NAMESPACE = "c10s_f5_m1_m30r20_rawbetween_dev_v1"
K = 400
B = 100
FIRST_INDEX = 50
Z95 = 1.959963984540054


def derive_seed(stream: str, index: int) -> int:
    payload = f"{SCHEDULE_ID}|{SEED_NAMESPACE}|{stream}|{CELL}|{index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def wilson(successes: int, n: int) -> list[float] | None:
    if n <= 0:
        return None
    p = successes / n
    z2 = Z95 * Z95
    den = 1.0 + z2 / n
    center = (p + z2 / (2.0 * n)) / den
    half = Z95 * math.sqrt(p * (1.0 - p) / n + z2 / (4.0 * n * n)) / den
    return [center - half, center + half]


def seed_audit() -> dict:
    historical = historical_seed_roster()
    # Include every seed used by the earlier M1 pilot, including its 100 refits.
    for cell in ("F5_beta22_M10_R5", CELL):
        for i in range(50):
            ds = derive_m1_seed("dataset", cell, i)
            bs = derive_m1_seed("bootstrap", cell, i)
            historical.add(ds)
            historical.add(bs)
            historical.update(_replicate_seed(bs, b) for b in range(100))
    new = set()
    for i in range(FIRST_INDEX, FIRST_INDEX + K):
        ds = derive_seed("dataset", i)
        bs = derive_seed("bootstrap", i)
        values = [ds, bs]
        values.extend(_replicate_seed(bs, b) for b in range(B))
        if len(values) != len(set(values)) or any(x in historical or x in new for x in values):
            raise RuntimeError("SEED_COLLISION")
        new.update(values)
    return {
        "status": "PASS",
        "historical_unique_values_checked": len(historical),
        "new_unique_values_checked": len(new),
        "collision_count": 0,
        "schedule_id": SCHEDULE_ID,
        "seed_namespace": SEED_NAMESPACE,
        "first_dataset_index": FIRST_INDEX,
        "dataset_count": K,
        "bootstrap_B": B,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-development-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.execute_development_only:
        raise RuntimeError("EXPLICIT_DEVELOPMENT_ONLY_FLAG_REQUIRED")

    audit = seed_audit()
    spec = next(x for x in tier_a_specs() if x.cell_id == CELL)
    rows = []
    started_all = time.perf_counter()
    for offset in range(K):
        index = FIRST_INDEX + offset
        ds = derive_seed("dataset", index)
        bs = derive_seed("bootstrap", index)
        generated = generate_holdout_dataset(spec, index, seed_override=ds)
        counts = [int(round(sum(row))) for row in generated]
        t0 = time.perf_counter()
        result = fitted_functional_refit_percentile_bootstrap(
            counts, r=spec.r, bootstrap_replicates=B, bootstrap_seed=bs,
        )
        elapsed = time.perf_counter() - t0
        emitted = result.status == "EMITTED"
        rows.append({
            "dataset_index": index,
            "dataset_seed": ds,
            "bootstrap_seed": bs,
            "counts_sha256": hashlib.sha256(
                json.dumps(counts, separators=(",", ":")).encode()
            ).hexdigest(),
            "status": result.status,
            "emitted": emitted,
            "elapsed_seconds": elapsed,
            "truth_within": spec.true_within,
            "truth_raw_between": spec.true_between,
            "point_within": result.point_within,
            "point_raw_between": result.point_between,
            "within_interval": result.within_interval,
            "raw_between_interval": result.between_interval,
            "fitted_concentration": result.original_fit.concentration,
            "original_fit_status": result.original_fit.status,
            "valid_replicates": result.valid_replicates,
            "failed_replicates": result.failed_replicates,
            "failure_counts": result.failure_counts,
        })

    emitted = [x for x in rows if x["emitted"]]
    raw_hits = sum(
        x["raw_between_interval"][0] <= x["truth_raw_between"] <= x["raw_between_interval"][1]
        for x in emitted
    )
    within_hits = sum(
        x["within_interval"][0] <= x["truth_within"] <= x["within_interval"][1]
        for x in emitted
    )
    kappa_values = [x["fitted_concentration"] for x in emitted if x["fitted_concentration"] is not None]
    kappa_cut = float(np.quantile(kappa_values, 0.90)) if kappa_values else None
    tail = [x for x in emitted if kappa_cut is not None and x["fitted_concentration"] >= kappa_cut]
    tail_hits = sum(
        x["raw_between_interval"][0] <= x["truth_raw_between"] <= x["raw_between_interval"][1]
        for x in tail
    )
    payload = {
        "schema": "C10S-F5-M1-M30R20-RAWBETWEEN-DEV-1.0",
        "scope": "DEVELOPMENT_ONLY_NOT_TIER_A_NOT_CONFIRMATORY",
        "method_id": "F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0",
        "fit_contract_id": "F5_M1_ANALYTIC_LBFGSB_BEST_SUCCESSFUL_START_1.0",
        "cell": CELL,
        "primary_target": "RAW_BETWEEN",
        "within_role": "DESCRIPTIVE_SECONDARY_ONLY_NOT_A_METHOD_SELECTION_TARGET",
        "k": K, "bootstrap_B": B,
        "seed_audit": audit,
        "runtime_seconds": time.perf_counter() - started_all,
        "emitted": len(emitted),
        "emission_rate": len(emitted) / K,
        "raw_between": {
            "hits": raw_hits, "denominator": len(emitted),
            "conditional_coverage": raw_hits / len(emitted) if emitted else None,
            "wilson_95": wilson(raw_hits, len(emitted)),
        },
        "within_descriptive": {
            "hits": within_hits, "denominator": len(emitted),
            "conditional_coverage": within_hits / len(emitted) if emitted else None,
            "wilson_95": wilson(within_hits, len(emitted)),
        },
        "exploratory_top_kappa_decile": {
            "postfit_kappa_cutoff": kappa_cut,
            "datasets": len(tail),
            "raw_between_hits": tail_hits,
            "raw_between_coverage": tail_hits / len(tail) if tail else None,
            "not_an_acceptance_stratum": True,
        },
        "status_counts": {
            status: sum(x["status"] == status for x in rows)
            for status in sorted({x["status"] for x in rows})
        },
        "total_failed_bootstrap_refits": sum(x["failed_replicates"] for x in rows),
        "datasets": rows,
        "coverage_adjudication": "DEVELOPMENT_SCREEN_ONLY",
        "method_selection": "NOT_PERFORMED",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in (
        "schema", "scope", "cell", "k", "bootstrap_B", "seed_audit",
        "runtime_seconds", "emitted", "emission_rate", "raw_between",
        "within_descriptive", "exploratory_top_kappa_decile", "status_counts",
        "total_failed_bootstrap_refits", "coverage_adjudication", "method_selection",
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
