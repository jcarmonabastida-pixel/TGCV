# C10-S — F5 B1 production/analytic reconciliation implementation 001

**Status:** IMPLEMENTED IN RESEARCH — PASS_STATIC  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** static software implementation and deterministic tests only  
**Design:** `C10S_F5_B1_PRODUCTION_FIT_RECONCILIATION_DESIGN_DRAFT_001.md`  
**Frozen development specification:** v1.0 unchanged  
**Historical B2/B3 result:** unchanged; failed frozen C5 gates

## 1. Implementation summary

The direct reconciliation gap is now addressed additively. C5's production fit remains the source of bootstrap parameters; the analytic-gradient fit and independent log-shape BFGS check remain diagnostic-only.

The per-dataset record now exposes three paths distinctly:

- **P — production:** finite-difference L-BFGS-B, the fit actually used by C5.
- **A — analytic:** analytic-gradient L-BFGS-B, retained as an independent diagnostic.
- **I — independent-coordinate check:** BFGS in (log alpha, log beta), initialized from A. It is explicitly labelled a local cross-check, not a global search.

No optimizer is silently substituted for P.

## 2. Code changes

### 2.1 Production fit records every start

`c10s_fitted_beta_binomial_bootstrap.py` now records, for each of the three production starts:
- start index and initial coordinates;
- success flag and raw termination message;
- final coordinates;
- negative log-likelihood;
- gradient norm when SciPy exposes a finite Jacobian;
- distances to all four configured parameter bounds.

The selected production start index is retained. If all production starts fail, `BetaBinomialFitError` carries the three raw outcomes rather than discarding them. Degenerate inputs rejected before optimizer invocation remain correctly distinguished from attempted-but-failed optimization.

### 2.2 Direct P/A comparison

The new `build_production_analytic_reconciliation` record contains:
- complete P and A start rosters;
- selected parameters and likelihoods for P and A;
- signed and absolute P-minus-A log-likelihood difference;
- signed differences in mean-logit and log-concentration;
- signed differences in alpha, beta, mean probability and concentration;
- separate I optimizer outcome and its existing A-relative diagnostics;
- typed missing-path states when P or A is unavailable.

No numeric concordance tolerance or weak-identification threshold has been introduced. The reconciliation status explicitly says `RAW_COMPARISON_RECORDED_NO_ADJUDICATION_THRESHOLD`; raw similarity is not promoted to a PASS and parameter agreement does not establish concentration identification.

### 2.3 End-to-end propagation

`c10s_nested_mr_comparative_inference_engine.py` serializes the complete reconciliation as `production_analytic_reconciliation_json` for each F5 dataset.

`run_c10s_post_holdout_f5_b2_b3_development_calibration.py` parses and embeds that object in `fit_diagnostics`, alongside the existing likelihood optimizer audit. It also exposes a separate reconciliation status field. This makes the P/A record available in the per-dataset calibration JSONL and downstream report without changing the C5 interval calculations.

## 3. Deterministic tests added

- Production fit retains exactly three starts and the selected start index.
- P/A log-likelihood and shape-parameter differences are calculated against A's selected fit, not I's BFGS terminal point.
- I is labelled as a local BFGS check initialized from A.
- All-failed production starts remain available in the typed exception and reconciliation record.
- Missing analytic audit does not erase the production fit or its three starts.
- Engine serialization includes the reconciliation.
- Calibration runner dataset records retain the complete reconciliation and status.

Existing score/Hessian, likelihood-limit, independent-oracle and boundary tests remain in place.

## 4. Multi-start gate disposition

The runner's existing requirement that all three analytic-gradient starts succeed has **not** been silently weakened. Nor has it been declared a frozen-specification requirement solely because the code currently enforces it.

The implementation preserves all three raw outcomes so that the interpretation can be adjudicated against frozen B1 wording and §8's prohibition on unresolved numerical states. A failed start cannot be equated automatically with either harmless termination or material optimizer disagreement. No threshold or gate change is authorized by this implementation record.

The new P/A status is descriptive and deliberately unthresholded. It is not evidence that the optimizer gate is resolved. A future gate change requires a separately versioned interpretation and deterministic tests; it cannot retroactively relabel B2/B3.

## 5. Scientific and execution boundaries preserved

- No B2/B3 replay or new calibration/validation bank.
- No increase to K or B and no new seeds.
- No C5 interval method substitution or plug-in bootstrap change.
- No new weak-identification cutoff.
- No changes to frozen specification v1.0, C0, C5 acceptance criteria or historical outputs.
- No F5 MCSE interval implementation.
- No writes to `main`, RMA or Evidence→Claim Matrix.
- No C10 Generator, Analyzer or Evaluator execution and no causal TGCV claim advancement.

## 6. Changed source and test files

- `03_EXPERIMENTS/C10-S/harness/c10s_fitted_beta_binomial_bootstrap.py`
- `03_EXPERIMENTS/C10-S/harness/test_c10s_fitted_beta_binomial_bootstrap.py`
- `03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py`
- `03_EXPERIMENTS/C10-S/harness/test_c10s_nested_mr_comparative_inference_engine.py`
- `03_EXPERIMENTS/C10-S/harness/run_c10s_post_holdout_f5_b2_b3_development_calibration.py`
- `03_EXPERIMENTS/C10-S/harness/test_c10s_post_holdout_f5_b2_b3_development_calibration.py`

The existing static workflow `.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml` already includes these source/test paths and runs compilation plus the relevant comparator test suite on pushes to this research branch.

## 7. Commit trail

Implementation and tests were committed incrementally on the research branch. The latest branch head at the time this record was prepared is:

`17283323344abf891fd2aae920f5e04753e2bf3b`

The implementation source identities were fetched after the changes:
- production/bootstrap module blob: `b32ea4fa181397049993bc2e2f0dbd8e919c0ebf`;
- comparative inference engine blob: `f265d1fcb9710ba89ff40fe421d80ce08dc0af68`;
- development calibration runner blob: `5040b3de9305b0ad69d7e06c82010a3057aaa2f5`.

The current branch head is later than some source updates because the commit trail also includes deterministic test and design-record updates. The branch is not promoted.

## 8. Validation disposition

**Implementation persistence:** PASS_STATIC (source and tests fetched from the research branch).  
**Static compile/unit workflow:** PASS — exact tested code commit `18e1c6372af1c191b640e0d1f8d3318b889b28b9`; GitHub Actions run `44645072630`; compile PASS; hash-locked dependency installation PASS; 171 deterministic tests PASS in 24.023 s.  
**Scientific execution:** NOT RUN / NOT AUTHORIZED.  
**F5 method eligibility:** OPEN; historical B2/B3 failed frozen gates.  
**Production/analytic numerical adjudication:** RAW DIFFERENCES NOW EXPOSED; NO THRESHOLD OR PASS/FAIL RULE SELECTED.

The static workflow completed successfully on the exact code/test commit. The later branch commits changed only research documentation; the implementation/test blobs are unchanged from the tested commit. The next admissible action is to review the multi-start gate interpretation and the observed P/A differences in the existing results. No replay or calibration is part of that next step.
