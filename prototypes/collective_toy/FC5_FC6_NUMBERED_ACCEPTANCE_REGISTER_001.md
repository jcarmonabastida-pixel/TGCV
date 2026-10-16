# FC-5 / FC-6 numbered acceptance register — draft 001

- **Status:** working acceptance register; not closure evidence.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Basis:** `FC5_FC6_PACKAGE_SCHEMA_INVENTORY_001.md`, contract `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`, implementation `web/index.html`, tests `web/ui_contract_test.cjs`.
- **Scope boundary:** no scientific execution; no detector/OCR changes; `main` unchanged.
- **State meanings:** `verified` = predicate is covered by mapped test evidence and passing CI on the cited commit; `partial` = relevant evidence exists but does not establish the full predicate or its interactions; `pending` = not demonstrated or unresolved contract decision. A dedicated test per predicate is not required.
- **Important:** identifiers below are atomic acceptance predicates for traceability, not a prescription to create one test per predicate. One contract, integration, replay, or adversarial test may cover multiple predicates. Rows marked `GROUP` are explicitly not atomic and must be expanded before a final denominator can be published.

## A. Package envelope

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-PKG-001 | Reject unknown top-level package key even when package hash is recomputed | verified | Existing adversarial test; latest five-workflow PASS for `a90b69a6` |
| FC5-PKG-002 | Reject missing or non-object `input` | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-003 | Reject missing or non-object `result` | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-004 | Reject unsupported `package_version` when outer hash is recomputed | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-005 | Reject absent `package_sha256` | verified | Grouped adversarial cases (missing, malformed, incorrect digest) rejected with integrity diagnostic; browser/cross-runtime run [38939926496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926496), exact SHA `a50e04119a45f2a8999dd0fb886844f4355f45b5`. |
| FC5-PKG-006 | Reject malformed `package_sha256` format | verified | Grouped adversarial cases (missing, malformed, incorrect digest) rejected with integrity diagnostic; browser/cross-runtime run [38939926496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926496), exact SHA `a50e04119a45f2a8999dd0fb886844f4355f45b5`. |
| FC5-PKG-007 | Reject incorrect package digest | verified | Grouped adversarial cases (missing, malformed, incorrect digest) rejected with integrity diagnostic; browser/cross-runtime run [38939926496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926496), exact SHA `a50e04119a45f2a8999dd0fb886844f4355f45b5`. |
| FC5-PKG-008 | Reject wrong type for `concrete_execution_trace` | verified | Grouped adversarial test rejects non-object section with a recomputed outer package digest and an explicit diagnostic; browser/cross-runtime run [38940845328](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38940845328), exact SHA `5e28277ef6ed04d70b855b1dcb5894ce21158d22`. |
| FC5-PKG-009 | Reject wrong type for `outcome_record` | verified | Grouped adversarial test rejects non-object section with a recomputed outer package digest and an explicit diagnostic; browser/cross-runtime run [38940845328](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38940845328), exact SHA `5e28277ef6ed04d70b855b1dcb5894ce21158d22`. |
| FC5-PKG-010 | Reject wrong type for `value_assessment` | verified | Grouped adversarial test rejects non-object section with a recomputed outer package digest and an explicit diagnostic; browser/cross-runtime run [38940845328](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38940845328), exact SHA `5e28277ef6ed04d70b855b1dcb5894ce21158d22`. |
| FC5-PKG-011 | Enforce assessment/status conditional combinations | verified (candidate; fresh exact-head gate pending after register update) | Grouped truth-table test enumerates 32 combinations (4 `package_stage` values × 8 trace/outcome/assessment presence patterns), accepts the four expected combinations and rejects 28 invalid combinations. All five workflows PASS on exact SHA `5c11cfa34a5030a31df88c3ef1859e783efae276`: engine [38981171858](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171858), browser/cross-runtime [38981171964](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171964), engine performance [38981171928](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171928), browser performance [38981171867](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171867), governance [38981171846](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171846). Status field is also set to `NOT_ASSESSED` without an assessment artifact and omitted when an assessment artifact exists. |
| FC5-PKG-012 | Reject unknown `value_assessment_status` values | verified | Grouped adversarial cases `PENDING_REVIEW`, `null`, and numeric status all rejected with explicit `value_assessment_status=NOT_ASSESSED` diagnostic after recomputing the outer package digest; browser/cross-runtime run [38953698867](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38953698867), exact SHA `8ee6cf833a0b046a83b550c2361438705cccdbd9`. |

