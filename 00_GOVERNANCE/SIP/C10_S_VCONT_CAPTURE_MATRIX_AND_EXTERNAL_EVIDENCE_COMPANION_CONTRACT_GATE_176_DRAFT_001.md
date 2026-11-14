# C10-S V_cont — Gate 176: capture-time matrix and external evidence companion contract

**Status:** CONTRACT DEFINED — SOURCE IMPLEMENTATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 175 static implementability audit  
**Scope:** close the exact-matrix retention and companion-evidence source contracts; no serializer implementation  
**Execution:** no imports, compilation, tests, CI, seed generation, calibration, package generation, benchmark or scientific execution

## 1. Decision summary

Gate 176 resolves the source-boundary design without changing Generator, Sealer, Analyzer, Evaluator, estimands, DGP semantics or the N/R/M hierarchy.

Four decisions are frozen:

1. The exact ordered 52-row `ScenarioEstimandSpec` matrix validated and passed to `evaluate_monte_carlo_benchmark()` is captured at that same invocation boundary in a dedicated immutable `MatrixCapture`. It is not rebuilt later from current code and is not inferred from the pair ledger.
2. The legacy `scenario_matrix_fingerprint()` remains unchanged for compatibility. A second versioned full-matrix SHA-256 commits to every declared matrix field, including `tolerance_id`, and every nested `EvaluationKey` field.
3. Calibration, Gate 159 reconciliation, GitHub source-execution provenance and technical-test evidence are separate immutable companion artifacts. They are joined to the benchmark export identity, not injected into the evaluation-bank producer or synthesized from its report.
4. The current `CapturedBenchmark.report` is a mutable dict despite the frozen outer dataclass. The compatibility report may remain available to existing consumers, but an exact immutable report snapshot/digest must be captured alongside it and be authoritative for package export.

## 2. MatrixCapture v1.0.0

Schema ID: `TGCV-C10S-VCONT-MATRIX-CAPTURE`; version `1.0.0`.

The benchmark producer must capture the exact `specs` tuple immediately after `validate_monte_carlo_benchmark_design(design, specs)` and before passing it to the evaluator. The same tuple object/value sequence is passed to the evaluator and committed to the capture. No second call to `build_scenario_estimand_matrix()` is allowed to stand in for capture-time evidence.

Logical fields:

- `schema_id`, `schema_version`;
- `benchmark_export_id` and `capture_id`, deterministically bound to the frozen design identity and capture envelope (no wall-clock/random identity);
- `design_identity`: scenario/version map, N, M, R and legacy matrix fingerprint;
- `row_count = 52`;
- `rows`: exactly 52 complete typed rows in canonical order, each with:
  - nested key: `scenario_id`, `scenario_version`, `estimand_id`, `estimand_version`;
  - `evaluation_class`, `truth_status`, `dgp_truth_field`;
  - `analyzer_output_field`, `aggregation_field`;
  - `identification_expectation`, `abstention_expectation`;
  - `tolerance_id`, `reason`;
  - `run_evaluation_class`, `repeated_evaluation_class`;
- `legacy_matrix_fingerprint`;
- `full_matrix_digest_algorithm = TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1`;
- `full_matrix_sha256`.

The 52 rows are ordered by the canonical `SCENARIO_IDS` order, then the canonical four-estimand order in `ESTIMAND_SPECS`. A duplicate key, missing key, additional row, unknown enum-like classification, invalid field type or ordering mismatch rejects capture. No semantic defaults are inserted during export: explicit null remains null.

### 2.1 Full-matrix digest

The digest input is a data-only JSON object with a fixed schema and fixed field names. It contains the schema ID/version and all 52 rows in the canonical order. Each row includes every field listed in §2, including the four nested EvaluationKey members and nullable `tolerance_id`.

Canonicalization is RFC 8785 JCS, UTF-8 bytes, no BOM, no trailing newline for the digest input. The digest is SHA-256 over those exact bytes. This is a new versioned digest; it does not replace or redefine the existing legacy fingerprint.

