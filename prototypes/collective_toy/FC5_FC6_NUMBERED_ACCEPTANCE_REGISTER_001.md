# FC-5 / FC-6 numbered acceptance register — draft 001

- **Status:** working acceptance register; not closure evidence.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Basis:** `FC5_FC6_PACKAGE_SCHEMA_INVENTORY_001.md`, contract `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`, implementation `web/index.html`, tests `web/ui_contract_test.cjs`.
- **Scope boundary:** no scientific execution; no detector/OCR changes; `main` unchanged.
- **State meanings:** `verified` = predicate is covered by mapped test evidence and passing CI on the cited commit; `partial` = relevant evidence exists but does not establish the full predicate or its interactions; `pending` = not demonstrated or unresolved contract decision. A dedicated test per predicate is not required.
- **Important:** identifiers below are atomic acceptance predicates for traceability, not a prescription to create one test per predicate. One contract, integration, replay, or adversarial test may cover multiple predicates. Rows marked `GROUP` are explicitly not atomic and must be expanded before a final denominator can be published.

> **Canonical-register rule (2026-10-16):** This document contains append-only iteration notes and older predicate tables, so repeated IDs across those historical entries are not independent active requirements. For current delta-reach acceptance, the canonical mapping is the single table under **“Delta-reach atomic acceptance reconciliation — candidate a7813bc”**, with later “FC5-DELTA-001/011 — exact intervention-key set adversaries” serving as evidence history only. Do not merge statuses from older tables or count duplicate labels as separate predicates. The canonical table's status must be updated only when exact-head test/run evidence supports it. The truncation predicates are further refined by the later direct fixture notes and must remain partial wherever baseline-specific consistency or wrong-type coverage for all three flags is missing.

## A. Package envelope

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-PKG-001 | Reject unknown top-level package key even when package hash is recomputed | verified | Existing adversarial test; latest five-workflow PASS for `a90b69a6` |
| FC5-PKG-002 | Reject missing or non-object `input` | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-003 | Reject missing or non-object `result` | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-004 | Reject unsupported `package_version` when outer hash is recomputed | verified | Existing adversarial test; latest five-workflow PASS |
| FC5-PKG-005 | Reject absent `package_sha256` | pending | Dedicated fixture not located |
| FC5-PKG-006 | Reject malformed `package_sha256` format | pending | Dedicated fixture not located |
| FC5-PKG-007 | Reject incorrect package digest | partial | Hash check exists; exact adversarial fixture mapping incomplete |
| FC5-PKG-008 | Reject wrong type for `concrete_execution_trace` | pending | No dedicated type fixture mapped |
| FC5-PKG-009 | Reject wrong type for `outcome_record` | pending | No dedicated type fixture mapped |
| FC5-PKG-010 | Reject wrong type for `value_assessment` | pending | No dedicated type fixture mapped |
| FC5-PKG-011 | Enforce assessment/status conditional combinations | partial | Positive assessed and NOT_ASSESSED round trips; truth table incomplete |
| FC5-PKG-012 | Reject unknown `value_assessment_status` values | pending | Dedicated fixture not located |

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
| FC5-DELTA-007 | Require boolean truncation fields | verified | Browser adversary rejects string `baseline_truncated="false"` with a field-specific diagnostic; enclosing result/package hashes are recomputed. Exact-head CI on `495dadb6e02b2c810e0750cfebbf2a745dec418f`: browser/cross-runtime 38818696371, engine 38818696355, governance 38818696366, browser benchmark 38818696348, engine benchmark 38818696411 — all PASS. |
| FC5-DELTA-008 | Require aggregate truncated flag to equal baseline OR intervention truncation, and both scenario flags to match their scenario results | verified | Two browser adversaries reject aggregate `truncated=true` when both scenario flags are false, and `intervention_truncated=true` when the intervention scenario is actually untruncated. Each recomputes enclosing result/package hashes and asserts the targeted diagnostic. Exact-head five-workflow CI on `495dadb6e02b2c810e0750cfebbf2a745dec418f` passed (runs 38818696371, 38818696355, 38818696366, 38818696348, 38818696411). |
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
| FC5-TRACE-012 | Require transition/state sequence to follow input edges | pending | Dedicated replay/semantic trace validator not located |
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
| FC5-OUT-001 | Require exact outcome schema and object type | partial | Schema check exists; negative matrix incomplete |
| FC5-OUT-002 | Enforce closed 12-key outcome schema | pending | Importer lacks closed-key allowlist |
| FC5-OUT-003 | Require non-empty outcome ID and value | partial | Implemented; individual type/empty fixtures not mapped |
| FC5-OUT-004 | Enforce allowed source_kind values | pending | UI has options; importer enum validation not located |
| FC5-OUT-005 | Validate value/unit/timing/uncertainty/provenance types and constraints | pending | Contract constraints/test mapping incomplete |
| FC5-OUT-006 | Enforce execution/trace hash/model/scenario links | partial | Some adversarial link tests pass; full mapping incomplete |
| FC5-OUT-007 | Reject unknown outcome fields | pending | No closed-key validation |
| FC5-OUT-008 | Reject null/array/primitive substitution for outcome object/fields | pending | Dedicated fixtures not located |
| FC5-OUT-009 | Recompute outcome digest when linked assessment exists | partial | Assessment hash check exists; direct tampering coverage incomplete |
| FC5-VAL-001 | Require exact assessment schema and object type | partial | Schema check exists; negative matrix incomplete |
| FC5-VAL-002 | Enforce closed 11-key assessment schema | pending | Importer lacks closed-key allowlist |
| FC5-VAL-003 | Require status exactly ASSESSED | partial | Implemented; wrong-type/value matrix incomplete |
| FC5-VAL-004 | Require non-empty assessment ID | pending | Explicit check not located |
| FC5-VAL-005 | Enforce outcome ID and execution ID links | partial | Adversarial tests cover links; full matrix incomplete |
| FC5-VAL-006 | Validate outcome hash format and recomputation | partial | Implemented and forged digest tested |
| FC5-VAL-007 | Require observer/context/criterion/rule/rationale to be non-empty strings | partial | Missing criterion tested; wrong-type and remaining fields not individually mapped |
| FC5-VAL-008 | Reject unknown assessment fields | pending | No closed-key validation |
| FC5-VAL-009 | Reject null/array/primitive substitution for assessment fields | pending | Dedicated fixtures not located |
| FC5-VAL-010 | Enforce assessment/status conditional truth table | partial | Round trips exist; all combinations not tested |

