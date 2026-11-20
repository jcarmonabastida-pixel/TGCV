# C10-S — F5 global beta-binomial MLE certification design 001

**Record:** C10S-F5-GLOBAL-MLE-CERTIFICATION-001  
**Status:** BOUNDED F5 CALIBRATION SUPPORT DESIGN + EXACT SCORE / BERNSTEIN / KRAWCZYK / BOUNDARY / GLOBAL-LIKELIHOOD IMPLEMENTATION PRESENT — BOUNDED DETERMINISTIC FIXTURES PASS; GENERAL SINGULAR-ROOT COMPLETENESS AND PROSPECTIVE TIER-A VALIDATION OPEN  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** F5 beta-binomial count likelihood, M10/R5 and M30/R20  
**Execution authorization:** NONE

---

## 1. Purpose

Resolve only the F5 likelihood-fit ambiguity that blocks reliable interpretation and calibration of the existing C5 within/raw-between intervals after Tier A/B2/B3 failed their frozen component gates. The concrete target is the beta-binomial count likelihood in the two frozen designs, M10/R5 and M30/R20, under the existing beta22 fixture. The work is subordinate to C10-S and exists to make its Analyzer/Evaluator calibration trustworthy; it is not a separate statistical research programme or a general-purpose inference library.

The exact algebraic and Bernstein/interval operations are tools, not deliverables in their own right. Each additional layer must resolve a demonstrated ambiguity in the fitted likelihood or profile calculation that materially affects fit-state adjudication, interval emission, or coverage calibration. If existing analytic scores/Hessians, multi-start concordance, independent likelihood checks and explicit concentration-boundary comparisons can resolve the issue with adequate evidence, further algebraic escalation is unnecessary and must stop. No generic solver, new estimator family, new DGP family, or expansion beyond the two frozen F5 designs is authorized by this design.

Partial executable research primitives now exist for exact rational score numerators, concentration compactification, Bernstein box zero-exclusion, axis-aligned common-component detection, an exact projection resultant and Sturm isolation of projection coordinates. These are source-level implementations only. The implementation now includes conditional-mean Bernstein tube census, Krawczyk simple-root inclusion, exact one-edge profiles, uniform joint-corner limits, exact rational likelihood enclosures and a global-likelihood adjudicator. The bounded M30/R20 fixture and a smaller nondegenerate fixture pass deterministic tests. General singular/multiple interior-root certification remains unresolved and must fail closed; no universal global MLE claim is made. No prospective TierA calibration or scientific run is claimed.

## 2. Likelihood in finite-product form

For observed world counts x_i in {0,...,r}, let n_x be the number of worlds with count x, M=sum_x n_x, and parameterize alpha=mu*kappa, beta=(1-mu)*kappa, with 0<mu<1 and kappa>0.

Ignoring the data-only binomial coefficient, the log-likelihood is

```
ell(mu,kappa) = sum_x n_x [
    sum_{j=0}^{x-1} log(mu*kappa+j)
  + sum_{j=0}^{r-x-1} log((1-mu)*kappa+j)
  - sum_{j=0}^{r-1} log(kappa+j)
].
```

Empty sums are zero. This follows from the rising-factorial identity for the beta-binomial PMF. The omitted combinatorial terms are restored for reported likelihood values but do not affect stationary points.

## 3. Key theorem: unique conditional mean maximum

For fixed kappa>0, each observation contributes

```
sum_{j=0}^{x-1} log(mu*kappa+j)
+ sum_{j=0}^{r-x-1} log((1-mu)*kappa+j)
```

to ell. Its second derivative with respect to mu is

```
- sum_{j=0}^{x-1} kappa^2/(mu*kappa+j)^2
- sum_{j=0}^{r-x-1} kappa^2/((1-mu)*kappa+j)^2.
```

For any nondegenerate dataset with 0 < sum_i x_i < M*r, the aggregate second derivative is strictly negative for every mu in (0,1): at least one of the two sums contributes a strictly negative j=0 term. Therefore ell(mu,kappa) is strictly concave in mu at fixed kappa and has exactly one interior conditional maximizer. If all counts are zero or all counts are r, the mean maximizer is the corresponding degenerate boundary and is handled separately.

Consequences:
- no grid over mu is needed to discover competing conditional maxima;
- the conditional score has at most one interior zero for every fixed positive kappa;
- every finite interior joint stationary point is a stationary point of the one-dimensional profile ell_p(kappa)=max_mu ell(mu,kappa);
- multiple global/local maxima, if present, must arise along concentration, not from multiple conditional mean maxima at a fixed concentration.

This theorem is analytic and does not depend on B2/B3.

## 4. Rational score equations

Differentiating the finite-product likelihood gives the exact rational scores:

```
S_mu(mu,kappa) = sum_x n_x [
    sum_{j=0}^{x-1} kappa/(mu*kappa+j)
  - sum_{j=0}^{r-x-1} kappa/((1-mu)*kappa+j)
].

S_kappa(mu,kappa) = sum_x n_x [
    sum_{j=0}^{x-1} mu/(mu*kappa+j)
  + sum_{j=0}^{r-x-1} (1-mu)/((1-mu)*kappa+j)
  - sum_{j=0}^{r-1} 1/(kappa+j)
].
```

Every denominator is strictly positive in the open parameter domain (0<mu<1, kappa>0). Multiply each score by a common denominator formed from its positive factors to obtain exact bivariate polynomials P(mu,kappa) and Q(mu,kappa). The resulting equations P=0 and Q=0 have exactly the same common zeros as the original scores in the open domain; denominator roots are outside that domain and must never be treated as candidates.

The coefficients are rational/integer because r, x and n_x are integers. Construct them exactly (integer/rational arithmetic), not by fitting coefficients from floating-point evaluations.

## 5. Exhaustive stationary-point enumeration — implemented bounded route

The current implementation is interval-first, with exact elimination retained as fallback/cross-check. This ordering follows the project decision to develop Bernstein and algebraic certification in parallel without prematurely selecting a universal method.

