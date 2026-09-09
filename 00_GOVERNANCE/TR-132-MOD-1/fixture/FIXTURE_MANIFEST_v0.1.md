# TR-132-MOD-1 — Concrete Fixture Manifest v0.1

**Fixture ID:** `MOD1-FX-001`
**Package ID:** `TR132-MOD1-PKG-001`
**Package version:** `0.1`
**Status:** FROZEN DESIGN / EXECUTION NOT AUTHORIZED
**Target level:** L3 bounded temporal identifiability
**Deterministic seed:** `132001`
**Protocol:** `TR-132_EXECUTABLE_PROTOCOL_v0.1`
**Schema:** `TR-132-MOD-1_DESIGN_AUDIT_AND_FIXTURE_SCHEMA_v0.1`

## Scope
A finite synthetic fixture designed to test whether a bounded, independently certified change in accessible transformations can be identified without using realization outcomes to define accessibility.

## Frozen objects
- finite candidate universe: exactly five transformations (`TA`, `TB`, `TC`, `TD`, `TE`);
- two decision timepoints: `t0`, `t1`;
- stable transformation identities;
- fixed accessibility predicate version `ACC-v0.1`;
- pre-realization evidence adjudication;
- realization schedule frozen separately;
- controls and expected classifications frozen before execution;
- evidence manifest and provenance mapping frozen before execution.

## State design
`t0` and `t1` are identical except that resource `R2` is unavailable at `t0` and available at `t1`. No candidate identity, admissibility rule, evidence rule, or predicate component changes.

## Intended bounded phenomenon
`TD` is INACCESSIBLE at `t0` and ACCESSIBLE at `t1` solely because `R2` changes from unavailable to available. Therefore the certified bounded sets are expected to differ:
`T_acc,t0+ = {TA, TB}`
`T_acc,t1+ = {TA, TB, TD}`.

These are **expected classifications frozen for test control**, not observed execution results.

## Realization separation
`TA` and `TD` are scheduled for realization; `TB` is deliberately not realized. Accessibility is adjudicated before realization is disclosed to the adjudication record.

## Integrity rule
All package-input hashes are recorded in the separate immutable `PACKAGE_INPUT_MANIFEST_v0.1.md`. The fixture manifest itself is hashed there after this file reaches its final frozen content. No self-hash is embedded in this file.

Any post-freeze change, use of realization to establish accessibility, or alteration of the candidate universe/predicate/evidence threshold invalidates the package.
