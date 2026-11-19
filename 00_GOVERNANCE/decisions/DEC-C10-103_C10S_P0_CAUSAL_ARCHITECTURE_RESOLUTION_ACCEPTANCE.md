# DEC-C10-103 — C10-S P0 causal architecture resolution

**Date:** 2026-11-15  
**Status:** ACCEPTED WORKING DESIGN DECISION — CONDITIONAL MATERIAL/IDENTIFICATION GATES OPEN; NOT DESIGN FREEZE  
**Scope:** C10-S / B-value extension / D2 package / causal population, assignment-interference, inference target, estimand hierarchy and UE identity  
**Branch:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Acceptance basis:** Explicit user approval on 2026-11-15 of all five recommendations in Gate 120, with their stated conditions.

## 1. Decision

The five recommendations R120-1…R120-5 in Gate 120 are accepted as the working causal-design architecture for C10-S, subject to the conditions below. This decision resolves the design choices; it does not assert that the empirical/synthetic identification conditions have already been demonstrated or that the required roster, assignment mechanism, evidence or implementation has been materialized.

## 2. Population and A/B roster relationship (R120-1)

1. DEC-C10-095 remains authoritative: A and B are distinct, versioned DGP variants; A remains the technical reference and B is the Value extension. This decision does not reopen or amend that separation.
2. The causal rosters for A and B are separate by default. A is not the control arm or counterfactual population of B.
3. A cross-variant spine or matching relation may be used only through an explicit, versioned crosswalk that establishes equivalent basal unit definition, pre-Z eligibility and compatible baseline variables/contracts. Without that evidence, no paired A/B comparison or pooled estimand is permitted.
4. The B1/Need_preZ validation census under DEC-C10-096 remains a validation-task cohort, not a substitute for the causal target population P*_{τ2}, nor a post-Z/Need-based causal inclusion rule.
5. The causal population and roster membership must be fixed ex ante, before Z and before truth/evidence inspection, consistently with the existing population contracts.

## 3. Assignment and interference architecture (R120-2)

1. Develop individual assignment at UE level as the preferred confirmatory architecture, conditional on demonstrating material isolation before it is treated as the operative design.
2. The isolation audit must cover plausible cross-UE pathways, including shared/mutable pools and dependencies, agents, channels, resources, state, side effects and carryover. Shared immutable/read-only infrastructure is not automatically interference, but its non-transmission of effects must be justified.
3. The accepted logical rule of one B1 service instance per UE does not itself demonstrate isolation of all relevant causal pathways.
4. If isolation is not demonstrated, individual-assignment identification is not presumed. A cluster-assignment architecture or individual assignment with a versioned exposure map may be proposed only with its own assignment mechanism, estimand, support/positivity and inference contract.
5. If relevant interference exists but cannot be adequately mapped, Analyzer must abstain or report bounds/non-identification under the existing adjudication contracts. No post-outcome switching among architectures is permitted.

## 4. Unit and target of inference (R120-3)

Under the individual-assignment architecture and demonstrated isolation, the primary target is the UE-average effect over the eligible B causal population. UE is the unit of potential outcomes and, only if the assignment contract confirms it, the assignment unit. Routes, events, service instances and V_cont intervals do not replace the number of independent UEs.

If a cluster architecture is selected, the weighting target and inferential unit must be explicitly reconsidered before analysis. UE-average and cluster-average effects are not interchangeable, particularly with unequal cluster sizes. No cluster estimand is approved by this decision.

## 5. Confirmatory estimand hierarchy (R120-4)

1. **Focal accessibility-attribution estimand:** accept \\(\\theta_A(q_X^*,r_{common};V_{cont})\\) as the focal causal target for the contribution of the complete vector \\(\\Delta T_{acc}^*\\) to V_cont in B, under the common basal history and non-focal regime specified by its contract. This is an estimand selection, not a declaration of identification. The interventions/distributions g_A1/g_A0 must be well-defined, jointly feasible and supported; positivity, consistency, interference, measurement and identification conditions remain to be demonstrated.
2. **ITT-D2:** retain as the separate total effect of assignment to the D2 material package on V_cont and other pre-specified outcomes. It is a package/policy effect and is not interpreted as the isolated effect of accessibility. The mapping from D2 assignment to g_A interventions remains unproven.
3. **C4:** retain as a secondary, conditional interventional longitudinal mediation analysis, only if its time-varying history, post-Z confounding, sequential support and measurement contracts permit identification. C4 is not algebraically derived from ITT-D2 or θ_A.
4. **Direct/non-mediated effect:** exclude from the current confirmatory nucleus. It may be introduced only through a separately defined coherent interventional direct-effect estimand with its own population, intervention and assumptions.
5. A residual must never be defined automatically as ITT-D2 minus C4 or minus θ_A. Package effects, accessibility interventions and mediation estimands remain distinct.

## 6. UE identity and roster versioning (R120-5)

1. UE identity is immutable within its approved, versioned DGP/package roster. Roster identity, version and digest, UE identity and valid pre-Z bindings must be fixed before assignment and before truth/evidence inspection.
2. Replay of the same experimental realization preserves roster and UE identity. A new replicate/realization has distinct realization identity under the applicable reproducibility contract.
3. Cross-variant A/B matching requires the explicit, versioned crosswalk described in §2; identifiers are not reused or equated implicitly.
4. This decision does not materialize or physically approve the Draft `ue_id` field, a roster, schema or binding.
5. UE→U_G root remains UNKNOWN and is not forced unless a specific estimand or technical contract demonstrates that the mapping is necessary and an exact source snapshot supports it.

## 7. Preconditions and open gates

The following remain OPEN/CONDITIONAL and must not be inferred from this decision:
- approved B causal roster and exact P*_{τ2} membership/eligibility contract;
- material isolation evidence and the UE=UA assignment contract;
- assignment probabilities, strata, RNG/seed, vector and provenance;
- feasibility and joint support of q_X*, g_A1/g_A0 and r_common;
- mapping (if any) from D2 package assignment to the accessibility interventions;
- V_cont measurement validity, S3 detection/calibration, missingness, T*, Δ, K and quantitative precision/power;
- collateral pathways, heterogeneity, sensitivity and bounds;
- Analyzer/Evaluator information firewall, recovery criteria and abstention behavior;
- UE→U_G mapping, only if justified as necessary.

DEC-C10-099…102 remain in force for the provisional V_cont construct and temporal rules. They do not close its measurement/identification gates.

## 8. Governance and authorization

This decision is a working design acceptance, not Design Freeze. It does not authorize physical roster/schema/fixture creation, code changes, implementation, generation, simulation, calibration, estimation, validation execution or scientific execution. No parameter, sample size, rate, seed, power target or tolerance is set here.

No changes are made to main, C0, U_G, RMA, Evidence→Claim Matrix or STATUS. PR #116 remains Draft.

`scientific_execution=false`  
`execution_authorized=false`

**Source docket:** `00_GOVERNANCE/SIP/C10_S_P0_SCIENTIFIC_DECISION_RESOLUTION_DOCKET_GATE_120_DRAFT_001.md`  
**Master/plan propagation:** C10-S consolidated master §290; closure/operationalization plan §16.271; Decision Log C10-S.
