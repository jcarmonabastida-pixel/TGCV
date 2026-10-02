# TGCV VIATRA Serial Runtime Observation Prototype Implementation Preflight

**Status:** UNDERDETERMINED — implementation not authorized  
**Date:** 2026-10-02  
**Candidate revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Direct API evidence reviewed

The VIATRA EVM API defines `IEVMListener.beforeFiring(Activation)` and `afterFiring(Activation)`, providing explicit pre/post firing callbacks. `TransformationDebugger` also forwards activation-firing notifications.

The `Activation` API exposes:
- `getAtom()`;
- `getInstance()`;
- activation state;
- equality based on rule instance plus atom;
- a `fire(Context)` operation.

These APIs establish a viable interception point, but they do not by themselves provide a reproducible semantic identity or canonical serialization of the observed model state.

## P1–P8 implementation feasibility

| Test | Result | Reason |
|---|---|---|
| P1 identity stability | UNDERDETERMINED | `Activation.equals/hashCode` is runtime-object based through instance/atom semantics; observer-level canonical identity still needs explicit encoding. |
| P2 execution uniqueness | FEASIBLE | Observer can assign a per-run instance ID at `beforeFiring`. |
| P3 state determinism | UNDERDETERMINED | VIATRA API evidence does not provide a canonical TGCV state serializer. |
| P4 boundary integrity | FEASIBLE WITH VALIDATION | `beforeFiring` and `afterFiring` provide explicit hooks; exact mutation scope still requires prototype validation. |
| P5 sequence integrity | FEASIBLE | Observer can maintain a serial counter. |
| P6 seriality | FEASIBLE WITH EXPERIMENTAL CHECK | Initial prototype can enforce one execution thread and reject overlap. |
| P7 provenance integrity | FEASIBLE | Repository revision and instrumentation revision can be frozen and hashed. |
| P8 scientific firewall | FEASIBLE | No outcome/value fields are required by the EVM listener interface. |

## Key finding

The VIATRA API is sufficiently instrumentable to justify a prototype, but **not sufficiently specified to admit implementation as a scientific instrument yet**.

The main unresolved item is canonical state observation. The TGCV state digest cannot be based on arbitrary Java object identity or unspecified traversal order. A concrete model/state representation must therefore be selected and frozen before implementation.

A second unresolved item is transformation identity. The observer should not treat Java object identity as a scientific identity. It must derive `transformation_id` from frozen rule metadata and a canonical representation of the relevant activation binding.

## Decision

**UNDERDETERMINED.**

No implementation or scientific execution is authorized by this preflight.

## Next gate

Select a **minimal concrete VIATRA model/transformation fixture** whose state can be canonically serialized and whose transformation identity can be explicitly encoded. Then perform a fixture-level instrumentation contract preflight before writing instrumentation code.
