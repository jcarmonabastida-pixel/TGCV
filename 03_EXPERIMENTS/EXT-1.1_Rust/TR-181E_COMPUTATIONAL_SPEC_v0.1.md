# TGCV — TR-181E Computational Specification v0.1

**Status:** RECONSTRUCTION REGISTER — NOT FROZEN

## Purpose

This document converts the currently recoverable MVE-1.0/TR-181E knowledge into an implementation boundary without silently filling missing historical details.

## Provenance classes

- **SPECIFIED** — explicitly fixed by a canonical source.
- **DERIVED** — follows mechanically from specified material with no discretionary choice.
- **UNSPECIFIED** — a computational decision is required but the canonical record does not determine it.
- **NOT RECOVERED** — an artefact is referenced or required but cannot currently be recovered from the repository.

Only SPECIFIED and DERIVED elements may enter an equivalence-tested implementation without an explicit new decision record.

## 1. Scientific primitives

| Element | Status | Current determination |
|---|---|---|
| State `S` | SPECIFIED | Frozen MVE semantic primitive |
| Context `C` | SPECIFIED | Environmental/contextual conditions |
| Transformation universe `T` | SPECIFIED | Defined conceptually by MVE |
| Accessible set `T_acc` | SPECIFIED | `F(S,C,L)` |
| Change `ΔT_acc` | SPECIFIED | Change in accessible transformations |
| Mechanism `I` | SPECIFIED | Explanatory mechanism, not primitive |
| Relational representation `R` | SPECIFIED | Frozen representational target; exact computational encoding requires verification |

## 2. MVE structure

The currently recoverable specification establishes six transformation families, three resource classes, twelve objectives and horizon `H=6`. The exact executable encoding of each family/objective is **NOT RECOVERED** unless separately evidenced by a canonical implementation/configuration.

## 3. Accessibility

`T_acc = F(S,C,L)` is semantically specified.

The exact executable predicate `F` is currently **NOT RECOVERED** at implementation level. No inferred predicate may be promoted to historical fact.

## 4. R construction

The scientific role of `R` is specified as the relational structure of accessible transformations.

The following are required for implementation but remain to be recovered/verified:

- node identity convention;
- edge identity convention;
- treatment of transformation families;
- treatment of resources;
- duplicate handling;
- ordering/canonicalisation;
- whether any attributes are attached to nodes/edges;
- exact serialization.

Status: **NOT RECOVERED**.

## 5. Dataset generation

The pilot requires independently generated data. The exact historical generator implementation is not recoverable from the current repository state.

Therefore:

- generator semantics: **PARTIALLY SPECIFIED**;
- generator implementation: **NOT RECOVERED**;
- seed: **UNSPECIFIED for new pilot until frozen**;
- sample size: **UNSPECIFIED for new pilot until frozen**.

## 6. Evaluation

Historical EMP-1.1 parameters are preserved as historical facts and must not be silently reclassified as TR-181E parameters.

TR-181E requires its own pilot configuration to be frozen before execution, including metric, splits, seeds, model configuration and inference/reporting procedure.

## 7. Controls

The conceptual role of count-only, structural/permutation and matched baseline controls is specified by the historical protocol. Their exact implementation must be verified against the canonical experimental record before freeze.

## 8. Fail-closed implementation rule

If an implementation module depends on an UNSPECIFIED or NOT RECOVERED element, that module must not produce scientific pilot output.

The correct action is to create a decision record, recover the missing source, or explicitly register a new implementation choice.

## 9. Immediate recovery targets

The next recovery pass must seek canonical evidence for:

1. exact six transformation-family definitions;
2. resource constraints;
3. twelve objective definitions;
4. horizon/episode construction;
5. exact accessibility predicate;
6. exact R construction;
7. pilot generator semantics;
8. control implementations;
9. reproducibility configuration.

## 10. Freeze criterion

TR-181E implementation freeze requires zero unresolved dependencies in the executable path. Any unresolved field must be either recovered or explicitly decided in a versioned decision record before E1–E7 equivalence testing.

**Current verdict: NOT READY FOR IMPLEMENTATION FREEZE.**
