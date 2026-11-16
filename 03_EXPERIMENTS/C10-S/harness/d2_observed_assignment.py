"""Observed D2 assignment and realized-history selection for C10-S.

This module materializes the randomized Z lane for the D2 cohort. It does
not expose potential outcomes to an Analyzer and does not itself claim to
produce S3 observations or an ITT-Z estimate.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
from typing import Sequence

from c10s_synthetic_components import (
    ContractError,
    D2VContTruthBundle,
    EventHistory,
    SyntheticWorldBundle,
    digest,
)


@dataclass(frozen=True)
class D2ObservedAssignmentConfig:
    mechanism_id: str
    mechanism_version: str
    randomization_salt: str
    probability_z1_by_history: tuple[tuple[str, float], ...]

    def validate(self, world: SyntheticWorldBundle) -> None:
        world.validate()
        refs = {row.history_ref for row in world.q_x}
        supplied = [row[0] for row in self.probability_z1_by_history]
        if not all((self.mechanism_id, self.mechanism_version, self.randomization_salt)):
            raise ContractError("D2 assignment requires mechanism identity, version and randomization salt")
        if len(supplied) != len(set(supplied)) or set(supplied) != refs:
            raise ContractError("D2 assignment probabilities must cover q_X* histories exactly")
        for history_ref, probability in self.probability_z1_by_history:
            if not math.isfinite(probability) or not 0.0 < probability < 1.0:
                raise ContractError(f"D2 assignment positivity fails for {history_ref}")


@dataclass(frozen=True)
class D2ObservedAssignment:
    unit_id: str
    history_ref: str
    assigned_z: int
    probability_z0: float
    probability_z1: float
    selected_history_id: str
    selected_potential_id: str
    assignment_uniform_sha256: str


@dataclass(frozen=True)
class D2ObservedAssignmentBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    mechanism_id: str
    mechanism_version: str
    mechanism_sha256: str
    randomization_salt_sha256: str
    q_x_sha256: str
    assignments: tuple[D2ObservedAssignment, ...]
    result_sha256: str

    def validate(
        self,
        world: SyntheticWorldBundle,
        truth: D2VContTruthBundle,
        histories_by_unit_z: dict[tuple[str, int], EventHistory],
    ) -> None:
        world.validate()
        truth.validate(world, histories_by_unit_z, _grid_from_truth_unavailable())
        # The full truth validation is performed by the caller with its actual
        # IntervalGrid. Here we validate assignment-to-world and potential links.
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("D2 assignment bundle belongs to a different world/DGP")
        expected_units = {unit.unit_id for unit in world.units}
        by_unit = {row.unit_id: row for row in self.assignments}
        if len(by_unit) != len(self.assignments) or set(by_unit) != expected_units:
            raise ContractError("D2 assignment must cover every world unit exactly once")
        truth_rows = {(row.unit_id, row.z): row for row in truth.potential_truth}
        for unit in world.units:
            row = by_unit[unit.unit_id]
            if row.history_ref != unit.d2_baseline.baseline_history_ref or row.assigned_z not in (0, 1):
                raise ContractError("D2 assignment unit/history/arm binding is invalid")
            p = row.probability_z1 if row.assigned_z == 1 else row.probability_z0
            if not (0.0 < p < 1.0):
                raise ContractError("D2 realized assignment probability must be positive")
            expected_truth = truth_rows[(unit.unit_id, row.assigned_z)]
            if (row.selected_history_id, row.selected_potential_id) != (
                expected_truth.history_id, expected_truth.potential_id
            ):
                raise ContractError("D2 assignment does not select its exact reserved potential history")
        payload = {
            "world": (self.world_id, self.world_version, self.dgp_id, self.dgp_version),
            "mechanism": (self.mechanism_id, self.mechanism_version, self.mechanism_sha256),
            "salt_sha256": self.randomization_salt_sha256,
            "q_x_sha256": self.q_x_sha256,
            "assignments": self.assignments,
        }
        if self.q_x_sha256 != digest(world.q_x) or self.result_sha256 != digest(payload):
            raise ContractError("D2 assignment provenance/result fingerprint is invalid")


def _uniform_from_commitment(*parts: str) -> tuple[float, str]:
    raw = hashlib.sha256("\x1f".join(parts).encode("utf-8")).digest()
    integer = int.from_bytes(raw[:8], "big")
    return integer / float(2**64), hashlib.sha256(raw).hexdigest()


def generate_d2_observed_assignments(
    world: SyntheticWorldBundle,
    truth: D2VContTruthBundle,
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
    config: D2ObservedAssignmentConfig,
) -> D2ObservedAssignmentBundle:
    """Randomize Z once per unit and select the corresponding D2 EventHistory.

    Truth is used only to resolve the selected history's opaque identity and
    provenance. No outcome value or interval adjudication enters assignment.
    """
    world.validate()
    config.validate(world)
    if (truth.world_id, truth.world_version, truth.dgp_id, truth.dgp_version) != (
        world.world_id, world.world_version, world.dgp_id, world.dgp_version
    ):
        raise ContractError("D2 truth bundle and assignment world differ")
    truth_by_key = {(row.unit_id, row.z): row for row in truth.potential_truth}
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(histories_by_unit_z) != expected or set(truth_by_key) != expected:
        raise ContractError("D2 assignment requires complete unit × Z potential-history coverage")
    probability_by_history = dict(config.probability_z1_by_history)
    assignments = []
    for unit in world.units:
        history_ref = unit.d2_baseline.baseline_history_ref
        p1 = probability_by_history[history_ref]
        uniform, uniform_sha = _uniform_from_commitment(
            config.randomization_salt, world.world_id, world.world_version,
            unit.unit_id, history_ref, config.mechanism_id, config.mechanism_version,
        )
        z = 1 if uniform < p1 else 0
        selected = truth_by_key[(unit.unit_id, z)]
        history = histories_by_unit_z[(unit.unit_id, z)]
        if (history.history_id, history.potential_id, history.unit_id) != (
            selected.history_id, selected.potential_id, unit.unit_id
        ):
            raise ContractError("selected D2 EventHistory does not match the reserved potential manifest")
        assignments.append(D2ObservedAssignment(
            unit.unit_id, history_ref, z, 1.0 - p1, p1,
            history.history_id, history.potential_id, uniform_sha,
        ))
    mechanism_sha = digest(config)
    payload = {
        "world": (world.world_id, world.world_version, world.dgp_id, world.dgp_version),
        "mechanism": (config.mechanism_id, config.mechanism_version, mechanism_sha),
        "salt_sha256": digest(config.randomization_salt),
        "q_x_sha256": digest(world.q_x),
        "assignments": tuple(assignments),
    }
    result = D2ObservedAssignmentBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        config.mechanism_id, config.mechanism_version, mechanism_sha,
        digest(config.randomization_salt), digest(world.q_x),
        tuple(assignments), digest(payload),
    )
    # Validate all assignment and selected-history bindings without exposing
    # reserved outcomes to any Analyzer-facing object.
    _validate_assignment_only(result, world, truth, histories_by_unit_z)
    return result


def _validate_assignment_only(
    bundle: D2ObservedAssignmentBundle,
    world: SyntheticWorldBundle,
    truth: D2VContTruthBundle,
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
) -> None:
    if (bundle.world_id, bundle.world_version, bundle.dgp_id, bundle.dgp_version) != (
        world.world_id, world.world_version, world.dgp_id, world.dgp_version
    ):
        raise ContractError("D2 assignment bundle belongs to a different world/DGP")
    if set(histories_by_unit_z) != {
        (unit.unit_id, z) for unit in world.units for z in (0, 1)
    }:
        raise ContractError("D2 assignment validation requires complete potential-history coverage")
    truth_rows = {(row.unit_id, row.z): row for row in truth.potential_truth}
    by_unit = {row.unit_id: row for row in bundle.assignments}
    if len(by_unit) != len(bundle.assignments) or set(by_unit) != {u.unit_id for u in world.units}:
        raise ContractError("D2 assignment must cover every world unit exactly once")
    for unit in world.units:
        row = by_unit[unit.unit_id]
        expected = truth_rows[(unit.unit_id, row.assigned_z)]
        history = histories_by_unit_z[(unit.unit_id, row.assigned_z)]
        if (row.history_ref, row.selected_history_id, row.selected_potential_id) != (
            unit.d2_baseline.baseline_history_ref, expected.history_id, expected.potential_id
        ) or history.history_id != row.selected_history_id:
            raise ContractError("D2 assignment does not bind to the exact realized potential EventHistory")
    payload = {
        "world": (bundle.world_id, bundle.world_version, bundle.dgp_id, bundle.dgp_version),
        "mechanism": (bundle.mechanism_id, bundle.mechanism_version, bundle.mechanism_sha256),
        "salt_sha256": bundle.randomization_salt_sha256,
        "q_x_sha256": bundle.q_x_sha256,
        "assignments": bundle.assignments,
    }
    if bundle.q_x_sha256 != digest(world.q_x) or bundle.result_sha256 != digest(payload):
        raise ContractError("D2 assignment provenance/result fingerprint is invalid")


def select_d2_realized_histories(
    assignments: D2ObservedAssignmentBundle,
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
) -> tuple[EventHistory, ...]:
    """Return only the assigned Z history per unit, preserving deterministic roster order."""
    selected = []
    for assignment in assignments.assignments:
        key = (assignment.unit_id, assignment.assigned_z)
        if key not in histories_by_unit_z:
            raise ContractError("assigned D2 potential EventHistory is missing")
        history = histories_by_unit_z[key]
        if (history.history_id, history.potential_id) != (
            assignment.selected_history_id, assignment.selected_potential_id
        ):
            raise ContractError("D2 selected history differs from assignment manifest")
        history.validate(require_complete=True)
        selected.append(history)
    return tuple(selected)
