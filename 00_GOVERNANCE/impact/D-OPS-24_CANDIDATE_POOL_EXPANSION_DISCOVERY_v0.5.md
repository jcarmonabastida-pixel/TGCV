# D-OPS-24 — Candidate Pool Expansion & Cross-Domain Translation v0.5

**Status:** DRAFT / DESIGN — EXECUTION NOT AUTHORIZED
**Date:** 2026-09-09
**Predecessor:** D-OPS-24 v0.4 (immutable; F2-Q1/Q2/Q3 closed)
**Governance trigger:** EXT-UPD-4.1

## 1. Purpose

Test whether a heterogeneous external domain can support an independent translation of the TGCV analytical core without requiring the domain to already represent the complete TGCV architecture.

The protocol therefore separates **minimum translation eligibility** from **full TGCV conformance**.

## 2. Scientific question

Can the TGCV analytical layer be translated into an independently specified external domain such that the distinction between system state and accessible transformations, and the change in accessible transformation membership, is preserved without circularity, outcome leakage or semantic collapse?

## 3. Staged gate architecture

### Gate A — Minimum Translation Eligibility (MTE)

A candidate is eligible for translation when the available evidence supports all mandatory conditions:

MTE-1. Stable unit of analysis / system state `S_D`.

MTE-2. An independently constructible transformation universe or transformation schema `Uτ,D`, specified without using TGCV terminology as its defining criterion.

MTE-3. A non-circular accessibility predicate `Pτ,D(S_D,C_D,L_D)` defined prior to the downstream outcome.

MTE-4. Constructible `T_acc,D` as the subset of transformations satisfying that predicate.

MTE-5. At least two ordered observations or states permitting an analytically meaningful `ΔT_acc,D` test; documentary evidence may establish feasibility before execution.

MTE-6. Accessibility is not defined by success, adoption, reward, survival, performance, popularity, impact or other downstream outcome.

MTE-7. The domain's native concepts remain distinguishable from the TGCV constructs; no silent proxy substitution.

MTE-8. Sufficient provenance to reproduce the translation trace.

MTE-9. Explicit unresolved/empty cases are representable.

MTE-10. The candidate is not already an operative TGCV instantiation or a near-duplicate of a previously rejected/validated domain without an explicit non-redundancy justification.

**Gate A decision:** PASS / FAIL / INDETERMINATE. Only PASS permits Gate B.

### Gate B — Translation Trace (TT)

For each relevant TGCV object, construct:

`TGCV object → formal role → native construct → semantic justification → evidence → mapping class → failure condition`

Mapping classes remain DIRECT / PARTIAL / PROXY / NOT_RECONSTRUCTABLE.

The translation must explicitly test:

- C1 semantic-role preservation;
- C2 non-circularity;
- C3 no downstream leakage;
- C4 non-collapse;
- C5 trace completeness.

Gate B does not require the native domain to name or predefine TGCV objects.

### Gate C — Extended TGCV Conformance (ETC)

Only after Gate B, assess whether the translation can extend to:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Reach, Trajectory, Outcome and Value are therefore **tests of extension**, not discovery prerequisites.

A failure at Gate C must not retroactively invalidate a successful Gate A result; it identifies the boundary of transversal translation.

## 4. Discovery strategy

The search is no longer restricted to domains whose literature explicitly combines state, reconfiguration, accessibility and longitudinal language.

Candidate families may include, without being limited to:

- physical/engineering reconfiguration;
- distributed/networked systems;
- biological/ecological state-transition systems;
- organizational/process systems;
- manufacturing and production systems;
- logistics/infrastructure systems;
- software/hardware co-evolution where Rust is not the selected instantiation;
- control and cyber-physical systems;
- scientific/experimental systems with repeated configuration changes.

A family is admissible when it offers a plausible route to MTE-1..MTE-9 and is not redundant under MTE-10.

## 5. Discovery vs validation evidence

Discovery evidence is permitted to establish that the constructs needed for Gate A are independently available in the domain literature. It need not establish Reach, Trajectory, Outcome or Value.

A candidate must not be rejected solely because downstream TGCV extensions have not yet been operationalized.

Conversely, documentary resemblance alone is insufficient for Gate A: the candidate must pass the explicit MTE tests.

## 6. Outcome-blindness

Candidate selection and Gate A must not use knowledge of favorable empirical outcomes. Where literature reports outcomes, the selection record must distinguish the pre-outcome accessibility definition from downstream observations.

## 7. Search protocol

A future execution version will preregister search families and exact queries. Unlike v0.4, query design may be staged by candidate-family discovery rather than forcing all semantic dimensions into one query string.

Each query remains versioned and budgeted. Material query changes create a new query-family unit. Search results are logged before candidate admission.

The new protocol does not inherit the exhausted F2 3/3 budget. Any search budget must be explicitly established in the execution authorization for v0.5.

## 8. Candidate record

Each candidate record must minimally contain:

- candidate ID and native domain;
- unit/system state definition;
- native transformation definition;
- native accessibility criterion;
- temporal ordering basis;
- pre-outcome status of accessibility;
- evidence/provenance;
- MTE-1..MTE-10 dispositions;
- unresolved/empty handling;
- non-redundancy analysis;
- provisional mapping class;
- Gate A decision;
- explicit exclusion/failure reason where applicable.

## 9. Failure taxonomy

F-A: state not independently identifiable.
F-B: transformation universe cannot be independently constructed.
F-C: accessibility is circular or outcome-defined.
F-D: `T_acc` collapses into an outcome or native state proxy.
F-E: temporal comparison cannot establish change in accessibility.
F-F: provenance insufficient.
F-G: semantic distinction cannot be preserved.
F-H: redundancy with an existing TGCV instantiation.
F-I: evidence insufficient for decision; candidate remains INDETERMINATE rather than FAIL.

## 10. Epistemic boundaries

Passing Gate A is evidence of **translation eligibility**, not evidence of cross-domain generalisation.

Passing Gate B is evidence of a successful bounded translation trace, not proof of universal transversal validity.

Passing Gate C provides stronger evidence about the scope of the TGCV analytical layer but does not by itself establish causality, prediction, value creation, originality or superiority.

## 11. Historical integrity

D-OPS-24 v0.4 and all F2 execution artifacts remain immutable. Their zero-candidate result is retained as a bounded historical observation. v0.5 does not constitute a retroactive reopening or Q4.

The from-scratch prohibition remains operative.

## 12. Authorization boundary

This file is design only. No search, candidate selection, dataset acquisition, empirical execution or conformance execution is authorized by this document.

Before execution: protocol audit, scientific-memory reconciliation, impact propagation, RMA/control-surface update, consistency closure, and explicit execution authorization are required.

## 13. Intended next decision

Determine whether v0.5 adequately removes the possible discovery bottleneck while preserving the scientific invariants. If approved, freeze v0.5 and design a controlled discovery execution with a broader candidate-family search and a separately audited Gate-A screening stage.
