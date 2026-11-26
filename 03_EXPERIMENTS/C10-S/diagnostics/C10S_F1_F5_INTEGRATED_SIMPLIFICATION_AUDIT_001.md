# C10-S — F1/F5 integrated instrumental simplification audit 001

**Status:** RESEARCH AUDIT — HISTORICAL RECONCILIATION COMPLETE / METHOD SELECTION OPEN / NO CODE CHANGE / NO NUMERICAL EXECUTION AUTHORIZED  
**Date:** 2026-11-26  
**Research branch:** `research/c10s-f1-f5-integrated-simplification-audit-20261126`  
**Canonical governance baseline:** GitHub `main`, RMA v3.38, Evidence→Claim Matrix v1.47, STATUS 2026-11-06  
**Scope:** simplify the statistical/inferential instrumentation needed to pass C10-S Tier-A and Tier-B; this is not C10 causal evidence.

## 1. Executive conclusion

The historical record supports the user's concern: the instrumental line accumulated substantial mathematical and numerical complexity without a corresponding improvement in the full Tier-A acceptance outcome.

The evidence does **not** support the stronger claim that every earlier method was close to passing, or that returning wholesale to the original bootstrap would solve the problem. The original percentile bootstrap had serious component-specific failures. However, the record contains a much simpler successful result for one important component: the exact Gaussian F1 within-variance pivot passed all six declared F1 cells in the independent comparative holdout (94.9–95.5% coverage, all Wilson intervals containing 95%, 100% emission). Conversely, the conservative F1 raw-between joint-pivot interval overcovers, and the F5 fitted beta-binomial percentile procedure fails in both M/R designs.

The most important distinction is:

- **F1 within:** a simple exact model-specific method already works in its declared Gaussian fixture family.
- **F1 raw-between:** the existing joint-pivot projection is valid but too conservative for the frozen [93%,97%] performance band; an existing profile-likelihood candidate is the next method to inspect, not a new method to invent.
- **F5 within/raw-between:** the fitted beta-binomial percentile interval has a real coverage problem. Exact global-MLE certification improves the fit's provenance/classification but does not repair the interval's repeated-sampling coverage.
- **F5 MCSE:** the existing profile-likelihood work addresses the MCSE functional, not the failed within/raw-between intervals. It must not be presented as a solution to those failures.
- **Tier-B and causal C10-S:** neither is authorized by the current results. G7 Tier-A is NOT_VALIDATED.

**Recommendation:** stop adding mathematical machinery to the production path for now. Preserve the existing work, use the simplest method already supported by evidence for F1 within, review the already-implemented F1 profile candidate for raw-between, and conduct a narrowly targeted diagnosis of the F5 interval construction using the existing exact beta-binomial oracle. Only after selecting and freezing a minimal candidate should a fresh independent Tier-A holdout be considered.

No protocol, threshold, estimator, source code, seed schedule, authorization, Tier-B status or C10 scientific execution status is changed by this audit.

## 2. Scope and historical evidence base

This audit reuses existing records; it does not rerun datasets, bootstraps, optimizers or workflows.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Original nested M/R Tier-A v002 investigation, run 44449787220 | Frozen percentile-bootstrap component results; point estimates broadly close to fixture truth in inspected cells; exact F1 within pivot and conservative F1 between benchmark | A validated full-family method |
| F1 exact/pivotal candidate and integrated validation | Formula implementation and deterministic software contracts; exact Gaussian within pivot's bounded coverage evidence | General validity outside balanced Gaussian F1 |
| F1/F5 comparative holdout and post-holdout diagnosis | Matched C0/C1/C5 comparisons, component-specific coverage and emission; C1 within passes six F1 cells | A validated raw-between method or general F5 method |
| F5 B2/B3 development calibration and coordinated diagnosis | 5,000 calibration + 5,000 disjoint development-validation datasets per F5 cell; optimizer and concentration diagnostics; B=1,000 vs 4,000 endpoint sensitivity | Confirmatory evidence or a validated C5 interval |
| F5 G7 Tier-A v1.1, original run 45750949936 and readjudication 45806714156 | 250/250 primary and 250/250 replay shards preserved and exactly matched; frozen four-component scientific adjudication | Tier-A pass, Tier-B authorization or C10 causal evidence |

