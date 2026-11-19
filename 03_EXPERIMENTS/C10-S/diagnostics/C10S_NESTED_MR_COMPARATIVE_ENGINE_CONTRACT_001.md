# C10-S — Unified Nested M/R Comparative Inference Engine

**Record:** C10S-NESTED-MR-COMPARATIVE-ENGINE-CONTRACT-001  
**Status:** RESEARCH BRANCH IMPLEMENTATION — STATIC CI PASS (36/36) / NUMERICAL CALIBRATION NOT RUN  
**Date:** 2026-11-19  
**Scope:** Matched-data inference comparison within F1 and within F5  
**Baseline preserved:** nested M/R protocol v002 and production Analyzer unchanged

## 1. Purpose

Connect the existing common observed-data interface to the first currently implemented family-specific inferential candidates and provide one adjudication contract. This is a research comparison harness. It does not select a method, calibrate coverage, authorize Tier B, or establish scientific validity for C10.

## 2. Reused components

The engine reuses, without duplicating their mathematical responsibilities:

- c10s_variance_comparison_interface.py: immutable input validation and common raw within, observed-world variance, untruncated raw-between and point MCSE targets.
- c10s_f1_exact_pivotal_candidate.py: F1-only exact within and conservative joint-pivot raw-between intervals, plus joint confidence-set projection for target MCSE.
- c10s_fitted_beta_binomial_bootstrap.py: fitted F5 beta-binomial parametric bootstrap and fit/boundary/failure diagnostics.
- c10s_gaussian_variance_oracles.py: independent F1 finite-sample reference formulas and profile likelihood diagnostic.
- c10s_beta_binomial_variance_oracles.py: independent F5 finite-R count law and finite-M estimator moments.

The oracles are references; they are not silently substituted for fitted inference. The F1 dispatch also performs an independent formula reconciliation of C1's conservative raw-between interval against the Gaussian oracle and fails closed on disagreement.

## 3. Dispatch contract

c10s_nested_mr_comparative_inference_engine.py::compare_dataset requires an explicit family label.

| Family | Common baseline | Candidate dispatched | Scope |
|---|---|---|---|
| F1 | C0 raw common result | C1 exact/pivotal | Balanced Gaussian random-intercept only |
| F5 | C0 raw common result | C5 fitted beta-binomial parametric percentile bootstrap | Bernoulli nested beta-binomial only |

F5 requires explicit bootstrap replicate count and seed. The candidate records fitted parameters, fit state, RNG, seed, replicate count and valid-MCSE-draw rate in provenance/diagnostics.

C2, C3 and C4 are explicitly returned as unavailable. No placeholder result, fallback method, or inferred implementation is permitted. The F1 oracle/profile diagnostic and F5 moment oracle remain distinct from interval candidates.

## 4. Adjudication contract

adjudicate_matched_datasets requires one family, paired comparison/truth records, and one common target design (M*,R*). Different target designs must be stratified rather than pooled.

For each method × target (within, raw between, target MCSE), it reports:

- point-estimate emission rate, bias and RMSE;
- interval emission rate;
- coverage conditional on interval emission;
- unconditional cover rate over all datasets (joint usable-and-covering rate);
- lower- and upper-tail miss rates among emitted intervals;
- mean interval width;
- typed abstention/non-emission counts and reason frequencies;
- coverage MCSE and 95% Wilson interval.

C0 is a point-only baseline; its lack of interval is explicitly labelled POINT_ONLY_BASELINE_NO_INTERVAL, not represented as a fitted candidate's statistical failure. The evaluator reports metrics; it does not apply acceptance thresholds or select a winner.

No pooling across F1 and F5 is allowed. No averaging across targets or methods can rescue a failed cell.

## 5. Tests authored, not executed

test_c10s_nested_mr_comparative_inference_engine.py contains deterministic contracts for:

1. F1 dispatch to C1 only and explicit unavailability of C2-C4.
2. F5 requirement for explicit bootstrap B and seed.
3. F5 dispatch to the fitted candidate and seed provenance.
4. Conditional and unconditional coverage, MCSE and Wilson interval reporting.
5. Abstention accounting, paired-data requirements and invalid truth rejection.
6. Unsupported-family rejection.

The six new engine tests executed successfully as part of the 36-test static suite. They are not coverage calibration or Monte Carlo evidence.

## 6. Integration boundary and remaining gates

| Gate | State |
|---|---|
| Common data contract | IMPLEMENTED; prior deterministic tests passed |
| F1 pivotal candidate | IMPLEMENTED; deterministic candidate tests PASS in static CI |
| F5 fitted candidate | IMPLEMENTED; deterministic candidate tests PASS in static CI; MCSE interval method requires further boundary audit |
| Unified F1/F5 dispatch | IMPLEMENTED |
| Common adjudication metrics | IMPLEMENTED |
| New engine deterministic tests | EXECUTED; 6/6 PASS within 36-test suite |
| Static workflow path/command integration | IMPLEMENTED; run 15 PASS |
| New engine test execution | AUTHORIZED BY USER; EXECUTED; PASS |
| Coverage calibration and method selection | NOT AUTHORIZED |
| Independent holdout | OPEN / NOT AUTHORIZED |
| Tier B | NOT AUTHORIZED |
| Scientific C10 execution | NOT AUTHORIZED |
| Promotion to main | NOT AUTHORIZED |

The existing GitHub Actions workflow has an explicit path allowlist and test command. It has not yet been changed to include the new engine and test. Updating that workflow would trigger its push-based static workflow; therefore this integration deliberately stops short of modifying the workflow while technical test execution remains unauthorized. Do not claim CI coverage for the new engine until the workflow is amended under explicit execution authorization and the resulting run is inspected.

## 7. Scientific interpretation

This engine creates a common comparison surface, not a validated general-purpose estimator. C1 exactness is conditional on F1's balanced Gaussian random-intercept model. C5 is a fitted-model exploratory percentile bootstrap and remains uncalibrated. A subsequent readiness audit found that C5's MCSE percentile currently conditions on bootstrap draws with a nonnegative plug-in projection, which violates the frozen no-positive-only-conditioning rule; until a boundary-aware F5 MCSE method exists, that target must be reported as not implemented/abstained. The engine also lacks C0's frozen v002 interval adapter, so it is not yet a complete interval-method comparison. F1 and F5 results must be interpreted within their own DGP families.

Coverage, interval width, point error, emission and abstention are all reported separately. A high conditional coverage with low emission cannot be called operationally successful. A narrow interval cannot compensate for undercoverage. The evaluator does not make that trade-off decision.

Protocol v002, its historical result, the production Analyzer, canonical main, RMA, Evidence→Claim Matrix and scientific authorization state are unchanged.