# TGCV — Teoría de Construcción de Valor de Sistemas Generativos

TGCV is a research programme investigating **interactions that modify the set of transformations accessible to a system**, and how those modifications relate to subsequent trajectories and value construction.

## Repository purpose

This repository is the canonical continuity and reproducibility layer for TGCV. It separates the research state into governance, conceptual core, literature/evidence, experiments, research assets, applications, code, and data manifests.

## Current state

- Research stage: post-EXT-1.1 continuity/bootstrap.
- Central research object: interactions that modify the set of transformations accessible to a system.
- Scientific hypothesis: a transversal phenomenon is studied through partial theories across several fields, but lacks a minimal unified representation independent of application domain.
- Scientific aim: establish and test a minimal analytical layer connecting interactions, changes in accessible transformations, subsequent trajectories, and value creation.
- Practical aim: derive a methodology of value construction from the ontological core and evaluate it in industrial contexts.

## Structure

```text
TGCV/
├── 00_GOVERNANCE/
│   ├── decisions/
│   ├── freezes/
│   └── provenance/
├── 01_CORE/
│   ├── architecture/
│   ├── ontology/
│   ├── glossary/
│   └── hypotheses/
├── 02_LITERATURE/
│   ├── SLR/
│   ├── evidence-map/
│   └── references/
├── 03_EXPERIMENTS/
│   ├── EXT-1.0_CollegeMsg/
│   ├── EXT-1.1_Rust/
│   ├── protocols/
│   ├── results/
│   └── validation/
├── 04_RMA/
├── 05_ASSETS/
│   ├── Vision_Paper/
│   ├── Research_Prospectus/
│   ├── ARM/
│   └── Research_Notes/
├── 06_APPLICATIONS/
│   ├── UAM/
│   ├── IE/
│   └── Orange/
├── 07_CODE/
│   ├── src/
│   ├── tests/
│   └── scripts/
├── 08_DATA_MANIFESTS/
│   ├── datasets/
│   ├── hashes/
│   └── provenance/
├── README.md
├── STATUS.md
├── CHANGELOG.md
└── CITATION.cff
```

## Freeze policy

A freeze is an immutable research-state snapshot. It records what was fixed, when, why, the exact inputs/configuration, provenance, and validation status. Frozen material is never silently overwritten; later changes receive a new revision.

**EXT-1.1 continuity constraint:** before downloading or processing the Rust dataset, an identifiability/privacy audit must pass. Only after that gate is satisfied should EXT-1.1 be frozen and the exact dataset identified/processed.

## Reproducibility principle

Large datasets are not committed to Git. The repository stores protocols, manifests, hashes, provenance, code, configurations, logs, and derived results sufficient to reproduce the computational pipeline.
