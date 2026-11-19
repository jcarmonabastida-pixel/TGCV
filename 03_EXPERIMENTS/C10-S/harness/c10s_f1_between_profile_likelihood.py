"""F1 profile likelihood for the between-world variance component.

Research-only numerical inversion. The likelihood-ratio cutoff is supplied by
the caller and is neither selected nor calibrated here. The interval is
obtained by root finding, not by classifying a finite parameter grid.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence
from fractions import Fraction

from scipy.optimize import brentq, minimize_scalar

from c10s_variance_comparison_interface import observed_nested_mr_result


METHOD_ID = "F1_BETWEEN_PROFILE_LIKELIHOOD_0.2"
MODEL_SCOPE = "BALANCED_GAUSSIAN_RANDOM_INTERCEPT"
_LOG2PI = math.log(2.0 * math.pi)


class F1ProfileError(ValueError):
    """Invalid input or numerical profile-likelihood request."""


@dataclass(frozen=True)
class F1NuisanceOptimizerDiagnostic:
    status: str
    bounded_optimizer_loglik: float | None
    independent_loglik: float | None
    absolute_loglik_difference: float | None
    stationary_points: int
    stationary_points_log_scale: tuple[float, ...]
    stationary_point_types: tuple[str, ...]
    tangential_score_roots: int
    unresolved_tangential_candidates: int
    polynomial_degree: int
    polynomial_root_count: int
    polynomial_status: str
    critical_point_solver_status: str
    polynomial_scan_discordant: bool
    independent_boundary_sensitive: bool
    optimizer_error: str | None


@dataclass(frozen=True)
class F1NuisanceStabilityDiagnostic:
    status: str
    configurations: tuple[tuple[int, float], ...]
    stationary_point_counts: tuple[int, ...]
    optimizer_statuses: tuple[str, ...]
    stationary_point_type_signatures: tuple[tuple[str, ...], ...]
    tangential_score_root_counts: tuple[int, ...]
    unresolved_tangential_candidate_counts: tuple[int, ...]
    polynomial_degrees: tuple[int, ...]
    polynomial_root_counts: tuple[int, ...]
    polynomial_statuses: tuple[str, ...]
    critical_point_solver_statuses: tuple[str, ...]
    polynomial_scan_discordances: tuple[bool, ...]
    maximum_loglik_spread: float | None
    maximum_stationary_location_spread: float | None


@dataclass(frozen=True)
class F1ProfileSet:
    likelihood_ratio_cutoff: float
    mle_between_variance: float
    max_profile_loglik: float
    confidence_components: tuple[tuple[float, float], ...]
    lower_boundary_included: bool
    upper_endpoint_bracket_expansions: int
    status: str
    method_id: str = METHOD_ID


def _sufficient_statistics(rows: Sequence[Sequence[float]]):
    observed = observed_nested_mr_result(rows)
    m, r = len(rows), len(rows[0])
    if m < 3:
        raise F1ProfileError("F1_PROFILE_REQUIRES_M_AT_LEAST_3")
    df_w, df_b = m * (r - 1), m - 1
    ssw = observed.within_estimate * df_w
    s2_means = observed.observed_world_variance
    if ssw <= 0.0:
        raise F1ProfileError(
            "ZERO_WITHIN_SUM_OF_SQUARES_REQUIRES_SEPARATE_BOUNDARY_MODEL"
        )
    if not math.isfinite(ssw) or not math.isfinite(s2_means) or s2_means < 0.0:
        raise F1ProfileError("INVALID_GAUSSIAN_SUFFICIENT_STATISTICS")
    return r, df_w, df_b, ssw, s2_means, observed.within_estimate


def _profile_at_tau(
    tau: float, *, r: int, df_w: int, df_b: int,
    ssw: float, s2_means: float, scale: float,
) -> float:
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("TAU_MUST_BE_FINITE_AND_NONNEGATIVE")

    # Optimize log(sigma_within^2), ensuring positivity over a scale-adaptive
    # interval. Endpoints are included as candidates to avoid trusting a
    # bounded optimizer's interior result without comparison.
    center = max(scale, 1e-300)
    lo, hi = math.log(center) - 36.0, math.log(center) + 36.0

    def negative_loglik(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        if not (s > 0.0 and q > 0.0):
            return math.inf
        ll = (
            -0.5 * df_w * (_LOG2PI + math.log(s))
            -0.5 * ssw / s
            -0.5 * df_b * (_LOG2PI + math.log(q))
            -0.5 * df_b * s2_means / q
        )
        return -ll

    result = minimize_scalar(
        negative_loglik, bounds=(lo, hi), method="bounded",
        options={"xatol": 1e-12, "maxiter": 2000},
    )
    candidates = [(negative_loglik(lo), lo), (negative_loglik(hi), hi)]
    if result.success and math.isfinite(result.fun):
        candidates.append((float(result.fun), float(result.x)))
    best_value, best_log_s = min(candidates)
    if not math.isfinite(best_value):
        raise F1ProfileError("PROFILE_LIKELIHOOD_NONFINITE")
    # A boundary optimum signals that the nuisance-parameter search range was
    # insufficient; fail closed rather than silently returning a false max.
    if best_log_s in (lo, hi):
        raise F1ProfileError("WITHIN_VARIANCE_PROFILE_OPTIMUM_AT_SEARCH_BOUND")
    return -best_value


def f1_profile_loglik(
    rows: Sequence[Sequence[float]], *, between_variance: float,
) -> float:
    """Profile log-likelihood at fixed tau>=0, profiling within variance."""
    if isinstance(between_variance, bool) or not isinstance(between_variance, (int, float)):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_NUMERIC")
    tau = float(between_variance)
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    scale = max(within, s2_means, tau, 1e-12)
    return _profile_at_tau(
        tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
        s2_means=s2_means, scale=scale,
    )


def f1_profile_between_confidence_set(
    rows: Sequence[Sequence[float]], *,
    likelihood_ratio_cutoff: float,
    max_bracket_expansions: int = 80,
) -> F1ProfileSet:
    """Invert the caller-supplied LR rule by bracketing and root finding.

    The profile MLE is max(0, S2(world means)-MSW/R). The lower endpoint is
    zero when zero lies in the LR set; otherwise it is solved between zero and
    the MLE. The upper endpoint is solved after geometric bracket expansion.
    No critical value is selected and no calibration is performed.
    """
    if (isinstance(likelihood_ratio_cutoff, bool)
            or not isinstance(likelihood_ratio_cutoff, (int, float))
            or not math.isfinite(likelihood_ratio_cutoff)
            or likelihood_ratio_cutoff <= 0.0):
        raise F1ProfileError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")
    if type(max_bracket_expansions) is not int or max_bracket_expansions < 1:
        raise F1ProfileError("MAX_BRACKET_EXPANSIONS_MUST_BE_POSITIVE_INTEGER")

    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    tau_hat = max(0.0, s2_means - within / r)
    scale = max(within, s2_means, 1e-12)

    def profile(tau: float) -> float:
        return _profile_at_tau(
            tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
            s2_means=s2_means, scale=max(scale, tau, 1e-12),
        )

    maximum = profile(tau_hat)
    if not math.isfinite(maximum):
        raise F1ProfileError("PROFILE_MLE_NONFINITE")

    def lr_excess(tau: float) -> float:
        value = profile(tau)
        return 2.0 * (maximum - value) - float(likelihood_ratio_cutoff)

    at_zero = lr_excess(0.0)
    lower_included = at_zero <= 0.0
    if lower_included:
        lower = 0.0
    else:
        if tau_hat <= 0.0:
            raise F1ProfileError("INCONSISTENT_PROFILE_MLE_AND_LOWER_ENDPOINT")
        lower = brentq(lr_excess, 0.0, tau_hat, xtol=1e-12, rtol=1e-12)

    step = max(scale, tau_hat, 1e-12)
    upper = max(tau_hat + step, 2.0 * step)
    expansions = 0
    upper_value = lr_excess(upper)
    while upper_value <= 0.0 and expansions < max_bracket_expansions:
        upper *= 2.0
        expansions += 1
        upper_value = lr_excess(upper)
    if upper_value <= 0.0:
        raise F1ProfileError("UPPER_PROFILE_ENDPOINT_NOT_BRACKETED")
    upper_endpoint = brentq(
        lr_excess, tau_hat, upper, xtol=1e-12, rtol=1e-12,
    )
    return F1ProfileSet(
        likelihood_ratio_cutoff=float(likelihood_ratio_cutoff),
        mle_between_variance=tau_hat,
        max_profile_loglik=maximum,
        confidence_components=((lower, upper_endpoint),),
        lower_boundary_included=lower_included,
        upper_endpoint_bracket_expansions=expansions,
        status="PROFILE_LR_INTERVAL_ROOT_SOLVED",
    )


@dataclass(frozen=True)
class F1ScorePolynomialDiagnostic:
    status: str
    degree: int
    coefficients_ascending: tuple[float, ...]
    positive_roots: tuple[float, ...]
    tangential_roots: tuple[float, ...]
    unresolved_critical_candidates: tuple[float, ...]
    critical_point_solver_status: str
    positive_critical_points: tuple[float, ...]


def _fraction_to_finite_float(value: Fraction, label: str) -> float:
    try:
        result = float(value)
    except OverflowError as exc:
        raise F1ProfileError(f"{label}_OVERFLOW") from exc
    if not math.isfinite(result):
        raise F1ProfileError(f"{label}_NONFINITE")
    if value != 0 and result == 0.0:
        raise F1ProfileError(f"{label}_UNDERFLOW")
    return result


def _score_polynomial_coefficients_exact(
    *, r: int, df_w: int, df_b: int,
    ssw: float, s2_means: float, tau: float,
) -> tuple[float, float, float, float]:
    """Construct coefficients exactly from the binary values of the inputs."""
    R = Fraction(r)
    A, B = Fraction(df_w), Fraction(df_b)
    W, M, T = Fraction(ssw), Fraction(s2_means), Fraction(tau)
    exact = (
        W * T * T,
        -A * T * T + 2 * W * T / R,
        -2 * A * T / R + W / (R * R) - B * T / R + B * M / R,
        -(A + B) / (R * R),
    )
    return tuple(
        _fraction_to_finite_float(value, f"SCORE_POLYNOMIAL_COEFFICIENT_{index}")
        for index, value in enumerate(exact)
    )


def _polyval_ascending(coefficients: Sequence[float], value: float) -> float:
    result = 0.0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def _normalize_scaled_polynomial(
    coefficients: Sequence[float], scale: float,
) -> tuple[float, ...]:
    """Apply x=s/scale without silently overflowing or erasing coefficients."""
    if not math.isfinite(scale) or scale <= 0.0:
        raise F1ProfileError("SCORE_POLYNOMIAL_SCALE_INVALID")
    if not coefficients or any(not math.isfinite(value) for value in coefficients):
        raise F1ProfileError("SCORE_POLYNOMIAL_COEFFICIENTS_NONFINITE")

    scaled = []
    scale_power = 1.0
    for index, coefficient in enumerate(coefficients):
        if index:
            scale_power *= scale
            if not math.isfinite(scale_power) or scale_power == 0.0:
                raise F1ProfileError("SCORE_POLYNOMIAL_SCALE_POWER_UNREPRESENTABLE")
        value = coefficient * scale_power
        if not math.isfinite(value):
            raise F1ProfileError("SCORE_POLYNOMIAL_SCALED_COEFFICIENT_OVERFLOW")
        if coefficient != 0.0 and value == 0.0:
            raise F1ProfileError("SCORE_POLYNOMIAL_SCALED_COEFFICIENT_UNDERFLOW")
        scaled.append(value)

    coefficient_scale = max(abs(value) for value in scaled)
    if not math.isfinite(coefficient_scale) or coefficient_scale == 0.0:
        raise F1ProfileError("SCORE_POLYNOMIAL_COEFFICIENT_SCALING_FAILED")
    normalized = tuple(value / coefficient_scale for value in scaled)
    if any(
        original != 0.0 and normalized_value == 0.0
        for original, normalized_value in zip(scaled, normalized)
    ):
        raise F1ProfileError("SCORE_POLYNOMIAL_NORMALIZATION_ERASED_COEFFICIENT")
    return normalized


def _restore_polynomial_scale(
    values: Sequence[float], scale: float, *, label: str,
) -> tuple[float, ...]:
    restored = []
    for value in values:
        result = value * scale
        if value > 0.0 and (result == 0.0 or not math.isfinite(result)):
            raise F1ProfileError(f"{label}_UNREPRESENTABLE")
        restored.append(result)
    return tuple(restored)


def _positive_quadratic_roots_diagnostic(
    a: float, b: float, c: float,
) -> tuple[tuple[float, ...], str]:
    """Stable positive-root solver with an explicit near-zero discriminant state."""
    if not all(math.isfinite(value) for value in (a, b, c)):
        return (), "DISCRIMINANT_UNRESOLVED"
    if a == 0.0:
        if b == 0.0:
            return (), "DEGREE_BELOW_ONE"
        root = -c / b
        if not math.isfinite(root):
            return (), "DISCRIMINANT_UNRESOLVED"
        return ((root,) if root > 0.0 else ()), "RESOLVED"
    b_squared = b * b
    four_ac = 4.0 * a * c
    if not math.isfinite(b_squared) or not math.isfinite(four_ac):
        return (), "DISCRIMINANT_UNRESOLVED"
    discriminant = math.fsum((b_squared, -four_ac))
    error_bound = 16.0 * math.ulp(1.0) * (abs(b_squared) + abs(four_ac))
    if not math.isfinite(discriminant) or not math.isfinite(error_bound):
        return (), "DISCRIMINANT_UNRESOLVED"
    if discriminant < -error_bound:
        return (), "RESOLVED"
    if discriminant != 0.0 and abs(discriminant) <= error_bound:
        return (), "DISCRIMINANT_UNRESOLVED"
    if discriminant == 0.0:
        root = -b / (2.0 * a)
        return ((root,) if root > 0.0 and math.isfinite(root) else ()), "RESOLVED"
    square_root = math.sqrt(discriminant)
    q = -0.5 * (b + math.copysign(square_root, b))
    candidates = (q / a, c / q) if q != 0.0 else (-b / (2.0 * a),)
    return tuple(sorted({
        value for value in candidates
        if value > 0.0 and math.isfinite(value)
    })), "RESOLVED"


def _positive_quadratic_roots(a: float, b: float, c: float) -> tuple[float, ...]:
    roots, _ = _positive_quadratic_roots_diagnostic(a, b, c)
    return roots


def f1_score_polynomial_diagnostic(
    rows: Sequence[Sequence[float]], *, between_variance: float,
    root_tolerance: float = 1e-10,
    unresolved_tolerance: float = 1e-7,
) -> F1ScorePolynomialDiagnostic:
    """Isolate all positive roots of the cubic numerator of the F1 nuisance score.

    For s=within variance, tau=between variance, r=replicates,
    a=df_within, b=df_between, W=SSW and M=variance of world means:
        P(s) = 2*s*(tau+s/r)^2*score(log(s)).
    P is at most cubic. Its positive derivative roots partition the positive
    axis into monotone intervals; each interval contains at most one simple
    root. A zero at a derivative root is a repeated/tangential root.
    """
    if (isinstance(between_variance, bool)
            or not isinstance(between_variance, (int, float))
            or not math.isfinite(between_variance) or between_variance < 0.0):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    if (not math.isfinite(root_tolerance) or root_tolerance <= 0.0
            or not math.isfinite(unresolved_tolerance)
            or unresolved_tolerance < root_tolerance):
        raise F1ProfileError("POLYNOMIAL_ROOT_TOLERANCES_INVALID")

    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    tau = float(between_variance)
    a, b, W, M = float(df_w), float(df_b), float(ssw), float(s2_means)
    coefficients = list(_score_polynomial_coefficients_exact(
        r=r, df_w=df_w, df_b=df_b, ssw=ssw,
        s2_means=s2_means, tau=tau,
    ))
    # At tau=0 the score numerator contains an extraneous s^2 factor.
    while len(coefficients) > 1 and coefficients[0] == 0.0:
        coefficients.pop(0)
    while len(coefficients) > 1 and coefficients[-1] == 0.0:
        coefficients.pop()
    degree = len(coefficients) - 1
    if degree < 1:
        raise F1ProfileError("SCORE_POLYNOMIAL_DEGENERATE")

    if degree == 3:
        derivative_coefficients = (
            3.0 * coefficients[3], 2.0 * coefficients[2], coefficients[1],
        )
        if any(not math.isfinite(value) for value in derivative_coefficients):
            raise F1ProfileError("SCORE_POLYNOMIAL_DERIVATIVE_COEFFICIENTS_NONFINITE")
        critical, critical_status = _positive_quadratic_roots_diagnostic(
            *derivative_coefficients,
        )
    elif degree == 2:
        derivative_coefficients = (0.0, 2.0 * coefficients[2], coefficients[1])
        if any(not math.isfinite(value) for value in derivative_coefficients):
            raise F1ProfileError("SCORE_POLYNOMIAL_DERIVATIVE_COEFFICIENTS_NONFINITE")
        critical, critical_status = _positive_quadratic_roots_diagnostic(
            *derivative_coefficients,
        )
    else:
        critical, critical_status = (), "RESOLVED"
    scale = max(
        within, M, tau, 1e-12,
        *(abs(value) for value in critical),
    )
    normalized = _normalize_scaled_polynomial(coefficients, scale)
    # Evaluate the normalized polynomial in x=s/scale.
    def polynomial_x(x: float) -> float:
        return _polyval_ascending(normalized, x)

    critical_x = tuple(value / scale for value in critical)
    if any(value > 0.0 and (
        scaled == 0.0 or not math.isfinite(scaled)
    ) for value, scaled in zip(critical, critical_x)):
        raise F1ProfileError("SCORE_POLYNOMIAL_CRITICAL_POINT_SCALE_UNREPRESENTABLE")
    critical_x = tuple(sorted(value for value in critical_x if value > 0.0))
    root_x: list[float] = []
    tangent_x: list[float] = []
    unresolved_x: list[float] = []
    for point in critical_x:
        residual = abs(polynomial_x(point))
        magnitude = max(
            1.0,
            sum(abs(coef) * max(1.0, point ** index)
                for index, coef in enumerate(normalized)),
        )
        if residual <= root_tolerance * magnitude:
            tangent_x.append(point)
            root_x.append(point)
        elif residual <= unresolved_tolerance * magnitude:
            unresolved_x.append(point)

    left_points = (0.0,) + critical_x
    right_bound = max(1.0, *(critical_x or ()), within / scale, M / scale, tau / scale)
    right_value = polynomial_x(right_bound)
    expansions = 0
    while right_value == 0.0 or right_value * normalized[-1] < 0.0:
        right_bound *= 2.0
        right_value = polynomial_x(right_bound)
        expansions += 1
        if expansions > 256 or not math.isfinite(right_bound):
            raise F1ProfileError("SCORE_POLYNOMIAL_POSITIVE_ROOT_BOUND_FAILED")
    right_points = critical_x + (right_bound,)
    for left, right in zip(left_points, right_points):
        fl, fr = polynomial_x(left), polynomial_x(right)
        if fl == 0.0:
            continue
        if fl * fr < 0.0:
            root_x.append(brentq(
                polynomial_x, left, right, xtol=1e-13, rtol=1e-13,
            ))
    roots = tuple(sorted(_restore_polynomial_scale(
        tuple(value for value in root_x if value > 0.0), scale,
        label="SCORE_POLYNOMIAL_ROOT_SCALE",
    )))
    tangential = tuple(sorted(_restore_polynomial_scale(
        tangent_x, scale, label="SCORE_POLYNOMIAL_TANGENCY_SCALE",
    )))
    unresolved = tuple(sorted(_restore_polynomial_scale(
        unresolved_x, scale, label="SCORE_POLYNOMIAL_UNRESOLVED_SCALE",
    )))
    status = "POLYNOMIAL_ROOTS_ISOLATED"
    if unresolved or critical_status != "RESOLVED":
        status = "POLYNOMIAL_ROOTS_UNRESOLVED"
    return F1ScorePolynomialDiagnostic(
        status=status,
        degree=degree,
        coefficients_ascending=tuple(coefficients),
        positive_roots=roots,
        tangential_roots=tangential,
        unresolved_critical_candidates=unresolved,
        critical_point_solver_status=critical_status,
        positive_critical_points=tuple(value * scale for value in critical_x),
    )


def _scan_score_stationary_points(
    score, score_derivative, *, lo: float, hi: float,
    grid_points: int, score_tolerance: float = 1e-10,
    near_tangent_tolerance: float = 1e-7,
) -> tuple[tuple[float, ...], tuple[str, ...], int, int]:
    """Find sign-changing score roots and candidate tangential score roots.

    Roots of score are stationary points of the profiled log-likelihood.
    Roots of score_derivative are inspected for even-multiplicity score roots,
    which a sign-change-only scan cannot detect. Near-zero but unconfirmed
    tangencies are counted separately so callers can abstain conservatively.
    """
    xs = [lo + (hi - lo) * i / (grid_points - 1) for i in range(grid_points)]
    score_values = [score(x) for x in xs]
    derivative_values = [score_derivative(x) for x in xs]
    score_scale = max(1.0, *(abs(value) for value in score_values))
    roots: list[tuple[float, str]] = []

    for index, (left, right) in enumerate(zip(xs, xs[1:])):
        fl, fr = score_values[index], score_values[index + 1]
        if fl == 0.0:
            roots.append((left, "CROSSING_CANDIDATE"))
        if fl * fr < 0.0:
            roots.append((
                brentq(score, left, right, xtol=1e-12, rtol=1e-12),
                "CROSSING_CANDIDATE",
            ))
    if score_values[-1] == 0.0:
        roots.append((xs[-1], "CROSSING_CANDIDATE"))

    tangential_count = 0
    unresolved_count = 0
    for index, (left, right) in enumerate(zip(xs, xs[1:])):
        dl, dr = derivative_values[index], derivative_values[index + 1]
        if dl == 0.0:
            candidate = left
        elif dl * dr < 0.0:
            candidate = brentq(
                score_derivative, left, right, xtol=1e-12, rtol=1e-12,
            )
        else:
            continue
        residual = abs(score(candidate))
        if residual <= score_tolerance * score_scale:
            roots.append((candidate, "TANGENTIAL_SCORE_ROOT"))
            tangential_count += 1
        elif residual <= near_tangent_tolerance * score_scale:
            unresolved_count += 1

    roots.sort(key=lambda item: item[0])
    unique: list[tuple[float, str]] = []
    for location, kind in roots:
        if unique and abs(location - unique[-1][0]) <= 1e-8:
            if kind == "TANGENTIAL_SCORE_ROOT":
                unique[-1] = (location, kind)
            continue
        unique.append((location, kind))

    delta = max(1e-7, (hi - lo) * 1e-7)
    classified = []
    for location, kind in unique:
        left_value = score(max(lo, location - delta))
        right_value = score(min(hi, location + delta))
        if kind == "TANGENTIAL_SCORE_ROOT" or left_value * right_value > 0.0:
            classified.append("TANGENTIAL_STATIONARY_NO_LOCAL_EXTREMUM")
        elif left_value > 0.0 > right_value:
            classified.append("LOCAL_MAXIMUM")
        elif left_value < 0.0 < right_value:
            classified.append("LOCAL_MINIMUM")
        else:
            classified.append("STATIONARY_TYPE_UNRESOLVED")
    return (
        tuple(location for location, _ in unique),
        tuple(classified),
        tangential_count,
        unresolved_count,
    )


def f1_profile_nuisance_optimizer_diagnostic(
    rows: Sequence[Sequence[float]], *, between_variance: float,
    grid_points: int = 241, log_span: float = 36.0,
    loglik_tolerance: float = 1e-7,
) -> F1NuisanceOptimizerDiagnostic:
    """Compare the production bounded optimizer with an independent score-root scan.

    The independent route scans the nuisance score over log(within variance),
    brackets every detected sign change, solves each stationary point, and
    compares their likelihoods with the bounded production optimizer. This is
    a numerical diagnostic only: it does not select an LR cutoff or certify
    interval coverage.
    """
    if isinstance(between_variance, bool) or not isinstance(between_variance, (int, float)):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_NUMERIC")
    tau = float(between_variance)
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    if type(grid_points) is not int or grid_points < 41:
        raise F1ProfileError("NUISANCE_GRID_POINTS_MUST_BE_INTEGER_GE_41")
    if (isinstance(log_span, bool) or not isinstance(log_span, (int, float))
            or not math.isfinite(log_span) or log_span <= 0.0):
        raise F1ProfileError("NUISANCE_LOG_SPAN_MUST_BE_FINITE_AND_POSITIVE")
    if (isinstance(loglik_tolerance, bool)
            or not isinstance(loglik_tolerance, (int, float))
            or not math.isfinite(loglik_tolerance) or loglik_tolerance <= 0.0):
        raise F1ProfileError("NUISANCE_LOGLIK_TOLERANCE_MUST_BE_FINITE_AND_POSITIVE")

    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    scale = max(within, s2_means, tau, 1e-12)
    center = max(scale, 1e-300)
    lo, hi = math.log(center) - float(log_span), math.log(center) + float(log_span)

    def loglik(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        return (
            -0.5 * df_w * (_LOG2PI + log_s)
            -0.5 * ssw / s
            -0.5 * df_b * (_LOG2PI + math.log(q))
            -0.5 * df_b * s2_means / q
        )

    def score(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        return (
            -0.5 * df_w + 0.5 * ssw / s
            -0.5 * df_b * (s / r) / q
            +0.5 * df_b * s2_means * (s / r) / (q * q)
        )

    def score_derivative(log_s: float) -> float:
        s = math.exp(log_s)
        u = s / r
        q = tau + u
        return (
            -0.5 * ssw / s
            -0.5 * df_b * u * tau / (q * q)
            +0.5 * df_b * s2_means * u * (tau - u) / (q * q * q)
        )

    scanned_roots, scanned_types, scanned_tangencies, unresolved_tangencies = (
        _scan_score_stationary_points(
            score, score_derivative, lo=lo, hi=hi,
            grid_points=grid_points,
        )
    )
    polynomial = f1_score_polynomial_diagnostic(
        rows, between_variance=tau,
    )
    roots = tuple(math.log(value) for value in polynomial.positive_roots)
    tangential_logs = tuple(math.log(value) for value in polynomial.tangential_roots)
    root_types_list = []
    for root in roots:
        if any(abs(root - candidate) <= 1e-7 for candidate in tangential_logs):
            root_types_list.append("TANGENTIAL_STATIONARY_NO_LOCAL_EXTREMUM")
            continue
        delta = max(1e-7, (hi - lo) * 1e-7)
        left_score = score(max(lo, root - delta))
        right_score = score(min(hi, root + delta))
        if left_score > 0.0 > right_score:
            root_types_list.append("LOCAL_MAXIMUM")
        elif left_score < 0.0 < right_score:
            root_types_list.append("LOCAL_MINIMUM")
        else:
            root_types_list.append("STATIONARY_TYPE_UNRESOLVED")
    root_types = tuple(root_types_list)
    tangential_count = len(polynomial.tangential_roots)
    polynomial_scan_discordant = (
        len(scanned_roots) != len(roots)
        or any(
            min((abs(value - root) for root in roots), default=math.inf) > 1e-5
            for value in scanned_roots
        )
    )
    if polynomial.status == "POLYNOMIAL_ROOTS_UNRESOLVED":
        unresolved_tangencies += len(polynomial.unresolved_critical_candidates)
    candidates = [(loglik(value), value) for value in roots]
    if not candidates:
        independent_value = None
        independent_boundary = True
    else:
        independent_value, independent_arg = max(candidates)
        independent_boundary = (
            independent_arg - lo <= 1e-7 or hi - independent_arg <= 1e-7
        )

    try:
        bounded_value = _profile_at_tau(
            tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
            s2_means=s2_means, scale=scale,
        )
        optimizer_error = None
    except F1ProfileError as exc:
        bounded_value = None
        optimizer_error = str(exc)

    if (bounded_value is None or independent_value is None
            or unresolved_tangencies > 0
            or "STATIONARY_TYPE_UNRESOLVED" in root_types
            or polynomial.status == "POLYNOMIAL_ROOTS_UNRESOLVED"):

        status = "OPTIMIZATION_INSUFFICIENT"
        difference = None
    else:
        difference = abs(bounded_value - independent_value)
        if independent_boundary:
            status = "OPTIMIZATION_BOUNDARY_SENSITIVE"
        elif polynomial_scan_discordant or difference > float(loglik_tolerance):
            status = "OPTIMIZATION_DISCORDANT"
        else:
            status = "OPTIMIZATION_CONCORDANT"

    return F1NuisanceOptimizerDiagnostic(
        status=status,
        bounded_optimizer_loglik=bounded_value,
        independent_loglik=independent_value,
        absolute_loglik_difference=difference,
        stationary_points=len(roots),
        stationary_points_log_scale=tuple(roots),
        stationary_point_types=root_types,
        tangential_score_roots=tangential_count,
        unresolved_tangential_candidates=unresolved_tangencies,
        polynomial_degree=polynomial.degree,
        polynomial_root_count=len(polynomial.positive_roots),
        polynomial_status=polynomial.status,
        critical_point_solver_status=polynomial.critical_point_solver_status,
        polynomial_scan_discordant=polynomial_scan_discordant,
        independent_boundary_sensitive=independent_boundary,
        optimizer_error=optimizer_error,
    )


def f1_profile_nuisance_stability_diagnostic(
    rows: Sequence[Sequence[float]], *, between_variance: float,
    grid_resolutions: Sequence[int] = (241, 481, 961),
    log_spans: Sequence[float] = (30.0, 36.0, 42.0),
    loglik_tolerance: float = 1e-7,
) -> F1NuisanceStabilityDiagnostic:
    """Cross-check nuisance score-root diagnostics across grids and log spans.

    Concordance means only that this finite family of scans found the same
    number of sign-changing stationary roots, no boundary/insufficient status,
    and a sufficiently small spread in the best stationary log-likelihood.
    It cannot detect every even-multiplicity score root or prove globality.
    """
    grids = tuple(grid_resolutions)
    spans = tuple(float(value) for value in log_spans)
    if not grids or any(type(value) is not int or value < 41 for value in grids):
        raise F1ProfileError("NUISANCE_GRID_RESOLUTIONS_MUST_BE_INTEGER_GE_41")
    if not spans or any(not math.isfinite(value) or value <= 0.0 for value in spans):
        raise F1ProfileError("NUISANCE_LOG_SPANS_MUST_BE_FINITE_AND_POSITIVE")
    if (isinstance(loglik_tolerance, bool)
            or not isinstance(loglik_tolerance, (int, float))
            or not math.isfinite(loglik_tolerance) or loglik_tolerance <= 0.0):
        raise F1ProfileError("NUISANCE_LOGLIK_TOLERANCE_MUST_BE_FINITE_AND_POSITIVE")

    configurations = tuple((grid, span) for span in spans for grid in grids)
    results = tuple(
        f1_profile_nuisance_optimizer_diagnostic(
            rows, between_variance=between_variance,
            grid_points=grid, log_span=span,
            loglik_tolerance=float(loglik_tolerance),
        )
        for grid, span in configurations
    )
    counts = tuple(item.stationary_points for item in results)
    statuses = tuple(item.status for item in results)
    type_signatures = tuple(item.stationary_point_types for item in results)
    tangential_counts = tuple(item.tangential_score_roots for item in results)
    unresolved_counts = tuple(item.unresolved_tangential_candidates for item in results)
    polynomial_degrees = tuple(item.polynomial_degree for item in results)
    polynomial_root_counts = tuple(item.polynomial_root_count for item in results)
    polynomial_statuses = tuple(item.polynomial_status for item in results)
    critical_statuses = tuple(item.critical_point_solver_status for item in results)
    polynomial_scan_discordances = tuple(item.polynomial_scan_discordant for item in results)
    values = tuple(
        item.independent_loglik for item in results
        if item.independent_loglik is not None
    )
    spread = max(values) - min(values) if len(values) == len(results) and values else None
    if len(set(counts)) == 1 and counts and counts[0] > 0:
        root_locations = tuple(
            tuple(item.stationary_points_log_scale[index] for item in results)
            for index in range(counts[0])
        )
        location_spread = max(
            max(locations) - min(locations) for locations in root_locations
        )
    elif counts and all(value == 0 for value in counts):
        location_spread = 0.0
    else:
        location_spread = None

    if any(status == "OPTIMIZATION_INSUFFICIENT" for status in statuses):
        status = "OPTIMIZATION_INSUFFICIENT"
    elif any(status == "OPTIMIZATION_BOUNDARY_SENSITIVE" for status in statuses):
        status = "OPTIMIZATION_BOUNDARY_SENSITIVE"
    elif (len(set(counts)) != 1
          or len(set(type_signatures)) != 1
          or len(set(tangential_counts)) != 1
          or len(set(polynomial_root_counts)) != 1
          or len(set(polynomial_statuses)) != 1
          or len(set(critical_statuses)) != 1
          or any(value != "POLYNOMIAL_ROOTS_ISOLATED" for value in polynomial_statuses)
          or any(polynomial_scan_discordances)):
        status = "OPTIMIZATION_DISCORDANT"
    elif (spread is None or spread > float(loglik_tolerance)
          or location_spread is None or location_spread > 1e-5):
        status = "OPTIMIZATION_DISCORDANT"
    elif any(status == "OPTIMIZATION_DISCORDANT" for status in statuses):
        status = "OPTIMIZATION_DISCORDANT"
    else:
        status = "OPTIMIZATION_CONCORDANT"

    return F1NuisanceStabilityDiagnostic(
        status=status,
        configurations=configurations,
        stationary_point_counts=counts,
        optimizer_statuses=statuses,
        stationary_point_type_signatures=type_signatures,
        tangential_score_root_counts=tangential_counts,
        unresolved_tangential_candidate_counts=unresolved_counts,
        polynomial_degrees=polynomial_degrees,
        polynomial_root_counts=polynomial_root_counts,
        polynomial_statuses=polynomial_statuses,
        critical_point_solver_statuses=critical_statuses,
        polynomial_scan_discordances=polynomial_scan_discordances,
        maximum_loglik_spread=spread,
        maximum_stationary_location_spread=location_spread,
    )
