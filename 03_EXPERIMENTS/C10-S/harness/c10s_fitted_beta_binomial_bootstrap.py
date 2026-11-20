"""Fitted beta-binomial parametric-bootstrap candidate for F5.

Development implementation only. It does not calibrate coverage or select a
method. All bootstrap replicates are generated from a fitted beta-binomial
world-cluster model and the complete raw nested M/R estimator is recomputed.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import math
from typing import Sequence

import numpy as np
from scipy.optimize import minimize
from scipy.special import betaln, gammaln

from c10s_f5_beta_binomial_likelihood_diagnostics import (
    BetaBinomialOptimizerAudit,
    F5LikelihoodDiagnosticError,
    audit_beta_binomial_count_fit,
)
from c10s_variance_comparison_interface import (
    ComparisonInputError,
    VarianceComparisonResult,
    observed_nested_mr_result,
)


class BetaBinomialFitError(ValueError):
    """The F5 beta-binomial model cannot be fitted admissibly."""


@dataclass(frozen=True)
class BetaBinomialProductionStartOutcome:
    """Raw finite-difference L-BFGS-B production-start outcome."""
    start_index: int
    initial_mean_logit: float
    initial_log_concentration: float
    success: bool
    message: str
    final_mean_logit: float | None
    final_log_concentration: float | None
    negative_log_likelihood: float | None
    gradient_norm: float | None
    lower_mean_bound_distance: float | None
    upper_mean_bound_distance: float | None
    lower_concentration_bound_distance: float | None
    upper_concentration_bound_distance: float | None


@dataclass(frozen=True)
class BetaBinomialFit:
    alpha: float
    beta: float
    mean_probability: float
    concentration: float
    log_likelihood: float
    converged: bool
    boundary: bool
    boundary_reasons: tuple[str, ...]
    optimizer_message: str
    selected_start_index: int = -1
    production_starts: tuple[BetaBinomialProductionStartOutcome, ...] = ()


@dataclass(frozen=True)
class FittedBetaBinomialBootstrapResult:
    comparison: VarianceComparisonResult
    fit: BetaBinomialFit | None
    bootstrap_replicates: int
    valid_mcse_replicates: int
    valid_mcse_rate: float
    confidence_level: float
    bootstrap_seed: int
    failure_reason: str | None
    optimizer_audit: BetaBinomialOptimizerAudit | None = None
    optimizer_audit_error: str | None = None
    production_analytic_reconciliation: dict | None = None


def fit_beta_binomial_counts(counts: Sequence[int], r: int) -> BetaBinomialFit:
    """MLE of beta-binomial mean and concentration from M cluster counts."""
    x = np.asarray(tuple(counts), dtype=float)
    if x.ndim != 1 or x.size < 2:
        raise BetaBinomialFitError("at least two world-cluster counts are required")
    if type(r) is not int or r < 2:
        raise BetaBinomialFitError("r must be an integer >= 2")
    if not np.all(np.isfinite(x)) or np.any(x < 0) or np.any(x > r):
        raise BetaBinomialFitError("counts must be finite and lie in [0,r]")
    if not np.all(x == np.floor(x)):
        raise BetaBinomialFitError("world-cluster counts must be integers")
    if np.all(x == 0) or np.all(x == r):
        raise BetaBinomialFitError("ALL_ZERO_OR_ALL_ONE_BOUNDARY")
    if np.all(x == x[0]):
        raise BetaBinomialFitError("NO_BETWEEN_CLUSTER_COUNT_VARIATION_BOUNDARY")

    m = int(x.size)
    empirical_mean = float(np.mean(x) / r)
    # Mean-logit and log-concentration avoid alpha/beta sign constraints.
    eps = 1e-6
    mean0 = min(1.0 - eps, max(eps, empirical_mean))
    logit0 = math.log(mean0 / (1.0 - mean0))
    starts = (
        np.asarray([logit0, math.log(2.0)]),
        np.asarray([logit0, math.log(0.5)]),
        np.asarray([logit0, math.log(20.0)]),
    )
    bounds = ((-18.0, 18.0), (-12.0, 18.0))

    def nll(parameters: np.ndarray) -> float:
        logit_mean, log_concentration = (float(v) for v in parameters)
        mean = 1.0 / (1.0 + math.exp(-logit_mean))
        concentration = math.exp(log_concentration)
        alpha = mean * concentration
        beta = (1.0 - mean) * concentration
        log_choose = (
            gammaln(r + 1.0) - gammaln(x + 1.0) - gammaln(r - x + 1.0)
        )
        ll = log_choose + betaln(x + alpha, r - x + beta) - betaln(alpha, beta)
        value = -float(np.sum(ll))
        return value if math.isfinite(value) else 1e300

    fits = [
        minimize(nll, start, method="L-BFGS-B", bounds=bounds,
                 options={"maxiter": 4000, "ftol": 1e-12, "gtol": 1e-8})
        for start in starts
    ]
    production_starts = []
    for index, (start, result) in enumerate(zip(starts, fits)):
        coordinates_finite = bool(np.all(np.isfinite(result.x)))
        eta_i = float(result.x[0]) if coordinates_finite else None
        xi_i = float(result.x[1]) if coordinates_finite else None
        jac = getattr(result, "jac", None)
        jac_array = np.asarray(jac, dtype=float) if jac is not None else None
        gradient_norm = (
            float(np.linalg.norm(jac_array))
            if jac_array is not None and np.all(np.isfinite(jac_array)) else None
        )
        objective_value = float(result.fun) if math.isfinite(float(result.fun)) else None
        production_starts.append(BetaBinomialProductionStartOutcome(
            start_index=index,
            initial_mean_logit=float(start[0]),
            initial_log_concentration=float(start[1]),
            success=bool(result.success), message=str(result.message),
            final_mean_logit=eta_i, final_log_concentration=xi_i,
            negative_log_likelihood=objective_value, gradient_norm=gradient_norm,
            lower_mean_bound_distance=(eta_i - bounds[0][0] if eta_i is not None else None),
            upper_mean_bound_distance=(bounds[0][1] - eta_i if eta_i is not None else None),
            lower_concentration_bound_distance=(xi_i - bounds[1][0] if xi_i is not None else None),
            upper_concentration_bound_distance=(bounds[1][1] - xi_i if xi_i is not None else None),
        ))
    admissible = [(index, result) for index, result in enumerate(fits)
                  if bool(result.success) and math.isfinite(float(result.fun))]
    if not admissible:
        messages = "; ".join(str(result.message) for result in fits)
        raise BetaBinomialFitError(f"MLE_NONCONVERGENCE: {messages}")
    best_index, best = min(admissible, key=lambda item: float(item[1].fun))

    logit_mean, log_concentration = (float(v) for v in best.x)
    mean = 1.0 / (1.0 + math.exp(-logit_mean))
    concentration = math.exp(log_concentration)
    alpha, beta = mean * concentration, (1.0 - mean) * concentration
    tolerance = 2e-4
    reasons: list[str] = []
    if abs(logit_mean - bounds[0][0]) < tolerance or abs(logit_mean - bounds[0][1]) < tolerance:
        reasons.append("MEAN_PARAMETER_AT_NUMERICAL_BOUND")
    if abs(log_concentration - bounds[1][0]) < tolerance:
        reasons.append("CONCENTRATION_AT_LOWER_BOUND")
    if abs(log_concentration - bounds[1][1]) < tolerance:
        reasons.append("CONCENTRATION_AT_UPPER_BOUND")
    return BetaBinomialFit(
        alpha=alpha, beta=beta, mean_probability=mean,
        concentration=concentration, log_likelihood=-float(best.fun),
        converged=True, boundary=bool(reasons),
        boundary_reasons=tuple(reasons), optimizer_message=str(best.message),
        selected_start_index=best_index,
        production_starts=tuple(production_starts),
    )


def build_production_analytic_reconciliation(
    fit: BetaBinomialFit | None,
    audit: BetaBinomialOptimizerAudit | None,
    *, audit_error: str | None = None,
) -> dict:
    """Retain direct P/A terminal comparisons without inventing a tolerance."""
    production = None
    analytic = None
    direct = None
    if fit is not None:
        production = {
            "optimizer": "L-BFGS-B_FINITE_DIFFERENCE",
            "selected_start_index": fit.selected_start_index,
            "selected_alpha": fit.alpha, "selected_beta": fit.beta,
            "selected_mean_probability": fit.mean_probability,
            "selected_concentration": fit.concentration,
            "selected_log_likelihood": fit.log_likelihood,
            "selected_mean_logit": math.log(fit.mean_probability / (1.0 - fit.mean_probability)),
            "selected_log_concentration": math.log(fit.concentration),
            "selected_termination_message": fit.optimizer_message,
            "selected_success": fit.converged,
            "boundary": fit.boundary,
            "boundary_reasons": list(fit.boundary_reasons),
            "starts": [asdict(item) for item in fit.production_starts],
        }
    if audit is not None:
        analytic = {
            "optimizer": "L-BFGS-B_ANALYTIC_GRADIENT",
            "status": audit.status,
            "selected_mean_logit": audit.selected_mean_logit,
            "selected_log_concentration": audit.selected_log_concentration,
            "selected_log_likelihood": audit.selected_log_likelihood,
            "selected_score_norm": audit.selected_score_norm,
            "profile_log_concentration_curvature": audit.profile_log_concentration_curvature,
            "starts": [asdict(item) for item in audit.starts],
            "independent_check": {
                "optimizer": "BFGS_LOG_ALPHA_LOG_BETA_INITIALIZED_FROM_ANALYTIC_FIT",
                "success": audit.independent_optimizer_success,
                "message": audit.independent_optimizer_message,
                "log_likelihood": audit.independent_log_likelihood,
                "terminal_log_alpha": audit.independent_terminal_log_alpha,
                "terminal_log_beta": audit.independent_terminal_log_beta,
                "score_norm": audit.independent_score_norm,
                "absolute_log_likelihood_difference_vs_analytic": audit.absolute_log_likelihood_difference,
                "log_shape_parameter_distance_vs_analytic": audit.log_shape_parameter_distance,
            },
        }
    if production is not None and audit is not None:
        eta_a, xi_a = audit.selected_mean_logit, audit.selected_log_concentration
        ll_a = audit.selected_log_likelihood
        mean_a = (1.0 / (1.0 + math.exp(-eta_a)) if eta_a >= 0
                  else math.exp(eta_a) / (1.0 + math.exp(eta_a))) if eta_a is not None else None
        concentration_a = math.exp(xi_a) if xi_a is not None else None
        direct = {
            "log_likelihood_difference_production_minus_analytic": fit.log_likelihood - ll_a if ll_a is not None else None,
            "absolute_log_likelihood_difference": abs(fit.log_likelihood - ll_a) if ll_a is not None else None,
            "mean_logit_difference_production_minus_analytic": production["selected_mean_logit"] - eta_a if eta_a is not None else None,
            "log_concentration_difference_production_minus_analytic": production["selected_log_concentration"] - xi_a if xi_a is not None else None,
            "alpha_difference_production_minus_analytic": fit.alpha - (math.exp(audit.independent_terminal_log_alpha) if audit.independent_terminal_log_alpha is not None else None) if audit.independent_terminal_log_alpha is not None else None,
            "beta_difference_production_minus_analytic": fit.beta - (math.exp(audit.independent_terminal_log_beta) if audit.independent_terminal_log_beta is not None else None) if audit.independent_terminal_log_beta is not None else None,
            "mean_probability_difference_production_minus_analytic": fit.mean_probability - mean_a if mean_a is not None else None,
            "concentration_difference_production_minus_analytic": fit.concentration - concentration_a if concentration_a is not None else None,
        }
    status = (
        "PRODUCTION_FIT_NOT_AVAILABLE" if fit is None else
        "ANALYTIC_AUDIT_UNAVAILABLE" if audit is None else
        "RAW_COMPARISON_RECORDED_NO_ADJUDICATION_THRESHOLD"
    )
    return {
        "schema": "C10S_F5_PRODUCTION_ANALYTIC_RECONCILIATION_1.0",
        "production_fit": production,
        "analytic_fit": analytic,
        "direct_comparison": direct,
        "status": status,
        "audit_error": audit_error,
        "adjudication": "NOT_THRESHOLDED; termination, numerical agreement and statistical identification remain separate",
        "independent_optimizer_scope": "LOCAL_BFGS_CHECK_INITIALIZED_FROM_ANALYTIC_FIT_NOT_GLOBAL_SEARCH",
    }


def fitted_beta_binomial_parametric_bootstrap(
    rows: Sequence[Sequence[float]], *,
    target_m: int, target_r: int, bootstrap_replicates: int,
    bootstrap_seed: int, confidence_level: float = 0.95,
    minimum_valid_mcse_rate: float = 0.90,
) -> FittedBetaBinomialBootstrapResult:
    """Fit F5, simulate beta-binomial worlds, and refit raw nested estimators.

    Each original row must contain Bernoulli 0/1 inner contributions. The
    parametric bootstrap resamples M independent world probabilities and R
    Bernoulli outcomes per world. Percentile intervals are exploratory
    candidates; no cutoff/coverage calibration is implied.
    """
    if type(bootstrap_replicates) is not int or bootstrap_replicates < 20:
        raise BetaBinomialFitError("bootstrap_replicates must be an integer >= 20")
    if type(bootstrap_seed) is not int or not 0 <= bootstrap_seed < 2**64:
        raise BetaBinomialFitError("bootstrap_seed must be an unsigned 64-bit integer")
    if not (0.0 < confidence_level < 1.0):
        raise BetaBinomialFitError("confidence_level must lie in (0,1)")
    if not (0.0 < minimum_valid_mcse_rate <= 1.0):
        raise BetaBinomialFitError("minimum_valid_mcse_rate must lie in (0,1]")

    observed = observed_nested_mr_result(rows, target_m=target_m, target_r=target_r)
    matrix = np.asarray(tuple(tuple(row) for row in rows), dtype=float)
    m, r = matrix.shape
    if not np.all(np.isin(matrix, (0.0, 1.0))):
        raise BetaBinomialFitError("F5_REQUIRES_BERNOULLI_0_1_INNER_CONTRIBUTIONS")
    counts = np.sum(matrix, axis=1).astype(int)

    # Diagnostic-only parallel audit. It does not select or replace the C5
    # fit below, and its failure never changes the candidate interval path.
    optimizer_audit = None
    optimizer_audit_error = None
    try:
        optimizer_audit = audit_beta_binomial_count_fit(counts, r)
    except (F5LikelihoodDiagnosticError, ArithmeticError, ValueError) as exc:
        optimizer_audit_error = f"{type(exc).__name__}:{exc}"

    try:
        fit = fit_beta_binomial_counts(counts, r)
    except BetaBinomialFitError as exc:
        return FittedBetaBinomialBootstrapResult(
            comparison=replace(
                observed, method_id="F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0",
                abstention_reason=str(exc),
                provenance=observed.provenance + (("fit_status", "ABSTAINED"),),
            ),
            fit=None, bootstrap_replicates=bootstrap_replicates,
            valid_mcse_replicates=0, valid_mcse_rate=0.0,
            confidence_level=confidence_level, bootstrap_seed=bootstrap_seed,
            failure_reason=str(exc),
            optimizer_audit=optimizer_audit,
            optimizer_audit_error=optimizer_audit_error,
            production_analytic_reconciliation=build_production_analytic_reconciliation(
                None, optimizer_audit, audit_error=optimizer_audit_error,
            ),
        )
    reconciliation = build_production_analytic_reconciliation(
        fit, optimizer_audit, audit_error=optimizer_audit_error,
    )
    if fit.boundary:
        reason = "BETA_BINOMIAL_MLE_BOUNDARY:" + ",".join(fit.boundary_reasons)
        return FittedBetaBinomialBootstrapResult(
            comparison=replace(
                observed, method_id="F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0",
                abstention_reason=reason,
                provenance=observed.provenance + (("fit_status", "BOUNDARY_ABSTENTION"),),
            ),
            fit=fit, bootstrap_replicates=bootstrap_replicates,
            valid_mcse_replicates=0, valid_mcse_rate=0.0,
            confidence_level=confidence_level, bootstrap_seed=bootstrap_seed,
            failure_reason=reason,
            optimizer_audit=optimizer_audit,
            optimizer_audit_error=optimizer_audit_error,
            production_analytic_reconciliation=reconciliation,
        )

    rng = np.random.Generator(np.random.PCG64(bootstrap_seed))
    p_world = rng.beta(fit.alpha, fit.beta, size=(bootstrap_replicates, m))
    counts_star = rng.binomial(r, p_world)
    within_star = np.empty(bootstrap_replicates, dtype=float)
    between_star = np.empty(bootstrap_replicates, dtype=float)
    mcse_star: list[float] = []
    for index in range(bootstrap_replicates):
        replicate_rows = np.zeros((m, r), dtype=float)
        for world_index, count in enumerate(counts_star[index]):
            replicate_rows[world_index, :int(count)] = 1.0
        result = observed_nested_mr_result(
            replicate_rows, target_m=target_m, target_r=target_r,
        )
        within_star[index] = result.within_estimate
        between_star[index] = result.between_estimate_raw
        if result.mcse_estimate is not None:
            mcse_star.append(result.mcse_estimate)

    alpha_tail = (1.0 - confidence_level) / 2.0
    within_interval = tuple(float(v) for v in np.quantile(
        within_star, [alpha_tail, 1.0 - alpha_tail],
    ))
    between_interval = tuple(float(v) for v in np.quantile(
        between_star, [alpha_tail, 1.0 - alpha_tail],
    ))
    valid_rate = len(mcse_star) / bootstrap_replicates

    # F5 MCSE is a constrained joint functional. The current candidate has no
    # boundary-aware confidence construction; quantiling only positive raw
    # projections would condition on a selected subset and violate protocol
    # v002's no-positive-only-conditioning rule. Keep the projectable-draw
    # count as a diagnostic, but fail closed for this target.
    mcse_interval = None
    abstention = "F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED"

    provenance = observed.provenance + (
        ("fit_model", "beta_binomial_world_probability"),
        ("fit_alpha", format(fit.alpha, ".17g")),
        ("fit_beta", format(fit.beta, ".17g")),
        ("fit_log_likelihood", format(fit.log_likelihood, ".17g")),
        ("optimizer_audit_status", (
            optimizer_audit.status if optimizer_audit is not None
            else "DIAGNOSTIC_UNAVAILABLE"
        )),
        ("optimizer_audit_error", optimizer_audit_error or "NONE"),
        ("optimizer_audit_ll_difference", (
            format(optimizer_audit.absolute_log_likelihood_difference, ".17g")
            if optimizer_audit is not None
            and optimizer_audit.absolute_log_likelihood_difference is not None
            else "UNAVAILABLE"
        )),
        ("bootstrap_rng", "PCG64"),
        ("bootstrap_seed", str(bootstrap_seed)),
        ("bootstrap_replicates", str(bootstrap_replicates)),
        ("mcse_valid_rate", format(valid_rate, ".17g")),
        ("interval_method", "parametric_percentile_exploratory"),
        ("mcse_interval_status", "NOT_IMPLEMENTED_BOUNDARY_AWARE_JOINT_INFERENCE"),
    )
    comparison = replace(
        observed,
        method_id="F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0",
        within_interval=within_interval,
        between_interval=between_interval,
        mcse_interval=mcse_interval,
        abstention_reason=abstention,
        provenance=provenance,
    )
    return FittedBetaBinomialBootstrapResult(
        comparison=comparison, fit=fit,
        bootstrap_replicates=bootstrap_replicates,
        valid_mcse_replicates=len(mcse_star), valid_mcse_rate=valid_rate,
        confidence_level=confidence_level, bootstrap_seed=bootstrap_seed,
        failure_reason=abstention,
        optimizer_audit=optimizer_audit,
        optimizer_audit_error=optimizer_audit_error,
        production_analytic_reconciliation=reconciliation,
    )
