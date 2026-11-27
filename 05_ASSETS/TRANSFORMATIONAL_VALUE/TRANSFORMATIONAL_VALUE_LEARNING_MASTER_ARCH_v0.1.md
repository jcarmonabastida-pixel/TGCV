# TRANSFORMATIONAL VALUE — Book & Learning Master Architecture

**Identifier:** TGCV-TV-LEARNING-MASTER-001  
**Version:** 0.7  
**Date:** 2026-11-26  
**Status:** STRATEGIC ARCHITECTURE — WORKING DOCUMENT; detailed contents proposal available for review  
**Branch:** `strategy/transformational-value-learning`  
**Canonical location:** `05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md`

> This document establishes the strategic, editorial, knowledge, learning-experience and future community architecture for the reference work *Transformational Value* and its public Learning environment. It authorises planning and content development, plus the narrowly bounded local PoC preview specified in §22. It does not authorise scientific changes, declare VALUE validated, establish a recognised standard, or authorise production website implementation or publication.

---

## 0. Executive summary

The initiative is to develop the reference work **TRANSFORMATIONAL VALUE — Understanding, Designing and Realizing Value in Changing Systems** and make its content available through a public **Learning** section on the TGCV website.

Learning should provide a structured, didactic and navigable knowledge experience inspired by the strengths of:
- **The Rust Programming Language** online book: a coherent book, progressive chapters and clear sequential navigation.
- **Starlight** documentation: hierarchical sidebar navigation, modular pages, contextual contents, search and cross-linking.

The intended experience combines both patterns: a reference book that can be read progressively and a knowledge base whose individual pages can also be consulted independently.

The initiative should be designed from the beginning to permit future community contributions and governed evolution if genuine adoption emerges. Community participation is a future capability, not an assumption about current adoption.

The work has five connected but distinct layers:

1. **TGCV** — research programme and source of relevant research concepts, models, hypotheses and evidence.
2. **TRANSFORMATIONAL VALUE** — reference work connecting understanding of transformation with the practice of value construction.
3. **Learning** — public learning and knowledge-navigation experience through which the work and related learning resources are accessed.
4. **VALUE** — applied framework explained and taught through the reference work, retaining its methodological identity and independence.
5. **ValueLabOS** — proposed digital and collaborative ecosystem that may support application, experimentation, documentation and evolution of VALUE; it is not a prerequisite for learning or using VALUE.

The architecture must preserve these distinctions. It must not imply that VALUE is a literal or fully validated derivation of TGCV, that ValueLabOS is already a finished product, or that any of these elements has achieved external standard status.

## 1. Purpose and scope

### 1.1 Purpose

Establish one governing architecture for:
- the editorial conception and development of the reference book;
- its information and content architecture;
- the Learning user experience;
- the source-of-truth and publication model for content;
- the relationship between the book, TGCV, VALUE and ValueLabOS;
- future learning resources beyond the book;
- a possible community contribution and review process;
- versioning, traceability, quality and evidence boundaries.

### 1.2 In scope

- Book purpose, audience, positioning, structure and editorial principles.
- Chapter and page granularity.
- Content types, metadata, glossary, references and cross-linking.
- Learning navigation and discovery requirements.
- Content repository and publishing principles.
- Editorial, methodological and scientific review distinctions.
- Future contribution workflow and governance principles.
- Phased development and decision backlog.

### 1.3 Out of scope for this version

- Writing the complete book.
- Freezing the final table of contents.
- Selecting or implementing the final web framework.
- Building Learning routes or UI.
- Launching community accounts, forums or contribution tooling.
- Declaring VALUE an established or validated standard.
- Changing TGCV scientific governance, Core, RMA, Evidence→Claim Matrix, experimental contracts or evidence status.
- Treating C10 or any other open research question as resolved.

## 2. Identity architecture and governing relationships

The identity architecture recorded in `TGCV_VALUE_VALUELABOS_IDENTITY_ARCH_v0.1.md` is the starting point.

| Element | Role | What it is not |
|---|---|---|
| **TGCV** | Applied research and innovation programme investigating transformations available to systems and their dynamics, conditions and possible consequences | A scientifically consolidated theory or a guarantee that expanded possibilities create value |
| **TRANSFORMATIONAL VALUE** | Reference work connecting transformation foundations, value design and evaluation, and practice | A software manual or proof that all proposed relationships are validated |
| **Learning** | Public didactic and knowledge-navigation environment | The source of scientific authority or a separate methodology |
| **VALUE** | Applied framework for understanding contexts and opportunities, connecting knowledge and evidence, designing alternatives, deciding, acting and learning about value | ValueLabOS, a software product, or a proven literal implementation of TGCV |
| **ValueLabOS** | Proposed digital and collaborative ecosystem supporting VALUE application, experimentation, documentation and evolution | VALUE itself or a prerequisite for understanding and using VALUE |

