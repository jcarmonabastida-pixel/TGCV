# C10-S V_cont — Gate 174: package serialization and independent verifier contract

**Status:** CONTRACT DEFINED — IMPLEMENTATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 173 package-readiness audit  
**Normative package target:** Gate 164 `TGCV-C10S-VCONT-MC-PACKAGE v1.0.0`  
**Execution:** no code changes, tests, package generation, CI, calibration, seed generation, benchmark or scientific execution in this gate

## 1. Decision summary

Gate 174 freezes the serialization boundary and independent verifier interface for the existing Gate 164 v1.0.0 package. It does not implement the packager.

Two package profiles are distinguished:

1. **CONFIRMATORY / Gate 164 v1.0.0:** fail closed. The exact 14-file inventory remains mandatory. Missing calibration manifest, unresolved Gate 159 reconciliation, unresolved effective fingerprints or absent independently resolved producer/test metadata prevents package acceptance as Gate 164-compliant. No placeholder or producer-declared PASS may satisfy a required payload.
2. **DIAGNOSTIC / non-Gate-164 transport:** may carry available evidence with explicit `UNAVAILABLE`, `DECLARED`, `NOT_RECONCILED` states and missing-evidence reasons. It must use a distinct schema ID/profile and must never be labelled Gate 164 v1.0.0, RECONCILED, AUTHENTICATED, or confirmatory. This profile is a future option; its schema is not defined or implemented by Gate 174.

This resolves the Gate 173 question without weakening the frozen Gate 164 contract. A missing calibration manifest is not replaced with an empty file or fabricated manifest.

## 2. Package input boundary

The pure builder input is the already materialized set:

- exact evaluator report, preserving all 52 pair rows, M contributions, denominators, statuses and legacy report fingerprint;
- frozen `MonteCarloBenchmarkDesign`;
- exact ordered 52-row `ScenarioEstimandSpec` matrix used by the evaluator;
- structural effective ScenarioConfig registry and per-run ScenarioConfig snapshots;
- AnalysisContract registry and per-run references/snapshots;
- exact ordered evaluation SeedAssignment rows;
- actual calibration seed manifest (required for Gate 164 profile);
- `CapturedBenchmark` outer-world bundles and evidence index;
- source execution metadata and externally resolved GitHub workflow/run/artifact metadata;
- independently computed Gate 159 reconciliation result;
- exact technical test workflow evidence.

The builder MUST NOT generate seeds, invoke Generator/Sealer/Analyzer/Evaluator, reconstruct missing source records from report summaries, or trust producer-supplied validation booleans.

## 3. Exact Gate 164 file mapping

The 14 paths in Gate 164 §3 remain unchanged and are all required for CONFIRMATORY profile. The builder maps them as follows:

| Existing path | Serialization contract |
|---|---|
| `manifest.json` | Gate 164 schema/profile, exact sorted file inventory, byte lengths and SHA-256 |
| `report/report.json` | Exact report payload; preserve legacy `report_fingerprint` |
| `design/benchmark_design.json` | Typed design fields, declared N/M/R, versions, targets and declared fingerprints |
| `design/scenario_estimand_matrix.json` | Exact 52 ordered matrix rows used in evaluation |
| `design/effective_scenario_configs.json` | One structural config per scenario/version/N plus explicit config identity/projection |
| `design/analysis_contracts.json` | Contract registry and exact per-run references; no implicit substitution |
| `seeds/evaluation_seed_assignments.json` | Exact ordered rows, scenario then numeric M, RUN first, numeric R |
| `seeds/calibration_seed_manifest.json` | Actual canonical calibration rows or immutable retrievable content under Gate 164 rules; absence blocks CONFIRMATORY |
| `runs/temporal_manifest.json` | Exact RUN/R identities and seed/world joins, in Gate 164 order |
| `runs/run_records.json` | Versioned envelope defined in §4 |
| `provenance/source_execution.json` | Producer declarations separately from GitHub-resolved workflow/run/attempt/event/ref/commit/tree/archive/runtime/dependency evidence |
| `provenance/configuration_fingerprints.json` | Declared, recomputed and compared digests for DGP, Generator, Analyzer, matrix and seed bank |
| `validation/reconciliation_results.json` | Independent Gate 159 result, checks, counts, failure list and verifier identity/version |
| `validation/test_evidence.json` | Exact technical workflow run, commit tested, command IDs, counts and artifact digests |

