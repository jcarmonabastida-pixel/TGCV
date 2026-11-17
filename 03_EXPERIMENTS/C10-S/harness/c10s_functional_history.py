"""Explicit functional DGP bridge from D2/g_A/trajectory mechanisms to EventHistory.

No accessibility-to-admission equivalence is built in. Every state transition
requires a versioned rule authored in FunctionalHistoryDGPConfig.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, Sequence

from c10s_synthetic_components import (
    ContractError, D2PotentialStage, EventHistory, EventHistoryGenerationSpec,
    FunctionalState, FunctionalStateChange, JointPolicyHistory, RCommonPairCertificate,
    SyntheticWorldBundle, Vector4, D2PotentialTrajectory, digest, generate_event_history,
)

Source = Literal["D2", "G_A", "G_M", "TRAJECTORY"]
D2_FIELDS = {
    "w_programmed", "w_attempt", "receipt", "s_install",
    "c_dep_star", "a_f_post", "d_f_opening",
}


@dataclass(frozen=True)
class FunctionalHistoryRule:
    """One explicit DGP rule with a D2-stage or joint-vector predicate."""
    rule_id: str
    source: Source
    event_time: Decimal
    causal_family: str
    provenance_ref: str
    set_enabled: bool | None = None
    set_admission: Literal["ADMIT", "NO_ADMISSION"] | None = None
    d2_field: str | None = None
    d2_value: bool | None = None
    vector_index: int | None = None
    vector_value: object | None = None
    # Conjunctive joint-vector predicates permit explicit interaction rules.
    # The legacy single-component pair remains supported unchanged.
    vector_predicates: tuple[tuple[int, object], ...] | None = None
    factor_m_value: bool | None = None
    trajectory_target_state: str | None = None
    trajectory_field: Literal["trajectory_status", "execution_state"] | None = None
    trajectory_value: object | None = None
    suborder: int | None = None

    def validate(self) -> None:
        if not all((self.rule_id, self.causal_family, self.provenance_ref)):
            raise ContractError("functional rule identity and causal provenance are mandatory")
        if not isinstance(self.event_time, Decimal):
            raise ContractError("functional rule event_time must be Decimal")
        if self.set_enabled is None and self.set_admission is None:
            raise ContractError("functional rule must change ENABLED and/or admission explicitly")
        if self.set_enabled is not None and type(self.set_enabled) is not bool:
            raise ContractError("set_enabled must be Boolean when supplied")
        if self.set_admission not in (None, "ADMIT", "NO_ADMISSION"):
            raise ContractError("unsupported admission state in functional rule")
        if self.source == "D2":
            if self.d2_field not in D2_FIELDS or type(self.d2_value) is not bool:
                raise ContractError("D2 rule requires an allowlisted stage field and Boolean trigger value")
            if (self.vector_index is not None or self.vector_value is not None
                    or self.vector_predicates is not None or self.factor_m_value is not None
                    or self.trajectory_target_state is not None
                    or self.trajectory_field is not None or self.trajectory_value is not None):
                raise ContractError("D2 rule cannot also contain a g_A vector predicate")
        elif self.source == "G_A":
            if (self.d2_field is not None or self.d2_value is not None or self.factor_m_value is not None
                    or self.trajectory_target_state is not None
                    or self.trajectory_field is not None or self.trajectory_value is not None):
                raise ContractError("g_A rule cannot contain a D2-stage or factor-M predicate")
            if self.vector_predicates is None:
                if type(self.vector_index) is not int or self.vector_index not in range(4) or self.vector_value is None:
                    raise ContractError("g_A rule requires one vector component index [0..3] and value")
            else:
                if (not isinstance(self.vector_predicates, tuple)
                        or not self.vector_predicates
                        or any(not isinstance(item, tuple) or len(item) != 2
                               for item in self.vector_predicates)
                        or any(item[1] is None for item in self.vector_predicates)):
                    raise ContractError("g_A conjunctive predicates must be a non-empty tuple of (index, value) pairs")
                indices = [item[0] for item in self.vector_predicates]
                if (self.vector_index is not None or self.vector_value is not None
                        or any(type(index) is not int or index not in range(4) for index in indices)
                        or len(indices) != len(set(indices))):
                    raise ContractError("g_A conjunctive predicates require unique component indices [0..3]")
        elif self.source == "G_M":
            if (self.d2_field is not None or self.d2_value is not None
                    or self.vector_index is not None or self.vector_value is not None
                    or self.vector_predicates is not None or type(self.factor_m_value) is not bool
                    or self.trajectory_target_state is not None
                    or self.trajectory_field is not None or self.trajectory_value is not None):
                raise ContractError("G_M rule requires only an explicit Boolean factor_m_value predicate")
        elif self.source == "TRAJECTORY":
            if (not self.trajectory_target_state
                    or self.trajectory_field not in ("trajectory_status", "execution_state")
                    or self.trajectory_value is None):
                raise ContractError("trajectory rule requires target, allowlisted field and explicit value")
            if self.trajectory_field == "trajectory_status" and self.trajectory_value not in (
                "COMPLETED", "PARTIAL", "NOT_SELECTED", "EXECUTION_FAILED",
                "NOT_REACHABLE", "UNKNOWN",
            ):
                raise ContractError("trajectory_status rule value is outside the declared status vocabulary")
            if self.trajectory_field == "execution_state" and (
                self.trajectory_value not in (1, 0, "?")
                or isinstance(self.trajectory_value, bool)
            ):
                raise ContractError("trajectory execution_state rule value must be 1, 0 or ?")
            if any(value is not None for value in (
                self.d2_field, self.d2_value, self.vector_index, self.vector_value,
                self.vector_predicates, self.factor_m_value,
            )):
                raise ContractError("trajectory rule cannot also contain D2, g_A or G_M predicates")
        else:
            raise ContractError("functional rule source must be D2, G_A, G_M or TRAJECTORY")


@dataclass(frozen=True)
class FunctionalHistoryDGPConfig:
    dgp_id: str
    dgp_version: str
    mechanism_id: str
    mechanism_version: str
    run_id: str
    history_version: str
    adjudication_rules_version: str
    support_start: Decimal
    support_end: Decimal
    profile_config_id: str
    profile_config_version: str
    rules: tuple[FunctionalHistoryRule, ...]

    def validate(self, world: SyntheticWorldBundle) -> None:
        world.validate()
        if (self.dgp_id, self.dgp_version) != (world.dgp_id, world.dgp_version):
            raise ContractError("functional-history DGP identity differs from synthetic world")
        if not all((self.mechanism_id, self.mechanism_version, self.run_id,
                    self.history_version, self.adjudication_rules_version,
                    self.profile_config_id, self.profile_config_version)):
            raise ContractError("functional-history generator identity/version fields are mandatory")
        if not isinstance(self.support_start, Decimal) or not isinstance(self.support_end, Decimal):
            raise ContractError("functional-history support must use Decimal coordinates")
        if self.support_start >= self.support_end:
            raise ContractError("functional-history support must have positive duration")
        ids = [rule.rule_id for rule in self.rules]
        if len(ids) != len(set(ids)):
            raise ContractError("functional rule IDs must be unique")
        for rule in self.rules:
            rule.validate()
            if rule.event_time < self.support_start or rule.event_time > self.support_end:
                raise ContractError("functional rule event_time falls outside declared support")
        # Empty rule subsets are meaningful null-effect mechanisms. They are
        # not silently replaced by an accessibility/admission mapping.


def _apply_rules(
    *, source: Source, initial: FunctionalState, rules: Sequence[FunctionalHistoryRule],
    mechanism: D2PotentialStage | Vector4, factor_m: bool | None = None,
    trajectories_by_target: dict[str, D2PotentialTrajectory] | None = None,
) -> tuple[FunctionalStateChange, ...]:
    current = initial
    changes = []
    selected_rules = (
        r for r in rules
        if r.source == source
        or (source == "G_A" and r.source in ("G_M", "TRAJECTORY"))
        or (source == "D2" and r.source == "TRAJECTORY")
    )
    for rule in sorted(
        selected_rules,
        key=lambda r: (r.event_time, -1 if r.suborder is None else r.suborder, r.rule_id),
    ):
        if rule.source == "D2":
            triggered = getattr(mechanism, rule.d2_field) is rule.d2_value
        elif rule.source == "TRAJECTORY":
            if trajectories_by_target is None or rule.trajectory_target_state not in trajectories_by_target:
                raise ContractError("functional EventHistory trajectory rule lacks its exact target-potential trajectory")
            trajectory = trajectories_by_target[rule.trajectory_target_state]
            triggered = getattr(trajectory, rule.trajectory_field) == rule.trajectory_value
        elif rule.source == "G_A":
            if rule.vector_predicates is None:
                triggered = mechanism[rule.vector_index] == rule.vector_value
            else:
                triggered = all(
                    mechanism[index] == value
                    for index, value in rule.vector_predicates
                )
        else:
            if factor_m is None:
                raise ContractError("G_M functional rules require an explicit factorial M potential")
            triggered = factor_m is rule.factor_m_value
        if not triggered:
            continue
        after = FunctionalState(
            enabled=current.enabled if rule.set_enabled is None else rule.set_enabled,
            admission_behavior=current.admission_behavior if rule.set_admission is None else rule.set_admission,
            profile=current.profile,
            profile_config_id=current.profile_config_id,
            profile_config_version=current.profile_config_version,
        )
        if after == current:
            continue
        changes.append(FunctionalStateChange(
            event_time=rule.event_time, state_after=after,
            causal_family=rule.causal_family,
            provenance_ref=rule.provenance_ref,
            suborder=rule.suborder,
        ))
        current = after
    by_time: dict[Decimal, list[int]] = {}
    for index, change in enumerate(changes):
        by_time.setdefault(change.event_time, []).append(index)
    for indices in by_time.values():
        if len(indices) == 1:
            index = indices[0]
            if changes[index].suborder is not None:
                row = changes[index]
                changes[index] = FunctionalStateChange(
                    row.event_time, row.state_after, row.causal_family,
                    row.provenance_ref, None,
                )
        else:
            supplied = [changes[index].suborder for index in indices]
            if all(value is None for value in supplied):
                for order, index in enumerate(indices):
                    row = changes[index]
                    changes[index] = FunctionalStateChange(
                        row.event_time, row.state_after, row.causal_family,
                        row.provenance_ref, order,
                    )
            elif any(value is None for value in supplied):
                raise ContractError("same-time functional rules must declare all suborders or none")
    return tuple(changes)


def _materialize(
    *, world: SyntheticWorldBundle, config: FunctionalHistoryDGPConfig,
    unit_id: str, potential_id: str, history_id: str,
    initial_state: FunctionalState, source: Source,
    mechanism: D2PotentialStage | Vector4, factor_m: bool | None = None,
    trajectories_by_target: dict[str, D2PotentialTrajectory] | None = None,
) -> EventHistory:
    initial_state.validate()
    if (initial_state.profile_config_id, initial_state.profile_config_version) != (
        config.profile_config_id, config.profile_config_version
    ):
        raise ContractError("initial functional state PROFILE identity/version differs from DGP config")
    initial = initial_state
    changes = _apply_rules(
        source=source, initial=initial,
        rules=config.rules, mechanism=mechanism, factor_m=factor_m,
        trajectories_by_target=trajectories_by_target,
    )
    spec = EventHistoryGenerationSpec(
        history_id=history_id, history_version=config.history_version,
        run_id=config.run_id, world_id=world.world_id, world_version=world.world_version,
        dgp_version=world.dgp_version, unit_id=unit_id, potential_id=potential_id,
        adjudication_rules_version=config.adjudication_rules_version,
        support_start=config.support_start, support_end=config.support_end,
        initial_post_z_state=initial, changes=changes,
        profile_config_id=config.profile_config_id,
        profile_config_version=config.profile_config_version,
    )
    return generate_event_history(spec)


def generate_d2_event_history_potentials(
    world: SyntheticWorldBundle, config: FunctionalHistoryDGPConfig,
    initial_state_by_unit_z: dict[tuple[str, int], FunctionalState],
    trajectories_by_unit_z_target: dict[tuple[str, int, str], D2PotentialTrajectory] | None = None,
) -> dict[tuple[str, int], EventHistory]:
    """Generate D2 functional histories with optional explicit trajectory-outcome rules."""
    config.validate(world)
    expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(initial_state_by_unit_z) != expected:
        raise ContractError("D2 initial functional states must cover exact unit × Z potential roster")
    trajectory_rules = tuple(rule for rule in config.rules if rule.source == "TRAJECTORY")
    trajectories_by_unit_z: dict[tuple[str, int], dict[str, D2PotentialTrajectory]] = {}
    if trajectory_rules:
        if trajectories_by_unit_z_target is None:
            raise ContractError("trajectory-driven D2 EventHistory requires generated potential trajectories")
        targets = {key[2] for key in trajectories_by_unit_z_target}
        required_targets = {rule.trajectory_target_state for rule in trajectory_rules}
        if not required_targets.issubset(targets):
            raise ContractError("trajectory bundle omits a target referenced by a functional rule")
        expected_trajectory_keys = {
            (unit_id, z, target) for unit_id, z in expected for target in targets
        }
        if set(trajectories_by_unit_z_target) != expected_trajectory_keys:
            raise ContractError("trajectory potentials must cover exact unit × Z × target support")
        for key, trajectory in trajectories_by_unit_z_target.items():
            trajectory.validate()
            if (trajectory.unit_id, trajectory.z, trajectory.target_state) != key:
                raise ContractError("trajectory potential identity differs from its declared key")
            trajectories_by_unit_z.setdefault((key[0], key[1]), {})[key[2]] = trajectory
    elif trajectories_by_unit_z_target is not None:
        raise ContractError("trajectory inputs were supplied but no trajectory-driven functional rule is declared")
    result = {}
    for unit in world.units:
        for stage in unit.d2_potentials.potentials_by_z:
            key = (unit.unit_id, stage.z)
            history = _materialize(
                world=world, config=config, unit_id=unit.unit_id,
                potential_id=f"{unit.unit_id}:D2:Z{stage.z}",
                history_id=f"{config.run_id}:{unit.unit_id}:D2:Z{stage.z}",
                initial_state=initial_state_by_unit_z[key],
                source="D2", mechanism=stage,
                trajectories_by_target=trajectories_by_unit_z.get(key),
            )
            result[key] = history
    return result


def generate_factorial_event_history_potentials(
    world: SyntheticWorldBundle, config: FunctionalHistoryDGPConfig,
    g_a0: Sequence[JointPolicyHistory], g_a1: Sequence[JointPolicyHistory],
    r_common_certificates: Sequence[RCommonPairCertificate],
    initial_state_by_history: dict[str, FunctionalState],
    *, factor_m_id: str, factor_m_version: str,
    trajectories_by_history_vector_target: dict[tuple[str, str, str, str], object] | None = None,
) -> dict[tuple[str, str, str, int], EventHistory]:
    """Generate the four A×M potential histories within one fixed synthetic world.

    A is represented by the existing direct-g_A joint-policy vector. M is a
    separate Boolean DGP intervention, never a Vector4 coordinate. Every
    supported vector is materialized under both M potentials and the same
    certified r_common regime.
    """
    config.validate(world)
    if not factor_m_id or not factor_m_version:
        raise ContractError("factor M identity and version are mandatory")
    qx_by_ref = {row.history_ref: row for row in world.q_x}
    expected_refs = set(qx_by_ref)
    if set(initial_state_by_history) != expected_refs:
        raise ContractError("factorial initial functional states must cover q_X* exactly")
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != expected_refs:
        raise ContractError("factorial generation requires one r_common certificate per q_X* history")
    policy_maps = []
    for policy_rows, label in ((g_a0, "g_A0"), (g_a1, "g_A1")):
        mapping = {row.history_ref: row for row in policy_rows}
        if len(mapping) != len(policy_rows) or set(mapping) != expected_refs:
            raise ContractError(f"{label} must cover q_X* histories exactly")
        policy_maps.append(mapping)
    if any(cert.status != "COMMON_FIXED" or not cert.regime_id or not cert.regime_version
           or not cert.g_a0_fingerprint or cert.g_a0_fingerprint != cert.g_a1_fingerprint
           for cert in certs.values()):
        raise ContractError("factorial generation requires certified common fixed r_common")
    trajectory_rules = tuple(rule for rule in config.rules if rule.source == "TRAJECTORY")
    trajectories_by_history_vector: dict[tuple[str, str, str], dict[str, object]] = {}
    expected_trajectory_keys = set()
    for history_ref in sorted(expected_refs):
        cert = certs[history_ref]
        vectors = {
            digest(vector): vector
            for policy_map in policy_maps
            for vector, probability in policy_map[history_ref].distribution
            if probability > 0
        }
        for vector_sha in vectors:
            for rule in trajectory_rules:
                expected_trajectory_keys.add((
                    history_ref, vector_sha, cert.g_a0_fingerprint,
                    rule.trajectory_target_state,
                ))
    if trajectory_rules:
        if trajectories_by_history_vector_target is None:
            raise ContractError("factorial EventHistory trajectory rules require exact g_A potential trajectories")
        if set(trajectories_by_history_vector_target) != expected_trajectory_keys:
            raise ContractError("factorial trajectory inputs must cover exact q_X* × vector × r_common × target support")
        for key, trajectory in trajectories_by_history_vector_target.items():
            if (trajectory.history_ref, trajectory.vector_sha256,
                    trajectory.r_common_fingerprint, trajectory.target_state) != key:
                raise ContractError("factorial trajectory identity differs from its declared potential key")
            trajectories_by_history_vector.setdefault(key[:3], {})[key[3]] = trajectory
    elif trajectories_by_history_vector_target is not None:
        raise ContractError("factorial trajectories supplied without a declared TRAJECTORY EventHistory rule")
    result = {}
    for history_ref in sorted(expected_refs):
        cert = certs[history_ref]
        unit = next(u for u in world.units if u.d2_baseline.baseline_history_ref == history_ref)
        vectors = {}
        for policy_map in policy_maps:
            for vector, probability in policy_map[history_ref].distribution:
                if probability > 0:
                    vectors[digest(vector)] = vector
        for m_arm in (0, 1):
            for vector_sha, vector in sorted(vectors.items()):
                key = (history_ref, vector_sha, cert.g_a0_fingerprint, m_arm)
                result[key] = _materialize(
                    world=world, config=config, unit_id=unit.unit_id,
                    potential_id=(f"{unit.unit_id}:G_AxM:{factor_m_id}:{factor_m_version}:"
                                  f"{vector_sha}:{cert.g_a0_fingerprint}:M{m_arm}"),
                    history_id=(f"{config.run_id}:{unit.unit_id}:G_AxM:"
                                f"{factor_m_id}:{factor_m_version}:{vector_sha}:M{m_arm}"),
                    initial_state=initial_state_by_history[history_ref],
                    source="G_A", mechanism=vector, factor_m=bool(m_arm),
                    trajectories_by_target=trajectories_by_history_vector.get(
                        (history_ref, vector_sha, cert.g_a0_fingerprint),
                    ),
                )
    return result


def generate_g_a_event_history_potentials(
    world: SyntheticWorldBundle, config: FunctionalHistoryDGPConfig,
    g_a0: Sequence[JointPolicyHistory], g_a1: Sequence[JointPolicyHistory],
    r_common_certificates: Sequence[RCommonPairCertificate],
    initial_state_by_history: dict[str, FunctionalState],
) -> dict[tuple[str, str, str], EventHistory]:
    """Generate one functional potential per supported joint vector and common regime.

    Keys match the existing theta_A oracle contract:
    (history_ref, digest(vector), r_common_fingerprint).
    """
    config.validate(world)
    qx_by_ref = {row.history_ref: row for row in world.q_x}
    expected_refs = set(qx_by_ref)
    if set(initial_state_by_history) != expected_refs:
        raise ContractError("g_A initial functional states must cover q_X* histories exactly")
    certs = {row.history_ref: row for row in r_common_certificates}
    if len(certs) != len(r_common_certificates) or set(certs) != expected_refs:
        raise ContractError("g_A generation requires one r_common certificate per q_X* history")
    policy_maps = []
    for policy_rows in (g_a0, g_a1):
        mapping = {row.history_ref: row for row in policy_rows}
        if len(mapping) != len(policy_rows) or set(mapping) != expected_refs:
            raise ContractError("each g_A policy must cover q_X* histories exactly")
        policy_maps.append(mapping)
    result = {}
    for history_ref in sorted(expected_refs):
        cert = certs[history_ref]
        if cert.status != "COMMON_FIXED" or not cert.regime_id or not cert.regime_version:
            raise ContractError("functional g_A generation requires a certified common fixed regime")
        unit = next(u for u in world.units if u.d2_baseline.baseline_history_ref == history_ref)
        unit_id = unit.unit_id
        vectors = {}
        for policy_map in policy_maps:
            for vector, probability in policy_map[history_ref].distribution:
                if probability > 0:
                    vectors[digest(vector)] = vector
        for vector_sha, vector in sorted(vectors.items()):
            key = (history_ref, vector_sha, cert.g_a0_fingerprint)
            history = _materialize(
                world=world, config=config, unit_id=unit_id,
                potential_id=f"{unit_id}:G_A:{vector_sha}:{cert.g_a0_fingerprint}",
                history_id=f"{config.run_id}:{unit_id}:G_A:{vector_sha}",
                initial_state=initial_state_by_history[history_ref],
                source="G_A", mechanism=vector,
            )
            result[key] = history
    return result
