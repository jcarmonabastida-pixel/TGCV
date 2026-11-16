"""Factorial A×M assignment and potential-history selection for C10-S.

A is the direct focal g_A intervention. M is an independent, versioned
Boolean functional mechanism; it is not a Vector4 coordinate and is not D2/Z.
The module deliberately separates assignment/selection from S3 observation,
analysis, and the reserved factorial oracle.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
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
    policies = []
    for rows in (g_a0, g_a1):
        mapping = {row.history_ref: row for row in rows}
        policies.append(mapping)
    probabilities = {row[0]: row[1:] for row in config.probability_by_history}
    certs = {row.history_ref: row for row in r_common_certificates}
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
        if (history.unit_id != assignment.unit_id
                or history.history_ref != assignment.history_ref
                or history.world_id != assignments.world_id
                or history.world_version != assignments.world_version
                or history.dgp_version != assignments.dgp_version):
            raise ContractError("selected factorial history does not match assignment/world provenance")
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
        {ref: tuple(vector for vector, _ in (
            next(rows for rows in (g_a0, g_a1) if rows[0].history_ref == ref).distribution
        )) for ref in {row.history_ref for row in world.q_x}},
        r_common_certificates,
    )
    selected, selection = select_factorial_potential_histories(assignments, potentials)
    return potentials, assignments, selected, selection
