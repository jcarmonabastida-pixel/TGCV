# C10-S V_cont — Gate 168: RunEvidenceBundle and SealedEvidence retention contract

**Status:** CONTRACT DEFINED; SOURCE BLOCKER SUPERSEDED BY GATE 169; CAPTURE API IMPLEMENTED BY GATE 170; ORCHESTRATION INTEGRATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Depends on:** Gates 154, 159, 164, 165, 166 and 167  
**Scientific execution:** NOT AUTHORIZED  
**Code/tests/workflow/CI changes:** NOT PERFORMED

## 1. Purpose and disposition

Freeze the minimum per-run evidence carrier and the retention rule needed to implement the Gate 166 export without reconstructing source objects from aggregate reports.

Gate 168 is a data-contract and source-integrity operation. It does not authorize seed-bank generation, calibration, N/R/M sizing, benchmark execution, Monte Carlo execution or scientific execution.

**Historical Gate 168 finding, superseded:** this gate initially reported that the Generator world-identity projection retained `assignment_role` and `assignment_index`. Gate 169 re-read the current branch source and withdrew that finding; the current projection excludes both fields. Gate 170 subsequently implemented the standalone immutable capture API. The remaining implementation gap is end-to-end producer/orchestration integration, not the world-identity projection.

## 2. Historical reconciliation

- Gate 166 defines the benchmark envelope and exact RunEvidenceRecord fields/cardinalities.
- Gate 167 identifies the orchestration boundary as the only valid capture point and confirms that SealedEvidence rows and manifest are available in memory at capture.
- Gate 154 requires one fixed world per M, shared by RUN and R, with independent worlds across M.
- Gate 159 requires exact one-to-one SeedAssignment/RunManifest reconciliation and calibration/evaluation disjointness from materialized manifests.

Gate 168 reuses these contracts. It does not redefine the estimands, matrix, 52-pair coverage, truth semantics, temporal classifications or M/R hierarchy.

## 3. RunEvidenceBundle v1.0.0

Schema ID: `TGCV-C10S-VCONT-RUN-EVIDENCE-BUNDLE`; version: `1.0.0`.

One immutable bundle is captured for every designated RUN or REPEATED_ASSIGNMENT execution, immediately after Evaluator.evaluate returns and before the source objects leave the orchestration scope.

The logical record contains:

1. Exact benchmark/bank identity and the exact canonical SeedAssignment row.
2. Full ScenarioConfig snapshot, plus the Gate 166 structural projection and its independently recomputed digest.
3. Complete RunManifest snapshot, preserving every field/default/null.
4. Matrix-relevant TruthBundle projection as frozen by Gate 166; `theta_a_truth` remains explicit null/value and is not made scoreable.
5. Exact SealedEvidence manifest, rows, row count, legacy digest and serialization identity.
6. Exact AnalysisContract snapshot and its content-addressed registry reference.
7. Complete AnalyzerResult snapshot, including input/output/provenance hashes and all M/R identities.
8. Exact EvaluationReport returned for that run.
9. Capture schema/version and local structural-validation results. Caller-supplied PASS booleans are not accepted as validation evidence.

The primary key remains Gate 166's:
`K_run = (scenario_id, scenario_version, n_units, outer_replicate_id, assignment_role, assignment_index, run_id)`.

No list position, dictionary insertion order or inferred relationship may substitute for an explicit identity.

### 3.1 Deep immutability

A frozen Python dataclass alone is insufficient because nested dictionaries/lists remain mutable.

The implementation must snapshot mutable source objects at capture into immutable canonical byte payloads (or an equivalently deep-immutable representation) and retain explicit schema/version/type identifiers. The bundle's identity fields must be scalar immutable values. Mutating any source object after capture must not mutate the bundle.

The source snapshots must round-trip to the exact declared typed objects, preserving defaults and nulls. Unsupported values, NaN and infinities fail closed.

### 3.2 Capture timing

The capture order is:

1. Resolve the exact SeedAssignment row selected by the bank manifest.
2. Construct and validate the full ScenarioConfig.
3. Call Generator; retain RunManifest, TruthBundle and EvidenceCandidate long enough to seal.
4. Call Sealer; retain the complete SealedEvidence.
5. Call Analyzer; retain AnalyzerResult.
6. Call Evaluator; retain its exact EvaluationReport.
7. Snapshot and validate the RunEvidenceBundle before leaving the orchestration scope.
8. Only after successful capture may transient EvidenceCandidate objects be released.

The Evaluator aggregate output must never be used to reconstruct omitted source records.

## 4. SealedEvidence retention decision

**Decision: include the complete canonical SealedEvidence manifest and rows in the evidence export/package for schema v1.0.0.**