## B. Input model

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-IN-001 | Require exact input schema version | partial | Validator exists; dedicated negative fixture mapping incomplete |
| FC5-IN-002 | Require non-empty string model ID | partial | Validator exists; dedicated wrong-type/empty fixtures not mapped |
| FC5-IN-003 | Require initial state to reference a declared state | partial | Semantic validation exists; dedicated negative fixture not mapped |
| FC5-IN-004 | Require non-empty states array within maximum size | partial | Validator exists; boundaries not systematically tested |
| FC5-IN-005 | Reject duplicate or empty state IDs | partial | Validator exists; fixture mapping incomplete |
| FC5-IN-006 | Require transitions array within maximum size | partial | Validator exists; boundaries not systematically tested |
| FC5-IN-007 | Reject duplicate/empty transition IDs | partial | Validator exists; fixture mapping incomplete |
| FC5-IN-008 | Require transition endpoints to reference declared states | partial | Validator exists; fixture mapping incomplete |
| FC5-IN-009 | Enforce relation object closed-key schema | partial | Implementation uses closed keys; adversarial fixture not mapped |
| FC5-IN-010 | Enforce relation type/profile compatibility | partial | Validator exists; negative fixture mapping incomplete |
| FC5-IN-011 | Require relation references to exist and differ where required | partial | Validator exists; fixture mapping incomplete |
| FC5-IN-012 | Enforce rule-profile closed-key schema and supported values | partial | Validator exists; negative fixtures not mapped |
| FC5-IN-013 | Require non-empty scenarios and unique scenario IDs | partial | Validator exists; negative fixtures not mapped |
| FC5-IN-014 | Require baseline scenario | partial | Validator exists; dedicated fixture not mapped |
| FC5-IN-015 | Validate disabled transition references | partial | Validator exists; dedicated fixture not mapped |
| FC5-IN-016 | Enforce exploration closed-key schema and integer bounds | partial | Validator exists; boundary matrix not mapped |
| FC5-IN-017 | Reject unknown keys at every input nesting level | partial | Code has closed-key checks; not all nesting levels have adversarial tests |

## C. Result envelope and scenario results

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-RES-001 | Reject unknown top-level result fields despite recomputed result/package hashes | verified | Added in `a90b69a6`; all five workflows PASS |
| FC5-RES-002 | Require supported result schema and equality with input schema | partial | Code/replay enforce; dedicated negative fixture not mapped |
| FC5-RES-003 | Require result model ID to match input | partial | Code/replay enforce; dedicated negative fixture not mapped |
| FC5-RES-004 | Require canonical rule profile equality with input | partial | Code/replay enforce; dedicated negative fixture not mapped |
| FC5-RES-005 | Require validation status exactly PASS for exported successful result | partial | Code check exists; dedicated negative fixture not mapped |
| FC5-RES-006 | Require result scenario keys to match input scenarios exactly | partial | Code/replay enforce; exhaustive unknown/missing cases not mapped |
| FC5-RES-007 | Require baseline comparisons for every non-baseline scenario and no others | partial | Code/replay enforce; exhaustive negative fixtures not mapped |
| FC5-RES-008 | Validate semantic identity version/hash conditional pairing | partial | Implementation exists; adversarial matrix incomplete |
| FC5-RES-009 | Validate input hash format and recomputation | partial | Code check exists; dedicated malformed/incorrect fixtures not mapped |
| FC5-RES-010 | Validate result hash format and recomputation | partial | Code check exists; dedicated malformed/incorrect fixtures not mapped |
| FC5-SCEN-001 | Enforce scenario result closed-key schema | partial | Validator exists; per-key negative matrix absent |
| FC5-SCEN-002 | Require scenario key to equal nested scenario ID | partial | Validator exists; dedicated fixture not mapped |
| FC5-SCEN-003 | Validate scenario transition/state arrays and references | partial | Validator exists; exhaustive invalid-reference cases not mapped |
| FC5-SCEN-004 | Validate trajectory paths as ordered valid transitions | partial | Validator exists; adversarial sequence matrix incomplete |
| FC5-SCEN-005 | Require boolean truncation flag | partial | Validator exists; wrong-type fixture not mapped |
| FC5-SCEN-006 | Enforce exploration_bounds closed keys and non-negative integer bounds | partial | Validator exists; boundaries/wrong types not mapped |
| FC5-SCEN-007 | Validate relation effects and temporal-prerequisite fields against active profile | partial | Validator exists; profile-specific negative matrix incomplete |
| FC5-SCEN-008 | Enforce blocked temporal step schema, references, and non-empty missing prerequisites | partial | Validator exists; dedicated fixtures not mapped |

