# EXT-UPD-4.8 — Stage B Accessibility Closure Reassessment — Execution Authorization v0.1

**Status:** CLOSED / EXECUTION AUTHORIZED — ONE BOUNDED CORRECTIVE ASSESSMENT ONLY  
**Date:** 2026-09-09  
**Decision:** `EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_DECISION_v0.1.md`  
**Design:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_DESIGN_v0.1.md`  
**Design audit:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_DESIGN_AUDIT_v0.1.md`  
**Preflight:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_PREFLIGHT_v0.1.md`

## 1. Authorization purpose

Authorize exactly one local, bounded corrective assessment of the accessibility status of O3 in IUT-A-01.

This authorization exists solely to determine whether the methodological defect identified in the original Stage-B execution can be resolved by independently grounded native decision-time evidence.

It does **not** authorize a second comparative IUT execution.

## 2. Frozen corrective question

> **Can O3 accessibility at decision time be closed from independently frozen native evidence, with an outcome-independent rule that is native to the case or a logically necessary inference, without analyst-supplied completion?**

## 3. Frozen hypotheses

### H-A — Case-specific closure

The native evidence contains sufficient decision-time information to close O3 membership without analyst completion. The original defect is therefore attributable to the synthetic execution construction.

### H-B — Deeper operationalization boundary

The native evidence remains insufficient to close O3 membership without analyst completion. The accessibility boundary therefore persists.

No hypothesis is privileged in advance.

## 4. Authorized scope

Only:

- case `IUT-A-01`;
- option `O3`;
- native tooling/setup conditions relevant to O3;
- decision-time accessibility;
- source-level provenance.

No O1/O2 comparative analysis is authorized.

## 5. Frozen O3 definition

O3:

> partially set-up machine plus alternative tooling not currently in place.

Native class:

`alternative_tooling_with_setup`

Required tools:

`T-A`, `T-B`, `T-C`

Requires additional setup:

`true`

The definition itself must not be changed during execution.

## 6. RF-AC01 — evidence inventory authorization

Before classification, the executor must create and freeze an evidence inventory containing:

- source identifier;
- source version/date where available;
- exact relevant section/fact;
- provenance;
- whether the fact is explicitly decision-time;
- evidence hash where applicable.

No source may be added because it favors H-A or H-B after an apparent classification.

## 7. RF-AC02 — native-rule classification

Every proposed accessibility rule must be classified as exactly one of:

1. `EXPLICIT-NATIVE-RULE`;
2. `NATIVE-FACT + EXPLICIT-INFERENCE`;
3. `ANALYST-INTERPRETATION`.

Only categories 1 and 2 can support closure.

Category 3 forces **INDETERMINATE**.

A logical inference must be necessary rather than merely plausible.

## 8. RF-AC03 — material-condition completeness

The executor must first enumerate every material condition required to determine O3 accessibility.

Each condition must have a status:

- `RESOLVED_NATIVE`;
- `RESOLVED_NECESSARY_INFERENCE`;
- `UNRESOLVED`.

If any material condition is unresolved and would require analyst judgment to resolve, final classification is **INDETERMINATE**.

## 9. RF-AC04 — accessibility versus feasibility

The executor must not equate:

- technical possibility;
- existence of a tool;
- mention of an alternative;
- eventual procurement/availability;
- eventual success;
- engineering plausibility

with decision-time accessibility unless the native evidence explicitly establishes the required relation or it follows as a necessary inference.

## 10. Outcome blindness

No downstream outcome or performance information may be used for accessibility classification.

The following are prohibited:

- achieved performance;
- realized cost/time/quality;
- eventual success/failure;
- experimental result;
- post-decision setup state.

## 11. Synthetic fixture boundary

A synthetic fixture may be used only as a representation of independently established native facts.

Synthetic identifiers do not themselves constitute native evidence.

The executor may not manufacture missing inventory, resource, time, setup or accessibility facts.

## 12. Authorized execution procedure

1. Load the frozen O3 definition.
2. Load/freeze the admissible evidence inventory.
3. Enumerate material accessibility conditions.
4. Attach native provenance to each condition.
5. Classify each supporting rule as native rule, necessary inference, or analyst interpretation.
6. Attempt O3 membership closure.
7. Apply hard stops before resolving any missing condition by judgment.
8. Record unresolved conditions explicitly.
9. Classify O3 accessibility as `ACCESSIBLE`, `NOT_ACCESSIBLE`, or `INDETERMINATE` only where defensible.
10. Classify interpretation as H-A, H-B, or `UNRESOLVED`.
11. Produce hashes/provenance and immutable result output.

## 13. Required primary output

The local executor must emit:

- executor version;
- Python/runtime version;
- O3 definition;
- frozen evidence inventory;
- material-condition table;
- rule classification table;
- resolved/unresolved conditions;
- accessibility classification;
- H-A/H-B interpretation;
- hard-stop status;
- evidence hashes;
- execution/result hash where applicable.

## 14. Hard stops

Immediate **INDETERMINATE / STOP** if:

- an accessibility condition is invented;
- arbitrary threshold/bound/discretization is introduced;
- an analyst interpretation is promoted to native rule;
- downstream outcome is consulted;
- a missing fact is supplied by analyst judgment;
- technical feasibility is substituted for accessibility;
- the scope expands beyond O3;
- comparative IUT execution is attempted.

## 15. Result boundary

A corrective `ACCESSIBLE` result may justify a **new governance decision** for a corrected Stage-B comparative execution. It does not authorize that execution automatically.

A corrective `INDETERMINATE` result closes this corrective route and strengthens H-B as a bounded methodological interpretation.

A `NOT_ACCESSIBLE` result is admissible but does not by itself establish industrial utility.

## 16. Post-execution governance

After execution, the mandatory sequence is:

**Corrective Execution Result → Evidence→Claim Impact Assessment → propagation/current-state reconciliation → consistency closure.**

No scientific or industrial claim may be upgraded before these controls are completed.

## 17. Explicit exclusions

This authorization does not authorize:

- Stage-B comparative IUT;
- IUT-2 classification;
- baseline reconstruction;
- O1/O2 analysis;
- third-domain discovery;
- I-01 reopening;
- global T_acc reconstruction;
- causal inference;
- prediction;
- financial value;
- Stage C/D;
- external asset refresh.

## 18. Local execution artefact

Required next artefact:

`03_EXPERIMENTS/IUT-A-01/src/assess_o3_accessibility_closure_v01.py`

Execution convention:

`python .\03_EXPERIMENTS\IUT-A-01\src\assess_o3_accessibility_closure_v01.py`

The Python file must be generated and committed to GitHub before local execution.

## 19. Authorization conclusion

**ONE BOUNDED CORRECTIVE ACCESSIBILITY ASSESSMENT IS AUTHORIZED.**

The original Stage-B execution remains immutable and its IUT-2 classification remains not accepted. This authorization exists only to test whether the missing O3 accessibility condition can be grounded independently before any decision about further comparative execution.
