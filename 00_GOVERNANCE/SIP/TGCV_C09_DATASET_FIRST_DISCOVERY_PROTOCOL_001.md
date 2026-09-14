# TGCV C09 — Dataset-First Discovery Protocol 001

**Date:** 2026-09-14  
**Status:** FROZEN — DISCOVERY PROTOCOL ADOPTED  
**Scope:** C09 real-world candidate discovery only

## 1. Purpose

Replace the previous paper/candidate-first discovery route for C09 with a dataset-first discovery route.

The objective is to identify public, reproducible datasets whose observable structure can support the C09 target:

`Z → bounded ΔT_acc → subsequent trajectory Y`

The discovery process must search for the required data architecture first and only then identify the corresponding intervention/study.

## 2. Strategic decision

The previous route is closed for discovery purposes:

`paper → intervention → accessibility → outcome → attempt to adapt to C09`

The adopted route is:

`public dataset → stable unit → structural state transition → intervention → downstream trajectory → causal identification → candidate admission`

No new candidate is admitted merely because a published paper reports an effect of infrastructure/access on an outcome.

## 3. D0–D6 pipeline

### D0 — Dataset universe

Search trusted public repositories and archives first, including openICPSR/AEA Data and Code, Harvard Dataverse, World Bank reproducibility resources, Zenodo and equivalent public repositories.

The core data required for the C09 test must be publicly accessible and reproducible. Public code alone is insufficient.

### D1 — Structural transition

The dataset must permit observation or reconstruction for the same stable unit of a structural state transition:

`S_0 → S_1`

with an accessibility/capability representation:

`T_acc,0` and `T_acc,1`, hence bounded `ΔT_acc`.

`T_acc` must represent structural accessibility/capability and must not be defined by realized downstream behaviour, adoption, use, treatment status alone, or outcome.

### D2 — Intervention

An identifiable intervention/exposure `Z` must exist and must be distinguishable from the measurement of `T_acc,1`.

`T_acc,1 = Z` is not sufficient. A continuous, ordinal, spatial, capacity, distance, connectivity or equivalent structural measure may qualify where provenance is defensible.

### D3 — Stable unit

The same identifiable unit must be linkable across the relevant periods:

`unit_i,t0 → unit_i,t1 → Y_i,t>1`.

Cross-sectional substitution of different units is not sufficient.

### D4 — Downstream trajectory

`Y` must be measured after the structural transition and must represent an independent subsequent trajectory.

Direct use, adoption, take-up or immediate utilization of the intervention is not sufficient as the sole downstream outcome.

### D5 — Causal identification

The candidate must provide a defensible identification strategy for the intervention-induced structural change:

`Z → ΔT_acc`

and must permit a bounded assessment of whether the subsequent trajectory can be attributed to the accessibility change rather than merely to the total treatment effect or direct treatment pathways.

Randomized or credibly exogenous assignment is preferred but not mandatory if the identification argument is sufficiently defensible and reproducible.

### D6 — Provenance and admission

Every variable required for `Z`, `T_acc,0`, `T_acc,1`, `ΔT_acc`, the unit linkage and `Y` must have public provenance, reproducible construction and persistent source identity.

Candidates failing D0–D6 are rejected without preflight, controlled execution or TR-132 admission.

## 4. Mandatory discovery table

Every screened dataset is recorded using exactly these core fields:

| Dataset | Unit | t0 | t1 | Structural S0 | Structural S1 | Z | Y | Public? | Causal identification? | C09 potential |
|---|---|---|---|---|---|---|---|---|---|---|

Additional notes may be added, but these fields must not be removed or collapsed.

## 5. Early-stop rules

Reject immediately when any of the following is established:

- no public unit-level core data;
- no stable unit linkage;
- no observable/reconstructible `T_acc,0` and `T_acc,1`;
- `T_acc` collapses into treatment assignment/realization;
- `T_acc` is defined using post-treatment behaviour, adoption or outcome;
- downstream `Y` is merely intervention use;
- no defensible causal identification;
- required provenance depends on restricted, licensed or embargoed core data.

Do not continue a candidate after a definitive early-stop failure.

## 6. Interpretation discipline

This protocol does not require `T_acc,1` to be unaffected by `Z`. The relevant requirement is that `T_acc` be an independently defined structural representation whose change can be measured rather than simply recoding treatment status.

A total treatment effect:

`Z → Y`

is not by itself evidence for the C09 bridge:

`Z → ΔT_acc → Y`.

A mediator diagnostic may be reported where scientifically useful, but it must not be represented as causal mediation without the required identification assumptions.

## 7. Relation to C09 Gate 002

This protocol operationalizes the route selected by `TGCV_C09_CANDIDATE_CLASS_DECISION_GATE_002`:

- retrospective candidate loop: CLOSED;
- controlled/synthetic C09 route: CLOSED;
- directed paper-by-paper candidate loop: CLOSED;
- new route: DATASET-FIRST DISCOVERY FOR ONE REAL-WORLD CASE.

C09 remains an open, untested real-world causal claim. This protocol does not upgrade any TGCV claim, Core, RMA, Evidence Matrix or STATUS.

## 8. Next operation

Construct the first dataset-first discovery table from trusted public repositories and apply D0–D6 sequentially. The output is a ranked dataset inventory, not a list of papers.
