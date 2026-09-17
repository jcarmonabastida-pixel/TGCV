# TGCV — VSL Synthetic Minimum v0.1
## Formal Freeze Record 001

**Date:** 2026-09-18  
**Status:** `FROZEN`  
**Scope:** Synthetic demonstrator only  
**Freeze basis:** Circularity and Identifiability Review 002

## 1. Frozen specification

The following artifact is formally frozen:

`00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_v0.1_SPECIFICATION.md`

Specification blob SHA at freeze:

`2b7c28afe0ab58e987911292903f82483cc96ab4`

## 2. Frozen outcome definition

The following artifact is frozen as the operational outcome definition:

`00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_OUTCOME_DEFINITION_v0.1.md`

Outcome definition blob SHA at freeze:

`RETRIEVED FROM CANONICAL GITHUB AT FREEZE`

Frozen outcome:

`O(S)=q+0.5r`

with:

`S_0=(10,10)`

and:

`O(S_0)=15`

## 3. Frozen Value mapping

`V*(S)=O(S)`

and:

`ΔV*=ΔO`

No other Value mapping is permitted in v0.1.

## 4. Frozen non-circularity boundary

The VSL/outcome path MUST NOT inspect or consume:

- `T_acc`;
- `ΔT_acc`;
- `Pτ`;
- treatment assignment;
- selected transformation identity;
- accessibility-change flags;
- Value-derived variables.

The operational separation is frozen as:

`state/context → T_acc`

`final state (q,r) → O`

`O → V*`

## 5. Frozen synthetic case requirements

The implementation must contain:

| Case | ΔT_acc | ΔO | ΔV* |
|---|---:|---:|---:|
| T1 | 0 | 0 | 0 |
| T2 | ≠0 | 0 | 0 |
| T3 | ≠0 | +4 | +4 |
| T4 | 0 | +2 | +2 |
| NC1 | 0 | 0 | 0 |
| NC2 | ≠0 | 0 | 0 |

These are protocol requirements, not execution results.

## 6. Freeze provenance

Freeze is authorized by:

`TGCV_VSL_SYNTHETIC_MIN_CIRCULARITY_IDENTIFIABILITY_REVIEW_002.md`

Review commit:

`fcff5bffa4ad72369879fd75bb3093ebdcad712c`

The freeze is specification-level only.

It does not constitute experimental evidence.

## 7. Immutability rule

No substantive modification may be made to the frozen v0.1 specification.

Any change to:

- objective;
- outcome;
- outcome formula;
- direction;
- reference frame;
- Value mapping;
- non-circularity boundary;
- required cases;
- domain;
- reproducibility rule;

requires a new version.

## 8. Execution boundary

After this freeze:

- fixture construction is authorized;
- protocol construction is authorized;
- runner construction is authorized only against this frozen contract;
- execution is not yet evidence until runtime integrity and audit conditions are satisfied.

No C09 field is imported.

No TGCV Core, RMA, Evidence-to-Claim Matrix or claim status is changed by this freeze.

## 9. Governance disposition

`VSL_SYNTHETIC_MIN_v0.1 = FROZEN`

`EXPERIMENTAL_EVIDENCE = NOT_YET_GENERATED`

`C09 = UNCHANGED`

`CORE = UNCHANGED`

`RMA = UNCHANGED`
