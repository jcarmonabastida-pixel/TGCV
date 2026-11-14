# C10-S V_cont — Gate 178: capture/export serialization and companion schemas

**Status:** CONTRACT RECONCILIATION — CONDITIONAL / GATE 164 v1.0.0 WIRE-FORMAT BLOCKER  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 177 capture/export implementability audit  
**Scope:** exact MatrixCapture, FrozenReportSnapshot, deterministic capture identity, calibration/Gate 159 companion schemas, strict decoder and regression contract  
**Execution:** source/document inspection only; no code changes, imports, compilation, tests, CI, seed generation, calibration, package generation, benchmark or scientific execution

## 1. Executive disposition

Gate 178 closes the contract details that can be specified from the current source and identifies one package-schema incompatibility that prevents an honest implementation claim.

The following are now specified:

1. Exact 52-row MatrixCapture schema, value domains, positional order and full-matrix digest input.
2. FrozenReportSnapshot payload and its separation from the legacy report fingerprint and mutable compatibility dictionary.
3. Non-circular deterministic `capture_id` derivation; `benchmark_export_id` is an alias of that identity.
4. CalibrationBankManifest and Gate159ReconciliationArtifact schemas, row keys, cardinality and status derivation.
5. Strict snapshot decoder behavior and an explicit regression matrix.
6. Compatibility constraints for the existing three-field CapturedBenchmark API.

**Blocking incompatibility:** SeedAssignment seeds are generated as unsigned 64-bit integers. Gate 164 v1.0.0 requires JCS serialization and prohibits numeric-to-string coercion. JCS/ECMAScript number semantics cannot preserve every uint64 integer exactly. The package schema therefore needs an explicit, versioned typed uint64 wire representation (or another formally specified exact encoding) before a conformant package writer can be implemented. Gate 178 does not silently amend or relabel Gate 164 v1.0.0.

No scientific estimand, DGP, N/R/M meaning, Generator, Sealer, Analyzer or Evaluator behavior is changed.

## 2. MatrixCapture v1.0.0 — exact schema

Schema ID: `TGCV-C10S-VCONT-MATRIX-CAPTURE`; version: `1.0.0`.

### 2.1 Envelope

The data-only MatrixCapture envelope contains exactly:

- `schema_id`
- `schema_version`
- `design_identity`
- `row_count` (exact integer 52)
- `rows` (exactly 52 ordered rows)
- `legacy_matrix_fingerprint`
- `full_matrix_digest_algorithm` (exact value `TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1`)
- `full_matrix_sha256`

The capture identity fields are attached by the enclosing CapturedBenchmark/export envelope after the identity digest is computed. They are not included in the full-matrix digest input.

`design_identity` contains the declared scenario/version pairs in authoritative scenario order, N, M, R and the legacy matrix fingerprint. It does not assert that declared seed/configuration/executable fingerprints have been independently reconciled.

### 2.2 Exact row fields

Every row contains exactly these fields:

| Field | Type and constraint |
|---|---|
| `key` | Object with exactly `scenario_id`, `scenario_version`, `estimand_id`, `estimand_version`; all non-empty strings |
| `evaluation_class` | One of `EVALUABLE`, `STATUS_ONLY`, `NOT_IDENTIFIABLE`, `NOT_EVALUABLE` |
| `truth_status` | One of `DEFINED`, `UNDEFINED`, `NOT_MATERIALIZED` |
| `dgp_truth_field` | Non-empty string |
| `analyzer_output_field` | Non-empty string or explicit null |
| `aggregation_field` | Non-empty string or explicit null |
| `identification_expectation` | One of `IDENTIFIED`, `NOT_IDENTIFIED`, `INDETERMINATE` |
| `abstention_expectation` | Exact JSON boolean; integers 0/1 are rejected |
| `tolerance_id` | Non-empty string or explicit null |
| `reason` | Non-empty string |
| `run_evaluation_class` | One of the EvaluationClass values or explicit null |
| `repeated_evaluation_class` | One of the EvaluationClass values or explicit null |

Missing and extra fields are rejected. Null is not equivalent to a missing field. No coercion from Enum, integer, boolean or arbitrary object is permitted; source Enum values are projected explicitly to their declared stable strings.

### 2.3 Canonical row order

The only valid row sequence is:

1. `SCENARIO_IDS` in its exact source-defined tuple order;
2. within each scenario, the four estimands in exact `ESTIMAND_SPECS` tuple order.

