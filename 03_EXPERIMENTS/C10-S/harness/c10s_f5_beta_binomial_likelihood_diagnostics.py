"""Deterministic F5 beta-binomial likelihood diagnostics.

Research-only numerical controls for C10-S post-holdout development.
No simulation, bootstrap, calibration, or scientific execution occurs here.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Integral
from typing import Sequence

from scipy.optimize import minimize, minimize_scalar
from scipy.special import betaln, digamma, gammaln, polygamma
import numpy as np


class F5LikelihoodDiagnosticError(ValueError):
    """Invalid input to the deterministic F5 likelihood diagnostics."""


@dataclass(frozen=True)
class BetaBinomialLikelihoodDerivatives:
    log_likelihood: float
    score_mean_logit: float
    score_log_concentration: float
    hessian_mean_logit: float
    hessian_cross: float
    hessian_log_concentration: float


@dataclass(frozen=True)
class BetaBinomialBoundaryLikelihoods:
    finite_log_likelihood: float
    binomial_limit_log_likelihood: float
    two_point_mixing_limit_log_likelihood: float
    concentration: float


def beta_binomial_loglik_score_hessian(
    counts: Sequence[int], r: int, *, mean_logit: float,
    log_concentration: float,
) -> BetaBinomialLikelihoodDerivatives:
    """Analytic log-likelihood, score and Hessian in (logit(mu), log(kappa)).

    The likelihood is the independent beta-binomial count likelihood for
    X_m ~ BetaBinomial(r, alpha=mu*kappa, beta=(1-mu)*kappa).
    Derivatives are analytic and use digamma/trigamma functions.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2:
        raise F5LikelihoodDiagnosticError("R_MUST_BE_INTEGER_GE_2")
    if len(values) < 2:
        raise F5LikelihoodDiagnosticError("AT_LEAST_TWO_WORLD_COUNTS_REQUIRED")
    if any(isinstance(x, bool) or not isinstance(x, Integral) or x < 0 or x > r for x in values):
        raise F5LikelihoodDiagnosticError("COUNTS_MUST_BE_INTEGER_IN_[0,R]")
    if (not math.isfinite(mean_logit) or not math.isfinite(log_concentration)
            or abs(mean_logit) > 700 or log_concentration > 700
            or log_concentration < -700):
        raise F5LikelihoodDiagnosticError("PARAMETERS_NONFINITE_OR_UNREPRESENTABLE")

    # Stable logistic transform.
    if mean_logit >= 0:
        e = math.exp(-mean_logit)
        mu = 1.0 / (1.0 + e)
    else:
        e = math.exp(mean_logit)
        mu = e / (1.0 + e)
    kappa = math.exp(log_concentration)
    alpha, beta = mu * kappa, (1.0 - mu) * kappa
    if min(alpha, beta, kappa) <= 0 or not all(
        math.isfinite(v) for v in (mu, kappa, alpha, beta)
    ):
        raise F5LikelihoodDiagnosticError("SHAPE_PARAMETERS_UNREPRESENTABLE")

    ll = 0.0
    ga = 0.0
    gb = 0.0
    haa = 0.0
    hab = 0.0
    hbb = 0.0
    psi_k = float(digamma(kappa))
    tri_k = float(polygamma(1, kappa))
    psi_rk = float(digamma(r + kappa))
    tri_rk = float(polygamma(1, r + kappa))
    for x in values:
        ll += (
            float(gammaln(r + 1) - gammaln(x + 1) - gammaln(r - x + 1))
            + float(betaln(x + alpha, r - x + beta))
            - float(betaln(alpha, beta))
        )
        ga += float(digamma(x + alpha) - psi_rk - digamma(alpha) + psi_k)
        gb += float(digamma(r - x + beta) - psi_rk - digamma(beta) + psi_k)
        haa += float(polygamma(1, x + alpha) - tri_rk
                     - polygamma(1, alpha) + tri_k)
        hbb += float(polygamma(1, r - x + beta) - tri_rk
                     - polygamma(1, beta) + tri_k)
        hab += -tri_rk + tri_k

    mu1 = mu * (1.0 - mu)
    mu2 = mu1 * (1.0 - 2.0 * mu)
    a_eta, b_eta = kappa * mu1, -kappa * mu1
    a_xi, b_xi = alpha, beta

    score_eta = ga * a_eta + gb * b_eta
    score_xi = ga * a_xi + gb * b_xi

    h_etaeta = (
        haa * a_eta * a_eta + 2.0 * hab * a_eta * b_eta
        + hbb * b_eta * b_eta + ga * kappa * mu2 - gb * kappa * mu2
    )
    h_etaxi = (
        haa * a_eta * a_xi + hab * (a_eta * b_xi + b_eta * a_xi)
        + hbb * b_eta * b_xi + ga * a_eta + gb * b_eta
    )
    h_xixi = (
        haa * a_xi * a_xi + 2.0 * hab * a_xi * b_xi
        + hbb * b_xi * b_xi + ga * alpha + gb * beta
    )
    result = (ll, score_eta, score_xi, h_etaeta, h_etaxi, h_xixi)
    if not all(math.isfinite(value) for value in result):
        raise F5LikelihoodDiagnosticError("LIKELIHOOD_DERIVATIVES_NONFINITE")
    return BetaBinomialLikelihoodDerivatives(*result)


