# C10-S — F1 Integrated Concordance Matrix (Draft 002)

**Status:** DESIGN / STATIC SOURCE REVIEW — CORRECTIONS IMPLEMENTED; VALIDATION NOT EXECUTED  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** F1 coefficient construction, floating-point reconstruction, exact-rational Sturm isolation, root adjudication, and F1/F5 inference gate.  
**Boundary:** This draft does not authorize tests, numerical validation, Monte Carlo calibration, or scientific execution.

## 1. Historical baseline reviewed

The current research branch contains:
- `c10s_f1_between_profile_likelihood.py` — F1 profile and score-polynomial construction.
- `c10s_f1_independent_root_isolator.py` — exact-rational Sturm reference, degree at most three.
- `c10s_f1_root_adjudication.py` — comparison of F1 positive roots with Sturm intervals.
- `c10s_nested_mr_comparative_inference_engine.py` — F1 diagnostic propagation into the comparative engine, including adjudication domain, removed-zero-factor multiplicity, boundary roots and exact rational isolator intervals.
- Unit tests for the F1 solver, Sturm isolator, and adjudicator.

The rational coefficient builder computes exact rational expressions from the exact binary values of the inputs, then rounds each coefficient to binary64. Sturm therefore certifies the polynomial defined by those rounded coefficient values, not the pre-rounded rational coefficient vector and not an uncertainty set for the statistical inputs.

## 2. Static-review findings that block integrated validation

### F1-AUD-01 — Zero-factor semantics at tau=0 (reviewed; explicit diagnostic added)

The initial review identified a possible mismatch between Sturm's closed lower endpoint and F1's strictly-positive root list. Full-source inspection shows that F1 already removes leading zero coefficients before returning the score polynomial. At `tau=0`, these coefficients encode the extraneous `s^2` factor in the score numerator `P(s)=2s(tau+s/r)^2 score(s)`; they are not positive stationary roots of the score. The prior claim of a production root-count defect was therefore too strong.

**Correction:** F1 now records `removed_zero_factor_multiplicity` while removing those exact leading zero coefficients. The adjudicator declares the comparison domain as `(0,+infinity)`, preserves any exact zero Sturm endpoint roots separately, and reports the removed extraneous factor multiplicity independently. The Sturm reference continues to certify the reduced polynomial actually supplied to it.

### F1-AUD-02 — Rational interval representation (corrected in code; validation pending)

The adjudication record now stores each Sturm endpoint as an exact canonical rational string `numerator/denominator`. Matching is performed with `Fraction` arithmetic against the exact binary-rational value of each F1 float candidate. No conversion of Sturm endpoints to binary64 is performed.

### F1-AUD-03 — Scale-aware unique matching (corrected in code; validation pending)

The adapter now uses the exact-rational mixed tolerance `max(abs_tol, rel_tol * max(|candidate|, |interval endpoints|))`. It constructs the candidate-to-interval correspondence in both directions. Only a one-to-one singleton correspondence can agree; ambiguous or missing correspondence returns `ROOTS_UNRESOLVED`.

### F1-AUD-04 — The current agreement label is narrower than full numerical certification

`ROOTS_AGREE` means the F1 binary64 roots can be matched to simple roots of the exact rationalized binary64 coefficient polynomial under the current tolerance. It does not certify coefficient uncertainty, forward error from the statistical inputs, nor the score-to-likelihood stationary-point classification.

**Required resolution:** retain this bounded meaning in the output schema and never promote it to global optimization exhaustiveness or inferential validity by itself.

## 3. Integrated concordance matrix

