# C10-S V_cont — Gate 194-C: independent RUN/R semantic reconciliation

**Status:** RUN/R RECONCILIATION IMPLEMENTED IN SOURCE — STATIC REVIEW CONDITIONAL — NOT EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 194-A/B — companion crosswalk and independent FrozenSnapshot decoder  
**Normative predecessors:** Gates 174, 181, 188, 191, 192 and 193  
**Scope:** independently reconstruct per-run identities, reconcile the nine source snapshots, assignment and temporal rows, outer-world references, report RUN tuples, repeated reports and pair-ledger contributions  
**Execution:** GitHub source inspection and source/document edits only. No imports, compilation, tests, CI, workflow dispatch, package construction, producer invocation, seed generation, calibration or scientific execution.

## 1. Decision and boundary

Gate 194-C adds a semantic RUN/R reconciliation layer to the independent verifier. It does not modify the writer, capture source, Generator, Sealer, Analyzer, Evaluator, DGP, estimands or seed derivation.

The verifier still does not import `vcont_package_v2.py`, `vcont_evidence_export.py`, Generator, Sealer, Analyzer or Evaluator. It decodes the historical snapshots using the independent Gate 194-B decoder and reconstructs joins from the decoded values and the other package files.

The implementation is deliberately split into two status levels:
- `run_r_reconciliation_status = RECONCILED` only if every implemented RUN/R relation below passes;
- `identity_reconciliation_status = NOT_VERIFIED` remains unchanged because the full package identity layer also requires companion, calibration, Gate159 and other independent checks not completed by this Gate.

No package has been verified in execution. The source-level status is not a runtime PASS.

## 2. Reconstructed identity and source relations

### 2.1 Canonical logical key

The verifier requires the exact seven-member RUN/R key:

`(scenario_id, scenario_version, N, outer_replicate_id, assignment_role, assignment_index, run_id)`

It enforces:
- RUN has index `-1`;
- REPEATED_ASSIGNMENT has a nonnegative index;
- exact key member set and value domains;
- globally unique `run_id` across logical RUN/R records;
- no duplicate six-field assignment identity, even if a different run_id is supplied.

The evaluation assignment bank and N are retained in the join domain; neither is inferred from list position.

### 2.2 Nine snapshots per run record

Every run record must carry exactly the nine Gate 174 references, each independently decoded with its expected registered type:

| Reference | Required source type |
|---|---|
| assignment | SeedAssignment |
| scenario_config | ScenarioConfig |
| run_manifest | RunManifest |
| truth_projection | MatrixTruthProjection |
| evidence_candidate | EvidenceCandidate |
| sealed_evidence | SealedEvidence |
| analysis_contract | AnalysisContract |
| analyzer_result | AnalyzerResult |
| evaluation_report | EvaluationReport |

The verifier validates each reference's six-field envelope, exact type ID, serialization ID, strict Base64, original-byte SHA-256 and registered nested field grammar. It does not trust `snapshot_validation_status`.

### 2.3 Assignment/config/manifest joins

For every run record it independently reconciles:
- SeedAssignment identity and bank;
- ScenarioConfig scenario/version/N/M/role/index and replicate identity;
- RunManifest scenario/version/N/M/role/index/run_id;
- RunManifest world version and temporal design against ScenarioConfig;
- all three assignment streams across SeedAssignment, ScenarioConfig and RunManifest;
- MatrixTruthProjection run_id/M/role/index against the logical key;
- EvidenceCandidate, SealedEvidence, AnalyzerResult and EvaluationReport run_id against RunManifest.run_id;
- AnalyzerResult M/role/index;
- AnalysisContract estimand, target, outcome, mechanism, reference-regime and transportability identity against AnalyzerResult and RunManifest.

