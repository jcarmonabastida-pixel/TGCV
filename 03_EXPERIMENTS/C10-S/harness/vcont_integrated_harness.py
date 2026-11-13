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
    outer_replicate_id: str = "outer-000000"
    assignment_role: str = "REPEATED_ASSIGNMENT"
    assignment_index: int = -1

    def validate(self) -> None:
        if not self.scenario_id or not self.version or not self.outer_replicate_id:
            raise ContractError("scenario, version and outer-replicate identity required")
        if self.assignment_role not in ("RUN", "REPEATED_ASSIGNMENT"):
            raise ContractError("assignment_role must be RUN or REPEATED_ASSIGNMENT")
        if ((self.assignment_role == "RUN" and self.assignment_index != -1)
                or (self.assignment_role == "REPEATED_ASSIGNMENT" and self.assignment_index < 0)):
            raise ContractError("assignment_index must be -1 for RUN and nonnegative for repeated assignments")
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
    run_conditional_estimand_id: str = "ITT_Z_RUN_CONDITIONAL_VCONT"
    run_conditional_estimand_version: str = "001"
    mechanism_marginal_estimand_id: str = "ITT_Z_MECHANISM_MARGINAL_VCONT"
    mechanism_marginal_estimand_version: str = "001"
    reference_regime_estimand_id: str = "ITT_Z_REFERENCE_REGIME_VCONT"
    reference_regime_estimand_version: str = "001"
    g_assignment_estimand_id: str = "ITT_G_Z0_VCONT"
    g_assignment_estimand_version: str = "001"

    def validate(self) -> None:
        if not self.estimand_id or not self.estimand_version or not self.target_regime_id or not self.target_regime_version:
            raise ContractError("estimand and target-regime identity/version required")
        expected_estimands = (
            ("ITT_Z_RUN_CONDITIONAL_VCONT", "001"),
            ("ITT_Z_MECHANISM_MARGINAL_VCONT", "001"),
            ("ITT_Z_REFERENCE_REGIME_VCONT", "001"),
            ("ITT_G_Z0_VCONT", "001"),
        )
        declared_estimands = (
            (self.run_conditional_estimand_id, self.run_conditional_estimand_version),
            (self.mechanism_marginal_estimand_id, self.mechanism_marginal_estimand_version),
            (self.reference_regime_estimand_id, self.reference_regime_estimand_version),
            (self.g_assignment_estimand_id, self.g_assignment_estimand_version),
        )
        if declared_estimands != expected_estimands:
            raise ContractError("assignment-estimand identities/versions do not match the registered V_cont contract")
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
    outer_replicate_id: str = "outer-000000"
    assignment_role: str = "REPEATED_ASSIGNMENT"
    assignment_index: int = -1


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
    outer_replicate_id: str = "outer-000000"
    assignment_role: str = "REPEATED_ASSIGNMENT"
    assignment_index: int = -1

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
    transportability_outcome_id: str | None = None
    transportability_basis: str | None = None
    reference_regime_itt: float | None = None
    run_conditional_estimand_id: str = "ITT_Z_RUN_CONDITIONAL_VCONT"
    run_conditional_estimand_version: str = "001"
    reference_regime_estimand_id: str = "ITT_Z_REFERENCE_REGIME_VCONT"
    reference_regime_estimand_version: str = "001"
    g_assignment_estimand_id: str = "ITT_G_Z0_VCONT"
    g_assignment_estimand_version: str = "001"
    outer_replicate_id: str = "outer-000000"
    assignment_role: str = "REPEATED_ASSIGNMENT"
    assignment_index: int = -1


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
    reference_regime_estimate_present: bool = False


