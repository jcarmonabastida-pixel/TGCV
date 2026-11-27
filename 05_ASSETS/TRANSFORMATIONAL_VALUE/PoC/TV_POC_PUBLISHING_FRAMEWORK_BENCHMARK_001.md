# Learning Publishing PoC — publishing framework benchmark

**Record ID:** TV-POC-BENCH-001  
**Version:** 0.1  
**Date:** 2026-11-27  
**Status:** DESK BENCHMARK — PRELIMINARY RECOMMENDATION; RUNTIME VALIDATION PENDING  
**Branch:** strategy/transformational-value-learning  
**Scope:** Compare Starlight, Stratus and a hybrid architecture for TGCV web + Learning  
**Governing specification:** TGCV-TV-POC-001 v0.4  
**Related records:** TV-POC-TECH-001, TV-POC-IMPL-001, TV-POC-VISUAL-001

> This benchmark is an evidence-based desk evaluation of the candidate repositories, documentation and current PoC state. It is not a completed runtime benchmark, framework selection, migration plan or implementation authorisation.

## 1. Executive conclusion

**Preliminary preferred architecture: Stratus for the TGCV institutional website and Starlight for the TRANSFORMATIONAL VALUE Learning book.**

This hybrid option best matches the different jobs:

- The TGCV website needs distinctive visual presentation, flexible landing pages, reusable sections and a coherent brand system.
- Learning is a long-form bilingual book with a substantial chapter hierarchy, native Markdown sources, language pairing, references, diagrams and a reading-focused navigation model.

Starlight is more directly aligned with the second job. Stratus is more directly aligned with the first.

The recommendation is conditional. The existing Starlight preview has demonstrated local content generation and build behaviour, but the full PoC visual/accessibility gate remains open. Stratus has been inspected statically; no clean install, build, browser or accessibility run has been performed in this benchmark.

The hybrid architecture also creates an integration and deployment boundary that must be designed deliberately.

## 2. Decision context and baseline

The governing PoC explicitly excludes final framework selection and requires candidates to be evaluated against content compatibility, bilingual pairing, navigation, diagrams, accessibility, validation, authoring, portability and maintenance.

Existing work on this branch:

- **TGCV-TV-POC-001 v0.4:** requirements for the bilingual book preview.
- **TV-POC-TECH-001:** initial Astro + Starlight candidate approach.
- **TV-POC-IMPL-001:** isolated Starlight preview implementation record.
- **TV-POC-VISUAL-001:** proposed framework-neutral reusable visual asset pattern.
- **Current local preview:** Chapter 3 is generated from canonical Spanish and English Markdown, KaTeX works after a documented delimiter-normalisation step, Mermaid SVG exports are generated during preparation, and the local Astro build has succeeded. Browser legibility/accessibility findings remain open.

This benchmark does not erase the existing work or imply that Starlight has passed all acceptance criteria.

## 3. Candidates

### 3.1 Starlight — one framework for the whole site

Starlight is Astro's documentation-focused framework. It includes documentation navigation, search, internationalisation, accessible reading-oriented defaults, Markdown/MDX content, code highlighting and theming.

**Strengths**
- Native Markdown and MDX documentation pages.
- Locale-based page pairing and language switching support.
- Hierarchical sidebar configuration and page navigation.
- A focused reading interface suitable for long chapters.
- Full Astro extensibility for custom landing pages and components.
- Existing TGCV Chapter 3 preview already uses it.

**Limitations for the institutional website**
- Its primary abstraction is a documentation site, not a highly art-directed institutional website with many different marketing and editorial page compositions.
- It can be customised using Astro, but extensive custom composition may work against the benefits of choosing a specialised documentation framework.

**Assessment:** strong for Learning; possible but not the most natural foundation for the whole TGCV website.

### 3.2 Stratus — one framework for the whole site

Stratus is a complete Astro documentation-site template maintained by CloudCannon. Its README describes it as source code that the adopting project owns and can modify. It includes a page builder, component library, grouped documentation sidebar, client-side search, table of contents, print layout, diagrams and design tokens.

