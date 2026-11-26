---
content_id: TV-LR-001
language_pair_id: TV-LR-001
title: "Observing transformation-space reconfiguration across two domains"
language: en
content_type: learning_resource
status: draft
version: 0.2
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

# Observing transformation-space reconfiguration across two domains

## Purpose

This note summarises a bounded methodological analysis examining whether a common analytical structure could be used to reconstruct the evolution of accessible transformation spaces in two computational domains with different semantics.

The question was not whether the representation was superior to each domain's native representation, nor whether the observed changes produced value. The analysis examined whether state, accessible transformations, the realised transformation, the successor state and the subsequent accessible space could be identified and related consistently.

## The two domains examined

**Grid-movement planning.** The first domain comes from a grid-visit planning problem published in Potassco's PDDL instance repository. A five-by-five grid instance was examined through exhaustive exploration to depth two. Candidate transformations are the moves permitted by the position and connectivity conditions defined in the original problem.

**Probabilistic process coordination.** The second domain comes from a distributed leader-election model published in the PRISM examples repository. The model represents three processes arranged in a ring and uses synchronised commands, guards and probabilistic alternatives. Transformation identities correspond to the action labels defined by the model itself.

The domains do not share the same transformations or semantics. The comparison does not equate a grid move with an action in the probabilistic model.

## Analytical procedure

The following sequence was reconstructed in both cases:

\[
S_t \rightarrow T_{acc,t} \rightarrow T_{real,t}
\rightarrow S_{t+1} \rightarrow T_{acc,t+1}
\]

Descriptors for persistence, added identities, removed identities, turnover and net cardinality change were derived from the accessible spaces at the two states. Set operations were performed within each domain; cross-domain comparison was limited to the structure of the descriptors.

The source evidence had already been frozen. The comparative analysis was a secondary analysis of those records, not a new scientific execution. For each transition, the initial accessible space was derived from the source state, while the successor space was recomputed from the reconstructed successor state. The independent grid-planning reconstructions agreed on the 21-node, 20-edge tree structure. In the probabilistic model, the two executors each reconstructed 25 records, with a matching source-fixture hash and zero structural deviations. An independent mathematical audit then checked the 36 comparative records and their derived descriptors.

## Results

The comparative analysis contained **36 transition records**: 20 from the grid-planning domain and 16 from the probabilistic model. The analysis identified no invalid records. The mathematical audit checked all 36 records and found no discrepancies in the calculated descriptors.

### Grid-planning domain

Identity turnover was observed in all 20 transitions: new accessible transformations appeared and others were no longer accessible. Mean space cardinality changed from 4.0 to 3.8. Four moves were accessible in the initial state.

This result has an important limitation. The domain-specific scientific audit found that both the accessible-move set and its changes could be fully reconstructed from the problem's conventional state, action and transition representation. Distinct representational gain from explicitly introducing the accessible transformation space was therefore not demonstrated in this instance.

This negative result is retained as part of the evidence; the domain definitions were not changed to avoid it.

### Probabilistic coordination model

Across the 16 transitions, mean accessible-space cardinality remained at 1.0 before and after the transition. However, the identity of the accessible transformation changed in every record. The number of options remained constant, but the available option was replaced.

This pattern illustrates why cardinality alone does not describe the full reconfiguration of a transformation space.

## What the analysis supports

The bounded methodological finding is that, in these two computational examples with different domain semantics and explicit accessibility rules, it was possible to reconstruct the relationship among state, accessibility, realisation, successor state and successor accessibility, and to derive comparable descriptors without equating transformation identities across domains.

The evidence supports treating this structure as a form of cross-domain operationalisation in the cases examined. It does not show that the procedure works in every system or that it is a necessary or superior representation.

## What it does not demonstrate

The analysis does not demonstrate:

- transversal or universal validity across domains;
- explanatory or representational superiority over native models;
- that the accessible space is a new ontological primitive;
- that accessibility changes cause trajectory changes;
- effects on downstream outcomes or value creation;
- Transformational Intelligence as a demonstrated capability;
- practical usefulness in deployed systems.

In addition, the probabilistic model reconstruction encoded the frozen model semantics directly; it was not a new execution of the PRISM engine. Although the domain sources are publicly identified and the independent reconstructions agreed, this note does not yet include a standalone public package containing the executors and all 36 derived records. Audited reconstruction agreement should therefore not be confused with independent reproduction by any reader from this note alone.

## Domain sources

- Potassco. *PDDL instances covering the International Planning Competitions*. Pinned repository revision: [potassco/pddl-instances](https://github.com/potassco/pddl-instances/tree/cf19edf7c53d1540ddbb396c642595e0926ee552).
- PRISM Model Checker. *PRISM Benchmark Suite — synchronous leader-election model*. Pinned file and revision: [leader_sync3_2.pm](https://github.com/prismmodelchecker/prism-benchmarks/blob/59ee49c031dbdfdb1e606edcdd643410de32192b/models/dtmcs/leader_sync/leader_sync3_2.pm).

## Relationship to the chapter

This note supplements the chapter **The Space of Accessible Transformations**. Its purpose is to document the scope of a specific methodological result, including its limitations and the negative result obtained in one of the domains.
