# TGCV TR-131 — Rainbow SWIM Runtime Smoke-Test Block 001

**Status:** BLOCKED — INFRASTRUCTURE / PINNED RUNTIME  
**Scientific evidence:** NO  
**Scientific execution:** NOT AUTHORIZED

## Scope

This record documents the exact-source Rainbow SWIM runtime smoke test performed against the pinned Rainbow runtime. The purpose was infrastructure validation only. No scientific execution, adaptation evaluation, trajectory generation, or value measurement was authorized.

## Pinned runtime

- Rainbow revision: `c053e2aab6d58c233016574887296e2be43ca60f4`
- Target: `swim`
- Packaged runtime: `Rainbow-202609210231.zip`
- Package SHA-256: `1ab03f1a92107de23b7ded3fd8a64deb9b9c1e92a6e790f7bb464a59c07e1fdc`
- PLADAPT source revision: `6d594bd8e16299f0bb8d0a403088c5638aff9e6f`
- PLADAPT Java wrapper was built and installed, but the smoke test did not reach its initialization call.

## Observed execution path

The controlled harness reached:

1. Rainbow singleton initialization.
2. Loading and registration of `SwimSys:Acme`.
3. Loading and registration of `ArrivalRate:TSP`.
4. Model lookup of `SwimSys:Acme`.
5. Creation of the SWIM adaptation manager.
6. Entry into `AdaptationManagerBase.initializeAdaptationMgr()`.
7. `computeDecisionHorizon()`.
8. `SwimModelHelper.getMaxServers()`.

The run then stopped with:

```
java.lang.ClassCastException:
class java.lang.Integer cannot be cast to class java.lang.Double
at org.sa.rainbow.model.acme.swim.SwimModelHelper.getDoubleProperty(SwimModelHelper.java:74)
at org.sa.rainbow.model.acme.swim.SwimModelHelper.getMaxServers(SwimModelHelper.java:162)
at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.computeDecisionHorizon(AdaptationManagerBase.java:422)
at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.initializeAdaptationMgr(AdaptationManagerBase.java:538)
```

The expression involved is:

```
[EXPR]size(/self/components:ServerT)
```

The evaluated result is an `Integer`, while the pinned `getDoubleProperty()` implementation casts non-`Float` values directly to `Double`.

## Boundary determination

The exception occurs before:

- `JavaSDPAdaptationManager.initialize()`;
- PLADAPT native-wrapper initialization;
- adaptation evaluation;
- `checkAdaptation()`;
- `runAction()`;
- `evaluate()`;
- any scientific execution.

Therefore this run provides no scientific evidence about TGCV, transformation-space properties, adaptation outcomes, trajectories, causality, or value.

## Disposition

The exact-source Rainbow SWIM smoke test is recorded as **BLOCKED_INFRASTRUCTURE** at the pinned runtime's model-property type boundary.

No Rainbow source was modified to bypass the exception. No scientific interpretation is attached to the failure.

**Scientific execution remains NOT AUTHORIZED.**

## Integrity note

This record is an infrastructure result only. It does not authorize changing the pinned runtime semantics, replacing the exact-source implementation, or treating a harness-level type normalization as an exact-source validation result.
