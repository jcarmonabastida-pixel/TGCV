"""Pre-registered descriptive/statistical summaries for the C10-S V_cont benchmark.

This module does not run simulations, select scientific thresholds, or turn a
synthetic benchmark into confirmatory evidence. It summarizes an independently
generated calibration/evaluation bank supplied by the caller.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from math import ceil, isfinite, sqrt
from statistics import mean, stdev
from typing import Iterable


class ProtocolError(ValueError):
    """Invalid benchmark inputs or an under-sized evaluation bank."""


@dataclass(frozen=True)
class ContinuousSummary:
    n: int
    truth: float
    estimate_mean: float
    bias: float
    mae: float
    rmse: float
    estimate_sd: float | None
    mcse_mean: float | None
    recovered_within_tolerance: bool | None


@dataclass(frozen=True)
class BinaryRateSummary:
    n: int
    successes: int
    rate: float
    mcse: float
    wilson_95_low: float
    wilson_95_high: float


@dataclass(frozen=True)
class ScenarioSummary:
    scenario_id: str
    estimate: ContinuousSummary | None
    identification_rate: BinaryRateSummary | None
    abstention_rate: BinaryRateSummary | None
    coverage_rate: BinaryRateSummary | None
    type_i_error_rate: BinaryRateSummary | None
    power_rate: BinaryRateSummary | None
    notes: tuple[str, ...]


def _finite_values(values: Iterable[float], name: str) -> tuple[float, ...]:
    result = tuple(float(x) for x in values)
    if not result or any(not isfinite(x) for x in result):
        raise ProtocolError(f"{name} must contain finite values and be nonempty")
    return result


def summarize_continuous(estimates: Iterable[float], truth: float,
                         tolerance: float | None = None) -> ContinuousSummary:
    xs = _finite_values(estimates, "estimates")
    if not isfinite(float(truth)):
        raise ProtocolError("truth must be finite")
    if tolerance is not None and (not isfinite(float(tolerance)) or tolerance < 0):
        raise ProtocolError("tolerance must be finite and nonnegative")
    errors = tuple(x - truth for x in xs)
    bias = mean(errors)
    mae = mean(abs(x) for x in errors)
    rmse = sqrt(mean(x * x for x in errors))
    sd = stdev(xs) if len(xs) >= 2 else None
    mcse = sd / sqrt(len(xs)) if sd is not None else None
    return ContinuousSummary(
        n=len(xs), truth=float(truth), estimate_mean=mean(xs), bias=bias,
        mae=mae, rmse=rmse, estimate_sd=sd, mcse_mean=mcse,
        recovered_within_tolerance=(abs(bias) <= tolerance if tolerance is not None else None),
    )


def summarize_binary(values: Iterable[bool | int], name: str = "binary outcomes") -> BinaryRateSummary:
    raw = tuple(values)
    if not raw or any(x not in (0, 1, False, True) for x in raw):
        raise ProtocolError(f"{name} must be a nonempty sequence of booleans/0/1")
    n = len(raw)
    successes = sum(int(x) for x in raw)
    p = successes / n
    mcse = sqrt(p * (1.0 - p) / n)
    # Wilson score interval: Monte Carlo uncertainty of a simulated rate,
    # not a confidence interval for a causal estimand.
    z = 1.959963984540054
    denom = 1.0 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return BinaryRateSummary(n, successes, p, mcse,
                             max(0.0, center-half), min(1.0, center+half))


def required_replicates(calibration_sd: float, target_mcse: float) -> int:
    """Minimum R for SD_cal/sqrt(R) <= target_mcse; R>=2."""
    if (not isfinite(calibration_sd) or calibration_sd < 0
            or not isfinite(target_mcse) or target_mcse <= 0):
        raise ProtocolError("calibration_sd must be >=0 and target_mcse >0, both finite")
    if calibration_sd == 0:
        return 2
    return max(2, ceil((calibration_sd / target_mcse) ** 2))


def summarize_scenario(
    scenario_id: str,
    *,
    estimates: Iterable[float] | None = None,
    truth: float | None = None,
    tolerance: float | None = None,
    identified: Iterable[bool] | None = None,
    abstained: Iterable[bool] | None = None,
    covered: Iterable[bool] | None = None,
    rejected_null: Iterable[bool] | None = None,
    rejected_alternative: Iterable[bool] | None = None,
) -> ScenarioSummary:
    if not scenario_id.strip():
        raise ProtocolError("scenario_id is required")
    estimate_summary = None
    if estimates is not None:
        if truth is None:
            raise ProtocolError("truth is required when estimates are supplied")
        estimate_summary = summarize_continuous(estimates, truth, tolerance)
    notes = []
    def rate(values, label):
        if values is None:
            return None
        return summarize_binary(values, label)
    identified_rate = rate(identified, "identification outcomes")
    abstention_rate = rate(abstained, "abstention outcomes")
    coverage_rate = rate(covered, "coverage outcomes")
    type_i_rate = rate(rejected_null, "null rejection outcomes")
    power_rate = rate(rejected_alternative, "alternative rejection outcomes")
    if coverage_rate is None:
        notes.append("COVERAGE_NOT_EVALUATED")
    if type_i_rate is None:
        notes.append("TYPE_I_ERROR_NOT_EVALUATED")
    if power_rate is None:
        notes.append("POWER_NOT_EVALUATED")
    return ScenarioSummary(scenario_id, estimate_summary, identified_rate,
                           abstention_rate, coverage_rate, type_i_rate,
                           power_rate, tuple(notes))


@dataclass(frozen=True)
class SeedAssignment:
    bank: str
    scenario_id: str
    n_units: int
    replicate: int
    world_seed: int
    z_assignment_seed: int
    g_assignment_seed: int
    scenario_version: str = "UNVERSIONED"


def _derive_seed(bank: str, scenario_id: str, n_units: int, replicate: int,
                 stream: str, namespace: str, scenario_version: str = "UNVERSIONED") -> int:
    if bank not in ("calibration", "evaluation"):
        raise ProtocolError("bank must be calibration or evaluation")
    if stream not in ("world", "z", "g"):
        raise ProtocolError("stream must be world, z or g")
    payload = f"TGCV-C10S-VCONT-SEED-v2|{namespace}|{bank}|{scenario_id}|{scenario_version}|{n_units}|{replicate}|{stream}"
    return int.from_bytes(hashlib.sha256(payload.encode("utf-8")).digest()[:8], "big")


def build_seed_bank(bank: str, scenarios: Iterable[str], n_grid: Iterable[int],
                    replicates: int, namespace: str,
                    scenario_versions: dict[str, str] | None = None) -> tuple[SeedAssignment, ...]:
    """Create deterministic, bank-separated seeds; each scenario/N has one fixed world.

    World seed is constant across assignment replicates for a scenario/N.
    Z and G assignment seeds vary independently by replicate and stream.
    Calibration and evaluation banks are cryptographically domain-separated.
    """
    scenario_ids = tuple(scenarios)
    sizes = tuple(n_grid)
    if bank not in ("calibration", "evaluation") or not namespace.strip():
        raise ProtocolError("valid bank and nonempty namespace required")
    if not scenario_ids or len(set(scenario_ids)) != len(scenario_ids):
        raise ProtocolError("scenario IDs must be nonempty and unique")
    if any(not x.strip() for x in scenario_ids):
        raise ProtocolError("scenario IDs must be nonempty")
    if not sizes or any(n < 16 or n % 4 for n in sizes) or len(set(sizes)) != len(sizes):
        raise ProtocolError("N grid must contain unique sizes >=16 divisible by four")
    if replicates < 1:
        raise ProtocolError("replicates must be >=1")
    versions = scenario_versions or {sid: "UNVERSIONED" for sid in scenario_ids}
    if set(versions) != set(scenario_ids) or any(not str(v).strip() for v in versions.values()):
        raise ProtocolError("scenario_versions must provide one nonempty version per scenario")
    plan = []
    for scenario_id in scenario_ids:
        scenario_version = versions[scenario_id]
        for n in sizes:
            world = _derive_seed(bank, scenario_id, n, 0, "world", namespace, scenario_version)
            for r in range(replicates):
                plan.append(SeedAssignment(
                    bank, scenario_id, n, r, world,
                    _derive_seed(bank, scenario_id, n, r, "z", namespace, scenario_version),
                    _derive_seed(bank, scenario_id, n, r, "g", namespace, scenario_version),
                    scenario_version,
                ))
    if bank == "calibration":
        validate_seed_banks(plan, ())
    else:
        validate_seed_banks((), plan)
    return tuple(plan)


def validate_seed_banks(calibration: Iterable[SeedAssignment],
                        evaluation: Iterable[SeedAssignment]) -> None:
    """Reject cross-bank seed reuse and within-record Z/G stream collisions."""
    cal = tuple(calibration)
    ev = tuple(evaluation)
    if any(x.bank != "calibration" for x in cal) or any(x.bank != "evaluation" for x in ev):
        raise ProtocolError("seed assignments are stored under the wrong bank label")
    def streams(rows):
        return {seed for row in rows for seed in
                (row.world_seed, row.z_assignment_seed, row.g_assignment_seed)}
    if streams(cal) & streams(ev):
        raise ProtocolError("calibration and evaluation banks share one or more seeds")
    for row in cal + ev:
        if len({row.world_seed, row.z_assignment_seed, row.g_assignment_seed}) != 3:
            raise ProtocolError("world, Z and G streams must use distinct seeds within each assignment record")
    for rows in (cal, ev):
        world_by_design = {}
        for row in rows:
            key = (row.scenario_id, row.scenario_version, row.n_units)
            if key in world_by_design and world_by_design[key] != row.world_seed:
                raise ProtocolError("world seed must remain fixed across assignment replicates within scenario/N")
            world_by_design[key] = row.world_seed


def select_minimum_n(mcse_by_n: dict[int, dict[str, float]],
                     target_mcse_by_scenario: dict[str, float]) -> int:
    """Choose the smallest candidate N meeting every predeclared scenario MCSE target.

    This is a calibration rule only. Targets and the candidate N grid must be
    supplied before evaluation-bank outcomes are inspected.
    """
    if not mcse_by_n or not target_mcse_by_scenario:
        raise ProtocolError("candidate MCSE results and predeclared targets are required")
    if any(not isfinite(float(v)) or v <= 0 for v in target_mcse_by_scenario.values()):
        raise ProtocolError("all target MCSE values must be finite and >0")
    for n in sorted(mcse_by_n):
        observed = mcse_by_n[n]
        if set(observed) != set(target_mcse_by_scenario):
            continue
        if all(isfinite(float(observed[s])) and observed[s] >= 0
               and observed[s] <= target_mcse_by_scenario[s]
               for s in target_mcse_by_scenario):
            return n
    raise ProtocolError("NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_MCSE_TARGETS")


def seed_bank_fingerprint(assignments: Iterable[SeedAssignment]) -> str:
    """Stable SHA-256 fingerprint for a fully materialized seed-bank manifest."""
    rows = tuple(assignments)
    if not rows:
        raise ProtocolError("cannot fingerprint an empty seed bank")
    banks = {row.bank for row in rows}
    if len(banks) != 1:
        raise ProtocolError("a seed-bank fingerprint must contain exactly one bank")
    payload = [
        {"bank": row.bank, "scenario_id": row.scenario_id, "scenario_version": row.scenario_version, "n_units": row.n_units,
         "replicate": row.replicate, "world_seed": row.world_seed,
         "z_assignment_seed": row.z_assignment_seed,
         "g_assignment_seed": row.g_assignment_seed}
        for row in rows
    ]
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


from enum import Enum


class EvaluationClass(str, Enum):
    EVALUABLE = "EVALUABLE"
    STATUS_ONLY = "STATUS_ONLY"
    NOT_IDENTIFIABLE = "NOT_IDENTIFIABLE"
    NOT_EVALUABLE = "NOT_EVALUABLE"


class TruthStatus(str, Enum):
    DEFINED = "DEFINED"
    UNDEFINED = "UNDEFINED"
    NOT_MATERIALIZED = "NOT_MATERIALIZED"


@dataclass(frozen=True, order=True)
class EvaluationKey:
    scenario_id: str
    scenario_version: str
    estimand_id: str
    estimand_version: str

    def validate(self) -> None:
        if not all((self.scenario_id, self.scenario_version, self.estimand_id, self.estimand_version)):
            raise ProtocolError("scenario and estimand IDs/versions are required")


@dataclass(frozen=True)
class ScenarioEstimandSpec:
    key: EvaluationKey
    evaluation_class: str
    truth_status: str
    dgp_truth_field: str
    analyzer_output_field: str | None
    aggregation_field: str | None
    identification_expectation: str
    abstention_expectation: bool
    tolerance_id: str | None
    reason: str


@dataclass(frozen=True)
class EstimandSummary:
    key: EvaluationKey
    evaluation_class: str
    truth_status: str
    estimate: ContinuousSummary | None
    identification_rate: BinaryRateSummary | None
    not_identified_rate: BinaryRateSummary | None
    indeterminate_rate: BinaryRateSummary | None
    abstention_rate: BinaryRateSummary | None
    precision_status: str
    recovery_status: str


ESTIMAND_SPECS = (
    ("ITT_Z_RUN_CONDITIONAL_VCONT", "itt_z_run_truth", "package_itt", None),
    ("ITT_Z_MECHANISM_MARGINAL_VCONT", "itt_z_mechanism_truth", "package_itt", "mean_run_estimate"),
    ("ITT_Z_REFERENCE_REGIME_VCONT", "itt_z_reference_truth", "reference_regime_itt", "reference_estimate_mean"),
    ("ITT_G_Z0_VCONT", "itt_g_z0_truth", "g_assignment_effect", None),
)
SCENARIO_IDS = (
    "R0_FOCAL_POSITIVE", "R0_FOCAL_NULL", "R0_FOCAL_ADVERSE",
    "R0_DIRECT_G", "R0_DIRECT_Z", "R1_ALTERNATIVE_BASELINE",
    "R2_ALTERNATIVE_AFFECTED", "R3_PROVISION_FAILURE",
    "R0_MEASUREMENT_ADVERSE", "R0_INTERFERENCE", "R0_SUPPORT_FAILURE",
    "R0_HETEROGENEITY", "R2_SUPPORT_FAILURE_ZG_INTERACTION",
)


def build_scenario_estimand_matrix(scenario_versions: dict[str, str] | None = None) -> tuple[ScenarioEstimandSpec, ...]:
    """Build all 52 coverage records; DGP truth is never inferred from Analyzer output."""
    versions = scenario_versions or {sid: "VCONT-SYNTH-001" for sid in SCENARIO_IDS}
    if set(versions) != set(SCENARIO_IDS) or any(not str(v).strip() for v in versions.values()):
        raise ProtocolError("scenario_versions must provide one nonempty version for every benchmark scenario")
    result = []
    for sid in SCENARIO_IDS:
        for estimand_id, truth_field, output_field, aggregation_field in ESTIMAND_SPECS:
            status_only = sid in ("R0_MEASUREMENT_ADVERSE", "R0_INTERFERENCE")
            not_identifiable = (
                (sid == "R2_SUPPORT_FAILURE_ZG_INTERACTION" and estimand_id in ("ITT_Z_REFERENCE_REGIME_VCONT", "ITT_G_Z0_VCONT"))
                or (sid == "R0_SUPPORT_FAILURE" and estimand_id == "ITT_G_Z0_VCONT")
            )
            if not_identifiable:
                cls, identification, abstain = "NOT_IDENTIFIABLE", "NOT_IDENTIFIED", True
                reason = "REFERENCE_NO_TRANSPORTABILITY" if estimand_id == "ITT_Z_REFERENCE_REGIME_VCONT" else "G_NO_COMMON_SUPPORT"
            elif status_only:
                cls, identification, abstain = "STATUS_ONLY", "INDETERMINATE", True
                reason = "MEASUREMENT_NOT_IDENTIFIED" if sid == "R0_MEASUREMENT_ADVERSE" else "UNIT_INTERFERENCE"
            else:
                cls, identification, abstain = "EVALUABLE", "IDENTIFIED", False
                if sid == "R0_SUPPORT_FAILURE" and estimand_id == "ITT_Z_REFERENCE_REGIME_VCONT":
                    reason = "REFERENCE_TRANSPORTABILITY_R0"
                elif estimand_id == "ITT_Z_REFERENCE_REGIME_VCONT":
                    reason = "REFERENCE_COMMON_SUPPORT"
                elif estimand_id == "ITT_G_Z0_VCONT":
                    reason = "G_COMMON_SUPPORT"
                elif estimand_id == "ITT_Z_RUN_CONDITIONAL_VCONT":
                    reason = "Z_RANDOMIZED_G_REALIZED"
                else:
                    reason = "Z_RANDOMIZED_G_MECHANISM"
            key = EvaluationKey(sid, versions[sid], estimand_id, "001")
            result.append(ScenarioEstimandSpec(key, cls, "DEFINED", truth_field,
                output_field if cls == "EVALUABLE" else None,
                aggregation_field if cls == "EVALUABLE" else None,
                identification, abstain,
                "OPEN_UNASSIGNED" if cls == "EVALUABLE" else None, reason))
    return tuple(result)


def validate_evaluation_observation(spec: ScenarioEstimandSpec, *, observed_key: EvaluationKey,
                                    analyzer_output_field: str | None, dgp_truth: float | None,
                                    analyzer_output: float | None, adjudication: str) -> None:
    spec.key.validate()
    observed_key.validate()
    if observed_key != spec.key:
        raise ProtocolError("observed scenario-estimand identity/version does not match the declared pair")
    if spec.evaluation_class == "EVALUABLE":
        if spec.truth_status != "DEFINED" or dgp_truth is None or not isfinite(float(dgp_truth)):
            raise ProtocolError("EVALUABLE pair requires DEFINED finite numeric DGP truth")
        if analyzer_output_field != spec.analyzer_output_field or not analyzer_output_field:
            raise ProtocolError("Analyzer output field does not match the declared estimand")
        if analyzer_output is None or not isfinite(float(analyzer_output)):
            raise ProtocolError("EVALUABLE pair requires matching finite Analyzer output")
        if adjudication not in ("PASS", "FAIL"):
            raise ProtocolError("EVALUABLE pair requires numeric recovery adjudication")
    elif spec.evaluation_class in ("STATUS_ONLY", "NOT_IDENTIFIABLE"):
        if analyzer_output_field is not None or adjudication not in ("STATUS_PASS", "STATUS_FAIL") or analyzer_output is not None:
            raise ProtocolError("status-only pair requires status adjudication and no numeric scoring")
    elif spec.evaluation_class == "NOT_EVALUABLE":
        if analyzer_output_field is not None or analyzer_output is not None or adjudication == "PASS":
            raise ProtocolError("NOT_EVALUABLE cannot receive numeric scoring or PASS")
    else:
        raise ProtocolError("unsupported evaluation class")


def summarize_estimand(spec: ScenarioEstimandSpec, *, estimates: Iterable[float] | None = None,
                       truth: float | None = None, tolerance: float | None = None,
                       identified: Iterable[bool] | None = None,
                       not_identified: Iterable[bool] | None = None,
                       indeterminate: Iterable[bool] | None = None,
                       abstained: Iterable[bool] | None = None,
                       mcse_target: float | None = None) -> EstimandSummary:
    if spec.evaluation_class == "EVALUABLE":
        if estimates is None or truth is None:
            raise ProtocolError("EVALUABLE pair requires estimates and DGP truth")
        estimate = summarize_continuous(estimates, truth, tolerance)
        precision = ("PASS" if estimate.mcse_mean is not None and mcse_target is not None and estimate.mcse_mean <= mcse_target else "NOT_EVALUABLE")
        recovery = "PASS" if estimate.recovered_within_tolerance is True else "FAIL" if estimate.recovered_within_tolerance is False else "NOT_EVALUABLE"
    else:
        if estimates is not None or truth is not None:
            raise ProtocolError("non-numeric evaluation classes cannot receive numeric scoring")
        estimate, precision, recovery = None, "NOT_APPLICABLE", "NOT_APPLICABLE"
    rate = lambda values, name: None if values is None else summarize_binary(values, name)
    return EstimandSummary(spec.key, spec.evaluation_class, spec.truth_status, estimate,
        rate(identified, "identified"), rate(not_identified, "not identified"),
        rate(indeterminate, "indeterminate"), rate(abstained, "abstained"), precision, recovery)


def select_minimum_n_by_estimand(mcse_by_n: dict[int, dict[EvaluationKey, float]],
                                 target_mcse_by_estimand: dict[EvaluationKey, float],
                                 required_keys: Iterable[EvaluationKey], numeric_keys: Iterable[EvaluationKey],
                                 coverage_by_n: dict[int, Iterable[EvaluationKey]]) -> int:
    """Select smallest N with complete coverage and all numeric MCSE targets met."""
    required, numeric = set(required_keys), set(numeric_keys)
    if not required or not numeric or not numeric.issubset(required):
        raise ProtocolError("required coverage and numeric estimand key sets are invalid")
    if set(target_mcse_by_estimand) != numeric or set(mcse_by_n) != set(coverage_by_n):
        raise ProtocolError("MCSE targets/candidate coverage do not match the declared key sets")
    for key, target in target_mcse_by_estimand.items():
        key.validate()
        if not isfinite(float(target)) or target <= 0:
            raise ProtocolError("MCSE targets must be finite and >0")
    for n in sorted(mcse_by_n):
        observed, covered = mcse_by_n[n], set(coverage_by_n[n])
        if not required.issubset(covered) or not numeric.issubset(observed):
            continue
        if all(isfinite(float(observed[k])) and observed[k] >= 0 and observed[k] <= target_mcse_by_estimand[k] for k in numeric):
            return n
    raise ProtocolError("NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_ESTIMAND_MCSE_TARGETS_AND_COVERAGE")


def required_replicates_by_estimand(calibration_sd_by_estimand: dict[EvaluationKey, float],
                                    target_mcse_by_estimand: dict[EvaluationKey, float]) -> dict[EvaluationKey, int]:
    if not calibration_sd_by_estimand or set(calibration_sd_by_estimand) != set(target_mcse_by_estimand):
        raise ProtocolError("calibration SDs and MCSE targets need identical nonempty keys")
    return {key: required_replicates(float(calibration_sd_by_estimand[key]), float(target_mcse_by_estimand[key]))
            for key in calibration_sd_by_estimand}
