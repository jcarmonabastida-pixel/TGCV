# C10-S V_cont — Gate 170: RunEvidenceBundle capture implementation

**Status:** CAPTURE API IMPLEMENTED; ORCHESTRATOR INTEGRATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Depends on:** Gates 166, 168 and 169  
**Scientific execution:** NOT AUTHORIZED  
**Tests/CI:** NOT EXECUTED

## 1. Scope

Gate 170 implements the immutable typed capture primitives specified by Gate 168. It does not invoke Generator, Sealer, Analyzer, Evaluator, seed-bank builders, benchmark runners, calibration or Monte Carlo operations. It does not change their scientific semantics.

The implementation is a standalone capture API. The existing benchmark input path still receives reduced tuples and no integrated producer/orchestration call site has yet been changed to call this API. Therefore Gate 170 does **not** claim end-to-end evidence export integration.

## 2. Implemented source

New module:

`03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`

It provides:

- `FrozenSnapshot`: canonical immutable bytes, explicit dataclass type identity and SHA-256; rejects unsupported types, non-string mapping keys, NaN and infinities; restores only when the requested type identifier matches and the byte digest recomputes.
- `RunEvidenceBundle.capture(...)`: captures exact SeedAssignment, full ScenarioConfig, complete RunManifest, EvidenceCandidate, complete SealedEvidence, AnalysisContract, AnalyzerResult and EvaluationReport.
- `MatrixTruthProjection`: stores only the Gate 166 matrix truth fields, including explicit `theta_a_truth`, and excludes potential-outcome arrays.
- `OuterWorldEvidenceBundle.capture(...)`: requires exactly one RUN and R repeated assignments, exact 0..R-1 indices, shared M/world identity, common bank/design identity, unique run IDs, distinct assignment Z/G seeds, and an exact ordered RepeatedAssignmentReport.

The bundle itself contains only immutable scalar fields, tuples, nested frozen snapshots and bytes. The source dataclasses may contain mutable nested dictionaries/lists; capture serializes their values immediately so later source mutation cannot mutate the captured payload.

## 3. Validation implemented at capture

The per-run capture validates:

1. SeedAssignment ↔ ScenarioConfig ↔ RunManifest scenario/version/N/M/role/index.
2. Effective world/Z/G seeds, including ScenarioConfig fallback semantics.
3. RunManifest temporal design and legacy replicate identity against ScenarioConfig.
4. Run ID equality across RunManifest, TruthBundle, EvidenceCandidate, SealedEvidence, AnalyzerResult and EvaluationReport.
5. TruthBundle M/role/index and base-seed binding.
6. EvidenceCandidate rows/provenance equality with the retained SealedEvidence.
7. SealedEvidence row count and complete provenance equality with RunManifest.
8. SealedEvidence provenance digest using the exact legacy Sealer JSON digest.
9. SealedEvidence full manifest+rows legacy digest, independently recomputed, and exact equality with AnalyzerResult.input_sha256.
10. AnalysisContract ↔ RunManifest mechanism/reference-regime identity.
11. AnalysisContract ↔ AnalyzerResult estimand, target-regime, outcome, mechanism and reference-regime identities.
12. AnalyzerResult provenance digest ↔ SealedEvidence manifest.
13. EvaluationReport ↔ AnalyzerResult run identity.

The ScenarioConfig structural projection follows Gate 166's closed exclusion list. A separate full per-run ScenarioConfig snapshot is retained. AnalysisContract receives a content-derived SHA-256 reference.

## 4. Truth retention correction

The full TruthBundle is supplied to capture for source validation, but the export stores a `MatrixTruthProjection` only. This follows Gate 166 §4.5 and avoids exporting full potential-outcome arrays in v1.0.0. `theta_a_truth` remains explicit null/value and is not made scoreable.

## 5. Regression source

A regression was added to:

`03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`

It creates one designated RUN from a deterministic fixture, captures a bundle, mutates the original EvidenceCandidate row after capture, and checks that the stored snapshot remains unchanged. It also checks the retained SealedEvidence digest and verifies that the matrix truth projection does not expose `potential_v`.

The test source has been statically inspected and persisted. **It has not been executed.** No test PASS, syntax-check result, CI run or runtime behavior is claimed.

## 6. Limitations and unresolved work

- The existing benchmark producer/orchestration path does not yet call `RunEvidenceBundle.capture`; it still hands reduced four-object tuples to the Monte Carlo evaluator.
- No orchestration-level object currently retains SeedAssignment and all per-run source objects together through capture. The capture API accepts them explicitly, but its integration point must be wired in a subsequent gate.
- The OuterWorldEvidenceBundle primitive is implemented but not yet wired to the existing repeated-assignment aggregation producer.
- No full benchmark export envelope, calibration-bank manifest, Gate 159 reconciliation, JCS package writer, tar packager, trusted builder or attestor is implemented by this gate.
- Structural validation does not establish external provenance or AUTHENTICATED status.
- The capture API is a local structural check, not an independent causal or scientific validation.

## 7. Disposition

- RunEvidenceBundle data carrier: IMPLEMENTED.
- Deep-immutable typed snapshots: IMPLEMENTED IN SOURCE.
- Gate 166 matrix truth projection: IMPLEMENTED.
- Inline SealedEvidence rows+manifest and legacy digest recomputation: IMPLEMENTED IN SOURCE.
- Per-run identity/provenance/contract joins: IMPLEMENTED IN SOURCE.
- OuterWorldEvidenceBundle data carrier and cardinality checks: IMPLEMENTED IN SOURCE.
- Regression source: ADDED / NOT EXECUTED.
- Orchestration integration: OPEN.
- Benchmark aggregation integration: OPEN.
- Gate 159 reconciliation: OPEN.
- Package/attestation: OPEN.
- Calibration, seed-bank generation, N/R/M sizing, Monte Carlo, benchmark and scientific execution: NOT AUTHORIZED / NOT PERFORMED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 8. Next operation — Gate 171

Integrate the capture API into a single explicit producer/orchestration boundary that has the exact SeedAssignment row and retains the complete per-run source objects through Evaluator.evaluate. Then adapt the M-level assembly to construct one OuterWorldEvidenceBundle per M without reconstructing source objects from reduced evaluator tuples. Preserve the existing evaluator outputs and the 52-pair ledger semantics. Add adversarial tests for failed joins, tampering, duplicate/missing R indices, cross-M mixing and source mutation. Do not execute tests without the applicable technical execution authorization.


## 9. Gate 171 supersession — M-level producer boundary added

Gate 171 adds `produce_and_capture_outer_world(...)` in the same source module. It invokes Generator → Sealer → Analyzer → Evaluator, captures each `RunEvidenceBundle` while the source objects coexist, computes one existing `RepeatedAssignmentReport`, and constructs one `OuterWorldEvidenceBundle` per supplied scenario/N/M group. It also returns the unchanged legacy four-object tuples for the existing Monte Carlo aggregation interface.

The Gate 170 statement that no integrated producer/orchestration call site existed is therefore superseded at the **single-M boundary**. Gate 170's original scope remains accurate: it implemented the capture primitives but did not itself wire them into a producer.

The benchmark-wide 13-scenario caller remains OPEN; no current caller yet loops all scenarios/M and combines the returned evidence bundles with the 52-pair benchmark report. See Gate 171 for the exact boundary, source and regression scope. The new regression tests are NOT EXECUTED.
