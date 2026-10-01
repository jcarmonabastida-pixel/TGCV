# TGCV — ARCH-DISC-002 A-Reconstruction Audit Specification v0.1

**Status:** GOVERNANCE SPECIFICATION / NOT EXECUTED
**Date:** 2026-10-01
**Candidate:** `G_T` / `O_T` from N-R8-C2 vNext

## 1. Purpose

Determine whether the bounded positive witness for `O_T` variation can be reconstructed from the inherited architecture A without importing B-specific information.

## 2. Frozen A boundary

The reconstruction model is restricted to the inherited working architecture:

`A_Core = (S, T_acc)`

plus only those auxiliary relations/mechanisms explicitly admissible in the current architecture before inspection of the witness.

No new structural relation may be introduced because it reproduces `O_T`.

## 3. Witness scope

The audit shall use only the immutable N-R8-C2 vNext witness states and their frozen provenance. It shall not expand the fixture or generate a new scientific corpus.

## 4. Reconstruction hierarchy

Test in this fixed order:

1. **Direct encoding:** Is `O_T` already a function explicitly represented in A?
2. **Deterministic derivation:** Is `O_T = f(A)` uniquely determined by the complete inherited representation?
3. **Admissible mechanism:** Can `O_T` be reconstructed using a relation/mechanism already explicitly admissible under A?
4. **Non-reconstructibility:** Does some `O_T` distinction remain after all three prior routes are exhausted?

Later stages must not be used to reinterpret an earlier negative stage.

## 5. Information-parity rule

Both witness states must be reconstructed from exactly the same categories of A information. The audit must not grant the reconstruction procedure access to `O_T`, future outcomes, trajectories, or witness labels as explanatory inputs.

## 6. Decision classes

**A-EQUIVALENT** — direct or deterministic reconstruction succeeds.

**A-RECONSTRUCTIBLE-VIA-ADMISSIBLE-MECHANISM** — reconstruction succeeds using an auxiliary mechanism already admitted by A.

**A-NON-EQUIVALENT** — a stable `O_T` distinction remains that cannot be reconstructed under the frozen A boundary.

**UNDERDETERMINED** — the current A boundary is insufficiently specified to decide.

## 7. Required evidence

The audit record must identify, for each reconstruction route:

- exact A inputs used;
- exact transformation/state operations used;
- whether the operation was already admissible before the witness;
- deterministic output;
- equality/difference against the observed `O_T`;
- provenance hashes.

An assertion that a relation is 'available in principle' is insufficient; admissibility must be traceable to canonical governance material.

## 8. Fail-closed conditions

Return `UNDERDETERMINED` rather than `A-NON-EQUIVALENT` if:

- the A auxiliary vocabulary is ambiguous;
- the witness does not contain enough provenance;
- the reconstruction requires a newly introduced relation;
- the construction depends on outcome/trajectory information;
- the two states do not have comparable A representations.

## 9. Architectural consequence

Only `A-NON-EQUIVALENT` can satisfy RR3.

Even `A-NON-EQUIVALENT` does not revise the Core or Matrix automatically. RR4–RR10 of the Architecture Revision Readiness Register remain mandatory.

## 10. Current status

**IDENTIFIABILITY: PASS (bounded).**

**A-RECONSTRUCTION: SPECIFICATION READY / NOT EXECUTED.**

No scientific execution, corpus expansion, statistical analysis or Core/Matrix revision is authorized.