The historical Tier-A v002 protocol remains frozen. Its eight-cell core is six Gaussian F1 cells (balanced/high-between/low-between × M10/R5 and M30/R20) plus two beta-binomial F5 cells (M10/R5 and M30/R20). The original K=1,000 and B=1,000 bank is development evidence, not an independent holdout after unblinding.

## 3. What happened as complexity increased

### 3.1 Original percentile bootstrap (C0 baseline)

Original Tier-A coverage:

| Cell | Within | Raw-between | MCSE availability |
|---|---:|---:|---:|
| F1 balanced M10/R5 | 84.0% | 93.8% | 24.4% |
| F1 balanced M30/R20 | 94.9% | 90.7% | 100.0% |
| F1 high-between M10/R5 | 84.3% | 80.1% | 91.6% |
| F1 high-between M30/R20 | 93.8% | 86.5% | 100.0% |
| F1 low-between M10/R5 | 79.9% | 98.2% | 0.0% |
| F1 low-between M30/R20 | 95.5% | 87.8% | 57.8% |
| F5 beta22 M10/R5 | 94.2% | 98.7% | 1.7% |
| F5 beta22 M30/R20 | 91.8% | 95.4% | 99.7% |

Within passed 4/8 components and raw-between 2/8; only one cell met the original MCSE availability and coverage/Wilson conditions. The bootstrap was not uniformly too narrow: some cells overcovered while others undercovered. A global width multiplier is therefore not defensible.

The point-estimator diagnostics in the original investigation were generally close to analytical truth in inspected examples. This supports investigating interval construction separately from point estimation, but does not establish point-estimator validity outside those fixtures.

### 3.2 F1: simple within method succeeds; between method remains unresolved

Under the balanced Gaussian random-intercept F1 model, the within residual sum of squares has an exact chi-square pivot. Its exact 95% interval produced:

| F1 cell | Percentile bootstrap | Exact chi-square pivot |
|---|---:|---:|
| Balanced M10/R5 | 84.0% | 95.6% |
| Balanced M30/R20 | 94.9% | 94.6% |
| High-between M10/R5 | 84.3% | 95.4% |
| High-between M30/R20 | 93.8% | 95.4% |
| Low-between M10/R5 | 79.9% | 94.6% |
| Low-between M30/R20 | 95.5% | 94.6% |

The later independent comparative holdout reports that C1 within passes all six F1 cells: 94.9–95.5% coverage, all Wilson intervals contain 95%, and 100% interval emission. This is the strongest simple-method success in the record. It is model-specific to the declared balanced Gaussian random-intercept fixture and must not be generalized to F5 or arbitrary C10-S contributions.

For raw-between, the C1 conservative joint-pivot projection produced 96.7–99.4% in the comparative holdout; all Wilson intervals lay above 95%. The earlier development benchmark gave 97.0–99.6%. This method is deliberately conservative and does not meet the frozen upper coverage bound. It is a useful reference/guard, not the preferred production candidate.

An F1 profile-likelihood implementation already exists for the exact raw-between estimand σ²_between = τ² − σ²_within/R, with explicit zero-boundary handling and caller-supplied likelihood-ratio cutoff. It is implemented but has not been executed or calibrated. Its immediate next step is a static mathematical/code review and independent score-equation reconciliation—not another implementation. The cutoff must be calibrated prospectively on development data and frozen before an independent holdout.

### 3.3 F5: beta-binomial percentile intervals fail in opposite directions

The C5 v1.0 B2 calibration/validation results (each bank K=5,000 per F5 cell) show:

| Cell / bank | Target | Coverage | Emission | Gate |
|---|---|---:|---:|---|
| M10/R5 calibration | within | 97.74% | 98.22% | FAIL |
| M10/R5 calibration | raw-between | 98.33% | 98.22% | FAIL |
| M10/R5 validation | within | 98.02% | 98.10% | FAIL |
| M10/R5 validation | raw-between | 98.70% | 98.10% | FAIL |
| M30/R20 calibration | within | 94.04% | 100% | FAIL |
| M30/R20 calibration | raw-between | 93.08% | 100% | FAIL |
| M30/R20 validation | within | 93.96% | 100% | FAIL |
| M30/R20 validation | raw-between | 93.00% | 100% | FAIL |

