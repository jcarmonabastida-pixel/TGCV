# C10-S — F1 Adversarial Numerical Stress Design (Draft 001)

**Status:** DESIGN ONLY — NOT EXECUTED — NEW AUTHORIZATION REQUIRED  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Validated software baseline:** `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b`  
**Integrated deterministic test result:** `C10S_F1_INTEGRATED_VALIDATION_RESULT_003.md` — 73/73 PASS  
**Predecessor design:** `C10S_F1_INTEGRATED_CONCORDANCE_MATRIX_DRAFT_002.md`  
**Scope:** deterministic adversarial numerical characterization of F1 polynomial construction, floating-point root reconstruction, exact-rational Sturm isolation, root adjudication, and the F1/F5 diagnostic boundary.  
**Exclusions:** no DGP experiment, no outer Monte Carlo calibration, no parameter tuning, no inferential coverage study, and no scientific C10 execution.

## 1. Purpose and evidence boundary

The integrated validation PASS establishes that four test modules pass on the frozen source and runtime. It does not establish numerical robustness outside their encoded fixtures, exhaustive root certification, or uncertainty-aware inference.

This protocol addresses the next narrower question:

> Across controlled perturbations of polynomial geometry, coefficient representation and numerical scale, does F1 either return a result concordant with the exact-rational reference for the actual binary64 coefficient vector, or abstain explicitly when the requested resolution is not supported?

The reference truth is always the exact rational polynomial represented by the binary64 coefficient values actually passed to Sturm. It is **not** the ideal pre-rounding polynomial and is not an uncertainty interval for the original statistical quantities. Both representations must be recorded where a fixture starts from ideal rational coefficients.

No execution is authorized by this document.

## 2. Historical coverage reconstruction

The existing 73-test PASS already covers the following baseline cases:

| Existing area | Existing coverage | Status after integrated run |
|---|---|---|
| F1 profile likelihood | Finite physical parameter space, LR endpoint equation, boundary inclusion, scale factors (10^{-4},10^{-2},10^2,10^4) | TESTED |
| Exact coefficient construction | Binary-rational construction, conversion overflow/underflow and non-finite inputs | TESTED |
| Polynomial scale helpers | Scale-power overflow/underflow, erased coefficient, root restoration overflow/underflow | TESTED |
| Critical-point solver | Two distinct positive roots, exact double root, near-zero discriminant abstention, invalid/non-finite cases | TESTED |
| Sturm isolator | Three simple real roots, double + simple, triple, close rational roots, domain endpoints, degree reduction, negative roots, constant and zero polynomials, degree and finite-input guards | TESTED |
| Root adjudication | Agreement, root-count discrepancy, overlapping tolerance abstention, zero-factor bookkeeping, rational interval serialization, relative tolerance, multiplicity abstention | TESTED |
| F1/F5 comparative engine | Diagnostic rosters, denominator and provenance checks, family/design separation, bounded F1/F5 propagation | TESTED |

The existing suite does **not** establish the following broader properties:

1. a systematic transition curve from resolved to unresolved as root separation approaches binary64 representation limits;
2. stability under one-ULP coefficient perturbations around repeated-root/discriminant boundaries;
3. scale equivariance of the independent Sturm isolator and the full F1 → Sturm → adjudicator chain over a broad binary-exponent range;
4. measured false-agreement and false-discrepancy rates over a predeclared adversarial fixture grid;
5. a quantified distinction between ideal-rational construction error and the exact binary64 polynomial that Sturm actually certifies;
6. behavior under deliberate isolation-depth and width exhaustion across root magnitudes.

These are new characterization objectives, not claims that the existing code is defective.

## 3. Experimental units and reference construction

The unit of analysis is one deterministic polynomial fixture plus its declared transformations/perturbations. Each fixture record must preserve:

- fixture ID and generator version;
- ideal rational coefficient vector, if applicable;
- exact binary64 coefficient vector passed to F1/Sturm (hexadecimal float representation);
- exact rationalization of each binary64 coefficient;
- effective degree after exact leading-zero trimming;
- known root geometry for the ideal polynomial, kept distinct from Sturm's certified roots of the binary64 polynomial;
- coefficient perturbation and scale transformation applied;
- F1 output, Sturm output, adjudication output, elapsed time and abstention reason;
- runtime, Python/SciPy/NumPy versions and source commit.