## G. Integrity/security, replay, and FC-6

| ID | Acceptance predicate | Initial state | Evidence / gap |
|---|---|---|---|
| FC5-SEC-001 | Explain that unkeyed hashes provide consistency, not origin authenticity | partial | Wording exists in one UI path; contract/UI consistency incomplete |
| FC5-SEC-002 | Regression test prevents claims of authentication based on SHA-256 alone | pending | Dedicated assertion not located |
| FC5-REPLAY-001 | Import replays independently and matches exported result for valid package | verified | Current tested round-trip fixture and clean-source CI |
| FC5-REPLAY-002 | Replay mismatch is rejected | partial | Implementation path exists; exact tampered-result fixture mapping incomplete |
| FC5-REPLAY-003 | Legacy/optional semantic identity compatibility behaves as documented | partial | Compatibility code exists; version matrix incomplete |
| FC6-CI-001 | All required workflows pass on the exact candidate commit | verified for a90b69a6 only | Runs 38749236634, 38749235581, 38749236114, 38749235856, 38749236050; rerun after any code/test change |
| FC6-CLEAN-001 | Clean-source archive replay passes on exact candidate commit | verified for a90b69a6 only | Included in run 38749236634; rerun after any code/test change |
| FC6-ART-001 | Inspect final exported package artifacts against contract | partial | Need artifact list and per-artifact evidence |
| FC6-SCOPE-001 | CI/evidence explicitly avoid claiming scientific validity from synthetic tests | partial | Governance states boundary; final evidence bundle mapping needed |
| FC6-MAIN-001 | Confirm main unchanged and PR #67 remains draft | pending fresh check | Must capture current PR/base/head evidence before closure |

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


## GT-04 grouped candidate update — CI pending

The development candidate now implements the closed 12-key outcome and 11-key assessment schemas, required-key checks, finite `source_kind` enum, non-empty outcome metadata and assessment ID checks. The browser test adds five grouped adversarial variants with package digest recomputed: unknown outcome key, invalid source kind, empty outcome unit, unknown assessment key, and empty assessment ID.