def beta_binomial_extended_boundary_likelihoods(
    counts: Sequence[int], r: int, *, mean_probability: float,
    concentration: float,
) -> BetaBinomialBoundaryLikelihoods:
    """Compare finite-kappa likelihood with kappa→∞ and kappa→0 limits.

    The kappa→∞ limit is Binomial(r, mu). The kappa→0 limit is a two-point
    mixing law: P(X=0)=1-mu, P(X=r)=mu, with interior counts having zero
    limiting probability. These are likelihood limits, not optimizer bounds.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2 or len(values) < 2:
        raise F5LikelihoodDiagnosticError("INVALID_R_OR_SAMPLE_SIZE")
    if any(type(x) is not int or x < 0 or x > r for x in values):
        raise F5LikelihoodDiagnosticError("COUNTS_MUST_BE_INTEGER_IN_[0,R]")
    if (not math.isfinite(mean_probability) or not 0 < mean_probability < 1
            or not math.isfinite(concentration) or concentration <= 0):
        raise F5LikelihoodDiagnosticError("INVALID_MEAN_OR_CONCENTRATION")

    mu = float(mean_probability)
    alpha, beta = mu * concentration, (1.0 - mu) * concentration
    finite = 0.0
    binomial = 0.0
    two_point = 0.0
    for x in values:
        log_choose = float(
            gammaln(r + 1) - gammaln(x + 1) - gammaln(r - x + 1)
        )
        finite += log_choose + float(
            betaln(x + alpha, r - x + beta) - betaln(alpha, beta)
        )
        binomial += log_choose + x * math.log(mu) + (r - x) * math.log1p(-mu)
        if x == 0:
            two_point += math.log1p(-mu)
        elif x == r:
            two_point += math.log(mu)
        else:
            two_point = -math.inf
    return BetaBinomialBoundaryLikelihoods(
        finite_log_likelihood=finite,
        binomial_limit_log_likelihood=binomial,
        two_point_mixing_limit_log_likelihood=two_point,
        concentration=float(concentration),
    )


@dataclass(frozen=True)
class BetaBinomialStartOutcome:
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
class BetaBinomialOptimizerAudit:
    status: str
    selected_mean_logit: float | None
    selected_log_concentration: float | None
    selected_log_likelihood: float | None
    selected_score_norm: float | None
    hessian_eigenvalues: tuple[float, float] | None
    profile_log_concentration_curvature: float | None
    independent_optimizer_success: bool
    independent_optimizer_message: str
    independent_log_likelihood: float | None
    absolute_log_likelihood_difference: float | None
    log_shape_parameter_distance: float | None
    binomial_limit_log_likelihood: float | None
    two_point_limit_log_likelihood: float | None
    starts: tuple[BetaBinomialStartOutcome, ...]
    selected_score_components: tuple[float, float] | None = None
    observed_hessian: tuple[tuple[float, float], tuple[float, float]] | None = None
    hessian_eigenvectors: tuple[tuple[float, float], tuple[float, float]] | None = None
    profile_minus_binomial_limit: float | None = None
    profile_minus_two_point_limit: float | None = None


def audit_beta_binomial_count_fit(
    counts: Sequence[int], r: int, *,
    concentration_starts: Sequence[float] = (2.0, 0.5, 20.0),
    mean_logit_bounds: tuple[float, float] = (-18.0, 18.0),
    log_concentration_bounds: tuple[float, float] = (-12.0, 18.0),
) -> BetaBinomialOptimizerAudit:
    """Audit all bounded L-BFGS-B starts against log(alpha)/log(beta) BFGS.

    This deterministic routine is a diagnostic only. It does not change the
    existing C5 fit selection, emit intervals, or run any simulation.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2 or len(values) < 2:
        raise F5LikelihoodDiagnosticError("INVALID_R_OR_SAMPLE_SIZE")
    if any(isinstance(x, bool) or not isinstance(x, Integral) or x < 0 or x > r
           for x in values):
        raise F5LikelihoodDiagnosticError("COUNTS_MUST_BE_INTEGER_IN_[0,R]")
    # Normalize NumPy integer scalars to built-in ints for the shared
    # extended-boundary likelihood evaluator's strict input contract.
    values = tuple(int(value) for value in values)
    starts_k = tuple(float(value) for value in concentration_starts)
    if (not starts_k or any(not math.isfinite(v) or v <= 0 for v in starts_k)
            or len(mean_logit_bounds) != 2 or len(log_concentration_bounds) != 2
            or not mean_logit_bounds[0] < mean_logit_bounds[1]
            or not log_concentration_bounds[0] < log_concentration_bounds[1]):
        raise F5LikelihoodDiagnosticError("INVALID_STARTS_OR_PARAMETER_BOUNDS")

    empirical_mean = min(
        1.0 - 1e-6, max(1e-6, sum(values) / (len(values) * r)),
    )
    eta0 = math.log(empirical_mean / (1.0 - empirical_mean))
    bounds = (mean_logit_bounds, log_concentration_bounds)

    def objective(parameters):
        eta, xi = (float(value) for value in parameters)
        try:
            return -beta_binomial_loglik_score_hessian(
                values, r, mean_logit=eta, log_concentration=xi,
            ).log_likelihood
        except (OverflowError, ValueError, F5LikelihoodDiagnosticError):
            return 1e300

    def gradient(parameters):
        eta, xi = (float(value) for value in parameters)
        result = beta_binomial_loglik_score_hessian(
            values, r, mean_logit=eta, log_concentration=xi,
        )
        return np.asarray(
            [-result.score_mean_logit, -result.score_log_concentration],
            dtype=float,
        )

    results = []
    start_records = []
    for concentration in starts_k:
        start = np.asarray([eta0, math.log(concentration)], dtype=float)
        result = minimize(
            objective, start, jac=gradient, method="L-BFGS-B", bounds=bounds,
            options={"maxiter": 4000, "ftol": 1e-12, "gtol": 1e-8},
        )
        results.append(result)
        eta = float(result.x[0]) if np.all(np.isfinite(result.x)) else None
        xi = float(result.x[1]) if np.all(np.isfinite(result.x)) else None
        grad_norm = (
            float(np.linalg.norm(gradient(result.x)))
            if eta is not None and xi is not None else None
        )
        start_records.append(BetaBinomialStartOutcome(
            initial_mean_logit=float(start[0]),
            initial_log_concentration=float(start[1]),
            success=bool(result.success),
            message=str(result.message),
            final_mean_logit=eta,
            final_log_concentration=xi,
            negative_log_likelihood=(
                float(result.fun) if math.isfinite(float(result.fun)) else None
            ),
            gradient_norm=grad_norm,
            lower_mean_bound_distance=(
                eta - mean_logit_bounds[0] if eta is not None else None
            ),
            upper_mean_bound_distance=(
                mean_logit_bounds[1] - eta if eta is not None else None
            ),
            lower_concentration_bound_distance=(
                xi - log_concentration_bounds[0] if xi is not None else None
            ),
            upper_concentration_bound_distance=(
                log_concentration_bounds[1] - xi if xi is not None else None
            ),
        ))

    admissible = [
        result for result in results
        if bool(result.success) and math.isfinite(float(result.fun))
    ]
    if not admissible:
        return BetaBinomialOptimizerAudit(
            status="NO_ADMISSIBLE_PRIMARY_FIT",
            selected_mean_logit=None, selected_log_concentration=None,
            selected_log_likelihood=None, selected_score_norm=None,
            hessian_eigenvalues=None, profile_log_concentration_curvature=None,
            independent_optimizer_success=False,
            independent_optimizer_message="NOT_RUN_NO_ADMISSIBLE_PRIMARY_FIT",
            independent_log_likelihood=None,
            absolute_log_likelihood_difference=None,
            log_shape_parameter_distance=None,
            binomial_limit_log_likelihood=None,
            two_point_limit_log_likelihood=None,
            starts=tuple(start_records),
        )

    best = min(admissible, key=lambda item: float(item.fun))
    eta, xi = float(best.x[0]), float(best.x[1])
    selected = beta_binomial_loglik_score_hessian(
        values, r, mean_logit=eta, log_concentration=xi,
    )
    mu = 1.0 / (1.0 + math.exp(-eta)) if eta >= 0 else (
        math.exp(eta) / (1.0 + math.exp(eta))
    )
    kappa = math.exp(xi)
    alpha, beta = mu * kappa, (1.0 - mu) * kappa

    def independent_objective(log_shapes):
        la, lb = (float(value) for value in log_shapes)
        if not all(math.isfinite(value) and abs(value) <= 700 for value in (la, lb)):
            return 1e300
        a, b = math.exp(la), math.exp(lb)
        total = 0.0
        for x in values:
            total += float(
                gammaln(r + 1) - gammaln(x + 1) - gammaln(r - x + 1)
                + betaln(x + a, r - x + b) - betaln(a, b)
            )
        return -total if math.isfinite(total) else 1e300

    def independent_gradient(log_shapes):
        la, lb = (float(value) for value in log_shapes)
        # Match the independent objective's explicit representability guard.
        # Outside it the objective is a flat finite penalty, so its declared
        # diagnostic gradient is zero rather than allowing exp() to overflow.
        if not all(math.isfinite(value) and abs(value) <= 700 for value in (la, lb)):
            return np.zeros(2, dtype=float)
        a, b = math.exp(la), math.exp(lb)
        ga = gb = 0.0
        total = a + b
        for x in values:
            ga += float(
                digamma(x + a) - digamma(r + total)
                - digamma(a) + digamma(total)
            )
            gb += float(
                digamma(r - x + b) - digamma(r + total)
                - digamma(b) + digamma(total)
            )
        return np.asarray([-a * ga, -b * gb], dtype=float)

    independent = minimize(
        independent_objective, np.asarray([math.log(alpha), math.log(beta)]),
        jac=independent_gradient, method="BFGS",
        options={"gtol": 1e-8, "maxiter": 4000},
    )
    independent_success = bool(independent.success) and math.isfinite(float(independent.fun))
    independent_ll = -float(independent.fun) if math.isfinite(float(independent.fun)) else None
    difference = (
        abs(selected.log_likelihood - independent_ll)
        if independent_ll is not None else None
    )
    shape_distance = None
    if independent_ll is not None:
        shape_distance = float(np.linalg.norm(
            np.asarray([math.log(alpha), math.log(beta)])
            - np.asarray(independent.x, dtype=float)
        ))

    hessian = np.asarray([
        [selected.hessian_mean_logit, selected.hessian_cross],
        [selected.hessian_cross, selected.hessian_log_concentration],
    ], dtype=float)
    eigenvalues = tuple(float(value) for value in np.linalg.eigvalsh(hessian))
    # Local observed curvature of the profile log-likelihood in log(kappa),
    # eliminating mean_logit as a nuisance coordinate via the Hessian Schur
    # complement. This is a raw, parameterization-specific diagnostic; it is
    # not a weak-identification threshold or a C5 selection rule.
    profile_curvature = None
    if (
        mean_logit_bounds[0] < eta < mean_logit_bounds[1]
        and math.isfinite(selected.hessian_mean_logit)
        and selected.hessian_mean_logit != 0.0
    ):
        candidate_curvature = (
            selected.hessian_log_concentration
            - selected.hessian_cross * selected.hessian_cross
            / selected.hessian_mean_logit
        )
        if math.isfinite(candidate_curvature):
            profile_curvature = float(candidate_curvature)
    boundary = beta_binomial_extended_boundary_likelihoods(
        values, r, mean_probability=mu, concentration=kappa,
    )
    if not independent_success:
        status = "INDEPENDENT_OPTIMIZER_UNRESOLVED"
    elif difference is None or difference > 1e-6:
        status = "OPTIMIZER_DISCORDANT"
    elif shape_distance is not None and shape_distance > 1e-3:
        status = "LIKELIHOOD_CONCORDANT_PARAMETER_DISAGREEMENT"
    else:
        status = "OPTIMIZER_CONCORDANT"

    return BetaBinomialOptimizerAudit(
        status=status,
        selected_mean_logit=eta,
        selected_log_concentration=xi,
        selected_log_likelihood=selected.log_likelihood,
        selected_score_norm=float(np.linalg.norm(gradient(best.x))),
        hessian_eigenvalues=eigenvalues,
        profile_log_concentration_curvature=profile_curvature,
        independent_optimizer_success=independent_success,
        independent_optimizer_message=str(independent.message),
        independent_log_likelihood=independent_ll,
        absolute_log_likelihood_difference=difference,
        log_shape_parameter_distance=shape_distance,
        binomial_limit_log_likelihood=boundary.binomial_limit_log_likelihood,
        two_point_limit_log_likelihood=boundary.two_point_mixing_limit_log_likelihood,
        starts=tuple(start_records),
        selected_score_components=(
            float(selected.score_mean_logit),
            float(selected.score_log_concentration),
        ),
        observed_hessian=(
            (float(selected.hessian_mean_logit), float(selected.hessian_cross)),
            (float(selected.hessian_cross), float(selected.hessian_log_concentration)),
        ),
        hessian_eigenvectors=tuple(
            tuple(float(value) for value in row)
            for row in np.linalg.eigh(hessian)[1].T
        ),
        profile_minus_binomial_limit=(
            float(selected.log_likelihood - boundary.binomial_limit_log_likelihood)
            if math.isfinite(boundary.binomial_limit_log_likelihood) else None
        ),
        profile_minus_two_point_limit=(
            float(selected.log_likelihood - boundary.two_point_mixing_limit_log_likelihood)
            if math.isfinite(boundary.two_point_mixing_limit_log_likelihood) else None
        ),
    )