No extra archive path is allowed in v1.0.0. No source-code, pickle, notebook, executable, secret or private environment dump is included.

## 4. `runs/run_records.json` envelope v1.0.0

Top-level object:

- `schema_id = TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE`
- `schema_version = 1.0.0`
- `benchmark_export_id`: deterministic identifier derived from the frozen design identity; not a random timestamp.
- `declared_cardinality`: `scenario_count=13`, `pair_count=52`, `outer_world_count=13*M`, `run_record_count=13*M*(1+R)`, `repeated_report_count=13*M`.
- `ordering_profile`: explicit reference to Gate 164 §4.2.
- `join_key_profile`: explicit field names below.
- `run_evidence_records`: exact ordered records, one per RUN/R.
- `outer_world_evidence_records`: exact ordered records, one per scenario/M.
- `evidence_index`: ordered `(scenario_id, outer_replicate_id, world_id)` rows, one per outer-world bundle.

Each `run_evidence_record` contains:
- `key`: scenario_id, scenario_version, N, outer_replicate_id, assignment_role, assignment_index, run_id;
- `bank`;
- `snapshot_refs`: assignment, scenario_config, run_manifest, truth_projection, evidence_candidate, sealed_evidence, analysis_contract, analyzer_result and evaluation_report;
- `scenario_config_structural_sha256`, `analysis_contract_sha256`, `sealed_evidence_legacy_sha256`;
- `snapshot_validation_status` as producer declaration only.

A snapshot reference is a complete inline envelope:
- `type_id`: exact allowlisted fully qualified dataclass type ID;
- `encoding = base64`;
- `media_type = application/vnd.tgcv.typed-snapshot+json`;
- `serialization_id = TGCV-FROZEN-SNAPSHOT-1`;
- `canonical_bytes_base64`: base64 of the exact existing FrozenSnapshot.canonical_bytes;
- `sha256`: SHA-256 over the decoded exact bytes.

The envelope preserves the original snapshot bytes byte-for-byte; it does not reinterpret their legacy serialization as JCS. The containing `run_records.json` file is then independently serialized under Gate 164 JCS.

Each `outer_world_evidence_record` contains:
- `key`: scenario_id, scenario_version, N, outer_replicate_id, world_id, world_version, world_seed;
- `run_record_key`: exactly one RUN key;
- `repeated_run_record_keys`: exactly R ordered keys for assignment indices 0..R-1;
- `repeated_assignment_report`: one typed snapshot envelope;
- `bank`.

The repeated report is represented exactly once in its owning outer-world record. It is not duplicated in a second independent registry. All referenced run keys must resolve exactly once.

No full potential-outcome arrays are added; the Gate 166 MatrixTruthProjection remains the truth payload boundary. SealedEvidence retains its full rows and manifest inline as selected in Gate 168 and confirmed in Gate 173.

## 5. Identity and cardinality join keys

The canonical per-run key is:
`(scenario_id, scenario_version, N, outer_replicate_id, assignment_role, assignment_index, run_id)`.

The canonical outer-world key is:
`(scenario_id, scenario_version, N, outer_replicate_id, world_id)`.

