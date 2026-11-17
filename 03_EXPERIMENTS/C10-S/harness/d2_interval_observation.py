"""D2 randomized-Z interval S3 observation lane for C10-S.

Only the realized Z history is projected. The resulting sealed evidence
contains interval observations and assignment provenance, never D2 potential
outcomes or reserved interval adjudications.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
import hashlib
import json
from typing import Any, Mapping, Sequence

from c10s_synthetic_components import (
    ContractError, D2VContTruthBundle, EventHistory, IntervalGrid,
    SyntheticWorldBundle, digest,
)
from d2_observed_assignment import (
    D2ObservedAssignmentBundle, D2ObservedAssignmentConfig,
    generate_d2_observed_assignments, select_d2_realized_histories,
)
from theta_a_interval_observation import (
    IntervalMonitorConfig, IntervalS3Observation,
    project_interval_s3, validate_interval_s3_observations,
)


SCHEMA = "C10S-D2-Z-S3-INTERVAL-002"


def _plain(value: Any) -> Any:
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in sorted(value.items())}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _hash(value: Any) -> str:
    raw = json.dumps(_plain(value), sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class D2IntervalObservationRecord:
    run_id: str
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    unit_id: str
    history_ref: str
    assignment_bundle_sha256: str
    q_x_sha256: str
    assignment_mechanism_id: str
    assignment_mechanism_version: str
    assigned_z: int
    probability_z0: float
    probability_z1: float
    assignment_probability: float
    assignment_uniform_sha256: str
    selected_potential_id: str
    history_id: str
    history_version: str
    history_content_sha256: str
    observation_id: str
    interval_index: int
    interval_start: Decimal
    interval_end: Decimal
    observed_compliance: bool | None
    observation_status: str
    coverage_mode: str
    capture_time: Decimal
    ingestion_time: Decimal
    monitor_id: str
    monitor_version: str
    grid_id: str
    grid_version: str
    temporal_resolution: str = "INTERVAL_LEVEL"


@dataclass(frozen=True)
class D2IntervalEvidenceCandidate:
    run_id: str
    rows: tuple[dict[str, Any], ...]
    expected_unit_history_refs: tuple[tuple[str, str], ...] = ()
    expected_unit_assignments: tuple[tuple[str, str, int, float, float], ...] = ()
    grid_id: str = ""
    grid_version: str = ""
    monitor_id: str = ""
    monitor_version: str = ""
    interval_bounds: tuple[tuple[Decimal, Decimal], ...] = ()
    assignment_bundle_sha256: str = ""
    assignment_mechanism_id: str = ""
    assignment_mechanism_version: str = ""
    q_x_sha256: str = ""


@dataclass(frozen=True)
class SealedD2IntervalEvidence:
    run_id: str
    rows: tuple[dict[str, Any], ...]
    manifest: dict[str, Any]
    sha256: str


def compose_d2_interval_s3_records(
    world: SyntheticWorldBundle,
    assignments: D2ObservedAssignmentBundle,
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
    truth: D2VContTruthBundle,
    grid: IntervalGrid,
    monitor_config_by_history_ref: Mapping[str, IntervalMonitorConfig] | IntervalMonitorConfig,
    seeds_by_unit: dict[str, int],
) -> tuple[D2IntervalObservationRecord, ...]:
    """Project exactly one assigned D2 EventHistory per q_X unit to interval S3."""
    world.validate()
    grid.validate()
    if isinstance(monitor_config_by_history_ref, IntervalMonitorConfig):
        monitor_configs = {unit.d2_baseline.baseline_history_ref: monitor_config_by_history_ref for unit in world.units}
    else:
        monitor_configs = dict(monitor_config_by_history_ref)
    expected_refs = {row.history_ref for row in world.q_x}
    if set(monitor_configs) != expected_refs:
        raise ContractError("D2 interval monitor configurations must cover q_X* histories exactly")
    for config in monitor_configs.values():
        config.validate()
    assignments.validate(world, truth, histories_by_unit_z, grid)
    if set(seeds_by_unit) != {unit.unit_id for unit in world.units}:
        raise ContractError("D2 interval monitor seeds must cover the exact randomized roster")
    selected = select_d2_realized_histories(assignments, histories_by_unit_z)
    if len(selected) != len(world.units):
        raise ContractError("D2 realized-history selection must contain exactly one history per unit")
    assignment_by_unit = {row.unit_id: row for row in assignments.assignments}
    records = []
    for history in selected:
        assignment = assignment_by_unit[history.unit_id]
        monitor_config = monitor_configs[assignment.history_ref]
        projected = project_interval_s3(
            history, grid, monitor_config, seed=seeds_by_unit[history.unit_id],
        )
        validate_interval_s3_observations(projected, history, grid, monitor_config)
        probability = (
            assignment.probability_z1 if assignment.assigned_z == 1
            else assignment.probability_z0
        )
        for observation in projected:
            records.append(D2IntervalObservationRecord(
                run_id=history.run_id, world_id=world.world_id,
                world_version=world.world_version, dgp_id=world.dgp_id,
                dgp_version=world.dgp_version, unit_id=history.unit_id,
                history_ref=assignment.history_ref,
                assignment_bundle_sha256=assignments.result_sha256,
                q_x_sha256=assignments.q_x_sha256,
                assignment_mechanism_id=assignments.mechanism_id,
                assignment_mechanism_version=assignments.mechanism_version,
                assigned_z=assignment.assigned_z,
                probability_z0=assignment.probability_z0,
                probability_z1=assignment.probability_z1,
                assignment_probability=probability,
                assignment_uniform_sha256=assignment.assignment_uniform_sha256,
                selected_potential_id=assignment.selected_potential_id,
                history_id=history.history_id, history_version=history.history_version,
                history_content_sha256=history.content_sha256,
                observation_id=observation.observation_id,
                interval_index=observation.interval_index,
                interval_start=observation.interval_start,
                interval_end=observation.interval_end,
                observed_compliance=observation.observed_compliance,
                observation_status=observation.observation_status,
                coverage_mode=observation.coverage_mode,
                capture_time=observation.capture_time,
                ingestion_time=observation.ingestion_time,
                monitor_id=observation.monitor_id,
                monitor_version=observation.monitor_version,
                grid_id=observation.grid_id, grid_version=observation.grid_version,
            ))
    return tuple(records)


def candidate_from_d2_interval_records(
    records: Sequence[D2IntervalObservationRecord],
    *,
    run_id: str | None = None,
    expected_unit_history_refs: tuple[tuple[str, str], ...] = (),
    expected_unit_assignments: tuple[tuple[str, str, int, float, float], ...] = (),
    grid_id: str = "",
    grid_version: str = "",
    monitor_id: str = "",
    monitor_version: str = "",
    interval_bounds: tuple[tuple[Decimal, Decimal], ...] = (),
    assignment_bundle_sha256: str = "",
    assignment_mechanism_id: str = "",
    assignment_mechanism_version: str = "",
    q_x_sha256: str = "",
) -> D2IntervalEvidenceCandidate:
    """Build S3 evidence; empty observations require a complete external context.

    The roster/assignment and temporal grid/monitor are declared independently
    of observed rows, so zero response cannot erase the observation design.
    """
    if records:
        run_ids = {row.run_id for row in records}
        if len(run_ids) != 1:
            raise ContractError("D2 interval observations contain multiple run identities")
        first = records[0]
        inferred = {
            "run_id": next(iter(run_ids)),
            "grid_id": first.grid_id, "grid_version": first.grid_version,
            "monitor_id": first.monitor_id, "monitor_version": first.monitor_version,
            "assignment_bundle_sha256": first.assignment_bundle_sha256,
            "assignment_mechanism_id": first.assignment_mechanism_id,
            "assignment_mechanism_version": first.assignment_mechanism_version,
            "q_x_sha256": first.q_x_sha256,
            "interval_bounds": tuple(
                (row.interval_start, row.interval_end)
                for row in sorted(records, key=lambda x: x.interval_index)
                if row.unit_id == first.unit_id
            ),
        }
        run_id = run_id or inferred["run_id"]
        grid_id = grid_id or inferred["grid_id"]
        grid_version = grid_version or inferred["grid_version"]
        monitor_id = monitor_id or inferred["monitor_id"]
        monitor_version = monitor_version or inferred["monitor_version"]
        interval_bounds = interval_bounds or inferred["interval_bounds"]
        assignment_bundle_sha256 = assignment_bundle_sha256 or inferred["assignment_bundle_sha256"]
        assignment_mechanism_id = assignment_mechanism_id or inferred["assignment_mechanism_id"]
        assignment_mechanism_version = assignment_mechanism_version or inferred["assignment_mechanism_version"]
        q_x_sha256 = q_x_sha256 or inferred["q_x_sha256"]
    if not run_id:
        raise ContractError("D2 interval evidence requires an explicit run identity")
    return D2IntervalEvidenceCandidate(
        run_id, tuple(asdict(row) for row in records),
        expected_unit_history_refs, expected_unit_assignments,
        grid_id, grid_version, monitor_id, monitor_version, interval_bounds,
        assignment_bundle_sha256, assignment_mechanism_id,
        assignment_mechanism_version, q_x_sha256,
    )


class D2IntervalSealer:
    """Closed-schema S3 sealer for the randomized D2 assignment lane."""
    version = "c10s-d2-interval-sealer-0.2"

    def seal(self, candidate: D2IntervalEvidenceCandidate) -> SealedD2IntervalEvidence:
        allowed = frozenset(D2IntervalObservationRecord.__dataclass_fields__)
        if not candidate.run_id:
            raise ContractError("D2 interval evidence requires run identity")
        if not candidate.rows and not (
            candidate.expected_unit_assignments and candidate.grid_id
            and candidate.grid_version and candidate.monitor_id
            and candidate.monitor_version and candidate.interval_bounds
            and candidate.assignment_bundle_sha256
            and candidate.assignment_mechanism_id
            and candidate.assignment_mechanism_version and candidate.q_x_sha256
        ):
            raise ContractError("zero-row D2 evidence requires full roster, assignment, grid, monitor and interval context")
        seen_ids = set()
        units: dict[str, dict[str, Any]] = {}
        normalised = []
        expected_pairs = candidate.expected_unit_history_refs
        expected_assignments = candidate.expected_unit_assignments
        if expected_assignments:
            assignment_ids = [row[0] for row in expected_assignments]
            if (any(len(row) != 5 for row in expected_assignments)
                    or len(assignment_ids) != len(set(assignment_ids))
                    or any(not row[0] or not row[1] or type(row[2]) is not int
                           or row[2] not in (0, 1)
                           or not 0.0 < row[3] < 1.0 or not 0.0 < row[4] < 1.0
                           or abs(row[3] + row[4] - 1.0) > 1e-12
                           for row in expected_assignments)):
                raise ContractError("D2 expected assignment roster has invalid identities, arms or probabilities")
            details_by_unit = {row[0]: row for row in expected_assignments}
            if expected_pairs and any(
                details_by_unit.get(unit_id, (None, history_ref))[1] != history_ref
                for unit_id, history_ref in expected_pairs
            ):
                raise ContractError("D2 expected assignment details disagree with expected history roster")
            expected_pairs = tuple((row[0], row[1]) for row in expected_assignments)
        if expected_pairs:
            expected_ids = [unit_id for unit_id, _ in expected_pairs]
            expected_refs = [history_ref for _, history_ref in expected_pairs]
            if (len(expected_ids) != len(set(expected_ids))
                    or len(expected_refs) != len(set(expected_refs))
                    or any(not unit_id or not history_ref for unit_id, history_ref in expected_pairs)):
                raise ContractError("D2 expected randomized roster must have unique unit/history identities")
        else:
            expected_pairs = ()
        for row in candidate.rows:
            if set(row) != allowed or row.get("temporal_resolution") != "INTERVAL_LEVEL":
                raise ContractError("D2 interval evidence violates its closed S3 schema")
            if row["run_id"] != candidate.run_id:
                raise ContractError("D2 interval evidence run identity mismatch")
            strings = (
                "world_id", "world_version", "dgp_id", "dgp_version", "unit_id",
                "history_ref", "assignment_bundle_sha256", "q_x_sha256",
                "assignment_mechanism_id", "assignment_mechanism_version",
                "assignment_uniform_sha256", "selected_potential_id", "history_id",
                "history_version", "history_content_sha256", "observation_id",
                "monitor_id", "monitor_version", "grid_id", "grid_version",
            )
            if any(not isinstance(row[k], str) or not row[k] for k in strings):
                raise ContractError("D2 S3 identity/version/provenance fields are mandatory")
            if type(row["assigned_z"]) is not int or row["assigned_z"] not in (0, 1):
                raise ContractError("D2 assigned Z must be binary")
            for field in ("probability_z0", "probability_z1", "assignment_probability"):
                value = row[field]
                if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0.0 < value <= 1.0:
                    raise ContractError("D2 assignment probabilities must be in (0,1]")
            if abs(row["probability_z0"] + row["probability_z1"] - 1.0) > 1e-12:
                raise ContractError("D2 assignment arm probabilities must sum to one")
            expected_p = row["probability_z1"] if row["assigned_z"] == 1 else row["probability_z0"]
            if abs(row["assignment_probability"] - expected_p) > 1e-12:
                raise ContractError("D2 realized assignment probability does not match assigned Z")
            if row["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE":
                raise ContractError("strict V_cont requires continuous event coverage declaration")
            if row["observation_status"] not in ("OBSERVED", "MISSING"):
                raise ContractError("invalid D2 interval observation status")
            value = row["observed_compliance"]
            if (row["observation_status"] == "MISSING") != (value is None):
                raise ContractError("D2 interval observation value and missingness status disagree")
            if value is not None and type(value) is not bool:
                raise ContractError("D2 interval compliance must be Boolean or missing")
            if type(row["interval_index"]) is not int or row["interval_index"] < 0:
                raise ContractError("D2 interval index must be non-negative")
            times = (row["interval_start"], row["interval_end"], row["capture_time"], row["ingestion_time"])
            if any(not isinstance(t, Decimal) or not t.is_finite() for t in times):
                raise ContractError("D2 interval timestamps must be finite Decimal values")
            if not times[0] < times[1] <= times[2] <= times[3]:
                raise ContractError("D2 interval/capture/ingestion chronology is invalid")
            if row["observation_id"] in seen_ids:
                raise ContractError("duplicate D2 interval observation ID")
            seen_ids.add(row["observation_id"])
            unit = row["unit_id"]
            assignment = tuple(row[k] for k in (
                "world_id", "world_version", "dgp_id", "dgp_version",
                "history_ref", "assignment_bundle_sha256", "q_x_sha256",
                "assignment_mechanism_id", "assignment_mechanism_version",
                "assigned_z", "probability_z0", "probability_z1",
                "assignment_probability", "assignment_uniform_sha256",
                "selected_potential_id", "history_id", "history_version",
                "history_content_sha256",
            ))
            contract = units.setdefault(unit, {"assignment": assignment, "rows": []})
            if contract["assignment"] != assignment:
                raise ContractError("D2 interval observations vary in unit assignment/history provenance")
            contract["rows"].append(row)
            normalised.append(dict(row))
        common_grid = ((candidate.grid_id, candidate.grid_version)
                       if not candidate.rows else None)
        common_bounds = candidate.interval_bounds if not candidate.rows else None
        common_monitor = ((candidate.monitor_id, candidate.monitor_version)
                          if not candidate.rows else None)
        if not candidate.rows:
            if (not common_grid[0] or not common_grid[1]
                    or not common_monitor[0] or not common_monitor[1]
                    or not common_bounds
                    or any(not isinstance(a, Decimal) or not isinstance(b, Decimal)
                           or not a.is_finite() or not b.is_finite() or not a < b
                           for a, b in common_bounds)
                    or any(left[1] != right[0]
                           for left, right in zip(common_bounds, common_bounds[1:]))):
                raise ContractError("zero-row D2 evidence has invalid declared grid/monitor context")
        for unit, contract in units.items():
            rows = sorted(contract["rows"], key=lambda x: x["interval_index"])
            if [r["interval_index"] for r in rows] != list(range(len(rows))):
                raise ContractError(f"D2 interval coverage has gaps or duplicate indices for {unit}")
            grid = (rows[0]["grid_id"], rows[0]["grid_version"])
            bounds = tuple((r["interval_start"], r["interval_end"]) for r in rows)
            monitor = (rows[0]["monitor_id"], rows[0]["monitor_version"])
            if any((r["grid_id"], r["grid_version"]) != grid for r in rows):
                raise ContractError("D2 interval grid identity changes within a unit")
            if any((r["monitor_id"], r["monitor_version"]) != monitor for r in rows):
                raise ContractError("D2 monitor identity changes within a unit")
            if any(a[1] != b[0] for a, b in zip(bounds, bounds[1:])):
                raise ContractError("D2 interval coverage must be contiguous without gaps or overlaps")
            if common_grid is None:
                common_grid, common_bounds, common_monitor = grid, bounds, monitor
            elif grid != common_grid or bounds != common_bounds or monitor != common_monitor:
                raise ContractError("all D2 units must share exact grid and monitor versions")
        observed_pairs = {
            unit: contract["assignment"][4]
            for unit, contract in units.items()
        }
        if expected_pairs:
            expected_by_unit = dict(expected_pairs)
            if not set(units).issubset(expected_by_unit):
                raise ContractError("D2 observed rows contain units outside the declared randomized roster")
            if any(observed_pairs[unit] != expected_by_unit[unit] for unit in units):
                raise ContractError("D2 observed history refs differ from the declared randomized roster")
        else:
            expected_by_unit = dict(observed_pairs)
            expected_pairs = tuple(sorted(expected_by_unit.items()))
        missing_unit_ids = tuple(sorted(set(expected_by_unit) - set(units)))
        if expected_assignments:
            detail_by_unit = {row[0]: row for row in expected_assignments}
            for unit_id, unit_contract in units.items():
                assignment = unit_contract["assignment"]
                observed_detail = (
                    unit_id, assignment[4], assignment[9], assignment[10], assignment[11],
                )
                if detail_by_unit.get(unit_id) != observed_detail:
                    raise ContractError("D2 expected assignment metadata differs from observed S3 assignment provenance")
        if expected_assignments:
            assignment_details = tuple(sorted(expected_assignments))
        elif expected_pairs and not missing_unit_ids:
            assignment_details = tuple(sorted(
                (unit, expected_by_unit[unit], units[unit]["assignment"][9],
                 units[unit]["assignment"][10], units[unit]["assignment"][11])
                for unit in expected_by_unit
            ))
        else:
            raise ContractError("D2 roster with unit nonresponse requires declared assigned arms and probabilities")
        if candidate.rows and (
            candidate.grid_id and (candidate.grid_id, candidate.grid_version) != common_grid
            or candidate.monitor_id and (candidate.monitor_id, candidate.monitor_version) != common_monitor
            or candidate.interval_bounds and candidate.interval_bounds != common_bounds
        ):
            raise ContractError("D2 candidate context differs from observed grid/monitor/interval rows")
        manifest = {
            "run_id": candidate.run_id, "schema": SCHEMA,
            "sealer_version": self.version, "row_count": len(normalised),
            "unit_count": len(units), "expected_unit_count": len(expected_by_unit),
            "expected_unit_history_refs": tuple(sorted(expected_pairs)),
            "expected_unit_assignments": assignment_details,
            "missing_unit_ids": missing_unit_ids,
            "temporal_resolution": "INTERVAL_LEVEL",
            "grid_id": common_grid[0], "grid_version": common_grid[1],
            "monitor_id": common_monitor[0], "monitor_version": common_monitor[1],
            "interval_count_per_unit": len(common_bounds),
            "interval_bounds": tuple(common_bounds),
        }
        return SealedD2IntervalEvidence(
            candidate.run_id, tuple(normalised), manifest,
            _hash({"manifest": manifest, "rows": normalised}),
        )


@dataclass(frozen=True)
class D2ObservedIntervalLaneResult:
    assignments: D2ObservedAssignmentBundle
    interval_records: tuple[D2IntervalObservationRecord, ...]
    sealed_evidence: SealedD2IntervalEvidence

    def validate(
        self,
        world: SyntheticWorldBundle,
        truth: D2VContTruthBundle,
        histories_by_unit_z: dict[tuple[str, int], EventHistory],
        grid: IntervalGrid,
    ) -> None:
        self.assignments.validate(world, truth, histories_by_unit_z, grid)
        expected_units = {unit.unit_id for unit in world.units}
        record_units = {row.unit_id for row in self.interval_records}
        evidence_units = {row["unit_id"] for row in self.sealed_evidence.rows}
        if record_units != evidence_units or not record_units.issubset(expected_units):
            raise ContractError("D2 interval records/evidence must be the same subset of the randomized roster")
        if self.sealed_evidence.run_id != truth.run_id or any(
            row.run_id != self.sealed_evidence.run_id for row in self.interval_records
        ):
            raise ContractError("D2 sealed evidence run differs from reserved truth/source interval records")
        source_rows = tuple(asdict(row) for row in self.interval_records)
        if source_rows != self.sealed_evidence.rows:
            raise ContractError("D2 sealed evidence content differs from its source interval records")
        expected_per_unit = len(grid.boundaries) - 1
        counts = {unit: 0 for unit in record_units}
        assignment_by_unit = {x.unit_id: x for x in self.assignments.assignments}
        for row in self.interval_records:
            counts[row.unit_id] += 1
            assignment = assignment_by_unit[row.unit_id]
            if (row.world_id, row.world_version, row.dgp_id, row.dgp_version,
                    row.assignment_bundle_sha256, row.assigned_z,
                    row.selected_potential_id, row.history_id) != (
                    world.world_id, world.world_version, world.dgp_id, world.dgp_version,
                    self.assignments.result_sha256, assignment.assigned_z,
                    assignment.selected_potential_id, assignment.selected_history_id
                    ):
                raise ContractError("D2 interval record is detached from its world/assignment/selected history")
        if any(count != expected_per_unit for count in counts.values()):
            raise ContractError("observed D2 units must cover the exact declared grid")
        if self.sealed_evidence.sha256 != _hash({
            "manifest": self.sealed_evidence.manifest,
            "rows": list(self.sealed_evidence.rows),
        }):
            raise ContractError("D2 sealed evidence digest does not match its contents")
        manifest = self.sealed_evidence.manifest
        expected_missing = tuple(sorted(expected_units - record_units))
        expected_assignments = tuple(sorted(
            (row.unit_id, row.history_ref, row.assigned_z,
             row.probability_z0, row.probability_z1)
            for row in self.assignments.assignments
        ))
        if (
            manifest.get("unit_count") != len(record_units)
            or manifest.get("row_count") != len(self.interval_records)
            or manifest.get("expected_unit_count") != len(expected_units)
            or manifest.get("missing_unit_ids") != expected_missing
            or tuple(manifest.get("expected_unit_assignments", ())) != expected_assignments
            or manifest.get("interval_count_per_unit") != expected_per_unit
            or tuple(manifest.get("interval_bounds", ())) != tuple(zip(grid.boundaries, grid.boundaries[1:]))
            or (manifest.get("grid_id"), manifest.get("grid_version"))
               != (grid.grid_id, grid.grid_version)
            or not manifest.get("monitor_id") or not manifest.get("monitor_version")
        ):
            raise ContractError("D2 sealed manifest differs from the randomized roster/grid/monitor context")


def materialize_d2_observed_interval_lane(
    *,
    world: SyntheticWorldBundle,
    truth: D2VContTruthBundle,
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
    assignment_config: D2ObservedAssignmentConfig,
    grid: IntervalGrid,
    monitor_config_by_history_ref: Mapping[str, IntervalMonitorConfig] | IntervalMonitorConfig,
    seeds_by_unit: dict[str, int],
) -> D2ObservedIntervalLaneResult:
    """Complete D2 Z assignment -> realized EventHistory -> interval S3 -> Sealer."""
    assignments = generate_d2_observed_assignments(
        world, truth, histories_by_unit_z, assignment_config,
    )
    records = compose_d2_interval_s3_records(
        world, assignments, histories_by_unit_z, truth, grid,
        monitor_config_by_history_ref, seeds_by_unit,
    )
    candidate = D2IntervalEvidenceCandidate(
        records[0].run_id, tuple(asdict(row) for row in records),
        tuple((row.unit_id, row.history_ref) for row in assignments.assignments),
        tuple((row.unit_id, row.history_ref, row.assigned_z,
               row.probability_z0, row.probability_z1)
              for row in assignments.assignments),
    )
    sealed = D2IntervalSealer().seal(candidate)
    result = D2ObservedIntervalLaneResult(assignments, records, sealed)
    result.validate(world, truth, histories_by_unit_z, grid)
    return result
