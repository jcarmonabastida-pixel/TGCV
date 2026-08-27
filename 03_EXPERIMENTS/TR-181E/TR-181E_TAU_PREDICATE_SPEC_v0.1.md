# TR-181E — Candidate Transformation and Predicate Specification v0.1

**Status:** PRE-FREEZE SPECIFICATION — NOT FROZEN

## 1. Purpose

Define the minimal operational object required to construct the accessible transformation set `T_acc` without using outcome or future trajectory information.

## 2. Candidate transformation

Each candidate transformation `τ` is represented by:

`τ = <id, class, target, eff>`

where:

- `id` uniquely identifies the candidate transformation in the pre-declared universe `T`.
- `class` is a controlled operational label, not asserted to be a primitive of TGCV ontology.
- `target` identifies the system element(s) whose configuration/capability is potentially changed.
- `eff` describes the potential effect as metadata only. It is not executed by the accessibility engine.

## 3. Accessibility predicate

`Pτ(S,C,L) = Preτ(S,C,L) ∧ Targetτ(S,C,L) ∧ Resourceτ(S,C,L)`

A candidate is accessible iff all three components are satisfied.

### 3.1 Preconditions

Preconditions are explicit predicates over the frozen pre-outcome snapshot and declared context. They may inspect only information available at the decision point.

### 3.2 Target condition

The target condition verifies that the transformation's declared target is well-defined and present in the state/context representation required by the candidate. A target is not inferred from outcome or trajectory.

### 3.3 Resource condition

Resource conditions specify explicit thresholds or requirements over declared resources. They are evaluated against the pre-outcome snapshot only.

## 4. Excluded information

The predicate language MUST NOT inspect:

- observed outcome;
- future trajectory;
- post-transformation state;
- empirical success/failure labels;
- variables derived from the test outcome.

## 5. Controlled classes

The current operational candidate universe may use:

`ACTIVATE, COMPOSE, RECONFIGURE, ACQUIRE, LEARN, RECOMBINE`.

These labels are representational categories for candidate construction. They must not be treated as recovered EMP-1.1 transformation families or as axiomatic TGCV ontology.

## 6. Effects

`eff` is retained to make each candidate transformation semantically inspectable, but the TR-181E accessibility engine does not recursively execute effects. Accessibility is evaluated from the frozen pre-outcome state.

## 7. Canonical R boundary

Given the frozen candidate universe `T`:

`T_acc = { τ ∈ T | Pτ(S,C,L) = true }`

The canonical R is:

`R = <T_acc, |T_acc|>`

Implementation may serialize `T_acc` as ordered candidate IDs, provided ordering is canonical and does not alter set semantics.

## 8. Freeze requirements

Before empirical execution, the following must be frozen:

1. candidate universe `T`;
2. class definitions;
3. target semantics;
4. predicate vocabulary;
5. resource thresholds/requirements;
6. effect metadata schema;
7. canonical serialization of `T_acc`;
8. B/R provenance mapping.

No empirical result may be used to alter these definitions after freeze.

## Decision

**Semantic specification:** READY FOR RECONCILIATION

**Freeze:** NO-GO until the final candidate inventory and B/R matrix are jointly reconciled.

**Experiment:** BLOCKED pending freeze.
