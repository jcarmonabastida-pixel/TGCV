# C10-S F5 — End-to-end closure dossier (research draft)

**Date:** 2026-11-20  
**Status:** OPEN — IMPLEMENTATION PARTIAL / GOVERNED VALIDATION NOT RUN  
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

The test source contains 76 deterministic test methods. This is a source-level count only. The tests have not been executed in the governed CPython 3.12 environment and no PASS is claimed.

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

- Run the complete 76-method suite under the canonical CPython 3.12 environment after integrity preflight.
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
| G1 exact score/input primitives | Implemented in research harness; governed execution pending | IMPLEMENTED / NOT VALIDATED |
| G2 complete interior census | Simple-root local census exists; projection roots not fully lifted; multiple roots and endpoint neighborhoods open | OPEN |
| G3 boundary/corner ingredients | Exact edge limits, edge root census, corner ownership and joint corner limits exist; integrated global adjudication not demonstrated | PARTIAL |
| G4 global likelihood ordering | No complete rigorous candidate-vs-boundary ordering engine | OPEN |
| G5 deterministic abstention | Several component-level limits/states exist; unified global result contract and ceilings not frozen | PARTIAL |
| G6 governed validation | 76 tests defined; no governed CPython 3.12 execution record | NOT RUN |
| G7 TierA relevance/calibration | No prospective calibration authorized or run | NOT RUN |

## 5. Known blockers that prevent honest F5 closure

1. Interior multiple-root certification: Krawczyk certifies simple roots only. The current algebraic route isolates projection roots but does not provide a complete subresultant/specialized-gcd lift with local multiplicity classification for all candidates.
2. Full open-domain coverage: the adaptive conditional-mean controller accepts only 0<t_-<t_+<1. Its success on a supplied interior interval does not cover neighborhoods of t=0 or t=1.
3. Projection-to-root lifting: Res_mu(P,Q) candidates must be lifted and verified against both original score equations; projection multiplicity is not local bivariate multiplicity.
4. Boundary/global ordering: exact edge and corner limits exist, but no integrated rigorous comparison of all interior and boundary likelihood candidates has been demonstrated.
5. Governed validation and calibration: the 76-test suite is unexecuted in CPython 3.12; no authorized prospective M10/R5 or M30/R20 calibration evidence exists.

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

Until all applicable items pass, the correct status is F5 OPEN — PARTIAL IMPLEMENTATION; GLOBAL MLE AND COVERAGE NOT CERTIFIED.

## 8. Governance and scientific boundary

This dossier is a research-branch design/coordination artifact. It does not modify main, RMA, Evidence→Claim Matrix, frozen F1/F5 contracts, B2/B3, or any scientific claim. It does not authorize execution. The canonical workflow remains: historical reconstruction → integrity preflight → explicit authorization → execution → primary audit → replay gate → final audit → scientific closure.

The purpose remains narrow: repair the fitting/coverage reliability limitation that blocked TierA, then return to the C10-S causal question of whether accessibility contributes to Value. F5 is not an independent statistical research programme.
