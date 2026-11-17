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
    measurement_lower_bound: float
    measurement_upper_bound: float
    randomization_lower_bound: float | None
    randomization_upper_bound: float | None
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
        contract.validate()
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
            "bound_scope": result.bound_scope,
            "input_sha256": result.input_sha256,
        }) != result.output_sha256:
            raise ContractError("ITT-Z Analyzer result fingerprint is invalid")
        if (result.estimand_id, result.estimand_version) != (
            contract.estimand_id, contract.estimand_version
        ):
            raise ContractError("ITT-Z Analyzer estimand identity/version mismatch")
        assignments_by_unit = {row.unit_id: row for row in assignments.assignments}
        evidence_units = {row["unit_id"] for row in evidence.rows}
        if not evidence_units.issubset(assignments_by_unit):
            raise ContractError("D2 S3 evidence contains units outside the randomized assignment roster")
        manifest = evidence.manifest
        expected_pairs = tuple(tuple(row) for row in manifest.get("expected_unit_history_refs", ()))
        expected_by_unit = dict(expected_pairs)
        expected_assignments = tuple(tuple(row) for row in manifest.get("expected_unit_assignments", ()))
        expected_assignment_by_unit = {row[0]: row for row in expected_assignments}
        if (manifest.get("temporal_resolution") != "INTERVAL_LEVEL"
                or manifest.get("row_count") != len(evidence.rows)
                or manifest.get("unit_count") != len(evidence_units)
                or manifest.get("expected_unit_count") != len(assignments_by_unit)
                or set(expected_by_unit) != set(assignments_by_unit)
                or len(expected_pairs) != len(expected_by_unit)
                or set(expected_assignment_by_unit) != set(assignments_by_unit)
                or len(expected_assignments) != len(expected_assignment_by_unit)
                or not isinstance(manifest.get("interval_count_per_unit"), int)
                or manifest.get("interval_count_per_unit") < 1):
            raise ContractError("D2 sealed manifest does not describe the complete randomized roster and observed interval subset")
        if any(expected_by_unit[unit_id] != assignment.history_ref
               for unit_id, assignment in assignments_by_unit.items()):
            raise ContractError("D2 sealed expected unit/history roster differs from hashed assignment bundle")
        expected_missing_unit_ids = tuple(sorted(set(assignments_by_unit) - evidence_units))
        if tuple(sorted(manifest.get("missing_unit_ids", ()))) != expected_missing_unit_ids:
            raise ContractError("D2 sealed manifest missing-unit list differs from assignment/evidence coverage")
        for unit_id, assignment in assignments_by_unit.items():
            expected_detail = expected_assignment_by_unit[unit_id]
            if expected_detail != (
                unit_id, assignment.history_ref, assignment.assigned_z,
                assignment.probability_z0, assignment.probability_z1,
            ):
                raise ContractError("D2 sealed expected assignment detail differs from hashed assignment bundle")
        by_unit_rows: dict[str, list[dict]] = {}
        for row in evidence.rows:
            by_unit_rows.setdefault(row["unit_id"], []).append(row)
        qx_mass = dict(contract.q_x_mass_by_history)
        observed_histories = set()
        arm_terms: list[list[tuple[float, int, int]]] = [[], []]
        missing_interval_count = total_interval_count = 0
        expected_interval_count = manifest["interval_count_per_unit"]
        for unit_id, rows in by_unit_rows.items():
            ordered = sorted(rows, key=lambda row: row["interval_index"])
            if (len(ordered) != expected_interval_count
                    or [row["interval_index"] for row in ordered] != list(range(expected_interval_count))):
                raise ContractError("D2 sealed evidence has an incomplete or duplicated interval sequence")
            if any(left["interval_end"] != right["interval_start"]
                   for left, right in zip(ordered, ordered[1:])):
                raise ContractError("D2 sealed evidence interval sequence is not contiguous")
            first = ordered[0]
            observed_histories.add(first["history_ref"])
            assignment = assignments_by_unit[unit_id]
            if first["history_ref"] not in qx_mass:
                raise ContractError("D2 sealed evidence history is outside q_X support")
            if any((row["history_ref"], row["assigned_z"], row["probability_z0"],
                    row["probability_z1"], row["assignment_probability"]) != (
                    first["history_ref"], assignment.assigned_z,
                    assignment.probability_z0, assignment.probability_z1,
                    assignment.probability_z1 if assignment.assigned_z else assignment.probability_z0
                    ) for row in ordered):
                raise ContractError("D2 interval rows disagree on history or randomized assignment")
            if any(row["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE"
                   or row["observation_status"] not in ("OBSERVED", "MISSING")
                   or ((row["observation_status"] == "MISSING") != (row["observed_compliance"] is None))
                   or (row["observation_status"] == "OBSERVED"
                       and type(row["observed_compliance"]) is not bool)
                   for row in ordered):
                raise ContractError("D2 interval observations violate strict S3 missingness/value semantics")
            any_failure = any(row["observed_compliance"] is False for row in ordered)
            any_missing = any(row["observation_status"] == "MISSING" for row in ordered)
            y_lower = 0 if any_failure or any_missing else 1
            y_upper = 0 if any_failure else 1
            missing_interval_count += sum(row["observation_status"] == "MISSING" for row in ordered)
            total_interval_count += len(ordered)
            mass = qx_mass[first["history_ref"]]
            p = assignment.probability_z1 if assignment.assigned_z else assignment.probability_z0
            arm_terms[assignment.assigned_z].append((mass / p, y_lower, y_upper))
        missing_histories = tuple(sorted(set(qx_mass) - observed_histories))
        assigned_counts = (len(arm_terms[0]), len(arm_terms[1]))
        expected_coverage = sum(qx_mass[key] for key in observed_histories)
        if (result.missing_target_histories != missing_histories
                or result.assigned_z_unit_counts != assigned_counts
                or result.missing_interval_count != missing_interval_count
                or result.total_interval_count != total_interval_count
                or not math.isclose(result.target_q_x_coverage, expected_coverage,
                                    rel_tol=0.0, abs_tol=1e-12)):
            raise ContractError("D2 Analyzer support, assignment-count or missingness diagnostics do not reproduce from S3")
        for unit_id in expected_missing_unit_ids:
            _, history_ref, z, p0, p1 = expected_assignment_by_unit[unit_id]
            mass = qx_mass[history_ref]
            p = p1 if z == 1 else p0
            arm_terms[z].append((mass / p, 0, 1))
        mu_lower = [sum(w * lo for w, lo, hi in values) for values in arm_terms]
        mu_upper = [sum(w * hi for w, lo, hi in values) for values in arm_terms]
        expected_lower = mu_lower[1] - mu_upper[0]
        expected_upper = mu_upper[1] - mu_lower[0]
        if missing_interval_count or expected_missing_unit_ids:
            expected_identification = "PARTIALLY_IDENTIFIED"
            expected_estimate = None
            reasons = []
            if expected_missing_unit_ids:
                reasons.append("UNIT_NONRESPONSE")
            if missing_interval_count:
                reasons.append("INTERVAL_MISSINGNESS")
            expected_reason = "_AND_".join(reasons) + "_PREVENTS_STRICT_VCONT_POINT_RECOVERY"
        else:
            expected_identification = "IDENTIFIED"
            expected_estimate = mu_lower[1] - mu_lower[0]
            expected_reason = ""
        if (result.identification != expected_identification
                or not math.isclose(result.lower_bound, expected_lower,
                                    rel_tol=1e-10, abs_tol=1e-12)
                or not math.isclose(result.upper_bound, expected_upper,
                                    rel_tol=1e-10, abs_tol=1e-12)
                or result.point_estimate != expected_estimate
                or result.abstention_reason != expected_reason):
            raise ContractError("D2 Analyzer identification status/measurement bounds do not reproduce independently from sealed S3")
        # Recompute the assignment-bundle digest independently. The Analyzer
        # only sees the opaque digest; the Evaluator verifies its full contents.
        assignment_payload = {
            "world": (assignments.world_id, assignments.world_version,
                      assignments.dgp_id, assignments.dgp_version),
            "mechanism": (assignments.mechanism_id, assignments.mechanism_version,
                          assignments.mechanism_sha256),
            "salt_sha256": assignments.randomization_salt_sha256,
            "q_x_sha256": assignments.q_x_sha256,
            "assignments": assignments.assignments,
        }
        if digest(assignment_payload) != assignments.result_sha256:
            raise ContractError("D2 assignment bundle digest does not match its contents")
        truth_rows = {(row.unit_id, row.z): row for row in truth.potential_truth}
        for unit_id, assignment in assignments_by_unit.items():
            selected_truth = truth_rows[(unit_id, assignment.assigned_z)]
            rows = [row for row in evidence.rows if row["unit_id"] == unit_id]
            if not rows:
                # Unit-level nonresponse is represented in the sealed roster
                # manifest and is handled as incomplete q_X support below.
                continue
            p_assigned = (
                assignment.probability_z1 if assignment.assigned_z == 1
                else assignment.probability_z0
            )
            if any((row["world_id"], row["world_version"], row["dgp_id"],
                    row["dgp_version"], row["history_ref"],
                    row["assignment_bundle_sha256"], row["q_x_sha256"],
                    row["assignment_mechanism_id"], row["assignment_mechanism_version"],
                    row["assigned_z"], row["probability_z0"], row["probability_z1"],
                    row["assignment_probability"], row["assignment_uniform_sha256"],
                    row["selected_potential_id"], row["history_id"],
                    row["history_content_sha256"]) != (
                    world.world_id, world.world_version, world.dgp_id,
                    world.dgp_version, assignment.history_ref,
                    assignments.result_sha256, assignments.q_x_sha256,
                    assignments.mechanism_id, assignments.mechanism_version,
                    assignment.assigned_z, assignment.probability_z0,
                    assignment.probability_z1, p_assigned,
                    assignment.assignment_uniform_sha256,
                    selected_truth.potential_id, selected_truth.history_id,
                    selected_truth.history_content_sha256
                    ) for row in rows):
                raise ContractError("D2 observed S3 assignment/probabilities do not match the hashed assignment and exact reserved potential")
        target_truth = truth.finite_population_itt_z_v_cont
        if not math.isfinite(target_truth) or not -1.0 <= target_truth <= 1.0:
            raise ContractError("reserved finite-population ITT-Z truth is outside [-1,1]")
        lower, upper = result.lower_bound, result.upper_bound
        if not (math.isfinite(lower) and math.isfinite(upper) and lower <= upper):
            raise ContractError("ITT-Z Analyzer bounds must be finite and ordered")
        if result.identification == "IDENTIFIED":
            if result.bound_scope != "NONE":
                raise ContractError("identified ITT-Z result must not declare measurement-completion bounds")
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
            qx_mass = {row.history_ref: row.mass for row in world.q_x}
            assignment_range_sq = sum(
                (
                    qx_mass[row.history_ref]
                    * (1.0 / row.probability_z1 + 1.0 / row.probability_z0)
                ) ** 2
                for row in assignments.assignments
            )
            expected_radius = math.sqrt(
                0.5 * assignment_range_sq
                * math.log(2.0 / (1.0 - contract.confidence_level))
            )
            expected_randomization_lower = max(-1.0, result.point_estimate - expected_radius)
            expected_randomization_upper = min(1.0, result.point_estimate + expected_radius)
            if (not math.isclose(result.hoeffding_radius, expected_radius,
                                 rel_tol=1e-10, abs_tol=1e-12)
                    or not math.isclose(result.randomization_lower_bound,
                                        expected_randomization_lower,
                                        rel_tol=1e-10, abs_tol=1e-12)
                    or not math.isclose(result.randomization_upper_bound,
                                        expected_randomization_upper,
                                        rel_tol=1e-10, abs_tol=1e-12)):
                raise ContractError("ITT-Z randomization bounds do not reproduce from the declared assignment design")
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
            if result.bound_scope != "REALIZED_HT_MEASUREMENT_COMPLETION":
                raise ContractError("partial ITT-Z bounds must declare their realized-HT measurement scope")
            if result.point_estimate is not None or not result.abstention_reason:
                raise ContractError("partial ITT-Z result must abstain with an explicit reason")
            if result.missing_interval_count <= 0 and not expected_missing_unit_ids:
                raise ContractError("partial ITT-Z status requires interval or unit-level nonresponse")
            if any(value is not None for value in (
                result.randomization_lower_bound, result.randomization_upper_bound,
                result.hoeffding_radius, result.randomization_confidence_level,
            )):
                raise ContractError("measurement-completion bounds must not be presented as randomization confidence bounds")
            # Bounds concern completion of unobserved binary outcomes in the
            # realized HT contrast, not randomization uncertainty or causal truth.
            error, covers = None, None
            correct = True
            disposition = (
                "CORRECT_ABSTENTION_UNIT_NONRESPONSE"
                if expected_missing_unit_ids and not result.missing_interval_count
                else "CORRECT_ABSTENTION_MEASUREMENT_AND_UNIT_NONRESPONSE"
                if expected_missing_unit_ids
                else "CORRECT_ABSTENTION_MEASUREMENT_INCOMPLETE"
            )
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
            result.point_estimate, lower, upper,
            result.randomization_lower_bound, result.randomization_upper_bound,
            error, covers, correct,
            disposition, tolerance, evidence.sha256, result.output_sha256,
        )