1. Construct the paired rational score numerators P(mu,kappa), Q(mu,kappa) exactly from one validated count histogram. Their open-domain zero set agrees with the two rational score equations because all cleared denominator factors are strictly positive for 0<mu<1 and kappa>0.
2. Compactify concentration with t=kappa/(1+kappa), preserving the interior zero set on 0<t<1 and treating t=0,1 as boundary strata.
3. Use strict conditional concavity in mu. For each rational t interval, exact Bernstein bounds at rational mean witnesses construct a tube containing the unique conditional-mean root for every finite t in that interval.
4. Apply tensor-product Bernstein bounds to Q over that tube. A strict sign excludes the entire t interval. Otherwise, exact rational Krawczyk inclusion is attempted to certify one simple common root in the box.
5. Bisect inconclusive concentration intervals under deterministic interval/depth/mean-depth ceilings. A complete interval-first census is returned only when every interval is either excluded or certified to contain exactly one simple root. Multiple/singular roots, endpoint ambiguity and unprocessed budget remainders remain explicitly unresolved; they are never promoted to simple roots.
6. If the interval-first route is incomplete, compute the exact concentration resultant and isolate its distinct real projection roots with square-free/Sturm machinery, retaining multiplicity metadata. Each interior projection candidate is then lifted through the same conditional-mean tube and Krawczyk procedure. The resultant is a candidate projection, not proof of a bivariate stationary point. Mixed common factors or unresolved lifts prevent a complete census.
7. Profile all four open-domain boundary strata exactly and establish the four joint-corner limits by uniform moment bounds (see §6). These are closed-form evaluations, not an iterative boundary-root search.
8. Enclose every certified interior candidate's likelihood by exact rational probability intervals with outward-rounded dyadic accumulation. Compare these enclosures with exact boundary suprema. Return a global classification only when strict interval ordering or a certified boundary co-maximum establishes the winner; otherwise return a typed unresolved state.

The strict-concavity theorem guarantees at most one conditional-mean root for each finite positive concentration. It does not imply that the one-dimensional concentration profile has only one stationary point. The census must therefore cover the full compactified concentration interval, not a local optimizer neighborhood.

### Scope of the implemented certificate

The current axis-content detector classifies common factors depending only on mu or t. It does not claim to classify every general mixed bivariate common factor. A zero resultant, a mixed common component, a non-simple interior lift or any incomplete interval/Sturm state blocks exhaustive/global status. This is intentional fail-closed behavior, not an implicit certificate.

The bounded M10/R5 and M30/R20 deterministic fixtures exercise the integrated global wrapper. The M30/R20 fixture requires the full-domain Bernstein route, exact likelihood interval ordering and the declared globality basis. These fixtures do not establish a universal theorem for every possible histogram at those M and R values.

## 6. Boundary strata and their profiled likelihoods

The open domain is noncompact. A global certificate must compare every interior stationary candidate against all relevant boundary limits; finite optimizer bounds are never substitutes.

### 6.1 Concentration kappa -> infinity

The beta-binomial converges to Binomial(r,mu). The profiled boundary mean is the pooled proportion

`mu_inf = sum_i x_i/(M*r)`.

Evaluate the exact binomial-limit log-likelihood at this mean, including the binomial coefficients. This is a candidate supremum on the closure, not an interior finite-kappa MLE.

### 6.2 Concentration kappa -> 0

For fixed 0<mu<1, the mixing distribution converges to a two-point law on p=0 and p=1:
- P(X=0)=1-mu;
- P(X=r)=mu;
- P(0<X<r)=0.

If any observed world count is interior, the limiting sample likelihood is minus infinity. If all observations are endpoints, the profiled boundary mean is the fraction of worlds with X=r, and the boundary log-likelihood is the corresponding endpoint-mixture likelihood. The all-zero/all-r cases are handled by their degenerate limits.

### 6.3 Mean boundaries mu -> 0 or mu -> 1

The predictive distribution degenerates at X=0 or X=r respectively. The boundary likelihood is finite only if all observed counts equal that endpoint; otherwise it is minus infinity. These cases are separately classified and must not be represented as finite optimizer-bound solutions.

### 6.4 Corners and path limits

Evaluate the closure strata and their intersections explicitly. In particular, kappa->0 with mu->0 or 1 is included in the endpoint-mixture closure; kappa->infinity with mu->0 or 1 is the corresponding degenerate binomial endpoint. If a path-dependent corner is identified that is not covered by these strata, the boundary analysis is incomplete and the fit abstains.

## 7. Global adjudication

A global fit is certified only when:
- the stationary-point enumeration is exhaustive over the open domain;
- every candidate is domain-verified;
- every candidate and boundary likelihood is evaluated with outward-rounded enclosures;
- the maximum candidate/boundary ordering is resolved, or a set of co-maximizers is certified;
- no algebraic, interval, precision or resource limit has been exceeded.

A certified finite interior maximizer may be selected even if one or more heuristic optimizer starts reported failure, provided the global algebraic certificate independently establishes it. Conversely, all optimizer starts reporting success does not establish globality.

If two distinct parameter points are certified as co-maximizers, report a non-unique MLE set. If their W/B functionals agree but kappa/mean differ, retain the parameter non-identification and functional equivalence separately. If likelihood enclosures overlap without a proof of equality or ordering, report `GLOBAL_MAXIMUM_ORDER_UNRESOLVED`.

No likelihood-difference tolerance is used to decide whether two candidates are equal. Equality is established by exact algebraic identity where possible; otherwise interval refinement must prove ordering, and failure to do so is abstention.

## 8. Typed outcomes

Add the following global-certificate states, distinct from optimizer termination:
- `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED`;
- `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED`;
- `GLOBAL_CO_MAXIMIZERS_CERTIFIED`;
- `NONISOLATED_STATIONARY_SET`;
- `WEAK_OR_NONIDENTIFIED_FUNCTIONAL_SET`;
- `GLOBAL_MAXIMUM_ORDER_UNRESOLVED`;
- `ALGEBRAIC_CERTIFICATE_UNAVAILABLE`;
- `BOUNDARY_SUPREMUM_UNRESOLVED`;
- `NUMERICAL_INTERVAL_CERTIFICATE_UNRESOLVED`.

