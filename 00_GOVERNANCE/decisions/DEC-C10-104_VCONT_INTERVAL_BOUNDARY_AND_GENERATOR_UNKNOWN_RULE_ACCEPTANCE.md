# DEC-C10-104 — V_cont interval-boundary convention and conservative Generator UNKNOWN rule

**Date:** 2026-11-16  
**Status:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Scope:** C10-S synthetic experiment / B1 functional continuity / V_cont interval adjudication and Generator truth semantics  
**Branch:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Acceptance basis:** Explicit user approval on 2026-11-16 of the Gate 137 proposal, including the semi-open interval convention and conservative handling of functional UNKNOWN.

## 1. Decision

The Gate 137 proposal is accepted as a complementary working decision to DEC-C10-100, DEC-C10-101 and DEC-C10-102. It resolves interval-boundary assignment and constrains the circumstances in which Generator may emit functional UNKNOWN for A_B1. It does not amend the accepted V_cont definition, window origin, strict-continuity rule or observation/truth separation.

## 2. Versioned interval-boundary convention

Let the common post-Z window be [t0,T*], with ordered boundaries b0=t0 < b1 < … < bK=T*. The K intervals are:

- For k=1,…,K−1: I_k=[b_{k−1},b_k).
- Final interval: I_K=[b_{K−1},b_K].

Consequences:

1. An event exactly at an internal boundary b_j, 0<j<K, is assigned to the interval beginning at that boundary, I_{j+1}.
2. An event exactly at T* is assigned to the final interval.
3. A functional-failure episode that extends across an interval boundary affects every interval whose temporal support it intersects, subject to the boundary assignment above.
4. The rule is deterministic, unique and versioned; it is the operative convention for future V_cont materialization and adjudication.

This decision does not select numerical values for T*, K, Δ, temporal unit, event resolution, sampling frequency, minimum failure duration or S3 detectability. It does not imply that the required event history or interval grid has been implemented.

## 3. Conservative Generator rule for functional UNKNOWN

The tri-valued state space accepted by DEC-C10-100 remains {1,0,?}, and its UNKNOWN-to-bounds propagation remains in force.

However, no functional ? may be emitted merely because a synthetic event, state, timestamp, component or rule is absent from the model or harness, or because the observation channel is incomplete. For a complete and determinate synthetic functional history, Generator must adjudicate A_B1 as 1 or 0 under DEC-C10-102 and the interval convention in §2.

A functional ? is permitted only after a separate, explicit DGP contract defines an intrinsic functional indeterminacy for A_B1, including its semantic condition, scope and provenance. No such condition is approved by this decision. Until then, the conservative default is that Generator emits no functional UNKNOWN in otherwise complete, determinate histories.

In particular, functional ? must not be derived from:
- S3 absence, loss, lag, invalidity, coverage or measurement error;
- missing ENABLED/PROFILE states, events or timestamps caused by an incomplete DGP/harness specification or implementation;
- unmodelled events, unbounded temporal support or unresolved interval boundaries;
- Analyzer's inability to observe, classify or identify the functional state;
- Generator, TruthBundle, Sealer or harness integrity/implementation failures.

These remain observation-channel uncertainty, design/specification gaps or implementation defects, as applicable; none is functional UNKNOWN under DEC-C10-102.

## 4. Preserved decisions and boundaries

- DEC-C10-100 remains authoritative for equal-duration interval aggregation and tri-valued truth/bounds.
- DEC-C10-101 remains authoritative for the post-Z window origin at t0, including provision and installation.
- DEC-C10-102 remains authoritative for strict continuity: any confirmed functional failure at any instant makes the affected interval's truth 0.
- S3 remains a passive, imperfect observation channel. S3 missingness is not functional UNKNOWN.
- This decision does not define causal contrast bounds by subtracting marginal interval endpoints. Causal bounds still require the relevant joint potential-outcome, population, support and interference contracts.
- No values for T*, K, Δ, temporal resolution, roster, sample size, measurement calibration or power are selected.

## 5. Implementation and authorization status

This is an accepted working design decision, not evidence of implementation, execution, identification or scientific confirmation. It does not authorize changes to code, schemas, fixtures, tests or workflows; nor generation, simulation, calibration, estimation, experiment execution or Design Freeze.

scientific_execution=false  
execution_authorized=false

## 6. Provenance

Gate 137: 00_GOVERNANCE/SIP/C10_S_UNKNOWN_AND_INTERVAL_BOUNDARY_DECISION_DOCKET_GATE_137_DRAFT_001.md.  
Gate 137 plan addendum: 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_137_UNKNOWN_BOUNDARY_DOCKET_ADDENDUM_DRAFT_001.md.  
Related decisions: DEC-C10-100, DEC-C10-101, DEC-C10-102.  
Decision Log: 00_GOVERNANCE/SIP/C10_S_DECISION_LOG_DRAFT_001.md.
