# TGCV — C10-C Candidate C10C-002 Documentary Admission Audit 001

**Status:** COMPLETED — DOCUMENTARY AUDIT; DATA ACQUISITION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*
**Gate:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`
**Admission specification:** `TGCV_C10_C_CANDIDATE_DISCOVERY_DATA_LEVEL_ADMISSION_SPECIFICATION_001.md`

## 1. Boundary

This audit uses only publicly available study/deposit metadata and documentary descriptions. It does not download, inspect or execute the replication data.

The OpenICPSR V1 deposit is publicly catalogued under ICPSR 113705 and states that the material is distributed as received from the depositor; ICPSR does not review, check or process the material. The public catalogue identifies household replication data and the study's real-estate replication material. 

## 2. Documentary findings

### D1 — Provenance
**PASS.** Stable study identity, named investigators and OpenICPSR V1 deposit are established. The public catalogue identifies V1 and the replication project DOI.

### D2 — Causal design
**PASS.** The study is documented as a randomized local-infrastructure investment experiment. The public study description states that $68 million was randomly allocated across low-income urban neighbourhoods.

### D3 — Structural state
**CONDITIONALLY SUPPORTED.** Public methodological documentation identifies observable infrastructure variables including piped water, drainage, electricity, curbs, sidewalks and paved streets. These are suitable candidates for structural state components because they describe infrastructure/service availability rather than downstream value.

The documentary record is sufficient to define the candidate state dimensions conceptually, but not yet sufficient to certify exact source-variable coding, missing-value rules, linkage and unit-level reconstruction. Those require controlled inspection of the deposited materials.

### D4 — Bounded transformation universe
**PROMISING / NOT YET ADMITTED.** A minimum-sufficient bounded universe can be formulated as opening/closing transformations for the six observable infrastructure dimensions:

`U_τ* = {Agua+, Agua−, Drenaje+, Drenaje−, Luz+, Luz−, Guarniciones+, Guarniciones−, Banquetas+, Banquetas−, Pavimento+, Pavimento−}`.

This is a methodological candidate only. It is not yet an empirical reconstruction because the exact deposited variable mappings and admissible-value rules have not been inspected in this audit.

### D5 — Accessibility predicates
**CONDITIONALLY SUPPORTED.** Structural feasibility predicates are available in principle:

`P(τ_j+) = 1[S_j < 1]`

`P(τ_j−) = 1[S_j > 0]`.

No value endpoint or downstream outcome is required by these predicates. However, exact coding and provenance must be verified at data level before admission.

### D6 — Treatment/state separation
**PASS AT DESIGN LEVEL; DATA-LEVEL VERIFICATION REQUIRED.** Randomized treatment assignment is conceptually distinct from realized infrastructure state. The study's intervention can therefore be treated as causal variation while `S_t` remains an observed structural state.

### D7 — Value endpoint
**PASS — STRONG DOCUMENTARY FIT.** The study explicitly reports aggregate real-estate value as an economic endpoint and separately documents professional real-estate valuation material. This is independently interpretable as value rather than as a definition of infrastructure accessibility.

### D8 — Counterfactual
**PASS AT DESIGN LEVEL.** Random allocation provides treatment/control counterfactual structure. The final estimand must nevertheless account for the documented neighbourhood-level treatment structure and possible saturation/spillover.

### D9 — Downstream mechanisms
**CONDITIONALLY SUPPORTED.** Public documentation identifies private housing investment and other downstream changes. These must remain downstream of `ΔT_acc` and must not be incorporated into `P_τ` or the transformation universe.

### D10 — Interference / spillovers
**EVIDENCE GAP.** Neighbourhood/municipality treatment saturation and spatial interactions are material to the causal design. The documentary record establishes the randomized neighbourhood structure but does not by itself certify an interference-free estimand.

### D11 — Reproducibility
**PROMISING / DATA-LEVEL VERIFICATION REQUIRED.** OpenICPSR V1 publicly identifies replication files including household data, household analysis code and real-estate replication material. Exact file hashes, variable provenance and executable reconstruction have not been performed in this audit.

## 3. Admission decision

**DECISION: PRIORITY-CANDIDATE / ADMITTED TO NEXT CONTROLLED DATA-LEVEL INSPECTION GATE.**

The candidate passes the documentary screen strongly enough to justify a candidate-specific controlled acquisition/inspection authorization. It is not yet admitted for empirical reconstruction.

The decisive unresolved items are:

1. exact variable-level reconstruction of `S_0` and `S_1`;
2. exact coding/missingness/unit/time/geographic provenance;
3. verification that the six-dimensional `U_τ*` is reproducible from deposited sources;
4. exact `T_acc,0`, `T_acc,1`, `ΔT_acc` linkage to the causal unit;
5. interference/saturation characterization;
6. exact value-endpoint linkage and horizon;
7. independent reproducibility requirements.

## 4. Governance boundary

This audit does **not** authorize:

- download of the dataset;
- execution of replication code;
- reconstruction of `T_acc`;
- causal estimation;
- value regression;
- claim upgrade.

A separate candidate-specific controlled acquisition/inspection authorization is required before any of those activities.

## 5. Conclusion

C10C-002 remains the highest-priority candidate for C10-C because it combines a randomized structural intervention, a plausible bounded transformation universe and an independently documented real-estate value endpoint. The documentary audit supports progression to controlled data-level inspection while preserving the frozen no-execution boundary.
