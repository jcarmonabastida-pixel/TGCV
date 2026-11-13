# C10-S V_cont — Calibration and Seed-Bank Protocol

**Status:** IMPLEMENTED PROTOCOL SCAFFOLD — NUMERIC PRECISION TARGETS OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** Phase A synthetic V_cont benchmark only  
**Scientific execution:** NOT AUTHORIZED

## 1. Purpose and boundary

This protocol defines how calibration outputs may select candidate sample size N and assignment-replicate count R before an independent evaluation bank is opened.

It does not change the C1 estimands, DGP scenario definitions, Analyzer identification rules, or the distinction between ITT-Z, ITT-G and theta_A. It does not establish real-world causal identification or the TGCV `ΔT_acc → ΔValue` claim.

## 2. Two disjoint banks

### Calibration bank

Used only to:
- estimate scenario- and estimand-specific dispersion at candidate N values;
- calculate the calibration SD used for R dimensioning;
- select the smallest candidate N meeting all predeclared Monte Carlo precision targets;
- identify numerical instability and feasibility constraints.

### Evaluation bank

Used only after N, R, estimands, metrics and acceptance rules are frozen. It must not be used to tune N, R, tolerances, scenarios or analysis choices.

The banks use deterministic, domain-separated seed derivation with distinct bank labels. Within each scenario/N:
- the world seed is fixed across assignment replicates;
- Z assignment seeds vary by replicate;
- G assignment seeds vary independently by replicate;
- world, Z and G streams are distinct within each run;
- calibration and evaluation seed sets must be disjoint.

The implementation is in `vcont_benchmark_protocol.py`: `build_seed_bank` and `validate_seed_banks`.

## 3. Candidate N selection

The N grid is an explicit protocol input, not silently inferred from the harness default. Each candidate must satisfy the Generator constraints (N >= 16 and divisible by four).

For every candidate N, calibration must report precision separately for each predeclared scenario and estimand. The selection rule is the smallest N for which every required scenario-specific MCSE is no greater than its predeclared target:

`N* = min{N : MCSE_cal(s, e, N) <= target_MCSE(s, e) for every required (s,e)}`.

If no candidate qualifies, the result is `NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_MCSE_TARGETS`; no extrapolation beyond the tested grid is permitted without a protocol amendment.

Implementation: `select_minimum_n`.

## 4. Assignment replicate count R

For each selected scenario/N/estimand, calibration estimates the across-assignment-replicate SD, `SD_cal`. The minimum R is:

`R = max(2, ceil((SD_cal / target_MCSE)^2))`.

Implementation: `required_replicates`.

This formula controls Monte Carlo precision of the simulated mean estimate, not sampling uncertainty of a real-world causal estimand. If the calibration SD is estimated imprecisely, the protocol must conservatively account for that uncertainty before freezing R; a plug-in point estimate alone is not an automatic guarantee.

## 5. Required calibration outputs

For each scenario and estimand:
- number of calibration assignment replicates;
- fixed world identity and scenario/N configuration hash;
- SD across assignment replicates;
- resulting MCSE for the planned R;
- selected N and R, with the exact target used;
- counts of identified, not-identified and indeterminate Analyzer results;
- abstention and invalid-run counts;
- seed-bank fingerprint and code/configuration hashes.

Do not pool scenarios to conceal a scenario-specific precision failure. Do not discard abstentions from denominators; report rates and denominators explicitly.

## 6. Metrics and inference boundary

Continuous recovery metrics: bias, MAE, RMSE, SD and MCSE.  
Adjudication metrics: identification, non-identification, indeterminacy and abstention rates.

Coverage, type-I error and power remain `NOT_EVALUATED` unless an inferential procedure with valid per-replicate interval/test outputs has been separately specified and implemented. The current Analyzer standard errors do not establish those properties. Wilson intervals in the protocol module quantify Monte Carlo uncertainty in simulated binary rates; they are not confidence intervals for causal effects.

