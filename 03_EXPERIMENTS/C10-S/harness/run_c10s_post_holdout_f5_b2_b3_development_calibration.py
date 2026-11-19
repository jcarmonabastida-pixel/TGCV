"""Authorized F5 B2/B3 development calibration runner.

This runner implements only the frozen F5 beta22 within/raw-between study.
It does not implement or score an F5 MCSE interval, does not run F1, Tier B,
a confirmatory holdout, or causal C10 scientific execution.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
import os
import platform
from pathlib import Path
import resource
import sys
import time
from typing import Any

import numpy as np
from scipy.stats import binom

from c10s_nested_mr_fixtures import tier_a_specs
from c10s_nested_mr_comparative_inference_engine import (
    IMPLEMENTED_METHODS,
    adjudicate_matched_datasets,
    compare_dataset,
)
from c10s_fitted_beta_binomial_bootstrap import fitted_beta_binomial_parametric_bootstrap
from run_c10s_nested_mr_comparative_holdout import (
    _jsonable,
    _truth,
    generate_holdout_dataset,
)

RUN_ID = "C10S-POST-HOLDOUT-F5-B2-B3-DEVELOPMENT-CALIBRATION-001"
SEED_SCHEDULE_ID = "C10S_POST_HOLDOUT_F1_F5_DEV_CAL_SEEDS_1.0"
SEED_NAMESPACE = "c10s_post_holdout_f1_f5_dev_cal_v1"
EXPECTED_CELLS = ("F5_beta22_M10_R5", "F5_beta22_M30_R20")
K_CALIBRATION = 5000
K_VALIDATION = 5000
C0_B = 1000
C5_B = 1000
B3_SELECTED_PER_CELL = 250
B3_B1000 = 1000
B3_B4000 = 4000
CONFIDENCE_LEVEL = 0.95
SPEC_PATH = "03_EXPERIMENTS/C10-S/diagnostics/C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md"
LOCK_PATH = "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock"
HISTORICAL_CELLS = tuple(spec.cell_id for spec in tier_a_specs())
MCSE_SCOPE = "EXPLICIT_ABSTENTION_OUT_OF_SCOPE_NOT_ADJUDICATED"


class F5DevelopmentCalibrationError(RuntimeError):
    """Invalid F5 development-bank design, provenance or execution state."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def derive_seed(stream: str, cell_id: str, replicate: int) -> int:
    allowed = {
        "f5_optimizer_calibration_dataset",
        "f5_optimizer_validation_dataset",
        "f5_c0_bootstrap",
        "f5_c5_bootstrap",
        "f5_endpoint_sensitivity_b1000",
        "f5_endpoint_sensitivity_b4000",
    }
    if stream not in allowed:
        raise F5DevelopmentCalibrationError("UNKNOWN_F5_DEVELOPMENT_SEED_STREAM")
    if cell_id not in EXPECTED_CELLS:
        raise F5DevelopmentCalibrationError("CELL_OUTSIDE_FROZEN_F5_ROSTER")
    if type(replicate) is not int or replicate < 0:
        raise F5DevelopmentCalibrationError("REPLICATE_MUST_BE_NONNEGATIVE_INTEGER")
    payload = (
        f"{SEED_SCHEDULE_ID}|{SEED_NAMESPACE}|{stream}|{cell_id}|{replicate}"
    ).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def _historical_seed_values() -> set[int]:
    """Reconstruct the previous Tier A, comparative holdout and preflight seeds."""
    values: set[int] = set()
    for cell_id in HISTORICAL_CELLS:
        for replicate in range(1000):
            for stream in ("fixture_dataset", "bootstrap"):
                payload = (
                    f"C10S_NESTED_MR_SEED_SCHEDULE_1.0|{stream}|"
                    f"{cell_id}|{replicate}"
                ).encode("utf-8")
                values.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
            holdout_prefix = (
                "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0|"
                "c10s_nested_mr_comparative_holdout_v1|"
            )
            for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
                payload = f"{holdout_prefix}{stream}|{cell_id}|{replicate}".encode()
                values.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
            old_prefix = "C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0|"
            for stream in ("dataset", "C0", "C5"):
                payload = f"{old_prefix}{stream}|{cell_id}|{replicate}".encode()
                values.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))

    # The separately authorized 100-dataset F1/F5 resource preflight.
    preflight_prefix = (
        "C10S_POST_HOLDOUT_F1_F5_DEV_PREFLIGHT_SEEDS_1.0|"
        "c10s_post_holdout_f1_f5_dev_preflight_v1|"
    )
    for cell_id in ("F1_balanced_M30_R20", "F5_beta22_M30_R20"):
        streams = ["dataset", "C0_bootstrap"]
        if cell_id.startswith("F5_"):
            streams.extend(("C5_bootstrap_B1000", "C5_bootstrap_B4000"))
        for replicate in range(100):
            for stream in streams:
                payload = f"{preflight_prefix}{stream}|{cell_id}|{replicate}".encode()
                values.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
    return values


