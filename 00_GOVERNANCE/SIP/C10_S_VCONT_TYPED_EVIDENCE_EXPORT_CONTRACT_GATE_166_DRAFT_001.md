# C10-S V_cont — Gate 166: typed evidence-export contract

**Status:** INTERFACE CONTRACT DEFINED; CAPTURE PRIMITIVES IMPLEMENTED; END-TO-END EXPORT OPEN  
**Branch:** research/c10-s-consolidation-draft  
**Depends on:** Gates 154, 159, 164 and 165  
**Scientific execution:** NOT AUTHORIZED  
**Code/tests/workflow/CI changes:** NOT PERFORMED

## 1. Decision

Freeze the minimum immutable, typed evidence-export interface required by Gate 164. The export is captured by the execution orchestrator while source objects coexist. It is not reconstructed later from aggregate report rows.

The export does not execute Generator, Sealer, Analyzer or Evaluator; derive seeds; perform calibration; or upgrade provenance. It is a data contract, not a package, attestation, scientific result or execution authorization.

The interface consists of a benchmark envelope, typed run records, configuration registries, exact seed manifests, producer execution claims and a deterministic export manifest.

## 2. Schema and cardinalities

- Schema ID: TGCV-C10S-VCONT-EVIDENCE-EXPORT.
- Schema version: 1.0.0.
- One export represents one benchmark design identity: scenario versions, N, M, R, matrix/estimand versions, metric targets and evaluation bank.
- For the current 13-scenario design at one N: exactly 13 × M × (1 + R) run records.
- For every (scenario_id, scenario_version, N, outer_replicate_id): exactly one RUN (assignment_index=-1) and R REPEATED_ASSIGNMENT records (indices 0..R-1).
- The current authoritative matrix contains exactly 52 unique scenario-estimand pairs.
- ScenarioConfig structural registry: one per (scenario_id, scenario_version, N), unless the design explicitly versions a structural change.
- Each run retains an exact per-run ScenarioConfig binding, including assignment-specific seeds and identity fields.
- AnalysisContract objects may be deduplicated by content digest, but every run references its exact contract.
- Calibration manifest has its own design, namespace, materialized rows and cardinality. Do not infer its size from the evaluation bank.
- Technical test evidence is a separate external reference class; never count it as a scientific benchmark run.

These cardinalities are checked against the declared design, not inferred from observed records.

## 3. Benchmark envelope

Required fields:

| Field | Contract |
|---|---|
| schema_id / schema_version | Exact constants above |
| export_id | Deterministic digest-derived ID; no timestamp/random component |
| benchmark_design | Exact MonteCarloBenchmarkDesign fields and source schema/version |
| scenario_estimand_matrix | Exact ordered 52 ScenarioEstimandSpec records used by Evaluator |
| scenario_config_registry | Structural ScenarioConfig projections keyed by canonical digest |
| analysis_contract_registry | Exact AnalysisContract records keyed by canonical digest |
| evaluation_seed_bank | Exact ordered materialized SeedAssignment rows, bank and namespace |
| calibration_seed_bank | Exact calibration rows or immutable retrievable manifest and availability evidence |
| run_evidence_records | Exactly one record per declared scenario × M × (RUN + R) |
| producer_execution_claims | Producer assertions about repo/ref/commit/workflow/run/attempt/artifact; untrusted until reconciled |
| technical_test_evidence_refs | Separate references to technical test runs, not scientific benchmark runs |
| export_manifest | Record inventory, cardinalities, ordered IDs, per-record hashes and validation inputs |

Unknown values remain explicit null/status values where allowed. Missing required evidence blocks a valid export; no guessed values.

## 4. RunEvidenceRecord v1.0.0

One record per execution, keyed by scenario/version/N/M/role/R-index/run.

### 4.1 Identity and assignment

