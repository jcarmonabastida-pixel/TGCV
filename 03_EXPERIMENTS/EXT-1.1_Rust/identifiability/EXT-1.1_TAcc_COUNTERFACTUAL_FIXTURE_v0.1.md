# EXT-1.1 Rust — `T_acc` Counterfactual Micro-Fixture v0.1

**Status:** DRAFT — executable verification pending
**Purpose:** Demonstrate that the operationalized `T_acc` is not definitionally identical to realised trajectory `T_real`.

## 1. Fixture principle

The fixture is deliberately independent of the scientific Rust dataset. It uses a tiny frozen historical registry context and a package state for which candidate dependency-edge insertions can be checked manually.

The fixture MUST be evaluated using the same canonical ontology and resolver specification `R` as the eventual experiment.

## 2. Fixed package state

Package state:

`S_t = demo_pkg 1.0.0`

Manifest:

```toml
[package]
name = "demo_pkg"
version = "1.0.0"
edition = "2021"

[dependencies]
base = "=1.0.0"
```

Only normal, unconditional, non-optional registry dependencies are in scope.

## 3. Historical registry context

The fixture registry contains at least these package/version records:

- `base 1.0.0`
- `candidate_a 1.0.0`
- `candidate_b 1.0.0`
- `candidate_c 1.0.0`

`candidate_a 1.0.0` has a dependency graph that resolves successfully when added to `demo_pkg 1.0.0`.

`candidate_b 1.0.0` is constructed to have an unsatisfiable dependency requirement within the same frozen registry context.

`candidate_c 1.0.0` is the dependency edge introduced in a later published package state and is therefore used as the realised case.

The exact registry records and their hashes MUST be committed as machine-readable fixture inputs before execution.

## 4. Candidate universe

For the fixture:

`U_t = {tau_a, tau_b, tau_c}`

where:

- `tau_a = (candidate_a, 1.0.0, =1.0.0)`
- `tau_b = (candidate_b, 1.0.0, =1.0.0)`
- `tau_c = (candidate_c, 1.0.0, =1.0.0)`

No realised-transition information is used to create this universe.

## 5. Required cases

### Case A — accessible + unrealised

`tau_a` MUST resolve successfully from `(S_t,C_t,R)` but must not occur in `T_real,t`.

Expected classification:

`tau_a ∈ T_acc,t`

`tau_a ∉ T_real,t`

### Case B — inaccessible + unrealised

`tau_b` MUST fail deterministic dependency resolution from `(S_t,C_t,R)` and must not occur in `T_real,t`.

Expected classification:

`tau_b ∉ T_acc,t`

`tau_b ∉ T_real,t`

### Case C — realised

A later package state `S_t+1` contains the `candidate_c =1.0.0` dependency edge.

Expected classification:

`tau_c ∈ T_real,t`

Its prior accessibility MUST be evaluated independently from `(S_t,C_t,R)` and MUST NOT be inferred from its later occurrence.

## 6. Acceptance criteria

The fixture passes only if all three classifications are obtained exactly as specified and the generated machine-readable result is deterministic across two runs.

The fixture is a methodological test. It does not constitute evidence from the scientific Rust dataset.

## 7. Required execution artifacts

Before final protocol freeze, commit:

1. exact fixture registry records;
2. fixture package manifests;
3. frozen resolver specification `R`;
4. execution script;
5. machine-readable result;
6. expected result;
7. SHA-256 checksums;
8. two-run byte-identical comparison;
9. short manual verification record.

## 8. Status

**NOT YET EXECUTED.**

The fixture structure is defined, but the exact historical registry records, resolver environment and executable verification remain outstanding. Scientific dataset processing remains blocked until this fixture passes.
