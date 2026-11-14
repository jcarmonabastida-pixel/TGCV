"""C10-S V_cont immutable evidence capture and M-level producer boundary.

RunEvidenceBundle/OuterWorldEvidenceBundle snapshot source objects without
reconstructing them. Importing this module performs no generation or evaluation.
The explicit produce_and_capture_outer_world() API invokes Generator, Sealer,
Analyzer and Evaluator for one M group; produce_and_capture_benchmark() coordinates
all declared scenario/M groups and invokes the existing benchmark evaluator. These
APIs run only when called with execution authority. Neither API builds or derives
a seed bank.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, fields, is_dataclass, replace
from enum import Enum
import hashlib
import json
import math
from typing import Any, TypeVar

from vcont_benchmark_protocol import (
    MonteCarloBenchmarkDesign, SCENARIO_IDS, SeedAssignment,
    ESTIMAND_SPECS, build_scenario_estimand_matrix, scenario_matrix_fingerprint,
)
from rfc8785 import dumps as _jcs_dumps

from vcont_integrated_harness import (
    AnalysisContract, Analyzer, AnalyzerResult, ContractError, EvaluationReport,
    Evaluator, EvidenceCandidate, Generator, RepeatedAssignmentReport, RunManifest,
    ScenarioConfig, SealedEvidence, Sealer, TruthBundle, contract_for,
)

T = TypeVar("T")


def _type_id(cls: type) -> str:
    return f"{cls.__module__}.{cls.__qualname__}"


_SNAPSHOT_TYPES = (
    SeedAssignment, AnalysisContract, AnalyzerResult, EvaluationReport,
    EvidenceCandidate, RepeatedAssignmentReport, RunManifest, ScenarioConfig,
    SealedEvidence, TruthBundle,
)
_SNAPSHOT_TYPE_BY_ID = {_type_id(item): item for item in _SNAPSHOT_TYPES}


def _encode(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return {
            "$dataclass": _type_id(type(value)),
            "fields": {item.name: _encode(getattr(value, item.name)) for item in fields(value)},
        }
    if isinstance(value, Enum):
        return {"$enum": _type_id(type(value)), "value": _encode(value.value)}
    if isinstance(value, tuple):
        return {"$tuple": [_encode(item) for item in value]}
    if isinstance(value, list):
        return {"$list": [_encode(item) for item in value]}
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ContractError("snapshot mappings require string keys")
        return {"$map": {key: _encode(value[key]) for key in sorted(value)}}
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ContractError("snapshot rejects NaN and infinite floats")
        return value
    raise ContractError(f"unsupported snapshot value type: {type(value).__name__}")


def _decode(value: Any) -> Any:
    if isinstance(value, dict):
        if set(value) == {"$tuple"}:
            return tuple(_decode(item) for item in value["$tuple"])
        if set(value) == {"$list"}:
            return [_decode(item) for item in value["$list"]]
        if set(value) == {"$map"}:
            return {key: _decode(item) for key, item in value["$map"].items()}
        if set(value) == {"$enum", "value"}:
            return _decode(value["value"])
        if set(value) == {"$dataclass", "fields"}:
            type_id = value["$dataclass"]
            snapshot_type = _SNAPSHOT_TYPE_BY_ID.get(type_id)
            if snapshot_type is None:
                raise ContractError(f"unregistered nested snapshot type: {type_id}")
            decoded_fields = {key: _decode(item) for key, item in value["fields"].items()}
            return snapshot_type(**decoded_fields)
        return {key: _decode(item) for key, item in value.items()}
    return value


@dataclass(frozen=True)
class FrozenSnapshot:
    """Canonical, deeply immutable typed payload; bytes are the retained source."""

    type_id: str
    canonical_bytes: bytes
    sha256: str

    @classmethod
    def capture(cls, value: Any) -> "FrozenSnapshot":
        if not is_dataclass(value) or isinstance(value, type):
            raise ContractError("only typed dataclass source objects can be snapshotted")
        encoded = _encode(value)
        payload = json.dumps(encoded, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")
        return cls(_type_id(type(value)), payload, hashlib.sha256(payload).hexdigest())

    def restore(self, expected_type: type[T]) -> T:
        if _type_id(expected_type) != self.type_id:
            raise ContractError("snapshot type identifier mismatch")
        if hashlib.sha256(self.canonical_bytes).hexdigest() != self.sha256:
            raise ContractError("snapshot payload digest mismatch")
        encoded = json.loads(self.canonical_bytes.decode("utf-8"))
        if not isinstance(encoded, dict) or encoded.get("$dataclass") != self.type_id:
            raise ContractError("snapshot envelope/type mismatch")
        values = _decode(encoded["fields"])
        return expected_type(**values)


def _legacy_sealed_digest(evidence: SealedEvidence) -> str:
    # Must remain byte-for-byte compatible with Sealer._hash semantics.
    payload = json.dumps({"manifest": evidence.manifest, "rows": evidence.rows},
                         sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _snapshot_digest(value: Any) -> str:
    payload = json.dumps(_encode(value), sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class MatrixTruthProjection:
    """Only the frozen Gate 166 matrix truth fields; no potential-outcome arrays."""

    run_id: str
    itt_z_run_truth: float | None
    itt_g_z0_truth: float
    itt_z_mechanism_truth: float | None
    itt_z_reference_truth: float | None
    outer_replicate_id: str
    assignment_role: str
    assignment_index: int
    g_reference_regime_id: str
    g_reference_regime_version: str
    g_assignment_mechanism_hash: str
    z_assignment_mechanism_hash: str
    seed: int
    theta_a_truth: float | None


_SNAPSHOT_TYPES = _SNAPSHOT_TYPES + (MatrixTruthProjection,)
_SNAPSHOT_TYPE_BY_ID = {_type_id(item): item for item in _SNAPSHOT_TYPES}


def _matrix_truth_projection(truth: TruthBundle) -> MatrixTruthProjection:
    return MatrixTruthProjection(
        run_id=truth.run_id,
        itt_z_run_truth=truth.itt_z_run_truth,
        itt_g_z0_truth=truth.itt_g_z0_truth,
        itt_z_mechanism_truth=truth.itt_z_mechanism_truth,
        itt_z_reference_truth=truth.itt_z_reference_truth,
        outer_replicate_id=truth.outer_replicate_id,
        assignment_role=truth.assignment_role,
        assignment_index=truth.assignment_index,
        g_reference_regime_id=truth.g_reference_regime_id,
        g_reference_regime_version=truth.g_reference_regime_version,
        g_assignment_mechanism_hash=truth.g_assignment_mechanism_hash,
        z_assignment_mechanism_hash=truth.z_assignment_mechanism_hash,
        seed=truth.seed,
        theta_a_truth=truth.theta_a_truth,
    )


@dataclass(frozen=True)
class RunEvidenceBundle:
    schema_id: str
    schema_version: str
    key: tuple[str, str, int, str, str, int, str]
    bank: str
    assignment: FrozenSnapshot
    scenario_config: FrozenSnapshot
    run_manifest: FrozenSnapshot
    truth_projection: FrozenSnapshot
    evidence_candidate: FrozenSnapshot
    sealed_evidence: FrozenSnapshot
    analysis_contract: FrozenSnapshot
    analyzer_result: FrozenSnapshot
    evaluation_report: FrozenSnapshot
    scenario_config_structural_sha256: str
    analysis_contract_sha256: str
    sealed_evidence_legacy_sha256: str
    validation_status: str

    @classmethod
    def capture(
        cls, *, assignment: SeedAssignment, config: ScenarioConfig,
        run_manifest: RunManifest, truth_bundle: TruthBundle,
        evidence_candidate: EvidenceCandidate, sealed_evidence: SealedEvidence,
        analysis_contract: AnalysisContract, analyzer_result: AnalyzerResult,
        evaluation_report: EvaluationReport,
    ) -> "RunEvidenceBundle":
        config.validate()
        analysis_contract.validate()
        if assignment.bank not in ("calibration", "evaluation"):
            raise ContractError("SeedAssignment bank must be calibration or evaluation")
        role, index = assignment.assignment_role, assignment.assignment_index
        effective_world_seed = config.seed if config.world_seed is None else config.world_seed
        effective_z_seed = config.seed + 100003 if config.z_assignment_seed is None else config.z_assignment_seed
        effective_g_seed = config.seed + 200003 if config.g_assignment_seed is None else config.g_assignment_seed
        expected = (assignment.scenario_id, assignment.scenario_version, assignment.n_units,
                    assignment.outer_replicate_id, role, index)
        actual_config = (config.scenario_id, config.version, config.n_units,
                         config.outer_replicate_id, config.assignment_role, config.assignment_index)
        actual_manifest = (run_manifest.scenario_id, run_manifest.version, run_manifest.n_units,
                           run_manifest.outer_replicate_id, run_manifest.assignment_role,
                           run_manifest.assignment_index)
        if expected != actual_config or expected != actual_manifest:
            raise ContractError("SeedAssignment/ScenarioConfig/RunManifest identity join failed")
        if (assignment.world_seed, assignment.z_assignment_seed, assignment.g_assignment_seed) != (
            effective_world_seed, effective_z_seed, effective_g_seed
        ):
            raise ContractError("SeedAssignment seeds do not match effective ScenarioConfig streams")
        if len({assignment.world_seed, assignment.z_assignment_seed, assignment.g_assignment_seed}) != 3:
            raise ContractError("world, Z and G streams must have distinct seeds within an assignment")
        if (run_manifest.world_seed, run_manifest.z_assignment_seed, run_manifest.g_assignment_seed) != (
            assignment.world_seed, assignment.z_assignment_seed, assignment.g_assignment_seed
        ):
            raise ContractError("SeedAssignment seeds do not match RunManifest")
        if run_manifest.replicate_id != config.replicate_id or run_manifest.world_version != config.version:
            raise ContractError("RunManifest replicate/world version does not match ScenarioConfig")
        expected_window_end = config.last_transition_support + config.follow_up
        expected_interval_width = (expected_window_end - config.window_start) / config.n_intervals
        if (run_manifest.n_intervals != config.n_intervals
                or run_manifest.window_start != config.window_start
                or run_manifest.window_end != expected_window_end
                or run_manifest.interval_width != expected_interval_width):
            raise ContractError("RunManifest temporal design does not match ScenarioConfig")
        run_id = run_manifest.run_id
        if not run_id or any(obj.run_id != run_id for obj in (
            truth_bundle, evidence_candidate, sealed_evidence, analyzer_result, evaluation_report
        )):
            raise ContractError("source-object run_id join failed")
        if (truth_bundle.outer_replicate_id, truth_bundle.assignment_role, truth_bundle.assignment_index) != (
            assignment.outer_replicate_id, role, index
        ) or truth_bundle.seed != config.seed:
            raise ContractError("TruthBundle run/M/role/index/seed join failed")
        if (analyzer_result.outer_replicate_id, analyzer_result.assignment_role,
            analyzer_result.assignment_index) != (assignment.outer_replicate_id, role, index):
            raise ContractError("AnalyzerResult M/role/index join failed")
        if (evidence_candidate.provenance or {}) != sealed_evidence.manifest.get("provenance"):
            raise ContractError("EvidenceCandidate/SealedEvidence provenance mismatch")
        if evidence_candidate.rows != sealed_evidence.rows:
            raise ContractError("EvidenceCandidate rows differ from the rows retained by SealedEvidence")
        if sealed_evidence.manifest.get("row_count") != len(sealed_evidence.rows):
            raise ContractError("SealedEvidence manifest row_count does not match retained rows")
        provenance = sealed_evidence.manifest.get("provenance", {})
        expected_provenance = {
            "run_id": run_id, "scenario_id": config.scenario_id,
            "scenario_version": config.version, "world_id": run_manifest.world_id,
            "world_version": run_manifest.world_version, "replicate_id": config.replicate_id,
            "outer_replicate_id": assignment.outer_replicate_id,
            "assignment_role": role, "assignment_index": index,
            "g_assignment_mechanism_id": run_manifest.g_assignment_mechanism_id,
            "g_assignment_mechanism_version": run_manifest.g_assignment_mechanism_version,
            "g_assignment_mechanism_hash": run_manifest.g_assignment_mechanism_hash,
            "z_assignment_mechanism_id": run_manifest.z_assignment_mechanism_id,
            "z_assignment_mechanism_version": run_manifest.z_assignment_mechanism_version,
            "z_assignment_mechanism_hash": run_manifest.z_assignment_mechanism_hash,
            "g_reference_regime_id": run_manifest.g_reference_regime_id,
            "g_reference_regime_version": run_manifest.g_reference_regime_version,
            "z_assignment_vector_hash": run_manifest.z_assignment_vector_hash,
            "g_assignment_vector_hash": run_manifest.g_assignment_vector_hash,
        }
        if any(provenance.get(k) != v for k, v in expected_provenance.items()):
            raise ContractError("SealedEvidence provenance does not match RunManifest/run identity")
        legacy_provenance = hashlib.sha256(json.dumps(
            provenance, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")).hexdigest()
        if sealed_evidence.manifest.get("provenance_sha256") != legacy_provenance:
            raise ContractError("SealedEvidence provenance digest does not recompute")
        legacy_digest = _legacy_sealed_digest(sealed_evidence)
        if legacy_digest != sealed_evidence.sha256 or analyzer_result.input_sha256 != legacy_digest:
            raise ContractError("SealedEvidence digest does not match retained rows or AnalyzerResult input")
        if (analysis_contract.g_assignment_mechanism_id,
            analysis_contract.g_assignment_mechanism_version,
            analysis_contract.g_assignment_mechanism_hash,
            analysis_contract.z_assignment_mechanism_id,
            analysis_contract.z_assignment_mechanism_version,
            analysis_contract.z_assignment_mechanism_hash,
            analysis_contract.reference_regime_id,
            analysis_contract.reference_regime_version) != (
            run_manifest.g_assignment_mechanism_id,
            run_manifest.g_assignment_mechanism_version,
            run_manifest.g_assignment_mechanism_hash,
            run_manifest.z_assignment_mechanism_id,
            run_manifest.z_assignment_mechanism_version,
            run_manifest.z_assignment_mechanism_hash,
            run_manifest.g_reference_regime_id,
            run_manifest.g_reference_regime_version):
            raise ContractError("AnalysisContract does not match RunManifest mechanism/regime identity")
        if (truth_bundle.g_assignment_mechanism_hash, truth_bundle.z_assignment_mechanism_hash,
            truth_bundle.g_reference_regime_id, truth_bundle.g_reference_regime_version) != (
            run_manifest.g_assignment_mechanism_hash, run_manifest.z_assignment_mechanism_hash,
            run_manifest.g_reference_regime_id, run_manifest.g_reference_regime_version):
            raise ContractError("TruthBundle mechanism/reference-regime source binding mismatch")
        if (analysis_contract.estimand_id, analysis_contract.estimand_version) != (
            analyzer_result.estimand_id, analyzer_result.estimand_version
        ):
            raise ContractError("AnalysisContract/AnalyzerResult estimand identity mismatch")
        if (analysis_contract.target_regime_id, analysis_contract.target_regime_version,
            analysis_contract.outcome_id, analysis_contract.outcome_version) != (
            analyzer_result.target_regime_id, analyzer_result.target_regime_version,
            analyzer_result.outcome_id, analyzer_result.outcome_version
        ):
            raise ContractError("AnalysisContract/AnalyzerResult target or outcome mismatch")
        contract_result_fields = (
            "run_conditional_estimand_id", "run_conditional_estimand_version",
            "reference_regime_estimand_id", "reference_regime_estimand_version",
            "g_assignment_estimand_id", "g_assignment_estimand_version",
            "transportability_id", "transportability_version", "transportability_scope",
            "transportability_evidence_status", "transportability_outcome_id", "transportability_basis",
        )
        if any(getattr(analysis_contract, name) != getattr(analyzer_result, name)
               for name in contract_result_fields):
            raise ContractError("AnalysisContract/AnalyzerResult estimand or transportability identity mismatch")
        if (analysis_contract.g_assignment_mechanism_id,
            analysis_contract.g_assignment_mechanism_version,
            analysis_contract.g_assignment_mechanism_hash,
            analysis_contract.z_assignment_mechanism_id,
            analysis_contract.z_assignment_mechanism_version,
            analysis_contract.z_assignment_mechanism_hash,
            analysis_contract.reference_regime_id,
            analysis_contract.reference_regime_version) != (
            analyzer_result.g_assignment_mechanism_id,
            analyzer_result.g_assignment_mechanism_version,
            analyzer_result.g_assignment_mechanism_hash,
            analyzer_result.z_assignment_mechanism_id,
            analyzer_result.z_assignment_mechanism_version,
            analyzer_result.z_assignment_mechanism_hash,
            analyzer_result.reference_regime_id,
            analyzer_result.reference_regime_version):
            raise ContractError("AnalysisContract/AnalyzerResult mechanism or reference-regime mismatch")
        if evaluation_report.run_id != analyzer_result.run_id:
            raise ContractError("EvaluationReport/AnalyzerResult run mismatch")
        if analyzer_result.provenance_sha256 != sealed_evidence.manifest.get("provenance_sha256"):
            raise ContractError("AnalyzerResult provenance digest does not match sealed manifest")

        structural = asdict(config)
        for name in ("seed", "world_seed", "z_assignment_seed", "g_assignment_seed",
                     "replicate_id", "outer_replicate_id", "assignment_role", "assignment_index"):
            structural.pop(name)
        key = (config.scenario_id, config.version, config.n_units,
               assignment.outer_replicate_id, role, index, run_id)
        return cls(
            "TGCV-C10S-VCONT-RUN-EVIDENCE-BUNDLE", "1.0.0", key, assignment.bank,
            FrozenSnapshot.capture(assignment), FrozenSnapshot.capture(config),
            FrozenSnapshot.capture(run_manifest), FrozenSnapshot.capture(_matrix_truth_projection(truth_bundle)),
            FrozenSnapshot.capture(evidence_candidate), FrozenSnapshot.capture(sealed_evidence),
            FrozenSnapshot.capture(analysis_contract), FrozenSnapshot.capture(analyzer_result),
            FrozenSnapshot.capture(evaluation_report), _snapshot_digest(structural),
            _snapshot_digest(analysis_contract), legacy_digest, "STRUCTURALLY_VALID",
        )


@dataclass(frozen=True)
class OuterWorldEvidenceBundle:
    schema_id: str
    schema_version: str
    scenario_id: str
    scenario_version: str
    n_units: int
    outer_replicate_id: str
    world_id: str
    world_version: str
    world_seed: int
    run_bundle: RunEvidenceBundle
    repeated_bundles: tuple[RunEvidenceBundle, ...]
    repeated_assignment_report: FrozenSnapshot

    @classmethod
    def capture(cls, run_bundles: tuple[RunEvidenceBundle, ...],
                repeated_assignment_report: RepeatedAssignmentReport,
                expected_repeated_assignments: int) -> "OuterWorldEvidenceBundle":
        if expected_repeated_assignments < 1:
            raise ContractError("expected repeated-assignment count must be positive")
        if len(run_bundles) != expected_repeated_assignments + 1:
            raise ContractError("outer-world bundle cardinality must be exactly 1 RUN + R")
        assignments = [bundle.assignment.restore(SeedAssignment) for bundle in run_bundles]
        runs = [bundle for bundle, row in zip(run_bundles, assignments) if row.assignment_role == "RUN"]
        repeated = sorted(
            (bundle for bundle, row in zip(run_bundles, assignments)
             if row.assignment_role == "REPEATED_ASSIGNMENT"),
            key=lambda bundle: bundle.assignment.restore(SeedAssignment).assignment_index,
        )
        if len(runs) != 1 or len(repeated) != expected_repeated_assignments:
            raise ContractError("outer-world bundle requires exactly one RUN and R repeated assignments")
        run_bundle = runs[0]
        run_assignment = run_bundle.assignment.restore(SeedAssignment)
        config = run_bundle.scenario_config.restore(ScenarioConfig)
        manifest = run_bundle.run_manifest.restore(RunManifest)
        indices = [bundle.assignment.restore(SeedAssignment).assignment_index for bundle in repeated]
        if indices != list(range(expected_repeated_assignments)):
            raise ContractError("outer-world repeated assignment indices must be exactly 0..R-1")
        all_bundles = (run_bundle,) + tuple(repeated)
        all_assignments = [bundle.assignment.restore(SeedAssignment) for bundle in all_bundles]
        all_manifests = [bundle.run_manifest.restore(RunManifest) for bundle in all_bundles]
        if len({bundle.key[-1] for bundle in all_bundles}) != len(all_bundles):
            raise ContractError("duplicate run_id within outer-world bundle")
        if any((row.bank, row.scenario_id, row.scenario_version, row.n_units,
                row.outer_replicate_id, row.world_seed) !=
               (run_assignment.bank, config.scenario_id, config.version, config.n_units,
                run_assignment.outer_replicate_id, run_assignment.world_seed)
               for row in all_assignments):
            raise ContractError("outer-world SeedAssignment identity/world mismatch")
        if any((item.world_id, item.world_version, item.world_seed) !=
               (manifest.world_id, manifest.world_version, manifest.world_seed)
               for item in all_manifests):
            raise ContractError("RUN/R RunManifest world identity mismatch")
        if len({row.z_assignment_seed for row in all_assignments}) != len(all_assignments) or len(
            {row.g_assignment_seed for row in all_assignments}
        ) != len(all_assignments):
            raise ContractError("assignment-specific Z/G seeds must be unique within M")
        repeated_reports = tuple(bundle.evaluation_report.restore(EvaluationReport) for bundle in repeated)
        if (repeated_assignment_report.world_id != manifest.world_id
                or repeated_assignment_report.replicate_count != expected_repeated_assignments
                or repeated_assignment_report.per_run_reports != repeated_reports):
            raise ContractError("RepeatedAssignmentReport does not match exact ordered R reports")
        return cls(
            "TGCV-C10S-VCONT-OUTER-WORLD-EVIDENCE-BUNDLE", "1.0.0",
            config.scenario_id, config.version, config.n_units, run_assignment.outer_replicate_id,
            manifest.world_id, manifest.world_version, manifest.world_seed,
            run_bundle, tuple(repeated), FrozenSnapshot.capture(repeated_assignment_report),
        )


@dataclass(frozen=True)
class CapturedRun:
    """One produced run plus the unchanged legacy tuple consumed by Evaluator."""
    evidence_bundle: RunEvidenceBundle
    evaluator_tuple: tuple[TruthBundle, AnalyzerResult, AnalysisContract, RunManifest]


@dataclass(frozen=True)
class CapturedOuterWorld:
    """Integrated M boundary: immutable evidence plus legacy aggregation inputs."""
    evidence_bundle: OuterWorldEvidenceBundle
    evaluator_runs: tuple[tuple[TruthBundle, AnalyzerResult, AnalysisContract, RunManifest], ...]


def produce_and_capture_outer_world(
    assignments: tuple[SeedAssignment, ...],
    config_template: ScenarioConfig,
    *,
    expected_repeated_assignments: int,
    tolerance: float,
) -> CapturedOuterWorld:
    """Produce and capture exactly one M while every per-run source object coexists.

    This is the producer/orchestration boundary missing from Gate 167. It consumes
    already-materialized SeedAssignment rows; it never derives seeds or builds a bank.
    The returned evaluator tuples preserve the existing four-object Monte Carlo
    interface, while the parallel immutable OuterWorldEvidenceBundle retains the
    complete Gate 166 source records. Calling this function performs synthetic
    generation/analyzer/evaluation and therefore requires the applicable execution
    authorization; defining/importing it does not execute a benchmark.
    """
    from vcont_benchmark_protocol import SeedAssignment as AssignmentType

    rows = tuple(assignments)
    if not rows or any(not isinstance(row, AssignmentType) for row in rows):
        raise ContractError("outer-world producer requires typed SeedAssignment rows")
    if expected_repeated_assignments < 1 or tolerance < 0:
        raise ContractError("positive R and nonnegative evaluation tolerance required")
    if len(rows) != expected_repeated_assignments + 1:
        raise ContractError("outer-world producer requires exactly one RUN plus R rows")
    run_rows = [row for row in rows if row.assignment_role == "RUN"]
    repeated_rows = sorted(
        (row for row in rows if row.assignment_role == "REPEATED_ASSIGNMENT"),
        key=lambda row: row.assignment_index,
    )
    if len(run_rows) != 1 or len(repeated_rows) != expected_repeated_assignments:
        raise ContractError("outer-world producer requires exactly one RUN and R repeated rows")
    if run_rows[0].assignment_index != -1 or [row.assignment_index for row in repeated_rows] != list(
        range(expected_repeated_assignments)
    ):
        raise ContractError("outer-world producer requires RUN=-1 and contiguous R indices 0..R-1")
    ordered = (run_rows[0],) + tuple(repeated_rows)
    group_identity = {
        (row.bank, row.scenario_id, row.scenario_version, row.n_units,
         row.outer_replicate_id, row.world_seed)
        for row in ordered
    }
    if len(group_identity) != 1:
        raise ContractError("SeedAssignment rows do not belong to one scenario/N/M/world")
    bank, scenario_id, scenario_version, n_units, _, _ = next(iter(group_identity))
    if (scenario_id, scenario_version, n_units) != (
        config_template.scenario_id, config_template.version, config_template.n_units
    ):
        raise ContractError("SeedAssignment group does not match the structural ScenarioConfig template")
    if bank != "evaluation":
        raise ContractError("benchmark producer accepts evaluation-bank assignments only")
    if (len({row.z_assignment_seed for row in ordered}) != len(ordered)
            or len({row.g_assignment_seed for row in ordered}) != len(ordered)):
        raise ContractError("assignment-specific Z/G seeds must be unique within M")

    generator, sealer, analyzer, evaluator = Generator(), Sealer(), Analyzer(), Evaluator()
    captured: list[CapturedRun] = []
    for assignment in ordered:
        config = replace(
            config_template,
            world_seed=assignment.world_seed,
            z_assignment_seed=assignment.z_assignment_seed,
            g_assignment_seed=assignment.g_assignment_seed,
            outer_replicate_id=assignment.outer_replicate_id,
            assignment_role=assignment.assignment_role,
            assignment_index=assignment.assignment_index,
        )
        run_manifest, truth_bundle, evidence_candidate = generator.generate(config)
        sealed_evidence = sealer.seal(evidence_candidate)
        analysis_contract = contract_for(config)
        analyzer_result = analyzer.analyze(sealed_evidence, analysis_contract)
        evaluation_report = evaluator.evaluate(
            truth_bundle, analyzer_result, analysis_contract, tolerance, run_manifest
        )
        run_bundle = RunEvidenceBundle.capture(
            assignment=assignment,
            config=config,
            run_manifest=run_manifest,
            truth_bundle=truth_bundle,
            evidence_candidate=evidence_candidate,
            sealed_evidence=sealed_evidence,
            analysis_contract=analysis_contract,
            analyzer_result=analyzer_result,
            evaluation_report=evaluation_report,
        )
        captured.append(CapturedRun(
            run_bundle,
            (truth_bundle, analyzer_result, analysis_contract, run_manifest),
        ))

    evaluator_runs = tuple(item.evaluator_tuple for item in captured)
    repeated_report = evaluator.evaluate_repeated_assignment(
        list(evaluator_runs[1:]), tolerance
    )
    outer_bundle = OuterWorldEvidenceBundle.capture(
        tuple(item.evidence_bundle for item in captured),
        repeated_report,
        expected_repeated_assignments,
    )
    return CapturedOuterWorld(outer_bundle, evaluator_runs)


# V_cont package v2 capture primitives. These helpers are pure and never invoke
# Generator, Sealer, Analyzer, Evaluator or a producer.
_MATRIX_SCHEMA_ID = "TGCV-C10S-VCONT-MATRIX-CAPTURE"
_MATRIX_SCHEMA_VERSION = "1.0.0"
_MATRIX_DIGEST_ALGORITHM = "TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1"
_REPORT_SCHEMA_ID = "TGCV-C10S-VCONT-REPORT-SNAPSHOT"
_REPORT_SCHEMA_VERSION = "2.0.0"
_REPORT_PAYLOAD_TYPE = "TGCV-C10S-VCONT-BENCHMARK-REPORT"
_REPORT_PAYLOAD_VERSION = "2.0.0"
_REPORT_CANONICALIZATION = "RFC8785-JCS"
# Stable identifier for the unchanged Evaluator _hash implementation:
# json.dumps(sort_keys=True, separators=(",", ":"), allow_nan=False), UTF-8, SHA-256.
_LEGACY_REPORT_FINGERPRINT_ALGORITHM = "TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1"
_UINT64_MAX = (1 << 64) - 1
_SAFE_JCS_INTEGER = (1 << 53) - 1


def _jcs_bytes(value: Any) -> bytes:
    try:
        return _jcs_dumps(value)
    except Exception as exc:
        raise ContractError(f"RFC 8785 canonicalization rejected payload: {exc}") from exc


def _sha256_hex(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _jcs_safe_source(value: Any) -> Any:
    """Project source dataclasses/tuples to JSON data without lossy coercion."""
    if is_dataclass(value) and not isinstance(value, type):
        return _jcs_safe_source(asdict(value))
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ContractError("JCS projection requires string object keys")
        return {key: _jcs_safe_source(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jcs_safe_source(item) for item in value]
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, int):
        if abs(value) > _UINT64_MAX:
            raise ContractError("integer exceeds the declared uint64/JCS source domain")
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ContractError("JCS projection rejects NaN and infinity")
        return value
    raise ContractError(f"unsupported JCS source type: {type(value).__name__}")


def _uint64_wire(value: Any) -> dict[str, str]:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= _UINT64_MAX:
        raise ContractError("registered seed field must be an exact unsigned 64-bit integer")
    return {"$type": "uint64", "decimal": str(value)}


def _legacy_report_fingerprint(manifest_payload: Any) -> str:
    # Exact existing Evaluator sequence: JSON round-trip with default=asdict and
    # sorted keys, followed by the unchanged compact _hash JSON/SHA-256 operation.
    normalized = json.loads(json.dumps(manifest_payload, default=asdict, sort_keys=True))
    payload = json.dumps(
        normalized, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return _sha256_hex(payload)


def _report_v2_projection(report: dict[str, Any]) -> dict[str, Any]:
    expected = {
        "design", "temporal_manifest", "pair_ledger", "manifest",
        "scenario_reports", "coverage", "report_fingerprint",
    }
    if not isinstance(report, dict) or set(report) != expected:
        raise ContractError("Evaluator report top-level schema differs from FrozenReportSnapshot v2.0.0")
    recomputed_legacy_fingerprint = _legacy_report_fingerprint(report["manifest"])
    if report.get("report_fingerprint") != recomputed_legacy_fingerprint:
        raise ContractError("legacy report_fingerprint does not match the frozen source algorithm")
    projected = _jcs_safe_source(report)
    expected_design_fields = {
        "scenario_versions", "n_units", "outer_replicates", "repeated_assignments",
        "matrix_fingerprint", "metric_targets", "seed_bank_label",
        "seed_bank_fingerprint", "executable_commit", "configuration_fingerprint",
    }
    if not isinstance(projected["design"], dict) or set(projected["design"]) != expected_design_fields:
        raise ContractError("Evaluator design projection differs from the declared report schema")
    if not isinstance(projected["report_fingerprint"], str) or len(projected["report_fingerprint"]) != 64:
        raise ContractError("legacy report_fingerprint must be a 64-character digest")
    if not isinstance(projected["manifest"], dict):
        raise ContractError("legacy report manifest must be an object")

    def wrap_temporal(rows):
        if not isinstance(rows, list):
            raise ContractError("temporal manifest must be an array")
        result = []
        for row in rows:
            if not isinstance(row, dict):
                raise ContractError("temporal manifest rows must be objects")
            item = dict(row)
            for field in ("world_seed", "z_assignment_seed", "g_assignment_seed"):
                if field not in item:
                    raise ContractError(f"temporal manifest missing registered uint64 field: {field}")
                item[field] = _uint64_wire(item[field])
            result.append(item)
        return result

    def wrap_pair_ledger(rows):
        if not isinstance(rows, list):
            raise ContractError("pair ledger must be an array")
        result = []
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("contributions"), list):
                raise ContractError("pair ledger row/contributions schema invalid")
            item = dict(row)
            contributions = []
            for contribution in item["contributions"]:
                if not isinstance(contribution, dict) or "world_seed" not in contribution:
                    raise ContractError("pair-ledger contribution missing registered world_seed")
                value = dict(contribution)
                value["world_seed"] = _uint64_wire(value["world_seed"])
                contributions.append(value)
            item["contributions"] = contributions
            result.append(item)
        return result

    projected["temporal_manifest"] = wrap_temporal(projected["temporal_manifest"])
    projected["pair_ledger"] = wrap_pair_ledger(projected["pair_ledger"])
    manifest = projected["manifest"]
    if set(manifest) != {
        "scenario_versions", "N", "M", "R", "matrix_fingerprint",
        "seed_bank_label", "seed_bank_fingerprint", "executable_commit",
        "configuration_fingerprint", "metric_targets", "temporal_manifest",
        "pair_ledger",
    }:
        raise ContractError("legacy manifest payload schema drift requires a report payload version increment")
    manifest["temporal_manifest"] = wrap_temporal(manifest["temporal_manifest"])
    manifest["pair_ledger"] = wrap_pair_ledger(manifest["pair_ledger"])
    if projected["temporal_manifest"] != manifest["temporal_manifest"]:
        raise ContractError("root and nested temporal manifests differ before uint64 projection")
    if projected["pair_ledger"] != manifest["pair_ledger"]:
        raise ContractError("root and nested pair ledgers differ before uint64 projection")
    return projected


def _freeze_nested(value: Any) -> Any:
    if isinstance(value, dict):
        return tuple((key, _freeze_nested(value[key])) for key in sorted(value))
    if isinstance(value, list):
        return tuple(_freeze_nested(item) for item in value)
    return value


def _thaw_nested(value: Any) -> Any:
    if isinstance(value, tuple):
        if all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str) for item in value):
            return {key: _thaw_nested(item) for key, item in value}
        return [_thaw_nested(item) for item in value]
    return value


@dataclass(frozen=True)
class MatrixCapture:
    schema_id: str
    schema_version: str
    design_identity: tuple
    row_count: int
    rows: tuple
    legacy_matrix_fingerprint: str
    full_matrix_digest_algorithm: str
    full_matrix_sha256: str
    canonical_bytes: bytes

    def to_payload(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "design_identity": _thaw_nested(self.design_identity),
            "row_count": self.row_count,
            "rows": [_thaw_nested(row) for row in self.rows],
            "legacy_matrix_fingerprint": self.legacy_matrix_fingerprint,
            "full_matrix_digest_algorithm": self.full_matrix_digest_algorithm,
            "full_matrix_sha256": self.full_matrix_sha256,
        }


@dataclass(frozen=True)
class FrozenReportSnapshot:
    schema_id: str
    schema_version: str
    payload_type: str
    legacy_report_fingerprint: str
    legacy_fingerprint_algorithm: str
    canonical_bytes: bytes
    sha256: str


def _matrix_row(spec: Any) -> dict[str, Any]:
    key = spec.key
    row = {
        "key": {
            "scenario_id": key.scenario_id,
            "scenario_version": key.scenario_version,
            "estimand_id": key.estimand_id,
            "estimand_version": key.estimand_version,
        },
        "evaluation_class": spec.evaluation_class,
        "truth_status": spec.truth_status,
        "dgp_truth_field": spec.dgp_truth_field,
        "analyzer_output_field": spec.analyzer_output_field,
        "aggregation_field": spec.aggregation_field,
        "identification_expectation": spec.identification_expectation,
        "abstention_expectation": spec.abstention_expectation,
        "tolerance_id": spec.tolerance_id,
        "reason": spec.reason,
        "run_evaluation_class": spec.run_evaluation_class,
        "repeated_evaluation_class": spec.repeated_evaluation_class,
    }
    if set(row) != {
        "key", "evaluation_class", "truth_status", "dgp_truth_field",
        "analyzer_output_field", "aggregation_field", "identification_expectation",
        "abstention_expectation", "tolerance_id", "reason",
        "run_evaluation_class", "repeated_evaluation_class",
    }:
        raise ContractError("MatrixCapture row field schema mismatch")
    if not isinstance(row["abstention_expectation"], bool):
        raise ContractError("abstention_expectation must be an exact boolean")
    if row["evaluation_class"] not in ("EVALUABLE", "STATUS_ONLY", "NOT_IDENTIFIABLE", "NOT_EVALUABLE"):
        raise ContractError("unknown MatrixCapture evaluation_class")
    if row["truth_status"] not in ("DEFINED", "UNDEFINED", "NOT_MATERIALIZED"):
        raise ContractError("unknown MatrixCapture truth_status")
    if row["identification_expectation"] not in ("IDENTIFIED", "NOT_IDENTIFIED", "INDETERMINATE"):
        raise ContractError("unknown MatrixCapture identification_expectation")
    for name in ("dgp_truth_field", "reason"):
        if not isinstance(row[name], str) or not row[name]:
            raise ContractError(f"MatrixCapture {name} must be a nonempty string")
    for name in ("analyzer_output_field", "aggregation_field", "tolerance_id",
                 "run_evaluation_class", "repeated_evaluation_class"):
        if row[name] is not None and (not isinstance(row[name], str) or not row[name]):
            raise ContractError(f"MatrixCapture {name} must be a nonempty string or explicit null")
    for name in ("run_evaluation_class", "repeated_evaluation_class"):
        if row[name] not in (None, "EVALUABLE", "STATUS_ONLY", "NOT_IDENTIFIABLE", "NOT_EVALUABLE"):
            raise ContractError(f"MatrixCapture {name} has an unknown EvaluationClass")
    if set(row["key"]) != {"scenario_id", "scenario_version", "estimand_id", "estimand_version"}:
        raise ContractError("MatrixCapture key must contain exactly four identity fields")
    for name, value in row["key"].items():
        if not isinstance(value, str) or not value:
            raise ContractError(f"MatrixCapture key.{name} must be a nonempty string")
    return row


def capture_matrix(specs, design) -> MatrixCapture:
    rows_source = tuple(specs)
    expected_keys = tuple(
        (scenario_id, estimand_id)
        for scenario_id in SCENARIO_IDS
        for estimand_id, *_ in ESTIMAND_SPECS
    )
    observed_keys = tuple((spec.key.scenario_id, spec.key.estimand_id) for spec in rows_source)
    if len(rows_source) != 52 or observed_keys != expected_keys:
        raise ContractError("MatrixCapture requires exactly 52 rows in authoritative positional order")
    versions = dict(design.scenario_versions)
    if tuple(sid for sid, _ in design.scenario_versions) != tuple(SCENARIO_IDS):
        raise ContractError("design scenario_versions must use authoritative SCENARIO_IDS order")
    if any(spec.key.scenario_version != versions[spec.key.scenario_id] for spec in rows_source):
        raise ContractError("MatrixCapture scenario versions differ from design identity")
    legacy = scenario_matrix_fingerprint(rows_source)
    if legacy != design.matrix_fingerprint:
        raise ContractError("historical matrix fingerprint does not match source matrix")
    row_payloads = tuple(_matrix_row(spec) for spec in rows_source)
    design_identity = {
        "scenario_versions": [
            {"scenario_id": sid, "scenario_version": version}
            for sid, version in design.scenario_versions
        ],
        "N": design.n_units,
        "M": design.outer_replicates,
        "R": design.repeated_assignments,
        "legacy_matrix_fingerprint": legacy,
    }
    digest_input = {
        "schema_id": _MATRIX_SCHEMA_ID,
        "schema_version": _MATRIX_SCHEMA_VERSION,
        "row_count": 52,
        "rows": list(row_payloads),
    }
    digest = _sha256_hex(_jcs_bytes(digest_input))
    payload = {
        **digest_input,
        "design_identity": design_identity,
        "legacy_matrix_fingerprint": legacy,
        "full_matrix_digest_algorithm": _MATRIX_DIGEST_ALGORITHM,
        "full_matrix_sha256": digest,
    }
    canonical = _jcs_bytes(payload)
    return MatrixCapture(
        _MATRIX_SCHEMA_ID, _MATRIX_SCHEMA_VERSION, _freeze_nested(design_identity),
        52, tuple(_freeze_nested(row) for row in row_payloads), legacy,
        _MATRIX_DIGEST_ALGORITHM, digest, canonical,
    )


def freeze_report_snapshot(report: dict[str, Any]) -> FrozenReportSnapshot:
    projected_report = _report_v2_projection(report)
    envelope = {
        "schema_id": _REPORT_SCHEMA_ID,
        "schema_version": _REPORT_SCHEMA_VERSION,
        "payload_type": _REPORT_PAYLOAD_TYPE,
        "legacy_report_fingerprint": projected_report["report_fingerprint"],
        "legacy_fingerprint_algorithm": _LEGACY_REPORT_FINGERPRINT_ALGORITHM,
        "report": projected_report,
    }
    canonical = _jcs_bytes(envelope)
    return FrozenReportSnapshot(
        _REPORT_SCHEMA_ID, _REPORT_SCHEMA_VERSION, _REPORT_PAYLOAD_TYPE,
        projected_report["report_fingerprint"], _LEGACY_REPORT_FINGERPRINT_ALGORITHM,
        canonical, _sha256_hex(canonical),
    )


def _design_identity_projection(design: MonteCarloBenchmarkDesign) -> dict[str, Any]:
    return {
        "scenario_versions": [
            {"scenario_id": sid, "scenario_version": version}
            for sid, version in design.scenario_versions
        ],
        "N": design.n_units, "M": design.outer_replicates,
        "R": design.repeated_assignments,
        "matrix_fingerprint": design.matrix_fingerprint,
        "metric_targets": _jcs_safe_source(design.metric_targets),
        "seed_bank_label": design.seed_bank_label,
        "seed_bank_fingerprint": design.seed_bank_fingerprint,
        "executable_commit": design.executable_commit,
        "configuration_fingerprint": design.configuration_fingerprint,
    }


def _assignment_wire(row: SeedAssignment) -> dict[str, Any]:
    return {
        "bank": row.bank, "scenario_id": row.scenario_id,
        "scenario_version": row.scenario_version, "n_units": row.n_units,
        "replicate": row.replicate, "outer_replicate_id": row.outer_replicate_id,
        "assignment_role": row.assignment_role,
        "world_seed": _uint64_wire(row.world_seed),
        "z_assignment_seed": _uint64_wire(row.z_assignment_seed),
        "g_assignment_seed": _uint64_wire(row.g_assignment_seed),
    }


def _outer_bundle_identity(bundle: OuterWorldEvidenceBundle) -> dict[str, Any]:
    run_bundles = (bundle.run_bundle,) + bundle.repeated_bundles
    records = []
    for run in run_bundles:
        records.append({
            "assignment": {"type_id": run.assignment.type_id, "sha256": run.assignment.sha256},
            "scenario_config": {"type_id": run.scenario_config.type_id, "sha256": run.scenario_config.sha256},
            "run_manifest": {"type_id": run.run_manifest.type_id, "sha256": run.run_manifest.sha256},
            "truth_projection": {"type_id": run.truth_projection.type_id, "sha256": run.truth_projection.sha256},
            "evidence_candidate": {"type_id": run.evidence_candidate.type_id, "sha256": run.evidence_candidate.sha256},
            "sealed_evidence": {"type_id": run.sealed_evidence.type_id, "sha256": run.sealed_evidence.sha256},
            "analysis_contract": {"type_id": run.analysis_contract.type_id, "sha256": run.analysis_contract.sha256},
            "analyzer_result": {"type_id": run.analyzer_result.type_id, "sha256": run.analyzer_result.sha256},
            "evaluation_report": {"type_id": run.evaluation_report.type_id, "sha256": run.evaluation_report.sha256},
        })
    projection = {
        "scenario_id": bundle.scenario_id,
        "scenario_version": bundle.scenario_version,
        "n_units": bundle.n_units,
        "outer_replicate_id": bundle.outer_replicate_id,
        "world_id": bundle.world_id,
        "world_version": bundle.world_version,
        "world_seed": _uint64_wire(bundle.world_seed),
        "run_and_repeated_snapshot_records": records,
        "repeated_assignment_report": {
            "type_id": bundle.repeated_assignment_report.type_id,
            "sha256": bundle.repeated_assignment_report.sha256,
        },
    }
    return {"sha256": _sha256_hex(_jcs_bytes(projection)), "projection": projection}


def derive_capture_identity(design_identity, matrix_capture, outer_world_bundles,
                            report_snapshot, evidence_index) -> str:
    if not isinstance(matrix_capture, MatrixCapture) or not isinstance(report_snapshot, FrozenReportSnapshot):
        raise ContractError("capture identity requires MatrixCapture and FrozenReportSnapshot")
    bundles = tuple(outer_world_bundles)
    expected_design_fields = {
        "scenario_versions", "N", "M", "R", "matrix_fingerprint",
        "metric_targets", "seed_bank_label", "seed_bank_fingerprint",
        "executable_commit", "configuration_fingerprint",
    }
    if not isinstance(design_identity, dict) or set(design_identity) != expected_design_fields:
        raise ContractError("capture identity design projection differs from the exact declared design schema")
    scenario_versions = design_identity["scenario_versions"]
    if (not isinstance(scenario_versions, (tuple, list))
            or any(not isinstance(item, (tuple, list)) or len(item) != 2
                   or not isinstance(item[0], str) or not isinstance(item[1], str) or not item[1]
                   for item in scenario_versions)
            or tuple(item[0] for item in scenario_versions) != tuple(SCENARIO_IDS)):
        raise ContractError("capture identity scenario/version projection is not in authoritative order")
    for name, minimum in (("N", 1), ("M", 2), ("R", 1)):
        value = design_identity[name]
        if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
            raise ContractError(f"capture identity design {name} is outside its declared integer domain")
    declared_versions = dict(scenario_versions)
    for bundle in bundles:
        if (bundle.scenario_id not in declared_versions
                or bundle.scenario_version != declared_versions[bundle.scenario_id]
                or bundle.n_units != design_identity["N"]):
            raise ContractError("outer-world bundle scenario/version/N differs from capture design identity")
    ordered_bundles = sorted(
        bundles, key=lambda b: (SCENARIO_IDS.index(b.scenario_id), int(b.outer_replicate_id.split("-")[-1]))
    )
    outer_ids = tuple(sorted(
        {bundle.outer_replicate_id for bundle in ordered_bundles},
        key=lambda value: int(value.split("-")[-1]),
    ))
    expected_keys = {
        (scenario_id, outer_id)
        for scenario_id in SCENARIO_IDS for outer_id in outer_ids
    }
    observed_keys = {(bundle.scenario_id, bundle.outer_replicate_id) for bundle in ordered_bundles}
    expected_m = design_identity.get("M") if isinstance(design_identity, dict) else None
    if (not outer_ids or (expected_m is not None and len(outer_ids) != expected_m)
            or outer_ids != tuple(f"outer-{m:06d}" for m in range(len(outer_ids)))
            or observed_keys != expected_keys or len(observed_keys) != len(ordered_bundles)):
        raise ContractError("capture identity requires exactly one ordered outer bundle per scenario/M")
    assignments = []
    for bundle in ordered_bundles:
        for run in (bundle.run_bundle,) + bundle.repeated_bundles:
            assignments.append(run.assignment.restore(SeedAssignment))
    assignment_digest = _sha256_hex(_jcs_bytes({"rows": [_assignment_wire(row) for row in assignments]}))
    bundle_digests = [_outer_bundle_identity(bundle)["sha256"] for bundle in ordered_bundles]
    evidence_rows = [
        {"scenario_id": sid, "outer_replicate_id": outer_id, "world_id": world_id}
        for sid, outer_id, world_id in evidence_index
    ]
    expected_evidence_rows = [
        {"scenario_id": bundle.scenario_id, "outer_replicate_id": bundle.outer_replicate_id,
         "world_id": bundle.world_id}
        for bundle in ordered_bundles
    ]
    if evidence_rows != expected_evidence_rows:
        raise ContractError("evidence_index order/content differs from ordered captured outer-world bundles")
    identity_payload = {
        "schema_id": "TGCV-C10S-VCONT-BENCHMARK-CAPTURE-IDENTITY",
        "schema_version": "2.0.0",
        "design_identity": _jcs_safe_source(design_identity),
        "matrix_full_sha256": matrix_capture.full_matrix_sha256,
        "evaluation_seed_manifest_sha256": assignment_digest,
        "outer_world_bundle_digests": bundle_digests,
        "report_snapshot_sha256": report_snapshot.sha256,
        "evidence_index": evidence_rows,
    }
    return _sha256_hex(_jcs_bytes(identity_payload))


@dataclass(frozen=True)
class CapturedBenchmark:
    """One benchmark report and its complete scenario/M evidence envelope."""
    report: dict[str, Any]
    outer_world_bundles: tuple[OuterWorldEvidenceBundle, ...]
    evidence_index: tuple[tuple[str, str, str], ...]
    matrix_capture: MatrixCapture | None = None
    report_snapshot: FrozenReportSnapshot | None = None
    capture_id: str | None = None

    @property
    def benchmark_export_id(self) -> str | None:
        return self.capture_id


def produce_and_capture_benchmark(
    design: MonteCarloBenchmarkDesign,
    assignments: tuple[SeedAssignment, ...],
    config_templates: tuple[ScenarioConfig, ...],
    *,
    tolerance: float,
    matrix=None,
) -> CapturedBenchmark:
    """Build the complete 13-scenario evidence envelope without deriving seeds.

    This function is an execution entry point: invocation generates synthetic
    observations and runs the V_cont benchmark. Defining/importing it is inert.
    It accepts a frozen design, already-materialized evaluation SeedAssignment
    rows and one structural ScenarioConfig template per registered scenario.
    """
    from vcont_integrated_harness import Evaluator
    from vcont_benchmark_protocol import validate_monte_carlo_benchmark_design

    if not isinstance(design, MonteCarloBenchmarkDesign):
        raise ContractError("benchmark producer requires a frozen MonteCarloBenchmarkDesign")
    versions = dict(design.scenario_versions)
    if (len(versions) != len(design.scenario_versions)
            or set(versions) != set(SCENARIO_IDS)):
        raise ContractError("design must declare exactly the 13 registered scenario IDs")
    if design.outer_replicates < 2 or design.repeated_assignments < 1:
        raise ContractError("benchmark producer requires M>=2 and R>=1")
    if tolerance < 0:
        raise ContractError("benchmark tolerance must be nonnegative")
    specs = tuple(matrix) if matrix is not None else build_scenario_estimand_matrix(versions)
    validate_monte_carlo_benchmark_design(design, specs)

    templates = tuple(config_templates)
    template_map = {item.scenario_id: item for item in templates}
    if len(template_map) != len(templates) or set(template_map) != set(SCENARIO_IDS):
        raise ContractError("producer requires exactly one unique ScenarioConfig template per registered scenario")
    for scenario_id in SCENARIO_IDS:
        template = template_map[scenario_id]
        template.validate()
        if (template.version, template.n_units) != (versions[scenario_id], design.n_units):
            raise ContractError("ScenarioConfig template version/N differs from frozen benchmark design")

    rows = tuple(assignments)
    expected_count = len(SCENARIO_IDS) * design.outer_replicates * (1 + design.repeated_assignments)
    if len(rows) != expected_count or any(not isinstance(row, SeedAssignment) for row in rows):
        raise ContractError("evaluation assignment bank cardinality/type differs from 13 x M x (1+R)")
    if any(row.bank != "evaluation" for row in rows):
        raise ContractError("benchmark producer rejects calibration or mixed-bank assignments")
    expected_groups = {
        (sid, versions[sid], design.n_units, f"outer-{m:06d}")
        for sid in SCENARIO_IDS for m in range(design.outer_replicates)
    }
    observed_groups = {
        (row.scenario_id, row.scenario_version, row.n_units, row.outer_replicate_id)
        for row in rows
    }
    if observed_groups != expected_groups:
        raise ContractError("evaluation assignments contain missing, extra or mis-keyed scenario/M groups")
    assignment_keys = [
        (row.scenario_id, row.scenario_version, row.n_units, row.outer_replicate_id,
         row.assignment_role, row.assignment_index)
        for row in rows
    ]
    if len(set(assignment_keys)) != expected_count:
        raise ContractError("duplicate scenario/M/role/R assignment identity")
    run_ids_by_group: dict[tuple[str, str, int, str], list[SeedAssignment]] = {}
    for row in rows:
        key = (row.scenario_id, row.scenario_version, row.n_units, row.outer_replicate_id)
        run_ids_by_group.setdefault(key, []).append(row)
    for key, group_rows in run_ids_by_group.items():
        run_rows = [row for row in group_rows if row.assignment_role == "RUN"]
        repeated = sorted(
            (row for row in group_rows if row.assignment_role == "REPEATED_ASSIGNMENT"),
            key=lambda row: row.assignment_index,
        )
        if (len(run_rows) != 1 or run_rows[0].assignment_index != -1
                or len(repeated) != design.repeated_assignments
                or [row.assignment_index for row in repeated] != list(range(design.repeated_assignments))):
            raise ContractError(f"incomplete or malformed RUN/R assignments for group {key}")
        if len({row.world_seed for row in group_rows}) != 1:
            raise ContractError("one world seed must be shared by RUN and R within M")
        if (len({row.z_assignment_seed for row in group_rows}) != len(group_rows)
                or len({row.g_assignment_seed for row in group_rows}) != len(group_rows)):
            raise ContractError("Z/G assignment seeds must be unique within each M group")
    for scenario_id in SCENARIO_IDS:
        scenario_world_seeds = {
            run_ids_by_group[(scenario_id, versions[scenario_id], design.n_units,
                              f"outer-{m:06d}")][0].world_seed
            for m in range(design.outer_replicates)
        }
        if len(scenario_world_seeds) != design.outer_replicates:
            raise ContractError("outer M worlds must have distinct world seeds within each scenario")

    evaluator = Evaluator()
    scenario_outer_runs: dict[str, dict[str, tuple]] = {}
    bundles: list[OuterWorldEvidenceBundle] = []
    evidence_index: list[tuple[str, str, str]] = []
    for scenario_id in SCENARIO_IDS:
        scenario_outer_runs[scenario_id] = {}
        for m in range(design.outer_replicates):
            outer_id = f"outer-{m:06d}"
            key = (scenario_id, versions[scenario_id], design.n_units, outer_id)
            group_rows = tuple(run_ids_by_group[key])
            captured = produce_and_capture_outer_world(
                group_rows, template_map[scenario_id],
                expected_repeated_assignments=design.repeated_assignments,
                tolerance=tolerance,
            )
            outer_bundle = captured.evidence_bundle
            if (outer_bundle.scenario_id, outer_bundle.scenario_version,
                outer_bundle.n_units, outer_bundle.outer_replicate_id) != key:
                raise ContractError("captured OuterWorldEvidenceBundle key differs from requested scenario/M group")
            if len(captured.evaluator_runs) != 1 + design.repeated_assignments:
                raise ContractError("captured legacy evaluator tuple count differs from design")
            by_run_id = {
                bundle.key[-1]: bundle
                for bundle in (outer_bundle.run_bundle,) + outer_bundle.repeated_bundles
            }
            for legacy in captured.evaluator_runs:
                manifest = legacy[3]
                source_bundle = by_run_id.get(manifest.run_id)
                if source_bundle is None:
                    raise ContractError("legacy evaluator tuple has no matching captured evidence bundle")
                if (source_bundle.truth_projection.restore(MatrixTruthProjection) != _matrix_truth_projection(legacy[0])
                        or source_bundle.analyzer_result.restore(type(legacy[1])) != legacy[1]
                        or source_bundle.analysis_contract.restore(type(legacy[2])) != legacy[2]
                        or source_bundle.run_manifest.restore(type(legacy[3])) != legacy[3]):
                    raise ContractError("legacy evaluator tuple differs from its exact captured source objects")
            scenario_outer_runs[scenario_id][outer_id] = captured.evaluator_runs
            bundles.append(outer_bundle)
            evidence_index.append((scenario_id, outer_id, outer_bundle.world_id))

    report = evaluator.evaluate_monte_carlo_benchmark(
        scenario_outer_runs, design, tolerance, matrix=specs
    )
    if (report.get("coverage") != {
        "required_pairs": 52, "observed_pairs": 52, "scenario_count": 13
    } or len(report.get("pair_ledger", ())) != 52):
        raise ContractError("benchmark evaluator did not return the complete 52-pair/13-scenario ledger")
    expected_temporal_rows = expected_count
    temporal_rows = tuple(report.get("temporal_manifest", ()))
    if len(temporal_rows) != expected_temporal_rows:
        raise ContractError("benchmark temporal manifest cardinality differs from captured evidence assignments")
    def temporal_key(row):
        return (
            row["scenario_id"], row["scenario_version"], row["N"],
            row["outer_replicate_id"], row["assignment_role"],
            row["assignment_index"], row["run_id"], row["world_id"],
            row["world_seed"], row["z_assignment_seed"], row["g_assignment_seed"],
        )
    captured_temporal = []
    for outer_bundle in bundles:
        run_bundles = (outer_bundle.run_bundle,) + outer_bundle.repeated_bundles
        for run_bundle in run_bundles:
            manifest = run_bundle.run_manifest.restore(RunManifest)
            captured_temporal.append(temporal_key({
                "scenario_id": manifest.scenario_id,
                "scenario_version": manifest.version,
                "N": manifest.n_units,
                "outer_replicate_id": manifest.outer_replicate_id,
                "assignment_role": manifest.assignment_role,
                "assignment_index": manifest.assignment_index,
                "run_id": manifest.run_id,
                "world_id": manifest.world_id,
                "world_seed": manifest.world_seed,
                "z_assignment_seed": manifest.z_assignment_seed,
                "g_assignment_seed": manifest.g_assignment_seed,
            }))
    observed_temporal = [temporal_key(row) for row in temporal_rows]
    if (len(set(captured_temporal)) != expected_temporal_rows
            or set(captured_temporal) != set(observed_temporal)):
        raise ContractError("benchmark temporal manifest does not join one-to-one with captured RUN/R evidence")
    evidence_worlds = {}
    for outer_bundle in bundles:
        run_manifest = outer_bundle.run_bundle.run_manifest.restore(RunManifest)
        evidence_worlds[(outer_bundle.scenario_id, outer_bundle.outer_replicate_id)] = (
            outer_bundle.world_id, run_manifest.run_id
        )
    for pair in report.get("pair_ledger", ()):
        scenario_id, scenario_version, _, _, level = pair["key"]
        if (level != "MONTE_CARLO" or scenario_version != versions.get(scenario_id)
                or len(pair.get("contributions", ())) != design.outer_replicates):
            raise ContractError("pair ledger contribution count/key does not match declared scenario/M design")
        contribution_ids = set()
        for contribution in pair["contributions"]:
            outer_id = contribution["outer_replicate_id"]
            expected_world, expected_run_id = evidence_worlds.get((scenario_id, outer_id), (None, None))
            if (expected_world is None or contribution["world_id"] != expected_world
                    or contribution["run_id"] != expected_run_id or outer_id in contribution_ids):
                raise ContractError("52-pair contribution does not join uniquely to its captured scenario/M RUN evidence")
            contribution_ids.add(outer_id)
        if contribution_ids != {f"outer-{m:06d}" for m in range(design.outer_replicates)}:
            raise ContractError("pair ledger is missing one or more captured M contributions")
    if len(bundles) != len(SCENARIO_IDS) * design.outer_replicates:
        raise ContractError("benchmark evidence envelope must contain exactly one bundle per scenario/M")
    matrix_capture = capture_matrix(specs, design)
    report_snapshot = freeze_report_snapshot(report)
    design_identity = _design_identity_projection(design)
    capture_id = derive_capture_identity(
        design_identity, matrix_capture, tuple(bundles), report_snapshot, tuple(evidence_index)
    )
    return CapturedBenchmark(
        report, tuple(bundles), tuple(evidence_index),
        matrix_capture, report_snapshot, capture_id,
    )
