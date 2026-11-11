# Reconciliation matrix — Interactive Prototype sequentiality contract 001

- **Status:** DESIGN REVIEW / HISTORICAL RECONSTRUCTION.
- **Date:** 2026-10-14.
- **Purpose:** map the proposed sequentiality contract to the extant engine contract (PR #45) and UI development (PR #63) before implementation.
- **Scope:** inspection of GitHub artifacts only. No code or test execution is claimed here.
- **Decision:** reuse compatible work; implement only gaps confirmed below.

## 1. Historical artifacts inspected

| Artifact | Observed state | What it already provides | What it does not establish |
|---|---|---|---|
| Engine contract, [PR #45](https://github.com/jcarmonabastida-pixel/TGCV/pull/45) | Open draft; proposal, not frozen | Finite deterministic directed graph; initial state; scenario disablement; state-local enabled transitions distinct from system-level T_acc; reachable states; bounded trajectory enumeration; deterministic traversal conventions; descriptive and guarded-relation profiles; canonical input/result hashing; reproducibility fixtures and cross-runtime expectations | Temporal prerequisite requiring an earlier occurrence in the same sequence; user-facing named transformations; concrete selected-and-executed sequence distinct from enumerated possibilities; visual intervention authoring; immutable run history beyond existing input/result packages; outcomes/observer evaluations |
| Browser UI, [PR #63](https://github.com/jcarmonabastida-pixel/TGCV/pull/63) | Open draft; required CI not assessed here | Browser graph visualization and layouts; visual state/edge editing; graph imports and image/OCR-assisted transcription with human review; advanced JSON; relationship editor; bounded scenario execution; package export/import assessment; status feedback | Form-first input using human-readable state names rather than technical IDs; transition names; UI to create and compare an intervention without editing model JSON; stepwise concrete execution trace; temporal dependencies; persistent in-app run history |
| Browser UI contract test in PR #63 | Existing test; not executed in this review | Graph editing/review, OCR failure handling and human review, run output, export/import and package integrity/replay assessment, layout and profile controls | New temporal-sequentiality and concrete-execution acceptance cases |
| Cross-runtime test suite in PR #63 | Existing substantial fixture suite; not executed in this review | Reproducibility and graph/intervention/guard/order/canonicalization/truncation cases | Temporal prerequisites, concrete execution records and immutable per-run provenance |

## 2. Requirement-by-requirement mapping

| New requirement | Existing coverage | Classification | Minimum next action |
|---|---|---|---|
| Preserve the distinction between T_acc and state-local enabled edges | Explicit in PR #45 and UI notice in PR #63 | REUSE / PRESERVE | Retain the boundary; do not reinterpret local enabled edges as T_acc. |
| Finite deterministic graph, reachability and bounded exploration | Engine contract and browser engine/tests exist | REUSE | Keep existing engine and fixtures as baseline; no replacement or new optimization without an observed real-use issue. |
| Ordered trajectory representation: state, transformation, state | PR #45 defines ordered finite trajectories; browser engine emits transition/state steps | PARTLY COVERED | Ensure output and tests assert every ordered step, not only path/count summaries. |
| Temporal dependency: transformation B requires A to have occurred earlier in the same sequence | Current profile-2 guard is scenario-level global disablement based on whether A is explicitly disabled; it is not temporal | GENUINE SEMANTIC GAP | Add a separately versioned rule/schema profile. Do not reinterpret profile 2. Add satisfied, unsatisfied, repeated and cyclic-sequence fixtures first. |
| Applicability only when current state matches transition source | Implicitly enforced by traversal from the current graph state | COVERED FOR GRAPH PROFILE | Reuse; add an explicit acceptance assertion if the existing tests do not already assert it. |
| Named transformations separate from technical IDs | Schema v001 contains only id/source/target; UI asks for a state ID and generates edge IDs | UX / SCHEMA GAP | Generate IDs automatically and add editable display names. Decide whether display names are semantic or presentation-only and document their hash policy. |
| Build a small model without JSON | PR #63 has visual graph editing, but exposes advanced JSON and asks for state IDs | PARTLY COVERED | Make a name-based form the default; retain JSON only as advanced import/export. |
| Create an intervention and compare it with baseline in the UI | Engine accepts declared scenarios; UI can select/render them, but intervention authoring remains in model data | UI GAP | Add visual “create intervention from baseline”, initially disabling one transformation; do not mutate the base model. |
| Distinguish possible trajectories from trajectories actually executed | Current engine enumerates possible paths; no separately selected and stepwise executed-sequence record is established in inspected UI | GENUINE FUNCTIONAL GAP | Add a concrete execution action and ordered event record. Enumeration must never be labeled execution. |
| Preserve run configuration and provenance | Reproducible input/result packages and hashes already exist | PARTLY COVERED | Reuse package machinery; ensure each run retains an immutable configuration snapshot and intervention identity, without overwriting earlier records. |
| Explain a blocked step or unmet dependency | Validation and scenario guard diagnostics exist; temporal failure does not | GENUINE GAP FOR NEW RULE | Add a typed failure reason tied to step index and unmet prerequisite. |
| Explicit truncation warnings | Covered by contract and existing fixtures | REUSE | Preserve exact boundary rules; comparisons must flag incomplete results. |
| Outcomes and contextual observer evaluation | Not defined as a separate operational layer in the inspected artifacts | DEFERRED | Do not implement in this gate; specify only after sequentiality passes reproducible tests. |
| Value is not an automatic consequence of expanding transformations | Existing drafts avoid scientific overclaim and do not define a value reward | REUSE / PRESERVE | Keep the boundary visible; no reward/value score in this iteration. |
| Preserve performance baseline | Instrumentation and benchmarks exist in PR #63 | REUSE | No new performance campaign absent an observed real-use problem. |
| OCR/image import | PR #63 already supports OCR-assisted text extraction and graph-draft conversion with review | REUSE AS SECONDARY PATH | Keep separate from this gate; do not make image recognition a prerequisite or change the structural detector here. |

## 3. Semantic collision to avoid

The current relation_guarded_graph v1 uses a relation type called requires_transition_enabled to derive an effective scenario-level disablement when a prerequisite transition ID is explicitly present in the scenario's disabled_transitions. It does not check whether the prerequisite was executed earlier in a sequence.

The new rule “must have occurred before in the same trajectory” is temporally stronger and semantically different. It must receive a new, explicitly named/versioned profile or schema extension. Historical profile-2 behavior and fixtures remain unchanged; they must not be silently reinterpreted.

The UI and output must also distinguish:
- **Possible sequence / explored trajectory:** generated by bounded exploration.
- **Executed sequence / execution trace:** one selected sequence actually stepped through and recorded.

Both may use the same ordered state/transition representation, but require different execution/provenance types.

## 4. Smallest implementation plan after this review

### Gate A — contract clarification (no engine changes)
1. Review the temporal dependency profile name/version and exact rules for repeated transformation IDs, cyclic models and prerequisite satisfaction.
2. Decide how to canonicalize display names versus semantic IDs, so renaming a label cannot silently change semantic identity.
3. Define an immutable run record: canonical model, scenario/intervention, rule profile/version, initial state, limits, engine version, ordered result/trace, truncation and validation outcomes.
4. Specify deterministic exploration order and the difference between exploration records and concrete execution records.

### Gate B — focused synthetic tests
Add tests first for:
- a linear sequence with exact ordered steps;
- a transition attempted from the wrong current state;
- a temporal dependency satisfied only after its prerequisite appears earlier in the same sequence;
- the same dependency unsatisfied at the point of use, with a clear blocked-step explanation;
- intervention disabling a transition without mutating baseline;
- descriptive relation addition leaving execution unchanged;
- replay of identical input producing identical canonical output;
- distinct baseline/intervention snapshots remaining available after both runs;
- explicit truncation, never presented as exhaustive;
- browser/Python parity if both runtimes implement the new profile.

### Gate C — smallest UX slice
1. Default form: add/edit state names; add/edit named transformation with source/destination selectors.
2. Select initial state.
3. Run baseline exploration.
4. Create intervention by disabling one transformation.
5. Compare outputs.
6. Select and step through a concrete sequence; label it “executed” only when its trace is recorded.
7. Keep graph/image import and advanced JSON as optional alternate entry points.

### Gate D — evidence and promotion
- Run only relevant authorized CI on a development branch after tests and implementation exist.
- Report exact workflow run IDs and results; do not infer PASS from a draft or static inspection.
- Keep main untouched until contract, UI, browser and cross-runtime gates pass and promotion is explicitly chosen.

## 5. State after reconciliation

- Existing finite graph/reachability/enumeration engine: **REUSE CANDIDATE; historical draft, not accepted by this review**.
- Existing UI graph editing/import/OCR/package support: **REUSE CANDIDATE; PR #63 remains draft**.
- Temporal within-sequence dependencies: **OPEN; distinct from profile-2 scenario guard**.
- Concrete executed sequence and immutable run history: **OPEN / not demonstrated in inspected UI**.
- Form-first UX with human-readable names: **OPEN / partial visual editing exists**.
- Outcomes and contextual value evaluation: **DEFERRED**.
- Scientific core: **UNCHANGED**.
- Scientific execution and real-data use: **NOT AUTHORIZED**.
- This matrix: **historical reconstruction and design mapping only; no tests executed**.