## 7. Numeric decisions deliberately left open

The following values cannot be responsibly inferred from software defaults or unit-test fixtures and must be explicitly approved before the calibration bank is run:

1. Candidate N grid.
2. Minimum scientifically relevant effect / precision scale for each primary estimand, or an independently justified absolute target MCSE.
3. Target MCSE by scenario and estimand.
4. Calibration replicate budget or adaptive stopping rule for estimating `SD_cal` with adequate precision.
5. The required scenario/estimand set for N and R selection.
6. Any scientific recovery tolerance. The existing test tolerance 0.10 is not promoted to a scientific criterion.

If a target is expressed relative to a minimum relevant effect `δ_min`, its ratio must also be approved explicitly; no ratio is assumed by this protocol.

## 8. Freeze and authorization sequence

1. Approve the numeric decisions in §7.
2. Freeze the N grid, targets, scenario/estimand set and calibration stopping rule.
3. Generate calibration bank only; persist its manifest and outputs.
4. Select N and R using the predeclared rules; record all failures and feasibility limits.
5. Freeze the evaluation-bank seed plan, N, R, metrics and acceptance criteria.
6. Conduct a separate authorization gate before generating the evaluation bank.

This document and its software are protocol preparation only. No calibration run, benchmark execution, or scientific execution is authorized by this record.


## 9. Gate 143–144 pair-keyed implementation alignment

The executable pair identity is (scenario_id, scenario_version, estimand_id, estimand_version). The protocol provides a 52-record coverage matrix for four V_cont assignment estimands across 13 benchmark scenarios, pair-specific summaries and R sizing, and a fail-closed pair-keyed N selector. Candidate N is eligible only when all predeclared coverage keys are present and every numeric EVALUABLE key has a finite MCSE within its own predeclared target. STATUS_ONLY and NOT_IDENTIFIABLE keys remain mandatory coverage records but do not receive numeric MCSE or recovery scoring. Numeric targets and the final required subset remain OPEN.

The legacy scenario-only selector is retained for historical result compatibility; it is not the conforming selector for new pair-keyed calibration. SeedAssignment now carries scenario_version, includes it in deterministic seed derivation and bank fingerprints, and groups fixed-world checks by scenario ID, scenario version and N. The default UNVERSIONED value is retained only for legacy callers; new governed banks must supply explicit scenario versions. No calibration or evaluation seed bank was generated by this source change.


## 10. Gates 149–152 — temporal aggregation and joint design contract (2026-11-13)

**Status:** DOCUMENTED DESIGN CONTRACT — IMPLEMENTATION GAP REMAINS OPEN  
**Execution:** no calibration, Monte Carlo, benchmark or scientific execution is authorized or recorded by this addendum.

This addendum reconciles the temporal aggregation gates with the existing pair-keyed matrix, Evaluator adapter and calibration/seed-bank scaffold. It does not change the four assignment estimands, the 52 required scenario–estimand coverage records, DGP truths, identification assumptions or numeric acceptance thresholds.

### 10.1 Gate 149 — aggregation identity and temporal levels

Every aggregation record is keyed by:

`K* = (scenario_id, scenario_version, estimand_id, estimand_version, temporal_level)`.

The supported temporal levels are:

- `RUN`: one generated dataset and one Analyzer/Evaluator run.
- `REPEATED_ASSIGNMENT`: aggregation over repeated joint Z×G assignments within one fixed generated synthetic world and one fixed scenario/DGP parameterization.
- `MONTE_CARLO`: aggregation over independent outer benchmark replications. This level is introduced by this design contract and is not yet implemented by the current harness.

The matrix remains authoritative for whether a pair is numerically scoreable or status-only at each level. The 52 scenario–estimand coverage obligations are retained; coverage does not imply that every pair has a numeric truth or estimate.

### 10.2 Gate 150 — metric-to-level mapping

