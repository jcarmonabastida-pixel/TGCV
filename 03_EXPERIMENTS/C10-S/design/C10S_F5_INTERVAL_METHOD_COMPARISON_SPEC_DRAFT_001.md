# C10-S — F5 comparative interval-method specification draft 001

**Record:** C10S-F5-INTERVAL-METHOD-COMPARISON-SPEC-001  
**Status:** D1 REVIEW CANDIDATE — NOT FROZEN / PARTIAL EXACT ALGEBRA PRIMITIVE IMPLEMENTED / GLOBAL CERTIFICATION NOT IMPLEMENTED / NOT EXECUTED  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Parent design:** `C10S_F5_INTERVAL_METHOD_COMPARISON_DESIGN_DRAFT_001.md`  
**Frozen parent specification:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md`, v1.0, unchanged  
**Historical evidence:** Tier A/B2/B3 and run `44615173745`, artifact `14586221304`  
**Execution authorization:** NONE  
**Decision:** no interval method selected or validated

---

## 1. Purpose and governance relationship

This document advances D0 into a D1 review candidate for a **separate, successor F5 method-comparison work package**. It does not amend, supersede or reinterpret frozen specification v1.0.

The parent v1.0 package remains authoritative for its defined F1 and F5 work. In particular, its F5 Phase B is explicitly limited to diagnosis of the existing C5 fitted beta-binomial percentile procedure against unchanged C0; it states that no alternative F5 interval method is selected in that package. This draft respects that boundary by proposing a separately versioned successor package, with fresh data and its own future authorization.

No new F5 method is implemented or executed by this document. No B2/B3 record, seed, output, gate or adjudication is reused for selection or tuning. Historical B2/B3 data are retained only as labelled development evidence and deterministic regression fixtures where already permitted by v1.0.

The successor package is restricted to the same frozen F5 beta22 DGP and the two original design cells:
- M10/R5;
- M30/R20.

It does not add stress families, misspecification cells, new targets, MCSE intervals, Tier B, or C10 Generator/Analyzer/Evaluator execution.

## 2. Frozen scientific target and estimators

Let independent world probabilities satisfy (p_m\sim\mathrm{Beta}(\alpha,\beta)), and let the R Bernoulli contributions within each world be conditionally independent given (p_m).

Define:
- \(\mu=\alpha/(\alpha+\beta)\);
- \(\kappa=\alpha+\beta\);
- \(W(\mu,\kappa)=E[p(1-p)]=\mu(1-\mu)\kappa/(\kappa+1)\);
- \(B(\mu,\kappa)=\operatorname{Var}(p)=\mu(1-\mu)/(\kappa+1)\).

The population coverage truths remain \(\sigma_w^2=W\) and \(\sigma_b^2=B\). Under the frozen beta22 DGP, these are 0.20 and 0.05 respectively.

The frozen C5 sample statistics remain:
- \(T_W=MSW\);
- \(T_B=S^2_{\bar q}-MSW/R\), untruncated.

Negative raw-between estimates and interval endpoints remain admissible. No candidate may clip, truncate, project to positive-only samples, or silently replace the frozen raw-between target.

The comparison deliberately distinguishes **method/estimator packages**:
- M0 intervals are centered on/distributed from the frozen raw sample statistics.
- M1 estimates W/B through replicate-specific beta-binomial MLE functionals.
- M2 obtains confidence sets for W/B by inverting the beta-binomial likelihood.

All candidates are scored against the same population truths. A comparison must not be described as an interval-only comparison when its point-estimator construction differs.

## 3. Candidate roster and proposed roles

### M0 — frozen C5 fixed-parameter plug-in bootstrap

- Exact current C5 method ID and point-statistic semantics are retained.
- Fit \((\alpha,\beta)\) once to the observed dataset.
- Generate all bootstrap worlds under this fixed fitted pair.
- Recompute the frozen raw sample statistics and percentile intervals.
- Do not change the existing production implementation or historical results.

Role: incumbent comparator. Historical B2/B3 show that it fails the frozen component gates; a fresh successor bank can quantify paired performance but cannot erase that result.

### M1 — refitted parametric bootstrap of fitted population functionals

For each original dataset:
1. Fit the beta-binomial likelihood using a versioned fit contract.
2. Compute \(\hat W=W(\hat\theta)\) and \(\hat B=B(\hat\theta)\).
3. Generate complete nested datasets under \(\hat\theta\), preserving M, R and the frozen hierarchy.
4. Refit the beta-binomial model in every bootstrap replicate using the same fit contract.
5. Retain replicate-specific \(\hat W_b^*,\hat B_b^*\) and every raw fit state.
6. Construct the interval variants below.

**Proposed primary: M1-PCT.** Percentile intervals from the empirical distributions of \(\hat W_b^*\) and \(\hat B_b^*\). This is preferred as the initial primary candidate because the fitted functionals remain in their natural feasible range when every replicate fit is admissible; it does not require clipping an unconstrained basic interval back into the parameter space.

**Prespecified secondary diagnostic: M1-BASIC.** Let \(\Delta_W^*=\hat W_b^*-\hat W\) and \(\Delta_B^*=\hat B_b^*-\hat B\). Form basic intervals \([\hat W-q_{W,U},\hat W-q_{W,L}]\) and \([\hat B-q_{B,U},\hat B-q_{B,L}]\). These may extend beyond the feasible parameter range. Do not clip them. Report feasibility violations and coverage without repairing endpoints.

M1-PCT is a proposal, not a frozen choice. D1 review must confirm that the different estimator package is acceptable as a candidate and that the MLE fit contract is sufficiently defined.

### M2 — profile-likelihood confidence sets for W and B

For each target \(\psi\in\{W,B\}\), define:
\[
\ell_p(\psi_0)=\sup_{\theta:\psi(\theta)=\psi_0}\ell(\theta),
\qquad
D(\psi_0)=2\{\ell(\hat\theta)-\ell_p(\psi_0)\}.
\]

Retain the full accepted set over the feasible target range, including disconnected components. Do not replace disconnected sets with a single convex hull for primary scoring. If a display-only hull is supplied, label it secondary and score the actual union.

The constrained profile has an exact one-dimensional nuisance reduction that should be used instead of a generic two-dimensional constrained optimizer. Since
\\[
q=W+B=\\mu(1-\\mu),\\qquad \\kappa=W/B,
\\]
for a fixed W=w, profile over the complementary component b=B in \\(0\\le b\\le0.25-w\\), set \\(q=w+b\\), \\(\\kappa=w/b\\), and evaluate both mean branches
\\[
\\mu_\\pm=\\frac{1\\pm\\sqrt{1-4q}}{2}.
\\]
For a fixed B=b, profile analogously over w=W in \\(0\\le w\\le0.25-b\\), with the same q, κ and two μ branches. Each branch maps to \\(\\alpha=\\mu\\kappa\\), \\(\\beta=(1-\\mu)\\kappa\\). The likelihood is evaluated on both branches; symmetry must not be assumed for an observed count vector.

This reduces each target profile to a bounded one-dimensional search over the complementary variance component, plus explicit endpoint limits. It does not by itself prove globality: all stationary regions and both branches must be traced, and the endpoints must be evaluated analytically. The corners (W=B=0), W=0 (κ→0), B=0 (κ→∞), and q=0.25 (μ=0.5) require explicit limiting evaluation. If the one-dimensional global maximum or accepted-set topology cannot be certified, M2 abstains.

Two variants:
- **M2a — asymptotic LR reference:** use the regular \(\chi^2_1\) cutoff only as a diagnostic reference. It is not eligible for acceptance where weak identification, boundary nonregularity, incomplete global maximization or unresolved profile topology is present.
- **M2b — beta22/design-cell calibrated LR:** calibrate the LR cutoff separately for W and B in each of M10/R5 and M30/R20 using a new calibration bank generated from the frozen beta22 DGP. For each calibration dataset, calculate the LR statistic at the known population target; the truth is used only for calibration, never in fitting or profile inversion. Use an upper tolerance order statistic with simultaneous one-sided confidence at least 95% across the four target × design cutoffs (Bonferroni family-wise control). Apply the frozen cutoffs to a separate validation bank without retuning.

M2b's scope is explicitly bounded to the two beta22 design cells. It does not imply uniform coverage over a continuum of beta-binomial parameters or under model misspecification.

## 4. Fit-state and boundary contract — unresolved D1 blocker

The existing B1 evidence requires retention of all three production starts, comparison with the analytic-gradient path and independent optimizer, and separation of optimizer termination from statistical identification. It does not require all three starts to report success. The historical runner's all-starts-success Boolean is not itself the frozen scientific rule, but removing it without a defensible replacement is also prohibited.

Every fit in M1 and every constrained/unconstrained fit in M2 must retain:
- all start vectors and terminal vectors;
- termination flags/messages and objective values;
- analytic score norm and independent score check;
- Hessian/observed-information or profile-curvature diagnostics;
- distances to finite numerical bounds;
- direct production/analytic likelihood and parameter comparisons;
- boundary-limit likelihood comparisons;
- typed terminal state and exact abstention reason.

Minimum mutually exclusive states:
- `INTERIOR_IDENTIFIED_CANDIDATE`;
- `THEORETICAL_BOUNDARY_LIMIT`;
- `WEAK_IDENTIFICATION_OR_FLAT_PROFILE`;
- `MULTISTART_OR_OPTIMIZER_DISAGREEMENT`;
- `NUMERICAL_TERMINATION_UNRESOLVED`;
- `NO_ADMISSIBLE_FIT`;
- `NUMERICAL_EXCEPTION`.

A finite optimizer bound is never a theoretical model boundary. The theoretical limits \(\kappa\to\infty\) and \(\kappa\to0\) must be evaluated as limits where mathematically supported. A boundary state may be accepted only if the limiting likelihood is evaluated independently and its global status is established; otherwise it is unresolved.

**D1 resolution — analytical route designed, implementation feasibility still OPEN:** the separate artifact `C10S_F5_GLOBAL_MLE_CERTIFICATION_DESIGN_001.md` derives strict conditional concavity in μ at fixed κ and an exact rational-score/resultant/Sturm route to enumerate all finite interior stationary points, preserve multiplicity, isolate near-coincident roots and compare them with profiled theoretical boundaries. This replaces the proposed arbitrary scale-aware likelihood-difference threshold. It is not yet implemented or validated. D1 therefore remains OPEN until exact polynomial construction, root isolation, interval likelihood ordering, boundary strata and resource ceilings pass deterministic adversarial fixtures. Until then M1/M2 must abstain whenever globality is not certified. Optimizer starts remain diagnostic; neither at least one nor all starts succeeding is a global certificate.

## 5. Bootstrap failure and emission semantics — proposed fail-closed rule

No bootstrap replicate may be silently dropped, redrawn, replaced, or treated as if it were successful.

For M1, preserve the requested replicate count and one terminal state per replicate. A dataset-level interval is emitted only if all required replicate contributions are mathematically defined under the frozen fit contract. If any replicate is unresolved and no valid boundary contribution has been formally specified, the dataset abstains. Report failure counts and reasons; no complete-case bootstrap distribution is allowed.

For M2b calibration, a calibration dataset with unresolved global MLE/profile state is not silently removed. The calibration procedure must either produce a valid LR statistic under the frozen boundary contract or mark the calibration cell blocked. It must not lower the cutoff by deleting difficult cases.

For M2 inversion, any unresolved profile segment, unbracketed endpoint or unverified global maximum causes a typed profile abstention. Disconnected accepted regions are retained as unions.

This rule is deliberately conservative. Its operational emission consequences must be measured in deterministic tests and then prospectively; it cannot be weakened after observing coverage.

## 6. Matched prospective evaluation

### 6.1 Banks and data separation

A new successor package requires fresh, disjoint banks. No B2/B3 seed, dataset, bootstrap stream or outcome may enter them.

Proposed bounded design:
- M10/R5 and M30/R20, beta22 only;
- 5,000 independent datasets per cell for method development/validation, with the exact split between calibration and validation specified below;
- a distinct M2b cutoff-calibration bank, separate from all method-comparison evaluation datasets;
- independent random-stream namespaces for dataset generation, M0 bootstrap, M1 bootstrap and M2b calibration;
- immutable manifests and hashes, with seed derivation including protocol version, namespace, cell and dataset index.

For a coverage estimate near 0.95, N=5,000 gives descriptive MCSE approximately 0.0031. This motivates a provisional 5,000 datasets per cell in each development and development-validation bank; it is not a guarantee of acceptance or a copied historical sample size. D1 must calculate exact Wilson/precision operating characteristics before freezing N. The separate M2b cutoff-calibration bank has a different purpose and its size must be derived from the simultaneous tolerance requirement, not assumed to be 5,000.

A separate confirmatory bank is not part of this successor development package. It would require a further frozen method and a new authorization.

### 6.2 Paired method comparison

On each common evaluation dataset, run M0, M1-PCT, M1-BASIC and M2a; run M2b after its cutoff has been calibrated independently. Retain the same dataset ID, raw input hash, DGP truth and method roster.

M0 is rerun only on the new prospective datasets as a matched comparator. This is not a replay of B2/B3 and cannot alter their historical adjudication.

### 6.3 Outcomes

For each method × cell × target:
- conditional coverage and two-sided 95% Wilson interval;
- unconditional usable-and-covering rate;
- interval/set emission and abstention rate;
- lower- and upper-tail misses;
- interval width (for disconnected sets, total measure of the union);
- endpoint/set boundary frequency;
- estimator bias and RMSE where a point estimate exists;
- optimizer/profile terminal-state frequencies;
- MCSE for coverage and interval quantiles;
- runtime and peak memory.

No pooling across M/R cells or W/B targets. Joint W/B coverage may be reported as a secondary outcome, never as a replacement for marginal component gates.

## 7. Acceptance gates inherited from frozen v1.0

For each M/R cell × bank × target, retain the complete frozen component gate:
- conditional coverage in [0.93, 0.97];
- two-sided 95% Wilson interval contains 0.95;
- interval emission at least 0.95;
- no unresolved numerical optimizer state;
- no truth, denominator, method-roster or provenance mismatch;
- no raw-between truncation or positive-only conditioning.

These are development eligibility gates, not confirmatory claims. They are not relaxed by the new package. M2's set-valued regions are scored by membership of the truth in the union; their total measure is reported for efficiency.

Abstentions are not counted as covered and are not deleted from the operational denominator. Report both conditional coverage among emitted intervals and unconditional usable-and-covering rate. The frozen emission gate applies separately.

No method is selected if any required cell/target fails. C0 is not an accepted fallback. MCSE interval construction remains an explicit abstention.

## 8. Monte Carlo precision and computational feasibility — D1 blockers

The following exact calculations have now been completed analytically for the provisional N=5,000:
- At nominal coverage 0.95, the descriptive coverage MCSE is \\(\\sqrt{0.95\\cdot0.05/5000}=0.003082\\).
- Under the inherited joint gate (point coverage in [0.93,0.97] and 95% Wilson interval containing 0.95), the admissible integer success-count range is 4,720–4,780 inclusive (observed coverage 0.944–0.956). The Wilson condition is materially stricter than the point-coverage band near its edges.
- For M2b's four simultaneous cutoffs (W/B × M10/R5 and M30/R20), Bonferroni assigns one-sided error 0.05/4=0.0125 per cutoff. With Kcal=5,000, the upper tolerance order-statistic rank is provisionally k=4,785; P{Binomial(5000,0.95) ≤ 4784}=0.988711, exceeding the required per-cutoff confidence 0.9875 and yielding family-wise confidence at least 0.95 by Bonferroni.

Before D1 freeze:
1. independently verify and unit-test the Wilson and order-statistic calculations, including off-by-one rank conventions;
2. set bootstrap replicate counts for M1 from a prespecified endpoint Monte Carlo error target;
3. set M2 profile grid/bracketing tolerances and constrained-optimizer start policy using deterministic numerical analysis;
4. establish a compute ceiling and worst-case runtime/memory budget from static deterministic microbenchmarks after the implementation contract is frozen;
5. define stop rules for calibration failure, profile topology failure and resource-budget exceedance.

No numeric bootstrap B, M2 profile grid density, runtime ceiling or memory ceiling is declared here because no measured benchmark or endpoint-MCSE analysis is yet available. These are blocking fields, not permission to choose them during execution.

## 9. Shared implementation architecture

Do not build three parallel likelihoods or data generators. Reuse the existing canonical F5 likelihood, exact finite-R oracle, nested-data generator and comparison interfaces. Add only the minimum shared contracts:

- `F5FitResult`: complete start roster, selected parameters, likelihood, score/curvature, boundary comparison, terminal state.
- `F5TargetFunctional`: W/B and feasible ranges.
- `F5ProfileResult`: target grid/brackets, nuisance optimizer states, accepted-set components, topology and terminal state.
- `F5BootstrapReplicateRecord`: seed/stream, generated-data digest, fit result, W/B functionals and terminal state.
- `F5IntervalResult`: interval or union of sets, method/version, target, emission/abstention, numerical diagnostics and MCSE.
- `F5MatchedMethodRecord`: common dataset ID/hash, truths, all method outputs and provenance.

M0 must be wrapped, not rewritten. M1 must reuse the frozen likelihood and fit diagnostics. M2 must reuse the same likelihood and fit contract for unconstrained and constrained optimization. Any alteration to the frozen C5 production estimator is out of scope and requires its own versioned decision.

## 10. Deterministic validation before any numerical bank

Required deterministic contracts:
1. analytic W/B identities and W+B=μ(1−μ);
2. parameterization invariance between (α,β) and (η,λ);
3. exact κ→0, κ→∞ and μ→0/1 limit checks;
4. M0 bitwise/contract reproduction on existing fixed fixtures;
5. M1-PCT and M1-BASIC quantile calculations on hand-constructed replicate arrays, including boundary-support and out-of-range basic endpoints;
6. M1 refit invocation and one terminal record per requested replicate;
7. injected failed-start, optimizer-disagreement, theoretical-boundary and numerical-exception paths;
8. proof that no failed replicate is silently omitted or replaced;
9. M2 one-dimensional profile reduction is checked against direct parameterization on analytic fixtures; constrained profile optimum never exceeds the verified unconstrained global maximum beyond a justified scale-aware tolerance;
10. M2 disconnected-set preservation, boundary inclusion, unbracketed endpoint and unresolved-topology abstention;
11. exact M2b order-statistic rank and simultaneous confidence calculation;
12. coverage/Wilson/MCSE/abstention denominator bookkeeping;
13. deterministic stream separation, serialization and provenance.

The deterministic suite does not establish statistical coverage. No Monte Carlo or bootstrap bank is authorized by passing these tests.

## 11. Integrated gates and sequence

| Gate | Work | Exit condition | Current status |
|---|---|---|---|
| D0 | Comparative design | Target mapping and candidates reconstructed | COMPLETE AS DRAFT |
| D1 | Method specification | Fit-state rule, M1/M2 procedures, precision and cost fields resolved; review against v1.0 | REVIEW CANDIDATE — OPEN |
| D2 | Static implementation | Shared interfaces and deterministic adversarial tests | PARTIAL RESEARCH PRIMITIVES — exact sparse score numerators, concentration compactification, Bernstein conversion/exclusion, de Casteljau subdivision and bounded exclusion controller; tests committed but not governed-executed; root inclusion/uniqueness and algebraic elimination/isolation absent |
| D3 | Static/resource preflight | Exact commit, dependency lock, deterministic microbenchmarks and resource report | NOT STARTED |
| D4 | Execution authorization | Separate one-use authorization bound to protocol/code/seeds/budget | NONE |
| D5 | Prospective development | New calibration/evaluation banks and full per-cell audit | NOT AUTHORIZED |
| D6 | Method freeze | Select method or no validated method using only development data | NOT STARTED |
| D7 | Confirmatory design | Separate fresh holdout and authorization | NOT STARTED |

No gate passes implicitly. Completion of D2/D3 does not authorize D5.

## 12. Explicit open blockers for D1 review

1. Select and validate a feasible global stationary-point backend. Exact sparse integer rational-score numerator construction is now implemented and passes deterministic tests, but generic exact rational and generic finite-field PRS resultants both exceeded the 60-second M30/R20 sizing ceiling. Compare a purpose-built modular subresultant/CRT implementation against an interval-certified one-dimensional profile method; do not assume either is feasible until tested.
2. Extend the selected global certification primitive to constrained M2 one-dimensional profiles, including endpoint limits and disconnected accepted-set topology. The current F1 Sturm isolator has a degree ceiling of three and cannot be reused unchanged for F5.
3. Exact M2b calibration rank calculation for four cutoffs and the corresponding bank size/precision.
4. Exact M1 bootstrap replicate count from an endpoint-MCSE target.
5. Wilson operating-characteristic calculation and confirmation of N=5,000 or a justified alternative.
6. Static compute ceiling and stopping policy, based on measured deterministic benchmarks.
7. Whether the no-unresolved-state gate is applied to every internal bootstrap/profile subfit or to the emitted dataset-level fit after a formally justified state aggregation. No unresolved state may be hidden.

These are technical/statistical blockers to be resolved by analysis and deterministic fixtures. They are not user preference questions and must not be settled by post-hoc inspection of prospective coverage.

## 13. Current disposition

- Frozen parent specification v1.0: unchanged and operative.
- M0/C5: implemented and historically executed; failed frozen F5 component gates.
- M1-PCT: proposed primary candidate; not implemented/executed/validated.
- M1-BASIC: prespecified secondary diagnostic proposal; not implemented/executed/validated.
- M2a: asymptotic diagnostic reference only.
- M2b: proposed design-cell-calibrated profile candidate; not implemented/executed/validated.
- C0: historical/matched diagnostic comparator only; not an accepted fallback.
- Historical B2/B3: immutable development evidence; prohibited for new method selection/tuning.
- D1: REVIEW CANDIDATE / OPEN because fit-state adjudication, M2 global-profile certification, precision and cost fields remain unresolved.
- Execution: NOT AUTHORIZED.

**Next operation:** continue the bounded backend comparison using the tested sparse score numerators as common input: purpose-built modular subresultant/CRT versus interval-certified one-dimensional profile isolation. Require identical M30/R20 fixtures and adversarial even-multiplicity/near-coincident-root cases under fixed resource ceilings. The score-numerator helper is a preliminary research primitive only; it does not mean D2 is complete or D1 is closed. Then extend the selected certificate to constrained M2 profiles and close precision/cost/emission semantics. No numerical bank, replay, calibration or scientific execution is authorized.


### Modular backend feasibility refinement (2026-11-20)

See `diagnostics/C10S_F5_MODULAR_BACKEND_FEASIBILITY_NOTE_001.md`. On the deterministic M30/R20 score-numerator fixture, the sparse Sylvester pattern has a 79×79 determinant. A maximum-weight perfect matching using each nonzero entry's degree in kappa gives a rigorous determinant-term degree upper bound of 3,501 (versus the coarse dense bound 3,862). This is not the actual resultant degree. Full evaluation/interpolation to that bound would require up to 3,502 evaluations per good prime before CRT and is not yet an acceptable implementation strategy.

Generic SymPy PRS over GF(p)[kappa] also exceeded the 60-second tool ceiling. The next modular candidate must exploit sparse subresultant/degree-drop structure rather than merely changing the coefficient field. D1 remains OPEN; D2 remains a partial exact score-construction primitive only.


## 13. Compactified concentration coordinate — implementation status (2026-11-20)

The research harness now has exact sparse score numerators and an exact coordinate transformation
\[
t=\frac{\kappa}{1+\kappa},\qquad
\widetilde P(\mu,t)=(1-t)^dP\!\left(\mu,\frac{t}{1-t}\right),
\quad d=\deg_\kappa P.
\]
This maps finite positive concentration to \(0<t<1\) and preserves the interior zero set because the multiplier is strictly positive there. The two endpoints are not finite concentration candidates: they encode the already-required \(\kappa\to0\) and \(\kappa\to\infty\) boundary strata and must be compared using their analytic likelihood limits.

The implementation and new deterministic exact-rational tests are committed in:
- `harness/c10s_f5_rational_score_polynomials.py`
- `harness/test_c10s_f5_rational_score_polynomials.py`

The added tests cover exact M30/R20 score identities and the compactification identity/root correspondence. They are committed but not yet executed under the governed CPython 3.12 environment. This is preprocessing only, not a root certificate.

**Backend decision remains OPEN.** The next comparison must use the compactified exact numerator pair as common input. The modular route must prove its modular reconstruction bound and independently verify the reconstructed result; the interval route must certify exhaustive coverage of the open square, including even-multiplicity stationary points, and abstain on unresolved boxes. Both must separately handle t=0, t=1, mu=0 and mu=1 strata. No backend is selected by this coordinate transformation alone.


## 14. Exact Bernstein range-enclosure primitive — implemented, tests committed (2026-11-20)

The shared F5 algebra harness now includes:
- `bernstein_coefficients_on_box(P, mu_bounds, t_bounds)`: exact tensor-product power-to-Bernstein conversion after rational affine mapping of an arbitrary rectangular box into the unit square;
- `bernstein_sign_excludes_zero(coefficients)`: returns true only when every exact Bernstein coefficient is strictly positive or every coefficient is strictly negative.

By the Bernstein convex-hull property, the polynomial then has that strict sign throughout the closed box, so the box cannot contain a zero of that score numerator. For a two-score system, exclusion by either score is sufficient to rule out a common stationary point in the box. Mixed-sign coefficients are inconclusive and must trigger subdivision or a different certification step; they are never treated as evidence that a root exists.

Four deterministic tests were added for:
1. exact coefficients and exclusion of a strictly positive polynomial on the unit square;
2. exact rational affine-box substitution and strict-sign exclusion;
3. mixed-sign coefficients remaining inconclusive;
4. rejection of a degenerate box.

The affine-box expected coefficients were independently checked with exact Fraction arithmetic and corrected before commit. These are committed tests, not a claim that the repository suite has run under CPython 3.12. The current GitHub integration does not provide a workflow-dispatch operation in this session, so no new CI execution is claimed.

### Scope and limitations

This is the first concrete interval-route primitive, complementary to the exact score construction and concentration compactification. It provides rigorous *zero exclusion* on a box. It does not isolate or prove existence/uniqueness of a root, certify a root when Bernstein coefficients have mixed signs, or establish exhaustive coverage of the open square. A complete interval backend still needs deterministic subdivision, exact stopping/resource semantics, and a root-inclusion/uniqueness certificate (for example, a rigorously implemented interval-Newton/Krawczyk step) plus explicit boundary-stratum likelihood adjudication.

No modular resultant backend is selected, no MLE is certified, and no scientific execution or bank generation has occurred.



## 15. Exact de Casteljau subdivision primitive — implemented, tests committed (2026-11-20)

The shared F5 harness now adds:
- `bernstein_subdivide(coefficients, axis)`: exact midpoint subdivision of a tensor-product Bernstein coefficient matrix along `mu` or `t`, using rational de Casteljau recurrences;
- `bernstein_box_excludes_zero(coefficients)`: an explicitly box-scoped name for the strict-sign exclusion predicate.

The split is exact: the left/right coefficient matrices describe the two half-boxes, and their shared boundary coefficients agree. This avoids repeating the power-to-Bernstein affine conversion for every child box. It is a subdivision kernel, not yet an adaptive search/controller.

Four new deterministic unit tests have been committed: exact univariate split along each axis, a bivariate shared-edge identity, and invalid-axis/nonrectangular-input rejection. They are committed but **not executed** in the governed CPython 3.12 environment. No PASS is claimed.

### Required adaptive-controller contract

The next implementation must be a deterministic breadth-first or depth-first controller with a fully specified, stable ordering; fixed axis-selection rule; exact rational box endpoints; and hard ceilings for processed boxes, maximum depth, coefficient bit length and wall-clock-independent operation counts. It must apply exclusion to both score polynomials and discard a box only when at least one polynomial has a strict one-sign Bernstein coefficient array. Mixed signs, zeros among coefficients, and failed inclusion tests remain unresolved and are subdivided or explicitly returned as unresolved.

The controller must cover the compactified closed square while distinguishing its interior from the four boundary strata. Boundary roots at `mu=0/1` or `t=0/1` must not be reported as finite interior stationary points; their likelihood limits are adjudicated by the separate boundary contract. A root box touching a boundary cannot be silently promoted to an interior root.

For simple roots, a rational Krawczyk/interval-Newton inclusion test may certify existence and uniqueness only when its interval hypotheses are satisfied. In particular, a nonsingular rational preconditioner, a strict inclusion in the box interior, and a verified contraction/regularity condition must be checked using outward-safe exact rational interval bounds. The implementation must not infer uniqueness from inclusion alone without its theorem's hypotheses.

A multiple root has singular Jacobian in the usual system formulation and may defeat ordinary Krawczyk inclusion. Such a box must remain represented and be handled by a multiplicity-aware/deflation method or terminate as typed unresolved. It must never be excluded by a sign-change heuristic. A bounded computation that cannot separate or certify all remaining boxes returns abstention, not a partial global certificate.

The exact algebraic and interval routes remain parallel candidates. This primitive does not select either route, close D1, certify an MLE, authorize D2 completion, or authorize any statistical/scientific execution.



## 16. Deterministic Bernstein exclusion controller — implemented, tests committed (2026-11-20)

The harness now provides `bernstein_exclusion_subdivision(P,Q,...)`. It starts from an exact rational rectangle, uses a FIFO breadth-first queue, alternates split axes deterministically by depth (`mu`, then `t`), and applies the strict-sign exclusion predicate to both score polynomials on every processed box. Child Bernstein matrices are produced by the exact de Casteljau kernel; child endpoints are rational midpoints.

The controller has explicit `max_boxes` and `max_depth` ceilings and returns typed outcomes:
- `ALL_BOXES_EXCLUDED`: every box in the initial closed rectangle was excluded by at least one score;
- `UNRESOLVED_BOXES`: at least one box reached the depth ceiling;
- `RESOURCE_LIMIT_WITH_REMAINDER`: the box budget was reached and unprocessed boxes are retained in the result.

The returned record includes processed/excluded counts and every unresolved or unprocessed box with exact bounds, depth and state. No remaining box is silently dropped. The controller does not certify root existence, multiplicity, uniqueness, or the likelihood maximum. `ALL_BOXES_EXCLUDED` is the only result that proves no common zero in the covered closed rectangle.

Four further deterministic tests are committed: root-free exclusion, retention of a known common-root box, fail-closed box-budget exhaustion, and invalid-budget rejection. They have **not** been executed under governed CPython 3.12. No PASS is claimed.

### Important scope boundary

The current controller conservatively covers the closed compactified square. It therefore may retain boundary-root boxes even when the open finite-parameter domain has no corresponding interior root. This is safe but can be inefficient. A later boundary-aware controller may partition/classify `mu=0`, `mu=1`, `t=0`, and `t=1` explicitly, but may not discard a boundary-adjacent box without a proof that its interior contains no common zero.

The adaptive controller is an exhaustive *exclusion* mechanism only. Any non-excluded boxes still require root inclusion/uniqueness or a typed unresolved result. In particular, even-/odd-multiplicity roots are retained because no sign-change criterion is used; singular multiple-root boxes may remain unresolved under ordinary Krawczyk inclusion.

D1 remains OPEN; the modular and Bernstein routes remain parallel. No backend is selected, no MLE is certified, and no scientific execution is authorized.


### Additional adversarial retention fixtures (2026-11-20)

Two further deterministic tests now exercise a common even-multiplicity root and two distinct common roots separated by exactly `2^-20`. Their purpose is deliberately limited: the exclusion controller must not return `ALL_BOXES_EXCLUDED` for either fixture. They do not establish root inclusion, uniqueness, multiplicity recovery, or successful isolation. The controller should retain unresolved boxes until a later inclusion/deflation layer is available. Both tests are committed and remain unexecuted under governed CPython 3.12.

### Exact-input hardening — implemented, execution pending (2026-11-20)

The Bernstein entry points now reject binary floating-point values rather than silently converting them through `Fraction(float)`. Bounds accepted by the box conversion and adaptive controller must be exact integers or `Fraction` values; coefficient matrices passed to sign exclusion and de Casteljau subdivision follow the same rule. The empty-polynomial path validates the rectangle before returning its zero coefficient matrix. Four adversarial tests were added for float bounds, float coefficient matrices, controller bounds, and invalid bounds with an empty polynomial.

These are static implementation changes only. The tests have not been run in governed CPython 3.12. No PASS is claimed. The adaptive controller still covers the closed compactified rectangle; boundary strata remain separately unresolved, and no root inclusion/uniqueness certificate exists.

### Fixture contract correction — integer-scaled root polynomials (2026-11-20)

Static review found that three adversarial fixtures supplied rational coefficients to a Bernstein converter whose polynomial contract is integer-coefficient sparse polynomials. The fixtures have been corrected by multiplying each equation by a positive integer denominator: the simple common root uses `2*mu-1` and `2*t-1`; the double-root fixture uses `(2*mu-1)^2` and `(2*t-1)^2`; the near-coincident fixture uses integer-scaled factors with root separation exactly `2^-20`. These scalings preserve the zero sets exactly and retain the integer-polynomial contract. The corrected tests remain unexecuted.

### Resource-budget fixture alignment (2026-11-20)

A final source scan found that the box-budget exhaustion test reused the simple common-root equations with `Fraction` coefficients. It has now been changed to the same integer-scaled equations (`2*mu-1`, `2*t-1`). Thus all four controller call sites in the adversarial tests honor the integer sparse-polynomial contract. This is a static source correction only; no test execution or PASS is claimed.

### Krawczyk inclusion stage — first exact primitive implemented (2026-11-20)

The Bernstein path now has a rational Krawczyk operator using Bernstein enclosures of exact polynomial derivatives. A box is certified as containing exactly one simple common root only if strict Krawczyk inclusion and a strict infinity-norm contraction bound are both proved. The integrated wrapper retains exclusions, certified boxes, unresolved multiple/singular boxes and resource remainders separately.

This is not yet an exhaustive root-isolation algorithm. In particular, adjacent closed partition boxes can share boundary roots; the current wrapper does not yet canonicalize shared-edge/vertex roots or prove global uniqueness across the whole cover. Multiple roots remain unresolved. No governed test execution has occurred, and no method comparison or MLE certificate is claimed.

### Boundary candidate arithmetic — first exact profile implementation (2026-11-20)

The research harness now calculates exact rational likelihood probabilities for the four one-edge boundary profiles: `kappa -> 0`, `kappa -> infinity`, `mu -> 0`, and `mu -> 1`. The Binomial-limit mean and endpoint-mixture mean are rational pooled proportions; the likelihoods include the combinatorial factors. Boundary tests are added but not executed.

This does not yet classify joint corner/path limits, boundary roots of the compactified score equations, or compare interior algebraic likelihood enclosures with boundary values. It is a separate candidate-evaluation primitive, not global certification.

### Adaptive Bernstein–Krawczyk controller (2026-11-20)

The integrated controller now adaptively refines boxes after an inconclusive Krawczyk attempt instead of applying Krawczyk only once to leaves produced by a separate exclusion pass. It uses deterministic breadth-first processing, alternating split axes, exact rational endpoints, and explicit depth/box ceilings. Resource remainders and depth-limited boxes are retained with distinct states. Tests for deterministic refinement and resource abstention have been added; governed execution remains pending.

This remains a simple-root/local-box method. It does not resolve multiple roots or shared-boundary roots and does not establish a complete root census or global MLE certificate.

### Compactification-edge common factors (2026-11-20)

A new exact-rational edge-analysis primitive restricts both score polynomials to all four edges of the compactified square, computes their univariate gcd, and square-free-factorizes that gcd to retain common-root multiplicity. Identically vanishing pairs on an edge are classified as unresolved common components. Tests cover a shared double root, an edge component and malformed input. Real-root isolation, corner ownership and joint corner limits remain open; governed test execution is pending.

### Sturm-certified boundary-root isolation (2026-11-20)

The exact edge gcd/square-free pipeline now feeds rational Sturm isolation on `[0,1]`. It returns exact rational roots separately from rational intervals proved to contain one real root, and it abstains explicitly on depth or interval-budget exhaustion. Tests cover rational and irrational roots and a resource-limited case. Adjacent-edge corner deduplication and the interior root census remain open; no global certificate or method selection follows from this implementation.

### Compactification corner ownership (2026-11-20)

A canonical ownership layer now assigns each corner to exactly one vertical edge and retains the adjacent horizontal-edge occurrence as provenance-only. The corner registry carries coordinates, owner, factor index, root parameter and edge multiplicity. Unresolved ownership and partial Sturm isolation remain explicit. Tests cover a single shared corner, all four corners and propagation of a partial isolation. The boundary census is now deduplicated at corners but remains separate from the two-dimensional interior root census.

### Joint corner likelihood limits and singular-root contract (2026-11-20)

All four joint compactification-corner likelihood limits are now classified path-independently using the uniform bounds `P(X>0) <= r*mu` and `P(X<r) <= r*(1-mu)`. The exact helper returns the limiting point-mass distribution and histogram likelihood at each corner. This does not classify stationary score roots or non-corner boundary likelihood profiles. For interior singular roots, Bernstein/Krawczyk remains a simple-root path only; a separate validated deflation theorem is required. The parallel algebraic route is specified through exact bivariate common-factor detection, projection resultants, square-free/Sturm isolation and subresultant back-substitution, with local multiplicity not inferred from resultant multiplicity.
