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

from theta_a_observation_harness import SealedThetaAEvidence
from c10s_synthetic_components import ContractError


@dataclass(frozen=True)
class ThetaAObservationAnalysisContract:
    q_x_mass_by_history: tuple[tuple[str, float], ...]
    q_x_sha256: str
    assignment_bundle_sha256: str
    estimand_id: str = "THETA_A_QX_GA_RCOMMON_VCONT"
    estimand_version: str = "1.0"

    def validate(self) -> None:
        if not self.q_x_sha256 or not self.assignment_bundle_sha256:
            raise ContractError("theta_A analysis requires q_X and assignment-bundle fingerprints")
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


def _canonical_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class ThetaAObservationAnalyzer:
    """Analyze sealed focal observations without access to DGP truth."""

    version = "c10s-theta-a-observation-analyzer-0.1"

    def analyze(self, evidence: SealedThetaAEvidence,
                contract: ThetaAObservationAnalysisContract) -> ThetaAObservationAnalysisResult:
        contract.validate()
        if not evidence.rows:
            raise ContractError("theta_A Analyzer requires non-empty sealed evidence")
        rows = evidence.rows
        if any(row.get("assignment_bundle_sha256") != contract.assignment_bundle_sha256
               or row.get("q_x_sha256") != contract.q_x_sha256 for row in rows):
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
            invariant = ("history_ref", "assigned_arm", "assignment_probability",
                         "assigned_vector_sha256", "policy_fingerprint",
                         "r_common_fingerprint", "history_id")
            if any(prior[k] != row[k] for k in invariant):
                raise ContractError("unit-level assignment/history fields vary across S3 observations")
        arms = [0, 0]
        for row in by_unit.values():
            arm = row["assigned_arm"]
            probability = row["assignment_probability"]
            if arm not in (0, 1) or not isinstance(probability, (int, float)) or not 0 < probability <= 1:
                raise ContractError("invalid assigned arm or assignment probability")
            arms[arm] += 1
        if arms[0] == 0 or arms[1] == 0:
            raise ContractError("both randomized g_A arms must be represented")
        covered_mass = sum(qx[key] for key in observed_histories)
        # Strict V_cont is binary, but no row observes the complete interval.
        # Point samples constrain instants only; absent an approved temporal
        # observation model, each arm-specific target mean remains in [0,1].
        # The sharp contrast bound is consequently [-1,1], even with full q_X
        # support. This is a bound, not an estimate and not evidence of effect.
        result_payload = {
            "run_id": evidence.run_id, "estimand_id": contract.estimand_id,
            "estimand_version": contract.estimand_version,
            "identification": "PARTIALLY_IDENTIFIED", "point_estimate": None,
            "lower_bound": -1.0, "upper_bound": 1.0,
            "target_q_x_coverage": covered_mass,
            "missing_target_histories": missing,
            "assigned_arm_unit_counts": tuple(arms),
            "temporal_resolution": "POINT_SAMPLE",
            "abstention_reason": "STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES",
            "input_sha256": evidence.sha256,
        }
        return ThetaAObservationAnalysisResult(**result_payload,
            output_sha256=_canonical_hash(result_payload))