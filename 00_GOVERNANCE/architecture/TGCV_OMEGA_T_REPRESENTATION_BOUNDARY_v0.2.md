# TGCV — Ω_T Representation Boundary Specification v0.2

**Status:** GOVERNANCE SPECIFICATION — FROZEN FOR SOURCE-ADMISSIBILITY REVIEW / NO EXPERIMENT AUTHORIZATION
**Date:** 2026-10-01
**Supersedes:** candidate v0.1 as the active boundary specification

## 1. Purpose

Freeze the representation boundary used to determine whether an empirical source can instantiate the TSDI candidate object without collapsing it into the inherited A representation.

This specification does not select a source, design an experiment, authorize execution, or revise the Core/Matrix/RMA.

## 2. Candidate object

`Ω_T = { (U_[t,t+1], ≡_T, R_[t,t+1], π_[t,t+1]) }_t`

`U_[t,t+1]` contains transformation instances evidenced over interval `[t,t+1]`.
`≡_T` is transformation-type equivalence, distinct from instance identity.
`R_[t,t+1]` is a typed structural relation over transformation instances.
`π_[t,t+1]` is the frozen longitudinal provenance/persistence mapping.

## 3. Identity layers

`id(u)` is the exact provenance identity of an observed instance.

`u ≡_T v` is a deterministic, symmetric and transitive equivalence rule based only on frozen transformation identity/type fields.

`π` determines continuation, replacement, split or merge across adjacent intervals using frozen provenance fields. It is not inferred from outcomes or target behaviour.

These three layers must not be collapsed.

## 4. Transformation-instance construction

Each `u ∈ U_[t,t+1]` must be constructed ex ante from primitive observations or an independently recorded transformation event and must include, where observable:

- source configuration/state;
- operation/change;
- target configuration/state;
- transformation type/domain;
- interval and provenance identity.

Success, value, reward, outcome, future trajectory or target prediction cannot define membership in `U`.

## 5. Structural relation

`R_[t,t+1]` uses a finite frozen vocabulary of relation types. Every relation type specifies:

- admissible source and target identity types;
- semantic condition;
- temporal scope;
- directionality where applicable;
- evidence/provenance fields;
- missing-data treatment.

Each edge must be computable from primitive observations and the frozen rule. A statistic or graph reconstructed from `T_acc` is not an independently admissible `R`.

## 6. Longitudinal semantics

Structural change is assessed by comparing adjacent interval objects after applying the frozen `π` mapping.

Identifier renaming or serialization changes must not be mistaken for transformation-space change.

At least two adjacent intervals are required for any empirical claim about dynamics.

## 7. Common observation boundary

Let `P` denote the primitive observations available to the source.

Both architectures must be constructed from the same `P`:

`P → A = (S_t, T_acc,t)`

`P → Ω_T`

B cannot receive additional variables merely because they expose `R` or `π`.

## 8. A-reconstruction gate

Before any architectural discrimination, apply:

1. direct encoding in A;
2. deterministic derivation from `A_Core`;
3. reconstruction through currently admissible auxiliary mechanisms;
4. non-reconstructibility only after 1–3 fail.

If the complete relevant `Ω_T` information is reconstructible from A under the frozen boundary, the candidate is **A-EQUIVALENT**.

## 9. Anti-circularity

Prohibited as definitions of any Ω_T component:

- outcome/value/reward;
- future success or target variables;
- post-hoc relation discovery;
- trajectory selection based on the desired distinction;
- relabelling `T_acc` as `U`;
- graph statistics of `T_acc` presented as independent structural observations.

## 10. Source-admission status

**BOUNDARY-PASS:** all identity, equivalence, relation, provenance, temporal and parity rules are sufficiently frozen for source-specific audit.

**BOUNDARY-BLOCKED:** at least one required rule remains unspecified or operationally ambiguous.

**BOUNDARY-FAIL:** the candidate is necessarily an A-derived representation or uses excluded downstream information.

BOUNDARY-PASS is an eligibility state only. It is not evidence for B, AGAINST-A evidence, experiment authorization, or Core revision.

## 11. Freeze decision

The v0.2 correction resolves the prior defects concerning interval indexing, identity/equivalence separation, and longitudinal relation semantics.

**Ω_T REPRESENTATION BOUNDARY: FROZEN FOR SOURCE-ADMISSIBILITY REVIEW.**

Future changes require a new version and explicit governance review.

**No source selected. No experiment designed. No scientific execution authorized. Core, Evidence→Claim Matrix and RMA unchanged.**
