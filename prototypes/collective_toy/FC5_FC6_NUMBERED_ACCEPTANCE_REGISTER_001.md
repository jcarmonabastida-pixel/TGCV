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