Related predicates: FC5-OUT-002/004/005/007/008 and FC5-VAL-002/004/008/009. Their status remains **pending** until the required five workflows pass on the exact candidate SHA and diagnostic assertions are confirmed. Existing cross-link and NOT_ASSESSED checks remain in place.


### GT-04 candidate CI diagnostic

The first grouped candidate commit `2ceca81321c00dce3c142e679f388c4d535918e3` passed four of five workflows; browser/cross-runtime failed in the pre-existing BLOCKED-trace outcome test because its adversarial outcome fixture omitted newly required outcome fields. The importer rejected it as incomplete before evaluating the expected COMPLETED-trace constraint. The fixture is being corrected to be schema-complete so the test isolates the intended predicate. No acceptance predicate is considered verified by this failed batch.


### GT-04 candidate CI diagnostic — assertion wording

On `6aab8a91eaf9c9296fa13b510c06a3361f492c42`, four of five workflows passed. The browser/cross-runtime workflow rejected the incomplete assessment as expected but the legacy test regex only recognized `valoración está incompleta`; the validator now emits `value_assessment está incompleta`. The test assertion is broadened to accept either label while preserving the required rejection. No acceptance predicate is considered verified by this failed batch.


### GT-04 evidence and next grouped risk

The five required workflows passed on exact commit `6f426724e48426b5a525764f592222a13b0a5886` (runs: `38792359668`, `38792359755`, `38792359714`, `38792359847`, `38792360053`). Browser/cross-runtime includes successful clean-source replay. Engineering gate only; no scientific-validity claim.

Next pending grouped adversarial cases: outcome null/array substitutions, assessment array substitution, invalid assessment status when the assessment object is present, and `value_assessment_status=ASSESSED` when no assessment object exists. The tests require targeted rejection diagnostics and recompute the outer package digest. GT-04 remains open.


### GT-04 iteration 2 evidence and pending field/status adversaries

Five required workflows passed on exact candidate commit `85141c0b7648fc07b25b55001aa81ca6b50a46d9`: browser/cross-runtime `38793015720`, synthetic engine `38793016043`, governance consistency `38793015627`, browser benchmark `38793015667`, and engine benchmark `38793015731`.

Next grouped fixtures target non-string outcome value, non-string provenance, non-string assessment criterion, empty assessment rationale, and unsupported status `PENDING` when no assessment object is present. Predicates: FC5-OUT-005, FC5-VAL-007, FC5-PKG-012 and FC5-PKG-011. Status remains pending until the next exact-head five-workflow gate passes.


### GT-04 iteration 3 — pending schema/field adversaries

Previous exact-head gate: all five workflows passed on `363557b0fc3f6e5fd8b5ecccf32cc86d731c4e00` (runs `38793710973`, `38793710676`, `38793710906`, `38793710696`, `38793710689`).

Pending grouped adversaries: wrong `outcome_schema`, blank `outcome_id`, wrong `assessment_schema`, numeric `observer`, and blank `valuation_rule`. Target predicates FC5-OUT-001/003 and FC5-VAL-001/007; require diagnostic-specific rejection and the five-workflow exact-head gate before updating predicate status.


### GT-04 iteration 4 — linked evidence-chain adversaries

The five-workflow exact-head gate passed on `d3593138cfcfeb087417ab2f117b751b68eaa42e`: browser/cross-runtime `38794551912`, synthetic engine `38794551709`, governance consistency `38794551639`, browser benchmark `38794551678`, engine benchmark `38794551659`. Clean-source replay passed in the browser/cross-runtime job.

Pending grouped adversaries break one link at a time across the chain: outcome execution ID, trace digest format, model ID, scenario ID, assessment outcome ID, assessment execution ID, and assessment's outcome digest (valid SHA-256 shape but wrong value). Outer package digest is recomputed. Require intended diagnostic plus all five workflows on one exact commit before claiming these predicates verified.


### GT-04 iteration 5 — lifecycle stage/artifact coherence

Previous exact-head five-workflow gate passed on `4f4a45f532e08c0f3ff13480ba61bec77552e822` (runs `38795223557`, `38795223565`, `38795223544`, `38795223577`, `38795223833`).