### 2.1 Relationship narrative

> TGCV studies how the transformations available to systems change. *Transformational Value* connects that understanding with the practice of discovering, designing and evaluating opportunities for value. Learning makes this knowledge accessible and teachable. VALUE structures applied intervention. ValueLabOS is the proposed ecosystem for supporting application, experimentation and collaborative evolution.

This is an explanatory architecture, not a proven causal chain or a mandatory operational sequence.

### 2.2 Independence and claim boundaries

- TGCV retains autonomy as a research programme; product or editorial needs must not determine scientific conclusions.
- VALUE must remain understandable and usable without ValueLabOS.
- ValueLabOS may facilitate practices but does not automatically redefine VALUE.
- The TGCV-to-VALUE articulation is a theoretical-applied relationship to be justified and evaluated, not presumed equivalence.
- Increasing accessible transformations does not automatically create realised value.
- Possibility, accessibility, decision, authorisation, execution, adoption, outcome and value must remain distinct.
- The causal question concerning accessibility, trajectories and value remains open wherever the current scientific governance says it is open.
- Claims of efficacy, causality, scientific validity, generalisability or standard status require appropriate evidence and external evaluation.

## 3. The reference work

### 3.1 Working title and identity

**TRANSFORMATIONAL VALUE**

*Understanding, Designing and Realizing Value in Changing Systems*

Identity line: **TGCV · VALUE · ValueLabOS**

The title and subtitle are the working editorial identity already recorded in the identity architecture. They express the intended scope of the work, not a claim that a consolidated academic field or recognised international standard already exists.

### 3.2 Editorial purpose

The book should help readers:
1. understand systems and the transformations available to them;
2. understand how conditions, constraints, capabilities and relationships influence those transformations;
3. reason carefully about what changes in a system's possibilities and trajectories;
4. understand the distinction between transformation and value;
5. learn the VALUE framework and its application logic;
6. design and evaluate interventions without confusing hypotheses with evidence;
7. understand how governance, experimentation, learning and collaboration may support the evolution of practice.

It should be a reference work and a learning resource, not a promotional brochure for TGCV, VALUE or ValueLabOS.

### 3.3 Intended audiences

The detailed audience model remains to be validated. The initial editorial design should accommodate:
- systems engineers and systems practitioners;
- researchers and postgraduate-level readers interested in systems, transformation and value;
- professionals responsible for designing or changing complex systems;
- practitioners seeking a structured approach to value construction;
- future contributors, educators and members of a community of practice.

The work should be accessible to motivated readers outside these groups through clear explanations, progressive learning and a glossary, without diluting technical precision.

### 3.4 Editorial voice

- Clear, rigorous, didactic and measured.
- Systems-engineering orientation rather than generic business-consulting language.
- Explain concepts before relying on them.
- Introduce terminology progressively and consistently.
- Distinguish established knowledge, TGCV proposals, VALUE methodology, working hypotheses, illustrative examples and empirical findings.
- Prefer concrete examples where they clarify a concept, while labelling synthetic or fictional cases accurately.
- Avoid claims of novelty, validation, superiority or adoption that exceed available evidence.
- Preserve official names and recognised terminology; do not translate or rename approved proper names without explicit authorisation.

## 4. Provisional book structure

The three-part structure below is the starting architecture from the identity document. It is a provisional content map, not a frozen table of contents. Chapter-level decomposition and sequencing require a dedicated content-design pass.

### Front matter
- Foreword / purpose and scope.
- How to use this book.
- Reader pathways and prerequisites.
- Terminology and conventions.
- A note on evidence, examples and epistemic status.

### Part I — Understanding Transformation

Purpose: establish the conceptual and systems foundations needed to understand transformations, accessible possibilities, conditions and trajectories.

Indicative content domains:
- Systems, boundaries, context and system states.
- Capabilities, actions and transformations.
- Candidate transformations and accessible transformations.
- Conditions, resources, constraints, permissions and relationships.
- Transformation spaces and their changing structure.
- Opening, closing, loss, reconfiguration and substitution of possibilities.
- Realised transformations, successor states and trajectories.
- What can and cannot be inferred about outcomes and value.
- TGCV research questions, models, evidence and limitations.

