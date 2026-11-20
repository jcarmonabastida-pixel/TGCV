# C10-S F5 — End-to-end closure dossier (research draft)

**Date:** 2026-11-20  
**Status:** OPEN — DETERMINISTIC SUITES PASS / GLOBAL CERTIFICATION AND TIERA CALIBRATION OPEN  
**Branch:** research/c10s-f1-integrated-correction-20261119  
**Purpose:** consolidate the definitive F5 closure sequence into one auditable contract. This dossier does not authorize execution, change frozen F1/F5 semantics, or upgrade any scientific claim.

## 1. Mission boundary

F5 is an instrumental reliability workstream within C10-S. Its sole purpose is to establish whether the beta-binomial fitting and uncertainty procedure used by the relevant F5 components can recover the correct likelihood solution and support valid interval coverage in the designs implicated by TierA (M10/R5 and M30/R20). It is not a general statistical-inference project.

F5 closure is necessary for the relevant calibration work; it is not evidence that accessibility causes Value. The scientific chain remains:

F5 fitting/coverage reliability → authorized prospective calibration → C10-S causal evaluation of accessibility contribution to Value.

No bank, replay, stochastic calibration, prospective calibration, or scientific execution is included in this engineering closure operation.

## 2. Reconstructed implementation inventory

The research harness currently contains the following reusable primitives in harness/c10s_f5_rational_score_polynomials.py:

- exact sparse integer numerator construction for the two beta-binomial scores;
- exact concentration compactification t=kappa/(1+kappa);
- exact tensor-product Bernstein coefficients, sign exclusion, and de Casteljau subdivision;
- deterministic Bernstein box exclusion with explicit depth/resource remainders;
- rational Krawczyk inclusion for simple common roots, with exact Bernstein Jacobian enclosures, strict inclusion, and contraction bound;
- exact one-edge boundary likelihood limits and path-independent joint corner likelihood limits;
- exact common-factor/gcd and square-free multiplicity analysis on compactification edges;
- Sturm isolation of edge roots and canonical corner ownership;
- axis-aligned common-component diagnostics;
- exact projection resultants and Sturm projection-root isolation, including the primary Res_mu(P,Q) concentration projection;
- conditional-mean tube construction and a deterministic adaptive concentration-interval census combining Bernstein exclusion and Krawczyk inclusion.

The three deterministic test modules currently define 133 test methods (85 exact-score/certification, 26 likelihood diagnostics, 22 MCSE profile). This is a source-level count, distinct from executed/discovered counts.

## 3. Definitive mathematical closure contract

A valid global-MLE certificate for one histogram must establish all of the following, without relying on optimizer convergence or sign-change heuristics.

### G1 — Input and equation integrity

- Validate the finite histogram, trial count, integer multiplicities, and nondegenerate support assumptions.
- Construct both exact score numerators from the same histogram.
- Verify the exact rational denominator sign conditions on the open parameter domain.
- Preserve exact input types and reject floating-point coefficients/bounds at exact public interfaces.
- Bind every result to the histogram, r, source revision, and exact polynomial hashes.

### G2 — Complete interior stationary-set census

- Cover the complete finite-concentration domain 0<t<1, not merely a convenient compact subinterval.
- Use conditional strict concavity in mu to reduce the search wherever its assumptions hold.
- Exclude candidate intervals only by exact Bernstein sign certificates.
- Certify simple common roots by a valid Krawczyk/interval-Newton inclusion and uniqueness argument.
- Use the exact concentration resultant Res_mu(P,Q) and Sturm isolation as the algebraic projection/cross-check where the reduced route is inconclusive.
- Lift every isolated concentration candidate back to the original paired equations; a projection root alone is not a bivariate root.
- Preserve and resolve multiplicity, common components, roots on subdivision boundaries, and endpoint accumulation. If a complete proof is unavailable, return an explicit incomplete/abstention result.

