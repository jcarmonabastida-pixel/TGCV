# FC-5 / FC-6 risk-prioritized grouped test plan — 001

- **Status:** approved grouped test plan; policy A approved 2026-10-15. GT-02 nested-delta integrity follow-up passed on exact head `dc76bb6a`; GT-03 trace-coherence adversarial case is implemented and awaiting exact-head CI.
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


### GT-03 third exact-head run — missing-result diagnostic regression and correction

Browser/cross-runtime [run 38765169557](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765169557) failed on commit `76262e9d`. The input validation was moved earlier, but this introduced an ordering regression for a package with no `result`: the importer tried to read `pkg.result.input_sha256` before checking that `result` exists, returning a JavaScript TypeError instead of the contract diagnostic `Falta result o no es un objeto`. The engine, both benchmarks, and governance passed.

Corrective candidate `9f4093d7bd41719ba969d9661d721d6a2bcea692`: check that `pkg.result` is a non-array object immediately after checking `pkg.input` is an object, then verify `input_sha256` and validate the input schema before inspecting derived result fields and deltas. This preserves the package's required-object diagnostic while establishing schema-before-derived-validation precedence.

Exact-head CI pending for `9f4093d7`. GT-03 remains open until all five checks pass and both adversarial diagnostics are observed.


### GT-02 nested-delta integrity follow-up — CLOSED on exact head

The five required checks passed on exact commit `dc76bb6a91cb9e56d75da20fe1b8fcd50889777a`: browser/cross-runtime [38765778802](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765778802), synthetic engine [38765778720](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765778720), engine benchmark [38765778722](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765778722), browser benchmark [38765778819](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765778819), and governance [38765778700](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38765778700). The browser log confirms 116 valid cross-runtime fixtures matched and 102 invalid fixtures were rejected in both runtimes; browser import lifecycle and tamper/replay checks passed. The newly added forged delta source-hash test is included in this successful browser run.

**Naming clarification:** the source-hash binding work previously labeled “GT-03” in intermediate notes is a nested-delta integrity follow-up to GT-02. The canonical GT-03 below remains execution-trace semantic coherence, as defined in the approved test plan. This clarification changes tracking labels only, not scientific claims or implementation.

### GT-03 — execution trace semantic coherence (new grouped adversarial case)

Source review found a narrow gap: `submitted_transition_ids` required non-empty strings but did not require every submitted ID to exist in the input model. For a `BLOCKED` trace, an unknown ID in the unexecuted suffix could pass the generic string check if the trace/package digests were recomputed and the blocked-step metadata agreed.

Implementation candidate: `5fd17ada1e6ad85d2452e4c38bcb3a0ef3693780`. The trace validator now requires each submitted transition ID to exist in the model. Grouped adversarial test candidate: `0075ad15801f46257835f3861f703ba900aacb36`. It constructs a version-2 `BLOCKED` trace with a valid executed prefix and an unknown transition ID at the blocked step, removes outcome/assessment artifacts per policy A, recomputes trace and package digests, and expects a specific rejection.

Exact-head CI pending for the final candidate and documentation commit. GT-03 is not closed until browser/cross-runtime, engine, both benchmarks, and governance all pass on the same exact head and the adversarial diagnostic is observed.


### GT-03 trace-ID adversary — PASSED on exact code head

All five CI checks passed on exact code head `0075ad15801f46257835f3861f703ba900aacb36`: browser/cross-runtime [38766691617](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38766691617), engine benchmark [38766691594](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38766691594), browser benchmark [38766691361](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38766691361), governance [38766691410](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38766691410), and synthetic engine [38766691402](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38766691402). The blocked trace with an unknown submitted transition ID is now rejected by the specific semantic check even when trace/package digests are recomputed.

### GT-03 follow-up — submitted-prefix consistency

Source review found a related but distinct gap: for `BLOCKED` traces, the validator checked that the blocked transition matches the submitted item at `steps.length`, but did not assert that the executed `steps` IDs equal the prefix of `submitted_transition_ids`. A package could therefore describe a valid execution of one sequence while claiming a different submitted prefix, then recompute both digests.

Implementation candidate: `96f54534f647e3461d14476da1f3e0576716e638`. The validator now requires the executed step IDs to equal the submitted sequence prefix for a `BLOCKED` trace. Adversarial test candidate: `fa28718f6fa22b8c892cecb38136380793fa36a8`, which changes the first submitted ID to a different existing transition, preserves the actual executed step and blocked step, recomputes trace/package digests, and expects rejection by the new prefix-consistency diagnostic.

This follow-up remains pending exact-head CI; GT-03 is not closed until the new adversary and full five-check battery pass on the same final head.


