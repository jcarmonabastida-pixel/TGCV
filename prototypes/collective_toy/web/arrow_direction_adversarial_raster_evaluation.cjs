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
  { id: "arrow-right", kind: "clear-arrow", arrow: "right" },
  { id: "arrow-left", kind: "clear-arrow", arrow: "left" },
  { id: "no-arrow", kind: "connector-no-arrow", arrow: "none" },
  { id: "ambiguous-two-heads", kind: "ambiguous", arrow: "both" },
  { id: "branch-arrow", kind: "branch", arrow: "right" }
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
    if (item.arrow === "both") drawing += head(71,90,"left")+head(249,90,"right");
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
      for (const edge of edges) {
        assert.equal(edge.direction_review_required, true, item.id + ": human review required");
        assert.notEqual(edge.direction_status, "accepted", item.id + ": no auto-acceptance");
        assert.equal(edge.arrowhead_presence_review_required, true, item.id + ": presence review required");
      }
      rows.push({
        case_id: item.id, case_kind: item.kind, edge_candidates: edges.length,
        direction_candidates: edges.filter(e => e.direction_status === "candidate").length,
        unresolved_or_undetermined: edges.filter(e => e.direction_status !== "candidate").length,
        auto_accepted: edges.filter(e => e.direction_status === "accepted").length,
        edge_diagnostics: edges.map(edge => ({
          edge_id: edge.id,
          direction: edge.direction,
          direction_status: edge.direction_status,
          direction_reason: edge.direction_reason,
          direction_confidence: edge.confidence,
          arrowhead_presence: edge.arrowhead_presence,
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
