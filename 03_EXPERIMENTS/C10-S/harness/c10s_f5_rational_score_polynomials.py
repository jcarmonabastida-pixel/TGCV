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

    # Convert the sparse power basis to a dense coefficient matrix once.
    # Then apply the two univariate power-to-Bernstein transforms separately.
    # This reduces exact arithmetic from O(d_mu^2*d_t^2) to
    # O(d_mu^2*d_t + d_mu*d_t^2), which matters for M30/R20 degrees.
    power = [
        [Fraction(0) for _ in range(degree_t + 1)]
        for _ in range(degree_mu + 1)
    ]
    for (i, j), coefficient in poly.items():
        power[i][j] += Fraction(coefficient)

    def monomial_bernstein_basis(degree, lower, upper):
        width = upper - lower
        basis = [
            [Fraction(0) for _ in range(degree + 1)]
            for _ in range(degree + 1)
        ]
        for monomial_degree in range(degree + 1):
            for bernstein_index in range(degree + 1):
                value = Fraction(0)
                for normalized_degree in range(min(monomial_degree, bernstein_index) + 1):
                    value += (
                        Fraction(comb(monomial_degree, normalized_degree))
                        * lower ** (monomial_degree - normalized_degree)
                        * width ** normalized_degree
                        * Fraction(
                            comb(bernstein_index, normalized_degree),
                            comb(degree, normalized_degree),
                        )
                    )
                basis[monomial_degree][bernstein_index] = value
        return basis

    mu_basis = monomial_bernstein_basis(degree_mu, mu_lo, mu_hi)
    t_basis = monomial_bernstein_basis(degree_t, t_lo, t_hi)

    # First transform the mu power axis.
    intermediate = [
        [Fraction(0) for _ in range(degree_t + 1)]
        for _ in range(degree_mu + 1)
    ]
    for k in range(degree_mu + 1):
        for j in range(degree_t + 1):
            intermediate[k][j] = sum(
                power[i][j] * mu_basis[i][k]
                for i in range(degree_mu + 1)
            )

    # Then transform the t power axis.
    result = [
        [Fraction(0) for _ in range(degree_t + 1)]
        for _ in range(degree_mu + 1)
    ]
    for k in range(degree_mu + 1):
        for ell in range(degree_t + 1):
            result[k][ell] = sum(
                intermediate[k][j] * t_basis[j][ell]
                for j in range(degree_t + 1)
            )
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
        if not isinstance(poly, Mapping):
            raise ValueError("INTEGER_SPARSE_POLYNOMIALS_REQUIRED")
        for monomial, coefficient in poly.items():
            if (
                not isinstance(monomial, tuple) or len(monomial) != 2
                or type(monomial[0]) is not int or monomial[0] < 0
                or type(monomial[1]) is not int or monomial[1] < 0
                or type(coefficient) is not int
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

def _uni_evaluate(poly, point):
    from fractions import Fraction
    x = Fraction(point)
    total = Fraction(0)
    for coefficient in reversed(_uni_trim(poly)):
        total = total * x + coefficient
    return total


def _uni_sturm_sequence(poly):
    p = _uni_monic(poly)
    if len(p) <= 1:
        return [p]
    sequence = [p, _uni_derivative(p)]
    while not _uni_is_zero(sequence[-1]):
        _, remainder = _uni_divmod(sequence[-2], sequence[-1])
        if _uni_is_zero(remainder):
            break
        sequence.append([-value for value in remainder])
    return sequence


def _uni_sign_variations(sequence, point):
    signs = []
    for poly in sequence:
        value = _uni_evaluate(poly, point)
        if value > 0:
            signs.append(1)
        elif value < 0:
            signs.append(-1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def _uni_sturm_root_count(sequence, left, right):
    if _uni_evaluate(sequence[0], left) == 0 or _uni_evaluate(sequence[0], right) == 0:
        raise ValueError("STURM_INTERVAL_ENDPOINT_IS_ROOT")
    return (
        _uni_sign_variations(sequence, left)
        - _uni_sign_variations(sequence, right)
    )


def _uni_divide_linear(poly, root):
    from fractions import Fraction
    quotient, remainder = _uni_divmod(poly, [-Fraction(root), Fraction(1)])
    if not _uni_is_zero(remainder):
        raise ArithmeticError("EXPECTED_EXACT_LINEAR_FACTOR")
    return _uni_monic(quotient)


def _uni_isolate_squarefree_unit_roots(
    poly,
    *,
    width,
    max_depth,
    max_intervals,
):
    from collections import deque
    from fractions import Fraction

    target_width = _exact_fraction(width)
    if target_width <= 0:
        raise ValueError("ISOLATION_WIDTH_MUST_BE_POSITIVE")
    if type(max_depth) is not int or max_depth < 0:
        raise ValueError("MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER")
    if type(max_intervals) is not int or max_intervals < 1:
        raise ValueError("MAX_INTERVALS_MUST_BE_POSITIVE_INTEGER")

    current = _uni_monic(poly)
    exact_roots = []
    processed = 0
    while len(current) > 1:
        if _uni_evaluate(current, Fraction(0)) == 0:
            exact_roots.append(Fraction(0))
            current = _uni_divide_linear(current, Fraction(0))
            continue
        if len(current) > 1 and _uni_evaluate(current, Fraction(1)) == 0:
            exact_roots.append(Fraction(1))
            current = _uni_divide_linear(current, Fraction(1))
            continue
        if len(current) <= 1:
            break

        sequence = _uni_sturm_sequence(current)
        total = _uni_sturm_root_count(sequence, Fraction(0), Fraction(1))
        queue = deque([(Fraction(0), Fraction(1), 0, total)])
        intervals = []
        unresolved = []
        discovered_rational_root = None

        while queue:
            left, right, depth, count = queue.popleft()
            if count == 0:
                continue
            processed += 1
            if processed > max_intervals:
                unresolved.append({
                    "interval": (left, right),
                    "root_count": count,
                    "depth": depth,
                    "state": "NOT_PROCESSED_INTERVAL_BUDGET",
                })
                unresolved.extend({
                    "interval": (a, b),
                    "root_count": n,
                    "depth": d,
                    "state": "NOT_PROCESSED_INTERVAL_BUDGET",
                } for a, b, d, n in queue if n)
                return {
                    "status": "RESOURCE_LIMIT_WITH_REMAINDER",
                    "exact_roots": tuple(sorted(exact_roots)),
                    "isolating_intervals": intervals,
                    "unresolved_intervals": unresolved,
                    "processed_intervals": processed,
                }
            if count == 1 and right - left <= target_width:
                intervals.append({
                    "interval": (left, right),
                    "root_count": 1,
                    "state": "ISOLATED_SINGLE_REAL_ROOT",
                })
                continue
            if depth >= max_depth:
                unresolved.append({
                    "interval": (left, right),
                    "root_count": count,
                    "depth": depth,
                    "state": "UNRESOLVED_AT_MAX_DEPTH",
                })
                continue

            midpoint = (left + right) / 2
            if _uni_evaluate(current, midpoint) == 0:
                discovered_rational_root = midpoint
                break
            left_count = _uni_sturm_root_count(sequence, left, midpoint)
            right_count = _uni_sturm_root_count(sequence, midpoint, right)
            if left_count:
                queue.append((left, midpoint, depth + 1, left_count))
            if right_count:
                queue.append((midpoint, right, depth + 1, right_count))

        if discovered_rational_root is not None:
            exact_roots.append(discovered_rational_root)
            current = _uni_divide_linear(current, discovered_rational_root)
            continue

        return {
            "status": "ISOLATION_COMPLETE" if not unresolved else "PARTIAL_ISOLATION",
            "exact_roots": tuple(sorted(exact_roots)),
            "isolating_intervals": intervals,
            "unresolved_intervals": unresolved,
            "processed_intervals": processed,
        }

    return {
        "status": "ISOLATION_COMPLETE",
        "exact_roots": tuple(sorted(exact_roots)),
        "isolating_intervals": [],
        "unresolved_intervals": [],
        "processed_intervals": processed,
    }


def compactified_boundary_common_roots(
    poly_p: Poly,
    poly_q: Poly,
    *,
    width=None,
    max_depth: int = 64,
    max_intervals: int = 10000,
) -> dict[str, object]:
    """Isolate real common score roots on all four compactification edges.

    Common factors and multiplicities are obtained by exact gcd/square-free
    decomposition. Each square-free factor is then isolated on [0,1] by an
    exact rational Sturm sequence. Returned intervals are disjoint within
    each factor; exact rational roots (including endpoints) are separated.
    A common edge component or any resource/depth remainder remains explicit.
    """
    from fractions import Fraction

    if width is None:
        width = Fraction(1, 2**20)
    _exact_fraction(width)
    factors = compactified_boundary_common_factors(poly_p, poly_q)
    if factors["status"] == "BOUNDARY_COMMON_COMPONENTS_UNRESOLVED":
        return {
            "status": "BOUNDARY_COMMON_COMPONENTS_UNRESOLVED",
            "edges": factors["edges"],
        }

    output = {}
    incomplete = False
    for edge, edge_result in factors["edges"].items():
        isolated = []
        for factor in edge_result["squarefree_factors"]:
            result = _uni_isolate_squarefree_unit_roots(
                factor["coefficients"],
                width=width,
                max_depth=max_depth,
                max_intervals=max_intervals,
            )
            isolated.append({
                "multiplicity": factor["multiplicity"],
                **result,
            })
            if result["status"] != "ISOLATION_COMPLETE":
                incomplete = True
        output[edge] = {
            **edge_result,
            "isolated_factors": isolated,
        }
    return {
        "status": "PARTIAL_BOUNDARY_ROOT_ISOLATION" if incomplete else "BOUNDARY_ROOT_ISOLATION_COMPLETE",
        "edges": output,
        "corner_deduplication": "NOT_YET_PERFORMED",
    }

def _boundary_corner_for_root(edge, root):
    from fractions import Fraction
    value = Fraction(root)
    if edge == "mu_zero":
        return (Fraction(0), value) if value in (0, 1) else None
    if edge == "mu_one":
        return (Fraction(1), value) if value in (0, 1) else None
    if edge == "t_zero":
        return (value, Fraction(0)) if value in (0, 1) else None
    if edge == "t_one":
        return (value, Fraction(1)) if value in (0, 1) else None
    raise ValueError("UNKNOWN_COMPACTIFIED_EDGE")


def _corner_name(corner):
    from fractions import Fraction
    names = {
        (Fraction(0), Fraction(0)): "mu0_t0",
        (Fraction(0), Fraction(1)): "mu0_t1",
        (Fraction(1), Fraction(0)): "mu1_t0",
        (Fraction(1), Fraction(1)): "mu1_t1",
    }
    return names[corner]


def _apply_boundary_corner_ownership(edges):
    """Assign each corner once; retain every edge occurrence as provenance."""
    from fractions import Fraction

    corner_occurrences = {}
    for edge, edge_result in edges.items():
        for factor_index, factor in enumerate(edge_result.get("isolated_factors", [])):
            for root in factor.get("exact_roots", ()):
                corner = _boundary_corner_for_root(edge, root)
                if corner is None:
                    continue
                corner_occurrences.setdefault(corner, []).append({
                    "edge": edge,
                    "factor_index": factor_index,
                    "root_parameter": Fraction(root),
                    "multiplicity": factor["multiplicity"],
                })

    corner_records = {}
    for corner, occurrences in corner_occurrences.items():
        # Vertical edges own corners; horizontal edges remain provenance-only.
        owner_edge = "mu_zero" if corner[0] == 0 else "mu_one"
        owner = next((item for item in occurrences if item["edge"] == owner_edge), None)
        if owner is None:
            # Defensive fail-closed behavior: never silently invent ownership.
            corner_records[_corner_name(corner)] = {
                "coordinates": corner,
                "status": "CORNER_OWNERSHIP_UNRESOLVED",
                "owner": None,
                "occurrences": occurrences,
            }
            continue
        corner_records[_corner_name(corner)] = {
            "coordinates": corner,
            "status": "CORNER_OWNED_ONCE",
            "owner": {
                "edge": owner_edge,
                "factor_index": owner["factor_index"],
                "root_parameter": owner["root_parameter"],
                "multiplicity": owner["multiplicity"],
            },
            "occurrences": occurrences,
        }

    for edge, edge_result in edges.items():
        for factor_index, factor in enumerate(edge_result.get("isolated_factors", [])):
            factor["root_ownership"] = []
            for root in factor.get("exact_roots", ()):
                corner = _boundary_corner_for_root(edge, root)
                if corner is None:
                    factor["root_ownership"].append({
                        "root": root,
                        "state": "EDGE_INTERIOR_ROOT",
                    })
                    continue
                record = corner_records[_corner_name(corner)]
                is_owner = (
                    record["status"] == "CORNER_OWNED_ONCE"
                    and record["owner"]["edge"] == edge
                    and record["owner"]["root_parameter"] == root
                    and record["owner"]["factor_index"] == factor_index
                )
                factor["root_ownership"].append({
                    "root": root,
                    "state": "CANONICAL_CORNER_OWNER" if is_owner
                    else "CORNER_REFERENCE_ONLY",
                    "corner": _corner_name(corner),
                })
    return corner_records


def compactified_boundary_corner_census(
    poly_p: Poly,
    poly_q: Poly,
    *,
    width=None,
    max_depth: int = 64,
    max_intervals: int = 10000,
) -> dict[str, object]:
    """Return edge roots with a unique, auditable owner for each corner."""
    result = compactified_boundary_common_roots(
        poly_p, poly_q, width=width,
        max_depth=max_depth, max_intervals=max_intervals,
    )
    if result["status"] == "BOUNDARY_COMMON_COMPONENTS_UNRESOLVED":
        return {
            "status": result["status"],
            "edges": result["edges"],
            "corners": {},
        }
    corners = _apply_boundary_corner_ownership(result["edges"])
    unresolved = any(
        corner["status"] != "CORNER_OWNED_ONCE"
        for corner in corners.values()
    )
    result["corners"] = corners
    result["corner_deduplication"] = (
        "CORNER_OWNERSHIP_COMPLETE" if not unresolved
        else "CORNER_OWNERSHIP_PARTIAL"
    )
    if result["status"] == "PARTIAL_BOUNDARY_ROOT_ISOLATION":
        result["status"] = "PARTIAL_BOUNDARY_ROOT_ISOLATION"
    elif unresolved:
        result["status"] = "CORNER_OWNERSHIP_UNRESOLVED"
    else:
        result["status"] = "BOUNDARY_ROOT_CENSUS_WITH_CORNER_OWNERSHIP"
    return result

def beta_binomial_joint_corner_likelihood_limits(
    r: int,
    count_histogram: Mapping[int, int],
) -> dict[str, object]:
    """Classify all four joint (mu,t) compactification-corner limits.

    Here t=kappa/(1+kappa). Uniformly over every kappa>0, the beta-binomial
    mean gives P(X>0) <= E[X] = r*mu and
    P(X<r) <= E[r-X] = r*(1-mu). Thus as mu->0 or mu->1,
    the count distribution converges path-independently to the corresponding
    endpoint point mass, even when kappa simultaneously tends to zero or
    infinity. For a finite independent-world histogram the joint likelihood
    limit is therefore exactly one iff every observed count is that endpoint,
    and zero otherwise.
    """
    from fractions import Fraction

    # Reuse both validation and exact endpoint likelihoods from the
    # established one-edge boundary implementation.
    profiles = beta_binomial_boundary_likelihoods(r, count_histogram)
    zero_likelihood = profiles["mu_zero"]["likelihood"]
    one_likelihood = profiles["mu_one"]["likelihood"]

    zero_mass = tuple([Fraction(1)] + [Fraction(0)] * r)
    one_mass = tuple([Fraction(0)] * r + [Fraction(1)])
    corners = {
        "mu_zero_t_zero": {
            "coordinates": (Fraction(0), Fraction(0)),
            "limit_distribution": zero_mass,
            "likelihood": zero_likelihood,
        },
        "mu_zero_t_one": {
            "coordinates": (Fraction(0), Fraction(1)),
            "limit_distribution": zero_mass,
            "likelihood": zero_likelihood,
        },
        "mu_one_t_zero": {
            "coordinates": (Fraction(1), Fraction(0)),
            "limit_distribution": one_mass,
            "likelihood": one_likelihood,
        },
        "mu_one_t_one": {
            "coordinates": (Fraction(1), Fraction(1)),
            "limit_distribution": one_mass,
            "likelihood": one_likelihood,
        },
    }
    return {
        "status": "ALL_JOINT_CORNER_LIMITS_PATH_INDEPENDENT",
        "parameterization": "t=kappa/(1+kappa)",
        "corners": corners,
        "uniform_probability_bounds": {
            "mu_to_zero": "P(X>0) <= r*mu",
            "mu_to_one": "P(X<r) <= r*(1-mu)",
        },
        "scope": "FINITE_INDEPENDENT_WORLD_HISTOGRAM",
    }

def _bivariate_axis_content(poly: Poly, axis: str):
    """Return the monic univariate content in one variable over Q."""
    from fractions import Fraction

    if axis not in ("mu", "t"):
        raise ValueError("AXIS_MUST_BE_MU_OR_T")
    if not isinstance(poly, Mapping):
        raise ValueError("SPARSE_POLYNOMIAL_MAPPING_REQUIRED")
    grouped = {}
    for monomial, coefficient in poly.items():
        if (
            not isinstance(monomial, tuple) or len(monomial) != 2
            or type(monomial[0]) is not int or monomial[0] < 0
            or type(monomial[1]) is not int or monomial[1] < 0
            or type(coefficient) is not int
        ):
            raise ValueError("POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS")
        if coefficient == 0:
            continue
        variable_degree = monomial[0] if axis == "mu" else monomial[1]
        coefficient_degree = monomial[1] if axis == "mu" else monomial[0]
        grouped.setdefault(coefficient_degree, {})
        grouped[coefficient_degree][variable_degree] = (
            grouped[coefficient_degree].get(variable_degree, 0) + coefficient
        )
    if not grouped:
        return [Fraction(0)]
    coefficient_polynomials = []
    for terms in grouped.values():
        degree = max(terms)
        coefficient_polynomials.append([
            Fraction(terms.get(index, 0)) for index in range(degree + 1)
        ])
    content = coefficient_polynomials[0]
    for coefficient_polynomial in coefficient_polynomials[1:]:
        content = _uni_gcd(content, coefficient_polynomial)
        if len(content) == 1:
            break
    return _uni_monic(content)


def compactified_axis_common_components(
    poly_p: Poly, poly_q: Poly
) -> dict[str, object]:
    """Detect common vertical/horizontal polynomial components exactly.

    This detects common factors depending on mu alone (vertical components)
    or t alone (horizontal components). It deliberately does not claim to
    detect general mixed bivariate factors; those require Q(mu)[t] gcd or
    another exact bivariate factor algorithm.
    """
    if not isinstance(poly_p, Mapping) or not isinstance(poly_q, Mapping):
        raise ValueError("SPARSE_POLYNOMIAL_MAPPING_REQUIRED")

    output = {}
    for axis in ("mu", "t"):
        content_p = _bivariate_axis_content(poly_p, axis)
        content_q = _bivariate_axis_content(poly_q, axis)
        if _uni_is_zero(content_p) or _uni_is_zero(content_q):
            return {
                "status": "ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED",
                "axes": {},
                "scope": "COMMON_FACTORS_DEPENDING_ON_MU_OR_T_ONLY",
                "general_mixed_bivariate_factors": "NOT_CHECKED",
            }
        common = _uni_gcd(content_p, content_q)
        if len(common) > 1:
            output[axis] = {
                "component_type": (
                    "VERTICAL_COMMON_COMPONENT" if axis == "mu"
                    else "HORIZONTAL_COMMON_COMPONENT"
                ),
                "common_factor": tuple(common),
                "squarefree_factors": _uni_squarefree_factors(common),
            }
        else:
            output[axis] = {
                "component_type": "NO_AXIS_ALIGNED_COMMON_COMPONENT",
                "common_factor": tuple(common),
                "squarefree_factors": [],
            }
    detected = any(
        item["component_type"] != "NO_AXIS_ALIGNED_COMMON_COMPONENT"
        for item in output.values()
    )
    return {
        "status": (
            "AXIS_ALIGNED_COMMON_COMPONENTS_DETECTED" if detected
            else "NO_AXIS_ALIGNED_COMMON_COMPONENT_DETECTED"
        ),
        "axes": output,
        "scope": "COMMON_FACTORS_DEPENDING_ON_MU_OR_T_ONLY",
        "general_mixed_bivariate_factors": "NOT_CHECKED",
    }

def _uni_add_exact(left, right):
    from fractions import Fraction
    a = _uni_trim(left)
    b = _uni_trim(right)
    size = max(len(a), len(b))
    return _uni_trim([
        (a[i] if i < len(a) else Fraction(0))
        + (b[i] if i < len(b) else Fraction(0))
        for i in range(size)
    ])


def _uni_mul_exact(left, right):
    from fractions import Fraction
    a = _uni_trim(left)
    b = _uni_trim(right)
    if _uni_is_zero(a) or _uni_is_zero(b):
        return [Fraction(0)]
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return _uni_trim(out)


def _uni_pow_exact(poly, exponent):
    from fractions import Fraction
    if type(exponent) is not int or exponent < 0:
        raise ValueError("POLYNOMIAL_EXPONENT_MUST_BE_NONNEGATIVE_INTEGER")
    result = [Fraction(1)]
    factor = _uni_trim(poly)
    power = exponent
    while power:
        if power & 1:
            result = _uni_mul_exact(result, factor)
        factor = _uni_mul_exact(factor, factor)
        power >>= 1
    return result


def _uni_exact_quotient(dividend, divisor):
    quotient, remainder = _uni_divmod(dividend, divisor)
    if not _uni_is_zero(remainder):
        raise ArithmeticError("BAREISS_DIVISION_NOT_EXACT")
    return quotient


def _bivariate_primitive_t_coefficients(poly):
    """Return mu-content and primitive t-coefficients, highest t-degree first."""
    from fractions import Fraction

    content = _bivariate_axis_content(poly, "mu")
    if _uni_is_zero(content):
        return content, []
    grouped = {}
    for (degree_mu, degree_t), coefficient in poly.items():
        if type(degree_mu) is not int or degree_mu < 0 or type(degree_t) is not int or degree_t < 0 or type(coefficient) is not int:
            raise ValueError("POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS")
        if coefficient:
            grouped.setdefault(degree_t, {})
            grouped[degree_t][degree_mu] = grouped[degree_t].get(degree_mu, 0) + coefficient
    if not grouped:
        return [Fraction(0)], []
    primitive = {}
    for degree_t, terms in grouped.items():
        degree_mu = max(terms)
        coefficient_poly = [Fraction(terms.get(i, 0)) for i in range(degree_mu + 1)]
        quotient, remainder = _uni_divmod(coefficient_poly, content)
        if not _uni_is_zero(remainder):
            raise ArithmeticError("CONTENT_DIVISION_NOT_EXACT")
        primitive[degree_t] = quotient
    max_degree = max(primitive)
    coefficients = [
        _uni_trim(primitive.get(degree, [Fraction(0)]))
        for degree in range(max_degree, -1, -1)
    ]
    while len(coefficients) > 1 and _uni_is_zero(coefficients[0]):
        coefficients.pop(0)
    return content, coefficients


def _polynomial_resultant_bareiss(left_descending, right_descending, max_dimension):
    """Exact Sylvester determinant over Q[mu] using fraction-free Bareiss."""
    from fractions import Fraction

    m = len(left_descending) - 1
    n = len(right_descending) - 1
    dimension = m + n
    if dimension > max_dimension:
        return {
            "status": "RESULTANT_MATRIX_RESOURCE_LIMIT",
            "resultant": None,
            "matrix_dimension": dimension,
        }
    if dimension == 0:
        return {
            "status": "CONSTANT_POLYNOMIAL_PAIR",
            "resultant": (Fraction(1),),
            "matrix_dimension": 0,
        }

    zero = [Fraction(0)]
    matrix = [[zero for _ in range(dimension)] for _ in range(dimension)]
    for row in range(n):
        for index, coefficient in enumerate(left_descending):
            matrix[row][row + index] = coefficient
    for row in range(m):
        for index, coefficient in enumerate(right_descending):
            matrix[n + row][row + index] = coefficient

    previous_pivot = [Fraction(1)]
    sign = 1
    for pivot_index in range(dimension - 1):
        pivot_row = next(
            (
                row for row in range(pivot_index, dimension)
                if not _uni_is_zero(matrix[row][pivot_index])
            ),
            None,
        )
        if pivot_row is None:
            return {
                "status": "ZERO_RESULTANT_COMMON_FACTOR_OR_DEGENERACY",
                "resultant": (Fraction(0),),
                "matrix_dimension": dimension,
            }
        if pivot_row != pivot_index:
            matrix[pivot_index], matrix[pivot_row] = matrix[pivot_row], matrix[pivot_index]
            sign *= -1
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, dimension):
            for column in range(pivot_index + 1, dimension):
                numerator = _uni_add_exact(
                    _uni_mul_exact(matrix[row][column], pivot),
                    [
                        -value for value in _uni_mul_exact(
                            matrix[row][pivot_index],
                            matrix[pivot_index][column],
                        )
                    ],
                )
                matrix[row][column] = (
                    numerator if pivot_index == 0
                    else _uni_exact_quotient(numerator, previous_pivot)
                )
            matrix[row][pivot_index] = zero
        previous_pivot = pivot

    determinant = matrix[-1][-1]
    if sign < 0:
        determinant = [-value for value in determinant]
    return {
        "status": (
            "ZERO_RESULTANT_COMMON_FACTOR_OR_DEGENERACY"
            if _uni_is_zero(determinant) else "EXACT_RESULTANT_NONZERO"
        ),
        "resultant": tuple(_uni_trim(determinant)),
        "matrix_dimension": dimension,
    }


def compactified_projection_resultant_mu(
    poly_p: Poly,
    poly_q: Poly,
    *,
    max_matrix_dimension: int = 64,
) -> dict[str, object]:
    """Compute exact Res_t(P,Q) as a rational polynomial in mu.

    Coefficient contents in mu are separated before the Sylvester determinant.
    The full resultant is reconstructed as content(P)^deg_t(Q) *
    content(Q)^deg_t(P) * Res_t(P_primitive,Q_primitive). A zero primitive
    resultant is reported as an unresolved common-factor/degeneracy state.
    """
    if type(max_matrix_dimension) is not int or max_matrix_dimension < 1:
        raise ValueError("MAX_MATRIX_DIMENSION_MUST_BE_POSITIVE_INTEGER")
    content_p, primitive_p = _bivariate_primitive_t_coefficients(poly_p)
    content_q, primitive_q = _bivariate_primitive_t_coefficients(poly_q)
    if not primitive_p or not primitive_q:
        return {
            "status": "ZERO_POLYNOMIAL_RESULTANT_UNRESOLVED",
            "resultant": None,
            "primitive_resultant": None,
            "content_mu_p": tuple(content_p),
            "content_mu_q": tuple(content_q),
            "matrix_dimension": None,
        }

    primitive_result = _polynomial_resultant_bareiss(
        primitive_p, primitive_q, max_matrix_dimension
    )
    if primitive_result["resultant"] is None:
        return {
            **primitive_result,
            "resultant": None,
            "primitive_resultant": None,
            "content_mu_p": tuple(content_p),
            "content_mu_q": tuple(content_q),
        }

    m = len(primitive_p) - 1
    n = len(primitive_q) - 1
    full = _uni_mul_exact(
        _uni_mul_exact(
            _uni_pow_exact(content_p, n),
            _uni_pow_exact(content_q, m),
        ),
        primitive_result["resultant"],
    )
    return {
        "status": primitive_result["status"],
        "resultant": tuple(_uni_trim(full)),
        "primitive_resultant": primitive_result["resultant"],
        "content_mu_p": tuple(content_p),
        "content_mu_q": tuple(content_q),
        "degree_t_p": m,
        "degree_t_q": n,
        "matrix_dimension": primitive_result["matrix_dimension"],
        "coefficient_order": "ASCENDING_MU_DEGREE",
        "coefficient_domain": "EXACT_FRACTION",
    }

def compactified_projection_root_isolation_mu(
    resultant_result: Mapping[str, object],
    *,
    width,
    max_depth: int = 64,
    max_intervals: int = 10000,
) -> dict[str, object]:
    """Square-free factor and Sturm-isolate real projection roots in mu in [0,1].

    Returned roots are projection coordinates only. They are not yet lifted
    to common (mu,t) roots and their multiplicities are not local intersection
    multiplicities.
    """
    from fractions import Fraction

    if not isinstance(resultant_result, Mapping):
        raise ValueError("RESULTANT_RESULT_MAPPING_REQUIRED")
    target_width = _exact_fraction(width)
    if target_width <= 0:
        raise ValueError("ISOLATION_WIDTH_MUST_BE_POSITIVE")
    if type(max_depth) is not int or max_depth < 0:
        raise ValueError("MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER")
    if type(max_intervals) is not int or max_intervals < 1:
        raise ValueError("MAX_INTERVALS_MUST_BE_POSITIVE_INTEGER")
    status = resultant_result.get("status")
    if status != "EXACT_RESULTANT_NONZERO":
        return {
            "status": "PROJECTION_ISOLATION_NOT_AVAILABLE_FROM_RESULTANT_STATUS",
            "resultant_status": status,
            "factors": [],
        }
    polynomial = resultant_result.get("resultant")
    if not isinstance(polynomial, (tuple, list)) or not polynomial:
        raise ValueError("NONZERO_RESULTANT_POLYNOMIAL_REQUIRED")
    if any(type(value) is not int and type(value) is not Fraction for value in polynomial):
        raise ValueError("EXACT_RATIONAL_REQUIRED")
    factors = _uni_squarefree_factors(polynomial)
    isolated_factors = []
    incomplete = False
    for factor in factors:
        isolation = _uni_isolate_squarefree_unit_roots(
            factor["coefficients"],
            width=width,
            max_depth=max_depth,
            max_intervals=max_intervals,
        )
        if isolation["status"] != "ISOLATION_COMPLETE":
            incomplete = True
        isolated_factors.append({
            "projection_multiplicity": factor["multiplicity"],
            **isolation,
        })
    return {
        "status": (
            "PROJECTION_ROOT_ISOLATION_COMPLETE" if not incomplete
            else "PROJECTION_ROOT_ISOLATION_PARTIAL"
        ),
        "axis": "mu",
        "domain": (0, 1),
        "factors": isolated_factors,
        "scope": "PROJECTION_COORDINATES_ONLY_NOT_LIFTED_TO_BIVARIATE_ROOTS",
        "multiplicity_warning": "PROJECTION_MULTIPLICITY_IS_NOT_LOCAL_INTERSECTION_MULTIPLICITY",
    }

def compactified_concentration_resultant_t(
    poly_p: Poly,
    poly_q: Poly,
    *,
    max_matrix_dimension: int = 64,
) -> dict[str, object]:
    """Compute Res_mu(P,Q) as an exact rational polynomial in compactified t.

    The sparse input convention is (degree_mu, degree_t). Swapping exponents
    lets the existing exact Sylvester/Bareiss kernel eliminate mu and retain t.
    This is the projection aligned with the F5 profile-likelihood reduction:
    t=kappa/(1+kappa), with 0<t<1 for finite positive concentration.
    """
    if not isinstance(poly_p, Mapping) or not isinstance(poly_q, Mapping):
        raise ValueError("SPARSE_POLYNOMIAL_MAPPING_REQUIRED")

    def swap_axes(poly):
        swapped = {}
        for monomial, coefficient in poly.items():
            if (
                not isinstance(monomial, tuple) or len(monomial) != 2
                or type(monomial[0]) is not int or monomial[0] < 0
                or type(monomial[1]) is not int or monomial[1] < 0
                or type(coefficient) is not int
            ):
                raise ValueError("POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS")
            swapped[(monomial[1], monomial[0])] = coefficient
        return swapped

    result = compactified_projection_resultant_mu(
        swap_axes(poly_p),
        swap_axes(poly_q),
        max_matrix_dimension=max_matrix_dimension,
    )
    return {
        **result,
        "projection_axis": "t",
        "eliminated_axis": "mu",
        "mathematical_object": "RESULTANT_MU_P_Q",
        "concentration_parameterization": "t=kappa/(1+kappa)",
        "finite_positive_concentration_domain": (0, 1),
    }


def compactified_concentration_root_isolation_t(
    resultant_result: Mapping[str, object],
    *,
    width,
    max_depth: int = 64,
    max_intervals: int = 10000,
) -> dict[str, object]:
    """Sturm-isolate the exact concentration-projection roots in 0<t<1."""
    isolated = compactified_projection_root_isolation_mu(
        resultant_result,
        width=width,
        max_depth=max_depth,
        max_intervals=max_intervals,
    )
    return {
        **isolated,
        "axis": "t",
        "scope": "CONCENTRATION_PROJECTION_ONLY_NOT_YET_LIFTED_TO_MEAN_ROOT",
        "concentration_parameterization": "t=kappa/(1+kappa)",
        "finite_positive_concentration_domain": (0, 1),
    }



def conditional_mean_tube_and_concentration_exclusion(
    poly_mean_score: Poly,
    poly_concentration_score: Poly,
    *,
    t_bounds: tuple[object, object],
    max_mu_depth: int = 10,
) -> dict[str, object]:
    """Bracket the unique conditional mean root uniformly over a t interval.

    Evaluate the mean-score numerator at rational mu values by exact
    univariate Bernstein bounds in t. Strict conditional concavity permits
    sign-guided dyadic bisection: a uniformly positive lower witness and a
    uniformly negative upper witness bracket the unique mean root for every
    t in the interval. This takes O(max_mu_depth) exact line evaluations. The concentration-score numerator is then bounded on
    the resulting rational (mu,t) tube by tensor-product Bernstein coefficients.

    If that second numerator has strict constant sign on the tube, the entire
    t interval contains no common stationary point. Otherwise the tube is a
    conservative candidate region, not a root/existence certificate. The
    caller must supply the compactified exact score numerators produced from
    the same nondegenerate beta-binomial histogram; the concavity implication
    is not valid for arbitrary unrelated polynomial pairs.
    """
    from fractions import Fraction
    from math import comb

    if type(max_mu_depth) is not int or not 1 <= max_mu_depth <= 16:
        raise ValueError("MAX_MU_DEPTH_MUST_BE_INTEGER_1_TO_16")
    if not isinstance(t_bounds, tuple) or len(t_bounds) != 2:
        raise ValueError("INVALID_T_BOUNDS")
    try:
        t_lo, t_hi = (_exact_fraction(t_bounds[0]), _exact_fraction(t_bounds[1]))
    except ValueError:
        raise ValueError("INVALID_T_BOUNDS") from None
    if not 0 <= t_lo < t_hi <= 1:
        raise ValueError("T_BOUNDS_MUST_BE_WITHIN_COMPACTIFIED_CLOSURE")
    for poly in (poly_mean_score, poly_concentration_score):
        if not isinstance(poly, Mapping) or any(
            not isinstance(monomial, tuple) or len(monomial) != 2
            or type(monomial[0]) is not int or monomial[0] < 0
            or type(monomial[1]) is not int or monomial[1] < 0
            or type(coefficient) is not int
            for monomial, coefficient in poly.items()
        ):
            raise ValueError("POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS")

    def line_bernstein_sign(poly, mu_value):
        # Restrict P(mu,t) to the rational line mu=mu_value.
        coeffs = defaultdict(Fraction)
        for (i, j), coefficient in poly.items():
            coeffs[j] += Fraction(coefficient) * mu_value**i
        while coeffs and max(coeffs) > 0 and coeffs[max(coeffs)] == 0:
            del coeffs[max(coeffs)]
        if not coeffs:
            return 0

        # The open concentration domain excludes t=1. A restricted mean-score
        # line may therefore carry an endpoint-only factor (t-1)^m even when
        # the full bivariate score has no common horizontal factor. Strip it
        # exactly before taking Bernstein bounds on an interval ending at 1;
        # on t<1 its sign is (-1)^m and it cannot create or remove an interior
        # mean root. The endpoint stratum itself is adjudicated separately.
        endpoint_multiplicity = 0
        if t_hi == 1 and t_lo < 1:
            while coeffs and sum(coeffs.values(), Fraction(0)) == 0:
                degree_now = max(coeffs)
                if degree_now == 0:
                    return 0
                ascending = [
                    Fraction(coeffs.get(index, 0))
                    for index in range(degree_now + 1)
                ]
                quotient, remainder = _uni_divmod(
                    ascending, (Fraction(-1), Fraction(1))
                )
                if not _uni_is_zero(remainder):
                    break
                coeffs = defaultdict(Fraction)
                for index, value in enumerate(quotient):
                    if value:
                        coeffs[index] = value
                endpoint_multiplicity += 1
        if not coeffs:
            return 0
        degree = max(coeffs)
        # Substitute t=t_lo+(t_hi-t_lo)*u in the power basis.
        transformed = [Fraction(0) for _ in range(degree + 1)]
        for power, coefficient in coeffs.items():
            for j in range(power + 1):
                transformed[j] += (
                    coefficient * comb(power, j) * t_lo**(power-j)
                    * (t_hi-t_lo)**j
                )
        bernstein = []
        for i in range(degree + 1):
            value = Fraction(0)
            for j in range(i + 1):
                value += transformed[j] * Fraction(comb(i, j), comb(degree, j))
            bernstein.append(value)
        if all(value > 0 for value in bernstein):
            sign = 1
        elif all(value < 0 for value in bernstein):
            sign = -1
        else:
            return 0
        return sign * (-1 if endpoint_multiplicity % 2 else 1)

    denominator = 2**max_mu_depth
    lower = Fraction(0)
    upper = Fraction(1)
    lower_sign = line_bernstein_sign(poly_mean_score, lower)
    upper_sign = line_bernstein_sign(poly_mean_score, upper)
    if lower_sign <= 0 or upper_sign >= 0:
        return {
            "status": "MEAN_ROOT_TUBE_UNRESOLVED_ENDPOINT_SIGNS",
            "t_bounds": (t_lo, t_hi),
            "grid_denominator": denominator,
            "certified_positive_grid_indices": [],
            "certified_negative_grid_indices": [],
        }

    # Strict conditional concavity means any uniformly positive lower witness
    # and negative upper witness bracket the unique mean root. Bisection needs
    # O(depth) exact line-sign evaluations rather than scanning 2**depth points.
    for _ in range(max_mu_depth):
        midpoint = (lower + upper) / 2
        midpoint_sign = line_bernstein_sign(poly_mean_score, midpoint)
        if midpoint_sign > 0:
            lower = midpoint
        elif midpoint_sign < 0:
            upper = midpoint
        else:
            # A zero/mixed Bernstein enclosure at the midpoint is not a sign
            # claim. Probe its adjacent dyadic grid points; if they bracket
            # uniformly, retain the narrow bracket, otherwise let t subdivision
            # reduce the variation and retry.
            step = Fraction(1, denominator)
            left_probe = max(lower, midpoint - step)
            right_probe = min(upper, midpoint + step)
            left_sign = line_bernstein_sign(poly_mean_score, left_probe)
            right_sign = line_bernstein_sign(poly_mean_score, right_probe)
            if left_sign > 0 and right_sign < 0:
                lower, upper = left_probe, right_probe
            break

    lower_index = int(lower * denominator)
    upper_index = int(upper * denominator)
    if lower >= upper or lower_sign <= 0 or upper_sign >= 0:
        return {
            "status": "MEAN_ROOT_TUBE_UNRESOLVED_SIGN_ORDER",
            "t_bounds": (t_lo, t_hi),
            "grid_denominator": denominator,
            "certified_positive_grid_indices": [lower_index],
            "certified_negative_grid_indices": [upper_index],
        }
    mu_bounds = (lower, upper)
    q_coefficients = bernstein_coefficients_on_box(
        poly_concentration_score, mu_bounds, (t_lo, t_hi)
    )
    excludes = bernstein_sign_excludes_zero(q_coefficients)
    return {
        "status": (
            "NO_COMMON_STATIONARY_POINT_ON_T_INTERVAL"
            if excludes else "CANDIDATE_T_INTERVAL_UNRESOLVED"
        ),
        "t_bounds": (t_lo, t_hi),
        "mean_root_tube_mu_bounds": mu_bounds,
        "grid_denominator": denominator,
        "mean_root_existence_for_every_t_certified": True,
        "mean_root_uniqueness_for_every_t_relies_on_strict_conditional_concavity": True,
        "concentration_score_excludes_zero_on_tube": excludes,
        "scope": "INTERVAL_PRUNING_ONLY_NOT_ROOT_EXISTENCE_OR_GLOBAL_CENSUS",
        "required_input_provenance": "PAIRED_COMPACTIFIED_BETA_BINOMIAL_SCORE_NUMERATORS_FROM_ONE_NONDEGENERATE_HISTOGRAM",
    }


def conditional_mean_adaptive_concentration_census(
    poly_mean_score: Poly,
    poly_concentration_score: Poly,
    *,
    t_bounds: tuple[object, object],
    max_intervals: int = 10000,
    max_depth: int = 32,
    max_mu_depth: int = 10,
) -> dict[str, object]:
    """Certify an interval census using conditional-mean tubes and Krawczyk.

    The supplied t interval may be any nonempty rational subinterval of [0,1]. A deterministic
    FIFO subdivision processes concentration intervals. On each interval,
    exact Bernstein signs construct a tube containing the unique conditional
    mean root for every finite t in that interval. A strict Bernstein sign of
    the concentration score excludes the interval. Otherwise, a Krawczyk
    certificate on the entire tube may certify exactly one simple common
    stationary point there. Inconclusive intervals are bisected in t.

    The result is a complete census only for the supplied closed t interval
    and only when every interval is either excluded or certified to contain
    exactly one simple root. Multiple roots, split-boundary roots, boundary
    roots at t=0 or t=1, and resource-limited intervals remain explicitly
    unresolved; the separate edge/corner census adjudicates the boundary strata.
    """
    from collections import deque
    from fractions import Fraction

    if type(max_intervals) is not int or max_intervals < 1:
        raise ValueError("MAX_INTERVALS_MUST_BE_POSITIVE_INTEGER")
    if type(max_depth) is not int or max_depth < 0:
        raise ValueError("MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER")
    if not isinstance(t_bounds, tuple) or len(t_bounds) != 2:
        raise ValueError("INVALID_T_BOUNDS")
    try:
        t_lo, t_hi = (_exact_fraction(t_bounds[0]), _exact_fraction(t_bounds[1]))
    except ValueError:
        raise ValueError("INVALID_T_BOUNDS") from None
    if not 0 <= t_lo < t_hi <= 1:
        raise ValueError("T_BOUNDS_MUST_BE_WITHIN_COMPACTIFIED_CLOSURE")

    queue = deque([(t_lo, t_hi, 0)])
    excluded = []
    certified = []
    unresolved = []
    processed = 0
    subdivisions = 0
    krawczyk_attempts = 0

    while queue and processed < max_intervals:
        t_a, t_b, depth = queue.popleft()
        processed += 1
        tube = conditional_mean_tube_and_concentration_exclusion(
            poly_mean_score,
            poly_concentration_score,
            t_bounds=(t_a, t_b),
            max_mu_depth=max_mu_depth,
        )
        if tube["status"] == "NO_COMMON_STATIONARY_POINT_ON_T_INTERVAL":
            excluded.append({
                "t_bounds": (t_a, t_b),
                "depth": depth,
                "certificate": "BERNSTEIN_CONCENTRATION_SCORE_STRICT_SIGN_ON_MEAN_ROOT_TUBE",
                "mean_root_tube_mu_bounds": tube["mean_root_tube_mu_bounds"],
            })
            continue

        certificate = None
        if tube["status"] == "CANDIDATE_T_INTERVAL_UNRESOLVED":
            krawczyk_attempts += 1
            certificate = krawczyk_certify_unique_root(
                poly_mean_score,
                poly_concentration_score,
                mu_bounds=tube["mean_root_tube_mu_bounds"],
                t_bounds=(t_a, t_b),
            )
            if certificate["status"] == "CERTIFIED_UNIQUE_ROOT":
                certified.append({
                    "t_bounds": (t_a, t_b),
                    "mean_root_tube_mu_bounds": tube["mean_root_tube_mu_bounds"],
                    "depth": depth,
                    "root_certificate": certificate,
                })
                continue

        if depth >= max_depth:
            unresolved.append({
                "t_bounds": (t_a, t_b),
                "depth": depth,
                "state": "UNRESOLVED_AT_MAX_DEPTH",
                "mean_tube_result": tube,
                "krawczyk_result": certificate,
            })
            continue

        midpoint = (t_a + t_b) / 2
        if midpoint == t_a or midpoint == t_b:
            unresolved.append({
                "t_bounds": (t_a, t_b),
                "depth": depth,
                "state": "UNRESOLVED_RATIONAL_SUBDIVISION_STAGNATION",
                "mean_tube_result": tube,
                "krawczyk_result": certificate,
            })
            continue
        queue.append((t_a, midpoint, depth + 1))
        queue.append((midpoint, t_b, depth + 1))
        subdivisions += 1

    while queue:
        t_a, t_b, depth = queue.popleft()
        unresolved.append({
            "t_bounds": (t_a, t_b),
            "depth": depth,
            "state": "NOT_PROCESSED_RESOURCE_LIMIT",
        })

    if unresolved:
        status = (
            "INCOMPLETE_RESOURCE_LIMIT"
            if any(item["state"] == "NOT_PROCESSED_RESOURCE_LIMIT" for item in unresolved)
            else "INCOMPLETE_UNRESOLVED_INTERVALS"
        )
    else:
        status = "COMPLETE_CENSUS_ON_SUPPLIED_T_INTERVAL"

    return {
        "status": status,
        "scope": "CLOSED_COMPACTIFIED_T_INTERVAL_BOUNDARY_ROOTS_NOT_PROMOTED_AS_INTERIOR",
        "t_bounds": (t_lo, t_hi),
        "excluded_intervals": excluded,
        "certified_simple_root_intervals": certified,
        "unresolved_intervals": unresolved,
        "processed_intervals": processed,
        "subdivisions": subdivisions,
        "krawczyk_attempts": krawczyk_attempts,
        "max_intervals": max_intervals,
        "max_depth": max_depth,
        "max_mu_depth": max_mu_depth,
    }


def _validate_f5_census_budgets(
    *,
    max_projection_depth: int,
    max_projection_intervals: int,
    max_lift_intervals: int,
    max_lift_depth: int,
    max_mu_depth: int,
) -> None:
    """Validate every active deterministic ceiling before any early return."""
    for name, value, minimum in (
        ("MAX_PROJECTION_DEPTH", max_projection_depth, 0),
        ("MAX_PROJECTION_INTERVALS", max_projection_intervals, 1),
        ("MAX_LIFT_INTERVALS", max_lift_intervals, 1),
        ("MAX_LIFT_DEPTH", max_lift_depth, 0),
    ):
        if type(value) is not int or value < minimum:
            raise ValueError(f"{name}_MUST_BE_INTEGER_AT_LEAST_{minimum}")
    if type(max_mu_depth) is not int or not 1 <= max_mu_depth <= 16:
        raise ValueError("MAX_MU_DEPTH_MUST_BE_INTEGER_1_TO_16")


def beta_binomial_compactified_stationary_census(
    r: int,
    count_histogram: Mapping[int, int],
    *,
    projection_width=None,
    max_projection_depth: int = 64,
    max_projection_intervals: int = 10000,
    max_lift_intervals: int = 256,
    max_lift_depth: int = 24,
    max_mu_depth: int = 12,
) -> dict[str, object]:
    """Integrate exact concentration projection, simple-root lifting and boundary census.

    The concentration resultant Res_mu(P,Q) plus exact Sturm isolation covers
    every real projection root on the compactified closed t interval. Each
    interior projection root is lifted against the original paired score
    equations using the unique conditional-mean branch, exact Bernstein
    exclusion and rational Krawczyk inclusion. Endpoint projection roots are
    assigned to the separately certified boundary strata.

    A nonzero resultant is necessary for a finite projection census. Axis-
    aligned common components, zero resultants, non-simple lifts, incomplete
    Sturm isolation and resource remainders remain explicit unresolved states.
    This operation does not compare likelihood values and therefore never
    claims a global MLE.
    """
    from fractions import Fraction

    _validate_f5_census_budgets(
        max_projection_depth=max_projection_depth,
        max_projection_intervals=max_projection_intervals,
        max_lift_intervals=max_lift_intervals,
        max_lift_depth=max_lift_depth,
        max_mu_depth=max_mu_depth,
    )
    # Validate the projection width even when the interval-first route avoids
    # the resultant/Sturm fallback.
    if projection_width is None:
        projection_width = Fraction(1, 2**16)
    try:
        projection_width = _exact_fraction(projection_width)
    except (TypeError, ValueError, ZeroDivisionError):
        raise ValueError("PROJECTION_WIDTH_MUST_BE_POSITIVE_RATIONAL") from None
    if projection_width <= 0:
        raise ValueError("PROJECTION_WIDTH_MUST_BE_POSITIVE_RATIONAL")

    # Validate once through the exact score constructor, then preserve the
    # paired provenance by compactifying both numerators from this histogram.
    raw_p, raw_q = beta_binomial_score_numerators(r, count_histogram)
    total = sum(count_histogram.values())
    successes = sum(x * n for x, n in count_histogram.items())
    if not 0 < successes < total * r:
        boundaries = beta_binomial_boundary_likelihoods(r, count_histogram)
        corners = beta_binomial_joint_corner_likelihood_limits(r, count_histogram)
        return {
            "status": "NO_INTERIOR_MEAN_ROOT_DEGENERATE_DATA",
            "interior_stationary_candidates": [],
            "boundary_likelihoods": boundaries,
            "joint_corner_limits": corners,
            "global_likelihood_ordering": "NOT_PERFORMED",
            "scope": "DEGENERATE_POOLED_MEAN_HAS_NO_INTERIOR_CONDITIONAL_MEAN_ROOT",
        }

    poly_p = compactify_concentration(raw_p)
    poly_q = compactify_concentration(raw_q)
    original_axis_components = compactified_axis_common_components(poly_p, poly_q)
    boundary_likelihoods = beta_binomial_boundary_likelihoods(r, count_histogram)
    corner_limits = beta_binomial_joint_corner_likelihood_limits(r, count_histogram)

    stripped = _strip_axis_content_factors_outside_open_unit_domain(poly_p, poly_q)
    if stripped["status"] != "NO_REAL_INTERIOR_AXIS_CONTENT_FACTORS":
        return {
            "status": "INCOMPLETE_COMMON_COMPONENT",
            "axis_components": original_axis_components,
            "component_disposition": stripped,
            "boundary_likelihoods": boundary_likelihoods,
            "joint_corner_limits": corner_limits,
            "interior_stationary_candidates": [],
            "global_likelihood_ordering": "NOT_PERFORMED",
        }
    poly_p = stripped["poly_p"]
    poly_q = stripped["poly_q"]
    axis_components = compactified_axis_common_components(poly_p, poly_q)
    if axis_components["status"] != "NO_AXIS_ALIGNED_COMMON_COMPONENT_DETECTED":
        return {
            "status": "INCOMPLETE_COMMON_COMPONENT",
            "axis_components": axis_components,
            "component_disposition": stripped,
            "boundary_likelihoods": boundary_likelihoods,
            "joint_corner_limits": corner_limits,
            "interior_stationary_candidates": [],
            "global_likelihood_ordering": "NOT_PERFORMED",
        }

    # The four open-domain boundary strata are already profiled exactly by
    # beta_binomial_boundary_likelihoods, and the uniform moment bounds in
    # beta_binomial_joint_corner_likelihood_limits prove all four joint corner
    # limits path-independent. A separate edge score-root census is therefore
    # not a prerequisite for global likelihood ordering.
    boundary = {
        "status": "BOUNDARY_STRATA_AND_CORNERS_ADJUDICATED",
        "method": "EXACT_ONE_EDGE_PROFILES_AND_UNIFORM_JOINT_CORNER_LIMITS",
        "edge_score_root_census": "NOT_REQUIRED_FOR_GLOBAL_MLE",
        "profile_status": boundary_likelihoods["status"],
        "joint_corner_status": corner_limits["status"],
    }

    # Preferred first line: certify the entire compactified concentration
    # interval directly with conditional-mean concavity, Bernstein exclusion
    # and Krawczyk inclusion. The exact resultant is the fallback/cross-check.
    interval_first = conditional_mean_adaptive_concentration_census(
        poly_p, poly_q,
        t_bounds=(Fraction(0), Fraction(1)),
        max_intervals=max_lift_intervals,
        max_depth=max_lift_depth,
        max_mu_depth=max_mu_depth,
    )
    if (
        interval_first["status"] == "COMPLETE_CENSUS_ON_SUPPLIED_T_INTERVAL"
        and boundary["status"] == "BOUNDARY_STRATA_AND_CORNERS_ADJUDICATED"
    ):
        return {
            "status": "INTERIOR_SIMPLE_ROOT_AND_BOUNDARY_CENSUS_COMPLETE",
            "paired_score_provenance": "SAME_VALIDATED_NONDEGENERATE_COUNT_HISTOGRAM",
            "compactified_parameterization": "t=kappa/(1+kappa)",
            "original_axis_components": original_axis_components,
            "component_disposition": stripped,
            "axis_components": axis_components,
            "concentration_resultant": {
                "status": "NOT_REQUIRED_INTERVAL_FIRST_LINE_COMPLETE",
                "method": "CONDITIONAL_MEAN_BERNSTEIN_KRAWCZYK",
            },
            "concentration_projection": {
                "status": "NOT_REQUIRED_INTERVAL_FIRST_LINE_COMPLETE",
                "domain": (Fraction(0), Fraction(1)),
            },
            "interior_stationary_candidates": [{
                "projection_source": "FULL_DOMAIN_CONDITIONAL_MEAN_BERNSTEIN",
                "lift_result": interval_first,
            }],
            "interval_first_attempt": interval_first,
            "endpoint_projection_roots": (),
            "boundary_census": boundary,
            "boundary_likelihoods": boundary_likelihoods,
            "joint_corner_limits": corner_limits,
            "unresolved_lifts": [],
            "global_likelihood_ordering": "NOT_PERFORMED",
            "scope": "FULL_OPEN_CONCENTRATION_DOMAIN_CENSUSED_WITH_BOUNDARY_STRATA_SEPARATE",
            "resource_contract": {
                "max_lift_intervals": max_lift_intervals,
                "max_lift_depth": max_lift_depth,
                "max_mu_depth": max_mu_depth,
                "boundary_evaluation": "EXACT_CLOSED_FORM_NO_ITERATIVE_BUDGET",
            },
        }

    resultant = compactified_concentration_resultant_t(poly_p, poly_q)
    if resultant["status"] != "EXACT_RESULTANT_NONZERO":
        return {
            "status": "INCOMPLETE_RESULTANT_OR_COMMON_COMPONENT",
            "original_axis_components": original_axis_components,
            "component_disposition": stripped,
            "axis_components": axis_components,
            "concentration_resultant": resultant,
            "interval_first_attempt": interval_first,
            "boundary_census": boundary,
            "boundary_likelihoods": boundary_likelihoods,
            "joint_corner_limits": corner_limits,
            "interior_stationary_candidates": [],
            "global_likelihood_ordering": "NOT_PERFORMED",
        }

    projection = compactified_concentration_root_isolation_t(
        resultant,
        width=projection_width,
        max_depth=max_projection_depth,
        max_intervals=max_projection_intervals,
    )
    if projection["status"] != "PROJECTION_ROOT_ISOLATION_COMPLETE":
        return {
            "status": "INCOMPLETE_PROJECTION_ROOT_ISOLATION",
            "original_axis_components": original_axis_components,
            "component_disposition": stripped,
            "axis_components": axis_components,
            "concentration_resultant": resultant,
            "concentration_projection": projection,
            "interval_first_attempt": interval_first,
            "boundary_census": boundary,
            "boundary_likelihoods": boundary_likelihoods,
            "joint_corner_limits": corner_limits,
            "interior_stationary_candidates": [],
            "global_likelihood_ordering": "NOT_PERFORMED",
        }

    # Collect all non-endpoint real projection roots. Sturm intervals each
    # contain exactly one root; rational roots are represented exactly and
    # receive a disjoint rational neighborhood for the interval lift.
    intervals = []
    exact_roots = []
    for factor in projection["factors"]:
        intervals.extend(item["interval"] for item in factor["isolating_intervals"])
        exact_roots.extend(factor["exact_roots"])
    intervals = sorted((Fraction(a), Fraction(b)) for a, b in intervals)
    exact_roots = sorted(set(Fraction(root) for root in exact_roots))
    interior_roots = [root for root in exact_roots if 0 < root < 1]
    endpoint_roots = [root for root in exact_roots if root in (0, 1)]

    lift_brackets = [(a, b, "STURM_ISOLATING_INTERVAL") for a, b in intervals]
    for root in interior_roots:
        left_neighbors = (
            [b for a, b in intervals if b < root]
            + [other for other in exact_roots if other < root]
        )
        right_neighbors = (
            [a for a, b in intervals if a > root]
            + [other for other in exact_roots if other > root]
        )
        left_gap = root - max(left_neighbors, default=Fraction(0))
        right_gap = min(right_neighbors, default=Fraction(1)) - root
        radius = min(Fraction(1, 2**16), root / 2, (1 - root) / 2,
                     left_gap / 4, right_gap / 4)
        if radius <= 0:
            return {
                "status": "INCOMPLETE_RATIONAL_PROJECTION_ROOT_NEIGHBORHOOD",
                "concentration_projection": projection,
                "exact_root": root,
                "global_likelihood_ordering": "NOT_PERFORMED",
            }
        lift_brackets.append((root - radius, root + radius, "EXACT_RATIONAL_ROOT_NEIGHBORHOOD"))

    lift_brackets.sort(key=lambda item: item[0])
    interior_lifts = []
    for t_lo, t_hi, source in lift_brackets:
        if not 0 < t_lo < t_hi < 1:
            return {
                "status": "INCOMPLETE_INTERIOR_PROJECTION_BRACKET_TOUCHES_BOUNDARY",
                "concentration_projection": projection,
                "interior_lifts": interior_lifts,
                "offending_bracket": (t_lo, t_hi, source),
                "global_likelihood_ordering": "NOT_PERFORMED",
            }
        lift = conditional_mean_adaptive_concentration_census(
            poly_p, poly_q,
            t_bounds=(t_lo, t_hi),
            max_intervals=max_lift_intervals,
            max_depth=max_lift_depth,
            max_mu_depth=max_mu_depth,
        )
        interior_lifts.append({
            "t_bounds": (t_lo, t_hi),
            "projection_source": source,
            "lift_result": lift,
        })

    unresolved_lifts = [
        item for item in interior_lifts
        if item["lift_result"]["status"] != "COMPLETE_CENSUS_ON_SUPPLIED_T_INTERVAL"
    ]
    boundary_complete = boundary["status"] == "BOUNDARY_STRATA_AND_CORNERS_ADJUDICATED"
    complete = not unresolved_lifts and boundary_complete
    return {
        "status": (
            "INTERIOR_SIMPLE_ROOT_AND_BOUNDARY_CENSUS_COMPLETE"
            if complete else "INCOMPLETE_STATIONARY_CENSUS"
        ),
        "paired_score_provenance": "SAME_VALIDATED_NONDEGENERATE_COUNT_HISTOGRAM",
        "compactified_parameterization": "t=kappa/(1+kappa)",
        "original_axis_components": original_axis_components,
        "component_disposition": stripped,
        "axis_components": axis_components,
        "concentration_resultant": resultant,
        "concentration_projection": projection,
        "interval_first_attempt": interval_first,
        "interior_stationary_candidates": interior_lifts,
        "endpoint_projection_roots": tuple(endpoint_roots),
        "boundary_census": boundary,
        "boundary_likelihoods": boundary_likelihoods,
        "joint_corner_limits": corner_limits,
        "unresolved_lifts": unresolved_lifts,
        "global_likelihood_ordering": "NOT_PERFORMED",
        "scope": (
            "ALL_REAL_CONCENTRATION_PROJECTION_ROOTS_LIFTED_OR_EXPLICITLY_UNRESOLVED; "
            "BOUNDARY_STRATA_CENSUSED; GLOBAL_MLE_NOT_CERTIFIED"
        ),
        "resource_contract": {
            "max_projection_depth": max_projection_depth,
            "max_projection_intervals": max_projection_intervals,
            "max_lift_intervals_per_projection_root": max_lift_intervals,
            "max_lift_depth": max_lift_depth,
            "max_mu_depth": max_mu_depth,
            "boundary_evaluation": "EXACT_CLOSED_FORM_NO_ITERATIVE_BUDGET",
        },
    }


def _beta_binomial_likelihood_enclosure(
    r: int,
    count_histogram: Mapping[int, int],
    *,
    mu_bounds: tuple[object, object],
    t_bounds: tuple[object, object],
    max_fraction_bits: int = 200000,
) -> dict[str, object]:
    """Enclose likelihood with exact outward-rounded fixed-point products.

    Per-outcome probability bounds are rational. The product over the full
    histogram is accumulated on a dyadic grid with directed integer rounding,
    preventing numerator/denominator bit growth while preserving a rigorous
    enclosure. No floating-point arithmetic is used.
    """
    from fractions import Fraction
    from math import comb

    if type(max_fraction_bits) is not int or max_fraction_bits < 64:
        raise ValueError("MAX_FRACTION_BITS_MUST_BE_INTEGER_AT_LEAST_64")
    if type(r) is not int or r < 1:
        raise ValueError("R_MUST_BE_POSITIVE_INTEGER")
    if not isinstance(count_histogram, Mapping) or not count_histogram:
        raise ValueError("NONEMPTY_COUNT_HISTOGRAM_REQUIRED")
    validated_total = 0
    for x, multiplicity in count_histogram.items():
        if type(x) is not int or not 0 <= x <= r:
            raise ValueError("COUNT_OUTSIDE_0_TO_R")
        if type(multiplicity) is not int or multiplicity < 0:
            raise ValueError("MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER")
        validated_total += multiplicity
    if validated_total <= 0:
        raise ValueError("POSITIVE_TOTAL_MULTIPLICITY_REQUIRED")

    mu_lo, mu_hi = (_exact_fraction(v) for v in mu_bounds)
    t_lo, t_hi = (_exact_fraction(v) for v in t_bounds)
    if not 0 < mu_lo <= mu_hi < 1 or not 0 < t_lo <= t_hi < 1:
        raise ValueError("LIKELIHOOD_BOX_MUST_BE_INTERIOR")

    corners = (
        (mu_lo, t_lo), (mu_lo, t_hi),
        (mu_hi, t_lo), (mu_hi, t_hi),
    )

    def bilinear_range(which: str, j: int):
        values = []
        for mu, t in corners:
            if which == "alpha":
                values.append(mu * t + j * (1 - t))
            else:
                values.append((1 - mu) * t + j * (1 - t))
        return min(values), max(values)

    # A fixed 256-bit dyadic accumulator keeps resource use independent of
    # sample size. The caller's ceiling remains a hard upper bound.
    precision = min(256, max_fraction_bits // 4)
    scale = 1 << precision

    def floor_scaled(value: Fraction) -> int:
        return (value.numerator * scale) // value.denominator

    def ceil_scaled(value: Fraction) -> int:
        return -((-value.numerator * scale) // value.denominator)

    def multiply_interval(left, right):
        lo = (left[0] * right[0]) // scale
        hi_product = right[1] * left[1]
        hi = (hi_product + scale - 1) // scale
        return lo, hi

    def power_interval(interval, exponent: int):
        result = (scale, scale)
        base = interval
        n = exponent
        while n:
            if n & 1:
                result = multiply_interval(result, base)
            n >>= 1
            if n:
                base = multiply_interval(base, base)
        return result

    likelihood = (scale, scale)
    for x, multiplicity in count_histogram.items():
        if type(x) is not int or not 0 <= x <= r:
            raise ValueError("COUNT_OUTSIDE_0_TO_R")
        if type(multiplicity) is not int or multiplicity < 0:
            raise ValueError("MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER")
        if multiplicity == 0:
            continue

        numerator_lo = Fraction(1)
        numerator_hi = Fraction(1)
        for j in range(x):
            lo, hi = bilinear_range("alpha", j)
            numerator_lo *= lo
            numerator_hi *= hi
        for j in range(r - x):
            lo, hi = bilinear_range("beta", j)
            numerator_lo *= lo
            numerator_hi *= hi

        denominator_lo = Fraction(1)
        denominator_hi = Fraction(1)
        for j in range(r):
            values = (t_lo + j * (1 - t_lo), t_hi + j * (1 - t_hi))
            denominator_lo *= min(values)
            denominator_hi *= max(values)

        combinatorial = Fraction(comb(r, x))
        probability_lo = combinatorial * numerator_lo / denominator_hi
        probability_hi = combinatorial * numerator_hi / denominator_lo
        # Every beta-binomial outcome probability is in [0, 1]. The
        # rectangular numerator/denominator enclosure can be wider than that
        # simplex constraint, so intersect its upper endpoint with the exact
        # universal probability bound before fixed-point rounding.
        probability = (
            floor_scaled(probability_lo),
            ceil_scaled(min(Fraction(1), probability_hi)),
        )
        likelihood = multiply_interval(
            likelihood,
            power_interval(probability, multiplicity),
        )

    return {
        "status": "EXACT_RATIONAL_LIKELIHOOD_ENCLOSURE",
        "likelihood_bounds": (
            Fraction(likelihood[0], scale),
            Fraction(likelihood[1], scale),
        ),
        "max_fraction_bits": max_fraction_bits,
        "accumulator": "OUTWARD_ROUNDED_DYADIC_FIXED_POINT",
        "precision_bits": precision,
    }


def _f5_input_provenance(
    r: int,
    count_histogram: Mapping[int, int],
    source_revision: str | None,
) -> dict[str, object]:
    """Bind an F5 certificate to exact input, score polynomials and source SHA."""
    import hashlib
    import json
    import os
    import re

    revision = source_revision or os.environ.get("GITHUB_SHA")
    if not isinstance(revision, str) or re.fullmatch(r"[0-9a-fA-F]{40}", revision) is None:
        raise ValueError("SOURCE_REVISION_MUST_BE_40_HEX_SHA")
    revision = revision.lower()

    score_mu, score_kappa = beta_binomial_score_numerators(r, count_histogram)
    compact_mu = compactify_concentration(score_mu)
    compact_kappa = compactify_concentration(score_kappa)
    normalized_histogram = sorted(
        (x, n) for x, n in count_histogram.items() if n
    )

    def digest(value) -> str:
        payload = json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
        ).encode("ascii")
        return hashlib.sha256(payload).hexdigest()

    def polynomial_payload(poly: Poly):
        return [[i, j, coefficient] for (i, j), coefficient in sorted(poly.items())]

    return {
        "schema": "TGCV-C10-S-F5-INPUT-PROVENANCE-001",
        "source_revision": revision,
        "r": r,
        "sample_size": sum(n for _, n in normalized_histogram),
        "pooled_successes": sum(x * n for x, n in normalized_histogram),
        "histogram_sha256": digest({
            "r": r,
            "histogram": normalized_histogram,
        }),
        "score_numerator_sha256": {
            "mu": digest(polynomial_payload(score_mu)),
            "kappa": digest(polynomial_payload(score_kappa)),
        },
        "compactified_score_numerator_sha256": {
            "mu": digest(polynomial_payload(compact_mu)),
            "kappa": digest(polynomial_payload(compact_kappa)),
        },
        "hash_algorithm": "SHA256_CANONICAL_JSON",
    }


def beta_binomial_global_mle_certificate(
    r: int,
    count_histogram: Mapping[int, int],
    *,
    max_refinements: int = 3,
    projection_bits: int = 16,
    max_projection_depth: int = 64,
    max_projection_intervals: int = 10000,
    max_lift_intervals: int = 256,
    max_lift_depth: int = 24,
    max_mu_depth: int = 12,
    max_fraction_bits: int = 200000,
    source_revision: str | None = None,
) -> dict[str, object]:
    """Certify the global beta-binomial likelihood winner or explicitly abstain.

    This is the final comparison layer over the integrated stationary/boundary
    census. Interior candidates are bounded with exact rational likelihood
    intervals; boundary profiles are exact rational values. A winner is
    reported only when its lower bound strictly exceeds every competitor's
    upper bound. Otherwise the concentration projection/lift is refined up to
    the deterministic budget and the operation returns an unresolved state.
    """
    from fractions import Fraction

    if type(max_refinements) is not int or max_refinements < 0:
        raise ValueError("MAX_REFINEMENTS_MUST_BE_NONNEGATIVE_INTEGER")
    if type(projection_bits) is not int or projection_bits < 4:
        raise ValueError("PROJECTION_BITS_MUST_BE_INTEGER_AT_LEAST_4")
    if type(max_fraction_bits) is not int or max_fraction_bits < 64:
        raise ValueError("MAX_FRACTION_BITS_MUST_BE_INTEGER_AT_LEAST_64")
    _validate_f5_census_budgets(
        max_projection_depth=max_projection_depth,
        max_projection_intervals=max_projection_intervals,
        max_lift_intervals=max_lift_intervals,
        max_lift_depth=max_lift_depth,
        max_mu_depth=max_mu_depth,
    )
    input_provenance = _f5_input_provenance(
        r, count_histogram, source_revision
    )

    history = []
    for refinement in range(max_refinements + 1):
        census = beta_binomial_compactified_stationary_census(
            r, count_histogram,
            projection_width=Fraction(1, 2 ** (projection_bits + 4 * refinement)),
            max_projection_depth=max_projection_depth + 8 * refinement,
            max_projection_intervals=max_projection_intervals,
            max_lift_intervals=max_lift_intervals,
            max_lift_depth=max_lift_depth + 4 * refinement,
            max_mu_depth=max_mu_depth,
        )
        census["input_provenance"] = input_provenance
        history.append({
            "refinement": refinement,
            "projection_width": Fraction(1, 2 ** (projection_bits + 4 * refinement)),
            "census_status": census["status"],
        })

        if census["status"] not in {
            "INTERIOR_SIMPLE_ROOT_AND_BOUNDARY_CENSUS_COMPLETE",
            "NO_INTERIOR_MEAN_ROOT_DEGENERATE_DATA",
        }:
            if census["status"] == "INCOMPLETE_COMMON_COMPONENT":
                disposition = census.get("component_disposition", {})
                typed_status = (
                    "NONISOLATED_STATIONARY_SET"
                    if disposition.get("status") == "REAL_INTERIOR_AXIS_COMMON_COMPONENT_UNRESOLVED"
                    else "ALGEBRAIC_CERTIFICATE_UNAVAILABLE"
                )
            elif census["status"] == "INCOMPLETE_RESULTANT_OR_COMMON_COMPONENT":
                typed_status = "ALGEBRAIC_CERTIFICATE_UNAVAILABLE"
            elif census["status"] == "INCOMPLETE_BOUNDARY_CENSUS":
                typed_status = "BOUNDARY_SUPREMUM_UNRESOLVED"
            else:
                typed_status = "NUMERICAL_INTERVAL_CERTIFICATE_UNRESOLVED"
            return {
                "status": typed_status,
                "census": census,
                "refinement_history": history,
                "likelihood_ordering": "NOT_PERFORMED",
            }

        competitors = []
        interior_index = 0
        for lift_record in census.get("interior_stationary_candidates", []):
            lift = lift_record["lift_result"]
            for certified in lift["certified_simple_root_intervals"]:
                # The Krawczyk image is a valid (usually tighter) enclosure
                # of the unique root, unlike the full subdivision input box.
                root_box = certified["root_certificate"]["krawczyk_box"]
                enclosure = _beta_binomial_likelihood_enclosure(
                    r, count_histogram,
                    mu_bounds=root_box[0],
                    t_bounds=root_box[1],
                    max_fraction_bits=max_fraction_bits,
                )
                if enclosure["status"] != "EXACT_RATIONAL_LIKELIHOOD_ENCLOSURE":
                    return {
                        "status": "NUMERICAL_INTERVAL_CERTIFICATE_UNRESOLVED",
                        "census": census,
                        "candidate_enclosure": enclosure,
                        "refinement_history": history,
                        "likelihood_ordering": "NOT_CERTIFIED",
                    }
                lower, upper = enclosure["likelihood_bounds"]
                competitors.append({
                    "candidate_id": f"interior-{interior_index}",
                    "kind": "INTERIOR_STATIONARY_ROOT",
                    "parameter_box": root_box,
                    "likelihood_bounds": (lower, upper),
                    "attained_in_open_domain": True,
                })
                interior_index += 1

        for name, record in census["boundary_likelihoods"].items():
            if not isinstance(record, Mapping) or "likelihood" not in record:
                continue
            value = record["likelihood"]
            competitors.append({
                "candidate_id": f"boundary-{name}",
                "kind": "BOUNDARY_SUPREMUM",
                "boundary": name,
                "likelihood_bounds": (value, value),
                "attained_in_open_domain": False,
            })

        if not competitors:
            return {
                "status": "GLOBAL_MAXIMUM_ORDER_UNRESOLVED",
                "census": census,
                "refinement_history": history,
                "competitors": [],
            }

        winners = []
        for index, candidate in enumerate(competitors):
            lower = candidate["likelihood_bounds"][0]
            if all(
                lower > other["likelihood_bounds"][1]
                for j, other in enumerate(competitors) if j != index
            ):
                winners.append(candidate)

        if len(winners) == 1:
            winner = winners[0]
            return {
                "status": (
                    "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED"
                    if winner["kind"] == "INTERIOR_STATIONARY_ROOT"
                    else "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED"
                ),
                "winner": winner,
                "competitors": competitors,
                "census": census,
                "refinement_history": history,
                "ordering_method": "EXACT_RATIONAL_PROBABILITY_INTERVALS",
                "globality_basis": "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS",
            }

        boundary_values = [
            candidate["likelihood_bounds"][0]
            for candidate in competitors
            if candidate["kind"] == "BOUNDARY_SUPREMUM"
        ]
        if boundary_values:
            boundary_max = max(boundary_values)
            top_boundaries = [
                candidate for candidate in competitors
                if candidate["kind"] == "BOUNDARY_SUPREMUM"
                and candidate["likelihood_bounds"][0] == boundary_max
            ]
            interior_upper = max(
                (
                    candidate["likelihood_bounds"][1]
                    for candidate in competitors
                    if candidate["kind"] == "INTERIOR_STATIONARY_ROOT"
                ),
                default=Fraction(0),
            )
            if interior_upper < boundary_max:
                return {
                    "status": (
                        "GLOBAL_CO_MAXIMIZERS_CERTIFIED"
                        if len(top_boundaries) > 1
                        else "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED"
                    ),
                    "winners": top_boundaries,
                    "competitors": competitors,
                    "census": census,
                    "refinement_history": history,
                    "ordering_method": "EXACT_RATIONAL_PROBABILITY_INTERVALS",
                    "globality_basis": "COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS",
                }

    return {
        "status": "GLOBAL_MAXIMUM_ORDER_UNRESOLVED",
        "census": census,
        "competitors": competitors,
        "refinement_history": history,
        "ordering_method": "EXACT_RATIONAL_PROBABILITY_INTERVALS",
        "reason": "INTERVALS_OVERLAP_AFTER_MAXIMUM_DETERMINISTIC_REFINEMENTS",
    }


def _axis_factor_has_open_unit_root(coefficients) -> bool:
    """Use exact Sturm counting to decide whether an axis factor vanishes in (0,1)."""
    from fractions import Fraction

    factor = _uni_monic(coefficients)
    for endpoint in (Fraction(0), Fraction(1)):
        if len(factor) > 1 and _uni_evaluate(factor, endpoint) == 0:
            factor = _uni_divide_linear(factor, endpoint)
    if len(factor) <= 1:
        return False
    sequence = _uni_sturm_sequence(factor)
    return _uni_sturm_root_count(sequence, Fraction(0), Fraction(1)) > 0


def _divide_sparse_by_axis_factor(poly: Poly, axis: str, factor):
    """Divide a sparse bivariate polynomial by an exact univariate axis factor."""
    from fractions import Fraction

    if axis not in ("mu", "t"):
        raise ValueError("AXIS_MUST_BE_MU_OR_T")
    grouped = {}
    for (degree_mu, degree_t), coefficient in poly.items():
        variable_degree = degree_mu if axis == "mu" else degree_t
        other_degree = degree_t if axis == "mu" else degree_mu
        grouped.setdefault(other_degree, {})
        grouped[other_degree][variable_degree] = (
            grouped[other_degree].get(variable_degree, 0) + coefficient
        )
    output = {}
    for other_degree, terms in grouped.items():
        degree = max(terms, default=0)
        coefficients = [Fraction(terms.get(i, 0)) for i in range(degree + 1)]
        quotient, remainder = _uni_divmod(coefficients, factor)
        if not _uni_is_zero(remainder):
            raise ArithmeticError("COMMON_AXIS_FACTOR_DIVISION_NOT_EXACT")
        for variable_degree, coefficient in enumerate(quotient):
            if not coefficient:
                continue
            monomial = (
                (variable_degree, other_degree)
                if axis == "mu" else (other_degree, variable_degree)
            )
            if coefficient.denominator != 1:
                raise ArithmeticError("INTEGER_POLYNOMIAL_QUOTIENT_NOT_INTEGRAL")
            output[monomial] = int(coefficient)
    return output


def _strip_noninterior_axis_common_components(
    poly_p: Poly,
    poly_q: Poly,
    axis_components: Mapping[str, object],
) -> dict[str, object]:
    """Remove common axis factors with no real zero in the open unit domain.

    Factors that vanish at an interior axis coordinate describe a genuine
    common component and remain unresolved. Factors supported only at the
    compactification boundary (or with no real unit-interval zero) do not
    affect the open-domain stationary set and are divided out exactly before
    the interior resultant. Their boundary likelihood is handled separately.
    """
    if axis_components.get("status") == "ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED":
        return {
            "status": "ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED",
            "removed_factors": [],
            "interior_components": [],
        }
    reduced_p = dict(poly_p)
    reduced_q = dict(poly_q)
    removed = []
    interior = []
    for axis, record in axis_components.get("axes", {}).items():
        if record.get("component_type") in {
            "NO_AXIS_ALIGNED_COMMON_COMPONENT",
            None,
        }:
            continue
        for factor_record in record.get("squarefree_factors", []):
            factor = tuple(factor_record["coefficients"])
            multiplicity = factor_record["multiplicity"]
            if _axis_factor_has_open_unit_root(factor):
                interior.append({
                    "axis": axis,
                    "factor": factor,
                    "multiplicity": multiplicity,
                    "status": "REAL_COMMON_COMPONENT_INTERSECTS_OPEN_DOMAIN",
                })
                continue
            for _ in range(multiplicity):
                reduced_p = _divide_sparse_by_axis_factor(reduced_p, axis, factor)
                reduced_q = _divide_sparse_by_axis_factor(reduced_q, axis, factor)
            removed.append({
                "axis": axis,
                "factor": factor,
                "multiplicity": multiplicity,
                "status": "COMMON_FACTOR_REMOVED_FROM_OPEN_DOMAIN_CENSUS",
            })
    if interior:
        return {
            "status": "REAL_INTERIOR_AXIS_COMMON_COMPONENT_UNRESOLVED",
            "removed_factors": removed,
            "interior_components": interior,
        }
    return {
        "status": "NO_REAL_INTERIOR_AXIS_COMMON_COMPONENT",
        "poly_p": reduced_p,
        "poly_q": reduced_q,
        "removed_factors": removed,
        "interior_components": [],
    }


def _strip_axis_content_factors_outside_open_unit_domain(
    poly_p: Poly, poly_q: Poly
) -> dict[str, object]:
    """Strip per-score axis factors that never vanish in the open unit square.

    Compactification and denominator clearing can leave factors supported at
    mu/t endpoints. Such factors are nonzero throughout the open parameter
    domain and may be divided out of each score separately without changing
    its interior zero set. Factors with any real root in (0,1) are retained.
    """
    from fractions import Fraction

    reduced = {"P": dict(poly_p), "Q": dict(poly_q)}
    removed = []
    retained_interior = []
    for label in ("P", "Q"):
        for axis in ("mu", "t"):
            content = _bivariate_axis_content(reduced[label], axis)
            if _uni_is_zero(content):
                return {
                    "status": "ZERO_SCORE_POLYNOMIAL_UNRESOLVED",
                    "removed_factors": removed,
                    "interior_factors": retained_interior,
                }
            for factor_record in _uni_squarefree_factors(content):
                factor = _uni_monic(factor_record["coefficients"])
                multiplicity = factor_record["multiplicity"]
                original_factor = tuple(factor)
                for endpoint in (Fraction(0), Fraction(1)):
                    if len(factor) > 1 and _uni_evaluate(factor, endpoint) == 0:
                        linear = [-endpoint, Fraction(1)]
                        linear_sign = 1 if _uni_evaluate(linear, Fraction(1, 2)) > 0 else -1
                        for _ in range(multiplicity):
                            reduced[label] = _divide_sparse_by_axis_factor(
                                reduced[label], axis, linear
                            )
                        if linear_sign < 0 and multiplicity % 2:
                            reduced[label] = {monomial: -value for monomial, value in reduced[label].items()}
                        factor = _uni_divide_linear(factor, endpoint)
                        removed.append({
                            "polynomial": label,
                            "axis": axis,
                            "factor": tuple(linear),
                            "multiplicity": multiplicity,
                            "reason": "COMPACTIFICATION_ENDPOINT_FACTOR",
                        })
                if len(factor) <= 1:
                    continue
                if _axis_factor_has_open_unit_root(factor):
                    retained_interior.append({
                        "polynomial": label,
                        "axis": axis,
                        "factor": tuple(factor),
                        "multiplicity": multiplicity,
                        "status": "REAL_INTERIOR_AXIS_FACTOR_RETAINED",
                    })
                    continue
                factor_sign = 1 if _uni_evaluate(factor, Fraction(1, 2)) > 0 else -1
                for _ in range(multiplicity):
                    reduced[label] = _divide_sparse_by_axis_factor(
                        reduced[label], axis, factor
                    )
                if factor_sign < 0 and multiplicity % 2:
                    reduced[label] = {monomial: -value for monomial, value in reduced[label].items()}
                removed.append({
                    "polynomial": label,
                    "axis": axis,
                    "factor": tuple(factor),
                    "multiplicity": multiplicity,
                    "reason": "NO_REAL_ZERO_IN_OPEN_UNIT_INTERVAL",
                })
    return {
        "status": "NO_REAL_INTERIOR_AXIS_CONTENT_FACTORS",
        "poly_p": reduced["P"],
        "poly_q": reduced["Q"],
        "removed_factors": removed,
        "interior_factors": retained_interior,
    }
