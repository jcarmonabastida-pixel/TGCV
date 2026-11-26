from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
from statistics import median
from time import perf_counter
from fractions import Fraction

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_nested_mr_comparative_holdout import generate_holdout_dataset
from run_c10s_f5_m1_dev_pilot import (
    F5_CELLS,
    K_PER_CELL as M1_K_PER_CELL,
    BOOTSTRAP_B as M1_BOOTSTRAP_B,
    SEED_NAMESPACE as M1_SEED_NAMESPACE,
    SCHEDULE_ID as M1_SCHEDULE_ID,
    derive_m1_seed,
    historical_seed_roster,
)
from c10s_f5_functional_refit_bootstrap import _replicate_seed
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate
from c10s_f5_component_profile_score import f5_component_profile_lr_statistic

PILOT_ID = "C10S_F5_POINTWISE_LR_DEVELOPMENT_STRESS_001"
SCHEDULE_ID = "C10S_F5_POINTWISE_LR_DEV_STRESS_SEEDS_1.0"
SEED_NAMESPACE = "c10s_f5_pointwise_lr_dev_stress_v1"
K_PER_CELL = 3
TARGETS = {"W": Fraction(1, 5), "B": Fraction(1, 20)}
WIDTH = Fraction(1, 2**8)
SOURCE_REVISION = os.environ.get("GITHUB_SHA", "unknown")


class StressPilotError(RuntimeError):
    pass


def derive_stress_seed(cell_id: str, index: int) -> int:
    if cell_id not in F5_CELLS or type(index) is not int or index < 0:
        raise StressPilotError("INVALID_STRESS_SEED_CELL_OR_INDEX")
    payload = f"{SCHEDULE_ID}|{SEED_NAMESPACE}|dataset|{cell_id}|{index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def _executed_m1_seed_values() -> set[int]:
    values: set[int] = set()
    for cell in F5_CELLS:
        for index in range(M1_K_PER_CELL):
            dataset_seed = derive_m1_seed("dataset", cell, index)
            bootstrap_seed = derive_m1_seed("bootstrap", cell, index)
            values.add(dataset_seed)
            values.add(bootstrap_seed)
            values.update(_replicate_seed(bootstrap_seed, b) for b in range(M1_BOOTSTRAP_B))
    return values


def build_seed_audit() -> tuple[list[tuple[str, int, int]], dict]:
    historical = historical_seed_roster()
    historical.update(_executed_m1_seed_values())
    rows = []
    new_values = []
    for cell in F5_CELLS:
        for index in range(K_PER_CELL):
            seed = derive_stress_seed(cell, index)
            rows.append((cell, index, seed))
            new_values.append(seed)
    if len(new_values) != len(set(new_values)):
        raise StressPilotError("NEW_STRESS_SEED_COLLISION")
    collisions = sorted(set(new_values).intersection(historical))
    if collisions:
        raise StressPilotError(f"HISTORICAL_STRESS_SEED_COLLISION:{collisions[:5]}")
    audit = {
        "status": "PASS",
        "historical_unique_seed_values_checked": len(historical),
        "new_seed_values_checked": len(new_values),
        "new_unique_seed_values": len(set(new_values)),
        "collision_count": 0,
        "schedule_id": SCHEDULE_ID,
        "seed_namespace": SEED_NAMESPACE,
        "m1_schedule_reconstructed": M1_SCHEDULE_ID,
        "m1_namespace_reconstructed": M1_SEED_NAMESPACE,
    }
    return rows, audit


def _fraction_pair(bounds):
    if bounds is None or len(bounds) != 2:
        return None
    return [{
        "exact": {
            "numerator_hex": ("-" if value.numerator < 0 else "") + hex(abs(value.numerator)),
            "denominator_hex": hex(value.denominator),
        },
        "approx_decimal": format(float(value), ".16g"),
        "numerator_bits": abs(value.numerator).bit_length(),
        "denominator_bits": value.denominator.bit_length(),
    } if isinstance(value, Fraction) else {
        "exact": str(value),
        "approx_decimal": str(value),
        "numerator_bits": None,
        "denominator_bits": None,
    } for value in bounds]