Optimizer status remains a separate diagnostic field. Do not collapse termination failure, statistical weak identification and global-certificate failure into one status.

## 9. Relationship to F1 and M2 W/B profiles

The global MLE certificate supplies the unconstrained likelihood supremum used by M2. It does not by itself certify every constrained W/B profile.

For fixed W=w or B=b, use the exact one-dimensional nuisance reduction already defined in the successor interval-method specification. Its constrained stationary points must receive the same exhaustive root-isolation treatment, now with the target constraint substituted into the rational likelihood score. Compare every constrained stationary candidate with its constrained boundary endpoints. A profile segment is certified only when all its stationary candidates and endpoints are ordered. The accepted confidence set is the union of all certified target segments; unresolved segments force profile abstention.

The F1 near-degenerate-root work should share the exact polynomial/root-isolation primitives, interval arithmetic and multiplicity-preserving representation. It must not use the F5 likelihood certificate as evidence about the separate algebraic reconstruction target; reuse is at the numerical-certification infrastructure level only.

## 10. Deterministic adversarial test contract

Before any numerical bank:
1. Verify the rising-factorial likelihood equals the existing `betaln` likelihood over exact small count fixtures.
2. Verify analytic rational scores against the existing digamma score/Hessian and independent log(alpha)/log(beta) derivatives.
3. Verify strict conditional concavity for nondegenerate fixtures and the all-zero/all-r exceptions.
4. Include fixtures with a single interior concentration stationary point, multiple concentration stationary points, an even-multiplicity stationary root, two arbitrarily close distinct roots, a non-isolated/common-factor case, and no interior stationary root.
5. Verify Sturm isolation counts roots without relying on sign changes and preserves multiplicity.
6. Inject a root-isolation resource limit and confirm fail-closed `ALGEBRAIC_CERTIFICATE_UNAVAILABLE`.
7. Verify all boundary strata against direct limiting PMF calculations, including all-zero, all-r, endpoint-mixture-only and at-least-one-interior-count fixtures.
8. Verify global likelihood ordering by interval enclosures; unresolved overlaps must abstain.
9. Verify heuristic optimizer failures do not overturn a valid global certificate and optimizer successes do not manufacture one.
10. Verify no B2/B3 data are used for coefficient tuning, threshold selection or method selection.

The fixtures must be deterministic and hand-constructed or algebraically specified. No stochastic bank is part of this test suite.

## 11. D1 disposition and current evidence

The original D1 design route is now implemented in a bounded form, but the design/comparison decision is not frozen and no method is selected as universally superior. The production order is Bernstein/conditional-mean first, exact resultant/Sturm as fallback and cross-check.

Evidence currently available:
- Exact rational score numerators are checked against an independent direct-rational score oracle on a small fixture and the M30/R20 fixture.
- Strict conditional concavity, compactification, Bernstein range enclosure, Krawczyk simple-root inclusion, multiplicity-preserving fail-closed behavior, edge profiles and joint-corner limits have deterministic adversarial tests.
- The M10/R5 nondegenerate fixture and M30/R20 fixture pass the integrated global-MLE wrapper, including exact rational likelihood ordering against all boundary profiles and corners.
- Run [44767224308](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44767224308) (commit `a9a56d7c142b441b0893858c75e13a38ae38a9a2`) passed 135 tests. Run [44770409949](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44770409949) (commit `4eda28ed28b23eacf641a81bc29705f1dd52d87d`) passed 136 tests, including the subsequent likelihood-input integrity regression.
- General singular/multiple interior-root lifting and arbitrary mixed common-component classification remain unresolved by design; these cases must abstain. The exact resultant/Sturm fallback preserves projection multiplicities but does not by itself prove a bivariate lift.
- The current active-resource contract is being hardened and revalidated in run [44771555687](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44771555687), commit `3591a63e095a67aa0dfaeae2df5528076a90b708`.

D1 must not be described as universally closed or as a selected method. Its bounded implementation evidence is sufficient to continue F5 engineering closure, while the remaining G1–G6 audits and adversarial contracts stay explicit in the end-to-end closure dossier. No stochastic TierA calibration, new bank, Analyzer/Evaluator scientific execution or coverage claim is authorized by this design. Prospective TierA calibration remains G7 and requires separate explicit authorization.

## 12. Deterministic symbolic-sizing probe (2026-11-20; not scientific execution)

A local static algebra prototype was attempted using exact rational polynomial construction and a general-purpose symbolic resultant implementation. The inputs were hand-constructed deterministic count fixtures, not generated from the F5 DGP and not drawn from B2/B3.

- M10/R5 fixture: the exact score-numerator polynomials had bidegrees (9,15) and (10,13); the exact resultant completed in approximately 0.40 seconds, with degree 235 in kappa.
- M30/R20 fixture: exact score-numerator construction completed in approximately 5.7 seconds, with bidegrees (39,60) and (40,58). The general-purpose exact rational resultant did not complete within the 60-second tool limit. No resultant or root count is claimed for this fixture.

This probe demonstrates that naive rational subresultant computation is not yet an acceptable D2 engine for M30/R20. It is a static symbolic computation, not a scientific run, bootstrap, calibration or coverage evaluation.

### Required implementation route refinement

Before coding the F5 certificate, select and validate one exact elimination backend:
- preferred candidate: modular subresultant/resultant over several good primes, with exact Chinese-remainder reconstruction, a rigorous coefficient bound, rational reconstruction where needed, and independent verification modulo additional primes;
- alternative: an exact bivariate real-root isolation/CAD backend with a pinned, governed dependency and deterministic resource ceiling.

The current F1 isolator `c10s_f1_independent_root_isolator.py` is reusable as a conceptual and code base for exact rational Sturm isolation, but it deliberately rejects polynomial degree >3. Its existing adversarial suite already covers double/triple roots and very close distinct roots. It cannot be called unchanged for a degree-235-or-higher F5 resultant. A backward-compatible general-degree extension and its complexity tests are required, or a separate F5 isolator must be versioned.

