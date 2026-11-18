# C10-S — Nested M/R Bootstrap Numerical Validation Protocol

**ID:** C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001  
**Version:** 002  
**Date:** 2026-11-18  
**Status:** FROZEN_FOR_NUMERICAL_METHOD_VALIDATION / NOT_EXECUTED / NO_EXECUTION_AUTHORIZATION  
**Parent specification:** `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, §§382–386  
**Scope:** numerical validation of the auxiliary nested M/R variance and MCSE bootstrap only.

## 1. Decision question and separation boundary

Determine whether the implemented hierarchical bootstrap recovers known within-world and between-world variance components, produces calibrated uncertainty intervals/projections in regular interior cases, and abstains correctly at boundaries, with insufficient support, or when required sampling contracts are absent.

This protocol does **not** test Analyzer causal recovery, the C10 estimand, `ΔT_acc → ΔV`, DGP scientific adequacy, Generator/Analyzer/Evaluator behaviour, or any confirmatory M/R target. Passing it can establish bounded numerical-method evidence only.

The validation uses scalar analytical fixtures that directly supply complete `q_mr` contributions. It must not invoke the C10 Generator, Analyzer, Evaluator, calibration protocol runner, seed-bank builder, or scientific workflows.

## 2. Frozen unit and assumptions to be tested

For each fixture dataset:
- M is the number of independently sampled outer worlds;
- R is the number of complete assignment-replicate contributions conditional on each fixed world;
- the bootstrap resamples complete M clusters, then complete R contributions inside each selected cluster;
- the outer and inner sampling contracts are separately declared and versioned;
- no missing contribution is dropped, imputed, or converted into a complete-case estimand.

The target components are:

`sigma²_within = E[Var(q_mr | m)]` and `sigma²_between = Var(E[q_mr | m])`.

For a balanced design, the analytical reference for the variance of the grand mean at target (M*,R*) is:

`V(M*,R*) = sigma²_between/M* + sigma²_within/(M*R*)`.

The raw between estimator remains untruncated. A negative raw estimate is a finite-sample boundary diagnostic, not a negative physical variance.

## 3. Fixture families and analytical oracles

### F1 — Gaussian interior, both components positive

`q_mr = mu + U_m + E_mr`, with independent `U_m ~ Normal(0, sigma²_between)` and `E_mr ~ Normal(0, sigma²_within)`.

Candidate parameter cells:
- balanced interior: `sigma²_between=1`, `sigma²_within=1`;
- low between signal: `sigma²_between=0.05`, `sigma²_within=1`;
- high between signal: `sigma²_between=2`, `sigma²_within=0.25`.

Oracle: exact component variances and exact `V(M*,R*)`. This is the primary regular-case coverage fixture.

### F2 — Between-component boundary and near-boundary

Use the same construction with:
- exact boundary: `sigma²_between=0`, `sigma²_within=1`;
- near boundary: `sigma²_between=0.01`, `sigma²_within=1`.

Oracle: raw between truth 0 or 0.01. Acceptance focuses on retaining the raw estimate, reporting boundary frequency, and suppressing numeric projections whenever bootstrap draws enter the forbidden negative-between region. No forced coverage pass is required for a regular percentile interval at the exact boundary.

### F3 — Within-component boundary

Set `sigma²_within=0` and `sigma²_between>0`.

Oracle: `MSW=0` without division by zero or NaN; between-component estimation and the algebraic reconciliation identity remain finite. Bootstrap degeneracy must be visible rather than hidden.

### F4 — Fully degenerate scalar contributions

Set both components to zero. All contributions are identical.

Oracle: finite point summaries, zero raw component estimates, explicit degeneracy, and no claim of regular inferential precision where the bootstrap distribution has no variation.

### F5 — Discrete Bernoulli contributions

Use:
- constant Bernoulli probability `p=0.5` for zero between / positive within;
- a beta-distributed world-specific probability with analytically known beta-binomial moments for positive between and within;
- degenerate `p=0` and `p=1` fixtures;
- rare-event probability `p=0.01` as a sparse indicator case.

Oracle: exact conditional and marginal moments. The method must preserve all-zero/all-one degeneracy and must not introduce continuity corrections or implicit parametric smoothing.

### F6 — RMSE/MSE scale and nonregularity

Supply squared errors `q_mr=e_mr²` directly:
- regular positive MSE;
- small positive MSE over a declared scale;
- exact zero MSE.

Oracle: variance decomposition on MSE contributions. The RMSE delta transformation is checked only in regular positive-MSE cells. Exact zero must return `RMSE_DELTA_NONREGULAR`. A numerical threshold for “near zero” is deliberately OPEN until a scale-aware rule is justified and frozen.

## 4. Support and design grid

The validation grid must include:
- outer support: M = 2, 3, 5, 10, 30;
- inner support: R = 2, 5, 20;
- at least one small-M/small-R cell, one moderate cell and one larger-support cell per applicable fixture family.

M=2 is a mandatory negative control: the implementation must return `INSUFFICIENT_OUTER_SUPPORT` and no numeric projection. M=3 and M=5 are diagnostic cells, not automatically accepted or rejected by a universal threshold. More bootstrap draws cannot compensate for too few distinct outer worlds.

The full Cartesian grid is not required if the computational burden is disproportionate. Any reduced grid must retain all six fixture families and all boundary conditions above, with the omitted cells and rationale recorded before execution.

## 5. Replication and bootstrap settings — candidate, not frozen

For a first numerical-validation wave, candidate settings are:
- nominal interval levels: 90% and 95%;
- bootstrap draws B: 2,000 per fixture dataset;
- independent fixture datasets K: 2,000 per regular parameter cell;
- deterministic, versioned seed schedule with separate namespaces for dataset generation and bootstrap resampling.

These are validation-study design candidates, not C10 confirmatory parameters or historical N/M/R recommendations. Before execution, conduct a resource estimate and freeze B, K, the reduced/full grid, seed schedule and software commit in a separate execution contract. If B/K or grid are changed, record the reason before inspecting coverage outcomes.

## 6. Adjudication criteria

### 6.1 Algebra and point-estimator invariants

Every fixture dataset must satisfy:
- the implemented MSW/MSB/raw-between formulas against independently calculated oracles;
- `s²(q̄_m) = between_raw + within_ms/R` within a predeclared floating-point tolerance;
- exact preservation of negative between estimates;
- unchanged reconciliation with the legacy observed MCSE for the observed R when outer IID is declared;
- deterministic output under a fixed seed and invariant results to a permutation of complete M rows (after restoring canonical identity order).

### 6.2 Coverage and calibration in regular interior cells

For each nominal interval level and each regular positive-component cell:
- report empirical coverage separately for within, between raw, and projected MCSE;
- report the binomial Monte Carlo standard error and a 95% Wilson interval for each coverage estimate;
- report interval width, bias, RMSE of component estimates, bootstrap-valid fraction and boundary-draw fraction.

Candidate acceptance rule: empirical coverage must lie within ±2 percentage points of nominal **and** the 95% Wilson interval must contain the nominal coverage. This is a method-validation tolerance, not a claim of universal nominal coverage. If the criterion fails in any cell, classify that cell as NOT_VALIDATED and investigate; do not average failures away across fixture families.

### 6.3 Boundary and degenerate cells

- F2 exact-zero between: retain raw estimates; record boundary frequency; numeric MCSE projection must abstain when any valid bootstrap draw has negative raw between.
- F2 near-zero between: report the full raw distribution and abstention frequency; do not claim regular coverage from a positive-only subset.
- F3 within zero: no NaN/Inf; zero within estimate is represented explicitly.
- F4 both zero: report degeneracy and no regular interval/projection claim.
- F5 p=0/1: preserve exact all-zero/all-one outcomes and abstain from unsupported regularity claims.
- F6 exact-zero MSE: `RMSE_DELTA_NONREGULAR`; no delta interval.
- F6 small positive MSE: report scale-specific behaviour; do not declare acceptance until the near-zero threshold and scale normalization are predeclared.

### 6.4 Support and contract abstention

- M=2: `INSUFFICIENT_OUTER_SUPPORT`, no numeric projection.
- Outer mode other than `DECLARED_IID_PSEUDORANDOM`: no inferential M projection.
- Within-R mode other than `DECLARED_IID_PSEUDORANDOM`, or missing contract identity/version/basis: no inferential R or M/R projection.
- Missing/unevaluable R contributions: metric NOT_EVALUABLE; no complete-case bootstrap.
- No R coupling contract: no paired within-R contrast.
- No N coupling contract: no paired N comparison.

### 6.5 Global disposition

A fixture family is:
- `PASS_BOUNDED_NUMERICAL_VALIDATION` only if every applicable criterion in that family passes;
- `CONDITIONAL` if regular cells pass but identified boundary/support cells correctly abstain and the limitations are explicit;
- `NOT_VALIDATED` if an applicable oracle, coverage or abstention criterion fails;
- `NOT_EVALUABLE` if the fixture does not supply the complete contract or denominator required by its estimand.

No global pass is awarded by averaging across families. The final report must show each cell and every abstention.

## 7. Required provenance and outputs

For every dataset and cell, retain:
- protocol ID/version and fixture family/parameter identity;
- code commit, method ID/version and dependency lock identity;
- outer/within sampling contract IDs, versions and independence bases;
- M, R, B, K, nominal level and all seeds/seed namespaces;
- analytical truth, estimated components, raw between, MCSE reconciliation and projection;
- interval endpoints, coverage indicator, widths, boundary/degeneracy diagnostics;
- counts of valid bootstrap draws and abstentions with exact reasons;
- run ID, runtime and SHA-256 manifest for all inputs and outputs.

Outputs must be separate from the C10 calibration/evaluation banks and must not be consumed as Analyzer performance evidence.

## 8. Execution boundary and next gate

**No execution is authorized by this draft.** It creates no fixture datasets, no DGP, no seed bank and no Monte Carlo run.

Before any numerical validation:
1. resolve the scale-aware near-zero RMSE rule or explicitly exclude that subcase from inferential acceptance;
2. freeze the full or reduced M/R grid and resource estimate;
3. freeze B, K, interval levels, seed schedule and coverage adjudication;
4. verify that the within-R contract is genuinely justified by the intended assignment mechanism, not merely by distinct seeds;
5. create a dedicated remote validation workflow with strict scope exclusions and artifact manifest;
6. obtain explicit authorization for this numerical-method validation, separately from static software tests and separately from C10 scientific execution.

**Current disposition:** protocol candidate ready for integrated review; NOT_FROZEN / NOT_EXECUTED. No causal or confirmatory claim follows.


## 9. Closure decisions and corrected bootstrap contract (version 002)

This section resolves the open design choices in version 001. It freezes the bounded numerical-method validation design, not the C10 confirmatory experiment and not the real C10 assignment mechanism.

### 9.1 Sampling contracts for the validation fixtures

Each synthetic fixture generator declares two distinct mechanisms:
- **Outer M:** independent draws from the fixture's explicitly defined world-generating distribution.
- **Inner R:** independent assignment-replicate draws conditional on the selected world, from the fixture's explicitly defined conditional distribution.

The fixture manifest records separate contract IDs, versions and independence bases for M and R. The implementation requires these fields whenever the corresponding mode is `DECLARED_IID_PSEUDORANDOM`. This is a test-fixture truth contract; it does not establish that the actual C10-S assignment mechanism satisfies conditional IID or that real C10 worlds are sampled from a target population. That remains a separate application-validity condition before using inferential M/R projections on C10-S outputs.

### 9.2 Bootstrap resampling law

The bootstrap retains every outer cluster draw, including a resample in which all selected source IDs happen to be the same. Such draws are valid draws from the ordinary cluster bootstrap law; dropping them conditions the bootstrap distribution on observed source-cluster diversity and changes that law.

Each selected cluster copy receives its own inner R resample. The implementation no longer discards all-same-source-ID draws. Consequently, `valid_bootstrap_replicates` must equal the requested B for valid balanced inputs; boundary or nonregular draws are retained and adjudicated, not removed from the bootstrap denominator.

The method version is now `TGCV_NESTED_MR_BOOTSTRAP` 1.2. The outer sampling contract is symmetric with the inner contract and requires:
- `outer_world_sampling_contract_id`;
- `outer_world_sampling_contract_version`;
- `outer_world_sampling_independence_basis`.

Missing identity/version/basis causes fail-closed rejection for a declared IID mode. A mode declaration alone is not a complete contract.

### 9.3 RMSE near zero

No universal numeric threshold for “near-zero MSE” is frozen. A threshold would depend on the scale and normalization of the underlying error metric, which are not common across the 16 metrics.

The numerical validation therefore:
- validates component estimation and bootstrap uncertainty on the **MSE contribution scale**;
- validates the exact-zero guard `RMSE_DELTA_NONREGULAR`;
- does not use RMSE delta-method interval coverage as an acceptance criterion;
- treats any positive-MSE delta projection as exploratory output only, not validated evidence, until a metric-specific scale/reference and nonregularity criterion are specified.

This closes the protocol without inventing a scale-free threshold.

### 9.4 Frozen validation grid and computational tiers

The full Cartesian product in version 001 is replaced by the following bounded design. All cells and seeds are generated by a deterministic, versioned schedule with separate namespaces for dataset generation and bootstrap resampling.

**Tier A — regular-cell coverage (primary numerical validation):**
- F1 Gaussian: three parameter cells from §3.
- F5 beta-binomial: `alpha=2, beta=2` for the world-specific probability, giving analytically known between and within components.
- Observed designs: `(M,R)=(10,5)` and `(30,20)` for each of the four parameter cells.
- Independent fixture datasets: `K=1,000` per cell.
- Hierarchical bootstrap draws: `B=1,000` per dataset.
- Nominal interval: 95% percentile interval only, matching the implemented method.
- Primary coverage targets: `sigma²_within` and `sigma²_between,raw`.
- Projected MCSE coverage is separately reported only where a numeric projection is emitted; its availability rate is reported and must be at least 95% before any conditional coverage result is described as calibrated. A conditional coverage percentage alone cannot pass the gate.

**Tier B — low-support and boundary diagnostics:**
- F1 balanced and low-between cells; F2 exact-zero and near-zero between cells; F3 within-zero; F4 fully degenerate; F5 `p=0.5`, `p=0.01`, `p=0`, `p=1`; F6 positive and exact-zero MSE.
- Diagnostic designs: `(M,R)=(3,2)` and `(10,5)`; the support negative control is `(2,2)`.
- `K=500`, `B=500` per stochastic diagnostic cell. Deterministic degeneracy and exact-zero guards additionally receive direct invariant tests.
- These cells assess raw-component preservation, boundary/degeneracy visibility, finite arithmetic and correct abstention. They do not receive a universal nominal-coverage acceptance criterion.

No 90% interval is evaluated because the current implementation emits 95% component intervals. No post hoc addition of cells, seeds, K, B or acceptance tolerances is allowed after inspecting outcomes. Any change requires a versioned protocol amendment before rerunning the affected tier.

### 9.5 Coverage adjudication and Monte Carlo uncertainty

For each Tier A cell and each primary component:
- empirical coverage is computed across the K independent fixture datasets;
- its Monte Carlo standard error is `sqrt(p_hat*(1-p_hat)/K)`;
- a 95% Wilson interval is reported;
- bias, RMSE, median error, interval width and finite/abstention counts are reported separately.

A component cell passes only if empirical 95% coverage lies in `[0.93, 0.97]` **and** its 95% Wilson interval contains 0.95. Cells are adjudicated individually; no averaging across cells or components can rescue a failed cell.

For projected MCSE, report both availability and coverage among emitted intervals. If availability is below 95%, the cell is `CONDITIONAL / NOT_CALIBRATED`, regardless of conditional coverage. If availability is at least 95%, the same coverage/Wilson criterion applies. This does not license extrapolation to boundary cells or actual C10-S sampling contracts.

### 9.6 Explicit scope exclusions

This protocol validates only the scalar, balanced, unpaired nested M/R estimator and bootstrap. It does **not** validate:
- paired A−B contrasts, paired R resampling, or cross-scenario covariance;
- comparisons or coupling across N;
- unbalanced or informative R designs;
- missing/unevaluable contributions or random denominators;
- the truth of the actual C10-S M/R sampling contracts;
- causal recovery, Analyzer performance, DGP adequacy or any Value claim.

The implementation must abstain from treating row order, equal indices, `world_family_id`, or coincident seeds as evidence of pairing. A separate design and implementation gate is required for paired contrasts or N coupling.

## 10. Frozen execution manifest requirements

Before numerical execution, a separate execution contract must bind:
- this protocol ID and version 002;
- exact code commit and method version 1.2;
- deterministic fixture-generator version and source hash;
- the complete Tier A/Tier B cell manifest;
- seed-schedule version and seed namespaces;
- K, B and interval definition for every cell;
- runtime/dependency lock and resource limits;
- output schema, run ID and SHA-256 manifest;
- a predeclared rule that any infrastructure interruption restarts only the incomplete cell with the same frozen seeds, never silently changes K/B or seeds.

No scientific Generator, Analyzer, Evaluator, calibration bank, seed bank or C10 workflow is in scope. This numerical-method run is a separate, bounded software/statistical validation.

## 11. Final protocol disposition

**DESIGN CLOSED FOR THE SPECIFIED NUMERICAL VALIDATION. NOT EXECUTED.**

Version 002 resolves the bootstrap law, outer and inner sampling-contract completeness, RMSE-near-zero scope, finite validation grid, replication counts, coverage adjudication and scope exclusions. The actual C10-S assignment mechanism and outer-world sampling validity remain application-specific conditions and are not assumed by this protocol.

The next operation is to create and review the exact fixture-generator and remote numerical-validation execution contract, including a resource estimate. That contract must be reviewed before the separate numerical-method execution is authorized. This protocol itself grants no execution authorization.
