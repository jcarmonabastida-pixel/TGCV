# DR-020 — Rust transformation candidate universe T

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision question

Define the concrete candidate universe `T` for EXT-1.1 in a way that is observable, pre-outcome, temporally reproducible and independent of the later accessibility predicate `T_acc`.

## Proposed decision

For each observational unit `v_o = package@version`, every observable dependency relation

`e = (v_o, p_d, q)`

induces a candidate family of alternative target releases of the referenced target package `p_d`.

The candidate universe associated with that edge is:

`T(e) = { τ(v_o,p_d,v_d) | v_d is a release of p_d and created_at(v_d) <= created_at(v_o) }`.

The complete candidate universe for an origin release is the union of these edge-specific candidate sets over the dependency relations observable for that release.

A candidate transformation is therefore the substitution of the target dependency release from the observed origin package-release context to one identifiable target release of the same referenced package, subject only to the temporal observation boundary.

## Candidate identity

A candidate `τ` is canonically identified by the tuple:

`(origin_version_id, target_package_id, target_version_id)`.

The original dependency constraint `q` is retained as provenance but is **not** part of candidate-universe membership. It is applied later by the frozen accessibility/resolution operator.

The candidate universe therefore distinguishes:

- **candidate existence:** whether a target release is a member of `T`;
- **candidate accessibility:** whether that candidate satisfies the frozen `R*` and other accessibility conditions.

This separation is mandatory to avoid defining `T` circularly through `T_acc`.

## Temporal rule

Only target releases with:

`created_at(target_version) <= created_at(origin_version)`

may belong to `T`.

No future release may enter the candidate universe. This rule is inherited from the frozen historical-context boundary in `R*` and is applied here as a leakage-control condition on candidate construction.

## Observable inputs

Construction of `T` may use only:

- `package_versions(id, package_id, version_str, created_at)`;
- `packages(id, name, ...)`;
- `package_dependencies(depending_version, depending_on_package, semver_str)`.

No downloads, stars, forks, downstream adoption, future trajectory, outcome, or post-release information may determine membership in `T`.

## What this decision does not define

This decision does **not** determine:

- whether a candidate is accessible;
- whether its constraint `q` is supported;
- which candidate `R*` selects;
- resource availability or thresholds;
- baseline `B`;
- outcome or horizon;
- sampling or exclusions beyond structural non-reconstructibility;
- the exact implementation parameters still open under DR-009.

In particular, a candidate can belong to `T` and nevertheless be inaccessible or excluded by `R*`.

## Non-circularity requirement

Membership in `T` must be decidable without computing `T_acc`, outcome, baseline `B`, downstream adoption, or any future state. The construction must therefore be implementable as a pure function of the frozen pre-outcome snapshot and the temporal cutoff.

## Structural rationale

This formulation makes `T` a universe of **possible target-release substitutions exposed by observed dependency relations**, while leaving feasibility to the subsequent accessibility layer. It preserves the TGCV distinction:

`T_acc ⊆ T`

without identifying the two sets.

It also preserves the distinction between the analytical component (Rust package) and the observational unit (`package@version`) established by DR-007/DR-019.

## Falsification / audit criteria

The proposal must be rejected or revised if implementation demonstrates any of the following:

1. candidate membership requires post-cutoff information;
2. candidate membership requires evaluating `q` or `R*`;
3. candidate identity is non-unique after canonicalization;
4. a future target release enters `T`;
5. candidate construction depends on row order or nondeterministic input ordering;
6. candidate construction cannot be reproduced from the frozen dataset alone;
7. candidate construction conflates target-package identity with target-version identity;
8. the resulting universe cannot be cleanly separated from the later accessibility predicate.

## Required audit before acceptance

Before this decision can become **ACCEPTED**, a structural audit should verify at minimum:

- canonical candidate-key uniqueness;
- valid origin and target foreign keys;
- target package consistency;
- temporal cutoff compliance;
- independence from `q` and `R*` during candidate generation;
- deterministic canonical ordering;
- reproducibility on repeated execution;
- explicit accounting of empty candidate sets and excluded structural records.

The audit must not execute the confirmatory experiment.

## Authorization consequence

This is a proposal only. It authorizes **no confirmatory execution** and does not freeze `T_acc`, `B`, `R`, sampling, resources or outcome.

## Provenance

This is a **NEW DECISION for EXT-1.1** and is not asserted as historical MVE/EMP-1.1 methodology.

## Dependencies

- DR-007 — Rust observational unit.
- DR-008 — observational-unit governance and temporal freeze requirements.
- DR-009 — dependency-resolution policy.
- DR-017 — normative `R*` boundary.
- DR-019 — Rust component identity and domain.
- `EXT-1.1_RESOLVER_SPEC_R_v0.2.md` — frozen accessibility/resolution specification.
