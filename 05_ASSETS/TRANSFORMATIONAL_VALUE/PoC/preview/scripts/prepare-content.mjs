import { mkdir, readFile, writeFile } from "node:fs/promises";
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
  const canonicalChapterText = await readFile(chapterSource, "utf8");
  // Mark the generated preview page as a Starlight draft; preserve canonical status metadata.
  const chapterText = canonicalChapterText.replace(/^(---\r?\n[\s\S]*?\nstatus:\s*draft\s*\n)/, "$1draft: true\n");
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

  const alt = item.lang === "es"
    ? "Diagrama con seis nodos de proceso o entrada: estado del sistema y condiciones relevantes iniciales; espacio de transformaciones accesibles; transformación realizada; estado sucesor del sistema; nuevas condiciones relevantes; y siguiente espacio de transformaciones accesibles. Una flecha continua conecta el estado inicial con la evaluación del espacio accesible. Una flecha discontinua indica que una transformación accesible puede realizarse o no. Si se realiza, conduce al estado sucesor. El siguiente espacio se evalúa a partir del estado sucesor y, de forma independiente, de las nuevas condiciones relevantes. Una conexión no direccional y etiquetada vincula el espacio accesible con una nota que distingue accesibilidad, realización, trayectoria, resultado y valor. Las flechas representan relaciones analíticas, no una ley causal universal."
    : "A diagram with six process or input nodes: initial system state and relevant conditions; accessible transformation space; realised transformation; successor system state; next relevant conditions; and next accessible transformation space. A solid arrow connects the initial state to the evaluation of the accessible space. A dashed arrow indicates that an accessible transformation may or may not be realised. If realised, it leads to the successor state. The next space is evaluated from the successor state and, independently, from the next relevant conditions. A non-directional labelled connector links the accessible space to a note distinguishing accessibility, realisation, trajectory, outcome and value. The arrows represent analytical relationships, not a universal causal law.";
  const caption = item.lang === "es"
    ? "El espacio de transformaciones accesibles se evalúa a partir del estado del sistema y de las condiciones relevantes. Una transformación accesible puede realizarse o no; si se realiza, conduce a un estado sucesor. El siguiente espacio accesible se evalúa considerando tanto ese estado como las nuevas condiciones relevantes."
    : "The accessible transformation space is evaluated from the system state and relevant conditions. An accessible transformation may or may not be realised; if it is, it leads to a successor state. The next accessible space is evaluated from both that state and the next relevant conditions.";
  const figure = `
\n\n<figure class="poc-diagram">\n  <picture>\n    <source media="(max-width: 700px)" srcset="/diagrams/${item.lang}/diagram-mobile.svg" />\n    <img src="/diagrams/${item.lang}/diagram-desktop.svg" alt="${alt}" />\n  </picture>\n  <figcaption>${caption}</figcaption>\n</figure>\n`;

  const target = resolve(pageDir, "chapter-03.md");
  await writeFile(target, chapterText + figure, "utf8");
}

for (const item of sources) {
  const title = item.lang === "es" ? "Vista previa de aprendizaje" : "Learning preview";
  const linkLabel = item.lang === "es" ? "Abrir el capítulo 3" : "Open Chapter 3";
  const landing = `---
title: "${title}"
---

# Transformational Value — Chapter 3 PoC

This is a local, non-production technical preview for the bilingual Chapter 3 publishing PoC.

[${linkLabel}](./chapter-03/)
`;
  await writeFile(resolve(outputRoot, item.lang, "index.md"), landing, "utf8");
}
console.log("Prepared paired bilingual Chapter 3 pages and responsive diagram variants.");
