# FC-5 / FC-6 finite schema inventory — draft 001

- **Status:** contract extraction from the current browser importer; inventory draft, not closure evidence.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Source commit at extraction:** `0d22cd9089485dd2f648f1a0fc9108ea612a038e`
- **Contract:** `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`
- **Implementation:** `web/index.html`, especially `validate(m)`, `assessImportedBrowserPackage(pkg)`, trace/outcome/assessment creation.
- **Test file:** `web/ui_contract_test.cjs`
- **No scientific execution. No change to main, detector, or OCR evaluation.**

> **Active delta-reach denominator (2026-10-16):** Use the 12 namespaced predicates `FC5-DELTA-C01`…`FC5-DELTA-C12` in the register's “Canonical delta-reach acceptance table — current register”. Earlier `FC5-DELTA-001`…`FC5-DELTA-012` tables are historical snapshots and must not be counted as active requirements. Do not infer a predicate as verified solely because a related workflow passed: map fixture, targeted diagnostic, and exact-head run together. Open truncation gaps include wrong-type tests for `truncated` and `intervention_truncated`, baseline-specific scenario consistency, and complete truth-table coverage.

> **Reconciliation rule (2026-10-16):** The inventory includes historical iteration notes that may use older FC5-DELTA numbering/statuses. Do not treat those notes as a second active acceptance table. Use the numbered acceptance register's canonical **“Delta-reach atomic acceptance reconciliation — candidate a7813bc”** table for current predicate IDs; use this inventory to describe schema/implementation and fixture evidence. In particular, truncation coverage is not complete merely because the three existing adversarial examples pass: wrong-type coverage for `truncated` and `intervention_truncated`, plus baseline-specific flag-to-scenario consistency and the complete truth table, remain open.

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

The engine emits `delta_reach[scenario_id]` for each non-baseline scenario. The current emitted field set is exactly: `baseline_source_sha256`, `intervention_source_sha256`, `reachable_states_added`, `reachable_states_removed`, `enabled_at_initial_added`, `enabled_at_initial_removed`, `trajectories_added`, `trajectories_removed`, `truncated`, `baseline_truncated`, `intervention_truncated`. The source hashes are computed over a projection containing `schema_version`, `model_id`, `initial_state`, `states`, `transitions`, `relations` (empty when absent), `rule_profile`, `exploration`, and the respective source scenario, with domain tags `delta_reach_baseline_source` and `delta_reach_intervention_source`.

**Atomic predicates and evidence status (reconciled against `web/index.html` lines 270–291 and `ui_contract_test.cjs` lines 1181–1258):** (1) exact non-baseline scenario-key set — validator lines 274–275; dedicated missing/extra-key negative fixtures not located (pending); (2) closed 11-key delta object — validator lines 273, 278; adversarial unknown-key fixture recomputes result/package digests and asserts specific rejection (test lines 1195–1214; directly tested); (3) lowercase 64-hex source hashes — validator line 279; malformed-shape negative fixture not located (pending); (4) source hashes recomputed from the correct baseline/intervention source projection and domain tags — validator lines 280–284; forged well-formed hash fixture asserts specific rejection after recomputing enclosing digests (test lines 1240–1258; directly tested for baseline source only; intervention-source negative remains pending); (5) added/removed state and enabled-transition lists are arrays of declared IDs — validator lines 285–286; malformed/wrong-ID delta fixtures not located (pending direct negative evidence); (6) added/removed trajectory lists are arrays of valid ordered paths — validator line 287; dedicated malformed-path fixture not located (pending); (7) three truncation fields are booleans — validator line 288; the browser adversary sets `baseline_truncated` to string `"false"`, recomputes enclosing digests, and asserts the specific boolean diagnostic (verified on exact-head five-workflow CI: runs 38818696371, 38818696355, 38818696366, 38818696348, 38818696411); (8) `truncated === baseline_truncated || intervention_truncated` and both match scenario flags — validator line 290; two adversaries test aggregate-flag disagreement and intervention-flag disagreement against the scenario result, with recomputed enclosing digests and specific diagnostics (verified on the same exact-head five-workflow CI); (9) delta arrays equal `comparisons_to_baseline` — validator line 289; forged semantic-delta fixture asserts specific rejection (test lines 1216–1234; directly tested for `reachable_states_removed`); (10–12) baseline has no delta, exactly one entry per intervention, and no entry without a matching comparison — enforced by exact-key-set comparison at validator lines 274–275; dedicated negative fixtures not located (pending direct evidence). Therefore the importer DOES have a field-level `delta_reach` validation block; the gap is primarily predicate-to-fixture coverage, not absence of validation. Do not infer all twelve predicates are verified from the existing three focused adversarial cases.

