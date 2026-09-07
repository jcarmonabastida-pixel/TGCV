# SLR-1 Source Dossier — SRC-MOMOT-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Bill, R., Fleck, M., Troya, J., Mayerhofer, T., & Wimmer, M. (2019), *A Local and Global Tour on MOMoT*, Software and Systems Modeling, 18(2), 1017–1046.
**DOI:** 10.1007/s10270-017-0644-3
**Initial classification:** **AC2 — STRUCTURAL EQUIVALENCE CONFIRMED; AC3 NOT ESTABLISHED**

## Bibliographic identity

Peer-reviewed journal article, 30 pages, published in *Software and Systems Modeling*. The repository record confirms the authors, journal, volume, pages and DOI. citeturn0search0

## Research object of the source

MOMoT addresses model-transformation scenarios in which different execution strategies are needed to obtain high-quality output models. The paper states that transformation problems can span a very large search space of possible transformation results and studies local and global search strategies for exploring that space. citeturn0search1turn2search1

The source therefore treats transformation search as an explicit search problem, not merely as execution of a predetermined transformation.

## Evidence extraction

### E1 — explicit transformation-result search space

The paper explicitly characterizes model-transformation problems as spanning a large search space of possible transformation results. This is a direct prior-art representation of a transformation-result space. citeturn0search1turn2search1

### E2 — initial model and transformation rules

MOMoT assumes a problem instance with an initial model and an existing set of transformation rules. Henshin supplies the transformation-rule language and transformation engine. The search then computes rule-application sequences. citeturn2search8turn2search12

### E3 — accessibility/applicability through executable rule applications

A transformation is not simply the abstract rule: the paper distinguishes the problem of finding the best sequence of rule applications for a given set of transformation rules. In the in-place setting, those rules rewrite the current input model to produce output models. citeturn2search12turn0search22

This establishes a strong operational analogue of an accessibility predicate: the sequence must consist of executable/applicable rule calls in the evolving model context.

### E4 — trajectory representation

MOMoT encodes candidate solutions as transformation-rule application sequences. The search algorithms modify these sequences through local and global search operators. citeturn2search12turn2search0

### E5 — state/result evolution

The model is progressively transformed by applying the selected rule sequence. A later 2024 synthesis of MOMoT describes the same architecture as: execute a transformation rule → obtain objective fitness and a transformed model as successor state. citeturn2search8

### E6 — objective/value analogue

The transformed model is evaluated against explicit objectives and constraints. The purpose is to identify high-quality transformation results, and the framework supports multi-objective search. citeturn2search0turn2search8

### E7 — local/global exploration of the same transformation problem

The principal contribution of the 2019 paper is extending MOMoT to local as well as global search, enabling comparison of search strategies and their exploration of the transformation-result space. This changes the search strategy, not the underlying definition of the transformation space. citeturn0search1turn2search1

### E8 — explicit relationship to Abdeen et al. 2014

The paper identifies Abdeen et al. as the most related prior approach: both address finding optimal sequences of rule applications and multi-objective exploration of graph transformation systems. MOMoT differentiates itself primarily by providing a loosely coupled framework that can reuse different optimization algorithms rather than integrating one specific optimization approach into a transformation engine. citeturn0search23

## TGCV structural mapping

| TGCV element | MOMoT analogue | Assessment |
|---|---|---|
| `S` | initial problem-instance model plus transformation context | strong analogue |
| `T_acc` | executable/applicable rule applications and feasible rule-application sequences | strong structural analogue |
| accessibility predicate | applicability/executability of rule applications in the current model context | strong operational analogue |
| `Reach` | models/results reachable through rule sequences | explicit |
| `Trajectory` | ordered transformation-rule application sequence | explicit |
| `Outcome` | resulting transformed model | explicit |
| `Value` | objective/fitness vector and quality of transformed model | partial analogue |
| `ΔT_acc` | change in the set of accessible transformations itself | **not explicit** |
| mechanism changing accessibility | rule application changes the model and can thereby affect subsequent applicability, but this is not isolated as a transversal causal construct | **not established** |

