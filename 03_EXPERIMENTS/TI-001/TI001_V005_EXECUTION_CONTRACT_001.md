# TGCV — TI-001 v005 Execution Contract 001
## Infrastructure Adaptation Contract for the Frozen Action-Conditioned Design

**Date:** 2026-09-25  
**Status:** CONTRACT — DESIGN / IMPLEMENTATION PRECONDITION  
**Scientific execution:** NOT AUTHORIZED  
**Scope:** adaptation of the TI-001 execution infrastructure from the historical v004 contract to frozen fixture v005

## 1. Purpose

This contract defines the minimum execution interface required to execute the frozen TI-001 v005 design without changing the scientific design and without modifying any v004 artifact.

The contract exists because the historical TI-001 execution infrastructure is explicitly coupled to the v004 schema. In particular, the historical provider/executor expects `instances`, `successors`, and the v004 fixture hash. Those assumptions are not part of frozen v005.

This contract therefore adapts the infrastructure to the v005 semantic contract rather than adapting v005 to the historical implementation.

## 2. Historical boundary

The following historical artifacts remain immutable and are not reused as semantic contracts for v005:

- `TI001_SCIENTIFIC_EXECUTION_SPECIFICATION_001.md`
- `TI001_SCIENTIFIC_EXECUTOR_001.py`
- `TI001_DECISION_AGENT_PROVIDER_001.py`
- `TI001_EXECUTOR_2_RECONSTRUCTION_SPECIFICATION_001.md`
- `TI001_EXECUTION_AUTHORIZATION_002.json`

Their scope is v004.

Historical v004 remains preserved as a traceable antecedent. No v004 rerun, mutation, deletion, or reinterpretation is authorized by this contract.

## 3. Authoritative v005 inputs

The execution layer MUST bind to:

- redesign specification: `TI001_REDESIGN_PREFLIGHT_SPECIFICATION_002.md`
- frozen fixture: `TI001_v005_CANDIDATE_001.json`
- frozen decision mechanism specification: `TI001_DECISION_AGENT_SPECIFICATION_001.md`
- frozen runtime configuration: `TI001_DECISION_AGENT_RUNTIME_FREEZE_001.md`
- this execution contract.

The exact frozen v005 fixture SHA is:

`edd83fd2df3d39aad8911087569c19614c2264b7`

The execution layer MUST reject any fixture whose canonical identity does not match the frozen v005 fixture.

## 4. Scientific boundary

The primary scientific observable is:

`matched_condition_difference_in_transformation_selection`

The execution layer MUST record which transformation was selected under each condition.

No composite TI score is generated.

No reward, value, utility, performance, payoff, outcome-quality, success/failure, or action-ranking measure is generated.

The execution infrastructure MUST NOT convert the neutral future descriptors into an evaluative score.

## 5. v005 decision-unit contract

Unlike v004, v005 is a condition-level frozen design rather than a generated `instances`/successor fixture.

A decision unit is:

`pair_id + condition`

The minimum decision-input fields are:

- `pair_id`
- `condition`
- `state = S0`
- `currently_executable_transformations = [a,b,c]`
- `task`
- `decision_timing = before_successor_realisation`

For treatment only, the decision input additionally contains:

`future_mapping = {a:F(a), b:F(b), c:F(c)}`

The null condition contains no future mapping.

The provider MUST NOT expose:

- successor state;
- realised future accessibility;
- future reveal;
- reward;
- value;
- utility;
- performance;
- outcome quality;
- other agents' decisions;
- post-decision feedback;
- execution metadata not required for the decision;
- conversation state;
- previous response identifiers;
- external tools or web information.

## 6. Pairing and assignment

The execution implementation MUST construct matched decision units from the frozen v005 design.

If multiple repeated decision units are required for the authorized execution, the replication/randomisation procedure MUST be specified and frozen in a separate execution-data specification before execution.

The execution contract itself MUST NOT silently inherit the v004 seed, pair count, environment seed, or successor generator.

No v004 randomisation parameter is implicitly valid for v005.

## 7. Provider interface

A new v005 provider implementation MUST:

1. load the frozen v005 fixture;
2. verify its canonical fixture identity;
3. construct decision input exclusively from decision-time information;
4. preserve the frozen base prompt and runtime constraints;
5. invoke exactly one isolated decision request per decision unit;
6. validate that the returned text is exactly one of `a`, `b`, `c`;
7. persist request/response identifiers and runtime metadata;
8. persist the selected transformation;
9. persist the exact decision-input hash for auditability;
10. never read or expose successor information.

The provider MUST NOT import or call the v004 provider implementation as a semantic adapter.

## 8. Decision-input isolation

For each decision unit, the provider MUST construct a minimal serialized input.

Canonical control/null shape:

```json
{
  "state": "S0",
  "currently_executable_transformations": ["a", "b", "c"],
  "task": {
    "id": "TI001-TASK-001",
    "text": "Select exactly one executable transformation from the currently available transformations."
  }
}
```

Canonical treatment shape:

```json
{
  "state": "S0",
  "currently_executable_transformations": ["a", "b", "c"],
  "task": {
    "id": "TI001-TASK-001",
    "text": "Select exactly one executable transformation from the currently available transformations."
  },
  "future_transformation_space_information": {
    "a": {
      "future_accessibility_class": "stable",
      "identity_turnover_class": "none",
      "persistence_class": "persistent",
      "reconfiguration_class": "static"
    },
    "b": {
      "future_accessibility_class": "expanded",
      "identity_turnover_class": "partial",
      "persistence_class": "persistent",
      "reconfiguration_class": "reconfigured"
    },
    "c": {
      "future_accessibility_class": "reduced",
      "identity_turnover_class": "full",
      "persistence_class": "nonpersistent",
      "reconfiguration_class": "reconfigured"
    }
  }
}
```

