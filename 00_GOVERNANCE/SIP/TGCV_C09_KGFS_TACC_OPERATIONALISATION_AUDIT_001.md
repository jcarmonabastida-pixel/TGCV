# TGCV C09 — KGFS T_acc Operationalisation Audit 001

**Date:** 2026-09-14
**Status:** AUDITED — REPRESENTATION SUFFICIENT FOR D5.2-S; D5-A CLOSURE PENDING FINAL REPRODUCIBILITY CHECK
**Candidate:** KGFS Rural Banking — Rural Banks Can Reduce Poverty: Experimental Evidence from 870 Indian Villages
**Scope:** D5.2-S representation and operationalisation only

## 1. Source boundary

The Yale ISPS public archive identifies the study as a field experiment with household-level public data (4,184 households), randomized by pairing comparable service areas and randomizing which service area receives the KGFS branch first. The archive describes the treatment as expansion of banking services.

The public User Reference states that the treatment is the random expansion of bank infrastructure across rural villages. It identifies 101 viable service areas, 50 matched pairs (one triplet), and randomization at service-area level. Baseline surveys preceded branch opening; endline surveys followed 18–24 months later.

## 2. Structural representation

The TGCV representation is frozen conceptually as:

`T_acc,0 = financial transformations structurally accessible before KGFS branch opening`

`T_acc,1 = T_acc,0 + structural financial-access capabilities introduced by KGFS`

`Delta T_acc = T_acc,1 - T_acc,0`

The KGFS intervention documentation specifies that the model adds:

- formal loans;
- formal savings;
- formal insurance;
- tailored financial advice delivered through local village branches.

These are treated as components of the structural accessibility intervention, not as downstream mediator variables.

## 3. Variables that must NOT define T_acc

The following are downstream realizations or outcomes and are excluded from the definition of T_acc:

- loan take-up;
- savings take-up;
- insurance take-up;
- investment;
- employment;
- business activity;
- income;
- consumption;
- poverty/wellbeing;
- health or empowerment outcomes.

The User Reference explicitly identifies loan, savings and insurance behaviour as first-stage responses and lists income, occupational choice, consumption and other wellbeing measures as outcomes.

## 4. Observable structural linkage

The public data provide:

- `hhid` as household identifier;
- `cont_s_id` as a location identifier capable of identifying district/block/gram panchayat/village and treatment/control village status;
- baseline and endline timing;
- the public intervention description and service-area randomization rule.

This supports an auditable linkage:

`household -> village/location -> service area -> randomized early-branch status -> pre/post structural exposure`

The structural treatment is therefore defined independently of household take-up and outcome variables.

## 5. D5.2-S assessment

**Representation component: PASS.**

The absence of a native variable named `T_acc` or `Delta T_acc` is not a failure. The structural state transition can be reconstructed from the documented intervention and randomized service-area exposure, with the public location/treatment linkage providing the unit assignment.

**Causal component: PASS under D5.2-S architecture.**

The experiment randomizes which service area receives the KGFS branch first. The assigned intervention is itself the implementation of the structural accessibility expansion. Therefore an additional endogenous mediation requirement of the form `Z -> take-up -> Y` is not required to identify the causal effect of the structural intervention.

## 6. Remaining closure condition

D5-A should not be declared until the final reproducibility check verifies the exact public-data variable mapping and reconstruction procedure at the analysis unit/time level.

The remaining task is therefore procedural rather than conceptual:

1. map the treatment/service-area identifiers to exact public variable names;
2. freeze the construction rule for `T_acc,0`, `T_acc,1` and `Delta T_acc`;
3. verify that no downstream take-up/outcome variable enters the construction;
4. record source/version/hash information for the public files used;
5. archive the resulting operationalisation record.

No new experiment is required.

## 7. Current gate state

`D5.0 PASS`

`D5.1 PASS`

`D5.2-S PASS`

`D5.3 PASS provisional — structural components incorporated; final variable-level audit pending`

`D5.4 -> D5-A candidate, not yet final`

This document does not upgrade C09, TGCV Core, RMA, Evidence→Claim Matrix or STATUS.
