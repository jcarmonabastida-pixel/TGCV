# RUST-DYN-2-STATE-GRAPH-1 — Successor-Graph Independence Specification v0.1

## Status

**CLOSED — NO VALID INDEPENDENT VERSION-STATE GRAPH IDENTIFIED / RUST-DYN-2 EMPIRICAL EXECUTION BLOCKED UNDER CURRENT FREEZE**

Date: 2026-09-08

## 1. Purpose

Determine whether the frozen Rust dataset and operational semantics provide a structural successor graph over `version_id` that can support Reach and Trajectory independently of `T_acc`, as required by DR-038 and DR-040.

This gate does not test the TGCV theory and does not reopen TR-131 or RUST-DYN-EXEC-1.

## 2. Frozen requirements

DR-038 requires:

- `T_acc`, Reach and Trajectory constructed independently;
- Reach not defined as a projection of `T_acc`;
- Trajectory not defined as an ordering of `T_acc`;
- `version_id` retained as the bounded successor-state identifier;
- no feedback from downstream objects into `P_tau`;
- no future/outcome/predictive information;
- DR-035 adjacent temporal population;
- H=1 for the first implementation.

RUST-DYN-STATE-1 accepts `version_id` only as a bounded successor-state identifier within the frozen structural transformation graph; it does not establish an independent successor relation. fileciteturn290file0

## 3. Available structural relations

The frozen dataset exposes two relevant relations:

1. package-version identity and creation time:
   `id, package_id, version_str, created_at`;
2. dependency declarations:
   `depending_version, depending_on_package, semver_str`.

The frozen resolver `R* v0.2` maps a dependency declaration and admissible target-version candidates to a selected target version. Its interface explicitly returns `selected_version_id` and `selected_version`. fileciteturn285file0

## 4. Candidate A — resolved dependency target graph

Construction:

`depending_version → R* → selected_version_id`

Decision: **REJECTED for independent Reach.**

Reason: this is exactly the transformation-resolution path used to construct `T_acc`. The resulting successor set is therefore a projection of the accessible transformation set.

The current RUST-DYN-2 executor implements Reach by extracting target IDs from canonical T_acc tuples, confirming that this construction is not independent. fileciteturn296file0

Using this path for the real experiment would violate the frozen independence requirement in DR-038 and the pre-authorization boundary in DR-039. fileciteturn283file0 fileciteturn292file0

## 5. Candidate B — raw dependency incidence graph

Construction:

`depending_version → depending_on_package`

Decision: **REJECTED as a version-state Reach graph.**

Reason: the edge terminates at `package_id`, whereas the frozen downstream state representation requires `version_id`. A package-level edge does not identify a successor package-version state without an additional version-selection rule. Introducing such a rule would either reproduce `R*`/T_acc semantics or create a new operational definition requiring a separate design amendment.

Therefore this raw relation cannot be silently promoted to the frozen `Reach_H` object.

## 6. Candidate C — later package releases

Construction would use later `created_at` observations as successor states.

Decision: **REJECTED.**

Reason: this would introduce later release activity into the downstream structural representation and violate the information firewall frozen for D-OPS-1/RUST-DYN-2.

It would also change the interpretation from an independently available structural successor relation to a retrospective temporal relation.

## 7. Candidate D — package/version metadata ordering

Possible secondary orderings such as `version_id`, lexical `version_str`, archive order, or row order do not constitute structural successor relations.

Decision: **REJECTED.**

Reason: they impose an ordering but do not define a transition relation. They would create artificial trajectories rather than recover an independent successor graph.

## 8. Candidate E — all structurally possible target versions

Constructing all target package versions satisfying a dependency requirement without applying the frozen maximum-selection rule would produce a candidate transformation universe or an alternative accessibility representation.

Decision: **REJECTED as independent Reach under the present freeze.**

Reason: the resulting target-version set remains generated from dependency requirements and target-version admissibility, and therefore overlaps the construction of `U_tau`/`T_acc`. It cannot be claimed as an independent successor-state graph without changing the semantics of the experiment.

## 9. Independence conclusion

No available relation in the frozen Rust representation has been identified that simultaneously satisfies all of the following:

1. successor node is the frozen `version_id` state identifier;
2. relation is independently defined from `T_acc`;
3. relation does not require `R*` accessibility selection;
4. relation does not use later release activity;
5. relation does not introduce arbitrary ordering;
6. relation does not introduce outcome/predictive information;
7. relation preserves the frozen D-OPS-1/STATE-1 semantics.

Therefore the required independent successor graph is **not available under the current operational freeze**.

## 10. Decision among DR-040 alternatives

DR-040 provided three possible outcomes:

1. identify an already frozen independent relation — **NOT ESTABLISHED**;
2. define a new relation from existing fields with explicit amendments — **NOT ADOPTED in this gate**, because doing so would change the empirical object and requires a new design rather than an implementation detail;
3. conclude that the present Rust dataset cannot support RUST-DYN-2 without changing the empirical object — **SELECTED**.

## 11. Scientific consequence

RUST-DYN-2 remains a valid formal TGCV downstream test design, but it is **empirically unresolved in the current Rust operationalization**.

This conclusion does not mean:

- Reach is theoretically redundant;
- Trajectory is theoretically redundant;
- `T_acc` is sufficient for all downstream analysis;
- TGCV fails its downstream hypothesis;
- the Rust dataset is defective.

It means only that the present frozen Rust data/semantics do not supply the independent structural relation required to test the hypothesis without semantic contamination.

## 12. Preservation of established results

The following remain closed and unaffected:

- TR-131 and DR-032;
- D-OPS-1;
- RUST-DYN-EXEC-1 and DR-037;
- RUST-DYN-2 design and DR-038;
- RUST-DYN-2 synthetic conformance;
- RUST-DYN-2 real-data input preflight;
- DR-039 and DR-040.

In particular, the RUST-DYN-EXEC-1 empirical result must not be reused as evidence for RUST-DYN-2.

## 13. Governance boundary

No real-data RUST-DYN-2 execution is authorized.

No H>1 extension is authorized.

No executor modification is authorized under the current design merely to manufacture an independent Reach relation.

A future attempt would require a new empirical design specifying a genuinely independent successor relation and a new governance review.

## 14. Final decision

**RUST-DYN-2-STATE-GRAPH-1 = CLOSED — INDEPENDENT SUCCESSOR GRAPH NOT IDENTIFIED UNDER CURRENT RUST FREEZE.**

**RUST-DYN-2 empirical execution in Rust = UNRESOLVED / BLOCKED BY OPERATIONAL REPRESENTATION.**

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

## 15. Next controlled operation

The next appropriate operation is not another Rust execution attempt. It is a **TGCV downstream architecture review** deciding whether:

- RUST-DYN-2 should remain a formal cross-domain test with Rust marked empirically unresolved; or
- another domain/dataset should be selected where an independent successor relation is observable without altering the TGCV architecture.