A census over a supplied closed interval strictly inside (0,1) is local completeness only. It cannot be promoted to complete coverage of the open finite-concentration domain without a proof covering both endpoint neighborhoods and all resultant candidates.

### G3 — Boundary and corner adjudication

- Evaluate all four compactification strata: mu=0, mu=1, t=0, and t=1.
- Use the existing exact one-edge likelihood-limit formulas only within their stated histogram/support assumptions.
- Use the existing uniform probability bounds for joint corner/path limits.
- Deduplicate edge/corner representations without losing multiplicity or provenance.
- Confirm whether any boundary stratum has a finite attained maximum or only a supremum/limit.

The existing boundary helpers provide exact ingredients, not yet a complete global ordering record.

### G4 — Likelihood ordering

- Evaluate the likelihood at every certified interior stationary candidate and every admissible boundary candidate/profile.
- Use rigorous rational/interval enclosures for log-likelihood or likelihood values; floating-point optimizer values are not sufficient.
- Refine enclosures until the global ordering is proved, or return MAXIMUM_ORDERING_UNRESOLVED.
- Distinguish unique global maximum, co-maxima, boundary supremum, non-attainment, and non-identification.
- Preserve an explicit abstention if intervals overlap or a candidate remains unresolved.

### G5 — Deterministic resource and abstention contract

- Freeze limits for interval count, subdivision depth, polynomial degree/coefficient growth, resultant matrix dimension, Sturm isolation, and arithmetic/runtime.
- Return every unprocessed interval/candidate with exact bounds and reason.
- Resource exhaustion, unsupported common components, singular/multiple roots without a certificate, and failed likelihood separation must never be mapped to PASS.
- Deterministic reruns on identical source/input/configuration must return identical classifications and certificate payloads.

### G6 — Governed software validation

- Run the complete 132-method suite under the canonical CPython 3.12 environment after integrity preflight.
- Add missing end-to-end tests for exact histogram-to-score provenance, resultant-root lifting, multiple-root resolution/abstention, shared subdivision-boundary roots, endpoint-neighborhood coverage, all boundary profiles/corners, likelihood ordering, and resource exhaustion.
- Run independent exact fixtures for simple, double, triple, near-coincident, boundary, common-component, and non-identifiable cases.
- Record command, interpreter/build, dependency state, source commit, test discovery count, stdout/stderr, exit code, and hashes.
- Audit the primary run; replay only if the applicable authorization and replay gate permit it.

### G7 — F5 relevance and TierA calibration gate

- On frozen hand-constructed fixtures, compare the reduced Bernstein/conditional-mean route against the exact resultant/Sturm route for identical mathematical targets.
- Measure coefficient growth, intervals processed, unresolved fraction, runtime and memory under declared ceilings.
- Only after software and mathematical gates pass, run the specifically authorized M10/R5 and M30/R20 coverage/calibration operation.
- Assess the original TierA failure criteria prospectively; B2/B3 remain diagnostic history and must not be reused to select a method or tune calibration.
- Decide whether the recovered coverage is adequate for C10-S or whether the procedure must abstain in defined regimes.

## 4. Current status against the contract

