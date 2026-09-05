# EXT-1.1 — Resolver Specification R* v0.2

**Status:** FROZEN FOR EXPERIMENTAL USE
**Date:** 2026-09-05
**Scope:** EXT-1.1 Rust empirical experiment

## 1. Purpose

This document freezes the operational definition of the restricted resolver/accessibility operator used by EXT-1.1.

The experiment does **not** claim to reconstruct the historical Cargo resolver. The published Rust dataset does not retain sufficient information to identify all historical Cargo resolution inputs and semantics (for example optional/feature-dependent, target-specific, dependency-kind, yanked-state, lockfile and historical registry/index state).

Accordingly, EXT-1.1 defines an explicitly restricted operator `R*` that is identifiable from the retained dataset fields and can be reproduced deterministically.

The empirical object is therefore:

`T_acc,t^(R*) = F(S_t, C_t, R*)`

and not an asserted reconstruction of `T_acc,t^(Cargo)`.

## 2. Identifiability boundary

The following distinction is mandatory in all EXT-1.1 reporting:

- `T_acc^(EXT-1.1) = F(S,C,R*)` — admissible claim under this freeze.
- `T_acc^(EXT-1.1) = T_acc^(Cargo)` — **not established and must not be claimed**.
- Agreement with a contemporary or reconstructed Cargo execution, if later demonstrated, is a validation result, not an assumption built into this specification.

## 3. Source data

The operational reconstruction may use only the frozen dataset artifacts and fields needed by the experiment:

- `packages(id, name, ...)`
- `package_versions(id, package_id, version_str, created_at)`
- `package_dependencies(depending_version, depending_on_package, semver_str)`

No live registry, current crates.io index, ambient Cargo cache, or unrecorded external state may enter the scientific calculation.

## 4. State and historical context

For an origin package version `v_o` with timestamp `t_o = created_at(v_o)`, define the historical registry context:

`C_t = { package versions with created_at <= t_o }`.

A target version `v_d` is temporally eligible only when:

`created_at(v_d) <= created_at(v_o)`.

This rule is a leakage-control rule and is part of `R*`.

The target package is identified by the observed `depending_on_package` relation. The dependency edge itself is an observed dataset relation; it must not be relabelled as a Cargo-normal/unconditional dependency, because the published export does not retain all dependency-kind/feature metadata needed to establish that historical fact.

## 5. Candidate eligibility

For each observed dependency edge `(v_o, p_d, q)`:

1. `v_o` must exist in `package_versions`.
2. `p_d` must identify the target package in `packages`.
3. `v_d` must be a version of `p_d`.
4. `created_at(v_d) <= created_at(v_o)`.
5. `q` must belong to the supported constraint grammar defined in Section 6.
6. Candidates must be unique by version identifier.
7. No future version may enter the candidate set.

The operator is therefore defined over **observable dependency edges plus reconstructible historical target versions**, not over unobserved Cargo dependency semantics.

## 6. Supported version-constraint grammar

EXT-1.1 v0.2 deliberately uses a conservative supported grammar. A dependency constraint is resolver-eligible only when its semantics are implemented and tested by the experiment code.

At minimum, the current implementation supports:

- exact constraints: `=X.Y.Z`
- caret constraints of the form `^1.0` and equivalent supported stable `1.x.y` ranges used by the microtests.

Unsupported Cargo SemVer forms, prerelease semantics, wildcards, tilde ranges, compound requirements, inequality combinations, and other forms not explicitly implemented must be classified as **UNSUPPORTED**, not guessed.

The experiment must record the number and identity of excluded/unsupported constraints.

**Important:** this is an experimental admissibility grammar, not a claim that these forms exhaust Cargo SemVer.

## 7. Candidate selection

For each eligible edge, form the candidate set `K(e,t)` from versions satisfying the frozen constraint semantics and temporal cutoff.

When `K(e,t)` is non-empty, select the candidate with the greatest semantic version under the implemented ordering. Ties are impossible after version-identity deduplication; if implementation encounters an unresolved tie or ordering ambiguity, execution must fail closed.

The selected edge is represented as:

`e* = (v_o -> v_d*)`.

The selection operator is deterministic and must not depend on database row order.

## 8. Definition of T_acc^(R*)

For each origin version `v_o`, define its accessible dependency-resolution structure as the set of selected admissible target-version edges:

`T_acc,t^(R*) = { (v_o, p_d, v_d*) | edge is observable, temporally eligible, constraint-supported, and K(e,t) != empty }`.

