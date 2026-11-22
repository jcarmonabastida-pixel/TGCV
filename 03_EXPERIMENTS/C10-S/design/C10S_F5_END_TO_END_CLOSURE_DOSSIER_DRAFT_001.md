# C10-S F5 — End-to-end closure dossier (research draft)

**Date:** 2026-11-20  
**Status:** OPEN — G1–G6 PASS / G7 protocol frozen; staged execution plan and software gate PASS; fresh one-use authorization for the staged executor pending  
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
- Run independent exact fixtures for simple, double, triple, near-coincident, boundary, common-component, and non-identifiable cases; certify or explicitly abstain without promoting unsupported roots.
- Cross-check the Bernstein/conditional-mean route against exact resultant/Sturm on the same hand-constructed M10/R5 target where computationally feasible; compare the lifted stationary set and global classification, and record coefficient growth, interval counts, unresolved fraction and runtime. This is deterministic engineering validation, not scientific calibration.
- Record command, interpreter/build, dependency state, source commit, test discovery count, stdout/stderr, exit code, and input/polynomial hashes.
- Audit the primary run; replay only if the applicable authorization and replay gate permit it.

### G7 — F5 relevance and TierA calibration gate

- Only after G1–G6 pass, run the specifically authorized prospective M10/R5 and M30/R20 TierA coverage/calibration operation.
- Assess the original TierA failure criteria prospectively; B2/B3 remain diagnostic history and must not be reused to select a method or tune calibration.
- Decide whether the recovered coverage is adequate for C10-S or whether the procedure must abstain in defined regimes.

## 4. Current status against the contract — G1–G6 closure (2026-11-20)

| Gate | Closure evidence | Status |
|---|---|---|
| G1 exact score/input/provenance integrity | Exact rational score derivation reviewed; exhaustive small-histogram and M10/R5/M30/R20 score-identity fixtures pass. Canonical SHA-256 binds normalized histogram, r, sample size, pooled successes, raw/compactified score polynomials and source revision. Run #54 verifies default source revision is the actual GitHub Actions `GITHUB_SHA`. | <badge color="success">PASS</badge> |
| G2 interior stationary-set census | Full-domain simple-root census complete on the bounded M10/R5 and M30/R20 targets using conditional-mean concavity, Bernstein exclusion and Krawczyk inclusion. Exact resultant/Sturm cross-check agrees on M10/R5. Multiple/singular roots and common-component regimes remain typed incomplete/abstention states; no global certificate is emitted for them. | <badge color="success">PASS</badge> — bounded target regime, fail-closed outside |
| G3 boundary/corner adjudication | Exact profiles for all four boundary strata; four path-independent joint-corner limits; endpoint-mixture, degenerate and non-attained `kappa->0` boundary-supremum global fixture passed. | <badge color="success">PASS</badge> |
| G4 global likelihood ordering | Exact rational likelihood enclosures and outward-rounded dyadic accumulation; M10/R5 interior maximum, M30/R20 interior/boundary ordering, boundary supremum and exact degenerate co-maxima fixtures pass. Unresolved overlapping enclosures abstain. | <badge color="success">PASS</badge> |
| G5 deterministic resource/abstention contract | Active projection/lift/mean ceilings validated before early returns; exact positive projection width; explicit resource remainders; boundary profiles correctly identified as closed-form with no iterative budget. Run #51 passed. | <badge color="success">PASS</badge> |
| G6 governed software validation | Runs #50–#54 passed in sequence; final run #54 passed 144/144 tests on CPython 3.12.10 with locked dependencies and all six F5 modules compiled. Includes the M10/R5 Bernstein/resultant/Sturm comparison with matching global classification and overlapping root boxes. | <badge color="success">PASS</badge> |
| G7 TierA relevance/calibration | User authorization received 2026-11-20; successor F5-only protocol v1.0 frozen with new seeds, global-MLE fit gate, resource preflight, primary/replay and no-pooling criteria. | AUTHORIZED — one-use workflow pending |

**Disposition:** the mathematical-operational/engineering closure of F5 through G6 is PASS for the bounded M10/R5 and M30/R20 target regimes. F5 overall remains functionally OPEN at G7 only. User authorization for the new F5 Tier-A G7 operation was received on 2026-11-20; execution is pending the one-use hash-bound workflow.

## 5. Accepted limitations and fail-closed scope

