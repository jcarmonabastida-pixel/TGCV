"""Independent oracle-side evaluator for the D2 observed ITT-Z Analyzer."""
from __future__ import annotations

from dataclasses import dataclass
import math

from c10s_synthetic_components import ContractError, D2VContTruthBundle, SyntheticWorldBundle, digest
from d2_interval_observation import SealedD2IntervalEvidence, _hash
from d2_observed_assignment import D2ObservedAssignmentBundle
from d2_ittz_analyzer import (
    D2ITTZAnalysisContract, D2ITTZAnalysisResult, _output_hash,
)


@dataclass(frozen=True)
class D2ITTZEvaluation:
    run_id: str
    truth_itt_z: float
    analyzer_identification: str
    point_estimate: float | None
    lower_bound: float
    upper_bound: float
    absolute_error: float | None
    truth_within_bounds: bool | None
    correct_adjudication: bool
    disposition: str
    tolerance: float
    evidence_sha256: str
    analyzer_output_sha256: str


class D2ITTZEvaluator:
    """The only component in this lane allowed to inspect reserved D2 truth."""

    version = "c10s-d2-ittz-evaluator-0.1"

    def evaluate(
        self,
        *,
        world: SyntheticWorldBundle,
        truth: D2VContTruthBundle,
        assignments: D2ObservedAssignmentBundle,
        evidence: SealedD2IntervalEvidence,
        contract: D2ITTZAnalysisContract,
        result: D2ITTZAnalysisResult,
        tolerance: float = 1e-10,
    ) -> D2ITTZEvaluation:
        world.validate()
        if not math.isfinite(tolerance) or tolerance < 0:
            raise ContractError("ITT-Z evaluator tolerance must be finite and non-negative")
        if (truth.world_id, truth.world_version, truth.dgp_id, truth.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("reserved ITT-Z truth belongs to a different world/DGP")
        if truth.q_x_sha256 != digest(world.q_x):
            raise ContractError("reserved ITT-Z truth q_X fingerprint differs from world")
        if (assignments.world_id, assignments.world_version, assignments.dgp_id, assignments.dgp_version) != (
            world.world_id, world.world_version, world.dgp_id, world.dgp_version
        ):
            raise ContractError("D2 assignment belongs to a different world/DGP")
        if assignments.q_x_sha256 != digest(world.q_x):
            raise ContractError("D2 assignment q_X fingerprint differs from world")
        if (contract.assignment_bundle_sha256 != assignments.result_sha256
                or contract.q_x_sha256 != assignments.q_x_sha256
                or contract.assignment_mechanism_id != assignments.mechanism_id
                or contract.assignment_mechanism_version != assignments.mechanism_version):
            raise ContractError("ITT-Z analysis contract differs from the realized assignment bundle")
        if result.run_id != evidence.run_id or result.input_sha256 != evidence.sha256:
            raise ContractError("ITT-Z Analyzer result is not bound to supplied evidence")
        if _hash({"manifest": evidence.manifest, "rows": list(evidence.rows)}) != evidence.sha256:
            raise ContractError("sealed D2 interval evidence digest is invalid")
        if _output_hash({
            "run_id": result.run_id, "estimand_id": result.estimand_id,
            "estimand_version": result.estimand_version,
            "identification": result.identification, "point_estimate": result.point_estimate,
            "lower_bound": result.lower_bound, "upper_bound": result.upper_bound,
            "randomization_lower_bound": result.randomization_lower_bound,
            "randomization_upper_bound": result.randomization_upper_bound,
            "hoeffding_radius": result.hoeffding_radius,
            "randomization_confidence_level": result.randomization_confidence_level,
            "target_q_x_coverage": result.target_q_x_coverage,
            "missing_target_histories": result.missing_target_histories,
            "assigned_z_unit_counts": result.assigned_z_unit_counts,
            "missing_interval_count": result.missing_interval_count,
            "total_interval_count": result.total_interval_count,
            "abstention_reason": result.abstention_reason,
            "input_sha256": result.input_sha256,
        }) != result.output_sha256:
            raise ContractError("ITT-Z Analyzer result fingerprint is invalid")
        if (result.estimand_id, result.estimand_version) != (
            contract.estimand_id, contract.estimand_version
        ):
            raise ContractError("ITT-Z Analyzer estimand identity/version mismatch")
        assignments_by_unit = {row.unit_id: row for row in assignments.assignments}
        evidence_units = {row["unit_id"] for row in evidence.rows}
        if evidence_units != set(assignments_by_unit):
            raise ContractError("D2 S3 evidence must cover exactly the randomized assignment roster")
        truth_rows = {(row.unit_id, row.z): row for row in truth.potential_truth}
        for unit_id, assignment in assignments_by_unit.items():
            selected_truth = truth_rows[(unit_id, assignment.assigned_z)]
            rows = [row for row in evidence.rows if row["unit_id"] == unit_id]
            if any((row["assigned_z"], row["selected_potential_id"], row["history_id"],
                    row["history_content_sha256"]) != (
                    assignment.assigned_z, selected_truth.potential_id,
                    selected_truth.history_id, selected_truth.history_content_sha256
                    ) for row in rows):
                raise ContractError("D2 observed S3 history does not match the exact reserved assigned-Z potential")
        target_truth = truth.finite_population_itt_z_v_cont
        if not math.isfinite(target_truth) or not -1.0 <= target_truth <= 1.0:
            raise ContractError("reserved finite-population ITT-Z truth is outside [-1,1]")
        lower, upper = result.lower_bound, result.upper_bound
        if not (math.isfinite(lower) and math.isfinite(upper) and lower <= upper):
            raise ContractError("ITT-Z Analyzer bounds must be finite and ordered")
        if result.identification == "IDENTIFIED":
            if result.point_estimate is None or not math.isfinite(result.point_estimate):
                raise ContractError("identified ITT-Z result requires a finite estimate")
            if result.missing_interval_count != 0:
                raise ContractError("identified ITT-Z result cannot contain missing intervals")
            if (result.randomization_lower_bound is None
                    or result.randomization_upper_bound is None
                    or result.hoeffding_radius is None
                    or result.randomization_confidence_level is None
                    or not math.isfinite(result.randomization_lower_bound)
                    or not math.isfinite(result.randomization_upper_bound)
                    or not math.isfinite(result.hoeffding_radius)
                    or result.randomization_confidence_level != contract.confidence_level
                    or result.randomization_lower_bound > result.randomization_upper_bound
                    or result.hoeffding_radius < 0):
                raise ContractError("identified ITT-Z requires finite design-based randomization bounds")
            error = abs(result.point_estimate - target_truth)
            covers = (
                result.randomization_lower_bound - tolerance <= target_truth
                <= result.randomization_upper_bound + tolerance
            )
            # HT is design-unbiased, not exactly equal to finite-population
            # truth in each randomization. Evaluate finite-sample coverage,
            # never exact equality to the oracle.
            correct = covers
            disposition = (
                "TRUTH_WITHIN_HOEFFDING_RANDOMIZATION_BOUND"
                if covers else "TRUTH_OUTSIDE_HOEFFDING_RANDOMIZATION_BOUND"
            )
        elif result.identification == "PARTIALLY_IDENTIFIED":
            if result.point_estimate is not None or not result.abstention_reason:
                raise ContractError("partial ITT-Z result must abstain with an explicit reason")
            if result.missing_interval_count <= 0:
                raise ContractError("partial ITT-Z status requires interval missingness")
            # These bounds concern completion of missing interval values in the
            # realized HT contrast, not sampling uncertainty or causal truth.
            # They must never be interpreted as causal identification bounds.
            error, covers = None, None
            correct = True
            disposition = "CORRECT_ABSTENTION_MEASUREMENT_INCOMPLETE"
        elif result.identification == "INDETERMINATE":
            if result.point_estimate is not None or not result.abstention_reason:
                raise ContractError("indeterminate ITT-Z result must abstain explicitly")
            error, covers = None, None
            correct = True
            disposition = "CORRECT_ABSTENTION_SUPPORT_INCOMPLETE"
        else:
            raise ContractError("unsupported ITT-Z identification status")
        return D2ITTZEvaluation(
            evidence.run_id, target_truth, result.identification,
            result.point_estimate, lower, upper, error, covers, correct,
            disposition, tolerance, evidence.sha256, result.output_sha256,
        )
