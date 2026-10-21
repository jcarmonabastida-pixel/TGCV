# Condition evaluator and visual graph editor — contract proposal 001

**Status:** proposed design; not canonical TGCV semantics and not yet implemented.
**Scope:** browser demonstrator only. This proposal does not change the TGCV scientific core, the existing graph-execution contract, or the meaning of (T_{acc}).

## 1. Problem and design boundary

The graph model can carry a transition `condition`, and the UI can display it, but the current demonstrator deliberately labels such transitions as **not evaluated** and omits them from automatic trajectory exploration. The concrete-execution path must also fail closed: a transition with a condition must not execute merely because its ID, source, target, enabled status, and temporal prerequisites are valid.

The condition evaluator must be a distinct, testable component used consistently by exploration and concrete execution. A condition's presence is not evidence that it is true.

## 2. Meaning of a condition result

Each evaluation returns exactly one of:

- `TRUE`: the supported predicate is well-formed and its required input data are present and match.
- `FALSE`: the supported predicate is well-formed, its required input data are present, and they do not match.
- `UNKNOWN`: the predicate is missing, malformed, unsupported, or any required datum is absent or invalid.

Evaluation must not coerce `UNKNOWN` to `TRUE`. For v1, both `FALSE` and `UNKNOWN` block execution, but the UI and trace must distinguish them. A blocked step must report the transition ID, condition, result, and reason.

No free-form natural-language condition is evaluated by guessing. A natural-language condition produced by the transcriber remains metadata/unresolved until a person represents it using a supported predicate and supplies the required data.

## 3. Minimal v1 predicate language

Use a small, explicit, typed predicate language rather than arbitrary JavaScript or general-purpose expression evaluation. The initial supported predicate is:

```json
{
  "kind": "fact_equals",
  "key": "system.mode",
  "value": "ready"
}
```

The evaluator reads the value at `key` from an explicitly supplied condition context and compares it to `value` using exact type-and-value equality. Missing keys return `UNKNOWN`; a present different value returns `FALSE`. No truthiness, implicit string conversion, expression execution, network lookup, or hidden defaults.

Do not silently reinterpret legacy string-valued `condition` fields as predicates. Until migrated or explicitly resolved in the editor, they evaluate as `UNKNOWN` and cannot execute.

Additional operators (boolean combinations, numeric comparisons, temporal predicates, etc.) require their own documented semantics and tests; they are outside v1.

## 4. Where evaluation data come from

Evaluation data must be explicit, inspectable, and reproducible:

1. **Model definition:** transition predicate, stored with the transition.
2. **Condition context:** a separate map of typed facts supplied by the user for the selected scenario/run, for example `{"system":{"mode":"ready"}}`.
3. **Provenance:** context values and edits are part of the model/run input and exported artifacts; the trace identifies the context used for each evaluation.

The evaluator must not infer facts from state labels, edge labels, free-form descriptions, outcomes, or the observer's value score. It must not call external services or access ambient browser/application state. If the required context is not provided, the result is `UNKNOWN`.

For a first implementation, scenario-specific context is preferable to hidden mutable global context: each scenario has an explicit condition context, and concrete execution uses the context of its selected scenario. If the UI permits run-specific overrides later, those overrides must be recorded in the run artifact and must not silently alter the scenario definition.

## 5. Effect on exploration and concrete execution

- **Exploration:** a transition is eligible only if it is not disabled, its temporal prerequisites are satisfied, and its condition evaluates to `TRUE` in that scenario's context.
- **Concrete execution:** re-evaluate the condition at the exact step where the transition is attempted, using the same scenario context. A non-`TRUE` result blocks that step and records why.
- **Consistency:** exploration and execution call the same evaluator function and share the same predicate semantics.
- **No optimistic path:** `FALSE` and `UNKNOWN` must not appear as executable paths. If the exploration output wants to expose blocked alternatives, it may show them separately as blocked candidates, not as accessible trajectories.
- **Trace:** record the condition result and reason for every attempted conditional transition; do not claim the condition was evaluated if it was merely skipped.

## 6. Visual graph editor requirements

The existing visual editor can add states and edges and delete edges, but does not offer a dedicated per-edge condition editor. Extend the edge review/editor without requiring users to edit raw JSON:

- Show each transition's ID, source, target, enabled/disabled state, and condition status.
- Provide an explicit condition editor for the selected transition: predicate type, fact key, expected value, and value type for v1.
- Provide a scenario condition-context editor for key/value facts, with explicit value types; show which context applies to the selected scenario.
- Clearly distinguish `TRUE`, `FALSE`, `UNKNOWN`, and `NOT EVALUATED`; do not use color alone.
- Explain blocking reasons in the graph and execution trace; selecting a conditional edge should expose its predicate and current evaluation result.
- Preserve unresolved legacy/free-text conditions and make them visibly unresolved; never discard or silently convert them.
- Validate edits before writing them to the model. Editing a condition or context invalidates prior exploration and execution results; require a rerun before those results are presented as current.
- Ensure keyboard access, labels, and mobile usability.

## 7. Acceptance tests before integration

At minimum, grouped contract tests must cover:

1. Matching typed fact -> `TRUE`; transition can be explored and executed.
2. Present non-matching fact -> `FALSE`; transition is absent from executable paths and concrete execution blocks it.
3. Missing key -> `UNKNOWN`; transition is blocked and the trace explains the missing datum.
4. Unsupported/malformed legacy string -> `UNKNOWN`; no optimistic execution.
5. Exploration and concrete execution agree on the same context and predicate.
6. Editing the condition/context invalidates stale results.
7. A disabled transition remains blocked even when its condition is `TRUE`.
8. Existing unconditional transitions and temporal-prerequisite behavior remain unchanged.
9. Export/import preserves predicate, typed context, and evaluation provenance.
10. UI can add, edit, and remove a condition without raw JSON, and can edit scenario context.

Tests must calculate expected outcomes independently of the evaluator implementation. Synthetic contract tests do not constitute scientific validation of TGCV.

## 8. Migration and implementation sequence

1. Review this proposal and settle the v1 data schema.
2. Add the pure evaluator and unit/contract tests.
3. Add model validation and a versioned schema/migration policy for legacy string conditions.
4. Integrate the evaluator into exploration and concrete execution.
5. Extend the visual edge editor and scenario-context editor.
6. Add browser adversarial/regression tests, run all existing CI, and inspect the post-change artifacts.
7. Only then consider a separate PR for integration.

**Current status:** design proposal only. No evaluator implementation, graph-editor code, model schema, or scientific execution has been changed by this document.
