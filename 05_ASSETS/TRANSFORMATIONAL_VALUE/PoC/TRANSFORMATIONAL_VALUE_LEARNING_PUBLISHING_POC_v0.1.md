# TRANSFORMATIONAL VALUE — Learning Publishing Proof of Concept

**Identifier:** TGCV-TV-POC-001  
**Version:** 0.4  
**Date:** 2026-11-26  
**Status:** PROPOSED VALIDATION SPECIFICATION — NOT IMPLEMENTATION AUTHORISATION  
**Branch:** `strategy/transformational-value-learning`  
**Governing documents:**
- `TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md`
- `TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md`
- `TRANSFORMATIONAL_VALUE_CONTENT_MODEL_EDITORIAL_WORKFLOW_v0.1.md`
- `05_ASSETS/Business_Translation/TGCV_VALUE_VALUELABOS_IDENTITY_ARCH_v0.1.md`

> This document defines a bounded proof of concept (PoC) to validate the proposed content model and Learning publishing experience. It does not authorise a production website, public release, full repository migration, framework selection, scientific claims, or large-scale book drafting.

---

## 1. Purpose

Validate that the proposed *TRANSFORMATIONAL VALUE* content architecture can support a coherent, accessible and maintainable bilingual online book before the project commits to full-scale authoring or publishing implementation.

The PoC must test the complete path from source content to rendered Learning experience:

1. Native Spanish and English authoring.
2. Stable content identity and metadata.
3. Shared glossary and reference records.
4. Reusable visual assets with editable sources.
5. Hierarchical navigation and direct page access.
6. Language pairing and switching.
7. Automated structural validation.
8. Draft preview without public publication.

The PoC is successful only if authors and reviewers can maintain the content without depending on a particular publishing framework or opaque visual assets.

## 2. Scope and boundaries

### 2.1 Included

- One representative book chapter, authored independently in Spanish and English.
- One glossary entry, authored independently in both languages.
- One shared conceptual diagram, with bilingual captions and alternative text.
- A small central reference set (target: two or three references).
- Stable content IDs and metadata.
- A hierarchical left-hand navigation panel.
- Chapter/section context, previous/next navigation and breadcrumbs or equivalent.
- A language selector that links only to the true counterpart.
- A responsive mobile navigation pattern.
- A draft build or preview, not publicly released.
- Automated checks for metadata, pairing, references, links and local assets.
- A short record of usability, authoring and technical findings.

### 2.2 Explicitly excluded

- Complete Learning website implementation.
- Production deployment or public release.
- User accounts, comments, bookmarks, learning progress or community contribution UI.
- Full-text search unless it is available with negligible implementation cost; search may be evaluated as a later requirement.
- Interactive exercises or software demonstrations.
- Full book drafting or creation of empty files for all planned chapters.
- Final selection of Starlight, another static-site generator, a CMS or a custom application.
- Any change to TGCV scientific governance or the epistemic status of TGCV claims.
- Any assumption that VALUE, ValueLabOS or the proposed TGCV–VALUE relationship is empirically validated.

## 3. Representative content selection

### 3.1 Recommended chapter

Use **Chapter 3 — The Space of Accessible Transformations** (TOC identifier: `TV-CH-03`) as the preferred pilot chapter, subject to a source-readiness check before drafting.

Reasons:
- It tests whether a central TGCV concept can be taught progressively.
- It exercises the distinction between candidate transformations and transformations accessible under specified conditions.
- It requires careful treatment of assumptions, boundaries and evidence.
- It provides a meaningful test of references, terminology, diagrams and epistemic qualifications.
- It is directly relevant to the identity and purpose of the reference work.

The chapter is a content-model test, not a vehicle for resolving open research questions. It must describe only what the current authoritative TGCV sources support and clearly identify proposals, hypotheses and limitations.

If the source-readiness check finds that Chapter 3 cannot be drafted responsibly from available authoritative material, do not fill gaps by inference. Record the gap and select the nearest suitable chapter with the strongest source support. The selection change must be documented before drafting.

### 3.2 Required content package

