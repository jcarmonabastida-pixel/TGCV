"""End-to-end C10-S synthetic-world composition.

This is an integration boundary, not a new scientific estimand. It composes
existing frozen D2, structural-delta, Reach, trajectory, EventHistory,
VCONT-B1-MIN, direct-g_A, S3, Sealer, Analyzer and Evaluator contracts.
All stochastic/design inputs are explicit. No tests or scientific execution
are performed by importing or authoring this module.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

from c10s_synthetic_components import (
    ContractError,
    D2MechanismConfig,
    D2ReachGenerationConfig,
    D2StructuralGenerationConfig,
    D2TrajectoryGenerationConfig,
    EventHistory,
    FunctionalState,
    IntervalGrid,
    JointPolicyHistory,
    QXHistoryMass,
    digest,
    RCommonPairCertificate,
    SyntheticWorldBuilder,
    SyntheticWorldBundle,
    SyntheticWorldConfig,
    NeedPreZStipulation,
    NeedPreZTruthBundle,
    materialize_need_prez_truth,
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
    ThetaAIntervalSealer,
    candidate_from_s3_records,
)
from theta_a_interval_observation import (
    IntervalMonitorConfig,
    ThetaAIntervalObservationRecord,
    compose_theta_a_interval_s3_records,
    candidate_from_theta_a_interval_records,
)
from theta_a_analyzer import (
    ThetaAObservationAnalysisContract,
    ThetaAStructuralSupportContract,
    ThetaAObservationAnalysisResult,
    ThetaAObservationAnalyzer,
)
from theta_a_evaluator import (
    ThetaAObservationEvaluation,
    ThetaAObservationEvaluator,
)
from d2_observed_assignment import D2ObservedAssignmentConfig
from d2_interval_observation import (
    D2ObservedIntervalLaneResult,
    materialize_d2_observed_interval_lane,
)
from d2_ittz_analyzer import (
    D2ITTZAnalysisContract,
    D2ITTZAnalysisResult,
    D2ITTZAnalyzer,
    analysis_contract_from_world,
)
from d2_ittz_evaluator import D2ITTZEvaluation, D2ITTZEvaluator


@dataclass(frozen=True)
class SyntheticThetaATargetHistory:
    """Explicit test-harness materialization of a target-only baseline history.

    This is synthetic DGP input, not authorization for a B1/UE population.
    """
    q_x: QXHistoryMass
    potential_unit_id: str
    x_values: tuple[float, ...]
    h0_value: str
    c_c_values: tuple[bool, ...]
    initial_functional_state: FunctionalState
    provenance_ref: str

    def validate(self, *, source_world: SyntheticWorldBundle, allowed_h0_values: set[str]) -> None:
        if not self.potential_unit_id or not self.provenance_ref:
            raise ContractError("target-only baseline requires explicit synthetic unit and provenance identities")
        if self.q_x.history_ref in {
            row.history_ref for row in source_world.q_x
        } or self.potential_unit_id in {unit.unit_id for unit in source_world.units}:
            raise ContractError("target-only materialization must not alias a source history or source unit")
        if (not self.q_x.x_ref or not self.q_x.h0_ref or not self.q_x.c_c_ref
                or self.h0_value not in allowed_h0_values):
            raise ContractError("target-only baseline requires explicit X/H0/C_c anchors and H0 value")
        if (not self.x_values or any(not math.isfinite(value) for value in self.x_values)
                or not self.c_c_values
                or any(type(value) is not bool for value in self.c_c_values)):
            raise ContractError("target-only X/C_c values must be nonempty, finite and typed")
        source = source_world.units[0]
        if len(self.x_values) != len(source.x) or len(self.c_c_values) != len(source.c_c):
            raise ContractError("target-only X/C_c dimensions must match the declared synthetic DGP schema")
        self.initial_functional_state.validate()


@dataclass(frozen=True)
class C10SCompleteWorldResult:
    """One identity-bound synthetic world and its independent causal adjudication."""

    world: SyntheticWorldBundle
    need_pre_z_truth: NeedPreZTruthBundle
    structural_pairs: tuple[tuple[tuple[str, int], D2StructuralPotentialPair], ...]
    structural_deltas: tuple[object, ...]
    reachability: SyntheticWorldReachabilityContrast
    trajectories: SyntheticWorldTrajectoryBundle
    d2_vcont_truth: D2VContTruthBundle
    d2_observed_lane: D2ObservedIntervalLaneResult
    d2_analysis_contract: D2ITTZAnalysisContract
    d2_analyzer_result: D2ITTZAnalysisResult
    d2_evaluator_result: D2ITTZEvaluation
    d2_histories_by_unit_z: tuple[tuple[tuple[str, int], EventHistory], ...]
    theta_a_truth: ThetaAVContTruthBundle
    theta_a_assignments: ThetaAPolicyAssignmentBundle
    realized_history_selection: ThetaAPolicyHistorySelection
    s3_records: tuple[ThetaAS3ObservationRecord | ThetaAIntervalObservationRecord, ...]
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
        theta_a_structural_support_contract: ThetaAStructuralSupportContract | None = None,
    ) -> None:
        world = self.world
        world.validate()
        self.need_pre_z_truth.validate(world)
        grid.validate()
        pairs = dict(self.structural_pairs)
        expected = {(unit.unit_id, z) for unit in world.units for z in (0, 1)}
        if set(pairs) != expected or len(pairs) != len(self.structural_pairs):
            raise ContractError("complete-world result must retain exact unit × Z structural-pair coverage")
        deltas = {(row.unit_id, row.potential_z): row for row in self.structural_deltas}
        if set(deltas) != expected or len(deltas) != len(self.structural_deltas):
            raise ContractError("complete-world result must retain exact unit × Z ΔT_acc* coverage")
        for key in sorted(expected):
            pair = pairs[key]
            delta = deltas[key]
            if (delta.baseline_snapshot_id, delta.post_snapshot_id) != (
                pair.baseline.snapshot_id, pair.post.snapshot_id,
            ):
                raise ContractError("ΔT_acc* does not reference its exact D2 baseline/post structural snapshots")
        self.reachability.validate(world)
        reach_by_key = {(row.unit_id, row.z): row for row in self.reachability.contrasts}
        if set(reach_by_key) != expected or len(reach_by_key) != len(expected):
            raise ContractError("complete-world Reach must retain exact unit × Z potential coverage")
        for key in sorted(expected):
            pair = pairs[key]
            contrast = reach_by_key[key]
            if (contrast.baseline.snapshot_id, contrast.post.snapshot_id) != (
                f"{pair.baseline.snapshot_id}:REACH:BASELINE",
                f"{pair.post.snapshot_id}:REACH:POST",
            ):
                raise ContractError("Reach baseline/post snapshots are detached from the exact ΔT_acc* potential")
        self.trajectories.validate(world, self.reachability, reach_config)
        d2_histories = dict(self.d2_histories_by_unit_z)
        self.d2_vcont_truth.validate(world, d2_histories, grid)
        self.d2_observed_lane.validate(world, self.d2_vcont_truth, d2_histories, grid)
        if self.d2_analyzer_result.input_sha256 != self.d2_observed_lane.sealed_evidence.sha256:
            raise ContractError("D2 ITT-Z Analyzer result is detached from its sealed evidence")
        if self.d2_evaluator_result.evidence_sha256 != self.d2_observed_lane.sealed_evidence.sha256:
            raise ContractError("D2 ITT-Z Evaluator result is detached from its sealed evidence")
        if self.d2_evaluator_result.analyzer_output_sha256 != self.d2_analyzer_result.output_sha256:
            raise ContractError("D2 ITT-Z Evaluator result is detached from its Analyzer output")
        if self.d2_evaluator_result.truth_itt_z != self.d2_vcont_truth.finite_population_itt_z_v_cont:
            raise ContractError("D2 ITT-Z Evaluator truth differs from reserved D2 V_cont truth")
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
            theta_a_structural_support_contract,
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
        if (self.evaluator_result.estimand_id != self.theta_a_truth.theta_a_truth.estimand_id
                or self.evaluator_result.estimand_version != self.theta_a_truth.theta_a_truth.estimand_version
                or self.evaluator_result.truth != self.theta_a_truth.theta_a_truth.theta_a_truth):
            raise ContractError("Evaluator result is detached from the reserved theta_A truth identity/value")
        # A false correct_adjudication is a scientific recovery result, not a
        # materialization/provenance failure. Preserve it for evaluation rather
        # than rejecting an otherwise valid synthetic world.
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
    d2_assignment_config: D2ObservedAssignmentConfig,
    d2_interval_monitor_configs_by_history_ref: dict[str, IntervalMonitorConfig] | IntervalMonitorConfig,
    d2_interval_monitor_seeds_by_unit: dict[str, int],
    need_pre_z_stipulations: Sequence[NeedPreZStipulation],
    grid: IntervalGrid,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    event_histories_by_policy: dict[tuple[str, str, str], EventHistory],
    assignment_config: ThetaAPolicyAssignmentConfig,
    s3_configs_by_history_ref: dict[str, object] | None = None,
    s3_seeds_by_unit: dict[str, int] | None = None,
    estimand_version: str,
    outcome_version: str,
    evaluation_tolerance: float,
    interval_monitor_configs_by_history_ref: dict[str, IntervalMonitorConfig] | None = None,
    interval_monitor_seeds_by_unit: dict[str, int] | None = None,
    theta_a_confidence_level: float | None = None,
    theta_a_unit_independence_certified: bool = False,
    theta_a_q_x: Sequence[QXHistoryMass] | None = None,
    theta_a_unit_id_by_history: dict[str, str] | None = None,
    theta_a_structural_support_contract: ThetaAStructuralSupportContract | None = None,
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
    need_truth = materialize_need_prez_truth(world, need_pre_z_stipulations)
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
    d2_observed_lane = materialize_d2_observed_interval_lane(
        world=world, truth=d2_truth, histories_by_unit_z=d2_histories_by_unit_z,
        assignment_config=d2_assignment_config, grid=grid,
        monitor_config_by_history_ref=d2_interval_monitor_configs_by_history_ref,
        seeds_by_unit=d2_interval_monitor_seeds_by_unit,
    )
    if isinstance(d2_interval_monitor_configs_by_history_ref, IntervalMonitorConfig):
        d2_monitor_config = d2_interval_monitor_configs_by_history_ref
    else:
        d2_monitor_configs = tuple(d2_interval_monitor_configs_by_history_ref.values())
        if not d2_monitor_configs:
            raise ContractError("D2 interval monitor configuration roster must not be empty")
        d2_monitor_config = d2_monitor_configs[0]
        if any((row.monitor_id, row.monitor_version) !=
               (d2_monitor_config.monitor_id, d2_monitor_config.monitor_version)
               for row in d2_monitor_configs):
            raise ContractError("D2 ITT-Z requires one common monitor identity/version across q_X*")
    d2_contract = analysis_contract_from_world(
        world, d2_observed_lane.assignments.result_sha256,
        d2_observed_lane.assignments.mechanism_id,
        d2_observed_lane.assignments.mechanism_version,
        grid.grid_id, grid.grid_version,
        d2_monitor_config.monitor_id, d2_monitor_config.monitor_version,
    )
    d2_analysis = D2ITTZAnalyzer().analyze(d2_observed_lane.sealed_evidence, d2_contract)
    d2_evaluation = D2ITTZEvaluator().evaluate(
        world=world, truth=d2_truth, assignments=d2_observed_lane.assignments,
        evidence=d2_observed_lane.sealed_evidence, contract=d2_contract,
        result=d2_analysis, tolerance=evaluation_tolerance,
    )
    structural_deltas = evaluate_d2_structural_deltas(world, structural_pairs)

    target_q_x = tuple(theta_a_q_x) if theta_a_q_x is not None else world.q_x
    target_unit_ids = theta_a_unit_id_by_history or {
        unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
    }
    if (len({row.history_ref for row in target_q_x}) != len(target_q_x)
            or set(target_unit_ids) != {row.history_ref for row in target_q_x}):
        raise ContractError("theta_A target q_X and target-unit identities must cover exactly the same histories")
    assignment_probabilities = dict(assignment_config.probability_a1_by_history)
    if theta_a_structural_support_contract is not None:
        if (theta_a_structural_support_contract.target_q_x_sha256 != digest(target_q_x)
                or theta_a_structural_support_contract.source_q_x_sha256 != digest(world.q_x)):
            raise ContractError("structural-support fingerprints do not bind the generated target and source q_X")
        source_masses = {row.history_ref: row.mass for row in world.q_x}
        if any(not math.isclose(
                row.source_mass, source_masses.get(row.history_ref, 0.0),
                rel_tol=0.0, abs_tol=1e-12,
        ) for row in theta_a_structural_support_contract.rows):
            raise ContractError("structural-support source masses do not reproduce the generated source q_X")
        if any(row.source_mass > 0.0 and not math.isclose(
                row.assignment_probability_a1,
                assignment_probabilities.get(row.history_ref, math.nan),
                rel_tol=0.0, abs_tol=1e-12,
        ) for row in theta_a_structural_support_contract.rows):
            raise ContractError("structural-support propensities do not reproduce the generated assignment mechanism")
    # Assignment and realized-history materialization span the complete
    # source roster (plus target-only histories), whereas the focal truth
    # functional is integrated only over q_X*. Keep these supports distinct:
    # source-only histories need randomized assignments and EventHistories,
    # but they must not enter the target estimand or its truth manifest.
    target_refs = {row.history_ref for row in target_q_x}
    target_g_a0 = tuple(row for row in g_a0 if row.history_ref in target_refs)
    target_g_a1 = tuple(row for row in g_a1 if row.history_ref in target_refs)
    target_r_common = tuple(
        row for row in r_common_certificates if row.history_ref in target_refs
    )
    target_feasible = {
        history_ref: vectors for history_ref, vectors in feasible_vectors_by_history.items()
        if history_ref in target_refs
    }
    target_event_histories = {
        key: history for key, history in event_histories_by_policy.items()
        if key[0] in target_refs
    }
    theta_truth = compute_theta_a_vcont_truth_from_event_histories(
        world, target_q_x, target_g_a0, target_g_a1, target_feasible,
        target_r_common, target_event_histories, grid,
        estimand_version=estimand_version, outcome_version=outcome_version,
        unit_id_by_history=target_unit_ids,
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
        structural_support_contract=theta_a_structural_support_contract,
    )
    selection = select_theta_a_realized_histories(assignments, policy_histories)
    if interval_monitor_configs_by_history_ref is not None:
        if s3_configs_by_history_ref is not None or s3_seeds_by_unit is not None:
            raise ContractError("select exactly one focal S3 measurement mode: point or interval")
        expected_refs = {row.history_ref for row in world.q_x}
        if set(interval_monitor_configs_by_history_ref) != expected_refs:
            raise ContractError("interval monitor configs must cover q_X* history support exactly")
        if interval_monitor_seeds_by_unit is None or set(interval_monitor_seeds_by_unit) != {
            row.unit_id for row in world.units
        }:
            raise ContractError("interval monitor seeds must cover the world unit roster exactly")
        grids_by_history = {ref: grid for ref in expected_refs}
        s3_records = compose_theta_a_interval_s3_records(
            assignments, selection, policy_histories, grids_by_history,
            interval_monitor_configs_by_history_ref, interval_monitor_seeds_by_unit,
        )
        candidate = candidate_from_theta_a_interval_records(s3_records)
        sealed = ThetaAIntervalSealer().seal(candidate)
    else:
        if s3_configs_by_history_ref is None or s3_seeds_by_unit is None:
            raise ContractError("point S3 mode requires explicit configs and seeds")
        s3_records = compose_theta_a_s3_observation_records(
            assignments, selection, policy_histories,
            s3_configs_by_history_ref, s3_seeds_by_unit,
        )
        candidate = candidate_from_s3_records(s3_records)
        sealed = ThetaASealer().seal(candidate)
    contract = ThetaAObservationAnalysisContract(
        q_x_mass_by_history=tuple((row.history_ref, row.mass) for row in target_q_x),
        q_x_sha256=digest(target_q_x),
        source_q_x_sha256=assignments.q_x_sha256,
        assignment_bundle_sha256=assignments.result_sha256,
        g_a0_sha256=assignments.g_a0_sha256,
        g_a1_sha256=assignments.g_a1_sha256,
        target_g_a0_sha256=digest(target_g_a0),
        target_g_a1_sha256=digest(target_g_a1),
        source_only_history_refs=tuple(sorted(
            {row.history_ref for row in world.q_x} - target_refs
        )),
        r_common_sha256=assignments.r_common_sha256,
        estimand_id=theta_truth.theta_a_truth.estimand_id,
        estimand_version=theta_truth.theta_a_truth.estimand_version,
        probability_a1_by_history=(
            tuple(
                (history_ref, probability)
                for history_ref, probability in assignment_config.probability_a1_by_history
                if history_ref in target_refs
            )
            if theta_a_confidence_level is not None else ()
        ),
        confidence_level=theta_a_confidence_level,
        unit_independence_certified=theta_a_unit_independence_certified,
        structural_support_contract=theta_a_structural_support_contract,
    )
    analysis = ThetaAObservationAnalyzer().analyze(sealed, contract)
    evaluation = ThetaAObservationEvaluator().evaluate(
        theta_truth, sealed, analysis, assignments, contract,
        tolerance=evaluation_tolerance,
    )

    result = C10SCompleteWorldResult(
        world=world,
        need_pre_z_truth=need_truth,
        structural_pairs=tuple(sorted(structural_pairs.items())),
        structural_deltas=tuple(structural_deltas),
        reachability=reachability,
        trajectories=trajectories,
        d2_vcont_truth=d2_truth,
        d2_observed_lane=d2_observed_lane,
        d2_analysis_contract=d2_contract,
        d2_analyzer_result=d2_analysis,
        d2_evaluator_result=d2_evaluation,
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
        theta_a_structural_support_contract=theta_a_structural_support_contract,
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
    d2_assignment_config: D2ObservedAssignmentConfig,
    d2_interval_monitor_configs_by_history_ref: dict[str, IntervalMonitorConfig] | IntervalMonitorConfig,
    d2_interval_monitor_seeds_by_unit: dict[str, int],
    initial_state_by_unit_z: dict[tuple[str, int], FunctionalState],
    initial_state_by_history: dict[str, FunctionalState],
    need_pre_z_stipulations: Sequence[NeedPreZStipulation],
    grid: IntervalGrid,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    assignment_config: ThetaAPolicyAssignmentConfig,
    s3_configs_by_history_ref: dict[str, object] | None = None,
    s3_seeds_by_unit: dict[str, int] | None = None,
    estimand_version: str,
    outcome_version: str,
    evaluation_tolerance: float,
    interval_monitor_configs_by_history_ref: dict[str, IntervalMonitorConfig] | None = None,
    interval_monitor_seeds_by_unit: dict[str, int] | None = None,
    theta_a_confidence_level: float | None = None,
    theta_a_unit_independence_certified: bool = False,
    theta_a_q_x: Sequence[QXHistoryMass] | None = None,
    theta_a_unit_id_by_history: dict[str, str] | None = None,
    theta_a_structural_support_contract: ThetaAStructuralSupportContract | None = None,
    theta_a_target_history_materializations: Sequence[SyntheticThetaATargetHistory] = (),
) -> C10SCompleteWorldResult:
    """Generate D2 and direct-g_A potential EventHistories inside the DGP pipeline.

    Functional rules, rather than implicit accessibility/admission equivalence,
    determine ENABLED/admission. The legacy composer receives only generated
    potential histories; S3 still sees only the realized-history projection.
    """
    builder = SyntheticWorldBuilder()
    world, _, _, trajectory_bundle = builder.generate_complete_with_trajectories(
        world_config, d2_config, structural_config, reach_config, trajectory_config,
    )
    trajectory_rules_declared = any(
        rule.source == "TRAJECTORY" for rule in functional_history_config.rules
    )
    trajectory_map = {
        (row.unit_id, row.z, row.target_state): row
        for row in trajectory_bundle.trajectories
    }
    d2_histories = generate_d2_event_history_potentials(
        world, functional_history_config, initial_state_by_unit_z,
        trajectories_by_unit_z_target=trajectory_map if trajectory_rules_declared else None,
    )
    if (theta_a_q_x is None) != (theta_a_unit_id_by_history is None):
        raise ContractError("independent target q_X and target-unit identities must be supplied together")
    target_unit_ids = theta_a_unit_id_by_history or {
        unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
    }
    target_q_x_rows = tuple(theta_a_q_x) if theta_a_q_x is not None else world.q_x
    target_refs = {row.history_ref for row in target_q_x_rows}
    source_unit_ids = {
        unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
    }
    source_refs = set(source_unit_ids)
    if set(target_unit_ids) != target_refs:
        raise ContractError("DGP target q_X and target unit identities must cover the same histories")
    # Assignment/realized-history materialization spans the source roster plus
    # target-only histories. The target unit map alone is not sufficient when
    # q_X* is a strict subset of source support: source-only units still receive
    # randomized assignments and require their generated functional histories.
    policy_unit_ids = dict(source_unit_ids)
    for history_ref in target_refs - source_refs:
        policy_unit_ids[history_ref] = target_unit_ids[history_ref]
    if set(initial_state_by_history) != source_refs | target_refs:
        raise ContractError(
            "DGP functional initial states must cover source histories plus target-only histories exactly"
        )
    materializations = {row.q_x.history_ref: row for row in theta_a_target_history_materializations}
    if len(materializations) != len(theta_a_target_history_materializations):
        raise ContractError("target-only baseline materializations must have unique history identities")
    target_only_refs = target_refs - source_refs
    if set(materializations) != target_only_refs:
        raise ContractError("every and only target-only histories require an explicit typed baseline materialization")
    for row in target_q_x_rows:
        if row.history_ref in source_refs:
            source_unit = next(unit for unit in world.units
                               if unit.d2_baseline.baseline_history_ref == row.history_ref)
            if (row.x_ref, row.h0_ref, row.c_c_ref) != (
                    source_unit.x_ref, source_unit.h0_ref, source_unit.c_c_ref):
                raise ContractError("overlapping target history anchors must reproduce source baseline anchors")
            if target_unit_ids[row.history_ref] != source_unit.unit_id:
                raise ContractError("overlapping target history identity must retain its source unit identity")
        else:
            materialization = materializations[row.history_ref]
            materialization.validate(
                source_world=world,
                allowed_h0_values={label for label, _ in world_config.h0_distribution},
            )
            if materialization.q_x != row or materialization.potential_unit_id != target_unit_ids[row.history_ref]:
                raise ContractError("typed target-only baseline identity differs from target q_X/unit map")
            if initial_state_by_history.get(row.history_ref) != materialization.initial_functional_state:
                raise ContractError("target-only initial functional state must come from its typed baseline materialization")
    policy_histories = generate_g_a_event_history_potentials(
        world, functional_history_config, g_a0, g_a1,
        r_common_certificates, initial_state_by_history,
        unit_id_by_history=policy_unit_ids,
    )
    return materialize_c10s_complete_world(
        world_config=world_config, d2_config=d2_config,
        structural_config=structural_config, reach_config=reach_config,
        trajectory_config=trajectory_config,
        d2_histories_by_unit_z=d2_histories,
        d2_assignment_config=d2_assignment_config,
        d2_interval_monitor_configs_by_history_ref=d2_interval_monitor_configs_by_history_ref,
        d2_interval_monitor_seeds_by_unit=d2_interval_monitor_seeds_by_unit,
        need_pre_z_stipulations=need_pre_z_stipulations, grid=grid,
        g_a0=g_a0, g_a1=g_a1,
        feasible_vectors_by_history=feasible_vectors_by_history,
        r_common_certificates=r_common_certificates,
        event_histories_by_policy=policy_histories,
        assignment_config=assignment_config,
        s3_configs_by_history_ref=s3_configs_by_history_ref,
        s3_seeds_by_unit=s3_seeds_by_unit,
        estimand_version=estimand_version, outcome_version=outcome_version,
        evaluation_tolerance=evaluation_tolerance,
        interval_monitor_configs_by_history_ref=interval_monitor_configs_by_history_ref,
        interval_monitor_seeds_by_unit=interval_monitor_seeds_by_unit,
        theta_a_confidence_level=theta_a_confidence_level,
        theta_a_unit_independence_certified=theta_a_unit_independence_certified,
        theta_a_q_x=theta_a_q_x,
        theta_a_unit_id_by_history=target_unit_ids,
        theta_a_structural_support_contract=theta_a_structural_support_contract,
    )
