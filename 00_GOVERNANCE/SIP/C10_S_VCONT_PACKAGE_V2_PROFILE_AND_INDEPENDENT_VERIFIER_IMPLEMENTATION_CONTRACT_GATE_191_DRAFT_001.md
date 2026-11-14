# C10-S V_cont — Gate 191: v2 package profile and independent verifier implementation contract

**Status:** IMPLEMENTATION CONTRACT DEFINED — SOURCE FIXES PERSISTED / STATIC AUDIT CONDITIONAL / TESTS NOT EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 190 — FrozenReportSnapshot v2.1 source reconciliation  
**Normative predecessors:** Gates 164, 174, 178, 181, 182, 188, 189 and 190  
**Scope:** static source audit, correction of Gate 190 reconciliation defects, explicit package-v2.0.0 profile dependency on FrozenReportSnapshot v2.1.0, and bounded writer/verifier implementation contract  
**Execution:** GitHub source inspection and source/document edits only. No imports, compilation, tests, workflow dispatch, package construction, producer invocation, seed generation, calibration or scientific execution.

## 1. Historical reconstruction and scope decision

Gate 182 already defines the package writer and independent verifier modules, public APIs, 14-file inventory, pure implementation boundary, dependency pin, test modules and acceptance criteria. Gate 188 subsequently made the FrozenReportSnapshot v2.1.0 schema decision. Gate 190 found that the writer, verifier and package test modules are absent.

Gate 191 does not duplicate or replace Gate 182. It closes the missing integration detail: the exact package-v2 profile dependency and how the report v2.1 sub-schema is admitted, serialized and independently verified. It also performs the source audit explicitly requested by Gate 190.

The following remain frozen:
- Gate 164 package v1.0.0 and its exact inventory/semantics;
- Gate 181 source-to-wire contract and FrozenReportSnapshot v2.0.0;
- Gate 188's explicit FrozenReportSnapshot v2.1.0 successor contract;
- Gate 182 writer/verifier public API and implementation boundary;
- RUN-EXPORT-ENVELOPE v1.0.0 historical semantics.

No artifact is silently reinterpreted. No package or report bytes are relabelled across versions.

## 2. Gate 190 source audit — defects found and corrected

### 2.1 Defect A: AnalysisContract incorrectly treated as run-scoped

The Gate 190 helper attempted to read `AnalysisContract.run_id`. Inspection of the actual dataclass confirms that AnalysisContract has no `run_id` field. This would raise an AttributeError for a valid bundle and prevent positive source reconciliation.

Correction persisted in `vcont_evidence_export.py`:
- run-scoped ID equality now applies only to TruthProjection, EvidenceCandidate, SealedEvidence, AnalyzerResult and EvaluationReport;
- AnalysisContract is instead reconciled through its actual semantic identity fields against RunManifest and AnalyzerResult;
- the AnalysisContract snapshot digest is recomputed and compared to the digest retained by RunEvidenceBundle.

### 2.2 Defect B: source bundle validation was incomplete

The prior helper restored some snapshots but did not verify the retained EvidenceCandidate and SealedEvidence source pair, despite these being part of RunEvidenceBundle and the package source boundary.

Correction persisted:
- restore and validate both typed snapshots;
- compare run IDs, rows, provenance and row count;
- recompute provenance digest;
- recompute the legacy SealedEvidence digest and compare it to the bundle's retained digest and AnalyzerResult.input_sha256;
- recompute the structural ScenarioConfig digest after removing the exact per-run identity/seed fields specified by RunEvidenceBundle.capture;
- recompute AnalysisContract digest.

These checks preserve the source bytes and do not invoke any producer.

### 2.3 Defect C: two adversarial tests could fail for the wrong reason

The Gate 190 manifest-seed and TruthBundle-seed tests replaced the complete per-outer row with a partial dictionary. After Gate 190 added required Evaluator row labels and summary fields, those tests could fail on a missing row label rather than the intended seed mismatch.

Correction persisted in `test_vcont_capture_v2.py`: both tests now preserve the original valid row and replace only the relevant RUN tuple value.

### 2.4 Positive fixture corrected to represent a complete source bundle

The positive fixture previously used a MatrixTruthProjection snapshot as a placeholder for EvidenceCandidate and SealedEvidence. Gate 191 replaced those placeholders with typed, digest-consistent EvidenceCandidate and SealedEvidence snapshots, consistent structural/contract hashes and AnalyzerResult source digests. The fixture remains deterministic and does not invoke Generator, Sealer, Analyzer, Evaluator or any producer.