| Gate | Current evidence | Status |
|---|---|---|
| G1 exact score/input primitives | Exact paired score construction and compactification are implemented; deterministic CPython 3.12.10 workflow run 44762685571 passed all 133 discovered tests on source snapshot a3bca9d | SOFTWARE TESTS PASS; MATHEMATICAL INPUT-PROVENANCE AUDIT OPEN |
| G2 complete interior census | Closed-domain Bernstein/conditional-mean first-line census passed the M30/R20 full-domain fixture, including the t=1 endpoint-neighborhood regression; Krawczyk inclusion remains simple-root only and multiple roots/common components/split-boundary roots remain unresolved. Exact resultant/Sturm projection fallback still needs complete candidate lifting | PARTIAL — SIMPLE-ROOT FIXTURE PASS |
| G3 boundary/corner ingredients | Exact one-edge profiles and uniform joint-corner limits are integrated; helper tests passed in run 44762685571. Their assumptions, edge/corner ownership and global candidate completeness still require adversarial fixture coverage | PARTIAL |
| G4 global likelihood ordering | Exact rational likelihood enclosures and strict separation engine pass the small nondegenerate fixture. A new M30/R20 end-to-end test now exercises census plus interior-vs-boundary ordering; run 44764446630 is queued | OPEN — M30/R20 GLOBAL ORDERING UNDER TEST |
| G5 deterministic abstention | Explicit statuses/remainders exist at interval, resultant and likelihood-enclosure layers; unified ceilings and full resource-exhaustion adversarial coverage remain incomplete | PARTIAL |
| G6 governed validation | Run 44762685571 on a3bca9d completed successfully: CPython 3.12.10, locked dependencies, six-module compilation, and all three deterministic suites PASS; 133 tests discovered/executed in 243.863 seconds. Run 44764446630 executed 134 tests and failed 1: the interior/boundary census completed, but exact rational likelihood multiplication exceeded the 200,000-bit fraction ceiling. The comparison layer has been replaced by outward-rounded exact dyadic fixed-point interval multiplication (256-bit accumulator, integer-only rounding), with a large-histogram resource regression test. Run 44765936307 is validating the correction. | PASS — deterministic suite; additional adversarial coverage in progress |
| G7 TierA relevance/calibration | No prospective calibration authorized or run | NOT RUN |

## 5. Known blockers that prevent honest F5 closure

1. Interior multiple-root certification: Krawczyk certifies simple roots only. Exact univariate square-free/Sturm multiplicities are implemented for projection and edge polynomials, but a general projection-root-to-bivariate-root multiplicity lift is not implemented. Multiple/singular common roots therefore remain explicit abstention cases, not certified stationary candidates.
2. Full open-domain coverage: the adaptive conditional-mean controller now accepts closed subintervals of [0,1], and exact one-sided removal of endpoint-only (t-1)^m factors allows the M30/R20 fixture to census the full compactified interval without the large resultant. General endpoint-accumulation and degeneracy coverage across admissible histograms is not yet established; the single M30/R20 fixture is not a universal completeness proof.
3. Projection-to-root lifting: the exact fallback isolates every real projection root on the unit interval and sends each interior isolating interval/neighborhood through the paired conditional-mean/Bernstein/Krawczyk lift. Simple-root lifts are supported; projection multiplicity is not local bivariate multiplicity, and non-simple lifts remain unresolved. The M30/R20 preferred interval-first path does not invoke this fallback.
4. Boundary/global ordering: exact one-edge profiles and path-independent joint-corner limits are integrated. The global-MLE wrapper compares certified interior-root likelihood enclosures with all boundary-profile values using exact rational probability intervals, and a small nondegenerate fixture passes. The dedicated M30/R20 end-to-end ordering test is currently running; global ordering across other regimes and adversarial co-maxima/non-attainment cases remains to be demonstrated.
5. Governed validation and calibration: run 44762685571 passed all 133 deterministic tests on a3bca9d. The M30/R20 full-domain simple-root census and endpoint-adjacent Bernstein regression now pass. A new M30/R20 end-to-end global likelihood-ordering test is queued in run 44764446630. No governed prospective M10/R5 or M30/R20 calibration authorization/evidence exists; a clean deterministic suite does not establish multiple-root completeness or TierA coverage.

These are substantive proof/validation gaps, not documentation tasks. They cannot be closed by changing status labels or by adding a wrapper that reports a local census as global.

## 6. Method-selection rule

The reduced conditional-mean/Bernstein route is the preferred first-line exclusion and simple-root route because it exploits the model's conditional concavity and avoids unnecessary algebraic lifting. The concentration resultant/Sturm route remains a complementary projection census and fallback. A full general-purpose algebraic backend is not selected in advance.

