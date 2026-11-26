"""M1-PCT: refitted beta-binomial parametric bootstrap of W and B.

Research-only candidate. The estimator is the deterministic best-successful
analytic-gradient L-BFGS-B fit from the existing three-start audit. It is an
algorithmic estimator, not a certified global MLE. The same fit procedure is
applied to the observed counts and every bootstrap replicate. Any unresolved
primary fit causes dataset-level abstention; no bootstrap replicate is dropped.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
from numbers import Integral
from typing import Sequence

import numpy as np

from c10s_f5_beta_binomial_likelihood_diagnostics import (
    BetaBinomialOptimizerAudit,
    F5LikelihoodDiagnosticError,
    audit_beta_binomial_count_fit,
)


METHOD_ID = "F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0"
FIT_CONTRACT_ID = "F5_M1_ANALYTIC_LBFGSB_BEST_SUCCESSFUL_START_1.0"
BOUND_TOLERANCE = 2e-4
BOUNDARY_LIKELIHOOD_ULPS = 64
MEAN_LOGIT_BOUNDS = (-18.0, 18.0)
LOG_CONCENTRATION_BOUNDS = (-12.0, 18.0)


class F5FunctionalBootstrapError(ValueError):
    """Invalid M1 input or bootstrap contract."""


@dataclass(frozen=True)
class F5FunctionalFitRecord:
    status: str
    mean_probability: float | None
    concentration: float | None
    within_functional: float | None
    between_functional: float | None
    log_likelihood: float | None
    score_norm: float | None
    hessian_eigenvalues: tuple[float, float] | None
    profile_log_concentration_curvature: float | None
    profile_minus_binomial_limit: float | None
    profile_minus_two_point_limit: float | None
    audit_status: str
    independent_optimizer_success: bool
    independent_optimizer_message: str
    independent_optimizer_role: str
    independent_log_likelihood: float | None
    independent_score_norm: float | None
    starts: tuple[dict, ...]
    failure_reason: str | None = None


@dataclass(frozen=True)
class F5FunctionalRefitBootstrapResult:
    method_id: str
    fit_contract_id: str
    status: str
    target_m: int
    target_r: int
    bootstrap_replicates: int
    bootstrap_seed: int
    confidence_level: float
    point_within: float | None
    point_between: float | None
    within_interval: tuple[float, float] | None
    between_interval: tuple[float, float] | None
    original_fit: F5FunctionalFitRecord
    replicate_records: tuple[dict, ...]
    valid_replicates: int
    failed_replicates: int
    failure_counts: tuple[tuple[str, int], ...]
    quantile_method: str = "NUMPY_LINEAR"
    global_mle_certificate_used: bool = False


def beta_binomial_functionals(
    mean_probability: float, concentration: float,
) -> tuple[float, float]:
    """Return W=E[p(1-p)] and B=Var(p) for a beta mixing distribution."""
    if (
        isinstance(mean_probability, bool)
        or not isinstance(mean_probability, (int, float))
        or not math.isfinite(mean_probability)
        or not 0.0 < mean_probability < 1.0
        or isinstance(concentration, bool)
        or not isinstance(concentration, (int, float))
        or not math.isfinite(concentration)
        or concentration <= 0.0
    ):
        raise F5FunctionalBootstrapError("FUNCTIONAL_PARAMETERS_OUTSIDE_OPEN_DOMAIN")
    q = float(mean_probability) * (1.0 - float(mean_probability))
    kappa = float(concentration)
    within = q * kappa / (kappa + 1.0)
    between = q / (kappa + 1.0)
    if not all(math.isfinite(value) for value in (within, between)):
        raise F5FunctionalBootstrapError("FUNCTIONAL_VALUE_NONFINITE")
    return within, between


def _strictly_exceeds_available_boundary(
    profile_minus_boundary: float | None, selected_log_likelihood: float,
) -> bool:
    if (
        profile_minus_boundary is None
        or not math.isfinite(float(profile_minus_boundary))
        or not math.isfinite(selected_log_likelihood)
    ):
        return False
    boundary_log_likelihood = selected_log_likelihood - float(profile_minus_boundary)
    scale = max(1.0, abs(selected_log_likelihood), abs(boundary_log_likelihood))
    tolerance = BOUNDARY_LIKELIHOOD_ULPS * np.finfo(float).eps * scale
    return float(profile_minus_boundary) > tolerance


def _fit_count_vector(
    counts: Sequence[int], r: int,
) -> F5FunctionalFitRecord:
    values = tuple(counts)
    try:
        audit: BetaBinomialOptimizerAudit = audit_beta_binomial_count_fit(values, r)
    except (F5LikelihoodDiagnosticError, ValueError, ArithmeticError, OverflowError) as exc:
        return F5FunctionalFitRecord(
            status="PRIMARY_FIT_UNRESOLVED",
            mean_probability=None, concentration=None,
            within_functional=None, between_functional=None,
            log_likelihood=None, score_norm=None, hessian_eigenvalues=None,
            profile_log_concentration_curvature=None,
            profile_minus_binomial_limit=None, profile_minus_two_point_limit=None,
            audit_status="AUDIT_EXCEPTION",
            independent_optimizer_success=False,
            independent_optimizer_message="NOT_AVAILABLE",
            independent_optimizer_role="SECONDARY_DIAGNOSTIC_ONLY",
            independent_log_likelihood=None, independent_score_norm=None,
            starts=(), failure_reason=f"{type(exc).__name__}:{exc}",
        )

    required = (
        audit.selected_mean_logit,
        audit.selected_log_concentration,
        audit.selected_log_likelihood,
        audit.selected_score_norm,
    )
    if audit.status == "NO_ADMISSIBLE_PRIMARY_FIT" or any(
        value is None or not math.isfinite(float(value)) for value in required
    ):
        return F5FunctionalFitRecord(
            status="NO_ADMISSIBLE_PRIMARY_FIT",
            mean_probability=None, concentration=None,
            within_functional=None, between_functional=None,
            log_likelihood=None, score_norm=None, hessian_eigenvalues=None,
            profile_log_concentration_curvature=audit.profile_log_concentration_curvature,
            profile_minus_binomial_limit=audit.profile_minus_binomial_limit,
            profile_minus_two_point_limit=audit.profile_minus_two_point_limit,
            audit_status=audit.status,
            independent_optimizer_success=audit.independent_optimizer_success,
            independent_optimizer_message=audit.independent_optimizer_message,
            independent_log_likelihood=audit.independent_log_likelihood,
            independent_score_norm=audit.independent_score_norm,
            starts=tuple(asdict(item) for item in audit.starts),
            failure_reason="NO_FINITE_SUCCESSFUL_ANALYTIC_GRADIENT_START",
        )

    eta = float(audit.selected_mean_logit)
    xi = float(audit.selected_log_concentration)
    mean = (
        1.0 / (1.0 + math.exp(-eta)) if eta >= 0.0
        else math.exp(eta) / (1.0 + math.exp(eta))
    )
    concentration = math.exp(xi)
    distances = (
        eta - MEAN_LOGIT_BOUNDS[0],
        MEAN_LOGIT_BOUNDS[1] - eta,
        xi - LOG_CONCENTRATION_BOUNDS[0],
        LOG_CONCENTRATION_BOUNDS[1] - xi,
    )
    if min(distances) <= BOUND_TOLERANCE:
        status = "FINITE_NUMERICAL_BOUND_HIT"
        reason = "SELECTED_ANALYTIC_FIT_WITHIN_BOUND_TOLERANCE"
    elif (
        audit.hessian_eigenvalues is None
        or len(audit.hessian_eigenvalues) != 2
        or any(not math.isfinite(float(value)) for value in audit.hessian_eigenvalues)
        or max(audit.hessian_eigenvalues) >= 0.0
    ):
        status = "PRIMARY_FIT_NOT_STRICT_LOCAL_MAXIMUM"
        reason = "OBSERVED_HESSIAN_NOT_FINITE_NEGATIVE_DEFINITE"
    elif (
        not _strictly_exceeds_available_boundary(
            audit.profile_minus_binomial_limit, float(audit.selected_log_likelihood),
        )
        or (
            audit.profile_minus_two_point_limit is not None
            and not _strictly_exceeds_available_boundary(
                audit.profile_minus_two_point_limit,
                float(audit.selected_log_likelihood),
            )
        )
    ):
        status = "BOUNDARY_LIMIT_NOT_EXCLUDED"
        reason = "SELECTED_INTERIOR_FIT_DOES_NOT_EXCEED_ALL_AVAILABLE_ONE_EDGE_LIMITS"
    else:
        status = "PRIMARY_ANALYTIC_INTERIOR_FIT"
        reason = None

    within, between = beta_binomial_functionals(mean, concentration)
    return F5FunctionalFitRecord(
        status=status,
        mean_probability=mean,
        concentration=concentration,
        within_functional=within,
        between_functional=between,
        log_likelihood=float(audit.selected_log_likelihood),
        score_norm=float(audit.selected_score_norm),
        hessian_eigenvalues=(
            tuple(float(value) for value in audit.hessian_eigenvalues)
            if audit.hessian_eigenvalues is not None else None
        ),
        profile_log_concentration_curvature=audit.profile_log_concentration_curvature,
        profile_minus_binomial_limit=audit.profile_minus_binomial_limit,
        profile_minus_two_point_limit=audit.profile_minus_two_point_limit,
        audit_status=audit.status,
        independent_optimizer_success=audit.independent_optimizer_success,
        independent_optimizer_message=audit.independent_optimizer_message,
        independent_optimizer_role="SECONDARY_DIAGNOSTIC_ONLY",
        independent_log_likelihood=audit.independent_log_likelihood,
        independent_score_norm=audit.independent_score_norm,
        starts=tuple(asdict(item) for item in audit.starts),
        failure_reason=reason,
    )


def _replicate_seed(bootstrap_seed: int, replicate_index: int) -> int:
    payload = f"{FIT_CONTRACT_ID}|{bootstrap_seed}|{replicate_index}".encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def _counts_digest(counts: Sequence[int]) -> str:
    payload = json.dumps([int(value) for value in counts], separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def fitted_functional_refit_percentile_bootstrap(
    counts: Sequence[int], *,
    r: int, bootstrap_replicates: int, bootstrap_seed: int,
    confidence_level: float = 0.95,
) -> F5FunctionalRefitBootstrapResult:
    """Refit the analytic-gradient beta-binomial estimator in every replicate.

    Any failed/boundary/unresolved replicate makes the complete dataset abstain.
    All replicate states are retained; no complete-case bootstrap distribution
    is formed. The exact global-MLE certificate is not invoked.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2:
        raise F5FunctionalBootstrapError("R_MUST_BE_INTEGER_GE_2")
    if len(values) < 2:
        raise F5FunctionalBootstrapError("AT_LEAST_TWO_WORLDS_REQUIRED")
    if any(
        isinstance(value, bool) or not isinstance(value, Integral)
        or not 0 <= int(value) <= r for value in values
    ):
        raise F5FunctionalBootstrapError("COUNTS_MUST_BE_INTEGERS_IN_[0,R]")
    values = tuple(int(value) for value in values)
    if type(bootstrap_replicates) is not int or bootstrap_replicates < 20:
        raise F5FunctionalBootstrapError("BOOTSTRAP_REPLICATES_MUST_BE_INTEGER_GE_20")
    if type(bootstrap_seed) is not int or not 0 <= bootstrap_seed < 2**64:
        raise F5FunctionalBootstrapError("BOOTSTRAP_SEED_MUST_BE_UNSIGNED_64_BIT")
    if (
        isinstance(confidence_level, bool)
        or not isinstance(confidence_level, (int, float))
        or not math.isfinite(confidence_level)
        or not 0.0 < confidence_level < 1.0
    ):
        raise F5FunctionalBootstrapError("CONFIDENCE_LEVEL_MUST_LIE_IN_OPEN_UNIT_INTERVAL")

    original = _fit_count_vector(values, r)
    m = len(values)
    if original.status != "PRIMARY_ANALYTIC_INTERIOR_FIT":
        return F5FunctionalRefitBootstrapResult(
            method_id=METHOD_ID, fit_contract_id=FIT_CONTRACT_ID,
            status="ABSTAINED_ORIGINAL_FIT",
            target_m=m, target_r=r, bootstrap_replicates=bootstrap_replicates,
            bootstrap_seed=bootstrap_seed, confidence_level=float(confidence_level),
            point_within=original.within_functional,
            point_between=original.between_functional,
            within_interval=None, between_interval=None,
            original_fit=original, replicate_records=(),
            valid_replicates=0, failed_replicates=0,
            failure_counts=((original.status, 1),),
        )

    within_values: list[float] = []
    between_values: list[float] = []
    records: list[dict] = []
    failures: dict[str, int] = {}
    alpha = float(original.mean_probability) * float(original.concentration)
    beta = (1.0 - float(original.mean_probability)) * float(original.concentration)

    for index in range(bootstrap_replicates):
        seed = _replicate_seed(bootstrap_seed, index)
        rng = np.random.Generator(np.random.PCG64(seed))
        probabilities = rng.beta(alpha, beta, size=m)
        simulated_counts = rng.binomial(r, probabilities).astype(int).tolist()
        fit = _fit_count_vector(simulated_counts, r)
        record = {
            "replicate_index": index,
            "replicate_seed": seed,
            "counts_sha256": _counts_digest(simulated_counts),
            "fit": asdict(fit),
        }
        records.append(record)
        if fit.status != "PRIMARY_ANALYTIC_INTERIOR_FIT":
            failures[fit.status] = failures.get(fit.status, 0) + 1
        else:
            within_values.append(float(fit.within_functional))
            between_values.append(float(fit.between_functional))

    failed = sum(failures.values())
    if failed:
        status = "ABSTAINED_BOOTSTRAP_FIT_FAILURE"
        within_interval = None
        between_interval = None
    else:
        tail = (1.0 - float(confidence_level)) / 2.0
        within_interval = tuple(float(value) for value in np.quantile(
            within_values, [tail, 1.0 - tail], method="linear",
        ))
        between_interval = tuple(float(value) for value in np.quantile(
            between_values, [tail, 1.0 - tail], method="linear",
        ))
        status = "EMITTED"

    return F5FunctionalRefitBootstrapResult(
        method_id=METHOD_ID, fit_contract_id=FIT_CONTRACT_ID,
        status=status, target_m=m, target_r=r,
        bootstrap_replicates=bootstrap_replicates,
        bootstrap_seed=bootstrap_seed, confidence_level=float(confidence_level),
        point_within=original.within_functional,
        point_between=original.between_functional,
        within_interval=within_interval,
        between_interval=between_interval,
        original_fit=original,
        replicate_records=tuple(records),
        valid_replicates=len(within_values),
        failed_replicates=failed,
        failure_counts=tuple(sorted(failures.items())),
    )
