# TGCV TR-131 — SOURCE-RUNTIME DISCOVERY AND PINNING RECORD 001

**Status:** DISCOVERY PASS — RUNTIME CANDIDATES PINNED; SMOKE TEST PENDING
**Scientific execution:** NOT AUTHORIZED

## VisitAll

The VisitAll repository is a generator/source repository, not the execution engine. A separately auditable PDDL execution engine is therefore required.

Pinned candidate:

- Engine: Fast Downward
- Repository: `aibasel/downward`
- Release: `26.6`
- Release branch: `release-26.6`
- Release source revision: `cc2269256a394e5b7b1283952857da98cddc8b26`
- Build contract: `./build.py release debug`
- Scientific use constraint: planner configuration must be fixed independently of the A/B transformation choice; the engine is used only to validate/apply source-defined PDDL semantics and must not select the experimental A/B treatment.

The exact VisitAll domain/problem remain the already pinned source artifacts. Fast Downward is an external execution dependency, not a replacement for those source artifacts.

## Rainbow/SWIM

The pinned Rainbow revision itself contains the deployment and build path for SWIM.

Pinned source:

- Repository: `cmu-able/rainbow`
- Revision: `c053e2aab6d58c233016574887296e2be43ca60f4`
- Deployment: `deployments/rainbow-swim`
- Target: `swim`
- Build command documented by the pinned deployment: `./build.sh -s -d rainbow-swim -t swim`
- Relevant runtime/source classes include the SWIM model and command implementations under `deployments/rainbow-swim/src/main/java/org/sa/rainbow/model/acme/swim/`.
- The pinned deployment documentation also identifies the SWIM simulator dependency and the model/simulation parameter correspondence.

## Gate disposition

**SOURCE-RUNTIME DISCOVERY: PASS**

**SOURCE-RUNTIME EXECUTION AVAILABILITY: PENDING SMOKE TEST**

No scientific execution has occurred.

## Required smoke tests

### VisitAll smoke test

Using the exact pinned VisitAll domain/problem and Fast Downward 26.6:

1. build the pinned engine;
2. validate the exact domain/problem;
3. execute a deterministic single-action transition trace for a selected grounded `move`;
4. capture the engine revision, command line, input hashes and resulting state/plan trace;
5. verify the transition against the source-defined action semantics.

### Rainbow/SWIM smoke test

Using the exact pinned Rainbow revision:

1. build `rainbow-swim` using the pinned deployment command;
2. verify the resulting build identity;
3. initialize the SWIM target with the exact pinned model;
4. execute one source-defined tactic operation corresponding to the selected fixture transformation;
5. capture command/runtime identity and resulting model state;
6. verify the resulting state against the pinned tactic/model semantics.

A failed or non-reproducible smoke test keeps the corresponding domain blocked.

## Scientific boundary

This record does not authorize A/B execution. The runtime smoke tests are infrastructure/provenance tests only.
