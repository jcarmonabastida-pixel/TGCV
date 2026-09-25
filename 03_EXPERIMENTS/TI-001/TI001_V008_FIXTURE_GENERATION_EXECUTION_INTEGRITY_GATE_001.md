# TI-001 V008 Fixture Generation Execution Integrity Gate 001

**Status:** BLOCKED — SCHEMA/GENERATOR ORDERING RECONCILIATION REQUIRED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false
**Generation authorization:** present

## Blocking discrepancy

The approved schema requires canonical decision-unit ordering within each pair to be:

1. `I1_FIRST`
2. `I2_FIRST`

However, the bound generator assigns a pair-level presentation orientation from the shuffled presentation stream and materializes the pair as either:

- `(I1_FIRST, I2_FIRST)`, or
- `(I2_FIRST, I1_FIRST)`.

Therefore the current generator can emit `I2_FIRST` before `I1_FIRST` for some pairs, which conflicts with §10 of the current schema specification.

## Gate consequence

The Generator–Schema Binding Preflight PASS is retained as the result of its implemented checks, but it did not test this exact canonical-order requirement. It therefore cannot be interpreted as proof of full schema/generator semantic equivalence.

The explicit generation authorization does not authorize changing the schema or generator semantics. Consequently, fixture generation is stopped before invoking `--generate`.

## Required reconciliation

Define and approve one unambiguous canonical rule for within-pair ordering, then update the affected specification/checker/generator artifacts consistently and rerun the relevant integrity preflights.

No fixture is to be generated until the reconciliation is PASS.

`scientific_execution = NOT_PERFORMED` remains in force.