# C10-S V_cont — Gate 194-F: configuration fingerprint and AnalysisContract companion design

**Status:** ACCEPTED DESIGN DIRECTION — DETAILED WIRE CONTRACT PROPOSED; NOT YET FROZEN  
**Decision basis:** user acceptance of the Gate 194-E recommendation, 2026-11-14  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** design only; no implementation, tests, package generation or scientific execution.

## 1. Purpose and boundary

This document translates the accepted Gate 194-E design direction into a concrete, reviewable companion-file contract. It resolves the intended cardinalities, logical keys, digest domains, dependency order, joins and adversarial acceptance criteria before verifier implementation.

It does not modify Gate 164 v1.0.0, the Gate 179/181 v2.0.0 package contract, FrozenSnapshot serialization, source dataclasses, Generator, Sealer, Analyzer, Evaluator, DGPs, estimands, seed derivation or scientific interpretation. It does not establish confirmatory package status or scientific evidence.

The companion schemas below are proposed as version 1.0.0 under distinct schema IDs. They become frozen only after a separate explicit schema review/acceptance. Until then, all identifiers and exact property names in this document are design proposals, not claims about already implemented source behavior.

## 2. Recovered facts and compatibility constraints

The following are treated as existing source/contract constraints:

1. Gate 181 `EffectiveScenarioConfigProjection@2.0.0` is the authoritative structural DGP/Generator payload: one exact projection per scenario/version/N, including `scenario_id`, `scenario_version`, `n_units`, `generator_version`, `seed_policy` and its frozen 26 structural fields. Assignment seeds and RUN/R identity are excluded.
2. The source `AnalysisContract` dataclass has 37 fields. `contract_for(cfg)` constructs it from `ScenarioConfig`; it has no RUN/R identity fields.
3. The inspected Analyzer exposes `version = c10s-vcont-analyzer-0.1` and `analyze(evidence, contract)`; no separate typed Analyzer configuration object or configurable instance state was found.
4. Every RUN/R record carries a historical tagged FrozenSnapshot for its AnalysisContract. Its SHA-256 is computed over the exact historical snapshot bytes and remains a separate check.
5. MatrixCapture v1.0.0 carries the canonical 52-row matrix and its full JCS SHA-256. The legacy matrix fingerprint remains a separate compatibility value.
6. Evaluation SeedAssignment rows have an ordered evaluation-manifest digest. Calibration is a distinct bank with its own manifest and disjointness obligations.
7. The existing `MonteCarloBenchmarkDesign.configuration_fingerprint` is only syntax-checked as 64 hexadecimal characters; the source does not define its derivation algorithm.

These constraints must not be weakened or reinterpreted by the companion format.

## 3. Design decision translated into cardinalities

### 3.1 Analysis contracts

The companion `design/analysis_contracts.json` contains:

- exactly **13 source contract rows**, one per unique `(scenario_id, scenario_version, n_units)`;
- exactly **26 applicability rows**, two per source contract, one for each `run_family` value `RUN` and `REPEATED_ASSIGNMENT`;
- one shared source contract identity/digest referenced by both applicability rows;
- no duplication of the 37-field source payload inside applicability rows.

The source payload includes the exact 37 AnalysisContract fields and the Analyzer version. It is scenario-scoped, not run-scoped. RUN/R applicability is represented by a separate relation and must not be falsely encoded as a source property.

### 3.2 Configuration fingerprints

The companion `provenance/configuration_fingerprints.json` contains exactly:

- 13 DGP/Generator component records (one per scenario projection);
- 13 Analyzer/AnalysisContract component records (one per scenario contract);
- one MatrixCapture component record;
- one evaluation seed-bank component record;
- one aggregate design fingerprint declaration.

This is four component families plus one aggregate. Calibration is not a fifth component of the evaluation aggregate; it remains separately declared and independently checked under its calibration contract.

## 4. Proposed wire schema: analysis_contracts.json

