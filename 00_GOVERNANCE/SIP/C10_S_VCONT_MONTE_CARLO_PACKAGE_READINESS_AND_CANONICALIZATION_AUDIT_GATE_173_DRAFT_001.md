# C10-S V_cont — Gate 173: package readiness and canonicalization audit

**Status:** STATIC SOURCE AUDIT COMPLETED — CONDITIONAL / PACKAGE BUILDER NOT READY  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** reconcile Gate 164 package v1.0.0, Gate 165 implementability findings, Gate 166 typed export, Gates 168–172 capture/orchestration source  
**Execution:** no tests, compilation, CI, calibration, seed generation, N/R/M sizing, benchmark or scientific execution

## 1. Purpose and historical reconstruction

Gate 173 audits whether the Gate 172 `CapturedBenchmark` and its nested evidence objects can be exported losslessly under the existing Gate 164 package contract. It reuses rather than recreates:

- Gate 164: package v1.0.0 path inventory, JCS/tar profile and digest dependency graph.
- Gate 165: report-only package insufficiency and the prohibition on reconstructing absent source evidence.
- Gate 166: typed export envelope, exact RunEvidenceRecord fields/cardinalities, structural/per-run config split and provenance separation.
- Gate 168: inline SealedEvidence rows+manifest retention decision and deep-immutable source snapshot requirement.
- Gates 170–172: immutable capture, one-M producer and benchmark-wide coordinator.

The source-of-truth remains GitHub. No main artifact was changed.

## 2. Executive finding

The Gate 172 source now carries most source objects that Gate 164 previously lacked. **The evidence envelope is present in memory, but there is no package serializer, JCS adapter, deterministic tar writer, package verifier or detached receipt.** A compliant package builder cannot be inferred merely from the existence of immutable snapshots.

Gate 164 v1.0.0's existing file inventory is sufficient in principle without adding a new archive path: `runs/run_records.json` can carry a versioned export-envelope object containing per-run records, one OuterWorldEvidenceBundle per scenario/M, the evidence index and explicit cardinality/integrity metadata. `report/report.json` remains the exact benchmark report. This is a clarified payload structure inside existing allowlisted paths, not a silent change to the path inventory or scientific semantics.

**Disposition: Gate 164 package schema remains DEFINED; source evidence availability is substantially improved; packager implementation remains BLOCKED/OPEN.**

## 3. Source-to-package implementability matrix

| Gate 164 payload | Gate 172 source availability | Gate 173 classification |
|---|---|---|
| Full report and 52-pair ledger | `CapturedBenchmark.report`; evaluator returns coverage, pair ledger, scenario reports, temporal manifest and legacy report fingerprint | AVAILABLE IN MEMORY; requires explicit data-only adapter |
| Benchmark design | `report["design"]` is the typed design | AVAILABLE; serialize exact typed fields |
| 52-row matrix | Exact `specs` passed to evaluator, but not returned as a first-class field by CapturedBenchmark | PARTIAL; retain exact matrix used in envelope, do not rebuild from report |
| Effective ScenarioConfig | Per-run snapshots in every RunEvidenceBundle, including structural parameters and assignment-specific values | AVAILABLE; structural projection and per-run binding remain distinct |
| AnalysisContract | Per-run immutable snapshots and content digest | AVAILABLE; preserve exact per-run references; deduplication is optional |
| Evaluation SeedAssignment | Exact SeedAssignment snapshot per run | AVAILABLE; bank/namespace/fingerprint reconciliation remains separate |
| Complete RunManifest | Exact per-run snapshot; report temporal manifest is reduced | AVAILABLE in bundle; report projection is not a substitute |
| Matrix truth fields | MatrixTruthProjection snapshot | AVAILABLE; full potential-outcome arrays remain intentionally excluded |
| SealedEvidence | Full typed snapshot includes rows, manifest and legacy digest; capture recomputes legacy digest and checks AnalyzerResult.input_sha256 | AVAILABLE IN MEMORY; package serializer must preserve rows and independently recompute the legacy digest after decoding |
| EvidenceCandidate | Exact per-run snapshot | AVAILABLE; retain as source record or document deterministic exclusion from package payload |
| Per-run EvaluationReport | Exact per-run snapshot | AVAILABLE |
| RepeatedAssignmentReport | One snapshot in each OuterWorldEvidenceBundle | AVAILABLE; exactly once per scenario/M |
| Evaluation-bank assignments | Exact per-run assignment snapshots | AVAILABLE; export ordering and bank fingerprint recomputation still required |
| Calibration seed manifest | Not an input to CapturedBenchmark or its driver | ABSENT — BLOCKER for RECONCILED provenance and Gate 164 package completeness |
| Source execution / workflow identity | Design contains declared executable commit only | EXTERNAL / ABSENT — GitHub-resolved workflow, run, attempt, artifact and tree/archive identity still required |
| Gate 159 reconciliation | No independent reconciliation artifact returned by CapturedBenchmark | ABSENT — BLOCKER |
| Technical test evidence | Test source exists; no executed workflow evidence was retrieved in this gate | EXTERNAL / NOT ESTABLISHED |
| Package manifest, file hashes, JCS and tar | No builder/verifier found in the inspected source module | ABSENT — OPEN |

