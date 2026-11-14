# C10-S V_cont — Gate 179: uint64 wire-format decision and package v2 crosswalk

**Status:** VERSIONED WIRE-FORMAT DECISION DEFINED — DRAFT BRANCH / IMPLEMENTATION BLOCKED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 178 capture/export serialization and companion schemas  
**Scope:** exact uint64 JCS representation, schema-version impact, 14-file crosswalk and verifier compatibility  
**Execution:** documentary/source inspection only; no code, tests, CI, package, seed generation, calibration, benchmark or scientific execution

## 1. Decision

Adopt a **versioned exact uint64 typed-object representation** for the confirmatory package successor:

- Existing `TGCV-C10S-VCONT-MC-PACKAGE v1.0.0` remains frozen and unchanged.
- The successor is `TGCV-C10S-VCONT-MC-PACKAGE v2.0.0`, not v1.1.0. The wire type changes from JSON number to typed object and is not backward-compatible; a major schema version is therefore required.
- All 14 package paths, the JCS canonicalization rule, the deterministic uncompressed POSIX tar profile and the non-circular package digest graph remain unchanged.
- The successor defines the uint64 wire type below and applies it to every direct seed occurrence in package JSON.
- No source seed derivation, source SeedAssignment field, seed value, historical fingerprint or scientific meaning changes.

This is a draft-branch contract decision. It does not modify main, declare implementation acceptance, or authorize implementation/execution.

## 2. Normative uint64 wire type

### 2.1 JSON representation

Every direct uint64 value in a v2.0.0 package JSON payload is represented as this exact object:

```json
{"$type":"uint64","decimal":"18446744073709551615"}
```

Exact constraints:
- object has exactly two members: `$type` and `decimal`;
- `$type` is exactly the string `uint64`;
- `decimal` is a JSON string matching `^(0|[1-9][0-9]*)$`;
- decoded integer range is inclusive `0…18446744073709551615`;
- no leading plus, leading zero (except zero itself), whitespace, exponent, sign, decimal point or Unicode digit substitution;
- the decoder returns the exact source-language unsigned integer value;
- a bare JSON number, bare decimal string, float, truncated value or differently tagged object is rejected for a uint64-typed field.

This is a typed representation, not an untyped numeric-to-string coercion. The field schema determines whether the tagged object is required. The tag is not inferred from arbitrary user data.

### 2.2 JCS treatment

The wrapper object is an ordinary RFC 8785-compatible JSON object containing a string. JCS canonicalizes its member ordering and string representation. The uint64 decimal is never parsed as an ECMAScript Number during canonicalization.

All non-seed integer fields remain JSON numbers subject to JCS/I-JSON safe-number constraints. If a non-seed integer exceeds the permitted exact JCS integer domain, validation rejects it until its own separately versioned semantic wire type is defined. The uint64 wrapper must not become a generic escape hatch for arbitrary large integers.

### 2.3 Source and legacy fingerprint boundary

Source `SeedAssignment` fields remain Python integers in the full uint64 domain. The wire adapter projects them into the typed object only at the package/JCS boundary.

Historical seed-bank fingerprints are recomputed from the original source-typed SeedAssignment rows under their existing frozen algorithm, before wire projection. They are not recomputed from decimal strings or wrapper dictionaries. New package/manifest digests are computed over the v2.0.0 typed wire representation.

Legacy `FrozenSnapshot` canonical bytes remain opaque, byte-for-byte payloads transported as base64 under the existing `TGCV-FROZEN-SNAPSHOT-1` serialization identifier. They are not rewritten as JCS and their embedded Python integer values are not converted. The strict decoder verifies their exact byte digest first and then decodes the allowlisted legacy snapshot format with Python's arbitrary-precision integer parser and uint64 range validation.

## 3. Exact field-level application

The uint64 wire profile applies to these direct fields:

| Gate 164 package path | Exact fields |
|---|---|
| `seeds/evaluation_seed_assignments.json` | `world_seed`, `z_assignment_seed`, `g_assignment_seed` on every SeedAssignment row |
| `seeds/calibration_seed_manifest.json` | `world_seed`, `z_assignment_seed`, `g_assignment_seed` on every calibration row |
| `runs/temporal_manifest.json` | `world_seed`, `z_assignment_seed`, `g_assignment_seed` on every RUN/R manifest row |
| `report/report.json` | The same three fields in every row of the embedded report `temporal_manifest` |
| `runs/run_records.json` | `outer_world_evidence_records[*].key.world_seed` |

No other Gate 164 v1.0.0 package field is a direct uint64 seed field under the current source/schema inspection.

