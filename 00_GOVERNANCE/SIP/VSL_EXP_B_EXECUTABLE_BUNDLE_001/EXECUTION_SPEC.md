# TGCV VSL Experimental Bundle B — Execution Specification 002

**Date:** 2026-09-19  
**Status:** BUNDLE DRAFT — NOT AUTHORIZED FOR EXECUTION  
**Frozen VSL:** TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_B_PETROLEUM_LCC_v0.1.md

## Synthetic scope
Synthetic methodological execution only; not evidence about real petroleum/petrochemical/natural-gas facilities.

## Paired unit
N=100 identical finite fixtures, IDs 1..100. Each fixture executes both conditions.

## Fixed transformations
Base options:
0->1 cost 6; 0->2 cost 8; 1->3 cost 5; 2->3 cost 2; 2->4 cost 5; 3->5 cost 7; 4->5 cost 2.
Treatment adds 1->4 cost 1.

## Conditions
Control = base graph. Treatment = identical graph plus intervention edge 1->4. Both execute for every fixture.

## Accessibility
Admissibility: option exists in frozen option table and endpoints are valid; no Outcome/LCC/NPV/V* input. T_acc,0=control graph; T_acc,1=treatment graph; ΔT_acc=treatment-control.

## Assignment / order
No treatment/control assignment. Primary comparison is paired within fixture. Seed 582031 is retained as bundle identifier; execution order is fixed control then treatment.

## Trajectory
Deterministic BFS from 0 to 5; ties resolved by ascending option ID, never by cost/NPV/Outcome/V*.

## Outcome / Value
O=sum of transition costs on selected trajectory. V*=-O under frozen B VSL. NPV is not substituted.

## Required outputs
For each fixture: control/treatment T_acc size, trajectories, O, V*, ΔT_acc and ΔV*. Dataset hash over canonical JSON.

## Independent reconstruction
Executor-2 reconstructs all 100 paired fixtures from frozen bundle, VSL and manifest without Executor-1 outputs/interpretations.

## Stop/failure
Fail closed on any mismatch of frozen constants, option table, trajectory rule, VSL reference or manifest integrity.

**Disposition:** OPERATIONAL BUNDLE CORRECTED — NOT FROZEN.
