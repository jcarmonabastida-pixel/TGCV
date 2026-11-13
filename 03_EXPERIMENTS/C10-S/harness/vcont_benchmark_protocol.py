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
