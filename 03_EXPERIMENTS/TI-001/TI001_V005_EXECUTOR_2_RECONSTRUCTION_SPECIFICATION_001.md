# TI-001 v005 Executor-2 Reconstruction Specification 001

Status: DEFINED — NOT EXECUTED
Scope: independent reconstruction of the frozen v005 decision-input contract

## 1. Purpose
Executor-2 independently reconstructs the observable v005 decision-unit structure and verifies equivalence with the frozen v005 fixture. It is a structural/equivalence activity only and never performs scientific model calls.

## 2. Independence boundary
Executor-2 MUST NOT import, call, execute, parse, or consume the v005 provider, v005 scientific executor, any Executor-1 decision output, or any v004 fixture, generator, successor table, seed, or hash.
Executor-2 MAY use only this specification, the frozen v005 fixture, and its own implementation.

## 3. Frozen decision environment
For every condition: state=S0; current executable transformations=[a,b,c]; actions=[a,b,c]; task id=TI001-TASK-001; decision timing=before_successor_realisation.
Conditions are exactly control, treatment, null.

## 4. Treatment reconstruction
Treatment MUST reconstruct exactly one future descriptor for each action: a -> F(a), b -> F(b), c -> F(c).
Descriptor fields MUST be exactly: future_accessibility_class, identity_turnover_class, persistence_class, reconfiguration_class.
Executor-2 MUST verify that at least two descriptors differ.

## 5. Control and null
Control MUST contain no future mapping.
Null MUST contain no future mapping, future signal, or recommendation and MUST preserve S0, [a,b,c], action identities, task, decision timing, and format compatibility.

## 6. Temporal boundary
Executor-2 MUST verify information presentation -> transformation selection -> successor realisation -> future accessibility reveal, and that successor state/accessibility are not exposed before selection.
Executor-2 MUST NOT introduce a successor generator.

## 7. Divergence witness
Executor-2 MUST independently verify the frozen D6/R11 witness: control action a; treatment action b; different=true; treatment mapping required; state, T_acc, task, timing and decision rule equal; no evaluation; removing mapping removes the witness.
This is a structural witness check, not an empirical prediction.

## 8. Canonical equivalence
Executor-2 MUST verify fixture identity, version, status, execution status, task, temporal order, randomisation declaration, shared execution environment, all conditions, divergence witness, future-reveal flags, and transition traceability.
Expected frozen fixture SHA: edd83fd2df3d39aad8911087569c19614c2264b7.

## 9. Output
Machine-readable outputs: fixture_identity_pass, condition_structure_pass, treatment_mapping_pass, descriptor_schema_pass, future_descriptor_distinction_pass, temporal_separation_pass, future_reveal_blocked, null_validity_pass, divergence_witness_pass, traceability_pass, canonical_hash_pass, overall_reconstruction_pass. Failures MUST include reasons.

## 10. Scientific boundary
Executor-2 MUST NOT invoke an LLM, create a decision, produce scientific execution output, calculate a TI score, or alter the frozen fixture.
A PASS authorizes no scientific execution.