## 6. Execution trace (`concrete_execution_trace`)

Creation currently emits these keys:
`trace_schema`, `execution_id`, `model_id`, `input_sha256`, `scenario_id`, `candidate_index`, `submitted_transition_ids`, `initial_state`, `steps`, `final_state`, `status`, `blocked_step`, `trace_sha256`.

Importer checks object shape, exact `trace_schema=collective-toy-sequence-trace-001`, exact `status=COMPLETED`, 64-hex `trace_sha256`, and hash consistency after removing `trace_sha256`. If an outcome is included, it checks execution ID, trace hash, model ID and scenario ID links.

Trace-field decomposition (fields emitted by the UI): `trace_schema`, `execution_id`, `model_id`, `input_sha256`, `scenario_id`, `candidate_index`, `submitted_transition_ids`, `initial_state`, `steps`, `final_state`, `status`, `blocked_step`, `trace_sha256`.

Step objects emitted on success have `step`, `transition_id`, `state_before`, `state_after`, `prior_transitions`, `prerequisites`, `status`. A blocked attempt records `blocked_step={index, transition_id, reason, required_transition_ids}` and `status=BLOCKED`; a completed attempt has `status=COMPLETED` and `blocked_step=null` (or serialized null).

**Atomic predicates to verify separately:** (1) trace is an object; (2) closed set of 13 keys; (3) exact trace schema; (4) non-empty execution/model/scenario IDs; (5) `input_sha256` is valid and equals package result/input hash; (6) scenario exists in input; (7) candidate index is null or non-negative integer; (8) submitted IDs are a string array; (9) initial/final states are declared; (10) steps is an array; (11) every step has a closed seven-key schema and valid types; (12) step numbers are ordered; (13) transition/state sequence is coherent with input edges; (14) prior-transition history is prefix-consistent; (15) prerequisites are consistent with relations and prior history; (16) status is `COMPLETED` or `BLOCKED` per policy; (17) completed traces have no block and end at the final step state; (18) blocked traces have a valid block index/reason and preserve the last successful state; (19) trace digest format; (20) trace digest recomputation; (21) outcome trace hash/execution/model/scenario cross-links; (22) trace-only packages are accepted/rejected according to an explicit policy.

**Gap:** current importer does not apply a closed-key allowlist to trace or step objects and does not fully validate each listed trace field's type/semantics. Existing test checks missing referenced trace when an outcome is present; a trace-only package, blocked trace, unknown nested trace field, malformed step, and wrong-type matrix are not exhaustively covered. The importer currently accepts only `COMPLETED` traces in packages, while UI can display `BLOCKED` traces; this contract boundary needs an explicit decision/test.

## 7. Outcome record (`outcome_record`)

Creation currently emits:
`outcome_schema`, `outcome_id`, `execution_id`, `execution_trace_sha256`, `model_id`, `scenario_id`, `source_kind`, `value`, `unit`, `timing`, `uncertainty_status`, `provenance`.

Importer checks object shape, exact `outcome_schema=collective-toy-outcome-001`, links to trace execution/hash/model/scenario, and non-empty `outcome_id` and `value`.