The null decision input MUST be structurally comparable to control and MUST contain no future mapping.

The provider implementation MUST NOT pass the frozen fixture's `divergence_witness`, `transition_traceability`, `status`, hashes, or governance fields to the decision agent.

## 9. Decision output contract

Each decision record MUST contain at least:

- `pair_id`
- `condition`
- `selected_transformation`
- `request_timestamp`
- `decision_timestamp`
- `response_id`
- `response_status`
- `model_id`
- `generation_configuration`
- `decision_input_sha256`

The selected transformation MUST be exactly one of `a`, `b`, `c`.

Any other output is a provider validation failure, not a scientific observation.

## 10. Scientific executor interface

A new v005 scientific executor MUST consume:

1. the frozen v005 fixture;
2. the v005 decision package;
3. the canonical GitHub commit;
4. the v005 execution contract.

It MUST validate:

- fixture identity;
- condition membership;
- current state identity;
- current executable transformation identity;
- decision timing;
- decision-package completeness;
- selected transformation validity;
- decision-input isolation metadata;
- absence of prohibited pre-decision information;
- provider/runtime binding.

The executor MUST NOT require a `successors` field.

The executor MUST NOT synthesize successor states from v004.

The executor MUST NOT calculate a composite TI score.

## 11. Post-decision successor boundary

The frozen v005 design specifies the temporal order:

information presentation → transformation selection → successor realisation → future accessibility reveal.

However, v005's scientific estimand is the transformation selected at the decision point, and the frozen v005 fixture does not contain a successor-state generator.

Therefore:

- successor realisation is a temporal boundary, not a required pre-decision input;
- successor state/accessibility MUST NOT be required to validate the decision;
- no successor value may be inferred from the neutral future descriptor;
- the v004 successor table MUST NOT be reused;
- post-decision successor realisation is outside the primary TI-001 decision evidence unless a separate frozen environment specification is later introduced and authorized.

This explicitly resolves the v005/v004 infrastructure mismatch without changing v005.

## 12. Primary execution output

The scientific executor MUST produce an output record with:

- record type;
- contract version;
- fixture SHA;
- canonical commit;
- provider version;
- model/runtime metadata;
- decision count;
- per-decision observations;
- deviations;
- scientific execution status.

Each observation MUST include:

- pair identifier;
- condition;
- selected transformation;
- decision timestamp;
- response identifier;
- decision-input hash.

The output MUST NOT include a value score or composite intelligence score.

## 13. Executor-2 reconstruction contract

A new independent Executor-2 reconstruction MUST reconstruct the v005 decision-input contract independently.

Executor-2 MUST NOT:

- import the provider implementation;
- import the scientific executor;
- consume Executor-1 output;
- consume the v004 fixture generator;
- reuse v004 successor data;
- use the v004 hash as its target.

Executor-2 MUST independently verify:

1. S0 identity;
2. T_acc identity;
3. action identity;
4. control/treatment/null structure;
5. treatment mapping completeness;
6. descriptor neutrality;
7. absence of future reveal;
8. null validity;
9. decision-input serialization;
10. canonical v005 fixture identity.

Executor-2 reconstruction is a structural/equivalence gate only and does not authorize scientific execution.

## 14. Infrastructure separation

The following components MUST be new v005-scoped artifacts:

- v005 execution specification/contract implementation;
- v005 provider implementation or explicit provider adapter;
- v005 scientific executor;
- v005 Executor-2 reconstruction specification;
- v005 Executor-2 reconstruction implementation;
- v005 compatibility/preflight checker;
- v005 authorization record.

Existing v004 files MUST NOT be modified to accept v005.

## 15. Compatibility gate

Before scientific execution, a machine-checkable compatibility preflight MUST establish:

- frozen v005 fixture is present and unchanged;
- v005 contract references the correct fixture;
- provider interface matches v005;
- decision-input construction matches v005;
- treatment mapping is preserved;
- null condition is preserved;
- no successor dependency exists;
- no v004 hash dependency exists;
- no v004 seed/pair-count dependency exists unless separately and explicitly frozen for v005;
- Executor-1 and Executor-2 contracts agree;
- runtime freeze is compatible;
- primary estimand is unchanged;
- prohibited information remains excluded.

Any failure blocks authorization.

## 16. Authorization boundary

This contract does not authorize scientific execution.

A new v005-specific authorization MUST be created only after:

1. implementation of the v005 infrastructure;
2. compatibility preflight PASS;
3. independent Executor-2 reconstruction/preflight PASS;
4. provider/runtime preflight PASS;
5. explicit user authorization for v005 execution.

The historical v004 authorization MUST NOT be reused or interpreted as authorization for v005.

## 17. Traceability

The v005 execution chain is:

`TI001_REDESIGN_PREFLIGHT_SPECIFICATION_002.md`
→ `TI001_v005_CANDIDATE_001.json`
→ `TI001_V005_EXECUTION_CONTRACT_001.md`
→ v005 provider implementation
→ v005 decision package
→ v005 scientific executor
→ v005 Executor-2 reconstruction
→ v005 compatibility/preflight
→ v005 authorization
→ scientific execution
→ audit/replay.

Every implementation artifact MUST record the exact GitHub commit/blob identity of the frozen inputs it consumes.

## 18. Status

**Contract status:** DEFINED — IMPLEMENTATION NOT YET AUTHORIZED  
**v005 fixture:** FROZEN  
**v004:** RETAINED / UNCHANGED / HISTORICAL  
**Scientific execution:** NOT AUTHORIZED  
**Next gate:** implement v005 infrastructure and run compatibility preflight.