Newly identified invariant: package v2 stage must match the highest artifact present: ASSESSMENT if a value assessment exists, else OUTCOME if an outcome exists, else EXECUTION if a concrete trace exists, else EXPLORATION. The validator and four diagnostic-specific adversarial cases now cover stage/artifact mismatch. Await exact-head five-workflow CI before considering this invariant verified; GT-04 remains open.


### GT-04 iteration 5 — evidence recorded

Exact-head five-workflow gate passed on `144c1d1332405c54b7b74e3ecd8afa29808cc6d0`: `38795907330`, `38795907082`, `38795906835`, `38795906832`, `38795906803`; all concluded success.

### GT-05 iteration 1 — assessed round-trip determinism pending

Added a grouped end-to-end assertion that imports the same fully assessed artifact twice and checks explicit `ASSESSMENT` stage, outcome-digest linkage, matching independent replay, and stable replay assessment. Status remains pending until the exact-head five-workflow gate passes.


### GT-05 iteration 1 — diagnostic correction

Initial candidate `01497f122dbd9facc9980fd95e2a8c1b8eabdffd`: 4/5 workflows passed; browser/cross-runtime `38796877033` failed because the test assumed an undeclared `outcome_record.outcome_sha256` property. Replaced that invalid expectation with an independent recomputation of the canonical SHA-256 for the exact outcome object and comparison against `value_assessment.outcome_sha256`. This is a test correction only; acceptance remains pending until all five workflows pass on one exact commit.


### GT-05 iteration 1 — corrected exact-head evidence

The corrected test candidate `fa15baeef941e9db679a9eca25b97a0ec4a94b5e` passed all five workflows on the exact same commit: browser/cross-runtime `38813194707`, synthetic engine `38813194676`, governance consistency `38813194713`, browser benchmark `38813194700`, engine benchmark `38813194665`. The digest assertion independently recomputes the canonical hash of `outcome_record` and compares it with `value_assessment.outcome_sha256`. The same assessed artifact is imported/replayed twice and the replay assessment is stable. This verifies this grouped engineering scenario only; it does not close GT-04 or establish scientific validity.

### Next action — acceptance inventory reconciliation before more tests

Per the finite schema inventory governance rule, do not add further adversarial cases until the numbered acceptance register is reconciled against the actual implementation, fixtures, and CI evidence. Expand remaining `GROUP` rows, reconcile top-level optional-field types, package digest negatives, conditional package-stage/status truth table, nested input/result predicates, and FC-6 artifact inspection predicates. Keep states `verified`, `partial`, and `pending` evidence-based; no blanket upgrade from the five-workflow aggregate.


## Reconciliation iteration 1 — expand delta, package integrity, and existing GT-04 evidence

This is a denominator/traceability update only. It does not change application code and does not promote any status without mapped evidence. The current test file is `prototypes/collective_toy/web/ui_contract_test.cjs`; the GT-04 grouped adversarial helper recomputes `package_sha256` after each mutation, so those cases isolate inner predicates rather than package-integrity failures.

### Package envelope gaps

| ID | Atomic acceptance predicate | State | Evidence / next action |
|---|---|---|---|
| FC5-PKG-005 | Reject absent `package_sha256` | pending | No dedicated fixture/call mapped in current UI contract test |
| FC5-PKG-006 | Reject malformed `package_sha256` shape | pending | No dedicated fixture/call mapped |
| FC5-PKG-007 | Reject a well-formed but incorrect `package_sha256` | partial | Validator recomputes digest; add explicit tampered-digest fixture without recomputing it |
| FC5-PKG-008 | Reject non-object `concrete_execution_trace` | pending | No dedicated top-level type substitution mapped |
| FC5-PKG-009 | Reject non-object `outcome_record` | partial | GT-04 calls `gt04-outcome-array-substitution.json` and `gt04-outcome-null-substitution.json` (test lines 705–706); confirm exact-head run before upgrading |
| FC5-PKG-010 | Reject non-object `value_assessment` | partial | GT-04 calls `gt04-assessment-array-substitution.json` (line 707); null/primitive substitutions remain unmapped |
| FC5-PKG-011 | Enforce all legal/illegal assessment-object and status combinations | partial | Positive assessed and NOT_ASSESSED replay; negative calls at lines 708–709 and 714; full truth table remains pending |
| FC5-PKG-012 | Reject unsupported `value_assessment_status` values | partial | `gt04-invalid-assessment-status.json` and `gt04-unknown-status-without-assessment.json` (lines 708, 714); confirm exact diagnostic/run evidence |

