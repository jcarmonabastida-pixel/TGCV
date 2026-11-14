# C10-S V_cont — Gate 194-A: companion crosswalk and decoder boundary audit

**Status:** CROSSWALK PARTIALLY CLOSED — IMPLEMENTATION PRECONDITIONS IDENTIFIED — NO EXECUTION
**Branch:** `research/c10-s-consolidation-draft`
**Parent:** Gate 193 — independent structural package-v2 verifier
**Normative predecessors:** Gates 178, 181, 188, 191, 192 and 193
**Scope:** exact 11-companion inventory, source-to-wire authority, verifier obligations, and FrozenSnapshot decoder boundary
**Execution:** GitHub source/document inspection and documentation only. No imports, compilation, tests, CI, workflow dispatch, package construction, producer invocation, seed generation, calibration or scientific execution.

## 1. Disposition

Gate 194-A confirms the exact eleven companion paths required by the Gate 192 writer and the exact fourteen-file package inventory. It does **not** claim that all eleven companion schemas are fully closed. The normative documents provide complete or partial source contracts for some artifacts, while others still require an exact field-level schema and provenance contract before implementation can honestly validate them.

The verifier must distinguish:
- **schema-known:** exact root/version/field contract is available;
- **source-mapped:** authoritative source object or external record is identified;
- **semantic-join-defined:** equality/key/cardinality rules are specified;
- **independently-verifiable:** the package contains sufficient material to recompute the claim without trusting producer PASS flags.

A path's presence, a schema header, or a declared digest is not evidence that these four conditions hold.

## 2. Exact package inventory and companion crosswalk

The three non-companion paths are `manifest.json`, `report/report.json` and `design/scenario_estimand_matrix.json`. The remaining eleven paths are the required materialized companion inputs:

