"""Reusable synthetic components for C10-S.

Implements contracts without choosing unapproved confirmatory parameters:
D2 potential stages, reserved EventHistory, strict interval adjudication,
an evaluator-side theta_A oracle, and passive S3 projection. This is not a
second experiment runner and does not select q_X*, g_A policies, temporal
support/grid, S3 calibration, or downstream TGCV Value rules.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from decimal import Decimal
import hashlib
import json
import math
import random
from typing import Callable, Literal, Sequence

from c10s_focal_accessibility import (
    D2FocalAccessibilitySpecification,
    D2FocalPotentialTruth,
    adjudicate_d2_focal_potentials,
)

AdmissionBehavior = Literal["ADMIT", "NO_ADMISSION"]
ProfileValue = Literal["STANDARD", "READ_ONLY", "DISABLED"]
TriState = Literal[1, 0, "?"]


class ContractError(ValueError):
    """A synthetic input violates a governing C10-S contract."""


def _normalise(value):
    if isinstance(value, Decimal):
        return str(value)
    if hasattr(value, "__dataclass_fields__"):
        return _normalise(asdict(value))
    if isinstance(value, dict):
        return {str(k): _normalise(v) for k, v in sorted(value.items(), key=lambda x: str(x[0]))}
    if isinstance(value, (tuple, list)):
        return [_normalise(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ContractError("non-finite numeric value")
    return value


def digest(value) -> str:
    payload = json.dumps(_normalise(value), sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _probability(value: float, label: str) -> None:
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ContractError(f"{label} must be finite and in [0,1]")


def _distribution_total(values: Sequence[tuple[object, float]], label: str) -> None:
    if not values:
        raise ContractError(f"{label} must be nonempty")
    for _, probability in values:
        _probability(probability, f"{label} probability")
        if probability <= 0.0:
            raise ContractError(f"{label} must omit zero-mass entries")
    if abs(sum(p for _, p in values) - 1.0) > 1e-12:
        raise ContractError(f"{label} probabilities must sum to one")


# D2: explicit stage-by-stage potential generation; no inherited success.

@dataclass(frozen=True)
class D2MechanismConfig:
    dgp_id: str
    dgp_version: str
    policy_id_by_z: tuple[str, str]
    policy_version_by_z: tuple[str, str]
    policy_artifact_ref_by_z: tuple[str, str]
    actor_id_by_z: tuple[str, str]
    programmed_probability_by_z: tuple[float, float]
    attempt_if_programmed_by_z: tuple[float, float]
    background_attempt_by_z: tuple[float, float]
    receipt_given_attempt_by_z: tuple[float, float]
    install_given_receipt_by_z: tuple[float, float]
    joint_component_distribution: tuple[tuple[tuple[bool, bool, bool, bool], float], ...]
    mechanism_version: str

    def validate(self) -> None:
        if not all((self.dgp_id, self.dgp_version, self.mechanism_version)):
            raise ContractError("D2 DGP and mechanism identities/versions are required")
        if any(len(v) != 2 for v in (
            self.policy_id_by_z, self.policy_version_by_z,
            self.policy_artifact_ref_by_z, self.actor_id_by_z,
        )):
            raise ContractError("separate policy, artifact and actor identity is required for Z=0 and Z=1")
        if any(not x for x in (
            self.policy_id_by_z + self.policy_version_by_z
            + self.policy_artifact_ref_by_z + self.actor_id_by_z
        )):
            raise ContractError("policy, artifact and actor identities/versions cannot be blank")
        vectors = (
            self.programmed_probability_by_z, self.attempt_if_programmed_by_z,
            self.background_attempt_by_z, self.receipt_given_attempt_by_z,
            self.install_given_receipt_by_z,
        )
        if any(len(v) != 2 for v in vectors):
            raise ContractError("each D2 stage requires explicit Z=0 and Z=1 parameters")
        for vector in vectors:
            for p in vector:
                _probability(p, "D2 stage probability")
        _distribution_total(self.joint_component_distribution, "joint technical-component distribution")
        if any(len(outcome) != 4 or any(type(x) is not bool for x in outcome)
               for outcome, _ in self.joint_component_distribution):
            raise ContractError("joint technical outcomes must be four Boolean predicates")
        if len({outcome for outcome, _ in self.joint_component_distribution}) != len(
            self.joint_component_distribution
        ):
            raise ContractError("joint technical outcomes must be unique")


@dataclass(frozen=True)
class D2Baseline:
    unit_id: str
    baseline_history_ref: str
    focal_accessible_pre: bool
    c_auth_base: bool
    c_resource: bool
    c_capacity: bool
    c_info: bool
    c_domain: bool
    c_other: bool

    def validate(self) -> None:
        if not self.unit_id or not self.baseline_history_ref:
            raise ContractError("synthetic unit and baseline-history references are required")
        if any(type(value) is not bool for value in (
            self.focal_accessible_pre, self.c_auth_base, self.c_resource,
            self.c_capacity, self.c_info, self.c_domain, self.c_other,
        )):
            raise ContractError("D2 baseline predicates must be explicit Booleans")


@dataclass(frozen=True)
class D2PotentialStage:
    """D2 policy-stage fixture; a_f_post/d_f_opening are legacy Booleans.

    Current focal accessibility truth is carried separately by the optional
    typed D2FocalPotentialTruth on D2PotentialBundle. Never treat these legacy
    stage fields as validated A_f*/D_f* truth.
    """
    unit_id: str
    z: int
    policy_id: str
    policy_version: str
    policy_artifact_ref: str
    actor_id: str
    w_programmed: bool
    w_attempt: bool
    receipt: bool
    s_install: bool
    c_install: bool
    c_integrity: bool
    c_compat: bool
    c_oper: bool
    c_dep_star: bool
    a_f_post: bool
    d_f_opening: bool
    provenance_sha256: str


@dataclass(frozen=True)
class D2PotentialBundle:
    unit_id: str
    dgp_id: str
    dgp_version: str
    mechanism_version: str
    baseline_history_ref: str
    potentials_by_z: tuple[D2PotentialStage, D2PotentialStage]
    exogenous_draws_sha256: str
    focal_accessibility_truth: D2FocalPotentialTruth | None = None

    def validate(self) -> None:
        if tuple(x.z for x in self.potentials_by_z) != (0, 1):
            raise ContractError("D2 potential bundle must preserve separate Z=0 and Z=1 worlds")
        if any(x.unit_id != self.unit_id for x in self.potentials_by_z):
            raise ContractError("D2 potential unit identity mismatch")
        for p in self.potentials_by_z:
            if p.c_dep_star != all((p.c_install, p.c_integrity, p.c_compat, p.c_oper)):
                raise ContractError("C_dep* must be the conjunction of its four technical predicates")
            if p.a_f_post and not p.c_dep_star:
                raise ContractError("legacy D2 a_f_post fixture cannot be true when C_dep* is false")
        if self.focal_accessibility_truth is not None:
            self.focal_accessibility_truth.validate()
            if self.focal_accessibility_truth.unit_id != self.unit_id:
                raise ContractError("typed D2 focal truth unit differs from D2 potential bundle")
            post_truth = dict(self.focal_accessibility_truth.post_by_z)
            for stage in self.potentials_by_z:
                result = post_truth[stage.z]
                route_components = dict(result.route_component_truth)
                if self.focal_accessibility_truth.focal_route_id not in route_components:
                    raise ContractError("typed D2 focal result omits its declared focal route components")
                component_truth = dict(route_components[self.focal_accessibility_truth.focal_route_id])
                expected_components = {
                    "C_install": "1" if stage.c_install else "0",
                    "C_integrity": "1" if stage.c_integrity else "0",
                    "C_compat": "1" if stage.c_compat else "0",
                    "C_oper": "1" if stage.c_oper else "0",
                }
                if component_truth != expected_components:
                    raise ContractError(
                        f"typed focal DEP components do not reproduce D2 Z={stage.z} technical component truth"
                    )
                expected_dep = "1" if stage.c_dep_star else "0"
                if result.dep_truth != expected_dep:
                    raise ContractError(
                        f"typed focal DEP truth does not reproduce D2 Z={stage.z} C_dep*"
                    )


def _draw_joint_component(distribution, u: float):
    cumulative = 0.0
    for outcome, probability in distribution:
        cumulative += probability
        if u < cumulative:
            return outcome
    return distribution[-1][0]


def generate_d2_potentials(
    baseline: D2Baseline, config: D2MechanismConfig, *, exogenous_seed: int,
) -> D2PotentialBundle:
    """Generate both Z potentials with common exogenous draws, not observed data.

    All stage probabilities and the joint technical distribution are mandatory
    inputs. DEC-C10-067 candidate values are not silently assumed.
    """
    baseline.validate()
    config.validate()
    rng = random.Random(exogenous_seed)
    u_programmed, u_attempt, u_receipt, u_install, u_components = (
        rng.random() for _ in range(5)
    )
    draws_hash = digest({
        "seed_commitment": digest({"seed": exogenous_seed}),
        "draws": (u_programmed, u_attempt, u_receipt, u_install, u_components),
    })
    potentials = []
    for z in (0, 1):
        programmed = u_programmed < config.programmed_probability_by_z[z]
        p_attempt = (
            config.attempt_if_programmed_by_z[z] if programmed
            else config.background_attempt_by_z[z]
        )
        attempted = u_attempt < p_attempt
        received = attempted and (u_receipt < config.receipt_given_attempt_by_z[z])
        installed = received and (u_install < config.install_given_receipt_by_z[z])
        components = (
            _draw_joint_component(config.joint_component_distribution, u_components)
            if installed else (False, False, False, False)
        )
        c_dep = all(components)
        a_f_post = all((
            c_dep, baseline.c_auth_base, baseline.c_resource,
            baseline.c_capacity, baseline.c_info, baseline.c_domain,
            baseline.c_other,
        ))
        provenance = digest({
            "dgp_id": config.dgp_id, "dgp_version": config.dgp_version,
            "mechanism_version": config.mechanism_version,
            "unit_id": baseline.unit_id, "baseline_history_ref": baseline.baseline_history_ref,
            "z": z, "policy_id": config.policy_id_by_z[z],
            "policy_version": config.policy_version_by_z[z],
            "policy_artifact_ref": config.policy_artifact_ref_by_z[z],
            "actor_id": config.actor_id_by_z[z],
            "shared_exogenous_draws_sha256": draws_hash,
        })
        potentials.append(D2PotentialStage(
            baseline.unit_id, z, config.policy_id_by_z[z],
            config.policy_version_by_z[z], config.policy_artifact_ref_by_z[z],
            config.actor_id_by_z[z], programmed, attempted,
            received, installed, components[0], components[1],
            components[2], components[3], c_dep, a_f_post,
            (not baseline.focal_accessible_pre and a_f_post), provenance,
        ))
    result = D2PotentialBundle(
        baseline.unit_id, config.dgp_id, config.dgp_version,
        config.mechanism_version, baseline.baseline_history_ref,
        (potentials[0], potentials[1]), draws_hash,
    )
    result.validate()
    return result


# EventHistory: generated functional truth, never PROCESS_EVENT or S3.

@dataclass(frozen=True)
class FunctionalState:
    enabled: bool
    admission_behavior: AdmissionBehavior
    # PROFILE and its identity/version are declarative configuration, not exposure.
    profile: ProfileValue = "STANDARD"
    profile_config_id: str = "B1-PROFILE"
    profile_config_version: str = "001"

    def validate(self) -> None:
        if type(self.enabled) is not bool or self.admission_behavior not in ("ADMIT", "NO_ADMISSION"):
            raise ContractError("unsupported ENABLED/admission state")
        if self.profile not in ("STANDARD", "READ_ONLY", "DISABLED"):
            raise ContractError("unsupported declared PROFILE value")
        if not self.profile_config_id or not self.profile_config_version:
            raise ContractError("declared PROFILE identity/version is required")

    @property
    def declarative_valid(self) -> bool:
        # RUL-SVC-ENABLE-PROFILE-01 is an implication, not an uptime rule.
        return not self.enabled or self.profile in ("STANDARD", "READ_ONLY")

    @property
    def compliant(self) -> bool:
        # Gate 154 / R208: A_B1 adjudicates only admission behaviour required by ENABLED.
        expected = "ADMIT" if self.enabled else "NO_ADMISSION"
        return self.admission_behavior == expected


@dataclass(frozen=True)
class FunctionalTransition:
    transition_id: str
    event_time: Decimal
    state_before: FunctionalState
    state_after: FunctionalState
    causal_family: str
    provenance_ref: str
    suborder: int | None = None


@dataclass(frozen=True)
class EventHistory:
    history_id: str
    history_version: str
    run_id: str
    world_id: str
    world_version: str
    dgp_version: str
    unit_id: str
    potential_id: str
    adjudication_rules_version: str
    support_start: Decimal
    support_end: Decimal
    initial_post_z_state: FunctionalState
    transitions: tuple[FunctionalTransition, ...]
    # Independent Generator-side manifest of all transition IDs in this
    # potential history; compared exactly with the materialized history.
    expected_transition_ids: tuple[str, ...]
    scope_declared_complete: bool
    generation_complete: bool
    representation_complete: bool
    profile_config_id: str = "B1-PROFILE"
    profile_config_version: str = "001"

    def validate(self, *, require_complete: bool = True) -> None:
        required = (
            self.history_id, self.history_version, self.run_id, self.world_id,
            self.world_version, self.dgp_version, self.unit_id, self.potential_id,
            self.adjudication_rules_version, self.profile_config_id,
            self.profile_config_version,
        )
        if any(not x for x in required):
            raise ContractError("EventHistory scope identities and versions are mandatory")
        if not isinstance(self.support_start, Decimal) or not isinstance(self.support_end, Decimal):
            raise ContractError("EventHistory uses exact Decimal event-time coordinates")
        if self.support_start >= self.support_end:
            raise ContractError("EventHistory support must have positive duration")
        self.initial_post_z_state.validate()
        if (self.initial_post_z_state.profile_config_id != self.profile_config_id
                or self.initial_post_z_state.profile_config_version != self.profile_config_version):
            raise ContractError("EventHistory initial PROFILE identity/version must match its declared baseline")
        ids = [event.transition_id for event in self.transitions]
        if any(not x for x in ids) or len(ids) != len(set(ids)):
            raise ContractError("truth transition IDs must be unique within EventHistory")
        if len(self.expected_transition_ids) != len(set(self.expected_transition_ids)):
            raise ContractError("Generator transition manifest IDs must be unique")
        if tuple(ids) != self.expected_transition_ids:
            raise ContractError("EventHistory does not match the Generator-side transition manifest")
        ordered = tuple(sorted(
            self.transitions,
            key=lambda e: (e.event_time, -1 if e.suborder is None else e.suborder),
        ))
        if ordered != self.transitions:
            raise ContractError("EventHistory transitions must be ordered by event_time/suborder")
        current = self.initial_post_z_state
        by_time: dict[Decimal, list[FunctionalTransition]] = {}
        for event in self.transitions:
            if not isinstance(event.event_time, Decimal):
                raise ContractError("truth event_time must use exact Decimal coordinates")
            if event.event_time < self.support_start or event.event_time > self.support_end:
                raise ContractError("truth transition falls outside declared support")
            if not event.causal_family or not event.provenance_ref:
                raise ContractError("truth transition causal family and reserved provenance are required")
            event.state_before.validate()
            event.state_after.validate()
            if event.state_before != current:
                raise ContractError("transition state_before does not continue the preceding functional state")
            if event.state_before == event.state_after:
                raise ContractError("functionally neutral process occurrences are not EventHistory transitions")
            if (event.state_before.profile != event.state_after.profile
                    and (event.state_before.profile_config_id, event.state_before.profile_config_version)
                    == (event.state_after.profile_config_id, event.state_after.profile_config_version)):
                raise ContractError("a PROFILE value change requires an explicit configuration identity/version change")
            current = event.state_after
            by_time.setdefault(event.event_time, []).append(event)
        for same_time in by_time.values():
            if len(same_time) == 1:
                if same_time[0].suborder is not None:
                    raise ContractError("suborder is only used for genuine same-time intermediate states")
            else:
                orders = [event.suborder for event in same_time]
                if any(x is None for x in orders) or len(set(orders)) != len(orders):
                    raise ContractError("same-time non-atomic transitions require explicit unique suborder")
                if sorted(orders) != list(range(len(orders))):
                    raise ContractError("same-time suborder must be contiguous from zero")
        if require_complete and not all((
            self.scope_declared_complete, self.generation_complete,
            self.representation_complete,
        )):
            raise ContractError("incomplete EventHistory is a harness defect, not functional UNKNOWN")

    @property
    def content_sha256(self) -> str:
        self.validate(require_complete=False)
        return digest(self)


@dataclass(frozen=True)
class FunctionalStateChange:
    """One DGP-authored functional state change; not a PROCESS_EVENT."""

    event_time: Decimal
    state_after: FunctionalState
    causal_family: str
    provenance_ref: str
    suborder: int | None = None


@dataclass(frozen=True)
class EventHistoryGenerationSpec:
    """Complete, explicit functional path specification for one potential."""

    history_id: str
    history_version: str
    run_id: str
    world_id: str
    world_version: str
    dgp_version: str
    unit_id: str
    potential_id: str
    adjudication_rules_version: str
    support_start: Decimal
    support_end: Decimal
    initial_post_z_state: FunctionalState
    changes: tuple[FunctionalStateChange, ...]
    profile_config_id: str = "B1-PROFILE"
    profile_config_version: str = "001"

    def validate(self) -> None:
        if not all((
            self.history_id, self.history_version, self.run_id, self.world_id,
            self.world_version, self.dgp_version, self.unit_id, self.potential_id,
            self.adjudication_rules_version, self.profile_config_id,
            self.profile_config_version,
        )):
            raise ContractError("EventHistory generation spec requires complete identity/version")
        if (not isinstance(self.support_start, Decimal)
                or not isinstance(self.support_end, Decimal)
                or self.support_start >= self.support_end):
            raise ContractError("EventHistory generation spec requires positive Decimal support")
        self.initial_post_z_state.validate()
        if (self.initial_post_z_state.profile_config_id != self.profile_config_id
                or self.initial_post_z_state.profile_config_version != self.profile_config_version):
            raise ContractError("initial PROFILE identity/version differs from generation spec")
        ordered = tuple(sorted(
            self.changes,
            key=lambda row: (row.event_time, -1 if row.suborder is None else row.suborder),
        ))
        if ordered != self.changes:
            raise ContractError("functional state changes must be ordered by event_time/suborder")
        if any(
            not isinstance(row.event_time, Decimal)
            or row.event_time < self.support_start or row.event_time > self.support_end
            or not row.causal_family or not row.provenance_ref
            for row in self.changes
        ):
            raise ContractError("each functional change needs in-support time and causal provenance")


def generate_event_history(spec: EventHistoryGenerationSpec) -> EventHistory:
    """Materialize one complete EventHistory from explicit DGP functional states.

    The function does not infer admission from D2 accessibility, infer state
    changes from PROCESS_EVENT, or derive temporal states from S3. The DGP must
    supply the functional state path and causal provenance explicitly.
    """
    spec.validate()
    current = spec.initial_post_z_state
    transitions = []
    for index, change in enumerate(spec.changes):
        change.state_after.validate()
        if current == change.state_after:
            raise ContractError("neutral state changes are not functional EventHistory transitions")
        if (current.profile != change.state_after.profile
                and (current.profile_config_id, current.profile_config_version)
                == (change.state_after.profile_config_id, change.state_after.profile_config_version)):
            raise ContractError("PROFILE value change requires a new configuration identity/version")
        transition_id = digest({
            "history_id": spec.history_id, "history_version": spec.history_version,
            "index": index, "event_time": change.event_time,
            "state_before": current, "state_after": change.state_after,
            "causal_family": change.causal_family,
            "provenance_ref": change.provenance_ref, "suborder": change.suborder,
        })
        transitions.append(FunctionalTransition(
            transition_id, change.event_time, current, change.state_after,
            change.causal_family, change.provenance_ref, change.suborder,
        ))
        current = change.state_after
    transition_tuple = tuple(transitions)
    history = EventHistory(
        spec.history_id, spec.history_version, spec.run_id, spec.world_id,
        spec.world_version, spec.dgp_version, spec.unit_id, spec.potential_id,
        spec.adjudication_rules_version, spec.support_start, spec.support_end,
        spec.initial_post_z_state, transition_tuple,
        tuple(row.transition_id for row in transition_tuple),
        True, True, True, spec.profile_config_id, spec.profile_config_version,
    )
    history.validate(require_complete=True)
    return history


@dataclass(frozen=True)
class IntervalGrid:
    boundaries: tuple[Decimal, ...]
    grid_id: str
    grid_version: str

    def validate(self) -> None:
        if not self.grid_id or not self.grid_version or len(self.boundaries) < 2:
            raise ContractError("explicit interval-grid identity/version and boundaries required")
        if any(not isinstance(value, Decimal) for value in self.boundaries):
            raise ContractError("interval boundaries must use exact Decimal coordinates")
        if any(a >= b for a, b in zip(self.boundaries, self.boundaries[1:])):
            raise ContractError("interval boundaries must be strictly increasing")
        widths = [b - a for a, b in zip(self.boundaries, self.boundaries[1:])]
        if any(width != widths[0] for width in widths):
            raise ContractError("DEC-C10-100 requires equal-duration intervals")


@dataclass(frozen=True)
class IntervalAdjudication:
    history_id: str
    history_version: str
    grid_id: str
    grid_version: str
    rules_version: str
    interval_truth: tuple[TriState, ...]
    v_cont_truth: float
    v_cont_lower: float
    v_cont_upper: float
    history_sha256: str


def adjudicate_intervals(history: EventHistory, grid: IntervalGrid) -> IntervalAdjudication:
    """Apply strict continuity and DEC-C10-104 half-open/final-closed boundaries."""
    history.validate(require_complete=True)
    grid.validate()
    if grid.boundaries[0] != history.support_start or grid.boundaries[-1] != history.support_end:
        raise ContractError("grid must cover the exact EventHistory support")
    truth: list[TriState] = []
    events = list(history.transitions)
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
        events_at_left = [event for event in interval_events if event.event_time == left]
        # At an internal boundary, the preceding state belongs only to the
        # preceding half-open interval. At t0, the accepted post-Z initial
        # state is part of the window before same-anchor transitions.
        compliant = current.compliant if left == history.support_start or not events_at_left else True
        for event in interval_events:
            current = event.state_after
            compliant = compliant and current.compliant
        truth.append(1 if compliant else 0)
    value = sum(truth) / len(truth)
    return IntervalAdjudication(
        history.history_id, history.history_version, grid.grid_id,
        grid.grid_version, history.adjudication_rules_version,
        tuple(truth), value, value, value, history.content_sha256,
    )


# q_X*, g_A0/g_A1 and r_common: generic evaluator-side truth engine.

Vector4 = tuple[object, object, object, object]


@dataclass(frozen=True)
class QXHistoryMass:
    history_ref: str
    x_ref: str
    h0_ref: str
    c_c_ref: str
    mass: float




# Structural transformation space and three-valued reachability.
# This engine consumes explicit structural predicates; it does not infer them
# from D2 stages, assignment, selection, execution, Outcome or Value.

ReachState = Literal[1, 0, "?"]


def _reach_state(value, label: str) -> None:
    if value not in (1, 0, "?") or isinstance(value, bool):
        raise ContractError(f"{label} must be one of 1, 0, ?")


def _kleene_and(values: Sequence[ReachState]) -> ReachState:
    if not values:
        return 1
    if any(value == 0 for value in values):
        return 0
    if all(value == 1 for value in values):
        return 1
    return "?"


def _kleene_or(values: Sequence[ReachState], *, exhaustive: bool) -> ReachState:
    if any(value == 1 for value in values):
        return 1
    if exhaustive and all(value == 0 for value in values):
        return 0
    return "?"


@dataclass(frozen=True)
class StructuralTransformation:
    transformation_id: str
    semantic_version: str
    snapshot_id: str
    accessible_state: ReachState

    def validate(self) -> None:
        if not all((self.transformation_id, self.semantic_version, self.snapshot_id)):
            raise ContractError("transformation identity, semantic version and snapshot are required")
        _reach_state(self.accessible_state, "T_acc state")


@dataclass(frozen=True)
class StructuralSnapshot:
    snapshot_id: str
    snapshot_version: str
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    unit_id: str
    potential_z: int | None
    boundary_id: str
    context_id: str
    horizon: float
    transformations: tuple[StructuralTransformation, ...]
    universe_exhaustive: bool
    relations_exhaustive: bool
    conditions_exhaustive: bool
    resources_exhaustive: bool
    catalog_version: str
    potential_axis: Literal["Z", "G_A"] = "Z"
    potential_label: str | None = None

    def validate(self) -> None:
        if not all((self.snapshot_id, self.snapshot_version, self.world_id,
                    self.world_version, self.dgp_id, self.dgp_version, self.unit_id,
                    self.boundary_id, self.context_id, self.catalog_version)):
            raise ContractError("structural snapshot identity, boundary, context and catalog version are required")
        if self.potential_axis == "Z":
            if self.potential_z not in (0, 1) or self.potential_label is not None:
                raise ContractError("Z structural snapshot must identify Z=0/1 and no factorial label")
        elif self.potential_axis == "G_A":
            if self.potential_z is not None or not self.potential_label:
                raise ContractError("g_A structural snapshot must identify its vector potential without a Z value")
        else:
            raise ContractError("structural snapshot potential axis must be Z or G_A")
        if not math.isfinite(self.horizon) or self.horizon <= 0:
            raise ContractError("structural horizon must be positive and finite")
        ids = [item.transformation_id for item in self.transformations]
        if len(ids) != len(set(ids)):
            raise ContractError("transformation IDs must be unique within a snapshot")
        for item in self.transformations:
            item.validate()
            if item.snapshot_id != self.snapshot_id:
                raise ContractError("transformation belongs to a different structural snapshot")
        if not self.transformations:
            raise ContractError("structural snapshot must declare its finite transformation catalog")

    @property
    def catalog_is_exhaustive(self) -> bool:
        return all((self.universe_exhaustive, self.relations_exhaustive,
                    self.conditions_exhaustive, self.resources_exhaustive))


@dataclass(frozen=True)
class StructuralRouteStep:
    transformation_id: str
    state_before: str
    state_after: str
    applicability_state: ReachState
    predicate_states: tuple[tuple[str, ReachState], ...] = ()
    duration: float = 0.0

    def validate(self) -> None:
        if not self.transformation_id or not self.state_before or not self.state_after:
            raise ContractError("route step requires transformation and explicit input/output states")
        _reach_state(self.applicability_state, "App_f state")
        if not math.isfinite(self.duration) or self.duration < 0:
            raise ContractError("route-step duration must be finite and nonnegative")
        names = [name for name, _ in self.predicate_states]
        if any(not name for name in names) or len(names) != len(set(names)):
            raise ContractError("route predicate names must be nonempty and unique per step")
        for name, value in self.predicate_states:
            _reach_state(value, f"route predicate {name}")


@dataclass(frozen=True)
class StructuralRoute:
    route_id: str
    target_state: str
    steps: tuple[StructuralRouteStep, ...]
    relation_states: tuple[ReachState, ...]
    temporal_feasibility_state: ReachState
    route_scope: str

    def validate(self) -> None:
        if not self.route_id or not self.target_state or not self.route_scope or not self.steps:
            raise ContractError("route identity, target, scope and at least one step are required")
        if len(self.relation_states) != len(self.steps) - 1:
            raise ContractError("one explicit relation state is required between adjacent route steps")
        for value in self.relation_states:
            _reach_state(value, "REL_f state")
        _reach_state(self.temporal_feasibility_state, "temporal feasibility state")
        for step in self.steps:
            step.validate()
        for left, right in zip(self.steps, self.steps[1:]):
            if left.state_after != right.state_before:
                raise ContractError("route state transition is discontinuous")


@dataclass(frozen=True)
class StructuralRouteEvaluation:
    route_id: str
    target_state: str
    route_state: ReachState
    first_blocking_predicate: str | None
    unknown_predicates: tuple[str, ...]
    total_duration: float


@dataclass(frozen=True)
class ReachabilityResult:
    snapshot_id: str
    snapshot_version: str
    target_states: tuple[tuple[str, ReachState], ...]
    route_evaluations: tuple[StructuralRouteEvaluation, ...]
    enumeration_complete: bool
    catalog_exhaustive: bool
    search_truncated: bool
    result_sha256: str

    def validate(self) -> None:
        targets = [target for target, _ in self.target_states]
        if len(targets) != len(set(targets)):
            raise ContractError("reachability result contains duplicate target states")
        for _, state in self.target_states:
            _reach_state(state, "Reach_H state")
        route_ids = [row.route_id for row in self.route_evaluations]
        if len(route_ids) != len(set(route_ids)):
            raise ContractError("reachability result contains duplicate route IDs")
        if not self.result_sha256:
            raise ContractError("reachability result fingerprint is required")


class StructuralReachabilityEngine:
    """Evaluate explicit T_acc, App, relation and route predicates separately.

    A confirmed route establishes Reach=1. Reach=0 requires exhaustive catalog,
    relations, conditions, resources and completed enumeration. Truncation or
    unknown predicates never become structural absence.
    """
    version = "c10s-structural-reachability-0.1"

    def evaluate(
        self,
        snapshot: StructuralSnapshot,
        routes: Sequence[StructuralRoute],
        *,
        enumeration_complete: bool,
        search_truncated: bool = False,
        target_states: Sequence[str] = (),
    ) -> ReachabilityResult:
        snapshot.validate()
        if search_truncated and enumeration_complete:
            raise ContractError("a truncated search cannot be declared enumeration-complete")
        transformations = {item.transformation_id: item for item in snapshot.transformations}
        route_ids = [route.route_id for route in routes]
        if len(route_ids) != len(set(route_ids)):
            raise ContractError("route IDs must be unique")
        evaluations = []
        for route in routes:
            route.validate()
            states: list[ReachState] = []
            names: list[str] = []
            first_block = None
            unknown = []
            total_duration = 0.0
            for index, step in enumerate(route.steps):
                transform = transformations.get(step.transformation_id)
                if transform is None:
                    raise ContractError("route references a transformation outside the declared snapshot catalog")
                predicates = [(f"T_acc:{step.transformation_id}", transform.accessible_state),
                              (f"App:{step.transformation_id}", step.applicability_state)]
                predicates.extend((f"{name}:{step.transformation_id}", value)
                                  for name, value in step.predicate_states)
                for name, value in predicates:
                    states.append(value)
                    names.append(name)
                    if value == "?" and name not in unknown:
                        unknown.append(name)
                    if value == 0 and first_block is None:
                        first_block = name
                total_duration += step.duration
                if index < len(route.relation_states):
                    name = f"REL:{route.route_id}:{index}"
                    value = route.relation_states[index]
                    states.append(value)
                    names.append(name)
                    if value == "?" and name not in unknown:
                        unknown.append(name)
                    if value == 0 and first_block is None:
                        first_block = name
            temporal_state = route.temporal_feasibility_state
            if total_duration > snapshot.horizon:
                temporal_state = 0
            states.append(temporal_state)
            names.append(f"TEMPORAL:{route.route_id}")
            if temporal_state == "?" and names[-1] not in unknown:
                unknown.append(names[-1])
            if temporal_state == 0 and first_block is None:
                first_block = names[-1]
            route_state = _kleene_and(states)
            evaluations.append(StructuralRouteEvaluation(
                route.route_id, route.target_state, route_state,
                first_block, tuple(unknown), total_duration,
            ))
        declared_targets = tuple(target_states)
        if any(not target for target in declared_targets) or len(declared_targets) != len(set(declared_targets)):
            raise ContractError("declared reachability target states must be nonempty and unique")
        target_results = []
        targets = sorted(set(declared_targets) | {route.target_state for route in routes})
        if any(not target for target in targets):
            raise ContractError("declared reachability target states must be nonempty")
        # A target absent from enumerated routes can be refuted only when both
        # the declared universe and the route enumeration are exhaustive.
        exhaustive = snapshot.catalog_is_exhaustive and enumeration_complete and not search_truncated
        for target in targets:
            target_routes = [row.route_state for row in evaluations if row.target_state == target]
            target_results.append((target, _kleene_or(target_routes, exhaustive=exhaustive)))
        payload = {
            "snapshot_id": snapshot.snapshot_id,
            "snapshot_version": snapshot.snapshot_version,
            "target_states": tuple(target_results),
            "route_evaluations": tuple(evaluations),
            "enumeration_complete": enumeration_complete,
            "catalog_exhaustive": snapshot.catalog_is_exhaustive,
            "search_truncated": search_truncated,
        }
        result = ReachabilityResult(
            snapshot.snapshot_id, snapshot.snapshot_version, tuple(target_results),
            tuple(evaluations), enumeration_complete, snapshot.catalog_is_exhaustive,
            search_truncated, digest(payload),
        )
        result.validate()
        return result



@dataclass(frozen=True)
class UnitPotentialReachability:
    unit_id: str
    z: int
    snapshot_id: str
    result: ReachabilityResult


@dataclass(frozen=True)
class SyntheticWorldReachabilityBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    unit_potential_results: tuple[UnitPotentialReachability, ...]
    result_sha256: str

    def validate(self, world: "SyntheticWorldBundle") -> None:
        world.validate()
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("reachability bundle identity differs from its synthetic world")
        expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
        actual = {(row.unit_id, row.z) for row in self.unit_potential_results}
        if actual != expected or len(actual) != len(self.unit_potential_results):
            raise ContractError("reachability bundle must contain exactly both Z potentials per world unit")
        for row in self.unit_potential_results:
            row.result.validate()
            if row.result.snapshot_id != row.snapshot_id:
                raise ContractError("reachability result and snapshot identities differ")
        if not self.result_sha256:
            raise ContractError("world reachability fingerprint is required")


def evaluate_synthetic_world_reachability(
    world: "SyntheticWorldBundle",
    snapshots_by_unit_z: dict[tuple[str, int], StructuralSnapshot],
    routes_by_unit_z: dict[tuple[str, int], Sequence[StructuralRoute]],
    target_states_by_unit_z: dict[tuple[str, int], Sequence[str]],
    enumeration_complete_by_unit_z: dict[tuple[str, int], bool],
    search_truncated_by_unit_z: dict[tuple[str, int], bool],
) -> SyntheticWorldReachabilityBundle:
    """Attach explicit structural snapshots/reachability to every D2 potential.

    No D2 field is translated into T_acc, App, REL or Reach. The caller must
    provide each structural world and its route predicates explicitly.
    """
    world.validate()
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    for label, mapping in (
        ("structural snapshots", snapshots_by_unit_z),
        ("route catalogs", routes_by_unit_z),
        ("target-state universes", target_states_by_unit_z),
        ("enumeration completeness", enumeration_complete_by_unit_z),
        ("search truncation", search_truncated_by_unit_z),
    ):
        if set(mapping) != expected:
            raise ContractError(f"{label} must cover every unit × Z potential exactly")
    engine = StructuralReachabilityEngine()
    rows = []
    for key in sorted(expected):
        snapshot = snapshots_by_unit_z[key]
        unit_id, z = key
        if (snapshot.world_id, snapshot.world_version, snapshot.dgp_id,
                snapshot.dgp_version, snapshot.unit_id, snapshot.potential_z) != (
            world.world_id, world.world_version, world.dgp_id,
            world.dgp_version, unit_id, z
        ):
            raise ContractError("structural snapshot does not bind to the exact world/unit/potential")
        result = engine.evaluate(
            snapshot, routes_by_unit_z[key],
            enumeration_complete=enumeration_complete_by_unit_z[key],
            search_truncated=search_truncated_by_unit_z[key],
            target_states=target_states_by_unit_z[key],
        )
        rows.append(UnitPotentialReachability(unit_id, z, snapshot.snapshot_id, result))
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "unit_potential_results": tuple(rows),
    }
    bundle = SyntheticWorldReachabilityBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        tuple(rows), digest(payload),
    )
    bundle.validate(world)
    return bundle



# Full structural snapshot/delta contract: U/R/C/X truth is kept apart from E_T.
StructuralComponent = Literal["U", "R", "C", "X"]
SnapshotTimepoint = Literal["BASELINE", "POST"]


@dataclass(frozen=True)
class StructuralAtom:
    component: StructuralComponent
    canonical_id: str
    semantic_type: str
    semantic_version: str
    state: ReachState
    attributes: tuple[tuple[str, str], ...]

    def validate(self) -> None:
        if self.component not in ("U", "R", "C", "X"):
            raise ContractError("structural atom must belong to U/R/C/X")
        if not all((self.canonical_id, self.semantic_type, self.semantic_version)):
            raise ContractError("structural atom identity/type/version are mandatory")
        _reach_state(self.state, f"{self.component} structural state")
        keys = [key for key, _ in self.attributes]
        if any(not key for key in keys) or len(keys) != len(set(keys)):
            raise ContractError("structural atom attribute keys must be nonempty and unique")
        forbidden = {"outcome", "value", "selection", "execution"}
        if any(key.strip().casefold() in forbidden for key in keys):
            raise ContractError("Outcome, Value, selection and execution are downstream, not S_T* fields")


@dataclass(frozen=True)
class StructuralIdentityMatch:
    baseline_id: str
    post_id: str
    match_state: ReachState

    def validate(self) -> None:
        if not self.baseline_id or not self.post_id:
            raise ContractError("identity correspondence requires both baseline and post IDs")
        if self.baseline_id == self.post_id:
            raise ContractError("explicit correspondence is only for different canonical IDs")
        if self.match_state not in (1, "?"):
            raise ContractError("identity correspondence must be confirmed (1) or unresolved (?)")


@dataclass(frozen=True)
class TransformationalStateSnapshot:
    snapshot_id: str
    snapshot_version: str
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    unit_id: str
    potential_z: int | None
    timepoint: SnapshotTimepoint
    boundary_id: str
    context_id: str
    catalog_version: str
    atoms: tuple[StructuralAtom, ...]
    component_complete: tuple[tuple[StructuralComponent, bool], ...]
    potential_axis: Literal["Z", "G_A"] = "Z"
    potential_label: str | None = None

    def validate(self) -> None:
        if not all((self.snapshot_id, self.snapshot_version, self.world_id,
                    self.world_version, self.dgp_id, self.dgp_version, self.unit_id,
                    self.boundary_id, self.context_id, self.catalog_version)):
            raise ContractError("transformational snapshot identity and scope are mandatory")
        if self.potential_axis == "Z":
            if self.potential_z not in (0, 1) or self.potential_label is not None:
                raise ContractError("Z-axis snapshot must identify Z=0/1 and no factorial potential label")
        elif self.potential_axis == "G_A":
            if self.potential_z is not None or not self.potential_label:
                raise ContractError("g_A-axis snapshot must use a vector-specific label and no Z value")
        else:
            raise ContractError("snapshot potential axis must be Z or G_A")
        if self.timepoint not in ("BASELINE", "POST"):
            raise ContractError("snapshot must identify BASELINE/POST timepoint")
        atom_ids = [atom.canonical_id for atom in self.atoms]
        if len(atom_ids) != len(set(atom_ids)):
            raise ContractError("canonical structural atom IDs must be globally unique within a snapshot")
        for atom in self.atoms:
            atom.validate()
        complete = dict(self.component_complete)
        if set(complete) != {"U", "R", "C", "X"} or any(type(v) is not bool for v in complete.values()):
            raise ContractError("component completeness must explicitly cover U/R/C/X")
        if len(self.component_complete) != 4:
            raise ContractError("component completeness declarations must not be duplicated")


@dataclass(frozen=True)
class StructuralDeltaEntry:
    component: StructuralComponent
    change_kind: Literal["ADDED", "REMOVED", "MODIFIED", "UNCHANGED", "UNKNOWN"]
    change_state: ReachState
    baseline_id: str | None
    post_id: str | None
    baseline_sha256: str | None
    post_sha256: str | None
    semantic_type: str | None


@dataclass(frozen=True)
class EvidenceStateSnapshot:
    evidence_id: str
    source_refs: tuple[str, ...]
    coverage_state: str
    validity_state: str
    provenance_sha256: str
    evidence_version: str
    adjudication_version: str

    def validate(self) -> None:
        if not all((self.evidence_id, self.coverage_state, self.validity_state,
                    self.provenance_sha256, self.evidence_version, self.adjudication_version)):
            raise ContractError("E_T evidence identity, coverage, validity, provenance and versions are required")
        if len(self.source_refs) != len(set(self.source_refs)):
            raise ContractError("E_T source references must be unique")


@dataclass(frozen=True)
class EvidenceDelta:
    changed: bool
    baseline_sha256: str
    post_sha256: str


@dataclass(frozen=True)
class TransformationalDelta:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    unit_id: str
    potential_z: int | None
    baseline_snapshot_id: str
    post_snapshot_id: str
    entries: tuple[StructuralDeltaEntry, ...]
    delta_u: tuple[StructuralDeltaEntry, ...]
    delta_r: tuple[StructuralDeltaEntry, ...]
    delta_c: tuple[StructuralDeltaEntry, ...]
    delta_x: tuple[StructuralDeltaEntry, ...]
    component_completeness: tuple[tuple[StructuralComponent, bool], ...]
    delta_state: ReachState
    evidence_delta: EvidenceDelta
    result_sha256: str
    potential_axis: Literal["Z", "G_A"] = "Z"
    potential_label: str | None = None

    def validate(self) -> None:
        if not self.result_sha256:
            raise ContractError("transformational delta fingerprint is required")
        if tuple(self.delta_u) != tuple(x for x in self.entries if x.component == "U"):
            raise ContractError("ΔU* projection differs from canonical delta entries")
        if tuple(self.delta_r) != tuple(x for x in self.entries if x.component == "R"):
            raise ContractError("ΔR* projection differs from canonical delta entries")
        if tuple(self.delta_c) != tuple(x for x in self.entries if x.component == "C"):
            raise ContractError("ΔC* projection differs from canonical delta entries")
        if tuple(self.delta_x) != tuple(x for x in self.entries if x.component == "X"):
            raise ContractError("ΔX* projection differs from canonical delta entries")
        completeness = dict(self.component_completeness)
        if set(completeness) != {"U", "R", "C", "X"} or len(self.component_completeness) != 4:
            raise ContractError("ΔT_acc* must retain completeness for all U/R/C/X components")
        _reach_state(self.delta_state, "ΔT_acc* state")


def _atom_fingerprint(atom: StructuralAtom | None) -> str | None:
    return None if atom is None else digest(atom)


def _evidence_delta(before: EvidenceStateSnapshot, after: EvidenceStateSnapshot) -> EvidenceDelta:
    before.validate()
    after.validate()
    before_hash, after_hash = digest(before), digest(after)
    return EvidenceDelta(before_hash != after_hash, before_hash, after_hash)


class TransformationalDeltaEngine:
    """Diff comparable structural truth snapshots; never folds E_T into ΔT_acc*."""
    version = "c10s-transformational-delta-0.1"

    def evaluate(
        self,
        baseline: TransformationalStateSnapshot,
        post: TransformationalStateSnapshot,
        *,
        identity_matches: Sequence[StructuralIdentityMatch] = (),
        evidence_baseline: EvidenceStateSnapshot,
        evidence_post: EvidenceStateSnapshot,
    ) -> TransformationalDelta:
        baseline.validate()
        post.validate()
        scope_before = (baseline.world_id, baseline.world_version, baseline.dgp_id,
                        baseline.dgp_version, baseline.unit_id, baseline.potential_axis,
                        baseline.potential_z, baseline.potential_label,
                        baseline.boundary_id, baseline.context_id, baseline.catalog_version)
        scope_after = (post.world_id, post.world_version, post.dgp_id,
                       post.dgp_version, post.unit_id, post.potential_axis,
                       post.potential_z, post.potential_label,
                       post.boundary_id, post.context_id, post.catalog_version)
        if scope_before != scope_after or baseline.timepoint != "BASELINE" or post.timepoint != "POST":
            raise ContractError("ΔT_acc* requires comparable BASELINE/POST snapshots in the same world/unit/potential-axis/boundary/context/catalog")
        before = {(a.component, a.canonical_id): a for a in baseline.atoms}
        after = {(a.component, a.canonical_id): a for a in post.atoms}
        matches = tuple(identity_matches)
        for match in matches:
            match.validate()
        if len({m.baseline_id for m in matches}) != len(matches) or len({m.post_id for m in matches}) != len(matches):
            raise ContractError("identity correspondence must be one-to-one")
        entries: list[StructuralDeltaEntry] = []
        consumed_before: set[tuple[str, str]] = set()
        consumed_after: set[tuple[str, str]] = set()

        def add_pair(component, left, right, unresolved=False):
            left_key = None if left is None else (component, left.canonical_id)
            right_key = None if right is None else (component, right.canonical_id)
            if left_key: consumed_before.add(left_key)
            if right_key: consumed_after.add(right_key)
            if unresolved:
                kind, state = "UNKNOWN", "?"
            elif left is None:
                complete = dict(baseline.component_complete)[component] and dict(post.component_complete)[component]
                kind, state = ("ADDED", 1) if complete else ("UNKNOWN", "?")
            elif right is None:
                complete = dict(baseline.component_complete)[component] and dict(post.component_complete)[component]
                kind, state = ("REMOVED", 1) if complete else ("UNKNOWN", "?")
            elif left.semantic_type != right.semantic_type:
                raise ContractError("semantic type mismatch cannot be silently matched across identities")
            elif left.state == "?" or right.state == "?":
                kind, state = "UNKNOWN", "?"
            elif (left.state, left.attributes) != (right.state, right.attributes):
                kind, state = "MODIFIED", 1
            else:
                kind, state = "UNCHANGED", 0
            entries.append(StructuralDeltaEntry(
                component, kind, state,
                None if left is None else left.canonical_id,
                None if right is None else right.canonical_id,
                _atom_fingerprint(left), _atom_fingerprint(right),
                None if right is None and left is None else (
                    right.semantic_type if right is not None else left.semantic_type
                ),
            ))

        for match in matches:
            left_candidates = [(key, atom) for key, atom in before.items()
                               if key[1] == match.baseline_id and key not in consumed_before]
            right_candidates = [(key, atom) for key, atom in after.items()
                                if key[1] == match.post_id and key not in consumed_after]
            if len(left_candidates) != 1 or len(right_candidates) != 1:
                raise ContractError("explicit identity correspondence must resolve exactly one atom on each side")
            (left_key, left), (right_key, right) = left_candidates[0], right_candidates[0]
            if left_key[0] != right_key[0]:
                raise ContractError("identity correspondence cannot move an object across U/R/C/X components")
            if match.match_state == 1 and left.semantic_type != right.semantic_type:
                raise ContractError("confirmed identity match requires the same semantic type")
            add_pair(left_key[0], left, right, unresolved=(match.match_state == "?"))

        for key in sorted(set(before) | set(after)):
            if key in consumed_before or key in consumed_after:
                continue
            left, right = before.get(key), after.get(key)
            if left is not None and right is not None:
                if left.semantic_type == right.semantic_type:
                    add_pair(key[0], left, right)
                else:
                    add_pair(key[0], left, None)
                    add_pair(key[0], None, right)
            else:
                add_pair(key[0], left, right)

        entries.sort(key=lambda row: (row.component, row.baseline_id or "", row.post_id or ""))
        changed_states = [row.change_state for row in entries]
        component_completeness = tuple(
            (component, dict(baseline.component_complete)[component]
             and dict(post.component_complete)[component])
            for component in ("U", "R", "C", "X")
        )
        if any(state == 1 for state in changed_states):
            delta_state: ReachState = 1
        elif any(state == "?" for state in changed_states) or not all(
            complete for _, complete in component_completeness
        ):
            delta_state = "?"
        else:
            delta_state = 0
        evidence_delta = _evidence_delta(evidence_baseline, evidence_post)
        by_component = {component: tuple(row for row in entries if row.component == component)
                        for component in ("U", "R", "C", "X")}
        payload = {
            "scope": scope_before, "baseline_snapshot_id": baseline.snapshot_id,
            "post_snapshot_id": post.snapshot_id, "entries": tuple(entries),
            "component_completeness": component_completeness,
            "delta_state": delta_state, "evidence_delta": evidence_delta,
        }
        result = TransformationalDelta(
            baseline.world_id, baseline.world_version, baseline.dgp_id,
            baseline.dgp_version, baseline.unit_id, baseline.potential_z,
            baseline.snapshot_id, post.snapshot_id, tuple(entries),
            by_component["U"], by_component["R"], by_component["C"], by_component["X"],
            component_completeness, delta_state, evidence_delta, digest(payload),
            baseline.potential_axis, baseline.potential_label,
        )
        result.validate()
        return result


@dataclass(frozen=True)
class D2StructuralPotentialPair:
    unit_id: str
    z: int
    focal_transformation_id: str
    baseline: TransformationalStateSnapshot
    post: TransformationalStateSnapshot
    evidence_baseline: EvidenceStateSnapshot
    evidence_post: EvidenceStateSnapshot
    identity_matches: tuple[StructuralIdentityMatch, ...] = ()
    focal_truth_sha256: str | None = None


def evaluate_d2_structural_deltas(
    world: "SyntheticWorldBundle",
    pairs_by_unit_z: dict[tuple[str, int], D2StructuralPotentialPair],
) -> tuple[TransformationalDelta, ...]:
    """Bind complete U/R/C/X baseline→post truth deltas to both D2 potentials.

    D2's focal A_f*/D_f* is checked against the focal U atom only; it is not
    substituted for the complete ΔT_acc* vector.
    """
    world.validate()
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(pairs_by_unit_z) != expected:
        raise ContractError("D2 structural pairs must cover every world unit × Z potential exactly")
    engine = TransformationalDeltaEngine()
    results = []
    units = {unit.unit_id: unit for unit in world.units}
    for key in sorted(expected):
        unit_id, z = key
        pair = pairs_by_unit_z[key]
        if (pair.unit_id, pair.z) != key or not pair.focal_transformation_id:
            raise ContractError("D2 structural pair identity/focal transformation binding is invalid")
        if pair.baseline.potential_axis != "Z" or pair.post.potential_axis != "Z":
            raise ContractError("D2 structural evaluator accepts only Z-axis potential snapshots")
        stage = units[unit_id].d2_potentials.potentials_by_z[z]
        expected_scope = (world.world_id, world.world_version, world.dgp_id,
                          world.dgp_version, unit_id, z)
        for snapshot in (pair.baseline, pair.post):
            actual_scope = (snapshot.world_id, snapshot.world_version, snapshot.dgp_id,
                            snapshot.dgp_version, snapshot.unit_id, snapshot.potential_z)
            if actual_scope != expected_scope:
                raise ContractError("D2 structural snapshot does not bind to its exact world/unit/Z potential")
        baseline_atoms = [a for a in pair.baseline.atoms
                          if a.component == "U" and a.canonical_id == pair.focal_transformation_id]
        post_atoms = [a for a in pair.post.atoms
                      if a.component == "U" and a.canonical_id == pair.focal_transformation_id]
        if len(baseline_atoms) != 1 or len(post_atoms) != 1:
            raise ContractError("D2 structural snapshots must contain exactly one focal U atom at baseline and post")
        focal_truth = units[unit_id].d2_potentials.focal_accessibility_truth
        expected_focal_hash = None if focal_truth is None else focal_truth.result_sha256
        if pair.focal_truth_sha256 != expected_focal_hash:
            raise ContractError("D2 structural pair is detached from its typed focal truth bundle")
        if focal_truth is None:
            expected_pre = 1 if units[unit_id].d2_baseline.focal_accessible_pre else 0
            expected_post = 1 if stage.a_f_post else 0
            expected_opening = "1" if (
                not units[unit_id].d2_baseline.focal_accessible_pre and stage.a_f_post
            ) else "0"
            if stage.d_f_opening != (expected_opening == "1"):
                raise ContractError("legacy D2 D_f_opening fixture is inconsistent with legacy A_f fields")
        else:
            post_truth = dict(focal_truth.post_by_z)[z]
            opening = dict(focal_truth.opening_by_z)[z]
            if opening.semantic_match_state != "MATCHED":
                raise ContractError("D2 structural delta requires confirmed semantic identity for the same focal tau2")
            if focal_truth.baseline.transformation_id != pair.focal_transformation_id:
                raise ContractError("D2 structural focal ID differs from typed baseline semantic transformation")
            expected_pre = {"1": 1, "0": 0, "?": "?"}[focal_truth.baseline.accessibility_truth]
            expected_post = {"1": 1, "0": 0, "?": "?"}[post_truth.accessibility_truth]
            if "?" in (focal_truth.baseline.accessibility_truth, post_truth.accessibility_truth):
                expected_opening = "?"
            else:
                expected_opening = "1" if (
                    focal_truth.baseline.accessibility_truth, post_truth.accessibility_truth
                ) == ("0", "1") else "0"
            if opening.d_f_truth != expected_opening:
                raise ContractError("typed D2 D_f* is inconsistent with baseline/post A_f*")
        if baseline_atoms[0].state != expected_pre or post_atoms[0].state != expected_post:
            raise ContractError("focal U accessibility truth disagrees with D2 baseline/A_f* potential truth")
        delta = engine.evaluate(
            pair.baseline, pair.post, identity_matches=pair.identity_matches,
            evidence_baseline=pair.evidence_baseline, evidence_post=pair.evidence_post,
        )        results.append(delta)
    return tuple(results)



@dataclass(frozen=True)
class StructuralTransitionRule:
    atom: StructuralAtom
    action: Literal["ADD", "REMOVE", "MODIFY"]
    trigger_stage: Literal[
        "w_programmed", "w_attempt", "receipt", "s_install",
        "c_dep_star", "a_f_post", "d_f_opening",
    ]
    trigger_when: bool = True

    def validate(self, invariant_atoms: Sequence[StructuralAtom]) -> None:
        self.atom.validate()
        if self.action not in ("ADD", "REMOVE", "MODIFY"):
            raise ContractError("structural transition action must be ADD/REMOVE/MODIFY")
        if self.trigger_stage not in (
            "w_programmed", "w_attempt", "receipt", "s_install",
            "c_dep_star", "a_f_post", "d_f_opening",
        ):
            raise ContractError("structural transition trigger is not an explicit D2 stage")
        existing = {atom.canonical_id: atom for atom in invariant_atoms}
        if self.action == "ADD" and self.atom.canonical_id in existing:
            raise ContractError("ADD transition target already exists in the baseline catalog")
        if self.action in ("REMOVE", "MODIFY") and self.atom.canonical_id not in existing:
            raise ContractError("REMOVE/MODIFY transition target must exist in the baseline catalog")
        if self.action in ("REMOVE", "MODIFY"):
            baseline = existing[self.atom.canonical_id]
            if baseline.component != self.atom.component or baseline.semantic_type != self.atom.semantic_type:
                raise ContractError("REMOVE/MODIFY transition must preserve component and semantic type")


@dataclass(frozen=True)
class D2StructuralGenerationConfig:
    """Explicit, versioned bridge from D2 focal admission to the focal U atom.

    Non-focal U/R/C/X atoms are a declared structural fixture and remain
    invariant in this minimal adapter. No C_dep* field is promoted to T_acc,
    applicability, relation or context.
    """
    config_id: str
    config_version: str
    focal_transformation_id: str
    focal_semantic_version: str
    boundary_id: str
    context_id: str
    catalog_version: str
    invariant_atoms: tuple[StructuralAtom, ...]
    transition_rules: tuple[StructuralTransitionRule, ...] = ()
    component_complete: tuple[tuple[StructuralComponent, bool], ...] = (
        ("U", True), ("R", True), ("C", True), ("X", True),
    )
    evidence_version: str = "C10S-TRUTH-PROJECTION-001"
    adjudication_version: str = "C10S-STRUCTURAL-ADJUDICATION-001"

    def validate(self) -> None:
        if not all((self.config_id, self.config_version, self.focal_transformation_id,
                    self.focal_semantic_version, self.boundary_id, self.context_id,
                    self.catalog_version, self.evidence_version, self.adjudication_version)):
            raise ContractError("D2 structural generation config identity and versions are mandatory")
        if any(atom.component not in ("U", "R", "C", "X") for atom in self.invariant_atoms):
            raise ContractError("invariant structural catalog contains an invalid component")
        if any(atom.canonical_id == self.focal_transformation_id for atom in self.invariant_atoms):
            raise ContractError("focal transformation must be generated from D2 potential truth, not duplicated in catalog")
        ids = [atom.canonical_id for atom in self.invariant_atoms]
        if len(ids) != len(set(ids)):
            raise ContractError("invariant structural catalog IDs must be unique")
        for atom in self.invariant_atoms:
            atom.validate()
        rule_ids = [rule.atom.canonical_id for rule in self.transition_rules]
        if len(rule_ids) != len(set(rule_ids)):
            raise ContractError("only one structural transition rule per canonical atom is allowed")
        for rule in self.transition_rules:
            rule.validate(self.invariant_atoms)
        completeness = dict(self.component_complete)
        if set(completeness) != {"U", "R", "C", "X"} or len(self.component_complete) != 4:
            raise ContractError("structural generator must explicitly declare U/R/C/X completeness")
        if any(type(value) is not bool for value in completeness.values()):
            raise ContractError("structural component completeness must be Boolean")


def generate_d2_structural_potential_pairs(
    world: "SyntheticWorldBundle",
    config: D2StructuralGenerationConfig,
) -> dict[tuple[str, int], D2StructuralPotentialPair]:
    """Materialize baseline/post structural truth for every unit × Z potential."""
    world.validate()
    config.validate()
    invariant = tuple(config.invariant_atoms)
    evidence_hash = digest({
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "structural_config": config,
        "typed_focal_truth_by_unit": tuple(
            (unit.unit_id,
             None if unit.d2_potentials.focal_accessibility_truth is None
             else unit.d2_potentials.focal_accessibility_truth.result_sha256)
            for unit in world.units
        ),
    })
    pairs: dict[tuple[str, int], D2StructuralPotentialPair] = {}
    for unit in world.units:
        focal_truth = unit.d2_potentials.focal_accessibility_truth
        if focal_truth is not None:
            if (
                focal_truth.baseline.transformation_id != config.focal_transformation_id
                or focal_truth.baseline.transformation_version != config.focal_semantic_version
                or focal_truth.baseline.boundary_id != config.boundary_id
                or focal_truth.baseline.context_id != config.context_id
            ):
                raise ContractError(
                    "D2 structural focal identity/boundary/context differs from typed baseline accessibility"
                )
        for z in (0, 1):
            stage = unit.d2_potentials.potentials_by_z[z]
            post_focal_truth = None if focal_truth is None else dict(focal_truth.post_by_z)[z]
            opening_truth = None if focal_truth is None else dict(focal_truth.opening_by_z)[z]
            if focal_truth is None:
                focal_baseline_state = 1 if unit.d2_baseline.focal_accessible_pre else 0
                focal_post_state = 1 if stage.a_f_post else 0
            else:
                if opening_truth.semantic_match_state != "MATCHED":
                    raise ContractError(
                        "D2 structural snapshot cannot map a focal transformation without confirmed semantic identity"
                    )
                if (
                    post_focal_truth.boundary_id != config.boundary_id
                    or post_focal_truth.context_id != config.context_id
                ):
                    raise ContractError("D2 post focal identity boundary/context differs from structural config")
                focal_baseline_state = {"1": 1, "0": 0, "?": "?"}[
                    focal_truth.baseline.accessibility_truth
                ]
                focal_post_state = {"1": 1, "0": 0, "?": "?"}[
                    post_focal_truth.accessibility_truth
                ]
            focal_baseline = StructuralAtom(
                "U", config.focal_transformation_id, "TRANSFORMATION",
                config.focal_semantic_version, focal_baseline_state,
                (("role", "D2_FOCAL"), ("boundary_id", config.boundary_id)),
            )
            focal_post = StructuralAtom(
                "U", config.focal_transformation_id, "TRANSFORMATION",
                config.focal_semantic_version, focal_post_state,
                (("role", "D2_FOCAL"), ("boundary_id", config.boundary_id)),
            )
            baseline_atoms = (focal_baseline,) + invariant
            post_by_id = {atom.canonical_id: atom for atom in invariant}
            for rule in config.transition_rules:
                if focal_truth is not None and rule.trigger_stage in ("a_f_post", "d_f_opening"):
                    trigger_truth = (
                        post_focal_truth.accessibility_truth
                        if rule.trigger_stage == "a_f_post"
                        else opening_truth.d_f_truth
                    )
                    if trigger_truth not in ("1", "0"):
                        raise ContractError(
                            f"typed D2 {rule.trigger_stage} is UNKNOWN/NOT_COMPARABLE and cannot drive a deterministic structural rule"
                        )
                    triggered = (trigger_truth == "1") is rule.trigger_when
                else:
                    triggered = getattr(stage, rule.trigger_stage) is rule.trigger_when
                if not triggered:
                    continue
                if rule.action == "ADD":
                    post_by_id[rule.atom.canonical_id] = rule.atom
                elif rule.action == "REMOVE":
                    post_by_id.pop(rule.atom.canonical_id)
                else:
                    post_by_id[rule.atom.canonical_id] = rule.atom
            post_atoms = (focal_post,) + tuple(
                post_by_id[key] for key in sorted(post_by_id)
            )
            common = (
                world.world_id, world.world_version, world.dgp_id, world.dgp_version,
                unit.unit_id, z, config.boundary_id, config.context_id, config.catalog_version,
            )
            baseline_snapshot = TransformationalStateSnapshot(
                f"{world.world_id}:{unit.unit_id}:Z{z}:BASE",
                config.config_version, *common[:4], common[4], common[5], "BASELINE",
                common[6], common[7], common[8], baseline_atoms, config.component_complete,
            )
            post_snapshot = TransformationalStateSnapshot(
                f"{world.world_id}:{unit.unit_id}:Z{z}:POST",
                config.config_version, *common[:4], common[4], common[5], "POST",
                common[6], common[7], common[8], post_atoms, config.component_complete,
            )
            baseline_snapshot.validate()
            post_snapshot.validate()
            source_refs = [f"{unit.d2_baseline.baseline_history_ref}:STRUCTURAL-CATALOG"]
            if focal_truth is not None:
                source_refs.append(f"D2-FOCAL-TRUTH:{focal_truth.result_sha256}")
            evidence = EvidenceStateSnapshot(
                f"{world.world_id}:{unit.unit_id}:Z{z}:STRUCTURAL-TRUTH",
                tuple(source_refs),
                "COMPLETE" if all(value for _, value in config.component_complete) else "PARTIAL",
                "VALID", evidence_hash, config.evidence_version, config.adjudication_version,
            )
            pairs[(unit.unit_id, z)] = D2StructuralPotentialPair(
                unit.unit_id, z, config.focal_transformation_id,
                baseline_snapshot, post_snapshot, evidence, evidence, (),
                None if focal_truth is None else focal_truth.result_sha256,
            )
    # The ordinary delta evaluator remains the single adjudication path.
    evaluate_d2_structural_deltas(world, pairs)
    return pairs


@dataclass(frozen=True)
class GAStructuralTransitionRule:
    """Explicit mapping from a complete g_A vector predicate to one structural atom change.

    Vector coordinates have no implicit U/R/C/X meaning. The rule names the
    concrete atom, component, action and complete predicate; mapping identity
    and version are supplied separately to generate_factorial_structural_potentials.
    """
    atom: StructuralAtom
    action: Literal["ADD", "REMOVE", "MODIFY"]
    vector_predicates: tuple[tuple[int, object], ...]

    def validate(self, baseline_atoms: Sequence[StructuralAtom]) -> None:
        self.atom.validate()
        if self.action not in ("ADD", "REMOVE", "MODIFY"):
            raise ContractError("g_A structural action must be ADD/REMOVE/MODIFY")
        if (not isinstance(self.vector_predicates, tuple) or not self.vector_predicates
                or any(not isinstance(row, tuple) or len(row) != 2 for row in self.vector_predicates)):
            raise ContractError("g_A structural rule requires explicit non-empty vector predicates")
        indices = [row[0] for row in self.vector_predicates]
        if (any(type(index) is not int or index not in range(4) for index in indices)
                or len(indices) != len(set(indices))):
            raise ContractError("g_A structural predicates require unique vector indices [0..3]")
        if any(value is None for _, value in self.vector_predicates):
            raise ContractError("g_A structural predicates cannot use null values")
        existing = {atom.canonical_id: atom for atom in baseline_atoms}
        if self.action == "ADD" and self.atom.canonical_id in existing:
            raise ContractError("g_A ADD target already exists in the baseline structural catalog")
        if self.action in ("REMOVE", "MODIFY") and self.atom.canonical_id not in existing:
            raise ContractError("g_A REMOVE/MODIFY target must exist in the baseline structural catalog")
        if self.action in ("REMOVE", "MODIFY"):
            baseline = existing[self.atom.canonical_id]
            if (baseline.component, baseline.semantic_type) != (self.atom.component, self.atom.semantic_type):
                raise ContractError("g_A structural transition must preserve component and semantic type")


@dataclass(frozen=True)
class FactorialStructuralPotential:
    history_ref: str
    unit_id: str
    vector: Vector4
    vector_sha256: str
    r_common_fingerprint: str
    mapping_id: str
    mapping_version: str
    mapping_sha256: str
    baseline: TransformationalStateSnapshot
    post: TransformationalStateSnapshot
    delta: TransformationalDelta
    evidence_baseline: EvidenceStateSnapshot
    evidence_post: EvidenceStateSnapshot

    def validate(self, world: "SyntheticWorldBundle") -> None:
        world.validate()
        self.baseline.validate()
        self.post.validate()
        self.delta.validate()
        self.evidence_baseline.validate()
        self.evidence_post.validate()
        if self.vector_sha256 != digest(self.vector) or len(self.vector) != 4:
            raise ContractError("factorial structural potential must retain its exact complete g_A vector")
        if not all((self.mapping_id, self.mapping_version, self.mapping_sha256)):
            raise ContractError("factorial structural potential requires versioned g_A mapping provenance")
        if (self.baseline.unit_id, self.post.unit_id, self.baseline.potential_axis,
                self.post.potential_axis, self.baseline.potential_z, self.post.potential_z,
                self.baseline.potential_label, self.post.potential_label,
                self.delta.potential_axis, self.delta.potential_z, self.delta.potential_label) != (
                self.unit_id, self.unit_id, "G_A", "G_A", None, None,
                self.potential_label, self.potential_label, "G_A", None, self.potential_label):
            raise ContractError("factorial structural snapshots/delta must bind to the exact vector/r_common potential")
        if (self.baseline.world_id, self.baseline.world_version, self.baseline.dgp_id,
                self.baseline.dgp_version) != (
                world.world_id, world.world_version, world.dgp_id, world.dgp_version):
            raise ContractError("factorial structural potential belongs to a different world/DGP")
        if (self.post.world_id, self.post.world_version, self.post.dgp_id,
                self.post.dgp_version, self.post.unit_id) != (
                world.world_id, world.world_version, world.dgp_id, world.dgp_version, self.unit_id):
            raise ContractError("factorial post snapshot belongs to a different world/DGP/unit")
        if (self.delta.baseline_snapshot_id, self.delta.post_snapshot_id) != (
                self.baseline.snapshot_id, self.post.snapshot_id):
            raise ContractError("factorial ΔT_acc* is detached from its exact structural snapshots")
        if (self.delta.world_id, self.delta.world_version, self.delta.dgp_id,
                self.delta.dgp_version, self.delta.unit_id) != (
                world.world_id, world.world_version, world.dgp_id, world.dgp_version, self.unit_id):
            raise ContractError("factorial ΔT_acc* belongs to a different world/DGP/unit")

    @property
    def potential_label(self) -> str:
        return f"{self.vector_sha256}:{self.r_common_fingerprint}"


def generate_factorial_structural_potentials(
    world: "SyntheticWorldBundle",
    config: D2StructuralGenerationConfig,
    g_a0: Sequence["JointPolicyHistory"],
    g_a1: Sequence["JointPolicyHistory"],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence["RCommonPairCertificate"],
    rules: Sequence[GAStructuralTransitionRule],
    *,
    mapping_id: str,
    mapping_version: str,
) -> dict[tuple[str, str, str], FactorialStructuralPotential]:
    """Materialize ΔT_acc* for every supported q_X* × complete-vector × r_common potential.

    The mapping is deliberately explicit: no Vector4 coordinate is assumed to
    be a U/R/C/X component. Rules that do not match a vector leave the declared
    structural catalog unchanged, which is a legitimate null structural effect.
    """
    world.validate()
    config.validate()
    if not mapping_id or not mapping_version:
        raise ContractError("g_A structural mapping identity and version are mandatory")
    mapping_sha256 = digest((mapping_id, mapping_version, tuple(rules), config.config_id, config.config_version))
    qx_by_ref = {row.history_ref: row for row in world.q_x}
    expected_refs = set(qx_by_ref)
    unit_by_ref = {
        unit.d2_baseline.baseline_history_ref: unit for unit in world.units
    }
    if set(unit_by_ref) != expected_refs:
        raise ContractError("factorial structural mapping requires exact q_X* to unit correspondence")
    policy_maps = []
    for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in rows}
        if len(mapping) != len(rows) or set(mapping) != expected_refs:
            raise ContractError(f"{label} structural policy must cover q_X* exactly")
        policy_maps.append(mapping)
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != expected_refs:
        raise ContractError("factorial structural potentials require one r_common certificate per q_X* history")
    if len({(row.regime_id, row.regime_version) for row in certs.values()}) != 1:
        raise ContractError("factorial structural potentials require one common r_common identity/version")
    for cert in certs.values():
        if (cert.status != "COMMON_FIXED" or not cert.regime_id or not cert.regime_version
                or not cert.g_a0_fingerprint or cert.g_a0_fingerprint != cert.g_a1_fingerprint):
            raise ContractError("factorial structural potentials require certified fixed common r_common")
    result = {}
    engine = TransformationalDeltaEngine()
    for history_ref in sorted(expected_refs):
        unit = unit_by_ref[history_ref]
        cert = certs[history_ref]
        baseline_atoms = (
            StructuralAtom(
                "U", config.focal_transformation_id, "TRANSFORMATION",
                config.focal_semantic_version,
                1 if unit.d2_baseline.focal_accessible_pre else 0,
                (("role", "D2_FOCAL"), ("boundary_id", config.boundary_id)),
            ),
        ) + tuple(config.invariant_atoms)
        feasible = {digest(vector) for vector in feasible_vectors_by_history.get(history_ref, ())}
        if not feasible:
            raise ContractError(f"joint structural feasibility is absent for q_X* history {history_ref}")
        vector_support = {}
        for arm, policy in enumerate(policy_maps):
            _distribution_total(policy[history_ref].distribution, f"g_A{arm} distribution for {history_ref}")
            for vector, probability in policy[history_ref].distribution:
                if not isinstance(vector, tuple) or len(vector) != 4:
                    raise ContractError("g_A structural potentials require the complete four-coordinate vector")
                if digest(vector) not in feasible:
                    raise ContractError(f"g_A{arm} support exceeds structural feasibility for {history_ref}")
                if probability > 0:
                    vector_support[digest(vector)] = vector
        for vector_sha, vector in sorted(vector_support.items()):
            for rule in rules:
                rule.validate(baseline_atoms)
            matched_rules = [
                rule for rule in rules
                if all(vector[index] == value for index, value in rule.vector_predicates)
            ]
            matched_targets = [rule.atom.canonical_id for rule in matched_rules]
            if len(matched_targets) != len(set(matched_targets)):
                raise ContractError("g_A structural mapping has overlapping predicates for one atom/vector")
            post_by_id = {atom.canonical_id: atom for atom in baseline_atoms}
            for rule in matched_rules:
                if rule.action == "ADD":
                    if rule.atom.canonical_id in post_by_id:
                        raise ContractError("g_A structural ADD target already exists in this potential")
                    post_by_id[rule.atom.canonical_id] = rule.atom
                elif rule.action == "REMOVE":
                    if rule.atom.canonical_id not in post_by_id:
                        raise ContractError("g_A structural REMOVE target is absent in this potential")
                    post_by_id.pop(rule.atom.canonical_id)
                else:
                    if rule.atom.canonical_id not in post_by_id:
                        raise ContractError("g_A structural MODIFY target is absent in this potential")
                    post_by_id[rule.atom.canonical_id] = rule.atom
            label = f"{vector_sha}:{cert.g_a0_fingerprint}"
            base_id = f"{world.world_id}:{unit.unit_id}:GA:{label}:BASE"
            post_id = f"{world.world_id}:{unit.unit_id}:GA:{label}:POST"
            common = (
                world.world_id, world.world_version, world.dgp_id, world.dgp_version,
                unit.unit_id, None, config.boundary_id, config.context_id, config.catalog_version,
            )
            baseline = TransformationalStateSnapshot(
                base_id, config.config_version, *common[:4], common[4], common[5],
                "BASELINE", common[6], common[7], common[8],
                baseline_atoms, config.component_complete, "G_A", label,
            )
            post = TransformationalStateSnapshot(
                post_id, config.config_version, *common[:4], common[4], common[5],
                "POST", common[6], common[7], common[8],
                tuple(post_by_id[key] for key in sorted(post_by_id)),
                config.component_complete, "G_A", label,
            )
            baseline.validate()
            post.validate()
            evidence_hash = digest({
                "world": (world.world_id, world.world_version, world.dgp_id, world.dgp_version),
                "unit_id": unit.unit_id, "history_ref": history_ref,
                "vector": vector, "r_common": cert, "structural_config": config,
                "mapping_id": mapping_id, "mapping_version": mapping_version,
                "mapping_sha256": mapping_sha256, "rules": tuple(rules),
            })
            evidence_base = EvidenceStateSnapshot(
                f"{base_id}:E_T", (f"{history_ref}:QX_BASELINE",),
                "COMPLETE" if all(v for _, v in config.component_complete) else "PARTIAL",
                "VALID", evidence_hash, config.evidence_version, config.adjudication_version,
            )
            evidence_post = EvidenceStateSnapshot(
                f"{post_id}:E_T", (f"{history_ref}:GA_POTENTIAL:{label}",),
                "COMPLETE" if all(v for _, v in config.component_complete) else "PARTIAL",
                "VALID", evidence_hash, config.evidence_version, config.adjudication_version,
            )
            delta = engine.evaluate(
                baseline, post, evidence_baseline=evidence_base, evidence_post=evidence_post,
            )
            potential = FactorialStructuralPotential(
                history_ref, unit.unit_id, vector, vector_sha, cert.g_a0_fingerprint,
                mapping_id, mapping_version, mapping_sha256,
                baseline, post, delta, evidence_base, evidence_post,
            )
            potential.validate(world)
            result[(history_ref, vector_sha, cert.g_a0_fingerprint)] = potential
    expected_support = {
        (history_ref, digest(vector), certs[history_ref].g_a0_fingerprint)
        for history_ref in expected_refs
        for policy_map in policy_maps
        for vector, probability in policy_map[history_ref].distribution
        if probability > 0
    }
    if set(result) != expected_support:
        raise ContractError("factorial structural potentials do not cover exact positive-mass g_A joint-policy support")
    return result


@dataclass(frozen=True)
class FactorialReachPotential:
    history_ref: str
    unit_id: str
    vector_sha256: str
    r_common_fingerprint: str
    baseline: ReachabilityResult
    post: ReachabilityResult
    delta_by_target: tuple[tuple[str, ReachState], ...]
    result_sha256: str

    def validate(self, potential: FactorialStructuralPotential, config: "D2ReachGenerationConfig") -> None:
        self.baseline.validate()
        self.post.validate()
        if (self.history_ref, self.unit_id, self.vector_sha256, self.r_common_fingerprint) != (
            potential.history_ref, potential.unit_id, potential.vector_sha256,
            potential.r_common_fingerprint,
        ):
            raise ContractError("factorial Reach potential is detached from its exact g_A structural potential")
        if (self.baseline.snapshot_id, self.post.snapshot_id) != (
            f"{potential.baseline.snapshot_id}:REACH:BASELINE",
            f"{potential.post.snapshot_id}:REACH:POST",
        ):
            raise ContractError("factorial Reach snapshots do not derive from the exact structural snapshots")
        expected_label = potential.potential_label
        if (potential.baseline.potential_axis, potential.post.potential_axis,
                potential.baseline.potential_z, potential.post.potential_z,
                potential.baseline.potential_label, potential.post.potential_label) != (
                "G_A", "G_A", None, None, expected_label, expected_label):
            raise ContractError("factorial Reach snapshots must preserve exact g_A vector/r_common identity")
        if set(dict(self.baseline.target_states)) != set(config.target_states) or set(
            dict(self.post.target_states)
        ) != set(config.target_states):
            raise ContractError("factorial Reach target support differs from its versioned configuration")
        if set(dict(self.delta_by_target)) != set(config.target_states):
            raise ContractError("factorial Reach deltas do not cover the exact target universe")
        baseline_states, post_states = dict(self.baseline.target_states), dict(self.post.target_states)
        expected_delta = {
            target: ("?" if "?" in (baseline_states[target], post_states[target])
                     else (0 if baseline_states[target] == post_states[target] else 1))
            for target in config.target_states
        }
        if dict(self.delta_by_target) != expected_delta:
            raise ContractError("factorial Reach delta does not match its baseline/post potential states")
        if not self.result_sha256:
            raise ContractError("factorial Reach potential digest is required")


def evaluate_factorial_structural_reachability(
    world: "SyntheticWorldBundle",
    structural_potentials: dict[tuple[str, str, str], FactorialStructuralPotential],
    config: "D2ReachGenerationConfig",
) -> dict[tuple[str, str, str], FactorialReachPotential]:
    """Derive Reach for each exact q_X* × g_A-vector × r_common potential."""
    world.validate()
    config.validate()
    unit_by_history = {
        unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
    }
    expected_refs = set(unit_by_history)
    if not structural_potentials:
        raise ContractError("factorial structural potentials are required before Reach")
    engine = StructuralReachabilityEngine()
    results = {}
    for key, potential in sorted(structural_potentials.items()):
        potential.validate(world)
        if key != (potential.history_ref, potential.vector_sha256, potential.r_common_fingerprint):
            raise ContractError("factorial structural potential dictionary key mismatch")
        if potential.history_ref not in expected_refs or unit_by_history[potential.history_ref] != potential.unit_id:
            raise ContractError("factorial structural potential history/unit is outside q_X*")
        def make_snapshot(source, atoms, complete, timepoint):
            transformations = []
            for transformation_id in config.transformation_universe:
                atom = atoms.get(transformation_id)
                if atom is None:
                    state = 0 if complete["U"] else "?"
                else:
                    if atom.component != "U":
                        raise ContractError("declared transformation universe ID resolves to a non-U atom")
                    state = atom.state
                transformations.append(StructuralTransformation(
                    transformation_id, atom.semantic_version if atom else "ABSENT-OR-UNKNOWN",
                    f"{source.snapshot_id}:REACH:{timepoint}", state,
                ))
            return StructuralSnapshot(
                f"{source.snapshot_id}:REACH:{timepoint}", config.snapshot_version,
                source.world_id, source.world_version, source.dgp_id, source.dgp_version,
                source.unit_id, source.potential_z, source.boundary_id, source.context_id,
                config.horizon, tuple(transformations),
                config.universe_exhaustive and complete["U"],
                config.relations_exhaustive and complete["R"],
                config.conditions_exhaustive and complete["C"],
                config.resources_exhaustive, config.catalog_version,
                source.potential_axis, source.potential_label,
            )
        def make_routes(atoms, complete):
            routes = []
            for template in config.route_templates:
                steps = []
                for step in template.steps:
                    predicates = tuple(
                        (name, _reach_atom_state(atoms, atom_id, component, complete))
                        for name, component, atom_id in step.predicate_atom_bindings
                    )
                    steps.append(StructuralRouteStep(
                        step.transformation_id, step.state_before, step.state_after,
                        step.applicability_state, predicates, step.duration,
                    ))
                relations = tuple(
                    _reach_atom_state(atoms, atom_id, component, complete)
                    for component, atom_id in template.relation_atom_bindings
                )
                routes.append(StructuralRoute(
                    template.route_id, template.target_state, tuple(steps),
                    relations, template.temporal_feasibility_state, template.route_scope,
                ))
            return tuple(routes)
        base_atoms = {atom.canonical_id: atom for atom in potential.baseline.atoms}
        post_atoms = {atom.canonical_id: atom for atom in potential.post.atoms}
        base_complete = dict(potential.baseline.component_complete)
        post_complete = dict(potential.post.component_complete)
        base_snapshot = make_snapshot(potential.baseline, base_atoms, base_complete, "BASELINE")
        post_snapshot = make_snapshot(potential.post, post_atoms, post_complete, "POST")
        baseline = engine.evaluate(
            base_snapshot, make_routes(base_atoms, base_complete),
            enumeration_complete=config.enumeration_complete,
            search_truncated=config.search_truncated, target_states=config.target_states,
        )
        post = engine.evaluate(
            post_snapshot, make_routes(post_atoms, post_complete),
            enumeration_complete=config.enumeration_complete,
            search_truncated=config.search_truncated, target_states=config.target_states,
        )
        base_states, post_states = dict(baseline.target_states), dict(post.target_states)
        delta = tuple(
            (target, "?" if "?" in (base_states[target], post_states[target])
             else (0 if base_states[target] == post_states[target] else 1))
            for target in sorted(config.target_states)
        )
        payload = {
            "world": (world.world_id, world.world_version, world.dgp_id, world.dgp_version),
            "structural_potential": key, "reach_config": config,
            "baseline": baseline, "post": post, "delta_by_target": delta,
        }
        result = FactorialReachPotential(
            potential.history_ref, potential.unit_id, potential.vector_sha256,
            potential.r_common_fingerprint, baseline, post, delta, digest(payload),
        )
        result.validate(potential, config)
        results[key] = result
    expected_keys = set(structural_potentials)
    if set(results) != expected_keys:
        raise ContractError("factorial Reach must cover exact structural potential support")
    return results


@dataclass(frozen=True)
class FactorialPotentialTrajectory:
    history_ref: str
    unit_id: str
    vector_sha256: str
    r_common_fingerprint: str
    target_state: str
    reach_state: ReachState
    selection_state: ReachState
    selected_route_id: str | None
    execution_state: ReachState
    trajectory_status: Literal[
        "COMPLETED", "PARTIAL", "NOT_SELECTED", "EXECUTION_FAILED", "NOT_REACHABLE", "UNKNOWN",
    ]
    executed_steps: tuple[ExecutedTrajectoryStep, ...]
    terminal_state: str | None

    def validate(self, reach: FactorialReachPotential) -> None:
        if (self.history_ref, self.unit_id, self.vector_sha256, self.r_common_fingerprint) != (
            reach.history_ref, reach.unit_id, reach.vector_sha256, reach.r_common_fingerprint,
        ):
            raise ContractError("factorial trajectory is detached from its exact Reach potential")
        _reach_state(self.reach_state, "factorial trajectory Reach")
        _reach_state(self.selection_state, "factorial trajectory selection")
        _reach_state(self.execution_state, "factorial trajectory execution")
        target_reach = dict(reach.post.target_states).get(self.target_state)
        if target_reach != self.reach_state:
            raise ContractError("factorial trajectory Reach differs from post-potential adjudication")
        route_rows = {row.route_id: row for row in reach.post.route_evaluations}
        if self.selected_route_id is not None:
            selected = route_rows.get(self.selected_route_id)
            if selected is None or selected.target_state != self.target_state or selected.route_state != 1:
                raise ContractError("factorial trajectory selected a route not confirmed by Reach")
        if self.selection_state == 1 and (self.reach_state != 1 or self.selected_route_id is None):
            raise ContractError("factorial route selection requires confirmed Reach and an exact route")
        if self.selected_route_id is None and self.executed_steps:
            raise ContractError("factorial trajectory cannot execute steps without a selected route")
        if self.selection_state == 1 and self.selected_route_id is None:
            raise ContractError("selected factorial trajectory must identify its exact route")
        if self.selection_state != 1 and self.selected_route_id is not None:
            raise ContractError("unselected factorial trajectory cannot identify a route")
        if self.reach_state == 0 and (
            self.selection_state != 0 or self.execution_state != 0
            or self.trajectory_status != "NOT_REACHABLE"
        ):
            raise ContractError("factorial Reach=0 must yield NOT_REACHABLE without selection/execution")
        if self.reach_state == "?" and (
            self.selection_state != "?" or self.execution_state != "?"
            or self.trajectory_status != "UNKNOWN"
        ):
            raise ContractError("factorial Reach=? must remain UNKNOWN without selection/execution")
        if self.selection_state == 0 and self.reach_state == 1 and (
            self.execution_state != 0 or self.trajectory_status != "NOT_SELECTED"
        ):
            raise ContractError("confirmed but unselected factorial route must remain NOT_SELECTED")
        if self.trajectory_status == "COMPLETED" and self.execution_state != 1:
            raise ContractError("completed factorial trajectory requires successful execution")
        if self.trajectory_status == "PARTIAL" and (self.execution_state != 0 or not self.executed_steps):
            raise ContractError("partial factorial trajectory requires an executed prefix and failed execution")
        if self.trajectory_status in (
            "NOT_SELECTED", "EXECUTION_FAILED", "NOT_REACHABLE", "UNKNOWN",
        ) and self.executed_steps:
            raise ContractError("non-executed factorial trajectory status cannot contain executed steps")
        if self.executed_steps:
            for left, right in zip(self.executed_steps, self.executed_steps[1:]):
                if left.state_after != right.state_before:
                    raise ContractError("factorial executed trajectory is discontinuous")
            if self.terminal_state != self.executed_steps[-1].state_after:
                raise ContractError("factorial trajectory terminal state differs from executed prefix")
        elif self.terminal_state is not None:
            raise ContractError("factorial trajectory without executed steps cannot declare a terminal state")


def evaluate_factorial_potential_trajectories(
    world: "SyntheticWorldBundle",
    reach_potentials: dict[tuple[str, str, str], FactorialReachPotential],
    reach_config: "D2ReachGenerationConfig",
    config: "D2TrajectoryGenerationConfig",
) -> dict[tuple[str, str, str, str], FactorialPotentialTrajectory]:
    """Generate route selection/execution for each factorial vector potential."""
    world.validate()
    reach_config.validate()
    config.validate(reach_config)
    selection_probability = dict(config.selection_probability_by_target)
    route_weights = dict(config.route_selection_weight)
    route_execution = dict(config.route_execution_probability)
    step_execution = dict(config.step_execution_probability)
    route_by_id = {route.route_id: route for route in reach_config.route_templates}
    results = {}
    for key, reach in sorted(reach_potentials.items()):
        if key != (reach.history_ref, reach.vector_sha256, reach.r_common_fingerprint):
            raise ContractError("factorial Reach dictionary key mismatch")
        for target in reach_config.target_states:
            target_reach = dict(reach.post.target_states)[target]
            candidates = [row for row in reach.post.route_evaluations if row.target_state == target]
            confirmed = [row for row in candidates if row.route_state == 1]
            unknown = [row for row in candidates if row.route_state == "?"]
            # Common random numbers across g_A vector potentials preserve
            # within-unit counterfactual pairing for route selection/execution.
            identity = (reach.unit_id, target)
            if confirmed:
                total_weight = sum(route_weights[row.route_id] for row in confirmed)
                draw = _dgp_uniform(
                    world.seed_commitment_sha256, config.randomization_salt, *identity, "selection-route",
                )
                cumulative = 0.0
                selected = confirmed[-1]
                for candidate in sorted(confirmed, key=lambda row: row.route_id):
                    cumulative += route_weights[candidate.route_id] / total_weight
                    if draw < cumulative:
                        selected = candidate
                        break
                selected_flag = _dgp_uniform(
                    world.seed_commitment_sha256, config.randomization_salt, *identity, "selection",
                ) < selection_probability[target]
                if not selected_flag:
                    result = FactorialPotentialTrajectory(
                        reach.history_ref, reach.unit_id, reach.vector_sha256,
                        reach.r_common_fingerprint, target, target_reach, 0, None, 0,
                        "NOT_SELECTED", (), None,
                    )
                else:
                    route = route_by_id[selected.route_id]
                    if _dgp_uniform(
                        world.seed_commitment_sha256, config.randomization_salt, *identity,
                        selected.route_id, "route-execution",
                    ) >= route_execution[selected.route_id]:
                        result = FactorialPotentialTrajectory(
                            reach.history_ref, reach.unit_id, reach.vector_sha256,
                            reach.r_common_fingerprint, target, target_reach, 1,
                            selected.route_id, 0, "EXECUTION_FAILED", (), None,
                        )
                    else:
                        executed = []
                        failed = False
                        for index, step in enumerate(route.steps):
                            success = _dgp_uniform(
                                world.seed_commitment_sha256, config.randomization_salt,
                                *identity, selected.route_id, index,
                                step.transformation_id, "step-execution",
                            ) < step_execution[step.transformation_id]
                            if not success:
                                failed = True
                                break
                            executed.append(ExecutedTrajectoryStep(
                                step.transformation_id, step.state_before, step.state_after, 1, step.duration,
                            ))
                        status = ("PARTIAL" if executed else "EXECUTION_FAILED") if failed else "COMPLETED"
                        result = FactorialPotentialTrajectory(
                            reach.history_ref, reach.unit_id, reach.vector_sha256,
                            reach.r_common_fingerprint, target, target_reach, 1,
                            selected.route_id, 0 if failed else 1, status, tuple(executed),
                            executed[-1].state_after if executed else None,
                        )
            elif target_reach == 0 and not unknown:
                result = FactorialPotentialTrajectory(
                    reach.history_ref, reach.unit_id, reach.vector_sha256,
                    reach.r_common_fingerprint, target, target_reach, 0, None, 0,
                    "NOT_REACHABLE", (), None,
                )
            elif target_reach == "?":
                result = FactorialPotentialTrajectory(
                    reach.history_ref, reach.unit_id, reach.vector_sha256,
                    reach.r_common_fingerprint, target, target_reach, "?",
                    None, "?", "UNKNOWN", (), None,
                )
            else:
                raise ContractError("factorial Reach=1 requires a confirmed route for selection")
            result.validate(reach)
            results[(reach.history_ref, reach.vector_sha256, reach.r_common_fingerprint, target)] = result
    expected = {
        (reach.history_ref, reach.vector_sha256, reach.r_common_fingerprint, target)
        for reach in reach_potentials.values() for target in reach_config.target_states
    }
    if set(results) != expected:
        raise ContractError("factorial trajectories must cover exact vector-potential × target support")
    return results



@dataclass(frozen=True)
class D2ReachStepTemplate:
    transformation_id: str
    state_before: str
    state_after: str
    applicability_state: ReachState
    duration: float = 0.0
    predicate_atom_bindings: tuple[tuple[str, StructuralComponent, str], ...] = ()

    def validate(self) -> None:
        if not all((self.transformation_id, self.state_before, self.state_after)):
            raise ContractError("D2 Reach step template requires transformation and state identities")
        _reach_state(self.applicability_state, "D2 route App state")
        if not math.isfinite(self.duration) or self.duration < 0:
            raise ContractError("D2 route duration must be finite and nonnegative")
        names = [name for name, _, _ in self.predicate_atom_bindings]
        if len(names) != len(set(names)) or any(not name or not atom_id for name, _, atom_id in self.predicate_atom_bindings):
            raise ContractError("D2 route predicate bindings must have unique names and atom identities")
        for _, component, _ in self.predicate_atom_bindings:
            if component not in ("R", "C", "X"):
                raise ContractError("route step predicate bindings must reference R/C/X atoms")


@dataclass(frozen=True)
class D2ReachRouteTemplate:
    route_id: str
    target_state: str
    steps: tuple[D2ReachStepTemplate, ...]
    relation_atom_bindings: tuple[tuple[StructuralComponent, str], ...]
    temporal_feasibility_state: ReachState
    route_scope: str

    def validate(self) -> None:
        if not all((self.route_id, self.target_state, self.route_scope)) or not self.steps:
            raise ContractError("D2 Reach route template requires route, target, scope and steps")
        if len(self.relation_atom_bindings) != len(self.steps) - 1:
            raise ContractError("D2 Reach route requires one explicit R binding between adjacent steps")
        for step in self.steps:
            step.validate()
        for component, atom_id in self.relation_atom_bindings:
            if component != "R" or not atom_id:
                raise ContractError("route relation bindings must identify explicit R atoms")
        _reach_state(self.temporal_feasibility_state, "D2 route temporal feasibility")


@dataclass(frozen=True)
class D2ReachGenerationConfig:
    config_id: str
    config_version: str
    horizon: float
    transformation_universe: tuple[str, ...]
    target_states: tuple[str, ...]
    route_templates: tuple[D2ReachRouteTemplate, ...]
    universe_exhaustive: bool
    relations_exhaustive: bool
    conditions_exhaustive: bool
    resources_exhaustive: bool
    enumeration_complete: bool
    search_truncated: bool = False
    snapshot_version: str = "C10S-REACH-SNAPSHOT-001"
    catalog_version: str = "C10S-REACH-CATALOG-001"

    def validate(self) -> None:
        if not self.config_id or not self.config_version or not self.snapshot_version or not self.catalog_version:
            raise ContractError("D2 Reach config identity and versions are mandatory")
        if not math.isfinite(self.horizon) or self.horizon <= 0:
            raise ContractError("D2 Reach horizon must be positive and finite")
        if not self.transformation_universe or len(self.transformation_universe) != len(set(self.transformation_universe)):
            raise ContractError("D2 Reach transformation universe must be finite, nonempty and unique")
        if not self.target_states or len(self.target_states) != len(set(self.target_states)) or any(not x for x in self.target_states):
            raise ContractError("D2 Reach target universe must be explicit, nonempty and unique")
        route_ids = [route.route_id for route in self.route_templates]
        if len(route_ids) != len(set(route_ids)):
            raise ContractError("D2 Reach route template IDs must be unique")
        if self.search_truncated and self.enumeration_complete:
            raise ContractError("truncated D2 route search cannot be declared complete")
        for route in self.route_templates:
            route.validate()
            if any(step.transformation_id not in self.transformation_universe for step in route.steps):
                raise ContractError("D2 route references a transformation outside the declared universe")


@dataclass(frozen=True)
class D2PotentialReachContrast:
    unit_id: str
    z: int
    baseline: ReachabilityResult
    post: ReachabilityResult
    delta_by_target: tuple[tuple[str, ReachState], ...]


@dataclass(frozen=True)
class SyntheticWorldReachabilityContrast:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    contrasts: tuple[D2PotentialReachContrast, ...]
    result_sha256: str

    def validate(self, world: "SyntheticWorldBundle") -> None:
        world.validate()
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("Reach contrast identity differs from its synthetic world")
        expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
        actual = {(row.unit_id, row.z) for row in self.contrasts}
        if actual != expected or len(actual) != len(self.contrasts):
            raise ContractError("Reach contrasts must cover every unit × Z potential exactly")
        for row in self.contrasts:
            row.baseline.validate()
            row.post.validate()
            if set(dict(row.baseline.target_states)) != set(dict(row.post.target_states)):
                raise ContractError("baseline/post Reach target universes differ")
            if dict(row.delta_by_target).keys() != dict(row.post.target_states).keys():
                raise ContractError("Reach contrast delta does not cover the exact target universe")
        if not self.result_sha256:
            raise ContractError("Reach contrast fingerprint is required")


@dataclass(frozen=True)
class D2TrajectoryGenerationConfig:
    """Explicit DGP rules for route selection and execution after Reach."""
    config_id: str
    config_version: str
    selection_probability_by_target: tuple[tuple[str, float], ...]
    route_selection_weight: tuple[tuple[str, float], ...]
    route_execution_probability: tuple[tuple[str, float], ...]
    step_execution_probability: tuple[tuple[str, float], ...]
    randomization_salt: str

    def validate(self, reach_config: D2ReachGenerationConfig) -> None:
        if not all((self.config_id, self.config_version, self.randomization_salt)):
            raise ContractError("trajectory config identity, version and randomization salt are mandatory")
        for rows, label in (
            (self.selection_probability_by_target, "selection probability"),
            (self.route_selection_weight, "route selection weight"),
            (self.route_execution_probability, "route execution probability"),
            (self.step_execution_probability, "step execution probability"),
        ):
            keys = [key for key, _ in rows]
            if len(keys) != len(set(keys)) or any(not key for key in keys):
                raise ContractError(f"{label} keys must be nonempty and unique")
            for _, value in rows:
                if not math.isfinite(value):
                    raise ContractError(f"{label} values must be finite")
        selection = dict(self.selection_probability_by_target)
        weights = dict(self.route_selection_weight)
        route_exec = dict(self.route_execution_probability)
        step_exec = dict(self.step_execution_probability)
        if set(selection) != set(reach_config.target_states):
            raise ContractError("trajectory selection probabilities must cover the exact Reach target universe")
        for value in selection.values():
            _probability(value, "route selection probability")
        route_ids = {route.route_id for route in reach_config.route_templates}
        if set(weights) != route_ids or set(route_exec) != route_ids:
            raise ContractError("route weights and execution probabilities must cover the exact route catalog")
        if any(value <= 0 for value in weights.values()):
            raise ContractError("route selection weights must be strictly positive")
        for value in route_exec.values():
            _probability(value, "route execution probability")
        step_ids = {step.transformation_id for route in reach_config.route_templates for step in route.steps}
        if set(step_exec) != step_ids:
            raise ContractError("step execution probabilities must cover the exact transformation steps")
        for value in step_exec.values():
            _probability(value, "step execution probability")


@dataclass(frozen=True)
class ExecutedTrajectoryStep:
    transformation_id: str
    state_before: str
    state_after: str
    executed_state: Literal[0, 1]
    duration: float


@dataclass(frozen=True)
class D2PotentialTrajectory:
    unit_id: str
    z: int
    target_state: str
    reach_state: ReachState
    selection_state: ReachState
    selected_route_id: str | None
    execution_state: ReachState
    trajectory_status: Literal[
        "COMPLETED", "PARTIAL", "NOT_SELECTED", "EXECUTION_FAILED", "NOT_REACHABLE", "UNKNOWN",
    ]
    executed_steps: tuple[ExecutedTrajectoryStep, ...]
    terminal_state: str | None

    def validate(self) -> None:
        if not self.unit_id or self.z not in (0, 1) or not self.target_state:
            raise ContractError("potential trajectory requires exact unit, Z and target identity")
        _reach_state(self.reach_state, "trajectory Reach")
        _reach_state(self.selection_state, "trajectory selection")
        _reach_state(self.execution_state, "trajectory execution")
        if self.selected_route_id is None and self.executed_steps:
            raise ContractError("trajectory cannot contain executed steps without a selected route")
        if self.selection_state == 1 and self.selected_route_id is None:
            raise ContractError("selected trajectory must identify its route")
        if self.selection_state != 1 and self.selected_route_id is not None:
            raise ContractError("unselected/unknown trajectory cannot identify a selected route")
        if self.trajectory_status == "COMPLETED" and self.execution_state != 1:
            raise ContractError("completed trajectory requires successful execution")
        if self.trajectory_status == "PARTIAL" and (self.execution_state != 0 or not self.executed_steps):
            raise ContractError("partial trajectory requires a nonempty executed prefix and failed execution")
        if self.trajectory_status in ("NOT_SELECTED", "EXECUTION_FAILED", "NOT_REACHABLE", "UNKNOWN") and self.executed_steps:
            raise ContractError("non-executed trajectory status cannot contain executed steps")
        if self.executed_steps:
            for left, right in zip(self.executed_steps, self.executed_steps[1:]):
                if left.state_after != right.state_before:
                    raise ContractError("executed trajectory state sequence is discontinuous")
            if self.terminal_state != self.executed_steps[-1].state_after:
                raise ContractError("trajectory terminal state differs from its executed prefix")
        elif self.terminal_state is not None:
            raise ContractError("trajectory without executed steps cannot declare a terminal state")


@dataclass(frozen=True)
class SyntheticWorldTrajectoryBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    trajectories: tuple[D2PotentialTrajectory, ...]
    result_sha256: str

    def validate(self, world: "SyntheticWorldBundle", reach: SyntheticWorldReachabilityContrast,
                 reach_config: D2ReachGenerationConfig) -> None:
        world.validate()
        reach.validate(world)
        expected = {
            (unit.unit_id, z, target)
            for unit in world.units for z in (0, 1) for target in reach_config.target_states
        }
        actual = {(row.unit_id, row.z, row.target_state) for row in self.trajectories}
        if actual != expected or len(actual) != len(self.trajectories):
            raise ContractError("potential trajectories must cover every unit × Z × target exactly")
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("trajectory bundle identity differs from its synthetic world")
        reach_by_key = {(row.unit_id, row.z): row for row in reach.contrasts}
        for row in self.trajectories:
            row.validate()
            potential = reach_by_key[(row.unit_id, row.z)]
            target_reach = dict(potential.post.target_states)[row.target_state]
            if row.reach_state != target_reach:
                raise ContractError("trajectory Reach state differs from its post-potential adjudication")
            route_rows = {item.route_id: item for item in potential.post.route_evaluations}
            if row.selected_route_id is not None:
                selected = route_rows.get(row.selected_route_id)
                if selected is None or selected.target_state != row.target_state or selected.route_state != 1:
                    raise ContractError("selected trajectory route is not a confirmed route to its target")
            if row.selection_state == 1 and row.reach_state != 1:
                raise ContractError("route selection cannot occur without confirmed Reach")
            if row.reach_state == 0 and (row.selection_state != 0 or row.trajectory_status != "NOT_REACHABLE"):
                raise ContractError("Reach=0 must yield no selection and NOT_REACHABLE")
            if row.reach_state == "?" and row.trajectory_status != "UNKNOWN":
                raise ContractError("unknown Reach cannot yield a determinate trajectory")
        if not self.result_sha256:
            raise ContractError("trajectory bundle fingerprint is required")


def _dgp_uniform(*parts: object) -> float:
    return int(digest(parts)[:16], 16) / float(16 ** 16)


def evaluate_d2_potential_trajectories(
    world: "SyntheticWorldBundle",
    reach: SyntheticWorldReachabilityContrast,
    reach_config: D2ReachGenerationConfig,
    config: D2TrajectoryGenerationConfig,
) -> SyntheticWorldTrajectoryBundle:
    """Generate potential selection/execution/trajectory without equating Reach to action."""
    world.validate()
    reach.validate(world)
    reach_config.validate()
    config.validate(reach_config)
    selection_probability = dict(config.selection_probability_by_target)
    route_weights = dict(config.route_selection_weight)
    route_execution = dict(config.route_execution_probability)
    step_execution = dict(config.step_execution_probability)
    contrasts = {(row.unit_id, row.z): row for row in reach.contrasts}
    trajectories = []
    for unit in world.units:
        for z in (0, 1):
            contrast = contrasts[(unit.unit_id, z)]
            route_evaluations = contrast.post.route_evaluations
            for target in reach_config.target_states:
                target_reach = dict(contrast.post.target_states)[target]
                candidates = [row for row in route_evaluations if row.target_state == target]
                confirmed = [row for row in candidates if row.route_state == 1]
                unknown = [row for row in candidates if row.route_state == "?"]
                if confirmed:
                    total_weight = sum(route_weights[row.route_id] for row in confirmed)
                    draw = _dgp_uniform(world.seed_commitment_sha256, config.randomization_salt, unit.unit_id, target, "selection-route")
                    cumulative = 0.0
                    selected = confirmed[-1]
                    for candidate in sorted(confirmed, key=lambda row: row.route_id):
                        cumulative += route_weights[candidate.route_id] / total_weight
                        if draw < cumulative:
                            selected = candidate
                            break
                    selected_flag = (
                        _dgp_uniform(world.seed_commitment_sha256, config.randomization_salt, unit.unit_id, target, "selection")
                        < selection_probability[target]
                    )
                    if not selected_flag:
                        trajectories.append(D2PotentialTrajectory(
                            unit.unit_id, z, target, target_reach, 0, None, 0,
                            "NOT_SELECTED", (), None,
                        ))
                        continue
                    route_template = next(route for route in reach_config.route_templates
                                          if route.route_id == selected.route_id)
                    if _dgp_uniform(world.seed_commitment_sha256, config.randomization_salt, unit.unit_id, target,
                                    selected.route_id, "route-execution") >= route_execution[selected.route_id]:
                        trajectories.append(D2PotentialTrajectory(
                            unit.unit_id, z, target, target_reach, 1, selected.route_id, 0,
                            "EXECUTION_FAILED", (), None,
                        ))
                        continue
                    executed = []
                    failed = False
                    for index, step in enumerate(route_template.steps):
                        success = _dgp_uniform(
                            world.seed_commitment_sha256, config.randomization_salt,
                            unit.unit_id, target, selected.route_id, index,
                            step.transformation_id, "step-execution",
                        ) < step_execution[step.transformation_id]
                        if not success:
                            failed = True
                            break
                        executed.append(ExecutedTrajectoryStep(
                            step.transformation_id, step.state_before, step.state_after, 1, step.duration,
                        ))
                    if failed:
                        status = "PARTIAL" if executed else "EXECUTION_FAILED"
                        execution_state = 0
                    else:
                        status = "COMPLETED"
                        execution_state = 1
                    trajectories.append(D2PotentialTrajectory(
                        unit.unit_id, z, target, target_reach, 1, selected.route_id,
                        execution_state, status, tuple(executed),
                        executed[-1].state_after if executed else None,
                    ))
                elif target_reach == 0 and not unknown:
                    trajectories.append(D2PotentialTrajectory(
                        unit.unit_id, z, target, target_reach, 0, None, 0,
                        "NOT_REACHABLE", (), None,
                    ))
                elif target_reach == "?":
                    trajectories.append(D2PotentialTrajectory(
                        unit.unit_id, z, target, "?", "?", None, "?",
                        "UNKNOWN", (), None,
                    ))
                else:
                    raise ContractError("Reach=1 requires at least one confirmed route for selection")
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "reach_sha256": reach.result_sha256, "reach_config": reach_config,
        "trajectory_config": config, "trajectories": tuple(trajectories),
    }
    result = SyntheticWorldTrajectoryBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        tuple(trajectories), digest(payload),
    )
    result.validate(world, reach, reach_config)
    return result



def _reach_atom_state(
    atoms_by_id: dict[str, StructuralAtom],
    atom_id: str,
    component: StructuralComponent,
    component_complete: dict[str, bool],
) -> ReachState:
    atom = atoms_by_id.get(atom_id)
    if atom is None:
        return 0 if component_complete[component] else "?"
    if atom.component != component:
        raise ContractError("D2 Reach binding component disagrees with structural atom")
    return atom.state


def evaluate_d2_structural_reachability(
    world: "SyntheticWorldBundle",
    structural_pairs: dict[tuple[str, int], D2StructuralPotentialPair],
    config: D2ReachGenerationConfig,
) -> SyntheticWorldReachabilityContrast:
    """Derive baseline/post Reach from generated U/R/C/X truth plus explicit route rules."""
    world.validate()
    config.validate()
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(structural_pairs) != expected:
        raise ContractError("D2 Reach input must cover every unit × Z structural pair exactly")
    engine = StructuralReachabilityEngine()
    contrasts = []
    for key in sorted(expected):
        pair = structural_pairs[key]
        if (pair.unit_id, pair.z) != key:
            raise ContractError("D2 Reach structural pair key mismatch")
        baseline = pair.baseline
        post = pair.post
        scope = (world.world_id, world.world_version, world.dgp_id, world.dgp_version, key[0], key[1])
        for snapshot in (baseline, post):
            if (snapshot.world_id, snapshot.world_version, snapshot.dgp_id,
                    snapshot.dgp_version, snapshot.unit_id, snapshot.potential_z) != scope:
                raise ContractError("D2 Reach structural snapshot is not bound to exact world/unit/Z")
        base_atoms = {atom.canonical_id: atom for atom in baseline.atoms}
        post_atoms = {atom.canonical_id: atom for atom in post.atoms}
        base_complete = dict(baseline.component_complete)
        post_complete = dict(post.component_complete)

        def make_snapshot(source, atoms, complete, timepoint):
            transformations = []
            for transformation_id in config.transformation_universe:
                atom = atoms.get(transformation_id)
                if atom is None:
                    state = 0 if complete["U"] else "?"
                else:
                    if atom.component != "U":
                        raise ContractError("declared transformation universe ID resolves to a non-U atom")
                    state = atom.state
                transformations.append(StructuralTransformation(
                    transformation_id, atom.semantic_version if atom else "ABSENT-OR-UNKNOWN",
                    f"{source.snapshot_id}:REACH:{timepoint}", state,
                ))
            return StructuralSnapshot(
                f"{source.snapshot_id}:REACH:{timepoint}", config.snapshot_version,
                source.world_id, source.world_version, source.dgp_id, source.dgp_version,
                source.unit_id, source.potential_z, source.boundary_id, source.context_id,
                config.horizon, tuple(transformations),
                config.universe_exhaustive and complete["U"],
                config.relations_exhaustive and complete["R"],
                config.conditions_exhaustive and complete["C"],
                config.resources_exhaustive,
                config.catalog_version,
            )

        def make_routes(atoms, complete):
            routes = []
            for template in config.route_templates:
                steps = []
                for step in template.steps:
                    predicates = tuple(
                        (name, _reach_atom_state(atoms, atom_id, component, complete))
                        for name, component, atom_id in step.predicate_atom_bindings
                    )
                    steps.append(StructuralRouteStep(
                        step.transformation_id, step.state_before, step.state_after,
                        step.applicability_state, predicates, step.duration,
                    ))
                relations = tuple(
                    _reach_atom_state(atoms, atom_id, component, complete)
                    for component, atom_id in template.relation_atom_bindings
                )
                routes.append(StructuralRoute(
                    template.route_id, template.target_state, tuple(steps),
                    relations, template.temporal_feasibility_state, template.route_scope,
                ))
            return tuple(routes)

        base_reach_snapshot = make_snapshot(baseline, base_atoms, base_complete, "BASELINE")
        post_reach_snapshot = make_snapshot(post, post_atoms, post_complete, "POST")
        base_result = engine.evaluate(
            base_reach_snapshot, make_routes(base_atoms, base_complete),
            enumeration_complete=config.enumeration_complete,
            search_truncated=config.search_truncated, target_states=config.target_states,
        )
        post_result = engine.evaluate(
            post_reach_snapshot, make_routes(post_atoms, post_complete),
            enumeration_complete=config.enumeration_complete,
            search_truncated=config.search_truncated, target_states=config.target_states,
        )
        base_states, post_states = dict(base_result.target_states), dict(post_result.target_states)
        delta = tuple(
            (target, "?" if "?" in (base_states[target], post_states[target])
             else (0 if base_states[target] == post_states[target] else 1))
            for target in sorted(config.target_states)
        )
        contrasts.append(D2PotentialReachContrast(key[0], key[1], base_result, post_result, delta))
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "config": config, "contrasts": tuple(contrasts),
    }
    result = SyntheticWorldReachabilityContrast(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        tuple(contrasts), digest(payload),
    )
    result.validate(world)
    return result


@dataclass(frozen=True)
class NeedPreZStipulation:
    """Reserved, explicit pre-Z B1 objective stipulation for one synthetic UE.

    This is an input to the DGP truth composer, never a stochastic draw,
    covariate, observed evidence record, or post-treatment classification.
    """
    unit_id: str
    b1_id: str
    service_instance_id: str
    contract_id: str
    contract_version: str
    instance_version: int
    package_version: str
    baseline_record_id: str
    baseline_time: str
    stipulation: str
    rule_version: str
    basis_ref: str

    def validate(self) -> None:
        required = (
            self.unit_id, self.b1_id, self.service_instance_id, self.contract_id,
            self.contract_version, self.instance_version, self.package_version,
            self.baseline_record_id, self.baseline_time, self.rule_version, self.basis_ref,
        )
        if not all(required):
            raise ContractError("Need_preZ stipulation identity, binding, baseline and provenance are mandatory")
        if type(self.instance_version) is not int or self.instance_version < 1:
            raise ContractError("B1 service instance_version must be a positive monotonic integer")
        if self.baseline_time != "t-1":
            raise ContractError("Need_preZ truth must be fixed at baseline t-1, before Z at t0")
        if self.stipulation not in ("FOCAL_INCLUSION", "FOCAL_EXCLUSION", "SEMANTIC_INDETERMINACY"):
            raise ContractError("Need_preZ requires an explicit inclusion, exclusion or semantic-indeterminacy stipulation")


@dataclass(frozen=True)
class NeedPreZTruthRecord:
    unit_id: str
    b1_id: str
    service_instance_id: str
    contract_id: str
    contract_version: str
    instance_version: int
    package_version: str
    baseline_record_id: str
    baseline_time: str
    need_truth_state: TriState
    rule_version: str
    truth_basis_ref: str
    stipulation_sha256: str


@dataclass(frozen=True)
class NeedPreZTruthBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    roster_id: str
    roster_version: str
    records: tuple[NeedPreZTruthRecord, ...]
    result_sha256: str

    def validate(self, world: "SyntheticWorldBundle") -> None:
        world.validate()
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version,
                self.roster_id, self.roster_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version,
            world.roster_id, world.roster_version
        ):
            raise ContractError("Need_preZ truth bundle must bind to the exact world and census roster versions")
        expected = {unit.unit_id for unit in world.units}
        actual = [row.unit_id for row in self.records]
        if set(actual) != expected or len(actual) != len(expected):
            raise ContractError("Need_preZ truth must cover the complete applicable UE census exactly once")
        b1_ids = [row.b1_id for row in self.records]
        service_ids = [row.service_instance_id for row in self.records]
        baseline_ids = [row.baseline_record_id for row in self.records]
        if (len(set(b1_ids)) != len(b1_ids)
                or len(set(service_ids)) != len(service_ids)
                or len(set(baseline_ids)) != len(baseline_ids)):
            raise ContractError("Need_preZ census requires unique B1, service-instance and baseline-record bindings")
        package_contracts = {
            (row.contract_id, row.contract_version, row.package_version, row.rule_version)
            for row in self.records
        }
        if len(package_contracts) != 1:
            raise ContractError("Need_preZ census must use one common versioned B1 contract, package and truth rule")
        for row in self.records:
            if (not all((row.b1_id, row.service_instance_id, row.contract_id,
                         row.contract_version, row.package_version,
                         row.baseline_record_id, row.rule_version, row.truth_basis_ref,
                         row.stipulation_sha256))
                    or type(row.instance_version) is not int or row.instance_version < 1
                    or row.baseline_time != "t-1"
                    or row.need_truth_state not in (0, 1, "?")):
                raise ContractError("Need_preZ truth row has incomplete binding, provenance or invalid state")
        payload = {
            "world_id": self.world_id, "world_version": self.world_version,
            "dgp_id": self.dgp_id, "dgp_version": self.dgp_version,
            "roster_id": self.roster_id, "roster_version": self.roster_version,
            "records": self.records,
        }
        if digest(payload) != self.result_sha256:
            raise ContractError("Need_preZ reserved truth fingerprint does not match its records")


def materialize_need_prez_truth(
    world: "SyntheticWorldBundle",
    stipulations: Sequence[NeedPreZStipulation],
) -> NeedPreZTruthBundle:
    """Compose reserved Need_preZ truth only from explicit versioned stipulations.

    Missing/duplicate units and invalid bindings are integrity errors, never
    truth=0 or truth=?. No prevalence, random draw, proxy, or post-Z field is used.
    """
    world.validate()
    expected = {unit.unit_id for unit in world.units}
    by_unit = {}
    for stipulation in stipulations:
        stipulation.validate()
        if stipulation.unit_id in by_unit:
            raise ContractError("Need_preZ census contains duplicate UE stipulations")
        by_unit[stipulation.unit_id] = stipulation
    if set(by_unit) != expected:
        raise ContractError("Need_preZ stipulations must cover the exact complete world roster; omissions block materialization")
    records = []
    for unit in world.units:
        row = by_unit[unit.unit_id]
        state = {
            "FOCAL_INCLUSION": 1,
            "FOCAL_EXCLUSION": 0,
            "SEMANTIC_INDETERMINACY": "?",
        }[row.stipulation]
        stipulation_hash = digest(row)
        records.append(NeedPreZTruthRecord(
            row.unit_id, row.b1_id, row.service_instance_id, row.contract_id,
            row.contract_version, row.instance_version, row.package_version,
            row.baseline_record_id, row.baseline_time, state, row.rule_version, row.basis_ref,
            stipulation_hash,
        ))
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "roster_id": world.roster_id, "roster_version": world.roster_version,
        "records": tuple(records),
    }
    result = NeedPreZTruthBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        world.roster_id, world.roster_version, tuple(records), digest(payload),
    )
    result.validate(world)
    return result


@dataclass(frozen=True)
class SyntheticWorldConfig:
    """Explicit finite target-world fixture; masses are q_X* inputs, not sample frequencies."""
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    roster_id: str
    roster_version: str
    unit_id_prefix: str
    n_units: int
    seed: int
    x_dimension: int
    h0_distribution: tuple[tuple[str, float], ...]
    c_c_dimension: int
    c_c_component_probability: float
    focal_accessible_pre_probability: float
    c_auth_base_probability: float
    c_resource_probability: float
    c_capacity_probability: float
    c_info_probability: float
    c_domain_probability: float
    c_other_probability: float
    q_x_mass_by_unit: tuple[float, ...]

    def validate(self) -> None:
        if not all((self.world_id, self.world_version, self.dgp_id, self.dgp_version,
                    self.roster_id, self.roster_version, self.unit_id_prefix)):
            raise ContractError("synthetic world, DGP and roster identities/versions are required")
        if self.n_units < 1 or self.x_dimension < 1 or self.c_c_dimension < 1:
            raise ContractError("synthetic roster and baseline dimensions must be positive")
        _distribution_total(self.h0_distribution, "H0 target distribution")
        if any(not isinstance(label, str) or not label for label, _ in self.h0_distribution):
            raise ContractError("H0 support labels must be nonempty strings")
        for label, probability in (
            ("C_c component", self.c_c_component_probability),
            ("focal baseline accessibility", self.focal_accessible_pre_probability),
            ("C_auth,base", self.c_auth_base_probability),
            ("C_resource", self.c_resource_probability),
            ("C_capacity", self.c_capacity_probability),
            ("C_info", self.c_info_probability),
            ("C_domain", self.c_domain_probability),
            ("C_other", self.c_other_probability),
        ):
            _probability(probability, label)
        if len(self.q_x_mass_by_unit) != self.n_units:
            raise ContractError("q_X* must supply one explicit target mass per synthetic baseline history")
        if any(not math.isfinite(mass) or mass <= 0.0 for mass in self.q_x_mass_by_unit):
            raise ContractError("q_X* target masses must be positive and finite")
        if abs(sum(self.q_x_mass_by_unit) - 1.0) > 1e-12:
            raise ContractError("q_X* target masses must sum to one")


@dataclass(frozen=True)
class SyntheticWorldUnit:
    unit_id: str
    x_ref: str
    h0_ref: str
    c_c_ref: str
    x: tuple[float, ...]
    h0: str
    c_c: tuple[bool, ...]
    d2_baseline: D2Baseline
    d2_potentials: D2PotentialBundle


@dataclass(frozen=True)
class SyntheticWorldBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    roster_id: str
    roster_version: str
    configuration_sha256: str
    seed_commitment_sha256: str
    d2_mechanism_sha256: str
    units: tuple[SyntheticWorldUnit, ...]
    q_x: tuple[QXHistoryMass, ...]
    roster_sha256: str

    def validate(self) -> None:
        if not all((self.world_id, self.world_version, self.dgp_id, self.dgp_version,
                    self.roster_id, self.roster_version, self.configuration_sha256,
                    self.seed_commitment_sha256, self.d2_mechanism_sha256,
                    self.roster_sha256)):
            raise ContractError("synthetic world identity, versions and fingerprints are required")
        unit_ids = [unit.unit_id for unit in self.units]
        history_refs = [row.history_ref for row in self.q_x]
        if not unit_ids or len(unit_ids) != len(set(unit_ids)):
            raise ContractError("synthetic world roster must be nonempty and uniquely keyed")
        if len(history_refs) != len(set(history_refs)) or set(history_refs) != {
            unit.d2_baseline.baseline_history_ref for unit in self.units
        }:
            raise ContractError("q_X* must bind exactly once to every generated baseline history")
        if len(self.q_x) != len(self.units) or abs(sum(row.mass for row in self.q_x) - 1.0) > 1e-12 or any(
            not math.isfinite(row.mass) or row.mass <= 0.0 for row in self.q_x
        ):
            raise ContractError("q_X* must bind one positive target mass per unit and sum to one")
        focal_truth_presence = [
            unit.d2_potentials.focal_accessibility_truth is not None for unit in self.units
        ]
        if any(focal_truth_presence) and not all(focal_truth_presence):
            raise ContractError("typed D2 focal truth must cover the complete world roster or be absent")
        roster_payload = []
        for unit, qx in zip(self.units, self.q_x):
            unit.d2_baseline.validate()
            unit.d2_potentials.validate()
            if unit.d2_baseline.unit_id != unit.unit_id or unit.d2_potentials.unit_id != unit.unit_id:
                raise ContractError("synthetic world unit, D2 baseline and potential identities differ")
            if (qx.history_ref != unit.d2_baseline.baseline_history_ref
                    or qx.x_ref != unit.x_ref or qx.h0_ref != unit.h0_ref
                    or qx.c_c_ref != unit.c_c_ref):
                raise ContractError("q_X* history/X/H0/C_c anchors must bind to the exact roster unit")
            if (unit.d2_potentials.dgp_id != self.dgp_id
                    or unit.d2_potentials.dgp_version != self.dgp_version):
                raise ContractError("D2 potential bundle DGP identity/version differs from world")
            if len(unit.x) == 0 or len(unit.c_c) == 0 or not unit.h0:
                raise ContractError("synthetic baseline X/H0/C_c must be materialized")
            roster_payload.append({
                "unit_id": unit.unit_id, "x_ref": unit.x_ref, "h0_ref": unit.h0_ref,
                "c_c_ref": unit.c_c_ref, "x": unit.x, "h0": unit.h0,
                "c_c": unit.c_c,
                "d2_baseline": unit.d2_baseline,
                "d2_potentials": unit.d2_potentials,
            })
        if digest(tuple(roster_payload)) != self.roster_sha256:
            raise ContractError("synthetic world roster fingerprint does not match materialized contents")


@dataclass(frozen=True)
class D2PotentialVContTruth:
    unit_id: str
    z: int
    potential_id: str
    history_id: str
    history_sha256: str
    grid_id: str
    grid_version: str
    rules_version: str
    interval_truth: tuple[TriState, ...]
    v_cont_truth: float


@dataclass(frozen=True)
class D2VContTruthBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    run_id: str
    grid_id: str
    grid_version: str
    potential_truth: tuple[D2PotentialVContTruth, ...]
    finite_population_itt_z_v_cont: float
    q_x_sha256: str
    result_sha256: str

    def validate(
        self,
        world: "SyntheticWorldBundle",
        histories_by_unit_z: dict[tuple[str, int], EventHistory],
        grid: IntervalGrid,
    ) -> None:
        world.validate()
        grid.validate()
        expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
        if set(histories_by_unit_z) != expected:
            raise ContractError("V_cont truth requires exactly one EventHistory per unit × Z potential")
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("V_cont truth identity differs from its synthetic world")
        if (self.grid_id, self.grid_version) != (grid.grid_id, grid.grid_version):
            raise ContractError("V_cont truth grid identity differs from its common adjudication grid")
        histories = tuple(histories_by_unit_z[key] for key in sorted(expected))
        run_ids = {history.run_id for history in histories}
        history_ids = [history.history_id for history in histories]
        potential_ids = [history.potential_id for history in histories]
        if len(run_ids) != 1 or self.run_id not in run_ids:
            raise ContractError("all potential EventHistories must share the declared run identity")
        if len(history_ids) != len(set(history_ids)) or len(potential_ids) != len(set(potential_ids)):
            raise ContractError("potential EventHistory and potential IDs must be unique")
        if len(self.potential_truth) != len(expected):
            raise ContractError("V_cont truth row count must equal unit × Z potential coverage")
        rows = {(row.unit_id, row.z): row for row in self.potential_truth}
        if set(rows) != expected or len(rows) != len(self.potential_truth):
            raise ContractError("V_cont truth rows must cover every unit × Z potential exactly")
        for key in sorted(expected):
            history = histories_by_unit_z[key]
            history.validate(require_complete=True)
            if (history.world_id, history.world_version, history.dgp_version, history.unit_id) != (
                world.world_id, world.world_version, world.dgp_version, key[0]
            ):
                raise ContractError("EventHistory does not bind to its exact world/unit potential")
            adjudication = adjudicate_intervals(history, grid)
            row = rows[key]
            if (row.potential_id, row.history_id, row.history_sha256, row.grid_id,
                    row.grid_version, row.rules_version, row.interval_truth, row.v_cont_truth) != (
                history.potential_id, history.history_id, history.content_sha256,
                grid.grid_id, grid.grid_version, history.adjudication_rules_version,
                adjudication.interval_truth, adjudication.v_cont_truth
            ):
                raise ContractError("V_cont potential truth does not reproduce from its reserved EventHistory")
        masses = {unit.unit_id: qx.mass for unit, qx in zip(world.units, world.q_x)}
        expected_itt = sum(
            masses[unit.unit_id] * (
                rows[(unit.unit_id, 1)].v_cont_truth - rows[(unit.unit_id, 0)].v_cont_truth
            ) for unit in world.units
        )
        if not math.isclose(self.finite_population_itt_z_v_cont, expected_itt, rel_tol=0.0, abs_tol=1e-12):
            raise ContractError("finite-population ITT-Z truth does not match q_X*-weighted potential contrast")
        expected_payload = {
            "world_id": world.world_id, "world_version": world.world_version,
            "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
            "run_id": self.run_id, "grid": grid,
            "potential_truth": self.potential_truth, "q_x": world.q_x,
            "finite_population_itt_z_v_cont": self.finite_population_itt_z_v_cont,
        }
        if self.q_x_sha256 != digest(world.q_x) or self.result_sha256 != digest(expected_payload):
            raise ContractError("V_cont truth q_X* provenance or result fingerprint is invalid")


def evaluate_d2_vcont_potential_truth(
    world: "SyntheticWorldBundle",
    histories_by_unit_z: dict[tuple[str, int], EventHistory],
    grid: IntervalGrid,
) -> D2VContTruthBundle:
    """Adjudicate B1 V_cont for both D2 assignment potentials, independently of trajectory."""
    world.validate()
    grid.validate()
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(histories_by_unit_z) != expected:
        raise ContractError("V_cont truth requires exactly one EventHistory per unit × Z potential")
    rows = []
    run_ids = set()
    for key in sorted(expected):
        history = histories_by_unit_z[key]
        history.validate(require_complete=True)
        if (history.world_id, history.world_version, history.dgp_version, history.unit_id) != (
            world.world_id, world.world_version, world.dgp_version, key[0]
        ):
            raise ContractError("EventHistory does not bind to its exact world/unit potential")
        if history.support_start != grid.boundaries[0] or history.support_end != grid.boundaries[-1]:
            raise ContractError("all V_cont potential histories must share the exact common grid support")
        adjudication = adjudicate_intervals(history, grid)
        run_ids.add(history.run_id)
        rows.append(D2PotentialVContTruth(
            key[0], key[1], history.potential_id, history.history_id,
            history.content_sha256, grid.grid_id, grid.grid_version,
            history.adjudication_rules_version, adjudication.interval_truth,
            adjudication.v_cont_truth,
        ))
    if len(run_ids) != 1:
        raise ContractError("all V_cont potential histories must belong to one run")
    row_map = {(row.unit_id, row.z): row for row in rows}
    masses = {unit.unit_id: qx.mass for unit, qx in zip(world.units, world.q_x)}
    itt_z = sum(
        masses[unit.unit_id] * (
            row_map[(unit.unit_id, 1)].v_cont_truth - row_map[(unit.unit_id, 0)].v_cont_truth
        ) for unit in world.units
    )
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "run_id": next(iter(run_ids)), "grid": grid,
        "potential_truth": tuple(rows), "q_x": world.q_x,
        "finite_population_itt_z_v_cont": itt_z,
    }
    result = D2VContTruthBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        next(iter(run_ids)), grid.grid_id, grid.grid_version, tuple(rows),
        itt_z, digest(world.q_x), digest(payload),
    )
    result.validate(world, histories_by_unit_z, grid)
    return result



class SyntheticWorldBuilder:
    """Materialize a finite baseline roster, q_X* masses and both D2 potentials.

    This builder deliberately does not infer D_f* -> ΔT_acc* -> Reach/trajectory.
    Those mappings remain separate contracts and must not be fabricated here.
    """
    version = "c10s-synthetic-world-builder-0.1"

    def generate(
        self, config: SyntheticWorldConfig, d2_config: D2MechanismConfig,
        focal_accessibility_specs_by_unit: dict[str, D2FocalAccessibilitySpecification] | None = None,
    ) -> SyntheticWorldBundle:
        config.validate()
        d2_config.validate()
        if config.dgp_id != d2_config.dgp_id or config.dgp_version != d2_config.dgp_version:
            raise ContractError("world and D2 mechanism must bind to the same DGP identity/version")
        rng = random.Random(config.seed)
        h0_labels = [label for label, _ in config.h0_distribution]
        h0_weights = [weight for _, weight in config.h0_distribution]
        expected_unit_ids = {
            f"{config.unit_id_prefix}-{index + 1:06d}" for index in range(config.n_units)
        }
        if focal_accessibility_specs_by_unit is not None:
            if set(focal_accessibility_specs_by_unit) != expected_unit_ids:
                raise ContractError(
                    "typed D2 focal specifications must cover every and only generated world unit"
                )
        units = []
        q_x = []
        for index in range(config.n_units):
            unit_id = f"{config.unit_id_prefix}-{index + 1:06d}"
            x_ref = f"{config.roster_id}-X-{index + 1:06d}"
            h0_ref = f"{config.roster_id}-H0-{index + 1:06d}"
            c_c_ref = f"{config.roster_id}-CC-{index + 1:06d}"
            history_ref = f"{config.roster_id}-BASE-{index + 1:06d}"
            x = tuple(rng.random() for _ in range(config.x_dimension))
            h0 = rng.choices(h0_labels, weights=h0_weights, k=1)[0]
            c_c = tuple(rng.random() < config.c_c_component_probability
                        for _ in range(config.c_c_dimension))
            baseline = D2Baseline(
                unit_id, history_ref,
                rng.random() < config.focal_accessible_pre_probability,
                rng.random() < config.c_auth_base_probability,
                rng.random() < config.c_resource_probability,
                rng.random() < config.c_capacity_probability,
                rng.random() < config.c_info_probability,
                rng.random() < config.c_domain_probability,
                rng.random() < config.c_other_probability,
            )
            d2_seed = rng.getrandbits(64)
            potentials = generate_d2_potentials(
                baseline, d2_config, exogenous_seed=d2_seed,
            )
            if focal_accessibility_specs_by_unit is not None:
                focal_spec = focal_accessibility_specs_by_unit[unit_id]
                if focal_spec.unit_id != unit_id:
                    raise ContractError("typed D2 focal specification key/unit identity mismatch")
                focal_truth = adjudicate_d2_focal_potentials(focal_spec)
                potentials = replace(potentials, focal_accessibility_truth=focal_truth)
            units.append(SyntheticWorldUnit(
                unit_id, x_ref, h0_ref, c_c_ref, x, h0, c_c,
                baseline, potentials,
            ))
            q_x.append(QXHistoryMass(
                history_ref, x_ref, h0_ref, c_c_ref,
                config.q_x_mass_by_unit[index],
            ))
        roster_payload = tuple({
            "unit_id": unit.unit_id, "x_ref": unit.x_ref, "h0_ref": unit.h0_ref,
            "c_c_ref": unit.c_c_ref, "x": unit.x, "h0": unit.h0,
            "c_c": unit.c_c,
            "d2_baseline": unit.d2_baseline,
            "d2_potentials": unit.d2_potentials,
        } for unit in units)
        result = SyntheticWorldBundle(
            config.world_id, config.world_version, config.dgp_id, config.dgp_version,
            config.roster_id, config.roster_version, digest(config),
            digest({"seed": config.seed}), digest(d2_config),
            tuple(units), tuple(q_x), digest(roster_payload),
        )
        result.validate()
        return result


    def generate_complete(
        self,
        config: SyntheticWorldConfig,
        d2_config: D2MechanismConfig,
        structural_config: D2StructuralGenerationConfig,
        focal_accessibility_specs_by_unit: dict[str, D2FocalAccessibilitySpecification] | None = None,
    ) -> tuple[SyntheticWorldBundle, dict[tuple[str, int], D2StructuralPotentialPair]]:
        """One-call materialization of roster, D2 potentials and structural truth."""
        world = self.generate(config, d2_config, focal_accessibility_specs_by_unit)
        structural_pairs = generate_d2_structural_potential_pairs(world, structural_config)
        return world, structural_pairs


    def generate_complete_with_reachability(
        self,
        config: SyntheticWorldConfig,
        d2_config: D2MechanismConfig,
        structural_config: D2StructuralGenerationConfig,
        reach_config: D2ReachGenerationConfig,
        focal_accessibility_specs_by_unit: dict[str, D2FocalAccessibilitySpecification] | None = None,
    ) -> tuple[
        SyntheticWorldBundle,
        dict[tuple[str, int], D2StructuralPotentialPair],
        SyntheticWorldReachabilityContrast,
    ]:
        """Materialize roster, D2/structural potentials and baseline/post Reach."""
        world, structural_pairs = self.generate_complete(
            config, d2_config, structural_config, focal_accessibility_specs_by_unit,
        )
        reach_contrast = evaluate_d2_structural_reachability(
            world, structural_pairs, reach_config,
        )
        return world, structural_pairs, reach_contrast



    def generate_complete_with_trajectories(
        self,
        config: SyntheticWorldConfig,
        d2_config: D2MechanismConfig,
        structural_config: D2StructuralGenerationConfig,
        reach_config: D2ReachGenerationConfig,
        trajectory_config: D2TrajectoryGenerationConfig,
        focal_accessibility_specs_by_unit: dict[str, D2FocalAccessibilitySpecification] | None = None,
    ) -> tuple[
        SyntheticWorldBundle,
        dict[tuple[str, int], D2StructuralPotentialPair],
        SyntheticWorldReachabilityContrast,
        SyntheticWorldTrajectoryBundle,
    ]:
        """Materialize the full path through potential route execution and trajectories."""
        world, structural_pairs, reach = self.generate_complete_with_reachability(
            config, d2_config, structural_config, reach_config,
            focal_accessibility_specs_by_unit,
        )
        trajectories = evaluate_d2_potential_trajectories(
            world, reach, reach_config, trajectory_config,
        )
        return world, structural_pairs, reach, trajectories



    def evaluate_complete_vcont_truth(
        self,
        world: SyntheticWorldBundle,
        histories_by_unit_z: dict[tuple[str, int], EventHistory],
        grid: IntervalGrid,
    ) -> D2VContTruthBundle:
        """Attach reserved B1 V_cont truth to an already materialized D2 world."""
        return evaluate_d2_vcont_potential_truth(world, histories_by_unit_z, grid)


@dataclass(frozen=True)
class JointPolicyHistory:
    history_ref: str
    distribution: tuple[tuple[Vector4, float], ...]


@dataclass(frozen=True)
class ThetaAPolicyAssignmentConfig:
    mechanism_id: str
    mechanism_version: str
    randomization_salt: str
    probability_a1_by_history: tuple[tuple[str, float], ...]

    def validate(
        self,
        world: "SyntheticWorldBundle",
        structural_support_contract: object | None = None,
    ) -> None:
        refs = {row.history_ref for row in world.q_x}
        supplied = [row[0] for row in self.probability_a1_by_history]
        if not all((self.mechanism_id, self.mechanism_version, self.randomization_salt)):
            raise ContractError("theta_A policy-assignment mechanism identity/version/salt required")
        if len(supplied) != len(set(supplied)) or set(supplied) != refs:
            raise ContractError("theta_A policy-assignment probabilities must cover source q_X histories exactly")
        probabilities = dict(self.probability_a1_by_history)
        boundary = tuple(sorted(
            history_ref for history_ref, probability in probabilities.items()
            if not math.isfinite(probability) or probability in (0.0, 1.0)
        ))
        if boundary and structural_support_contract is None:
            raise ContractError(
                "boundary theta_A assignment probabilities require an explicit structural-support contract"
            )
        if any(not math.isfinite(probability) or not 0.0 <= probability <= 1.0
               for probability in probabilities.values()):
            raise ContractError("theta_A assignment probabilities must lie in [0,1]")
        if structural_support_contract is not None:
            validate_contract = getattr(structural_support_contract, "validate", None)
            if not callable(validate_contract):
                raise ContractError("structural-support contract must expose its validator")
            validate_contract()
            if getattr(structural_support_contract, "source_q_x_sha256", None) != digest(world.q_x):
                raise ContractError("assignment structural-support contract does not bind source q_X")
            support_rows = {
                row.history_ref: row for row in getattr(structural_support_contract, "rows", ())
            }
            source_masses = {row.history_ref: row.mass for row in world.q_x}
            if not set(boundary).issubset(support_rows):
                raise ContractError(
                    "every boundary assignment propensity must be represented in the target structural-support contract"
                )
            for history_ref in refs.intersection(support_rows):
                support_row = support_rows[history_ref]
                if (not math.isclose(support_row.source_mass, source_masses[history_ref],
                                     rel_tol=0.0, abs_tol=1e-12)
                        or not math.isclose(support_row.assignment_probability_a1,
                                            probabilities[history_ref],
                                            rel_tol=0.0, abs_tol=1e-12)):
                    raise ContractError(
                        f"assignment mechanism differs from structural-support contract for {history_ref}"
                    )


@dataclass(frozen=True)
class ThetaAPolicyAssignment:
    unit_id: str
    history_ref: str
    assigned_arm: int
    probability_a0: float
    probability_a1: float
    assigned_vector: Vector4
    assigned_vector_sha256: str
    policy_fingerprint: str
    r_common_fingerprint: str


@dataclass(frozen=True)
class ThetaAPolicyAssignmentBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    mechanism_id: str
    mechanism_version: str
    mechanism_sha256: str
    randomization_salt_sha256: str
    q_x_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    assignments: tuple[ThetaAPolicyAssignment, ...]
    result_sha256: str

    def validate(
        self,
        world: "SyntheticWorldBundle",
        config: ThetaAPolicyAssignmentConfig,
        g_a0: Sequence["JointPolicyHistory"],
        g_a1: Sequence["JointPolicyHistory"],
        feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
        r_common_certificates: Sequence["RCommonPairCertificate"],
        structural_support_contract: object | None = None,
    ) -> None:
        world.validate()
        config.validate(world, structural_support_contract)
        refs = {row.history_ref for row in world.q_x}
        policy_maps = []
        for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
            mapping = {row.history_ref: row for row in rows}
            if len(mapping) != len(rows) or not refs.issubset(mapping):
                raise ContractError(f"{label} must cover every source q_X* history; target-only histories may also be declared")
            for history_ref, policy in mapping.items():
                _distribution_total(policy.distribution, f"{label} distribution for {history_ref}")
                feasible = {digest(vector) for vector in feasible_vectors_by_history.get(history_ref, ())}
                if not feasible or any(digest(vector) not in feasible for vector, _ in policy.distribution):
                    raise ContractError(f"{label} support is not jointly feasible for {history_ref}")
            policy_maps.append(mapping)
        certs = {row.history_ref: row for row in r_common_certificates}
        if len(certs) != len(r_common_certificates) or not refs.issubset(certs):
            raise ContractError("one r_common certificate is required per source q_X* history; target-only certificates may also be declared")
        for cert in certs.values():
            if (cert.status != "COMMON_FIXED" or not cert.regime_id or not cert.regime_version
                    or not cert.g_a0_fingerprint or cert.g_a0_fingerprint != cert.g_a1_fingerprint):
                raise ContractError("theta_A policy assignment requires fixed common r_common")
        if len({(row.regime_id, row.regime_version, row.g_a0_fingerprint)
                for row in certs.values()}) != 1:
            raise ContractError("r_common identity/version/fingerprint must be common across q_X*")
        units = {unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units}
        rows = {row.history_ref: row for row in self.assignments}
        if len(rows) != len(self.assignments) or set(rows) != refs:
            raise ContractError("theta_A policy assignments must cover every q_X* unit exactly")
        probabilities = dict(config.probability_a1_by_history)
        for history_ref, row in rows.items():
            arm = row.assigned_arm
            if arm not in (0, 1) or row.unit_id != units[history_ref]:
                raise ContractError("theta_A assignment arm or unit/history binding is invalid")
            p1 = probabilities[history_ref]
            if (row.probability_a0, row.probability_a1) != (1.0 - p1, p1):
                raise ContractError("theta_A assignment probabilities differ from declared mechanism")
            policy = policy_maps[arm][history_ref]
            if row.policy_fingerprint != digest(policy.distribution):
                raise ContractError("assigned policy fingerprint does not match declared g_A policy")
            if digest(row.assigned_vector) not in {digest(v) for v, _ in policy.distribution}:
                raise ContractError("assigned vector is outside the selected joint-policy support")
            cert = certs[history_ref]
            if row.r_common_fingerprint != cert.g_a0_fingerprint:
                raise ContractError("assigned policy does not bind to the common r_common regime")
            if row.assigned_vector_sha256 != digest(row.assigned_vector):
                raise ContractError("assigned joint vector fingerprint is invalid")
        payload = {
            "world_id": self.world_id, "world_version": self.world_version,
            "dgp_id": self.dgp_id, "dgp_version": self.dgp_version,
            "mechanism_id": self.mechanism_id, "mechanism_version": self.mechanism_version,
            "mechanism_sha256": self.mechanism_sha256,
            "randomization_salt_sha256": self.randomization_salt_sha256,
            "q_x_sha256": self.q_x_sha256, "g_a0_sha256": self.g_a0_sha256,
            "g_a1_sha256": self.g_a1_sha256, "r_common_sha256": self.r_common_sha256,
            "assignments": self.assignments,
        }
        if (self.world_id, self.world_version, self.dgp_id, self.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("theta_A assignment bundle world/DGP identity mismatch")
        if (self.mechanism_id, self.mechanism_version, self.mechanism_sha256,
                self.randomization_salt_sha256, self.q_x_sha256,
                self.g_a0_sha256, self.g_a1_sha256,
                self.r_common_sha256) != (
            config.mechanism_id, config.mechanism_version, digest(config),
            digest(config.randomization_salt), digest(world.q_x),
            digest(tuple(g_a0)), digest(tuple(g_a1)), digest(tuple(r_common_certificates))
        ):
            raise ContractError("theta_A assignment bundle provenance mismatch")
        if self.result_sha256 != digest(payload):
            raise ContractError("theta_A assignment bundle content fingerprint is invalid")


def generate_theta_a_policy_assignments(
    world: "SyntheticWorldBundle",
    config: ThetaAPolicyAssignmentConfig,
    g_a0: Sequence["JointPolicyHistory"],
    g_a1: Sequence["JointPolicyHistory"],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence["RCommonPairCertificate"],
    structural_support_contract: object | None = None,
) -> ThetaAPolicyAssignmentBundle:
    """Randomize the joint g_A intervention directly; never use Z or legacy G.

    Boundary assignment probabilities are available only for explicit synthetic
    non-identification fixtures carrying a source-bound structural-support contract.
    """
    world.validate()
    config.validate(world, structural_support_contract)
    refs = {row.history_ref for row in world.q_x}
    policy_maps = []
    for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in rows}
        if len(mapping) != len(rows) or not refs.issubset(mapping):
            raise ContractError(f"{label} must cover every source q_X* history; target-only histories may also be declared")
        for history_ref, policy in mapping.items():
            _distribution_total(policy.distribution, f"{label} distribution for {history_ref}")
            feasible = {digest(vector) for vector in feasible_vectors_by_history.get(history_ref, ())}
            if not feasible or any(digest(vector) not in feasible for vector, _ in policy.distribution):
                raise ContractError(f"{label} support is not jointly feasible for {history_ref}")
        policy_maps.append(mapping)
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or not refs.issubset(certs):
        raise ContractError("one r_common certificate is required per source q_X* history; target-only certificates may also be declared")
    if any(row.status != "COMMON_FIXED" or row.g_a0_fingerprint != row.g_a1_fingerprint
           for row in certs.values()):
        raise ContractError("theta_A assignment requires certified fixed common r_common")
    if len({(row.regime_id, row.regime_version, row.g_a0_fingerprint)
            for row in certs.values()}) != 1:
        raise ContractError("r_common identity/version/fingerprint must be common across q_X*")
    p_a1 = dict(config.probability_a1_by_history)
    assignments = []
    for unit, qx in zip(world.units, world.q_x):
        arm_draw = _dgp_uniform(
            world.seed_commitment_sha256, config.randomization_salt,
            unit.unit_id, "theta-a-policy-arm",
        )
        arm = 1 if arm_draw < p_a1[qx.history_ref] else 0
        policy = policy_maps[arm][qx.history_ref]
        vector_draw = _dgp_uniform(
            world.seed_commitment_sha256, config.randomization_salt,
            unit.unit_id, arm, "theta-a-joint-vector",
        )
        cumulative = 0.0
        vector = policy.distribution[-1][0]
        for candidate, probability in policy.distribution:
            cumulative += probability
            if vector_draw < cumulative:
                vector = candidate
                break
        cert = certs[qx.history_ref]
        assignments.append(ThetaAPolicyAssignment(
            unit.unit_id, qx.history_ref, arm, 1.0 - p_a1[qx.history_ref],
            p_a1[qx.history_ref], vector, digest(vector),
            digest(policy.distribution), cert.g_a0_fingerprint,
        ))
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "mechanism_id": config.mechanism_id, "mechanism_version": config.mechanism_version,
        "mechanism_sha256": digest(config),
        "randomization_salt_sha256": digest(config.randomization_salt),
        "q_x_sha256": digest(world.q_x), "g_a0_sha256": digest(tuple(g_a0)),
        "g_a1_sha256": digest(tuple(g_a1)),
        "r_common_sha256": digest(tuple(r_common_certificates)),
        "assignments": tuple(assignments),
    }
    result = ThetaAPolicyAssignmentBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        config.mechanism_id, config.mechanism_version, digest(config),
        digest(config.randomization_salt), digest(world.q_x),
        digest(tuple(g_a0)), digest(tuple(g_a1)),
        digest(tuple(r_common_certificates)), tuple(assignments), digest(payload),
    )
    result.validate(
        world, config, g_a0, g_a1, feasible_vectors_by_history,
        r_common_certificates, structural_support_contract,
    )
    return result



def theta_a_event_history_potential_id(assignment: "ThetaAPolicyAssignment") -> str:
    """Canonical link from a realized g_A assignment to its reserved EventHistory."""
    if assignment.assigned_arm not in (0, 1):
        raise ContractError("theta_A EventHistory link requires a valid assigned policy arm")
    # A functional potential is indexed by unit, assigned joint vector and
    # common regime. The randomized arm selects a policy distribution; it is
    # not itself a distinct functional potential when both policies support
    # the same vector. Keep this identity aligned with
    # generate_g_a_event_history_potentials().
    return (
        f"{assignment.unit_id}:G_A:"
        f"{assignment.assigned_vector_sha256}:{assignment.r_common_fingerprint}"
    )


@dataclass(frozen=True)
class ThetaAPolicyHistorySelection:
    run_id: str
    assignment_bundle_sha256: str
    selected_history_id_by_unit: tuple[tuple[str, str], ...]
    selected_history_manifest: tuple[tuple[str, str, str, str], ...]
    result_sha256: str


def select_theta_a_realized_histories(
    assignments: "ThetaAPolicyAssignmentBundle",
    histories: Sequence[EventHistory],
) -> ThetaAPolicyHistorySelection:
    """Select exactly the EventHistory implied by each direct joint g_A assignment."""
    if not histories:
        raise ContractError("theta_A realized-history selection requires EventHistory inputs")
    run_ids = {history.run_id for history in histories}
    if len(run_ids) != 1:
        raise ContractError("theta_A policy EventHistories must belong to one run")
    run_id = next(iter(run_ids))
    history_ids = [history.history_id for history in histories]
    if len(history_ids) != len(set(history_ids)):
        raise ContractError("theta_A policy EventHistory identities must be unique")
    index = {}
    for history in histories:
        history.validate(require_complete=True)
        if (history.world_id, history.world_version, history.dgp_version) != (
            assignments.world_id, assignments.world_version, assignments.dgp_version
        ):
            raise ContractError("theta_A EventHistory world/DGP identity differs from its assignment bundle")
        key = (history.unit_id, history.potential_id)
        if key in index:
            raise ContractError("duplicate EventHistory for the same unit and g_A potential")
        index[key] = history
    selected = []
    for assignment in assignments.assignments:
        potential_id = theta_a_event_history_potential_id(assignment)
        history = index.get((assignment.unit_id, potential_id))
        if history is None:
            raise ContractError("realized g_A assignment has no matching EventHistory potential")
        selected.append((assignment.unit_id, history))
    if len({history.history_id for _, history in selected}) != len(selected):
        raise ContractError("one EventHistory cannot be selected for multiple assigned units")
    selected_map = tuple((unit_id, history.history_id) for unit_id, history in selected)
    manifest = tuple(
        (unit_id, history.history_id, history.content_sha256, history.potential_id)
        for unit_id, history in selected
    )
    payload = {
        "run_id": run_id,
        "assignment_bundle_sha256": assignments.result_sha256,
        "selected_history_id_by_unit": selected_map,
        "selected_history_manifest": manifest,
    }
    return ThetaAPolicyHistorySelection(
        run_id, assignments.result_sha256, selected_map, manifest, digest(payload),
    )



@dataclass(frozen=True)
class RCommonPairCertificate:
    history_ref: str
    regime_id: str
    regime_version: str
    g_a0_fingerprint: str
    g_a1_fingerprint: str
    status: Literal["COMMON_FIXED", "DIFFERENTIAL_IDENTIFIED", "DIFFERENTIAL_UNRESOLVED"]


@dataclass(frozen=True)
class ThetaAContribution:
    history_ref: str
    q_x_mass: float
    mean_under_g_a0: float
    mean_under_g_a1: float
    contrast: float
    r_common_fingerprint: str


@dataclass(frozen=True)
class ThetaATruth:
    estimand_id: str
    estimand_version: str
    outcome_id: str
    outcome_version: str
    q_x_fingerprint: str
    g_a0_fingerprint: str
    g_a1_fingerprint: str
    contributions: tuple[ThetaAContribution, ...]
    theta_a_truth: float
    evaluator_only: bool = True


def compute_theta_a_truth(
    q_x: Sequence[QXHistoryMass],
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    outcome_function: Callable[[str, Vector4, str], float],
    *,
    estimand_version: str,
    outcome_version: str,
) -> ThetaATruth:
    """Compute DEC-C10-103 standardized joint-policy contrast.

    Masses and policies are explicit inputs, never inferred from assignment
    frequencies. This oracle is evaluator-side; it is not an Analyzer estimator.
    """
    if not q_x or not estimand_version or not outcome_version:
        raise ContractError("q_X* rows and estimand/outcome versions are required")
    refs = [row.history_ref for row in q_x]
    if len(refs) != len(set(refs)) or any(
        not row.history_ref or not row.x_ref or not row.h0_ref or not row.c_c_ref for row in q_x
    ):
        raise ContractError("q_X* requires unique history refs and explicit X/H0/C_c anchors")
    for row in q_x:
        if not math.isfinite(row.mass) or row.mass <= 0.0:
            raise ContractError("q_X* masses must be strictly positive")
    if abs(sum(row.mass for row in q_x) - 1.0) > 1e-12:
        raise ContractError("q_X* masses must sum to one")
    maps = []
    for rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in rows}
        if len(mapping) != len(rows) or set(mapping) != set(refs):
            raise ContractError(f"{label} must have exactly one joint policy row per q_X* history")
        for h, row in mapping.items():
            _distribution_total(row.distribution, f"{label} distribution for {h}")
            vector_keys = [digest(vector) for vector, _ in row.distribution]
            if len(vector_keys) != len(set(vector_keys)):
                raise ContractError(f"{label} has duplicate joint-vector support entries")
            if any(len(vector) != 4 for vector, _ in row.distribution):
                raise ContractError(f"{label} must act on the complete four-coordinate vector")
        maps.append(mapping)
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != set(refs):
        raise ContractError("one r_common certificate is required per positive-mass history")
    contributions = []
    for row in q_x:
        h = row.history_ref
        feasible = {digest(vector) for vector in feasible_vectors_by_history.get(h, ())}
        if not feasible:
            raise ContractError(f"joint structural support absent for history {h}")
        policy_rows = (maps[0][h], maps[1][h])
        for policy in policy_rows:
            if any(digest(vector) not in feasible for vector, _ in policy.distribution):
                raise ContractError(f"policy support exceeds structural feasibility for history {h}")
        certificate = certs[h]
        if certificate.status != "COMMON_FIXED":
            raise ContractError(f"r_common is not certified COMMON_FIXED for history {h}")
        if not certificate.regime_id or not certificate.regime_version:
            raise ContractError("r_common regime identity/version required")
        if any(
            (other.regime_id, other.regime_version) !=
            (certificate.regime_id, certificate.regime_version)
            for other in certs.values()
        ):
            raise ContractError("r_common regime identity/version must be common across q_X* histories")
        if not certificate.g_a0_fingerprint or certificate.g_a0_fingerprint != certificate.g_a1_fingerprint:
            raise ContractError(f"r_common differs between g_A worlds for history {h}")
        fingerprint = certificate.g_a0_fingerprint
        means = [
            sum(probability * float(outcome_function(h, vector, fingerprint))
                for vector, probability in policy.distribution)
            for policy in policy_rows
        ]
        if any(not math.isfinite(x) or not 0.0 <= x <= 1.0 for x in means):
            raise ContractError("V_cont outcome function must return values in [0,1]")
        contributions.append(ThetaAContribution(
            h, row.mass, means[0], means[1], means[1] - means[0], fingerprint,
        ))
    theta = sum(row.q_x_mass * row.contrast for row in contributions)
    return ThetaATruth(
        "THETA_A_QX_GA_RCOMMON_VCONT", estimand_version, "V_CONT",
        outcome_version, digest(tuple(q_x)), digest(tuple(g_a0)),
        digest(tuple(g_a1)), tuple(contributions), theta,
    )


@dataclass(frozen=True)
class ThetaAVContTruthBundle:
    world_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    theta_a_truth: ThetaATruth
    grid_id: str
    grid_version: str
    event_history_manifest: tuple[tuple[str, str, str, str, str], ...]
    result_sha256: str

    def validate(self) -> None:
        if not all((self.world_id, self.world_version, self.dgp_id, self.dgp_version)):
            raise ContractError("theta_A V_cont world/DGP identity is mandatory")
        if not self.theta_a_truth.evaluator_only or self.theta_a_truth.outcome_id != "V_CONT":
            raise ContractError("theta_A V_cont truth must remain evaluator-only and outcome-specific")
        if not self.grid_id or not self.grid_version or not self.event_history_manifest:
            raise ContractError("theta_A V_cont truth requires grid and EventHistory provenance")
        if len({row[3] for row in self.event_history_manifest}) != len(self.event_history_manifest):
            raise ContractError("theta_A V_cont EventHistory manifest IDs must be unique")
        payload = {
            "world_id": self.world_id, "world_version": self.world_version,
            "dgp_id": self.dgp_id, "dgp_version": self.dgp_version,
            "theta_a_truth": self.theta_a_truth,
            "grid_id": self.grid_id, "grid_version": self.grid_version,
            "event_history_manifest": self.event_history_manifest,
        }
        if self.result_sha256 != digest(payload):
            raise ContractError("theta_A V_cont content fingerprint is invalid")


def compute_theta_a_vcont_truth_from_event_histories(
    world: "SyntheticWorldBundle",
    q_x: Sequence[QXHistoryMass],
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    event_histories_by_policy: dict[tuple[str, str, str], EventHistory],
    grid: IntervalGrid,
    *,
    estimand_version: str,
    outcome_version: str,
    unit_id_by_history: dict[str, str] | None = None,
) -> ThetaAVContTruthBundle:
    """Compute evaluator-only theta_A truth using reserved EventHistory V_cont outcomes.

    Each history is keyed explicitly by (q_X history ref, digest(joint policy
    vector), common-r regime fingerprint). No outcome is inferred from D2 Z,
    structural Reach, selection, execution or the trajectory.
    """
    world.validate()
    grid.validate()
    qx_by_history = {row.history_ref: row for row in q_x}
    unit_by_history = unit_id_by_history or {
        unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
    }
    if (not qx_by_history or len(qx_by_history) != len(q_x)
            or set(qx_by_history) != set(unit_by_history)
            or any(not unit_id for unit_id in unit_by_history.values())
            or len(set(unit_by_history.values())) != len(unit_by_history)):
        raise ContractError("theta_A target q_X* and reserved potential-unit identities must cover exactly the same histories")
    certificates = {row.history_ref: row for row in r_common_certificates}
    if len(certificates) != len(r_common_certificates) or set(certificates) != set(qx_by_history):
        raise ContractError("theta_A requires one r_common certificate per world q_X* history")
    required_keys = set()
    for policies in (g_a0, g_a1):
        for policy in policies:
            certificate = certificates.get(policy.history_ref)
            if certificate is None:
                raise ContractError("joint policy has no matching r_common certificate")
            if certificate.g_a0_fingerprint != certificate.g_a1_fingerprint:
                raise ContractError("theta_A V_cont EventHistory adapter requires fixed common r_common")
            for vector, _ in policy.distribution:
                required_keys.add((
                    policy.history_ref, digest(vector), certificate.g_a0_fingerprint,
                ))
    if set(event_histories_by_policy) != required_keys:
        raise ContractError("EventHistory inputs must cover exact q_X × joint-policy support under r_common")
    histories = tuple(event_histories_by_policy[key] for key in sorted(required_keys))
    history_ids = [history.history_id for history in histories]
    potential_ids = [history.potential_id for history in histories]
    run_ids = {history.run_id for history in histories}
    if (len(history_ids) != len(set(history_ids))
            or len(potential_ids) != len(set(potential_ids)) or len(run_ids) != 1):
        raise ContractError("theta_A EventHistory identities/potentials must be unique and belong to one run")
    values = {}
    manifest = []
    for key in sorted(required_keys):
        history_ref, vector_sha, regime_fingerprint = key
        history = event_histories_by_policy[key]
        history.validate(require_complete=True)
        if (history.world_id, history.world_version, history.dgp_version, history.unit_id) != (
            world.world_id, world.world_version, world.dgp_version, unit_by_history[history_ref]
        ):
            raise ContractError("theta_A EventHistory does not bind to its exact world/q_X unit")
        if history.support_start != grid.boundaries[0] or history.support_end != grid.boundaries[-1]:
            raise ContractError("theta_A EventHistories must share the exact common V_cont grid support")
        adjudication = adjudicate_intervals(history, grid)
        values[key] = adjudication.v_cont_truth
        manifest.append((
            history_ref, vector_sha, regime_fingerprint,
            history.history_id, history.content_sha256,
        ))

    def vcont_outcome(history_ref: str, vector: Vector4, regime_fingerprint: str) -> float:
        key = (history_ref, digest(vector), regime_fingerprint)
        if key not in values:
            raise ContractError("theta_A outcome requested outside the sealed EventHistory policy support")
        return values[key]

    theta_truth = compute_theta_a_truth(
        q_x, g_a0, g_a1, feasible_vectors_by_history,
        r_common_certificates, vcont_outcome,
        estimand_version=estimand_version, outcome_version=outcome_version,
    )
    manifest_tuple = tuple(manifest)
    payload = {
        "world_id": world.world_id, "world_version": world.world_version,
        "dgp_id": world.dgp_id, "dgp_version": world.dgp_version,
        "theta_a_truth": theta_truth,
        "grid_id": grid.grid_id, "grid_version": grid.grid_version,
        "event_history_manifest": manifest_tuple,
    }
    result = ThetaAVContTruthBundle(
        world.world_id, world.world_version, world.dgp_id, world.dgp_version,
        theta_truth, grid.grid_id, grid.grid_version,
        manifest_tuple, digest(payload),
    )
    result.validate()
    return result



# S3: passive projection via an explicit joint emission kernel.

@dataclass(frozen=True)
class S3SequenceKernelRow:
    # ENABLED, admission behaviour and declared PROFILE at each scheduled time.
    # PROFILE is configuration state; no PROFILE-exposure signal is modelled.
    truth_sequence: tuple[tuple[bool, AdmissionBehavior, ProfileValue], ...]
    observed_sequences: tuple[
        tuple[tuple[tuple[bool | None, AdmissionBehavior | None, ProfileValue | None], ...], float], ...
    ]


@dataclass(frozen=True)
class S3ObservationConfig:
    schedule: tuple[Decimal, ...]
    capture_lags: tuple[Decimal, ...]
    ingestion_lags: tuple[Decimal, ...]
    kernel: tuple[S3SequenceKernelRow, ...]
    config_id: str
    config_version: str

    def validate(self, history: EventHistory) -> None:
        if not self.config_id or not self.config_version:
            raise ContractError("S3 configuration identity/version required")
        if len(self.capture_lags) != len(self.schedule) or len(self.ingestion_lags) != len(self.schedule):
            raise ContractError("one explicit capture and ingestion lag is required per scheduled observation")
        if any(not isinstance(value, Decimal) for value in self.schedule + self.capture_lags + self.ingestion_lags):
            raise ContractError("S3 schedule and lags must use exact Decimal coordinates")
        if any(lag < 0 for lag in self.capture_lags + self.ingestion_lags):
            raise ContractError("S3 capture/ingestion lags cannot be negative")
        if not self.schedule or any(
            t < history.support_start or t > history.support_end for t in self.schedule
        ):
            raise ContractError("S3 schedule must be explicit and lie within truth support")
        if any(a >= b for a, b in zip(self.schedule, self.schedule[1:])):
            raise ContractError("S3 schedule must be strictly increasing")
        keys = [row.truth_sequence for row in self.kernel]
        if len(keys) != len(set(keys)):
            raise ContractError("S3 sequence kernel has duplicate latent paths")
        for row in self.kernel:
            if len(row.truth_sequence) != len(self.schedule):
                raise ContractError("S3 kernel latent path must cover the complete schedule")
            _distribution_total(row.observed_sequences, "S3 joint sequence emission kernel")
            if any(
                type(enabled) is not bool
                or behavior not in ("ADMIT", "NO_ADMISSION")
                or profile not in ("STANDARD", "READ_ONLY", "DISABLED")
                for enabled, behavior, profile in row.truth_sequence
            ):
                raise ContractError("invalid latent S3 ENABLED/admission/PROFILE sequence")
            for observed, _ in row.observed_sequences:
                if len(observed) != len(self.schedule):
                    raise ContractError("S3 emitted sequence must match the declared schedule")
                if any(
                    (enabled is not None and type(enabled) is not bool)
                    or behavior not in (None, "ADMIT", "NO_ADMISSION")
                    or profile not in (None, "STANDARD", "READ_ONLY", "DISABLED")
                    for enabled, behavior, profile in observed
                ):
                    raise ContractError("invalid S3 observed sequence emission")


@dataclass(frozen=True)
class S3Observation:
    observation_id: str
    unit_id: str
    history_ref: str
    observation_time: Decimal
    capture_time: Decimal
    ingestion_time: Decimal
    enabled_observed: bool | None
    admission_behavior_observed: AdmissionBehavior | None
    profile_value_observed: ProfileValue | None
    enabled_status: Literal["OBSERVED", "MISSING"]
    admission_status: Literal["OBSERVED", "MISSING"]
    profile_status: Literal["OBSERVED", "MISSING"]
    profile_config_id: str
    profile_config_version: str
    config_id: str
    config_version: str


def _state_at(history: EventHistory, at: Decimal) -> FunctionalState:
    state = history.initial_post_z_state
    for event in history.transitions:
        if event.event_time <= at:
            state = event.state_after
        else:
            break
    return state


def project_s3(history: EventHistory, config: S3ObservationConfig, *, seed: int) -> tuple[S3Observation, ...]:
    """Project one complete truth path through a joint passive S3 kernel.

    The joint kernel samples the observation sequence as one object, preserving
    arbitrary cross-signal and temporal dependence. Truth is never mutated.
    """
    history.validate(require_complete=True)
    config.validate(history)
    truth_sequence = tuple(
        (state.enabled, state.admission_behavior, state.profile)
        for state in (_state_at(history, at) for at in config.schedule)
    )
    kernel = {row.truth_sequence: row.observed_sequences for row in config.kernel}
    outcomes = kernel.get(truth_sequence)
    if outcomes is None:
        raise ContractError("S3 joint kernel does not cover the generated truth sequence")
    rng = random.Random(seed)
    u = rng.random()
    cumulative = 0.0
    selected = outcomes[-1][0]
    for observed_sequence, probability in outcomes:
        cumulative += probability
        if u < cumulative:
            selected = observed_sequence
            break
    observations = []
    for index, (at, observed) in enumerate(zip(config.schedule, selected)):
        enabled, behavior, _kernel_profile = observed
        state_at_observation = _state_at(history, at)
        # PROFILE is a declared, versioned configuration invariant, not a
        # stochastic exposure measurement. Its observed projection therefore
        # comes from the state/configuration even when the joint kernel marks
        # ENABLED and admission as missing.
        profile = state_at_observation.profile
        capture_time = at + config.capture_lags[index]
        ingestion_time = capture_time + config.ingestion_lags[index]
        observations.append(S3Observation(
            f"S3-{history.history_id}-{index:06d}", history.unit_id,
            history.history_id, at, capture_time, ingestion_time,
            enabled, behavior, profile,
            "MISSING" if enabled is None else "OBSERVED",
            "MISSING" if behavior is None else "OBSERVED",
            "MISSING" if profile is None else "OBSERVED",
            state_at_observation.profile_config_id, state_at_observation.profile_config_version,
            config.config_id, config.config_version,
        ))
    return tuple(observations)


@dataclass(frozen=True)
class ThetaAS3ObservationRecord:
    """Analyzer-candidate row: realized g_A assignment joined to passive S3 only."""
    run_id: str
    unit_id: str
    history_ref: str
    assignment_bundle_sha256: str
    q_x_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    assigned_arm: int
    assignment_probability: float
    assigned_vector_sha256: str
    policy_fingerprint: str
    r_common_fingerprint: str
    history_id: str
    observation_id: str
    observation_time: Decimal
    capture_time: Decimal
    ingestion_time: Decimal
    enabled_observed: bool | None
    admission_behavior_observed: AdmissionBehavior | None
    profile_value_observed: ProfileValue | None
    enabled_status: Literal["OBSERVED", "MISSING"]
    admission_status: Literal["OBSERVED", "MISSING"]
    profile_status: Literal["OBSERVED", "MISSING"]
    profile_config_id: str
    profile_config_version: str
    s3_config_id: str
    s3_config_version: str
    temporal_resolution: Literal["POINT_SAMPLE"] = "POINT_SAMPLE"


def compose_theta_a_s3_observation_records(
    assignments: "ThetaAPolicyAssignmentBundle",
    selection: "ThetaAPolicyHistorySelection",
    histories: Sequence[EventHistory],
    configs_by_history_ref: dict[str, S3ObservationConfig],
    seeds_by_unit: dict[str, int],
) -> tuple[ThetaAS3ObservationRecord, ...]:
    """Join direct g_A assignment -> selected realized EventHistory -> S3 observations.

    This is an observation-only projection. It deliberately does not export
    potential outcomes, latent truth states between sample times, q_X masses,
    policy distributions, or the reserved theta_A oracle.
    """
    if selection.assignment_bundle_sha256 != assignments.result_sha256:
        raise ContractError("theta_A history selection does not bind to this assignment bundle")
    if len(selection.selected_history_manifest) != len(assignments.assignments):
        raise ContractError("theta_A selected-history manifest must cover assignments exactly")
    history_by_id = {history.history_id: history for history in histories}
    if len(history_by_id) != len(histories):
        raise ContractError("duplicate EventHistory IDs in theta_A S3 composition")
    selected = {unit_id: (history_id, content_sha, potential_id)
                for unit_id, history_id, content_sha, potential_id
                in selection.selected_history_manifest}
    if len(selected) != len(selection.selected_history_manifest):
        raise ContractError("duplicate units in theta_A selected-history manifest")
    assignment_units = {row.unit_id for row in assignments.assignments}
    if set(selected) != assignment_units or set(seeds_by_unit) != assignment_units:
        raise ContractError("theta_A S3 composition requires exact assignment/selection/seed unit coverage")
    records = []
    for assignment in assignments.assignments:
        history_id, content_sha, potential_id = selected[assignment.unit_id]
        history = history_by_id.get(history_id)
        if history is None:
            raise ContractError("selected theta_A EventHistory is absent from supplied histories")
        if (history.unit_id != assignment.unit_id
                or history.potential_id != potential_id
                or history.content_sha256 != content_sha
                or history.world_id != assignments.world_id
                or history.world_version != assignments.world_version
                or history.dgp_version != assignments.dgp_version):
            raise ContractError("selected theta_A EventHistory does not match assignment identity/provenance")
        config = configs_by_history_ref.get(assignment.history_ref)
        if config is None:
            raise ContractError("missing S3 configuration for theta_A baseline history")
        observations = project_s3(history, config, seed=seeds_by_unit[assignment.unit_id])
        for obs in observations:
            records.append(ThetaAS3ObservationRecord(
                history.run_id, assignment.unit_id, assignment.history_ref,
                assignments.result_sha256, assignments.q_x_sha256,
                assignments.g_a0_sha256, assignments.g_a1_sha256,
                assignments.r_common_sha256, assignment.assigned_arm,
                assignment.probability_a1 if assignment.assigned_arm == 1 else assignment.probability_a0,
                assignment.assigned_vector_sha256,
                assignment.policy_fingerprint, assignment.r_common_fingerprint,
                history.history_id, obs.observation_id, obs.observation_time,
                obs.capture_time, obs.ingestion_time, obs.enabled_observed,
                obs.admission_behavior_observed, obs.profile_value_observed,
                obs.enabled_status, obs.admission_status, obs.profile_status,
                obs.profile_config_id, obs.profile_config_version,
                obs.config_id, obs.config_version,
            ))
    observation_ids = [row.observation_id for row in records]
    if len(observation_ids) != len(set(observation_ids)):
        raise ContractError("theta_A S3 observation IDs must be unique")
    return tuple(records)


@dataclass(frozen=True)
class ThetaAEvaluation:
    estimand_id: str
    truth: float
    estimate: float | None
    identification_status: Literal["IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"]
    absolute_error: float | None
    recovered_within_tolerance: bool | None
    abstention_respected: bool
    tolerance: float


def evaluate_theta_a_output(
    truth: ThetaATruth,
    *,
    identification_status: Literal["IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"],
    estimate: float | None,
    tolerance: float,
) -> ThetaAEvaluation:
    """Evaluator-side score after Analyzer output has been sealed."""
    if (not truth.evaluator_only or tolerance < 0.0 or not math.isfinite(tolerance)
            or identification_status not in ("IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE")):
        raise ContractError("invalid theta_A truth role, identification status or evaluation tolerance")
    if identification_status == "IDENTIFIED":
        if estimate is None or not math.isfinite(estimate):
            raise ContractError("identified theta_A output requires a finite estimate")
        error = abs(estimate - truth.theta_a_truth)
        return ThetaAEvaluation(
            truth.estimand_id, truth.theta_a_truth, estimate,
            identification_status, error, error <= tolerance, True, tolerance,
        )
    if estimate is not None:
        raise ContractError("non-identified theta_A output must abstain from a point estimate")
    return ThetaAEvaluation(
        truth.estimand_id, truth.theta_a_truth, None,
        identification_status, None, None, True, tolerance,
    )


@dataclass(frozen=True)
class ThetaAInputs:
    q_x: tuple[QXHistoryMass, ...]
    g_a0: tuple[JointPolicyHistory, ...]
    g_a1: tuple[JointPolicyHistory, ...]
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]]
    r_common_certificates: tuple[RCommonPairCertificate, ...]
    outcome_function: Callable[[str, Vector4, str], float]
    estimand_version: str
    outcome_version: str


@dataclass(frozen=True)
class C10STruthExtension:
    """Truth-side extension kept outside the Analyzer evidence object."""
    run_id: str
    d2_potential_bundles: tuple[D2PotentialBundle, ...]
    event_histories: tuple[EventHistory, ...]
    interval_adjudications: tuple[IntervalAdjudication, ...]
    theta_a_truth: ThetaATruth | None

    def validate(self) -> None:
        if not self.run_id:
            raise ContractError("extension run identity is required")
        unit_ids = [bundle.unit_id for bundle in self.d2_potential_bundles]
        if len(unit_ids) != len(set(unit_ids)):
            raise ContractError("D2 truth extension contains duplicate units")
        for bundle in self.d2_potential_bundles:
            bundle.validate()
        history_ids = [history.history_id for history in self.event_histories]
        if len(history_ids) != len(set(history_ids)):
            raise ContractError("truth extension contains duplicate EventHistory identities")
        for history in self.event_histories:
            if history.run_id != self.run_id:
                raise ContractError("EventHistory run identity differs from extension")
            history.validate(require_complete=True)
        adjudicated_ids = [x.history_id for x in self.interval_adjudications]
        if len(adjudicated_ids) != len(set(adjudicated_ids)) or set(adjudicated_ids) != set(history_ids):
            raise ContractError("every EventHistory must have exactly one interval adjudication")
        history_by_id = {history.history_id: history for history in self.event_histories}
        for adjudication in self.interval_adjudications:
            history = history_by_id[adjudication.history_id]
            if (adjudication.history_version != history.history_version
                    or adjudication.rules_version != history.adjudication_rules_version
                    or adjudication.history_sha256 != history.content_sha256):
                raise ContractError("IntervalAdjudication does not bind to the exact EventHistory version/content")
        if self.theta_a_truth is not None and not self.theta_a_truth.evaluator_only:
            raise ContractError("theta_A truth must remain evaluator-only")


@dataclass(frozen=True)
class C10SGenerationEnvelope:
    """End-to-end generation envelope with separate evidence and reserved truth."""
    run_manifest: object
    base_truth_bundle: object
    evidence_candidate: object
    s3_observations: tuple[S3Observation, ...]
    truth_extension: C10STruthExtension


def compose_existing_generation(
    base_generator,
    scenario_config,
    d2_baselines: Sequence[D2Baseline],
    d2_config: D2MechanismConfig,
    d2_seed_by_unit: dict[str, int],
    event_history_factory: Callable[[object, Sequence[D2PotentialBundle]], Sequence[EventHistory]],
    grid_factory: Callable[[Sequence[EventHistory]], dict[str, IntervalGrid]],
    *,
    selected_history_id_by_unit: dict[str, str],
    s3_configs_by_history: dict[str, S3ObservationConfig],
    s3_seeds_by_history: dict[str, int],
    theta_a_inputs: ThetaAInputs | None = None,
) -> C10SGenerationEnvelope:
    """Compose new D2/EventHistory truth with the existing V_cont Generator.

    No parameters are inferred from Z/G frequencies. D2 seeds, all potential
    histories, the realized-history selector, grids, S3 configurations and S3
    seeds are explicit caller-supplied DGP rules. No clock or grid is inferred.
    """
    manifest, base_truth, evidence = base_generator.generate(scenario_config)
    baseline_ids = [row.unit_id for row in d2_baselines]
    if len(baseline_ids) != len(set(baseline_ids)) or not baseline_ids:
        raise ContractError("D2 baseline roster must be nonempty and uniquely keyed")
    if set(d2_seed_by_unit) != set(baseline_ids):
        raise ContractError("one explicit D2 exogenous seed is required per baseline unit")
    d2_config.validate()
    d2_bundles = tuple(
        generate_d2_potentials(row, d2_config, exogenous_seed=d2_seed_by_unit[row.unit_id])
        for row in d2_baselines
    )
    histories = tuple(event_history_factory(manifest, d2_bundles))
    if not histories or any(h.run_id != manifest.run_id for h in histories):
        raise ContractError("complete EventHistory factory output must bind to the generated run")
    if len({h.history_id for h in histories}) != len(histories):
        raise ContractError("EventHistory identities must be unique within the run")
    if {h.unit_id for h in histories} != set(baseline_ids):
        raise ContractError("D2 baseline roster and EventHistory unit roster must match exactly")
    grids_by_history = grid_factory(histories)
    if set(grids_by_history) != {h.history_id for h in histories}:
        raise ContractError("grid factory must return one explicit temporal grid per EventHistory")
    adjudications = tuple(
        adjudicate_intervals(history, grids_by_history[history.history_id])
        for history in histories
    )
    theta_truth = None
    if theta_a_inputs is not None:
        theta_truth = compute_theta_a_truth(
            theta_a_inputs.q_x, theta_a_inputs.g_a0, theta_a_inputs.g_a1,
            theta_a_inputs.feasible_vectors_by_history,
            theta_a_inputs.r_common_certificates, theta_a_inputs.outcome_function,
            estimand_version=theta_a_inputs.estimand_version,
            outcome_version=theta_a_inputs.outcome_version,
        )
    extension = C10STruthExtension(
        manifest.run_id, d2_bundles, histories, adjudications, theta_truth,
    )
    extension.validate()

    # Select exactly one realized-assignment history per evidence unit. The
    # selection is explicit; it is never inferred from IDs or row ordering.
    if set(selected_history_id_by_unit) != set(baseline_ids):
        raise ContractError("realized-history selector must cover the D2 unit roster exactly")
    histories_by_id = {history.history_id: history for history in histories}
    if len(selected_history_id_by_unit.values()) != len(set(selected_history_id_by_unit.values())):
        raise ContractError("a realized EventHistory cannot be selected for multiple units")
    selected_histories = []
    for unit_id, history_id in selected_history_id_by_unit.items():
        history = histories_by_id.get(history_id)
        if history is None or history.unit_id != unit_id:
            raise ContractError("selected EventHistory identity/unit binding is invalid")
        selected_histories.append(history)
    selected_ids = {history.history_id for history in selected_histories}
    if set(s3_configs_by_history) != selected_ids or set(s3_seeds_by_history) != selected_ids:
        raise ContractError("S3 configs and seeds must cover the realized EventHistory roster exactly")
    s3_observations = project_s3_batch(
        tuple(selected_histories), s3_configs_by_history, s3_seeds_by_history,
    )
    projected_evidence = project_s3_into_evidence_candidate(
        evidence, tuple(selected_histories), s3_observations,
    )
    return C10SGenerationEnvelope(
        manifest, base_truth, projected_evidence, s3_observations, extension,
    )


def project_s3_batch(
    event_histories: Sequence[EventHistory],
    configs_by_history: dict[str, S3ObservationConfig],
    seeds_by_history: dict[str, int],
) -> tuple[S3Observation, ...]:
    """Create a separate observation-only projection for each truth history."""
    history_ids = {history.history_id for history in event_histories}
    if not history_ids or set(configs_by_history) != history_ids or set(seeds_by_history) != history_ids:
        raise ContractError("S3 config and seed maps must cover every supplied EventHistory exactly")
    rows = []
    for history in event_histories:
        rows.extend(project_s3(
            history, configs_by_history[history.history_id],
            seed=seeds_by_history[history.history_id],
        ))
    observation_ids = [row.observation_id for row in rows]
    if len(observation_ids) != len(set(observation_ids)):
        raise ContractError("S3 observation IDs must be unique")
    return tuple(rows)



def project_s3_into_evidence_candidate(candidate, selected_histories, observations):
    """Bind realized EventHistory/S3 observations to the sealed evidence schema.

    Only observations and public configuration identity are projected. Truth,
    potential histories, adjudications, seeds and DGP parameters stay reserved.
    PROFILE is carried as declarative configuration; exposure is not modelled.
    """
    if not getattr(candidate, "run_id", None) or not getattr(candidate, "rows", None):
        raise ContractError("identified nonempty EvidenceCandidate is required")
    histories_by_unit, history_ids = {}, set()
    for history in selected_histories:
        history.validate(require_complete=True)
        if history.run_id != candidate.run_id:
            raise ContractError("selected EventHistory run differs from EvidenceCandidate")
        if history.unit_id in histories_by_unit or history.history_id in history_ids:
            raise ContractError("one realized EventHistory per unit is required")
        histories_by_unit[history.unit_id] = history
        history_ids.add(history.history_id)
    rows = tuple(candidate.rows)
    unit_ids = [row.get("unit_id") if isinstance(row, dict) else None for row in rows]
    if any(not unit_id for unit_id in unit_ids) or len(unit_ids) != len(set(unit_ids)):
        raise ContractError("candidate rows require unique explicit unit_id values")
    if set(unit_ids) != set(histories_by_unit):
        raise ContractError("selected EventHistory roster must exactly match candidate units")
    by_history, observation_ids = {}, set()
    for item in observations:
        if item.observation_id in observation_ids:
            raise ContractError("S3 observation IDs must be unique")
        observation_ids.add(item.observation_id)
        by_history.setdefault(item.history_ref, []).append(item)
    if set(by_history) != history_ids:
        raise ContractError("S3 observations must cover every selected EventHistory exactly")
    projected_rows = []
    for row in rows:
        history = histories_by_unit[row["unit_id"]]
        projected = by_history[history.history_id]
        if not projected or any(x.unit_id != history.unit_id or x.history_ref != history.history_id for x in projected):
            raise ContractError("S3 observation unit/history binding mismatch")
        if tuple(sorted(projected, key=lambda x: x.observation_time)) != tuple(projected):
            raise ContractError("S3 observations must preserve temporal order")
        if any(
            x.profile_config_id != _state_at(history, x.observation_time).profile_config_id
            or x.profile_config_version != _state_at(history, x.observation_time).profile_config_version
            or x.capture_time < x.observation_time
            or x.ingestion_time < x.capture_time
            or x.enabled_status != ("MISSING" if x.enabled_observed is None else "OBSERVED")
            or x.admission_status != ("MISSING" if x.admission_behavior_observed is None else "OBSERVED")
            or x.profile_status != ("MISSING" if x.profile_value_observed is None else "OBSERVED")
            for x in projected
        ):
            raise ContractError("S3 status, PROFILE binding or chronology is inconsistent")
        if len({(x.config_id, x.config_version) for x in projected}) != 1:
            raise ContractError("one S3 observation configuration identity/version is required per history")
        if len(projected) != len(row.get("s3_enabled", ())):
            raise ContractError("S3 observation count must match Analyzer evidence cardinality")
        updated = dict(row)
        updated["s3_enabled"] = [None if x.enabled_observed is None else int(x.enabled_observed) for x in projected]
        updated["s3_admission_behavior"] = [x.admission_behavior_observed for x in projected]
        updated["s3_profile_value"] = [x.profile_value_observed for x in projected]
        updated["s3_enabled_status"] = [x.enabled_status for x in projected]
        updated["s3_admission_status"] = [x.admission_status for x in projected]
        updated["s3_profile_status"] = [x.profile_status for x in projected]
        updated["s3_temporal_support"] = ["POINT_SAMPLE"] * len(projected)
        updated["s3_profile_config_id"] = [x.profile_config_id for x in projected]
        updated["s3_profile_config_version"] = [x.profile_config_version for x in projected]
        projected_rows.append(updated)
    return replace(candidate, rows=tuple(projected_rows))
