"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");

(async () => {
  const root = path.join(__dirname, "fixtures", "ocr_graph_images");
  for (const name of ["SYN-LINEAR-001.png", "SYN-BRANCH-001.png", "SYN-CROSSING-001.png"]) {
    const result = await detectGraphCandidates(path.join(root, "images", name));
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.equal(result.image.width, 320);
    assert.equal(result.image.height, 180);
    assert.ok(Array.isArray(result.nodes));
    assert.ok(Array.isArray(result.edge_candidates));
    assert.ok(result.limitations.length >= 3);
    assert.ok(result.nodes.every(n => n.review_required === true));
    process.stdout.write(name + ": " + result.nodes.length + " provisional node candidates; " +
      result.edge_candidates.length + " horizontal stroke candidates.\n");
  }
  process.stdout.write("PASS: detector executes on all three raster fixtures and returns provisional candidates only.\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