Rationale:

- The current source has no durable content-addressed evidence store or independently retrievable locator abstraction.
- A digest-only record cannot be independently recomputed after rows are discarded.
- Inventing an external storage locator would create an unimplemented dependency and a false verification claim.
- The rows are synthetic benchmark evidence, not an authorized real-world personal-data store.
- Including the exact rows is the smallest verifiable implementation and avoids a new storage trust boundary.

The export must preserve both:
- the exact legacy Sealer payload used by the current digest algorithm, `json.dumps(..., sort_keys=True, separators=(",", ":"), allow_nan=False)` over `{"manifest": manifest, "rows": rows}`; and
- the Gate 164 package's separately versioned RFC 8785 JCS representation.

These digests have different semantics and must not be substituted for one another. The existing SealedEvidence SHA-256 must be recomputed from the retained canonical legacy payload and match exactly before export acceptance. The final package digest is computed separately after package construction.

This decision amends Gate 166's default exclusion of raw SealedEvidence rows for this v1.0.0 implementation. Future externalization requires a separately governed immutable storage/retrieval contract and independent retrieval tests; a locator string alone is insufficient.

## 5. OuterWorldEvidenceBundle

Schema ID: `TGCV-C10S-VCONT-OUTER-WORLD-EVIDENCE-BUNDLE`; version: `1.0.0`.

One outer-world bundle groups:
- exactly one RUN RunEvidenceBundle with assignment index `-1`;
- exactly R REPEATED_ASSIGNMENT RunEvidenceBundles with indices `0..R-1`;
- exactly one RepeatedAssignmentReport generated after the complete R set passes identity/cardinality checks;
- one shared `outer_replicate_id`, `world_id`, `world_version` and `world_seed`;
- distinct run IDs and assignment-specific Z/G seeds under the Gate 154 stream contract.

The designated RUN EvaluationReport remains separate from the repeated-assignment aggregate. Per-R EvaluationReports remain nested in the RepeatedAssignmentReport and are not counted a second time.

Across M, distinct outer identities must have distinct world seeds and world IDs within the same bank × scenario/version × N. RUN and R are not independent M observations.

## 6. Mandatory joins and fail-closed checks

Before a bundle is accepted:

1. SeedAssignment ↔ ScenarioConfig: exact scenario/version/N/M/role/index and seed equality.
2. SeedAssignment ↔ RunManifest: exact one-to-one match on bank/scenario/version/N/M/role/index and world/Z/G seeds. RunManifest does not gain a synthetic bank field.
3. RunManifest ↔ TruthBundle: exact run/M/role/index and truth-source binding.
4. RunManifest ↔ SealedEvidence: run/world/M/role/index and manifest provenance equality.
5. SealedEvidence ↔ AnalyzerResult: exact run identity and recomputed digest equality with AnalyzerResult.input_sha256.
6. AnalysisContract ↔ AnalyzerResult: exact estimand, version, mechanism, regime, outcome and transportability identities.
7. AnalyzerResult ↔ EvaluationReport: exact run identity and exact capture of the Evaluator return value.
8. Bundle set ↔ declared design: exact cardinality, uniqueness, no orphan/duplicate/missing records and no cross-M reuse.
9. Calibration/evaluation separation: recompute from materialized or independently retrievable manifests across every seed stream.
10. Preserve distinct `TRUTH_MISSING`, `INVALID_OUTPUT`, abstention and status-only classifications and all original denominators.

Any failed or unverifiable join blocks the affected export. No record is silently filtered, repaired from aggregate values, coerced to zero or converted into an Analyzer abstention.

## 7. Historical source discrepancy — superseded by Gate 169

At Gate 168, the source inspection was reported as showing the following:

- `world_spec = asdict(cfg)`;
- the current removal list excludes `seed`, `world_seed`, `z_assignment_seed`, `g_assignment_seed` and `replicate_id`;
- it does **not** exclude `assignment_role` or `assignment_index`;
- `world_id` hashes `world_seed`, `outer_replicate_id` and this `world_spec`.

Because RUN and REPEATED_ASSIGNMENT have different role/index values, their world identity projection differs even when their intended exogenous world and world seed are shared. This contradicts Gate 154 §§2–4 and its acceptance test requiring all assignments within one M to share one world identity.

Gate 167's description of the projection as removing role/index is therefore corrected by this Gate 168 finding. Gate 155's historical implementation/CI record is not erased; its scope is qualified by this newly identified source-level invariant gap.

