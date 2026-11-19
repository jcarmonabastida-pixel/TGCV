"""Independent finite-sample beta-binomial variance-component oracles.

F5 development reference only. No bootstrap calibration, coverage study,
production Analyzer integration, or C10 scientific execution is performed.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.special import betaln, gammaln


class BetaBinomialOracleError(ValueError):
    """Invalid beta-binomial oracle parameters."""


@dataclass(frozen=True)
class BetaBinomialVarianceReference:
    alpha: float
    beta: float
    m: int
    r: int
    pmf_cluster_count: tuple[float, ...]
    true_within: float
    true_between: float
    observed_world_mean_variance: float
    true_mcse: float
    expected_within_estimator: float
    expected_observed_world_variance: float
    expected_raw_between_estimator: float
    variance_within_estimator: float
    variance_observed_world_variance_estimator: float
    covariance_within_observed_world_variance: float
    variance_raw_between_estimator: float


def beta_binomial_f5_reference(
    *, alpha: float, beta: float, m: int, r: int,
) -> BetaBinomialVarianceReference:
    """Exact finite-R count law and finite-M moments of nested estimators.

    For each world, p_m ~ Beta(alpha,beta), then X_m|p_m ~ Binomial(r,p_m).
    The observed world contribution is q_m=X_m/r. The within estimator is
    the average of the unbiased sample variances within worlds; the observed
    between estimator is S²(q_m)-MSW/r and is deliberately not truncated.

    The function computes the exact beta-binomial PMF for X_m and uses its
    finite support to obtain exact moments, including covariance between the
    within and observed-world-variance estimators. It does not provide
    inferential intervals or calibrated cutoffs.
    """
    _validate(alpha, beta, m, r)
    a, b = float(alpha), float(beta)
    total = a + b
    mean_p = a / total
    true_between = a * b / (total * total * (total + 1.0))
    true_within = a * b / (total * (total + 1.0))
    observed_var = true_between + true_within / r

    counts = np.arange(r + 1, dtype=float)
    log_choose = gammaln(r + 1.0) - gammaln(counts + 1.0) - gammaln(r - counts + 1.0)
    log_pmf = (
        log_choose + betaln(a + counts, b + r - counts) - betaln(a, b)
    )
    pmf = np.exp(log_pmf)
    pmf /= math.fsum(float(value) for value in pmf)

    q = counts / r
    within_world = counts * (r - counts) / (r * (r - 1.0))
    mean_q = float(np.dot(pmf, q))
    centered_q = q - mean_q
    mean_within = float(np.dot(pmf, within_world))
    var_within_world = float(np.dot(pmf, (within_world - mean_within) ** 2))
    var_q = float(np.dot(pmf, centered_q ** 2))
    mu4_q = float(np.dot(pmf, centered_q ** 4))
    cov_within_q2 = float(np.dot(
        pmf, (within_world - mean_within) * centered_q ** 2,
    ))

    # For iid worlds: Var(S²) = [mu4 - ((M-3)/(M-1))*var²] / M.
    var_s2_q = (
        mu4_q - ((m - 3.0) / (m - 1.0)) * var_q * var_q
    ) / m
    var_mean_within = var_within_world / m
    cov_mean_within_s2 = cov_within_q2 / m
    var_raw_between = (
        var_s2_q + var_mean_within / (r * r)
        - 2.0 * cov_mean_within_s2 / r
    )

    return BetaBinomialVarianceReference(
        alpha=a, beta=b, m=m, r=r,
        pmf_cluster_count=tuple(float(x) for x in pmf),
        true_within=true_within,
        true_between=true_between,
        observed_world_mean_variance=observed_var,
        true_mcse=math.sqrt(observed_var / m),
        expected_within_estimator=mean_within,
        expected_observed_world_variance=var_q,
        expected_raw_between_estimator=var_q - mean_within / r,
        variance_within_estimator=var_mean_within,
        variance_observed_world_variance_estimator=var_s2_q,
        covariance_within_observed_world_variance=cov_mean_within_s2,
        variance_raw_between_estimator=var_raw_between,
    )


def _validate(alpha: float, beta: float, m: int, r: int) -> None:
    for name, value in (("alpha", alpha), ("beta", beta)):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise BetaBinomialOracleError(f"{name} must be finite and > 0")
        if not math.isfinite(value) or value <= 0:
            raise BetaBinomialOracleError(f"{name} must be finite and > 0")
    if type(m) is not int or m < 2:
        raise BetaBinomialOracleError("m must be an integer >= 2")
    if type(r) is not int or r < 2:
        raise BetaBinomialOracleError("r must be an integer >= 2")
