# TGCV — MT5 VSL Synthetic Minimum
## Contribution Assessment and Next Bottleneck 001

**Date:** 2026-09-18  
**Status:** CURRENT METHODOLOGICAL ASSESSMENT  
**Evidence basis:** VSL Synthetic Minimum v0.1, fixture/runtime audits, runner source/runtime integrity audit, Evidence-to-Claim Matrix v1.17.

## 1. What the synthetic experiment establishes

The experiment establishes a bounded implementation result:

`S' -> O -> V*`

can be specified, frozen and executed as an external valuation layer while the valuation functions receive neither accessibility, treatment, selected transformation nor transformation identity.

The experiment also demonstrates controlled contrasts:

- accessibility change without Value change (T2/NC2);
- specified synthetic accessibility/selection pathway with Value change (T3);
- Value change without accessibility change through an exogenous factor (T4).

This establishes methodological separability and operational reproducibility of the synthetic VSL interface.

## 2. What it does not establish

The experiment does not establish:

- that accessibility causes Value in real systems;
- that `Delta T_acc -> Delta V` is a general empirical relation;
- a universal Value construct or scalar;
- that improved Outcome is universally higher Value;
- a real-world valuation objective;
- cross-domain comparability;
- predictive validity;
- economic/monetary Value or ROI.

T3 is a synthetic pathway realization, not an independent causal estimate.

## 3. Contribution to MT5

The synthetic experiment resolves the **implementation-separation question** sufficiently for the current programme stage:

> A VSL can be represented as an external downstream layer without computationally collapsing Value into accessibility or transformation identity.

It therefore strengthens the methodological architecture identified after MT5-11e, but does not validate the valuation construct empirically.

The remaining MT5 uncertainty is no longer primarily whether such a layer can be implemented in principle. The critical unresolved issue is whether a VSL can be specified **independently and reproducibly for a non-synthetic domain**, with an independently justified valuation objective, outcome mapping, direction, reference frame and aggregation rule.

## 4. Next bottleneck

The next bottleneck is therefore:

**VSL-SPEC-01 — Independent Domain Valuation Specification Gate**

Question:

> Can an external VSL be specified, frozen and independently reproduced for a real or independently sourced domain without deriving its valuation objective or Value mapping from TGCV's accessibility/transformation variables?

## 5. Required controls

A candidate domain must provide, before execution:

1. independently justified reference entity;
2. explicit valuation objective;
3. explicit direction;
4. operational Outcome definition;
5. explicit Outcome → Value mapping;
6. reference/baseline frame;
7. aggregation rule if multiple outcomes exist;
8. missing-data rule;
9. provenance/versioning;
10. non-circularity proof;
11. independent reproducibility protocol.

The VSL must be frozen before observing the target experimental result.

## 6. Relationship to C09 and MT5-11e

This gate should not reopen C09 or reinterpret the C09/KGFS underdetermination.

The synthetic experiment is deliberately external to that unresolved domain. MT5-11e established that the frozen C09/KGFS evidence boundary does not uniquely determine `V*`; the synthetic experiment demonstrates how a separate specification can solve the underdetermination in an artificial domain.

The next test must therefore examine whether this specification discipline transfers to an independently justified non-synthetic domain.

## 7. Evidence classification

Current result:

**METHOD-LEVEL SUPPORT — BOUNDED**

It supports the architecture and operational separation of VSL, but not the empirical validity of a Value construct.

## 8. Governance disposition

No Core change.  
No C09 reopening.  
No claim-level upgrade.  
No new causal claim.

The next authorized activity is construction of the VSL-SPEC-01 gate and candidate-domain selection criteria. The gate must be designed before selecting or fitting a domain-specific valuation mapping.
