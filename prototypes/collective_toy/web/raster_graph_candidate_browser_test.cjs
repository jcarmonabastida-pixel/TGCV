"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.setContent("<!doctype html><html><body></body></html>");
    await page.addScriptTag({
      path: path.join(__dirname, "raster_graph_candidate_browser.js")
    });
    const result = await page.evaluate(async () => {
      const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="32" height="32" fill="white"/></svg>';
      const source = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
      return globalThis.TGCVRasterGraphCandidateDetector.detectGraphCandidatesFromImage(source);
    });
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.deepEqual(result.nodes, []);
    assert.deepEqual(result.edge_candidates, []);
    assert.ok(result.limitations.some((item) => item.includes("visual review")));
    process.stdout.write("CANVAS-BROWSER-ENTRY-001: native browser Canvas entry point and candidate contract passed.\n");
  } finally {
    await browser.close();
  }
})().catch((error) => {
  process.stderr.write(String(error && error.stack || error) + "\n");
  process.exitCode = 1;
});
