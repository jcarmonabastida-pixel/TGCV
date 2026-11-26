# Local Learning preview prototype

**Status:** Initial scaffold; not yet executed or validated.  
**Purpose:** Isolated, non-production experiment for the Chapter 3 bilingual publishing PoC.  
**Candidate:** Astro + Starlight. This is not a production framework decision.

## Requirements

- Node.js 20.19+ or 22.12+
- npm
- Chromium available to Mermaid CLI / Puppeteer (the Mermaid CLI may download a compatible browser on first use)

## Run locally

From this directory:

```bash
npm install
npm run dev
```

For a production-mode local build:

```bash
npm run build
npm run preview
```

The preview is local. Do not deploy it or publish its output. The generator maps the canonical `status: draft` metadata to Starlight `draft: true`; chapter pages should be available in development and excluded from production output.

## Source-of-truth behaviour

`scripts/prepare-content.mjs` reads the canonical Spanish and English Chapter 3 Markdown files and the paired TV-DIA-001 Mermaid sources from the repository. It creates generated Starlight pages under `src/content/docs/` and SVG diagram exports under `public/diagrams/`.

Generated files are disposable. Do not edit them manually and do not commit generated output. The Mermaid desktop source is preserved; the mobile variant is derived by changing only the flow direction from LR to TB. The generated SVGs must be inspected to confirm that the graph structure and labels remain intact.

The chapter content is copied without editorial rewriting. The generated preview adds a responsive diagram figure with a language-paired caption and a direction-neutral alternative text. Confirm its placement and verify that the wording matches the canonical diagram README.

## Current limitations

- No dependency installation, build, browser rendering or accessibility test has yet been run.
- A Starlight content schema extension preserves additional canonical TGCV metadata in generated pages; the actual metadata parse still needs a successful build to verify it.
- KaTeX rendering is configured through `remark-math` and `rehype-katex`, but inline and display equations have not yet been verified in a browser.
- The two locale pages use the same relative page slug so Starlight can pair them. Verify the language selector and route behaviour in a browser.
- SVG accessibility, diagram legibility, keyboard navigation, contrast and mobile layout remain unverified.

## Test record

Record actual command, runtime versions, exit status, browser/viewport, observations and defects in the PoC validation workspace. A successful build alone does not pass visual or accessibility criteria.
