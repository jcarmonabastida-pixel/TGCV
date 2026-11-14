# C10-S V_cont — Gate 194-G: static source crosswalk for Gate 194-F

**Status:** STATIC SOURCE AUDIT — CONDITIONAL; CONTRACT FREEZE BLOCKED BY SPECIFICATION CORRECTIONS  
**Branch:** `research/c10-s-consolidation-draft`  
**Audited design:** Gate 194-F, commit `195bc0d1d59f3c8daa45597ace844039f5a60fed`  
**Audit basis:** GitHub source/document inspection only. No imports, compilation, tests, CI, producers, seed generation, calibration, package generation or scientific execution.

## 1. Purpose and audit rule

This gate compares the accepted Gate 194-F design against the actual C10-S source and frozen Gate 164/178/179/181 contracts. It distinguishes:

- **MATCH** — exact source or frozen contract support exists;
- **MISMATCH** — Gate 194-F wording or a proposed algorithm conflicts with the source/frozen contract;
- **NOT_VERIFIABLE** — the source/contract does not define the required fact or schema.

A proposed new algorithm may be a valid design decision, but it must not be reported as an already existing source algorithm. No implementation-readiness or package PASS is inferred from this audit.

## 2. Reconstructed source inventory

The following source files were inspected on `research/c10-s-consolidation-draft`:

| Artifact | Git blob SHA | Inspected scope |
|---|---|---|
| `vcont_integrated_harness.py` | `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002` | ScenarioConfig, AnalysisContract, Analyzer, contract_for |
| `vcont_benchmark_protocol.py` | `8511f289224a885bdc69b2b494f4e6dd345fa8b8` | SeedAssignment, build_seed_bank, MonteCarloBenchmarkDesign, SCENARIO_IDS |
| `vcont_evidence_export.py` | `7d383100508f3e8284f36b3bcb1bad862b0ebb8c` | JCS helpers, MatrixCapture, FrozenReportSnapshot, assignment wire projection, capture identity |
| `vcont_package_v2.py` | `5c2c86a7f577afcc13a0b7bae17d5a2ef8597bf1` | 14-file inventory, pure writer, companion pass-through, matrix digest check |
| `vcont_package_v2_verify.py` | `73e05aa1da7c3f9609f1590b4d78c06c1ec080e8` | independent snapshot decoder, effective-config reconciliation, matrix digest, current companion checks |

Frozen documentary sources inspected: Gates 164, 178, 179 and 181. Gate 181 remains the normative source for the effective structural ScenarioConfig projection and the report/capture serialization boundaries.

## 3. Crosswalk results

### 3.1 Scenario universe and effective ScenarioConfig projection

**Result: MATCH for the frozen 13-scenario / 26-field projection; NOT_VERIFIABLE for a new semantic fingerprint until its algorithm is frozen.**

The authoritative `SCENARIO_IDS` registry contains exactly these 13 identifiers, in this order:

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

The benchmark-design validator requires exactly one declared version for each of those 13 scenarios. The current source design has one `n_units` value. The independent verifier requires exactly 13 effective-config rows and checks their authoritative scenario/version/N order. Thus the 13-row scenario projection is supported for the current design; the verifier does not yet recompute a semantic config fingerprint.

Gate 181 freezes exactly 26 structural ScenarioConfig fields. The source `ScenarioConfig` contains those fields plus the key fields and excluded seed/run-identity fields. The 26-field allowlist in the verifier matches Gate 181 exactly:

`profile, mechanism, n_intervals, window_start, last_transition_support, follow_up, enabled_probability, baseline_conformity, focal_access_effect, package_direct_effect, focal_direct_effect, collateral_effect, provision_probability, alternative_probability, heterogeneity, interference_effect, measurement_sensitivity, measurement_specificity, missing_probability, randomized_z, randomized_g, positivity, no_interference, measurement_identified, version_consistency, zg_interaction_effect`.

Gate 181's three-part row key is `(scenario_id, scenario_version, n_units)`; `generator_version` and the exact `seed_policy` are also required at row level. The source field `ScenarioConfig.version` maps to the projection's `scenario_version`. The 8 excluded source fields remain excluded from structural JSON: `seed`, the three explicit stream seeds, `replicate_id`, `outer_replicate_id`, `assignment_role`, `assignment_index`. Their full source values remain in the opaque per-run snapshots and/or assignment/manifest records.

**Gate 194-F correction needed:** the 26-field structural allowlist must be reproduced verbatim in the normative design appendix or referenced as an exact Gate 181 allowlist. The F document currently refers to the 26 fields but does not enumerate them; an implementation must not infer the missing field `zg_interaction_effect` from memory or from a partial list.

