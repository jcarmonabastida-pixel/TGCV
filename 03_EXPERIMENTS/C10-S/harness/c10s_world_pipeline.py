"""End-to-end C10-S synthetic-world composition.

This is an integration boundary, not a new scientific estimand. It composes
existing frozen D2, structural-delta, Reach, trajectory, EventHistory,
VCONT-B1-MIN, direct-g_A, S3, Sealer, Analyzer and Evaluator contracts.
All stochastic/design inputs are explicit. No tests or scientific execution
are performed by importing or authoring this module.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from c10s_synthetic_components import (
    ContractError,
    D2MechanismConfig,
    D2ReachGenerationConfig,
    D2StructuralGenerationConfig,
    D2TrajectoryGenerationConfig,
    EventHistory,
    IntervalGrid,
    JointPolicyHistory,
    QXHistoryMass,
    RCommonPairCertificate,
    SyntheticWorldBuilder,
    SyntheticWorldBundle,
    SyntheticWorldConfig,
    SyntheticWorldReachabilityContrast,
    SyntheticWorldTrajectoryBundle,
    D2StructuralPotentialPair,
    D2VContTruthBundle,
    ThetaAPolicyAssignmentBundle,
    ThetaAPolicyAssignmentConfig,
    ThetaAPolicyHistorySelection,
    ThetaAVContTruthBundle,
    ThetaAS3ObservationRecord,
    Vector4,
    compute_theta_a_vcont_truth_from_event_histories,
    compose_theta_a_s3_observation_records,
    evaluate_d2_structural_deltas,
    generate_theta_a_policy_assignments,
    select_theta_a_realized_histories,
)
from theta_a_observation_harness import (
    SealedThetaAEvidence,
    ThetaASealer,
    candidate_from_s3_records,
)
from theta_a_analyzer import (
    ThetaAObservationAnalysisContract,
    ThetaAObservationAnalysisResult,
    ThetaAObservationAnalyzer,
)
from theta_a_evaluator import (
    ThetaAObservationEvaluation,
    ThetaAObservationEvaluator,
)


@dataclass(frozen=True)
class C10SCompleteWorldResult:
    """One identity-bound synthetic world and its independent causal adjudication."""

    world: SyntheticWorldBundle
    structural_pairs: tuple[tuple[tuple[str, int], D2StructuralPotentialPair], ...]
    structural_deltas: tuple[object, ...]
    reachability: SyntheticWorldReachabilityContrast
    trajectories: SyntheticWorldTrajectoryBundle
    d2_vcont_truth: D2VContTruthBundle
    d2_histories_by_unit_z: tuple[tuple[tuple[str, int], EventHistory], ...]
    theta_a_truth: ThetaAVContTruthBundle
    theta_a_assignments: ThetaAPolicyAssignmentBundle
    realized_history_selection: ThetaAPolicyHistorySelection
    s3_records: tuple[ThetaAS3ObservationRecord, ...]
    sealed_evidence: SealedThetaAEvidence
    analyzer_contract: ThetaAObservationAnalysisContract
    analyzer_result: ThetaAObservationAnalysisResult
    evaluator_result: ThetaAObservationEvaluation

    def validate(
        self,
        *,
        grid: IntervalGrid,
        reach_config: D2ReachGenerationConfig,
        g_a0: Sequence[JointPolicyHistory],
        g_a1: Sequence[JointPolicyHistory],
        assignment_config: ThetaAPolicyAssignmentConfig,
        feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
        r_common_certificates: Sequence[RCommonPairCertificate],
    ) -> None:
        world = self.world
        world.validate()
        grid.validate()
        pairs = dict(self.structural_pairs)
        expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
        if set(pairs) != expected or len(pairs) != len(self.structural_pairs):
            raise ContractError("complete-world result must retain exact unit × Z structural-pair coverage")
        deltas = {(row.unit_id, row.potential_z): row for row in self.structural_deltas}
        if set(deltas) != expected or len(deltas) != len(self.structural_deltas):
            raise ContractError("complete-world result must retain exact unit × Z ΔT_acc* coverage")
        self.reachability.validate(world)
        self.trajectories.validate(world, self.reachability, reach_config)
        d2_histories = dict(self.d2_histories_by_unit_z)
        self.d2_vcont_truth.validate(world, d2_histories, grid)
        self.theta_a_truth.validate()
        if (self.theta_a_truth.world_id, self.theta_a_truth.world_version,
                self.theta_a_truth.dgp_id, self.theta_a_truth.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("theta_A oracle identity differs from the composed synthetic world")
        if (self.theta_a_assignments.world_id, self.theta_a_assignments.world_version,
                self.theta_a_assignments.dgp_id, self.theta_a_assignments.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("direct-g_A assignment identity differs from the composed synthetic world")
        self.theta_a_assignments.validate(
            world, assignment_config, g_a0, g_a1,
            feasible_vectors_by_history, r_common_certificates,
        )
        if self.realized_history_selection.assignment_bundle_sha256 != self.theta_a_assignments.result_sha256:
            raise ContractError("realized EventHistory selection is detached from direct-g_A assignments")
        if not self.s3_records or not self.sealed_evidence.rows:
            raise ContractError("complete-world result requires realized S3 observations and sealed evidence")
        if self.analyzer_result.input_sha256 != self.sealed_evidence.sha256:
            raise ContractError("Analyzer result is detached from sealed evidence")
        if self.evaluator_result.evidence_sha256 != self.sealed_evidence.sha256:
            raise ContractError("Evaluator result is detached from sealed evidence")
        if self.evaluator_result.analyzer_output_sha256 != self.analyzer_result.output_sha256:
            raise ContractError("Evaluator result is detached from Analyzer output")
        if not self.evaluator_result.correct_adjudication:
            raise ContractError("independent Evaluator rejected the Analyzer's current adjudication")
        run_ids = {history.run_id for history in d2_histories.values()}
        run_ids.update(history.run_id for history in self._policy_histories)
        if len(run_ids) != 1 or self.sealed_evidence.run_id not in run_ids:
            raise ContractError("complete-world components do not share one experiment run identity")

    _policy_histories: tuple[EventHistory, ...] = ()

def materialize_c10s_complete_world(
    *,
    world_config: SyntheticWorldConfig,
    d2_config: D2MechanismConfig,
    structural_config: D2StructuralGenerationConfig,
    reach_config: D2ReachGenerationConfig,
    trajectory_config: D2TrajectoryGenerationConfig,
    d2_histories_by_unit_z: dict[tuple[str, int], EventHistory],
    grid: IntervalGrid,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    event_histories_by_policy: dict[tuple[str, str, str], EventHistory],
    assignment_config: ThetaAPolicyAssignmentConfig,
    s3_configs_by_history_ref: dict[str, object],
    s3_seeds_by_unit: dict[str, int],
    estimand_version: str,
    outcome_version: str,
    evaluation_tolerance: float,
) -> C10SCompleteWorldResult:
    """Materialize one coherent world through D2/ΔT_acc*/Reach/trajectory and
    the direct-g_A → EventHistory → S3 → Sealer → Analyzer → Evaluator path.

    D2 potential EventHistories and direct-g_A policy EventHistories are
    explicit outputs of the versioned DGP/event-history generator and must
    share one run identity and the exact world roster. This function does not
    invent event transitions or infer missing temporal states.
    """
    if not estimand_version or not outcome_version:
        raise ContractError("estimand and outcome versions must be explicit")
    builder = SyntheticWorldBuilder()
    world, structural_pairs, reachability, trajectories = (
        builder.generate_complete_with_trajectories(
            world_config, d2_config, structural_config,
            reach_config, trajectory_config,
        )
    )
    expected_d2 = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
    if set(d2_histories_by_unit_z) != expected_d2:
        raise ContractError("D2 EventHistory inputs must cover every world unit × Z potential exactly")
    if any(
        history.world_id != world.world_id
        or history.world_version != world.world_version
        or history.dgp_version != world.dgp_version
        or history.unit_id != unit_id
        for (unit_id, _), history in d2_histories_by_unit_z.items()
    ):
        raise ContractError("D2 EventHistory identity differs from its exact world/unit/Z potential")
    d2_truth = builder.evaluate_complete_vcont_truth(world, d2_histories_by_unit_z, grid)
    structural_deltas = evaluate_d2_structural_deltas(world, structural_pairs)

    theta_truth = compute_theta_a_vcont_truth_from_event_histories(
        world, world.q_x, g_a0, g_a1, feasible_vectors_by_history,
        r_common_certificates, event_histories_by_policy, grid,
        estimand_version=estimand_version, outcome_version=outcome_version,
    )
    policy_histories = tuple(event_histories_by_policy.values())
    run_ids = {history.run_id for history in d2_histories_by_unit_z.values()}
    run_ids.update(history.run_id for history in policy_histories)
    if len(run_ids) != 1:
        raise ContractError("D2 and direct-g_A EventHistory potentials must share one experiment run identity")
    run_id = next(iter(run_ids))
    if d2_truth.run_id != run_id:
        raise ContractError("D2 V_cont truth run identity differs from the composed experiment")

    assignments = generate_theta_a_policy_assignments(
        world, assignment_config, g_a0, g_a1,
        feasible_vectors_by_history, r_common_certificates,
    )
    selection = select_theta_a_realized_histories(assignments, policy_histories)
    s3_records = compose_theta_a_s3_observation_records(
        assignments, selection, policy_histories,
        s3_configs_by_history_ref, s3_seeds_by_unit,
    )
    candidate = candidate_from_s3_records(s3_records)
    sealed = ThetaASealer().seal(candidate)
    contract = ThetaAObservationAnalysisContract(
        q_x_mass_by_history=tuple((row.history_ref, row.mass) for row in world.q_x),
        q_x_sha256=assignments.q_x_sha256,
        assignment_bundle_sha256=assignments.result_sha256,
        g_a0_sha256=assignments.g_a0_sha256,
        g_a1_sha256=assignments.g_a1_sha256,
        r_common_sha256=assignments.r_common_sha256,
        estimand_id=theta_truth.theta_a_truth.estimand_id,
        estimand_version=theta_truth.theta_a_truth.estimand_version,
    )
    analysis = ThetaAObservationAnalyzer().analyze(sealed, contract)
    evaluation = ThetaAObservationEvaluator().evaluate(
        theta_truth, sealed, analysis, assignments, contract,
        tolerance=evaluation_tolerance,
    )

    result = C10SCompleteWorldResult(
        world=world,
        structural_pairs=tuple(sorted(structural_pairs.items())),
        structural_deltas=tuple(structural_deltas),
        reachability=reachability,
        trajectories=trajectories,
        d2_vcont_truth=d2_truth,
        d2_histories_by_unit_z=tuple(sorted(d2_histories_by_unit_z.items())),
        theta_a_truth=theta_truth,
        theta_a_assignments=assignments,
        realized_history_selection=selection,
        s3_records=tuple(s3_records),
        sealed_evidence=sealed,
        analyzer_contract=contract,
        analyzer_result=analysis,
        evaluator_result=evaluation,
        _policy_histories=policy_histories,
    )
    result.validate(
        grid=grid, reach_config=reach_config, g_a0=g_a0, g_a1=g_a1,
        assignment_config=assignment_config,
        feasible_vectors_by_history=feasible_vectors_by_history,
        r_common_certificates=r_common_certificates,
    )
    return result


# DGP-driven functional history materialization. The lower-level composer above
# remains available for explicit fixtures; this entry point removes externally
# supplied EventHistory dictionaries from the normal synthetic-world path.
from c10s_functional_history import (
    FunctionalHistoryDGPConfig,
    generate_d2_event_history_potentials,
    generate_g_a_event_history_potentials,
)


def materialize_c10s_complete_world_from_dgp(
    *,
    world_config: SyntheticWorldConfig,
    d2_config: D2MechanismConfig,
    structural_config: D2StructuralGenerationConfig,
    reach_config: D2ReachGenerationConfig,
    trajectory_config: D2TrajectoryGenerationConfig,
    functional_history_config: FunctionalHistoryDGPConfig,
    initial_state_by_unit_z: dict[tuple[str, int], FunctionalState],
    initial_state_by_history: dict[str, FunctionalState],
    grid: IntervalGrid,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    assignment_config: ThetaAPolicyAssignmentConfig,
    s3_configs_by_history_ref: dict[str, object],
    s3_seeds_by_unit: dict[str, int],
    estimand_version: str,
    outcome_version: str,
    evaluation_tolerance: float,
) -> C10SCompleteWorldResult:
    """Generate D2 and direct-g_A potential EventHistories inside the DGP pipeline.

    Functional rules, rather than implicit accessibility/admission equivalence,
    determine ENABLED/admission. The legacy composer receives only generated
    potential histories; S3 still sees only the realized-history projection.
    """
    builder = SyntheticWorldBuilder()
    world, _, _ = builder.generate_complete_with_trajectories(
        world_config, d2_config, structural_config, reach_config, trajectory_config,
    )
    d2_histories = generate_d2_event_history_potentials(
        world, functional_history_config, initial_state_by_unit_z,
    )
    policy_histories = generate_g_a_event_history_potentials(
        world, functional_history_config, g_a0, g_a1,
        r_common_certificates, initial_state_by_history,
    )
    return materialize_c10s_complete_world(
        world_config=world_config, d2_config=d2_config,
        structural_config=structural_config, reach_config=reach_config,
        trajectory_config=trajectory_config,
        d2_histories_by_unit_z=d2_histories, grid=grid,
        g_a0=g_a0, g_a1=g_a1,
        feasible_vectors_by_history=feasible_vectors_by_history,
        r_common_certificates=r_common_certificates,
        event_histories_by_policy=policy_histories,
        assignment_config=assignment_config,
        s3_configs_by_history_ref=s3_configs_by_history_ref,
        s3_seeds_by_unit=s3_seeds_by_unit,
        estimand_version=estimand_version, outcome_version=outcome_version,
        evaluation_tolerance=evaluation_tolerance,
    )
