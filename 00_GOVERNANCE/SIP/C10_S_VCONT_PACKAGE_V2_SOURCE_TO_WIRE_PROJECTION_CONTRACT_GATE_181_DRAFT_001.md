# C10-S V_cont — Gate 181: package v2 source-to-wire projection contract

**Status:** SOURCE-TO-WIRE PROJECTIONS DEFINED — IMPLEMENTATION CONTRACT STILL REQUIRED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 180 package v2 source-schema crosswalk audit  
**Scope:** exact direct uint64 registry, effective ScenarioConfig projection, report projection/fingerprint order, companion assembly and 14-file verifier crosswalk  
**Execution:** GitHub source/document inspection only; no code edits, imports, compilation, tests, CI, seed generation, calibration, package generation, benchmark or scientific execution

## 1. Gate disposition

Gate 181 closes the source-to-wire **design decisions** left open by Gate 180. It does not claim that the current harness implements these projections. The current `CapturedBenchmark` API still lacks MatrixCapture and FrozenReportSnapshot retention, and the package writer/verifier and companion assembler do not exist.

The following are now normative for the v2.0.0 successor:

1. The direct uint64 registry includes every cleartext occurrence visible in the source report and package schema, including duplicated report pair-ledger and temporal-manifest views.
2. `design/effective_scenario_configs.json` is a structural DGP/Generator projection and MUST NOT contain direct seed values or run-assignment identities. All three actual RNG streams are supplied explicitly by the evaluation SeedAssignment rows; the legacy `ScenarioConfig.seed` fallback is forbidden in confirmatory capture. Exact RUN/R config snapshots remain preserved as opaque FrozenSnapshot bytes in `runs/run_records.json`.
3. The legacy report fingerprint is recomputed from the original source-typed `manifest_payload` using the frozen historical algorithm **before** uint64 wire projection. The v2 report snapshot/JCS digest is computed separately over the complete typed v2 projection.
4. Capture identity commits only to evaluation capture content. Calibration, Gate159, source-execution and technical-test evidence are independent companion inputs joined by `benchmark_export_id`; they do not enter `capture_id`. The final package identity commits to the companion digests.
5. The 14-file inventory is unchanged; each path has a defined source and verification role.

This is a documentary schema closure, not implementation acceptance or authorization.

## 2. Exact direct uint64 field registry v2.0.0

Wire representation at every listed location:

```json
{"$type":"uint64","decimal":"<canonical unsigned decimal>"}
```

Exact wrapper validation, decimal grammar, uint64 range and JCS handling are inherited from Gate 179 §2. A typed wrapper is required only at the exact registered paths below; it is not a generic arbitrary-integer escape.

### 2.1 Machine-readable path registry

JSON Pointer patterns use `*` for array indices. Each pointer is rooted at the JSON file payload (not at the archive root).