The sequence is positional, not a set comparison. A permutation is rejected even if all 52 keys and the legacy fingerprint remain unchanged. No post-capture sorting is allowed to repair a noncanonical input.

The exact same validated `specs` tuple/value sequence must be used to create MatrixCapture and passed to `evaluate_monte_carlo_benchmark()`.

### 2.4 Full-matrix digest

Digest input:

```json
{
  "schema_id": "TGCV-C10S-VCONT-MATRIX-CAPTURE",
  "schema_version": "1.0.0",
  "row_count": 52,
  "rows": ["the exact 52 row objects, in canonical order"]
}
```

The actual `rows` value is the full row array, not the explanatory string shown above.

Canonicalization: RFC 8785 JCS; UTF-8; no BOM; no trailing LF in the digest input. Digest: lowercase SHA-256 hex over the exact canonical bytes.

The digest includes every row field, all four nested key fields, explicit nulls, `tolerance_id`, and canonical row order. The legacy `scenario_matrix_fingerprint()` remains byte-for-byte unchanged and is independently recomputed under its historical algorithm. It is not replaced by the full digest.

Required metamorphic regressions:
- changing only `tolerance_id` changes the full digest;
- changing any key or row field changes the full digest;
- permuting rows is rejected before digest acceptance;
- missing, extra, duplicate, wrongly typed or unknown-valued fields are rejected;
- explicit null and absent field do not collapse to the same representation.

## 3. FrozenReportSnapshot v1.0.0

Schema ID: `TGCV-C10S-VCONT-REPORT-SNAPSHOT`; version: `1.0.0`.

### 3.1 Envelope

Exact fields:

- `schema_id`
- `schema_version`
- `payload_type` = `TGCV-C10S-VCONT-BENCHMARK-REPORT`
- `payload_version` = `1.0.0`
- `canonicalization` = `RFC8785-JCS`
- `canonical_bytes` (retained bytes; package transport uses base64)
- `sha256` (SHA-256 over those exact bytes)

### 3.2 Exact report payload projection

The payload is a typed, data-only projection of the current Evaluator report with exactly these top-level members:

- `design`
- `temporal_manifest`
- `pair_ledger`
- `manifest`
- `scenario_reports`
- `coverage`
- `report_fingerprint`

The `design` projection contains the exact declared MonteCarloBenchmarkDesign fields: `scenario_versions`, `n_units`, `outer_replicates`, `repeated_assignments`, `matrix_fingerprint`, `metric_targets`, `seed_bank_label`, `seed_bank_fingerprint`, `executable_commit`, `configuration_fingerprint`.

The pair ledger preserves all 52 records, their ordered contributions, all status/numeric denominators and counts, metrics, MCSE/precision states, explicit nulls and temporal source. The temporal manifest preserves all 13×M×(1+R) identities. Scenario report substructures are projected under a versioned allowlist matching the current evaluator output; unknown fields or schema drift require a report payload version increment, not silent omission.

The `manifest` member preserves the evaluator's exact legacy manifest payload. The legacy `report_fingerprint` is preserved unchanged. It is not recomputed using JCS and is not treated as the snapshot digest.

### 3.3 Snapshot timing and compatibility

Capture the immutable report bytes immediately after `evaluate_monte_carlo_benchmark()` returns and before returning CapturedBenchmark. Existing fields and shapes remain unchanged:

- `report` remains the existing mutable dict compatibility view;
- `outer_world_bundles` remains unchanged;
- `evidence_index` remains unchanged.

New fields are trailing optional fields only, preserving the existing three-positional-argument constructor. Producer-created captures MUST populate `matrix_capture` and `report_snapshot`. A missing field is permitted only for legacy object construction/consumption and MUST fail confirmatory export validation. Mutation of `report` after capture never refreshes or overwrites snapshot bytes.

## 4. JCS implementation and strict input domain

### 4.1 Selected Python implementation

The selected implementation candidate is **`rfc8785==0.1.4`**, a pure-Python, no-runtime-dependency implementation exposing UTF-8 byte output. The exact dependency pin must be added to the project dependency/lock mechanism at the later authorized implementation preflight, with the resolved distribution artifact hash recorded. No dependency file is present at the inspected harness root; Gate 178 therefore does not claim that the package is installed or locked.

The normative behavior is RFC 8785, not a particular library's undocumented behavior. The selected library must pass the full RFC vectors and the C10-S vectors below before it can be used for any evidence digest. A second independent implementation must reproduce the same bytes for the project-specific vectors before the package verifier is accepted.

### 4.2 I-JSON and numeric restrictions

