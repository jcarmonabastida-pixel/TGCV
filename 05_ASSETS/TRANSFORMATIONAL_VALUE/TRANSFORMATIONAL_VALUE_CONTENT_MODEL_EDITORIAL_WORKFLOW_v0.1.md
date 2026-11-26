# TRANSFORMATIONAL VALUE — Content Model & Editorial Workflow

**Identifier:** TGCV-TV-CONTENT-MODEL-001  
**Version:** 0.5  
**Date:** 2026-11-26  
**Status:** CONTENT ARCHITECTURE PROPOSAL — FOR REVIEW  
**Governing document:** `TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md`  
**Related specification:** `TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md`  
**Branch:** `strategy/transformational-value-learning`

> This specification defines a proposed repository content model and editorial workflow for the *TRANSFORMATIONAL VALUE* reference work and the future Learning section. It is an authoring and publication architecture, not a selection of website framework, a publication authorisation, a licensing decision, or a change to TGCV scientific or VALUE methodological governance.

---

## 1. Purpose

Define how the book and future Learning resources are identified, organised, authored, reviewed, connected, versioned and prepared for publication.

The content model must support:
- one coherent reference work with independently addressable pages;
- original Spanish and English authoring for every content unit;
- stable identity across language versions and revisions;
- explicit editorial and review status for each language;
- references, glossary terms, diagrams, examples and cross-links;
- evidence and epistemic-status traceability where relevant;
- future contribution through a governed Git workflow;
- publication through a documentation-oriented web experience without coupling content to one framework.

## 2. Governing principles

1. **GitHub is the canonical source.** Published pages are generated from reviewed source content; the website is not the only place where the content exists.
2. **Content is independent of presentation.** Markdown files should remain readable outside the website and must not contain framework-specific components unless a later, explicit publishing specification approves a portable convention.
3. **One content identity, two original language versions.** Spanish and English versions share a stable content ID but are authored and reviewed natively and independently.
4. **No translation-first workflow.** Machine translation may assist drafting or quality checks but cannot replace native authorship and editorial review.
5. **Equivalent scope, not literal wording.** Language versions must preserve concepts, depth, examples, references, qualifications and learning objectives while using natural expression.
6. **No false bilingual completeness.** The status of each language is tracked separately. A content unit is bilingual-complete only when both language versions meet publication criteria.
7. **Canonical definitions and sources.** Shared concepts, references and diagrams should be reused rather than copied into conflicting versions.
8. **Separate content status from epistemic status.** A page can be editorially approved while explaining an open hypothesis; publication status does not validate its claims.
9. **Preserve authority boundaries.** TGCV scientific claims follow TGCV governance. VALUE method changes follow VALUE governance. Editorial workflow cannot approve either by itself.
10. **Portable and evolvable.** Stable IDs, metadata and simple formats should survive a future publishing-framework change.

## 3. Repository layout proposal

The following is the proposed content-root layout. It should be treated as a content architecture, not yet as an implementation of Learning routes.

```text
05_ASSETS/
└── TRANSFORMATIONAL_VALUE/
    ├── TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md
    ├── TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md
    ├── TRANSFORMATIONAL_VALUE_CONTENT_MODEL_EDITORIAL_WORKFLOW_v0.1.md
    │
    ├── book/
    │   ├── es/
    │   │   ├── front-matter/
    │   │   ├── part-01-understanding-transformation/
    │   │   ├── part-02-designing-value/
    │   │   ├── part-03-evolving-value/
    │   │   └── back-matter/
    │   └── en/
    │       ├── front-matter/
    │       ├── part-01-understanding-transformation/
    │       ├── part-02-designing-value/
    │       ├── part-03-evolving-value/
    │       └── back-matter/
    │
    ├── learning-resources/
    │   ├── es/
    │   └── en/
    │
    ├── glossary/
    │   ├── es/
    │   └── en/
    │
    ├── references/
    │   └── references.yml
    │
    ├── assets/
    │   ├── diagrams/
    │   ├── images/
    │   ├── tables/
    │   └── downloads/
    │
    ├── metadata/
    │   ├── content-registry.yml
    │   ├── terminology.yml
    │   ├── navigation.yml
    │   └── editorial-policy.yml
    │
    └── governance/
        ├── CONTRIBUTING.md
        ├── REVIEW_POLICY.md
        └── CHANGELOG.md
```

