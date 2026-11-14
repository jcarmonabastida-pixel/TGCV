# C10-S V_cont — Gate 182: integrated package v2 implementation contract

**Status:** IMPLEMENTATION CONTRACT DEFINED — IMPLEMENTATION NOT AUTHORIZED BY THIS GATE  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 181 source-to-wire projection contract  
**Scope:** additive capture API, MatrixCapture/FrozenReportSnapshot capture points, v2 serialization, companion assembly, deterministic archive writer and independent verifier  
**Execution:** GitHub source/document inspection only; no code edits, imports, compilation, tests, CI, seed generation, calibration, package generation, benchmark or scientific execution

## 1. Disposition

Gate 182 translates Gates 164/174/176/178/179/180/181 into a bounded implementation contract. It does not implement the contract or authorize a synthetic benchmark.

The implementation boundary is:

- preserve the existing Generator → Sealer → Analyzer → Evaluator behavior and scientific estimands;
- extend only the evidence capture/export boundary;
- keep package writing and verification pure with respect to synthetic generation;
- keep calibration, Gate 159, source-execution and test evidence as independent companion inputs;
- preserve the existing three-field `CapturedBenchmark` positional interface.

The current source still has no MatrixCapture/FrozenReportSnapshot retention, v2 writer, companion assembler or independent v2 verifier.

## 2. Historical reconstruction and source facts

The current source establishes:

1. `CapturedBenchmark` in `vcont_evidence_export.py` is a frozen dataclass with exactly three fields: mutable `report` dict, `outer_world_bundles` tuple, and `evidence_index` tuple.
2. `produce_and_capture_benchmark(..., matrix=None)` resolves `specs`, validates the 52-pair matrix, and passes that same tuple to Evaluator, but does not retain it in the return value.
3. The producer captures each RUN/R bundle before source objects are discarded and then invokes Evaluator once to build the benchmark report.
4. The Evaluator constructs `manifest_payload`, exposes it as report[`manifest`], and calculates `report_fingerprint` by applying `json.loads(json.dumps(manifest_payload, default=asdict, sort_keys=True))` followed by the source `_hash` function.
5. `_hash` uses Python JSON with sorted keys, compact separators and `allow_nan=False`, UTF-8 and SHA-256. This historical algorithm is not JCS.
6. The Generator selects each RNG stream from its explicit field when present, falling back to `seed` only when the corresponding explicit field is `None`. The existing producer uses `dataclasses.replace` to populate world/Z/G stream seeds from each SeedAssignment before calling Generator.
7. The existing `FrozenSnapshot` accepts dataclasses only and uses its own tagged JSON encoding; it is not the report JCS snapshot or an independent strict package decoder.
8. Gate 178 already defines MatrixCapture v1.0.0, canonical 52-row order, full-matrix digest including `tolerance_id`, FrozenReportSnapshot requirements, and calibration/Gate159 companion schemas. Gate 181 defines the v2 wire projections and source-to-wire registry.

No historical implementation satisfying these new capture/export requirements was located in the inspected branch files or GitHub code search. This is a source inspection result, not proof that no unindexed historical artifact exists.

## 3. Explicit schema-version migration

Gate 174's `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE` v1.0.0 derives `benchmark_export_id` from frozen design identity. Gate 181 changes the meaning to an alias of content-derived `capture_id`.

These meanings MUST NOT share one schema version.

- Preserve the Gate 174 v1.0.0 envelope and its historical meaning unchanged.
- Implement a new `TGCV-C10S-VCONT-RUN-EXPORT-ENVELOPE` v2.0.0 for package v2.0.0. In v2, `benchmark_export_id = capture_id` as specified by Gate 181.
- Preserve Gate 164 v1.0.0 package semantics and exact inventory as historical. The v2 writer emits a separately versioned package manifest/profile; it MUST NOT label v2 bytes as v1.0.0.
- CalibrationBankManifest uses the Gate 178 schema upgraded/versioned as specified by Gates 179/181; Gate159 companion remains its separately versioned artifact.
- A v1 reader MUST reject v2 envelope/package IDs and vice versa. No permissive downgrade or implicit conversion.

This is a compatibility migration, not a change to scientific content.

## 4. Module and API boundaries

### 4.1 Existing module: `vcont_evidence_export.py`

Only this module owns capture-time attachment to existing source objects.

Add immutable value types and pure projection helpers:

