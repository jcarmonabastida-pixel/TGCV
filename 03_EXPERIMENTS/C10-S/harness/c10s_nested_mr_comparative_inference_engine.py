"""Unified matched-data F1/F5 nested M/R inference comparison.

Research-only orchestration. C0 calls the frozen v002 implementation directly;
C1 is F1-specific and C5 is F5-specific. No calibration is run here.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import json
import math
from statistics import mean
from types import SimpleNamespace
from typing import Sequence

from c10s_f1_exact_pivotal_candidate import f1_exact_pivotal_result
from c10s_f1_between_profile_likelihood import (
    F1ProfileError, f1_profile_loglik,
    f1_profile_nuisance_stability_diagnostic,
)
from c10s_f1_root_adjudication import adjudicate_f1_roots
from c10s_gaussian_variance_oracles import gaussian_f1_reference
from c10s_f5_beta_binomial_mcse_profile import F5ProfileError, f5_beta_binomial_mcse_profile_loglik
from c10s_f5_beta_binomial_likelihood_diagnostics import (
    F5LikelihoodDiagnosticError,
    beta_binomial_profile_log_concentration,
    beta_binomial_profiled_boundary_likelihoods,
    beta_binomial_profile_numerical_stability,
    build_beta_binomial_profile_audit_record,
)
from c10s_fitted_beta_binomial_bootstrap import (
    FittedBetaBinomialBootstrapResult,
    fitted_beta_binomial_parametric_bootstrap,
)
from c10s_variance_comparison_interface import (
    VarianceComparisonResult,
    observed_nested_mr_result,
)
from theta_a_nested_mc_precision import analyze_nested_precision


ENGINE_ID = "C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.1"
C0_METHOD_ID = "C0_FROZEN_V002_NESTED_PERCENTILE_1.2"
IMPLEMENTED_METHODS = {
    "F1": (C0_METHOD_ID, "C1_F1_EXACT_PIVOTAL_1.0"),
    "F5": (C0_METHOD_ID, "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0"),
}


class ComparativeEngineError(ValueError):
    """Invalid family, comparison record or adjudication input."""


def _f5_profile_diagnostic(
    rows: Sequence[Sequence[float]], *, target_m: int, target_r: int,
    point_mcse: float | None,
) -> tuple[tuple[str, str], ...]:
    if point_mcse is None:
        return (("mcse_profile_status", "NOT_EVALUATED_POINT_MCSE_UNAVAILABLE"),)
    try:
        result = f5_beta_binomial_mcse_profile_loglik(
            rows, target_m=target_m, target_r=target_r,
            target_mcse=point_mcse,
        )
    except F5ProfileError as exc:
        return (
            ("mcse_profile_status", "ABSTAINED_DIAGNOSTIC"),
            ("mcse_profile_reason", str(exc)),
        )
    optimizer_status = dict(result.optimizer_diagnostics).get(
        "optimizer_adjudication", "OPTIMIZATION_DIAGNOSTIC_MISSING",
    )
    policy = {
        "OPTIMIZATION_CONCORDANT": (
            "PROFILE_DIAGNOSTIC_ELIGIBLE_NOT_COVERAGE_CERTIFIED",
            "NONE",
        ),
        "OPTIMIZATION_DISCORDANT": (
            "ABSTAIN_PROFILE_INFERENCE",
            "OPTIMIZER_DISCORDANCE",
        ),
        "OPTIMIZATION_INSUFFICIENT": (
            "ABSTAIN_PROFILE_INFERENCE",
            "INSUFFICIENT_SUCCESSFUL_STARTS",
        ),
        "OPTIMIZATION_BOUNDARY_SENSITIVE": (
            "ABSTAIN_PROFILE_INFERENCE",
            "BOUNDARY_SENSITIVE_OPTIMUM",
        ),
    }.get(optimizer_status, ("ABSTAIN_PROFILE_INFERENCE", "OPTIMIZER_STATUS_UNRECOGNIZED"))
    return (
        ("mcse_profile_status", result.boundary_status),
        ("mcse_profile_inference_eligibility", policy[0]),
        ("mcse_profile_abstention_reason", policy[1]),
        ("mcse_profile_optimizer_adjudication_status", optimizer_status),
        ("mcse_profile_loglik_at_observed_point", format(result.profile_loglik, ".17g")),
        ("mcse_profile_maximizing_branch", result.maximizing_branch),
        ("mcse_profile_maximizing_concentration", (
            "BOUNDARY_LIMIT" if result.maximizing_concentration is None
            else format(result.maximizing_concentration, ".17g")
        )),
        ("mcse_profile_interval", "NOT_EMITTED_NO_LR_CUTOFF_SELECTED"),
        *tuple((f"mcse_profile_{key}", value)
               for key, value in result.optimizer_diagnostics),
    )


def _f1_profile_diagnostic(
    rows: Sequence[Sequence[float]], result: VarianceComparisonResult,
) -> tuple[tuple[str, str], ...]:
    tau = max(0.0, result.between_estimate_raw)
    try:
        optimizer = f1_profile_nuisance_stability_diagnostic(
            rows, between_variance=tau,
        )
        value = f1_profile_loglik(rows, between_variance=tau)
    except F1ProfileError as exc:
        return (
            ("between_profile_status", "ABSTAINED_DIAGNOSTIC"),
            ("between_profile_inference_eligibility", "ABSTAIN_PROFILE_INFERENCE"),
            ("between_profile_abstention_reason", str(exc)),
            ("between_profile_reason", str(exc)),
            ("between_profile_interval", "NOT_EMITTED_NO_LR_CUTOFF_SELECTED"),
        )
    policy = {
        "OPTIMIZATION_CONCORDANT": (
            "PROFILE_DIAGNOSTIC_ELIGIBLE_NOT_COVERAGE_CERTIFIED", "NONE",
        ),
        "OPTIMIZATION_DISCORDANT": (
            "ABSTAIN_PROFILE_INFERENCE", "NUISANCE_OPTIMIZER_DISCORDANCE",
        ),
        "OPTIMIZATION_INSUFFICIENT": (
            "ABSTAIN_PROFILE_INFERENCE", "NUISANCE_OPTIMIZER_INSUFFICIENT",
        ),
        "OPTIMIZATION_BOUNDARY_SENSITIVE": (
            "ABSTAIN_PROFILE_INFERENCE", "NUISANCE_OPTIMUM_BOUNDARY_SENSITIVE",
        ),
    }.get(optimizer.status, (
        "ABSTAIN_PROFILE_INFERENCE", "NUISANCE_OPTIMIZER_STATUS_UNRECOGNIZED",
    ))
    try:
        root_adjudication = adjudicate_f1_roots(
            rows, between_variance=tau,
        )
    except (F1ProfileError, ValueError, ArithmeticError) as exc:
        root_status = "ROOTS_UNRESOLVED"
        root_reason = f"ROOT_ADJUDICATION_ERROR:{exc}"
        root_counts = ("", "", "")
        root_domain = "(0,+infinity)"
        zero_factor_multiplicity = ""
        boundary_root_text = ""
        isolator_interval_text = ""
    else:
        root_status = root_adjudication.status
        root_reason = root_adjudication.reason
        root_counts = (
            str(root_adjudication.f1_root_count),
            str(root_adjudication.independent_root_count),
            str(root_adjudication.matched_root_count),
        )
        root_domain = root_adjudication.root_domain
        zero_factor_multiplicity = str(
            root_adjudication.removed_zero_factor_multiplicity,
        )
        boundary_root_text = ";".join(
            f"{lower}..{upper}*{multiplicity}"
            for lower, upper, multiplicity in root_adjudication.boundary_roots
        )
        isolator_interval_text = ";".join(
            f"{lower}..{upper}*{multiplicity}"
            for lower, upper, multiplicity in root_adjudication.independent_intervals
        )
    if root_status != "ROOTS_AGREE":
        policy = (
            "ABSTAIN_PROFILE_INFERENCE",
            "INDEPENDENT_ROOT_ADJUDICATION_" + root_status,
        )
    return (
        ("between_profile_status", "LOG_LIKELIHOOD_DIAGNOSTIC_AVAILABLE"),
        ("between_profile_inference_eligibility", policy[0]),
        ("between_profile_abstention_reason", policy[1]),
        ("between_profile_optimizer_adjudication_status", optimizer.status),
        ("between_profile_root_adjudication_status", root_status),
        ("between_profile_root_adjudication_reason", root_reason),
        ("between_profile_root_adjudication_f1_count", root_counts[0]),
        ("between_profile_root_adjudication_sturm_count", root_counts[1]),
        ("between_profile_root_adjudication_matched_count", root_counts[2]),
        ("between_profile_root_adjudication_domain", root_domain),
        ("between_profile_root_adjudication_removed_zero_factor_multiplicity", zero_factor_multiplicity),
        ("between_profile_root_adjudication_boundary_roots", boundary_root_text),
        ("between_profile_root_adjudication_exact_intervals", isolator_interval_text),
        ("between_profile_optimizer_stationary_point_counts",
         ",".join(str(value) for value in optimizer.stationary_point_counts)),
        ("between_profile_optimizer_stationary_point_types",
         ";".join("|".join(types) for types in optimizer.stationary_point_type_signatures)),
        ("between_profile_optimizer_tangential_score_root_counts",
         ",".join(str(value) for value in optimizer.tangential_score_root_counts)),
        ("between_profile_optimizer_unresolved_tangential_candidate_counts",
         ",".join(str(value) for value in optimizer.unresolved_tangential_candidate_counts)),
        ("between_profile_optimizer_polynomial_degrees",
         ",".join(str(value) for value in optimizer.polynomial_degrees)),
        ("between_profile_optimizer_polynomial_root_counts",
         ",".join(str(value) for value in optimizer.polynomial_root_counts)),
        ("between_profile_optimizer_polynomial_statuses",
         ",".join(optimizer.polynomial_statuses)),
        ("between_profile_optimizer_critical_point_solver_statuses",
         ",".join(optimizer.critical_point_solver_statuses)),
        ("between_profile_optimizer_polynomial_scan_discordances",
         ",".join(str(value) for value in optimizer.polynomial_scan_discordances)),
        ("between_profile_optimizer_grid_span_configurations",
         ";".join(f"{grid}@{span:g}" for grid, span in optimizer.configurations)),
        ("between_profile_optimizer_loglik_spread",
         "" if optimizer.maximum_loglik_spread is None
         else format(optimizer.maximum_loglik_spread, ".17g")),
        ("between_profile_optimizer_stationary_location_spread",
         "" if optimizer.maximum_stationary_location_spread is None
         else format(optimizer.maximum_stationary_location_spread, ".17g")),
        ("between_profile_loglik_at_nonnegative_raw_estimate", format(value, ".17g")),
        ("between_profile_tau_evaluation", format(tau, ".17g")),
        ("between_profile_interval", "NOT_EMITTED_NO_LR_CUTOFF_SELECTED"),
    )


@dataclass(frozen=True)
class CandidateOutput:
    method_id: str
    comparison: VarianceComparisonResult
    diagnostics: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class DatasetComparison:
    engine_id: str
    dataset_id: str
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
    dataset_id: str
    within: float
    between: float
    mcse: float


@dataclass(frozen=True)
class ProfileDiagnosticMetrics:
    """Operational profile diagnostics; deliberately separate from interval coverage."""
    family: str
    diagnostic: str
    n_datasets: int
    eligible_count: int
    abstained_count: int
    not_evaluated_count: int
    eligible_rate: float
    abstention_reasons: tuple[tuple[str, int], ...]
    statuses: tuple[tuple[str, int], ...]


@dataclass(frozen=True)
class MethodTargetMetrics:
    method_id: str
    target: str
    n_datasets: int
    point_emission_rate: float
    point_emission_wilson_95: tuple[float, float]
    point_bias: float | None
    point_rmse: float | None
    interval_emission_rate: float
    interval_emission_wilson_95: tuple[float, float]
    conditional_coverage: float | None
    coverage_mcse: float | None
    coverage_wilson_95: tuple[float, float] | None
    unconditional_cover_rate: float
    unconditional_cover_mcse: float
    unconditional_cover_wilson_95: tuple[float, float]
    lower_miss_rate: float | None
    upper_miss_rate: float | None
    mean_interval_width: float | None
    abstention_count: int
    abstention_reasons: tuple[tuple[str, int], ...]


def _wilson(successes: int, trials: int) -> tuple[float, float]:
    if trials <= 0:
        raise ComparativeEngineError("WILSON_REQUIRES_POSITIVE_DENOMINATOR")
    z = 1.959963984540054
    p = successes / trials
    denominator = 1.0 + z * z / trials
    center = (p + z * z / (2.0 * trials)) / denominator
    half = z * math.sqrt(
        p * (1.0 - p) / trials + z * z / (4.0 * trials * trials)
    ) / denominator
    return max(0.0, center - half), min(1.0, center + half)


def _finite_json_value(value):
    """Encode extended-real diagnostic values as explicit JSON strings."""
    if isinstance(value, float) and not math.isfinite(value):
        return "NaN" if math.isnan(value) else "Infinity" if value > 0 else "-Infinity"
    if isinstance(value, dict):
        return {key: _finite_json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_finite_json_value(item) for item in value]
    return value


def _unsigned_seed(value: int, name: str) -> None:
    if type(value) is not int or not 0 <= value < 2**64:
        raise ComparativeEngineError(f"{name}_MUST_BE_UNSIGNED_64_BIT_INTEGER")


def _frozen_v002_baseline(
    rows: Sequence[Sequence[float]], *, dataset_id: str,
    target_m: int, target_r: int,
    bootstrap_replicates: int, bootstrap_seed: int,
) -> VarianceComparisonResult:
    """Thin adapter to the frozen v002 callable; no copied bootstrap logic."""
    common = observed_nested_mr_result(
        rows, target_m=target_m, target_r=target_r,
    )
    matrix = tuple(tuple(float(x) for x in row) for row in rows)
    m, r = len(matrix), len(matrix[0])
    world_means = tuple(math.fsum(row) / r for row in matrix)
    grand_mean = math.fsum(world_means) / m
    world_variance = common.observed_world_variance
    summary = SimpleNamespace(
        metric="fixture_scalar",
        mean=grand_mean,
        mcse=math.sqrt(world_variance / m),
        outer_world_contributions=tuple(
            (f"{dataset_id}-M{index:04d}", value)
            for index, value in enumerate(world_means)
        ),
    )
    legacy = analyze_nested_precision(
        metric="fixture_scalar",
        replicate_contributions=matrix,
        summary_metric=summary,
        outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
        outer_world_sampling_contract_id=f"C10S-COMPARISON-M-{dataset_id}",
        outer_world_sampling_contract_version="1.0",
        outer_world_sampling_independence_basis="Synthetic fixture generator declares independent outer draws.",
        within_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
        within_world_sampling_contract_id=f"C10S-COMPARISON-R-{dataset_id}",
        within_world_sampling_contract_version="1.0",
        within_world_sampling_independence_basis="Synthetic fixture generator declares independent conditional inner draws.",
        projections=((target_m, target_r),),
        bootstrap_replicates=bootstrap_replicates,
        bootstrap_seed=bootstrap_seed,
    )
    reconciliations = (
        ("within", legacy.within_ms, common.within_estimate),
        ("between_raw", legacy.between_raw, common.between_estimate_raw),
        ("world_mean_variance", legacy.observed_world_mean_variance, common.observed_world_variance),
    )
    for label, legacy_value, common_value in reconciliations:
        tolerance = 1e-10 * max(1.0, abs(legacy_value), abs(common_value))
        if abs(legacy_value - common_value) > tolerance:
            raise ComparativeEngineError(f"C0_V002_COMMON_ESTIMAND_RECONCILIATION_FAILURE:{label}")
    intervals = {name: (low, high) for name, low, high in legacy.component_intervals}
    projection = legacy.projections[0]
    mcse_interval = (
        (projection[2], projection[3])
        if projection[2] is not None and projection[3] is not None
        else None
    )
    flags = list(common.boundary_flags)
    if legacy.bootstrap_degenerate:
        flags.append("BOOTSTRAP_DEGENERATE")
    reason = None if mcse_interval is not None else projection[4]
    return replace(
        common,
        method_id=C0_METHOD_ID,
        within_interval=intervals["within_ms"],
        between_interval=intervals["between_raw"],
        mcse_interval=mcse_interval,
        boundary_flags=tuple(flags),
        abstention_reason=reason,
        provenance=common.provenance + (
            ("protocol_id", "C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001"),
            ("protocol_version", "002"),
            ("method_version", "1.2"),
            ("bootstrap_replicates", str(bootstrap_replicates)),
            ("bootstrap_seed", str(bootstrap_seed)),
            ("bootstrap_law", "frozen_v002_two_stage_outer_cluster_then_inner_R"),
            ("legacy_projection_status", projection[4]),
            ("common_estimand_reconciliation", "PASS_V002_POINT_TARGETS"),
            ("legacy_boundary_fraction", format(legacy.boundary_fraction or 0.0, ".17g")),
        ),
    )


def _f5_concentration_profile_audit_diagnostics(
    rows: Sequence[Sequence[float]],
    optimizer_audit,
    log_concentration_grid: Sequence[float],
) -> tuple[tuple[str, str], ...]:
    """Serialize B1 concentration-profile and numerical-stability audits.

    This is opt-in and diagnostic-only. The supplied concentration grid is
    explicit; no data-dependent range, threshold, or identification verdict
    is inferred. These diagnostics never alter the fitted C5 candidate.
    """
    counts = tuple(sum(int(value) for value in row) for row in rows)
    r = len(rows[0])
    profile_record = None
    profile_error = None
    stability_record = None
    stability_error = None
    try:
        if optimizer_audit is None:
            raise F5LikelihoodDiagnosticError("OPTIMIZER_AUDIT_UNAVAILABLE")
        profile = beta_binomial_profile_log_concentration(
            counts, r, log_concentration_grid,
        )
        boundary = beta_binomial_profiled_boundary_likelihoods(counts, r)
        profile_record = build_beta_binomial_profile_audit_record(
            optimizer_audit, profile, boundary,
        )
    except (F5LikelihoodDiagnosticError, ArithmeticError, ValueError) as exc:
        profile_error = f"{type(exc).__name__}:{exc}"
    try:
        stability_record = beta_binomial_profile_numerical_stability(
            counts, r, log_concentration_grid,
            mean_logit_bounds=(-18.0, 18.0),
            expanded_mean_logit_bounds=(-24.0, 24.0),
            mean_grid_size=65,
            refined_mean_grid_size=257,
        )
    except (F5LikelihoodDiagnosticError, ArithmeticError, ValueError) as exc:
        stability_error = f"{type(exc).__name__}:{exc}"
    return (
        ("concentration_profile_audit_json", (
            json.dumps(_finite_json_value(asdict(profile_record)),
                       sort_keys=True, separators=(",", ":"), allow_nan=False)
            if profile_record is not None else "null"
        )),
        ("concentration_profile_audit_error", profile_error or "NONE"),
        ("concentration_profile_stability_json", (
            json.dumps(_finite_json_value(asdict(stability_record)),
                       sort_keys=True, separators=(",", ":"), allow_nan=False)
            if stability_record is not None else "null"
        )),
        ("concentration_profile_stability_error", stability_error or "NONE"),
    )


def compare_dataset(
    rows: Sequence[Sequence[float]], *,
    dataset_id: str,
    family: str,
    target_m: int,
    target_r: int,
    baseline_bootstrap_replicates: int,
    baseline_bootstrap_seed: int,
    confidence_level: float = 0.95,
    bootstrap_replicates: int | None = None,
    bootstrap_seed: int | None = None,
    include_profile_diagnostics: bool = True,
    include_f5_concentration_profile_audit: bool = False,
    f5_profile_log_concentration_grid: Sequence[float] | None = None,
    require_f5_global_mle_certificate: bool = False,
) -> DatasetComparison:
    """Run C0 plus the currently implemented family-specific candidate."""
    if family not in IMPLEMENTED_METHODS:
        raise ComparativeEngineError("SUPPORTED_FAMILIES_ARE_F1_AND_F5")
    if not isinstance(include_profile_diagnostics, bool):
        raise ComparativeEngineError("INCLUDE_PROFILE_DIAGNOSTICS_MUST_BE_BOOLEAN")
    if not isinstance(include_f5_concentration_profile_audit, bool):
        raise ComparativeEngineError("INCLUDE_F5_CONCENTRATION_PROFILE_AUDIT_MUST_BE_BOOLEAN")
    if not isinstance(require_f5_global_mle_certificate, bool):
        raise ComparativeEngineError("REQUIRE_F5_GLOBAL_MLE_CERTIFICATE_MUST_BE_BOOLEAN")
    if include_f5_concentration_profile_audit:
        if family != "F5":
            raise ComparativeEngineError("F5_CONCENTRATION_PROFILE_AUDIT_REQUIRES_F5_FAMILY")
        if f5_profile_log_concentration_grid is None:
            raise ComparativeEngineError("F5_CONCENTRATION_PROFILE_GRID_REQUIRED")
    elif f5_profile_log_concentration_grid is not None:
        raise ComparativeEngineError("F5_PROFILE_GRID_REQUIRES_AUDIT_ENABLED")
    if (isinstance(confidence_level, bool) or not isinstance(confidence_level, (int, float))
            or not math.isfinite(confidence_level) or abs(float(confidence_level) - 0.95) > 1e-12):
        raise ComparativeEngineError("COMPARISON_NOMINAL_LEVEL_MUST_MATCH_FROZEN_C0_V002_95_PERCENT")
    if not isinstance(dataset_id, str) or not dataset_id.strip():
        raise ComparativeEngineError("NONEMPTY_DATASET_ID_REQUIRED")
    if type(target_m) is not int or target_m < 2 or type(target_r) is not int or target_r < 2:
        raise ComparativeEngineError("INVALID_TARGET_DESIGN")
    if type(baseline_bootstrap_replicates) is not int or baseline_bootstrap_replicates < 100:
        raise ComparativeEngineError("C0_BASELINE_BOOTSTRAP_REPLICATES_MUST_BE_INTEGER_GE_100")
    _unsigned_seed(baseline_bootstrap_seed, "C0_BASELINE_BOOTSTRAP_SEED")

    common = observed_nested_mr_result(rows, target_m=target_m, target_r=target_r)
    m, r = len(rows), len(rows[0])
    baseline = _frozen_v002_baseline(
        rows, dataset_id=dataset_id, target_m=target_m, target_r=target_r,
        bootstrap_replicates=baseline_bootstrap_replicates,
        bootstrap_seed=baseline_bootstrap_seed,
    )
    outputs: list[CandidateOutput] = []

    if family == "F1":
        result = f1_exact_pivotal_result(
            rows, target_m=target_m, target_r=target_r,
            family="F1", confidence_level=confidence_level,
        )
        oracle = gaussian_f1_reference(
            m=m, r=r, msw=result.within_estimate,
            world_mean_variance=result.observed_world_variance,
            confidence=confidence_level,
        )
        oracle_delta = max(
            abs(result.between_interval[0] - oracle.between_raw_conservative_interval[0]),
            abs(result.between_interval[1] - oracle.between_raw_conservative_interval[1]),
        )
        tolerance = 1e-10 * max(1.0, *(abs(x) for x in oracle.between_raw_conservative_interval))
        if oracle_delta > tolerance:
            raise ComparativeEngineError("F1_C1_ORACLE_RECONCILIATION_FAILURE")
        diagnostics = (
            ("inference_scope", "balanced_gaussian_random_intercept_only"),
            ("independent_oracle_reconciliation", "PASS_FORMULA_AGREEMENT"),
            ("oracle_max_abs_delta_between_interval", format(oracle_delta, ".17g")),
        )
        if include_profile_diagnostics:
            diagnostics += _f1_profile_diagnostic(rows, result)
        outputs.append(CandidateOutput(
            method_id=result.method_id, comparison=result, diagnostics=diagnostics,
        ))
    else:
        if bootstrap_replicates is None or bootstrap_seed is None:
            raise ComparativeEngineError("F5_REQUIRES_EXPLICIT_C5_BOOTSTRAP_REPLICATES_AND_SEED")
        fitted: FittedBetaBinomialBootstrapResult = fitted_beta_binomial_parametric_bootstrap(
            rows, target_m=target_m, target_r=target_r,
            bootstrap_replicates=bootstrap_replicates,
            bootstrap_seed=bootstrap_seed,
            confidence_level=confidence_level,
            require_global_mle_certificate=require_f5_global_mle_certificate,
        )
        fit = fitted.fit
        global_cert_status = str((fitted.global_mle_certificate or {}).get("status", "NOT_REQUIRED"))
        if fit is None:
            fit_status = "ABSTAINED"
        elif require_f5_global_mle_certificate and global_cert_status != "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED":
            fit_status = "GLOBAL_MLE_CERTIFICATION_ABSTAINED"
        else:
            fit_status = "BOUNDARY" if fit.boundary else "INTERIOR"
        diagnostics = (
            ("fit_status", fit_status),
            ("bootstrap_replicates", str(fitted.bootstrap_replicates)),
            ("projectable_mcse_replicates", str(fitted.valid_mcse_replicates)),
            ("projectable_mcse_draw_fraction", format(fitted.valid_mcse_rate, ".17g")),
            ("bootstrap_seed", str(fitted.bootstrap_seed)),
            ("mcse_interval_status", "NOT_IMPLEMENTED_BOUNDARY_AWARE_JOINT_INFERENCE"),
            ("failure_reason", fitted.failure_reason or "NONE"),
            ("likelihood_optimizer_audit_json", (
                json.dumps(
                    _finite_json_value(asdict(fitted.optimizer_audit)),
                    sort_keys=True, separators=(",", ":"), allow_nan=False,
                )
                if fitted.optimizer_audit is not None else "null"
            )),
            ("likelihood_optimizer_audit_error", fitted.optimizer_audit_error or "NONE"),
            ("production_analytic_reconciliation_json", (
                json.dumps(
                    _finite_json_value(fitted.production_analytic_reconciliation),
                    sort_keys=True, separators=(",", ":"), allow_nan=False,
                )
                if fitted.production_analytic_reconciliation is not None else "null"
            )),
        )
        if include_profile_diagnostics:
            diagnostics += _f5_profile_diagnostic(
                rows, target_m=target_m, target_r=target_r,
                point_mcse=fitted.comparison.mcse_estimate,
            )
        if include_f5_concentration_profile_audit:
            diagnostics += _f5_concentration_profile_audit_diagnostics(
                rows, fitted.optimizer_audit, f5_profile_log_concentration_grid,
            )
        outputs.append(CandidateOutput(
            method_id=fitted.comparison.method_id,
            comparison=fitted.comparison,
            diagnostics=diagnostics,
        ))

    return DatasetComparison(
        engine_id=ENGINE_ID, dataset_id=dataset_id, family=family,
        input_m=m, input_r=r, target_m=target_m, target_r=target_r,
        baseline=baseline, candidates=tuple(outputs), unavailable_methods=("C2", "C3", "C4"),
    )


def adjudicate_matched_datasets(
    comparisons: Sequence[DatasetComparison],
    truths: Sequence[TruthTargets],
) -> tuple[MethodTargetMetrics, ...]:
    """Adjudicate complete paired rosters; never hide missing methods or abstentions."""
    records = tuple(comparisons)
    truth_rows = tuple(truths)
    if not records or len(records) != len(truth_rows):
        raise ComparativeEngineError("COMPARISONS_AND_TRUTHS_MUST_BE_NONEMPTY_AND_PAIRED")
    families = {record.family for record in records}
    if len(families) != 1:
        raise ComparativeEngineError("ONE_FAMILY_PER_ADJUDICATION_BATCH")
    if any(record.engine_id != ENGINE_ID for record in records):
        raise ComparativeEngineError("UNKNOWN_ENGINE_RECORD")
    dataset_ids = [record.dataset_id for record in records]
    truth_ids = [truth.dataset_id for truth in truth_rows]
    if any(not isinstance(value, str) or not value.strip() for value in dataset_ids + truth_ids):
        raise ComparativeEngineError("DATASET_AND_TRUTH_IDS_REQUIRED")
    if len(set(dataset_ids)) != len(dataset_ids) or len(set(truth_ids)) != len(truth_ids):
        raise ComparativeEngineError("DUPLICATE_DATASET_OR_TRUTH_ID")
    if set(dataset_ids) != set(truth_ids):
        raise ComparativeEngineError("DATASET_TRUTH_ID_MISMATCH")
    truth_by_id = {truth.dataset_id: truth for truth in truth_rows}
    ordered_truths = tuple(truth_by_id[record.dataset_id] for record in records)
    for truth in ordered_truths:
        for name, value in (("within", truth.within), ("between", truth.between), ("mcse", truth.mcse)):
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or value < 0.0):
                raise ComparativeEngineError(f"TRUTH_{name.upper()}_MUST_BE_FINITE_AND_NONNEGATIVE")

    target_designs = {(record.target_m, record.target_r) for record in records}
    input_designs = {(record.input_m, record.input_r) for record in records}
    if len(target_designs) != 1 or len(input_designs) != 1:
        raise ComparativeEngineError("STRATIFY_DIFFERENT_INPUT_OR_TARGET_DESIGNS")

    family = next(iter(families))
    if family not in IMPLEMENTED_METHODS:
        raise ComparativeEngineError("UNSUPPORTED_ADJUDICATION_FAMILY")
    expected = set(IMPLEMENTED_METHODS[family])
    for record in records:
        candidate_ids = [candidate.method_id for candidate in record.candidates]
        if any(candidate.method_id != candidate.comparison.method_id for candidate in record.candidates):
            raise ComparativeEngineError("CANDIDATE_METHOD_ID_COMPARISON_MISMATCH")
        if len(candidate_ids) != len(set(candidate_ids)):
            raise ComparativeEngineError("DUPLICATE_CANDIDATE_METHOD_ID")
        roster = {record.baseline.method_id, *candidate_ids}
        if roster != expected:
            raise ComparativeEngineError("INCOMPLETE_OR_UNEXPECTED_METHOD_ROSTER")
        if record.baseline.method_id != C0_METHOD_ID:
            raise ComparativeEngineError("FROZEN_C0_BASELINE_REQUIRED")

    method_ids = sorted(expected)
    targets = ("within", "between", "mcse")
    output: list[MethodTargetMetrics] = []
    n = len(records)

    for method_id in method_ids:
        for target in targets:
            points: list[float] = []
            errors: list[float] = []
            widths: list[float] = []
            covered = lower_miss = upper_miss = 0
            interval_emitted = 0
            abstentions: dict[str, int] = {}
            for record, truth in zip(records, ordered_truths):
                comparison = (
                    record.baseline if method_id == C0_METHOD_ID
                    else next(item.comparison for item in record.candidates if item.method_id == method_id)
                )
                true_value = float(getattr(truth, target))
                point_value = (
                    getattr(comparison, "between_estimate_raw")
                    if target == "between"
                    else getattr(comparison, f"{target}_estimate")
                )
                if point_value is not None and math.isfinite(point_value):
                    points.append(float(point_value))
                    errors.append(float(point_value) - true_value)
                interval = getattr(comparison, f"{target}_interval")
                if interval is None:
                    reason = comparison.abstention_reason or "INTERVAL_NOT_EMITTED"
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

            point_emission = len(points) / n
            interval_emission = interval_emitted / n
            conditional = covered / interval_emitted if interval_emitted else None
            coverage_mcse = (
                math.sqrt(conditional * (1.0 - conditional) / interval_emitted)
                if conditional is not None else None
            )
            coverage_wilson = _wilson(covered, interval_emitted) if interval_emitted else None
            unconditional = covered / n
            output.append(MethodTargetMetrics(
                method_id=method_id, target=target, n_datasets=n,
                point_emission_rate=point_emission,
                point_emission_wilson_95=_wilson(len(points), n),
                point_bias=math.fsum(errors) / len(errors) if errors else None,
                point_rmse=math.sqrt(math.fsum(error * error for error in errors) / len(errors)) if errors else None,
                interval_emission_rate=interval_emission,
                interval_emission_wilson_95=_wilson(interval_emitted, n),
                conditional_coverage=conditional,
                coverage_mcse=coverage_mcse,
                coverage_wilson_95=coverage_wilson,
                unconditional_cover_rate=unconditional,
                unconditional_cover_mcse=math.sqrt(unconditional * (1.0 - unconditional) / n),
                unconditional_cover_wilson_95=_wilson(covered, n),
                lower_miss_rate=lower_miss / interval_emitted if interval_emitted else None,
                upper_miss_rate=upper_miss / interval_emitted if interval_emitted else None,
                mean_interval_width=math.fsum(widths) / len(widths) if widths else None,
                abstention_count=n - interval_emitted,
                abstention_reasons=tuple(sorted(abstentions.items())),
            ))
    return tuple(output)


def adjudicate_profile_diagnostics(
    comparisons: Sequence[DatasetComparison],
) -> tuple[ProfileDiagnosticMetrics, ...]:
    """Summarize F1/F5 profile diagnostics without scoring interval coverage.

    F1's current signal is a point evaluation of the nuisance-profiled
    likelihood; F5's is an optimizer-adjudication diagnostic. Neither is a
    confidence interval or coverage result. Missing, failed and eligible
    diagnostics remain distinct; no truth values enter this function.
    """
    records = tuple(comparisons)
    if not records:
        raise ComparativeEngineError("PROFILE_DIAGNOSTIC_ROSTER_MUST_BE_NONEMPTY")
    families = {record.family for record in records}
    if len(families) != 1 or next(iter(families)) not in {"F1", "F5"}:
        raise ComparativeEngineError("PROFILE_DIAGNOSTICS_REQUIRE_ONE_FAMILY_F1_OR_F5")
    family = next(iter(families))
    if any(record.engine_id != ENGINE_ID for record in records):
        raise ComparativeEngineError("UNKNOWN_ENGINE_RECORD")
    ids = [record.dataset_id for record in records]
    if any(not isinstance(value, str) or not value.strip() for value in ids):
        raise ComparativeEngineError("DATASET_IDS_REQUIRED")
    if len(set(ids)) != len(ids):
        raise ComparativeEngineError("DUPLICATE_DATASET_IDS")
    designs = {(record.input_m, record.input_r, record.target_m, record.target_r)
               for record in records}
    if len(designs) != 1:
        raise ComparativeEngineError("STRATIFY_PROFILE_DIAGNOSTICS_BY_DESIGN")

    statuses: dict[str, int] = {}
    reasons: dict[str, int] = {}
    eligible = abstained = not_evaluated = 0
    for record in records:
        expected_method = (
            "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0"
            if family == "F5" else "C1_F1_EXACT_PIVOTAL_1.0"
        )
        candidate = next(
            (item for item in record.candidates if item.method_id == expected_method),
            None,
        )
        if candidate is None:
            raise ComparativeEngineError(f"{family}_PROFILE_CANDIDATE_MISSING")
        diagnostics = dict(candidate.diagnostics)
        prefix = "mcse_profile" if family == "F5" else "between_profile"
        status = diagnostics.get(f"{prefix}_inference_eligibility")
        if status == "PROFILE_DIAGNOSTIC_ELIGIBLE_NOT_COVERAGE_CERTIFIED":
            eligible += 1
        elif status == "ABSTAIN_PROFILE_INFERENCE":
            abstained += 1
            reason = diagnostics.get(f"{prefix}_abstention_reason", "ABSTENTION_REASON_MISSING")
            reasons[reason] = reasons.get(reason, 0) + 1
        else:
            not_evaluated += 1
            status = status or diagnostics.get(f"{prefix}_status", "PROFILE_DIAGNOSTIC_MISSING")
        statuses[status] = statuses.get(status, 0) + 1

    n = len(records)
    return (ProfileDiagnosticMetrics(
        family=family,
        diagnostic=("MCSE_PROFILE_OPTIMIZATION" if family == "F5"
                    else "BETWEEN_VARIANCE_PROFILE_LOG_LIKELIHOOD"),
        n_datasets=n, eligible_count=eligible, abstained_count=abstained,
        not_evaluated_count=not_evaluated, eligible_rate=eligible / n,
        abstention_reasons=tuple(sorted(reasons.items())),
        statuses=tuple(sorted(statuses.items())),
    ),)
