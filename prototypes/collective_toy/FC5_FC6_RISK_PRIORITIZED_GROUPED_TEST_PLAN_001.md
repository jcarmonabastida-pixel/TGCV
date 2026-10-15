# FC-5 / FC-6 risk-prioritized grouped test plan — 001

- **Status:** proposed test plan; no tests added or executed, no implementation changes.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Inputs reviewed:** full-chain contract, current browser importer and current `ui_contract_test.cjs` FC-5 section.
- **Purpose:** choose a small number of coherent test scenarios that cover multiple acceptance predicates, rather than creating one test per predicate.

## Test design rule

Each test case represents a behavior or risk. Its assertions may map to many acceptance predicates. Keep scenarios diagnostically coherent: assertions in one case should describe one package/contract invariant or one end-to-end flow, not an unrelated collection of fields.

## Priority 0 — resolve policy before implementing dependent tests

### P0-A. Execution trace lifecycle and package optional-artifact policy

**Contract source:** full-chain demonstrator contract, stage 7 says a blocked attempted sequence must remain inspectable; stages 8–10 link outcomes and valuation to an execution and permit valuation to be absent.

**Proposed policy for owner decision (not yet normative):**
- A `COMPLETED` trace may be exported with no outcome; if no assessment exists, package status is `NOT_ASSESSED`.
- A `COMPLETED` trace may have an outcome, and that outcome must link to the exact trace.
- A `BLOCKED` attempted trace must remain inspectable/exportable, but must not carry an outcome claiming a completed observation of that blocked execution.
- A value assessment requires a valid outcome.
- A package without any trace may be valid only when it represents an earlier stage and the package contract explicitly permits stage-partial exports; otherwise require the trace for a full-chain run package.

**Why this needs a decision:** current importer appears to require `COMPLETED` status for any imported trace, while the product contract explicitly requires blocked attempts to remain inspectable. Trace-only and stage-partial package acceptance also affects required fields and the status truth table. Do not add tests with conflicting expectations before the policy is accepted.

## Priority 1 — grouped tests for clear existing risks

### GT-01. Package envelope, canonical integrity, and fail-closed behavior

**Scenario:** start from one valid exported package; mutate the package envelope and recompute the outer digest where appropriate to isolate schema validation.

**Group assertions:** supported package version; required input/result object presence and types; unknown envelope keys rejected; digest format/recomputation; malformed optional artifact types rejected; error is stable and user-readable.

**Covers:** `FC5-PKG-001..012` subsets, existing unknown/missing/unsupported fixtures, plus untested wrong-type/hash cases. Reuse the existing fixture helpers; do not create one file for each field.

### GT-02. Nested result integrity and semantic replay

**Scenario:** export a valid baseline/intervention package, alter one nested result/comparison/delta invariant, recompute outer hashes, then import and replay.

**Group assertions:** scenario keys match input; comparison keys match non-baseline scenarios; closed nested schemas are enforced where specified; state/transition references are valid; trajectories are ordered valid paths; truncation fields and exploration bounds have valid types/ranges; delta fields agree with comparisons and source projections; replay rejects a self-consistent-hash but semantically forged result.

**Covers:** result, scenario, comparison, delta, hash, and replay predicate families. Existing replay tests are retained as baseline. The `delta_reach` nested schema/import checks are a known current gap and may require implementation before this test can pass.

### GT-03. Execution trace semantic coherence

**Scenario:** export one valid completed trace, then create targeted variants: unknown trace/step key; malformed step type/order; transition inconsistent with the model; wrong state-before/state-after; incorrect prior-transition history or prerequisites; forged trace digest.

**Group assertions:** closed trace/step schemas; required field types; sequence is coherent with the input model; history/prerequisites agree with the rule profile; trace digest and outcome cross-links are consistent.

**Covers:** trace and step predicates together. The blocked-trace branch is intentionally excluded until P0-A is decided.

### GT-04. Outcome and valuation as one linked evidence chain

**Scenario:** one valid trace → explicit outcome → contextual assessment package, with variants that break a cross-link or violate the optional assessment policy.

**Group assertions:** outcome schema/types/enumerations; trace/execution/model/scenario links; assessment schema/status/context completeness; outcome digest recomputation; unknown keys rejected; absence of assessment is represented exactly as specified and never silently inferred.

**Covers:** outcome, assessment, and optional-field conditional predicates. Reuse current forged-link, forged-digest, and incomplete-context fixtures; extend them as one coherent chain rather than duplicating all fields.

### GT-05. End-to-end round-trip and deterministic replay

**Scenario:** create a hand-checkable model with alternative routes and a temporal prerequisite; run baseline/intervention; inspect `T_acc`/delta/trajectories; execute a valid sequence; record outcome and optional assessment; export, import, and replay from a clean source.

**Group assertions:** all required artifacts are linked; replayed semantic output matches; per-run IDs may differ where allowed; historical profiles 1/2 remain unchanged; truncation/block reasons are not conflated; synthetic/scientific boundary is explicit.

**Covers:** the cross-stage contract and the core FC-6 clean-source/compatibility acceptance path. Keep focused negative variants in GT-01..GT-04 to preserve diagnosis.

## Priority 2 — evidence and release gate

### GT-06. CI evidence and artifact inspection

On the exact candidate commit, confirm all required workflows pass, clean-source replay succeeds, exported artifacts match the contract, and evidence makes no claim of scientific validity from synthetic tests. Record workflow run IDs and inspected artifact identities in the audit. A documentation commit does not inherit CI evidence for a different code commit.

## Ordering

1. Obtain a decision on P0-A and record it in the contract.
2. Map current fixtures and CI evidence to GT-01..GT-06.
3. Identify which grouped scenarios can pass with current implementation and which expose actual code gaps.
4. Implement only the highest-risk demonstrated gap, in isolation, after the normal development gate.
5. Run required CI on the exact candidate commit and update requirement coverage from the result.

## Current conclusion

The next unit of work is a **test scenario/risk**, not an individual atomic predicate. The acceptance register remains a traceability index; this plan is the proposed test inventory. No tests or code were changed by this document.


## Contract-policy dependency

GT-03 and GT-04 depend on an explicit decision about blocked traces and optional artifacts. The proposal and alternatives are documented in [`FC5_FC6_TRACE_ARTIFACT_POLICY_DECISION_001.md`](FC5_FC6_TRACE_ARTIFACT_POLICY_DECISION_001.md), commit `65fe13daf16001f65db38a5e916909882f8bd663`. It is intentionally a proposal awaiting owner approval; no code/tests were changed and no test expectations should be implemented until the policy is accepted.
