# C10-S — F5 component profile-likelihood design review draft 001

**Date:** 2026-11-26  
**Status:** STATIC DESIGN REVIEW — NOT IMPLEMENTED / NOT CALIBRATED / NOT SELECTED  
**Branch:** \`research/c10s-instrumental-autonomous-workpackage-20261126\`  
**Predecessor diagnostic:** \`C10S_F5_M1_PCT_DEVELOPMENT_PILOT_RESULT_001.md\`

## 1. Purpose

Define the smallest next candidate worth a bounded static review after M1-PCT failed the frozen M10/R5 emission requirement. The candidate is a profile-likelihood confidence set for each actual F5 population functional:
- within functional \(W=\mu(1-\mu)\kappa/(\kappa+1)\);
- raw-between functional \(B=\mu(1-\mu)/(\kappa+1)\).

This document is a design derivation only. It does not implement intervals, select an LR cutoff, claim coverage, or authorize any calibration.

## 2. Existing assets to reuse

- \`c10s_f5_beta_binomial_likelihood_diagnostics.py\`: beta-binomial log-likelihood, analytic score/Hessian in \((\operatorname{logit}\mu,\log\kappa)\), independent \((\log\alpha,\log\beta)\) derivative route, optimizer audit, and explicit \(\kappa\to0\)/\(\kappa\to\infty\) likelihood limits.
- \`c10s_f5_beta_binomial_mcse_profile.py\`: a target-specific MCSE profile evaluator that already retains both mean branches, finite concentration limits, profile components/hull, grid-convergence diagnostics, and adversarial numerical tests. It is not a W/B interval method and cannot be relabelled as one.
- \`c10s_beta_binomial_variance_oracles.py\`: exact finite-R beta-binomial count PMF and exact finite-M moments/covariance for the W/B estimators. It is a truth/diagnostic oracle, not an interval or cutoff calibrator.
- Existing G7 exact global-MLE certificate and B2/B3/G7 historical records remain diagnostic/provenance assets only; no retrospective tuning on exposed data.

## 3. Constrained profile geometry

Let \(q=\mu(1-\mu)\in(0,1/4]\). Then:
\[
W=q\frac{\kappa}{1+\kappa},\qquad
B=q\frac{1}{1+\kappa},\qquad W+B=q.
\]

For a proposed within value \(w\in(0,1/4)\), the constraint implies:
\[
q_W(\kappa;w)=w\frac{1+\kappa}{\kappa}
=w+\frac{w}{\kappa},
\qquad
\kappa\ge \frac{w}{1/4-w}.
\]
For every feasible finite \(\kappa\), retain both mean branches:
\[
\mu_\pm(\kappa;w)=\frac{1\pm\sqrt{1-4q_W(\kappa;w)}}{2}.
\]
The lower feasible concentration endpoint has \(q=1/4\), \(\mu=1/2\); as \(\kappa\to\infty\), \(q\to w\) and the binomial limit must be evaluated explicitly.

For a proposed raw-between value \(b\in(0,1/4)\):
\[
q_B(\kappa;b)=b(1+\kappa),
\qquad
0<\kappa\le \frac{1}{4b}-1,
\]
with both branches
\[
\mu_\pm(\kappa;b)=\frac{1\pm\sqrt{1-4q_B(\kappa;b)}}{2}.
\]
The upper feasible concentration endpoint has \(q=1/4\), \(\mu=1/2\); as \(\kappa\to0\), \(q\to b\) and the two-point mixing limit must be evaluated explicitly.

The boundary targets \(w=0\) and \(b=0\), and degenerate mean boundaries \(\mu\to0,1\), require separately declared likelihood limits. They must not be approximated by arbitrary finite optimizer bounds. The endpoint \(W+B=1/4\) corresponds to \(\mu=1/2\); it is a joint feasibility boundary, not a reason to clip estimated endpoints silently.

## 4. Profile definition

For observed world counts \(x=(x_1,\ldots,x_M)\), define:
\[
\ell_W(w;x)=\sup_{\kappa\in\mathcal K_W(w),\,s\in\{-,+\}}
\ell\bigl(x;\mu_s(\kappa;w),\kappa\bigr),
\]
\[
\ell_B(b;x)=\sup_{\kappa\in\mathcal K_B(b),\,s\in\{-,+\}}
\ell\bigl(x;\mu_s(\kappa;b),\kappa\bigr).
\]
The supremum must include the applicable analytic concentration limits and feasible endpoints, not only finite grid points. The unrestricted likelihood maximum must be reconciled independently against the existing analytic-gradient fit and the independent log-shape derivative route. Neither multi-start optimizer success nor a finite grid alone certifies globality.

A candidate LR set would be
\[
\mathcal C_W(c)=\{w:2[\ell_{\max}(x)-\ell_W(w;x)]\le c\},
\quad
\mathcal C_B(c)=\{b:2[\ell_{\max}(x)-\ell_B(b;x)]\le c\}.
\]
Retain all connected components. A reported interval hull may be formed only if the frozen result contract explicitly allows it and its conservatism is measured; do not silently replace a disconnected set with a point estimate or drop a component.

## 5. Statistical issue: the LR cutoff is not supplied by this derivation

A nominal \(\chi^2_1\) cutoff must not be assumed. M10/R5 already exhibits weak concentration identification, boundary likelihood states and multiple numerical fit classifications. These conditions can invalidate a routine Wilks approximation or make it non-uniform across the frozen DGP cell.

The cutoff must be prospectively calibrated using development-only data, with an independent development-validation bank, before any fresh Tier-A holdout. Calibration must be component-wise (W and B, M10/R5 and M30/R20), unless a mathematically justified common cutoff is established. The design must report coverage, Wilson intervals, emission, interval width, directional misses, disconnected-set frequency, boundary frequency, numerical failures, runtime and endpoint Monte Carlo error. No pooled-cell rescue is permitted.

A possible calibration route is parametric simulation under constrained nuisance values with least-favourable or explicitly justified nuisance coverage. The nuisance search, DGP truth points, Monte Carlo precision, cutoff selection rule and validation split must be specified before running it. This route is not yet demonstrated feasible and may be computationally expensive.

## 6. Fail-closed numerical contract required before implementation

A future implementation must distinguish:
- finite interior nuisance maximum;
- \(\kappa\to0\) two-point boundary;
- \(\kappa\to\infty\) binomial boundary;
- \(\mu\to0\) or \(\mu\to1\) degenerate boundary;
- non-unique or disconnected nuisance maxima;
- grid/local-optimizer disagreement;
- unresolved global maximum;
- infeasible target value;
- non-finite likelihood or derivative.

No failed replicate/profile point may be silently dropped. Grid refinement must establish stable profile likelihood values, component count and endpoints. Both mean branches and both concentration limits must be tested. The independent log-shape route must be used as a cross-check, not substituted as a second estimator.

## 7. Minimum deterministic tests before any simulation

1. Algebraic constraint reconstruction: generated \((\mu,\kappa)\) maps back to exact W/B and both branch roots reconstruct the same q.
2. Feasibility boundaries: \(w,b\in[0,1/4]\), finite \(\kappa\) endpoints, \(W=0\), \(B=0\), and \(W+B=1/4\).
3. Analytic limits: binomial and two-point likelihood limits match independent direct calculations, including datasets with interior counts where the two-point limit is \(-\infty\).
4. Branch retention and count-reflection symmetry.
5. Profile maximum is not below the direct likelihood at any feasible known \((\mu,\kappa)\) point.
6. Independent derivative concordance in \((\eta,\xi)\) and \((\log\alpha,\log\beta)\).
7. Grid convergence for profile values, nuisance maximizers, connected components and endpoints.
8. Adversarial samples: all-zero, all-\(R\), endpoint mixtures, interior-heavy, asymmetric and near-binomial patterns.
9. Explicit unresolved/globality states; no confidence set emitted when the unrestricted or constrained maximum is not sufficiently reconciled.
10. Set topology and interval hull semantics tested, including empty, disconnected, one-sided and boundary-touching sets.

## 8. Go/no-go criteria for proceeding to development simulation

Proceed only if the static review and deterministic tests show:
- correct constrained geometry and analytic boundaries;
- independent likelihood/score agreement;
- stable profile maxima under grid refinement and multi-start nuisance search;
- no silent loss of branches or components;
- a credible, predeclared LR calibration/validation design;
- a plausible route to >=95% emission without redefining non-identification as a numerical success.

If the LR cutoff cannot be calibrated with adequate precision or if the profile set routinely remains unresolved in M10/R5, stop and report that the frozen Tier-A emission requirement is incompatible with the current candidate family. Do not weaken the acceptance thresholds.

## 9. Current disposition

**M2 component-profile likelihood:** DESIGN CANDIDATE ONLY — NOT IMPLEMENTED, NOT CALIBRATED, NOT SELECTED.  
**M1-PCT:** rejected for Tier-A under its current fail-closed fit contract due 4% M10/R5 emission.  
**Tier-A/Tier-B/C10 causal execution:** not launched and not authorized.


## 10. Repository code audit — reuse boundaries and numerical caveats

A direct source inspection was completed for the existing F5 assets.

### 10.1 Likelihood and derivative asset

\`c10s_f5_beta_binomial_likelihood_diagnostics.py\` already provides:
- the exact beta-binomial count log-likelihood and analytic score/Hessian in \((\operatorname{logit}\mu,\log\kappa)\);
- an independently parameterized analytic score/Hessian in \((\log\alpha,\log\beta)\);
- explicit pointwise likelihood limits at \(\kappa\to0\) and \(\kappa\to\infty\);
- multi-start bounded L-BFGS-B and independent BFGS diagnostics.

But its unrestricted audit is not a global-MLE certificate. The primary optimizer is bounded to \(\eta\in[-18,18]\), \(\log\kappa\in[-12,18]\), and the independent BFGS success flag plus likelihood agreement does not prove a global maximum or exclude all boundary/interior alternatives. The code is suitable as a derivative/optimizer diagnostic and cross-check, not as the sole source of \(\ell_{\max}\) for an LR confidence set.

### 10.2 Existing MCSE profile asset

\`c10s_f5_beta_binomial_mcse_profile.py\` is a valuable numerical pattern, not a reusable W/B interval engine:
- it retains both mean branches and evaluates analytic \(\kappa\to0\) and \(\kappa\to\infty\) likelihood limits;
- it scans finite concentration grids, refines detected local maxima, and adds a Powell multi-start cross-check;
- its finite numerical domain is nevertheless truncated (log-concentration bounds are derived using ±24 offsets), so it is not a proof that no optimum or topology lies farther into a tail;
- its confidence-set inversion detects components from a finite target grid and refines crossings; the implementation explicitly says it cannot certify global topology, and its grid-convergence check cannot detect a component missed by both grids.

Consequently, neither its profile optimiser nor its LR inversion should be copied as a certified M2 solution. Its branch handling, analytic-limit treatment, result diagnostics and test fixtures can be adapted after replacing the tail truncation and strengthening topology/globality controls.

### 10.3 Exact finite-R oracle

\`c10s_beta_binomial_variance_oracles.py\` computes the exact beta-binomial count PMF and finite-M moments/covariance for the W and raw-B estimators. It does not provide likelihood intervals or an LR cutoff. It should remain an independent truth and moment oracle for later coverage studies.

## 11. Compactification of the nuisance search

A better numerical parameterization avoids arbitrary finite log-\(\kappa\) truncation for each fixed target.

For \(W=w\), define \(t=1/(1+\kappa)\). The feasible range is compact:
\[
0\le t\le t_{\max}(w)=\frac{1}{1+\kappa_{\min}(w)},\quad
\kappa_{\min}(w)=\frac{w}{1/4-w}.
\]
The endpoint \(t=0\) is the analytic binomial limit; \(t=t_{\max}\) is \(\mu=1/2\). Interior points reconstruct \(\kappa=(1-t)/t\), \(q=w/(1-t)\), and both mean roots.

For \(B=b\), define \(s=\kappa/\kappa_{\max}(b)\), where \(\kappa_{\max}(b)=1/(4b)-1\). Then \(0\le s\le1\); \(s=0\) is the analytic two-point limit and \(s=1\) is \(\mu=1/2\). Interior points reconstruct \(\kappa=s\kappa_{\max}\), \(q=b(1+\kappa)\), and both mean roots.

This compactifies the *mathematical domain*, but does not by itself certify a numerical maximum. A robust evaluator must include both endpoints analytically, retain both branches, detect and refine every grid-detected local maximum, perform adaptive grid refinement, and return an unresolved status if maxima, branch winners or endpoint values are not stable. The compactified coordinate also needs careful endpoint evaluation to avoid floating-point overflow in \(\kappa=(1-t)/t\).

## 12. Revised implementation gate

Before coding the M2 evaluator, the implementation contract must specify:
1. compactified nuisance coordinates above and analytic endpoint evaluation;
2. stable beta-binomial log-likelihood evaluation near both limits (without replacing a limit by a large/small finite \(\kappa\));
3. independent direct-likelihood and derivative checks at interior points;
4. adversarial profile fixtures where both branches compete, and where a maximum occurs at either concentration boundary;
5. adaptive refinement criteria for profile value, maximizing nuisance coordinate, branch identity and all detected local maxima;
6. an explicit \`GLOBALITY_UNRESOLVED\` result whenever refinement or independent checks disagree;
7. a separate unrestricted maximum reconciliation, not merely the bounded optimizer output from the existing diagnostic;
8. LR inversion that preserves all components and abstains if adaptive target-grid refinement cannot establish stable topology.

**Important:** this review found no existing F5 W/B profile-likelihood implementation. The MCSE profile is a separate estimand. M2 remains design-only until these contracts are encoded and tested.
