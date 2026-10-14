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

## 7. Current baseline and next operation

The repository already contains a browser graph editor/importer and synthetic profiles 1/2; the sequentiality development branch contains the Python temporal profile and 18 synthetic contract tests. The existing browser engine currently validates only profiles 1/2 and enumerates paths; the full chain is therefore not yet implemented.

**Next operation:** FC-1, first add browser-engine contract tests for temporal profile v1 (including historical-profile regression cases), then implement the minimal matching semantics and run the browser CI. Do not claim end-to-end completion until FC-2 through FC-6 are verified.
