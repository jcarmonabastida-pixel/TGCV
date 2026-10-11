const { chromium } = require("playwright");
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const os = require("node:os");
const assert = require("node:assert/strict");

(async () => {
  const root = path.resolve(__dirname, "../..");
  const htmlPath = path.join(root, "prototypes/collective_toy/web/index.html");
  const engineDir = path.join(root, "prototypes/collective_toy");
  const python = spawnSync("python", ["-c",
    "import json; from collective_toy_engine_001 import demo_model, run_model; print(json.dumps(run_model(demo_model()), sort_keys=True))"
  ], { cwd: engineDir, encoding: "utf8" });
  assert.equal(python.status, 0, "Python reference engine must run: " + python.stderr);
  const pyResult = JSON.parse(python.stdout.trim());

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ acceptDownloads: true });
  try {
    await page.goto("file://" + htmlPath);
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.getByText(/Ejecución completada/).waitFor({ timeout: 5000 });
    const status = await page.locator("#status").innerText();
    assert.match(status, /Ejecución completada/);

    const [download] = await Promise.all([
      page.waitForEvent("download"),
      page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click()
    ]);
    const outputPath = path.join(os.tmpdir(), "collective-toy-browser-" + process.pid + ".json");
    await download.saveAs(outputPath);
    const browserPackage = JSON.parse(fs.readFileSync(outputPath, "utf8"));
    fs.unlinkSync(outputPath);

    assert.deepEqual(
      browserPackage.result.scenario_results,
      pyResult.scenario_results,
      "Browser and Python scenario results must match exactly"
    );
    assert.deepEqual(
      browserPackage.result.comparisons_to_baseline,
      pyResult.comparisons_to_baseline,
      "Browser and Python intervention comparisons must match exactly"
    );
    assert.equal(browserPackage.result.input_sha256, pyResult.input_sha256,
      "Input content hash must match across runtimes");
    assert.equal(browserPackage.result.result_sha256, pyResult.result_sha256,
      "Result content hash must match across runtimes");
    console.log("PASS: browser and Python scenario outputs, comparisons, and hashes match.");
  } finally {
    await browser.close();
  }
})().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