No dependency lock has been changed. The existing vcont lock is not an F5 dependency contract and does not include a symbolic algebra backend. Do not add an unpinned dependency or silently borrow another harness's environment.

### Updated D1 exit condition

D1 remains OPEN. The mathematical reduction and exact elimination formulation are established, but the M30/R20 computational route is not yet feasible under the naive backend. The next D2-preparation operation is a bounded, deterministic comparison of modular-resultant and CAD/interval backends on hand-constructed M10/R5 and M30/R20 fixtures, followed by general-degree root-isolator validation. No scientific data, B2/B3 outcomes or prospective bank may be used for this engineering choice.


## 13. First exact algebra primitive implemented — rational score numerator construction (2026-11-20)

Two research-only harness files are now present:
- `harness/c10s_f5_rational_score_polynomials.py`
- `harness/test_c10s_f5_rational_score_polynomials.py`

The constructor uses sparse bivariate integer polynomials and exact prefix/suffix products of the finite-product likelihood denominators. It avoids symbolic expression expansion, floating-point coefficients and external dependencies. It returns the exact numerator pair for the rational scores, with separate minimal positive-domain denominators:
- `S_mu = N_mu / product_j[(mu*kappa+j)((1-mu)*kappa+j)]`;
- `S_kappa = N_kappa / product_j[(mu*kappa+j)((1-mu)*kappa+j)(kappa+j)]`.

The implementation was checked against direct rational score evaluation at three exact rational parameter points on a hand-constructed R=5 fixture. Four deterministic unit tests pass, including histogram validation and a hand-constructed M=30, R=20 histogram spanning all 21 count cells. For that M30/R20 fixture, the sparse numerator sizes are 629 and 1,368 terms, with bidegrees (39,40) and (40,58), respectively. Construction plus the four tests took approximately 0.5 seconds in the available Python 3.13 environment. This is a harness-level static result, not yet a parity claim for the governed CPython 3.12 execution environment.

The separate-denominator representation explains why bidegrees can differ from earlier sizing notes that cleared both scores against the larger shared denominator: multiplying N_mu by the positive product of the C_j=(kappa+j) factors raises its kappa degree by R without changing its zero set in the open domain. The implementation deliberately uses the smaller numerator and retains the denominator formula explicitly.

### Backend comparison status

The first exact score-numerator constructor is now implemented and tested. The elimination backend is not selected yet:
- A general-purpose exact rational resultant on the earlier M30/R20 sizing fixture exceeded the 60-second tool ceiling.
- A trial of SymPy's generic subresultant resultant routine over a finite field also exceeded the 60-second ceiling on the new sparse M30/R20 score polynomials. This is not a modular-CRT implementation and does not show that a properly engineered modular resultant will fail; it does show that simply changing the coefficient field inside the generic PRS routine is insufficient.
- No exact CAD/real-algebraic backend is installed in the available environment, so no CAD performance result is claimed.

Decision: do not select either generic SymPy PRS or CAD by assumption. Next compare a purpose-built modular subresultant/CRT path with an interval-certified one-dimensional profile path on the same deterministic M30/R20 fixtures. The latter exploits the strict conditional concavity in mu and may avoid constructing a high-degree resultant, but it must prove exhaustive stationary-root coverage, including even-multiplicity roots, or abstain. A bounded exact backend comparison is still required before D1 can close.

The implementation does not compute a resultant, isolate roots, evaluate likelihood enclosures, or certify globality. It is the first verified algebra layer only. No fit, bootstrap, calibration, coverage run, or scientific execution was performed.


## 14. Exact compactification of the concentration domain — implemented (2026-11-20)

The score-polynomial module now includes `compactify_concentration(P)`. For a sparse integer polynomial
\[
P(\mu,\kappa)=\sum_{i,j}c_{ij}\mu^i\kappa^j,
\qquad d=\max\{j:c_{ij}\ne0\},
\]
it returns the exact integer polynomial
\[
\widetilde P(\mu,t)=(1-t)^dP\!\left(\mu,\frac{t}{1-t}\right).
\]
The bijection \(t=\kappa/(1+\kappa)\) maps the open concentration domain \(0<\kappa<\infty\) to the bounded interval \(0<t<1\). Since \((1-t)^d>0\) there, the transformation preserves the interior zero set exactly. It is implemented using integer binomial coefficients only.

The endpoints are deliberately excluded from interior root enumeration:
- \(t=0\) represents the \(\kappa\to0\) boundary;
- \(t=1\) represents \(\kappa\to\infty\), and its value is governed by the leading-concentration coefficient polynomial.

Endpoint likelihood limits remain separate boundary candidates; endpoint roots of the compactified score polynomial must not be misreported as finite interior stationary points. Each score numerator is compactified with its own actual concentration degree; their degrees need not match.

Three additional deterministic tests were added: exact M30/R20 score identity at rational parameter points, exact compactification identity at rational points, and preservation of an interior zero under the map. The transformation identity was also independently checked with exact rational arithmetic in a separate scratch calculation. The repository test suite has not been executed in the governed Python 3.12 environment; these tests are committed, not yet reported PASS.

### What this does and does not solve

This removes the unbounded concentration coordinate from the prospective elimination and interval-certification interfaces. It does not itself isolate roots, prove there are no even-multiplicity roots, order likelihood candidates, or certify the global MLE. The next implementation layer must operate on the compactified pair and provide a complete certificate on the open unit interval while treating both endpoints explicitly.


## 15. Historical asset reuse check — compatibility boundary (2026-11-20)

The harness already contains relevant numerical assets; they have been inspected rather than recreated:

1. `c10s_f1_independent_root_isolator.py` and its tests provide exact-rational Sturm isolation, square-free multiplicity handling, and adversarial double/triple/close-root fixtures. Its explicit degree ceiling is three. Reuse the mathematical test patterns and fail-closed semantics, not the implementation unchanged for the high-degree F5 elimination polynomial.
2. `c10s_f1_between_profile_likelihood.py` solves a balanced Gaussian random-intercept F1 nuisance profile. Its score polynomial and one-stationary-point argument are model-specific and do not transfer to the beta-binomial F5 likelihood.
3. `c10s_f5_beta_binomial_mcse_profile.py` already handles both mean branches and analytic concentration limits for a scalar MCSE target. However, its finite-concentration search uses a 241-point grid plus local scalar refinement and explicitly describes itself as numerical/diagnostic rather than globally certified. Its branch/limit bookkeeping can inform interface design, but its objective constraint and search cannot certify the F5 MLE or W/B profiles.

Accordingly, the current work is not a restart from scratch: it reuses the exact F1 isolation/adversarial semantics and the F5 MCSE branch/boundary representation while adding the missing high-degree global stationary certification for the distinct beta-binomial MLE and W/B targets. No existing F1 or MCSE behavior is modified by this work.

## 16. Interval-route primitive added — Bernstein box exclusion (2026-11-20)

The research harness now implements exact tensor-product Bernstein coefficients for a rational rectangular box in compactified coordinates, plus a strict-sign exclusion predicate. If all Bernstein coefficients of either score numerator are strictly positive or strictly negative, that score has no zero in the closed box; hence the box contains no common stationary point. Mixed-sign coefficients remain inconclusive.

This gives the interval route a rigorous exclusion primitive. It does not prove root existence or uniqueness, isolate a root, or establish exhaustive coverage. The remaining interval certificate needs deterministic subdivision, a root-inclusion/uniqueness operator, resource-ceiling/abstention semantics, and separate boundary likelihood adjudication. Tests are committed but not yet executed in the governed CPython 3.12 environment. No global MLE certificate is claimed.



## 17. Exact Bernstein subdivision kernel — partial implementation (2026-11-20)

The F5 research module now contains an exact de Casteljau midpoint split for tensor-product Bernstein coefficient matrices. It subdivides along either compactified coordinate without converting the child rectangles again from the power basis. The operation uses `Fraction` arithmetic and returns both child coefficient matrices with an exactly shared interface.

The accompanying four unit tests cover each coordinate direction, a bivariate shared-edge identity, and malformed input rejection. They are committed but have not been executed under the governed CPython 3.12 runtime; this record makes no test PASS claim.

This is only the arithmetic kernel. The adaptive controller, exact box queue/order, resource accounting, boundary-stratum separation, and root inclusion/uniqueness procedure are still absent. For a simple root, Krawczyk/interval-Newton requires a verified nonsingular preconditioner and strict interval inclusion/contraction conditions. Multiple roots require multiplicity-aware deflation or explicit unresolved status; standard nonsingular-Jacobian inclusion is not presumed to work.

The interval method must cover the open finite-parameter domain exhaustively while separately classifying roots on compactification boundaries. No boundary point may be counted as an interior finite stationary point. Any box not excluded or certified at the resource ceiling forces an incomplete/abstaining global result.

D1 remains OPEN. No MLE certificate, method selection, governed test execution, benchmark, bootstrap, calibration, replay or scientific execution is claimed or authorized.



## 18. Deterministic Bernstein exclusion controller — partial implementation (2026-11-20)

A bounded breadth-first controller has been added on top of exact de Casteljau subdivision. It applies both score-polynomial Bernstein sign tests to each box, alternates the split axis by depth in a fixed order, and preserves rational box endpoints. The box-count and depth ceilings are explicit. Every unresolved or unprocessed box is returned with bounds and a typed reason.

The only conclusive zero-free outcome is `ALL_BOXES_EXCLUDED`, which means every box in the covered closed rectangle was excluded by at least one score. Depth exhaustion returns `UNRESOLVED_BOXES`; box-budget exhaustion returns `RESOURCE_LIMIT_WITH_REMAINDER`. Neither may be treated as a partial root certificate.

The controller is conservative at compactification boundaries: it covers the closed square and can therefore retain boxes containing boundary roots. Explicit boundary-stratum classification is still required for the open finite-parameter domain and likelihood supremum comparison.

Four controller tests are committed but not run in governed CPython 3.12. Root inclusion/uniqueness is still missing. Simple roots may be candidates for rational Krawczyk/interval-Newton certification under all theorem hypotheses; multiple roots require deflation or abstention. The controller never uses sign changes to exclude roots.

No global MLE certification, D1 closure, backend selection, benchmark, calibration or scientific execution is claimed or authorized.


### Multiple/near-coincident retention fixtures added (2026-11-20)

The interval exclusion test contract now includes a hand-constructed common double root and a pair of distinct common roots separated by `2^-20`. Current controller assertions require that neither case is declared root-free. They are preservation/negative-certification tests only; the controller does not yet isolate these roots or certify multiplicity. Governed CPython 3.12 execution remains pending.

### 19. Exact-rational input contract hardened (2026-11-20)

The Bernstein conversion, sign predicate, de Casteljau subdivision and adaptive exclusion controller now enforce exact input types at their public boundaries: integers and `Fraction` only. Binary floats are rejected rather than rationalized from their binary representation. The empty-polynomial conversion also validates the supplied rectangle before returning. Four adversarial tests were added for these rejection paths.

This closes an input-integrity gap, not a mathematical certification gap. The adaptive controller remains exclusion-only; it does not prove existence, uniqueness, multiplicity or global optimality. The closed-square boundary issue remains open. Tests remain unexecuted under governed CPython 3.12; no PASS or MLE certificate is claimed.

### 20. Adversarial fixture coefficient-contract correction (2026-11-20)

Three root-retention fixtures were statically inconsistent with the module's integer-coefficient polynomial contract: they supplied `Fraction` coefficients. They now use positive integer scalings of the same equations. The common-root fixture is `(2*mu-1, 2*t-1)`; the double-root fixture is their squared form; the near-coincident fixture uses integer factors with exact separation `2^-20`. Zero sets and multiplicities are unchanged. This is a fixture correction only; governed tests remain pending.

### Resource-budget fixture alignment (2026-11-20)

