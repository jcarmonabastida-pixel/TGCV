# TI-001 V008 Executor-1 Specification 001

**Status:** READY FOR IMPLEMENTATION — SCIENTIFIC EXECUTION NOT_AUTHORIZED

## Purpose

Define the canonical Executor-1 boundary for the TI-001 V008 scientific execution. Executor-1 is the primary scientific executor and is distinct from all preflight, diagnostic, and Executor-2 reconstruction activities.

## Canonical bindings

- fixture_id: `TI001-V008-FIXTURE-001`
- fixture_sha256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- fixture_git_blob_sha1: `3ff971544f98c8d810173493cd49d54c46070952`
- schema_id: `TI001-V008-DU-SCHEMA-001`
- schema_git_blob_sha1: `d9539790452b047bc845a19bdcf50b8713a42b2a`
- provider_id: `TI001-V008-DECISION-AGENT-PROVIDER-001`
- provider_git_blob_sha1: `c7d066de3481143d878f06bb2c1d791cb7dc54e1`
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

Executor-1 MUST consume the frozen V008 fixture and expose to the provider only:

- context;
- available_actions;
- future_structure.

The following fields MUST remain hidden from the model/provider boundary:

- decision_id;
- pair_id;
- condition;
- presentation.

No outcome, reward, value, utility, performance feedback, successor state, or realized successor may be supplied.

## Execution population

- 210 pairs;
- 420 decision units;
- 70 control pairs;
- 70 treatment pairs;
- 70 null pairs;
- 105 I1_FIRST pair orientations;
- 105 I2_FIRST pair orientations.

Every decision unit MUST be executed exactly once if scientific execution is authorized.

## Response contract

Valid scientific responses are exactly:

- `A`
- `B`

An invalid response MUST be rejected. There MUST be no retry, recoding, substitution, or post-hoc correction.

For every attempted scientific decision, Executor-1 MUST persist sufficient raw provenance to establish:

- decision identity;
- request configuration;
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
- reveal hidden fixture fields;
- realize or expose the successor before the decision;
- inject outcome/reward/value/performance information;
- retry or recode invalid model responses.

## Scientific execution boundary

Preflights and diagnostics MUST remain `scientific_execution = NOT_PERFORMED`.

This specification does not authorize scientific execution. Scientific execution requires:

1. runtime compatibility preflight PASS;
2. fixture identity preflight PASS;
3. provider identity preflight PASS;
4. independent Executor-2 reconstruction PASS;
5. analysis definition bound and validated;
6. separate execution authorization gate PASS;
7. explicit user authorization.

## Independence and identity

The Executor-1 implementation MUST be separately bound by its Git blob SHA-1. Its source identity MUST be recorded before scientific authorization. Executor-1 MUST NOT consume Executor-2 outputs or implementation.

## Required execution result

The scientific result MUST distinguish:

- execution attempted/performed;
- completed decisions;
- invalid responses;
- API/runtime errors;
- response provenance.

No scientific result may be interpreted as evidence until the subsequent primary execution audit and analysis validation gates pass.