### 3.1 Layout rules

- The `book/es/` and `book/en/` trees mirror each other conceptually, not necessarily through identical translated filenames.
- The same content ID links counterpart pages even if their language-specific slugs differ.
- Shared assets live once in `assets/` unless language-specific rendering or text embedded in an image makes separate versions necessary.
- Learning resources are distinct from the core book. They may include tutorials, exercises, demonstrations and curated learning paths.
- Glossary entries have paired language files and a shared term ID.
- References are maintained centrally where feasible, with stable reference IDs.
- Metadata files describe content and navigation; they must not become alternative copies of chapter prose.
- Do not create empty placeholder files for every future chapter. Register planned content in the content registry and create page files when substantive drafting begins.
- The exact folder and file naming convention can be revised after a small publishing proof of concept, without changing stable content IDs.

## 4. Stable identity and naming

### 4.1 Content IDs

Every independently addressable content unit receives a stable, language-neutral ID. IDs should not encode mutable titles or language.

Suggested patterns:

| Content type | ID pattern | Example |
|---|---|---|
| Front matter | `TV-FM-NNN` | `TV-FM-001` |
| Part overview | `TV-PN-OV` | `TV-P1-OV` |
| Chapter | `TV-CH-NN` | `TV-CH-01` |
| Section page | `TV-CH-NN-SNN` | `TV-CH-03-S02` |
| Glossary term | `TV-TERM-NNN` | `TV-TERM-014` |
| Learning resource | `TV-LR-NNN` | `TV-LR-003` |
| Case study | `TV-CASE-NNN` | `TV-CASE-001` |
| Diagram | `TV-DIA-NNN` | `TV-DIA-006` |

IDs are permanent. If a chapter is renamed, its ID remains. If content is split or merged, record redirects or supersession relationships in the registry rather than silently reusing an old ID.

### 4.2 Filenames and slugs

- Use lowercase kebab-case filenames.
- Avoid accents and punctuation in filenames for portability; visible titles retain correct language orthography.
- Language folders provide the language context, but metadata must also declare language explicitly.
- Do not use translated title text as the only identifier.
- Keep URLs stable once published; title changes should not automatically change published routes.

Example counterpart paths:

- `book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`
- `book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`

Both declare `content_id: TV-CH-01`.

## 5. Content types and required structure

The first content model supports:
- book front matter;
- part overview;
- chapter;
- section page;
- glossary entry;
- learning resource;
- case study;
- reference record;
- diagram or other reusable asset record.

A chapter may be a single page or a parent grouping several section pages. The content registry defines its position and relationships.

### 5.1 Common Markdown page structure

A normal chapter or learning page should use:
1. YAML front matter;
2. a single H1 matching the page title;
3. a short opening that establishes purpose and context;
4. learning objectives where appropriate;
5. the explanatory content;
6. examples and diagrams where they add learning value;
7. limitations or common misunderstandings where relevant;
8. summary or key takeaways;
9. reflection/application questions where appropriate;
10. related content and references.

This is a reusable guide, not a compulsory template for every content type.

## 6. Metadata model

### 6.1 Required common metadata

Each published Markdown page must declare:

| Field | Required | Meaning |
|---|---|---|
| `content_id` | Yes | Stable language-neutral content identity |
| `title` | Yes | Natural title in the page language |
| `language` | Yes | `es` or `en` |
| `content_type` | Yes | Controlled content type |
| `status` | Yes | Editorial lifecycle status for this language |
| `version` | Yes | Content revision, independent of book edition |
| `created` | Yes | Initial creation date |
| `updated` | Yes | Last substantive update |
| `authors` | Yes | Native author(s) of this language version |
| `reviewers` | At review stage | Relevant reviewers |
| `summary` | Yes | Short description in the page language |
| `part` | Book pages | Part identifier |
| `chapter` | Chapter/section pages | Chapter identifier |
| `parent_id` | Where applicable | Parent content ID |
| `translation_of` | No | Must not be used to imply translation-first authorship; use `language_pair_id` instead |
| `language_pair_id` | Yes for bilingual content | Shared content ID connecting native language versions |
| `tags` | Recommended | Controlled or reviewed topics |
| `concepts` | Recommended | Glossary term IDs |
| `prerequisites` | Where relevant | IDs of prior learning content |
| `related` | Where relevant | Related content IDs |
| `references` | Where relevant | Central reference IDs |
| `epistemic_status` | Where claims require it | Claim/content status classification |
| `source_assets` | Where relevant | Authoritative source artefact paths or IDs |
| `license` | When approved | Explicit approved licence identifier; never infer one |

