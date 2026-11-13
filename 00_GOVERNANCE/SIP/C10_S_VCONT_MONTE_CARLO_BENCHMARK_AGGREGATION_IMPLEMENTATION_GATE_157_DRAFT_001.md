# C10-S V_cont — Gate 157: MONTE_CARLO Benchmark Aggregation Implementation

**Status:** IMPLEMENTED / TECHNICALLY VERIFIED — TARGETED CLASSIFICATION REGRESSION PASS  
**Branch:** `research/c10-s-consolidation-draft`  
**Governing contract:** `C10_S_VCONT_MONTE_CARLO_MATRIX_COVERAGE_CONTRACT_GATE_156_DRAFT_001.md`  
**Preflight:** `C10_S_VCONT_MONTE_CARLO_GATE_157_IMPLEMENTATION_PREFLIGHT_DRAFT_001.md`  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / evaluation seed-bank generation:** NOT EXECUTED

## 1. Implemented scope

Gate 157 completes the benchmark-level integration specified in Gate 156. The implementation reuses Gate 155's per-scenario M Evaluator and adds the missing typed assignment identity, declared benchmark design, 13-scenario composition, 52-pair ledger, temporal manifest and report fingerprint.

### 1.1 Typed R identity

A typed `assignment_index` now propagates through:
- `ScenarioConfig`;
- `RunManifest`;
- `TruthBundle`;
- sealed evidence provenance;
- `AnalyzerResult`;
- Evaluator identity and output-seal checks.

Rules:
- designated RUN: `assignment_role="RUN"`, `assignment_index=-1`;
- repeated assignment: `assignment_role="REPEATED_ASSIGNMENT"`, nonnegative integer index;
- within each M: exactly the declared contiguous indices `0..R-1`, with no duplicate;
- `SeedAssignment.assignment_index` is an explicit typed property over the legacy R field `replicate`.

The legacy `replicate` meaning remains R; it is not redefined as M.

### 1.2 Declared benchmark design and matrix validation

`MonteCarloBenchmarkDesign` declares:
- exactly 13 scenario/version identities;
- N, M and R;
- authoritative matrix fingerprint;
- pair-keyed MCSE targets for every numeric EVALUABLE pair/metric;
- seed-bank label and fingerprint;
- executable commit and configuration fingerprint.

The validator fails closed on incomplete/duplicate scenario identities, non-52 or duplicate matrix keys, version/fingerprint mismatch, missing/extra/duplicate metric targets, invalid M/R/N and absent/invalid provenance identities.

### 1.3 Benchmark-level aggregator

`Evaluator.evaluate_monte_carlo_benchmark()` composes the existing per-scenario M aggregation across all 13 scenarios and requires exactly 52 unique matrix keys.

It emits:
- a temporal manifest with one RUN and R repeated assignments for each M, including world/assignment seeds and run identities;
- one per-M contribution for every matrix pair, at its authorized temporal level;
- a 52-row pair ledger with expected/observed M, numeric and status denominators, separate RUN and repeated status rates, expected/observed identification and abstention adjudication, and metric precision status;
- bias, MAE and RMSE with M-level MCSE only for complete numeric EVALUABLE series;
- no numeric scoring for STATUS_ONLY or NOT_IDENTIFIABLE classes;
- separate NOT_IDENTIFIED, INDETERMINATE, ABSTAINED, TRUTH_MISSING and INVALID_OUTPUT dispositions;
- a canonical report manifest and SHA-256 fingerprint binding design identities, metric targets, temporal manifest and pair ledger.

Incomplete M/R identity or temporal manifests are rejected; they cannot be silently reinterpreted as abstention or omitted from denominators. An incomplete numeric series does not produce a deceptively complete metric summary.

## 2. Changed implementation and tests

- `03_EXPERIMENTS/C10-S/harness/vcont_benchmark_protocol.py`
- `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py`
- `03_EXPERIMENTS/C10-S/harness/test_vcont_benchmark_protocol.py`
- `03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`

