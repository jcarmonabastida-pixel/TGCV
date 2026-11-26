# Learning Publishing PoC — preview implementation record

**Record ID:** TV-POC-IMPL-001  
**Date:** 2026-11-26  
**Status:** Initial scaffold committed; runtime verification blocked  
**Branch:** `strategy/transformational-value-learning`  
**Scope:** Chapter 3 bilingual preview and TV-DIA-001 only

## 1. Implementation created

An isolated candidate project now exists at `05_ASSETS/TRANSFORMATIONAL_VALUE/PoC/preview/`.

Files committed:

- `package.json` — Astro, Starlight, Mermaid CLI and math-rendering dependencies; local dev/build commands.
- `astro.config.mjs` — Starlight multilingual configuration with Spanish as default, English as the second locale, and KaTeX processing.
- `src/content.config.ts` — extends Starlight's documentation schema while preserving additional canonical TGCV metadata.
- `src/styles/katex.css` — KaTeX stylesheet and responsive diagram presentation.
- `scripts/prepare-content.mjs` — reads the two canonical Chapter 3 Markdown files and the two canonical Mermaid sources, generates paired locale pages, derives a mobile top-to-bottom Mermaid variant from each desktop source, and renders SVGs through Mermaid CLI.
- `.gitignore` — excludes dependencies, generated pages, SVGs and build output.
- `README.md` — local setup, scope, limitations and test instructions.

The generated chapter pages preserve the canonical editorial metadata and map `status: draft` to Starlight's `draft: true`, so the chapter can be examined in the development server but is excluded from a production build. Generated pages and diagram exports are disposable and must not be edited or committed.

The Spanish and English pages use matching relative page names to enable Starlight's built-in language pairing.

## 2. Scope controls

- No changes were made to the canonical Chapter 3 text or Mermaid source files.
- No changes were made to `main`.
- No domain, hosting, public preview or paid service was created.
- No production framework decision was made.
- The prototype is isolated from `collective_toy` and other projects.

## 3. Static review completed

The committed files were re-read from GitHub after creation. The following configuration choices were checked against current Starlight documentation:

- Multilingual routes are organised by locale directory, and matching filenames associate language counterparts.
- Additional canonical metadata can be retained by extending Starlight's docs schema.
- The draft flag excludes draft pages from production output.

References:
- https://starlight.astro.build/es/guides/i18n/
- https://starlight.astro.build/es/reference/frontmatter/

This is a static configuration review only. It is not evidence that the project installs or builds successfully.

## 3.1 Follow-up static configuration review

After GitHub access was restored, the candidate configuration was checked against the current official Starlight documentation:

- The configured `defaultLocale: "es"` is valid because `es` is a key in the `locales` object.
- Locale directories are expected under the docs content root.
- Starlight associates translated pages using the same relative filename in each locale directory, matching the generated `es/chapter-03.md` and `en/chapter-03.md` pages.

Official references:
- https://starlight.astro.build/reference/configuration/
- https://starlight.astro.build/guides/i18n/

This resolves the static concern about the locale key and page pairing. It does not prove that the configured project builds or that the language selector behaves correctly at runtime.

## 4. Runtime verification status

**Not executed.**

An attempt to clone the repository into the available temporary execution environment failed because that environment could not resolve `github.com`. Consequently, no dependency installation, Node syntax check, Mermaid render, Astro build, browser session or accessibility test was run.

Do not mark any PoC test as passed on the basis of the scaffold or static review.

## 5. Next verification sequence

Run from the `05_ASSETS/TRANSFORMATIONAL_VALUE/PoC/preview` directory in an environment with repository access:

1. `npm install`
2. `npm run dev` — inspect Spanish and English Chapter 3 routes, language switching, math and diagrams.
3. `npm run build` — confirm the production output excludes the draft chapter pages.
4. Inspect the generated SVGs and compare desktop/mobile node IDs, labels, symbols and edge structure.
5. Test keyboard operation, focus visibility, semantic headings, image alternative text, contrast, clipping and mobile layout at representative viewport widths.
6. Record command output, versions, browser/viewport, screenshots or other evidence, defects and test outcomes.

The first run may reveal dependency, schema, Markdown or Mermaid compatibility issues. Resolve those in this isolated PoC without changing the canonical chapter or diagram sources unless a separate editorial decision authorises such a change.

## 6. Current decision

The candidate scaffold is committed, but Gate 2 visual/accessibility validation remains **open**. The project is not ready to accept the PoC or select a publishing framework.