Additional rules:
- `runs/run_records.json` snapshot `canonical_bytes_base64` values remain exact opaque bytes; do not rewrite seed integers inside those snapshots.
- Any future cleartext/direct seed field added to a v2.0.0 package payload MUST use the same typed uint64 object and be added to the field registry through a versioned schema update.
- `design/effective_scenario_configs.json` is the structural scenario configuration registry; assignment-specific seed values remain in the per-run opaque snapshots. If a future schema exposes such a seed directly, it must use the typed uint64 representation.
- `validation/reconciliation_results.json` must not disclose raw seed values in mismatch diagnostics; use the assignment key plus field name and digest/value references. If a future diagnostic schema includes a raw seed value, it must use the typed representation.
- No seed values are introduced into `manifest.json`, benchmark design, matrix, analysis contracts, configuration fingerprints or source-execution metadata.

## 4. Versioned schema crosswalk

| Artifact | Existing version | v2 successor | Reason |
|---|---:|---:|---|
| Package `TGCV-C10S-VCONT-MC-PACKAGE` | 1.0.0 | **2.0.0** | Direct uint64 JSON type changes |
| `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE` | 1.0.0 | **2.0.0** | Outer-world key contains typed world_seed |
| `TGCV-C10S-VCONT-REPORT-SNAPSHOT` | Gate 178 1.0.0 | **2.0.0** | Report temporal_manifest contains typed uint64 fields |
| `TGCV-C10S-VCONT-CALIBRATION-BANK-MANIFEST` | Gate 178 1.0.0 | **2.0.0** | Calibration assignment rows contain typed uint64 fields |
| `TGCV-C10S-VCONT-BENCHMARK-CAPTURE-IDENTITY` | Gate 178 1.0.0 | **2.0.0** | Evaluation assignment digest input uses v2 typed uint64 projection |
| `TGCV-C10S-VCONT-MATRIX-CAPTURE` | Gate 178 1.0.0 | **1.0.0 unchanged** | No uint64 fields; matrix digest unchanged |
| `TGCV-C10S-VCONT-GATE159-RECONCILIATION` | Gate 178 1.0.0 | **1.0.0 unchanged** | Carries artifact digests/references and derived check states, not raw seeds |
| `SourceExecutionEvidence` | Gate 178 v1.0.0 | **1.0.0 unchanged** | No seed values |
| `TechnicalTestEvidence` | Gate 178 v1.0.0 | **1.0.0 unchanged** | No seed values |

The package `manifest.json` declares package schema version 2.0.0 and the exact profile identifier `TGCV-C10S-VCONT-UINT64-TYPED-JCS-1`. The `runs/run_records.json` envelope declares schema version 2.0.0. FrozenReportSnapshot, CalibrationBankManifest and capture identity schema IDs retain their IDs but bump schema versions as shown.

Gate 164 v1.0.0 and all v1.0.0 subordinate schemas remain immutable historical formats. A v2 verifier MUST reject v1.0.0 when asked to validate a v2 confirmatory package. A v1 verifier MUST reject v2.0.0 as unsupported; no implicit coercion or auto-upgrade is allowed.

## 5. Package-level digest and identity consequences

- JCS canonical bytes for each affected JSON file are generated from the typed uint64 projection.
- Per-file SHA-256, manifest digest, deterministic package ID and final archive SHA-256 are recalculated under package schema v2.0.0.
- Package identity is not expected to match a v1.0.0 package, even when source data are identical.
- The legacy seed-bank fingerprints, SealedEvidence digest, legacy report fingerprint, legacy Matrix fingerprint and source FrozenSnapshot digests remain distinct and unchanged.
- Gate 178 capture identity is versioned to v2.0.0; its evaluation seed-manifest digest is calculated from the ordered typed uint64 projection. `capture_id` remains the SHA-256 of the canonical identity payload, and `benchmark_export_id = capture_id`. Neither ID is included in its own identity input.
- MatrixCapture full digest remains governed by Gate 178 v1.0.0 and does not change as a consequence of this decision.

## 6. Required v2 verifier behavior