The SeedAssignment join compares the full identity plus bank and all three seeds (world, Z-assignment, G-assignment). The RunManifest join compares scenario/version/N, outer ID, role/index, run_id, world_id/world_version and all seeds. The ScenarioConfig join compares scenario/version/N, outer ID, role/index, replicate/world version and effective seed streams. TruthProjection, EvidenceCandidate, SealedEvidence, AnalyzerResult and EvaluationReport must share the exact run_id; AnalyzerResult.input_sha256 must equal the recomputed legacy SealedEvidence digest.

Cardinality rules:
- exactly 13 scenarios and 52 unique scenario-estimand pairs;
- exactly M outer-world records per scenario;
- exactly one RUN (index -1) plus R repeated assignments (indices 0..R-1) per outer-world record;
- exactly 13×M×(1+R) unique run records;
- exactly 13×M repeated aggregate reports;
- exactly 52 pair keys and one contribution per M per pair;
- no orphan, duplicate, missing, extra or silently reordered record.

## 6. Serialization and canonicalization

1. Verify each source snapshot's base64 decoding and exact SHA-256 before parsing.
2. Parse its tagged snapshot JSON with duplicate-key rejection, strict UTF-8, no BOM, finite numbers only and exact top-level type ID.
3. Use an allowlisted, versioned type registry. Reject unknown dataclass/enum IDs, missing/extra fields and incompatible schema versions. Enum decoding MUST restore the registered enum type, not merely its string value.
4. Preserve tuple/list/map distinctions and null/missing distinctions. The current snapshot encoder does not support arbitrary bytes and its enum decoder currently returns the underlying value; the Gate 174 adapter MUST reject unsupported values and supply a versioned, lossless decoder rather than claiming current restore is universally type-preserving.
5. Do not alter or reserialize the retained snapshot bytes during package construction.
6. Construct the data-only package objects and serialize each of the 13 JSON files under Gate 164 RFC 8785 JCS, UTF-8 without BOM and exactly one trailing LF. Reject NaN/Infinity, duplicate keys, invalid Unicode and implicit coercion.
7. Apply Gate 164 array ordering exactly: SCENARIO_IDS; matrix canonical estimand order; assignments and temporal/run records scenario → numeric M → RUN → numeric R; pair contributions numeric M; file inventory lexicographic POSIX paths.
8. Recompute legacy SealedEvidence digest from decoded manifest+rows using the unchanged Sealer-compatible algorithm. Compare to stored SealedEvidence digest and AnalyzerResult.input_sha256.
9. Independently recompute existing structural config, AnalysisContract, matrix and evaluation-seed fingerprints using their declared legacy algorithms. Record those results separately from JCS file digests.
10. Compute each non-manifest file SHA-256 over final canonical bytes and exact byte length. Construct manifest from sorted inventory; hash canonical manifest bytes. Derive package_id under Gate 164. Compute final tar SHA-256 only over exact completed archive bytes and store it in detached receipt/attestation, never inside the archive.

The archive follows Gate 164 §5 deterministic uncompressed POSIX tar profile exactly. No fallback to a non-deterministic implementation is permitted.

## 7. Independent verifier API and result model

The independent verifier is a separate implementation boundary and MUST NOT import the producer's package builder or trust its status flags. Conceptual interface:

`verify_report_package(archive_bytes, policy, resolved_github_metadata, trusted_attestation_context=None) -> VerificationResult`.

It must operate fail-closed and return:
- `package_integrity`: PASS / FAIL;
- `schema_conformance`: PASS / FAIL;
- `evidence_completeness`: COMPLETE / INCOMPLETE;
- `identity_reconciliation`: RECONCILED / NOT_RECONCILED / REJECTED / UNVERIFIABLE;
- `source_execution_provenance`: DECLARED / RECONCILED / REJECTED / UNVERIFIABLE;
- `test_evidence_status`: VERIFIED / NOT_VERIFIED / REJECTED / UNAVAILABLE;
- `attestation_status`: AUTHENTICATED / NOT_AUTHENTICATED / REJECTED / NOT_APPLICABLE;
- `findings`: stable check_id, severity, status, affected key/path and reason;
- `verified_digests`: per-file digests, manifest digest and archive digest.

