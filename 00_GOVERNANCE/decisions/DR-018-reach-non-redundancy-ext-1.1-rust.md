# DR-018 — EXT-1.1 Rust Reach Non-Redundancy Result

**Date:** 2026-09-07  
**Status:** ACCEPTED  
**Scope:** EXT-1.1 Rust / structural identifiability and non-redundancy

## Decision

Accept `REACH_NON_REDUNDANCY_RESULT_REVIEW = PASS` for the EXT-1.1 Rust structural audit.

Under the tested Depth-1 successor-configuration representation, `Reach` is informationally non-redundant relative to the tested `T_acc` representation: the audit reports 2,490,426 `Delta T_acc` additions with non-redundant successor configurations and zero with redundant successor configurations; additionally, 69,890 pairs have equal local `T_acc` cardinality but different `Reach`.

## Interpretation boundary

This decision establishes **structural/informational non-redundancy**, not ontological primitivity. `Reach` therefore remains a derived/analytical structure for TGCV Core purposes unless a later core test demonstrates that it must be primitive.

No inference about execution, outcome, value, trajectory, or future activity is authorized by this decision.

## Provenance

- Dataset: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`
- `RSTAR_VERSION`: v0.2
- Audit artifact: `03_EXPERIMENTS/EXT-1.1_Rust/AUDIT_REACH_Non_Redundancy_v0.1.md`
- `REPORT_CANONICAL_SHA256`: `276c0e7883b72804b5f094bbe12ce0f15b7e021c4791a77c8149c60293f8c418`
- Audit runtime status: `RUNTIME_AUDIT_OK = True`

## Consequence

The EXT-1.1 Rust line may proceed beyond the Reach non-redundancy gate, subject to the remaining frozen experimental gates and without collapsing `Reach` into the TGCV Core merely on the basis of this result.
