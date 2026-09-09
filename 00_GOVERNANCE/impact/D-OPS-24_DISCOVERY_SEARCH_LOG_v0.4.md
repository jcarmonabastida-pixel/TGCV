# D-OPS-24 — Discovery Search Log v0.4

**Status:** PRE-REGISTERED — SEARCH EXECUTION NOT AUTHORIZED
**Date:** 2026-09-09
**Protocol:** `D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.4.md`
**Governance decision:** `EXT-UPD-4.0_DOPS24_CONTINUATION_DECISION_v0.1.md`
**Scope:** F2 — Physical/engineering reconfiguration systems

## 1. Execution boundary

This log pre-registers the complete F2 Q1–Q3 query formulations before execution. No search has been executed under this log.

Execution remains blocked until the v0.4 preflight/consistency gate is explicitly closed and a documentary-search authorization is recorded.

## 2. Fixed semantic groups

### State terms
`state configuration structure composition condition topology mode regime system configuration`

### Transformation terms
`reconfiguration switching restructuring topology change repair replacement operation intervention transition modification`

### Accessibility terms
`feasible admissible available enabled applicable possible permitted reachable realizable`

### Temporal terms
`longitudinal temporal sequence history repeated observation evolution change over time`

### F2 native-domain terms
`physical engineering device infrastructure mechanical electrical control system`

### Source-type restriction
Peer-reviewed scholarly literature, established scholarly indexes, authoritative institutional/project documentation, official dataset documentation/repositories, and stable archival primary sources.

## 3. Pre-registered query families

The three query families are materially distinct in their exact formulation while preserving the same fixed semantic groups and source restriction. Q1 is the broad baseline; Q2 changes the formulation to require an explicit longitudinal/accessibility conjunction; Q3 changes the formulation to foreground the F2 native-domain construct and explicit reconfiguration/accessibility conjunction. These distinctions are registered before execution and are not to be altered during the F2 run.

### F2-Q1 — Broad physical/engineering reconfiguration baseline

`state configuration structure composition condition topology mode regime system configuration reconfiguration switching restructuring topology change repair replacement operation intervention transition modification feasible admissible available enabled applicable possible permitted reachable realizable longitudinal temporal sequence history repeated observation evolution change over time physical engineering device infrastructure mechanical electrical control system`

**Q-ID:** F2-Q1
**Budget unit:** 1 of 3
**Formulation class:** broad concatenative baseline across all fixed semantic groups.

### F2-Q2 — Longitudinal accessibility conjunction

`"longitudinal" "temporal" "history" "repeated observation" (reconfiguration OR switching OR restructuring OR transition OR modification) (feasible OR admissible OR available OR enabled OR applicable OR possible OR permitted OR reachable OR realizable) (state OR configuration OR structure OR composition OR condition OR topology OR mode OR regime) (physical OR engineering OR device OR infrastructure OR mechanical OR electrical OR control OR system)`

**Q-ID:** F2-Q2
**Budget unit:** 2 of 3
**Formulation class:** explicit temporal/accessibility conjunction with transformation, state and F2-native constraints.

### F2-Q3 — Native engineering reconfiguration/accessibility conjunction

`("physical engineering" OR device OR infrastructure OR mechanical OR electrical OR "control system") (reconfiguration OR switching OR restructuring OR "topology change" OR repair OR replacement OR operation OR intervention OR transition OR modification) (feasible OR admissible OR available OR enabled OR applicable OR possible OR permitted OR reachable OR realizable) (state OR configuration OR structure OR composition OR condition OR topology OR mode OR regime) (longitudinal OR temporal OR sequence OR history OR "repeated observation" OR evolution)`

**Q-ID:** F2-Q3
**Budget unit:** 3 of 3
**Formulation class:** explicit F2-native-domain emphasis with transformation/accessibility conjunction and temporal condition.

## 4. Candidate screening budget

- Maximum initial candidate records: 10.
- Budget is cumulative across engines, repositories, sessions and operators.
- No reset.
- No retroactive reclassification.
- Search snippets alone cannot support candidate admission.

## 5. Candidate-record minimum

For each screened record: candidate ID; Q-ID; exact query; timestamp; primary/authoritative source; native unit/state; native transformation universe; temporal ordering; accessibility criterion; feasibility of `U_τ,D`, `T_acc,D`, `ΔT_acc,D`; pre-outcome accessibility; unresolved/empty cases; Reach/Trajectory; Outcome separation; provenance; redundancy/prior-art check; C1–C5 preliminary risks; mapping class; exclusion/admission reason.

## 6. Deviation rule

If an executed search materially differs from the exact pre-registered formulation or its fixed semantic groups/source restriction, the deviation is NON-ADMISSIBLE. The intended Q-ID must not be retroactively assigned to the deviating search. Execution stops pending a new versioned governance decision.

## 7. Stopping rules

A — candidate threshold reached and transferred to candidate-admission audit.

B — F2 exhausted within the registered budget with no admissible candidate.

C — governance/procedural deviation or scientific-memory/prior-art conflict; immediate stop.

## 8. Non-authorized activities

No dataset acquisition, dataset processing, empirical execution, outcome analysis, model fitting, value analysis or D-OPS-24 translation-conformance execution is authorized by this log.

## 9. Pre-registration checksum fields

Q1 exact formulation: REGISTERED / NOT EXECUTED
Q2 exact formulation: REGISTERED / NOT EXECUTED
Q3 exact formulation: REGISTERED / NOT EXECUTED
F2 candidate budget: 10 maximum
F2 query-family budget: 3 maximum