def _new_seed_roster(
    *, k_calibration: int, k_validation: int, b3_selected_per_cell: int,
) -> list[tuple[int, str, str, int]]:
    roster: list[tuple[int, str, str, int]] = []
    for cell_id in EXPECTED_CELLS:
        for replicate in range(k_calibration):
            roster.append((derive_seed("f5_optimizer_calibration_dataset", cell_id, replicate),
                           "f5_optimizer_calibration_dataset", cell_id, replicate))
            roster.append((derive_seed("f5_c0_bootstrap", cell_id, replicate),
                           "f5_c0_bootstrap", cell_id, replicate))
            roster.append((derive_seed("f5_c5_bootstrap", cell_id, replicate),
                           "f5_c5_bootstrap", cell_id, replicate))
        for replicate in range(k_validation):
            roster.append((derive_seed("f5_optimizer_validation_dataset", cell_id, replicate),
                           "f5_optimizer_validation_dataset", cell_id, replicate))
            roster.append((derive_seed("f5_c0_bootstrap", cell_id, k_calibration + replicate),
                           "f5_c0_bootstrap_validation", cell_id, replicate))
            roster.append((derive_seed("f5_c5_bootstrap", cell_id, k_calibration + replicate),
                           "f5_c5_bootstrap_validation", cell_id, replicate))
        for replicate in range(b3_selected_per_cell):
            roster.append((derive_seed("f5_endpoint_sensitivity_b1000", cell_id, replicate),
                           "f5_endpoint_sensitivity_b1000", cell_id, replicate))
            roster.append((derive_seed("f5_endpoint_sensitivity_b4000", cell_id, replicate),
                           "f5_endpoint_sensitivity_b4000", cell_id, replicate))
    return roster


def validate_seed_separation(
    *, k_calibration: int = K_CALIBRATION,
    k_validation: int = K_VALIDATION,
    b3_selected_per_cell: int = B3_SELECTED_PER_CELL,
) -> dict[str, Any]:
    if any(type(value) is not int or value < 1 for value in (
        k_calibration, k_validation, b3_selected_per_cell,
    )):
        raise F5DevelopmentCalibrationError("BANK_SIZES_MUST_BE_POSITIVE_INTEGERS")
    if b3_selected_per_cell > k_calibration:
        raise F5DevelopmentCalibrationError("B3_SELECTION_EXCEEDS_CALIBRATION_BANK")
    historical = _historical_seed_values()
    roster = _new_seed_roster(
        k_calibration=k_calibration,
        k_validation=k_validation,
        b3_selected_per_cell=b3_selected_per_cell,
    )
    seen: dict[int, tuple[str, str, int]] = {}
    for value, stream, cell_id, replicate in roster:
        if value in historical:
            raise F5DevelopmentCalibrationError(
                f"NEW_SEED_COLLIDES_WITH_HISTORICAL:{stream}:{cell_id}:{replicate}"
            )
        previous = seen.get(value)
        if previous is not None:
            raise F5DevelopmentCalibrationError(
                f"NEW_SEED_COLLISION:{previous}:{(stream, cell_id, replicate)}"
            )
        seen[value] = (stream, cell_id, replicate)
    return {
        "status": "PASS",
        "historical_unique_seed_values_checked": len(historical),
        "new_seed_values_checked": len(roster),
        "new_unique_seed_values": len(seen),
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "seed_namespace": SEED_NAMESPACE,
        "historical_schedules": [
            "C10S_NESTED_MR_SEED_SCHEDULE_1.0",
            "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0",
            "C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0",
            "C10S_POST_HOLDOUT_F1_F5_DEV_PREFLIGHT_SEEDS_1.0",
        ],
    }