C0 also failed the frozen full-family component gates. It is a comparator, not a fallback acceptance route.

The coordinated B2/B3 diagnostic separates two different F5 patterns:

- **M10/R5:** a near-binomial/high-concentration weak-identification ridge appears in the fitted concentration tail, with substantial production-fit/analytic-fit divergence in a subset. This is a mixture of possible likelihood ambiguity and numerical/optimizer path issues; not every failed optimizer flag is equivalent to a different likelihood solution.
- **M30/R20:** the large unresolved BFGS count is often a precision-loss termination flag despite extremely close objective values and parameter agreement. Separately, a high-fitted-concentration tail has severe C5 conditional undercoverage. This is not the same near-flat binomial-limit ridge as M10/R5.

The B3 comparison from B=1,000 to B=4,000 shows modest endpoint shifts on selected datasets. Increasing B again is not a justified next step: it does not recover uncertainty in fitted α/β and does not repair the plug-in distributional approximation.

The static review of C5 identifies a structural limitation: its parametric bootstrap generates worlds from one fitted (α,β) pair but does not refit those parameters inside each bootstrap replicate. This conditions on the original fitted concentration and does not reproduce the repeated-sampling distribution of the concentration estimator. This is a plausible contributor to undercoverage, especially in the high-κ M30/R20 stratum, but the available exploratory stratification does not prove it is the sole cause.

### 3.4 What G7's exact certificate did—and did not do

G7 v1.1 moved exact global-MLE certification ahead of floating-point optimizer diagnostics. That is a meaningful correction to fit classification/provenance: the exact certificate now decides whether a global interior maximum or a boundary/unresolved state has been established; the numerical optimizers are diagnostics and cannot override it.

However, this complexity addresses **which fitted likelihood solution is admissible**, not whether the resulting percentile interval has correct repeated-sampling coverage. G7 confirms the distinction:

| G7 v1.1 cell | Target | Conditional coverage | Wilson 95% interval | Emission | Result |
|---|---|---:|---:|---:|---|
| M10/R5 | within | 98.644% | [97.645%, 99.223%] | 88.5% | FAIL |
| M10/R5 | raw-between | 99.661% | [99.008%, 99.885%] | 88.5% | FAIL |
| M30/R20 | within | 94.260% | [92.635%, 95.543%] | 99.3% | PASS |
| M30/R20 | raw-between | 93.353% | [91.631%, 94.742%] | 99.3% | FAIL |

M10/R5 had 115/1,000 abstentions: 18 certificate-unavailable and 97 certified global-boundary supremum cases. M30/R20 had seven certificate-unavailable abstentions. Overall: one of four components passes; G7 is `NOT_VALIDATED`, with primary/replay exact match.

This is the clearest evidence that adding exact certification did not solve the acceptance problem. It improved the integrity of the fit decision, but the interval coverage and emission gates remain unmet. It should therefore be retained as a diagnostic/provenance capability only if its cost is justified by the scientific role; it must not be mistaken for an interval-calibration solution.

## 4. Complexity inventory and keep/drop decision

| Instrumental element | Existing evidence/status | Recommendation |
|---|---|---|
| C0 two-stage percentile bootstrap | Frozen comparator; fails full Tier-A component gates | Keep as baseline comparator, not production default |
| F1 exact chi-square within pivot | Independent coverage passes all six declared Gaussian cells | Keep as minimal F1 within method within its model scope |
| F1 conservative joint-pivot raw-between | Implemented; systematic overcoverage above frozen upper band | Keep as conservative benchmark/guard; do not make it the sole production method |
| F1 raw-between profile likelihood | Implemented; unexecuted/uncalibrated; caller cutoff required | Review and test this existing candidate before creating anything new |
| F5 C5 fitted beta-binomial plug-in percentile bootstrap | B2/B3 and G7 fail coverage; M10/R5 weak-identification/emission problem; M30/R20 high-κ conditional miscalibration | Retain only as comparator; freeze further feature growth |
| F5 exact global-MLE certificate v1.1 | G7 fit classification/provenance; 115 + 7 certificate/boundary abstentions; no coverage cure | Do not expand certificate complexity until a targeted comparison proves it is necessary for the chosen inferential method |
| F5 beta-binomial exact finite-R oracle | Existing independent PMF/moment/covariance oracle | Reuse as primary truth/diagnostic oracle; no new oracle needed |
| F5 MCSE profile likelihood | Evaluator/design for MCSE functional only; not calibrated | Keep separate; do not conflate with within/raw-between coverage |
| Larger bootstrap B | B3 B=1,000 vs 4,000 changes modest | Do not increase B as a reflex |
| Additional F2/F3/F4-named method layers | No distinct F2/F3/F4 method artifacts were found in the scoped C10-S F1/F5 research tree inspected for this audit | Do not invent a taxonomy or reconstruct presumed stages; reconcile exact intended labels if they are used elsewhere |

