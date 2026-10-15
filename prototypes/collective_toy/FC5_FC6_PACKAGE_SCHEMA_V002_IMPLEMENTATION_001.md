# FC-5 / FC-6 package schema v002 — implementation note 001

- **Status:** implemented on the development branch; CI verification pending.
- **Schema v001:** `collective-toy-browser-run-001` (legacy import compatibility).
- **Schema v002:** `collective-toy-browser-run-002`.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`.
- **Implementation commits:** `7282d64f` (schema/stage and trace lifecycle validator), `e6d05d5d` (preserve v001 completed-only trace policy), `cf51930f` (grouped lifecycle tests).
- **Scope:** synthetic browser package contract only. No scientific execution and no promotion to `main`.

## v002 envelope

The v002 package has the existing v001 fields plus one required top-level field:

- `package_stage`: one of `EXPLORATION`, `EXECUTION`, `OUTCOME`, `ASSESSMENT`.

The package SHA-256 is computed over the entire package body, including `package_stage`, with only `package_sha256` removed.

### Stage truth table

| Stage | Trace | Outcome | Assessment | `value_assessment_status` |
|---|---|---|---|---|
| `EXPLORATION` | absent | absent | absent | `NOT_ASSESSED` |
| `EXECUTION` | `COMPLETED` or `BLOCKED` | absent | absent | `NOT_ASSESSED` |
| `OUTCOME` | `COMPLETED` | present and linked | absent | `NOT_ASSESSED` |
| `ASSESSMENT` | `COMPLETED` | present and linked | present and linked | absent |

The importer derives the expected stage from the artifacts and rejects a mismatch. An outcome requires a completed trace; a blocked trace cannot carry an outcome or assessment. A value assessment requires an outcome. `NOT_ASSESSED` indicates only that there is no value assessment; it does not indicate whether execution occurred.

Exploration artifacts (including `delta_reach`) are not concrete execution outcomes, so an exploration-stage package may validly contain them without a trace.

## Trace validation in v002

The importer checks the closed trace envelope and step key sets, supported trace schema/status, input/model/scenario identity links, digest format and recomputation, declared states/transitions, sequential numbering, state-edge coherence, prior-transition prefix history, temporal prerequisites, final state, and blocked-step metadata. A blocked trace preserves its last valid state and blocked reason/transition.

This is a contract validator for the prototype's declared synthetic model; hash consistency does not authenticate provenance or prove that an external event occurred.

## Compatibility

- v001 remains importable under its original envelope and completed-only trace policy; `package_stage` is not accepted in v001.
- v002 is emitted by the current browser exporter and carries `package_stage`.
- Do not rewrite or relabel historical v001 artifacts as v002 without explicitly adding stage information and recomputing hashes.
- Replay checks the deterministic exploration result; trace acceptance additionally validates the trace structure and its linkage. Replay success is not scientific validation.

## Grouped evidence added

The browser contract test now checks:
1. a v002 exploration-stage export and its stage declaration;
2. round-trip/import of a coherent `BLOCKED` execution trace with no outcome;
3. rejection of an outcome linked to a `BLOCKED` trace;
4. the existing completed-trace, outcome, assessment, hash and cross-link cases.

These tests have been committed but are **not claimed to pass until CI for the exact candidate commit completes**.

## Next gate

Wait for the required browser contract CI and inspect its exact run. Fix only demonstrated failures, preserving the historical v001 path and profile 1/2 compatibility. Update the coverage audit only from the resulting evidence.