### 6.2 Example chapter metadata

```yaml
---
content_id: TV-CH-01
language_pair_id: TV-CH-01
title: "Pensar en sistemas"
language: es
content_type: chapter
status: draft
version: 0.1
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "Fundamentos para razonar sobre sistemas, sus límites y su contexto."
part: TV-P1
chapter: TV-CH-01
parent_id: TV-P1-OV
tags:
  - systems-thinking
  - systems-engineering
concepts: []
prerequisites: []
related: []
references: []
epistemic_status:
  - established_external_knowledge
source_assets: []
license: null
---
```

English counterpart uses the same content and pair IDs, `language: en`, an original English title and summary, its own editorial status, authors, reviewers and revision.

### 6.3 Metadata validation

Before publication, automated checks should validate:
- required fields and allowed values;
- unique content IDs in the registry;
- counterpart language records for content marked bilingual;
- valid references to existing content IDs;
- valid glossary and reference IDs;
- allowed status transitions;
- absence of duplicate routes;
- no broken local asset paths.

Automation should report missing or inconsistent metadata; it must not automatically approve content.

## 7. Language pairing and bilingual completeness

### 7.1 Pairing rules

- Spanish and English pages share `content_id` and `language_pair_id`.
- Each page is an original authored text in its declared language.
- Pairing does not require identical paragraph counts, sentence order or literal phrasing.
- Both versions must have equivalent conceptual coverage, learning objectives, examples, references, qualifications and depth.
- If one version changes substantively, the counterpart must be flagged for equivalence review.
- A content unit is bilingual-complete only when both versions are approved and publishable.
- If staged publication is chosen, the site must clearly indicate which language is available; it must not silently route readers to an incomplete counterpart.

### 7.2 Language status

Track editorial status separately for each language:

- `planned`
- `draft`
- `editorial_review`
- `subject_review`
- `cross_language_review`
- `approved`
- `published`
- `needs_revision`
- `retired`

Not every page requires every review stage. The applicable route depends on content type and claim category. The status field records the current state; review history and decisions should be traceable in GitHub discussions/PRs or the approved editorial record.

### 7.3 Cross-language review checklist

- Are all concepts present in both versions?
- Are the claims and evidence qualifications equivalent?
- Are examples and numerical values consistent?
- Are references and links equivalent or appropriately localised?
- Is terminology consistent with the shared terminology register?
- Are proper names and approved labels preserved exactly?
- Does each version read naturally to a proficient reader of that language?
- Are diagrams, captions, alt text and navigation labels available in both languages where required?

## 8. Shared terminology and glossary

The terminology register is the control point for preferred terms and their language equivalents.

Each term record should contain:
- stable term ID;
- canonical concept name;
- Spanish preferred term;
- English preferred term;
- definition in Spanish;
- definition in English;
- accepted synonyms;
- terms to avoid or distinctions to preserve;
- first-use explanation guidance;
- related term IDs;
- source and review status.

The glossary pages themselves are paired Spanish and English content units. Definitions should be authored natively and then checked for conceptual equivalence.

The register must explicitly preserve distinctions such as:
- transformation versus change, action or outcome;
- candidate transformation versus accessible transformation;
- accessibility versus execution or adoption;
- transformation versus value;
- Value Construction versus VCF, VSM and Value Architecture;
- CCV as a capability concept versus IVS as an exploratory measurement proposal;
- VALUE as a framework versus ValueLabOS as a proposed supporting ecosystem.

Do not create a new canonical term merely to avoid explaining an existing one.

## 9. References and source traceability

### 9.1 Central reference records

Use stable reference IDs, for example `REF-0001`. Each record should include, where applicable:
- authors or responsible organisation;
- title;
- publication or release date;
- publisher / venue;
- DOI or stable URL;
- source type;
- access date for web resources;
- relevant pages or sections;
- language;
- notes on relevance and limitations.