Root schema ID: `TGCV-C10S-ANALYSIS-CONTRACTS`  
Schema version: `1.0.0`

Exact root members:

- `schema_id`: fixed schema ID above.
- `schema_version`: fixed string `1.0.0`.
- `benchmark_export_id`: exact Gate 181/182 export identity.
- `source_contracts`: array of 13 source rows.
- `applicability`: array of 26 applicability rows.

Each `source_contracts[]` row has exactly:

- `scenario_id`: non-empty string.
- `scenario_version`: non-empty string.
- `n_units`: positive integer.
- `analyzer_version`: non-empty string.
- `analysis_contract`: object containing exactly the 37 frozen AnalysisContract fields, with source types and nullability preserved.
- `contract_payload_digest`: lowercase 64-character SHA-256 hex.

The logical key is `(scenario_id, scenario_version, n_units)`. It must be unique. The row's `analysis_contract` object is not a FrozenSnapshot and is not itself the historical snapshot byte representation.

Each `applicability[]` row has exactly:

- `scenario_id`
- `scenario_version`
- `n_units`
- `run_family`: exactly `RUN` or `REPEATED_ASSIGNMENT`.
- `contract_payload_digest`: reference to exactly one source row.

The logical key is `(scenario_id, scenario_version, n_units, run_family)`. It must be unique and complete: every source row has exactly one applicability row for each run family, and no applicability row may refer to a missing source row.

Canonical array order:

1. source contracts ordered lexicographically by UTF-8 code-point order of `scenario_id`, then `scenario_version`, then numerically by `n_units`;
2. applicability ordered by the same three keys, then `RUN` before `REPEATED_ASSIGNMENT`.

No extra root or row properties are permitted. The verifier must validate exact field allowlists and source types; permissive object spreading or unknown-field acceptance is prohibited.

### 4.1 Contract payload digest

Algorithm ID: `TGCV-C10S-ANALYSIS-CONTRACT-PAYLOAD-JCS-SHA256-1`.

Digest input is the RFC 8785 JCS byte serialization of this exact object:

```json
{
  "schema_id": "TGCV-C10S-EFFECTIVE-ANALYSIS-CONTRACT",
  "schema_version": "1.0.0",
  "scenario_id": "<source scenario_id>",
  "scenario_version": "<source scenario_version>",
  "n_units": 0,
  "analyzer_version": "<source Analyzer.version>",
  "analysis_contract": { "<exact 37 source fields>": "..." }
}
```

The illustrative `n_units` value and ellipsis are explanatory only; actual values and the exact 37-field allowlist/types come from the source contract registry. The digest is SHA-256 of the JCS bytes, lowercase hex. No newline is appended.

This digest is the companion's scenario-level semantic contract identity. It is not the per-RUN/R historical FrozenSnapshot SHA-256. For every observed RUN/R snapshot, the verifier must independently:
1. validate and decode the historical snapshot using its frozen type/serialization registry;
2. recompute its historical SHA-256 from exact original bytes;
3. compare the decoded 37-field value exactly with the companion's source contract;
4. verify Analyzer version and scenario/version/N binding from authoritative source records;
5. match the snapshot to exactly one applicability row for its run family.

No conversion of historical FrozenSnapshot bytes to JCS is allowed.

## 5. Proposed wire schema: configuration_fingerprints.json

Root schema ID: `TGCV-C10S-CONFIGURATION-FINGERPRINTS`  
Schema version: `1.0.0`

Exact root members:

- `schema_id`
- `schema_version`
- `benchmark_export_id`
- `components`
- `aggregate`

Each component row has exactly:

- `component_id`: stable identifier.
- `component_type`: controlled vocabulary.
- `scope_key`: exact source scope key.
- `source_ref`: package-relative JSON Pointer or frozen source-record locator.
- `payload_schema_id`
- `payload_schema_version`
- `algorithm_id`
- `digest_sha256`

Controlled `component_type` values:

- `DGP_GENERATOR_CONFIG`
- `ANALYZER_EFFECTIVE_CONTRACT`
- `SCENARIO_ESTIMAND_MATRIX`
- `EVALUATION_SEED_BANK`

Component identity and scope:

- DGP/Generator: `component_id = dgp-generator:<scenario_id>:<scenario_version>:<n_units>`; scope key is the same triple.
- Analyzer/contract: `component_id = analyzer-contract:<scenario_id>:<scenario_version>:<n_units>`; scope key is the same triple.
- Matrix: `component_id = scenario-estimand-matrix`; scope key is `benchmark_export_id`.
- Evaluation seed bank: `component_id = evaluation-seed-bank`; scope key is `benchmark_export_id`.

The component array contains exactly 28 rows: 13 DGP/Generator, 13 Analyzer/contract, one matrix and one evaluation seed bank. Canonical order is component_type in the order listed above, then scope key in the same canonical scenario order; singleton components follow their family position. Duplicate component IDs or duplicate logical scopes are invalid.

### 5.1 Component digest algorithms

**DGP/Generator**  
Algorithm ID: `TGCV-C10S-EFFECTIVE-SCENARIO-CONFIG-JCS-SHA256-1`.  
Input: the exact Gate 181 `EffectiveScenarioConfigProjection@2.0.0` row, including all frozen fields, `generator_version` and `seed_policy`.  
Digest: SHA-256 of RFC 8785 JCS bytes, lowercase hex.

**Analyzer/AnalysisContract**  
Algorithm ID: `TGCV-C10S-EFFECTIVE-ANALYSIS-CONTRACT-JCS-SHA256-1`.  
Input: the exact versioned contract payload object defined in §4.1.  
Digest: SHA-256 of RFC 8785 JCS bytes, lowercase hex.  
This must equal the corresponding `contract_payload_digest` in `analysis_contracts.json`. The historical FrozenSnapshot digest remains a separate per-record integrity check.

**Matrix**  
Algorithm ID and digest: reuse the MatrixCapture v1.0.0 full-matrix JCS SHA-256 exactly. Source is the exact MatrixCapture payload from the same capture/export identity. The legacy matrix fingerprint is not substituted for this digest.

**Evaluation seed bank**  
Algorithm ID: the exact Gate 181 ordered evaluation assignment-manifest digest algorithm and identifier. Source is the complete evaluation SeedAssignment row sequence in its frozen canonical order. Recompute from actual rows. Do not use a design-declared digest as the source of truth. Calibration assignments are excluded from this evaluation digest and retain separate calibration manifest/disjointness checks.

### 5.2 Aggregate design fingerprint

Algorithm ID: `TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT-JCS-SHA256-1`.

The aggregate input is the RFC 8785 JCS serialization of this exact versioned object:

```json
{
  "schema_id": "TGCV-C10S-AGGREGATE-DESIGN-FINGERPRINT",
  "schema_version": "1.0.0",
  "components": [
    {
      "component_id": "...",
      "component_type": "...",
      "scope_key": "...",
      "payload_schema_id": "...",
      "payload_schema_version": "...",
      "algorithm_id": "...",
      "digest_sha256": "..."
    }
  ]
}
```

The array contains the 28 component rows, in the canonical order in §5. No source_ref, recomputation status, package file hash, package ID, capture ID, aggregate digest, calibration digest or attestation is included. This makes the dependency non-circular and binds the four required component families. The aggregate digest is SHA-256 of those JCS bytes, lowercase hex.

The `aggregate` object has exactly:

- `algorithm_id`
- `digest_sha256`
- `source_design_declaration`: fixed locator identifying the legacy `MonteCarloBenchmarkDesign.configuration_fingerprint` declaration being checked.

The verifier recomputes the aggregate and requires equality with both the companion declaration and the source design declaration. The source design declaration is not trusted merely because it is valid 64-character hex.

