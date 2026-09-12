# TGCV — C09 Domain / Identification Gate 001

**Status:** `OPEN — DESIGN GATE / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-12
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Precondition:** `TGCV_C09_CAUSAL_DESIGN_SPECIFICATION_001.md`

## 1. Decision objective

Select, or explicitly reject, a concrete domain and unit of analysis for a future C09 causal test.

The gate is passed only if a candidate domain permits an independently identifiable accessibility intervention and a defensible counterfactual without encoding the subsequent trajectory in the treatment.

## 2. Mandatory candidate requirements

A candidate domain must provide, before any execution authorization:

1. a uniquely identifiable decision-time unit;
2. reconstructible `S0` and `C0`;
3. a finite or operationally bounded candidate transformation universe;
4. a frozen accessibility rule `L` allowing reconstruction of `T_acc,0`;
5. an intervention that can change accessibility conditions independently of the target trajectory;
6. a credible treatment/control or counterfactual identification strategy;
7. an independently observable subsequent trajectory over a fixed horizon;
8. sufficient temporal resolution to separate pre-treatment accessibility from post-treatment trajectory;
9. provenance sufficient for independent reconstruction;
10. no requirement to infer missing pre-treatment variables from post-treatment outcomes.

## 3. Candidate-domain screening

### Candidate A — SWIM

**Disposition:** `REJECT FOR C09 CAUSAL EXECUTION`

Reason: SWIM provides bounded observed association between accessibility changes and subsequent trajectory, but the existing reconstruction does not provide an independently controlled accessibility intervention/counterfactual suitable for causal identification. Reusing it for C09 would convert association into causality without the required design.

### Candidate B — RUST-DYN-2

**Disposition:** `REJECT FOR C09 CAUSAL EXECUTION`

Reason: RUST-DYN-2 provides bounded structural empirical evidence distinguishing `ΔT_acc` from potential one-step Reach. Its operational population is observational/historical and was not constructed around an independently assigned accessibility treatment and counterfactual trajectory outcome. Re-running it would not solve the causal-identification deficiency.

### Candidate C — existing industrial cases

**Disposition:** `NOT ADMISSIBLE BY DEFAULT`

The existing AWS/industrial cases demonstrate governed reconstruction and, in one case, functional recovery. They do not by themselves provide a predeclared causal intervention in accessibility with an independently identified counterfactual trajectory. An industrial case may only be admitted if a separate pre-execution audit establishes all mandatory requirements.

### Candidate D — historical longitudinal operational domain

**Disposition:** `CANDIDATE CLASS — REQUIRES PRE-EXECUTION FEASIBILITY AUDIT`

A longitudinal domain with repeated reconstructible states and externally determined changes in an accessibility condition is the preferred candidate class. The required next task is not execution but evidence-feasibility assessment: identify whether the intervention is plausibly exogenous/controlled, whether `T_acc` can be reconstructed before the intervention, and whether subsequent trajectories can be observed independently.

## 4. Identification rule

A candidate cannot pass merely because accessibility and trajectory are correlated. The gate requires a defensible mapping from intervention assignment to accessibility change and from accessibility change to subsequent trajectory, while excluding direct treatment pathways that bypass accessibility.

Preferred identification hierarchy:

`randomized intervention > controlled matched/quasi-experimental intervention > credible natural experiment > observational association`

The last category is insufficient for C09.

## 5. Stop conditions

Reject the candidate if any of the following is true:

- no independently manipulable or identifiable accessibility condition exists;
- treatment assignment is determined by the future trajectory;
- trajectory information is needed to classify pre-treatment accessibility;
- intervention directly forces the trajectory;
- no credible counterfactual can be reconstructed;
- temporal ordering cannot be established;
- the candidate requires reopening a closed experiment solely to obtain causal evidence;
- the candidate depends on post-treatment or outcome leakage;
- causal identification relies on an untestable narrative unsupported by observable design conditions.

## 6. Current gate decision

**Decision:** `NO CANDIDATE ADMITTED FOR EXECUTION`

**Preferred next candidate class:** historical longitudinal operational domain with an independently determined accessibility intervention and reconstructible subsequent trajectory.

This is not a scientific failure of C09. It is a pre-execution identification gate remaining open.

## 7. Execution boundary

`EXECUTION AUTHORIZATION = NONE`

No dataset acquisition, external intervention, AWS mutation, SWIM rerun, RUST-DYN-2 rerun, or causal outcome collection is authorized by this gate.

## 8. Next operation

Perform a **C09 historical-longitudinal feasibility audit** using the existing scientific asset registry and previously registered historical/longitudinal domain assets. The audit must determine whether a concrete admissible intervention/counterfactual can actually be reconstructed before any domain is selected for execution.
