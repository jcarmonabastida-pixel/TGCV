# C10-S V_cont — Gate 172: benchmark-wide evidence envelope

**Status:** BENCHMARK-WIDE DRIVER IMPLEMENTED IN SOURCE; NOT EXECUTED / NOT RUNTIME VERIFIED  
**Branch:** `research/c10-s-consolidation-draft`  
**Depends on:** Gates 154, 166–171  
**Scientific execution:** NOT AUTHORIZED  
**Tests/CI:** NOT EXECUTED

## 1. Objective and historical boundary

Gate 171 closed the producer boundary for one scenario/N/M group. It returned an `OuterWorldEvidenceBundle` and the unchanged four-object tuples required by the existing Monte Carlo evaluator.

Gate 172 adds the benchmark-wide coordinator. It does not replace or modify Generator, Sealer, Analyzer, Evaluator, the frozen `MonteCarloBenchmarkDesign`, the 52-pair matrix, estimands, denominators, metric targets or M/R aggregation semantics.

## 2. New API

Source: `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`

`produce_and_capture_benchmark(design, assignments, config_templates, *, tolerance, matrix=None) -> CapturedBenchmark`

Return type:

- `CapturedBenchmark.report`: exact result returned by the existing `Evaluator.evaluate_monte_carlo_benchmark()`.
- `CapturedBenchmark.outer_world_bundles`: one complete `OuterWorldEvidenceBundle` per scenario/M.
- `CapturedBenchmark.evidence_index`: ordered `(scenario_id, outer_replicate_id, world_id)` references for the evidence envelope.

The API is inert when imported/defined. Calling it is an execution operation: it generates synthetic observations and evaluates the complete benchmark. Gate 172 did not call it.

## 3. Inputs and fail-closed preflight

The driver requires:

1. One `MonteCarloBenchmarkDesign` that passes the existing `validate_monte_carlo_benchmark_design()` against the supplied or registered 52-pair matrix.
2. Exactly one structural `ScenarioConfig` template for each of the 13 registered scenario IDs, with version and N matching the design.
3. Already-materialized evaluation-bank `SeedAssignment` rows with exact cardinality:
   `13 × M × (1 + R)`.
4. Exact scenario/version/N/M grouping, with M identities `outer-000000 … outer-(M-1)`.
5. Exactly one RUN (index -1) and R repeated assignments (indices 0…R-1) in every group; no duplicate role/index keys.
6. One shared world seed per M group and unique Z/G assignment seeds within each M group.

Missing or extra scenario/M groups, wrong bank, malformed identities, incomplete R groups, duplicate assignment keys and incompatible templates are rejected before the first call to Generator.

The producer does not build or derive a seed bank. It does not infer assignments from the design.

## 4. Integrated sequence

In deterministic `SCENARIO_IDS` order, then ascending M:

1. Partition the exact assignment rows by scenario/version/N/M.
2. Call `produce_and_capture_outer_world()` exactly once for each group.
3. Verify the returned M bundle identity and expected RUN+R tuple count.
4. Join every legacy tuple to its RunEvidenceBundle by `run_id`; compare the truth fields against the exact registered Gate 166 `MatrixTruthProjection` (the bundle intentionally excludes potential-outcome arrays), and restore/compare AnalyzerResult, AnalysisContract and RunManifest against their exact captured snapshots.
5. Populate the existing `scenario_outer_runs[scenario_id][outer_id]` structure with the unchanged legacy tuples.
6. Retain exactly one OuterWorldEvidenceBundle and one evidence-index row for that scenario/M.
7. Invoke `Evaluator.evaluate_monte_carlo_benchmark()` exactly once after all groups have been captured.
8. Verify 52 unique pair-ledger rows, 13 scenario reports, complete temporal-manifest cardinality and exactly 13×M evidence bundles.

The benchmark evaluator remains the sole producer of the existing pair ledger and report fingerprint. Gate 172 does not reimplement or rewrite its aggregation. After evaluation, the driver also performs one-to-one equality checks between captured RUN/R RunManifest identities and the returned temporal manifest, and checks each of the 52 pair contributions against the matching scenario/M world and designated RUN `run_id` in the evidence envelope.

## 5. Regression source

Source: `03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`

Three Gate 172 tests were added:

- positive complete-envelope case asserting 52 pairs, 13 scenarios, 13×M bundles and 13×M×(1+R) temporal rows;
- missing scenario/M group rejected before generation;
- calibration-bank contamination rejected before generation.

The positive regression invokes the complete synthetic driver when the test is run. **No tests were executed in Gate 172.** No runtime PASS, CI result, benchmark result or scientific result is claimed.

## 6. Provenance and authentication limits