### Delta-reach predicates — explicit denominator

The finite schema inventory enumerates eleven emitted fields and twelve validation predicates. None of the predicates below is marked verified solely because engine output exists or replay compares valid generated packages.

| ID | Atomic acceptance predicate | State | Evidence / gap |
|---|---|---|---|
| FC5-DELTA-001 | Exactly one delta entry for each declared non-baseline scenario | pending | Dedicated missing/extra-entry fixtures not mapped |
| FC5-DELTA-002 | Reject unknown keys in a delta object | pending | Inventory reports no importer closed-key block; requires implementation review before test addition |
| FC5-DELTA-003 | Require lowercase 64-hex baseline/intervention source hashes | pending | Malformed-hash fixtures not mapped |
| FC5-DELTA-004 | Recompute each source hash from the correct canonical source projection and domain tag | partial | Engine computes hashes; importer tamper evidence not mapped |
| FC5-DELTA-005 | Require state/transition delta fields to be arrays of declared IDs | pending | Wrong-type and unknown-ID fixtures not mapped |
| FC5-DELTA-006 | Require added/removed trajectory deltas to be ordered valid paths | pending | Malformed path fixtures not mapped |
| FC5-DELTA-007 | Require all three truncation fields to be booleans | pending | Wrong-type fixtures not mapped |
| FC5-DELTA-008 | Require aggregate `truncated` to equal baseline OR intervention truncation | pending | Inconsistent-boolean fixture not mapped |
| FC5-DELTA-009 | Require delta arrays to equal corresponding baseline-comparison fields | partial | Replay equality gives indirect coverage only; direct tampering fixture not mapped |
| FC5-DELTA-010 | Forbid a baseline scenario's own delta entry | pending | Dedicated fixture not mapped |
| FC5-DELTA-011 | Require one delta entry per intervention and no duplicate/missing scenario | pending | Dedicated fixtures not mapped |
| FC5-DELTA-012 | Reject delta entry without a matching baseline comparison | pending | Dedicated fixture not mapped |

### GT-04 evidence map (current test source, not a substitute for CI)

The current browser contract test contains 32 calls to `rejectGt04Mutation`. Explicit cases include outcome/assessment type and field adversaries (lines 701–719), cross-links and digest checks (720–726), and package-stage/artifact mismatches (727–730). The corrected GT-05 replay test passed the five-workflow exact-head gate on `fa15baeef941e9db679a9eca25b97a0ec4a94b5e` (runs `38813194707`, `38813194676`, `38813194713`, `38813194700`, `38813194665`). That run predates this documentation-only commit and does not verify any later code changes.

### FC-6 closure evidence remains pending

| ID | Atomic acceptance predicate | State | Required evidence |
|---|---|---|---|
| FC6-ART-001 | Enumerate the exact exported artifacts and inspect each against its contract | partial | Attach artifact names, canonical hashes, and inspection outcome |
| FC6-SCOPE-001 | Evidence bundle explicitly limits CI conclusions to engineering/reproducibility, not scientific validity | partial | Map exact governance text and final bundle artifact |
| FC6-MAIN-001 | Verify `main` remains unchanged and PR #67 remains draft | pending fresh check | Capture branch SHA and PR base/head/draft state at closure |

### Reconciliation decision

The acceptance denominator is still **not finalized**: input, result, scenario and comparison nested predicates need the same atomic expansion and exact implementation/test mapping. The next work item remains documentation/schema reconciliation, beginning with verifying whether `delta_reach` has any import-time field-level validation. If it does not, record that as a contract gap and propose the smallest grouped implementation candidate on this development branch; do not silently treat replay as complete substitute validation. No scientific execution is authorized.


## Reconciliation correction — delta_reach implementation was present

A direct read of the current branch's importer (`prototypes/collective_toy/web/index.html`, lines 270–291) corrects the earlier inventory statement that no field-level `delta_reach` validation block existed. The importer validates the exact intervention key set, closed 11-field schema, lowercase SHA-256 shape, recomputed baseline/intervention source hashes, state/transition IDs, ordered paths, boolean truncation flags, semantic correspondence to `comparisons_to_baseline`, and truncation consistency. The correct gap is missing dedicated negative fixtures for several individual predicates, not missing implementation wholesale.

