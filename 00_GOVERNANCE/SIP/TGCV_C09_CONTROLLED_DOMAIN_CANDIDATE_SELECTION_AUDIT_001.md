# TGCV — C09 Controlled Domain Candidate Selection Audit 001

**Status:** `AUDIT PASS — DOMAIN/IDENTIFICATION GATE CLOSED / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_PRE_EXECUTION_DOMAIN_IDENTIFICATION_GATE_001.md`
**Audited package:** `TGCV_C09_CONTROLLED_DOMAIN_PREEXECUTION_PACKAGE_001.md`

## 1. Decision

Select a purpose-designed **finite resource-gated transformation microdomain** as the C09 controlled domain.

The domain is intentionally synthetic and domain-agnostic. It is not an extension of IUT-A-01 and does not reuse any unresolved empirical accessibility classification. The causal variable is defined directly by the experimental system.

`Z → resource availability → T_acc → selected transformation → subsequent state/trajectory`

The first execution shall use `H=1`; no H>1 conclusion is authorized.

## 2. Concrete domain definition

Each unit contains a frozen decision-time state `(S0,C0)` and the same finite candidate universe:

`U = {A,B,C}`

Candidate transformations have fixed transition effects and fixed objective scores. `B` is the only transformation whose execution requires enabling resource `R1`.

The accessibility rule is fixed before treatment:

- `L0(B)=0` when `R1=false`;
- `L1(B)=1` when `R1=true`;
- accessibility of A and C is unchanged by the intervention.

Thus, for the frozen fixture:

`T_acc,0 = {A,C}`

`T_acc,1 = {A,B,C}`

and therefore:

`ΔT_acc ≠ ∅`.

The treatment is the exogenous assignment of `R1=true`; it does not identify, select, execute or encode the transformation that will subsequently occur.

## 3. Trajectory mechanism invariance

The following remain byte-identical/canonically identical between treatment and control:

- transformation definitions;
- state-transition equations;
- objective/scoring rule;
- decision policy over the accessible set;
- execution mechanism;
- observation procedure;
- randomization mechanism after assignment.

Only the predeclared accessibility condition `R1` changes.

The decision policy is therefore explicitly represented as:

`P(S,C,T_acc)`

rather than as a treatment-specific policy. Any treatment-dependent implementation of `P` is a protocol failure.

## 4. Identification

Use randomized assignment of units to `Z=0` or `Z=1` after the pre-treatment fixture is frozen.

Unit of analysis: one independently seeded system replica.

Eligibility and exclusion rules are fixed before execution. Baseline state/context and candidate universe are sealed before assignment. The primary comparison is the difference in the prespecified trajectory endpoint `Y` between randomized treatment and control.

The exact finite domain permits independent reconstruction of the potential trajectories and of `T_acc,0/T_acc,1` from the frozen specification, providing a stronger audit anchor than an observational association.

## 5. Direct-effect exclusion

The intervention is implemented as a change to an accessibility predicate only.

It is inadmissible for the treatment flag to be read by:

- the transition function;
- objective/scoring function;
- decision policy except through `T_acc`;
- trajectory metric;
- observation code.

A static dependency graph and canonical parameter comparison shall verify that the only causal path from `Z` into the trajectory mechanism is through the accessibility calculation.

## 6. Mandatory gate audit

| Criterion | Result | Audit finding |
|---|---|---|
| State/context freeze | PASS | `S0,C0` are fully synthetic, finite and sealable before assignment. |
| Bounded transformation universe | PASS | `U={A,B,C}` is explicit and immutable. |
| Independent `T_acc` reconstruction | PASS | `L` is deterministic and evaluated before any trajectory outcome. |
| Verifiable accessibility intervention | PASS | `T_acc,0={A,C}` and `T_acc,1={A,B,C}` by construction. |
| No direct target encoding | PASS | `Z` carries only resource availability, not transformation identity. |
| Counterfactual | PASS | Randomized assignment plus exact finite potential-world reconstruction. |
| Temporal ordering | PASS | freeze → assignment → accessibility evaluation → trajectory. |
| Confounding | PASS | Synthetic randomization and identical frozen generator eliminate uncontrolled external confounding within scope. |
| Independent reconstruction | PASS | All inputs and transformations are finite, canonicalizable and hashable. |
| Fixed horizon | PASS | Initial execution bounded to `H=1`. |
| Direct-effect exclusion | PASS | Treatment is forbidden outside accessibility calculation. |
| Falsification | PASS | Null intervention, invariant-rule and hash checks are predeclared. |

## 7. Important limitation

This audit establishes **design admissibility**, not scientific causal success.

In particular, the mathematical fact that `T_acc,0 ≠ T_acc,1` is a prerequisite/design validation. The scientific result remains unknown until controlled execution demonstrates whether the accessibility change produces the prespecified trajectory contrast under the frozen protocol.

The result must not be reported as evidence for C09 until execution and independent reconstruction are complete.

## 8. Relationship to existing TGCV evidence

SWIM and FOS remain the principal bounded prior evidence for accessibility/trajectory structure; RUST-DYN-2 remains structural empirical support. This controlled domain is not a replacement or repetition of those results. Its sole purpose is to address the unresolved causal identification gap.

Existing IUT-A-01 accessibility work is not treated as causal evidence for C09. Its documented unresolved accessibility conditions reinforce the requirement that this new domain define `L` natively and explicitly rather than infer it from empirical material.

## 9. Gate disposition

`DOMAIN / IDENTIFICATION GATE = PASS`

`C09 = OPEN — CAUSAL EXECUTION GAP REMAINS`

`EXECUTION AUTHORIZATION = NONE`

`DATASET ACQUISITION = NONE`

`CLAIM UPGRADE = NONE`

The gate is closed only for **domain selection and identification design**. The next stage is construction of the separately frozen C09 execution protocol, followed by its protocol audit. No scientific execution is authorized by this artifact.
