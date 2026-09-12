# TGCV — C09 Domain / Identification Gate 001

**Status:** `OPEN — DESIGN GATE / TR-132 APPLIES / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Precondition:** `TGCV_C09_CAUSAL_DESIGN_SPECIFICATION_001.md`
**Sufficiency gate:** `TGCV_C09_TR132_SUFFICIENCY_GATE_001.md`

## 1. Decision objective

Select, or explicitly reject, a concrete domain and unit of analysis for a future C09 causal test.

The gate is passed only if a candidate domain permits an independently identifiable accessibility intervention and a defensible counterfactual without encoding the subsequent trajectory in the treatment, **and** its bounded operational representation passes TR-132.

## 2. Mandatory candidate requirements

A candidate domain must provide, before any execution authorization:

1. a uniquely identifiable decision-time unit;
2. reconstructible `S0` and `C0`;
3. a finite or operationally bounded candidate transformation universe `U*` within the declared C09 scope;
4. a frozen accessibility rule `L` allowing reconstruction of `T_acc,0` and `T_acc,1` **within `U*`**;
5. an intervention that can change accessibility conditions independently of the target trajectory;
6. a credible treatment/control or counterfactual identification strategy;
7. an independently observable subsequent trajectory over a fixed horizon;
8. sufficient temporal resolution to separate pre-treatment accessibility from post-treatment trajectory;
9. provenance sufficient for independent reconstruction of the bounded representation;
10. no requirement to infer missing pre-treatment variables from post-treatment outcomes;
11. **TR-132 PASS**, establishing that omitted transformations outside `U*` cannot create an uncontrolled alternative pathway capable of changing the declared causal conclusion.

Complete system-wide `T_acc` reconstruction is **not** a mandatory requirement.

## 3. Candidate-domain screening

### Candidate A — SWIM

**Disposition:** `REJECT FOR C09 CAUSAL EXECUTION`

Reason: SWIM provides bounded observed association between accessibility changes and subsequent trajectory, but the existing reconstruction does not provide an independently controlled accessibility intervention/counterfactual suitable for causal identification. TR-132 does not repair the missing intervention identification.

### Candidate B — RUST-DYN-2

**Disposition:** `REJECT FOR C09 CAUSAL EXECUTION`

Reason: RUST-DYN-2 provides bounded structural empirical evidence distinguishing `ΔT_acc` from potential one-step Reach. Its operational population is observational/historical and was not constructed around an independently assigned accessibility treatment and counterfactual trajectory outcome. TR-132 does not repair the causal-identification deficiency.

### Candidate C — existing industrial cases

**Disposition:** `NOT ADMISSIBLE BY DEFAULT`

The existing AWS/industrial cases demonstrate governed reconstruction and, in one case, functional recovery. They do not by themselves provide a predeclared causal intervention in accessibility with an independently identified counterfactual trajectory. TR-132 may be applied only if a separate audit establishes a sufficient bounded causal representation.

### Candidate D — historical longitudinal operational domain

**Disposition:** `CANDIDATE CLASS — REQUIRES TR-132 SUFFICIENCY AUDIT`

A longitudinal domain with repeated reconstructible states and externally determined changes in an accessibility condition remains the preferred candidate class. The relevant question is now whether a **bounded** representation is sufficient for the declared causal contrast, not whether the entire system-wide transformation space can be reconstructed.

## 4. Retrospective review rule

Historical candidate audits closed solely because of complete-system/public-`T_acc` requirements are eligible for a new governed TR-132 retrospective review. Their original audit records remain immutable historical records; retrospective review does not erase or rewrite those dispositions.

The retrospective review asks only:

`Can the declared C09 causal contrast be identified from a frozen bounded U* without an uncontrolled omitted transformation pathway?`

## 5. Identification rule

A candidate cannot pass merely because accessibility and trajectory are correlated. The gate requires a defensible mapping from intervention assignment to accessibility change and from accessibility change to subsequent trajectory, while excluding direct treatment pathways that bypass accessibility.

Preferred identification hierarchy:

`randomized intervention > controlled matched/quasi-experimental intervention > credible natural experiment > observational association`

The last category is insufficient for C09.

## 6. Stop conditions

Reject the candidate if any of the following is true:

- no independently manipulable or identifiable accessibility condition exists;
- treatment assignment is determined by the future trajectory;
- trajectory information is needed to classify pre-treatment accessibility;
- intervention directly forces the trajectory;
- no credible counterfactual can be reconstructed;
- temporal ordering cannot be established;
- the bounded `U*` omits a transformation class capable of changing the causal conclusion;
- `T_acc,0/T_acc,1` cannot be distinguished within `U*`;
- the trajectory endpoint depends on omitted transformations in an uncontrolled way;
- the candidate depends on post-treatment or outcome leakage;
- causal identification relies on an untestable narrative unsupported by observable design conditions.

## 7. Current gate decision

**Decision:** `NO CANDIDATE ADMITTED FOR EXECUTION`

**Retrospective TR-132 review:** `OPEN`

This is not a scientific failure of C09. It is a pre-execution identification/sufficiency gate remaining open.

## 8. Execution boundary

`EXECUTION AUTHORIZATION = NONE`

No dataset acquisition, external intervention, AWS mutation, SWIM rerun, RUST-DYN-2 rerun, or causal outcome collection is authorized by this gate.

## 9. Next operation

Perform the **controlled retrospective TR-132 review of the strongest previously rejected C09 candidates**, beginning with candidates whose original blocker was representation completeness rather than causal assignment: MTO, Chicago voucher lottery, NYCHANS, King County free transit, naturalization fee voucher, OHIE, and school-choice lottery.