Existing directly mapped adversarial tests in `web/ui_contract_test.cjs`: unknown delta field (lines 1195–1214), forged delta semantics (1216–1234), and forged baseline source digest (1240–1258). Their enclosing result/package hashes are recomputed to reach the intended validation branch. These establish focused evidence for those predicates only. Pending direct fixtures include malformed source-hash shape, forged intervention-source digest, wrong-type/unknown-ID arrays, malformed trajectory paths, wrong-type/inconsistent truncation flags, and missing/extra intervention keys. Keep those predicates pending until exact-head browser test evidence is linked.

The previous note saying “current importer ... does not include a dedicated closed-key/field-by-field validation block” is superseded by this correction. No application code changed in this reconciliation iteration.


### FC5-DELTA-003/004 — intervention-source digest adversarial fixtures added

Added two focused browser contract cases after the baseline-source digest case: (a) malformed `intervention_source_sha256` must trigger the digest-format diagnostic; (b) a syntactically valid but forged 64-hex intervention-source digest must trigger the source-correspondence diagnostic. Both fixtures recompute the enclosing result and package digests so the intended nested predicate is reached. Status remains pending exact-head CI evidence.


### FC5-DELTA-007/008 — truncation consistency fixtures added

Added three browser adversarial cases: (1) `baseline_truncated` is the string `"false"` and must fail the boolean predicate; (2) aggregate `truncated=true` conflicts with both scenario flags remaining false; (3) `intervention_truncated=true` conflicts with the intervention scenario's actual `truncated=false`. Each fixture recomputes the enclosing result and package digests and asserts the specific importer diagnostic. State remains pending exact-head five-workflow CI evidence.


### FC5-DELTA-005/006 — state/transition delta list predicates

The previous truncation iteration passed all five required workflows on exact commit `f4cc56a5db01f52cd9f9a54223e07e24cd9b4591`: browser/cross-runtime `38815534166`, synthetic engine `38815534390`, governance consistency `38815534200`, browser benchmark `38815534257`, and engine benchmark `38815534173`. Both browser execution and clean-source replay passed.

Added four focused negative fixtures for the next grouped risk: a non-array `reachable_states_added`, an unknown state ID in `reachable_states_removed`, a non-array `enabled_at_initial_added`, and an unknown transition ID in `enabled_at_initial_removed`. Each mutation recomputes the enclosing result and package hashes and asserts the field-specific rejection. These new predicates remain pending until the exact-head five-workflow gate passes.


### FC5-DELTA-009/010 — trajectory path validation fixtures

The state/transition delta-list candidate `044527b23cc61f9781c740b6033b944fee6c1253` passed all five workflows on the same exact commit: browser/cross-runtime `38816440366`, synthetic engine `38816440406`, governance consistency `38816440385`, browser benchmark `38816440371`, and engine benchmark `38816440375`. Browser execution and clean-source replay passed.

Added three focused browser adversaries for the next grouped risk: `trajectories_added` as a non-list; a removed trajectory containing an undeclared state; and a removed trajectory whose transition edge does not connect the preceding and next states. Each case recomputes enclosing result/package digests and asserts the targeted validator diagnostic. New predicates remain pending exact-head CI.


### FC5-DELTA-011/012 — semantic correspondence to baseline comparison

The ordered-trajectory candidate `ca6ee8c48f41acd9dce4c2ff872fc6a9006c698d` passed all five exact-head workflows: browser/cross-runtime `38816955178`, synthetic engine `38816954767`, governance consistency `38816954811`, engine benchmark `38816954808`, and browser benchmark `38816954841`. Browser execution and clean-source replay passed.

Added three adversarial fixtures where the delta value is structurally valid and uses declared IDs but disagrees with `comparisons_to_baseline`: a valid state ID in `reachable_states_added`, a valid transition ID in `enabled_at_initial_added`, and a valid ordered path in `trajectories_added`. Each fixture recomputes enclosing result/package hashes and expects the semantic cross-check diagnostic. Pending exact-head CI.


## Canonical delta-reach acceptance table — current register

