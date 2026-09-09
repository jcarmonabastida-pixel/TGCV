# TR-132-MOD-1 — Fixture Instantiation and Freeze v0.1

**Status:** CURRENT / OPERATIVE — FROZEN PACKAGE
**Execution:** NOT AUTHORIZED
**Scientific result:** NONE
**Fixture:** `MOD1-FX-001`
**Package:** `TR132-MOD1-PKG-001`
**Target:** L3 bounded temporal identifiability

## 1. Freeze decision
The design-level package has now been instantiated with exact finite records. No placeholder transformation, state, predicate value, evidence classification, control case or realization schedule remains to be supplied for the defined fixture.

The package is frozen at `F0-MOD1-001`. The freeze is a governance/design state, not an execution result.

## 2. Exact frozen candidate universe
Exactly five candidates are included and identities are invariant across `t0` and `t1`:

- `TA`: admissible, resource `R1`, available at both timepoints; accessible.
- `TB`: admissible, resource `R1`, available at both timepoints; accessible but deliberately not realized.
- `TC`: technically possible but explicitly inadmissible; never accessible.
- `TD`: admissible, requires `R2`; inaccessible at `t0`, accessible at `t1`.
- `TE`: admissible, but one mandatory evidence condition is unresolved; indeterminate at both timepoints.

## 3. Exact state pair
`S_id=S-FX-001`, `C_id=C-FX-001` at both timepoints. `R1` is available at both. `R2` is unavailable at `t0` and available at `t1`. All authorization flags and temporal windows are valid at both timepoints.

No other accessibility-relevant variable changes.

## 4. Frozen accessibility predicate
`ACC(τ,t)=ID ∧ STATE ∧ ADM ∧ MAT ∧ SETUP ∧ AUTH ∧ TIME ∧ EVIDENCE`

Predicate version: `ACC-v0.1`. A false mandatory condition yields `INACCESSIBLE`; unresolved mandatory evidence yields `INDETERMINATE`.

## 5. Frozen adjudication
The exact pre-realization classifications are recorded in `ACCESSIBILITY_ADJUDICATION_v0.1.csv`. Adjudication is complete before the realization schedule is disclosed to the adjudication layer.

The resulting **design-certified target sets** for the L3 test are:
- `T_acc,t0+ = {TA, TB}`
- `T_acc,t1+ = {TA, TB, TD}`
- symmetric difference = `{TD}`

These are frozen package expectations, not empirical observations.

## 6. Frozen controls
`CTRL-A` through `CTRL-F` provide accessible/realized, accessible/unrealized, possible/inadmissible, admissible/inaccessible, evidence-indeterminate and state-enabled controls.

## 7. Freeze integrity
The following are immutable after `F0-MOD1-001`: candidate universe, identities, states, predicate, evidence rules, control classifications, realization schedule, target level, result schema and deterministic seed `132001`.

Any alteration requires a new package version and a new authorization path.

## 8. Authorization boundary
Instantiation and freeze are complete under the previously granted authorization for package instantiation. **Execution remains NOT AUTHORIZED.** No execution result, scientific evidence, claim upgrade, Core change, Rust processing or industrial operation is introduced by this artifact.

## 9. Integrity disposition
Package instantiation: `PASS`.
Package execution authorization: `PENDING SEPARATE REVIEW`.
Scientific result: `NONE`.