| Package file | JSON Pointer pattern | Source object / field | Relation |
|---|---|---|---|
| `seeds/evaluation_seed_assignments.json` | `/rows/*/world_seed` | evaluation SeedAssignment.world_seed | Source row |
| same | `/rows/*/z_assignment_seed` | evaluation SeedAssignment.z_assignment_seed | Source row |
| same | `/rows/*/g_assignment_seed` | evaluation SeedAssignment.g_assignment_seed | Source row |
| `seeds/calibration_seed_manifest.json` | `/rows/*/world_seed` | calibration SeedAssignment.world_seed | Source row |
| same | `/rows/*/z_assignment_seed` | calibration SeedAssignment.z_assignment_seed | Source row |
| same | `/rows/*/g_assignment_seed` | calibration SeedAssignment.g_assignment_seed | Source row |
| `runs/temporal_manifest.json` | `/rows/*/world_seed` | RunManifest.world_seed | Joins evaluation row |
| same | `/rows/*/z_assignment_seed` | RunManifest.z_assignment_seed | Joins evaluation row |
| same | `/rows/*/g_assignment_seed` | RunManifest.g_assignment_seed | Joins evaluation row |
| `report/report.json` | `/temporal_manifest/*/world_seed` | report temporal manifest | Same value as runs temporal row |
| same | `/temporal_manifest/*/z_assignment_seed` | report temporal manifest | Same value as runs temporal row |
| same | `/temporal_manifest/*/g_assignment_seed` | report temporal manifest | Same value as runs temporal row |
| same | `/manifest/temporal_manifest/*/world_seed` | legacy manifest temporal copy | Exact duplicate of report root temporal row |
| same | `/manifest/temporal_manifest/*/z_assignment_seed` | legacy manifest temporal copy | Exact duplicate of report root temporal row |
| same | `/manifest/temporal_manifest/*/g_assignment_seed` | legacy manifest temporal copy | Exact duplicate of report root temporal row |
| same | `/pair_ledger/*/contributions/*/world_seed` | pair-ledger contribution | Joins scenario/M RUN evidence |
| same | `/manifest/pair_ledger/*/contributions/*/world_seed` | legacy manifest pair-ledger copy | Exact duplicate of report root contribution |
| `runs/run_records.json` | `/outer_world_evidence_records/*/key/world_seed` | OuterWorldEvidenceBundle key | Joins RUN and repeated snapshots in that M |

No direct seed fields are permitted in the remaining package JSON fields unless a future schema version explicitly adds them to this registry. In particular, the v2 registry marks `design/effective_scenario_configs.json` as seed-free direct JSON; see §3. Opaque snapshot bytes are not direct JSON occurrences and are handled under §3.4.

### 2.2 Equality and joins

The v2 verifier MUST check all of the following after decoding typed uint64 values:

- evaluation SeedAssignment row ↔ RunManifest row: exact one-to-one match on bank, scenario/version, N, outer ID, role, assignment index and all three seed values;
- RUN/R within one scenario/M: identical world_seed; assignment Z/G seeds remain distinct as required by the seed-bank contract;
- every report temporal row ↔ exactly one evaluation assignment and one captured RunManifest;
- report root temporal row ↔ its nested `manifest.temporal_manifest` copy: exact equality of every field;
- report root pair-ledger row ↔ nested `manifest.pair_ledger` row: exact equality of every field, including ordered contributions;
- each pair-ledger contribution world_seed ↔ the world_seed of the unique RUN evidence record for that scenario/M;
- `runs/run_records.json` outer-world key.world_seed ↔ the corresponding RUN/R snapshot RunManifest world_seed and evaluation assignment.

A mismatch is a reconciliation FAIL, not a normalization opportunity. The verifier MUST NOT sort, coerce, fill or silently repair mismatched records.

### 2.3a Exact root envelopes for the registered row arrays

To make the JSON Pointer registry in §2.1 unambiguous, the following v2.0.0 file envelopes are normative.

**Evaluation assignments** — `seeds/evaluation_seed_assignments.json`:
- `schema_id` = `TGCV-C10S-VCONT-EVALUATION-SEED-ASSIGNMENTS`;
- `schema_version` = `2.0.0`;
- `bank` = `evaluation`;
- `row_count`;
- `seed_derivation` with algorithm `TGCV-C10S-VCONT-SEED-v3`, hash `SHA-256`, output rule `first_8_digest_bytes_unsigned_big_endian`, and declared namespace;
- `seed_bank_fingerprint_legacy`;
- `rows`, exact ordered SeedAssignment projections.

Each evaluation row contains exactly `bank`, `scenario_id`, `scenario_version`, `n_units`, `replicate`, `outer_replicate_id`, `assignment_role`, `world_seed`, `z_assignment_seed`, `g_assignment_seed`. `replicate` is the source dataclass field; `assignment_index` is its runtime alias and is not emitted as a second independent value.

