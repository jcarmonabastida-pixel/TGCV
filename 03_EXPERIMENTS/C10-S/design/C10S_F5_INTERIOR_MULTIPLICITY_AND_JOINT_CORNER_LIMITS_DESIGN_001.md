# C10-S F5 — Interior multiplicity and joint compactification-corner limits

**Status:** RESEARCH DESIGN / IMPLEMENTATION PARTIAL — NOT VALIDATED  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** F5 global stationary-candidate and likelihood-boundary certification only.

## 1. Purpose and historical reuse

This design consolidates the next unresolved layer without recreating existing primitives. The research harness already contains exact integer score numerators, concentration compactification, tensor-product Bernstein conversion and exclusion, rational de Casteljau subdivision, adaptive Bernstein exclusion, rational Krawczyk inclusion for simple roots, an adaptive Bernstein–Krawczyk controller, one-edge likelihood limits, exact edge gcd/square-free decomposition, Sturm edge-root isolation, and canonical corner ownership.

The current deterministic suite has 50 test methods after the joint-corner additions in this change. None is represented as governed CPython 3.12 PASS by this design. No scientific bank, replay, calibration or empirical execution is authorized.

The new work closes one analytically tractable part of the boundary problem and specifies, without pretending to implement it, the missing multiplicity-aware interior census.

## 2. Joint likelihood limits at the four compactification corners

The compactification is \(t=\kappa/(1+\kappa)\), so \(t=0\) denotes \(\kappa\to0\) and \(t=1\) denotes \(\kappa\to\infty\). The four corners combine either \(\mu\to0\) or \(\mu\to1\) with either concentration limit.

For a beta-binomial count \(X\in\{0,\ldots,r\}\), the mean is \(E[X]=r\mu\). Therefore, for every \(\kappa>0\), irrespective of its magnitude or its rate of approach to zero/infinity,

\[
P(X>0)\le E[X]=r\mu.
\]

Likewise,

\[
P(X<r)\le E[r-X]=r(1-\mu).
\]

Consequently, as \(\mu\to0\), the full count distribution converges uniformly over \(\kappa>0\) to the point mass at zero. As \(\mu\to1\), it converges uniformly over \(\kappa>0\) to the point mass at \(r\). These bounds establish path independence when \(\mu\) and \(t\) approach a corner jointly; no assumption about the relative rates is required.

For a finite histogram of independent worlds, the joint corner likelihood limit is exactly:
- one at either \(\mu=0\) corner iff every positive-multiplicity observed count is zero; otherwise zero;
- one at either \(\mu=1\) corner iff every positive-multiplicity observed count is \(r\); otherwise zero.

This is stronger than extrapolating the one-edge profiles: it supplies a uniform probability bound that covers arbitrary joint paths. It is not a statement about the score equations or about the likelihood along non-corner boundary strata.

### Implemented primitive

`beta_binomial_joint_corner_likelihood_limits(r, count_histogram)` returns all four exact corner distributions and likelihoods, the uniform bounds, and an explicit path-independent status. It reuses the existing histogram validation contract and uses only rational values for the returned point masses and likelihoods.

Four deterministic tests cover all-zero observations, all-(r) observations, mixed/interior observations, and invalid histograms. These tests are committed but not executed.

## 3. Interior roots: separate simple and singular cases

Let \(P(\mu,t)=Q(\mu,t)=0\) be the compactified exact score-numerator system. For an isolated candidate \(z=(\mu,t)\), define

\[
J(z)=\begin{pmatrix}P_\mu&P_t\\Q_\mu&Q_t\end{pmatrix}.
\]

The existing Krawczyk certificate is restricted to simple roots: strict inclusion and a strict contraction bound certify one root in a box. A box whose Jacobian is singular or whose Krawczyk hypotheses cannot be proved must remain unresolved. In particular:
- a vanishing determinant at a candidate is a singularity flag, not by itself a multiplicity value;
- sign changes are not a valid existence test for even- or higher-multiplicity roots;
- a subdivision budget or depth limit cannot be converted into an exhaustive census.

## 4. Algebraic enumeration candidate — resultant and subresultant route

The following is the exact algebraic candidate route; it is a design contract, not an implemented claim.

