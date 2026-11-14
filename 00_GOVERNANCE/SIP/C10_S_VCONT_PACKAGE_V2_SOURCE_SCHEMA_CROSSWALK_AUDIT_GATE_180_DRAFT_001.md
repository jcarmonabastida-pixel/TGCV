# C10-S V_cont — Gate 180: package v2 source-schema crosswalk audit

**Status:** CONDITIONAL — SOURCE/SCHEMA CROSSWALK INCOMPLETE; IMPLEMENTATION NOT READY  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 179 uint64 wire-format decision  
**Scope:** static inspection of the current V_cont producer, evaluator report, snapshot types, test definitions and Gate 164/174/176/178/179 package contracts  
**Execution:** GitHub source/document inspection only; no imports, compilation, tests, CI, seed generation, calibration, package generation, benchmark or scientific execution

## 1. Executive disposition

Gate 180 does **not** certify the Gate 179 v2.0.0 crosswalk as complete or implementation-ready. The exact uint64 tagged-object representation is a viable JCS-compatible wire primitive, but the current source-to-package projection is not yet fully enumerated and the current capture API does not retain two artifacts required by Gate 178.

Four material findings determine the disposition:

1. **Gate 179's direct-seed field registry is incomplete.** The evaluator's 52-pair ledger stores `world_seed` in every M contribution. The same ledger is included both at report root and inside the report's legacy `manifest` payload. Gate 179 currently names the three seed fields in report.temporal_manifest but does not explicitly include these pair-ledger contribution occurrences in its field registry. All direct occurrences must use the uint64 wrapper.
2. **The effective-config projection is not resolved.** Source `ScenarioConfig` has `seed`, `world_seed`, `z_assignment_seed` and `g_assignment_seed`. Gate 164 requires effective configurations, while Gate 179 says no seed values are introduced in `design/effective_scenario_configs.json`. No package projection implementation exists to prove which fields are included or excluded. This must be an explicit schema decision, not an assumption.
3. **The current producer does not retain MatrixCapture or FrozenReportSnapshot.** `produce_and_capture_benchmark()` validates and passes `specs` to Evaluator but returns `CapturedBenchmark(report, outer_world_bundles, evidence_index)`; the matrix tuple is discarded and the report remains a mutable dict. There are no `matrix_capture` or `report_snapshot` fields.
4. **The current capture API does not receive independent companions.** It accepts evaluation assignments and structural config templates. It does not accept a calibration manifest, Gate 159 reconciliation, independently resolved source-execution evidence or technical-test evidence. Those artifacts must remain separately sourced and joined by the export/verification boundary; they cannot be synthesized from the evaluation capture.

Consequently, Gate 179 is a useful wire-format decision but its claim that the field-level crosswalk is fully exact is premature. Gate 180 records the necessary corrections and preserves all existing source APIs. No scientific estimand, DGP, N/R/M semantics or Generator/Sealer/Analyzer/Evaluator behavior is changed.

## 2. Inspected canonical source and artifacts

The following current branch files were fetched directly from GitHub:

| Artifact | Inspected content SHA |
|---|---|
| `vcont_evidence_export.py` | `b309742b0f8999106da9215eed6afc1cf8d13780` |
| `vcont_benchmark_protocol.py` | `8511f289224a885bdc69b2b494f4e6dd345fa8b8` |
| `vcont_integrated_harness.py` | `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002` |
| `test_vcont_integrated_harness.py` | `1933f9b17cedce919adb3d60ac138d18320ef35e` |
| `Gate 164 package contract` | inspected from research branch |
| `Gate 174 verifier contract` | inspected from research branch |
| `Gate 176 capture/companions contract` | inspected from research branch |
| `Gate 178 serialization contract` | `08a3456b0bdfdfc8543f18a1b1dfe56cc5a95c16` |
| `Gate 179 uint64 v2 decision` | inspected from research branch |
| `harness README` | `d0f7a3da2c7e96ac9714c373dc1a7baa26e615fd` |

Canonical bootstrap was also read from `main`: governance README, CHATGPT_BOOTSTRAP, CANONICAL_STATE, STATUS, current Matrix pointer and artifact, current RMA pointer, traceability, governance operating principles, historical reconstruction rule, technical execution workflow, scientific asset registry and validator source files. The main pointers declare RMA v3.38, Matrix v1.47 and RMA traceability v3.38. The local validators were not executable through this GitHub inspection pass; no validator PASS is claimed.

## 3. Finding F180-01 — missing direct uint64 occurrence in report pair ledger

In `vcont_integrated_harness.py`, each contribution assembled for the 52-pair ledger includes:
- `outer_replicate_id`;
- `world_id`;
- `world_seed`;
- `run_id`;
- temporal/status/estimate/truth/error fields.

The contribution is appended to `pair_ledger`. The evaluator then places `pair_ledger` both in the report root and in `manifest_payload`; the final report returns both `pair_ledger` and `manifest`.

