# DR-021 — EXT-1.1 Rust accessibility operationalization

**Status:** PROPOSED NEW EXPERIMENTAL DECISION
**Scope:** Operationalization of `T_acc` after acceptance of candidate universe `T`

## 1. Decision status

This record is a **proposal only**. It does not accept or freeze the Rust accessibility predicate. Scientific execution remains blocked until the proposal is audited, any required implementation changes are made, and the decision is explicitly accepted.

## 2. Governing distinction

EXT-1.1 must preserve the strict separation:

`T` → candidate existence

`R*` → admissibility/selection under the frozen restricted SemVer semantics

`T_acc^(R*)` → selected accessible transformation structure

The candidate universe `T` is already accepted by DR-020. Its membership must not be redefined by this decision.

## 3. Proposed Rust accessibility definition

For an origin release `v_o` and an observed dependency edge `e=(v_o,p_d,q)`, a candidate transformation is accessible under EXT-1.1 iff the edge is observable and its target selection satisfies the frozen `R*` operator at the origin release cutoff.

For each edge, let:

`K(e,t) = {v_d ∈ T(e) | q is supported by R* and v_d satisfies q under the frozen temporal cutoff}`.

If `K(e,t)` is non-empty, define:

`v_d* = argmax_{v_d ∈ K(e,t)} SemVer(v_d)`.

Then:

`T_acc,t^(R*) = { (v_o,p_d,v_d*) | K(e,t) ≠ ∅ }`.

The resulting structure retains the dependency constraint and provenance required by the frozen R* specification.

## 4. Preconditions frozen by existing decisions

The proposal relies only on already frozen/accepted elements:

1. observational unit `package@version` (DR-007);
2. Rust package identity/domain (DR-019);
3. candidate universe `T` (DR-020);
4. historical temporal cutoff `created_at(v_d) <= created_at(v_o)`;
5. restricted R* grammar and deterministic maximal-version selection (R* v0.2 / DR-017).

No future release, downstream adoption, outcome, popularity, or live registry state may enter accessibility.

## 5. Resource term boundary

The generic TGCV logical form remains `Pre ∧ Target ∧ Resource`, as recorded in DR-011. This proposal does **not** invent Rust resource variables or thresholds.

For the current dependency-resolution transformation family, the resource predicate is therefore treated as **not yet operationally instantiated**. Any resource constraint that changes membership in `T_acc` requires a separate accepted decision record before scientific freeze.

Consequently, acceptance of this proposal would freeze the **R*-based dependency-accessibility layer**, not all possible Rust transformation families or resource semantics.

## 6. Important implementation finding

The existing `src/tacc_pipeline.py` must not be treated as the normative implementation of this proposal. It returns all versions satisfying a requirement rather than selecting the maximal admissible target required by R* and it uses the fixture helper `semver_reference.py`. The frozen specification explicitly distinguishes this behaviour from the normative R* resolver.

The normative implementation remains `src/rstar_v02.py`. fileciteturn72file0

## 7. Required conformance gate before acceptance

A dedicated audit must verify at minimum:

- exact and supported caret requirements resolve according to R*;
- unsupported requirements are reported as `UNSUPPORTED` and never guessed;
- target releases after the origin cutoff are excluded;
- each dependency edge yields at most one selected target version;
- selected target is the greatest eligible semantic version;
- candidate identity remains within `T`;
- dependency constraint `q` is provenance and selection input, not candidate-universe membership;
- row order cannot change the result;
- duplicate version IDs fail closed;
- empty candidate sets are distinguishable from execution errors;
- canonical output is reproducible across two runs;
- no live/current registry or outcome information is consulted.

## 8. Acceptance criteria

DR-021 may be accepted only if the conformance audit passes all mandatory criteria and any implementation discrepancy is resolved by an explicit versioned change before acceptance.

A passing conformance audit does not authorize confirmatory execution. Resource policy, outcome, sampling, baseline `B`, and `R` serialization remain separately governed.

## 9. Scientific rationale

This operationalization preserves the TGCV distinction between the existence of candidate transformations and their accessibility from a particular pre-outcome state. It also prevents the accessibility layer from retroactively changing the already audited candidate universe `T`.

## 10. Explicit non-claims

This proposal does not claim:

- reconstruction of historical Cargo resolution;
- completeness of Cargo's SemVer semantics;
- causal accessibility effects;
- that every TGCV transformation family has been operationalized in Rust;
- that resource feasibility has been resolved;
- that the experiment is scientifically frozen.

## 11. Next action

Run the **DR-021 R* conformance audit** against the frozen implementation and synthetic edge cases first. If it passes, prepare the acceptance amendment to the Decision Log. If it fails, record the discrepancy and correct the implementation under a new explicit change before acceptance.