**Strengths**
- A richer page-composition model for the institutional website.
- Reusable page sections and building blocks.
- Brand styling through shared design tokens.
- Static Astro output and Pagefind search indexing.
- Component source is available for modification; the template is MIT-licensed.
- The CloudCannon visual-editing layer is an optional operating model rather than a requirement to use the generated static site.

**Important limitations for Learning**
- Its documentation collection is explicitly configured with a Markdown/MDX loader pattern that only matches MDX files. A .md file in that collection is silently skipped. Astro itself supports Markdown, but Stratus's current documentation collection must be adapted to load canonical TGCV .md files or use a deterministic adapter.
- The documentation page schema is relatively simple (title, description, group, order, etc.). TGCV metadata and paired language identities would need a deliberate schema extension.
- The sidebar is derived from each page's group and order; sidebar.json orders groups. A multi-level book hierarchy and exact chapter sequencing may require additional navigation logic.
- The included Mermaid component renders in the browser using client-side JavaScript. The source is initially shown and hidden after rendering. Its print fallback displays source text. This differs from the TGCV technical approach's preference for build-time SVG exports and requires separate accessibility, no-JavaScript and print evaluation.
- The template's current package manifest specifies Astro 7.2 and Node >=22.12. The existing TGCV preview uses Astro 5.x. A Stratus-based site would be a separate application and should not be forced into the current preview dependency tree.
- The CloudCannon component editing conventions add a vendor-specific authoring layer. The project can own the source, but should decide whether it will use CloudCannon visual editing or maintain content through GitHub-only workflows.

**Assessment:** strong candidate for the institutional website; viable for Learning only after a non-trivial content/navigation/diagram adaptation.

### 3.3 Hybrid — Stratus website + Starlight Learning

The institutional site and book are separate Astro applications, each using the template best suited to its purpose.

**Benefits**
- Stratus can provide the TGCV identity, landing pages, institutional sections and reusable visual components.
- Starlight can provide the dedicated book-reading environment and native bilingual documentation structure.
- The two applications can evolve at different speeds without forcing the book into a marketing-site component model or the main website into a documentation shell.
- Both are Astro-based, so shared design tokens, typography, colours, icons and selected components can be shared deliberately where this does not create tight coupling.

**Costs and risks**
- Two build pipelines, dependency trees, release processes and test suites.
- Shared header/footer, language conventions, typography and visual identity must be coordinated.
- The route boundary must be designed: for example, a dedicated Learning subdomain or a /learning/ path served through deployment routing. Neither option is selected here.
- Cross-site links, canonical URLs, sitemap ownership, analytics/privacy configuration and navigation continuity need explicit handling.
- Shared components should be published or copied through a controlled source strategy; do not create an early shared package unless actual duplication justifies it.

**Assessment:** strongest strategic fit, with higher operational complexity than a single application.

## 4. Requirements comparison

Legend: Native = provided directly; Adaptation = requires configuration or implementation; Open = requires practical validation.

| Requirement | Starlight | Stratus | Hybrid |
|---|---|---|---|
| Distinctive TGCV institutional pages | Adaptation | Native strength | Native strength through Stratus |
| Long-form book reading | Native strength | Adaptation | Native strength through Starlight |
| Large hierarchical chapter navigation | Native strength | Adaptation | Native strength through Starlight |
| Spanish/English page pairing | Native i18n model | Custom implementation required | Native book pairing; website i18n separate |
| Canonical Markdown chapters | Native | Adaptation: current docs loader is MDX-only | Native in Learning |
| TGCV metadata and stable IDs | Schema extension | Schema extension | Schema extension in Learning |
| Glossary and references | Adaptation | Adaptation | Adaptation in Learning |
| KaTeX / mathematical notation | Already exercised in PoC; review open | Integration test required | Existing Starlight path retained |
| Build-time Mermaid SVG | Custom build integration; existing PoC approach | Replace/adapt client-side component | Existing Starlight approach retained |
| Responsive diagrams and accessible descriptions | Visual/accessibility gate open | Open; current component needs review | Open, isolated to book |
| Full-site design tokens and components | Custom design system | Native strength | Stratus design system plus controlled book theme |
| Search | Integrated Starlight search | Pagefind indexing in template | Separate indexes or coordinated strategy |
| Print-friendly book | Adaptation/test | Stratus has print layout; book output untested | Starlight book print behaviour untested |
| GitHub-first editorial workflow | Strong fit | Possible; CloudCannon visual editing optional | Strong for book; website workflow to define |
| Operational simplicity | Highest as one app | High as one app | Lowest: two apps and integration boundary |

