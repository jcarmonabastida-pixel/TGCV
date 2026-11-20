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


def compactify_concentration(poly: Poly) -> Poly:
    """Map kappa in (0,+inf) to t=kappa/(1+kappa) in (0,1).

    Returns (1-t)^d * P(mu, t/(1-t)), where d is the maximum kappa
    degree in P. This is an exact integer polynomial transformation and
    preserves the zero set for 0<t<1. The endpoints t=0 and t=1 represent
    kappa->0 and kappa->infinity and must be adjudicated separately; roots
    there are not interior stationary points.
    """
    from math import comb

    if not poly:
        return {}
    if any(
        type(i) is not int or i < 0 or type(j) is not int or j < 0
        or type(coefficient) is not int
        for (i, j), coefficient in poly.items()
    ):
        raise ValueError("POLYNOMIAL_MUST_HAVE_NONNEGATIVE_INTEGER_MONOMIALS")
    degree_kappa = max(j for _, j in poly)
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (degree_mu, degree_kappa_term), coefficient in poly.items():
        remaining = degree_kappa - degree_kappa_term
        for power in range(remaining + 1):
            out[(degree_mu, degree_kappa_term + power)] += (
                coefficient * comb(remaining, power)
                * (-1 if power % 2 else 1)
            )
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def bernstein_coefficients_on_box(
    poly: Poly,
    mu_bounds: tuple[object, object] = (0, 1),
    t_bounds: tuple[object, object] = (0, 1),
) -> list[list[object]]:
    """Return exact tensor-product Bernstein coefficients on a rational box.

    The input is a sparse power-basis polynomial in (mu,t). Bounds must be
    ordered rational values (int or Fraction). The returned matrix has shape
    (degree_mu+1) x (degree_t+1). Its convex-hull property encloses the
    polynomial range on the closed box. Consequently, coefficients all
    strictly positive or all strictly negative certify that the polynomial
    has no zero anywhere in that box.

    This is a root-exclusion primitive only. Mixed-sign coefficients do not
    prove that a root exists, and this function does not certify a root of a
    two-polynomial system or handle open-domain boundary likelihoods.
    """
    from fractions import Fraction
    from math import comb

    if not poly:
        return [[Fraction(0)]]
    if any(
        type(i) is not int or i < 0 or type(j) is not int or j < 0
        or type(coefficient) is not int
        for (i, j), coefficient in poly.items()
    ):
        raise ValueError("POLYNOMIAL_MUST_HAVE_NONNEGATIVE_INTEGER_MONOMIALS")

    def rational_pair(bounds, code):
        if not isinstance(bounds, tuple) or len(bounds) != 2:
            raise ValueError(code)
        try:
            lo, hi = Fraction(bounds[0]), Fraction(bounds[1])
        except (TypeError, ValueError, ZeroDivisionError):
            raise ValueError(code) from None
        if lo >= hi:
            raise ValueError(code)
        return lo, hi

    mu_lo, mu_hi = rational_pair(mu_bounds, "INVALID_MU_BOUNDS")
    t_lo, t_hi = rational_pair(t_bounds, "INVALID_T_BOUNDS")
    degree_mu = max(i for i, _ in poly)
    degree_t = max(j for _, j in poly)

    # First substitute mu=mu_lo+(mu_hi-mu_lo)u and
    # t=t_lo+(t_hi-t_lo)v into the power basis.
    power: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (i, j), coefficient in poly.items():
        for a in range(i + 1):
            ca = Fraction(comb(i, a)) * mu_lo ** (i - a) * (mu_hi - mu_lo) ** a
            for b in range(j + 1):
                cb = Fraction(comb(j, b)) * t_lo ** (j - b) * (t_hi - t_lo) ** b
                power[(a, b)] += coefficient * ca * cb

    # Convert power coefficients to tensor-product Bernstein coefficients.
    result = []
    for k in range(degree_mu + 1):
        row = []
        for ell in range(degree_t + 1):
            value = Fraction(0)
            for i in range(k + 1):
                for j in range(ell + 1):
                    coefficient = power.get((i, j), Fraction(0))
                    if coefficient:
                        value += (
                            coefficient
                            * Fraction(comb(k, i), comb(degree_mu, i))
                            * Fraction(comb(ell, j), comb(degree_t, j))
                        )
            row.append(value)
        result.append(row)
    return result


def bernstein_sign_excludes_zero(coefficients: list[list[object]]) -> bool:
    """Return True only when exact Bernstein coefficients exclude zero."""
    from fractions import Fraction

    flat = [Fraction(value) for row in coefficients for value in row]
    return bool(flat) and (all(value > 0 for value in flat) or all(value < 0 for value in flat))



