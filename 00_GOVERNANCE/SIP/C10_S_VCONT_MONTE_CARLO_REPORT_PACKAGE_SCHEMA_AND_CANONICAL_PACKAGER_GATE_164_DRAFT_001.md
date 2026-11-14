# C10-S V_cont — Gate 164: Monte Carlo report-package schema and canonical packager contract

**Status:** PACKAGE CONTRACT DEFINED / PACKAGER IMPLEMENTATION OPEN  
**Branch:** research/c10-s-consolidation-draft  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / seed-bank generation / N/R/M sizing / Monte Carlo:** NOT AUTHORIZED  
**Code, tests, workflow or CI changes:** NOT PERFORMED

## 1. Purpose and boundary

Define the single immutable subject that a future dedicated trusted attestor may sign. The package must let an independent verifier establish exact report and matrix coverage; recompute file and package digests; inspect the complete M/R/RunManifest/SeedAssignment relationship; recompute seed-bank, effective-configuration and matrix fingerprints from included canonical inputs; distinguish declared, reconciled and externally authenticated provenance; and inspect all 52 scenario-estimand pairs without rerunning scientific code.

This package is an audit/evidence container, not a scientific validity certificate. A digest proves integrity relative to a trusted expected digest; an Artifact Attestation authenticates the signer/workflow and subject digest. Neither proves that the DGP is scientifically appropriate, that the Analyzer is unbiased, or that Delta T_acc -> Delta V is empirically established.

Gate 164 defines a format and packager contract only. It does not authorize implementation, CI, benchmark execution or scientific execution.

## 2. Identity and versioning

- Package schema ID: TGCV-C10S-VCONT-MC-PACKAGE.
- Initial schema version: 1.0.0.
- Report protocol identity: exact report schema/version emitted by the benchmark implementation; do not infer it from package schema version.
- Package subject: one archive containing exactly the allowlisted paths in §3.
- Package identity: SHA-256 of exact final archive bytes; file-level hashes are separately recorded in the manifest.
- Package ID: deterministic identifier derived from schema ID, schema version and canonical manifest digest; it excludes timestamps and random IDs.
- Producer execution identity: repository, workflow ID/path, run ID, run attempt, source ref, full source commit, source-tree digest, producer artifact ID and producer artifact digest. These identifiers remain distinct.
- Benchmark identity key: scenario ID/version, N, M, R, matrix fingerprint, estimand versions, metric targets, seed-bank identity and effective DGP/Analyzer configuration identity.

M is the outer independent-world dimension; R is repeated assignment within each M; the designated RUN row is separate from R rows. The package preserves Gate 154 semantics and may not use the legacy replicate field as an untyped M/R identifier.

## 3. Canonical package layout

The package contains exactly these regular files; no extra files, symlinks, hardlinks, devices, executable bits, hidden files or path aliases are permitted:

    manifest.json
    report/report.json
    design/benchmark_design.json
    design/scenario_estimand_matrix.json
    design/effective_scenario_configs.json
    design/analysis_contracts.json
    seeds/evaluation_seed_assignments.json
    seeds/calibration_seed_manifest.json
    runs/temporal_manifest.json
    runs/run_records.json
    provenance/source_execution.json
    provenance/configuration_fingerprints.json
    validation/reconciliation_results.json
    validation/test_evidence.json

