"""Exact sparse integer numerators for the F5 beta-binomial score equations.

Research-only deterministic algebra primitive. No floating-point coefficients,
symbolic simplification, or scientific data generation is used.
Polynomial representation: {(degree_mu, degree_kappa): integer coefficient}.
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping


Poly = dict[tuple[int, int], int]


def _exact_fraction(value):
    """Convert only integers/Fractions; reject binary floats at the boundary."""
    from fractions import Fraction

    if type(value) is int or type(value) is Fraction:
        return Fraction(value)
    raise ValueError("EXACT_RATIONAL_REQUIRED")


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

    def rational_pair(bounds, code):
        if not isinstance(bounds, tuple) or len(bounds) != 2:
            raise ValueError(code)
        try:
            lo, hi = (_exact_fraction(bounds[0]), _exact_fraction(bounds[1]))
        except ValueError:
            raise ValueError(code) from None
        if lo >= hi:
            raise ValueError(code)
        return lo, hi

    mu_lo, mu_hi = rational_pair(mu_bounds, "INVALID_MU_BOUNDS")
    t_lo, t_hi = rational_pair(t_bounds, "INVALID_T_BOUNDS")
    if not poly:
        return [[Fraction(0)]]
    if any(
        type(i) is not int or i < 0 or type(j) is not int or j < 0
        or type(coefficient) is not int
        for (i, j), coefficient in poly.items()
    ):
        raise ValueError("POLYNOMIAL_MUST_HAVE_NONNEGATIVE_INTEGER_MONOMIALS")
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
    if not isinstance(coefficients, list) or not coefficients:
        raise ValueError("NONEMPTY_RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    if any(not isinstance(row, list) or not row for row in coefficients):
        raise ValueError("NONEMPTY_RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    width = len(coefficients[0])
    if any(len(row) != width for row in coefficients):
        raise ValueError("RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED")
    flat = [_exact_fraction(value) for row in coefficients for value in row]
    return all(value > 0 for value in flat) or all(value < 0 for value in flat)



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
    matrix = [[_exact_fraction(value) for value in row] for row in coefficients]

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
    if not isinstance(mu_bounds, tuple) or len(mu_bounds) != 2:
        raise ValueError("INVALID_INITIAL_BOX")
    if not isinstance(t_bounds, tuple) or len(t_bounds) != 2:
        raise ValueError("INVALID_INITIAL_BOX")
    try:
        mu_lo, mu_hi = (_exact_fraction(mu_bounds[0]), _exact_fraction(mu_bounds[1]))
        t_lo, t_hi = (_exact_fraction(t_bounds[0]), _exact_fraction(t_bounds[1]))
    except ValueError:
        raise ValueError("INVALID_INITIAL_BOX") from None
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

def _poly_derivative(poly: Poly, axis: int) -> Poly:
    if axis not in (0, 1):
        raise ValueError("DERIVATIVE_AXIS_MUST_BE_ZERO_OR_ONE")
    return {
        (i - 1, j) if axis == 0 else (i, j - 1): coefficient * (i if axis == 0 else j)
        for (i, j), coefficient in poly.items()
        if (i if axis == 0 else j) > 0
    }


def _poly_evaluate_rational(poly: Poly, mu, t):
    from fractions import Fraction

    mu = _exact_fraction(mu)
    t = _exact_fraction(t)
    return sum(
        Fraction(coefficient) * mu**i * t**j
        for (i, j), coefficient in poly.items()
    )


def _interval_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def _interval_neg(a):
    return (-a[1], -a[0])


def _interval_sub(a, b):
    return _interval_add(a, _interval_neg(b))


def _interval_mul(a, b):
    products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (min(products), max(products))


def _interval_scale(scalar, interval):
    return _interval_mul((scalar, scalar), interval)


def _interval_abs_upper(interval):
    return max(abs(interval[0]), abs(interval[1]))


def _bernstein_range(poly: Poly, mu_bounds, t_bounds):
    coefficients = bernstein_coefficients_on_box(poly, mu_bounds, t_bounds)
    flat = [value for row in coefficients for value in row]
    return (min(flat), max(flat))


def krawczyk_certify_unique_root(
    poly_p: Poly,
    poly_q: Poly,
    *,
    mu_bounds: tuple[object, object],
    t_bounds: tuple[object, object],
) -> dict[str, object]:
    """Attempt a rigorous simple-root certificate on one rational rectangle.

    All calculations use Fraction arithmetic. The Jacobian enclosure is
    obtained from tensor-product Bernstein convex-hull bounds for the exact
    derivative polynomials. A rational point preconditioner C is the inverse
    of the Jacobian at the box midpoint. Certification requires C nonsingular,
    strict Krawczyk inclusion in the interior of the box, and a strict
    infinity-norm contraction bound for I-C*J(X).

    This certifies exactly one common zero in the box when successful. It is
    not a multiple-root method; singular or inconclusive boxes are UNRESOLVED.
    """
    from fractions import Fraction

    if not isinstance(mu_bounds, tuple) or len(mu_bounds) != 2:
        raise ValueError("INVALID_MU_BOUNDS")
    if not isinstance(t_bounds, tuple) or len(t_bounds) != 2:
        raise ValueError("INVALID_T_BOUNDS")
    try:
        mu_lo, mu_hi = (_exact_fraction(v) for v in mu_bounds)
        t_lo, t_hi = (_exact_fraction(v) for v in t_bounds)
    except ValueError:
        raise ValueError("EXACT_RATIONAL_BOUNDS_REQUIRED") from None
    if mu_lo >= mu_hi or t_lo >= t_hi:
        raise ValueError("INVALID_CERTIFICATION_BOX")
    for poly in (poly_p, poly_q):
        if not isinstance(poly, Mapping) or any(
            type(i) is not int or i < 0 or type(j) is not int or j < 0
            or type(c) is not int
            for (i, j), c in poly.items()
        ):
            raise ValueError("INTEGER_SPARSE_POLYNOMIALS_REQUIRED")

    x0 = ((mu_lo + mu_hi) / 2, (t_lo + t_hi) / 2)
    f0 = (
        _poly_evaluate_rational(poly_p, *x0),
        _poly_evaluate_rational(poly_q, *x0),
    )
    derivatives = (
        (_poly_derivative(poly_p, 0), _poly_derivative(poly_p, 1)),
        (_poly_derivative(poly_q, 0), _poly_derivative(poly_q, 1)),
    )
    j0 = tuple(tuple(
        _poly_evaluate_rational(derivatives[row][col], *x0)
        for col in range(2)
    ) for row in range(2))
    determinant = j0[0][0] * j0[1][1] - j0[0][1] * j0[1][0]
    if determinant == 0:
        return {
            "status": "UNRESOLVED_SINGULAR_MIDPOINT_JACOBIAN",
            "box": (mu_bounds, t_bounds),
            "reason": "MIDPOINT_JACOBIAN_NOT_INVERTIBLE",
        }

    # C = inverse(J(x0)); exact rational preconditioner.
    c = (
        (j0[1][1] / determinant, -j0[0][1] / determinant),
        (-j0[1][0] / determinant, j0[0][0] / determinant),
    )
    j_box = tuple(tuple(
        _bernstein_range(derivatives[row][col], (mu_lo, mu_hi), (t_lo, t_hi))
        for col in range(2)
    ) for row in range(2))

    # B = I - C*J(X), using outward-exact interval operations.
    b = []
    for row in range(2):
        b_row = []
        for col in range(2):
            total = (Fraction(0), Fraction(0))
            for k in range(2):
                total = _interval_add(
                    total,
                    _interval_scale(c[row][k], j_box[k][col]),
                )
            identity = (Fraction(1), Fraction(1)) if row == col else (Fraction(0), Fraction(0))
            b_row.append(_interval_sub(identity, total))
        b.append(tuple(b_row))

    delta = (
        (mu_lo - x0[0], mu_hi - x0[0]),
        (t_lo - x0[1], t_hi - x0[1]),
    )
    k_box = []
    for row in range(2):
        center = x0[row] - sum(c[row][k] * f0[k] for k in range(2))
        correction = (Fraction(0), Fraction(0))
        for col in range(2):
            correction = _interval_add(
                correction, _interval_mul(b[row][col], delta[col])
            )
        k_box.append(_interval_add((center, center), correction))

    contraction = max(
        sum(_interval_abs_upper(b[row][col]) for col in range(2))
        for row in range(2)
    )
    strict_inclusion = (
        mu_lo < k_box[0][0] and k_box[0][1] < mu_hi
        and t_lo < k_box[1][0] and k_box[1][1] < t_hi
    )
    if strict_inclusion and contraction < 1:
        return {
            "status": "CERTIFIED_UNIQUE_ROOT",
            "box": ((mu_lo, mu_hi), (t_lo, t_hi)),
            "krawczyk_box": tuple(k_box),
            "contraction_bound": contraction,
            "preconditioner": c,
            "jacobian_interval": j_box,
        }
    return {
        "status": "UNRESOLVED",
        "box": ((mu_lo, mu_hi), (t_lo, t_hi)),
        "krawczyk_box": tuple(k_box),
        "contraction_bound": contraction,
        "strict_inclusion": strict_inclusion,
        "reason": "INCLUSION_OR_CONTRACTION_NOT_PROVED",
    }

def bernstein_krawczyk_root_classification(
    poly_p: Poly,
    poly_q: Poly,
    *,
    mu_bounds: tuple[object, object] = (0, 1),
    t_bounds: tuple[object, object] = (0, 1),
    max_boxes: int = 10000,
    max_depth: int = 32,
) -> dict[str, object]:
    """Adaptively combine exact Bernstein exclusion and Krawczyk inclusion.

    A deterministic breadth-first queue processes each rational closed box:
    Bernstein may exclude it; otherwise Krawczyk may certify one simple root;
    otherwise the box is bisected until max_depth or max_boxes. Every
    unclassified leaf and every unprocessed resource remainder is retained.
    Shared-boundary roots and multiple roots are deliberately not promoted
    to certified roots. This is not an exhaustive global MLE certificate.
    """
    from collections import deque
    from fractions import Fraction

    if type(max_boxes) is not int or max_boxes < 1:
        raise ValueError("MAX_BOXES_MUST_BE_POSITIVE_INTEGER")
    if type(max_depth) is not int or max_depth < 0:
        raise ValueError("MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER")
    if not isinstance(mu_bounds, tuple) or len(mu_bounds) != 2:
        raise ValueError("INVALID_INITIAL_BOX")
    if not isinstance(t_bounds, tuple) or len(t_bounds) != 2:
        raise ValueError("INVALID_INITIAL_BOX")
    try:
        mu_lo, mu_hi = (_exact_fraction(v) for v in mu_bounds)
        t_lo, t_hi = (_exact_fraction(v) for v in t_bounds)
    except ValueError:
        raise ValueError("INVALID_INITIAL_BOX") from None
    if mu_lo >= mu_hi or t_lo >= t_hi:
        raise ValueError("INVALID_INITIAL_BOX")

    queue = deque([(mu_lo, mu_hi, t_lo, t_hi, 0)])
    excluded = []
    certified = []
    unresolved = []
    processed = 0
    krawczyk_attempts = 0
    subdivisions = 0

    while queue and processed < max_boxes:
        mu_a, mu_b, t_a, t_b, depth = queue.popleft()
        processed += 1
        p_coeff = bernstein_coefficients_on_box(
            poly_p, (mu_a, mu_b), (t_a, t_b)
        )
        q_coeff = bernstein_coefficients_on_box(
            poly_q, (mu_a, mu_b), (t_a, t_b)
        )
        if (
            bernstein_box_excludes_zero(p_coeff)
            or bernstein_box_excludes_zero(q_coeff)
        ):
            excluded.append({
                "mu_bounds": (mu_a, mu_b),
                "t_bounds": (t_a, t_b),
                "depth": depth,
            })
            continue

        krawczyk_attempts += 1
        result = krawczyk_certify_unique_root(
            poly_p, poly_q,
            mu_bounds=(mu_a, mu_b),
            t_bounds=(t_a, t_b),
        )
        if result["status"] == "CERTIFIED_UNIQUE_ROOT":
            certified.append({
                **result,
                "depth": depth,
            })
            continue

        if depth >= max_depth:
            unresolved.append({
                "mu_bounds": (mu_a, mu_b),
                "t_bounds": (t_a, t_b),
                "depth": depth,
                "state": "UNRESOLVED_AT_MAX_DEPTH",
                "certificate_attempt": result,
            })
            continue

        axis = "mu" if depth % 2 == 0 else "t"
        if axis == "mu":
            midpoint = (mu_a + mu_b) / 2
            queue.append((mu_a, midpoint, t_a, t_b, depth + 1))
            queue.append((midpoint, mu_b, t_a, t_b, depth + 1))
        else:
            midpoint = (t_a + t_b) / 2
            queue.append((mu_a, mu_b, t_a, midpoint, depth + 1))
            queue.append((mu_a, mu_b, midpoint, t_b, depth + 1))
        subdivisions += 1

    while queue:
        mu_a, mu_b, t_a, t_b, depth = queue.popleft()
        unresolved.append({
            "mu_bounds": (mu_a, mu_b),
            "t_bounds": (t_a, t_b),
            "depth": depth,
            "state": "NOT_PROCESSED_RESOURCE_LIMIT",
        })

    if unresolved:
        status = (
            "RESOURCE_LIMIT_WITH_REMAINDER"
            if any(x["state"] == "NOT_PROCESSED_RESOURCE_LIMIT" for x in unresolved)
            else "PARTIAL_CERTIFICATION_WITH_REMAINDER"
        )
    elif certified:
        status = "ALL_SURVIVING_BOXES_CERTIFIED_SIMPLE_ROOTS"
    else:
        status = "ALL_BOXES_EXCLUDED"

    return {
        "status": status,
        "excluded_boxes": excluded,
        "certified_root_boxes": certified,
        "unresolved_boxes": unresolved,
        "processed_boxes": processed,
        "krawczyk_attempts": krawczyk_attempts,
        "subdivisions": subdivisions,
        "max_boxes": max_boxes,
        "max_depth": max_depth,
    }


def beta_binomial_boundary_likelihoods(
    r: int,
    count_histogram: Mapping[int, int],
) -> dict[str, object]:
    """Return exact profiled likelihood values on the four open-domain edges.

    Values are exact probabilities (Fractions), including binomial
    combinatorial factors, for independent worlds represented by a histogram.
    They are boundary suprema/limits, not finite-parameter interior MLEs.
    Corner/path limits where two boundary coordinates diverge together are
    deliberately not inferred from these one-edge profiles.
    """
    from fractions import Fraction
    from math import comb

    if type(r) is not int or r < 1:
        raise ValueError("R_MUST_BE_POSITIVE_INTEGER")
    if not isinstance(count_histogram, Mapping) or not count_histogram:
        raise ValueError("NONEMPTY_COUNT_HISTOGRAM_REQUIRED")
    hist = {}
    for x, n in count_histogram.items():
        if type(x) is not int or not 0 <= x <= r:
            raise ValueError("COUNT_OUTSIDE_0_TO_R")
        if type(n) is not int or n < 0:
            raise ValueError("MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER")
        if n:
            hist[x] = hist.get(x, 0) + n
    total = sum(hist.values())
    if total == 0:
        raise ValueError("POSITIVE_TOTAL_MULTIPLICITY_REQUIRED")

    pooled_successes = sum(x * n for x, n in hist.items())
    mu_inf = Fraction(pooled_successes, total * r)
    binomial_limit = Fraction(1)
    for x, n in hist.items():
        probability = (
            Fraction(comb(r, x))
            * mu_inf**x
            * (1 - mu_inf) ** (r - x)
        )
        binomial_limit *= probability**n

    n_zero = hist.get(0, 0)
    n_r = hist.get(r, 0)
    n_interior = total - n_zero - n_r
    endpoint_total = n_zero + n_r
    if n_interior:
        mu_zero_concentration = None
        zero_concentration_likelihood = Fraction(0)
        zero_concentration_status = "ZERO_LIMIT_LIKELIHOOD"
    elif endpoint_total:
        mu_zero_concentration = Fraction(n_r, endpoint_total)
        zero_concentration_likelihood = (
            (1 - mu_zero_concentration) ** n_zero
            * mu_zero_concentration**n_r
        )
        zero_concentration_status = "PROFILED_ENDPOINT_MIXTURE_LIMIT"
    else:
        mu_zero_concentration = None
        zero_concentration_likelihood = Fraction(0)
        zero_concentration_status = "ZERO_LIMIT_LIKELIHOOD"

    mu_zero_likelihood = Fraction(1) if all(x == 0 for x in hist) else Fraction(0)
    mu_one_likelihood = Fraction(1) if all(x == r for x in hist) else Fraction(0)

    return {
        "status": "EXACT_ONE_EDGE_BOUNDARY_LIMITS",
        "kappa_infinity": {
            "status": "BINOMIAL_LIMIT",
            "profile_mean": mu_inf,
            "likelihood": binomial_limit,
        },
        "kappa_zero": {
            "status": zero_concentration_status,
            "profile_mean": mu_zero_concentration,
            "likelihood": zero_concentration_likelihood,
            "zero_count_worlds": n_zero,
            "endpoint_count_worlds": n_r,
            "interior_count_worlds": n_interior,
        },
        "mu_zero": {
            "status": "DEGENERATE_AT_ZERO",
            "likelihood": mu_zero_likelihood,
        },
        "mu_one": {
            "status": "DEGENERATE_AT_R",
            "likelihood": mu_one_likelihood,
        },
        "corner_path_limits": "NOT_CLASSIFIED_BY_ONE_EDGE_PROFILES",
    }

def _uni_trim(poly):
    from fractions import Fraction
    values = [Fraction(value) for value in poly]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [Fraction(0)]


def _uni_is_zero(poly):
    return len(poly) == 1 and poly[0] == 0


def _uni_monic(poly):
    from fractions import Fraction
    values = _uni_trim(poly)
    if _uni_is_zero(values):
        return values
    lead = values[-1]
    return [value / lead for value in values]


def _uni_divmod(dividend, divisor):
    from fractions import Fraction
    a = _uni_trim(dividend)
    b = _uni_trim(divisor)
    if _uni_is_zero(b):
        raise ZeroDivisionError("UNIVARIATE_ZERO_DIVISOR")
    if len(a) < len(b):
        return [Fraction(0)], a
    quotient = [Fraction(0)] * (len(a) - len(b) + 1)
    remainder = list(a)
    while not _uni_is_zero(remainder) and len(remainder) >= len(b):
        degree = len(remainder) - len(b)
        coefficient = remainder[-1] / b[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(b):
            remainder[degree + index] -= coefficient * value
        remainder = _uni_trim(remainder)
    return _uni_trim(quotient), _uni_trim(remainder)


def _uni_gcd(left, right):
    a = _uni_trim(left)
    b = _uni_trim(right)
    while not _uni_is_zero(b):
        _, remainder = _uni_divmod(a, b)
        a, b = b, remainder
    return _uni_monic(a)


def _uni_derivative(poly):
    from fractions import Fraction
    values = _uni_trim(poly)
    if len(values) <= 1:
        return [Fraction(0)]
    return _uni_trim([index * values[index] for index in range(1, len(values))])


def _uni_squarefree_factors(poly):
    """Return monic square-free factors paired with exact multiplicities."""
    from fractions import Fraction
    f = _uni_monic(poly)
    if _uni_is_zero(f):
        raise ValueError("ZERO_POLYNOMIAL_HAS_NO_FINITE_SQUAREFREE_DECOMPOSITION")
    if len(f) <= 1:
        return []
    c = _uni_gcd(f, _uni_derivative(f))
    w, remainder = _uni_divmod(f, c)
    if not _uni_is_zero(remainder):
        raise ArithmeticError("SQUAREFREE_INITIAL_DIVISION_FAILED")
    multiplicity = 1
    factors = []
    while len(w) > 1:
        y = _uni_gcd(w, c)
        factor, remainder = _uni_divmod(w, y)
        if not _uni_is_zero(remainder):
            raise ArithmeticError("SQUAREFREE_FACTOR_DIVISION_FAILED")
        if len(factor) > 1:
            factors.append({
                "multiplicity": multiplicity,
                "coefficients": tuple(_uni_monic(factor)),
            })
        w = y
        c, remainder = _uni_divmod(c, y)
        if not _uni_is_zero(remainder):
            raise ArithmeticError("SQUAREFREE_GCD_DIVISION_FAILED")
        multiplicity += 1
    if len(c) > 1:
        raise ArithmeticError("SQUAREFREE_DECOMPOSITION_INCOMPLETE")
    return factors


def _edge_restriction(poly, edge):
    from fractions import Fraction
    if edge in ("mu_zero", "mu_one"):
        fixed_mu = Fraction(0 if edge == "mu_zero" else 1)
        degree = max((j for _, j in poly), default=0)
        result = [Fraction(0)] * (degree + 1)
        for (i, j), coefficient in poly.items():
            result[j] += Fraction(coefficient) * fixed_mu**i
        return _uni_trim(result)
    if edge in ("t_zero", "t_one"):
        fixed_t = Fraction(0 if edge == "t_zero" else 1)
        degree = max((i for i, _ in poly), default=0)
        result = [Fraction(0)] * (degree + 1)
        for (i, j), coefficient in poly.items():
            result[i] += Fraction(coefficient) * fixed_t**j
        return _uni_trim(result)
    raise ValueError("UNKNOWN_COMPACTIFIED_EDGE")


def compactified_boundary_common_factors(
    poly_p: Poly,
    poly_q: Poly,
) -> dict[str, object]:
    """Find exact common score factors on each edge of [0,1]^2.

    Edge parameter is t on mu=0/1 and mu on t=0/1. The polynomial gcd
    preserves the minimum common-root multiplicity; square-free factorization
    reports each factor with that multiplicity. An edge on which both
    restrictions vanish identically is reported as a common component and
    remains unresolved rather than being misreported as finitely many roots.
    """
    from collections.abc import Mapping
    from fractions import Fraction

    for poly in (poly_p, poly_q):
        if not isinstance(poly, Mapping) or any(
            not isinstance(monomial, tuple) or len(monomial) != 2
            or type(i) is not int or i < 0
            or type(j) is not int or j < 0
            or type(coefficient) is not int
            for monomial, coefficient in poly.items()
            for i, j in (monomial,)
        ):
            raise ValueError("INTEGER_SPARSE_POLYNOMIALS_REQUIRED")

    output = {}
    for edge in ("mu_zero", "mu_one", "t_zero", "t_one"):
        p_edge = _edge_restriction(poly_p, edge)
        q_edge = _edge_restriction(poly_q, edge)
        if _uni_is_zero(p_edge) and _uni_is_zero(q_edge):
            output[edge] = {
                "status": "COMMON_EDGE_COMPONENT_UNRESOLVED",
                "p_coefficients": tuple(p_edge),
                "q_coefficients": tuple(q_edge),
                "common_gcd": None,
                "squarefree_factors": [],
            }
            continue
        common = _uni_gcd(p_edge, q_edge)
        factors = _uni_squarefree_factors(common)
        output[edge] = {
            "status": "FINITE_COMMON_EDGE_ROOTS" if factors else "NO_COMMON_EDGE_ROOT",
            "p_coefficients": tuple(p_edge),
            "q_coefficients": tuple(q_edge),
            "common_gcd": tuple(common),
            "squarefree_factors": factors,
        }
    return {
        "status": (
            "BOUNDARY_COMMON_COMPONENTS_UNRESOLVED"
            if any(v["status"] == "COMMON_EDGE_COMPONENT_UNRESOLVED" for v in output.values())
            else "BOUNDARY_COMMON_FACTORS_CLASSIFIED"
        ),
        "edges": output,
        "root_isolation": "NOT_YET_PERFORMED",
    }