Validation requires:
1. independently recompute the legacy fingerprint using the unchanged historical algorithm and compare it with the design declaration;
2. independently recompute the full JCS digest from the captured rows and compare it with `full_matrix_sha256`;
3. verify that the rows are the exact matrix values passed to the evaluator, through the capture-time orchestration join (not by comparing only the resulting 52 pair keys).

A change to `tolerance_id`, any key field, any class, truth/output/aggregation field, expectation, reason or row order must change the full digest or fail canonical-order validation.

### 2.2 Compatibility

The `MonteCarloBenchmarkDesign.matrix_fingerprint` field and `scenario_matrix_fingerprint()` semantics remain unchanged in this gate. Existing callers may continue supplying the legacy fingerprint. The full digest is carried by MatrixCapture and later package manifest/validation records; it is not retroactively required in the frozen design constructor in this contract-only change.

## 3. CapturedBenchmark immutability and compatibility

Current source declares `CapturedBenchmark` as frozen but stores `report: dict[str, Any]`. A frozen dataclass does not deep-freeze that dictionary or its nested objects. The report can therefore be mutated after capture.

Minimum source-level resolution:

- retain `report` as the legacy compatibility view for current consumers;
- add a versioned immutable report snapshot with exact canonical source bytes and SHA-256, captured immediately after report production and before returning;
- package export reads the immutable report snapshot, never the mutable compatibility dict;
- any mismatch between a freshly serialized compatibility view and the retained snapshot is a validation failure, not a silent refresh;
- add `matrix_capture` as an immutable typed field on `CapturedBenchmark`;
- keep `outer_world_bundles` and `evidence_index` unchanged.

This does not require converting the entire legacy report API to immutable mapping types in the same change. It establishes a stable authoritative export payload without breaking existing report consumers.

## 4. External companion artifacts

The following companion artifacts are independent of `CapturedBenchmark`. They are not generated by the benchmark producer and are not fabricated from its declared fingerprints.

### 4.1 CalibrationBankManifest v1.0.0

Schema ID: `TGCV-C10S-VCONT-CALIBRATION-BANK-MANIFEST`.

Required fields:
- schema ID/version and benchmark/design identity;
- bank label exactly `calibration`;
- the complete ordered calibration SeedAssignment rows actually materialized and used for calibration;
- declared scenario/version/N/M/R and assignment cardinalities;
- seed-derivation namespace/version and generator identity where applicable;
- canonical manifest bytes and SHA-256;
- source execution/run identity and artifact reference.

The independent verifier recomputes the manifest digest and validates each row, exact cardinality/order and bank label. It then recomputes the disjointness check against the complete evaluation SeedAssignment rows retained in the benchmark capture, across all world, Z-assignment and G-assignment streams. A declared seed-bank fingerprint alone is insufficient. If the calibration rows actually used cannot be recovered, status is `UNAVAILABLE` and Gate 164 confirmatory completeness fails. No empty or placeholder manifest is accepted.

The calibration manifest must be retained as a separate package file `seeds/calibration_seed_manifest.json`, as already specified by Gate 164. It must not be passed into the evaluation producer as if it were evaluation input.

### 4.2 Gate159ReconciliationArtifact v1.0.0

Schema ID: `TGCV-C10S-VCONT-GATE159-RECONCILIATION`.

Required fields:
- benchmark/export identity and the exact calibration/evaluation manifest digests;
- check-set and verifier version;
- row counts and one-to-one join counts;
- calibration/evaluation stream intersection results;
- SeedAssignment ↔ RunManifest reconciliation results;
- explicit findings keyed to the affected assignment/run identity;
- status `RECONCILED`, `NOT_RECONCILED`, `REJECTED` or `UNVERIFIABLE`;
- canonical bytes and digest.

The artifact is produced by a deterministic reconciliation operation separate from the package builder. The package builder must not create a successful reconciliation result by copying producer fields. A missing artifact is `UNAVAILABLE`, not an empty success.

### 4.3 SourceExecutionEvidence v1.0.0

