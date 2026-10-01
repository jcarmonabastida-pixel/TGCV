# TGCV — Definition and Architectural Meaning of Ω_T,t

**Status:** GOVERNANCE RECORD — CONCEPTUAL DEFINITION / NO SCIENTIFIC EXECUTION  
**Date:** 2026-10-01  
**Scope:** Consolidation of the conversation defining the candidate Ω-primary object for Transformational Space Dynamics.

## 1. Canonical candidate object

The candidate primary structural object is:

`Ω_T,t = (U_t, ≡_T, R_t)`

It is intended to represent the **structural transformation space at time t**, before applying the current system conditions that determine which transformations are accessible.

The object is not synonymous with `T_acc`, Reach, or `ΔReach`.

## 2. U_t — candidate transformation universe

`U_t` is the set of identifiable candidate transformations that exist as structural possibilities at time `t`:

`U_t = {τ_1, τ_2, …, τ_n}`

Membership in `U_t` does **not** mean that the transformation is currently executable or accessible.

For the current Rust candidate route, a proposed transformation representation is:

`τ = (origin_version_id, target_package_id, target_version_id)`

with candidate membership determined by a pre-outcome temporal registry boundary. Accessibility is applied later.

Thus:

- component = Rust package/crate `p`;
- `package@version` = observational state/unit;
- transformation = a change/substitution involving an identified target release;
- candidate existence is established independently of current accessibility.

## 3. ≡_T — transformation identity/equivalence

`≡_T` specifies when two observational representations correspond to the same transformation for the architectural question.

`τ_a ≡_T τ_b`

means that the two representations are treated as the same transformation under a frozen equivalence rule.

This prevents the transformation universe from being merely a collection of syntactic records.

The identity tuple proposed for Rust is sufficient for observational uniqueness, but it does **not** by itself establish semantic equivalence. The semantic equivalence relation remains open and must be frozen independently rather than introduced through an unfrozen heuristic.

## 4. R_t — structural relations among transformations

`R_t` describes the observable structural relations between transformations.

Conceptually it may contain typed relations such as dependency, compatibility, conflict, composition, or precedence, but no particular vocabulary is yet canonical.

A relation may be represented schematically as:

`r = (τ_i, τ_j, relation_type, provenance)`

The Rust dependency declaration provides a candidate observable structural relation, but it must not automatically be promoted to the complete Ω-primary relation set.

Directionality, relation vocabulary and provenance must be frozen.

## 5. Why the three components belong together

The three components answer different questions:

| Component | Question |
|---|---|
| `U_t` | What transformations are identifiable as candidate transformations? |
| `≡_T` | When do two observations represent the same transformation? |
| `R_t` | How are those transformations structurally related? |

Therefore `Ω_T,t` is intended to be a structural object, not merely a list of currently executable actions.

## 6. Relationship to accessibility

The architectural distinction is:

`Ω_T,t → T_acc,t`

with accessibility represented as a derived layer:

`T_acc,t = F(Ω_T,t, S_t, C_t, L_t)`

where `S_t` is system state, `C_t` context/conditions, and `L_t` restrictions/resources or other admissibility constraints.

A transformation can belong to `U_t` while not belonging to `T_acc,t`.

Example:

`U_t = {τ_1, τ_2, τ_3, τ_4}`

while under the current conditions:

`T_acc,t = {τ_1, τ_3}`

Then `τ_2` and `τ_4` remain part of the transformation space even though they are not currently accessible.

## 7. Relationship to Reach and ΔReach

Under the inherited architecture, Reach was schematically:

`Reach(S_t,C_t,L_t) = {τ ∈ T | τ is reachable from S_t under (C_t,L_t)}`

and the basic new-reachable set was:

`ΔReach_t = Reach_{t+1} \ Reach_t`

For a full change decomposition:

`ΔReach_t^+ = Reach_{t+1} \ Reach_t`

`ΔReach_t^- = Reach_t \ Reach_{t+1}`

`ΔReach_t = (ΔReach_t^+, ΔReach_t^-)`

These definitions are retained as historical/derived concepts, but they do not define the new Ω-primary object.

Under the candidate new architecture, Reach is better understood as an operation over the transformation space:

`Reach_t = Reach(Ω_T,t, S_t, C_t, L_t)`

or equivalently as a derived accessibility function of Ω and current conditions.

Therefore Reach and ΔReach do not replace Ω_T,t and should not be used to redefine the primary architecture.

## 8. Architectural significance

The distinction permits longitudinal analysis of the transformation space itself:

`Ω_T,t → Ω_T,t+1`

Potential changes include:

- appearance or disappearance of candidate transformations;
- changes in transformation identity/equivalence classes;
- changes in structural relations `R_t`;
- reconfiguration of dependencies or other relation structure;
- changes in the resulting accessibility under fixed or changing system conditions.

This is the conceptual basis for the proposed direction **Transformational Space Dynamics**.

The architectural hypothesis is therefore not simply that `T_acc` changes. It is that the **structure from which accessibility is derived may itself have dynamics**.

## 9. Scientific status and boundary

This definition is a candidate architectural formulation, not an established empirical result.

The unresolved scientific questions are:

1. whether `U_t` can be observed and identified independently of accessibility;
2. whether `≡_T` can be frozen without circular semantic relabelling;
3. whether `R_t` can be observed as a structural relation rather than reconstructed from downstream outcomes;
4. whether longitudinal correspondence of Ω objects can be defined independently;
5. whether Ω contains information that is not reducible to `S_t, T_acc,t, C_t, L_t`.

Accordingly, this record does **not** authorize scientific execution and does not by itself justify changing the TGCV Core, Evidence→Claim Matrix v1.44, or RMA v3.37.

## 10. Current Rust gate

The preceding Rust Ω-primary semantic instantiability review concluded:

- `U_t`: conditionally instantiable;
- observational transformation identity: pass for uniqueness;
- `≡_T`: not frozen;
- `R_t`: candidate available, schema open;
- longitudinal correspondence: conditional;
- outcome-independent construction: possible in principle;
- Ω-primary empirical freeze: not admitted.

The next controlled gate is:

`RUST_OMEGA_PRIMARY_TRANSFORMATION_EQUIVALENCE_AND_RELATION_SCHEMA_REVIEW`

Its purpose is to freeze `≡_T`, typed `R_t`, and longitudinal correspondence together, then test their independence from accessibility and outcomes.

## 11. Architectural rule

The governing distinction captured by this record is:

> **`T_acc` describes what is accessible under current conditions; `Ω_T,t` is the candidate structural space of transformations from which accessibility is derived.**

The old chain

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

is therefore **not** the defining architecture for the new Transformational Space Dynamics direction.

No claim is made here that Ω-primary has yet been empirically established.
