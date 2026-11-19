# C10-S F1 — Integrated Validation Attempt 002

**Authorization:** `C10S-F1-INTEGRATED-VALIDATION-20261119-02`  
**Authorization approval commit:** `ce6ee286470bde0098ffa2a1e89bd921b5673656`  
**Frozen source commit:** `0d430adae891b3914475c60334d93e977efc44cc`  
**Workflow run:** [44522352509](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44522352509)  
**Job:** `135553916921`  
**Artifact:** [c10s-f1-integrated-validation-002](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44522352509/artifacts/14528261759)  
**Artifact SHA-256:** `929b08b509478da643edcf2d0d2696f410b996c3a9152e2ab248b68ac1e75608`  
**Outcome:** `FAIL — TEST SUITE COMPLETED WITH 3 DEFECTS`

## Environment and provenance

- Runner: GitHub-hosted `ubuntu-24.04`, image `20261111.370.1`
- Python: `3.12.3`
- NumPy: `2.1.3`
- SciPy: `1.14.1`
- Checkout: detached HEAD at the exact frozen commit.
- Working tree: clean before evidence creation.
- Nine expected Git blob identities: all nine matched exactly.
- All four test modules imported successfully.
- Exact authorized unittest command was executed once.
- Exit code: `1`.
- Total tests: `73`; failures: `1`; errors: `2`; passed: `70`.

## Test defects

### E1 — Missing import in the test module (two errors)

Both tests call `_restore_polynomial_scale` without importing it into the test module namespace:

- `test_polynomial_root_restore_rejects_underflow`
- `test_polynomial_root_restore_rejects_overflow`

Both fail with `NameError: name '_restore_polynomial_scale' is not defined`. The function exists in the frozen implementation; the test module's explicit import list includes `_normalize_scaled_polynomial` but omits `_restore_polynomial_scale`.

Classification: **test harness defect / unexecuted assertions**, not evidence that the production restore function itself fails.

### F1 — Observation-scale equivariance tolerance failure (one failure)

- Test: `test_profile_interval_is_equivariant_to_observation_scale`
- Assertion: lower endpoint after rescaling observations and dividing variance by scale squared.
- Observed: `0.2776353140133947`
- Expected baseline: `0.2776430627638891`
- Absolute difference: approximately `7.74875e-6`
- Test tolerance: `places=6` (rounding tolerance approximately (5\times10^{-7})).

The current confidence-set implementation solves the LR endpoint using `brentq` with `xtol=1e-12`, `rtol=1e-12`; the scale-equivariance assertion nevertheless fails. This needs a targeted numerical diagnosis before deciding whether the implementation, the scale-transformation test, or the stated tolerance is wrong. Do not simply relax the tolerance without an error-budget argument.

Classification: **numerical equivariance discrepancy requiring diagnosis**.

## Scope and scientific interpretation

- The preflight and provenance checks passed.
- The test suite ran to completion, so this is not an environment failure.
- 70 tests passed; 3 test outcomes did not pass (2 errors, 1 failure).
- The two NameErrors leave the root-restoration assertions untested.
- The scale-equivariance property is not established by this run.
- No claim of F1 validation, exhaustive correctness, mathematical certification, inferential validity, or scientific closure is warranted.
- No Monte Carlo calibration or C10 scientific execution occurred.
- No frozen source files or `main` were modified by the run.

## Disposition

Authorization 002 is consumed and cannot be reused. Correct the test import and investigate the scale-equivariance discrepancy on a new research snapshot. Then prepare a new exact freeze and a new one-shot authorization before any further execution.
