# Temporal sequentiality profile — implementation record 001

- **Status:** SYNTHETIC CONTRACT SUITE PASS on tested source commit `94a72541b0bb607547b5460ff060e9d0a689f02b`; not a scientific validation.
- **Date:** 2026-10-14.
- **Implementation origin:** `prototype/sequentiality-test-first-001-20261014`.
- **Verification branch:** `prototype/sequentiality-contract-tests-001-20261014`.
- **Scope:** synthetic prototype engine only. No changes to TGCV scientific Core.

## Changes

The existing engine now accepts an explicit rule profile:
`{"type":"temporal_prerequisite_graph","version":"1"}`.

Under this profile, relation type `requires_prior_execution` means that a transition is applicable only when its required transition ID has occurred earlier in the same sequence prefix. The rule is evaluated path-locally during bounded exploration and during explicit concrete sequence execution.

A new `execute_sequence(model, scenario_id, transition_ids)` function records ordered step events, current-state progression, blocked step/reason, a deep-copied configuration snapshot, configuration hash, trace hash and a per-invocation execution ID.

The historical `finite_deterministic_graph` and `relation_guarded_graph` profiles retain their separate dispatch and existing relation type. No existing profile was reinterpreted.

## Deliberate scope limits

- The engine remains a finite synthetic graph simulator; this does not implement TGCV T_acc, outcome evaluation, contextual value or empirical inference.
- The current execution trace is an in-memory returned record. A persistent run-history store and UX integration remain future work.
- This implementation is an initial minimum profile; repeated/cyclic prerequisite semantics beyond “required transition occurred at least once earlier in this path” remain limited to the stated rule.
- No performance optimization was attempted.
- Synthetic CI verified in GitHub Actions run [38615999235](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38615999235), source commit `94a72541b0bb607547b5460ff060e9d0a689f02b`.
- The workflow passed Python compilation, all 96 historical engine tests, all 18 temporal sequentiality contract tests, and a clean-source-archive replay of both suites.
- The same suites were replayed from a clean source archive; log evidence records 96 historical tests and 18 temporal contract tests as passing.
- This evidence validates only the tested synthetic implementation and contract cases. It does not validate TGCV scientific claims, empirical inference, or the structural detector.

## Next gate

Next gate: perform an adversarial coverage review of the existing contract suite, focus next on the still-open semantic boundary between a prerequisite that occurred historically and one that must remain currently valid. The existing contract defines historical occurrence within the same sequence; do not strengthen that meaning without a versioned contract decision. Sequence truncation/termination is already covered for exploration, while explicit execution termination remains a separate API question. Do not promote to `main` unless the relevant gates pass and promotion is explicitly selected.
