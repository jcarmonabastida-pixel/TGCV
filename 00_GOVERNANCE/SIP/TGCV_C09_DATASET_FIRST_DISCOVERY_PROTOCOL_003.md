# TGCV C09 — Dataset-First Discovery Protocol 003

**Date:** 2026-09-14  
**Status:** FROZEN — EARLY D6 FEASIBILITY GATE ADOPTED; D5 MECHANISM-IDENTIFICATION GATE RETAINED  
**Supersedes:** `TGCV_C09_DATASET_FIRST_DISCOVERY_PROTOCOL_002.md` for future C09 discovery  
**Scope:** C09 real-world candidate discovery only

## 1. Purpose

Refine the dataset-first discovery route after repeated D5 failures and the recent discovery that a candidate can satisfy D0–D5 structurally yet fail late because the unit-level data required for reproducible execution are not publicly accessible.

The discovery process must therefore test **public-data feasibility early**, before investing substantial screening effort in D1–D5, while retaining the full D6 provenance/admission gate before candidate admission.

The protocol now distinguishes:

- **D6-E — Early D6 feasibility:** rapid verification that the public unit-level data needed for the likely C09 causal test exist and are accessible.
- **D6 — Full provenance/admission:** final verification that every variable and mechanism-identification input required by the admitted causal design is publicly reproducible.

This is a search-efficiency refinement, not a relaxation of the admission standard.

## 2. Strategic decision

The adopted route is now:

`public dataset → early public-data feasibility → stable unit → structural state transition → intervention → downstream trajectory → mechanism-identification architecture → causal bridge → full provenance/admission`

A dataset is not a strong C09 candidate merely because it contains a randomized intervention, pre/post accessibility measure and downstream outcome. If the same intervention simultaneously changes multiple post-treatment channels and there is no design or identification strategy capable of separating them, the candidate fails D5.

Likewise, a candidate must not be taken through a detailed D1–D5 analysis when the required unit-level core data are already demonstrably unavailable, restricted or non-reproducible.

## 3. D0–D6 pipeline

### D0 — Dataset universe

Search trusted public repositories and archives first, including openICPSR/AEA Data and Code, Harvard Dataverse, World Bank reproducibility resources, Zenodo and equivalent public repositories.

The core data required for the C09 test must be publicly accessible and reproducible. Public code alone is insufficient.

### D0 priority filter — mechanism-separation architecture first

Before investing in the full D1–D5 screen, the D0 ranking must preferentially select datasets with at least one credible mechanism-separation signature:

1. **Factorial / separate randomization** of the accessibility-producing component and one or more competing intervention components.
2. **Multiple intervention arms** in which the structural accessibility component can be isolated from complementary treatment components.
3. **Encouragement / two-stage design** in which the encouragement changes structural accessibility while direct effects on `Y` can plausibly be excluded or bounded.
4. **Independently randomized infrastructure/accessibility intensity** rather than only a binary treatment indicator.
5. **Explicit principal-stratification/compliance architecture**, with public data sufficient to define the relevant strata or bounds.
6. **Repeated mediator measurements plus rich baseline covariates** supporting an explicitly interventional mediated estimand.
7. **Design features supporting informative partial-identification bounds** that constrain direct versus accessibility-mediated effects.

A dataset with only the signature `RCT → structural access change → outcome`, but no plausible mechanism-separation architecture, is **low priority** and should normally be screened out at D0/D5 rather than subjected to ad hoc mediator regressions.

The D0 priority filter is a ranking/admission heuristic, not itself evidence that D5 will pass. D1–D6 remain mandatory for candidate admission.

### D6-E — Early public-data feasibility gate

Immediately after D0 discovery/ranking, and **before detailed D1–D5 screening**, perform a bounded feasibility check of the public data required for the most plausible C09 reconstruction.

D6-E is deliberately narrower than final D6. Its purpose is to answer one operational question:

> **Can the public source actually provide the unit-level observations needed to reconstruct a stable unit, structural state transition, intervention, downstream trajectory and the likely mechanism-identification variables?**

The check must verify, at minimum:

