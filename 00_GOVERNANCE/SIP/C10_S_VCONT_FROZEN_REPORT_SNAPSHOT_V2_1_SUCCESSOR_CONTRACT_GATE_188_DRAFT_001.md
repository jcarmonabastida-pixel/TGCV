# C10-S V_cont — Gate 188: FrozenReportSnapshot v2.1.0 successor contract

**Status:** CONTRACT DECISION DEFINED — IMPLEMENTATION AND CONFORMANCE OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 187 nested report schema allowlists and cardinality  
**Scope:** versioned completion of the report uint64 registry; source-to-wire equality/reconciliation for the four nested scenario-report seed fields  
**Execution:** GitHub source/document inspection and contract authoring only. No source edits, imports, compilation, tests, CI dispatch, dependency installation, seed generation, producer invocation, package generation, calibration or scientific execution.

## 1. Decision

Retain the complete Evaluator report projection. Do not omit, null, redact, or relocate the nested RUN tuple to avoid the Gate 181 registry omission.

Introduce **FrozenReportSnapshot v2.1.0** as an explicit successor to v2.0.0. Add exactly four typed uint64 paths under `scenario_reports`, with source-specific equality and reconciliation rules in this contract.

This is a new schema version, not a retroactive amendment:
- Gate 181's source-to-wire contract and FrozenReportSnapshot v2.0.0 remain frozen as historical definitions.
- Gate 187 remains an immutable record of its source inspection and conditional disposition. Its interpretation of `TruthBundle.seed` as the world seed is corrected prospectively by this Gate: the current Generator source shows it is `ScenarioConfig.seed`, not the explicit `RunManifest.world_seed`.
- Gate 164 package v1.0.0 remains frozen and is not relabelled.
- The v2 package profile must explicitly reference FrozenReportSnapshot v2.1.0. Its 14-path archive inventory does not change. If an implementation changes any other v2 package-file schema or byte-level package contract beyond the declared report sub-schema reference, that change requires its own explicit package/envelope version increment; no silent compatibility claim is permitted.
- Gate 182 remains the implementation-boundary contract. This Gate authorizes specification of the successor schema only; it does not authorize producer, seed, calibration, package, or scientific execution.

The wire representation at each added path is exactly:

```json
{"$type":"uint64","decimal":"<canonical unsigned decimal>"}
```

The wrapper is permitted only at the four registered pointers below. It is not a generic integer escape.

## 2. Source-level finding: the four values are not four copies of one seed

The current source establishes two different source semantics.

### 2.1 TruthBundle.seed

In `vcont_integrated_harness.py`, `Generator.generate(cfg)` constructs:
- `world_seed` from `cfg.world_seed` when explicitly supplied, otherwise `cfg.seed`;
- the RunManifest's `world_seed` from that effective world seed;
- `TruthBundle.seed` from `cfg.seed` itself.

The Gate 171 producer applies `dataclasses.replace(config_template, world_seed=..., z_assignment_seed=..., g_assignment_seed=...)` for each SeedAssignment. It does not replace `config_template.seed`.

`RunEvidenceBundle.capture` independently checks `truth_bundle.seed == config.seed`, and `_matrix_truth_projection(truth)` copies `truth.seed` into the retained `MatrixTruthProjection.seed`.

Therefore:

**`TruthBundle.seed` MUST reconcile to the per-run `ScenarioConfig.seed` and retained `MatrixTruthProjection.seed`. It MUST NOT be equated to `SeedAssignment.world_seed` or `RunManifest.world_seed` merely because all fields are named “seed”.**

The confirmatory producer's explicit-stream rule remains unchanged: `ScenarioConfig.world_seed`, `z_assignment_seed`, and `g_assignment_seed` must be populated from the SeedAssignment. The legacy `ScenarioConfig.seed` is preserved as its own source field; it is not an alternative source for the three explicitly supplied streams.

The report wire projection treats `TruthBundle.seed` as a uint64 field and requires an exact source integer in `[0, 2^64-1]`. This is a serialization-domain requirement for the report field; it does not change Generator RNG selection or redefine its equality relation.

### 2.2 RunManifest seed streams

The other three fields in the nested RUN tuple are copied from the RUN's `RunManifest`:
- `world_seed`;
- `z_assignment_seed`;
- `g_assignment_seed`.

For the designated RUN, these values must equal the corresponding evaluation `SeedAssignment` values, the effective per-run `ScenarioConfig` stream fields, and the retained `RunManifest` snapshot fields. The world seed must also equal the `OuterWorldEvidenceBundle` key's world seed.

## 3. Exact v2.1.0 report schema delta