A final source scan found that the box-budget exhaustion test reused the simple common-root equations with `Fraction` coefficients. It has now been changed to the same integer-scaled equations (`2*mu-1`, `2*t-1`). Thus all four controller call sites in the adversarial tests honor the integer sparse-polynomial contract. This is a static source correction only; no test execution or PASS is claimed.

### Exact Krawczyk inclusion primitive — implemented, validation pending (2026-11-20)

The research harness now contains `krawczyk_certify_unique_root()`. It differentiates the integer sparse polynomials exactly, encloses each Jacobian entry over a rational rectangle using tensor-product Bernstein convex-hull bounds, evaluates the midpoint and rational preconditioner exactly, and forms the Krawczyk image with rational interval arithmetic. It emits `CERTIFIED_UNIQUE_ROOT` only when the Krawczyk image is strictly inside the box and an independently computed infinity-norm contraction upper bound is strictly below one. A singular midpoint Jacobian or failed inclusion/contraction returns an unresolved status.

A wrapper, `bernstein_krawczyk_root_classification()`, now composes the existing deterministic Bernstein exclusion partition with Krawczyk attempts on surviving leaves. Excluded leaves remain excluded; successful simple-root leaves are certified; multiple-root/singular leaves and resource remainders remain unresolved. Two deterministic tests were added: an affine simple root with exact dyadic coordinates and a double-root singular fixture that must abstain.

This is a local-box simple-root inclusion primitive, not exhaustive root isolation. It does not resolve multiple roots, boundary strata, overlaps/duplicate roots across adjacent closed boxes, or the global likelihood ordering. The wrapper currently attempts Krawczyk only after the exclusion controller reaches its configured depth; failed attempts are retained rather than adaptively refined further. All new tests remain unexecuted in governed CPython 3.12; no PASS is claimed.

### Exact one-edge boundary likelihood profiles — implemented, validation pending (2026-11-20)

The harness now exposes `beta_binomial_boundary_likelihoods(r, count_histogram)`. It computes exact rational likelihood values (including binomial combinatorial coefficients) for four separately profiled one-edge limits: concentration `kappa -> infinity` (Binomial limit, pooled mean), concentration `kappa -> 0` (endpoint two-point mixture, or zero likelihood if any observed count is interior), and mean boundaries `mu -> 0` / `mu -> 1` (degenerate-at-zero / degenerate-at-r limits). Four deterministic tests cover endpoint-only, interior-count, degenerate-mean and invalid-histogram cases.

These values are exact likelihood probabilities, not log-likelihood floats. They can be compared by rational ordering with one another, but not yet with interior algebraic stationary candidates. The helper deliberately marks simultaneous boundary-corner/path limits as unclassified: one-edge profiles do not establish all possible joint paths as two compactification coordinates approach their boundaries. It also does not yet classify stationary score roots on the compactification edges. No global maximum ordering or MLE certificate is claimed. Tests remain unexecuted under governed CPython 3.12.

### Adaptive Bernstein–Krawczyk refinement controller (2026-11-20)

The previous one-shot composition has been replaced by a deterministic breadth-first controller. Each rational box is first tested by exact Bernstein exclusion; a surviving box is passed to the exact Krawczyk simple-root test; an inconclusive box is bisected in alternating `mu`/`t` order until the depth ceiling. The box budget counts processed boxes. Every unprocessed queue item is emitted as `NOT_PROCESSED_RESOURCE_LIMIT`; every leaf at the depth ceiling retains its exact bounds and Krawczyk attempt. The controller reports processed boxes, Krawczyk attempts, subdivisions, exclusions, certified simple-root boxes and unresolved remainder separately.

Two deterministic tests were added for repeatable adaptive subdivision of a double-root fixture and fail-closed resource-budget exhaustion. These tests are committed but have not been executed in governed CPython 3.12.

This improves local refinement but does not close the proof gaps: shared-edge/vertex roots can remain unresolved, multiple roots are not deflated, closed-square boundary strata are not separated from the finite-parameter interior, and certified boxes do not yet constitute a global non-overlapping root census. No global MLE ordering or certification is claimed.

### Exact common-factor and multiplicity analysis on compactification edges (2026-11-20)

The research harness now includes `compactified_boundary_common_factors(poly_p, poly_q)`. It restricts both integer sparse score polynomials to each of the four edges of the compactified square (`mu=0`, `mu=1`, `t=0`, `t=1`), computes their exact univariate polynomial gcd over `Fraction`, and applies characteristic-zero square-free factorization to report common factors with their minimum shared algebraic multiplicities. If both restrictions vanish identically on an edge, the routine returns `COMMON_EDGE_COMPONENT_UNRESOLVED` rather than inventing a finite root list. Three deterministic tests cover a common double factor, a common edge component and malformed sparse inputs.

This is exact edge algebra, not yet root isolation: the rational factors still need Sturm-certified real-root isolation on the unit interval, endpoint/corner deduplication, and integration with the interior census. It also does not solve two-dimensional multiple roots or joint corner/path likelihood limits. The test file now contains 40 deterministic tests; none has been executed in governed CPython 3.12. No PASS or global MLE certificate is claimed.

### Exact Sturm isolation of compactification-edge common roots (2026-11-20)

The edge pipeline now continues beyond gcd and square-free multiplicity analysis. `compactified_boundary_common_roots()` applies exact rational Sturm sequences to each square-free common factor on the unit edge. It separates rational roots found exactly (including endpoints), returns rational isolating intervals with Sturm root count one for non-rational roots, and retains depth/interval-budget remainders as partial isolation. A shared edge component still fails closed. Three tests cover an exact rational double common root, an irrational root of `2*t^2-1`, and depth-limited abstention.

Corner deduplication between adjacent edges remains explicitly unperformed; a corner root may appear in two edge records until a canonical ownership rule is added. This edge solver does not yet classify the two-dimensional interior roots, joint corner/path likelihood limits, or global maximum. The test file now contains 43 deterministic tests, all still unexecuted in governed CPython 3.12. No PASS is claimed.

### Canonical corner ownership and deduplicated boundary census (2026-11-20)

