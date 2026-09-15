# TGCV — C10-C C10C-002 Controlled Acquisition and Inspection Authorization 002

**Status:** AUTHORIZED — CONTROLLED DATA-LEVEL ACQUISITION AND INSPECTION ONLY
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico
**Source:** OpenICPSR 113705 V1
**Parent:** `TGCV_C10_C_CANDIDATE_DISCOVERY_DATA_LEVEL_ADMISSION_SPECIFICATION_001.md`
**Design gate:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`

## 1. Authorization purpose

Authorize acquisition and controlled inspection of the exact OpenICPSR 113705 V1 replication materials solely to determine whether C10C-002 can support a reproducible bounded C10-C reconstruction of `T_acc,0`, `T_acc,1`, `ΔT_acc` and an independently defined value endpoint.

This authorization does **not** authorize causal estimation, claim upgrade, or unrestricted exploratory analysis.

## 2. Authorized source boundary

Only the following V1 deposit files are authorized:

1. `Encuestas-2012.docx`
2. `Habitat_Household_Analysis_Replication_170830.do`
3. `Habitat_Household_Data_for_Replication.dta`
4. `Habitat_Household_Data_for_Replication.xlsx`
5. `Habitat_Real_Estate_Replication_170830.do`
6. `ReadMe.txt`
7. `real_estate_polygon_level.dta`
8. `real_estate_polygon_level.xlsx`

A companion file may be admitted only if the official V1 documentation establishes that it is necessary to decode one of the authorized files; it must then be separately recorded before use.

## 3. Mandatory acquisition record

Before inspection, record for every acquired file:

- exact filename;
- source/version;
- byte size;
- SHA-256;
- acquisition timestamp;
- acquisition route;
- any archive/container SHA-256.

No silent substitution, conversion or version mixing is permitted.

## 4. Controlled inspection questions

### A — Provenance

Can every structural and value variable be traced through:

`source_file → variable → label/definition → coding → admissible values → missing codes → unit → time → geographic/unit level → transformation rule`?

### B — Structural state

Identify the minimum structural state variables required to represent the infrastructure conditions independently of value and treatment assignment.

### C — Treatment/state separation

Identify assignment variables separately from realized infrastructure state. Treatment must not be used as a substitute for `S_t`.

### D — Bounded transformation universe

Determine whether a minimum sufficient finite/operationally enumerable `U_τ*` can be frozen before causal estimation.

Every transformation must have an identifier, verbal definition, structural prerequisites, source mapping and deterministic predicate.

### E — Accessibility reconstruction

Determine whether `T_acc,0`, `T_acc,1` and `ΔT_acc` can be reconstructed reproducibly from structural/context variables alone.

### F — Independent value endpoint

Verify the real-estate endpoint, its unit, timing, linkage to the same causal unit, measurement protocol and independence from the accessibility construction.

### G — Identification/counterfactual

Verify treatment allocation, control structure, timing and the assumptions needed for the intended bounded causal contrast.

### H — Interference/spillovers

Inspect municipality saturation, spatial structure and any documented spillover mechanisms sufficiently to determine whether the intended estimand can remain identifiable or must be bounded/qualified.

### I — Reproducibility

Verify that the deposited scripts and files contain enough information for an independent reconstruction without undocumented assumptions.

## 5. Permitted operations

- acquire the eight authorized V1 files;
- calculate and record hashes and sizes;
- read documentation and code;
- inspect variable metadata and coding;
- construct provenance tables;
- define candidate structural variables;
- define a provisional bounded `U_τ*` and deterministic `P_τ` only for admission assessment;
- verify unit/time linkage and endpoint availability;
- document interference and reproducibility constraints.

## 6. Prohibited operations

- causal estimation;
- treatment-effect regression;
- value regression;
- hypothesis testing;
- selecting transformations based on observed outcomes/value;
- fitting `P_τ` to value or downstream outcomes;
- post-hoc narrowing of `U_τ*` to obtain a preferred result;
- using real-estate value as part of accessibility;
- claim upgrade;
- mixing V1 with other versions or external datasets;
- reopening C10C-002's already completed bounded causal experiment;
- modifying frozen C10-C design or admission rules.

## 7. Stop conditions

Immediately stop and classify the candidate as `BLOCKED` if any of the following occurs:

- source identity/version cannot be established;
- provenance requires guessing;
- structural variables cannot be reconstructed;
- `U_τ*` cannot be bounded independently of value/outcomes;
- treatment and structural state cannot be separated;
- value endpoint cannot be independently linked;
- counterfactual cannot be defended;
- interference makes the intended estimand undefined or materially ambiguous;
- missingness/linkage prevents reproducible reconstruction;
- required information is absent from the authorized source boundary.

No workaround by adding an unapproved dataset is permitted.

## 8. Required outputs

The controlled inspection must produce:

1. acquisition manifest with hashes and sizes;
2. provenance table;
3. structural state dictionary;
4. treatment/state separation record;
5. bounded `U_τ*` proposal and transformation dictionary;
6. deterministic `P_τ` definitions;
7. `T_acc,0/T_acc,1/ΔT_acc` feasibility assessment;
8. independent value-endpoint assessment;
9. causal-unit and temporal linkage assessment;
10. interference/spillover assessment;
11. reproducibility assessment;
12. T1–T10 admission disposition;
13. candidate decision: `ADMISSIBLE FOR EMPIRICAL EXECUTION`, `PROMISING`, `EVIDENCE GAP REMAINS`, `BLOCKED`, or `REJECTED FOR C10-C`.

## 9. Governance boundary

This authorization creates a controlled data-level inspection boundary only. A positive inspection result does not itself authorize causal estimation.

If the candidate is found admissible, a separate execution authorization must freeze the final operational variables, estimand, counterfactual, analysis specification and reproducibility requirements before any causal estimation.

## 10. Relationship to prior C10C-002 work

The previously completed C10C-002 bounded causal experiment remains closed and its negative result remains unchanged.

This inspection is a **methodological C10-C value-linkage admission audit**, not a rerun and not an attempt to obtain a positive result.

## 11. Decision

**AUTHORIZED — CONTROLLED DATA-LEVEL ACQUISITION AND INSPECTION ONLY.**

Next operation: acquire the exact OpenICPSR 113705 V1 package, record the manifest/hashes, and execute the controlled variable-level inspection. No causal estimation is authorized at this stage.