## 5. Minimal scientifically defensible route to Tier-A

### Workstream 1 — F1 (bounded Gaussian family)

1. Retain the exact chi-square within interval as the default F1 within procedure for the declared balanced Gaussian random-intercept family.
2. Keep the joint-pivot raw-between interval as a conservative reference and boundary diagnostic.
3. Review the existing raw-between profile-likelihood implementation: estimand, zero boundary, nuisance optimization, bracket/root inversion, independent score-equation agreement, numerical failure semantics.
4. Use the existing development evidence—not the unblinded holdout—to specify a prospectively calibrated LR cutoff. Do not select a cutoff from the holdout or assume a Wilks cutoff.
5. Compare coverage, Wilson interval, interval width, directional misses, emission and runtime against C0 and C1 on a fresh independent holdout.

### Workstream 2 — F5 (beta-binomial family)

1. Freeze further expansion of the exact-certificate-first production path pending a decision on whether the selected interval method actually needs a certified global MLE.
2. Reconcile the production fit and analytic-gradient fit on existing B2 records. Separate: (a) termination flag, (b) objective/parameter concordance, (c) genuine ridge/boundary ambiguity, and (d) inadmissible fit. Do not retrospectively change B2/G7 adjudications.
3. Reuse the independent finite-R beta-binomial PMF/moment/covariance oracle to check fitted parameter and variance-component behaviour.
4. Design one small, disjoint development comparison of only the materially different interval constructions:
   - existing fixed-parameter plug-in percentile bootstrap (C5 baseline);
   - parametric bootstrap that refits α/β in every replicate, with explicit boundary/non-identification handling;
   - a likelihood/profile interval for the actual within and raw-between functionals, only if the existing likelihood implementation can support them without creating a separate oversized framework.
5. Predefine all estimands, boundaries, abstention states, numerical convergence rules, endpoint Monte Carlo error, computational budget and metrics. Do not choose the winner by aggregate coverage or pooled cells.
6. Do not build or tune the separate F5 MCSE profile as a supposed repair for within/raw-between. Keep MCSE as its own method/gate.

The purpose of this development comparison is to identify the minimum valid interval construction—not to build an all-purpose exact algebraic solver. If the simplest refitted parametric bootstrap passes the required component gates with stable estimation and honest boundary handling, there is no reason to retain a more elaborate profile/certificate apparatus in the production path solely for mathematical prestige. If it does not, the evidence should identify the exact limitation that justifies the next increment of complexity.

### Workstream 3 — one clean confirmatory Tier-A

After the F1/F5 candidates are selected on development evidence:

- freeze one method per family/component and its exact domain of applicability;
- retain the existing eight-cell Tier-A comparability core and the frozen component-wise acceptance rules unless a prospective, explicit protocol decision justifies a scientifically necessary change;
- generate a fresh independent seed namespace and fresh datasets; do not reuse the original v002 bank, B2/B3, comparative holdout or G7 data as confirmatory evidence;
- justify K/B and endpoint Monte Carlo error before execution;
- run Tier-A once under a new explicit authorization; audit integrity and adjudicate each component separately.

Tier-A acceptance remains component-wise: coverage [0.93,0.97], two-sided 95% Wilson interval containing 0.95, interval emission >=0.95, exact accounting, finite ordered endpoints, correct raw-between handling and no unresolved numerical state. No pooling or averaging to rescue a failed cell.

## 6. Tier-B and C10-S: preserve the actual objective

