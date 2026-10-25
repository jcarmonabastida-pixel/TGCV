# TGCV Collective Toy — full-chain demonstrator contract 001

- **Status:** DEVELOPMENT CONTRACT; not scientific validation and not a change to the TGCV scientific Core.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`.
- **Parent:** `dadc87c786fb0e8e5901fb2301bfa7c14d172c1f`.
- **Purpose:** turn the existing graph editor, synthetic engine, temporal profile, scenario comparison and replay package into one inspectable end-to-end demonstration.
- **Governance:** `main` remains unchanged. No real-data execution or scientific experiment is authorized by this contract.

## 1. Demonstration objective

A user must be able to enter or import a small system, inspect its model, define an intervention, derive and compare the model's accessible transformations under explicit prototype rules, execute an ordered sequence, inspect reachable states and trajectories, record outcomes separately from observer-contextual value, and export/replay the evidence package.

The demonstrator is successful only when each stage is connected by explicit, inspectable artifacts. A diagram that only enumerates graph paths is not the complete TGCV chain.

## 2. End-to-end stages and artifacts

1. **System and context input** — capture the system/state description and declared context/conditions. Input may be created visually or imported from JSON, DOT, Mermaid or GraphML. Image/OCR remains an optional draft-import route requiring human review.
   - Artifact: `system_model`, input provenance, schema/version.
2. **Transformations and relations** — define transformation IDs, source/target or declared pre/postconditions, and typed relations. Keep descriptive, scenario-availability and temporal-prerequisite semantics separate and versioned.
   - Artifact: `transformation_model`, relation list, rule profile/version.
3. **Accessible transformations** — calculate the prototype's accessible set under its explicit operational rules and selected scenario/context. Show why each transformation is accessible or blocked.
   - Artifact: `T_acc` candidate with rule trace and configuration hash.
   - Scientific boundary: this is a synthetic operational approximation for the demonstrator, not a claim that the current code implements the canonical scientific function (T_{acc}=F(S,C,L)).
4. **Baseline and intervention** — preserve a baseline configuration; represent each intervention as a separate immutable scenario/delta, never by overwriting the baseline.
   - Artifact: baseline/intervention IDs and hashes.
5. **Reachability change** — compute added/removed reachable states and accessible transformations for baseline vs intervention. Do not conflate `ΔReach` with a value score or causal effect.
   - Artifact: `delta_reach` with both source hashes and explicit truncation status.
6. **Possible trajectories** — enumerate bounded candidate paths with limits and a visible truncation indicator. This is exploration, not execution.
   - Artifact: `possible_trajectories`, bounds, complete/truncated status.
7. **Concrete ordered execution** — allow a user to select/enter an exact transition sequence. Validate each step against current state and the temporal-prerequisite profile. Preserve step order, success/block reason, state-before/state-after, and path-local prerequisite history.
   - Artifact: `execution_trace`, execution ID, input/configuration hash, trace hash. An attempted but blocked sequence must remain inspectable.
8. **Outcomes** — let the user record observed or synthetic outcomes with provenance, measurement unit, timing and uncertainty/status. Never infer an outcome merely from reachability or path count.
   - Artifact: `outcome_record`, linked to a specific execution/intervention.
9. **Observer-contextual value assessment** — capture observer, objective/criterion, context, valuation rule and rationale explicitly. Keep this as a separate assessment of an outcome, not a reward silently fed into the engine.
   - Artifact: `value_assessment`, linked to outcome and declared valuation protocol. If the user supplies no valuation, report “not assessed”; do not invent one.
10. **Audit and replay** — export a self-contained package containing schema/engine versions, source model, scenario/intervention, all stage artifacts, limits, hashes, provenance and scientific-boundary notices. Re-import must verify integrity and replay deterministic portions.
   - Artifact: versioned run package and integrity assessment.

## 3. Required UI walkthrough

The primary walkthrough must make the chain visible in this order:

`Model → T / R → T_acc → Intervention → ΔReach → Possible trajectories → Concrete execution → Outcome → Observer/context value → Audit/export`

Every stage shows its status: `NOT_RUN`, `PASS`, `BLOCKED`, `TRUNCATED`, `NOT_ASSESSED` or `ERROR`. Status must be derived from real stage results, not decorative labels.

The interface must distinguish:
- imported/edited model vs validated model;
- accessible transformations vs transformations merely declared in the model;
- possible trajectories vs a concrete executed sequence;
- an execution block vs a search bound/truncation;
- outcome observations vs observer-contextual value assessment;
- synthetic demonstration evidence vs scientific/empirical validation.

## 4. Minimum acceptance walkthrough

Use one hand-checkable synthetic model with at least two alternative routes and one temporal prerequisite. Run these checks:

1. Load or visually create the fixture; verify the declared state and transformation inventory.
2. Derive and display the accessible transformation set with reasons.
3. Run a baseline and a separate intervention; show added/removed accessible transformations and reachable states.
4. Enumerate possible trajectories and visibly mark any truncation.
5. Execute a valid ordered sequence and inspect each step and the trace hash.
6. Attempt a sequence missing a temporal prerequisite; it must stop at the exact step and state the missing requirement.
7. Record an outcome explicitly; verify it is linked to the execution, not inferred from graph metrics.
8. Assess value only after selecting an observer/context/criterion; absent inputs must yield `NOT_ASSESSED`.
9. Export and re-import the package; verify hashes and replay deterministic outputs.
10. Repeat the same model/configuration; semantic outputs must match while per-run execution IDs may differ.
11. Run historical profile-1/profile-2 compatibility tests; old profile semantics must remain unchanged.
12. Confirm that OCR output remains a human-reviewed draft and that no change to the structural graph detector is required for this work.

## 5. Implementation sequence

- **FC-0 — contract and artifact map:** this document.
- **FC-1 — engine/browser semantic alignment:** implement the explicitly versioned temporal profile in the browser engine, aligned with the tested Python contract; preserve profile 1 and profile 2.
- **FC-2 — accessible-transformation and intervention panel:** expose rule trace and baseline/intervention delta. Label any proxy/operationalization as prototype-only.
- **FC-3 — sequence execution panel:** exact ordered sequence, step-by-step validation, blocked-step explanation, immutable trace.
- **FC-4 — outcome and observer-context assessment:** separate data-entry layers and linked provenance; no implicit reward/value score.
- **FC-5 — run package and replay:** package schema, canonical hashes, import/integrity check, deterministic replay.
- **FC-6 — end-to-end CI:** browser and engine contract tests, historical compatibility, adversarial fixtures, clean-source replay, artifact inspection.
- **FC-7 — review gate:** audit the walkthrough and evidence. Promotion to `main` requires a separate explicit decision.

Implement one stage at a time. Do not combine unrelated fixes or optimize performance without evidence of a real-use problem.

## 6. Non-goals and scientific boundaries

- This work does not amend TGCV's scientific Core, settle open architectural proposals, or establish causality.
- It does not claim the prototype operationalization is the canonical scientific `T_acc=F(S,C,L)`.
- It does not derive value from `ΔReach`, trajectory counts or execution success.
- It does not use real Rust repositories, production datasets or other real-world data.
- It does not alter OCR/vision graph-structure detection.
- It does not promote code to `main` automatically.

## 7. Current implementation and acceptance status (2026-10-19)

The browser engine and Python reference implement the tested synthetic Full Chain path, including accessible-transformation exploration, baseline/intervention comparison, ordered execution, explicit outcomes, observer/contextual assessment, export/import, and deterministic replay. The numbered acceptance register and evidence bundle index document grouped contract and adversarial coverage.

The prior Full Chain candidate passed its five-workflow exact-HEAD gate. The clean promotion branch must independently pass the required five workflows on its own exact HEAD before promotion. No scientific execution or empirical TGCV validation is implied.

The image-to-graph route is an optional extension, not a Full Chain acceptance dependency. PaddleOCR performed better in the prior text-recognition evaluation; its integration and an OpenCV structural-detection feasibility comparison are assigned to a separate development branch. Arrow direction remains an acknowledged limitation and must not be silently inferred.

## 8.1 Approved package-stage and trace lifecycle policy (2026-10-15)

The owner approved Alternative A for FC-5/FC-6. This section is normative for the development contract; implementation and CI evidence remain outstanding.

### Package stage

Implemented on the development branch in versioned package schema `collective-toy-browser-run-002`. Its required `package_stage` is one of `EXPLORATION`, `EXECUTION`, `OUTCOME`, or `ASSESSMENT`. The importer derives the expected stage from the actual artifacts and rejects inconsistencies. The exporter emits v002; v001 remains supported under its historical contract and does not accept `package_stage`. See `FC5_FC6_PACKAGE_SCHEMA_V002_IMPLEMENTATION_001.md`.

### Artifact dependencies

- A stage snapshot containing model/input and exploration result may omit trace, outcome, and assessment when its stage explicitly indicates that execution has not yet occurred.
- An execution trace may be `COMPLETED` or `BLOCKED`; both must remain exportable and inspectable.
- A `COMPLETED` trace may exist without an outcome.
- An outcome record requires a `COMPLETED` trace and must link to the exact execution ID, trace digest, model and scenario.
- A `BLOCKED` trace must preserve the blocked-step/reason and last valid state coherently; it must not have an outcome or assessment representing a completed observation from that blocked execution.
- A value assessment requires a valid outcome and must link to that outcome and execution.
- If no value assessment exists, `value_assessment_status` must be `NOT_ASSESSED`, independently of whether execution occurred. It does not imply that no trace exists.
- Reject undocumented artifact combinations, contradictory statuses, malformed artefacts, and broken cross-links.

### Semantic distinctions

Exploration results (including reachable states and `delta_reach`) are not the same as a concrete execution's `outcome_record`. Therefore a stage snapshot may legitimately include model/exploration result without a concrete execution trace; this does not permit an explicit execution outcome without its completed trace.

### Integrity boundary

Hashes support integrity/consistency checks but do not establish provenance authenticity or prove that an event actually occurred. Keep provenance declarations explicit and do not overstate what package validation establishes.

### Implementation and acceptance gate

Schema v002, package-stage inference, and trace lifecycle validation have been implemented on the development branch; grouped tests cover the exploration-stage export, blocked-trace round-trip, and rejection of an outcome attached to a blocked trace. The prior Full Chain candidate passed its five-workflow exact-HEAD gate. The clean promotion candidate must pass the same gate before promotion. Preserve the historical v001 importer and profile 1/2 compatibility. This approval does not authorize scientific execution or promotion to `main`.


## 9. TGCV correspondence derivation — explicit contract decision (2026-10-22)

### Scope decision
General automatic discovery/learning of system transition rules is outside the current demonstrator scope. Deriving or proposing correspondences between the system graph and the TGCV transformation graph is a separate required capability and must not be conflated with transition-condition evaluation.

### Two correspondence sources
1. **User-declared correspondence** — a mapping explicitly supplied by the user or in the input model. Preserve its declared provenance (for example, `user-declared`), mapping rule, source/target IDs, and any user rationale. This is the only source that may be treated as an explicitly accepted mapping without an additional acceptance action, provided it passes schema and consistency validation.
2. **Derived correspondence candidate** — a proposal generated by a deterministic, versioned derivation procedure from the available model and explicit metadata. A candidate is not an accepted mapping and must not affect the TGCV graph, accessible-transformation calculation, or execution semantics until the user accepts it.

### Minimum candidate record
Each candidate must carry:
- stable candidate ID and derivation algorithm/version;
- source graph element(s) and proposed TGCV transformation/relation target(s);
- candidate status: `PROPOSED`, `NEEDS_REVIEW`, `ACCEPTED`, or `REJECTED`;
- evidence used (explicit IDs, declared source/target states, preconditions/postconditions, condition text or declared aliases), plus a human-readable rationale;
- provenance linking it to the exact input model/version or digest;
- any ambiguity/conflict and the reason for abstention when no safe proposal can be made.

### Derivation policy and safety boundaries
- Prefer explicit identifiers, declared mappings, and structured pre/postconditions over lexical or topological similarity.
- Lexical/heuristic matching may produce reviewable suggestions only; it must never silently create accepted mappings.
- Graph topology alone is insufficient evidence for semantic equivalence, causal direction, or a transformation's meaning.
- Do not invent transformation IDs, relation types, conditions, or missing semantics. If evidence is absent, conflicting, or ambiguous, return `NEEDS_REVIEW` or no candidate.
- A proposed mapping must not be represented as scientific validation, causal evidence, or canonical TGCV semantics.
- Accepting/rejecting a candidate is an explicit user action with provenance. Rejection must prevent the same unchanged candidate from being silently re-applied; changing the source model or derivation version may create a new candidate.
- When the source model, transformation inventory, conditions, or relevant metadata changes, mark affected accepted/derived mappings as potentially stale and require revalidation; never silently rewrite the user's explicit mappings.
- Existing explicit mappings and their provenance must remain intact when deriving new candidates.

### Minimum acceptance tests
1. An explicit valid user-declared mapping is preserved through import, evaluation, graph rendering, and export/replay.
2. A deterministic candidate is generated from sufficient explicit structured evidence and remains `PROPOSED` until user acceptance.
3. Accepting a candidate records actor/action provenance and only then updates the TGCV graph.
4. Rejecting a candidate records the decision and does not affect graph semantics.
5. Ambiguous, contradictory, or insufficient evidence yields `NEEDS_REVIEW` or no proposal; no mapping is invented.
6. Lexical similarity and graph topology alone cannot auto-accept a mapping.
7. A source-model or derivation-version change marks affected candidates/mappings stale and is auditable.
8. Browser and Python/reference representations agree on accepted mapping semantics; proposed/rejected candidates do not change accessible transformations or execution results.
9. Export/import/replay preserves candidate status, evidence, provenance, and source-model linkage.

### Implementation status and gate
This section defines the required contract. The bounded exact-boundary derivation/review/materialization path is implemented, and the minimum grouped correspondence lifecycle integration gate is **PASS** on code commit `1491c2dce624e42da3ef6fb682a4645700612764` (browser/cross-runtime run [40208152055](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40208152055); synthetic engine run [40208152054](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40208152054)). This does **not** close the complete acceptance criteria in §10.6: the three-path condition-entry acceptance suite, a general user-facing resolution workflow for all `CONFLICT_NEEDS_REVIEW` types, and restoration of conflict-resolution decisions after browser-context restart remain open/unverified. Derivation remains exact-boundary only, not general semantic inference. This contract does not authorize scientific execution, alter the stabilized scientific Core, or authorize promotion to `main`.


## 10. Transition-condition entry paths and correspondence integration gate (2026-10-22)

### 10.1 Canonical condition contract

All three entry paths must produce the same canonical transition representation. For schema `collective-toy-input-002`, the condition is `transitions[].condition` (non-empty text); the evaluation is separate, scenario-scoped data in `scenarios[].condition_evaluations[transition_id]`, bound to the exact current condition text and one of `TRUE`, `FALSE`, or `UNKNOWN`. Missing/stale evaluation is distinct from `UNKNOWN`. Changing or removing a condition invalidates its prior evaluation; no input route may silently convert a conditional transition to an unconditional one.

The JSON, transcriber, and visual editor are alternative entry/edit paths over the same canonical model, not separate semantics. After any edit, validate the model, refresh both graph views, mark derived artifacts/correspondence candidates stale where affected, and require an explicit re-run before treating execution/exploration results as current.

### 10.2 Input-path coverage matrix

| Path | Current inspection | Required behavior / acceptance gate |
|---|---|---|
| JSON advanced import/editor | The schema validator accepts `condition` on a transition in input schema v002 and stores scenario evaluations separately. | Import/export/replay preserves condition and evaluation provenance; reject malformed or stale evaluation; changing condition invalidates the old evaluation; run equivalent fixtures through browser and Python/reference semantics. |
| Text-to-graph transcriber | The local parser recognizes a limited set of explicit conditional patterns and can preserve the recognized clause as condition metadata. Unrecognized/ambiguous clauses are pending clarification, not accepted graph semantics. | Grouped positive, negative, ambiguous and adversarial cases; recognized condition must be attached to the correct directed edge; unsupported/negated/ambiguous language must remain pending and must never become an unconditional edge; condition and provenance survive review, execution, export/import. Language patterns are documented as limited, not general language understanding. |
| Visual graph editor | It can add/remove transitions and display/evaluate an existing condition; inspection found no visual control to add/edit the condition text on a transition. | Add an explicit condition edit control for each transition, including add/change/clear; show condition text and evaluation status; changing/clearing it invalidates prior evaluation; persist via canonical schema v002; preserve stable transition IDs where possible; update both graphs and mark TGCV mapping candidates stale where relevant. |

### 10.3 Grouped cross-path acceptance suite

A shared fixture set must cover at least:
1. An unconditional transition and a conditional transition entered through each supported route.
2. Equivalent inputs across routes normalize to equivalent canonical models, apart from documented provenance/IDs.
3. `TRUE` enables the transition; `FALSE`, `UNKNOWN`, missing evaluation, and stale evaluation each block it with distinguishable status.
4. Editing the condition text invalidates the prior evaluation and cannot reuse a result bound to the old text.
5. A transcriber clause with unsupported negation, ambiguous scope, missing condition, or unclear direction is held for user clarification rather than silently simplified.
6. Visual creation/edit/clear followed by export/import/replay preserves the intended condition and status.
7. Both system and TGCV graph views refresh consistently; no stale result is presented as current.
8. Browser and Python/reference semantics agree on the canonical model and resulting exploration/execution.
9. Existing unconditional models and historical schema/profile behavior remain compatible.

This is grouped contract coverage; it does not require a separate test for every phrase permutation. Add adversarial cases where they test a distinct failure mode.

### 10.4 Correspondence derivation integration architecture

Correspondence derivation is a separate, explicit stage between validation of the system model and construction/update of the TGCV graph. It is not part of the condition evaluator and must not be triggered as an invisible side effect of executing a model.

Pipeline:
1. **Validate inputs:** canonical system model, declared TGCV transformation/relation inventory or other explicit candidate-target catalogue, and any user-supplied mapping hints.
2. **Preserve explicit mappings:** validate and retain `tgcv_mapping` entries with their original provenance; never overwrite them with a derived result.
3. **Generate candidates:** call a pure, deterministic, versioned derivation procedure over the validated model and declared target catalogue. It may use explicit IDs, structured pre/postconditions, condition metadata, aliases, and explicit user hints. Heuristic/lexical matching may only rank or explain reviewable candidates.

The first implemented derivation slice uses catalogue schema `tgcv-target-catalogue-001` with an explicit version and entries `{id, source_state, target_state}`. Algorithm `tgcv-correspondence-exact-boundary-001` proposes a candidate only for exact transition source/target-state matches. A unique exact match yields `PROPOSED`; multiple exact matches yield `NEEDS_REVIEW`; no match yields no candidate. Each candidate carries SHA-256 source-model linkage, a stable SHA-256 candidate ID, catalogue/algorithm version, matching evidence and rationale. This deliberately conservative exact-boundary algorithm is a first slice, not a general semantic inference engine. The browser exposes a user-facing candidate review panel with accept/reject controls and local persistence scoped by source-model SHA-256, catalogue version, and SHA-256 of the complete catalogue content. Matching decisions are restored only for the same scope; when the model, version label, or catalogue content changes, prior decisions remain archived under the old key and are not reused. The current review snapshot is included in exported run packages. Accepting a candidate deliberately does not apply it to the TGCV graph. Regression coverage for catalogue-content invalidation passed on exact head `447b231eae5529f5fd3200115eca3667c6ec795e`: browser/cross-runtime run [39803504788](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39803504788) and Python engine run [39803504830](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39803504830), both `completed / success`. Import/replay of correspondence-review snapshots is now implemented as audit-only validation: schema, source-model digest, catalogue version/content digest, candidate IDs, provenance fields, evidence, and decision states are checked; a valid snapshot is preserved in the package assessment and never written into active local decisions or applied to the TGCV graph. Regression coverage for a valid accepted decision surviving package assessment and model-linkage tampering is PASS on exact head `6763bd629443f31a138e0192ea3771308e7633dc`: browser/cross-runtime run [39807093092](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39807093092) and Python engine run [39807093124](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39807093124), both `completed / success`. Effective-mapping materialization boundary is now specified in §10.4.1; implementation and grouped acceptance tests remain open.
4. **Review queue:** show candidate source, proposed target, evidence, rationale, confidence/ambiguity indicators where justified, algorithm version and source-model digest. Candidate statuses are `PROPOSED`, `NEEDS_REVIEW`, `ACCEPTED`, `REJECTED`, or `STALE`.
5. **Explicit decision:** acceptance/rejection is a user action and is persisted with decision provenance. A candidate is not effective while proposed, needs review, rejected, or stale.
6. **Materialize accepted mappings:** only accepted candidates are converted into the effective mapping set used to render the TGCV graph and calculate operational accessible transformations/relations. Preserve the distinction between user-declared and derived-and-accepted provenance.
7. **Invalidation/replay:** model, condition, target inventory, mapping-hint, or derivation-version changes invalidate affected candidates and mark affected derived mappings `STALE`; require review again. Explicit user-declared mappings are not silently rewritten, though their consistency may be flagged for review.
8. **Audit/export:** persist the candidate set, evidence, source digest, derivation version, decisions and effective mapping set; export/import/replay must preserve them.

### 10.4.1 Effective-mapping materialization boundary

An accepted candidate becomes effective only through a distinct, explicit **Apply accepted mappings** action. The Accept action records the review decision; it does not itself apply the mapping. Materialization must satisfy all of the following:

- **Exact scope:** candidate source-model SHA-256, catalogue version and full catalogue-content SHA-256 must match the currently loaded model/catalogue; the candidate's derivation algorithm/version must still be supported.
- **Structural validation:** the referenced system transition and TGCV transformation must exist in the current inputs, and the candidate evidence must validate against those exact objects.
- **Conflict handling:** an existing user-declared `tgcv_mapping` always retains its original definition and provenance. A derived candidate that duplicates or conflicts with a declared mapping or another effective mapping is not applied; report `CONFLICT_NEEDS_REVIEW` and require an explicit resolution rather than silently overriding either mapping.
- **Separate effective layer:** materialization creates/updates a derived effective-mapping overlay; it must not rewrite the input model's `tgcv_mapping`. Each entry records mapping ID, candidate ID, source-model digest, catalogue version/content digest, algorithm/version, decision actor/type and decision timestamp or deterministic event reference, plus provenance `derived-and-accepted`.
- **Idempotence:** applying the same valid accepted candidate twice yields one effective mapping, not duplicates. The operation must be deterministic for the same model/catalogue/candidate/decision scope.
- **Revocation and staleness:** rejecting/revoking a decision or changing the model, relevant conditions, mapping hints, catalogue content/version or derivation algorithm removes the affected derived mapping from the active effective set and records it as `STALE`/inactive in audit history. Never delete or silently rewrite a user-declared mapping; flag its consistency separately when necessary.
- **No downstream effect before apply:** `ACCEPTED` means review accepted, not effective. Only validated, active entries in the effective overlay may affect TGCV graph rendering, accessible transformations/relations, reachability or other operational calculations.
- **Import/replay safety:** package import/replay validates and preserves the review snapshot as audit evidence only. It must not write local active decisions or materialize mappings. Activating an imported decision requires a separate explicit user action and fresh validation against the currently loaded model and catalogue.

The UI must distinguish at least `PENDING_REVIEW`, `ACCEPTED_NOT_APPLIED`, `EFFECTIVE`, `CONFLICT_NEEDS_REVIEW`, `STALE` and `REJECTED`; labels must not imply that accepted candidates are already effective.

No declared target catalogue or insufficient/conflicting evidence means no fabricated target and no automatic candidate; return no proposal or `NEEDS_REVIEW`. Graph topology alone cannot establish semantic equivalence, causal direction, or scientific meaning. A candidate's ranking/confidence is a procedural hint, not a probability of scientific truth.

### 10.5 Correspondence stage boundaries and acceptance

The correspondence stage consumes the validated system model plus an explicitly declared TGCV target catalogue. It produces a candidate set and, after user decisions, an effective mapping set. The condition evaluator consumes condition text and explicit scenario evaluations; it must not infer correspondences. The graph renderer consumes only the validated model and effective mappings; proposed/rejected/stale candidates must not alter the TGCV graph, `T_acc`, reachability, or execution results.

Acceptance requires grouped tests for: deterministic candidate generation from sufficient structured evidence; no candidates or review status for absent/ambiguous/conflicting evidence; explicit accept/reject provenance; no semantic effect before acceptance; stale invalidation; preservation of explicit mappings; export/import/replay; browser/reference agreement; and adversarial checks that lexical similarity/topology alone never auto-accept a mapping.

### 10.6 Status and promotion gate

- JSON condition metadata: **PARTIAL — schema/runtime behavior exists; complete three-path acceptance suite pending**.
- Text transcriber condition metadata: **PARTIAL — bounded pattern recognition exists; grouped adversarial acceptance suite pending**.
- Visual condition editing: **IMPLEMENTED AND CI-PASS — add/edit/clear UI, stale-evaluation invalidation, and grouped regression tests passed on exact head `d8d6f420a0259d59c2bd08c689c121318c23419e`**.
- TGCV correspondence derivation/review/materialization: **PARTIAL — deterministic exact-boundary generation; explicit accept/reject and separate apply action; scoped decision persistence; effective overlay; idempotent application; conflict validation; and audit-only package import/replay are implemented. Integrated browser coverage exercises effective mapping → catalogue change → stale/history retention → catalogue restoration without reactivation → explicit re-review/re-apply → source-model edit invalidation → execution/TGCV-graph exclusion → model rollback without resurrecting the old ACCEPTED decision. The declared-target collision UI regression checks exclusion of an incompatible derived proposal and preservation of declared mapping/provenance. The application-time conflict test now proves fail-closed behavior (zero effective mappings while unresolved), persists ACCEPTED and REJECTED review decisions, and proves that explicit rejection followed by re-application leaves only the selected correspondence effective. Browser/cross-runtime run [40049887219](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40049887219) and synthetic-engine run [40049887171](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40049887171) PASS on exact head `e1af7a5cb6aeb72642f2d2a3bf03ba289220c781`. Remaining scope: broader semantic correspondence inference is not claimed; current derivation is exact-boundary only. Reload/restart restoration of the conflict-resolution decision and a general user-facing resolution workflow for all `CONFLICT_NEEDS_REVIEW` types remain unverified; do not claim full correspondence-stage completeness.**

PR #95 must remain unmerged until these gates are implemented or explicitly split into a separately reviewed follow-up with no claim of full demonstrator completeness. Any split must retain the missing capabilities as visible, tracked blockers rather than silently dropping them from acceptance. No scientific execution is authorized by this contract; this does not modify the stabilized scientific Core or authorize promotion to `main`.


### Reconciliación de evidencia vigente — 2026-10-25

Estado de CI confirmado sobre el commit `f12bf81214f90807cb8d6ce0a5f743a096ce424f`:

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075921)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075929)

El bloque de orden inverso para la colisión declarada↔derivada queda PASS. El rechazo sin alteración operacional y la reaplicación idempotente tienen evidencia PASS separada en el commit `6b5ee82bb9935a051a312ea12b4bc3233c27e943` (runs 40203256337 y 40203256339). Las notas históricas que los dejan “pendientes de CI” no describen el estado actual.

**No declarar completo el gate de integración cruzada:** queda un bloque agrupado por ejecutar y dos workflows en el mismo commit. Debe combinar baseline, propuesta pendiente, rechazo, mapping aplicado, invalidación a `STALE`, restauración/recarga y reaplicación idempotente, con comparaciones independientes de mapping declarado/efectivo y procedencia, `T_acc`, grafo, resultado por escenario, alcanzabilidad y trayectorias. No se reabren las 60 permutaciones declarada↔declarada.

Este bloque no elimina los blockers de alcance enumerados en §10.6: restauración tras reinicio de las decisiones de resolución de conflicto y flujo general de resolución para todos los tipos `CONFLICT_NEEDS_REVIEW` continúan sin verificar. La derivación sigue limitada a coincidencia exacta de fronteras; no se reclama inferencia semántica general. PR #95 permanece abierta y en borrador; `main` no se modifica.
