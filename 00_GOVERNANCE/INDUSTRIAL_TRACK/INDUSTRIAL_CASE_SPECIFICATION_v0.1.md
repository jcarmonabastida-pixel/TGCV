# TGCV — Industrial Case Specification v0.1

**Date:** 2026-09-09  
**Status:** PROPOSED / DESIGN-ONLY  
**Origin:** EXT-UPD-4.9 / INDUSTRIAL-TRACK Governance Specification v0.1  
**Execution status:** NOT AUTHORIZED  
**Scientific evidence introduced:** NO

## 1. Purpose

Define the minimum specification by which a concrete industrial case may later be admitted to the INDUSTRIAL-TRACK. This artifact does not select, execute, or validate an industrial case.

## 2. Case status

No industrial case is selected by this specification. A candidate may only be designated after satisfying the entry conditions below through a subsequent governance review.

## 3. Required case definition

A candidate case record shall contain, before execution authorization:

- industrial decision context and decision owner/context boundary;
- explicit system boundary `S`;
- bounded unit of analysis;
- temporal frame and decision horizon;
- relevant state/context variables;
- candidate transformations and their enabling/limiting conditions;
- independently observable outcomes;
- material/data/setup access conditions;
- comparator capability, where differentiated utility is tested.

The case description must be independent of the expected TGCV result.

## 4. Unit-of-analysis admissibility

The unit shall permit independent reconstruction of:

`(S_t, C_t) → candidate transformation → accessibility/admissibility conditions → (S_{t+1}, C_{t+1}) → observed outcome`

The unit is not admissible if its boundaries, temporal ordering, or required observations can only be defined after inspecting TGCV-favorable results.

## 5. Variable register requirements

The future case package shall identify, freeze and version at least:

1. **State/context:** variables describing system and contextual conditions.
2. **Transformation:** candidate transformation identity and admissibility conditions.
3. **Accessibility:** material, setup, temporal and dependency conditions.
4. **Outcome:** independently observed consequence or decision result.
5. **Utility:** pre-specified practical benefit measure, distinct from `ΔT_acc`.

No variable may be defined as a proxy for the desired conclusion merely because it correlates with `ΔT_acc`.

## 6. Accessibility closure requirement

Before any comparative outcome assessment, the case must specify ex ante:

- admissible transformation rule;
- required material/data/configuration;
- temporal availability constraints;
- evidence required to establish accessibility;
- insufficient/ambiguous evidence;
- treatment of unresolved dependencies as **INCONCLUSIVE/INDETERMINATE** as applicable.

Accessibility cannot be inferred from the existence of a candidate in a repository or system alone.

## 7. Utility/comparator requirement

Where differentiated utility is tested, the case package must freeze before outcome assessment:

- practical analytical/decision task;
- baseline/comparator;
- utility dimensions;
- minimum meaningful difference, if applicable;
- observation period;
- sampling/inclusion rules;
- handling of null, adverse, missing and indeterminate results.

Utility shall not be defined as `ΔT_acc` itself.

## 8. Admission decision table

| Condition | Required state | Consequence |
|---|---|---|
| Concrete industrial context | CLOSED | Required for IT-G1 |
| System boundary | CLOSED | Required for IT-G1 |
| Unit of analysis | CLOSED | Required for IT-G1 |
| Temporal frame | CLOSED | Required for IT-G1 |
| Required variables | CLOSED | Required for IT-G2 |
| Accessibility criterion | CLOSED | Required for IT-G3 |
| Utility criterion/comparator | FROZEN | Required for IT-G4 |
| Execution authorization | EXPLICIT | Required for IT-G5 |

Any unresolved mandatory condition blocks progression; criteria may not be relaxed after observing results.

## 9. Evidence separation

This artifact is governance/design infrastructure. It creates no Core evidence and no industrial utility evidence. Any later industrial result must be separately classified and accompanied by an Evidence→Claim impact assessment.

## 10. Scientific boundary

The scientific Core remains:

- ontology: `S`;
- analytical object: `T_acc = F(S,C,L)`;
- central phenomenon: `ΔT_acc`;
- downstream chain: `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`;
- `I`: explanatory mechanism, not Core primitive.

This specification does not alter definitions, thresholds, falsification criteria, claim statuses, or epistemic states.

## 11. Authorization boundary

This artifact does **not** authorize:

- industrial case execution;
- dataset execution;
- further O3 accessibility execution;
- Stage C/D;
- partner evidential engagement;
- causal inference;
- value optimization;
- Core modification;
- claim upgrade;
- external-asset update representing utility as established.

## 12. Next gate

The next permissible governance activity is **IT-G1 Case Identifiability review** only after a concrete candidate case is separately proposed. Until then, INDUSTRIAL-TRACK remains PROPOSED and execution remains NOT AUTHORIZED.

**Disposition:** `INDUSTRIAL_CASE_SPECIFICATION = PROPOSED / DESIGN-ONLY / NO CASE SELECTED / NO EXECUTION AUTHORIZED`.