**Historical required correction (withdrawn by Gate 169):** the proposed projection correction is not required for the current branch source. Gate 169 records the actual current projection and strengthens the regression. Its deterministic checks include:
- RUN and every R assignment in the same M have the same world_id and world_seed;
- distinct M values have distinct world IDs and world seeds;
- changing role/index alone does not change world identity;
- changing the DGP/world-defining configuration or M/world seed does change world identity;
- run_id remains unique across RUN and R.

Do not treat this historical finding as a current blocker. See Gate 169 for the superseding source audit and regression status.

## 8. Compatibility and non-goals

- Do not change Generator/Sealer/Analyzer/Evaluator scientific semantics to satisfy export.
- Prefer a new orchestration/export module and frozen carrier.
- Preserve the legacy SealedEvidence hash algorithm; JCS is a separate package layer.
- Preserve Gate 154 meanings of N, R and M and Gate 166's 52-pair matrix.
- Do not export full potential-outcome arrays by default.
- Do not add a new evidence store or signer workflow in this gate.
- Do not claim RECONCILED or AUTHENTICATED provenance from producer declarations.
- Do not change main, RMA, Evidence→Claim Matrix, STATUS, C09, Core or claim statuses.

## 9. Acceptance criteria for the later implementation

1. RunEvidenceBundle is deeply immutable and round-trips every required source snapshot.
2. Exactly one bundle exists for every declared RUN/R assignment.
3. All Gate 166 identity and join invariants pass.
4. SealedEvidence rows and manifest are retained in the v1.0.0 export.
5. Legacy SealedEvidence digest is independently recomputed and matches AnalyzerResult.input_sha256.
6. JCS package representation is separately deterministic.
7. OuterWorldEvidenceBundle contains exactly one RUN, R repeated assignments and one repeated aggregate report.
8. RUN/R share the same world identity; distinct M worlds are independent.
9. Calibration/evaluation disjointness is recomputed from actual manifests.
10. Adversarial tests reject mutation after capture, tampering, duplicate/orphan rows, wrong bank, seed mismatch, role/index mismatch, cross-M reuse, digest mismatch and missing evidence.
11. Gate 157 TRUTH_MISSING / INVALID_OUTPUT regression and denominators remain unchanged.
12. Technical tests are run only under the applicable technical authorization; no calibration or scientific benchmark is implied.

## 10. Gate 168 status and next operation

- RunEvidenceBundle v1.0.0: DEFINED.
- OuterWorldEvidenceBundle v1.0.0: DEFINED.
- SealedEvidence retention: INLINE CANONICAL ROWS SELECTED.
- Gate 166 raw-row exclusion default: AMENDED FOR THIS PACKAGE VERSION.
- Gate 167 source-boundary audit: QUALIFIED BY WORLD-IDENTITY DISCREPANCY.
- World-identity implementation invariant: BLOCKED / CORRECTION REQUIRED.
- Export orchestrator and packager: NOT IMPLEMENTED.
- Gate 159 reconciliation: OPEN.
- Tests/runtime/CI: NOT RUN IN THIS GATE.
- Calibration, seed-bank generation, N/R/M sizing, Monte Carlo and scientific execution: NOT AUTHORIZED / NOT EXECUTED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

**Next operation:** prepare the minimal source correction and compatibility test design for the world-identity projection, then implement the carrier/orchestrator only after the corrected identity invariant is verified. Preserve all existing scientific contracts and keep execution strictly technical; no scientific experiment is authorized.
## 11. Gate 169 supersession — world identity blocker withdrawn

Gate 169's static reinspection of the current branch source found that `Generator.generate()` already removes both `assignment_role` and `assignment_index` from `world_spec` before computing `world_id`. The Gate 168 §7 finding that these fields remained in the current projection was incorrect and is withdrawn. The earlier blocker is closed at static-source level; no Generator source correction is required based on that finding.

The existing regression `test_outer_replicate_identity_propagates_and_separates_worlds` already checked RUN/R shared world identity and separation across M. Gate 169 strengthens it to isolate role/index changes, assert run-ID distinction, isolate DGP-parameter changes and assert different world seeds across M. The strengthened test source has been persisted but NOT EXECUTED. No runtime PASS or CI claim is made.

This supersession does not close Gate 159 seed-bank reconciliation, establish cryptographic provenance, or implement RunEvidenceBundle. Gate 168's schema, deep-immutability requirements and inline SealedEvidence retention decision remain operative. See `C10_S_VCONT_WORLD_IDENTITY_INVARIANCE_AUDIT_GATE_169_DRAFT_001.md`.


## 12. Gate 170 implementation update and Gate 169 supersession

Gate 169 withdrew the Gate 168 source-level world-identity blocker: current Generator source excludes `assignment_role` and `assignment_index` from the world identity projection. Gate 170's current implementation does not modify Generator.