Schema ID remains `TGCV-C10S-VCONT-REPORT-SNAPSHOT`. Schema version and payload version become `2.1.0`. Canonicalization remains `RFC8785-JCS`. The existing v2.0.0 envelope field allowlist and all non-seed report fields remain unchanged.

Add exactly these JSON Pointer patterns, rooted at the `report` object inside the FrozenReportSnapshot envelope:

| JSON Pointer pattern | Source object / field | Reconciliation target |
|---|---|---|
| `/scenario_reports/*/per_outer_replicate/*/run/0/seed` | `TruthBundle.seed` | RUN `ScenarioConfig.seed` and `MatrixTruthProjection.seed` |
| `/scenario_reports/*/per_outer_replicate/*/run/3/world_seed` | `RunManifest.world_seed` | RUN `SeedAssignment.world_seed`, RUN `ScenarioConfig.world_seed`, RUN `RunManifest.world_seed`, outer-world key |
| `/scenario_reports/*/per_outer_replicate/*/run/3/z_assignment_seed` | `RunManifest.z_assignment_seed` | RUN `SeedAssignment.z_assignment_seed`, RUN `ScenarioConfig.z_assignment_seed`, RUN `RunManifest.z_assignment_seed` |
| `/scenario_reports/*/per_outer_replicate/*/run/3/g_assignment_seed` | `RunManifest.g_assignment_seed` | RUN `SeedAssignment.g_assignment_seed`, RUN `ScenarioConfig.g_assignment_seed`, RUN `RunManifest.g_assignment_seed` |

The `*` in the scenario position ranges over exactly the 13 registered scenario IDs. The `*` in the per-outer position ranges over exactly the M registered outer-replicate records in numeric M order. These are array/object traversal wildcards, not permission to accept unknown scenario keys or arbitrary path shapes. The `run` array remains exactly four ordered source objects: TruthBundle at index 0, AnalyzerResult at 1, AnalysisContract at 2, RunManifest at 3.

No other new pointer is admitted. Unknown nested fields, unexpected tuple length/order, unknown scenario IDs, missing rows, duplicate logical keys, and unconsumed or multiply consumed registered occurrences are hard failures.

### 3.1 Type and nullability

All four source fields are required, non-null, exact Python integers; booleans are rejected despite being integer subclasses. Each must satisfy:

`0 <= value <= 18446744073709551615`.

No float, decimal string, coercion, truncation, signed representation, or implicit default is permitted. The projected wrapper must contain exactly `$type` and `decimal`; `$type` is exactly `uint64`; `decimal` is the canonical base-10 unsigned representation with no sign, whitespace, leading zero (except the value `0`), exponent, or non-ASCII digit.

Each source occurrence is required exactly once per scenario/M RUN report. The repeated-assignment reports do not create extra instances of these four pointers: the nested `run` tuple is the designated RUN tuple returned by Evaluator.

## 4. Exact source reconciliation and joins

Reconciliation is performed on source-domain integers before accepting the typed wire projection. It is not enough that all four fields are valid uint64 values.

### 4.1 Primary logical key

For each `scenario_reports[scenario_id].per_outer_replicate[m]`, derive the RUN key:

`(bank="evaluation", scenario_id, scenario_version, n_units, outer_replicate_id, assignment_role="RUN", assignment_index=-1, run_id)`.

The report's `scenario_id` and `scenario_version` must match its scenario object and declared design. The per-outer record's `outer_replicate_id` must match the RUN `RunManifest.outer_replicate_id`. The RUN manifest must carry `assignment_role="RUN"` and `assignment_index=-1`. The `run_id` in TruthBundle, RunManifest, AnalyzerResult and the captured RUN record key must be identical. The scenario/M record must be unique.

The exact run-record key fields are those defined in Gate 174 §4: `scenario_id`, `scenario_version`, `N`, `outer_replicate_id`, `assignment_role`, `assignment_index`, and `run_id`. No positional or “nearest matching” join is allowed.

### 4.2 TruthBundle.seed reconciliation

For every scenario/M RUN:
1. `report.scenario_reports[scenario_id].per_outer_replicate[m].run[0].seed` equals `run[0].seed` in the source Evaluator tuple before projection.
2. It equals the decoded `seed` in the matching run record's `truth_projection` snapshot (`MatrixTruthProjection.seed`).
3. It equals the decoded `seed` in that same run record's `scenario_config` snapshot (`ScenarioConfig.seed`).
4. The decoded truth projection and ScenarioConfig identities must match the same RUN key and run_id.
5. The value is validated as uint64 independently at all three source occurrences before the report occurrence is wrapped.

There is deliberately **no equality assertion** between this value and `SeedAssignment.world_seed`, `ScenarioConfig.world_seed`, or `RunManifest.world_seed`. Those are separate fields with separate semantics. The verifier must not silently substitute one for another.

