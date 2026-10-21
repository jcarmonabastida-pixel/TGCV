# Dual-graph first implementation plan 001

**Status:** scope approved by user; implementation tracked in [PR #91](https://github.com/jcarmonabastida-pixel/TGCV/pull/91). This document describes the approved target; code acceptance remains gated on CI and rendered behavior.  
**Branch:** design/condition-evaluator-contract-001-20261021  
**Source basis:** `main:prototypes/collective_toy/web/index.html`, fetched file blob `6e79802dec5d399638757518dfd2c8b94214613d`. The GitHub fetch did not expose the current main HEAD commit; no commit SHA is claimed.  
**Design basis:** `MINIMAL_DUAL_GRAPH_DATA_CONTRACT_001.md`, `TGCV_GRAPH_DERIVATION_CONTRACT_001.md`, `TGCV_FIRST_DEMONSTRATION_CASE_001.md`, `DUAL_GRAPH_ADAPTATION_MATRIX_001.md`, and `DUAL_GRAPH_PERSISTENCE_CONTRACT_PROPOSAL_001.md`.

## 1. Objective

Deliver the smallest user-visible increment that demonstrates two different semantic views in sequence:

1. **Graph 1 — system:** retain the current state/transition graph, its editor, scenario selection, and execution behavior.
2. **Graph 2 — TGCV:** show a separately typed, explicitly illustrative transformation-space model with its own transformations, compatibility relations, before/after accessible sets, and trajectory results.

Both graphs start empty. One `Cargar ejemplo` action loads a single integrated illustrative case into both views. The cross-layer mapping is explicit and specific to that teaching fixture; it is not a universal rule for arbitrary user systems. No scientific claim, general TGCV inference, condition evaluator, or persistence migration is part of this increment.

## 2. Current source anchors

Verified in the inspected browser entry file:

- System graph container: SVG `#graph`; explanatory text `#graph-note`.
- System graph renderer: `draw(m,r,sid)`, around line 125.
- Scenario selector: `#which`.
- System editor: `#model`, `#edge-source`, `#edge-target`, `#transition-review-list`, and the existing state/transition actions.
- Exploration/execution: `runTemporalScenario`, `execute(m)`, `addDeltaReach(m,result)`, and `run()`.
- Current export button: `#export`; package is built from `lastPackage` in `run()` and serialized by the export click handler near the end of the file.
- The source notice explicitly states that the current prototype does not itself implement canonical TGCV `T_acc`.

These are integration anchors, not instructions to refactor the existing system engine.

## 3. Proposed first increment

### A. Preserve Graph 1

- Keep the current system model and rendering behavior unchanged.
- Rename or clarify the section title and help text only if needed to make its system-state/transition meaning explicit.
- Keep scenario selection and condition warning behavior as-is.
- Do not silently map arbitrary user-provided system graphs into TGCV. The example-only mapping rule applies only to the bundled integrated fixture.
- Do not change `runTemporalScenario`, `execute(m)`, `addDeltaReach`, the condition evaluator, the value dashboard, or the current execution package.

### B. Load one integrated example into both models

- Initial state: no model is preloaded; both graph canvases are empty.
- The existing `Cargar ejemplo` action loads the system fixture and its matching TGCV view together.
- For this illustrative fixture only, each system transition `t` has a corresponding TGCV transformation `tau_t`, recorded in an explicit mapping record with provenance `illustrative` and named rule `each-system-transition-to-one-transformation-v1`.
- TGCV compatibility relations are derived from sequentially composable system transitions: a transition pair is compatible when the first transition's target equals the second transition's source. This is a declared teaching rule, not a universal TGCV inference.
- The before view uses the existing `block_ac` scenario; the after view uses `baseline`. For this fixture, a transformation belongs to scenario `T_acc` only if its system transition occurs in at least one trajectory enumerated by the existing system engine for that scenario. This distinguishes reachable transitions from transitions that are merely not disabled. The set difference is calculated as `ΔT_acc`, rather than hardcoded.
- The before set is `{tau_t_ab, tau_t_bd}`; the after set is `{tau_t_ab, tau_t_ac, tau_t_bd, tau_t_cd}`. Thus `ΔT_acc={tau_t_ac, tau_t_cd}`: enabling `A→C` also makes downstream `C→D` occur in an enumerated trajectory. The trajectory test distinguishes `[tau_t_ab, tau_t_bd]` from `[tau_t_ac, tau_t_cd]`; the latter becomes reachable only in the after scenario.

The model must keep declared inputs and explicit mappings separate from computed outputs. TGCV transformations are not system states, and the scenario switch `m` is illustrative rather than an executable system transition.

### C. Add Graph 2 presentation after Graph 1

- Add a separate labelled section after the existing system-graph section, not a replacement for `#graph`.
- Use a separate SVG/container and renderer; do not reuse the system graph's node IDs, positions, or transition renderer as the TGCV graph.
- Show transformations and typed compatibility relations.
- Show before/interaction-rule/after and `ΔT_acc` in a compact, mobile-readable layout.
- Show the explicit mapping provenance and corresponding system scenario names.
- Add a persistent, visible label that this is one integrated artificial example, not empirical data or scientific validation.

### D. Derive, don't hardcode, displayed outputs

The integrated system model may be a fixture, but the displayed TGCV mapping, before/after sets, delta, and reachable sequences must be calculated from the explicit mapping rule and the two system scenarios. The acceptance test should fail if the fixture or rule changes but the displayed outputs remain stale. If the system model is edited after loading, the TGCV view must be marked stale rather than presented as a current correspondence.

For the first increment, it is acceptable to keep the demonstration fixture local and non-editable if this is clearly labelled and the derivation is genuinely computed. User editing of TGCV objects is a later scope unless implementation review identifies it as necessary.

### E. Keep unrelated layers out of scope

- Do not change the current schema or export format.
- Do not compute value or claim that `ΔT_acc` causes value.
- Do not apply the fixture's mapping rule to arbitrary user-provided systems. The loaded example's two views are intentionally integrated; after a user edits the system model, the TGCV view must be marked stale rather than silently remapped.

## 4. Acceptance matrix

| Grouped requirement | Evidence required |
|---|---|
| Graph separation | Browser acceptance shows the system graph first and a distinct TGCV graph second; the existing system graph remains functional |
| Semantic typing | TGCV objects are labelled transformations, compatibility relations, and interaction/rule—not system states or executable transitions |
| Integrated mapping | One load action renders both graphs from the same system fixture, with explicit illustrative mapping records |
| Before/after derivation | Scenario `T_acc` contains only transformations whose mapped system transitions occur in an enumerated trajectory; the fixture yields before `{tau_t_ab,tau_t_bd}`, after `{tau_t_ab,tau_t_ac,tau_t_bd,tau_t_cd}`, and `ΔT_acc={tau_t_ac,tau_t_cd}` |
| Trajectories | `[tau_t_ac, tau_t_cd]` is not reachable in `block_ac` and is reachable in `baseline`; the other branch remains consistent |
| Provenance/limits | UI labels the fixture and rule illustrative/stipulated and makes no empirical or value-causality claim |
| Regression | Existing system graph loading, editing, scenario exploration, concrete execution, and export tests remain passing |
| Adversarial checks | Invalid relation endpoint is rejected; a transformation is not silently accepted as a system state; changed rule cannot leave old derived output presented as current |
| Performance/accessibility | No material regression in existing browser benchmark; labels remain understandable at mobile viewport widths |

Use one end-to-end test for the demonstration chain plus a small number of adversarial tests; do not create one test per sentence or duplicate coverage mechanically.

## 5. Validation and acceptance sequence

1. Create a dedicated implementation branch from a freshly verified main revision.
2. Add the integrated fixture, explicit example-only mapping records, and pure TGCV derivation functions.
3. Add the second graph section and renderer.
4. Add the grouped end-to-end and adversarial browser tests.
5. Run the relevant existing CI checks; report synthetic/software conformance separately from scientific validity.
6. Review the rendered behavior and CI evidence before any promotion. Keep main unchanged until a separate promotion decision.

## 6. Out of scope / explicit non-actions

The implementation scope excludes:
- modifications to `main` except through a separately reviewed promotion decision;
- condition-evaluator implementation or schema migration;
- dual-graph import/export implementation;
- a general empirical method for identifying real accessible transformations;
- scientific execution, TGCV Core changes, or value-causality claims.

## 7. Review decision requested

Approved scope: both graphs start blank; one button loads the integrated example into both; the mapping is explicit and fixture-specific; changing the system model marks the TGCV correspondence stale. CI and rendered behavior remain acceptance gates.
