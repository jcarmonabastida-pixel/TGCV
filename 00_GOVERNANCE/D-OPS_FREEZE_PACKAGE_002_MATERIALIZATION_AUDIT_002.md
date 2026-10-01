# TGCV — D-OPS Freeze Package 002 — Materialization Audit 002

**Status:** BLOCKED — CONTRACT/INDEPENDENCE ISSUES
**Date:** 2026-10-01
**Package:** D-OPS_FREEZE_PACKAGE_002
**Supersedes:** Materialization Audit 001 as the current audit record

## 1. Scope

Audit Package 002 as currently present on `main`, after exact-byte materialization and SHA-256 registration.

This audit does not execute the scientific/conformance test and does not authorize execution.

## 2. PASS — package materialization

All declared Package 002 input/executable files were materialized through the GitHub API content route and hashed from their exact UTF-8 bytes.

The provenance manifest now records SHA-256 values for:
- D0_FORMAL_FIXTURE.json
- G_S_SPECIFICATION.md
- R3_manifest_D0.json
- README.md
- dops_canonical.py
- dops_gs.py
- dops_oracle.py
- dops_perturbations.py
- expected_results.json
- oracle_specification.md
- perturbation_manifest.json

Git blob SHAs were not substituted for SHA-256 byte hashes.

## 3. PASS — executable components present

The package now contains:
- canonicalizer/relation builder;
- G_S implementation;
- oracle implementation;
- perturbation implementation.

Therefore the corresponding absence finding in Materialization Audit 001 is obsolete.

## 4. PASS — D0/R3 reconfiguration structure

The frozen D0 fixture contains the three transformations `tau_move`, `tau_wait`, and `tau_scan`.

The ex ante R3 manifest contains:
- `tau_move -> tau_wait`
- `tau_wait -> tau_move`

The declared reconfiguration removes exactly:
- `tau_move -> tau_wait`

and adds exactly:
- `tau_wait -> tau_scan`

U, equivalence, R1 and R2 remain unchanged for this perturbation.

## 5. FAIL — G_S executable contract mismatch

The frozen G_S specification defines the output domain:

`NO_STRUCTURAL_CHANGE | STRUCTURAL_CHANGE | NON_COMPARABLE`

The current `dops_gs.py` implementation returns a boolean equality result for the four comparable representations and the string `NON_COMPARABLE` for an unknown representation.

Therefore the implementation does not conform to the declared output contract.

This must be resolved before freeze preflight.

## 6. FAIL — independent oracle boundary not established

The frozen oracle specification requires an independent oracle that independently canonicalizes U, equivalence, R1, R2 and ex ante R3 and computes the complete five-way diff.

The current `dops_oracle.py` imports `canonical_omega` directly from `dops_canonical.py`.

No separate oracle-side canonicalization implementation is currently present in Package 002.

Consequently, the required independence of the oracle from the canonicalizer/SUT has not been established.

This must be resolved before freeze preflight.

## 7. Scientific boundary

`execution_authorized=false` remains in the provenance manifest.

No scientific/conformance execution is authorized by this audit.

## 8. Decision

**DO NOT RUN FREEZE PREFLIGHT.**

Package 002 is now materially hashed, but it is not yet contract-clean or independently auditable.

## 9. Required next operation

Resolve exactly these two open issues:
1. bring `dops_gs.py` into exact conformance with the frozen G_S output contract;
2. provide a genuinely independent oracle-side canonicalization/diff implementation, without reusing `dops_canonical.py`.

Then rerun this materialization audit against the resulting package before freeze preflight.

No other scientific redesign is required by this audit.