Deterministic tests cover typed RUN/R identity, exact R completeness, exact 13×4 matrix coverage, duplicate/missing matrix and metric-target rejection, provenance validation, complete temporal manifest, status-only non-scoring and the reconstructable 52-pair output. The integration fixture is a bounded deterministic test fixture (N=16, M=2, R=2); it is not a calibration, seed-bank generation, benchmark study or scientific execution.

## 3. Technical verification

**Verified commit:** `0afb77fb45308a7d1573d0ab644a9d6f69e7302d`  
**GitHub Actions run:** `43494346461`  
**Result:** compile PASS; primary suite 99/99 PASS; clean source-archive replay 99/99 PASS.  
**Artifact ID:** `14070228979`  
**Artifact SHA-256:** `c9cb24f9d4504f609abbf8d7eaa8ce0ad839279cbc0b2ddc0c2768b8b1a556c7`  
**Workflow:** https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43494346461

This is deterministic technical verification only. It is not scientific, causal, calibration or benchmark evidence.

## 4. Remaining boundaries

- Numeric N/R/M design and calibration remain OPEN.
- Pair-specific MCSE targets are required inputs; no targets are selected by this implementation.
- The benchmark report records supplied seed-bank/configuration/executable identities; the authorized caller remains responsible for supplying the canonical values matching the actual bank and execution.
- No calibration or evaluation seed bank was generated.
- No Monte Carlo sizing, calibration, benchmark run or scientific execution was performed or authorized.
- `scientific_execution=false`; `execution_authorized=false`.

## 4.1 Post-verification audit — invalid-output classification

A post-closure audit initially found that the 99-test Gate 157 suite did not directly exercise the `TRUTH_MISSING` and `INVALID_OUTPUT` branches. The gap was corrected with a dedicated integration regression in `test_vcont_integrated_harness.py`.

The regression constructs two outer worlds for the same EVALUABLE RUN-conditional pair:
- M0: the DGP run truth is absent while the Analyzer status remains IDENTIFIED; expected classification `TRUTH_MISSING`.
- M1: the DGP truth is present while the sealed Analyzer estimate is absent and its status remains IDENTIFIED; expected classification `INVALID_OUTPUT`.

Assertions verify both distinct contribution states, `truth_missing_count=1`, `invalid_output_count=1`, `missing_contribution_count=0`, `status_denominator=2`, `numeric_denominator=0`, `abstention_count=0`, and `observed_M=expected_M=2`.

**Targeted verification:** commit `a399c5810fa988b31390e2957671f6bf134836b7`; GitHub Actions run `43496381997`; compile PASS; primary suite 100/100 PASS; clean source-archive replay 100/100 PASS. Artifact ID `14070369862`; SHA-256 `c9a3050c8081bb48099b57ad123cd2e955c31f88791529016c2943252b5f9ffd`. Workflow: https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43496381997.

Corrected status:
- Classification code: IMPLEMENTED.
- Targeted regression: PASS.
- General technical suite and clean replay: PASS (100/100 each).
- Gate 157 classification item: CLOSED — TECHNICALLY VERIFIED.
- This is deterministic software verification, not calibration, benchmark evidence or scientific execution.

No calibration, seed-bank generation or scientific execution is authorized by this verification.

## 5. Gate status

- Gate 154: M/R separation contract — DEFINED / PERSISTED.
- Gate 155: outer M and per-scenario aggregation — IMPLEMENTED / TECHNICALLY VERIFIED.
- Gate 156: 52-pair matrix coverage contract — IMPLEMENTED / TECHNICALLY VERIFIED through Gate 157.
- Gate 157: benchmark-level aggregation, typed R identity and `TRUTH_MISSING` / `INVALID_OUTPUT` classification regression — IMPLEMENTED / TECHNICALLY VERIFIED (100/100 primary + 100/100 clean replay; run `43496381997`).
- `main` unchanged; PR #116 remains Draft on its original base branch.
