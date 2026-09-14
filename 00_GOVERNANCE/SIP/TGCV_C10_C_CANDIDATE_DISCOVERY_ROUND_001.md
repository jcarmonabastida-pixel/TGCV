# TGCV — C10-C Candidate Discovery Round 001

**Status:** DOCUMENTARY SCREENING COMPLETE — NO EMPIRICAL EXECUTION
**Date:** 2026-09-14
**Gate:** `TGCV_C10_C_CANDIDATE_DISCOVERY_DATASET_FIRST_ADMISSION_GATE_001.md`
**Design contract:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`

## 1. Scope

This round performs documentary candidate discovery only. No dataset was downloaded, no `T_acc` was reconstructed, and no causal estimate was executed.

### Screening result

Two candidates merit **A/B-level follow-up**, while the remaining screened cases are retained as lower-priority or rejected/indeterminate candidates.

## 2. Candidate C10C-001 — Exporting and Firm Performance: Randomized Experiment

**Source:** Atkin, Khandelwal & Osman, *Exporting and Firm Performance: Evidence from a Randomized Experiment*, Quarterly Journal of Economics (2017).

**Discovery evidence:** The study reports randomized variation in access to foreign markets for rug producers in Egypt and causal effects on firm profits. Treatment firms reported 16–26% higher profits; the paper uses an ITT framework because not all firms offered export opportunities took them up. citeturn0search0

### D1 — Study identity/provenance

**PASS — documentary.** Peer-reviewed study with stable journal/DOI identity.

### D2 — Causal design

**PASS — strong.** Randomized experiment generating exogenous variation in export-market access. citeturn0search0

### D3 — Structural accessibility transition

**BORDERLINE / REQUIRES PRIMARY-DATA AUDIT.** Candidate interpretation:

`S_0 = firm without experimentally enabled foreign-market access`

`S_1 = firm with experimentally enabled foreign-market access`

`T_acc,0 → T_acc,1` = change in the set of export-related transformations structurally accessible to the firm.

The crucial unresolved issue is whether the available treatment documentation and firm-level variables allow an explicit, reproducible transformation universe/predicate rather than treating “export access” itself as synonymous with `T_acc`.

### D4 — Independent value endpoint

**PASS — promising.** Firm profit is an explicit economic outcome and is not definitionally identical to export accessibility. The paper directly estimates impacts on profits. citeturn0search0

### D5 — Counterfactual

**PASS — strong.** Randomized treatment/control structure supplies a defensible counterfactual.

### D6 — Downstream pathway

**B — evidence gap.** The paper contains productivity, quality and output mechanisms, but a C10-C reconstruction must explicitly separate accessibility, export take-up, production choices, learning and profit. citeturn0search0

### D7 — Competing mechanisms

**B — manageable but material.** Take-up, learning-by-exporting, product quality, productivity and production intensity are plausible mediators/mechanisms. The study itself discusses these channels. citeturn0search0

### D8 — Reproducibility/provenance

**B — documentary confirmation required.** Study is highly promising, but admission requires verification of replication-data availability and exact variable-level provenance before execution.

**Classification: B — PROMISING / EVIDENCE GAP.**

**Priority:** HIGH.

## 3. Candidate C10C-002 — Neighborhood Impacts of Local Infrastructure Investment: Urban Mexico

**Source:** *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*; OpenICPSR replication project.

**Discovery evidence:** The project reports a large infrastructure investment experiment in which $68 million was randomly allocated across low-income urban neighborhoods. The intervention improved infrastructure access and increased private housing investment; aggregate real-estate value increased by about $2 per $1 invested. Replication data are publicly catalogued in OpenICPSR. citeturn0search5turn0search12

### D1 — Study identity/provenance

**PASS — strong documentary evidence.** Public OpenICPSR replication project with named investigators and data files. citeturn0search12

### D2 — Causal design

**PASS — strong.** Random allocation of infrastructure investment across neighborhoods. citeturn0search5

### D3 — Structural accessibility transition

**A/B — promising.** Infrastructure investment directly changes structural access to forms of infrastructure including electric lighting, street lights, sidewalks, medians and road paving. This is a strong candidate for explicit `S_0 → S_1` and `T_acc,0 → T_acc,1` reconstruction. citeturn0search13

### D4 — Independent value endpoint

**PASS — promising.** Aggregate real-estate value provides an explicit monetary value endpoint distinct from infrastructure accessibility. citeturn0search5turn0search13

### D5 — Counterfactual

**PASS — strong.** Random allocation provides a defensible counterfactual at the neighborhood level, subject to the study's saturation/spillover structure. citeturn0search13

### D6 — Downstream pathway

**B — evidence gap.** Infrastructure access, private housing investment and real-estate value are documented, but a C10-C analysis must establish whether intermediate accessibility changes can be represented independently of the investment amount and downstream property-value response.

### D7 — Competing mechanisms

**B — material.** Municipal responses, spillovers and substitution by other government investment are explicitly relevant to the study design. The paper discusses saturation and potential spillovers. citeturn0search13

### D8 — Reproducibility/provenance

**PASS — strong documentary evidence.** Public replication project includes data files; candidate-specific audit still required before execution. citeturn0search5turn0search12

**Classification: B — PROMISING / EVIDENCE GAP.**

**Priority:** HIGH.

## 4. Candidate C10C-003 — Off-grid Solar Power in India

**Source:** Aklin et al., *Does basic energy access generate socioeconomic benefits?* (Science Advances, 2017).

**Evidence:** Randomized field experiment with 1,281 rural households; treatment increased electrification by 29–36 percentage points and reduced kerosene expenditure, but showed no systematic changes in several broader socioeconomic indicators. citeturn0search2

**D1:** PASS.

**D2:** PASS — randomized field experiment.

**D3:** A/B — strong structural-access candidate: electricity access changes the set of feasible household activities, but explicit `T_acc` reconstruction is not yet demonstrated.

**D4:** B — potentially strong endpoints, but the value interpretation must be specified independently rather than equating socioeconomic outcomes with value.

**D5:** PASS — randomized treatment/control.

**D6:** B — downstream outcomes exist, but accessibility, usage and socioeconomic outcomes must be separated.

**D7:** B — treatment take-up, actual electricity use and broader household responses require separation.

**D8:** B — public full-text/replication provenance is promising; exact dataset admission still requires documentary audit.

**Classification: B — PROMISING / EVIDENCE GAP.**

**Priority:** MEDIUM-HIGH.

## 5. Candidate C10C-004 — Rural financial access / microcredit Morocco

**Source:** OpenICPSR replication data for *Estimating the Impact of Microcredit on Those Who Take It Up: Evidence from a Randomized Experiment in Morocco*.

**Evidence:** Treatment villages had access to microcredit; the documented results include effects on investment and profit but no overall gain in income or consumption. Replication data are publicly deposited. citeturn0search3

**D1:** PASS.

**D2:** PASS — randomized village-level access.

**D3:** B — financial-access transition is plausible, but `T_acc` must not be collapsed into loan take-up.

**D4:** B — profit is a promising value endpoint; income/consumption are not automatically value.

**D5:** PASS.

**D6:** B — borrower selection/take-up and business investment require mechanism separation.

**D7:** B — substantial selection/heterogeneity and externalities must be addressed.

**D8:** PASS/B — public replication deposit, subject to exact file-level audit.

**Classification: B — PROMISING / EVIDENCE GAP.**

**Priority:** MEDIUM.

## 6. Candidate C10C-005 — StudentPOWR digital intervention

**Evidence:** Randomized wait-list trial with full-access, partial-access and control groups; subjective wellbeing measured longitudinally. Dataset is deposited in DataverseNL. citeturn0search1

**D1:** PASS.

**D2:** PASS — randomized design.

**D3:** FAIL/BORDERLINE — intervention access is primarily access to a behavioral intervention rather than a clear structural transformation-space change. It risks collapsing “access to intervention” into `T_acc` without a defensible broader transformation universe.

**D4:** PASS — subjective wellbeing is an explicit evaluative endpoint.

**D5:** PASS.

**D6:** B.

**D7:** B.

**D8:** PASS — deposited dataset.

**Classification: C — REJECTED / DESIGN-INCOMPATIBLE FOR CURRENT C10-C ROUND.**

Reason: insufficiently clear structural accessibility transition under the frozen TGCV operational definition.

## 7. Candidate C10C-006 — Digital support / child development Peru

**Evidence:** Cluster-randomized trial with 2,461 caregiver-child dyads; public Dryad replication data and code; intervention effects on child development and reported cost-effectiveness. citeturn0search4

**D1:** PASS.

**D2:** PASS — cluster randomized.

**D3:** B — digital support changes accessible support transformations, but the structural transformation universe requires careful definition.

**D4:** B — cost-effectiveness is promising but may be an evaluation construct rather than a native value endpoint; exact value estimand would need freezing.

**D5:** PASS.

**D6:** B.

**D7:** B.

**D8:** PASS — Dryad provides data, code and codebook. citeturn0search4

**Classification: B — PROMISING / EVIDENCE GAP.**

**Priority:** MEDIUM.

## 8. Candidate C10C-007 — Local infrastructure / public-service access Mumbai 2026

**Evidence:** A 2026 cluster-randomized field experiment in Mumbai tested bureaucratic assistance and political coordination for obtaining municipal water connections, with midline and long-term endline observations; verification materials are deposited in the American Journal of Political Science Dataverse. citeturn0search6turn0search9

**D1:** PASS — current peer-reviewed study with replication materials.

**D2:** PASS — cluster-randomized factorial intervention.

**D3:** A/B — strong candidate for structural public-service accessibility transition.

**D4:** B — primary outcome is formal water connection/access; an independent value endpoint is not established from the discovery evidence. This is the principal current gap.

**D5:** PASS — randomized factorial counterfactual.

**D6:** PASS/B — long-term trajectory observations are promising.

**D7:** B — policy eligibility/exclusion and interaction effects require explicit handling.

**D8:** PASS — verification materials in Dataverse.

**Classification: B — PROMISING / EVIDENCE GAP, VALUE ENDPOINT GAP.**

**Priority:** MEDIUM.

## 9. Discovery conclusion

The round identifies **two highest-priority candidates for candidate-specific documentary admission audit**:

1. **C10C-001 — Export-market access / firm profits (Egypt).**
2. **C10C-002 — Randomized neighborhood infrastructure investment / real-estate value (Mexico).**

Both have strong causal designs and explicit value-like endpoints. The critical unresolved C10-C question is not whether they have treatment effects; it is whether a reproducible, non-circular `T_acc,0 → T_acc,1 → ΔT_acc` representation can be constructed while preserving the causal counterfactual and separating downstream mechanisms.

C10C-003 (India solar) is the strongest backup because it combines randomized structural access with several downstream outcomes, including a clear null/negative-style pattern that is scientifically useful under the sign-agnostic C10-C design.

## 10. Authorization status

**Discovery round:** COMPLETE.

**Candidate-specific documentary audit:** AUTHORIZED for C10C-001, C10C-002 and, if required, C10C-003.

**Dataset download:** NOT YET AUTHORIZED.

**Empirical reconstruction:** NOT AUTHORIZED.

**Causal estimation:** NOT AUTHORIZED.

**C10 claim upgrade:** NOT AUTHORIZED.

## 11. Next controlled operation

Perform candidate-specific **D1–D8 documentary admission audits** for C10C-001 and C10C-002, prioritizing the exact operational feasibility of `T_acc,0`, `T_acc,1` and `ΔT_acc`, value-endpoint independence, and replication-data provenance.
