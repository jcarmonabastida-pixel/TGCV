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

The engine emits `delta_reach[scenario_id]` for each non-baseline scenario. The current emitted field set is exactly: `baseline_source_sha256`, `intervention_source_sha256`, `reachable_states_added`, `reachable_states_removed`, `enabled_at_initial_added`, `enabled_at_initial_removed`, `trajectories_added`, `trajectories_removed`, `truncated`, `baseline_truncated`, `intervention_truncated`. The source hashes are computed over a projection containing `schema_version`, `model_id`, `initial_state`, `states`, `transitions`, `relations` (empty when absent), `rule_profile`, `exploration`, and the respective source scenario, with domain tags `delta_reach_baseline_source` and `delta_reach_intervention_source`.

**Atomic predicates to verify separately:** (1) each scenario key is a declared non-baseline scenario; (2) every delta object has only the 11 listed keys; (3) both source hashes are lowercase 64-hex strings; (4) each source hash is recomputed from the correct source projection; (5) the four state/transition delta lists are arrays of declared IDs; (6) trajectory additions/removals are arrays of valid ordered paths; (7) `truncated`, `baseline_truncated`, and `intervention_truncated` are booleans; (8) `truncated === baseline_truncated || intervention_truncated`; (9) delta arrays match the corresponding `comparisons_to_baseline` fields; (10) baseline has no delta entry; (11) each intervention has exactly one delta entry; (12) no delta entry exists without a matching comparison. Current importer code shown in this branch does not include a dedicated closed-key/field-by-field validation block for `delta_reach`; deterministic replay equality indirectly covers the supported-engine path, but these predicates lack a separately mapped negative-fixture set. Mark them partial/pending, not verified.

## 6. Execution trace (`concrete_execution_trace`)

Creation currently emits these keys:
`trace_schema`, `execution_id`, `model_id`, `input_sha256`, `scenario_id`, `candidate_index`, `submitted_transition_ids`, `initial_state`, `steps`, `final_state`, `status`, `blocked_step`, `trace_sha256`.

Importer checks object shape, exact `trace_schema=collective-toy-sequence-trace-001`, exact `status=COMPLETED`, 64-hex `trace_sha256`, and hash consistency after removing `trace_sha256`. If an outcome is included, it checks execution ID, trace hash, model ID and scenario ID links.

Trace-field decomposition (fields emitted by the UI): `trace_schema`, `execution_id`, `model_id`, `input_sha256`, `scenario_id`, `candidate_index`, `submitted_transition_ids`, `initial_state`, `steps`, `final_state`, `status`, `blocked_step`, `trace_sha256`.

Step objects emitted on success have `step`, `transition_id`, `state_before`, `state_after`, `prior_transitions`, `prerequisites`, `status`. A blocked attempt records `blocked_step={index, transition_id, reason, required_transition_ids}` and `status=BLOCKED`; a completed attempt has `status=COMPLETED` and `blocked_step=null` (or serialized null).

**Mapped grouped-test evidence (limited scope, 2026-10-17):** FC5-TRACE-016 rejects a `COMPLETED` trace with a `blocked_step` and a valid-but-incorrect `final_state`; exact test SHA `b00058d84b176ffc8c6ee2dd5e911b147442753e`, five workflows PASS (browser [39045767789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767789), engine [39045767741](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767741), engine benchmark [39045767743](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767743), browser benchmark [39045768012](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045768012), governance [39045767739](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767739)). FC5-TRACE-017 similarly covers two `BLOCKED` lifecycle predicates. These are narrow mappings, not closure of the full 22-predicate trace inventory.

**Atomic predicates to verify separately:** (1) trace is an object; (2) closed set of 13 keys; (3) exact trace schema; (4) non-empty execution/model/scenario IDs; (5) `input_sha256` is valid and equals package result/input hash; (6) scenario exists in input; (7) candidate index is null or non-negative integer; (8) submitted IDs are a string array; (9) initial/final states are declared; (10) steps is an array; (11) every step has a closed seven-key schema and valid types; (12) step numbers are ordered; (13) transition/state sequence is coherent with input edges; (14) prior-transition history is prefix-consistent; (15) prerequisites are consistent with relations and prior history; (16) status is `COMPLETED` or `BLOCKED` per policy; (17) completed traces have no block and end at the final step state; (18) blocked traces have a valid block index/reason and preserve the last successful state; (19) trace digest format; (20) trace digest recomputation; (21) outcome trace hash/execution/model/scenario cross-links; (22) trace-only packages are accepted/rejected according to an explicit policy.