@dataclass(frozen=True)
class RepeatedAssignmentReport:
    world_id: str
    replicate_count: int
    mean_run_estimate: float | None
    mechanism_truth: float
    marginal_abs_error: float | None
    marginal_recovered: bool | None
    per_run_reports: tuple[EvaluationReport, ...]
    reference_truth: float | None = None
    reference_estimate_mean: float | None = None
    reference_abs_error: float | None = None
    reference_recovered: bool | None = None
    reference_identification_status: Identification = "INDETERMINATE"
    mechanism_marginal_estimand_id: str = "ITT_Z_MECHANISM_MARGINAL_VCONT"
    mechanism_marginal_estimand_version: str = "001"
    reference_regime_estimand_id: str = "ITT_Z_REFERENCE_REGIME_VCONT"
    reference_regime_estimand_version: str = "001"


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
        for key in ("seed", "world_seed", "z_assignment_seed", "g_assignment_seed",
                    "replicate_id", "assignment_role", "assignment_index"):
            world_spec.pop(key, None)
        world_id = _hash({"world_seed": world_seed, "outer_replicate_id": cfg.outer_replicate_id,
                          "world_spec": world_spec})
        run_id = _hash({"config": asdict(cfg), "replicate_id": cfg.replicate_id,
                        "outer_replicate_id": cfg.outer_replicate_id,
                        "assignment_role": cfg.assignment_role, "world_id": world_id,
                        "z_seed": z_seed, "g_seed": g_seed})[:24]
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
        g_probabilities = (("LOW", 0.5), ("HIGH", 0.0 if not cfg.positivity else 0.5))
        gh = _hash({"algorithm": "balanced_binary_then_zero_HIGH_if_support_failure", "positivity": cfg.positivity, "n": cfg.n_units, "probability_by_stratum": g_probabilities})
        zh = _hash({"algorithm": "balanced_binary_complete_randomization", "n": cfg.n_units})
        manifest = RunManifest(run_id, cfg.scenario_id, cfg.version, cfg.n_units, cfg.n_intervals,
            cfg.window_start, window_end, interval_width, self.version,
            world_id, cfg.version, cfg.replicate_id,
            "G_BALANCED_WITH_STRATUM_SUPPORT" if not cfg.positivity else "G_BALANCED", "001", gh,
            "Z_BALANCED_INDEPENDENT", "001", zh, "G_REFERENCE_50_50", "001",
            _hash(z_assign), _hash(g_assign), (("LOW", 0.5), ("HIGH", 0.0 if not cfg.positivity else 0.5)),
            world_seed, z_seed, g_seed, cfg.outer_replicate_id, cfg.assignment_role, cfg.assignment_index)
        truth = TruthBundle(run_id, tuple(v_truth), tuple(interval_truth), tuple(enabled_truth), tuple(profile_truth), tuple(delta_truth),
            itt_reference, itt_g_z0, None, cfg.seed, itt_run, itt_mechanism, itt_reference, invariant_truth,
            "HIGH" if unsupported_high else "ALL", "G_REFERENCE_50_50", "001", gh, zh,
            cfg.outer_replicate_id, cfg.assignment_role, cfg.assignment_index)
        provenance = {"run_id": run_id, "scenario_id": cfg.scenario_id, "scenario_version": cfg.version,
            "world_id": world_id, "world_version": cfg.version, "replicate_id": cfg.replicate_id,
            "outer_replicate_id": cfg.outer_replicate_id, "assignment_role": cfg.assignment_role,
            "assignment_index": cfg.assignment_index,
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
        provenance_allowed = {"run_id", "scenario_id", "scenario_version", "world_id", "world_version",
            "replicate_id", "outer_replicate_id", "assignment_role", "assignment_index",
            "g_assignment_mechanism_id", "g_assignment_mechanism_version",
            "g_assignment_mechanism_hash", "z_assignment_mechanism_id", "z_assignment_mechanism_version",
            "z_assignment_mechanism_hash", "g_reference_regime_id", "g_reference_regime_version",
            "z_assignment_vector_hash", "g_assignment_vector_hash"}
        if not candidate.provenance or set(candidate.provenance) != provenance_allowed or candidate.provenance.get("run_id") != candidate.run_id:
            raise FirewallError("provenance envelope contains reserved/missing fields or run mismatch")
        if _hash([row["assignment_z"] for row in candidate.rows]) != candidate.provenance.get("z_assignment_vector_hash") or _hash([row["assignment_g"] for row in candidate.rows]) != candidate.provenance.get("g_assignment_vector_hash"):
            raise ContractError("assignment vectors do not match provenance hashes")
        manifest = {"run_id": candidate.run_id, "schema": "C10S-VCONT-S3-001",
                    "row_count": len(candidate.rows), "sealer_version": "0.2",
                    "outer_replicate_id": candidate.provenance["outer_replicate_id"],
                    "assignment_role": candidate.provenance["assignment_role"],
                    "assignment_index": candidate.provenance["assignment_index"],
                    "provenance": candidate.provenance, "provenance_sha256": _hash(candidate.provenance)}
        digest = _hash({"manifest": manifest, "rows": candidate.rows})
        return SealedEvidence(candidate.run_id, candidate.rows, manifest, digest)


class Analyzer:
    version = "c10s-vcont-analyzer-0.1"

    def analyze(self, evidence: SealedEvidence, contract: AnalysisContract) -> AnalyzerResult:
        contract.validate()
        if _hash({"manifest": evidence.manifest, "rows": evidence.rows}) != evidence.sha256:
            raise FirewallError("sealed evidence integrity failure")
        provenance = evidence.manifest.get("provenance", {})
        if (provenance.get("run_id") != evidence.run_id or
            provenance.get("g_assignment_mechanism_id") != contract.g_assignment_mechanism_id or
            provenance.get("g_assignment_mechanism_version") != contract.g_assignment_mechanism_version or
            provenance.get("g_assignment_mechanism_hash") != contract.g_assignment_mechanism_hash or
            provenance.get("z_assignment_mechanism_id") != contract.z_assignment_mechanism_id or
            provenance.get("z_assignment_mechanism_version") != contract.z_assignment_mechanism_version or
            provenance.get("z_assignment_mechanism_hash") != contract.z_assignment_mechanism_hash or
            provenance.get("g_reference_regime_id") != contract.reference_regime_id or
            provenance.get("g_reference_regime_version") != contract.reference_regime_version):
            raise ContractError("analysis contract does not match sealed assignment provenance")
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
            if package is None:
                package_reasons.append("Z_REALIZED_ARM_SUPPORT_INSUFFICIENT")
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
            if g_assignment_estimate is None:
                g_assignment_reasons.append("G_REALIZED_ARM_SUPPORT_INSUFFICIENT")
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
                   "provenance_sha256": evidence.manifest["provenance_sha256"],
                   "transportability_outcome_id": contract.transportability_outcome_id,
                   "transportability_basis": contract.transportability_basis,
                   "reference_regime_itt": (package if reference_regime_status == "IDENTIFIED" and package_status == "IDENTIFIED" else None),
                   "run_conditional_estimand_id": contract.run_conditional_estimand_id,
                   "run_conditional_estimand_version": contract.run_conditional_estimand_version,
                   "reference_regime_estimand_id": contract.reference_regime_estimand_id,
                   "reference_regime_estimand_version": contract.reference_regime_estimand_version,
                   "g_assignment_estimand_id": contract.g_assignment_estimand_id,
                   "g_assignment_estimand_version": contract.g_assignment_estimand_version,
                   "outer_replicate_id": provenance["outer_replicate_id"],
                   "assignment_role": provenance["assignment_role"],
                   "assignment_index": provenance["assignment_index"]}
        reference_regime_itt = package if reference_regime_status == "IDENTIFIED" and package_status == "IDENTIFIED" else None
        return AnalyzerResult(evidence.run_id, contract.estimand_id, package_status, g_assignment_status,
            package, g_assignment_estimate, first_stage, package_se, g_assignment_se, reasons, evidence.sha256,
            _hash(payload), contract.target_regime_id, contract.target_regime_version, contract.outcome_id, contract.outcome_version,
            reference_regime_status, contract.reference_regime_id, contract.reference_regime_version,
            contract.g_assignment_mechanism_hash, contract.z_assignment_mechanism_hash,
            contract.transportability_id, contract.transportability_version,
            contract.transportability_scope, contract.transportability_evidence_status,
            contract.estimand_version, contract.g_assignment_mechanism_id, contract.g_assignment_mechanism_version,
            contract.z_assignment_mechanism_id, contract.z_assignment_mechanism_version,
            evidence.manifest["provenance_sha256"], contract.transportability_outcome_id,
            contract.transportability_basis, reference_regime_itt,
            contract.run_conditional_estimand_id, contract.run_conditional_estimand_version,
            contract.reference_regime_estimand_id, contract.reference_regime_estimand_version,
            contract.g_assignment_estimand_id, contract.g_assignment_estimand_version,
            provenance["outer_replicate_id"], provenance["assignment_role"], provenance["assignment_index"])


