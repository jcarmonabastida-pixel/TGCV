"""Deterministic F5 beta-binomial likelihood diagnostics.

Research-only numerical controls for C10-S post-holdout development.
No simulation, bootstrap, calibration, or scientific execution occurs here.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Integral
from typing import Sequence

from scipy.optimize import minimize
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
    independent_optimizer_success: bool
    independent_optimizer_message: str
    independent_log_likelihood: float | None
    absolute_log_likelihood_difference: float | None
    log_shape_parameter_distance: float | None
    binomial_limit_log_likelihood: float | None
    two_point_limit_log_likelihood: float | None
    starts: tuple[BetaBinomialStartOutcome, ...]


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
            hessian_eigenvalues=None, independent_optimizer_success=False,
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
        independent_optimizer_success=independent_success,
        independent_optimizer_message=str(independent.message),
        independent_log_likelihood=independent_ll,
        absolute_log_likelihood_difference=difference,
        log_shape_parameter_distance=shape_distance,
        binomial_limit_log_likelihood=boundary.binomial_limit_log_likelihood,
        two_point_limit_log_likelihood=boundary.two_point_mixing_limit_log_likelihood,
        starts=tuple(start_records),
    )