Retain:
- scenario_id, scenario_version, n_units;
- outer_replicate_id (M);
- assignment_role (RUN or REPEATED_ASSIGNMENT);
- assignment_index (-1 for RUN; 0..R-1 for repeated);
- replicate_id (legacy string; separate from M and R);
- run_id, world_id, world_version, generator_version;
- references to exact SeedAssignment, ScenarioConfig and AnalysisContract records.

Do not overload replicate_id as M or R.

### 4.2 Exact SeedAssignment

Serialize every source field: bank, scenario_id, scenario_version, n_units, replicate, world_seed, z_assignment_seed, g_assignment_seed, outer_replicate_id and assignment_role. Serialize assignment_index as an explicit equality check against replicate; it is not a second identifier.

### 4.3 Complete RunManifest

Serialize every source field, including defaults and nulls:
- run_id, scenario_id, version, n_units, n_intervals;
- window_start, window_end, interval_width, generator_version;
- world_id, world_version, replicate_id;
- G and Z assignment mechanism IDs, versions and hashes;
- G reference-regime ID/version;
- Z/G assignment-vector hashes;
- G assignment probability by stratum;
- world/Z/G seeds;
- outer_replicate_id, assignment_role, assignment_index.

This is the complete typed RunManifest, not the Evaluator's reduced temporal-manifest projection.

### 4.4 ScenarioConfig: structural projection and per-run binding

Preserve two linked objects.

1. Structural projection: all scientific/DGP/Generator parameters, excluding only execution identity and seed-stream fields: seed, world_seed, z_assignment_seed, g_assignment_seed, replicate_id, outer_replicate_id, assignment_role and assignment_index. It includes scenario/version/profile/mechanism, N/intervals, temporal support, probabilities, effects, randomization/support/interference/measurement/version flags and interactions.
2. Per-run binding: exact full source ScenarioConfig fields, including the excluded seed and execution identity fields, linked to the run record.

This exclusion list is closed and versioned. No scientific parameter may be removed from the structural projection.

### 4.5 Matrix-relevant TruthBundle projection

Retain the exact fields consumed by the frozen matrix:
- run_id;
- itt_z_run_truth, itt_g_z0_truth, itt_z_mechanism_truth, itt_z_reference_truth;
- outer_replicate_id, assignment_role, assignment_index;
- g_reference_regime_id/version;
- G/Z assignment mechanism hashes;
- seed.

Retain theta_a_truth explicitly as null/value without coercion. It is not an estimand in the current 52-pair matrix; its presence does not authorize scoring.

Do not serialize full potential-outcome arrays in v1.0.0 by default. They are outside the minimum matrix truth projection. If later required, add a separately versioned extension. Do not claim an omitted array is independently inspectable merely because a digest is supplied.

### 4.6 SealedEvidence

Retain run_id, exact SealedEvidence manifest, sha256, row count and declared serialization/schema version. Require exact equality between SealedEvidence sha256 and AnalyzerResult.input_sha256.

Raw sealed rows are excluded by default. The manifest/digest can be RECONCILED only if the canonical sealed representation is retrievable by the verifier or backed by an immutable retrievable evidence object. A digest alone is DECLARED/UNVERIFIABLE, not recomputable.

### 4.7 AnalyzerResult and EvaluationReport

Retain the complete typed AnalyzerResult: run/estimand identities and versions; package and G statuses, estimates and SEs; first-stage ΔT_acc vector; abstention reasons; input/output/provenance hashes; target regime/outcome identities; reference-regime status/estimate; Z/G mechanism IDs, versions and hashes; transportability fields; outer M, role and assignment index.

Retain the exact per-run EvaluationReport: run_id, package/G absolute errors, package/G recovery flags, expected-abstention flag, notes, reference status correctness and estimate-presence flags.

For each M, retain exactly one RepeatedAssignmentReport with world_id, replicate_count, mechanism estimate/truth/error/recovery, reference truth/estimate/error/recovery/identification status and ordered per-run reports. The designated RUN EvaluationReport remains separate from the repeated aggregate report.

## 5. Join keys and invariants

### 5.1 Primary key

K_run = (scenario_id, scenario_version, n_units, outer_replicate_id, assignment_role, assignment_index, run_id). It must be unique.

