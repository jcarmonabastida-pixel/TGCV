# TGCV — VSL Executable Bundle Second Integrity Audit 001

**Date:** 2026-09-19  
**Status:** CLOSED — BLOCKED PENDING CORRECTION

## Result

The A and B bundles are structurally coherent with their frozen VSLs and contain no Value circularity. However, the current executable design contains a material comparability defect:

**The specification describes a paired within-fixture intervention/reference design, but the code assigns each fixture to either treatment or control.**

Therefore the current code does not actually execute the claimed paired comparison.

## Findings

| Gate | A | B |
|---|---|---|
| Frozen VSL referenced | PASS | PASS |
| Outcome independent of V* | PASS | PASS |
| T_acc independent of Outcome/V* | PASS | PASS |
| Deterministic trajectory rule | PASS | PASS |
| Intervention structurally specified | PASS | PASS |
| Declared paired design implemented | FAIL | FAIL |
| Executor-2 reconstruction possible | CONDITIONAL | CONDITIONAL |
| Bundle executable as specified | BLOCKED | BLOCKED |

## Required correction

The unit must be a fixture with both frozen conditions:

1. control/reference: base transformation graph;
2. treatment: identical graph plus the frozen intervention edge.

For each fixture, both conditions must be executed and compared. Random assignment of a fixture to treatment/control must be removed from the primary design because it contradicts the paired specification.

If execution-order randomization is desired, it must randomize only the order in which the two already-defined conditions are executed, not whether a condition exists.

## Required output

For each fixture:
- T_acc,0;
- T_acc,1;
- ΔT_acc;
- control trajectory and Outcome;
- treatment trajectory and Outcome;
- control V*;
- treatment V*;
- within-fixture ΔV*;
- reconstruction hashes.

## Governance consequence

No execution is authorized. No VSL freeze is changed. No Core, C09, RMA or Evidence-to-Claim Matrix change is made.

The next operation is to correct both executable bundles, regenerate their manifests, and rerun this integrity audit.