1. **General singular/multiple interior roots.** Krawczyk inclusion certifies simple roots. Projection/edge Sturm isolation preserves univariate multiplicity, but arbitrary projection-root-to-bivariate-root multiplicity lifting is not implemented. Such boxes remain typed unresolved; the global wrapper abstains. This is an explicit scope limitation, not permission to report a partial census as exhaustive.
2. **General mixed common components.** The exact component detector classifies axis-aligned factors. It does not claim a complete bivariate gcd for arbitrary mixed factors. A zero resultant or unresolved common-component state blocks global certification.
3. **Boundary-supremum adjudication.** Exact edge profiles and uniform joint-corner limits are implemented; M10/R5 and M30/R20 global interior cases, degenerate co-maxima and the direct non-attained `kappa->0` boundary-supremum fixture all passed.
4. **G1 provenance binding.** Canonical hashes bind normalized histogram, r, sample size, pooled successes, raw/compactified score polynomials and source revision. Run #54 passed the actual GitHub Actions `GITHUB_SHA` default binding.
5. **G7 scientific relevance.** No prospective TierA calibration has been run. Historical P178 benchmark assets do not satisfy this gate. G7 remains a separate scientific execution gate and requires explicit user authorization.

The G1–G6 closure decision is bounded and fail-closed: the required M10/R5 and M30/R20 deterministic fixtures receive complete certificates; every unsupported singular/common-component/resource regime returns a typed incomplete/abstention state; no local or partial result is labelled global. G7 is not part of this engineering authorization.

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

### 9.12 Run #52 — provenance, exact score grid and boundary supremum PASS (2026-11-20)

