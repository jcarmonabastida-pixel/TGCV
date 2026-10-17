# FC-5 / FC-6 risk-prioritized grouped test plan — 001

- **Status:** approved grouped test plan; policy A approved 2026-10-15. GT-02 nested-delta integrity follow-up passed on exact head `dc76bb6a`; FC5-TRACE-017's two BLOCKED lifecycle predicates passed on exact test head `1813498d4adf3aa33ae5d6de63ee531acd2e867a`.
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


### GT-04 lifecycle truth table — browser evidence PASS; full acceptance gate pending

On exact candidate commit `8c61ba4b22a21041aee87dbe4b380c7a3bd23c61`, browser/cross-runtime workflow [38924503511](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38924503511) completed with conclusion `success`. The same job ran the browser/Python concordance and clean-source archive replay; both executions logged 116 valid fixtures matched, 102 invalid fixtures rejected in both runtimes, and the UI import/tamper lifecycle passed. The active grouped GT-04 assertions specifically verify: (1) COMPLETED trace without outcome remains EXECUTION/NOT_ASSESSED and independently replays; (2) assessment without outcome is rejected; (3) ASSESSED status without a valuation artifact is rejected; and (4) a complete valuation combined with NOT_ASSESSED is rejected. The broader lifecycle suite also round-trips a BLOCKED trace without outcome and rejects an outcome attached to BLOCKED trace.

This is **browser/cross-runtime evidence**, not yet the complete GT-04/FC-6 closure gate: the required exact-head workflow set and the acceptance-register reconciliation still need confirmation on this same SHA. GT-03's C12 closure is treated as prior evidence for this workstream; its obsolete scenario-context harness is no longer in the active test file. No scientific execution; no promotion to `main`.


### GT-05 continuation — evidence map after GT-04 recovery (2026-10-16)

Exact current candidate SHA at the start of this review: `0deec788f2ae8c958c6f20fac478ec83c412507a`. Browser/cross-runtime workflow [38925343766](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38925343766) completed successfully on that SHA, including the clean-source archive replay. Its logs confirm 116 valid fixtures matched exactly and 102 invalid fixtures were rejected in both runtimes; UI lifecycle/import/tamper checks passed. This is reusable baseline evidence, not proof that every GT-05 acceptance assertion is covered.

**Existing coverage reusable for GT-05:** FC-4 executes baseline/intervention and checks explicit `delta_reach` provenance/truncation; the positive package fixture links a concrete execution trace, outcome and contextual assessment; grouped negative cases tamper outcome/assessment links, digests, schema and trace coherence; CI performs a clean-source replay.

**Remaining GT-05 gaps (do not mark accepted yet):** (1) no single named acceptance scenario currently asserts the complete ordered walkthrough from hand-checkable alternative-route + temporal-prerequisite model through `T_acc`, `delta_reach`, candidate trajectories, concrete execution, outcome, contextual value, export/import and independent semantic replay; (2) `FC5-TRACE-012` remains pending in the register because an independent semantic trace validator has not been mapped; (3) the replay-mismatch negative and historical profile 1/2 compatibility matrix are only partial. Next code/test iteration should add one grouped GT-05 end-to-end assertion reusing the current valid package fixture, then target only the gaps exposed by that run. Do not duplicate every atomic field test and do not weaken production validation. No scientific execution; no promotion to `main`.


### GT-05 grouped semantic-trace adversary added (2026-10-16)

Commit `9001838676306aea4a3f10be8b9914d3729b3a21` adds one grouped negative case in `web/ui_contract_test.cjs`: it changes a concrete trace step's destination to a declared but non-adjacent state, then recomputes the trace digest, outcome linkage digest, and package digest. Acceptance requires the importer to reject the semantic edge/state mismatch, not merely a stale checksum. This directly targets pending `FC5-TRACE-012` while reusing the assessed FC-4 package fixture; it does not add an atomic test per field and does not modify the production validator. Status remains pending until CI passes on the exact commit. No scientific execution; no promotion to `main`.


### GT-05 replay-divergence adversary added (2026-10-16)

