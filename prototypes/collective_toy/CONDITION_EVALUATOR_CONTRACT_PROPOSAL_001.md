# Condition evaluator and visual graph editor — contract proposal 001

**Status:** PAUSED pending review of FUNCTIONAL_ARCHITECTURE_REVIEW_001.md; not approved for implementation. The typed-predicate design remains a candidate for the optional system/domain execution layer only.
**Scope:** browser demonstrator only. This is not canonical TGCV semantics and does not change the scientific core, the existing graph-execution contract, or the meaning of (T_{acc}).

## 1. Problem and design boundary

The graph model can carry a transition `condition`, and the UI can display it, but the current demonstrator labels such transitions as **not evaluated** and omits them from automatic trajectory exploration. Concrete execution must also fail closed: a transition with a condition must not execute merely because its ID, source, target, enabled status, and temporal prerequisites are valid.

The condition evaluator is a distinct, testable component used consistently by exploration and concrete execution. A condition's presence is not evidence that it is true.

## 2. Meaning of a condition result

Each evaluation returns exactly one of:

- `TRUE`: the supported predicate is well-formed and all required input data are present and match.
- `FALSE`: the supported predicate is well-formed, all required input data are present, and at least one required comparison does not match.
- `UNKNOWN`: the predicate is missing, malformed, unsupported, or any required datum is absent or invalid.

Evaluation must not coerce `UNKNOWN` to `TRUE`. For v1, both `FALSE` and `UNKNOWN` block execution, but the UI and trace distinguish them. A blocked step reports the transition ID, predicate, result, and reason.

No free-form natural-language condition is evaluated by guessing. A natural-language condition produced by the transcriber remains unresolved metadata until a person represents it using a supported predicate and supplies the required data.

## 3. Minimal v1 data schema

### Transition condition

A v1 condition is an object with exactly these fields:

```json
{
  "kind": "fact_equals",
  "key": "system.mode",
  "value_type": "string",
  "value": "ready"
}
```

- `kind` is currently only `fact_equals`.
- `key` is a dot-separated path of non-empty object-property names. Lookup traverses own properties only; it must not read prototype properties or invoke getters.
- `value_type` is one of `string`, `number`, or `boolean`.
- `value` must be a finite number, string, or boolean matching `value_type` exactly. No null, arrays, objects, implicit conversion, truthiness, or expression evaluation.
- Unknown fields, missing fields, invalid paths, and mismatched value types make the condition invalid and produce `UNKNOWN`; validation must explain why.

### Scenario condition context

Each scenario has an explicit `condition_context` object, separate from transition definitions. Example:

```json
{
  "condition_context": {
    "system": {
      "mode": "ready",
      "attempts": 2,
      "verified": true
    }
  }
}
```

Facts use JSON scalar values with types preserved. A path such as `system.mode` resolves to the matching nested own-property value. An absent path or a value with a different type yields `UNKNOWN` (not `FALSE`); only a present value of the expected type that differs from the expected value yields `FALSE`.

The exact storage location of `condition_context` in the existing scenario schema must be confirmed during implementation against the current model and import/export code. Do not invent a second scenario representation. If a legacy scenario lacks the field, treat its context as an empty object.

Do not silently reinterpret legacy string-valued `condition` fields as predicates. Until explicitly resolved in the editor, they evaluate as `UNKNOWN` and cannot execute. Preserve the original text for user review.

Additional operators (boolean combinations, numeric comparisons, temporal predicates, etc.) are outside v1 and require their own documented semantics and tests.

## 4. Where evaluation data come from

Evaluation data are explicit, inspectable, and reproducible:

1. **Model definition:** typed predicate stored with the transition.
2. **Condition context:** typed facts supplied by the user for the selected scenario.
3. **Provenance:** context values and edits are part of the model/run input and exported artifacts; the trace identifies the context used for each evaluation.

The evaluator must not infer facts from state labels, edge labels, free-form descriptions, outcomes, or the observer's value score. It must not call external services or access ambient browser/application state. Missing context means `UNKNOWN`.

For v1, scenario-specific context is preferred over hidden mutable global context: each scenario has an explicit context, and concrete execution uses the context of its selected scenario. Any future run-specific override must be recorded in the run artifact and must not silently alter the scenario definition.

## 5. Effect on exploration and concrete execution

- **Exploration:** a transition is eligible only if it is not disabled, its temporal prerequisites are satisfied, and its condition evaluates to `TRUE` in that scenario's context.
- **Concrete execution:** re-evaluate the condition at the exact step where the transition is attempted, using the same scenario context. Any non-`TRUE` result blocks that step and records why.
- **Consistency:** exploration and execution call the same evaluator function and share the same predicate semantics.
- **No optimistic path:** `FALSE` and `UNKNOWN` do not appear as executable paths. Blocked alternatives may be displayed separately as blocked candidates, not as accessible trajectories.
- **Trace:** record the condition result and reason for every attempted conditional transition; do not claim the condition was evaluated if it was merely skipped.

## 6. Visual graph editor requirements

Extend the existing editor without requiring raw JSON editing:

- Show each transition's ID, source, target, enabled/disabled state, and condition status.
- Provide a condition editor for the selected transition: predicate type, fact key, expected value, and value type.
- Provide a scenario condition-context editor for key/value facts, with explicit types; show which context applies to the selected scenario.
- Distinguish `TRUE`, `FALSE`, `UNKNOWN`, and `NOT EVALUATED` in text, not by color alone.
- Explain blocking reasons in the graph and execution trace; selecting a conditional edge exposes its predicate and current evaluation result.
- Preserve unresolved legacy/free-text conditions and show them as unresolved; never discard or silently convert them.
- Validate edits before writing them to the model. Editing a condition or context invalidates prior exploration and execution results; require rerun before those results are presented as current.
- Ensure keyboard access, labels, and mobile usability.

## 7. Acceptance tests before integration

Grouped contract tests must cover at least:

1. Matching fact with exact type -> `TRUE`; transition can be explored and executed.
2. Present non-matching fact with exact type -> `FALSE`; transition is absent from executable paths and concrete execution blocks it.
3. Missing key -> `UNKNOWN`; transition is blocked and trace explains the missing datum.
4. Present fact with mismatched type -> `UNKNOWN`, not `FALSE`.
5. Unsupported/malformed legacy string -> `UNKNOWN`; no optimistic execution and original text is preserved.
6. Exploration and concrete execution agree on the same context and predicate.
7. Editing the condition/context invalidates stale results.
8. A disabled transition remains blocked even when its condition is `TRUE`.
9. Existing unconditional transitions and temporal-prerequisite behavior remain unchanged.
10. Export/import preserves predicate, typed context, and evaluation provenance.
11. UI can add, edit, and remove a condition without raw JSON and edit scenario context.
12. Malformed paths and prototype-property paths cannot access ambient or inherited data.

Expected outcomes must be specified independently of evaluator implementation. Synthetic contract tests do not constitute scientific validation of TGCV.

## 8. Implementation sequence

1. Confirm the existing scenario schema and graph import/export paths before choosing the precise insertion point for `condition_context`.
2. Add the pure evaluator and independent unit/contract tests.
3. Add model validation and a versioned schema/migration policy for legacy string conditions.
4. Integrate the same evaluator into exploration and concrete execution.
5. Extend the visual edge editor and scenario-context editor.
6. Add browser adversarial/regression tests, run existing CI, and inspect post-change artifacts.
7. Only then consider a separate implementation PR.

**Current status:** design contract only. No evaluator implementation, graph-editor code, model schema, or scientific execution has been changed by this document.