def _f5_specs():
    specs = {spec.cell_id: spec for spec in tier_a_specs() if spec.family == "F5"}
    if tuple(sorted(specs)) != tuple(sorted(EXPECTED_CELLS)):
        raise F5DevelopmentCalibrationError("FROZEN_F5_CELL_ROSTER_MISMATCH")
    for spec in specs.values():
        params = dict(spec.parameters)
        if (
            spec.family != "F5" or spec.distribution != "beta_binomial_world_probability"
            or params != {"alpha": 2, "beta": 2}
            or spec.true_within != 0.20 or spec.true_between != 0.05
        ):
            raise F5DevelopmentCalibrationError("F5_BETA22_DGP_MISMATCH")
    return tuple(specs[cell_id] for cell_id in EXPECTED_CELLS)


def dataset_id(bank: str, cell_id: str, replicate: int) -> str:
    if bank not in {"calibration", "validation"}:
        raise F5DevelopmentCalibrationError("UNKNOWN_F5_BANK")
    return f"{RUN_ID}:{bank}:{cell_id}:{replicate:05d}"


def _selection_digest(cell_id: str, dataset: str) -> str:
    payload = f"{SEED_SCHEDULE_ID}|B3_SELECTION|{cell_id}|{dataset}".encode()
    return hashlib.sha256(payload).hexdigest()


def select_b3_calibration_datasets(
    cell_id: str, calibration_dataset_ids: list[str], *, n: int = B3_SELECTED_PER_CELL,
) -> list[dict[str, str]]:
    if cell_id not in EXPECTED_CELLS or type(n) is not int or n < 1 or n > len(calibration_dataset_ids):
        raise F5DevelopmentCalibrationError("INVALID_B3_SELECTION_REQUEST")
    if len(set(calibration_dataset_ids)) != len(calibration_dataset_ids):
        raise F5DevelopmentCalibrationError("DUPLICATE_CALIBRATION_DATASET_IDS")
    ranked = sorted(
        ((_selection_digest(cell_id, value), value) for value in calibration_dataset_ids),
        key=lambda item: (item[0], item[1]),
    )
    return [
        {"dataset_id": value, "selection_sha256": digest}
        for digest, value in ranked[:n]
    ]


def _finite_summary(values: list[float]) -> dict[str, float | int | None]:
    finite = [float(value) for value in values if isinstance(value, (int, float)) and math.isfinite(value)]
    if not finite:
        return {"n": 0, "mean": None, "median": None, "q05": None, "q95": None}
    array = np.asarray(finite, dtype=float)
    return {
        "n": int(array.size),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "q05": float(np.quantile(array, 0.05)),
        "q95": float(np.quantile(array, 0.95)),
    }