**Atomic predicates to verify separately:** closed 12-key schema; exact schema ID; non-empty `outcome_id`; execution ID links to trace; trace digest link; model/scenario links; `source_kind` is an allowed value from the UI control; `value`, `unit`, `timing`, `uncertainty_status`, and `provenance` have documented non-empty string/type constraints; no unknown keys; no null/array/primitive substitution; outcome digest is recomputed when assessed. Current importer explicitly checks schema and cross-links plus non-empty ID/value, but does not enforce a closed key set or the complete field/type rules.

## 8. Value assessment (`value_assessment`)

Creation currently emits:
`assessment_schema`, `assessment_id`, `outcome_id`, `execution_id`, `outcome_sha256`, `observer`, `context`, `criterion`, `valuation_rule`, `rationale`, `status`.

Importer checks object shape, exact `assessment_schema=collective-toy-value-assessment-001`, `status=ASSESSED`, outcome/execution links, 64-hex outcome hash and digest match, and non-empty `observer`, `context`, `criterion`, `valuation_rule`, `rationale`. It rejects simultaneous `value_assessment_status`.

**Atomic predicates to verify separately:** closed 11-key schema; exact schema ID; `status=ASSESSED`; non-empty `assessment_id`; outcome ID and execution ID links; `outcome_sha256` format and recomputation; observer/context/criterion/valuation_rule/rationale each non-empty strings; no unknown keys; no null/array/primitive substitution; `value_assessment_status` absent when assessed and exactly `NOT_ASSESSED` when absent. Current importer checks schema/status, links, digest, and five contextual strings but does not enforce closed keys or validate assessment_id.

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

This register contains 16 predicate families, **not 16 atomic requirements**. The `delta_reach`, trace/step, outcome and assessment families are now decomposed into explicit candidate atomic predicates, but the complete total is still not safe to publish: the nested scenario/comparison/input/result fields, top-level optional-field type matrix, package hash negative cases, conditional package truth table, and FC-6 artifact inspections must be atomized and reconciled with actual fixtures. Next step: convert this candidate predicate list into a numbered acceptance register, mark each item `verified`, `partial`, or `pending` only after linking the exact implementation lines, test case, and CI run. Do not add more tests until that register exists.

## 11. Governance

- Keep `main` unchanged and PR #67 in draft.
- No scientific execution or empirical validation.
- Do not modify the structural detector or OCR quality work.
- Add tests only after the finite predicate list exists; change implementation only for a demonstrated failure.


## 11. GT-04 grouped implementation update — awaiting CI

Candidate implementation now enforces closed key sets for the 12-field `outcome_record` and 11-field `value_assessment`, rejects missing required fields, validates `source_kind` against the UI's finite values (`synthetic`, `observed`), checks trace digest format as well as equality, requires non-empty outcome value/unit/timing/uncertainty-status/provenance, and requires a non-empty `assessment_id`. The grouped browser suite adds adversarial cases for unknown outcome/assessment keys, invalid `source_kind`, empty outcome unit, and empty assessment ID with outer package digest recomputed.

Clarification: the approved contract does not require a separate standalone `outcome_sha256` field inside `outcome_record`. When a value assessment exists, `value_assessment.outcome_sha256` commits to the canonical outcome record; the execution trace is separately committed through `execution_trace_sha256`. These are consistency commitments, not proof of authenticity. No cryptographic signature is introduced.

The new checks and fixtures remain implementation candidates until the five required workflows pass on the exact same commit. Do not mark acceptance predicates verified before that evidence exists.


## 12. GT-05 iteration 1 — exact-head evidence and next gate

Corrected round-trip/replay test passed on exact commit `fa15baeef941e9db679a9eca25b97a0ec4a94b5e`: browser/cross-runtime `38813194707`, synthetic engine `38813194676`, governance consistency `38813194713`, browser benchmark `38813194700`, engine benchmark `38813194665`; all five concluded success. The test independently recomputes the canonical outcome-record digest, checks the explicit `ASSESSMENT` stage and replay equivalence, then imports the same artifact again and checks deterministic replay assessment text. Engineering evidence only.

