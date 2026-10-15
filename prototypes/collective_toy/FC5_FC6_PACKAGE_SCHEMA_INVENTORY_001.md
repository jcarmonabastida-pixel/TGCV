# FC-5 / FC-6 finite schema inventory — draft 001

- **Status:** contract extraction from the current browser importer; inventory draft, not closure evidence.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Source commit at extraction:** `0d22cd9089485dd2f648f1a0fc9108ea612a038e`
- **Contract:** `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`
- **Implementation:** `web/index.html`, especially `validate(m)`, `assessImportedBrowserPackage(pkg)`, trace/outcome/assessment creation.
- **Test file:** `web/ui_contract_test.cjs`
- **No scientific execution. No change to main, detector, or OCR evaluation.**

## 1. Scope and counting rule

Count a requirement as one independently testable acceptance predicate, not as one field name and not as one test function. Positive validity, missing-field rejection, wrong-type rejection, unknown-field rejection, cross-link consistency, hash consistency, deterministic replay, and compatibility are distinct predicates where applicable. One test may cover multiple predicates; one predicate may need multiple fixtures.

This is a first finite inventory of the schema surface visible in the current importer. It does **not** yet claim an exhaustive count of all acceptance predicates because several nested structures lack closed-key validation or explicit type constraints.

## 2. Package envelope

Top-level accepted keys (8):
- `package_version` — required; exact supported value `collective-toy-browser-run-001`.
- `input` — required object; must pass model validation.
- `result` — required object; schema and replay checks apply.
- `package_sha256` — required lowercase 64-hex string; hashes the package body with this field removed.
- `concrete_execution_trace` — optional object; when present, trace schema/status/hash checked.
- `outcome_record` — optional object; if present, requires a matching completed execution trace and identity/hash links.
- `value_assessment` — optional object; if present, requires an outcome and complete contextual fields.
- `value_assessment_status` — conditional: must be `NOT_ASSESSED` when no assessment is present; must be absent when an assessment is present.

| Predicate | Existing evidence | Status |
|---|---|---|
| Reject unknown top-level package key | `unknown-package-field.json` | verified in latest CI |
| Reject missing `input` | `missing-package-input.json` | verified in latest CI |
| Reject missing `result` | `missing-package-result.json` | verified in latest CI |
| Reject unsupported `package_version` | `unsupported-package-version.json` | verified in latest CI |
| Reject absent/malformed package hash | Validator branch exists; no dedicated case located in current adversarial set | pending dedicated test |
| Reject wrong type for each optional top-level field | No exhaustive per-field wrong-type matrix located | pending |
| Validate conditional presence combinations of trace/outcome/assessment/status | Positive assessed and NOT_ASSESSED round trips exist; full truth table not enumerated | partial |

## 3. Input model (`input`)

Accepted top-level keys (9):
- `schema_version` — exact `collective-toy-input-001`
- `model_id` — non-empty string
- `initial_state` — declared state ID
- `states` — non-empty list of unique non-empty string IDs; maximum 500
- `transitions` — list of transition objects; maximum 2,000; IDs unique; source/target must reference declared states
- `relations` — optional list; relation objects allowed only `id`, `type`, `transition_id`, `requires_transition_id`; type depends on rule profile; referenced transition IDs must exist and differ
- `rule_profile` — object with only `type`, `version`; one of finite deterministic graph v1, relation guarded graph v1, temporal prerequisite graph v1
- `scenarios` — non-empty list; scenario objects allow only `id`, `disabled_transitions`; IDs unique; baseline required; disabled IDs must exist
- `exploration` — object with only `max_depth`, `max_trajectories`; integers within declared bounds

| Predicate group | Existing evidence | Status |
|---|---|---|
| Valid input and model semantic checks | Main synthetic engine/browser and replay tests | partial: broad valid coverage, not one test per predicate |
| Unknown input/model field rejection | `validate(m)` uses closed-key checks | implementation present; adversarial tests not enumerated for every nesting level |
| Missing/wrong-type input fields | `validate(m)` checks many fields | implementation present; systematic negative matrix pending |
| Duplicate IDs, invalid references, numeric boundaries | Validator contains checks | implementation present; exhaustive test mapping pending |

## 4. Result envelope (`result`)

