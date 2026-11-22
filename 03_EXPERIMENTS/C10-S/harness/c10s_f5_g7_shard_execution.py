"""Deterministic shard execution and exact re-adjudication for G7 primary/replay banks."""
from __future__ import annotations

import hashlib
import json
from typing import Any

import run_c10s_f5_g7_tiera_calibration as g7
from c10s_nested_mr_comparative_inference_engine import (
    CandidateOutput,
    DatasetComparison,
    TruthTargets,
    adjudicate_matched_datasets,
)
from c10s_variance_comparison_interface import VarianceComparisonResult

SHARD_SCHEMA = "TGCV-C10S-F5-G7-SHARD-002"


def _restore_comparison(raw: dict[str, Any]) -> VarianceComparisonResult:
    return VarianceComparisonResult(
        method_id=raw["method_id"],
        within_estimate=raw["within_estimate"],
        observed_world_variance=raw["observed_world_variance"],
        between_estimate_raw=raw["between_estimate_raw"],
        mcse_estimate=raw["mcse_estimate"],
        within_interval=tuple(raw["within_interval"]) if raw["within_interval"] is not None else None,
        between_interval=tuple(raw["between_interval"]) if raw["between_interval"] is not None else None,
        mcse_interval=tuple(raw["mcse_interval"]) if raw["mcse_interval"] is not None else None,
        boundary_flags=tuple(raw["boundary_flags"]),
        abstention_reason=raw["abstention_reason"],
        provenance=tuple(tuple(item) for item in raw["provenance"]),
    )


