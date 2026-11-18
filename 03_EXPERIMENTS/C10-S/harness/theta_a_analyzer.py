"""Observation-only theta_A analyzer for the C10-S focal S3 evidence path.

POINT_SAMPLE records do not reveal strict interval continuity V_cont. The
analyzer therefore reports sharp logical bounds for a binary outcome rather
than fabricating a point estimate. Target q_X masses are supplied as an
explicit analysis input and checked against the assignment manifest.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any

from theta_a_observation_harness import SealedThetaAEvidence, _hash
from c10s_synthetic_components import ContractError


@dataclass(frozen=True)
class ThetaAObservationAnalysisContract:
    q_x_mass_by_history: tuple[tuple[str, float], ...]
    q_x_sha256: str
    assignment_bundle_sha256: str
    g_a0_sha256: str
    g_a1_sha256: str
    r_common_sha256: str
    estimand_id: str = "THETA_A_QX_GA_RCOMMON_VCONT"
    estimand_version: str = "1.0"
    probability_a1_by_history: tuple[tuple[str, float], ...] = ()
    confidence_level: float | None = None
    unit_independence_certified: bool = False
    structural_support_contract: "ThetaAStructuralSupportContract | None" = None
    source_q_x_sha256: str | None = None

    def validate(self) -> None:
        if not all((self.q_x_sha256, self.assignment_bundle_sha256,
                    self.g_a0_sha256, self.g_a1_sha256, self.r_common_sha256)):
            raise ContractError("theta_A analysis requires q_X, assignment, g_A0/g_A1 and r_common fingerprints")
        if not self.estimand_id or not self.estimand_version:
            raise ContractError("theta_A estimand identity/version are required")
        mapping = dict(self.q_x_mass_by_history)
        if len(mapping) != len(self.q_x_mass_by_history) or not mapping:
            raise ContractError("q_X target masses must have unique, non-empty history support")
        if any(not key or not math.isfinite(value) or value <= 0 for key, value in mapping.items()):
            raise ContractError("q_X target masses must be finite and strictly positive")
        if not math.isclose(sum(mapping.values()), 1.0, rel_tol=0.0, abs_tol=1e-10):
            raise ContractError("q_X target masses must sum to one")
        if self.probability_a1_by_history:
            probabilities = dict(self.probability_a1_by_history)
            if len(probabilities) != len(self.probability_a1_by_history) or set(probabilities) != set(mapping):
                raise ContractError("theta_A inference probabilities must cover q_X histories exactly")
            if any(not math.isfinite(p) or not 0.0 < p < 1.0 for p in probabilities.values()):
                raise ContractError("theta_A inference requires strict positivity for both policy arms")
        if self.structural_support_contract is not None:
            self.structural_support_contract.validate()
            if self.structural_support_contract.target_q_x_sha256 != self.q_x_sha256:
                raise ContractError("structural-support target fingerprint must match analysis q_X")
            source_fingerprint = self.source_q_x_sha256 or self.q_x_sha256
            if self.structural_support_contract.source_q_x_sha256 != source_fingerprint:
                raise ContractError("structural-support source fingerprint must match assignment source q_X")
            target_masses = dict(self.q_x_mass_by_history)
            support_rows = self.structural_support_contract.rows
            if set(target_masses) != {row.history_ref for row in support_rows}:
                raise ContractError("structural-support contract must cover the full q_X target")
            if any(not math.isclose(target_masses[row.history_ref], row.target_mass, rel_tol=0.0, abs_tol=1e-10) for row in support_rows):
                raise ContractError("structural-support target masses must match analysis q_X")
        if self.confidence_level is not None:
            if not math.isfinite(self.confidence_level) or not 0.0 < self.confidence_level < 1.0:
                raise ContractError("theta_A confidence_level must be explicitly between zero and one")
            if not self.probability_a1_by_history:
                raise ContractError("theta_A confidence interval requires the declared history-specific assignment probabilities")
            if self.unit_independence_certified is not True:
                raise ContractError("theta_A Hoeffding interval requires explicit unit-independence certification")


@dataclass(frozen=True)
class ThetaAObservationAnalysisResult:
    run_id: str
    estimand_id: str
    estimand_version: str
    identification: str
    point_estimate: float | None
    lower_bound: float
    upper_bound: float
    target_q_x_coverage: float
    missing_target_histories: tuple[str, ...]
    assigned_arm_unit_counts: tuple[int, int]
    temporal_resolution: str
    abstention_reason: str
    input_sha256: str
    output_sha256: str
    measurement_lower_bound: float | None = None
    measurement_upper_bound: float | None = None
    missing_interval_count: int = 0
    total_interval_count: int = 0
    inference_method: str | None = None
    inference_confidence_level: float | None = None
    inference_lower_bound: float | None = None
    inference_upper_bound: float | None = None
    hoeffding_range_sum_squares: float | None = None
    structural_support_sha256: str | None = None


def _canonical_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class ThetaAObservationAnalyzer:
    """Analyze sealed focal observations without access to DGP truth."""

    version = "c10s-theta-a-observation-analyzer-0.2"

    def analyze(self, evidence: SealedThetaAEvidence,
                contract: ThetaAObservationAnalysisContract) -> ThetaAObservationAnalysisResult:
        contract.validate()
        structural = adjudicate_theta_a_structural_support(contract.structural_support_contract) if contract.structural_support_contract is not None else None
        if structural is not None and structural.status == "NOT_IDENTIFIED":
            if not evidence.rows or _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
                raise ContractError("structural-support Analyzer requires non-empty sealed evidence with a valid digest")
            rows = evidence.rows
            source_qx_sha256 = contract.source_q_x_sha256 or contract.q_x_sha256
            if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
                   or row.get("q_x_sha256") != source_qx_sha256
                   or row.get("g_a0_sha256") != contract.g_a0_sha256
                   or row.get("g_a1_sha256") != contract.g_a1_sha256
                   or row.get("r_common_sha256") != contract.r_common_sha256 for row in rows):
                raise ContractError("structural-support evidence fingerprints do not match analysis contract")
            by_unit = {}
            for row in rows:
                prior = by_unit.setdefault(row["unit_id"], row)
                if any(prior[key] != row[key] for key in ("assigned_arm", "assignment_probability", "history_ref")):
                    raise ContractError("unit-level assignment fields vary across structural-support evidence")
            arms = [0, 0]
            for row in by_unit.values():
                if row["assigned_arm"] not in (0, 1):
                    raise ContractError("invalid assigned arm in structural-support evidence")
                arms[row["assigned_arm"]] += 1
            supported_mass = sum(row.target_mass for row in contract.structural_support_contract.rows if row.source_mass > 0)
            result_payload = {
                "run_id": evidence.run_id, "estimand_id": contract.estimand_id,
                "estimand_version": contract.estimand_version, "identification": "NOT_IDENTIFIED",
                "point_estimate": None, "lower_bound": -1.0, "upper_bound": 1.0,
                "target_q_x_coverage": supported_mass,
                "missing_target_histories": structural.unsupported_target_histories,
                "assigned_arm_unit_counts": tuple(arms),
                "temporal_resolution": evidence.manifest.get("temporal_resolution", "POINT_SAMPLE"),
                "abstention_reason": structural.reason, "input_sha256": evidence.sha256,
                "measurement_lower_bound": None, "measurement_upper_bound": None,
                "missing_interval_count": 0, "total_interval_count": 0,
                "inference_method": None, "inference_confidence_level": None,
                "inference_lower_bound": None, "inference_upper_bound": None,
                "hoeffding_range_sum_squares": None,
                "structural_support_sha256": structural.contract_sha256,
            }
            return ThetaAObservationAnalysisResult(**result_payload, output_sha256=_canonical_hash(result_payload))
        if evidence.manifest.get("temporal_resolution") == "INTERVAL_LEVEL":
            return self._analyze_interval(evidence, contract)
        if not evidence.rows:
            raise ContractError("theta_A Analyzer requires non-empty sealed evidence")
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("theta_A Analyzer received evidence with an invalid seal digest")
        rows = evidence.rows
        source_qx_sha256 = contract.source_q_x_sha256 or contract.q_x_sha256
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != source_qx_sha256
               or row.get("g_a0_sha256") != contract.g_a0_sha256
               or row.get("g_a1_sha256") != contract.g_a1_sha256
               or row.get("r_common_sha256") != contract.r_common_sha256
               for row in rows):
            raise ContractError("analysis contract fingerprints do not match sealed assignment/q_X provenance")
        qx = dict(contract.q_x_mass_by_history)
        observed_histories = {row["history_ref"] for row in rows}
        missing = tuple(sorted(set(qx) - observed_histories))
        unexpected = observed_histories - set(qx)
        if unexpected:
            raise ContractError("sealed evidence contains histories outside the q_X target support")
        by_unit: dict[str, dict[str, Any]] = {}
        for row in rows:
            unit = row["unit_id"]
            prior = by_unit.setdefault(unit, row)
            invariant = ("history_ref", "assignment_bundle_sha256", "q_x_sha256",
                         "g_a0_sha256", "g_a1_sha256", "r_common_sha256",
                         "assigned_arm", "assignment_probability", "assigned_vector_sha256",
                         "policy_fingerprint", "r_common_fingerprint", "history_id")
            if any(prior[k] != row[k] for k in invariant):
                raise ContractError("unit-level assignment/history fields vary across S3 observations")
        arms = [0, 0]
        for row in by_unit.values():
            arm = row["assigned_arm"]
            probability = row["assignment_probability"]
            if arm not in (0, 1) or not isinstance(probability, (int, float)) or not 0 < probability <= 1:
                raise ContractError("invalid assigned arm or assignment probability")
            arms[arm] += 1
        covered_mass = sum(qx[key] for key in observed_histories)
        # Distinguish missing target support / realized-arm support from the
        # temporal measurement limitation. All three prevent a point estimate,
        # but they are scientifically different reasons for abstention.
        if arms[0] == 0 or arms[1] == 0:
            identification = "INDETERMINATE"
            abstention_reason = "REALIZED_GA_ARM_SUPPORT_MISSING"
        elif missing:
            identification = "INDETERMINATE"
            abstention_reason = "TARGET_QX_SUPPORT_INCOMPLETE"
        else:
            identification = "PARTIALLY_IDENTIFIED"
            abstention_reason = "STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES"
        # Strict V_cont is binary, but point samples do not observe complete
        # interval continuity. The logical contrast bounds remain [-1,1].
        result_payload = {
            "run_id": evidence.run_id, "estimand_id": contract.estimand_id,
            "estimand_version": contract.estimand_version,
            "identification": identification, "point_estimate": None,
            "lower_bound": -1.0, "upper_bound": 1.0,
            "target_q_x_coverage": covered_mass,
            "missing_target_histories": missing,
            "assigned_arm_unit_counts": tuple(arms),
            "temporal_resolution": "POINT_SAMPLE",
            "abstention_reason": abstention_reason,
            "input_sha256": evidence.sha256,
            "measurement_lower_bound": None,
            "measurement_upper_bound": None,
            "missing_interval_count": 0,
            "total_interval_count": 0,
            "inference_method": None,
            "inference_confidence_level": None,
            "inference_lower_bound": None,
            "inference_upper_bound": None,
            "hoeffding_range_sum_squares": None,
            "structural_support_sha256": structural.contract_sha256 if structural else None,
        }
        return ThetaAObservationAnalysisResult(**result_payload,
            output_sha256=_canonical_hash(result_payload))


    @staticmethod
    def _bounded_ht_interval(contract, by_unit, qx, estimate, *, eligible):
        """Conservative finite-sample CI for the two-stage stochastic-policy HT target.

        The selected joint-vector draw is part of each unit's bounded [0,1]
        outcome. Independence is required across units for the complete
        arm-assignment plus within-policy vector randomization.
        """
        empty = {
            "inference_method": None,
            "inference_confidence_level": None,
            "inference_lower_bound": None,
            "inference_upper_bound": None,
            "hoeffding_range_sum_squares": None,
        }
        if contract.confidence_level is None or not eligible or estimate is None:
            return empty
        p1_by_history = dict(contract.probability_a1_by_history)
        range_sum_squares = 0.0
        for bucket in by_unit.values():
            first = bucket[0]
            history = first["history_ref"]
            p1 = p1_by_history[history]
            p0 = 1.0 - p1
            expected_assigned_probability = p1 if first["assigned_arm"] == 1 else p0
            if not math.isclose(first["assignment_probability"], expected_assigned_probability,
                                rel_tol=0.0, abs_tol=1e-12):
                raise ContractError("sealed assignment probability differs from inferential design contract")
            width = qx[history] * (1.0 / p1 + 1.0 / p0)
            range_sum_squares += width * width
        alpha = 1.0 - contract.confidence_level
        radius = math.sqrt(0.5 * range_sum_squares * math.log(2.0 / alpha))
        return {
            "inference_method": "HOEFFDING_TWO_STAGE_BOUNDED_HT_V1",
            "inference_confidence_level": contract.confidence_level,
            "inference_lower_bound": estimate - radius,
            "inference_upper_bound": estimate + radius,
            "hoeffding_range_sum_squares": range_sum_squares,
        }

    def _analyze_interval(self, evidence: SealedThetaAEvidence,
                          contract: ThetaAObservationAnalysisContract) -> ThetaAObservationAnalysisResult:
        """Use the design-unbiased q_X-standardized Horvitz-Thompson contrast."""
        if not evidence.rows or _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("interval Analyzer requires non-empty evidence with a valid seal")
        rows = evidence.rows
        if any(row.get("temporal_resolution") != "INTERVAL_LEVEL" for row in rows):
            raise ContractError("interval Analyzer cannot mix point and interval evidence")
        source_qx_sha256 = contract.source_q_x_sha256 or contract.q_x_sha256
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != source_qx_sha256
               or row.get("g_a0_sha256") != contract.g_a0_sha256
               or row.get("g_a1_sha256") != contract.g_a1_sha256
               or row.get("r_common_sha256") != contract.r_common_sha256 for row in rows):
            raise ContractError("interval evidence fingerprints do not match analysis contract")
        qx = dict(contract.q_x_mass_by_history)
        by_unit = {}
        for row in rows:
            unit = row["unit_id"]
            bucket = by_unit.setdefault(unit, [])
            bucket.append(row)
        observed_histories = {bucket[0]["history_ref"] for bucket in by_unit.values()}
        missing_histories = tuple(sorted(set(qx) - observed_histories))
        if observed_histories - set(qx):
            raise ContractError("interval evidence contains histories outside q_X support")
        invariant_fields = ("history_ref", "assignment_bundle_sha256", "q_x_sha256",
                            "g_a0_sha256", "g_a1_sha256", "r_common_sha256",
                            "assigned_arm", "assignment_probability", "assigned_vector_sha256",
                            "policy_fingerprint", "r_common_fingerprint", "history_id",
                            "history_version", "history_content_sha256")
        arm_units = [[], []]
        missing_count = 0
        total_count = 0
        common_grid = None
        common_bounds = None
        for unit, bucket in by_unit.items():
            first = bucket[0]
            if any(any(row[k] != first[k] for k in invariant_fields) for row in bucket):
                raise ContractError("interval unit assignment/history provenance is inconsistent")
            ordered = sorted(bucket, key=lambda row: row["interval_index"])
            if [row["interval_index"] for row in ordered] != list(range(len(ordered))):
                raise ContractError("interval evidence has gaps or duplicate interval indices")
            grid = (ordered[0]["grid_id"], ordered[0]["grid_version"])
            bounds = tuple((row["interval_start"], row["interval_end"]) for row in ordered)
            if any((row["grid_id"], row["grid_version"]) != grid for row in ordered):
                raise ContractError("interval evidence grid identity changes within a unit")
            if any(left[1] != right[0] for left, right in zip(bounds, bounds[1:])):
                raise ContractError("interval evidence contains a temporal gap or overlap")
            if common_grid is None:
                common_grid, common_bounds = grid, bounds
            elif grid != common_grid or bounds != common_bounds:
                raise ContractError("interval evidence must use one common grid across q_X units")
            if first["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE":
                raise ContractError("interval evidence lacks certified continuous coverage")
            successes = sum(row["observed_compliance"] is True for row in ordered)
            missing = sum(row["observation_status"] == "MISSING" for row in ordered)
            if any(row["observation_status"] == "OBSERVED" and type(row["observed_compliance"]) is not bool
                   for row in ordered):
                raise ContractError("observed interval compliance must be Boolean")
            n = len(ordered)
            if n == 0:
                raise ContractError("each q_X unit must have a non-empty interval record sequence")
            missing_count += missing
            total_count += n
            lower_y, upper_y = successes / n, (successes + missing) / n
            arm = first["assigned_arm"]
            probability = first["assignment_probability"]
            if arm not in (0, 1) or not isinstance(probability, (int, float)) or not 0 < probability <= 1:
                raise ContractError("invalid interval assignment arm/probability")
            arm_units[arm].append((qx[first["history_ref"]] / probability, lower_y, upper_y))
        arm_counts = tuple(len(items) for items in arm_units)
        covered_mass = sum(qx[key] for key in observed_histories)
        if 0 in arm_counts or missing_histories:
            identification, reason, estimate = "INDETERMINATE", (
                "REALIZED_GA_ARM_SUPPORT_MISSING" if 0 in arm_counts
                else "TARGET_QX_SUPPORT_INCOMPLETE"
            ), None
            measurement_lower = measurement_upper = None
        else:
            arm_lower = [sum(w * lo for w, lo, hi in items)
                         for items in arm_units]
            arm_upper = [sum(w * hi for w, lo, hi in items)
                         for items in arm_units]
            measurement_lower = arm_lower[1] - arm_upper[0]
            measurement_upper = arm_upper[1] - arm_lower[0]
            if missing_count:
                identification, reason, estimate = "INDETERMINATE", (
                    "INTERVAL_MISSINGNESS_REQUIRES_ABSTENTION"
                ), None
            else:
                identification, reason = "IDENTIFIED", ""
                # Horvitz-Thompson preserves the declared q_X target masses
                # and is design-unbiased under the recorded arm probabilities.
                # Its finite-sample value may lie outside the parameter range;
                # it is never clipped.
                estimate = arm_lower[1] - arm_lower[0]
        inference = self._bounded_ht_interval(
            contract, by_unit, qx, estimate,
            eligible=(identification == "IDENTIFIED" and missing_count == 0),
        )
        result_payload = {
            "run_id": evidence.run_id, "estimand_id": contract.estimand_id,
            "estimand_version": contract.estimand_version,
            "identification": identification, "point_estimate": estimate,
            # These are logical causal-contrast bounds. Measurement-only bounds
            # are reported separately and are never mislabelled as truth bounds.
            "lower_bound": -1.0, "upper_bound": 1.0,
            "target_q_x_coverage": covered_mass,
            "missing_target_histories": missing_histories,
            "assigned_arm_unit_counts": arm_counts,
            "temporal_resolution": "INTERVAL_LEVEL",
            "abstention_reason": reason,
            "input_sha256": evidence.sha256,
            "measurement_lower_bound": measurement_lower,
            "measurement_upper_bound": measurement_upper,
            "missing_interval_count": missing_count,
            "total_interval_count": total_count,
            **inference,
        }
        return ThetaAObservationAnalysisResult(**result_payload,
            output_sha256=_canonical_hash(result_payload))


@dataclass(frozen=True)
class ThetaAStructuralSupportRow:
    """One positive-mass target history and its source/policy support facts.

    This is a test-harness adjudication input, not a population roster and
    not authorization to materialize any B1/UE target population.
    """
    history_ref: str
    target_mass: float
    source_mass: float
    intervention_defined: bool
    g_a0_feasible: bool
    g_a1_feasible: bool
    assignment_probability_a1: float


@dataclass(frozen=True)
class ThetaAStructuralSupportContract:
    """Versioned separation of target mass, source support and policy feasibility."""
    contract_id: str
    contract_version: str
    target_q_x_sha256: str
    source_q_x_sha256: str
    rows: tuple[ThetaAStructuralSupportRow, ...]

    def validate(self) -> None:
        if not all((self.contract_id, self.contract_version,
                    self.target_q_x_sha256, self.source_q_x_sha256)):
            raise ContractError("structural-support contract identity and both distribution fingerprints are required")
        refs = [row.history_ref for row in self.rows]
        if not refs or len(refs) != len(set(refs)):
            raise ContractError("structural-support rows require unique positive-mass target histories")
        if not math.isclose(sum(row.target_mass for row in self.rows), 1.0,
                            rel_tol=0.0, abs_tol=1e-10):
            raise ContractError("structural-support target masses must sum to one")
        for row in self.rows:
            if not row.history_ref or not math.isfinite(row.target_mass) or row.target_mass <= 0:
                raise ContractError("each structural-support row requires a positive finite target mass")
            if not math.isfinite(row.source_mass) or row.source_mass < 0:
                raise ContractError("source mass must be finite and non-negative")
            if any(type(value) is not bool for value in
                   (row.intervention_defined, row.g_a0_feasible, row.g_a1_feasible)):
                raise ContractError("intervention definition and policy feasibility must be explicit Booleans")
            if (not math.isfinite(row.assignment_probability_a1)
                    or not 0.0 < row.assignment_probability_a1 < 1.0):
                raise ContractError("both focal policy assignment probabilities must be strictly positive")


@dataclass(frozen=True)
class ThetaAStructuralSupportAdjudication:
    status: str
    reason: str
    unsupported_target_histories: tuple[str, ...]
    contract_sha256: str


def adjudicate_theta_a_structural_support(
    contract: ThetaAStructuralSupportContract,
) -> ThetaAStructuralSupportAdjudication:
    """Adjudicate structural target/source support before inspecting outcomes.

    Undefined/infeasible interventions are contract errors, not non-identification.
    A well-defined policy contrast with target mass outside source support is
    NOT_IDENTIFIED. Realized sample-arm/evidence failures remain Analyzer-level
    INDETERMINATE results and are not inferred here.
    """
    contract.validate()
    for row in contract.rows:
        if not row.intervention_defined:
            raise ContractError(
                f"theta_A intervention is undefined for positive-mass target history {row.history_ref}"
            )
        if not row.g_a0_feasible or not row.g_a1_feasible:
            raise ContractError(
                f"theta_A policy is structurally infeasible for positive-mass target history {row.history_ref}"
            )
    unsupported = tuple(sorted(
        row.history_ref for row in contract.rows if row.source_mass <= 0.0
    ))
    status = "NOT_IDENTIFIED" if unsupported else "STRUCTURAL_SUPPORT_SUFFICIENT"
    reason = "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT" if unsupported else ""
    return ThetaAStructuralSupportAdjudication(
        status, reason, unsupported, _canonical_hash(contract)
    )
