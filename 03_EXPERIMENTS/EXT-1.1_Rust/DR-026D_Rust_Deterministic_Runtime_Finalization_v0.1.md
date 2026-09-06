# DR-026D — EXT-1.1 Rust Deterministic Runtime Finalization v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Date:** 2026-09-06  
**Scope:** Deterministic runtime and execution-environment finalization for the frozen EXT-1.1 confirmatory protocol  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A, DR-026C

## Governing question

Can the frozen confirmatory protocol be executed under a fully specified and reproducible software/runtime environment without introducing an implementation choice after confirmatory observations become available?

## Decision required before execution

The execution environment must be frozen before any confirmatory outcome construction, model fitting, prediction, metric computation, or result inspection.

### 1. Randomness

The primary learner is `sklearn.linear_model.LogisticRegression` with `solver='liblinear'`. Because the accepted DR-026C protocol currently specifies `random_state=None`, a deterministic seed must be explicitly frozen by this decision before execution.

**Proposed value:** `random_state = 0`.

No alternative seed may be selected after observing outcomes or model results. If the implementation proves that the selected configuration is deterministic without consuming randomness, the explicit seed remains part of the frozen protocol for reproducibility.

### 2. Python/runtime

The exact Python major/minor/patch version used for confirmatory execution must be recorded before execution.

**Requirement:** execution must fail closed if the runtime does not match the frozen environment manifest.

### 3. Scientific Python dependencies

The exact versions of:

- scikit-learn;
- NumPy;
- SciPy;

must be recorded in the environment manifest before execution.

The implementation must not silently install, upgrade, downgrade, or substitute these packages during execution.

### 4. Platform

The execution platform must be recorded, including operating system and architecture. The execution log must retain the runtime/platform information sufficient to identify the environment used.

### 5. Dataset identity

The exact SHA-256 digest of the frozen Rust dataset ZIP must be computed and recorded before confirmatory execution.

The execution program must verify this digest before reading the dataset. A mismatch is a hard failure; the run must not proceed.

### 6. Code identity

Every code artifact participating in confirmatory execution must be identified by Git commit and/or content SHA. The execution must occur from a clean checkout of the frozen repository state.

Any uncommitted modification, dirty working tree, or code artifact not included in the frozen execution manifest is a hard failure.

### 7. Frozen protocol manifest

The execution manifest must bind together the accepted decisions DR-023, DR-024, DR-025A, DR-026A and DR-026C and the deterministic runtime decision DR-026D.

No confirmatory script may override values contained in the manifest.

### 8. Reproducibility

The execution must be deterministic at the protocol level. A replay under the identical frozen environment, dataset and code must reproduce the same primary outputs within the explicitly documented numerical reproducibility tolerance, with exact equality required for all discrete/count/hash outputs.

### 9. Prohibited adaptive changes

After confirmatory execution begins, the following may not be changed in response to any observed result:

- outcome or horizon;
- eligibility or population;
- baseline representation;
- T_acc representation;
- tokenization or hashing;
- preprocessing;
- temporal split;
- learner/solver/regularization;
- random seed;
- primary metric;
- class handling;
- exclusions;
- dataset or code version.

Any necessary change requires a new ex-ante decision and a new execution gate.

## Required preflight audit

Before DR-027 acceptance, a structural preflight must verify:

1. exact accepted decision files are present;
2. required normative resolver code is present and identified;
3. dataset SHA-256 can be established;
4. runtime versions can be captured;
5. deterministic seed is explicitly configured;
6. execution manifest can be generated;
7. dirty/untracked implementation changes are detected;
8. no outcome/model/metric computation occurs during preflight;
9. no confirmatory result is inspected or used for any protocol choice.

## Acceptance boundary

DR-026D acceptance freezes the deterministic runtime environment. It does **not** authorize confirmatory execution.

After DR-026D acceptance, DR-027 will be the sole execution authorization gate.

## Falsification conditions

DR-026D fails if any of the following occurs:

- random seed remains implicit or mutable;
- required package versions cannot be frozen;
- dataset identity cannot be verified;
- execution code cannot be uniquely identified;
- runtime differs from the frozen manifest;
- execution can silently override frozen protocol values;
- preflight performs prohibited confirmatory computations;
- reproducibility requirements cannot be operationalized.

**No confirmatory outcome construction or model fitting is authorized by this proposal.**
