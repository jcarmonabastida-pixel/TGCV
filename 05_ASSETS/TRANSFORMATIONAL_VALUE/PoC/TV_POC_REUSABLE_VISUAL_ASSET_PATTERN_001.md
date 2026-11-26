# Learning Publishing PoC — reusable visual asset publishing pattern

**Record ID:** TV-POC-VISUAL-001  
**Version:** 0.1  
**Date:** 2026-11-27  
**Status:** DESIGN DRAFT — PENDING REVIEW; NOT IMPLEMENTATION AUTHORISATION  
**Branch:** `strategy/transformational-value-learning`  
**Scope:** Chapter 3 PoC; TV-DIA-001 is the sole validation asset  
**Governing specification:** `TRANSFORMATIONAL_VALUE_LEARNING_PUBLISHING_POC_v0.1.md` (TGCV-TV-POC-001, v0.4)  
**Related technical record:** `TV_POC_PREVIEW_TECHNICAL_APPROACH_001.md` (TV-POC-TECH-001)

> This document proposes a reusable design pattern. It does not authorise changes to the preview generator, canonical chapter content, TV-DIA-001 source files, other assets, or the publishing framework decision.

## 1. Purpose

Define a repeatable, content-first mechanism to declare, validate, render and place visual assets in the bilingual TRANSFORMATIONAL VALUE Learning book.

The pattern must separate asset-specific editorial and visual decisions from the shared publishing mechanism. TV-DIA-001 is the first and only asset used to validate the pattern in this PoC.

The design must remain proportionate to the existing PoC. It does not authorise migration of other chapters or creation of placeholder assets.

## 2. Historical reconstruction and relationship to existing work

The following canonical work already exists on this branch and must be reused:

| Existing record or asset | Established scope / state | Relationship to this proposal |
|---|---|---|
| TGCV-TV-POC-001 v0.4 | Governs the bounded bilingual Learning PoC, visual asset editability, provenance, responsive behaviour and accessibility | Governing requirements |
| TV-POC-TECH-001 | Candidate Astro + Starlight preview approach; proposes paired language rendering and derived desktop/mobile diagram variants | Existing technical approach; not replaced by this document |
| TV-POC-IMPL-001 | Records the isolated preview scaffold and explicitly states that runtime, visual and accessibility validation remain open | Implementation baseline and test record |
| TV-DIA-001 v0.3 | Existing bilingual Mermaid sources, README, captions, alternative text and visual checklist | Sole validation asset |

The current preview generator is known to contain Chapter 3 and TV-DIA-001-specific paths and values, append the diagram at the end of the chapter, and derive a mobile Mermaid source by changing the flow direction. These are baseline implementation characteristics, not requirements of the reusable pattern.

### 2.1 Design discrepancy requiring explicit review

TV-POC-TECH-001 proposes mechanically deriving a top-to-bottom mobile rendering from a left-to-right source. This proposal does not assume that such a transformation is valid for every diagram. The reusable pattern instead requires each asset to declare which visual presentations it supports and how each is sourced.

This is a proposed strengthening/generalisation of the asset model, not a silent amendment to TV-POC-TECH-001. The technical approach record must be reconciled explicitly before implementation changes are made.

## 3. Design principles

1. **Stable identity:** every visual asset has one stable asset ID, independent of language and rendering format.
2. **Editable source:** rendered outputs are derived artefacts; the maintained source remains available in a version-controlled, documented format.
3. **Single source of truth:** structured data used by the renderer must not be duplicated as independently editable values in multiple files.
4. **Separation of concerns:** asset definition, chapter placement, rendering and validation are separate responsibilities.
5. **Native bilingual content:** language-specific source labels, captions and alternative text are explicitly declared where needed.
6. **Explicit visual variants:** desktop, mobile or other presentations are declared per asset; no universal orientation conversion is assumed.
7. **Responsive legibility:** scaling, scrolling or an alternative visual variant is selected according to the asset's actual characteristics.
8. **Accessible explanation:** visual information is supported by meaningful alternative text, captions and surrounding chapter explanation.
9. **Framework portability:** asset identity, metadata and chapter declarations do not depend on Starlight-specific frontmatter or components.
10. **Bounded validation:** the pattern is tested only with TV-DIA-001 in this PoC.

## 4. Logical architecture

The pattern has five logical elements.

### 4.1 Editable asset source

Contains the maintained source file(s) for the visual asset. It may contain language variants and explicitly authored visual variants when the asset requires them.

The source format is asset-dependent. Mermaid is appropriate for TV-DIA-001 but must not be imposed as a universal format for all future visual assets.

### 4.2 Asset manifest

A machine-readable record declares the asset identity, editorial metadata, language-specific reader-facing text, source files and available visual variants.

The manifest is the proposed canonical structured source for values consumed by automated rendering and validation.

### 4.3 Human-readable asset documentation

The asset README explains purpose, conceptual interpretation, provenance, dependencies, known limitations and review checklist.

To prevent drift, fields such as captions, alternative text, source paths and variant declarations should not be independently maintained in both README and manifest. The implementation design must choose one of these approaches:

- the manifest is authoritative and the README references or is generated from it; or
- the README is authoritative and a deterministic process extracts the structured data.

**Proposed preference:** the manifest is authoritative for structured and reader-facing fields; the README explains the asset and its editorial/conceptual context. This is a design recommendation, not yet an implementation decision.

### 4.4 Chapter placement declaration

A chapter declares where an asset appears by referring to its stable asset ID. The rendering engine resolves the reference; it does not contain chapter-specific asset paths or IDs.

A chapter may reference more than one asset, and an asset may be reused by more than one chapter without duplicating its source.

### 4.5 Shared rendering and validation engine

The engine resolves chapter references and asset manifests, selects the appropriate language and presentation variant, generates or locates the required exports, integrates the asset and applies common presentation rules.

It must not encode TV-DIA-001-specific labels, paths, captions, alternative text or layout transformations.

## 5. Proposed manifest model

This is a logical schema for design review, not an approved YAML contract.

| Field | Purpose |
|---|---|
| `asset_id` | Stable identity, e.g. `TV-DIA-001` |
| `version` | Asset definition version |
| `status` | Editorial/validation status; not inferred from successful rendering |
| `title` | Asset title |
| `purpose` | Why the asset exists and what it explains |
| `source_format` | Format of the editable source |
| `owner` | Responsible owner |
| `languages` | Language-specific source, caption and alternative text |
| `visual_variants` | Explicitly supported visual presentations and their source references |
| `provenance` | Origin and dependencies |
| `licence` | Approved rights/licence information, only when established |

Conceptual shape:

```yaml
asset_id: TV-DIA-001
version: 0.3
status: draft
title: Accessible transformation space sequence
purpose: Explain the distinction between accessible transformations and realised transformations.
source_format: mermaid
owner: TRANSFORMATIONAL VALUE editorial project

languages:
  en:
    source: source/accessible-transformation-space-sequence.mmd
    caption: "<English caption>"
    alternative_text: "<English alternative text>"
  es:
    source: source/accessible-transformation-space-sequence.es.mmd
    caption: "<Spanish caption>"
    alternative_text: "<Spanish alternative text>"

visual_variants:
  - variant_id: desktop
    target: wide
    source: null
    strategy: responsive
  - variant_id: mobile
    target: narrow
    source: null
    strategy: responsive

provenance:
  dependencies: []

licence: null
```

The example intentionally leaves visual source references unresolved. The correct variant strategy for TV-DIA-001 must be established through review and testing; this document does not approve the current LR-to-TB transformation.

The final schema must define whether a visual variant references the same language source, a separately maintained source, or a deterministic derived source. It must also define how generated exports are named and located. These details must be settled before implementation.

## 6. Chapter placement

The current generator appends TV-DIA-001 to the end of Chapter 3. A reusable pattern needs explicit placement within the chapter so that diagrams can appear next to the explanation they support.

The placement declaration must:

- identify the asset by stable ID;
- occur at the intended location in the Markdown source;
- support more than one asset per chapter;
- be readable and maintainable by an author;
- remain independent of a particular publishing framework;
- fail validation if the referenced asset does not exist.

### 6.1 Candidate mechanism for evaluation

A framework-neutral Markdown marker is a candidate:

```markdown
<!-- visual-asset: TV-DIA-001 -->
```

The build process would recognise the marker and replace it with the rendered asset component. The marker is a proposal only. Before adoption, verify that it survives the selected Markdown processing pipeline in a predictable way, does not create inaccessible output, and can be validated without coupling canonical content to Starlight.

An alternative is a portable directive/shortcode syntax, provided its semantics are documented independently of the chosen renderer.

**Open decision:** select and test the least intrusive placement mechanism against the existing Chapter 3 Markdown. No canonical chapter edit is authorised by this draft.

## 7. Responsive presentation model

The renderer must support three presentation modes:

1. **Fluid scaling:** use when the full visual remains legible at the available width.
2. **Controlled horizontal scrolling:** use when reducing the visual would make labels, symbols or relationships difficult to read. Scrolling must be deliberate and discoverable.
3. **Explicit alternative variant:** use when a separately designed narrow-screen presentation materially improves comprehension.

The selected mode must be based on the asset's declared and validated characteristics. The renderer must not infer that every wide diagram can be converted by changing its orientation.

A single source may serve all viewports when it remains legible. Separate variants are justified only when they preserve the same intended meaning and have a demonstrable usability benefit.

No universal fixed width, automatic orientation change or universal layout rule is prescribed.

## 8. Accessibility and reader-facing content

For each language presented to readers:

- Provide meaningful alternative text that describes the conceptual content, not the current screen orientation.
- Provide a caption that identifies the diagram and its role in the chapter.
- Explain important relationships and qualifications in the surrounding text.
- Ensure distinctions such as solid and dashed connections do not rely on colour alone.
- Check contrast, text size, clipping and keyboard/screen-reader behaviour of the rendered presentation.
- Preserve meaningful reading order and do not expose redundant or confusing alternative descriptions when multiple responsive variants are used.