A v2 verifier MUST:
1. Validate package schema ID/version and exact 14-path inventory before interpreting payloads.
2. Require the exact uint64 wrapper on every field enumerated in §3.
3. Reject bare JSON numbers or strings at those locations, wrong tags, extra/missing wrapper members, noncanonical decimal strings and out-of-range values.
4. Decode the decimal string using arbitrary-precision integer parsing, range-check it, and compare the resulting integer with source snapshot values after the snapshot's exact-byte digest has passed.
5. Recompute historical fingerprints from source-typed values using the frozen legacy algorithms, not from wire wrapper objects.
6. Recompute new JCS file and manifest digests from the typed v2 representation.
7. Reject unregistered direct seed fields or schema drift; never silently omit or auto-tag unknown fields.
8. Preserve RUN/R, M and scenario ordering exactly as Gate 164 requires.
9. Reject a v1.0.0 package when v2 confirmatory validation was requested, and reject a v2.0.0 package when the verifier only supports v1.0.0.
10. Keep integrity, schema conformance, completeness, reconciliation, execution provenance, technical test evidence and external authentication as distinct outputs.

## 7. Deterministic regression vectors — specified, not executed

The serializer/verifier suite must include:

| Case | Input / mutation | Expected |
|---|---|---|
| Zero | `{"$type":"uint64","decimal":"0"}` | Accept → integer 0 |
| Safe boundary | decimal `9007199254740991` | Accept exact |
| First unsafe JCS integer | decimal `9007199254740992` | Accept exact via typed object |
| uint64 maximum | decimal `18446744073709551615` | Accept exact |
| Overflow | decimal `18446744073709551616` | Reject |
| Leading zero | decimal `01` | Reject |
| Plus sign | decimal `+1` | Reject |
| Negative | decimal `-1` | Reject |
| Exponent | decimal `1e3` | Reject |
| Bare number | `9007199254740993` at a uint64 field | Reject |
| Bare string | `"9007199254740993"` at a uint64 field | Reject |
| Wrong tag | `{"$type":"int64","decimal":"1"}` | Reject |
| Extra member | wrapper includes `"value":1` | Reject |
| Missing member | wrapper lacks `decimal` | Reject |
| JCS determinism | reorder wrapper source members | Same canonical bytes |
| Source round trip | uint64 max source int → typed JCS → source int | Exact equality |
| Legacy fingerprint | compare source-int fingerprint before/after wire adapter | Identical |
| Snapshot opacity | same FrozenSnapshot bytes before/after package projection | Byte-identical |
| Package version | v1.0.0 payload under v2 verifier | Reject unsupported version |
| Package version | v2.0.0 payload under v1 verifier | Reject unsupported version |

These vectors are contract requirements only. No tests were run by Gate 179.

## 8. Exact 14-file inventory remains unchanged

The v2.0.0 archive MUST contain exactly the existing Gate 164 paths:

1. `manifest.json`
2. `report/report.json`
3. `design/benchmark_design.json`
4. `design/scenario_estimand_matrix.json`
5. `design/effective_scenario_configs.json`
6. `design/analysis_contracts.json`
7. `seeds/evaluation_seed_assignments.json`
8. `seeds/calibration_seed_manifest.json`
9. `runs/temporal_manifest.json`
10. `runs/run_records.json`
11. `provenance/source_execution.json`
12. `provenance/configuration_fingerprints.json`
13. `validation/reconciliation_results.json`
14. `validation/test_evidence.json`

No fifteenth file, detached file inside the archive, new directory payload, or optional path is introduced. Detached attestation/receipt remains outside the package subject as defined by Gate 164.

## 9. Impact on Gates 164, 174, 176 and 178

- **Gate 164:** v1.0.0 remains frozen; v2.0.0 is the successor target. The 14-file inventory, JCS and archive profiles remain; the uint64 typed wire profile is added.
- **Gate 174:** RUN-EXPORT-ENVELOPE advances to 2.0.0; strict decoder and independent verifier must implement the v2 field registry and reject cross-version coercion.
- **Gate 176:** MatrixCapture/report/companion capture timing and source boundaries remain. Report snapshot version advances to 2.0.0; no reconstruction after evaluation.
- **Gate 178:** MatrixCapture remains 1.0.0; FrozenReportSnapshot, CalibrationBankManifest and capture identity advance to 2.0.0. Gate159 reconciliation remains 1.0.0.
- **Harness source:** no source changes in this gate. The runtime SeedAssignment type and `_derive_seed()` remain unchanged.

The earlier Gate 178 suggestion of a v1.1.0 successor is superseded: because the wire-level JSON type is incompatible, v2.0.0 is the correct schema version.

## 10. Gate 179 disposition and authorization

