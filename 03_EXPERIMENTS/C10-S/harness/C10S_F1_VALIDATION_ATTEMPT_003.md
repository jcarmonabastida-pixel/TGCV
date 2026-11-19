# C10-S F1 — Integrated Correction and Validation Preparation 003

**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen source commit:** `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b`  
**Freeze manifest:** `C10S_F1_VALIDATION_FREEZE_MANIFEST_002.md`  
**Manifest commit:** `fef2b4c16de6e7380cb97495f080c0bfbe9542b6`  
**Workflow commit:** `c4095607ac7ea359f1626d157547c4b2e6e12824`  
**Workflow blob:** `d10a1beb0ebf3afa057198f84b167c61efc7f050`  
**Authorization draft:** `C10S_F1_INTEGRATED_NUMERICAL_VALIDATION_AUTHORIZATION_DRAFT_003.json`  
**Authorization state:** `DRAFT_NOT_APPROVED`

## 1. Corrections implemented

### C1 — Scale-equivariant profile-LR endpoint inversion

The previous lower-endpoint discrepancy was caused by using an absolute root tolerance in physical variance units. The F1 confidence-set inversion now solves in the dimensionless coordinate (x=\tau/s_{ref}), where (s_{ref}=\max(MSW,S^2_{means})). Lower and upper endpoints use the same normalized LR function and root tolerances, then map back to physical variance.

The profile reference scale no longer has an absolute (10^{-12}) variance floor. Positive scale is validated before the log-scale optimizer is called. Conversion back to physical variance fails closed on overflow or positive underflow.

### C2 — Consistent scale convention across F1 numerical paths

A cross-call-site review found the same fixed variance floor in polynomial-root normalization and nuisance-optimizer scanning. These floors were removed as well. Profile likelihood, polynomial normalization and nuisance diagnostics now use positive data-derived reference scales. The LR likelihood, score polynomial, parameter domain and caller-supplied cutoff were not changed.

### C3 — Root-restoration tests

The test module now explicitly imports `_restore_polynomial_scale`. The existing underflow and overflow tests can therefore reach the helper rather than fail with `NameError`.

### C4 — Equivariance regression contract

The test retains the observation multipliers (10^{-4},10^{-2},10^2,10^4). It checks lower and upper endpoints after transforming back to baseline units with `delta=1e-8), and checks the MLE with `delta=1e-10). These bounds are tighter than the prior assertions; no tolerance was relaxed.

## 2. Static provenance checks completed

At the exact frozen commit `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b), all nine blob identities in Freeze Manifest 002 were fetched directly and matched the values pinned in the workflow.

The workflow's nine expected blob lines were also inspected and match those same paths and identities. The workflow is configured for the corrected research branch and the exact authorization ID `C10S-F1-INTEGRATED-VALIDATION-20261119-03`. It checks out the frozen commit in detached mode.

## 3. Validation not executed

- No test module was executed.
- No Python compile check was run.
- No Monte Carlo calibration or DGP execution was run.
- No scientific execution was run.
- No changes were made to `main`.
- The prior authorization 002 remains consumed and is not reused.

The new one-shot authorization draft binds the frozen commit, manifest, workflow, four test modules, Python 3.12.3 and exact dependency pins. It remains unapproved.

## 4. Decision

**Implementation state:** `CORRECTIONS IMPLEMENTED`  
**Static identity review:** `PASS — NINE OF NINE FROZEN BLOBS MATCH`  
**Test execution:** `NOT RUN`  
**Numerical validation:** `PENDING NEW AUTHORIZATION`  
**Scientific closure:** `NOT CLAIMED`

A user approval is required before the workflow can be triggered. A PASS in that run would remain bounded to the four deterministic software test modules and would not establish exhaustive mathematical correctness, uncertainty-aware certification, inferential validity, causal contribution, or C10 closure.