| Unit | Shared ID | Languages | Purpose |
|---|---|---|---|
| Pilot chapter | `TV-CH-03` | es, en | Validate a full bilingual book page |
| Glossary entry | `TV-TERM-XXX` | es, en | Validate terminology pairing and reuse |
| Diagram | `TV-DIA-XXX` | Shared source; bilingual text variants if needed | Validate editable asset workflow |
| References | `REF-XXXX` | Shared records | Validate source traceability |

The exact glossary and diagram IDs must be allocated from the content registry or agreed ID sequence before files are created. Do not invent duplicate IDs if a canonical record already exists.

### 3.3 Chapter content requirements

Each language version must include, as appropriate:

- A clear purpose and short introduction.
- Learning objectives.
- Definitions and distinctions required to understand the chapter.
- A progressive explanation with at least one concrete example.
- The shared diagram and an explanation of what it does and does not represent.
- Explicit assumptions, scope and limitations.
- Links to the glossary and references.
- A concise synthesis.
- Reflection or application questions.

The Spanish and English versions must be authored natively. Neither is the source translation of the other.

The two versions may differ in sentence structure, paragraph count and idiom, but must have equivalent conceptual coverage, learning objectives, examples, references, qualifications and depth.

## 4. Proposed source structure for the PoC

Use only the minimum directories needed for the test. This is a trial of the content model, not the creation of the entire future repository tree.

Proposed structure:

```text
05_ASSETS/TRANSFORMATIONAL_VALUE/
  poc/
    README.md
    registry/
      content-registry.yml
      references.yml
      terminology.yml
    book/
      es/
        part-01-understanding-transformation/
          ch-03-espacio-de-transformaciones-accesibles.md
      en/
        part-01-understanding-transformation/
          ch-03-space-of-accessible-transformations.md
    glossary/
      es/
        [glossary-entry].md
      en/
        [glossary-entry].md
    assets/
      diagrams/
        [diagram-id]/
          source/
          exports/
          README.md
    validation/
      README.md
      test-results/
```

The exact filenames for the glossary and diagram are assigned when their IDs and canonical terms are confirmed.

Do not create empty folders or placeholder files for the other 21 chapters. Do not duplicate shared references, glossary definitions or diagrams inside both language folders.

## 5. Metadata and registry validation

The PoC must exercise the proposed metadata model from the Content Model & Editorial Workflow document.

At minimum, validate:

- `content_id` and `language_pair_id`;
- `title`, `language`, `content_type` and `status`;
- `version`, `created` and `updated`;
- `authors`, `summary`;
- `part`, `chapter` and `parent_id` where applicable;
- glossary concepts, prerequisites and related content IDs;
- reference IDs and source asset IDs;
- epistemic status where claims require it;
- licence only where an approved licence has actually been assigned.

Automated checks must detect at least:

1. Missing required metadata.
2. Invalid language or status values.
3. Duplicate content IDs or conflicting language pairs.
4. Missing Spanish or English counterpart.
5. A language switch that points to a non-counterpart.
6. Broken internal content links.
7. Unknown glossary, reference or asset IDs.
8. Missing local asset files.
9. Duplicate or conflicting routes.
10. Draft content accidentally included in the public-output configuration.

A passing validation run confirms structural consistency only. It does not approve the accuracy, scientific validity or methodological authority of the content.

## 6. Learning interface requirements

### 6.1 Desktop experience

The preview must demonstrate:

**Left navigation**
- A persistent hierarchical panel.
- Expandable/collapsible book parts and chapters.
- Clear indication of the active page.
- Stable ordering independent of file-system accident.
- Navigation labels in the selected interface language.

**Main reading area**
- Clear page title and location context.
- Readable heading hierarchy and body typography.
- Rendering of the shared diagram, captions and explanatory text.
- Working internal links and references.
- Previous/next navigation.

**Language control**
- A visible Spanish/English selector.
- Switching from one page to its actual counterpart.
- No silent fallback to a different chapter or to an untranslated page.
- A clear indication if a counterpart is not yet available.

### 6.2 Mobile experience

On narrow screens:
- The left navigation becomes an accessible drawer or equivalent compact navigation.
- The reader can open and close navigation without losing page context.
- Main content remains readable without horizontal scrolling, except for intentionally scrollable wide tables or diagrams.
- Language switching and previous/next navigation remain available.

