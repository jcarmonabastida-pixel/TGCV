# TGCV C09 — Dataset-First Discovery Protocol 002

**Date:** 2026-09-14  
**Status:** FROZEN — D5 CAUSAL-BRIDGE REFINEMENT ADOPTED  
**Supersedes:** `TGCV_C09_DATASET_FIRST_DISCOVERY_PROTOCOL_001.md` for future C09 discovery  
**Scope:** C09 real-world candidate discovery only

## 1. Purpose

Refine the dataset-first discovery route after repeated D5 failures showed that the principal bottleneck is not merely observing:

`Z → ΔT_acc`

and:

`Z → Y`

but identifying, bounding or otherwise defensibly separating the **specific causal bridge**:

`ΔT_acc → subsequent trajectory Y`

from direct treatment effects and alternative post-treatment pathways.

The discovery process must therefore search not only for a structural accessibility transition, but for a **mechanism-identification architecture** capable of separating or bounding the accessibility-mediated pathway.

## 2. Strategic decision

The adopted route is now:

`public dataset → stable unit → structural state transition → intervention → downstream trajectory → mechanism-identification architecture → causal bridge → candidate admission`

A dataset is not a strong C09 candidate merely because it contains a randomized intervention, pre/post accessibility measure and downstream outcome. If the same intervention simultaneously changes multiple post-treatment channels and there is no design or identification strategy capable of separating them, the candidate fails D5.

The previous protocol remains the conceptual base, but D5 is replaced by the refined mechanism-identification gate below.

## 3. D0–D6 pipeline

### D0 — Dataset universe

Search trusted public repositories and archives first, including openICPSR/AEA Data and Code, Harvard Dataverse, World Bank reproducibility resources, Zenodo and equivalent public repositories.

The core data required for the C09 test must be publicly accessible and reproducible. Public code alone is insufficient.

### D1 — Structural transition

The dataset must permit observation or reconstruction for the same stable unit of a structural state transition:

`S_0 → S_1`

with an independently defined accessibility/capability representation:

`T_acc,0` and `T_acc,1`, hence bounded `ΔT_acc`.

`T_acc` must represent structural accessibility/capability and must not be defined by realized downstream behaviour, adoption, use, treatment status alone, or outcome.

### D2 — Intervention

An identifiable intervention/exposure `Z` must exist and must be distinguishable from the measurement of `T_acc,1`.

`T_acc,1 = Z` is not sufficient. A continuous, ordinal, spatial, capacity, distance, connectivity or equivalent structural measure may qualify where provenance is defensible.

### D3 — Stable unit

The same identifiable structural unit must be linkable across the relevant periods:

`unit_i,t0 → unit_i,t1 → Y_i,t>1`.

Cross-sectional substitution of different units is not sufficient.

Where `Y` is measured on later cohorts or users attached to the stable structural unit, this is admissible only if the cohort-to-unit linkage is explicit and the estimand is defined at the structural-unit level.

### D4 — Downstream trajectory

`Y` must be measured after the structural transition and must represent an independent subsequent trajectory.

Direct use, adoption, take-up or immediate utilization of the intervention is not sufficient as the sole downstream outcome.

The existence of `Y` is necessary but does not establish the C09 causal bridge.

## 4. D5 — Mechanism-identification gate

D5 is no longer a single generic causal-identification check. It is a structured gate with four questions.

### D5.0 — Mechanism architecture exists

The dataset must contain at least one credible design feature capable of separating the accessibility pathway from alternative treatment pathways.

Preferred architectures, in descending strength, are:

1. **Separate randomization / factorial mechanism design** — accessibility-producing component is independently randomized from other intervention components.
2. **Two-stage / encouragement design** — `Z` changes `ΔT_acc`, with a defensible exclusion restriction or equivalent design argument excluding direct effects of `Z` on `Y` except through `ΔT_acc`.
3. **Mechanism-specific natural experiment** — exogenous variation changes the structural accessibility state while leaving competing treatment channels unchanged or explicitly controlled by design.
4. **Principal-stratification architecture** — causal effects are identified or bounded within strata defined by potential accessibility states/compliance, without treating observed post-treatment `T_acc` as if randomized.
5. **Interventional mediation architecture** — mediator/outcome confounding is sufficiently measured and the estimand is an explicitly defined interventional mediated effect rather than an unsupported natural indirect effect.
6. **Partial-identification / bounding architecture** — direct and mediated effects cannot be point identified, but scientifically meaningful bounds on the accessibility-mediated contribution can be constructed.

A simple regression of `Y` on observed `ΔT_acc`, including adjustment for baseline covariates, is **not** a D5 mechanism-identification architecture by itself.

### D5.1 — First-stage identification

There must be a defensible causal estimate of:

`Z → ΔT_acc`

including a clear definition of the structural mediator and its estimand.

The first stage must not merely reproduce treatment assignment.

### D5.2 — Bridge identification

There must be a defensible strategy for estimating, identifying or bounding the contribution of `ΔT_acc` to `Y` while accounting for the fact that `ΔT_acc` is post-treatment.

At least one of the following must be available:

- independently randomized accessibility component;
- valid instrument/encouragement with explicit exclusion restriction supported by design or strong institutional evidence;
- principal-stratum causal estimand with identifiable/bounded interpretation;
- interventional mediated effect under explicitly stated and defensible assumptions;
- controlled/direct/mediated effect with sufficient path-blocking variables;
- informative partial-identification bounds that distinguish a nontrivial mediated contribution from zero/direct-only explanations.

The identification assumptions must be stated explicitly and must be testable where possible.

### D5.3 — Alternative-pathway audit

The candidate must enumerate the principal post-treatment pathways through which `Z` can affect `Y` other than `ΔT_acc`.

Examples include:

- complementary infrastructure;
- information or training;
- staffing/resources;
- prices/income/transfers;
- institutional or organizational change;
- behavioural adoption/use;
- spillovers/interference;
- selection/compliance changes;
- simultaneous treatment components.

For each material pathway the public data/design must provide one of:

`blocked by design | separately randomized | measured and adjusted under stated assumptions | bounded | remains unresolved`.

A candidate with a material unresolved direct pathway cannot receive a D5 PASS merely from a positive total treatment effect.

### D5.4 — Causal-bridge classification

D5 receives one of four statuses:

**D5-A — IDENTIFIED**  
The accessibility-mediated estimand is identified under a defensible design/assumption set, with alternative pathways addressed.

**D5-B — BOUNDED / ASSUMPTION-EXPLICIT**  
Point identification is unavailable, but the accessibility-mediated contribution is bounded or identified within a clearly defined principal/interventional stratum, and the bounds/assumptions materially constrain the causal interpretation.

**D5-C — DIAGNOSTIC ONLY**  
The dataset supports first-stage evidence and a useful mediator diagnostic (including IV/Wald diagnostics), but causal interpretation of `ΔT_acc → Y` is not authorized because exclusion, sequential ignorability or equivalent assumptions remain unresolved.

**D5-FAIL — TOTAL EFFECT ONLY**  
The dataset establishes `Z → Y` and possibly `Z → ΔT_acc`, but provides no credible mechanism-identification architecture for separating the accessibility bridge from direct/alternative pathways.

For ordinary C09 candidate admission, **D5-A or D5-B is required**. D5-C is informative but does not admit the candidate. D5-FAIL rejects it.

## 5. D6 — Provenance and admission

Every variable required for `Z`, `T_acc,0`, `T_acc,1`, `ΔT_acc`, the stable-unit linkage, `Y`, and the D5 mechanism-identification architecture must have public provenance, reproducible construction and persistent source identity.

D6 must also verify that the specific mechanism-identification variables are public. A candidate cannot pass D6 if the causal bridge depends on restricted treatment-assignment, service-area, compliance, mediator, outcome or administrative records.

Candidates failing D0–D6 are rejected without preflight, controlled execution or TR-132 admission.

## 6. Mandatory discovery table — refined