1. **Public core data exist:** the dataset itself is downloadable or otherwise directly accessible without private credentials, special institutional access or case-by-case author approval.
2. **Unit-level granularity exists:** the public files contain observations at the unit level required by the candidate design, rather than only aggregate tables, published coefficients or replication summaries.
3. **Stable linkage is feasible:** the public data expose a persistent unit identifier or an explicit reproducible linkage key sufficient to connect the relevant periods.
4. **Likely structural variables are public:** candidate variables for `T_acc,0` and `T_acc,1` are present or demonstrably reconstructible from public files.
5. **Intervention/assignment is public:** the relevant `Z` or assignment/exposure variables are present at the required unit level.
6. **Downstream outcome is public:** the principal `Y` required by the likely C09 estimand is present at the required unit level and horizon.
7. **Mechanism variables are public:** the variables needed by the apparent D5 architecture — for example separate factorial arms, compliance, encouragement, component assignments, mediator measurements or principal-stratum variables — are public if the design depends on them.
8. **Access conditions are reproducible:** the source has a persistent identity/version or equivalent provenance sufficient to freeze the input later.

D6-E must **not** require the full D5 causal analysis. It is a data-availability feasibility screen only.

### D6-E statuses

**D6-E PASS** — the required public unit-level core appears accessible and sufficiently granular for a meaningful D1–D5 screen.

**D6-E CONDITIONAL** — the core is public but one or more required variables/linkages need a narrowly bounded verification during D1; continue only when the missing item is plausibly present in the same public source.

**D6-E FAIL** — the core unit-level data, stable linkage, principal `Z`, principal `Y`, or essential mechanism-identification variables are definitively restricted, embargoed, proprietary, aggregate-only or otherwise unavailable for reproducible public reconstruction.

**D6-E UNKNOWN** — public availability has not yet been established. Do not perform an extended D1–D5 analysis. Perform only a targeted availability verification; if it cannot be resolved promptly, mark the candidate low priority and move on.

### Early-stop rule for D6-E

If D6-E FAIL is established, **reject immediately**. Do not continue to D1–D5.

If D6-E UNKNOWN, perform only the minimum targeted provenance/data-availability search needed to resolve it. Do not infer public availability from the existence of a paper, replication code, supplementary tables, a secure repository statement, or public aggregate statistics.

A statement such as “data are available in a secure repository” is **not D6-E PASS** unless the repository and downloadable unit-level files are actually identified and accessible under the protocol's public-data conditions.

### D1 — Structural transition

The dataset must permit observation or reconstruction for the same stable unit of a structural state transition `S_0 → S_1` with an independently defined accessibility/capability representation `T_acc,0` and `T_acc,1`, hence bounded `ΔT_acc`.

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

## 4. D5 — Mechanism-Identification Gate

D5 is now an explicit **Mechanism-Identification Gate**, not a generic causal-identification check. It asks whether the dataset contains an architecture capable of separating or bounding the specific bridge `ΔT_acc → Y` from direct and alternative treatment pathways.

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

There must be a defensible causal estimate of `Z → ΔT_acc`, including a clear definition of the structural mediator and its estimand. The first stage must not merely reproduce treatment assignment.

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

Examples include complementary infrastructure, information or training, staffing/resources, prices/income/transfers, institutional or organizational change, behavioural adoption/use, spillovers/interference, selection/compliance changes and simultaneous treatment components.

For each material pathway the public data/design must provide one of:

`blocked by design | separately randomized | measured and adjusted under stated assumptions | bounded | remains unresolved`.

A candidate with a material unresolved direct pathway cannot receive a D5 PASS merely from a positive total treatment effect.

### D5.4 — Causal-bridge classification

D5 receives one of four statuses:

**D5-A — IDENTIFIED** — accessibility-mediated estimand identified under a defensible design/assumption set, with alternative pathways addressed.

**D5-B — BOUNDED / ASSUMPTION-EXPLICIT** — point identification unavailable, but accessibility-mediated contribution bounded or identified within a clearly defined principal/interventional stratum, with materially constraining assumptions.

**D5-C — DIAGNOSTIC ONLY** — first-stage evidence and mediator diagnostic available, but causal interpretation of `ΔT_acc → Y` not authorized because exclusion, sequential ignorability or equivalent assumptions remain unresolved.

**D5-FAIL — TOTAL EFFECT ONLY** — `Z → Y` and possibly `Z → ΔT_acc` established, but no credible mechanism-identification architecture for separating the accessibility bridge from direct/alternative pathways.

For ordinary C09 candidate admission, **D5-A or D5-B is required**. D5-C is informative but does not admit the candidate. D5-FAIL rejects it.

## 5. D6 — Full Provenance and Admission Gate

D6 remains mandatory after D1–D5. It is the final provenance and reproducibility gate, not the first public-data feasibility check.

