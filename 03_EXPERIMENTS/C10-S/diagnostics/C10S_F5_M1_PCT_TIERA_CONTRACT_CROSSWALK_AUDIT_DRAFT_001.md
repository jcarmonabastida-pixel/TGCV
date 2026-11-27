# C10-S — M1-PCT to F5 Tier-A contract crosswalk audit

**Status:** DRAFT — STATIC RECONCILIATION ONLY  
**Branch:** research/c10s-coverage-first-focus-20261127  
**Scope:** M1-PCT / F5 Raw-between / existing comparative Tier-A adjudication  
**Execution:** NONE — no tests, benchmarks, calibration, holdout or simulation executed  
**Authorization:** This record does not authorize scientific execution or amend a frozen protocol.

## 1. Finding

M1-PCT's population functional is mathematically aligned with the F5 beta-binomial Raw-between target, but M1-PCT is **not currently integrated into, nor adjudicated under, the frozen F5 Tier-A method contract**.

The existing Tier-A infrastructure can be reused as an adjudication substrate, but it cannot be claimed to have validated M1-PCT. The present pilot is development-only and is not a Tier-A result.

## 2. Estimand correspondence — PASS, bounded to F5 beta mixing

The F5 fixture generates independent world probabilities

\[
p_i \sim \operatorname{Beta}(\alpha,\beta),\qquad
Y_{ij}\mid p_i \sim \operatorname{Bernoulli}(p_i).
\]

For \(\mu=\alpha/(\alpha+\beta)\) and \(\kappa=\alpha+\beta\), M1-PCT computes

\[
W=E[p_i(1-p_i)]
=\frac{\mu(1-\mu)\kappa}{\kappa+1},
\qquad
B=\operatorname{Var}(p_i)
=\frac{\mu(1-\mu)}{\kappa+1}.
\]

The frozen F5 beta22 fixture uses \((\alpha,\beta)=(2,2)\), hence \(\mu=0.5\), \(\kappa=4\), \(W=0.20\), and \(B=0.05\). This is the declared F5 within and untruncated raw-between truth.

The M1 pilot reduces each binary world row to its success count. For the declared common within-world size R, this is sufficient for the beta-binomial likelihood. M1's point_between and between_interval therefore target the same F5 population functional B, subject to the beta-mixing model and the candidate's fitting/bootstrap procedure.

**Boundary of this finding:** this establishes target correspondence for the declared F5 beta-binomial DGP. It does not establish robustness to misspecification, generality beyond F5, or causal identification of theta_A/V_cont.

## 3. M1-PCT is a distinct candidate, not the frozen C5 implementation

The current comparative inference engine declares the F5 method roster as:

- C0_FROZEN_V002_NESTED_PERCENTILE_1.2
- F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.1

The engine's F5 path calls fitted_beta_binomial_parametric_bootstrap; the adjudicator requires the exact declared method roster and reads the candidate's between_estimate_raw and between_interval fields.

M1-PCT declares a different method and fit contract:

- Method: F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0
- Fit: F5_M1_ANALYTIC_LBFGSB_BEST_SUCCESSFUL_START_1.0

M1 refits the analytic-gradient beta-binomial procedure on every parametric bootstrap replicate. The existing C5 path fits its existing candidate and generates component bootstrap intervals using its own implementation. These are not interchangeable merely because both target B.

No adapter currently maps M1's point_between and between_interval into the comparative engine's typed VarianceComparisonResult; M1 is not in IMPLEMENTED_METHODS["F5"]. The current engine therefore cannot accept M1 as a candidate without an explicit method-roster/adapter change.

The M1 fit contract describes a deterministic best-successful analytic-gradient L-BFGS-B fit from a three-start audit and explicitly does not certify a global MLE. This must remain visible as part of the candidate's inferential contract; it must not be silently relabelled as the existing C5 fit procedure.

## 4. Population, unit and denominator reconciliation

| Contract dimension | Existing Tier-A adjudicator | M1 development pilot | Finding |
|---|---|---|---|
| Statistical unit for coverage | One generated dataset paired to one independent truth record | One generated dataset / count vector | Same intended unit |
| Within-dataset structure | M independent worlds, each with R Bernoulli observations | Counts from the same M×R fixture | Compatible for F5 beta-binomial |
| Target population | F5 beta22 fixture population | Same F5 beta22 fixture | Compatible within declared DGP |
| Truth source | Independent fixture truth, joined by dataset ID | spec.true_between from fixture | Independent of M1 fitted values |
| Coverage denominator | All emitted intervals conditional coverage; all datasets for emission | Pilot summary uses emitted datasets for descriptive conditional coverage and all pilot datasets for emission | Formula aligned; pilot is descriptive only |
| Abstention | Missing/invalid interval counted against full dataset denominator with reason | Original-fit failure or any failed bootstrap refit abstains the complete dataset; replicate records retained | Conservative policy compatible in principle |
| Method roster | Frozen C0/C5 pair | M1 alone in a separate pilot | Not integrated |
| Adjudication | adjudicate_matched_datasets and frozen component gates | No Tier-A adjudication; coverage_adjudication=NOT_PERFORMED | Not Tier-A evidence |