Every screened dataset is recorded using these core fields:

| Dataset | Unit | t0 | t1 | Structural S0 | Structural S1 | Z | ΔT_acc | Y | Mechanism architecture | Alternative paths | Public? | D5 status | C09 potential |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Additional notes may be added, but these fields must not be removed or collapsed.

## 7. Early-stop rules

Reject immediately when any of the following is established:

- no public unit-level core data;
- no stable unit linkage;
- no observable/reconstructible `T_acc,0` and `T_acc,1`;
- `T_acc` collapses into treatment assignment/realization;
- `T_acc` is defined using post-treatment behaviour, adoption or outcome;
- downstream `Y` is merely intervention use;
- no mechanism-identification architecture exists;
- `ΔT_acc` is post-treatment and no valid identification/bounding strategy exists;
- material direct/alternative pathway remains unresolved and cannot be bounded;
- the apparent mediator effect is only a regression/association;
- the only available result is `Z → Y` total treatment effect;
- required provenance depends on restricted, licensed or embargoed core data.

Do not continue a candidate after a definitive early-stop failure.

## 8. Interpretation discipline

The protocol does not require `T_acc,1` to be unaffected by `Z`. The requirement is that `T_acc` be an independently defined structural representation whose change can be measured rather than simply recoding treatment status.

The key distinction is now explicit:

`Z → Y`  ≠  `Z → ΔT_acc → Y`.

Likewise:

`Z → ΔT_acc` + `Z → Y`  ≠  causal identification of `ΔT_acc → Y`.

A mediator diagnostic may be reported where scientifically useful, including IV/Wald diagnostics. It must be labelled **diagnostic only** unless the D5 assumptions authorize causal interpretation.

Principal stratification may be used to avoid pretending that an observed post-treatment mediator is randomized; however, the resulting estimand must be reported as a principal-stratum effect or bound and must not be silently generalized to the full population. The mediation literature explicitly recognizes that post-treatment mediators are not generally randomized and that principal stratification can relax the sequential-ignorability problem, while identification may remain model-dependent or partial. citeturn0search0turn0search1

Interventional mediation estimands may be considered when natural indirect-effect assumptions are too strong, especially with multiple or post-treatment confounding, but the assumptions and estimand must be made explicit. citeturn0search3turn0search12

## 9. Implication for the current dataset-first search

Repeated D5 failures are now treated as evidence about **search architecture**, not as a reason to keep testing ordinary RCT datasets.

Future D0 searches must preferentially rank datasets containing one of the following structural signatures:

- factorial/separate randomization of the accessibility-producing component;
- encouragement designs with a credible exclusion restriction;
- independently randomized infrastructure/accessibility intensity;
- multiple intervention arms that isolate the structural component;
- explicit principal-stratification/compliance data;
- repeated mediator measurements plus rich baseline covariates enabling interventional effects;
- design features supporting informative bounds on direct versus accessibility-mediated effects.

Datasets with only:

`RCT → structural access change → outcome`

but no mechanism-separation architecture should be screened out at D5 without attempting ad hoc mediation regressions.

## 10. Relation to C09 Gate 002

This refinement preserves the decisions of `TGCV_C09_CANDIDATE_CLASS_DECISION_GATE_002`:

- retrospective candidate loop: CLOSED;
- controlled/synthetic C09 route: CLOSED;
- directed paper-by-paper candidate loop: CLOSED;
- new route: DATASET-FIRST DISCOVERY FOR ONE REAL-WORLD CASE.

It changes only the **search/admission criterion for the causal bridge** so that the next dataset search actively targets mechanism-identification architectures.

C09 remains an open, untested real-world causal claim. This protocol does not upgrade any TGCV claim, Core, RMA, Evidence Matrix or STATUS.

## 11. Next operation

Restart D0 ranking from the existing public-dataset universe, but apply a new priority filter:

`mechanism-identification architecture first → structural transition → stable unit → downstream trajectory → causal bridge`.

Do not continue broad screening of ordinary RCTs whose only identification is `Z → Y`.
