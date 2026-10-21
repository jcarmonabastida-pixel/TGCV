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


## Follow-up verification — synchronized scenario view

**Status: implementation updated; CI verified on 2026-10-22.**

The functional gap above is addressed in the separate implementation branch `implementation/dual-graph-sync-002-20261022`, currently proposed as [draft PR #92](https://github.com/jcarmonabastida-pixel/TGCV/pull/92). This does not rewrite the historical finding: it records the follow-up disposition.

- The scenario selector now refreshes both graph views from the same model and engine result.
- The TGCV current-scenario view derives its transformations from mapped system transitions present in enumerated trajectories for the selected scenario.
- The before/after/ΔT_acc comparison remains a distinct derived comparison.
- Custom/edited models retain the stale-mapping guard rather than silently receiving the illustrative demo mapping.
- A grouped browser acceptance test covers `block_ac` (two accessible transformations), `baseline` (four), and preservation of the stale warning after re-execution of an edited model.

### CI evidence on exact PR head

Head commit: `609ebdd669abc8196b11ca7c7d9300e64c46029c`.

- [Governance consistency — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39688352410)
- [Synthetic engine tests — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39688352512)
- [Browser performance benchmark — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39688352538)
- [Browser and cross-runtime tests — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39688352445)

This is software/contract evidence only. It is not scientific validation of TGCV, the illustrative mapping rule, or any causal/value claim. PR #92 remains draft; no promotion or merge to `main` is implied.


## Rendered-interface review gate — pending

A follow-up inspection of the artifacts from the passing browser/cross-runtime workflow found the acceptance-package JSON and standalone executable distribution, but **no desktop or mobile screenshots**. The performance workflow provides a benchmark report, not rendered screenshots. Therefore the CI PASS results do not establish visual correctness or responsive usability.

A source-level inspection confirms that the page has a responsive single-column layout breakpoint at 760px and that the TGCV graph is a separate panel following the system graph. This is not a substitute for inspecting the rendered page. In particular, visual clarity of the selected-scenario label, transformation/relationship labels, comparison section, and graph clipping at narrow widths remains unverified.

**Disposition:** keep [draft PR #92](https://github.com/jcarmonabastida-pixel/TGCV/pull/92) in draft. Do not claim the visual review complete or promote to `main` until rendered desktop and mobile evidence is available and reviewed. No implementation changes were made in this documentation step.


## State labels inside node shapes — implementation update

The implementation branch now gives each system-state node a width based on its label (bounded to preserve graph spacing), aligns the label centrally inside the rectangle, adjusts transition endpoints to the corresponding node widths, and reduces font size for longer identifiers. SVG elements carry state-label/state-node identifiers for browser-level geometry assertions.

A grouped browser acceptance assertion checks that all four visible state labels in the integrated example are fully inside their corresponding node shapes. The change is in implementation branch `implementation/dual-graph-sync-002-20261022`, commit `42a17e3ec78f653b984db8015cb79ce7eed6aaa2`; fresh CI on this exact head is pending. This is a source/test-level change and does not by itself establish that long arbitrary names are visually ideal on every device. Review rendered desktop/mobile evidence after CI.


### Long-label acceptance refinement

The implementation width cap was increased from 112 to 140 SVG units to give longer state identifiers more room while keeping node width bounded. A new grouped browser adversarial case uses four long state names and verifies (1) every label's SVG bounding box is contained by its node, (2) label font size is at least 11px, and (3) no pair of node rectangles overlaps in the rendered layout. It then reloads the integrated demo to avoid leaking test state into later assertions.

Implementation head: `4144cad99863498a7cfe7adc61a68083eb85c7c7`. Fresh CI for this exact head is pending. These geometric checks are a useful regression gate, not a replacement for human review of screenshots on actual mobile and desktop viewports.