The aggregate binds matrix and evaluation seed-bank digests. Calibration remains outside this aggregate and is independently validated for actual manifest integrity and evaluation/calibration disjointness. Package ID, capture ID, package file digests and tar digest remain separate identities.

## 6. Cross-file and source reconciliation

The independent verifier must establish all of the following:

1. Every one of the 13 effective ScenarioConfig projections has exactly one DGP/Generator component and exactly one source AnalysisContract row.
2. Every source AnalysisContract row has exactly two applicability rows.
3. Every RUN and REPEATED_ASSIGNMENT snapshot maps to exactly one applicability row and exactly one source contract row.
4. Every RUN/R snapshot's historical bytes, type ID, serialization ID and historical SHA-256 are independently checked; decoded semantic fields equal the companion payload.
5. The Analyzer version in source records, source contract companion and Analyzer/contract fingerprint component agrees exactly.
6. Each of the 13 DGP/Generator digests is recomputed from its actual Gate 181 effective projection, not a report copy or a caller-supplied declaration.
7. The MatrixCapture digest is recomputed from the exact captured 52-row matrix; its legacy fingerprint is separately reconciled.
8. The evaluation seed-bank digest is recomputed from the exact ordered assignment rows; calibration is separately checked.
9. All 28 component declarations are consumed exactly once by the aggregate. No missing, duplicate, extra, reused or orphan component is accepted.
10. The aggregate recomputation equals the declared design fingerprint and the legacy design declaration.
11. Every source record and companion is bound to the same `benchmark_export_id`; no cross-export join is permitted.

The verifier must not accept a producer-provided `verified`, `recomputed`, `PASS` or equivalent field as evidence. Reconciliation status is derived by the independent verifier and reported in its own output.

## 7. Digest and identity separation

The following are distinct and must remain distinct:

- historical FrozenSnapshot SHA-256 over exact tagged source bytes;
- AnalysisContract semantic companion JCS SHA-256;
- effective ScenarioConfig JCS SHA-256;
- MatrixCapture full JCS SHA-256;
- ordered evaluation SeedAssignment manifest digest;
- aggregate design fingerprint;
- package JSON file hashes, package ID and tar SHA-256;
- capture/export identity;
- calibration manifest digest and disjointness evidence;
- external source provenance and attestation.

Equality between two values from different domains is not evidence that the domains are interchangeable. No digest is recomputed after a lossy projection. No package-layer digest substitutes for a semantic source digest.

## 8. Adversarial acceptance matrix (tests to write; NOT to execute)

The implementation must include positive fixtures and adversarial tests for at least:

- 12 or 14 source contract rows instead of exactly 13;
- 25 or 27 applicability rows instead of exactly 26;
- missing RUN or REPEATED_ASSIGNMENT mapping for a scenario;
- duplicate source key or duplicate applicability key;
- applicability row referencing a nonexistent contract digest;
- contract digest correct as package-file bytes but wrong for semantic JCS payload;
- one changed AnalysisContract field with stale digest;
- one changed Analyzer version with stale digest;
- a RUN snapshot associated with another scenario or repeated-assignment family;
- a repeated assignment mapped to RUN;
- historical FrozenSnapshot SHA mismatch despite matching decoded fields;
- correct historical digest but semantically different decoded contract;
- unknown or missing AnalysisContract field;
- extra root/row property;
- component record missing, duplicated, extra or consumed twice;
- DGP/Generator component digest insensitive to a changed structural field;
- DGP/Generator digest changing when only excluded assignment seeds change;
- MatrixCapture digest mismatch while legacy matrix fingerprint remains unchanged;
- evaluation seed row order changed while a stale ordered-manifest digest is retained;
- calibration row accidentally included in evaluation aggregate;
- aggregate component order changed;
- aggregate declaration syntactically valid but not derived from the 28 component records;
- cross-export companion/source references;
- package file digest valid while semantic component digest is wrong;
- producer-supplied PASS field attempting to override failed recomputation.

