# C10C-004 — G4 Baseline T_acc Reconstruction

**Status:** PROTOCOL — READY FOR EXECUTION

## Objective

Reconstruct the baseline household-level transformation-accessibility structure `T_acc,0` from the frozen C10C-004 transformation universe and the baseline state `S0`, using only pre-treatment information.

## Inputs

Primary source:

`Microcredit_BL_mini_anonym.dta`

Baseline dataset: 4,465 households.

Frozen semantic capability/agency block:

- `j1_*–j9_*`: independent activity, material/input control, productive decisions, potential trade, trade decision and trade capacity;
- `j9b*–j9d*`: prior activity, activity type and training interest;
- `j10–j13`: mobility/autonomy;
- `j14–j21`: productive work participation and time capacity;
- `j22`, `j2301–j2317`: women's credit state, retained as auxiliary state information unless required by a pre-specified transformation predicate.

Baseline resource/constraint variables may enter predicates only where required by the frozen admissibility specification.

## Reconstruction rule

For each household `h`:

`S0(h) → A(S0(h), τ) → T_acc,0(h)`

where `A` is the treatment-independent and outcome-independent admissibility predicate established at G3, and `τ` belongs to the transformation universe established at G2.

Observed baseline responses are state information. A transformation is represented only when an explicit admissibility mapping is specified.

## Required integrity checks

1. Deterministic reconstruction from identical inputs.
2. Household identity uniqueness.
3. Coverage and missingness accounting for every predicate input.
4. Explicit treatment of special/missing codes.
5. Logical consistency among related predicates.
6. No use of treatment assignment to construct admissibility.
7. No use of endline variables or downstream outcomes.
8. No post-hoc transformation selection.
9. Reproducible representation of each household's `T_acc,0`.
10. Independent rerun should produce identical structural output and hashes.

## Scientific gate

G4 passes only if baseline `T_acc,0` can be reconstructed operationally with sufficient coverage and reproducibility, with all exclusions and unresolved predicates explicitly reported.

G4 PASS does **not** establish `ΔT_acc`, treatment effects, mediation, downstream trajectory effects, or value creation.

## Governance boundary

- Core: **UNCHANGED**
- RMA: **UNCHANGED**
- Evidence-to-Claim Matrix: **UNCHANGED**
- Claim-level upgrade: **NONE** until structural treatment/control contrast is established.

## Execution state

**READY FOR LOCAL EXECUTION.**

The execution must use the canonical local C10C-004 baseline source and produce an auditable reconstruction artifact containing predicate definitions, coding decisions, coverage, household-level structural representation, integrity checks, and hashes.

## Next gate

**G5 — Endline T_acc Reconstruction**, conditional on successful G4 baseline reconstruction.