Therefore the Gate 164 `report/report.json` has at least these direct uint64 paths:
- `temporal_manifest[*].world_seed`;
- `temporal_manifest[*].z_assignment_seed`;
- `temporal_manifest[*].g_assignment_seed`;
- `pair_ledger[*].contributions[*].world_seed`;
- `manifest.temporal_manifest[*].world_seed`;
- `manifest.temporal_manifest[*].z_assignment_seed`;
- `manifest.temporal_manifest[*].g_assignment_seed`;
- `manifest.pair_ledger[*].contributions[*].world_seed`.

The last four are duplicates of the legacy manifest payload's own copies, but they remain direct JSON seed occurrences and must be encoded and verified. A report projector must preserve equality between duplicated views after typed projection. The verifier must check that the root and nested legacy-manifest copies agree exactly before recomputing the legacy report fingerprint from source-typed values.

Gate 179 §3 is incomplete until these locations are explicitly added. No other field may be assumed to be seed-free solely because it is nested.

## 4. Finding F180-02 — effective ScenarioConfig seed-field classification unresolved

The source `ScenarioConfig` dataclass has:
- required `seed: int`;
- optional `world_seed: int | None`;
- optional `z_assignment_seed: int | None`;
- optional `g_assignment_seed: int | None`.

The per-run `RunEvidenceBundle` captures the full ScenarioConfig as an opaque FrozenSnapshot. The benchmark producer starts from structural templates and uses `dataclasses.replace` to insert the three assignment stream seeds. The base `seed` remains on the config. Generator uses explicit stream seeds when present, while `seed` remains part of the config identity/run identity and is a fallback for stream derivation when explicit seeds are absent.

Gate 164's `design/effective_scenario_configs.json` is required to retain effective DGP/Generator configurations and all parameters affecting generated worlds. Gate 179 states that no seeds are introduced in this path, but the source contract does not currently define a separate structural-config projection or an explicit exclusion list for these four source fields.

**Required resolution:** define a versioned `EffectiveScenarioConfigProjection` with exact fields and explicit seed semantics. It must decide whether:
- the structural config file excludes all four seed fields and records that assignment-specific seed identity is bound exclusively through the seed assignment manifest and run snapshots; or
- any seed fields are retained directly, in which case each retained uint64 field uses the Gate 179 typed object and is added to the exact field registry.

The choice must preserve the declared configuration fingerprint semantics and must not remove a source parameter merely to simplify packaging. Until that projection is specified, Gate 179's five-path direct-seed registry is not complete.

## 5. Finding F180-03 — MatrixCapture and FrozenReportSnapshot are not in CapturedBenchmark

Current source declaration:

```python
@dataclass(frozen=True)
class CapturedBenchmark:
    report: dict[str, Any]
    outer_world_bundles: tuple[OuterWorldEvidenceBundle, ...]
    evidence_index: tuple[tuple[str, str, str], ...]
```

The current `produce_and_capture_benchmark()`:
1. obtains `specs` from the optional matrix argument or builds the matrix;
2. validates it;
3. passes the same tuple to `evaluate_monte_carlo_benchmark(..., matrix=specs)`;
4. checks report coverage, temporal manifest and pair-ledger joins;
5. returns only `CapturedBenchmark(report, tuple(bundles), tuple(evidence_index))`.

It does not retain `specs` as MatrixCapture and does not capture the report as FrozenReportSnapshot. The current report remains mutable. This is a direct source-level gap against Gate 178 §3.3, which requires producer-created captures to populate both artifacts.

Required implementation shape (contract only; not implemented here):
- preserve the existing three fields and positional constructor compatibility;
- add trailing optional `matrix_capture` and `report_snapshot` fields for legacy construction;
- producer-created captures MUST populate both;
- capture the exact validated `specs` sequence before or at evaluator invocation, without sorting or reconstructing it later;
- capture the report snapshot immediately after Evaluator returns and before returning the CapturedBenchmark;
- confirmatory export fails closed if either field is absent;
- later mutation of `report` must not mutate or refresh `report_snapshot`.

The API currently has no such fields or capture path. Gate 180 therefore audits the contract as not yet implemented; no code changes are made.

## 6. Finding F180-04 — companion artifacts are separate inputs, not producer outputs

The current producer accepts:
- a `MonteCarloBenchmarkDesign`;
- pre-materialized evaluation-bank `SeedAssignment` rows;
- structural `ScenarioConfig` templates;
- tolerance;
- optional matrix.

It does not accept or return:
- the actual calibration-bank manifest;
- Gate159 reconciliation artifact;
- independently resolved GitHub source/workflow/artifact execution evidence;
- technical workflow/test evidence.

This is consistent with Gate 176's intended separation only if the package/export boundary receives these artifacts from their authoritative sources and binds them to the same capture identity. It is not acceptable to infer calibration disjointness from evaluation rows, to infer Gate159 PASS from producer validation, or to treat test definitions as executed test evidence.