Positive fixtures must demonstrate the full 13/26/28 cardinality, correct exact-once joins, seed-stream separation and digest recomputation. These tests are design requirements only; no tests are run under the current execution boundary.

## 9. Verifier output dimensions

Do not collapse these into a single package PASS:

- companion schema validity;
- AnalysisContract source/applicability cardinality;
- FrozenSnapshot byte integrity and typed decoding;
- RUN/R identity and exact-once reconciliation;
- effective ScenarioConfig fingerprint recomputation;
- AnalysisContract semantic fingerprint recomputation;
- MatrixCapture recomputation;
- evaluation seed-bank recomputation;
- aggregate design fingerprint recomputation;
- calibration integrity/disjointness;
- package file/archive integrity;
- Gate 159 reconciliation;
- GitHub source/workflow provenance;
- technical test evidence;
- external attestation/authentication.

A structural pass does not imply Gate 164 confirmatory acceptance, scientific execution, causal identification or evidence for `ΔT_acc → ΔV`.

## 10. Open implementation prerequisites

Before code is written, a static source review must pin, by exact source path and symbol:

1. the full 37-field AnalysisContract registry, types and nullability;
2. the full Gate 181 26-field EffectiveScenarioConfigProjection registry and canonical ordering;
3. the exact MatrixCapture v1.0.0 serialization and digest function;
4. the exact ordered evaluation seed-manifest algorithm and row source;
5. the exact source locator/JSON Pointer for `MonteCarloBenchmarkDesign.configuration_fingerprint`;
6. the existing RFC 8785 implementation and version already required by Gate 164/181;
7. the actual 13 scenario identities from the frozen design, without hardcoding invented identifiers.

If any item conflicts with this proposal, stop and record the discrepancy; do not silently adapt the schema or alter a frozen historical contract.

## 11. Current disposition

- Gate 194-E source audit: recorded.
- Gate 194-F design direction: ACCEPTED by user.
- Exact schemas and algorithms in this document: PROPOSED, pending static source crosswalk and explicit freeze.
- Package writer/verifier implementation: NOT AUTHORIZED by this document.
- Tests: NOT WRITTEN / NOT EXECUTED.
- CI/workflows/compilation: NOT EXECUTED.
- Calibration, seed-bank generation, package generation and scientific execution: NOT AUTHORIZED / NOT EXECUTED.
- `main`: unchanged.
- PR #116: remains Draft; this document belongs only to `research/c10-s-consolidation-draft`.

**Next operation:** perform the static source crosswalk in §10 and compare every proposed schema/digest input with the exact source APIs and frozen Gate 181/179 definitions. Only after that reconciliation should the schemas be frozen and implementation considered.


## 11. Gate 194-F.1 amendment — source crosswalk corrections

**Status:** DESIGN AMENDMENT — PROPOSED, NOT FROZEN  
**Authority:** Gate 194-G source crosswalk, 2026-11-14  
**Precedence:** This section supersedes any inconsistent wording in §§2–10. It does not rewrite historical Gate 194-G findings or imply implementation.

### 11.1 Authoritative scenario order

The 13 scenario identifiers and their canonical order are:

1. `R0_FOCAL_POSITIVE`
2. `R0_FOCAL_NULL`
3. `R0_FOCAL_ADVERSE`
4. `R0_DIRECT_G`
5. `R0_DIRECT_Z`
6. `R1_ALTERNATIVE_BASELINE`
7. `R2_ALTERNATIVE_AFFECTED`
8. `R3_PROVISION_FAILURE`
9. `R0_MEASUREMENT_ADVERSE`
10. `R0_INTERFERENCE`
11. `R0_SUPPORT_FAILURE`
12. `R0_HETEROGENEITY`
13. `R2_SUPPORT_FAILURE_ZG_INTERACTION`

All scenario-indexed companion arrays MUST follow this registry order, then the declared scenario version and numeric N. Do not substitute lexical ordering.

