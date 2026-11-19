"""Thin orchestration runner for the frozen C0/C1/C5 independent holdout.

This module does not authorize or launch a numerical holdout by itself. Its
callable functions are exercised with small deterministic contract fixtures;
the production CLI remains fail-closed until a dedicated authorization layer
is added and bound to the frozen protocol/code/workflow.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from c10s_nested_mr_fixtures import FixtureSpec, tier_a_specs
from c10s_nested_mr_comparative_inference_engine import (
    IMPLEMENTED_METHODS,
    TruthTargets,
    adjudicate_matched_datasets,
    compare_dataset,
)

PROTOCOL_ID = "C10S-NESTED-MR-COMPARATIVE-HOLDOUT-PROTOCOL-001"
PROTOCOL_VERSION = "1.0"
PROTOCOL_PATH = (
    "03_EXPERIMENTS/C10-S/diagnostics/"
    "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_PROTOCOL_001.md"
)
SEED_SCHEDULE_ID = "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0"
SEED_NAMESPACE = "c10s_nested_mr_comparative_holdout_v1"
K_PER_CELL = 1000
C0_BOOTSTRAP_B = 1000
C5_BOOTSTRAP_B = 1000
CONFIDENCE_LEVEL = 0.95
EXPECTED_CELLS = (
    "F1_balanced_M10_R5", "F1_balanced_M30_R20",
    "F1_high_between_M10_R5", "F1_high_between_M30_R20",
    "F1_low_between_M10_R5", "F1_low_between_M30_R20",
    "F5_beta22_M10_R5", "F5_beta22_M30_R20",
)


class HoldoutRunnerError(RuntimeError):
    pass


def derive_holdout_seed(namespace: str, cell_id: str, replicate_index: int) -> int:
    """Stable SHA-256-derived uint64; separate namespaces per random stream."""
    if namespace not in {"dataset", "C0_bootstrap", "C5_bootstrap"}:
        raise HoldoutRunnerError("UNRECOGNIZED_HOLDOUT_SEED_NAMESPACE")
    if not isinstance(cell_id, str) or not cell_id:
        raise HoldoutRunnerError("CELL_ID_REQUIRED")
    if type(replicate_index) is not int or replicate_index < 0:
        raise HoldoutRunnerError("REPLICATE_INDEX_MUST_BE_NONNEGATIVE_INTEGER")
    payload = (
        f"{SEED_SCHEDULE_ID}|{SEED_NAMESPACE}|{namespace}|"
        f"{cell_id}|{replicate_index}"
    ).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def _validate_spec(spec: FixtureSpec) -> None:
    if not spec.stochastic or spec.family not in {"F1", "F5"}:
        raise HoldoutRunnerError("HOLDOUT_ACCEPTS_ONLY_STOCHASTIC_F1_OR_F5_SPECS")
    if spec.m < 2 or spec.r < 2:
        raise HoldoutRunnerError("INVALID_MR_DESIGN")
    if spec.cell_id not in EXPECTED_CELLS:
        raise HoldoutRunnerError("CELL_NOT_IN_FROZEN_HOLDOUT_ROSTER")
    expected = {
        "F1_balanced_M10_R5": ("F1", 10, 5, 1.0, 1.0),
        "F1_balanced_M30_R20": ("F1", 30, 20, 1.0, 1.0),
        "F1_high_between_M10_R5": ("F1", 10, 5, 0.25, 2.0),
        "F1_high_between_M30_R20": ("F1", 30, 20, 0.25, 2.0),
        "F1_low_between_M10_R5": ("F1", 10, 5, 1.0, 0.05),
        "F1_low_between_M30_R20": ("F1", 30, 20, 1.0, 0.05),
        "F5_beta22_M10_R5": ("F5", 10, 5, 0.20, 0.05),
        "F5_beta22_M30_R20": ("F5", 30, 20, 0.20, 0.05),
    }[spec.cell_id]
    actual = (spec.family, spec.m, spec.r, spec.true_within, spec.true_between)
    if actual != expected:
        raise HoldoutRunnerError("CELL_SPEC_DOES_NOT_MATCH_FROZEN_PROTOCOL")


def generate_holdout_dataset(
    spec: FixtureSpec, replicate_index: int,
) -> tuple[tuple[float, ...], ...]:
    """Generate one fresh dataset under the holdout-only seed namespace."""
    _validate_spec(spec)
    seed = derive_holdout_seed("dataset", spec.cell_id, replicate_index)
    outer_seq, inner_seq = np.random.SeedSequence(seed).spawn(2)
    outer_rng = np.random.Generator(np.random.PCG64(outer_seq))
    inner_rngs = [
        np.random.Generator(np.random.PCG64(s))
        for s in inner_seq.spawn(spec.m)
    ]
    params = dict(spec.parameters)
    if spec.family == "F1":
        worlds = outer_rng.normal(0.0, math.sqrt(spec.true_between), size=spec.m)
        matrix = np.vstack([
            worlds[i] + inner_rngs[i].normal(
                0.0, math.sqrt(spec.true_within), size=spec.r
            )
            for i in range(spec.m)
        ])
    elif spec.family == "F5":
        alpha, beta = float(params["alpha"]), float(params["beta"])
        world_probabilities = outer_rng.beta(alpha, beta, size=spec.m)
        matrix = np.vstack([
            inner_rngs[i].binomial(1, world_probabilities[i], size=spec.r)
            for i in range(spec.m)
        ])
    else:  # guarded above; kept fail-closed
        raise HoldoutRunnerError("UNSUPPORTED_HOLDOUT_FAMILY")
    return tuple(tuple(float(x) for x in row) for row in matrix)


def _truth(spec: FixtureSpec, dataset_id: str) -> TruthTargets:
    # The independent analytical fixture truth, never fitted candidate output.
    mcse = math.sqrt(
        spec.true_between / spec.m
        + spec.true_within / (spec.m * spec.r)
    )
    return TruthTargets(
        dataset_id=dataset_id,
        within=float(spec.true_within),
        between=float(spec.true_between),
        mcse=mcse,
    )


def _jsonable(value: Any) -> Any:
    if hasattr(value, "__dataclass_fields__"):
        return {key: _jsonable(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    return value


def run_comparative_cell(
    spec: FixtureSpec, *, k: int = K_PER_CELL,
    c0_b: int = C0_BOOTSTRAP_B, c5_b: int = C5_BOOTSTRAP_B,
) -> dict[str, Any]:
    """Generate once, compare matched methods, and adjudicate one frozen cell.

    k/b overrides exist for deterministic unit tests only. Production invocation
    is expected to use the protocol constants and the authorization wrapper.
    """
    _validate_spec(spec)
    if type(k) is not int or k < 1 or type(c0_b) is not int or c0_b < 100:
        raise HoldoutRunnerError("INVALID_K_OR_C0_B")
    if type(c5_b) is not int or c5_b < 100:
        raise HoldoutRunnerError("INVALID_C5_B")
    family = spec.family
    if family not in IMPLEMENTED_METHODS:
        raise HoldoutRunnerError("NO_IMPLEMENTED_COMPARISON_FOR_FAMILY")

    comparisons = []
    truths = []
    records = []
    seen_dataset_seeds: set[int] = set()
    seen_c0_seeds: set[int] = set()
    seen_c5_seeds: set[int] = set()
    for replicate in range(k):
        dataset_id = (
            f"{PROTOCOL_VERSION}:{spec.cell_id}:"
            f"{replicate:06d}"
        )
        dataset_seed = derive_holdout_seed("dataset", spec.cell_id, replicate)
        c0_seed = derive_holdout_seed("C0_bootstrap", spec.cell_id, replicate)
        c5_seed = derive_holdout_seed("C5_bootstrap", spec.cell_id, replicate)
        if dataset_seed in seen_dataset_seeds or c0_seed in seen_c0_seeds:
            raise HoldoutRunnerError("DUPLICATE_DATASET_OR_C0_SEED")
        if family == "F5" and c5_seed in seen_c5_seeds:
            raise HoldoutRunnerError("DUPLICATE_C5_SEED")
        seen_dataset_seeds.add(dataset_seed)
        seen_c0_seeds.add(c0_seed)
        if family == "F5":
            seen_c5_seeds.add(c5_seed)

        rows = generate_holdout_dataset(spec, replicate)
        comparison = compare_dataset(
            rows,
            dataset_id=dataset_id,
            family=family,
            target_m=spec.m,
            target_r=spec.r,
            baseline_bootstrap_replicates=c0_b,
            baseline_bootstrap_seed=c0_seed,
            confidence_level=CONFIDENCE_LEVEL,
            bootstrap_replicates=c5_b if family == "F5" else None,
            bootstrap_seed=c5_seed if family == "F5" else None,
            include_profile_diagnostics=False,
        )
        if comparison.dataset_id != dataset_id:
            raise HoldoutRunnerError("COMPARATOR_CHANGED_DATASET_ID")
        if comparison.input_m != spec.m or comparison.input_r != spec.r:
            raise HoldoutRunnerError("COMPARATOR_INPUT_DESIGN_MISMATCH")
        if (comparison.target_m, comparison.target_r) != (spec.m, spec.r):
            raise HoldoutRunnerError("COMPARATOR_TARGET_DESIGN_MISMATCH")
        roster = {comparison.baseline.method_id}
        roster.update(item.method_id for item in comparison.candidates)
        if roster != set(IMPLEMENTED_METHODS[family]):
            raise HoldoutRunnerError("COMPARATOR_METHOD_ROSTER_MISMATCH")
        comparisons.append(comparison)
        truths.append(_truth(spec, dataset_id))
        records.append({
            "dataset_id": dataset_id,
            "dataset_seed": dataset_seed,
            "C0_bootstrap_seed": c0_seed,
            "C5_bootstrap_seed": c5_seed if family == "F5" else None,
            "rows_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()
            ).hexdigest(),
            "comparison": _jsonable(comparison),
            "truth": _jsonable(truths[-1]),
        })

    metrics = adjudicate_matched_datasets(comparisons, truths)
    if len(records) != k or len({row["dataset_id"] for row in records}) != k:
        raise HoldoutRunnerError("INCOMPLETE_OR_DUPLICATE_DATASET_DENOMINATOR")
    return {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "cell": spec.manifest(),
        "datasets_completed": len(records),
        "method_roster": sorted(IMPLEMENTED_METHODS[family]),
        "records": records,
        "metrics": [_jsonable(metric) for metric in metrics],
        "mcse_adjudication": "NON_CONFIRMATORY_DIAGNOSTIC_ONLY",
        "status": "COMPUTED_NOT_AUTHORIZED_NOT_EXECUTED_AS_HOLDOUT",
    }


def run_holdout(
    *, specs: Iterable[FixtureSpec] | None = None,
    k: int = K_PER_CELL, c0_b: int = C0_BOOTSTRAP_B,
    c5_b: int = C5_BOOTSTRAP_B,
) -> dict[str, Any]:
    """In-memory orchestration for all eight cells; no files/workflow launched."""
    selected = tuple(tier_a_specs() if specs is None else specs)
    by_id = {spec.cell_id: spec for spec in selected}
    if len(by_id) != len(selected):
        raise HoldoutRunnerError("DUPLICATE_CELL_SPEC")
    selected = tuple(by_id.get(cell_id) for cell_id in EXPECTED_CELLS)
    if any(spec is None for spec in selected):
        raise HoldoutRunnerError("HOLDOUT_REQUIRES_EXACT_ORDERED_EIGHT_CELL_ROSTER")
    ids = tuple(spec.cell_id for spec in selected)
    if ids != EXPECTED_CELLS:
        raise HoldoutRunnerError("HOLDOUT_REQUIRES_EXACT_ORDERED_EIGHT_CELL_ROSTER")
    cells = [
        run_comparative_cell(spec, k=k, c0_b=c0_b, c5_b=c5_b)
        for spec in selected
    ]
    return {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "k_per_cell": k,
        "c0_bootstrap_replicates": c0_b,
        "c5_bootstrap_replicates": c5_b,
        "cell_count": len(cells),
        "total_datasets": sum(cell["datasets_completed"] for cell in cells),
        "cells": cells,
        "status": "COMPUTED_NOT_AUTHORIZED_NOT_EXECUTED_AS_HOLDOUT",
    }


def write_result_bundle(result: dict[str, Any], output_dir: Path) -> dict[str, str]:
    """Write deterministic JSON records and a content-hash manifest."""
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    result_path = output_dir / "comparative_holdout_result.json"
    result_path.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    manifest = {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "result_file": result_path.name,
        "result_sha256": digest,
        "status": "COMPUTED_NOT_AUTHORIZED_NOT_EXECUTED_AS_HOLDOUT",
    }
    manifest_payload = json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    manifest_path = output_dir / "run_manifest.json"
    manifest_path.write_text(manifest_payload, encoding="utf-8")
    return {
        "result_sha256": digest,
        "manifest_sha256": hashlib.sha256(manifest_payload.encode()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.parse_args()
    raise SystemExit(
        "FAIL_CLOSED: numerical holdout execution requires a separate approved "
        "authorization wrapper bound to protocol hash, code commit and workflow."
    )


if __name__ == "__main__":
    raise SystemExit(main())
