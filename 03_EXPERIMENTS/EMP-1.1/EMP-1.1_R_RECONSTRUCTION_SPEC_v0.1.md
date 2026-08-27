# EMP-1.1 — R Reconstruction Specification v0.1

**Status:** CONTROLLED RECONSTRUCTION SPECIFICATION — NOT VERIFIED
**Date:** 2026-08-27

## Objective

Define the reconstruction boundary for the mapping from a frozen episode snapshot to the TGCV representation `R`, without claiming historical source recovery.

## Source-of-truth hierarchy

1. Frozen EMP-1.1 protocol.
2. Frozen dataset records.
3. Other explicitly frozen experiment artifacts.
4. Only then, controlled reconstruction assumptions.

The known final result is never an input to the reconstruction.

## Required mapping

`S_snapshot -> T_acc -> R -> learner features`

where `T_acc` is the set/structure of accessible transformations induced by the frozen snapshot and `R` is the representation specified by EMP-1.1.

## Evidence currently available

The frozen protocol states that R is derived from accessible-transformation structure at the frozen snapshot and that the baseline B contains component count, three resource values and objective identity while excluding relational edge structure.

The sealed confirmatory episodes contain snapshots with components, directed edges, resource values, objective identity, trajectories and outcomes.

## Open reconstruction items

The following are not to be guessed:

- exact transformation-family predicates;
- exact edge semantics;
- exact transition equations;
- accessibility closure rule;
- exact aggregation/encoding from `T_acc` to `R`;
- ordering of R features;
- handling of empty/degenerate transformation sets;
- any normalization or categorical encoding.

## Reconstruction classes

Each implementation element must be labelled:

- `SPECIFIED`: directly stated by a frozen artifact;
- `DERIVED`: logically determined by specified rules with no free choice;
- `RECONSTRUCTED`: requires an explicit implementation choice;
- `VERIFIED`: independently tested against an acceptance criterion.

## Verification gate

R reconstruction cannot be declared verified until:

1. every feature has a traceable definition;
2. the same snapshot always produces the same R;
3. no information from future trajectory/outcome enters R;
4. R uses only information permitted by the frozen protocol;
5. the implementation can process the sealed dataset without modifying it;
6. the evaluation harness can consume R independently of the reconstruction code;
7. any reconstructed assumption is separately recorded.

## Current status

**BLOCKED — exact transformation/accessibility semantics not yet established from recovered artifacts.**

No executable implementation is to be promoted to canonical status until this gate is passed.