### 11.2 Exact EffectiveScenarioConfig structural field registry

The 26 structural fields, in the Gate 181 projection order, are:

```text
profile
mechanism
n_intervals
window_start
last_transition_support
follow_up
enabled_probability
baseline_conformity
focal_access_effect
package_direct_effect
focal_direct_effect
collateral_effect
provision_probability
alternative_probability
heterogeneity
interference_effect
measurement_sensitivity
measurement_specificity
missing_probability
randomized_z
randomized_g
positivity
no_interference
measurement_identified
version_consistency
zg_interaction_effect
```

The effective row additionally carries `scenario_id`, `scenario_version`, `n_units`, `generator_version` and the exact `seed_policy` as defined by Gate 181. The eight excluded source fields remain excluded from this structural projection: `seed`, `world_seed`, `z_assignment_seed`, `g_assignment_seed`, `replicate_id`, `outer_replicate_id`, `assignment_role`, `assignment_index`. They remain represented and reconciled in their authoritative assignment/manifest/snapshot records.

The DGP/Generator fingerprint input MUST be the exact Gate 181 effective structural projection row, not a reconstructed subset and not the full mutable ScenarioConfig object.

### 11.3 Exact AnalysisContract field and type registry

The source payload has exactly these 37 fields:

```text
estimand_id
estimand_version
randomized_z
randomized_g
positivity
no_interference
measurement_identified
version_consistency
focal_direct_path_absent
common_nonfocal_regime
target_regime_id
target_regime_version
outcome_id
outcome_version
z_effect_invariant_across_g
transportability_id
transportability_version
transportability_scope
transportability_evidence_status
g_assignment_mechanism_hash
z_assignment_mechanism_hash
g_assignment_mechanism_id
g_assignment_mechanism_version
z_assignment_mechanism_id
z_assignment_mechanism_version
reference_regime_id
reference_regime_version
transportability_outcome_id
transportability_basis
run_conditional_estimand_id
run_conditional_estimand_version
mechanism_marginal_estimand_id
mechanism_marginal_estimand_version
reference_regime_estimand_id
reference_regime_estimand_version
g_assignment_estimand_id
g_assignment_estimand_version
```

Type partition, matching the source annotations:

- Boolean: `randomized_z`, `randomized_g`, `positivity`, `no_interference`, `measurement_identified`, `version_consistency`, `focal_direct_path_absent`, `common_nonfocal_regime`, `z_effect_invariant_across_g`.
- Nullable string: `transportability_id`, `transportability_version`, `transportability_scope`, `transportability_outcome_id`, `transportability_basis`.
- Non-null string: the remaining 23 fields.

No coercion is permitted between booleans, strings, nulls or numeric values. The companion row MUST contain exactly these 37 properties in its `analysis_contract` object. The semantic digest input is a separate envelope:

```json
{
  "schema_id": "TGCV-C10S-EFFECTIVE-ANALYSIS-CONTRACT",
  "schema_version": "1.0.0",
  "scenario_id": "<exact scenario id>",
  "scenario_version": "<exact scenario version>",
  "n_units": 0,
  "analyzer_version": "c10s-vcont-analyzer-0.1",
  "analysis_contract": {
    "<all 37 exact source properties>": "<source-typed values>"
  }
}
```

The example is schematic; actual values MUST be taken from the source `contract_for(cfg)` projection and authoritative design identity. Digest: lowercase SHA-256 of RFC 8785 JCS UTF-8 bytes, no trailing newline. Algorithm ID: `TGCV-C10S-ANALYSIS-CONTRACT-PAYLOAD-JCS-SHA256-1`. This is a newly introduced semantic digest, not an existing source digest.

The historical RUN/R FrozenSnapshot digest remains a distinct integrity check over the exact retained historical snapshot bytes. The verifier MUST decode the snapshot, validate the exact 37-field typed payload, project its semantic contract, and compare that projection with the companion source row. It MUST NOT compare unlike digest domains or replace the historical snapshot digest with the new JCS digest.

