"""Continuous interval-monitor S3 projection for focal theta_A.

The monitor emits only per-interval compliance observations. It never exports
EventHistory transitions, potential outcomes, or interval adjudication objects.
The initial instrument is explicitly perfect when coverage is certified and
allows interval-level missingness; imperfect detection is a separate future
measurement model, not silently assumed.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
import hashlib
import json
import random
from typing import Literal

from c10s_synthetic_components import (
    ContractError, EventHistory, IntervalGrid, digest,
)


@dataclass(frozen=True)
class IntervalMonitorConfig:
    monitor_id: str
    monitor_version: str
    coverage_mode: Literal["CONTINUOUS_EVENT_COVERAGE"]
    missing_probability: float
    capture_lag: Decimal
    ingestion_lag: Decimal

    def validate(self) -> None:
        if not self.monitor_id or not self.monitor_version:
            raise ContractError("interval monitor identity/version are mandatory")
        if self.coverage_mode != "CONTINUOUS_EVENT_COVERAGE":
            raise ContractError("strict V_cont requires certified continuous event coverage")
        if not 0.0 <= self.missing_probability < 1.0:
            raise ContractError("interval missingness probability must be in [0,1)")
        if (not isinstance(self.capture_lag, Decimal)
                or not isinstance(self.ingestion_lag, Decimal)
                or not self.capture_lag.is_finite() or not self.ingestion_lag.is_finite()
                or self.capture_lag < 0 or self.ingestion_lag < 0):
            raise ContractError("interval capture/ingestion lags must be non-negative Decimal values")


@dataclass(frozen=True)
class IntervalS3Observation:
    observation_id: str
    unit_id: str
    history_id: str
    history_version: str
    interval_index: int
    interval_start: Decimal
    interval_end: Decimal
    observed_compliance: bool | None
    observation_status: Literal["OBSERVED", "MISSING"]
    coverage_mode: Literal["CONTINUOUS_EVENT_COVERAGE"]
    capture_time: Decimal
    ingestion_time: Decimal
    monitor_id: str
    monitor_version: str
    grid_id: str
    grid_version: str


def project_interval_s3(
    history: EventHistory,
    grid: IntervalGrid,
    config: IntervalMonitorConfig,
    *,
    seed: int,
) -> tuple[IntervalS3Observation, ...]:
    """Project one realized history through a continuous interval monitor.

    The monitor's coverage is a declared DGP property. Missingness is sampled
    independently per interval with a reproducible seed. No latent state or
    EventHistory transition is copied into the emitted observation.
    """
    history.validate(require_complete=True)
    grid.validate()
    config.validate()
    if grid.boundaries[0] != history.support_start or grid.boundaries[-1] != history.support_end:
        raise ContractError("interval monitor grid must cover exact EventHistory support")
    # Independent continuous-monitor scan: no call to the evaluator's
    # interval adjudicator and no adjudication object crosses this boundary.
    monitored_values = []
    events = history.transitions
    for index, (left, right) in enumerate(zip(grid.boundaries, grid.boundaries[1:])):
        final = index == len(grid.boundaries) - 2
        current = history.initial_post_z_state
        for event in events:
            if event.event_time < left:
                current = event.state_after
            else:
                break
        interval_events = [
            event for event in events
            if event.event_time >= left and (
                event.event_time <= right if final else event.event_time < right
            )
        ]
        events_at_left = any(event.event_time == left for event in interval_events)
        compliant = current.compliant if left == history.support_start or not events_at_left else True
        for event in interval_events:
            current = event.state_after
            compliant = compliant and current.compliant
        monitored_values.append(compliant)
    rng = random.Random(seed)
    records = []
    for index, (left, right, monitored_value) in enumerate(zip(
        grid.boundaries, grid.boundaries[1:], monitored_values
    )):
        missing = rng.random() < config.missing_probability
        observed = None if missing else bool(monitored_value)
        capture_time = right + config.capture_lag
        ingestion_time = capture_time + config.ingestion_lag
        identity = digest((
            history.run_id, history.unit_id, history.history_id,
            config.monitor_id, config.monitor_version, grid.grid_id,
            grid.grid_version, index, seed,
        ))[:24]
        records.append(IntervalS3Observation(
            observation_id=f"IS3-{identity}", unit_id=history.unit_id,
            history_id=history.history_id, history_version=history.history_version,
            interval_index=index, interval_start=left, interval_end=right,
            observed_compliance=observed,
            observation_status="MISSING" if missing else "OBSERVED",
            coverage_mode=config.coverage_mode,
            capture_time=capture_time, ingestion_time=ingestion_time,
            monitor_id=config.monitor_id, monitor_version=config.monitor_version,
            grid_id=grid.grid_id, grid_version=grid.grid_version,
        ))
    return tuple(records)


def validate_interval_s3_observations(
    records: tuple[IntervalS3Observation, ...],
    history: EventHistory,
    grid: IntervalGrid,
    config: IntervalMonitorConfig,
) -> None:
    """Validate observation contract without comparing values to reserved truth."""
    config.validate()
    if not records or len(records) != len(grid.boundaries) - 1:
        raise ContractError("interval S3 observations must cover every declared grid interval")
    if len({row.observation_id for row in records}) != len(records):
        raise ContractError("interval S3 observation IDs must be unique")
    for index, row in enumerate(records):
        if (row.unit_id, row.history_id, row.history_version) != (
            history.unit_id, history.history_id, history.history_version
        ):
            raise ContractError("interval S3 observation history binding mismatch")
        if (row.interval_index, row.interval_start, row.interval_end) != (
            index, grid.boundaries[index], grid.boundaries[index + 1]
        ):
            raise ContractError("interval S3 observations must exactly cover ordered grid cells")
        if row.coverage_mode != config.coverage_mode:
            raise ContractError("interval S3 coverage declaration differs from monitor config")
        if row.observation_status not in ("OBSERVED", "MISSING"):
            raise ContractError("invalid interval S3 missingness status")
        if (row.observation_status == "MISSING") != (row.observed_compliance is None):
            raise ContractError("interval S3 value and missingness status disagree")
        if (row.capture_time < row.interval_end
                or row.ingestion_time < row.capture_time):
            raise ContractError("interval S3 capture/ingestion chronology is invalid")
        if (row.monitor_id, row.monitor_version, row.grid_id, row.grid_version) != (
            config.monitor_id, config.monitor_version, grid.grid_id, grid.grid_version
        ):
            raise ContractError("interval S3 monitor/grid identity mismatch")
        if (row.capture_time != row.interval_end + config.capture_lag
                or row.ingestion_time != row.capture_time + config.ingestion_lag):
            raise ContractError("interval S3 capture/ingestion lags differ from monitor config")