Do not generate a random fixture without recording its seed and complete realized coefficients. Prefer exact rational fixture construction and deterministic ULP stepping. If a pseudo-random supplement is later justified, its seed and generator algorithm must be frozen before execution.

## 4. Adversarial blocks

### N1 — Root-separation ladder

Construct degree-2 and degree-3 exact-rational polynomials with:
- two distinct positive simple roots separated by (delta);
- one positive double root plus a distinct simple root;
- a positive triple root;
- one positive close pair plus one negative root.

Use a predeclared logarithmic separation ladder spanning comfortably resolved cases through cases where the roots round to indistinguishable binary64 values. For each (delta), retain both the ideal rational polynomial and the exact rationalization of the rounded binary64 coefficients.

Expected disposition:
- **AGREEMENT:** all relevant simple roots have a unique one-to-one F1/Sturm match under the frozen tolerance contract;
- **DISCREPANCY:** a demonstrable count/location mismatch when the reference roots are isolated and the F1 solver claims a resolved result;
- **UNRESOLVED:** multiplicity is not certified by F1, isolation width/depth is insufficient, matching is ambiguous, or the rounded representation no longer preserves the intended root geometry.

The transition threshold is an empirical characterization result; do not choose it after seeing outcomes.

### N2 — One-ULP coefficient perturbations

For selected simple, double and near-double fixtures, perturb each nonzero binary64 coefficient by (-1), (+1), and (where finite) (pm 2) adjacent representable values using deterministic next-representable-float steps.

Record the exact rational polynomial after each perturbation. A perturbation can change the root count or multiplicity; that is not automatically a defect. The adjudication must track the polynomial actually supplied.

Expected disposition:
- correct agreement for the perturbed polynomial when the root geometry remains resolvable;
- explicit discrepancy only when F1 claims a resolved root set that conflicts with the exact-rational reference;
- abstention when the numerical contract cannot distinguish the cases.

### N3 — Polynomial amplitude and variable-scale transformations

Use exact rational transformations before binary64 conversion.

For amplitude scaling, (q(x)=alpha p(x)), (alpha=2^k): roots must be invariant whenever the transformed coefficient vector remains representable and the solver's normalization contract supports it.

For variable scaling, (q(y)=p(y/2^k)): roots transform as (y=2^k x). Compare intervals after applying the inverse scale map, preserving exact rational endpoints.

Use a predeclared exponent ladder that includes ordinary, very small and very large but representable coefficient vectors. Cases in which any nonzero coefficient becomes zero or non-finite during binary64 conversion must be classified as representation failure/UNRESOLVED, not silently treated as the same polynomial.

This block tests the polynomial isolator/adjudicator separately from the statistical observation-scale equivariance test already present in F1 profile likelihood.

### N4 — Full F1 observation-scale stress

Extend the existing observation-scale fixture beyond (10^{-4},10^{-2},10^2,10^4) using powers of two over a predeclared exponent ladder. For each scale (k), transform observations by (2^k), and variance quantities by (2^{2k}).

Record separately:
- profile log-likelihood equivariance after subtracting the analytically expected scale-dependent constant, where applicable;
- MLE and LR endpoint equivariance after mapping variances back by (2^{-2k});
- score coefficient construction status;
- polynomial normalization and root restoration status;
- F1/Sturm adjudication status.

Do not require every layer to return roots at every extreme. If exact coefficient construction correctly abstains because the final binary64 coefficient vector is not representable, count this as a bounded fail-closed outcome, not a numerical PASS for root recovery.

### N5 — Isolation-resolution and root-magnitude ladder

Vary `max_width` and `max_depth` on fixed exact-rational fixtures, including roots near zero, roots near finite domain endpoints and roots with large magnitude.

Check:
- every returned interval is rational, ordered, within the requested domain and disjoint;
- each interval has the declared root count and multiplicity;
- exact endpoint roots are singleton intervals;
- exhausting depth/width returns `ROOTS_UNRESOLVED` with no partial certificate;
- increasing the allowed depth or width resolution does not silently alter the polynomial or domain.