Two additional negative fixtures cover AnalysisContract/RunManifest identity divergence and SealedEvidence digest divergence.

**Disposition of these corrections:** source edits persisted, statically inspected, not compiled or executed. They are not a test PASS.

## 3. Package v2 profile — exact version and dependency

The only confirmatory successor profile defined by this Gate is:

- package schema ID: `TGCV-C10S-VCONT-MC-PACKAGE`;
- package schema version: `2.0.0`;
- RUN export envelope schema ID: `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE`;
- RUN export envelope schema version: `2.0.0`;
- `benchmark_export_id = capture_id` exactly, as the Gate 181 v2 identity contract specifies;
- report snapshot schema ID: `TGCV-C10S-VCONT-REPORT-SNAPSHOT`;
- report snapshot schema version: **`2.1.0`**;
- report payload type: `TGCV-C10S-VCONT-BENCHMARK-REPORT`;
- report canonicalization: RFC 8785 JCS.

The v2 package manifest MUST declare the report dependency explicitly as a typed schema dependency containing exactly the report schema ID, version and payload type. The report JSON itself remains the exact FrozenReportSnapshot v2.1.0 envelope defined in Gate 188; no additional `payload_version`, `payload_schema` or other envelope key may be inserted into that report envelope.

The package profile is not a permissive family selector. It accepts exactly the declared report v2.1.0 schema. It rejects v2.0.0, unknown future versions, missing version declarations and mismatched payload types. No implicit migration or fallback is permitted.

## 4. Exact archive inventory

The v2 profile retains the exact 14 Gate 164 paths, each once:

1. `manifest.json`
2. `report/report.json`
3. `design/benchmark_design.json`
4. `design/scenario_estimand_matrix.json`
5. `design/effective_scenario_configs.json`
6. `design/analysis_contracts.json`
7. `seeds/evaluation_seed_assignments.json`
8. `seeds/calibration_seed_manifest.json`
9. `runs/temporal_manifest.json`
10. `runs/run_records.json`
11. `provenance/source_execution.json`
12. `provenance/configuration_fingerprints.json`
13. `validation/reconciliation_results.json`
14. `validation/test_evidence.json`

No fifteenth path, alias, duplicate, symlink, hardlink, executable, hidden file or directory-as-data is allowed. The exact path-to-payload mappings and the JSON/JCS and deterministic uncompressed POSIX TAR profiles remain those frozen in Gate 164 and elaborated by Gate 174.

### 4.1 Report file

`report/report.json` contains the complete FrozenReportSnapshot v2.1.0 envelope, byte-for-byte as produced by the capture boundary. It includes the four wrappers at the exact registered scenario RUN pointers from Gate 188. It must not be regenerated from report summaries or from the run records.

The package writer checks:
- exact schema ID/version/payload type;
- exact v2.1 field allowlist and four-pointer registry;
- all four source values were reconciled before projection;
- JCS canonical bytes and report snapshot SHA-256;
- the historical Evaluator report fingerprint remains a separate source-domain digest calculated before uint64 projection.

The writer must not recompute the legacy report fingerprint over wrapper objects.

### 4.2 RUN export envelope

`runs/run_records.json` uses RUN-EXPORT-ENVELOPE v2.0.0. It preserves the Gate 174 record layout and source snapshots, with the v2 identity alias `benchmark_export_id = capture_id`. It is not compatible with RUN-EXPORT-ENVELOPE v1.0.0; each reader rejects the other version.

All legacy FrozenSnapshot canonical bytes remain opaque and byte-preserved. Their own SHA-256 and allowlisted type IDs are verified; they are not reserialized as JCS and are not modified to insert uint64 wrappers. Typed uint64 wrappers apply to the package/report JSON projection only at the exact registered pointers.

## 5. Digest and identity dependency graph

The writer and verifier must preserve the following distinct sequence:

1. Historical Evaluator report fingerprint: recompute from the original source-typed manifest payload using the exact legacy algorithm before wire projection.
2. FrozenReportSnapshot v2.1.0 digest: SHA-256 over RFC 8785 JCS bytes of the complete report envelope, including the four typed uint64 wrappers.
3. Capture identity: derive from the versioned Gate 181 content identity inputs, including the v2.1 report snapshot digest; `capture_id` is not an input to itself.
4. `benchmark_export_id`: exact alias of `capture_id` in RUN export envelope v2.0.0.
5. Package manifest digest and package ID: derive from the exact package-v2 manifest identity inputs and all 14 file digests under Gate 164/182 rules.
6. Archive SHA-256: hash the exact final deterministic TAR bytes. It is a detached result/receipt field and must not be embedded in the archive whose digest it represents.

