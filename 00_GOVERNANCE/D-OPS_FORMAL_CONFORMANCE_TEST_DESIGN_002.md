# TGCV — Transformational Dynamics Formal Conformance Test Design 002

**Status:** DESIGN DRAFT — NOT EXECUTED
**Date:** 2026-10-01
**Supersedes for development:** Design 001
**Purpose:** resolve Audit 001 and produce a freeze-ready formal conformance specification.

## 1. Test boundary

This is formal/conformance validation only. It does not validate Transformational Dynamics empirically and does not modify Core, RMA, Matrix, or claim status.

The primary object is Ω_T,t=(U_t,≡_t,R_t). No outcome, reward, utility, planner success, or realized trajectory is used to construct it.

## 2. Frozen formal domain

Use one finite deterministic grounded planning fixture D0.

The freeze package MUST contain: domain source; problem source; canonicalization implementation; relation-construction implementation; perturbation manifest; independent oracle; executor/version manifest; expected-result manifest; schema and serialization specification.

All files receive SHA-256 hashes before execution.

## 3. Canonical transformation identity

A transformation is a grounded action instance represented as τ = (action_name, ordered_typed_parameters).

Canonicalization rules:
1. action name is case-sensitive canonical text;
2. parameters follow the domain declaration order;
3. each parameter is represented by canonical object ID plus declared type;
4. duplicate equivalent parameter tuples are collapsed;
5. predicate names and object IDs use canonical lexical identifiers;
6. conjunction ordering is normalized;
7. duplicate literals are removed;
8. add/delete effect sets are normalized separately;
9. logically equivalent but syntactically different formulas are NOT assumed equivalent unless the frozen normalizer explicitly proves equivalence.

Equivalence ≡ is byte-equivalence of the canonical tuple after normalization, except for a separately declared symbol-renaming correspondence κ.

## 4. Typed relation signature

R contains exactly three relation families:

### R1 — precondition_support
`τ → literal`
Directed, unweighted, set-valued. A relation exists iff the literal is a canonical precondition literal of τ.

### R2 — effect_production
`τ → literal`
Directed, typed by ADD or DELETE. A relation exists iff the literal occurs in the corresponding normalized effect set.

### R3 — action_interaction
`τ → τ`
Directed, unweighted. A relation exists iff the frozen interaction predicate I(τ_i,τ_j)=1, where an ADD or DELETE effect of τ_i unifies with a precondition literal of τ_j. Unification is syntactic over canonical predicate/argument structure; no observed execution is consulted.

Relation equality is exact equality of canonical endpoint identities plus relation type/direction and, for R2, effect subtype.

## 5. Structural perturbation manifest

Four frozen fixtures are generated from D0:
- PERSISTENCE: byte-identical canonical structure.
- EXPANSION: add exactly one new grounded action identity τ+ and its deterministically induced R1/R2/R3 relations.
- CONTRACTION: remove exactly one existing grounded action identity τ− and all incident relations.
- RECONFIGURATION: preserve U and ≡ exactly; alter exactly one declared R3 interaction relation while keeping induced R1/R2 sets unchanged.

The oracle compares identity and relation layers separately. A descriptor is compositional: identity expansion/contraction is reported separately from relation expansion/contraction; reconfiguration is reported only when identity correspondence is unchanged and at least one relation differs.

## 6. Representation perturbation class

Admissible transformations: bijective symbol renaming with frozen κ; declaration reordering; conjunction/literal ordering normalization; whitespace/comments changes.

No transformation may alter canonical semantic content.

The expected descriptor must be invariant under every declared perturbation.

## 7. Structural null

Null fixtures preserve canonical Ω_T exactly while changing object names under κ, declaration order, initial state values, irrelevant state variables, or execution/planner ordering.

State variables do not enter R1/R2/R3 construction. Therefore H0 is testable directly as equality of canonical Ω_T, without assuming it from outcomes.

## 8. State-reducibility test

Define C_S before execution as all state-only views containing initial-state predicate set, typed object inventory, and declared state-variable values.

C_S cannot contain action identities, action preconditions/effects, relation graphs, goals, plan success, or future states.

The oracle checks whether any C_S representation alone yields the same structural-change descriptor under the frozen descriptor algorithm. If yes, the result is STATE-REDUCIBLE.

## 9. Conditional reorganization

Conditions c0/c1 are metadata labels external to transformation identity.

H0: c0 and c1 have identical canonical Ω_T and may differ only in state values.
H1: c0 and c1 share U and ≡ but have a pre-specified difference in R3 under the same relation signature.

The condition-indexed structural operator is F(c)=canonical Ω_T,c. Conditional reorganization is detected iff F(c0) ≠ F(c1) while U and ≡ remain comparable.

## 10. Independent oracle

The oracle is a separate deterministic implementation that consumes only the frozen perturbation manifest, canonicalized fixtures, and frozen comparison rules.

It must not import descriptor labels from the system under test.

The oracle outputs expected identity/relation diffs and expected descriptors.

## 11. Result schema

Each test result is a JSON object containing: test_id; fixture_id; input_hashes; oracle_version; sut_version; comparison_status; identity_diff; relation_diff; descriptor; state_reducibility; representation_invariance; pass; failure_reason.

Results are serialized with UTF-8, LF line endings, sorted object keys, and no insignificant whitespace. The SHA-256 is computed over the exact serialized bytes.

## 12. Freeze package and execution protocol

Before execution: create immutable fixture package; generate SHA-256 manifest; freeze oracle and SUT versions; perform clean-room preflight; verify expected-result manifest against oracle output; execute exactly once under the frozen environment; store raw machine-readable results; independently recompute result hash; run an audit against the frozen manifest.

Any hash mismatch or schema violation invalidates the execution.

## 13. Expected test matrix

| Test | Expected |
|---|---|
| canonical identity normalization | PASS |
| persistence | PERSISTENCE |
| expansion | identity/relation expansion |
| contraction | identity/relation contraction |
| reconfiguration | relation reconfiguration only |
| representation perturbations | invariant |
| structural null | PERSISTENCE |
| state-only variation | no Ω_T change |
| structural change at fixed state | detected |
| incomparable semantics | NON-COMPARABLE |
| conditional H0 | no reorganization |
| conditional H1 | conditional reorganization |

## 14. Execution authorization

**NOT AUTHORIZED.**

Execution requires a subsequent freeze gate confirming all hashes are frozen, oracle/SUT independence is verified, the fixture manifest is immutable, the expected-result manifest is complete, and clean-room preflight passes.

## 15. Decision

**DESIGN 002 — READY FOR FREEZE-READINESS AUDIT.**

No scientific claim or canonical architecture status changes.