Reject:
- NaN and positive/negative infinity;
- invalid Unicode, unpaired surrogates and invalid UTF-8;
- duplicate object member names;
- non-string object keys;
- implicit coercion of enums, bytes, tuples, integers, booleans or null;
- integers that cannot be represented exactly under the declared JCS wire type.

**uint64 issue:** `_derive_seed()` takes the first eight SHA-256 digest bytes and converts them to an unsigned big-endian integer. These values occupy the uint64 domain. JCS uses ECMAScript IEEE-754 number serialization; exact integer representation is not guaranteed above 9007199254740991. The existing Gate 164 seed files and temporal/report projections include seed values as numeric fields, while Gate 164 §4.1 disallows string coercion.

Consequently, Gate 164 v1.0.0 is not yet proven capable of losslessly carrying the actual seed domain. Do not round, cast to float, truncate or emit a bare decimal string as a purportedly unchanged v1.0.0 value.

**Required resolution before implementation:** formally amend/supersede the package wire schema with a versioned typed uint64 representation, e.g. `{"$type":"uint64","decimal":"<canonical unsigned decimal>"}`, or another exact encoding with equivalent type preservation. A schema-version change and crosswalk are required; this Gate does not unilaterally change Gate 164 v1.0.0. The original FrozenSnapshot bytes remain opaque base64 payloads and are not rewritten by this rule.

### 4.3 Required JCS vectors

The implementation regression suite must include, at minimum:

| Vector | Input | Expected canonical UTF-8 |
|---|---|---|
| Object ordering | `{"b":2,"a":1}` | `{"a":1,"b":2}` |
| Numeric normalization | `{"numbers":[333333333.33333329,1E+30,4.50,2e-3,0.000000000000000000000000001]}` | `{"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27]}` |
| Null preservation | `{"a":null,"b":[]}` | `{"a":null,"b":[]}` |
| String escaping | Include quote, reverse solidus and control characters | RFC 8785 exact escaping |
| Property sorting | Include non-ASCII property names | UTF-16 code-unit ordering required by RFC 8785 |

Also run all RFC 8785 Appendix B number vectors. Add adversarial rejection vectors for duplicate keys, invalid UTF-8, BOM, lone surrogates, NaN/Infinity, unsafe integer values and non-string keys. Project-specific tests must verify MatrixCapture tolerance sensitivity, report snapshot immutability and deterministic capture identity.

## 5. Deterministic capture identity

The capture identity is a content identity, not a timestamp, random UUID or GitHub execution identity.

### 5.1 Identity payload

Construct the following data-only payload before attaching either ID:

- `schema_id = TGCV-C10S-VCONT-BENCHMARK-CAPTURE-IDENTITY`
- `schema_version = 1.0.0`
- `design_identity`: exact declared design projection and declared fingerprints;
- `matrix_full_sha256`;
- `evaluation_seed_manifest_sha256`: digest of the exact ordered evaluation assignment projection under the approved wire schema;
- `outer_world_bundle_digests`: one digest per scenario/M in SCENARIO_IDS then numeric M order; each digest commits to the outer-world key, ordered RUN/R snapshot type IDs and snapshot SHA-256 values, and the repeated-assignment-report snapshot digest;
- `report_snapshot_sha256`;
- `evidence_index`: exact ordered scenario/outer ID/world ID triples.

The outer-world bundle digest is computed from this explicit JCS projection; do not hash a Python repr or an unregistered dataclass serialization.

### 5.2 Derivation

`capture_id = lowercase_hex(SHA256(JCS(identity_payload)))`.

`benchmark_export_id = capture_id`.

Neither ID appears in `identity_payload`; neither is included in the matrix or report snapshot digest. Companion artifacts refer to this ID but are excluded from its derivation. No wall-clock timestamp, random value, mutable path, caller-supplied PASS flag or externally retrieved GitHub metadata is included.

Identical content under identical schema versions yields the same ID. Any change to design identity, matrix, evaluation assignments, captured RUN/R evidence, repeated aggregate report, report snapshot or evidence index changes the ID.

## 6. CalibrationBankManifest v1.0.0

Schema ID: `TGCV-C10S-VCONT-CALIBRATION-BANK-MANIFEST`; version: `1.0.0`.

### 6.1 Envelope

Exact fields:

- `schema_id`, `schema_version`;
- `bank` = `calibration`;
- `namespace` (non-empty declared seed-derivation namespace);
- `seed_derivation`: algorithm `TGCV-C10S-VCONT-SEED-v3`, hash `SHA-256`, output rule `first_8_digest_bytes_unsigned_big_endian`;
- `design`: ordered scenario IDs/version map, sorted N grid, M, R and declared calibration purpose/targets;
- `row_count`;
- `rows`: exact materialized SeedAssignment projection;
- `seed_bank_fingerprint_legacy`;
- `manifest_sha256` under the versioned manifest JCS profile;
- `execution_evidence_status`: `NOT_CAPTURED`, `AVAILABLE`, `UNVERIFIABLE`.

### 6.2 Row schema and mapping

Each row contains exactly:

- `bank` = `calibration`;
- `scenario_id`;
- `scenario_version`;
- `n_units`;
- `replicate` (the actual SeedAssignment dataclass field; this is the RUN=-1 / R=0..R-1 index);
- `outer_replicate_id`;
- `assignment_role`;
- `world_seed`;
- `z_assignment_seed`;
- `g_assignment_seed`.

The runtime `assignment_index` property is an alias of `replicate`; it is not a second independent row field. A schema projection may expose a named `assignment_index` only if it records this exact source-field mapping and does not allow the two values to diverge. The uint64 wire representation issue in §4.2 applies to all three seed fields.

### 6.3 Cardinality, order and validation

Cardinality is derived from the calibration design itself:

`row_count = scenario_count × n_grid_count × M × (1 + R)`.

It MUST NOT be copied from the evaluation design unless the calibration design independently declares the same dimensions.

Canonical order:
1. authoritative scenario order;
2. ascending numeric N;
3. ascending numeric M, represented by `outer-000000` etc.;
4. RUN first (`replicate=-1`);
5. repeated assignments in ascending numeric R (`0…R-1`).

Required validation:
- exactly one RUN and exactly R contiguous repeated indices per scenario/version/N/M;
- one fixed world seed across RUN/R within each M;
- distinct world seeds across M within scenario/version/N;
- unique Z-assignment seeds and unique G-assignment seeds within each M group;
- world, Z and G seeds pairwise distinct within every assignment row;
- calibration/evaluation union seed sets are disjoint across all three streams;
- recompute the legacy seed-bank fingerprint from exact materialized rows under its unchanged historical algorithm;
- independently compute the new JCS manifest digest.

The namespace and derivation algorithm are envelope metadata because current SeedAssignment rows do not store them. Their provenance must be bound to the seed-generation source/execution record; rows alone cannot independently prove which namespace generated them.

Calibration assignment rows are not forced into evaluation RunManifest joins. If calibration execution records exist and are used to justify N/R sizing, they must be separately linked to those exact calibration assignment keys. Missing execution records are UNAVAILABLE/UNVERIFIABLE, never an empty successful join.

## 7. Gate159ReconciliationArtifact v1.0.0

Schema ID: `TGCV-C10S-VCONT-GATE159-RECONCILIATION`; version: `1.0.0`.

### 7.1 Envelope

Exact fields:

- `schema_id`, `schema_version`;
- `benchmark_export_id`;
- `design_identity`;
- `verifier_identity`: verifier name, version, source commit and implementation digest;
- `input_artifacts`: named artifact IDs and SHA-256 digests;
- `required_check_ids`: exact ordered required check list for this package profile;
- `checks`: exact ordered check records;
- `derived_status`;
- `findings_digest`.

### 7.2 Check-row schema

Each check record contains exactly:

- `check_id`;
- `check_version`;
- `scope`;
- `applicability` = `REQUIRED` or `CONDITIONAL`;
- `join_key_profile`;
- `expected_count` (nonnegative integer or null only when genuinely not defined);
- `observed_count` (nonnegative integer or null when input unavailable);
- `matched_count` (nonnegative integer or null when not computable);
- `mismatch_count` (nonnegative integer or null when not computable);
- `mismatches` (ordered bounded records with key, field, expected digest/value reference, observed digest/value reference and reason; never include secrets);
- `input_digests`;
- `status`;
- `reason`.

Allowed check statuses: `PASS`, `FAIL`, `UNAVAILABLE`, `UNVERIFIABLE`, `NOT_APPLICABLE`.

### 7.3 Required checks

The v1.0.0 required check catalogue is:

1. `EVALUATION_ASSIGNMENT_RUN_MANIFEST_ONE_TO_ONE`: evaluation SeedAssignment ↔ RunManifest exact one-to-one join on bank/scenario/version/N/M/role/index/run_id and all three seeds.
2. `CALIBRATION_EVALUATION_SEED_DISJOINTNESS`: recompute disjointness from actual calibration and evaluation rows, across world/Z/G seed unions.
3. `EVALUATION_SEED_FINGERPRINT_RECOMPUTATION`: recompute the unchanged legacy evaluation-bank fingerprint from exact materialized rows.
4. `CALIBRATION_SEED_FINGERPRINT_RECOMPUTATION`: recompute the unchanged legacy calibration-bank fingerprint from exact materialized rows.
5. `EFFECTIVE_CONFIGURATION_FINGERPRINT_RECOMPUTATION`: recompute from included effective configuration payloads, not from declared hash strings.
6. `MATRIX_LEGACY_AND_FULL_DIGEST_RECOMPUTATION`: independently recompute both the historical fingerprint and versioned full-matrix digest.
7. `SOURCE_EXECUTION_GITHUB_BINDING`: compare producer declarations with independently resolved repository/workflow/run/attempt/event/ref/commit/tree/artifact metadata.
8. `TECHNICAL_TEST_RUN_BINDING`: bind test workflow/run/attempt, tested commit, target, conclusion and artifact digest to the source execution identity.

Conditional check:
- `CALIBRATION_ASSIGNMENT_EXECUTION_LINK`: required when calibration run outputs or N/R sizing claims rely on executed calibration records; otherwise `NOT_APPLICABLE` only with a documented reason and a seed-manifest-only calibration scope.

A missing input does not produce zero mismatches. It produces null observed/matched/mismatch counts as appropriate and status UNAVAILABLE or UNVERIFIABLE.

### 7.4 Derived status

- `REJECTED`: any required check is FAIL.
- `NOT_RECONCILED`: no required check fails, but at least one required check is UNAVAILABLE or UNVERIFIABLE, or a required check is absent.
- `RECONCILED`: every required check is present and PASS; conditional checks are PASS or validly NOT_APPLICABLE with a documented reason.

The producer cannot set this status. The independent verifier derives it from the complete check set. Reconciled is not authenticated and does not imply scientific validity.

## 8. SourceExecutionEvidence and TechnicalTestEvidence

These remain independent companion artifacts, joined by `benchmark_export_id`.

### SourceExecutionEvidence

Minimum exact members:
- schema ID/version;
- benchmark_export_id;
- producer repository full name;
- workflow path and workflow ID;
- run ID and run attempt;
- event, source ref and full commit SHA;
- source tree digest;
- producer artifact ID and artifact digest;
- tested source archive digest;
- runtime identity and dependency-lock digest;
- producer-declared values and independently GitHub-resolved values in separate objects;
- resolution timestamp and resolver identity.

GitHub-resolved fields must be fetched independently. A producer-supplied commit, run ID or artifact digest is a claim, not proof.

### TechnicalTestEvidence

Minimum exact members:
- schema ID/version;
- benchmark_export_id;
- workflow path/ID, run ID and attempt;
- tested commit SHA;
- test target/suite and command identifier;
- conclusion;
- declared and observed test counts;
- artifact ID and SHA-256;
- source execution reference;
- resolver identity.

Serializer/verifier tests and scientific harness tests remain separate test classes. A technical test PASS is not a scientific execution or causal result.

## 9. Strict decoder contract

The current `FrozenSnapshot` tagged representation remains a legacy source format; its bytes are transported unchanged. The package verifier uses a separate strict decoder with:

- strict UTF-8 and no BOM;
- duplicate-key rejection during JSON parsing;
- rejection of NaN/Infinity and invalid Unicode;
- exact top-level schema/type/version;
- allowlisted dataclass and enum IDs;
- exact field-set equality (missing and extra fields both reject);
- exact field types before object construction;
- enum restoration to the registered enum class, not its underlying string;
- tuple/list/map distinction preserved;
- explicit null preserved separately from missing;
- bytes only through an explicit typed base64 envelope with decoded-length and digest checks;
- recursion, record-count, payload-size and nesting limits;
- no dynamic imports, arbitrary class construction or pickle.

The verifier must recompute the snapshot SHA over the exact transported bytes before parsing. It must not normalize, rewrite or reserialize legacy FrozenSnapshot bytes and then claim byte identity.

## 10. Required regression suite — not executed by this gate

The later implementation must add deterministic, non-scientific contract tests for:

**Matrix**
- canonical 52-row order accepted;
- any row permutation rejected;
- duplicate/missing/extra row rejected;
- each allowed enum-like value accepted and unknown value rejected;
- exact bool validation;
- explicit null vs missing distinction;
- tolerance_id-only change changes full digest;
- legacy fingerprint remains unchanged for the same historical input.

