"""Focal theta_A calibration design and aggregation.

This protocol is separate from the legacy 13x52 V_cont assignment benchmark.
It defines N units per world, M independent outer worlds, and R repeated
joint-policy assignments within each fixed world. It never executes a
calibration or creates a bank unless its explicit builder is called.
"""
from __future__ import annotations

from dataclasses import dataclass
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


@dataclass(frozen=True)
class ThetaACalibrationScenario:
    scenario_id: str
    scenario_version: str
    expected_identification: Identification
    unit_independence_certified: bool
    independence_basis: str = ""

    def validate(self) -> None:
        if not self.scenario_id.strip() or not self.scenario_version.strip():
            raise ThetaACalibrationError("focal scenario identity/version is required")
        if self.expected_identification not in _VALID_IDENTIFICATION:
            raise ThetaACalibrationError(
                "focal calibration currently supports IDENTIFIED, NOT_IDENTIFIED or INDETERMINATE truth classes"
            )
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
        for scenario_id, version, n_units, metric, target in self.metric_targets:
            if (scenario_id, version) not in scenario_keys or n_units not in self.n_grid:
                raise ThetaACalibrationError("metric target references an undeclared scenario/version/N")
            if not metric.strip() or isinstance(target, bool) or not isfinite(target) or target <= 0:
                raise ThetaACalibrationError("metric targets require a name and finite positive MCSE")
            target_keys.append((scenario_id, version, n_units, metric))
        if len(target_keys) != len(set(target_keys)):
            raise ThetaACalibrationError("duplicate focal metric target")


@dataclass(frozen=True)
class ThetaASeedAssignment:
    bank: Bank
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_world_id: str
    assignment_replicate: int
    world_id: str
    run_id: str
    world_seed: int
    randomization_salt: str
    s3_seed: int


def _digest(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _seed(payload: str) -> int:
    return int.from_bytes(hashlib.sha256(payload.encode("utf-8")).digest()[:8], "big")


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
                    f"{scenario.scenario_id}|{scenario.scenario_version}|{n_units}|{outer_id}"
                )
                world_seed = _seed(root + "|world")
                world_id = "theta-a-world-" + _digest(root + "|world-id")[:24]
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
                        run_id="theta-a-run-" + _digest(run_root + "|run-id")[:24],
                        world_seed=world_seed,
                        randomization_salt=_digest(run_root + "|joint-policy-randomization"),
                        s3_seed=_seed(run_root + "|s3-measurement"),
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
            not x.world_id or not x.run_id or not x.randomization_salt
            or x.n_units < 1 or x.assignment_replicate < 0
            for x in rows
        ):
            raise ThetaACalibrationError("focal seed row has missing identity or invalid N/R")
        worlds = {}
        for row in rows:
            key = (row.scenario_id, row.scenario_version, row.n_units, row.outer_world_id)
            prior = worlds.setdefault(key, (row.world_id, row.world_seed))
            if prior != (row.world_id, row.world_seed):
                raise ThetaACalibrationError("world identity/seed must remain fixed across R within each M")
        by_design = {}
        for key, (world_id, world_seed) in worlds.items():
            by_design.setdefault(key[:3], []).append((world_id, world_seed))
        for values in by_design.values():
            ids, seeds = zip(*values)
            if len(set(ids)) != len(ids) or len(set(seeds)) != len(seeds):
                raise ThetaACalibrationError("independent outer worlds M require distinct identities and seeds")
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
        if len(assignment_keys) != len(expected):
            raise ThetaACalibrationError("focal seed bank row cardinality mismatch")

    validate_one(cal, "calibration") if cal else None
    validate_one(ev, "evaluation") if ev else None
    def streams(rows):
        return {
            "world": {x.world_seed for x in rows},
            "assignment": {x.randomization_salt for x in rows},
            "s3": {x.s3_seed for x in rows},
            "run": {x.run_id for x in rows},
        }
    left, right = streams(cal), streams(ev)
    if any(left[key] & right[key] for key in left):
        raise ThetaACalibrationError("calibration and evaluation banks must be disjoint across every focal stream")


def s3_seeds_by_unit(seed: int, unit_ids: Sequence[str]) -> dict[str, int]:
    """Expand one R-specific S3 seed into deterministic unit-specific monitor seeds."""
    if not unit_ids or any(not isinstance(x, str) or not x for x in unit_ids):
        raise ThetaACalibrationError("S3 seed expansion requires nonempty unit IDs")
    if len(unit_ids) != len(set(unit_ids)):
        raise ThetaACalibrationError("S3 seed expansion received duplicate unit IDs")
    return {unit_id: _seed(f"TGCV-C10S-THETA-A-S3-UNIT-v1|{seed}|{unit_id}")
            for unit_id in unit_ids}


