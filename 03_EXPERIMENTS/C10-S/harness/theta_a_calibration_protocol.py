"""Focal theta_A calibration design and aggregation.

This protocol is separate from the legacy 13x52 V_cont assignment benchmark.
It defines N units per world, M independent outer worlds, and R repeated
joint-policy assignments within each fixed world. It never executes a
calibration or creates a bank unless its explicit builder is called.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from math import isfinite, sqrt
from statistics import mean, stdev
from typing import Iterable, Literal, Sequence


class ThetaACalibrationError(ValueError):
    """Invalid focal calibration design, seed bank, or replicate evidence."""


Bank = Literal["calibration", "evaluation"]
Identification = Literal["IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"]
_VALID_IDENTIFICATION = {"IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"}
_VALID_ANALYZER_IDENTIFICATION = _VALID_IDENTIFICATION | {"PARTIALLY_IDENTIFIED"}
FOCAL_ESTIMAND_ID = "THETA_A_QX_GA_RCOMMON_VCONT"
FOCAL_OUTCOME_ID = "V_CONT"
_ALLOWED_METRICS = {
    "interval_coverage", "interval_width", "point_bias", "point_mae",
    "point_rmse", "point_recovery_rate", "identification_rate",
    "abstention_rate", "interval_availability_rate", "false_abstention_rate",
    "correct_abstention_rate", "wrong_cause_abstention_rate",
    "partial_identification_rate", "false_identification_rate",
}


@dataclass(frozen=True)
class ThetaACalibrationDGPProfile:
    """Versioned, synthetic-only support profile for one focal DGP scenario."""
    profile_id: str
    profile_version: str
    target_q_x_sha256: str
    source_q_x_sha256: str
    structural_support_contract_id: str
    structural_support_contract_version: str
    support_relation: Literal["EQUAL", "SOURCE_STRICT_SUPERSET", "TARGET_HAS_UNSUPPORTED_HISTORIES"]
    target_unsupported_history_masses: tuple[tuple[str, float], ...] = ()
    expected_abstention_reason: str | None = None

    def validate(self) -> None:
        identities = (
            self.profile_id, self.profile_version, self.structural_support_contract_id,
            self.structural_support_contract_version,
        )
        if any(not isinstance(value, str) or not value.strip() for value in identities):
            raise ThetaACalibrationError("typed DGP profile and structural-support contract identities/versions are mandatory")
        for value in (self.target_q_x_sha256, self.source_q_x_sha256):
            if len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
                raise ThetaACalibrationError("DGP profile requires target/source lowercase SHA-256 fingerprints")
        if self.support_relation not in {
            "EQUAL", "SOURCE_STRICT_SUPERSET", "TARGET_HAS_UNSUPPORTED_HISTORIES"
        }:
            raise ThetaACalibrationError("unsupported target/source support relation")
        refs = [row[0] for row in self.target_unsupported_history_masses]
        if len(refs) != len(set(refs)) or any(not ref for ref in refs):
            raise ThetaACalibrationError("unsupported target-history references must be nonempty and unique")
        if any(not isfinite(mass) or mass <= 0.0 for _, mass in self.target_unsupported_history_masses):
            raise ThetaACalibrationError("unsupported target-history masses must be finite and positive")
        mass = sum(value for _, value in self.target_unsupported_history_masses)
        if mass > 1.0 + 1e-12:
            raise ThetaACalibrationError("unsupported target mass cannot exceed one")
        if self.support_relation == "TARGET_HAS_UNSUPPORTED_HISTORIES":
            if not self.target_unsupported_history_masses or self.expected_abstention_reason != "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT":
                raise ThetaACalibrationError("target-only profile requires unsupported mass and its exact Analyzer reason")
        elif self.target_unsupported_history_masses or self.expected_abstention_reason is not None:
            raise ThetaACalibrationError("benign/equal support profiles cannot declare target-only mass or abstention reason")

    @property
    def fingerprint_sha256(self) -> str:
        return _canonical_hash(asdict(self))


@dataclass(frozen=True)
class ThetaACalibrationScenario:
    scenario_id: str
    scenario_version: str
    world_version: str
    dgp_id: str
    dgp_version: str
    roster_version: str
    unit_id_prefix: str
    expected_identification: Identification
    unit_independence_certified: bool
    independence_basis: str = ""
    dgp_profile: ThetaACalibrationDGPProfile | None = None

    @property
    def dgp_profile_sha256(self) -> str:
        return _canonical_hash(asdict(self.dgp_profile)) if self.dgp_profile is not None else _canonical_hash({"profile": None})

    def validate(self) -> None:
        if not all((
            self.scenario_id.strip(), self.scenario_version.strip(),
            self.world_version.strip(), self.dgp_id.strip(), self.dgp_version.strip(),
            self.roster_version.strip(), self.unit_id_prefix.strip(),
        )):
            raise ThetaACalibrationError("focal scenario, world, DGP and roster identities/versions are required")
        if self.expected_identification not in _VALID_IDENTIFICATION:
            raise ThetaACalibrationError(
                "focal calibration currently supports IDENTIFIED, NOT_IDENTIFIED or INDETERMINATE truth classes"
            )
        if self.dgp_profile is not None:
            self.dgp_profile.validate()
        if self.expected_identification == "NOT_IDENTIFIED" and self.dgp_profile is None:
            raise ThetaACalibrationError("NOT_IDENTIFIED scenarios require a typed DGP/support profile")
        if self.expected_identification == "NOT_IDENTIFIED" and self.dgp_profile.expected_abstention_reason is None:
            raise ThetaACalibrationError("NOT_IDENTIFIED scenarios require an exact expected abstention reason")
        if type(self.unit_independence_certified) is not bool:
            raise ThetaACalibrationError("unit-independence declaration must be Boolean")
        if self.unit_independence_certified and not self.independence_basis.strip():
            raise ThetaACalibrationError("unit-independence certification requires an explicit design basis")
        if self.expected_identification == "IDENTIFIED" and not self.unit_independence_certified:
            raise ThetaACalibrationError(
                "the current individual-level theta_A HT target requires certified unit independence"
            )


@dataclass(frozen=True)
class ThetaACalibrationDesign:
    scenario_specs: tuple[ThetaACalibrationScenario, ...]
    n_grid: tuple[int, ...]
    outer_worlds_m: int
    assignment_replicates_r: int
    confidence_level: float
    namespace: str
    point_recovery_tolerance: float | None = None
    metric_targets: tuple[tuple[str, str, int, str, float], ...] = ()

    def validate(self) -> None:
        if not self.scenario_specs:
            raise ThetaACalibrationError("at least one focal scenario contract is required")
        for scenario in self.scenario_specs:
            scenario.validate()
        keys = [(x.scenario_id, x.scenario_version) for x in self.scenario_specs]
        if len(keys) != len(set(keys)):
            raise ThetaACalibrationError("focal scenario/version identities must be unique")
        if not self.n_grid or any(type(n) is not int or n < 1 for n in self.n_grid):
            raise ThetaACalibrationError("N grid must contain positive exact integers")
        if len(self.n_grid) != len(set(self.n_grid)):
            raise ThetaACalibrationError("N grid contains duplicate candidate sizes")
        if tuple(sorted(self.n_grid)) != self.n_grid:
            raise ThetaACalibrationError("N candidate grid must be in ascending canonical order")
        if (type(self.outer_worlds_m) is not int or type(self.assignment_replicates_r) is not int
                or self.outer_worlds_m < 2 or self.assignment_replicates_r < 2):
            raise ThetaACalibrationError("focal calibration requires exact integer M>=2 and R>=2")
        if not isfinite(self.confidence_level) or not 0.0 < self.confidence_level < 1.0:
            raise ThetaACalibrationError("confidence_level must be explicitly between zero and one")
        if not self.namespace.strip():
            raise ThetaACalibrationError("a dedicated focal calibration namespace is required")
        if self.point_recovery_tolerance is not None and (
            not isfinite(self.point_recovery_tolerance) or self.point_recovery_tolerance < 0
        ):
            raise ThetaACalibrationError("point-recovery tolerance must be finite and nonnegative")
        target_keys = []
        scenario_keys = set(keys)
        scenario_map = {(x.scenario_id, x.scenario_version): x for x in self.scenario_specs}
        for scenario_id, version, n_units, metric, target in self.metric_targets:
            if (scenario_id, version) not in scenario_keys or n_units not in self.n_grid:
                raise ThetaACalibrationError("metric target references an undeclared scenario/version/N")
            if metric not in _ALLOWED_METRICS or isinstance(target, bool) or not isfinite(target) or target <= 0:
                raise ThetaACalibrationError("metric targets require a supported metric and finite positive MCSE")
            scenario = scenario_map[(scenario_id, version)]
            if metric == "point_recovery_rate" and self.point_recovery_tolerance is None:
                raise ThetaACalibrationError("point-recovery target requires an explicit tolerance")
            identified_only = {
                "interval_coverage", "interval_width", "point_bias", "point_mae",
                "point_rmse", "point_recovery_rate", "false_abstention_rate",
            }
            abstention_only = {"correct_abstention_rate", "false_identification_rate"}
            if metric in identified_only and scenario.expected_identification != "IDENTIFIED":
                raise ThetaACalibrationError("identified-only metric target assigned to a nonidentified scenario")
            if metric in abstention_only and scenario.expected_identification == "IDENTIFIED":
                raise ThetaACalibrationError("abstention-only metric target assigned to an identified scenario")
            target_keys.append((scenario_id, version, n_units, metric))
        if len(target_keys) != len(set(target_keys)):
            raise ThetaACalibrationError("duplicate focal metric target")


def theta_a_pipeline_inference_options(
    design: ThetaACalibrationDesign,
    scenario: ThetaACalibrationScenario,
) -> dict[str, float | bool | None]:
    """Bind the explicit scenario independence declaration to pipeline inputs."""
    design.validate()
    scenario.validate()
    if scenario not in design.scenario_specs:
        raise ThetaACalibrationError("pipeline scenario is not part of the declared focal design")
    if scenario.unit_independence_certified:
        return {
            "theta_a_confidence_level": design.confidence_level,
            "theta_a_unit_independence_certified": True,
        }
    return {
        "theta_a_confidence_level": None,
        "theta_a_unit_independence_certified": False,
    }


@dataclass(frozen=True)
class ThetaASeedAssignment:
    bank: Bank
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_world_id: str
    assignment_replicate: int
    world_id: str
    roster_id: str
    world_version: str
    dgp_id: str
    dgp_version: str
    roster_version: str
    unit_id_prefix: str
    run_id: str
    world_seed: int
    randomization_salt: str
    s3_seed: int
    dgp_profile_sha256: str


def _digest(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _seed(payload: str) -> int:
    return int.from_bytes(hashlib.sha256(payload.encode("utf-8")).digest()[:8], "big")


def _canonical_hash(value) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_theta_a_seed_bank(
    design: ThetaACalibrationDesign, bank: Bank,
) -> tuple[ThetaASeedAssignment, ...]:
    """Materialize a focal N×M×R seed plan; no Generator or DGP is invoked.

    One world seed/world identity is fixed across all R assignments in M.
    Each R gets a new randomization salt and S3 stream. The existing assignment
    generator domain-separates its Bernoulli arm draw and joint-vector draw
    within that per-R salt.
    """
    design.validate()
    if bank not in ("calibration", "evaluation"):
        raise ThetaACalibrationError("bank must be calibration or evaluation")
    rows = []
    for scenario in design.scenario_specs:
        for n_units in design.n_grid:
            for m in range(design.outer_worlds_m):
                outer_id = f"outer-{m:06d}"
                root = (
                    f"TGCV-C10S-THETA-A-SEED-v1|{design.namespace}|{bank}|"
                    f"{scenario.scenario_id}|{scenario.scenario_version}|{scenario.dgp_profile_sha256}|{n_units}|{outer_id}"
                )
                world_seed = _seed(root + "|world")
                world_id = "theta-a-world-" + _digest(root + "|world-id")[:24]
                roster_id = "theta-a-roster-" + _digest(root + "|roster-id")[:24]
                unit_id_prefix = scenario.unit_id_prefix + "-" + _digest(root + "|unit-prefix")[:8]
                for r in range(design.assignment_replicates_r):
                    run_root = root + f"|assignment-{r:06d}"
                    rows.append(ThetaASeedAssignment(
                        bank=bank,
                        scenario_id=scenario.scenario_id,
                        scenario_version=scenario.scenario_version,
                        n_units=n_units,
                        outer_world_id=outer_id,
                        assignment_replicate=r,
                        world_id=world_id,
                        roster_id=roster_id,
                        world_version=scenario.world_version,
                        dgp_id=scenario.dgp_id,
                        dgp_version=scenario.dgp_version,
                        roster_version=scenario.roster_version,
                        unit_id_prefix=unit_id_prefix,
                        run_id="theta-a-run-" + _digest(run_root + "|run-id")[:24],
                        world_seed=world_seed,
                        randomization_salt=_digest(run_root + "|joint-policy-randomization"),
                        s3_seed=_seed(run_root + "|s3-measurement"),
                        dgp_profile_sha256=scenario.dgp_profile_sha256,
                    ))
    validate_theta_a_seed_banks(rows if bank == "calibration" else (),
                                rows if bank == "evaluation" else (),
                                design=design)
    return tuple(rows)


def validate_theta_a_seed_banks(
    calibration: Iterable[ThetaASeedAssignment],
    evaluation: Iterable[ThetaASeedAssignment],
    *,
    design: ThetaACalibrationDesign,
) -> None:
    """Fail-closed N/M/R completeness and disjointness check for focal banks."""
    design.validate()
    cal, ev = tuple(calibration), tuple(evaluation)
    if not cal and not ev:
        raise ThetaACalibrationError("at least one focal seed bank must be supplied")
    if any(row.bank != "calibration" for row in cal) or any(row.bank != "evaluation" for row in ev):
        raise ThetaACalibrationError("seed rows are stored under the wrong bank label")

    expected_scenarios = {(x.scenario_id, x.scenario_version) for x in design.scenario_specs}
    def validate_one(rows: tuple[ThetaASeedAssignment, ...], bank: Bank) -> None:
        expected = {
            (sid, version, n, f"outer-{m:06d}", r)
            for sid, version in expected_scenarios
            for n in design.n_grid
            for m in range(design.outer_worlds_m)
            for r in range(design.assignment_replicates_r)
        }
        actual = [
            (x.scenario_id, x.scenario_version, x.n_units,
             x.outer_world_id, x.assignment_replicate) for x in rows
        ]
        if len(actual) != len(set(actual)) or set(actual) != expected:
            raise ThetaACalibrationError(f"{bank} bank must contain every declared scenario×N×M×R row exactly once")
        if any(
            not x.world_id or not x.roster_id or not x.world_version
            or not x.dgp_id or not x.dgp_version or not x.roster_version
            or not x.unit_id_prefix or not x.run_id or not x.outer_world_id
            or type(x.n_units) is not int or x.n_units < 1
            or type(x.assignment_replicate) is not int or x.assignment_replicate < 0
            or type(x.world_seed) is not int or type(x.s3_seed) is not int
            or len(x.randomization_salt) != 64
            or any(ch not in "0123456789abcdef" for ch in x.randomization_salt)
            for x in rows
        ):
            raise ThetaACalibrationError("focal seed row has missing identity, invalid N/R or malformed stream material")
        scenario_map = {(x.scenario_id, x.scenario_version): x for x in design.scenario_specs}
        for row in rows:
            scenario = scenario_map[(row.scenario_id, row.scenario_version)]
            root = (
                f"TGCV-C10S-THETA-A-SEED-v1|{design.namespace}|{bank}|"
                f"{scenario.scenario_id}|{scenario.scenario_version}|{scenario.dgp_profile_sha256}|{row.n_units}|{row.outer_world_id}"
            )
            run_root = root + f"|assignment-{row.assignment_replicate:06d}"
            expected_derivation = (
                _seed(root + "|world"),
                "theta-a-world-" + _digest(root + "|world-id")[:24],
                "theta-a-roster-" + _digest(root + "|roster-id")[:24],
                scenario.unit_id_prefix + "-" + _digest(root + "|unit-prefix")[:8],
                "theta-a-run-" + _digest(run_root + "|run-id")[:24],
                _digest(run_root + "|joint-policy-randomization"),
                _seed(run_root + "|s3-measurement"),
            )
            actual = (
                row.world_seed, row.world_id, row.roster_id, row.unit_id_prefix,
                row.run_id, row.randomization_salt, row.s3_seed,
            )
            if actual != expected_derivation or (
                row.world_version != scenario.world_version
                or row.dgp_id != scenario.dgp_id
                or row.dgp_version != scenario.dgp_version
                or row.roster_version != scenario.roster_version
                or row.dgp_profile_sha256 != scenario.dgp_profile_sha256
            ):
                raise ThetaACalibrationError("focal seed row differs from its canonical scenario×N×M×R derivation")
        worlds = {}
        for row in rows:
            key = (row.scenario_id, row.scenario_version, row.n_units, row.outer_world_id)
            prior = worlds.setdefault(
                key,
                (row.world_id, row.roster_id, row.world_seed, row.world_version,
                 row.dgp_id, row.dgp_version, row.roster_version, row.unit_id_prefix),
            )
            current = (
                row.world_id, row.roster_id, row.world_seed, row.world_version,
                row.dgp_id, row.dgp_version, row.roster_version, row.unit_id_prefix,
            )
            if prior != current:
                raise ThetaACalibrationError("world/roster/DGP identity and seed must remain fixed across R within each M")
        by_design = {}
        for key, identity in worlds.items():
            by_design.setdefault(key[:3], []).append(identity)
        for values in by_design.values():
            world_ids = [x[0] for x in values]
            roster_ids = [x[1] for x in values]
            seeds = [x[2] for x in values]
            unit_prefixes = [x[7] for x in values]
            if (len(set(world_ids)) != len(values) or len(set(roster_ids)) != len(values)
                    or len(set(seeds)) != len(values) or len(set(unit_prefixes)) != len(values)):
                raise ThetaACalibrationError("independent outer worlds M require distinct world/roster/unit identities and seeds")
        distinct_worlds = {key: identity for key, identity in worlds.items()}
        if (len({x[0] for x in distinct_worlds.values()}) != len(distinct_worlds)
                or len({x[1] for x in distinct_worlds.values()}) != len(distinct_worlds)
                or len({x[2] for x in distinct_worlds.values()}) != len(distinct_worlds)
                or len({x[7] for x in distinct_worlds.values()}) != len(distinct_worlds)):
            raise ThetaACalibrationError("each distinct scenario×N×M world requires unique world/roster identities and seed")
        if len({x.run_id for x in rows}) != len(rows):
            raise ThetaACalibrationError("each M×R assignment requires a unique run_id")
        assignment_keys = [
            (x.scenario_id, x.scenario_version, x.n_units, x.outer_world_id, x.assignment_replicate)
            for x in rows
        ]
        if len({x.randomization_salt for x in rows}) != len(rows):
            raise ThetaACalibrationError("each R requires a distinct joint-policy randomization salt")
        if len({x.s3_seed for x in rows}) != len(rows):
            raise ThetaACalibrationError("each R requires a distinct S3 measurement seed")
        if {x.world_seed for x in rows} & {x.s3_seed for x in rows}:
            raise ThetaACalibrationError("world and S3 measurement streams must be disjoint")
        if len(assignment_keys) != len(expected):
            raise ThetaACalibrationError("focal seed bank row cardinality mismatch")

    validate_one(cal, "calibration") if cal else None
    validate_one(ev, "evaluation") if ev else None
    def streams(rows):
        return {
            "world": {x.world_seed for x in rows},
            "world_id": {x.world_id for x in rows},
            "assignment": {x.randomization_salt for x in rows},
            "s3": {x.s3_seed for x in rows},
            "run": {x.run_id for x in rows},
        }
    left, right = streams(cal), streams(ev)
    if any(left[key] & right[key] for key in left):
        raise ThetaACalibrationError("calibration and evaluation banks must be disjoint across every focal stream")
    if (left["world"] | left["s3"]) & (right["world"] | right["s3"]):
        raise ThetaACalibrationError("calibration and evaluation numeric seed streams must be cross-disjoint")


def s3_seeds_by_unit(seed: int, unit_ids: Sequence[str]) -> dict[str, int]:
    """Expand one R-specific S3 seed into deterministic unit-specific monitor seeds."""
    if type(seed) is not int:
        raise ThetaACalibrationError("S3 root seed must be an exact integer")
    if not unit_ids or any(not isinstance(x, str) or not x for x in unit_ids):
        raise ThetaACalibrationError("S3 seed expansion requires nonempty unit IDs")
    if len(unit_ids) != len(set(unit_ids)):
        raise ThetaACalibrationError("S3 seed expansion received duplicate unit IDs")
    result = {unit_id: _seed(f"TGCV-C10S-THETA-A-S3-UNIT-v1|{seed}|{unit_id}")
              for unit_id in unit_ids}
    if len(set(result.values())) != len(result):
        raise ThetaACalibrationError("derived S3 unit seeds collided")
    return result


@dataclass(frozen=True)
class ThetaAReplicateRecord:
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_world_id: str
    assignment_replicate: int
    world_id: str
    run_id: str
    estimand_id: str
    estimand_version: str
    outcome_id: str
    outcome_version: str
    expected_identification: Identification
    analyzer_identification: Identification
    truth: float
    point_estimate: float | None
    inference_lower_bound: float | None
    inference_upper_bound: float | None
    inference_covered: bool | None
    inference_width: float | None
    requested_confidence_level: float | None
    world_configuration_sha256: str
    policy_design_sha256: str
    assignment_randomization_sha256: str
    evidence_sha256: str
    analyzer_output_sha256: str
    dgp_profile_sha256: str
    expected_abstention_reason: str | None
    observed_abstention_reason: str | None
    target_unsupported_mass: float

    def validate(self) -> None:
        if not all((self.scenario_id, self.scenario_version, self.outer_world_id,
                    self.world_id, self.run_id, self.estimand_id,
                    self.estimand_version, self.outcome_id, self.outcome_version)):
            raise ThetaACalibrationError("replicate record identities and estimand/outcome versions are mandatory")
        if self.estimand_id != FOCAL_ESTIMAND_ID or self.outcome_id != FOCAL_OUTCOME_ID:
            raise ThetaACalibrationError("focal calibration is restricted to THETA_A_QX_GA_RCOMMON_VCONT over V_CONT")
        fingerprints = (
            self.world_configuration_sha256, self.policy_design_sha256,
            self.assignment_randomization_sha256, self.evidence_sha256,
            self.analyzer_output_sha256, self.dgp_profile_sha256,
        )
        if any(len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value)
               for value in fingerprints):
            raise ThetaACalibrationError("replicate record requires five lowercase SHA-256 fingerprints")
        if self.n_units < 1 or self.assignment_replicate < 0:
            raise ThetaACalibrationError("replicate record N/R identity is invalid")
        if (self.expected_identification not in _VALID_IDENTIFICATION
                or self.analyzer_identification not in _VALID_ANALYZER_IDENTIFICATION):
            raise ThetaACalibrationError("unsupported truth/analyzer identification status in replicate record")
        if not isfinite(self.truth) or not -1.0 <= self.truth <= 1.0:
            raise ThetaACalibrationError("theta_A truth must be finite and in [-1,1]")
        if not isfinite(self.target_unsupported_mass) or not 0.0 <= self.target_unsupported_mass <= 1.0:
            raise ThetaACalibrationError("replicate target unsupported mass must be finite and in [0,1]")
        if self.expected_identification == "NOT_IDENTIFIED" and not self.expected_abstention_reason:
            raise ThetaACalibrationError("NOT_IDENTIFIED replicate requires its exact expected abstention reason")
        if self.observed_abstention_reason is not None and not isinstance(self.observed_abstention_reason, str):
            raise ThetaACalibrationError("observed Analyzer abstention reason must be a string or None")
        if self.analyzer_identification == "IDENTIFIED":
            if self.point_estimate is None or not isfinite(self.point_estimate):
                raise ThetaACalibrationError("identified replicate requires a finite point estimate")
        elif self.point_estimate is not None:
            raise ThetaACalibrationError("abstaining replicate cannot contain a point estimate")
        interval = (self.inference_lower_bound, self.inference_upper_bound)
        if (interval[0] is None) != (interval[1] is None):
            raise ThetaACalibrationError("inferential interval bounds must be jointly present or absent")
        if self.requested_confidence_level is not None and (
            not isfinite(self.requested_confidence_level)
            or not 0.0 < self.requested_confidence_level < 1.0
        ):
            raise ThetaACalibrationError("requested confidence level must be finite and between zero and one")
        if interval[0] is None:
            if self.inference_covered is not None or self.inference_width is not None:
                raise ThetaACalibrationError("coverage/width cannot exist without an inferential interval")
        else:
            if (self.analyzer_identification != "IDENTIFIED"
                    or not isfinite(interval[0]) or not isfinite(interval[1])
                    or interval[0] > interval[1]
                    or type(self.inference_covered) is not bool
                    or self.inference_width is None or not isfinite(self.inference_width)
                    or not _close(self.inference_width, interval[1] - interval[0])
                    or self.requested_confidence_level is None
                    or self.inference_covered != (interval[0] <= self.truth <= interval[1])):
                raise ThetaACalibrationError("inferential interval evidence is inconsistent")


def _close(a: float, b: float) -> bool:
    return abs(a - b) <= 1e-12


def _validate_interval_s3_seed_provenance(result, assignment: ThetaASeedAssignment) -> None:
    """Require the focal continuous-interval lane and verify every emitted S3 seed."""
    rows = tuple(result.s3_records)
    unit_ids = {unit.unit_id for unit in result.world.units}
    if not rows or {row.unit_id for row in rows} != unit_ids:
        raise ThetaACalibrationError("focal calibration requires interval S3 coverage for the exact world roster")
    if any(
        getattr(row, "coverage_mode", None) != "CONTINUOUS_EVENT_COVERAGE"
        or getattr(row, "run_id", None) != assignment.run_id
        for row in rows
    ):
        raise ThetaACalibrationError(
            "focal confidence calibration requires continuous interval S3 records bound to this R; point samples are not eligible"
        )
    seeds = s3_seeds_by_unit(assignment.s3_seed, tuple(sorted(unit_ids)))
    by_unit = {}
    for row in rows:
        by_unit.setdefault(row.unit_id, []).append(row)
        expected_id = "IS3-" + _canonical_hash((
            row.run_id, row.unit_id, row.history_id,
            row.monitor_id, row.monitor_version, row.grid_id,
            row.grid_version, row.interval_index, seeds[row.unit_id],
        ))[:24]
        if row.observation_id != expected_id:
            raise ThetaACalibrationError("interval S3 observation ID does not bind to its assigned R-specific unit seed")
        if row.observation_status == "MISSING":
            if row.observed_compliance is not None:
                raise ThetaACalibrationError("missing S3 interval must not contain an observed compliance value")
        elif row.observation_status == "OBSERVED":
            if type(row.observed_compliance) is not bool:
                raise ThetaACalibrationError("observed S3 interval requires a Boolean compliance value")
        else:
            raise ThetaACalibrationError("unsupported interval S3 observation status")
    counts = {unit_id: len(unit_rows) for unit_id, unit_rows in by_unit.items()}
    if len(set(counts.values())) != 1:
        raise ThetaACalibrationError("all units must have the same complete interval-grid cardinality")
    common_grid = {
        (row.grid_id, row.grid_version, row.monitor_id, row.monitor_version)
        for row in rows
    }
    if len(common_grid) != 1:
        raise ThetaACalibrationError("focal interval S3 requires one common versioned grid and monitor")
    expected_boundaries = None
    for unit_id, unit_rows in by_unit.items():
        ordered = sorted(unit_rows, key=lambda row: row.interval_index)
        if [row.interval_index for row in ordered] != list(range(len(ordered))):
            raise ThetaACalibrationError("interval S3 indices must cover each grid cell exactly once")
        boundaries = tuple((row.interval_start, row.interval_end) for row in ordered)
        if any(left >= right for left, right in boundaries):
            raise ThetaACalibrationError("interval S3 cells must have positive duration")
        if any(boundaries[i][1] != boundaries[i + 1][0] for i in range(len(boundaries) - 1)):
            raise ThetaACalibrationError("interval S3 grid must be contiguous within each unit")
        if expected_boundaries is None:
            expected_boundaries = boundaries
        elif boundaries != expected_boundaries:
            raise ThetaACalibrationError("all units must share the exact same interval boundaries")


def _validate_truth_assignment_population_bindings(
    truth_bundle,
    assignment_bundle,
    analysis_contract,
) -> str:
    """Validate source-assignment and target-estimand fingerprints separately.

    Assignment/evidence are materialized over the source roster; the reserved
    focal truth is standardized over q_X*. These fingerprints coincide only
    when source and target populations (and their policy restrictions) coincide.
    """
    source_q_x = analysis_contract.source_q_x_sha256 or analysis_contract.q_x_sha256
    target_g_a0 = analysis_contract.target_g_a0_sha256 or analysis_contract.g_a0_sha256
    target_g_a1 = analysis_contract.target_g_a1_sha256 or analysis_contract.g_a1_sha256
    if (
        assignment_bundle.q_x_sha256 != source_q_x
        or assignment_bundle.g_a0_sha256 != analysis_contract.g_a0_sha256
        or assignment_bundle.g_a1_sha256 != analysis_contract.g_a1_sha256
        or assignment_bundle.r_common_sha256 != analysis_contract.r_common_sha256
    ):
        raise ThetaACalibrationError(
            "source assignment bundle fingerprints differ from the Analyzer source contract"
        )
    if (
        truth_bundle.q_x_fingerprint != analysis_contract.q_x_sha256
        or truth_bundle.g_a0_fingerprint != target_g_a0
        or truth_bundle.g_a1_fingerprint != target_g_a1
    ):
        raise ThetaACalibrationError(
            "reserved truth fingerprints differ from the Analyzer target estimand contract"
        )
    return _digest("|".join((
        source_q_x,
        assignment_bundle.g_a0_sha256,
        assignment_bundle.g_a1_sha256,
        assignment_bundle.r_common_sha256,
        analysis_contract.q_x_sha256,
        target_g_a0,
        target_g_a1,
        _canonical_hash(asdict(analysis_contract.structural_support_contract))
        if analysis_contract.structural_support_contract is not None else "",
    )))


def capture_theta_a_replicate(
    result,
    assignment: ThetaASeedAssignment,
    scenario: ThetaACalibrationScenario,
    *,
    requested_confidence_level: float | None,
) -> ThetaAReplicateRecord:
    """Capture evaluator-side metrics from one completed world without rerunning it."""
    scenario.validate()
    _validate_interval_s3_seed_provenance(result, assignment)
    if (result.world.world_id != assignment.world_id
            or result.world.roster_id != assignment.roster_id
            or result.world.world_version != assignment.world_version
            or result.world.dgp_id != assignment.dgp_id
            or result.world.dgp_version != assignment.dgp_version
            or result.world.roster_version != assignment.roster_version
            or len(result.world.units) != assignment.n_units
            or any(not unit.unit_id.startswith(assignment.unit_id_prefix) for unit in result.world.units)
            or result.world.seed_commitment_sha256 != _canonical_hash({"seed": assignment.world_seed})
            or result.analyzer_result.run_id != assignment.run_id
            or result.evaluator_result.run_id != assignment.run_id):
        raise ThetaACalibrationError("complete-world result does not match its focal M/R seed assignment")
    if (scenario.scenario_id, scenario.scenario_version) != (
        assignment.scenario_id, assignment.scenario_version
    ):
        raise ThetaACalibrationError("scenario contract differs from focal seed assignment")
    evaluation = result.evaluator_result
    truth_bundle = result.theta_a_truth.theta_a_truth
    profile = scenario.dgp_profile
    structural_contract = result.analyzer_contract.structural_support_contract
    unsupported_mass = 0.0
    if profile is not None:
        if structural_contract is None:
            raise ThetaACalibrationError("profiled DGP replicate is missing its structural-support contract")
        if (structural_contract.contract_id != profile.structural_support_contract_id
                or structural_contract.contract_version != profile.structural_support_contract_version
                or structural_contract.target_q_x_sha256 != profile.target_q_x_sha256
                or structural_contract.source_q_x_sha256 != profile.source_q_x_sha256):
            raise ThetaACalibrationError("materialized structural-support contract differs from the scenario DGP profile")
        actual_unsupported = tuple(sorted(
            (row.history_ref, row.target_mass)
            for row in structural_contract.rows if row.source_mass == 0.0
        ))
        expected_unsupported = tuple(sorted(profile.target_unsupported_history_masses))
        if actual_unsupported != expected_unsupported:
            raise ThetaACalibrationError("materialized target-only histories/masses differ from the typed DGP profile")
        unsupported_mass = sum(mass for _, mass in actual_unsupported)
        structural_digest = _canonical_hash(asdict(structural_contract))
        if result.analyzer_result.structural_support_sha256 != structural_digest:
            raise ThetaACalibrationError("Analyzer structural-support fingerprint differs from materialized contract")
    elif scenario.expected_identification == "NOT_IDENTIFIED":
        raise ThetaACalibrationError("structural non-identification capture requires a typed DGP profile")
    assignment_bundle = result.theta_a_assignments
    if (assignment_bundle.randomization_salt_sha256 != _canonical_hash(assignment.randomization_salt)):
        raise ThetaACalibrationError("actual assignment salt differs from its focal R seed assignment")
    policy_design_sha256 = _validate_truth_assignment_population_bindings(
        truth_bundle, assignment_bundle, result.analyzer_contract,
    )
    if (truth_bundle.estimand_id != FOCAL_ESTIMAND_ID
            or truth_bundle.outcome_id != FOCAL_OUTCOME_ID
            or result.analyzer_result.estimand_id != truth_bundle.estimand_id
            or result.analyzer_result.estimand_version != truth_bundle.estimand_version
            or evaluation.estimand_id != truth_bundle.estimand_id
            or evaluation.estimand_version != truth_bundle.estimand_version):
        raise ThetaACalibrationError("Analyzer/Evaluator estimand identity differs from reserved V_CONT truth")
    if (evaluation.truth != truth_bundle.theta_a_truth
            or evaluation.analyzer_identification != result.analyzer_result.identification
            or evaluation.point_estimate != result.analyzer_result.point_estimate):
        raise ThetaACalibrationError("Evaluator record differs from the supplied Analyzer and reserved truth")
    record = ThetaAReplicateRecord(
        assignment.scenario_id, assignment.scenario_version, assignment.n_units,
        assignment.outer_world_id, assignment.assignment_replicate,
        assignment.world_id, assignment.run_id,
        truth_bundle.estimand_id, truth_bundle.estimand_version,
        truth_bundle.outcome_id, truth_bundle.outcome_version,
        scenario.expected_identification, result.analyzer_result.identification,
        truth_bundle.theta_a_truth,
        result.analyzer_result.point_estimate,
        result.analyzer_result.inference_lower_bound,
        result.analyzer_result.inference_upper_bound,
        evaluation.inference_truth_covered,
        evaluation.inference_interval_width,
        requested_confidence_level,
        result.world.configuration_sha256,
        policy_design_sha256,
        assignment_bundle.randomization_salt_sha256,
        result.sealed_evidence.sha256,
        result.analyzer_result.output_sha256,
        scenario.dgp_profile_sha256,
        profile.expected_abstention_reason if profile is not None else None,
        result.analyzer_result.abstention_reason or None,
        unsupported_mass,
    )
    if evaluation.inference_confidence_level is not None and (
        requested_confidence_level is None
        or not _close(evaluation.inference_confidence_level, requested_confidence_level)
    ):
        raise ThetaACalibrationError("Evaluator confidence level differs from the requested focal calibration level")
    record.validate()
    return record


@dataclass(frozen=True)
class ThetaAMetricSummary:
    metric: str
    mean: float | None
    mcse: float | None
    target_mcse: float | None
    precision_status: str
    outer_world_contributions: tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class ThetaACalibrationSummary:
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_worlds_m: int
    assignment_replicates_r: int
    metrics: tuple[ThetaAMetricSummary, ...]
    type_i_error_status: str = "NOT_DEFINED_NO_TEST_PROCEDURE"
    power_status: str = "NOT_DEFINED_NO_TEST_PROCEDURE"


def summarize_theta_a_calibration(
    design: ThetaACalibrationDesign,
    assignments: Iterable[ThetaASeedAssignment],
    records: Iterable[ThetaAReplicateRecord],
    *,
    bank: Bank,
) -> tuple[ThetaACalibrationSummary, ...]:
    """Summarize R within each fixed world, then aggregate independent M worlds.

    A metric is NOT_EVALUABLE if any expected M/R contribution is missing or
    if the Analyzer abstains where a numeric identified-only metric is required.
    This prevents silent complete-case denominators. Type-I error/power remain
    unavailable until a separate hypothesis-test procedure is specified.
    """
    design.validate()
    seed_rows, result_rows = tuple(assignments), tuple(records)
    if bank not in ("calibration", "evaluation") or any(x.bank != bank for x in seed_rows):
        raise ThetaACalibrationError("summary bank label does not match seed assignments")
    validate_theta_a_seed_banks(
        seed_rows if bank == "calibration" else (),
        seed_rows if bank == "evaluation" else (),
        design=design,
    )
    assignment_map = {
        (x.scenario_id, x.scenario_version, x.n_units, x.outer_world_id, x.assignment_replicate): x
        for x in seed_rows
    }
    record_map = {
        (x.scenario_id, x.scenario_version, x.n_units, x.outer_world_id, x.assignment_replicate): x
        for x in result_rows
    }
    if len(record_map) != len(result_rows) or set(record_map) != set(assignment_map):
        raise ThetaACalibrationError("replicate records must match the complete N×M×R seed plan exactly")
    scenario_map = {(x.scenario_id, x.scenario_version): x for x in design.scenario_specs}
    for key, record in record_map.items():
        record.validate()
        seed = assignment_map[key]
        scenario = scenario_map[(record.scenario_id, record.scenario_version)]
        if record.expected_identification != scenario.expected_identification:
            raise ThetaACalibrationError("replicate truth-class label differs from its scenario contract")
        if record.dgp_profile_sha256 != scenario.dgp_profile_sha256 or seed.dgp_profile_sha256 != scenario.dgp_profile_sha256:
            raise ThetaACalibrationError("replicate/seed DGP profile fingerprint differs from its scenario contract")
        expected_reason = scenario.dgp_profile.expected_abstention_reason if scenario.dgp_profile else None
        expected_mass = sum(mass for _, mass in scenario.dgp_profile.target_unsupported_history_masses) if scenario.dgp_profile else 0.0
        if record.expected_abstention_reason != expected_reason or not _close(record.target_unsupported_mass, expected_mass):
            raise ThetaACalibrationError("replicate expected abstention cause or unsupported target mass differs from its DGP profile")
        if (record.world_id, record.run_id) != (seed.world_id, seed.run_id):
            raise ThetaACalibrationError("replicate evidence provenance differs from its seed assignment")
        expected_level = (
            design.confidence_level if scenario.unit_independence_certified else None
        )
        if record.requested_confidence_level != expected_level:
            raise ThetaACalibrationError("replicate requested confidence level differs from its scenario/design contract")

    target_map = {(sid, ver, n, metric): target
                  for sid, ver, n, metric, target in design.metric_targets}
    summaries = []
    for scenario in design.scenario_specs:
        for n_units in design.n_grid:
            scenario_records = [
                row for row in result_rows
                if row.scenario_id == scenario.scenario_id
                and row.scenario_version == scenario.scenario_version
                and row.n_units == n_units
            ]
            estimand_versions = {
                (row.estimand_id, row.estimand_version, row.outcome_id, row.outcome_version)
                for row in scenario_records
            }
            if len(estimand_versions) != 1:
                raise ThetaACalibrationError("estimand/outcome identity and versions must remain fixed across all M worlds")
            by_m = {}
            for m in range(design.outer_worlds_m):
                outer_id = f"outer-{m:06d}"
                group = [
                    record_map[(scenario.scenario_id, scenario.scenario_version,
                                n_units, outer_id, r)]
                    for r in range(design.assignment_replicates_r)
                ]
                if len({x.world_id for x in group}) != 1:
                    raise ThetaACalibrationError("R replicates within one M do not share one world")
                for field in (
                    "world_configuration_sha256", "policy_design_sha256",
                    "estimand_id", "estimand_version", "outcome_id", "outcome_version",
                ):
                    if len({getattr(x, field) for x in group}) != 1:
                        raise ThetaACalibrationError(f"R replicates within one M changed {field}")
                for field in ("assignment_randomization_sha256", "evidence_sha256", "analyzer_output_sha256"):
                    if len({getattr(x, field) for x in group}) != len(group):
                        raise ThetaACalibrationError(f"R replicates within one M must have distinct {field}")
                truths = [x.truth for x in group]
                if any(not _close(value, truths[0]) for value in truths[1:]):
                    raise ThetaACalibrationError("theta_A truth must remain fixed across R within each M")
                by_m[outer_id] = group

            metric_values: dict[str, list[tuple[str, float] | None]] = {}
            for outer_id, group in by_m.items():
                r_count = len(group)
                identified = [x.analyzer_identification == "IDENTIFIED" for x in group]
                metric_values.setdefault("identification_rate", []).append((outer_id, sum(identified) / r_count))
                metric_values.setdefault("abstention_rate", []).append((outer_id, 1.0 - sum(identified) / r_count))
                metric_values.setdefault("interval_availability_rate", []).append(
                    (outer_id, sum(x.inference_covered is not None for x in group) / r_count)
                )
                if scenario.expected_identification == "IDENTIFIED":
                    false_abstention = sum(not value for value in identified) / r_count
                    metric_values.setdefault("false_abstention_rate", []).append((outer_id, false_abstention))
                    if all(identified):
                        errors = [x.point_estimate - x.truth for x in group]
                        metric_values.setdefault("point_bias", []).append((outer_id, mean(errors)))
                        metric_values.setdefault("point_mae", []).append((outer_id, mean(abs(x) for x in errors)))
                        metric_values.setdefault("point_rmse_mse", []).append((outer_id, mean(x*x for x in errors)))
                        if design.point_recovery_tolerance is not None:
                            metric_values.setdefault("point_recovery_rate", []).append((
                                outer_id,
                                sum(abs(x) <= design.point_recovery_tolerance for x in errors) / r_count,
                            ))
                    else:
                        for name in ("point_bias", "point_mae", "point_rmse_mse"):
                            metric_values.setdefault(name, []).append(None)
                        if design.point_recovery_tolerance is not None:
                            metric_values.setdefault("point_recovery_rate", []).append(None)
                    if all(x.inference_covered is not None and x.inference_width is not None for x in group):
                        metric_values.setdefault("interval_coverage", []).append(
                            (outer_id, sum(bool(x.inference_covered) for x in group) / r_count)
                        )
                        metric_values.setdefault("interval_width", []).append(
                            (outer_id, mean(float(x.inference_width) for x in group))
                        )
                    else:
                        metric_values.setdefault("interval_coverage", []).append(None)
                        metric_values.setdefault("interval_width", []).append(None)
                else:
                    expected_status = scenario.expected_identification
                    expected_reason = scenario.dgp_profile.expected_abstention_reason if scenario.dgp_profile else None
                    correct = [
                        x.analyzer_identification == "NOT_IDENTIFIED"
                        and x.observed_abstention_reason == expected_reason
                        for x in group
                    ]
                    wrong_cause = [
                        x.analyzer_identification in ("NOT_IDENTIFIED", "INDETERMINATE")
                        and not (x.analyzer_identification == "NOT_IDENTIFIED"
                                 and x.observed_abstention_reason == expected_reason)
                        for x in group
                    ]
                    partial = [x.analyzer_identification == "PARTIALLY_IDENTIFIED" for x in group]
                    metric_values.setdefault("correct_abstention_rate", []).append(
                        (outer_id, sum(correct) / r_count)
                    )
                    metric_values.setdefault("wrong_cause_abstention_rate", []).append(
                        (outer_id, sum(wrong_cause) / r_count)
                    )
                    metric_values.setdefault("partial_identification_rate", []).append(
                        (outer_id, sum(partial) / r_count)
                    )
                    metric_values.setdefault("false_identification_rate", []).append(
                        (outer_id, sum(identified) / r_count)
                    )

            names = sorted(metric_values)
            metric_summaries = []
            for name in names:
                contributions = metric_values[name]
                target_name = "point_rmse" if name == "point_rmse_mse" else name
                target = target_map.get((scenario.scenario_id, scenario.scenario_version, n_units, target_name))
                output_name = "point_rmse" if name == "point_rmse_mse" else name
                if len(contributions) != design.outer_worlds_m or any(x is None for x in contributions):
                    metric_summaries.append(ThetaAMetricSummary(
                        output_name, None, None, target, "NOT_EVALUABLE", tuple()
                    ))
                    continue
                values = tuple((x[0], x[1]) for x in contributions if x is not None)
                xs = [x[1] for x in values]
                if name == "point_rmse_mse":
                    mse = mean(xs)
                    value = sqrt(mse)
                    mcse_mse = stdev(xs) / sqrt(design.outer_worlds_m)
                    mcse = mcse_mse / (2.0 * value) if value > 0 else (0.0 if mcse_mse == 0 else None)
                else:
                    value = mean(xs)
                    mcse = stdev(xs) / sqrt(design.outer_worlds_m)
                    output_name = name
                status = (
                    "NOT_TARGETED" if target is None
                    else "NOT_EVALUABLE" if mcse is None
                    else "PASS_PRECISION" if mcse <= target
                    else "FAIL_PRECISION"
                )
                metric_summaries.append(ThetaAMetricSummary(
                    output_name, value, mcse, target, status, values
                ))
            summaries.append(ThetaACalibrationSummary(
                scenario.scenario_id, scenario.scenario_version, n_units,
                design.outer_worlds_m, design.assignment_replicates_r,
                tuple(metric_summaries),
            ))
    return tuple(summaries)
