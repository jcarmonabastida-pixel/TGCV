# C10-S F5/G7 Dispatch Recovery and Resource Preflight Contract — Draft 001

**Status:** DRAFT — technical contract for research-branch implementation; not an authorization to execute G7.  
**Scope:** GitHub Actions orchestration, resource-profile provenance, preflight recovery, and one-use authorization semantics.  
**Scientific boundary:** No change to DGP, estimands, oracle, F5/G7 analysis, seed schedule, sample sizes, or causal claims. G7 remains prospective Tier-A calibration only; Tier B and causal C10 execution remain unauthorized.

## 1. Evidence baseline and corrections

Inspected source: .github/workflows/c10-s-f5-g7-tiera-calibration-v3.yml on authorization branch research/c10s-f5-g7-auth-C10S-F5-G7-3c1355d70d88, authorization commit 0743f0973292bdd26bd37c1da6a8d76dd9fd02c2, approved code parent 3c1355d70d88c39b3085c86d10520e74cb45f64c.

Run 45736995385 failed in resource preflight before any primary/replay shard. The workflow's authorization job writes the permanent consumption marker before the dependent resource preflight job. The authorization gate also rejects any earlier workflow_dispatch on the branch, even if the earlier run failed before shards. These two controls make a preflight-only failure irrecoverable on that authorization branch.

**Resource-manifest correction:** the authorization branch contains 03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json. Its values match the authorization's profile run 45365559253, artifact 14908914198, namespace c10s_f5_g7_resource_v1_1, K=100, and profile JSON SHA-256 005ef265fa7dd8812c2572d9187cc7943c365506dc8e1169f1883487c0094d9f. The separate 03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_G7_RESOURCE_PROFILE_MANIFEST_001.json is a legacy profile (run 44926453920, artifact 14717426261, namespace v1). It is not the manifest referenced by this authorization. Earlier statements that the authorization branch's active manifest pointed to the legacy artifact were incorrect.

The actual route defect is in the preflight job's working directory 03_EXPERIMENTS/C10-S/harness: it sets MANIFEST to 03_EXPERIMENTS/C10-S/fixtures/... and passes fixtures/...; neither is valid from that working directory. The later profile-validation step correctly uses ../fixtures/.... The route must be derived from the repository root or normalized once and reused consistently.

## 2. Required job order

The workflow must enforce this dependency graph:

1. **Authorization validation (read-only):** validate dispatch actor, exact input, authorization schema/status/expiry/scope, branch/ref, exact approved-code parent, workflow identity, and all source hashes. It must not write to the repository or create a consumption marker.
2. **Resource preflight (non-consuming):** fetch the exact artifact ID and run ID from the validated authorization; verify repository identity, artifact metadata, archive digest, profile digest, manifest digest, profile schema/scope, expiry, K=100 resource-only boundary, seed namespace, and all required resource constraints. Produce and validate the complete shard plan. Do not execute any shard.
3. **Atomic one-use claim/consumption:** only after steps 1–2 pass, claim the authorization exactly once. Use a compare-and-swap mechanism with a stable authorization identity and immutable commit binding. Concurrent dispatches must not both claim. The durable consumed record must include authorization commit, approved code commit, workflow blob identity, preflight result/plan digest, run ID, actor, and timestamp. The claim operation must fail closed if the ref or authorization content changed.
4. **Primary and replay:** require successful consumption and the exact preflight plan digest; execute only the authorized Tier-A phases.
5. **Final adjudication:** require complete primary/replay evidence and verify source, plan, shard, and aggregation integrity.

A failed step 1 or 2 must leave the authorization unconsumed. A failed step 3 or any later step must leave it consumed; no automatic rerun or replay is permitted under that authorization.

## 3. Retry and concurrency semantics

- Do not reject a dispatch merely because a prior dispatch exists.
- Reject only when a valid durable consumption/claim record exists, or when the authorization is expired, invalid, changed, or otherwise outside scope.
- Serialize dispatches per authorization identity.
- Prevent concurrent preflights from racing into duplicate consumption. The final claim must be atomic (e.g. GitHub ref update with expected old SHA / create-only marker semantics); a plain check-then-write sequence is insufficient.
- A preflight failure permits a corrected dispatch against the same still-valid authorization only if the authorization's approved code and workflow binding remain unchanged. If workflow code itself changes, the authorization must not be silently reused: generate a new authorization binding after deterministic validation.
- A successful consumption permanently disables further dispatches for that authorization, regardless of whether shards start or later fail.

## 4. Resource path and provenance contract

- Resolve repository root once using git rev-parse --show-toplevel.
- Resolve the active manifest as $REPO_ROOT/03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json.
- Pass that exact absolute path to the artifact verifier and profile validator; do not reconstruct a second relative path.
- Verify that the authorization's manifest SHA-256 equals the active manifest file's SHA-256 and that all manifest fields match the authorization's profile run/artifact/archive/profile digests and resource namespace.
- Treat the legacy diagnostics manifest as a separate historical profile; never substitute it based on filename similarity.
- Add a preflight test that runs from the workflow's actual working directory and proves the manifest resolves and matches the approved artifact.
- Add negative tests for wrong path, legacy manifest, mismatched artifact ID/run ID, archive digest mismatch, profile digest mismatch, expired artifact, wrong namespace, and changed manifest.

## 5. Required acceptance tests

The workflow change is not ready until all of these are demonstrated on a non-authorizing test path:

| Test | Expected result |
|---|---|
| Valid authorization + valid artifact/profile | Preflight PASS; plan emitted; no consumption yet |
| Missing/wrong manifest path | Preflight FAIL; no consumption marker |
| Legacy manifest substituted | Preflight FAIL; no consumption marker |
| Wrong artifact ID/run ID or repository | Preflight FAIL; no consumption marker |
| Archive/profile/manifest digest mismatch | Preflight FAIL; no consumption marker |
| Expired artifact or authorization | FAIL closed; no consumption marker |
| Two concurrent valid dispatches | Exactly one atomic claim succeeds |
| Second dispatch after successful claim | Rejected as already consumed |
| Preflight failure followed by corrected retry | Retry allowed only while authorization and bound workflow/code remain unchanged |
| Failure after successful claim | Authorization remains consumed; no retry |
| Primary/replay attempted without claim and plan | Jobs remain skipped |

The tests must inspect both GitHub job dependencies and durable repository state, not merely unit-test helper functions.

## 6. Authorization and governance boundary

This contract does not create, approve, extend, or revive any authorization. The authorization C10S-F5-G7-3c1355d70d88 was consumed by run 45736995385 and remains unusable. No new authorization is to be prepared until the corrected workflow, provenance chain, and recovery tests pass and the canonical governance state permits the next execution.

main must remain unchanged during research implementation. Changes are to be developed and validated on a research branch/PR. No G7 dispatch, shard, Tier-B run, or causal C10 execution is authorized by this document.

## 7. Completion criterion

The recovery defect is closed only when a clean research-branch validation proves, end-to-end, both:
- **Preflight failure -> no authorization consumption and a valid corrected retry path**, and
- **Preflight success -> one atomic consumption -> exactly one primary/replay launch path**.

A green compilation or unit-test suite alone is insufficient. No claim of successful G7 launch may be made before GitHub records actual primary/replay jobs.