@dataclass(frozen=True)
class ThetaAReplicateRecord:
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_world_id: str
    assignment_replicate: int
    world_id: str
    run_id: str
    expected_identification: Identification
    analyzer_identification: Identification
    truth: float
    point_estimate: float | None
    inference_lower_bound: float | None
    inference_upper_bound: float | None
    inference_covered: bool | None
    inference_width: float | None
    confidence_level: float | None

    def validate(self) -> None:
        if not all((self.scenario_id, self.scenario_version, self.outer_world_id,
                    self.world_id, self.run_id)):
            raise ThetaACalibrationError("replicate record identities are mandatory")
        if self.n_units < 1 or self.assignment_replicate < 0:
            raise ThetaACalibrationError("replicate record N/R identity is invalid")
        if self.expected_identification not in _VALID_IDENTIFICATION or self.analyzer_identification not in _VALID_IDENTIFICATION:
            raise ThetaACalibrationError("unsupported identification status in replicate record")
        if not isfinite(self.truth) or not -1.0 <= self.truth <= 1.0:
            raise ThetaACalibrationError("theta_A truth must be finite and in [-1,1]")
        if self.analyzer_identification == "IDENTIFIED":
            if self.point_estimate is None or not isfinite(self.point_estimate):
                raise ThetaACalibrationError("identified replicate requires a finite point estimate")
        elif self.point_estimate is not None:
            raise ThetaACalibrationError("abstaining replicate cannot contain a point estimate")
        interval = (self.inference_lower_bound, self.inference_upper_bound)
        if (interval[0] is None) != (interval[1] is None):
            raise ThetaACalibrationError("inferential interval bounds must be jointly present or absent")
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
                    or self.confidence_level is None
                    or not isfinite(self.confidence_level)
                    or not 0.0 < self.confidence_level < 1.0
                    or self.inference_covered != (interval[0] <= self.truth <= interval[1])):
                raise ThetaACalibrationError("inferential interval evidence is inconsistent")
        elif self.confidence_level is not None:
            raise ThetaACalibrationError("confidence level cannot be recorded when no interval was emitted")


def _close(a: float, b: float) -> bool:
    return abs(a - b) <= 1e-12


def capture_theta_a_replicate(
    result,
    assignment: ThetaASeedAssignment,
    scenario: ThetaACalibrationScenario,
) -> ThetaAReplicateRecord:
    """Capture evaluator-side metrics from one completed world without rerunning it."""
    scenario.validate()
    if (result.world.world_id != assignment.world_id
            or len(result.world.units) != assignment.n_units
            or result.analyzer_result.run_id != assignment.run_id
            or result.evaluator_result.run_id != assignment.run_id):
        raise ThetaACalibrationError("complete-world result does not match its focal M/R seed assignment")
    if (scenario.scenario_id, scenario.scenario_version) != (
        assignment.scenario_id, assignment.scenario_version
    ):
        raise ThetaACalibrationError("scenario contract differs from focal seed assignment")
    evaluation = result.evaluator_result
    record = ThetaAReplicateRecord(
        assignment.scenario_id, assignment.scenario_version, assignment.n_units,
        assignment.outer_world_id, assignment.assignment_replicate,
        assignment.world_id, assignment.run_id, scenario.expected_identification,
        result.analyzer_result.identification,
        result.theta_a_truth.theta_a_truth.theta_a_truth,
        result.analyzer_result.point_estimate,
        result.analyzer_result.inference_lower_bound,
        result.analyzer_result.inference_upper_bound,
        evaluation.inference_truth_covered,
        evaluation.inference_interval_width,
        evaluation.inference_confidence_level,
    )
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
        if (record.world_id, record.run_id) != (seed.world_id, seed.run_id):
            raise ThetaACalibrationError("replicate evidence provenance differs from its seed assignment")
        if record.inference_lower_bound is not None and not _close(
            record.confidence_level, design.confidence_level
        ):
            raise ThetaACalibrationError("replicate confidence level differs from the calibration design")

    target_map = {(sid, ver, n, metric): target
                  for sid, ver, n, metric, target in design.metric_targets}
    summaries = []
    for scenario in design.scenario_specs:
        for n_units in design.n_grid:
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
                    metric_values.setdefault("correct_abstention_rate", []).append((
                        outer_id,
                        sum(x.analyzer_identification == expected_status for x in group) / r_count,
                    ))
                    metric_values.setdefault("false_identification_rate", []).append(
                        (outer_id, sum(identified) / r_count)
                    )

            names = sorted(metric_values)
            metric_summaries = []
            for name in names:
                contributions = metric_values[name]
                target_name = "point_rmse" if name == "point_rmse_mse" else name
                target = target_map.get((scenario.scenario_id, scenario.scenario_version, n_units, target_name))
                if len(contributions) != design.outer_worlds_m or any(x is None for x in contributions):
                    metric_summaries.append(ThetaAMetricSummary(
                        name, None, None, target, "NOT_EVALUABLE", tuple()
                    ))
                    continue
                values = tuple((x[0], x[1]) for x in contributions if x is not None)
                xs = [x[1] for x in values]
                if name == "point_rmse_mse":
                    mse = mean(xs)
                    value = sqrt(mse)
                    mcse_mse = stdev(xs) / sqrt(design.outer_worlds_m)
                    mcse = mcse_mse / (2.0 * value) if value > 0 else (0.0 if mcse_mse == 0 else None)
                    output_name = "point_rmse"
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
