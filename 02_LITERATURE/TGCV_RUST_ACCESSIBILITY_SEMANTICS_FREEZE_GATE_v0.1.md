# TGCV — Rust Accessibility Semantics Freeze Gate v0.1

**Status:** PASS — SEMANTIC CONTRACT FROZEN FOR STRUCTURAL VALIDATION  
**Date:** 2026-09-07  
**Phase:** Rust domain instantiation

## 1. Purpose

Freeze, ex ante and outcome-blind, the semantics by which a candidate Rust dependency transformation is classified as accessible at an origin package-version and how changes in accessible transformation membership are compared over time.

This Gate authorizes a subsequent paired structural audit. It does not authorize outcome selection, predictive modelling, or value analysis.

## 2. Locked TGCV architecture

`Core_ontological = S`

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

`I` remains explanatory, not primitive.

## 3. Rust transformation semantics

The candidate transformation is a dependency transition:

`τ = (e_o, p_d, v_d)`

where:

- `e_o` is the focal origin package-version;
- `p_d` is a dependency package;
- `v_d` is a concrete released version of `p_d`.

The transformation is interpreted as the admissible dependency relation from `e_o` to `v_d`, not as an observed execution event.

Identity is canonical and independent of accessibility:

`τ_id = (origin_version_id, target_package_id, target_version_id)`.

## 4. Independent candidate universe

`U_τ(e_o) = {τ(e_o,p_d,v_d) | v_d is a released version of p_d and created_at(v_d) <= created_at(e_o)}`.

The temporal rule is deliberately strict: a target release must exist no later than the origin observation time.

Candidate construction is independent of the accessibility predicate and uses no post-origin outcome.

The prior DR-020 construction provides technical precedent for this independent candidate-universe pattern, but this Gate freezes the rule as the Rust TGCV contract rather than inheriting DR-020's entire protocol.

## 5. Dependency requirement grammar

For the initial Rust instantiation, the declared dependency requirement associated with `e_o → p_d` is parsed using the frozen R* SemVer contract already established for the Rust empirical environment.

Accepted requirement forms are:

- exact `=X.Y.Z`;
- caret `^X.Y`;
- caret `^X.Y.Z`;
- bare `X.Y.Z`, interpreted as caret-compatible according to the frozen R* contract.

Unsupported requirement forms are not coerced into accessibility. They enter the unresolved/unsupported category and are reported separately.

## 6. Admissibility / accessibility predicate

For a candidate `τ=(e_o,p_d,v_d)`:

`P_τ(e_o,t)=1`

iff all of the following hold:

1. `v_d` is a canonical released version of `p_d`;
2. `created_at(v_d) <= t`, with the origin observation boundary fixed by the candidate universe;
3. the dependency declaration for `e_o` targeting `p_d` is present and parsable under R*;
4. `v_d` satisfies the frozen R* requirement semantics for that declaration;
5. no frozen exclusion rule marks `v_d` inadmissible.

Accessibility therefore means **present-time admissibility under the frozen dependency requirement semantics**, not subsequent observed selection or use.

## 7. Explicit exclusions

The following do **not** enter `P_τ`:

- whether the target version was actually selected by a later resolver execution;
- whether the focal package subsequently released;
- subsequent download/use/activity;
- the primary or secondary outcome;
- any model prediction;
- any value evaluation;
- information first appearing after the origin observation boundary.

## 8. Yanked, deleted and unresolved versions

A candidate whose identity or release metadata cannot be resolved is **unresolved**, not inaccessible.

A version excluded by an explicit frozen admissibility rule is **inaccessible**.

A version whose later ecosystem status changes after the origin observation does not retroactively alter the historical accessibility classification unless that status was already part of the frozen origin-time information boundary.

No unresolved candidate may be silently converted to `P_τ=0`.

## 9. `T_acc` representation

The primary representation is the membership relation:

`T_acc,t = {(e_o,τ_id) | P_τ(e_o,t)=1}`.

For each focal origin:

`T_acc,t(e_o) = {τ_id | P_τ(e_o,t)=1}`.

Cardinality is a derived diagnostic only:

`A_count(e_o,t)=|T_acc,t(e_o)|`.

The relational membership representation is primary because `ΔT_acc` requires identifying additions and removals, not merely a change in count.

## 10. Temporal observation pairing

The structural validation unit consists of an origin observation at `t` and a subsequent defined observation point `t+1` for the same analytical unit.

The pairing rule must preserve:

- identical focal-unit identity;
- identical transformation identity semantics;
- identical R* grammar;
- identical admissibility rules;
- identical canonicalization;
- a pre-specified temporal boundary.

No pairing may be selected because it maximizes a later outcome difference.