| File | Required content |
|---|---|
| manifest.json | Package schema/version, exact file inventory, byte lengths and SHA-256 digests, canonicalization and archive profile, report fingerprint, package ID derivation inputs |
| report/report.json | Full report output: coverage, all 52 pair-ledger records, all M-level contributions, metric summaries, MCSE/precision states, status rates, denominators and report fingerprint |
| design/benchmark_design.json | Exact declared N/M/R, scenario versions, metric targets, seed-bank label/fingerprint, executable commit claim, configuration fingerprint claim and matrix fingerprint |
| design/scenario_estimand_matrix.json | Full authoritative 52-row matrix, including temporal evaluation classes, truth source, output field, identification/abstention expectations and reasons |
| design/effective_scenario_configs.json | Canonical effective DGP/Generator configuration for each scenario/version/N; all parameters affecting generated worlds |
| design/analysis_contracts.json | Canonical effective AnalysisContract and Analyzer configuration/version per scenario/run family |
| seeds/evaluation_seed_assignments.json | Exact ordered evaluation SeedAssignment rows materialized for all 13 scenarios × M × (1+R), with bank, scenario/version, N, outer ID, role, assignment index and world/Z/G seeds |
| seeds/calibration_seed_manifest.json | Calibration bank identity, full canonical assignment manifest or immutable retrievable content digest plus availability reference, namespace and separation-validation result. A digest without actual rows or an immutable retrievable manifest is insufficient to recompute disjointness |
| runs/temporal_manifest.json | Every RUN and R row, including RunManifest identities and all seed/assignment/world links |
| runs/run_records.json | Per-run TruthBundle fields used by the matrix, AnalyzerResult, AnalysisContract identity, sealed-input/output digests, EvaluationReport and run-level pair records |
| provenance/source_execution.json | Producer repo/workflow/run/run-attempt, event/ref, full source commit, source tree digest, tested source archive digest, runtime and dependency lock identity; asserted fields are distinguished from GitHub-resolved fields |
| provenance/configuration_fingerprints.json | Canonical configuration payload digests and recomputation records for DGP, Generator, Analyzer, matrix and seed bank |
| validation/reconciliation_results.json | Gate 159 reconciliation results, one-to-one joins, validation version, check IDs, counts and explicit failure list; caller-supplied PASS booleans are not authoritative |
| validation/test_evidence.json | Exact technical workflow run IDs, commit tested, test command identifiers, counts and artifact digests; test evidence is not a scientific execution record |

All file contents are data only. No executable, notebook, pickle, Python module, shell script, binary, credential, secret, private runner path or unredacted environment dump is allowed.

## 4. Canonical serialization

### 4.1 JSON profile

All JSON files use UTF-8 without BOM, RFC 8785 JSON Canonicalization Scheme (JCS), no insignificant whitespace, object keys canonicalized by JCS, arrays in the ordering specified below, and exactly one trailing LF after canonical JSON bytes.

- Reject NaN, positive/negative infinity, duplicate object keys, invalid Unicode and non-JSON values.
- Numeric values must be finite. No string coercion of numbers, booleans or null.
- Missing, null, zero and empty arrays remain distinct.
- Tuples serialize as arrays; enums serialize as declared stable string values.
- Timestamps use UTC RFC 3339 with fixed precision and Z; timestamps are excluded from deterministic scientific payload fingerprints unless part of an external execution record.
- No machine-specific absolute paths or transient environment fields.
- Hashes are lowercase hexadecimal SHA-256.

JCS is the cross-implementation canonicalization rule. Python json.dumps(sort_keys=True) alone is not an acceptable substitute unless proven byte-equivalent to JCS for the permitted schema domain.

### 4.2 Array ordering

- Scenario arrays: authoritative SCENARIO_IDS order.
- Matrix pairs: scenario order, then canonical estimand order defined by the matrix contract.
- Seed assignments: scenario order, ascending numeric M index, RUN first, then ascending numeric R index.
- Temporal manifest and run records: the same scenario/M/R order.
- Pair contributions: ascending numeric M index, retaining exact outer ID.
- File inventory: lexicographic normalized POSIX path order.
- Any other array must declare whether it is semantically ordered; unordered collections are sorted by a documented stable composite key.

No sorting may erase the identity distinction between RUN and R or turn numeric indices into lexicographic order (e.g. R10 before R2).

## 5. Deterministic archive profile

The archive format is uncompressed POSIX tar (USTAR where path limits permit; otherwise PAX with deterministic extended-header ordering and normalized metadata). Compression is excluded from schema v1.0.0 to avoid compressor-version and timestamp variability.

