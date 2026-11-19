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
from scipy.optimize import minimize, minimize_scalar
from scipy.special import betaln, gammaln


METHOD_ID = "F5_BETA_BINOMIAL_MCSE_PROFILE_0.1"
OPTIMIZER_LOG_LIK_TOLERANCE = 1e-7
OPTIMIZER_MIN_SUCCESSFUL_STARTS_PER_BRANCH = 5


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
    concentration_grid_points: int = 241
    method_id: str = METHOD_ID


@dataclass(frozen=True)
class F5ProfileGridConvergence:
    coarse: F5ProfileConfidenceSet
    fine: F5ProfileConfidenceSet
    component_count_stable: bool
    maximum_loglik_difference: float
    endpoint_maximum_difference: float | None
    within_tolerance: bool
    tolerance: float


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
    target_mcse: float, concentration_grid_points: int = 241,
) -> F5ProfileResult:
    """Evaluate the F5 profile log-likelihood at a proposed MCSE value.

    Both mu branches are maximized over finite concentration and their analytic
    kappa->0 / kappa->infinity limits. This is a numerical profile evaluator;
    the separate confidence-set inversion remains grid-dependent and uncalibrated.
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

    grid = np.linspace(logk_low, logk_high, concentration_grid_points)
    branch_values = [[], []]
    branch_candidates = [[], []]
    for z in grid:
        pair = branch_pair(float(z))
        for branch_index in (0, 1):
            branch_values[branch_index].append(pair[branch_index])
    for branch_index in (0, 1):
        vals = branch_values[branch_index]
        # Retain every evaluated grid point, including finite feasible-domain
        # endpoints. Local refinement augments rather than replaces them.
        for z, value in zip(grid, vals):
            if math.isfinite(value):
                branch_candidates[branch_index].append(
                    (float(value), math.exp(float(z)))
                )
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

    # Preserve the grid-detected interior maxima by branch. These are
    # diagnostics only: a finite grid cannot certify global topology.
    local_maxima_by_branch = [[], []]
    for branch_index in (0, 1):
        vals = branch_values[branch_index]
        for idx in range(1, len(vals) - 1):
            value = vals[idx]
            if (math.isfinite(value) and value >= vals[idx - 1]
                    and value >= vals[idx + 1]):
                local_maxima_by_branch[branch_index].append(
                    (float(value), math.exp(float(grid[idx])))
                )

    # Independent multi-start optimization in log(kappa), using Powell
    # rather than the bounded scalar optimizer above. This is a numerical
    # cross-check, not a certificate of global optimality.
    independent_candidates = [[], []]
    independent_successes = [0, 0]
    primary_best_values = [
        max((v for v, _ in candidates if math.isfinite(v)), default=-math.inf)
        for candidates in branch_candidates
    ]
    seed_indices = sorted(set(
        int(round(i * (len(grid) - 1) / 8.0)) for i in range(9)
    ))
    for branch_index in (0, 1):
        for seed_index in seed_indices:
            seed = float(grid[seed_index])
            def objective(z):
                value = branch_pair(float(np.asarray(z).reshape(-1)[0]))[branch_index]
                return -value if math.isfinite(value) else 1e100
            try:
                opt = minimize(
                    objective, x0=np.asarray([seed]), method="Powell",
                    bounds=[(float(logk_low), float(logk_high))],
                    options={"xtol": 1e-9, "ftol": 1e-11, "maxiter": 3000},
                )
            except (ArithmeticError, FloatingPointError, ValueError):
                continue
            if opt.success and math.isfinite(float(opt.fun)) and float(opt.fun) < 1e99:
                independent_successes[branch_index] += 1
                independent_candidates[branch_index].append(
                    (-float(opt.fun), math.exp(float(np.asarray(opt.x).reshape(-1)[0])))
                )
        if independent_candidates[branch_index]:
            branch_candidates[branch_index].extend(independent_candidates[branch_index])

    independent_gaps = []
    for branch_index in (0, 1):
        candidates = sorted(
            (v for v, _ in independent_candidates[branch_index]), reverse=True
        )
        independent_gaps.append(
            "NA" if not candidates else format(
                abs(candidates[0] - primary_best_values[branch_index]), ".17g"
            )
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

    local_maxima_gaps = []
    for maxima in local_maxima_by_branch:
        ordered = sorted((v for v, _ in maxima), reverse=True)
        local_maxima_gaps.append(
            "NA" if len(ordered) < 2 else format(ordered[0] - ordered[1], ".17g")
        )

    optimizer_gap_values = [
        None if item == "NA" else float(item) for item in independent_gaps
    ]
    winner_is_boundary = (
        kappa is None
        or math.log(kappa) - logk_low <= 1e-6
        or logk_high - math.log(kappa) <= 1e-6
    )
    if any(n < OPTIMIZER_MIN_SUCCESSFUL_STARTS_PER_BRANCH for n in independent_successes):
        optimizer_adjudication = "OPTIMIZATION_INSUFFICIENT"
    elif winner_is_boundary:
        optimizer_adjudication = "OPTIMIZATION_BOUNDARY_SENSITIVE"
    elif any(gap is None or gap > OPTIMIZER_LOG_LIK_TOLERANCE
             for gap in optimizer_gap_values):
        optimizer_adjudication = "OPTIMIZATION_DISCORDANT"
    else:
        optimizer_adjudication = "OPTIMIZATION_CONCORDANT"

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
            ("mu_plus_grid_local_maxima_count", str(len(local_maxima_by_branch[0]))),
            ("mu_minus_grid_local_maxima_count", str(len(local_maxima_by_branch[1]))),
            ("mu_plus_grid_local_maxima_kappa", repr(tuple(k for _, k in local_maxima_by_branch[0]))),
            ("mu_minus_grid_local_maxima_kappa", repr(tuple(k for _, k in local_maxima_by_branch[1]))),
            ("mu_plus_top_two_local_maxima_loglik_gap", local_maxima_gaps[0]),
            ("mu_minus_top_two_local_maxima_loglik_gap", local_maxima_gaps[1]),
            ("mu_plus_independent_multistart_successes", str(independent_successes[0])),
            ("mu_minus_independent_multistart_successes", str(independent_successes[1])),
            ("mu_plus_independent_optimizer_gap", independent_gaps[0]),
            ("mu_minus_independent_optimizer_gap", independent_gaps[1]),
            ("optimizer_adjudication", optimizer_adjudication),
            ("optimizer_loglik_tolerance", format(OPTIMIZER_LOG_LIK_TOLERANCE, ".17g")),
            ("optimizer_min_successful_starts_per_branch", str(OPTIMIZER_MIN_SUCCESSFUL_STARTS_PER_BRANCH)),

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
    concentration_grid_points: int = 241,
) -> F5ProfileConfidenceSet:
    """Invert the profile LR rule over the admissible scalar MCSE domain.

    The profile is evaluated on deterministic MCSE and concentration grids;
    every detected crossing is refined by bracketed bisection. Multiple
    connected components are retained.
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
    if type(concentration_grid_points) is not int or concentration_grid_points < 41:
        raise F5ProfileError("CONCENTRATION_GRID_POINTS_MUST_BE_INTEGER_GE_41")

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
                concentration_grid_points=concentration_grid_points,
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
            concentration_grid_points=concentration_grid_points,
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
        concentration_grid_points=concentration_grid_points,
    )