The current adjudicator invokes Sturm with lower bound zero and a fixed absolute isolation width. This block characterizes its supported domain; it does not silently replace that contract with a relative-width contract.

### N6 — Boundary, degree and fail-closed regression

Re-run as part of the stress harness, with expanded parameterization:
- (	au=0) and removed extraneous zero-factor multiplicity;
- positive roots arbitrarily near zero;
- exact zero and finite upper-bound roots in the isolator;
- degree reduction to 2, 1 and 0;
- nonzero constant and identically-zero polynomials;
- non-finite inputs and invalid bounds;
- overflow/underflow at coefficient conversion and root restoration.

This is regression protection for the existing contracts, not a reason to reinterpret their expected outcomes.

## 5. Frozen adjudication and metrics

Use the existing three-way adjudication semantics without introducing a fourth success state:

- `AGREEMENT`: unique, one-to-one, domain-consistent match of F1 simple roots to exact-rational Sturm isolators for the actual binary64 coefficient vector.
- `DISCREPANCY`: a demonstrated disagreement where both sides claim resolved results under the same polynomial and domain.
- `UNRESOLVED`: multiplicity not certified, tolerance matching ambiguous, representation lost, isolation exhausted, or coefficient uncertainty outside the central-polynomial contract.

Report denominators separately:
- number of fixtures generated;
- number with representable binary64 coefficients;
- number where F1 returned resolved roots;
- number where Sturm returned complete isolators;
- AGREEMENT / DISCREPANCY / UNRESOLVED counts;
- false-agreement count (must be zero by direct exact-rational fixture adjudication);
- false-discrepancy count after separating ideal-polynomial changes caused by binary64 rounding;
- abstention rate by cause;
- elapsed-time distribution and maximum rational numerator/denominator bit length.

Do not collapse unresolved cases into failures or successes. Do not report only the conditional agreement rate among resolved cases; always publish the full denominator and abstention rate.

## 6. Predeclared acceptance rules

The stress suite can pass only if all of the following hold:

1. No fixture is labelled AGREEMENT when the exact-rational reference for the actual binary64 coefficients demonstrates a different positive simple-root set.
2. Every multiplicity greater than one remains UNRESOLVED by F1 adjudication unless a separately approved F1 multiplicity contract is implemented.
3. Every isolation-depth/width exhaustion is fail-closed and returns no partial certificate.
4. Every non-finite or erased nonzero coefficient is rejected or classified UNRESOLVED; no silent coefficient deletion.
5. All scale transformations are compared after exact inverse mapping and against the actual transformed binary64 coefficient vector.
6. The report publishes all denominators, all abstentions and every discrepancy, including failed fixtures.
7. No threshold, tolerance, exponent ladder, seed, or fixture is modified after outcomes are observed. Any change requires a versioned protocol amendment and a new authorization.

A PASS means only that the implementation met these predeclared deterministic numerical stress criteria on this fixture grid. It does not establish exhaustive correctness for all real coefficients or all hardware/platforms.

## 7. Execution boundary and required authorization

This draft authorizes **no execution**. Before running it, a separate one-shot authorization must bind:

- exact source commit and all source/test blob identities;
- exact stress harness commit and fixture-generation specification;
- Python/runtime and dependency pins;
- exact command, working directory and runner;
- maximum fixture count, ULP ladder, scale exponents, isolation widths/depths and execution time budget;
- evidence schema and artifact hashes;
- explicit exclusions: no DGP experiment, no Monte Carlo calibration, no inferential coverage study and no C10 scientific execution.

Any source or protocol change after freeze requires a new snapshot and authorization. The previous one-shot authorization 003 is consumed and cannot be reused.

## 8. Current disposition and next operation

- Integrated deterministic software tests: **PASS — 73/73** on the frozen snapshot.
- Existing matrix v002: retained as historical design baseline; it is not retroactively rewritten.
- Adversarial numerical stress: **DESIGNED IN THIS DRAFT / NOT IMPLEMENTED / NOT EXECUTED**.
- Calibration and scientific C10-S execution: **NOT AUTHORIZED**.

**Next operation:** static implementation review of the proposed fixture generator and harness contract, followed by a frozen design and a separate execution authorization. Do not begin outer Monte Carlo calibration until the numerical stress gate is audited and accepted.
