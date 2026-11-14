#!/usr/bin/env python3
"""Run the C10-S Analyzer against the exact 27-cell P178 focal benchmark.

The Analyzer receives only sealed observed assignment/Q_B1 evidence. Analytic
truth and reference summaries are read by the outer evaluation driver only
after each Analyzer result has been produced.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path
from statistics import mean
from typing import Any

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
CALIBRATION = HERE.parent / "calibration"
sys.path.insert(0, str(CALIBRATION))
import p178_focal_monte_carlo as p178  # noqa: E402

from focal_harness import (  # noqa: E402
    AnalysisContract,
    Analyzer,
    EvaluationReport,
    Evaluator,
    EvidenceCandidate,
    SealedEvidence,
    Sealer,
    TruthBundle,
)

REFERENCE = CALIBRATION / "p178_reference_N700.csv"
SCENARIO_ORDER = ("null", "positive", "negative")
EXPECTED_CELLS = 27
EXPECTED_REPLICATIONS = 10_000
REFERENCE_TOLERANCE = 1e-9
BATCH = 250

CONTRACT = AnalysisContract(
    estimand_id="THETA_A_Q_B1",
    estimand_version="001",
    randomized_assignment=True,
    direct_path_status="ABSENT",
    common_regime=True,
    positivity=True,
    version_consistency=True,
    measurement_ideal=True,
    interference_absent=True,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def wilson(successes: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    phat = successes / n
    den = 1.0 + z * z / n
    center = (phat + z * z / (2 * n)) / den
    half = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n)) / den
    return center - half, center + half


def read_reference() -> dict[tuple[int, float, str], dict[str, str]]:
    with REFERENCE.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    result = {(int(row["K"]), float(row["pi0"]), row["scenario"]): row for row in rows}
    if len(result) != EXPECTED_CELLS:
        raise RuntimeError(f"Expected {EXPECTED_CELLS} P178 reference cells, found {len(result)}")
    return result


def make_evidence(
    sealer: Sealer, run_id: str, q0: np.ndarray, q1: np.ndarray
) -> SealedEvidence:
    rows: list[dict[str, Any]] = []
    for index, value in enumerate(q0):
        rows.append({
            "unit_id": f"{run_id}-C-{index:04d}",
            "assignment_z": 0,
            "q_b1_observed": float(value),
            "observation_status": "OBSERVED",
        })
    for index, value in enumerate(q1):
        rows.append({
            "unit_id": f"{run_id}-T-{index:04d}",
            "assignment_z": 1,
            "q_b1_observed": float(value),
            "observation_status": "OBSERVED",
        })
    return sealer.seal(EvidenceCandidate(run_id, tuple(rows)))


def run_cell(
    pi0: float, k_slots: int, scenario: str, replications: int, seed: int,
    reference_row: dict[str, str],
) -> dict[str, Any]:
    alpha01, alpha10 = p178.SCENARIOS[scenario]
    theta = p178.oracle_theta(pi0, k_slots, alpha01, alpha10)
    rng = np.random.default_rng(seed)
    n_arm = p178.N_REFERENCE // 2
    analyzer = Analyzer()
    evaluator = Evaluator()
    sealer = Sealer()

    estimates = np.empty(replications, dtype=np.float64)
    standard_errors = np.empty(replications, dtype=np.float64)
    lower = np.empty(replications, dtype=np.float64)
    upper = np.empty(replications, dtype=np.float64)
    rejected = np.zeros(replications, dtype=np.bool_)
    covered = np.zeros(replications, dtype=np.bool_)
    invalid = 0
    classification_errors = 0
    abstentions = 0

    completed = 0
    while completed < replications:
        batch_size = min(BATCH, replications - completed)
        # Preserve P178's exact RNG call order: control arm first, then treated.
        q0_batch = p178.draw_arm(
            rng, batch_size, n_arm, pi0, k_slots, alpha01, alpha10, p178.LAMBDA0
        )
        q1_batch = p178.draw_arm(
            rng, batch_size, n_arm, pi0, k_slots, alpha01, alpha10, p178.LAMBDA1
        )

        for offset in range(batch_size):
            replicate_index = completed + offset
            run_id = f"P178-K{k_slots}-PI{pi0:.2f}-{scenario}-R{replicate_index:05d}"
            evidence = make_evidence(sealer, run_id, q0_batch[offset], q1_batch[offset])
            result = analyzer.analyze(evidence, CONTRACT)

            # Truth is made available only after Analyzer has returned its sealed result.
            truth = TruthBundle(
                run_id=run_id,
                potential_q_by_z=(),
                signature_d1_by_z=(),
                theta_access_truth=theta,
                itt_value_truth=theta,
                direct_path_truth=False,
                seed=seed + replicate_index,
            )
            adjudication: EvaluationReport = evaluator.evaluate(
                truth, result, CONTRACT, tolerance=0.0
            )
            if not adjudication.classification_correct:
                classification_errors += 1
            if result.focal_identification != "IDENTIFIED":
                abstentions += 1

            estimate = result.focal_estimate
            se = result.focal_standard_error
            interval = result.focal_interval_95
            if estimate is None or se is None or interval is None or not math.isfinite(se) or se <= 0:
                invalid += 1
                estimates[replicate_index] = np.nan
                standard_errors[replicate_index] = np.nan
                lower[replicate_index] = np.nan
                upper[replicate_index] = np.nan
                continue

            estimates[replicate_index] = estimate
            standard_errors[replicate_index] = se
            lower[replicate_index], upper[replicate_index] = interval
            rejected[replicate_index] = interval[0] > 0.0 or interval[1] < 0.0
            covered[replicate_index] = interval[0] <= theta <= interval[1]

        completed += batch_size

    valid_mask = np.isfinite(estimates) & np.isfinite(standard_errors)
    valid_n = int(valid_mask.sum())
    if valid_n != replications:
        raise RuntimeError(
            f"Invalid Analyzer outputs in K={k_slots}, pi0={pi0}, scenario={scenario}: "
            f"{replications-valid_n}/{replications}"
        )

    est = estimates[valid_mask]
    se_values = standard_errors[valid_mask]
    widths = upper[valid_mask] - lower[valid_mask]
    reject_count = int(rejected[valid_mask].sum())
    cover_count = int(covered[valid_mask].sum())
    rejection_rate = reject_count / valid_n
    coverage = cover_count / valid_n
    sampling_sd = float(est.std(ddof=1))
    bias = float(est.mean() - theta)
    squared_error = (est - theta) ** 2
    rmse = float(np.sqrt(np.mean(squared_error)))
    bias_mcse = sampling_sd / math.sqrt(valid_n)
    rmse_mcse = (
        float(squared_error.std(ddof=1) / math.sqrt(valid_n) / (2.0 * rmse))
        if rmse > 0 else 0.0
    )
    mean_width = float(widths.mean())
    width_mcse = float(widths.std(ddof=1) / math.sqrt(valid_n))
    reject_low, reject_high = wilson(reject_count, valid_n)
    cover_low, cover_high = wilson(cover_count, valid_n)

    metrics: dict[str, Any] = {
        "N": p178.N_REFERENCE,
        "R": replications,
        "pi0": pi0,
        "K": k_slots,
        "scenario": scenario,
        "alpha01": alpha01,
        "alpha10": alpha10,
        "lambda0": p178.LAMBDA0,
        "lambda1": p178.LAMBDA1,
        "theta_true": theta,
        "rejection_rate": rejection_rate,
        "rejection_mcse": math.sqrt(rejection_rate * (1 - rejection_rate) / valid_n),
        "rejection_wilson_low": reject_low,
        "rejection_wilson_high": reject_high,
        "coverage": coverage,
        "coverage_mcse": math.sqrt(coverage * (1 - coverage) / valid_n),
        "coverage_wilson_low": cover_low,
        "coverage_wilson_high": cover_high,
        "bias": bias,
        "bias_mcse": bias_mcse,
        "bias_mcse_over_sampling_sd": bias_mcse / sampling_sd if sampling_sd > 0 else 0.0,
        "rmse": rmse,
        "rmse_mcse": rmse_mcse,
        "rmse_mcse_over_sampling_sd": rmse_mcse / sampling_sd if sampling_sd > 0 else 0.0,
        "mean_ci_width": mean_width,
        "mean_ci_width_mcse": width_mcse,
        "mean_ci_width_mcse_relative": width_mcse / mean_width if mean_width > 0 else 0.0,
        "mean_se": float(se_values.mean()),
        "seed": seed,
        "invalid_replicates": invalid,
        "classification_errors": classification_errors,
        "abstentions": abstentions,
        "valid_replicates": valid_n,
    }

    # Paired-seed equivalence against the already persisted P178 estimator benchmark.
    comparisons = (
        "rejection_rate", "coverage", "bias", "rmse", "mean_ci_width", "mean_se"
    )
    diffs = {
        f"reference_abs_diff_{name}": abs(float(metrics[name]) - float(reference_row[name]))
        for name in comparisons
    }
    metrics.update(diffs)
    metrics["reference_match"] = all(
        value <= REFERENCE_TOLERANCE for value in diffs.values()
    )
    return metrics


def evaluate_acceptance(rows: list[dict[str, Any]], replications: int) -> dict[str, Any]:
    null_rows = [row for row in rows if row["scenario"] == "null"]
    nonnull_rows = [row for row in rows if row["scenario"] != "null"]
    coverage_compatible = sum(
        row["coverage_wilson_low"] <= 0.95 <= row["coverage_wilson_high"]
        for row in rows
    )
    criteria = {
        "27_cells_present": len(rows) == EXPECTED_CELLS,
        "replications_per_cell": all(row["valid_replicates"] == replications for row in rows),
        "zero_invalid_replicates": all(row["invalid_replicates"] == 0 for row in rows),
        "zero_classification_errors": all(row["classification_errors"] == 0 for row in rows),
        "zero_focal_abstentions": all(row["abstentions"] == 0 for row in rows),
        "coverage_wilson_compatible_in_at_least_26_cells": coverage_compatible >= 26,
        "coverage_absolute_deviation_at_most_0_005": all(
            abs(row["coverage"] - 0.95) <= 0.005 for row in rows
        ),
        "null_rejection_wilson_compatible_in_all_9_cells": all(
            row["rejection_wilson_low"] <= 0.05 <= row["rejection_wilson_high"]
            for row in null_rows
        ),
        "nonnull_power_lower_wilson_at_least_0_80": all(
            row["rejection_wilson_low"] >= 0.80 for row in nonnull_rows
        ),
        "proportion_mcse_at_most_0_005": all(
            row["rejection_mcse"] <= 0.005 and row["coverage_mcse"] <= 0.005
            for row in rows
        ),
        "bias_mcse_over_sampling_sd_at_most_0_05": all(
            row["bias_mcse_over_sampling_sd"] <= 0.05 for row in rows
        ),
        "rmse_mcse_over_sampling_sd_at_most_0_05": all(
            row["rmse_mcse_over_sampling_sd"] <= 0.05 for row in rows
        ),
        "reference_metrics_match_within_1e_9": all(row["reference_match"] for row in rows),
    }
    return {
        "status": "PASS" if all(criteria.values()) else "FAIL",
        "criteria": criteria,
        "coverage_wilson_compatible_cells": coverage_compatible,
        "null_cells": len(null_rows),
        "nonnull_cells": len(nonnull_rows),
    }


def run(out_dir: Path, replications: int, strict_protocol: bool) -> dict[str, Any]:
    if strict_protocol and replications != EXPECTED_REPLICATIONS:
        raise ValueError(f"Strict protocol requires exactly {EXPECTED_REPLICATIONS} replications per cell")
    if replications < 2:
        raise ValueError("At least two replications per cell are required")
    out_dir.mkdir(parents=True, exist_ok=True)
    reference = read_reference()
    rows: list[dict[str, Any]] = []
    index = 0
    for k_slots in p178.K_VALUES:
        for pi0 in p178.PI_VALUES:
            for scenario in SCENARIO_ORDER:
                key = (k_slots, pi0, scenario)
                seed = p178.BASE_SEED + 29 * index
                cell = run_cell(pi0, k_slots, scenario, replications, seed, reference[key])
                rows.append(cell)
                index += 1
                print(
                    f"completed K={k_slots} pi0={pi0:.2f} scenario={scenario} "
                    f"R={replications} reference_match={cell['reference_match']}",
                    flush=True,
                )

    acceptance = evaluate_acceptance(rows, replications)
    summary_path = out_dir / "p178_analyzer_monte_carlo.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    manifest: dict[str, Any] = {
        "protocol": "TGCV-C10-S-P178-ANALYZER-MC-001",
        "status": acceptance["status"],
        "strict_protocol": strict_protocol,
        "replications_per_cell": replications,
        "cells": len(rows),
        "cell_order": "K_VALUES, PI_VALUES, null-positive-negative",
        "seed_rule": "p178.BASE_SEED + 29*cell_index",
        "n_total": p178.N_REFERENCE,
        "assignment": "balanced 350/350; P178 draw_arm RNG sequence preserved",
        "parameters": {
            "lambda0": p178.LAMBDA0,
            "lambda1": p178.LAMBDA1,
            "baseline_transition_p01": 0.2,
            "baseline_transition_p10": 0.2,
            "pi0": list(p178.PI_VALUES),
            "K": list(p178.K_VALUES),
            "scenarios": {name: list(p178.SCENARIOS[name]) for name in SCENARIO_ORDER},
        },
        "analyzer_version": Analyzer.version,
        "sealer_version": Sealer.version,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "rng": "numpy.random.default_rng / PCG64",
        "reference_script_sha256": sha256_file(CALIBRATION / "p178_focal_monte_carlo.py"),
        "reference_csv_sha256": sha256_file(REFERENCE),
        "runner_sha256": sha256_file(Path(__file__).resolve()),
        "analyzer_source_sha256": sha256_file(HERE / "focal_harness.py"),
        "acceptance": acceptance,
        "outputs": {"summary_csv": summary_path.name},
        "limitations": [
            "Non-confirmatory methodological calibration only.",
            "Only the 27 existing P178 N=700 focal cells are evaluated.",
            "The Analyzer receives observed assignment and Q_B1 only; truth is supplied to Evaluator after analysis.",
            "No adversarial direct-path, positivity failure, measurement degradation, interference, or weak-signal cells are included.",
            "This run does not validate the full TGCV causal claim or confirmatory experiment.",
        ],
    }
    manifest_path = out_dir / "p178_analyzer_monte_carlo_manifest.json"
    manifest["outputs"]["summary_csv_sha256"] = sha256_file(summary_path)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": acceptance["status"],
        "cells": len(rows),
        "replications_per_cell": replications,
        "total_analyzer_runs": len(rows) * replications,
        "summary_csv": str(summary_path),
        "manifest": str(manifest_path),
        "acceptance": acceptance,
    }, indent=2, sort_keys=True), flush=True)
    if strict_protocol and acceptance["status"] != "PASS":
        raise SystemExit("P178 Analyzer Monte Carlo acceptance criteria failed")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--replications", type=int, default=EXPECTED_REPLICATIONS)
    parser.add_argument("--strict-protocol", action="store_true")
    args = parser.parse_args()
    run(args.out, args.replications, args.strict_protocol)


if __name__ == "__main__":
    main()