### 9.2 Claim traceability

For substantive claims, especially TGCV scientific statements and empirical results:
- identify the authoritative source asset or publication;
- link to the precise evidence or section where possible;
- state the scope and limitations;
- distinguish an external source from a TGCV result or VALUE proposal;
- avoid treating an editorial reference list as proof of a claim.

A future claim register may be warranted if the book contains many scientific claims. Do not duplicate the TGCV Evidence→Claim Matrix; reference it and follow its governance.

### 9.3 Reference rendering

The publishing system may format references differently by language, but reference identity and bibliographic facts should be maintained once in the central registry where possible.

## 10. Diagrams, images and reusable assets

- Every substantive diagram should have a stable asset ID, source/editable file where available, version, title, description, owner and source provenance.
- Text embedded in an image must be language-neutral or supplied as paired language variants.
- Captions, explanatory notes and alternative text must be authored in Spanish and English.
- A diagram that communicates different claims in each language is not a valid language variant.
- Prefer editable source formats and accessible text/diagram descriptions.
- Do not use a screenshot as the only source of a model that should be maintained.
- Reuse shared diagrams by ID; do not copy diverging versions into chapter folders.
- Licence and third-party rights must be checked before publication.

## 11. Editorial workflow

### 11.1 Workflow overview

`Planned → Draft → Editorial review → Subject review (when required) → Cross-language review → Approved → Published`

A page may return to `needs_revision` at any review stage. Publication is a separate release action; approval alone does not publish it automatically.

### 11.2 Drafting

1. Confirm the page ID, purpose, audience, prerequisites and source dependencies.
2. Confirm that the chapter-level structure has been approved sufficiently to support drafting.
3. Draft the Spanish and English versions as original texts. They may be developed in parallel or in either order, but neither is treated as the source translation of the other.
4. Add metadata, references, glossary links and asset references.
5. Label examples and claims accurately.
6. Record unresolved questions rather than filling gaps by assumption.

### 11.3 Editorial review

Review for:
- clarity, structure and didactic progression;
- consistency with the book's editorial voice;
- correct introduction of terms;
- useful examples and learning objectives;
- readability and accessibility;
- duplication or contradiction with other pages;
- appropriate links and references.

### 11.4 Subject-matter review

Route review according to content:
- TGCV scientific claims: current TGCV scientific governance and relevant evidence owners.
- VALUE methodology: current VALUE methodology governance and source specification.
- Systems engineering or external technical material: suitable domain review.
- Legal, licensing, privacy or safety claims: competent specialist review where required.

Editorial approval cannot substitute for these reviews.

### 11.5 Cross-language review

Check both versions for equivalent scope and meaning, then separately check that each reads naturally. A bilingual reviewer may coordinate this stage, but native-language quality must be represented.

### 11.6 Approval and publication

- Record the approval rationale and required reviewers.
- Confirm that all required assets, links, references and metadata are present.
- Confirm language publication policy for the release.
- Publish through a controlled website release process.
- Record the published edition and date.
- Retain the source history and prior published content.

## 12. GitHub contribution workflow

GitHub is the proposed review and contribution mechanism, subject to future governance approval.

### 12.1 Change categories

- editorial;
- terminology;
- technical/domain;
- methodological;
- scientific;
- asset/diagram;
- reference or citation;
- publishing metadata/navigation.

### 12.2 Pull request requirements

A substantive PR should state:
- affected content IDs and language versions;
- purpose and reason for change;
- change category;
- source references or evidence;
- impact on related chapters, glossary, diagrams and references;
- whether the counterpart language version is included or needs follow-up;
- review path required.

### 12.3 Review routing

- Editorial-only changes: editorial review.
- Technical/domain claims: relevant subject reviewer.
- VALUE method changes: VALUE method authority/reviewers.
- TGCV scientific claims: TGCV scientific governance; no approval by ordinary editorial merge.
- Cross-cutting changes: all relevant review paths.

A contribution must not be merged merely because automated checks pass. Automated checks validate structure, not truth or methodological authority.

## 13. Versioning model

Keep four version dimensions distinct:

1. **Document revision:** the version of an individual page, tracked in metadata and Git history.
2. **Book edition:** a curated release of the complete reference work, for example `0.1`, `1.0`.
3. **Method/science source version:** the exact version of VALUE or TGCV material on which a page depends.
4. **Website release:** the build or deployment version of Learning.

These are not interchangeable. Updating a website does not automatically create a new book edition; a new book edition does not imply a new TGCV scientific status.

For each book edition, maintain a release manifest listing:
- included content IDs and language versions;
- page revisions;
- source versions relied upon;
- known omissions and limitations;
- publication date;
- change summary.

## 14. Licensing and rights — decision deferred

No licence is assigned by this document.

The project should decide separately, after reviewing ownership and third-party constraints:
- book prose and editorial content;
- research material and evidence-derived figures;
- original diagrams and visual assets;
- code, demos and interactive examples;
- user/community contributions;
- third-party quotations, images and data.

Do not assume that one Creative Commons licence applies to all content or that an open-source software licence is suitable for prose. Do not promise contributor rights or reuse permissions until the relevant licence and contribution terms are approved.

## 15. Publication-system requirements (framework-neutral)

A future publishing implementation should support:
- rendering Markdown and front matter;
- hierarchical left navigation;
- part/chapter/section ordering;
- paired Spanish/English routes;
- language switch between true counterparts;
- stable canonical URLs and redirects;
- contextual table of contents;
- search;
- glossary and reference links;
- previous/next navigation;
- responsive and accessible behaviour;
- visible content version and update information;
- build-time metadata and link validation;
- draft exclusion from public builds;
- versioned release manifests.

This is a requirements list, not a decision to use Starlight or another specific framework.

## 16. Initial decision register

| ID | Decision | Initial position | Status |
|---|---|---|---|
| CM01 | Canonical content source | GitHub version-controlled Markdown | Proposed |
| CM02 | Content identity | Stable language-neutral IDs | Proposed |
| CM03 | Languages | Native Spanish and English for every content unit | Governing requirement from master architecture |
| CM04 | Pairing | Shared content ID; independent language files and status | Proposed |
| CM05 | Metadata | YAML front matter plus central registries | Proposed |
| CM06 | Glossary | Shared term IDs with paired native definitions | Proposed |
| CM07 | References | Central reference registry with stable IDs | Proposed |
| CM08 | Assets | Shared asset library with paired captions/alt text | Proposed |
| CM09 | Editorial workflow | Draft, editorial, subject, cross-language, approval, publication | Proposed |
| CM10 | Contributions | GitHub PRs with category-based review routing | Future proposal |
| CM11 | Versioning | Separate page, book edition, source and website versions | Proposed |
| CM12 | Licensing | Separate decision by content class; no licence presumed | Open |
| CM13 | Publishing framework | Defer pending requirements and proof of concept | Open |

## 17. Open questions before implementation

1. Should section-level pages be used from the first edition, or should some chapters remain single Markdown files until content length justifies splitting?
2. Should the central content registry be manually maintained or generated from page metadata?
3. Which metadata fields should be mandatory for every page versus only specific content types?
4. What bilingual publication policy should apply if one language version is delayed?
5. Which terminology register source should be authoritative, and how should it relate to existing TGCV/VALUE glossaries?
6. Should references use a simple YAML registry initially or a bibliographic format such as BibTeX/CSL JSON?
7. Which checks can run in GitHub Actions without creating excessive maintenance?
8. What release policy defines a public book edition?
9. What licence and contributor agreement are appropriate for each content class?
10. Which publication framework best fits the existing TGCV website and the requirements in the master architecture?

## 18. Recommended proof of concept

Before creating the full repository tree or drafting all chapters, validate the model with a small representative set:

- one chapter page in Spanish and its independently authored English counterpart;
- one glossary term in both languages;
- one shared diagram with bilingual captions and alternative text;
- two or three central references;
- one cross-link between chapter and glossary;
- metadata validation for pairing and status;
- a draft build that demonstrates sidebar ordering and language switching, without public release.

The proof of concept should test whether the content model is usable by authors and reviewers, not attempt to validate the book's substantive claims.

## 19. Version history