### 11.4 MatrixCapture digest correction

The Matrix component MUST reuse the source-supported MatrixCapture full digest. Its exact digest input is the four-member object:

```json
{
  "schema_id": "<MatrixCapture schema id>",
  "schema_version": "<MatrixCapture schema version>",
  "row_count": 52,
  "rows": ["<the exact 52 canonical rows>"]
}
```

Algorithm ID: `TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1`. The SHA-256 is computed over RFC 8785 JCS UTF-8 bytes, lowercase hex, with no appended newline.

The digest input explicitly EXCLUDES `design_identity`, `legacy_matrix_fingerprint`, `full_matrix_digest_algorithm` and `full_matrix_sha256`. The legacy fingerprint remains a separate compatibility field. Hashing the complete MatrixCapture envelope is prohibited because it defines a different and circular digest domain.

### 11.5 Evaluation assignment component digest

The evaluation assignment component MUST reuse the exact source-supported ordered assignment wire projection:

```text
bank
scenario_id
scenario_version
n_units
replicate
outer_replicate_id
assignment_role
world_seed
z_assignment_seed
g_assignment_seed
```

The three seed values MUST retain the Gate 179 typed uint64 wire representation. Rows are ordered by the canonical 13-scenario registry, then numeric outer-world replicate, with RUN first and repeated assignments in their authoritative assignment-index order.

Digest input: `{"rows": ordered_assignment_wire_rows}`. Algorithm ID: `TGCV-C10S-EVALUATION-ASSIGNMENT-MANIFEST-JCS-SHA256-1`. Digest: lowercase SHA-256 of RFC 8785 JCS UTF-8 bytes, no trailing newline.

This value is a recomputable evaluation assignment-manifest component. It MUST NOT be represented as a recomputation of the historical `MonteCarloBenchmarkDesign.seed_bank_fingerprint`; that legacy field remains a separately preserved declaration unless and until its own source algorithm is defined and audited. Calibration assignments are excluded from this evaluation component and remain independently manifested and checked for disjointness.

### 11.6 Exact 28-component aggregate manifest

The aggregate contains exactly 28 component records:

- 13 `DGP_GENERATOR_EFFECTIVE_CONFIG` records, one for each canonical scenario row;
- 13 `ANALYZER_EFFECTIVE_CONTRACT` records, one for each canonical scenario contract;
- one `MATRIX_CAPTURE` record;
- one `EVALUATION_ASSIGNMENT_MANIFEST` record.

Each component record has exactly:

- `component_type`: one of the four values above;
- `component_key`: the scenario key `(scenario_id, scenario_version, n_units)` for scenario-indexed components; the fixed string `GLOBAL` for the two global components;
- `algorithm_id`: exact algorithm identifier;
- `schema_id`: exact input schema identifier;
- `schema_version`: exact input schema version;
- `sha256`: lowercase 64-character digest independently recomputed from the authoritative input.

Canonical ordering is the four component families in the order listed above; within each scenario family, use the authoritative 13-scenario registry order. The global MatrixCapture record precedes the global evaluation assignment record.

The aggregate input is the exact versioned object:

```json
{
  "schema_id": "TGCV-C10S-CONFIGURATION-FINGERPRINT-MANIFEST",
  "schema_version": "1.0.0",
  "algorithm_id": "TGCV-C10S-CONFIGURATION-FINGERPRINT-AGGREGATE-JCS-SHA256-1",
  "component_count": 28,
  "components": ["<the exact ordered 28 component records>"]
}
```

The aggregate digest is lowercase SHA-256 over RFC 8785 JCS UTF-8 bytes of this object, with no trailing newline. The aggregate object MUST NOT include its own digest, the legacy `configuration_fingerprint` declaration, package file hashes, package ID, archive digest, capture ID, report snapshot digest or calibration-bank digest. This prevents circularity and keeps package integrity, capture identity and calibration provenance as separate dimensions.

