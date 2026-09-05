# N-R1.3 — Branch N R Encoding and Feature Specification v0.2

**Program:** TGCV  
**Experiment:** EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** PROSPECTIVE SPECIFICATION — CORRECTED AND SUPERSEDING v0.1  
**Gate:** N-R1.3  
**Date:** 2026-09-05

## 1. Scope of this version

This version is a specification clarification of N-R1.3 v0.1. It does **not** change the 58-feature dimensionality, feature definitions, family selection, canonical ordering, normalization policy, or scientific objective.

The sole correction resolves an internal ambiguity in the empty-accessibility case: when `T_acc = emptyset`, **all 58 scientific R features are exactly zero**, including all four R4 min/max successor-state features.

This correction is prospective, result-independent, and does not use the historical EMP-1.1 result as an input.

**v0.2 supersedes v0.1 for implementation and all subsequent Branch N gates.**

## 2. Canonical representation

The Branch N representation remains:

`R = [R1 || R2 || R3 || R4]`

with exactly **58 numerical features**:

- R1: 6 family-availability features;
- R2: 6 family-cardinality features;
- R3: 30 component-incidence features;
- R4: 16 transition-result structural features.

All feature definitions, feature order, component order, family order, raw integer encoding, and normalization rules are unchanged from v0.1.

## 3. Corrected empty-accessibility rule

For any valid snapshot `S`, if:

`T_acc(S) = emptyset`

then the canonical scientific representation is:

`R(S) = (0,0,...,0)`

with exactly **58 zeros**.

Therefore:

- all six R1 features = `0`;
- all six R2 features = `0`;
- all thirty R3 features = `0`;
- all sixteen R4 features = `0`;
- in particular, `max_next_component_count = 0`;
- `min_next_component_count = 0`;
- `max_next_edge_count = 0`;
- `min_next_edge_count = 0`.

No current-state structural quantity is copied into R when there is no accessible transformation, because there is no successor transformation set from which an R4 successor statistic can be derived.

An implementation may emit an accessibility-status or validity diagnostic **outside R** for execution auditing. Such a diagnostic is not part of the scientific 58-feature vector and must never alter the vector itself.

## 4. Remainder of v0.1 unchanged

Except for Section 3 above, N-R1.3 v0.1 remains normative, including:

- snapshot-locality;
- structurality;
- no cardinality-only representation;
- fixed dimensionality;
- determinism;
- permutation invariance;
- no target leakage;
- no result-driven tuning;
- exact R1/R2/R3/R4 feature definitions;
- canonical component order `A1,A2,B1,B2,C1,C2`;
- canonical family order `ADD_COMPONENT < REMOVE_COMPONENT < ADD_EDGE < REMOVE_EDGE < REWIRE_EDGE < MODIFY_RESOURCE`;
- no pre-R normalization;
- traceability requirements;
- integer arithmetic and overflow safeguards;
- required invariance properties;
- provenance classification;
- anti-retrofitting rule.

## 5. Scientific and provenance status

This correction does not constitute recovery of the historical EMP-1.1 R implementation.

The 58-feature representation remains **RECONSTRUCTED** for Branch N.

The historical EMP-1.1 result remains a frozen historical record and is not validation evidence for the Branch N representation.

No confirmatory scientific execution is authorized by this correction alone.

## 6. Gate decision — N-R1.3 v0.2

**N-R1.3 v0.2 STATUS: PASS / CLOSED — CORRECTED SPECIFICATION**

The empty-accessibility encoding is now unambiguous and implementation-deterministic.

**N-R1 GLOBAL STATUS: BLOCKED pending N-R2 implementation conformance.**

### Next gate

**N-R2 — Transformation/R implementation conformance** against N-R1.2 and this v0.2 specification.