Commit `3d1e8019dc273b3694c816240f75e348db1fd773` adds a grouped negative case that changes the exported scenario result while recomputing the semantic digest, result digest, and package digest. The importer must reject because independent replay differs from the exported result, not because a stale checksum was detected. This targets `FC5-REPLAY-002`; exact-head CI is pending. No production code changed; no scientific execution; no promotion to `main`.


### GT-05 replay-divergence result and next compatibility gap (2026-10-16)

The self-consistent replay-divergence adversary passed in browser/cross-runtime workflow [38929033347](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38929033347) on exact candidate SHA `0c0cecdd73502fb9699e89ed598e1eab141c516a`. The test changed the exported result and recomputed semantic/result/package digests; import was rejected because independent replay diverged. `FC5-REPLAY-002` is now verified.

Next grouped gap: complete the documented package/engine compatibility matrix. Existing checks cover an unknown engine as inspect-only/no replay and an unsupported package schema as reject-even-with-recomputed-digest; `FC5-REPLAY-003` (legacy/optional semantic identity compatibility) and the historical profile matrix remain partial. Add only the missing compatibility case(s), using the policy's fail-closed semantics; do not infer backwards compatibility or silently adapt historical data. Browser/cross-runtime workflow is green on the exact SHA above; this is not evidence that every required workflow or all GT-05 acceptance is complete. No scientific execution; no promotion to `main`.


### Historical package compatibility test added (2026-10-16)

Commit `f4ebda1935bb7dbbea55bc08109392c4da00e886` adds a grouped GT-05 test for the explicitly supported historical package schema `collective-toy-browser-run-001`: removes `package_stage`, `delta_reach`, and optional semantic-identity fields, recomputes result/package digests, imports, and requires `replay-verified` under the validator's documented legacy projection. This tests only the compatibility path declared by `PACKAGE_REPLAY_COMPATIBILITY_POLICY_001.md`; it does not imply general backwards compatibility. Exact-head CI is pending. No production code changed; no scientific execution; no promotion to `main`.


### Historical replay fixture: first CI failure and correction (2026-10-16)

The first historical-v1 test attempt timed out while waiting for `replay-verified` ([run 38930163710](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38930163710)); diagnosis found the fixture hashed the wrong result projection by including `input_sha256`. Commit `b7a295429593c6caa18055be51acb878963b92bb` corrected the fixture digest projection. The follow-up diagnostic exposed a separate contract issue: a legacy-shaped package without explicit `value_assessment_status=NOT_ASSESSED` is rejected. The grouped adversary was then changed to assert fail-closed rejection and its diagnostic; this passed in [run 38931716530](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38931716530) on SHA `4207f3f87bdbbae5dea6b4e643d3f87c9c12299a`. This does not establish successful replay or general historical-profile compatibility; the broader compatibility matrix remains partial.


### GT-05 legacy-shaped package fail-closed result (2026-10-16)

The grouped legacy-package adversary passed in browser/cross-runtime run [38931716530](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38931716530) on exact SHA `4207f3f87bdbbae5dea6b4e643d3f87c9c12299a`. The fixture omits the required explicit `value_assessment_status=NOT_ASSESSED` field and asserts that import reaches a terminal `rejected` state with a diagnostic naming the missing status. This verifies fail-closed rejection of this incomplete legacy-shaped package only; it does not establish successful replay for historical profiles or general backwards compatibility. No production validator changed; no scientific execution; no promotion to `main`.

### FC-6 required-workflow gate (2026-10-16)

The five required controls were all triggered and passed on exact candidate SHA `ff39f0cd94980ea2d8228f3ca1f2b8ad83bc5441`: engine [38934182862](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38934182862), browser/navigation + cross-runtime [38934182858](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38934182858), engine performance [38934182825](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38934182825), browser performance [38934182807](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38934182807), and governance [38934182740](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38934182740). This satisfies the required-workflow gate for that SHA only. A later commit must receive a fresh exact-SHA gate before final closure. Do not infer scientific validity from synthetic tests or engineering benchmarks.


### FC-5 lifecycle truth-table result (2026-10-17)

