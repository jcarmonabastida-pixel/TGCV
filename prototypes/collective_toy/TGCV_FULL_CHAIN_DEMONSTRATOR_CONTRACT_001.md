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
This section defines the required contract; it does not claim that candidate derivation or its acceptance workflow is already implemented. Treat the capability as **PENDING** until implementation and grouped adversarial tests demonstrate the criteria above. The existing evaluator CI PASS does not satisfy this gate by itself. This contract addition does not authorize scientific execution, alter the stabilized scientific Core, or authorize promotion to `main`.