## AC2 assessment

**AC2 — STRUCTURAL EQUIVALENCE CONFIRMED.**

MOMoT independently and explicitly contains the following architecture:

`initial model → applicable transformations → transformation sequence → resulting model → objective evaluation`

The source therefore materially overlaps TGCV's structural layer involving transformation accessibility, reachability, trajectory and outcome evaluation. This is substantially beyond terminology similarity and is not merely an optimization algorithm analogy.

The 2019 paper also explicitly connects its framework to Abdeen et al. 2014, confirming that the structural antecedent is a coherent prior-art lineage rather than an isolated publication. citeturn0search23

## AC3 assessment

**AC3 — ARCHITECTURAL ABSORPTION NOT ESTABLISHED.**

The critical distinction remains:

### 1. MOMoT searches a transformation space; it does not theorize its endogenous change

The transformation space is treated as the search space generated by the available transformation rules and their executable applications. The scientific problem is how to search that space effectively and find high-quality results. citeturn0search1turn2search12

TGCV instead makes a different transition central:

`conditions/state change → change in accessible transformation space → changed reachability/trajectory → later outcome/value consequences`.

### 2. State-dependent applicability is present, but not elevated to a transversal phenomenon

Because transformations are applied to the evolving model, applicability can change after previous transformations. Thus MOMoT contains a *dynamic operational accessibility* phenomenon in the narrow sense that the next executable rule calls depend on the current model.

However, the source does not formulate the change of this accessibility relation itself as an analytical object `ΔT_acc`, nor does it investigate the conditions under which the transformation space expands, contracts, reconfigures or substitutes across system states.

### 3. No general mechanism layer corresponding to TGCV's explanatory role of `I`

MOMoT treats transformation rules as operators in a search procedure. It does not separate a domain-transversal mechanism that modifies system conditions and thereby modifies future accessibility.

### 4. Value remains optimization fitness, not construction-of-value architecture

MOMoT evaluates transformed models using objectives. This is relevant prior art for the outcome/evaluation side of TGCV, but it does not establish the TGCV theoretical chain linking changes in transformation accessibility to trajectories and value construction across domains.

## Important methodological implication

MOMoT creates a stronger falsification burden for any TGCV claim that the following are themselves novel:

- representing transformation spaces;
- representing possible/feasible transformations;
- rule applicability as a condition on transformation execution;
- reachability through transformation sequences;
- trajectories as ordered transformation chains;
- optimization/evaluation over resulting states.

Those elements are demonstrably established in MDE/search-based transformation literature. citeturn0search23turn2search0

The potentially distinctive TGCV claim is narrower: **the analytical elevation of changes in the accessible-transformation relation itself, independently of a specific transformation language, search algorithm or optimization problem, and its connection to subsequent reachability, trajectories, outcomes and value.**

## Relation to SRC-DSE-001

Abdeen et al. (2014) and Bill et al. (2019) should be treated as the same strong prior-art cluster for the structural layer. Bill et al. explicitly describes Abdeen et al. as the most related approach and positions MOMoT mainly as a more loosely coupled and algorithm-flexible search framework. citeturn0search23

Accordingly, the chain now supports a consolidated finding:

**Transformation-space representation + rule-based accessibility + reachable candidates + transformation trajectories + objective evaluation = established prior art.**

No evidence in this source establishes that the literature has already absorbed the stronger TGCV architectural proposition concerning *change of the accessibility structure itself*.

## Decision boundary

- **SLR-1 status for this source:** AC2 confirmed.
- **AC3:** not established.
- **TGCV Core:** unchanged.
- **EXT-1.1:** not used in classification.
- **No post-hoc modification of prior experimental records.**

## Next controlled operation

Proceed to `SRC-MDEO-001` — Burdusel, Zschaler & Strüber, *MDEOptimiser: A Search Based Model Engineering Tool* (2018), to determine whether the same structural architecture is reproduced independently and whether it adds any element relevant to the AC3 boundary.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. Evidence, facts and architectural interpretation are intentionally separated.