- **v0.1 — 2026-11-26:** Initial proposal for repository organisation, stable content IDs, bilingual native authoring, metadata, glossary and references, assets, editorial workflow, GitHub contribution routing, versioning, licensing boundaries and a representative proof of concept.


## 20. Repository directory layout

The canonical root is `05_ASSETS/TRANSFORMATIONAL_VALUE/`. Keep only these three governing documents directly in that root:

- `TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md`
- `TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md`
- `TRANSFORMATIONAL_VALUE_CONTENT_MODEL_EDITORIAL_WORKFLOW_v0.1.md`

All proof-of-concept specifications, source-readiness records, test results and evaluation decisions belong under `PoC/`.

The book and shared learning content follow this structure:

```text
TRANSFORMATIONAL_VALUE/
  [three governing documents]
  PoC/
  book/
    es/
      part-01-understanding-transformation/
    en/
      part-01-understanding-transformation/
  learning-resources/
    research-notes/
      es/
      en/
  glossary/
  references/
  assets/
    diagrams/
    images/
  metadata/
  governance/
```

Spanish and English book content must be stored in their respective language trees. Shared assets, references, metadata and terminology records must not be duplicated by language unless the resource genuinely requires language-specific variants. Bilingual research notes and evidence summaries belong under `learning-resources/research-notes/es/` and `learning-resources/research-notes/en/`, sharing a language-neutral content ID and receiving independent editorial status. Their reader-facing text must use descriptive study titles and must not expose internal experiment or repository identifiers. Internal provenance paths may be retained in metadata. The `PoC/` directory is a project-validation workspace, not a fourth governing-document layer. Directories may initially contain short `README.md` orientation files; do not create empty chapter files or placeholders for all planned content. New chapter and section files are created only when their drafting gate is reached.

## 21. Version history

- **v0.2 — 2026-11-26:** Formalised the repository directory layout, reserved the root for three governing documents, and assigned PoC artefacts to `PoC/`.


## 22. Public-facing terminology and internal research identifiers

This is a book-wide editorial rule for every reader-facing component of *TRANSFORMATIONAL VALUE*, not a rule limited to the pilot chapter or to scientific research summaries. Readers are not expected to understand TGCV's internal research organisation, experiment labels, workstreams, repository structure or artefact naming conventions.

### 22.1 Scope: all reader-facing surfaces

The rule applies independently to the Spanish and English versions and to every surface that a reader may encounter, including:

- book and part titles, chapter and section titles, headings and subheadings;
- body text, examples, case studies, exercises, questions, summaries and callouts;
- tables, charts, diagrams, labels, legends, captions, figure notes and alternative text;
- glossary entries, sidebars, navigation labels, page summaries and search descriptions;
- public bibliographies, footnotes, endnotes, acknowledgements and appendices;
- downloadable reader-facing resources and content embedded in demonstrations.

A code is not acceptable merely because it appears outside the main prose. If it is visible to the reader, it is in scope.

### 22.2 What counts as an internal identifier

Internal identifiers include, without limitation, names or codes for:

- experiments, studies, workstreams, projects and research packages;
- gates, milestones, runs, jobs, cohorts, test fixtures and benchmark cells;
- datasets, evidence records, claim records and internal evaluation outputs;
- repository documents, branches, commits, workflows, scripts and implementation artefacts;
- internal teams, review processes, issue numbers and operational tracking records.

Examples include short alphanumeric codes, project-specific acronyms, run numbers, commit hashes, branch names and filenames. The list is illustrative, not exhaustive: the test is whether the label is an internal lookup key rather than a meaningful reader-facing concept.

### 22.3 Reader-facing treatment

- Replace internal identifiers with a precise, meaningful name or a concise description of the underlying study, method, result, evidence or limitation.
- Explain what was examined, under what conditions, and what the evidence does and does not support. Do not substitute a code with a vague promotional label.
- Do not invent a polished public name for an internal artefact unless that name has been deliberately approved through the relevant governance.
- Do not imply that an internal study label is a recognised scientific term, a public product name or an established method.
- Preserve scientific precision and qualifications when rewriting. Removing a code must not remove provenance, scope or limitations.

For example, instead of writing “TR-131/V007 demonstrates…”, describe the relevant study in ordinary language, state the examined setting and result, and cite an accessible public source where one exists. If no public source exists, do not make an internal artefact appear to be a published reference.

