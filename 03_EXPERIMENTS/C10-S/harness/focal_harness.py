"""C10-S focal synthetic harness (methodological implementation slice).

Scope: randomized two-policy accessibility mixture with B1 value Q_B1.
This module is parameterized: it has no confirmatory defaults and performs
no run at import time. Truth and observed evidence use separate objects.
The Analyzer API accepts only sealed observed evidence and a public contract.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
import random
from statistics import mean, variance
from typing import Any, Literal


Identification = Literal["IDENTIFIED", "PARTIALLY_IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"]
DirectPathStatus = Literal["ABSENT", "PRESENT", "UNKNOWN"]


class ContractError(ValueError):
    """A required scenario or analysis-contract condition is invalid."""


class FirewallError(RuntimeError):
    """A role boundary or sealed-artifact integrity check failed."""


@dataclass(frozen=True)
class ScenarioConfig:
    scenario_id: str
    scenario_version: str
    n_units: int
    seed: int
    pi0: float
    k_slots: int
    lambda0: float
    lambda1: float
    p01_base: float
    p10_base: float
    alpha01: float
    alpha10: float
    gamma01: float
    gamma10: float
    assignment_probability: float
    direct_path_status: DirectPathStatus
    measurement_ideal: bool
    interference_absent: bool

    def validate(self) -> None:
        if not self.scenario_id.strip() or not self.scenario_version.strip():
            raise ContractError("scenario identity and version are required")
        if self.n_units < 4 or self.n_units % 2:
            raise ContractError("n_units must be even and >= 4 for balanced assignment")
        if self.k_slots < 1:
            raise ContractError("k_slots must be >= 1")
        for name in ("pi0", "lambda0", "lambda1", "p01_base", "p10_base", "assignment_probability"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ContractError(f"{name} must be in [0, 1]")
        if not 0.0 < self.lambda0 < self.lambda1 < 1.0:
            raise ContractError("common support requires 0 < lambda0 < lambda1 < 1")
        if not 0.0 < self.assignment_probability < 1.0:
            raise ContractError("assignment_probability must be strictly between 0 and 1")
        if self.p01_base in (0.0, 1.0) or self.p10_base in (0.0, 1.0):
            raise ContractError("baseline transition probabilities must be strictly between 0 and 1")
        if self.direct_path_status not in ("ABSENT", "PRESENT", "UNKNOWN"):
            raise ContractError("direct_path_status must be ABSENT, PRESENT or UNKNOWN")
        if not all(math.isfinite(value) for value in
                   (self.alpha01, self.alpha10, self.gamma01, self.gamma10)):
            raise ContractError("transition effects must be finite numbers")
        if self.direct_path_status == "ABSENT" and (self.gamma01 != 0.0 or self.gamma10 != 0.0):
            raise ContractError("cannot declare direct paths ABSENT when gamma is non-zero")


@dataclass(frozen=True)
class AnalysisContract:
    estimand_id: str
    estimand_version: str
    randomized_assignment: bool
    direct_path_status: DirectPathStatus
    common_regime: bool
    positivity: bool
    version_consistency: bool
    measurement_ideal: bool
    interference_absent: bool

    def validate(self) -> None:
        if not self.estimand_id.strip() or not self.estimand_version.strip():
            raise ContractError("estimand identity and version are required")
        if self.direct_path_status not in ("ABSENT", "PRESENT", "UNKNOWN"):
            raise ContractError("direct_path_status must be explicit")


@dataclass(frozen=True)
class RunManifest:
    run_id: str
    scenario_id: str
    scenario_version: str
    n_units: int
    k_slots: int
    generator_version: str


@dataclass(frozen=True)
class TruthBundle:
    run_id: str
    potential_q_by_z: tuple[tuple[float, float], ...]
    signature_d1_by_z: tuple[tuple[int, int], ...]
    theta_access_truth: float
    itt_value_truth: float
    direct_path_truth: bool
    seed: int


@dataclass(frozen=True)
class GeneratedSource:
    """Restricted pre-projection source; never passed to Analyzer."""
    run_id: str
    rows: tuple[dict[str, Any], ...]


@dataclass(frozen=True)
class EvidenceCandidate:
    run_id: str
    rows: tuple[dict[str, Any], ...]


@dataclass(frozen=True)
class SealedEvidence:
    run_id: str
    rows: tuple[dict[str, Any], ...]
    manifest: dict[str, Any]
    sha256: str


@dataclass(frozen=True)
class AnalyzerResult:
    run_id: str
    estimand_id: str
    estimand_version: str
    package_identification: Identification
    focal_identification: Identification
    package_itt_estimate: float | None
    package_itt_standard_error: float | None
    package_itt_interval_95: tuple[float, float] | None
    focal_estimate: float | None
    focal_standard_error: float | None
    focal_interval_95: tuple[float, float] | None
    abstention_reason: str | None
    input_sha256: str
    output_sha256: str


@dataclass(frozen=True)
class EvaluationReport:
    run_id: str
    analyzer_output_sha256: str
    package_abs_error: float | None
    focal_abs_error: float | None
    package_recovery: bool
    focal_recovery: bool | None
    classification_correct: bool
    notes: tuple[str, ...]


def _logit(p: float) -> float:
    return math.log(p / (1.0 - p))


def _expit(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))



def _beta_continued_fraction(a: float, b: float, x: float) -> float:
    """Numerically stable continued fraction for the incomplete beta function."""
    max_iter, eps, tiny = 300, 3.0e-14, 1.0e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            return h
    raise ArithmeticError("incomplete-beta continued fraction did not converge")


def _regularized_beta(x: float, a: float, b: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    factor = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                      + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return factor * _beta_continued_fraction(a, b, x) / a
    return 1.0 - factor * _beta_continued_fraction(b, a, 1.0 - x) / b


def _student_t_cdf(value: float, degrees_freedom: float) -> float:
    if degrees_freedom <= 0.0:
        raise ValueError("degrees of freedom must be positive")
    if value == 0.0:
        return 0.5
    x = degrees_freedom / (degrees_freedom + value * value)
    tail = 0.5 * _regularized_beta(x, degrees_freedom / 2.0, 0.5)
    return 1.0 - tail if value > 0.0 else tail


def _student_t_critical_975(degrees_freedom: float) -> float:
    """Two-sided 95% Student-t critical value, found by monotone bisection."""
    if degrees_freedom <= 0.0:
        raise ValueError("degrees of freedom must be positive")
    low, high = 0.0, 2.0
    while _student_t_cdf(high, degrees_freedom) < 0.975:
        high *= 2.0
    for _ in range(100):
        mid = (low + high) / 2.0
        if _student_t_cdf(mid, degrees_freedom) < 0.975:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def _mean_q(pi0: float, k: int, p01: float, p10: float) -> float:
    state_probability = pi0
    total = 0.0
    for _ in range(k):
        state_probability = p01 + (1.0 - p01 - p10) * state_probability
        total += state_probability
    return total / k


def _canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class Generator:
    version = "c10s-focal-generator-0.1"

    def generate(self, config: ScenarioConfig) -> tuple[RunManifest, TruthBundle, GeneratedSource]:
        config.validate()
        rng = random.Random(config.seed)
        # Include every declared DGP parameter in the run identity; scenario labels alone
        # are not sufficient provenance when a parameter changes.
        run_id = _canonical_hash(asdict(config))[:24]
        base01, base10 = _logit(config.p01_base), _logit(config.p10_base)
        potential: list[tuple[float, float]] = []
        signatures: list[tuple[int, int]] = []
        observed_rows: list[dict[str, Any]] = []
        truth_rows: list[tuple[float, float]] = []

        for index in range(config.n_units):
            initial = 1 if rng.random() < config.pi0 else 0
            signature_uniform = rng.random()
            d0 = int(signature_uniform < config.lambda0)
            d1 = int(signature_uniform < config.lambda1)
            q_potentials: list[float] = []
            for z, signature in ((0, d0), (1, d1)):
                state = initial
                available = 0
                p01 = _expit(base01 + config.alpha01 * signature + config.gamma01 * z)
                p10 = _expit(base10 + config.alpha10 * signature + config.gamma10 * z)
                for _ in range(config.k_slots):
                    draw = rng.random()
                    state = (1 if draw < p01 else 0) if state == 0 else (0 if draw < p10 else 1)
                    available += state
                q_potentials.append(available / config.k_slots)
            q0, q1 = q_potentials
            z = 1 if rng.random() < config.assignment_probability else 0
            q_observed = q1 if z else q0
            potential.append((q0, q1))
            signatures.append((d0, d1))
            truth_rows.append((q0, q1))
            observed_rows.append({"unit_id": f"UE-{index + 1:06d}", "assignment_z": z,
                                  "q_b1_observed": q_observed, "observation_status": "OBSERVED"})

        # The focal accessibility contrast is evaluated under a common direct-path regime (gamma=0).
        p01_0, p10_0 = config.p01_base, config.p10_base
        p01_1 = _expit(base01 + config.alpha01)
        p10_1 = _expit(base10 + config.alpha10)
        mu0 = _mean_q(config.pi0, config.k_slots, p01_0, p10_0)
        mu1 = _mean_q(config.pi0, config.k_slots, p01_1, p10_1)
        theta_access = (config.lambda1 - config.lambda0) * (mu1 - mu0)
        itt_truth = mean(q1 - q0 for q0, q1 in truth_rows)
        manifest = RunManifest(run_id, config.scenario_id, config.scenario_version,
                               config.n_units, config.k_slots, self.version)
        truth = TruthBundle(run_id, tuple(potential), tuple(signatures), theta_access, itt_truth,
                            config.gamma01 != 0.0 or config.gamma10 != 0.0, config.seed)
        return manifest, truth, GeneratedSource(run_id, tuple(observed_rows))


class Projector:
    """Allow-list projection from generated source to the Analyzer-visible schema."""
    ALLOWED = ("unit_id", "assignment_z", "q_b1_observed", "observation_status")

    def project(self, source: GeneratedSource) -> EvidenceCandidate:
        rows = []
        for row in source.rows:
            if set(row) != set(self.ALLOWED):
                raise FirewallError("generated row contains missing or reserved fields")
            rows.append({key: row[key] for key in self.ALLOWED})
        return EvidenceCandidate(source.run_id, tuple(rows))


class Sealer:
    version = "c10s-sealer-0.1"

    def seal(self, candidate: EvidenceCandidate) -> SealedEvidence:
        if not candidate.rows:
            raise ContractError("cannot seal empty evidence")
        for row in candidate.rows:
            if set(row) != set(Projector.ALLOWED):
                raise FirewallError("evidence schema is not allow-listed")
            if row["observation_status"] != "OBSERVED":
                raise ContractError("this focal implementation requires explicitly observed Q_B1")
            if row["assignment_z"] not in (0, 1) or not 0.0 <= row["q_b1_observed"] <= 1.0:
                raise ContractError("invalid assignment or Q_B1 value")
        manifest = {"run_id": candidate.run_id, "schema": "C10S-OBSERVED-EVIDENCE-001",
                    "sealer_version": self.version, "row_count": len(candidate.rows)}
        digest = _canonical_hash({"manifest": manifest, "rows": candidate.rows})
        return SealedEvidence(candidate.run_id, candidate.rows, manifest, digest)


class Analyzer:
    version = "c10s-focal-analyzer-0.1"

    def analyze(self, evidence: SealedEvidence, contract: AnalysisContract) -> AnalyzerResult:
        contract.validate()
        expected = _canonical_hash({"manifest": evidence.manifest, "rows": evidence.rows})
        if expected != evidence.sha256:
            raise FirewallError("sealed evidence hash mismatch")
        if any(set(row) != set(Projector.ALLOWED) for row in evidence.rows):
            raise FirewallError("Analyzer received a non-conforming evidence schema")
        arm0 = [r["q_b1_observed"] for r in evidence.rows if r["assignment_z"] == 0]
        arm1 = [r["q_b1_observed"] for r in evidence.rows if r["assignment_z"] == 1]
        if not contract.randomized_assignment or len(arm0) < 2 or len(arm1) < 2:
            return self._abstain(evidence, contract, "RANDOMIZATION_OR_ARM_SUPPORT_NOT_ESTABLISHED")
        estimate = mean(arm1) - mean(arm0)
        var0 = variance(arm0) / len(arm0)
        var1 = variance(arm1) / len(arm1)
        se = math.sqrt(var0 + var1)
        denominator = (var0 * var0 / (len(arm0) - 1)
                       + var1 * var1 / (len(arm1) - 1))
        if se == 0.0:
            degrees_freedom = math.inf
            critical = 1.959963984540054
        else:
            degrees_freedom = ((var0 + var1) ** 2 / denominator
                               if denominator > 0.0 else math.inf)
            critical = (1.959963984540054 if math.isinf(degrees_freedom)
                        else _student_t_critical_975(degrees_freedom))
        interval = (estimate - critical * se, estimate + critical * se)
        package_ok = contract.measurement_ideal and contract.interference_absent
        if not package_ok:
            return self._abstain(evidence, contract, "PACKAGE_ITT_ASSUMPTIONS_OR_MEASUREMENT_NOT_ESTABLISHED")
        package_status: Identification = "IDENTIFIED"
        focal_ok = (contract.direct_path_status == "ABSENT" and contract.common_regime
                    and contract.positivity and contract.version_consistency)
        focal_status: Identification = "IDENTIFIED" if focal_ok else (
            "NOT_IDENTIFIED" if contract.direct_path_status == "PRESENT" else "INDETERMINATE")
        reason = None if focal_ok else "FOCAL_ATTRIBUTION_REQUIRES_NO_DIRECT_PATH_AND_COMMON_REGIME"
        focal_estimate = estimate if focal_ok else None
        focal_se = se if focal_ok else None
        focal_interval = interval if focal_ok else None
        result_payload = {"run_id": evidence.run_id, "estimand_id": contract.estimand_id,
                          "estimand_version": contract.estimand_version,
                          "package_identification": package_status, "focal_identification": focal_status,
                          "package_itt_estimate": estimate, "package_itt_standard_error": se,
                          "package_itt_interval_95": interval, "focal_estimate": focal_estimate,
                          "focal_standard_error": focal_se, "focal_interval_95": focal_interval,
                          "abstention_reason": reason, "input_sha256": evidence.sha256}
        return AnalyzerResult(evidence.run_id, contract.estimand_id, contract.estimand_version,
                              package_status, focal_status, estimate, se, interval,
                              focal_estimate, focal_se, focal_interval, reason,
                              evidence.sha256, _canonical_hash(result_payload))

    def _abstain(self, evidence: SealedEvidence, contract: AnalysisContract, reason: str) -> AnalyzerResult:
        payload = {"run_id": evidence.run_id, "estimand_id": contract.estimand_id,
                   "estimand_version": contract.estimand_version,
                   "package_itt_estimate": None, "package_itt_standard_error": None,
                   "package_itt_interval_95": None, "focal_estimate": None,
                   "focal_standard_error": None, "focal_interval_95": None,
                   "package_identification": "INDETERMINATE",
                   "focal_identification": "INDETERMINATE",
                   "abstention_reason": reason, "input_sha256": evidence.sha256}
        return AnalyzerResult(evidence.run_id, contract.estimand_id, contract.estimand_version,
                              "INDETERMINATE", "INDETERMINATE",
                              None, None, None, None, None, None, reason,
                              evidence.sha256, _canonical_hash(payload))


class Evaluator:
    """Truth access begins only here, after AnalyzerResult has been produced and sealed."""
    def evaluate(self, truth: TruthBundle, result: AnalyzerResult,
                 contract: AnalysisContract, tolerance: float) -> EvaluationReport:
        contract.validate()
        if tolerance < 0.0 or result.run_id != truth.run_id:
            raise ContractError("invalid tolerance or mismatched run identity")
        result_payload = {"run_id": result.run_id, "estimand_id": result.estimand_id,
                          "estimand_version": result.estimand_version,
                          "package_identification": result.package_identification,
                          "focal_identification": result.focal_identification,
                          "package_itt_estimate": result.package_itt_estimate,
                          "package_itt_standard_error": result.package_itt_standard_error,
                          "package_itt_interval_95": result.package_itt_interval_95,
                          "focal_estimate": result.focal_estimate,
                          "focal_standard_error": result.focal_standard_error,
                          "focal_interval_95": result.focal_interval_95,
                          "abstention_reason": result.abstention_reason,
                          "input_sha256": result.input_sha256}
        if _canonical_hash(result_payload) != result.output_sha256:
            raise FirewallError("AnalyzerResult seal/hash mismatch")
        package_error = (None if result.package_itt_estimate is None else
                         abs(result.package_itt_estimate - truth.itt_value_truth))
        package_recovery = package_error is not None and package_error <= tolerance
        focal_error = None
        focal_recovery: bool | None = None
        if result.focal_identification == "IDENTIFIED" and result.focal_estimate is not None:
            focal_error = abs(result.focal_estimate - truth.theta_access_truth)
            focal_recovery = focal_error <= tolerance
        package_conditions = (contract.randomized_assignment and contract.measurement_ideal
                              and contract.interference_absent and result.package_itt_estimate is not None)
        expected_package_status = "IDENTIFIED" if package_conditions else "INDETERMINATE"
        if expected_package_status == "INDETERMINATE":
            expected_focal_status = "INDETERMINATE"
        elif contract.direct_path_status == "PRESENT":
            expected_focal_status = "NOT_IDENTIFIED"
        elif (contract.direct_path_status == "UNKNOWN" or not contract.common_regime
              or not contract.positivity or not contract.version_consistency):
            expected_focal_status = "INDETERMINATE"
        else:
            expected_focal_status = "NOT_IDENTIFIED" if truth.direct_path_truth else "IDENTIFIED"
        classification_correct = (
            result.package_identification == expected_package_status
            and result.focal_identification == expected_focal_status
        )
        notes = ("Analyzer input contains observed Q_B1 and randomized assignment only.",
                 "Finite-sample recovery is not a confirmatory result.",
                 "Focal truth is defined under the common direct-path regime gamma=0.")
        return EvaluationReport(truth.run_id, result.output_sha256, package_error, focal_error,
                                package_recovery, focal_recovery, classification_correct, notes)
