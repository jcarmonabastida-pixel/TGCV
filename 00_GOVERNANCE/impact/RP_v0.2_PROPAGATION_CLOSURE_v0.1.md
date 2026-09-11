# TGCV — Research Prospectus v0.2 Propagation Closure

**Asset:** `TGCV-EXT-RP-001`  
**Version:** `v0.2`  
**Date:** `2026-09-11`  
**Status:** `CLOSED / CURRENT / CONTROLLED`

## 1. Scope

This record closes the controlled promotion of the Research Prospectus from the 2026-09-08 working/current-situation draft to the current programme-level prospectus aligned with the canonical TGCV state.

## 2. Canonical inputs

- RMA v3.32 — current operative architecture.
- Evidence→Claim Matrix v1.1 — current claim control.
- TR-131 — accepted analytical indispensability boundary for `T_acc`.
- TCP v0.4 — current testability and methodological synthesis.
- Vision Paper v0.3 — current research vision and evidence boundary.
- ARM v0.2, RII v0.1 and MOI v0.1 — current controlled external interfaces.

## 3. Material corrections

RP v0.2 updates the prior draft to reflect:

- `Core_ontological = S` and `T_acc = F(S,C,L)`;
- `T_acc` as analytically indispensable but not an independent ontological primitive;
- interaction `I` as explanatory mechanism rather than Core primitive;
- the current downstream chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`;
- TR-132-MOD-1 methodological consequence that complete ex-ante enumeration of `T_acc` is not a universal prerequisite;
- current bounded evidence from IUT-A-01 U2, IT-NOSD-010, EXT-UPD-4.8 O3 and Class-II AWS;
- closure of D-OPS-24 and EXT-UPD-4.8 within their authorized scopes, without presenting them as pending;
- current no-claim and authorization boundaries.

## 4. Claim impact

No C01–C16 claim status or level is upgraded by this asset update. The Research Prospectus is a programme-level synthesis and does not constitute new scientific evidence, validation, industrial utility evidence, causal evidence, value evidence, superiority evidence, or execution authorization.

## 5. Historical preservation

`TGCV-EXT-RP-001_v0.1.md` remains immutable historical material. The IE-specific adaptation remains separate and is not authoritative for the canonical Core.

## 6. Propagation completed

The following canonical surfaces were updated:

- `05_ASSETS/Research_Prospectus/TGCV-EXT-RP-001_v0.2.md`
- `05_ASSETS/Research_Prospectus/README.md`
- `05_ASSETS/README.md`
- `00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv`

The traceability entries identify RP v0.2 as current and RP v0.1 as historical.

## 7. Governance boundary

This closure does not authorize any experimental, methodological or industrial execution. Standing industrial execution authorization remains `NONE`.

## 8. Closure decision

**RP v0.2 is CLOSED / CURRENT / CONTROLLED and canonically propagated.**

Final validator gate remains required after synchronization of the local execution copy with `origin/main`.