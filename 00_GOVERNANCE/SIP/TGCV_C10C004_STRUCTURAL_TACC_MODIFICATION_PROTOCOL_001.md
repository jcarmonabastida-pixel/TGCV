# TGCV C10C-004 — Structural T_acc Modification Protocol 001

**Date:** 2026-09-15  
**Case:** C10C-004 — Morocco microcredit randomized experiment  
**Source:** openICPSR Project 116333, V1  
**DOI:** 10.3886/E116333V1  
**Status:** **PROTOCOL — FROZEN FOR OPERATIONAL RECONSTRUCTION**  
**Supersedes:** C10C-004 OPERATIONAL MECHANISTIC RECONSTRUCTION 001 (mediation-first sequence)  
**Core/RMA:** Unchanged

## 1. Protocol decision

The primary route is changed from a mediation-first reconstruction to a **structural T_acc modification test**, adapted from the logic used in the KFGS structural intervention experiment.

The reason is methodological: C10C-004 contains randomized treatment assignment and longitudinal state observations, but the candidate mediator `client` and the administrative loan variables are sparse and do not constitute a clean causal mediation chain. Requiring a validated mediator would therefore add assumptions that are not necessary for the TGCV question.

The primary question becomes:

> Does randomized microcredit intervention produce a detectable modification in the structure of transformations accessible to households, beyond a simple change in endpoint state variables?

## 2. KFGS-derived principle adapted to Morocco

KFGS demonstrated the structural logic by holding conventional structural summaries fixed while changing relational structure through degree-preserving rewiring, then testing downstream consequences under common stochastic seeds.

C10C-004 cannot reproduce that intervention literally because the historical experiment randomized access to microcredit rather than graph structure. The transferable principle is therefore **not the rewiring procedure itself**, but the separation between:

1. conventional state summaries;
2. transformation-accessibility structure;
3. downstream realized trajectory/outcomes.

For Morocco, treatment is the randomized intervention and `T_acc` is reconstructed from a pre-specified representation of household capabilities/resources/constraints and their admissible transformations.

## 3. Primary TGCV object

For each household and relevant time point:

`T_acc = F(S,C,L)`

where `S` is the household state, `C` captures contextual/relational conditions and `L` captures relevant constraints/resources available to transformation.

The test seeks evidence that:

`T_acc,EL(treatment) ≠ T_acc,EL(control)`

conditional on an independently reconstructed baseline state and a frozen transformation/admissibility specification.

A stronger form is evidence for differential accessibility of particular transformation classes:

`τ ∈ T_acc,treated` while `τ ∉ T_acc,control`,

or the reverse, with the distinction defined independently of downstream outcome values.

## 4. Frozen methodological constraints

- No mediator is required for the primary test.
- `client` and `admin_*` remain auxiliary mechanism evidence only.
- No downstream outcome may be used to define the transformation universe or admissibility predicate.
- No post-hoc selection of transformations based on treatment differences.
- Baseline information used to define admissibility must be frozen before endline comparison.
- Treatment assignment remains the causal intervention; no causal interpretation is assigned to observed credit take-up itself.
- A change in an observed variable is not by itself accepted as `ΔT_acc`.
- A change in `T_acc` requires an explicit operational mapping from state/conditions to admissible transformations.
- No Core/RMA/claim update follows automatically from a PASS.

## 5. Operational sequence

### Step 1 — Baseline transformation-state reconstruction

Construct the pre-treatment household state representation `S_BL` and the contextual/constraint representation needed for transformation admissibility, using baseline variables only.

### Step 2 — Candidate transformation universe

Define, before inspecting treatment effects at endline, a finite and independently justified set of transformation classes relevant to the Moroccan household domain. Primary candidates include productive/economic activity, resource/material use, market/trade activity, mobility and agency-related transformations.

### Step 3 — Admissibility predicate

Specify `P_τ(S_BL,C_BL,L_BL)` for each candidate transformation class. The predicate must be reproducible from baseline information and must not contain endline outcomes or treatment-dependent quantities.

### Step 4 — Baseline `T_acc`

Compute the household-level baseline accessible-transformation structure:

`T_acc,BL = {τ : P_τ(S_BL,C_BL,L_BL)=1}`.

This step establishes the operational object before endline treatment comparison.

### Step 5 — Endline structural reconstruction

Using the same frozen transformation universe and the same operational definitions, reconstruct the corresponding endline accessibility structure from endline state/conditions.

### Step 6 — Treatment/control structural comparison

Estimate whether the intervention changes the accessibility structure beyond what is observed in controls, using the randomized matched design and the established linkage structure.

The primary comparison is structural, not a mediation coefficient.

### Step 7 — Robustness / negative controls

Test whether apparent structural differences disappear or materially weaken when the accessibility structure is replaced by appropriate conventional state summaries, permuted assignments, or other pre-specified negative controls.

### Step 8 — Trajectory linkage

Only after `ΔT_acc` has been independently established, test whether the structural modification is associated with differential subsequent transformation/trajectory. This is a downstream stage and is not needed to define `ΔT_acc`.

## 6. Role of credit variables

The previously reconstructed relation:

`treatment → client → admin_*`

is retained as **auxiliary mechanism evidence**.

The observed pattern — no clients in control and 435/2,741 treated households classified as Al Amana clients — establishes useful separation between treatment assignment and observed credit use, but the sparsity of administrative fields prevents it from being the primary evidential route.

## 7. Role of j1–j13

The `j1_*`–`j13` block is promoted from a possible mediator block to a **primary candidate source for transformation/accessibility definitions**.

Its variables potentially encode capabilities, decision authority, purchasing/production capacity, trading activity and mobility. These are relevant because the TGCV test asks whether the intervention changes the conditions under which subsequent transformations are accessible, not merely whether an endpoint score changes.

## 8. Gate structure

**G1 — Baseline operational sufficiency:** PASS required before defining endline `T_acc`.  
**G2 — Transformation-universe independence:** PASS required; no outcome-driven selection.  
**G3 — Admissibility predicate reproducibility:** PASS required.  
**G4 — Baseline `T_acc` reconstruction:** PASS required.  
**G5 — Endline `T_acc` reconstruction:** PASS required.  
**G6 — Structural treatment/control contrast:** primary scientific gate.  
**G7 — Negative-control / robustness support:** required for strong interpretation.  
**G8 — Downstream trajectory linkage:** optional subsequent gate after structural evidence.

A failure at G2 or G3 blocks scientific interpretation rather than being repaired by outcome-driven redefinition.

## 9. Interpretation boundary

A positive structural contrast will support the bounded statement that the randomized intervention is compatible with, and may causally induce, a modification of the operationalized transformation-accessibility structure under the frozen reconstruction.

It will **not** by itself establish:

- universal TGCV validity;
- a specific causal mediator;
- universal improvement in value;
- a specific `ΔT_acc` mechanism outside the operationalization;
- or any modification of the TGCV Core.

A null result will be treated as evidence against the particular operationalized structural hypothesis, not as automatic falsification of TGCV as a whole.

## 10. Current status

The protocol is now the primary route for C10C-004.

The previously planned temporal mediation step is **not executed** as the primary path.

**Next executable step:** **G1 — Baseline operational sufficiency / state reconstruction**, using baseline variables only and no endline treatment outcomes.
