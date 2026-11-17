"""Two-cohort integration for D2 package ITT-Z and focal factorial A×M.

Both cohorts are materialized by the same DGP specification and paired baseline
draws, but have disjoint unit/roster/world identities and independent randomized
assignments. A unit is never assigned in both experimental lanes.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from c10s_synthetic_components import (
    ContractError, D2MechanismConfig, D2VContTruthBundle, EventHistory,
    IntervalGrid, SyntheticWorldBuilder, SyntheticWorldBundle, SyntheticWorldConfig,
)
from c10s_functional_history import (
    FunctionalHistoryDGPConfig, generate_d2_event_history_potentials,
)
from theta_a_interval_observation import IntervalMonitorConfig
from d2_observed_assignment import D2ObservedAssignmentConfig
from d2_interval_observation import (
    D2ObservedIntervalLaneResult, materialize_d2_observed_interval_lane,
)
from d2_ittz_analyzer import (
    D2ITTZAnalysisContract, D2ITTZAnalysisResult, D2ITTZAnalyzer,
    analysis_contract_from_world,
)
from d2_ittz_evaluator import D2ITTZEvaluation, D2ITTZEvaluator
from c10s_factorial_pipeline import (
    C10SFactorialWorldResult, materialize_c10s_factorial_world_from_dgp,
)


@dataclass(frozen=True)
class C10SDualCohortWorldResult:
    factorial_cohort: C10SFactorialWorldResult
    d2_world: SyntheticWorldBundle
    d2_event_histories_by_unit_z: dict[tuple[str, int], EventHistory]
    d2_vcont_truth: D2VContTruthBundle
    d2_observed_lane: D2ObservedIntervalLaneResult
    d2_analysis_contract: D2ITTZAnalysisContract
    d2_analyzer_result: D2ITTZAnalysisResult
    d2_evaluator_result: D2ITTZEvaluation

    def validate(self, grid: IntervalGrid) -> None:
        grid.validate()
        self.factorial_cohort.validate(grid)
        self.d2_world.validate()
        expected = {
            (unit.unit_id, z) for unit in self.d2_world.units for z in (0, 1)
        }
        if set(self.d2_event_histories_by_unit_z) != expected:
            raise ContractError("D2 cohort must retain exact unit × Z potential EventHistory coverage")
        self.d2_vcont_truth.validate(self.d2_world, self.d2_event_histories_by_unit_z, grid)
        self.d2_observed_lane.validate(
            self.d2_world, self.d2_vcont_truth,
            self.d2_event_histories_by_unit_z, grid,
        )
        if self.factorial_cohort.world.world_id == self.d2_world.world_id:
            raise ContractError("D2 and A×M cohorts must have distinct world identities")
        if self.factorial_cohort.world.roster_id == self.d2_world.roster_id:
            raise ContractError("D2 and A×M cohorts must have distinct roster identities")
        if (self.factorial_cohort.world.dgp_id, self.factorial_cohort.world.dgp_version) != (
            self.d2_world.dgp_id, self.d2_world.dgp_version
        ):
            raise ContractError("D2 and A×M cohorts must use the same DGP identity/version")
        _validate_paired_baseline(self.factorial_cohort.world, self.d2_world)
        if self.d2_analysis_contract.assignment_bundle_sha256 != self.d2_observed_lane.assignments.result_sha256:
            raise ContractError("D2 ITT-Z analysis contract is detached from the observed assignment")
        if self.d2_analyzer_result.input_sha256 != self.d2_observed_lane.sealed_evidence.sha256:
            raise ContractError("D2 ITT-Z Analyzer result is detached from sealed S3 evidence")
        if self.d2_evaluator_result.analyzer_output_sha256 != self.d2_analyzer_result.output_sha256:
            raise ContractError("D2 ITT-Z Evaluator result is detached from Analyzer output")
        if self.d2_evaluator_result.evidence_sha256 != self.d2_observed_lane.sealed_evidence.sha256:
            raise ContractError("D2 ITT-Z Evaluator result is detached from sealed S3 evidence")
        factorial_run_ids = {
            history.run_id for history in self.factorial_cohort.factorial_potential_histories.values()
        }
        d2_run_ids = {history.run_id for history in self.d2_event_histories_by_unit_z.values()}
        if len(factorial_run_ids) != 1 or d2_run_ids != factorial_run_ids:
            raise ContractError("both experimental cohorts must share one run identity")


def _validate_paired_baseline(
    factorial_world: SyntheticWorldBundle,
    d2_world: SyntheticWorldBundle,
) -> None:
    if len(factorial_world.units) != len(d2_world.units):
        raise ContractError("paired experimental cohorts must have equal roster sizes")
    if factorial_world.seed_commitment_sha256 != d2_world.seed_commitment_sha256:
        raise ContractError("paired cohorts must share the same baseline exogenous seed commitment")
    if tuple(row.mass for row in factorial_world.q_x) != tuple(row.mass for row in d2_world.q_x):
        raise ContractError("paired cohorts must use identical q_X* target masses")
    f_ids = {unit.unit_id for unit in factorial_world.units}
    d_ids = {unit.unit_id for unit in d2_world.units}
    f_refs = {row.history_ref for row in factorial_world.q_x}
    d_refs = {row.history_ref for row in d2_world.q_x}
    if f_ids & d_ids or f_refs & d_refs:
        raise ContractError("experimental cohort unit IDs and baseline-history refs must be disjoint")
    baseline_fields = (
        "focal_accessible_pre", "c_auth_base", "c_resource", "c_capacity",
        "c_info", "c_domain", "c_other",
    )
    for f_unit, d_unit in zip(factorial_world.units, d2_world.units):
        if (f_unit.x, f_unit.h0, f_unit.c_c, f_unit.need_pre_z) != (
            d_unit.x, d_unit.h0, d_unit.c_c, d_unit.need_pre_z
        ):
            raise ContractError("paired cohorts do not share the same baseline X/H0/C_c/need draws")
        if tuple(getattr(f_unit.d2_baseline, name) for name in baseline_fields) != tuple(
            getattr(d_unit.d2_baseline, name) for name in baseline_fields
        ):
            raise ContractError("paired cohorts have different D2 baseline predicates")
        if f_unit.d2_potentials.exogenous_draws_sha256 != d_unit.d2_potentials.exogenous_draws_sha256:
            raise ContractError("paired cohorts do not share the same D2 exogenous potential draws")


def materialize_c10s_dual_cohort_world_from_dgp(
    *,
    factorial_world_config: SyntheticWorldConfig,
    d2_world_config: SyntheticWorldConfig,
    d2_config: D2MechanismConfig,
    structural_config,
    reach_config,
    trajectory_config,
    functional_history_config: FunctionalHistoryDGPConfig,
    factorial_initial_state_by_unit_z,
    d2_initial_state_by_unit_z,
    initial_state_by_history,
    grid: IntervalGrid,
    g_a0,
    g_a1,
    feasible_vectors_by_history,
    r_common_certificates,
    factorial_assignment_config,
    d2_assignment_config: D2ObservedAssignmentConfig,
    factorial_grids_by_history_ref,
    factorial_interval_monitor_configs_by_history_ref,
    factorial_interval_monitor_seeds_by_unit,
    d2_interval_monitor_configs_by_history_ref: Mapping[str, IntervalMonitorConfig],
    d2_interval_monitor_seeds_by_unit: dict[str, int],
    estimand_version: str,
    evaluation_tolerance: float,
) -> C10SDualCohortWorldResult:
    """Build paired, disjoint cohorts and integrate both sealed causal lanes."""
    if (factorial_world_config.world_id, factorial_world_config.roster_id,
            factorial_world_config.unit_id_prefix) == (
        d2_world_config.world_id, d2_world_config.roster_id,
        d2_world_config.unit_id_prefix
    ):
        raise ContractError("D2 and A×M cohort world/roster/unit namespaces must be distinct")
    if (factorial_world_config.seed, factorial_world_config.n_units) != (
        d2_world_config.seed, d2_world_config.n_units
    ):
        raise ContractError("paired cohorts require the same baseline seed and roster size")
    if (factorial_world_config.dgp_id, factorial_world_config.dgp_version) != (
        d2_world_config.dgp_id, d2_world_config.dgp_version
    ):
        raise ContractError("both cohorts must bind to the same DGP identity/version")
    if (functional_history_config.dgp_id, functional_history_config.dgp_version) != (
        d2_world_config.dgp_id, d2_world_config.dgp_version
    ):
        raise ContractError("functional EventHistory generator must bind to the cohort DGP")
    factorial = materialize_c10s_factorial_world_from_dgp(
        world_config=factorial_world_config, d2_config=d2_config,
        structural_config=structural_config, reach_config=reach_config,
        trajectory_config=trajectory_config,
        functional_history_config=functional_history_config,
        initial_state_by_unit_z=factorial_initial_state_by_unit_z,
        initial_state_by_history=initial_state_by_history, grid=grid,
        g_a0=g_a0, g_a1=g_a1,
        feasible_vectors_by_history=feasible_vectors_by_history,
        r_common_certificates=r_common_certificates,
        assignment_config=factorial_assignment_config,
        grids_by_history_ref=factorial_grids_by_history_ref,
        interval_monitor_configs_by_history_ref=factorial_interval_monitor_configs_by_history_ref,
        interval_monitor_seeds_by_unit=factorial_interval_monitor_seeds_by_unit,
        estimand_version=estimand_version,
        evaluation_tolerance=evaluation_tolerance,
    )
    builder = SyntheticWorldBuilder()
    d2_world = builder.generate(d2_world_config, d2_config)
    _validate_paired_baseline(factorial.world, d2_world)
    d2_histories = generate_d2_event_history_potentials(
        d2_world, functional_history_config, d2_initial_state_by_unit_z,
    )
    d2_truth = builder.evaluate_complete_vcont_truth(d2_world, d2_histories, grid)
    d2_lane = materialize_d2_observed_interval_lane(
        world=d2_world, truth=d2_truth, histories_by_unit_z=d2_histories,
        assignment_config=d2_assignment_config, grid=grid,
        monitor_config_by_history_ref=d2_interval_monitor_configs_by_history_ref,
        seeds_by_unit=d2_interval_monitor_seeds_by_unit,
    )
    analysis_contract = analysis_contract_from_world(
        d2_world, d2_lane.assignments.result_sha256,
        d2_lane.assignments.mechanism_id, d2_lane.assignments.mechanism_version,
    )
    analyzer_result = D2ITTZAnalyzer().analyze(
        d2_lane.sealed_evidence, analysis_contract,
    )
    evaluator_result = D2ITTZEvaluator().evaluate(
        world=d2_world, truth=d2_truth, assignments=d2_lane.assignments,
        evidence=d2_lane.sealed_evidence, contract=analysis_contract,
        result=analyzer_result, tolerance=evaluation_tolerance,
    )
    result = C10SDualCohortWorldResult(
        factorial, d2_world, d2_histories, d2_truth, d2_lane,
        analysis_contract, analyzer_result, evaluator_result,
    )
    result.validate(grid)
    return result
