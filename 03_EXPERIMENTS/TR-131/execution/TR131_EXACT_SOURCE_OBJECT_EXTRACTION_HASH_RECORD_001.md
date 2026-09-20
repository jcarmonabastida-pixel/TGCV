# TGCV — Exact Source Object Extraction and Hash Record 001

**Status:** PASS — SOURCE OBJECTS PINNED FOR CANDIDATE FIXTURE CONSTRUCTION
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Purpose
Pin the exact external source objects used for the two candidate fixtures and record immutable revisions and object hashes before fixture freeze.

## 2. Domain A — Rainbow / SWIM
Primary repository: `cmu-able/rainbow`.
Immutable repository revision: `c053e2aab6d58c233016574887296e2be43ca60f`.

Selected source model: `targets/swim/model/swim.acme`.
GitHub blob SHA: `9989790020ff1b814e0b1aa7bd1f926d980ce823`.

Selected adaptation strategy source: `targets/swim/stitch/swimStrategies.s`.
GitHub blob SHA: `5ac062d6a01c918c018f29e26a9a3bc2943d4885`.

Selected tactic source: `targets/swim/stitch/swimTactics.t.s`.
GitHub blob SHA: `513a5d78e301e9fa4660b8bac9154b93e6a7a605`.

Verified source semantics include:
- `DIMMER_LEVELS = 5`;
- `DIMMER_MARGIN = 0.1`;
- `LB0.dimmer` as an explicit model property;
- strategies `IncDimmer`, `DecDimmer`, `AddServer`, `RemoveServer`;
- tactic-level applicability conditions;
- tactic-level actions/effects.

The exact source files therefore provide a reproducible basis for a finite Rainbow fixture.

## 3. Domain B — VisitAll
Primary formal domain repository: `AI-Planning/pddl-generators`.
Immutable repository revision: `d5c22c9ab21ecaf90db82daf2a0537973c661009`.

Domain artifact: `visitall/domain.pddl`.
GitHub blob SHA: `0e0ce4e845fac76ad9c8c815f9a697e7946784d8`.

Generator artifact: `visitall/grid.c`.
GitHub blob SHA: `5febdf45316e7e61f6d2920901e3f52ae401e03b`.

The generator explicitly defines width/height, unavailable-cell count and random seed parameters and derives adjacency and initial state from the generated grid.

## 4. Exact VisitAll problem instance
For the minimal candidate fixture, use the independently published `grid-1` Visitall instance reproduced in ACTIONREASONINGBENCH Appendix F.2.

Source: Handa et al., ACTIONREASONINGBENCH, arXiv:2406.04046v3, published 2 March 2025; Appendix F.2 identifies `grid-1` as a Visitall instance and gives its PDDL object, initial and goal state.

Exact instance text used for fixture hashing:

```text
(define (problem grid-1)
(:domain grid-visit-all)
(:objects loc-x1-y0 - place )
(:init (at-robot loc-x1-y0)
(visited loc-x1-y0))
(:goal (and (visited loc-x1-y0))))
```

Normalized UTF-8 SHA-256 of the exact text above:
`2bdda52c5f96ffb10f227cee15983cf1f7b0e7a98fef5c4daeac233aca7d0374`.

The published source describes the instance as a trivial one-cell case whose initial and goal conditions coincide. citeturn1search25turn2view0

## 5. Critical limitation of the current VisitAll pin
The `grid-1` instance is intentionally minimal and therefore does **not** satisfy the previously proposed multi-action fixture requirements.

In particular, it has only one location and therefore cannot supply:
- two simultaneously accessible movement transformations;
- a non-trivial trajectory contrast;
- a later accessibility change.

Therefore the exact source pin **passes**, but the scientific fixture construction remains incomplete.

## 6. Consequence
The source-identification blocker is resolved.
The fixture-design blocker is now explicit and narrower:

**VisitAll requires a non-trivial exact instance.**

We must select an existing exact IPC Visitall instance with at least four usable locations and at least two applicable move actions at some state, rather than manufacture one.

## 7. Domain A fixture constraint
The Rainbow source similarly permits exact extraction, but the final fixture must select a concrete pre-realization model state and at least two source-defined applicable strategies/operators without inserting an invented state.

## 8. Governance
No scientific execution is authorized.
No frozen TR-131 artifact is modified.
No Core/RMA/Evidence→Claim Matrix modification is authorized.

## 9. Next gate
**NON-TRIVIAL EXACT INSTANCE SELECTION AND FIXTURE TRACEABILITY AUDIT**

Select an existing exact Visitall IPC instance satisfying the multi-action requirement and an exact Rainbow SWIM model state satisfying the same structural requirement. Then produce the final source-to-fixture traceability record.