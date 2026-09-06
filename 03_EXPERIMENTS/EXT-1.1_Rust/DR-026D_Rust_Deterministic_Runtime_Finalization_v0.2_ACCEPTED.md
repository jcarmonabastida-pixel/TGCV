# DR-026D — EXT-1.1 Rust Deterministic Runtime Finalization v0.2

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION  
**Acceptance date:** 2026-09-07  
**Scope:** Deterministic runtime and execution-environment finalization for the frozen EXT-1.1 confirmatory protocol  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A, DR-026C

## Decision

DR-026D is accepted on the basis of the successful pre-confirmatory structural preflight. The deterministic runtime environment is frozen for the subsequent confirmatory execution gate DR-027.

## Frozen runtime

- Python: **3.14.7**
- Implementation: **CPython**
- Platform: **Windows 11 10.0.26200-SP0**
- Architecture: **AMD64**
- scikit-learn: **1.9.0**
- NumPy: **2.5.2**
- SciPy: **1.18.1**
- Explicit learner seed: **random_state = 0**

The execution environment must not silently install, upgrade, downgrade, or substitute these versions.

## Frozen dataset identity

Rust dataset ZIP:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Dataset size observed during preflight: 6,047,715,996 bytes.

The confirmatory execution must verify the SHA-256 digest before reading the dataset. A mismatch is a hard failure.

## Frozen code identity

The successful preflight was executed from Git HEAD:

`e4c105406d40ca7fa45e7d1e0b629b6c7682a202`

with a clean working tree at preflight time.

The confirmatory execution must occur from a clean checkout of the frozen repository state. Any uncommitted modification, dirty working tree, or execution artifact not included in the frozen manifest is a hard failure.

## Frozen protocol consistency

The preflight verified consistency with DR-026C:

- solver: `liblinear`
- regularization: L2
- C: `1.0`
- fit_intercept: `True`
- max_iter: `1000`
- tol: `1e-8`
- class_weight: `None`
- random_state: `0`
- hash dimension: `2^20 = 1048576`

The preflight also verified that no outcome labels, T_acc, model fitting, predictions, performance metrics, or significance calculations were performed.

## Reproducibility requirements

At protocol level, the confirmatory execution must be deterministic. A replay under the identical frozen environment, dataset and code must reproduce exact equality for all discrete/count/hash outputs and the explicitly documented numerical reproducibility tolerance for floating-point outputs.

## Manifest binding

The confirmatory execution manifest must bind DR-023, DR-024, DR-025A, DR-026A, DR-026C and DR-026D. No confirmatory implementation may override frozen values from those decisions.

## Prohibited adaptive changes

After confirmatory execution begins, no observed result may be used to change the outcome/horizon, population, B representation, T_acc representation, tokenization/hashing, preprocessing, temporal split, learner, solver, regularization, seed, metric, class handling, exclusions, dataset, or code version.

Any necessary methodological change requires a new ex-ante decision and a new execution gate.

## Acceptance basis

The DR-026D structural preflight returned:

`DR026D_PREFLIGHT_PASS: True`

with:

- `GIT_STATUS_CLEAN: True`
- `REQUIRED_ARTIFACTS_PRESENT: True`
- `RANDOM_SEED_EXPLICIT: True`
- `HASH_DIMENSION_FROZEN: True`
- `MODEL_CONFIGURATION_FROZEN: True`
- `PROHIBITED_COMPUTATIONS_ALL_FALSE: True`

No confirmatory outcome, T_acc, model fit, prediction, metric, or significance result contributed to this acceptance.

The initial preflight failure was caused solely by untracked local execution artifacts. Those artifacts were excluded locally without deletion or modification of scientific evidence; the versioned repository state was not altered by that cleanup.

## Boundary

This decision freezes the deterministic runtime environment. **It does not authorize confirmatory execution.**

DR-027 remains the sole execution authorization gate.
