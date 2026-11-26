"""Exact constrained score polynomials for F5 within/between profiles.

Research-only algebra primitive. It enumerates stationary candidates on a
fixed W or B likelihood constraint; it does not evaluate likelihood intervals,
certify a profile maximum, invert an LR set, calibrate a cutoff, or run data.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Callable, Mapping, Sequence

from c10s_f5_rational_score_polynomials import (
    _a, _b, _c, _add, _mul, _scale,
    _uni_add_exact, _uni_mul_exact, _uni_pow_exact,
    _primitive_integer_polynomial, _uni_gcd, _uni_divmod,
    _uni_squarefree_factors, _uni_isolate_squarefree_unit_roots, _uni_monic,
    _beta_binomial_likelihood_enclosure, beta_binomial_score_numerators,
    beta_binomial_global_mle_certificate,
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


def _q_bounds(mu_bounds: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    lo, hi = mu_bounds
    q_lo = lo * (1 - lo)
    q_hi = hi * (1 - hi)
    minimum = min(q_lo, q_hi)
    maximum = max(q_lo, q_hi)
    if lo <= Fraction(1, 2) <= hi:
        maximum = Fraction(1, 4)
    return minimum, maximum


def _boundary_profile_likelihood(
    component: str, r: int, histogram: Mapping[int, int],
    mu_bounds: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Exact likelihood enclosure at the fixed-W/B concentration endpoint."""
    from math import comb

    lo, hi = mu_bounds
    total_worlds = sum(histogram.values())
    if component == "W":
        # kappa -> infinity: product of Binomial(r, mu) count probabilities.
        successes = sum(x * n for x, n in histogram.items())
        failures = total_worlds * r - successes
        combinatorial = math.prod(
            comb(r, x) ** n for x, n in histogram.items() if n
        )

        def likelihood(mu: Fraction) -> Fraction:
            return Fraction(combinatorial) * (mu ** successes) * ((1 - mu) ** failures)

        candidates = [likelihood(lo), likelihood(hi)]
        mode = Fraction(successes, total_worlds * r)
        if lo <= mode <= hi:
            candidates.append(likelihood(mode))
        return min(candidates), max(candidates)

    # kappa -> zero: only all-zero/all-R world counts have positive mass.
    if any(n and 0 < x < r for x, n in histogram.items()):
        return Fraction(0), Fraction(0)
    n_zero = histogram.get(0, 0)
    n_full = histogram.get(r, 0)

    def likelihood(mu: Fraction) -> Fraction:
        return (mu ** n_full) * ((1 - mu) ** n_zero)

    candidates = [likelihood(lo), likelihood(hi)]
    if total_worlds:
        mode = Fraction(n_full, total_worlds)
        if lo <= mode <= hi:
            candidates.append(likelihood(mode))
    return min(candidates), max(candidates)




def _target_fraction_closed(value) -> Fraction:
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
    if not 0 <= result <= Fraction(1, 4):
        raise F5ConstrainedScoreError("TARGET_MUST_LIE_IN_CLOSED_ZERO_TO_ONE_QUARTER")
    return result


def _exact_endpoint_profile_likelihood(
    r: int, histogram: Mapping[int, int], *,
    component: str, target: Fraction,
) -> tuple[Fraction, str]:
    from math import comb

    worlds = sum(histogram.values())
    successes = sum(x * n for x, n in histogram.items())
    trials = worlds * r
    combinatorial = math.prod(
        comb(r, x) ** n for x, n in histogram.items() if n
    )
    has_interior = any(n and 0 < x < r for x, n in histogram.items())
    if target == 0:
        if component == "W":
            # W=0 is the two-point concentration boundary, profiled over mu.
            if has_interior:
                return Fraction(0), "TWO_POINT_LIMIT_ZERO_WITH_INTERIOR_COUNTS"
            n_full = histogram.get(r, 0)
            n_zero = histogram.get(0, 0)
            mu_hat = Fraction(n_full, worlds)
            value = (mu_hat ** n_full) * ((1 - mu_hat) ** n_zero)
            return value, "TWO_POINT_LIMIT_PROFILE"
        # B=0 is the binomial concentration boundary, profiled over mu.
        mu_hat = Fraction(successes, trials)
        value = Fraction(combinatorial) * (mu_hat ** successes) * ((1 - mu_hat) ** (trials - successes))
        return value, "BINOMIAL_LIMIT_PROFILE"
    if component == "W":
        # W=1/4: mu=1/2 and kappa -> infinity.
        return Fraction(combinatorial, 2 ** trials), "BINOMIAL_LIMIT_MU_HALF"
    # B=1/4: mu=1/2 and kappa -> zero.
    if has_interior:
        return Fraction(0), "TWO_POINT_LIMIT_ZERO_WITH_INTERIOR_COUNTS"
    return Fraction(1, 2 ** worlds), "TWO_POINT_LIMIT_MU_HALF"


