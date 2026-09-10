# IT-METH-I — Class II AWS-PatchAsgInstance Phase A Code Audit 002

**Date:** 2026-09-10  
**Status:** `CLOSED — FAIL / IMPLEMENTATION PATCH REQUIRED`  
**Executable audited:** `class_ii_aws_patchasginstance_phase_a_fixture_build_v01.py`  
**Audited blob:** `7a183fdc9c568361d90b3e9fb587f323763c6115`  
**Audit basis:** frozen Phase A technical build specification, pre-decision state/comparator contract, fixture-build authorization, and prior executable audit 001.

## Decision

The patched executable is materially closer to the frozen Phase A contract, but it is **not yet safe for AWS execution**. The code audit identifies concrete implementation defects and contract-coverage gaps that must be repaired before any runtime invocation with `--build-fixture`.

`CODE_AUDIT_RESULT = FAIL`

`AWS_EXECUTION = NOT AUTHORIZED BY THIS AUDIT`

`CANDIDATE_TRANSFORMATION = NOT AUTHORIZED`

`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`

## Findings

### C1 — Frozen source hash defect: PATCH_TEMPLATE expected hash is incorrect

The executable contains an incorrect final value for `EXPECTED_SOURCE_SHA256["PATCH_TEMPLATE"]`:

`FD1C09C1FD200BC14A8039F00BF15AB0A15315A07C375FD2ECEF5E2`

The independently frozen source hash is:

`FD1C09C1FD200BC14E9D19F63B6DE5CA9688CB0A810A309BAB197D56211BC1F5E2`

Therefore the hard source-integrity gate would reject the known-good frozen patch template. The correction must use the exact previously verified SHA-256:

`FD1C09C1FD200BC14A8039F00BF15AB0E?`

**Correction note:** the implementation must not reconstruct or manually retype this value. It must be replaced from the canonical frozen source-integrity record / independently verified value in the repository and then re-audited.

`C1 = BLOCKING`

### C2 — Fixture template is not sufficient to establish the required patch baseline

The build path deploys a packaged form of the ASG sample template. That template establishes the ASG/launch-template/networking/instance topology but does not itself establish the required `Patch Group=App` effective patch baseline.

The executable applies the `Patch Group` tag after instance creation, then calls `get-patch-baseline-for-patch-group`. It does not create or otherwise freeze the required explicit baseline before this lookup.

Consequently the required state variable “effective patch baseline identity/version/assignment” is not guaranteed to exist or be deterministically controlled by the fixture build.

`C2 = BLOCKING`

### C3 — `--packaged-template` is an external mutable input without canonical composition binding

The executable accepts an arbitrary local packaged template. It records its hash, but does not establish that the supplied packaged artifact is the authorized deterministic composition of the frozen public sources.

The frozen technical specification requires source composition and hashes to remain bound to the authorized inputs. A package supplied at runtime must therefore be accompanied by a reproducible packaging identity/provenance record, or generated deterministically by the executor from the frozen sources.

`C3 = BLOCKING`

### C4 — SAM/CloudFormation packaging is declared as prerequisite but not implemented

The executor requires a packaged template but does not implement or verify the packaging step. This leaves the executable dependent on an undocumented external transformation between frozen source and deployed artifact.

That transformation must be either deterministic and explicitly recorded, or the build specification must identify a separately frozen packaged artifact.

`C4 = BLOCKING`

### C5 — Comparator definition is not fully operationalized

The comparator is recorded as prose:

“ordinary patching of the same target under the same frozen pre-decision evidence boundary”.

This does not provide an explicit implementation/procedure reference or an operational transformation identity. The frozen contract requires comparator identity, implementation/procedure reference and eligibility predicates to be frozen.

No comparator execution is required or authorized; the defect is solely in the definition record.

`C5 = BLOCKING`

### C6 — Sixteen-variable contract is only partially mapped

The state capture is structurally present, but several required variables are not captured with the precision required by the contract:

- lifecycle/replacement behavior is reduced to lifecycle hooks plus `TerminationPolicy`, which does not establish actual replacement/termination behavior;
- Patch Group is hard-coded to `App` rather than independently freezing the actual effective assignment and its provenance;
- effective baseline is queried generically but its identity/version semantics are not normalized/frozen;
- pre-decision compliance is captured as raw compliance items without an explicit pre-decision compliance state derivation;
- candidate/comparator eligibility is represented by a small custom predicate set rather than the full frozen eligibility contract;
- timestamp cutoff is not demonstrated to be the common cutoff governing every observation.

`C6 = BLOCKING`

### C7 — Cutoff semantics are insufficiently enforced

The code sets `window_start` and then `cutoff`, but `capture_state()` timestamps individual observations after the cutoff. The cutoff therefore functions as a label rather than as an enforced upper bound on observation timestamps.

The implementation must establish a cutoff/window policy and verify every mandatory observation timestamp satisfies it. A future observation cannot be admitted merely because the record stores an earlier cutoff.

`C7 = BLOCKING`

### C8 — Evidence hashing is self-referential/incomplete

The code hashes files already present in the output directory and stores those hashes inside the final record that is itself written afterward. This means the final evidence record does not contain a complete hash of itself and does not establish a stable manifest over all evidence outputs.

A separate manifest with deterministic file list, relative paths, sizes and hashes must be written and then itself frozen/audited according to the evidence-integrity procedure.

`C8 = BLOCKING`

### C9 — Independent reconstruction is not implemented

The executable explicitly records:

`REQUIRED — EXTERNAL SECOND RECONSTRUCTION NOT AUTOMATICALLY CLAIMED`

This is correct as a scientific safeguard, but means Phase A cannot close from this executable alone. The implementation must produce a reconstruction-ready package sufficient for the independently executed second reconstruction.

`C9 = REQUIRED GATE — NOT A CODE DEFECT`

### C10 — No explicit final Phase A closure record

The executable emits `PREDECISION_FREEZE_READY`, not a formal closure result containing all mandatory gate outcomes. This is appropriate before independent reconstruction, but a later closure operation must consume the primary package plus the independent reconstruction and explicitly determine PASS/FAIL without altering the frozen inputs.

`C10 = REQUIRED GATE`

### C11 — Cleanup option is misleading

`--no-cleanup` is accepted, but the code never performs automatic cleanup in either mode. This is not a safety failure, but the interface should state preservation semantics explicitly rather than expose a no-op cleanup control.

`C11 = NON-BLOCKING`

### C12 — Runtime failure handling may leave partially created resources without a governed recovery record

If stack creation succeeds but later pre-decision capture fails, the code reports `BLOCKED_PHASE_A` but does not persist a governed failure record containing stack identity and cleanup/preservation disposition.

For a controlled disposable fixture, partial infrastructure must be explicitly preserved for forensic audit or cleaned up by a governed operation; silent orphaning is not acceptable.

`C12 = BLOCKING`

## Positive controls confirmed

- Static governance checks precede AWS interaction.
- Candidate transformation is never invoked.
- Comparator transformation is never invoked.
- Utility scoring is never invoked.
- Source integrity is treated as a hard gate.
- AWS caller identity is checked before mutation.
- The executable requires explicit `--build-fixture` for infrastructure creation.
- Pre-decision state capture is separated from transformation execution.

## Required repair routing

Do **not** execute the current executable against AWS.

The next implementation patch must address C1–C8 and C12. C9–C10 must remain explicit closure gates rather than being falsely automated. C11 may be corrected opportunistically.

After the repair, perform a new primary code audit. Only a PASS from that audit may open the runtime Phase A execution gate.
