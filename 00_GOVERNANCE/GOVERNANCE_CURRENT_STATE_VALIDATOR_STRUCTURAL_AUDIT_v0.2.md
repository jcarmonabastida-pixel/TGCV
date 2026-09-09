# TGCV — Governance Current-State Validator Structural Audit v0.2

**Date:** 2026-09-09  
**Status:** CURRENT / OPERATIVE  
**Scope:** second-pass structural audit of `00_GOVERNANCE/tools/validate_current_state.py` after CI execution of the v0.1 repair.

## Finding

The first structural repair correctly changed traceability handling from key/value parsing to CSV parsing, but CI exposed a second defect in the version parser: the expression `v[^.]+` did not admit semantic versions containing a dot, such as `v3.7`, although the canonical RMA uses that valid form.

This is a validator-contract defect, not a canonical-state or scientific-state defect.

## Corrective rule

RMA versions are parsed as semantic numeric versions of the form `vN`, `vN.N`, `vN.N.N`, etc. The validator must derive the version from the canonical RMA pointer and must not encode the current version as a constant.

The resulting version is then used only to resolve the corresponding versioned traceability asset.

## Structural checks retained

- canonical manifest roles and locations;
- stable RMA and Evidence→Claim Matrix current pointers;
- dynamic RMA master resolution;
- RMA `CURRENT / OPERATIVE` status;
- dynamic matrix version alignment;
- CSV schema and row integrity for current traceability;
- required `RMA-current` and `TRACEABILITY-current` rows;
- bidirectional current RMA / traceability alignment;
- existence of versioned traceability derived from the resolved RMA version;
- STATUS alignment;
- stable validator location.

## Scientific impact

**NO SCIENTIFIC CLAIM CHANGE.**

No Core definition, claim, threshold, falsification criterion, epistemic status, experiment result, authorization boundary or Industrial Track decision is changed by this repair.

## Gate consequence

This repair remains governance infrastructure only. The hard gate remains active until GitHub Actions independently confirms `GOVERNANCE_CURRENT_STATE=PASS` on the repaired commit.

No new scientific or industrial operation is authorized before that confirmation.
