# TGCV — ARCH-DISC-002 A-Reconstruction Gate Readiness v0.1

**Status:** CURRENT GOVERNANCE GATE / NOT EXECUTED
**Date:** 2026-10-01
**Candidate:** `G_T` / `O_T` from N-R8-C2 vNext

## 1. Current evidence

The canonical N-R8-C2 vNext bounded probe has an immutable PASS / IDENTIFIABLE result. The result is limited to the declared bounded fixture family and does not establish architectural non-equivalence.

Therefore the candidate has passed the transition-layer identifiability gate, but has not passed the A-reconstruction gate.

## 2. A-reconstruction question

Can the observed `O_T` distinction be reconstructed from the complete inherited A representation and its frozen admissible auxiliary vocabulary, without importing B-specific information?

The test must compare the candidate structural information against A at the representation level, not merely compare predictive performance.

## 3. Required frozen inputs

- inherited Core representation `A_Core = (S, T_acc)`;
- frozen admissible auxiliary vocabulary under the current architecture;
- canonical N-R8-C2 vNext `K_C2_vNext`;
- canonical `G_T` / `O_T` construction;
- the bounded witness pair(s) from the immutable identifiability result;
- deterministic serialization and provenance.

## 4. Required reconstruction modes

At minimum, the audit must test whether `O_T` is:

1. directly encoded in A;
2. deterministically reconstructible from A;
3. reconstructible only by adding a relation/mechanism that is already admissible under A;
4. not reconstructible under the frozen A boundary.

The fourth case is the only one capable of supporting an A-non-equivalence finding.

## 5. Fail-closed rule

An A-non-equivalence finding is not permitted if the reconstruction procedure introduces a new auxiliary representation after inspecting the witness, changes the definition of A, or uses outcome/trajectory information.

An unresolved reconstruction result is `UNDERDETERMINED`, not `AGAINST-A`.

## 6. Decision classes

**A-EQUIVALENT:** O_T is directly encoded or deterministically reconstructible under A.

**A-RECONSTRUCTIBLE-VIA-ADMISSIBLE-MECHANISM:** O_T requires an auxiliary mechanism already permitted by the frozen A boundary.

**A-NON-EQUIVALENT:** O_T contains information not reconstructible under the frozen A boundary and all observation-parity and anti-post-hoc controls pass.

**UNDERDETERMINED:** the available evidence cannot decide the reconstruction question.

## 7. Architectural consequence

Only `A-NON-EQUIVALENT` can satisfy RR3 of the Architecture Revision Readiness Register.

Even then, no Core revision follows automatically. RR4–RR10 remain necessary.

## 8. Current status

**ARCH-DISC-002 IDENTIFIABILITY: PASS (BOUNDED).**

**ARCH-DISC-002 A-RECONSTRUCTION: NOT YET AUDITED.**

No corpus expansion, statistical experiment, or scientific execution is authorized by this gate.

## 9. Next action

Perform the A-reconstruction audit on the canonical bounded witness using the frozen inherited representation and admissibility boundary. Do not generate a new corpus before that audit.
