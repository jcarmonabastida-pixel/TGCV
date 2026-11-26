"""Exact constrained score polynomials for F5 within/between profiles.

Research-only algebra primitive. It enumerates stationary candidates on a
fixed W or B likelihood constraint; it does not evaluate likelihood intervals,
certify a profile maximum, invert an LR set, calibrate a cutoff, or run data.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Mapping

from c10s_f5_rational_score_polynomials import (
    _a, _b, _c, _add, _mul, _scale,
    _uni_add_exact, _uni_mul_exact, _uni_pow_exact,
    _primitive_integer_polynomial, _uni_gcd, _uni_divmod,
    _uni_squarefree_factors, _uni_isolate_squarefree_unit_roots,
    beta_binomial_score_numerators,
)


class F5ConstrainedScoreError(ValueError):
    """Invalid or unresolved constrained F5 score-polynomial request."""


@dataclass(frozen=True)
class F5ConstrainedScorePolynomial:
    component: str
    target: Fraction
    coefficients_ascending: tuple[int, ...]
    degree: int
    stripped_boundary_factor_multiplicity: int
    status: str


@dataclass(frozen=True)
class F5ConstrainedScoreRoot:
    multiplicity: int
    exact_root: Fraction | None
    isolating_interval: tuple[Fraction, Fraction] | None
    feasibility: str


@dataclass(frozen=True)
class F5ConstrainedScoreRootSet:
    status: str
    roots: tuple[F5ConstrainedScoreRoot, ...]
    unresolved_intervals: tuple[tuple[Fraction, Fraction], ...]
    processed_intervals: int


def _target_fraction(value) -> Fraction:
    if isinstance(value, bool):
        raise F5ConstrainedScoreError("TARGET_MUST_BE_FINITE_RATIONAL")
    if isinstance(value, Fraction):
        result = value
    elif isinstance(value, int):
        result = Fraction(value)
    elif isinstance(value, float) and math.isfinite(value):
        result = Fraction.from_float(value)
    else:
        raise F5ConstrainedScoreError("TARGET_MUST_BE_FINITE_RATIONAL")
    if not 0 < result < Fraction(1, 4):
        raise F5ConstrainedScoreError("TARGET_MUST_LIE_STRICTLY_BETWEEN_ZERO_AND_ONE_QUARTER")
    return result


def _bivariate_product_for_denominators(r: int):
    d_mu = {(0, 0): 1}
    d_kappa_extra = {(0, 0): 1}
    for j in range(r):
        d_mu = _mul(d_mu, _mul(_a(j), _b(j)))
        d_kappa_extra = _mul(d_kappa_extra, _c(j))
    return d_mu, _mul(d_mu, d_kappa_extra)


def _component_stationary_bivariate(
    r: int, histogram: Mapping[int, int], component: str, target: Fraction,
):
    n_mu, n_kappa = beta_binomial_score_numerators(r, histogram)
    d_mu, d_kappa = _bivariate_product_for_denominators(r)

    # Q(mu) = denominator * (mu*(1-mu) - target), represented exactly
    # as an integer univariate polynomial and as a bivariate polynomial.
    den, num = target.denominator, target.numerator
    q_minus_target = {
        (0, 0): -num,
        (1, 0): den,
        (2, 0): -den,
    }
    q_prime = {(0, 0): 1, (1, 0): -2}

    if component == "W":
        q2 = _mul(q_minus_target, q_minus_target)
        first = _mul(_mul(q2, n_mu), d_kappa)
        second = _scale(
            _mul(_mul(q_prime, n_kappa), d_mu), num * den,
        )
        return _add(first, _scale(second, -1))
    if component == "B":
        first = _scale(_mul(n_mu, d_kappa), num)
        second = _mul(_mul(q_prime, n_kappa), d_mu)
        return _add(first, _scale(second, den))
    raise F5ConstrainedScoreError("COMPONENT_MUST_BE_W_OR_B")


def _substitute_concentration(
    polynomial, *, component: str, target: Fraction,
) -> list[Fraction]:
    den, num = target.denominator, target.numerator
    # Q(mu) = den*mu*(1-mu)-num.
    q_poly = [Fraction(-num), Fraction(den), Fraction(-den)]
    if not polynomial:
        return [Fraction(0)]
    degree_kappa = max(k for _, k in polynomial)
    output = [Fraction(0)]
    for (degree_mu, degree_kappa_term), coefficient in polynomial.items():
        if component == "W":
            # kappa = num / Q(mu); multiply by Q**degree_kappa.
            term = [Fraction(coefficient * (num ** degree_kappa_term))]
            term = _uni_mul_exact(
                term, _uni_pow_exact([Fraction(0), Fraction(1)], degree_mu),
            )
            term = _uni_mul_exact(
                term, _uni_pow_exact(q_poly, degree_kappa - degree_kappa_term),
            )
        else:
            # kappa = Q(mu) / num; multiply by num**degree_kappa.
            term = [Fraction(coefficient * (num ** (degree_kappa - degree_kappa_term)))]
            term = _uni_mul_exact(
                term, _uni_pow_exact([Fraction(0), Fraction(1)], degree_mu),
            )
            term = _uni_mul_exact(
                term, _uni_pow_exact(q_poly, degree_kappa_term),
            )
        output = _uni_add_exact(output, term)
    return output


def f5_component_profile_score_polynomial(
    r: int, count_histogram: Mapping[int, int], *,
    component: str, target,
) -> F5ConstrainedScorePolynomial:
    """Build the exact univariate score numerator for fixed W or B.

    W = mu*(1-mu)*kappa/(1+kappa); B = mu*(1-mu)/(1+kappa).
    The polynomial's interior roots are exactly the stationary points of the
    corresponding constrained likelihood, provided 0 < target < 1/4.
    Boundary points q(mu)=target are stripped and handled by their analytic
    kappa->infinity (W) or kappa->zero (B) likelihood limits.
    """
    if type(r) is not int or r < 2:
        raise F5ConstrainedScoreError("R_MUST_BE_INTEGER_GE_2")
    if component not in {"W", "B"}:
        raise F5ConstrainedScoreError("COMPONENT_MUST_BE_W_OR_B")
    target_value = _target_fraction(target)
    bivariate = _component_stationary_bivariate(
        r, count_histogram, component, target_value,
    )
    univariate = _substitute_concentration(
        bivariate, component=component, target=target_value,
    )
    primitive = _primitive_integer_polynomial(univariate)
    if primitive == [0]:
        return F5ConstrainedScorePolynomial(
            component, target_value, (), -1, 0, "DEGENERATE_CONSTRAINED_SCORE",
        )

    # q(mu)-target = 0 are exactly the two feasible-domain endpoints.
    # Remove all common endpoint factors; endpoints are evaluated separately.
    q_boundary = [
        Fraction(-target_value),
        Fraction(1),
        Fraction(-1),
    ]
    stripped = list(univariate)
    removed = 0
    removed_factor_sign_on_feasible_domain = 1
    while len(stripped) > 1:
        common = _uni_gcd(stripped, q_boundary)
        if len(common) <= 1:
            break
        # The monic gcd may have either sign on the feasible interval.
        # Its sign is constant there because all its roots are feasibility
        # endpoints. Evaluate at mu=1/2, which is strictly feasible.
        half_value = sum(
            coefficient * (Fraction(1, 2) ** degree)
            for degree, coefficient in enumerate(common)
        )
        if half_value == 0:
            raise F5ConstrainedScoreError("BOUNDARY_FACTOR_SIGN_UNRESOLVED")
        if half_value < 0:
            removed_factor_sign_on_feasible_domain *= -1
        quotient, remainder = _uni_divmod(stripped, common)
        if any(remainder):
            raise F5ConstrainedScoreError("BOUNDARY_FACTOR_REMOVAL_NOT_EXACT")
        stripped = quotient
        removed += 1
    # Preserve the sign of the original derivative numerator. The shared
    # primitive helper normalizes the leading coefficient positive, which is
    # suitable for root isolation but would otherwise erase score orientation.
    orientation = (1 if stripped[-1] > 0 else -1)
    orientation *= removed_factor_sign_on_feasible_domain
    primitive = _primitive_integer_polynomial(stripped)
    coefficients = tuple(orientation * value for value in primitive)
    if coefficients == (0,):
        return F5ConstrainedScorePolynomial(
            component, target_value, (), -1, removed, "DEGENERATE_CONSTRAINED_SCORE",
        )
    return F5ConstrainedScorePolynomial(
        component=component,
        target=target_value,
        coefficients_ascending=coefficients,
        degree=len(coefficients) - 1,
        stripped_boundary_factor_multiplicity=removed,
        status=(
            "NO_INTERIOR_STATIONARY_ROOTS"
            if len(coefficients) == 1 else "EXACT_SCORE_POLYNOMIAL_READY"
        ),
    )


def f5_isolate_component_profile_score_roots(
    polynomial: F5ConstrainedScorePolynomial, *,
    isolation_width: Fraction = Fraction(1, 2**48),
    max_depth: int = 160,
    max_intervals: int = 10000,
) -> F5ConstrainedScoreRootSet:
    """Isolate every real score root in (0,1), then retain feasible roots.

    A root is feasible only when q(mu)-target is strictly positive. A root
    interval overlapping a feasibility endpoint is not guessed or rounded:
    the result is UNRESOLVED_FEASIBILITY_CLASSIFICATION.
    """
    if polynomial.status == "DEGENERATE_CONSTRAINED_SCORE":
        return F5ConstrainedScoreRootSet(
            "NONISOLATED_OR_DEGENERATE_SCORE", (), (), 0,
        )
    if polynomial.status == "NO_INTERIOR_STATIONARY_ROOTS":
        return F5ConstrainedScoreRootSet("COMPLETE_NO_INTERIOR_ROOTS", (), (), 0)
    if not polynomial.coefficients_ascending:
        raise F5ConstrainedScoreError("SCORE_POLYNOMIAL_COEFFICIENTS_MISSING")

    target = polynomial.target
    roots: list[F5ConstrainedScoreRoot] = []
    unresolved: list[tuple[Fraction, Fraction]] = []
    processed = 0
    for factor in _uni_squarefree_factors(polynomial.coefficients_ascending):
        isolated = _uni_isolate_squarefree_unit_roots(
            factor["coefficients"], width=isolation_width,
            max_depth=max_depth, max_intervals=max_intervals,
        )
        processed += int(isolated["processed_intervals"])
        if isolated["status"] != "ISOLATION_COMPLETE":
            unresolved.extend(
                item["interval"] for item in isolated["unresolved_intervals"]
            )
        multiplicity = int(factor["multiplicity"])
        for root in isolated["exact_roots"]:
            q_minus_target = root * (1 - root) - target
            if q_minus_target > 0:
                roots.append(F5ConstrainedScoreRoot(
                    multiplicity, root, None, "FEASIBLE_INTERIOR",
                ))
            elif q_minus_target == 0:
                continue
        for item in isolated["isolating_intervals"]:
            left, right = item["interval"]
            left_value = left * (1 - left) - target
            right_value = right * (1 - right) - target
            if min(left_value, right_value) > 0:
                roots.append(F5ConstrainedScoreRoot(
                    multiplicity, None, (left, right), "FEASIBLE_INTERIOR",
                ))
            else:
                # q(mu)-target is concave. Its maximum on an interval is at
                # mu=1/2 when the interval contains that point, otherwise at
                # one of the interval endpoints.
                maximum_value = max(left_value, right_value)
                if left <= Fraction(1, 2) <= right:
                    maximum_value = max(
                        maximum_value, Fraction(1, 4) - target,
                    )
                if maximum_value < 0:
                    continue
                unresolved.append((left, right))

    if unresolved:
        return F5ConstrainedScoreRootSet(
            "UNRESOLVED_FEASIBILITY_CLASSIFICATION",
            tuple(roots), tuple(unresolved), processed,
        )
    roots.sort(key=lambda item: (
        item.exact_root if item.exact_root is not None
        else (item.isolating_interval[0] + item.isolating_interval[1]) / 2
    ))
    return F5ConstrainedScoreRootSet(
        "COMPLETE_ROOT_ISOLATION", tuple(roots), (), processed,
    )