- Entries are written in exact lexicographic path order from the manifest.
- Normalize uid/gid to 0, uname/gname to empty, mtime to 0, mode to 0644 for files and 0755 for directories.
- Reject symlinks, hardlinks, devices, FIFOs, sparse files, absolute paths, .., backslashes, duplicate normalized paths and Unicode-normalization collisions.
- No PAX atime/ctime, access metadata, host names or comments.
- Directory entries, if required, must be deterministic and excluded from the manifest data-file inventory.
- Verify the archive without extracting it where possible; otherwise use a fresh isolated directory and enforce file-count and total-uncompressed-size limits.
- Recompute each file digest and byte length from final archive bytes; then compute package SHA-256 over exact complete archive bytes.

The packager must produce byte-identical archive bytes for identical canonical inputs. If the chosen tar implementation cannot meet this profile, stop and propose a separately versioned archive profile; do not silently relax canonicalization.

## 6. Required semantic and structural invariants

### 6.1 Benchmark coverage and aggregation

- Exactly 13 declared scenarios and 52 unique scenario-estimand pairs.
- Each pair retains exactly one contribution per M and explicit expected/observed M.
- For each scenario/M: exactly one designated RUN with assignment index -1, plus exactly R repeated assignments with indices 0..R-1.
- RUN-level ITT-Z run-conditional and ITT-G Z=0 remain distinct from repeated-assignment marginal/reference aggregation.
- ITT-Z mechanism marginal is computed only within each fixed M before the between-M summary.
- ITT-Z reference regime retains its RUN status-only and repeated-level numeric/status semantics.
- Numeric denominators, status denominators, missing contributions, TRUTH_MISSING and INVALID_OUTPUT counts remain explicit. Missing/invalid outputs are not relabelled as abstentions and null is never converted to zero.
- All M-level metric summaries and MCSEs use independent M contributions, never R rows as independent Monte Carlo replicates.

### 6.2 Seed bank and identity reconciliation

- Each M has exactly one world ID and world seed shared by its RUN and R rows.
- Different M values within the same scenario/version/N/evaluation bank have distinct world IDs and world seeds.
- Every run record maps one-to-one to exactly one canonical SeedAssignment row on bank/scenario/version/N/M/role/R and all three seeds.
- Temporal-manifest outer key equals the row outer_replicate_id; no orphan or duplicate keys.
- Evaluation and calibration banks are disjoint under the canonical seed-stream identity and approved bank namespace.
- Evaluation-bank fingerprint is recomputed from exact materialized rows; calibration-bank fingerprint and disjointness are independently recomputed from actual calibration manifest.
- The same bank manifest cannot be silently relabelled from calibration to evaluation.

### 6.3 Configuration and execution provenance

- Effective DGP/Generator/Analyzer configurations are included, not only claimed fingerprints.
- Recompute configuration fingerprints from included effective payloads and compare to benchmark design declarations.
- Matrix fingerprint is recomputed from the included authoritative 52-row matrix.
- Source commit/tree/archive digests are separately named. A commit string in JSON is not proof of the code that ran.
- Producer workflow/run metadata is independently resolved from GitHub; package claims are compared with, never substituted for, GitHub-resolved metadata.
- Gate 159 reconciliation status and external attestation status are separate fields and separate gates.

## 7. Fingerprint dependency graph

Use a non-circular digest graph:

1. Each data file except manifest.json: SHA-256 over its exact canonical bytes.
2. manifest.json: contains schema/profile identity and sorted file paths, byte lengths and file hashes; it does not contain its own hash or final archive digest.
3. manifest_digest: SHA-256 over canonical manifest.json bytes.
4. report_fingerprint: existing report-level integrity digest over canonical report payload as defined by the report protocol; preserve it as a distinct digest, not the package digest.
5. package_id: deterministic derivation from schema ID/version and manifest digest.
6. package_sha256: SHA-256 over exact final tar bytes; it is the attestation subject digest and is stored in external attestation/sidecar, not embedded in the package itself.

The package cannot embed its own final archive digest without circular dependency. A detached receipt may record package digest and attestation reference, but is not part of the attested package subject.

