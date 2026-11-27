# C10-S — F5 M10/R5 minimum method decision 001

**Status:** NO SUPPORTED REPLACEMENT CANDIDATE YET — DEVELOPMENT DESIGN ONLY  
**Date:** 2026-11-27  
**Branch:** `research/c10s-coverage-first-focus-20261127`  
**Inputs:** `C10S_F5_M10R5_COVERAGE_EMISSION_RECONCILIATION_001.md`; historical M1-PCT pilot; B2/B3 audits; G7 v1.1 adjudication.

## 1. Decision

Do not launch a new M10/R5 simulation or implement a new interval engine at this point. **No replacement interval candidate is currently supported by the available evidence.**

The current C5 plug-in percentile procedure has adequate emission in B2/B3 but fails coverage. G7 v1.1 fails coverage and has method-specific emission of 88.5%. M1-PCT's strict refitted bootstrap has 4% emission. These results do not support relaxing fit/refit failure rules, dropping replicates, or selecting a method.

The current Tier-A M10/R5 failure remains open. This is a scientific/methodological blocker, not a reason to expand exact numerical certification.

## 2. Why a simple M1 relaxation is rejected

M1-PCT's all-refits-admissible contract rejected 846/4,500 refits:
- 395 finite numerical bound hits;
- 181 no admissible primary fit;
- 158 boundary limits not excluded;
- 112 not strict local maxima / Hessian condition failures.

The first, third and fourth classes may have finite W/B functional values in the current implementation, but they are not automatically valid estimates. Accepting them solely to increase emission would be post-hoc relaxation. The 181 no-admissible-fit cases have no selected fit functional under the current algorithm. Dropping these or using arbitrary terminal optimizer coordinates is not a defensible interval construction.

A legitimate boundary-aware refit procedure would need a prospectively defined estimator on the extended parameter space, a deterministic rule for non-unique or boundary likelihood maxima, and a repeated-sampling interpretation for W and B. The current evidence does not supply that contract. Building such a contract would be a new method, not a minimal relaxation.

## 3. Why profile likelihood is not selected now

Direct W/B profile likelihood remains a possible alternative, but:
- its cutoff is not calibrated for the relevant weak-identification/boundary regimes;
- existing F5 M2 work concerns a more complex inversion path and has not established coverage;
- the prior profile work became computationally expensive;
- no evidence yet shows that this complexity is necessary or that it would meet emission.

It is not selected as the default next method. Do not resume Sturm/topology work.

## 4. M10/R5 disposition

- C5 B2/B3: emission PASS, coverage FAIL.
- G7 v1.1: emission FAIL, coverage FAIL.
- M1-PCT: emission FAIL; descriptive coverage based on two intervals is unusable.
- C0: not a validated fallback; its frozen coverage/Wilson gates fail.
- No new M10/R5 simulation, calibration, code change or method selection.
- No post-hoc κ threshold, complete-case bootstrap, failed-refit deletion, or global width adjustment.

**Decision:** `NO_SUPPORTED_F5_M10R5_CANDIDATE`.

Reopen M10/R5 only if a concrete new method contract explains how it obtains valid W/B intervals for boundary/non-identification cases without changing the estimands or conditioning on successful fits.

## 5. Next coverage task

Proceed to the separate **F5 M30/R20 raw-between** deficit. Preserve the existing M30/R20 within PASS under the exact declared G7 method/DGP scope.

The next task is a narrow static reconciliation of:
- G7 v1.1 raw-between coverage 93.353%, Wilson [91.631%,94.742%], emission 99.3%;
- C5 B2/B3 raw-between coverage 93.08%/93.00%, Wilson intervals [92.34%,93.75%]/[92.26%,93.67%], emission 100%;
- high-fitted-κ tail directional misses and interval width;
- the small B=1,000 versus B=4,000 endpoint sensitivity;
- the M1-PCT pilot's descriptive M30/R20 raw-between 94% with 100% emission (K=50; not formal evidence).

Determine whether the repeated deficit is primarily a conditional plug-in interval defect and whether the existing M1-PCT refitted candidate is worth a bounded M30/R20 raw-between development comparison. Do not touch M30/R20 within.

## 6. Governance

No frozen criterion, DGP, estimand, historical result or authorization changed. No Tier-A confirmatory, Tier-B or causal C10-S execution is authorized. All historical exposed data remain development evidence only.
