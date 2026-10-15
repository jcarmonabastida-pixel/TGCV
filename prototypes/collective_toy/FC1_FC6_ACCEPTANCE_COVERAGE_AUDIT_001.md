# FC-1 to FC-6 acceptance coverage audit 001

- **Status:** Evidence-based development audit; not scientific validation.
- **Audited source commit:** `6ea6b9d0e434624c27333028ae1c730521bd061e`.
- **PR:** #67, open draft; base `9eea51286203a28fa085631bc42ea440cd37cf4f`.
- **CI evidence:** cross-runtime run [38725294922](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38725294922); synthetic engine run [38725294916](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38725294916); governance run [38725295018](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38725295018).
- **Scope boundary:** `main` unchanged. No scientific execution or empirical validation. OCR/detector are out of scope.

## Acceptance matrix

| Contract stage | Acceptance requirement | Implementation located | Test/evidence | Status |
|---|---|---|---|---|
| FC-1 — engine/browser semantic alignment | Versioned temporal profile in browser, semantically aligned with Python; preserve profile 1/2 | `prototypes/collective_toy/web/index.html`; `prototypes/collective_toy/collective_toy_engine_001.py` | Run 38725294922: 116 valid cross-runtime fixtures matched; 102 invalid fixtures rejected in both runtimes; `temporal-prerequisite-sequentiality: PASS`; clean-source archive replay passed. Run 38725294916: 96 historical engine tests and 18 temporal contract tests passed, including profile-1 inert metadata and profile-2 guard semantics. | **verified** (synthetic contract only) |
| FC-2 — accessible-transformation and intervention panel | Show accessible transformation set with rule trace; baseline/intervention delta with source hashes and truncation status | `prototypes/collective_toy/web/index.html`; `web/ui_contract_test.cjs`; scenario/delta result schema | UI CI checks explicit `delta_reach`, source SHA-256 values, added/removed reachable states and enabled transitions, and truncation flags. Evidence does not yet establish a complete per-transformation rule trace/reason for each accessible or blocked transition. | **partial** |
| FC-3 — sequence execution panel | Exact ordered sequence; validate each step; expose blocked step/reason; immutable, auditable trace | `web/index.html` sequence selector/action and `#sequence-trace`; Python `execute_sequence` | UI test verifies concrete sequence action, starting state, ordered step 1, exported trace, trace SHA-256 and COMPLETED status. The current browser acceptance evidence does not yet demonstrate a manually submitted sequence blocked at the exact temporal step with the missing prerequisite shown, nor an immutable attempted-blocked trace. | **partial** |
| FC-4 — outcome and observer-context value assessment | Explicit outcome entry/provenance linked to execution; separate observer/context/criterion assessment; absent valuation is NOT_ASSESSED | No complete implementation established by the audited evidence | Current UI test evidence covers execution, delta and replay; it does not establish outcome/value entry, linkage, provenance, or NOT_ASSESSED behavior. | **pending** |
| FC-5 — run package and replay | Versioned self-contained package, canonical hashes, integrity verification and deterministic replay of stage artifacts | `web/index.html` export/import and package assessor; Python package/replay engine | Browser CI verifies fresh export/import, independent replay, matching recomputed result, tamper/divergence rejection, schema/version/hash rejection, malformed/oversized import handling, and stale-state clearing. Full package coverage for FC-4 outcome/value artifacts remains unverified. | **partial** |
| FC-6 — end-to-end CI | Browser/engine contract tests, historical compatibility, adversarial fixtures, clean-source replay, artifact inspection | `.github/workflows/collective-toy-engine-tests.yml` and associated tests | Runs 38725294922, 38725294916 and 38725295018 all succeeded. Evidence covers 116 valid/102 invalid cross-runtime fixtures, temporal fixture, historical Python suite, browser UI/import/replay/tamper tests, clean-source archive replay, and governance consistency. Full acceptance remains incomplete because FC-2–FC-5 have partial/pending criteria. | **partial** |

## First demonstrated gap and next operation

FC-1 is now verified within the stated synthetic contract boundary. The first unresolved requirement in the contract order is **FC-2's per-transformation accessibility rule trace**. Before modifying code, inspect the current result artifacts and UI to determine exactly which transitions expose a reason and which do not. Then add the narrowest failing acceptance assertion and implement only that missing evidence path. Do not alter the structural detector or OCR quality work.

FC-3's blocked-sequence trace and FC-4 outcome/value layers remain separate later gaps; do not fold them into the FC-2 correction.

## Non-claims

- This matrix records software-contract and CI evidence only.
- A green CI does not establish scientific validity of TGCV, causal claims, empirical generalization, or the canonical scientific definition of (T_{acc}).
- Synthetic outcomes must not be described as empirical findings.
- No promotion to `main` is implied; PR #67 remains a draft until a separate explicit review/promotion decision.