### 3.2 AnalysisContract source projection

**Result: MATCH for 37-field source shape and role-independent factory; MATCH for the accepted Analyzer.version + AnalysisContract design interpretation; NOT_VERIFIABLE for companion schema/cardinality as a frozen historical wire contract.**

The source `AnalysisContract` dataclass has exactly 37 fields. The verifier's closed FrozenSnapshot registry independently lists the same 37 field names. The field set is:

```text
estimand_id, estimand_version,
randomized_z, randomized_g, positivity, no_interference,
measurement_identified, version_consistency,
focal_direct_path_absent, common_nonfocal_regime,
target_regime_id, target_regime_version, outcome_id, outcome_version,
z_effect_invariant_across_g,
transportability_id, transportability_version, transportability_scope,
transportability_evidence_status,
g_assignment_mechanism_hash, z_assignment_mechanism_hash,
g_assignment_mechanism_id, g_assignment_mechanism_version,
z_assignment_mechanism_id, z_assignment_mechanism_version,
reference_regime_id, reference_regime_version,
transportability_outcome_id, transportability_basis,
run_conditional_estimand_id, run_conditional_estimand_version,
mechanism_marginal_estimand_id, mechanism_marginal_estimand_version,
reference_regime_estimand_id, reference_regime_estimand_version,
g_assignment_estimand_id, g_assignment_estimand_version
```

Source annotations distinguish booleans, non-null strings and nullable strings. In particular, the transportability ID/version/scope/outcome/basis fields are nullable; the remaining fields have non-null source types. The source type partition is: **9 booleans** (`randomized_z`, `randomized_g`, `positivity`, `no_interference`, `measurement_identified`, `version_consistency`, `focal_direct_path_absent`, `common_nonfocal_regime`, `z_effect_invariant_across_g`), **non-null strings** for all identity/version/hash/status/mechanism/basis fields other than the nullable set, and **5 nullable strings** (`transportability_id`, `transportability_version`, `transportability_scope`, `transportability_outcome_id`, `transportability_basis`). The source annotations are authoritative; the exact field names and types are captured in the decoder registry. Note: the boolean list comprises nine fields, not ten.

`contract_for(cfg)` constructs the contract from `ScenarioConfig`. It does not accept a SeedAssignment, RunManifest, RUN/R role, assignment index or run ID. The resulting AnalysisContract is therefore scenario/config-scoped, not run-scoped. The Analyzer class exposes only `version = "c10s-vcont-analyzer-0.1"` and `analyze(evidence, contract)`; no separate Analyzer configuration object or mutable configuration state was found. The accepted Gate 194-F interpretation of Analyzer.version plus AnalysisContract as the current effective Analyzer configuration is source-compatible.

The source does not currently serialize `design/analysis_contracts.json` from a frozen typed schema. The package writer accepts that companion as caller-materialized mapping data; the verifier's current implementation does not validate its source-contract rows, applicability rows or semantic digest. Existing per-RUN/R AnalysisContract FrozenSnapshots and their historical SHA-256 are independently checked, but this is not a substitute for the separate companion.

The 13 source rows / 26 applicability rows are consistent with one role-independent contract per scenario and Gate 164's per-scenario/run-family requirement. However, their exact root schema, row allowlists, digest domain and exact-once mapping are new design choices, not a pre-existing frozen schema.

### 3.3 MatrixCapture digest

**Result: MATCH for MatrixCapture existence, canonical order, row schema and digest function; MISMATCH in Gate 194-F if “MatrixCapture full JCS SHA-256” is read as hashing the complete MatrixCapture payload.**

The source `capture_matrix()`:
- requires exactly 52 rows in authoritative positional order;
- checks the scenario/version identities;
- computes the legacy matrix fingerprint separately;
- constructs the exact digest input object:
  `{schema_id, schema_version, row_count: 52, rows}`;
- computes SHA-256 over RFC 8785 JCS bytes of that object;
- then constructs the larger MatrixCapture payload, which additionally contains `design_identity`, `legacy_matrix_fingerprint`, `full_matrix_digest_algorithm` and `full_matrix_sha256`.

The verifier recomputes the same digest input object. Therefore the matrix component digest must reuse the existing `full_matrix_sha256` and the exact algorithm `TGCV-C10S-VCONT-MATRIX-FULL-JCS-SHA256-1`. It must not hash the entire serialized MatrixCapture payload, which would be a different digest domain and would include the digest field itself.

**Required Gate 194-F wording correction:** specify the exact digest input as `{schema_id, schema_version, row_count, rows}`; explicitly exclude `design_identity`, the legacy fingerprint, the algorithm label and the digest field from that digest input. The legacy matrix fingerprint remains a separate compatibility value.

