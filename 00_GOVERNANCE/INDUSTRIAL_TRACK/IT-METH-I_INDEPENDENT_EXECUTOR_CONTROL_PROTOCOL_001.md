# IT-METH-I — Independent Executor Control Protocol v0.1

## Status

`CONTROLLED METHODOLOGICAL PROTOCOL — DESIGN / READY FOR GOVERNED APPLICATION`

This protocol defines the minimum verifiable mechanism for establishing an independent execution context for FAA AMOC reconstruction 002.

It does **not** itself establish that an independent executor exists, does not authorize reconstruction 002, and does not modify IT-G4, G5, reconstruction 001, the existing utility result, the Industrial Track status, or the TGCV Core.

## 1. Scope

This protocol applies only to:

- Case: `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`
- Frozen methodological action: `IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_ACTION_001.md`
- Frozen reconstruction package: `IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_PACKAGE_002.md`
- Target artifact: `IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_002.md`

The purpose is to make the independence condition auditable before reconstruction 002 is performed.

## 2. Operational definition of independence

For this operation, `INDEPENDENT_EXECUTION_CONTEXT = PASS` only if all of the following are demonstrably satisfied:

1. **Executor separation** — reconstruction 002 is performed by an executor that did not perform reconstruction 001 and is not merely a repeat execution by the same executor/session.
2. **Information separation** — before sealing reconstruction 002, the executor has no access to reconstruction 001 answers, scores, interpretation, effort measurements, comparison results, or any derivative summary that could condition their reconstruction.
3. **Input freeze** — the executor receives only the frozen case/evidence boundary and reconstruction-002 package required by the already approved method.
4. **Execution-context traceability** — the execution context is identifiable sufficiently to establish that the above separation conditions were in force during the reconstruction.
5. **Artifact separation** — reconstruction 002 is produced as a distinct artifact and sealed before reconstruction 001 is disclosed to the executor.
6. **Temporal ordering** — the seal event for reconstruction 002 precedes any disclosure of reconstruction 001 to the executor.

Failure of any mandatory condition means `INDEPENDENCE_STATUS = FAIL` and reconstruction 002 must not be treated as an independent reconstruction.

## 3. Roles

### EXECUTOR-1
Producer of reconstruction 001. Must not perform reconstruction 002 under this protocol.

### EXECUTOR-2
Independent executor responsible for reconstruction 002. Receives the frozen package only and seals their result before any exposure to reconstruction 001.

### CONTROL / CUSTODIAN
Controls package delivery, access boundary, timestamps and sealing evidence. The custodian must not alter the frozen reconstruction method or scoring rules.

### COMPARATOR
May inspect both sealed artifacts only after EXECUTOR-2 has sealed reconstruction 002. Comparison is a separate governed operation and is outside this protocol.

## 4. Information barrier

Before execution begins, the custodian shall establish an explicit information boundary:

### Permitted to EXECUTOR-2

- frozen case identity;
- frozen evidence package;
- frozen reconstruction-002 worksheet/instructions;
- methodological instructions necessary to execute the reconstruction;
- execution environment necessary to complete and seal the artifact.

### Withheld from EXECUTOR-2 until sealing

- reconstruction 001;
- reconstruction 001 scores or answers;
- reconstruction 001 interpretation;
- reconstruction 001 effort record;
- any comparative analysis between reconstruction 001 and 002;
- any communication whose purpose or effect is to reveal reconstruction 001 content.

The information barrier is not satisfied merely by instructing the executor not to look at reconstruction 001 if the executor has unrestricted access to it.

## 5. Acceptable independence mechanisms

The following mechanisms are acceptable if their implementation is verifiable:

### A. Genuinely separate human executor
A second person, distinct from EXECUTOR-1, performs reconstruction 002 from the frozen package without access to reconstruction 001 before sealing.

Evidence should include executor identity/control record, package hash, delivery record, execution timestamp and sealed artifact hash. No unnecessary personal information should be persisted.

### B. Controlled blind execution environment
A technically controlled environment can establish the separation if EXECUTOR-2 can execute the frozen package while reconstruction 001 is inaccessible until the seal event. The environment must provide auditable evidence of the access boundary and temporal ordering.

### C. Independent institutional or laboratory execution
A separate institution, laboratory or organizational unit may serve as EXECUTOR-2 if the same information-separation and artifact-sealing requirements are demonstrably satisfied.

### Non-acceptable substitutes

- a second run by EXECUTOR-1;
- a second ChatGPT/model/session controlled by the same executor where reconstruction 001 is available;
- post-hoc re-answering after seeing reconstruction 001;
- an executor who receives reconstruction 001 before sealing 002;
- merely changing the computer or browser while retaining the same executor and information state;
- self-declaration of independence without a verifiable execution boundary.

## 6. Pre-execution gate

Before reconstruction 002 starts, the custodian shall record:

| Check | Required status |
|---|---|
| Executor-2 distinct from Executor-1 | PASS |
| Frozen package identified | PASS |
| Package integrity verified | PASS |
| Reconstruction 001 inaccessible to Executor-2 | PASS |
| Comparison outputs inaccessible to Executor-2 | PASS |
| Execution context identifiable | PASS |
| Seal mechanism available | PASS |

If any item is not PASS, execution is blocked.

## 7. Execution and sealing sequence

The required order is:

`FREEZE → ASSIGN EXECUTOR-2 → VERIFY INFORMATION BARRIER → EXECUTE → SEAL 002 → RECORD HASH/TIME → RELEASE 001 → SEPARATE COMPARISON OPERATION`

No step may be reordered.

The executor must not be shown reconstruction 001 merely to facilitate completion of 002.

## 8. Minimum evidence package

The control record for a successful independent execution should contain, at minimum:

1. independent execution context identifier;
2. frozen package identifier and integrity hash;
3. confirmation of the information boundary;
4. execution start and seal timestamps;
5. reconstruction-002 artifact hash;
6. confirmation that reconstruction 001 remained withheld until sealing;
7. any protocol deviation, with disposition.

Personal identity details should be minimized to what is necessary to establish independence and traceability.

## 9. Decision rule

`INDEPENDENCE_STATUS = PASS` only when every mandatory condition in Sections 2, 4, 6 and 7 is evidenced.

Otherwise:

`INDEPENDENCE_STATUS = FAIL / NOT ESTABLISHED`

A successful reconstruction 002 without proven independence remains a non-independent reconstruction and cannot be used to measure reproducibility or comparative analytical effort.

## 10. Separation from downstream comparison

This protocol ends when reconstruction 002 is sealed and its independence-control evidence is recorded.

It does not calculate reproducibility, effort agreement, utility, superiority, causality, value, prediction or scientific validity.

A later comparison operation may inspect the two sealed artifacts only after this protocol's completion.

## 11. Governance constraints

This protocol explicitly prohibits:

- modification of IT-G4 utility thresholds or comparator;
- reopening or rewriting reconstruction 001;
- modification of G5 authorization;
- use of post-decision outcomes to reconstruct the decision-time state;
- proprietary or partner evidence outside the frozen boundary;
- Rust / EXT-1.1 execution;
- modification of the TGCV Core;
- upgrading any scientific or industrial claim.

## 12. Current decision

`PROTOCOL STATUS = ESTABLISHED`

`INDEPENDENT EXECUTOR = NOT YET ESTABLISHED`

This artifact resolves the methodological definition of the independence mechanism. It does not resolve the factual availability of an EXECUTOR-2. That condition remains the open blocker tracked by GitHub Issue #2.