## 4. Canonicalization boundary

The current `FrozenSnapshot.capture()` serializes a typed source object using a custom tagged representation (`$dataclass`, `$tuple`, `$map`, etc.) and Python `json.dumps(sort_keys=True, separators=...)`. Its SHA-256 is a **snapshot digest under that existing serialization**, not an RFC 8785 JCS digest.

The legacy SealedEvidence digest is independently calculated with the existing Sealer-compatible JSON serialization. The existing report fingerprint is calculated by the evaluator's legacy `_hash` path. These three semantics must remain separate:

1. `FrozenSnapshot.sha256`: integrity of the retained typed snapshot bytes.
2. `SealedEvidence.sha256`: legacy digest over exact sealed manifest+rows, recomputed after package decode using the legacy algorithm.
3. `report_fingerprint`: legacy report-level fingerprint, preserved exactly.
4. New JCS file digests, manifest digest and final archive SHA-256: package-layer digests only.

Do not relabel a snapshot digest, sealed digest or report fingerprint as a JCS digest. Do not change legacy hash algorithms to make them appear canonical under Gate 164.

A package adapter must define a stable, versioned data-only mapping for every snapshot type. Since snapshot payloads are bytes, their package representation must use an explicit binary encoding (e.g. base64 with encoding and media/schema labels) or a lossless typed expansion. JSON must not silently coerce bytes, enums, tuples, nulls or numbers. The decoded representation must restore the declared typed object and reproduce its legacy digest.

JCS applies to the package JSON files after this mapping; it does not retroactively redefine the capture snapshots.

## 5. Gate 164 v1.0.0 file mapping — no new path required

Keep the exact Gate 164 allowlisted paths. Clarify the payload envelope within `runs/run_records.json`:

- `schema_id`, `schema_version`, `benchmark_export_id`;
- ordered `run_evidence_records`, exactly 13×M×(1+R);
- ordered `outer_world_evidence_records`, exactly 13×M;
- `evidence_index`, exactly one (scenario, M, world) row per outer bundle;
- `repeated_assignment_reports` embedded once through their owning OuterWorldEvidenceBundle (no duplicate independent copy);
- declared cardinalities, ordering profile and join-key definitions;
- source snapshot digests and validation findings, explicitly marked as producer-side structural checks rather than independent reconciliation.

The run records preserve the exact source snapshots, including inline SealedEvidence rows and manifest, plus their existing legacy digest. The report remains a distinct file and is cross-checked against the envelope. The matrix used by the evaluator must be carried in `design/scenario_estimand_matrix.json` as the exact ordered object; it must not be reconstructed from the report.

The Gate 164 manifest continues to inventory only the exact package files and their final byte lengths/SHA-256 values. Its manifest digest and final archive digest remain non-circular as already defined in Gate 164 §7.

## 6. Required independent package verification

Before a package can be called STRUCTURALLY_VALID, the independent package verifier must:

1. Decode every typed snapshot using an allowlisted type registry and reject unknown type IDs/fields.
2. Verify each snapshot byte digest and exact type envelope.
3. Recompute every SealedEvidence legacy digest from decoded manifest+rows and compare it to both the retained source digest and AnalyzerResult.input_sha256.
4. Recompute structural ScenarioConfig and AnalysisContract legacy snapshot digests using their existing algorithms; separately compute package JCS file digests.
5. Recompute the exact matrix fingerprint under its existing algorithm and separately compute the JCS package digest.
6. Join each SeedAssignment to its RunManifest and config on the full Gate 166 key and all seed fields.
7. Verify one RUN plus contiguous R for every scenario/M; shared world identity within M; distinct world identity/seeds across M.
8. Join the complete RUN/R set one-to-one to the reduced temporal manifest and every pair-ledger M contribution to the designated RUN/world identity.
9. Verify exactly 52 unique pair keys and one contribution per declared M, retaining all missing/invalid/status classifications and denominators.
10. Reject omitted, duplicated, reordered or orphaned evidence records rather than repairing them from aggregate values.

