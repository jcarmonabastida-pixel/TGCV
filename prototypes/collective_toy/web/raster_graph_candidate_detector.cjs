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
      // Merge left/right arc fragments that share a vertical span. Rounded
      // outlines often produce two short scanline runs per row rather than one.
      const mergedClusters = [];
      for (const cluster of clusters) {
        let target = mergedClusters.find(c => {
          const overlap = Math.max(0, Math.min(c.maxY, cluster.maxY) - Math.max(c.minY, cluster.minY) + 1);
          const minHeight = Math.min(c.maxY - c.minY + 1, cluster.maxY - cluster.minY + 1);
          const horizontalGap = Math.max(0, Math.max(c.minX, cluster.minX) - Math.min(c.maxX, cluster.maxX) - 1);
          return minHeight > 0 && overlap / minHeight >= 0.6 && horizontalGap <= maxNodeSize;
        });
        if (!target) {
          target = { ...cluster, runs: [...cluster.runs] };
          mergedClusters.push(target);
        } else {
          target.runs.push(...cluster.runs);
          target.minX = Math.min(target.minX, cluster.minX);
          target.maxX = Math.max(target.maxX, cluster.maxX);
          target.minY = Math.min(target.minY, cluster.minY);
          target.maxY = Math.max(target.maxY, cluster.maxY);
          target.cx = (target.minX + target.maxX) / 2;
          target.lastY = Math.max(target.lastY, cluster.lastY);
        }
      }
      const clusterDiagnostics = mergedClusters.map(c => ({ rows: c.runs.length, minX: c.minX, maxX: c.maxX, minY: c.minY, maxY: c.maxY, width: c.maxX - c.minX + 1, height: c.maxY - c.minY + 1, centerX: Math.round(c.cx), firstY: c.runs[0]?.y, lastY: c.lastY }));
      const rejectionCounts = { tooFewRows: 0, heightOutOfRange: 0, widthOutOfRange: 0, duplicateCenter: 0, accepted: 0 };
      const candidates = [];
      for (const cluster of mergedClusters) {
        const w = cluster.maxX - cluster.minX + 1;
        const h = cluster.maxY - cluster.minY + 1;
        if (cluster.runs.length < 8) { rejectionCounts.tooFewRows++; continue; }
        if (h < minNodeSize || h > maxNodeSize) { rejectionCounts.heightOutOfRange++; continue; }
        if (w < minNodeSize || w > maxNodeSize) { rejectionCounts.widthOutOfRange++; continue; }
        const cx = Math.round((cluster.minX + cluster.maxX) / 2);
        const cy = Math.round((cluster.minY + cluster.maxY) / 2);
        if (candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) { rejectionCounts.duplicateCenter++; continue; }
        candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
          bbox: [cluster.minX, cluster.minY, cluster.maxX, cluster.maxY], confidence: "low", review_required: true });
        rejectionCounts.accepted++;
      }

      // Fallback candidate pass: pair broad horizontal bands at similar x
      // extents. This matches the observed rasterized rounded-node caps where
      // the top and bottom bands are separated by the node's full height.
      const bands = runs.filter(r => r.len >= minNodeSize && r.len <= maxNodeSize);
      for (let i = 0; i < bands.length; i++) {
        const top = bands[i];
        let best = null;
        let bestScore = Infinity;
        for (let j = i + 1; j < bands.length; j++) {
          const bottom = bands[j];
          const dy = bottom.y - top.y;
          if (dy < minNodeSize) continue;
          if (dy > maxNodeSize) break;
          const xError = Math.abs(top.x1 - bottom.x1) + Math.abs(top.x2 - bottom.x2);
          if (xError > 8) continue;
          const score = xError + Math.abs(top.len - bottom.len);
          if (score < bestScore) { best = bottom; bestScore = score; }
        }
        if (!best) continue;
        const x1 = Math.min(top.x1, best.x1), x2 = Math.max(top.x2, best.x2);
        const y1 = top.y, y2 = best.y;
        const w = x2 - x1 + 1, h = y2 - y1 + 1;
        if (w < minNodeSize || w > maxNodeSize || h < minNodeSize || h > maxNodeSize) continue;
        const cx = Math.round((x1 + x2) / 2), cy = Math.round((y1 + y2) / 2);
        if (candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) continue;
        candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
          bbox: [x1, y1, x2, y2], confidence: "low", review_required: true,
          proposal_method: "paired-horizontal-bands" });
        rejectionCounts.accepted++;
      }

      // Enclosed-light-region pass: node borders enclose white interior
      // regions even when their dark outlines are split into several runs.
      // Components touching the canvas boundary are background and ignored.
      const visitedLight = new Uint8Array(width * height);
      const queue = new Int32Array(width * height);
      const interiorRegions = [];
      for (let seed = 0; seed < width * height; seed++) {
        if (visitedLight[seed] || dark[seed]) continue;
        let head = 0, tail = 0;
        queue[tail++] = seed;
        visitedLight[seed] = 1;
        let minX = width, maxX = -1, minY = height, maxY = -1, touchesBorder = false, area = 0;
        while (head < tail) {
          const p = queue[head++], x = p % width, y = Math.floor(p / width);
          area++;
          minX = Math.min(minX, x); maxX = Math.max(maxX, x);
          minY = Math.min(minY, y); maxY = Math.max(maxY, y);
          if (x === 0 || y === 0 || x === width - 1 || y === height - 1) touchesBorder = true;
          const neighbors = [x > 0 ? p - 1 : -1, x + 1 < width ? p + 1 : -1,
            y > 0 ? p - width : -1, y + 1 < height ? p + width : -1];
          for (const q of neighbors) {
            if (q >= 0 && !visitedLight[q] && !dark[q]) {
              visitedLight[q] = 1;
              queue[tail++] = q;
            }
          }
        }
        const w = maxX - minX + 1, h = maxY - minY + 1;
        if (!touchesBorder && area >= 12 && w >= minNodeSize - 4 && w <= maxNodeSize &&
            h >= minNodeSize - 4 && h <= maxNodeSize) {
          interiorRegions.push({ bbox: [minX, minY, maxX, maxY], area, width: w, height: h });
          const cx = Math.round((minX + maxX) / 2), cy = Math.round((minY + maxY) / 2);
          if (!candidates.some(n => Math.hypot(n.center[0] - cx, n.center[1] - cy) < 12)) {
            candidates.push({ id: "candidate-node-" + (candidates.length + 1), center: [cx, cy],
              bbox: [minX, minY, maxX, maxY], confidence: "low", review_required: true,
              proposal_method: "enclosed-light-region" });
            rejectionCounts.accepted++;
          }
        }
      }

      // Multi-angle line evidence: accumulate dark pixels along candidate
      // directions, excluding pixels well inside accepted node boxes. These
      // are geometric hypotheses only; node attachment/direction are not inferred.
      const lineCandidates = [];
      const seenLines = new Set();
      const angles = [-45, -30, -20, -10, 0, 10, 20, 30, 45];
      for (const angle of angles) {
        const slope = Math.tan(angle * Math.PI / 180);
        for (let x0 = 0; x0 < width; x0 += 2) {
          for (let y0 = 0; y0 < height; y0 += 2) {
            let points = [], misses = 0;
            for (let step = 0; step < Math.max(width, height); step++) {
              const x = Math.round(x0 + step);
              const y = Math.round(y0 + slope * step);
              if (x < 0 || x >= width || y < 0 || y >= height) break;
              const insideNode = candidates.some(n => x > n.bbox[0] + 2 && x < n.bbox[2] - 2 &&
                y > n.bbox[1] + 2 && y < n.bbox[3] - 2);
              if (!insideNode && dark[y * width + x]) {
                points.push([x,y]); misses = 0;
              } else if (points.length) {
                misses++;
                if (misses > 2) break;
              }
            }
            if (points.length < 24) continue;
            const from = points[0], to = points[points.length - 1];
            if (Math.hypot(to[0]-from[0],to[1]-from[1]) < 24) continue;
            const key = [from[0],from[1],to[0],to[1]].join(",");
            const reverseKey = [to[0],to[1],from[0],from[1]].join(",");
            if (seenLines.has(key) || seenLines.has(reverseKey)) continue;
            seenLines.add(key);
            lineCandidates.push({ orientation: angle === 0 ? "horizontal" : angle === 45 || angle === -45 ? "diagonal" : "oblique",
              angle_degrees: angle, from, to, evidence_pixels: points.length,
              confidence: "low", review_required: true });
          }
        }
      }
      // Node-pair edge hypotheses: sample the corridor between each pair
      // of node boxes. This filters arbitrary long strokes into graph-shaped
      // hypotheses; the support score is diagnostic and does not assert direction.
      const edgeCandidates = [];
      const nodePairs = [];
      const lineSupport = (a, b) => {
        const dx = b[0] - a[0], dy = b[1] - a[1];
        const length = Math.hypot(dx, dy);
        const steps = Math.max(1, Math.ceil(length));
        let supported = 0, tested = 0;
        for (let i = 2; i < steps - 2; i++) {
          const x = Math.round(a[0] + dx * i / steps), y = Math.round(a[1] + dy * i / steps);
          let found = false;
          for (let oy = -1; oy <= 1 && !found; oy++) for (let ox = -1; ox <= 1; ox++) {
            const px = x + ox, py = y + oy;
            if (px >= 0 && px < width && py >= 0 && py < height && dark[py * width + px]) { found = true; break; }
          }
          tested++;
          if (found) supported++;
        }
        return { ratio: tested ? supported / tested : 0, supported, tested };
      };
      const boundaryPoint = (node, target) => {
        const c = node.center, dx = target[0] - c[0], dy = target[1] - c[1];
        const halfW = Math.max(1, (node.bbox[2] - node.bbox[0]) / 2);
        const halfH = Math.max(1, (node.bbox[3] - node.bbox[1]) / 2);
        const scale = 1 / Math.max(Math.abs(dx) / halfW || 0, Math.abs(dy) / halfH || 0);
        return [Math.round(c[0] + dx * scale), Math.round(c[1] + dy * scale)];
      };
      for (let i = 0; i < candidates.length; i++) {
        for (let j = i + 1; j < candidates.length; j++) {
          const a = candidates[i], b = candidates[j];
          const pa = boundaryPoint(a, b.center), pb = boundaryPoint(b, a.center);
          const support = lineSupport(pa, pb);
          if (support.tested < 20 || support.ratio < 0.42) continue;
          const key = [a.id, b.id].sort().join("--");
          if (nodePairs.includes(key)) continue;
          nodePairs.push(key);
          edgeCandidates.push({ id: "candidate-edge-" + (edgeCandidates.length + 1),
            source_candidate_node_id: a.id, target_candidate_node_id: b.id,
            from: pa, to: pb, orientation: Math.abs(pa[1]-pb[1]) <= 3 ? "horizontal" : "diagonal",
            line_support_ratio: Number(support.ratio.toFixed(3)), evidence_pixels: support.supported,
            confidence: "low", review_required: true, direction: "undetermined" });
        }
      }
      return {
        detector: "TGCV-RASTER-GRAPH-CANDIDATES-001",
        status: "experimental-candidates-only",
        image: { width, height },
        method: "Canvas grayscale threshold; vertically clustered horizontal runs for rounded/box node candidates; long horizontal stroke candidates",
        nodes: candidates,
        diagnostics: { runCount: runs.length, clusterCount: clusters.length, enclosedRegionCount: interiorRegions.length, enclosedRegions: interiorRegions, rejectionCounts, largestClusters: clusterDiagnostics.sort((a, b) => b.rows - a.rows).slice(0, 20) },
        edge_candidates: edgeCandidates,\n        raw_line_candidates: lineCandidates,
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