def f5_component_profile_maximum_enclosure(
    r: int, count_histogram: Mapping[int, int], *,
    component: str, target,
    root_isolation_width: Fraction = Fraction(1, 2**64),
    max_depth: int = 180,
    max_intervals: int = 10000,
    max_fraction_bits: int = 200000,
) -> dict[str, object]:
    """Enclose the global constrained profile likelihood at fixed W or B.

    Every interior stationary point is enumerated by the exact univariate score
    polynomial and Sturm isolation. The two analytic concentration-limit
    endpoints are included. Likelihoods at interior root boxes use the existing
    outward-rounded rational enclosure; endpoint likelihoods use exact
    binomial/two-point formulas over algebraic-root intervals.

    This is a profile-*maximum* enclosure only. It does not construct an LR
    confidence set or select/calibrate a likelihood-ratio cutoff.
    """
    if component not in {"W", "B"}:
        raise F5ConstrainedScoreError("COMPONENT_MUST_BE_W_OR_B")
    if type(r) is not int or r < 2:
        raise F5ConstrainedScoreError("R_MUST_BE_INTEGER_GE_2")
    target_value = _target_fraction_closed(target)
    # Reuse the canonical histogram validator even on closed-domain endpoints.
    beta_binomial_score_numerators(r, count_histogram)
    if target_value in {Fraction(0), Fraction(1, 4)}:
        endpoint_value, endpoint_kind = _exact_endpoint_profile_likelihood(
            r, count_histogram, component=component, target=target_value,
        )
        return {
            "status": "PROFILE_MAXIMUM_ENCLOSED",
            "component": component,
            "target": target_value,
            "profile_likelihood_bounds": (endpoint_value, endpoint_value),
            "candidate_count": 1,
            "interior_stationary_count": 0,
            "candidates": ({
                "kind": endpoint_kind,
                "likelihood_bounds": (endpoint_value, endpoint_value),
            },),
            "root_set": None,
            "endpoint_root_set": None,
            "likelihood_ordering": "EXACT_CLOSED_DOMAIN_ENDPOINT_PROFILE",
        }
    polynomial = f5_component_profile_score_polynomial(
        r, count_histogram, component=component, target=target_value,
    )
    roots = f5_isolate_component_profile_score_roots(
        polynomial, isolation_width=root_isolation_width,
        max_depth=max_depth, max_intervals=max_intervals,
    )
    if roots.status not in {"COMPLETE_ROOT_ISOLATION", "COMPLETE_NO_INTERIOR_ROOTS"}:
        return {
            "status": "PROFILE_STATIONARY_ROOT_CENSUS_UNRESOLVED",
            "component": component, "target": target_value,
            "polynomial": polynomial, "root_set": roots,
        }

    # The two feasible-domain endpoints solve mu*(1-mu)=target exactly.
    boundary_poly = _uni_monic([
        -target_value, Fraction(1), Fraction(-1),
    ])
    endpoints = _uni_isolate_squarefree_unit_roots(
        boundary_poly, width=root_isolation_width,
        max_depth=max_depth, max_intervals=max_intervals,
    )
    if endpoints["status"] != "ISOLATION_COMPLETE":
        return {
            "status": "PROFILE_ENDPOINT_ISOLATION_UNRESOLVED",
            "component": component, "target": target_value,
            "polynomial": polynomial, "root_set": roots,
            "endpoint_root_set": endpoints,
        }
    endpoint_intervals = []
    for value in endpoints["exact_roots"]:
        endpoint_intervals.append((value, value))
    for item in endpoints["isolating_intervals"]:
        endpoint_intervals.append(item["interval"])
    endpoint_intervals.sort(key=lambda pair: (pair[0] + pair[1]) / 2)
    if len(endpoint_intervals) != 2:
        return {
            "status": "PROFILE_ENDPOINT_COUNT_UNRESOLVED",
            "component": component, "target": target_value,
            "endpoint_root_set": endpoints,
        }

    candidates = []
    for index, mu_bounds in enumerate(endpoint_intervals):
        likelihood_bounds = _boundary_profile_likelihood(
            component, r, count_histogram, mu_bounds,
        )
        candidates.append({
            "kind": "BINOMIAL_LIMIT" if component == "W" else "TWO_POINT_LIMIT",
            "endpoint_index": index,
            "mu_bounds": mu_bounds,
            "t_bounds": (Fraction(1), Fraction(1)) if component == "W"
                        else (Fraction(0), Fraction(0)),
            "likelihood_bounds": likelihood_bounds,
        })

    for index, root in enumerate(roots.roots):
        if root.exact_root is not None:
            mu_lo = mu_hi = root.exact_root
        else:
            mu_lo, mu_hi = root.isolating_interval
        mu_bounds = (mu_lo, mu_hi)
        q_min, q_max = _q_bounds(mu_bounds)
        if q_min <= target_value:
            return {
                "status": "PROFILE_ROOT_BOX_NOT_STRICTLY_FEASIBLE",
                "component": component, "target": target_value,
                "root": root, "root_set": roots,
            }
        if component == "W":
            t_bounds = (target_value / q_max, target_value / q_min)
        else:
            t_bounds = (
                1 - target_value / q_min,
                1 - target_value / q_max,
            )
        if not (0 < t_bounds[0] <= t_bounds[1] < 1):
            return {
                "status": "PROFILE_ROOT_PARAMETER_BOX_INVALID",
                "component": component, "target": target_value,
                "root": root, "t_bounds": t_bounds,
            }
        enclosure = _beta_binomial_likelihood_enclosure(
            r, count_histogram, mu_bounds=mu_bounds,
            t_bounds=t_bounds, max_fraction_bits=max_fraction_bits,
        )
        if enclosure.get("status") != "EXACT_RATIONAL_LIKELIHOOD_ENCLOSURE":
            return {
                "status": "PROFILE_ROOT_LIKELIHOOD_ENCLOSURE_UNRESOLVED",
                "component": component, "target": target_value,
                "root": root, "likelihood_enclosure": enclosure,
            }
        candidates.append({
            "kind": "INTERIOR_STATIONARY_POINT",
            "stationary_index": index,
            "multiplicity": root.multiplicity,
            "mu_bounds": mu_bounds,
            "t_bounds": t_bounds,
            "likelihood_bounds": enclosure["likelihood_bounds"],
            "likelihood_precision_bits": enclosure["precision_bits"],
        })

    maximum_lower = max(item["likelihood_bounds"][0] for item in candidates)
    maximum_upper = max(item["likelihood_bounds"][1] for item in candidates)
    if maximum_lower <= 0:
        return {
            "status": "PROFILE_MAXIMUM_LOWER_BOUND_ZERO",
            "component": component, "target": target_value,
            "candidates": tuple(candidates),
            "root_set": roots,
        }
    return {
        "status": "PROFILE_MAXIMUM_ENCLOSED",
        "component": component,
        "target": target_value,
        "profile_likelihood_bounds": (maximum_lower, maximum_upper),
        "candidate_count": len(candidates),
        "interior_stationary_count": len(roots.roots),
        "candidates": tuple(candidates),
        "root_set": roots,
        "endpoint_root_set": endpoints,
        "likelihood_ordering": "MAXIMUM_OF_ALL_STATIONARY_AND_ANALYTIC_ENDPOINT_ENCLOSURES",
    }


