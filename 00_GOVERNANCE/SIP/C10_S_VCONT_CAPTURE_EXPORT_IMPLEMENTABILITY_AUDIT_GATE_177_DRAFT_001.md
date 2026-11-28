# C10-S V_cont — Gate 177: capture/export implementability audit

**Status:** STATIC SOURCE/API AUDIT — CONDITIONAL / NOT YET IMPLEMENTATION-READY  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 176 capture-time matrix and external companion contract  
**Audited source:** `vcont_evidence_export.py`, `vcont_benchmark_protocol.py`, `vcont_integrated_harness.py`, and `test_vcont_integrated_harness.py`  
**Execution:** GitHub source inspection only; no imports, compilation, tests, CI, benchmark, seed generation, calibration, package generation or scientific execution

## 1. Executive verdict

The Gate 176 change remains correctly bounded to the capture/export boundary. The producer already has the exact orchestration point required: it materializes `specs`, validates the matrix, and later passes that same tuple to `evaluate_monte_carlo_benchmark()`. RUN/R and M evidence capture is already implemented.

However, Gate 176 is **not yet implementation-ready as written**. The source audit found four specification gaps that must be closed before code is changed:

1. The existing validator accepts any ordering of the 52 unique matrix rows, while Gate 176 requires canonical ordering. The legacy fingerprint sorts rows and therefore does not establish input order.
2. The report snapshot's canonical encoding, schema and deterministic identity derivation are not fully specified. The current `FrozenSnapshot.capture()` accepts dataclasses only, not the top-level report dictionary; the generic encoder is not RFC 8785 JCS.
3. The compatibility-preserving field extension to `CapturedBenchmark` is not explicit enough. Existing tests consume the mutable `report` dict and its current keys/cardinalities.
4. The companion artifact schemas still need exact row schemas, cardinality/order rules and reconciliation scope, especially for calibration rows that may not map one-to-one to evaluation RunManifest records.

No evidence justifies changing Generator, Sealer, Analyzer, Evaluator, the DGP, estimands or N/R/M semantics.

## 2. Reconstructed current source boundary

### 2.1 Matrix path

`produce_and_capture_benchmark()` currently:

1. converts the supplied matrix to `specs = tuple(matrix)`, or builds the default matrix;
2. calls `validate_monte_carlo_benchmark_design(design, specs)`;
3. retains `specs` in local scope while capturing the 13×M evidence bundles;
4. passes the same `specs` to `Evaluator.evaluate_monte_carlo_benchmark(..., matrix=specs)`;
5. returns `CapturedBenchmark(report, tuple(bundles), tuple(evidence_index))`.

This is the correct capture boundary for MatrixCapture. No second matrix build is needed.

### 2.2 Matrix validation gap

The current `validate_monte_carlo_benchmark_design()` validates:
- exactly 52 unique EvaluationKeys;
- declared scenario/version coverage;
- estimand version `001`;
- equality of the legacy fingerprint;
- design dimensions and MCSE target coverage.

It does **not** validate the canonical row sequence. `scenario_matrix_fingerprint()` sorts tuples before hashing, so a permutation of the same matrix rows retains the same legacy fingerprint. Consequently, Gate 176's canonical ordering requirement is not enforced at the current producer boundary.

Minimum resolution: construct the expected ordered key sequence from `SCENARIO_IDS` × `ESTIMAND_SPECS` and reject any supplied `specs` sequence whose keys differ positionally. Do not silently sort after capture. The exact accepted tuple is then both captured and passed to the evaluator.

The matrix capture validator must also enforce exact field types and enumerated value sets, not merely rely on dataclass annotations. At minimum validate the allowed values for evaluation class, truth status, run/repeated evaluation classes and identification expectation; require exact booleans for abstention; validate nullable string fields explicitly; reject missing/extra fields and duplicate keys. Preserve explicit nulls.

### 2.3 Existing fingerprint

The current legacy fingerprint sorts rows and includes most declared fields but omits `ScenarioEstimandSpec.tolerance_id`. Gate 176 correctly requires a separate full-matrix digest. The new digest must include:
- all four nested EvaluationKey fields;
- all ScenarioEstimandSpec fields, including `tolerance_id`;
- explicit null values;
- canonical row order;
- schema ID/version.

The legacy function must remain byte-for-byte unchanged for compatibility. The full digest must not be substituted into `MonteCarloBenchmarkDesign.matrix_fingerprint`.

## 3. CapturedBenchmark compatibility

Current source:

```python
@dataclass(frozen=True)
class CapturedBenchmark:
    report: dict[str, Any]
    outer_world_bundles: tuple[OuterWorldEvidenceBundle, ...]
    evidence_index: tuple[tuple[str, str, str], ...]
```

