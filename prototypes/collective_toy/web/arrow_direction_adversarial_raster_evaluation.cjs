"use strict";

// Diagnostic-only adversarial raster benchmark. Generated probes are not independently
// adjudicated ground truth and must not be treated as a validation claim.
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const assert = require("node:assert/strict");
const { chromium } = require("playwright");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");

const W = 320, H = 180;
const cases = [
  { id: "arrow-right", kind: "clear-arrow", arrow: "right", expectedDirection: "source-to-target", expectedStatus: "candidate" },
  { id: "arrow-left", kind: "clear-arrow", arrow: "left", expectedDirection: "target-to-source", expectedStatus: "candidate" },
  { id: "no-arrow", kind: "connector-no-arrow", arrow: "none", expectedDirection: "undetermined", expectedStatus: "unresolved" },
  { id: "ambiguous-two-heads", kind: "ambiguous", arrow: "both", expectedDirection: "undetermined", expectedStatus: "unresolved" },
  { id: "branch-arrow", kind: "branch", arrow: "right", arrowTips: [[142,51],[142,129]], expectedStatus: "candidate" }
];

function svgFor(item) {
  const node = (x, y, label) => '<circle cx="' + x + '" cy="' + y + '" r="16" fill="white" stroke="#111" stroke-width="2"/><text x="' + x + '" y="' + (y+5) + '" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111">' + label + '</text>';
  const line = (x1,y1,x2,y2) => '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#111" stroke-width="2.5"/>';
  // Construct arrowhead arms relative to the actual edge direction.
  // The earlier horizontal-only V was invalid for diagonal branch edges and
  // could create an artificial ambiguity in the benchmark itself.
  const head = (x,y,dx,dy) => {
    const length = Math.hypot(dx,dy);
    const ux = dx / length, uy = dy / length;
    const bx = x - ux * 10, by = y - uy * 10;
    const px = -uy * 7, py = ux * 7;
    return '<path d="M ' + (bx+px) + ' ' + (by+py) + ' L ' + x + ' ' + y + ' L ' + (bx-px) + ' ' + (by-py) + '" fill="none" stroke="#111" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>';
  };
  let drawing = "";
  if (item.kind === "branch") {
    drawing = node(45,90,"A")+node(160,45,"B")+node(160,135,"C");
    drawing += line(61,86,142,51)+head(142,51,81,-35);
    drawing += line(61,94,142,129)+head(142,129,81,35);
  } else {
    drawing = node(55,90,"A")+node(265,90,"B")+line(71,90,249,90);
    if (item.arrow === "right") drawing += head(249,90,1,0);
    if (item.arrow === "left") drawing += head(71,90,-1,0);
    if (item.arrow === "both") drawing += head(71,90,-1,0)+head(249,90,1,0);
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '"><rect width="100%" height="100%" fill="white"/>' + drawing + '</svg>';
}

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "tgcv-arrow-adversarial-"));
  const browser = await chromium.launch({ headless: true });
  const rows = [];
  try {
    const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
    for (const item of cases) {
      await page.setContent(svgFor(item));
      const imagePath = path.join(tmp, item.id + ".png");
      await page.locator("svg").screenshot({ path: imagePath, type: "png" });
      const result = await detectGraphCandidates(imagePath);
      const edges = result.edge_candidates || [];
      process.stderr.write("ARROW-ADVERSARIAL-PROBE-DIAGNOSTIC " + item.id + ": " +
        JSON.stringify(edges.map(candidate => ({
          from: candidate.from,
          to: candidate.to,
          direction: candidate.direction,
          direction_status: candidate.direction_status,
          direction_reason: candidate.direction_reason,
          direction_evidence: candidate.direction_evidence,
          at_from: candidate.arrowhead_evidence?.at_from,
          at_to: candidate.arrowhead_evidence?.at_to
        }))) + "\\n");
      for (const edge of edges) {
        assert.equal(edge.direction_review_required, true, item.id + ": human review required");
        assert.notEqual(edge.direction_status, "accepted", item.id + ": no auto-acceptance");
        assert.equal(edge.arrowhead_presence_review_required, true, item.id + ": presence review required");
      }
      // These assertions validate the generated probe's known construction,
      // not generalization to independently sourced diagrams.
      if (item.expectedStatus) {
        assert.ok(edges.length > 0, item.id + ": expected at least one detected edge");
        for (const edge of edges) {
          if (edge.direction_status !== item.expectedStatus ||
              (item.expectedDirection && edge.direction !== item.expectedDirection)) {
            process.stderr.write("ARROW-ADVERSARIAL-FAILURE-DIAGNOSTIC " + item.id + ": " +
              JSON.stringify(edges.map(candidate => ({
                id: candidate.id,
                from: candidate.from,
                to: candidate.to,
                direction: candidate.direction,
                direction_status: candidate.direction_status,
                direction_reason: candidate.direction_reason,
                direction_evidence: candidate.direction_evidence,
                arrowhead_presence: candidate.arrowhead_presence,
                arrowhead_evidence: candidate.arrowhead_evidence,
                arrowhead_hypotheses: candidate.arrowhead_hypotheses
              }))) + "\\n");
          }
          assert.equal(edge.direction_status, item.expectedStatus,
            item.id + ": direction status differs from the expected probe behavior");
          if (item.expectedDirection) assert.equal(edge.direction, item.expectedDirection,
            item.id + ": direction differs from the generated arrow annotation");
        }
      }
      if (item.arrowTips) {
        assert.equal(edges.length, item.arrowTips.length,
          item.id + ": detected edge count differs from the generated branch annotation");
        // Derive each expected direction from the independently authored arrow-tip
        // coordinate and the edge endpoint coordinates, not from a hard-coded
        // resolver label. source-to-target means the annotated tip is nearer "to".
        for (const edge of edges) {
          assert.ok(Array.isArray(edge.from) && Array.isArray(edge.to),
            item.id + ": endpoint coordinates are required for reference comparison");
          const midpointY = (edge.from[1] + edge.to[1]) / 2;
          const tip = item.arrowTips.reduce((best, candidate) =>
            Math.abs(candidate[1] - midpointY) < Math.abs(best[1] - midpointY) ? candidate : best);
          const distance = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
          const expected = distance(edge.to, tip) < distance(edge.from, tip)
            ? "source-to-target" : "target-to-source";
          assert.equal(edge.direction, expected,
            item.id + ": proposal disagrees with arrow-tip annotation " + JSON.stringify(tip));
        }
      }
      rows.push({
        case_id: item.id, case_kind: item.kind, edge_candidates: edges.length,
        direction_candidates: edges.filter(e => e.direction_status === "candidate").length,
        unresolved_or_undetermined: edges.filter(e => e.direction_status !== "candidate").length,
        auto_accepted: edges.filter(e => e.direction_status === "accepted").length,
        edge_diagnostics: edges.map(edge => ({
          edge_id: edge.id,
          source_candidate_node_id: edge.source_candidate_node_id,
          target_candidate_node_id: edge.target_candidate_node_id,
          from: edge.from,
          to: edge.to,
          orientation: edge.orientation,
          direction: edge.direction,
          direction_status: edge.direction_status,
          direction_reason: edge.direction_reason,
          direction_evidence: edge.direction_evidence,
          // Keep detector confidence separate from directional confidence.
          // The resolver currently emits no calibrated direction-confidence field.
          edge_candidate_confidence: edge.confidence,
          direction_confidence: Number.isFinite(edge.direction_confidence)
            ? edge.direction_confidence : null,
          arrowhead_presence: edge.arrowhead_presence,
          arrowhead_evidence: {
            at_from: edge.arrowhead_evidence?.at_from
              ? { support_ratio: edge.arrowhead_evidence.at_from.support_ratio,
                  tested_samples: edge.arrowhead_evidence.at_from.tested_samples,
                  selected_hypothesis: edge.arrowhead_evidence.at_from }
              : null,
            at_to: edge.arrowhead_evidence?.at_to
              ? { support_ratio: edge.arrowhead_evidence.at_to.support_ratio,
                  tested_samples: edge.arrowhead_evidence.at_to.tested_samples,
                  selected_hypothesis: edge.arrowhead_evidence.at_to }
              : null,
            hypothesis_summary: {
              at_from: (edge.arrowhead_hypotheses?.at_from || []).slice(0, 5).map(h => ({
                angle_degrees: h.angle_degrees,
                tip_offset_px: h.tip_offset_px,
                tip_candidate: h.tip_candidate,
                support_ratio: h.support_ratio,
                left_support_ratio: h.left_support_ratio,
                right_support_ratio: h.right_support_ratio,
                off_axis_support_ratio: h.off_axis_support_ratio,
                vertex_support_ratio: h.geometric_v_diagnostic?.vertex_support_ratio
              })),
              at_to: (edge.arrowhead_hypotheses?.at_to || []).slice(0, 5).map(h => ({
                angle_degrees: h.angle_degrees,
                tip_offset_px: h.tip_offset_px,
                tip_candidate: h.tip_candidate,
                support_ratio: h.support_ratio,
                left_support_ratio: h.left_support_ratio,
                right_support_ratio: h.right_support_ratio,
                off_axis_support_ratio: h.off_axis_support_ratio,
                vertex_support_ratio: h.geometric_v_diagnostic?.vertex_support_ratio
              }))
            }
          },
          review_required: edge.direction_review_required
        })),
        diagnostic_only: true, ground_truth_status: "synthetic_probe_not_independently_adjudicated"
      });
    }
    process.stdout.write("OCR-ARROW-ADVERSARIAL-DIAGNOSTIC-001\n");
    process.stdout.write(JSON.stringify({
      benchmark_status: "diagnostic-only",
      claim: "No accuracy/generalization claim; probes are generated and not independently adjudicated.",
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