**Next gate:** reconcile this inventory with the numbered acceptance register and actual fixture/test mappings before adding new adversarial tests. Complete the nested input/result schema predicate list, optional top-level artifact type matrix, package hash negatives, conditional stage/status truth table, and FC-6 artifact inspection. Do not infer that all predicates are verified merely because the grouped gate passed.


### Delta-reach follow-up — intervention-source digest fixtures

Two new browser adversarial cases now complement the baseline-source case: malformed intervention digest shape and well-formed but forged intervention digest. Both recompute result/package integrity commitments and assert the specific importer diagnostic. They are not considered verified until the exact-head browser/cross-runtime workflow passes.


### Delta-reach truncation follow-up

Direct-negative fixtures now cover a wrong-type `baseline_truncated`, an inconsistent aggregate `truncated`, and a specific `intervention_truncated` flag inconsistent with the scenario. All recompute enclosing hashes to reach the intended validator branch. These predicates remain pending until the exact-head browser/cross-runtime gate passes; other missing delta predicates remain pending.


### Delta-reach state/transition ID fixture update

Four browser adversarial cases now exercise list type and declared-ID membership for state and initially-enabled-transition deltas. Enclosing result/package hashes are recomputed to isolate the target predicate. Do not mark FC5-DELTA-005/006 verified until exact-head CI confirms all cases.


### Delta-reach trajectory validation follow-up

Three negative fixtures cover non-list trajectory deltas, an undeclared state in an ordered path, and a transition edge that is not applicable to the adjacent states. Fixtures recompute result/package hashes and assert the specific trajectory validation diagnostic. Do not mark verified until all five workflows pass on the exact candidate commit.


### Delta-reach comparison correspondence follow-up

Added three browser fixtures isolating semantic mismatch against `comparisons_to_baseline` after satisfying structural/type/ID/path checks. The cases use declared state/transition IDs and a valid ordered path, so rejection should occur at the final delta-versus-comparison equality predicate. Acceptance awaits all five workflows on the same commit.


### Atomic predicate reconciliation — candidate a7813bc

The delta-reach inventory has been reconciled to the numbered acceptance register (FC5-DELTA-001 through FC5-DELTA-012). The current validator exists at `web/index.html:270–290`; coverage gaps are now distinguished from missing implementation. On exact candidate `a7813bc221f38e023936ba6c4883b877d92729b7`, all five workflows passed: browser/cross-runtime `38817517560`, browser benchmark `38817517546`, engine benchmark `38817517566`, synthetic engine `38817517638`, governance consistency `38817517659`.

Current status: state/transition ID list predicates and ordered-path structure have direct adversarial coverage; source-hash syntax/intervention recomputation, exact delta key set, full truncation type/truth table, and exhaustive field-by-field comparison mismatches remain pending or partial. See the numbered register for the atomic statuses. No new adversarial tests are added in this iteration.


### Exact delta-reach key-set coverage

Two browser adversaries now check that `delta_reach` contains exactly the declared intervention scenario IDs: missing intervention entry and illegal baseline entry. Enclosing hashes are recomputed to reach the schema predicate. Require all five workflows on the candidate commit before marking FC5-DELTA-001/011 verified.


## Delta truncation coverage update — candidate e8e5637

The browser contract suite now adds wrong-type adversaries for `truncated` and `intervention_truncated`, completing wrong-type fixture coverage across all three delta truncation booleans when combined with the existing `baseline_truncated` case. It also adds a baseline-specific mismatch adversary that sets `baseline_truncated=true` and aggregate `truncated=true` while the baseline scenario remains untruncated. Each fixture recomputes the result and package hashes and asserts the validator diagnostic. Source commit: `e8e56377f949f03415b63aa92500bf7d42e660e9`. These additions remain pending exact-HEAD CI; do not mark the predicates verified until the browser/cross-runtime workflow passes on that commit. Full truth-table coverage remains open.
