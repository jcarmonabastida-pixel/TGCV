# TGCV — Canonical Scientific Asset Registry v0.1

**Status:** CURRENT / OPERATIVE
**Date:** 2026-09-09
**Purpose:** canonical discovery and reuse index for research-bearing scientific assets that may materially affect future TGCV gates, audits, experiments, operationalisations or domain-selection decisions.

## 1. Registry rule

`02_EXTERNAL_SCIENCE/` is the canonical registry/integration surface. It does not require physical relocation of historical artifacts.

`02_LITERATURE/` remains the historical SLR working/archive surface. Registered artifacts may remain there physically; their historical paths are authoritative provenance references.

Registration does **not** upgrade epistemic status, evidence level, closure state or scientific claim strength.

## 2. Mandatory reuse gate

Before any new scientific gate, audit, experiment, domain selection, dataset search, operationalisation, cross-domain translation or technical feasibility study, the investigator must consult:

1. `00_GOVERNANCE/` current and relevant historical control surfaces;
2. this registry;
3. `02_LITERATURE/` when the registry or scientific question points to historical SLR material.

The existence of a relevant historical artifact blocks a claim that the new operation starts "from scratch" unless the operation explicitly records why the artifact is scientifically irrelevant.

## 3. Registered reusable scientific assets

| ID | Historical artifact | Type | Scientific role | Status | Reuse relevance | Canonical handling |
|---|---|---|---|---|---|---|
| ESA-TGCV-001 | `02_LITERATURE/TGCV_ARCHITECTURE_DEVELOPMENT_OPERATIONALIZATION_GATE_v0.1.md` | Architecture/gate | Core S, T_acc, ΔT_acc, operational objects, falsifiers and gate criteria | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-002 | `02_LITERATURE/TGCV_CONTRIBUTION_FORMALIZATION_GATE_v0.1.md` | Contribution gate | Formalises candidate contribution and claim boundary | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-003 | `02_LITERATURE/TGCV_CROSS_DOMAIN_ARCHITECTURE_CLOSURE_CONTRIBUTION_NON_REDUNDANCY_GATE_v0.1.md` | Comparative gate | Prior-art absorption and bounded residual contribution | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-004 | `02_LITERATURE/TGCV_CROSS_DOMAIN_RECONSTRUCTION_NON_REDUNDANCY_GATE_v0.1.md` | Comparative gate | Cross-domain reconstruction/non-redundancy | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-005 | `02_LITERATURE/TGCV_DELTA_TACC_INFORMATION_SUFFICIENCY_STATE_REDUCTION_GATE_v0.1.md` | Information-sufficiency gate | ΔT_acc information sufficiency and state reduction | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-006 | `02_LITERATURE/TGCV_DOMAIN_INSTANTIATION_SELECTION_GATE_v0.1.md` | Domain-selection gate | Criteria for selecting an empirical domain instantiation | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-007 | `02_LITERATURE/TGCV_DYNAMIC_DELTA_TACC_TEST_v0.1.md` | Dynamic test | Dynamic empirical representation of ΔT_acc | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-008 | `02_LITERATURE/TGCV_OPERATIONAL_REPRESENTATION_SPECIFICATION_GATE_v0.1.md` | Operational specification | Operational representation requirements | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-009 | `02_LITERATURE/TGCV_REACHABILITY_LINK_TRAJECTORY_SUFFICIENCY_GATE_v0.1.md` | Sufficiency gate | ΔT_acc → Reach → Trajectory link and sufficiency boundary | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-010 | `02_LITERATURE/TGCV_RUST_ACCESSIBILITY_SEMANTICS_FREEZE_GATE_v0.1.md` | Domain semantic freeze | Rust accessibility semantics | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-011 | `02_LITERATURE/TGCV_RUST_DOMAIN_INSTANTIATION_SPECIFICATION_GATE_v0.1.md` | Domain operationalisation | Rust domain instantiation | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-012 | `02_LITERATURE/TGCV_RUST_INSTANTIATION_STRUCTURAL_AUDIT_v0.1.md` | Structural audit | Rust structural admissibility/integrity | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-013 | `02_LITERATURE/TGCV_RUST_TEMPORAL_PAIRING_FREEZE_GATE_v0.1.md` | Temporal freeze | Ex-ante temporal pairing rule for Rust | HISTORICAL / WORKING | High | Register; preserve historical location |
| ESA-TGCV-014 | `02_LITERATURE/TGCV_VALUE_LINK_OUTCOME_SUFFICIENCY_GATE_v0.1.md` | Value-link gate | Boundary for ΔT_acc → Reach → Trajectory → Outcome → Value | HISTORICAL / WORKING | High | Register; preserve historical location |

## 4. Relationship to later Rust execution records

Rust execution records under `03_EXPERIMENTS/EXT-1.1_Rust/` remain the canonical experiment-specific execution surface. This registry records the earlier scientific artifacts because they can affect interpretation, reconstruction, reuse and claims about independent development.

The registry therefore prevents a future Rust or other-domain operation from treating these artifacts as nonexistent while avoiding duplication of the experiment record.

## 5. SLR source material

The `SLR-1_SOURCE_DOSSIER_*`, search logs, evidence-bank schemas and fact-bank schemas remain primarily SLR archive material in `02_LITERATURE/`. They are not individually promoted here unless a future operation establishes that a particular source artifact has reusable scientific-control significance beyond the SLR archive.

## 6. Physical migration policy

No physical migration is performed by this registry creation. Any future relocation from `02_LITERATURE/` to another canonical physical surface is a separate controlled operation with provenance, equivalence and integrity checks.

## 7. Governance consequence

This registry establishes a reusable scientific-memory layer between the SLR archive and future gates. Its purpose is anti-redundancy and provenance control, not expansion of the scientific evidence base.