### GT-03 submitted-prefix consistency — PASSED on exact code head

All five CI checks passed on exact commit `fa28718f6fa22b8c892cecb38136380793fa36a8`: browser/cross-runtime [38767560269](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38767560269), synthetic engine [38767560551](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38767560551), engine benchmark [38767560295](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38767560295), browser benchmark [38767560224](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38767560224), and governance [38767560534](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38767560534). Browser logs confirm the full import lifecycle passed, with 116 valid fixtures matched and 102 invalid fixtures rejected across runtimes. The tampered submitted-prefix adversary is included in that exact-head browser pass.

### GT-03 follow-up — blocked reason and prerequisite metadata coherence

Source review found that `blocked_step.reason` only needed to be a non-empty string and `required_transition_ids` only needed to contain existing IDs. A forged BLOCKED trace could omit a genuinely missing temporal prerequisite (or provide a false reason) and still pass the metadata shape checks after digest recomputation.

Implementation candidate: `46e6e9fa201e295e9ddd54e172759c0de0b255a0`. The importer derives the expected blocked reason from baseline scenario disablement, current state/source mismatch, and missing temporal prerequisites, and requires `required_transition_ids` to equal the actual missing prerequisite set. Adversarial test candidate: `4145df6788fd441564e83b04d23b5d650eaa9745`, which removes the missing-prerequisite IDs from a temporal-prerequisite BLOCKED trace, recomputes trace/package digests, and expects a semantic rejection.

Exact-head CI pending. GT-03 remains open until the five-check battery passes on the same final head and the new forged-metadata diagnostic is observed.


### GT-03 blocked metadata integrity — PASSED on exact head

The five checks passed on the documentation head `75fd25716d6c5050fec86c3a85c31149f9eb4402`: browser/cross-runtime [38768436194](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38768436194), synthetic engine [38768436177](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38768436177), engine benchmark [38768436292](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38768436292), browser benchmark [38768436253](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38768436253), and governance [38768436201](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38768436201). The browser test confirms a BLOCKED trace that omits a genuinely missing temporal prerequisite is rejected despite recomputed trace and package digests.

### GT-03 paired follow-up — forged blocked reason

Added a paired adversarial test on candidate `4f782d470a4c714672d6983182f43d703785f7d4`: mutate a valid temporal-prerequisite block reason to `transition_source_mismatch`, recompute trace/package digests, and require rejection by the reason/context diagnostic. This complements the missing-prerequisite-list test and checks both dimensions of blocked metadata coherence.

Exact-head CI pending. GT-03 remains open until all five checks pass on the final exact head and both forged-reason and forged-prerequisite diagnostics are observed.


### GT-03 forged blocked reason — PASSED on exact code head

All five checks passed on exact code head `4f782d470a4c714672d6983182f43d703785f7d4`: browser/cross-runtime [38769814881](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38769814881), synthetic engine [38769814846](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38769814846), engine benchmark [38769814892](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38769814892), browser benchmark [38769814827](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38769814827), and governance [38769814806](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38769814806). Browser/cross-runtime logs confirm 116 valid fixtures matched, 102 invalid fixtures rejected in both runtimes, and the full UI import/tamper lifecycle passed. The forged-reason adversary is included in this successful exact-head run.

### GT-03 follow-up — per-step prerequisite metadata coherence

Source review found that `step.prerequisites` was checked against the input relations only under the temporal-prerequisite profile. Under other profiles, any list of existing transition IDs could pass. The validator now requires the step's prerequisite list to equal the relation-derived list for the active profile (empty when the profile does not define temporal prerequisites), and separately checks that all required temporal transitions appear in prior execution history.

Implementation candidate: `5e274ccfde842485ce868c3d85e48403ea6f22f3`. Adversarial test candidate: `87814ca31d3a0aa202441886559cea67e7a2d3e9`; it injects an unrelated existing transition into a step's empty prerequisite list, recomputes trace/package digests, and expects rejection by the profile-coherence diagnostic.

Exact-head CI pending. GT-03 remains open until all five checks pass on the final exact head and the specific forged-step-prerequisite diagnostic is observed.


### GT-03 per-step prerequisite adversary — first CI attempt failed in test setup

On candidate `87814ca31d3a0aa202441886559cea67e7a2d3e9`, four of five checks passed; browser/cross-runtime failed because the adversarial fixture recomputed the trace digest using the wrong hash input contract and did not update the linked outcome/assessment digests. The importer correctly rejected the package earlier at the outcome-to-trace link check, so the run did not yet demonstrate the intended prerequisite diagnostic. This is a test-fixture sequencing issue, not evidence that the new validator check failed.

