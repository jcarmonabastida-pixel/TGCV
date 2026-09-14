# TGCV C09 — D5.2 Structural Accessibility Intervention Extension 001

**Date:** 2026-09-14
**Status:** ADOPTED — FORMAL METHODOLOGICAL EXTENSION
**Scope:** C09 D5.2/D5.3 and retrospective/future candidate evaluation
**Trigger:** KGFS Rural Banking reevaluation under the D5.2 Representation Correction 001

## 1. Purpose

The KGFS reevaluation identified a distinct admissible causal architecture that should be represented explicitly in C09: a randomized intervention may itself be the structural implementation of a change in the TGCV accessibility space.

In such cases, requiring an additional mediated pathway of the form

`Z -> M -> Y`

would be unnecessarily restrictive when `Z` directly implements the structural transition

`T_acc,0 -> T_acc,1`.

The relevant causal question is then the effect of the randomized structural accessibility intervention, not the effect of an endogenous downstream realization such as take-up.

## 2. New D5.2-S category

Introduce:

**D5.2-S — Structural Accessibility Intervention**

A candidate may satisfy the D5.2 causal-identification component through a direct randomized structural accessibility intervention when all of the following hold:

1. `Z` is independently randomized, or otherwise causally identified under a defensible intervention design;
2. `Z` implements, or is the experimentally assigned implementation of, a structural change from `T_acc,0` to `T_acc,1`;
3. `T_acc,0` and `T_acc,1` can be reconstructed or explicitly characterized independently of downstream outcomes and endogenous take-up;
4. the estimand is the causal effect of the structural accessibility intervention, typically an ITT effect when assignment is the intervention;
5. all material components of the assigned intervention are either represented within `T_acc` or explicitly bounded/assumption-labelled;
6. downstream adoption, use, investment, employment, income, wellbeing, or other realized responses are not substituted for `T_acc` itself.

## 3. Consequence for mediation requirements

When D5.2-S applies, an additional mediation identification step is **not required** merely to establish the causal effect of the structural accessibility intervention.

The valid architecture is:

`Z -> structural transition -> Delta T_acc -> downstream trajectory/Y`

where `Z` is the identified implementation of the structural transition.

This is distinct from a case where `Z` affects `T_acc` only indirectly through an unobserved or separately varying mediator. In the latter case, the existing D5.2 architectures remain applicable.

## 4. Boundary condition

D5.2-S does not permit relabelling the total treatment effect as a TGCV accessibility effect without examination.

The candidate must still audit whether the assigned intervention contains material components that cannot defensibly be represented as part of the accessibility-space change. Such components must be:

- included in the structural representation;
- separately randomized/measured and accounted for;
- bounded under explicit assumptions; or
- recorded as an unresolved direct pathway.

If a material residual pathway remains unresolved, the candidate cannot be promoted automatically to D5-A. It may instead qualify as D5-B (bounded/assumption-explicit) or D5-C (diagnostic only), according to the evidence.

## 5. KGFS application

The KGFS Rural Banking experiment is the motivating case. Its randomized early branch opening directly implemented an expansion of formal financial accessibility, including the service structure associated with the KGFS model. Downstream product take-up, investment, employment and income are treated as subsequent realizations/trajectories, not as definitions of `T_acc`.

Under this extension, KGFS currently qualifies as:

**D5.2-S = PASS provisional**

and, after the direct-channel audit, the present classification is:

**D5-B — BOUNDED / ASSUMPTION-EXPLICIT**

because the structural representation is strong but complete exclusion of every possible residual direct pathway has not been demonstrated to the D5-A standard.

This does not constitute a C09 claim upgrade by itself.

## 6. Methodological significance

The extension prevents C09 from conflating three different objects:

- structural accessibility (`T_acc`);
- realized use/adoption of accessible transformations; and
- downstream causal outcomes.

It also prevents C09 from imposing a mediation requirement where the experiment already randomizes the structural accessibility intervention itself.

## 7. Governance effect

This document is an adopted methodological extension of C09 D5.2. It does not upgrade C09, TGCV Core, RMA, Evidence→Claim Matrix or STATUS.

Future candidate screens and retrospective re-evaluations must apply D5.2-S where the design warrants it. Existing results are not rewritten automatically; only the relevant candidate may be re-evaluated under the new rule.

**Next authorized operation:** apply D5.2-S to El Salvador Rural Electrification, preserving the no-rerun rule and the existing evidence boundary.