Use the algebraic route only for candidate intervals the reduced route cannot certify, for multiplicity/projection analysis, or as an independent cross-check. Compare both on the same frozen deterministic fixtures. Select the least costly route that meets G1–G6; do not use B2/B3 to tune or select the method.

## 7. Required final closure record

F5 may be changed from OPEN only by one evidence-backed closure record that links:

- exact source commit and polynomial/input identities;
- complete interior and boundary candidate census;
- multiplicity and common-component disposition;
- rigorous global likelihood ordering;
- deterministic resource/abstention results;
- governed CPython 3.12 test execution and primary audit (plus replay if authorized);
- prospective TierA coverage/calibration results and their frozen acceptance criteria;
- explicit limits and regimes in which the fitter abstains.

Until all applicable items pass, the correct status is F5 OPEN — DETERMINISTIC SOFTWARE PASS; GENERAL GLOBAL-MLE COMPLETENESS AND TIERA COVERAGE NOT CERTIFIED.

## 8. Governance and scientific boundary

This dossier is a research-branch design/coordination artifact. It does not modify main, RMA, Evidence→Claim Matrix, frozen F1/F5 contracts, B2/B3, or any scientific claim. It does not authorize execution. The canonical workflow remains: historical reconstruction → integrity preflight → explicit authorization → execution → primary audit → replay gate → final audit → scientific closure.

The purpose remains narrow: repair the fitting/coverage reliability limitation that blocked TierA, then return to the C10-S causal question of whether accessibility contributes to Value. F5 is not an independent statistical research programme.


## 9. Validation update — 2026-11-20

The three assertion defects identified in run 44747642542 were corrected in the research test source:
- exact Krawczyk image for the affine fixture;
- a genuinely multiple-root fixture for the resource-remainder assertion;
- inclusive comparison at the exact Sturm isolation-width threshold.

The unchanged production mathematics was then exercised by two independent deterministic workflow runs:
- [Run 44749347942](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44749347942), source snapshot `2c276b4ddc77e2e7a6e2a89bd11000271b34cd1b`: 124 tests, 91.666 seconds, **OK**.
- [Run 44749353232](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44749353232), source snapshot `67d147b75ed6fc46c4a83792c50951d82e2dcf49`: 124 tests, 91.917 seconds, **OK**.

Both runs passed locked dependency installation, CPython 3.12.10 setup, compilation of the six F5 modules, and all three deterministic suites. The duplicate run is an independent repeat, not 248 distinct tests.

This closes the deterministic software-test gate for the current tested source snapshot. It does **not** close G2–G5: the tests do not establish complete lifting of every concentration-resultant root, resolution of all multiple/common-component cases, a global likelihood ordering, or TierA coverage. F5 remains OPEN.

## 10. Integrated resolution sequence from this validated baseline

The next implementation is one connected certification pipeline, not a parallel statistics package:

1. Build the paired exact score numerators from one frozen histogram and compactify both to ((\mu,t)\).
2. Compute the primary \\(\operatorname{Res}_{\mu}(P,Q)\\) concentration projection and isolate every real root on the closed compactified interval; classify (t=0,1) as boundary strata, not finite-interior roots.
3. Lift every interior projection root back to the original paired equations. Use conditional-mean strict concavity to reduce the lift to one admissible mean branch; use Bernstein exclusion and Krawczyk for simple roots. Any singular/multiple lift must be resolved by exact subresultant/gcd multiplicity analysis or remain explicitly unresolved.
4. Reconcile the lifted interior set with the four edge censuses, exact corner limits, and unique corner ownership. Common components and projection degeneracies must not be counted as finite isolated roots.
5. Compare every admissible interior stationary candidate and boundary supremum under one likelihood contract. Use certified rational probability enclosures and rigorous logarithm enclosures; refine until the ordering is strict or return TIE/UNRESOLVED, never use floating-point optimizer ranking as proof.
6. Enforce deterministic caps for resultant dimension/coefficient growth, Sturm intervals, lift subdivisions, rational bit growth, and likelihood refinement. Every exhausted cap returns a machine-readable remainder and ABSTAIN.
7. Only after the integrated deterministic certificate and its adversarial fixtures pass, prepare the frozen prospective TierA M10/R5 and M30/R20 calibration protocol. No B2/B3 reuse or post-hoc tuning.

