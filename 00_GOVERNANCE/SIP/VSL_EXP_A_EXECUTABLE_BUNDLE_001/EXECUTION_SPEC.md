# TGCV VSL Experimental Bundle A — Execution Specification 001
Date: 2026-09-19
Status: BUNDLE DRAFT — NOT AUTHORIZED FOR EXECUTION
Frozen VSL: TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_A_BUILT_ASSETS_LCC_v0.1.md

## Synthetic scope
This is a synthetic methodological execution bundle. It is not evidence about real buildings or infrastructure.

## Unit
Each fixture is a six-state finite built-asset decision system. States are 0..5. Baseline state is 0; terminal state is 5.

## Fixed transformations
For every fixture, the base directed edges are:
0->1 cost 4, 0->2 cost 7, 1->3 cost 5, 2->3 cost 2, 2->4 cost 6, 3->5 cost 8, 4->5 cost 3.
Each edge has a stable identifier in the execution code.

## Treatment
Treatment adds exactly one admissible edge selected by the frozen fixture seed:
1->4 cost 1.
Control/reference adds no edge.
The intervention changes T_acc only; all other base state/edge definitions remain unchanged.

## Admissibility
An edge is admissible iff it exists in the fixture edge table and both endpoint states are valid. No outcome, cost total, or V* is used by the predicate.

## Assignment
N=100 fixtures. Fixture IDs 1..100. Assignment is deterministic pseudorandom using Python's random.Random(582031). For each fixture, one Bernoulli draw p=0.5 assigns treatment/control. The seed, N and assignment rule are frozen.

## Trajectory
Deterministic breadth-first search from state 0 to state 5; ties resolved by ascending edge identifier. The trajectory rule does not inspect cost, LCC, Outcome or V*.

## Outcome and Value
Outcome O = sum of transition costs on the selected trajectory.
V* = -O, exactly implementing the frozen A valuation convention V*=-LCC.
Reference contrast = V*_treatment - V*_control is computed only across paired fixture conditions; primary fixture-level treatment indicator is assigned before execution.

## Metrics
Report N, treatment/control counts, mean O by assignment, mean V* by assignment, mean ΔT_acc (edge-count difference), trajectory identity frequencies, and exact reconstruction hashes.

## Null/control
Control is the identical fixture without the added 1->4 edge.

## Integrity
No external data. Python 3 standard library only. UTF-8 JSON. Frozen seed 582031. No network access.

## Independent reconstruction
Executor-2 must use only this bundle, its manifest, and the frozen VSL; no Executor-1 outputs or interpretations.

## Stop/failure
Fail closed if any frozen constant, seed, edge table, assignment, trajectory rule, VSL reference, or hash differs from the manifest.
