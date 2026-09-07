# AUDIT DR-029 — TR-131 Implementation / Pre-Execution Audit Protocol v0.1

**Status:** PROTOCOL — NO EXECUTION AUTHORIZED  
**Decision gate:** DR-029 v0.2  
**Scope:** EXT-1.1 Rust / TR-131 State Sufficiency / Transformational-Space Irreducibility

## 1. Purpose

Verify, before constructing or running the TR-131 executor, that the accepted DR-029 design is implementable without introducing an unfrozen analytical choice, prohibited information, alternative state representation, alternative resolver, sampling, or predictive criterion.

This document is an audit protocol, not an execution result. It does not authorize dataset extraction or a TR-131 conclusion.

## 2. Frozen normative inputs

The audit shall treat the following as normative and immutable:

1. DR-029 v0.2 — candidate conventional state representation and comparison rule;
2. DR-025A v0.2 — baseline representation `B`;
3. EXT-1.1 Operational Specification v0.1 — Rust state, candidate transformation and accessibility boundaries;
4. DR-021 — accepted/proposed R*-based accessibility construction and its provenance constraints;
5. DR-026A — accepted canonical `T_acc` representation and structural integrity requirements;
6. frozen Rust dataset `rust_repos_2022_09_07.zip`;
7. normative `R* v0.2` implementation for construction of `T_acc`.

No result from DR-027C may alter any of these inputs.

## 3. Exact object to be implemented

For every admissible origin release `v_o`, construct:

`B(v_o) = (V_o, H_o, A_o, D_o)`

where:

- `V_o` = exact observed `version_str`;
- `H_o` = count of earlier same-package releases with `created_at < created_at(v_o)`;
- `A_o` = elapsed days from earliest observed same-package release to `created_at(v_o)`;
- `D_o` = count of raw dependency declaration rows attached to `v_o`.

State equivalence is exact tuple equality:

`v_a ~_B v_b  iff  B(v_a) = B(v_b)`.

For every origin, construct the canonical `T_acc(v_o)` already defined by DR-021/DR-026A.

The structural comparison is set equality of canonical transformation membership, not comparison of cardinality alone.

## 4. Mandatory audit checks

### A. State representation fidelity

Verify that the implementation:

- uses exactly the four DR-025A components;
- treats `version_str` as nominal categorical information;
- computes prior-release count strictly from earlier same-package releases;
- computes package age from the earliest observed same-package release;
- counts raw dependency declaration rows without semantic resolution;
- excludes package identity from `B`;
- does not use `B_num` for equivalence;
- does not add SemVer arithmetic, ordering, embeddings, target encoding, learned features, or model-derived information.

### B. Temporal integrity

Verify that all fields used for `B` and `T_acc` are reconstructible from the frozen historical structural snapshot and that no post-origin information enters state equivalence.

The implementation must not use `Y_180`, daily downloads, adoption, popularity, later releases, later package activity, or any future outcome.

### C. T_acc fidelity

Verify that the executor reuses the normative `T_acc` construction rather than reimplementing a different resolver.

The following must remain true:

- historical temporal cutoff is respected;
- target selection follows frozen `R* v0.2` semantics;
- at most one selected target exists per dependency edge;
- selected target is canonical and provenance traceable;
- empty `T_acc` is represented as an empty set, not missing;
- future targets are excluded;
- canonical ordering is deterministic.

### D. Equivalence construction

Verify that:

- grouping key is exactly `(V_o,H_o,A_o,D_o)`;
- equality is exact, not approximate;
- no binning, nearest-neighbour matching, hashing with collision risk, learned similarity, or post-hoc grouping is used;
- classes with fewer than two origin observations are retained as admissible but generate no pairwise comparison;
- all origin observations are considered unless a separate integrity failure excludes them;
- exclusion is fail-closed and explicitly counted.

### E. Comparison construction

For every `B` equivalence class containing multiple distinct origins, compare canonical transformation membership sets.

The audit must require reporting of:

- total origin observations;
- number of distinct `B` equivalence classes;
- singleton classes;
- multi-member classes;
- number of admissible comparisons or class-level comparisons;
- classes with unequal `T_acc` membership;
- number of constructive witnesses;
- deterministic identifier/provenance for every witness.

The primary structural predicate is:

`B(v_a) = B(v_b) AND T_acc(v_a) != T_acc(v_b)`.

A difference in `A_count` may be reported descriptively but cannot substitute for membership-set comparison.

## 5. Information firewall

The implementation must contain explicit assertions or equivalent accounting showing that the following are not read by the TR-131 selection/equivalence logic:

- outcome tables;
- `Y_180`;
- download counts;
- future activity;
- predictive metrics;
- model outputs;
- `Reach`;
- trajectory variables;
- DR-027 result values;
- package identity as a feature;
- any post-hoc selection variable.

The audit must fail if any prohibited channel is used.

## 6. Determinism and replay

The executor must use deterministic ordering for:

1. origin observations;
2. construction of `B`;
3. canonical `T_acc` serialization;
4. equivalence-class identifiers;
5. witness reporting.

A replay of the same frozen inputs must reproduce the same class counts, comparison counts, witness set, and canonical output hash.

## 7. Exhaustive census requirement

The default and preferred execution mode is a deterministic census over all admissible origin observations. No sampling is authorized by DR-029.

The previously established computational feasibility result supports census execution; this audit must not use that feasibility as evidence for TR-131 itself.

## 8. Synthetic conformance tests required before dataset execution

Before the real Rust dataset is touched by the TR-131 executor, synthetic fixtures must test at minimum:

1. two identical `B` states with identical `T_acc` → no witness;
2. two identical `B` states with different `T_acc` membership → positive witness;
3. same `A_count` but different `T_acc` membership → positive witness;
4. different `A_count` with same membership → impossible under set semantics and must be handled consistently;
5. empty `T_acc` versus non-empty `T_acc` within identical `B` → positive witness;
6. duplicate origin identifiers → fail closed;
7. missing structural input → fail closed;
8. row-order permutation → identical result;
9. prohibited outcome field made available → executor must not consult it;
10. repeated execution → identical result and hashes.

These tests are implementation conformance tests only. They do not constitute empirical evidence from the Rust dataset.

## 9. Acceptance criteria for the audit

The implementation/pre-execution audit may PASS only if all mandatory conditions are demonstrated:

- exact `B` fidelity;
- exact `T_acc` reuse;
- exact equivalence relation;
- direct set-membership comparison;
- exhaustive census design;
- deterministic canonicalization;
- replayability;
- synthetic conformance suite defined and passing;
- prohibited-information firewall verified;
- no unresolved ambiguity affecting the scientific interpretation.

Any unresolved ambiguity concerning the state representation, transformation identity, `T_acc` membership, equivalence relation, or information firewall is a BLOCKER and must not be resolved by inspecting empirical results.

## 10. Scientific boundary

A passing implementation audit establishes only that the proposed TR-131 test can be executed faithfully under the frozen design.

It does not establish that `T_acc` is irreducible, that a witness exists, or that TGCV is supported.

The subsequent scientific result must be classified only as:

- support for TR-131 relative to `B`,
- non-support for TR-131 relative to `B`, or
- indeterminate.

## 11. Governance status

**No execution is authorized by this protocol.**

The next implementation step after audit acceptance is construction of the deterministic executor and synthetic conformance fixture. Only after that implementation gate passes may the real Rust dataset be executed.
