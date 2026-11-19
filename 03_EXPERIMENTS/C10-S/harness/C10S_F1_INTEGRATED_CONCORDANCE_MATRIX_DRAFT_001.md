# C10-S — F1 Integrated Concordance Matrix (Draft 001)

**Status:** DESIGN / STATIC SOURCE REVIEW — NOT EXECUTED  
**Branch:** `research/c10s-nested-mr-calibration-design-20261119`  
**Scope:** F1 coefficient construction, floating-point reconstruction, exact-rational Sturm isolation, root adjudication, and F1/F5 inference gate.  
**Boundary:** This draft does not authorize tests, numerical validation, Monte Carlo calibration, or scientific execution.

## 1. Historical baseline reviewed

The current research branch contains:
- `c10s_f1_between_profile_likelihood.py` — F1 profile and score-polynomial construction.
- `c10s_f1_independent_root_isolator.py` — exact-rational Sturm reference, degree at most three.
- `c10s_f1_root_adjudication.py` — comparison of F1 positive roots with Sturm intervals.
- `c10s_nested_mr_comparative_inference_engine.py` — F1 diagnostic propagation into the comparative engine.
- Unit tests for the F1 solver, Sturm isolator, and adjudicator.

The rational coefficient builder computes exact rational expressions from the exact binary values of the inputs, then rounds each coefficient to binary64. Sturm therefore certifies the polynomial defined by those rounded coefficient values, not the pre-rounded rational coefficient vector and not an uncertainty set for the statistical inputs.

## 2. Static-review findings that block integrated validation

### F1-AUD-01 — Zero is included by the reference but excluded by the F1 positive-root list

The adapter calls `isolate_real_roots(..., lower=0)`. The isolator explicitly treats the finite domain as closed and extracts exact endpoint roots, including zero. The F1 diagnostic exposes `positive_roots`, which is a strictly-positive domain.

At `between_variance = 0`, the score-polynomial constant coefficient is zero by construction (`c0 = W tau^2`), so zero may be an exact root (often with multiplicity). The integrated comparator evaluates the diagnostic at `tau = max(0, between_estimate_raw)`; boundary cases can therefore compare different domains and report a false root-count discrepancy or abstention.

**Required resolution:** define and freeze the domain contract explicitly. For the positive-root comparison use an open lower boundary (e.g. isolate roots on `(0,+infinity)` by exact extraction-and-exclusion of zero), while retaining a separate boundary-root diagnostic. Do not silently discard zero without recording it.

### F1-AUD-02 — Rational isolators are converted to binary64 in the adjudication record

The adapter converts each rational endpoint with `float(root.lower)` and `float(root.upper)` before returning diagnostics. An exact rational endpoint outside binary64 range can become infinity; a nonzero endpoint below the subnormal range can become zero. That conversion can destroy the interval's ordering/width information in the diagnostic record even though the internal Sturm result was exact.

**Required resolution:** preserve numerator/denominator (or canonical rational strings) as the authoritative interval representation. Any float projection must be explicitly optional and fail closed when non-finite or non-injective.

### F1-AUD-03 — Matching tolerance is absolute and scale-dependent

The adapter uses one absolute `match_tolerance` for all root magnitudes. The current close-root guard prevents some ambiguous pairings, but it does not establish a scale-invariant error contract for very small or very large roots.

**Required resolution:** define matching against exact rational interval bounds plus a declared mixed absolute/relative error policy, or compare F1 roots using certified enclosures. Keep ambiguous matches as `ROOTS_UNRESOLVED`.

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
| M07 | Root exactly at zero, including `tau=0` boundary polynomial | Strictly-positive list excludes zero | Current closed `[0,+∞)` isolator includes zero | Current adapter can falsely disagree; resolve F1-AUD-01 first | Abstain |
| M08 | Negative roots only | No positive candidates | No roots in positive domain | AGREEMENT only after domain equivalence | Eligible for next diagnostic only |
| M09 | Positive and negative roots | Positive subset only | Positive-domain subset only | Compare same domain; negative roots recorded separately if all-real audit requested | Eligible for next diagnostic only |
| M10 | Constant nonzero polynomial | No positive roots | NO_ROOTS_CONSTANT_POLYNOMIAL | AGREEMENT under explicit constant-polynomial rule | Eligible for next diagnostic only |
| M11 | Identically zero polynomial | No finite root list | IDENTICALLY_ZERO_POLYNOMIAL_UNRESOLVED | UNRESOLVED | Abstain |
| M12 | Effective degree reduction | Degree reduced before solving | Same reduced degree | AGREEMENT if coefficient vectors and domain match | Eligible for next diagnostic only |
| M13 | Coefficient overflow/underflow during exact-to-float conversion | F1 construction rejects | Reference not invoked on invalid coefficient vector | UNRESOLVED / construction failure | Abstain |
| M14 | Extreme root endpoint not representable as binary64 | F1 candidate may fail or be absent | Exact rational isolator may still succeed | Current diagnostic projection unsafe; resolve F1-AUD-02 | Abstain |
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
- exact rational isolators and multiplicities;
- F1 candidate roots and their numerical representation;
- root-count, location, and multiplicity comparison;
- isolation depth/width outcome;
- coefficient-uncertainty status (separate from central-polynomial Sturm result);
- optimizer stability status;
- F1/F5 comparative status;
- explicit abstention reason.

Adjudication states remain:
- `AGREEMENT` — bounded agreement under the same declared domain and representation contract;
- `DISCREPANCY` — a demonstrated mismatch;
- `UNRESOLVED` — insufficient numerical resolution, representation, multiplicity, or uncertainty handling.

## 5. Gate decision

**Current decision: BLOCKED FOR INTEGRATED VALIDATION.**

The static review found at least one domain mismatch that can affect the `tau=0` boundary and a lossy rational-to-float diagnostic projection. These must be resolved before running the integrated validation battery. The absolute matching-tolerance policy also requires a declared scale-aware contract.

No tests or experiments were executed in preparing this draft. No calibration was performed. No scientific claim, C10 status, RMA, Evidence→Claim Matrix, or TGCV Core state is changed.