def _optimizer_fields(comparison) -> dict[str, Any]:
    candidate = comparison.candidates[0]
    diagnostics = dict(candidate.diagnostics)
    raw = diagnostics.get("likelihood_optimizer_audit_json", "null")
    audit = json.loads(raw) if raw != "null" else None
    fit_status = diagnostics.get("fit_status", "FIT_STATUS_MISSING")
    failure_reason = diagnostics.get("failure_reason", "FAILURE_REASON_MISSING")
    derived: dict[str, Any] = {
        "fit_status": fit_status,
        "failure_reason": failure_reason,
        "optimizer_audit": audit,
    }
    if audit is None:
        derived["optimizer_status"] = "DIAGNOSTIC_UNAVAILABLE"
        return derived
    derived["optimizer_status"] = audit.get("status", "DIAGNOSTIC_STATUS_MISSING")
    eta = audit.get("selected_mean_logit")
    xi = audit.get("selected_log_concentration")
    if isinstance(eta, (int, float)) and isinstance(xi, (int, float)) and math.isfinite(eta) and math.isfinite(xi):
        mu = 1.0 / (1.0 + math.exp(-eta)) if eta >= 0 else math.exp(eta) / (1.0 + math.exp(eta))
        kappa = math.exp(xi)
        derived.update({
            "selected_mean_probability": mu,
            "selected_concentration": kappa,
            "selected_alpha": mu * kappa,
            "selected_beta": (1.0 - mu) * kappa,
        })
    else:
        derived.update({
            "selected_mean_probability": None,
            "selected_concentration": None,
            "selected_alpha": None,
            "selected_beta": None,
        })
    starts = audit.get("starts") or []
    distances = []
    for start in starts:
        for key in (
            "lower_mean_bound_distance", "upper_mean_bound_distance",
            "lower_concentration_bound_distance", "upper_concentration_bound_distance",
        ):
            value = start.get(key)
            if isinstance(value, (int, float)) and math.isfinite(value):
                distances.append(float(value))
    derived["minimum_start_to_bound_distance"] = min(distances) if distances else None
    return derived