Commit `5c11cfa34a5030a31df88c3ef1859e783efae276` adds a grouped 32-row matrix crossing four `package_stage` values with all eight presence combinations for `concrete_execution_trace`, `outcome_record`, and `value_assessment`. The test accepts exactly the four expected stage/artifact combinations, rejects the other 28, and checks `value_assessment_status` conditionality. All five required workflows passed on that exact SHA: engine [38981171858](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171858), browser/cross-runtime [38981171964](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171964), engine performance [38981171928](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171928), browser performance [38981171867](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171867), governance [38981171846](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38981171846). The matrix closes the structural lifecycle conditionality gap only; it does not validate scientific outcome/value semantics. No scientific execution; no promotion to `main`.


### GT-02 delta_reach nested-schema adversaries — result (2026-10-17)

Test commit `45871566cbd4d5ba209cd3aa68650ca8d78e20d5` adds seven grouped import adversaries for missing intervention delta, forbidden baseline delta, malformed source hash, undeclared state reference, invalid trajectory edge, non-boolean truncation, and aggregate truncation mismatch. Each case recomputes result/package hashes so rejection must come from the nested `delta_reach` invariant. All five required workflows passed on that exact test commit: synthetic engine [39036611795](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39036611795), browser/cross-runtime [39036611900](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39036611900), engine benchmark [39036611801](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39036611801), browser benchmark [39036611802](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39036611802), governance [39036611835](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39036611835).

Acceptance register reconciled narrowly: FC5-DELTA-001/002/003/004/006/007/008/009 are verified for the named predicates on that test head; FC5-DELTA-005 remains partial because explicit added/removed transition-ID adversaries are still unmapped; FC5-DELTA-010 remains pending because a dedicated orphan-delta-without-comparison case is not isolated. This closes only the targeted GT-02 delta nested-schema follow-up, not all FC-5/FC-6 acceptance or GT-05. The register update is a documentation-only commit and must receive its own exact-head required-workflow gate. No scientific execution; no promotion to `main`.


### GT-02 follow-up — transition references and orphan delta (2026-10-17)

Candidate test commit `6b0076891f307e79e21de3cca362d30396514ba9` adds grouped adversaries for an undeclared transition in `enabled_at_initial_added`, an undeclared transition in `enabled_at_initial_removed`, and a delta whose matching `comparisons_to_baseline` entry is removed. The orphan fixture refreshes semantic identity, result digest, and package digest so the importer reaches the intended missing-comparison invariant rather than rejecting stale hashes. All five required workflows passed on that exact test commit: synthetic engine [39037360464](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037360464), browser/cross-runtime [39037360425](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037360425), engine benchmark [39037360497](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037360497), browser benchmark [39037360445](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037360445), governance [39037360566](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037360566).

The acceptance register now marks `FC5-DELTA-010` verified for the specific missing-comparison predicate. `FC5-DELTA-005` remains partial because explicit added/removed transition references are covered for enabled-at-initial arrays, but the complete predicate wording also includes other transition delta lists and those need review/mapping before claiming full coverage. This closes the targeted GT-02 follow-up only, not all FC-5/FC-6 or GT-05. This documentation commit requires a fresh exact-head gate. No scientific execution and no promotion to `main`.


### GT-03 trace metadata/sequence adversaries — result (2026-10-17)

Test commit `40ac7a1810df98459891b475bb47ad8b06dd2cad` adds grouped cases for an unknown trace key, negative candidate index, undeclared submitted transition, out-of-order step index, and inconsistent `prior_transitions` history. Each fixture refreshes trace/outcome/assessment/package dependent digests so the assertion reaches the intended trace invariant. All five required workflows passed on that exact test commit: synthetic engine [39037992894](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037992894), browser/cross-runtime [39037992892](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037992892), engine benchmark [39037992884](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037992884), browser benchmark [39037992910](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037992910), governance [39037992913](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39037992913).

Acceptance register updated narrowly: `FC5-TRACE-002`, `006`, `011`, and `013` are verified for the tested predicates; `FC5-TRACE-007` is partial because the undeclared-ID case does not establish the full wrong-type/string-array matrix. This does not close trace lifecycle policy, step schema/type coverage, prerequisites, initial/final-state validation, or outcome cross-links as a whole. The documentation update requires a fresh exact-head workflow gate. No scientific execution and no promotion to `main`.


### GT-04 outcome/assessment semantic adversaries — result (2026-10-17)