The implementation contract must define a separate companion assembly boundary, exact references/digests, applicability, and fail-closed behavior. For confirmatory v2 packaging, absent required companions remain blocking. The capture producer itself must remain free of external authentication claims.

## 7. Finding F180-05 — current snapshot codec is not the strict v2 verifier

Current `FrozenSnapshot.capture()` accepts registered dataclass source objects and serializes the tagged representation with Python `json.dumps(sort_keys=True,...)`; this is the legacy snapshot format, not RFC 8785 JCS. It accepts integer values without a uint64 field registry. Current `_decode()`:
- decodes enum wrappers to their underlying value rather than restoring enum identity;
- uses standard `json.loads` without duplicate-key rejection;
- accepts ordinary mappings not matching a known wrapper;
- does not apply an exact per-type field allowlist/version schema before constructing nested dataclasses.

This does not invalidate the Gate 179 rule that existing FrozenSnapshot bytes remain opaque and byte-preserved. It does mean the current `FrozenSnapshot.restore()` must not be represented as the strict independent v2 package verifier. The v2 verifier must separately validate package JSON/JCS, exact wrapper locations, exact snapshot envelope/type allowlists and byte digests before any allowlisted legacy snapshot decode. Enum-valued fields in registered snapshots need either explicit stable-string restoration under a versioned codec or an explicit rejection rule; silent enum erasure is not acceptable for typed identity.

## 8. Finding F180-06 — test coverage exists for the old capture API, not the new package properties

The current `test_vcont_integrated_harness.py` includes source-level test definitions for:
- FrozenSnapshot capture/restore;
- MatrixTruthProjection retention;
- RUN/R producer behavior;
- benchmark-wide capture;
- malformed/incomplete assignment banks and mixed-bank rejection.

The current test file does not define the Gate 178/179 package properties:
- MatrixCapture exact 52-row retention and canonical order;
- report snapshot immutability/JCS bytes;
- typed uint64 projection at every direct path, including duplicated pair-ledger paths;
- strict duplicate-key/unknown-field/enum decoding;
- structural ScenarioConfig seed projection decision;
- calibration/Gate159/source/test companion binding;
- 14-file package writer and independent v2 verifier;
- v1/v2 cross-version rejection.

No tests were executed in Gate 180. The test definitions already present are not promoted to PASS evidence.

## 9. Corrected v2 direct-seed registry requirement

Before package implementation, create a machine-checkable, versioned registry of every direct uint64 field path, derived from the actual v2 JSON schema/projection, not inferred from a prose summary. At minimum it must include the eight report path patterns in §3. It must additionally resolve the effective-config fields in §4.

The registry must define:
- JSON file path;
- JSON Pointer or equivalent exact field path;
- source object/type and source field;
- whether the occurrence is direct JSON or opaque snapshot bytes;
- uint64 wrapper required/forbidden;
- duplication/equality relation where the same source value appears in multiple report views;
- historical fingerprint input domain;
- v2 JCS digest input domain.

The verifier must reject an unregistered direct seed field or a bare integer at any registered uint64 path. The same seed value appearing in multiple projections must round-trip to the same exact source integer.

## 10. Gate 180 disposition

| Requirement | Static result |
|---|---|
| Gate 179 typed uint64 object is JCS-compatible | DEFINED; source-compatible at the wire primitive level |
| Direct seed path inventory | INCOMPLETE — report pair-ledger copies omitted; effective-config scope unresolved |
| MatrixCapture source retention | NOT IMPLEMENTED |
| FrozenReportSnapshot source retention | NOT IMPLEMENTED |
| CapturedBenchmark compatibility constraints | DEFINED; not implemented |
| Calibration/Gate159/source/test companion assembly | NOT PROVIDED BY CURRENT CAPTURE API; separate boundary required |
| Strict v2 decoder/verifier | NOT IMPLEMENTED; current FrozenSnapshot codec is not a substitute |
| Regression definitions for new v2 properties | OPEN |
| Tests/CI | NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `CONDITIONAL — SOURCE/SCHEMA CROSSWALK INCOMPLETE; IMPLEMENTATION NOT READY`.

Gate 180 does not authorize source changes, tests, CI, seed generation, calibration, package generation, benchmark execution or scientific execution. It does not change `main`, canonical RMA/Matrix, claim status, C10 scientific design, or PR base.

## 11. Next operation — Gate 181

Gate 181 should close the source-to-wire projection contract before implementation:
1. correct the Gate 179 direct-seed registry, including duplicated pair-ledger occurrences;
2. define the exact effective ScenarioConfig projection and seed-field classification;
3. define the precise report payload projection and legacy fingerprint recomputation order;
4. define the companion-assembly interface and capture-ID binding without making the producer claim external evidence;
5. reconcile the exact 14-file schema and v2 verifier registry against these projections.

Only after Gate 181 is reconciled should a bounded implementation contract be proposed. Implementation and test execution remain subject to the required explicit authorization.
