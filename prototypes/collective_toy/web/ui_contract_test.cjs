const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
(async () => {
  const htmlPath = path.resolve(__dirname, "index.html");
  const source = fs.readFileSync(htmlPath, "utf8");
  assert.doesNotMatch(source, /id="profile-editor"|id="guarded-transition"|id="required-transition"|id="add-relation"|id="relation-list"/);
  assert.match(source, /temporal_prerequisite_graph v1/);
  const browser = await chromium.launch({headless:true});
  try {
    const page = await browser.newPage();
    await page.goto("file://" + htmlPath);
    const notice = await page.locator(".notice").innerText();
    assert.match(notice, /datos sintéticos/i);
    assert.match(notice, /No es una validación científica/i);
    const initial = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(initial.rule_profile,{type:"temporal_prerequisite_graph",version:"1"});
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const pkg = await page.evaluate(() => window.lastPackage);
    assert.ok(pkg && pkg.input && pkg.result);
    assert.equal(pkg.result.validation,"PASS");
    assert.equal(pkg.input.rule_profile.type,"temporal_prerequisite_graph");
    assert.ok(await page.locator("#trajectory-scenario").count());
    assert.ok(await page.locator("#sequence-select").count());
    assert.ok(await page.locator("#execute-sequence").count());
    assert.ok(await page.locator("#package-assessment").count());
    assert.ok(await page.locator("#outcome-status").count());
    assert.ok(await page.locator("#value-status").count());
  } finally { await browser.close(); }
  process.stdout.write("PASS: grouped Full Chain UI contract\n");
})().catch(error => { console.error(error); process.exit(1); });
