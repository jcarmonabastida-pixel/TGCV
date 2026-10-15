# FC-5 / FC-6 risk-prioritized grouped test plan — 001

- **Status:** approved grouped test plan; policy A approved 2026-10-15. No tests added or executed in this documentation iteration.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Inputs reviewed:** full-chain contract, current browser importer and current `ui_contract_test.cjs` FC-5 section.
- **Purpose:** choose a small number of coherent test scenarios that cover multiple acceptance predicates, rather than creating one test per predicate.

## Test design rule

Each test case represents a behavior or risk. Its assertions may map to many acceptance predicates. Keep scenarios diagnostically coherent: assertions in one case should describe one package/contract invariant or one end-to-end flow, not an unrelated collection of fields.

## Priority 0 — approved contract policy; implementation gate remains

### P0-A. Execution trace lifecycle and package optional-artifact policy

**Contract source:** full-chain demonstrator contract, stage 7 says a blocked attempted sequence must remain inspectable; stages 8–10 link outcomes and valuation to an execution and permit valuation to be absent.

**Approved policy (Alternative A):**
- A `COMPLETED` trace may be exported with no outcome; if no assessment exists, package status is `NOT_ASSESSED`.
- A `COMPLETED` trace may have an outcome, and that outcome must link to the exact trace.
- A `BLOCKED` attempted trace must remain inspectable/exportable, but must not carry an outcome claiming a completed observation of that blocked execution.
- A value assessment requires a valid outcome.
- A package without any trace may be valid only when it represents an earlier stage and the package contract explicitly permits stage-partial exports; otherwise require the trace for a full-chain run package.

**Implementation requirement:** current importer appears to require `COMPLETED` status for any imported trace. The accepted policy is now normative in the development contract. The package schema currently lacks an explicit stage field, so introduce a deliberate versioned package schema before accepting stage-partial snapshots. Do not silently extend the closed schema.

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

**Covers:** trace and step predicates together. The blocked-trace branch is now in scope under the approved policy.

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

1. Introduce the versioned package-stage schema and map current fixtures/CI evidence to GT-01..GT-06.
2. Identify which grouped scenarios pass with current implementation and which expose actual code gaps.
3. Implement schema/lifecycle validation as a focused change on the development branch.
4. Reuse existing fixtures and add grouped lifecycle/adversarial coverage for the approved policy.
5. Run required CI on the exact candidate commit and update requirement coverage from the result.

## Current conclusion

The next unit of work is a **test scenario/risk**, not an individual atomic predicate. The acceptance register remains a traceability index; this plan is the proposed test inventory. No tests or code were changed by this document.


## Contract-policy dependency

GT-03 and GT-04 depend on an explicit decision about blocked traces and optional artifacts. The approved decision is documented in [`FC5_FC6_TRACE_ARTIFACT_POLICY_DECISION_001.md`](FC5_FC6_TRACE_ARTIFACT_POLICY_DECISION_001.md). Policy A is approved; code/test changes must still follow the versioned schema and development-branch gates.


## Implementation update: package schema v002

The development branch now emits `collective-toy-browser-run-002` with required `package_stage` (`EXPLORATION`, `EXECUTION`, `OUTCOME`, `ASSESSMENT`), keeps v001 import compatibility, and validates trace/step structure plus the approved blocked-trace lifecycle. Grouped browser tests were added for exploration-stage export, blocked-trace round-trip, and rejection of an outcome linked to a blocked trace. Details: [`FC5_FC6_PACKAGE_SCHEMA_V002_IMPLEMENTATION_001.md`](FC5_FC6_PACKAGE_SCHEMA_V002_IMPLEMENTATION_001.md), commit `29515bea7e0cc5413bfe1c234e83927841bfaa02`.

**Evidence status (updated 2026-10-15):** run [38758570843](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38758570843) passed on exact code commit `f8b6623a8ab316db092cac179966fd337ee29b39`, including browser/Python concordance and clean-source archive replay. The exact run's `browser-cross-runtime` job concluded `success`. See `SCHEMA_ACCEPTANCE_COVERAGE_AUDIT_001.md` for the evidence supplement. This supports the tested lifecycle cases, not exhaustive FC-5/FC-6 coverage or scientific validity. No scientific execution and no changes to `main`.


## Next grouped iteration — GT-02 delta_reach nested integrity

After the schema-v002 lifecycle suite passed on commit `f8b6623a8ab316db092cac179966fd337ee29b39`, source review identified a concrete gap: the browser importer allow-listed `delta_reach` at the result envelope but did not directly enforce its nested closed schema or compare its declared deltas with the exported baseline comparison. Replay could detect some forged content later, but the artifact's own contract should fail closed before replay.

**Implementation candidate:** `7091c39df8acfd4014fdf77dde3d8e4f5e29fa4b`.

