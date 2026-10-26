# TGCV correspondence and trajectory-source gap — corrected review 001

**Status:** CORRECTED IMPLEMENTATION REVIEW — design review only  
**Branch:** `proposal/graph-tgcv-representation-contract-001`  
**Scope:** Clarify the actual pending integration gap before trajectory-selector integration.  
**Execution status:** No scientific execution, no runtime test execution, no motor/UI code changes, no TGCV Core change, and no claim-status change.

## 1. Correction to the previous review

The earlier framing incorrectly treated the graph-to-TGCV correspondence layer as an unimplemented semantic layer. That conclusion is withdrawn.

The existing demonstrator already contains correspondence candidate derivation, review/acceptance, validation and effective correspondence handling. Relevant code in `prototypes/collective_toy/web/index.html` includes:

- `deriveTgcvCorrespondenceCandidates(systemModel, catalogue)`: derives correspondence candidates against an explicitly supplied, versioned TGCV transformation catalogue;
- `applyAcceptedTgcvCorrespondences()` and `validateAcceptedCorrespondenceCandidates(...)`: validates and materializes accepted correspondences;
- `effectiveCorrespondencesForModel(m)`: returns only effective mappings whose source-model and catalogue fingerprints still match.

The derivation is a constrained candidate-generation procedure, not a universal or automatic semantic mapping. Nevertheless, the correspondence mechanism is already implemented; do not create a duplicate intermediate semantic layer to solve the current problem.

## 2. Actual issue

The system graph and TGCV transformation representation are already distinguished in the demonstrator. The outstanding integration issue is that trajectory exploration and selection still consume trajectories enumerated from the **system graph** rather than trajectories generated from the **TGCV transformation graph/representation using the effective correspondences**.

The current system-graph traversal `runTemporalScenario(m, s)` constructs adjacency from `m.transitions` and produces paths through system states and transitions. The selector then ranks the trajectories supplied to it. The unresolved question is therefore not whether a new semantic layer should exist; it is where and how the trajectory-generation flow should switch to the TGCV representation, while retaining a valid mapping back to system transitions for execution.

## 3. Correct target flow

1. Validate the current system model and TGCV target catalogue.
2. Obtain the effective, non-stale accepted correspondences using the existing mechanism.
3. Generate candidate trajectories in the TGCV representation, using its transformation identities and applying the relevant accessibility, condition and prerequisite rules.
4. Pass those TGCV trajectories to the heuristic selector. The selector ranks candidates; it does not define accessibility, derive mappings, or execute transformations.
5. For a selected TGCV trajectory, resolve each selected transformation through the effective correspondence to the system transition(s) required for concrete execution. Reject missing, ambiguous or conflicting mappings rather than guessing.
6. Record both identities in the execution trace: TGCV transformation identity and corresponding system transition identity, together with source/result state and the applicable evaluated-condition/prerequisite evidence.

An accepted correspondence does not by itself prove that its transformation is accessible in the current state/context. The TGCV trajectory generator must apply the existing accessibility and constraint semantics; it must not simply traverse every accepted correspondence.

## 4. Focused acceptance tests

| ID | Case | Expected result |
|---|---|---|
| TG-TR-01 | Correspondences are absent, stale, or invalidated after source/catalogue change | No TGCV trajectory is presented as valid; fail closed with a clear reason |
| TG-TR-02 | Valid effective correspondences exist | Candidate trajectories are generated in TGCV transformation identities, not directly copied from system-graph path records |
| TG-TR-03 | System graph contains a transition with no effective TGCV mapping | It cannot silently appear as a TGCV transformation in the candidate trajectory |
| TG-TR-04 | TGCV transformation has no unique resolvable system execution mapping | Concrete execution is blocked pending explicit resolution |
| TG-TR-05 | Multiple TGCV transformations map to the same system transition or share endpoints | Preserve distinct TGCV identities; do not collapse by endpoint pair or system transition ID |
| TG-TR-06 | Condition is unevaluated/unknown or prerequisite unsatisfied | Candidate is not treated as accessible/executable merely because a correspondence exists |
| TG-TR-07 | Selector ranking order changes | TGCV accessibility set and generated candidate set do not change as a side effect |
| TG-TR-08 | Recommendation is executed | Trace preserves both TGCV transformation IDs and system transition IDs, in order |
| TG-TR-09 | Same system-level endpoints admit different TGCV transformation sequences | Candidate generation and trace retain the distinct TGCV sequences |
| TG-TR-10 | No TGCV path exists but system graph has a path | Do not fall back silently to a system-graph trajectory while labeling it TGCV |
| TG-TR-11 | Repeated exploration with identical model, catalogue, effective correspondences, scenario and constraints | Deterministic candidate trajectories under the same versioned contract |
| TG-TR-12 | Trajectory is displayed, selected, then executed | UI and audit distinguish TGCV trajectory selection from mapped system-level execution |

These are proposed software-contract tests, not executed test results and not evidence of scientific validity.

## 5. Minimal next implementation block

- Trace the existing UI handlers from correspondence application through exploration, selector input, trajectory selection and `execute-sequence`.
- Identify the exact boundary where system-graph trajectories are currently passed to the selector.
- Add a TGCV-trajectory generation/adaptation step that consumes the already existing effective correspondences; do not duplicate correspondence derivation or introduce another semantic layer.
- Keep system-level execution behind explicit, validated mapping from each TGCV transformation to the system transition(s).
- Add focused contract tests from TG-TR-01 to TG-TR-12, starting with the missing/stale mapping and identity-preservation cases.
- Keep the selector disconnected from the main demo execution flow until the above passes; retain PR #99 and `main` unchanged pending review.

## 6. Governance boundary

This correction changes the diagnosis of the implementation gap, not TGCV's scientific status. It does not modify TR-131, the Core, RMA, the Evidence→Claim Matrix, or any scientific claim. No scientific execution is authorized.

**Corrected disposition:** reuse the existing correspondence mechanism; adapt trajectory generation and selector input so trajectories are defined over the TGCV representation, then map selected transformations back to the system graph for concrete execution.
