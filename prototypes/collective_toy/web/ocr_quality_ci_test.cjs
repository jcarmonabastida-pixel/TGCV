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
      return status && /Métricas verificadas: 8\/8/.test(status.textContent);
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
    assert.equal(report.results.length, 5, "All five reference fixtures must be measured");
    assert.equal(report.metric_validation.passed, report.metric_validation.total, "CER/WER self-checks must all pass");
    for (const row of report.results) {
      assert.match(row.fixture_sha256, /^[a-f0-9]{64}$/);
      assert.ok(Number.isFinite(row.cer) && Number.isFinite(row.wer));
      assert.ok(Number.isFinite(row.first_call_elapsed_ms));
      assert.equal(row.warm_elapsed_ms_samples.length, 3);
    }
    const reportPath = path.join(outputDir, "tgcv-ocr-quality-result.json");
    fs.writeFileSync(reportPath, JSON.stringify(report, null, 2) + "\n", "utf8");
    console.log(JSON.stringify({ status, reportPath, mean_cer: report.mean_cer, mean_wer: report.mean_wer, gate_pass: report.gate_pass, cases: report.results.map(({ id, cer, wer, first_call_elapsed_ms, warm_elapsed_ms_mean, identifier_exact }) => ({ id, cer, wer, first_call_elapsed_ms, warm_elapsed_ms_mean, identifier_exact })) }, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
