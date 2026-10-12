const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");

(async () => {
  const htmlPath = path.resolve(__dirname, "index.html");
  assert.ok(fs.existsSync(htmlPath), "Collective Toy UI must exist");

  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto("file://" + htmlPath);

    // Keep the MVP's state-local graph semantics and non-scientific boundary visible.
    const notice = await page.locator(".notice").innerText();
    assert.match(notice, /grafo finito/i);
    assert.match(notice, /No procesa datos reales/i);
    assert.match(notice, /No es una validación científica/i);
    assert.match(notice, /no implementa por sí solo Tacc de TGCV/i);

    // Output labels must not silently promote graph-local results to system-level TGCV claims.
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.getByText("Estados alcanzables en baseline", { exact: true }).waitFor();
    await page.getByText("Trayectorias enumeradas", { exact: true }).first().waitFor();
    await page.getByText("Límite alcanzado", { exact: true }).waitFor();
    await page.getByText("Escenario: baseline", { exact: true }).waitFor();

    const packageData = await page.evaluate(() => window.lastPackage);
    assert.ok(packageData, "A successful run must produce an inspectable package");
    assert.equal(
      packageData.result.scientific_interpretation,
      "NONE: synthetic model execution only; no empirical or TGCV validity claim."
    );
    assert.equal(packageData.input.rule_profile.type, "finite_deterministic_graph");

    // Profile 1 is the default; selecting profile 2 then returning to profile 1
    // must preserve the relation as metadata without silently retaining an operative profile.
    assert.equal(await page.locator("#profile-editor").inputValue(), "1");
    await page.locator("#profile-editor").selectOption("2");
    await page.locator("#profile-editor").selectOption("1");
    const model = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(model.rule_profile, { type: "finite_deterministic_graph", version: "1" });
    assert.match(await page.locator("#relation-help").innerText(), /metadatos inertes|perfil 2/i);

    console.log("PASS: UI terminology, synthetic-only caveat, output labels, package boundary, and profile default.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