### 5.2 SeedAssignment ↔ RunManifest

Join on scenario ID/version, N, outer ID, role, assignment index ↔ replicate, and exact equality of world/Z/G seeds. RunManifest has no bank field: bank is verified through the exact SeedAssignment row and benchmark bank identity. Do not invent a RunManifest bank property.

### 5.3 RunManifest ↔ ScenarioConfig

Require exact equality for scenario/version/N, intervals and temporal support, assignment seeds, outer ID, role, assignment index and replicate_id. Recompute the structural projection digest. Verify Generator version and resulting world/run identities using the versioned identity algorithm and corresponding source implementation.

### 5.4 TruthBundle ↔ run

Require run_id, M, role and assignment index equality. Each matrix truth field must match its declared source. Never infer truth from AnalyzerResult or report output. Preserve theta_a_truth=null.

### 5.5 AnalyzerResult / SealedEvidence ↔ run

Require run_id and assignment identity equality. AnalyzerResult.input_sha256 must equal SealedEvidence.sha256. Retain output_sha256 and provenance_sha256 under their own semantics; do not substitute them for package digests.

### 5.6 M/R structure

For each scenario/M: one RUN with index -1; R unique repeated rows 0..R-1; one shared world_id/world_version/world_seed; unique run IDs and assignment-specific Z/G seeds. Distinct M values have distinct world IDs and world seeds within scenario/version/N/evaluation bank. RUN and R remain separate.

### 5.7 Calibration/evaluation separation

Materialize both manifests or use immutable manifests retrievable by the verifier. Recompute disjointness across world/Z/G seed streams. Verify bank labels, namespace, derivation algorithm ID/version and inputs. Recompute the legacy seed-bank fingerprint for compatibility and a separate JCS package digest. If calibration rows cannot be retrieved, separation is UNVERIFIABLE and package provenance cannot be RECONCILED.

## 6. Provenance separation

Producer execution claims may include repository, ref, commit, workflow path, run ID/attempt, event, artifact ID/name/digest, source tree/archive digest and runtime/dependency-lock identity. They are DECLARED only.

The independent attestor/verifier resolves repository, workflow, run, attempt, commit and artifact metadata from GitHub and compares them with producer claims. The producer cannot self-assert RECONCILED or AUTHENTICATED.

Technical tests are separately bound to exact workflow run, attempt, tested commit and artifact. A test run is not a scientific benchmark run. Test source files alone are not test execution evidence.

## 7. Export validation status

- STRUCTURALLY_VALID: schema, cardinality and local joins pass.
- RECONCILED: structural validation passes; seed/config/source evidence is recomputed; calibration/evaluation separation is verifiable; GitHub-resolved run/artifact identity matches.
- CONDITIONAL: explicit unresolved fields remain; never call it reconciled.
- BLOCKED: required evidence missing, duplicate, contradictory or unverifiable.
- AUTHENTICATED is not an export status; reserved for independent attestation verification.

The validator computes statuses. Caller-supplied PASS booleans cannot override failed checks. Failed records remain in the validation ledger and are never silently filtered.

## 8. Mapping to Gate 164

| Gate 164 file | Gate 166 source |
|---|---|
| report/report.json | Evaluator report, pair records and source references |
| design/benchmark_design.json | Exact benchmark design |
| design/scenario_estimand_matrix.json | Exact 52-row matrix |
| design/effective_scenario_configs.json | Structural config registry plus per-run bindings |
| design/analysis_contracts.json | Deduplicated registry plus per-run references |
| seeds/evaluation_seed_assignments.json | Exact evaluation seed manifest |
| seeds/calibration_seed_manifest.json | Exact calibration manifest and design metadata |
| runs/temporal_manifest.json | Full RunManifest projection |
| runs/run_records.json | RunEvidenceRecords and M-level repeated reports |
| provenance/source_execution.json | Producer claims plus separately resolved attestor metadata |
| provenance/configuration_fingerprints.json | Recomputed config, contract, matrix and seed fingerprints |
| validation/reconciliation_results.json | Independent Gate 159/export validator results |
| validation/test_evidence.json | External technical workflow references and resolved metadata |

