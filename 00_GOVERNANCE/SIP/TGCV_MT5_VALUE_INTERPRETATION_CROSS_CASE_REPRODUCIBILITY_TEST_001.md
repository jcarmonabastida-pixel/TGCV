# TGCV — MT5 Value Interpretation Cross-Case Reproducibility Test 001

**Date:** 2026-09-17  
**Status:** `CLOSED — BOUNDED CROSS-CASE METHODOLOGICAL REPRODUCIBILITY`  
**Programme:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos

## 1. Objective

Test whether the Value Interpretation Layer identified in MT5-07 and partially instantiated in MT5-08 survives a materially different substantive domain, without defining a universal substantive Value construct and without contaminating `T_acc`.

The tested architecture is:

`O → {Reference, Objective, Direction, Mapping, Reference frame, Measurement rule} → V*`

The test concerns reproducibility of the **methodological interpretation structure**, not equivalence of substantive Value across domains.

## 2. Cases

Primary comparison:

- **C09 / KGFS:** randomized structural financial accessibility followed by downstream longitudinal financial/economic and welfare-related outcomes.
- **C10C002:** bounded structural urban-accessibility reconstruction followed by independently defined downstream property-value outcomes where observed.

C10C002 provides a materially different substantive domain while preserving the TGCV separation between reconstructed accessibility and downstream outcome variables. Its closed audit reconstructs `T_acc,0*`, `T_acc,1*`, and `ΔT_acc*` independently of value variables; property-value endpoint fields are observed for only 138 of 342 polygons, leaving an endpoint-selection/attrition evidence gap.

## 3. Interpretation-layer comparison

| Field | C09 / KGFS | C10C002 | Cross-case result |
|---|---|---|---|
| Outcome `O` downstream | PASS | PASS | REPRODUCIBLE |
| Reference entity | PARTIAL | PARTIAL | NOT FULLY SPECIFIED |
| Valuation objective | PARTIAL | PARTIAL | NOT FULLY SPECIFIED |
| Direction | PARTIAL | PARTIAL | NOT FULLY SPECIFIED |
| Outcome-to-Value mapping | PARTIAL | PARTIAL | NOT FULLY SPECIFIED |
| Reference frame / horizon | PASS | PASS | REPRODUCIBLE |
| Measurement / provenance | PASS | PARTIAL | DOMAIN-DEPENDENT |
| Non-circularity | PASS | PASS | REPRODUCIBLE |
| Domain-boundedness | PASS | PASS | REPRODUCIBLE |

## 4. Result

**MT5-09: `CLOSED — BOUNDED CROSS-CASE METHODOLOGICAL REPRODUCIBILITY`.**

The same interpretation-layer structure remains applicable when the substantive domain changes. What survives cross-case is the **information architecture required to interpret an independently measured downstream outcome as a candidate Value endpoint**.

What does not survive as an invariant is the substantive content of Value itself: poverty/wellbeing and property-value outcomes are not treated as equivalent TGCV Value constructs.

## 5. Limitation

The test does **not** establish a fully reproducible `V*` in either case. Reference entity, valuation objective, direction rule, and the explicit `O → V*` mapping remain partially specified. Therefore the result is methodological reproducibility of the interpretation layer, not operationalization of Value.

The C10C002 endpoint attrition gap further prevents treating the property-value pathway as a complete empirical Value endpoint reconstruction.

## 6. Governance disposition

No Core modification.  
No RMA modification.  
No Evidence→Claim Matrix upgrade.  
No claim upgrade.  
No causal claim `ΔT_acc → ΔV`.  
M9 remains open.

## 7. Next authorized movement

**MT5-10 — Value Interpretation Sufficiency Gate.**

Question: determine whether the identified interpretation fields are merely necessary conditions or can constitute a sufficient domain-bounded specification for producing a reproducible `V*` without hidden normative assumptions or contamination of `T_acc`.
