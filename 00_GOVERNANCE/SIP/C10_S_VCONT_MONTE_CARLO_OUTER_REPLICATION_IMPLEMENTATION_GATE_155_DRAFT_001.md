# C10-S V_cont — Gate 155: Outer Monte Carlo Replication Implementation

**Status:** IMPLEMENTED — TECHNICALLY VERIFIED  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** C10-S synthetic V_cont harness and calibration/evaluation seed protocol  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / seed-bank generation:** NOT EXECUTED

## 1. Governing contract and boundary

This implementation realizes the identity and aggregation contract in:

`C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_CONTRACT_DRAFT_001.md`

It preserves the Gate 154 distinction:

- `outer_replicate_id` identifies M, the independent outer synthetic world.
- `assignment_role=RUN` identifies the single designated run within that outer world.
- `assignment_role=REPEATED_ASSIGNMENT` identifies the R assignment repetitions within that same world.
- The legacy `replicate` field remains the R index; `replicate=-1` is reserved for the designated RUN and is disambiguated by the explicit role.
- A world seed is shared by RUN and all R assignments within one M, and differs across M.

No N/R/M numeric design values, MCSE targets, recovery thresholds, calibration stopping rules or confirmatory subsets are approved by this implementation.

## 2. Seed protocol implementation

File: `03_EXPERIMENTS/C10-S/harness/vcont_benchmark_protocol.py`

Implemented:

1. `SeedAssignment.outer_replicate_id` and `assignment_role`.
2. Seed derivation schema v3, domain-separated by bank, scenario/version, N, M identity, assignment role, R index and stream.
3. `build_seed_bank(..., outer_replicates=M)` creates one RUN row and R repeated-assignment rows for each outer world.
4. World seeds vary across M and remain fixed within each M.
5. `validate_seed_banks` checks role validity, designated RUN cardinality, duplicate R identities, within-world seed consistency, distinct world seeds across M and calibration/evaluation bank separation.
6. `seed_bank_fingerprint` includes outer identity and assignment role.

The default `outer_replicates=1` preserves a non-confirmatory compatibility path for existing callers; it does not satisfy the M>=2 requirement of Monte Carlo aggregation. The seed-bank function has not been used to materialize a calibration or evaluation bank.

## 3. Identity propagation through the harness

File: `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py`

The following objects now carry the outer identity and assignment role:

- `ScenarioConfig`
- `RunManifest`
- `TruthBundle`
- `AnalyzerResult`
- sealed evidence provenance and manifest envelope
- `PairEvaluationRecord`

Generator world identity incorporates the outer-replicate identity and world seed, but not the assignment role, so RUN and R records in one M resolve to the same world. Run identity incorporates role and assignment seeds, so separate assignments remain distinct.

Analyzer output integrity hashes include the propagated outer identity and role. Evaluator verifies consistency among manifest, truth, Analyzer result and sealed provenance; altered or cross-world identities fail closed.

## 4. Two-stage aggregation

The Evaluator now exposes:

`evaluate_monte_carlo(outer_runs, tolerance, target_mcse_by_metric=...)`

Input structure: a mapping from each outer-replicate identity to its runs.

For each M, the Evaluator requires exactly one designated RUN, verifies a single shared world identity and world seed across its R assignments, and rejects world identity or seed reuse across M. Scenario/version and N cannot be pooled.

Aggregation order:

1. Evaluate the designated RUN for run-conditional ITT-Z and ITT-G at that M.
2. Aggregate the R assignment records within that same M for mechanism-marginal and reference-regime targets.
3. Aggregate one metric contribution per M across independent outer worlds.

The current M summary reports, where the matrix class is EVALUABLE:

- Bias across outer-world errors.
- MAE across outer-world absolute errors.
- RMSE from outer-world squared-error contributions, with first-order delta-method MCSE.
- Recovery and identification rates with their Monte Carlo uncertainty.
- Explicit numeric coverage counts and per-world records.

Reference-regime RUN remains status-only; its numerical recovery is available only through the within-world R aggregate when identified and truth-comparable. STATUS_ONLY and NOT_IDENTIFIABLE pairs do not receive numeric error metrics. Missing contributions prevent a complete numeric M summary rather than being silently dropped.

MCSE targets are supplied by the caller and must match exactly the numeric EVALUABLE metrics selected by the authoritative scenario–estimand matrix. No target is inferred from a software default.

## 5. Tests added

- Outer M seed-bank generation: independent world seeds, one RUN per world, R assignments sharing that world.
- Seed fingerprint sensitivity to outer identity and assignment role.
- Monte Carlo aggregation: exact M coverage and unique outer identities.
- RMSE aggregation and delta-method precision.
- Generator-to-Evaluator identity propagation and cross-identity rejection.
- Evaluator M aggregation with RUN and R within each independent world.
- Rejection of reused world seeds across distinct outer identities.
- Matrix adapter retention of outer identity and assignment role.

## 6. Verification and execution boundary

**Successful technical verification:**
- Tested commit: `3159ab10566e61eff97cb6d0a10bfc3801a6291b`
- Workflow run: `43490700407`
- Result: compilation PASS; primary suite 94/94 PASS; clean source-archive replay 94/94 PASS.
- Artifact: `14069950102` (SHA-256 `cc70b24cbf7774a6b58a51ca42de4b6ecea60c721e98cd698bf495f78e8e6b6a`).

Technical verification is performed by the existing `c10-s-focal-harness-tests.yml` workflow: Python compilation, the full harness contract suite, and clean source-archive replay. The current implementation must not be marked technically verified until a successful run tests the exact final implementation commit.

This workflow exercises deterministic unit/contract fixtures. It does not generate calibration or evaluation seed banks, run Monte Carlo sizing, run the benchmark, or conduct scientific execution.

## 7. Remaining limitations

- M is now represented in seed planning and Evaluator aggregation, but no numerical M has been selected.
- N/R/M design sufficiency and calibration uncertainty remain governed by Gates 149–152 and remain open for numerical approval.
- The implementation is a benchmark harness capability, not evidence for the empirical causal contribution of accessibility to Value.
- No C10 claim, estimand, DGP truth, identification rule, or matrix classification is changed.
- `scientific_execution=false`; `execution_authorized=false`; `main` unchanged; PR #116 remains Draft.

## 8. Gate 155 status

**IMPLEMENTED — TECHNICALLY VERIFIED** at the exact commit and workflow run recorded in §6.

No calibration, seed-bank generation, Monte Carlo sizing, benchmark execution or scientific execution has been performed.
