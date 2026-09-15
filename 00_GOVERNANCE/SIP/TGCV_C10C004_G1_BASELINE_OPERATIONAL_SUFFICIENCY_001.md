# C10C-004 — G1 Baseline Operational Sufficiency

**Gate:** G1 — Baseline Operational Sufficiency  
**Status:** PASS — BOUNDED OPERATIONAL SUFFICIENCY  
**Experiment:** C10C-004 — Morocco Microcredit RCT  
**Protocol:** TGCV_C10C004_STRUCTURAL_TACC_MODIFICATION_PROTOCOL_001  
**Role:** Operational gate record; no claim-level upgrade

## Result

G1 passes because the baseline data provide sufficient pre-intervention information to construct and freeze a candidate representation of household state, capabilities, resources and constraints before using endline data for the structural `T_acc` analysis.

## Evidence supporting the gate

- Dedicated baseline dataset: `Microcredit_BL_mini_anonym.dta`.
- Baseline sample: 4,465 household observations and 3,733 variables.
- Baseline precedes the randomized village-level treatment assignment.
- The baseline instrument covers relevant domains including assets and investment, agricultural and non-agricultural production, labour supply, consumption, education, health, credit and women's decision-making.
- The replication package contains a dedicated baseline outcome-construction do-file: `OutcomeConstruction_baseline_Oct2014.do`.
- Prior operational reconstruction established unique `ident` linkage in BL and EL, the BL→EL overlap of 4,118 households, and the matched-pair / demi-pair treatment structure required for subsequent reconstruction.
- Candidate baseline variable blocks include credit (`i*`), assets/resources (`c1_*`, `e1_*`), housing/infrastructure (`b*`), consumption (`h*`) and women's agency/capability (`j1_*`–`j13`).

## Interpretation boundary

This PASS does **not** establish:

- `T_acc` itself;
- `P_tau`;
- `Delta T_acc`;
- a treatment effect on transformational accessibility;
- mediation;
- downstream trajectory effects;
- value effects.

A change in an observed state variable is not, by itself, evidence of `Delta T_acc`. The next gates must define the transformation universe and admissibility independently of treatment effects and downstream outcomes.

## Freeze boundary

G1 authorizes progression to G2 only. The candidate transformation universe must be selected from baseline semantics, instrument structure and independently justified transformational domains, without using observed endline treatment differences to define the universe.

## Next gate

**G2 — Transformation-Universe Independence.**

Primary candidate domain for G2: baseline capability/agency and productive-transformation space represented principally by `j1_*`–`j13`, supplemented only by baseline resource and constraint variables required to make transformations operationally admissible.

## Governance effect

- Core: unchanged.
- RMA: unchanged.
- Claim matrix: unchanged.
- No causal or theoretical claim upgrade.
- Protocol remains frozen for operational reconstruction.
