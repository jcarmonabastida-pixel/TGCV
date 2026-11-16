"""Factorial A×M assignment and potential-history selection for C10-S.

A is the direct focal g_A intervention. M is an independent, versioned
Boolean functional mechanism; it is not a Vector4 coordinate and is not D2/Z.
The module deliberately separates assignment/selection from S3 observation,
analysis, and the reserved factorial oracle.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
import hashlib
import json
from decimal import Decimal
from typing import Literal, Sequence

from c10s_synthetic_components import (
    ContractError, JointPolicyHistory, RCommonPairCertificate,
    SyntheticWorldBundle, Vector4, _dgp_uniform, digest,
)
from c10s_functional_history import FunctionalHistoryDGPConfig, generate_factorial_event_history_potentials
from c10s_synthetic_components import EventHistory


FactorialCell = Literal["00", "10", "01", "11"]


@dataclass(frozen=True)
class FactorialAssignmentConfig:
    mechanism_id: str
    mechanism_version: str
    factor_m_id: str
    factor_m_version: str
    randomization_salt: str
    probability_by_history: tuple[tuple[str, float, float, float, float], ...]

    def validate(self, world: SyntheticWorldBundle) -> None:
        world.validate()
        if not all((self.mechanism_id, self.mechanism_version,
                    self.factor_m_id, self.factor_m_version,
                    self.randomization_salt)):
            raise ContractError("factorial assignment and M identities/versions/salt are mandatory")
        refs = {row.history_ref for row in world.q_x}
        supplied = [row[0] for row in self.probability_by_history]
        if len(supplied) != len(set(supplied)) or set(supplied) != refs:
            raise ContractError("factorial cell probabilities must cover q_X* histories exactly")
        for history_ref, p00, p10, p01, p11 in self.probability_by_history:
            probabilities = (p00, p10, p01, p11)
            if any(not isinstance(p, (int, float)) or isinstance(p, bool)
                   or not 0.0 < p < 1.0 for p in probabilities):
                raise ContractError(f"factorial positivity fails for {history_ref}")
            if abs(sum(probabilities) - 1.0) > 1e-12:
                raise ContractError(f"factorial cell probabilities must sum to one for {history_ref}")


@dataclass(frozen=True)
class FactorialAssignment:
    unit_id: str
    history_ref: str
    cell_id: FactorialCell
    a_arm: int
    m_arm: int
    assignment_probability: float
    assigned_vector: Vector4
    assigned_vector_sha256: str
    policy_fingerprint: str
    r_common_fingerprint: str


@dataclass(frozen=True)
class FactorialAssignmentBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    mechanism_id: str
    mechanism_version: str
    mechanism_sha256: str
    factor_m_id: str
    factor_m_version: str
    factor_m_sha256: str
    randomization_salt_sha256: str
    q_x_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    assignments: tuple[FactorialAssignment, ...]
    result_sha256: str

    def validate(
        self, world: SyntheticWorldBundle, config: FactorialAssignmentConfig,
        g_a0: Sequence[JointPolicyHistory], g_a1: Sequence[JointPolicyHistory],
        feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
        r_common_certificates: Sequence[RCommonPairCertificate],
    ) -> None:
        config.validate(world)
        refs = {row.history_ref for row in world.q_x}
        policy_maps = []
        for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
            mapping = {row.history_ref: row for row in rows}
            if len(mapping) != len(rows) or set(mapping) != refs:
                raise ContractError(f"{label} must cover q_X* histories exactly")
            for history_ref, policy in mapping.items():
                total = sum(p for _, p in policy.distribution)
                if (not policy.distribution or any(not 0.0 < p <= 1.0 for _, p in policy.distribution)
                        or abs(total - 1.0) > 1e-12):
                    raise ContractError(f"{label} distribution is invalid for {history_ref}")
                feasible = {digest(v) for v in feasible_vectors_by_history.get(history_ref, ())}
                if not feasible or any(digest(v) not in feasible for v, _ in policy.distribution):
                    raise ContractError(f"{label} support is not jointly feasible for {history_ref}")
            policy_maps.append(mapping)
        certs = {row.history_ref: row for row in r_common_certificates}
        if len(certs) != len(r_common_certificates) or set(certs) != refs:
            raise ContractError("one r_common certificate is required per q_X* history")
        if any(c.status != "COMMON_FIXED" or not c.regime_id or not c.regime_version
               or not c.g_a0_fingerprint or c.g_a0_fingerprint != c.g_a1_fingerprint
               for c in certs.values()):
            raise ContractError("factorial assignment requires fixed common r_common")
        if len({(c.regime_id, c.regime_version, c.g_a0_fingerprint) for c in certs.values()}) != 1:
            raise ContractError("r_common identity/version/fingerprint must be common across q_X*")
        unit_by_ref = {u.d2_baseline.baseline_history_ref: u.unit_id for u in world.units}
        probability_map = {row[0]: row[1:] for row in config.probability_by_history}
        seen = {}
        for row in self.assignments:
            if row.history_ref in seen or row.history_ref not in refs:
                raise ContractError("factorial assignment must contain one unique row per q_X* unit")
            seen[row.history_ref] = row
            if row.unit_id != unit_by_ref[row.history_ref] or row.cell_id not in ("00", "10", "01", "11"):
                raise ContractError("factorial assignment unit/cell binding is invalid")
            a, m = int(row.cell_id[0]), int(row.cell_id[1])
            if (row.a_arm, row.m_arm) != (a, m):
                raise ContractError("factorial cell id does not match its A/M factor values")
            cell_index = ("00", "10", "01", "11").index(row.cell_id)
            if row.assignment_probability != probability_map[row.history_ref][cell_index]:
                raise ContractError("factorial assignment probability differs from declared cell mechanism")
            policy = policy_maps[a][row.history_ref]
            if row.policy_fingerprint != digest(policy.distribution):
                raise ContractError("factorial assigned policy fingerprint mismatch")
            if row.assigned_vector_sha256 != digest(row.assigned_vector):
                raise ContractError("factorial assigned vector fingerprint mismatch")
            if row.assigned_vector_sha256 not in {digest(v) for v, _ in policy.distribution}:
                raise ContractError("factorial assigned vector is outside selected g_A support")
            if row.r_common_fingerprint != certs[row.history_ref].g_a0_fingerprint:
                raise ContractError("factorial assignment is detached from common r_common")
        if set(seen) != refs:
            raise ContractError("factorial assignment roster does not cover q_X* exactly")
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("factorial assignment world/DGP identity mismatch")
        expected = (
            config.mechanism_id, config.mechanism_version, digest(config),
            config.factor_m_id, config.factor_m_version,
            digest((config.factor_m_id, config.factor_m_version)),
            digest(config.randomization_salt), digest(world.q_x),
            digest(tuple(g_a0)), digest(tuple(g_a1)),
            digest(tuple(r_common_certificates)),
        )
        actual = (
            self.mechanism_id, self.mechanism_version, self.mechanism_sha256,
            self.factor_m_id, self.factor_m_version, self.factor_m_sha256,
            self.randomization_salt_sha256, self.q_x_sha256,
            self.g_a0_sha256, self.g_a1_sha256, self.r_common_sha256,
        )
        if actual != expected:
            raise ContractError("factorial assignment provenance fingerprints mismatch")
        payload = _assignment_payload(self)
        if self.result_sha256 != digest(payload):
            raise ContractError("factorial assignment bundle digest mismatch")


def _assignment_payload(bundle: FactorialAssignmentBundle) -> dict:
    return {
        "world_id": bundle.world_id, "world_version": bundle.world_version,
        "dgp_id": bundle.dgp_id, "dgp_version": bundle.dgp_version,
        "mechanism_id": bundle.mechanism_id, "mechanism_version": bundle.mechanism_version,
        "mechanism_sha256": bundle.mechanism_sha256,
        "factor_m_id": bundle.factor_m_id, "factor_m_version": bundle.factor_m_version,
        "factor_m_sha256": bundle.factor_m_sha256,
        "randomization_salt_sha256": bundle.randomization_salt_sha256,
        "q_x_sha256": bundle.q_x_sha256, "g_a0_sha256": bundle.g_a0_sha256,
        "g_a1_sha256": bundle.g_a1_sha256, "r_common_sha256": bundle.r_common_sha256,
        "assignments": bundle.assignments,
    }


def generate_factorial_assignments(
    world: SyntheticWorldBundle, config: FactorialAssignmentConfig,
    g_a0: Sequence[JointPolicyHistory], g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
) -> FactorialAssignmentBundle:
    """Randomize one of four A×M cells per unit with known positive probability."""
    config.validate(world)
    refs = {row.history_ref for row in world.q_x}
    policies = []
    for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in rows}
        if len(mapping) != len(rows) or set(mapping) != refs:
            raise ContractError(f"{label} must cover q_X* histories exactly")
        policies.append(mapping)
    probabilities = {row[0]: row[1:] for row in config.probability_by_history}
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != refs:
        raise ContractError("factorial assignment requires one r_common certificate per q_X* history")
    assignments = []
    for unit, qx in zip(world.units, world.q_x):
        p00, p10, p01, p11 = probabilities[qx.history_ref]
        cell_probs = (("00", p00), ("10", p10), ("01", p01), ("11", p11))
        draw = _dgp_uniform(world.seed_commitment_sha256, config.randomization_salt,
                            unit.unit_id, "theta-am-factorial-cell")
        cumulative = 0.0
        cell: FactorialCell = "11"
        for candidate, probability in cell_probs:
            cumulative += probability
            if draw < cumulative:
                cell = candidate  # type: ignore[assignment]
                break
        a, m = int(cell[0]), int(cell[1])
        policy = policies[a][qx.history_ref]
        vector_draw = _dgp_uniform(world.seed_commitment_sha256, config.randomization_salt,
                                   unit.unit_id, cell, "theta-am-factorial-vector")
        cumulative_vector = 0.0
        vector = policy.distribution[-1][0]
        for candidate, probability in policy.distribution:
            cumulative_vector += probability
            if vector_draw < cumulative_vector:
                vector = candidate
                break
        cert = certs[qx.history_ref]
        assignments.append(FactorialAssignment(
            unit_id=unit.unit_id, history_ref=qx.history_ref, cell_id=cell,
            a_arm=a, m_arm=m, assignment_probability=dict(cell_probs)[cell],
            assigned_vector=vector, assigned_vector_sha256=digest(vector),
            policy_fingerprint=digest(policy.distribution),
            r_common_fingerprint=cert.g_a0_fingerprint,
        ))
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "mechanism_id": config.mechanism_id, "mechanism_version": config.mechanism_version,
        "mechanism_sha256": digest(config),
        "factor_m_id": config.factor_m_id, "factor_m_version": config.factor_m_version,
        "factor_m_sha256": digest((config.factor_m_id, config.factor_m_version)),
        "randomization_salt_sha256": digest(config.randomization_salt),
        "q_x_sha256": digest(world.q_x), "g_a0_sha256": digest(tuple(g_a0)),
        "g_a1_sha256": digest(tuple(g_a1)),
        "r_common_sha256": digest(tuple(r_common_certificates)),
        "assignments": tuple(assignments),
    }
    bundle = FactorialAssignmentBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        config.mechanism_id, config.mechanism_version, digest(config),
        config.factor_m_id, config.factor_m_version,
        digest((config.factor_m_id, config.factor_m_version)),
        digest(config.randomization_salt), digest(world.q_x), digest(tuple(g_a0)),
        digest(tuple(g_a1)), digest(tuple(r_common_certificates)),
        tuple(assignments), digest(payload),
    )
    bundle.validate(world, config, g_a0, g_a1, feasible_vectors_by_history, r_common_certificates)
    return bundle


@dataclass(frozen=True)
class FactorialHistorySelection:
    assignment_bundle_sha256: str
    selected_history_manifest: tuple[tuple[str, str, str, str], ...]


def select_factorial_potential_histories(
    assignments: FactorialAssignmentBundle,
    potential_histories: dict[tuple[str, str, str, int], EventHistory],
) -> tuple[tuple[EventHistory, ...], FactorialHistorySelection]:
    """Select exactly the realized A×M potential history for each assigned unit."""
    selected = []
    manifest = []
    for assignment in assignments.assignments:
        key = (assignment.history_ref, assignment.assigned_vector_sha256,
               assignment.r_common_fingerprint, assignment.m_arm)
        history = potential_histories.get(key)
        if history is None:
            raise ContractError("assigned factorial potential EventHistory is missing")
        expected_potential_id = (
            f"{assignment.unit_id}:G_AxM:{assignments.factor_m_id}:"
            f"{assignments.factor_m_version}:{assignment.assigned_vector_sha256}:"
            f"{assignment.r_common_fingerprint}:M{assignment.m_arm}"
        )
        if (history.unit_id != assignment.unit_id
                or history.history_ref != assignment.history_ref
                or history.world_id != assignments.world_id
                or history.world_version != assignments.world_version
                or history.dgp_version != assignments.dgp_version
                or history.potential_id != expected_potential_id):
            raise ContractError("selected factorial history does not match exact A×M assignment/world provenance")
        selected.append(history)
        manifest.append((assignment.unit_id, history.history_id,
                         history.content_sha256, history.potential_id))
    if len({row[0] for row in manifest}) != len(assignments.assignments):
        raise ContractError("factorial history selection contains duplicate units")
    return tuple(selected), FactorialHistorySelection(assignments.result_sha256, tuple(manifest))


def materialize_factorial_potentials(
    world: SyntheticWorldBundle, functional_history_config: FunctionalHistoryDGPConfig,
    g_a0: Sequence[JointPolicyHistory], g_a1: Sequence[JointPolicyHistory],
    r_common_certificates: Sequence[RCommonPairCertificate],
    initial_state_by_history,
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    assignment_config: FactorialAssignmentConfig,
):
    """Generate all A×M potentials and one randomized realized assignment bundle."""
    potentials = generate_factorial_event_history_potentials(
        world, functional_history_config, g_a0, g_a1, r_common_certificates,
        initial_state_by_history, factor_m_id=assignment_config.factor_m_id,
        factor_m_version=assignment_config.factor_m_version,
    )
    assignments = generate_factorial_assignments(
        world, assignment_config, g_a0, g_a1,
        feasible_vectors_by_history, r_common_certificates,
    )
    selected, selection = select_factorial_potential_histories(assignments, potentials)
    return potentials, assignments, selected, selection


@dataclass(frozen=True)
class FactorialIntervalObservationRecord:
    """One realized cell assignment joined to one interval-only S3 observation."""
    run_id: str
    unit_id: str
    history_ref: str
    assignment_bundle_sha256: str
    q_x_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    factor_m_id: str
    factor_m_version: str
    factor_m_sha256: str
    assigned_cell: FactorialCell
    a_arm: int
    m_arm: int
    assignment_probability: float
    assigned_vector_sha256: str
    policy_fingerprint: str
    r_common_fingerprint: str
    history_id: str
    history_version: str
    history_content_sha256: str
    observation_id: str
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
    temporal_resolution: Literal["INTERVAL_LEVEL"] = "INTERVAL_LEVEL"


def compose_factorial_interval_s3_records(
    assignments: FactorialAssignmentBundle,
    selection: FactorialHistorySelection,
    histories: Sequence[EventHistory],
    grids_by_history_ref,
    monitor_configs_by_history_ref,
    seeds_by_unit: dict[str, int],
) -> tuple[FactorialIntervalObservationRecord, ...]:
    """Project only the realized factorial history into interval S3 observations."""
    from theta_a_interval_observation import project_interval_s3
    if selection.assignment_bundle_sha256 != assignments.result_sha256:
        raise ContractError("factorial S3 selection is detached from its assignment bundle")
    history_by_id = {row.history_id: row for row in histories}
    if len(history_by_id) != len(histories):
        raise ContractError("duplicate EventHistory IDs in factorial S3 composition")
    selected = {u: (hid, sha, pid) for u, hid, sha, pid in selection.selected_history_manifest}
    roster = {row.unit_id for row in assignments.assignments}
    if set(selected) != roster or set(seeds_by_unit) != roster:
        raise ContractError("factorial S3 requires exact assignment/selection/seed roster coverage")
    records = []
    for assignment in assignments.assignments:
        history_id, history_sha, potential_id = selected[assignment.unit_id]
        history = history_by_id.get(history_id)
        if history is None or (
            history.unit_id, history.history_id, history.content_sha256,
            history.potential_id, history.history_ref, history.world_id,
            history.world_version, history.dgp_version,
        ) != (
            assignment.unit_id, history_id, history_sha, potential_id,
            assignment.history_ref, assignments.world_id,
            assignments.world_version, assignments.dgp_version,
        ):
            raise ContractError("factorial realized EventHistory provenance mismatch")
        grid = grids_by_history_ref.get(assignment.history_ref)
        monitor = monitor_configs_by_history_ref.get(assignment.history_ref)
        if grid is None or monitor is None:
            raise ContractError("factorial S3 requires one grid and monitor config per q_X history")
        projected = project_interval_s3(history, grid, monitor, seed=seeds_by_unit[assignment.unit_id])
        for row in projected:
            records.append(FactorialIntervalObservationRecord(
                run_id=history.run_id, unit_id=assignment.unit_id,
                history_ref=assignment.history_ref,
                assignment_bundle_sha256=assignments.result_sha256,
                q_x_sha256=assignments.q_x_sha256,
                g_a0_sha256=assignments.g_a0_sha256,
                g_a1_sha256=assignments.g_a1_sha256,
                r_common_sha256=assignments.r_common_sha256,
                factor_m_id=assignments.factor_m_id,
                factor_m_version=assignments.factor_m_version,
                factor_m_sha256=assignments.factor_m_sha256,
                assigned_cell=assignment.cell_id, a_arm=assignment.a_arm,
                m_arm=assignment.m_arm,
                assignment_probability=assignment.assignment_probability,
                assigned_vector_sha256=assignment.assigned_vector_sha256,
                policy_fingerprint=assignment.policy_fingerprint,
                r_common_fingerprint=assignment.r_common_fingerprint,
                history_id=history.history_id, history_version=history.history_version,
                history_content_sha256=history.content_sha256,
                observation_id=row.observation_id, interval_index=row.interval_index,
                interval_start=row.interval_start, interval_end=row.interval_end,
                observed_compliance=row.observed_compliance,
                observation_status=row.observation_status, coverage_mode=row.coverage_mode,
                capture_time=row.capture_time, ingestion_time=row.ingestion_time,
                monitor_id=row.monitor_id, monitor_version=row.monitor_version,
                grid_id=row.grid_id, grid_version=row.grid_version,
            ))
    if len({row.observation_id for row in records}) != len(records):
        raise ContractError("factorial S3 observation IDs must be unique")
    return tuple(records)


@dataclass(frozen=True)
class FactorialEvidenceCandidate:
    run_id: str
    rows: tuple[dict, ...]


@dataclass(frozen=True)
class SealedFactorialEvidence:
    run_id: str
    rows: tuple[dict, ...]
    manifest: dict
    sha256: str


def _plain(value):
    if isinstance(value, Decimal):
        return str(value)
    if is_dataclass(value):
        return _plain(asdict(value))
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in sorted(value.items())}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _canonical_sha256(value) -> str:
    raw = json.dumps(_plain(value), sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def factorial_candidate_from_records(records) -> FactorialEvidenceCandidate:
    if not records:
        raise ContractError("cannot create factorial evidence from empty S3 records")
    run_ids = {row.run_id for row in records}
    if len(run_ids) != 1:
        raise ContractError("factorial S3 records contain multiple run identities")
    return FactorialEvidenceCandidate(next(iter(run_ids)),
                                       tuple(asdict(row) for row in records))


class FactorialIntervalSealer:
    """Closed-schema firewall for realized factorial interval observations."""
    version = "c10s-factorial-interval-sealer-0.1"

    def seal(self, candidate: FactorialEvidenceCandidate) -> SealedFactorialEvidence:
        allowed = frozenset(FactorialIntervalObservationRecord.__dataclass_fields__)
        if not candidate.run_id or not candidate.rows:
            raise ContractError("factorial evidence requires run identity and rows")
        seen = set()
        units = {}
        rows_out = []
        for row in candidate.rows:
            if set(row) != allowed or row.get("temporal_resolution") != "INTERVAL_LEVEL":
                raise ContractError("factorial interval row violates its closed schema")
            if row["run_id"] != candidate.run_id:
                raise ContractError("factorial interval run identity mismatch")
            string_fields = (
                "unit_id", "history_ref", "assignment_bundle_sha256", "q_x_sha256",
                "g_a0_sha256", "g_a1_sha256", "r_common_sha256", "factor_m_id",
                "factor_m_version", "factor_m_sha256", "assigned_vector_sha256",
                "policy_fingerprint", "r_common_fingerprint", "history_id",
                "history_version", "history_content_sha256", "observation_id",
                "monitor_id", "monitor_version", "grid_id", "grid_version",
            )
            if any(not isinstance(row[k], str) or not row[k] for k in string_fields):
                raise ContractError("factorial interval identity/version fields are mandatory")
            cell = row["assigned_cell"]
            if cell not in ("00", "10", "01", "11"):
                raise ContractError("factorial cell must be one of 00, 10, 01, 11")
            if (row["a_arm"], row["m_arm"]) != (int(cell[0]), int(cell[1])):
                raise ContractError("factorial cell and factor values disagree")
            p = row["assignment_probability"]
            if not isinstance(p, (int, float)) or isinstance(p, bool) or not 0.0 < p < 1.0:
                raise ContractError("factorial assignment probability must be in (0,1)")
            if row["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE":
                raise ContractError("factorial strict V_cont requires certified continuous event coverage")
            if row["observation_status"] not in ("OBSERVED", "MISSING"):
                raise ContractError("invalid factorial interval observation status")
            value = row["observed_compliance"]
            if (row["observation_status"] == "MISSING") != (value is None):
                raise ContractError("factorial interval value and missingness status disagree")
            if value is not None and type(value) is not bool:
                raise ContractError("factorial interval compliance must be Boolean or missing")
            if type(row["interval_index"]) is not int or row["interval_index"] < 0:
                raise ContractError("factorial interval index must be non-negative")
            times = (row["interval_start"], row["interval_end"],
                     row["capture_time"], row["ingestion_time"])
            if any(not isinstance(t, Decimal) or not t.is_finite() for t in times):
                raise ContractError("factorial interval chronology must use finite Decimal values")
            if not times[0] < times[1] <= times[2] <= times[3]:
                raise ContractError("factorial interval/capture/ingestion chronology is invalid")
            if row["observation_id"] in seen:
                raise ContractError("duplicate factorial interval observation ID")
            seen.add(row["observation_id"])
            invariant = tuple(row[k] for k in (
                "assignment_bundle_sha256", "q_x_sha256", "g_a0_sha256", "g_a1_sha256",
                "r_common_sha256", "factor_m_id", "factor_m_version", "factor_m_sha256",
                "assigned_cell", "a_arm", "m_arm", "assignment_probability",
                "assigned_vector_sha256", "policy_fingerprint", "r_common_fingerprint",
                "history_ref", "history_id", "history_version", "history_content_sha256",
            ))
            bucket = units.setdefault(row["unit_id"], {"invariant": invariant, "rows": []})
            if bucket["invariant"] != invariant:
                raise ContractError("factorial assignment/history fields vary within a unit")
            bucket["rows"].append(row)
            rows_out.append(dict(row))
        common_grid = None
        common_bounds = None
        for unit, bucket in units.items():
            ordered = sorted(bucket["rows"], key=lambda x: x["interval_index"])
            if [r["interval_index"] for r in ordered] != list(range(len(ordered))):
                raise ContractError(f"factorial interval coverage has gaps for unit {unit}")
            grid = (ordered[0]["grid_id"], ordered[0]["grid_version"])
            bounds = tuple((r["interval_start"], r["interval_end"]) for r in ordered)
            if any((r["grid_id"], r["grid_version"]) != grid for r in ordered):
                raise ContractError("factorial grid identity varies within a unit")
            if any(left[1] != right[0] for left, right in zip(bounds, bounds[1:])):
                raise ContractError("factorial interval coverage has a gap or overlap")
            if common_grid is None:
                common_grid, common_bounds = grid, bounds
            elif grid != common_grid or bounds != common_bounds:
                raise ContractError("factorial units must share one exact interval grid")
        global_fields = (
            "assignment_bundle_sha256", "q_x_sha256", "g_a0_sha256",
            "g_a1_sha256", "r_common_sha256", "factor_m_id",
            "factor_m_version", "factor_m_sha256",
        )
        if any(row[k] != rows_out[0][k] for row in rows_out for k in global_fields):
            raise ContractError("factorial evidence mixes assignment, population, policy or M provenance")
        manifest = {
            "run_id": candidate.run_id, "schema": "C10S-FACTORIAL-AxM-S3-INTERVAL-001",
            "sealer_version": self.version, "row_count": len(rows_out),
            "unit_count": len(units), "temporal_resolution": "INTERVAL_LEVEL",
            "grid_id": common_grid[0], "grid_version": common_grid[1],
            "interval_count_per_unit": len(common_bounds),
            "assignment_bundle_sha256": rows_out[0]["assignment_bundle_sha256"],
            "q_x_sha256": rows_out[0]["q_x_sha256"],
            "factor_m_id": rows_out[0]["factor_m_id"],
            "factor_m_version": rows_out[0]["factor_m_version"],
            "factor_m_sha256": rows_out[0]["factor_m_sha256"],
        }
        return SealedFactorialEvidence(candidate.run_id, tuple(rows_out), manifest,
                                       _canonical_sha256({"manifest": manifest, "rows": rows_out}))


@dataclass(frozen=True)
class FactorialAnalysisContract:
    q_x_mass_by_history: tuple[tuple[str, float], ...]
    expected_unit_ids: tuple[str, ...]
    probability_by_history: tuple[tuple[str, float, float, float, float], ...]
    q_x_sha256: str
    assignment_bundle_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    factor_m_id: str
    factor_m_version: str
    factor_m_sha256: str
    estimand_version: str = "1.0"

    def validate(self) -> None:
        if not all((self.q_x_sha256, self.assignment_bundle_sha256,
                    self.g_a0_sha256, self.g_a1_sha256, self.r_common_sha256,
                    self.factor_m_id, self.factor_m_version, self.factor_m_sha256,
                    self.estimand_version)):
            raise ContractError("factorial analysis provenance and estimand versions are mandatory")
        qx = dict(self.q_x_mass_by_history)
        if not qx or len(qx) != len(self.q_x_mass_by_history):
            raise ContractError("factorial q_X target masses must have unique nonempty support")
        if any(not k or not isinstance(v, (int, float)) or not 0 < v < 1.0000000001
               for k, v in qx.items()):
            raise ContractError("factorial q_X masses must be positive and finite")
        if abs(sum(qx.values()) - 1.0) > 1e-10:
            raise ContractError("factorial q_X masses must sum to one")
        if (not self.expected_unit_ids or len(self.expected_unit_ids) != len(set(self.expected_unit_ids))
                or len(self.expected_unit_ids) != len(qx)):
            raise ContractError("factorial analysis requires the exact unique q_X unit roster")
        probabilities = {row[0]: row[1:] for row in self.probability_by_history}
        if len(probabilities) != len(self.probability_by_history) or set(probabilities) != set(qx):
            raise ContractError("factorial analysis cell probabilities must cover q_X exactly")
        for ref, values in probabilities.items():
            if (len(values) != 4 or any(not 0.0 < p < 1.0 for p in values)
                    or abs(sum(values) - 1.0) > 1e-12):
                raise ContractError(f"factorial analysis cell probabilities are invalid for {ref}")


@dataclass(frozen=True)
class FactorialContrast:
    """Point estimate plus measurement-only missingness bounds; not a sampling CI."""
    estimand_id: str
    point_estimate: float | None
    lower_bound: float | None
    upper_bound: float | None
    identification: Literal["IDENTIFIED", "PARTIALLY_IDENTIFIED", "NOT_IDENTIFIED"]


@dataclass(frozen=True)
class FactorialAnalysisResult:
    run_id: str
    estimand_version: str
    cell_unit_counts: tuple[int, int, int, int]
    cell_means: tuple[float | None, float | None, float | None, float | None]
    cell_lower_bounds: tuple[float | None, float | None, float | None, float | None]
    cell_upper_bounds: tuple[float | None, float | None, float | None, float | None]
    contrasts: tuple[FactorialContrast, ...]
    missing_interval_count: int
    total_interval_count: int
    input_sha256: str
    output_sha256: str


def _factorial_result_payload(result: FactorialAnalysisResult) -> dict:
    return {
        "run_id": result.run_id, "estimand_version": result.estimand_version,
        "cell_unit_counts": result.cell_unit_counts, "cell_means": result.cell_means,
        "cell_lower_bounds": result.cell_lower_bounds,
        "cell_upper_bounds": result.cell_upper_bounds,
        "contrasts": result.contrasts,
        "missing_interval_count": result.missing_interval_count,
        "total_interval_count": result.total_interval_count,
        "input_sha256": result.input_sha256,
    }


class FactorialObservationAnalyzer:
    """Observation-only HT analysis of both simple effects and A×M interaction."""
    version = "c10s-factorial-observation-analyzer-0.1"

    def analyze(self, evidence: SealedFactorialEvidence,
                contract: FactorialAnalysisContract) -> FactorialAnalysisResult:
        contract.validate()
        if (not evidence.rows
                or _canonical_sha256({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256):
            raise ContractError("factorial Analyzer requires nonempty evidence with a valid seal")
        qx = dict(contract.q_x_mass_by_history)
        expected_units = set(contract.expected_unit_ids)
        by_unit = {}
        for row in evidence.rows:
            if (row["assignment_bundle_sha256"] != contract.assignment_bundle_sha256
                    or row["q_x_sha256"] != contract.q_x_sha256
                    or row["g_a0_sha256"] != contract.g_a0_sha256
                    or row["g_a1_sha256"] != contract.g_a1_sha256
                    or row["r_common_sha256"] != contract.r_common_sha256
                    or row["factor_m_id"] != contract.factor_m_id
                    or row["factor_m_version"] != contract.factor_m_version
                    or row["factor_m_sha256"] != contract.factor_m_sha256):
                raise ContractError("factorial evidence does not match the frozen analysis contract")
            by_unit.setdefault(row["unit_id"], []).append(row)
        if set(by_unit) != expected_units:
            raise ContractError("factorial evidence must cover the exact assigned-unit roster")
        observed_histories = {rows[0]["history_ref"] for rows in by_unit.values()}
        if observed_histories != set(qx):
            raise ContractError("factorial evidence must cover each q_X history exactly once")
        cell_order = ("00", "10", "01", "11")
        cell_items = {cell: [] for cell in cell_order}
        missing_count = total_count = 0
        common_grid = common_bounds = None
        for unit, bucket in by_unit.items():
            first = bucket[0]
            if first["history_ref"] not in qx:
                raise ContractError("factorial evidence history falls outside q_X target support")
            invariant_fields = (
                "history_ref", "assignment_bundle_sha256", "q_x_sha256",
                "g_a0_sha256", "g_a1_sha256", "r_common_sha256", "factor_m_id",
                "factor_m_version", "factor_m_sha256", "assigned_cell", "a_arm",
                "m_arm", "assignment_probability", "assigned_vector_sha256",
                "policy_fingerprint", "r_common_fingerprint", "history_id",
                "history_version", "history_content_sha256",
            )
            if any(any(row[k] != first[k] for k in invariant_fields) for row in bucket):
                raise ContractError("factorial unit assignment/history provenance varies across intervals")
            cell = first["assigned_cell"]
            if cell not in cell_order or (first["a_arm"], first["m_arm"]) != (int(cell[0]), int(cell[1])):
                raise ContractError("factorial unit cell encoding is invalid")
            probability_index = cell_order.index(cell)
            expected_probability = dict((ref, values) for ref, *values in contract.probability_by_history)[first["history_ref"]][probability_index]
            if first["assignment_probability"] != expected_probability:
                raise ContractError("factorial evidence probability differs from the declared randomization design")
            ordered = sorted(bucket, key=lambda x: x["interval_index"])
            if [r["interval_index"] for r in ordered] != list(range(len(ordered))):
                raise ContractError("factorial interval sequence has gaps or duplicate indices")
            grid = (ordered[0]["grid_id"], ordered[0]["grid_version"])
            bounds = tuple((r["interval_start"], r["interval_end"]) for r in ordered)
            if any((r["grid_id"], r["grid_version"]) != grid for r in ordered):
                raise ContractError("factorial interval grid changes within a unit")
            if any(a[1] != b[0] for a, b in zip(bounds, bounds[1:])):
                raise ContractError("factorial interval sequence has a temporal gap or overlap")
            if common_grid is None:
                common_grid, common_bounds = grid, bounds
            elif grid != common_grid or bounds != common_bounds:
                raise ContractError("factorial units do not share one exact interval grid")
            if any(r["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE" for r in ordered):
                raise ContractError("factorial V_cont analysis requires certified continuous coverage")
            if any((r["observation_status"] == "MISSING") != (r["observed_compliance"] is None)
                   for r in ordered):
                raise ContractError("factorial interval missingness/value coding is inconsistent")
            missing = sum(r["observation_status"] == "MISSING" for r in ordered)
            n = len(ordered)
            if n == 0:
                raise ContractError("factorial unit must have at least one interval")
            missing_count += missing
            total_count += n
            # V_cont is strict continuity across the complete horizon, not an
            # average interval-compliance score. Any observed failure fixes 0;
            # all-true observed intervals plus missing intervals leave {0,1}.
            observed_failure = any(
                r["observation_status"] == "OBSERVED" and r["observed_compliance"] is False
                for r in ordered
            )
            if observed_failure:
                lo, hi = 0.0, 0.0
            elif missing:
                lo, hi = 0.0, 1.0
            else:
                lo, hi = 1.0, 1.0
            probability = first["assignment_probability"]
            if not isinstance(probability, (int, float)) or isinstance(probability, bool) or not 0 < probability < 1:
                raise ContractError("factorial cell assignment probability is invalid")
            cell_items[cell].append((qx[first["history_ref"]] / probability, lo, hi))
        counts = tuple(len(cell_items[cell]) for cell in cell_order)
        cell_means = []
        cell_lowers = []
        cell_uppers = []
        for cell in cell_order:
            items = cell_items[cell]
            if not items:
                cell_means.append(None)
                cell_lowers.append(None)
                cell_uppers.append(None)
            else:
                lower = sum(w * lo for w, lo, hi in items)
                upper = sum(w * hi for w, lo, hi in items)
                cell_lowers.append(lower)
                cell_uppers.append(upper)
                cell_means.append(lower if lower == upper else None)
        contrasts = []
        specs = (
            ("THETA_A_GIVEN_M0", ((1, 1), (0, -1))),
            ("THETA_A_GIVEN_M1", ((3, 1), (2, -1))),
            ("THETA_AxM_INTERACTION", ((3, 1), (2, -1), (1, -1), (0, 1))),
        )
        for estimand_id, terms in specs:
            term_indices = tuple(i for i, _ in terms)
            if any(cell_items[cell_order[i]] == [] for i in term_indices):
                contrasts.append(FactorialContrast(
                    estimand_id, None, None, None, "NOT_IDENTIFIED",
                ))
                continue
            lower = sum(cell_lowers[i] if sign > 0 else -cell_uppers[i]
                        for i, sign in terms)
            upper = sum(cell_uppers[i] if sign > 0 else -cell_lowers[i]
                        for i, sign in terms)
            if all(cell_means[i] is not None for i in term_indices):
                point = sum(sign * cell_means[i] for i, sign in terms)
                status = "IDENTIFIED"
            else:
                point, status = None, "PARTIALLY_IDENTIFIED"
            contrasts.append(FactorialContrast(estimand_id, point, lower, upper, status))
        provisional = FactorialAnalysisResult(
            evidence.run_id, contract.estimand_version, counts, tuple(cell_means),
            tuple(cell_lowers), tuple(cell_uppers), tuple(contrasts),
            missing_count, total_count, evidence.sha256, "",
        )
        return FactorialAnalysisResult(
            provisional.run_id, provisional.estimand_version, provisional.cell_unit_counts,
            provisional.cell_means, provisional.cell_lower_bounds, provisional.cell_upper_bounds,
            provisional.contrasts, provisional.missing_interval_count,
            provisional.total_interval_count, provisional.input_sha256,
            _canonical_sha256(_factorial_result_payload(provisional)),
        )


@dataclass(frozen=True)
class FactorialTruthBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    factor_m_id: str
    factor_m_version: str
    estimand_version: str
    cell_means: tuple[float, float, float, float]
    theta_a_given_m0: float
    theta_a_given_m1: float
    theta_am_interaction: float
    q_x_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    grid_id: str
    grid_version: str
    event_history_manifest: tuple[tuple[str, str, str, int, str, str], ...]
    evaluator_only: bool
    result_sha256: str

    def validate(self) -> None:
        if (not self.evaluator_only or not all((
            self.world_id, self.world_version, self.dgp_id, self.dgp_version,
            self.factor_m_id, self.factor_m_version, self.estimand_version,
            self.q_x_sha256, self.g_a0_sha256, self.g_a1_sha256,
            self.r_common_sha256, self.grid_id, self.grid_version,
        ))):
            raise ContractError("factorial truth must be fully identified and evaluator-only")
        if len(self.cell_means) != 4 or any(not isinstance(v, (int, float)) for v in self.cell_means):
            raise ContractError("factorial truth requires four finite cell means")
        if any(not __import__("math").isfinite(v) or not 0.0 <= v <= 1.0
               for v in self.cell_means):
            raise ContractError("strict binary V_cont cell truths must be finite and in [0,1]")
        if (not self.event_history_manifest
                or len({row[4] for row in self.event_history_manifest}) != len(self.event_history_manifest)
                or any(row[3] not in (0, 1) for row in self.event_history_manifest)):
            raise ContractError("factorial truth requires unique, explicitly indexed M potential histories")
        mu00, mu10, mu01, mu11 = self.cell_means
        expected = (mu10 - mu00, mu11 - mu01, (mu11 - mu01) - (mu10 - mu00))
        actual = (self.theta_a_given_m0, self.theta_a_given_m1, self.theta_am_interaction)
        if any(abs(a - b) > 1e-12 for a, b in zip(expected, actual)):
            raise ContractError("factorial truth contrasts do not match the four cell means")
        payload = _factorial_truth_payload(self)
        if self.result_sha256 != _canonical_sha256(payload):
            raise ContractError("factorial reserved truth digest mismatch")


def _factorial_truth_payload(truth: FactorialTruthBundle) -> dict:
    return {
        "world_id": truth.world_id, "world_version": truth.world_version,
        "dgp_id": truth.dgp_id, "dgp_version": truth.dgp_version,
        "factor_m_id": truth.factor_m_id, "factor_m_version": truth.factor_m_version,
        "estimand_version": truth.estimand_version, "cell_means": truth.cell_means,
        "theta_a_given_m0": truth.theta_a_given_m0,
        "theta_a_given_m1": truth.theta_a_given_m1,
        "theta_am_interaction": truth.theta_am_interaction,
        "q_x_sha256": truth.q_x_sha256, "g_a0_sha256": truth.g_a0_sha256,
        "g_a1_sha256": truth.g_a1_sha256, "r_common_sha256": truth.r_common_sha256,
        "grid_id": truth.grid_id, "grid_version": truth.grid_version,
        "event_history_manifest": truth.event_history_manifest,
        "evaluator_only": truth.evaluator_only,
    }


def compute_factorial_vcont_truth_from_event_histories(
    world: SyntheticWorldBundle,
    q_x,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    r_common_certificates: Sequence[RCommonPairCertificate],
    potential_histories: dict[tuple[str, str, str, int], EventHistory],
    grid,
    *,
    factor_m_id: str,
    factor_m_version: str,
    estimand_version: str,
) -> FactorialTruthBundle:
    """Reserved four-cell q_X-standardized V_cont truth from all potential histories."""
    from c10s_synthetic_components import adjudicate_intervals
    world.validate()
    grid.validate()
    if tuple(q_x) != world.q_x:
        raise ContractError("factorial truth q_X must match the exact world target population")
    if not factor_m_id or not factor_m_version or not estimand_version:
        raise ContractError("factorial truth requires M and estimand identities/versions")
    qx_by_ref = {row.history_ref: row for row in q_x}
    unit_by_ref = {unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units}
    if set(qx_by_ref) != set(unit_by_ref):
        raise ContractError("factorial truth q_X does not cover the exact world roster")
    policies = []
    for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in rows}
        if len(mapping) != len(rows) or set(mapping) != set(qx_by_ref):
            raise ContractError(f"factorial truth {label} support differs from q_X")
        policies.append(mapping)
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != set(qx_by_ref):
        raise ContractError("factorial truth requires one common-r certificate per q_X history")
    required = set()
    for ref in qx_by_ref:
        cert = certs[ref]
        if cert.status != "COMMON_FIXED" or cert.g_a0_fingerprint != cert.g_a1_fingerprint:
            raise ContractError("factorial truth requires fixed common r_common")
        for policy_map in policies:
            for vector, probability in policy_map[ref].distribution:
                if probability > 0:
                    for m in (0, 1):
                        required.add((ref, digest(vector), cert.g_a0_fingerprint, m))
    if set(potential_histories) != required:
        raise ContractError("factorial EventHistory potentials do not cover exact q_X × A-policy × M support")
    outcome = {}
    manifest = []
    history_ids = set()
    potential_ids = set()
    run_ids = set()
    for key in sorted(required):
        ref, vector_sha, regime_sha, m = key
        history = potential_histories[key]
        history.validate(require_complete=True)
        if (history.unit_id, history.history_ref, history.world_id,
            history.world_version, history.dgp_version) != (
            unit_by_ref[ref], ref, world.world_id, world.world_version, world.dgp_version
        ):
            raise ContractError("factorial potential EventHistory is detached from its world/q_X unit")
        if history.support_start != grid.boundaries[0] or history.support_end != grid.boundaries[-1]:
            raise ContractError("factorial potential histories must share exact V_cont grid support")
        if history.history_id in history_ids or history.potential_id in potential_ids:
            raise ContractError("factorial potential EventHistory IDs must be unique")
        expected_potential_id = (
            f"{unit_by_ref[ref]}:G_AxM:{factor_m_id}:{factor_m_version}:"
            f"{vector_sha}:{regime_sha}:M{m}"
        )
        if history.potential_id != expected_potential_id:
            raise ContractError("factorial EventHistory potential identity does not match its exact A×M key")
        history_ids.add(history.history_id)
        potential_ids.add(history.potential_id)
        run_ids.add(history.run_id)
        outcome[key] = adjudicate_intervals(history, grid).v_cont_truth
        manifest.append((ref, vector_sha, regime_sha, m, history.history_id, history.content_sha256))
    if len(run_ids) != 1:
        raise ContractError("factorial potential histories must belong to one synthetic run")
    cell_means = []
    for cell in ("00", "10", "01", "11"):
        a, m = int(cell[0]), int(cell[1])
        policy_map = policies[a]
        mu = 0.0
        for qx_row in q_x:
            ref = qx_row.history_ref
            cert = certs[ref]
            for vector, probability in policy_map[ref].distribution:
                key = (ref, digest(vector), cert.g_a0_fingerprint, m)
                mu += qx_row.mass * probability * outcome[key]
        cell_means.append(mu)
    mu00, mu10, mu01, mu11 = cell_means
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "factor_m_id": factor_m_id, "factor_m_version": factor_m_version,
        "estimand_version": estimand_version, "cell_means": tuple(cell_means),
        "theta_a_given_m0": mu10 - mu00, "theta_a_given_m1": mu11 - mu01,
        "theta_am_interaction": (mu11 - mu01) - (mu10 - mu00),
        "q_x_sha256": digest(tuple(q_x)), "g_a0_sha256": digest(tuple(g_a0)),
        "g_a1_sha256": digest(tuple(g_a1)),
        "r_common_sha256": digest(tuple(r_common_certificates)),
        "grid_id": grid.grid_id, "grid_version": grid.grid_version,
        "event_history_manifest": tuple(manifest), "evaluator_only": True,
    }
    truth = FactorialTruthBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        factor_m_id, factor_m_version, estimand_version, tuple(cell_means),
        mu10 - mu00, mu11 - mu01, (mu11 - mu01) - (mu10 - mu00),
        digest(tuple(q_x)), digest(tuple(g_a0)), digest(tuple(g_a1)),
        digest(tuple(r_common_certificates)), grid.grid_id, grid.grid_version,
        tuple(manifest), True, _canonical_sha256(payload),
    )
    truth.validate()
    return truth


@dataclass(frozen=True)
class FactorialEvaluationResult:
    estimand_version: str
    truth_contrasts: tuple[float, float, float]
    analyzer_contrasts: tuple[FactorialContrast, ...]
    absolute_errors: tuple[float | None, float | None, float | None]
    truth_within_reported_bounds: tuple[bool | None, bool | None, bool | None]
    correct_adjudication: bool
    disposition: str
    tolerance: float
    evidence_sha256: str
    analyzer_output_sha256: str


def evaluate_factorial_analysis(
    truth: FactorialTruthBundle, evidence: SealedFactorialEvidence,
    result: FactorialAnalysisResult, assignment_bundle: FactorialAssignmentBundle,
    *, tolerance: float,
) -> FactorialEvaluationResult:
    """Evaluator-only comparison; the truth bundle is never an Analyzer input."""
    import math
    truth.validate()
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ContractError("factorial evaluation tolerance must be finite and non-negative")
    if result.run_id != evidence.run_id or result.input_sha256 != evidence.sha256:
        raise ContractError("factorial Analyzer result is detached from supplied sealed evidence")
    if _canonical_sha256({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
        raise ContractError("factorial evidence digest is invalid at evaluation")
    if _canonical_sha256(_factorial_result_payload(result)) != result.output_sha256:
        raise ContractError("factorial Analyzer output digest is invalid")
    if result.estimand_version != truth.estimand_version:
        raise ContractError("factorial Analyzer and reserved truth estimand versions differ")
    if ((
        evidence.manifest.get("factor_m_id"), evidence.manifest.get("factor_m_version"),
        evidence.manifest.get("q_x_sha256"),
        evidence.rows[0].get("g_a0_sha256"), evidence.rows[0].get("g_a1_sha256"),
        evidence.rows[0].get("r_common_sha256"),
    ) != (
        truth.factor_m_id, truth.factor_m_version, truth.q_x_sha256,
        truth.g_a0_sha256, truth.g_a1_sha256, truth.r_common_sha256,
    )):
        raise ContractError("factorial evidence and reserved truth provenance differ")
    if ((
        assignment_bundle.result_sha256, assignment_bundle.q_x_sha256,
        assignment_bundle.g_a0_sha256, assignment_bundle.g_a1_sha256,
        assignment_bundle.r_common_sha256, assignment_bundle.factor_m_id,
        assignment_bundle.factor_m_version, assignment_bundle.factor_m_sha256,
    ) != (
        evidence.manifest.get("assignment_bundle_sha256"), truth.q_x_sha256,
        truth.g_a0_sha256, truth.g_a1_sha256, truth.r_common_sha256,
        truth.factor_m_id, truth.factor_m_version,
        evidence.manifest.get("factor_m_sha256"),
    )):
        raise ContractError("factorial assignment bundle, sealed evidence and reserved truth provenance differ")
    assignment_by_unit = {row.unit_id: row for row in assignment_bundle.assignments}
    if len(assignment_by_unit) != len(assignment_bundle.assignments):
        raise ContractError("factorial assignment bundle contains duplicate unit IDs")
    if {row["unit_id"] for row in evidence.rows} != set(assignment_by_unit):
        raise ContractError("factorial evidence does not cover the exact assigned-unit roster")
    reserved_history_keys = {
        (row[0], row[1], row[2], row[3], row[4], row[5])
        for row in truth.event_history_manifest
    }
    for row in evidence.rows:
        assigned = assignment_by_unit[row["unit_id"]]
        history_key = (
            row["history_ref"], row["assigned_vector_sha256"],
            row["r_common_fingerprint"], row["m_arm"],
            row["history_id"], row["history_content_sha256"],
        )
        if history_key not in reserved_history_keys:
            raise ContractError("realized factorial EventHistory is absent from the reserved potential-history manifest")
        if (
            row["assigned_cell"] != assigned.cell_id
            or row["a_arm"] != assigned.a_arm
            or row["m_arm"] != assigned.m_arm
            or row["assignment_probability"] != assigned.assignment_probability
            or row["assigned_vector_sha256"] != assigned.assigned_vector_sha256
            or row["policy_fingerprint"] != assigned.policy_fingerprint
            or row["r_common_fingerprint"] != assigned.r_common_fingerprint
            or row["history_ref"] != assigned.history_ref
        ):
            raise ContractError("factorial sealed observation does not reproduce its exact randomized assignment")
    truth_values = (truth.theta_a_given_m0, truth.theta_a_given_m1, truth.theta_am_interaction)
    if len(result.contrasts) != 3:
        raise ContractError("factorial Analyzer must report both simple effects and interaction")
    errors = []
    coverage = []
    correct = True
    for expected, contrast in zip(truth_values, result.contrasts):
        if contrast.identification == "IDENTIFIED":
            error = abs(contrast.point_estimate - expected) if contrast.point_estimate is not None else None
            covered = None
            item_correct = error is not None and error <= tolerance
        elif contrast.identification == "PARTIALLY_IDENTIFIED":
            error = None
            covered = None
            item_correct = (contrast.point_estimate is None
                            and contrast.lower_bound is not None
                            and contrast.upper_bound is not None)
        elif contrast.identification == "NOT_IDENTIFIED":
            error, covered, item_correct = (None, None,
                contrast.point_estimate is None and contrast.lower_bound is None
                and contrast.upper_bound is None)
        else:
            raise ContractError("unsupported factorial identification status")
        errors.append(error)
        coverage.append(covered)
        correct = correct and item_correct
    disposition = "CORRECT_RECOVERY_OR_ABSTENTION" if correct else "INCORRECT_FACTORIAL_ADJUDICATION"
    return FactorialEvaluationResult(
        truth.estimand_version, truth_values, result.contrasts, tuple(errors),
        tuple(coverage), correct, disposition, tolerance, evidence.sha256,
        result.output_sha256,
    )