The experiment must retain sufficient provenance to reconstruct:

- origin version identifier;
- origin package/name;
- target package identifier/name;
- original constraint string;
- candidate count;
- selected target version identifier/version string;
- origin and target timestamps;
- exclusion reason where no selection is made.

`T_acc` is treated as a **structure**, consistent with the stabilized TGCV ontology; it is not reduced to a bare cardinality.

## 9. Explicit exclusions

The following are outside the identifiable scope of `R*` unless separately introduced as frozen observable inputs:

- historical Cargo lockfiles;
- historical Cargo registry/index snapshots not contained in the frozen fixture;
- current/live registry state;
- ambient local Cargo cache or filesystem state;
- yanked status when not retained in the dataset;
- optional dependencies and feature activation semantics when not retained;
- target-specific dependency activation;
- build/dev dependency distinctions when not retained;
- path dependencies;
- git dependencies;
- workspace inheritance not represented in the exported fields;
- dependency resolution semantics not expressible in the frozen grammar.

Excluded cases are not silently converted into negative evidence. They are reported as excluded/unsupported observations.

## 10. Cycle-pruning and dataset provenance

The published dataset pipeline includes dependency-link processing associated with cycle removal. Therefore `package_dependencies` is not to be interpreted as an untouched historical Cargo dependency graph without qualification.

EXT-1.1 must treat the exported dependency relations as the empirical source relation and preserve the dataset's provenance. Any cycle-related flags or retained/pruned information available in the actual frozen artifact must be handled according to the acquisition manifest and execution code; where such information is unavailable in the retained export, the limitation must be stated rather than inferred away.

## 11. Reproducibility and isolation

The scientific execution must:

- run against the frozen local dataset only;
- isolate Cargo home/cache if Cargo is used for auxiliary validation;
- prohibit live registry/index access;
- prohibit unrecorded environment-dependent inputs;
- record software/runtime versions;
- record input hashes;
- produce deterministic outputs;
- perform two independent runs on the same frozen inputs.

Any missing required input causes a fail-closed result rather than an inferred substitute.

## 12. A/B/C validation protocol

The execution protocol is:

**A — Baseline:** run the frozen `R*` implementation on the designated historical fixture/data slice.

**B — Counterfactual:** modify only the pre-registered factor under test while holding all other frozen inputs constant.

**C — Reproduction:** repeat the relevant A/B computation from a clean isolated environment and compare canonicalized outputs and hashes.

A scientific result is valid only if the expected invariant/difference is observed and the two-run reproducibility check passes.

## 13. Falsification / failure criteria

The `R*` operationalization is rejected or execution is blocked if any of the following occurs:

1. Candidate selection depends on row order or nondeterministic database behavior.
2. A future target version passes the temporal cutoff.
3. An unsupported constraint is silently resolved.
4. Missing resolver input is silently substituted from live/current state.
5. The same frozen input produces non-identical canonical output across repeated runs.
6. The implementation cannot distinguish an empty candidate set from an execution error.
7. A counterfactual known to alter the frozen candidate structure produces no corresponding structural change.
8. The implementation requires information declared unavailable by this specification.

## 14. Claims permitted after a successful execution

A successful EXT-1.1 result may support claims about the behaviour of the explicitly defined `R*` accessibility structure and its changes over the observed historical sequence.

It may be used to test whether changes in this reconstructed accessibility structure exhibit the TGCV-predicted relation to subsequent reachability/trajectory variables under the registered analysis.

It may **not**, by itself, establish:

- historical equivalence to Cargo's production resolver;
- causal effects of dependency resolution in the broader Rust ecosystem;
- universality of the TGCV mechanism across domains;
- novelty of TGCV relative to the literature.

## 15. Freeze decision

**Decision: FREEZE `R*` v0.2 for EXT-1.1 execution.**

The prior identifiability audit is recorded as **CONDITIONAL PASS / IDENTIFIABILITY BOUNDARY**. This freeze resolves the boundary operationally: the experiment proceeds only as a restricted, explicitly specified and reproducible accessibility reconstruction.

No scientific execution may silently broaden `R*` beyond this document. Any substantive change requires a new specification version and a new pre-execution decision.

## 16. Next gate

The next step after this freeze is implementation-level conformance checking of the resolver harness against this specification, followed by the registered A/B/C and double-run protocol. The scientific experiment itself remains **NOT EXECUTED** until that conformance gate passes.