The existing integration regression constructs the object only through `produce_and_capture_benchmark()` and checks:
- `captured.report["coverage"]`;
- `captured.report["pair_ledger"]`;
- `captured.report["temporal_manifest"]`;
- `captured.outer_world_bundles`;
- `captured.evidence_index`.

These legacy fields and their current value shapes must remain unchanged.

**Compatibility decision:** add `matrix_capture` and `report_snapshot` only as trailing fields with defaults of `None`, so the existing three-positional-argument constructor remains source-compatible. The producer must always populate both fields. Any confirmatory package/export validator must fail closed if either is absent; the defaults exist only for legacy construction/consumption, not to make an incomplete capture exportable. Do not replace `report` with a mapping proxy or change its current indexing behavior in this gate.

No exhaustive repository-wide caller inventory is claimed: GitHub code-search returned an incomplete result. The current harness integration test is a known compatibility consumer and must be preserved.

## 4. Report snapshot — exact implementation contract still needed

Current `FrozenSnapshot.capture()` rejects non-dataclass top-level values. `CapturedBenchmark.report` is a dictionary. Although the internal `_encode()` helper can recursively encode dictionaries, tuples and dataclasses, `_snapshot_digest()` uses Python `json.dumps` rather than RFC 8785 JCS. The current `_decode()` also restores enum payloads as their underlying values, accepts untagged dictionaries, and does not enforce exact field sets or duplicate-key rejection.

Therefore do not use `FrozenSnapshot.capture(report)` or treat `_snapshot_digest(report)` as the Gate 176 report snapshot contract.

Minimum new type: `FrozenReportSnapshot v1.0.0`, with:
- schema ID/version;
- payload type fixed to the benchmark report schema;
- canonical payload bytes;
- SHA-256 of those exact bytes;
- an explicit encoder version and canonicalization algorithm identifier.

The report payload must be a data-only, typed projection of the current report: design identity, temporal manifest, 52-pair ledger, scenario reports, coverage and the existing report fingerprint. It must preserve tuple/list distinctions where semantically relevant and preserve nulls. Only the currently allowed nested dataclasses/types may be encoded; arbitrary objects, bytes, non-string mapping keys, NaN and infinities are rejected.

Because report content includes floating-point metrics, its canonicalization must be a pinned RFC 8785 JCS implementation or an explicitly specified alternative with independently checked cross-language test vectors. Python's standard `json.dumps(sort_keys=True)` is not sufficient evidence of JCS conformance. The package verifier must recompute the digest from the canonical payload bytes, not from the mutable compatibility dictionary.

The snapshot is captured immediately after Evaluator returns the report and before the producer returns. The report dictionary remains the legacy view. Mutation of that dictionary after capture must not mutate the retained bytes. If a compatibility consistency check is exposed, it is a separate check and must never refresh or overwrite the frozen snapshot.

## 5. Deterministic capture identity — Gate 176 ambiguity

Gate 176 declares both `capture_id` and `benchmark_export_id` but does not define their exact derivation or prevent a circular digest.

Freeze the following non-circular construction:
1. Build a capture identity payload that excludes both IDs and excludes all companion artifacts.
2. Include the canonical design identity, full-matrix digest, evaluation assignment manifest digest, ordered scenario/M evidence-bundle digests, immutable report-snapshot digest, and a deterministic evidence-index projection.
3. Canonicalize that payload under a named versioned algorithm and calculate SHA-256.
4. Set `capture_id` to that digest and define `benchmark_export_id = capture_id` as an alias for this benchmark capture identity.
5. Companion artifacts refer to this ID but do not change it.

The exact canonical identity payload schema and field order must be frozen before implementation. It must not include timestamps, random UUIDs, mutable paths or caller-supplied self-assertions. Identical captured content under identical schema versions yields the same identity; a changed assignment, matrix, evidence bundle or report changes it.

## 6. Companion artifact readiness

Gate 176 correctly separates calibration, Gate 159 reconciliation, source execution and technical-test evidence from the evaluation producer. Their current descriptions are not yet strict enough to implement independent validators.

### 6.1 CalibrationBankManifest

Before implementation, freeze:
- exact `SeedAssignment` row field set and types;
- canonical order (scenario order, outer-world order, designated RUN, then R index);
- expected cardinality for the declared calibration design, not copied from evaluation design unless the calibration design explicitly has identical dimensions;
- the exact stream-disjointness calculation over world, Z and G seeds;
- the seed-derivation namespace/version and generator identity fields;
- whether calibration rows have associated calibration execution records and what those records are.