def _log_positive_fraction_interval(
    value: Fraction, *, terms: int = 100,
) -> tuple[Fraction, Fraction]:
    """Rigorous rational enclosure of log(value) via the atanh series."""
    if not isinstance(value, Fraction) or value <= 0:
        raise F5ConstrainedScoreError("LOG_ARGUMENT_MUST_BE_POSITIVE_FRACTION")
    if type(terms) is not int or terms < 1:
        raise F5ConstrainedScoreError("LOG_SERIES_TERMS_MUST_BE_POSITIVE_INTEGER")
    if value == 1:
        return Fraction(0), Fraction(0)
    if value < 1:
        lo, hi = _log_positive_fraction_interval(1 / value, terms=terms)
        return -hi, -lo

    def log_unit_interval(y: Fraction) -> tuple[Fraction, Fraction]:
        # 1 <= y <= 2 gives 0 <= z=(y-1)/(y+1) <= 1/3.
        z = (y - 1) / (y + 1)
        z2 = z * z
        partial = Fraction(0)
        power = z
        for index in range(terms):
            partial += 2 * power / (2 * index + 1)
            power *= z2
        remainder = (
            2 * power
            / ((2 * terms + 1) * (1 - z2))
        )
        return partial, partial + remainder

    # Find exact integer k with 1 <= value / 2**k < 2.
    k = value.numerator.bit_length() - value.denominator.bit_length()
    if k >= 0:
        scaled = value / (1 << k)
    else:
        scaled = value * (1 << (-k))
    if scaled < 1:
        k -= 1
        scaled *= 2
    elif scaled >= 2:
        k += 1
        scaled /= 2

    log_two = log_unit_interval(Fraction(2))
    log_scaled = log_unit_interval(scaled)
    if k >= 0:
        return (
            k * log_two[0] + log_scaled[0],
            k * log_two[1] + log_scaled[1],
        )
    return (
        k * log_two[1] + log_scaled[0],
        k * log_two[0] + log_scaled[1],
    )