Test commit `20cc48ed7366db9ab200faf34b625382c05adb7c` adds eight grouped cases: invalid `outcome_record.source_kind`; blank `unit`, `timing`, and `provenance`; invalid `value_assessment.status`; blank `observer`, `context`, and `criterion`. Dependent assessment/outcome/package digests are refreshed so validation reaches the intended semantic predicate. All five required workflows passed on that exact test commit: browser/cross-runtime [39038603637](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603637), engine [39038603600](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603600), engine benchmark [39038603592](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603592), browser benchmark [39038603602](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603602), governance [39038603626](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603626).

Register updated narrowly: `FC5-OUT-004` and `FC5-VAL-003` verified for the tested predicates; `FC5-OUT-005` and `FC5-VAL-007` remain partial because not every field/type/domain constraint is covered. Existing lifecycle matrix remains evidence for structural stage/artifact conditionality, not a substitute for semantic outcome/value validation. This documentation commit requires a fresh exact-head gate. No production code changed; no scientific execution; no promotion to `main`.


### GT-04 cross-link audit — existing coverage mapped (2026-10-17)

Audit of `ui_contract_test.cjs` found that the named FC5-TRACE-019 / outcome-to-trace linkage predicates already have explicit grouped adversaries: mismatched outcome execution ID, model ID, scenario ID, and trace digest; plus assessment execution/outcome identity and outcome digest mismatch. The fixtures assert targeted rejection; these should not be duplicated. The acceptance register now maps FC5-TRACE-019 to this existing evidence using the exact test head `20cc48ed7366db9ab200faf34b625382c05adb7c`, whose five required workflows passed (browser/cross-runtime [39038603637](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603637), engine [39038603600](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603600), engine benchmark [39038603592](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603592), browser benchmark [39038603602](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603602), governance [39038603626](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39038603626)).

This mapping closes only the named linkage predicates, not all trace policy/schema requirements. Next risk-ranked item: GT-05 single-scenario end-to-end round-trip coverage; FC5-SEC-001/002 and final artifact inspection also remain open. This documentation update requires its own exact-head gate. No production code changed, no scientific execution, no promotion to `main`.


### GT-05 single-scenario full-chain gap confirmed (2026-10-17)

All five required workflows passed on the prior documentation commit `260297e782523988f7191064c7b3cd16a3aedba9`: browser/cross-runtime [39039276777](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39039276777), synthetic engine [39039276781](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39039276781), engine benchmark [39039276833](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39039276833), browser benchmark [39039276724](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39039276724), governance [39039276709](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39039276709).

Review of the current browser contract test found that clean-source replay, lifecycle truth-table, blocked trace, hash-consistent semantic tampering, and imported package validation already have tests. However, the FC-4 UI-originated run explicitly clicks `Cargar ejemplo`, a multi-scenario fixture. The evidence does not establish the specific GT-05 acceptance path: a single-scenario model created or selected in the UI, exploration, a concrete ordered transition sequence, explicit outcome, optional contextual assessment, export, clean re-import, and deterministic replay. This is a genuine coverage gap, not a reason to duplicate existing imported-package adversaries.

Added acceptance item `GT-05-E2E-001` as pending and clarified `FC5-REPLAY-001` only covers the existing replay predicate. Next implementation should add one focused UI-originated single-scenario round-trip fixture, asserting scenario cardinality = 1 and checking artifact links/digests/replay state. Preserve the existing multi-scenario FC-4 test; no production changes until a test demonstrates a specific mismatch. This register/plan documentation commit requires fresh exact-head CI. No scientific execution or promotion to `main`.


### GT-05-E2E-001 result — single-scenario UI round-trip PASS (2026-10-17)

Test fix `20e8c56748e22bcd2513486dd60d4a8b5bc13503` opens the advanced editor before entering the one-scenario fixture. The exact-head browser/cross-runtime workflow passed, including both the browser contract suite and replay of browser/Python suites from a clean source archive: [39040191874](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39040191874). The other four required workflows also passed on this exact SHA: synthetic engine [39040191836](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39040191836), engine performance [39040191783](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39040191783), browser performance [39040191821](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39040191821), governance [39040191909](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39040191909).

