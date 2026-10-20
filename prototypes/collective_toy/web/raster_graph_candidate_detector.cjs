"use strict";

const { resolveArrowDirection } = require("./arrow_direction_resolver.cjs");

/**
 * Current evidence is insufficient to classify arrowhead presence or absence.
 * Positive V-shaped evidence is only a candidate cue, and zero sampled support
 * is not calibrated negative evidence. Return null until both positive and
 * negative classifications have validated confidence criteria; direction
 * proposals remain subject to human review.
 */
function inferArrowheadPresenceFromEvidence(edge) {
  const endpoints = [edge?.arrowhead_hypotheses?.at_from, edge?.arrowhead_hypotheses?.at_to];
  // Missing or malformed evidence cannot establish presence or absence.
  if (endpoints.some(endpoint => !Array.isArray(endpoint) || endpoint.length === 0)) return null;
  const diagnostics = endpoints.map(endpoint => endpoint.map(candidate => candidate?.geometric_v_diagnostic));
  if (diagnostics.some(endpoint => endpoint.some(v =>
    !Number.isFinite(v?.left_arm_support_ratio) ||
    !Number.isFinite(v?.right_arm_support_ratio) ||
    !Number.isFinite(v?.bilateral_off_axis_support_ratio)))) return null;

  // Positive V-shaped evidence is only a candidate cue, not an adjudicated
  // arrowhead. Conversely, zero sampled support is not proof of absence:
  // rasterization, orientation, occlusion or sampling can hide a real tip.
  // This detector has no calibrated negative-evidence model, so it must not
  // emit arrowhead_present=false from these diagnostics alone.
  return null;
}

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
    const detected = await page.evaluate(async ({ imageDataUrl, threshold, minNodeSize, maxNodeSize }) => {
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
      const arrowheadEvidence = (tip, inwardUnit) => {
        // The visible arrow tip may sit slightly inside the edge corridor rather
        // than exactly on the node boundary. Search a short, bounded interval
        // along the edge axis instead of sampling only the boundary point.
        // This is evidence localization only; it never accepts a direction.
        const candidates = [];
        for (let offset = 0; offset <= 18; offset += 2) {
          const candidateTip = [
            Math.round(tip[0] + inwardUnit[0] * offset),
            Math.round(tip[1] + inwardUnit[1] * offset)
          ];
          for (const angle of [25, 35, 45, 55, 65]) {
            const rad = angle * Math.PI / 180;
            const armHits = [0, 0];
            const armHitsOffAxis = [0, 0];
            const armOffAxisByDistance = [[], []];
            const armTested = [0, 0];
            for (let side = 0; side < 2; side++) {
              const sign = side === 0 ? -1 : 1;
              const ux = inwardUnit[0] * Math.cos(rad) - sign * inwardUnit[1] * Math.sin(rad);
              const uy = inwardUnit[1] * Math.cos(rad) + sign * inwardUnit[0] * Math.sin(rad);
              for (let distance = 3; distance <= 13; distance++) {
                const x = Math.round(candidateTip[0] + ux * distance);
                const y = Math.round(candidateTip[1] + uy * distance);
                armTested[side]++;
                let found = false;
                let foundOffAxis = false;
                for (let oy = -1; oy <= 1; oy++) {
                  for (let ox = -1; ox <= 1; ox++) {
                    const px = x + ox, py = y + oy;
                    if (px < 0 || px >= width || py < 0 || py >= height || !dark[py * width + px]) continue;
                    found = true;
                    const lateral = Math.abs((px - candidateTip[0]) * (-inwardUnit[1]) +
                      (py - candidateTip[1]) * inwardUnit[0]);
                    if (lateral >= 2.5) foundOffAxis = true;
                  }
                }
                if (found) armHits[side]++;
                if (foundOffAxis) armHitsOffAxis[side]++;
                armOffAxisByDistance[side].push(foundOffAxis ? 1 : 0);
              }
            }
            const armRatios = armHits.map((hits, i) => armTested[i] ? hits / armTested[i] : 0);
            const offAxisArmRatios = armHitsOffAxis.map((hits, i) => armTested[i] ? hits / armTested[i] : 0);
            const vertexPixels = [];
            // candidateTip can be fractional; typed-array indexing must use integer pixel coordinates.
            const vertexCenterX = Math.round(candidateTip[0]);
            const vertexCenterY = Math.round(candidateTip[1]);
            for (let oy = -2; oy <= 2; oy++) for (let ox = -2; ox <= 2; ox++) {
              const px = vertexCenterX + ox, py = vertexCenterY + oy;
              if (px >= 0 && px < width && py >= 0 && py < height && dark[py * width + px]) {
                vertexPixels.push([px, py]);
              }
            }
            const vertexSupportRatio = vertexPixels.length / 25;
            const armBalanceRatio = Math.min(...armRatios) / Math.max(0.0001, Math.max(...armRatios));
            const pairedArmSupportRatio = Math.min(
              armOffAxisByDistance[0].reduce((sum, hit) => sum + hit, 0),
              armOffAxisByDistance[1].reduce((sum, hit) => sum + hit, 0)
            ) / Math.max(1, armTested[0]);
            candidates.push({
              angle_degrees: angle,
              tip_offset_px: offset,
              tip_candidate: candidateTip,
              geometric_v_diagnostic: {
                vertex_dark_pixels_5x5: vertexPixels.length,
                vertex_support_ratio: Number(vertexSupportRatio.toFixed(4)),
                left_arm_support_ratio: Number(armRatios[0].toFixed(4)),
                right_arm_support_ratio: Number(armRatios[1].toFixed(4)),
                arm_balance_ratio: Number(armBalanceRatio.toFixed(4)),
                bilateral_off_axis_support_ratio: Number(pairedArmSupportRatio.toFixed(4)),
                diagnostic_only: true
              },
              support_ratio: Math.min(...armRatios),
              bilateral_support_ratio: Number(Math.min(...armRatios).toFixed(4)),
              left_support_ratio: Number(armRatios[0].toFixed(4)),
              right_support_ratio: Number(armRatios[1].toFixed(4)),
              off_axis_support_ratio: Number(Math.min(...offAxisArmRatios).toFixed(4)),
              left_off_axis_support_ratio: Number(offAxisArmRatios[0].toFixed(4)),
              right_off_axis_support_ratio: Number(offAxisArmRatios[1].toFixed(4)),
              left_off_axis_hits_by_distance: armOffAxisByDistance[0],
              right_off_axis_hits_by_distance: armOffAxisByDistance[1],
              paired_off_axis_distances: armOffAxisByDistance[0].filter((hit, i) => hit && armOffAxisByDistance[1][i]).length,
              supported_samples: armHits.reduce((sum, n) => sum + n, 0),
              tested_samples: armTested.reduce((sum, n) => sum + n, 0)
            });
          }
        }
        // Retain the leading hypotheses for diagnosis. The downstream resolver
        // still selects the highest-scoring candidate, so this adds observability
        // without changing the direction decision or its confidence thresholds.
        return candidates.sort((a, b) =>
          b.support_ratio - a.support_ratio ||
          a.tip_offset_px - b.tip_offset_px ||
          a.angle_degrees - b.angle_degrees
        );
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
          // Do not propose a long edge that passes through an intervening node.
          // This removes the linear fixture's A->C shortcut when B lies on A-C.
          const vx = b.center[0] - a.center[0], vy = b.center[1] - a.center[1];
          const lengthSquared = vx * vx + vy * vy;
          const interveningNode = candidates.some((node, k) => {
            if (k === i || k === j || lengthSquared === 0) return false;
            const wx = node.center[0] - a.center[0], wy = node.center[1] - a.center[1];
            const t = (wx * vx + wy * vy) / lengthSquared;
            if (t <= 0.08 || t >= 0.92) return false;
            const perpendicular = Math.abs(vx * wy - vy * wx) / Math.sqrt(lengthSquared);
            return perpendicular <= 10;
          });
          if (interveningNode) continue;
          const pa = boundaryPoint(a, b.center), pb = boundaryPoint(b, a.center);
          const support = lineSupport(pa, pb);
          if (support.tested < 20 || support.ratio < 0.42) continue;
          const key = [a.id, b.id].sort().join("--");
          if (nodePairs.includes(key)) continue;
          nodePairs.push(key);
          const edgeLength = Math.max(1, Math.hypot(pb[0]-pa[0], pb[1]-pa[1]));
          const unitAB = [(pb[0]-pa[0]) / edgeLength, (pb[1]-pa[1]) / edgeLength];
          const unitBA = [-unitAB[0], -unitAB[1]];
          const arrowheadHypothesesByEndpoint = {
            at_from: arrowheadEvidence(pa, unitAB),
            at_to: arrowheadEvidence(pb, unitBA)
          };
          // Preserve the original single-object evidence contract for the
          // detector integration tests and resolver; expose alternatives in a
          // separate diagnostic field so observability cannot break consumers.
          const arrowheadEvidenceByEndpoint = {
            at_from: arrowheadHypothesesByEndpoint.at_from[0] || null,
            at_to: arrowheadHypothesesByEndpoint.at_to[0] || null
          };
          // Direction resolution runs in Node after Canvas analysis returns.
          // Browser evaluate has no access to CommonJS module bindings.
          edgeCandidates.push({ id: "candidate-edge-" + (edgeCandidates.length + 1),
            source_candidate_node_id: a.id, target_candidate_node_id: b.id,
            from: pa, to: pb, orientation: Math.abs(pa[1]-pb[1]) <= 3 ? "horizontal" : "diagonal",
            line_support_ratio: Number(support.ratio.toFixed(3)), evidence_pixels: support.supported,
            arrowhead_evidence: arrowheadEvidenceByEndpoint,
            arrowhead_hypotheses: arrowheadHypothesesByEndpoint,
            direction_status: "unresolved",
            direction_reason: "Direction resolution pending post-processing outside the browser context.",
            direction_evidence: null,
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
        edge_candidates: edgeCandidates,
        raw_line_candidates: lineCandidates,
        limitations: [
          "Not a complete node detector: connected outlines may be fragmented or merged.",
          "Direction proposals are generated by a separate experimental resolver after Canvas analysis; diagonal edges, edge-to-node attachment and crossing topology are not fully inferred.",
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
    detected.edge_candidates = (detected.edge_candidates || []).map(edge => {
      // Select endpoint evidence by the actual two-arm arrowhead geometry,
      // not by raw arm-pixel support alone (which often favors the connector).
      // A candidate that does not pass these conservative gates is not used
      // to propose direction; it remains unresolved.
      const bestArrowhead = endpoint => {
        const hypotheses = Array.isArray(endpoint) ? endpoint : endpoint ? [endpoint] : [];
        const eligible = hypotheses.filter(item =>
          Number.isFinite(item?.support_ratio) &&
          Number.isFinite(item?.left_support_ratio) &&
          Number.isFinite(item?.right_support_ratio) &&
          Number.isFinite(item?.off_axis_support_ratio) &&
          item.left_support_ratio >= 0.55 &&
          item.right_support_ratio >= 0.55 &&
          item.off_axis_support_ratio >= 0.35
        );
        const byArrowheadGeometry = (a, b) =>
          (b.off_axis_support_ratio ?? -1) - (a.off_axis_support_ratio ?? -1) ||
          Math.min(b.left_support_ratio ?? -1, b.right_support_ratio ?? -1) -
            Math.min(a.left_support_ratio ?? -1, a.right_support_ratio ?? -1) ||
          b.support_ratio - a.support_ratio ||
          (a.tip_offset_px ?? Infinity) - (b.tip_offset_px ?? Infinity);
        // Preserve a measured fallback for the weaker endpoint so the resolver
        // can compare both endpoint scores. The bilateral geometry gate applies
        // to the winning endpoint only; discarding the weaker endpoint here
        // would force every otherwise-clear arrow to "unresolved".
        return eligible.sort(byArrowheadGeometry)[0] ||
          hypotheses.filter(item => Number.isFinite(item?.support_ratio))
            .sort((a, b) => b.support_ratio - a.support_ratio)[0] || null;
      };
      const arrowheadPresent = inferArrowheadPresenceFromEvidence(edge);
      const decision = resolveArrowDirection({
        arrowhead_evidence: {
          at_from: bestArrowhead(edge.arrowhead_hypotheses?.at_from ?? edge.arrowhead_evidence?.at_from),
          at_to: bestArrowhead(edge.arrowhead_hypotheses?.at_to ?? edge.arrowhead_evidence?.at_to),
          ...(arrowheadPresent === false ? { arrowhead_present: false } : {})
        }
      });
      return {
        ...edge,
        arrowhead_presence: arrowheadPresent === false ? "not_detected" : "possible_or_uncertain",
        arrowhead_presence_review_required: true,
        ...decision,
        direction_review_required: true
      };
    });
    detected.direction_diagnostics = {
      resolver: "TGCV-ARROW-DIRECTION-RESOLVER-001",
      edge_candidates: detected.edge_candidates.length,
      proposed_directions: detected.edge_candidates.filter(edge => edge.direction_status === "candidate").length,
      unresolved_directions: detected.edge_candidates.filter(edge => edge.direction_status === "unresolved").length,
      automatic_acceptance: false,
      note: "Direction proposals are experimental and require human review; resolver has not been validated for real-world diagrams."
    };
    return detected;
  } finally {
    await browser.close();
  }
}

module.exports = { detectGraphCandidates, inferArrowheadPresenceFromEvidence };
