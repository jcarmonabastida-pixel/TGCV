# TGCV — Candidate Structural Object Admissibility Audit v0.1

**Status:** CURRENT GOVERNANCE AUDIT / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision:** ARCH-TRANS-001

## 1. Purpose

Assess candidate TSDI structural objects already visible in the accumulated evidence against the inherited-architecture admissibility specification, without designing or executing a new experiment.

This audit is a governance assessment. It does not upgrade scientific claims and does not replace the Evidence→Claim Matrix.

## 2. Candidate objects

### O1 — Accessible-transformation set change / ΔT_acc

**Admissibility:** A-ADMISSIBLE.

ΔT_acc is a derived temporal quantity over the inherited representation. It can be computed from successive T_acc states and therefore does not cross the admissibility boundary.

**Architectural status:** not a candidate new primary object.

### O2 — Persistence / expansion / contraction of T_acc

**Admissibility:** A-ADMISSIBLE as a derived descriptor.

These are properties of successive accessible sets and can be represented without introducing a new independently evolving relational object.

**Architectural status:** non-discriminating for Core revision.

### O3 — Independently evolving relation/dependency structure among transformations

**Admissibility:** NOT AUTOMATICALLY ADMISSIBLE.

A relation structure is not admissible merely because it improves prediction. It crosses the review boundary if it is independently observable, has its own temporal evolution, and cannot be derived from the frozen A representation.

**Evidence status:** candidate only. Existing evidence does not yet establish independent non-reducibility.

**Architectural status:** eligible for further admissibility analysis, not established as a new Core object.

### O4 — Connectivity/topology/reconfiguration of transformation space

**Admissibility:** NOT AUTOMATICALLY ADMISSIBLE.

If connectivity or topology is independently observed and evolves in its own right, it may constitute a candidate structural object. If it is only computed from T_acc using a declared fixed relation, it remains a derived descriptor.

**Evidence status:** MT5 and RUST-DYN-2 make this a relevant candidate, but the current evidence assessment does not establish that its structural information is non-reconstructible from A.

**Architectural status:** candidate for further analysis; not yet architecturally non-equivalent.

### O5 — Trajectories through transformation space

**Admissibility:** CONDITIONAL / POTENTIALLY A-DERIVABLE.

A trajectory computed from the frozen A representation and declared transition rules is an admissible derived temporal quantity. A trajectory-space object with independently evolving structure not derivable from A would require architectural review.

**Evidence status:** current evidence establishes operational relevance but not non-reducibility.

**Architectural status:** unresolved.

### O6 — Reconfiguration of the organisation of possibilities

**Admissibility:** NOT AUTOMATICALLY ADMISSIBLE.

This is potentially closer to the proposed TSDI architectural object because it concerns structural change beyond set membership. However, the phrase itself is not an operational object and cannot be treated as evidence.

It must be decomposed into an independently measurable structural property with a pre-specified derivation/reconstruction test.

**Architectural status:** candidate hypothesis, not an established object.

## 3. Audit conclusion

The audit identifies **no candidate that currently satisfies all five Core-revision triggers**: independent observability; independent temporal/structural evolution; non-derivability under frozen A rules; explanatory/predictive information relevant to the architectural question; and a genuine change in the primary explanatory object.

The unresolved candidate classes are O3, O4 and O6. They are listed as distinct object classes, not as a scientific ranking.

## 4. Important consequence

The current evidence supports keeping TSDI as an **architectural hypothesis under evaluation**, but does not justify modifying the canonical Core or Matrix v1.44.

In particular, ΔT_acc is not sufficient to motivate a Core revision; merely adding E_tau as an auxiliary is insufficient; terminology such as “space dynamics”, “topology” or “reconfiguration” is not itself evidence; independent observability and non-reconstructibility remain unresolved requirements.

## 5. Current gate

**ARCHITECTURAL DISCRIMINATION GATE: CLOSED.**

The next activity must define a candidate structural object operationally and test its admissibility/reconstructibility before any experimental design.

No fixture, N, power analysis, statistical model or workflow is authorized by this audit.