def f5_component_profile_lr_statistic(
    r: int, count_histogram: Mapping[int, int], *,
    component: str, target,
    global_certificate: Mapping[str, object] | None = None,
    root_isolation_width: Fraction = Fraction(1, 2**64),
    max_depth: int = 180,
    max_intervals: int = 10000,
    max_fraction_bits: int = 200000,
    log_series_terms: int = 100,
) -> dict[str, object]:
    """Enclose the LR statistic for a fixed W or B target.

    The unrestricted maximum is taken from the existing exact global-MLE
    certificate. The constrained profile maximum is enumerated by the exact
    one-dimensional score polynomial and likelihood enclosures. Logarithms
    are enclosed with a rational atanh-series remainder, not floating logs.
    """
    if global_certificate is None:
        global_certificate = beta_binomial_global_mle_certificate(
            r, count_histogram,
        )
    global_status = global_certificate.get("status")
    if global_status == "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED":
        winner = global_certificate.get("winner")
        global_candidates = [winner] if isinstance(winner, Mapping) else []
    elif global_status == "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED":
        winner = global_certificate.get("winner")
        if isinstance(winner, Mapping):
            global_candidates = [winner]
        else:
            winners = global_certificate.get("winners")
            global_candidates = list(winners) if isinstance(winners, (tuple, list)) else []
    elif global_status == "GLOBAL_CO_MAXIMIZERS_CERTIFIED":
        winners = global_certificate.get("winners")
        global_candidates = list(winners) if isinstance(winners, (tuple, list)) else []
    else:
        return {
            "status": "UNRESTRICTED_GLOBAL_MLE_UNRESOLVED",
            "global_mle_status": global_status,
            "global_likelihood_ordering": global_certificate.get("likelihood_ordering"),
        }
    if not global_candidates:
        return {
            "status": "UNRESTRICTED_GLOBAL_MLE_WINNER_MISSING",
            "global_mle_status": global_status,
        }
    try:
        global_lower = max(item["likelihood_bounds"][0] for item in global_candidates)
        global_upper = max(item["likelihood_bounds"][1] for item in global_candidates)
    except (KeyError, TypeError, ValueError):
        return {
            "status": "UNRESTRICTED_GLOBAL_MLE_BOUNDS_MALFORMED",
            "global_mle_status": global_status,
        }

    profile = f5_component_profile_maximum_enclosure(
        r, count_histogram, component=component, target=target,
        root_isolation_width=root_isolation_width,
        max_depth=max_depth, max_intervals=max_intervals,
        max_fraction_bits=max_fraction_bits,
    )
    if profile.get("status") != "PROFILE_MAXIMUM_ENCLOSED":
        return {
            "status": "CONSTRAINED_PROFILE_MAXIMUM_UNRESOLVED",
            "global_mle_status": global_status,
            "profile": profile,
        }
    profile_lower, profile_upper = profile["profile_likelihood_bounds"]
    if global_lower <= 0:
        return {
            "status": "LR_LIKELIHOOD_LOWER_BOUND_ZERO",
            "global_mle_status": global_status,
            "global_likelihood_bounds": (global_lower, global_upper),
            "profile": profile,
        }
    if profile_upper == 0:
        return {
            "status": "LR_STATISTIC_INFINITE",
            "component": component,
            "target": profile["target"],
            "global_mle_status": global_status,
            "global_likelihood_bounds": (global_lower, global_upper),
            "profile_likelihood_bounds": (profile_lower, profile_upper),
            "likelihood_ratio_bounds": None,
            "lr_statistic_bounds": (math.inf, math.inf),
            "reason": "CONSTRAINED_PROFILE_LIKELIHOOD_IS_EXACTLY_ZERO",
            "profile": profile,
        }
    if profile_lower <= 0:
        return {
            "status": "LR_LIKELIHOOD_LOWER_BOUND_ZERO",
            "global_mle_status": global_status,
            "global_likelihood_bounds": (global_lower, global_upper),
            "profile": profile,
        }

    ratio_lower = global_lower / profile_upper
    ratio_upper = global_upper / profile_lower
    if ratio_upper < 1:
        return {
            "status": "PROFILE_LIKELIHOOD_EXCEEDS_GLOBAL_MLE_ENCLOSURE",
            "global_mle_status": global_status,
            "global_likelihood_bounds": (global_lower, global_upper),
            "profile": profile,
            "likelihood_ratio_bounds": (ratio_lower, ratio_upper),
        }
    ratio_lower = max(Fraction(1), ratio_lower)
    log_lower = _log_positive_fraction_interval(
        ratio_lower, terms=log_series_terms,
    )[0]
    log_upper = _log_positive_fraction_interval(
        ratio_upper, terms=log_series_terms,
    )[1]
    return {
        "status": "LR_STATISTIC_ENCLOSED",
        "component": component,
        "target": profile["target"],
        "global_mle_status": global_status,
        "global_likelihood_bounds": (global_lower, global_upper),
        "profile_likelihood_bounds": (profile_lower, profile_upper),
        "likelihood_ratio_bounds": (ratio_lower, ratio_upper),
        "lr_statistic_bounds": (2 * log_lower, 2 * log_upper),
        "log_series_terms": log_series_terms,
        "globality_basis": (
            "EXACT_UNRESTRICTED_GLOBAL_MLE_CERTIFICATE_PLUS_COMPLETE_"
            "CONSTRAINED_STATIONARY_ROOT_AND_ENDPOINT_CENSUS"
        ),
        "profile": profile,
    }