**Coverage gap (reconciled against implementation at `9e9831112b19932f1335e24693d214e4daa933cb`, 2026-10-17):** the current importer DOES apply a closed 13-key allowlist to the top-level trace, requires all listed keys, applies a closed seven-key schema to every step, and validates several core field types and lifecycle semantics. Therefore, do not treat absence of those validator blocks as a current implementation defect. Remaining evidence gaps are systematic negative fixtures for unknown top-level trace key, unknown/missing/wrong-type step fields, candidate_index/submitted IDs/steps wrong-type combinations, and required/unknown `blocked_step` keys/types; current checks exist for many of these but are not all individually exercised adversarially. Policy A is explicit in contract § trace lifecycle: COMPLETED/BLOCKED traces are exportable and inspectable; COMPLETED may exist without outcome; outcomes require COMPLETED; BLOCKED cannot carry an outcome/assessment for a completed observation. Grouped browser tests cover BLOCKED round-trip, rejection of outcome linked to BLOCKED, and COMPLETED-without-outcome mapped to EXECUTION/NOT_ASSESSED. FC5-TRACE-016/017 add selected lifecycle adversaries. These are limited mappings, not closure of the 22-predicate trace inventory.

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
| FC5-TRACE-01 | Trace schema, types, steps, status, hash and links | partial; policy A resolved; implementation has closed trace/step keys and core semantic checks, but grouped negative-fixture mapping incomplete |
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


### FC5-TRACE-015 policy/status reconciliation (2026-10-17)

The stale statement that the BLOCKED policy is unresolved is superseded. Contract § trace lifecycle and tests establish policy A: both statuses remain inspectable/exportable; COMPLETED may lack outcome; outcome requires COMPLETED; BLOCKED cannot carry an outcome or assessment representing a completed observation. Tests cover blocked round-trip, outcome rejection on BLOCKED, and COMPLETED-without-outcome as EXECUTION/NOT_ASSESSED. The exact test SHA `b00058d84b176ffc8c6ee2dd5e911b147442753e` passed all five workflows: browser [39045767789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767789), engine [39045767741](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767741), engine benchmark [39045767743](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767743), browser benchmark [39045768012](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045768012), governance [39045767739](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767739).

### FC5-TRACE schema coverage reconciliation (2026-10-17)

Reinspection of `web/index.html` confirms a top-level trace closed-key allowlist and required-key check; each step has an exact seven-key schema check; core trace/step field types, state/edge sequence, final state, COMPLETED/BLOCKED lifecycle, blocked reason/prerequisites and trace digest are validated. The inventory's prior assertion that no trace/step closed-key checks exist was stale and has been corrected. The remaining issue is evidence mapping: add grouped adversarial cases for the highest-risk untested wrong-type/unknown-key combinations rather than one test per field. This correction does not claim those combinations have all been tested.


### BLOCKED metadata schema evidence update (2026-10-17)

The latest grouped browser suite on test SHA `a5a8753f4609d4e4708ec311a20e3297bd288a2d` now covers two additional `blocked_step` adversaries: unknown key and wrong-type `required_transition_ids` (string instead of array). All five workflows passed: governance [39051214686](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214686), engine [39051214571](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214571), browser/cross-runtime [39051214639](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214639), engine benchmark [39051214567](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214567), browser benchmark [39051214613](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214613). These add evidence for selected predicates only; the full blocked metadata and trace schema/type matrix remains partial.


### FC5-TRACE-014 — temporal prerequisite semantic evidence mapping (2026-10-17)

