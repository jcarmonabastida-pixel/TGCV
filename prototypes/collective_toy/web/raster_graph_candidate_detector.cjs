"use strict";

/**
 * First deterministic raster candidate detector for TGCV development fixtures.
 * Uses browser Canvas to inspect pixels. It is a candidate generator, not a
 * production-grade graph parser; OCR labels are intentionally ignored.
 */
async function detectGraphCandidates(imagePath, options = {}) {
  const { chromium } = require("playwright");
  const fs = require("node:fs");
  const path = require("node:path");
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    const absolute = path.resolve(imagePath);
    const url = "file://" + absolute.replace(/\\/g, "/");
    return await page.evaluate(async ({ url, threshold, minNodeSize, maxNodeSize }) => {
      const image = new Image();
      image.src = url;
      await image.decode();
      const canvas = document.createElement("canvas");
      canvas.width = image.naturalWidth;
      canvas.height = image.naturalHeight;
      const ctx = canvas.getContext("2d", { willReadFrequently: true });
      ctx.drawImage(image, 0, 0);
      const { data, width, height } = ctx.getImageData(0, 0, canvas.width, canvas.height);
      const dark = new Uint8Array(width * height);
      for (let i = 0; i < width * height; i++) {
        const r = data[i * 4], g = data[i * 4 + 1], b = data[i * 4 + 2];
        if ((r + g + b) / 3 < threshold) dark[i] = 1;
      }

      // Find closed rectangular/elliptical outline candidates by horizontal
      // and vertical dark-pixel runs. This avoids treating every line crossing
      // as a node; candidates are provisional and still require review.
      const runs = [];
      for (let y = 2; y < height - 2; y++) {
        let start = -1;
        for (let x = 0; x <= width; x++) {
          const on = x < width && dark[y * width + x] === 1;
          if (on && start < 0) start = x;
          if ((!on || x === width) && start >= 0) {
            const len = x - start;
            if (len >= minNodeSize && len <= maxNodeSize) runs.push({ y, x1: start, x2: x - 1, len });
            start = -1;
          }
        }
      }
      const groups = [];
      for (const run of runs) {
        let group = groups.find(g => Math.abs(g.y - run.y) <= 2 &&
          Math.abs(g.x1 - run.x1) <= 3 && Math.abs(g.x2 - run.x2) <= 3);
        if (!group) { group = { rows: [], x1: run.x1, x2: run.x2, y: run.y }; groups.push(group); }
        group.rows.push(run.y);
        group.x1 = Math.min(group.x1, run.x1);
        group.x2 = Math.max(group.x2, run.x2);
      }
      const candidates = [];
      for (const g of groups) {
        if (g.rows.length < 3) continue;
        const y1 = Math.min(...g.rows), y2 = Math.max(...g.rows);
        const w = g.x2 - g.x1 + 1, h = y2 - y1 + 1;
        if (h < minNodeSize || h > maxNodeSize || w < minNodeSize || w > maxNodeSize) continue;
        const cx = Math.round((g.x1 + g.x2) / 2), cy = Math.round((y1 + y2) / 2);
        if (candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) continue;
        candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
          bbox: [g.x1, y1, g.x2, y2], confidence: "low", review_required: true });
      }

      // Report straight-line candidates using long horizontal/vertical runs.
      // Diagonal runs and arrowheads remain explicitly unclassified in v0.1.
      const lineCandidates = [];
      for (let y = 0; y < height; y++) {
        let start = -1;
        for (let x = 0; x <= width; x++) {
          const on = x < width && dark[y * width + x] === 1;
          if (on && start < 0) start = x;
          if ((!on || x === width) && start >= 0) {
            if (x - start >= 24) lineCandidates.push({ orientation: "horizontal", from: [start, y], to: [x - 1, y] });
            start = -1;
          }
        }
      }
      return {
        detector: "TGCV-RASTER-GRAPH-CANDIDATES-001",
        status: "experimental-candidates-only",
        image: { width, height },
        method: "Canvas grayscale threshold; horizontal-run node-outline candidates; long horizontal stroke candidates",
        nodes: candidates,
        edge_candidates: lineCandidates,
        limitations: [
          "Not a complete node detector: connected outlines may be fragmented or merged.",
          "Diagonal edges, arrowhead direction, edge-to-node attachment and crossing topology are not yet inferred.",
          "Text can generate false geometric candidates; OCR semantics are not used.",
          "All candidates require visual review."
        ]
      };
    }, {
      url,
      threshold: options.threshold ?? 100,
      minNodeSize: options.minNodeSize ?? 18,
      maxNodeSize: options.maxNodeSize ?? 50
    });
  } finally {
    await browser.close();
  }
}

module.exports = { detectGraphCandidates };
