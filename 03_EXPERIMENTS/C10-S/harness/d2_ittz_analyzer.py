"""Observation-only ITT-Z Analyzer for the D2 strict V_cont S3 lane."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any

from c10s_synthetic_components import ContractError, SyntheticWorldBundle, digest
from d2_interval_observation import SealedD2IntervalEvidence, _hash


@dataclass(frozen=True)
class D2ITTZAnalysisContract:
    q_x_mass_by_history: tuple[tuple[str, float], ...]
    q_x_sha256: str
    assignment_bundle_sha256: str
    assignment_mechanism_id: str
    assignment_mechanism_version: str
    estimand_id: str = "ITT_Z_D2_VCONT_QX"
    estimand_version: str = "1.0"
    confidence_level: float = 0.95

    def validate(self) -> None:
        mapping = dict(self.q_x_mass_by_history)
        if not mapping or len(mapping) != len(self.q_x_mass_by_history):
            raise ContractError("ITT-Z q_X masses must have unique non-empty history support")
        if any(not key or not math.isfinite(value) or value <= 0 for key, value in mapping.items()):
            raise ContractError("ITT-Z q_X masses must be finite and strictly positive")
        if not math.isclose(sum(mapping.values()), 1.0, rel_tol=0.0, abs_tol=1e-10):
            raise ContractError("ITT-Z q_X masses must sum to one")
        if not 0.0 < self.confidence_level < 1.0:
            raise ContractError("ITT-Z randomization confidence level must be in (0,1)")
        if not all((self.q_x_sha256, self.assignment_bundle_sha256,
                    self.assignment_mechanism_id, self.assignment_mechanism_version,
                    self.estimand_id, self.estimand_version)):
            raise ContractError("ITT-Z analysis requires assignment/q_X/estimand provenance")


@dataclass(frozen=True)
class D2ITTZAnalysisResult:
    run_id: str
    estimand_id: str
    estimand_version: str
    identification: str
    point_estimate: float | None
    lower_bound: float
    upper_bound: float
    randomization_lower_bound: float | None
    randomization_upper_bound: float | None
    hoeffding_radius: float | None
    randomization_confidence_level: float | None
    target_q_x_coverage: float
    missing_target_histories: tuple[str, ...]
    assigned_z_unit_counts: tuple[int, int]
    missing_interval_count: int
    total_interval_count: int
    abstention_reason: str
    input_sha256: str
    output_sha256: str


def _result_payload(result: D2ITTZAnalysisResult) -> dict[str, Any]:
    return {
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
    }


def _output_hash(payload: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False, allow_nan=False).encode()).hexdigest()


class D2ITTZAnalyzer:
    """Estimate the randomized D2 package ITT; no potential truth is accepted."""

    version = "c10s-d2-ittz-analyzer-0.1"

    def analyze(
        self,
        evidence: SealedD2IntervalEvidence,
        contract: D2ITTZAnalysisContract,
    ) -> D2ITTZAnalysisResult:
        contract.validate()
        if not evidence.rows or _hash({"manifest": evidence.manifest, "rows": list(evidence.rows)}) != evidence.sha256:
            raise ContractError("ITT-Z Analyzer requires non-empty sealed evidence with valid digest")
        manifest = evidence.manifest
        if manifest.get("temporal_resolution") != "INTERVAL_LEVEL":
            raise ContractError("ITT-Z strict V_cont requires interval-level evidence")
        if (manifest.get("row_count") != len(evidence.rows)
                or not isinstance(manifest.get("unit_count"), int)
                or manifest.get("unit_count") < 1
                or not isinstance(manifest.get("expected_unit_count"), int)
                or manifest.get("expected_unit_count") < manifest.get("unit_count")
                or not isinstance(manifest.get("expected_unit_history_refs"), (tuple, list))
                or not isinstance(manifest.get("missing_unit_ids"), (tuple, list))
                or not isinstance(manifest.get("interval_count_per_unit"), int)
                or manifest.get("interval_count_per_unit") < 1):
            raise ContractError("ITT-Z sealed manifest counts/roster are missing or inconsistent")
        expected_pairs = tuple(tuple(row) for row in manifest["expected_unit_history_refs"])
        expected_assignments = tuple(tuple(row) for row in manifest.get("expected_unit_assignments", ()))
        expected_ids = [row[0] for row in expected_pairs]
        expected_refs = [row[1] for row in expected_pairs]
        assignment_ids = [row[0] for row in expected_assignments]
        if (len(expected_pairs) != manifest["expected_unit_count"]
                or len(expected_ids) != len(set(expected_ids))
                or len(expected_refs) != len(set(expected_refs))
                or set(expected_refs) != set(contract_history for contract_history, _ in contract.q_x_mass_by_history)
                or len(expected_assignments) != manifest["expected_unit_count"]
                or len(assignment_ids) != len(set(assignment_ids))
                or set(assignment_ids) != set(expected_ids)
                or any(type(row[2]) is not int or row[2] not in (0, 1)
                       or not 0.0 < row[3] < 1.0 or not 0.0 < row[4] < 1.0
                       or abs(row[3] + row[4] - 1.0) > 1e-12
                       for row in expected_assignments)):
            raise ContractError("ITT-Z sealed expected roster/assignment metadata does not map one-to-one onto q_X* support")
        qx = dict(contract.q_x_mass_by_history)
        by_unit: dict[str, list[dict[str, Any]]] = {}
        for row in evidence.rows:
            if row.get("run_id") != evidence.run_id:
                raise ContractError("ITT-Z evidence contains a foreign run identity")
            if (row.get("grid_id"), row.get("grid_version"),
                    row.get("monitor_id"), row.get("monitor_version")) != (
                    manifest.get("grid_id"), manifest.get("grid_version"),
                    manifest.get("monitor_id"), manifest.get("monitor_version")
                    ):
                raise ContractError("ITT-Z row grid/monitor identity differs from sealed manifest")
            if (row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
                    or row.get("q_x_sha256") != contract.q_x_sha256
                    or row.get("assignment_mechanism_id") != contract.assignment_mechanism_id
                    or row.get("assignment_mechanism_version") != contract.assignment_mechanism_version):
                raise ContractError("ITT-Z analysis contract does not match sealed assignment provenance")
            by_unit.setdefault(row["unit_id"], []).append(row)
        if len(by_unit) != manifest["unit_count"]:
            raise ContractError("ITT-Z sealed manifest unit count differs from observed evidence")
        expected_by_unit = dict(expected_pairs)
        if not set(by_unit).issubset(expected_by_unit):
            raise ContractError("ITT-Z evidence contains units outside the declared randomized roster")
        observed_history_by_unit = {
            unit: rows[0]["history_ref"] for unit, rows in by_unit.items()
        }
        if any(expected_by_unit[unit] != history_ref
               for unit, history_ref in observed_history_by_unit.items()):
            raise ContractError("ITT-Z observed unit/history mapping differs from sealed expected roster")
        if tuple(sorted(set(expected_by_unit) - set(by_unit))) != tuple(sorted(manifest["missing_unit_ids"])):
            raise ContractError("ITT-Z sealed missing-unit manifest does not match observed roster")
        if len(by_unit) > len(qx):
            raise ContractError("ITT-Z evidence contains more units than q_X target support")
        expected_interval_count = manifest["interval_count_per_unit"]
        observed_bounds = None
        for unit, rows in by_unit.items():
            ordered = sorted(rows, key=lambda row: row["interval_index"])
            if len(ordered) != expected_interval_count:
                raise ContractError(f"ITT-Z interval count differs from manifest for {unit}")
            bounds = tuple((row["interval_start"], row["interval_end"]) for row in ordered)
            if observed_bounds is None:
                observed_bounds = bounds
            elif bounds != observed_bounds:
                raise ContractError("ITT-Z units do not share the same interval grid boundaries")
        observed_histories = {rows[0]["history_ref"] for rows in by_unit.values()}
        unexpected = observed_histories - set(qx)
        if unexpected:
            raise ContractError("ITT-Z evidence contains histories outside q_X target support")
        missing_histories = tuple(sorted(set(qx) - observed_histories))
        arm: list[list[tuple[float, int, int]]] = [[], []]
        randomization_range_sq = 0.0
        missing_count = total_count = 0
        for unit, rows in by_unit.items():
            first = rows[0]
            invariant = (
                "world_id", "world_version", "dgp_id", "dgp_version", "history_ref",
                "assignment_bundle_sha256", "q_x_sha256", "assignment_mechanism_id",
                "assignment_mechanism_version", "assigned_z", "probability_z0",
                "probability_z1", "assignment_probability", "assignment_uniform_sha256",
                "selected_potential_id", "history_id", "history_version",
                "history_content_sha256", "grid_id", "grid_version", "monitor_id",
                "monitor_version",
            )
            if any(any(row.get(k) != first.get(k) for k in invariant) for row in rows):
                raise ContractError("ITT-Z unit has inconsistent assignment/history provenance")
            ordered = sorted(rows, key=lambda row: row["interval_index"])
            if [row["interval_index"] for row in ordered] != list(range(len(ordered))):
                raise ContractError("ITT-Z interval sequence has gaps or duplicate indices")
            if any(left["interval_end"] != right["interval_start"] for left, right in zip(ordered, ordered[1:])):
                raise ContractError("ITT-Z interval sequence is not contiguous")
            if first["coverage_mode"] != "CONTINUOUS_EVENT_COVERAGE":
                raise ContractError("ITT-Z strict V_cont requires continuous event coverage")
            z = first["assigned_z"]
            p = first["assignment_probability"]
            if type(z) is not int or z not in (0, 1) or not isinstance(p, (int, float)) or not 0 < p <= 1:
                raise ContractError("ITT-Z assigned arm/probability is invalid")
            if abs(first["probability_z0"] + first["probability_z1"] - 1.0) > 1e-12:
                raise ContractError("ITT-Z assignment probabilities do not sum to one")
            expected_p = first["probability_z1"] if z else first["probability_z0"]
            if abs(p - expected_p) > 1e-12:
                raise ContractError("ITT-Z realized assignment probability mismatch")
            if any(row["observation_status"] not in ("OBSERVED", "MISSING") for row in ordered):
                raise ContractError("ITT-Z invalid interval observation status")
            if any((row["observation_status"] == "MISSING") != (row["observed_compliance"] is None)
                   for row in ordered):
                raise ContractError("ITT-Z interval missingness/value mismatch")
            if any(row["observation_status"] == "OBSERVED" and type(row["observed_compliance"]) is not bool
                   for row in ordered):
                raise ContractError("ITT-Z observed compliance must be Boolean")
            # Strict continuity is a conjunction across time, not an interval mean.
            any_failure = any(row["observed_compliance"] is False for row in ordered)
            any_missing = any(row["observation_status"] == "MISSING" for row in ordered)
            y_lower = 0 if any_failure or any_missing else 1
            y_upper = 0 if any_failure else 1
            missing_count += sum(row["observation_status"] == "MISSING" for row in ordered)
            total_count += len(ordered)
            mass = qx[first["history_ref"]]
            arm[z].append((mass / p, y_lower, y_upper))
            p1 = first["probability_z1"]
            p0 = first["probability_z0"]
            contribution_range = mass * (1.0 / p1 + 1.0 / p0)
            randomization_range_sq += contribution_range * contribution_range
        # Unit-level nonresponse contributes an unknown binary strict-V_cont
        # outcome to its known randomized arm. This bounds the realized HT
        # contrast; it is not a confidence interval or causal identification bound.
        expected_assignment_by_unit = {row[0]: row for row in expected_assignments}
        observed_unit_ids = set(by_unit)
        for unit_id in sorted(set(expected_assignment_by_unit) - observed_unit_ids):
            _, history_ref, z, p0, p1 = expected_assignment_by_unit[unit_id]
            mass = qx[history_ref]
            p = p1 if z == 1 else p0
            arm[z].append((mass / p, 0, 1))
            randomization_range_sq += (mass * (1.0 / p1 + 1.0 / p0)) ** 2
        counts = (len(arm[0]) - len(missing_unit_ids), len(arm[1]) - len(missing_unit_ids))
        coverage = sum(qx[key] for key in observed_histories)
        randomization_lower = randomization_upper = radius = confidence_level = None
        mu_lower = [sum(w * lo for w, lo, hi in values) for values in arm]
        mu_upper = [sum(w * hi for w, lo, hi in values) for values in arm]
        lower = mu_lower[1] - mu_upper[0]
        upper = mu_upper[1] - mu_lower[0]
        if missing_count or missing_unit_ids:
            identification, estimate = "PARTIALLY_IDENTIFIED", None
            reasons = []
            if missing_unit_ids:
                reasons.append("UNIT_NONRESPONSE")
            if missing_count:
                reasons.append("INTERVAL_MISSINGNESS")
            reason = "_AND_".join(reasons) + "_PREVENTS_STRICT_VCONT_POINT_RECOVERY"
        else:
            identification, reason = "IDENTIFIED", ""
            estimate = mu_lower[1] - mu_lower[0]
            confidence_level = contract.confidence_level
            alpha = 1.0 - confidence_level
            radius = math.sqrt(0.5 * randomization_range_sq * math.log(2.0 / alpha))
            randomization_lower = max(-1.0, estimate - radius)
            randomization_upper = min(1.0, estimate + radius)
        payload = {
            "run_id": evidence.run_id, "estimand_id": contract.estimand_id,
            "estimand_version": contract.estimand_version,
            "identification": identification, "point_estimate": estimate,
            "lower_bound": lower, "upper_bound": upper,
            "randomization_lower_bound": randomization_lower,
            "randomization_upper_bound": randomization_upper,
            "hoeffding_radius": radius,
            "randomization_confidence_level": confidence_level,
            "target_q_x_coverage": coverage, "missing_target_histories": missing_histories,
            "assigned_z_unit_counts": counts, "missing_interval_count": missing_count,
            "total_interval_count": total_count, "abstention_reason": reason,
            "input_sha256": evidence.sha256,
        }
        result = D2ITTZAnalysisResult(**payload, output_sha256=_output_hash(payload))
        return result


def analysis_contract_from_world(
    world: SyntheticWorldBundle,
    assignment_bundle_sha256: str,
    assignment_mechanism_id: str,
    assignment_mechanism_version: str,
) -> D2ITTZAnalysisContract:
    world.validate()
    return D2ITTZAnalysisContract(
        tuple((row.history_ref, row.mass) for row in world.q_x),
        digest(world.q_x),
        assignment_bundle_sha256, assignment_mechanism_id, assignment_mechanism_version,
    )
