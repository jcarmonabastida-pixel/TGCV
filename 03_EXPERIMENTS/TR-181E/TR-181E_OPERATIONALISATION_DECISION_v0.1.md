# TR-181E — Operationalisation Decision v0.1

**Status:** DECISION RECORD — DESIGN GATE
**Date:** 2026-08-27

## Decision

The six historical EMP-1.1 transformation families are **not** promoted into TR-181E as if they were derivable from the TGCV Core. Their exact predicates were not recovered.

TR-181E will therefore use a **Core-derived minimal transformation schema**. The schema is defined at the level of transformation preconditions and effects, with a finite candidate universe frozen independently of EMP-1.1 outcomes.

## Minimal schema

A candidate transformation is represented as:

`τ = (pre, effect, target)`

A transformation is accessible at snapshot `(S,C,L)` iff its precondition is satisfied by the snapshot and its required target/resources are available under the frozen schema:

`Pτ(S,C,L)=1`.

`T_acc(S) = {τ ∈ T : Pτ(S,C,L)=1}`.

The schema is deliberately agnostic about whether the mechanism producing a transformation is interaction, learning, reconfiguration, acquisition, or another process. Mechanism is not made primitive by the representation.

## Required empirical safeguards

The candidate universe `T` must be finite, explicit, and generated without reference to outcomes. Each candidate must have a deterministic predicate. The resulting R must be computed solely from the pre-outcome snapshot.

## Representation

The primary R representation will encode:

1. number of accessible transformations;
2. counts by pre-declared transformation type;
3. distribution/diversity across types;
4. incidence of accessible transformations over components/resources, using only the frozen transformation schema.

The exact feature vector, ordering and normalisation remain to be frozen in the executable protocol.

## Why this is not EMP-1.1 replication

Because the historical family predicates and exact feature encoding are unavailable, this schema is a **new operationalisation**. Any TR-181E result therefore bears on the stability of the TGCV phenomenon under an independently specified representation; it does not retroactively reproduce EMP-1.1.

## Falsification protection

The operationalisation must be frozen before test-set generation/evaluation. If more than one Core-consistent schema survives theoretical review, the selection criterion must be specified before data inspection, or all admissible variants must be evaluated as a pre-declared sensitivity family.

## Gate

**R operationalisation:** CONCEPTUALLY SELECTED

**Exact executable schema:** NOT YET FROZEN

**Test execution:** PROHIBITED

**Next:** formalise the finite candidate universe and deterministic predicates, then run leakage/unit tests before pre-registration freeze.
