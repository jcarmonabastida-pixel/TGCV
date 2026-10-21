# Dual-graph first implementation plan 001

**Status:** implementation plan for review; no code changes authorized by this document.  
**Branch:** design/condition-evaluator-contract-001-20261021  
**Source basis:** `main:prototypes/collective_toy/web/index.html`, fetched file blob `6e79802dec5d399638757518dfd2c8b94214613d`. The GitHub fetch did not expose the current main HEAD commit; no commit SHA is claimed.  
**Design basis:** `MINIMAL_DUAL_GRAPH_DATA_CONTRACT_001.md`, `TGCV_GRAPH_DERIVATION_CONTRACT_001.md`, `TGCV_FIRST_DEMONSTRATION_CASE_001.md`, `DUAL_GRAPH_ADAPTATION_MATRIX_001.md`, and `DUAL_GRAPH_PERSISTENCE_CONTRACT_PROPOSAL_001.md`.

## 1. Objective

Deliver the smallest user-visible increment that demonstrates two different semantic views in sequence:

1. **Graph 1 — system:** retain the current state/transition graph, its editor, scenario selection, and execution behavior.
2. **Graph 2 — TGCV:** show a separately typed, explicitly illustrative transformation-space model with its own transformations, compatibility relations, before/after accessible sets, and trajectory results.

The increment must make clear that Graph 2 is not automatically inferred from Graph 1. No scientific claim, general TGCV inference, condition evaluator, or persistence migration is part of this increment.

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
- Do not route system-graph transitions into TGCV trajectories.

### B. Add an independent TGCV demonstration model

Introduce a separate in-memory object for the stipulated example:

- transformations: `a` (prepare), `b` (inspect), `c` (repair);
- before set: `T_acc_before = {a,b}`;
- before relation: `R_before = {(a,b)}`;
- interaction: `m`;
- explicit illustrative rule: add `c` and relation `(b,c)`;
- after set: `T_acc_after = {a,b,c}`;
- after relation: `R_after = {(a,b),(b,c)}`;
- delta: `ΔT_acc = {c}`;
- trajectory rule: a non-empty sequence is reachable only when each adjacent pair is in the declared compatibility relation and all transformations are in the corresponding accessible set.

The model must keep declared inputs separate from computed outputs. Do not call these transformations system states or treat `m` as an executable system transition.

### C. Add Graph 2 presentation after Graph 1

- Add a separate labelled section after the existing system-graph section, not a replacement for `#graph`.
- Use a separate SVG/container and renderer; do not reuse the system graph's node IDs, positions, or transition renderer as the TGCV graph.
- Show transformations and typed compatibility relations.
- Show before/interaction-rule/after and `ΔT_acc` in a compact, mobile-readable layout.
- Distinguish the pre-existing sequence `[a,b]` from the newly reachable sequence `[a,b,c]`.
- Add a persistent, visible label that this is an artificial illustrative example with stipulated inputs/rule, not empirical data or scientific validation.

### D. Derive, don't hardcode, displayed outputs

The example's declared inputs may be fixtures, but the displayed after-set, delta, and reachable sequences must be calculated by the explicitly displayed rule. The acceptance test should fail if the rule or fixture changes but the displayed outputs remain stale.

For the first increment, it is acceptable to keep the demonstration fixture local and non-editable if this is clearly labelled and the derivation is genuinely computed. User editing of TGCV objects is a later scope unless implementation review identifies it as necessary.

### E. Keep unrelated layers out of scope

- Do not change `runTemporalScenario`, `execute(m)`, `addDeltaReach`, the condition evaluator, the value dashboard, or the current execution package.
- Do not change the current schema or export format.
- Do not compute value or claim that `ΔT_acc` causes value.
- Do not introduce automatic system↔TGCV mapping. The first increment should explicitly state that the example is independent of the user's system model.

## 4. Acceptance matrix

| Grouped requirement | Evidence required |
|---|---|
| Graph separation | Browser acceptance shows the system graph first and a distinct TGCV graph second; the existing system graph remains functional |
| Semantic typing | TGCV objects are labelled transformations, compatibility relations, and interaction/rule—not system states or executable transitions |
| Before/after derivation | Computed output exactly matches `{a,b}`, `{a,b,c}`, and `ΔT_acc={c}` for the stipulated fixture |
| Trajectories | `[a,b]` is reachable before and after; `[a,b,c]` is newly reachable after; no sequence containing `c` is shown as reachable before |
| Provenance/limits | UI labels the fixture and rule illustrative/stipulated and makes no empirical or value-causality claim |
| Regression | Existing system graph loading, editing, scenario exploration, concrete execution, and export tests remain passing |
| Adversarial checks | Invalid relation endpoint is rejected; a transformation is not silently accepted as a system state; changed rule cannot leave old derived output presented as current |
| Performance/accessibility | No material regression in existing browser benchmark; labels remain understandable at mobile viewport widths |

Use one end-to-end test for the demonstration chain plus a small number of adversarial tests; do not create one test per sentence or duplicate coverage mechanically.

## 5. Implementation sequence after approval

1. Create a dedicated implementation branch from a freshly verified main revision.
2. Add the independent fixture/model and pure derivation functions.
3. Add the second graph section and renderer.
4. Add the grouped end-to-end and adversarial browser tests.
5. Run the relevant existing CI checks; report synthetic/software conformance separately from scientific validity.
6. Review the rendered behavior and CI evidence before any promotion. Keep main unchanged until a separate promotion decision.

## 6. Out of scope / explicit non-actions

This plan does not authorize:
- any code change by itself;
- modifications to `main`;
- condition-evaluator implementation or schema migration;
- dual-graph import/export implementation;
- a general empirical method for identifying real accessible transformations;
- scientific execution, TGCV Core changes, or value-causality claims.

## 7. Review decision requested

Review whether this scope is correct: a separately rendered, computed, illustrative TGCV graph placed after the existing system graph, with no automatic mapping and no changes to execution, conditions, value assessment, or persistence.

Only after that decision should implementation begin.
