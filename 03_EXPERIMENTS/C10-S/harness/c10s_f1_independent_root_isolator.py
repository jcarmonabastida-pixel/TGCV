"""Independent exact-rational real-root isolator for low-degree polynomials.

Research-only reference implementation. Coefficients are supplied in ascending
power order. Integers and Fractions are exact; floats are converted to the
exact rational represented by that binary float (not to an inferred
measurement interval). No floating-point root finding is used.

The returned rational intervals certify roots of that exact rational
polynomial. They do not certify uncertain/original coefficients; callers must
handle coefficient uncertainty separately.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence


Q = Fraction
Poly = tuple[Q, ...]


@dataclass(frozen=True)
class IsolatedRoot:
    lower: Q
    upper: Q
    multiplicity: int
    distinct_root_count: int = 1


@dataclass(frozen=True)
class RootIsolationResult:
    status: str
    degree: int
    roots: tuple[IsolatedRoot, ...]
    coefficient_semantics: str = "EXACT_RATIONALIZATION_OF_INPUT_VALUES"


def _trim(p: Sequence[Q]) -> Poly:
    values = list(p)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [Q(0)])


def _derivative(p: Poly) -> Poly:
    if len(p) <= 1:
        return (Q(0),)
    return _trim(tuple(Q(i) * p[i] for i in range(1, len(p))))


def _eval(p: Poly, x: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def _divmod_poly(a: Poly, b: Poly) -> tuple[Poly, Poly]:
    if b == (Q(0),):
        raise ZeroDivisionError("POLYNOMIAL_DIVISION_BY_ZERO")
    rem = list(a)
    quotient = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(rem) >= len(b) and any(rem):
        shift = len(rem) - len(b)
        factor = rem[-1] / b[-1]
        quotient[shift] = factor
        for i, value in enumerate(b):
            rem[shift + i] -= factor * value
        while len(rem) > 1 and rem[-1] == 0:
            rem.pop()
    return _trim(quotient), _trim(rem)


def _monic(p: Poly) -> Poly:
    if p == (Q(0),):
        return p
    lead = p[-1]
    return _trim(tuple(v / lead for v in p))


def _gcd(a: Poly, b: Poly) -> Poly:
    x, y = a, b
    while y != (Q(0),):
        _, r = _divmod_poly(x, y)
        x, y = y, r
    return _monic(x)


def _square_free_factors(p: Poly) -> tuple[tuple[Poly, int], ...]:
    """Yun square-free decomposition over Q; returns (factor, multiplicity)."""
    f = _monic(p)
    if len(f) <= 1:
        return ()
    c = _gcd(f, _derivative(f))
    w, rem = _divmod_poly(f, c)
    if rem != (Q(0),):
        raise ArithmeticError("SQUARE_FREE_DECOMPOSITION_FAILED")
    multiplicity = 1
    factors: list[tuple[Poly, int]] = []
    while w != (Q(1),):
        y = _gcd(w, c)
        z, rem = _divmod_poly(w, y)
        if rem != (Q(0),):
            raise ArithmeticError("SQUARE_FREE_FACTOR_DIVISION_FAILED")
        if len(z) > 1:
            factors.append((_monic(z), multiplicity))
        w = y
        c, rem = _divmod_poly(c, y)
        if rem != (Q(0),):
            raise ArithmeticError("SQUARE_FREE_REMAINDER_FAILED")
        multiplicity += 1
        if multiplicity > len(f):
            raise ArithmeticError("SQUARE_FREE_DECOMPOSITION_DID_NOT_TERMINATE")
    return tuple(factors)


def _sturm_sequence(p: Poly) -> tuple[Poly, ...]:
    seq = [p, _derivative(p)]
    while seq[-1] != (Q(0),):
        _, remainder = _divmod_poly(seq[-2], seq[-1])
        if remainder == (Q(0),):
            break
        seq.append(_trim(tuple(-v for v in remainder)))
    return tuple(seq)


def _variations_at(seq: tuple[Poly, ...], x: Q) -> int:
    signs: list[int] = []
    for p in seq:
        value = _eval(p, x)
        if value:
            signs.append(1 if value > 0 else -1)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def _root_count(seq: tuple[Poly, ...], a: Q, b: Q) -> int:
    # All callers ensure neither endpoint is a root of the square-free factor.
    return _variations_at(seq, a) - _variations_at(seq, b)


def _cauchy_bound(p: Poly) -> Q:
    lead = abs(p[-1])
    bound = Q(1) + max((abs(v) / lead for v in p[:-1]), default=Q(0))
    return Q((bound.numerator + bound.denominator - 1) // bound.denominator)


def _nonroot_split(p: Poly, a: Q, b: Q) -> Q:
    # Deterministically avoid rational roots at the subdivision point.
    for denominator in range(2, 258):
        x = a + (b - a) / denominator
        if a < x < b and _eval(p, x) != 0:
            return x
    raise ArithmeticError("NO_NONROOT_RATIONAL_SPLIT_FOUND")


def _isolate_square_free(
    p: Poly, multiplicity: int, *, lower: Q, upper: Q,
    max_depth: int, max_width: Q,
) -> list[IsolatedRoot]:
    seq = _sturm_sequence(p)
    roots: list[IsolatedRoot] = []

    # Include exact roots at domain boundaries, then divide them out.
    work = p
    for endpoint in (lower, upper):
        if len(work) > 1 and _eval(work, endpoint) == 0:
            roots.append(IsolatedRoot(endpoint, endpoint, multiplicity))
            quotient, remainder = _divmod_poly(work, (-endpoint, Q(1)))
            if remainder != (Q(0),):
                raise ArithmeticError("EXACT_ENDPOINT_ROOT_DIVISION_FAILED")
            work = quotient
    if len(work) <= 1:
        return roots

    seq = _sturm_sequence(work)
    stack: list[tuple[Q, Q, int, int]] = []
    a, b = lower, upper
    if _eval(work, a) == 0 or _eval(work, b) == 0:
        raise ArithmeticError("ENDPOINT_ROOT_REMAINS_AFTER_EXTRACTION")
    count = _root_count(seq, a, b)
    if count:
        stack.append((a, b, count, 0))

    while stack:
        left, right, count, depth = stack.pop()
        if count == 1 and right - left <= max_width:
            roots.append(IsolatedRoot(left, right, multiplicity))
            continue
        if depth >= max_depth:
            raise TimeoutError("ROOT_ISOLATION_MAX_DEPTH_EXCEEDED")
        split = _nonroot_split(work, left, right)
        left_count = _root_count(seq, left, split)
        right_count = _root_count(seq, split, right)
        if left_count + right_count != count:
            raise ArithmeticError("STURM_ROOT_COUNT_NOT_CONSERVED")
        if right_count:
            stack.append((split, right, right_count, depth + 1))
        if left_count:
            stack.append((left, split, left_count, depth + 1))
    return roots


def isolate_real_roots(
    coefficients_ascending: Sequence[int | float | Fraction],
    *,
    lower: int | float | Fraction = 0,
    upper: int | float | Fraction | None = None,
    max_depth: int = 256,
    max_width: int | float | Fraction = Fraction(1, 10**12),
) -> RootIsolationResult:
    """Certify all distinct real roots in [lower, upper] using rational Sturm intervals.

    The default domain is [0, +infinity), matching positive-root use cases.
    For a finite domain, both endpoints are included. Exact endpoint roots are
    represented by singleton intervals. If the requested separation cannot be
    achieved within max_depth, status is ROOTS_UNRESOLVED and no partial
    certificate is returned.
    """
    if not coefficients_ascending:
        raise ValueError("POLYNOMIAL_COEFFICIENTS_REQUIRED")
    if type(max_depth) is not int or max_depth < 1:
        raise ValueError("MAX_DEPTH_MUST_BE_POSITIVE_INTEGER")

    def rational(value: int | float | Fraction) -> Q:
        if isinstance(value, bool) or not isinstance(value, (int, float, Fraction)):
            raise ValueError("COEFFICIENTS_AND_BOUNDS_MUST_BE_REAL_NUMBERS")
        if isinstance(value, float):
            if value != value or value in (float("inf"), float("-inf")):
                raise ValueError("NONFINITE_FLOAT_INPUT")
            return Q.from_float(value)
        return Q(value)

    p = _trim(tuple(rational(v) for v in coefficients_ascending))
    degree = len(p) - 1
    if p == (Q(0),):
        # The zero polynomial vanishes everywhere; it has no finite root
        # list and must never be reported as an ordinary root-free constant.
        return RootIsolationResult("IDENTICALLY_ZERO_POLYNOMIAL_UNRESOLVED", 0, ())
    if degree > 3:
        raise ValueError("POLYNOMIAL_DEGREE_EXCEEDS_THREE")
    if degree < 1:
        return RootIsolationResult("NO_ROOTS_CONSTANT_POLYNOMIAL", degree, ())
    lo = rational(lower)
    width = rational(max_width)
    if width <= 0:
        raise ValueError("MAX_WIDTH_MUST_BE_POSITIVE")
    hi = rational(upper) if upper is not None else _cauchy_bound(p)
    if hi <= lo:
        raise ValueError("UPPER_BOUND_MUST_EXCEED_LOWER_BOUND")

    try:
        isolated: list[IsolatedRoot] = []
        for factor, multiplicity in _square_free_factors(p):
            factor_hi = hi
            # Cauchy bound for the factor, clipped to the caller's finite bound.
            if upper is None:
                factor_hi = max(hi, _cauchy_bound(factor))
            isolated.extend(_isolate_square_free(
                factor, multiplicity, lower=lo, upper=factor_hi,
                max_depth=max_depth, max_width=width,
            ))
        isolated.sort(key=lambda item: (item.lower, item.upper))
        # Independent square-free factors cannot share roots; reject overlap as
        # a defensive invariant rather than merging uncertain certificates.
        for left, right in zip(isolated, isolated[1:]):
            if left.upper >= right.lower:
                raise ArithmeticError("ROOT_INTERVALS_NOT_DISJOINT")
        return RootIsolationResult("ROOTS_ISOLATED", degree, tuple(isolated))
    except (TimeoutError, ArithmeticError):
        return RootIsolationResult("ROOTS_UNRESOLVED", degree, ())