1. Validate integer sparse input and remove zero terms.
2. Treat \(P,Q\) as polynomials in \(t\) with coefficients in \(\mathbb Z[\mu]\). Extract and compare their coefficient contents in \(\mathbb Z[\mu]\); a nonconstant common content factor identifies a vertical common component candidate and must be isolated/classified separately. Form primitive parts and compute their gcd over \(\mathbb Q(\mu)[t]\). A nonconstant gcd identifies a nonvertical common component; do not treat an identically zero resultant as a finite root list.
3. Compute the exact projection resultant of the primitive parts, \(R_\mu(\mu)=\operatorname{Res}_t(P_{\mathrm{prim}},Q_{\mathrm{prim}})\). A symmetric \(R_t(t)\), with the analogous content extraction, is an independent projection check.
4. If the resultant is nonzero, compute its square-free decomposition and isolate all real projection roots in the compactified unit interval with exact Sturm counts.
5. For each isolated algebraic projection root, use a subresultant chain / specialized polynomial gcd to recover the common roots in the eliminated coordinate. Verify every recovered pair in the original two equations using exact algebraic-number arithmetic.
6. Distinguish isolated affine roots, degree-drop/projection artifacts, roots on already-owned boundary strata, and unresolved algebraic components. Resultant multiplicity is not to be equated automatically with local intersection multiplicity.
7. Compute local multiplicity only through a justified local-algebra, subresultant, or dual-basis procedure; otherwise return `MULTIPLICITY_UNRESOLVED`.

A resultant that is identically zero, an unverified coefficient reconstruction, a degree drop not accounted for, or a failed back-substitution must fail closed. Modular resultants with CRT reconstruction remain a parallel performance implementation; the reconstructed integer polynomial must be verified by exact substitution/divisibility identities before it can be used as evidence.

## 5. Interval route for singular roots

Bernstein exclusion remains the exhaustive box-pruning mechanism. Ordinary Krawczyk inclusion remains a simple-root method. Singular boxes require a separate validated layer, such as a mathematically specified deflation/regularization system with:
- a proved equivalence between roots of the original system and admissible roots of the deflated system in the box;
- explicit treatment of rank-deficient Jacobians and all required projective/normalization charts;
- exact or outward-rigorous interval arithmetic for every coefficient and derivative enclosure;
- a validated inclusion/uniqueness theorem for the augmented system;
- a map back to the original root and a local multiplicity certificate, or an explicit unresolved outcome.

No naive Jacobian perturbation, floating-point singular-value threshold, sign-change heuristic, or unverified symbolic deflation is admissible as a certificate. Until a complete theorem and adversarial fixtures exist, singular boxes remain unresolved and prevent a global census.

## 6. Unified output contract

The future global census must keep distinct records for:
- `INTERIOR_SIMPLE_ROOT_CERTIFIED`;
- `INTERIOR_SINGULAR_ROOT_CERTIFIED` (only with a validated multiplicity-aware proof);
- `BOUNDARY_EDGE_ROOT_CERTIFIED`;
- `BOUNDARY_CORNER_ROOT_OWNED`;
- `COMMON_COMPONENT_UNRESOLVED`;
- `PROJECTION_ARTIFACT_REJECTED`;
- `UNRESOLVED_AT_DEPTH_LIMIT`;
- `UNRESOLVED_AT_RESOURCE_LIMIT`;
- `MULTIPLICITY_UNRESOLVED`.

Each record must retain exact isolating bounds, proof method, polynomial identity, multiplicity status, canonical boundary ownership where relevant, and provenance. A global stationary-candidate census is complete only if the initial compactified domain is covered and every box/stratum is either rigorously excluded or assigned to exactly one certified candidate/component. Any unresolved item blocks the word `EXHAUSTIVE`.

The likelihood comparison gate is separate: a complete stationary-root census is not itself a global MLE certificate. Interior candidate likelihoods and all boundary-stratum/corner limits must be enclosed and compared rigorously. Ties/co-maxima and unattained boundary suprema must be reported explicitly.

## 7. Adversarial fixture matrix required before certification

| Fixture | Required outcome |
|---|---|
| Simple isolated interior root | Krawczyk simple-root certificate |
| Double and triple interior roots | Retained; multiplicity-aware certificate or typed abstention |
| Two close interior roots | Separate isolating regions or explicit unresolved status |
| Tangential intersection without sign change | Never excluded by sign-change logic |
| Common bivariate factor | Common-component unresolved/classified, never finite root list |
| Resultant degree drop | Exact artifact classification or abstention |
| Same projection coordinate, distinct second coordinates | Both recovered; no projection-based merge |
| Root on an internal subdivision boundary | No duplicate ownership; unresolved if uniqueness cannot be assigned |
| Each of four compactification corners | One canonical owner and path-independent likelihood limit |
| Resource/depth exhaustion | Full remainder retained; no exhaustive status |

