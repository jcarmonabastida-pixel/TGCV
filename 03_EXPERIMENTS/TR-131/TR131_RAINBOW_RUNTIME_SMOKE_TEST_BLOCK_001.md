# TGCV TR-131 — Rainbow SWIM Runtime Smoke-Test Block 001

**Status:** BLOCKED — INFRASTRUCTURE / PINNED RUNTIME  
**Scientific evidence:** NO  
**Scientific execution:** NOT AUTHORIZED

## Scope

This record documents the exact-source Rainbow SWIM runtime smoke test performed against the pinned Rainbow runtime. The purpose was infrastructure validation only. No scientific execution, adaptation evaluation, trajectory generation, or value measurement was authorized.

## Pinned runtime

- Rainbow revision: `c053e2aab6d58c233016574887296e2be43ca60f4`
- Target: `swim`
- Rebuilt packaged runtime: `Rainbow-202609210558.zip`
- Rebuilt package SHA-256: `B538E095E57F23CA80687FD6F738C3B34CE684084FFBC164AD29ADF166FB1415`
- Rebuilt package size: `44,373,109` bytes
- PLADAPT source revision: `6d594bd8e16299f0bb8d0a403088c5638aff9e6f`
- PLADAPT native wrapper loaded successfully in the rebuilt reproduction from `/tmp/TR131_pladapt/java/libpladapt_wrap.so`.
- Java runtime: OpenJDK `1.8.0_502`
- Maven build environment: Maven `3.3.9` under Ubuntu 24.04; the historical Rainbow source/build configuration was not modified.

## Rebuilt-runtime reproduction

A fresh Rainbow package was produced from the pinned Rainbow revision and exercised with the same minimal smoke-test harness used for the prior runtime check.

The rebuilt run reached:

1. Rainbow singleton initialization.
2. Loading and registration of `SwimSys:Acme`.
3. Loading and registration of `ArrivalRate:TSP`.
4. Model lookup of `SwimSys:Acme`.
5. Creation of the SWIM adaptation manager.
6. Evaluation of `[EXPR]size(/self/components:ServerT)`, yielding `MAX_SERVERS=3`.
7. Entry into `AdaptationManagerBase.initializeAdaptationMgr()`.
8. `computeDecisionHorizon()`.
9. `SwimModelHelper.getMaxServers()`.

The rebuilt run then stopped with the same type-boundary exception:

```
java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.Double
    at org.sa.rainbow.model.acme.swim.SwimModelHelper.getDoubleProperty(SwimModelHelper.java:74)
    at org.sa.rainbow.model.acme.swim.SwimModelHelper.getMaxServers(SwimModelHelper.java:162)
    at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.computeDecisionHorizon(AdaptationManagerBase.java:422)
    at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.initializeAdaptationMgr(AdaptationManagerBase.java:538)
```

The relevant expression remains:

```
[EXPR]size(/self/components:ServerT)
```

The expression evaluates to an `Integer`, while the pinned `getDoubleProperty()` implementation casts non-`Float` values directly to `Double`.

## Diagnostic significance

The same exception is reproduced after rebuilding the pinned Rainbow source at revision `c053e2a...`, using Java 8 and the rebuilt package. The earlier failure therefore cannot be attributed to the previous packaged runtime alone, nor to the Java 21 runtime used in the preliminary `CheckConfiguration` attempt.

The preliminary `CheckConfiguration` failure is not used as the blocking evidence: it was a separate configuration-checker path and produced a `NullPointerException` after configuration loading. The controlled harness reaches the SWIM adaptation-manager initialization boundary directly.

The PLADAPT native-library loading issue observed in an intermediate harness invocation was an environment-path issue only; after correcting the library path to the actual `/tmp/TR131_pladapt/java` directory, the harness loaded PLADAPT successfully and reproduced the original type-boundary exception.

## Boundary determination

The exception occurs before:

- `JavaSDPAdaptationManager.initialize()`;
- adaptation evaluation;
- `checkAdaptation()`;
- `runAction()`;
- `evaluate()`;
- any scientific execution.

Therefore this run provides no scientific evidence about TGCV, transformation-space properties, adaptation outcomes, trajectories, causality, or value.

## Disposition

The exact-source Rainbow SWIM runtime remains **BLOCKED_INFRASTRUCTURE** at the pinned runtime's model-property type boundary.

No Rainbow source was modified to bypass the exception. No Integer-to-Double normalization was introduced. No scientific interpretation is attached to the failure.

The rebuilt package does not establish an exact-source executable transition adapter for TR-131.

**Scientific execution remains NOT AUTHORIZED.**

## Integrity note

This record is an infrastructure result only. It does not authorize changing the pinned runtime semantics, replacing the exact-source implementation, or treating a harness-level type normalization as an exact-source validation result.
