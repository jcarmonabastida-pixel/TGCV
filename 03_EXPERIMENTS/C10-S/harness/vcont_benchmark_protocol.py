"""Pre-registered descriptive/statistical summaries for the C10-S V_cont benchmark.

This module does not run simulations, select scientific thresholds, or turn a
synthetic benchmark into confirmatory evidence. It summarizes an independently
generated calibration/evaluation bank supplied by the caller.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil, isfinite, sqrt
from statistics import mean, stdev
from typing import Iterable


class ProtocolError(ValueError):
    """Invalid benchmark inputs or an under-sized evaluation bank."""


@dataclass(frozen=True)
class ContinuousSummary:
    n: int
    truth: float
    estimate_mean: float
    bias: float
    mae: float
    rmse: float
    estimate_sd: float | None
    mcse_mean: float | None
    recovered_within_tolerance: bool | None


@dataclass(frozen=True)
class BinaryRateSummary:
    n: int
    successes: int
    rate: float
    mcse: float
    wilson_95_low: float
    wilson_95_high: float


@dataclass(frozen=True)
class ScenarioSummary:
    scenario_id: str
    estimate: ContinuousSummary | None
    identification_rate: BinaryRateSummary | None
    abstention_rate: BinaryRateSummary | None
    coverage_rate: BinaryRateSummary | None
    type_i_error_rate: BinaryRateSummary | None
    power_rate: BinaryRateSummary | None
    notes: tuple[str, ...]


def _finite_values(values: Iterable[float], name: str) -> tuple[float, ...]:
    result = tuple(float(x) for x in values)
    if not result or any(not isfinite(x) for x in result):
        raise ProtocolError(f"{name} must contain finite values and be nonempty")
    return result


def summarize_continuous(estimates: Iterable[float], truth: float,
                         tolerance: float | None = None) -> ContinuousSummary:
    xs = _finite_values(estimates, "estimates")
    if not isfinite(float(truth)):
        raise ProtocolError("truth must be finite")
    if tolerance is not None and (not isfinite(float(tolerance)) or tolerance < 0):
        raise ProtocolError("tolerance must be finite and nonnegative")
    errors = tuple(x - truth for x in xs)
    bias = mean(errors)
    mae = mean(abs(x) for x in errors)
    rmse = sqrt(mean(x * x for x in errors))
    sd = stdev(xs) if len(xs) >= 2 else None
    mcse = sd / sqrt(len(xs)) if sd is not None else None
    return ContinuousSummary(
        n=len(xs), truth=float(truth), estimate_mean=mean(xs), bias=bias,
        mae=mae, rmse=rmse, estimate_sd=sd, mcse_mean=mcse,
        recovered_within_tolerance=(abs(bias) <= tolerance if tolerance is not None else None),
    )


def summarize_binary(values: Iterable[bool | int], name: str = "binary outcomes") -> BinaryRateSummary:
    raw = tuple(values)
    if not raw or any(x not in (0, 1, False, True) for x in raw):
        raise ProtocolError(f"{name} must be a nonempty sequence of booleans/0/1")
    n = len(raw)
    successes = sum(int(x) for x in raw)
    p = successes / n
    mcse = sqrt(p * (1.0 - p) / n)
    # Wilson score interval: Monte Carlo uncertainty of a simulated rate,
    # not a confidence interval for a causal estimand.
    z = 1.959963984540054
    denom = 1.0 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return BinaryRateSummary(n, successes, p, mcse,
                             max(0.0, center-half), min(1.0, center+half))


def required_replicates(calibration_sd: float, target_mcse: float) -> int:
    """Minimum R for SD_cal/sqrt(R) <= target_mcse; R>=2."""
    if (not isfinite(calibration_sd) or calibration_sd < 0
            or not isfinite(target_mcse) or target_mcse <= 0):
        raise ProtocolError("calibration_sd must be >=0 and target_mcse >0, both finite")
    if calibration_sd == 0:
        return 2
    return max(2, ceil((calibration_sd / target_mcse) ** 2))


def summarize_scenario(
    scenario_id: str,
    *,
    estimates: Iterable[float] | None = None,
    truth: float | None = None,
    tolerance: float | None = None,
    identified: Iterable[bool] | None = None,
    abstained: Iterable[bool] | None = None,
    covered: Iterable[bool] | None = None,
    rejected_null: Iterable[bool] | None = None,
    rejected_alternative: Iterable[bool] | None = None,
) -> ScenarioSummary:
    if not scenario_id.strip():
        raise ProtocolError("scenario_id is required")
    estimate_summary = None
    if estimates is not None:
        if truth is None:
            raise ProtocolError("truth is required when estimates are supplied")
        estimate_summary = summarize_continuous(estimates, truth, tolerance)
    notes = []
    def rate(values, label):
        if values is None:
            return None
        return summarize_binary(values, label)
    identified_rate = rate(identified, "identification outcomes")
    abstention_rate = rate(abstained, "abstention outcomes")
    coverage_rate = rate(covered, "coverage outcomes")
    type_i_rate = rate(rejected_null, "null rejection outcomes")
    power_rate = rate(rejected_alternative, "alternative rejection outcomes")
    if coverage_rate is None:
        notes.append("COVERAGE_NOT_EVALUATED")
    if type_i_rate is None:
        notes.append("TYPE_I_ERROR_NOT_EVALUATED")
    if power_rate is None:
        notes.append("POWER_NOT_EVALUATED")
    return ScenarioSummary(scenario_id, estimate_summary, identified_rate,
                           abstention_rate, coverage_rate, type_i_rate,
                           power_rate, tuple(notes))


@dataclass(frozen=True)
class SeedAssignment:
    bank: str
    scenario_id: str
    n_units: int
    replicate: int
    world_seed: int
    z_assignment_seed: int
    g_assignment_seed: int


def _derive_seed(bank: str, scenario_id: str, n_units: int, replicate: int,
                 stream: str, namespace: str) -> int:
    if bank not in ("calibration", "evaluation"):
        raise ProtocolError("bank must be calibration or evaluation")
    if stream not in ("world", "z", "g"):
        raise ProtocolError("stream must be world, z or g")
    payload = f"TGCV-C10S-VCONT-SEED-v1|{namespace}|{bank}|{scenario_id}|{n_units}|{replicate}|{stream}"
    return int.from_bytes(__import__("hashlib").sha256(payload.encode("utf-8")).digest()[:8], "big")


def build_seed_bank(bank: str, scenarios: Iterable[str], n_grid: Iterable[int],
                    replicates: int, namespace: str) -> tuple[SeedAssignment, ...]:
    """Create deterministic, bank-separated seeds; each scenario/N has one fixed world.

    World seed is constant across assignment replicates for a scenario/N.
    Z and G assignment seeds vary independently by replicate and stream.
    Calibration and evaluation banks are cryptographically domain-separated.
    """
    scenario_ids = tuple(scenarios)
    sizes = tuple(n_grid)
    if bank not in ("calibration", "evaluation") or not namespace.strip():
        raise ProtocolError("valid bank and nonempty namespace required")
    if not scenario_ids or len(set(scenario_ids)) != len(scenario_ids):
        raise ProtocolError("scenario IDs must be nonempty and unique")
    if any(not x.strip() for x in scenario_ids):
        raise ProtocolError("scenario IDs must be nonempty")
    if not sizes or any(n < 16 or n % 4 for n in sizes) or len(set(sizes)) != len(sizes):
        raise ProtocolError("N grid must contain unique sizes >=16 divisible by four")
    if replicates < 1:
        raise ProtocolError("replicates must be >=1")
    plan = []
    for scenario_id in scenario_ids:
        for n in sizes:
            world = _derive_seed(bank, scenario_id, n, 0, "world", namespace)
            for r in range(replicates):
                plan.append(SeedAssignment(
                    bank, scenario_id, n, r, world,
                    _derive_seed(bank, scenario_id, n, r, "z", namespace),
                    _derive_seed(bank, scenario_id, n, r, "g", namespace),
                ))
    validate_seed_banks(plan, ())
    return tuple(plan)


def validate_seed_banks(calibration: Iterable[SeedAssignment],
                        evaluation: Iterable[SeedAssignment]) -> None:
    """Reject cross-bank seed reuse and within-record Z/G stream collisions."""
    cal = tuple(calibration)
    ev = tuple(evaluation)
    if any(x.bank != "calibration" for x in cal) or any(x.bank != "evaluation" for x in ev):
        raise ProtocolError("seed assignments are stored under the wrong bank label")
    def streams(rows):
        return {seed for row in rows for seed in
                (row.world_seed, row.z_assignment_seed, row.g_assignment_seed)}
    if streams(cal) & streams(ev):
        raise ProtocolError("calibration and evaluation banks share one or more seeds")
    for row in cal + ev:
        if row.z_assignment_seed == row.g_assignment_seed:
            raise ProtocolError("Z and G assignment streams must use distinct seeds")


def select_minimum_n(mcse_by_n: dict[int, dict[str, float]],
                     target_mcse_by_scenario: dict[str, float]) -> int:
    """Choose the smallest candidate N meeting every predeclared scenario MCSE target.

    This is a calibration rule only. Targets and the candidate N grid must be
    supplied before evaluation-bank outcomes are inspected.
    """
    if not mcse_by_n or not target_mcse_by_scenario:
        raise ProtocolError("candidate MCSE results and predeclared targets are required")
    if any(not isfinite(float(v)) or v <= 0 for v in target_mcse_by_scenario.values()):
        raise ProtocolError("all target MCSE values must be finite and >0")
    for n in sorted(mcse_by_n):
        observed = mcse_by_n[n]
        if set(observed) != set(target_mcse_by_scenario):
            continue
        if all(isfinite(float(observed[s])) and observed[s] >= 0
               and observed[s] <= target_mcse_by_scenario[s]
               for s in target_mcse_by_scenario):
            return n
    raise ProtocolError("NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_MCSE_TARGETS")