| # | Package path | Authoritative source / contract | Gate 194 verifier obligation | Disposition |
|---:|---|---|---|---|
| 1 | `design/benchmark_design.json` | `MonteCarloBenchmarkDesign`; design identity in Gate 181 and package profile Gates 191–192 | Exact field allowlist and types; reconcile scenario/version order, N, M, R, matrix fingerprint, metric targets, seed-bank label/fingerprint, executable commit and configuration fingerprint to the report, MatrixCapture and other source artifacts | Source fields identified; exact package schema/complete joins still require closure |
| 2 | `design/effective_scenario_configs.json` | Gate 181 §3, `ScenarioConfig`, Generator version | Exact row key `(scenario_id, scenario_version, n_units)`; exact structural config allowlist; exact `seed_policy`; no direct seeds or RUN/R identity fields; reconcile every row to the declared design and the corresponding opaque per-run config snapshots | Normative structural projection defined; verifier implementation absent |
| 3 | `design/analysis_contracts.json` | `AnalysisContract` and `contract_for` in integrated harness; Gate 191 §2.1/§2.2 | Exact contract field schema; validate contract digest; reconcile semantic fields with RunManifest and AnalyzerResult; do not invent `AnalysisContract.run_id` (it does not exist) | Source type and critical join rule known; exact package schema still open |
| 4 | `seeds/evaluation_seed_assignments.json` | `SeedAssignment`, Gate 181 §2.3a and Gate 178/179 uint64 wire rules | Exact root and row envelopes; ordered rows; bank=evaluation; one-to-one assignment/manifest joins on full logical key and all three streams; recompute legacy fingerprint and typed-wire digest | Contract substantially defined |
| 5 | `seeds/calibration_seed_manifest.json` | Gate 178 §6, Gate 179 typed uint64 successor, Gate 181 §2.3a | Exact calibration-specific design/cardinality/order; recompute legacy fingerprint and JCS manifest digest; validate namespace/derivation declaration; independently establish disjointness from evaluation across world/Z/G stream unions; do not force calibration rows into evaluation RUN joins | Contract substantially defined; actual calibration payload and disjointness verifier open |
| 6 | `runs/temporal_manifest.json` | Gate 181 §2.3a; `RunManifest` | Exact row schema/order; reconcile every row one-to-one with evaluation SeedAssignment and the matching captured RunManifest, including scenario/version/N/M/role/index/run_id/world_id and all three streams | Contract substantially defined |
| 7 | `runs/run_records.json` | Gate 174 RUN-EXPORT-ENVELOPE v2.0.0; Gate 181 §3.4; Gate 188; `RunEvidenceBundle` and `OuterWorldEvidenceBundle` | Exact envelope and record schemas; strict decode of every registered FrozenSnapshot; validate type ID, serialization ID, root dataclass, field allowlist, exact bytes digest; reconstruct RUN/R keys and reconcile assignment/config/manifest/truth/evidence/seal/contract/analyzer/evaluator snapshots to report and outer-world records | Highest-priority semantic gap; snapshot decoder and full joins remain open |
| 8 | `provenance/source_execution.json` | Independently resolved GitHub repository/workflow/run/attempt/event/ref/commit/tree/artifact metadata; Gate 178 §7 and Gate 191 | Validate exact source-execution schema; independently resolve each GitHub identity; compare resolved facts to declarations and package capture/design; a producer-written JSON declaration alone cannot establish provenance | Source class identified; exact schema and independent resolution contract remain open |
| 9 | `provenance/configuration_fingerprints.json` | Effective DGP/Generator/Analyzer configuration payloads and declared configuration fingerprints; Gate 181 §3 and Gate 178 Gate159 check catalogue | Recompute each fingerprint from included canonical source payloads; bind names, versions, scopes and digests to design/config/analysis contracts; reject a file containing only claimed digest strings | Required recomputation identified; exact payload inventory/field schema remains open |
| 10 | `validation/reconciliation_results.json` | Gate159ReconciliationArtifact v1.0.0, Gate 178 §7 | Recompute required checks, counts, mismatches, findings digest and derived status from actual input rows/artifacts; exact required-check order; missing input => UNAVAILABLE/UNVERIFIABLE, never zero mismatches or PASS | Gate159 contract substantially defined; verifier derivation remains open |
| 11 | `validation/test_evidence.json` | Independently resolved technical-test workflow/run/attempt, tested commit, command/module allowlist, conclusion and artifact digest; Gate 178 §8 and Gate 191 | Independently bind test evidence to exact repository, workflow run, attempt, commit and test artifacts; separate authored tests from executed tests and CI conclusion; no self-asserted PASS | Source class identified; exact schema and independent binding contract remain open |

### 2.1 Crosswalk conclusion

The eleven paths do not share one generic validation rule. In particular:
- rows 4–6 have explicit row-level source mappings in Gate 181;
- row 2 has an explicit structural projection and exclusions in Gate 181;
- row 7 carries opaque source snapshots and is the primary object of G194-B/G194-C;
- rows 5 and 10 have dedicated Gate 178 schemas, but their semantic claims must be recomputed from actual materialized inputs;
- rows 8 and 11 require independent external GitHub resolution, not local JSON self-attestation;
- rows 1, 3 and 9 still need their complete package-level field and source-payload crosswalk closed before a verifier can claim full companion schema conformance.

No missing schema is to be guessed from a filename, a header, or the writer's accepted input type.

## 3. FrozenSnapshot decoder boundary

### 3.1 Historical codec recovered from source

The capture implementation in `vcont_evidence_export.py` defines:
- root type identity as `<module>.<qualname>`;
- root encoding as an exact `$dataclass` plus `fields` object;
- nested dataclass tags `$dataclass`;
- enum tags `$enum` plus `value`;
- tuple/list/map tags `$tuple`, `$list`, `$map`;
- canonical source bytes from sorted-key compact JSON, UTF-8, `ensure_ascii=False`, `allow_nan=False`;
- SHA-256 over those exact bytes.

The source registry includes SeedAssignment, AnalysisContract, AnalyzerResult, EvaluationReport, EvidenceCandidate, RepeatedAssignmentReport, RunManifest, ScenarioConfig, SealedEvidence, TruthBundle and MatrixTruthProjection.

This source inspection identifies the historical encoding mechanics. It does not make the production `restore()` method an acceptable independent verifier decoder: the Gate 194 verifier must implement its own strict parser and closed type/field registry, without importing the capture codec or writer.

