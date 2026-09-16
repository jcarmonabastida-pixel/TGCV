# TGCV MT4-7 — Downstream Separation Protocol 001

**Status:** ANALYSIS PROTOCOL — NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16

## Objective

Test whether the frozen energy-system dataset permits an auditable separation between:

1. pre-decisional / technical candidate constraints;
2. realized transformation;
3. subsequent state or trajectory;
4. downstream outcome;
5. value-related variables.

The test must prevent realized adoption, generation, capacity, or outcome variables from being reclassified as `T_acc` merely because they are available in the same dataset.

## Frozen input

`TGCV_MT4_energy_public-dataset_v2.zip`  
SHA256: `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

## Layer rules

### A. Candidate admissibility / technical layer

CORE6 remains the bounded candidate technical representation:
`Fuel_efficiency`, `LF_min`, `LF_max`, `Peak_contr`, `Ramp_rate`, `Resource`.

`Potential_annual`, `Potential_installed`, `Buildrates`, and `Actual_*` must not be promoted automatically to `P_tau`.

### B. Realized transformation layer

Candidate observed transformation variables are `Actual_new_capacity` and `Actual_retired_capacity`. They represent realized/reconstructed system changes and must remain distinct from accessibility.

### C. State / trajectory layer

`Actual_capacity` and `Actual_generation` may describe subsequent realized system state/operation. They are not admissibility variables.

### D. Outcome layer

The executor must identify dataset variables that are temporally downstream of a transformation and can be treated as outcomes without being used to define the transformation itself. If no sufficiently clean outcome is identifiable, record the limitation.

### E. Value layer

Economic variables such as investment or operating costs may be value-relevant, but must not be treated as TGCV value realization without an explicit temporal and semantic rule. `Inv`, `Fixed_OM_annual`, and `Variable_OM` therefore remain candidate economic/value-related variables, not established `Delta V`.

## Required audit

The independent auditor must classify the relevant technology parameters into the five layers, report counts by layer, and flag any variable whose semantics or temporal status prevents clean assignment.

The audit must verify at minimum that:

- no `Actual_*` variable enters the CORE6 candidate rule;
- no downstream outcome/value variable enters the CORE6 candidate rule;
- realized transformation variables are temporally distinguishable from candidate constraints;
- state/trajectory variables are not used to define admissibility;
- economic/value variables remain isolated from accessibility.

## Decision rule

`MT4-7 PASS` requires a reproducible layer separation with no semantic substitution and no temporal leakage identified in the frozen rule.

`MT4-7 BOUNDED PASS` applies if the upstream/downstream separation is reproducible but the dataset lacks a sufficiently clean downstream outcome or value endpoint.

`MT4-7 FAIL` applies if the layers cannot be separated without using downstream information to define accessibility or transformation.

This test does not establish causal effects or full `P_tau` sufficiency.
