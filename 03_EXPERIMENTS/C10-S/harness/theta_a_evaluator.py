"""Independent Evaluator for the sealed direct-g_A theta_A observation path.

The Evaluator is the first component in this path allowed to inspect the
reserved ThetaAVContTruthBundle. It validates evidence/result provenance,
checks point recovery or bound coverage, and distinguishes a correct
abstention from an invalid Analyzer claim.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any

from c10s_synthetic_components import (ContractError, ThetaAVContTruthBundle,
                                        ThetaAPolicyAssignmentBundle)
from theta_a_observation_harness import SealedThetaAEvidence, _hash
from theta_a_analyzer import (ThetaAObservationAnalysisContract,
                              ThetaAObservationAnalysisResult,
                              _canonical_hash, adjudicate_theta_a_structural_support)


@dataclass(frozen=True)
class ThetaAObservationEvaluation:
    run_id: str
    estimand_id: str
    estimand_version: str
    truth: float
    analyzer_identification: str
    point_estimate: float | None
    lower_bound: float
    upper_bound: float
    absolute_error: float | None
    truth_within_bounds: bool
    bound_width: float
    informative_bounds: bool
    correct_adjudication: bool
    disposition: str
    tolerance: float
    evidence_sha256: str
    analyzer_output_sha256: str
    inference_truth_covered: bool | None = None
    inference_interval_width: float | None = None
    inference_confidence_level: float | None = None


def _result_payload(result: ThetaAObservationAnalysisResult) -> dict[str, Any]:
    return {
        "run_id": result.run_id, "estimand_id": result.estimand_id,
        "estimand_version": result.estimand_version,
        "identification": result.identification, "point_estimate": result.point_estimate,
        "lower_bound": result.lower_bound, "upper_bound": result.upper_bound,
        "target_q_x_coverage": result.target_q_x_coverage,
        "missing_target_histories": result.missing_target_histories,
        "assigned_arm_unit_counts": result.assigned_arm_unit_counts,
        "temporal_resolution": result.temporal_resolution,
        "abstention_reason": result.abstention_reason,
        "input_sha256": result.input_sha256,
        "measurement_lower_bound": result.measurement_lower_bound,
        "measurement_upper_bound": result.measurement_upper_bound,
        "missing_interval_count": result.missing_interval_count,
        "total_interval_count": result.total_interval_count,
        "inference_method": result.inference_method,
        "inference_confidence_level": result.inference_confidence_level,
        "inference_lower_bound": result.inference_lower_bound,
        "inference_upper_bound": result.inference_upper_bound,
        "hoeffding_range_sum_squares": result.hoeffding_range_sum_squares,
        "structural_support_sha256": result.structural_support_sha256,
    }


class ThetaAObservationEvaluator:
    """Independent oracle comparison; never pass its truth object to Analyzer."""

    version = "c10s-theta-a-observation-evaluator-0.2"

    def evaluate(self, truth_bundle: ThetaAVContTruthBundle,
                 evidence: SealedThetaAEvidence,
                 result: ThetaAObservationAnalysisResult,
                 assignment_bundle: ThetaAPolicyAssignmentBundle,
                 contract: ThetaAObservationAnalysisContract,
                 *, tolerance: float) -> ThetaAObservationEvaluation:
        truth_bundle.validate()
        contract.validate()
        if not math.isfinite(tolerance) or tolerance < 0:
            raise ContractError("theta_A evaluation tolerance must be finite and non-negative")
        truth = truth_bundle.theta_a_truth
        if not truth.evaluator_only or truth.outcome_id != "V_CONT":
            raise ContractError("Evaluator requires reserved evaluator-only V_CONT truth")
        if (truth.estimand_id != contract.estimand_id
                or truth.estimand_version != contract.estimand_version):
            raise ContractError("Analyzer contract and reserved theta_A estimand identity/version differ")
        if truth.q_x_fingerprint != contract.q_x_sha256:
            raise ContractError("analysis q_X fingerprint does not match reserved oracle q_X fingerprint")
        if (truth.g_a0_fingerprint != contract.g_a0_sha256
                or truth.g_a1_fingerprint != contract.g_a1_sha256):
            raise ContractError("analysis g_A policy fingerprints do not match reserved oracle policies")
        if result.run_id != evidence.run_id or result.run_id == "":
            raise ContractError("Analyzer result and sealed evidence run identity mismatch")
        if result.estimand_id != truth.estimand_id or result.estimand_version != truth.estimand_version:
            raise ContractError("Analyzer result estimand identity/version mismatch")
        if result.input_sha256 != evidence.sha256:
            raise ContractError("Analyzer result is not bound to the supplied sealed evidence")
        expected_support_sha = structural.contract_sha256 if structural is not None else None
        if result.structural_support_sha256 != expected_support_sha:
            raise ContractError("Analyzer result structural-support provenance differs from evaluation contract")
        if structural is not None and structural.status == "NOT_IDENTIFIED":
            if (result.identification != "NOT_IDENTIFIED"
                    or result.abstention_reason != structural.reason
                    or result.point_estimate is not None
                    or result.lower_bound != -1.0 or result.upper_bound != 1.0
                    or result.missing_target_histories != structural.unsupported_target_histories):
                raise ContractError("Analyzer did not correctly abstain for structural target/source non-overlap")
        elif structural is not None and structural.status == "STRUCTURAL_SUPPORT_SUFFICIENT":
            if result.identification == "NOT_IDENTIFIED" and result.abstention_reason == "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT":
                raise ContractError("Analyzer falsely reported structural non-identification under complete support")
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("sealed theta_A evidence digest is invalid")
        if _canonical_hash(_result_payload(result)) != result.output_sha256:
            raise ContractError("Analyzer result digest is invalid")
        source_qx_sha256 = contract.source_q_x_sha256 or contract.q_x_sha256
        structural = (
            adjudicate_theta_a_structural_support(contract.structural_support_contract)
            if contract.structural_support_contract is not None else None
        )
        if (assignment_bundle.result_sha256 != contract.assignment_bundle_sha256
                or assignment_bundle.q_x_sha256 != source_qx_sha256
                or assignment_bundle.g_a0_sha256 != contract.g_a0_sha256
                or assignment_bundle.g_a1_sha256 != contract.g_a1_sha256
                or assignment_bundle.r_common_sha256 != contract.r_common_sha256):
            raise ContractError("assignment bundle does not match the analysis intervention/population contract")
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != source_qx_sha256
               or row.get("g_a0_sha256") != contract.g_a0_sha256
               or row.get("g_a1_sha256") != contract.g_a1_sha256
               or row.get("r_common_sha256") != contract.r_common_sha256
               for row in evidence.rows):
            raise ContractError("sealed evidence does not match the analysis assignment/q_X/policy contract")
        assignment_by_unit = {row.unit_id: row for row in assignment_bundle.assignments}
        if len(assignment_by_unit) != len(assignment_bundle.assignments):
            raise ContractError("assignment bundle contains duplicate unit assignments")
        if contract.confidence_level is not None:
            p1_by_history = dict(contract.probability_a1_by_history)
            if set(p1_by_history) != {row.history_ref for row in assignment_bundle.assignments}:
                raise ContractError("inferential probability contract does not cover the exact assignment histories")
            if any(not math.isclose(
                    p1_by_history[row.history_ref], row.probability_a1,
                    rel_tol=0.0, abs_tol=1e-12
            ) for row in assignment_bundle.assignments):
                raise ContractError("inferential probability contract differs from the actual two-arm assignment bundle")
        evidence_units = {row["unit_id"] for row in evidence.rows}
        if evidence_units != set(assignment_by_unit):
            raise ContractError("sealed observations must cover the exact assigned-unit roster")
        for row in evidence.rows:
            assigned = assignment_by_unit[row["unit_id"]]
            assigned_probability = (assigned.probability_a1 if assigned.assigned_arm == 1
                                    else assigned.probability_a0)
            if (row["assigned_arm"] != assigned.assigned_arm
                    or row["assigned_vector_sha256"] != assigned.assigned_vector_sha256
                    or row["policy_fingerprint"] != assigned.policy_fingerprint
                    or row["r_common_fingerprint"] != assigned.r_common_fingerprint
                    or row["history_ref"] != assigned.history_ref
                    or row["assignment_probability"] != assigned_probability):
                raise ContractError("sealed observation does not reproduce its exact direct-g_A assignment record")

        # Bind every observed unit/history to the reserved selected-history manifest.
        # Manifest rows are (history_ref, vector_sha, r_common_fingerprint,
        # history_id, EventHistory content SHA); unit identity is carried by
        # the assignment/evidence binding, not by this policy-potential manifest.
        truth_history_keys = {(row[0], row[3]) for row in truth_bundle.event_history_manifest}
        evidence_history_keys = {(row["history_ref"], row["history_id"])
                                 for row in evidence.rows}
        if not evidence_history_keys or not evidence_history_keys.issubset(truth_history_keys):
            raise ContractError("sealed observations do not map to the reserved realized EventHistory manifest")
        if result.temporal_resolution == "INTERVAL_LEVEL":
            truth_history_content = {(row[0], row[3]): row[4]
                                     for row in truth_bundle.event_history_manifest}
            for row in evidence.rows:
                key = (row["history_ref"], row["history_id"])
                if row.get("history_content_sha256") != truth_history_content.get(key):
                    raise ContractError("interval evidence does not bind to the exact reserved EventHistory content")
        truth_regime_by_history = {
            contribution.history_ref: contribution.r_common_fingerprint
            for contribution in truth.contributions
        }
        for row in evidence.rows:
            if (row["r_common_sha256"] != contract.r_common_sha256
                    or row["r_common_fingerprint"] != truth_regime_by_history.get(row["history_ref"])):
                raise ContractError("observed assignment is not bound to the reserved common-r_common policy regime")

        if result.temporal_resolution == "INTERVAL_LEVEL":
            observed_missing = sum(row.get("observation_status") == "MISSING" for row in evidence.rows)
            if (evidence.manifest.get("temporal_resolution") != "INTERVAL_LEVEL"
                    or result.missing_interval_count != observed_missing
                    or result.total_interval_count != len(evidence.rows)
                    or result.missing_interval_count < 0
                    or result.total_interval_count <= 0
                    or result.missing_interval_count > result.total_interval_count):
                raise ContractError("interval Analyzer counts do not reproduce sealed observation missingness")
            if (result.measurement_lower_bound is None) != (result.measurement_upper_bound is None):
                raise ContractError("interval measurement bounds must be jointly present or absent")
            if result.measurement_lower_bound is not None and not (
                math.isfinite(result.measurement_lower_bound)
                and math.isfinite(result.measurement_upper_bound)
                and result.measurement_lower_bound <= result.measurement_upper_bound
            ):
                raise ContractError("interval measurement-only bounds must be finite and within [-1,1]")
            if result.missing_interval_count and result.identification not in ("PARTIALLY_IDENTIFIED", "INDETERMINATE"):
                raise ContractError("missing interval evidence requires partial-identification or support abstention")
            if not result.missing_interval_count and result.identification == "PARTIALLY_IDENTIFIED":
                raise ContractError("complete interval evidence must not abstain for missingness")
            # Independently reconstruct measurement-only HT bounds from sealed
            # observations. This does not consult the reserved outcome oracle.
            qx_mass = dict(contract.q_x_mass_by_history)
            by_unit = {}
            for row in evidence.rows:
                by_unit.setdefault(row["unit_id"], []).append(row)
            arm_lower = [0.0, 0.0]
            arm_upper = [0.0, 0.0]
            arm_support = [0, 0]
            observed_histories = set()
            for unit_rows in by_unit.values():
                first = unit_rows[0]
                ordered = sorted(unit_rows, key=lambda row: row["interval_index"])
                n = len(ordered)
                successes = sum(row["observed_compliance"] is True for row in ordered)
                missing = sum(row["observation_status"] == "MISSING" for row in ordered)
                y_lower = successes / n
                y_upper = (successes + missing) / n
                arm = first["assigned_arm"]
                weight = qx_mass[first["history_ref"]] / first["assignment_probability"]
                arm_lower[arm] += weight * y_lower
                arm_upper[arm] += weight * y_upper
                arm_support[arm] += 1
                observed_histories.add(first["history_ref"])
            if set(qx_mass).issubset(observed_histories) and all(arm_support):
                expected_measurement_lower = arm_lower[1] - arm_upper[0]
                expected_measurement_upper = arm_upper[1] - arm_lower[0]
            else:
                expected_measurement_lower = expected_measurement_upper = None
            if expected_measurement_lower is None:
                if result.measurement_lower_bound is not None:
                    raise ContractError("interval Analyzer reported measurement bounds without q_X/arm support")
            elif (result.measurement_lower_bound is None
                  or result.measurement_upper_bound is None
                  or not math.isclose(result.measurement_lower_bound, expected_measurement_lower,
                                      rel_tol=0.0, abs_tol=1e-12)
                  or not math.isclose(result.measurement_upper_bound, expected_measurement_upper,
                                      rel_tol=0.0, abs_tol=1e-12)):
                raise ContractError("interval measurement-only bounds do not reproduce sealed S3 observations")
            if result.missing_interval_count == 0 and all(arm_support):
                if (result.identification != "IDENTIFIED" or result.point_estimate is None
                        or not math.isclose(result.point_estimate, expected_measurement_lower,
                                            rel_tol=0.0, abs_tol=1e-12)):
                    raise ContractError("complete interval Analyzer point estimate does not reproduce HT contrast")

            # Independently verify the optional bounded two-stage HT interval.
            inference_fields = (
                result.inference_method, result.inference_confidence_level,
                result.inference_lower_bound, result.inference_upper_bound,
                result.hoeffding_range_sum_squares,
            )
            inference_eligible = (
                result.missing_interval_count == 0
                and result.identification == "IDENTIFIED"
                and result.point_estimate is not None
                and set(qx_mass).issubset(observed_histories)
                and all(arm_support)
            )
            if contract.confidence_level is None or not inference_eligible:
                if any(value is not None for value in inference_fields):
                    raise ContractError("theta_A inferential interval reported without a complete eligible design")
            else:
                if not contract.probability_a1_by_history:
                    raise ContractError("theta_A inferential interval lacks declared assignment probabilities")
                p1_by_history = dict(contract.probability_a1_by_history)
                range_sum_squares = 0.0
                for unit_rows in by_unit.values():
                    first = unit_rows[0]
                    p1 = p1_by_history[first["history_ref"]]
                    p0 = 1.0 - p1
                    selected_probability = p1 if first["assigned_arm"] == 1 else p0
                    if not math.isclose(first["assignment_probability"], selected_probability,
                                        rel_tol=0.0, abs_tol=1e-12):
                        raise ContractError("sealed assignment probability differs from inferential contract")
                    width = qx_mass[first["history_ref"]] * (1.0 / p1 + 1.0 / p0)
                    range_sum_squares += width * width
                radius = math.sqrt(
                    0.5 * range_sum_squares
                    * math.log(2.0 / (1.0 - contract.confidence_level))
                )
                expected_lower = result.point_estimate - radius
                expected_upper = result.point_estimate + radius
                if (result.inference_method != "HOEFFDING_TWO_STAGE_BOUNDED_HT_V1"
                        or result.inference_confidence_level != contract.confidence_level
                        or result.hoeffding_range_sum_squares is None
                        or not math.isclose(result.hoeffding_range_sum_squares, range_sum_squares,
                                            rel_tol=0.0, abs_tol=1e-12)
                        or result.inference_lower_bound is None
                        or result.inference_upper_bound is None
                        or not math.isclose(result.inference_lower_bound, expected_lower,
                                            rel_tol=0.0, abs_tol=1e-12)
                        or not math.isclose(result.inference_upper_bound, expected_upper,
                                            rel_tol=0.0, abs_tol=1e-12)):
                    raise ContractError("theta_A bounded two-stage inferential interval failed independent reconstruction")
        lower, upper = result.lower_bound, result.upper_bound
        if not (math.isfinite(lower) and math.isfinite(upper) and lower <= upper):
            raise ContractError("Analyzer bounds must be finite and ordered")
        if not (math.isfinite(truth.theta_a_truth) and -1.0 <= truth.theta_a_truth <= 1.0):
            raise ContractError("reserved theta_A truth is outside the declared binary-outcome contrast range")
        covers = lower - tolerance <= truth.theta_a_truth <= upper + tolerance
        width = upper - lower
        estimate = result.point_estimate
        status = result.identification

        if status == "IDENTIFIED":
            if estimate is None or not math.isfinite(estimate):
                raise ContractError("identified Analyzer result must provide a finite point estimate")
            if (result.temporal_resolution != "INTERVAL_LEVEL"
                    and not lower - tolerance <= estimate <= upper + tolerance):
                raise ContractError("identified point estimate lies outside its reported interval")
            error = abs(estimate - truth.theta_a_truth)
            correct = covers and error <= tolerance
            disposition = "POINT_RECOVERED" if correct else "POINT_RECOVERY_FAILED"
        elif status == "PARTIALLY_IDENTIFIED":
            if estimate is not None:
                raise ContractError("partially identified Analyzer result must not expose a point estimate")
            if not result.abstention_reason:
                raise ContractError("partial-identification result requires an explicit limitation reason")
            error = None
            correct = covers
            disposition = ("BOUNDS_COVER_TRUTH" if covers else "INVALID_BOUNDS_EXCLUDE_TRUTH")
        elif status in ("NOT_IDENTIFIED", "INDETERMINATE"):
            if estimate is not None:
                raise ContractError("non-identified Analyzer result must abstain from a point estimate")
            if not result.abstention_reason:
                raise ContractError("non-identified Analyzer result requires an explicit abstention reason")
            error = None
            correct = covers
            disposition = ("CORRECT_ABSTENTION" if covers
                           else "ABSTENTION_BOUNDS_EXCLUDE_TRUTH")
        else:
            raise ContractError(f"unsupported theta_A identification status: {status}")

        # Width 2 is the logical range for a binary contrast and is not informative.
        informative = width < 2.0 - 1e-12
        inference_covered = None
        inference_width = None
        if result.inference_lower_bound is not None and result.inference_upper_bound is not None:
            inference_covered = (
                result.inference_lower_bound <= truth.theta_a_truth
                <= result.inference_upper_bound
            )
            inference_width = result.inference_upper_bound - result.inference_lower_bound
        return ThetaAObservationEvaluation(
            result.run_id, truth.estimand_id, truth.estimand_version,
            truth.theta_a_truth, status, estimate, lower, upper, error, covers,
            width, informative, correct, disposition, tolerance, evidence.sha256,
            result.output_sha256, inference_covered, inference_width,
            result.inference_confidence_level,
        )