## 8. Work order and authorization boundary

1. Preserve the new joint-corner theorem and exact helper.
2. Specify and implement exact bivariate common-factor detection and resultant/subresultant prototypes on bounded algebraic fixtures.
3. Add rational fixtures for double, triple, tangential, close, shared-component, and projection-collision cases.
4. Independently specify the validated interval-deflation theorem; do not claim the algebraic resultant route validates it.
5. Integrate both routes into a common typed census only after their proof obligations are explicit.
6. Compare runtime/cost only after deterministic correctness fixtures pass.
7. Continue to keep M10/R5 and M30/R20 scientific banks, replays and calibrations outside this design-only authorization.

**Current conclusion:** the four joint compactification-corner likelihood limits are analytically classified and a rational helper is implemented. Interior multiple-root certification, a complete interior census, cross-stratum likelihood ordering, and global MLE certification remain OPEN. No backend is selected.

## 9. Coordinator crosswalk

- Global MLE certification design: this document closes only the four joint corner likelihood limits; it does not close the score-root census or global likelihood comparison.
- Interval-method comparison specification: the interval backend remains simple-root Krawczyk plus Bernstein exclusion until a validated deflation theorem is implemented; the algebraic backend remains a parallel exact resultant/subresultant candidate.
- F1/F5 weak-identification audit: the corner result is a boundary-likelihood classification, not an identification or causal evidence upgrade. Weak-identification diagnostics and statistical execution gates remain unchanged.
- Test inventory: four new deterministic joint-corner tests bring the source-level test-method count to 50. Governed execution remains pending.

## 4A. Implemented first algebraic subroutine: axis-aligned common components

The harness now includes `compactified_axis_common_components(P,Q)`. For each axis it treats the bivariate polynomial as a univariate polynomial in that axis with coefficient polynomials in the other variable, computes the exact coefficient content over \\(\\mathbb Q\\), and takes the gcd of the two contents. It therefore detects:
- common factors depending on \\(\\mu\\) alone, which represent vertical components in the compactified square;
- common factors depending on \\(t\\) alone, which represent horizontal components.

The common content is square-free factorized in characteristic zero, preserving the minimum shared multiplicity encoded by the gcd. A zero input polynomial returns `ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED`; malformed sparse terms are rejected. The result explicitly reports `general_mixed_bivariate_factors = NOT_CHECKED`.

This is a useful first exact component of the algebraic route, but it is not a general bivariate gcd. It does not detect mixed factors such as \\(\\mu+t-1\\), does not compute a resultant, does not isolate the component's intersections with the domain, and does not prove that no other common component exists. A negative axis-aligned result must never be interpreted as absence of a general common component.

Five deterministic tests cover a vertical factor, a repeated horizontal factor, absence of axis-aligned factors without overclaiming, malformed inputs and zero-polynomial abstention. The source-level suite now contains 55 test methods. All remain unexecuted under governed CPython 3.12.

## 4B. Implemented exact projection resultant in the algebraic route

The harness now includes `compactified_projection_resultant_mu(P,Q)`, computing \(\operatorname{Res}_t(P,Q)\) as an exact rational-coefficient polynomial in \(\mu\). The implementation:
1. extracts the exact \(\mu\)-content of each polynomial;
2. divides coefficient polynomials by their content to obtain primitive polynomials in \(t\);
3. constructs the Sylvester matrix over \(\mathbb Q[\mu]\);
4. evaluates its determinant with fraction-free Bareiss elimination and exact polynomial division;
5. restores the full resultant by multiplying \(c_P(\mu)^{\deg_t Q}c_Q(\mu)^{\deg_t P}\);
6. returns exact rational coefficients, matrix dimension and explicit resource/degeneracy statuses.

A zero primitive resultant is reported as `ZERO_RESULTANT_COMMON_FACTOR_OR_DEGENERACY`, not as a finite root list. A matrix-dimension ceiling returns `RESULTANT_MATRIX_RESOURCE_LIMIT` with no fabricated polynomial. Constant-in-`t` cases retain their coefficient-content interpretation; the separate axis-component detector remains necessary when both equations are independent of \(t\).