### Part II — Designing Value

Purpose: teach VALUE as an applied framework for understanding contexts, discovering opportunities, designing alternatives, deciding, acting and learning.

Indicative content domains:
- What value means in context: actors, outcomes, horizons and constraints.
- Understanding the system and its environment.
- Needs, capabilities, knowledge, relationships, flows and friction.
- Opportunity discovery and problem framing.
- Hypotheses, evidence and uncertainty.
- Connecting knowledge and evidence.
- Designing alternatives and evaluating trade-offs.
- Decision, authority, authorisation and execution.
- Outcomes, evaluation and learning.
- The VALUE lifecycle and its iterative character.
- Worked examples, including the fictional clinic appointment-management case where source artefacts and publication suitability are verified.

The current working VALUE lifecycle is ALIGN as entry/alignment and governance, followed by SENSE, CONNECT, DESIGN, DECIDE, ACT and LEARN. The book must explain its iterative nature and must not imply that completing the lifecycle guarantees value.

### Part III — Evolving Value

Purpose: explain evaluation, governance, experimentation, organisational learning and the possible evolution of VALUE and its supporting ecosystem.

Indicative content domains:
- Evaluating outcomes and value.
- Attribution, causality, uncertainty and limits.
- Learning from interventions and experiments.
- Governance and methodological integrity.
- Documenting cases and reusable knowledge.
- Evolving methods through evidence and practice.
- ValueLabOS: role, boundaries and proposed capabilities.
- Collaboration and community contribution.
- Versioning, review and quality assurance.
- Evidence, adoption and conditions for possible standardisation.

### Back matter and reference resources
- Glossary.
- References and further reading.
- Concept index / subject index.
- Method and artefact references.
- Acknowledgements and contributor information.
- Version history and change notes.

### 4.1 Rules for developing the detailed contents

The detailed table of contents should:
- distinguish parts, chapters, sections and individual Learning pages;
- give each chapter a clear learning purpose;
- avoid duplication between TGCV foundations and VALUE practice;
- identify prerequisites and concepts that must be introduced earlier;
- map cross-references between related concepts;
- identify where evidence, examples, diagrams, exercises or case studies are needed;
- distinguish core book content from optional supplementary resources;
- remain evolvable as the conceptual and methodological work matures.

## 5. Learning experience architecture

### 5.1 Product concept

Learning is the public learning environment on the TGCV website. It initially publishes the reference work, but its architecture should permit additional learning resources later.

It should combine:
- the coherence and progressive reading experience of an online technical book;
- the modularity and navigability of a documentation site;
- a knowledge graph-like experience through cross-links, glossary entries and related content, without requiring a graph visualisation in the first release.

### 5.2 Primary desktop layout

The target desktop experience should include:

1. **Persistent left navigation panel**
   - hierarchical book and resource index;
   - expandable parts and chapters;
   - clear active-page indication;
   - optional collapse/expand behaviour;
   - responsive behaviour on smaller screens.

2. **Main content area**
   - title, part/chapter context and concise introduction;
   - readable typography and clear heading hierarchy;
   - diagrams, tables, examples, callouts and references where useful;
   - previous/next navigation;
   - contextual links to related concepts and resources.

3. **Optional contextual table of contents**
   - headings within the current page;
   - current-section indication;
   - anchor links.

4. **Global Learning utilities**
   - search;
   - breadcrumbs or equivalent location context;
   - glossary access;
   - language selector when bilingual content is available;
   - version and update information.

The exact arrangement is a design decision for the later UX phase. The left-hand hierarchical navigation is a core requirement of the concept.

### 5.3 Responsive and accessibility requirements

- On mobile, the left navigation should become an accessible drawer or equivalent compact navigation pattern.
- All navigation must be keyboard operable.
- Heading structure, focus order, contrast and link semantics must be accessible.
- Diagrams must have meaningful text alternatives or accompanying explanations.
- Do not rely on colour alone to communicate status or distinctions.
- Search and navigation must remain usable without pointer interaction.
- Page layouts must work at common desktop, tablet and mobile widths.

### 5.4 Learning page types

The architecture should support at least:
- book landing page;
- part overview;
- chapter/page;
- glossary entry;
- reference/resource page;
- tutorial or practical guide;
- case study;
- learning path;
- research connection / evidence note.

Not all page types need to be populated at launch.

### 5.5 Learning functionality priorities