The design validator checks the declared seed-bank fingerprint, configuration fingerprint and executable commit for format and structural presence, but it does not independently recompute those values from the effective assignments, configurations and executing process. Gate 172 checks assignment coverage and internal joins; it does not authenticate that the caller's declared seed-bank fingerprint or executable commit is truthful.

Therefore:

- assignment identity and coverage: structurally checked by the driver;
- evidence-to-legacy-tuple identity: checked by snapshot restoration and equality;
- seed-bank fingerprint reconciliation against the exact rows: OPEN under Gate 159;
- effective configuration fingerprint recomputation: OPEN under Gate 159;
- executable commit attestation: OPEN under Gate 159 / trusted-builder work;
- canonical package JCS/tar writer and external attestation: OPEN.

Do not label the output provenance-authenticated or independently reproducible until these remaining checks and the package/attestation chain are implemented.

## 7. Disposition

- Gate 171 per-M producer: reused; not duplicated.
- Benchmark-wide 13-scenario driver: IMPLEMENTED IN SOURCE.
- One call per declared scenario/M: encoded in driver source.
- Existing benchmark evaluator: called once by driver source.
- Existing 52-pair ledger and temporal manifest: retained as evaluator output and cardinality-checked.
- Evidence envelope: exactly one OuterWorldEvidenceBundle per scenario/M, with per-run source joins.
- Regression source: ADDED / NOT EXECUTED.
- Runtime / CI / benchmark: NOT EXECUTED.
- Gate 159 reconciliation, canonical package and trusted attestation: OPEN.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 8. Next operation — Gate 173

Audit the benchmark-wide source boundary and package readiness without executing it. Verify that the driver truly invokes the benchmark evaluator once, that all evidence bundles are co-addressable with the 52-pair ledger and temporal manifest, that the envelope can be serialized without lossy reconstruction, and that report fingerprint versus evidence-package digest are distinct and non-circular. Then specify the minimal canonical benchmark package schema and capture manifest, preserving the legacy report fingerprint and SealedEvidence digest semantics. Keep Gate 159 authentication gaps explicit; do not sign or claim authentication until a trusted builder and attestation workflow exist.

## 9. Gate 173 — package-readiness qualification

Gate 173 confirms statically that the `CapturedBenchmark` source envelope contains the Gate 166 run snapshots, inline SealedEvidence rows+manifest, exact per-run reports, one repeated aggregate per scenario/M, the evaluator report and scenario/M/world index. This resolves Gate 165's source-capture absence at the orchestration boundary; it does not make the reduced report independently sufficient.

The Gate 164 archive can retain its exact path inventory. `runs/run_records.json` is to be serialized as a versioned envelope containing all RUN/R RunEvidenceRecords and all OuterWorldEvidenceBundles, with explicit order, cardinalities and join keys. The exact matrix used by the evaluator must also be retained as its own Gate 164 design file.

No package serialization exists yet. FrozenSnapshot's tagged JSON bytes, SealedEvidence's legacy digest and the evaluator's report fingerprint are separate legacy/source integrity layers, not JCS. A package adapter must round-trip snapshots and recompute legacy SealedEvidence digests before computing separate JCS file/manifest/archive digests.

Gate 159, calibration manifest, GitHub-resolved workflow/source/artifact metadata, JCS/tar writer and independent verifier remain open. No tests, package build or benchmark was executed. See Gate 173.

## 10. Gate 175 — exact matrix capture gap

Gate 175 confirms that `produce_and_capture_benchmark()` accepts and validates the exact matrix, then uses it for the 52-pair evaluation, but the returned `CapturedBenchmark` does not retain that matrix. Its report contains the design/fingerprint and resulting pair ledger only. Therefore Gate 172's benchmark-wide evidence envelope is complete for RUN/R and M evidence but not self-contained for exact matrix export. A capture-time immutable matrix payload (or immutable companion explicitly bound to the same capture/design) is required; do not reconstruct it from current code.

The existing matrix fingerprint also omits `ScenarioEstimandSpec.tolerance_id`; retain it as legacy and add a separately versioned full-matrix digest. Calibration, Gate 159 and external workflow/test provenance remain separate absent inputs. See Gate 175. No execution occurred.

## 11. Gate 176 — complete benchmark capture qualification

Gate 172's benchmark envelope now has a defined extension: the exact 52-row matrix passed to the evaluator must be retained in a capture-time immutable `MatrixCapture`, not reconstructed from the report or current source. The full-matrix JCS digest includes all ScenarioEstimandSpec and EvaluationKey fields, including `tolerance_id`; the legacy fingerprint remains unchanged.

The frozen CapturedBenchmark wrapper does not make its nested report dict immutable. Gate 176 therefore adds a required immutable report snapshot as the authoritative package-export payload, while preserving the legacy report view. Calibration, Gate 159, source-execution and technical-test evidence remain independent companion artifacts. See Gate 176. No implementation/execution occurred.