Allowed keys (13):
- `engine_version` — non-empty string
- `schema_version` — must equal `input.schema_version`
- `model_id` — must equal `input.model_id`
- `rule_profile` — canonical equality with input rule profile
- `validation` — exact `PASS`
- `scenario_results` — object; must contain exactly the scenario identities represented by the input (unknown IDs and missing input scenarios rejected)
- `comparisons_to_baseline` — object; one comparison for every non-baseline input scenario, no baseline/unknown keys
- `delta_reach` — produced by engine and included in result; detailed nested schema needs independent enumeration
- `scientific_interpretation` — string
- `semantic_identity_version` — optional; when present exact `collective-toy-semantic-identity-001`
- `semantic_sha256` — conditional 64-hex digest; required/verified when semantic identity version is present and forbidden without it
- `input_sha256` — 64-hex hash of input
- `result_sha256` — 64-hex hash of result body excluding `input_sha256` and `result_sha256`

Existing adversarial coverage: unknown `result` key is tested with result and package hashes recomputed. Cross-links for model ID and rule profile, schema version, validation status, and replay equality are enforced in code; dedicated negative fixtures for every individual predicate are not yet inventoried.

## 5. Nested result objects

### `scenario_results[id]`

Allowed keys (11):
`scenario_id`, `disabled_transitions`, `enabled_transitions_at_initial_state`, `reachable_states`, `trajectories`, `truncated`, `exploration_bounds`, `relation_effects`, `effective_disabled_transitions`, `blocked_temporal_steps`, `temporal_prerequisites`.

Current checks include object type, closed keys, key/id consistency, array/string constraints, valid state/transition references in trajectories, boolean truncation, integer exploration bounds, profile-specific relation semantics, and temporal-prerequisite derivation. Several profile-dependent fields are optional by design. Dedicated wrong-type/missing-field coverage for each key remains to be mapped.

### `scenario_results[id].exploration_bounds`

Allowed keys (2): `max_depth`, `max_trajectories`; both non-negative integers.

### `blocked_temporal_steps[]`

Allowed keys (4): `at_state`, `transition_id`, `missing_prerequisites`, `prior_transitions`; state/transition references must exist and missing prerequisites must be non-empty.

### `comparisons_to_baseline[id]`

Allowed keys (8): `intervention`, `enabled_at_initial_added`, `enabled_at_initial_removed`, `reachable_states_added`, `reachable_states_removed`, `trajectories_added`, `trajectories_removed`, `truncated`.

Nested `intervention` allows only `disabled_transitions` (array). The validator checks scenario identity, required comparisons, arrays, referenced transition/state IDs, route consistency, and boolean truncation. Exhaustive missing/wrong-type tests remain pending.

### `delta_reach`

The engine attaches a delta artifact containing baseline/intervention source hashes, changes in reachable states and accessible transitions, and truncation metadata per contract. A complete field-by-field nested schema and dedicated adversarial test mapping have **not yet been extracted**; treat this as an explicit inventory gap rather than assuming full coverage.

## 6. Execution trace (`concrete_execution_trace`)

Creation currently emits these keys:
`trace_schema`, `execution_id`, `model_id`, `input_sha256`, `scenario_id`, `candidate_index`, `submitted_transition_ids`, `initial_state`, `steps`, `final_state`, `status`, `blocked_step`, `trace_sha256`.

Importer checks object shape, exact `trace_schema=collective-toy-sequence-trace-001`, exact `status=COMPLETED`, 64-hex `trace_sha256`, and hash consistency after removing `trace_sha256`. If an outcome is included, it checks execution ID, trace hash, model ID and scenario ID links.

**Gap:** current importer does not apply a closed-key allowlist to trace or step objects and does not fully validate each listed trace field's type/semantics. Existing test checks missing referenced trace when an outcome is present; a trace-only package, blocked trace, unknown nested trace field, malformed step, and wrong-type matrix are not exhaustively covered. Note: the importer currently accepts only COMPLETED traces in packages, while UI can display BLOCKED traces; this contract boundary needs an explicit decision/test.

## 7. Outcome record (`outcome_record`)