The verifier recomputes the ScenarioConfig structural digest from the source-domain configuration after applying the exact Gate 181 exclusions. It independently compares the AnalysisContract snapshot digest and recomputes the SealedEvidence legacy digest from its decoded manifest and rows. It then checks AnalyzerResult.input_sha256, the record's declared sealed digest, EvidenceCandidate rows/provenance, SealedEvidence row_count and provenance digest.

### 2.4 Seed-domain anti-conflation

The source-specific equalities are enforced without equating the different seed domains:

- MatrixTruthProjection.seed = ScenarioConfig.seed;
- SeedAssignment.world_seed = ScenarioConfig.world_seed = RunManifest.world_seed;
- SeedAssignment.z_assignment_seed = ScenarioConfig.z_assignment_seed = RunManifest.z_assignment_seed;
- SeedAssignment.g_assignment_seed = ScenarioConfig.g_assignment_seed = RunManifest.g_assignment_seed.

The decoder validates every source seed as an exact uint64 integer. The three assignment streams must be distinct within each assignment. No equality is imposed between ScenarioConfig.seed and world_seed.

The new positive unit fixture explicitly uses `ScenarioConfig.seed = MatrixTruthProjection.seed = 17` and `world_seed = 101`, with independent Z/G streams. This is written test evidence only; it has not been executed.

### 2.5 Outer-world and repeated assignment joins

For each scenario/M, the verifier requires:
- exactly one designated RUN record;
- exactly R repeated references in index order 0…R-1;
- each referenced full logical key resolves to exactly one run record;
- every repeated assignment shares the owning outer-world world_id, world_version and world_seed;
- each assignment's world_seed equals the outer-world key;
- Z and G assignment streams are unique within that outer-world cluster;
- one RepeatedAssignmentReport snapshot, with the correct world_id, replicate_count and exact ordered EvaluationReport snapshots.

No orphan, duplicate, cross-world, cross-scenario or unconsumed run reference is accepted.

### 2.6 Report, temporal manifest and pair ledger

The verifier binds:
- each evaluation SeedAssignment row to exactly one RunManifest snapshot;
- each temporal-manifest row to that same logical key, run_id, world_id and three seed streams;
- report root temporal rows to the temporal companion rows;
- report nested temporal rows to the root copy through the existing report contract;
- each scenario/M report RUN tuple's TruthBundle projection, AnalyzerResult, AnalysisContract and RunManifest to their independently decoded source snapshots;
- each report RUN evaluation summary to its EvaluationReport snapshot;
- each repeated aggregate report to its RepeatedAssignmentReport snapshot;
- each of the 52 pair-ledger rows' M contributions to the corresponding scenario/M designated RUN world_id, world_seed and run_id, with canonical M order and no missing or duplicate contribution.

The 13×M outer-world universe, 13×M×(1+R) run universe, assignment rows, temporal rows, run records, outer-world records and evidence_index must have exact cardinality and canonical order. Root/nested report duplicate views remain independently checked by the pre-existing report verifier.

## 3. Result status model

`PackageVerificationResult` now exposes `run_r_reconciliation_status` independently.

| Dimension | Source implementation status |
|---|---|
| Archive and package integrity | Existing structural verifier |
| Snapshot byte integrity and typed identity | Gate 194-B decoder |
| RUN/R source reconciliation | Implemented; static review conditional |
| Assignment ↔ config ↔ manifest streams | Implemented |
| MatrixTruthProjection seed semantics | Implemented |
| Outer-world and repeated-report joins | Implemented |
| Report temporal and pair-ledger joins | Implemented |
| Overall package identity reconciliation | NOT_VERIFIED — broader companion layers remain open |
| Calibration/evaluation disjointness | NOT_VERIFIED |
| Gate159 derived-status recomputation | NOT_VERIFIED |
| Companion schemas and provenance joins | PARTIAL / OPEN |
| GitHub source-execution provenance | NOT_VERIFIED |
| Technical-test evidence | NOT_VERIFIED |
| External authentication | NOT_AUTHENTICATED |
| Tests / compilation / CI | NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