No digest is a substitute for another. No package self-hash, circular manifest field or post-hoc change to a frozen identity algorithm is allowed.

## 6. Writer implementation contract

The writer is the pure module `vcont_package_v2.py`, using Gate 182's normative API:

- `build_package_v2(captured, design, companions, *, profile="CONFIRMATORY")`;
- `serialize_package_files_v2(captured, design, companions, *, profile)`;
- `build_deterministic_tar_v2(files)`.

It MUST:
- import neither producer classes nor producer functions that execute generation/evaluation;
- accept already materialized CapturedBenchmark, design and actual companion evidence;
- reject incomplete captures, unsupported schema versions, wrong capture identity, matrix order/fingerprint mismatch, report v2.0.0 or unknown report schema, and every unregistered uint64 path;
- require the exact 14 paths and serialize every file under the Gate 164/174 JCS profile;
- apply Gate 181 v2 projections and the Gate 188 v2.1 report projection contract;
- preserve every FrozenSnapshot byte sequence exactly in run records;
- require actual calibration manifest, Gate159 reconciliation, source-execution evidence and technical-test evidence for CONFIRMATORY output; missing or unverifiable mandatory inputs block confirmatory construction;
- never infer, synthesize, repair, normalize or fabricate missing companion evidence;
- return exact inventory, per-file byte lengths/digests, package ID, archive bytes and archive SHA-256 without claiming external authentication.

No diagnostic package profile is defined by Gate 191. If later required, it needs a distinct schema ID/profile and explicit governance decision; it cannot be labelled confirmatory, reconciled or authenticated.

## 7. Independent verifier implementation contract

The independent module is `vcont_package_v2_verify.py`, using Gate 182's API:

`verify_package_v2(archive_bytes, *, expected_profile=None, trust_policy=None) -> PackageVerificationResult`.

Independence means:
- no import or call of writer projection, serialization, package-ID or TAR-building functions;
- no trust in writer status flags, package-declared PASS values or caller-supplied reconciliation booleans;
- independent TAR parsing, path validation, JSON duplicate-key parser, schema/allowlist validation, report pointer traversal, uint64 wrapper decoder, digest recomputation and logical joins;
- independent recomputation of the historical report fingerprint from the decoded source-domain manifest payload;
- independent enforcement of exact report schema dependency v2.1.0 and RUN export envelope v2.0.0;
- strict rejection of any v1/v2 cross-read, unknown schema version, wrong report payload type or unregistered wrapper.

It returns separate results for package integrity, schema conformance, evidence completeness, identity reconciliation, source-execution provenance, technical test evidence and external authentication. No single aggregate PASS may conceal an unavailable layer. Authentication is NOT_AUTHENTICATED unless a separate governed trust policy and valid external attestation are actually verified.

The verifier must check all 14 files, JCS canonical bytes, manifest lengths/digests, deterministic TAR metadata, report/capture/run-record joins, 13 scenarios, 52 matrix pairs, M/R/RUN cardinalities, all Gate 181 and Gate 188 seed pointers, Gate159 companion derivation and calibration/evaluation disjointness. It must reject duplicate JSON keys, malformed uint64 wrappers, bare integers at registered pointers, wrappers at unregistered pointers, orphan/duplicate joins, tampered bytes, path traversal and noncanonical archive entries.

## 8. Implementation order and bounded file scope

Gate 192 should implement in the following reviewable order:

1. `vcont_package_v2.py`: immutable companion/result types, exact profile/schema constants, pure projection/serialization, 14-file inventory and deterministic TAR.
2. Pure serializer fixtures: `test_vcont_package_v2_serialization.py`, `test_vcont_package_v2_companions.py`, and `test_vcont_package_v2_compatibility.py`.
3. `vcont_package_v2_verify.py`: independently implemented archive/parser/schema/digest/join validation.
4. Independent verifier fixtures: `test_vcont_package_v2_verifier.py`.
5. Static source audit of the writer/verifier/test separation and workflow path scope.