| ID | Adversarial geometry / input | F1 expected | Sturm reference expected | Adjudication expected | Inference gate |
|---|---|---|---|---|---|
| M01 | Three distinct positive simple roots | Three positive candidates | Three disjoint isolators, multiplicity 1 | AGREEMENT only if every candidate is uniquely enclosed | Eligible for next diagnostic only |
| M02 | One positive double root plus one simple root | Legacy multiplicity not certified | Multiplicities 2 and 1 | UNRESOLVED pending F1 multiplicity contract | Abstain |
| M03 | Positive triple root | Legacy multiplicity not certified | One isolator, multiplicity 3 | UNRESOLVED | Abstain |
| M04 | Two close but distinct positive roots, resolvable | Two candidates | Two disjoint isolators | AGREEMENT only with unique certified matching | Eligible for next diagnostic only |
| M05 | Two close roots below requested isolation resolution | May return approximate candidates | ROOTS_UNRESOLVED at depth/width limit | UNRESOLVED | Abstain |
| M06 | Positive root exactly at requested upper endpoint | Endpoint candidate behavior must be specified | Singleton endpoint isolator | Compare only under identical closed/open domain contract | Abstain until domain contract fixed |
| M07 | Root exactly at zero, including `tau=0` boundary polynomial | F1 removes the extraneous zero factor and records its multiplicity | Sturm isolates the reduced polynomial; any exact zero root is retained separately | Compare strictly-positive roots only; report removed factor multiplicity separately | Continue only if reduced-polynomial contract holds |
| M08 | Negative roots only | No positive candidates | No roots in positive domain | AGREEMENT only after domain equivalence | Eligible for next diagnostic only |
| M09 | Positive and negative roots | Positive subset only | Positive-domain subset only | Compare same domain; negative roots recorded separately if all-real audit requested | Eligible for next diagnostic only |
| M10 | Constant nonzero polynomial | No positive roots | NO_ROOTS_CONSTANT_POLYNOMIAL | AGREEMENT under explicit constant-polynomial rule | Eligible for next diagnostic only |
| M11 | Identically zero polynomial | No finite root list | IDENTICALLY_ZERO_POLYNOMIAL_UNRESOLVED | UNRESOLVED | Abstain |
| M12 | Effective degree reduction | Degree reduced before solving | Same reduced degree | AGREEMENT if coefficient vectors and domain match | Eligible for next diagnostic only |
| M13 | Coefficient overflow/underflow during exact-to-float conversion | F1 construction rejects | Reference not invoked on invalid coefficient vector | UNRESOLVED / construction failure | Abstain |
| M14 | Extreme rational isolator endpoint not representable as binary64 | F1 candidate remains binary64 | Exact rational isolator retains arbitrary-precision rational endpoints | Canonical rational strings retained; matching remains exact-rational | Eligible subject to unique mixed-tolerance match |
| M15 | Same polynomial under extreme scale transformations | F1 roots should transform equivariantly within declared numerical bounds | Exact rational reference gives transformed polynomial's exact roots | Compare after explicit scale map; no silent tolerance reuse | Abstain on lost representation |
| M16 | Coefficient uncertainty interval crosses discriminant zero | Central F1 polynomial may have definite roots | Sturm certifies only central rationalized polynomial | UNRESOLVED for uncertainty-aware claim | Abstain |
| M17 | Nonfinite input coefficient / bound | Reject | Reject | UNRESOLVED / invalid input | Abstain |
| M18 | Isolation depth exhausted | May return candidate roots | ROOTS_UNRESOLVED with no partial certificate | UNRESOLVED | Abstain |
| M19 | F1/Sturm root count or location mismatch | Candidate set differs | Certified reference differs | DISCREPANT | Abstain |
| M20 | F1 optimizer scan and algebraic roots disagree | Internal diagnostics discordant | Sturm adjudication independently recorded | DISCREPANT or UNRESOLVED; never agreement by averaging | Abstain |
| M21 | Root agreement but optimizer stability is insufficient/boundary-sensitive | Root sets may agree | Root sets may agree | ROOTS_AGREE does not override optimizer status | Abstain |
| M22 | F1 root agreement but F5 comparison is discordant | F1 diagnostic bounded pass | Sturm bounded pass | Preserve separate F1 and F5 statuses | No comparative favorable adjudication |

## 4. Required output contract

The integrated record must preserve, at minimum:
- coefficient provenance and coefficient semantics;
- effective polynomial degree;
- requested root domain, including endpoint inclusion/exclusion;
- exact rational isolators and multiplicities (canonical numerator/denominator strings);\n- multiplicity of any extraneous zero factor removed before positive-root solving;
- F1 candidate roots and their numerical representation;
- root-count, location, and multiplicity comparison;
- isolation depth/width outcome;
- coefficient-uncertainty status (separate from central-polynomial Sturm result);
- optimizer stability status;
- F1/F5 comparative status;
- explicit abstention reason;\n- root-domain and exact interval provenance propagated into the comparative engine.

Adjudication states remain:
- `AGREEMENT` — bounded agreement under the same declared domain and representation contract;
- `DISCREPANCY` — a demonstrated mismatch;
- `UNRESOLVED` — insufficient numerical resolution, representation, multiplicity, or uncertainty handling.

