# C10-S F1 — Numerical Stress Harness Implementation Boundary (Draft 001)

**Status:** IMPLEMENTED — STATIC REVIEW ONLY — NOT EXECUTED  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Design source:** `C10S_F1_NUMERICAL_STRESS_DESIGN_DRAFT_001.md`  
**Implementation:** `c10s_f1_numerical_stress.py`  
**Frozen F1 validation baseline:** `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b`

## 1. Purpose

This record documents the first deterministic fixture generator and callable stress harness for F1's numerical characterization. It is an implementation artifact only. Importing the module does not launch a run; both runner functions must be invoked explicitly.

No test, compile check, stress run, Monte Carlo calibration, or scientific C10-S execution was performed while preparing this artifact.

## 2. Historical reuse

The implementation reuses, without modifying:

- `c10s_f1_between_profile_likelihood.py` — data-derived F1 score-polynomial construction, profile likelihood and positive-root reconstruction;
- `c10s_f1_independent_root_isolator.py` — exact-rational Sturm reference, degree at most three;
- `c10s_f1_root_adjudication.py` — F1-row-to-score-polynomial-to-Sturm adjudication.

The validated baseline source files remain unchanged. The new harness is additive.

## 3. Implemented fixture lanes

### Polynomial/Sturm lane

- **N1:** exact-rational simple-root separation ladder, close pair plus negative root, double-plus-simple and triple-root fixtures.
- **N2:** independent coefficient perturbations at ±1 and ±2 adjacent binary64 representable values. Each coefficient is perturbed separately; no combinatorial cross-product is implied.
- **N3:** exact-rational amplitude and variable-coordinate scaling at exponents −500, −200, −50, 0, 50, 200 and 500.
- **N5:** one close-pair polynomial crossed with three exact-rational width settings and five depth settings.
- **N6:** exact lower/upper endpoint roots, zero root, negative root, degree-one, nonzero constant and identically-zero polynomial cases.

The fixture record preserves the ideal rational coefficients, ideal roots where known, binary64 hexadecimal coefficients, exact rationalization of the binary64 values, domain, transformation, perturbation, width/depth settings and Sturm output. Nonrepresentable coefficient vectors are classified as representation-unresolved before Sturm is called.

The current roster contains 56 base fixtures; N5 expands to 15 width/depth combinations in the polynomial runner, for 70 records total. This is a deterministic design count, not an execution result.

### F1 end-to-end lane

N4 uses the existing observed-row interface and a fixed observation-scale ladder (2^k), (k in {-100,-50,-20,0,20,50,100}). It records the profile interval, MLE, F1 polynomial result and existing F1/Sturm adjudication after inverse scale mapping. Fail-closed exceptions remain visible as records.

## 4. Critical interface boundary discovered during implementation

The current `adjudicate_f1_roots` interface accepts observed rows and recomputes the F1 score polynomial. It does not accept an arbitrary polynomial coefficient vector. The F1 numerical root reconstruction is embedded in `f1_score_polynomial_diagnostic` and depends on the model-derived sufficient statistics.

Consequently:

- N1–N3 and N5–N6 currently characterize the independent exact-rational Sturm reference and its representation/resolution/fail-closed behavior.
- They do **not** claim arbitrary-polynomial F1-versus-Sturm concordance.
- N4 is the F1 end-to-end data-derived scale lane.
- False-agreement and false-discrepancy rates for arbitrary polynomial fixtures are explicitly marked not applicable, not silently reported as zero.

This boundary preserves the validated F1 source unchanged. Extending arbitrary polynomial concordance would require a separately reviewed pure-polynomial F1 solver interface or a principled inverse construction from valid F1 sufficient statistics. Neither is smuggled into this additive harness.

## 5. Static implementation review

The code has been inspected against the existing module signatures and contracts:

- coefficients are supplied in ascending order, matching the Sturm API;
- exact rational fixture construction is used before binary64 conversion;
- ULP perturbations use deterministic `math.nextafter` steps;
- exact binary64 coefficient values are recorded with `float.hex()` and `Fraction.from_float`;
- finite domains are explicitly supplied for the endpoint fixtures;
- N5 varies both `max_width` and `max_depth`;
- Sturm's `ROOTS_UNRESOLVED` result is preserved without partial roots;
- no randomness, external data, parameter fitting, or import-time execution is introduced;
- the validated F1, Sturm and adjudication source modules are not edited.

This is a static compatibility review only. It does not establish syntax/runtime correctness or numerical behavior; those require a separately authorized validation.

## 6. Execution boundary

**Not authorized and not performed:**

- invoking `run_polynomial_stress_grid()`;
- invoking `run_f1_observation_scale_ladder()`;
- unit tests, compilation or smoke tests;
- Monte Carlo calibration;
- DGP execution or inferential coverage study;
- scientific C10-S execution.

The two runner functions return in-memory records only; they do not write evidence files or initiate workflows.

## 7. Next operation

Before authorization, perform a second static design review focused on:
1. whether the chosen exponent/ULP/depth ladders are bounded and scientifically adequate;
2. whether the F1 scale ladder's recorded invariance metrics need explicit predeclared tolerances and acceptance states;
3. whether N1–N3/N5–N6 should remain a Sturm-only numerical reference lane or whether a separate pure-polynomial F1 solver API is justified;
4. whether the evidence schema should be JSONL plus summary JSON with deterministic canonicalization and hashes.

Then freeze the harness source and exact blob identities. A new one-shot authorization must identify the exact commit, runtime, commands, fixture counts and outputs. No prior authorization is reusable.
