---
content_id: TV-LR-001
language_pair_id: TV-LR-001
title: "Observing the reconfiguration of the transformation space in two domains"
language: en
content_type: research_note
status: draft
version: 0.1
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "A bounded methodological evidence note on reconstructing changes in accessible transformation spaces across two computational domains."
part: null
chapter: null
parent_id: null
tags:
  - research-evidence
  - transformation-space
  - cross-domain-method
concepts:
  - TV-TERM-001
prerequisites: []
related:
  - TV-CH-03
references:
  - TV-REF-004
  - TV-REF-005
epistemic_status:
  - bounded_methodological_evidence
source_assets:
  - 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.47.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_CROSS_DOMAIN_OPERATIONALISATION_UPDATE_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_VISITALL_DYNAMIC_SPACE_SCIENTIFIC_EVALUATION_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_GATE_A_A1_A5_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_LEADER_SYNC_A6_RECONSTRUCTION_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_GATE_A_A7_DOMAIN_BOUNDARY_AUDIT_001.md
license: null
---

# Observing the reconfiguration of the transformation space in two domains

## Purpose

This note summarises a bounded methodological analysis that examined whether the same analytical structure could be used to reconstruct the evolution of accessible transformation spaces in two computational domains with different semantics.

The question was not whether this representation was superior to the native representations of either domain, nor whether the observed changes produced value. The analysis examined whether the system state, accessible transformations, realised transformation, successor state and successor accessible space could be identified and related consistently.

## The two domains examined

**Grid-movement planning.** The first domain comes from a grid-visit planning problem published in the Potassco PDDL instances repository. One grid instance of size five was examined, with exhaustive exploration to depth two. Candidate transformations are the movements permitted by the connectivity and position conditions defined in the original problem.

**Probabilistic process coordination.** The second domain comes from a distributed leader-election model published in the PRISM examples repository. The model represents three processes arranged in a ring and uses synchronised commands, guards and probabilistic alternatives. Transformation identities correspond to the action labels defined by the model itself.

The domains do not share the same transformations or semantics. The comparison does not equate a grid movement with an action in the probabilistic model.

## Analytical procedure

The following sequence was reconstructed in both cases:

\[
S_t \rightarrow T_{acc,t} \rightarrow T_{real,t}
\rightarrow S_{t+1} \rightarrow T_{acc,t+1}
\]

From the accessible spaces in the two states, the analysis derived descriptors of persistence, added identities, removed identities, turnover and net change in cardinality. Set operations were performed within each domain; the cross-domain comparison was limited to the structure of the descriptors.

The source evidence had already been frozen. The comparative analysis was a secondary elaboration of those records, not a new scientific execution. For each transition, the initial accessible space was derived from the source state, and the successor space was recalculated from the reconstructed successor state. Independent grid reconstructions agreed on the structure of the tree, with 21 nodes and 20 edges. In the probabilistic model, the two executors each reconstructed 25 records, with matching source fingerprints and zero structural deviations. An independent mathematical audit subsequently reviewed all 36 comparative records and their derived descriptors.

## Results

The comparative analysis assembled **36 transition records**: 20 from the grid-planning domain and 16 from the probabilistic model. The analysis identified no invalid records. The mathematical audit checked all 36 records and found no discrepancies in the calculated descriptors.

### Grid-planning domain

Identity turnover was observed in all 20 transitions: new accessible transformations appeared and others ceased to be accessible. The mean cardinality of the space changed from 4.0 to 3.8. The initial state had four accessible movements.

This result has an important limitation. The domain-specific scientific audit showed that both the set of accessible movements and its changes could be reconstructed completely from the problem's conventional representation of states, actions and transitions. Therefore, in this instance, a distinct representational gain from explicitly introducing the accessible transformation space was not demonstrated.

This negative result is retained as part of the evidence; the domain definitions were not modified to avoid it.

### Probabilistic coordination model

Across the 16 transitions, the mean cardinality of the accessible space remained at 1.0 before and after the transition. However, the identity of the accessible transformation changed in every record. The number of options remained the same, but the available option was replaced.

This pattern illustrates why cardinality, considered in isolation, does not describe the full reconfiguration of a transformation space.

## What the analysis supports

The result supports a bounded methodological conclusion: in these two computational examples, with different domain semantics and explicit accessibility rules, it was possible to reconstruct the relationship between state, accessibility, realisation, successor state and successor accessibility, and to derive comparable descriptors without equating transformation identities across the two domains.

The evidence supports treating this structure as a form of cross-domain operationalisation in the cases examined. It does not demonstrate that it works in every system or that it is a necessary or superior representation.

## What it does not demonstrate

The analysis does not demonstrate:

- cross-domain validity or universality;
- explanatory or representational superiority over native models;
- that the accessible space is a new ontological primitive;
- that accessibility changes cause changes in trajectories;
- effects on downstream outcomes or value creation;
- Transformational Intelligence as a demonstrated capability;
- practical utility in deployed systems.

In addition, the reconstruction of the probabilistic model directly encoded the semantics of the frozen model; it was not a new execution of the PRISM engine. Although the domain sources are publicly identified and the independent reconstructions agreed, this note does not yet include a self-contained public package containing the executors and the 36 derived records. Therefore, audited reconstruction agreement should not be confused with independent reproduction by any reader from this note.

## Domain sources

- Potassco. *PDDL instances covering the International Planning Competitions*. Pinned repository revision: [potassco/pddl-instances](https://github.com/potassco/pddl-instances/tree/cf19edf7c53d1540ddbb396c642595e0926ee552).
- PRISM Model Checker. *PRISM Benchmark Suite — synchronous leader-election model*. Pinned file and revision: [leader_sync3_2.pm](https://github.com/prismmodelchecker/prism-benchmarks/blob/59ee49c031dbdfdb1e606edcdd643410de32192b/models/dtmcs/leader_sync/leader_sync3_2.pm).

## Relationship to the chapter

This note complements the chapter **The Space of Accessible Transformations**. Its purpose is to document the scope of a specific methodological result, including its limitations and the negative result obtained in one of the domains.