Changes:
- Validate that `delta_reach` is an object with exactly the intervention scenario keys.
- Validate exact nested keys, SHA-256 source identifiers, typed/known state and transition IDs, trajectory path structure, and truncation booleans.
- Cross-check each delta against `comparisons_to_baseline` and baseline/intervention truncation flags.
- Add two grouped adversarial cases: unknown nested field with recomputed result/package hashes, and semantically forged reachable-state delta with recomputed enclosing hashes.

**Evidence status:** required CI was observed in progress when this note was written. Do not mark GT-02 passed until the exact candidate run completes successfully. The previous green run remains valid only for its own commit. Preserve the existing profile 1/2 behavior; no scientific execution and no promotion to `main`.


### GT-02 diagnosis and corrective candidate

Run [38759475524](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38759475524) failed in the browser/Python concordance test at `assessInBrowser` while importing the valid profile-1 export. The nested `delta_reach` validation referenced scenario/state/transition indexes before their assignments later in the function; JavaScript hoisting left those variables undefined/empty at the point of validation. This is a validator initialization-order defect, not evidence that the adversarial assertions themselves are incorrect.

Corrective candidate: `bbe63bfa2024dee9befb9478fad6f917a7a2f115`. The scenario IDs, state IDs and transition map are now initialized before the nested `delta_reach` checks, with duplicate later declarations removed. New exact-head browser/cross-runtime run: [38760661746](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38760661746) (queued at time of note). Synthetic-engine tests, both performance benchmarks, and governance consistency have also been triggered on this exact commit and are pending. Do not mark GT-02 passed until the browser/cross-runtime run completes successfully.


### GT-02 second failure and diagnostic improvement

Run [38760661746](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38760661746) still failed in `cross_runtime_test.cjs` at the first valid-package import. The previous timeout only reported that the expected assessment had not appeared; it concealed the actual terminal rejection message. The earlier initialization-order defect is not yet shown to be the only cause.

Corrective test-instrumentation commit: `d737081841e7f2ff1db25339b6411573fc71a2c4`. The browser test now waits for a terminal assessment state and reports the actual state/message when it differs from expectation, rather than waiting for a particular expected state until timeout. This is diagnostic only; it does not relax package validation.

Exact-head CI is queued: browser/cross-runtime [38761076420](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761076420), synthetic engine [38761076359](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761076359), browser benchmark [38761076224](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761076224), engine benchmark [38761076451](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761076451), governance [38761076190](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761076190). Next step: inspect the diagnostic message from the browser/cross-runtime run, then fix only the demonstrated cause. GT-02 remains unverified.


### GT-02 third failure — diagnostic precedence

Run [38761131177](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761131177) exposed the terminal message: an existing adversarial case deliberately removes `input.initial_state`, but the new `delta_reach` trajectory check rejected the derived trajectory first. The importer's stricter check masked the primary input-schema diagnostic expected by the test. This is a validation-order/diagnostic-precedence issue, not evidence that the valid profile-1 package is rejected.

Corrective candidate: `ee783af3d80f1643ca7c33482ce433af4b386335`. The delta trajectory arrays remain type-checked unconditionally; path semantics are checked when `input.initial_state` identifies a valid state, matching the existing scenario/comparison validators. The input's invalid initial state remains rejected by the existing primary validation path. Exact-head CI must pass before GT-02 can be marked verified.


### GT-02 fourth failure — validation precedence between comparison and delta artifacts

Run [38761578722](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38761578722) passed the earlier malformed-initial-state case but exposed another precedence conflict. An existing adversarial fixture corrupts `comparisons_to_baseline.reachable_states_added` with an undeclared state ID; the new `delta_reach` comparison then fails first with `delta_reach de block_ac no coincide con la comparación baseline exportada`, masking the intended primary error `IDs de estado declarados`.

Corrective candidate commit: `d725a88a7189e9f03766c46f474de295f93e562e`. The entire nested `delta_reach` validation block is moved to run after the comparison objects have passed their own structural and reference checks, but before trace/result completion. This preserves primary input/comparison diagnostics while still rejecting a semantically forged delta after its source comparison is valid.

Exact-head browser/cross-runtime CI must pass before GT-02 can be considered verified. No scientific execution and no promotion to `main`.


### GT-02 closure — nested delta_reach schema and semantic linkage

**Exact-head evidence:** commit `d725a88a7189e9f03766c46f474de295f93e562e`. Browser/cross-runtime [run 38762211152](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38762211152), engine benchmark [38762211164](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38762211164), browser benchmark [38762211381](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38762211381), synthetic engine [38762211379](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38762211379), and governance consistency [38762211439](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38762211439) all concluded `success`.

This closes GT-02 for the implemented predicates on that exact head: nested closed schema, state/transition references, trajectory structure, delta/comparison consistency, truncation flags, and preservation of primary validation diagnostics. It is not exhaustive FC-5/FC-6 closure.

### GT-03 — bind delta source hashes to their declared source scenarios

