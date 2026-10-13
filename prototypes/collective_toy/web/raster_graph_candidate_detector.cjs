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

      // Gather all moderate horizontal runs, including short runs at the
      // rounded caps of circular/elliptical nodes.
      const runs = [];
      for (let y = 2; y < height - 2; y++) {
        let start = -1;
        for (let x = 0; x <= width; x++) {
          const on = x < width && dark[y * width + x] === 1;
          if (on && start < 0) start = x;
          if ((!on || x === width) && start >= 0) {
            const len = x - start;
            if (len >= 3 && len <= maxNodeSize) runs.push({ y, x1: start, x2: x - 1, len, cx: (start + x - 1) / 2 });
            start = -1;
          }
        }
      }

      // Cluster row runs by approximate center x and continuity in y. A node's
      // rounded outline changes width by row, so exact run-end matching is
      // inappropriate. Wide connector strokes are excluded from node clusters.
      const clusters = [];
      for (const run of runs) {
        if (run.len > maxNodeSize) continue;
        let cluster = clusters.find(c => Math.abs(c.cx - run.cx) <= 5 &&
          run.y >= c.lastY && run.y - c.lastY <= 3);
        if (!cluster) {
          cluster = { runs: [], cx: run.cx, lastY: run.y, minX: run.x1, maxX: run.x2, minY: run.y, maxY: run.y };
          clusters.push(cluster);
        }
        cluster.runs.push(run);
        cluster.lastY = run.y;
        cluster.minX = Math.min(cluster.minX, run.x1);
        cluster.maxX = Math.max(cluster.maxX, run.x2);
        cluster.minY = Math.min(cluster.minY, run.y);
        cluster.maxY = Math.max(cluster.maxY, run.y);
        cluster.cx = cluster.runs.reduce((sum, r) => sum + r.cx, 0) / cluster.runs.length;
      }
      const candidates = [];
      for (const cluster of clusters) {
        const w = cluster.maxX - cluster.minX + 1;
        const h = cluster.maxY - cluster.minY + 1;
        if (cluster.runs.length < 8 || h < minNodeSize || h > maxNodeSize || w < minNodeSize || w > maxNodeSize) continue;
        const cx = Math.round((cluster.minX + cluster.maxX) / 2);
        const cy = Math.round((cluster.minY + cluster.maxY) / 2);
        if (candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) continue;
        candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
          bbox: [cluster.minX, cluster.minY, cluster.maxX, cluster.maxY], confidence: "low", review_required: true });
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
        method: "Canvas grayscale threshold; vertically clustered horizontal runs for rounded/box node candidates; long horizontal stroke candidates",
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