Follow-up candidate `667a0be18e0f5ce0d491bff0be915651a81335c1` corrects the fixture to hash the trace body according to the validator contract and updates the linked outcome and assessment digests before recomputing the package digest. Exact-head CI pending.


### GT-03 step-prerequisite adversary — diagnostic PASS, harness sequencing defect fixed

The first CI run on the new validator reached the adversarial assertion and correctly rejected the forged per-step prerequisite metadata with the intended diagnostic. The browser job failed only because a later generic FC-5 replay assertion was still executed after the adversarial import had intentionally changed the assessment state to `rejected`. No validator failure was observed.

Harness correction: `0fdf32cd1bc67aa027180aba264edde45368ffcd` scopes that generic replay assertion to the successful round-trip before the adversarial mutation. The adversarial rejection remains explicitly asserted.

A fresh exact-head five-check battery is now required before closing this risk group.


### GT-03 follow-up — trace initial-state binding

Source review found that the importer checked whether a trace initial state existed in the model, but did not require it to equal the model's declared initial state. A forged trace could start at another declared state while keeping the package input/result binding intact. The grouped adversary changes only the trace initial state to another known state and recomputes the trace, linked outcome, assessment, and package digests. The importer now rejects the semantic mismatch with a dedicated diagnostic.

Implementation/test candidate: pending exact-head CI. This risk remains open until all five required workflows pass on the same exact head and the specific diagnostic is observed. No scientific execution is authorized.


### GT-03 trace initial-state binding — PASSED on exact head

All five required workflows passed on exact code head `cd6202508f3423343bed3cb416ce34ffa552ca37`: browser/cross-runtime [38774669264](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38774669264), synthetic engine [38774669433](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38774669433), engine benchmark [38774669242](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38774669242), browser benchmark [38774669184](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38774669184), and governance [38774669274](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38774669274). Browser/cross-runtime logs confirm 116 valid fixtures matched, 102 invalid fixtures rejected in both runtimes, and the full UI import/tamper lifecycle passed. The trace initial-state binding adversary is included in this exact-head pass.

### GT-03 next review item — scenario-context binding for BLOCKED reason

The blocked-reason validator currently derives `transition_disabled_by_scenario` from the model's `baseline` scenario rather than the concrete trace's `scenario_id`. This risks validating a blocked trace against the wrong scenario context. Next iteration: resolve the exact scenario referenced by the trace, derive disabled-transition status from that scenario, and add an adversary proving the reason cannot be validated against baseline when the trace references a different scenario. Do not close GT-03 until the specific diagnostic and all five exact-head checks pass.


### GT-03 next grouped risk — BLOCKED reason bound to trace scenario

The prior validator derived `transition_disabled_by_scenario` from the model's `baseline` scenario even when the concrete trace declared another `scenario_id`. Updated the validator to resolve the trace's declared scenario and derive disablement from that scenario; an absent trace scenario is rejected explicitly. Added an adversarial import that changes baseline/alternate disablement context, points the BLOCKED trace at the alternate scenario, and recomputes linked input/trace/package digests while preserving a temporal-prerequisite block reason. The expected assertion is the scenario-context-specific diagnostic.

Status: implementation and grouped adversary committed; awaiting all five exact-head checks and observation of the specific diagnostic. GT-03 remains open. No scientific execution authorized; main unchanged.


### GT-03 scenario-context attempt 1 — diagnostic assertion mismatch

On exact head `3ec65da09de3bad42b870773468b98b0d9996e6d`, four workflows passed and browser/cross-runtime failed at the pre-existing forged-blocked-reason assertion. The importer rejected the adversarial package with the new, more specific scenario-context diagnostic as intended, but that earlier assertion still expected the previous diagnostic string. This is a test expectation mismatch, not evidence that the semantic rejection failed. Updated the assertion to accept the new scenario-context wording while retaining the legacy wording compatibility. Rerun all five checks on the new exact head; GT-03 remains open until they pass and the dedicated scenario-context adversary also passes.


### GT-03 scenario-context attempt 2 — preserve delta_reach source commitments

On exact head `78838efc3466e30124400a267347116c9a53f623`, four of five controls passed; browser/cross-runtime failed because the adversarial fixture changed scenario disablement but left `result.delta_reach[*].baseline_source_sha256` and `intervention_source_sha256` stale. The importer correctly rejected that earlier inconsistency, so the test never reached the intended BLOCKED-reason diagnostic. Updated the adversary to recompute both delta_reach source commitments for every affected intervention scenario before recomputing input/trace/package digests. This preserves fail-closed validation and makes the adversarial package internally coherent up to the intended assertion. Rerun all five controls on the new exact head; GT-03 remains open.