Gate 170 implements the Gate 168 data contract as a standalone capture API in `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`. It provides deeply immutable canonical typed snapshots, per-run joins and digest checks, the Gate 166 matrix-only truth projection, inline SealedEvidence rows+manifest, and an OuterWorldEvidenceBundle cardinality/identity validator. Details and source-level limitations are recorded in `C10_S_VCONT_RUN_EVIDENCE_BUNDLE_CAPTURE_IMPLEMENTATION_GATE_170_DRAFT_001.md`.

**Important qualification:** the capture API is not yet called by the existing benchmark orchestration; the latter still uses reduced four-object tuples. Thus Gate 168's contract is IMPLEMENTED AS A CAPTURE PRIMITIVE, not end-to-end integrated. The regression source is persisted but NOT EXECUTED. Gate 159, producer integration, package creation and external provenance remain OPEN. The earlier §1/§7 world-identity blocker statements are superseded by Gate 169 and must not be treated as current findings.


## 13. Gate 171 — M-level producer boundary implemented

The Gate 170 standalone capture API is now called by an explicit M-level producer/orchestration function: `produce_and_capture_outer_world(...)` in `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`.

For one scenario/N/M group, it consumes the exact evaluation SeedAssignment rows, applies their three seed streams and M/R identity to a copy of the structural ScenarioConfig template, invokes the existing Generator, Sealer, Analyzer and Evaluator in order, captures each RunEvidenceBundle while all source objects coexist, computes one repeated-assignment report, and creates one OuterWorldEvidenceBundle. It also returns the existing four-object evaluator tuples unchanged.

Thus the Gate 168/170 implementation is now integrated at the **single-M producer boundary**, not merely available as a disconnected capture primitive. The benchmark-wide 13-scenario driver and 52-pair evidence co-export remain OPEN and are the next Gate 172 operation. The source regression tests are persisted but NOT EXECUTED. No runtime PASS or benchmark execution is claimed.


## 14. Gate 172 — benchmark-wide bundle composition

Gate 172 now composes the Gate 168/170 RunEvidenceBundle and OuterWorldEvidenceBundle into a complete benchmark-level result. For every one of the 13 registered scenarios and every declared M, the driver captures one M bundle and joins all its RUN/R legacy evaluator tuples to the exact source snapshots. The final `CapturedBenchmark` co-returns the unchanged 52-pair evaluator report, temporal manifest, evidence bundles and evidence index.

The source-level benchmark-wide capture boundary is implemented. No execution has been performed. Serialization of the full benchmark envelope into the canonical package and Gate 159 external provenance reconciliation remain open. See Gate 172.

## 15. Gate 173 — package serialization boundary

Gate 173 confirms that the Gate 170 typed snapshots retain the complete SealedEvidence rows and manifest in source memory, and Gate 172 returns one OuterWorldEvidenceBundle per scenario/M. The complete source evidence is now available for a future package adapter; it has not yet been serialized into the Gate 164 archive or independently round-tripped.

The current FrozenSnapshot bytes use a custom tagged Python JSON representation and a snapshot-specific SHA-256. This is not RFC 8785 JCS. Preserve it as the source-snapshot integrity layer. A package adapter must losslessly encode/decode snapshot bytes and restore the declared typed objects; then independently recompute the legacy SealedEvidence digest from restored rows+manifest and compare it with AnalyzerResult.input_sha256. JCS digests are a separate package layer and must not replace snapshot, SealedEvidence or report fingerprint semantics.

The Gate 164 `runs/run_records.json` path can carry the complete ordered RunEvidenceRecord and OuterWorldEvidenceBundle envelope; no new archive path is needed. Gate 159 reconciliation, actual calibration manifest availability, external workflow/source identity and package verifier remain open. See Gate 173. No tests or runtime/package execution occurred.

## 16. Gate 174 — snapshot transport contract

Gate 174 specifies transport of each FrozenSnapshot as base64 of its exact retained `canonical_bytes`, plus the exact type ID, serialization ID and SHA-256. The source snapshot bytes and their digest remain unchanged; package JCS applies only to the containing package JSON. The verifier must validate base64, byte digest, allowlisted type/schema and restore the typed source before recomputing the legacy SealedEvidence digest from exact rows+manifest.

A concrete source limitation is recorded: current `_decode` returns enum underlying values rather than restoring registered enum types, and `_encode` rejects arbitrary bytes. The future adapter therefore needs a versioned allowlisted decoder and fail-closed handling of unsupported values; no universal type-preserving round-trip is claimed yet.

The Gate 164 confirmatory profile requires actual calibration manifest and Gate 159 reconciliation; diagnostic partial transport, if later specified, must have a distinct schema ID/version. See Gate 174. No serializer/verifier code or tests were executed.
