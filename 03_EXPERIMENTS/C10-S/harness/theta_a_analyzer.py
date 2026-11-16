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


def _canonical_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class ThetaAObservationAnalyzer:
    """Analyze sealed focal observations without access to DGP truth."""

    version = "c10s-theta-a-observation-analyzer-0.1"

    def analyze(self, evidence: SealedThetaAEvidence,
                contract: ThetaAObservationAnalysisContract) -> ThetaAObservationAnalysisResult:
        contract.validate()
        if evidence.manifest.get("temporal_resolution") == "INTERVAL_LEVEL":
            return self._analyze_interval(evidence, contract)
        if not evidence.rows:
            raise ContractError("theta_A Analyzer requires non-empty sealed evidence")
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("theta_A Analyzer received evidence with an invalid seal digest")
        rows = evidence.rows
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != contract.q_x_sha256
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
        if missing:
            identification = "INDETERMINATE"
            abstention_reason = "TARGET_QX_SUPPORT_INCOMPLETE"
        elif arms[0] == 0 or arms[1] == 0:
            identification = "INDETERMINATE"
            abstention_reason = "REALIZED_GA_ARM_SUPPORT_MISSING"
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
        }
        return ThetaAObservationAnalysisResult(**result_payload,
            output_sha256=_canonical_hash(result_payload))

    def _analyze_interval(self, evidence: SealedThetaAEvidence,
                          contract: ThetaAObservationAnalysisContract) -> ThetaAObservationAnalysisResult:
        """Analyze interval evidence; keep missingness bounds distinct from causal bounds."""
        if not evidence.rows or _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise ContractError("interval Analyzer requires non-empty evidence with a valid seal")
        rows = evidence.rows
        if any(row.get("temporal_resolution") != "INTERVAL_LEVEL" for row in rows):
            raise ContractError("interval Analyzer cannot mix point and interval evidence")
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != contract.q_x_sha256
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
        if missing_histories or 0 in arm_counts:
            identification, reason, estimate = "INDETERMINATE", (
                "TARGET_QX_SUPPORT_INCOMPLETE" if missing_histories else "REALIZED_GA_ARM_SUPPORT_MISSING"
            ), None
            measurement_lower = measurement_upper = None
        else:
            denominators = [sum(item[0] for item in items) for items in arm_units]
            if any(value <= 0 or not math.isfinite(value) for value in denominators):
                raise ContractError("interval IPW/Hajek arm weights must have positive finite totals")
            arm_lower = [sum(w * lo for w, lo, hi in items) / denominators[a]
                         for a, items in enumerate(arm_units)]
            arm_upper = [sum(w * hi for w, lo, hi in items) / denominators[a]
                         for a, items in enumerate(arm_units)]
            measurement_lower = arm_lower[1] - arm_upper[0]
            measurement_upper = arm_upper[1] - arm_lower[0]
            if missing_count:
                identification, reason, estimate = "PARTIALLY_IDENTIFIED", (
                    "INTERVAL_MISSINGNESS_REQUIRES_ABSTENTION"
                ), None
            else:
                identification, reason = "IDENTIFIED", ""
                estimate = arm_lower[1] - arm_lower[0]
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
        }
        return ThetaAObservationAnalysisResult(**result_payload,
            output_sha256=_canonical_hash(result_payload))
