# Executor-2 Reconstruction Package A — Specification 001

**Status:** READY FOR FREEZE AUDIT — NOT EXECUTED
**Purpose:** independent reconstruction of the paired A bundle.

Executor-2 must receive only:
- corrected A execution specification;
- corrected A execute.py;
- A manifest;
- frozen A VSL;
- declared Python 3 environment.

Executor-2 must reconstruct all 100 fixtures and independently verify:
1. control and treatment graphs;
2. T_acc,0 and T_acc,1;
3. ΔT_acc;
4. both trajectories;
5. O and V* for both conditions;
6. ΔV*;
7. canonical dataset hash.

Executor-2 must not receive Executor-1 outputs, interpretations, expected effect direction, or derived results before reconstruction.

Any mismatch is a STOP condition. No reconciliation by editing the reconstruction is permitted.