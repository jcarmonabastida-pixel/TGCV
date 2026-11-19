# C10-S — Post-holdout F1/F5 deterministic controls implementation record

**Record:** C10S-POST-HOLDOUT-F1-F5-DETERMINISTIC-CONTROLS-IMPLEMENTATION-001  
**Date:** 2026-11-19  
**Status:** PARTIAL IMPLEMENTATION / STATIC SUITE PASS / NUMERICAL DEVELOPMENT EXECUTION NOT AUTHORIZED  
**Frozen design:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md` v1.0  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Implementation commit:** `e7920543e8c6fb19582c62446381df7cb1d95e1a`  
**Execution authorization:** NONE

---

## 1. Scope and disposition

This record documents the first implementation increment for deterministic controls A1 (F1 profile likelihood) and B1 (F5 beta-binomial likelihood/optimizer audit) under the frozen post-holdout development specification.

The increment is limited to software-level deterministic calculations and tests on fixed fixtures. It did **not** generate DGP datasets, run Monte Carlo calibration/validation banks, bootstrap comparison banks, endpoint sensitivity experiments, Tier A/B, or the causal C10 Generator/Analyzer/Evaluator experiment.

The latest static workflow passed. This establishes that the listed source compiles and the declared software-contract suite passes on the exact commit. It does not establish coverage, estimator calibration, empirical eligibility, or scientific acceptance.

## 2. F1 — profile-likelihood controls implemented

Source:
- `harness/c10s_f1_between_profile_likelihood.py`
- `harness/test_c10s_f1_between_profile_likelihood.py`

Implemented controls:

1. The confidence-set callable now requires an explicit `family="F1"`; non-F1 dispatch is rejected.
2. Each profile evaluation invokes the existing nuisance optimizer/root diagnostic and the exact-rational score-polynomial root isolator.
3. All isolated positive nuisance stationary roots are evaluated; the independent score sign is checked on the monotone polynomial partitions.
4. The bounded scalar optimizer is compared with the likelihood at the isolated stationary-root maximum. A discrepancy above the frozen numerical tolerance, unresolved root/tangency, optimizer boundary state, non-finite value or non-unique local nuisance maximum causes typed abstention.
5. The search span and diagnostic grid adapt to the ratio between the variance scale and within variance. Excessive required range fails closed.
6. The profile result records nuisance-certification and topology status.
7. The connectedness argument is documented in the callable: by the envelope derivative, an interior stationary point of the profiled likelihood requires (q^*=S^2_{\bar Y}); substituting into the nuisance score gives (s^*=MSW) and (\tau^*=S^2_{\bar Y}-MSW/R). Hence, conditional on the unique certified nuisance maximum and continuity, there is at most one interior stationary point in (\tau>0), and the LR acceptance set is connected.

Deterministic tests include explicit family rejection, root inversion, endpoint LR equations, zero-boundary inclusion, extreme-cutoff fail-closed behaviour, scale equivariance, polynomial roots, tangential/near-tangential score cases, and critical-point solver adversarial cases.

**F1 disposition:** deterministic control path implemented and tested for current fixtures. It is not yet eligible for calibration. The six frozen F1 cell regimes and additional adversarial nuisance/topology cases still require a systematic fixture matrix and independent review of the analytical connectedness argument.

## 3. F5 — analytic likelihood and optimizer audit implemented

Source:
- `harness/c10s_f5_beta_binomial_likelihood_diagnostics.py`
- `harness/test_c10s_f5_beta_binomial_likelihood_diagnostics.py`

Implemented controls:

1. Analytic beta-binomial log-likelihood, score and Hessian in mean-logit/log-concentration coordinates.
2. Deterministic central finite-difference comparisons for both score components and the full Hessian.
3. Explicit likelihood evaluations for the extended limits (\kappa\to\infty) (binomial) and (\kappa\to0) (two-point mixing), including the zero-probability state for interior counts under the latter.
4. A deterministic optimizer audit that retains every declared bounded L-BFGS-B start, including success/message, final coordinates, objective, gradient norm and distance to each numerical bound.
5. An independently parameterized BFGS audit in ((\log\alpha,\log\beta)), recording objective difference, parameter distance, score norm and observed-Hessian eigenvalues.
6. The audit reports likelihood-concordant parameter disagreement separately from objective discordance and optimizer non-convergence; it does not silently rewrite the existing C5 fit selection.

Deterministic tests cover derivative agreement, Hessian symmetry/finiteness, input guards, both extended likelihood limits, the high-concentration/binomial limit and retention of all optimizer starts plus the independent fit audit.

**F5 disposition:** deterministic likelihood and optimizer-audit primitives implemented and tested. The audit helper is not yet integrated into the per-dataset C5 result/provenance path. The exact finite-R oracle crosswalk, boundary-adjacent derivative fixtures, and diagnostic status propagation into C5 records remain open.

## 4. Static validation

Workflow:
`.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`

Run:
- ID: `44582807370`
- Commit: `e7920543e8c6fb19582c62446381df7cb1d95e1a`
- Conclusion: `SUCCESS`
- Compile step: PASS
- Test step: PASS
- Test modules: existing comparator/oracle/runner contracts plus F1 profile-likelihood and F5 likelihood-diagnostic modules
- Result: **110 tests passed**

The workflow used the repository's hash-locked dependencies. No DGP or bootstrap dataset bank was executed.

Other F1 numerical-stress workflows were triggered by branch pushes but their authorization conditions were false; their jobs concluded `SKIPPED`. No numerical-stress execution was performed.

## 5. Exact source identities at the validated commit

| Artifact | Git blob SHA |
|---|---|
| Frozen design v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |
| F1 profile source | `87de3f15468482327fa1170b050fdd54dac13ade5` |
| F1 profile tests | `81c42c6af743faca11df6aa4b8219e2ef6bb214a` |
| F5 likelihood/optimizer diagnostics | `7df6d4e679c909d79f4aa184918b75117f28f3c0` |
| F5 diagnostics tests | `3e54bc39cd36b4c24619354d031ef9e579f942a5` |
| Static workflow | `624370a438000809c7cc6b660fda126b77ced5de` |

The canonical branch head at validation was `e7920543e8c6fb19582c62446381df7cb1d95e1a`. `main` remained at `e22928eb79adb5bc74295967a45b9c440b78f849`.

## 6. Remaining implementation gates before resource preflight

### F1
- Build the frozen six-cell adversarial fixture matrix, including near-zero within sums, low/high between regimes and scale extremes.
- Add explicit multiple/tangential nuisance-root fixtures to the *interval-path* gate, not only the standalone polynomial diagnostic.
- Independently verify the score-polynomial and profile-likelihood identities against a separately coded likelihood/score oracle.
- Exercise boundary inclusion, endpoint bracketing/overflow and the connectedness argument over the full declared design roster.
- Preserve typed abstention for any mismatch.

### F5
- Integrate the optimizer audit into a separate diagnostic output for each fixed C5 fit without changing the existing interval calculation or C5 selection rule.
- Reconcile the fitted count likelihood and finite-R distribution with the existing exact beta-binomial PMF/moment oracle.
- Add boundary-adjacent score/Hessian tests and explicit weak-curvature/near-binomial cases.
- Ensure all starts and the independent optimizer result are serializable in the future per-dataset audit records.

### Shared
- Add static schema/manifest tests for diagnostic records and provenance.
- Re-run the static workflow on the final implementation commit and record exact hashes.
- Only then perform the bounded 100-dataset-per-representative-cell resource preflight under its own authorization.
- Do not request the 80,000-dataset development/calibration authorization until these gates and the resource preflight pass.

## 7. Prohibitions preserved

No Tier A v1.0 protocol, raw result, replay, authorization or audit was changed. No C0/C1/C5 interval definition was changed. No calibration cutoff was selected. No new method was promoted. No data from the unblinded Tier A holdout were reused. No scientific C10 execution was performed. No write was made to `main`.

**Final disposition:** A1/B1 deterministic implementation has advanced, with 110/110 static tests passing. The integrated development/calibration package remains OPEN and numerical execution remains unauthorized.