## 8. Provenance status model

The package retains distinct claims:
- DECLARED: supplied by producer, syntactically valid only;
- RECONCILED: recomputed from included canonical data and matched to independently resolved execution metadata where applicable;
- AUTHENTICATED: supported by successful external attestation verification under governed signer policy;
- REJECTED: mismatch or failed integrity/policy check;
- UNVERIFIABLE: required evidence unavailable; never coerce to PASS.

The package itself cannot declare itself AUTHENTICATED. Only the independent verifier may emit that status after cryptographic verification. Scientific validity and causal identification are not package provenance statuses.

## 9. Packager API contract

The future packager should expose a pure deterministic operation conceptually equivalent to:

    build_report_package(report, design, matrix, effective_configs,
                         analysis_contracts, evaluation_seed_rows,
                         calibration_seed_manifest, run_records,
                         source_execution, validation_evidence) -> PackageArtifact

The packager:
- accepts already materialized records; it does not generate seeds or run Generator/Analyzer;
- validates schema and invariants before writing;
- refuses unresolved Gate 159 reconciliation or incomplete required evidence;
- writes to caller-supplied staging directory, never directly to canonical GitHub path;
- returns archive path, package SHA-256, manifest digest, report fingerprint and per-file digest inventory;
- is deterministic and side-effect-bounded;
- does not sign or attest the package.

The trusted attestor consumes only the completed immutable archive and GitHub-resolved run/artifact metadata. It does not import or execute the packager from the producer artifact.

## 10. Adversarial acceptance tests

The packager/verifier test suite must reject:
1. missing or extra package path;
2. duplicate JSON key, invalid UTF-8, BOM, NaN/Infinity or noncanonical JSON;
3. different array order for identical semantic inputs;
4. archive byte changes caused by mtime, uid/gid, file mode or file ordering;
5. absolute path, .., backslash, symlink, hardlink, device, duplicate normalized path or Unicode collision;
6. file hash/length mismatch and manifest tampering;
7. package self-hash or circular digest field;
8. missing scenario, pair, M, RUN or R row; duplicate IDs or non-contiguous R;
9. RUN/R world seed mismatch or cross-M world-seed reuse;
10. temporal-manifest key mismatch or orphan RunManifest;
11. SeedAssignment mismatch in any identity or seed field;
12. calibration/evaluation seed overlap or unavailable calibration manifest;
13. effective configuration payload changed while declared fingerprint remains unchanged;
14. matrix row changed while matrix fingerprint remains unchanged;
15. missing/invalid output incorrectly counted as abstention or zero;
16. ITT-Z mechanism marginal computed from R pooled across M;
17. RUN status-only reference-regime record incorrectly scored numerically;
18. source commit claim inconsistent with GitHub-resolved producer run;
19. producer artifact metadata from another repository/run/attempt/workflow;
20. any report marked AUTHENTICATED without independent successful attestation verification.

Existing Gate 157 regression requirements remain mandatory, including all 52 pairs and explicit TRUTH_MISSING / INVALID_OUTPUT classification.

## 11. Dependencies and implementation order

1. Gate 159 seed/configuration/manifest reconciliation must be implemented and tested before package status can be RECONCILED.
2. Current report schema and report fingerprint semantics must be frozen or versioned before packager implementation.
3. Actual calibration manifest must be materialized or immutably retrievable; a fingerprint alone cannot prove disjointness.
4. Package packager and deterministic archive tests are implemented only after explicit implementation authorization.
5. Trusted attestor workflow is implemented separately on main, under its own explicit workflow-change authorization.
6. Verifier independently validates package, provenance and attestation; it does not trust a producer-supplied status field.

## 12. Gate 164 status