### 6.3 Accessibility

The PoC must check:
- Keyboard operation of all navigation controls.
- Visible focus states.
- Semantic heading order and landmarks.
- Adequate text/background contrast.
- Meaningful link labels.
- Alternative text for the diagram.
- No reliance on colour alone.
- Usability at common desktop and mobile viewport widths.

The PoC is not a formal accessibility certification. Any known gaps must be recorded.

## 7. Visual assets: editability, provenance and licensing

Visual assets are part of the maintained knowledge base, not disposable decoration.

For the pilot diagram:

- Maintain an editable source file in a documented, versionable format.
- Prefer text-based formats such as Mermaid or SVG where they meet the diagram's needs.
- Store rendered exports separately from editable sources.
- Give the diagram a stable asset ID.
- Record its title, purpose, source, version, owner and dependencies.
- Provide Spanish and English captions and alternative text.
- Keep embedded labels language-neutral where practical; otherwise maintain controlled language variants from the same source.
- Explain the diagram in surrounding text; do not make an image the sole carrier of a critical claim.
- Check third-party rights and licence compatibility before publication.

Do not use AI-generated raster images as the only editable source of a conceptual model, architecture or process diagram. AI-generated illustrations may be considered later where they add genuine explanatory value and their provenance and reuse rights are clear.

No content or asset licence is presumed by this PoC. Licence fields remain unset until the project approves the relevant policy.

## 8. Publishing technology evaluation

The PoC must remain framework-neutral at the requirements level.

It may use one or more candidate technologies to render the preview, but a successful trial does not by itself establish the production framework decision.

Evaluate candidate publishing approaches against:

- Markdown and metadata compatibility.
- Hierarchical sidebar and ordering control.
- Bilingual route pairing.
- Stable URLs and redirects.
- Diagram and asset handling.
- Accessibility and responsive behaviour.
- Search capability and extensibility.
- Build-time validation and draft exclusion.
- Ease of authoring and review through GitHub.
- Portability and avoidance of unnecessary vendor lock-in.
- Fit with the existing TGCV website and deployment architecture.
- Maintenance burden for a small project team.

Starlight may be included as a candidate because its documentation-oriented model resembles the intended experience. The Rust online book is a UX reference, not a requirement to use its technology.

Record evidence and trade-offs for each evaluated candidate. Do not select a framework solely because the first demo is visually attractive.

## 9. Test plan

| Test ID | Test | Expected result |
|---|---|---|
| POC-01 | Build Spanish chapter | Page renders with correct metadata and content |
| POC-02 | Build English counterpart | Page renders independently and naturally |
| POC-03 | Switch language | Correct counterpart opens and preserves content identity |
| POC-04 | Navigate hierarchy | Part/chapter ordering and active state are correct |
| POC-05 | Previous/next | Sequence follows the approved registry |
| POC-06 | Open glossary link | Correct language-specific glossary page opens |
| POC-07 | Render diagram | Correct asset appears with language-appropriate caption and alt text |
| POC-08 | Resolve references | All declared reference IDs resolve to valid records |
| POC-09 | Validate metadata | Valid sample passes; intentionally invalid fixtures fail with actionable messages |
| POC-10 | Detect broken links/assets | Broken fixtures are detected |
| POC-11 | Exclude drafts | Draft content is absent from public-output build |
| POC-12 | Keyboard navigation | Core reading and navigation path works without a pointer |
| POC-13 | Responsive layout | Navigation and content work on desktop and mobile widths |
| POC-14 | Rebuild from clean checkout | Preview can be reproduced from documented repository instructions |

Test fixtures that intentionally contain errors must be isolated from publishable source content.

## 10. Acceptance criteria

The PoC is accepted only when all mandatory criteria below are met or a deviation is explicitly approved and recorded.

