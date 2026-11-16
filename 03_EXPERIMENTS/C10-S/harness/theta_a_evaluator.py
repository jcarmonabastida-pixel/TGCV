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
                              _canonical_hash)


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
    }


class ThetaAObservationEvaluator:
    """Independent oracle comparison; never pass its truth object to Analyzer."""

    version = "c10s-theta-a-observation-evaluator-0.1"

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
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("sealed theta_A evidence digest is invalid")
        if _canonical_hash(_result_payload(result)) != result.output_sha256:
            raise ContractError("Analyzer result digest is invalid")
        if (assignment_bundle.result_sha256 != contract.assignment_bundle_sha256
                or assignment_bundle.q_x_sha256 != contract.q_x_sha256
                or assignment_bundle.g_a0_sha256 != contract.g_a0_sha256
                or assignment_bundle.g_a1_sha256 != contract.g_a1_sha256
                or assignment_bundle.r_common_sha256 != contract.r_common_sha256):
            raise ContractError("assignment bundle does not match the analysis intervention/population contract")
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != contract.q_x_sha256
               or row.get("g_a0_sha256") != contract.g_a0_sha256
               or row.get("g_a1_sha256") != contract.g_a1_sha256
               or row.get("r_common_sha256") != contract.r_common_sha256
               for row in evidence.rows):
            raise ContractError("sealed evidence does not match the analysis assignment/q_X/policy contract")
        assignment_by_unit = {row.unit_id: row for row in assignment_bundle.assignments}
        if len(assignment_by_unit) != len(assignment_bundle.assignments):
            raise ContractError("assignment bundle contains duplicate unit assignments")
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
                and -1.0 <= result.measurement_lower_bound <= result.measurement_upper_bound <= 1.0
            ):
                raise ContractError("interval measurement-only bounds must be finite and within [-1,1]")
            if result.missing_interval_count and result.identification not in ("PARTIALLY_IDENTIFIED", "INDETERMINATE"):
                raise ContractError("missing interval evidence requires partial-identification or support abstention")
            if not result.missing_interval_count and result.identification == "PARTIALLY_IDENTIFIED":
                raise ContractError("complete interval evidence must not abstain for missingness")
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
            if not lower - tolerance <= estimate <= upper + tolerance:
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
        return ThetaAObservationEvaluation(
            result.run_id, truth.estimand_id, truth.estimand_version,
            truth.theta_a_truth, status, estimate, lower, upper, error, covers,
            width, informative, correct, disposition, tolerance, evidence.sha256,
            result.output_sha256,
        )