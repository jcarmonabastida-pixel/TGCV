# TGCV — Governance Current-State Validator Structural Audit v0.3

**Date:** 2026-09-09  
**Status:** CURRENT / OPERATIVE  
**Scope:** final structural repair of `00_GOVERNANCE/tools/validate_current_state.py` following CI validation of the v0.2 repair.

## Finding

CI confirmed that semantic version parsing was repaired, but exposed a representation mismatch in the traceability dependency check. The traceability CSV identifies the current master by semantic asset ID (`RMA-v3.7`), while the RMA pointer resolves to the filename (`TGCV_RMA_v3.7.md`).

The validator was therefore comparing two different identity layers.

## Corrective rule

Canonical assets may expose both a filesystem identity and a semantic governance identity. The validator must compare like with like:

`TGCV_RMA_v3.7.md` → parsed version `v3.7` → semantic asset identity `RMA-v3.7`.

No current version is hardcoded. The semantic identity is derived from the resolved canonical RMA version.

## Structural outcome

The validator now distinguishes:

1. **Location identity** — canonical filesystem path.
2. **Version identity** — semantic version parsed from the canonical RMA filename.
3. **Governance asset identity** — `RMA-{version}` used by traceability dependencies.

The traceability CSV remains parsed as CSV and validated structurally and semantically.

## Scientific impact

**NO SCIENTIFIC CLAIM CHANGE.**

No Core definition, claim, threshold, falsification criterion, epistemic status, experiment result, authorization boundary or Industrial Track decision is changed.

## Gate consequence

This is the final validator repair attempt in this cycle. The hard gate remains active until CI confirms `GOVERNANCE_CURRENT_STATE=PASS` on the resulting commit. No scientific or industrial operation proceeds before that confirmation.