Creation currently emits:
`outcome_schema`, `outcome_id`, `execution_id`, `execution_trace_sha256`, `model_id`, `scenario_id`, `source_kind`, `value`, `unit`, `timing`, `uncertainty_status`, `provenance`.

Importer checks object shape, exact `outcome_schema=collective-toy-outcome-001`, links to trace execution/hash/model/scenario, and non-empty `outcome_id` and `value`.

**Gaps:** no closed-key allowlist; no complete type/non-empty validation for `source_kind`, `unit`, `timing`, `uncertainty_status`, `provenance`; unknown nested keys and wrong types are not covered by a finite test matrix.

## 8. Value assessment (`value_assessment`)

Creation currently emits:
`assessment_schema`, `assessment_id`, `outcome_id`, `execution_id`, `outcome_sha256`, `observer`, `context`, `criterion`, `valuation_rule`, `rationale`, `status`.

Importer checks object shape, exact `assessment_schema=collective-toy-value-assessment-001`, `status=ASSESSED`, outcome/execution links, 64-hex outcome hash and digest match, and non-empty `observer`, `context`, `criterion`, `valuation_rule`, `rationale`. It rejects simultaneous `value_assessment_status`.

**Gaps:** no closed-key allowlist; `assessment_id` and types for all string fields lack a complete independent test mapping; unknown nested keys/wrong-type cases remain pending.

## 9. Hash semantics and security boundary

The package uses unkeyed SHA-256 hashes for canonical integrity/replay checks. If an actor can rewrite a package and recompute all unkeyed hashes, the hashes alone do not authenticate who created it or prove that it is trustworthy. Current UI wording already distinguishes consistency from origin authentication in the unsupported-engine path; user-facing package assessment and contract text still need an explicit, consistent security statement and a regression assertion.

No cryptographic authenticity/signature requirement is currently defined. Do not silently add signing keys or claim authentication.

## 10. Coverage register and next work

| ID | Predicate family | Current state |
|---|---|---|
| FC5-PKG-01 | Package envelope closed keys / unknown top-level rejection | verified |
| FC5-PKG-02 | Required input/result and package version | verified |
| FC5-PKG-03 | Package hash presence, format, integrity | partial; dedicated missing/wrong-format cases not located |
| FC5-IN-01 | Input model schema and semantic validation | implementation present; systematic negative fixtures pending |
| FC5-RES-01 | Result closed keys and top-level cross-links | partial; unknown result field tested, remaining predicates not individually mapped |
| FC5-SCEN-01 | Scenario result nested schema | partial; field-level negative matrix pending |
| FC5-CMP-01 | Baseline comparison nested schema | partial; field-level negative matrix pending |
| FC5-DELTA-01 | Delta-reach nested schema and source hashes | pending inventory and test mapping |
| FC5-TRACE-01 | Trace schema, types, steps, status, hash and links | partial; unknown nested keys/types and BLOCKED policy unresolved |
| FC5-OUT-01 | Outcome schema, types and execution linkage | partial; unknown nested keys/types not tested |
| FC5-VAL-01 | Assessment schema, types and outcome linkage | partial; unknown nested keys/types not tested |
| FC5-SEC-01 | Integrity vs authenticity wording and regression | partial |
| FC5-REPLAY-01 | Independent deterministic replay and compatibility | verified for current tested fixtures; broader boundary matrix pending |
| FC6-CI-01 | All required workflows run on the candidate commit | verified for commit `a90b69a6`; must rerun on any later code/test change |
| FC6-CLEAN-01 | Clean-source archive replay | verified for commit `a90b69a6`; must rerun on any later code/test change |
| FC6-ART-01 | Artifact inspection and scope/non-claim checks | partial; inspect exact artifacts and evidence per contract |

This register contains 16 predicate families, **not 16 atomic requirements**. The remaining atomic count is intentionally not stated until nested `delta_reach`, trace steps, and field/type predicates are decomposed consistently. Next step is to finish those three sub-schema extractions, turn each row into atomic acceptance predicates, then compute the verified/partial/pending count before adding further tests.

## 11. Governance

- Keep `main` unchanged and PR #67 in draft.
- No scientific execution or empirical validation.
- Do not modify the structural detector or OCR quality work.
- Add tests only after the finite predicate list exists; change implementation only for a demonstrated failure.