Five deterministic fixtures have been added: a simple linear resultant, a shared mixed factor, restoration of common axis contents, a projection root associated with degree drop, and resource/invalid/zero-polynomial abstention. The source-level suite now contains 60 test methods. They are committed but have not been executed under governed CPython 3.12.

This is the first resultant implementation, not yet a complete algebraic root solver. The resultant's real roots still require square-free decomposition and exact Sturm isolation in \(\mu\); each projection root must then be lifted through subresultants or specialized gcds in \(t\), with exact back-substitution into both original equations. Projection multiplicity is not local intersection multiplicity. A zero resultant still requires common-component classification, including mixed bivariate factors. No exhaustive interior census or global MLE certificate follows yet.

## 4C. Implemented projection-root square-free and Sturm isolation

The algebraic path now includes `compactified_projection_root_isolation_mu(resultant_result, ...)`. It accepts only a nonzero exact resultant, performs characteristic-zero square-free decomposition, and isolates every real projection root in the compactified interval \(0\leq\mu\leq1\) using the existing exact rational Sturm sequence. Rational roots, including endpoints, are returned exactly; irrational roots are returned as rational intervals with Sturm count one. The projection multiplicity is retained as metadata.

The helper validates rational coefficients, positive isolation width, depth and interval budgets. Non-resultant/zero-resultant statuses are not passed to Sturm as if they were finite polynomials. Depth and resource exhaustion preserve unresolved intervals and produce a partial status.

Three deterministic tests cover a repeated rational projection root, an irrational projection root, and partial/non-resultant abstention with strict input validation. The source-level suite now contains 63 test methods, still unexecuted under governed CPython 3.12.

This completes only the projection-coordinate stage. It does not lift an algebraic \(\mu\)-root to one or more \(t\)-coordinates. The next algebraic operation must use subresultant sequences or specialized gcds over the isolated algebraic projection root, retain multiple distinct lifts sharing one projection, and verify both original equations. Projection multiplicity remains distinct from local intersection multiplicity.

## 4D. Primary projection aligned with the F5 conditional-mean theorem

The global design in `C10S_F5_GLOBAL_MLE_CERTIFICATION_DESIGN_001.md` specifies the primary elimination as \\(R(\\kappa)=\\operatorname{Res}_{\\mu}(P,Q)\\). After concentration compactification \\(t=\\kappa/(1+\\kappa)\\), the corresponding polynomial is \\(R(t)=\\operatorname{Res}_{\\mu}(P(\\mu,t),Q(\\mu,t))\\).

The earlier `compactified_projection_resultant_mu` computes the complementary projection \\(\\operatorname{Res}_{t}(P,Q)\\), retaining \\(\\mu\\). That operation is mathematically valid and remains available as a diagnostic, but it is not the primary projection for the F5 fit. The strict conditional concavity theorem gives at most one interior conditional-mean maximizer for each fixed finite concentration, so the primary route should enumerate concentration candidates and then recover the unique admissible mean.

The harness now includes:
- `compactified_concentration_resultant_t(P,Q)`: swaps the sparse exponent axes and uses exact Sylvester/Bareiss arithmetic to compute \\(\\operatorname{Res}_{\\mu}(P,Q)\\) as a rational polynomial in \\(t\\);
- `compactified_concentration_root_isolation_t(...)`: applies the existing square-free/Sturm isolation to the concentration projection on \\(0\\leq t\\leq1\\), retaining projection multiplicity and partial states.

Three deterministic tests cover the linear projection \\(2t-1\\), a repeated projection root \\( (2t-1)^2\\), and malformed sparse input. The source-level suite now contains 66 test methods; none has been executed under governed CPython 3.12.

This correction aligns the implementation with the stated mathematical reduction; it does not complete the fit certificate. For each isolated interior \\(t\\)-root, the next step is to recover \\(\\mu\\) using the strictly decreasing conditional score, with exact/rational interval enclosures over the isolating \\(t\\)-interval. A certified sign bracket plus strict monotonicity can establish existence and uniqueness without a general bivariate subresultant lift, provided the interval evaluation proves the endpoint signs uniformly over the full \\(t\\)-interval. If it cannot, refine the \\(t\\)-interval or abstain. The recovered pair must then be verified in both original score equations and compared against all explicit concentration/mean boundary likelihoods.

Accordingly, the next operation is **not** general subresultant back-substitution by default. First implement and test this lower-dimensional lift. Escalate to general algebraic-number/subresultant machinery only if the conditional-score interval method cannot certify a candidate that materially affects the two frozen F5 designs.
