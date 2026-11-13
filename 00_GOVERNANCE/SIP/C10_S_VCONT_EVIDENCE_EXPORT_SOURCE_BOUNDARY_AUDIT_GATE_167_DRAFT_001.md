# C10-S V_cont — Gate 167: source-boundary and compatibility audit

**Status:** AUDITED — CONDITIONAL / EXPORT ORCHESTRATION NOT IMPLEMENTED  
**Branch:** research/c10-s-consolidation-draft  
**Depends on:** Gates 154, 159, 164, 165 and 166  
**Scientific execution:** NOT AUTHORIZED  
**Code/tests/workflow/CI changes:** NOT PERFORMED

## 1. Scope and method

Static inspection of:
- \`03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py\`;
- \`03_EXPERIMENTS/C10-S/harness/vcont_benchmark_protocol.py\`;
- \`03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py\`;
- \`03_EXPERIMENTS/C10-S/harness/test_vcont_benchmark_protocol.py\`;
- Gate 166 typed evidence-export contract.

This is a source-boundary audit, not runtime verification. No test, compile, workflow, calibration, seed generation or scientific benchmark was executed.

## 2. Executive finding

The component chain constructs nearly all source objects required by Gate 166, but the current Monte Carlo aggregation interface does not transport the complete object set to a durable export boundary.

The existing flow is:

\`ScenarioConfig → Generator.generate → (RunManifest, TruthBundle, EvidenceCandidate) → Sealer.seal → SealedEvidence → Analyzer.analyze → AnalyzerResult → Evaluator\`.

The source objects are available at their respective construction points. However, the current evaluator's Monte Carlo input rows are four-tuples:

\`(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)\`.

Consequently, \`ScenarioConfig\`, \`EvidenceCandidate\` and \`SealedEvidence\` are not retained by the Monte Carlo aggregation interface. The Evaluator's temporal manifest is a reduced projection, not a substitute for the complete source records.

**Decision:** Gate 166 is implementable only by introducing a typed per-run evidence carrier at the orchestration boundary, before these source objects are discarded. The Evaluator must not attempt to reconstruct missing objects from its aggregate output.

## 3. Field-to-construction-point map

| Gate 166 object/field | Actual source point | Current retention | Finding |
|---|---|---|---|
| Full ScenarioConfig | Caller constructs config; Generator receives it | Not present in current MC tuple | Must capture before Generator call |
| Structural config projection | Deterministically derivable from full ScenarioConfig | Generator derives a related \`world_spec\` for world identity, but no export registry exists | Reuse a versioned projection function; do not assume world_spec digest equals Gate 166 config digest |
| RunManifest | Generator.generate | Retained in current tuple | Complete typed object exists; temporal_manifest is only a projection |
| TruthBundle | Generator.generate | Retained in current tuple | Exact source object exists; export only matrix fields per Gate 166 |
| EvidenceCandidate | Generator.generate | Not retained in MC tuple | Transient source; not required in package if sealed evidence and provenance are captured |
| SealedEvidence | Sealer.seal | Not retained in MC tuple | Required capture point; rows and manifest are present in memory |
| AnalysisContract | contract_for/config-dependent caller | Retained in current tuple | Full object available, but no registry/export identity layer |
| AnalyzerResult | Analyzer.analyze | Retained in current tuple | Full typed result available |
| EvaluationReport | Evaluator.evaluate | Recomputed/created inside Evaluator | Must be returned or captured in the same run envelope; do not reconstruct from summary metrics |
| RepeatedAssignmentReport | Evaluator.evaluate_repeated_assignment | Created per M from R rows | Available at M aggregation boundary; retain exactly once per M |
| MonteCarloBenchmarkDesign | Caller constructs design | Passed to benchmark evaluator | Retain exact design and matrix object at export boundary |
| Evaluation SeedAssignment | build_seed_bank | Caller-owned; not passed to Generator/Evaluator as a typed row | Bind the exact selected row to each run before generation |
| Calibration SeedAssignment | build_seed_bank calibration plan | External to benchmark run tuples | Retain exact manifest separately; no inferred reconstruction |
| Producer workflow/artifact metadata | GitHub Actions/CI environment | Not supplied by Generator/Analyzer/Evaluator | Resolve independently; producer claims remain DECLARED |

## 4. Construction-point findings

### 4.1 Generator

\`Generator.generate(cfg)\` validates the supplied ScenarioConfig, derives effective world/Z/G seeds, and constructs:
- RunManifest;
- TruthBundle;
- EvidenceCandidate, including rows and provenance.

The world identity is derived from world_seed, outer_replicate_id and a \`world_spec\` projection. That projection removes seed-stream and execution-identity fields for world identity. It is not a Gate 166 canonical configuration fingerprint and must not be reused as one without a separately versioned projection/serialization contract.

The complete input \`cfg\` remains available to the caller at this boundary. Capture its exact dataclass serialization and the SeedAssignment row that produced it.

### 4.2 Sealer

\`Sealer.seal(candidate)\` returns SealedEvidence containing:
- run_id;
- the full rows tuple;
- manifest, including provenance and row count;
- sha256 calculated over the manifest and rows using the existing \`_hash\` serialization.

This resolves an ambiguity in Gate 166: **the digest is recalculable at export time from the in-memory SealedEvidence object**. The problem is subsequent retrieval. If raw rows are excluded from the package, the export must preserve an immutable content-addressed evidence object or retrieval reference whose bytes/records can be fetched by an independent verifier. A manifest and digest without retrievable canonical rows remain UNVERIFIABLE.

Do not replace the existing SealedEvidence digest algorithm with JCS. Preserve its legacy semantics and compute any package/JCS digest separately.

### 4.3 Analyzer

\`Analyzer.analyze(evidence, contract)\` verifies the SealedEvidence digest and checks assignment/mechanism provenance against AnalysisContract. It returns AnalyzerResult with run_id, input/output hashes, provenance hash, estimand identities, estimates/statuses and M/R identity fields.

AnalyzerResult does not carry the full ScenarioConfig, SeedAssignment, RunManifest or SealedEvidence object. Gate 166 export therefore must bind these source records by explicit join keys; it must not infer them from AnalyzerResult.

### 4.4 Evaluator

\`Evaluator.evaluate(truth, result, contract, tolerance, manifest)\` creates EvaluationReport and validates a number of cross-object identities. It does not receive ScenarioConfig, SeedAssignment or SealedEvidence.

\`evaluate_repeated_assignment\` consumes R tuples and returns one RepeatedAssignmentReport for the fixed world.

\`evaluate_monte_carlo\` consumes M groups of four-tuples and internally creates per-M RUN EvaluationReport and RepeatedAssignmentReport. It retains a reduced \`per_outer_replicate\` structure in its result, but does not retain SealedEvidence, ScenarioConfig, SeedAssignment or the full EvidenceCandidate.

\`evaluate_monte_carlo_benchmark\` composes the 13 scenario reports and 52-pair ledger. Its temporal_manifest stores scenario/version/N/M/role/index/run/world and seed values, but is not the complete RunManifest or source evidence package.

**Boundary:** the full export must be assembled by an orchestration function around these calls, not by the report summarizer after aggregation.

## 5. Minimum typed carrier and placement

Introduce a frozen typed carrier at the caller/orchestration boundary, conceptually:

\`RunEvidenceBundle\`:
- exact ScenarioConfig;
- exact SeedAssignment;
- RunManifest;
- TruthBundle;
- EvidenceCandidate reference/identity (optional retention after sealing);
- SealedEvidence or immutable retrievable evidence reference;
- AnalysisContract;
- AnalyzerResult;
- EvaluationReport;
- producer execution context reference.

The carrier is assembled in this order:
1. select one exact SeedAssignment row;
2. construct the full ScenarioConfig from the frozen structural design plus that row's execution seeds/identity;
3. call Generator and capture its three outputs;
4. call Sealer and retain SealedEvidence or publish its canonical rows to immutable content-addressed storage;
5. call Analyzer and retain AnalyzerResult;
6. call Evaluator and retain EvaluationReport;
7. append the complete bundle to its scenario/M group;
8. after R aggregation, attach exactly one RepeatedAssignmentReport to that M group;
9. after all M and scenarios, construct and validate the benchmark export envelope.

This is a proposed minimal carrier boundary, not an existing class. It must be introduced with explicit schema/version and compatibility tests if implementation is authorized.

## 6. Compatibility and identity constraints

1. Do not change the meaning or signature semantics of existing Generator, Sealer, Analyzer or Evaluator methods merely to satisfy export, unless a separate compatibility decision justifies it.
2. Prefer a new orchestration/export module and frozen carrier over expanding every core dataclass with duplicate payloads.
3. Preserve existing dataclass fields/defaults and legacy JSON hash semantics. New export digests are separate.
4. Keep \`replicate_id\` as a legacy string; M is \`outer_replicate_id\`; R is \`assignment_index\` / SeedAssignment.replicate.
5. The exact SeedAssignment must be bound to the RunManifest by scenario/version/N/M/role/index and seed equality. RunManifest has no bank field; bank remains on SeedAssignment and benchmark design.
6. Capture EvaluationReport at the time Evaluator.evaluate returns. Recomputing it later is unnecessary and risks tolerance/config drift.
7. Capture RepeatedAssignmentReport once after the complete R set has passed identity/cardinality checks.
8. Do not add potential-outcome arrays to the default export. Preserve the Gate 166 matrix-relevant TruthBundle projection and theta_a_truth null/value.
9. Technical test evidence and GitHub workflow/artifact facts remain separate from scientific run bundles.
10. No export status may be upgraded based only on producer-supplied hashes or booleans.

## 7. Findings requiring Gate 166 contract clarification

### 7.1 SealedEvidence retrieval

The SealedEvidence object currently contains rows in memory, so an independent digest recomputation is possible before export. Gate 166's data-minimization rule is viable only if one of these is chosen:
- retain canonical sealed rows in the evidence export; or
- publish the exact canonical representation to immutable content-addressed storage and include a retrievable locator plus media/schema/serialization identity and availability verification.

If neither is available, mark the digest UNVERIFIABLE and block RECONCILED status. The current source has no durable evidence locator/store abstraction.

### 7.2 AnalysisContract cardinality

AnalysisContract is constructed per execution path but contains no run_id or explicit contract registry digest. Gate 166's content-addressed deduplication is compatible, provided the exporter serializes the exact contract and adds a per-run reference. Do not imply that the current contract object already has that digest or registry.

### 7.3 EvaluationReport cardinality

The current benchmark aggregator internally produces one run report per designated RUN and a RepeatedAssignmentReport per M; repeated report itself contains per-R EvaluationReports. Gate 166 should preserve this exact hierarchy and avoid duplicating RUN reports inside the R aggregate. The current \`per_outer_replicate\` structure has a \`run_report\` and \`repeated_report\`; this is the correct source boundary to export.

### 7.4 EvidenceCandidate

EvidenceCandidate is an intermediate object whose rows become SealedEvidence rows. Gate 166 does not need to retain both full candidate and sealed rows in the final package. Retain its provenance/source identity as required, then discard candidate payload after Sealer succeeds, provided SealedEvidence remains retrievable and linked.

## 8. Gate 166 disposition

Gate 166's schema is substantially compatible with the actual source objects. The source audit identifies one material implementation prerequisite: **a RunEvidenceBundle/export orchestrator must capture objects before the current four-tuple reduction and carry them through M aggregation**.

The SealedEvidence digest algorithm is available for recomputation from in-memory rows; durable independent verification requires a retrievable immutable canonical representation. This is a storage/export boundary gap, not an absence of a digest algorithm.

No evidence supports claiming the export interface is implemented. No code was changed and no tests were run.

## 9. Acceptance criteria for implementation

1. One RunEvidenceBundle is created per declared RUN/R assignment.
2. Every bundle binds exact ScenarioConfig, SeedAssignment, RunManifest, TruthBundle, SealedEvidence, AnalysisContract, AnalyzerResult and EvaluationReport.
3. All join keys and seed equality rules from Gate 166 are checked at capture.
4. SealedEvidence digest is independently recomputed from the exact canonical rows before rows are omitted or externalized.
5. If externalized, immutable retrieval and digest verification are tested; missing retrieval blocks RECONCILED.
6. Full RunManifest and exact source objects are retained; reduced temporal_manifest is not substituted.
7. One RUN report and one repeated report per M are preserved without double counting.
8. Calibration manifest is captured separately and exact bank separation is independently recomputed.
9. The export envelope is built from complete bundles, not reconstructed from Evaluator summary output.
10. Tamper, orphan, duplicate, cross-M, wrong-bank, seed mismatch and non-retrievable evidence tests fail closed.
11. Existing technical and scientific test scopes remain distinct.
12. All tests are technical contract tests; no calibration or scientific Monte Carlo run is implied.

## 10. Gate 167 state and next operation

- Source construction points mapped: AUDITED.
- Existing Evaluator tuple insufficiency: CONFIRMED STATICALLY.
- Minimal typed carrier boundary: DEFINED.
- SealedEvidence digest algorithm: PRESENT; independent retrieval after data minimization: OPEN.
- Export orchestrator: NOT IMPLEMENTED.
- Gate 166 schema: COMPATIBLE WITH CLARIFICATIONS ABOVE.
- Tests/runtime/CI: NOT RUN.
- Scientific execution/calibration/seed generation/Monte Carlo: NOT AUTHORIZED / NOT EXECUTED.
- main unchanged; PR #116 remains Draft on its existing base.

**Gate 168 — freeze the RunEvidenceBundle and immutable SealedEvidence retention/retrieval contract**, then reconcile the Gate 166 schema. Implementation should follow only after that boundary is frozen and explicitly authorized.

## 11. Gate 168 correction — world-identity projection

The Gate 167 source audit's description of the Generator world-identity projection was incomplete. Reinspection of the exact source shows that `Generator.generate()` removes `seed`, `world_seed`, `z_assignment_seed`, `g_assignment_seed` and `replicate_id` from `world_spec`, but does **not** remove `assignment_role` or `assignment_index`. Both remain in the object hashed into `world_id`.

This means a designated RUN and repeated assignments with the same intended M/world seed can receive different world IDs solely because their role/index differ. That conflicts with Gate 154's fixed-world-within-M contract. The earlier Gate 167 statement implying role/index were removed is corrected; no historical record is erased.

Gate 168 defines the required versioned correction and deterministic regression. Until it is implemented and verified, shared world identity is a BLOCKER for evidence-bundle acceptance. This is a static source finding, not a runtime test result.
