# EXT-1.1 Rust — `T_acc` Counterfactual Micro-Fixture v0.1

**Status:** DRAFT — executable verification pending  
**Purpose:** Demonstrate that the operationalized `T_acc` is not definitionally identical to realised trajectory `T_real`.

## 1. Fixture principle

The fixture is deliberately independent of the scientific Rust dataset. It uses a tiny **synthetic but fully frozen registry context** and package states for which candidate dependency-edge insertions can be checked by the real Cargo resolver.

The fixture MUST be evaluated using the same canonical ontology and resolver specification `R` as the eventual experiment.

The fixture is methodological evidence only; it is not evidence about the empirical Rust ecosystem.

## 2. Fixed package state

Package state:

`S_t = demo_pkg 1.0.0`

Manifest:

```toml
[package]
name = "demo_pkg"
version = "1.0.0"
edition = "2021"
resolver = "2"

[dependencies]
base = "=1.0.0"
```

Only normal, unconditional, non-optional registry dependencies are in scope.

## 3. Frozen fixture registry context

The fixture registry contains exactly these in-scope package/version records:

- `base 1.0.0`
- `candidate_a 1.0.0`
- `candidate_b 1.0.0`
- `candidate_c 1.0.0`

`candidate_a 1.0.0` has no additional dependency and therefore resolves successfully when added to `demo_pkg 1.0.0`.

`candidate_b 1.0.0` declares an unsatisfiable normal registry dependency on `impossible =9.9.9`; no such package/version exists in the frozen fixture registry.

`candidate_c 1.0.0` is present in the frozen registry at time `t`, but its dependency edge is introduced only in the later observed package state `S_t+1`. It is therefore the realised case.

The exact generated `.crate` artifacts, sparse-index records and their SHA-256 hashes MUST be committed as machine-readable fixture inputs/results after execution.

## 4. Candidate universe

For the fixture:

`U_t = {tau_a, tau_b, tau_c}`

where:

- `tau_a = (candidate_a, 1.0.0, =1.0.0)`
- `tau_b = (candidate_b, 1.0.0, =1.0.0)`
- `tau_c = (candidate_c, 1.0.0, =1.0.0)`

No realised-transition information is used to create this universe. All three candidate records are available in the frozen registry context independently of the later package state.

## 5. Required cases

### Case A — accessible + unrealised

`tau_a` MUST resolve successfully from `(S_t,C_t,R)` but must not occur in `T_real,t`.

Expected classification:

`tau_a ∈ T_acc,t`

`tau_a ∉ T_real,t`

### Case B — inaccessible + unrealised

`tau_b` MUST fail deterministic dependency resolution from `(S_t,C_t,R)` because its own dependency requirement cannot be satisfied in `C_t`, and it must not occur in `T_real,t`.

Expected classification:

`tau_b ∉ T_acc,t`

`tau_b ∉ T_real,t`

### Case C — realised

A later package state `S_t+1 = demo_pkg 1.1.0` contains the `candidate_c =1.0.0` dependency edge.

Expected classification:

`tau_c ∈ T_real,t`

Its prior accessibility MUST be evaluated independently from `(S_t,C_t,R)` and MUST NOT be inferred from its later occurrence.

## 6. Acceptance criteria

The fixture passes only if all three classifications are obtained exactly as specified and the generated machine-readable result is deterministic across two independent runs using the same frozen inputs.

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

The fixture structure is defined, but executable verification remains outstanding. Scientific dataset processing remains blocked until this fixture passes.