### 4.3 RunManifest stream reconciliation

For each RUN key:
1. The three source values at report `run[3]` equal the matching source `RunManifest` snapshot values.
2. They equal the matching evaluation `SeedAssignment` snapshot values.
3. They equal the three explicit stream fields in the matching `ScenarioConfig` snapshot.
4. `RunManifest.world_seed` equals the matching `OuterWorldEvidenceBundle` key.world_seed.
5. The same outer-world bundle contains exactly one designated RUN bundle for that scenario/version/N/M and the declared R repeated bundles; each bundle's assignment, config and manifest identities remain reconciled under Gate 170/174 contracts.
6. The evaluation assignment bank is exactly `evaluation`; calibration rows cannot satisfy an evaluation join.

The matching `run_records.json` run evidence record is resolved by the exact primary logical key in §4.1. Its snapshot refs `assignment`, `scenario_config`, `run_manifest` and `truth_projection` are decoded only under their registered FrozenSnapshot type/serialization identities. Their opaque bytes remain byte-preserved; the verifier does not rewrite them to add wrappers.

### 4.4 Existing duplicated views remain in force

All Gate 181 v2.0.0 reconciliation rules remain in force:
- root report temporal manifest ↔ nested `manifest.temporal_manifest`;
- root pair ledger ↔ nested `manifest.pair_ledger`;
- report temporal rows ↔ evaluation SeedAssignment and captured RunManifest;
- pair-ledger contribution world_seed ↔ unique scenario/M RUN world seed;
- outer-world key.world_seed ↔ corresponding RUN/R manifests and evaluation assignment.

The four new report occurrences add checks; they do not replace any prior checks or relax any existing path.

### 4.5 Fail-closed reconciliation

Reject the capture or package if any of the following occurs:
- a required source or duplicate is absent, null, wrong type, negative, greater than uint64 max, or boolean;
- a wrapper has missing, extra, duplicate, malformed or noncanonical members;
- a report scenario/M RUN cannot be joined one-to-one to a run evidence record, SeedAssignment, ScenarioConfig, RunManifest, truth projection or OuterWorldEvidenceBundle;
- any seed value differs from its corresponding source field;
- TruthBundle.seed is compared to world_seed as though they were aliases;
- any duplicate logical key, duplicated source occurrence, unknown pointer, unknown nested field, or unconsumed registered pointer is found;
- any report field is silently omitted, filled, sorted, normalized or coerced to make reconciliation pass;
- a source snapshot fails its type ID, schema, byte digest, or exact field validation.

## 5. Fingerprints, digests and non-circular identity

The historical report fingerprint algorithm and its input domain remain exactly as frozen in Gate 181:
1. construct the source-typed `manifest_payload`;
2. apply the historical `json.dumps(..., default=asdict, sort_keys=True)` round trip;
3. apply the frozen compact sorted-key JSON SHA-256 operation.

This calculation occurs before any v2.1.0 uint64 projection. It is not recalculated over wrapper dictionaries.

The v2.1.0 FrozenReportSnapshot digest is SHA-256 over RFC 8785 JCS bytes of the complete v2.1.0 envelope, including all four wrappers. It is not the historical report fingerprint.

The capture identity is then derived using the versioned capture identity contract and the v2.1.0 report snapshot digest. It must not include itself. The package manifest/package ID commits to its file digests under the package contract. The archive digest is calculated only after deterministic archive bytes exist.

These identities are distinct and must never be substituted for one another:
- historical `report_fingerprint`;
- FrozenReportSnapshot v2.1.0 JCS `sha256`;
- `capture_id` / `benchmark_export_id` (the declared alias under the v2 capture identity contract);
- package ID;
- archive SHA-256.

## 6. Compatibility matrix

| Artifact | Status under Gate 188 | Rule |
|---|---|---|
| Gate 164 package v1.0.0 | FROZEN | No reinterpretation, wrapper insertion or schema relabelling |
| FrozenReportSnapshot v2.0.0 | FROZEN HISTORICAL | Its original registry and bytes are not amended; it remains incomplete for the four newly discovered paths |
| FrozenReportSnapshot v2.1.0 | NEW SUCCESSOR CONTRACT | Adds exactly the four pointers and source reconciliation rules in this Gate |
| RUN-EXPORT-ENVELOPE v1.0.0 | FROZEN HISTORICAL | Gate 174 semantics remain unchanged |
| RUN-EXPORT-ENVELOPE v2.0.0 | EXISTING V2 CONTRACT | Must explicitly declare the report snapshot schema dependency as v2.1.0 when using this successor |
| Gate 164 package v2.0.0 profile | VERSIONED V2 SUCCESSOR | Retains the exact 14-file inventory; `report/report.json` is FrozenReportSnapshot v2.1.0. Any other changed package-file contract requires a further explicit version bump |
| MatrixCapture v1.0.0 | UNCHANGED | No schema change |
| CalibrationBankManifest v2.0.0 | UNCHANGED | No schema change |
| Gate159ReconciliationArtifact v1.0.0 | UNCHANGED | No schema change |

