# TGCV VIATRA V002 External Listener Host Design Specification v001

## Status

CURRENT — DESIGN SPECIFICATION FOR IMPLEMENTATION

This specification formalizes the V002 external listener host design after completion of the historical-source, fixture, packaging, observer-host, PF-09, runtime-equivalence, static-preflight, and build/integration work already recorded in the V002 architecture records.

It is an implementation specification. It does not authorize runtime execution or scientific execution.

## 1. Purpose

V002 shall provide an external host around the pinned historical VIATRA CPS-to-Deployment batch transformation so that an external listener can observe transformation lifecycle events without modifying the historical transformation source.

The historical transformation remains the semantic reference.

Historical source binding:

- repository: `eclipse-viatra/org.eclipse.viatra.examples`
- revision: `eb68158a3d74581f69ccb8bc4f47673b12abdf85`
- class: `CPS2DeploymentBatchViatra.xtend`
- blob: `cf16b9c1305bdb06bf3b4c67deed57474ad7914c`

The historical VQL binding remains:

- file: `cpsXformM2M.vql`
- blob: `48033b9a6ddfd89bc875e1bbd4a505bd2411ff41`

## 2. Architectural boundary

The V002 host shall keep transformation semantics and observation infrastructure separate.

```
historical VIATRA transformation semantics
                |
                v
      V002 external host
                |
        +-------+-------+
        |               |
        v               v
 transformation     external
 execution          listener
        |               |
        +-------+-------+
                |
                v
       deterministic observation
```

The listener is an observer of transformation execution. It is not part of the transformation's semantic actions.

## 3. Historical rule contract

The V002 implementation shall preserve the historical six-rule execution sequence:

1. `HostRule`
2. `ApplicationRule`
3. `StateMachineRule`
4. `StateRule`
5. `TransitionRule`
6. `ActionRule`

The corresponding historical preconditions are:

| Rule | Preconditions |
|---|---|
| HostRule | `HostInstance.instance` |
| ApplicationRule | `ApplicationInstance.instance` |
| StateMachineRule | `AppInstanceWithStateMachine.instance` |
| StateRule | `State.instance` |
| TransitionRule | `Transition.instance` |
| ActionRule | `ActionPair.instance` |

The implementation shall retain the historical sequential `fireAllCurrent` execution semantics and ordering.

The ordering is part of the implementation contract because later rules consume model and traceability state established by earlier rules.

## 4. Rule representation

The historical rule fields are private implementation details of `CPS2DeploymentBatchViatra`. The investigation found no public API exposing those rule objects for direct reuse.

Therefore V002 shall not claim reflective or object-level reuse of the historical private rule instances.

The implementation shall reproduce the historical rule definitions externally, preserving:

- precondition;
- rule name;
- action semantics;
- required mapping and engine access;
- traceability operations;
- generated model relationships;
- historical execution order.

This is an external reconstruction of the historical host/rule definitions, not a modification of the historical source.

## 5. Transformation construction

The V002 host shall construct the batch transformation through the public `BatchTransformation` builder API.

Conceptually:

```
ViatraQueryEngine
      |
      v
BatchTransformation.forEngine(engine)
      |
      +-- addRule(HostRule)
      +-- addRule(ApplicationRule)
      +-- addRule(StateMachineRule)
      +-- addRule(StateRule)
      +-- addRule(TransitionRule)
      +-- addRule(ActionRule)
      |
      +-- addListener(externalListener)
      |
      v
    build()
      |
      v
BatchTransformation
```

The listener shall be registered before `build()`.

The builder shall remain responsible for creation and configuration of the listener-capable EVM infrastructure.

## 6. EVM boundary

The V002 implementation shall not instantiate, configure, or manipulate `AdaptableEVM` directly.

Any listener/adaptor infrastructure required for observation shall be supplied through the public transformation builder API.

The internal EVM implementation remains an implementation detail of the VIATRA transformation framework.

## 7. Query/index preparation

V002 shall rely on the transformation builder's preparation of the preconditions of rules registered with the builder.

The historical explicit preparation step shall not be reproduced as an independent semantic operation merely for textual similarity.

The implementation must nevertheless preserve the historical requirement that all registered rule preconditions are prepared before rule execution.

## 8. Listener contract

The external listener shall observe the lifecycle required by the V002 observer contract.

At minimum, the implementation shall provide deterministic observation of:

- transformation begin;
- selected activation identity;
- pre-action state where required by the observer contract;
- post-action state where required by the observer contract;
- transformation end.

For the minimal V002 observation path, the concrete selected transformation transition is the canonical `HostRule` / `HostInstance` activation defined by the frozen fixture and PF-09 contract.

The listener shall not invoke transformation rules.

The listener shall not change rule ordering.

The listener shall not alter transformation semantics.

## 9. Determinism and seriality

The V002 host shall execute serially.

It shall not introduce:

- parallel rule execution;
- random scheduling;
- pooling;
- aggregation;
- nondeterministic ordering.

For identical pinned inputs, source revisions, host revision, and runtime/toolchain identity, the observation serializer shall produce a deterministic representation and SHA-256 digest according to the existing observer contract.

## 10. Provenance

The implementation shall retain provenance for:

- historical VIATRA source repository and revision;
- historical transformation/example revision;
- V002 fixture revision;
- fixture SHA-256 manifest;
- V002 host revision;
- observer/instrumentation revision;
- runtime/toolchain identity.

Git blob identifiers do not substitute for fixture-byte SHA-256 values.

## 11. Scientific firewall

The V002 observer host is infrastructure only.

It shall not compute, store, infer, or emit:

- value;
- utility;
- reward;
- `T_acc`;
- accessibility labels;
- future assignment;
- TGCV performance metrics;
- scientific claim scores.

Observation artifacts shall remain technical/runtime artifacts.

## 12. Execution boundary

Construction, static validation, compilation, packaging, and build verification are implementation activities.

Runtime execution is separately gated.

This specification does not authorize:

- VIATRA runtime execution;
- scientific execution;
- scientific analysis;
- modification of TGCV claim status.

Any runtime execution must be authorized by the applicable execution gate after implementation construction and static checks are complete.

## 13. Acceptance conditions

The V002 implementation is structurally ready when:

1. the external host is materialized at the canonical V002 implementation location;
2. the six historical rule definitions are represented;
3. the historical execution order is preserved;
4. listener registration occurs before transformation build;
5. no direct `AdaptableEVM` manipulation is introduced;
6. the selected HostRule activation is uniquely scoped;
7. the serial observer contract is implemented;
8. deterministic serialization and SHA-256 are preserved;
9. provenance is complete;
10. the scientific firewall remains intact;
11. the existing build/static gates continue to pass.

## 14. Next implementation step

The next step is implementation of the V002 external listener host against this specification, followed by static inspection of the resulting source.

No runtime execution is implied by implementation completion.