The grouped test now proves this specific path: UI model input with exactly one scenario; exploration; concrete ordered transition `t_ab` from A to B; outcome creation; contextual assessment; export of an `ASSESSMENT` package; scenario cardinality and trace/outcome/assessment linkage/digest assertions; clean file import and independently verified deterministic replay. Register marks `GT-05-E2E-001` and `FC5-REPLAY-001` verified within this tested synthetic fixture's scope. It does not establish scientific validity, every package/profile compatibility, or all remaining GT-05 criteria. No production code changed, no scientific execution, no promotion to `main`.

This acceptance-register/plan update is documentation-only and must itself receive a fresh exact-head five-workflow gate.


### GT-05 temporal full-chain success path — result (2026-10-17)

The grouped test at exact test SHA `c62c13c8bb97e91506e3da7ea67a37e4d981654c` exercises a successful temporal prerequisite path, not just rejection of an invalid order. Model profile `temporal_prerequisite_graph` requires `t_ab` before `t_cd`; the accepted concrete sequence is `t_ab → t_bc → t_cd` on the same trajectory. The test verifies exploration contains that path, concrete execution is `COMPLETED` / `replay-verified`, outcome and contextual assessment are recorded, the exported package has stage `ASSESSMENT` and consistent artifact links, and clean re-import independently reproduces it.

All five workflows passed on the exact test SHA: browser/cross-runtime [39041867237](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39041867237), engine [39041867225](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39041867225), engine performance [39041867194](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39041867194), browser performance [39041867204](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39041867204), governance [39041867241](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39041867241).

This closes the specific positive-path gap for the exercised deterministic temporal fixture. It does not close the broader inventory of temporal semantic adversaries or imply scientific validity. No production changes, no scientific execution, no promotion to `main`. Register/plan documentation changes require a fresh exact-head gate.


### FC5 trace input binding and digest adversaries — result (2026-10-17)

Test commit `478954eada00597d6f1c592ed4f6002c91a71f7b` adds three grouped negative cases for the imported concrete trace: a mismatched `input_sha256` after refreshing dependent digests; malformed `trace_sha256`; and a well-formed but incorrect 64-hex trace digest. Each asserts the intended trace-specific rejection. All five workflows passed on the exact test SHA: governance [39042797222](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39042797222), engine [39042797232](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39042797232), engine benchmark [39042797223](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39042797223), browser benchmark [39042797229](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39042797229), browser/cross-runtime [39042797231](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39042797231).

This closes only the named FC5-TRACE-004 mismatch and FC5-TRACE-018 digest format/recomputation predicates. The acceptance register and plan updates require a fresh exact-head five-workflow gate. No production changes, no scientific execution, no promotion to `main`.


### FC5-TRACE-005 — undeclared scenario reference rejected (2026-10-17)

The grouped browser adversary changes a BLOCKED trace's `scenario_id` to an undeclared identifier, recomputes trace and package digests, and asserts the targeted diagnostic `scenario_id de la traza no existe en la entrada.` The initial run found an assertion-message mismatch, not a validator defect; the assertion was aligned in test commit `30249281e11ad4d8cf225365c9b0ae4df13b0ef5`. All five workflows passed on that exact head: browser/cross-runtime [39043819831](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39043819831), engine [39043819794](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39043819794), engine benchmark [39043819813](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39043819813), browser benchmark [39043819903](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39043819903), governance [39043820036](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39043820036).

This verifies only the specific undeclared-scenario predicate. The register and plan changes are documentation-only and require a new exact-head five-workflow gate. No production changes, no scientific execution, no promotion to `main`.


### FC5-TRACE-017 — grouped BLOCKED lifecycle adversaries passed (2026-10-17)

On exact test SHA `1813498d4adf3aa33ae5d6de63ee531acd2e867a`, the browser suite rejects a BLOCKED trace whose block index does not follow the executed prefix and a trace whose `final_state` is a valid declared state but does not equal the last valid state in the trace. The fixture was corrected after the first browser run showed that an undeclared forged state was caught earlier by state-membership validation; no production code changed. All five required workflows passed on that same SHA: browser/cross-runtime [39045108880](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045108880), synthetic engine [39045108879](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045108879), engine benchmark [39045108860](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045108860), browser benchmark [39045108853](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045108853), governance [39045108856](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045108856).

