# FC-5 / FC-6 test strategy correction — 001

- Status: strategy clarification; no code changes, no tests added or executed, no scientific execution.
- Branch: `prototype/tgcv-full-chain-001-20261014`.

## Decision

Atomic acceptance predicates make the contract unambiguous and coverage auditable. They do **not** imply one test per predicate. Test granularity follows coherent behavior, system boundaries, and risk. One test can cover multiple predicates; one adversarial case can exercise several contract guarantees. Neither test count nor one-to-one test-to-requirement mapping is a goal.

## Test layers

1. **Contract/schema:** package envelope and coherent nested structures, types, required/optional fields, versions and closed-key policy.
2. **Integration/round-trip:** export → import → integrity checks → independent replay, including optional trace, outcome and assessment artifacts.
3. **Semantics:** trajectories, ordered transitions, prerequisites, reachability deltas and consistency between artifacts.
4. **Adversarial:** targeted risks such as tampered hashes, forged cross-links, unknown nested fields, malformed types, incoherent sequences or conflicting statuses. Prioritize by risk; do not manufacture a separate negative fixture for every field.
5. **Reproducibility/CI:** required workflows and clean-source replay on the exact candidate commit.

## Coverage reporting

Maintain two linked views:

- **Requirement coverage:** each atomic predicate maps to one or more tests/evidence items; each test may map to several predicates.
- **Test inventory:** each test records purpose, scenario/fixture, risk, predicates covered and passing CI evidence.

`verified`, `partial` and `pending` describe evidence strength, not whether a predicate has its own test. Grouped tests are appropriate when assertions remain diagnosable; avoid giant tests that combine unrelated behaviors and obscure failures.

## Effect on current work

The numbered register remains a traceability catalogue. Its row count is not a test count and does not mean the same number of tests must be created. Reconcile its predicates against existing tests and CI, identify the most consequential uncovered risks, and only then add or adjust targeted tests. Reuse the current round-trip, digest, cross-link, envelope and delta tests where coherent.

Resolve the contract policy for `BLOCKED` traces and trace-only packages before writing tests whose expected behavior depends on those decisions.

## Boundaries

- Keep `main` unchanged during this development pass.
- Do not change the graph structural detector or OCR evaluation.
- Do not initiate scientific execution.
- Do not claim synthetic contract conformance as empirical/scientific validation.