## 5. Gate decision

**Current decision: DESIGN CORRECTIONS IMPLEMENTED; INTEGRATED VALIDATION NOT YET AUTHORIZED OR EXECUTED.**

The three identified items now have explicit code-level handling: the zero-factor multiplicity is recorded after F1's existing algebraic removal; Sturm intervals remain rational through adjudication and serialization; and matching uses a mixed absolute/relative tolerance with unique one-to-one correspondence. The updated adversarial tests are defined but have not been run. Static implementation is not yet validation evidence.

No tests or experiments were executed in preparing this draft. No calibration was performed. No scientific claim, C10 status, RMA, Evidence→Claim Matrix, or TGCV Core state is changed.

## 7. Integrated correction after validation attempt 002

### F1-AUD-05 — Scale-dependent endpoint root tolerance (corrected; validation pending)

Attempt 002 identified a reproducible equivariance discrepancy at the lower LR endpoint when observations were multiplied by (10^{-4}). The root solver used an absolute `xtol=1e-12) in the physical variance coordinate `tau`. Since the variance coordinate scales by (k^2), the numerical tolerance did not scale with the model. The lower endpoint was approximately (7.74875\times10^{-6}) away after transforming back to the baseline units, exceeding the previous assertion tolerance.

**Correction:** define a positive data-derived reference scale (s_{ref}=\max(MSW,S^2_{means})), and solve both LR endpoints in the dimensionless coordinate (x=\tau/s_{ref}). The bracket expansion and Brent tolerances now operate in (x), and the endpoints are transformed back only after solving. The fixed absolute variance floor (10^{-12}) was removed from the profile-likelihood reference scale; the profile optimizer uses the positive supplied reference scale directly. Conversion back to physical variance fails closed on overflow or positive underflow.

This targets the cause; it does not relax the numerical assertion.

### F1-AUD-06 — Root-restoration test namespace (corrected; validation pending)

The test module now explicitly imports `_restore_polynomial_scale`, which was missing from its import list. Both existing underflow and overflow tests now reach the intended helper instead of raising `NameError`.

### Regression contract

The observation-scale equivariance test retains the scale factors (10^{-4},10^{-2},10^2,10^4). It compares lower and upper endpoints in baseline variance units with absolute delta (10^{-8}), and the MLE with delta (10^{-10}). These are stricter than the prior `places=6` and `places=7` assertions. No tolerance was widened.

### Static review and evidence boundary

- The endpoint root equations, MLE, and likelihood-ratio cutoff are unchanged.
- Both endpoints use the same dimensionless coordinate and the same root tolerance.
- The reference scale is positive because the within-world sum of squares is required to be positive; the sufficient statistics are checked finite.
- The conversion back to the physical variance coordinate rejects overflow and positive underflow.
- The two restoration tests now resolve the helper symbol explicitly.
- The original frozen attempt 002 and its failed result remain immutable historical evidence.
- This correction has **not** been executed. No test, compile check, calibration, DGP, or scientific experiment has been run.
- The next execution requires a new frozen snapshot and a new one-shot authorization.

**Current disposition:** `CORRECTION IMPLEMENTED / STATIC REVIEW PENDING COMPLETION / VALIDATION PENDING`. No claim of numerical validation, exhaustive root certification, inferential validity, or C10 scientific closure is made.

### F1-AUD-07 — Residual absolute variance floors in related F1 diagnostics (corrected; validation pending)

A cross-call-site review found the same (10^{-12}) absolute variance floor in the polynomial-root normalization scale and in the nuisance optimizer's log-scale scan. These floors could break scale equivariance for sufficiently small, but still representable, variance inputs even after the LR endpoint correction.

**Integrated correction:** all reference-scale selections in the F1 profile-likelihood, polynomial-root, and nuisance-optimizer paths now use positive data-derived quantities (`within`, `s2_means`, `tau`, and positive critical-point magnitudes) without a fixed absolute variance floor. The within sum of squares is required to be strictly positive, so the scale remains positive. The log-scale optimizer and polynomial normalizer continue to fail closed on non-finite or unrepresentable values.

This extends the same scale convention across the F1 paths; it does not alter the likelihood, score polynomial, root domain, LR cutoff, or scientific estimand.
