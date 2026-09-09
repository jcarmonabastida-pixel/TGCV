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

## Frozen object integrity
The following blob SHA-1 values are the exact Git object identities of the frozen package inputs at the freeze commit:

| object | path | blob_sha |
|---|---|---|
| fixture_manifest | `00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md` | `PENDING_SELF_HASH` |
| evidence_manifest | `00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md` | `a5c5c3d3e7bdbb1f2e1c4f7b2d1d1e4f8a7c6b5d` |
| accessibility_adjudication | `00_GOVERNANCE/TR-132-MOD-1/fixture/ACCESSIBILITY_ADJUDICATION_v0.1.csv` | `a9c2dfbcb5c5baf2df61ef3d3de331e6e3d31a53` |
| control_cases | `00_GOVERNANCE/TR-132-MOD-1/fixture/CONTROL_CASES_v0.1.csv` | `63567783c74c35b0dfd3d08a6aa29a1541f62da5` |
| realization_schedule | `00_GOVERNANCE/TR-132-MOD-1/fixture/REALIZATION_SCHEDULE_v0.1.csv` | `fc7cc4a8ab2f6951cd5a388701e1eab23ef04ec8` |
| states | `00_GOVERNANCE/TR-132-MOD-1/fixture/STATES_v0.1.csv` | `b4b10c262b9eac53e039dad10ba1777b45b5d286` |
| transformations | `00_GOVERNANCE/TR-132-MOD-1/fixture/TRANSFORMATIONS_v0.1.csv` | `182cd12d5daede2b9646df5daa58f217410b53fb` |

**Important:** the evidence-manifest SHA above is a temporary placeholder and the fixture-manifest self-hash is intentionally unresolved because a file cannot contain its own final content hash. The authorization gate must replace this table with a mechanically generated immutable package manifest before empirical execution.

## Integrity rule
Any post-freeze change, use of realization to establish accessibility, or alteration of the candidate universe/predicate/evidence threshold invalidates the package.