**Temporal manifest** — `runs/temporal_manifest.json`:
- `schema_id` = `TGCV-C10S-VCONT-TEMPORAL-MANIFEST`;
- `schema_version` = `2.0.0`;
- `row_count`;
- `rows`, exact ordered RunManifest projections.

Each temporal row contains exactly `scenario_id`, `scenario_version`, `N`, `outer_replicate_id`, `assignment_role`, `assignment_index`, `run_id`, `world_id`, `world_seed`, `z_assignment_seed`, `g_assignment_seed`. Row order is authoritative scenario order, numeric M order, RUN first, then numeric R order.

**Calibration assignments** — `seeds/calibration_seed_manifest.json` use the Gate 178 CalibrationBankManifest envelope, versioned to 2.0.0 by Gate 179. Its existing exact `rows` member and row schema are retained; only the three seed values use the typed uint64 wire object.

The `report/report.json` remains the FrozenReportSnapshot v2.0.0 envelope defined in §4.3. The `runs/run_records.json` root and `outer_world_evidence_records` member retain the Gate 174 RUN-EXPORT-ENVELOPE structure, version 2.0.0.

### 2.3b Pointer registry root convention

All pointers in §2.1 are now rooted at the file JSON object. In particular, the three assignment/temporal row collections are explicitly `/rows/*`; calibration uses its Gate 178 `rows` member. This removes any assumption that these files are bare top-level arrays. Any implementation emitting a different root shape is nonconforming and must fail closed.

### 2.3 Prohibited direct-seed locations

The following are not direct uint64 fields in v2.0.0:
- `manifest.json` package identity and file-digest records;
- `design/benchmark_design.json` declared design metadata and historical fingerprints;
- `design/scenario_estimand_matrix.json`;
- `design/analysis_contracts.json`;
- `provenance/source_execution.json`;
- `provenance/configuration_fingerprints.json`;
- `validation/reconciliation_results.json`;
- `validation/test_evidence.json`.

If an implementation emits a seed value in any of these paths, the verifier MUST reject schema drift. It must not silently expand the registry.

## 3. EffectiveScenarioConfigProjection v2.0.0

Schema ID: `TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION`; version: `2.0.0`.

### 3.1 Projection purpose and row key

This file represents the structural DGP/Generator configuration by scenario/version/N, not each stochastic assignment or run identity.

Each row has exactly:
- `scenario_id`;
- `scenario_version`;
- `n_units`;
- `generator_version` (exact Generator.version);
- `seed_policy`;
- `config` (the structural field object defined in §3.2).

Rows are ordered by authoritative `SCENARIO_IDS` order, then ascending N if a future design contains more than one N. Duplicate row keys are rejected. For the current single-N design there is exactly one row per registered scenario.

### 3.2 Exact structural config fields

The `config` object contains exactly the following source ScenarioConfig fields, mapped without renaming or numeric coercion:

- `profile`
- `mechanism`
- `n_intervals`
- `window_start`
- `last_transition_support`
- `follow_up`
- `enabled_probability`
- `baseline_conformity`
- `focal_access_effect`
- `package_direct_effect`
- `focal_direct_effect`
- `collateral_effect`
- `provision_probability`
- `alternative_probability`
- `heterogeneity`
- `interference_effect`
- `measurement_sensitivity`
- `measurement_specificity`
- `missing_probability`
- `randomized_z`
- `randomized_g`
- `positivity`
- `no_interference`
- `measurement_identified`
- `version_consistency`
- `zg_interaction_effect`

The row key carries `scenario_id`, `scenario_version` and `n_units`; they MUST NOT be duplicated inside `config`.

### 3.3 Explicit exclusions and their authoritative locations

The following source ScenarioConfig fields are excluded from direct structural config JSON:

