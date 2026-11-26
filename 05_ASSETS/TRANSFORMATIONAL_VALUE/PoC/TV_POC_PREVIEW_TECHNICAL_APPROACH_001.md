# Learning Publishing PoC — technical approach for the preview

**Record ID:** TV-POC-TECH-001  
**Date:** 2026-11-26  
**Status:** Candidate approach for implementation; not a framework decision  
**Scope:** Chapter 3 bilingual preview and TV-DIA-001 only

## 1. Purpose

Define the smallest reproducible technical experiment that can test the existing Learning content package without creating a production website, changing approved chapter content, or selecting the final publishing framework.

The experiment is authorised by §22 of the Learning Master Architecture v0.6. It must remain local, isolated and non-production.

## 2. Source inspection findings

The following canonical sources exist on the Learning editorial branch:

- Spanish Chapter 3 Markdown, with YAML frontmatter and mathematical notation.
- English Chapter 3 Markdown, with YAML frontmatter and mathematical notation.
- Spanish and English Mermaid source files for TV-DIA-001.
- TV-DIA-001 README containing paired captions, alternative text and the outstanding visual/accessibility checklist.
- The content registry with the paired chapter routes and the diagram asset identity.

No root `package.json`, Astro configuration, Vite configuration or Learning preview workflow was found at the expected repository paths. The PoC workspace contains its orientation README but no preview implementation. This supports creating an isolated test project rather than adapting an unrelated prototype.

## 3. Candidate under test

**Candidate:** Astro + Starlight.

Rationale:
- Starlight is designed for structured documentation and provides a reading/navigation experience close to the PoC requirements.
- Astro supports Markdown content and configurable Markdown processing.
- The existing chapter files can remain the editorial source of truth; preview-specific copies or adapters must be generated, not manually forked.
- The trial can be built locally without a domain or paid hosting.

This is a candidate for the PoC only. A successful build or attractive preview does not select the production framework.

## 4. Rendering approach to test

### 4.1 Chapter content

Test rendering the original Spanish and English Markdown, preserving:
- the existing authored prose and headings;
- mathematical expressions and display equations;
- tables, lists, internal links and references;
- the YAML metadata required by the content model.

Any adaptation needed by the preview must be deterministic and documented. Do not edit the canonical chapter files merely to satisfy the candidate framework.

### 4.2 Diagram

Prefer build-time SVG generation for the test rather than relying initially on client-side rendering. This avoids making diagram comprehension dependent on JavaScript executing after page load and permits inspection of the generated SVG and its accessible labelling.

A candidate implementation may use the current Astro Markdown processor ecosystem with a Mermaid-to-SVG build plugin. Pele is one candidate renderer; it must be tested for compatibility with the actual Mermaid syntax in both canonical sources before adoption.

The generated SVG is a derived preview artefact. The two canonical `.mmd` files remain the editable source assets.

### 4.3 Desktop and mobile orientation

The canonical diagram sources currently specify a left-to-right layout. A single fixed Mermaid layout does not automatically reflow into a top-to-bottom graph when the viewport narrows.

The preview should test two renderings derived from each canonical language source:
- left-to-right for desktop;
- top-to-bottom for narrow/mobile viewports.

The mobile variant must be generated mechanically from the same source by changing only the flow direction, not maintained as a separate manually edited diagram. Both variants must preserve node IDs, labels, edges, symbols and semantic relationships. If this cannot be achieved reliably, retain the canonical layout and document the resulting mobile legibility limitation rather than silently changing the conceptual model.

Captions and alternative text must describe the diagram accurately and must not imply that the mobile rendering is a different analytical model.

## 5. Minimum preview acceptance tests

1. Build the Spanish Chapter 3 page from the canonical source.
2. Build the English counterpart from the canonical source.
3. Render mathematical notation correctly in both languages.
4. Render TV-DIA-001 in both languages.
5. Verify the generated desktop/mobile diagrams preserve equivalent node and edge structure.
6. Verify captions and alternative text are present and language-matched.
7. Verify language switching resolves to the actual counterpart.
8. Verify the chapter can be read at desktop and mobile viewport widths without unintended horizontal page scrolling.
9. Verify keyboard focus and operation of language and navigation controls.
10. Inspect diagram text size, clipping, contrast, line styles and readability at mobile width.
11. Confirm no draft content outside the bounded test is included.
12. Reproduce the build from a clean checkout using documented commands.

A build passing is not equivalent to a visual or accessibility test passing. Record each test separately with evidence and limitations.

## 6. Risks and controls

| Risk | Control |
|---|---|
| Framework-specific frontmatter schema rejects existing metadata | Use a permissive preview schema/adapter; preserve canonical metadata unchanged |
| Mathematical notation renders differently | Test inline and display equations against source expressions in both chapters |
| Mermaid renderer changes diagram semantics or fails on syntax | Compare node/edge structure and inspect SVG output for both languages |
| Mobile layout becomes unreadable | Generate a derived top-to-bottom layout and test at narrow widths |
| Two language versions drift | Generate both from the paired canonical source paths and compare structural invariants |
| Preview work leaks into production scope | Keep all implementation under the PoC workspace and follow architecture §22 |
| Build success is mistaken for acceptance | Maintain separate build, visual, responsive and accessibility results |

## 7. Decision status

No publishing framework is selected. No preview implementation or test has yet been executed by this record. The next implementation step is a minimal isolated Starlight candidate with build-time diagram rendering and math support, followed by reproducible build and browser-based tests.

## 8. External technical references consulted

- Starlight community integrations, including Mermaid options: https://starlight.astro.build/resources/plugins/
- Astro Markdown processing and plugin configuration: https://docs.astro.build/guides/markdown-content/
- Starlight client-side Mermaid plugin documentation and its stated trade-offs: https://pasqal-io.github.io/starlight-client-mermaid/getting-started/
- Build-time Mermaid-to-SVG approach using Pele with Starlight: https://hideoo.dev/notes/starlight-add-mermaid-diagrams-using-pele

These references inform the candidate approach; they do not establish compatibility with the TGCV sources. Compatibility must be tested in the PoC.