The active GT-03 grouped browser suite contains two adversaries relevant to trace prerequisite semantics: it rejects a BLOCKED trace that omits required unsatisfied temporal prerequisites, and rejects a forged blocked reason, even when trace/package digests are recomputed. Exact test head `46180bb0f21bbba302a2ef0fd4805a8eb1ddf6f9` passed all five workflows: governance [39052324930](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324930), engine [39052324987](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324987), browser/cross-runtime [39052324916](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324916), engine benchmark [39052324943](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324943), browser benchmark [39052324951](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324951). These establish selected semantic predicates; they do not exhaustively verify each successful step's prerequisites against all relations and prior-history combinations.


### FC5-SEC-001/002 — existing UI assertions mapped (2026-10-17)

The browser suite already asserts that the footer frames hashes as reproducibility support, rejects claims that unkeyed SHA-256 authenticates package/origin, and checks importer wording distinguishing internal consistency from origin authenticity (`ui_contract_test.cjs` lines 22–31 at test SHA `754c1bcaf1c3f67076ec20cdeab72621609bcb88`). These selected UI predicates are mapped as covered; this does not mean the package has cryptographic authentication or that all surfaces have exhaustive wording checks. Four test workflows passed on that test SHA—engine [39052689873](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689873), engine benchmark [39052689875](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689875), browser benchmark [39052689877](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689877), browser/cross-runtime [39052689839](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689839); governance was absent on that exact SHA. This documentation update requires a fresh exact-head five-workflow gate.


### FC5-TRACE-010 — executed-step schema evidence (2026-10-17)

Current implementation enforces the closed seven-key schema for each step. The grouped browser test adds two adversarial checks: unknown step key and wrong-type `prerequisites` (string instead of array), recomputing trace and package digests before asserting rejection. Exact test SHA `294e20fb4cc2483078c6b70f2aa85a66acdb54d7` passed all five workflows: governance [39053882898](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882898), engine [39053882899](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882899), browser/cross-runtime [39053882881](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882881), engine benchmark [39053882880](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882880), browser benchmark [39053882886](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882886). This is evidence for two predicates only; full step field schema/type coverage remains partial.

## Trace schema evidence delta — 2026-10-17

The browser suite contains grouped adversaries for wrong-type `submitted_transition_ids` (string instead of array), undeclared `final_state`, and wrong-type `steps` (string instead of array), introduced in test commit `be1cc399bcfe6510910ee35bb7506753dddd9ffa`. The existing `unknown-trace-key`, `unknown-step-key`, and `wrong-type-step-prerequisites` cases cover selected closed-key and nested-step predicates.

The three grouped cases are now verified on code head `a9bce4c7d404aaaee75b8a7b2e2ee638afbffe32`, which contains the cases and passed all five required workflows: governance [39062553540](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39062553540), synthetic engine [39062553561](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39062553561), browser/cross-runtime [39062553571](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39062553571), engine benchmark [39062553529](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39062553529), and browser benchmark [39062553596](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39062553596). The cases recompute dependent digests and verify rejection of the wrong-type `submitted_transition_ids`, an undeclared `final_state`, and wrong-type `steps`. This verifies those three predicates only; the wider trace schema/type matrix and overall FC-5/FC-6 acceptance remain partial.

The broader 22-predicate trace inventory and all FC-5/FC-6 acceptance remain partial; no scientific execution or promotion to `main`.

### FC5-REPLAY-003 — legacy-shaped projection (scope correction, 2026-10-17)

The browser suite exercises a constructed `collective-toy-browser-run-001`-shaped package with `value_assessment_status=NOT_ASSESSED` and rejects an incomplete variant missing that field. The positive replay and negative rejection cases passed all five workflows on exact test SHA `e327b4ae489472c3a65b2a2e4141cf71d6322d14`: governance [39059726191](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39059726191), synthetic engine [39059726181](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39059726181), browser/cross-runtime [39059726168](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39059726168), engine benchmark [39059726093](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39059726093), browser benchmark [39059726208](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39059726208).

**Verified:** behavior for the constructed legacy-shaped projection. **Not verified:** replay compatibility with a real historical package artifact. No original package bytes/provenance and independently preserved expected output are registered under `COMPATIBILITY_FIXTURE_REGISTER_001.md`; historical profile compatibility remains partial/unverified until those admission criteria are met. No production change, scientific execution, or promotion to `main`.
