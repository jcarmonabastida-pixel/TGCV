# SLR-1 Source Dossier — SRC-TRANS-001

**Status:** RECONSTRUCTED / WORKING
**Initial absorption classification:** **AC2 candidate — structural equivalence requires deeper full-text verification**
**Source:** Eisenberg, M., Sahay, A., Di Ruscio, D., Iovino, L., Wimmer, M., & Pierantonio, A. (2024), *Multi-objective model transformation chain exploration with MOMoT*, Information and Software Technology, 174, 107500.
**DOI:** 10.1016/j.infsof.2024.107500
**Search provenance:** Q-D02, first supplementary web-discovery pass, 2026-09-07

## Bibliographic identity

Peer-reviewed journal article, published in 2024, open access. The JKU research portal and the journal record identify the article, authors, volume, article number and DOI. citeturn0search0turn0search1

## Retrieved evidence

The paper explicitly presents a method for **exploring possible transformation chains** residing in model repositories and states that MOMoT is used to explore the **transformation space spanned by the repository**. citeturn0search0turn0search1

The paper further states that its exhaustive search explores the **entire model transformation space defined by graph transformation rules**, allowing all possible transformation chains to be considered as solutions. Its conclusion reports that the approach elicits all legitimate transformation chains. citeturn0search0turn0search3

## TGCV mapping

Potential mapping:

- `S`: input model plus the repository/rule context;
- candidate `T_acc` analogue: legitimate model transformations / transformation chains available from the model and repository/rule configuration;
- accessibility criterion: compatibility/applicability of graph transformation rules and chain construction;
- transformation-space representation: explicit and computationally explored;
- trajectory analogue: transformation chains;
- outcome: specified output model and multi-objective quality criteria.

## Why this candidate is materially stronger

Unlike the affordance and dynamic-capabilities candidates, this source does not merely discuss change or possible action. It explicitly constructs and searches a **space of possible transformations** and treats the set of legitimate transformation chains as an object of exhaustive exploration. citeturn0search0

This makes it a genuine **AC2 candidate** for TGCV's structural layer around `T_acc`.

## Limits of present evidence

The current discovery pass does **not** yet establish AC3 architectural absorption. In particular, the retrieved abstract does not demonstrate that the source:

1. defines transformation accessibility as a general function `T_acc = F(S,C,L)` across arbitrary systems/domains;
2. makes change in the transformation space itself (`T_acc,t ≄ T_acc,t+1`) the central phenomenon;
3. separates the transformation-space object from the mechanism that changes the system conditions generating that space;
4. connects transformation-space change to reachability, trajectory, outcome and value as a transversal analytical chain;
5. claims a domain-independent ontology equivalent to TGCV.

The paper is explicitly situated in model-driven software engineering and graph transformation rules. Therefore domain specificity remains a major potential boundary against AC3.

## Provisional absorption assessment

**AC2 candidate / structural equivalence pending verification.**

The source contains an explicit transformation-space construction and an accessibility/legitimacy mechanism over transformations. This is materially closer to TGCV than the AC1 candidates.

However, **no architectural absorption decision is made yet**. Full-text extraction is required to determine whether the source's transformation space is structurally equivalent to TGCV's analytical `T_acc`, or whether it is a domain-specific search space for a narrower transformation formalism.

## Required next evidence extraction

- exact formal definition of the transformation space;
- exact definition of legitimate/applicable transformation chains;
- representation of system/input state;
- whether applicability depends on state/context;
- whether transformation-space change across system states is represented;
- whether mechanisms that alter the space are represented separately;
- treatment of reachability/trajectories;
- relationship to objectives/outcomes;
- explicit scope limitations and assumptions.

## Decision boundary

This dossier does **not** modify TGCV Core. It only elevates `SRC-TRANS-001` to the highest-priority candidate for full-text structural comparison.

No AC3 classification and no Core-change gate is authorized from the abstract-level evidence alone.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. It preserves the distinction between evidence, fact and interpretation and does not use EXT-1.1's empirical result to influence the classification.
