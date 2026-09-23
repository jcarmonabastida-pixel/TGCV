# TR-131 VisitAll Dynamic Space Executor-2 Reconstruction Comparison 001

**Status:** PASS — INDEPENDENT EXECUTOR COMPARISON AUDIT PASSED / SCIENTIFIC RESULT INTERPRETATION NOT PERFORMED

## Executor-2 execution

- Executor: `EXECUTOR_2`
- Independent: `true`
- Scientific execution authorized: `true`
- Scientific execution performed: `true`
- Source repository: `potassco/pddl-instances`
- Source revision: `cf19edf7c53d1540ddbb396c642595e0926ee552`
- Source problem: `grid-5`
- Source blob: `f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34`
- Depth: `2`
- Nodes: `21`
- Root T_acc cardinality: `4`

## Structural agreement with Executor-1

The received Executor-2 reconstruction reports:

- root T_acc hash: `9d841a3a8a0c059a141d8280a031504afdb5d93d18b49140c05040e6d63ffce9`
- node count: `21`
- depth-2 exhaustive tree
- all root branches reconstructed
- return-to-root branches reproduce the root T_acc hash
- Delta_T_acc recorded on realized edges
- baseline state / realized transformation / successor state recorded on each edge

The Executor-2 result is therefore structurally consistent with the Executor-1 reconstruction under the canonical comparison audit. The audit found identical source basis, depth, node count, root T_acc, root hash, and all compared node fields after normalizing only the redundant `S_parent` provenance field against `baseline.S_t`.

## Comparison audit result

The independent comparison audit returned `PASS`. Scientific interpretation remains explicitly separate and was not performed by the comparison audit.

- Executor-1 captured-output SHA-256: `735a4b6d13c763bbf6211bc9aebdf8ba5f6e00397e08ffa815df7edd601a3afa`
- Executor-2 captured-output SHA-256: `6c2a0dd29764c41c7aa5264cda4c9c070edbf096813b38fe90fc447c2615d95c`
- `node_structure_equal_excluding_redundant_parent_provenance`: `true`
- `e1_parent_provenance_consistent`: `true`
- `e2_parent_provenance_consistent`: `true`

Byte identity is not required and is not asserted.

## Important limitation

This document does **not** declare a scientific PASS/FAIL result. The experiment runner deliberately does not infer the representation result, and the independent reconstruction has not yet been reduced through a separate comparison gate.

The canonical Executor-1 captured-output hash is:

`735a4b6d13c763bbf6211bc9aebdf8ba5f6e00397e08ffa815df7edd601a3afa`

The Executor-2 captured-output hash has now been obtained from the persistence wrapper: `6c2a0dd29764c41c7aa5264cda4c9c070edbf096813b38fe90fc447c2615d95c`. The raw output remains local; this record preserves its captured-output hash.

## Next gate

The independent reconstruction/comparison gate is closed. The next gate is a separate scientific evaluation of the Dynamic Transformation Space representation cases against the frozen VisitAll baseline.

No scientific interpretation is asserted by this record.