| Estimand/pair class | RUN | REPEATED_ASSIGNMENT | MONTE_CARLO |
|---|---|---|---|
| ITT-Z run-conditional | Numeric error/recovery against run-conditional truth | Not a substitute for run-level truth | Aggregate distribution of run-level performance |
| ITT-Z mechanism-marginal | No numeric marginal recovery from one run | Numeric marginal recovery against mechanism-marginal truth | Aggregate performance across independent outer replications |
| ITT-Z reference-regime | Identification/status only; no comparison of a single run estimate to marginal reference truth | Numeric reference recovery only when identified and truth-comparable | Aggregate performance and identification rates |
| ITT-G, Z=0 | Numeric error/recovery against the declared run truth | Not applicable to the run-level assignment contrast unless a distinct repeated target is declared | Aggregate run-level performance |
| STATUS_ONLY / NOT_IDENTIFIABLE | Status adjudication | Status aggregation only if declared by the matrix | Status rates; never numeric error or recovery |

For all levels:
- report coverage counts and denominators;
- report bias, MAE, RMSE and recovery only for eligible numeric records;
- report identification, non-identification, indeterminacy, abstention and invalid-output rates with explicit denominators;
- do not count missing records as abstentions;
- do not coerce null or NOT_EVALUABLE to zero;
- do not pool scenario/version/estimand/temporal-level identities;
- preserve non-numeric pairs in coverage even when they are excluded from numeric summaries.

### 10.3 Gate 151 — hierarchy and meaning of N, R and M

The design hierarchy is:

`scenario/version/estimand → outer replicate m (1…M) → joint assignment r (1…R) → units i (1…N)`.

- `N`: units in each generated dataset/run. It governs within-run information and estimator precision.
- `R`: repeated joint Z×G assignments within the same fixed synthetic world. It governs precision of assignment-marginal aggregates, including mechanism-marginal and reference-regime targets where the matrix permits them.
- `M`: independent outer Monte Carlo replications of the benchmark procedure. Each outer replicate uses a newly generated synthetic world/sample under the same fixed scenario version and DGP parameterization; within each outer replicate, the world is held fixed across its R assignment repetitions. M quantifies uncertainty in benchmark performance summaries across independent outer replications.

The current seed scaffold fixes one world seed across assignment replicates within scenario/version/N. This is consistent with the R level but does not yet represent M independent outer replications. The implementation currently has no explicit outer-replicate identity/dimension. Consequently, MONTE_CARLO summaries across M are a specified requirement, not an implemented capability.

A draw of DGP parameters from a distribution is not silently folded into M. The present contract is conditional on the declared scenario version and fixed DGP parameterization. If a future target averages over parameter configurations, that requires an explicit world/parameter sampling distribution, target definition, versioned identity and separate analysis; it is not authorized by this addendum.

For a scalar benchmark metric `psi_m` computed once per independent outer replicate:

`MCSE(mean(psi)) = SD(psi_1,…,psi_M) / sqrt(M)`.

For a binary metric (e.g. recovery, identification or correct abstention), the Monte Carlo standard error of its estimated rate is:

`MCSE(p_hat) = sqrt(p_hat * (1-p_hat) / M)`.

A candidate M may be planned using `M >= ceil((SD_cal / target_MCSE)^2)`, or the corresponding conservative binary-rate bound, using a separate calibration source and predeclared target. Calibration and confirmatory evaluation seeds must be disjoint. The empirical plug-in SD is not an automatic precision guarantee; uncertainty in the calibration SD must be addressed conservatively before M is frozen.

**Important reconciliation with the existing implementation:** `required_replicates(calibration_sd, target_mcse)` currently sizes the assignment-replicate dimension R. It must not be reinterpreted as sizing M. A separate M-sizing rule and explicit outer-replicate identity are required before MONTE_CARLO summaries can be implemented.

