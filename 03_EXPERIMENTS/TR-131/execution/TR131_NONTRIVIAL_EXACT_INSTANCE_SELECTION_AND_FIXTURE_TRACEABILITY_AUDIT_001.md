# TGCV — NON-TRIVIAL EXACT INSTANCE SELECTION AND FIXTURE TRACEABILITY AUDIT 001

**Status:** PASS — EXACT NON-TRIVIAL VISITALL INSTANCE SELECTED; RAINBOW STRUCTURAL STATE IDENTIFIED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20
**Parent canonical commit:** c21bbc466f97361c107d0370fd579bb6c0bada75

## 1. Gate objective

Resolve the remaining fixture-design blocker by selecting an existing exact VisitAll instance satisfying:

|T_acc| >= 2

at an explicitly identifiable state, without manufacturing an instance, and identify a Rainbow/SWIM state at the same structural resolution.

This record is a traceability audit only. It does not authorize scientific execution and does not modify the TGCV Core, RMA, Evidence Matrix, or frozen TR-131 package.

## 2. VisitAll exact source selection

### 2.1 Formal source

Primary formal domain repository:

- Repository: AI-Planning/pddl-generators
- Revision: d5c22c9ab21ecaf90db82daf2a0537973c661009
- Artifact: visitall/domain.pddl
- Blob SHA: 0e0ce4e845fac76ad9c8c815f9a697e7946784d8
- Artifact: visitall/grid.c
- Blob SHA: 5febdf45316e7e61f6d2920901e3f52ae401e03b

The generator exposes grid dimensions, unavailable locations and random seed, and derives connectivity and the initial robot state from the generated grid.

### 2.2 Existing exact benchmark instance

Selected instance:

- Repository: potassco/pddl-instances
- Repository revision: cf19edf7c53d1540ddbb396c642595e0926ee552
- Benchmark family: IPC-2014
- Domain variant: visit-all-sequential-optimal
- Exact path: ipc-2014/domains/visit-all-sequential-optimal/instances/instance-1.pddl
- Blob SHA: f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34
- Problem name: grid-5

The instance is therefore an existing published benchmark object, not a TGCV-generated or manually constructed problem.

## 3. VisitAll state audit

The exact initial state contains:

(at-robot loc-x2-y2)

and:

(visited loc-x2-y2)

The exact initial state contains four outgoing connected relations from the robot location:

1. loc-x2-y2 -> loc-x1-y2
2. loc-x2-y2 -> loc-x3-y2
3. loc-x2-y2 -> loc-x2-y1
4. loc-x2-y2 -> loc-x2-y3

The VisitAll domain defines move as applicable when the current robot position and the target position satisfy the corresponding connected relation.

Therefore, at the exact initial state:

|T_acc| = 4

and the gate requirement |T_acc| >= 2 is satisfied with margin.

No generated, altered or synthetic instance is used.

## 4. Rainbow / SWIM exact source state

Primary Rainbow source:

- Repository: cmu-able/rainbow
- Revision: c053e2aab6d58c233016574887296e2be43ca60f
- Model: targets/swim/model/swim.acme
- Blob SHA: 9989790020ff1b814e0b1aa7bd1f926d980ce823
- Strategies: targets/swim/stitch/swimStrategies.s
- Blob SHA: 5ac062d6a01c918c018f29e26a9a3bc2943d4885
- Tactics: targets/swim/stitch/swimTactics.t.s
- Blob SHA: 513a5d78e301e9fa4660b8bac9154b93e6a7a605

The exact model declares:

- LB0.dimmer default = 1.0
- DIMMER_LEVELS = 5
- DIMMER_MARGIN = 0.1
- server1, server2 and server3
- each declared server has isActive default = true
- each declared server has isArchEnabled default = true

These declarations define the candidate initial model state without introducing an externally invented value.

## 5. Rainbow applicability audit

Two tactics are directly established as applicable from the pinned source state and pinned tactic definitions:

### TIncDimmer

Condition:

SwimUtils.dimmerFactorToLevel(M.LB0.dimmer, M.DIMMER_LEVELS, M.DIMMER_MARGIN) < M.DIMMER_LEVELS

With LB0.dimmer = 1.0 and DIMMER_LEVELS = 5, the condition is true.

### TRemoveServer

Condition:

numberOfServers > 1

The pinned model declares three ServerT components, so the condition is true.

Therefore the selected Rainbow state satisfies:

|T_acc| >= 2

with at least:

- TIncDimmer
- TRemoveServer

No reliance on TAddServer is required for this gate.

## 6. Structural-resolution equivalence

The two selected states are not claimed to be semantically isomorphic.

They are equivalent only at the fixture-design resolution required by this gate:

**explicit state S -> explicit applicability conditions -> finite applicable transformation set -> source-defined transformation effects**

VisitAll:

S_VA,0 = exact PDDL initial state
T_acc,VA(S_VA,0) = 4 move transformations

Rainbow:

S_SWIM,0 = exact declared/default model state
T_acc,SWIM(S_SWIM,0) contains at least 2 source-defined tactics

This is sufficient for the intended cross-domain structural fixture contrast while preserving domain-specific transformation semantics.

## 7. Traceability result

| Gate item | Result |
|---|---|
| Existing exact VisitAll instance | PASS |
| VisitAll instance traceable to immutable source revision | PASS |
| VisitAll exact blob identified | PASS |
| VisitAll initial state explicit | PASS |
| VisitAll |T_acc| >= 2 | PASS — 4 |
| No fabricated VisitAll instance | PASS |
| Rainbow source revision immutable | PASS |
| Rainbow state values source-derived | PASS |
| Rainbow |T_acc| >= 2 | PASS — at least 2 |
| Common structural resolution defined | PASS |
| Scientific execution authorized | NO |

## 8. Gate conclusion

**NON-TRIVIAL EXACT INSTANCE SELECTION AND FIXTURE TRACEABILITY AUDIT: PASS**

The remaining source-selection blocker is closed.

The selected VisitAll fixture is:

**IPC-2014 / visit-all-sequential-optimal / instance-1.pddl / grid-5**

with exact initial-state accessibility:

**|T_acc| = 4**

The corresponding Rainbow candidate state is the declared/default SWIM model state with at least two directly source-defined applicable tactics:

**TIncDimmer, TRemoveServer**

## 9. Next operational gate

The next operation is not scientific execution.

It is the **final fixture construction / preflight package update**, using only the two pinned source objects and the exact benchmark instance recorded here.

The scientific boundary remains:

**SCIENTIFIC EXECUTION: NOT AUTHORIZED**
