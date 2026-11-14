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
4. Join every legacy tuple to its RunEvidenceBundle by `run_id`; restore and compare TruthBundle, AnalyzerResult, AnalysisContract and RunManifest against the exact captured snapshots.
5. Populate the existing `scenario_outer_runs[scenario_id][outer_id]` structure with the unchanged legacy tuples.
6. Retain exactly one OuterWorldEvidenceBundle and one evidence-index row for that scenario/M.
7. Invoke `Evaluator.evaluate_monte_carlo_benchmark()` exactly once after all groups have been captured.
8. Verify 52 unique pair-ledger rows, 13 scenario reports, complete temporal-manifest cardinality and exactly 13×M evidence bundles.

The benchmark evaluator remains the sole producer of the existing pair ledger and report fingerprint. Gate 172 does not reimplement or rewrite its aggregation.

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
