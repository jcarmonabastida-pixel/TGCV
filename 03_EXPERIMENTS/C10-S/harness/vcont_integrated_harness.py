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
    window_start: float
    last_transition_support: float
    follow_up: float
    enabled_probability: float
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
    zg_interaction_effect: float = 0.0
    world_seed: int | None = None
    z_assignment_seed: int | None = None
    g_assignment_seed: int | None = None
    replicate_id: str = "replicate-000"

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
            self.enabled_probability, self.baseline_conformity, self.provision_probability,
            self.alternative_probability, self.measurement_sensitivity,
            self.measurement_specificity, self.missing_probability,
        )
        if any(not 0.0 <= x <= 1.0 for x in probs):
            raise ContractError("probabilities must lie in [0,1]")
        if not all(math.isfinite(x) for x in (
            self.focal_access_effect, self.package_direct_effect,
            self.focal_direct_effect, self.collateral_effect,
            self.heterogeneity, self.interference_effect, self.zg_interaction_effect,
        )):
            raise ContractError("effects must be finite")
        if not self.randomized_z or not self.randomized_g:
            raise ContractError("benchmark requires randomized Z and randomized g_A")
        if not self.version_consistency:
            raise ContractError("scenario generator requires explicit version consistency")
        if not (math.isfinite(self.window_start) and
                math.isfinite(self.last_transition_support) and
                math.isfinite(self.follow_up) and
                self.window_start < self.last_transition_support and self.follow_up > 0.0):
            raise ContractError("temporal support and positive follow-up must be explicit")
        total_width = (self.last_transition_support + self.follow_up - self.window_start) / self.n_intervals
        transition_slots = (self.last_transition_support - self.window_start) / total_width
        if abs(transition_slots - round(transition_slots)) > 1e-9 or round(transition_slots) >= self.n_intervals:
            raise ContractError("transition support must end on an interval boundary before follow-up")
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
    target_regime_id: str = "G_REFERENCE_50_50"
    target_regime_version: str = "001"
    outcome_id: str = "V_CONT"
    outcome_version: str = "001"
    z_effect_invariant_across_g: bool = False
    transportability_id: str | None = None
    transportability_version: str | None = None
    transportability_scope: str | None = None
    transportability_evidence_status: str = "NOT_ESTABLISHED"
    g_assignment_mechanism_hash: str = ""
    z_assignment_mechanism_hash: str = ""
    g_assignment_mechanism_id: str = "G_BALANCED"
    g_assignment_mechanism_version: str = "001"
    z_assignment_mechanism_id: str = "Z_BALANCED_INDEPENDENT"
    z_assignment_mechanism_version: str = "001"
    reference_regime_id: str = "G_REFERENCE_50_50"
    reference_regime_version: str = "001"
    transportability_outcome_id: str | None = None
    transportability_basis: str | None = None

    def validate(self) -> None:
        if not self.estimand_id or not self.estimand_version or not self.target_regime_id or not self.target_regime_version:
            raise ContractError("estimand and target-regime identity/version required")
        if self.z_effect_invariant_across_g and not (self.transportability_id and self.transportability_version and self.transportability_scope and self.transportability_evidence_status == "STRUCTURALLY_VERIFIED" and self.transportability_outcome_id == self.outcome_id and self.transportability_basis):
            raise ContractError("transportability declaration requires ID, version, scope, matching outcome, basis and structural verification")
        if not all((self.g_assignment_mechanism_id, self.g_assignment_mechanism_version, self.z_assignment_mechanism_id, self.z_assignment_mechanism_version, self.reference_regime_id, self.reference_regime_version)):
            raise ContractError("assignment mechanism and reference regime identities/versions required")


@dataclass(frozen=True)
class RunManifest:
    run_id: str
    scenario_id: str
    version: str
    n_units: int
    n_intervals: int
    window_start: float
    window_end: float
    interval_width: float
    generator_version: str
    world_id: str = "world-legacy"
    world_version: str = "001"
    replicate_id: str = "replicate-000"
    g_assignment_mechanism_id: str = "G_BALANCED"
    g_assignment_mechanism_version: str = "001"
    g_assignment_mechanism_hash: str = ""
    z_assignment_mechanism_id: str = "Z_BALANCED"
    z_assignment_mechanism_version: str = "001"
    z_assignment_mechanism_hash: str = ""
    g_reference_regime_id: str = "G_REFERENCE_50_50"
    g_reference_regime_version: str = "001"
    z_assignment_vector_hash: str = ""
    g_assignment_vector_hash: str = ""
    g_assignment_probability_by_stratum: tuple[tuple[str, float], ...] = ()
    world_seed: int = 0
    z_assignment_seed: int = 0
    g_assignment_seed: int = 0


