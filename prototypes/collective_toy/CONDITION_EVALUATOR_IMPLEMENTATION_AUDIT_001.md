# Condition evaluator implementation audit — current model schema

**Status:** source inspection only; no runtime behavior changed.
**Base inspected:** `main`, `prototypes/collective_toy/web/index.html`.
**Related design:** `CONDITION_EVALUATOR_CONTRACT_PROPOSAL_001.md`.

## Findings confirmed from current source

1. The validator accepts only `collective-toy-input-001` and `collective-toy-input-002`.
2. Transition keys are restricted to `id`, `source`, `target`, and `condition`.
3. Schema v001 rejects `condition`; schema v002 accepts only a non-empty string condition.
4. Scenario keys are restricted to `id` and `disabled_transitions`; there is no `condition_context` field yet.
5. `runTemporalScenario` builds adjacency from transitions that are not scenario-disabled and have no `condition`. Therefore conditional transitions are omitted rather than evaluated.
6. The current concrete `execute-sequence` handler checks that a transition exists, is not scenario-disabled, starts at the current state, and satisfies temporal prerequisites. The inspected loop does not evaluate `tr.condition` before executing the transition.
7. Graph rendering labels conditional transitions `CONDICIÓN NO EVALUADA`.
8. The model's import/export identity includes the full input model and hashes it. Adding predicate objects and scenario context will therefore affect the model schema, validation, result semantics and serialized artifacts, not just the editor.

## Consequences

- A schema migration is required. Do not change `condition` from string to object under `collective-toy-input-002`; that would silently break the current contract.
- Introduce a new version (proposed `collective-toy-input-003`) for typed condition objects and scenario `condition_context`.
- Preserve old v001/v002 input compatibility. Existing v002 string conditions must remain unresolved and blocked; do not infer predicate meaning from their text.
- Confirm whether package import accepts historical schemas and how it validates results before implementation. Existing package versions and hashes must not be rewritten silently.
- The v003 validator should accept `condition` only when absent or a valid typed predicate object. Legacy strings should be migrated explicitly by a user-facing conversion workflow or remain in v002; do not accept strings in v003 as if they were predicates.
- Add `condition_context` to scenarios in v003, with absent context normalized to an empty object only if canonicalization and hashing rules explicitly specify that normalization. Otherwise require it in newly authored v003 scenarios.
- Implement one pure evaluator and invoke it from both exploration and concrete execution. Keep disabled-transition and temporal-prerequisite checks in force.
- Editor changes must be checked against existing DOM IDs and state/update handlers before implementation; avoid a parallel model store.

## Implementation gates

1. Audit import/export and semantic hashing for historical v001/v002 packages.
2. Agree v003 migration rules and backward-compatibility expectations.
3. Add pure evaluator tests with independently stated expected results.
4. Add v003 validation and scenario context.
5. Integrate exploration and concrete execution, then update graph rendering and visual editor.
6. Run all CI and inspect result/package round-trip behavior.

No code or model schema was changed by this audit. No scientific execution was performed.
