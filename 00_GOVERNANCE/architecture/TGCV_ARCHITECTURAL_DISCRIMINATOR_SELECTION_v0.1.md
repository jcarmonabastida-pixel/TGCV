# TGCV — Architectural Discriminator Selection Record v0.1

**Status:** CURRENT GOVERNANCE DESIGN / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision ID:** ARCH-DISC-001  
**Parent:** `TGCV_ARCHITECTURAL_DISCRIMINATION_CRITERIA_v0.1.md`

## Decision

Select **D1 — Same accessible set, different internal organisation** as the first architectural discriminator to be formalised.

This is a design selection, not a scientific result and not an endorsement that TSDI is correct.

## Rationale

D1 provides the cleanest minimal separation between the inherited and TSDI propositions:

- Under A, two cases with the same relevant `S` and `T_acc` should be equivalent for predictions that use only the inherited representation.
- Under B, two cases may have the same transformation membership while differing in the relations/dependencies organising those transformations.
- Therefore, a controlled comparison can ask whether a future observable differs when set membership is held fixed and only the candidate structural organisation differs.

This directly tests the architectural distinction rather than testing whether `T_acc` changes.

## Frozen conceptual contrast

**A prediction basis:** `S_t + T_acc,t` (plus pre-specified inherited auxiliary variables).

**B prediction basis:** the same common information plus a pre-specified structural organisation of the transformation space.

The experiment must not permit B to introduce arbitrary additional predictors after observing outcomes.

## Minimal observable

The primary observable must be a **future transformation/trajectory outcome** that is:

1. defined independently of A/B terminology;
2. measurable after the controlled initial condition;
3. identical in definition across both conditions;
4. not used to define the transformation space or its internal organisation.

The exact operational observable remains to be specified in the experimental package.

## Required control

The future outcome must be compared between matched cases satisfying:

`T_acc^(1) = T_acc^(2)`

while the pre-registered structural organisation differs:

`G_tau^(1) != G_tau^(2)`

where `G_tau` denotes the candidate relational/dependency structure.

Any residual difference in baseline state, accessible-set membership, intervention, exposure or measurement must be controlled or explicitly modelled before the test is admissible.

## Discrimination logic

- **Potential FOR-B / AGAINST-A:** same `T_acc`, different `G_tau`, reproducible difference in the pre-specified future observable, with the difference specifically attributable to `G_tau`.
- **Potential AGAINST-B:** same `T_acc`, different `G_tau`, but no reproducible difference where B predicts one under its frozen mechanism.
- **NON-DISCRIMINATING:** no difference, or a difference explainable equally under A without the disputed structural object.
- **INVALID:** structural organisation or outcome was defined retrospectively, or the equality of `T_acc` was not independently verified.

## Mandatory anti-circularity rule

`G_tau` must be defined before the future outcome is observed. The future outcome must not be used to construct `G_tau`, `T_acc`, or the transformation universe.

## Next gate

Before any scientific preflight, the next document must freeze:

1. the representation of `T_acc`;
2. the representation of `G_tau`;
3. the matching/equivalence procedure;
4. the independent future observable;
5. the A prediction rule;
6. the B prediction rule;
7. the statistical discrimination criterion;
8. failure/invalidity conditions;
9. replication requirements.

**No scientific execution is authorized by this record.**