| Source field | Reason | Authoritative retained location |
|---|---|---|
| `seed` | Legacy fallback seed; forbidden for confirmatory capture | Exact per-run ScenarioConfig FrozenSnapshot bytes in run_records; fallback must not be used |
| `world_seed` | Stochastic assignment identity, not structural DGP parameter | Evaluation SeedAssignment rows, temporal manifest and RunManifest snapshots |
| `z_assignment_seed` | Stochastic assignment identity | Same |
| `g_assignment_seed` | Stochastic assignment identity | Same |
| `replicate_id` | Per-run identity | RunManifest / run record |
| `outer_replicate_id` | M-world identity | Assignment rows, temporal manifest and outer-world key |
| `assignment_role` | RUN/R identity | Assignment rows and RunManifest |
| `assignment_index` | RUN/R identity | Assignment rows and RunManifest |

`seed_policy` is exactly:

```json
{
  "mode": "EXPLICIT_ASSIGNMENT_STREAMS_REQUIRED",
  "source": "SeedAssignment",
  "streams": ["world_seed", "z_assignment_seed", "g_assignment_seed"],
  "fallback": "FORBIDDEN",
  "algorithm": "TGCV-C10S-VCONT-SEED-v3"
}
```

The producer MUST reject any effective RUN/R ScenarioConfig whose three explicit stream seeds are absent or do not exactly match the corresponding SeedAssignment row. The legacy `seed` field remains preserved in the opaque run config snapshot and is not deleted or rewritten; the confirmatory producer MUST demonstrate by the explicit-stream precondition that it was not used as an RNG fallback.

This exclusion is justified by the actual Generator source: it derives world/Z/G RNG seeds from the three explicit fields when present and removes `seed`, the three stream seeds, `replicate_id`, `assignment_role` and `assignment_index` from the structural `world_spec`. The run snapshot retains the full original effective ScenarioConfig, while the assignment manifest independently retains exact stream values. `outer_replicate_id` is retained in run/world identity and in its explicit assignment identity fields, not as a structural parameter.

### 3.4 Opaque run config snapshots

Each RunEvidenceBundle continues to retain its exact effective ScenarioConfig as a registered FrozenSnapshot inside `runs/run_records.json`. The v2 package envelope transports:
- snapshot type ID and schema/version identity;
- exact canonical-bytes base64;
- SHA-256 of the exact bytes.

The package writer MUST NOT decode, edit, normalize or reserialize these legacy snapshot bytes to construct the structural config file. The independent verifier checks the byte digest and allowlisted type/schema identity, then may decode under the separately versioned legacy snapshot decoder. Direct uint64 wrappers do not apply inside the opaque byte string. After a supported decode, the verifier reconciles the snapshot's seed fields to the evaluation assignment row; undecodable or identity-losing snapshots yield UNVERIFIABLE, not PASS.

## 4. FrozenReportSnapshot and legacy report fingerprint ordering

### 4.1 Source report shape

The current Evaluator returns:
- root `temporal_manifest`;
- root `pair_ledger`;
- nested legacy `manifest.temporal_manifest`;
- nested legacy `manifest.pair_ledger`;
- `report_fingerprint`;
- coverage, design and scenario summaries.

Each pair-ledger row contains an ordered `contributions` array. Every contribution includes `world_seed`; the same pair-ledger array is copied into `manifest_payload`.

### 4.2 Historical fingerprint algorithm — frozen input domain

The historical report fingerprint is computed by the current source from the source-typed `manifest_payload`:

1. Construct `manifest_payload` with its original fields and source-typed temporal/pair-ledger rows.
2. Apply the existing source conversion `json.loads(json.dumps(manifest_payload, default=asdict, sort_keys=True))`.
3. Apply the existing `_hash(...)` implementation, which executes `json.dumps(obj, sort_keys=True, separators=(\",\", \":\"), allow_nan=False)`, encodes UTF-8 and returns lowercase SHA-256 hex.
4. Store the result as the legacy `report_fingerprint`.

The frozen algorithm identifier for this exact two-stage process is `TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1`. It is a source-compatibility identifier, not an RFC 8785/JCS profile.