@dataclass(frozen=True)
class BetaBinomialProfilePoint:
    """Numerical nuisance-profile point; deliberately not a global certificate."""
    log_concentration: float
    profiled_mean_logit: float
    profiled_log_likelihood: float
    nuisance_score: float
    concentration_score: float
    profile_log_concentration_curvature: float | None
    mean_profile_at_bound: bool
    nuisance_refinement_succeeded: bool
    status: str


@dataclass(frozen=True)
class BetaBinomialProfileBoundaryLikelihoods:
    """Boundary models with their own nuisance mean maximized."""
    binomial_profile_log_likelihood: float
    binomial_profile_mean: float
    two_point_profile_log_likelihood: float | None
    two_point_profile_mean: float | None
    two_point_boundary_status: str
    interior_count_observations: int


def beta_binomial_profile_log_concentration(
    counts: Sequence[int],
    r: int,
    log_concentrations: Sequence[float],
    *,
    mean_logit_bounds: tuple[float, float] = (-18.0, 18.0),
    mean_grid_size: int = 257,
) -> tuple[BetaBinomialProfilePoint, ...]:
    """Trace the numerical profile over supplied log(kappa) values.

    For each fixed log(kappa), a deterministic eta grid locates a candidate
    bracket and bounded scalar optimization refines it. The output is explicitly
    NUMERICAL_PROFILE_UNCERTIFIED: it is a diagnostic trace, not proof of a
    global nuisance maximum and not an identification classification.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2 or len(values) < 2:
        raise F5LikelihoodDiagnosticError("INVALID_R_OR_SAMPLE_SIZE")
    if any(isinstance(x, bool) or not isinstance(x, Integral) or x < 0 or x > r
           for x in values):
        raise F5LikelihoodDiagnosticError("COUNTS_MUST_BE_INTEGER_IN_[0,R]")
    if (len(mean_logit_bounds) != 2
            or not all(math.isfinite(float(v)) for v in mean_logit_bounds)
            or not mean_logit_bounds[0] < mean_logit_bounds[1]
            or type(mean_grid_size) is not int or mean_grid_size < 17):
        raise F5LikelihoodDiagnosticError("INVALID_PROFILE_SEARCH_CONTROLS")
    xis = tuple(float(value) for value in log_concentrations)
    if (len(xis) < 3 or any(not math.isfinite(value) for value in xis)
            or any(right <= left for left, right in zip(xis, xis[1:]))):
        raise F5LikelihoodDiagnosticError("LOG_CONCENTRATIONS_MUST_BE_FINITE_STRICTLY_INCREASING")

    eta_lo, eta_hi = (float(v) for v in mean_logit_bounds)
    eta_grid = np.linspace(eta_lo, eta_hi, mean_grid_size)
    output = []
    for xi in xis:
        grid_ll = []
        for eta in eta_grid:
            grid_ll.append(beta_binomial_loglik_score_hessian(
                values, r, mean_logit=float(eta), log_concentration=xi,
            ).log_likelihood)
        best_index = int(np.argmax(np.asarray(grid_ll)))
        best_eta = float(eta_grid[best_index])
        best_ll = float(grid_ll[best_index])
        at_bound = best_index in (0, mean_grid_size - 1)
        refinement_succeeded = at_bound
        if not at_bound:
            result = minimize_scalar(
                lambda eta: -beta_binomial_loglik_score_hessian(
                    values, r, mean_logit=float(eta), log_concentration=xi,
                ).log_likelihood,
                bounds=(float(eta_grid[best_index - 1]),
                        float(eta_grid[best_index + 1])),
                method="bounded",
                options={"xatol": 1e-12, "maxiter": 2000},
            )
            if bool(result.success) and math.isfinite(float(result.fun)):
                refinement_succeeded = True
                refined_eta = float(result.x)
                refined_ll = -float(result.fun)
                if refined_ll >= best_ll:
                    best_eta, best_ll = refined_eta, refined_ll
            else:
                refinement_succeeded = False
        derivatives = beta_binomial_loglik_score_hessian(
            values, r, mean_logit=best_eta, log_concentration=xi,
        )
        curvature = None
        if (not at_bound and refinement_succeeded and math.isfinite(derivatives.hessian_mean_logit)
                and derivatives.hessian_mean_logit != 0.0):
            candidate = (
                derivatives.hessian_log_concentration
                - derivatives.hessian_cross ** 2
                / derivatives.hessian_mean_logit
            )
            if math.isfinite(candidate):
                curvature = float(candidate)
        output.append(BetaBinomialProfilePoint(
            log_concentration=xi,
            profiled_mean_logit=best_eta,
            profiled_log_likelihood=best_ll,
            nuisance_score=derivatives.score_mean_logit,
            concentration_score=derivatives.score_log_concentration,
            profile_log_concentration_curvature=curvature,
            mean_profile_at_bound=at_bound,
            nuisance_refinement_succeeded=refinement_succeeded,
            status=("MEAN_PROFILE_BOUNDARY" if at_bound else
                    "NUISANCE_PROFILE_OPTIMIZER_UNRESOLVED" if not refinement_succeeded
                    else "NUMERICAL_PROFILE_UNCERTIFIED"),
        ))
    return tuple(output)


def beta_binomial_profiled_boundary_likelihoods(
    counts: Sequence[int], r: int,
) -> BetaBinomialProfileBoundaryLikelihoods:
    """Profile each extended concentration boundary over its own mean.

    The binomial limit uses its pooled Bernoulli MLE. The two-point limit is
    finite only when every world count is 0 or R; its endpoint-mixture MLE is
    then the observed fraction of R-valued counts. These are separate nuisance
    optimizations, unlike fixed-mean boundary comparisons.
    """
    values = tuple(counts)
    if type(r) is not int or r < 2 or len(values) < 2:
        raise F5LikelihoodDiagnosticError("INVALID_R_OR_SAMPLE_SIZE")
    if any(isinstance(x, bool) or not isinstance(x, Integral) or x < 0 or x > r
           for x in values):
        raise F5LikelihoodDiagnosticError("COUNTS_MUST_BE_INTEGER_IN_[0,R]")
    values = tuple(int(x) for x in values)
    n = len(values)
    total = sum(values)
    total_trials = n * r
    binomial_mean = total / total_trials
    binomial_ll = 0.0
    for x in values:
        binomial_ll += float(
            gammaln(r + 1) - gammaln(x + 1) - gammaln(r - x + 1)
        )
    if total == 0 or total == total_trials:
        binomial_ll = float(binomial_ll)
    else:
        binomial_ll += (
            total * math.log(binomial_mean)
            + (total_trials - total) * math.log1p(-binomial_mean)
        )

    interior = sum(1 for x in values if 0 < x < r)
    if interior:
        two_point_ll = None
        two_point_mean = None
        two_point_status = "ZERO_PROBABILITY_INTERIOR_COUNTS"
    else:
        n_zero = sum(1 for x in values if x == 0)
        n_full = sum(1 for x in values if x == r)
        two_point_mean = n_full / n
        two_point_status = "FINITE_ENDPOINT_MIXTURE_PROFILE"
        if n_full == 0 or n_zero == 0:
            two_point_ll = 0.0
        else:
            two_point_ll = (
                n_full * math.log(two_point_mean)
                + n_zero * math.log1p(-two_point_mean)
            )
    return BetaBinomialProfileBoundaryLikelihoods(
        binomial_profile_log_likelihood=float(binomial_ll),
        binomial_profile_mean=float(binomial_mean),
        two_point_profile_log_likelihood=(
            float(two_point_ll) if two_point_ll is not None else None
        ),
        two_point_profile_mean=(
            float(two_point_mean) if two_point_mean is not None else None
        ),
        two_point_boundary_status=two_point_status,
        interior_count_observations=interior,
    )


@dataclass(frozen=True)
class BetaBinomialProfileAuditRecord:
    """Separated optimizer, boundary-comparison and profile-shape diagnostics."""
    optimizer_convergence_status: str
    identification_status: str
    profile_status: str
    profile_point_count: int
    profile_max_log_likelihood: float | None
    binomial_boundary_profile_log_likelihood: float
    two_point_boundary_profile_log_likelihood: float | None
    two_point_boundary_status: str
    profile_minus_binomial_boundary: float | None
    profile_minus_two_point_boundary: float | None
    profile_curvature_values: tuple[float | None, ...]
    profile_curvature_min: float | None
    profile_curvature_max: float | None


def build_beta_binomial_profile_audit_record(
    optimizer_audit: BetaBinomialOptimizerAudit,
    profile_points: Sequence[BetaBinomialProfilePoint],
    boundary: BetaBinomialProfileBoundaryLikelihoods,
) -> BetaBinomialProfileAuditRecord:
    """Combine raw diagnostics without adjudicating statistical identification.

    Profile-vs-boundary differences are descriptive only: the numerical profile
    is not globally certified, and no scale-aware identification criterion has
    been adopted. Consequently identification_status is always INDETERMINATE.
    """
    points = tuple(profile_points)
    if not points:
        raise F5LikelihoodDiagnosticError("PROFILE_AUDIT_REQUIRES_POINTS")
    if any(not math.isfinite(point.profiled_log_likelihood) for point in points):
        raise F5LikelihoodDiagnosticError("PROFILE_AUDIT_REQUIRES_FINITE_PROFILE_VALUES")
    if any(
        right.log_concentration <= left.log_concentration
        for left, right in zip(points, points[1:])
    ):
        raise F5LikelihoodDiagnosticError("PROFILE_AUDIT_POINTS_MUST_BE_STRICTLY_INCREASING")
    maximum = max(point.profiled_log_likelihood for point in points)
    curvatures = tuple(
        point.profile_log_concentration_curvature for point in points
    )
    finite_curvatures = tuple(
        value for value in curvatures
        if value is not None and math.isfinite(value)
    )
    return BetaBinomialProfileAuditRecord(
        optimizer_convergence_status=optimizer_audit.status,
        identification_status="INDETERMINATE",
        profile_status=(
            "NUMERICAL_PROFILE_UNCERTIFIED"
            if all(point.status == "NUMERICAL_PROFILE_UNCERTIFIED" for point in points)
            else "PROFILE_HAS_BOUNDARY_OR_UNRESOLVED_POINTS"
        ),
        profile_point_count=len(points),
        profile_max_log_likelihood=float(maximum),
        binomial_boundary_profile_log_likelihood=(
            boundary.binomial_profile_log_likelihood
        ),
        two_point_boundary_profile_log_likelihood=(
            boundary.two_point_profile_log_likelihood
        ),
        two_point_boundary_status=boundary.two_point_boundary_status,
        profile_minus_binomial_boundary=float(
            maximum - boundary.binomial_profile_log_likelihood
        ),
        profile_minus_two_point_boundary=(
            float(maximum - boundary.two_point_profile_log_likelihood)
            if boundary.two_point_profile_log_likelihood is not None else None
        ),
        profile_curvature_values=curvatures,
        profile_curvature_min=(
            min(finite_curvatures) if finite_curvatures else None
        ),
        profile_curvature_max=(
            max(finite_curvatures) if finite_curvatures else None
        ),
    )


@dataclass(frozen=True)
class BetaBinomialProfileStabilityPoint:
    """Raw paired sensitivity values at one fixed log-concentration."""
    log_concentration: float
    reference_status: str
    refined_grid_status: str
    expanded_bounds_status: str
    refined_minus_reference_log_likelihood: float
    expanded_minus_reference_log_likelihood: float
    refined_minus_reference_mean_logit: float
    expanded_minus_reference_mean_logit: float
    refined_minus_reference_curvature: float | None
    expanded_minus_reference_curvature: float | None


@dataclass(frozen=True)
class BetaBinomialProfileStabilityAudit:
    """Numerical-control comparison; deliberately contains no pass threshold."""
    status: str
    identification_status: str
    reference_mean_logit_bounds: tuple[float, float]
    expanded_mean_logit_bounds: tuple[float, float]
    reference_mean_grid_size: int
    refined_mean_grid_size: int
    profile_point_count: int
    points: tuple[BetaBinomialProfileStabilityPoint, ...]
    max_abs_refined_log_likelihood_delta: float
    max_abs_expanded_log_likelihood_delta: float
    max_abs_refined_mean_logit_delta: float
    max_abs_expanded_mean_logit_delta: float


def beta_binomial_profile_numerical_stability(
    counts: Sequence[int],
    r: int,
    log_concentrations: Sequence[float],
    *,
    mean_logit_bounds: tuple[float, float] = (-18.0, 18.0),
    expanded_mean_logit_bounds: tuple[float, float] = (-24.0, 24.0),
    mean_grid_size: int = 65,
    refined_mean_grid_size: int = 257,
) -> BetaBinomialProfileStabilityAudit:
    """Compare profile traces under nuisance-grid refinement and wider bounds.

    Three deterministic traces are computed on the same log(kappa) points:
    reference controls, refined eta grid at the reference bounds, and the
    refined eta grid at expanded bounds. All paired differences are retained
    as raw diagnostics. No tolerance, threshold, or identification decision is
    applied; status remains NUMERICAL_STABILITY_NOT_ADJUDICATED.
    """
    if (type(mean_grid_size) is not int or type(refined_mean_grid_size) is not int
            or mean_grid_size < 17 or refined_mean_grid_size <= mean_grid_size):
        raise F5LikelihoodDiagnosticError("INVALID_STABILITY_GRID_SIZES")
    if (len(mean_logit_bounds) != 2 or len(expanded_mean_logit_bounds) != 2
            or not all(math.isfinite(float(v)) for v in
                       (*mean_logit_bounds, *expanded_mean_logit_bounds))):
        raise F5LikelihoodDiagnosticError("INVALID_STABILITY_MEAN_BOUNDS")
    lo, hi = (float(v) for v in mean_logit_bounds)
    wide_lo, wide_hi = (float(v) for v in expanded_mean_logit_bounds)
    if not (lo < hi and wide_lo < lo and wide_hi > hi):
        raise F5LikelihoodDiagnosticError("EXPANDED_BOUNDS_MUST_STRICTLY_CONTAIN_REFERENCE")
    xis = tuple(float(value) for value in log_concentrations)
    reference = beta_binomial_profile_log_concentration(
        counts, r, xis, mean_logit_bounds=(lo, hi),
        mean_grid_size=mean_grid_size,
    )
    refined = beta_binomial_profile_log_concentration(
        counts, r, xis, mean_logit_bounds=(lo, hi),
        mean_grid_size=refined_mean_grid_size,
    )
    expanded = beta_binomial_profile_log_concentration(
        counts, r, xis, mean_logit_bounds=(wide_lo, wide_hi),
        mean_grid_size=refined_mean_grid_size,
    )

    def curvature_delta(left: float | None, right: float | None) -> float | None:
        if left is None or right is None:
            return None
        if not (math.isfinite(left) and math.isfinite(right)):
            return None
        return float(right - left)

    rows = []
    for base, fine, wide in zip(reference, refined, expanded):
        rows.append(BetaBinomialProfileStabilityPoint(
            log_concentration=base.log_concentration,
            reference_status=base.status,
            refined_grid_status=fine.status,
            expanded_bounds_status=wide.status,
            refined_minus_reference_log_likelihood=float(
                fine.profiled_log_likelihood - base.profiled_log_likelihood
            ),
            expanded_minus_reference_log_likelihood=float(
                wide.profiled_log_likelihood - base.profiled_log_likelihood
            ),
            refined_minus_reference_mean_logit=float(
                fine.profiled_mean_logit - base.profiled_mean_logit
            ),
            expanded_minus_reference_mean_logit=float(
                wide.profiled_mean_logit - base.profiled_mean_logit
            ),
            refined_minus_reference_curvature=curvature_delta(
                base.profile_log_concentration_curvature,
                fine.profile_log_concentration_curvature,
            ),
            expanded_minus_reference_curvature=curvature_delta(
                base.profile_log_concentration_curvature,
                wide.profile_log_concentration_curvature,
            ),
        ))
    if not rows:
        raise F5LikelihoodDiagnosticError("STABILITY_AUDIT_REQUIRES_PROFILE_POINTS")
    return BetaBinomialProfileStabilityAudit(
        status="NUMERICAL_STABILITY_NOT_ADJUDICATED",
        identification_status="INDETERMINATE",
        reference_mean_logit_bounds=(lo, hi),
        expanded_mean_logit_bounds=(wide_lo, wide_hi),
        reference_mean_grid_size=mean_grid_size,
        refined_mean_grid_size=refined_mean_grid_size,
        profile_point_count=len(rows),
        points=tuple(rows),
        max_abs_refined_log_likelihood_delta=max(
            abs(row.refined_minus_reference_log_likelihood) for row in rows
        ),
        max_abs_expanded_log_likelihood_delta=max(
            abs(row.expanded_minus_reference_log_likelihood) for row in rows
        ),
        max_abs_refined_mean_logit_delta=max(
            abs(row.refined_minus_reference_mean_logit) for row in rows
        ),
        max_abs_expanded_mean_logit_delta=max(
            abs(row.expanded_minus_reference_mean_logit) for row in rows
        ),
    )
