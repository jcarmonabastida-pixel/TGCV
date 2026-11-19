"""F5 beta-binomial profile likelihood for the scalar target MCSE.

Research-only profile evaluator. Both mean branches and analytic concentration
limits are represented. It does not select/calibrate an LR cutoff or claim
uniform coverage. The finite-concentration maximization is diagnostic and
must pass the separately specified adversarial numerical checks.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import betaln, gammaln


METHOD_ID = "F5_BETA_BINOMIAL_MCSE_PROFILE_0.1"


class F5ProfileError(ValueError):
    """Invalid target, count data, or profile-likelihood computation."""


@dataclass(frozen=True)
class F5ProfileConfidenceSet:
    likelihood_ratio_cutoff: float
    unrestricted_profile_loglik: float
    confidence_components: tuple[tuple[float, float], ...]
    confidence_hull: tuple[float, float] | None
    scan_grid_points: int
    status: str
    method_id: str = METHOD_ID


@dataclass(frozen=True)
class F5ProfileResult:
    target_mcse: float
    profile_loglik: float
    maximizing_branch: str
    maximizing_concentration: float | None
    boundary_status: str
    branch_loglik_plus: float
    branch_loglik_minus: float
    optimizer_diagnostics: tuple[tuple[str, str], ...]
    method_id: str = METHOD_ID


def _counts_and_validate(rows: Sequence[Sequence[float]]) -> tuple[tuple[int, ...], int]:
    try:
        matrix = tuple(tuple(row) for row in rows)
    except TypeError as exc:
        raise F5ProfileError("ROWS_MUST_BE_RECTANGULAR_SEQUENCE") from exc
    if len(matrix) < 2 or not matrix[0] or len(matrix[0]) < 2:
        raise F5ProfileError("F5_PROFILE_REQUIRES_M_GE_2_AND_R_GE_2")
    r = len(matrix[0])
    counts = []
    for i, row in enumerate(matrix):
        if len(row) != r:
            raise F5ProfileError("RAGGED_ROWS")
        for j, value in enumerate(row):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise F5ProfileError(f"NON_NUMERIC_COUNT_AT_{i}_{j}")
            if not math.isfinite(value) or value not in (0, 1):
                raise F5ProfileError("F5_PROFILE_REQUIRES_BERNOULLI_0_1_ROWS")
        counts.append(int(math.fsum(row)))
    return tuple(counts), r


def _loglik(counts: tuple[int, ...], r: int, mu: float, kappa: float) -> float:
    if not (0.0 < mu < 1.0 and kappa > 0.0):
        return -math.inf
    alpha, beta = mu * kappa, (1.0 - mu) * kappa
    x = np.asarray(counts, dtype=float)
    log_choose = gammaln(r + 1.0) - gammaln(x + 1.0) - gammaln(r - x + 1.0)
    terms = log_choose + betaln(x + alpha, r - x + beta) - betaln(alpha, beta)
    value = float(np.sum(terms))
    return value if math.isfinite(value) else -math.inf


def _limit_loglik(
    counts: tuple[int, ...], r: int, mu: float, *, limit: str,
) -> float:
    if not 0.0 < mu < 1.0:
        if mu == 0.0:
            return 0.0 if all(x == 0 for x in counts) else -math.inf
        if mu == 1.0:
            return 0.0 if all(x == r for x in counts) else -math.inf
        return -math.inf
    if limit == "KAPPA_TO_ZERO":
        if any(x not in (0, r) for x in counts):
            return -math.inf
        n_zero = sum(x == 0 for x in counts)
        n_one = sum(x == r for x in counts)
        return n_zero * math.log1p(-mu) + n_one * math.log(mu)
    if limit == "KAPPA_TO_INFINITY":
        x = np.asarray(counts, dtype=float)
        log_choose = gammaln(r + 1.0) - gammaln(x + 1.0) - gammaln(r - x + 1.0)
        value = float(np.sum(
            log_choose + x * math.log(mu) + (r - x) * math.log1p(-mu)
        ))
        return value if math.isfinite(value) else -math.inf
    raise F5ProfileError("UNKNOWN_CONCENTRATION_LIMIT")


def f5_beta_binomial_mcse_profile_loglik(
    rows: Sequence[Sequence[float]], *, target_m: int, target_r: int,
    target_mcse: float,
) -> F5ProfileResult:
    """Evaluate the F5 profile log-likelihood at a proposed MCSE value.

    Both mu branches are maximized over finite concentration and their analytic
    kappa->0 / kappa->infinity limits. This is a numerical profile evaluator,
    not yet a confidence-set inversion or calibrated inferential method.
    """
    if type(target_m) is not int or target_m < 2:
        raise F5ProfileError("TARGET_M_MUST_BE_INTEGER_GE_2")
    if type(target_r) is not int or target_r < 2:
        raise F5ProfileError("TARGET_R_MUST_BE_INTEGER_GE_2")
    if (isinstance(target_mcse, bool) or not isinstance(target_mcse, (int, float))
            or not math.isfinite(target_mcse) or target_mcse < 0.0):
        raise F5ProfileError("TARGET_MCSE_MUST_BE_FINITE_AND_NONNEGATIVE")

    counts, r = _counts_and_validate(rows)
    g = float(target_mcse)
    maximum_g = 1.0 / (2.0 * math.sqrt(target_m))
    if g > maximum_g + 1e-12:
        return F5ProfileResult(
            g, -math.inf, "NONE", None, "TARGET_OUTSIDE_PARAMETER_SPACE",
            -math.inf, -math.inf, (("feasibility", "HARD_UPPER_BOUND_EXCEEDED"),),
        )

    base = g * g * target_m
    h_zero = base
    h_infinity = base * target_r
    # h(kappa) increases monotonically from h_zero to h_infinity for R*>1.
    if h_zero > 0.25 + 1e-12:
        return F5ProfileResult(
            g, -math.inf, "NONE", None, "TARGET_INFEASIBLE",
            -math.inf, -math.inf, (("feasibility", "NO_CONCENTRATION_SUPPORTS_TARGET"),),
        )

    # Optimize both roots at every finite kappa. For fixed g, h varies with
    # kappa, so use a scalar concentration search on the full constrained
    # interval. The two branches are evaluated jointly at each kappa.
    def branch_pair(logk: float) -> tuple[float, float]:
        k = math.exp(logk)
        h = base * (1.0 + k) / (1.0 + k / target_r)
        if h > 0.25 + 1e-12:
            return -math.inf, -math.inf
        root = math.sqrt(max(0.0, 1.0 - 4.0 * min(0.25, h)))
        mu_plus, mu_minus = (1.0 + root) / 2.0, (1.0 - root) / 2.0
        return (
            _loglik(counts, r, mu_plus, k),
            _loglik(counts, r, mu_minus, k),
        )

    # At the maximum attainable target, only the kappa->0 boundary is
    # feasible. Treat it analytically rather than forcing a positive grid.
    if abs(base - 0.25) <= 1e-14:
        mu_boundary = 0.5
        value = _limit_loglik(counts, r, mu_boundary, limit="KAPPA_TO_ZERO")
        return F5ProfileResult(
            g, value, "MU_BOTH", None, "KAPPA_TO_ZERO_LIMIT",
            value, value, (("feasibility", "ONLY_KAPPA_ZERO_BOUNDARY"),),
        )

    # The feasible concentration domain may be unbounded or have a finite cap.
    if h_infinity <= 0.25 + 1e-12:
        logk_low, logk_high = -24.0, 24.0
        upper_limit_feasible = True
        finite_cap = None
    else:
        # Solve base*(1+k)/(1+k/R*)=1/4 for k:
        # k = (1/4 - base) / (base - 1/(4 R*)).
        denominator = base - 0.25 / target_r
        numerator = 0.25 - base
        if denominator <= 0.0 or numerator < 0.0:
            raise F5ProfileError("FAILED_TO_DERIVE_FEASIBLE_CONCENTRATION_BOUND")
        finite_cap = numerator / denominator
        if not math.isfinite(finite_cap) or finite_cap <= 0.0:
            raise F5ProfileError("FAILED_TO_DERIVE_FEASIBLE_CONCENTRATION_BOUND")
        logk_high = math.log(finite_cap)
        logk_low = min(-24.0, logk_high - 48.0)
        upper_limit_feasible = False

    if logk_high <= logk_low:
        # A cap below the numerical interior range is represented by its
        # analytic h=1/4 endpoint, with both mean branches equal to 1/2.
        if finite_cap is not None:
            value = _loglik(counts, r, 0.5, finite_cap)
            if not math.isfinite(value):
                value = _limit_loglik(counts, r, 0.5, limit="KAPPA_TO_ZERO")
            return F5ProfileResult(
                g, value, "MU_BOTH", finite_cap, "FINITE_FEASIBILITY_BOUNDARY",
                value, value, (("feasibility", "FINITE_CAP_BELOW_LOG_GRID"),),
            )
        raise F5ProfileError("EMPTY_NUMERICAL_CONCENTRATION_DOMAIN")

    grid = np.linspace(logk_low, logk_high, 241)
    branch_values = [[], []]
    branch_candidates = [[], []]
    for z in grid:
        pair = branch_pair(float(z))
        for branch_index in (0, 1):
            branch_values[branch_index].append(pair[branch_index])
    for branch_index in (0, 1):
        vals = branch_values[branch_index]
        for idx, value in enumerate(vals):
            left = vals[idx - 1] if idx else -math.inf
            right = vals[idx + 1] if idx + 1 < len(vals) else -math.inf
            if math.isfinite(value) and value >= left and value >= right:
                lo = float(grid[max(0, idx - 1)])
                hi = float(grid[min(len(grid) - 1, idx + 1)])
                if hi > lo:
                    opt = minimize_scalar(
                        lambda z: -branch_pair(float(z))[branch_index],
                        bounds=(lo, hi), method="bounded",
                        options={"xatol": 1e-10, "maxiter": 2000},
                    )
                    if opt.success and math.isfinite(float(opt.fun)):
                        branch_candidates[branch_index].append(
                            (-float(opt.fun), math.exp(float(opt.x)))
                        )

    # Explicit analytic concentration limits.
    limit_h0 = h_zero
    if limit_h0 <= 0.25:
        root0 = math.sqrt(max(0.0, 1.0 - 4.0 * limit_h0))
        mu0 = ((1.0 + root0) / 2.0, (1.0 - root0) / 2.0)
        for idx, mu in enumerate(mu0):
            value = _limit_loglik(counts, r, mu, limit="KAPPA_TO_ZERO")
            branch_candidates[idx].append((value, None))

    if upper_limit_feasible:
        root_inf = math.sqrt(max(0.0, 1.0 - 4.0 * min(0.25, h_infinity)))
        mu_inf = ((1.0 + root_inf) / 2.0, (1.0 - root_inf) / 2.0)
        for idx, mu in enumerate(mu_inf):
            value = _limit_loglik(counts, r, mu, limit="KAPPA_TO_INFINITY")
            branch_candidates[idx].append((value, None))

    winners = []
    for idx, candidates in enumerate(branch_candidates):
        if candidates:
            winners.append(max(candidates, key=lambda item: item[0]))
        else:
            winners.append((-math.inf, None))
    plus_value, plus_k = winners[0]
    minus_value, minus_k = winners[1]
    if plus_value >= minus_value:
        value, branch, kappa = plus_value, "MU_PLUS", plus_k
    else:
        value, branch, kappa = minus_value, "MU_MINUS", minus_k

    if not math.isfinite(value):
        status = "PROFILE_NONFINITE_OR_UNSUPPORTED_BOUNDARY"
    elif kappa is None:
        status = "CONCENTRATION_BOUNDARY_LIMIT"
    else:
        status = "FINITE_CONCENTRATION_OPTIMUM"
    return F5ProfileResult(
        target_mcse=g, profile_loglik=value, maximizing_branch=branch,
        maximizing_concentration=kappa, boundary_status=status,
        branch_loglik_plus=plus_value, branch_loglik_minus=minus_value,
        optimizer_diagnostics=(
            ("concentration_log_grid_points", str(len(grid))),
            ("finite_optimizer_candidates_plus", str(sum(k is not None for _, k in branch_candidates[0]))),
            ("finite_optimizer_candidates_minus", str(sum(k is not None for _, k in branch_candidates[1]))),
            ("upper_concentration_limit_feasible", str(upper_limit_feasible)),
        ),
    )


def _bisect_profile_crossing(
    function, lower: float, upper: float, *, tolerance: float = 1e-12,
    max_iterations: int = 160,
) -> float:
    """Bisection for signed profile margins, allowing -inf outside support."""
    f_lower = float(function(lower))
    f_upper = float(function(upper))
    if f_lower == 0.0:
        return lower
    if f_upper == 0.0:
        return upper
    if (f_lower > 0.0) == (f_upper > 0.0):
        raise F5ProfileError("PROFILE_ROOT_NOT_BRACKETED")
    for _ in range(max_iterations):
        midpoint = lower + (upper - lower) / 2.0
        f_mid = float(function(midpoint))
        if f_mid == 0.0 or upper - lower <= tolerance:
            return midpoint
        if (f_mid > 0.0) == (f_lower > 0.0):
            lower, f_lower = midpoint, f_mid
        else:
            upper, f_upper = midpoint, f_mid
    if upper - lower > tolerance * 2.0:
        raise F5ProfileError("PROFILE_ROOT_BISECTION_DID_NOT_CONVERGE")
    return lower + (upper - lower) / 2.0


def f5_beta_binomial_mcse_profile_confidence_set(
    rows: Sequence[Sequence[float]], *, target_m: int, target_r: int,
    likelihood_ratio_cutoff: float, scan_grid_points: int = 81,
) -> F5ProfileConfidenceSet:
    """Invert the profile LR rule over the admissible scalar MCSE domain.

    The profile is evaluated on a deterministic grid; every detected crossing
    is refined with Brent's method. Multiple connected components are retained.
    This is a numerical inversion candidate, not a certified global topology
    algorithm: the grid resolution is reported and must be stress-tested.
    """
    if (isinstance(likelihood_ratio_cutoff, bool)
            or not isinstance(likelihood_ratio_cutoff, (int, float))
            or not math.isfinite(likelihood_ratio_cutoff)
            or likelihood_ratio_cutoff <= 0.0):
        raise F5ProfileError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")
    if type(scan_grid_points) is not int or scan_grid_points < 21:
        raise F5ProfileError("SCAN_GRID_POINTS_MUST_BE_INTEGER_GE_21")
    if type(target_m) is not int or target_m < 2:
        raise F5ProfileError("TARGET_M_MUST_BE_INTEGER_GE_2")
    if type(target_r) is not int or target_r < 2:
        raise F5ProfileError("TARGET_R_MUST_BE_INTEGER_GE_2")

    counts, _ = _counts_and_validate(rows)
    del counts
    g_max = 1.0 / (2.0 * math.sqrt(target_m))
    cache: dict[float, float] = {}

    def profile(g: float) -> float:
        key = float(g)
        if key not in cache:
            result = f5_beta_binomial_mcse_profile_loglik(
                rows, target_m=target_m, target_r=target_r,
                target_mcse=key,
            )
            cache[key] = result.profile_loglik
        return cache[key]

    grid = np.linspace(0.0, g_max, scan_grid_points)
    values = [profile(float(g)) for g in grid]
    finite_values = [v for v in values if math.isfinite(v)]
    if not finite_values:
        return F5ProfileConfidenceSet(
            float(likelihood_ratio_cutoff), -math.inf, (), None,
            scan_grid_points, "ABSTAINED_NO_FINITE_PROFILE_VALUES",
        )

    # Refine every grid-detected local maximum, including both domain edges.
    maxima = [(float(g), float(v)) for g, v in zip(grid, values) if math.isfinite(v)]
    for i in range(1, len(grid) - 1):
        if (math.isfinite(values[i]) and values[i] >= values[i - 1]
                and values[i] >= values[i + 1]):
            opt = minimize_scalar(
                lambda z: -profile(float(z)),
                bounds=(float(grid[i - 1]), float(grid[i + 1])),
                method="bounded", options={"xatol": 1e-12, "maxiter": 500},
            )
            if opt.success and math.isfinite(float(opt.fun)):
                maxima.append((float(opt.x), -float(opt.fun)))
    max_g, max_ll = max(maxima, key=lambda item: item[1])
    del max_g

    cutoff = float(likelihood_ratio_cutoff)

    def accepted_margin(g: float) -> float:
        ll = profile(g)
        if not math.isfinite(ll):
            return -math.inf
        return 2.0 * (ll - max_ll) + cutoff

    margins = [accepted_margin(float(g)) for g in grid]
    accepted = [v >= 0.0 for v in margins]
    components: list[tuple[float, float]] = []
    i = 0
    while i < len(grid):
        if not accepted[i]:
            i += 1
            continue
        start = i
        while i + 1 < len(grid) and accepted[i + 1]:
            i += 1
        end = i
        if start == 0:
            lower = 0.0
        else:
            lower = _bisect_profile_crossing(
                accepted_margin, float(grid[start - 1]), float(grid[start]),
            )
        if end == len(grid) - 1:
            upper = g_max
        else:
            upper = _bisect_profile_crossing(
                accepted_margin, float(grid[end]), float(grid[end + 1]),
            )
        components.append((lower, upper))
        i += 1

    if not components:
        status = "EMPTY_LR_SET_ON_NUMERICAL_SCAN"
        hull = None
    else:
        status = "GRID_DETECTED_COMPONENTS_ROOT_REFINED"
        hull = (components[0][0], components[-1][1])
        if len(components) > 1:
            status = "GRID_DETECTED_DISCONNECTED_COMPONENTS_ROOT_REFINED"

    return F5ProfileConfidenceSet(
        likelihood_ratio_cutoff=cutoff,
        unrestricted_profile_loglik=max_ll,
        confidence_components=tuple(components),
        confidence_hull=hull,
        scan_grid_points=scan_grid_points,
        status=status,
    )
