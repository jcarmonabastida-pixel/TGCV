"""Versioned F5 challenger adapter; source-only until separately authorized.

Engine 1.1 remains the immutable source of C0/C5 records. This module wraps
those records without mutation and adds M1-PCT as an interval-only challenger.
It performs no calibration, simulation, workflow dispatch, or scientific run.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import math
from typing import Sequence

from c10s_nested_mr_comparative_inference_engine import (
    C0_METHOD_ID,
    DatasetComparison as LegacyDatasetComparison,
    MethodTargetMetrics,
    TruthTargets,
    _wilson,
    compare_dataset as compare_legacy_dataset,
)
from c10s_variance_comparison_interface import (
    VarianceComparisonResult,
    observed_nested_mr_result,
)
from c10s_f5_functional_refit_bootstrap import (
    METHOD_ID as M1_METHOD_ID,
    FIT_CONTRACT_ID as M1_FIT_CONTRACT_ID,
    F5FunctionalRefitBootstrapResult,
    fitted_functional_refit_percentile_bootstrap,
)


ENGINE_ID = "C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.2_M1_CHALLENGER"
C5_METHOD_ID = "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.1"
F5_ROSTER = frozenset((C0_METHOD_ID, C5_METHOD_ID, M1_METHOD_ID))


class M1ChallengerError(ValueError):
    """Invalid input or roster for the versioned M1 challenger path."""


@dataclass(frozen=True)
class M1ChallengerDatasetComparison:
    engine_id: str
    dataset_id: str
    family: str
    input_m: int
    input_r: int
    target_m: int
    target_r: int
    legacy_record: LegacyDatasetComparison
    m1_comparison: VarianceComparisonResult
    m1_result: F5FunctionalRefitBootstrapResult
    m1_diagnostics: tuple[tuple[str, str], ...]


def _binary_count_vector(rows: Sequence[Sequence[float]]) -> tuple[int, ...]:
    matrix = tuple(tuple(row) for row in rows)
    if len(matrix) < 2 or not matrix or len(matrix[0]) < 2:
        raise M1ChallengerError("M1_REQUIRES_RECTANGULAR_M_BY_R_WITH_M_R_GE_2")
    width = len(matrix[0])
    counts = []
    for i, row in enumerate(matrix):
        if len(row) != width:
            raise M1ChallengerError(f"M1_RAGGED_BINARY_INPUT_AT_WORLD_{i}")
        total = 0
        for j, value in enumerate(row):
            if isinstance(value, bool) or value not in (0, 1, 0.0, 1.0):
                raise M1ChallengerError(f"M1_NON_BINARY_INPUT_AT_{i}_{j}")
            total += int(value)
        counts.append(total)
    return tuple(counts)


def _m1_diagnostics(result: F5FunctionalRefitBootstrapResult) -> tuple[tuple[str, str], ...]:
    original_fit_admissible = result.original_fit.status == "PRIMARY_ANALYTIC_INTERIOR_FIT"
    values = (
        ("m1_status", result.status),
        ("m1_original_fit_failure_reason", result.original_fit.failure_reason or "NONE"),
        ("m1_model_point_status", "VALID_ORIGINAL_FIT" if original_fit_admissible else "UNAVAILABLE_ORIGINAL_FIT"),
        ("m1_fit_contract_id", result.fit_contract_id),
        ("m1_original_fit_status", result.original_fit.status),
        ("m1_bootstrap_replicates", str(result.bootstrap_replicates)),
        ("m1_valid_replicates", str(result.valid_replicates)),
        ("m1_failed_replicates", str(result.failed_replicates)),
        ("m1_point_within", "" if not original_fit_admissible or result.point_within is None else format(result.point_within, ".17g")),
        ("m1_point_between", "" if not original_fit_admissible or result.point_between is None else format(result.point_between, ".17g")),
        ("m1_interval_within", repr(result.within_interval)),
        ("m1_interval_between", repr(result.between_interval)),
        ("m1_global_mle_certificate_used", str(result.global_mle_certificate_used)),
    )
    return values + tuple(
        (f"m1_failure_{key}", str(count)) for key, count in result.failure_counts
    )


def compare_f5_dataset(
    rows: Sequence[Sequence[float]], *,
    dataset_id: str,
    target_m: int,
    target_r: int,
    c0_bootstrap_replicates: int,
    c0_bootstrap_seed: int,
    c5_bootstrap_replicates: int,
    c5_bootstrap_seed: int,
    m1_bootstrap_replicates: int,
    m1_bootstrap_seed: int,
    confidence_level: float = 0.95,
) -> M1ChallengerDatasetComparison:
    """Compare frozen C0/C5 through 1.1 and attach M1 intervals without mutation."""
    counts = _binary_count_vector(rows)
    seeds = (c0_bootstrap_seed, c5_bootstrap_seed, m1_bootstrap_seed)
    if any(type(seed) is not int or not 0 <= seed < 2**64 for seed in seeds):
        raise M1ChallengerError("ALL_BOOTSTRAP_SEEDS_MUST_BE_UNSIGNED_64_BIT")
    if len(set(seeds)) != 3:
        raise M1ChallengerError("C0_C5_M1_BOOTSTRAP_SEEDS_MUST_BE_DISTINCT")
    legacy = compare_legacy_dataset(
        rows, dataset_id=dataset_id, family="F5",
        target_m=target_m, target_r=target_r,
        baseline_bootstrap_replicates=c0_bootstrap_replicates,
        baseline_bootstrap_seed=c0_bootstrap_seed,
        bootstrap_replicates=c5_bootstrap_replicates,
        bootstrap_seed=c5_bootstrap_seed,
        confidence_level=confidence_level,
        include_profile_diagnostics=False,
    )
    if legacy.engine_id != "C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.1":
        raise M1ChallengerError("LEGACY_ENGINE_ID_MISMATCH")
    legacy_ids = {legacy.baseline.method_id, *(item.method_id for item in legacy.candidates)}
    if (legacy.baseline.method_id != C0_METHOD_ID
            or len(legacy.candidates) != 1
            or legacy.candidates[0].method_id != C5_METHOD_ID
            or legacy.candidates[0].comparison.method_id != C5_METHOD_ID
            or legacy_ids != {C0_METHOD_ID, C5_METHOD_ID}
            or legacy.unavailable_methods):
        raise M1ChallengerError("LEGACY_C0_C5_ROSTER_MISMATCH")
    if (legacy.input_m != len(rows) or legacy.input_r != len(rows[0])
            or legacy.target_m != target_m or legacy.target_r != target_r):
        raise M1ChallengerError("LEGACY_DESIGN_IDENTITY_MISMATCH")

    m1 = fitted_functional_refit_percentile_bootstrap(
        counts, r=len(rows[0]),
        bootstrap_replicates=m1_bootstrap_replicates,
        bootstrap_seed=m1_bootstrap_seed,
        confidence_level=confidence_level,
    )
    if m1.method_id != M1_METHOD_ID or m1.fit_contract_id != M1_FIT_CONTRACT_ID:
        raise M1ChallengerError("M1_METHOD_OR_FIT_CONTRACT_ID_MISMATCH")
    if m1.status not in {"EMITTED", "ABSTAINED_ORIGINAL_FIT", "ABSTAINED_BOOTSTRAP_FIT_FAILURE"}:
        raise M1ChallengerError("UNKNOWN_M1_RESULT_STATUS")
    if m1.status == "EMITTED" and (m1.within_interval is None or m1.between_interval is None):
        raise M1ChallengerError("M1_EMITTED_STATUS_REQUIRES_BOTH_COMPONENT_INTERVALS")
    if m1.status != "EMITTED" and (m1.within_interval is not None or m1.between_interval is not None):
        raise M1ChallengerError("M1_ABSTENTION_MUST_NOT_CARRY_COMPONENT_INTERVALS")
    common = observed_nested_mr_result(rows, target_m=target_m, target_r=target_r)
    if m1.status == "EMITTED":
        within_interval, between_interval, abstention = (
            m1.within_interval, m1.between_interval, None,
        )
    else:
        within_interval, between_interval = None, None
        abstention = f"M1_{m1.status}"
    m1_comparison = replace(
        common,
        method_id=M1_METHOD_ID,
        within_interval=within_interval,
        between_interval=between_interval,
        mcse_estimate=None,
        mcse_interval=None,
        abstention_reason=("M1_MCSE_INTERVAL_NOT_IMPLEMENTED" if m1.status == "EMITTED" else abstention),
        provenance=common.provenance + (
            ("interval_method", M1_METHOD_ID),
            ("point_metric_contract", "COMMON_RAW_NESTED_MR"),
            ("m1_fit_contract_id", m1.fit_contract_id),
            ("m1_point_estimates_role", "AUXILIARY_MODEL_DIAGNOSTICS_ONLY"),
            ("mcse_estimation_and_interval", "NOT_IMPLEMENTED"),
        ),
    )
    m, r = len(rows), len(rows[0])
    return M1ChallengerDatasetComparison(
        engine_id=ENGINE_ID, dataset_id=dataset_id, family="F5",
        input_m=m, input_r=r, target_m=target_m, target_r=target_r,
        legacy_record=legacy, m1_comparison=m1_comparison,
        m1_result=m1, m1_diagnostics=_m1_diagnostics(m1),
    )


def _validate_roster(record: M1ChallengerDatasetComparison) -> None:
    if record.engine_id != ENGINE_ID or record.family != "F5":
        raise M1ChallengerError("UNKNOWN_ENGINE_OR_FAMILY")
    legacy = record.legacy_record
    if legacy.engine_id != "C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.1":
        raise M1ChallengerError("LEGACY_ENGINE_RECORD_CHANGED")
    if legacy.dataset_id != record.dataset_id or legacy.family != "F5":
        raise M1ChallengerError("LEGACY_DATASET_IDENTITY_MISMATCH")
    ids = {legacy.baseline.method_id, *(x.method_id for x in legacy.candidates),
           record.m1_comparison.method_id}
    if (legacy.baseline.method_id != C0_METHOD_ID
            or len(legacy.candidates) != 1
            or legacy.candidates[0].method_id != C5_METHOD_ID
            or legacy.candidates[0].comparison.method_id != C5_METHOD_ID
            or legacy.unavailable_methods
            or ids != F5_ROSTER or len(ids) != 3):
        raise M1ChallengerError("INCOMPLETE_OR_UNEXPECTED_VERSION_1_2_ROSTER")
    if (legacy.input_m != record.input_m or legacy.input_r != record.input_r
            or legacy.target_m != record.target_m or legacy.target_r != record.target_r):
        raise M1ChallengerError("LEGACY_RECORD_DESIGN_MISMATCH")
    if record.m1_result.method_id != M1_METHOD_ID or record.m1_result.fit_contract_id != M1_FIT_CONTRACT_ID:
        raise M1ChallengerError("M1_RESULT_IDENTITY_MISMATCH")
    if (record.m1_result.target_m != record.input_m
            or record.m1_result.target_r != record.input_r):
        raise M1ChallengerError("M1_RESULT_INPUT_DESIGN_MISMATCH")
    if record.m1_comparison.method_id != M1_METHOD_ID:
        raise M1ChallengerError("M1_METHOD_ID_MISMATCH")
    if (record.m1_comparison.within_interval != record.m1_result.within_interval
            or record.m1_comparison.between_interval != record.m1_result.between_interval):
        raise M1ChallengerError("M1_INTERVAL_PROVENANCE_MISMATCH")
    expected_abstention = (
        "M1_MCSE_INTERVAL_NOT_IMPLEMENTED" if record.m1_result.status == "EMITTED"
        else f"M1_{record.m1_result.status}"
    )
    if record.m1_comparison.abstention_reason != expected_abstention:
        raise M1ChallengerError("M1_ABSTENTION_REASON_MISMATCH")
    if record.m1_comparison.mcse_estimate is not None or record.m1_comparison.mcse_interval is not None:
        raise M1ChallengerError("M1_MCSE_MUST_REMAIN_UNAVAILABLE")
    if record.m1_comparison.method_id == C5_METHOD_ID:
        raise M1ChallengerError("M1_MUST_NOT_OVERWRITE_C5_IDENTITY")


def adjudicate_m1_challenger(
    comparisons: Sequence[M1ChallengerDatasetComparison],
    truths: Sequence[TruthTargets],
) -> tuple[MethodTargetMetrics, ...]:
    """Adjudicate C0/C5/M1 on paired truth; preserve all-dataset emission denominators."""
    records, truth_rows = tuple(comparisons), tuple(truths)
    if not records or len(records) != len(truth_rows):
        raise M1ChallengerError("COMPARISONS_AND_TRUTHS_MUST_BE_NONEMPTY_AND_PAIRED")
    for record in records:
        _validate_roster(record)
    ids = [x.dataset_id for x in records]
    truth_ids = [x.dataset_id for x in truth_rows]
    if len(set(ids)) != len(ids) or len(set(truth_ids)) != len(truth_ids):
        raise M1ChallengerError("DUPLICATE_DATASET_OR_TRUTH_ID")
    if set(ids) != set(truth_ids):
        raise M1ChallengerError("DATASET_TRUTH_ID_MISMATCH")
    if len({(x.input_m, x.input_r, x.target_m, x.target_r) for x in records}) != 1:
        raise M1ChallengerError("STRATIFY_DIFFERENT_INPUT_OR_TARGET_DESIGNS")
    truth_by_id = {x.dataset_id: x for x in truth_rows}
    ordered_truths = tuple(truth_by_id[x.dataset_id] for x in records)
    for truth in ordered_truths:
        for name in ("within", "between", "mcse"):
            value = getattr(truth, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise M1ChallengerError(f"TRUTH_{name.upper()}_MUST_BE_FINITE_AND_NONNEGATIVE")

    output = []
    targets = ("within", "between", "mcse")
    for method_id in (C0_METHOD_ID, C5_METHOD_ID, M1_METHOD_ID):
        for target in targets:
            points, errors, widths = [], [], []
            covered = lower_miss = upper_miss = emitted = 0
            abstentions: dict[str, int] = {}
            for record, truth in zip(records, ordered_truths):
                if method_id == C0_METHOD_ID:
                    comparison = record.legacy_record.baseline
                elif method_id == C5_METHOD_ID:
                    comparison = next(x.comparison for x in record.legacy_record.candidates
                                      if x.method_id == C5_METHOD_ID)
                else:
                    comparison = record.m1_comparison
                true = float(getattr(truth, target))
                point = (getattr(comparison, "between_estimate_raw") if target == "between"
                         else getattr(comparison, f"{target}_estimate"))
                if point is not None and math.isfinite(point):
                    points.append(float(point))
                    errors.append(float(point) - true)
                interval = getattr(comparison, f"{target}_interval")
                if interval is None:
                    reason = comparison.abstention_reason or "INTERVAL_NOT_EMITTED"
                    abstentions[reason] = abstentions.get(reason, 0) + 1
                    continue
                low, high = interval
                if not (math.isfinite(low) and math.isfinite(high) and low <= high):
                    abstentions["INVALID_INTERVAL_OUTPUT"] = abstentions.get("INVALID_INTERVAL_OUTPUT", 0) + 1
                    continue
                emitted += 1
                widths.append(high - low)
                if low <= true <= high:
                    covered += 1
                elif true < low:
                    lower_miss += 1
                else:
                    upper_miss += 1
            n = len(records)
            conditional = covered / emitted if emitted else None
            unconditional = covered / n
            output.append(MethodTargetMetrics(
                method_id=method_id, target=target, n_datasets=n,
                point_emission_rate=len(points) / n,
                point_emission_wilson_95=_wilson(len(points), n),
                point_bias=math.fsum(errors) / len(errors) if errors else None,
                point_rmse=math.sqrt(math.fsum(e * e for e in errors) / len(errors)) if errors else None,
                interval_emission_rate=emitted / n,
                interval_emission_wilson_95=_wilson(emitted, n),
                conditional_coverage=conditional,
                coverage_mcse=(math.sqrt(conditional * (1 - conditional) / emitted)
                               if conditional is not None else None),
                coverage_wilson_95=_wilson(covered, emitted) if emitted else None,
                unconditional_cover_rate=unconditional,
                unconditional_cover_mcse=math.sqrt(unconditional * (1 - unconditional) / n),
                unconditional_cover_wilson_95=_wilson(covered, n),
                lower_miss_rate=lower_miss / emitted if emitted else None,
                upper_miss_rate=upper_miss / emitted if emitted else None,
                mean_interval_width=math.fsum(widths) / len(widths) if widths else None,
                abstention_count=n - emitted,
                abstention_reasons=tuple(sorted(abstentions.items())),
            ))
    return tuple(output)
