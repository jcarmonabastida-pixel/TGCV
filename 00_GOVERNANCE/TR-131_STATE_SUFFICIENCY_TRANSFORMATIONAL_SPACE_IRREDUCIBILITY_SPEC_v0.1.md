# TGCV — TR-131 State Sufficiency / Transformational-Space Irreducibility Test

**Version:** v0.1  
**Status:** `SPECIFICATION FROZEN FOR EXECUTOR DESIGN`  
**Date:** 2026-09-11  
**Programme:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos

## 1. Purpose

TR-131 tests whether the candidate state representation `S` is sufficient, at the tested resolution, to account for differences in accessible transformations without introducing an additional primitive state dimension that is irreducible with respect to `S`.

The test is methodological and falsifiable. It does not assume that `S` is sufficient, and it does not by itself establish or reject the TGCV programme as a whole.

## 2. Conceptual position

Current candidate core:

`TGCV_Core = (S, T_acc)`

Auxiliary/derived elements may include context, laws/constraints, transition predicates and trajectory descriptors, provided their status is not silently promoted to primitive state.

TR-131 therefore asks whether there exists an admissible distinction between two cases that are represented as the same `S` but for which the accessible transformation structure relevant to the tested transformation differs in a way that cannot be reconstructed from `S` plus explicitly declared derived/auxiliary information.

## 3. Research question

Can two empirically admissible cases be observationally identical under the candidate state representation `S` while requiring different accessibility for the same candidate transformation `τ`, such that the difference cannot be reduced to already declared components of the representation?

## 4. Unit of analysis

The unit is a bounded transformation candidate:

`(S_t, C_t, τ_i) → admissibility/accessibility → (S_{t+1}, C_{t+1})`

The test MUST NOT require exhaustive ex-ante enumeration of all `T_acc(S_t)`. In accordance with TR-132-MOD-1, the admissibility/accessibility question is evaluated for concrete candidate transformations and their reconstructable pre-outcome conditions.

## 5. Test construction

A valid test instance requires:

1. Two cases `A` and `B` with the same candidate state representation `S_A = S_B` at the declared observational resolution.
2. The same candidate transformation `τ` or formally equivalent transformation unit.
3. Sufficient pre-outcome information to establish the relevant accessibility/admissibility condition independently of the outcome.
4. A demonstrated difference in accessibility/admissibility, or an attempted demonstration that no such difference exists.
5. An audit of plausible explanatory variables outside `S`, classified as either:
   - derivable from `S`;
   - explicitly auxiliary/contextual and admissibly conditioned;
   - genuinely irreducible with respect to `S`.
6. A reconstructable transition or downstream consequence only where needed to distinguish the tested accessibility condition from its later outcome.

## 6. Primary decision rule

### PASS — state sufficiency supported

The tested cases do not establish an irreducible accessibility distinction outside `S`, after declared auxiliary/derived variables are accounted for.

This is a bounded methodological PASS, not proof that `S` is universally sufficient.

### FAIL — state sufficiency challenged

A reproducible case establishes that `S_A = S_B` while accessibility/admissibility of the same `τ` differs, and the difference survives the reduction audit against all declared derived/auxiliary variables.

This constitutes evidence that the candidate state representation is insufficient at the tested resolution and that an additional primitive or revised state representation may be required.

### INCONCLUSIVE

The equality of `S`, the accessibility distinction, or the reduction audit cannot be established independently and reproducibly.

Infrastructure defects MUST be separated from scientific outcomes and MUST NOT be converted into PASS/FAIL claims.

## 7. Independence and blindness requirements

The primary executor MUST operate only on the frozen package and admissible evidence defined by the protocol.

An independent reconstruction, when required by the closure protocol, MUST NOT use the primary outcome, its interpretation, or later evidence. The independent executor reproduces the test from the same frozen admissible inputs.

## 8. Outcome separation

Accessibility/admissibility MUST be established without using the post-outcome result that the transformation is intended to produce.

A later observed outcome may be used only for the separately declared transition/downstream analysis. It MUST NOT retroactively define whether `τ` was accessible.

## 9. Non-goals

TR-131 does not:

- prove a universal ontology of systems;
- establish transversal validity across domains;
- establish causal superiority of TGCV;
- establish industrial utility or financial value;
- require complete enumeration of `T_acc`;
- by itself modify `TGCV_Core`;
- upgrade any C01–C16 claim.

## 10. Required executor outputs

The executor MUST produce machine-readable and human-auditable records containing at minimum:

- package/protocol identifier;
- frozen input identity and hashes;
- case identifiers;
- state representation definition and canonical serialization;
- equality/identity result for `S`;
- candidate transformation identity;
- pre-outcome accessibility/admissibility evidence;
- reduction-audit results for non-state variables;
- transition/downstream evidence where applicable;
- explicit PASS/FAIL/INCONCLUSIVE classification;
- infrastructure status separately from scientific status;
- environment information sufficient for reconstruction;
- authorization status;
- scientific-core status.

## 11. Closure constraints

A closure record MUST state explicitly:

- whether the test was scientifically executable;
- whether the evidence supports, challenges, or leaves unresolved state sufficiency;
- whether an irreducible state distinction was demonstrated;
- whether any Core modification is warranted;
- whether evidence propagation is required;
- whether any claim status/level changes (default: no).

Evidence propagation, if material, is separate from claim upgrade.

## 12. Gate sequence

`TR-131-SPEC → frozen package → executor preflight → primary execution → independent reconstruction (if required) → closure review → evidence propagation decision`

No execution authorization is implied by this specification. The standing industrial authorization remains `NONE` until separately granted by the applicable governance record.

## 13. Scientific status

`SCIENTIFIC_CORE = UNCHANGED`

`CLAIM_UPGRADE = NONE`

`INDUSTRIAL_AUTHORIZATION = NONE`

`TR-131_STATUS = SPECIFICATION_FROZEN_FOR_EXECUTOR_DESIGN`
