"""Exact sparse integer numerators for the F5 beta-binomial score equations.

Research-only deterministic algebra primitive. No floating-point coefficients,
symbolic simplification, or scientific data generation is used.
Polynomial representation: {(degree_mu, degree_kappa): integer coefficient}.
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping


Poly = dict[tuple[int, int], int]


def _add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, 0) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def _scale(a: Poly, scalar: int) -> Poly:
    if scalar == 0:
        return {}
    return {m: c * scalar for m, c in a.items() if c * scalar}


def _mul(a: Poly, b: Poly) -> Poly:
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (i, j), x in a.items():
        for (u, v), y in b.items():
            out[(i + u, j + v)] += x * y
    return {m: c for m, c in out.items() if c}


def _excluded_products(factors: list[Poly]) -> list[Poly]:
    """Return product(factors except factors[i]) for every i, exactly."""
    prefix = [{(0, 0): 1}]
    for factor in factors:
        prefix.append(_mul(prefix[-1], factor))
    suffix: list[Poly] = [{} for _ in range(len(factors) + 1)]
    suffix[-1] = {(0, 0): 1}
    for i in range(len(factors) - 1, -1, -1):
        suffix[i] = _mul(factors[i], suffix[i + 1])
    return [_mul(prefix[i], suffix[i + 1]) for i in range(len(factors))]


def _a(j: int) -> Poly:
    # mu*kappa + j
    return {(1, 1): 1, **({(0, 0): j} if j else {})}


def _b(j: int) -> Poly:
    # (1-mu)*kappa + j
    out = {(0, 1): 1, (1, 1): -1}
    if j:
        out[(0, 0)] = j
    return out


def _c(j: int) -> Poly:
    # kappa + j
    return {(0, 1): 1, **({(0, 0): j} if j else {})}


def beta_binomial_score_numerators(
    r: int, count_histogram: Mapping[int, int]
) -> tuple[Poly, Poly]:
    """Build exact numerator polynomials (N_mu, N_kappa).

    The rational scores satisfy:
        S_mu = N_mu / product_j[(mu*k+j)((1-mu)*k+j)]
        S_k  = N_k  / product_j[(mu*k+j)((1-mu)*k+j)(k+j)]
    throughout the open parameter domain 0<mu<1, kappa>0.

    Histogram keys are counts x in [0,r], values are nonnegative integer
    multiplicities. Zero multiplicities are ignored. Coefficients are exact
    Python integers. No resultant or root-isolation claim is made here.
    """
    if type(r) is not int or r < 1:
        raise ValueError("R_MUST_BE_POSITIVE_INTEGER")
    if not isinstance(count_histogram, Mapping) or not count_histogram:
        raise ValueError("NONEMPTY_COUNT_HISTOGRAM_REQUIRED")
    hist: dict[int, int] = {}
    for x, n in count_histogram.items():
        if type(x) is not int or not 0 <= x <= r:
            raise ValueError("COUNT_OUTSIDE_0_TO_R")
        if type(n) is not int or n < 0:
            raise ValueError("MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER")
        if n:
            hist[x] = hist.get(x, 0) + n
    if not hist:
        raise ValueError("POSITIVE_TOTAL_MULTIPLICITY_REQUIRED")

    a_factors = [_a(j) for j in range(r)]
    b_factors = [_b(j) for j in range(r)]
    c_factors = [_c(j) for j in range(r)]
    ab_excluded = _excluded_products(a_factors + b_factors)

    n_mu: Poly = {}
    for j in range(r):
        count_a = sum(n for x, n in hist.items() if x > j)
        count_b = sum(n for x, n in hist.items() if r - x > j)
        if count_a:
            n_mu = _add(n_mu, _scale(_mul({(0, 1): 1}, ab_excluded[j]), count_a))
        if count_b:
            n_mu = _add(
                n_mu, _scale(_mul({(0, 1): 1}, ab_excluded[r + j]), -count_b)
            )

    abc_excluded = _excluded_products(a_factors + b_factors + c_factors)
    n_kappa: Poly = {}
    total = sum(hist.values())
    for j in range(r):
        count_a = sum(n for x, n in hist.items() if x > j)
        count_b = sum(n for x, n in hist.items() if r - x > j)
        if count_a:
            n_kappa = _add(
                n_kappa, _scale(_mul({(1, 0): 1}, abc_excluded[j]), count_a)
            )
        if count_b:
            n_kappa = _add(
                n_kappa,
                _scale(
                    _mul({(0, 0): 1, (1, 0): -1}, abc_excluded[r + j]),
                    count_b,
                ),
            )
        if total:
            n_kappa = _add(n_kappa, _scale(abc_excluded[2 * r + j], -total))

    return n_mu, n_kappa