Every variable required for `Z`, `T_acc,0`, `T_acc,1`, `ΔT_acc`, stable-unit linkage, `Y`, and the D5 mechanism-identification architecture must have public provenance, reproducible construction and persistent source identity.

D6 must verify that the **specific mechanism-identification variables actually used in the final estimand** are public. A candidate cannot pass D6 if the causal bridge depends on restricted treatment-assignment, service-area, compliance, mediator, outcome or administrative records.

D6 must also verify exact source versions, file identities, checksums where practicable, transformations and any licensing/embargo conditions relevant to reproducibility.

Candidates failing D0–D6 are rejected without preflight, controlled execution or TR-132 admission.

## 6. Mandatory discovery table — refined

Every screened dataset is recorded using these core fields:

| Dataset | D6-E | Unit | t0 | t1 | Structural S0 | Structural S1 | Z | ΔT_acc | Y | Mechanism architecture | Alternative paths | Public? | D5 status | D6 status | C09 potential |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Additional notes may be added, but these fields must not be removed or collapsed.

## 7. Early-stop rules

Reject immediately when any of the following is established:

- **D6-E:** no public unit-level core data;
- **D6-E:** no plausible stable linkage in the public source;
- **D6-E:** principal `Z` or principal `Y` is not publicly available at the required unit level;
- **D6-E:** essential mechanism-identification variables are restricted, embargoed, proprietary or aggregate-only;
- no stable unit linkage after D6-E;
- no observable/reconstructible `T_acc,0` and `T_acc,1`;
- `T_acc` collapses into treatment assignment/realization;
- `T_acc` is defined using post-treatment behaviour, adoption or outcome;
- downstream `Y` is merely intervention use;
- no mechanism-identification architecture exists;
- `ΔT_acc` is post-treatment and no valid identification/bounding strategy exists;
- material direct/alternative pathway remains unresolved and cannot be bounded;
- the apparent mediator effect is only a regression/association;
- the only available result is `Z → Y` total treatment effect;
- final D6 provenance depends on restricted, licensed or embargoed core data.

Do not continue a candidate after a definitive early-stop failure.

## 8. Interpretation discipline

The protocol does not require `T_acc,1` to be unaffected by `Z`. The requirement is that `T_acc` be an independently defined structural representation whose change can be measured rather than simply recoding treatment status.

The key distinction is explicit:

`Z → Y` ≠ `Z → ΔT_acc → Y`.

Likewise:

`Z → ΔT_acc` + `Z → Y` ≠ causal identification of `ΔT_acc → Y`.

A mediator diagnostic may be reported where scientifically useful, including IV/Wald diagnostics. It must be labelled **diagnostic only** unless D5 assumptions authorize causal interpretation.

## 9. Implication for the current dataset-first search

The recent Uttar Pradesh WASH factorial candidate demonstrated why D6 must be checked early: its D0–D5 architecture was highly promising, but the unit-level experimental data required for reproducible execution were not established as publicly downloadable. Under Protocol 002 this was discovered only after a detailed screen; under Protocol 003 the same candidate would receive D6-E FAIL/UNKNOWN before extended D1–D5 effort.

Future D0 searches must therefore apply the following ordering:

`mechanism-separation architecture + early public-data feasibility → structural transition → stable unit → downstream trajectory → causal bridge → full provenance`

The early D6 gate does **not** replace D0 mechanism prioritization or D5 causal-bridge analysis. It prevents expenditure of screening effort on candidates whose required public data are unavailable.

## 10. Relation to C09 Gate 002

This refinement preserves the decisions of `TGCV_C09_CANDIDATE_CLASS_DECISION_GATE_002.md`:

- retrospective candidate loop: CLOSED;
- controlled/synthetic C09 route: CLOSED;
- directed paper-by-paper candidate loop: CLOSED;
- new route: DATASET-FIRST DISCOVERY FOR ONE REAL-WORLD CASE.

It changes only the **order and resolution of public-data feasibility checking**: a lightweight D6-E gate is moved immediately after D0, while the full D6 admission gate remains mandatory at the end.

C09 remains an open, untested real-world causal claim. This protocol does not upgrade any TGCV claim, Core, RMA, Evidence Matrix or STATUS.

## 11. Next operation

Restart D0 ranking from the existing public-dataset universe with the priority order:

`mechanism-separation architecture + D6-E feasibility first → structural transition → stable unit → downstream trajectory → causal bridge → full D6 provenance`.

Do not continue broad screening of ordinary RCTs whose only identification is `Z → Y` or whose unit-level core data fail D6-E.