def _classify_profile_lr_result(
    result: Mapping[str, object], cutoff: Fraction,
) -> str:
    status = result.get("status")
    if status == "LR_STATISTIC_INFINITE":
        return "OUT"
    if status != "LR_STATISTIC_ENCLOSED":
        return "AMBIGUOUS"
    bounds = result.get("lr_statistic_bounds")
    if not isinstance(bounds, (tuple, list)) or len(bounds) != 2:
        return "AMBIGUOUS"
    lower, upper = bounds
    if upper <= cutoff:
        return "IN"
    if lower > cutoff:
        return "OUT"
    return "AMBIGUOUS"


def _scan_profile_lr_grid(
    nodes: Sequence[Fraction], *,
    cutoff: Fraction,
    evaluate: Callable[[Fraction], Mapping[str, object]],
    max_bisection_steps: int = 6,
) -> dict[str, object]:
    """Retain every grid-detected LR component and bracket each crossing.

    This is explicitly a numerical topology scan, not a proof that a finer
    component was not missed between two rejected grid nodes.
    """
    ordered = tuple(sorted(set(nodes)))
    if len(ordered) < 3 or ordered[0] != 0 or ordered[-1] != Fraction(1, 4):
        raise F5ConstrainedScoreError("LR_GRID_MUST_COVER_CLOSED_FUNCTIONAL_DOMAIN")
    if any(not 0 <= value <= Fraction(1, 4) for value in ordered):
        raise F5ConstrainedScoreError("LR_GRID_TARGET_OUTSIDE_CLOSED_DOMAIN")
    if type(max_bisection_steps) is not int or max_bisection_steps < 0:
        raise F5ConstrainedScoreError("MAX_BISECTION_STEPS_MUST_BE_NONNEGATIVE_INTEGER")

    cache: dict[Fraction, tuple[str, Mapping[str, object]]] = {}

    def classify(value: Fraction) -> str:
        if value not in cache:
            result = evaluate(value)
            cache[value] = (_classify_profile_lr_result(result, cutoff), result)
        return cache[value][0]

    for value in ordered:
        if classify(value) == "AMBIGUOUS":
            return {
                "status": "UNRESOLVED_GRID_CUTOFF_CLASSIFICATION",
                "grid": ordered,
                "evaluated": tuple((v, cache[v][0]) for v in ordered if v in cache),
                "target_evaluations": len(cache),
                "topology_certified": False,
            }

    def refine_lower(outside: Fraction, inside: Fraction):
        for _ in range(max_bisection_steps):
            midpoint = (outside + inside) / 2
            state = classify(midpoint)
            if state == "IN":
                inside = midpoint
            elif state == "OUT":
                outside = midpoint
            else:
                return None
        return outside, inside

    def refine_upper(inside: Fraction, outside: Fraction):
        for _ in range(max_bisection_steps):
            midpoint = (inside + outside) / 2
            state = classify(midpoint)
            if state == "IN":
                inside = midpoint
            elif state == "OUT":
                outside = midpoint
            else:
                return None
        return inside, outside

    accepted = [classify(value) == "IN" for value in ordered]
    components = []
    brackets = []
    index = 0
    while index < len(ordered):
        if not accepted[index]:
            index += 1
            continue
        start = index
        while index + 1 < len(ordered) and accepted[index + 1]:
            index += 1
        end = index

        if start == 0:
            lower = Fraction(0)
            lower_bracket = (Fraction(0), Fraction(0))
        else:
            refined = refine_lower(ordered[start - 1], ordered[start])
            if refined is None:
                return {
                    "status": "UNRESOLVED_LOWER_CROSSING",
                    "grid": ordered, "target_evaluations": len(cache),
                    "topology_certified": False,
                }
            lower, inside_lower = refined
            lower_bracket = (lower, inside_lower)

        if end == len(ordered) - 1:
            upper = Fraction(1, 4)
            upper_bracket = (Fraction(1, 4), Fraction(1, 4))
        else:
            refined = refine_upper(ordered[end], ordered[end + 1])
            if refined is None:
                return {
                    "status": "UNRESOLVED_UPPER_CROSSING",
                    "grid": ordered, "target_evaluations": len(cache),
                    "topology_certified": False,
                }
            inside_upper, upper = refined
            upper_bracket = (inside_upper, upper)

        components.append((lower, upper))
        brackets.append({
            "lower_outside_inside": lower_bracket,
            "upper_inside_outside": upper_bracket,
        })
        index += 1

    if not components:
        status = "EMPTY_LR_SET_ON_NUMERICAL_GRID"
    elif len(components) == 1:
        status = "GRID_DETECTED_SINGLE_COMPONENT_BRACKETED"
    else:
        status = "GRID_DETECTED_DISCONNECTED_COMPONENTS_BRACKETED"
    return {
        "status": status,
        "confidence_components": tuple(components),
        "crossing_brackets": tuple(brackets),
        "grid": ordered,
        "grid_states": tuple((value, cache[value][0]) for value in ordered),
        "target_evaluations": len(cache),
        "max_bisection_steps": max_bisection_steps,
        "topology_certified": False,
        "topology_caveat": (
            "A component narrower than the scan spacing can be missed; "
            "nested-grid convergence is a separate required diagnostic."
        ),
    }