@dataclass(frozen=True)
class TruthBundle:
    run_id: str
    potential_v: tuple[tuple[tuple[float, float], tuple[float, float]], ...]
    potential_interval_truth: tuple[Any, ...]
    potential_enabled_truth: tuple[Any, ...]
    potential_profile_truth: tuple[Any, ...]
    potential_delta_t_acc: tuple[Any, ...]
    # Truths are kept distinct: Z package ITT, G assignment contrast, and
    # focal accessibility intervention truth. theta_a_truth remains absent
    # until the approved joint g_A policies and q_X* are materialized.
    itt_z_truth: float
    itt_g_z0_truth: float
    theta_a_truth: float | None
    seed: int
    itt_z_run_truth: float | None = None
    itt_z_mechanism_truth: float | None = None
    itt_z_reference_truth: float | None = None
    transportability_invariant_truth: bool | None = None
    transportability_scope_truth: str | None = None
    g_reference_regime_id: str = "G_REFERENCE_50_50"
    g_reference_regime_version: str = "001"
    g_assignment_mechanism_hash: str = ""
    z_assignment_mechanism_hash: str = ""

    @property
    def itt_package_truth(self) -> float:
        """Explicit legacy alias for the unchanged ITT-Z target."""
        return self.itt_z_truth


@dataclass(frozen=True)
class EvidenceCandidate:
    run_id: str
    rows: tuple[dict[str, Any], ...]
    provenance: dict[str, Any] | None = None


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
    g_assignment_status: Identification
    package_itt: float | None
    g_assignment_effect: float | None
    first_stage_delta_t_acc: tuple[float, float, float, float] | None
    package_se: float | None
    g_assignment_se: float | None
    abstention_reasons: tuple[str, ...]
    input_sha256: str
    output_sha256: str
    target_regime_id: str = "G_REFERENCE_50_50"
    target_regime_version: str = "001"
    outcome_id: str = "V_CONT"
    outcome_version: str = "001"
    reference_regime_status: Identification = "INDETERMINATE"
    reference_regime_id: str = "G_REFERENCE_50_50"
    reference_regime_version: str = "001"
    g_assignment_mechanism_hash: str = ""
    z_assignment_mechanism_hash: str = ""
    transportability_id: str | None = None
    transportability_version: str | None = None
    transportability_scope: str | None = None
    transportability_evidence_status: str = "NOT_ESTABLISHED"
    estimand_version: str = "002"
    g_assignment_mechanism_id: str = "G_BALANCED"
    g_assignment_mechanism_version: str = "001"
    z_assignment_mechanism_id: str = "Z_BALANCED_INDEPENDENT"
    z_assignment_mechanism_version: str = "001"
    provenance_sha256: str = ""


@dataclass(frozen=True)
class EvaluationReport:
    run_id: str
    package_abs_error: float | None
    g_assignment_abs_error: float | None
    package_recovered: bool | None
    g_assignment_recovered: bool | None
    expected_abstention_respected: bool
    notes: tuple[str, ...]
    reference_regime_status_correct: bool = False


@dataclass(frozen=True)
class RepeatedAssignmentReport:
    world_id: str
    replicate_count: int
    mean_run_estimate: float | None
    mechanism_truth: float
    marginal_abs_error: float | None
    marginal_recovered: bool | None
    per_run_reports: tuple[EvaluationReport, ...]