No single aggregate PASS may conceal a missing layer. `AUTHENTICATED` is emitted only after independent cryptographic verification under the governed signer policy. Scientific validity, causal identification and TGCV claim status are outside this package verifier.

## 8. Fail-closed profile rules

For Gate 164 CONFIRMATORY:
- absent calibration manifest, Gate 159 result, effective configuration payload, independently resolved GitHub source/workflow metadata or required technical test evidence => reject as incomplete / UNVERIFIABLE;
- any digest, identity, cardinality, report-ledger or tar mismatch => REJECTED;
- producer-supplied PASS/AUTHENTICATED fields never override verifier output.

A future DIAGNOSTIC transport profile may preserve partial records and missing-evidence reasons, but must have a distinct schema ID/version and explicit non-reconciled state. It is not Gate 164 v1.0.0 and cannot be used as confirmatory or authenticated evidence. Gate 174 does not define its serialization schema.

## 9. Required adversarial tests

In addition to Gate 164 §10:
- corrupted/invalid base64 and snapshot SHA mismatch;
- unknown type ID, enum ID, field, missing field or schema version;
- enum decode returning string instead of registered enum;
- tuple/list/map/null/missing coercion;
- unsupported bytes or non-finite number;
- SealedEvidence rows omitted, reordered or altered;
- SealedEvidence legacy digest mismatch with AnalyzerResult.input_sha256;
- duplicate/orphan run references and repeated report duplication;
- snapshot bytes altered while outer JCS file remains syntactically valid;
- calibration placeholder or absent manifest falsely marked complete;
- diagnostic profile mislabeled as Gate 164 v1.0.0;
- verifier trusting producer validation_status or producer-supplied GitHub metadata.

## 10. Gate 174 verdict and next operation

- Gate 164 v1.0.0 exact file inventory: RETAINED.
- `runs/run_records.json` envelope: DEFINED.
- Snapshot binary envelope: DEFINED as base64 of exact retained bytes plus type/serialization ID and SHA-256.
- Snapshot type restoration: requires versioned allowlisted decoder; current enum behavior is insufficient for a universal round-trip claim.
- JCS and deterministic TAR: existing Gate 164 rules retained; no implementation.
- Independent verifier interface and status vector: DEFINED.
- Confirmatory profile: FAIL-CLOSED on missing calibration/Gate 159/external provenance/test evidence.
- Diagnostic partial transport: conceptually separated; schema not defined.
- Packager, decoder, verifier, tests and CI: NOT IMPLEMENTED / NOT EXECUTED.
- Calibration, seed-bank generation, benchmark and scientific execution: NOT AUTHORIZED / NOT EXECUTED.
- main unchanged; PR #116 remains Draft on its existing base.

**Next Gate 175:** static implementability audit of the Gate 174 contract against the actual type registry, snapshot encoder/decoder, matrix object, report schema and available provenance APIs. Resolve type/field gaps before authorizing any serializer implementation.

## 11. Gate 175 — source implementability qualification

Gate 175 found that `produce_and_capture_benchmark()` validates and consumes the exact 52-row matrix locally but does not retain it in the returned `CapturedBenchmark` (which contains only report, outer-world bundles and evidence index). The report retains the design fingerprint and 52-pair ledger, not the exact matrix definitions. Therefore the Gate 174 requirement to export the exact matrix cannot be met from CapturedBenchmark alone; callers would need a separately retained immutable matrix explicitly bound to the capture.

A second issue: `scenario_matrix_fingerprint()` omits `ScenarioEstimandSpec.tolerance_id`. Preserve this legacy fingerprint unchanged for compatibility, but add a versioned full-matrix digest covering every declared field including tolerance_id and nested EvaluationKey fields. The full digest is the exact matrix commitment.

