# C10-S F5 G7 — staged and resumable execution architecture 002

**Record:** C10S-F5-G7-EXECUTION-ARCHITECTURE-002  
**Version:** 1.1  
**Status:** DRAFT FOR DETERMINISTIC SOFTWARE VALIDATION — NOT AUTHORIZATION TO RUN HOLDOUT  
**Scientific protocol:** C10S-F5-G7-TIERA-PROSPECTIVE-001 v1.1  
**Research branch:** `research/c10s-f5-g7-canonical-mle-v1.1-20261122`

## 1. Purpose and boundary

This architecture preserves the staged/resumable G7 execution graph and the same-runner clean-source replay correction already implemented after the v1.0 failure. It adds the v1.1 canonical-fit and scientific-record/diagnostic-sidecar contracts.

It does not change the scientific target cells, K=1,000 per cell, C0/C5 B=1,000, estimands, percentile interval construction, nominal level, coverage bounds, Wilson rule, 95% interval-emission threshold, no-pooling rule or failure dispositions. The v1.1 seed schedule and namespaces are new and disjoint because the v1.0 bank is consumed and unblinded.

## 2. Canonical F5 fit and optimizer diagnostics

The G7 production path runs the exact global beta-binomial likelihood certificate before any floating-point optimizer.

- A certified global boundary supremum, co-maximum or unresolved global ordering is a typed abstention.
- A certified global interior maximum supplies the exact Krawczyk root enclosure.
- Newton locator steps never count as a root proof; only the final exact Krawczyk certificate accepts the refined candidate box, which must be nested in the original certified enclosure.
- The canonical bootstrap fit is the rational midpoint of the enclosure in compactified `(mu,t)` coordinates, where `t=kappa/(1+kappa)`.
- The production certificate call uses `max_refinements=3`, `max_lift_depth=24` and `max_mu_depth=12`; each interior root box is then refined with up to 12 exact rational Newton locator steps rounded to a fixed 2^{-64} dyadic grid to bound intermediate denominator growth, followed by an exact Krawczyk inclusion/contraction proof on a candidate box. Each axis enclosure width must be no greater than (2^{-32}). Wider enclosures fail closed; optimizer-selected parameters are not a fallback.
- Three-start finite-difference L-BFGS-B and the independent analytic-gradient audit run after certification for diagnostics only. Their raw outputs cannot select or veto the canonical fit.

The exact certificate remains responsible for global likelihood ordering. The floating-point midpoint is only the deterministic numerical representative used to parameterize the bootstrap generator.

## 3. Scientific record and diagnostic sidecar schemas

- Scientific shard schema: `TGCV-C10S-F5-G7-SHARD-002`.
- Scientific record digest: SHA-256 over canonical sorted-key JSON of the scientific record list, excluding CandidateOutput diagnostics.
- Diagnostic sidecar: `optimizer_diagnostics`, keyed by dataset and method, preserving every CandidateOutput diagnostic item.
- Diagnostic sidecar digest: `optimizer_diagnostics_digest`, SHA-256 over canonical sorted-key JSON of the complete sidecar list.

The aggregator must:
1. verify the scientific record digest;
2. verify the diagnostic sidecar digest and exact dataset/method roster;
3. verify all seed, row, truth, method-roster and denominator constraints;
4. compare primary/replay scientific records and their digests exactly;
5. preserve both diagnostic sidecars and their digests in the immutable shard artifacts and final shard manifest;
6. not require optimizer diagnostic sidecars to be byte-identical and not allow them to influence the scientific replay verdict.

A diagnostic-sidecar mismatch is retained and auditable. A scientific-record mismatch remains a replay integrity failure and blocks adjudication.

## 4. Execution graph

1. **Authorization:** validate the new one-use approval, exact code parent, protocol v1.1, architecture v1.1, fresh resource-profile manifest and complete source hashes.
2. **Preflight evidence validation:** download the immutable v1.1 resource-only profile and validate its archive/JSON digests, source ancestry, source-file byte identity, K/B, cells, namespace and timing-only scope. Do not recompute the profile on retries.
3. **Primary matrix:** execute each frozen cell as independent global replicate-index shards. Each shard writes one immutable scientific-record artifact plus its optimizer-diagnostics sidecar and separate digests. No shard-level coverage adjudication.
4. **Replay matrix:** each primary shard is paired sequentially with a clean-source replay on the same Ubuntu 24.04 runner. The replay tree is freshly materialized from the exact approved commit using `git archive`; the pinned Python environment and single-thread BLAS/OpenMP settings are retained. Replay artifacts remain separate and immutable.
5. **Final aggregation:** verify gap-free/non-overlapping coverage of indices 0–999 per cell; verify data/seed/truth/row identities; validate each diagnostic sidecar independently; require exact scientific-record equality; rehydrate records; invoke `adjudicate_matched_datasets` exactly once on the full K=1,000 denominator per cell; then apply the unchanged G7 adjudicator.

