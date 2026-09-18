# TGCV VSL Experimental Bundle B — Execution Specification 001
Date: 2026-09-19
Status: BUNDLE DRAFT — NOT AUTHORIZED FOR EXECUTION
Frozen VSL: TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_B_PETROLEUM_LCC_v0.1.md

## Synthetic scope
This is a synthetic methodological execution bundle. It is not evidence about real petroleum, petrochemical or natural-gas facilities.

## Unit
Each fixture is a six-state finite facility/option decision system. States are 0..5; baseline state 0; terminal state 5.

## Fixed transformations
Base directed options:
0->1 cost 6, 0->2 cost 8, 1->3 cost 5, 2->3 cost 2, 2->4 cost 5, 3->5 cost 7, 4->5 cost 2.

## Treatment
Treatment adds exactly one admissible option 1->4 cost 1. Control/reference adds no option. The intervention changes T_acc only.

## Admissibility
An option is admissible iff present in the frozen option table and endpoints are valid. No economic outcome, LCC, NPV or V* is used.

## Assignment
N=100 fixtures; IDs 1..100; Python random.Random(582031); p=0.5 treatment assignment. Seed and assignment are frozen.

## Trajectory
Deterministic breadth-first search from 0 to 5; ties resolved by ascending option identifier, never by cost/NPV/V*.

## Outcome and Value
O = sum of costs on the selected trajectory. V*=-O under the frozen B VSL. NPV is not used or substituted.

## Metrics
Report N, assignment counts, mean O, mean V*, ΔT_acc, trajectory frequencies and reconstruction hashes.

## Null/control
Control is identical to treatment fixture except the intervention edge is absent.

## Integrity
Python 3 standard library only; no external data or network. UTF-8 JSON; seed 582031.

## Independent reconstruction
Executor-2 receives only frozen bundle, manifest and VSL.

## Stop/failure
Fail closed on any mismatch in frozen constants, seed, option table, assignment, trajectory rule, VSL reference or manifest hashes.