Producer-side validation flags (including `validation_status`) are inputs to audit, never authoritative verifier outcomes.

## 7. Remaining blockers

- **Calibration manifest:** no actual calibration assignments or immutable retrieval reference enters the benchmark capture API. Evaluation-only capture cannot establish calibration/evaluation disjointness.
- **Gate 159:** evaluation seed-bank fingerprint, effective configuration fingerprint and executing source identity are not independently reconciled.
- **Source execution:** workflow/run/attempt/event/ref, full commit, source tree/tested archive digest and producer artifact identity must be independently resolved from GitHub.
- **Technical test evidence:** source tests are not proof of their execution; exact workflow run/commit/artifact metadata remains external.
- **JCS/tar:** no package writer or independent verifier is implemented.
- **Trusted attestation:** remains a separate later operation and must not be conflated with package integrity or scientific validity.

A package may be built for diagnostic transport only if the missing fields are explicitly UNAVAILABLE/CONDITIONAL and the package schema permits that state. It must not be described as Gate 164-compliant, RECONCILED or AUTHENTICATED while required evidence is absent.

## 8. Audit verdict

- Gate 165 report-only insufficiency: **RESOLVED AT SOURCE-CAPTURE LEVEL** by Gates 166–172; the report itself remains insufficient alone.
- RunEvidenceBundle and OuterWorldEvidenceBundle: **AVAILABLE IN SOURCE**, runtime unverified.
- Full SealedEvidence retention: **AVAILABLE IN SNAPSHOT SOURCE**, runtime/package round-trip unverified.
- Benchmark-wide co-export: **IMPLEMENTED IN SOURCE**, runtime unverified.
- Gate 164 file inventory: **REUSABLE WITHOUT ADDING PATHS**, with the explicit envelope structure above.
- JCS adapter and deterministic archive: **OPEN**.
- Calibration manifest and Gate 159 reconciliation: **BLOCKING** for RECONCILED status.
- External source/test metadata and trusted attestation: **OPEN**.
- Tests, CI, package generation and benchmark: **NOT EXECUTED**.

## 9. Next operation — Gate 174

Define the pure, non-executing serialization contract and independent verifier interface for the existing Gate 164 v1.0.0 package paths. Freeze exact typed snapshot encoding, the `runs/run_records.json` envelope schema, array ordering, digest recomputation sequence and fail-closed validation result model. Before implementation, decide whether the packager should reject incomplete calibration/source provenance entirely or permit a clearly non-reconciled diagnostic package profile. Do not execute or generate any package in this gate.

## 10. Gate 174 — serialization/verifier contract

Gate 174 resolves the open profile decision. Gate 164 v1.0.0 remains a fail-closed CONFIRMATORY package: absent calibration manifest, Gate 159 reconciliation, independently resolved GitHub producer/source metadata or required technical test evidence blocks acceptance. No placeholder manifest or producer-declared PASS is allowed. Any future partial diagnostic transport must use a different schema ID/version and cannot claim Gate 164 compliance, RECONCILED or AUTHENTICATED status.

The exact 14-file Gate 164 inventory remains unchanged. The existing `runs/run_records.json` path is specified as a versioned envelope of ordered RUN/R records, one outer-world record per scenario/M, one repeated aggregate report per M, evidence index, cardinalities and join keys. Source snapshots are transported as base64 of their exact existing bytes with type ID, serialization ID and SHA-256; package JSON receives separate JCS canonicalization.

Gate 174 also identifies a concrete decoder gap: current snapshot enum decoding returns the underlying value rather than restoring the enum type; arbitrary bytes are not supported by the snapshot encoder. A versioned allowlisted decoder must close this before claiming type-preserving round-trip.

The independent verifier's status vector and fail-closed behavior are defined. No code, tests, package or verifier was implemented/executed. See `C10_S_VCONT_PACKAGE_SERIALIZATION_AND_INDEPENDENT_VERIFIER_CONTRACT_GATE_174_DRAFT_001.md`. Next: Gate 175 static implementability audit.
