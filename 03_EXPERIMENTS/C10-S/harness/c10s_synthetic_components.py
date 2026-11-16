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

AdmissionBehavior = Literal["ADMIT", "NO_ADMISSION"]
ProfileValue = Literal["STANDARD", "READ_ONLY", "DISABLED"]
TriState = Literal[1, 0]


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

    def validate(self) -> None:
        if tuple(x.z for x in self.potentials_by_z) != (0, 1):
            raise ContractError("D2 potential bundle must preserve separate Z=0 and Z=1 worlds")
        if any(x.unit_id != self.unit_id for x in self.potentials_by_z):
            raise ContractError("D2 potential unit identity mismatch")
        for p in self.potentials_by_z:
            if p.c_dep_star != all((p.c_install, p.c_integrity, p.c_compat, p.c_oper)):
                raise ContractError("C_dep* must be the conjunction of its four technical predicates")
            if p.a_f_post and not p.c_dep_star:
                raise ContractError("A_f* cannot be true when C_dep* is false")


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


@dataclass(frozen=True)
class JointPolicyHistory:
    history_ref: str
    distribution: tuple[tuple[Vector4, float], ...]


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
        enabled, behavior, profile = observed
        state_at_observation = _state_at(history, at)
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
    """Composes the existing integrated Generator with the additive truth extension.

    The legacy evidence candidate remains unchanged. Truth-side objects are
    returned separately and must never be passed to Sealer or Analyzer.
    """
    run_manifest: object
    base_truth_bundle: object
    evidence_candidate: object
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
    theta_a_inputs: ThetaAInputs | None = None,
) -> C10SGenerationEnvelope:
    """Compose new D2/EventHistory truth with the existing V_cont Generator.

    No parameters are inferred from Z/G frequencies. Every D2 unit seed,
    EventHistory and grid factories are explicit caller-supplied DGP rules;
    no clock, event-time schedule or grid is selected here.
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
    return C10SGenerationEnvelope(manifest, base_truth, evidence, extension)


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
