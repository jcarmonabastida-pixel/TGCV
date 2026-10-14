const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

(async () => {
  const root = __dirname;
  const outputDir = process.env.TGCV_PADDLEOCR_FIXTURE_DIR || path.join(root, "paddleocr-fixtures");
  fs.mkdirSync(outputDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1400, height: 1200 } });
    await page.goto("file://" + path.join(root, "ocr_quality_evaluation.html"), { waitUntil: "load" });
    await page.getByRole("button", { name: "Generar imágenes de referencia" }).click();
    await page.waitForFunction(() => document.querySelectorAll("#fixtures canvas").length === 5);
    const canvases = page.locator("#fixtures canvas");
    const expected = [
      { id: "OCR-TXT-001", lines: ["Estado A", "Estado B", "Transición"] },
      { id: "OCR-TXT-002", lines: ["A", "B", "C", "Inicio: A"] },
      { id: "OCR-TXT-003", lines: ["Estado inicial", "Estado final", "Condición: x > 0"] },
      { id: "OCR-TXT-004", lines: ["Nodo_01", "Nodo-02", "T1: A -> B"] },
      { id: "OCR-TXT-005", lines: ["Sistema adaptable", "Transformación accesible", "Relación causal?"] }
    ];
    for (let i = 0; i < expected.length; i++) {
      await canvases.nth(i).screenshot({ path: path.join(outputDir, expected[i].id + ".png") });
    }
    fs.writeFileSync(path.join(outputDir, "expected.json"), JSON.stringify(expected, null, 2) + "\n");
    console.log(JSON.stringify({ status: "fixtures-exported", count: expected.length, outputDir }));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
