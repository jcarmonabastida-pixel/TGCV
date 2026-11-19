"""Unified matched-data F1/F5 nested M/R inference comparison.

Development-only orchestration and adjudication. It does not calibrate coverage,
select a method, modify protocol v002, or execute a Monte Carlo study.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

from c10s_f1_exact_pivotal_candidate import f1_exact_pivotal_result
from c10s_fitted_beta_binomial_bootstrap import (
    FittedBetaBinomialBootstrapResult,
    fitted_beta_binomial_parametric_bootstrap,
)
from c10s_variance_comparison_interface import (
    VarianceComparisonResult,
    observed_nested_mr_result,
)


ENGINE_ID = "C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.0"
IMPLEMENTED_METHODS = {
    "F1": ("C0_RAW_COMMON", "C1_F1_EXACT_PIVOTAL"),
    "F5": ("C0_RAW_COMMON", "C5_F5_FITTED_BETA_BINOMIAL_PARAMETRIC"),
}
UNIMPLEMENTED_METHODS = ("C2", "C3", "C4")


class ComparativeEngineError(ValueError):
    """Invalid family, comparison record or adjudication input."""


@dataclass(frozen=True)
class CandidateOutput:
    method_id: str
    comparison: VarianceComparisonResult
    diagnostics: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class DatasetComparison:
    engine_id: str
    family: str
    input_m: int
    input_r: int
    target_m: int
    target_r: int
    baseline: VarianceComparisonResult
    candidates: tuple[CandidateOutput, ...]
    unavailable_methods: tuple[str, ...]


@dataclass(frozen=True)
class TruthTargets:
    within: float
    between: float
    mcse: float


@dataclass(frozen=True)
class MethodTargetMetrics:
    method_id: str
    target: str
    n_datasets: int
    point_emission_rate: float
    point_bias: float | None
    point_rmse: float | None
    interval_emission_rate: float
    conditional_coverage: float | None
    coverage_mcse: float | None
    coverage_wilson_95: tuple[float, float] | None
    unconditional_cover_rate: float
    lower_miss_rate: float | None
    upper_miss_rate: float | None
    mean_interval_width: float | None
    abstention_count: int
    abstention_reasons: tuple[tuple[str, int], ...]


def compare_dataset(
    rows: Sequence[Sequence[float]], *,
    family: str,
    target_m: int,
    target_r: int,
    confidence_level: float = 0.95,
    bootstrap_replicates: int | None = None,
    bootstrap_seed: int | None = None,
) -> DatasetComparison:
    """Run the currently implemented family-appropriate candidates on one dataset.

    C0 is always emitted as the common observed-data baseline. C1 is restricted
    to F1; C5 is restricted to F5. C2-C4 remain explicitly unavailable rather
    than being represented by placeholder or silently substituted methods.
    """
    if family not in IMPLEMENTED_METHODS:
        raise ComparativeEngineError("SUPPORTED_FAMILIES_ARE_F1_AND_F5")
    baseline = observed_nested_mr_result(
        rows, target_m=target_m, target_r=target_r,
    )
    m, r = len(rows), len(rows[0])
    outputs: list[CandidateOutput] = []

    if family == "F1":
        result = f1_exact_pivotal_result(
            rows, target_m=target_m, target_r=target_r,
            family="F1", confidence_level=confidence_level,
        )
        outputs.append(CandidateOutput(
            method_id=result.method_id, comparison=result,
            diagnostics=(("inference_scope", "balanced_gaussian_random_intercept_only"),),
        ))
    else:
        if bootstrap_replicates is None or bootstrap_seed is None:
            raise ComparativeEngineError(
                "F5_REQUIRES_EXPLICIT_BOOTSTRAP_REPLICATES_AND_SEED"
            )
        fitted: FittedBetaBinomialBootstrapResult = (
            fitted_beta_binomial_parametric_bootstrap(
                rows, target_m=target_m, target_r=target_r,
                bootstrap_replicates=bootstrap_replicates,
                bootstrap_seed=bootstrap_seed,
                confidence_level=confidence_level,
            )
        )
        fit = fitted.fit
        diagnostics = (
            ("fit_status", "ABSTAINED" if fit is None else "BOUNDARY" if fit.boundary else "INTERIOR"),
            ("bootstrap_replicates", str(fitted.bootstrap_replicates)),
            ("valid_mcse_replicates", str(fitted.valid_mcse_replicates)),
            ("valid_mcse_rate", format(fitted.valid_mcse_rate, ".17g")),
            ("bootstrap_seed", str(fitted.bootstrap_seed)),
            ("failure_reason", fitted.failure_reason or "NONE"),
        )
        outputs.append(CandidateOutput(
            method_id=fitted.comparison.method_id,
            comparison=fitted.comparison,
            diagnostics=diagnostics,
        ))

    return DatasetComparison(
        engine_id=ENGINE_ID, family=family, input_m=m, input_r=r,
        target_m=target_m, target_r=target_r, baseline=baseline, candidates=tuple(outputs),
        unavailable_methods=UNIMPLEMENTED_METHODS,
    )


def adjudicate_matched_datasets(
    comparisons: Sequence[DatasetComparison],
    truths: Sequence[TruthTargets],
) -> tuple[MethodTargetMetrics, ...]:
    """Summarize matched datasets without hiding abstentions or misses.

    Coverage is conditional on interval emission; unconditional_cover_rate is
    the fraction of all datasets on which a covering interval was emitted.
    Point bias/RMSE use only finite emitted point estimates and report their
    own point-emission rate. No averaging across targets or methods occurs.
    """
    records = tuple(comparisons)
    truth_rows = tuple(truths)
    if not records or len(records) != len(truth_rows):
        raise ComparativeEngineError("COMPARISONS_AND_TRUTHS_MUST_BE_NONEMPTY_AND_PAIRED")
    families = {record.family for record in records}
    if len(families) != 1:
        raise ComparativeEngineError("ONE_FAMILY_PER_ADJUDICATION_BATCH")
    if any(record.engine_id != ENGINE_ID for record in records):
        raise ComparativeEngineError("UNKNOWN_ENGINE_RECORD")
    target_designs = {(record.target_m, record.target_r) for record in records}
    if len(target_designs) != 1:
        raise ComparativeEngineError("STRATIFY_DIFFERENT_TARGET_DESIGNS")
    for truth in truth_rows:
        for name, value in (("within", truth.within), ("between", truth.between), ("mcse", truth.mcse)):
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or value < 0.0):
                raise ComparativeEngineError(f"TRUTH_{name.upper()}_MUST_BE_FINITE_AND_NONNEGATIVE")
    method_ids = sorted({
        candidate.method_id
        for record in records for candidate in record.candidates
    })
    # Include C0, but never fabricate interval coverage for a point-only baseline.
    method_ids.append("RAW_NESTED_MR_COMPONENTS_1.0")
    targets = ("within", "between", "mcse")
    output: list[MethodTargetMetrics] = []

    for method_id in method_ids:
        for target in targets:
            points: list[float] = []
            errors: list[float] = []
            widths: list[float] = []
            covered = lower_miss = upper_miss = 0
            interval_emitted = 0
            abstentions: dict[str, int] = {}
            for record, truth in zip(records, truth_rows):
                comparison = (
                    record.baseline if method_id == "RAW_NESTED_MR_COMPONENTS_1.0"
                    else next((item.comparison for item in record.candidates if item.method_id == method_id), None)
                )
                if comparison is None:
                    continue
                true_value = float(getattr(truth, target))
                point_value = getattr(comparison, f"{target}_estimate" if target != "between" else "between_estimate_raw")
                if point_value is not None and math.isfinite(point_value):
                    points.append(float(point_value))
                    errors.append(float(point_value) - true_value)
                interval = getattr(comparison, f"{target}_interval")
                if interval is None:
                    reason = comparison.abstention_reason or (
                        "POINT_ONLY_BASELINE_NO_INTERVAL"
                        if method_id == "RAW_NESTED_MR_COMPONENTS_1.0"
                        else "INTERVAL_NOT_EMITTED"
                    )
                    abstentions[reason] = abstentions.get(reason, 0) + 1
                    continue
                low, high = interval
                if not (math.isfinite(low) and math.isfinite(high) and low <= high):
                    abstentions["INVALID_INTERVAL_OUTPUT"] = abstentions.get("INVALID_INTERVAL_OUTPUT", 0) + 1
                    continue
                interval_emitted += 1
                widths.append(high - low)
                if low <= true_value <= high:
                    covered += 1
                elif true_value < low:
                    lower_miss += 1
                else:
                    upper_miss += 1

            n = len(records)
            point_rate = len(points) / n
            interval_rate = interval_emitted / n
            conditional = (covered / interval_emitted) if interval_emitted else None
            coverage_mcse = (
                math.sqrt(conditional * (1.0 - conditional) / interval_emitted)
                if conditional is not None else None
            )
            if conditional is None:
                wilson = None
            else:
                z = 1.959963984540054
                denom = 1.0 + z * z / interval_emitted
                center = (conditional + z * z / (2.0 * interval_emitted)) / denom
                half = z * math.sqrt(
                    conditional * (1.0 - conditional) / interval_emitted
                    + z * z / (4.0 * interval_emitted * interval_emitted)
                ) / denom
                wilson = (max(0.0, center - half), min(1.0, center + half))
            output.append(MethodTargetMetrics(
                method_id=method_id, target=target, n_datasets=n,
                point_emission_rate=point_rate,
                point_bias=(math.fsum(errors) / len(errors)) if errors else None,
                point_rmse=(math.sqrt(math.fsum(e * e for e in errors) / len(errors))) if errors else None,
                interval_emission_rate=interval_rate,
                conditional_coverage=conditional,
                coverage_mcse=coverage_mcse,
                coverage_wilson_95=wilson,
                unconditional_cover_rate=covered / n,
                lower_miss_rate=(lower_miss / interval_emitted) if interval_emitted else None,
                upper_miss_rate=(upper_miss / interval_emitted) if interval_emitted else None,
                mean_interval_width=(math.fsum(widths) / len(widths)) if widths else None,
                abstention_count=n - interval_emitted,
                abstention_reasons=tuple(sorted(abstentions.items())),
            ))
    return tuple(output)