A calibration row must not be forced into an evaluation RunManifest join if the calibration procedure does not create that object. Evaluation SeedAssignment ↔ RunManifest reconciliation remains a separate exact one-to-one check. Any calibration execution identity that cannot be independently retrieved remains UNAVAILABLE/UNVERIFIABLE.

### 6.2 Gate159ReconciliationArtifact

Freeze exact check-row schemas and keys before implementing the verifier. At minimum distinguish:
- evaluation assignment ↔ captured RunManifest one-to-one reconciliation;
- calibration/evaluation seed-stream disjointness;
- calibration assignment ↔ calibration execution evidence, only where such execution records actually exist;
- artifact/source identity checks.

Each check needs an explicit denominator, observed count, mismatch list and status. Missing inputs must be UNAVAILABLE/UNVERIFIABLE, not zero mismatches or successful empty checks. The artifact's status is derived from the complete required check set, not caller-declared.

### 6.3 SourceExecutionEvidence and TechnicalTestEvidence

The source-execution companion must be independently resolved from GitHub run/artifact metadata and trusted-builder policy; it cannot accept the producer's `executable_commit` as proof. Technical test evidence must bind exact workflow/run/attempt, tested commit, test target, conclusion and artifact digest. Keep serializer/verifier tests separate from scientific harness tests.

Gate 177 does not claim those external records are available or authenticated.

## 7. Existing regression coverage

The source contains `VContEvidenceOrchestrationTests` in `test_vcont_integrated_harness.py`. Its complete-benchmark regression checks the 52-pair report, 13×M evidence bundles, evidence index and temporal-manifest cardinality. It also checks rejection of missing scenario/M groups and calibration rows supplied to the evaluation producer.

The current tests do not cover the Gate 176 additions:
- exact MatrixCapture row retention and canonical order;
- rejection of a permuted matrix;
- full-matrix digest sensitivity to `tolerance_id`;
- complete field/type/enum validation;
- report snapshot immutability and JCS test vectors;
- deterministic capture/export identity and circularity exclusion;
- strict decoding and duplicate-key rejection;
- calibration companion schema and stream disjointness;
- Gate 159 reconciliation artifact completeness;
- independent source/test evidence binding.

No tests were executed in Gate 177. These are required regression cases for the later implementation gate.

## 8. Gate 177 disposition

| Item | Result |
|---|---|
| Capture boundary for exact matrix | AVAILABLE |
| Exact matrix retention | NOT IMPLEMENTED |
| Canonical matrix order enforcement | MISSING IN CURRENT VALIDATOR |
| Legacy fingerprint compatibility | PRESERVABLE |
| Full-matrix digest | SPECIFIED IN PRINCIPLE; exact type/ordering validation pending |
| CapturedBenchmark legacy API | PRESERVE THREE EXISTING FIELDS/SHAPES |
| Report snapshot | NOT IMPLEMENTED; current FrozenSnapshot API is not applicable to dict root |
| Report JCS canonicalization | ALGORITHM/DEPENDENCY NOT FROZEN |
| Deterministic capture/export ID | AMBIGUOUS IN GATE 176; non-circular derivation proposed in §5 |
| Calibration companion | CONCEPT DEFINED; row schema/cardinality/record linkage pending |
| Gate 159 companion | CONCEPT DEFINED; check-row schema/denominators pending |
| Source/test companions | EXTERNAL; independent retrieval/authentication not performed |
| Regression coverage | PARTIAL; no Gate 176-specific tests |
| Code/tests/CI/benchmark/scientific execution | NOT MODIFIED / NOT EXECUTED |

**Overall:** `AUDITED — CONDITIONAL`. Gate 176 is conceptually sound but not yet an executable implementation contract. No code change is made by this audit.

## 9. Next Gate 178

Close the remaining contract-level details before implementation:
1. Freeze MatrixCapture exact row schema, allowed values, canonical ordering and full-digest test vectors.
2. Freeze FrozenReportSnapshot encoding, pinned JCS implementation/version, report payload schema and strict decoder behavior.
3. Freeze the capture identity payload and deterministic `capture_id = benchmark_export_id` derivation.
4. Freeze exact CalibrationBankManifest and Gate159ReconciliationArtifact row schemas, cardinalities and applicability rules.
5. Freeze compatibility rules and the full regression test specification while preserving the existing report/bundle/index interface.

After Gate 178, reassess whether the bounded source diff is ready for implementation. Any test execution remains subject to the applicable technical execution authorization. No calibration, seed generation, benchmark or scientific execution is authorized by this audit.
