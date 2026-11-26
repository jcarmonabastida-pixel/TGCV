import { cp, mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);
const here = dirname(fileURLToPath(import.meta.url));
const previewRoot = resolve(here, "..");
const repoRoot = resolve(previewRoot, "../../../..");
const contentRoot = resolve(repoRoot, "05_ASSETS/TRANSFORMATIONAL_VALUE");
const outputRoot = resolve(previewRoot, "src/content/docs");

const sources = [
  {
    lang: "es",
    chapter: "book/es/part-01-understanding-transformation/ch-03-espacio-de-transformaciones-accesibles.md",
    diagram: "assets/diagrams/TV-DIA-001/source/accessible-transformation-space-sequence.es.mmd"
  },
  {
    lang: "en",
    chapter: "book/en/part-01-understanding-transformation/ch-03-space-of-accessible-transformations.md",
    diagram: "assets/diagrams/TV-DIA-001/source/accessible-transformation-space-sequence.mmd"
  }
];

await mkdir(outputRoot, { recursive: true });

for (const item of sources) {
  const pageDir = resolve(outputRoot, item.lang);
  const assetDir = resolve(previewRoot, "public/diagrams", item.lang);
  await mkdir(pageDir, { recursive: true });
  await mkdir(assetDir, { recursive: true });

  const chapterSource = resolve(contentRoot, item.chapter);
  const chapterText = await readFile(chapterSource, "utf8");
  const diagramSource = resolve(contentRoot, item.diagram);
  const diagramText = await readFile(diagramSource, "utf8");

  const desktopSource = resolve(assetDir, "diagram-desktop.mmd");
  const mobileSource = resolve(assetDir, "diagram-mobile.mmd");
  const desktopSvg = resolve(assetDir, "diagram-desktop.svg");
  const mobileSvg = resolve(assetDir, "diagram-mobile.svg");

  await writeFile(desktopSource, diagramText, "utf8");
  const mobileText = diagramText.replace(/^flowchart\s+LR\s*$/m, "flowchart TB");
  if (mobileText === diagramText) {
    throw new Error(`Could not derive mobile direction for ${item.lang}; expected flowchart LR.`);
  }
  await writeFile(mobileSource, mobileText, "utf8");

  await execFileAsync("mmdc", ["-i", desktopSource, "-o", desktopSvg, "-b", "transparent"]);
  await execFileAsync("mmdc", ["-i", mobileSource, "-o", mobileSvg, "-b", "transparent"]);

  const figure = `
\n\n## TV-DIA-001\n\n<figure class="poc-diagram">\n  <picture>\n    <source media="(max-width: 700px)" srcset="/diagrams/${item.lang}/diagram-mobile.svg" />\n    <img src="/diagrams/${item.lang}/diagram-desktop.svg" alt="${item.lang === "es" ? "Diagrama del espacio de transformaciones accesibles; la descripción completa está disponible en el texto que acompaña al diagrama." : "Diagram of the accessible transformation space; the full description is provided in the accompanying text."}" />\n  </picture>\n  <figcaption>${item.lang === "es" ? "El espacio accesible se evalúa desde el estado del sistema y las condiciones relevantes; la realización es posible, no necesaria." : "The accessible space is evaluated from system state and relevant conditions; realisation is possible, not necessary."}</figcaption>\n</figure>\n`;

  const target = resolve(pageDir, "chapter-03.mdx");
  await writeFile(target, chapterText + figure, "utf8");
}

const landing = `---
title: "Transformational Value — Chapter 3 PoC"
---

# Transformational Value — Learning preview

This is a local, non-production technical preview for the Chapter 3 publishing PoC.

- [Español](/es/chapter-03/)
- [English](/en/chapter-03/)

The preview is generated from the canonical Markdown and Mermaid sources. Generated pages and diagrams are disposable build artefacts; do not edit them directly.
`;
await writeFile(resolve(outputRoot, "index.mdx"), landing, "utf8");
console.log("Prepared bilingual Chapter 3 preview content and responsive diagram variants.");
