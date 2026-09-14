# TGCV — C10-C Candidate Discovery Round 001

**Status:** DOCUMENTARY SCREENING COMPLETE — NO EMPIRICAL EXECUTION
**Date:** 2026-09-14
**Gate:** `TGCV_C10_C_CANDIDATE_DISCOVERY_DATASET_FIRST_ADMISSION_GATE_001.md`
**Design contract:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`

## 1. Scope

This round performs documentary candidate discovery and candidate-specific admission screening only. No dataset was downloaded, no `T_acc` was reconstructed, and no causal estimate was executed.

## 2. Candidate C10C-001 — Exporting and Firm Performance: Randomized Experiment, Egypt

**Source:** Atkin, Khandelwal & Osman, *Exporting and Firm Performance: Evidence from a Randomized Experiment*, QJE 2017. J-PAL identifies 219 eligible rug producers, 74 randomized to treatment and 145 comparison; treatment consisted of an opportunity to fill export orders, with repeated surveys over 2011–2014 and profit/productivity/quality outcomes. Data are linked from J-PAL to Harvard Dataverse. citeturn2view2turn0search0

### D1 — Study identity/provenance
**PASS.** Peer-reviewed study, stable DOI, AEA RCT registration, named researchers and public-data route. citeturn2view2

### D2 — Causal design
**PASS — strong.** Random assignment generated exogenous variation in the opportunity to export. citeturn2view2turn0search0

### D3 — Structural accessibility transition
**B — precise operational gap.** The intervention is not merely observed exporting: firms were randomly given an opportunity to fill foreign orders, while Hamis Carpets and buyers established prices, delivery timing and product specifications. This supports a candidate change in accessible export-related transformations through the treatment/context condition. However, admission requires defining an explicit transformation universe `U_τ` and predicate `P_τ(S,C,L)` from the documented firm/intervention state, rather than using treatment assignment or export take-up as a proxy for `T_acc`. The fact that subsequent orders could depend on performance makes this distinction essential. citeturn2view2

### D4 — Independent value endpoint
**PASS — strong candidate.** Monthly firm profit is a directly measured economic endpoint and is not definitionally identical to treatment or accessibility. J-PAL reports a 26% ITT effect on monthly profits. citeturn2view2

### D5 — Counterfactual
**PASS — strong.** Randomized treatment/comparison assignment supplies the basic counterfactual. citeturn2view2

### D6 — Downstream pathway
**B — evidence gap.** The documented sequence contains opportunity to export → actual production/exporting → learning/quality/productivity → profit. The C10-C audit must preserve these distinctions rather than treating exporting itself as `ΔT_acc`. citeturn2view2

### D7 — Competing mechanisms
**B — material but auditable.** Take-up and subsequent orders depend partly on firm performance/buyer interest; learning, product quality, productivity and prices are downstream mechanisms. These are analytically useful but must not be absorbed into accessibility. citeturn2view2

### D8 — Reproducibility/provenance
**A/B — strong route, file-level verification pending.** J-PAL provides a Harvard Dataverse data route and the study has detailed survey documentation. Exact files, variable dictionary, treatment fields and derived-variable provenance must still be verified before empirical admission. citeturn2view2

**Classification: B — PROMISING / EVIDENCE GAP.**
**Priority: HIGH.**

## 3. Candidate C10C-002 — Neighborhood Impacts of Local Infrastructure Investment: Urban Mexico

**Source:** McIntosh, Alegría, Ordóñez & Zenteno, *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*, AEJ Applied Economics 2018. The study reports $68 million randomly allocated across low-income urban neighborhoods, improvements in infrastructure access, private housing investment, and an increase in aggregate real-estate value of about $2 per $1 invested. citeturn0search3

### D1 — Study identity/provenance
**PASS — strong.** Named investigators, peer-reviewed publication and public OpenICPSR replication project. The deposit includes household data, analysis scripts and real-estate replication scripts. citeturn1search1turn1search6

### D2 — Causal design
**PASS — strong.** Infrastructure spending was randomly allocated across neighborhoods. citeturn0search3

### D3 — Structural accessibility transition
**B — strong candidate, exact representation still open.** The intervention directly improves infrastructure access. The replication project contains household and real-estate data plus analysis scripts, making an explicit `S_0/S_1 → T_acc,0/T_acc,1` reconstruction plausible. However, the exact infrastructure variables and their mapping to a transformation universe/predicate have not yet been audited at variable level. The C10-C requirement is therefore not yet satisfied. citeturn0search1turn1search1

### D4 — Independent value endpoint
**PASS — strong.** Real-estate value is a monetary endpoint distinct from infrastructure accessibility. The published result explicitly reports aggregate real-estate value gains relative to investment. citeturn0search3

### D5 — Counterfactual
**PASS — strong.** Random allocation provides the core treatment/control counterfactual; spillovers/saturation must be represented explicitly in the final identification analysis. citeturn0search3

### D6 — Downstream pathway
**B — evidence gap.** The study documents infrastructure access and private housing investment before the value endpoint, but the candidate audit must determine which intermediate variables can represent `ΔReach`/`ΔTrajectory` without substituting investment amount or observed real-estate value for `ΔT_acc`. The replication deposit includes dedicated analysis scripts, so this is a tractable documentary audit rather than an assumed PASS. citeturn1search1turn1search6

### D7 — Competing mechanisms
**B — material.** Spillovers, municipal responses, substitution and neighborhood-level interactions need to be explicitly considered. The study's randomized neighborhood design does not by itself make these mechanisms disappear. citeturn0search3

### D8 — Reproducibility/provenance
**PASS — strong documentary basis.** OpenICPSR provides the replication package, including `Habitat_Household_Data_for_Replication.dta`, household analysis code and real-estate analysis code. The DTA is about 139.9 MB, so no download is authorized yet. citeturn1search1turn0search5turn1search6

**Classification: B — PROMISING / EVIDENCE GAP.**
**Priority: HIGH.**

## 4. Candidate C10C-003 — Off-grid Solar Power in India

**Classification: B — PROMISING / EVIDENCE GAP.** Randomized structural access candidate with useful null/negative downstream evidence; retained as backup. No candidate-specific audit yet.

## 5. Candidate C10C-004 — Rural financial access / microcredit Morocco

**Classification: B — PROMISING / EVIDENCE GAP.** Randomized financial-access candidate with profit/investment endpoints; retained as secondary candidate. No candidate-specific audit yet.

## 6. Candidate C10C-005 — StudentPOWR digital intervention

**Classification: C — REJECTED / DESIGN-INCOMPATIBLE FOR CURRENT C10-C ROUND.** Structural transformation-space transition is insufficiently clear under the frozen TGCV operational definition.

## 7. Candidate C10C-006 — Digital support / child development Peru

**Classification: B — PROMISING / EVIDENCE GAP.** Cluster-randomized candidate with public replication materials; value endpoint and structural accessibility mapping remain insufficiently specified.

## 8. Candidate C10C-007 — Local infrastructure / public-service access Mumbai 2026

**Classification: B — PROMISING / VALUE-ENDPOINT GAP.** Strong structural-access design candidate, but independent value endpoint not yet established from documentary screening.

## 9. Admission decision after candidate-specific audit

### C10C-001 — Egypt
**Remain B.** The causal and value layers are unusually strong. The decisive unresolved question is whether the experimental “opportunity to export” can be translated into an explicit, reproducible `ΔT_acc` without equating accessibility with take-up/exporting or importing downstream learning into accessibility.

### C10C-002 — Mexico
**Remain B.** This is currently the stronger structural-accessibility candidate because the intervention is physical/local infrastructure and the replication package contains dedicated household and real-estate analysis files. The decisive unresolved question is exact variable-level reconstruction of `T_acc,0`, `T_acc,1`, and `ΔT_acc`, plus separation from investment intensity and spillovers.

## 10. Current priority order

1. **C10C-002 Mexico infrastructure — HIGH / first documentary admission audit.**
2. **C10C-001 Egypt export access — HIGH / parallel documentary audit.**
3. C10C-003 India solar — backup.
4. C10C-004 Morocco microcredit — secondary.

## 11. Authorization status

**Discovery:** COMPLETE.

**Candidate-specific documentary admission audit:** AUTHORIZED.

**Dataset download:** NOT AUTHORIZED.

**Empirical reconstruction:** NOT AUTHORIZED.

**Causal estimation:** NOT AUTHORIZED.

**Claim-level upgrade:** NOT AUTHORIZED.

## 12. Next controlled operation

Perform the **variable-level documentary admission audit for C10C-002 (Mexico)** using only publicly documented replication metadata/scripts at this stage. The audit must answer, before any download or execution authorization:

1. What observed variables encode the pre/post structural infrastructure state?
2. Can `U_τ` and `P_τ(S,C,L)` be specified without using real-estate value or downstream outcomes?
3. Can `T_acc,0`, `T_acc,1` and `ΔT_acc` be reconstructed reproducibly?
4. Is the value endpoint independently defined at the same unit/horizon?
5. Can investment intensity, spillovers and other competing mechanisms be separated or bounded?
6. Does the existing replication package contain all provenance needed for an independent reconstruction?

No empirical dataset download or execution is authorized by this record.
