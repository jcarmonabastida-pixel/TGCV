# TGCV — TR-181E Reimplementation Specification v0.1

**Status:** BUILD SPECIFICATION — NOT FROZEN
**Purpose:** Define a new, explicitly identified implementation of the frozen MVE-1.0 semantics for the TR-181E predictive pilot. This is not represented as recovery of historical code.

## 1. Provenance boundary

Historical EMP-1.1 evidence and the frozen MVE-1.0 specification are authoritative. No implementation detail absent from those records may be silently reconstructed and presented as historical fact.

The implementation produced from this specification will carry its own version, hash and reproducibility record.

## 2. Equivalence target

The implementation must reproduce the semantics frozen in MVE-1.0:

- state `S` and contextual conditions `C` define the transformation domain;
- `T_acc = F(S,C,L)` is the accessible transformation set;
- `ΔT_acc` denotes change in that set;
- `I` is explanatory/mechanistic, not a Core primitive;
- the tested representation `R` encodes the relevant relational structure of accessible transformations;
- the implementation must not introduce additional predictive information unrelated to the declared representation.

## 3. Required implementation layers

```text
configuration
   ↓
state/context representation
   ↓
transformation universe
   ↓
accessibility predicate
   ↓
accessible transformation set
   ↓
relational representation R
   ↓
prediction dataset
   ↓
model/evaluation
```

Each layer must have a deterministic interface and machine-readable configuration.

## 4. Non-negotiable constraints

1. No optimisation of `R` against the pilot outcome.
2. No access to the future test outcome when constructing predictors.
3. Baseline and relational representations use matched observations and splits.
4. Any randomness must be explicitly seeded.
5. Dataset generation must be independent of EMP-1.1 outcomes.
6. All exclusions and preprocessing rules must be explicit.
7. Implementation changes after equivalence testing create a new implementation version.

## 5. Equivalence tests before TR-181E

### E1 — Semantic unit tests
Verify each transformation type, resource constraint and accessibility condition against the frozen MVE specification.

### E2 — Determinism test
Same configuration + same seed → identical generated state/transition representation.

### E3 — Structural invariants
Verify declared counts/distributions and conservation properties of the generated representation.

### E4 — R construction test
Verify that `R` is derived solely from the declared accessible-transformation structure and that no outcome variable enters its construction.

### E5 — Baseline/control compatibility
Verify identical observational units, splits and eligible cases across baseline and relational arms.

### E6 — Leakage audit
Programmatically verify that future outcome fields cannot enter feature construction.

### E7 — Independent implementation review
A second inspection of the implementation/configuration must confirm that it follows this specification without outcome-driven tuning.

## 6. Freeze candidate

The reimplementation may become **TR-181E IMPLEMENTATION FROZEN** only after E1–E7 pass and the following are recorded:

- source commit SHA;
- implementation version;
- configuration hash;
- generator seed(s);
- dependency/environment specification;
- test results;
- exact dataset-generation command;
- checksum of generated pilot data;
- reviewer record.

## 7. Separation from confirmatory inference

The pilot implementation freeze does not open or determine the confirmatory dataset. TR-181E remains a pilot for effect-size and variability estimation until its results are analysed under its registered rules.

## 8. Failure policy

If an equivalence test fails, do not patch silently. Record the failure, identify whether the issue concerns the implementation or the frozen specification, and issue a new version with a traceable rationale.

## 9. Current state

**MVE-1.0:** frozen.

**Historical implementation recovery:** not established.

**New implementation:** specification only.

**TR-181E execution:** blocked pending implementation build and E1–E7 equivalence tests.
