# TI-001 Executor-2 Reconstruction Specification 001

**Status:** CANDIDATE — NOT EXECUTED

## Purpose

Define the independent reconstruction contract for the TI-001 preflight fixture.

The reconstruction is a fixture-equivalence activity only. It is not scientific execution.

## Independence boundary

Executor-2 MUST NOT import, call, execute, parse, or consume:

- `TI001_PREFLIGHT_FIXTURE_GENERATOR_001.py`
- Executor-1 implementation artifacts
- Executor-1 outputs

Executor-2 MAY use only:

- this reconstruction specification;
- explicitly frozen TI-001 fixture parameters;
- its own independent implementation.

## Reconstruction parameters

- `RANDOMISATION_SEED = 582031`
- `ENVIRONMENT_SEED_BASE = 731407`
- `PAIR_COUNT = 32`
- `BASE_ACTIONS = ["a","b","c"]`

## Pair identifiers

The pair identifiers are:

`TI001-001` through `TI001-032`.

## Assignment rule

1. Construct the ordered pair-ID sequence.
2. Shuffle it using the specified `RANDOMISATION_SEED`.
3. For shuffled position `j`:
   - even `j`: `slot_A=control`, `slot_B=treatment`;
   - odd `j`: `slot_A=treatment`, `slot_B=control`.

The resulting fixture contains 32 pairs and 64 records.

## Deterministic environment structure

For every pair:

- `S_t = "S0"`
- `T_acc_t = ["a","b","c"]`
- `available_transformations = ["a","b","c"]`

Successors:

- `a -> SA, ["x","y"]`
- `b -> SB, ["x","z"]`
- `c -> SC, ["y","z"]`

Future alternatives:

- `a -> SA, ["x","y"]`
- `b -> SB, ["x","z"]`

## Environment seed

For pair index `i`, using the canonical zero-based construction:

`environment_seed = 731407 + i`

The resulting seed is an observable fixture field and MUST therefore be reproduced.

The environment seed MUST NOT be interpreted as determining the environment structure.

The canonical generator derives an internal `_environment_nonce` from this seed, but that nonce is discarded and does not enter the fixture. Executor-2 MUST NOT treat the discarded nonce as part of the reconstruction contract.

## Condition-specific information

### Control

- `task = select_one_current_transformation`
- `candidate_count = 3`

### Treatment

- `future_reconfiguration = two_of_three_identity_pattern`
- `candidate_count = 3`
- `descriptor = successor_space_identity_turnover`

## Common record structure

Executor-2 MUST reproduce the complete observable record structure, including:

- `pair_id`
- `instance_id`
- `condition`
- `execution_slot`
- `S_t`
- `T_acc_t`
- `available_transformations`
- `successors`
- `future_alternatives`
- `temporal_order`
- `primary_estimand`
- `null`
- `null_condition`
- `seed`
- `environment_seed`
- `randomisation_seed`
- `information_control`
- `information_treatment`
- `selected_transformation`
- `S_t1`
- `T_acc_t1`
- `Delta_T_acc_t`
- `TSDA_descriptors`
- `decision_before_future_reveal`
- `leakage_checks`

Condition-specific treatment information is present only for treatment records; control records have `information_treatment = null`.

## Preflight status

The following fields MUST remain null:

- `selected_transformation`
- `S_t1`
- `T_acc_t1`
- `Delta_T_acc_t`

No scientific execution is performed by Executor-2.

## Canonical serialization and hash

The fixture object MUST first be constructed with:

- `schema = TI001_PREFLIGHT_FIXTURE_v004`
- `randomisation_seed = 582031`
- `environment_seed_base = 731407`
- `pair_count = 32`
- `record_count = 64`
- `instances = records`

The canonical hash input is the UTF-8 encoding of JSON serialized with:

- lexicographic key ordering (`sort_keys=True`);
- separators `(",", ":")`;
- no `fixture_sha256` field.

The SHA-256 digest of that byte sequence is then stored as `fixture_sha256`.

Thus, the hash is calculated over the fixture object **before** `fixture_sha256` is added.

## Equivalence requirement

Executor-2 PASS requires observational identity with the canonical fixture for:

- schema;
- top-level parameters;
- pair and record cardinalities;
- record content;
- canonical JSON serialization;
- `fixture_sha256`.

A matching hash is necessary but does not replace verification of the structural equivalence requirements.

## Gate result

**PASS** only if the independently reconstructed fixture satisfies every requirement above and its canonical hash equals the canonical fixture hash.

**FAIL** otherwise.

A PASS authorizes no scientific execution by itself; any subsequent scientific execution remains governed by the applicable TI-001 execution gates.