- `MatrixCapture` — Gate 178 schema v1.0.0, with exact typed row projection, design identity, legacy fingerprint and full JCS digest.
- `FrozenReportSnapshot` — Gate 181 schema v2.0.0, retaining immutable canonical JCS bytes, SHA-256, schema/type identity, historical report fingerprint and algorithm ID.
- `CapturedBenchmark` — retain the existing first three fields in the same order and with the same meanings; add trailing optional fields:
  - `matrix_capture: MatrixCapture | None = None`
  - `report_snapshot: FrozenReportSnapshot | None = None`
  - `capture_id: str | None = None`

Expose pure helpers (exact names are normative for this implementation slice):

- `capture_matrix(specs, design) -> MatrixCapture`
- `freeze_report_snapshot(report) -> FrozenReportSnapshot`
- `derive_capture_identity(design_identity, matrix_capture, outer_world_bundles, report_snapshot, evidence_index) -> str`

The existing producer's return type remains `CapturedBenchmark`. Producer-created captures MUST populate all three new fields. Direct legacy construction with the original three positional arguments remains valid but produces an incomplete capture that the v2 package writer rejects as `CAPTURE_INCOMPLETE`.

Do not add a second independently mutable copy of the report dictionary. `report` remains the compatibility view; `report_snapshot` is the authoritative immutable export input.

### 4.2 Capture sequence in `produce_and_capture_benchmark`

The sequence is normative:

1. Resolve `specs` once from the supplied matrix or the existing builder.
2. Run the existing benchmark-design validator without changing its historical fingerprint semantics.
3. Run a separate fail-closed canonical-order/type validator for Gate 178's 52-row matrix contract. It checks exact positional `SCENARIO_IDS × ESTIMAND_SPECS` order and every row field, including explicit `tolerance_id`; it does not sort or reconstruct rows.
4. Immediately capture `MatrixCapture` from that exact tuple.
5. Pass the same `specs` tuple, without transformation, to `evaluate_monte_carlo_benchmark(..., matrix=specs)`.
6. Immediately after Evaluator returns, create `FrozenReportSnapshot` from the returned source-typed report. The historical report fingerprint is recomputed/checked from the exact source `report["manifest"]` payload before any uint64 wire projection.
7. Retain the existing ordered `outer_world_bundles` and `evidence_index` unchanged.
8. Derive `capture_id` from Gate 181's identity payload using the exact MatrixCapture, bundle digests, report snapshot digest, design identity and evidence index.
9. Return `CapturedBenchmark(report, bundles, evidence_index, matrix_capture, report_snapshot, capture_id)`.

No sorting, seed derivation, calibration, extra Generator call, second Evaluator call or report reconstruction is allowed in these steps.

### 4.3 New module: `vcont_package_v2.py`

This module owns pure serialization and deterministic package construction. It MUST NOT import or invoke Generator, Sealer, Analyzer, Evaluator, `produce_and_capture_outer_world` or `produce_and_capture_benchmark`.

Normative public API:

- `build_package_v2(captured, design, companions, *, profile="CONFIRMATORY") -> PackageBuildResult`
- `serialize_package_files_v2(captured, design, companions, *, profile) -> Mapping[str, bytes]`
- `build_deterministic_tar_v2(files) -> bytes`

`PackageBuildResult` contains exact ordered file paths, per-file byte lengths and SHA-256 values, package ID, archive bytes and archive SHA-256. It does not claim external authentication.

The writer MUST:
- reject missing capture fields, mismatched capture identity, unsupported schema versions, unregistered uint64 paths, noncanonical matrix order, missing required companions or any source/companion mismatch;
- construct exactly the 14 Gate 164 paths, each exactly once; no fifteenth file;
- apply Gate 181's v2 projections and exact direct uint64 registry;
- preserve all legacy FrozenSnapshot bytes byte-for-byte in run_records;
- compute the historical report fingerprint before uint64 projection and verify it;
- use RFC 8785 JCS for each package JSON file and the manifest as required by the v2 schema;
- use deterministic uncompressed POSIX TAR with normalized path order, metadata, ownership, timestamps and modes under Gate 164's archive profile;
- derive package_id from the non-circular manifest identity inputs and all 14 file digests; derive archive SHA-256 only after TAR bytes exist;
- fail closed; never repair or silently coerce malformed inputs.

### 4.4 New module: `vcont_package_v2_verify.py`

This module owns independent verification. It MUST NOT call the writer's serialization, projection, package-ID or archive-building helpers. Shared constants/schema identifiers are allowed; algorithmic implementations and validation paths must be independently exercised.

Normative public API:

- `verify_package_v2(archive_bytes, *, expected_profile=None, trust_policy=None) -> PackageVerificationResult`