This is an independently resolved provenance companion, not a producer assertion. It must bind repository, workflow path/ref, workflow event, run ID/attempt, source commit/tree identity, artifact ID/digest, and the relationship between the artifact and the tested/producer commit. The exact trusted-workflow requirements remain those in Gates 160–163 and the Gate 164 provenance contract.

The producer's `design.executable_commit` is a declaration only. It is not proof of the executed commit. Missing independent GitHub resolution remains `UNAVAILABLE` / `UNVERIFIABLE`.

### 4.4 TechnicalTestEvidence v1.0.0

This companion records independently retrieved workflow/run and test-artifact evidence: repository, workflow identity, run/attempt, event/ref/commit, command or test target, counts, conclusion, artifact ID and digest. It must distinguish tests of the serializer/verifier from tests of the scientific harness. A test PASS does not establish scientific validity or causal identification.

No technical test artifact is created by Gate 176. Until actual execution and independent retrieval, status remains `UNAVAILABLE` / `NOT_VERIFIED`.

## 5. Join and trust model

All companion artifacts bind to the same deterministic `benchmark_export_id` and frozen design identity. Their own schema version and digest remain independent. The package builder verifies byte integrity and schema shape; the independent verifier resolves external provenance and validates signatures/attestations under the governed policy.

Trust states remain distinct:
- present with valid self-digest is not independently reconciled;
- reconciled identity is not authenticated;
- authenticated provenance is not scientific validity;
- technical test evidence is not experiment evidence;
- a complete package is not causal identification.

No single `PASS` collapses these layers.

## 6. Required source changes after this contract

The minimum future implementation diff is bounded to the capture/export boundary:

1. Add a data-only matrix row serializer and `MatrixCapture` builder using the exact already validated `specs`.
2. Add the versioned full-matrix JCS digest while preserving the legacy function unchanged.
3. Extend `CapturedBenchmark` with `matrix_capture` and immutable report snapshot fields; preserve the existing report/bundle/index fields for compatibility.
4. Add strict validators for the matrix capture schema and digest.
5. Add independent companion-artifact input types/validators for calibration, Gate 159, source execution and test evidence. These remain separately supplied and independently verified.
6. Update Gate 164 package adapter only after the new capture fields exist and have technical regression coverage.

Do not:
- rebuild the matrix during export;
- derive calibration rows from evaluation assignments;
- treat the design's seed/config/executable fingerprints as independently authenticated;
- use a mutable report dict as the package's authoritative payload;
- modify estimand definitions, DGP, Analyzer, Evaluator, Generator or Sealer semantics;
- execute calibration, generate seeds, run a benchmark or perform scientific execution as part of this contract.

## 7. Gate 176 disposition

- Exact capture-time matrix retention contract: **DEFINED**.
- Full matrix digest including `tolerance_id`: **DEFINED; NOT IMPLEMENTED**.
- Legacy matrix fingerprint compatibility: **PRESERVED**.
- Mutable report dict issue: **CONFIRMED; immutable export snapshot contract DEFINED**.
- Calibration manifest as independent companion: **DEFINED; NOT PROVIDED BY CURRENT CAPTURE API**.
- Gate 159 reconciliation artifact: **DEFINED; NOT IMPLEMENTED/NOT PROVIDED**.
- GitHub source execution and technical test evidence: **EXTERNAL COMPANIONS DEFINED; NOT PROVIDED BY CAPTURE API**.
- Serializer and strict verifier: **NOT IMPLEMENTED**.
- Tests, CI, package generation, calibration, seed generation and benchmark: **NOT EXECUTED**.
- Scientific execution: **NOT AUTHORIZED**.
- `main`: unchanged; PR #116 remains Draft on its existing base.

**Next Gate 177:** source/API implementation-readiness review of the Gate 176 bounded change set, including compatibility of CapturedBenchmark consumers, full-matrix digest algorithm test vectors, immutable report snapshot encoding, and companion artifact schemas. Do not execute tests until technical execution is explicitly authorized by the applicable governance.

## 8. Gate 177 — implementation-readiness qualification