The already pinned `rfc8785==0.1.4` and wheel SHA-256 from Gate 184 are reused; do not introduce a second canonicalizer or silently change the dependency. RFC 8785 conformance vectors remain unexecuted and must be included in the pure tests.

Only these new package modules and their pure test modules, the relevant documentation and explicitly scoped pure workflow may be touched. Do not modify Generator, Sealer, Analyzer, Evaluator, ScenarioConfig semantics, seed generation, DGPs, estimands, calibration producers, scientific protocols or main.

The workflow remains manual-only. Gate 192 must preflight its exact path filter and explicit test list before any source writes. No tests or workflow are run under this Gate.

## 9. Required test vectors before technical execution authorization

The pure suite must include:
- exact 14-file inventory; missing/extra/duplicate path;
- report schema v2.1 accepted; v2.0, unknown version and payload mismatch rejected;
- RUN envelope v2.0 accepted; v1.0 and unknown versions rejected;
- all four nested uint64 pointers, zero, 2^53-1, 2^53 and 2^64-1;
- malformed wrappers, duplicate JSON keys, bare numeric values, unregistered wrappers and unknown nested fields;
- source report fingerprint unchanged by wrapper projection;
- report snapshot JCS digest, capture identity, package ID and archive digest separated and non-circular;
- exact opaque FrozenSnapshot bytes preserved;
- positive source-to-report/run-record reconciliation and negative seed/source/identity divergence;
- JCS UTF-16 property ordering, Unicode escaping, number formatting, negative zero and non-finite rejection;
- deterministic TAR byte equality, normalized metadata, path traversal and duplicate path rejection;
- missing/invalid calibration, Gate159, source-execution or test companions blocking CONFIRMATORY profile;
- companion digest changes package ID but not capture_id;
- writer/verifier algorithmic separation;
- tampering of each file, manifest, report wrapper, snapshot bytes and archive metadata rejected.

All tests use fixed deterministic source fixtures. They must not call Generator, Sealer, Analyzer, Evaluator, producer functions, seed-bank generation, calibration, or scientific DGPs.

## 10. Current disposition and authorization boundary

| Item | State |
|---|---|
| Canonical bootstrap from main | READ / POINTERS CONSISTENT AT DOCUMENT LEVEL |
| Gate 190 source audit | CORRECTIVE DEFECTS FOUND AND SOURCE-CORRECTED |
| AnalysisContract false run_id access | CORRECTED IN SOURCE |
| EvidenceCandidate/SealedEvidence source checks | ADDED |
| Gate 190 false-positive-prone test rows | CORRECTED |
| Complete positive typed source fixture | ADDED |
| Gate 191 additional negative fixtures | WRITTEN |
| Package v2.0.0 → report v2.1.0 profile dependency | DEFINED |
| Exact 14-file v2 inventory | FROZEN / REUSED |
| Writer module | NOT IMPLEMENTED |
| Independent verifier module | NOT IMPLEMENTED |
| Package pure test modules | NOT IMPLEMENTED |
| Tests / compilation / CI | NOT EXECUTED |
| Package generation / seed / calibration / scientific execution | NOT AUTHORIZED / NOT EXECUTED |
| main / RMA / Evidence→Claim Matrix / STATUS | UNCHANGED |
| PR #116 | OPEN / DRAFT / ORIGINAL BASE RETAINED |

**Gate 191: IMPLEMENTATION CONTRACT DEFINED — STATIC SOURCE AUDIT CONDITIONAL; NO TECHNICAL OR SCIENTIFIC EXECUTION.**

### Next operation — Gate 192

Preflight the manual pure workflow against the exact future package module/test paths, then implement the package writer only. Do not implement or call the verifier in the same code slice; first complete a static writer review. Tests remain unexecuted pending separate technical execution authorization.

## Gate 192 implementation addendum

Gate 192 partially implements the pure file/TAR writer in `03_EXPERIMENTS/C10-S/harness/vcont_package_v2.py`, with seven deterministic pure tests and an expanded explicit manual workflow allowlist. The writer uses the locked RFC 8785 dependency, preserves the 14-path inventory, requires all eleven materialized companion payloads, recomputes capture identity, and constructs normalized deterministic USTAR bytes. It does not import or invoke producer classes/functions.

This is not complete package conformance: field-level companion schemas and all semantic joins are not yet fully validated by the writer; the independent verifier remains absent. No tests, compilation or workflow were executed. See Gate 192.

