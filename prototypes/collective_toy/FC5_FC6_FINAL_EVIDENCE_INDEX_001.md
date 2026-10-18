# FC5/FC6 Final Evidence Index — 001

Date: 2026-10-18  
Candidate branch: `prototype/tgcv-full-chain-001-20261014-scenario-context-recovery`  
Evidence-register HEAD reviewed: `72c061e76841e59549c9cc461edff5676c4b77f1`  
Status: reconciliation index; not a promotion or scientific-validation decision.

## 1. Exact-HEAD CI gate for reviewed register

All five required workflows completed successfully on exact HEAD `72c061e76841e59549c9cc461edff5676c4b77f1`:

| Workflow | Result |
|---|---|
| Governance current-state consistency | [PASS — run 39124797353](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39124797353) |
| Synthetic engine tests | [PASS — run 39124797458](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39124797458) |
| Engine performance benchmark | [PASS — run 39124797366](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39124797366) |
| Browser performance benchmark | [PASS — run 39124797393](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39124797393) |
| Browser and cross-runtime tests | [PASS — run 39124797325](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39124797325) |

This gate verifies CI for that exact source revision. Any later commit needs a fresh exact-HEAD gate.

## 2. Evidence groups and current gaps

Use `FC5_FC6_NUMBERED_ACCEPTANCE_REGISTER_001.md` as the detailed requirement-level inventory. The following is a navigation and decision index, not a replacement for that register.

| Group | Existing evidence located | Material gap still open |
|---|---|---|
| Semantic identity and input/result hashes (RES-008/009/010) | Grouped negative adversaries for missing/inconsistent identity fields, unsupported version, malformed and mismatched input/result digests; replay-integrity adversaries | Complete positive/negative conditional matrix and supported-pairing controls not mapped end-to-end |
| Scenario paths and bounds (SCEN-003/004/006) | Undeclared reachable state, disconnected trajectory, closed exploration keys, integer types and explicit bounds | Complete grouped matrix for all array/reference classes, path ordering, unknown keys, types and lower/upper boundaries |
| Relation/temporal profiles (SCEN-007/008) | Profile-specific execution paths, prerequisite ordering, satisfied path and blocked unsatisfied prerequisite | Invalid field/profile combinations and complete blocked-step import/schema/reference matrix |
| Comparisons (CMP-002/006) | Exact expected comparison-key set validation; grouped schema adversaries | Explicit missing/extra comparison fixtures and wrong-type `truncated` fixture not located |
| Delta arrays (DELTA-005) | Rejection of undeclared state and transition IDs in reviewed added/removed fields | Map all remaining added/removed transition arrays against declared IDs |
| Trace schema and references (TRACE-001/003/007/008/009) | Unknown trace key, unknown transition ID, wrong-type transition array, unknown final state, wrong-type steps array, and other grouped trace adversaries | Complete required-ID empty/type cases; non-string transition-array members; unknown initial state; positive and edge controls |
| Outcome and valuation (OUT-003/005/008; VAL-007/009) | Record substitution adversaries; blank-field adversaries; package digests refreshed where needed | Complete per-field type/domain matrix, including value, uncertainty status, valuation rule and rationale; record-level substitutions do not prove every field-level case |
| Replay compatibility (REPLAY-003) | Fail-closed diagnostic for an incomplete legacy-shaped package | Successful legacy/historical compatibility matrix not established |
| Export artifacts and scientific-claim boundary (FC6-ART-001, FC6-SCOPE-001) | GT-04 stage/artifact presence-dependency matrix; GT-05 full-chain assessment export, outcome link and deterministic clean-import replay; explicit repository non-claims | Consolidated per-stage artifact/field/link inventory and mapping from each workflow/artifact to permitted claims and non-claims |

## 3. Claim boundary

The five-workflow PASS is evidence of software and contract conformance for the tested candidate revision. It does **not** establish:
- empirical validity of TGCV;
- causal effects or generalization beyond tested conditions;
- proof of the canonical TGCV core or of any scientific hypothesis;
- validation of value claims merely because a synthetic assessment was exported.

Synthetic tests are software evidence, not empirical findings. The Rust historical dataset remains parked and is not part of this gate.

## 4. Operating decision

- Keep every item marked `partial` or `pending` in the numbered register at that status until the exact evidence is mapped and verified.
- Prefer one grouped contract-coverage test for a material gap, with adversarial cases grouped where they exercise distinct failure modes; do not create atom-by-atom tests without a demonstrated need.
- Before adding tests, inspect the current validator and existing test fixtures at the same candidate SHA, then document the uncovered branch and why existing tests do not cover it.
- After any code or evidence-register change, run the required five workflows on the new exact HEAD.
- PR #70 remains open and draft. Do not merge. Keep `main` unchanged.
- `scientific_execution_authorized=false`; this index does not authorize scientific execution.

## 5. Next action

Use this index with the numbered acceptance register to choose the smallest grouped test set that closes the highest-impact remaining contract gaps. First candidates are comparison cardinality/type cases, missing-initial-state and transition-array element validation, and the remaining per-field outcome/valuation constraints. Confirm whether existing fixtures already cover each before writing anything.
