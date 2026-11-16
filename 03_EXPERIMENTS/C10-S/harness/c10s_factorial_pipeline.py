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
    SyntheticWorldConfig, Vector4,
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

    def validate(self, grid: IntervalGrid) -> None:
        self.world.validate()
        grid.validate()
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
        if not self.evaluator_result.correct_adjudication:
            raise ContractError("factorial Evaluator rejected the Analyzer result")
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
    d2_histories = generate_d2_event_history_potentials(
        world, functional_history_config, initial_state_by_unit_z,
    )
    # Keep the D2 package-level ITT-Z truth as a distinct oracle output.
    # It is not substituted for either focal A simple effect or the A×M interaction.
    d2_vcont_truth = builder.evaluate_complete_vcont_truth(world, d2_histories, grid)
    d2_vcont_truth.validate(world, d2_histories, grid)
    potentials, assignments, realized, selection = materialize_factorial_potentials(
        world, functional_history_config, g_a0, g_a1, r_common_certificates,
        initial_state_by_history, feasible_vectors_by_history, assignment_config,
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
        world, structural, reach, trajectories, d2_histories, d2_vcont_truth, potentials,
        assignments, realized, selection, interval_records, sealed,
        analysis_contract, analyzer_result, truth, evaluation,
    )
    result.validate(grid)
    return result