A successful RUN/R sublayer cannot promote the overall package to RECONCILED, CONFIRMATORY, scientifically confirmatory or AUTHENTICATED.

## 4. Adversarial fixtures added

Three tests were added to the independent verifier test module:
1. positive seed-domain fixture with Truth/ScenarioConfig seed different from world_seed;
2. rejection of Truth/ScenarioConfig seed divergence and Z/G stream divergence;
3. rejection of noncanonical role/index pairs and extra logical-key fields.

Together with the four decoder fixtures, these tests remain authored but unexecuted. The larger end-to-end RUN/R adversarial fixtures still need to be completed in G194-D, including cross-world reference, repeated assignment mapped to RUN, run_id divergence, duplicate logical key, orphan reference and semantically false report with structurally valid content.

## 5. Source commits

All commits are on `research/c10-s-consolidation-draft`:
- RUN/R semantic reconciliation: `44c2ce3c69798e77eb38f84e4c0244573443661d`
- source-value comparison correction: `74c7fac3b032ef831c7e6c6077f1af937cc03231`
- canonical ordering and source digest joins: `13b3e75f2e71c4468977adbbdc2e0dccdf14bd59`
- seed-domain relation enforcement: `fd0c0298803add312c363b63cc90d3e4b44e3eae`
- temporal and analysis identity joins: `ff7775b085a41f6d1a22978369e30414d4a5d303`
- pair contribution identity binding: `0813582cec004cbf88086195b4bc1a2994f0e3eb`
- repeated-report comparison correction: `00a7bee948237ce14db03ec13ad8840f3fcb3eef`
- separate RUN/R result status: `49c0cf8665300fad8b078b8c41368851a9fc60f2`
- final verifier scope clarification: `30e51edab1f574bcdfa58454c075391903af7a67`
- seed-domain and key fixtures: `fc9cafd872ea3df8b3664673e6b06a5e9ebc68aa`
- globally unique run_id guard: `50741f2c9589126a759b13b6c3467eb8106d5c0e`

## 6. Gate disposition and next operation

**G194-C: IMPLEMENTED IN SOURCE / STATIC REVIEW CONDITIONAL / NOT EXECUTED.**

Before treating this layer as stable, G194-E must perform a full static independence and contract audit. G194-D must add the complete positive and adversarial end-to-end fixture matrix, still without executing it.

The remaining G194-C adjacent work is not silently absorbed into this implementation:
- exact MatrixCapture row ↔ 52 pair-ledger key reconciliation;
- exact effective structural config registry and AnalysisContract companion joins;
- benchmark_export_id equality across all independent companions;
- complete validation of repeated report summaries and scenario report aggregates beyond the direct snapshot equality checks;
- calibration/evaluation disjointness, Gate159 derivation, source/test provenance and authentication.

No tests, compilation, CI, workflow, package construction, producers, seeds, calibration or scientific experiments were executed. No changes were made to `main`, frozen historical contracts or scientific components. PR #116 remains Draft.


## 7. Fail-closed input handling addendum

The verifier call site now preserves `PackageVerificationError` and converts unexpected malformed-input exceptions raised inside RUN/R reconciliation into a fail-closed `PackageVerificationError`. This does not broaden acceptance; it makes malformed semantic structures reject through the verifier's declared error boundary.

Additional source commit: `551c82b4ffddc84af697f35a0141bd45536c01b3`.

The verifier source was re-read after this change. A static text scan found no remaining temporary placeholder guards or empty-comprehension scaffolding in the inserted RUN/R section. This is not a syntax/compile check and does not substitute for G194-E review.


A final fail-closed hardening pass rejects boolean-as-integer aliases and malformed identity field types in assignment rows, temporal rows, decoded assignment/config/manifest snapshots and outer-world keys. Source commit: `5eb296c88c8b8c45844df3d00a996be07cd98ae0`.

This is source-level defensive validation only. It has not been compiled or exercised.
