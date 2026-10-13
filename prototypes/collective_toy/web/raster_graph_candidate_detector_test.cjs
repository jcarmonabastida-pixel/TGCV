"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");
const fs = require("node:fs");
const { chromium } = require("playwright");

(async () => {
  const root = path.join(__dirname, "fixtures", "ocr_graph_images");
  const tempRoot = path.join(require("node:os").tmpdir(), "tgcv-colored-node-fixtures");
  fs.mkdirSync(tempRoot, { recursive: true });
  const colorVariants = [
    { name: "SYN-LINEAR-001.png", boxes: [[35,75,65,105],[145,75,175,105],[255,75,285,105]] },
    { name: "SYN-BRANCH-001.png", boxes: [[35,75,65,105],[145,30,175,60],[145,120,175,150],[255,75,285,105]] },
    { name: "SYN-CROSSING-001.png", boxes: [[35,30,65,60],[255,120,285,150],[35,120,65,150],[255,30,285,60]] }
  ];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const fixture of colorVariants) {
      const source = fs.readFileSync(path.join(root, "images", fixture.name));
      const dataUrl = "data:image/png;base64," + source.toString("base64");
      const coloredPng = await browser.newPage().then(async page => {
        const result = await page.evaluate(async ({ dataUrl, boxes }) => {
          const img = new Image(); img.src = dataUrl; await img.decode();
          const canvas = document.createElement("canvas"); canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
          const ctx = canvas.getContext("2d"); ctx.drawImage(img, 0, 0);
          const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const palette = [[205,232,255],[218,245,218],[255,235,190],[235,218,255]];
          boxes.forEach((box, index) => {
            const color = palette[index % palette.length];
            for (let y = box[1] + 2; y < box[3] - 1; y++) for (let x = box[0] + 2; x < box[2] - 1; x++) {
              const i = (y * canvas.width + x) * 4;
              if (pixels.data[i] > 210 && pixels.data[i+1] > 210 && pixels.data[i+2] > 210) {
                pixels.data[i] = color[0]; pixels.data[i+1] = color[1]; pixels.data[i+2] = color[2];
              }
            }
          });
          ctx.putImageData(pixels, 0, 0);
          return canvas.toDataURL("image/png").split(",")[1];
        }, { dataUrl, boxes: fixture.boxes });
        await page.close();
        return Buffer.from(result, "base64");
      });
      fs.writeFileSync(path.join(tempRoot, fixture.name), coloredPng);
    }
  } finally { await browser.close(); }
  for (const name of ["SYN-LINEAR-001.png", "SYN-BRANCH-001.png", "SYN-CROSSING-001.png"]) {
    const result = await detectGraphCandidates(path.join(root, "images", name));
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.equal(result.image.width, 320);
    assert.equal(result.image.height, 180);
    assert.ok(Array.isArray(result.nodes));
    assert.ok(Array.isArray(result.edge_candidates));
    if (result.nodes.length === 0) process.stderr.write(name + " diagnostics: " + JSON.stringify(result.diagnostics) + "\\n");
    assert.ok(result.nodes.length > 0, name + ": detector must find at least one provisional node box");
    assert.ok(result.limitations.length >= 3);
    assert.ok(result.nodes.every(n => n.review_required === true));
    process.stdout.write(name + ": " + result.nodes.length + " provisional node candidates; " +
      result.edge_candidates.length + " horizontal stroke candidates.\n");
  }
  for (const fixture of colorVariants) {
    const coloredPath = path.join(tempRoot, fixture.name);
    const result = await detectGraphCandidates(coloredPath);
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.ok(result.nodes.length > 0, fixture.name + ": colored-node variant must yield provisional candidates");
    assert.ok(result.nodes.every(n => n.review_required === true));
    process.stdout.write(fixture.name + ": " + result.nodes.length + " provisional candidates on colored-node variant.\\n");
  }
  process.stdout.write("PASS: detector executes on baseline and colored-node raster fixtures; candidates remain provisional.\\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
