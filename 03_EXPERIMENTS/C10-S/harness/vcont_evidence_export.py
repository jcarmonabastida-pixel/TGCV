"""Immutable capture boundary for C10-S V_cont run evidence.

This module snapshots already-produced source objects. It never invokes the
Generator, Sealer, Analyzer, Evaluator, seed-bank builder or benchmark runner.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, fields, is_dataclass
from enum import Enum
import hashlib
import json
import math
from typing import Any, TypeVar

from vcont_benchmark_protocol import SeedAssignment
from vcont_integrated_harness import (
    AnalysisContract, AnalyzerResult, ContractError, EvaluationReport,
    EvidenceCandidate, RepeatedAssignmentReport, RunManifest, ScenarioConfig,
    SealedEvidence, TruthBundle,
)

T = TypeVar("T")


def _type_id(cls: type) -> str:
    return f"{cls.__module__}.{cls.__qualname__}"


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
            return {key: _decode(item) for key, item in value["fields"].items()}
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
        if (run_manifest.world_seed, run_manifest.z_assignment_seed, run_manifest.g_assignment_seed) != (
            assignment.world_seed, assignment.z_assignment_seed, assignment.g_assignment_seed
        ):
            raise ContractError("SeedAssignment seeds do not match RunManifest")
        if run_manifest.replicate_id != config.replicate_id:
            raise ContractError("RunManifest replicate_id does not match ScenarioConfig")
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