def _profile_summary(result: dict, elapsed: float) -> dict:
    profile = result.get("profile") or {}
    root_set = profile.get("root_set")
    root_status = getattr(root_set, "status", None)
    root_count = len(getattr(root_set, "roots", ()) or ())
    bounds = result.get("lr_statistic_bounds")
    return {
        "status": result.get("status"),
        "component": result.get("component"),
        "target": str(result.get("target")),
        "global_mle_status": result.get("global_mle_status"),
        "lr_statistic_bounds": _fraction_pair(bounds),
        "profile_status": profile.get("status"),
        "candidate_count": profile.get("candidate_count"),
        "interior_stationary_count": profile.get("interior_stationary_count"),
        "root_isolation_status": root_status,
        "root_count": root_count,
        "elapsed_seconds": round(elapsed, 6),
    }


def _append_event(path: Path, event: str, **fields) -> None:
    record = {
        "event": event,
        "utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        **fields,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True, allow_nan=False) + "\\n")
        stream.flush()


def _write_checkpoint(path: Path, *, source_revision: str, seed_audit: dict,
                      results: list, completed_stage: str, complete: bool) -> None:
    payload = {
        "schema": "C10S-F5-POINTWISE-LR-DEV-STRESS-CHECKPOINT-1.0",
        "pilot_id": PILOT_ID,
        "source_revision": source_revision,
        "scope": "DEVELOPMENT_ONLY_POINTWISE_LR_DIAGNOSTIC_NOT_CALIBRATION_NOT_CONFIRMATORY",
        "seed_collision_audit": seed_audit,
        "completed_stage": completed_stage,
        "complete": complete,
        "completed_datasets": len(results),
        "datasets": results,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def run_stress(
    output_path: Path, *, progress_path: Path, checkpoint_path: Path,
    cell_filter: str | None = None, component_filter: str | None = None,
) -> dict:
    import faulthandler
    import sys

    if len(SOURCE_REVISION) != 40 or any(c not in "0123456789abcdef" for c in SOURCE_REVISION):
        raise StressPilotError("EXACT_GITHUB_SOURCE_REVISION_REQUIRED")
    if cell_filter is not None and cell_filter not in F5_CELLS:
        raise StressPilotError("UNKNOWN_SINGLE_CASE_CELL")
    if component_filter is not None and component_filter not in TARGETS:
        raise StressPilotError("UNKNOWN_SINGLE_CASE_COMPONENT")

    seed_rows, seed_audit = build_seed_audit()
    specs = {spec.cell_id: spec for spec in tier_a_specs()}
    selected = [
        item for item in seed_rows
        if (cell_filter is None or item[0] == cell_filter)
    ]
    if cell_filter is not None:
        selected = selected[:1]
    results = []
    root_progress_path = progress_path.with_suffix(progress_path.suffix + ".roots.jsonl")
    os.environ["TGCV_C10S_ROOT_PROGRESS_PATH"] = str(root_progress_path)
    faulthandler.enable(file=sys.stderr)
    faulthandler.dump_traceback_later(60, repeat=True, file=sys.stderr)
    _append_event(
        progress_path, "RUN_START", source_revision=SOURCE_REVISION,
        selected_datasets=len(selected), selected_components=(
            [component_filter] if component_filter else list(TARGETS)
        ), seed_collision_audit=seed_audit,
    )
    _write_checkpoint(
        checkpoint_path, source_revision=SOURCE_REVISION, seed_audit=seed_audit,
        results=results, completed_stage="SEED_AUDIT", complete=False,
    )

    try:
        for cell, index, seed in selected:
            spec = specs[cell]
            dataset_started = perf_counter()
            _append_event(progress_path, "DATASET_START", cell_id=cell, dataset_index=index, seed=seed)
            rows = generate_holdout_dataset(spec, index, seed_override=seed)
            counts = [sum(int(value) for value in row) for row in rows]
            histogram = dict(sorted(Counter(counts).items()))
            rows_digest = hashlib.sha256(
                json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()
            ).hexdigest()
            _append_event(
                progress_path, "DATASET_COMPLETE", cell_id=cell,
                dataset_index=index, rows_sha256=rows_digest,
                generation_elapsed_seconds=round(perf_counter() - dataset_started, 6),
                distinct_count_bins=len(histogram),
            )

            _append_event(progress_path, "GLOBAL_CERTIFICATE_START", cell_id=cell, dataset_index=index)
            certificate_started = perf_counter()
            certificate = beta_binomial_global_mle_certificate(
                spec.r, histogram, max_refinements=1, projection_bits=12,
                max_projection_depth=40, max_lift_intervals=100,
                max_lift_depth=20, max_mu_depth=10,
                source_revision=SOURCE_REVISION,
            )
            certificate_elapsed = perf_counter() - certificate_started
            _append_event(
                progress_path, "GLOBAL_CERTIFICATE_COMPLETE", cell_id=cell,
                dataset_index=index, status=certificate.get("status"),
                elapsed_seconds=round(certificate_elapsed, 6),
            )

            component_results = {}
            components = [component_filter] if component_filter else list(TARGETS)
            for component in components:
                target = TARGETS[component]
                _append_event(
                    progress_path, "PROFILE_START", cell_id=cell,
                    dataset_index=index, component=component, target=str(target),
                )
                profile_started = perf_counter()
                result = f5_component_profile_lr_statistic(
                    spec.r, histogram, component=component, target=target,
                    global_certificate=certificate,
                    root_isolation_width=WIDTH,
                    max_depth=140, max_intervals=5000, log_series_terms=80,
                )
                summary = _profile_summary(result, perf_counter() - profile_started)
                component_results[component] = summary
                _append_event(
                    progress_path, "PROFILE_COMPLETE", cell_id=cell,
                    dataset_index=index, component=component,
                    status=summary.get("status"),
                    root_isolation_status=summary.get("root_isolation_status"),
                    elapsed_seconds=summary.get("elapsed_seconds"),
                )
                partial_dataset = {
                    "cell_id": cell, "dataset_index": index, "dataset_seed": seed,
                    "counts": counts, "count_histogram": histogram,
                    "rows_sha256": rows_digest,
                    "global_certificate_status": certificate.get("status"),
                    "global_certificate_elapsed_seconds": round(certificate_elapsed, 6),
                    "components": dict(component_results),
                }
                _write_checkpoint(
                    checkpoint_path, source_revision=SOURCE_REVISION,
                    seed_audit=seed_audit, results=results + [partial_dataset],
                    completed_stage=f"{cell}:{index}:{component}", complete=False,
                )

            results.append({
                "cell_id": cell, "dataset_index": index, "dataset_seed": seed,
                "counts": counts, "count_histogram": histogram,
                "rows_sha256": rows_digest,
                "global_certificate_status": certificate.get("status"),
                "global_certificate_refinement_history": [
                    {
                        "refinement": item.get("refinement"),
                        "projection_width": str(item.get("projection_width")),
                        "census_status": item.get("census_status"),
                    }
                    for item in certificate.get("refinement_history", [])
                ],
                "global_certificate_elapsed_seconds": round(certificate_elapsed, 6),
                "dataset_generation_elapsed_seconds": round(perf_counter() - dataset_started - certificate_elapsed, 6),
                "components": component_results,
            })
            _write_checkpoint(
                checkpoint_path, source_revision=SOURCE_REVISION,
                seed_audit=seed_audit, results=results,
                completed_stage=f"{cell}:{index}:DATASET_COMPLETE", complete=False,
            )

        summaries = {}
        for cell in F5_CELLS:
            cell_rows = [item for item in results if item["cell_id"] == cell]
            if not cell_rows:
                continue
            summaries[cell] = {}
            for component in ( [component_filter] if component_filter else list(TARGETS) ):
                items = [
                    item["components"][component] for item in cell_rows
                    if component in item["components"]
                ]
                enclosed = [item for item in items if item["status"] == "LR_STATISTIC_ENCLOSED"]
                midpoints = [
                    (float(item["lr_statistic_bounds"][0]["approx_decimal"])
                     + float(item["lr_statistic_bounds"][1]["approx_decimal"])) / 2
                    for item in enclosed
                ]
                summaries[cell][component] = {
                    "profile_evaluations": len(items),
                    "lr_enclosed_count": len(enclosed),
                    "typed_status_counts": dict(sorted(Counter(item["status"] for item in items).items())),
                    "median_lr_midpoint_descriptive": median(midpoints) if midpoints else None,
                    "lr_midpoint_range_descriptive": [min(midpoints), max(midpoints)] if midpoints else None,
                    "mean_runtime_seconds": sum(item["elapsed_seconds"] for item in items) / len(items),
                }

        payload = {
            "schema": "C10S-F5-POINTWISE-LR-DEV-STRESS-1.0",
            "pilot_id": PILOT_ID,
            "source_revision": SOURCE_REVISION,
            "scope": "DEVELOPMENT_ONLY_POINTWISE_LR_DIAGNOSTIC_NOT_CALIBRATION_NOT_CONFIRMATORY",
            "schedule_id": SCHEDULE_ID,
            "seed_namespace": SEED_NAMESPACE,
            "k_per_cell": K_PER_CELL,
            "selected_cell": cell_filter,
            "selected_component": component_filter,
            "targets": {key: str(value) for key, value in TARGETS.items()},
            "root_isolation_width": str(WIDTH),
            "global_certificate_budgets": {
                "max_refinements": 1, "projection_bits": 12,
                "max_projection_depth": 40, "max_lift_intervals": 100,
                "max_lift_depth": 20, "max_mu_depth": 10,
            },
            "seed_collision_audit": seed_audit,
            "coverage_adjudication": "NOT_PERFORMED",
            "lr_cutoff_calibration": "NOT_PERFORMED",
            "confidence_set_inversion": "NOT_PERFORMED",
            "summaries": summaries,
            "datasets": results,
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\\n",
            encoding="utf-8",
        )
        _write_checkpoint(
            checkpoint_path, source_revision=SOURCE_REVISION, seed_audit=seed_audit,
            results=results, completed_stage="RUN_COMPLETE", complete=True,
        )
        _append_event(progress_path, "RUN_COMPLETE", completed_datasets=len(results))
        return payload
    except BaseException as exc:
        _append_event(
            progress_path, "RUN_ABORTED", exception_type=type(exc).__name__,
            exception=str(exc),
        )
        raise
    finally:
        faulthandler.cancel_dump_traceback_later()
        os.environ.pop("TGCV_C10S_ROOT_PROGRESS_PATH", None)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-development-stress", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--progress", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--single-case", choices=F5_CELLS)
    parser.add_argument("--component", choices=tuple(TARGETS))
    args = parser.parse_args()
    if not args.execute_development_stress:
        raise StressPilotError("EXPLICIT_DEVELOPMENT_STRESS_FLAG_REQUIRED")
    if args.component and not args.single_case:
        raise StressPilotError("COMPONENT_FILTER_REQUIRES_SINGLE_CASE")
    result = run_stress(
        args.output, progress_path=args.progress, checkpoint_path=args.checkpoint,
        cell_filter=args.single_case, component_filter=args.component,
    )
    print(json.dumps({
        "schema": result["schema"],
        "source_revision": result["source_revision"],
        "seed_collision_audit": result["seed_collision_audit"],
        "summaries": result["summaries"],
        "coverage_adjudication": result["coverage_adjudication"],
        "lr_cutoff_calibration": result["lr_cutoff_calibration"],
        "confidence_set_inversion": result["confidence_set_inversion"],
    }, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
