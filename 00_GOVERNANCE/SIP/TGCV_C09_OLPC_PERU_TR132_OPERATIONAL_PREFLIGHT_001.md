# TGCV — C09 OLPC Peru TR-132 Operational Preflight 001

**Status:** `COMPLETED — CANDIDATE PROVISIONALLY ADMITTED TO TR-132 OPERATIONAL AUDIT / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-14
**Candidate:** Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo — *One Laptop per Child at Home: Short-Term Impacts from a Randomized Experiment in Peru*
**Domain:** Home computer access / educational transformations
**Data package:** openICPSR 113587, Version V2 (2024-03-28)
**Publication DOI:** 10.1257/app.20130267
**Replication DOI:** 10.3886/E113587V2

## 1. Search decision

This candidate was identified in a new targeted real-world search. It is not part of the previously closed C09 candidate sequence.

It is materially attractive because the intervention itself is explicitly reported to increase access to home computers, the assignment is randomized, the observation unit is the student, follow-up outcomes are available, and a public replication package exists.

## 2. TR-132 operational screen

| Gate | Status | Evidence / remaining condition |
|---|---|---|
| P1 — identifiable unit | **PASS** | openICPSR identifies Student as unit of observation. |
| P2 — baseline and assignment reconstructibility | **PASS DESIGN / DATA PACKAGE CONFIRMED** | Randomized controlled trial; approximately 1,000 primary-school children in Lima; public V2 replication package contains original, intermediate, final, instruments and results materials. |
| P3 — intervention changes accessibility | **PASS CONCEPTUALLY** | Treatment provided an OLPC XO laptop for home use and the publication reports increased access and use of home computers. |
| P4 — bounded `U*` and `T_acc,0/T_acc,1` | **CONDITIONAL — CRITICAL NEXT CHECK** | A bounded transformation universe can plausibly be defined around home-computer-enabled educational/computational activities. Exact unit-level variables and the admissible construction of `T_acc,0/T_acc,1` must be verified directly from the public replication files before execution admission. |
| P5 — independent trajectory / endpoint | **PASS DESIGN** | Follow-up outcomes include XO proficiency, academic effort, academic achievement and cognitive skills; publication reports post-intervention measurement. |
| P6 — treatment / counterfactual | **PASS DESIGN** | Randomized treatment assignment supplies a credible counterfactual. |
| P7 — public independent reproducibility | **PASS PROVISIONALLY** | openICPSR V2 is publicly listed as experimental/survey data with Student as observation unit and includes multiple data stages plus README/materials. Exact raw-variable accessibility still requires local package inspection. |
| P8 — C09 execution | **NOT AUTHORIZED** | TR-132 operational sufficiency is not yet closed; no causal execution is authorized by this preflight. |

## 3. Candidate operationalization under TGCV

### Unit

Student `u_i` enrolled in the randomized Lima primary-school sample.

### Intervention

`Z_i = 1`: student randomized to receive an OLPC XO laptop for home use.

`Z_i = 0`: student randomized to the comparison condition without the home laptop.

### Bounded transformation universe `U*`

The admissible universe must be restricted before outcome analysis to transformations directly relevant to the declared causal question, for example a prespecified family of home-computer-enabled educational/computational activities observable in the study instruments/logs. The preflight does **not** assume that the entire student's activity space is observable.

### Accessibility profiles

`T_acc,0`: transformations in the declared `U*` accessible to the student under the control condition, given frozen baseline state/context and pre-treatment resources.

`T_acc,1`: transformations in the same `U*` accessible after provision of the home laptop, holding the frozen baseline state/context fixed except for the accessibility intervention.

The decisive next check is whether the public unit-level package contains enough pre-treatment resource/access information and intervention-linked information to construct these two profiles without using post-treatment realized activity as a proxy for accessibility.

### Outcome / trajectory

Primary candidate endpoints should be selected before execution from post-treatment measures that are not themselves definitions of `T_acc`, with a fixed follow-up horizon. The publication provides post-intervention measures of digital proficiency, academic effort, academic achievement and cognitive skills.

## 4. Information firewall

The following substitutions are prohibited unless independently justified as part of the frozen operational definition:

- realized laptop use as `T_acc`;
- post-treatment computer activity as the accessibility state;
- outcome variables as components of `T_acc`;
- treatment assignment alone as the transformation-space representation;
- aggregate treatment/control statistics in place of unit-level accessibility data.

## 5. Why this candidate is materially better than the closed candidates

The candidate directly targets the outstanding C09 gap: a real intervention that changes an explicitly observable access condition, with randomized assignment and a public unit-level replication package. The public package is a materially different provenance situation from the previously rejected cases where unit-level `T_acc,0/T_acc,1` data were unavailable.

This does **not** establish that the candidate passes TR-132. The remaining decisive question is the exact public-data construction of bounded `U*`, `T_acc,0` and `T_acc,1`.

## 6. Decision

**CANDIDATE = PROVISIONALLY ADMITTED TO TARGETED TR-132 OPERATIONAL AUDIT.**

**EXECUTION = NOT AUTHORIZED.**

**NEXT REQUIRED OPERATION = INSPECT THE PUBLIC V2 REPLICATION PACKAGE AND FREEZE THE BOUNDED `U*`, `T_acc,0`, `T_acc,1`, INTERVENTION, OUTCOME AND HORIZON.**

If the required unit-level accessibility variables cannot be reconstructed without leakage or proxy substitution, the candidate must be closed immediately and the search must continue with a genuinely new case. If they can, the candidate can proceed to a full TR-132 sufficiency audit.

## 7. External evidence

1. Beuermann et al. (2015), American Economic Journal: Applied Economics, documents the randomized trial and reports that provision of approximately 1,000 XO laptops for home use increased access and use of home computers. DOI 10.1257/app.20130267.
2. openICPSR replication package 113587 V2, released 2024-03-28, publicly lists experimental/survey data, Student as the observation unit, and data folders including Originales, Intermedias, Finales, Instrumentos and Resultados.

No causal claim or C09 matrix/RMA/Core upgrade follows from this preflight.
