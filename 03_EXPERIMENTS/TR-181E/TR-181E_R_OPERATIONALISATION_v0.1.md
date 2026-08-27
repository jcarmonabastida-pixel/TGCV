# TR-181E — R Operationalisation v0.1

**Status:** PROPOSED — NOT FROZEN
**Date:** 2026-08-27

## 1. Design principle

R is a derived representation of the transformation structure accessible from the pre-outcome snapshot. It is not an additional ontological primitive and it must not encode future trajectory or outcome information.

The Core defines the analytical object as `T_acc = F(S,C,L)` and the phenomenon as change in that structure. Accessibility is represented through realisation conditions rather than defined circularly by the word accessible.

## 2. Proposed operational object

For a snapshot `S`, define a finite candidate transformation universe `T` and a binary realisation predicate `P_tau(S,C,L)`. Then:

`T_acc(S) = { tau in T : P_tau(S,C,L) = 1 }`

For TR-181E, R is proposed to encode the transformation structure through a fixed, pre-declared feature vector derived from `T_acc`, rather than through raw graph statistics alone.

## 3. Proposed feature families

The representation should contain, at minimum:

- family-specific accessible-transformation counts;
- total accessible-transformation count;
- structural diversity across transformation families;
- transformation-to-component incidence summaries where defined by the transformation schema.

All feature definitions, ordering and normalisation must be frozen before test evaluation.

## 4. Leakage constraints

R may use only information available in the frozen pre-outcome snapshot and the pre-declared transformation schema. It must not use:

- future trajectory;
- outcome;
- labels derived from outcome;
- post-snapshot resources;
- test-set statistics;
- model residuals or predictions.

## 5. Baseline separation

B remains the conventional snapshot representation containing component count, the three resource values and objective identity. R must be evaluated as an incremental relational/transformation representation, not as a disguised duplicate of B.

## 6. Important limitation

The historical EMP-1.1 family predicates and exact R encoding are not recoverable from the currently available record. Therefore this document is a **new operational proposal**, not a reconstruction of historical EMP-1.1 code.

## 7. Required next decision

Before this can become `v1.0 FROZEN`, we must specify the exact candidate transformation universe and predicates for each family and demonstrate that they are derivable from the current TGCV Core without importing an empirical result into the definition.

**Gate status:** PROPOSED / NOT FROZEN / NO TEST EXECUTION AUTHORIZED.