The verifier independently:
1. validates TAR structure, path safety, duplicate paths, exact 14-file inventory and deterministic metadata;
2. parses JSON with duplicate-key rejection before schema validation;
3. validates exact schema IDs/versions, field allowlists, required/nullable fields and value types;
4. validates RFC 8785 canonical bytes and file digests;
5. enforces the exact uint64 pointer registry and canonical unsigned-decimal/range grammar;
6. decodes typed uint64 wrappers only at registered pointers and rejects bare numbers/wrappers elsewhere;
7. checks all assignment, temporal-manifest, RUN/R, outer-world and duplicate report-view joins;
8. recomputes the historical report fingerprint from the decoded source-typed manifest payload using the frozen legacy algorithm;
9. validates MatrixCapture full digest and canonical 52-row order, including `tolerance_id`;
10. validates opaque FrozenSnapshot byte digests and allowlisted type/schema identities without treating legacy snapshot JSON as JCS;
11. validates companion schemas, capture/export joins, calibration/evaluation disjointness, Gate159 result derivation and source/test evidence bindings;
12. derives separate statuses for integrity, schema conformance, completeness, identity reconciliation, source provenance, technical test evidence and external authentication.

No producer-declared PASS, RECONCILED or AUTHENTICATED flag is accepted as verifier evidence. No aggregate PASS may conceal an unavailable layer. The verifier does not establish scientific validity, causal identification, Value attribution or TGCV claim status.

### 4.5 Companion inputs

`VContPackageCompanionsV2` is a distinct immutable input type, defined in `vcont_package_v2.py`, containing the actual Gate 178/179/181 calibration manifest, Gate159 reconciliation artifact, source-execution evidence and technical-test evidence.

The companion assembler MUST validate artifact schemas and joins; it MUST NOT synthesize evidence from CapturedBenchmark, GitHub declarations embedded by the producer or caller-supplied booleans.

The confirmatory profile requires all applicable companions. Missing/invalid companions block confirmatory output. A diagnostic profile, if implemented, requires a distinct schema/profile and can never be labelled confirmatory, reconciled or authenticated.

## 5. RFC 8785 implementation prerequisite

The inspected harness source has no report JCS snapshot implementation. Before implementing any v2 serializer, the implementation PR MUST pin one RFC 8785-conformant Python implementation in the harness dependency lock and record its exact version and artifact hash. It MUST include independently sourced RFC 8785 conformance vectors covering UTF-16 property ordering, escaping, number serialization, negative zero, exponent formatting, Unicode and invalid non-finite numbers.

A home-grown partial canonicalizer, ordinary `json.dumps(sort_keys=True)`, or the legacy FrozenSnapshot encoder is not an acceptable substitute.

The package verifier must independently check canonical bytes; it cannot accept a digest over merely parseable JSON.

## 6. Compatibility and migration rules

- Existing consumers of `CapturedBenchmark.report`, `outer_world_bundles` and `evidence_index` continue to receive the same types, values and ordering.
- The original three-argument positional constructor remains valid.
- v2 export rejects legacy/incomplete CapturedBenchmark instances without the new capture fields; it does not synthesize missing matrix/report snapshots after the fact.
- Existing v1 package/envelope artifacts, fingerprints, snapshot bytes and tests remain unchanged.
- New v2 fields are additive; no changes to Generator, Sealer, Analyzer, Evaluator, ScenarioConfig semantics, DGPs, estimands, N/M/R, assignment policies or scientific interpretation.
- No changes to `main`, canonical RMA, Evidence→Claim Matrix, STATUS or scientific claim status.

## 7. Required implementation sequence

Implementation must occur in this order, each step reviewable independently:

1. **Capture value types and pure projections:** MatrixCapture, FrozenReportSnapshot, exact JCS dependency pin, strict source projection helpers.
2. **Additive producer integration:** capture matrix before Evaluator, report immediately after Evaluator, compute capture_id; preserve old return fields and ordering.
3. **Pure v2 serializers:** uint64 registry, effective config/analysis-contract projections, seed and temporal manifests, run records, report envelope and 14-file inventory.
4. **Companion assembler:** calibration, Gate159, source-execution and technical-test artifacts.
5. **Deterministic archive writer:** manifest, package ID, TAR and archive digest.
6. **Independent verifier:** strict parser, schema validation, joins, legacy fingerprint and all digest/status layers.
7. **Regression suite and CI wiring:** only after implementation and under separate technical execution authorization.

Do not combine the first code change with synthetic generation or a full benchmark run. Unit tests for pure projections/serializers must use fixed inline fixtures and must not call the producer.

## 8. Required regression suite

Create focused test modules:

- `test_vcont_capture_v2.py`: matrix capture identity/order; report snapshot immutability; three-field positional compatibility; incomplete legacy capture rejection; exact report fingerprint preservation.
- `test_vcont_package_v2_serialization.py`: every uint64 pointer; effective ScenarioConfig exact allowlist; opaque snapshot byte preservation; 14-file inventory; JCS and deterministic TAR vectors.
- `test_vcont_package_v2_verifier.py`: independent positive fixtures, duplicate JSON keys, malformed uint64, unregistered seed paths, root/nested report mismatch, orphan/duplicate joins, bad fingerprints, tampered snapshots and path traversal.
- `test_vcont_package_v2_companions.py`: valid and invalid calibration/Gate159/source/test companions; missing companion blocks confirmatory output; companion changes package_id but not capture_id.
- `test_vcont_package_v2_compatibility.py`: old positional CapturedBenchmark construction and unchanged legacy v1 fixtures.

All tests must be deterministic and use no random seed generation, no Generator, no Sealer, no Analyzer, no Evaluator and no scientific DGP execution. A separate producer integration test, if later necessary, requires its own explicit authorization because invoking the producer generates synthetic observations.

## 9. Acceptance criteria

The implementation is acceptable only when:

1. Existing three-field CapturedBenchmark consumers remain unchanged.
2. Producer-created capture contains immutable exact matrix/report snapshots and deterministic capture_id.
3. The exact same canonical matrix tuple is captured and passed to Evaluator.
4. Historical report fingerprint remains byte-for-byte compatible.
5. All v2 projections match Gate 181 and every direct uint64 path is registered.
6. Package writer emits exactly 14 deterministic files and a deterministic TAR.
7. Independent verifier validates all layers without using writer internals.
8. Missing or contradictory companions fail closed.
9. v1/v2 schema separation and rejection are tested.
10. Required deterministic technical tests pass under a separately authorized technical execution.
11. No scientific estimand, DGP, generator behavior or scientific claim is altered.

A package writer PASS is not a technical test PASS, external provenance reconciliation, cryptographic authentication or scientific result.

## 10. Gate 182 disposition and authorization boundary

| Item | State |
|---|---|
| Historical source/API facts | AUDITED STATICALLY |
| MatrixCapture/FrozenReportSnapshot contracts | DEFINED in Gates 178/181 |
| Additive CapturedBenchmark API | DEFINED |
| Capture sequence | DEFINED |
| v1/v2 envelope migration | DEFINED |
| Writer/verifier module boundary and APIs | DEFINED |
| RFC 8785 dependency/version | OPEN prerequisite before code |
| Implementation | NOT IMPLEMENTED |
| Tests / CI | NOT EXECUTED |
| Seed generation / calibration / package / benchmark | NOT AUTHORIZED / NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |
| main / canonical state / PR base | UNCHANGED |

**Overall:** `IMPLEMENTATION CONTRACT DEFINED — CONDITIONAL ON PINNED RFC 8785 DEPENDENCY; IMPLEMENTATION NOT AUTHORIZED BY THIS GATE`.

This gate is sufficient to prepare a bounded implementation change after the JCS dependency decision is recorded. It does not authorize running the synthetic producer, calibrating, generating seed banks, packaging benchmark output or conducting a scientific experiment.

## 11. Next operation — Gate 183

Gate 183 should perform a final static implementability preflight against the exact dependency lock, workflow permissions and test layout, then produce a file-by-file implementation plan. Only after that preflight should a separate explicit authorization govern code changes and deterministic technical tests. Scientific execution remains separately governed.

## 12. Gate 183 — preflight disposition

Gate 183's static preflight confirms that the implementation architecture is feasible but blocks an ordinary in-branch harness code push under the current workflow configuration. The push trigger in `.github/workflows/c10-s-focal-harness-tests.yml` covers every path under `03_EXPERIMENTS/C10-S/harness/**` and runs the full unittest suite; `test_vcont_integrated_harness.py` calls Generator.generate and both evidence producers, so this workflow is not a pure serializer-only suite. The harness and repository also have no dependency lock/project manifest and no pinned RFC 8785/JCS implementation.

No workflow, code, dependency or test was changed. Gate 183 recommends a governed workflow split so pure v2 fixture tests can run independently while producer/integrated synthetic tests remain behind separate explicit authorization. Gate 183 is CONDITIONAL / BLOCKED pending the CI execution-boundary decision and pinned JCS dependency. See `C10_S_VCONT_PACKAGE_V2_IMPLEMENTATION_PREFLIGHT_GATE_183_DRAFT_001.md`. This supersedes no Gate 182 API decision; it adds an execution-governance prerequisite.
