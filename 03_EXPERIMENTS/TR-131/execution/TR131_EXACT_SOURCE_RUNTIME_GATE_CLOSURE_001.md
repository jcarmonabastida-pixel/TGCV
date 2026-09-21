# TGCV TR-131 — Exact-Source Runtime Gate Closure 001

**Status:** CLOSED — CROSS-DOMAIN PACKAGE BLOCKED  
**Scientific execution:** NOT AUTHORIZED

## Gate conclusion

VisitAll remains available for infrastructure-level smoke testing. Rainbow/SWIM remains blocked, now with the block reproduced against a newly rebuilt package from the pinned Rainbow revision.

## Rainbow/SWIM reproduced block

Pinned Rainbow revision: `c053e2aab6d58c233016574887296e2be43ca60f4`

Rebuilt package: `Rainbow-202609210558.zip`

Rebuilt package SHA-256: `B538E095E57F23CA80687FD6F738C3B34CE684084FFBC164AD29ADF166FB1415`

Runtime: OpenJDK `1.8.0_502`.

The PLADAPT native wrapper was successfully loaded after correcting the library path to the actual wrapper directory. The controlled harness then reached Rainbow initialization, registration of `SwimSys:Acme` and `ArrivalRate:TSP`, SWIM model lookup, adaptation-manager initialization, and evaluation of `[EXPR]size(/self/components:ServerT)`, yielding `MAX_SERVERS=3`.

The rebuilt run then reproduced the same pinned-runtime failure:

```text
java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.Double
    at org.sa.rainbow.model.acme.swim.SwimModelHelper.getDoubleProperty(SwimModelHelper.java:74)
    at org.sa.rainbow.model.acme.swim.SwimModelHelper.getMaxServers(SwimModelHelper.java:162)
    at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.computeDecisionHorizon(AdaptationManagerBase.java:422)
    at org.sa.rainbow.swim.adaptation.AdaptationManagerBase.initializeAdaptationMgr(AdaptationManagerBase.java:538)
```

The expression `[EXPR]size(/self/components:ServerT)` returns `Integer`, while the pinned `getDoubleProperty()` implementation casts the non-`Float` value directly to `Double`.

The intermediate `CheckConfiguration` failure is not used as the gate result. The controlled harness is the relevant reproduction.

## Boundary determination

The failure occurs before adaptation evaluation and before any scientific execution. No Rainbow source was modified, no Integer-to-Double normalization was introduced, and no synthetic transition was used.

Therefore the rebuilt package does not establish an exact-source executable Rainbow transition adapter for TR-131.

## Package consequence

Because the exact-source TR-131 design requires authentic source-defined transition execution for both source domains, the cross-domain exact-source scientific package cannot proceed to Freeze Audit or G8.

The VisitAll runtime result must not silently replace the blocked Rainbow domain. Existing hand-written adapter functions remain preflight approximations and are not promoted to scientific execution adapters.

## Methodological disposition

- no synthetic Rainbow transition;
- no runtime source patch;
- no Integer-to-Double bypass;
- no cross-domain semantic mapping;
- no reuse of the historical G8 authorization;
- no scientific execution.

## Next legitimate paths

1. Establish an independently auditable, exact-source-compatible Rainbow execution path without changing pinned semantics; or
2. explicitly redesign the research package as a VisitAll-only experiment, with a new protocol, package, audit and authorization.

**Canonical gate result: CROSS-DOMAIN EXACT-SOURCE PACKAGE BLOCKED.**