Package manifest/archive digests are constructed only after export validation and do not alter source evidence records.

## 9. Future implementation acceptance criteria

1. Exact round-trip of typed source objects, defaults and nulls.
2. Deterministic structural ScenarioConfig projection and exact per-run binding.
3. Deduplicated AnalysisContract registry with mandatory per-run references.
4. Full SeedAssignment/RunManifest join, RUN=-1 and R=0..R-1.
5. Matrix-truth binding and theta_A null preservation.
6. SealedEvidence digest/input binding; no recomputation claim without retrievable canonical evidence.
7. AnalyzerResult and EvaluationReport identity binding.
8. Exactly one repeated aggregate report per M; no R-to-M promotion.
9. Exact declared cardinalities and 52-pair matrix.
10. Calibration/evaluation disjointness recomputed from actual manifests.
11. Producer claims remain DECLARED until GitHub resolution.
12. TRUTH_MISSING and INVALID_OUTPUT remain distinct from abstention.
13. Reject tampering, duplicate/orphan rows, seed mismatch, wrong role/index, cross-M reuse, wrong truth source, null coercion and fake provenance.
14. Structured validation failures; no silent filtering.

## 10. Gate 166 status

- Benchmark envelope: DEFINED.
- RunEvidenceRecord v1.0.0: DEFINED.
- ScenarioConfig structural projection/per-run binding: DEFINED.
- AnalysisContract registry cardinality: DEFINED.
- SeedAssignment and complete RunManifest join: DEFINED.
- Matrix-relevant TruthBundle projection and theta_A null: DEFINED.
- SealedEvidence digest and AnalyzerResult input binding: DEFINED; recomputation conditional on retrievable canonical evidence.
- EvaluationReport and repeated M report cardinalities: DEFINED.
- Calibration manifest requirements: DEFINED.
- Producer/external provenance split: DEFINED.
- RunEvidenceBundle capture primitives: IMPLEMENTED (Gate 170).\n- Producer/orchestration integration, full export validator and package implementation: OPEN.
- Gate 159 reconciliation implementation: OPEN.
- Packager implementation: OPEN pending export.
- Tests: NOT RUN.
- Scientific execution/calibration/seed generation/N/R/M sizing/Monte Carlo: NOT AUTHORIZED / NOT EXECUTED.
- main unchanged; PR #116 remains Draft on its existing base.

## 11. Next gate

**Gate 171 — producer/orchestration integration.** Wire the Gate 170 capture API into the execution path that holds the exact SeedAssignment and all source objects through Evaluator.evaluate; assemble one OuterWorldEvidenceBundle per M without reconstructing source objects from reduced aggregate tuples.


## 12. Gate 167 source-boundary audit qualification

Gate 167's static source-boundary audit is recorded in:
`00_GOVERNANCE/SIP/C10_S_VCONT_EVIDENCE_EXPORT_SOURCE_BOUNDARY_AUDIT_GATE_167_DRAFT_001.md`.

The source objects required by this contract are constructed by Generator, Sealer, Analyzer and Evaluator, but the existing Monte Carlo interface reduces each run to `(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)`. It therefore does not retain ScenarioConfig, SeedAssignment or SealedEvidence. The export must be captured by a typed RunEvidenceBundle at the orchestration boundary before that reduction; the Evaluator report must not be used to reconstruct omitted source objects.

**SealedEvidence clarification:** SealedEvidence currently retains canonical rows and manifest in memory, and Sealer computes its digest over both. The digest is therefore recalculable at capture time. If raw rows are excluded from the package, RECONCILED status additionally requires an immutable, independently retrievable canonical evidence object and verified locator. The current code does not provide that durable retrieval abstraction. Without it, digest status remains UNVERIFIABLE.