def _hash(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _balanced_binary(n: int, rng: random.Random) -> list[int]:
    values = [0] * (n // 2) + [1] * (n // 2)
    rng.shuffle(values)
    return values


def _mean_se(a: list[float], b: list[float]) -> tuple[float | None, float | None]:
    if len(a) < 2 or len(b) < 2:
        return None, None
    estimate = mean(b) - mean(a)
    se = math.sqrt(variance(a) / len(a) + variance(b) / len(b))
    return estimate, se


class Generator:
    version = "c10s-vcont-generator-0.1"

    def generate(self, cfg: ScenarioConfig) -> tuple[RunManifest, TruthBundle, EvidenceCandidate]:
        cfg.validate()
        world_seed = cfg.seed if cfg.world_seed is None else cfg.world_seed
        z_seed = cfg.seed + 100003 if cfg.z_assignment_seed is None else cfg.z_assignment_seed
        g_seed = cfg.seed + 200003 if cfg.g_assignment_seed is None else cfg.g_assignment_seed
        world_rng = random.Random(world_seed)
        z_rng = random.Random(z_seed)
        g_rng = random.Random(g_seed)
        world_spec = asdict(cfg)
        for key in ("seed", "world_seed", "z_assignment_seed", "g_assignment_seed", "replicate_id"):
            world_spec.pop(key, None)
        world_id = _hash({"world_seed": world_seed, "world_spec": world_spec})
        run_id = _hash({"config": asdict(cfg), "replicate_id": cfg.replicate_id, "world_id": world_id, "z_seed": z_seed, "g_seed": g_seed})[:24]
        z_assign = _balanced_binary(cfg.n_units, z_rng)
        g_assign = _balanced_binary(cfg.n_units, g_rng)
        baseline_x = [world_rng.random() for _ in range(cfg.n_units)]
        if not cfg.positivity:
            # Deliberate structural positivity failure: G=1 is unavailable in
            # the high-baseline stratum, not merely flagged in metadata.
            g_assign = [0 if baseline_x[i] >= 0.5 else g_assign[i]
                        for i in range(cfg.n_units)]
        # Shared exogenous variables: same unit/interval uniforms are reused
        # across all four potential regimes (z,g).
        rows: list[dict[str, Any]] = []
        v_truth = []
        interval_truth = []
        enabled_truth = []
        profile_truth = []
        delta_truth = []

        for i in range(cfg.n_units):
            x = baseline_x[i]
            u_access = world_rng.random()
            u_relation = world_rng.random()
            u_context = world_rng.random()
            u_mapping = world_rng.random()
            u_provision = world_rng.random()
            u_alt = world_rng.random()
            u_trajectory = world_rng.random()
            u_enabled = [world_rng.random() for _ in range(cfg.n_intervals)]
            u_profile = [world_rng.random() for _ in range(cfg.n_intervals)]
            cluster = i // 4
            # Synthetic exposure is based on the other units' assigned Z in
            # the same four-unit cluster; it is inert in no-interference worlds.
            unit_potentials = []
            unit_intervals = []
            unit_enabled = []
            unit_profile = []
            unit_delta = []
            for z in (0, 1):
                z_potentials = []
                z_intervals = []
                z_enabled = []
                z_profile = []
                z_delta = []
                for g in (0, 1):
                    provision_p = cfg.provision_probability
                    if cfg.profile == "R3":
                        provision_p = max(0.0, min(1.0, provision_p - 0.20 * z))
                    provision_ok = int(u_provision < provision_p)
                    delta_vector = (
                        int(g == 1 and provision_ok and u_access < 0.95),
                        int(g == 1 and provision_ok and u_relation < 0.95),
                        int(g == 1 and provision_ok and u_context < 0.95),
                        int(g == 1 and provision_ok and u_mapping < 0.95),
                    )
                    focal_access = int(all(delta_vector))
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
                        + cfg.zg_interaction_effect * z * g
                    )
                    if not cfg.no_interference:
                        # Partial-interference potential: hold the realized assignments
                        # of the other three cluster members fixed while intervening on i.
                        peers = [j for j in range(cluster * 4, cluster * 4 + 4) if j != i]
                        peer_exposure = mean(z_assign[j] for j in peers)
                        profile_match_p += cfg.interference_effect * peer_exposure
                    profile_match_p = max(0.0, min(1.0, profile_match_p))
                    # B1 is conjunctive: ENABLED and the declared PROFILE must
                    # both hold throughout an interval. Components stay separate.
                    enabled_raw = [int(u < cfg.enabled_probability) for u in u_enabled]
                    profile_raw = [int(u < profile_match_p) for u in u_profile]
                    transition_slots = int(round(
                        (cfg.last_transition_support - cfg.window_start) /
                        ((cfg.last_transition_support + cfg.follow_up - cfg.window_start) / cfg.n_intervals)
                    ))
                    for slot in range(transition_slots, cfg.n_intervals):
                        enabled_raw[slot] = enabled_raw[transition_slots - 1]
                        profile_raw[slot] = profile_raw[transition_slots - 1]
                    enabled_states = tuple(enabled_raw)
                    profile_states = tuple(profile_raw)
                    states = tuple(int(en and pr) for en, pr in zip(enabled_states, profile_states))
                    v = sum(states) / cfg.n_intervals
                    z_potentials.append(v)
                    z_intervals.append(states)
                    z_enabled.append(enabled_states)
                    z_profile.append(profile_states)
                    z_delta.append(delta_vector)
                unit_potentials.append(tuple(z_potentials))
                unit_intervals.append(tuple(z_intervals))
                unit_enabled.append(tuple(z_enabled))
                unit_profile.append(tuple(z_profile))
                unit_delta.append(tuple(z_delta))
            v_truth.append(tuple(unit_potentials))
            interval_truth.append(tuple(unit_intervals))
            enabled_truth.append(tuple(unit_enabled))
            profile_truth.append(tuple(unit_profile))
            delta_truth.append(tuple(unit_delta))

            z, g = z_assign[i], g_assign[i]
            true_enabled = unit_enabled[z][g]
            true_profile = unit_profile[z][g]
            observed_enabled, observed_profile = [], []
            status_enabled, status_profile = [], []
            for en_state, pr_state in zip(true_enabled, true_profile):
                if world_rng.random() < cfg.missing_probability:
                    observed_enabled.append(None)
                    status_enabled.append("MISSING")
                else:
                    flip = world_rng.random()
                    observed_enabled.append(int(flip < cfg.measurement_sensitivity) if en_state
                                            else int(flip >= cfg.measurement_specificity))
                    status_enabled.append("OBSERVED")
                if world_rng.random() < cfg.missing_probability:
                    observed_profile.append(None)
                    status_profile.append("MISSING")
                else:
                    flip = world_rng.random()
                    observed_profile.append(int(flip < cfg.measurement_sensitivity) if pr_state
                                             else int(flip >= cfg.measurement_specificity))
                    status_profile.append("OBSERVED")
            rows.append({
                "unit_id": f"UE-{i + 1:06d}",
                "cluster_id": f"CL-{cluster:05d}",
                "assignment_z": z,
                "assignment_g": g,
                "baseline_stratum": "HIGH" if x >= 0.5 else "LOW",
                "s3_enabled": observed_enabled,
                "s3_profile_match": observed_profile,
                "s3_enabled_status": status_enabled,
                "s3_profile_status": status_profile,
                "delta_t_acc_observed": unit_delta[z][g],
                "profile": cfg.profile,
                "version": cfg.version,
            })

        # Potential arrays are indexed [unit][z][g].
        itt_reference = mean((unit[1][0] + unit[1][1]) / 2 - (unit[0][0] + unit[0][1]) / 2 for unit in v_truth)
        itt_run = mean(unit[1][g_assign[i]] - unit[0][g_assign[i]] for i, unit in enumerate(v_truth))
        qrun = [0.5 if cfg.positivity or baseline_x[i] < 0.5 else 0.0 for i in range(cfg.n_units)]
        itt_mechanism = mean((1-qrun[i]) * (unit[1][0]-unit[0][0]) + qrun[i] * (unit[1][1]-unit[0][1]) for i, unit in enumerate(v_truth))
        itt_g_z0 = mean(unit[0][1] - unit[0][0] for unit in v_truth)
        unsupported_high = [i for i, x in enumerate(baseline_x) if not cfg.positivity and x >= 0.5]
        invariant_truth = all(abs((v_truth[i][1][1]-v_truth[i][0][1]) - (v_truth[i][1][0]-v_truth[i][0][0])) < 1e-12 for i in unsupported_high) if unsupported_high else True
        window_end = cfg.last_transition_support + cfg.follow_up
        interval_width = (window_end - cfg.window_start) / cfg.n_intervals
        gh = _hash({"algorithm": "balanced_binary_then_zero_HIGH_if_support_failure", "positivity": cfg.positivity, "n": cfg.n_units})
        zh = _hash({"algorithm": "balanced_binary_complete_randomization", "n": cfg.n_units})
        manifest = RunManifest(run_id, cfg.scenario_id, cfg.version, cfg.n_units, cfg.n_intervals,
            cfg.window_start, window_end, interval_width, self.version,
            world_id, cfg.version, cfg.replicate_id,
            "G_BALANCED_WITH_STRATUM_SUPPORT" if not cfg.positivity else "G_BALANCED", "001", gh,
            "Z_BALANCED_INDEPENDENT", "001", zh, "G_REFERENCE_50_50", "001",
            _hash(z_assign), _hash(g_assign), (("LOW", 0.5), ("HIGH", 0.0 if not cfg.positivity else 0.5)),
            world_seed, z_seed, g_seed)
        truth = TruthBundle(run_id, tuple(v_truth), tuple(interval_truth), tuple(enabled_truth), tuple(profile_truth), tuple(delta_truth),
            itt_reference, itt_g_z0, None, cfg.seed, itt_run, itt_mechanism, itt_reference, invariant_truth,
            "HIGH" if unsupported_high else "ALL", "G_REFERENCE_50_50", "001", gh, zh)
        provenance = {"run_id": run_id, "scenario_id": cfg.scenario_id, "scenario_version": cfg.version,
            "world_id": world_id, "world_version": cfg.version, "replicate_id": cfg.replicate_id,
            "g_assignment_mechanism_id": manifest.g_assignment_mechanism_id,
            "g_assignment_mechanism_version": manifest.g_assignment_mechanism_version,
            "g_assignment_mechanism_hash": gh,
            "z_assignment_mechanism_id": manifest.z_assignment_mechanism_id,
            "z_assignment_mechanism_version": manifest.z_assignment_mechanism_version,
            "z_assignment_mechanism_hash": zh,
            "g_reference_regime_id": manifest.g_reference_regime_id,
            "g_reference_regime_version": manifest.g_reference_regime_version,
            "z_assignment_vector_hash": manifest.z_assignment_vector_hash,
            "g_assignment_vector_hash": manifest.g_assignment_vector_hash}
        return manifest, truth, EvidenceCandidate(run_id, tuple(rows), provenance)


class Sealer:
    def seal(self, candidate: EvidenceCandidate) -> SealedEvidence:
        if not candidate.rows:
            raise ContractError("empty evidence")
        allowed = {"unit_id", "cluster_id", "assignment_z", "assignment_g",
                   "baseline_stratum", "s3_enabled", "s3_profile_match", "s3_enabled_status",
                   "s3_profile_status", "delta_t_acc_observed", "profile", "version"}
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
            if len(row["delta_t_acc_observed"]) != 4 or any(v not in (0, 1) for v in row["delta_t_acc_observed"]):
                raise ContractError("Delta T_acc must contain four binary coordinates")
        if not candidate.provenance or candidate.provenance.get("run_id") != candidate.run_id:
            raise ContractError("observable provenance envelope missing or run mismatch")
        manifest = {"run_id": candidate.run_id, "schema": "C10S-VCONT-S3-001",
                    "row_count": len(candidate.rows), "sealer_version": "0.2",
                    "provenance": candidate.provenance, "provenance_sha256": _hash(candidate.provenance)}
        digest = _hash({"manifest": manifest, "rows": candidate.rows})
        return SealedEvidence(candidate.run_id, candidate.rows, manifest, digest)


class Analyzer:
    version = "c10s-vcont-analyzer-0.1"

    def analyze(self, evidence: SealedEvidence, contract: AnalysisContract) -> AnalyzerResult:
        contract.validate()
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise FirewallError("sealed evidence integrity failure")
        # Keep the two assignment estimands' identification conditions separate.
        # Shared outcome/evidence requirements are common; Z randomization is
        # not a prerequisite for the within-Z=0 randomized G contrast.
        shared_reasons = []
        package_reasons = []
        g_assignment_reasons = []
        if not contract.randomized_z:
            package_reasons.append("PACKAGE_RANDOMIZATION_NOT_ESTABLISHED")
        if not contract.randomized_g:
            g_assignment_reasons.append("G_RANDOMIZATION_NOT_ESTABLISHED")
        reference_regime_status: Identification = "IDENTIFIED"
        if not contract.randomized_z or not contract.randomized_g:
            reference_regime_status = "NOT_IDENTIFIED"
        if not contract.positivity:
            g_assignment_reasons.append("COMMON_SUPPORT_FAILURE")
            if not contract.z_effect_invariant_across_g:
                reference_regime_status = "NOT_IDENTIFIED"
            elif contract.transportability_scope != "HIGH":
                reference_regime_status = "INDETERMINATE"
        if not contract.no_interference:
            shared_reasons.append("INTERFERENCE_REQUIRES_CLUSTER_EXPOSURE_ESTIMAND")
        if not contract.measurement_identified:
            shared_reasons.append("S3_MEASUREMENT_NOT_IDENTIFIED")
        if not contract.version_consistency:
            shared_reasons.append("VERSION_INCONSISTENCY")

        complete = all(
            all(v in (0, 1) for k in ("s3_enabled", "s3_profile_match") for v in row[k])
            for row in evidence.rows
        )
        if not complete:
            shared_reasons.append("S3_MISSINGNESS_REQUIRES_BOUNDS_OR_MODEL")
        ideal = all(
            all(s == "OBSERVED" for k in ("s3_enabled_status", "s3_profile_status") for s in row[k])
            for row in evidence.rows
        )
        if not ideal:
            shared_reasons.append("S3_COVERAGE_INCOMPLETE")
        if shared_reasons and reference_regime_status == "IDENTIFIED":
            reference_regime_status = "INDETERMINATE"

        package_reasons.extend(shared_reasons)
        g_assignment_reasons.extend(shared_reasons)
        observed_v = None
        if not shared_reasons:
            # Outcome construction is shared; each estimand is adjudicated
            # independently against its own assignment and support conditions.
            observed_v = [
                mean(int(en and pr) for en, pr in zip(row["s3_enabled"], row["s3_profile_match"]))
                for row in evidence.rows
            ]

        if not package_reasons and observed_v is not None:
            z0 = [observed_v[i] for i, row in enumerate(evidence.rows) if row["assignment_z"] == 0]
            z1 = [observed_v[i] for i, row in enumerate(evidence.rows) if row["assignment_z"] == 1]
            package, package_se = _mean_se(z0, z1)
            package_status: Identification = "IDENTIFIED" if package is not None else "INDETERMINATE"
        else:
            package, package_se = None, None
            package_status = "NOT_IDENTIFIED" if "PACKAGE_RANDOMIZATION_NOT_ESTABLISHED" in package_reasons else "INDETERMINATE"

        first_stage = None
        if observed_v is not None:
            focal_assign_rows = [row for row in evidence.rows if row["assignment_z"] == 0]
            first_stage_values = []
            for coordinate in range(4):
                g0_d = [row["delta_t_acc_observed"][coordinate] for row in focal_assign_rows
                        if row["assignment_g"] == 0]
                g1_d = [row["delta_t_acc_observed"][coordinate] for row in focal_assign_rows
                        if row["assignment_g"] == 1]
                if not g0_d or not g1_d:
                    first_stage_values = []
                    break
                first_stage_values.append(mean(g1_d) - mean(g0_d))
            first_stage = tuple(first_stage_values) if len(first_stage_values) == 4 else None

        if not g_assignment_reasons and observed_v is not None:
            z0_focal_rows = [(observed_v[i], row) for i, row in enumerate(evidence.rows)
                             if row["assignment_z"] == 0]
            g0 = [v for v, row in z0_focal_rows if row["assignment_g"] == 0]
            g1 = [v for v, row in z0_focal_rows if row["assignment_g"] == 1]
            g_assignment_estimate, g_assignment_se = _mean_se(g0, g1)
            g_assignment_status: Identification = "IDENTIFIED" if g_assignment_estimate is not None else "INDETERMINATE"
        else:
            g_assignment_estimate, g_assignment_se = None, None
            g_assignment_status = "NOT_IDENTIFIED" if (
                "COMMON_SUPPORT_FAILURE" in g_assignment_reasons or
                "G_RANDOMIZATION_NOT_ESTABLISHED" in g_assignment_reasons
            ) else "INDETERMINATE"

        reasons = tuple(dict.fromkeys(package_reasons + g_assignment_reasons))
        payload = {"run_id": evidence.run_id, "estimand_id": contract.estimand_id,
                   "package_status": package_status, "g_assignment_status": g_assignment_status,
                   "package_itt": package, "g_assignment_effect": g_assignment_estimate,
                   "first_stage_delta_t_acc": first_stage,
                   "package_se": package_se, "g_assignment_se": g_assignment_se,
                   "reasons": list(reasons), "input_sha256": evidence.sha256,
                   "target_regime_id": contract.target_regime_id, "target_regime_version": contract.target_regime_version,
                   "outcome_id": contract.outcome_id, "outcome_version": contract.outcome_version,
                   "reference_regime_status": reference_regime_status,
                   "reference_regime_id": contract.reference_regime_id, "reference_regime_version": contract.reference_regime_version,
                   "g_assignment_mechanism_hash": contract.g_assignment_mechanism_hash,
                   "z_assignment_mechanism_hash": contract.z_assignment_mechanism_hash,
                   "transportability_id": contract.transportability_id,
                   "transportability_version": contract.transportability_version,
                   "transportability_scope": contract.transportability_scope,
                   "transportability_evidence_status": contract.transportability_evidence_status,
                   "estimand_version": contract.estimand_version,
                   "g_assignment_mechanism_id": contract.g_assignment_mechanism_id,
                   "g_assignment_mechanism_version": contract.g_assignment_mechanism_version,
                   "z_assignment_mechanism_id": contract.z_assignment_mechanism_id,
                   "z_assignment_mechanism_version": contract.z_assignment_mechanism_version,
                   "reference_regime_id": contract.reference_regime_id,
                   "reference_regime_version": contract.reference_regime_version,
                   "provenance_sha256": evidence.manifest["provenance_sha256"]}
        return AnalyzerResult(evidence.run_id, contract.estimand_id, package_status, g_assignment_status,
            package, g_assignment_estimate, first_stage, package_se, g_assignment_se, reasons, evidence.sha256,
            _hash(payload), contract.target_regime_id, contract.target_regime_version, contract.outcome_id, contract.outcome_version,
            reference_regime_status, contract.reference_regime_id, contract.reference_regime_version,
            contract.g_assignment_mechanism_hash, contract.z_assignment_mechanism_hash,
            contract.transportability_id, contract.transportability_version,
            contract.transportability_scope, contract.transportability_evidence_status,
            contract.estimand_version, contract.g_assignment_mechanism_id, contract.g_assignment_mechanism_version,
            contract.z_assignment_mechanism_id, contract.z_assignment_mechanism_version,
            evidence.manifest["provenance_sha256"])


class Evaluator:
    def evaluate(self, truth: TruthBundle, result: AnalyzerResult,
                 contract: AnalysisContract, tolerance: float, manifest: RunManifest) -> EvaluationReport:
        if tolerance < 0 or truth.run_id != result.run_id or manifest.run_id != truth.run_id:
            raise ContractError("invalid tolerance or run mismatch")
        payload = {
            "run_id": result.run_id, "estimand_id": result.estimand_id,
            "package_status": result.package_status, "g_assignment_status": result.g_assignment_status,
            "package_itt": result.package_itt, "g_assignment_effect": result.g_assignment_effect,
            "first_stage_delta_t_acc": result.first_stage_delta_t_acc,
            "package_se": result.package_se, "g_assignment_se": result.g_assignment_se,
            "reasons": list(result.abstention_reasons), "input_sha256": result.input_sha256,
            "target_regime_id": result.target_regime_id, "target_regime_version": result.target_regime_version,
            "outcome_id": result.outcome_id, "outcome_version": result.outcome_version,
            "reference_regime_status": result.reference_regime_status,
            "reference_regime_id": result.reference_regime_id,
            "reference_regime_version": result.reference_regime_version,
            "g_assignment_mechanism_hash": result.g_assignment_mechanism_hash,
            "z_assignment_mechanism_hash": result.z_assignment_mechanism_hash,
            "transportability_id": result.transportability_id,
            "transportability_version": result.transportability_version,
            "transportability_scope": result.transportability_scope,
            "transportability_evidence_status": result.transportability_evidence_status,
            "estimand_version": result.estimand_version,
            "g_assignment_mechanism_id": result.g_assignment_mechanism_id,
            "g_assignment_mechanism_version": result.g_assignment_mechanism_version,
            "z_assignment_mechanism_id": result.z_assignment_mechanism_id,
            "z_assignment_mechanism_version": result.z_assignment_mechanism_version,
            "reference_regime_id": result.reference_regime_id,
            "reference_regime_version": result.reference_regime_version,
            "provenance_sha256": result.provenance_sha256,
        }
        if _hash(payload) != result.output_sha256:
            raise FirewallError("Analyzer output seal invalid")
        manifest_provenance = {"run_id": manifest.run_id, "scenario_id": manifest.scenario_id,
            "scenario_version": manifest.version, "world_id": manifest.world_id,
            "world_version": manifest.world_version, "replicate_id": manifest.replicate_id,
            "g_assignment_mechanism_id": manifest.g_assignment_mechanism_id,
            "g_assignment_mechanism_version": manifest.g_assignment_mechanism_version,
            "g_assignment_mechanism_hash": manifest.g_assignment_mechanism_hash,
            "z_assignment_mechanism_id": manifest.z_assignment_mechanism_id,
            "z_assignment_mechanism_version": manifest.z_assignment_mechanism_version,
            "z_assignment_mechanism_hash": manifest.z_assignment_mechanism_hash,
            "g_reference_regime_id": manifest.g_reference_regime_id,
            "g_reference_regime_version": manifest.g_reference_regime_version,
            "z_assignment_vector_hash": manifest.z_assignment_vector_hash,
            "g_assignment_vector_hash": manifest.g_assignment_vector_hash}
        if (result.estimand_id != contract.estimand_id or result.estimand_version != contract.estimand_version or
            result.target_regime_id != contract.target_regime_id or result.target_regime_version != contract.target_regime_version or
            result.outcome_id != contract.outcome_id or result.outcome_version != contract.outcome_version or
            result.reference_regime_id != manifest.g_reference_regime_id or result.reference_regime_version != manifest.g_reference_regime_version or
            result.g_assignment_mechanism_id != manifest.g_assignment_mechanism_id or result.g_assignment_mechanism_version != manifest.g_assignment_mechanism_version or
            result.z_assignment_mechanism_id != manifest.z_assignment_mechanism_id or result.z_assignment_mechanism_version != manifest.z_assignment_mechanism_version or
            result.g_assignment_mechanism_hash != manifest.g_assignment_mechanism_hash or result.z_assignment_mechanism_hash != manifest.z_assignment_mechanism_hash or
            truth.g_assignment_mechanism_hash != manifest.g_assignment_mechanism_hash or truth.z_assignment_mechanism_hash != manifest.z_assignment_mechanism_hash or
            result.provenance_sha256 != _hash(manifest_provenance) or
            result.g_assignment_mechanism_id != contract.g_assignment_mechanism_id or result.g_assignment_mechanism_version != contract.g_assignment_mechanism_version or
            result.z_assignment_mechanism_id != contract.z_assignment_mechanism_id or result.z_assignment_mechanism_version != contract.z_assignment_mechanism_version or
            result.reference_regime_id != contract.reference_regime_id or result.reference_regime_version != contract.reference_regime_version or
            result.transportability_id != contract.transportability_id or result.transportability_version != contract.transportability_version or
            result.transportability_scope != contract.transportability_scope or result.transportability_evidence_status != contract.transportability_evidence_status):
            raise ContractError("run, scenario, estimand, regime, mechanism, provenance, transportability or outcome identity mismatch")
        if contract.z_effect_invariant_across_g and (truth.transportability_invariant_truth is not True or truth.transportability_scope_truth != contract.transportability_scope or contract.transportability_outcome_id != contract.outcome_id):
            raise ContractError("declared transportability is not supported for the declared scope/outcome by DGP truth")
        package_target = truth.itt_z_run_truth
        package_error = None if result.package_itt is None or package_target is None else abs(result.package_itt - package_target)
        # Analyzer's G-assignment estimate is adjudicated against its matching
        # assignment truth, never against theta_A.
        g_assignment_error = (
            None if result.g_assignment_effect is None or result.g_assignment_status != "IDENTIFIED"
            else abs(result.g_assignment_effect - truth.itt_g_z0_truth)
        )
        package_ok = None if package_error is None else package_error <= tolerance
        g_assignment_ok = (
            None if g_assignment_error is None
            else g_assignment_error <= tolerance
        )
        if not contract.randomized_z or not contract.randomized_g:
            expected_reference_status: Identification = "NOT_IDENTIFIED"
        elif not contract.positivity and truth.transportability_invariant_truth is False:
            expected_reference_status = "NOT_IDENTIFIED"
        elif (not contract.no_interference or not contract.measurement_identified or not contract.version_consistency):
            expected_reference_status = "INDETERMINATE"
        elif not contract.positivity and (truth.transportability_invariant_truth is not True or truth.transportability_scope_truth != contract.transportability_scope or contract.transportability_evidence_status != "STRUCTURALLY_VERIFIED"):
            expected_reference_status = "INDETERMINATE"
        else:
            expected_reference_status = "IDENTIFIED"
        reference_status_correct = result.reference_regime_status == expected_reference_status
        expected_abstention = (
            ((not contract.randomized_z or not contract.no_interference or not contract.measurement_identified or not contract.version_consistency) and result.package_status in ("NOT_IDENTIFIED", "INDETERMINATE"))
            or ((not contract.positivity or not contract.randomized_g) and result.g_assignment_status in ("NOT_IDENTIFIED", "INDETERMINATE"))
            or (expected_reference_status != "IDENTIFIED" and reference_status_correct)
        )
        notes = []
        if result.package_status == "IDENTIFIED" and package_ok is False:
            notes.append("PACKAGE_ESTIMATE_OUTSIDE_TOLERANCE")
        if result.g_assignment_status == "IDENTIFIED" and g_assignment_ok is False:
            notes.append("G_ASSIGNMENT_ESTIMATE_OUTSIDE_TOLERANCE")
        if not reference_status_correct:
            notes.append("REFERENCE_REGIME_IDENTIFICATION_STATUS_MISMATCH")
        return EvaluationReport(truth.run_id, package_error, g_assignment_error,
                                package_ok, g_assignment_ok, expected_abstention, tuple(notes), reference_status_correct)

    def evaluate_repeated_assignment(self, runs: list[tuple[TruthBundle, AnalyzerResult, AnalysisContract, RunManifest]], tolerance: float) -> RepeatedAssignmentReport:
        if not runs or tolerance < 0:
            raise ContractError("nonempty repeated-assignment runs and nonnegative tolerance required")
        world_ids = {run[3].world_id for run in runs}
        mechanism_truths = {run[0].itt_z_mechanism_truth for run in runs}
        if len(world_ids) != 1 or len(mechanism_truths) != 1 or None in mechanism_truths:
            raise ContractError("repeated-assignment evaluation requires one fixed world and one defined mechanism truth")
        reports = tuple(self.evaluate(truth, result, contract, tolerance, manifest)
                        for truth, result, contract, manifest in runs)
        estimates = [result.package_itt for _, result, _, _ in runs]
        if any(value is None or result.package_status != "IDENTIFIED"
               for value, (_, result, _, _) in zip(estimates, runs)):
            marginal_estimate = None
            marginal_error = None
            recovered = None
        else:
            marginal_estimate = mean(estimates)
            target = next(iter(mechanism_truths))
            marginal_error = abs(marginal_estimate - target)
            recovered = marginal_error <= tolerance
        return RepeatedAssignmentReport(next(iter(world_ids)), len(runs), marginal_estimate,
            next(iter(mechanism_truths)), marginal_error, recovered, reports)


def benchmark_scenarios(n_units: int = 400, n_intervals: int = 20,
                        seed: int = 20261112) -> tuple[ScenarioConfig, ...]:
    """Explicit candidate design points; not empirical rates or confirmatory defaults."""
    common = dict(
        version="VCONT-SYNTH-001", n_units=n_units, n_intervals=n_intervals,
        seed=seed, window_start=0.0, last_transition_support=0.8, follow_up=0.2,
        enabled_probability=0.98, baseline_conformity=0.55, focal_access_effect=0.20,
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
        ("R2_SUPPORT_FAILURE_ZG_INTERACTION", "R2", "SUPPORT_FAILURE_ZG_INTERACTION", {"positivity": False, "alternative_probability": 0.65, "collateral_effect": 0.10, "zg_interaction_effect": 0.30}),
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
        estimand_id="ITT_Z_RUN_CONDITIONAL_AND_ITT_G_Z0", estimand_version="002",
        randomized_z=cfg.randomized_z,
        randomized_g=cfg.randomized_g,
        positivity=cfg.positivity,
        no_interference=cfg.no_interference,
        measurement_identified=cfg.measurement_identified,
        version_consistency=cfg.version_consistency,
        focal_direct_path_absent=(cfg.focal_direct_effect == 0.0),
        common_nonfocal_regime=True, target_regime_id="G_REALIZED_VECTOR", target_regime_version="001",
        outcome_id="V_CONT", outcome_version="001",
        z_effect_invariant_across_g=(not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 and cfg.package_direct_effect == 0.0 and cfg.collateral_effect == 0.0 and cfg.heterogeneity == 0.0 and cfg.no_interference),
        transportability_id=("R0_TOTAL_Z_EFFECT_INVARIANCE" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else None),
        transportability_version=("001" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else None),
        transportability_scope=("HIGH" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else None),
        transportability_evidence_status=("STRUCTURALLY_VERIFIED" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else "NOT_ESTABLISHED"),
        transportability_outcome_id=("V_CONT" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else None),
        transportability_basis=("Complete DGP potential-outcome invariance: all Z-dependent terms are absent and shared exogenous draws are reused" if not cfg.positivity and cfg.profile == "R0" and cfg.zg_interaction_effect == 0.0 else None),
        g_assignment_mechanism_id=("G_BALANCED_WITH_STRATUM_SUPPORT" if not cfg.positivity else "G_BALANCED"),
        g_assignment_mechanism_version="001", z_assignment_mechanism_id="Z_BALANCED_INDEPENDENT",
        z_assignment_mechanism_version="001", reference_regime_id="G_REFERENCE_50_50", reference_regime_version="001",
        g_assignment_mechanism_hash=_hash({"algorithm": "balanced_binary_then_zero_HIGH_if_support_failure", "positivity": cfg.positivity, "n": cfg.n_units}),
        z_assignment_mechanism_hash=_hash({"algorithm": "balanced_binary_complete_randomization", "n": cfg.n_units}),
    )
