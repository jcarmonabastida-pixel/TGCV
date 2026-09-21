# TGCV TR-131 — Exact-Source Runtime Gate Closure 001

**Status:** CLOSED — CROSS-DOMAIN PACKAGE BLOCKED  
**Scientific execution:** NOT AUTHORIZED

## Gate conclusion

The source-runtime availability gate has now been resolved asymmetrically:

| Domain | Source runtime | Disposition |
|---|---|---|
| VisitAll | Pinned PDDL + pinned Fast Downward revision | AVAILABLE for non-scientific smoke test |
| Rainbow/SWIM | Pinned Rainbow revision and exact packaged build | BLOCKED by pinned runtime type incompatibility |

## VisitAll disposition

The exact source domain/problem was executed through the pinned Fast Downward runtime. Translation and search completed successfully, and the resulting plan was consistent with the source-defined action semantics.

This establishes infrastructure-level executability only.

## Rainbow/SWIM disposition

The exact packaged Rainbow SWIM runtime loads and registers the pinned SWIM model, but the initialization path fails in the pinned source at:

`SwimModelHelper.getDoubleProperty()`

when the source expression `[EXPR]size(/self/components:ServerT)` returns `Integer` and the pinned implementation casts it directly to `Double`.

The failure occurs before PLADAPT initialization and before adaptation evaluation.

No source patch, semantic substitution, or synthetic transition has been introduced to bypass this condition.

## Package consequence

Because the TR-131 exact-source design requires authentic source-defined transition execution for both source domains, the cross-domain exact-source scientific package **cannot proceed to Freeze Audit or G8** at this time.

The VisitAll runtime result must not be used to silently replace the blocked Rainbow domain.

The existing hand-written adapter functions remain **preflight approximations** and are not promoted to scientific execution adapters.

## Methodological disposition

This closure is preferable to silently changing the experimental object:

- no synthetic Rainbow transition;
- no cross-domain semantic mapping;
- no runtime source patch;
- no reuse of the historical G8 authorization;
- no scientific execution.

## Next legitimate paths

Only two paths remain methodologically valid:

1. establish an independently auditable, exact-source-compatible Rainbow execution path without changing the pinned semantics; or
2. explicitly redesign the research package as a VisitAll-only experiment, with a new protocol, package, audit and authorization rather than treating it as the existing cross-domain TR-131 experiment.

**Canonical gate result: CROSS-DOMAIN EXACT-SOURCE PACKAGE BLOCKED.**