Scope is limited to these two predicates. GT-03's blocked-reason and missing-prerequisite adversaries are distinct checks; the full trace schema/type matrix remains incomplete. Documentation-only update; this commit needs its own exact-head gate. No scientific execution and no promotion to `main`.


### FC5-TRACE-016 — grouped COMPLETED lifecycle adversaries passed (2026-10-17)

The browser test on exact SHA `b00058d84b176ffc8c6ee2dd5e911b147442753e` rejects both a `COMPLETED` trace with a non-null `blocked_step` and a `COMPLETED` trace whose declared-valid `final_state` disagrees with the final state of the executed steps. The test recomputes trace and package digests so rejection exercises lifecycle semantics. All five workflows passed on that exact test SHA: browser/cross-runtime [39045767789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767789), synthetic engine [39045767741](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767741), engine benchmark [39045767743](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767743), browser benchmark [39045768012](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045768012), governance [39045767739](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767739).

Scope is limited to the two named predicates. Full trace schema/type coverage remains incomplete. Documentation-only update; no production change, scientific execution, or promotion to `main`. This commit needs its own exact-head five-workflow gate.


### FC5-TRACE-015 — policy A evidence reconciliation (2026-10-17)

The lifecycle policy decision is already explicit in the contract § trace lifecycle: `COMPLETED` and `BLOCKED` traces are exportable/inspectable; `COMPLETED` may exist without an outcome; outcome requires `COMPLETED`; `BLOCKED` must not carry an outcome/assessment representing a completed observation. Existing grouped browser tests cover blocked-trace round-trip, rejection of outcome linked to BLOCKED, and COMPLETED-without-outcome mapped to EXECUTION/NOT_ASSESSED. They passed on exact test SHA `b00058d84b176ffc8c6ee2dd5e911b147442753e` with all five workflows: browser [39045767789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767789), engine [39045767741](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767741), engine benchmark [39045767743](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767743), browser benchmark [39045768012](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045768012), governance [39045767739](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767739).

No new test is needed solely to repeat the existing policy decision. Register reconciliation only; the broader trace schema/type matrix remains open. This documentation change needs its own exact-head gate.


### CI gate reconciliation — historical SHA `306139776f21a4c25b482dbb01210976ed965707` (2026-10-17)

The prior gate on `3061397` had four successful workflows but no governance run associated with that exact SHA. To avoid leaving the record inconsistent, rerun the complete five-workflow gate on the current experimental branch head, which contains the same inventory/policy reconciliation plus the subsequent grouped trace-step adversaries. This is a superset revalidation, not a claim that a run occurred on the historical SHA. Record the exact new SHA and all five run URLs after completion. No changes to `main`, no scientific execution, and no promotion.


### CI gate reconciliation — five-workflow revalidation passed (2026-10-17)

The revalidation commit `0ee9896fc1fde233b72284a028d6c19d71b927c9` passed all five required workflows on the exact same SHA: governance [39050668873](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39050668873), synthetic engine [39050668957](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39050668957), browser/cross-runtime [39050668886](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39050668886), engine benchmark [39050668871](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39050668871), browser benchmark [39050668949](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39050668949). This revalidates the current experimental branch state, including the inventory/policy reconciliation and subsequent grouped trace-step adversaries. It is not retroactive evidence that governance ran on historical SHA `306139776f21a4c25b482dbb01210976ed965707`; the historical gate remains documented as incomplete at that exact SHA. No `main` changes, scientific execution, or promotion.


### FC5-TRACE-017 — BLOCKED metadata schema extension passed (2026-10-17)

The existing grouped BLOCKED lifecycle suite now also rejects an unknown key inside `blocked_step` and `required_transition_ids` provided as a string instead of an array. The fixtures recompute dependent digests and assert rejection. All five workflows passed on exact test SHA `a5a8753f4609d4e4708ec311a20e3297bd288a2d`: governance [39051214686](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214686), engine [39051214571](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214571), browser/cross-runtime [39051214639](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214639), engine benchmark [39051214567](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214567), browser benchmark [39051214613](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39051214613).

The tested subset of FC5-TRACE-017 now comprises four predicates; it remains a subset, not exhaustive blocked metadata validation. The register and plan update require their own exact-head five-workflow gate.


### FC5-TRACE-020 — reconcile trace-only acceptance policy (2026-10-17)