### 10.4 Gate 152 — joint design specification and sufficiency states

Each design configuration is keyed by scenario/version, estimand/version and temporal level, and must declare:
- N, R and M values or an explicit `NOT_APPLICABLE` for dimensions not required by that estimand/level;
- precision targets and the metric/denominator to which each target applies;
- truth source, truth identity/version and comparability rule;
- assignment support and identification requirements;
- seed protocol and calibration/evaluation bank fingerprints;
- required coverage keys and any predeclared exclusions;
- design configuration identity/version and status.

Sufficiency is multidimensional and must not be collapsed into one unqualified PASS:

- `DESIGN_SUFFICIENT`: every applicable design dimension, truth/support prerequisite and precision target passes.
- `DESIGN_INSUFFICIENT_N`: within-run sample-size requirement fails.
- `DESIGN_INSUFFICIENT_R`: repeated-assignment precision requirement fails.
- `DESIGN_INSUFFICIENT_M`: outer Monte Carlo precision requirement fails.
- `DESIGN_SUPPORT_FAILURE`: the declared assignment support cannot identify the target under the approved contract.
- `DESIGN_TRUTH_MISMATCH`: truth and evaluated estimand/regime are not comparable.
- `DESIGN_SPECIFICATION_INCOMPLETE`: a required design parameter, target, provenance field or rule is absent.

Multiple failure reasons may coexist. `NOT_APPLICABLE` is not a precision PASS. Design sufficiency only permits the relevant evaluation; it does not guarantee Analyzer recovery or causal identification.

The order of design preparation is: freeze estimand/truth/support and target population; dimension N for within-run estimation; dimension R for repeated-assignment targets; dimension M for benchmark performance summaries; then validate full pair coverage and all design identities before opening the confirmatory evaluation bank.

The current code's pair-keyed N selector and R-sizing helper remain scaffolding. This addendum does not certify that their calibration inputs already implement all three dimensions or the full sufficiency state machine. In particular, no numerical N/R/M values, MCSE tolerances, recovery tolerances, required confirmatory subset or calibration stopping rule are approved here.

### 10.5 Implementation and verification obligations

Before the MONTE_CARLO level can be marked IMPLEMENTED, the harness must:
1. add an explicit outer-replicate identity to seed assignments, manifests, TruthBundle/outputs and aggregation keys;
2. generate independent world seeds across M while holding each world fixed across its within-world R assignment repetitions;
3. preserve disjoint calibration/evaluation banks across all world, Z and G seed streams;
4. compute one correctly defined metric contribution per outer replicate and aggregate only across independent M units;
5. keep R-level marginal-target recovery separate from M-level uncertainty in benchmark performance;
6. preserve the 52-pair coverage matrix and temporal-level eligibility rules;
7. reject duplicate, missing, cross-version, cross-world or non-independent replicate identities as specified;
8. expose separate N-, R- and M-sufficiency outcomes and retain all failure reasons;
9. test null/missing/invalid/status-only cases without denominator loss or numeric coercion.

Technical tests and CI may verify implementation conformance when separately authorized. Calibration, seed-bank generation, Monte Carlo sizing runs, benchmark execution and scientific execution remain outside this contract and require their own explicit authorization.

### 10.6 Gate status

- Gate 149: aggregation identity and temporal levels — DEFINED.
- Gate 150: metric-to-level mapping — DEFINED.
- Gate 151: N/R/M hierarchy and Monte Carlo precision — DEFINED; M implementation OPEN.
- Gate 152: joint design and sufficiency contract — DEFINED; numeric design choices OPEN.
- Existing calibration protocol scaffold: IMPLEMENTED as previously recorded; it does not yet implement M.
- This addendum: DOCUMENTARY PERSISTENCE ONLY; no code, tests, CI or scientific execution changed or ran.


## 11. Gate 154 — outer Monte Carlo replication contract

