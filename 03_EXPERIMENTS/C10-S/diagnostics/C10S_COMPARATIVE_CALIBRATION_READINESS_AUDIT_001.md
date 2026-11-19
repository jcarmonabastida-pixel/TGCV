# C10-S — Comparative calibration readiness audit 001

**Record:** C10S-COMPARATIVE-CALIBRATION-READINESS-AUDIT-001  
**Status:** RESEARCH AUDIT — DESIGN/IMPLEMENTATION REVIEW ONLY / NOT READY FOR NUMERICAL CALIBRATION  
**Date:** 2026-11-19  
**Branch:** `research/c10s-nested-mr-calibration-design-20261119`  
**Baseline:** nested M/R protocol v002 remains frozen; Tier A original disposition remains NOT_VALIDATED.

## 1. Purpose and governance boundary

This audit checks whether the new F1/F5 comparison engine is a scientifically adequate basis for the next numerical calibration/holdout. It does not authorize or perform numerical execution, calibration, Tier B, C10 scientific execution, or promotion to `main`.

The canonical repository state was recovered from `main`: RMA v3.38, Evidence→Claim Matrix v1.47, STATUS 2026-11-06. The canonical RMA and Matrix retain C10/Value as OPEN; C09's bounded causal support does not establish `Delta T_acc -> Delta V`. The research-branch C10-S nested M/R work is auxiliary numerical-method validation only and must not be represented as C10 causal recovery evidence.

## 2. Evidence already established

- Frozen numerical protocol: `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001` v002, SHA-256 `cf3fd80e474e58632f6a88d8afb092df8db31716ed962826f949f5750405bad1`.
- Original Tier A: K=1,000 and B=1,000 in each of eight cells; the result is NOT_VALIDATED and remains development evidence, not a holdout.
- Tier A analysis identifies substantial percentile-bootstrap undercoverage in several F1 within/between cells and F5 small-support limitations. The exact F1 within pivot restores nominal coverage in the explored Gaussian cells; the conservative joint-pivot between interval overcovers but provides a model-specific reference.
- F1 exact/pivotal candidate, F5 fitted beta-binomial candidate, common data interface and unified F1/F5 orchestrator are implemented on this research branch.
- GitHub Actions run `44456441892`, commit `478ee8033828ac5cdd773cb3cd6f397162fc11bb`, completed SUCCESS: compile passed and 36 deterministic tests passed. This is static/formula-contract evidence only, not coverage calibration.

## 3. Blocking methodological findings

### R1 — C0 interval baseline is absent from the unified engine

The engine emits C0 only as the common point-estimate record. It does not run or adapt the frozen v002 two-stage nonparametric percentile bootstrap and therefore emits no C0 within, raw-between or projected-MCSE intervals.

Consequently, the current engine cannot yet answer the comparative question "does C1/C5 improve on the frozen v002 procedure on the same datasets?" It can compare candidate point estimates with C0 and candidate intervals with analytical truth, but it cannot make a matched interval-method comparison against C0.

**Required resolution:** add a strictly additive adapter around the frozen v002 bootstrap implementation, preserving its exact outer-cluster then inner-R resampling law, B-draw denominator, all-same-source cluster draws, raw negative between draws, MCSE abstention rule and output provenance. Do not reimplement or subtly alter v002 inside the comparator. If the frozen implementation cannot be imported without changing it, use a read-only adapter to its existing callable or mark C0 interval comparison NOT_AVAILABLE; do not copy/paste a divergent implementation.

### R2 — F5 MCSE interval currently conditions on valid/nonnegative projections

The fitted F5 candidate appends a bootstrap MCSE draw only when the common point adapter returns a numeric `mcse_estimate`. Negative raw-between/projected-variance draws therefore do not enter the MCSE quantile calculation. The candidate then computes percentile limits from the retained subset when the valid-draw fraction reaches its internal threshold.

This is a positive-projection conditional bootstrap distribution. It is not a boundary-aware joint confidence construction. The Tier A investigation and frozen v002 protocol explicitly prohibit silently dropping negative raw draws or conditioning MCSE inference on positive draws. A minimum-valid-draw threshold does not repair that conditioning.

**Required resolution:** until a separately specified F5 boundary-aware joint procedure exists, C5 may report within and raw-between intervals but MUST return no MCSE interval, with a typed reason such as `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED`. Preserve the count/rate of non-projectable draws as a diagnostic, not as permission to calculate a conditional interval. A future F5 MCSE method must define the constrained parameter space and coverage target directly, and be checked against the independent beta-binomial oracle.

### R3 — Two distinct availability denominators are not separated in the contract

C5 currently has an internal per-dataset valid-MCSE-bootstrap-draw fraction (default threshold 0.90), while the study-level protocol requires the fraction of independent datasets emitting an MCSE interval to be at least 0.95 before conditional coverage can be treated as calibrated.