For complex diagrams, the design may require a longer description in the chapter or an adjacent accessible text representation. Alternative text alone should not be forced to carry an entire detailed explanation.

The PoC does not claim formal accessibility certification. Findings and limitations must be recorded.

## 9. Automated validation requirements

The shared validator should eventually check:

| ID | Validation | Expected result |
|---|---|---|
| VAP-01 | Asset ID uniqueness | Each ID resolves to exactly one manifest |
| VAP-02 | Manifest completeness | Required fields and valid values are present |
| VAP-03 | Source existence | Every declared editable source exists |
| VAP-04 | Language coverage | Required language variants have source, caption and alternative text |
| VAP-05 | Variant resolution | Every declared visual variant resolves to a valid source or supported generation rule |
| VAP-06 | Chapter reference resolution | Every chapter marker resolves to an asset |
| VAP-07 | Placement | Each asset appears at its declared position and only as often as declared |
| VAP-08 | No hardcoded asset logic | Renderer contains no TV-DIA-001-specific editorial values or paths |
| VAP-09 | Multiple references | More than one asset declaration can be processed without renderer changes |
| VAP-10 | Language pairing | The correct language-specific source and reader-facing text are selected |
| VAP-11 | Accessible output | Required caption and alternative text are present in rendered output |
| VAP-12 | Responsive output | Declared presentation mode is applied and does not cause unintended page overflow |
| VAP-13 | Variant semantic consistency | Variants preserve required conceptual nodes, relationships and symbols |
| VAP-14 | Reproducibility | A clean build produces the declared outputs from canonical sources |

Automated checks cannot establish visual clarity or conceptual equivalence on their own. Those checks require recorded human inspection.

## 10. TV-DIA-001 validation plan

TV-DIA-001 is the only validation case for this PoC. The validation must establish:

1. Both canonical language sources resolve through the asset declaration.
2. Caption and alternative text are selected from the appropriate language metadata.
3. The diagram is inserted at an explicit location in both Chapter 3 pages.
4. Desktop and narrow-screen presentation strategies are declared and reproducible.
5. Any alternative visual variant preserves node identity, edges, symbols and conceptual meaning.
6. Labels remain legible without clipping or excessive reduction.
7. A wide visual can be explored without compressing it into illegibility.
8. Solid and dashed connectors remain distinguishable without colour.
9. The chapter explanation and visual description agree.
10. The result can be rebuilt from a clean checkout using documented commands.

The current implementation is a baseline for comparison, not a mandatory implementation to preserve.

## 11. Implementation boundaries

This draft does not authorise:

- editing `scripts/prepare-content.mjs`;
- editing the canonical Chapter 3 Markdown files;
- editing TV-DIA-001 source files or README;
- introducing a manifest or placement marker into the working tree;
- creating assets or chapter structures beyond the existing PoC;
- migrating other chapters;
- selecting Starlight or another production framework;
- production deployment or public release.

Any implementation must follow the existing PoC authorisation in the Learning Master Architecture §22 and remain on `strategy/transformational-value-learning`.

## 12. Open design decisions

The following decisions must be reviewed before implementation:

| ID | Question | Proposed direction | Status |
|---|---|---|---|
| OD-01 | Which file is the structured source of truth for captions, alternative text and variant declarations? | Manifest authoritative; README provides conceptual documentation | Open |
| OD-02 | What chapter placement syntax is least intrusive and portable? | Evaluate a stable-ID Markdown marker against a portable directive | Open |
| OD-03 | How are language and visual variants represented without duplicating sources? | Explicit references in the manifest | Open |
| OD-04 | Should a narrow-screen variant be generated or separately authored for TV-DIA-001? | Decide from visual inspection; do not assume LR-to-TB conversion is valid | Open |
| OD-05 | How should complex diagrams expose a longer accessible description? | Chapter text or adjacent description, as appropriate | Open |
| OD-06 | Which validation checks are automated and which require human review? | Automate structural checks; record visual/conceptual review separately | Open |
| OD-07 | How will the existing TV-POC-TECH-001 proposal be reconciled with the selected pattern? | Update that record only after explicit design review | Open |

## 13. Acceptance condition for this design

This design may be approved for implementation planning when:

- its relationship with TV-POC-TECH-001 is explicitly reconciled;
- the manifest and README responsibilities are unambiguous;
- a portable chapter placement mechanism is selected;
- responsive variant behaviour is specified for TV-DIA-001;
- accessibility and validation responsibilities are testable;
- the scope remains limited to Chapter 3 and TV-DIA-001.

Approval of this design would not itself authorise implementation changes beyond the existing PoC scope. Any changes to canonical chapter or asset sources remain subject to the applicable approval and editorial controls.

## 14. Version history

- **v0.1 — 2026-11-27:** Initial design draft. Reconstructs and references existing PoC work; separates asset metadata, chapter placement, rendering and validation; identifies the existing mechanically derived mobile layout as a design discrepancy requiring review. No implementation authorised.