def _global_mle_functional_centers(
    global_certificate: Mapping[str, object], component: str,
) -> tuple[Fraction, ...] | None:
    status = global_certificate.get("status")
    if status == "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED":
        candidates = [global_certificate.get("winner")]
    elif status in {
        "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
        "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
    }:
        winner = global_certificate.get("winner")
        winners = global_certificate.get("winners")
        candidates = (
            [winner] if isinstance(winner, Mapping)
            else list(winners) if isinstance(winners, (tuple, list))
            else []
        )
    else:
        return None

    census = global_certificate.get("census")
    boundaries = (
        census.get("boundary_likelihoods", {})
        if isinstance(census, Mapping) else {}
    )
    centers = []
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            return None
        if candidate.get("kind") == "INTERIOR_STATIONARY_ROOT":
            box = candidate.get("parameter_box")
            if not isinstance(box, (tuple, list)) or len(box) != 2:
                return None
            mu_bounds, t_bounds = box
            q_min, q_max = _q_bounds(tuple(mu_bounds))
            t_lo, t_hi = t_bounds
            if component == "W":
                lo, hi = q_min * t_lo, q_max * t_hi
            else:
                lo, hi = q_min * (1 - t_hi), q_max * (1 - t_lo)
            centers.append((lo + hi) / 2)
            continue

        boundary = candidate.get("boundary")
        if boundary in {"mu_zero", "mu_one"}:
            centers.append(Fraction(0))
            continue
        if boundary in {"kappa_zero", "kappa_infinity"}:
            record = boundaries.get(boundary)
            if not isinstance(record, Mapping):
                return None
            mean = record.get("profile_mean")
            if not isinstance(mean, Fraction):
                return None
            q = mean * (1 - mean)
            if component == "W":
                centers.append(q if boundary == "kappa_infinity" else Fraction(0))
            else:
                centers.append(q if boundary == "kappa_zero" else Fraction(0))
            continue
        return None

    if not centers:
        return None
    return tuple(sorted(set(
        min(Fraction(1, 4), max(Fraction(0), value))
        for value in centers
    )))