The edge Sturm isolator now has a corner-census layer, `compactified_boundary_corner_census()`. Each compactification corner is owned exactly once by its vertical edge (`mu=0` owns `(0,0)` and `(0,1)`; `mu=1` owns `(1,0)` and `(1,1)`). The corresponding horizontal-edge occurrence is retained as `CORNER_REFERENCE_ONLY`, with factor index and edge parameter provenance. The result exposes a corner registry with coordinates, owner, multiplicity and all edge occurrences. If a vertical owner cannot be established, the corner is marked unresolved rather than silently dropped. Partial Sturm isolation remains partial even when all discovered corners have ownership.

Three deterministic tests were added: one shared corner with both edge references, all four corners with unique vertical ownership, and propagation of a depth-limited edge isolation. The test file now contains 46 deterministic tests. They remain unexecuted under governed CPython 3.12. This is only a deduplicated boundary-root census; it is not yet joined to the interior census, and it does not classify joint likelihood path limits or certify a global MLE.

### Joint compactification-corner likelihood limits classified (2026-11-20)

The harness adds `beta_binomial_joint_corner_likelihood_limits()`. For the beta-binomial count, `E[X]=r*mu`, so Markov's inequality gives `P(X>0) <= r*mu` uniformly over every positive concentration. Symmetrically, `P(X<r) <= r*(1-mu)`. Therefore the count distribution tends path-independently to the point mass at zero as `mu -> 0`, and to the point mass at `r` as `mu -> 1`, even when concentration simultaneously tends to zero or infinity. This classifies all four `(mu,t)` compactification corners for finite independent-world histograms: likelihood one iff every positive-multiplicity count equals the corresponding endpoint, otherwise zero. Four tests cover endpoint-only, mixed/interior, and invalid histograms.

This closes the *likelihood limit* question at the four corners, not the score-root census or all boundary strata. The new integrated design `C10S_F5_INTERIOR_MULTIPLICITY_AND_JOINT_CORNER_LIMITS_DESIGN_001.md` specifies the remaining exact resultant/subresultant route and validated interval-deflation obligations for singular interior roots. The suite now has 50 deterministic test methods, still unexecuted under governed CPython 3.12. F5 remains OPEN; no MLE certificate or method selection is claimed.

### Exact axis-aligned common-component detection added (2026-11-20)

`compactified_axis_common_components(P,Q)` now computes coefficient contents over `Q` for each compactification axis and takes their exact gcd. It detects common factors in `mu` alone (vertical components) and `t` alone (horizontal components), then square-free factorizes the shared content. Zero-polynomial cases abstain explicitly; malformed sparse terms are rejected. The helper explicitly states that general mixed bivariate factors are NOT CHECKED. Five deterministic tests were added, bringing the source-level test count to 55. They remain unexecuted under governed CPython 3.12. This is only axis-aligned component detection: it is not a general bivariate gcd, resultant, interior root census, or global MLE certificate.

### Exact mu-projection resultant implemented (2026-11-20)

`compactified_projection_resultant_mu(P,Q)` now forms the exact Sylvester matrix in `t` over `Q[mu]`, strips coefficient contents, computes the determinant using fraction-free Bareiss elimination with exact polynomial division, and restores the full resultant using the content powers. It returns exact rational coefficients and explicit zero-resultant, zero-polynomial and matrix-resource statuses. Five adversarial fixtures cover a linear resultant, a shared mixed factor, content restoration, degree-drop projection root and fail-closed limits. The suite now has 60 source-level test methods, still unexecuted under governed CPython 3.12. Projection-root isolation/lifting, exact back-substitution, local multiplicity and complete interior census remain OPEN; this is not a global MLE certificate.

### Projection-root square-free decomposition and Sturm isolation added (2026-11-20)

`compactified_projection_root_isolation_mu()` now square-free factorizes the exact `mu`-resultant and isolates real projection roots on `[0,1]` with rational Sturm sequences. Exact rational roots (including endpoints), irrational isolating intervals with root count one, projection multiplicity, and unresolved depth/resource remainders are retained. Three deterministic tests cover repeated rational roots, an irrational root and partial/non-resultant abstention. The source-level suite now has 63 test methods, not executed under governed CPython 3.12. This still produces projection coordinates only; subresultant lifting to `t`, exact verification in both original equations, local multiplicity and exhaustive interior census remain OPEN.

### Projection alignment correction (2026-11-20)

The primary resultant in §5 is `Res_mu(P,Q)` and therefore yields concentration candidates. With `t=kappa/(1+kappa)`, the harness now computes this as `compactified_concentration_resultant_t(P,Q)` and isolates its real roots using `compactified_concentration_root_isolation_t()`. The previously implemented `compactified_projection_resultant_mu()` computes the complementary `Res_t(P,Q)` projection onto `mu`; it remains a valid diagnostic but is not the primary route. Because the conditional likelihood is strictly concave in `mu` at fixed finite concentration, the next lift should first exploit the strictly decreasing conditional mean score with certified interval endpoint signs. General subresultant lifting is a fallback only if this simpler route cannot certify the relevant roots. Three tests were added; suite count is 66 source-level test methods, unexecuted under governed CPython 3.12.


## 21. Conditional-mean tube pruning for concentration intervals (2026-11-20)

A reduced interval operation, `conditional_mean_tube_and_concentration_exclusion()`, has been added. For a rational concentration interval in compactified (t), it evaluates the mean-score numerator on a dyadic grid of rational (mu) values and applies exact univariate Bernstein sign certification over the entire (t)-interval. Strictly positive and negative grid locations bracket the unique conditional mean-score root for every (t) in that interval, using strict conditional concavity of the original log-likelihood in (mu). The resulting rational ((mu,t)) tube is then tested against the concentration-score numerator with tensor-product Bernstein coefficients.

