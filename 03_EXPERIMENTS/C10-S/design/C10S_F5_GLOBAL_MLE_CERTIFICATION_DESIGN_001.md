# C10-S — F5 global beta-binomial MLE certification design 001

**Record:** C10S-F5-GLOBAL-MLE-CERTIFICATION-001  
**Status:** ANALYTICAL DESIGN — NOT IMPLEMENTED / NOT TESTED / NOT EXECUTED  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** F5 beta-binomial count likelihood, M10/R5 and M30/R20  
**Execution authorization:** NONE

---

## 1. Purpose

Resolve the D1 blocker concerning global maximum adjudication, multiple stationary roots, nearly degenerate stationary roots, and theoretical concentration boundaries.

The proposed solution is not another multistart heuristic and does not introduce an empirical likelihood-difference threshold. It exploits the finite-product form of the beta-binomial likelihood and uses exact algebraic elimination/root isolation as the global candidate-enumeration layer. Floating-point optimizers remain useful for candidate discovery and numerical cross-checks, but they do not certify globality.

This is a design proposal. No executable implementation, numerical root isolation, benchmark, simulation or scientific run is claimed.

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

## 5. Exhaustive stationary-point enumeration

Proposed certificate procedure:

1. Construct P and Q exactly from the observed count histogram.
2. Compute their polynomial gcd and the resultant R(kappa)=Res_mu(P,Q), with exact arithmetic.
3. If a nonconstant common factor intersects the positive open domain, record a non-isolated stationary component. Unless its likelihood supremum can itself be certified by a separate exact argument, return `NONISOLATED_STATIONARY_SET` and abstain. Do not perturb the data or regularize the likelihood to remove it.
4. If the resultant is identically zero, or elimination degree/coefficient growth exceeds the declared deterministic resource ceiling, return `ALGEBRAIC_CERTIFICATE_UNAVAILABLE`; no numerical multistart fallback may be promoted to a global certificate.
5. Factor/square-free decompose the nonzero resultant while retaining multiplicity metadata. Use an exact Sturm/subresultant real-root isolation procedure to isolate every distinct positive real kappa root in disjoint rational intervals. Repeated roots are retained as one distinct candidate with algebraic multiplicity recorded, not discarded.
6. For each isolated kappa interval, recover the corresponding mu root(s) using subresultant representation and rational interval refinement. Intersect with 0<mu<1 and verify the original two score equations with interval enclosures. Because of the strict conditional concavity theorem, at most one valid mu root exists for a given positive kappa.
7. Refine each candidate enclosure until it is disjoint from all other candidates and the score-system inclusion/uniqueness test succeeds. A candidate that cannot be certified because it is too close to another root, has singular unresolved multiplicity, or exceeds the arithmetic/resource ceiling is typed unresolved; it is not merged with a neighbor.
8. Evaluate the original log-likelihood over certified candidate enclosures using outward-rounded interval arithmetic. Compare candidate likelihood enclosures with each other and with all theoretical boundary likelihoods. If the intervals do not establish a unique ordering or a set of co-maximizers, increase precision/refine. If still unresolved at the resource ceiling, abstain.

The resultant may contain extraneous kappa roots caused by leading-coefficient degeneration or roots for which the corresponding mu is not in (0,1). These are rejected only after exact/subresultant recovery and domain verification; they are never counted as likelihood stationary points.

### Why this handles multiple and near-degenerate roots

- Sturm isolation counts all distinct real roots, including roots with even multiplicity that a sign-change scan would miss.
- Square-free factorization preserves multiplicity metadata.
- Distinct roots receive disjoint rational isolating intervals, even when very close.
- A root that cannot be separated within the resource ceiling remains unresolved; no distance threshold is invented.
- The original likelihood and score equations, not optimizer termination flags, determine candidate stationarity.

This is a mathematical certification route, not yet a claim that its computational cost is acceptable. Exact resultant degrees and coefficient growth for M10/R5 and M30/R20 must be measured on deterministic fixtures before D2 can be frozen.

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

## 11. D1 disposition

This design resolves the *mathematical route* to global adjudication. It does not yet resolve the *implementation feasibility* gate.

D1 may close only after:
- exact polynomial construction and resultant/root-isolation prototypes pass deterministic adversarial fixtures;
- coefficient growth and runtime are measured for representative M10/R5 and M30/R20 count histograms;
- interval evaluation of likelihood ordering and boundary limits is independently checked;
- constrained W/B profile root isolation is specified consistently;
- failure/abstention semantics and resource ceilings are frozen.

Until those conditions pass, the global MLE certificate remains `DESIGNED_NOT_IMPLEMENTED`, M1/M2 remain unvalidated candidates, and no new bank or scientific execution is authorized.


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