## 5. Weighted decision matrix

Scores are preliminary judgement based on source inspection and current TGCV PoC evidence. They are not measured performance scores.

Scale: 1 = weak fit; 3 = workable with meaningful adaptation; 5 = strong fit.

| Criterion | Weight | Starlight for all | Stratus for all | Hybrid |
|---|---:|---:|---:|---:|
| Institutional website visual flexibility | 20% | 2 | 5 | 5 |
| Long-form book and navigation | 20% | 5 | 3 | 5 |
| Bilingual editorial experience | 15% | 5 | 2 | 4 |
| Canonical Markdown and content model | 10% | 5 | 2 | 5 |
| Diagram and mathematical publishing fit | 10% | 5 | 2 | 5 |
| Responsive/accessibility potential | 10% | 4 | 3 | 4 |
| Maintenance and operating simplicity | 10% | 5 | 4 | 3 |
| Extensibility and brand system | 5% | 3 | 5 | 4 |
| **Weighted result / 5** | **100%** | **4.2** | **3.25** | **4.5** |

### Interpretation

The hybrid option scores highest because it assigns each candidate to the domain where its architecture is strongest. Its lower operating-simplicity score is real and must not be hidden.

Starlight for all remains a credible alternative if minimising maintenance and deployment complexity becomes more important than the visual flexibility of the main website.

Stratus for all is not recommended at this stage because the book's bilingual, Markdown-first, long-form requirements would require more adaptation than the hybrid option.

## 6. Architecture recommendation

### 6.1 Proposed responsibility boundary

| Surface | Candidate | Primary responsibility |
|---|---|---|
| TGCV institutional website | Stratus | Identity, overview, Explore, Research, Systems Engineering, Value Construction, Transformational Intelligence, Labs & Applications |
| TRANSFORMATIONAL VALUE Learning book | Starlight | Bilingual long-form book, chapters, glossary, references, reading navigation and book-specific search |

This is a candidate architecture, not an approved production topology.

### 6.2 Shared design system

The two surfaces should share a small set of design decisions:
- TGCV logo and identity assets.
- Core colour and typography tokens.
- Link, focus and accessibility conventions.
- Language naming and switching conventions.
- Header/footer relationship and cross-site navigation labels.

They do not need to share the same page layout or component implementation.

### 6.3 Route and deployment options

Two possible route patterns should be evaluated later:

**Option A — dedicated Learning subdomain**
- Clear technical boundary and independent deployment.
- Simpler asset/base-path isolation.
- Requires strong visual and navigation continuity between domains.