### 3.2 Strict independent decode requirements

The independent decoder must:
1. validate strict Base64 and reject noncanonical/invalid encodings;
2. preserve the decoded byte sequence unchanged and calculate SHA-256 over those exact bytes;
3. parse strict UTF-8 JSON, rejecting BOM, duplicate object keys, non-finite values, invalid Unicode and trailing/ambiguous data;
4. require exact canonical historical byte representation as specified by the registered codec, without rewriting the stored bytes;
5. validate the snapshot envelope root against the declared `type_id`;
6. validate the exact `serialization_id` and schema/version identity declared by the RUN envelope contract;
7. validate the root dataclass against a closed allowlist and exact field set;
8. validate nested dataclass/enum/tuple/list/map tags, their exact member sets and recursively permitted contents;
9. reject unknown tags, types, enum identities, fields, malformed collections and unsupported values;
10. return a typed decoded value only after all checks pass, while retaining the original bytes and digest separately.

**Important contract gap:** the inspected historical `FrozenSnapshot` source currently exposes `type_id`, `canonical_bytes` and `sha256`; the exact package-level `serialization_id` and schema/version envelope mapping must be taken from Gate 174 and the actual RUN-EXPORT-ENVELOPE v2 source contract. It must not be fabricated by assuming that the Python module name is a serialization ID. Close this mapping before implementing G194-B.

### 3.3 Byte-preservation invariant

The verifier may decode a snapshot for validation and semantic joins, but:
- it MUST NOT replace the retained base64 payload;
- it MUST NOT rewrite historical snapshot bytes into JCS;
- it MUST NOT insert package uint64 wrappers inside the opaque snapshot;
- it MUST NOT calculate a new snapshot digest over decoded/re-serialized objects;
- it MUST keep snapshot SHA-256, report legacy fingerprint, report JCS digest, capture identity, package ID and archive digest distinct.

The positive fixture must include `TruthBundle.seed != RunManifest.world_seed` while preserving all source-specific equalities: TruthBundle.seed = ScenarioConfig.seed = MatrixTruthProjection.seed; the three RunManifest stream values equal their corresponding SeedAssignment and ScenarioConfig fields; RunManifest.world_seed equals the outer-world key. This is an explicit anti-conflation test.

## 4. Required RUN/R join model for G194-C

The primary logical key remains the complete tuple:

`(bank, scenario_id, scenario_version, N, outer_replicate_id, assignment_role, assignment_index, run_id)`

The package's declared shorthand key in the Gate 194 proposal omits bank/N in its displayed tuple; the verifier must not omit them from the actual join key. The evaluation bank and exact N are part of the contract.

For each scenario/M:
- exactly one designated RUN with role RUN and assignment index -1;
- exactly R repeated assignments with role REPEATED_ASSIGNMENT and contiguous indices 0…R-1;
- exactly one OuterWorldEvidenceBundle for the scenario/version/N/M key;
- all RUN/R assignments share the same world seed within that M;
- each assignment has distinct, correctly mapped world/Z/G streams;
- all snapshot refs resolve once and only once;
- all report and temporal references are consumed exactly once;
- no orphan, duplicate, cross-world, cross-scenario or cross-role references.

The verifier must derive these relations from decoded source objects and exact keys, not list position, approximate values, source similarity, or the writer's reconstructed index.

## 5. Status separation

Gate 194 results remain dimension-specific:

| Dimension | Gate 194-A conclusion |
|---|---|
| Package byte/archive integrity | Gate 193 implementation exists; no package has been verified in execution |
| Snapshot byte integrity | Decoder contract specified; not implemented here |
| Snapshot typed identity | OPEN pending exact RUN-envelope serialization/schema mapping and decoder |
| RUN/R semantic reconciliation | OPEN |
| Companion completeness | Exact 11 paths identified; content schemas not all closed |
| Gate159 | Independent, pending |
| Calibration/evaluation disjointness | Independent, pending |
| GitHub source provenance | Independent, pending |
| Technical-test evidence | Independent, pending |
| External authentication | NOT_AUTHENTICATED |

