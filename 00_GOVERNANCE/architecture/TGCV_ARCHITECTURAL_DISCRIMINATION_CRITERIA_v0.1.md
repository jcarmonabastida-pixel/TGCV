# TGCV — Architectural Discrimination Criteria v0.1

**Status:** CURRENT GOVERNANCE DESIGN CRITERIA / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Parent layer:** `TGCV_ARCHITECTURAL_TRANSITION_REGISTER_v0.1.md`  
**Evidence assessment:** `TGCV_ARCHITECTURAL_TRANSITION_EVIDENCE_ASSESSMENT_v0.1.md`

## Purpose

Define, before any new experiment is designed, what would constitute evidence that discriminates between the inherited architecture (A) and the TSDI architectural hypothesis (B).

This document is a **design constraint**, not a scientific result and not an execution authorization.

## 1. Competing architectural propositions

### A — inherited architecture

The explanatory object is the system state/context together with its accessible transformations. Temporal dynamics are represented through changes in the accessible transformation set and derived relations.

A sufficient representation may therefore encode:

`S_t, T_acc,t, T_acc,t+1, ΔT_acc`

plus any auxiliary relations needed for the specified analysis.

### B — TSDI hypothesis

The explanatory object includes the **structure and dynamics of the transformation space itself**.

Relevant structure may include:

- relations/dependencies among transformations;
- persistence, emergence, disappearance and reconfiguration;
- adjacency or transition structure;
- trajectories through transformation space;
- changes in the organisation of possibilities that are not reducible to set membership alone.

## 2. What would count as genuine architectural discrimination

An observation is potentially discriminating only if all of the following hold:

1. The observation is defined independently of the preferred architectural vocabulary.
2. The same underlying data can be represented under both A and B.
3. A pre-specified quantity differs between A and B in a way that can be empirically adjudicated.
4. The B-side quantity cannot be reconstructed from A without introducing an equivalent representation of the disputed structural object.
5. The result is reproducible under an independent or materially different operationalisation.

## 3. Candidate discriminating observables

The following are candidate classes, not yet selected experimental variables:

### D1 — Same accessible set, different internal organisation

Construct cases where:

`T_acc,A = T_acc,B`

but relations/dependencies among the transformations differ.

**Potential discrimination:** if future behaviour differs systematically while set membership remains identical, and the difference is predicted by the relational structure, cardinality/set membership alone is insufficient.

### D2 — Same membership change, different reconfiguration

Construct transitions with equivalent `ΔT_acc` but different structural reconfiguration.

**Potential discrimination:** if a future observable tracks reconfiguration structure rather than `ΔT_acc`, this bears directly on B.

### D3 — Dependency-sensitive reachability

Hold the immediate accessible transformation set fixed while varying dependencies between transformations.

**Potential discrimination:** if subsequent accessible trajectories differ according to dependency structure, B has an empirically relevant object beyond the instantaneous set.

### D4 — Path/trajectory equivalence test

Construct systems with equivalent initial state and equivalent instantaneous `T_acc`, but different transformation-space topology/history.

**Potential discrimination:** systematic differences in subsequent trajectories attributable to the structural history/topology would challenge an explanation based only on the instantaneous inherited representation.

### D5 — Predictive compression / reconstruction test

Require A and B to make predictions from the same frozen observations.

**Potential discrimination:** B would have to yield reproducibly different, better-calibrated predictions **because of the explicitly represented space structure**, not because B simply contains additional unconstrained variables.

## 4. Anti-discrimination traps

The following do **not** constitute evidence for B by themselves:

- observing `ΔT_acc`;
- observing persistence, expansion or contraction of `T_acc`;
- renaming existing variables as “space dynamics”;
- adding relational variables after observing the outcome;
- obtaining better fit merely by adding parameters;
- defining transformations retrospectively from downstream outcomes;
- using TSDI terminology in the measurement instrument;
- demonstrating that a dynamic representation is possible without showing that it is empirically necessary.

## 5. Minimum requirements for a future discriminating experiment

Before an experiment can enter a scientific preflight, its design must freeze:

- A representation and prediction rule;
- B representation and prediction rule;
- common input/state information;
- the structural variable that is unique to B;
- primary discriminating outcome;
- null/equivalence condition under which A and B make the same prediction;
- explicit AGAINST-A criterion;
- explicit AGAINST-B criterion;
- NON-DISCRIMINATING outcome;
- anti-circularity rule;
- complexity/equivalence control;
- independent replication or materially distinct operationalisation.

## 6. Architectural decision rule

The transition question should remain open until evidence satisfies the following sequence:

`candidate observable → preregistered A/B predictions → controlled observation → discrimination result → independent/material replication → architectural review`

Only the final architectural review may recommend changing the canonical Core.

A single significant result, improved model fit, or successful implementation of B is insufficient by itself.

## 7. Current disposition

**Status: OPEN — CRITERIA DEFINED, EXPERIMENT NOT DESIGNED.**

The next activity, if authorized, is to select one candidate discrimination class and formalize its minimal observable and controls. No scientific execution is authorized by this document.


## 8. Transition-layer admissibility constraint

The criteria above are subordinate to the inherited-architecture admissibility specification. A candidate B object is not discriminating merely because it is represented explicitly. It must first survive the pre-specified A-reconstruction test. The relevant statuses are **A-equivalent**, **A-non-equivalent**, **NON-DISCRIMINATING**, and **UNDERDETERMINED**.

An AGAINST-A result may trigger Core review only when the candidate object is independently measured, non-reconstructible under the frozen admissibility boundary, reproducibly informative, and not introduced post hoc. This remains a trigger for review, not an automatic Core revision.

The current O4/E3 route is closed because the canonical evidence does not currently contain an independently measured E3 relation. Future discrimination must therefore obtain an independently justified observable rather than inventing one to satisfy these criteria.