These are different quantities:
1. within-dataset bootstrap projection-valid fraction, denominator B;
2. across-dataset interval-emission rate, denominator K.

They must be named, reported and adjudicated separately. The 0.90 internal default is not justified as a calibration criterion and cannot be conflated with the 0.95 study-level emission gate.

### R4 — C1 and C5 do not have equivalent inferential scope

C1's MCSE interval is a projection of an F1 Gaussian Bonferroni joint confidence region. It may be empty after intersection with the physical parameter space, producing a legitimate typed abstention. It is conservative and model-specific.

C5's present MCSE percentile construction is not a comparable joint procedure and is invalid for confirmatory comparison under R2. Do not compare their MCSE coverage as if both intervals had equivalent inferential definitions. The initial matched comparison can validly compare:
- within component: C0 v002, C1 F1, C5 F5;
- raw between component: C0 v002, C1 F1, C5 F5;
- target MCSE: C0 v002 versus C1 F1 only, while C5 is explicitly NOT_IMPLEMENTED/ABSTAINED until R2 is resolved.

No pooling across F1 and F5 is allowed.

### R5 — Adjudication uncertainty is incomplete for operational gates

The engine reports conditional coverage MCSE/Wilson limits and unconditional cover rate, but does not provide Wilson limits for dataset-level interval-emission rate or unconditional cover rate. These are required to judge the operational emission gate and the joint usable-and-covering rate without relying on point percentages alone.

**Required resolution:** report K-denominator Wilson intervals for emission and unconditional cover rates in addition to the conditional-coverage Wilson interval whose denominator is the number of emitted intervals. Keep all denominators explicit.

### R6 — Missing-method and pairing integrity need explicit enforcement

The adjudicator requires paired comparison/truth rows and one target design, but it does not currently require every dataset record to contain the same expected method roster. A method absent from some records can be omitted from per-record evaluation while still using total K as the denominator.

**Required resolution:** require exact expected method roster per family and per dataset, with explicit typed abstention records for methods that cannot emit an interval. Fail closed on missing/duplicate method IDs, duplicate dataset IDs, or inconsistent cell/target metadata. Pairing must be established by immutable dataset IDs and truth IDs, not only equal sequence lengths.

## 4. Calibration design inherited from frozen v002

The existing v002 numerical-method protocol already fixes the baseline validation design:
- Tier A: eight cells, K=1,000, B=1,000, nominal 95%, F1 three Gaussian parameter regimes × two M/R designs and F5 beta22 × two M/R designs.
- Acceptance for each regular component cell: observed coverage in [0.93, 0.97] and its 95% Wilson interval contains 0.95.
- Projected-MCSE availability must be at least 0.95 across datasets before conditional coverage is treated as calibrated.
- Tier B: 20 stochastic diagnostic cells, K=500, B=500, plus deterministic guards; Tier B remains unauthorized.
- The Tier A datasets are development evidence and MUST NOT be reused as independent holdout after method development/selection.

The comparative candidate study is a separate protocol and must not rewrite v002. Its holdout should reuse the same eight Tier A parameter cells and M/R designs with a new seed namespace and new independent datasets. Any additional stress cells must be specified prospectively and kept separate from the v002 eight-cell comparability core. K/B must be justified by a resource benchmark and endpoint Monte Carlo-error analysis before a new execution contract is frozen; no value is selected by this audit.

## 5. Required integrated closure sequence

1. Resolve R1 by adding the frozen C0 interval adapter and tests that reconcile its outputs with the existing v002 implementation on fixed datasets/seeds.
2. Resolve R2 by disabling C5 MCSE interval emission until a valid F5 joint boundary method is specified; preserve diagnostics and typed abstention.
3. Resolve R3–R6 in the common result/adjudication contract, with adversarial tests for denominator integrity, missing methods and pairing.
4. Reconcile all methods against independent F1/F5 truth oracles; do not use the same implementation path to generate truth and estimate.
5. Freeze a separate comparative holdout protocol: eight-cell core, new seed namespace, K/B/resource limits, bootstrap endpoint Monte Carlo uncertainty, acceptance and family/cell adjudication.
6. Only then prepare a dedicated remote calibration workflow and execution manifest. This requires a separate explicit authorization; the prior approval covered only the static deterministic software suite.

## 6. Disposition

**COMPARATIVE CALIBRATION READINESS: NOT READY.**

The common engine is a useful software integration milestone, and its static suite passes. It is not yet a complete matched interval comparator because C0 intervals are missing, F5 MCSE inference conditions on a selected subset, and the adjudicator needs stronger denominator/method-roster integrity.

No code, frozen v002 protocol, original Tier A result, production Analyzer, main, RMA, Evidence→Claim Matrix, STATUS, Tier B authorization or scientific C10 authorization is changed by this audit.
