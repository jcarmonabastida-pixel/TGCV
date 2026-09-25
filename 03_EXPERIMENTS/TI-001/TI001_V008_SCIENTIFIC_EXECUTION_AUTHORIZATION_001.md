# TI-001 V008 Scientific Execution Authorization 001

**Status:** AUTHORIZED — SCIENTIFIC EXECUTION MAY PROCEED

## Explicit user authorization

The user explicitly authorized scientific execution of TI-001 V008 on 2026-09-25.

Authorization text:
> «Autorizo la ejecución científica de TI-001 V008.»

## Bound preconditions

- Final Pre-Authorization Gate: `TI001-V008-FINAL-PREAUTHORIZATION-GATE-001`
- Final gate status: `PASS`
- Execution Contract: `TI001_V008_EXECUTION_CONTRACT_001.json`
- Scientific Executor-1: `TI001-V008-SCIENTIFIC-EXECUTOR-1-001`
- Runner SHA-1: `04a1b6cf37197499988579e5636c72a445a03a16`
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Decision units: 420
- Valid outputs: A / B
- Scientific object: Transformational Intelligence

## Execution boundary

Authorization permits the bound scientific Executor-1 to execute the frozen V008 fixture under the canonical runtime contract.

The executor must:
- expose only `context`, `available_actions`, and `future_structure` to the model;
- keep `decision_id`, `pair_id`, `condition`, and `presentation` hidden from the model;
- realize no successor before the decision;
- accept only A/B as valid decision outputs;
- perform no retry or recoding of invalid responses;
- perform no scientific analysis during execution;
- persist raw response/provenance required by the execution contract.

## Authorization status

**scientific_execution:** `AUTHORIZED`

This record authorizes execution but does not itself constitute execution evidence. Execution evidence must be produced by the scientific runner and audited separately.
