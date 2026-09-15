# C10C-004 — G3 Admissibility Predicate Reproducibility

**Status:** PASS — BOUNDED PREDICATE SPECIFICATION

## Scope

G3 evaluates whether the admissibility logic for the frozen transformation universe can be specified reproducibly and independently of treatment effects, downstream outcomes, and realized trajectories.

## Result

**PASS — BOUNDED PREDICATE SPECIFICATION.**

The complete baseline variable dictionary now permits variable-level semantic specification of the principal capability/agency predicates, especially the `j` block:

- `j1_*`: independent economic activity;
- `j2_*`, `j3_*`: decision and autonomous acquisition of materials;
- `j4_*`, `j5_*`: decision and autonomous acquisition of inputs;
- `j6_*`: autonomous productive decisions;
- `j7_*`: production with potential for trade;
- `j8_*`: autonomous decision to trade;
- `j9_*`: autonomous capacity to trade;
- `j9b*`, `j9c*`, `j9d*`: prior independent activity, activity type, and desired training;
- `j10–j13`: mobility and autonomy conditions;
- `j14–j21`: productive work participation and time capacity;
- `j22`, `j2301–j2317`: women's credit-related state.

These variables provide a reproducible semantic basis for defining admissibility conditions without using endline treatment differences or downstream outcomes to construct the transformation universe.

## Predicate logic boundary

The operational distinction is:

`variable → semantic state condition → admissibility predicate → transformation`

Observed change in a variable is not itself treated as a transformation or as evidence of `ΔT_acc`.

The admissibility predicate must remain:

1. treatment-independent;
2. outcome-independent;
3. defined from the frozen transformation universe;
4. reproducible by an independent executor;
5. distinct from realized execution of the transformation.

## Limitation

The exact numeric response coding of the `.dta` variables has not yet been independently validated against value-label metadata for every predicate. Therefore this gate establishes the reproducibility of the **semantic predicate specification**, not yet the executable household-level `T_acc` reconstruction.

## Exclusions

G3 does not establish:

- baseline `T_acc` itself;
- `ΔT_acc`;
- a treatment effect on transformation accessibility;
- mediation;
- downstream trajectory effects;
- value creation effects.

Treatment-induced `client` / `admin_*` variables remain auxiliary and do not define the admissibility universe.

## Governance state

- Core: **UNCHANGED**
- RMA: **UNCHANGED**
- Evidence-to-Claim Matrix: **UNCHANGED**
- Claim-level upgrade: **NONE**
- Scientific conclusion: **NONE**

## Next gate

**G4 — Baseline T_acc Reconstruction**

G4 must operationalize the predicates on the baseline dataset, construct household-level accessible transformation structures, and verify reconstruction integrity before any treatment/control structural contrast is interpreted.
