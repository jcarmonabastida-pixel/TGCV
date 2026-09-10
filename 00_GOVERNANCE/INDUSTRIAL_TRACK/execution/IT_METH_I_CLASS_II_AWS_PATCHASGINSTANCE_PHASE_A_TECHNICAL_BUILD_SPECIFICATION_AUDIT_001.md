# IT-METH-I — Class II AWS-PatchAsgInstance Phase A Technical Build Specification Audit 001

**Date:** 2026-09-10  
**Status:** `AUDIT COMPLETE — PASS WITH REQUIRED CORRECTIONS BEFORE EXECUTABLE REPAIR`  
**Audited specification:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_A_TECHNICAL_BUILD_SPECIFICATION_001.md`  
**Primary contract:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md`  
**Build specification:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md`  
**Authorization:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_BUILD_AUTHORIZATION_001.md`

## 1. Audit decision

The technical specification is structurally consistent with the governing records and correctly preserves the Phase A / transformation boundary. It is **not yet sufficiently precise to serve as the direct implementation contract for the executable**.

`AUDIT_RESULT = PASS WITH REQUIRED CORRECTIONS`

No AWS execution is authorized by this audit.

## 2. Confirmed alignments

The specification correctly carries forward:

- Class II evidence classification;
- Phase A-only authorization;
- explicit exclusion of candidate/comparator transformations and utility scoring;
- frozen public source composition and SHA-256 values;
- minimum fixture boundary;
- effective-value freezing for dynamic/latest identifiers;
- all 16 mandatory pre-decision state variables;
- pre-decision-only accessibility evaluation;
- evidence preservation and hashing;
- independent reconstruction requirement;
- material-disagreement blocking;
- explicit non-claims;
- no TGCV Core modification.

These elements align with the pre-decision contract, which requires the same 16 state variables, common evidence boundary, accessibility predicates, metric contract, independent reconstruction and closure conditions.

## 3. Required correction C1 — cutoff ordering

The technical build sequence currently evaluates accessibility predicates before freezing the observation cutoff:

13. evaluate accessibility predicates;
14. freeze the observation cutoff timestamp.

This is temporally underspecified. The governing contract defines the cutoff as the boundary for pre-decision evidence. The cutoff must therefore be established **before or atomically with the observations used to evaluate the predicates**, not after predicate evaluation.

Required implementation wording:

1. establish the observation cutoff immediately before the pre-decision observation set;
2. capture all state/evidence observations against that cutoff;
3. evaluate predicates only from observations within that boundary;
4. preserve the exact UTC cutoff in the evidence manifest.

`C1 = REQUIRED`

## 4. Required correction C2 — comparator operationalization

The authorization requires Phase A completion to include **comparator identity/operationalization**. The technical specification records comparator identity as part of reconstruction but does not explicitly require an operational comparator definition to be frozen before Phase A closure.

The governing contract requires an operationally explicit comparator, not merely a label such as “normal patching”.

Required addition:

- freeze comparator transformation identity and implementation/procedure reference before Phase A closure;
- freeze its eligibility predicates against the common pre-decision state;
- do not execute it during Phase A.

`C2 = REQUIRED`

## 5. Required correction C3 — effort convention

The governing contract makes the effort convention conditional: it is required if effort is measured. The technical specification defines runtime/cost boundaries but does not explicitly state that any measured effort must use a frozen convention.

Required addition:

- if effort is measured, freeze the effort definition and measurement boundary before execution;
- if effort is not measured, record `EFFORT_MEASURED = FALSE` rather than leaving the dimension implicit.

`C3 = REQUIRED`

## 6. Required correction C4 — observation atomicity

The specification uses several sequential AWS observations (health, lifecycle, compliance, SSM, baseline, etc.). Because these can change independently, the implementation must explicitly distinguish:

- a single observation cutoff;
- individual API/query capture times;
- whether the resulting state vector is considered valid as a bounded snapshot.

Required addition:

- record capture time for every raw observation;
- require all mandatory state observations to fall within the declared pre-decision observation window;
- if the window cannot be bounded sufficiently for the state to be treated as common, block closure rather than silently treating asynchronous observations as simultaneous.

`C4 = REQUIRED`

## 7. Required correction C5 — source-location contract

The specification freezes source hashes but does not make the canonical local source locations part of the executable implementation contract. Since the local source inventory is known to contain stale information, the executor must not resolve sources through that inventory.

Required addition:

- bind each expected source hash to an explicitly frozen source path/reference in the execution package;
- validate bytes against the expected hash;
- do not consume `LOCAL_SOURCE_INVENTORY_001.json` as authoritative provenance.

`C5 = REQUIRED`

## 8. No other substantive divergence identified

No divergence was found that justifies changing:

- the Class II classification;
- the fixture boundary;
- the Phase A authorization;
- the 16-variable state contract;
- the accessibility representation;
- the independent reconstruction requirement;
- the transformation boundary;
- TGCV Core.

## 9. Routing decision

The specification should be **patched once** to incorporate C1–C5, then re-audited as a delta check. If the delta audit passes, the corrected specification becomes the direct contract for repairing the Phase A executable.

The executable must not be repaired against the current uncorrected specification because doing so would recreate the exact omission cycle we are deliberately eliminating.

`AWS_EXECUTION = NOT PERFORMED`

`CANDIDATE_TRANSFORMATION = NOT AUTHORIZED`

`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`