- Package schema v1.0.0: DEFINED.
- Canonical JSON/JCS profile: DEFINED.
- Deterministic uncompressed tar profile: DEFINED.
- Package file inventory and required payload: DEFINED.
- M/R/RUN and 52-pair invariants: DEFINED.
- Seed/config/source identity separation: DEFINED.
- Digest dependency graph: DEFINED.
- Packager implementation: OPEN.
- Report schema freeze/version alignment: OPEN.
- Gate 159 implementation: OPEN.
- Calibration manifest availability: OPEN.
- Adversarial tests: OPEN.
- Trusted attestor and independent verifier: OPEN.
- Code/tests/workflows/CI changes: NOT PERFORMED.
- Calibration, seed-bank generation, sizing, Monte Carlo and scientific execution: NOT AUTHORIZED / NOT EXECUTED.
- main: unchanged; PR #116 remains Draft on its existing base.


## 13. Gate 165 implementability-audit qualification

Gate 165 static audit is recorded in:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_PACKAGE_IMPLEMENTABILITY_AUDIT_GATE_165_DRAFT_001.md`.

The schema in this document remains the target package contract, but it is **not currently implementable from the existing Evaluator return object alone**. The aggregation boundary omits or reduces several required source records: effective ScenarioConfig payloads, complete AnalysisContract/SeedAssignment/RunManifest identities, SealedEvidence and per-run EvaluationReport records, calibration assignments, independent Gate 159 reconciliation and GitHub-resolved producer workflow/artifact metadata. A packager must not reconstruct or invent these fields from the reduced report.

Before packager implementation, Gate 166 must freeze a typed evidence-export interface and its cardinalities, join keys, data-minimization boundary and provenance split. The package schema's effective configuration and analysis-contract cardinalities must also be clarified. Existing report and seed-bank fingerprints retain their legacy serialization semantics; package JCS digests are computed separately.

**Gate 164 state after Gate 165:** TARGET SCHEMA DEFINED / IMPLEMENTATION BLOCKED PENDING EVIDENCE-EXPORT CONTRACT. No implementation or execution authorization is implied.


## 14. Gate 166 — typed source evidence interface

Gate 166 has frozen the typed source interface in:
`00_GOVERNANCE/SIP/C10_S_VCONT_TYPED_EVIDENCE_EXPORT_CONTRACT_GATE_166_DRAFT_001.md`.

The package builder must consume the Gate 166 benchmark envelope and RunEvidenceRecords, not reconstruct records from the Evaluator's reduced report. The export retains complete SeedAssignment and RunManifest identities, exact per-run ScenarioConfig bindings plus structural projections, AnalysisContract references, matrix-relevant TruthBundle fields, SealedEvidence manifest/digest, AnalyzerResult and EvaluationReport, and one repeated aggregate report per M.

Two deliberate data-minimization constraints apply: full potential-outcome arrays are not included by default; raw SealedEvidence rows are not included by default. The latter digest is independently recomputable only if its canonical source representation is retrievable. Otherwise it remains UNVERIFIABLE and blocks RECONCILED provenance.

Gate 164 remains the target package format. Its implementation remains OPEN pending Gate 166 export implementation and Gate 159 reconciliation. No code or execution authorization is implied.

## 15. Gate 173 — package readiness and canonicalization audit

Gate 173 statically reconciled the Gate 164 v1.0.0 package contract with the source added by Gates 166–172. The typed source evidence now exists in the Gate 172 `CapturedBenchmark` envelope: exact per-run snapshots, complete RunManifest and SeedAssignment, matrix truth projection, inline SealedEvidence rows+manifest, AnalyzerResult, AnalysisContract, per-run EvaluationReport and one repeated aggregate report per scenario/M. The report-only insufficiency found at Gate 165 is therefore resolved at source-capture level, not by the aggregate report itself.

The existing exact package path inventory remains reusable; no additional archive path is required. Clarify `runs/run_records.json` as a versioned envelope containing the ordered RunEvidenceRecords (13×M×(1+R)), OuterWorldEvidenceBundles (13×M), evidence index and declared cardinalities/join keys. The exact matrix used must be included in `design/scenario_estimand_matrix.json`; it must not be reconstructed from report output.

**Canonicalization boundary:** Gate 170's FrozenSnapshot bytes use a custom tagged Python JSON serialization and their own snapshot SHA-256. The SealedEvidence legacy digest and evaluator report fingerprint also retain their existing serialization semantics. None is RFC 8785 JCS. A future package adapter must losslessly encode/decode the typed snapshots (including bytes, tuple/list distinctions, enums, nulls and numeric values), independently recompute legacy digests, and only then apply JCS to package JSON files. Package file hashes, manifest digest and final tar SHA-256 remain separate, non-circular package-layer digests.

**Still blocking RECONCILED package status:** no calibration manifest is supplied to CapturedBenchmark; Gate 159 seed/config/source reconciliation is not implemented; GitHub-resolved producer workflow/run/artifact metadata and exact technical test execution evidence are external; no JCS adapter, tar writer, independent package verifier or attestation exists.

Gate 173 verdict: source evidence availability substantially improved; package implementation remains OPEN/BLOCKED pending the Gate 174 serialization/verifier contract and explicit treatment of incomplete calibration/source provenance. No tests, CI, package generation, benchmark or scientific execution occurred. See `C10_S_VCONT_MONTE_CARLO_PACKAGE_READINESS_AND_CANONICALIZATION_AUDIT_GATE_173_DRAFT_001.md`.


**Explicit supersession of §14 raw-row default:** Gate 168 selected inline canonical SealedEvidence rows+manifest for this V_cont package lineage, and Gate 173 confirms that Gate 170/172 snapshots retain those rows in source memory. Therefore the §14 statement that raw SealedEvidence rows are excluded by default is historical and does not govern this package lineage. The package `runs/run_records.json` envelope must preserve the exact rows and manifest and the verifier must recompute the legacy SealedEvidence digest after decoding. This does not require full TruthBundle potential-outcome arrays; the Gate 166 matrix truth projection remains the data-minimization boundary.

## 16. Gate 174 — serialization and independent verifier contract

Gate 174 freezes the package serialization boundary without implementing it. The exact 14-file Gate 164 v1.0.0 inventory, JCS profile, deterministic uncompressed POSIX tar profile and digest dependency graph remain unchanged.

The existing `runs/run_records.json` path is now specified as `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE v1.0.0`: ordered RUN/R RunEvidenceRecords, one OuterWorldEvidenceRecord per scenario/M, exact repeated aggregate report once per M, evidence index, declared cardinalities and explicit join keys. Each source snapshot is carried as base64 of its exact existing `FrozenSnapshot.canonical_bytes`, together with type ID, serialization ID and SHA-256. This preserves source bytes and does not relabel their custom tagged JSON digest as JCS. The containing package JSON file is separately JCS-canonicalized.

Gate 174 also identifies a decoder requirement: the current snapshot `_decode` returns an enum's underlying value rather than restoring the registered enum type, and the encoder rejects arbitrary bytes. A future adapter must use a versioned allowlisted type/enum registry, reject unsupported values, and prove exact round-trip; current source does not justify a universal type-preserving claim.

**Profile decision:** Gate 164 CONFIRMATORY v1.0.0 is fail-closed. Missing actual calibration manifest, Gate 159 reconciliation, independently resolved GitHub source/workflow metadata, or required technical test evidence prevents acceptance. No placeholder manifest or producer PASS can satisfy it. A possible diagnostic partial-transport profile must use a distinct schema ID/version and cannot be labelled Gate 164-compliant, RECONCILED or AUTHENTICATED; its schema is not defined here.

The independent verifier is a separate implementation boundary and returns separate integrity, schema, completeness, reconciliation, source provenance, test evidence and attestation statuses. It does not trust producer validation flags. Full contract: `C10_S_VCONT_PACKAGE_SERIALIZATION_AND_INDEPENDENT_VERIFIER_CONTRACT_GATE_174_DRAFT_001.md`.

Gate 174 status: serialization/verifier contract DEFINED; packager, decoder, verifier and tests NOT IMPLEMENTED/NOT EXECUTED. Next Gate 175 audits actual type/schema/API implementability before any serializer implementation.
