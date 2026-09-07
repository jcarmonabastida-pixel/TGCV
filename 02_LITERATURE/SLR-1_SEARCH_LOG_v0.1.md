# TGCV SLR-1 — Search Log v0.1

**Status:** RECONSTRUCTED / WORKING
**Type:** normative search-record template; partially populated with supplementary web-discovery and citation-chaining passes.
**Protocol:** `SLR-1_OPERATIONAL_PROTOCOL_v0.1_RECONSTRUCTED.md`
**Date frozen:** 2026-09-07

## 5. Citation-chain register — MOMoT

`SRC-TRANS-001` was classified AC2 after full-text extraction. Citation chaining was therefore initiated as a falsification operation, not as enrichment.

### CH-0001 — backward conceptual/technical chain

**Parent:** `SRC-TRANS-001` — Eisenberg et al. (2024), MOMoT.

**Search date:** 2026-09-07.

**Sources surfaced for independent screening:**

1. **Bill et al. — *A local and global tour on MOMoT* (2019), DOI 10.1007/s10270-017-0644-3.** The article describes transformation problems as spanning a very large search space of possible transformation results and develops local/global search over model-transformation orchestrations.
2. **Abdeen et al. — *Multi-Objective Optimization in Rule-Based Design Space Exploration* (2014).** The paper explicitly treats rule-based design-space exploration as an optimization problem over design candidates constrained by structural and numerical restrictions.
3. **Burdusel, Zschaler & Strüber — *MDEOptimiser: A Search Based Model Engineering Tool* (2018/2019), DOI 10.1145/3270112.3270130.** The tool represents candidate solutions with models and uses model transformations as search operators; related work explicitly distinguishes transformation-chain encodings used by MOMoT and VIATRA-DSE.
4. **Strüber et al. — *Henshin: A Model Transformation Language and its Use for Search-Based Model Optimisation in MDEOptimiser* (2018).** Henshin is presented as a graph-transformation language used to specify evolutionary operators for search-based model optimization.
5. **Search-based model-engineering infrastructure literature** explicitly distinguishes the MOMoT approach as encoding solution candidates as chains of model transformations applied to an input model, with mutation/crossover generating new chains and reapplying them to the initial model.

### CH-0001 preliminary interpretation

The chain substantially strengthens the conclusion that **explicit transformation/search spaces and trajectories through transformation operators are established prior art in model-driven engineering**. MOMoT is therefore not an isolated terminology match.

At the same time, the surfaced chain remains **domain-specific and optimization-oriented**. The sources found so far focus on finding good transformation results/design candidates, not on a transversal theory of how a system's conditions modify the set of transformations that are subsequently accessible.

Therefore:

- `AC2` for `SRC-TRANS-001` remains supported.
- `AC3` is still **not established**.
- No Core modification is triggered.
- The citation chain itself becomes a source-discovery cluster requiring independent dossiers before any architectural absorption conclusion.

### CH-0002 — forward-chain status

Forward citation chaining for `SRC-TRANS-001` remains pending systematic bibliographic execution. The web-discovery pass surfaced later work on reinforcement-learning-based model transformation that explicitly compares MOMoT, MDEOptimiser and VIATRA-style transformation-rule sequence approaches, but this is contextual evidence rather than a completed forward-citation census.

## 6. Candidate cluster created by CH-0001

| Candidate ID | Source ID | Source | Provisional role | AC level |
|---|---|---|---|---|
| CAND-0009 | SRC-MOMOT-001 | Bill et al. (2019), *A local and global tour on MOMoT* | direct predecessor / structural antecedent | **AC2 confirmed; AC3 not established** |
| CAND-0010 | SRC-DSE-001 | Abdeen et al. (2014), *Multi-Objective Optimization in Rule-Based Design Space Exploration* | foundational DSE antecedent | **AC2 candidate/strong structural antecedent; AC3 not established** |
| CAND-0011 | SRC-MDEO-001 | Burdusel et al. (2018/2019), *MDEOptimiser* | adjacent competing architecture / representation comparison | **AC2 confirmed; AC3 not established** |
| CAND-0012 | SRC-HENSHIN-001 | Strüber et al. (2018), *Henshin...MDEOptimiser* | formal transformation-language antecedent | pending |

### CH-0001 dossier outcome — consolidated structural cluster

Independent screening of `SRC-DSE-001`, `SRC-MOMOT-001` and `SRC-MDEO-001` confirms a coherent prior-art cluster covering:

- explicit transformation/search spaces;
- transformation-rule applicability/executability or consistency;
- reachable candidate states;
- transformation sequences as trajectories;
- objective/fitness evaluation of resulting states;
- model transformations used explicitly as search operators.

This cluster **absorbs any broad originality claim over those individual structural elements**. It does not, on the current evidence, absorb the stronger TGCV architectural proposition concerning the explicit analytical object `ΔT_acc` — change in the accessibility relation itself — and its transversal connection to future reachability, trajectories, outcomes and value.

This remains a bounded interpretation, not a final SLR-1 originality conclusion.

## 7. Immediate controlled operation after chaining

The next operation is to screen:

1. `SRC-HENSHIN-001` — Strüber et al. (2018), *Henshin: A Model Transformation Language and its Use for Search-Based Model Optimisation in MDEOptimiser*, if the formal transformation-language layer can materially affect the AC3 boundary;
2. otherwise continue with the predefined SLR-1 search families and independent candidate screening.

No AC3 decision should be made solely from the current cluster.

## 8. Integrity boundary

The citation-chain results do not prove TGCV originality or non-originality. They establish a **prior-art cluster** that materially raises the standard required for any originality claim concerning transformation-space representation, transformation-chain exploration, reachability/path search or optimization over transformation sequences.

The unresolved question remains the higher-level architecture: whether prior literature already contains the transversal relation in which changes in system conditions modify an accessible transformation space and thereby alter future reachability/trajectories and downstream outcomes/value.

## 9. Remaining search completeness requirements

The final SLR-1 search remains incomplete until predefined query families have been searched across accessible primary bibliographic databases, all AC2+ candidates have backward and forward chaining where available, candidate clusters have been independently screened, evidence and facts have been normalized separately from architectural interpretation, and coverage limitations are recorded.

`NO_FULL_ABSORPTION_IDENTIFIED` remains a bounded possible outcome, never proof of universal novelty.