**First release / essential**
- Hierarchical sidebar navigation.
- Stable URLs for chapters and sections.
- Previous/next navigation.
- Responsive layout.
- Search across published Learning content, if feasible within the chosen platform.
- Cross-links and references.
- Clear content version/date.
- Paired Spanish and English content authored natively in each language, with independent review and publication status.

**Later enhancements**
- Reading progress or bookmarks.
- Learning paths and curated sequences.
- Exercises and interactive demonstrations.
- User accounts and personal learning history.
- Comments or discussion.
- Community proposals and contribution interfaces.
- Rich concept maps or graph navigation.

Do not let later enhancements delay a coherent first release.

## 6. Knowledge and content architecture

### 6.1 Source of truth

The canonical content should live as version-controlled source files in GitHub, not exclusively inside the website CMS or rendered website.

The website should render or build from those source files. This provides:
- revision history;
- reviewable changes;
- traceability;
- stable identifiers and links;
- portability between publishing technologies;
- a future contribution workflow;
- a durable archive of previous versions.

### 6.2 Recommended content format

Markdown is the preferred initial authoring format because it is readable, versionable and supported by common documentation and static-site systems.

Use structured front matter or equivalent metadata for fields such as:
- stable content ID;
- title;
- content type;
- part / chapter / section;
- language;
- status;
- version;
- last updated;
- author / editor;
- reviewers where appropriate;
- tags and concepts;
- prerequisites;
- related pages;
- references;
- epistemic or evidence classification where relevant.

The final metadata schema must be specified before large-scale authoring or implementation.

### 6.3 Content granularity

A chapter may consist of several independently addressable pages. The preferred unit is a coherent learning page that:
- answers a clear question or teaches a bounded concept;
- has an identifiable learning purpose;
- can be linked directly;
- avoids becoming so small that the navigation fragments the book;
- avoids becoming so large that it is difficult to scan, review or maintain.

### 6.4 Shared knowledge components

The architecture should support reusable and centrally maintained:
- glossary terms;
- definitions and concept notes;
- diagrams and visual models;
- reference records;
- case-study records;
- examples and exercises;
- evidence notes and research links;
- recurring methodological patterns.

A concept should have one preferred canonical definition, with other pages linking to it rather than silently creating conflicting definitions.

### 6.5 Bilingual authoring strategy

Spanish and English are two original editorial languages of the book and Learning content. Each section must be conceived and written natively in both languages, not drafted in one language and subsequently translated as the standard production workflow.

This is a governing editorial requirement, not merely a future localisation option.

- Every published content unit must have a Spanish version and an English version with equivalent scope, depth, structure, examples, references and learning objectives.
- Authors should write each language version directly and naturally for its intended readership. The two versions should express the same concepts and claims, but need not follow identical sentence structures or literal wording.
- Translation tools may assist review, terminology checks or drafting, but machine translation or post-hoc translation must not substitute for native editorial authorship and review.
- Both language versions must share a stable content ID and have explicit language metadata, while retaining language-specific filenames, URLs and publication status.
- The content model must support language parity tracking: draft, editorial review, subject review, approved and published, independently for each language.
- A section should not be represented as fully bilingual when only one language version is complete. Where publication is staged, the availability and status of each language must be clear.
- Spanish and English versions must be reviewed for conceptual equivalence, technical accuracy, tone, terminology and evidence qualifications.
- A shared terminology register should record preferred terms, definitions, approved equivalents, terms intentionally retained in English and names that must not be translated.
- Official names, product names, framework labels, lifecycle phase names and other explicitly approved proper names must remain exactly as approved. Explanatory prose and descriptive headings should be written naturally in the language of the page.
- Changes to a concept or claim must trigger review of both language versions; a substantive change must not silently leave the other language outdated.

The final repository layout and metadata schema will be defined in the content-model specification. The architecture should support paired language files without duplicating the conceptual identity of a content unit.

### 6.5 Bilingual strategy

The website is intended to support Spanish and English. Learning should be designed for bilingual publication from the beginning, even if both language versions are not ready simultaneously.

- Each language version should have a stable relationship to its counterpart.
- Translation must preserve meaning, technical precision and epistemic qualifications.
- Official proper names and approved navigation/product names must remain exactly as approved; descriptive text may be translated.
- A translated page must not be presented as complete if important sections are missing.
- The language status of each page should be visible or otherwise unambiguous.

## 7. Evidence, epistemic status and content quality

The book and Learning must preserve the evidence and claim boundaries of TGCV and the methodological independence of VALUE.

### 7.1 Content classifications

