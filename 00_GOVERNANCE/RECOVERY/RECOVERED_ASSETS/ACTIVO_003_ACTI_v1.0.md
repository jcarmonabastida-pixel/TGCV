# TGCV — ACTIVO 003: ARQUITECTURA CIENTÍFICO-TECNOLÓGICA INTEGRAL (ACTI v1.0)

**Recovery date:** 2026-08-27  
**Source:** user-supplied recovery record  
**Status:** RECOVERED — CANONICAL CANDIDATE  
**Version recovered:** v1.0

> **Provenance note:** This file preserves the recovered ACTI specification supplied by the programme owner. It is treated as the recovered architectural definition, not as a verbatim historical file unless the original source is subsequently recovered.

## 1. Role

ACTI is the **integral scientific-technological architecture of the Programme**. It locates the internal scientific engine, scientific production, TGCV theoretical artefacts, engineering/validation, impact/transfer and strategic communication in a single controlled architecture.

Its central architectural principle is that downstream communication and transfer are derived from the programme's knowledge base rather than becoming alternative sources of scientific truth.

## 2. Level 0 — Research Programme / scientific engine

Level 0 is the engine that generates everything else.

Permanent internal assets:

- Programa de Investigación TGCV;
- Mapa del Territorio Científico;
- Registro de Evidencias;
- Registro de Objeciones;
- Registro de Hipótesis;
- Registro de Riesgos;
- Registro de Decisiones Ontológicas (RDO);
- Modelo Ontológico Provisional (MOP);
- Protocolo de Integración de Evidencias (PIE).

These are **internal Programme assets and are not publication deliverables**.

## 3. Level 1 — Scientific production

**Mission:** produce validatable knowledge.

Assets:

- Research Prospectus;
- Systematic Literature Review (SLR);
- Vision Paper;
- Technical Concept Paper;
- derived scientific articles;
- Doctoral Thesis.

**Dependency rule:** Level 1 is fed exclusively from Level 0. Scientific production does not become an upstream authority over Level 0 merely because it is published.

## 4. Level 2 — TGCV theoretical construction

Level 2 contains TGCV's own scientific artefacts. They are **not merely articles**; they are scientific artefacts of the theory.

- TGCV Core Theory;
- TGCV Ontology;
- TGCV Formal Model;
- TGCV Reference Architecture;
- TGCV Methodology.

### Critical architectural correction recovered with ACTI

The **TGCV Reference Architecture & Methodology is part of the scientific-technological core**, not an external-transfer deliverable.

Transfer uses and operationalises the architecture/methodology; it does not replace or redefine it.

This correction must be respected in the Programme OS and asset taxonomy.

## 5. Level 3 — Engineering and validation

Level 3 answers one operational question:

> **¿Funciona?**

It includes:

- case studies;
- prototypes;
- industrial pilots;
- experimental validation;
- benchmarking;
- comparative evaluations.

This level creates empirical validation and practical test evidence for the relevant scientific/methodological claims. It does not automatically promote an applied result into theory without explicit analysis and governance.

## 6. Level 4 — Impact and transfer

This level converts research into impact and supports exploitation/application.

Assets/functions include:

- Innovation & Impact Roadmap;
- adoption strategy;
- technology roadmap;
- scientific roadmap;
- exploitation plan;
- industrial collaborations;
- industrial doctorate;
- European projects.

This layer is open-ended and should be understood as an impact/value-delivery portfolio, not a fixed list of external institutions.

## 7. Level 5 — Strategic communication

Level 5 contains dossiers and audience-specific communication products.

It is a **family**, not a single dossier:

- academic dossier;
- doctoral-supervisor dossier;
- university dossier;
- industrial dossier;
- investor dossier;
- European-call dossier;
- executive dossier;
- technical dossier.

All share the same underlying knowledge base. What changes is the audience, framing, emphasis and communication format — not the underlying scientific truth.

## 8. Integral architecture

```text
PROGRAMME TGCV
      │
      ▼
LEVEL 0 — SCIENTIFIC ENGINE
      │
      ├──────────────────┐
      ▼                  ▼
LEVEL 1              LEVEL 2
Scientific            TGCV CORE
production            theory + ontology +
                      architecture + methodology
      │                  │
      └────────┬─────────┘
               ▼
LEVEL 3 — ENGINEERING & VALIDATION
               │
               ▼
LEVEL 4 — IMPACT & TRANSFER
               │
               ▼
LEVEL 5 — STRATEGIC COMMUNICATION
      dossiers / audience-specific materials
```

The linear representation is a programme flow, not a claim that every asset always proceeds in a single irreversible sequence. Feedback loops may exist, but they must be governed and traced.

## 9. Architectural implications

### Technical Concept Paper

It no longer competes with the Vision Paper. It functions as a gateway into the TGCV theoretical core.

### TGCV Reference Architecture & Methodology

It is a central scientific-technological pillar and must not be classified as a mere transfer asset.

### Innovation & Impact Roadmap

It is not an appendix. It is the bridge from research toward exploitation, adoption, impact and value delivery.

### Dossiers

Dossiers are derived communication products. They are not independent intellectual sources and cannot redefine the underlying architecture.

## 10. Relationship to the constitutional layer

Project Zero defines Programme identity and purpose. The Programme Contract defines rules that protect integrity. ACTI specifies **where the principal scientific-technological assets live and how they relate**.

```text
PROJECT ZERO
      ↓
PROGRAMME CONTRACT
      ↓
ACTI — scientific-technological architecture
      ↓
PMO / SIP / RMA / execution controls
      ↓
research → theory → validation → impact/value → communication
```

ACTI therefore operationalises the constitutional principles but does not replace them.

## 11. Boundary with the scientific Core

ACTI is broader than the minimal scientific Core. It is an architecture of the Programme's scientific-technological assets, not itself the definition of the phenomenon under study.

The current scientific boundary remains separately governed, including the present formulation:

`Core = S`

`T_acc = F(S,C,L)`

`ΔT_acc → ΔReach → ΔTrajectory`

`Trajectory → Outcome → Value`

with `I` as explanatory mechanism rather than a Core primitive.

## 12. Governance and change control

Changes to ACTI must identify whether they affect:

- programme architecture;
- scientific production;
- TGCV theory;
- engineering/validation;
- impact/transfer;
- strategic communication.

A change in an ACTI level does not automatically imply a change in the scientific Core. Conversely, a scientific Core change may require an ACTI reconciliation.

## 13. Recovery questions

The following definitions should be reconciled when their source records are recovered:

- exact scope of the Programa de Investigación TGCV;
- historical MOP semantics;
- exact RDO and PIE procedures;
- relationship between ACTI and PMO/SIP;
- historical ACTII distinction, if ACTII is a separate asset rather than a prior/variant naming of this architecture.

Until then, ACTI v1.0 is retained as the recovered architectural specification.