This order MUST be preserved. The input is the original source-domain manifest payload, not JCS bytes, not uint64 wrapper dictionaries and not the complete report root. The duplicated root views are equality-checked against the nested manifest views, but they are not independently inserted into the historical fingerprint input.

The v2 serializer MUST first preserve/calculate this historical fingerprint from source-typed objects, then construct the typed v2 report projection. A verifier reverses the process: decode wrappers to exact source integers, validate duplicate root/nested equality, reconstruct the exact legacy manifest payload, then recompute the legacy fingerprint using the frozen algorithm. It separately verifies JCS report snapshot and package digests.

### 4.3 FrozenReportSnapshot v2.0.0 payload

Schema ID: `TGCV-C10S-VCONT-REPORT-SNAPSHOT`; version: `2.0.0`.

Exact envelope fields:
- `schema_id`;
- `schema_version`;
- `payload_type` = `TGCV-C10S-VCONT-BENCHMARK-REPORT`;
- `legacy_report_fingerprint`;
- `legacy_fingerprint_algorithm` = exact source algorithm identifier frozen by Gate 164;
- `report` = complete report root projection.

The report projection retains all source report fields and order. All direct uint64 occurrences are replaced at the exact registered paths in §2.1. No other field is omitted or added. The nested `manifest` is preserved, including its duplicate temporal and pair-ledger views. The envelope digest is SHA-256 over RFC 8785 JCS of this exact envelope. It is distinct from the historical report fingerprint.

The compatibility `CapturedBenchmark.report` remains the legacy source-typed dictionary. The snapshot is captured immediately after Evaluator returns and is immutable; later mutation of the compatibility dictionary MUST NOT mutate the snapshot.

## 5. Capture identity and companion assembly

### 5.1 Capture identity v2.0.0

Schema ID: `TGCV-C10S-VCONT-BENCHMARK-CAPTURE-IDENTITY`; version: `2.0.0`.

Identity payload fields:
- schema ID/version;
- exact design identity projection;
- MatrixCapture full digest;
- evaluation SeedAssignment ordered-manifest digest under v2 typed uint64 projection;
- ordered OuterWorldEvidenceBundle digests, each committing to outer-world key, ordered RUN/R snapshot type IDs and exact snapshot SHA-256 values, and repeated-assignment report snapshot digest;
- FrozenReportSnapshot digest;
- exact ordered evidence_index.

Derivation:
- `capture_id = lowercase_hex(SHA256(JCS(identity_payload)))`;
- `benchmark_export_id = capture_id`.

Neither identifier is included in its own input. Calibration, Gate159, source-execution, technical-test companions, wall-clock timestamps, mutable paths, caller-supplied PASS flags and externally retrieved GitHub metadata are excluded from capture identity.

### 5.2 Separate companion assembly interface

The package writer MUST accept a distinct `VContPackageCompanionsV2` input containing references/content for:
- actual CalibrationBankManifest v2.0.0 and its exact materialized calibration assignment rows;
- Gate159ReconciliationArtifact v1.0.0;
- independently resolved source-execution evidence;
- independently resolved technical-test execution evidence.

Each companion is validated against `benchmark_export_id`, design identity, relevant source/artifact digests and declared applicability. The package writer MUST NOT synthesize these artifacts from the captured evaluation report or accept a caller-provided PASS boolean in place of the artifact.

Missing required confirmatory companion → package status BLOCKED / NOT CONFIRMATORY. A diagnostic package may represent explicit unavailable states only under its separately declared diagnostic profile; it MUST NOT be labelled confirmatory or reconciled/authenticated.

Companion content is excluded from `capture_id` to keep capture identity independent of external evidence. It is included in the final package manifest file digests and package ID, so changing a companion changes the package identity without changing the underlying capture identity.

### 5.3 Package identity layers

Keep these identities separate:
- `capture_id`: evaluation capture content;
- `benchmark_export_id`: alias of capture_id for companion joins;
- `package_id`: deterministic digest over v2 package manifest inputs including all 14 file digests and companion content;
- archive SHA-256: digest of the final deterministic TAR bytes;
- detached external attestation/receipt: outside the 14-file package and bound to the exact archive digest.

