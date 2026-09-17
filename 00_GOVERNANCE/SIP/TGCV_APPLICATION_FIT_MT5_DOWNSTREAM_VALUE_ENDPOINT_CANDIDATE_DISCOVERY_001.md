# TGCV Application Fit — MT5 Downstream Value Endpoint Candidate Discovery 001

**Status:** `DESIGN / ANALYSIS ONLY — NO VALUE CLAIM / NO EXECUTION AUTHORIZATION`
**Date:** 2026-09-17
**Cycle:** TGCV Application Fit
**Purpose:** identify and structure candidate downstream value endpoints that could be linked to accessibility changes and subsequent trajectories, using only already-available bounded evidence and without upgrading any scientific or industrial claim.

## 1. Scope

This artifact advances the Application Fit cycle after closure of the TSTC minimum demonstrator and its cumulative evidence registration. It does **not** constitute a value experiment, causal validation, ROI analysis, industrial validation, or deployment recommendation.

The analytical chain remains:

`state/context → accessibility conditions → trajectory → candidate downstream value endpoint`

Only the final endpoint is being inventoried here. No causal effect on value is inferred.

## 2. Inputs admitted

The inventory may use already-registered bounded evidence from:

- TSTC / WP2 minimum demonstrator (C01, C03, C05), including its baseline reconstruction, negative controls and cross-domain synthetic propagation;
- bounded RUST-DYN-2 structural evidence concerning accessibility and one-step reach under the stated horizon;
- bounded SWIM/FOS trajectory and reconstructability evidence already registered in the programme;
- closed/bounded C10C application cases already registered in the evidence base.

No new dataset, rerun, AWS mutation, SWIM rerun, RUST-DYN-2 rerun, or new empirical execution is authorized by this artifact.

## 3. Candidate endpoint families

### E1 — Option-set / operational flexibility

Candidate endpoint: change in the practically usable transformation/option space available to an operator or system after an accessibility change.

Potential observable forms:
- number or proportion of admissible options;
- availability of previously unavailable transformation paths;
- persistence or loss of alternative routes.

Boundary: this is an operational endpoint candidate, not evidence that option-set expansion creates economic value.

### E2 — Reconfiguration / adaptation time

Candidate endpoint: time required to reach a specified subsequent operational state after an accessibility-relevant change.

Potential observable forms:
- time-to-reconfiguration;
- time-to-recovery;
- time-to-completion of a defined adaptation sequence.

Boundary: must be defined independently of the accessibility classification and measured over a frozen observation window before any causal design.

### E3 — Trajectory efficiency / path burden

Candidate endpoint: resource or step burden of reaching a fixed target state through the resulting trajectory.

Potential observable forms:
- number of transitions;
- elapsed time;
- resource consumption;
- detour or path length relative to a prespecified baseline.

Boundary: endpoint definition must not encode the expected direction of the result.

### E4 — Robustness / recovery envelope

Candidate endpoint: persistence of feasible trajectories under subsequent perturbations or recovery from a defined disruption.

Potential observable forms:
- fraction of admissible continuation paths retained;
- recovery time;
- successful completion under prespecified perturbations.

Boundary: no claim that robustness is economically valuable without a separate value model.

### E5 — Compliance / approval / coordination burden

Candidate endpoint: downstream operational burden associated with obtaining or maintaining the conditions required for a trajectory.

Potential observable forms:
- number of required approvals or coordination steps;
- elapsed approval/coordination time;
- rework or exception count.

Boundary: only appropriate where the underlying case contains an independently reconstructable process and a stable measurement definition.

### E6 — Resource utilisation / constraint pressure

Candidate endpoint: downstream utilisation or constraint pressure associated with the selected trajectory.

Potential observable forms:
- capacity utilisation;
- resource consumption;
- constraint violations avoided or incurred;
- slack remaining after execution.

Boundary: must be separated from the accessibility rule so that the endpoint is not circularly defined.

## 4. Candidate-case mapping

| Evidence family | Candidate endpoint families | Status |
|---|---|---|
| TSTC C01/C03/C05 | E1, E2, E3, E4 | candidate only; synthetic demonstrator |
| RUST-DYN-2 | E1, E3, E4 | bounded structural evidence; no value inference |
| SWIM/FOS | E2, E3, E4 | bounded trajectory/reconstructability evidence |
| Closed/bounded C10C cases | E2, E3, E5, E6 | case-dependent; endpoint availability must be audited |

This mapping is a discovery inventory, not a ranking.

## 5. Selection criteria for a future value endpoint study

A candidate endpoint can proceed to a later design stage only if all of the following can be satisfied:

1. the endpoint has an unambiguous operational definition;
2. its measurement does not use post-treatment accessibility information;
3. the observation window can be fixed before result inspection;
4. the trajectory preceding the endpoint can be independently reconstructed;
5. a suitable baseline/counterfactual can be specified;
6. the endpoint is distinct from the accessibility treatment itself;
7. alternative explanations and confounders can be specified;
8. the endpoint can be reproduced from frozen inputs;
9. any monetary or business-value interpretation is kept as a separate modelling layer.

## 6. Explicit non-claims

This artifact does **not** establish:

- that accessibility changes cause any listed endpoint;
- that any endpoint is a valid measure of value;
- that one endpoint is superior to another;
- that TGCV improves performance, ROI, productivity, resilience, compliance, or any other business outcome;
- industrial utility or deployment readiness;
- generality beyond the bounded evidence already registered.

## 7. Next controlled operation

The next Application Fit operation is an **endpoint admissibility audit**: select candidate endpoints only where the underlying evidence permits an independent, non-circular, reproducible operational definition. The audit must precede any value-oriented execution or claim update.

No execution authorization is created by this document.