The snapshot registry covers the current run dataclasses but not ScenarioEstimandSpec/EvaluationKey. The generic decoder drops enum type identity, accepts untagged dictionaries and does not enforce exact field sets or schema versions; arbitrary bytes and non-string mapping keys are rejected. No enum-valued field was identified in the currently registered snapshot dataclass fields, so enum loss is a latent generic gap rather than a demonstrated loss in current RUN/R records. `FrozenSnapshot.restore()` is not an independent strict package decoder.

RUN/R snapshots, M bundles, repeated reports, design, temporal manifest and 52-pair report are available in source. Structural ScenarioConfig registry can be deterministically projected from retained per-run configs under the capture's explicit field-removal rule; AnalysisContracts can be deduplicated by complete snapshot bytes with per-run references. Calibration manifest, Gate 159 reconciliation and independently resolved GitHub source/test metadata are not provided by the capture API.

**Gate 174 disposition updated:** contract DEFINED / QUALIFIED; confirmatory packager remains BLOCKED pending exact matrix retention/full digest, calibration and independent provenance inputs, and strict decoder. See Gate 175. No code, tests or benchmark were executed.

## 12. Gate 176 — matrix capture and companion artifact resolution

Gate 176 defines a capture-time immutable `MatrixCapture v1.0.0` containing the exact 52 typed matrix rows passed to the evaluator. It adds a versioned full-matrix JCS SHA-256 over every declared ScenarioEstimandSpec field and nested EvaluationKey field, including `tolerance_id`. The legacy `scenario_matrix_fingerprint()` remains unchanged and is checked separately.

The `CapturedBenchmark.report` is a mutable dictionary inside a frozen dataclass. Gate 176 therefore requires a capture-time immutable report snapshot/digest as the authoritative package input while retaining the mutable report as a compatibility view.

CalibrationBankManifest, Gate159ReconciliationArtifact, SourceExecutionEvidence and TechnicalTestEvidence are independent companion artifacts joined by benchmark_export_id. They are not supplied by the current evaluation capture API and cannot be inferred from producer-declared fingerprints. Missing companions remain UNAVAILABLE/UNVERIFIABLE and block Gate 164 confirmatory acceptance.

See Gate 176. No source implementation or tests occurred.

## 13. Gate 177 — serializer input readiness

Gate 177 confirms that the exact matrix capture boundary exists but the current validator does not enforce Gate 176's canonical row order. The legacy matrix fingerprint sorts rows and omits `tolerance_id`; the full-matrix validator must enforce canonical order and exact field/value types.

The current FrozenSnapshot API accepts dataclasses only, not the top-level report dict; its generic Python JSON encoding is not RFC 8785 JCS and its decoder is not a strict independent package decoder. A separate versioned FrozenReportSnapshot with an explicit typed report projection, pinned JCS implementation/version and strict decoder is required.

Preserve CapturedBenchmark's existing report/bundle/index fields and shapes. Add only trailing optional capture fields for compatibility, but fail closed for export when absent. Define one non-circular content-derived capture identity, with benchmark_export_id aliased to capture_id and companion artifacts excluded from its digest. Exact calibration and Gate 159 check schemas remain pending.

See Gate 177. Serializer implementation is not yet ready; no code/tests executed.

## 11. Gate 178 — strict decoder and uint64/JCS qualification

Gate 178 closes the strict decoder, MatrixCapture, FrozenReportSnapshot, deterministic capture identity, CalibrationBankManifest and Gate159ReconciliationArtifact contracts. It selects `rfc8785==0.1.4` as the Python JCS implementation candidate, subject to dependency pinning, RFC vector conformance and independent cross-implementation byte equality at the later authorized implementation preflight.

A material compatibility blocker remains: seed derivation emits unsigned 64-bit integers, while Gate 164 v1.0.0 requires JCS and disallows numeric-to-string coercion. Exact uint64 preservation is not guaranteed by ordinary JCS numbers above 2^53-1. Gate 164 v1.0.0 remains unchanged and implementation-blocked until an explicit exact wire representation is approved under a versioned schema decision. See Gate 178. No source code, tests, CI or scientific execution occurred.

