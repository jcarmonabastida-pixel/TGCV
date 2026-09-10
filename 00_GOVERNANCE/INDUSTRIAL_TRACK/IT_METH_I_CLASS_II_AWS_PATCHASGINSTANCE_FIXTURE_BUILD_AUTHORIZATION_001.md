# IT-METH-I — Class II AWS-PatchAsgInstance Fixture Build Authorization 001

**Date:** 2026-09-10  
**Status:** `CLOSED — PHASE A FIXTURE BUILD AUTHORIZED / TRANSFORMATION EXECUTION NOT AUTHORIZED`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`

## 1. Authorization scope

Authorization is granted for **Phase A only**:

`FIXTURE_BUILD_AND_PREDECISION_FREEZE`

The authorization covers construction of the isolated reproducible AWS fixture and capture/freeze of the common pre-decision state required by the frozen experiment design.

## 2. Explicit exclusions

This authorization does NOT authorize:

- invocation of `AWS-PatchAsgInstance`;
- execution of the comparator transformation;
- utility scoring;
- industrial performance claims;
- production-resource use;
- post-decision outcome analysis as a substitute for pre-decision observability;
- modification of the frozen experiment design or TGCV Core.

## 3. Governing records

Phase A SHALL conform to:

- `IT_METH_I_CLASS_II_FIXTURE_EVIDENCE_CATEGORY_RULE_001.md`
- `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_EXPERIMENT_DESIGN_001.md`
- `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_VARIABLE_OBSERVABILITY_ASSESSMENT_001.md`
- `IT_METH_I_CLASS_II_FIXTURE_COMPOSITION_MANIFEST_001.md`
- `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md`
- `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_INSTANTIATION_PLAN_001.md`
- `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md`
- `TECHNICAL_EXECUTION_WORKFLOW_v0.1.md` for any governed technical execution.

## 4. Required execution discipline

Before construction, the executor MUST recover the canonical records from GitHub and perform integrity preflight.

During Phase A:

1. use only the frozen source composition and explicitly recorded instantiation parameters;
2. keep fixture resources isolated from production;
3. record effective values rather than relying on dynamic/latest identifiers;
4. preserve raw outputs;
5. hash every generated evidence file;
6. freeze the common pre-decision state before any transformation;
7. perform the independent reconstruction;
8. stop at the Phase A boundary.

A disagreement between GitHub canonical state and local execution material blocks progression.

## 5. Phase A completion gate

Phase A is complete only if all mandatory pre-decision variables are directly observable and frozen, including:

- ASG identity;
- target instance identity;
- effective AMI/image;
- OS identity;
- ASG capacity;
- lifecycle/health/replacement configuration;
- Patch Group state;
- effective patch baseline;
- pre-decision patch compliance;
- SSM managed-instance state;
- accessibility-predicate inputs;
- timestamp cutoff;
- evidence provenance and hashes;
- comparator identity/operationalization;
- independent reconstruction agreement.

If any mandatory item remains unresolved, the gate remains blocked and no transformation execution may begin.

## 6. Authorization decision

`FIXTURE_BUILD_AUTHORIZATION = GRANTED`

`PHASE_A_AUTHORIZED = TRUE`

`CANDIDATE_EXECUTION_AUTHORIZED = FALSE`

`COMPARATOR_EXECUTION_AUTHORIZED = FALSE`

`PRE_EXECUTION_TRANSFORMATION_GATE = BLOCKED`

## 7. Next operation

Execute the **canonical Phase A technical build/pre-decision freeze procedure exactly once**, subject to the Technical Execution Workflow and the frozen build specification.

The resulting primary execution must be audited before any replay or transformation execution is considered.