A structural PASS cannot imply identity reconciliation, companion completeness, test execution, scientific execution or confirmation.

## 6. Next operation

**G194-A disposition:** exact path inventory and source authority crosswalk are established; complete field-level crosswalk is **PARTIAL**, not PASS. Before G194-B code is written, retrieve and reconcile the exact Gate 174 RUN-EXPORT-ENVELOPE v2.0.0 schema, including `serialization_id`, snapshot envelope fields and per-type schema/version registry. Then implement the independent decoder in `vcont_package_v2_verify.py` only, with no writer/capture-code imports.

No tests, compilation, CI, workflow, producers, seeds, calibration, package generation or scientific execution are authorized or performed by this Gate. No scientific component, estimand, DGP, seed derivation or canonical `main` artifact is changed.


## 7. Gate 174 retrieval correction

The exact Gate 174 contract has now been located at:
`00_GOVERNANCE/SIP/C10_S_VCONT_PACKAGE_SERIALIZATION_AND_INDEPENDENT_VERIFIER_CONTRACT_GATE_174_DRAFT_001.md`.

It closes the RUN envelope mapping precisely. Each snapshot reference has exactly:
- `type_id`;
- `encoding = base64`;
- `media_type = application/vnd.tgcv.typed-snapshot+json`;
- `serialization_id = TGCV-FROZEN-SNAPSHOT-1`;
- `canonical_bytes_base64`;
- `sha256`.

There is no per-snapshot `schema_version` field in this envelope. The closed type/field registry is therefore bound to the verifier implementation/profile version, not inferred from a nonexistent snapshot schema-version member. The earlier wording in §3.2 requiring a separate per-snapshot schema/version field is superseded by this exact Gate 174 mapping. Enum tags must retain registered enum identity; current generic restore behavior is not accepted as the independent decoder.

Gate 174 also specifies the canonical run key, outer-world key, exact RUN/R cardinalities, the nine snapshot references per run record, one repeated-assignment report per outer-world record, and the requirement that every referenced run key resolve exactly once.

## 8. Gate 194-B implementation addendum

The independent verifier now contains:
- a closed type registry for the ten source dataclasses plus MatrixTruthProjection;
- exact field allowlists recovered from the current source dataclass definitions;
- a closed enum identity/value registry for EvaluationClass and TruthStatus;
- recursive validation of dataclass, enum, tuple, list and map tags;
- rejection of untagged/unknown objects, unknown types/enums, missing/extra fields and malformed collection tags;
- strict Base64 decoding with canonical re-encoding check;
- exact SHA-256 verification over the decoded original bytes;
- strict UTF-8/JSON parsing with duplicate-key and non-finite rejection;
- exact historical compact sorted-key JSON byte check, with no conversion to JCS;
- exact Gate 174 envelope field, media type, encoding and serialization ID validation;
- an immutable result retaining original bytes and digest separately from the decoded tagged structure.

Public helper added: `decode_frozen_snapshot_ref(reference, expected_type_id=None)`.

The pure verifier fixture module now contains four additional decoder tests: positive SeedAssignment snapshot, digest/root-type divergence, missing field/invalid Base64, and duplicate JSON key/unknown nested tag. These tests are written, not executed.

Implementation commits:
- Gate 194-A crosswalk: `41dcdbbe9a3196d7dd98667c742ffe213375c474`.
- Gate 194-B decoder: `b0bf9b90728458079d525bd1211cca859bc27412`.
- Gate 194-B decoder fixtures: `9ba72bdad00a2f4cbc3a94be907a67eb2c4a0ce9`.

**Disposition:** G194-A crosswalk is now materially closed for the RUN snapshot envelope; companion schemas 1, 3, 8, 9 and 11 still require their own exact field-level/source-resolution contracts. G194-B decoder is IMPLEMENTED IN SOURCE / NOT COMPILED / NOT EXECUTED / STATIC REVIEW PENDING. No tests, compilation, CI, workflow, package, producer, seed generation, calibration or scientific execution occurred.
