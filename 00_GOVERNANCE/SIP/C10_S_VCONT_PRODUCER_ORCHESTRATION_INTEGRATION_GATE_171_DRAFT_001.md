# C10-S V_cont — Gate 171: producer/orchestration integration at the M boundary

**Status:** M-LEVEL PRODUCER BOUNDARY IMPLEMENTED IN SOURCE; BENCHMARK-WIDE DRIVER INTEGRATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Depends on:** Gates 154, 166–170  
**Scientific execution:** NOT AUTHORIZED  
**Tests/CI:** NOT EXECUTED

## 1. Purpose and historical reconstruction

Gate 167 established that Generator, Sealer, Analyzer and Evaluator produce the required objects but the existing Monte Carlo evaluator receives only the legacy four-object tuple:

`(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)`.

Gate 168 specified a typed, immutable carrier. Gate 169 withdrew the erroneous world-identity blocker. Gate 170 implemented the standalone `RunEvidenceBundle.capture(...)` and `OuterWorldEvidenceBundle.capture(...)` primitives, but did not call them from a producer/orchestration function.

Static inspection of the current branch found no existing V_cont benchmark producer/driver that loops the 13 scenario blocks and invokes `evaluate_monte_carlo_benchmark()`. The evaluator itself validates and aggregates already-produced tuples; it does not own the source objects at Generator/Sealer/Analyzer time. The separate P178 runner uses the older focal harness and is not the V_cont producer.

Gate 171 therefore adds the smallest explicit M-level producer boundary. It does not modify the Generator, Sealer, Analyzer, Evaluator or benchmark aggregation semantics.

## 2. Implemented API

Source: `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`

New public function:

`produce_and_capture_outer_world(assignments, config_template, *, expected_repeated_assignments, tolerance) -> CapturedOuterWorld`

New immutable return carriers:

- `CapturedRun`: one `RunEvidenceBundle` plus the unchanged legacy evaluator tuple.
- `CapturedOuterWorld`: one `OuterWorldEvidenceBundle` plus the ordered legacy tuples needed by the existing aggregation interface.

The function accepts already-materialized typed evaluation-bank `SeedAssignment` rows. It does not build, derive, or mutate a seed bank.

## 3. Orchestration sequence

For one scenario/N/M group, the producer:

1. Requires exactly one RUN (index -1) and exactly R repeated assignments (indices 0..R-1).
2. Rejects cross-scenario, cross-version, cross-N, cross-M, cross-world, wrong-bank and duplicate assignment-stream groups before generation.
3. Applies the exact row's world/Z/G seeds, M identity, role and index to a copy of the frozen structural ScenarioConfig template. The template's base `seed` and legacy `replicate_id` remain as supplied; neither is overloaded as M or R.
4. Calls the existing Generator and captures RunManifest, TruthBundle and EvidenceCandidate immediately.
5. Calls the existing Sealer and retains the complete SealedEvidence, including rows and manifest.
6. Derives the existing AnalysisContract using `contract_for(config)`, calls Analyzer, then calls Evaluator only after Analyzer returns.
7. Calls `RunEvidenceBundle.capture(...)` while every exact source object is still available.
8. Preserves the unchanged four-object tuple for each run, in deterministic order: RUN, then R=0..R-1.
9. Calls the existing `Evaluator.evaluate_repeated_assignment()` once for the R rows and passes that exact report plus the captured run bundles to `OuterWorldEvidenceBundle.capture()`.
10. Returns both the immutable evidence carrier and the unchanged tuples expected by the existing Monte Carlo aggregation API.

The producer does not reconstruct any source object from an EvaluationReport or aggregate summary.

## 4. Compatibility boundary

The existing public interfaces and semantics remain unchanged:

- `Generator.generate(config)`
- `Sealer.seal(candidate)`
- `Analyzer.analyze(sealed, contract)`
- `Evaluator.evaluate(...)`
- `Evaluator.evaluate_repeated_assignment(...)`
- `Evaluator.evaluate_monte_carlo(...)`
- `Evaluator.evaluate_monte_carlo_benchmark(...)`