## D. Baseline comparison and delta reach

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-CMP-001 | Enforce comparison closed-key schema | partial | Validator exists; negative fixture not mapped |
| FC5-CMP-002 | Require exactly one comparison per non-baseline scenario | partial | Code/replay; exhaustive fixture mapping incomplete |
| FC5-CMP-003 | Validate intervention disabled-transition schema and references | partial | Validator exists; negative fixture not mapped |
| FC5-CMP-004 | Validate added/removed state and transition ID arrays | partial | Validator exists; wrong-type/invalid-ID matrix incomplete |
| FC5-CMP-005 | Validate added/removed trajectories as coherent paths | partial | Validator exists; adversarial path cases incomplete |
| FC5-CMP-006 | Require boolean comparison truncation | partial | Validator exists; wrong-type fixture not mapped |
| FC5-DELTA-001 | Require exactly one delta entry per non-baseline scenario and none for baseline | pending | Dedicated delta schema checks not located |
| FC5-DELTA-002 | Reject unknown delta object fields | pending | Closed-key validation/test not located |
| FC5-DELTA-003 | Validate baseline/intervention source hash format | pending | Dedicated malformed hash fixtures not located |
| FC5-DELTA-004 | Recompute source hashes from correct canonical source projection | partial | Engine computes; importer negative cases not mapped |
| FC5-DELTA-005 | Validate added/removed state and transition arrays against declared IDs | pending | Dedicated importer validation/test not located |
| FC5-DELTA-006 | Validate trajectory delta arrays as ordered valid paths | pending | Dedicated importer validation/test not located |
| FC5-DELTA-007 | Require boolean truncation fields | pending | Dedicated importer validation/test not located |
| FC5-DELTA-008 | Require aggregate truncated flag to equal baseline OR intervention truncation | pending | Dedicated check/test not located |
| FC5-DELTA-009 | Require delta arrays to match baseline comparison fields | partial | Replay equality indirectly checks supported-engine path; no targeted tampering fixture |
| FC5-DELTA-010 | Reject delta entry without matching comparison | pending | Dedicated fixture not located |

## E. Execution trace and steps

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-TRACE-001 | Require trace object and exact trace schema | partial | Schema check exists; negative matrix incomplete |
| FC5-TRACE-002 | Enforce closed 13-key trace schema | pending | Importer lacks closed-key allowlist |
| FC5-TRACE-003 | Require non-empty execution/model/scenario IDs | partial | Link checks exist; individual type/empty fixtures not mapped |
| FC5-TRACE-004 | Require trace input hash to match package input/result | partial | Need exact implementation cross-check and negative fixture |
| FC5-TRACE-005 | Require scenario to exist in input | partial | Dedicated negative fixture not mapped |
| FC5-TRACE-006 | Require candidate index null or non-negative integer | pending | Dedicated validation/test not located |
| FC5-TRACE-007 | Require submitted transition IDs to be a string array | pending | Dedicated validation/test not located |
| FC5-TRACE-008 | Require initial/final states to be declared | pending | Dedicated validation/test not located |
| FC5-TRACE-009 | Require steps to be an array | pending | Dedicated validation/test not located |
| FC5-TRACE-010 | Enforce closed seven-key schema and types for each step | pending | Importer lacks step closed-key validation |
| FC5-TRACE-011 | Require ordered step indices | pending | Dedicated validation/test not located |
| FC5-TRACE-012 | Require transition/state sequence to follow input edges | verified | Grouped adversary passed in browser/cross-runtime run [38928105212](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38928105212) on test commit `9001838676306aea4a3f10be8b9914d3729b3a21`; the altered destination is rejected after dependent digests are recomputed. Profile compatibility remains separate. |
| FC5-TRACE-013 | Require prior-transition history to be prefix-consistent | pending | Dedicated validation/test not located |
| FC5-TRACE-014 | Require prerequisites to match relations and prior history | pending | Dedicated validation/test not located |
| FC5-TRACE-015 | Define and enforce COMPLETED/BLOCKED trace policy | pending | Contract decision unresolved |
| FC5-TRACE-016 | Require completed trace to have no blocked step and correct final state | pending | Dedicated validation/test not located |
| FC5-TRACE-017 | Require blocked trace to have coherent block index/reason/last state | pending | Dedicated validation/test not located |
| FC5-TRACE-018 | Validate trace digest format and recomputation | partial | Implemented and tested indirectly; targeted tampering case not mapped |
| FC5-TRACE-019 | Enforce outcome-to-trace execution/hash/model/scenario cross-links | partial | Multiple cross-link adversarial tests exist; full predicate mapping needed |
| FC5-TRACE-020 | Define acceptance policy for trace-only package without outcome | pending | Contract decision not documented |