This is the **only active acceptance table** for delta-reach. All `FC5-DELTA-001` through `FC5-DELTA-012` rows in preceding iteration notes are historical snapshots, not additional active predicates. Their IDs are retained in history for auditability; they must not be counted in the current denominator or used to override this table. The canonical IDs below are deliberately namespaced `FC5-DELTA-C01`…`FC5-DELTA-C12` to avoid collisions with historical numbering.

Implementation baseline: `web/index.html` lines 270–290 at candidate `a7813bc221f38e023936ba6c4883b877d92729b7`. The current branch has subsequent key-set adversaries and documentation changes; statuses must be advanced only when the exact current HEAD has passing relevant CI and the fixture is mapped directly.

| Canonical ID | Acceptance predicate | State | Evidence / remaining gap |
|---|---|---|---|
| FC5-DELTA-C01 | `delta_reach` keys equal exactly the non-baseline input scenario IDs | partial | Validator `index.html:274–275`; missing-intervention and illegal-baseline-entry adversaries recompute result/package hashes and assert the scenario-key-set diagnostic. Confirm exact fixture mapping and exact-HEAD CI before marking verified. |
| FC5-DELTA-C02 | Each delta object has exactly the 11 declared fields | partial | Validator `index.html:273,278`; unknown-key adversary exists in earlier suite. Pin the exact fixture and diagnostic to current CI evidence. |
| FC5-DELTA-C03 | Both source-hash fields have lowercase 64-hex SHA-256 syntax | pending | Validator `index.html:279`; malformed-format fixture mapping not confirmed. |
| FC5-DELTA-C04 | Both source hashes are recomputed from their correct canonical source projections and domain tags | partial | Validator `index.html:280–284`; baseline forged-hash fixture mapped; intervention-specific forged-hash fixture was added in later iteration, but current exact-head evidence mapping is still required. |
| FC5-DELTA-C05 | Added/removed reachable-state deltas are lists of declared state IDs | verified | Validator `index.html:285`; direct negative fixtures `ui_contract_test.cjs:1368–1369`; verify current exact-head CI before release. |
| FC5-DELTA-C06 | Added/removed initially enabled-transition deltas are lists of declared transition IDs | verified | Validator `index.html:286`; direct negative fixtures `ui_contract_test.cjs:1370–1371`; verify current exact-head CI before release. |
| FC5-DELTA-C07 | Added/removed trajectory deltas are nonempty, ordered valid paths | verified | Validator `index.html:287`; direct negative fixtures `ui_contract_test.cjs:1395–1397`; verify current exact-head CI before release. |
| FC5-DELTA-C08 | All three truncation fields are booleans | verified on exact test HEAD `d0a496eb162c4e2bbc161991311439af69909a2c`; revalidation required after this documentation commit | Validator `index.html:288`; wrong-type adversaries for `baseline_truncated`, `truncated`, and `intervention_truncated` recompute result/package digests and assert field-specific diagnostics. Browser/cross-runtime CI passed on exact test HEAD: run [38822992426](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38822992426). This evidence verifies the test HEAD, not a later changed HEAD. |
| FC5-DELTA-C09 | Aggregate truncation equals baseline OR intervention truncation, and each scenario flag equals its own scenario result | verified on exact test HEAD `d0a496eb162c4e2bbc161991311439af69909a2c`; revalidation required after this documentation commit | Validator `index.html:290`; baseline/intervention-specific mismatch cases and all eight claimed boolean triples are exercised with result/package hashes recomputed. The one tuple matching both scenario flags and their OR aggregate must reach `replay-verified`; the seven inconsistent tuples must be rejected with the targeted diagnostic. Browser/cross-runtime CI passed on exact test HEAD: run [38822992426](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38822992426). This evidence verifies the test HEAD, not a later changed HEAD. |
| FC5-DELTA-C10 | State, transition, and trajectory deltas equal corresponding exported baseline-comparison fields | verified on exact test HEAD `b123ff1174d91c5c9de989758e80c3b157b535d9` | Validator `index.html:289`; valid-but-inconsistent semantic adversaries cover all six fields: `reachable_states_added/removed`, `enabled_at_initial_added/removed`, and `trajectories_added/removed`. Each mutation recomputes result/package hashes and requires the targeted baseline-comparison mismatch diagnostic. All five workflows passed on this exact HEAD: browser/cross-runtime `38824283979`, browser benchmark `38824284051`, synthetic engine `38824283983`, engine benchmark `38824283953`, governance `38824284028`. Engineering contract coverage only; C12 remains partial. |
| FC5-DELTA-C11 | Baseline has no `delta_reach` entry | partial | Implied by exact-key-set validator and directly exercised by illegal-baseline-entry adversary; verify current exact-head fixture/CI mapping. |
| FC5-DELTA-C12 | Every non-baseline scenario has exactly one delta entry and a matching baseline comparison; no missing, extra, or duplicate scenario correspondence | verified | All five workflows passed on exact HEAD `b9066e5358627d616b3cd2acb8f111f3059434ea`: governance `38886446155`, synthetic engine `38886446220`, engine benchmark `38886446408`, browser benchmark `38886446330`, browser/cross-runtime `38886446084`. Validator inventory and adversarial evidence cover exact scenario/key correspondence for `scenario_results`, `comparisons_to_baseline`, and `delta_reach`; internal `scenario_id`; fixed allowed payload fields; both source commitments across intervention IDs; semantic delta/comparison consistency; and truncation type/coherence. Engineering-contract acceptance only; no scientific claim or GT-03 closure. |