### 3.4 Evaluation SeedAssignment manifest digest

**Result: MATCH for the ordered row projection and derivation expression in capture identity; NOT_VERIFIABLE for a separately named frozen “seed-bank fingerprint” algorithm.**

The source `_assignment_wire(row)` projects exactly:
`bank, scenario_id, scenario_version, n_units, replicate, outer_replicate_id, assignment_role, world_seed, z_assignment_seed, g_assignment_seed`.
The three seeds use the Gate 179 typed uint64 wire object. The capture-identity builder orders outer bundles by authoritative scenario order and numeric M, and appends each world's RUN row followed by its ordered repeated-assignment rows. It computes:

`SHA256(JCS({"rows": [assignment_wire rows in that order]}))`.

This is a source-supported ordered evaluation assignment-manifest digest and is already a capture-identity component. The source does not expose a separately named constant/function for a configuration-fingerprint component algorithm, nor does it prove that this digest is identical to the historical `MonteCarloBenchmarkDesign.seed_bank_fingerprint` declaration. That field is only validated as a 64-character hexadecimal string; it is not recomputed by `validate_monte_carlo_benchmark_design`.

**Required Gate 194-F clarification:** either reuse the exact capture-identity assignment digest as the evaluation seed-bank component, with a newly frozen explicit algorithm ID and the exact input above, or define a separately versioned seed-bank digest. Do not call the design's legacy `seed_bank_fingerprint` independently recomputed unless a source algorithm for that value is added and audited. Calibration rows remain excluded and separately reconciled.

### 3.5 Analyzer version and AnalysisContract digest

**Result: MATCH for source facts; NOT_VERIFIABLE for the proposed semantic JCS algorithm until its exact schema and type registry are frozen.**

The Analyzer version string is a class attribute. The 37-field AnalysisContract object can be projected without run identity. RFC 8785 support is imported in the evidence-export source as `rfc8785.dumps`; source helper `_jcs_bytes` returns the resulting bytes and `_sha256_hex` computes lowercase SHA-256.

No existing source function currently hashes the proposed versioned AnalysisContract payload. The Gate 194-F algorithm is therefore a valid proposed new digest domain, not a recovered historical algorithm. Its exact input must specify the complete 37-field allowlist, source types/nullability, scenario key and Analyzer version, and must remain separate from each snapshot's exact-byte FrozenSnapshot SHA-256.

### 3.6 Aggregate design fingerprint

**Result: NOT_VERIFIABLE in current source; accepted as a new design algorithm, not an existing implementation.**

`MonteCarloBenchmarkDesign.configuration_fingerprint` is only checked for 64 hexadecimal characters in `validate_monte_carlo_benchmark_design`. It is copied into the design/report projection and package payload. No source function defines its payload, component order, domain separation or derivation. The current verifier does not recompute it from configuration components.

The Gate 194-F aggregate JCS/SHA-256 algorithm is thus a new algorithm and may be introduced as such. It must be explicitly versioned, non-circular and recomputed from the 28 component records. The existing source declaration becomes the value to be compared against the recomputation; its previous syntax validation is not proof of provenance.

### 3.7 Companion writer/verifier boundary

**Result: MATCH for the existence of the 14-file package inventory and caller-materialized companion boundary; NOT_VERIFIABLE for Gate 194-F companion schemas as current source behavior.**

The writer's `VContPackageCompanionsV2` accepts mappings for the companion files. It checks some envelope-level properties (including evaluation/calibration assignment and temporal rows) and computes package-file digests; it does not derive or validate the semantic schema proposed for `analysis_contracts.json` or `configuration_fingerprints.json`.

The independent verifier has exact schema/semantic handling for FrozenSnapshot, RUN/R joins, effective ScenarioConfig and MatrixCapture. Its current top-level flow does not parse or recompute `design/analysis_contracts.json` or `provenance/configuration_fingerprints.json`; their paths are present in the 14-file inventory but not consumed by a semantic verifier routine. The verifier explicitly returns bounded/partial dimensions and does not authenticate external provenance.

This is the actual unresolved gap Gate 194-F is intended to close. No writer/verifier implementation for the two proposed companions is present in the inspected source.

## 4. Consolidated result matrix

