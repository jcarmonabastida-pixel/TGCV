# TGCV TR-131 — SOURCE-RUNTIME EXECUTION ADAPTER AVAILABILITY AUDIT 002

**Status:** PARTIAL — VISITALL ESTABLISHED; RAINBOW BLOCKED  
**Scientific execution:** NOT AUTHORIZED

## Scope

This audit updates the previous source-runtime availability finding using the completed non-scientific runtime smoke tests.

## VisitAll

**Status: ESTABLISHED FOR NON-SCIENTIFIC SMOKE TEST**

Pinned artifacts:

- pddl-generators revision: `d5c22c9ab21ecaf90db82daf2a0537973c661009`
- pddl-instances revision: `cf19edf7c53d1540ddbb396c642595e0926ee552`
- Fast Downward revision: `cc2269256a394e5b7b1283952857da98cddc8b26`

The exact domain/problem were translated and executed with the pinned Fast Downward build. The runtime produced a valid plan of cost/length 18. The first grounded action was consistent with the pinned source semantics.

This establishes an auditable source-runtime path for infrastructure testing. It does **not** constitute scientific execution or evidence.

## Rainbow / SWIM

**Status: BLOCKED — PINNED SOURCE RUNTIME**

Pinned Rainbow revision:

`c053e2aab6d58c233016574887296e2be43ca60f4`

The Rainbow SWIM package was built successfully and the exact packaged runtime was exercised through a controlled harness. Model loading and registration succeeded:

- `SwimSys:Acme`
- `ArrivalRate:TSP`

The runtime then failed during `AdaptationManagerBase.computeDecisionHorizon()` because the pinned `SwimModelHelper.getDoubleProperty()` casts the result of `[EXPR]size(/self/components:ServerT)` directly to `Double`, while the evaluated result is an `Integer`.

The failure occurs before `JavaSDPAdaptationManager.initialize()`, before PLADAPT initialization, and before any adaptation evaluation.

Therefore the Rainbow source-runtime execution adapter is **not established**.

## Combined gate result

The exact-source package has:

- VisitAll source-runtime path: **AVAILABLE FOR INFRASTRUCTURE SMOKE TEST**
- Rainbow/SWIM source-runtime path: **BLOCKED**
- Scientific execution: **NOT AUTHORIZED**

The hand-written Rainbow transition helpers remain preflight approximations and are not promoted.

## Governance consequence

The exact-source package cannot yet satisfy the source-runtime adapter availability gate for both domains.

No scientific runner, Freeze Audit, or G8 authorization may treat the Rainbow runtime as validated on the basis of this smoke test.

The infrastructure blocker must remain explicit unless an independently auditable exact-source-compatible runtime path is established without changing the pinned semantics.