def f5_beta_binomial_mcse_profile_grid_convergence(
    rows: Sequence[Sequence[float]], *, target_m: int, target_r: int,
    likelihood_ratio_cutoff: float,
    coarse_scan_grid_points: int = 81,
    fine_scan_grid_points: int = 161,
    coarse_concentration_grid_points: int = 241,
    fine_concentration_grid_points: int = 481,
    tolerance: float = 1e-3,
) -> F5ProfileGridConvergence:
    """Compare nested numerical resolutions; this is a diagnostic, not proof.

    The caller supplies the LR cutoff. Stability requires equal detected
    component counts, finite profile maxima, and maximum absolute differences
    in the unrestricted profile log likelihood and component endpoints no
    larger than tolerance. It cannot detect a component missed by both grids.
    """
    if (not math.isfinite(tolerance) or tolerance <= 0.0
            or isinstance(tolerance, bool)):
        raise F5ProfileError("CONVERGENCE_TOLERANCE_MUST_BE_FINITE_AND_POSITIVE")
    if (fine_scan_grid_points <= coarse_scan_grid_points
            or fine_concentration_grid_points <= coarse_concentration_grid_points):
        raise F5ProfileError("FINE_GRIDS_MUST_EXCEED_COARSE_GRIDS")

    coarse = f5_beta_binomial_mcse_profile_confidence_set(
        rows, target_m=target_m, target_r=target_r,
        likelihood_ratio_cutoff=likelihood_ratio_cutoff,
        scan_grid_points=coarse_scan_grid_points,
        concentration_grid_points=coarse_concentration_grid_points,
    )
    fine = f5_beta_binomial_mcse_profile_confidence_set(
        rows, target_m=target_m, target_r=target_r,
        likelihood_ratio_cutoff=likelihood_ratio_cutoff,
        scan_grid_points=fine_scan_grid_points,
        concentration_grid_points=fine_concentration_grid_points,
    )
    component_stable = (
        len(coarse.confidence_components) == len(fine.confidence_components)
        and coarse.status != "ABSTAINED_NO_FINITE_PROFILE_VALUES"
        and fine.status != "ABSTAINED_NO_FINITE_PROFILE_VALUES"
    )
    if not (math.isfinite(coarse.unrestricted_profile_loglik)
            and math.isfinite(fine.unrestricted_profile_loglik)):
        maxll_diff = math.inf
    else:
        maxll_diff = abs(
            coarse.unrestricted_profile_loglik - fine.unrestricted_profile_loglik
        )
    endpoint_diff = None
    if component_stable and coarse.confidence_components:
        endpoint_diff = max(
            abs(a - b)
            for pair_coarse, pair_fine in zip(
                coarse.confidence_components, fine.confidence_components,
            )
            for a, b in zip(pair_coarse, pair_fine)
        )
    within = (
        component_stable
        and endpoint_diff is not None
        and maxll_diff <= tolerance
        and endpoint_diff <= tolerance
    )
    return F5ProfileGridConvergence(
        coarse=coarse, fine=fine,
        component_count_stable=component_stable,
        maximum_loglik_difference=maxll_diff,
        endpoint_maximum_difference=endpoint_diff,
        within_tolerance=within, tolerance=tolerance,
    )
