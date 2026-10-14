const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");

(async () => {
  const htmlPath = path.resolve(__dirname, "ocr_quality_evaluation.html");
  const outputDir = process.env.TGCV_OCR_OUTPUT_DIR || path.resolve(__dirname, "ocr-quality-output");
  fs.mkdirSync(outputDir, { recursive: true });
  assert.ok(fs.existsSync(htmlPath), "OCR quality evaluator must exist");

  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ acceptDownloads: true });
    page.setDefaultTimeout(120000);
    const pageErrors = [];
    page.on("pageerror", error => pageErrors.push(error.message));
    await page.goto("file://" + htmlPath, { waitUntil: "load" });

    await page.waitForFunction(() => {
      const status = document.querySelector("#status");
      return status && /Métricas verificadas: 9\/9/.test(status.textContent);
    }, null, { timeout: 15000 });

    await page.getByRole("button", { name: "Ejecutar OCR real" }).click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#status");
      return status && /OCR real completado|Evaluación fallida:/.test(status.textContent);
    }, null, { timeout: 240000 });

    const status = await page.locator("#status").innerText();
    assert.match(status, /OCR real completado/, "Real OCR evaluation must complete; status was: " + status);
    assert.equal(pageErrors.length, 0, "Browser page errors: " + pageErrors.join(" | "));

    const report = await page.evaluate(() => window.__tgcvOcrReport);
    assert.ok(report, "Evaluation report must exist");
    assert.equal(report.results.length, 10, "All five baseline and five adversarial graph-text fixtures must be measured");
    assert.deepEqual(report.results.filter(row => row.id.startsWith("OCR-GRAPH-")).map(row => row.id).sort(), ["OCR-GRAPH-006", "OCR-GRAPH-007", "OCR-GRAPH-008", "OCR-GRAPH-009", "OCR-GRAPH-010"], "All adversarial graph-text fixtures must be included");
    assert.equal(report.metric_validation.passed, report.metric_validation.total, "CER/WER self-checks must all pass");
    assert.equal(report.segmentation_diagnostics.length, 2, "Both diagnostic segmentation modes must be recorded");
    assert.equal(report.preprocessing_diagnostics.length, 3, "All three OCR-TXT-004 preprocessing variants must be recorded");
    assert.ok(Array.isArray(report.character_case_preprocessing_diagnostics), "Targeted-character preprocessing comparisons must be recorded");
    assert.equal(report.character_case_preprocessing_diagnostics.length, 6, "Both character-confusion fixtures must be compared across three preprocessing variants");
    assert.deepEqual(report.character_case_preprocessing_diagnostics.map(x => x.id + ":" + x.variant).sort(), [
      "OCR-TXT-002:grayscale_contrast", "OCR-TXT-002:original", "OCR-TXT-002:upscale_2x",
      "OCR-TXT-003:grayscale_contrast", "OCR-TXT-003:original", "OCR-TXT-003:upscale_2x"
    ]);
    for (const diagnostic of report.character_case_preprocessing_diagnostics) {
      assert.ok(Number.isFinite(diagnostic.cer) && Number.isFinite(diagnostic.wer));
      assert.ok(Number.isFinite(diagnostic.elapsed_ms));
      assert.match(diagnostic.scope, /no sustituye el OCR primario ni modifica la puerta de calidad/);
    }
    assert.ok(report.notation_spacing_diagnostic, "Transition-notation spacing diagnostic must be recorded");
    assert.ok(Array.isArray(report.targeted_character_diagnostics), "Targeted character-confusion diagnostics must be recorded");
    assert.equal(report.targeted_character_diagnostics.length, 2, "Both targeted character-confusion diagnostics must be recorded");
    const cConfusion = report.targeted_character_diagnostics.find(x => x.id === "OCR-TXT-002");
    const zeroConfusion = report.targeted_character_diagnostics.find(x => x.id === "OCR-TXT-003");
    assert.ok(cConfusion && cConfusion.confusion === "C_vs_Cc", "C/Cc diagnostic must be tied to OCR-TXT-002");
    assert.ok(zeroConfusion && zeroConfusion.confusion === "zero_vs_letter_O", "0/O diagnostic must be tied to OCR-TXT-003");
    assert.ok(Number.isInteger(cConfusion.c_exact_occurrences) && Number.isInteger(cConfusion.cc_exact_occurrences));
    assert.ok(Number.isInteger(zeroConfusion.zero_occurrences) && Number.isInteger(zeroConfusion.capital_o_occurrences));
    assert.match(cConfusion.scope, /no normaliza ni altera CER\/WER primarios o el gate/);
    assert.match(zeroConfusion.scope, /no normaliza ni altera CER\/WER primarios o el gate/);

    assert.equal(report.notation_spacing_diagnostic.id, "OCR-TXT-004");
    assert.ok(Number.isFinite(report.notation_spacing_diagnostic.cer) && Number.isFinite(report.notation_spacing_diagnostic.wer));
    assert.equal(report.notation_spacing_diagnostic.expected_spacing_canonical, "Nodo_01\nNodo-02\nT1: A -> B");
    assert.equal(report.gate_pass, report.mean_cer <= 0.05 && report.mean_wer <= 0.10 && report.results.every(row => row.identifier_exact), "Diagnostic normalization must not alter the primary quality gate");
    assert.deepEqual(report.preprocessing_diagnostics.map(x => x.variant).sort(), ["grayscale_contrast", "original", "upscale_2x"]);
    for (const diagnostic of report.preprocessing_diagnostics) {
      assert.equal(diagnostic.id, "OCR-TXT-004");
      assert.ok(Number.isFinite(diagnostic.cer) && Number.isFinite(diagnostic.wer));
      assert.ok(Number.isFinite(diagnostic.elapsed_ms));
    }
    assert.deepEqual(report.segmentation_diagnostics.map(x => x.mode).sort(), ["single_block", "sparse_text"]);
    for (const diagnostic of report.segmentation_diagnostics) {
      assert.equal(diagnostic.id, "OCR-TXT-004");
      assert.ok(Number.isFinite(diagnostic.cer) && Number.isFinite(diagnostic.wer));
      assert.ok(Number.isFinite(diagnostic.elapsed_ms));
    }
    for (const row of report.results) {
      assert.match(row.fixture_sha256, /^[a-f0-9]{64}$/);
      assert.ok(Number.isFinite(row.cer) && Number.isFinite(row.wer));
      assert.ok(Number.isFinite(row.first_call_elapsed_ms));
      assert.equal(row.warm_elapsed_ms_samples.length, 3);
    }
    const reportPath = path.join(outputDir, "tgcv-ocr-quality-result.json");
    fs.writeFileSync(reportPath, JSON.stringify(report, null, 2) + "\n", "utf8");
    console.log(JSON.stringify({ status, reportPath, mean_cer: report.mean_cer, mean_wer: report.mean_wer, gate_pass: report.gate_pass, cases: report.results.map(({ id, cer, wer, first_call_elapsed_ms, warm_elapsed_ms_mean, identifier_exact }) => ({ id, cer, wer, first_call_elapsed_ms, warm_elapsed_ms_mean, identifier_exact })), diagnostics: { notation_spacing: report.notation_spacing_diagnostic, segmentation: report.segmentation_diagnostics, preprocessing: report.preprocessing_diagnostics, targeted_characters: report.targeted_character_diagnostics } }, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
