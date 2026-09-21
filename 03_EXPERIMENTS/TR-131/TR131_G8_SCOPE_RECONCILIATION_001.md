# TGCV TR-131 — G8 Scope Reconciliation 001

**Status:** RECONCILED — LEGACY G8 NOT APPLICABLE TO EXACT-SOURCE PACKAGE  
**Scientific execution under exact-source package:** NOT AUTHORIZED

## Canonical conflict resolved

The repository currently contains:

- `G8_AUTHORIZATION_RECORD_v01.json`, which records a historical G8 authorization for a previously frozen package at commit `b0b3cd4e2d4c86f341b9465f9f6188de9f1bfbb0`.
- `TR-131_EXACT_SOURCE_FREEZE_CANDIDATE_MANIFEST_v03.json`, which explicitly defines the exact-source VisitAll/Rainbow package as a new candidate and states `scientific_execution_authorized: false`.

The exact-source manifest explicitly prohibits extending the old G8 to this package:

```
"old_G8_extended_to_this_package": true
```

and requires, before exact-source freeze:

1. exact-source scientific runner;
2. runner source-traceability preflight;
3. complete immutable artifact hash inventory;
4. independent Executor-2 reconstruction;
5. new Freeze Audit;
6. new hash-bound G8 authorization.

## Disposition

The historical `G8_AUTHORIZATION_RECORD_v01.json` remains a record of its original package and is **not** interpreted as authorization for the exact-source VisitAll/Rainbow package.

For the exact-source package, the controlling state is:

```
EXACT-SOURCE FREEZE CANDIDATE — BLOCKED
scientific_execution_authorized = false
```

The Rainbow SWIM runtime smoke-test result is independently recorded as `BLOCKED_INFRASTRUCTURE` and does not authorize scientific execution.

No existing historical authorization record has been rewritten.

## Next gate

Do not execute the exact-source scientific runner.

The next operational work is to complete or formally close the exact-source package construction gates, with the Rainbow runtime blocker retained as infrastructure evidence.

**Canonical disposition:** EXACT-SOURCE G8 NOT ESTABLISHED.
