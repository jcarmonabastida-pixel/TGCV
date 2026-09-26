# TI-001 V012 V002 Executor-1 Specification 001

**Status:** READY FOR IMPLEMENTATION — SCIENTIFIC EXECUTION NOT_AUTHORIZED

## Purpose

Define the canonical Executor-1 boundary for TI-001 V012 V002. Executor-1 is the primary scientific executor and is distinct from preflight, diagnostics, and Executor-2 reconstruction.

## Canonical bindings

- fixture_schema: `TI001_V012_FIXTURE_v002`
- fixture_path: `03_EXPERIMENTS/TI-001/TI001_V012_FIXTURE_v002.json`
- fixture_sha256: `bf9dd4d44d9caad5079ad24617df2f56e6175523f31e75e32435aa087f032b5f`
- fixture_instance_count: `72`
- seed: `582031`
- executor_id: `TI001-V012-V002-SCIENTIFIC-EXECUTOR-1-001`
- provider_id: `TI001-V012-V002-DECISION-AGENT-PROVIDER-001`
- model_id: `gpt-5.6-luna`
- api_surface: `Responses API`
- top_p: `0.98`
- max_output_tokens: `16`
- temperature: omitted
- tools: empty
- conversation: null
- previous_response_id: null
- store: false

## Input boundary

For each decision unit, Executor-1 MUST expose only the decision information permitted by the frozen V012 protocol:

- current task;
- available transformations;
- future-space representation when applicable.

For non-NULL units, the representation MUST be taken from the unit's frozen `presentation_representation` according to its P1/P2 assignment. P1 uses the frozen order `a,b,c`; P2 uses the frozen order `c,b,a`.

The following fixture identity fields MUST NOT be exposed as decision content:

- instance_id;
- pair_id;
- condition;
- presentation.

No realized successor state, outcome, reward, value, utility, performance feedback, or post-decision information may be supplied before the decision.

NULL units MUST receive the frozen NULL information boundary and no future presentation records.

## Execution population

- 72 decision units;
- 36 P1 units;
- 36 P2 units;
- 24 NULL units;
- operationalisations O1/O2/O3;
- conditions INTACT/SCRAMBLED/NULL.

Every decision unit MUST be attempted exactly once if scientific execution is authorized. No retries, substitutions, omissions, or duplicate attempts are permitted.

## Response contract

Valid scientific responses are exactly:

- `a`
- `b`
- `c`

Responses outside this set MUST be classified as INVALID. There MUST be no retry, recoding, substitution, or post-hoc correction.

For every attempted scientific decision, Executor-1 MUST persist sufficient provenance to establish:

- decision identity;
- request/input configuration;
- provider identity;
- response identifier;
- response status;
- raw/structured response evidence;
- parsed response;
- validity classification.

## Execution isolation

Executor-1 MUST NOT:

- use conversation state;
- use previous responses;
- use external tools;
- expose hidden fixture identity fields;
- reveal realized successor states before the decision;
- inject outcome/reward/value/utility/performance information;
- retry or recode invalid responses;
- consume Executor-2 outputs or implementation.

## Scientific execution boundary

Preflights, diagnostics, package construction, and reconstruction MUST remain `scientific_execution = NOT_PERFORMED`.

This specification does not authorize execution. Execution requires all applicable compatibility, fixture, provider/runtime, executor, reconstruction, analysis, package-integrity, and separate authorization gates to PASS, plus explicit user authorization.

## Identity and reproducibility

The Executor-1 implementation MUST be separately bound by its Git blob SHA-1 before scientific execution. The exact provider/runtime configuration, system-prompt hash, validation procedure, execution command, and Executor-2 reconstruction binding MUST be recorded in the final execution package.

Any mismatch against the frozen V002 fixture identity or this specification is a blocking condition.

## Required execution result

The scientific result MUST distinguish:

- execution attempted/performed;
- completed decisions;
- invalid responses;
- API/runtime errors;
- response provenance.

No scientific result may be interpreted as evidence until the subsequent primary execution audit and analysis validation gates pass.
