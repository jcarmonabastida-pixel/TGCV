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

### R1 — C0 interval baseline is now integrated (RESOLVED)

The engine emits C0 only as the common point-estimate record. It does not run or adapt the frozen v002 two-stage nonparametric percentile bootstrap and therefore emits no C0 within, raw-between or projected-MCSE intervals.

Consequently, the current engine cannot yet answer the comparative question "does C1/C5 improve on the frozen v002 procedure on the same datasets?" It can compare candidate point estimates with C0 and candidate intervals with analytical truth, but it cannot make a matched interval-method comparison against C0.

**Resolution implemented:** the engine now calls `theta_a_nested_mc_precision.py::analyze_nested_precision` directly through `_frozen_v002_baseline`. No bootstrap law was copied. It preserves v002's outer-cluster then inner-R resampling, B denominator, all-same-source draws, raw negative-between draws, MCSE abstention and provenance. The adapter independently reconciles within, raw-between and observed world-mean variance against the common interface and fails closed on disagreement. Deterministic tests verify interval emission, protocol/method provenance and point-target reconciliation.

### R2 — F5 MCSE positive-only conditioning is removed (RESOLVED BY FAIL-CLOSED ABSTENTION)

The fitted F5 candidate appends a bootstrap MCSE draw only when the common point adapter returns a numeric `mcse_estimate`. Negative raw-between/projected-variance draws therefore do not enter the MCSE quantile calculation. The candidate then computes percentile limits from the retained subset when the valid-draw fraction reaches its internal threshold.

This is a positive-projection conditional bootstrap distribution. It is not a boundary-aware joint confidence construction. The Tier A investigation and frozen v002 protocol explicitly prohibit silently dropping negative raw draws or conditioning MCSE inference on positive draws. A minimum-valid-draw threshold does not repair that conditioning.

**Resolution implemented:** C5 still reports the projectable-draw count/fraction as a diagnostic but no longer computes or emits an MCSE percentile interval from that selected subset. It always returns `mcse_interval=None` with `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED`. A future F5 MCSE method must define the constrained parameter space and coverage target directly, and be checked against the independent beta-binomial oracle.

### R3 — Availability denominators are now separately exposed (RESOLVED FOR CURRENT SCOPE)

C5 currently has an internal per-dataset valid-MCSE-bootstrap-draw fraction (default threshold 0.90), while the study-level protocol requires the fraction of independent datasets emitting an MCSE interval to be at least 0.95 before conditional coverage can be treated as calibrated.

These are different quantities:
1. within-dataset bootstrap projection-valid fraction, denominator B;
2. across-dataset interval-emission rate, denominator K.

The engine now reports C5's projectable draw fraction with denominator B as a diagnostic and the adjudicator reports interval-emission rate with denominator K, including a K-based Wilson interval. Because C5 MCSE intervals are withheld, the B fraction is not used as an emission threshold or as permission to calculate conditional coverage.

### R4 — F1/F5 MCSE scope is separated explicitly (RESOLVED BY SCOPE EXCLUSION)

C1's MCSE interval is a projection of an F1 Gaussian Bonferroni joint confidence region. It may be empty after intersection with the physical parameter space, producing a legitimate typed abstention. It is conservative and model-specific.

C5's present MCSE percentile construction is not a comparable joint procedure and is invalid for confirmatory comparison under R2. Do not compare their MCSE coverage as if both intervals had equivalent inferential definitions. The initial matched comparison can validly compare:
- within component: C0 v002, C1 F1, C5 F5;
- raw between component: C0 v002, C1 F1, C5 F5;
- target MCSE: C0 v002 versus C1 F1 only, while C5 is explicitly NOT_IMPLEMENTED/ABSTAINED until R2 is resolved.

C5 MCSE is explicitly not implemented, so no false like-for-like F1/F5 MCSE comparison is produced. F1 MCSE can be compared between C0 and C1; F5 MCSE remains an explicit abstention until its own joint method exists. No pooling across F1 and F5 is allowed.

### R5 — Adjudication Wilson uncertainty is complete for operational gates (RESOLVED)

The engine reports conditional coverage MCSE/Wilson limits and unconditional cover rate, but does not provide Wilson limits for dataset-level interval-emission rate or unconditional cover rate. These are required to judge the operational emission gate and the joint usable-and-covering rate without relying on point percentages alone.

**Resolution implemented:** the adjudicator now reports Wilson 95% intervals for point emission, interval emission and unconditional cover using denominator K, plus conditional coverage Wilson/MCSE using the number of emitted intervals. Denominators are explicit in the metrics contract.

### R6 — Method roster and dataset/truth pairing integrity are enforced (RESOLVED)

The adjudicator requires paired comparison/truth rows and one target design, but it does not currently require every dataset record to contain the same expected method roster. A method absent from some records can be omitted from per-record evaluation while still using total K as the denominator.

**Resolution implemented:** each comparison now carries an immutable `dataset_id`; each truth row carries the same ID. The adjudicator rejects duplicate/mismatched IDs, incomplete or unexpected family-specific method rosters, duplicate candidate IDs, candidate/result method-ID mismatch, unsupported families and inconsistent input/target designs. Methods that cannot emit an interval remain present with typed abstention.

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

## 6. Updated disposition (2026-11-19)

**MATCHED COMPONENT COMPARATOR: IMPLEMENTED / STATIC CI PASS 39/39. FULL F5 MCSE COMPARISON: NOT READY.**

R1, R2, R3, R5 and R6 are now resolved in the research implementation. R4 is resolved by explicitly withholding the unsupported C5 MCSE interval rather than pretending it is comparable to C1. The engine now compares frozen C0 v002 intervals against C1 within F1 and against C5 within/between F5 on the same dataset IDs. F5 MCSE is an explicit typed abstention; F1 MCSE remains C0-vs-C1 only.

GitHub Actions run `44457516440` (run 24), commit `932ac429e85897430b9a42901533cb61cba6ac11`, completed SUCCESS: pinned dependencies, compilation and 39 deterministic tests passed. This is static/formula-contract evidence, not coverage calibration.

A separate branch-targeting correction is recorded transparently: one GitHub Contents update briefly wrote the research-only engine file to `main` (commit `22eb35f413f0941acd725b024b50852b514f291e`); the file was immediately deleted from `main` in corrective commit `d7e103afdf5d701b6d4970645a2c2bb017578597` and then committed to the research branch (`eda3f54...`). The final `main` tree is expected to contain no C10-S comparative engine; verify its absence. No lasting scientific/governance content on `main` was changed.

Remaining before a full F1/F5 calibration study: specify and implement a valid F5 boundary-aware joint MCSE method; freeze the comparative holdout protocol and seed namespace; justify K/B and bootstrap endpoint Monte Carlo error prospectively; then obtain separate explicit authorization for numerical calibration. The original v002 Tier A result remains NOT_VALIDATED and is not a holdout. Tier B and C10 scientific execution remain unauthorized.

No frozen v002 protocol, original Tier A result, production Analyzer, RMA, Evidence→Claim Matrix, STATUS, Tier B authorization or scientific C10 authorization is changed by this audit.
