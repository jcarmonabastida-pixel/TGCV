# D-OPS-4 — Cross-Domain Discovery Search v0.1

**Status:** CLOSED — NO EXECUTION-READY DOMAIN SELECTED  
**Date:** 2026-09-08

## 1. Purpose

Extend D-OPS-3 beyond software configuration, process mining and access-control systems, seeking a genuinely external empirical domain with observable rule-governed transformations and public reproducible data.

## 2. Discovery candidates reviewed

### A — Public transport network / timetable systems

Aalto/Scientific Data provides curated public-transport network datasets for 25–27 cities in edge-list, temporal-event, SQLite, GeoJSON and GTFS formats, with public archival copies. citeturn0search1turn0search2turn0search6

Potential TGCV mapping:
- S: network/timetable state;
- Uτ: route/service/network modifications;
- Pτ: schedule/network validity constraints;
- T_acc: admissible network transformations;
- Reach: successor network/service configurations.

Blocker: the canonical dataset is primarily a spatial/temporal extract of operations, including representative week periods, rather than a longitudinal sequence of independently versioned network states. Therefore ΔT_acc over genuine state evolution cannot currently be identified without importing an external version history. **Not selected.**

### B — CNC manufacturing / changeover systems

A 2025 open Scientific Data descriptor provides 30 manufacturing sessions, five complete changeover matrices, three products, 170 recorded features and explicit changeover-process documentation. The changeover matrix represents all considered setup transitions between products. citeturn0search0

Potential TGCV mapping:
- S: machine/setup state;
- Uτ: product/setup transformation;
- Pτ: technically admissible changeover;
- T_acc: admissible setup transformations;
- Reach: successor setup configurations.

Blocker: the dataset is excellent for independent rule-governed transformation structure but has only three products and repeated sessions under essentially the same changeover universe. It therefore offers little evidence for temporal ΔT_acc; using measured changeover times as accessibility would be circular. **Not selected for replication.**

### C — Longitudinal biological evolution / protein sequences

A public Dryad dataset contains HIV-1 protease sequences spanning nine years and paired before/after treatment sequences from the same patients. citeturn1search0

Potential TGCV mapping:
- S: sequence/genotype state;
- Uτ: sequence mutations;
- Pτ: biologically admissible mutation under defined sequence constraints;
- T_acc: accessible sequence transformations;
- Reach: potential sequence states.

Blocker: accessibility would require a defensible pre-execution biological admissibility model. The observed evolutionary sequence and treatment history cannot themselves define Pτ. A separate mechanistic mutation/admissibility model would have to be frozen independently of the dataset. This is a potentially high-information domain but is not currently operationally ready. **Retain as research candidate, not selected.**

### D — Architectural design-process evolution

A 2026 Mendeley dataset provides 376 design moves from six architectural design protocols, with temporal/linkographic measures. citeturn1search2

Potential TGCV mapping:
- S: evolving design graph;
- Uτ: design moves;
- Reach: potential subsequent design states.

Blocker: the dataset records observed design moves and retrospective structural measures. It does not provide an independently specified universe of admissible alternative design moves or a pre-execution accessibility predicate. **Not selected.**

### E — Longitudinal human-cell / metabolomics systems

Public longitudinal biological datasets exist with repeated measurements over time, including longitudinal RNA-sequencing across cellular lifespan and time-resolved metabolomics repositories. citeturn1search4turn1search5

Blocker: these datasets primarily expose observed state trajectories, not an independently enumerable transformation universe with a pre-execution admissibility predicate. Their use would risk redefining accessibility from observed biological change. **Not selected.**

## 3. Comparative assessment

| Candidate | Domain independence | Uτ independent | Pτ pre-execution | ΔT_acc identifiable | Public reproducibility | Decision |
|---|---:|---:|---:|---:|---:|---|
| Public transport | High | Conditional | Conditional | Fail | Pass | Reject |
| CNC manufacturing | High | Pass | Conditional | Fail | Pass | Reject |
| Protein evolution | High | Conditional | Conditional | Conditional | Pass | Retain |
| Architectural design | High | Conditional | Fail | Fail | Pass | Reject |
| Longitudinal biology | High | Fail/Conditional | Fail | Fail | Pass | Reject |

## 4. D-OPS-4 decision

**NO EXECUTION-READY DOMAIN SELECTED.**

The search has nevertheless identified a new high-information candidate class: **longitudinal protein evolution under independently specified mutation/admissibility rules**.

This candidate is scientifically attractive because it is outside software systems and organizational/process domains, while its transformation identity (mutation) is naturally discrete and its longitudinal data are public. However, TGCV must not manufacture Pτ from observed evolutionary trajectories or fitness/outcome data.

## 5. Next controlled operation

Open **D-OPS-5 — Protein-Evolution Admissibility and Transformation Identifiability Audit**.

The audit must answer, before any dataset acquisition or implementation:

1. Can a mutation universe Uτ be defined independently?
2. Can Pτ be defined from sequence/biophysical constraints without using observed future mutations, treatment response or fitness?
3. Can T_acc be computed before execution/evolution?
4. Can Reach be represented as a distinct downstream object?
5. Can ΔT_acc be compared longitudinally without outcome leakage?
6. Does this domain provide genuinely new information beyond Rust?

Only if these conditions pass may a domain operational specification be designed.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
