# TGCV TR-131 — SOURCE-DEFINED TRANSITION EXECUTION ADAPTER SPECIFICATION 001

**Status:** PASS — ADAPTER SPECIFICATION COMPLETE; IMPLEMENTATION NOT YET AUTHORIZED
**Scientific execution:** NOT AUTHORIZED

## 1. Purpose

Define the minimum auditable mechanism for applying the selected transformation using the exact pinned source semantics, without inventing a cross-domain transformation meaning.

## 2. VisitAll adapter

### Authoritative sources

- Instance: `potassco/pddl-instances`
  - revision: `cf19edf7c53d1540ddbb396c642595e0926ee552`
  - blob: `f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34`
- Domain: `AI-Planning/pddl-generators`
  - revision: `d5c22c9ab21ecaf90db82daf2a0537973c661009`
  - blob: `0e0ce4e845fac76ad9c8c815f9a697e7946784d8`

### Transformation

`move(?curpos, ?nextpos)`

Source-defined precondition:

`at-robot(curpos) AND connected(curpos,nextpos)`

Source-defined effect:

- add `at-robot(nextpos)`
- remove `at-robot(curpos)`
- add `visited(nextpos)`

### Executable adapter

The adapter shall implement only the STRIPS transition semantics present in the pinned domain artifact:

1. verify the selected grounded action is present in `T_acc`;
2. verify its source-defined precondition against `S_t`;
3. apply exactly the positive and negative literals in the source effect;
4. preserve all other state predicates;
5. emit the complete resulting state and transition trace.

No planner search, optimization, or goal-directed behavior is introduced.

## 3. Rainbow/SWIM adapter

### Authoritative sources

- Model: `targets/swim/model/swim.acme`
  - revision: `c053e2aab6d58c233016574887296e2be43ca60f4`
  - blob: `9989790020ff1b814e0b1aa7bd1f926d980ce823`
- Tactics: `targets/swim/stitch/swimTactics.t.s`
  - blob: `513a5d78e301e9fa4660b8bac9154b93e6a7a605`
- Strategies: `targets/swim/stitch/swimStrategies.s`
  - blob: `5ac062d6a01c918c018f29e26a9a3bc2943d4885`

### TIncDimmer

Source-defined applicability:

`dimmerFactorToLevel(LB0.dimmer,DIMMER_LEVELS,DIMMER_MARGIN) < DIMMER_LEVELS`

Source-defined action:

`M.setDimmer(LB0, dimmerLevelToFactor(currentLevel + 1, DIMMER_LEVELS, DIMMER_MARGIN))`

The adapter must execute this source-defined operation or an independently frozen executable representation whose code/provenance is traceable to the pinned tactic.

### TRemoveServer

Source-defined applicability:

`numberOfServers > 1`

where `numberOfServers = |M.components : ServerT|`.

Source-defined action:

- enumerate the current `ServerT` components;
- select the server with maximum `index`;
- invoke `M.removeServer(M.LB0,lastServer)`.

The adapter must execute this source-defined operation or an independently frozen executable representation whose code/provenance is traceable to the pinned tactic.

## 4. Execution boundary

The adapter must not:

- infer effects from transformation names;
- translate VisitAll moves into Rainbow tactics;
- introduce TGCV-specific state changes;
- use future observations to determine applicability;
- modify `T_acc`;
- select a transformation outside `T_acc`.

## 5. Required trace

For every application:

`domain, source_revision, source_blob(s), S_t, C_t, T_acc_hash, X, selected_rank, T_real, applicability_evidence, transition_operation, S_t1`

The trace must permit an independent executor to reconstruct the same transition from the pinned source.

## 6. Independent reconstruction

Executor-2 must independently:

1. obtain the same pinned source artifacts;
2. reconstruct the same initial state;
3. reconstruct `T_acc`;
4. verify the selected transformation;
5. verify applicability from source semantics;
6. apply the same source-defined transition;
7. reproduce `S_{t+1}`;
8. reproduce the transition trace hashes.

A disagreement blocks the package.

## 7. Critical implementation gate

The specification is complete, but **implementation is not yet authorized as scientific execution**.

Before implementation is frozen, the actual adapter code must itself be source-traceable and its resulting state representation must be audited.

## 8. Gate result

**SOURCE-DEFINED TRANSITION EXECUTION ADAPTER SPECIFICATION: PASS**

This closes the specification gap identified by the previous adapter audit.

It does **not** authorize scientific execution.

## 9. Next gate

**ADAPTER IMPLEMENTATION + SOURCE TRACEABILITY PREFLIGHT**

Implement the adapters, run only deterministic integrity/precondition tests, and produce an auditable trace for each selected transformation. No scientific A/B execution yet.