The recomputed aggregate is compared with the declared `MonteCarloBenchmarkDesign.configuration_fingerprint`. A mismatch is a semantic provenance failure even if the declaration is syntactically valid hexadecimal. The legacy declaration is not an input to its own recomputation.

### 11.7 Exact-once reconciliation obligations

The independent verifier MUST establish all of the following, not merely compare row counts:

1. Every one of the 13 source contract rows maps to exactly one authoritative scenario/version/N configuration.
2. Every source contract row is referenced by exactly two applicability rows: one `RUN`, one `REPEATED_ASSIGNMENT`.
3. Every observed RUN/R AnalysisContract snapshot maps to exactly one applicability row and the corresponding source contract row.
4. No applicability row, source contract row, observed RUN/R snapshot or scenario identity is duplicated, omitted, orphaned or cross-linked.
5. All 13 DGP/Generator and 13 Analyzer/contract components are consumed exactly once by the aggregate; MatrixCapture and evaluation assignment components are each consumed exactly once.
6. Each component digest is recomputed from its own authoritative input before aggregate recomputation.
7. Calibration assignments are not silently included in evaluation rows or aggregate components; calibration manifest and disjointness are checked independently.
8. The legacy `seed_bank_fingerprint` and `configuration_fingerprint` declarations are preserved and compared only against the explicitly defined corresponding semantics; syntax-only validity is never treated as provenance.

### 11.8 Gate 194-F.1 disposition

This amendment corrects the source-field registries, authoritative ordering and digest domains identified by Gate 194-G. It resolves the design ambiguities at the documentary level but does not establish that the schemas are implemented or that the verifier consumes them.

**Disposition: CONDITIONAL — AMENDED DESIGN, NOT FROZEN.**

Before schema freeze, perform one read-only consistency review across this amendment, Gate 181's exact projection, the source field/type registry, the package writer's 14-path inventory and the independent verifier's existing decoder/reconciliation boundaries. Record any residual mismatch explicitly. No implementation, tests, compilation, CI, package generation, calibration or scientific execution is authorized by this amendment.


### 11.9 DGP/Generator component algorithm and remaining schema-identity gate

The DGP/Generator component algorithm is newly introduced under this amendment:

- Algorithm ID: `TGCV-C10S-EFFECTIVE-SCENARIO-CONFIG-JCS-SHA256-1`.
- Input: the complete, exact Gate 181 `EffectiveScenarioConfigProjection@2.0.0` row, including `scenario_id`, `scenario_version`, `n_units`, `generator_version`, `seed_policy` and all 26 structural fields in their frozen types.
- Digest: lowercase SHA-256 over RFC 8785 JCS UTF-8 bytes, with no trailing newline.
- Exclusions: no assignment seed, RUN/R identity, replicate identity, capture ID, report, MatrixCapture, package metadata or derived fingerprint may be added to this component input.

The component record's `schema_id` and `schema_version` MUST be copied literally from the authoritative Gate 181 projection contract; the implementation MUST NOT invent aliases or infer them from the display label `EffectiveScenarioConfigProjection@2.0.0`.

**Residual schema-identity blocker:** Gate 194-G establishes the projection version and exact fields but its crosswalk does not transcribe the literal schema ID/version values for every input family (Gate 181 effective-config projection, AnalysisContract semantic envelope, MatrixCapture and ordered evaluation assignment manifest). Those literals must be recovered from the governing source contracts/constants and entered into a closed registry before schema freeze. This is a documentary/source-reconciliation task, not permission to create replacement IDs.

Accordingly, the Gate 194-F.1 amendment is internally specified at the field and digest-domain level, but the companion schemas remain **NOT FROZEN** until the literal schema-identity registry is verified. The final consistency review must fail closed on any missing or conflicting schema ID/version, rather than accepting a guessed value.
