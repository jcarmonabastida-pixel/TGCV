# DR-040 — RUST-DYN-2 Reach-Graph Independence Gate v0.1

## Status

**ACCEPTED — SCIENTIFIC BLOCKER IDENTIFIED / REAL-DATA EXECUTION NOT AUTHORIZED**

Date: 2026-09-08

## Trigger

During implementation review for RUST-DYN-2-EXEC-1B, the frozen RUST-DYN-2 design was compared against the available Rust structural representation.

The design requires Reach and Trajectory to be constructed through an **independently constructed structural successor graph** and explicitly prohibits defining Reach as a projection of `T_acc` or Trajectory as an ordering of `T_acc`.

The currently available executor representation constructs bounded Reach/Trajectory directly from resolved `T_acc` transformations. That would violate the frozen independence requirement if reused for RUST-DYN-2.

Therefore, constructing a real-data executor by simply adapting RUST-DYN-EXEC-1 would create a semantic deviation, even though the code could technically run.

## Finding

The frozen Rust input schema currently provides:

- package-version origins: `id, package_id, version_str, created_at`;
- dependency declarations: `depending_version, depending_on_package, semver_str`;
- frozen resolver `R* v0.2` for admissible dependency transformations.

Under the current D-OPS-1/RUST-DYN-STATE-1 semantics, `version_id` is the bounded successor-state identifier, while `T_acc` contains the resolved transformation identities leading to target versions.

A Reach implementation based directly on the resolved target versions of `T_acc` is therefore a projection of `T_acc`, not an independent successor graph.

Conversely, using later package releases as successors would introduce later release activity and violate the existing information firewall.

Using package IDs instead of version IDs would change the frozen successor-state semantics and would not constitute a silent implementation detail.

## Decision

**RUST-DYN-2 real-data execution must NOT proceed until the independence of the structural successor graph is explicitly resolved.**

No executor is authorized to claim RUST-DYN-2 compliance while Reach/Trajectory are merely projections or orderings of `T_acc`.

This is a methodological protection, not an execution failure and not a failure of the Rust dataset.

## Consequence for implementation

The next controlled operation is:

**RUST-DYN-2-STATE-GRAPH-1 — Successor-Graph Independence Specification Gate.**

That gate must choose one of the following, with explicit scientific justification:

1. identify an already frozen structural relation in the Rust dataset that yields `version_id` successor states independently of `T_acc` and without forbidden future information;
2. define a new independent successor-state relation from the existing frozen fields, with an explicit amendment to RUST-DYN-STATE-1 and RUST-DYN-2;
3. conclude that the present Rust dataset cannot support the RUST-DYN-2 downstream test without changing the empirical object, in which case RUST-DYN-2 remains formally specified but empirically unresolved for Rust.

Any option that changes the analytical semantics requires a new design review before implementation.

## Evidence already accepted

- RUST-DYN-2 design review: DR-038.
- Synthetic conformance: `RUST-DYN-2_EXEC-1A_SYNTHETIC_CONFORMANCE_CLOSURE_v01.md`.
- Real-data input preflight: `RUST-DYN-2_EXEC-1A_REAL_DATA_PREFLIGHT_CLOSURE_v01.md`.
- Pre-authorization boundary: DR-039.

These remain valid. None authorizes real execution under a semantically non-independent Reach/Trajectory implementation.

## Scientific boundary

This finding does not alter:

- `Core_ontological = S`;
- `T_acc` as the explicit analytical object;
- `ΔT_acc` as the primary comparative object;
- the closed RUST-DYN-EXEC-1 result;
- TR-131/DR-032 conclusions.

It also does not imply that Reach or Trajectory are theoretically redundant. It means only that the present Rust operationalization does not yet provide a valid independent empirical representation for testing their distinction.

**REAL-DATASET EXECUTION AUTHORIZED: NO.**
