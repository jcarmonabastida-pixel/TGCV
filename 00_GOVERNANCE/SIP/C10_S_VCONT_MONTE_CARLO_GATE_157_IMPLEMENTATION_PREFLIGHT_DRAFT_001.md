# C10-S V_cont — Gate 157 Implementation Preflight

**Status:** IMPLEMENTATION PREFLIGHT COMPLETED — CODE CHANGE AUTHORIZATION REQUIRED  
**Branch:** `research/c10-s-consolidation-draft`  
**Governing contract:** `C10_S_VCONT_MONTE_CARLO_MATRIX_COVERAGE_CONTRACT_GATE_156_DRAFT_001.md`  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / seed-bank generation:** NOT EXECUTED

## 1. Historical reconstruction

The current branch contains:
- Gate 154 outer-M/R separation contract.
- Gate 155 implementation and deterministic technical verification.
- Gate 156 52-pair MONTE_CARLO matrix-coverage contract.

Gate 155's per-scenario `Evaluator.evaluate_monte_carlo()` is reusable and must not be rewritten wholesale. Gate 157 should add a benchmark-level composition layer and only extend lower-level identities where the contract proves that necessary.

## 2. Verified implementation boundary

The current code establishes:
- `build_scenario_estimand_matrix()` returns 52 unique pairs (13 scenarios × 4 estimands).
- `Evaluator.evaluate_monte_carlo()` accepts one scenario/version and returns four estimand summaries plus per-M source tuples.
- The method already keeps the designated RUN separate from R and aggregates repeated-assignment reports within each M.
- The matrix adapter already produces RUN and REPEATED_ASSIGNMENT pair records with the correct temporal classes.

The following Gate 156 requirements are not yet implemented:
1. A benchmark-level method composing all 13 per-scenario M blocks into exactly 52 pair-ledger rows.
2. A declared benchmark design object fixing scenario versions, N, M, R, matrix identity and pair-keyed MCSE targets.
3. Exact R completeness enforcement for every M; current `evaluate_monte_carlo()` requires one RUN but does not require a declared R count or contiguous R identities.
4. Full pair-keyed metric targets; current per-scenario method accepts generic metric names such as `run_conditional.mae`, which do not identify the full matrix key.
5. A canonical per-M contribution ledger with status and numeric denominators for each pair.
6. A report fingerprint and deterministic reconstruction checks.

## 3. Identity gap discovered

`SeedAssignment.replicate` stores the R index (with -1 reserved for RUN), but the runtime identity chain currently exposes `outer_replicate_id` and `assignment_role` without a dedicated integer R index in `ScenarioConfig`, `RunManifest`, `TruthBundle` and `AnalyzerResult`.

A string `replicate_id` is not a substitute for a typed, validated R index. Gate 157 must propagate the exact assignment index from SeedAssignment through Generator, sealed provenance, Analyzer and Evaluator, and verify:
- RUN index = -1;
- repeated indices = exactly 0..R-1;
- no duplicate or omitted index within an M;
- index/role consistency at every identity boundary.

This is a required extension to Gate 155's identity propagation, not a reason to change the meaning of M or R.

## 4. Implementation plan

1. Add a typed assignment index to the runtime identity chain and its integrity hashes.
2. Add an immutable benchmark design object with exact 13 scenario/version declarations, N/M/R, matrix fingerprint and pair-keyed metric targets.
3. Validate each scenario block before invoking the existing per-scenario M Evaluator.
4. Compose all 13 outputs into a 52-row pair ledger; preserve RUN status alongside repeated-level numeric reference-regime contributions where both temporal levels apply.
5. Retain exactly one per-M contribution for each pair, including status-only/non-identifiable dispositions.
6. Compute per-pair denominators, rates and precision states without pooling scenario/version/N/temporal levels.
7. Fingerprint the design, matrix, temporal manifest, contribution ledger and final report.
8. Add deterministic fail-closed tests for complete coverage, omissions, duplicates, version mismatch, M/R counts, role/index mismatch, pair-keyed targets and summary reconstruction.
9. Run the existing technical verification workflow only after the final code/test commit; do not generate banks or run calibration/benchmark experiments.

## 5. Important limitation to preserve

The current adapter fails closed when an EVALUABLE pair lacks finite truth/output or an identified Analyzer estimate. Gate 156 requires that such a failure remain visible as an invalid/failed contribution rather than silently disappearing. Gate 157 must decide and test an explicit invalid-contribution representation at the benchmark-ledger boundary; it must not catch identity/provenance errors and relabel them as ordinary Analyzer abstentions.

No numeric M/R/N, MCSE target, recovery threshold or scientific acceptance threshold is selected by this preflight.

## 6. Gate state

- Gate 156: DEFINED / PERSISTED; implementation OPEN.
- Gate 157 preflight: COMPLETED / PERSISTED.
- Gate 157 code implementation: OPEN pending explicit authorization for integrated code/test changes.
- No tests have been run for this preflight.
- No seed bank, calibration, Monte Carlo sizing, benchmark or scientific execution has been generated or performed.
- `main` unchanged; PR #116 remains Draft on its existing base branch.


## 7. Supersession by completed implementation

This preflight is retained as the historical authorization boundary and diagnosis record. Its former statement that code implementation was OPEN is superseded by the completed implementation record:

`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_BENCHMARK_AGGREGATION_IMPLEMENTATION_GATE_157_DRAFT_001.md`.

Gate 157 is now IMPLEMENTED / TECHNICALLY VERIFIED at commit `0afb77fb45308a7d1573d0ab644a9d6f69e7302d`, workflow run `43494346461` (compile PASS; primary 99/99 PASS; clean replay 99/99 PASS). No seed bank, calibration, Monte Carlo sizing, benchmark study or scientific execution was generated or performed.
