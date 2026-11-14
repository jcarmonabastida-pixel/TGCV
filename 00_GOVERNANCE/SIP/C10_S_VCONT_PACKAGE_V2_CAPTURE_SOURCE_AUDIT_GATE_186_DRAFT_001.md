# C10-S V_cont — Gate 186: static audit of capture primitives

**Status:** CONDITIONAL — TWO SOURCE CORRECTIONS IMPLEMENTED; REPORT NESTED SCHEMA ALLOWLIST OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 185 capture primitives implementation  
**Scope:** Gate 178/181 conformance audit of MatrixCapture, FrozenReportSnapshot and capture identity  
**Execution:** GitHub source/document inspection and source edits only. No imports, compilation, tests, CI dispatch, dependency installation, producer invocation, seed generation, calibration, package generation or scientific execution.

## 1. Audit basis and historical reconciliation

Gate 186 re-read the operative contracts before changing code:
- Gate 178 — `C10_S_VCONT_CAPTURE_EXPORT_SERIALIZATION_AND_COMPANION_SCHEMAS_GATE_178_DRAFT_001.md`;
- Gate 181 — `C10_S_VCONT_PACKAGE_V2_SOURCE_TO_WIRE_PROJECTION_CONTRACT_GATE_181_DRAFT_001.md`;
- Gate 182 — integrated implementation contract;
- Gate 184 — CI execution boundary;
- Gate 185 — implementation record;
- source `vcont_evidence_export.py`, `vcont_benchmark_protocol.py` and `vcont_integrated_harness.py`;
- Gate 185 pure fixture tests.

The canonical governance bootstrap on `main` was also recovered: RMA v3.38, Evidence→Claim Matrix v1.47, traceability v3.38 and Governance Operating Principles v0.1. Their pointers and declared versions agree at the source level. Local read-only validators were not executable in this GitHub-only operation; therefore no validator PASS is claimed. Main and the PR base were not modified.

## 2. Findings and corrections

### 2.1 Legacy report fingerprint algorithm identifier — corrected

Gate 181 freezes the exact identifier:

`TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1`

Gate 185's source constant used a different string. The fingerprint bytes and algorithm implementation were already intended to match the historical Evaluator sequence, but the metadata identifier did not conform to the contract.

Correction: `_LEGACY_REPORT_FINGERPRINT_ALGORITHM` now uses the exact Gate 181 identifier. The pure fixture test asserts the exact identifier as well as the report schema ID. The legacy fingerprint is still recomputed from the source-typed manifest before typed uint64 projection.

### 2.2 Capture identity design binding — strengthened

The previous `derive_capture_identity()` checked scenario/M coverage but did not independently verify that each OuterWorldEvidenceBundle's scenario version and N matched the declared design identity.

Correction: before ordering or hashing bundles, the helper now:
- requires the exact declared design identity field set;
- validates the authoritative 13-scenario/version order and nonempty versions;
- validates integer domains for N, M and R;
- checks every bundle's scenario ID/version and N against that design identity.

This is a capture-boundary identity validation only. It does not alter Generator, Sealer, Analyzer, Evaluator, assignments or estimands.

### 2.3 Report nested schema allowlists — OPEN / BLOCKING STRICT-CONFORMANCE CLAIM

The current report projection enforces:
- exact report root fields;
- exact design field set;
- exact legacy manifest field set;
- exact direct uint64 wrapping at the report's registered temporal and pair-ledger paths;
- equality of root and nested temporal manifests and pair ledgers;
- legacy fingerprint recomputation before wire projection.

However, it recursively projects `scenario_reports`, `coverage`, pair-ledger rows, contributions and nested metric/status objects without enforcing complete field allowlists for those nested structures. The current source therefore preserves unknown nested fields in the digest but does not reject schema drift as Gate 181 requires.

This is not a data-loss defect: unknown fields are not silently dropped. It is a schema-conformance defect: a changed nested source shape could still be emitted under the existing report snapshot version. Do not call the report projection a strict decoder or claim full Gate 181 conformance until the nested allowlists are implemented.

Gate 187 must define and enforce versioned exact field sets for:
- pair-ledger rows, contributions, metric summaries and identification-rate summaries;
- scenario report roots, coverage, metric blocks and per-outer-replicate substructures;
- top-level coverage and scenario key cardinality/order;
- report temporal-manifest cardinality and pair-ledger 52-row cardinality.

The allowlists must be derived from the actual Evaluator return construction, not invented from fixture-only shapes. Any future source-schema change must require an explicit payload schema-version increment.

## 3. Conformance disposition

| Component | Gate 186 result |
|---|---|
| MatrixCapture 52-row positional order and full digest | STATICALLY CONFORMANT TO REVIEWED CONTRACT |
| Legacy matrix fingerprint preserved separately | STATICALLY CONFORMANT |
| FrozenReportSnapshot envelope identity | STATICALLY CONFORMANT |
| Typed uint64 report pointers | STATICALLY CONFORMANT FOR THE REVIEWED REPORT PATHS |
| Root/nested temporal and pair-ledger equality | IMPLEMENTED; STATICALLY REVIEWED |
| Legacy fingerprint input/order | IMPLEMENTED; algorithm identifier corrected |
| Capture identity non-circularity | STATICALLY CONFORMANT TO REVIEWED PAYLOAD |
| Capture identity design-to-outer-world version/N join | CORRECTED; TEST NOT EXECUTED |
| Complete nested report field allowlists | OPEN — BLOCKS STRICT SCHEMA CONFORMANCE |
| Calibration/Gate159 companion schemas and assembler | DEFINED IN CONTRACT; NOT IMPLEMENTED |
| Package writer, independent verifier and deterministic TAR | NOT IMPLEMENTED |
| Pure tests / JCS conformance | NOT EXECUTED / NOT VERIFIED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `CONDITIONAL — CAPTURE PRIMITIVES IMPLEMENTED; NESTED REPORT SCHEMA CONFORMANCE OPEN`.

## 4. Modified source and regression

- `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`: exact Gate 181 legacy fingerprint algorithm identifier; capture design identity and outer bundle version/N reconciliation.
- `03_EXPERIMENTS/C10-S/harness/test_vcont_capture_v2.py`: exact Gate 181 report schema/algorithm identifier assertions.

The new design-to-bundle validation has not been exercised. The pure workflow remains manual-only and was not dispatched. The three earlier unintended push-triggered runs remain recorded under Gate 185 §9 / Gate 184 §10; no new CI run occurred during Gate 186.

## 5. Next operation — Gate 187

Implement the complete nested Evaluator-report schema allowlists and cardinality checks from the actual source construction, with positive and adversarial fixture vectors. Keep the existing report source payload and historical fingerprint unchanged. Do not run tests or dispatch CI without separate technical execution authorization. Do not invoke the producer or any scientific operation.
