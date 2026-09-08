# D-OPS-3 — Alternative External Domain Discovery v0.1

**Status:** OPEN — BOUNDED DISCOVERY / NO EXECUTION AUTHORIZED  
**Date:** 2026-09-08

## 1. Purpose

Identify a second empirical domain that can provide genuine cross-domain information gain for TGCV after RUST-DYN-2, without reusing a semantically incompatible operationalization or merely reproducing already absorbed prior art.

## 2. Historical decision carried forward

D-OPS-2 did not select Organizational Capability, Reactive/Self-Adaptive Systems, or the historical CollegeMsg/Social Network candidate. No second domain is currently execution-ready.

The current evidence matrix identifies independent replication/cross-domain generalisation as the highest-value unresolved evidence class. RUST-DYN-2 remains bounded structural evidence only.

## 3. Discovery constraints

A candidate must permit, in principle:

1. observable system state S;
2. independently defined transformation universe Uτ;
3. canonical transformation identity τ;
4. pre-execution, non-circular accessibility predicate Pτ;
5. construction of T_acc and ΔT_acc without future outcomes;
6. a downstream object distinguishable from T_acc, preferably Reach;
7. deterministic temporal or counterfactual comparison;
8. reproducible public data;
9. an explicit information firewall;
10. non-trivial falsification conditions.

Convenience, dataset size, or availability alone is insufficient.

## 4. Initial discovery candidates

### A — Configurable software-system evolution / software product lines

Current external evidence indicates longitudinal datasets exist for highly configurable open-source systems. One empirical study analyzes 12 real configurable systems over 190 releases and reports configuration-space evolution across time. Another open dataset/work reports six open-source systems with feature revisions across space and time, including LibSSH, SQLite, Irssi, Bison, Curl and Marlin. These sources demonstrate empirical observability and reproducibility potential. They also provide explicit configuration structures that could support a transformation universe independent of observed performance outcomes.

**Strength:** high observability of state/configuration and explicit alternative configurations.  
**Risk:** substantial conceptual proximity to software transformation/configuration literature; must not define τ merely as a configuration change without proving non-redundancy.  
**Status:** CANDIDATE — requires D-OPS-3 compatibility audit before selection.

### B — Process-mining / operational workflow systems

Public datasets exist containing event logs and experiment results from discrete-event job-shop scheduling. Such data potentially expose state, enabled actions, alternative process transitions and temporal paths.

**Strength:** naturally temporal and transition-oriented; Reach/Trajectory may be independently represented.  
**Risk:** accessibility can easily collapse into observed event occurrence unless the enabled-action universe and admissibility predicate are specified independently of execution traces.  
**Status:** CANDIDATE — requires domain-level identifiability test.

### C — Cybersecurity / access-control policy systems

Recent public-data work demonstrates contextual access-event representations containing role, resource, location, time and action, with accept/reject policy decisions. This suggests a potentially observable transformation/accessibility space where policy changes can alter admissible actions.

**Strength:** accessibility has an explicit policy semantics and can potentially be evaluated before an action occurs.  
**Risk:** accept/reject labels and observed activity must not leak into Pτ; public datasets may encode outcomes that must be firewalled.  
**Status:** CANDIDATE — requires strict firewall and independent Uτ/Pτ audit.

## 5. Discovery assessment

At this stage no candidate is selected. The discovery evidence establishes only that these domains are plausible enough to merit a bounded compatibility audit.

Priority for the next audit should be based on expected information gain and independence from Rust:

1. **Process-mining / operational workflow** — potentially strongest domain independence and natural temporal structure.
2. **Cybersecurity/access-control policy** — potentially strongest explicit accessibility semantics.
3. **Configurable software systems** — strongest data readiness but higher semantic proximity to Rust/software transformation literature.

This ordering is provisional and is not a selection decision.

## 6. Required next operation

Perform a focused compatibility audit of the three candidates against D2-1…D2-12, with special attention to:

- whether τ can be defined independently of observed execution;
- whether Pτ is genuinely pre-execution;
- whether T_acc is not merely the set of observed actions;
- whether Reach can be defined independently of T_acc;
- whether the dataset exposes sufficient state/context to reconstruct these objects;
- whether the candidate adds information not already empirically tested by Rust.

The audit must end in **one selected domain or NO SELECTION**.

## 7. Governance boundary

**REAL-DATA EXECUTION AUTHORIZED: NO.**

No dataset download, sampling, implementation, preflight or experiment is authorized by D-OPS-3.