The preferred implementation remains the conditional-mean/Bernstein reduction first, with exact resultant/Sturm projection as the global concentration census and fallback/cross-check. This ordering uses the model structure and avoids a general-purpose algebraic backend.


### 9.1 Full-domain Bernstein correction and governed deterministic PASS

Run [44762685571](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44762685571), source snapshot `a3bca9d3712736532bf2b3454d037ea815122135`, completed successfully on CPython 3.12.10 with locked dependencies. All six F5 modules compiled; all three deterministic suites completed with 133 tests in 243.863 seconds and exit status 0. The run includes:
- exact stripping of endpoint-only `(t-1)^m` factors from restricted mean-score lines on intervals ending at (t=1), with parity-correct sign restoration;
- a regression test that proves the endpoint-only factor does not prevent a uniform conditional-mean tube on the open concentration domain;
- the M30/R20 full-closed-domain Bernstein census, which now completes without invoking the dimension-77 resultant fallback.

This is a deterministic software/fixture PASS, not a proof for all admissible histograms. Krawczyk inclusion still certifies simple roots only. The current adaptive census explicitly leaves multiple roots, split-boundary roots, and unresolved components as incomplete.

### 9.2 M30/R20 global likelihood-ordering validation

A new test, `test_m30_r20_global_mle_orders_interior_and_boundary_candidates`, now exercises the complete public global-MLE wrapper on the same M30/R20 histogram. It requires an exact rational winner/co-winner/boundary-supremum classification and the declared globality basis. It is committed as `31e28f8803153a20fc083dfe78b8084c3363382d`; workflow [44764446630](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44764446630) is queued. This test is a deliberately bounded fixture; it does not replace multiplicity, common-component, or prospective coverage gates.


### 9.3 Likelihood-ordering resource correction

Run [44764446630](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44764446630), commit `31e28f8803153a20fc083dfe78b8084c3363382d`, completed with 134 tests and one failure. The integrated stationary/boundary census completed, but the exact rational product enclosure hit `LIKELIHOOD_FRACTION_RESOURCE_LIMIT` at 200,000 bits. This is an ordering-layer resource failure, not an unresolved stationary census.

The likelihood enclosure now accumulates nonnegative rational probability intervals on a 256-bit dyadic grid, rounding lower products downward and upper products upward using integer arithmetic only. This preserves a rigorous enclosure while bounding intermediate integer growth. A large-histogram regression test checks bounded representation and enclosure validity. The correction is committed as `5c1223d` with regression test `2fcf3f2`; run [44765936307](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44765936307) is validating the combined snapshot. No global-MLE PASS is claimed until this run succeeds.

### 9.4 Run 44767224308 — dyadic likelihood enclosure correction (2026-11-20)

The run previously described as pending in §4–§5 and §9.3 has now completed successfully. GitHub Actions run [44767224308](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44767224308), workflow run number 48, checked out exact source commit `a9a56d7c142b441b0893858c75e13a38ae38a9a2` on `research/c10s-f1-integrated-correction-20261119`.

