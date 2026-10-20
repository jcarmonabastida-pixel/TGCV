"use strict";

// Diagnostic-only geometry comparison. This does not change the production resolver
// and makes no accuracy claim: the probes are generated and not independently adjudicated.
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { chromium } = require("playwright");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");

const W = 320, H = 180;
const cases = [
  { id: "arrow-right-circle-25", arrow: "right", halfAngle: 25, targetShape: "circle" },
  { id: "arrow-right-circle-35", arrow: "right", halfAngle: 35, targetShape: "circle" },
  { id: "arrow-right-circle-45", arrow: "right", halfAngle: 45, targetShape: "circle" },
  { id: "arrow-left-circle-35", arrow: "left", halfAngle: 35, targetShape: "circle" },
  { id: "no-arrow-circle", arrow: "none", targetShape: "circle" },
  { id: "no-arrow-ellipse", arrow: "none", targetShape: "ellipse" },
  { id: "no-arrow-rectangle", arrow: "none", targetShape: "rectangle" },
  { id: "no-arrow-rounded-rectangle", arrow: "none", targetShape: "rounded-rectangle" }
];

function svgFor(item) {
  const node = (x, y, label, shape) => {
    let body;
    if (shape === "ellipse") {
      body = '<ellipse cx="' + x + '" cy="' + y + '" rx="16" ry="14" fill="white" stroke="#111" stroke-width="2"/>';
    } else if (shape === "rectangle" || shape === "rounded-rectangle") {
      body = '<rect x="' + (x - 16) + '" y="' + (y - 14) + '" width="32" height="28"' +
        (shape === "rounded-rectangle" ? ' rx="7"' : "") +
        ' fill="white" stroke="#111" stroke-width="2"/>';
    } else {
      body = '<circle cx="' + x + '" cy="' + y + '" r="16" fill="white" stroke="#111" stroke-width="2"/>';
    }
    return body + '<text x="' + x + '" y="' + (y + 5) +
      '" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111">' + label + '</text>';
  };
  const line = (x1, y1, x2, y2) =>
    '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 +
    '" stroke="#111" stroke-width="2.5"/>';
  const head = (x, y, dx, dy, halfAngleDegrees) => {
    const length = Math.hypot(dx, dy);
    const ux = dx / length, uy = dy / length;
    const back = 10;
    const wing = Math.tan(halfAngleDegrees * Math.PI / 180) * back;
    const bx = x - ux * back, by = y - uy * back;
    const px = -uy * wing, py = ux * wing;
    return '<path d="M ' + (bx + px) + ' ' + (by + py) + ' L ' + x + ' ' + y +
      ' L ' + (bx - px) + ' ' + (by - py) +
      '" fill="none" stroke="#111" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>';
  };

  let drawing = node(55, 90, "A", "circle") +
    node(265, 90, "B", item.targetShape) +
    line(71, 90, 249, 90);
  if (item.arrow === "right") drawing += head(249, 90, 1, 0, item.halfAngle);
  if (item.arrow === "left") drawing += head(71, 90, -1, 0, item.halfAngle);
  return '<svg xmlns="http://www.w3.org/2000/svg" width="' + W + '" height="' + H +
    '" viewBox="0 0 ' + W + ' ' + H + '"><rect width="100%" height="100%" fill="white"/>' +
    drawing + '</svg>';
}

function candidateSummary(candidate) {
  if (!candidate) return null;
  const v = candidate.geometric_v_diagnostic || {};
  return {
    angle_degrees: candidate.angle_degrees,
    tip_offset_px: candidate.tip_offset_px,
    tip_candidate: candidate.tip_candidate,
    support_ratio: candidate.support_ratio,
    left_support_ratio: candidate.left_support_ratio,
    right_support_ratio: candidate.right_support_ratio,
    off_axis_support_ratio: candidate.off_axis_support_ratio,
    vertex_dark_pixels_5x5: v.vertex_dark_pixels_5x5,
    vertex_support_ratio: v.vertex_support_ratio
  };
}

function geometryShortlist(hypotheses) {
  const eligible = (Array.isArray(hypotheses) ? hypotheses : []).filter(item =>
    Number.isFinite(item?.support_ratio) &&
    Number.isFinite(item?.left_support_ratio) &&
    Number.isFinite(item?.right_support_ratio) &&
    Number.isFinite(item?.off_axis_support_ratio) &&
    item.left_support_ratio >= 0.50 &&
    item.right_support_ratio >= 0.50 &&
    item.off_axis_support_ratio >= 0.25
  );
  eligible.sort((a, b) =>
    b.off_axis_support_ratio - a.off_axis_support_ratio ||
    Math.min(b.left_support_ratio, b.right_support_ratio) -
      Math.min(a.left_support_ratio, a.right_support_ratio) ||
    b.support_ratio - a.support_ratio ||
    a.tip_offset_px - b.tip_offset_px
  );
  return eligible.slice(0, 3).map(candidateSummary);
}

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "tgcv-arrow-geometry-"));
  const browser = await chromium.launch({ headless: true });
  const rows = [];
  try {
    const page = await browser.newPage({
      viewport: { width: W, height: H },
      deviceScaleFactor: 1
    });
    for (const item of cases) {
      await page.setContent(svgFor(item));
      const imagePath = path.join(tmp, item.id + ".png");
      await page.locator("svg").screenshot({ path: imagePath, type: "png" });
      const result = await detectGraphCandidates(imagePath);
      const edges = result.edge_candidates || [];
      rows.push({
        case_id: item.id,
        intended_geometry: {
          arrow: item.arrow !== "none",
          direction: item.arrow === "right" ? "source-to-target" :
            item.arrow === "left" ? "target-to-source" : "unannotated",
          designed_half_angle_degrees: item.halfAngle ?? null,
          target_node_shape: item.targetShape
        },
        edge_candidates: edges.length,
        observations: edges.map(edge => ({
          direction: edge.direction,
          direction_status: edge.direction_status,
          direction_evidence: edge.direction_evidence,
          from_selected_geometry: candidateSummary(edge.arrowhead_evidence?.at_from),
          to_selected_geometry: candidateSummary(edge.arrowhead_evidence?.at_to),
          from_geometry_shortlist: geometryShortlist(edge.arrowhead_hypotheses?.at_from),
          to_geometry_shortlist: geometryShortlist(edge.arrowhead_hypotheses?.at_to),
          human_review_required: edge.direction_review_required,
          automatic_acceptance: edge.direction_status === "accepted"
        })),
        diagnostic_only: true,
        ground_truth_status: "generated_probe_not_independently_adjudicated"
      });
    }
    process.stdout.write("OCR-ARROW-GEOMETRY-DISCRIMINATOR-001\n");
    process.stdout.write(JSON.stringify({
      benchmark_status: "diagnostic-only",
      claim: "Compare selected tip geometry with no-arrow node contours; no production changes or generalization claim.",
      cases: rows
    }, null, 2) + "\n");
  } finally {
    await browser.close();
    fs.rmSync(tmp, { recursive: true, force: true });
  }
})().catch(error => {
  process.stderr.write(String(error.stack || error) + "\n");
  process.exitCode = 1;
});