The comparative adjudicator pairs dataset and truth IDs, rejects duplicates/mismatches, requires one input/target design per batch, uses the full dataset count n for emission, and uses emitted intervals as the conditional-coverage denominator. Abstentions are retained as n minus interval_emitted.

The M1 pilot's own summary uses the same denominator distinction, but it does not call the frozen adjudicator and its output explicitly declares that coverage adjudication and method selection were not performed.

## 5. Abstention and interval semantics

M1 abstains on an inadmissible original fit. If any bootstrap refit is not an admissible interior fit, the complete dataset abstains; failed replicates are not removed to manufacture a complete-case bootstrap distribution. This is a conservative, auditable policy.

For a valid dataset, M1 emits percentile intervals for both functionals. The point estimate and interval must be treated as M1 outputs, not substituted into C5 records without a typed adapter and method identity.

A remaining contract check for any future integration is to preserve the distinction between:
- point-estimate emission;
- interval emission;
- conditional coverage among emitted intervals;
- unconditional usable-and-covering rate;
- dataset-level abstention and typed reason.

No clipping, positive-only filtering, or hidden deletion is permitted.

## 6. Frozen protocol boundary

The existing comparative holdout protocol defines C0/C1/C5, the existing method roster, K=1,000 per F5 cell, and the two F5 designs M10/R5 and M30/R20. Its specification explicitly states that no new F5 interval method is selected in the preceding development/calibration work package and that a new holdout requires a new protocol, fresh seed namespace, independent data and separate one-use authorization.

Accordingly:
- do not relabel M1 as C5;
- do not reuse prior C5 Tier-A coverage as M1 evidence;
- do not change the frozen C5 protocol or method roster retroactively;
- do not promote the M1 K=50/B=100 development pilot to Tier-A;
- do not initiate a new M1 coverage run from this audit.

## 7. Disposition

| Question | Disposition |
|---|---|
| Does M1's between functional equal F5 beta22 Raw-between truth? | **YES**, for the declared beta-binomial F5 DGP |
| Is the population/world/dataset unit compatible? | **YES**, for the current M/R fixture and dataset-level coverage |
| Are independent truth and denominator concepts already implemented? | **YES**, in the comparative engine; the M1 pilot does not yet use that adjudicator |
| Are M1 abstentions conservatively retained? | **YES**, by dataset-level fail-closed bootstrap policy |
| Is M1 integrated into the existing F5 Tier-A engine/roster? | **NO** |
| Does existing C5 Tier-A evidence validate M1? | **NO** |
| Is the M1 pilot Tier-A evidence? | **NO — development-only, adjudication not performed** |
| Is a new simulation authorized? | **NO** |

**Overall:** ESTIMAND_CROSSWALK_PASS / IMPLEMENTATION_AND_TIERA_CROSSWALK_OPEN / NO_EXECUTION_AUTHORIZED.

## 8. Minimum next operation

Before any M1 coverage execution, prepare a separate, reviewable candidate-integration specification that:

1. defines M1 as a new F5 method ID and preserves its fit contract;
2. specifies a typed adapter from M1 point/interval/abstention outputs to the common comparison record without overwriting C5;
3. reuses the existing independent fixture truth and matched-dataset adjudicator, with no change to the coverage or emission definitions;
4. specifies fresh, disjoint development and validation seed namespaces and a prospective sample-size/resource design;
5. states whether M1 is a development challenger only or is intended for a later independent confirmatory protocol;
6. leaves all C10 causal Analyzer/Evaluator and theta_A/V_cont contracts untouched.

Only after that design is reviewed may an explicitly authorized bounded development operation be considered. This document itself authorizes no tests, benchmark, calibration, holdout or simulation.


## 9. Additional point-estimator contract mismatch

A further static check of the typed comparison interface identifies a second integration gap.

The existing F5 C5 path replaces the observed-data comparison's interval fields and method ID, but retains the common observed-data point fields from observed_nested_mr_result. In particular, its between_estimate_raw remains the untruncated sample estimator S²(world means) − within/R. The comparative engine therefore reports point bias/RMSE for that common point estimator, while C5's principal candidate contribution is its fitted-model interval.

M1 exposes point_within and point_between from the fitted beta-binomial functionals. Those are model-based point estimators and are not the same point estimators retained by the existing C5 comparison record. The current VarianceComparisonResult also requires finite, non-optional point fields, so it cannot directly represent an M1 point-estimation abstention.

Consequences:
- an adapter that simply copies M1 point_between into between_estimate_raw would change the point-estimator semantics for the candidate and make its point metrics non-comparable with the existing engine's current C5 semantics;
- an adapter that retains the common raw point estimate would evaluate M1 intervals but would not evaluate M1's own fitted functional point estimator;
- an M1 fit abstention cannot be represented as an absent point estimate without a typed interface/engine extension.

This is not a reason to redesign the existing adjudicator now. It is an unresolved integration choice that must be explicit in any future M1 candidate specification: either define M1 as an interval-only challenger using the common raw point estimator for cross-method point metrics, while reporting fitted M1 functionals separately; or extend the typed comparison contract to distinguish candidate point estimators and point-estimation abstentions. The latter is a substantive interface change and requires separate review and tests before any execution.

The current audit therefore classifies the M1-to-Tier-A implementation crosswalk as OPEN, not as a ready-to-adapt mapping.