If the concentration score excludes zero throughout the tube, the whole concentration interval is certified to contain no common stationary point. Otherwise it is retained as an unresolved candidate interval. Failure to certify both signs returns an explicit unresolved status. The operation is interval pruning only: it does not prove existence of a stationary point, isolate a concentration root, certify multiplicity, or establish a global census. The dyadic mean grid is bounded by an explicit depth ceiling. Five deterministic tests cover successful pruning, candidate retention, endpoint-sign abstention, invalid budgets/domains and explicit rejection of compactification endpoints. They are committed but not executed under governed CPython 3.12.

This is the preferred next step in the reduced route because it exploits conditional mean uniqueness without requiring immediate algebraic lifting of each resultant root. Subresultant lifting remains a fallback for candidate intervals that cannot be resolved by interval pruning or require exact algebraic root recovery. No F5 closure, calibration, benchmark or scientific execution is claimed.


## 22. Adaptive conditional-mean concentration census (2026-11-20)

The reduced interval route now has an integrated deterministic controller, `conditional_mean_adaptive_concentration_census()`. Its input is a strictly interior rational compactified-concentration interval ([t_-,t_+]subset(0,1)), together with the paired exact compactified beta-binomial score numerators from one nondegenerate histogram.

For each FIFO-processed concentration interval, the controller:

1. certifies signs of the mean-score numerator at rational dyadic μ grid points over the entire t interval using exact univariate Bernstein coefficients;
2. uses strict conditional concavity of the underlying beta-binomial log-likelihood to obtain a tube containing the unique conditional mean root for every t in that interval;
3. excludes the interval if the concentration-score numerator has a strict Bernstein sign throughout the tube;
4. otherwise attempts the existing exact-rational Krawczyk certificate on the complete tube; strict inclusion plus the contraction bound certifies exactly one simple common stationary point in that tube;
5. bisects t deterministically when neither exclusion nor inclusion succeeds, retaining multiple/singular roots, split-boundary roots, and all depth/resource remainders as unresolved.

The controller returns `COMPLETE_CENSUS_ON_SUPPLIED_T_INTERVAL` only when every interval in the supplied closed finite-t range is either excluded or certified to contain exactly one simple root. It returns explicit incomplete statuses otherwise. This is a local-domain census, not a certificate over all (0<t<1): the t=0 and t=1 boundary strata are excluded and remain subject to the separately specified exact boundary/corner likelihood adjudication. The caller must cover the full finite domain with an independently justified endpoint treatment before claiming global exhaustiveness.

Five deterministic controller tests cover root-free exclusion, a simple affine root, retention of a multiple root, resource remainder and invalid domains/budgets. The source-level test module now contains 76 methods. These tests are committed but have not been executed in governed CPython 3.12. The simple affine fixtures test the numerical-certification kernel contract; production use remains restricted to paired score numerators generated from the same nondegenerate beta-binomial histogram. No calibration, bank, replay or scientific execution is claimed or authorized.

This controller is the current preferred reduced route for the interior concentration search. Algebraic resultant/Sturm isolation remains a complementary cross-check and fallback for unresolved concentration intervals; it is not invoked indiscriminately. Multiple-root deflation and endpoint-complete domain coverage remain open proof obligations. D1/F5 remain OPEN.


## 23. Consolidated end-to-end closure contract (2026-11-20)

The definitive F5 closure gates G1–G7, the reconstructed implementation inventory, current blocker classification, method-selection rule, and required final evidence record are consolidated in `C10S_F5_END_TO_END_CLOSURE_DOSSIER_DRAFT_001.md`. This is a research-branch coordination/design artifact only. It does not upgrade implementation or execution status. In particular, full open-domain interior census, multiple-root lifting/classification, rigorous global likelihood ordering, governed CPython 3.12 validation, and authorized prospective TierA calibration remain open. F5 remains OPEN.


## 11. Evidence reconciliation — 2026-11-20

The source and governed workflow evidence supersede the stale implementation-status statements above where they conflict:
- Workflow `.github/workflows/c10s-f5-exact-certification-tests.yml`, run [44767224308](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44767224308), source commit `a9a56d7c142b441b0893858c75e13a38ae38a9a2`: 135 deterministic tests PASS on CPython 3.12.10.
- The integrated bounded M30/R20 test requires a completed full-domain simple-root census, exact rational likelihood interval ordering and a globality basis including all one-edge profiles and joint-corner limits. It passes for that fixed histogram and declared resource budget.
- The implementation deliberately does not certify arbitrary interior multiple/singular roots. Such boxes remain unresolved and prevent a global certificate. The axis-component helper only detects axis-aligned factors; general mixed bivariate factors are not directly classified by that helper. The interval-first census must therefore retain unresolved boxes rather than promote them.
- Boundary coverage includes exact one-edge likelihood profiles and a uniform Markov-bound proof for all four joint corners. This supports path-independent corner likelihood limits for finite independent-world histograms; it does not prove every conceivable boundary statement outside this beta-binomial model.
- The exact score-numerator implementation has independent direct-rational score identity tests on small and M30/R20 fixtures. This is deterministic algebraic consistency evidence, not an independent external mathematical audit.

**Current gate interpretation:** the global-MLE wrapper is implemented and tested on bounded fixtures. G1's independent derivation/provenance review, G2's supported-regime completeness plus explicit singular abstention, G3's cross-stratum adversarial audit, G5's unified resource contract, and G6's evidence packaging remain in the F5 closure work order. Execution authorization in this design remains `NONE` for prospective scientific calibration; deterministic software verification is a separate engineering activity.

### 12.1 Historical probe disposition — superseded for the bounded F5 implementation (2026-11-20)

Section 12 records the preimplementation symbolic-sizing probe and the then-proposed need to select a general exact elimination backend. That recommendation is historical, not a current blocker for the bounded F5 path: the implemented interval-first conditional-mean/Bernstein/Krawczyk route now certifies the named M10/R5 and M30/R20 fixtures without constructing the large M30/R20 resultant. Exact resultant/Sturm remains available as a fallback/cross-check when the interval-first census is incomplete. No general modular resultant engine or universal singular-root solver is claimed or required by the current bounded fixture evidence. Any such escalation must be justified by an actual supported TierA fit that the bounded method cannot certify and must not become a parallel general-purpose project.