### GT-03 scenario-context attempt 3 — recompute result integrity

On exact head `664966f8c3032087b116a9e4a683e6afb46dc077`, four controls passed and browser/cross-runtime failed because the adversarial fixture correctly refreshed input, delta_reach source, trace, and package commitments but did not recompute `result.semantic_sha256` and `result.result_sha256`. The importer therefore rejected at result integrity before reaching the intended scenario-context diagnostic. Updated the fixture to recompute semantic projection and result integrity commitments before trace/package digests. Rerun all five controls on the next exact head; GT-03 remains open.


### GT-03 scenario-context attempt 5 — correct adversarial direction

Review of the adversarial fixture exposed an inversion in the test itself: it disabled the blocked transition in `baseline` but removed the disablement from the trace-declared alternate scenario. A validator correctly using `trace.scenario_id` could therefore accept the recorded temporal-prerequisite reason, while the baseline-based validator would reject it—the opposite of the intended discrimination. Corrected the fixture so baseline permits the transition and the trace-declared `block_ac` scenario disables it, while the trace retains the stale `temporal_prerequisite_not_satisfied` reason. This is the intended adversarial direction: a baseline-based validator would accept; a scenario-aware validator must reject with the context-specific diagnostic. Integrity/replay checks must still be satisfied; run the five-control battery before claiming a pass. GT-03 remains open.


### GT-03 scenario-context adversary — PASS on exact code head

Exact code head: `d54bec8e33a7464c91dc6953b22cb6faf742d11c`.

All five required workflows passed on that same SHA:
- Browser and cross-runtime tests: [38780626151](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38780626151) — success.
- Browser performance benchmark: [38780626003](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38780626003) — success.
- Synthetic engine tests: [38780625943](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38780625943) — success.
- Governance current-state consistency: [38780626010](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38780626010) — success.
- Engine performance benchmark: [38780626013](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38780626013) — success.

The browser/cross-runtime test completed successfully with the dedicated GT-03 assertion that the forged BLOCKED reason is rejected with the scenario-context-specific diagnostic after the adversarial fixture reverses baseline/alternate disablement and recomputes the linked digests. This demonstrates the tested validator uses the trace-declared scenario rather than baseline for this case. The adversarial case passes; it does not establish exhaustive FC-5/FC-6 coverage or scientific validity.

GT-03 grouped execution-trace coherence is closed for the currently enumerated cases. Next grouped risk: GT-04, outcome and valuation as one linked evidence chain. Begin with source/fixture audit on the development branch, preserve main, and do not authorize scientific execution. This plan-only update does not inherit the above code-head CI evidence.


### GT-04 source/fixture audit — initial gap identified

Audit performed against code head `d54bec8e33a7464c91dc6953b22cb6faf742d11c` (the five-workflow evidence recorded above). Existing browser contract tests already cover forged outcome execution/model/scenario links and forged assessment execution/outcome links. The importer also checks the outcome schema identifier, assessment schema/status, required non-empty assessment context strings, assessment-to-outcome digest, and the explicit `NOT_ASSESSED` state when assessment is absent.

**Candidate gap for grouped adversarial coverage:** `assessImportedBrowserPackage` validates the required outcome and assessment fields individually but does not currently enforce closed key sets for `outcome_record` and `value_assessment`. It also does not show a separate digest commitment for the outcome record itself; the assessment commits to the outcome through `outcome_sha256`. Before implementation, compare these observations against the approved artifact contract and existing policy/acceptance register. If confirmed, add grouped fixtures for unknown outcome field, unknown assessment field, and outcome/assessment schema/enumeration/type boundary while preserving the already-tested cross-links and optional `NOT_ASSESSED` behavior. Do not relax existing checks or infer value from synthetic data.

This is a source/fixture audit only; no code behavior was changed in this iteration. GT-04 remains open. Main remains unchanged; no scientific execution authorized.


### GT-04 grouped iteration 1 — closed schemas and outcome/assessment boundaries

Contract reconciliation used `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`, the numbered acceptance register, finite schema inventory, and the owner-approved artifact policy. The approved schema inventory explicitly defines a 12-key outcome record and 11-key value assessment; unknown keys and missing required keys are invalid. The UI exposes only `synthetic` and `observed` source kinds. The prior audit's concern about a separate outcome digest was refined: no standalone digest field is required by the contract; when present, the assessment's `outcome_sha256` commits to the outcome record, while the outcome's `execution_trace_sha256` links to the execution trace. Hashes do not prove authenticity.