Execution evidence from job `f5-tests`:
- Ubuntu 24.04 runner; CPython 3.12.10; locked dependencies installed with hash enforcement.
- All six F5 modules compiled successfully.
- All three deterministic F5 suites completed: **135 tests, 342.600 seconds, exit status 0 (OK)**.
- The large-histogram dyadic likelihood enclosure regression passed after intersecting the rational upper probability bound with the mathematical unit interval [0,1].
- `test_m30_r20_full_domain_bernstein_route_avoids_large_resultant` passed.
- `test_m30_r20_global_mle_orders_interior_and_boundary_candidates` passed. Its assertions require one of the three certified global classifications (interior maximum, boundary supremum, or co-maximizers), exact rational probability-interval ordering, and the declared globality basis `COMPLETE_INTERIOR_STATIONARY_CENSUS_PLUS_ALL_BOUNDARY_PROFILES_AND_CORNER_LIMITS`. Thus the bounded M30/R20 fixture now passes the integrated public wrapper; this is not a universal theorem over all histograms.

The test suite also passed explicit multiplicity fail-closed cases: a singular/multiple common root is retained as unresolved and is not promoted to a certified simple root; edge square-free multiplicity and Sturm isolation fixtures pass; resource-limit remainders are tested. These establish correct behavior on those fixtures, not general resolution of arbitrary interior multiple roots or all common components.

**Updated gate classification for this tested snapshot:**
- G1: deterministic exact-score and input-validation tests PASS; independent mathematical/provenance audit remains OPEN.
- G2: bounded full-domain M30/R20 simple-root census PASS; general multiple/singular interior-root lifting and broader endpoint/degeneracy completeness remain OPEN or explicit abstention regimes.
- G3: exact edge/corner ingredients and selected adversarial fixtures PASS; exhaustive cross-stratum ownership, co-maxima and non-attainment coverage remains OPEN.
- G4: bounded M30/R20 integrated interior-versus-boundary global ordering fixture PASS; broader adversarial ordering regimes remain OPEN.
- G5: deterministic abstention/resource remainders are exercised; one unified, frozen ceiling contract across every layer and its complete adversarial audit remain OPEN.
- G6: deterministic software validation PASS for commit `a9a56d7...`; independent replay is not claimed or required by this push-only test workflow. A separate primary execution audit of the certificate payload/provenance remains OPEN.
- G7: NOT RUN. The canonical C10-S mission currently records calibration/dispatch/scientific execution as not authorized. This user's delegation is treated as authority to continue the engineering and protocol-preparation work, but it does not silently amend the frozen execution-authorization record. No stochastic TierA calibration has been run.

**Disposition:** F5 remains OPEN. The run closes the immediate likelihood-enclosure software blocker and validates one end-to-end M30/R20 global-MLE fixture. It does not close mathematical-operational F5 across the required admissible regime, and does not close functional F5/TierA coverage. Continue by consolidating the smallest remaining mathematical/abstention contract and preparing the prospective TierA protocol without running calibration until its explicit governance authorization is resolved. The work remains on the research branch; `main`, RMA, Evidence→Claim Matrix, STATUS and scientific claims are unchanged.

### 9.5 Historical calibration asset reconciliation — P178 is not G7

The existing `03_EXPERIMENTS/C10-S/calibration/p178_*` assets were inspected before proposing any new calibration. Their manifest identifies protocol `TGCV-C10-S-P178-FOCAL-MC-REPRO-001`, Python 3.13.5, 10,000 replications per cell, a 27-cell N=700 reference grid and a separate 32-cell central-N curve. The manifest explicitly limits the asset to a benchmark estimator: it contains no TGCV Analyzer, no adversarial measurement scenarios and no confirmatory experiment. Its DGP and outputs therefore do not satisfy the F5 TierA M10/R5 and M30/R20 prospective calibration gate and must not be relabelled as such.

The current global-MLE design record `C10S_F5_GLOBAL_MLE_CERTIFICATION_DESIGN_001.md` and the interval comparison design/specification drafts also explicitly declare `Execution authorization: NONE`. The interval comparison specification is a D1 review candidate, not frozen. Accordingly, the P178 assets are retained as historical bounded benchmark evidence only; they are not a substitute for the still-unfrozen TierA protocol or its required authorization.

### 9.6 Input-integrity hardening discovered during delegated G1–G6 audit — 2026-11-20