Gate 177's source/API audit confirms the exact capture boundary exists, but Gate 176 is **not yet implementation-ready**. The current matrix validator checks 52 unique keys and declared coverage but does not enforce the canonical SCENARIO_IDS × ESTIMAND_SPECS row order; the legacy fingerprint sorts rows and therefore cannot prove order. Gate 178 must freeze positional validation and exact allowed field/value types.

The current `FrozenSnapshot.capture()` accepts dataclasses only, not the top-level report dict. The generic encoder's Python `json.dumps` is not RFC 8785 JCS, and the current decoder is not strict. Gate 178 must define a separate typed `FrozenReportSnapshot`, its report projection, pinned JCS implementation/version and strict decoder.

Preserve the three current `CapturedBenchmark` fields and their report/bundle/index shapes. Gate 177 recommends adding new trailing optional fields for MatrixCapture and report snapshot; producer-created captures must populate both, while package export rejects missing fields. The existing integration regression consumes the legacy report shape.

Gate 176's `capture_id` and `benchmark_export_id` need a non-circular deterministic derivation. Gate 177 proposes one content digest with `benchmark_export_id = capture_id`, excluding external companion artifacts. Calibration and Gate 159 companion descriptions also require exact row schemas, cardinalities, denominators and applicability rules.

See `C10_S_VCONT_CAPTURE_EXPORT_IMPLEMENTABILITY_AUDIT_GATE_177_DRAFT_001.md`. Gate 176 remains DEFINED / QUALIFIED; implementation remains OPEN. No code or tests were changed/executed.

## 8. Gate 178 — schema closure and serialization qualification

Gate 178 specifies the exact MatrixCapture row field set/value domains and positional order (SCENARIO_IDS × ESTIMAND_SPECS), the full-matrix JCS digest input, the FrozenReportSnapshot payload, deterministic non-circular capture identity, CalibrationBankManifest, Gate159ReconciliationArtifact, SourceExecutionEvidence, TechnicalTestEvidence and strict decoder requirements. The legacy matrix fingerprint and legacy report fingerprint remain unchanged and separately verified.

Gate 178 also identifies a blocker not resolved by Gate 176: the seed derivation produces uint64 integers, while the Gate 164 JCS package contract does not define an exact uint64 wire encoding and prohibits bare numeric-to-string coercion. No package implementation may proceed until this is resolved through an explicit versioned schema decision. Full crosswalk: `C10_S_VCONT_CAPTURE_EXPORT_SERIALIZATION_AND_COMPANION_SCHEMAS_GATE_178_DRAFT_001.md`.

## 9. Gate 179 — capture identity and report/calibration schema v2

Gate 179 versions the JCS projections that contain direct seed values. FrozenReportSnapshot, CalibrationBankManifest and benchmark capture identity advance to schema version 2.0.0 and use the exact typed uint64 object `{"$type":"uint64","decimal":"<canonical unsigned decimal>"}` for every direct seed field. MatrixCapture remains v1.0.0 because it contains no seeds. Gate159 reconciliation remains v1.0.0 because raw seed values are not included in its check records.

The historical report, matrix and seed-bank fingerprints remain unchanged and are computed under their existing algorithms from source values. Gate 164 v1.0.0 remains frozen; its wire-compatible successor is v2.0.0. The full decision and direct-field registry are in Gate 179.

## 10. Gate 180 — source API reconciliation

Gate 180 confirms that the current `produce_and_capture_benchmark()` validates and passes the exact `specs` tuple to Evaluator but does not retain it in the returned `CapturedBenchmark`. The returned object still contains only `report`, `outer_world_bundles` and `evidence_index`; no MatrixCapture or FrozenReportSnapshot fields are present. Gate 176/178's required immutable capture-at-source behavior therefore remains specified but not implemented.

The current producer accepts evaluation assignments and structural ScenarioConfig templates only. Calibration manifest, Gate159 reconciliation, source-execution evidence and technical-test evidence remain separately sourced companions; a future export assembler must bind them to the same capture identity and fail closed when required companions are absent. See Gate 180.