## 12. Gate 179 — RUN envelope v2 and typed uint64 verifier

Gate 179 versions `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE` from 1.0.0 to **2.0.0** for the Gate 164 package v2.0.0 successor. Direct `outer_world_evidence_records[*].key.world_seed` is encoded using the exact typed uint64 object `{"$type":"uint64","decimal":"<canonical unsigned decimal>"}`. The other direct seed-bearing JSON locations are listed in Gate 179 §3.

The per-run `FrozenSnapshot.canonical_bytes_base64` remains opaque and byte-identical; its SHA-256 is verified before strict allowlisted decoding. Historical fingerprints are recomputed from source-typed integers before package projection. The verifier must reject bare numeric/string seed values, malformed/out-of-range wrappers and cross-version auto-coercion.

The exact 14-file inventory is unchanged. Gate 164 v1.0.0 remains immutable; package v2.0.0 and RUN envelope v2.0.0 are the successor draft. No code/tests/CI or scientific execution occurred. Full decision and vectors: Gate 179.

## 13. Gate 180 — v2 verifier field registry and capture-source gaps

Gate 180 adds two mandatory report seed locations to the v2 verifier registry: `report.pair_ledger[*].contributions[*].world_seed` and `report.manifest.pair_ledger[*].contributions[*].world_seed`. The legacy manifest also duplicates the temporal-manifest seed fields. The verifier must validate all direct occurrences, enforce equality of duplicated views, decode exact uint64 values and only then recompute historical report fingerprints from source-typed values.

The `design/effective_scenario_configs.json` seed-field scope remains unresolved because source ScenarioConfig contains four seed-valued fields and no package projection currently establishes their inclusion/exclusion. The verifier registry must be generated from the final versioned projection schema, not a prose assumption.

The current FrozenSnapshot codec is not the strict v2 verifier: its JSON parser does not reject duplicate keys, enum decoding erases enum identity, and nested mappings are not constrained by a full exact-field schema. Existing opaque snapshot bytes remain unchanged; the independent verifier must validate their type allowlist and exact-byte digest separately. See Gate 180. No verifier implementation or tests were executed.

## 14. Gate 181 — exact v2 verifier registry and projection contract

Gate 181 freezes the direct uint64 JSON Pointer registry for package v2.0.0. It includes evaluation/calibration assignment rows, run temporal rows, root and nested report temporal rows, root and nested pair-ledger contribution `world_seed` values, and the outer-world key in run_records. The verifier must enforce all duplicate-view and assignment/RunManifest/run-record joins; no coercion, repair or silent sorting is permitted.

`design/effective_scenario_configs.json` uses EffectiveScenarioConfigProjection v2.0.0: exact structural DGP/Generator fields only, explicit seed policy requiring world/Z/G stream seeds from SeedAssignment, and no direct seed or RUN/R identity fields. Full effective ScenarioConfig snapshots remain opaque byte-preserved FrozenSnapshot payloads in run_records and are reconciled after supported decoding.

The verifier reconstructs the historical report fingerprint from source-typed manifest_payload after decoding uint64 wrappers and checking root/nested duplicate equality. It separately verifies FrozenReportSnapshot JCS and package digests. Calibration, Gate159, source-execution and test evidence are independent companion artifacts; absent required confirmatory companions block package acceptance. Full exact contract: Gate 181. No verifier code or tests were executed.

Gate 181 pins the v2 evaluation-assignment and temporal-manifest file root envelopes, each with an exact `rows` array and schema ID/version 2.0.0; all direct-seed JSON Pointers are relative to these declared roots. It also pins the legacy report fingerprint identifier `TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1`, which is recomputed from source-typed values and remains separate from JCS.