Source review found that `baseline_source_sha256` and `intervention_source_sha256` were only checked for 64-hex syntax. A forged but well-formed hash could pass the local schema checks until independent replay. The importer should directly bind each source hash to the canonical common model plus its named baseline/intervention scenario.

Implementation candidate: `cf3fb58feaa877746c7dba6522dca3b3888ed2c6`. Added direct recomputation of both source hashes from the imported input. Added a grouped adversarial test that substitutes a syntactically valid all-zero baseline hash, recomputes enclosing result/package hashes, and expects rejection specifically for source mismatch.

**Exact-head CI pending:** browser/cross-runtime [run 38763028937](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763028937), synthetic engine [38763028995](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763028995), engine benchmark [38763029013](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763029013), browser benchmark [38763029216](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763029216), governance [38763029220](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763029220). The test-only follow-up is commit `36356576ab2fb806448eac47bfa965b0b6cdd85d); its exact-head CI is also pending. GT-03 must not be marked passed until the final exact-head suite completes successfully.


### GT-03 first exact-head run — JavaScript parse failure and correction

The first GT-03 test-head browser/cross-runtime run [38763028937](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763028937) and browser benchmark [38763029216](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763029216) failed before the relevant importer tests. The relation-editor selects remained empty because the newly added `await hash(...)` expressions were inside a synchronous `Object.keys(deltaReach).forEach(function(id){...})` callback, which makes the browser script syntactically invalid. The other engine and governance checks passed, but this did not validate GT-03.

Corrective candidate: `8fa0534e83ad89d5918abb2d41377c8f91c44ab9`. Replaced the synchronous callback with an awaited `for...of` loop so source-hash assertions execute sequentially and failures propagate from `assessImportedBrowserPackage`.

Exact-head CI now running: browser/cross-runtime [38763755117](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763755117), engine [38763755037](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763755037), engine benchmark [38763754769](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763754769), browser benchmark [38763755131](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763755131), governance [38763755040](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763755040). GT-03 remains unverified until the browser/cross-runtime and benchmark jobs finish green on this exact head.


The awaited-loop candidate [8fa0534e](https://github.com/jcarmonabastida-pixel/TGCV/commit/8fa0534e83ad89d5918abb2d41377c8f91c44ab9) fixed the parse failure, but browser/cross-runtime [run 38763755117](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763755117) then exposed a second ordering issue: a malformed `rule_profile` was rejected by the derived delta source-hash check before the input schema validator, masking the expected `rule_profile no compatible` diagnostic. The browser test is now executing and the engine/governance checks pass, but GT-03 is still not validated.

Corrective candidate: `152c30b72230cc7ca8c7dcf4397fc758630d7564`. The imported input schema validation is moved to immediately after verifying `input_sha256`, before result/delta structural and semantic validation. This makes the declared input contract primary while retaining source-hash recomputation for structurally valid inputs.

Exact-head CI pending: browser/cross-runtime [38763981926](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763981926), engine [38763981902](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763981902), engine benchmark [38763981914](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763981914), browser benchmark [38763981900](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763981900), governance [38763982025](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763982025).


### GT-03 second precedence failure and correction

Browser/cross-runtime [run 38763981926](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38763981926) failed on the malformed `rule_profile` adversarial fixture. Although `validate(pkg.input)` had been moved before replay, it still ran after the nested `delta_reach` validation (the input hash/schema block was near the end of the importer), so a stale delta source hash masked the expected `rule_profile no compatible` error. Engine, both benchmarks, and governance passed on the same head.

Corrective candidate commit: `5c4202ad06f266604f6ffae786634c282977eeaf`. The importer now checks the declared input hash and validates the input schema immediately after confirming `pkg.input` is an object, before inspecting derived result/comparison/delta structures. The later duplicate input hash/schema block was removed. This preserves integrity checks while establishing the intended validation precedence.

Exact-head CI pending for `5c4202ad`; GT-03 remains open until browser/cross-runtime, engine, both benchmarks, and governance all complete successfully and the forged-source-hash adversarial assertion is observed.


### GT-03 third precedence failure — validation was still below result-field checks

Browser/cross-runtime [run 38764688276](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38764688276) failed with the exact diagnostic `baseline_source_sha256 de delta_reach en block_ac no corresponde a la fuente del escenario baseline`, while the adversarial fixture expected `rule_profile no compatible`. Engine, engine benchmark, browser benchmark, and governance passed on commit `5c4202ad`.

Inspection showed the previous move was ineffective: `validate(pkg.input)` still sat after result/comparison/delta checks (around the end of the importer). Corrective candidate `76262e9d3068a9e6d50f6d997c79cf55c6c26a59` now moves input-hash verification and schema validation immediately after confirming `pkg.input` is an object, before any result-field or delta checks.

Exact-head CI pending for `76262e9d`. GT-03 remains open until all browser/cross-runtime, engine, both benchmark, and governance jobs pass on this exact head, including the forged-source-hash rejection test.