The Gate 166 schema remains DEFINED. Implementation is conditional on Gate 168 freezing RunEvidenceBundle and sealed-evidence retention/retrieval. This qualification does not imply code or test execution.

## 13. Gate 168 amendment — SealedEvidence retention and world identity

Gate 168 is persisted in `00_GOVERNANCE/SIP/C10_S_VCONT_RUN_EVIDENCE_BUNDLE_AND_SEALED_EVIDENCE_RETENTION_CONTRACT_GATE_168_DRAFT_001.md`.

For the v1.0.0 export implementation, the default exclusion of raw SealedEvidence rows is amended: the complete canonical manifest and rows are retained inline. The current repository has no immutable independently retrievable evidence store; a digest-only export would therefore be UNVERIFIABLE after capture. The legacy Sealer digest remains unchanged and is recomputed from its exact legacy canonical payload. The package-level JCS representation and digest remain separate.

Gate 168 also defines the frozen RunEvidenceBundle and OuterWorldEvidenceBundle. Implementation acceptance is blocked pending correction of the Generator world-identity projection: current `world_spec` retains `assignment_role` and `assignment_index`, so role/index changes alter `world_id` despite Gate 154 requiring RUN and R to share one world. See Gate 168 §7. This is a source-level finding; no runtime test was run in Gate 168.


## 14. Gate 170 implementation mapping — immutable capture API

Gate 170's source implementation is recorded in `C10_S_VCONT_RUN_EVIDENCE_BUNDLE_CAPTURE_IMPLEMENTATION_GATE_170_DRAFT_001.md` and `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`.

The new `RunEvidenceBundle.capture(...)` accepts the exact SeedAssignment and all source objects while they coexist, validates the per-run identity/provenance/contract joins, snapshots the full ScenarioConfig and complete RunManifest, retains EvidenceCandidate and complete SealedEvidence, stores the Gate 166 `MatrixTruthProjection` only (not potential-outcome arrays), and captures AnalysisContract, AnalyzerResult and EvaluationReport. FrozenSnapshot uses canonical typed envelopes and immutable bytes; its payload digest is checked on restore. SealedEvidence legacy digest is recomputed from retained manifest+rows and must equal AnalyzerResult.input_sha256.

`OuterWorldEvidenceBundle.capture(...)` checks one RUN, exactly R ordered repeated indices, shared M/world identity, bank/design identity, unique run IDs and assignment-specific Z/G seeds, plus exact ordered repeated reports.

**Qualification:** this is a standalone capture API, not yet wired into the existing benchmark producer. The existing Monte Carlo path still consumes reduced four-object tuples. Regression source is persisted but NOT EXECUTED. End-to-end export remains OPEN; no execution or scientific claim follows from the implementation.


## 15. Gate 171 — M-level producer/orchestration integration

Gate 171 implements the explicit M-level producer boundary in `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`:

- `produce_and_capture_outer_world(...)` consumes exact pre-materialized evaluation-bank SeedAssignment rows and a matching structural ScenarioConfig template;
- it validates one RUN and exactly R contiguous repeated assignments, rejecting cross-M/world/scenario/N/bank groups before generation;
- it executes the existing Generator → Sealer → Analyzer → Evaluator sequence in source code and captures each complete RunEvidenceBundle before source objects are discarded;
- it constructs exactly one OuterWorldEvidenceBundle for the M group;
- it returns the unchanged legacy four-object tuples in RUN, R=0..R-1 order for compatibility with existing MC aggregation.

No Generator/Sealer/Analyzer/Evaluator method semantics or 52-pair ledger logic were changed. The API is defined and persisted but has NOT been called in this gate. Three regression tests were added and NOT EXECUTED.

**Remaining:** there is no benchmark-wide 13-scenario driver yet. The caller must still partition exact evaluation assignments, call the M producer for every scenario/M, assemble `scenario_outer_runs`, invoke `evaluate_monte_carlo_benchmark()` once and co-return the evidence bundles with the 52-pair result. This is Gate 172. Gate 159, package writer and trusted attestation remain OPEN.
