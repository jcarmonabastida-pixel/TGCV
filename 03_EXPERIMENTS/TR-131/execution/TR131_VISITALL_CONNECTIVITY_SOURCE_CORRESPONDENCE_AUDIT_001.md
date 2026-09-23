# TR-131 VisitAll Connectivity Source Correspondence Audit 001

**Status:** PASS — CONNECTIVITY CORRESPONDENCE VERIFIED / SCIENTIFIC EXECUTION CONTINUATION GATED  
**Date:** 2026-09-23

## Purpose

Verify that the connectivity relation used by the frozen VisitAll Runner and the independent Executor-2 reconstruction corresponds exactly to the source-defined `connected` relation of the pinned `grid-5` PDDL problem.

This audit does not execute the scientific experiment and does not infer a scientific result.

## Frozen source

- Repository: `potassco/pddl-instances`
- Revision: `cf19edf7c53d1540ddbb396c642595e0926ee552`
- Problem: `grid-5`
- PDDL blob SHA: `f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34`
- Path: `ipc-2014/domains/visit-all-sequential-optimal/instances/instance-1.pddl`

## Source-defined connectivity

The pinned PDDL defines the VisitAll grid connectivity through the problem facts. For the 5x5 grid, the source relation contains exactly the orthogonal directed adjacency relation:

- horizontal directed edges: 5 rows × 4 adjacent pairs × 2 directions = 40
- vertical directed edges: 5 columns × 4 adjacent pairs × 2 directions = 40
- total directed `connected` facts: **80**

The relation is therefore equivalent to the bounded-grid construction used by the experiment:

`(x,y) -> (x-1,y), (x+1,y), (x,y-1), (x,y+1)`

with coordinates restricted to `0..4`.

No diagonal, wrap-around, or additional connectivity relation is introduced by the experiment.

## Implementation correspondence

### Runner

Frozen Runner SHA-256:

`696a41fcdaf3eed8dd9d4b8ec18cbedf190f7fce9d89d2f6b4703f5f83e89cba`

Its `build_connected()` construction enumerates every coordinate in `0..4 × 0..4` and adds exactly the four orthogonal neighbors that remain inside the same bounds.

### Executor-2

Current independent reconstruction SHA-256:

`03b3c8b8b1c2ed419900eaa2f33281c4496005a7`

Its `build_connected()` construction is the same bounded orthogonal adjacency rule and is independently implemented in the reconstruction.

## Correspondence checks

| Check | Result |
|---|---|
| Pinned source problem identified | PASS |
| Pinned PDDL blob identified | PASS |
| Source grid dimensions = 5×5 | PASS |
| Source directed connectivity = 80 facts | PASS |
| Runner uses bounded orthogonal 5×5 connectivity | PASS |
| Executor-2 uses bounded orthogonal 5×5 connectivity | PASS |
| No diagonal connectivity | PASS |
| No wrap-around connectivity | PASS |
| No additional TGCV connectivity semantics | PASS |
| Runner root T_acc agrees with frozen source-lock T_acc | PASS |
| Scientific execution performed by this audit | NO |
| Scientific conclusion inferred by this audit | NO |

## Boundary

This audit establishes correspondence between the pinned source connectivity and the deterministic connectivity representation used by the Runner and Executor-2.

It does **not** establish that T_acc is theoretically irreducible, that ΔT_acc has explanatory superiority over the baseline, or any relationship to value.

The scientific interpretation remains pending independent Executor-2 reconstruction and comparison.

## Decision

**PASS.**

The connectivity representation is not a remaining source-traceability blocker for the VisitAll Dynamic Transformation Space experiment.

**Next gate:** bring Executor-2 to the same explicit scientific-authorization standard as Executor-1, then execute the independent reconstruction and compare it against the persisted Executor-1 result.
