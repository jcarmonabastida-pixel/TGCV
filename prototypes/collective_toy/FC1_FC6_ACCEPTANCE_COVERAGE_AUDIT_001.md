# FC-1 to FC-6 acceptance coverage audit 001

- **Status:** Evidence-based development audit; not scientific validation.
- **Audited source commit:** `4ab2412ed6cc75e65621a85a05353068d48dae0e` (FC-2 per-transition accessibility assertions).
- **PR:** #67, open draft; base `9eea51286203a28fa085631bc42ea440cd37cf4f`.
- **Latest CI evidence:** cross-runtime/browser run [38728521793](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38728521793) **success**, synthetic engine run [38728521401](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38728521401) **success**, governance run [38728521740](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38728521740) **success**, Python benchmark [38728521646](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38728521646) **success**, browser benchmark [38728521663](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38728521663) **success**. Browser job includes clean-source archive replay.
- **Scope boundary:** `main` unchanged. No scientific execution or empirical validation. OCR/detector are out of scope.

## Acceptance matrix

| Contract stage | Acceptance requirement | Implementation located | Test/evidence | Status |
|---|---|---|---|---|
| FC-1 — engine/browser semantic alignment | Versioned temporal profile in browser, semantically aligned with Python; preserve profile 1/2 | `prototypes/collective_toy/web/index.html`; `prototypes/collective_toy/collective_toy_engine_001.py` | Run 38725294922: 116 valid cross-runtime fixtures matched; 102 invalid fixtures rejected in both runtimes; `temporal-prerequisite-sequentiality: PASS`; clean-source archive replay passed. Run 38725294916: 96 historical engine tests and 18 temporal contract tests passed, including profile-1 inert metadata and profile-2 guard semantics. | **verified** (synthetic contract only) |
| FC-2 — accessible-transformation and intervention panel | Show accessible transformation set with rule trace; baseline/intervention delta with source hashes and truncation status | `prototypes/collective_toy/web/index.html`; `web/ui_contract_test.cjs`; scenario/delta result schema | UI CI checks explicit `delta_reach`, source SHA-256 values, added/removed reachable states and enabled transitions, and truncation flags. Latest browser CI `38728521793` additionally verifies every rendered transition row has a status and human-readable reason, and verifies guarded `t_cd` is `BLOQUEADA POR REGLA` with reason `prerequisite_transition_disabled`. This is verified for the audited synthetic scenarios, not all possible systems. | **verified** (synthetic contract only) |
| FC-3 — sequence execution panel | Exact ordered sequence; validate each step; expose blocked step/reason; immutable, auditable trace | `web/index.html` sequence selector/action and `#sequence-trace`; Python `execute_sequence` | UI test verifies concrete sequence action, starting state, ordered step 1, exported trace, trace SHA-256 and COMPLETED status. Latest browser CI `38727846589` passes the manual `t_ac, t_cd` blocked-attempt assertions: step 2 (`t_cd`), `temporal_prerequisite_not_satisfied`, missing `t_ab`, and trace SHA-256 are checked; successful execution is then restored and clean-source replay passes. The evidence does not establish immutability of the attempted-blocked trace beyond recording/digesting it. | **partial** |
| FC-4 — outcome and observer-context value assessment | Explicit outcome entry/provenance linked to execution; separate observer/context/criterion assessment; absent valuation is NOT_ASSESSED | No complete implementation established by the audited evidence | Current UI test evidence covers execution, delta and replay; it does not establish outcome/value entry, linkage, provenance, or NOT_ASSESSED behavior. | **pending** |
| FC-5 — run package and replay | Versioned self-contained package, canonical hashes, integrity verification and deterministic replay of stage artifacts | `web/index.html` export/import and package assessor; Python package/replay engine | Browser CI verifies fresh export/import, independent replay, matching recomputed result, tamper/divergence rejection, schema/version/hash rejection, malformed/oversized import handling, and stale-state clearing. Full package coverage for FC-4 outcome/value artifacts remains unverified. | **partial** |
| FC-6 — end-to-end CI | Browser/engine contract tests, historical compatibility, adversarial fixtures, clean-source replay, artifact inspection | `.github/workflows/collective-toy-engine-tests.yml` and associated tests | Runs 38725294922, 38725294916 and 38725295018 all succeeded. Evidence covers 116 valid/102 invalid cross-runtime fixtures, temporal fixture, historical Python suite, browser UI/import/replay/tamper tests, clean-source archive replay, and governance consistency. Full acceptance remains incomplete because FC-2–FC-5 have partial/pending criteria. | **partial** |

## First demonstrated gap and next operation

FC-1 and FC-2 are verified within the stated synthetic contract/scenario boundary. FC-3 has passing browser assertions for a blocked temporal attempt and subsequent valid execution, but immutability of the recorded blocked-attempt trace remains unverified. The next narrow gap is **FC-3 trace immutability**: determine whether the displayed/exported trace can be mutated after its digest is computed, then add a focused acceptance test and implement only the missing integrity protection. Do not alter the structural detector or OCR quality work.

FC-3's blocked-sequence trace and FC-4 outcome/value layers remain separate later gaps; do not fold them into the FC-2 correction.

## Non-claims

- This matrix records software-contract and CI evidence only.
- A green CI does not establish scientific validity of TGCV, causal claims, empirical generalization, or the canonical scientific definition of (T_{acc}).
- Synthetic outcomes must not be described as empirical findings.
- No promotion to `main` is implied; PR #67 remains a draft until a separate explicit review/promotion decision.