The acceptance register previously marked this policy as unresolved, but contract § trace lifecycle already allows a `COMPLETED` trace without an outcome, and existing grouped GT-04 test `completed-trace-without-outcome.json` (test lines 797–818) imports/replays it as `EXECUTION` / `NOT_ASSESSED`. This is a trace-only execution package, not an outcome or contextual assessment. Related policy A rejects assessment without outcome and outcome linked to BLOCKED. The predicate is already covered on exact test SHA `b00058d84b176ffc8c6ee2dd5e911b147442753e`, with five workflows PASS: browser [39045767789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767789), engine [39045767741](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767741), engine benchmark [39045767743](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767743), browser benchmark [39045768012](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045768012), governance [39045767739](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39045767739).

No duplicate test was added. This is a policy/register reconciliation only; the wider trace schema/type matrix remains partial. This plan update triggers the exact-head gate including governance because the workflow path filter includes this plan.


### FC5-TRACE-014 — map existing temporal-prerequisite semantic coverage (2026-10-17)

No new atomic test is needed for the already-covered predicates. GT-03 rejects a BLOCKED trace whose `required_transition_ids` omits a prerequisite actually missing from the execution history, and rejects a forged blocked reason after trace/package digests are recomputed. Both are semantic checks, not checksum-only checks. The exact-head gate on `46180bb0f21bbba302a2ef0fd4805a8eb1ddf6f9` passed all five workflows: governance [39052324930](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324930), engine [39052324987](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324987), browser/cross-runtime [39052324916](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324916), engine benchmark [39052324943](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324943), browser benchmark [39052324951](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052324951).

Reconcile FC5-TRACE-014 to verified for these two predicates only. The complete per-step prerequisite/relation/history matrix remains partial. The documentation update triggers a fresh exact-head gate.


### FC5-SEC-001/002 — existing UI assertions mapped (2026-10-17)

The browser suite already asserts that the footer frames hashes as reproducibility support, rejects claims that unkeyed SHA-256 authenticates package/origin, and checks importer wording distinguishing internal consistency from origin authenticity (`ui_contract_test.cjs` lines 22–31 at test SHA `754c1bcaf1c3f67076ec20cdeab72621609bcb88`). These selected UI predicates are mapped as covered; this does not mean the package has cryptographic authentication or that all surfaces have exhaustive wording checks. Four test workflows passed on that test SHA—engine [39052689873](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689873), engine benchmark [39052689875](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689875), browser benchmark [39052689877](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689877), browser/cross-runtime [39052689839](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39052689839); governance was absent on that exact SHA. This documentation update requires a fresh exact-head five-workflow gate.


### FC5-TRACE-010 — executed-step schema evidence reconciled (2026-10-17)

The previous inventory note incorrectly implied the importer lacked closed step-key validation. Implementation already enforces the seven-key schema; the gap was adversarial evidence. The grouped FC5-TRACE-016 browser suite now rejects an unknown key and a wrong-type `prerequisites` value after dependent digests are recomputed. All five workflows passed on exact test SHA `294e20fb4cc2483078c6b70f2aa85a66acdb54d7`: governance [39053882898](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882898), engine [39053882899](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882899), browser/cross-runtime [39053882881](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882881), engine benchmark [39053882880](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882880), browser benchmark [39053882886](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39053882886).

Update FC5-TRACE-010 to verified for these two predicates only. Keep the complete missing/unknown/wrong-type field matrix partial. This documentation change needs its own exact-head five-workflow gate.

### GT-03 trace schema follow-up — pending exact-head gate (2026-10-17)

On candidate test commit `be1cc399bcfe6510910ee35bb7506753dddd9ffa`, three grouped cases were added for wrong-type `submitted_transition_ids`, undeclared `final_state`, and wrong-type `steps`. Existing coverage for an unknown top-level trace key and nested step schema remains reused; no duplicate test was added for those predicates.

The available GitHub status and PR-triggered workflow-run queries return no checks/runs for this exact SHA. Therefore the new cases are **not yet accepted**. Next action: obtain push-triggered CI evidence for the exact candidate head; inspect the browser job's targeted diagnostics and require all five workflows to pass on that same SHA. Only then reconcile the register/inventory as verified. No production change, scientific execution, or promotion to `main`.