The new producer is an explicit orchestration entry point alongside those APIs. Its returned `evaluator_runs` can be inserted into the existing per-M input structure without changing the 52-pair matrix ledger, estimands, report calculations, denominators or M/R aggregation order.

No new field is added to SeedAssignment or RunManifest. In particular, the SeedAssignment row remains the authority for bank identity; `replicate_id` remains the legacy ScenarioConfig/RunManifest field and is not treated as M or R.

## 5. Regression source added

Source: `03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`

Three tests were added:

- successful production/capture of one RUN + one R assignment, verifying the M bundle and legacy tuple cardinality;
- fail-closed rejection of a missing R row before generation;
- fail-closed rejection of cross-M row mixing before generation.

The successful test uses a small deterministic fixture and checks typed restoration of the repeated-assignment report. **No test has been executed.** No syntax, runtime, CI or PASS result is claimed.

## 6. Remaining boundary and limitations

- There is still no benchmark-wide driver that loops all 13 scenarios × M and invokes this function for each M.
- The caller must provide the exact pre-materialized evaluation-bank assignments and the matching structural ScenarioConfig template for each scenario.
- The caller must collect each returned `evaluator_runs` under the correct scenario/M key before calling `evaluate_monte_carlo_benchmark()`.
- The final 13-scenario benchmark result and its 52-pair ledger are not yet co-exported with all OuterWorldEvidenceBundles in one benchmark envelope.
- Calibration-bank manifests, Gate 159 producer-claim reconciliation, canonical JCS package writer, deterministic tar packager, trusted builder and attestation remain OPEN.
- The API performs synthetic generation and evaluation when called. This gate only defines and persists the API; it does not call it.
- Structural validation is not external provenance authentication and is not causal scientific evidence.

## 7. Disposition

- Per-run capture primitive (Gate 170): IMPLEMENTED IN SOURCE.
- Explicit per-run producer sequence: IMPLEMENTED IN SOURCE.
- M grouping and one OuterWorldEvidenceBundle per M: IMPLEMENTED IN SOURCE.
- Legacy four-object evaluator tuple compatibility: PRESERVED IN SOURCE.
- Regression source: ADDED / NOT EXECUTED.
- 13-scenario benchmark-wide caller/driver: OPEN.
- 52-pair ledger plus evidence-envelope co-export: OPEN.
- Gate 159 reconciliation and package/attestation: OPEN.
- Tests, CI, calibration, seed-bank generation, N/R/M sizing, Monte Carlo, benchmark and scientific execution: NOT AUTHORIZED / NOT PERFORMED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 8. Next operation — Gate 172

Implement the benchmark-wide driver that accepts the frozen `MonteCarloBenchmarkDesign`, exact evaluation-bank SeedAssignment rows and 13 structural ScenarioConfig templates; partitions rows deterministically by scenario and M; calls `produce_and_capture_outer_world()` exactly once per declared M; builds the existing `scenario_outer_runs` tuple structure without altering its contents; invokes the existing `evaluate_monte_carlo_benchmark()` once; and returns the 52-pair benchmark result together with exactly one evidence bundle per scenario/M. Add static/adversarial regressions for missing/extra scenario blocks, M/R cardinality, cross-bank contamination, duplicate run IDs and evidence/legacy-tuple identity. Do not execute the driver or tests without the applicable technical execution authorization.


## 9. Gate 172 supersession — benchmark-wide coordinator added

Gate 172 adds `produce_and_capture_benchmark(...)` in `vcont_evidence_export.py`. It validates the frozen design, 13 structural templates and exact evaluation assignment coverage; invokes the Gate 171 producer once per scenario/M; checks each legacy tuple against its captured source snapshots; builds the existing `scenario_outer_runs` input; calls the unchanged `evaluate_monte_carlo_benchmark()` once; and returns the 52-pair report together with one OuterWorldEvidenceBundle per scenario/M.

The Gate 171 statement that no benchmark-wide caller existed is superseded at source-design level. Neither Gate 171 nor Gate 172 has been runtime-executed. Gate 159 fingerprint reconciliation and external attestation remain OPEN. See Gate 172 for exact scope and limits.
