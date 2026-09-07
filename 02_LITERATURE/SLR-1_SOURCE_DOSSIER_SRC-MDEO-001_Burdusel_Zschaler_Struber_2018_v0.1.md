# SLR-1 Source Dossier — SRC-MDEO-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Burdusel, A., Zschaler, S., & Strüber, D. (2018), *MDEOptimiser: A Search Based Model Engineering Tool*, MODELS 2018 Companion, pp. 12–16.
**DOI:** 10.1145/3270112.3270130
**Classification:** **AC2 — STRUCTURAL EQUIVALENCE CONFIRMED; AC3 NOT ESTABLISHED**

## Bibliographic identity

The publication record identifies the three authors, MODELS 2018 Companion Proceedings, pages 12–16 and DOI 10.1145/3270112.3270130. citeturn0search0turn0search4

## Source scope

MDEOptimiser (MDEO) is presented as a tool for specifying and solving optimisation problems using Model-Driven Engineering. It provides a DSL for optimisation problems and executes evolutionary optimisation algorithms using models as population-member encodings and model transformations as search operators. citeturn0search2turn0search4

## Evidence extraction

### E1 — model as state/solution representation

MDEO uses models as the representation of candidate solutions/population members. The model is therefore the evolving object on which search operators act. citeturn0search2turn0search4

### E2 — transformations as operators

Model transformations are explicitly used as search operators. The search process therefore defines a set of operations capable of modifying a model and generating alternative candidate states. citeturn0search2turn0search4

### E3 — explicit transformation-chain representation in the rule-based comparison

The accessible full-text indexing for the publication reports that rule-based optimisation tools encode solution candidates as sequences of model transformations and apply mutation/crossover to those transformation chains. This places MDEO directly in the same structural family as Abdeen/DSE and MOMoT. citeturn0search2

### E4 — search-space / candidate-generation structure

MDEO abstracts optimisation into a search process over model candidates. Its DSL lets users specify the optimisation problem while the framework supplies evolutionary search machinery. The resulting architecture is explicitly search-based rather than a theory of system evolution. citeturn0search4turn0search9

### E5 — feasibility / consistency of transformations

The broader MDEOptimiser research line develops consistency-preserving mutation/search operators. Later work describes the key contribution as automatically generating atomic consistency-preserving mutation operators for search-based model engineering. This supports an operational notion of admissible model changes, but it remains an engineering/search concern rather than a transversal theory of accessibility-space change. citeturn0search10turn0search32

### E6 — objective/value analogue

MDEO is explicitly an optimisation framework: candidate models are evaluated according to the optimisation problem specified by the user. The source therefore contains outcome evaluation and fitness, but not TGCV's broader value-construction relation. citeturn0search2turn0search4

### E7 — separation from MOMoT is representational, not architectural

The MDEOptimiser research programme later describes a key contribution as directly encoding solution candidates as models to which transformation rules are applied, avoiding genotype–phenotype translations. This distinguishes the encoding/search architecture from MOMoT, but does not introduce the TGCV-level abstraction of changing accessibility conditions. citeturn0search32

## TGCV mapping

| TGCV element | MDEOptimiser analogue | Assessment |
|---|---|---|
| `S` | current candidate model / model state | strong analogue |
| `T_acc` | available/valid model transformations used as search operators | structural analogue |
| accessibility predicate | applicability/consistency of transformation operators | partial/operational analogue |
| `Reach` | candidate models reachable through search operators | implicit/explicit in search process |
| `Trajectory` | sequences of transformations / mutation history | explicit in rule-based family |
| `Outcome` | resulting candidate model | explicit |
| `Value` | optimisation fitness/objective values | partial analogue |
| `ΔT_acc` | change in the accessible operator set itself | **not explicit** |
| mechanism modifying future accessibility | operator/model interaction affects future applicability, but no separate transversal mechanism construct | **not established** |

## AC2 assessment

**AC2 — STRUCTURAL EQUIVALENCE CONFIRMED.**

MDEOptimiser independently reproduces the same structural layer identified in Abdeen and MOMoT:

`model/state → transformation operators → candidate states → search trajectory → objective evaluation`.

It is therefore strong evidence that this structural construction is established prior art within search-based model engineering. The official project publication list also places MDEOptimiser alongside the Henshin transformation-language work and later scalable search-based model-engineering work, confirming a sustained research line rather than an isolated contribution. citeturn0search3

## AC3 assessment

**AC3 — ARCHITECTURAL ABSORPTION NOT ESTABLISHED.**

The evidence does not show that MDEOptimiser treats the *change in the accessibility relation itself* as the research object.

Its problem is instead: how to represent candidate models, apply transformation/search operators, and optimise the resulting candidates. The set of search operators is an input/engineering component of the optimisation architecture, while changes in the model are effects of search operations.

This is materially different from the TGCV proposition:

`changed conditions of S → changed T_acc → changed Reach/Trajectory → downstream Outcome → Value`.

MDEOptimiser therefore strengthens the prior-art case against broad structural novelty, but it does not absorb the higher-level TGCV architecture on the evidence reviewed here.

## Cross-source cluster conclusion

The independent dossiers for:

- `SRC-DSE-001` — Abdeen et al. 2014;
- `SRC-MOMOT-001` — Bill et al. 2019;
- `SRC-MDEO-001` — Burdusel et al. 2018;

now form a coherent prior-art cluster covering explicit model/design search spaces, transformation operators, applicability/consistency, reachable candidates, transformation sequences and optimisation objectives.

This cluster means TGCV must **not** present any of those elements individually as the core of its originality claim.

The unresolved architectural distinction remains narrower and more demanding: whether there is a transversal theory whose object is **the change in the set/relation of accessible transformations itself**, independently of a particular transformation language, search algorithm, optimisation framework or domain.

## Decision boundary

- `AC2`: confirmed.
- `AC3`: not established.
- TGCV Core: unchanged.
- No inference from EXT-1.1 is used.
- No post-hoc alteration of experimental records.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. Evidence, factual normalization and architectural interpretation remain separated.