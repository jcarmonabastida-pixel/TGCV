# TGCV — Ω_T New Primitive Bridge Design Review v0.1

**Status:** CLOSED — DESIGN SPECIFICATION / NO SOURCE ADMITTED
**Date:** 2026-10-01
**Gate:** NEW_PRIMITIVE_BRIDGE_DESIGN_REVIEW

## 1. Purpose

Define the minimum observable primitive record required to instantiate the frozen Ω_T boundary while constructing the matched inherited A representation from the same observation boundary.

This review does not select a domain, authorize data collection, design a scientific experiment, revise the Core, or revise the Evidence→Claim Matrix.

## 2. Minimum primitive record

Let each observation event be:

`p = (id_s, t0, t1, x_s, op, x_t, type_fields, relation_fields, provenance)`

where:

- `id_s` is the stable identity of the source configuration/object;
- `t0,t1` define the observation interval;
- `x_s` is the observed source configuration relevant to the transformation;
- `op` is the observed operation/change, recorded independently of outcome;
- `x_t` is the observed target configuration;
- `type_fields` are ex-ante fields defining transformation type;
- `relation_fields` are primitive fields from which frozen structural relations can be computed;
- `provenance` records immutable source/version/event evidence and temporal lineage.

These fields are admissible only if observable independently of outcome, value, reward or future-trajectory information.

## 3. Derived Ω_T object

From the same P, a frozen transformation-instance constructor produces:

`u = (id(u), source, op, target, type_fields, [t0,t1], provenance)`

Then:

`U_[t,t+1] = {u}`

`≡_T` is computed only from the frozen `type_fields` signature.

`R_[t,t+1]` is computed only from `relation_fields` and the frozen relation vocabulary.

`π_[t,t+1]` is computed only from immutable provenance and continuity fields.

No component may inspect `T_acc`, outcome, reward, value, future trajectory, or target success.

## 4. Matched A construction

The same primitive record must independently support:

`P → S_t`
`P → T_acc,t`

with `T_acc,t` determined by the already governed accessibility/admissibility rules.

No additional B-only observations are admissible.

## 5. Required relation vocabulary

Before source admission, the source-specific rule must freeze a finite relation vocabulary. At minimum, where applicable:

- dependency / prerequisite;
- compatibility / incompatibility;
- continuation;
- replacement;
- split;
- merge;
- emergence;
- disappearance.

Not every source must instantiate every relation type. The source-specific audit must state which types are observable and how missing/unknown cases are represented.

## 6. A-reconstruction test

The candidate must pass the existing reconstruction sequence:

1. direct encoding in A;
2. deterministic derivation from A_Core;
3. derivation through admissible auxiliary mechanisms;
4. only then, non-reconstructibility.

If Ω_T is deterministically recoverable from A under the frozen rules, the representation is A-EQUIVALENT.

## 7. Longitudinal requirement

At least two adjacent intervals with immutable provenance are required for any empirical statement about structural dynamics.

Single snapshots can establish candidate transformation identity, but cannot establish persistence, emergence, disappearance, replacement, split, merge or structural change.

## 8. Admission test

A source can receive Ω_T BOUNDARY-PASS only if the source-specific audit demonstrates:

- observable operation and source/target states;
- frozen type fields sufficient for `≡_T`;
- primitive relation fields sufficient for `R`;
- provenance sufficient for `π`;
- longitudinal identity across adjacent intervals;
- common P for A and Ω_T;
- outcome-independent construction;
- A-reconstruction failure.

BOUNDARY-PASS remains eligibility only. It is not evidence for B.

## 9. Design consequence

The existing evidence base does not currently satisfy this bridge. Therefore the next legitimate operation is a source-neutral primitive feasibility audit against this minimum tuple.

That audit must answer:

> Does any already available or independently accessible source expose the required primitive tuple without introducing B-specific privileged observations?

If no source passes, the Ω_T candidate remains a formal architectural hypothesis rather than an empirically instantiable object.

## 10. Governance consequence

- Core: unchanged.
- Evidence→Claim Matrix v1.44: unchanged.
- RMA v3.37: unchanged.
- Ω_T boundary v0.2: unchanged.
- No source admitted.
- No experiment designed.
- No scientific execution authorized.

**Next gate: `OMEGA_T_PRIMITIVE_FEASIBILITY_AUDIT`.**