| Item | State |
|---|---|
| Exact uint64 representation | DEFINED |
| JCS compatibility | DEFINED via typed object |
| Source seed algorithm/type | UNCHANGED |
| Legacy seed fingerprints | UNCHANGED |
| FrozenSnapshot bytes | OPAQUE / BYTE-PRESERVED |
| Gate 164 v1.0.0 | FROZEN / IMMUTABLE |
| Gate 164 v2.0.0 | DEFINED AS SUCCESSOR DRAFT |
| 14-file inventory | UNCHANGED |
| RUN-EXPORT-ENVELOPE | v2.0.0 defined |
| FrozenReportSnapshot | v2.0.0 defined |
| CalibrationBankManifest | v2.0.0 defined |
| Capture identity | v2.0.0 defined |
| MatrixCapture | v1.0.0 unchanged |
| Gate159 reconciliation | v1.0.0 unchanged |
| Source implementation | NOT PERFORMED |
| Tests / CI | NOT EXECUTED |
| Seed generation / calibration / package / benchmark / scientific execution | NOT AUTHORIZED / NOT EXECUTED |
| Main / canonical state / PR base | UNCHANGED |

**Overall:** `WIRE-FORMAT DECISION DEFINED — CONDITIONAL`. The uint64/JCS incompatibility is resolved at the schema-design level. Implementation remains blocked pending the governed implementation-contract acceptance and explicit implementation authorization, plus availability of actual calibration and independent Gate 159/source/test companions required for confirmatory acceptance.

## 11. Next operation

Gate 180 should perform a final v2.0.0 crosswalk against the exact Gate 164/174/178 payload projections and confirm every direct seed-bearing JSON location from the source schema. It must also reconcile the 14-file schema inventory with the existing capture API and Gate159 companion inputs. Only after that crosswalk is stable should the implementation contract be submitted for acceptance/authorization. No serializer implementation or test execution is implied.

## 12. Gate 180 source-schema correction — direct seed registry not yet complete

Gate 180's static inspection of the current evaluator identifies additional direct uint64 occurrences in `report/report.json` omitted from the initial Gate 179 §3 prose registry. Each 52-pair ledger contribution contains `world_seed`; the pair ledger is present both at report root and inside the legacy `manifest` payload. The v2 wire registry must therefore include:

- `pair_ledger[*].contributions[*].world_seed`;
- `manifest.pair_ledger[*].contributions[*].world_seed`;

in addition to the three seed fields in report.temporal_manifest and their duplicated `manifest.temporal_manifest` occurrences. Root and nested legacy-manifest copies must decode to the same source integer and be equality-checked before historical fingerprint recomputation.

Gate 180 also finds that source `ScenarioConfig` contains `seed`, `world_seed`, `z_assignment_seed` and `g_assignment_seed`, while Gate 164 requires an effective configuration file. The current package projection does not exist, so it is not yet proven whether these fields are excluded from `design/effective_scenario_configs.json` or serialized directly. Gate 179's assertion that no seed values occur in that path is therefore **UNVERIFIED** pending an exact EffectiveScenarioConfigProjection schema.

This addendum qualifies Gate 179's field-level completeness claim; it does not alter the uint64 wire primitive, package v2.0.0 version decision, source seed algorithm, legacy fingerprints or 14-file inventory. See Gate 180. No code/tests/CI or scientific execution occurred.

## 13. Gate 181 — completed direct-seed registry and source projection

Gate 181 supersedes the incomplete direct-seed field list in Gate 179 §3 with an exact JSON Pointer registry. In addition to evaluation/calibration rows, temporal manifests and outer-world keys, it includes both root and nested legacy-manifest report temporal rows and pair-ledger contribution `world_seed` fields. Duplicated report views must decode to exact equality before the historical report fingerprint is recomputed.

Gate 181 also resolves the effective-config question: direct `design/effective_scenario_configs.json` is a structural projection that excludes `seed`, world/Z/G assignment seeds and RUN/R identity fields, and includes a mandatory explicit-stream seed policy. Full per-run ScenarioConfig snapshots remain opaque byte-preserved records; their seed values are reconciled to SeedAssignment after supported decoding. Confirmatory capture MUST reject missing or mismatched explicit stream seeds, so the legacy fallback cannot be used.

The historical report fingerprint is recomputed over the original source-typed manifest_payload before uint64 wire projection. FrozenReportSnapshot v2.0.0 JCS digest remains separate. See Gate 181 for the full field registry, equality joins, 14-file crosswalk and companion assembly contract. The Gate 179 wire primitive and package v2.0.0 decision remain unchanged.

Gate 181 further defines the exact evaluation-assignment and temporal-manifest root envelopes and their `rows` arrays, resolving the pointer-root ambiguity. The calibration manifest retains the Gate 178 rows envelope. The legacy report fingerprint is explicitly identified as `TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1`; it is recomputed before uint64 projection and is not JCS.
