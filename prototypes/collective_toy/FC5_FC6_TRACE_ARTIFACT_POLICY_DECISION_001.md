# FC-5 / FC-6 contract decision memo: trace and optional artifacts — 001

- **Status:** proposed decision; awaiting owner approval.
- **Branch:** `prototype/tgcv-full-chain-001-20261014`
- **Scope:** contract clarification only. Do not change importer, UI, tests, or main until approved.
- **Evidence reviewed:** `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md`, `web/index.html` importer/exporter and sequence execution, `web/ui_contract_test.cjs` round-trip and adversarial tests.

## Problem

The contract says an attempted but blocked sequence must remain inspectable. The engine creates a trace with status `BLOCKED` and a blocked-step description. However, import validation currently accepts a concrete trace only when `trace.status === "COMPLETED"`. Export can also produce a package before any sequence has been executed, and package status `NOT_ASSESSED` describes absence of a value assessment rather than absence of an execution trace. These are distinct states and should not be conflated.

## Recommended policy (proposal, not normative until approved)

### 1. Artifact dependencies

- A **stage snapshot** may contain input/result without an execution trace, outcome, or assessment, provided the package schema explicitly identifies the artifact stage or documents stage-partial packages as valid. It must not be represented as a completed full-chain execution.
- An **execution trace** may be `COMPLETED` or `BLOCKED`; both are inspectable evidence of an attempted execution.
- An **outcome record** requires a `COMPLETED` trace and must link to its exact execution ID, trace digest, model and scenario.
- A **value assessment** requires a valid outcome and must link to its exact outcome digest and execution.
- A package with no value assessment declares `value_assessment_status: "NOT_ASSESSED"`, regardless of whether a trace exists. That status must never be used to imply whether execution occurred.

### 2. Trace invariants

For `COMPLETED`:
- no blocked step/reason is present;
- every step is ordered and semantically follows the input model and applicable rules;
- final state agrees with the last step (or initial state for a valid zero-step execution);
- no outcome may claim a different execution.

For `BLOCKED`:
- the blocked-step index/reason and last valid state are coherent with the attempted sequence;
- all preceding steps are valid and ordered;
- the trace remains exportable and inspectable;
- no outcome or assessment may claim that this blocked execution produced a completed observation.

The exact representation of the blocked step (whether it is included among completed steps or stored separately) must follow the existing trace schema or be clarified as a schema-versioned change; do not silently reinterpret existing fields.

### 3. Integrity and fail-closed behavior

Permit only documented artifact combinations. Reject outcome without trace, assessment without outcome, outcome linked to a blocked trace, contradictory status declarations, malformed artifacts and broken cross-links. Keep stage-partial package validity distinct from trace lifecycle status.

Hashes provide consistency/integrity checking, not proof of origin or authenticity.

## Alternatives considered

- **A — Recommended:** allow stage-partial packages and both trace statuses, while enforcing dependencies above. This matches the inspectability requirement and supports the prototype's stage-by-stage workflow.
- **B — Full-run-only package:** require a trace in every package, but permit both COMPLETED and BLOCKED. This simplifies import but conflicts with the existing ability to export before execution unless the exporter changes.
- **C — Completed-only import:** keep the current restriction and do not import blocked traces. Not recommended: it fails to preserve the contract's inspectability requirement for blocked attempts.

## Approval required

Approve the recommended policy (A), choose B, or provide a correction. No implementation or test changes should be made until this contract decision is accepted.

## If A is approved: grouped test consequences

- Extend one end-to-end lifecycle suite to round-trip a stage snapshot, completed trace without outcome, completed trace with outcome and optional assessment, and blocked trace without outcome.
- In the same suite, reject outcome without trace, outcome attached to a blocked trace, assessment without outcome, and contradictory assessment-status combinations.
- Keep targeted adversarial variants for forged digests/cross-links and malformed blocked-step metadata; do not create a separate test for every field.
- Run the required CI on the exact candidate commit and update the coverage map from the evidence.

## Boundaries

No code or tests changed by this memo. No CI or scientific execution initiated. `main` remains untouched.
