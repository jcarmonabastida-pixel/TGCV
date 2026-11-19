"""Deterministic F5 beta-binomial likelihood diagnostics.

Research-only numerical controls for C10-S post-holdout development.
No simulation, bootstrap, calibration, or scientific execution occurs here.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Integral
from typing import Sequence

from scipy.special import betaln, digamma, gammaln, polygamma


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
