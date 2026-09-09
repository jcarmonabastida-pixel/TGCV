# D-OPS-24 — Candidate Pool Expansion & Cross-Domain Translation v0.5

**Status:** REVISED DRAFT / DESIGN — EXECUTION NOT AUTHORIZED
**Date:** 2026-09-09
**Predecessor:** D-OPS-24 v0.4 (immutable; F2-Q1/Q2/Q3 closed)
**Governance trigger:** EXT-UPD-4.1
**Design audit:** EXT-UPD-4.1_DOPS24_V05_DESIGN_AUDIT_v0.1 — CONDITIONAL PASS WITH REQUIRED REFINEMENTS

## 1. Purpose

Test whether a heterogeneous external domain can support an independent translation of the TGCV analytical core without requiring the domain to already represent the complete TGCV architecture.

The protocol separates **minimum translation eligibility**, **translation readiness**, **translation trace**, and **extended TGCV conformance**.

## 2. Scientific question

Can the TGCV analytical layer be translated into an independently specified external domain such that the distinction between system state and accessible transformations, and the change in accessible transformation membership, is preserved without circularity, outcome leakage or semantic collapse?

## 3. Staged gate architecture

### Gate A — Minimum Translation Eligibility (MTE)

A candidate is eligible for translation when the available evidence supports all mandatory conditions:

MTE-1. Stable unit of analysis / system state `S_D`.

MTE-2. An independently constructible transformation universe or transformation schema `Uτ,D`, specified without using TGCV terminology as its defining criterion. Adequacy requires that transformations be enumerable or otherwise explicitly specifiable at the chosen unit of analysis without reference to downstream outcomes.

MTE-3. A non-circular accessibility predicate `Pτ,D(S_D,C_D,L_D)` defined independently of the TGCV translation and prior to the downstream outcome. Adequacy requires that accessibility be evaluable from pre-outcome state/context information and distinguish at least feasible from non-feasible transformations.

MTE-4. Constructible `T_acc,D` as the subset of transformations satisfying that predicate.

MTE-5. At least two ordered observations or states permitting an analytically meaningful `ΔT_acc,D` test; documentary evidence may establish feasibility before execution.

MTE-6. Accessibility is not defined by success, adoption, reward, survival, performance, popularity, impact or other downstream outcome.

MTE-7. The domain's native concepts remain distinguishable from the TGCV constructs; no silent proxy substitution.

MTE-8. Sufficient provenance to reproduce the translation trace.

MTE-9. Explicit unresolved/empty cases are representable.

MTE-10. The candidate is not already an operative TGCV instantiation or a near-duplicate of a previously rejected/validated domain without an explicit non-redundancy justification.

**Gate A decision:** PASS / FAIL / INDETERMINATE. Only PASS permits Gate B.

### Gate B — Translation Readiness (TR)

TR is a documentary feasibility demonstration, not empirical validation.

TR-1. At least one worked native-domain example is available in which a defined native state admits at least two distinguishable candidate transformations.

TR-2. For those transformations, accessibility can be assessed from pre-outcome state/context information using the independently specified native criterion.

TR-3. The example does not equate an observed state transition with the accessible transformation space.

**Gate B decision:** PASS / FAIL / INDETERMINATE. Only PASS permits Gate C.

### Gate C — Translation Trace (TT)

For each relevant TGCV object, construct:

`TGCV object → formal role → native construct → semantic justification → evidence → mapping class → failure condition`

Mapping classes remain DIRECT / PARTIAL / PROXY / NOT_RECONSTRUCTABLE.

The translation must explicitly test:

- C1 semantic-role preservation;
- C2 non-circularity;
- C3 no downstream leakage;
- C4 non-collapse;
- C5 trace completeness.

For PARTIAL or PROXY mappings, the record must state explicitly what the native construct represents and what it does **not** represent. Proxy status never implies equivalence.

Gate C does not require the native domain to name or predefine TGCV objects.

### Gate D — Extended TGCV Conformance (ETC)