**Option B — same domain under /learning/**
- More seamless reader experience.
- Requires deployment routing or reverse-proxy configuration, correct Astro base paths, asset URLs, canonical URLs and sitemap coordination.
- Must be tested before choosing.

No domain, hosting provider, deployment topology or public release is authorised by this benchmark.

## 7. What the benchmark has and has not tested

**Evidence reviewed**
- TGCV PoC v0.4 requirements and current technical/implementation records.
- Existing TGCV branch records for Starlight preview.
- Stratus repository README, package manifest, content collection schema and Mermaid component source.
- Official Astro documentation for Markdown and content collections.
- Official Starlight documentation for pages, sidebar and supported content formats.

**Not tested in this benchmark**
- Fresh installation and clean build of Stratus.
- Real TGCV page implementation using Stratus.
- Runtime bilingual navigation in Stratus.
- KaTeX compatibility with the actual Chapter 3 formulas in Stratus.
- Accessibility of Stratus Mermaid SVG output, including screen readers and no-JavaScript fallback.
- Print output of a long bilingual book in either candidate.
- A shared design-token implementation across two Astro applications.
- A deployment route joining Stratus and Starlight.
- Performance measurements, Lighthouse scores or browser compatibility.

No score in the matrix should be interpreted as a passed acceptance test.

## 8. Required validation before final decision

The next practical comparison should remain small and reversible.

### Work package A — close the existing Starlight baseline
1. Preserve the existing Chapter 3 preview.
2. Record current build and browser evidence.
3. Complete the outstanding responsive, diagram and accessibility checks.
4. Keep canonical Markdown and Mermaid sources unchanged.

### Work package B — minimal Stratus institutional-site trial
Use a separate temporary worktree or branch/workspace; do not replace the existing preview.
1. Run the unmodified Stratus starter and record its baseline.
2. Replace only the homepage content with a small TGCV identity/landing-page sample.
3. Reproduce one representative institutional page using its page sections and design tokens.
4. Test Spanish/English routing only to the extent needed to assess the website surface.
5. Record build, authoring effort, customisation effort and dependencies.
6. Do not migrate Learning chapters into this trial.

### Work package C — validate the hybrid boundary
1. Produce a small navigation and route-boundary prototype, without public deployment.
2. Verify that a reader can move from the TGCV website into Learning and return without confusion.
3. Compare a subdomain boundary with a /learning/ path boundary.
4. Verify shared identity tokens without forcing shared runtime components.
5. Estimate the ongoing build, test and maintenance burden of two applications.

### Work package D — Learning book acceptance
Complete the TGCV-TV-POC-001 requirements for the Starlight candidate:
- native Spanish/English source handling;
- stable chapter pairing and navigation;
- glossary and references;
- maths;
- reusable visual assets;
- responsive reading;
- accessibility;
- structural validation;
- reproducible local draft preview.

Only after these tests should a final framework/architecture decision be recorded.

## 9. Preliminary recommendation and decision gate

**Recommendation:** carry the hybrid architecture forward as the preferred candidate. Retain Starlight for Learning and evaluate Stratus as the institutional website foundation.

Do not:
- migrate the current Starlight PoC to Stratus;
- copy canonical chapters into Stratus;
- alter the current preview generator;
- replace the reusable visual asset design;
- create a production website or deployment;
- declare either candidate accepted.

The next decision gate is reached when the small Stratus institutional-site trial and the outstanding Starlight Learning checks have evidence. If Stratus proves too costly to adapt to TGCV identity or the two-app boundary imposes excessive maintenance, reconsider Starlight for all.

## 10. Sources

### TGCV project records
- [TGCV-TV-POC-001 v0.4](TRANSFORMATIONAL_VALUE_LEARNING_PUBLISHING_POC_v0.1.md)
- [TV-POC-TECH-001](TV_POC_PREVIEW_TECHNICAL_APPROACH_001.md)
- [TV-POC-IMPL-001](TV_POC_PREVIEW_IMPLEMENTATION_001.md)
- [TV-POC-VISUAL-001](TV_POC_REUSABLE_VISUAL_ASSET_PATTERN_001.md)

### Candidate repositories and official documentation
- [CloudCannon Stratus repository](https://github.com/CloudCannon/stratus-astro-documentation-template)
- [Stratus README](https://github.com/CloudCannon/stratus-astro-documentation-template/blob/main/README.md)
- [Stratus content collection schema](https://github.com/CloudCannon/stratus-astro-documentation-template/blob/main/src/content.config.ts)
- [Stratus Mermaid component](https://github.com/CloudCannon/stratus-astro-documentation-template/blob/main/src/components/building-blocks/core-elements/diagram/Diagram.astro)
- [Stratus Mermaid rendering logic](https://github.com/CloudCannon/stratus-astro-documentation-template/blob/main/src/components/building-blocks/core-elements/diagram/setup.ts)
- [Starlight overview](https://starlight.astro.build/)
- [Starlight pages and Markdown/MDX](https://starlight.astro.build/guides/pages/)
- [Starlight internationalisation](https://starlight.astro.build/guides/i18n/)
- [Starlight sidebar](https://starlight.astro.build/guides/sidebar/)
- [Astro Markdown content](https://docs.astro.build/en/guides/markdown-content/)
- [Astro content collections](https://docs.astro.build/en/guides/content-collections/)

## 11. Version history

- **v0.1 — 2026-11-27:** Initial desk benchmark of Starlight, Stratus and hybrid architecture. Preliminary recommendation is Stratus for the TGCV institutional website and Starlight for Learning. Runtime and deployment validation remain pending.