No identity substitutes for another.

## 6. Exact 14-file source/projection/verification crosswalk

| Path | Source / projection | Required verifier operation |
|---|---|---|
| `manifest.json` | v2 package envelope, exact file inventory, lengths/digests, profile, package ID inputs | Exact schema, inventory, JCS, digest and non-circular identity checks |
| `report/report.json` | FrozenReportSnapshot v2.0.0 report projection | All report uint64 pointers, duplicate-view equality, legacy fingerprint recomputation and JCS digest |
| `design/benchmark_design.json` | Frozen MonteCarloBenchmarkDesign projection | Exact N/M/R, scenario/version, targets, declared fingerprints; declarations are not independent proof |
| `design/scenario_estimand_matrix.json` | MatrixCapture v1.0.0 | Exactly 52 canonical rows, full digest and separate historical fingerprint |
| `design/effective_scenario_configs.json` | EffectiveScenarioConfigProjection v2.0.0 | Exact field allowlist, row keys/order, explicit-stream policy; reject seed/assignment fields |
| `design/analysis_contracts.json` | Exact effective AnalysisContract projection | Exact per-scenario/run-family identity and source mapping |
| `seeds/evaluation_seed_assignments.json` | Exact ordered evaluation SeedAssignment rows | Direct uint64 decode, canonical order, cardinality and historical fingerprint recomputation |
| `seeds/calibration_seed_manifest.json` | CalibrationBankManifest v2.0.0 | Direct uint64 decode, independent design/cardinality and evaluation/calibration disjointness |
| `runs/temporal_manifest.json` | RunManifest projection for all RUN/R | Direct uint64 decode and one-to-one joins to assignment and run records |
| `runs/run_records.json` | RUN/R and outer-world typed evidence envelopes with opaque snapshots | Strict envelope schema, exact bytes/digests, run/world joins and direct outer key uint64 |
| `provenance/source_execution.json` | Independently resolved repository/workflow/run/attempt/event/ref/commit/tree/artifact evidence | Independent source/workflow/artifact reconciliation; no producer self-assertion |
| `provenance/configuration_fingerprints.json` | Recomputed structural config and effective analysis contract digests | Recompute from exact projections; compare declarations |
| `validation/reconciliation_results.json` | Gate159ReconciliationArtifact v1.0.0 | Verify exact checks, inputs, counts, statuses and derived status |
| `validation/test_evidence.json` | Independently retrieved technical test execution evidence | Bind exact workflow/run/commit/test artifact; test definitions are not execution evidence |

No fifteenth file is introduced. The package contains only these paths; detached attestations remain outside the archive.

## 7. Gate 181 implementation boundary and regression requirements

### 7.1 Source compatibility

The future implementation MUST:
- preserve the existing three positional `CapturedBenchmark` fields and their meanings;
- add trailing optional `matrix_capture` and `report_snapshot` fields for legacy construction compatibility;
- ensure producer-created captures populate both;
- capture the exact validated matrix tuple before/at evaluator invocation without sorting/rebuilding;
- snapshot the report immediately after Evaluator returns;
- preserve the mutable legacy `report` view for current consumers, while freezing the separate report snapshot;
- require explicit three-stream seed equality for every effective RUN/R config;
- keep Generator, Sealer, Analyzer, Evaluator and scientific estimands unchanged.

### 7.2 Required regression vectors — specified, not executed