Tier-B remains the existing 20 stochastic diagnostic cells (K=500, B=500) plus deterministic guards, to be run only after Tier-A passes and after its own explicit authorization. Tier-B should test the predeclared robustness envelope; it must not become an unlimited search for every conceivable mathematical edge case.

After Tier-A and Tier-B pass, the project can proceed to the authorized C10-S causal execution path. Instrumental calibration is a prerequisite for trustworthy analysis, not the scientific objective. The objective remains to test whether the design/analyzer recovers, limits or refutes the causal accessibility contribution to contextual Value, distinguishing total assignment/package effects, accessibility-mediated effects and alternative/direct paths.

Neither a Tier-A pass nor a Tier-B pass establishes ΔT_acc → Value. They establish only that the specified instrument is sufficiently calibrated for the declared synthetic design.

## 7. Recommended immediate next operation

**Do not run another calibration now. Do not implement another estimator now.**

The next operation should be a bounded static reconciliation of the two already-existing candidates that have the strongest chance of reducing the work:

1. F1 raw-between: review the existing profile-likelihood implementation and independent score equation; report any mathematical or numerical defect and the minimum deterministic tests required.
2. F5: reconcile production versus analytic-gradient fits in the existing B2 records and inspect the existing beta-binomial likelihood/oracle; specify the smallest development comparison that discriminates fixed-parameter plug-in bootstrap from refitted bootstrap and/or component profile intervals.

Deliver one decision table: method, target, evidence, unresolved issue, minimum next test, and whether it is required for Tier-A. No code change or numerical execution in this operation.

This is narrower than another general F1/F5 architecture or a new MCSE/certificate subsystem. If these static checks show that an existing candidate is already sufficient, reuse it. If they reveal a real gap, specify only that gap.

## 8. Explicit boundaries and non-claims

- This audit does not change frozen v002, B2/B3, comparative holdout or G7 records.
- It does not retroactively convert any FAIL to PASS.
- It does not authorize Tier-B, C10 scientific execution or any new numerical calibration.
- It does not establish a general-purpose F1/F5 estimator outside the stated DGP families.
- It does not establish the causal contribution ΔT_acc → Value.
- It does not modify main, RMA v3.38, Evidence→Claim Matrix v1.47, STATUS, TGCV Core, or any canonical claim status.
- The separate PR #126 remains Draft and targets a fix branch; it is not part of this audit branch and must not be merged as an implicit promotion of research work.

## 9. Sources and provenance

Historical records consulted:

- `03_EXPERIMENTS/C10-S/diagnostics/C10S_NESTED_MR_TIER_A_CALIBRATION_INVESTIGATION_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_COMPARATIVE_CALIBRATION_READINESS_AUDIT_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_TIER_A_POST_HOLDOUT_METHOD_DIAGNOSIS_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_RESULT_AUDIT_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_B2_B3_COORDINATED_DIAGNOSTIC_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_C5_HIGH_CONCENTRATION_PLUGIN_COVERAGE_DIAGNOSTIC_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_FITTED_BETA_BINOMIAL_STATIC_REVIEW_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F1_EXACT_PIVOTAL_CANDIDATE_SPEC_001.md`
- `03_EXPERIMENTS/C10-S/diagnostics/C10S_F1_BETWEEN_PROFILE_LIKELIHOOD_IMPLEMENTATION_NOTE_001.md`
- `03_EXPERIMENTS/C10-S/harness/C10S_F1_INTEGRATED_VALIDATION_RESULT_003.md`
- `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_RESULT_003.md`
- `03_EXPERIMENTS/C10-S/design/C10S_F5_G7_TIERA_PROSPECTIVE_PROTOCOL_002.md`
- `03_EXPERIMENTS/C10-S/harness/C10S_F5_G7_TIERA_READJUDICATION_RESULT_001.md` (research/fix branch readjudication record; not canonical main)
- `00_GOVERNANCE/SIP/C10_S_EXECUTABLE_EXPERIMENT_MISSION_AND_NO_DRIFT_CONTRACT_001.md`

Governance baseline recovered from main: `00_GOVERNANCE/README.md`, `CHATGPT_BOOTSTRAP.md`, `CANONICAL_STATE.json`, `STATUS.md`, RMA v3.38, Matrix v1.47, traceability v3.38, governance operating principles v0.1 and scientific asset registry v0.1.