Each relevant content item should be distinguishable as one or more of:
- established external knowledge;
- TGCV research concept or working model;
- TGCV hypothesis or open research question;
- empirical result with an explicit scope and limitation;
- VALUE methodological proposal or practice;
- illustrative example;
- synthetic or fictional case;
- proposed ValueLabOS capability;
- future direction or open question.

The final controlled vocabulary and visual treatment remain to be designed.

### 7.2 Scientific review boundary

Content making claims about TGCV must be checked against the current scientific source of truth and relevant evidence artefacts. This Learning architecture does not supersede scientific governance.

A page may explain an open hypothesis, but it must label it as open. A synthetic demonstration may illustrate a concept, but it cannot be described as real-world validation.

### 7.3 VALUE review boundary

Methodological descriptions must be checked against the current VALUE methodology assets. Editorial improvements must not silently change the method. Proposed changes should be recorded and reviewed as methodological changes.

### 7.4 Examples and cases

- Label fictional and synthetic cases explicitly.
- Identify assumptions and simulated values.
- Separate a method demonstration from evidence of effectiveness.
- Do not imply deployment, adoption or causal impact without supporting records.
- Verify publication suitability and consistency of source artefacts before including them.

## 8. Editorial governance and future community evolution

### 8.1 Initial governance

Before community adoption exists, the project should operate with a lightweight editorial model:
- an accountable editorial owner;
- named subject-matter reviewers as available;
- explicit review status;
- documented acceptance decisions for substantive changes;
- version history and change notes.

The governance model should be proportionate to the actual contributor base and must not simulate institutional consensus.

### 8.2 Contribution categories

Future contributions should be classified at least as:

| Category | Examples | Required review |
|---|---|---|
| Editorial / didactic | Clarity, structure, grammar, diagrams, learning objectives | Editorial review |
| Technical / domain | Technical accuracy, domain examples, references | Relevant subject-matter review |
| Methodological | VALUE practices, lifecycle, tools, procedures | VALUE method owner / designated reviewers |
| Scientific | TGCV models, hypotheses, evidence, interpretation | Applicable TGCV scientific governance |
| Ecosystem / platform | ValueLabOS capabilities, workflows, integrations | Product/ecosystem review, with method boundary preserved |

A contribution that crosses categories must receive all applicable reviews.

### 8.3 Future contribution workflow

The intended future workflow is:

1. A contributor identifies an issue or proposes a change.
2. The proposal identifies affected pages, change category and rationale.
3. Editorial triage determines the required review path.
4. Relevant reviewers assess clarity, correctness, evidence, consistency and impact.
5. The proposal is accepted, revised or rejected with a recorded rationale.
6. Accepted changes are merged into the canonical source.
7. The published Learning content is rebuilt or updated.
8. The version history and change notes make the evolution traceable.

GitHub Issues and Pull Requests are a plausible initial mechanism, but the final tooling decision is deferred until the contribution model is designed.

### 8.4 Community and standardisation boundary

The possibility of evolving into an open body of practice or a standard is a long-term opportunity, not a current status.

- Community contributions do not automatically become authoritative.
- Popularity is not evidence of correctness.
- Editorial acceptance is not scientific validation.
- Adoption must be demonstrated, not asserted.
- Any future standardisation path requires explicit governance, transparent decision rights, external participation and evaluation.

## 9. Technical and publishing architecture principles

The architecture should remain implementation-neutral at this stage.

### 9.1 Principles

- Content-first, not framework-first.
- GitHub as canonical content source.
- Stable URLs and identifiers.
- Clear separation between content, navigation metadata, presentation and application logic.
- Reusable components for glossary, references, diagrams and callouts.
- Bilingual-ready structure.
- Search and cross-linking.
- Accessible and responsive presentation.
- Portability and low migration cost.
- No dependency on ValueLabOS for reading or learning.

### 9.2 Reference patterns

Use these as experience references, not as mandatory technology choices:
- The Rust Programming Language online book: progressive reading and book-like chapter structure.
- Starlight: documentation navigation, modular content and sidebar-led discovery.

Official references:
- https://doc.rust-lang.org/book/
- https://starlight.astro.build/

### 9.3 Technology decision deferred

The choice between Starlight, another documentation framework, or a custom implementation must follow:
- detailed content architecture;
- UX requirements;
- bilingual and routing requirements;
- search and cross-reference needs;
- compatibility with the existing TGCV web architecture;
- maintenance and contributor workflow evaluation.

This document does not authorise implementation or migration.

## 10. Relationship with the TGCV website

Learning should be a first-class website destination, but it should not be confused with the existing Research, Value Construction or Labs & Applications sections.