The explicit outer-replication identity, world-seed variation across M, designated RUN assignment, within-world R repeated assignments, stream roles, manifest provenance and two-stage aggregation contract are governed by:

`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_CONTRACT_DRAFT_001.md`.

This contract supersedes any ambiguous interpretation of the legacy `SeedAssignment.replicate`: that field represents assignment repetition R only and is not an outer Monte Carlo replicate. The current implementation remains without explicit M and must not be described as providing independent outer-world replication.

The existing `required_replicates(calibration_sd, target_mcse)` continues to size R only. M requires its own predeclared sizing and calibration-uncertainty procedure. No numerical M, new seed bank, calibration, Monte Carlo or scientific execution is authorized by this cross-reference.

**Gate 154 status:** DEFINED and cross-referenced; implementation OPEN.


## 12. Gate 155 — outer M implementation

**Implementation record:** `00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_IMPLEMENTATION_GATE_155_DRAFT_001.md`.

The seed-bank and harness implementation now carries `outer_replicate_id` and `assignment_role`, preserves one designated RUN and R repeated assignments within each outer world, derives distinct world seeds across M, and provides a two-stage Evaluator aggregation over within-world R followed by across-world M. Bias, MAE, RMSE (delta-method MCSE), recovery and identification metrics are aggregated only when the authoritative matrix marks the corresponding temporal pair EVALUABLE.

The legacy `replicate` remains the R assignment index; `replicate=-1` plus `assignment_role=RUN` denotes the designated run. Seed-bank fingerprints include M identity and role. The existing `required_replicates` continues to size R only; no numeric M sizing rule or target is inferred here.

**Gate 155:** IMPLEMENTED and TECHNICALLY VERIFIED — commit `3159ab10566e61eff97cb6d0a10bfc3801a6291b`, workflow run `43490700407` (compile PASS; primary 94/94 PASS; clean replay 94/94 PASS). Full implementation record: `C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_IMPLEMENTATION_GATE_155_DRAFT_001.md`. No calibration or evaluation seed bank was generated. No Monte Carlo sizing, benchmark or scientific execution is authorized or recorded.


## 13. Gate 156 — MONTE_CARLO matrix coverage and temporal manifest

**Status:** DEFINED / PERSISTED — IMPLEMENTATION OPEN.

The Gate 155 Evaluator currently aggregates the four estimand pairs for one scenario/version at a time. Gate 156 defines the remaining benchmark-level integration: compose the 13 scenario blocks into the authoritative 52-pair ledger, enforce declared M and R completeness, retain one per-M contribution for every pair at its matrix-authorized temporal level, adjudicate statuses and denominators against the matrix, and preserve reconstruction fingerprints.

Canonical contract:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_MATRIX_COVERAGE_CONTRACT_GATE_156_DRAFT_001.md`.

This is a contract/persistence update only. Gate 156 implementation is OPEN. No seed bank has been generated; no calibration, Monte Carlo sizing, benchmark or scientific execution has been performed or authorized. Numeric N/R/M and MCSE targets remain OPEN.


## 14. Gate 157 — implementation preflight

**Status:** PREFLIGHT COMPLETED / PERSISTED — CODE IMPLEMENTATION OPEN.

The Gate 157 preflight confirms that Gate 155's per-scenario M evaluator is reusable, but the full 52-pair benchmark aggregator, declared design object, pair-keyed metric targets, exact R completeness and reconstructable per-M ledger remain unimplemented. It also identifies a typed R-index propagation gap: `SeedAssignment.replicate` exists, but the runtime chain does not yet carry a dedicated assignment index through ScenarioConfig, RunManifest, TruthBundle and AnalyzerResult.

Canonical preflight record:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_GATE_157_IMPLEMENTATION_PREFLIGHT_DRAFT_001.md`.

No code/test change, seed-bank generation, calibration, Monte Carlo sizing, benchmark or scientific execution was performed in this preflight.