### Content and editorial
- Both chapter versions are original authored texts.
- Conceptual equivalence has been reviewed and recorded.
- Required sources and evidence qualifications are traceable.
- The glossary entry is reusable from both language versions.
- No unsupported scientific or methodological claim has been introduced.
- Editorial status is maintained separately for each language.
- The chapter is not marked approved or published merely because the preview builds.
- Each language version independently passes the mandatory reader-facing terminology gate defined in the Content Model & Editorial Workflow §22.
- The terminology audit covers all visible surfaces: titles, headings, prose, examples, tables, diagrams, labels, legends, captions, alt text, glossary, navigation, references, notes and downloadable material.
- Any internal identifier retained in a reader-facing surface has a documented rationale and the required approval; otherwise it is removed or replaced by a precise description.
- The audit records Spanish and English findings separately, including retained acronyms, technical notation and justified exceptions.

### Navigation and experience
- The left-hand hierarchy works on desktop.
- Mobile navigation is usable.
- The active page and reading sequence are clear.
- Language switching resolves to the correct counterpart.
- Previous/next navigation follows the content registry.
- Core content is readable and accessible by keyboard.

### Technical and maintenance
- Metadata and link validation run reproducibly.
- Invalid fixtures fail as expected.
- Draft content is excluded from the public-output configuration.
- The diagram has an editable source and documented provenance.
- A clean checkout can reproduce the preview.
- No production website or public release has occurred.

### Decision quality
- Findings, defects, trade-offs and unresolved questions are recorded.
- The project can decide whether to refine the model, repeat the PoC, compare another publishing approach or proceed to a larger pilot.
- No production framework is selected without an explicit decision record.

## 11. Roles and review

The initial PoC may be developed by a small team, but review responsibilities must remain distinct:

- **Content author(s):** create the Spanish and English originals.
- **Editorial reviewer:** checks clarity, structure and didactic quality.
- **Subject reviewer:** checks TGCV or other specialist claims against authoritative sources.
- **Bilingual reviewer:** checks conceptual equivalence and naturalness in both languages.
- **Technical implementer:** builds the preview and validation.
- **Project owner:** accepts the PoC scope and records the next decision.

One person may perform more than one role in this early phase, but the review record must disclose that fact. Technical implementation cannot substitute for subject-matter review.

## 12. Execution sequence and gates

### Gate 0 — Source readiness

Before drafting:
1. Confirm the authoritative source material for Chapter 3.
2. Identify unsupported or unresolved content areas.
3. Confirm the canonical glossary term and any existing definition.
4. Confirm reference records and source locations.
5. Allocate stable content and asset IDs.

**Exit condition:** a bounded chapter outline and source map exist; no unresolved source gap is being concealed by drafting.

### Gate 1 — Content package

1. Draft both language versions natively.
2. Create the paired glossary entry.
3. Create the shared editable diagram.
4. Add metadata, references and cross-links.
5. Complete editorial, subject and bilingual reviews appropriate to the content.

**Exit condition:** the package is structurally complete and ready for preview; editorial approval is recorded separately from scientific status.

### Gate 2 — Publishing preview

1. Implement the minimum interface against the content package.
2. Run the test plan.
3. Record accessibility and responsive findings.
4. Verify reproducibility from a clean checkout.

**Exit condition:** test results and defects are documented; no public release.

### Gate 3 — Evaluation and decision

Review:
- authoring effort and friction;
- bilingual maintenance effort;
- navigation and reading quality;
- validation coverage;
- asset editability and provenance;
- technical complexity and maintenance cost;
- framework fit and portability.

Possible decisions:
- accept the model and proceed to a larger pilot;
- accept with specified changes;
- repeat with a different chapter or publishing candidate;
- revise the content model;
- stop the approach if the maintenance burden or limitations are unacceptable.

No automatic progression to production is implied.

## 13. Deliverables

The PoC is expected to produce:

1. A Spanish pilot chapter.
2. An independently authored English counterpart.
3. A bilingual glossary entry.
4. An editable shared diagram and rendered exports.
5. A small reference registry.
6. A content registry and metadata fixtures.
7. A navigable draft preview.
8. Automated validation scripts/checks and test results.
9. A concise evaluation report with defects, limitations and recommendations.
10. A decision record authorising or declining the next phase.

## 14. Risks and controls