def f5_component_profile_confidence_set(
    r: int, count_histogram: Mapping[int, int], *,
    component: str, likelihood_ratio_cutoff,
    global_certificate: Mapping[str, object] | None = None,
    scan_grid_points: int = 17,
    max_bisection_steps: int = 6,
    root_isolation_width: Fraction = Fraction(1, 2**64),
    max_depth: int = 180,
    max_intervals: int = 10000,
    max_fraction_bits: int = 200000,
    log_series_terms: int = 100,
) -> dict[str, object]:
    """Numerically invert the exact fixed-target LR enclosure on [0,1/4].

    All detected connected components are retained and crossings are
    conservatively bracketed. The scan is not a proof of global topology;
    nested-grid convergence is mandatory before method selection.
    """
    if component not in {"W", "B"}:
        raise F5ConstrainedScoreError("COMPONENT_MUST_BE_W_OR_B")
    if type(scan_grid_points) is not int or scan_grid_points < 5:
        raise F5ConstrainedScoreError("SCAN_GRID_POINTS_MUST_BE_INTEGER_GE_5")
    if (
        isinstance(likelihood_ratio_cutoff, bool)
        or not isinstance(likelihood_ratio_cutoff, (int, float, Fraction))
        or (
            isinstance(likelihood_ratio_cutoff, float)
            and not math.isfinite(likelihood_ratio_cutoff)
        )
    ):
        raise F5ConstrainedScoreError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")
    cutoff = (
        likelihood_ratio_cutoff
        if isinstance(likelihood_ratio_cutoff, Fraction)
        else Fraction.from_float(float(likelihood_ratio_cutoff))
        if isinstance(likelihood_ratio_cutoff, float)
        else Fraction(likelihood_ratio_cutoff)
    )
    if cutoff <= 0:
        raise F5ConstrainedScoreError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")

    if global_certificate is None:
        global_certificate = beta_binomial_global_mle_certificate(
            r, count_histogram,
        )
    centers = _global_mle_functional_centers(global_certificate, component)
    if centers is None:
        return {
            "status": "GLOBAL_MLE_FUNCTIONAL_CENTER_UNRESOLVED",
            "global_mle_status": global_certificate.get("status"),
            "topology_certified": False,
        }
    uniform = tuple(
        Fraction(index, 4 * (scan_grid_points - 1))
        for index in range(scan_grid_points)
    )
    nodes = tuple(sorted(set(uniform + centers)))

    def evaluate(target_value: Fraction):
        return f5_component_profile_lr_statistic(
            r, count_histogram, component=component, target=target_value,
            global_certificate=global_certificate,
            root_isolation_width=root_isolation_width,
            max_depth=max_depth, max_intervals=max_intervals,
            max_fraction_bits=max_fraction_bits,
            log_series_terms=log_series_terms,
        )

    scan = _scan_profile_lr_grid(
        nodes, cutoff=cutoff, evaluate=evaluate,
        max_bisection_steps=max_bisection_steps,
    )
    return {
        **scan,
        "component": component,
        "likelihood_ratio_cutoff": cutoff,
        "global_mle_status": global_certificate.get("status"),
        "global_mle_functional_centers": centers,
        "scan_grid_points": scan_grid_points,
        "root_isolation_width": root_isolation_width,
        "method_status": "NUMERICAL_PROFILE_LR_INVERSION_CANDIDATE",
    }
