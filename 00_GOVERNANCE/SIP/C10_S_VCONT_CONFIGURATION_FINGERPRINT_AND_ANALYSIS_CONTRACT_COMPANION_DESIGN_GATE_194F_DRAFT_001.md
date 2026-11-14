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
