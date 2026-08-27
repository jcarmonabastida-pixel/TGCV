# TGCV — Teoría de Construcción de Valor de Sistemas Generativos

## Research programme

TGCV investigates a transversal phenomenon: **interactions that modify the set of transformations accessible to a system**, and how those modifications relate to subsequent trajectories and value construction.

The programme is organized around a cautious, falsifiable research hypothesis: a widely distributed phenomenon is studied across multiple fields through partial theories, but lacks a minimal unified representation that is independent of application domain.

### Current research state

- Conceptual architecture: stabilized working architecture following EXT-1.1.
- Central object: interactions that modify the set of transformations accessible to a system.
- Scientific aim: establish and test a minimal transversal analytical layer connecting interactions, changes in accessible transformations, subsequent trajectories, and value creation.
- Practical aim: derive a methodology for value construction from the ontological core and evaluate its applicability in industrial contexts.
- Research programme: literature synthesis → ontological/conceptual stabilization → falsifiable experimental programme → empirical validation → value-construction methodology.

## Repository structure

```text
TGCV/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── STATUS.md
├── CITATION.cff
├── docs/
│   ├── architecture/
│   ├── research-prospectus/
│   ├── vision-paper/
│   ├── research-notes/
│   ├── transfer/
│   └── freezes/
├── ontology/
│   ├── core/
│   ├── glossary/
│   └── mappings/
├── experiments/
│   ├── EXT-1.1/
│   ├── protocols/
│   ├── data-dictionary/
│   └── results/
├── evidence/
│   ├── literature/
│   ├── traceability/
│   └── claims/
├── industrial/
│   ├── ARM/
│   └── Orange/
├── reproducibility/
│   ├── code/
│   ├── configs/
│   └── manifests/
└── archive/
```

## Versioning and freezes

Research-state freezes are immutable snapshots used to preserve continuity between research stages. They are stored under `docs/freezes/` and referenced from `STATUS.md` and the relevant experimental records.

The EXT-1.1 freeze material is the authoritative continuity layer for the present repository bootstrap. New work must not silently overwrite a frozen state; subsequent changes are recorded as explicit revisions.

## Principle of continuity

The repository is intended to make TGCV computationally and conceptually reproducible across conversations and research stages. The canonical state is represented by versioned documents, explicit freezes, traceability records, and reproducibility assets rather than by conversational context alone.
