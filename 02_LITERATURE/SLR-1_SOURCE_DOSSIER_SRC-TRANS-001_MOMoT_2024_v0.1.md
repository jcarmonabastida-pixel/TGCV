# SLR-1 Source Dossier — SRC-TRANS-001

**Status:** RECONSTRUCTED / WORKING
**Classification after full-text extraction:** **AC2 — STRUCTURAL EQUIVALENCE CANDIDATE; AC3 NOT ESTABLISHED**
**Source:** Eisenberg, M., Sahay, A., Di Ruscio, D., Iovino, L., Wimmer, M., & Pierantonio, A. (2024), *Multi-objective model transformation chain exploration with MOMoT*, Information and Software Technology, 174, 107500.
**DOI:** 10.1016/j.infsof.2024.107500
**Search provenance:** Q-D02, first supplementary web-discovery pass, followed by full-text structural extraction, 2026-09-07

## Bibliographic identity

Peer-reviewed open-access journal article. The publisher and repository records identify the article as Information and Software Technology 174 (2024), article 107500. citeturn2view0turn1view0

## Full-text evidence extracted

### E1 — explicit transformation-space object

The article states that MOMoT explores the transformation space spanned by a model repository and that the exhaustive search explores the entire model-transformation space defined by graph-transformation rules. citeturn2view0

### E2 — explicit possible/legitimate transformations

The paper distinguishes possible transformation chains and reports that the exhaustive approach elicits all legitimate transformation chains. The discovery process derives chains from the input model/metamodel toward a requested target, subject to compatibility and suitability conditions. citeturn1view0turn2view0

### E3 — explicit state/design-space representation

The full text states that MOMoT automatically explores alternative states in the model's design space under user-defined criteria. It describes the model design space as corresponding to the problem search space and representing the spectrum of potential solutions. citeturn2view0

### E4 — applicability/feasibility constraint

Transformation-chain construction is constrained by compatibility and suitability, and candidate additions must guarantee executability of the resulting chain. The repository discoverer constructs a graph whose nodes are models/metamodels and whose edges are transformations. citeturn2view0

### E5 — trajectory analogue

The paper explicitly represents transformation chains as ordered selections of transformations and treats feasible paths through the transformation graph as solutions. It therefore contains a clear trajectory/path analogue. citeturn2view0

### E6 — outcome/objective relation

The chain is evaluated against user-defined quality criteria, including model coverage, transformation coverage and number of transformation steps. The execution of a selected chain produces the desired output model. citeturn2view0

## TGCV structural mapping

The source can be mapped as follows, with the qualification that this is an analytical comparison rather than a claim made by the source:

| TGCV element | MOMoT analogue | Evidence status |
|---|---|---|
| `S` | concrete input/model + repository/rule configuration | supported |
| `T_acc` | legitimate/feasible transformation chains and applicable transformations | strongly supported |
| accessibility predicate | compatibility, suitability, executability and graph-rule applicability | supported |
| `ΔT_acc` | **not explicitly formulated as the research object** | absent/not established |
| `Reach` | feasible paths/chains in transformation graph | supported |
| `Trajectory` | ordered transformation chains | strongly supported |
| `Outcome` | resulting output model | supported |
| `Value` | multi-objective quality criteria / user selection utility | partially analogous, not TGCV value theory |
| mechanism changing `S` and thereby `T_acc` | **not separated as a transversal causal mechanism** | not established |

## Why AC2 is now justified

AC2 is justified because the source does more than use similar terminology. It explicitly constructs a graph/search-space representation in which:

1. a current model/configuration is represented;
2. transformations are represented as possible operations/edges;
3. only compatible/feasible/executable paths are admitted;
4. alternative states and potential solutions are explored;
5. ordered transformation chains constitute trajectories through the space;
6. resulting outputs are evaluated against explicit criteria.

This is a **structural correspondence** with substantial portions of TGCV's analytical layer around accessible transformations, reachability and trajectories. citeturn2view0

## Why AC3 is NOT established

The source still falls short of demonstrated architectural absorption in at least four decisive respects.

### 1. Transformation-space change is not the central phenomenon

MOMoT explores the search space for a given transformation problem. The paper does not formulate the temporal/dynamic question central to TGCV:

`T_acc,t ≄ T_acc,t+1`

nor does it make the change of the accessible transformation space itself the object of study.

### 2. No transversal `T_acc = F(S,C,L)` construction

The source's search space is defined by a specific model-driven transformation formalism, repository contents, metamodels and graph-transformation rules. The evidence does not establish a domain-independent accessibility construction of the form required by TGCV.

### 3. Mechanism → changed conditions → changed accessibility is not separated

The source describes transformation rules that operate on models and search procedures that explore alternatives. It does not establish the TGCV analytical separation in which an explanatory mechanism changes system conditions and the resulting conditions induce a changed accessible-transformation space.

### 4. No demonstrated transversal value-construction chain

The source has quality objectives and output selection, but this is not equivalent to TGCV's proposed transversal relation:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

## Provisional absorption assessment

**AC2 — STRUCTURAL EQUIVALENCE CANDIDATE.**

The full text confirms that this is not merely a terminology match. There is a substantial structural analogue involving state/design space, admissible transformations, feasibility, paths/chains, trajectories and outcomes.

**AC3 — ARCHITECTURAL ABSORPTION: NOT ESTABLISHED.**

The decisive missing component is the transversal architecture in which the *change in accessible transformation space* is itself the central analytical object and is related to subsequent reachability, trajectories, outcomes and value, independently of the specific transformation formalism.

## Citation-chain implications

This source should now become a citation-chain hub rather than merely another candidate. Its references and related-work section should be mined for earlier constructions involving:

- transformation spaces;
- graph transformation applicability;
- design-space exploration;
- reachability/state-space exploration;
- transformation composition and chains;
- evolving/reconfigurable transformation systems.

Those sources must receive independent dossiers before any AC3 judgement.

## Decision boundary

No TGCV Core modification is authorized. AC2 records structural proximity only. AC3 requires convergent evidence that the full TGCV architecture is already materially established in prior literature.

The EXT-1.1 negative predictive result is not used in this classification.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. Evidence, normalized facts and architectural interpretation remain separate. No historical TGCV test or Core decision is reopened.