### 22.4 Permitted internal use and exceptional public disclosure

Internal identifiers may remain in non-reader-facing material where needed for operational traceability, including:

- source maps, editorial working files and private review records;
- repository paths, filenames, metadata and internal registries;
- private evidence and claim traceability records;
- source references that allow editors to locate the authoritative artefact.

Their presence in internal metadata or a source path does not authorise their reproduction in the public-facing citation or narrative.

A public technical appendix, reproducibility package or formal citation may retain an identifier only when it is genuinely necessary for independent verification and no stable descriptive reference is sufficient. Such an exception must:
1. be approved by the relevant scientific or methodological authority, as applicable;
2. explain the identifier in plain language at first use;
3. state why disclosure is necessary;
4. avoid exposing unrelated internal codes or operational details; and
5. be recorded in the editorial review record for each affected language version.

An exception is not created merely because an identifier is present in a source document.

### 22.5 Acronyms, abbreviations and technical notation

Acronyms and abbreviations may appear in reader-facing content only when at least one of the following applies:

1. the abbreviation is widely established in the relevant discipline and materially helps the reader;
2. it is an approved public name or term used consistently by the book; or
3. it is a necessary recurring concept, introduced at first use with its full form and a clear definition.

Avoid creating acronyms for phrases used only once or a few times. Do not expose internal shorthand merely because it appears in source artefacts. Do not assume that an acronym familiar to the author is familiar to the intended reader.

Recognised technical symbols and notation belonging to the conceptual framework (for example, (T_{acc}), once defined) are not repository identifiers. They may be used where they improve precision, provided that they are explained and applied consistently. A project-specific code does not become a technical term simply by being formatted as a symbol or acronym.

Spanish and English versions must make their own first-use explanations natural to each language. An acronym retained in one language is not automatically appropriate in the other.

### 22.6 Mandatory bilingual editorial gate

Before a language version can move to `approved`, reviewers must complete and record the following check for that version. Spanish and English must be checked independently; passing one does not imply that the other passes.

- [ ] Inspect every reader-facing surface listed in §22.1, not only the chapter body.
- [ ] Identify acronyms, abbreviations, alphanumeric codes, named experiments, internal labels and opaque references.
- [ ] For each item, determine whether it is an established disciplinary term, an approved public name, necessary technical notation or an internal identifier.
- [ ] Remove or replace internal identifiers with precise reader-facing descriptions unless a documented exception under §22.4 applies.
- [ ] Check that retained acronyms are defined at first use and genuinely useful to the reader.
- [ ] Check diagrams, tables, captions, legends, alternative text, glossary, navigation, references and downloadable material as well as prose.
- [ ] Check that public terminology is consistent with the terminology register and that Spanish and English express equivalent concepts naturally.
- [ ] Record any permitted exception, its rationale, approving authority and affected locations.
- [ ] Re-run the check after substantive edits that may introduce or expose new labels.

Automated searches and linting should support this review by flagging likely codes, unexplained capitalised terms and patterns from internal registries. They are aids, not substitutes for semantic human review; a clean automated scan alone is not evidence of compliance.

### 22.7 Approval rule

An unexplained internal identifier, opaque project-specific acronym or unjustified internal label on any reader-facing surface is an editorial defect. The affected language version must not be approved until it is removed or an explicit exception is documented and approved. The bilingual content unit is complete only when both language versions independently pass this gate.

This editorial gate controls reader-facing clarity and traceability. It does not certify the truth, validity or epistemic status of the underlying scientific or methodological claims.

## 23. Version history

- **v0.3 — 2026-11-26:** Added a binding editorial rule separating reader-facing terminology from internal TGCV research and repository identifiers, including acronym policy and review checks.
- **v0.4 — 2026-11-26:** Expanded the rule to every reader-facing surface, defined internal identifiers and permitted exceptions, distinguished technical notation from repository codes, and introduced a mandatory independently recorded bilingual approval gate supported by automated checks and human review.
- **v0.5 — 2026-11-26:** Added a bilingual `learning-resources/research-notes/` structure for reader-facing evidence notes, with independent language status, descriptive public titles and internal provenance retained only in metadata.