class Evaluator:
    def evaluate(self, truth: TruthBundle, result: AnalyzerResult,
                 contract: AnalysisContract, tolerance: float, manifest: RunManifest) -> EvaluationReport:
        contract.validate()
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
            "transportability_outcome_id": result.transportability_outcome_id,
            "transportability_basis": result.transportability_basis,
            "reference_regime_itt": result.reference_regime_itt,
            "run_conditional_estimand_id": result.run_conditional_estimand_id,
            "run_conditional_estimand_version": result.run_conditional_estimand_version,
            "reference_regime_estimand_id": result.reference_regime_estimand_id,
            "reference_regime_estimand_version": result.reference_regime_estimand_version,
            "g_assignment_estimand_id": result.g_assignment_estimand_id,
            "g_assignment_estimand_version": result.g_assignment_estimand_version,
            "outer_replicate_id": result.outer_replicate_id,
            "assignment_role": result.assignment_role,
            "assignment_index": result.assignment_index,
        }
        if _hash(payload) != result.output_sha256:
            raise FirewallError("Analyzer output seal invalid")
        manifest_provenance = {"run_id": manifest.run_id, "scenario_id": manifest.scenario_id,
            "scenario_version": manifest.version, "world_id": manifest.world_id,
            "world_version": manifest.world_version, "replicate_id": manifest.replicate_id,
            "outer_replicate_id": manifest.outer_replicate_id,
            "assignment_role": manifest.assignment_role,
            "assignment_index": manifest.assignment_index,
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
        expected_g_probabilities = (("LOW", 0.5), ("HIGH", 0.0 if not contract.positivity else 0.5))
        expected_g_hash = _hash({"algorithm": "balanced_binary_then_zero_HIGH_if_support_failure", "positivity": contract.positivity, "n": manifest.n_units, "probability_by_stratum": expected_g_probabilities})
        if manifest.g_assignment_probability_by_stratum != expected_g_probabilities or manifest.g_assignment_mechanism_hash != expected_g_hash:
            raise ContractError("RunManifest G assignment probabilities do not match the declared mechanism")
        if (result.estimand_id != contract.estimand_id or result.estimand_version != contract.estimand_version or
            result.run_conditional_estimand_id != contract.run_conditional_estimand_id or result.run_conditional_estimand_version != contract.run_conditional_estimand_version or
            result.reference_regime_estimand_id != contract.reference_regime_estimand_id or result.reference_regime_estimand_version != contract.reference_regime_estimand_version or
            result.g_assignment_estimand_id != contract.g_assignment_estimand_id or result.g_assignment_estimand_version != contract.g_assignment_estimand_version or
            result.target_regime_id != contract.target_regime_id or result.target_regime_version != contract.target_regime_version or
            result.outcome_id != contract.outcome_id or result.outcome_version != contract.outcome_version or
            result.reference_regime_id != manifest.g_reference_regime_id or result.reference_regime_version != manifest.g_reference_regime_version or
            result.g_assignment_mechanism_id != manifest.g_assignment_mechanism_id or result.g_assignment_mechanism_version != manifest.g_assignment_mechanism_version or
            result.z_assignment_mechanism_id != manifest.z_assignment_mechanism_id or result.z_assignment_mechanism_version != manifest.z_assignment_mechanism_version or
            result.g_assignment_mechanism_hash != manifest.g_assignment_mechanism_hash or result.z_assignment_mechanism_hash != manifest.z_assignment_mechanism_hash or
            result.g_assignment_mechanism_hash != contract.g_assignment_mechanism_hash or result.z_assignment_mechanism_hash != contract.z_assignment_mechanism_hash or
            truth.g_assignment_mechanism_hash != manifest.g_assignment_mechanism_hash or truth.z_assignment_mechanism_hash != manifest.z_assignment_mechanism_hash or
            truth.g_reference_regime_id != manifest.g_reference_regime_id or truth.g_reference_regime_version != manifest.g_reference_regime_version or
            result.outer_replicate_id != manifest.outer_replicate_id or
            result.assignment_role != manifest.assignment_role or
            result.assignment_index != manifest.assignment_index or
            truth.outer_replicate_id != manifest.outer_replicate_id or
            truth.assignment_role != manifest.assignment_role or
            truth.assignment_index != manifest.assignment_index or
            result.provenance_sha256 != _hash(manifest_provenance) or
            result.g_assignment_mechanism_id != contract.g_assignment_mechanism_id or result.g_assignment_mechanism_version != contract.g_assignment_mechanism_version or
            result.z_assignment_mechanism_id != contract.z_assignment_mechanism_id or result.z_assignment_mechanism_version != contract.z_assignment_mechanism_version or
            result.reference_regime_id != contract.reference_regime_id or result.reference_regime_version != contract.reference_regime_version or
            result.transportability_id != contract.transportability_id or result.transportability_version != contract.transportability_version or
            result.transportability_scope != contract.transportability_scope or result.transportability_evidence_status != contract.transportability_evidence_status or
            result.transportability_outcome_id != contract.transportability_outcome_id or result.transportability_basis != contract.transportability_basis):
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
        reference_estimate_present = result.reference_regime_itt is not None
        if expected_reference_status == "IDENTIFIED" and reference_estimate_present != (result.package_status == "IDENTIFIED"):
            raise ContractError("reference-regime estimator presence must match identified package evidence")
        if expected_reference_status != "IDENTIFIED" and reference_estimate_present:
            raise ContractError("reference-regime estimator must be absent when reference target is not identified")
        expected_abstention = (
            ((not contract.randomized_z or not contract.no_interference or not contract.measurement_identified or not contract.version_consistency) and result.package_status in ("NOT_IDENTIFIED", "INDETERMINATE"))
            or ((not contract.positivity or not contract.randomized_g) and result.g_assignment_status in ("NOT_IDENTIFIED", "INDETERMINATE"))
            or ("Z_REALIZED_ARM_SUPPORT_INSUFFICIENT" in result.abstention_reasons and result.package_status == "INDETERMINATE")
            or ("G_REALIZED_ARM_SUPPORT_INSUFFICIENT" in result.abstention_reasons and result.g_assignment_status == "INDETERMINATE")
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
                                package_ok, g_assignment_ok, expected_abstention, tuple(notes),
                                reference_status_correct, reference_estimate_present)

    def evaluate_repeated_assignment(self, runs: list[tuple[TruthBundle, AnalyzerResult, AnalysisContract, RunManifest]], tolerance: float) -> RepeatedAssignmentReport:
        if not runs or tolerance < 0:
            raise ContractError("nonempty repeated-assignment runs and nonnegative tolerance required")
        world_ids = {run[3].world_id for run in runs}
        outer_ids = {run[3].outer_replicate_id for run in runs}
        roles = {run[3].assignment_role for run in runs}
        mechanism_truths = {run[0].itt_z_mechanism_truth for run in runs}
        reference_truths = {run[0].itt_z_reference_truth for run in runs}
        reference_statuses = {run[1].reference_regime_status for run in runs}
        mechanism_estimand_ids = {(run[2].mechanism_marginal_estimand_id, run[2].mechanism_marginal_estimand_version) for run in runs}
        reference_estimand_ids = {(run[2].reference_regime_estimand_id, run[2].reference_regime_estimand_version) for run in runs}
        g_mechanism_ids = {(run[3].g_assignment_mechanism_id, run[3].g_assignment_mechanism_version,
                            run[3].g_assignment_mechanism_hash, run[3].g_reference_regime_id,
                            run[3].g_reference_regime_version) for run in runs}
        z_mechanism_ids = {(run[3].z_assignment_mechanism_id, run[3].z_assignment_mechanism_version,
                            run[3].z_assignment_mechanism_hash) for run in runs}
        if (len(world_ids) != 1 or len(outer_ids) != 1 or roles != {"REPEATED_ASSIGNMENT"}
                or len(mechanism_truths) != 1
                or len(g_mechanism_ids) != 1 or len(z_mechanism_ids) != 1
                or len(reference_truths) != 1 or len(reference_statuses) != 1
                or len(mechanism_estimand_ids) != 1 or len(reference_estimand_ids) != 1
                or None in mechanism_truths or None in reference_truths):
            raise ContractError("repeated-assignment evaluation requires one outer identity/world, R-only assignment roles, homogeneous G/Z mechanisms and defined truths/status")
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
        reference_status = next(iter(reference_statuses))
        reference_values = [result.reference_regime_itt for _, result, _, _ in runs]
        if reference_status != "IDENTIFIED" or any(value is None for value in reference_values):
            reference_mean = reference_error = reference_recovered = None
        else:
            reference_mean = mean(reference_values)
            reference_error = abs(reference_mean - next(iter(reference_truths)))
            reference_recovered = reference_error <= tolerance
        return RepeatedAssignmentReport(next(iter(world_ids)), len(runs), marginal_estimate,
            next(iter(mechanism_truths)), marginal_error, recovered, reports,
            next(iter(reference_truths)), reference_mean, reference_error,
            reference_recovered, reference_status,
            next(iter(mechanism_estimand_ids))[0], next(iter(mechanism_estimand_ids))[1],
            next(iter(reference_estimand_ids))[0], next(iter(reference_estimand_ids))[1])


    def evaluate_matrix_pairs(self, runs, tolerance: float, matrix=None):
        """Evaluate this scenario against its versioned matrix at run and repeat levels.

        Each run contributes run-conditional, reference-regime and ITT-G records.
        Mechanism-marginal is emitted once from the repeated-assignment aggregate.
        """
        from vcont_benchmark_protocol import (
            PairEvaluationAdapter, ProtocolError, build_scenario_estimand_matrix,
        )
        runs = tuple(runs)
        if not runs:
            raise ContractError("matrix evaluation requires at least one run")
        scenario_versions = {(item[3].scenario_id, item[3].version) for item in runs}
        world_ids = {item[3].world_id for item in runs}
        outer_ids = {item[3].outer_replicate_id for item in runs}
        roles = {item[3].assignment_role for item in runs}
        if len(scenario_versions) != 1 or len(world_ids) != 1 or len(outer_ids) != 1 or roles != {"REPEATED_ASSIGNMENT"}:
            raise ContractError("matrix repeated evaluation requires one scenario/version, one outer world and R-only assignment roles")
        scenario_id, scenario_version = next(iter(scenario_versions))
        specs = tuple(matrix) if matrix is not None else build_scenario_estimand_matrix()
        selected = tuple(spec for spec in specs if spec.key.scenario_id == scenario_id)
        if len(selected) != 4 or {spec.key.scenario_version for spec in selected} != {scenario_version}:
            raise ProtocolError("matrix must contain exactly four pairs for the observed scenario/version")
        if len({spec.key for spec in selected}) != 4:
            raise ProtocolError("matrix contains duplicate scenario-estimand keys")
        adapter = PairEvaluationAdapter()
        per_run_reports = []
        records = []
        for truth, result, contract, manifest in runs:
            if manifest.scenario_id != scenario_id or manifest.version != scenario_version:
                raise ContractError("run manifest scenario identity/version changed within repeated set")
            per_run_reports.append(self.evaluate(truth, result, contract, tolerance, manifest))
            for spec in selected:
                if spec.key.estimand_id == "ITT_Z_MECHANISM_MARGINAL_VCONT":
                    continue
                records.append(adapter.adapt_run(spec, truth, result, manifest, tolerance))
        repeated = self.evaluate_repeated_assignment(list(runs), tolerance)
        representative_manifest = runs[0][3]
        for spec in selected:
            if spec.key.estimand_id in ("ITT_Z_MECHANISM_MARGINAL_VCONT", "ITT_Z_REFERENCE_REGIME_VCONT"):
                records.append(adapter.adapt_repeated(spec, repeated, representative_manifest, tolerance))
        expected = {spec.key for spec in selected}
        if {record.key for record in records} != expected:
            raise ProtocolError("matrix adapter did not produce all four required estimand keys")
        return {
            "scenario_id": scenario_id,
            "scenario_version": scenario_version,
            "pair_records": tuple(records),
            "per_run_reports": tuple(per_run_reports),
            "repeated_assignment_report": repeated,
        }

    def evaluate_monte_carlo(self, outer_runs, tolerance: float, *,
                             target_mcse_by_metric: dict[str, float], matrix=None):
        """Aggregate benchmark metrics across M independent outer worlds.

        outer_runs maps outer_replicate_id to the runs generated within that world:
        exactly one designated RUN plus zero or more REPEATED_ASSIGNMENT rows.
        R is aggregated within each world before any metric is aggregated across M.
        """
        from vcont_benchmark_protocol import (
            ProtocolError, build_scenario_estimand_matrix, summarize_binary,
            summarize_monte_carlo, summarize_monte_carlo_rmse,
        )
        if (not isinstance(outer_runs, dict) or len(outer_runs) < 2 or tolerance < 0
                or target_mcse_by_metric is None):
            raise ContractError("Monte Carlo evaluation requires at least two named outer worlds, metric targets and nonnegative tolerance")
        scenario_versions = set()
        sample_sizes = set()
        world_ids = set()
        world_seeds = set()
        per_outer = []
        for outer_id, runs in outer_runs.items():
            runs = tuple(runs)
            if not outer_id or not runs:
                raise ContractError("each outer replicate requires an identity and at least one run")
            if any(item[3].outer_replicate_id != outer_id for item in runs):
                raise ContractError("run outer-replicate identity does not match its enclosing M group")
            run_rows = [item for item in runs if item[3].assignment_role == "RUN"]
            repeated_rows = [item for item in runs if item[3].assignment_role == "REPEATED_ASSIGNMENT"]
            if len(run_rows) != 1:
                raise ContractError("each outer world must contain exactly one designated RUN")
            all_world_ids = {item[3].world_id for item in runs}
            if len(all_world_ids) != 1:
                raise ContractError("RUN and R assignments must share one fixed world within each M")
            world_id = next(iter(all_world_ids))
            world_seed_values = {item[3].world_seed for item in runs}
            if len(world_seed_values) != 1:
                raise ContractError("RUN and R assignments must share one world seed within each M")
            world_seed = next(iter(world_seed_values))
            if world_id in world_ids or world_seed in world_seeds:
                raise ContractError("outer Monte Carlo replicates must have distinct world identities and world seeds")
            world_ids.add(world_id)
            world_seeds.add(world_seed)
            identities = {(item[3].scenario_id, item[3].version) for item in runs}
            if len(identities) != 1:
                raise ContractError("scenario/version must remain fixed across runs within an outer world")
            scenario_versions.update(identities)
            sample_sizes.update(item[3].n_units for item in runs)
            run_tuple = run_rows[0]
            run_report = self.evaluate(*run_tuple[:3], tolerance=tolerance, manifest=run_tuple[3])
            repeated_report = None
            if repeated_rows:
                repeated_report = self.evaluate_repeated_assignment(repeated_rows, tolerance)
            per_outer.append({
                "outer_replicate_id": outer_id,
                "run": run_tuple,
                "run_report": run_report,
                "repeated_report": repeated_report,
            })
        if len(scenario_versions) != 1 or len(sample_sizes) != 1:
            raise ContractError("Monte Carlo aggregation cannot pool scenario versions or N values")
        scenario_id, scenario_version = next(iter(scenario_versions))
        specs = tuple(matrix) if matrix is not None else build_scenario_estimand_matrix()
        selected = tuple(spec for spec in specs if spec.key.scenario_id == scenario_id
                         and spec.key.scenario_version == scenario_version)
        if len(selected) != 4 or len({spec.key for spec in selected}) != 4:
            raise ProtocolError("Monte Carlo aggregation requires the four authoritative matrix pairs")
        m = len(per_outer)

        metric_prefix_by_estimand = {
            "ITT_Z_RUN_CONDITIONAL_VCONT": "run_conditional",
            "ITT_G_Z0_VCONT": "g_assignment_z0",
            "ITT_Z_MECHANISM_MARGINAL_VCONT": "mechanism_marginal",
            "ITT_Z_REFERENCE_REGIME_VCONT": "reference_regime",
        }
        required_metric_targets = set()
        for spec in selected:
            eligible = (
                spec.run_evaluation_class == "EVALUABLE"
                if spec.key.estimand_id in ("ITT_Z_RUN_CONDITIONAL_VCONT", "ITT_G_Z0_VCONT")
                else spec.repeated_evaluation_class == "EVALUABLE"
            )
            if eligible:
                prefix = metric_prefix_by_estimand[spec.key.estimand_id]
                required_metric_targets.update(
                    f"{prefix}.{metric}" for metric in ("bias", "mae", "rmse")
                )
        if set(target_mcse_by_metric) != required_metric_targets:
            raise ContractError("MCSE targets must cover exactly bias, MAE and RMSE for numeric EVALUABLE M-level metrics")
        def continuous_metric(values, metric_name):
            if metric_name not in target_mcse_by_metric or len(values) != m or any(value is None for value in values):
                return None
            return summarize_monte_carlo(
                [(row["outer_replicate_id"], value) for row, value in zip(per_outer, values)],
                expected_m=m, target_mcse=target_mcse_by_metric[metric_name],
            )
        def rmse_metric(values, metric_name):
            if metric_name not in target_mcse_by_metric or len(values) != m or any(value is None for value in values):
                return None
            return summarize_monte_carlo_rmse(
                [(row["outer_replicate_id"], value) for row, value in zip(per_outer, values)],
                expected_m=m, target_mcse=target_mcse_by_metric[metric_name],
            )

        def binary_metric(values):
            if len(values) != m or any(value is None for value in values):
                return None
            return summarize_binary(values, "outer-replicate status outcomes")

        run_signed_errors = [
            None if row["run"][1].package_itt is None or row["run"][0].itt_z_run_truth is None
            else row["run"][1].package_itt - row["run"][0].itt_z_run_truth
            for row in per_outer
        ]
        run_errors = [None if value is None else abs(value) for value in run_signed_errors]
        run_squared_errors = [None if value is None else value * value for value in run_signed_errors]
        run_recovered = [row["run_report"].package_recovered for row in per_outer]
        run_identified = [row["run"][1].package_status == "IDENTIFIED" for row in per_outer]
        g_signed_errors = [
            None if row["run"][1].g_assignment_effect is None
            else row["run"][1].g_assignment_effect - row["run"][0].itt_g_z0_truth
            for row in per_outer
        ]
        g_errors = [None if value is None else abs(value) for value in g_signed_errors]
        g_squared_errors = [None if value is None else value * value for value in g_signed_errors]
        g_recovered = [row["run_report"].g_assignment_recovered for row in per_outer]
        g_identified = [row["run"][1].g_assignment_status == "IDENTIFIED" for row in per_outer]
        mechanism_signed_errors = [
            None if row["repeated_report"] is None or row["repeated_report"].mean_run_estimate is None
            else row["repeated_report"].mean_run_estimate - row["repeated_report"].mechanism_truth
            for row in per_outer
        ]
        mechanism_errors = [None if value is None else abs(value) for value in mechanism_signed_errors]
        mechanism_squared_errors = [None if value is None else value * value for value in mechanism_signed_errors]
        mechanism_recovered = [
            None if row["repeated_report"] is None else row["repeated_report"].marginal_recovered
            for row in per_outer
        ]
        reference_signed_errors = [
            None if row["repeated_report"] is None
            or row["repeated_report"].reference_estimate_mean is None
            or row["repeated_report"].reference_truth is None
            else row["repeated_report"].reference_estimate_mean - row["repeated_report"].reference_truth
            for row in per_outer
        ]
        reference_errors = [None if value is None else abs(value) for value in reference_signed_errors]
        reference_squared_errors = [None if value is None else value * value for value in reference_signed_errors]
        reference_identified = [
            None if row["repeated_report"] is None else
            row["repeated_report"].reference_identification_status == "IDENTIFIED"
            for row in per_outer
        ]
        reference_recovered = [
            None if row["repeated_report"] is None else row["repeated_report"].reference_recovered
            for row in per_outer
        ]
        return {
            "scenario_id": scenario_id,
            "scenario_version": scenario_version,
            "n_units": next(iter(sample_sizes)),
            "outer_replicate_count": m,
            "coverage": {
                "required_pairs": len(selected),
                "run_conditional_numeric": sum(value is not None for value in run_errors),
                "g_assignment_numeric": sum(value is not None for value in g_errors),
                "mechanism_marginal_numeric": sum(value is not None for value in mechanism_errors),
                "reference_regime_numeric": sum(value is not None for value in reference_errors),
                "reference_regime_identification_status": sum(value is not None for value in reference_identified),
            },
            "run_conditional": {
                "bias": continuous_metric(run_signed_errors, "run_conditional.bias"),
                "mae": continuous_metric(run_errors, "run_conditional.mae"),
                "rmse": rmse_metric(run_squared_errors, "run_conditional.rmse"),
                "recovery_rate": binary_metric(run_recovered),
                "identification_rate": binary_metric(run_identified),
            },
            "g_assignment_z0": {
                "bias": continuous_metric(g_signed_errors, "g_assignment_z0.bias"),
                "mae": continuous_metric(g_errors, "g_assignment_z0.mae"),
                "rmse": rmse_metric(g_squared_errors, "g_assignment_z0.rmse"),
                "recovery_rate": binary_metric(g_recovered),
                "identification_rate": binary_metric(g_identified),
            },
            "mechanism_marginal": {
                "bias": continuous_metric(mechanism_signed_errors, "mechanism_marginal.bias"),
                "mae": continuous_metric(mechanism_errors, "mechanism_marginal.mae"),
                "rmse": rmse_metric(mechanism_squared_errors, "mechanism_marginal.rmse"),
                "recovery_rate": binary_metric(mechanism_recovered),
            },
            "reference_regime": {
                "bias": continuous_metric(reference_signed_errors, "reference_regime.bias"),
                "mae": continuous_metric(reference_errors, "reference_regime.mae"),
                "rmse": rmse_metric(reference_squared_errors, "reference_regime.rmse"),
                "identification_rate": binary_metric(reference_identified),
                "recovery_rate": binary_metric(reference_recovered),
            },
            "per_outer_replicate": tuple(per_outer),
        }


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
        g_assignment_mechanism_hash=_hash({"algorithm": "balanced_binary_then_zero_HIGH_if_support_failure", "positivity": cfg.positivity, "n": cfg.n_units, "probability_by_stratum": (("LOW", 0.5), ("HIGH", 0.0 if not cfg.positivity else 0.5))}),
        z_assignment_mechanism_hash=_hash({"algorithm": "balanced_binary_complete_randomization", "n": cfg.n_units}),
    )
