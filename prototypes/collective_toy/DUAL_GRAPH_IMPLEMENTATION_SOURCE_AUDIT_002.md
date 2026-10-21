# Dual-Graph Implementation Source Audit 002

**Purpose:** focused source review of the integrated dual-graph implementation, following the user's approval of the separate visual concept preview.

**Reviewed implementation commit:** `a436ca36ecf60f55205af8cc264128ca5ef5ca80`  
**Repository:** `jcarmonabastida-pixel/TGCV`  
**Reviewed paths:**
- `prototypes/collective_toy/web/index.html`
- `prototypes/collective_toy/web/ui_contract_test.cjs`
- `prototypes/collective_toy/web/cross_runtime_test.cjs`

This is a source audit, not a claim that the deployed repository implementation has been manually inspected on a mobile device.

## Verified behavior

1. **Initial empty state.** At approximately line 415, the model textarea is initialized to an empty string, `syncGraphEditor()` runs, `clearTgcvDemo()` clears the TGCV SVG, and the status explicitly says both graphs are empty. The system SVG is not populated until an example is loaded or a model is executed.
2. **One integrated load action.** At approximately line 414, the `load` handler creates the integrated example, writes that same model to the editor, obtains one engine result via `execute(integrated)`, passes that result to `renderTgcvDemo(integrated, preview)`, and draws the system graph from the same result. The load action therefore does perform a scenario-engine computation needed for the TGCV derivation; it does not yet populate the full exploration/results workflow shown by the separate “Ejecutar escenarios” action.
3. **Explicit illustrative mapping.** `tgcvDemoFixture` (approximately lines 527–551) creates a mapping record for each example transition, labels it illustrative, derives consecutive-transition relations, and calculates scenario sets from transitions present in enumerated trajectories.
4. **Stale mapping warning.** `markTgcvStale` compares the edited model against the stored canonical snapshot and warns that the old TGCV view must not be treated as current. The browser contract test exercises this and verifies that reloading the integrated example restores the declared correspondence.
5. **Automated test scope.** The browser contract test covers initial blank state, integrated loading, mapping/derivation, invalid relation endpoints, and stale-mapping recovery. Existing CI evidence for commit `a436ca36ecf60f55205af8cc264128ca5ef5ca80` is recorded in `DUAL_GRAPH_FIRST_CI_VERIFICATION_001.md`.

## Functional gap found

The system graph's scenario selector handler (approximately line 527) only calls `draw(lastModel, lastPackage.result, $("which").value)`. It does not refresh the TGCV view. Meanwhile, `renderTgcvDemo` renders the fixed comparison between `block_ac` and `baseline`, with `T_acc` before, `T_acc` after, and `ΔT_acc`; it does not accept the currently selected system scenario as a view parameter.

Consequently, after the user runs the model and changes the system graph's selected scenario, the system graph can change while the TGCV graph continues to show the same fixed before/after comparison. The comparison remains internally labelled, but the two views are not dynamically synchronized around the selected scenario. The current tests do not establish that changing the system scenario updates the TGCV view.

## Recommended next increment

Make the scenario relationship explicit in the UI and acceptance contract. Preferred minimal behavior:
- retain the before/after/Δ comparison as a clearly labelled comparison, not as if it were the current selected scenario; and
- when the system scenario selector changes, either update a clearly separated “current scenario” TGCV view from the same scenario result, or clearly state that the TGCV panel is a fixed comparison and is not controlled by that selector.

The visual concept the user approved used a direct block/enable interaction that updates both views together. The actual implementation should match that interaction or explain the distinction visibly. Add one grouped browser acceptance test that changes scenario selection and verifies the declared cross-view behavior.

## Boundaries

- No files were modified by this audit.
- No changes to `main`, TGCV Core, scientific claims, persistence, or condition evaluation.
- Passing CI is software evidence, not scientific validation.
- Do not claim mobile visual inspection of the actual PR implementation without direct rendered evidence.
