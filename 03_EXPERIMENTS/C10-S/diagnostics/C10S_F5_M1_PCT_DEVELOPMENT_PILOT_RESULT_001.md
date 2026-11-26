# C10-S — F5 M1-PCT development pilot result 001

**Date:** 2026-11-26  
**Status:** EXECUTED — DEVELOPMENT-ONLY — M1-PCT NOT SELECTED  
**Workflow run:** [45822945892](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45822945892)  
**Code commit:** `ab32975c00b8c0c1764f3f455c11fa1092c9fe53`  
**Artifact ID:** `15120216994`  
**Artifact SHA-256:** `142915b64fb819028f2db8c59b38d0b616c96b7d7d2e1f19b52effa597665806`  
**Artifact:** `c10s-f5-m1-development-pilot.zip`

## 1. Scope and integrity

The workflow completed successfully:
- pinned Python 3.12.10 and hash-locked dependencies: PASS;
- Python compilation: PASS;
- deterministic M1 tests: PASS (9/9);
- bounded development pilot: PASS as an execution;
- artifact upload: PASS.

Pilot contract:
- schema: `C10S-F5-M1-PCT-DEV-PILOT-1.0`;
- scope: `DEVELOPMENT_ONLY_SMOKE_PILOT_NOT_TIER_A_NOT_CONFIRMATORY`;
- 50 datasets per cell;
- 100 parametric-bootstrap refits per admissible original dataset;
- no coverage adjudication and no method selection;
- seed audit: PASS, 10,200 new seed values, zero collisions against 137,200 historical values checked.

This is evidence that the implementation executed reproducibly under its declared development scope. It is not a calibration adjudication.

## 2. Component results

| Cell | Datasets | Emitted | Emission | Within descriptive coverage | Raw-between descriptive coverage | Failed bootstrap refits |
|---|---:|---:|---:|---:|---:|---:|
| F5 beta22 M10/R5 | 50 | 2 | 4% | 100% (2 emitted) | 100% (2 emitted) | 846 |
| F5 beta22 M30/R20 | 50 | 50 | 100% | 98% (50 emitted) | 94% (50 emitted) | 0 |

Descriptive coverage here is only the fraction of emitted development intervals covering the known fixture truth. It is not accompanied by a confirmatory Wilson adjudication and must not be interpreted as evidence that the target coverage band has been met. In M10/R5, the denominator is only two emitted intervals.

## 3. M10/R5 failure-state reconciliation

Across 50 original datasets:
- 45 original fits were classified as `PRIMARY_ANALYTIC_INTERIOR_FIT`;
- 5 original fits abstained: 2 `BOUNDARY_LIMIT_NOT_EXCLUDED`, 2 `NO_ADMISSIBLE_PRIMARY_FIT`, and 1 `FINITE_NUMERICAL_BOUND_HIT`.

Across the 4,500 bootstrap refits generated from the 45 admissible original fits:
- 3,654 were `PRIMARY_ANALYTIC_INTERIOR_FIT`;
- 395 were `FINITE_NUMERICAL_BOUND_HIT`;
- 181 were `NO_ADMISSIBLE_PRIMARY_FIT`;
- 158 were `BOUNDARY_LIMIT_NOT_EXCLUDED`;
- 112 were `PRIMARY_FIT_NOT_STRICT_LOCAL_MAXIMUM`.

Thus 846/4,500 bootstrap refits (18.8%) were non-admissible. Under the frozen M1-PCT draft contract, any non-admissible replicate makes the complete dataset abstain; no complete-case bootstrap distribution is formed. This produces 43 bootstrap-failure abstentions among 45 originally admissible datasets, in addition to the five original-fit abstentions, leaving only two emitted intervals overall.

This is not merely a generic optimizer precision warning. The failures span finite numerical bound hits, absent admissible starts, failure to exclude available likelihood limits, and non-negative-definite/non-finite observed Hessian classifications. The present M1 contract therefore cannot meet the frozen >=95% emission requirement in M10/R5.

## 4. M30/R20 result

All 50 original fits and all 5,000 bootstrap refits were classified as admissible interior fits under the current contract. Emission was 100%. Descriptive coverage was 98% for within and 94% for raw-between. These small development counts do not establish coverage calibration or satisfy the Tier-A adjudication procedure.

## 5. Decision

**M1-PCT is not selected for Tier-A.** The method fails the inherited emission requirement decisively in M10/R5. Its M30/R20 descriptive result cannot compensate for a failed cell; no pooling is permitted.

The failure is informative: the strict interior-only refit bootstrap is unstable under the weak-identification / boundary behaviour of M10/R5. Weakening the abstention rule or dropping failed replicates would change the inferential procedure and is not an acceptable repair.

## 6. Next bounded operation

Proceed to a static design review of a minimal F5 component-profile-likelihood route for the actual functionals W and B, using the existing analytic beta-binomial likelihood, derivatives, exact finite-R oracle and boundary likelihood comparisons. The existing F5 profile-likelihood code located in the harness concerns the MCSE functional and must not be misrepresented as a W/B interval method.

The review must establish:
1. whether W and B can be profiled directly with a one-dimensional nuisance optimization and explicit `kappa -> 0` / `kappa -> infinity` boundaries;
2. whether the likelihood-ratio cutoff can be justified/calibrated without assuming regular Wilks behaviour at weak-identification or boundary cases;
3. how the profile set handles disconnected/non-identifiable regions, non-unique nuisance maxima and unbounded/one-sided intervals;
4. what deterministic score, oracle, boundary and inversion tests are required before any development-only simulation;
5. whether the candidate can plausibly meet emission >=95% without concealing non-identification.

No W/B profile interval implementation, cutoff, method selection, Tier-A run or authorization is created by this report. If profile likelihood cannot produce admissible finite intervals under the frozen rules, report the exact incompatibility rather than relaxing thresholds.

## 7. Non-claims

This pilot does not establish F5 calibration, Tier-A readiness, Tier-A PASS, Tier-B authorization, or the causal effect `ΔT_acc -> Value`. It does not modify frozen C10-S protocols, historical B2/B3/G7 results, canonical governance, or `main`.
