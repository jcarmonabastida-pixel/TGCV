# TGCV — TI-001 Randomisation & Assignment Protocol
## Protocol 001

Date: 2026-09-24  
Status: PRE-FLIGHT PROTOCOL — SCIENTIFIC EXECUTION NOT AUTHORIZED  
Basis: TI-001 Preflight Specification 001.

## 1. Purpose

This protocol defines the reproducible randomisation and condition-assignment procedure required by TI-001 §8. It is a preparation artifact only and does not execute the scientific experiment.

## 2. Experimental unit and assignment model

A matched instance is the common frozen environment from which two condition records are generated:
- one control record;
- one treatment record.

The matched instance therefore remains the unit of pairing, while condition is a property of each realised condition record.

To prevent condition labels from being confounded with a fixed execution slot, the protocol randomises the mapping of the two condition labels to two execution slots within each matched pair.

For each pair_id, the assignment is exactly one of:
- slot_A = control, slot_B = treatment; or
- slot_A = treatment, slot_B = control.

Both conditions are therefore represented exactly once per matched pair.

## 3. Frozen parameters

- Number of matched pairs: 32.
- Conditions per pair: 2.
- Execution slots per pair: 2.
- Randomisation algorithm: deterministic pseudo-random permutation using Python standard random.Random.
- Randomisation seed: 582031.
- Pair identifiers: TI001-001 through TI001-032.
- Assignment rule: shuffle the ordered pair identifiers with the frozen seed; for shuffled position j, assign even j → slot_A=control, slot_B=treatment; odd j → slot_A=treatment, slot_B=control.

The rule produces a deterministic assignment sequence from the frozen seed and pair identifiers.

## 4. Separation of seeds

The randomisation seed is distinct from any seed used to generate a synthetic environment or transition structure.

Environment-generation seeds may remain instance-specific, but they must not be used implicitly as condition-assignment seeds.

Every realised condition record must persist:
- pair_id;
- instance_id;
- condition;
- execution_slot;
- environment-generation seed;
- randomisation seed reference.

## 5. Independence requirements

The assignment procedure must not inspect or branch on:
- state identifiers;
- transformation identifiers;
- current accessibility;
- successor states;
- successor accessibility;
- treatment descriptors;
- expected outcomes;
- selected transformations.

Condition assignment is determined solely by the frozen randomisation configuration and the ordered pair identifiers.

## 6. Reproducibility

Executor-2 must be able to reconstruct the complete assignment from this protocol, the frozen pair identifier list, the frozen randomisation seed, and the declared algorithm and assignment rule.

The reconstructed assignment must match the persisted assignment exactly.

## 7. Required persisted assignment fields

The frozen dataset must make the assignment auditable. At minimum each realised condition record must expose:

pair_id  
instance_id  
condition  
execution_slot  
environment_seed  
randomisation_seed

A separate machine-readable randomisation configuration may additionally persist the algorithm and assignment rule.

## 8. Balance and invariants

The frozen package must satisfy:
- exactly 32 matched pairs;
- exactly one control record per pair;
- exactly one treatment record per pair;
- exactly one record per execution slot per pair;
- no duplicate instance_id;
- no duplicate (pair_id, condition);
- no duplicate (pair_id, execution_slot);
- assignment reproducible from the frozen protocol;
- assignment independent of environment content.

Across the complete package this yields 32 control records and 32 treatment records.

## 9. Relationship to the preflight specification

This protocol operationalises TI-001 Preflight Specification 001 §8 and supplies the assignment component required by §11 and §12.

The existing P1–P10 checker must not be interpreted as checking this protocol until explicit assignment checks are implemented.

## 10. Governance boundary

This protocol does not authorise scientific execution.

The required sequence remains:

protocol → generator/fixture implementation → assignment checker → preflight audit → independent reconstruction → separate execution authorisation.

## 11. Disposition

Randomisation protocol: defined.

Scientific execution: NOT AUTHORIZED.

TI-001 design: unchanged.

TGCV Core: unchanged.

Value: excluded from primary TI inference.