**Counting rule:** denominator = these 12 canonical predicates only. A predicate can be covered by a grouped test; test count and predicate count are distinct. Historical numbered tables are retained as provenance but are not active rows. This is engineering contract coverage only; it does not establish scientific validity or close GT-03.

### FC5-DELTA-001/011 — exact intervention-key set adversaries

The atomic-register reconciliation candidate `159a736b93fcdfa48f10f27434b61a0e0297a946` passed all five workflows on the exact head: browser/cross-runtime `38818148318`, synthetic engine `38818148346`, browser benchmark `38818148294`, engine benchmark `38818148369`, and governance consistency `38818148292`.

Added two negative fixtures: remove the only intervention delta entry, and add an illegal `baseline` delta entry. Both recompute result/package hashes and require the exact scenario-key-set diagnostic. The fixtures are pending exact-head CI; this covers only missing/extra entry shape and does not by itself establish comparison semantics.


### GT-01 package digest adversaries — candidate added, exact-HEAD CI pending

Commit `b3b8cb38e06693fa2213879853993c558795ead9` adds three browser-import adversaries in `prototypes/collective_toy/web/ui_contract_test.cjs`:

- `FC5-PKG-005`: remove `package_sha256`; expect the specific absent/malformed digest diagnostic.
- `FC5-PKG-006`: set `package_sha256` to a non-SHA-256 string; expect the same schema diagnostic.
- `FC5-PKG-007`: replace the digest with a different well-formed 64-character lowercase hex value and deliberately do not recompute it; expect the package-integrity mismatch diagnostic.

These cases distinguish digest presence/format from digest integrity. They are implemented but remain **pending** until the browser test and the full five-workflow suite pass on one exact HEAD. No scientific execution or GT-03 closure.


### FC5-PKG-008 — execution-trace type substitution adversaries (candidate; CI pending)

Commit `4c54aaef2a373c49b32b1ffffa936fe692c78cc4` adds browser-import cases replacing `concrete_execution_trace` with `null`, an array, a string, a number, and a boolean. Each case recomputes `package_sha256` so the validator must reject the trace type specifically, not merely detect package digest mismatch. Expected diagnostic: `concrete_execution_trace debe ser un objeto`. Coverage remains pending until all five controls pass on one exact HEAD.


### FC5-PKG-008 diagnostic-precedence correction — CI pending

The first run on the previous candidate failed on the `null` trace case: the fixture retained an outcome record, so the importer correctly rejected the package earlier with `El resultado no está vinculado a la traza de ejecución exportada o requiere una traza COMPLETED.` This did not exercise the intended trace-type diagnostic. Commit `218b3885f0fe84831b615fb8acef86efb5005c05` adjusts each invalid-trace fixture to exploration stage, removes outcome/value records, sets `value_assessment_status=NOT_ASSESSED`, and recomputes the package digest. This isolates the type predicate. FC5-PKG-008 remains pending until exact-HEAD browser and five-workflow CI pass.