## 11. `ΔT_acc` operator

The comparison is performed on membership sets:

`Add_t = T_acc,t+1 \ T_acc,t`

`Rem_t = T_acc,t \ T_acc,t+1`

and:

- persistence iff `Add_t=∅` and `Rem_t=∅`;
- expansion iff `Add_t≠∅` and `Rem_t=∅`;
- contraction iff `Add_t=∅` and `Rem_t≠∅`;
- reconfiguration/substitution iff `Add_t≠∅` and `Rem_t≠∅`.

`ΔT_acc ≠ 0` iff either `Add_t` or `Rem_t` is non-empty.

The operator is structural and does not depend on outcome, execution, or value.

## 12. Accessibility versus execution

The frozen sequence is:

`τ exists → P_τ=1 → selection/execution may or may not occur → result may or may not occur`.

Observed post-origin dependency use cannot define present accessibility.

Where the data permit the distinction, accessible-but-unexecuted candidates must remain identifiable.

## 13. Empty sets

`T_acc,t(e_o)=∅` is a valid structural observation.

Empty sets must be retained and participate in temporal comparison. A transition from empty to non-empty is expansion; non-empty to empty is contraction.

## 14. Canonicalization and determinism

The structural representation must be canonicalized by:

1. canonical origin identifier;
2. canonical target package identifier;
3. canonical target version identifier;
4. deterministic ordering of membership records.

Equivalent input row permutations must yield identical canonical `T_acc` and `ΔT_acc` outputs.

## 15. Leakage firewall

The following information is prohibited from semantic construction:

`future release data beyond the frozen candidate rule`,
`post-origin execution/selection`,
`outcome`,
`value`,
`model predictions`,
`model-derived feature importance`.

Any audit implementation that accesses such information before accessibility classification fails the structural gate.

## 16. Relationship to EXT-1.1

The following are explicitly **not inherited as semantic definitions**:

- EXT-1.1 outcome `subsequent_release_activity`;
- EXT-1.1 predictive model;
- EXT-1.1 feature encoding;
- EXT-1.1 predictive hypothesis;
- EXT-1.1 temporal evaluation window.

Generic parsing, indexing and integrity infrastructure may be reused when separately documented.

## 17. Structural falsifiers

**SF-1:** R* cannot define admissibility deterministically for the accepted candidate class.

**SF-2:** `P_τ` requires post-origin information.

**SF-3:** candidate existence and accessibility cannot be separated.

**SF-4:** unresolved cases cannot be distinguished from inaccessible cases.

**SF-5:** membership-level `T_acc` cannot be reconstructed.

**SF-6:** paired temporal `T_acc` cannot be reconstructed under identical semantics.

**SF-7:** `ΔT_acc` cannot be calculated from membership changes.

**SF-8:** execution is required to establish accessibility.

**SF-9:** deterministic canonicalization fails.

**SF-10:** semantic construction depends on outcome/model/value information.

## 18. Gate criteria

| Criterion | Result |
|---|---|
| ASF-G1 | Transformation identity frozen — PASS |
| ASF-G2 | Independent candidate universe frozen — PASS |
| ASF-G3 | Requirement grammar frozen — PASS |
| ASF-G4 | Accessibility semantics frozen — PASS |
| ASF-G5 | Temporal boundary rule frozen — PASS |
| ASF-G6 | Unresolved/excluded treatment frozen — PASS |
| ASF-G7 | Membership-level T_acc frozen — PASS |
| ASF-G8 | ΔT_acc operator frozen — PASS |
| ASF-G9 | Empty-set semantics frozen — PASS |
| ASF-G10 | Execution/outcome/value firewall frozen — PASS |
| ASF-G11 | EXT-1.1 inheritance firewall preserved — PASS |
| ASF-G12 | Structural implementation audit executed — NOT YET |

## 19. Gate decision

**PASS — SEMANTIC CONTRACT FROZEN FOR STRUCTURAL VALIDATION.**

The Rust accessibility semantics are now fixed ex ante. The next audit may test whether these rules can actually be executed reproducibly over the available Rust data. It may not alter the rules in response to observed results.

## 20. Immediate next controlled operation

**TGCV Rust Paired Temporal T_acc / ΔT_acc Structural Audit v0.1**.

This audit must execute the frozen contract at two temporal points, reconstruct membership-level `T_acc`, compute `Add`, `Rem` and `ΔT_acc`, and report empty/unresolved coverage.

It remains outcome-blind and model-blind.

## 21. Integrity lock

No outcome, predictive model, value criterion, feature selection or hypothesis may be chosen or modified from this Gate. Any semantic change after this point requires a new ex-ante versioned Gate.