A direct audit of the final likelihood-enclosure helper found that its internal loop validated histogram entries but an empty histogram or a histogram with only zero multiplicities could bypass the loop and return the multiplicative identity likelihood enclosure. The integrated public wrapper already validated its input through the score/census path, so this did not invalidate run 44767224308's tested M30/R20 result; nevertheless, the private enclosure primitive's own input contract was incomplete.

Corrective change:
- `_beta_binomial_likelihood_enclosure` now independently validates positive integer r, a nonempty Mapping, integer count keys in [0,r], nonnegative integer multiplicities and strictly positive total multiplicity before any likelihood arithmetic.
- New deterministic regression `test_likelihood_enclosure_rejects_invalid_or_empty_histograms` covers invalid r, empty histogram, all-zero multiplicities, out-of-range count and negative multiplicity.
- Code commit: `628bf7bb7bc040ff009b346dd38026a9f5d590bd`.
- Regression commit: `4eda28ed28b23eacf641a81bc29705f1dd52d87d`.
- Workflow run #50, ID `44770409949`, was triggered for the regression commit and is pending at the time of this record: [run #50](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44770409949).

This is a G1 input-integrity hardening item, not a change to the estimator, DGP, target, or scientific protocol. Do not count the new regression as validated until run #50 completes successfully.

### 9.7 Run #50 — G1 likelihood input contract regression PASS (2026-11-20)

GitHub Actions run [44770409949](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44770409949), source commit `4eda28ed28b23eacf641a81bc29705f1dd52d87d`, completed successfully:
- 136 deterministic tests, 339.734 seconds, exit status 0.
- The five invalid/empty histogram cases for the likelihood enclosure helper passed.
- Locked dependency installation and compilation of all six F5 modules passed.
This closes the specific G1 input-validation regression on that source snapshot. It does not constitute the independent derivation/provenance audit or the full G1 gate.

### 9.8 G5 resource-contract audit — remove inert boundary ceilings (2026-11-20)

A review of the global-MLE wrapper found that `max_boundary_depth` and `max_boundary_intervals` were accepted and reported as resource ceilings but never controlled any computation: the one-edge beta-binomial profiles and the four joint-corner limits are closed-form exact evaluations, not iterative censuses. Reporting unused controls as operative ceilings was misleading.

Corrective change in commit `3591a63e095a67aa0dfaeae2df5528076a90b708`:
- Removed the two inert boundary-budget arguments from the stationary census and global-MLE APIs and their tests.
- Replaced their misleading resource-contract entries with `boundary_evaluation = EXACT_CLOSED_FORM_NO_ITERATIVE_BUDGET`.
- Added one shared early validator for every active projection/lift/conditional-mean ceiling; both the stationary census and global wrapper validate before degenerate-data early returns.
- Projection width is now required to be a positive exact rational even when the interval-first path avoids resultant/Sturm.
- Added regressions for invalid depth/interval/mean ceilings, zero projection width, and global-wrapper budget validation on degenerate data.
- The exact boundary work is therefore accurately represented as closed-form, not falsely budgeted. Active interval and projection loops retain deterministic hard ceilings and typed incomplete/resource outcomes.