A v2.0.0 report reader MUST reject a v2.1.0 report as an unsupported schema version, and vice versa. The v2 package verifier must accept only the exact report sub-schema version declared by its package profile. No downgrade, permissive read, or inferred compatibility is allowed.

## 7. Required regression vectors

The pure capture/verification test suite must include all of the following. These are test requirements, not claims that tests have been written or run.

### 7.1 Positive uint64 boundary and round-trip vectors

For each of the four pointers, independently test:
- `0`;
- `9007199254740991` (`2^53-1`);
- `9007199254740992` (`2^53`);
- `18446744073709551615` (`2^64-1`).

Require exact wrapper output, exact decimal recovery, exact source integer recovery, byte-stable JCS output, and no float conversion.

### 7.2 Source-equality and join negatives

- TruthBundle.seed differs from ScenarioConfig.seed.
- TruthBundle.seed differs from MatrixTruthProjection.seed.
- RunManifest.world_seed differs from SeedAssignment.world_seed.
- RunManifest.z_assignment_seed differs from SeedAssignment.z_assignment_seed.
- RunManifest.g_assignment_seed differs from SeedAssignment.g_assignment_seed.
- ScenarioConfig explicit stream differs from the matching SeedAssignment.
- OuterWorldEvidenceBundle key.world_seed differs from RUN RunManifest.world_seed.
- run_id, scenario/version, N, M, role or assignment index differs at any join.
- Duplicate RUN, missing RUN, repeated-assignment record incorrectly used as RUN, or duplicate logical key.

The tests must also include a positive case in which `TruthBundle.seed != RunManifest.world_seed` but all source-specific equalities hold. This proves that the verifier does not conflate the legacy config seed with the world stream.

### 7.3 Structural, wrapper and parser negatives

- missing each of the four pointers, null, negative integer, boolean, float, and value greater than `2^64-1`;
- wrapper with missing/extra keys, wrong `$type`, non-string decimal, leading zeros, sign, whitespace, exponent, Unicode digits, or out-of-range decimal;
- duplicate JSON object keys in raw input;
- unknown scenario key, unknown nested field, wrong RUN tuple length/order, duplicate path traversal, unconsumed path, or duplicate logical join;
- tampering with each wrapped value after digest calculation;
- round-trip exactness, idempotent projection, and source snapshot immutability;
- identity non-circularity: attaching `capture_id` or `benchmark_export_id` after derivation must not change the identity payload/digest.

## 8. Implementation boundary and workflow safety

Implementation may change only the existing report capture/projection boundary in `vcont_evidence_export.py` and its pure fixture tests, plus the required package schema reference and documentation. Do not change Generator, Sealer, Analyzer, Evaluator, ScenarioConfig semantics, seed derivation, SeedAssignment generation, estimands, DGPs, calibration producers or scientific execution paths.

Before any implementation write:
1. re-read the exact current branch source and this contract;
2. confirm the pure workflow remains `workflow_dispatch` only and its explicit test list contains only pure capture fixtures;
3. confirm the integrated synthetic workflow is not triggered by pushes to these paths;
4. ensure no new workflow trigger, unittest discovery, producer invocation or package-generation command is introduced.

The workflow `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml` currently has a manual `workflow_dispatch` trigger and explicitly compiles/runs only `vcont_evidence_export.py` and `test_vcont_capture_v2.py`. This Gate did not dispatch it. No tests, imports, compilation or CI were run.

## 9. Gate disposition and next operation

**Gate 188: CONTRACT DECISION DEFINED — IMPLEMENTATION OPEN.**

The complete report is retained. The four report paths are explicitly typed in the new FrozenReportSnapshot v2.1.0 contract. The source semantics are distinguished: TruthBundle.seed reconciles to ScenarioConfig.seed / MatrixTruthProjection.seed; the three RunManifest stream seeds reconcile to SeedAssignment / ScenarioConfig / RunManifest and outer-world identity.

Still open:
- implementation of the v2.1.0 projection and strict decoder;
- update of the v2 package schema dependency reference;
- positive/negative regression authoring;
- source-level audit of implementation;
- execution of pure tests and CI, separately authorized;
- package writer, independent verifier, companion assembly and trusted authentication;
- all calibration and scientific execution.

No scientific estimand, DGP, Generator, Sealer, Analyzer, Evaluator behavior, causal claim, or execution authorization is changed by this contract.