Only after Gate C, assess whether the translation can extend to:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Reach, Trajectory, Outcome and Value are therefore **tests of extension**, not discovery prerequisites.

A failure at Gate D must not retroactively invalidate a successful Gate A or Gate B result; it identifies the boundary of transversal translation.

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

A family is admissible when it offers a plausible route to MTE-1..MTE-10 and is not redundant under MTE-10.

## 5. Discovery vs validation evidence

Discovery evidence is permitted to establish that the constructs needed for Gate A and Gate B are independently available in the domain literature. It need not establish Reach, Trajectory, Outcome or Value.

A candidate must not be rejected solely because downstream TGCV extensions have not yet been operationalized.

Conversely, documentary resemblance alone is insufficient: the candidate must pass the explicit MTE and TR tests.

## 6. Outcome-blindness

Candidate selection and Gates A/B must not use knowledge of favorable empirical outcomes. Where literature reports outcomes, the selection record must distinguish the pre-outcome accessibility definition from downstream observations.

## 7. State / transformation distinction

Observed transitions are evidence about what occurred, not automatically evidence about what was accessible.

The protocol must maintain the distinction:

`observed transition ⊄ automatically T_acc,D`

A candidate that cannot independently specify transformations and their pre-outcome accessibility criterion cannot pass MTE merely because repeated state transitions are documented.

## 8. Search protocol

A future execution version will preregister search families and exact queries. Unlike v0.4, query design may be staged by candidate-family discovery rather than forcing all semantic dimensions into one query string.

Each query remains versioned and budgeted. Material query changes create a new query-family unit. Search results are logged before candidate admission.

The new protocol does not inherit the exhausted F2 3/3 budget. Any search budget must be explicitly established in the execution authorization for v0.5.

## 9. Candidate record

Each candidate record must minimally contain:

- candidate ID and native domain;
- unit/system state definition;
- native transformation definition;
- transformation-universe adequacy statement;
- native accessibility criterion;
- temporal ordering basis;
- pre-outcome status of accessibility;
- evidence/provenance;
- MTE-1..MTE-10 dispositions;
- TR-1..TR-3 dispositions;
- unresolved/empty handling;
- non-redundancy analysis;
- provisional mapping class;
- Gate A and Gate B decisions;
- explicit exclusion/failure reason where applicable.

## 10. Failure taxonomy

F-A: state not independently identifiable.

F-B: transformation universe cannot be independently constructed or adequately specified.

F-C: accessibility is circular or outcome-defined.

F-D: `T_acc` collapses into an outcome or native state proxy.

F-E: temporal comparison cannot establish a meaningful accessibility-change test.

F-F: provenance insufficient.

F-G: semantic distinction cannot be preserved.

F-H: redundancy with an existing TGCV instantiation.

F-I: evidence insufficient for decision; candidate remains INDETERMINATE rather than FAIL.

F-J: translation readiness cannot be demonstrated without using downstream outcome information.

## 11. Epistemic boundaries

Passing Gate A is evidence of **translation eligibility**, not evidence of cross-domain generalisation.

Passing Gate B is evidence of **translation readiness**, not empirical validation or proof of transversal validity.

Passing Gate C is evidence of a bounded translation trace, not proof of universal transversal validity.

Passing Gate D provides stronger evidence about the scope of the TGCV analytical layer but does not by itself establish causality, prediction, value creation, originality or superiority.

## 12. Historical integrity

D-OPS-24 v0.4 and all F2 execution artifacts remain immutable. Their zero-candidate result is retained as a bounded historical observation. v0.5 does not constitute a retroactive reopening or Q4.

The from-scratch prohibition remains operative.

## 13. Authorization boundary

This file is design only. No search, candidate selection, dataset acquisition, empirical execution or conformance execution is authorized by this document.

Before execution: protocol audit, scientific-memory reconciliation, impact propagation, RMA/control-surface update, consistency closure, and explicit execution authorization are required.

## 14. Intended next decision

Perform a final preflight of this revised design. If it passes, freeze v0.5, propagate the governance state, and separately authorize a controlled broader discovery execution followed by Gate-A/Gate-B screening.