The change is under deterministic verification in [run #51](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44771555687). Do not count the new G5 contract regression as PASS until that run completes.

### 9.9 G1 mathematical derivation audit — internal exact review (2026-11-20)

A line-by-line mathematical review was completed against the implemented score construction and the finite-product beta-binomial likelihood. This is an internal derivation audit, not an independent external review.

1. **Likelihood identity.** The beta-binomial PMF is written as the rising-factorial product in `alpha=mu*kappa`, `beta=(1-mu)*kappa`, and `kappa`; the binomial coefficient is data-only for score purposes and is restored in the likelihood comparator.
2. **Score derivatives.** Differentiation gives
   `S_mu = sum_x n_x[sum_{j<x} kappa/(mu*kappa+j) - sum_{j<r-x} kappa/((1-mu)*kappa+j)]`
   and
   `S_kappa = sum_x n_x[sum_{j<x} mu/(mu*kappa+j) + sum_{j<r-x}(1-mu)/((1-mu)*kappa+j) - sum_{j<r}1/(kappa+j)]`.
   The polynomial builder multiplies these terms by the corresponding common products with one factor omitted. All cleared factors are strictly positive on the open domain, so the paired polynomial zero set is exactly the score zero set there.
3. **Conditional mean uniqueness.** For nondegenerate pooled counts, at least one observation has x>0 and at least one has x<r. The second derivative in mu is a sum of nonpositive terms and contains at least one strictly negative j=0 term. Hence it is strictly negative for every 0<mu<1 and fixed kappa>0; the endpoint score signs give one and only one conditional-mean root.
4. **Compactification.** t=kappa/(1+kappa) is a bijection from positive finite concentration to 0<t<1. Multiplication by (1-t)^d gives the exact transformed integer polynomial and preserves the open-domain zero set. t=0 and t=1 are handled only as boundary strata.
5. **Exclusion/inclusion.** Bernstein coefficients provide exact convex-hull range enclosures; strict one-sign coefficients exclude zeros. Krawczyk inclusion is used only for simple-root existence/uniqueness; mixed signs and singular/multiple cases remain unresolved, never promoted.
6. **Boundary/global comparison.** The four edge profiles are exact closed forms. The joint-corner limits follow uniformly from P(X>0)<=r*mu and P(X<r)<=r*(1-mu). The interior likelihood enclosure bounds every PMF factor by exact rational intervals and multiplies with outward-rounded dyadic integer arithmetic. A global winner is returned only under strict enclosure separation or a proven boundary co-maximum; overlapping intervals abstain.

The derivation is supported by the direct-rational score identity fixtures (small M10/R5 and M30/R20), exact compactification tests, boundary/corner fixtures, and independent exact PMF/score diagnostics. This closes the *derivation review portion* of G1 on the implemented model. Input validation was separately exercised by run #50. The resource-contract correction under run #51 remains pending; G1–G6 are not yet declared closed as a group.

### 9.10 Run #51 — active resource contract regression PASS (2026-11-20)

GitHub Actions run [44771555687](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44771555687), source commit `3591a63e095a67aa0dfaeae2df5528076a90b708`, completed successfully:
- 138 deterministic tests, 341.429 seconds, exit status 0.
- All six F5 modules compiled; locked dependencies installed.
- The new early-validation tests for projection/lift/mean budgets, positive exact projection width, and degenerate-data early returns passed.
This validates the G5 resource-contract correction on that source snapshot. It does not alone close the broader G5 gate until all resource-remainder and result-payload requirements are reconciled.

### 9.11 G1 provenance binding — implementation added, verification pending (2026-11-20)

The G1 audit found that a global-MLE result contained a same-histogram provenance label but did not bind the returned census payload to the actual histogram, trial count, source revision and exact score equations. This is now addressed in code commit `05cffe1843d4ed6f64837e51ac1d16983c115fd8`:
- A canonical SHA-256 provenance record is generated from `r`, the normalized positive-multiplicity histogram, sample size and pooled successes.
- It records the explicit 40-hex source revision (or the GitHub Actions `GITHUB_SHA` when no explicit revision is supplied).
- It hashes both exact raw score-numerator polynomials and their compactified forms using canonical sorted sparse terms.
- The provenance record is attached to every stationary census returned within the global-MLE certificate, including typed incomplete/abstention results.
- New tests verify semantic normalization of zero-count entries, hash sensitivity to changed data, source-SHA validation, and explicit binding in a boundary-supremum certificate. An exhaustive small-histogram rational score-identity test was also added.

The new deterministic workflow is [run #52](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44772784165), queued at the time of this record. Do not count G1 provenance binding as validated until it completes successfully.
