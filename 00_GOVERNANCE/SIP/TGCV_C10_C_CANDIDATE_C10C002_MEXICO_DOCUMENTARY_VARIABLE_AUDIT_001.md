# TGCV C10-C — C10C-002 Mexico Documentary Variable Audit 001

**Status:** DOCUMENTARY AUDIT COMPLETE — VARIABLE-LEVEL EMPIRICAL RECONSTRUCTION NOT YET AUTHORIZED
**Date:** 2026-09-14
**Candidate:** C10C-002 — *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*
**Study:** McIntosh, Alegría, Ordóñez & Zenteno (2018), AEJ Applied Economics.
**Replication:** OpenICPSR 113705, V1.

## 1. Audit scope

This audit uses only publicly accessible study documentation, publication material and replication-package metadata. It does **not** download the 139.9 MB household DTA, the 70.1 MB XLSX, or execute the Stata replication code.

The objective is to determine whether the candidate is methodologically compatible with the frozen C10-C design and whether the remaining gap is sufficiently precise to justify a later, separately authorized data-level audit.

## 2. Documentary facts established

The study randomized treatment at the polygon level: 370 eligible polygons, 176 treatment and 194 control, with a two-level municipality-saturation randomization. citeturn1view2

The intervention was a multidimensional infrastructure programme. More than two-thirds of spending went to localized infrastructure; reported components include street paving, piped water, sewerage, medians and sidewalks. The paper also describes improvements in road paving, sidewalks, medians and public lighting. citeturn1view2

The study collected panel block- and household-level data at baseline (2009) and follow-up (2012), and separately collected professional property valuations. citeturn1view2

The pre-analysis plan explicitly included an overall infrastructure index and availability of six infrastructure types: electricity, piped water, sewerage, paved streets, streetlights, and sidewalks/medians. citeturn1view2

For the property-value endpoint, professional INDAABIN assessors valued the same 464 unbuilt lots at baseline and follow-up; assessors were blinded to treatment status. The paper uses these valuations to estimate changes in raw land value. citeturn1view2

The public replication deposit contains the household dataset, household analysis script, real-estate data, real-estate analysis script, questionnaire and README. OpenICPSR lists the household DTA at 139.9 MB and the real-estate DTA at 125.9 KB. citeturn0search0turn0search2

## 3. C10-C D1–D8 audit

### D1 — Study identity / provenance
**PASS.** Peer-reviewed AEJ Applied Economics article; DOI `10.1257/app.20160429`; public OpenICPSR replication project with named investigators and versioned V1 deposit. citeturn0search3turn0search5

### D2 — Causal design
**PASS — strong.** Polygon-level randomized assignment with municipality-level saturation randomization supplies a credible experimental counterfactual, subject to explicit treatment saturation and spillover handling. citeturn1view2

### D3 — Structural accessibility transition
**PROVISIONAL PASS AT DOCUMENTARY LEVEL / EMPIRICAL VARIABLE AUDIT REQUIRED.**

The study provides unusually strong material for a TGCV accessibility construction because it observes multiple structural infrastructure attributes independently of property value. The pre-specified infrastructure dimensions are explicit and temporally ordered. citeturn1view2

A defensible candidate representation is:

`S_t = (infrastructure state of polygon/block/house, context)`

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

where candidate transformation families are defined from infrastructure-enabled activities/services, not from observed treatment outcomes.

The six documented infrastructure dimensions can provide observable state components, but **the exact variable names, coding, missing-value rules, aggregation level and panel correspondence have not yet been inspected**. Therefore D3 cannot be upgraded to an empirical PASS yet.

Critical anti-leakage rule: real-estate value, rents, private housing investment, social capital, crime, satisfaction and other downstream outcomes must not enter `P_τ`.

### D4 — Independent value endpoint
**PASS — strong.** Raw land/property value is independently measured by professional assessors, using the same unbuilt lots at baseline and follow-up, with assessors blinded to treatment. It is therefore not definitionally constructed from infrastructure access. citeturn1view2

For C10-C the preferred endpoint is the change in professionally assessed raw land value for the relevant lot/polygon aggregation, with the exact estimand and aggregation frozen before empirical execution.

### D5 — Counterfactual adequacy
**PASS — strong, bounded.** Randomized treatment/control assignment provides the basic counterfactual. The two-level saturation design and spatial structure require explicit consideration of spillovers and interference rather than assuming SUTVA without qualification. citeturn1view2