def _json_line(path: Path, value: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def run_f5_bank(
    spec, *, bank: str, k: int, c0_b: int, c5_b: int,
    selected_b3_ids: set[str] | None = None, output_path: Path | None = None,
) -> dict[str, Any]:
    if bank not in {"calibration", "validation"}:
        raise F5DevelopmentCalibrationError("UNKNOWN_F5_BANK")
    if type(k) is not int or k < 1 or type(c0_b) is not int or c0_b < 100 or type(c5_b) is not int or c5_b < 100:
        raise F5DevelopmentCalibrationError("INVALID_BANK_K_OR_BOOTSTRAP_B")
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("", encoding="utf-8")

    comparisons = []
    truths = []
    records = []
    fit_statuses: dict[str, int] = {}
    optimizer_statuses: dict[str, int] = {}
    parameter_values: dict[str, list[float]] = {
        key: [] for key in (
            "selected_mean_probability", "selected_concentration",
            "selected_alpha", "selected_beta", "selected_log_likelihood",
            "selected_score_norm", "profile_log_concentration_curvature",
            "minimum_start_to_bound_distance",
        )
    }
    for replicate in range(k):
        identifier = dataset_id(bank, spec.cell_id, replicate)
        dataset_stream = (
            "f5_optimizer_calibration_dataset" if bank == "calibration"
            else "f5_optimizer_validation_dataset"
        )
        data_seed = derive_seed(dataset_stream, spec.cell_id, replicate)
        c0_seed = derive_seed("f5_c0_bootstrap", spec.cell_id, replicate if bank == "calibration" else K_CALIBRATION + replicate)
        c5_seed = derive_seed("f5_c5_bootstrap", spec.cell_id, replicate if bank == "calibration" else K_CALIBRATION + replicate)
        rows = generate_holdout_dataset(spec, replicate, seed_override=data_seed)
        rows_hash = hashlib.sha256(
            json.dumps(rows, separators=(",", ":"), allow_nan=False).encode("utf-8")
        ).hexdigest()
        comparison = compare_dataset(
            rows, dataset_id=identifier, family="F5",
            target_m=spec.m, target_r=spec.r,
            baseline_bootstrap_replicates=c0_b,
            baseline_bootstrap_seed=c0_seed,
            confidence_level=CONFIDENCE_LEVEL,
            bootstrap_replicates=c5_b, bootstrap_seed=c5_seed,
            include_profile_diagnostics=False,
            include_f5_concentration_profile_audit=False,
        )
        if comparison.dataset_id != identifier or (comparison.input_m, comparison.input_r) != (spec.m, spec.r):
            raise F5DevelopmentCalibrationError("COMPARISON_DATASET_OR_DESIGN_MISMATCH")
        if {comparison.baseline.method_id, *(item.method_id for item in comparison.candidates)} != set(IMPLEMENTED_METHODS["F5"]):
            raise F5DevelopmentCalibrationError("F5_METHOD_ROSTER_MISMATCH")
        truth = _truth(spec, identifier)
        comparisons.append(comparison)
        truths.append(truth)
        fit = _optimizer_fields(comparison)
        fit_statuses[fit["fit_status"]] = fit_statuses.get(fit["fit_status"], 0) + 1
        optimizer_statuses[fit["optimizer_status"]] = optimizer_statuses.get(fit["optimizer_status"], 0) + 1
        audit = fit.get("optimizer_audit") or {}
        for key in parameter_values:
            if key in fit and isinstance(fit[key], (int, float)) and math.isfinite(fit[key]):
                parameter_values[key].append(float(fit[key]))
            elif key in audit and isinstance(audit[key], (int, float)) and math.isfinite(audit[key]):
                parameter_values[key].append(float(audit[key]))
        record = {
            "dataset_id": identifier,
            "bank": bank,
            "cell_id": spec.cell_id,
            "replicate_index": replicate,
            "dataset_seed": data_seed,
            "rows_sha256": rows_hash,
            "C0_bootstrap_seed": c0_seed,
            "C0_bootstrap_B": c0_b,
            "C5_bootstrap_seed": c5_seed,
            "C5_bootstrap_B": c5_b,
            "b3_selected_before_outcome": identifier in (selected_b3_ids or set()) if bank == "calibration" else False,
            "fit_diagnostics": fit,
            "comparison": _jsonable(comparison),
            "truth": _jsonable(truth),
        }
        records.append(record)
        if output_path is not None:
            _json_line(output_path, record)

    metrics = [
        _jsonable(metric)
        for metric in adjudicate_matched_datasets(comparisons, truths)
        if metric.target in {"within", "between"}
    ]
    if len(records) != k or len({record["dataset_id"] for record in records}) != k:
        raise F5DevelopmentCalibrationError("INCOMPLETE_OR_DUPLICATE_BANK_DENOMINATOR")
    diagnostic_gate = all(
        record["fit_diagnostics"]["fit_status"] == "INTERIOR"
        and record["fit_diagnostics"]["optimizer_status"] == "OPTIMIZER_CONCORDANT"
        for record in records
    )
    return {
        "bank": bank,
        "cell": spec.manifest(),
        "datasets_completed": len(records),
        "method_roster": sorted(IMPLEMENTED_METHODS["F5"]),
        "metrics_within_and_raw_between_only": metrics,
        "fit_status_counts": dict(sorted(fit_statuses.items())),
        "optimizer_status_counts": dict(sorted(optimizer_statuses.items())),
        "fit_parameter_summaries": {
            key: _finite_summary(values) for key, values in parameter_values.items()
        },
        "optimizer_diagnostic_gate": (
            "PASS_NO_UNRESOLVED_NUMERICAL_STATE" if diagnostic_gate
            else "UNRESOLVED_NUMERICAL_STATE_PRESENT"
        ),
        "mcse_scope": MCSE_SCOPE,
        "records": records,
    }


def _rank_uncertainty(bootstrap_b: int, probability: float) -> dict[str, Any]:
    alpha = 1.0 - CONFIDENCE_LEVEL
    lower_count = int(binom.ppf(alpha / 2.0, bootstrap_b, probability))
    upper_count = int(binom.ppf(1.0 - alpha / 2.0, bootstrap_b, probability))
    lower_rank = max(1, min(bootstrap_b, lower_count))
    upper_rank = max(1, min(bootstrap_b, upper_count + 1))
    return {
        "quantile_probability": probability,
        "bootstrap_replicates": bootstrap_b,
        "interpolated_quantile_rank_1based": 1.0 + (bootstrap_b - 1) * probability,
        "binomial_rank_mean": bootstrap_b * probability,
        "binomial_rank_sd": math.sqrt(bootstrap_b * probability * (1.0 - probability)),
        "approximate_95_percent_order_statistic_rank_bounds_1based": [lower_rank, upper_rank],
        "rank_uncertainty_width": upper_rank - lower_rank,
        "interpretation": "DISCRETE_BINOMIAL_ORDER_STATISTIC_RANK_DIAGNOSTIC_NOT_COVERAGE",
    }


def _endpoint_record(interval, bootstrap_b: int) -> dict[str, Any]:
    if interval is None:
        return {
            "interval": None,
            "lower_rank_uncertainty": _rank_uncertainty(bootstrap_b, 0.025),
            "upper_rank_uncertainty": _rank_uncertainty(bootstrap_b, 0.975),
        }
    return {
        "interval": [float(interval[0]), float(interval[1])],
        "lower_rank_uncertainty": _rank_uncertainty(bootstrap_b, 0.025),
        "upper_rank_uncertainty": _rank_uncertainty(bootstrap_b, 0.975),
    }


def run_f5_endpoint_sensitivity(
    spec, *, calibration_records: list[dict[str, Any]], n_selected: int,
    b1000: int, b4000: int, output_path: Path | None = None,
) -> dict[str, Any]:
    calibration_records = [r for r in calibration_records if r["cell_id"] == spec.cell_id]
    ids = [r["dataset_id"] for r in calibration_records]
    selected = select_b3_calibration_datasets(spec.cell_id, ids, n=n_selected)
    by_id = {r["dataset_id"]: r for r in calibration_records}
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("", encoding="utf-8")

    records = []
    endpoint_deltas: dict[str, list[float]] = {
        f"{target}_{endpoint}": [] for target in ("within", "between")
        for endpoint in ("lower", "upper")
    }
    width_deltas: dict[str, list[float]] = {"within": [], "between": []}
    for selection in selected:
        source = by_id[selection["dataset_id"]]
        replicate = source["replicate_index"]
        data_seed = source["dataset_seed"]
        rows = generate_holdout_dataset(spec, replicate, seed_override=data_seed)
        rows_hash = hashlib.sha256(
            json.dumps(rows, separators=(",", ":"), allow_nan=False).encode("utf-8")
        ).hexdigest()
        if rows_hash != source["rows_sha256"]:
            raise F5DevelopmentCalibrationError("B3_REGENERATED_DATASET_HASH_MISMATCH")

        outputs = {}
        for bootstrap_b, stream in (
            (b1000, "f5_endpoint_sensitivity_b1000"),
            (b4000, "f5_endpoint_sensitivity_b4000"),
        ):
            seed = derive_seed(stream, spec.cell_id, replicate)
            result = fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=spec.m, target_r=spec.r,
                bootstrap_replicates=bootstrap_b, bootstrap_seed=seed,
                confidence_level=CONFIDENCE_LEVEL,
            )
            outputs[str(bootstrap_b)] = {
                "bootstrap_seed": seed,
                "bootstrap_replicates": bootstrap_b,
                "fit_status": (
                    "ABSTAINED" if result.fit is None
                    else "BOUNDARY" if result.fit.boundary else "INTERIOR"
                ),
                "failure_reason": result.failure_reason,
                "valid_mcse_replicates": result.valid_mcse_replicates,
                "valid_mcse_rate": result.valid_mcse_rate,
                "within_endpoint_diagnostics": _endpoint_record(result.comparison.within_interval, bootstrap_b),
                "between_raw_endpoint_diagnostics": _endpoint_record(result.comparison.between_interval, bootstrap_b),
            }

        record = {
            "dataset_id": source["dataset_id"],
            "cell_id": spec.cell_id,
            "replicate_index": replicate,
            "selection_sha256": selection["selection_sha256"],
            "dataset_seed_reused_from_calibration_bank": data_seed,
            "rows_sha256": rows_hash,
            "selection_rule": "SHA256(schedule_id|B3_SELECTION|cell_id|dataset_id), ascending, first N; no C5 outcome field used",
            "B1000": outputs[str(b1000)],
            "B4000": outputs[str(b4000)],
        }
        for target, key in (
            ("within", "within_endpoint_diagnostics"),
            ("between", "between_raw_endpoint_diagnostics"),
        ):
            i1 = outputs[str(b1000)][key]["interval"]
            i4 = outputs[str(b4000)][key]["interval"]
            if i1 is not None and i4 is not None:
                endpoint_deltas[f"{target}_lower"].append(i4[0] - i1[0])
                endpoint_deltas[f"{target}_upper"].append(i4[1] - i1[1])
                width_deltas[target].append((i4[1] - i4[0]) - (i1[1] - i1[0]))
        records.append(record)
        if output_path is not None:
            _json_line(output_path, record)

    return {
        "cell_id": spec.cell_id,
        "selected_datasets": len(records),
        "B1000": b1000,
        "B4000": b4000,
        "endpoint_value_change_B4000_minus_B1000": {
            key: _finite_summary(values) for key, values in endpoint_deltas.items()
        },
        "interval_width_change_B4000_minus_B1000": {
            key: _finite_summary(values) for key, values in width_deltas.items()
        },
        "coverage_adjudication": "NOT_USED_B3_IS_DIAGNOSTIC_ONLY",
        "records": records,
    }