Proposed information architecture:
- **TGCV website:** public identity, research, disciplines, concepts, applications and contact.
- **Learning:** structured educational access to *Transformational Value* and future learning resources.
- **Research:** research programme, methods, evidence, limitations and open questions.
- **Value Construction:** public introduction to VALUE and its applied purpose.
- **Labs & Applications:** bounded demonstrators, experiments and application explorations.
- **ValueLabOS:** proposed ecosystem, distinct from the website and its Learning section.

The exact position of Learning in the global navigation, its relationship to Explore and any future sub-navigation must be specified in the website master brief and navigation design. Adding Learning is a proposed scope extension; it is not silently implemented by this document.

## 11. Development roadmap

### Phase 1 — Knowledge architecture
- Confirm purpose, audiences and editorial boundaries.
- Develop the detailed book table of contents.
- Map concepts, prerequisites and cross-references.
- Define page granularity and content types.
- Define metadata, glossary and reference model.
- Identify source assets and evidence dependencies.
- Produce a content coverage and gap analysis.

**Exit condition:** an internally coherent and reviewable content architecture, not merely a list of chapter titles.

### Phase 2 — Book development
- Draft chapters and supporting pages.
- Develop diagrams, examples, exercises and case material.
- Review technical, methodological and scientific claims.
- Review consistency, terminology and references.
- Prepare Spanish and English publication plan.
- Establish initial editorial version and change history.

**Exit condition:** a coherent first edition suitable for publication as a reference work, with limitations and unfinished areas disclosed.

### Phase 3 — Learning experience
- Specify Learning navigation and page templates.
- Select publishing technology based on requirements.
- Implement responsive sidebar, content layout, search and cross-links.
- Connect the site to canonical GitHub content.
- Test accessibility, navigation, performance and bilingual behaviour.
- Publish only after content and destination checks.

**Exit condition:** a usable, accessible and maintainable Learning experience.

### Phase 4 — Community evolution
- Observe actual readership and usage.
- Identify whether there is a real contributor community.
- Define contributor roles and review authority.
- Establish contribution guidelines and issue/PR templates.
- Pilot contributions with transparent review.
- Publish governance and versioning rules.
- Consider a broader standardisation path only if adoption and external participation justify it.

**Exit condition:** a functioning and proportionate contribution process, not simply the presence of a public repository.

## 12. Initial decision register

| ID | Decision / question | Initial position | Status |
|---|---|---|---|
| D01 | Keep book identity | *TRANSFORMATIONAL VALUE — Understanding, Designing and Realizing Value in Changing Systems* | Inherited working decision |
| D02 | Use three-part structure | Understanding Transformation / Designing Value / Evolving Value | Provisional baseline |
| D03 | Create public Learning section | Yes, as a first-class learning destination | Proposed; website scope update required |
| D04 | Learning UX pattern | Combine online-book progression with documentation-style sidebar navigation | Proposed |
| D05 | Canonical content source | Version-controlled Markdown in GitHub | Recommended principle |
| D06 | Keep content independent of ValueLabOS | Yes | Architectural constraint |
| D07 | Design for bilingual content | Yes, from the beginning | Recommended requirement |
| D08 | Prepare future community contribution | Yes, but activate only when adoption justifies it | Strategic direction |
| D09 | Select web framework | Defer until requirements and content architecture are clear | Open |
| D10 | Finalise detailed table of contents | Detailed proposal created; structural review pending | In review |
| D11 | Finalise metadata/content schema | After content model is reviewed | Open |
| D12 | Define editorial and scientific review roles | Lightweight initial governance, explicit future scaling | Open |
| D13 | Confirm Learning navigation placement | Update web master brief after architecture review | Open |
| D14 | Decide licensing per content class | Evaluate separately for book text, research material, code, demos and community contributions | Open |

## 13. Source assets and dependencies

The following assets are initial references and must be checked for current versions and consistency before drafting dependent content:

- `05_ASSETS/Business_Translation/TGCV_VALUE_VALUELABOS_IDENTITY_ARCH_v0.1.md` — identity architecture and reference-book proposal.
- `05_ASSETS/Business_Translation/VALUE_METHODOLOGY_LIFECYCLE_001.md` — VALUE methodology architecture.
- `05_ASSETS/Business_Translation/VALUE_FICTIONAL_CASE_CLINIC_001_v1.1.md` — fictional clinic case, subject to current-version and publication-suitability checks.
- Current TGCV scientific governance and evidence sources in their authoritative locations.
- `06_WEB/TGCV_WEB_MASTER_BRIEF_v0.1.md` on the web strategy branch — current website identity, navigation and editorial constraints.