### D6 — Downstream pathway adequacy
**PASS/B — structurally promising.** The data architecture contains infrastructure measures, private housing investment, rents/property values and other downstream outcomes. This supports a potential decomposition:

`Z → ΔT_acc → ΔReach/Trajectory → private response → land value`

but the actual `Reach` and `Trajectory` representation is not yet established and must not be manufactured retrospectively from the outcome variables.

### D7 — Competing mechanisms / interference
**B — material but potentially auditable.** The intervention is multidimensional; private housing investment is itself affected by treatment; municipalities participate in implementation; and the experiment includes saturation at municipality level. These factors can mediate or modify the value pathway. The paper explicitly discusses the saturation design and reports no strong spillover effects, but C10-C must still preserve the distinction between intervention, accessibility change, downstream response and value. citeturn1view2

### D8 — Reproducibility / provenance
**PASS — documentary.** The replication package contains the principal household data, real-estate data, analysis scripts, questionnaire and README. The public deposit is versioned. Exact variable-level provenance remains pending because the current audit has deliberately not downloaded or executed the files. citeturn0search0turn0search2

## 4. Variable-level questions that remain open

Before any empirical execution authorization, the following must be answered directly from the replication files/scripts:

1. Exact variable names for each of the six infrastructure dimensions.
2. Coding and admissible values for each infrastructure variable.
3. Whether baseline/endline variables are directly panel-linked at the polygon/block/house level.
4. Exact construction of the pre-committed infrastructure index.
5. Whether treatment assignment and actual infrastructure realization can be separated.
6. Whether actual infrastructure realization should be represented as `S_1` or whether treatment assignment must remain the causal instrument/exposure `Z` while `S_1` is reconstructed separately.
7. Exact unit and aggregation rule for `T_acc,0` and `T_acc,1`.
8. A defensible finite or operationally enumerable `U_τ` for the selected infrastructure transformation families.
9. A predicate `P_τ(S,C,L)` that uses only admissible structural/context variables and never downstream value/outcome information.
10. Whether missingness, replacements and panel attrition affect the structural-state reconstruction.
11. Exact property-value variables, units, timing and aggregation.
12. Exact treatment/control linkage for the 464 valued lots.
13. Whether property-value estimation is sufficiently independent of private housing investment for the chosen value endpoint.
14. How municipality saturation and spatial spillovers enter the causal estimand.
15. Which variables, if any, can legitimately represent `Reach` and `Trajectory` without circularly encoding value.

## 5. Current methodological assessment

**C10C-002 remains B — PROMISING / EVIDENCE GAP.**

This audit strengthens rather than weakens the candidate. The published design provides all major documentary ingredients required by the frozen C10-C gate:

- randomized structural intervention;
- independently observed infrastructure/accessibility dimensions;
- explicit pre/post timing;
- independent monetary value endpoint;
- randomized counterfactual;
- public replication package;
- documented downstream private investment and other outcomes.

However, the decisive TGCV-specific construct — reproducible `ΔT_acc` — has **not** yet been demonstrated at variable level. It would be methodologically incorrect to mark C10C-002 admissible for execution before that step.

## 6. Important finding: no need to modify the frozen C10-C gate

The documentary audit does **not** reveal a need to change the frozen C10-C design. The remaining problem is operationalization within the existing contract:

`Z → structural state change → T_acc,0/T_acc,1 → ΔT_acc → downstream pathway → V`

The candidate should therefore proceed to a controlled **data-level variable dictionary audit**, not to a redesign of C10-C.

## 7. Authorization boundary

**Documentary screening:** PASS.

**Candidate status:** B — PROMISING / EVIDENCE GAP.

**Data-level variable audit:** NEXT CONTROLLED OPERATION.

**Dataset download:** NOT AUTHORIZED by this record.

**Empirical reconstruction:** NOT AUTHORIZED.

**Causal estimation:** NOT AUTHORIZED.

**Claim-level upgrade:** NOT AUTHORIZED.

## 8. Next controlled operation

Freeze a candidate-specific **C10C-002 data-level admission package specification** listing the exact files that may be inspected, the variables to audit, the admissible derived-variable rules, the `T_acc` construction test, and the stop conditions. Only after that package is frozen should a separate authorization permit acquisition/inspection of the replication data.
