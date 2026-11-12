"""Integrated synthetic C10-S harness for V_cont.

This is a parameterized research benchmark, not a real migration model.
Generator creates common-exogenous potential V_cont paths; Projector exposes
only S3 observations and randomized assignments; Analyzer never receives truth;
Evaluator opens truth only after the Analyzer output is sealed.

The randomized G intervention is an explicit synthetic intervention on the
full focal accessibility change (g_A), separate from package assignment Z.
It does NOT claim that D2 assignment identifies g_A.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
import random
from statistics import mean, variance
from typing import Any, Literal

Profile = Literal["R0", "R1", "R2", "R3"]
Identification = Literal["IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"]


class ContractError(ValueError):
    pass


class FirewallError(RuntimeError):
    pass


@dataclass(frozen=True)
class ScenarioConfig:
    scenario_id: str
    version: str
    profile: Profile
    mechanism: str
    n_units: int
    n_intervals: int
    seed: int
    baseline_conformity: float
    focal_access_effect: float
    package_direct_effect: float
    focal_direct_effect: float
    collateral_effect: float
    provision_probability: float
    alternative_probability: float
    heterogeneity: float
    interference_effect: float
    measurement_sensitivity: float
    measurement_specificity: float
    missing_probability: float
    randomized_z: bool
    randomized_g: bool
    positivity: bool
    no_interference: bool
    measurement_identified: bool
    version_consistency: bool

    def validate(self) -> None:
        if not self.scenario_id or not self.version:
            raise ContractError("scenario identity/version required")
        if self.profile not in ("R0", "R1", "R2", "R3"):
            raise ContractError("profile must be R0/R1/R2/R3")
        if self.n_units < 16 or self.n_units % 4:
            raise ContractError("n_units must be >=16 and divisible by four")
        if self.n_intervals < 2:
            raise ContractError("at least two equal V_cont intervals required")
        probs = (
            self.baseline_conformity, self.provision_probability,
            self.alternative_probability, self.measurement_sensitivity,
            self.measurement_specificity, self.missing_probability,
        )
        if any(not 0.0 <= x <= 1.0 for x in probs):
            raise ContractError("probabilities must lie in [0,1]")
        if not all(math.isfinite(x) for x in (
            self.focal_access_effect, self.package_direct_effect,
            self.focal_direct_effect, self.collateral_effect,
            self.heterogeneity, self.interference_effect,
        )):
            raise ContractError("effects must be finite")
        if not self.randomized_z or not self.randomized_g:
            raise ContractError("benchmark requires randomized Z and randomized g_A")
        if not self.version_consistency:
            raise ContractError("scenario generator requires explicit version consistency")
        if self.measurement_identified and not (
            self.measurement_sensitivity == 1.0 and
            self.measurement_specificity == 1.0 and
            self.missing_probability == 0.0
        ):
            raise ContractError("point identification currently requires perfect, complete S3; calibrated-error correction is not implemented")


@dataclass(frozen=True)
class AnalysisContract:
    estimand_id: str
    estimand_version: str
    randomized_z: bool
    randomized_g: bool
    positivity: bool
    no_interference: bool
    measurement_identified: bool
    version_consistency: bool
    focal_direct_path_absent: bool
    common_nonfocal_regime: bool

    def validate(self) -> None:
        if not self.estimand_id or not self.estimand_version:
            raise ContractError("estimand identity/version required")


@dataclass(frozen=True)
class RunManifest:
    run_id: str
    scenario_id: str
    version: str
    n_units: int
    n_intervals: int
    generator_version: str


@dataclass(frozen=True)
class TruthBundle:
    run_id: str
    potential_v: tuple[tuple[tuple[float, float], tuple[float, float]], ...]
    potential_interval_truth: tuple[tuple[tuple[tuple[int, ...], tuple[int, ...]],
                                          tuple[tuple[int, ...], tuple[int, ...]]], ...]
    itt_package_truth: float
    theta_access_truth: float
    seed: int


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
    package_status: Identification
    focal_status: Identification
    package_itt: float | None
    focal_effect: float | None
    package_se: float | None
    focal_se: float | None
    abstention_reasons: tuple[str, ...]
    input_sha256: str
    output_sha256: str


@dataclass(frozen=True)
class EvaluationReport:
    run_id: str
    package_abs_error: float | None
    focal_abs_error: float | None
    package_recovered: bool | None
    focal_recovered: bool | None
    expected_abstention_respected: bool
    notes: tuple[str, ...]


def _hash(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _balanced_binary(n: int, rng: random.Random) -> list[int]:
    values = [0] * (n // 2) + [1] * (n // 2)
    rng.shuffle(values)
    return values


def _mean_se(a: list[float], b: list[float]) -> tuple[float, float]:
    if len(a) < 2 or len(b) < 2:
        raise ContractError("both randomized arms need at least two units")
    estimate = mean(b) - mean(a)
    se = math.sqrt(variance(a) / len(a) + variance(b) / len(b))
    return estimate, se


class Generator:
    version = "c10s-vcont-generator-0.1"

    def generate(self, cfg: ScenarioConfig) -> tuple[RunManifest, TruthBundle, EvidenceCandidate]:
        cfg.validate()
        rng = random.Random(cfg.seed)
        run_id = _hash(asdict(cfg))[:24]
        if not cfg.no_interference:
            n_clusters = cfg.n_units // 4
            if n_clusters % 2:
                raise ContractError("cluster-interference benchmark requires an even number of four-unit clusters")
            cluster_z_assign = _balanced_binary(n_clusters, rng)
            z_assign = [cluster_z_assign[i // 4] for i in range(cfg.n_units)]
        else:
            z_assign = _balanced_binary(cfg.n_units, rng)
        g_assign = _balanced_binary(cfg.n_units, rng)
        # Shared exogenous variables: same unit/interval uniforms are reused
        # across all four potential regimes (z,g).
        rows: list[dict[str, Any]] = []
        v_truth = []
        interval_truth = []
        potential_package_by_g: list[list[float]] = [[], []]
        potential_focal_by_z: list[list[float]] = [[], []]

        for i in range(cfg.n_units):
            x = rng.random()
            u_access = rng.random()
            u_provision = rng.random()
            u_alt = rng.random()
            u_trajectory = rng.random()
            u_enabled = [rng.random() for _ in range(cfg.n_intervals)]
            u_profile = [rng.random() for _ in range(cfg.n_intervals)]
            cluster = i // 4
            # Synthetic exposure is based on the other units' assigned Z in
            # the same four-unit cluster; it is inert in no-interference worlds.
            unit_potentials = []
            unit_intervals = []
            unit_enabled = []
            unit_profile = []
            for z in (0, 1):
                z_potentials = []
                z_intervals = []
                z_enabled = []
                z_profile = []
                for g in (0, 1):
                    provision_p = cfg.provision_probability
                    if cfg.profile == "R3":
                        provision_p = max(0.0, min(1.0, provision_p - 0.20 * z))
                    provision_ok = int(u_provision < provision_p)
                    focal_access = int(g == 1 and provision_ok and u_access < 0.95)
                    if cfg.profile == "R1":
                        alternative = 1
                    elif cfg.profile == "R2":
                        alternative = int(u_alt < max(0.0, min(1.0,
                            cfg.alternative_probability - 0.20 * z)))
                    else:
                        alternative = int(u_alt < cfg.alternative_probability)
                    reach = int(bool(focal_access or alternative))
                    trajectory = int(reach and u_trajectory < 0.95)
                    profile_match_p = (
                        cfg.baseline_conformity
                        + cfg.focal_access_effect * trajectory
                        + cfg.package_direct_effect * z
                        + cfg.focal_direct_effect * g
                        + cfg.collateral_effect * (z * alternative)
                        + cfg.heterogeneity * (x - 0.5) * trajectory
                    )
                    if not cfg.no_interference:
                        # Cluster-level assignment makes the exposure counterfactual coherent.
                        profile_match_p += cfg.interference_effect * z
                    profile_match_p = max(0.0, min(1.0, profile_match_p))
                    # B1 is conjunctive: ENABLED and the declared PROFILE must
                    # both hold throughout an interval. Components stay separate.
                    enabled_states = tuple(int(u < 0.98) for u in u_enabled)
                    profile_states = tuple(int(u < profile_match_p) for u in u_profile)
                    states = tuple(int(en and pr) for en, pr in zip(enabled_states, profile_states))
                    v = sum(states) / cfg.n_intervals
                    z_potentials.append(v)
                    z_intervals.append(states)
                    z_enabled.append(enabled_states)
                    z_profile.append(profile_states)
                    potential_package_by_g[g].append(v)
                    potential_focal_by_z[z].append(v)
                unit_potentials.append(tuple(z_potentials))
                unit_intervals.append(tuple(z_intervals))
                unit_enabled.append(tuple(z_enabled))
                unit_profile.append(tuple(z_profile))
            v_truth.append(tuple(unit_potentials))
            interval_truth.append(tuple(unit_intervals))

            z, g = z_assign[i], g_assign[i]
            true_enabled = unit_enabled[z][g]
            true_profile = unit_profile[z][g]
            observed_enabled, observed_profile = [], []
            status_enabled, status_profile = [], []
            for en_state, pr_state in zip(true_enabled, true_profile):
                if rng.random() < cfg.missing_probability:
                    observed_enabled.append(None)
                    status_enabled.append("MISSING")
                else:
                    flip = rng.random()
                    observed_enabled.append(int(flip < cfg.measurement_sensitivity) if en_state
                                            else int(flip >= cfg.measurement_specificity))
                    status_enabled.append("OBSERVED")
                if rng.random() < cfg.missing_probability:
                    observed_profile.append(None)
                    status_profile.append("MISSING")
                else:
                    flip = rng.random()
                    observed_profile.append(int(flip < cfg.measurement_sensitivity) if pr_state
                                             else int(flip >= cfg.measurement_specificity))
                    status_profile.append("OBSERVED")
            rows.append({
                "unit_id": f"UE-{i + 1:06d}",
                "cluster_id": f"CL-{cluster:05d}",
                "assignment_z": z,
                "assignment_g": g,
                "s3_enabled": observed_enabled,
                "s3_profile_match": observed_profile,
                "s3_enabled_status": status_enabled,
                "s3_profile_status": status_profile,
                "profile": cfg.profile,
                "version": cfg.version,
            })

        # Potential arrays are indexed [unit][z][g].
        itt = mean(
            (unit[1][0] + unit[1][1]) / 2 - (unit[0][0] + unit[0][1]) / 2
            for unit in v_truth
        )
        theta = mean(unit[0][1] - unit[0][0] for unit in v_truth)
        manifest = RunManifest(run_id, cfg.scenario_id, cfg.version,
                               cfg.n_units, cfg.n_intervals, self.version)
        truth = TruthBundle(run_id, tuple(v_truth), tuple(interval_truth), itt, theta, cfg.seed)
        return manifest, truth, EvidenceCandidate(run_id, tuple(rows))


class Sealer:
    def seal(self, candidate: EvidenceCandidate) -> SealedEvidence:
        if not candidate.rows:
            raise ContractError("empty evidence")
        allowed = {"unit_id", "cluster_id", "assignment_z", "assignment_g",
                   "s3_enabled", "s3_profile_match", "s3_enabled_status",
                   "s3_profile_status", "profile", "version"}
        for row in candidate.rows:
            if set(row) != allowed:
                raise FirewallError("reserved/missing evidence fields")
            lengths = {len(row[k]) for k in ("s3_enabled", "s3_profile_match",
                       "s3_enabled_status", "s3_profile_status")}
            if len(lengths) != 1:
                raise ContractError("S3 interval/status cardinality mismatch")
            if any(v not in (0, 1, None) for k in ("s3_enabled", "s3_profile_match")
                   for v in row[k]):
                raise ContractError("invalid S3 value")
        manifest = {"run_id": candidate.run_id, "schema": "C10S-VCONT-S3-001",
                    "row_count": len(candidate.rows), "sealer_version": "0.1"}
        digest = _hash({"manifest": manifest, "rows": candidate.rows})
        return SealedEvidence(candidate.run_id, candidate.rows, manifest, digest)


class Analyzer:
    version = "c10s-vcont-analyzer-0.1"

    def analyze(self, evidence: SealedEvidence, contract: AnalysisContract) -> AnalyzerResult:
        contract.validate()
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise FirewallError("sealed evidence integrity failure")
        package_reasons = []
        focal_reasons = []
        if not contract.randomized_z:
            package_reasons.append("PACKAGE_RANDOMIZATION_NOT_ESTABLISHED")
        if not contract.randomized_g:
            focal_reasons.append("FOCAL_RANDOMIZATION_NOT_ESTABLISHED")
        if not contract.positivity:
            focal_reasons.append("COMMON_SUPPORT_FAILURE")
        if not contract.no_interference:
            package_reasons.append("INTERFERENCE_REQUIRES_CLUSTER_EXPOSURE_ESTIMAND")
            focal_reasons.append("INTERFERENCE_REQUIRES_CLUSTER_EXPOSURE_ESTIMAND")
        if not contract.measurement_identified:
            package_reasons.append("S3_MEASUREMENT_NOT_IDENTIFIED")
            focal_reasons.append("S3_MEASUREMENT_NOT_IDENTIFIED")
        if not contract.version_consistency:
            package_reasons.append("VERSION_INCONSISTENCY")
            focal_reasons.append("VERSION_INCONSISTENCY")
        complete = all(all(v in (0, 1) for v in row["s3_interval"]) for row in evidence.rows)
        if not complete:
            package_reasons.append("S3_MISSINGNESS_REQUIRES_BOUNDS_OR_MODEL")
            focal_reasons.append("S3_MISSINGNESS_REQUIRES_BOUNDS_OR_MODEL")
        ideal = all(all(s == "OBSERVED" for s in row["s3_status"]) for row in evidence.rows)
        if not ideal:
            package_reasons.append("S3_COVERAGE_INCOMPLETE")
            focal_reasons.append("S3_COVERAGE_INCOMPLETE")

        observed_v = None
        if not package_reasons:
            observed_v = [mean(row["s3_interval"]) for row in evidence.rows]
            z0 = [observed_v[i] for i, row in enumerate(evidence.rows) if row["assignment_z"] == 0]
            z1 = [observed_v[i] for i, row in enumerate(evidence.rows) if row["assignment_z"] == 1]
            package, package_se = _mean_se(z0, z1)
            package_status: Identification = "IDENTIFIED"
        else:
            package, package_se = None, None
            package_status = "INDETERMINATE"

        if not contract.focal_direct_path_absent or not contract.common_nonfocal_regime:
            focal_reasons.append("FOCAL_EXCLUSION_OR_COMMON_REGIME_NOT_ESTABLISHED")
        if not focal_reasons and observed_v is not None:
            focal_rows = [(observed_v[i], row) for i, row in enumerate(evidence.rows)
                          if row["assignment_z"] == 0]
            g0 = [v for v, row in focal_rows if row["assignment_g"] == 0]
            g1 = [v for v, row in focal_rows if row["assignment_g"] == 1]
            focal, focal_se = _mean_se(g0, g1)
            focal_status: Identification = "IDENTIFIED"
        else:
            focal, focal_se = None, None
            focal_status = "NOT_IDENTIFIED" if (
                "FOCAL_EXCLUSION_OR_COMMON_REGIME_NOT_ESTABLISHED" in focal_reasons or
                "COMMON_SUPPORT_FAILURE" in focal_reasons or
                "FOCAL_RANDOMIZATION_NOT_ESTABLISHED" in focal_reasons
            ) else "INDETERMINATE"

        reasons = tuple(dict.fromkeys(package_reasons + focal_reasons))
        payload = {"run_id": evidence.run_id, "estimand_id": contract.estimand_id,
                   "package_status": package_status, "focal_status": focal_status,
                   "package_itt": package, "focal_effect": focal,
                   "package_se": package_se, "focal_se": focal_se,
                   "reasons": list(reasons), "input_sha256": evidence.sha256}
        return AnalyzerResult(evidence.run_id, contract.estimand_id,
            package_status, focal_status, package, focal, package_se, focal_se,
            reasons, evidence.sha256, _hash(payload))


class Evaluator:
    def evaluate(self, truth: TruthBundle, result: AnalyzerResult,
                 contract: AnalysisContract, tolerance: float) -> EvaluationReport:
        if tolerance < 0 or truth.run_id != result.run_id:
            raise ContractError("invalid tolerance or run mismatch")
        payload = {
            "run_id": result.run_id, "estimand_id": result.estimand_id,
            "package_status": result.package_status, "focal_status": result.focal_status,
            "package_itt": result.package_itt, "focal_effect": result.focal_effect,
            "package_se": result.package_se, "focal_se": result.focal_se,
            "reasons": list(result.abstention_reasons), "input_sha256": result.input_sha256,
        }
        if _hash(payload) != result.output_sha256:
            raise FirewallError("Analyzer output seal invalid")
        package_error = None if result.package_itt is None else abs(result.package_itt - truth.itt_package_truth)
        focal_error = None if result.focal_effect is None else abs(result.focal_effect - truth.theta_access_truth)
        package_ok = None if package_error is None else package_error <= tolerance
        focal_ok = None if focal_error is None else focal_error <= tolerance
        expected_abstention = (
            (not contract.no_interference or not contract.measurement_identified or
             not contract.version_consistency) and
            result.package_status == "INDETERMINATE"
        ) or (
            (not contract.positivity or not contract.randomized_g or
             not contract.focal_direct_path_absent or not contract.common_nonfocal_regime)
            and result.focal_status in ("NOT_IDENTIFIED", "INDETERMINATE")
        )
        notes = []
        if result.package_status == "IDENTIFIED" and package_ok is False:
            notes.append("PACKAGE_ESTIMATE_OUTSIDE_TOLERANCE")
        if result.focal_status == "IDENTIFIED" and focal_ok is False:
            notes.append("FOCAL_ESTIMATE_OUTSIDE_TOLERANCE")
        return EvaluationReport(truth.run_id, package_error, focal_error,
                                package_ok, focal_ok, expected_abstention, tuple(notes))


def benchmark_scenarios(n_units: int = 400, n_intervals: int = 20,
                        seed: int = 20261112) -> tuple[ScenarioConfig, ...]:
    """Explicit candidate design points; not empirical rates or confirmatory defaults."""
    common = dict(
        version="VCONT-SYNTH-001", n_units=n_units, n_intervals=n_intervals,
        seed=seed, baseline_conformity=0.55, focal_access_effect=0.20,
        package_direct_effect=0.0, focal_direct_effect=0.0, collateral_effect=0.0,
        provision_probability=1.0, alternative_probability=0.0, heterogeneity=0.0,
        interference_effect=0.0, measurement_sensitivity=1.0,
        measurement_specificity=1.0, missing_probability=0.0,
        randomized_z=True, randomized_g=True, positivity=True, no_interference=True,
        measurement_identified=True, version_consistency=True,
    )
    specs = [
        ("R0_FOCAL_POSITIVE", "R0", "FOCAL_POSITIVE", {}),
        ("R0_FOCAL_NULL", "R0", "FOCAL_NULL", {"focal_access_effect": 0.0}),
        ("R0_FOCAL_ADVERSE", "R0", "FOCAL_ADVERSE", {"focal_access_effect": -0.20}),
        ("R0_DIRECT_G", "R0", "DIRECT_FOCAL_PATH", {"focal_direct_effect": 0.15}),
        ("R0_DIRECT_Z", "R0", "DIRECT_PACKAGE_PATH", {"package_direct_effect": 0.15}),
        ("R1_ALTERNATIVE_BASELINE", "R1", "ALTERNATIVE_BASELINE", {}),
        ("R2_ALTERNATIVE_AFFECTED", "R2", "ALTERNATIVE_COLLATERAL", {
            "alternative_probability": 0.65, "collateral_effect": 0.15}),
        ("R3_PROVISION_FAILURE", "R3", "PROVISION_STAGE_FAILURE", {
            "provision_probability": 0.75}),
        ("R0_MEASUREMENT_ADVERSE", "R0", "S3_ERROR_MISSINGNESS", {
            "measurement_sensitivity": 0.85, "measurement_specificity": 0.90,
            "missing_probability": 0.10, "measurement_identified": False}),
        ("R0_INTERFERENCE", "R0", "CLUSTER_INTERFERENCE", {
            "interference_effect": 0.15, "no_interference": False}),
        ("R0_SUPPORT_FAILURE", "R0", "POSITIVITY_FAILURE", {"positivity": False}),
        ("R0_HETEROGENEITY", "R0", "EFFECT_HETEROGENEITY", {"heterogeneity": 0.20}),
    ]
    result = []
    for sid, profile, mechanism, overrides in specs:
        values = dict(common)
        values.update(overrides)
        result.append(ScenarioConfig(scenario_id=sid, profile=profile, mechanism=mechanism,
                                     **values))
    return tuple(result)


def contract_for(cfg: ScenarioConfig) -> AnalysisContract:
    return AnalysisContract(
        estimand_id="ITT_D2_AND_THETA_A_VCONT",
        estimand_version="001",
        randomized_z=cfg.randomized_z,
        randomized_g=cfg.randomized_g,
        positivity=cfg.positivity,
        no_interference=cfg.no_interference,
        measurement_identified=cfg.measurement_identified,
        version_consistency=cfg.version_consistency,
        focal_direct_path_absent=(cfg.focal_direct_effect == 0.0),
        common_nonfocal_regime=True,
    )