| Gate 194-F requirement | Result | Reason |
|---|---|---|
| Exactly 13 authoritative scenarios | MATCH | Source registry and design validator |
| 13 effective-config rows, current single N | MATCH | Gate 181 and current verifier |
| Exact 26 structural ScenarioConfig fields | MATCH | Gate 181 and verifier allowlist; F should enumerate all 26 |
| 8 excluded seed/RUN-R fields | MATCH | Gate 181, source ScenarioConfig, verifier reconciliation |
| 37-field AnalysisContract source shape | MATCH | Dataclass and independent decoder registry |
| Analyzer.version + AnalysisContract current config interpretation | MATCH | Analyzer has version and no separate config object |
| 13 contract source / 26 applicability mapping | NOT_VERIFIABLE as frozen schema | Source-compatible new design; exact companion schema absent |
| MatrixCapture digest algorithm | MATCH with F wording correction | Digest hashes the four-member digest-input object, not entire MatrixCapture payload |
| Ordered evaluation assignment digest input | MATCH | Exact source projection/order and JCS/SHA-256 expression exist |
| Separate named evaluation seed-bank component algorithm | NOT_VERIFIABLE | No separate source algorithm ID; legacy design fingerprint is syntax-only |
| Analyzer/contract semantic JCS digest | NOT_VERIFIABLE as existing algorithm | Proposed new digest domain; source fields are available |
| Aggregate configuration fingerprint | NOT_VERIFIABLE in source | Declaration is only hex-validated |
| Companion exact root/row schemas | NOT_VERIFIABLE | Writer accepts mappings; verifier does not consume these two schemas |
| Exact-once 28-component aggregate consumption | NOT_VERIFIABLE in current implementation | New verifier obligation |
| Calibration outside evaluation aggregate | MATCH as separation principle | Gate 181 and separate calibration manifest/disjointness |
| RFC 8785 implementation use | MATCH | `rfc8785.dumps` is used in the source; `requirements-vcont-v2.lock` pins `rfc8785==0.1.4` with the exact Gate 178 wheel SHA-256 `520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48` (lock blob `3b49087a242d14e3bc30f8d56e00b4f8d213a51c`) |
| External authentication | NOT_VERIFIABLE / NOT_AUTHENTICATED | Explicitly absent from current verifier |

## 5. Required amendments to Gate 194-F before schema freeze

1. Add the exact 26-field EffectiveScenarioConfig structural allowlist from Gate 181, including `zg_interaction_effect`.
2. Correct the MatrixCapture digest description to the exact digest input `{schema_id, schema_version, row_count, rows}`; do not hash the full MatrixCapture payload.
3. Give the evaluation assignment component a distinct explicit algorithm ID and define its exact source-supported digest input as `SHA256(JCS({"rows": ordered _assignment_wire rows}))`. Explicitly state that this is not the legacy `seed_bank_fingerprint` unless a separate algorithm is defined.
4. Include the exact 37 AnalysisContract field names, types and nullability in the schema registry or a versioned registry reference; preserve all source defaults and explicit nulls.
5. Name the new AnalysisContract semantic JCS digest and aggregate design fingerprint as newly introduced algorithms, not historical source algorithms.
6. Freeze exact root/row schemas, canonical ordering, source references, benchmark_export_id joins and exact-once consumption for both companion files.
7. Retain the verified RFC 8785 dependency pin: `rfc8785==0.1.4`, wheel SHA-256 `520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48`, in `requirements-vcont-v2.lock`. No installation or execution is required.

No source contract should be changed merely to fit the proposed companion schema. If any proposed field mapping cannot be grounded, retain NOT_VERIFIABLE and stop before implementation.

## 6. Implementation boundary

The following remain prohibited under the current authorization state:
- edits to Generator, Sealer, Analyzer, Evaluator, DGPs, estimands or seed generation;
- changes to FrozenSnapshot historical serialization;
- package writer/verifier implementation;
- test execution, compilation, CI/workflows or imports;
- seed-bank generation, calibration, package generation or scientific execution.

The audit is documentary and static. It does not authorize scientific execution.

## 7. Disposition and next operation

**Gate 194-G disposition: CONDITIONAL — source facts are sufficiently reconstructed to correct the design, but Gate 194-F is not yet freeze-ready.**

The 13/26/28 architecture remains viable. The source crosswalk confirms the 13-scenario universe, exact 26 structural config fields, 37 AnalysisContract fields, role-independent contract factory, Analyzer version, MatrixCapture digest primitive and ordered assignment digest input. It also confirms that the two companion semantic verifiers and aggregate fingerprint derivation do not yet exist.

**Next operation:** issue a Gate 194-F.1 amendment implementing the seven corrections in §5, then conduct a final read-only schema consistency review. Only after that review should the companion schemas be frozen and implementation authorization considered.

**No tests, compilation, CI, producers, seed generation, calibration, package generation or scientific execution were performed.**