def adjudicate_serialized_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Rehydrate shard records and apply the unchanged full-bank adjudicator once."""
    if not records:
        raise ValueError("G7_SERIALIZED_RECORDS_REQUIRED")
    comparisons = []
    truths = []
    seen = set()
    for record in records:
        dataset_id = record.get("dataset_id")
        if not isinstance(dataset_id, str) or dataset_id in seen:
            raise ValueError("G7_SERIALIZED_DATASET_ID_MISSING_OR_DUPLICATE")
        seen.add(dataset_id)
    for record in records:
        raw = record["comparison"]
        candidates = tuple(
            CandidateOutput(
                method_id=item["method_id"],
                comparison=_restore_comparison(item["comparison"]),
                diagnostics=tuple(tuple(pair) for pair in item.get("diagnostics", [])),
            )
            for item in raw["candidates"]
        )
        comparisons.append(DatasetComparison(
            engine_id=raw["engine_id"],
            dataset_id=raw["dataset_id"],
            family=raw["family"],
            input_m=raw["input_m"],
            input_r=raw["input_r"],
            target_m=raw["target_m"],
            target_r=raw["target_r"],
            baseline=_restore_comparison(raw["baseline"]),
            candidates=candidates,
            unavailable_methods=tuple(raw["unavailable_methods"]),
        ))
        truth = record["truth"]
        truths.append(TruthTargets(
            dataset_id=truth["dataset_id"],
            within=truth["within"],
            between=truth["between"],
            mcse=truth["mcse"],
        ))
    if len(comparisons) != len(truths):
        raise ValueError("G7_SERIALIZED_COMPARISON_TRUTH_DENOMINATOR_MISMATCH")
    metrics = adjudicate_matched_datasets(comparisons, truths)
    return [
        g7._jsonable(metric)
        for metric in metrics
        if metric.target in {"within", "between"}
    ]


def records_digest(records: list[dict[str, Any]]) -> str:
    payload = json.dumps(
        records, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def diagnostics_digest(diagnostics: list[dict[str, Any]]) -> str:
    """Hash raw optimizer/operational diagnostics independently of scientific records."""
    payload = json.dumps(
        diagnostics, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run_cell_shard(
    spec,
    *,
    phase: str,
    replicate_start: int,
    replicate_count: int,
    c0_b: int,
    c5_b: int,
    source_commit: str,
) -> dict[str, Any]:
    """Execute one frozen global replicate-index range; no partial adjudication."""
    if phase not in {"primary", "replay"}:
        raise ValueError("G7_SHARD_PHASE_MUST_BE_PRIMARY_OR_REPLAY")
    if spec.family != "F5" or spec.cell_id not in g7.EXPECTED_CELLS:
        raise ValueError("G7_SHARD_ACCEPTS_ONLY_FROZEN_F5_CELLS")
    if type(replicate_start) is not int or replicate_start < 0:
        raise ValueError("G7_SHARD_REPLICATE_START_INVALID")
    if type(replicate_count) is not int or replicate_count < 1:
        raise ValueError("G7_SHARD_REPLICATE_COUNT_INVALID")
    if replicate_start + replicate_count > g7.K_PER_CELL:
        raise ValueError("G7_SHARD_RANGE_EXCEEDS_FROZEN_K")
    if type(c0_b) is not int or c0_b != g7.C0_B or type(c5_b) is not int or c5_b != g7.C5_B:
        raise ValueError("G7_SHARD_BOOTSTRAP_REPLICATES_MUST_MATCH_FROZEN_PROTOCOL")
    if not isinstance(source_commit, str) or len(source_commit) != 40:
        raise ValueError("G7_SHARD_SOURCE_COMMIT_MUST_BE_FULL_SHA")

    records = []
    optimizer_diagnostics = []
    seen_seeds = {name: set() for name in ("dataset", "C0_bootstrap", "C5_bootstrap")}
    for replicate in range(replicate_start, replicate_start + replicate_count):
        dataset_id = (
            f"{g7.PROTOCOL_VERSION}:{g7.HOLDOUT_NAMESPACE}:"
            f"{spec.cell_id}:{replicate:06d}"
        )
        seeds = {
            name: g7.derive_seed(g7.HOLDOUT_NAMESPACE, name, spec.cell_id, replicate)
            for name in seen_seeds
        }
        for name, value in seeds.items():
            if value in seen_seeds[name]:
                raise ValueError(f"G7_SHARD_DUPLICATE_{name.upper()}_SEED")
            seen_seeds[name].add(value)
        rows = g7.generate_holdout_dataset(
            spec, replicate, seed_override=seeds["dataset"]
        )
        comparison = g7.compare_dataset(
            rows,
            dataset_id=dataset_id,
            family="F5",
            target_m=spec.m,
            target_r=spec.r,
            baseline_bootstrap_replicates=c0_b,
            baseline_bootstrap_seed=seeds["C0_bootstrap"],
            confidence_level=g7.CONFIDENCE_LEVEL,
            bootstrap_replicates=c5_b,
            bootstrap_seed=seeds["C5_bootstrap"],
            include_profile_diagnostics=False,
            require_f5_global_mle_certificate=True,
        )
        roster = {comparison.baseline.method_id}
        roster.update(candidate.method_id for candidate in comparison.candidates)
        if roster != set(g7.IMPLEMENTED_METHODS["F5"]):
            raise ValueError("G7_SHARD_METHOD_ROSTER_MISMATCH")
        if (
            comparison.dataset_id != dataset_id
            or (comparison.input_m, comparison.input_r) != (spec.m, spec.r)
        ):
            raise ValueError("G7_SHARD_DATASET_OR_DESIGN_IDENTITY_MISMATCH")
        truth = g7._truth(spec, dataset_id)
        comparison_payload = g7._jsonable(comparison)
        for candidate in comparison_payload["candidates"]:
            optimizer_diagnostics.append({
                "dataset_id": dataset_id,
                "method_id": candidate["method_id"],
                "items": candidate.get("diagnostics", []),
            })
            candidate["diagnostics"] = []
        records.append({
            "dataset_id": dataset_id,
            "dataset_seed": seeds["dataset"],
            "C0_bootstrap_seed": seeds["C0_bootstrap"],
            "C5_bootstrap_seed": seeds["C5_bootstrap"],
            "rows_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()
            ).hexdigest(),
            "comparison": comparison_payload,
            "truth": g7._jsonable(truth),
        })

    if len(records) != replicate_count or len({row["dataset_id"] for row in records}) != replicate_count:
        raise ValueError("G7_SHARD_DATASET_DENOMINATOR_INCOMPLETE")
    return {
        "schema": SHARD_SCHEMA,
        "phase": phase,
        "protocol_id": g7.PROTOCOL_ID,
        "protocol_version": g7.PROTOCOL_VERSION,
        "seed_schedule_id": g7.SEED_SCHEDULE_ID,
        "seed_namespace": g7.HOLDOUT_NAMESPACE,
        "source_commit": source_commit,
        "cell_id": spec.cell_id,
        "cell": spec.manifest(),
        "replicate_start": replicate_start,
        "replicate_count": replicate_count,
        "datasets_completed": len(records),
        "method_roster": sorted(g7.IMPLEMENTED_METHODS["F5"]),
        "records_digest": records_digest(records),
        "records": records,
        "optimizer_diagnostics": optimizer_diagnostics,
        "optimizer_diagnostics_digest": diagnostics_digest(optimizer_diagnostics),
        "coverage_adjudication": "NOT_PERFORMED_SHARD_LEVEL",
    }
