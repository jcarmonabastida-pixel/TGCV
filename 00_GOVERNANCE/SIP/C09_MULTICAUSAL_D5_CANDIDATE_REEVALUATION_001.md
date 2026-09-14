# TGCV C09 — Multicausal D5 Candidate Re-evaluation 001

**Date:** 2026-09-14
**Status:** COMPLETED — NO CANDIDATE UPGRADED; SEARCH TARGET REFINED
**Basis:** `TGCV_C09_DATASET_FIRST_DISCOVERY_PROTOCOL_005.md`
**Method:** retrospective methodological re-evaluation only; no experiment rerun and no historical result rewritten

## 1. Purpose

Re-evaluate the three strongest previously screened candidates under the revised D5 causal-contribution interpretation.

The question is no longer whether `T_acc` is the exclusive causal bridge to `Y`. The question is whether the existing design/data can identify or meaningfully bound a clearly defined causal contribution of `Delta T_acc` to `Y` while other determinants/pathways of `Y` are allowed to exist.

## 2. Candidate A — KGFS Rural Banking, Tamil Nadu

### Prior status
D0/D6-E/D1/D2/D3/D4 strong; prior D5-C because the branch expansion simultaneously changed access to multiple financial products and advisory services.

### Revised contribution estimand considered

`Effect of a structural increase in local formal-financial accessibility on downstream household/economic trajectories, with other determinants of Y retained as concurrent causes.`

### Assessment

The revised multicausal framing removes the incorrect requirement that financial accessibility explain the entire outcome. However, the existing KGFS design still does not isolate the contribution of `Delta T_acc` from the specific components bundled by the branch expansion: credit, savings, insurance and financial advice.

The randomized branch-opening exposure identifies the effect of the **KGFS access bundle**, but not a separable contribution of the abstract structural accessibility change itself.

A causal-contribution estimand for `Delta T_acc` therefore remains underidentified unless additional design/data allow component-specific variation or a defensible interventional mediation estimand.

**Revised D5: D5-C / DIAGNOSTIC ONLY.**

### What would change the classification

A design/data layer that separately varies or measures the accessibility-producing component from product/advice components, or a defensible interventional mediation strategy with sufficient mediator/outcome-confounder measurement.

## 3. Candidate B — El Salvador Rural Electrification

### Prior status
D0/D6-E/D1/D2/D3/D4 strong; prior D5-C.

### Revised contribution estimand considered

`Causal contribution of the induced structural transition to electricity access to downstream labour, income, time-use and welfare trajectories, allowing other determinants to affect Y.`

### Assessment

The revised framing correctly allows labour, income, household characteristics and other mechanisms to affect the outcomes simultaneously.

However, the randomized voucher changes the cost of connection as well as the probability of connection. The design therefore does not provide a clean exclusion argument that voucher assignment affects downstream outcomes only through the structural access transition. The first stage is strong, but the existing evidence does not separately identify the accessibility contribution from the direct economic/cost channel of the voucher.

A mediator diagnostic or IV/Wald ratio would remain diagnostic unless an explicit exclusion/interventional-mediation argument is supplied.

**Revised D5: D5-C / DIAGNOSTIC ONLY.**

### What would change the classification

A valid design-based exclusion restriction, a separately randomized access-producing component, or sufficient mediator/confounder data for an explicitly identified interventional contribution estimand.

## 4. Candidate C — Peru Domestic Internet

### Prior status
D0/D6-E/D1/D2/D3/D4 strong; prior D5-C.

### Revised contribution estimand considered

`Incremental causal contribution of increased structural household Internet accessibility to subsequent digital/educational trajectories, allowing other causes of Y.`

### Assessment

The multicausal correction removes any requirement that Internet access explain all educational/cognitive outcomes. The second-stage randomization remains valuable because Internet access is separately randomized among laptop recipients.

The remaining problem is treatment composition: the Internet treatment also included instructional/tutorial material on using online resources. Therefore the randomized treatment does not cleanly vary `Delta T_acc(internet)` while holding all other treatment components fixed.

The Laptop-Only arm isolates the incremental package of Internet treatment, but not a pure accessibility-only contribution.

**Revised D5: D5-C / DIAGNOSTIC ONLY.**

### What would change the classification

A pure Internet-access arm separated from tutorial/training content, or an identification strategy that can separately identify the accessibility component under explicit assumptions.

## 5. Comparative conclusion

| Candidate | Revised D5 | Main remaining blocker |
|---|---|---|
| KGFS Rural Banking | D5-C | bundled access/products/advice prevent separable `Delta T_acc` contribution |
| El Salvador Rural Electrification | D5-C | voucher cost effect/direct pathway prevents clean exclusion |
| Peru Domestic Internet | D5-C | Internet access bundled with tutorial/manual component |

### Overall conclusion

**None of the three candidates reaches D5-A or D5-B under the revised contribution estimand.**

This is not evidence against the multicausal correction. Instead, it reveals a more precise search requirement:

> The next candidate must permit estimation of a contribution of `Delta T_acc` while other determinants of `Y` remain present, and must contain a design or measurement layer that separates the accessibility component from bundled treatment components.

The revised D5 therefore appears **more realistic but still falsifiable**. It eliminates the unnecessary monocausal requirement without turning any of the previously rejected candidates into automatic passes.

## 6. TGCV applicability implication

The re-evaluation supports the methodological rationale for the revised D5: real-world outcomes need not be monocausal, and TGCV need not claim that `Delta T_acc` explains total value. Its potential empirical role is to identify the causal contribution of transformation-space expansion/contraction within a multicausal system.

No TGCV claim is upgraded by this record.

## 7. Next discovery priority

Search for a real-world case with:

`Z_access → Delta T_acc`

plus independently varying/measurable competing mechanisms, such that the contribution estimand can be identified or bounded.

Highest-priority signatures:

1. factorial randomization of accessibility component vs complementary component;
2. multiple randomized accessibility intensities;
3. separate infrastructure/access intervention and training/information arm;
4. pure access arm plus access+complementary-treatment arm;
5. interventional mediation with rich baseline mediator-outcome confounders;
6. partial-identification bounds for the accessibility contribution.

No candidate execution is authorized by this record.