1. Every JSON Pointer in §2.1 contains exactly one typed uint64 wrapper per source value.
2. Root/nested temporal manifest arrays are exactly equal after decoding.
3. Root/nested pair-ledger arrays and contribution order are exactly equal after decoding.
4. Mutating any one of the duplicated copies yields reconciliation FAIL.
5. Every RUN/R config has all three explicit stream seeds and they match the exact SeedAssignment row; missing/null/mismatch fails closed.
6. Effective config projection contains exactly the §3.2 structural fields and none of the §3.3 exclusions.
7. Changing any structural field changes the effective config digest.
8. Changing any assignment seed changes the assignment manifest digest and capture_id, but does not change the structural config digest.
9. Changing only opaque snapshot bytes changes the relevant bundle digest and capture_id.
10. Mutating compatibility report after capture does not mutate FrozenReportSnapshot.
11. Legacy report fingerprint computed before wire projection equals the independently recomputed fingerprint after wrapper decoding.
12. Attempting to recompute the historical fingerprint over wrapper dictionaries is detected as a mismatch.
13. Companion changes alter package_id but do not alter capture_id.
14. Missing required companion blocks confirmatory package output.
15. All 14 paths present exactly once; extra/missing/duplicate path rejected.
16. Any unregistered direct seed field or bare numeric value at a registered field is rejected.
17. Snapshot bytes are byte-identical through packaging and digest verification.
18. v1/v2 cross-version verifier rejection remains mandatory.

These are test specifications only. Gate 181 executed no tests or code.

## 8. Gate 181 disposition

| Item | State |
|---|---|
| Complete direct uint64 field registry | DEFINED |
| EffectiveScenarioConfigProjection v2.0.0 | DEFINED |
| Explicit stream-seed precondition | DEFINED |
| Legacy report fingerprint order/input | DEFINED |
| FrozenReportSnapshot v2.0.0 projection | DEFINED |
| Capture identity / companion separation | DEFINED |
| 14-file source/projection/verifier crosswalk | DEFINED |
| Existing CapturedBenchmark implementation | NOT YET UPDATED |
| MatrixCapture / FrozenReportSnapshot capture | NOT IMPLEMENTED |
| Companion assembler | NOT IMPLEMENTED |
| Package writer / independent v2 verifier | NOT IMPLEMENTED |
| Tests / CI | NOT EXECUTED |
| Seed generation / calibration / package / benchmark / scientific execution | NOT AUTHORIZED / NOT EXECUTED |
| Main / canonical state / PR base | UNCHANGED |

**Overall:** `SOURCE-TO-WIRE CONTRACT DEFINED — IMPLEMENTATION CONTRACT REQUIRED`. Gate 181 closes the schema-level ambiguities from Gate 180. It does not establish that the contract is implemented or authorize implementation/execution.

## 9. Next operation — Gate 182

Gate 182 should translate this closed source-to-wire contract into a bounded implementation contract with:
- exact modules/functions and additive API changes;
- immutable MatrixCapture and FrozenReportSnapshot capture points;
- strict v2 serializers/decoders and field-registry enforcement;
- independent companion assembler and package writer/verifier;
- migration/compatibility tests for the existing three-field CapturedBenchmark consumers;
- explicit non-goals preserving Generator/Sealer/Analyzer/Evaluator semantics.

After static reconciliation of that implementation contract, implementation and test execution require their governed authorization. No scientific execution is implied.

## 10. Gate 182 — implementation contract

Gate 182 translates the Gate 181 projections into a bounded implementation contract. It preserves the three existing CapturedBenchmark fields and adds trailing optional MatrixCapture, FrozenReportSnapshot and capture_id fields. The producer must capture the exact canonical matrix tuple before Evaluator and freeze the report immediately after Evaluator returns. The v2 writer and independent verifier are separate modules and must not invoke Generator/Sealer/Analyzer/Evaluator.

Gate 182 explicitly versions the envelope migration: Gate 174 RUN-EXPORT-ENVELOPE v1.0.0 retains design-derived benchmark_export_id; v2.0.0 uses benchmark_export_id=capture_id. It also requires a pinned RFC 8785 dependency before serializer implementation. Full API, module boundaries, compatibility, test plan and acceptance criteria are in Gate 182. Implementation remains NOT IMPLEMENTED; no tests or scientific execution occurred.