The web master brief remains authoritative for website scope and public navigation until explicitly revised. This book/Learning master document governs the book and Learning architecture; neither document silently overrides the other's domain.

## 14. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Book becomes a promotional narrative rather than a rigorous reference | Editorial independence, evidence labels and explicit limitations |
| TGCV, VALUE and ValueLabOS are conflated | Preserve identity boundaries and review all cross-layer descriptions |
| Content structure is dictated by a web framework | Complete knowledge architecture before technology selection |
| Excessive chapter fragmentation | Use coherent learning pages with stable identifiers |
| Duplicate or contradictory definitions | Canonical glossary entries and cross-links |
| Scientific claims become stale | Link to authoritative evidence and schedule claim reviews |
| Community edits weaken methodological/scientific integrity | Categorised review paths and explicit decision authority |
| Bilingual versions drift | Linked language counterparts and terminology controls |
| Community infrastructure is built before there is a community | Defer accounts, forums and contribution UI until adoption warrants them |
| The book is treated as a standard before adoption | Use accurate status language and require external evidence |

## 15. Versioning and change control

- This document is the master architecture for the book and Learning initiative.
- Subordinate specifications may be created when needed, but must reference this document and must not redefine its governing decisions independently.
- Material changes to identity, scope, epistemic boundaries, content governance or the relationship between TGCV, VALUE and ValueLabOS require an explicit revision here.
- Changes to website navigation and implementation requirements must also be reflected in the Web Master Brief.
- Changes to TGCV scientific claims must follow scientific governance, not this document.
- Once chapter content exists, each page should carry stable metadata and be version-controlled.
- A public edition should have a clearly identifiable release/version and a change history.

### Version history

- **v0.1 — 2026-11-26:** Initial master architecture for the *Transformational Value* reference work, Learning experience, GitHub-based knowledge source, evidence boundaries, future community evolution and phased development.


## 16. Detailed table of contents — subordinate specification

The first detailed chapter-level proposal is maintained in a separate, versioned document:

**[TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md](TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md)**

It contains:
- the proposed reader journey and editorial logic;
- front matter and the three-part chapter structure;
- chapter purposes and section-level breakdowns;
- a reusable chapter template;
- cross-cutting editorial, evidence and bilingual requirements;
- an initial content dependency map;
- ten structural questions to resolve before approval.

The detailed contents document is subordinate to this master architecture. It may develop chapter structure but cannot redefine the identity boundaries, scientific status, VALUE methodology or governance principles established here.

**Current status:** proposed for structural review; not yet approved as the final table of contents.

### Version history

- **v0.2 — 2026-11-26:** Added the detailed table-of-contents specification and updated the decision register to reflect that structural review is now the next action.


## 17. Native Spanish and English authoring — governing requirement

The book and all Learning content units must be authored natively in Spanish and English. The language versions are parallel original editorial works with equivalent meaning, scope and quality; one is not merely a translation of the other.

This requirement applies to every content level: front matter, parts, chapters, sections, glossary entries, examples, exercises, case studies, captions, diagrams, navigation labels and supporting resources. Shared identifiers and metadata should connect language counterparts, while each language retains its own natural expression.

The content model must make bilingual completeness and review status visible. No content unit may be described as fully bilingual while one language version is missing, materially incomplete or awaiting required review.

Approved proper names and framework/product labels remain unchanged. Other titles and explanatory content should be composed naturally in Spanish or English as appropriate.

### Version history

- **v0.3 — 2026-11-26:** Established native Spanish and English authorship as a mandatory editorial requirement for every book and Learning content unit, including parity, metadata, review and terminology controls.


## 18. Content model and editorial workflow — subordinate specification

The proposed repository structure, stable content IDs, metadata, native bilingual pairing, glossary and reference registries, editorial workflow, contribution routing and versioning model are specified in:

**[TRANSFORMATIONAL_VALUE_CONTENT_MODEL_EDITORIAL_WORKFLOW_v0.1.md](TRANSFORMATIONAL_VALUE_CONTENT_MODEL_EDITORIAL_WORKFLOW_v0.1.md)**

This subordinate specification translates the governing principles of this master architecture into an authoring and maintenance model. It does not select a publishing framework, approve licences, authorise public release or supersede TGCV scientific governance or VALUE methodological governance.

**Current status:** proposal for review. A representative proof of concept should be completed before the full repository structure is populated or large-scale chapter drafting begins.