## F. Outcome and value assessment

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-OUT-001 | Require exact outcome schema and object type | verified (candidate; exact-head gate refreshed after register update) | Closed 12-key schema and object-type guard; Eight grouped cases replace the record with null, array, string, and number for both `outcome_record` and `value_assessment`; outer package digest is recomputed. All five workflows PASS on exact SHA `b44d4618bd06d691da1e0b1d58ca0466c85026dd`: engine [38966431461](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431461), browser/cross-runtime [38966431451](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431451), engine performance [38966431481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431481), browser performance [38966431405](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431405), governance [38966431389](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431389). |
| FC5-OUT-002 | Enforce closed 12-key outcome schema | verified (candidate; exact-head CI pending after register update) | Closed-key allowlists added in production importer and both forged-field cases pass on exact SHA `781288c6c75193802a38e510acc4e20d6321b2d3`; browser/cross-runtime run [38956047097](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38956047097). Four workflows pass on this SHA; governance must be rechecked after this register update. |
| FC5-OUT-003 | Require non-empty outcome ID and value | partial | Implemented; individual type/empty fixtures not mapped |
| FC5-OUT-004 | Enforce allowed `source_kind` values | verified (candidate; full exact-SHA gate pending) | Importer now permits only `synthetic` or `observed`; adversarial values `inferred`, `null`, and numeric are rejected in grouped browser/cross-runtime run [38957232585](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38957232585), exact SHA `75943b24ae965aaf1f6a5a2297846ced84aab715`. |
| FC5-OUT-005 | Validate value/unit/timing/uncertainty/provenance types and constraints | partial | Importer now requires non-empty strings for `value`, `unit`, `timing`, `uncertainty_status`, and `provenance`; adversarial unit-empty, timing-null, uncertainty-number, and provenance-empty cases pass on browser/cross-runtime run [38957232585](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38957232585), exact SHA `75943b24ae965aaf1f6a5a2297846ced84aab715`. Additional domain-specific constraints remain to be established from the contract. |
| FC5-OUT-006 | Enforce execution/trace hash/model/scenario links | verified (candidate; exact-SHA gate must be refreshed after register update) | Existing adversarial checks reject forged execution ID, model ID, and scenario ID; new trace-digest mismatch also rejected. Grouped hash-consistent linkage adversaries pass in browser/cross-runtime run [38958362979](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38958362979), exact SHA `528d14b403a5f16e3534975d41e5897c7fbdf912`; all five workflows PASS on that SHA. |
| FC5-OUT-007 | Reject unknown outcome fields | verified (candidate; exact-head CI pending after register update) | Closed-key allowlists added in production importer and both forged-field cases pass on exact SHA `781288c6c75193802a38e510acc4e20d6321b2d3`; browser/cross-runtime run [38956047097](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38956047097). Four workflows pass on this SHA; governance must be rechecked after this register update. |
| FC5-OUT-008 | Reject null/array/primitive substitution for outcome object/fields | partial | Record-level substitutions `null`, array, string, and number are rejected. Per-field null/array/primitive coverage is not exhaustive yet. Eight grouped cases replace the record with null, array, string, and number for both `outcome_record` and `value_assessment`; outer package digest is recomputed. All five workflows PASS on exact SHA `b44d4618bd06d691da1e0b1d58ca0466c85026dd`: engine [38966431461](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431461), browser/cross-runtime [38966431451](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431451), engine performance [38966431481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431481), browser performance [38966431405](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431405), governance [38966431389](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431389). |
| FC5-OUT-009 | Recompute outcome digest when linked assessment exists | verified (candidate; exact-SHA gate must be refreshed after register update) | New adversary alters outcome trace digest, recomputes outcome_sha256 and outer package digest, and is rejected on the independent trace-link invariant. Grouped hash-consistent linkage adversaries pass in browser/cross-runtime run [38958362979](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38958362979), exact SHA `528d14b403a5f16e3534975d41e5897c7fbdf912`; all five workflows PASS on that SHA. |
| FC5-VAL-001 | Require exact assessment schema and object type | verified (candidate; exact-head gate refreshed after register update) | Closed 11-key schema and object-type guard; Eight grouped cases replace the record with null, array, string, and number for both `outcome_record` and `value_assessment`; outer package digest is recomputed. All five workflows PASS on exact SHA `b44d4618bd06d691da1e0b1d58ca0466c85026dd`: engine [38966431461](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431461), browser/cross-runtime [38966431451](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431451), engine performance [38966431481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431481), browser performance [38966431405](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431405), governance [38966431389](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431389). |
| FC5-VAL-002 | Enforce closed 11-key assessment schema | verified (candidate; exact-head CI pending after register update) | Closed-key allowlists added in production importer and both forged-field cases pass on exact SHA `781288c6c75193802a38e510acc4e20d6321b2d3`; browser/cross-runtime run [38956047097](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38956047097). Four workflows pass on this SHA; governance must be rechecked after this register update. |
| FC5-VAL-003 | Require status exactly ASSESSED | partial | Implemented; wrong-type/value matrix incomplete |
| FC5-VAL-004 | Require non-empty assessment ID | verified (candidate; full exact-SHA gate pending) | Importer now rejects empty, null, and numeric `assessment_id`; grouped browser/cross-runtime run [38957232585](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38957232585), exact SHA `75943b24ae965aaf1f6a5a2297846ced84aab715`. |
| FC5-VAL-005 | Enforce outcome ID and execution ID links | verified (candidate; exact-SHA gate must be refreshed after register update) | Existing forged assessment execution-ID case plus new forged assessment outcome-ID case are rejected. Grouped hash-consistent linkage adversaries pass in browser/cross-runtime run [38958362979](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38958362979), exact SHA `528d14b403a5f16e3534975d41e5897c7fbdf912`; all five workflows PASS on that SHA. |
| FC5-VAL-006 | Validate outcome hash format and recomputation | verified (candidate; exact-SHA gate must be refreshed after register update) | New adversary supplies a well-formed 64-character but incorrect outcome_sha256 and is rejected; dependent outer package digest is recomputed. Grouped hash-consistent linkage adversaries pass in browser/cross-runtime run [38958362979](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38958362979), exact SHA `528d14b403a5f16e3534975d41e5897c7fbdf912`; all five workflows PASS on that SHA. |
| FC5-VAL-007 | Require observer/context/criterion/rule/rationale to be non-empty strings | partial | Missing criterion tested; wrong-type and remaining fields not individually mapped |
| FC5-VAL-008 | Reject unknown assessment fields | verified (candidate; exact-head CI pending after register update) | Closed-key allowlists added in production importer and both forged-field cases pass on exact SHA `781288c6c75193802a38e510acc4e20d6321b2d3`; browser/cross-runtime run [38956047097](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38956047097). Four workflows pass on this SHA; governance must be rechecked after this register update. |
| FC5-VAL-009 | Reject null/array/primitive substitution for assessment fields | partial | Record-level substitutions `null`, array, string, and number are rejected. Per-field null/array/primitive coverage is not exhaustive yet. Eight grouped cases replace the record with null, array, string, and number for both `outcome_record` and `value_assessment`; outer package digest is recomputed. All five workflows PASS on exact SHA `b44d4618bd06d691da1e0b1d58ca0466c85026dd`: engine [38966431461](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431461), browser/cross-runtime [38966431451](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431451), engine performance [38966431481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431481), browser performance [38966431405](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431405), governance [38966431389](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38966431389). |
| FC5-VAL-010 | Enforce assessment/status conditional truth table | verified (candidate; fresh exact-head gate pending after register update) | Grouped truth-table test enumerates 32 combinations (4 `package_stage` values × 8 trace/outcome/assessment presence patterns), accepts the four expected combinations and rejects 28 invalid combinations. All five workflows PASS on exact SHA `5c11cfa34a5030a31df88c3ef1859e783efae276`: engine [38981171858](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171858), browser/cross-runtime [38981171964](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171964), engine performance [38981171928](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171928), browser performance [38981171867](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171867), governance [38981171846](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171846). This closes the previously open stage/artifact-presence matrix; it does not claim scientific validation of outcome/value semantics. |