def bernstein_subdivide(
    coefficients: list[list[object]], axis: str
) -> tuple[list[list[object]], list[list[object]]]:
    """Split an exact tensor-product Bernstein coefficient matrix at its midpoint.

    The input matrix uses rows for the mu degree and columns for the t degree,
    matching bernstein_coefficients_on_box(). The split is performed by the
    de Casteljau algorithm using Fraction arithmetic only. The two returned
    matrices represent the lower/left and upper/right half along the selected
    axis. No polynomial is approximated and no floating-point operation occurs.
    """
    from fractions import Fraction

    if axis not in ("mu", "t"):
        raise ValueError("AXIS_MUST_BE_MU_OR_T")
    if not isinstance(coefficients, list) or not coefficients:
        raise ValueError("NONEMPTY_RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    if any(not isinstance(row, list) or not row for row in coefficients):
        raise ValueError("NONEMPTY_RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    width = len(coefficients[0])
    if any(len(row) != width for row in coefficients):
        raise ValueError("RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    matrix = [[Fraction(value) for value in row] for row in coefficients]

    def split_line(values):
        levels = [values]
        while len(levels[-1]) > 1:
            previous = levels[-1]
            levels.append([
                (previous[i] + previous[i + 1]) / 2
                for i in range(len(previous) - 1)
            ])
        degree = len(values) - 1
        left = [levels[k][0] for k in range(degree + 1)]
        right = [levels[degree - k][k] for k in range(degree + 1)]
        return left, right

    if axis == "mu":
        left_columns = []
        right_columns = []
        for j in range(width):
            left, right = split_line([matrix[i][j] for i in range(len(matrix))])
            left_columns.append(left)
            right_columns.append(right)
        left_matrix = [
            [left_columns[j][i] for j in range(width)]
            for i in range(len(matrix))
        ]
        right_matrix = [
            [right_columns[j][i] for j in range(width)]
            for i in range(len(matrix))
        ]
        return left_matrix, right_matrix

    left_rows = []
    right_rows = []
    for row in matrix:
        left, right = split_line(row)
        left_rows.append(left)
        right_rows.append(right)
    return left_rows, right_rows


def bernstein_box_excludes_zero(coefficients: list[list[object]]) -> bool:
    """Named box-level predicate; mixed signs and zero coefficients are inconclusive."""
    return bernstein_sign_excludes_zero(coefficients)



def bernstein_exclusion_subdivision(
    poly_p: Poly,
    poly_q: Poly,
    *,
    mu_bounds: tuple[object, object] = (0, 1),
    t_bounds: tuple[object, object] = (0, 1),
    max_boxes: int = 10000,
    max_depth: int = 32,
) -> dict[str, object]:
    """Deterministically subdivide a rational box cover using Bernstein exclusion.

    This controller proves absence of common zeros only when every processed
    leaf is excluded by at least one score polynomial. It does not certify
    existence or uniqueness of roots. Boxes reaching max_depth are retained
    as unresolved; boxes left in the FIFO queue at max_boxes are returned as
    an unprocessed remainder. Axis selection alternates mu,t by depth.
    """
    from collections import deque
    from fractions import Fraction

    if type(max_boxes) is not int or max_boxes < 1:
        raise ValueError("MAX_BOXES_MUST_BE_POSITIVE_INTEGER")
    if type(max_depth) is not int or max_depth < 0:
        raise ValueError("MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER")
    mu_lo, mu_hi = Fraction(mu_bounds[0]), Fraction(mu_bounds[1])
    t_lo, t_hi = Fraction(t_bounds[0]), Fraction(t_bounds[1])
    if mu_lo >= mu_hi or t_lo >= t_hi:
        raise ValueError("INVALID_INITIAL_BOX")

    p0 = bernstein_coefficients_on_box(
        poly_p, (mu_lo, mu_hi), (t_lo, t_hi)
    )
    q0 = bernstein_coefficients_on_box(
        poly_q, (mu_lo, mu_hi), (t_lo, t_hi)
    )
    queue = deque([(
        mu_lo, mu_hi, t_lo, t_hi, 0, p0, q0
    )])
    excluded = 0
    processed = 0
    unresolved: list[dict[str, object]] = []

    while queue and processed < max_boxes:
        mu_a, mu_b, t_a, t_b, depth, p_coeff, q_coeff = queue.popleft()
        processed += 1
        if (
            bernstein_box_excludes_zero(p_coeff)
            or bernstein_box_excludes_zero(q_coeff)
        ):
            excluded += 1
            continue
        if depth >= max_depth:
            unresolved.append({
                "mu_bounds": (mu_a, mu_b),
                "t_bounds": (t_a, t_b),
                "depth": depth,
                "state": "UNRESOLVED_AT_MAX_DEPTH",
            })
            continue

        axis = "mu" if depth % 2 == 0 else "t"
        if axis == "mu":
            midpoint = (mu_a + mu_b) / 2
            p_left, p_right = bernstein_subdivide(p_coeff, "mu")
            q_left, q_right = bernstein_subdivide(q_coeff, "mu")
            queue.append((mu_a, midpoint, t_a, t_b, depth + 1, p_left, q_left))
            queue.append((midpoint, mu_b, t_a, t_b, depth + 1, p_right, q_right))
        else:
            midpoint = (t_a + t_b) / 2
            p_left, p_right = bernstein_subdivide(p_coeff, "t")
            q_left, q_right = bernstein_subdivide(q_coeff, "t")
            queue.append((mu_a, mu_b, t_a, midpoint, depth + 1, p_left, q_left))
            queue.append((mu_a, mu_b, midpoint, t_b, depth + 1, p_right, q_right))

    while queue:
        mu_a, mu_b, t_a, t_b, depth, _, _ = queue.popleft()
        unresolved.append({
            "mu_bounds": (mu_a, mu_b),
            "t_bounds": (t_a, t_b),
            "depth": depth,
            "state": "NOT_PROCESSED_RESOURCE_LIMIT",
        })

    if not unresolved:
        status = "ALL_BOXES_EXCLUDED"
    elif any(item["state"] == "NOT_PROCESSED_RESOURCE_LIMIT" for item in unresolved):
        status = "RESOURCE_LIMIT_WITH_REMAINDER"
    else:
        status = "UNRESOLVED_BOXES"
    return {
        "status": status,
        "processed_boxes": processed,
        "excluded_boxes": excluded,
        "unresolved_boxes": unresolved,
        "max_boxes": max_boxes,
        "max_depth": max_depth,
    }