### Version history

- **v0.4 — 2026-11-26:** Added the Content Model & Editorial Workflow subordinate specification, covering repository layout, stable IDs, bilingual native authoring, metadata, terminology, references, assets, editorial and contribution workflows, versioning and proof-of-concept requirements.


## 20. Repository organisation

The `05_ASSETS/TRANSFORMATIONAL_VALUE/` root is reserved for the three governing documents: this Master Architecture, the Detailed TOC and the Content Model & Editorial Workflow. Supporting proof-of-concept specifications and reports belong in `PoC/`. Book content and shared learning resources must follow the directory model defined in the Content Model & Editorial Workflow, with native Spanish and English book content kept under `book/es/` and `book/en/` respectively. Do not accumulate working notes, chapter drafts or PoC artefacts in the root.

## 21. Version history

- **v0.5 — 2026-11-26:** Established the clean repository-root convention: three governing documents only; PoC artefacts under `PoC/`; book content and shared resources in the architecture-defined directory tree.

## 22. Limited authorisation — Learning Publishing PoC preview

**Decision:** The project owner explicitly authorised this limited amendment on 2026-11-26.

This section supersedes the blanket prohibition on website implementation only to the narrow extent stated below. It authorises implementation and testing of a **temporary, local, non-production preview solely to complete the existing Learning Publishing PoC**.

### 22.1 Permitted work

- Build the minimum preview needed to render the existing Chapter 3 content package in Spanish and English.
- Render and assess the existing shared conceptual diagram, its captions and alternative text in both languages.
- Test the PoC requirements for desktop and mobile layouts, navigation, language pairing, links, metadata and accessibility.
- Evaluate one or more candidate technologies for this bounded test, including Starlight if useful, without treating a successful trial as a framework selection.
- Use local execution and temporary, non-public test artefacts. A temporary private preview may be used only if technically necessary and without creating a production service or recurring cost.

### 22.2 Explicit exclusions

This authorisation does **not** permit:

- production website implementation, migration or launch;
- public release or indexing of the preview;
- purchase or registration of a domain, paid hosting, subscriptions or other deployment services;
- selection or approval of the final publishing framework;
- expansion beyond the existing PoC content package or creation of the complete Learning website;
- changes to TGCV scientific governance, scientific claims, VALUE status or the epistemic status of any evidence;
- changes to the approved chapter content except separately authorised editorial corrections.

### 22.3 Technical and governance controls

- Keep the preview isolated from the production TGCV website and from unrelated prototypes.
- Preserve GitHub as the canonical source of content and governance.
- Work only on the designated Learning editorial branch; do not write to `main`.
- Reuse the existing chapter, glossary, reference and diagram assets; do not recreate them.
- Keep content independent of the preview technology.
- Record the chosen test setup, commands, versions, actual test results, limitations and any unresolved defects in the PoC workspace.
- Do not claim a test passed unless it was actually executed and its result inspected.
- Stop before any action that would breach the exclusions above.

### 22.4 Exit condition

This limited authorisation remains in force only for completing and documenting the PoC preview and its tests. Completion of the PoC does not itself authorise production implementation, public release, migration or final framework selection. Those require separate explicit decisions.

### Version history

- **v0.6 — 2026-11-26:** Added owner-authorised, narrowly bounded permission for a local, non-production Learning PoC preview and its desktop, mobile, bilingual, diagram and accessibility tests. Production implementation, public release, paid deployment and final framework selection remain unauthorised.


## 23. Chapter review and correction discipline

Substantive chapter development must include a section-by-section conceptual review and a controlled correction cycle before a chapter is considered editorially complete. Findings are recorded in a persistent review record; unresolved conceptual choices are decided explicitly; accepted corrections are then integrated into both independently authored Spanish and English manuscripts; and the committed manuscripts are re-read to verify that the corrections and cross-language conceptual equivalence are present.

A review log is not the manuscript and does not demonstrate that a correction has been applied. Review completion, decision resolution, manuscript integration and post-commit verification are distinct states and must be tracked separately. A chapter must not advance as complete merely because its review notes have been written.

The detailed operational procedure is defined in §11.3 of the Content Model & Editorial Workflow. It governs chapter work across the book; the chapter-specific review record provides traceability but does not replace the canonical ES/EN source files.

### Version history

- **v0.7 — 2026-11-27:** Established section-by-section conceptual review, persistent findings, explicit decisions, bilingual manuscript integration and post-commit verification as required chapter-development discipline.