## G. Integrity/security, replay, and FC-6

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-SEC-001 | Explain that unkeyed hashes provide consistency, not origin authenticity | partial | Wording exists in one UI path; contract/UI consistency incomplete |
| FC5-SEC-002 | Regression test prevents claims of authentication based on SHA-256 alone | pending | Dedicated assertion not located |
| FC5-REPLAY-001 | Import replays independently and matches exported result for valid package | verified | Clean-source replay PASS on exact candidate SHA `0deec788f2ae8c958c6f20fac478ec83c412507a`, run [38925343766](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38925343766). GT-05 single-scenario coverage remains a separate pending item. |
| FC5-REPLAY-002 | Replay mismatch is rejected | verified | Self-consistent divergence adversary passed in browser/cross-runtime run [38929033347](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38929033347) on exact candidate SHA `0c0cecdd73502fb9699e89ed598e1eab141c516a`; altered result and recomputed semantic/result/package digests, then importer rejected because independent replay differed. |
| FC5-REPLAY-003 | Legacy/optional semantic identity compatibility behaves as documented | partial | Browser/cross-runtime run [38931716530](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38931716530) PASS on exact SHA `4207f3f87bdbbae5dea6b4e643d3f87c9c12299a`. The grouped adversary now verifies fail-closed rejection and an explicit diagnostic when a legacy-shaped package omits `value_assessment_status=NOT_ASSESSED`. This verifies rejection of this incomplete package, not successful replay or general historical-profile compatibility; the broader compatibility matrix remains partial. |
| FC6-CI-001 | All required workflows pass on the exact candidate commit | verified (candidate gate) | All five required workflows PASS on exact SHA `a50e04119a45f2a8999dd0fb886844f4355f45b5`: engine [38939926646](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926646), browser/navigation + cross-runtime [38939926496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926496), engine performance [38939926564](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926564), browser performance [38939926838](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926838), governance [38939926452](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926452). Any subsequent commit requires a fresh exact-SHA gate before final closure. |
| FC6-CLEAN-001 | Clean-source archive replay passes on exact candidate commit | verified (candidate gate) | Engine clean-source archive replay and browser/cross-runtime replay passed in required workflows on exact SHA `a50e04119a45f2a8999dd0fb886844f4355f45b5`; see [engine run 38939926646](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926646) and [browser run 38939926496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38939926496). Recheck after any later candidate change. |
| FC6-ART-001 | Inspect final exported package artifacts against contract | partial | Need artifact list and per-artifact evidence |
| FC6-SCOPE-001 | CI/evidence explicitly avoid claiming scientific validity from synthetic tests | partial | Governance states boundary; final evidence bundle mapping needed |
| FC6-MAIN-001 | Confirm main unchanged and PR #70 remains draft | verified (snapshot) | At verification: `main` SHA `29515bea7e0cc5413bfe1c234e83927841bfaa02`; PR [#70](https://github.com/jcarmonabastida-pixel/TGCV/pull/70) is open/draft, base `main`, head `a50e04119a45f2a8999dd0fb886844f4355f45b5`. Recheck before any promotion. |

## H. Items deliberately not counted yet

These are known gaps in the atomic inventory and must be expanded before publishing a final denominator:
1. Wrong-type and missing-field predicates for every nested scenario-result field, comparison field, and input field.
2. Package optional-field types and the full trace/outcome/assessment/status presence truth table.
3. All numeric lower/upper boundaries, maximum array sizes, duplicate IDs, and malformed identifiers.
4. Complete `delta_reach` relationship and hash projections, including whether a supplied delta must be independently recomputed on import.
5. Full trace semantic checks for relation-guarded and temporal-prerequisite rule profiles.
6. FC-6 artifact inventory: exact expected files, provenance/hash checks, and non-claim statements.
7. A contract decision for BLOCKED traces and trace-only packages.

**Counting rule:** do not report a definitive total until section H has been atomized and each row in sections A–G is reconciled to exact implementation location, named test, and passing CI evidence. Do not add tests until this register is reviewed and reconciled; then work on the first proven uncovered predicate only.
