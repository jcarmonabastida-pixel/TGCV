# TGCV — Rust Ω-Primary Semantic Instantiability Review v0.1

**Status:** CLOSED — CONDITIONALLY INSTANTIABLE / SEMANTIC FREEZE REQUIRED
**Date:** 2026-10-01
**Gate:** RUST_OMEGA_PRIMARY_SEMANTIC_INSTANTIABILITY_REVIEW

## 1. Question

Can the existing Rust observational records support a legitimate transformation-level `U_t` and `≡_T` without relabelling `package@version` as a transformation and without reverting to the legacy `ΔT_acc → ΔReach → ΔTrajectory` chain?

## 2. Finding

**Conditionally yes.** The existing Rust records contain enough pre-outcome structure to define a candidate transformation universe independently of accessibility.

DR-020 proposes candidate transformations as target-release substitutions exposed by observed dependency relations:

`τ = (origin_version_id, target_package_id, target_version_id)`

with candidate membership determined by the pre-outcome temporal registry boundary, while accessibility is applied later by `R*`.

This is materially different from defining `T` as `T_acc`.

## 3. Semantic distinction

The review confirms that:

- the **component** is the Rust package/crate `p`, not `package@version`;
- `package@version` is the observational state/unit;
- a candidate transformation is a change/substitution involving an identified target release;
- candidate existence can be determined before accessibility;
- accessibility is a separate predicate over candidates;
- no outcome or future trajectory is needed for candidate membership.

Therefore the candidate transformation is not merely a relabelled package version.

## 4. Transformation identity

The proposed identity `(origin_version_id, target_package_id, target_version_id)` is sufficient for observational uniqueness, but it is not yet sufficient for an Ω-primary equivalence relation `≡_T`.

An Ω-primary Rust instantiation must additionally specify when two observationally distinct candidate transformations are semantically equivalent for the architectural question.

For example, equivalence cannot simply be byte/string equality if the intended object is transformation semantics; conversely, semantic equivalence cannot be introduced by an unfrozen heuristic.

Therefore:

`U_t`: CONDITIONALLY INSTANTIABLE.
`≡_T`: NOT YET FROZEN.

## 5. Relation structure

The Rust dependency declaration provides an observable structural relation between the origin observational unit and a target package. After candidate construction, target-release identity is explicit.

This supports a candidate `R_t` over transformation identities, but the exact relation vocabulary and directionality remain to be frozen. The existing dependency relation must not silently be promoted to the complete Ω-primary relation set.

## 6. Longitudinal correspondence

Package identity is stable across releases and release timestamps provide an outcome-independent temporal boundary. This supports longitudinal correspondence of component observations.

However, correspondence of transformation identities across adjacent Ω snapshots requires a separate frozen rule because the origin release is part of the current candidate identity.

Thus longitudinal Ω correspondence is **conditionally available but not yet frozen**.

## 7. Legacy-chain exclusion

The candidate passes the architectural semantic test only if the primary object remains:

`Ω_T,t = (U_t, ≡_t, R_t)`

and accessibility is a derived/secondary layer:

`T_acc,t = F(Ω_T,t, S_t, C_t, L_t)`

RUST-DYN-2's previously rejected independent successor graph is not required to instantiate Ω-primary.

Accordingly, this route does not reinstate `ΔT_acc → ΔReach → ΔTrajectory` as the architectural chain.

## 8. Admissibility status

| Component | Status |
|---|---|
| Observable transformation candidates `U_t` | CONDITIONAL PASS |
| Transformation identity | PASS for observational uniqueness |
| Transformation equivalence `≡_T` | OPEN |
| Structural relations `R_t` | OPEN / candidate available |
| Longitudinal correspondence `κ` | CONDITIONAL |
| Outcome-independent construction | PASS in principle |
| Ω-primary empirical freeze | NOT ADMITTED |

## 9. Decision

Rust is a **legitimate candidate domain for Ω-primary operationalisation**, but the domain is not yet empirically admitted.

No semantic relabelling is required to reach this candidate status, and no legacy downstream chain is reintroduced.

The next controlled operation is therefore not scientific execution. It is to freeze the missing semantic objects:

**`RUST_OMEGA_PRIMARY_TRANSFORMATION_EQUIVALENCE_AND_RELATION_SCHEMA_REVIEW`**

This review must define `≡_T`, the typed `R_t` vocabulary, and the longitudinal correspondence rule together, then test whether those definitions remain independent of accessibility and outcomes.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

**Scientific execution: NOT AUTHORIZED.**
