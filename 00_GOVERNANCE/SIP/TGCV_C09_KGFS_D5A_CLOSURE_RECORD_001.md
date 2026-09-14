# TGCV C09 — KGFS D5-A Closure Record 001

**Date:** 2026-09-14
**Status:** CLOSED — D5-A IDENTIFIED CONTRIBUTION
**Candidate:** KGFS Rural Banking
**Scope:** C09 D5 causal gate

## 1. Closure basis

The KGFS public User Reference defines the intervention as a cluster randomized controlled trial of expanding financial access. The treatment is the random expansion of bank infrastructure across rural villages. KGFS offers formal loans, savings and insurance, with tailored financial advice through local village branches.

The study identified 101 viable service areas, formed 50 matched pairs (one triplet), and randomized which service area received the KGFS branch first. Randomization is therefore at service-area level. Baseline surveys preceded branch opening and endline surveys followed 18–24 months later.

The Yale archive independently records the design as a field experiment, unit of observation as household, sample size 4,184, randomization by paired service areas, and treatment as expansion of banking services.

The independent evaluation report explicitly describes the randomized treatment as increased access to formal finance through opening a KGFS branch in a service area and defines the service-area treatment dummy as the ITT intervention.

## 2. TGCV representation

For C09, the intervention is represented as a structural accessibility transition:

`T_acc,0 = financial transformations structurally accessible before KGFS branch opening`

`T_acc,1 = T_acc,0 + KGFS financial-access capabilities introduced by the branch model`

`Delta T_acc = T_acc,1 - T_acc,0`

The KGFS components documented by the User Reference are:

- formal loans;
- formal savings;
- formal insurance;
- tailored financial advice through local village branches.

The representation is defined independently of downstream realization.

## 3. Exclusion of downstream variables

Loan take-up, savings take-up, insurance take-up, investment, employment, income, consumption, poverty, wellbeing, health, empowerment and networks are not used to define `T_acc`. The User Reference explicitly separates the intervention from first-stage behavioural responses and downstream wellbeing outcomes.

## 4. Variable-level reproducibility assessment

The public dataset supplies `hhid` as the household identifier and `cont_s_id` as a location identifier that can identify district, block, gram panchayat and village and can identify whether a respondent is in a treated or control village. The dataset is harmonized by survey round, and the documented timeline distinguishes baseline and endline observations.

The evaluation methodology independently defines the service-area treatment indicator `T_k` and states that its coefficient is the ITT effect. Thus the causal treatment assignment is not inferred from downstream outcomes or take-up.

For TGCV operationalisation, the exact numeric contents of the accessible transformation set need not be encoded as a native dataset variable. The intervention documentation supplies the structural state definition, while the public location/treatment linkage supplies the experimental exposure and the survey timing supplies the transition boundary. This satisfies the corrected D5.2 representation rule.

## 5. Causal identification

The causal architecture is D5.2-S — Structural Accessibility Intervention:

`randomized branch assignment -> structural financial-access expansion -> Delta T_acc -> downstream trajectory/Y`

Because the randomized assignment implements the structural accessibility intervention itself, no additional endogenous mediation requirement through product take-up is necessary to identify the causal effect of the structural intervention.

The ITT effect is therefore interpretable as the causal effect of the assigned structural accessibility expansion represented by `Delta T_acc`, subject to the explicit TGCV operationalisation above.

## 6. Gate decision

`D5.0 PASS`

`D5.1 PASS`

`D5.2-S PASS`

`D5.3 PASS`

`D5.4 D5-A — IDENTIFIED CONTRIBUTION`

**KGFS therefore closes the C09 D5 causal gate as D5-A.**

This is a candidate-level scientific result. It does not by itself upgrade the global C09 claim, TGCV Core, RMA, Evidence→Claim Matrix or STATUS. Those upgrades require their respective consolidation gates.

## 7. Next authorized operation

Do not reopen KGFS during candidate discovery. Preserve this closure as canonical evidence and proceed to the next C09 consolidation step: formulate the KGFS evidence-to-C09 claim bridge and test whether the identified contribution establishes the required causal accessibility-to-trajectory relation rather than merely a treatment/outcome effect.