## 5. Shard sizing and resource-only profile

The v1.0 resource profile (run 44926453920) is invalid for v1.1 because the fitting/certificate path has changed. It cannot be reused to authorize a v1.1 holdout.

A fresh profile is required from the final v1.1 compute snapshot:
- K=100 per cell in the new disjoint resource namespace;
- C0/C5 B=1,000;
- timing/resource measurements only;
- no certificate-status counts, interval-emission counts, abstention outcomes, coverage or method-selection results;
- no coverage adjudication and no mixing with the holdout bank.

The profile schema is `C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002`; its scope is `RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT`. The profile manifest schema is `C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002`. Its source commit must be an ancestor of the authorized source snapshot and every performance-critical source file must be byte-identical. A change to the fitter, certificate, engine, fixtures, dependency lock, runner or profile script invalidates the profile.

The workflow uses one GitHub matrix job per shard pair: each job executes the primary shard and then its clean-source replay sequentially on the same runner. The frozen 150-minute per-job work budget therefore applies to the combined primary+replay pair, not to either phase separately; the workflow hard timeout is 165 minutes. The validator must reject any shard size whose conservative paired runtime (two measured phase runtimes plus the declared per-phase setup allowance) exceeds 9,000 seconds. The matrix has one shared `max-parallel: 20` pool across both cells; concurrency is not reset per cell. The wall-clock projection therefore uses the global paired-job workload divided by 20 plus the Graham list-scheduling tail bound `(1 - 1/20) × longest paired job`. Aggregate runner-compute hours are reported separately. No prior v1.0 projection is silently carried forward.

The v1.1 resource profile (run 45365559253; K=100 per cell) has a slow-cell maximum of 418.194638 seconds per dataset. The integrated planner now declares a conservative **900-second setup allowance per phase** (engineering reserve, not a measured constant) and evaluates shard candidates including size 8. Under this reserve, the selected plan is **8 datasets per shard**, 125 shards per cell (250 matrix jobs per phase), with a worst-observed paired primary+replay job estimate of **8,491.114 seconds (141.519 minutes)**, leaving 508.886 seconds against the 9,000-second work budget. Sensitivity scenarios of 300 and 600 seconds per phase also remain within the budget for this shard size.

Under the maximum-observed-dataset projection, the 8-shard plan implies 361.756 aggregate primary+replay runner-hours and a 73,182.699-second (20.329-hour) shared-pool list-scheduling bound; adding the already completed 2,600.725-second resource-only profile gives 75,783.425 seconds (21.051 hours). These remain conditional scheduling estimates, not guarantees for future runtimes. RG-07 therefore remains conditional: K=100 does not bound the maximum or upper tail of K=1,000. No new profile or holdout data are generated by this planner change.

## 6. Recovery and no-repeat guarantee

Each primary/replay pair is a separate matrix job and immutable artifact. A transient failure may retry only the failed shard pair. Completed pairs and the resource profile are reused within that exact authorized run. A later failure must not trigger regeneration of completed datasets.

The consumed v1.0 primary/replay artifacts remain immutable. No v1.0 shard is replaced, relabelled as v1.1 or mixed into v1.1 denominators. No replay mismatch is repaired by replacing one side.

## 7. Integrity and scientific adjudication

The v1.1 final aggregator verifies:
- exact cell roster and K=1,000 coverage per cell;
- no replicate-index gaps or overlaps;
- exact dataset IDs, seed schedule and namespace;
- exact row digests, analytical truth pairing and C0/C5 method roster;
- per-shard scientific-record digest integrity;
- per-shard diagnostic-sidecar digest and dataset/method roster;
- exact primary/replay scientific record equality;
- one full-bank adjudication per cell and the unchanged four component-cell G7 criteria.

The resource-only profile is never included in primary/replay denominators. The diagnostics sidecar is never used to rescue, fail or alter a scientific interval or global-MLE classification.

## 8. Authorization status

This architecture is a research draft for deterministic software validation. The previous one-use authorization `G7-20261122-0100` is consumed and bound to the v1.0 code/protocol snapshot. It cannot authorize v1.1.

A future v1.1 holdout requires a new one-use authorization branch and commit, bound to:
- protocol v1.1 and architecture v1.1;
- canonical fitter, exact certificate and inference engine;
- shard executor, aggregator and CLI;
- timing-only resource-profile script, validator and fresh manifest;
- deterministic and adversarial tests;
- dependency lock and G7 workflow.

No holdout authorization or holdout execution is created by this document.