| Risk | Control |
|---|---|
| Drafting outruns source maturity | Source-readiness gate and explicit gap register |
| One language becomes a translation of the other | Native authorship and independent language review |
| Editorial approval is mistaken for scientific validation | Separate editorial and epistemic status |
| Framework choice drives content architecture | Framework-neutral content model and comparative evaluation |
| Visual assets become opaque or unmaintainable | Editable sources, IDs, provenance and versioning |
| PoC grows into a production project | Fixed scope, explicit exclusions and decision gates |
| Empty chapter scaffolding creates maintenance overhead | Create only the representative pilot content |
| A preview is accidentally published | Draft-only build and explicit release exclusion |

## 15. Open decisions

The PoC must not silently resolve the following:

1. Final publishing framework and hosting/deployment approach.
2. Whether the content registry is manually maintained or generated.
3. Exact YAML schema and validation implementation.
4. Bibliographic registry format.
5. Final licence policy for prose, research material, diagrams, code and contributions.
6. Whether both languages must be ready simultaneously for each release.
7. The long-term relationship between the book repository and the main TGCV website repository.
8. Whether search belongs in the first public release or a later enhancement.

## 16. Version history

- **v0.1 — 2026-11-26:** Initial bounded PoC specification covering bilingual content, content model, navigation, visual asset governance, framework-neutral evaluation, validation, acceptance criteria and staged decision gates.
- **v0.2 — 2026-11-26:** Aligned the directory example and location references with the dedicated `PoC/` workspace and the canonical repository layout.


## 17. Reader-facing terminology control

The PoC must demonstrate the book-wide terminology policy in the Content Model & Editorial Workflow §22. This is not limited to Chapter 3 prose: every reader-facing surface produced by the PoC is in scope.

### 17.1 Required audit scope

Audit both language versions independently, including:

- chapter title, headings, subheadings and body text;
- examples, tables, callouts, summaries and reflection questions;
- diagram labels, legends, captions, figure notes and alternative text;
- glossary entry and its cross-links;
- navigation labels, page summaries and language-switch labels;
- public references, notes and any downloadable reader-facing resource.

### 17.2 Internal identifiers and terminology

- Internal experiment, study, workstream, dataset, run, gate, evidence and repository identifiers may remain in this private PoC/source-readiness documentation where needed for traceability.
- They must not appear as unexplained names in the public chapter, diagram, captions, glossary, references or Learning interface.
- Describe the substance of the research: what was examined, in which setting, by what method, and what the bounded result does and does not support.
- Do not invent a public-facing study name unless it has been deliberately approved. Prefer a precise descriptive phrase.
- Acronyms must be discipline-standard, approved public terminology, or defined at first use and genuinely useful thereafter.
- Technical notation such as (T_{acc}) may be retained when it belongs to the conceptual model and is explained clearly.
- An identifier retained in a public technical appendix for reproducibility requires a documented reason and approval under the governing terminology policy.

### 17.3 Mandatory PoC acceptance test

The PoC must include a terminology-audit record with separate Spanish and English results. For each language, the record must confirm:

1. All reader-facing surfaces listed in §17.1 were inspected.
2. Acronyms, abbreviations, alphanumeric codes and opaque labels were identified and classified.
3. Internal identifiers were removed or replaced with precise descriptions, except for explicitly approved and explained exceptions.
4. Retained acronyms and technical notation are defined and used consistently.
5. The terminology register and counterpart language version were checked for conceptual consistency and natural wording.
6. Any exception records its rationale, approving authority and affected location.

Automated searches should be used to flag likely internal codes and unexplained abbreviations, but a human semantic review is still mandatory. A clean automated scan alone does not pass the test.

**Acceptance rule:** if either language version contains an unexplained internal identifier on any reader-facing surface, that version fails the terminology test and cannot be marked approved. The PoC cannot be accepted as demonstrating the bilingual publishing model until both language audits pass.

## 18. Version history

- **v0.3 — 2026-11-26:** Added reader-facing terminology and acronym controls for the Chapter 3 content package; internal identifiers remain solely for source traceability.
- **v0.4 — 2026-11-26:** Aligned the PoC with the book-wide terminology policy; extended the audit to every reader-facing surface and made independently recorded Spanish and English terminology checks mandatory acceptance criteria.