def run_f5_development_calibration(
    output_dir: Path, *, root: Path,
    k_calibration: int = K_CALIBRATION,
    k_validation: int = K_VALIDATION,
    c0_b: int = C0_B,
    c5_b: int = C5_B,
    b3_selected_per_cell: int = B3_SELECTED_PER_CELL,
    b3_b1000: int = B3_B1000,
    b3_b4000: int = B3_B4000,
    code_commit: str,
    authorization: dict[str, Any],
) -> dict[str, Any]:
    """Run the frozen F5 B2/B3 development banks after one-use authorization."""
    expected = {
        "scope": "C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_ONLY",
        "f5_b2_b3_authorized": True,
        "f1_a2_a3_authorized": False,
        "tier_b_authorized": False,
        "comparative_holdout_authorized": False,
        "c10_scientific_execution_authorized": False,
    }
    for key, value in expected.items():
        if authorization.get(key) != value:
            raise F5DevelopmentCalibrationError(f"AUTHORIZATION_SCOPE_MISMATCH:{key}")
    if (
        k_calibration != K_CALIBRATION or k_validation != K_VALIDATION
        or c0_b != C0_B or c5_b != C5_B
        or b3_selected_per_cell != B3_SELECTED_PER_CELL
        or b3_b1000 != B3_B1000 or b3_b4000 != B3_B4000
    ):
        raise F5DevelopmentCalibrationError("PRODUCTION_K_B_OVERRIDE_PROHIBITED")
    seed_audit = validate_seed_separation()
    output_dir.mkdir(parents=True, exist_ok=True)
    specs = _f5_specs()

    # Select the B3 roster from IDs alone before any B2 C5 result is examined.
    b3_selection = {}
    for spec in specs:
        ids = [dataset_id("calibration", spec.cell_id, i) for i in range(k_calibration)]
        b3_selection[spec.cell_id] = select_b3_calibration_datasets(
            spec.cell_id, ids, n=b3_selected_per_cell,
        )
    _write_json(output_dir / "b3_selection_manifest.json", {
        "selection_rule": "SHA256(schedule_id|B3_SELECTION|cell_id|dataset_id), ascending, first N",
        "selection_uses_c5_outcomes": False,
        "selection_schedule_id": SEED_SCHEDULE_ID,
        "selected_by_cell": b3_selection,
    })

    results = []
    started = time.perf_counter()
    for spec in specs:
        selected_ids = {item["dataset_id"] for item in b3_selection[spec.cell_id]}
        calibration = run_f5_bank(
            spec, bank="calibration", k=k_calibration, c0_b=c0_b, c5_b=c5_b,
            selected_b3_ids=selected_ids,
            output_path=output_dir / f"{spec.cell_id}.calibration.jsonl",
        )
        validation = run_f5_bank(
            spec, bank="validation", k=k_validation, c0_b=c0_b, c5_b=c5_b,
            output_path=output_dir / f"{spec.cell_id}.validation.jsonl",
        )
        sensitivity = run_f5_endpoint_sensitivity(
            spec, calibration_records=calibration["records"],
            n_selected=b3_selected_per_cell, b1000=b3_b1000, b4000=b3_b4000,
            output_path=output_dir / f"{spec.cell_id}.B3_endpoint_sensitivity.jsonl",
        )
        results.append({
            "cell_id": spec.cell_id,
            "calibration": {key: value for key, value in calibration.items() if key != "records"},
            "validation": {key: value for key, value in validation.items() if key != "records"},
            "B3_endpoint_sensitivity": {key: value for key, value in sensitivity.items() if key != "records"},
        })

    elapsed = time.perf_counter() - started
    manifest = {
        "schema": "TGCV-C10S-F5-B2-B3-DEVELOPMENT-CALIBRATION-1",
        "run_id": RUN_ID,
        "status": "COMPLETED_DEVELOPMENT_CALIBRATION_NOT_CONFIRMATORY",
        "authorization_id": authorization.get("authorization_id"),
        "authorization_sha256": authorization.get("authorization_sha256"),
        "approved_code_commit": code_commit,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "seed_namespace": SEED_NAMESPACE,
        "cells": list(EXPECTED_CELLS),
        "k_calibration_per_cell": k_calibration,
        "k_validation_per_cell": k_validation,
        "c0_bootstrap_B": c0_b,
        "c5_bootstrap_B": c5_b,
        "B3_selected_per_cell": b3_selected_per_cell,
        "B3_bootstrap_B": [b3_b1000, b3_b4000],
        "seed_collision_audit": seed_audit,
        "elapsed_seconds": elapsed,
        "peak_process_rss_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
        },
        "spec_sha256": sha256_file(root / SPEC_PATH),
        "dependency_lock_sha256": sha256_file(root / LOCK_PATH),
        "source_sha256": {
            path: sha256_file(root / path) for path in (
                "03_EXPERIMENTS/C10-S/harness/run_c10s_post_holdout_f5_b2_b3_development_calibration.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py",
                "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_fitted_beta_binomial_bootstrap.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_likelihood_diagnostics.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_variance_comparison_interface.py",
                "03_EXPERIMENTS/C10-S/harness/c10s_beta_binomial_variance_oracles.py",
                LOCK_PATH,
                SPEC_PATH,
            )
        },
        "mcse_scope": MCSE_SCOPE,
        "f1_a2_a3_execution": False,
        "tier_b_execution": False,
        "comparative_holdout_execution": False,
        "c10_scientific_execution": False,
        "results": results,
    }
    _write_json(output_dir / "manifest.json", manifest)
    _write_json(output_dir / "summary.json", {
        "run_id": RUN_ID,
        "status": manifest["status"],
        "elapsed_seconds": elapsed,
        "results": results,
        "mcse_scope": MCSE_SCOPE,
    })
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validated-authorization", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--code-commit", required=True)
    args = parser.parse_args()
    authorization = json.loads(args.validated_authorization.read_text(encoding="utf-8"))
    run_f5_development_calibration(
        args.output_dir, root=args.root, code_commit=args.code_commit,
        authorization=authorization,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
