# Temporal sequentiality profile — implementation record 001

- **Status:** IMPLEMENTED IN DEVELOPMENT BRANCH; TESTS NOT EXECUTED.
- **Date:** 2026-10-14.
- **Branch:** `prototype/sequentiality-test-first-001-20261014`.
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
- No workflow/test execution is claimed. The repository operating gate requires explicit authorization before running CI; this record is documentation, not a PASS.

## Next gate

Review the implementation and test expectations together, authorize the focused synthetic CI, inspect its exact run result, then correct any failures on this branch. Do not promote to `main` unless the relevant gates pass and promotion is explicitly selected.