**Report**
- exact current top-level payload keys;
- report snapshot is immutable after compatibility dict mutation;
- legacy report fingerprint remains unchanged;
- JCS bytes and digest reproduce independently;
- unknown report field requires schema version change.

**Identity**
- same inputs produce same capture_id;
- changed matrix, assignment, bundle, report snapshot or evidence index changes capture_id;
- companions and timestamps do not change capture_id;
- neither capture_id nor benchmark_export_id is part of its own identity payload.

**Calibration / Gate 159**
- cardinality derived from calibration design;
- RUN/R ordering and contiguous indices;
- cross-M world-seed uniqueness;
- within-M world consistency and Z/G uniqueness;
- calibration/evaluation seed overlap rejected;
- missing calibration rows yield UNAVAILABLE, not PASS with zero mismatch;
- each required Gate159 check has denominator/count semantics;
- missing check and duplicate check IDs rejected;
- caller-supplied derived_status ignored/rejected.

**Decoder / JCS**
- all RFC 8785 Appendix B vectors;
- project-specific vectors in §4.3;
- duplicate-key, invalid UTF-8, BOM, NaN/Infinity, lone surrogate and unsafe integer rejection;
- enum type restoration;
- tuple/list/map/null/missing distinction;
- bytes envelope corruption and digest mismatch;
- uint64 exact round-trip under the amended typed wire schema.

No test in this list has been executed or is represented as PASS.

## 11. Gate 164 v1.0.0 compatibility blocker and required decision

Gate 164 v1.0.0 requires JCS for package JSON, includes uint64 seed values in evaluation/calibration manifests and temporal/report structures, and disallows string coercion. These requirements are not jointly sufficient to prove exact uint64 preservation under JCS.

Before any packager implementation, one explicit schema decision is required:
- retain Gate 164 v1.0.0 unchanged and demonstrate a fully exact compatible representation already allowed by its normative schema; or
- create a versioned successor (proposed v1.1.0) that defines typed uint64 encoding across every package file and updates the relevant schemas, vectors and verifier contract.

No silent field-type change is permitted. Gate 164 v1.0.0 remains DEFINED / IMPLEMENTATION BLOCKED. The confirmatory package cannot be declared conformant until this is resolved.

## 12. Governance and authorization boundary

The C10-S Draft 004 operational plan §2.1/§2.2 states that executable code generation/modification is blocked until the implementation contract is accepted and explicit authorization is given. This gate is documentary contract work only. It does not authorize source changes, tests, CI, seed generation, calibration, package generation, benchmark execution or scientific execution.

The canonical bootstrap remains design/recovery only; no experiment authorization is inferred. `main`, canonical RMA, Matrix, STATUS and scientific claim states are untouched. PR #116 base is not changed.

## 13. Gate 178 disposition

| Item | State |
|---|---|
| MatrixCapture row schema and allowed values | DEFINED |
| Matrix canonical order | DEFINED |
| Full-matrix JCS digest input | DEFINED |
| Legacy matrix fingerprint | PRESERVED |
| FrozenReportSnapshot projection | DEFINED |
| Legacy report fingerprint | PRESERVED / SEPARATE |
| JCS implementation candidate | SELECTED: rfc8785 0.1.4; dependency not installed/locked |
| Strict decoder contract | DEFINED |
| Deterministic capture identity | DEFINED |
| CalibrationBankManifest | DEFINED |
| Gate159ReconciliationArtifact | DEFINED |
| SourceExecutionEvidence / TechnicalTestEvidence | DEFINED |
| CapturedBenchmark compatibility | DEFINED |
| Gate 164 v1.0.0 uint64/JCS compatibility | BLOCKED — VERSIONED SCHEMA DECISION REQUIRED |
| Source implementation | NOT AUTHORIZED / NOT PERFORMED |
| Tests and CI | NOT AUTHORIZED / NOT EXECUTED |
| Calibration, seed generation, package, benchmark/scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `CONTRACT RECONCILED — CONDITIONAL`. The schemas are specified; implementation remains blocked by the Gate 164 uint64/JCS wire-format conflict and the explicit implementation authorization boundary.

## 14. Next operation

Gate 179 must resolve the Gate 164 wire-format compatibility through a versioned schema decision, then perform a final crosswalk against the exact 14-file inventory and the current Gate 174 verifier interface. Only after that can the implementation contract be submitted for acceptance and explicit implementation authorization. Do not start the serializer in Gate 179 by default.
