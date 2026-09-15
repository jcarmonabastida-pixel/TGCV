# C10C-004 — G4.1 Predicate Operational Table

**Status:** FROZEN FOR G4 OPERATIONALIZATION

## Purpose

Freeze the operational predicate layer required before household-level reconstruction of baseline `T_acc,0` under G4.

G2 established the transformation universe and G3 established the semantic admissibility specification. G3 explicitly left one unresolved implementation dependency: the exact numeric response coding in the `.dta` had not yet been independently validated against value-label metadata. Therefore this artifact freezes the **predicate structure, variable routing, raw-code treatment, and transformation mapping** without inventing the semantic polarity of numeric codes that has not yet been independently validated.

## Frozen scope

Primary executable capability/agency block present in the baseline `.dta`:

- F1–F6 only: `j1_*` through `j9_*`, with six observed woman/activity slots per household where applicable.
- F7–F11 appearing in the instrument/dictionary but absent from the baseline `.dta` are not introduced into G4.
- `j9b*–j9d*` are retained as contextual/history/preference information and do not define primary `T_acc,0` predicates.
- `j10–j13`, `j14–j21`, `j22`, and `j2301–j2317` remain auxiliary unless a separately frozen admissibility predicate explicitly requires them.
- `j0*`, `k*`, `m*`, and administrative variables are routing/control/auxiliary information and do not define the transformation universe.

## Predicate table

| ID | Baseline variables | Semantic state condition | Transformation represented | Raw-code policy |
|---|---|---|---|---|
| P1 | `j1_1–j1_6` | Independent economic activity | `tau_independent_activity` | Preserve raw `1/2/-99/NaN`; numeric polarity must be label-validated before booleanization |
| P2 | `j2_1–j2_6` | Autonomous decision over materials required for activity | `tau_material_decision` | Preserve raw `1/2/NaN`; numeric polarity must be label-validated |
| P3 | `j3_1–j3_6` | Autonomous purchase/acquisition of materials | `tau_material_acquisition` | Preserve raw `1/2/NaN`; numeric polarity must be label-validated |
| P4 | `j4_1–j4_6` | Autonomous decision over required inputs | `tau_input_decision` | Preserve raw `1/2/NaN`; numeric polarity must be label-validated |
| P5 | `j5_1–j5_6` | Autonomous purchase/acquisition of inputs | `tau_input_acquisition` | Preserve raw `1/2/NaN`; numeric polarity must be label-validated |
| P6 | `j6_1–j6_6` | Autonomous decision over what to produce | `tau_production_decision` | Preserve raw `1/2/NaN`; numeric polarity must be label-validated |
| P7 | `j7_1–j7_6` | Produces something potentially tradeable | `tau_tradeable_output` | Preserve raw `1/2/-99/NaN`; numeric polarity must be label-validated |
| P8 | `j8_1–j8_6` | Autonomous decision whether to trade products | `tau_trade_decision` | Preserve raw `1/2/-99/NaN`; numeric polarity must be label-validated |
| P9 | `j9_1–j9_6` | Autonomous capacity to trade products | `tau_autonomous_trade` | Preserve raw `1/2/-99/NaN`; numeric polarity must be label-validated |

## Observed raw-code inventory

The baseline scan established the following observed raw-code classes across the household × woman/activity cells:

- `j1`: `-99`, `1`, `2`, `NaN`
- `j2`: `1`, `2`, `NaN`
- `j3`: `1`, `2`, `NaN`
- `j4`: `1`, `2`, `NaN`
- `j5`: `1`, `2`, `NaN`
- `j6`: `1`, `2`, `NaN`
- `j7`: `-99`, `1`, `2`, `NaN`
- `j8`: `-99`, `1`, `2`, `NaN`
- `j9`: `-99`, `1`, `2`, `NaN`

No numeric code is silently interpreted as TRUE/FALSE by this frozen artifact until the corresponding value-label semantics have been independently validated.

## Missing and special-code rule

- `NaN` is **UNRESOLVED/MISSING**, never automatically FALSE.
- Negative special codes such as `-99` are preserved and treated as **SPECIAL/UNRESOLVED** unless an independently validated routing rule establishes another meaning.
- A special/missing response cannot create an admissible transformation merely because the alternative state is absent.
- Missingness and routing must be reported separately from substantive FALSE states.

## Routing rule

`j0*` variables are treated as routing/control information. Their observed structure is conditional and not assumed to be a temporal sequence. A `j1→j2→…→j9` chain is a structural dependency chain, not an assumed time sequence.

The exact eligibility of each F1–F6 slot for predicate evaluation must therefore be resolved from the validated `j0*` routing semantics before household-level aggregation.

## Transformation rule

A baseline transformation is represented only through the explicit mapping:

`S0(h) → predicate state → admissible tau`

The following transformations are frozen as candidate structural elements:

1. independent economic activity;
2. autonomous material decision;
3. autonomous material acquisition;
4. autonomous input decision;
5. autonomous input acquisition;
6. autonomous production decision;
7. production of potentially tradeable output;
8. autonomous trade decision;
9. autonomous trade capacity.

These are accessibility elements, not claims that the transformations were realized, temporally executed, or caused by treatment.

## Household aggregation boundary

This artifact freezes the slot-level predicate definitions and transformation mapping. The household-level aggregation/routing rule is a separate G4 operational decision and must use only the validated slot eligibility and the frozen predicates above. No post-hoc aggregation based on treatment/control differences is permitted.

## Excluded from primary T_acc,0 definition

- `j9b*–j9d*` as direct transformation predicates;
- treatment-induced `client` / `admin_*` variables;
- endline variables;
- downstream outcomes;
- value measures;
- post-treatment realized trajectories;
- any transformation selected because it produces a statistically attractive treatment contrast.

## Integrity boundary

This G4.1 artifact does not establish G4 PASS, `T_acc,0` itself, `Delta T_acc`, treatment effects, mediation, trajectory effects, or value creation.

## Governance state

- Core: **UNCHANGED**
- RMA: **UNCHANGED**
- Evidence-to-Claim Matrix: **UNCHANGED**
- Claim-level upgrade: **NONE**

## Next operational step

Validate the numeric value-label semantics and `j0*` routing before boolean predicate execution and household-level `T_acc,0` aggregation.
