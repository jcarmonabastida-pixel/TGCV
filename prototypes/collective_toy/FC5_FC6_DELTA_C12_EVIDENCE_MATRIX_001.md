# FC5-DELTA-C12 — predicate/evidence matrix 001

Status: engineering-contract evidence only. C12 remains **partial**. No scientific execution or claim is authorized by this matrix.

## Evidence baseline

- Code/test HEAD for the relevant validator and adversarial cases: `9540b1ac93049d443b6b0db6910229e036a9c3b1`.
- Documentation HEAD whose five workflows passed before this matrix was added: `d4a1a82aea152158fa53a773e681d664176c6cc0`.
- Current validator file: `prototypes/collective_toy/web/index.html`; line numbers below refer to the version read while preparing this matrix.
- Current browser contract tests: `prototypes/collective_toy/web/ui_contract_test.cjs`; line numbers below refer to the version read while preparing this matrix.

## Predicate/evidence matrix

Legend: **I** = implementation-backed guard; **A** = adversarially exercised with a targeted test; **P** = partial evidence; **—** = not established by the current evidence set. A guard existing is not equivalent to an adversarial test for every row/scenario.

| Object / predicate | Exact key set / duplicate raw keys | Scenario identity / key correspondence | Baseline & intervention source commitments | Intervention payload identity | Delta ↔ comparison equivalence |
|---|---|---|---|---|---|
| `scenario_results` | **I** — validator lines 208–214 checks object shape, no unknown scenario keys, and presence of all input scenario IDs. Duplicate raw JSON keys are rejected by the import parser before `JSON.parse`; this is parser-level, not per-map identity evidence. | **I/P** — lines 213–214 check IDs against input and require every input ID. Commit `0536253f3561e7c9250be8cdd7f35077f0bb9bfd` adds a per-key `scenario_id` mismatch adversary for every `scenario_results` entry, recomputing semantic/result/package hashes and asserting the specific identity diagnostic; exact-HEAD CI is pending. | **—** — source commitments are calculated from the baseline and intervention scenario objects; no separate source commitment field exists on each `scenario_results` entry. | **P** — scenario fields are consumed by downstream validation, but this matrix does not yet enumerate every field that must agree with the input scenario and the derived result. | **P** — delta fields are compared with the exported baseline comparison (validator lines 291–292); there is not yet one cross-object adversary matrix that perturbs each `scenario_results` payload and checks all dependent representations. |
| `delta_reach` | **I/A** — validator lines 272–280 requires an object, exact intervention key set, and exact fields per delta entry. Group-6 tests cover missing and extra scenario entries; raw duplicate keys are rejected before parsing. | **I/A/P** — exact keys are compared with non-baseline input scenario IDs at line 277; missing/extra entry adversaries exist. Full one-to-one identity coverage across every scenario is not yet established in a single matrix. | **I/A/P** — lines 281–286 check SHA-256 format and recompute baseline/intervention source hashes from the corresponding source objects. Targeted valid-but-wrong hash adversaries originally covered `block_ac`; commit `050991d8f37f5f4ea6d48caa1da8e0d3d147c289` changes this into a loop over every `delta_reach` intervention ID, independently mutating both `baseline_source_sha256` and `intervention_source_sha256` and requiring the scenario-specific diagnostic. This coverage is pending exact-HEAD CI. | **P** — source hashes bind the scenario source objects, but the evidence set has not yet tested every source-relevant input field and every scenario ID in a table-driven sweep. | **I/A** — line 291 compares reachable-state, initially-enabled-transition, and ordered-trajectory delta fields with the comparison; tests around lines 1680–1700 forge delta fields while recomputing enclosing digests and require the specific mismatch diagnostic. |
| `comparisons_to_baseline` | **I** — validator lines 255–257 rejects incompatible keys and requires a comparison for each non-baseline input scenario. **A** — browser tests `comparison-missing-intervention.json` and `comparison-extra-baseline.json` (test lines 1260–1295) recompute semantic/result/package digests and assert dedicated diagnostics. | **I/P** — key correspondence is checked against input scenario IDs; **A** — targeted missing/extra comparison-key cases are present at test lines 1260–1295. | **—/P** — comparison records do not carry the delta source-commitment fields; their relationship is indirectly checked through scenario and delta validation. | **I/A** — validator line 270 checks `intervention.disabled_transitions` against the matching input scenario. Test `comparison-intervention-source-mismatch.json` around lines 1705–1735 changes this payload, recomputes semantic/result/package hashes, and expects the specific source-scenario mismatch diagnostic. | **I/A** — line 291 compares delta payload fields to the baseline comparison; the targeted forged-delta tests around lines 1680–1700 cover mismatched state/transition/trajectory values. |

## Cross-cutting evidence

- Exact key-set guards: `index.html` lines 213–214 (`scenario_results`), 255–257 (`comparisons_to_baseline`), and 272–280 (`delta_reach`).
- Delta source commitments: `index.html` lines 281–286.
- Comparison intervention payload binding: `index.html` line 270.
- Delta/comparison payload equivalence and truncation coherence: `index.html` lines 291–292.
- Browser adversaries: `ui_contract_test.cjs` around lines 1680–1735 for delta/comparison and comparison intervention identity; around lines 1740–1780 for GT-03 scenario-context adversary and source-hash repair.
- Exact-head CI evidence before adding this matrix: all five workflows passed on documentation HEAD `d4a1a82aea152158fa53a773e681d664176c6cc0`: browser/cross-runtime `38828197960`, governance `38828198005`, synthetic engine `38828198130`, browser benchmark `38828198098`, engine benchmark `38828198233`.

## Remaining gaps / next smallest test batch

1. Comparison missing/extra key adversaries are implemented (`ui_contract_test.cjs` lines 1260–1295); preserve them and verify exact diagnostics in CI.
2. Source-commitment adversaries now iterate over all non-baseline `delta_reach` IDs and test each hash independently; validate on the exact resulting HEAD.
3. Per-scenario `scenario_results[*].scenario_id` identity adversary implemented in commit `0536253f3561e7c9250be8cdd7f35077f0bb9bfd`; it recomputes semantic/result/package hashes and expects the key-specific identity diagnostic. Remaining gap after CI: assess whether intervention payload identity needs any additional field beyond `disabled_transitions` and source commitments.
4. After CI passes, reconcile the register from the exact code/test HEAD and run all five workflows on one exact resulting HEAD before changing C12's acceptance state.

Do not close C12 solely because the five general CI workflows pass. Do not close GT-03 based on this matrix. Do not authorize or perform scientific execution.
