# TGCV VSL — Evidence-to-Claim Propagation 003

## Status

**REGISTERED — BOUNDED METHODOLOGICAL / STRUCTURAL EVIDENCE**

This record registers the VSL paired A/B E1/E2 result following the completed post-E2 integrity gate and scientific interpretation gate.

## Evidence item

**Case:** VSL paired synthetic A/B execution and independent reconstruction  
**E1:** A/B canonical execution, N=100 per bundle  
**E2:** A/B independently bounded reconstruction, N=100 per bundle  
**Integrity:** E1/E2 dataset hashes agree within each bundle  
**Interpretation gate:** PASS  
**Evidence class:** bounded synthetic methodological / structural evidence

### A channel

- E1 dataset SHA-256: `6b51f7f46e75c76bfbb9e0428f8828d0b2641805c545f8cd7436a59b2cfdea58`
- E2 dataset SHA-256: `6b51f7f46e75c76bfbb9e0428f8828d0b2641805c545f8cd7436a59b2cfdea58`
- ΔT_acc = +1 for all 100 fixtures
- ΔV* = 0 for all 100 fixtures

### B channel

- E1 dataset SHA-256: `a3c7cefa75cf01ce7bd6944d845a578b652d499e6fa01ff38443c7c15e5cda03`
- E2 dataset SHA-256: `a3c7cefa75cf01ce7bd6944d845a578b652d499e6fa01ff38443c7c15e5cda03`
- ΔT_acc = +1 for all 100 fixtures
- ΔV* = 0 for all 100 fixtures

## Evidence statement

Within the frozen VSL construction, an intervention that increases the accessible transformation space can leave the realized trajectory and downstream V* unchanged under the specified deterministic BFS realization policy.

The result was independently reconstructed for both A and B.

Observed bounded pattern:

`ΔT_acc > 0` while `Δtrajectory = 0` and `ΔV* = 0`.

## Claim routing

### C02 — bounded qualification

The experiment provides additional synthetic evidence that an intervention-defined transformation-space change can be represented explicitly as a change in `T_acc`. It does not establish general empirical accessibility or validate the admissibility predicate outside the frozen construction.

**Status:** unchanged — E0.

### C07 — bounded qualification

The paired experiment provides synthetic evidence that `T_acc` can change while the realized trajectory remains unchanged. This is a controlled structural instance of accessibility-space change, not evidence of temporal change in a real system.

**Status:** unchanged — E1.

### C08 — bounded qualification

The result adds a bounded negative/qualifying case for the accessibility-to-trajectory relationship: an accessibility-space change need not alter the realized trajectory under the frozen realization policy. It does not identify a causal trajectory estimand or establish a general absence/presence rule.

**Status:** unchanged — H.

### C10 — bounded qualification

The result adds bounded methodological evidence that a positive `ΔT_acc` can coexist with `ΔV*=0` in a frozen synthetic construction. It therefore prevents interpreting accessibility-space expansion as an automatic value increase. It does not establish real-world Value, a causal `ΔT_acc → ΔV` relation, predictive value or a universal value function.

**Status:** unchanged — H.

### C16 — bounded methodological contribution

The result extends the translation protocol evidence through an independently reconstructed downstream chain preserving the distinctions among `T_acc`, realized trajectory and `V*`. It demonstrates implementation-level separation under a controlled synthetic contract.

**Status:** unchanged — H.

## No routing

No positive propagation is made to C01, C03, C04, C05, C06, C09, C11, C12, C13, C14 or C15.

## Governance effect

- No claim status changes.
- No claim level changes.
- No TGCV Core change.
- No RMA change.
- No causal claim is added.
- No industrial or transversal empirical validation is claimed.
- No completed VSL execution or reconstruction gate is reopened.
- Canonical executable bundle components remain untouched.

## Matrix action

This record is the controlled propagation source for the next cumulative Evidence-to-Claim Matrix version. The current matrix must be updated cumulatively, preserving all prior material sections and adding an enriched VSL A/B material-evidence section plus the routing above.