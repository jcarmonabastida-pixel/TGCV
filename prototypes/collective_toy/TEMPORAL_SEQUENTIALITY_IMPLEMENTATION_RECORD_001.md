# Temporal sequentiality profile — implementation record 001

- **Status:** SYNTHETIC CONTRACT SUITE PASS on tested source commit `a40878c75faf9087386d4dde77ecc0e64615c7fc`; not a scientific validation.
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
- Synthetic CI verified in GitHub Actions run [38610656773](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38610656773), source commit `a40878c75faf9087386d4dde77ecc0e64615c7fc`.
- The workflow passed Python compilation, all 96 historical engine tests, all 11 temporal sequentiality contract tests, and a clean-source-archive replay of both suites.
- The same suites were replayed from a clean source archive; log evidence records 96 historical tests and 11 temporal contract tests as passing.
- This evidence validates only the tested synthetic implementation and contract cases. It does not validate TGCV scientific claims, empirical inference, or the structural detector.

## Next gate

Next gate: perform an adversarial coverage review of the existing contract suite, especially repeated prerequisites, cyclic paths, missing/duplicate relation identifiers, and sequence truncation/termination. Add tests only where a concrete uncovered contract is established. Do not promote to `main` unless the relevant gates pass and promotion is explicitly selected.
