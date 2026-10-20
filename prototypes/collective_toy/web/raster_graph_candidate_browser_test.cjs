"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { chromium } = require("playwright");

function svgFor(kind) {
  const node = (x, y, label) =>
    '<circle cx="' + x + '" cy="' + y + '" r="15" fill="white" stroke="#111" stroke-width="2"/>' +
    '<text x="' + x + '" y="' + (y + 5) + '" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#111">' + label + '</text>';
  const line = (x1, y1, x2, y2) =>
    '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#111" stroke-width="2.5"/>';
  const head = (x, y, dx, dy) => {
    const length = Math.hypot(dx, dy), ux = dx / length, uy = dy / length;
    const bx = x - ux * 9, by = y - uy * 9, px = -uy * 6, py = ux * 6;
    return '<path d="M ' + (bx + px) + ' ' + (by + py) + ' L ' + x + ' ' + y +
      ' L ' + (bx - px) + ' ' + (by - py) + '" fill="none" stroke="#111" stroke-width="2.5"/>';
  };
  let drawing;
  if (kind === "linear") {
    drawing = node(45, 90, "A") + node(160, 90, "B") + node(275, 90, "C") +
      line(60, 90, 145, 90) + head(145, 90, 1, 0) +
      line(175, 90, 260, 90) + head(260, 90, 1, 0);
  } else if (kind === "branch") {
    drawing = node(45, 90, "A") + node(160, 45, "B") + node(160, 135, "C") +
      line(60, 84, 145, 49) + head(145, 49, 85, -35) +
      line(60, 96, 145, 131) + head(145, 131, 85, 35);
  } else if (kind === "convergence") {
    drawing = node(45, 45, "A") + node(45, 135, "B") + node(160, 90, "C") +
      line(60, 49, 145, 84) + head(145, 84, 85, 35) +
      line(60, 131, 145, 96) + head(145, 96, 85, -35);
  } else if (kind === "chromatic") {
    // Dark node outlines, but saturated red transition strokes and arrowheads.
    drawing = node(45, 90, "A") + node(160, 90, "B") + node(275, 90, "C") +
      '<line x1="62" y1="90" x2="143" y2="90" stroke="#e63946" stroke-width="2.5"/>' +
      '<path d="M 134 84 L 143 90 L 134 96" fill="none" stroke="#e63946" stroke-width="2.5"/>' +
      '<line x1="177" y1="90" x2="258" y2="90" stroke="#2878d0" stroke-width="2.5"/>' +
      '<path d="M 249 84 L 258 90 L 249 96" fill="none" stroke="#2878d0" stroke-width="2.5"/>';
  } else {
    drawing = node(45, 45, "A") + node(275, 135, "B") +
      node(45, 135, "C") + node(275, 45, "D") +
      line(60, 50, 260, 130) + head(260, 130, 200, 80) +
      line(60, 130, 260, 50) + head(260, 50, 200, -80);
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180">' +
    '<rect width="320" height="180" fill="white"/>' + drawing + '</svg>';
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.setContent("<!doctype html><html><body></body></html>");
    await page.addScriptTag({
      path: path.join(__dirname, "raster_graph_candidate_browser.js")
    });
    await page.addScriptTag({ path: path.join(__dirname, "raster_graph_review_adapter.browser.js") });
    const blank = await page.evaluate(async () => {
      const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="32" height="32" fill="white"/></svg>';
      const source = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
      return globalThis.TGCVRasterGraphCandidateDetector.detectGraphCandidatesFromImage(source);
    });
    assert.equal(blank.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(blank.status, "experimental-candidates-only");
    assert.deepEqual(blank.nodes, []);
    assert.deepEqual(blank.edge_candidates, []);
    assert.ok(blank.limitations.some((item) => item.includes("visual review")));

    // Characterization probes use the actual browser Canvas detector, not a stub.
    // They report current topology recovery without claiming general accuracy.
    const observations = [];
    for (const kind of ["linear", "branch", "convergence", "crossing", "chromatic"]) {
      const detected = await page.evaluate(async (svg) => {
        const source = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
        return globalThis.TGCVRasterGraphCandidateDetector.detectGraphCandidatesFromImage(source);
      }, svgFor(kind));
      assert.equal(detected.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
      assert.equal(detected.status, "experimental-candidates-only");
      assert.ok(Array.isArray(detected.nodes) && Array.isArray(detected.edge_candidates));
      assert.ok(detected.nodes.every((node) => node.review_required === true));
      assert.ok(detected.edge_candidates.every((edge) =>
        edge.review_required === true && edge.direction_status === "unresolved" &&
        edge.direction === "undetermined"));
      assert.ok(detected.nodes.every((node) =>
        node.center.every((coordinate) => Number.isFinite(coordinate))));
      const expectedNodeCount = kind === "crossing" ? 4 : 3;
      assert.equal(detected.nodes.length, expectedNodeCount, kind + ": expected geometric node candidate count; diagnostics=" + JSON.stringify(detected.diagnostics));
      assert.equal(detected.edge_candidates.length, 2, kind + ": expected two geometric edge candidates");
      if (kind === "chromatic") {
        assert.ok(detected.raw_line_candidates.length > 0,
          "chromatic: colored transition strokes must appear in raw geometric line evidence");
      }
      const centersByPosition = detected.nodes.map((node) => node.center)
        .sort((a, b) => a[1] - b[1] || a[0] - b[0]);
      const expectedCenters = kind === "linear" || kind === "chromatic" ? [[45, 90], [160, 90], [275, 90]]
        : kind === "branch" ? [[160, 45], [45, 90], [160, 135]]
        : kind === "convergence" ? [[45, 45], [160, 90], [45, 135]]
        : [[45, 45], [275, 45], [45, 135], [275, 135]];
      assert.deepEqual(centersByPosition, expectedCenters,
        kind + ": node centers should match the authored synthetic layout");
      const reviewDraft = await page.evaluate((graph) =>
        globalThis.TGCVRasterGraphReviewAdapter.candidateGraphToReviewDraft(graph, { sourceName: "probe" }), detected);
      assert.equal(reviewDraft.unresolved_transition_ids.length, reviewDraft.model.transitions.length,
        "direction proposals from the actual detector must remain unresolved for human confirmation");
      assert.deepEqual(reviewDraft.model.transitions.map((edge) => [edge.source, edge.target]),
        kind === "linear" || kind === "chromatic" ? [["N001", "N002"], ["N002", "N003"]]
          : kind === "branch" ? [["N002", "N001"], ["N002", "N003"]]
          : kind === "convergence" ? [["N001", "N002"], ["N003", "N002"]]
          : [["N001", "N004"], ["N003", "N002"]],
        kind + ": conservative resolver proposal should follow the authored arrow geometry");
      observations.push({
        fixture: kind,
        expected_nodes: expectedNodeCount,
        expected_edges: 2,
        detected_nodes: detected.nodes.length,
        detected_edges: detected.edge_candidates.length,
        node_centers: detected.nodes.map((node) => node.center),
        proposed_model_transitions: reviewDraft.model.transitions,
        unresolved_transition_ids: reviewDraft.unresolved_transition_ids
      });
    }
    process.stdout.write("CANVAS-REAL-DETECTOR-CHARACTERIZATION-001 " +
      JSON.stringify(observations) + "\\n");

    const draft = await page.evaluate(() => globalThis.TGCVRasterGraphReviewAdapter.candidateGraphToReviewDraft({
      detector: "TGCV-RASTER-GRAPH-CANDIDATES-001",
      status: "experimental-candidates-only",
      image: { width: 200, height: 100 },
      nodes: [
        { id: "candidate-node-1", center: [30, 50] },
        { id: "candidate-node-2", center: [170, 50] }
      ],
      edge_candidates: [{
        id: "candidate-edge-1",
        source_candidate_node_id: "candidate-node-1",
        target_candidate_node_id: "candidate-node-2",
        direction: "candidate",
        direction_status: "candidate"
      }]
    }, { sourceName: "browser-fixture" }));
    assert.deepEqual(draft.model.states, ["N001", "N002"]);
    assert.equal(draft.model.transitions.length, 1);
    assert.deepEqual(draft.unresolved_transition_ids, ["t_canvas_1"]);
    assert.equal(draft.review.automatic_acceptance, false);
    process.stdout.write("CANVAS-BROWSER-ENTRY-001: native browser Canvas entry point and candidate contract passed.\\n");
  } finally {
    await browser.close();
  }
})().catch((error) => {
  process.stderr.write(String(error && error.stack || error) + "\\n");
  process.exitCode = 1;
});