GitHub Actions run [44772784165](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44772784165), source commit `05cffe1843d4ed6f64837e51ac1d16983c115fd8), completed successfully:
- 142 deterministic tests, 340.942 seconds, exit status 0.
- The canonical provenance hash tests passed for normalized histograms and raw/compactified score polynomials.
- The exhaustive small-rational histogram grid passed exact score-numerator identity checks.
- The global wrapper certified the mixed endpoint-only sample's unattained `kappa->0` boundary supremum and retained `attained_in_open_domain = false`.
- Locked dependencies and six-module compilation passed.

The remaining G1 refinement is to verify that the default source revision is taken from the actual CI `GITHUB_SHA`, rather than only exercising an explicit valid SHA fixture. G6's deterministic method comparison is being executed separately in run #53.

### 9.13 Run #53 — deterministic Bernstein/resultant cross-check PASS (2026-11-20)

GitHub Actions run [44773997684](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44773997684), source commit `9d5ca258b8f976b700949b8a9a978e7312e28f1d`, completed successfully:
- 143 deterministic tests, 355.711 seconds, exit status 0.
- The new M10/R5 comparison forced the exact resultant/Sturm route and compared it against the default Bernstein/conditional-mean route on the same histogram and score equations.
- Both routes returned `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`; the exact route returned a nonzero resultant and complete Sturm projection isolation; both routes certified the same number of simple roots and their Krawczyk boxes overlapped in both coordinates.
- The resultant route is now an executable deterministic cross-check, not merely a theoretical fallback. This does not select it over Bernstein-first; the default remains Bernstein-first and exact resultant/Sturm is available as fallback/cross-check.

The last G1 provenance detail is being verified separately: tests now use the real CI `GITHUB_SHA` by default and assert that an omitted explicit source revision is populated from that exact value. This is run [#54](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44775205756).

### 9.14 Run #54 — actual source-revision binding PASS (2026-11-20)

GitHub Actions run [44775205756](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44775205756), source commit `a22f2edc7f7ff39f158e6ab2740eea2662b047d3`, completed successfully:
- 144 deterministic tests, 353.169 seconds, exit status 0 (OK).
- CPython 3.12.10; locked dependencies installed; all six F5 modules compiled successfully.
- `test_input_provenance_defaults_to_actual_github_source_revision` passed. The global certificate's provenance now binds to the actual `GITHUB_SHA` when no explicit source revision is supplied; all global wrapper fixtures also use the actual CI SHA by default.
This closes the last pending G1 provenance item and supplies the final governed software snapshot for G1–G6.

## 10. G1–G6 closure record — 2026-11-20

**PASS:** G1, G2, G3, G4, G5 and G6 for the declared bounded F5 target regime (M10/R5 and M30/R20), with explicit typed abstention for unsupported singular/multiple-root, mixed-component and resource-exhaustion cases. The supported fixtures receive complete interior/boundary/global-likelihood certificates; unsupported cases cannot be promoted to global PASS.

**Not claimed:** a universal multiplicity-aware bivariate solver; external independent review; prospective TierA coverage; causal evidence about accessibility's contribution to Value. The exact resultant route is an independently exercised cross-check on M10/R5, not a universal selection over Bernstein.

**G7 remains NOT RUN.** It requires a frozen prospective TierA protocol, predeclared acceptance thresholds and explicit user authorization before any calibration bank, validation bank, Analyzer/Evaluator scientific execution or coverage results are generated.

All work remains on `research/c10s-f1-integrated-correction-20261119`. No change was made to `main`, canonical RMA, Evidence→Claim Matrix, STATUS or scientific claims. This is the F5 G1–G6 research-branch closure record, not a promotion/merge.

### 9.15 G7 authorization and successor protocol preparation — 2026-11-20

The user explicitly authorized G7 on 2026-11-20. Historical reconstruction found that the earlier eight-cell comparative Tier-A holdout had already executed as run [44572812481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44572812481) and was adjudicated NOT_VALIDATED (10/32 method × cell × component combinations passed; C5/F5 passed 0/4). That bank is consumed and unblinded; it is excluded from G7 and cannot be rerun or reused.

A successor F5-only prospective protocol was therefore frozen: `C10S-F5-G7-TIERA-PROSPECTIVE-001 v1.0`, at `C10S_F5_G7_TIERA_PROSPECTIVE_PROTOCOL_001.md`. It tests the two frozen beta22 cells M10/R5 and M30/R20, K=1,000 per cell, C0/C5 B=1,000, a new SHA-256 seed schedule/namespace, 100-per-cell resource-only preflight, primary plus exact clean-source replay, and the unchanged no-pooling Tier-A criteria. The old v1.0 holdout and original v002 datasets are explicitly excluded.

The C5 path now has a fail-closed global-MLE gate: the existing three-start production fit is accepted only if the exact Bernstein/conditional-mean/Krawczyk certificate returns `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` and the fitted mean/compactified concentration lies inside the certified unique-root box. Otherwise C5 emits no within/raw-between interval and records a typed abstention. The interval formula and percentile procedure are not changed. A real M10/R5 integration fixture verifies the optimizer point lies inside the actual certificate box.

Static validation: GitHub Actions run [44803113319](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44803113319), commit `fa1b2009304f5de8382632ff1d15470a79e52cf2`, passed 180/180 tests under CPython 3.12.10 with locked dependencies. This includes the real M10/R5 certificate-to-production-fit linkage, G7 no-pooling adjudication, resource-only no-adjudication contract, seed-separation checks and one-use authorization validator tests.

**Execution state:** authorized by the user, but not yet executed. The only pending action is the dedicated one-use authorization-branch push, hash-bound to the exact code/protocol/workflow snapshot. Tier B and C10 Generator/Analyzer/Evaluator scientific execution remain false and out of scope.


### 9.16 Historical deterministic validation snapshot — run 44767224308 (2026-11-20)

Run [44767224308](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44767224308), source commit `a9a56d7c142b441b0893858c75e13a38ae38a9a2`, completed successfully on CPython 3.12.10. Locked dependencies installed, all six F5 modules compiled, and the three deterministic suites completed: **135 tests in 342.600 seconds; OK; exit status 0**.

This historical run validated the bounded dyadic likelihood-enclosure correction after the preceding resource failures:
- nonnegative rational probability intervals were multiplied using a 256-bit outward-rounded dyadic accumulator and integer-only rounding;
- each beta-binomial outcome-probability upper bound was intersected with the mathematical unit interval before dyadic rounding;
- the large-histogram regression verified enclosure ordering, non-negativity, the unit upper bound and bounded representation;
- the M30/R20 global-ordering fixture passed its then-current typed-certificate assertions.

This run is retained as an intermediate evidence point, not the final G1–G6 validation snapshot. Its M30/R20 fixture accepted any of the three typed certified global outcomes and was not an independent expected-winner oracle. Later work strengthened the implementation and evidence: run [44775205756](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44775205756) bound input provenance to the actual GitHub source revision (144/144 tests), and run [44803113319](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44803113319) passed 180/180 tests, including the real M10/R5 certificate-to-production-fit linkage, G7 no-pooling adjudication, resource-only no-adjudication, seed-separation and one-use authorization-validator tests.

The current consolidated disposition is therefore the one recorded in §10 and §9.15 above: **G1–G6 PASS for the declared bounded F5 target regime, with explicit typed abstention for unsupported singular/multiple-root, mixed-component and resource-exhaustion cases. G7 is authorized by the user and its successor protocol is frozen, but the one-use authorization-branch workflow has not yet executed.** The G1–G6 closure is not a universal multiplicity-aware solver, external review, prospective TierA coverage result or causal evidence for `ΔT_acc → Value`.



### 9.17 G7 one-use execution attempt and resource gate — 2026-11-21

The frozen G7 protocol v1.0 was activated using the previously recorded explicit user authorization. The one-use authorization record is committed on dedicated branch `research/c10s-f5-g7-auth-C10S-F5-G7-20261121-001`:
- authorization commit: `3136b7f639808262a7120d6efda9e9d3b0b4b91f`;
- sole parent / approved code commit: `fa1b2009304f5de8382632ff1d15470a79e52cf2`;
- GitHub Actions run: [44842130930](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44842130930);
- one-use authorization validator and exact source-hash / parent checks: PASS.

Historical execution evidence must be considered before interpreting the current attempt. Earlier run [44803576150](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44803576150), on an authorization commit whose approved code parent differs only by documentation from the current approved code snapshot, passed authorization validation and dependency setup but failed during the resource-only preflight with `G7_RESOURCE_PREFLIGHT_PROJECTS_OVER_4_5_HOURS`. It stopped before generating the prospective primary bank; no coverage adjudication or G7 holdout data were produced. The failure is a frozen resource stop condition, not a coverage result and not a G7 NOT_VALIDATED finding.

Run 44842130930 has passed the same authorization and dependency gates and is currently executing the same resource-preflight path against the approved code commit `fa1b2009304f5de8382632ff1d15470a79e52cf2`. Since the executable snapshot and frozen resource contract are materially unchanged from the earlier attempt, a repeated resource-gate failure is a material risk. Do not treat this run as a fresh performance improvement or as evidence of calibration until its preflight result is available.

If the 4.5-hour projection gate fails again, the next action is an engineering optimization of the per-dataset certified-fit path under unchanged G7 K/B, seed separation, coverage thresholds and replay requirements, followed by a new governed static validation and a new hash-bound one-use authorization. Do not relax the resource threshold, reduce K/B, omit replay, inspect coverage early or reuse any consumed bank.

Current scientific disposition: G1–G6 remain PASS for their declared bounded F5 target regime; G7 remains AUTHORIZED BUT NOT YET EXECUTED. Tier B and C10 Generator/Analyzer/Evaluator causal execution remain out of scope and unauthorized.


### 9.18 G7 resource bottleneck diagnosis and vectorized bootstrap correction — 2026-11-21

The failed preflight in run [44803576150](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44803576150) is now localized more precisely. The workflow spent approximately 3 h 49 min in the resource-only preflight before raising `G7_RESOURCE_PREFLIGHT_PROJECTS_OVER_4_5_HOURS`. The preflight processes 100 datasets per cell (200 total), and each dataset called the full comparator with C0 bootstrap B=1,000 and C5 bootstrap B=1,000. Even with `adjudicate=False`, those bootstrap computations still ran; only coverage adjudication was skipped.

The dominant avoidable Python overhead in C5 was rebuilding an M×R Bernoulli matrix and calling the scalar nested-estimand routine once per bootstrap replicate. For a Bernoulli row with success count `x_i`, the same point estimands are exactly expressible from counts:
- within component: `mean_i[x_i(R-x_i)/(R(R-1))]`;
- world-mean variance: sample variance of `x_i/R`;
- raw between component: world-mean variance minus within/R;
- projectable MCSE draw count: the same nonnegative projected-variance predicate.

The implementation now computes those quantities in vectorized NumPy batches, without changing the beta-binomial DGP, PCG64 seed stream, bootstrap draws, target estimands, interval quantiles, or boundary/abstention rule. A regression compares 257 deterministic count-vector draws against the original scalar `observed_nested_mr_result` calculation at tight numerical tolerances.

A second operational defect was corrected: a resource-gate failure previously raised before `resource_preflight.json` was written. The preflight now returns a typed PASS/FAIL record with elapsed time, projection, peak RSS, cell counts and an explicit no-adjudication marker; the executor writes that artifact before raising on FAIL. A deterministic regression exercises the over-4.5-hour branch and verifies the timing evidence is retained.

Governed static validation:
- Run [44843034684](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44843034684), commit `6a79cecaee6b60037c5203ec480f63a32ba237aa`: **181 tests PASS**, including vectorized-vs-scalar equivalence; CPython 3.12.10, pinned dependencies and compile step passed.
- Run [44843094528](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44843094528), commit `352a29da07879eb9d9ce6bc226a57af2540cc756`: **182 tests PASS**, including the persisted failed-preflight artifact regression; CPython 3.12.10, pinned dependencies and compile step passed.

These are deterministic software tests, not a measured G7 speedup. The revised code has not yet been benchmarked against the 4.5-hour projection gate. The previous G7 authorization was one-use and is consumed; the revised code requires a fresh authorization branch hash-bound to this exact snapshot before any new preflight. No K/B, seed, coverage, replay or scientific-scope constraint is relaxed. G7 remains AUTHORIZED AT PROGRAMME LEVEL / NEW EXECUTION AUTHORIZATION PENDING; no prospective holdout or coverage result exists.


### 9.19 Hash-bound retry authorization — current execution state (2026-11-21)

The first replacement authorization attempt `C10S-F5-G7-20261121-003` failed closed at source-inventory validation because the `gaussian_oracle_sha256` field had been transcribed with two hexadecimal characters missing. No approved-code checkout or G7 computation occurred on that attempt. The digest was recomputed from the exact approved source file and its 64-character length checked.

Corrected one-use authorization:
- authorization ID: `C10S-F5-G7-20261121-004`;
- authorization commit: `d7fd9ac32badcbee192364e3e7bbeb53a60045ca`;
- sole parent / approved code commit: `b0d1f53198e6f56520f9a872e48f8a027cbe4fdf`;
- workflow: [44843498295](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44843498295);
- source-hash inventory, parent identity, authorization window, frozen protocol and scope validator: **PASS**;
- exact approved research-code checkout and locked dependency installation: **PASS**;
- latest observed job state: resource preflight / primary / replay executor step **IN_PROGRESS**.

The corrected attempt is bound to the vectorized C5 bootstrap snapshot and the new preflight-evidence persistence behavior. It is the first execution that can measure whether that optimization brings the full primary-plus-replay projection below the unchanged 4.5-hour limit. Until the preflight artifact is available, no speedup or G7 calibration outcome is claimed.


### 9.20 G7 retry #004: measured resource failure and preflight emission warning — 2026-11-21

Run [44843498295](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44843498295), authorization ID `C10S-F5-G7-20261121-004`, completed with conclusion **FAILURE**. Authorization/hash validation, approved-code checkout, pinned dependencies and artifact upload all passed. The executor stopped only because the resource preflight returned `G7_RESOURCE_PREFLIGHT_PROJECTS_OVER_4_5_HOURS`; primary calibration and clean-source replay were not run.

The uploaded artifact (ID `14692240291`, SHA-256 `24c4ee485b93961bbc6cd6d3c36c91410c0c36c62e8e7565edc2fc9f77526567`) records:
- resource-only sample: 100 datasets per cell, 200 total;
- elapsed preflight: 14,583.034 s (4 h 03 min 03 s);
- projected primary plus replay: 291,660.689 s (81 h 01 min 01 s);
- unchanged ceiling: 16,200 s (4 h 30 min);
- peak RSS: 145,064 KiB;
- coverage adjudication: `NOT_PERFORMED`.

Thus the count-vector C5 vectorization and artifact-persistence fix are validated as software changes but have **not** made the end-to-end workload resource-feasible. The earlier claim that scalar C5 reconstruction was the dominant runtime bottleneck was not supported by component-level timings; the new measurement shows only that the aggregate optimization is insufficient. No further full G7 attempt should be made until a bounded profiler identifies the time distribution across C0 bootstrap, production/analytic fitting, exact global certification, C5 bootstrap and serialization. Any profiling must use resource-only synthetic seeds and leave K/B, the holdout namespace and coverage adjudication untouched.

A second, scientifically material warning appears in the same resource-only sample:
- `F5_beta22_M10_R5`: 67 `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`, 19 `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED`, 14 `GLOBAL_MAXIMUM_ORDER_UNRESOLVED`;
- `F5_beta22_M30_R20`: 100 `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`.

This is not a coverage result: the resource namespace is not the prospective holdout and adjudication was explicitly not performed. However, the current C5 path requires `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`; both a certified boundary supremum and an unresolved global ordering return before interval construction. Therefore, for these 100 M10/R5 resource datasets, C5 interval emission is bounded above by 67/100 (and may be lower due to other abstention causes). The frozen G7 adjudicator requires interval emission >=0.95 separately for each C5 target and cell. If this pattern persists in the holdout, G7 cannot pass even if runtime is solved.

This exposes two independent blockers, not one:
1. **Computational:** the certified-fit pipeline must be profiled and materially accelerated without reducing K=1,000, C0/C5 B=1,000, replay, or the 4.5-hour gate.
2. **Statistical/operational:** boundary-supremum and unresolved-census cases need a scientifically justified interval/abstention disposition compatible with the frozen >=0.95 emission requirement, or the current C5 candidate must be declared unsuitable for M10/R5. Do not relabel boundary suprema as interior maxima, silently drop cases, lower the emission threshold, or use the resource sample as a coverage estimate.

The next engineering action is a bounded component-level resource profiler plus a review of the M10/R5 boundary/unresolved disposition. No new G7 holdout execution is authorized by this failure; no primary/replay bank or coverage result was produced. G7 remains NOT EXECUTED / RESOURCE GATE FAILED, and the Tier-A candidate is not yet validated.


### 9.21 F5 exact-certificate performance optimization and G7 execution redesign — 2026-11-21

The first component profile, [run 44913152875](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44913152875), passed the governed comparator tests and measured one resource-only dataset per G7 cell. For M30/R20, the exact global-MLE certificate consumed 164.32 s of a 164.60 s full comparison. P/A/I fitting, C0 and vectorized C5 bootstrap together were negligible by comparison. This corrects the earlier hypothesis that separating P/A/I would materially reduce the 81-hour projection: it would not.

The certificate-internal profile, [run 44925170868](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44925170868), isolated the M30/R20 cost:
- 94.00 s in tensor-product Bernstein coefficient construction;
- 41.32 s in exact axis-content/common-component GCD;
- 23.27 s in exact removal of non-interior axis factors;
- 4.25 s in conditional-mean tube/exclusion;
- 1.08 s in Krawczyk;
- 0.92 s in exact likelihood enclosure.

A semantics-preserving exact-arithmetic optimization was then implemented at commit `5d3174de14fe9f5a5a19ddc5a97a44d7a7da88d8`:
- Bernstein basis matrices are represented by integer numerators and a positive common denominator; tensor transforms are performed over integers, with exact rational values materialized only at API boundaries;
- univariate GCD uses primitive integer pseudo-remainder sequences over Q rather than repeated Fraction Euclidean divisions;
- endpoint linear factors are divided by exact integer synthetic division.

The same resource-only M30/R20 dataset, same resource seed, same K=1 and B=1,000 was profiled after the optimization in [run 44926034181](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926034181), artifact ID `14716260010`, SHA-256 `6263ef767de7152429d0c2427aaba62c60d2fe5e5f83296545e0344445953518`:
- full dataset comparison: 24.676 s versus 164.601 s before (6.67× faster);
- certificate still returned `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`;
- complete census unchanged: 21 concentration intervals processed, 10 excluded, 11 Krawczyk attempts, one simple root certified, zero unresolved intervals;
- exclusive hot spots after optimization: 10.03 s Bernstein calls, 9.41 s Krawczyk (including derivative Bernstein ranges), 3.02 s mean-tube work, 0.22 s axis common-component checks, 0.12 s axis-factor stripping.

Governed F5 tests passed on [run 44925771538](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44925771538), commit `5d3174de14fe9f5a5a19ddc5a97a44d7a7da88d8`; additional exact GCD and synthetic-division regressions passed on [run 44926090717](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926090717), commit `186ce896fe264f47d3c379f05995f047b961ef7e`. No floating-point approximation, budget reduction, seed change, K/B reduction, or coverage relaxation was introduced.

The single-dataset speedup is not yet a validated full-bank runtime projection. A full resource-only latency sample (K=100 per cell, C0/C5 B=1,000, disjoint resource namespace, no coverage adjudication) is now running as [run 44926453920](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926453920). It records per-dataset timings and conservative shard-size projections; it is not a holdout or calibration run.

#### G7 execution architecture correction (design requirement before any new prospective authorization)

The current `execute_g7` bundles resource preflight, the full primary bank and the full replay in one sequential job. This repeats the resource preflight on every retry and does not provide shard-level checkpointing. The next executor/workflow revision must instead provide separate dependent stages in one hash-bound workflow run:

1. **Resource preflight:** run once for the approved code/environment snapshot, upload its immutable timing/status artifact, and do not repeat it when later stages are retried.
2. **Primary bank:** matrix-sharded by frozen cell and global replicate-index range. Each shard writes an atomic, hash-manifested result artifact. The full K=1,000 denominator and global seed schedule remain unchanged.
3. **Clean-source replay:** start only after all primary shards pass integrity checks; rerun the same seeds and shard boundaries independently. Each replay shard is compared with its corresponding primary shard.
4. **Adjudication:** start only after all primary/replay shard pairs are present, complete, and digest-equal. Reconstruct the full 1,000-dataset denominator per cell before applying the unchanged no-pooling metrics and G7 criteria.
5. **Recovery:** rerun only failed or missing shards. Successful preflight, primary, and replay artifacts remain reusable within the workflow run; no completed 1,000-dataset bank is repeated because one later shard failed.

Each compute job must have a hard timeout below three hours (target 150 minutes, workflow ceiling 165 minutes). Shard size and `max-parallel` are to be selected from the full resource-only p95/p99 timings, not guessed from one dataset. The expected hosted-runner parallelism is a scheduling parameter, not a scientific assumption; the design must remain correct if GitHub schedules fewer jobs concurrently.

The 81-hour sequential projection must be replaced by a measured parallel wall-time projection while also reporting total runner-compute hours. These are distinct quantities and neither may be hidden. K=1,000, C0/C5 B=1,000, the holdout namespace, primary/replay identity, exact certificate requirements, interval-emission threshold and coverage criteria remain frozen.

No prospective G7 holdout has been run. The current G7 v1.0 one-use authorization is consumed and bound to the earlier monolithic executor; the staged/sharded executor requires a new protocol/source-hash snapshot and a fresh explicit one-use authorization before any holdout computation. The separate M10/R5 boundary/unresolved emission blocker in §9.20 remains open and is not solved by this performance work.


### 9.22 Resumable G7 shard executor and workflow implementation — 2026-11-21

The staged execution implementation is now present on the research branch:
- `c10s_f5_g7_shard_execution.py`: global replicate-index shard generation, canonical per-shard record digest, and rehydration into the existing matched-dataset adjudicator.
- `execute_c10s_f5_g7_tiera_shard.py`: independent primary/replay shard entry point.
- `aggregate_c10s_f5_g7_tiera_shards.py`: gap/overlap, seed, truth, roster, row-digest, per-shard primary/replay and full-bank digest checks; reconstructs each full K=1,000 cell and invokes the unchanged adjudicator once.
- `validate_c10s_f5_g7_resource_profile.py`: validates a reusable resource-only profile, verifies the compute-path source files are byte-identical to the profile source snapshot, and derives the shard matrix from the worst observed per-dataset latency (not the mean).
- `C10S_F5_G7_EXECUTION_ARCHITECTURE_001.md`: records the execution-only design and no-repeat/recovery contract.

The G7 workflow has been replaced by distinct authorization, resource-profile validation, primary matrix, replay matrix and final-adjudication jobs. Primary and replay are separate matrix stages (up to 20 concurrent jobs), with 165-minute job timeouts and a 150-minute measured-work budget. The preflight profile is reused; it is not recomputed on downstream retries. Completed shards are preserved as immutable artifacts and the workflow dependency graph prevents replay from starting before the entire primary matrix succeeds.

Equivalence/integrity tests cover:
- byte-equivalent shard-0 records against the former monolithic `run_cell` path;
- global replicate indices and unchanged seed derivation for non-zero shards;
- rehydrated shard adjudication matching the monolithic adjudicator;
- complete primary/replay aggregation and profile-manifest integrity.

The static workflow, staged G7 YAML syntax check, compilation and 188 deterministic tests passed on [run 44930084805](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44930084805). This is software validation only; it is not a G7 holdout result.

The full 100-dataset-per-cell resource latency profile remains in progress as [run 44926453920](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926453920). Its immutable JSON and artifact metadata must be persisted before the profile validator can derive and freeze the actual shard size. No holdout primary or replay computation has been started.


### 9.23 Resource-profile completion and corrected shard plan — 2026-11-22

This section supersedes the earlier statement in §9.22 that the 100-dataset resource profile was still running. It completed successfully on [run 44926453920](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926453920); the immutable artifact and JSON/archive digests are recorded in `C10S_F5_G7_RESOURCE_PROFILE_MANIFEST_001.json` and `C10S_F5_G7_EXECUTION_ARCHITECTURE_001.md`.

A full comparison of candidate shard sizes (25, 40, 50, 100) found that the earlier 50-row choice was not optimal. The regression test has been corrected to require the actual minimum-wall-time candidate: **25 datasets per shard**, 4 shards per cell, 8 jobs per phase. At the configured 20-job parallelism ceiling, the conservative serialized-by-cell projection is 28.15 minutes per phase and 56.30 minutes for primary plus replay. Adding the already completed 41.15-minute resource-only profile gives **97.45 minutes (1.62 hours)** end-to-end. The worst observed shard estimate, including 5-minute setup, is 22.73 minutes. Aggregate runner-compute projection remains 13.72 hours; it is distinct from elapsed wall time.

This is an execution-plan correction only. It does not change the frozen G7 protocol, K=1,000 per cell, C0/C5 B=1,000, seed namespaces, method roster, coverage/emission criteria, replay equality or adjudication. It does not start the holdout bank. The plan still requires a successful live validation of the downloaded immutable profile and a fresh one-use authorization bound to the exact staged executor before any primary/replay computation.


### 9.24 Denominator correction to §9.23 — 2026-11-22

The 25-dataset plan stated in §9.23 was based on an incorrect denominator substitution and is superseded. The resource profile contains K=100 observations per cell solely to estimate per-dataset runtime. The prospective G7 holdout remains frozen at **K=1,000 per cell**. The shard planner correctly uses `g7.K_PER_CELL=1,000` when calculating shard count and waves. Consequently, 25-row shards require 40 shards per cell and two waves; 50-row shards require 20 shards per cell and one wave. The minimum conservative wall-time candidate is therefore **50 datasets per shard**, 20 jobs per cell and 40 jobs per phase. The worst-observed shard estimate including setup is 40.46 minutes (M30/R20) and 5.84 minutes (M10/R5); conservative serialized-by-cell wall time is 46.30 minutes per phase, 92.59 minutes for primary plus replay, and **133.75 minutes (2.23 hours)** including the one-time 41.15-minute resource-only preflight. Aggregate primary-plus-replay runner compute remains 13.72 hours. No scientific denominator or protocol has changed; this corrects only the execution projection and restores the test expectation to the frozen K=1,000 contract.


### 9.25 Live resource-profile validation and software gate — 2026-11-22

[Run 44968818184](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44968818184) passed. It downloaded resource artifact `14717426261` from run `44926453920`; the artifact archive digest and profile JSON digest matched the persisted manifest. The source-compatibility check passed: the profile source commit is an ancestor and all compute-path source files are byte-identical.

The validated plan uses the frozen holdout denominator K=1,000: 50 datasets per shard, 40 jobs per phase, max-parallel 20. The conservative projection is 5,555.57 s (92.59 min) for primary plus replay and 8,024.76 s (133.75 min; 2 h 13 min 45 s) including the one-time resource-only profile. Aggregate primary-plus-replay runner compute is 13.7167 hours. Every shard's worst-observed estimate plus setup is below the 150-minute measured-work budget; workflow hard timeout remains 165 minutes.

The workflow YAML syntax check, source compatibility/profile validation, compilation and all 189 deterministic static tests passed. This establishes that the staged execution plan is internally consistent and under the requested three-hour wall-time ceiling **under the configured 20-job parallelism**. It is not a primary/replay run, coverage result, or scientific G7 PASS. No holdout data were generated.


### 9.26 G7 v1.0 replay-integrity failure and same-runner execution correction — 2026-11-22

This section supersedes the prior expectation that the v1.0 primary/replay matrix would yield an adjudicable bank. The one-use execution [run 44969714756](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44969714756) completed all primary and replay shards but failed the mandatory exact identity gate at F5_beta22_M10_R5:(300,50). The primary/replay digests differ, so the frozen protocol blocks coverage adjudication.

The affected artifacts (primary 14733425693, replay 14734427042) were downloaded and recursively compared. Dataset identities, row hashes, seeds, truths, point estimates and bootstrap interval outputs match. Differences are in the fitted beta-binomial parameters/log-likelihood and optimizer/audit diagnostics, including solver termination status/messages. This is a floating-point optimizer reproducibility failure across separate hosted runner jobs, not a data-generation or seed mismatch. No tolerance or rounding exception has been introduced.

**G7 v1.0 is INDETERMINATE.** The exact replay requirement in protocol v1.0 was not met. The v1.0 holdout is consumed and must not be regenerated or reused for another calibration attempt. No coverage claim is made.

A future-run execution correction has been prepared on this research branch: each shard now executes primary and then a clean-source replay from a fresh tree of the same approved commit on the same ubuntu-24.04 runner, with numerical-library thread counts fixed to one. This preserves separate primary/replay artifacts and the exact equality gate. A new unit test checks same-runner primary/replay record identity on a disjoint test namespace.

The revised workflow and test suite passed [run 45018483942](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45018483942): 190 deterministic tests, including the new paired replay test; G7 YAML syntax, immutable resource-profile compatibility and the frozen K=1,000 shard plan also passed. This is engineering validation only; it does not repair the consumed v1.0 bank or establish G7 calibration.

Any future prospective attempt requires a new protocol/authorization snapshot and an independent seed namespace, with the v1.0 scientific estimands, M/R cells, K=1,000, B=1,000, method roster, thresholds and no-pooling rules frozen unless a separately justified change is preregistered. The consumed v1.0 holdout remains excluded. main and canonical scientific claims remain unchanged.