Implemented on the development branch candidate: closed-key and required-key checks for both artifacts; allowed `source_kind` enumeration; non-empty value/unit/timing/uncertainty/provenance fields; explicit 64-hex trace digest validation; non-empty `assessment_id`. Added grouped adversarial browser fixtures for unknown outcome key, invalid source kind, empty outcome unit, unknown assessment key, and empty assessment ID. Each fixture recomputes the outer package digest to ensure rejection is due to the targeted schema/semantic predicate rather than stale package integrity.

Status: implementation and fixtures are committed as a candidate only; CI and diagnostic confirmation are pending. GT-04 remains open. Preserve historical profile compatibility, main remains unchanged, and no scientific execution is authorized.


### GT-04 iteration 1 — CI diagnostic and fixture correction

The five-workflow batch for candidate `2ceca81321c00dce3c142e679f388c4d535918e3` completed with four workflows passing and the browser/cross-runtime workflow failing. The failure was an existing FC-5 adversary fixture-ordering issue, not a demonstrated defect in the new validator: the test for rejecting an explicit outcome linked to a `BLOCKED` trace constructed an incomplete outcome (it omitted `source_kind`, `unit`, `timing`, `uncertainty_status`, and `provenance`). The newly enforced required-field check correctly rejected the malformed outcome first, so the test never reached its intended assertion that a validly shaped outcome requires a `COMPLETED` trace.

Corrective action: complete the adversarial outcome fixture with all required schema fields while retaining the BLOCKED trace and its matching trace digest. Keep the expected diagnostic `requiere una traza COMPLETED`. This preserves validator strictness and makes the test isolate the intended predicate. Re-run the grouped CI suite on one exact commit; GT-04 remains open until diagnostic-specific checks and all five workflows pass. No scientific execution authorized; main remains untouched.


### GT-04 iteration 2 — browser diagnostic assertion compatibility

The corrected candidate `6aab8a91eaf9c9296fa13b510c06a3361f492c42` completed four of five workflows successfully; the browser/cross-runtime suite failed at an existing FC-5 assertion for an incomplete contextual assessment. The importer rejected the malformed record as intended, but the diagnostic text now says `value_assessment está incompleta.` while the older assertion only accepted `valoración está incompleta`. This is a test-message compatibility mismatch, not evidence that the invalid assessment was accepted.

Correction: allow the assertion to match either the schema field name (`value_assessment`) or the Spanish label (`valoración`), retaining the rejection-state assertion. Re-run all five workflows on one exact commit. GT-04 remains open pending full green CI and diagnostic-specific confirmation. Main remains untouched; no scientific execution authorized.


### GT-04 exact-head CI gate — first complete green batch

All five required workflows passed on exact commit `6f426724e48426b5a525764f592222a13b0a5886`: browser/cross-runtime `38792359668`, synthetic engine `38792359755`, governance consistency `38792359714`, browser benchmark `38792359847`, and engine benchmark `38792360053`. The browser job passed both the browser/Python concordance test and replay from a clean source archive. This confirms the candidate's current engineering gate and the diagnostic-assertion correction; it does not establish scientific validity and does not close GT-04, which retains further grouped boundary risks.

### GT-04 next grouped risk — artifact shape substitutions and NOT_ASSESSED coherence

Next adversarial group targets schema substitution and lifecycle-state coherence: array/null substituted for `outcome_record`, array substituted for `value_assessment`, assessment status set to `NOT_ASSESSED` while a value assessment object is present, and missing assessment paired with a contradictory `value_assessment_status=ASSESSED`. Each mutation recomputes the outer package digest and must be rejected by the intended structural or status diagnostic. These cases complement the existing closed-key, required-field, enum, cross-link, and hash tests. GT-04 remains open until this grouped set and the same five-workflow exact-head gate pass.


### GT-04 iteration 2 — field types and assessment-status domain

The five-workflow exact-head gate passed on `85141c0b7648fc07b25b55001aa81ca6b50a46d9` (runs `38793015720`, `38793016043`, `38793015627`, `38793015667`, `38793015731`). The grouped shape/state mutations are now covered by that green batch; this remains an engineering result, not scientific validation.

Next grouped adversarial set expands field-level type/constraint coverage and status-domain handling: numeric outcome value, object-valued outcome provenance, numeric assessment criterion, empty assessment rationale, and unsupported `value_assessment_status=PENDING` when no assessment object exists. The package digest is recomputed in every mutation so the importer must reject the specific contract violation. These tests map to FC5-OUT-005, FC5-VAL-007, FC5-PKG-012 and FC5-PKG-011. Require targeted diagnostic rejection and all five workflows passing on the same exact commit. GT-04 remains open.
