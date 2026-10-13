"use strict";

/**
 * First deterministic raster candidate detector for TGCV development fixtures.
 * Uses browser Canvas to inspect pixels. It is a candidate generator, not a
 * production-grade graph parser; OCR labels are intentionally ignored.
 */
async function detectGraphCandidates(imagePath, options = {}) {
  const { chromium } = require("playwright");
  const fs = require("node:fs");
  const bytes = fs.readFileSync(imagePath);
  const imageDataUrl = "data:image/png;base64," + bytes.toString("base64");
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    return await page.evaluate(async ({ imageDataUrl, threshold, minNodeSize, maxNodeSize }) => {
      const image = new Image();
      image.src = imageDataUrl;
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
      // Pair top/bottom horizontal border runs with similar x extents.
      // This detects simple outlined node boxes without reading labels.
      const candidates = [];
      const usedBottom = new Set();
      for (let i = 0; i < runs.length; i++) {
        const top = runs[i];
        let best = -1;
        let bestScore = Infinity;
        for (let j = i + 1; j < runs.length; j++) {
          const bottom = runs[j];
          const dy = bottom.y - top.y;
          if (dy < minNodeSize - 2) continue;
          if (dy > maxNodeSize) break;
          if (usedBottom.has(j)) continue;
          const xError = Math.abs(top.x1 - bottom.x1) + Math.abs(top.x2 - bottom.x2);
          if (xError > 10) continue;
          const score = xError + Math.abs(top.len - bottom.len);
          if (score < bestScore) { best = j; bestScore = score; }
        }
        if (best < 0) continue;
        const bottom = runs[best];
        usedBottom.add(best);
        const x1 = Math.min(top.x1, bottom.x1);
        const x2 = Math.max(top.x2, bottom.x2);
        const y1 = top.y, y2 = bottom.y;
        const w = x2 - x1 + 1, h = y2 - y1 + 1;
        if (w < minNodeSize || w > maxNodeSize || h < minNodeSize || h > maxNodeSize) continue;
        const cx = Math.round((x1 + x2) / 2), cy = Math.round((y1 + y2) / 2);
        if (candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) continue;
        candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
          bbox: [x1, y1, x2, y2], confidence: "low", review_required: true });
      }

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
        method: "Canvas grayscale threshold; paired horizontal border runs for provisional box nodes; long horizontal stroke candidates",
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
      imageDataUrl,
      threshold: options.threshold ?? 100,
      minNodeSize: options.minNodeSize ?? 18,
      maxNodeSize: options.maxNodeSize ?? 50
    });
  } finally {
    await browser.close();
  }
}

module.exports = { detectGraphCandidates };
