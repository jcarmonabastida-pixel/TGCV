# TGCV TR-131 — SCIENTIFIC EXECUTION BUNDLE v0.1

**Status:** DRAFT — NOT FROZEN
**Scientific execution:** NOT AUTHORIZED
**Purpose:** assemble the minimum independently auditable package required before scientific freeze.

## 1. Bundle contents

Required components:
- protocol reference;
- scientific runner;
- scientific configuration;
- canonical baseline definition;
- X declaration;
- realization rule;
- transition rule;
- trace schema;
- trajectory derivation;
- execution environment;
- integrity manifest;
- Executor-2 reconstruction instructions;
- independent audit worksheet.

## 2. Scientific runner reference

`03_EXPERIMENTS/TR-131/tr131_scientific_runner_v02.py`

The scientific runner v0.2 implements `SCIENTIFIC_CANDIDATE` but remains fail-closed: execution requires a valid canonical G8 authorization record bound to the frozen package.

## 3. Scientific configuration

`03_EXPERIMENTS/TR-131/scientific_execution_config_v01.json`

The candidate scientific configuration is `SCIENTIFIC_CANDIDATE` and MUST be frozen and hashed before execution.

## 4. Canonical baseline

The scientific baseline must preserve the construction-checked values of S0, C and T_acc unless a documented protocol revision changes them before freeze.

Observed construction hashes:
- S0: `f172e9a705a27d73b864f6ce34e0c6b6cdf9f18bf1e61a646f2d81efdd40ec0a`
- C: `0aefc336bb0509d6403b51449c07f75a08b83d69137823e4653437a63164af43`
- T_acc: `0b5d8211831f6f2701578dc4a91d82ce63a4192422f66fee7aae856e9ba539b9`

## 5. X declaration

`X_A = policy_A` and `X_B = policy_B` are currently the construction-checked policies.

The scientific package must freeze the policy definitions before execution and prohibit post hoc modification.

## 6. Primary scientific contrast

The pre-specified primary comparison is the canonical realized-transformation trajectory H.

- Null result: `H_A = H_B`.
- Positive result: `H_A != H_B`.

The result must be reported descriptively; no causal conclusion follows automatically from the contrast.

## 7. Non-target invariants

The scientific execution must fail closed if A/B differ in any non-X component:
- S0;
- C;
- T_acc;
- transformation definitions;
- admissibility rules;
- transition function;
- observation window;
- environment;
- measurement procedure;
- analysis code.

## 8. Independent reconstruction

Executor-2 must reconstruct both cases from the frozen bundle without access to Executor-1 outputs, interpretation, or post-execution changes.

Executor-2 output must include:
- reconstructed baseline hashes;
- X declarations;
- realized transformations;
- transition traces;
- H_A/H_B;
- integrity hashes;
- deviations, if any.

## 9. Current blockers

Before freeze, the following remain incomplete:
- frozen scientific configuration;
- explicit immutable policy-definition artifact;
- environment specification;
- integrity manifest covering the complete bundle;
- canonical G8 authorization-record schema;
- canonical scientific execution-output schema;
- Executor-2 package;
- audit worksheet;
- freeze audit;
- G8 authorization.

## 10. Disposition

This bundle specification is a construction artifact. It does not authorize execution and does not constitute scientific evidence.

**Disposition:** `BUNDLE_ASSEMBLY_UPDATED — SCIENTIFIC EXECUTION BLOCKED`.