"""Integrated DGP-to-observation factorial A×M pipeline for C10-S.

This is a design/materialization function only. Calling it constructs synthetic
objects in memory; it does not run tests, Monte Carlo repetitions, or external
scientific executions. Analyzer receives only sealed realized S3 evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from c10s_synthetic_components import (
    D2MechanismConfig, D2ReachGenerationConfig, D2StructuralGenerationConfig,
    D2VContTruthBundle,
    D2TrajectoryGenerationConfig, EventHistory, IntervalGrid, ContractError,
    JointPolicyHistory, RCommonPairCertificate, SyntheticWorldBuilder,
    SyntheticWorldConfig, Vector4, GAStructuralTransitionRule,
    FactorialStructuralPotential, FactorialReachPotential, FactorialPotentialTrajectory,
    evaluate_d2_structural_deltas, generate_factorial_structural_potentials,
    evaluate_factorial_structural_reachability, evaluate_factorial_potential_trajectories,
)
from c10s_functional_history import (
    FunctionalHistoryDGPConfig, generate_d2_event_history_potentials,
)
from theta_a_interval_observation import IntervalMonitorConfig
from theta_am_factorial import (
    FactorialAnalysisContract, FactorialAnalysisResult, FactorialAssignmentConfig,
    FactorialAssignmentBundle, FactorialEvaluationResult, FactorialHistorySelection,
    FactorialIntervalObservationRecord, FactorialObservationAnalyzer,
    FactorialIntervalSealer, FactorialTruthBundle, SealedFactorialEvidence,
    compose_factorial_interval_s3_records, compute_factorial_vcont_truth_from_event_histories,
    evaluate_factorial_analysis, factorial_candidate_from_records,
    materialize_factorial_potentials,
)


@dataclass(frozen=True)
class C10SFactorialWorldResult:
    world: object
    structural: object
    structural_deltas: tuple[object, ...]
    reach: object
    trajectories: object
    d2_event_histories_by_unit_z: dict[tuple[str, int], EventHistory]
    d2_vcont_truth: D2VContTruthBundle
    factorial_potential_histories: dict[tuple[str, str, str, int], EventHistory]
    assignment_bundle: FactorialAssignmentBundle
    realized_histories: tuple[EventHistory, ...]
    history_selection: FactorialHistorySelection
    interval_observations: tuple[FactorialIntervalObservationRecord, ...]
    sealed_evidence: SealedFactorialEvidence
    analysis_contract: FactorialAnalysisContract
    analyzer_result: FactorialAnalysisResult
    reserved_truth: FactorialTruthBundle
    evaluator_result: FactorialEvaluationResult
    factorial_structural_potentials: dict[tuple[str, str, str], FactorialStructuralPotential]
    factorial_reach_potentials: dict[tuple[str, str, str], FactorialReachPotential]
    factorial_trajectories: dict[tuple[str, str, str, str], FactorialPotentialTrajectory]
    factorial_target_states: tuple[str, ...]
    factorial_reach_config: D2ReachGenerationConfig

    @property
    def accessibility_attribution_status(self) -> str:
        """Current causal scope of the factorial result.

        Structural ΔT_acc*, Reach and trajectory potentials are generated per
        supported q_X* × complete g_A vector × r_common potential. This closes
        the structural path only; Outcome/Value composition and causal Analyzer
        identification remain open.
        """
        return "GA_TO_DELTA_T_ACC_REACH_TRAJECTORY_MATERIALIZED_VALUE_BRIDGE_OPEN"

    def require_accessibility_attribution(self) -> None:
        """Fail closed if a caller attempts to treat the V_cont contrast as θ_A on ΔT_acc*."""
        raise ContractError(
            "full accessibility-to-Value attribution is not established: the structural "
            "g_A-to-ΔT_acc*-to-Reach-to-trajectory chain is materialized, but Outcome/Value "
            "composition and Analyzer identification are not yet validated"
        )

    def validate(self, grid: IntervalGrid) -> None:
        self.world.validate()
        grid.validate()
        structural_pairs = dict(self.structural)
        expected_structural = {
            (unit.unit_id, z) for unit in self.world.units for z in (0, 1)
        }
        if set(structural_pairs) != expected_structural or len(structural_pairs) != len(self.structural):
            raise ContractError("factorial cohort must retain exact unit × Z structural-pair coverage")
        delta_by_key = {(row.unit_id, row.potential_z): row for row in self.structural_deltas}
        if set(delta_by_key) != expected_structural or len(delta_by_key) != len(self.structural_deltas):
            raise ContractError("factorial cohort must retain exact unit × Z ΔT_acc* coverage")
        for key in expected_structural:
            pair, delta = structural_pairs[key], delta_by_key[key]
            if (delta.baseline_snapshot_id, delta.post_snapshot_id) != (
                pair.baseline.snapshot_id, pair.post.snapshot_id
            ):
                raise ContractError("factorial ΔT_acc* is detached from its exact structural potential snapshots")
        self.reach.validate(self.world)
        reach_by_key = {(row.unit_id, row.z): row for row in self.reach.contrasts}
        if set(reach_by_key) != expected_structural or len(reach_by_key) != len(expected_structural):
            raise ContractError("factorial cohort must retain exact unit × Z Reach coverage")
        for key in expected_structural:
            pair, reach = structural_pairs[key], reach_by_key[key]
            if (reach.baseline.snapshot_id, reach.post.snapshot_id) != (
                pair.baseline.snapshot_id, pair.post.snapshot_id
            ):
                raise ContractError("factorial Reach is detached from its exact structural potential snapshots")
        expected_factorial_support = {
            (row[0], row[1], row[2])
            for row in self.factorial_potential_histories
        }
        if set(self.factorial_structural_potentials) != expected_factorial_support:
            raise ContractError("g_A structural potentials must cover exact positive-mass vector × r_common support")
        if set(self.factorial_reach_potentials) != expected_factorial_support:
            raise ContractError("g_A Reach potentials must cover exact structural potential support")
        mapping_identities = {
            (row.mapping_id, row.mapping_version, row.mapping_sha256)
            for row in self.factorial_structural_potentials.values()
        }
        if len(mapping_identities) != 1:
            raise ContractError("all factorial structural potentials must share one exact versioned g_A mapping")
        if (not self.factorial_target_states
                or len(self.factorial_target_states) != len(set(self.factorial_target_states))
                or self.factorial_target_states != self.factorial_reach_config.target_states):
            raise ContractError("factorial trajectory target universe must match its exact versioned Reach configuration")
        expected_factorial_trajectories = {
            (history_ref, vector_sha, regime, target)
            for history_ref, vector_sha, regime in expected_factorial_support
            for target in self.factorial_target_states
        }
        if set(self.factorial_trajectories) != expected_factorial_trajectories:
            raise ContractError("g_A trajectories must cover exact vector-potential × target support")
        for key, potential in self.factorial_structural_potentials.items():
            potential.validate(self.world)
            if key != (potential.history_ref, potential.vector_sha256, potential.r_common_fingerprint):
                raise ContractError("g_A structural potential key/provenance mismatch")
            reach_potential = self.factorial_reach_potentials[key]
            reach_potential.validate(potential, self.factorial_reach_config)
            for target in self.factorial_target_states:
                self.factorial_trajectories[(*key, target)].validate(reach_potential)
        expected_d2 = {
            (unit.unit_id, z) for unit in self.world.units for z in (0, 1)
        }
        if set(self.d2_event_histories_by_unit_z) != expected_d2:
            raise ContractError("factorial result must retain exact unit × Z D2 potential-history coverage")
        self.d2_vcont_truth.validate(
            self.world, self.d2_event_histories_by_unit_z, grid,
        )
        self.reserved_truth.validate()
        if self.history_selection.assignment_bundle_sha256 != self.assignment_bundle.result_sha256:
            raise ContractError("factorial realized-history selection is detached from assignment bundle")
        if not self.sealed_evidence.rows or self.sealed_evidence.sha256 != self.analyzer_result.input_sha256:
            raise ContractError("factorial Analyzer result is detached from sealed S3 evidence")
        if self.evaluator_result.evidence_sha256 != self.sealed_evidence.sha256:
            raise ContractError("factorial Evaluator result is detached from sealed S3 evidence")
        if self.evaluator_result.analyzer_output_sha256 != self.analyzer_result.output_sha256:
            raise ContractError("factorial Evaluator result is detached from Analyzer output")
        for assignment in self.assignment_bundle.assignments:
            assigned_structural_key = (
                assignment.history_ref, assignment.assigned_vector_sha256,
                assignment.r_common_fingerprint,
            )
            if assigned_structural_key not in self.factorial_structural_potentials:
                raise ContractError("realized factorial assignment has no matching structural g_A potential")
        for history_key, history in self.factorial_potential_histories.items():
            history_ref, vector_sha, regime_fingerprint, m_arm = history_key
            structural_potential = self.factorial_structural_potentials.get(
                (history_ref, vector_sha, regime_fingerprint),
            )
            if structural_potential is None:
                raise ContractError("factorial EventHistory has no matching structural g_A potential")
            expected_potential_id = (
                f"{structural_potential.unit_id}:G_AxM:{self.assignment_bundle.factor_m_id}:"
                f"{self.assignment_bundle.factor_m_version}:{vector_sha}:{regime_fingerprint}:M{m_arm}"
            )
            if (history.unit_id, history.potential_id, history.world_id,
                    history.world_version, history.dgp_version) != (
                    structural_potential.unit_id, expected_potential_id,
                    self.world.world_id, self.world.world_version, self.world.dgp_version):
                raise ContractError("factorial EventHistory is detached from its exact structural vector potential")
        run_ids = {history.run_id for history in self.d2_event_histories_by_unit_z.values()}
        run_ids.update(history.run_id for history in self.factorial_potential_histories.values())
        if len(run_ids) != 1 or self.sealed_evidence.run_id not in run_ids:
            raise ContractError("factorial D2, A×M potentials and sealed observations must share one run identity")


def materialize_c10s_factorial_world_from_dgp(
    *,
    world_config: SyntheticWorldConfig,
    d2_config: D2MechanismConfig,
    structural_config: D2StructuralGenerationConfig,
    reach_config: D2ReachGenerationConfig,
    trajectory_config: D2TrajectoryGenerationConfig,
    functional_history_config: FunctionalHistoryDGPConfig,
    initial_state_by_unit_z,
    initial_state_by_history,
    grid: IntervalGrid,
    g_a0: Sequence[JointPolicyHistory],
    g_a1: Sequence[JointPolicyHistory],
    g_a_structural_rules: Sequence[GAStructuralTransitionRule],
    g_a_structural_mapping_id: str,
    g_a_structural_mapping_version: str,
    feasible_vectors_by_history: dict[str, tuple[Vector4, ...]],
    r_common_certificates: Sequence[RCommonPairCertificate],
    assignment_config: FactorialAssignmentConfig,
    grids_by_history_ref: dict[str, IntervalGrid],
    interval_monitor_configs_by_history_ref: dict[str, IntervalMonitorConfig],
    interval_monitor_seeds_by_unit: dict[str, int],
    estimand_version: str,
    evaluation_tolerance: float,
) -> C10SFactorialWorldResult:
    """Materialize one complete synthetic world and its randomized 2×2 A×M path.

    Cell assignment probabilities are declared per q_X history and all four
    cells must have positive support. Four potential functional histories are
    generated within the same world and common-r regime. Only the selected
    history is projected to S3; the reserved potential histories remain
    evaluator-side.
    """
    grid.validate()
    builder = SyntheticWorldBuilder()
    world, structural, reach, trajectories = builder.generate_complete_with_trajectories(
        world_config, d2_config, structural_config, reach_config, trajectory_config,
    )
    expected_refs = {row.history_ref for row in world.q_x}
    if set(grids_by_history_ref) != expected_refs or set(interval_monitor_configs_by_history_ref) != expected_refs:
        raise ContractError("factorial S3 grids and monitor configurations must cover q_X* exactly")
    for candidate_grid in grids_by_history_ref.values():
        candidate_grid.validate()
        if (candidate_grid.grid_id, candidate_grid.grid_version, candidate_grid.boundaries) != (
            grid.grid_id, grid.grid_version, grid.boundaries
        ):
            raise ContractError("factorial truth and observed S3 must share the exact same interval grid")
    if set(interval_monitor_seeds_by_unit) != {unit.unit_id for unit in world.units}:
        raise ContractError("factorial interval-monitor seeds must cover the exact world roster")
    trajectory_rules_declared = any(
        rule.source == "TRAJECTORY" for rule in functional_history_config.rules
    )
    trajectory_map = {
        (row.unit_id, row.z, row.target_state): row
        for row in trajectories.trajectories
    }
    d2_histories = generate_d2_event_history_potentials(
        world, functional_history_config, initial_state_by_unit_z,
        trajectories_by_unit_z_target=trajectory_map if trajectory_rules_declared else None,
    )
    # Keep the D2 package-level ITT-Z truth as a distinct oracle output.
    # It is not substituted for either focal A simple effect or the A×M interaction.
    d2_vcont_truth = builder.evaluate_complete_vcont_truth(world, d2_histories, grid)
    d2_vcont_truth.validate(world, d2_histories, grid)
    structural_deltas = evaluate_d2_structural_deltas(world, structural)
    factorial_structural = generate_factorial_structural_potentials(
        world, structural_config, g_a0, g_a1, feasible_vectors_by_history,
        r_common_certificates, g_a_structural_rules,
        mapping_id=g_a_structural_mapping_id,
        mapping_version=g_a_structural_mapping_version,
    )
    factorial_reach = evaluate_factorial_structural_reachability(
        world, factorial_structural, reach_config,
    )
    factorial_trajectories = evaluate_factorial_potential_trajectories(
        world, factorial_reach, reach_config, trajectory_config,
    )
    trajectory_rules_declared = any(
        rule.source == "TRAJECTORY" for rule in functional_history_config.rules
    )
    factorial_trajectory_map = factorial_trajectories if trajectory_rules_declared else None
    potentials, assignments, realized, selection = materialize_factorial_potentials(
        world, functional_history_config, g_a0, g_a1, r_common_certificates,
        initial_state_by_history, feasible_vectors_by_history, assignment_config,
        trajectories_by_history_vector_target=factorial_trajectory_map,
    )
    interval_records = compose_factorial_interval_s3_records(
        assignments, selection, realized, grids_by_history_ref,
        interval_monitor_configs_by_history_ref, interval_monitor_seeds_by_unit,
    )
    candidate = factorial_candidate_from_records(interval_records)
    sealed = FactorialIntervalSealer().seal(candidate)
    analysis_contract = FactorialAnalysisContract(
        q_x_mass_by_history=tuple((row.history_ref, row.mass) for row in world.q_x),
        expected_unit_ids=tuple(unit.unit_id for unit in world.units),
        probability_by_history=assignment_config.probability_by_history,
        q_x_sha256=assignments.q_x_sha256,
        assignment_bundle_sha256=assignments.result_sha256,
        g_a0_sha256=assignments.g_a0_sha256,
        g_a1_sha256=assignments.g_a1_sha256,
        r_common_sha256=assignments.r_common_sha256,
        factor_m_id=assignments.factor_m_id,
        factor_m_version=assignments.factor_m_version,
        factor_m_sha256=assignments.factor_m_sha256,
        estimand_version=estimand_version,
    )
    analyzer_result = FactorialObservationAnalyzer().analyze(sealed, analysis_contract)
    truth = compute_factorial_vcont_truth_from_event_histories(
        world, world.q_x, g_a0, g_a1, r_common_certificates,
        potentials, grid, factor_m_id=assignment_config.factor_m_id,
        factor_m_version=assignment_config.factor_m_version,
        estimand_version=estimand_version,
    )
    evaluation = evaluate_factorial_analysis(
        truth, sealed, analyzer_result, assignments, tolerance=evaluation_tolerance,
    )
    result = C10SFactorialWorldResult(
        world=world,
        structural=structural,
        structural_deltas=tuple(structural_deltas),
        reach=reach,
        trajectories=trajectories,
        d2_event_histories_by_unit_z=d2_histories,
        d2_vcont_truth=d2_vcont_truth,
        factorial_potential_histories=potentials,
        assignment_bundle=assignments,
        realized_histories=realized,
        history_selection=selection,
        interval_observations=interval_records,
        sealed_evidence=sealed,
        analysis_contract=analysis_contract,
        analyzer_result=analyzer_result,
        reserved_truth=truth,
        evaluator_result=evaluation,
        factorial_structural_potentials=factorial_structural,
        factorial_reach_potentials=factorial_reach,
        factorial_trajectories=factorial_trajectories,
        factorial_target_states=reach_config.target_states,
        factorial_reach_config=reach_config,
    )
    result.validate(grid)
    return result
