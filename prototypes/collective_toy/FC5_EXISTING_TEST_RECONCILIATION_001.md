# FC-5 existing test-to-predicate reconciliation — 001

- **Status:** static reconciliation of repository source; no tests executed by this operation.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Test source:** `web/ui_contract_test.cjs`
- **Importer source:** `web/index.html`, function `assessImportedBrowserPackage(pkg)`
- **Register:** `FC5_FC6_NUMBERED_ACCEPTANCE_REGISTER_001.md`
- **Scope:** map current named fixtures to individual predicates without changing code or adding fixtures.

## 1. Exact positive/negative fixture mapping visible in current test source

| Fixture / assertion | Candidate predicate ID | What it demonstrates | Limitation |
|---|---|---|---|
| `assessed-fc4-roundtrip.json` | FC5-REPLAY-001; FC5-PKG-011 (positive assessed branch) | A package with trace, outcome and complete assessment is imported and independently replayed | Does not test all conditional combinations |
| `outcome-not-assessed-roundtrip.json` | FC5-PKG-011 (positive NOT_ASSESSED branch) | Outcome without assessment is accepted when status is explicitly NOT_ASSESSED | Does not test wrong status, missing status, or assessment/status conflicts |
| `forged-assessment-outcome-digest.json` | FC5-VAL-006 | Forged outcome digest is rejected even after outer package hash is recomputed | Tests a wrong digest, not every malformed type/format |
| `forged-outcome-trace-link.json` | FC5-OUT-006; FC5-TRACE-019 | Outcome trace digest must match the exported trace | One trace-link predicate only |
| `forged-assessment-outcome-link.json` | FC5-VAL-005 | Assessment outcome reference must point to the exported outcome | Does not cover every execution-link variant |
| `incomplete-contextual-assessment.json` | FC5-VAL-007 | Missing `criterion` causes incomplete assessment rejection | Does not independently prove all five context strings and their types |
| `unknown-package-field.json` | FC5-PKG-001 | Unknown package envelope key is rejected even with recomputed package digest | Does not test nested unknown keys |
| `missing-package-input.json` | FC5-PKG-002 | Missing input is rejected with recomputed package digest | Does not independently test every non-object type |
| `missing-package-result.json` | FC5-PKG-003 | Missing result is rejected with recomputed package digest | Does not independently test every non-object type |
| `missing-package-trace.json` | FC5-TRACE-019 | Outcome cannot refer to a missing exported trace | Tests conditional cross-link, not trace-only package policy |
| `unsupported-package-version.json` | FC5-PKG-004 | Unsupported package version is rejected even with recomputed package digest | Does not test malformed type separately |
| `unknown-result-field.json` | FC5-RES-001 | Unknown result envelope key is rejected after result and package digests are recomputed | Does not test nested scenario/delta fields |
| `forged-outcome-execution-link.json` | FC5-OUT-006 | Outcome execution ID must match trace | One execution-link predicate |
| `forged-assessment-execution-link.json` | FC5-VAL-005 | Assessment execution ID must match outcome/trace | One execution-link predicate |
| `forged-outcome-model-link.json` | FC5-OUT-006 | Outcome model identity must match package input and trace | Recomputes outcome digest to isolate the cross-link check |
| `forged-outcome-scenario-link.json` | FC5-OUT-006 | Outcome scenario ID must match trace | One scenario-link predicate |

The assertions for the above fixtures are located in the FC-5 section of `web/ui_contract_test.cjs` around lines 560–845 on the branch at the time of this reconciliation. Treat the fixture names and assertion messages as the stable mapping keys; re-fetch line numbers from the current branch before using line ranges as closure evidence.

## 2. Existing baseline/intervention delta test

The browser test loads the canonical example, executes baseline/intervention scenarios, and checks:
- a `delta_reach` artifact exists for `block_ac`;
- baseline and intervention source hashes are 64-character hexadecimal strings;
- reachable-state and initially-enabled-transition differences match the hand-checkable expected values;
- all three truncation fields are explicitly false.

This is positive semantic evidence for the tested fixture, but it does **not** establish importer-side validation of arbitrary imported `delta_reach` objects, unknown-field rejection, hash recomputation, cross-link completeness, or malformed nested types. Keep FC5-DELTA predicates partial/pending until evidence targets those exact import predicates.

## 3. Importer behavior verified by source inspection, not by a dedicated fixture

Current importer source visibly performs:
- closed-key checks for package and result envelopes;
- package/result/input hash format and consistency checks;
- input model validation before replay;
- scenario-result and comparison structure/reference checks;
- closed-key checks on nested scenario results, exploration bounds, comparisons and comparison interventions;
- trace schema/status/hash checks when a trace is present;
- outcome/assessment schema and selected identity/hash cross-links;
- deterministic replay comparison, including a legacy result compatibility branch.

Source inspection alone is not a passing acceptance test. These predicates remain `partial` unless an existing named test exercises that exact failure or boundary and the corresponding required CI run passes.

## 4. Confirmed gaps from the source/test comparison

1. Imported `delta_reach` is not validated field-by-field against a closed nested schema before replay; replay comparison may catch some mutations on the supported-engine path, but this is not a substitute for explicit schema checks.
2. Imported execution trace and step objects do not have closed-key validation; the importer checks trace schema/status/digest but does not independently validate every emitted field or ordered step against the input model.
3. Outcome and assessment objects lack closed-key validation. Several emitted field types/constraints and the outcome `source_kind` enum are not fully validated.
4. The trace policy accepts only `COMPLETED`, while the UI can produce `BLOCKED`; contract policy must be decided before adding tests for the intended behavior.
5. A trace-only package (without outcome) and the complete package optional-field truth table are not yet specified/tested.
6. A hash is an unkeyed integrity check, not proof of origin or authenticity; retain that security boundary in user-facing and contract language.

## 5. Counting snapshot (inventory rows, not final atomic denominator)

The numbered register currently has 112 listed rows. Static parsing identifies:
- 6 rows marked `verified`;
- 65 rows marked `partial`;
- 38 rows marked `pending`;
- 3 rows with qualified statuses (the two CI rows marked verified only for commit `a90b69a6`, plus the main/PR state row pending a fresh check).

These figures are a snapshot of the current register formatting, **not a definitive total of all atomic requirements**. Several rows are grouped predicates and section H lists areas still requiring decomposition. No overall completion percentage should be calculated from these counts.

## 6. Next permitted operation

Finish atomization of section H and normalize the three qualified statuses into explicit state + evidence-commit fields. Then re-fetch current source and workflow evidence and reconcile every row. Only after that choose the first uncovered predicate with a settled contract decision, add the smallest targeted adversarial fixture, and run the required CI on the exact candidate commit.
