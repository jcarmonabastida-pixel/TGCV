"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");
const fs = require("node:fs");
const { chromium } = require("playwright");

(async () => {
  const root = path.join(__dirname, "fixtures", "ocr_graph_images");
  const tempRoot = path.join(require("node:os").tmpdir(), "tgcv-colored-node-fixtures");
  fs.mkdirSync(tempRoot, { recursive: true });
  const annotationFile = path.join(root, "synthetic_graph_image_annotations_v0.1.json");
  const annotations = JSON.parse(fs.readFileSync(annotationFile, "utf8"));
  const referenceByFile = new Map(annotations.images.map(item => [path.basename(item.file), item]));
  function summarizeCounts(candidateCount, referenceCount, truePositives) {
    return {
      candidates: candidateCount,
      references: referenceCount,
      true_positives: truePositives,
      false_positives: candidateCount - truePositives,
      false_negatives: referenceCount - truePositives,
      precision: candidateCount > 0 ? truePositives / candidateCount : 0,
      recall: referenceCount > 0 ? truePositives / referenceCount : 0
    };
  }

  function testAggregateMetricEdgeCases() {
    assert.deepEqual(summarizeCounts(0, 0, 0), {
      candidates: 0, references: 0, true_positives: 0,
      false_positives: 0, false_negatives: 0, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: empty graph metrics must be finite and explicit");
    assert.deepEqual(summarizeCounts(0, 3, 0), {
      candidates: 0, references: 3, true_positives: 0,
      false_positives: 0, false_negatives: 3, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: no candidates must yield zero precision and full omissions");
    assert.deepEqual(summarizeCounts(4, 0, 0), {
      candidates: 4, references: 0, true_positives: 0,
      false_positives: 4, false_negatives: 0, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: no references must penalize all proposed candidates");
    assert.deepEqual(summarizeCounts(5, 4, 3), {
      candidates: 5, references: 4, true_positives: 3,
      false_positives: 2, false_negatives: 1, precision: 0.6, recall: 0.75
    }, "METRIC-AGGREGATE-EDGE-CASES-001: ordinary aggregate ratios must be correct");
    process.stdout.write("METRIC-AGGREGATE-EDGE-CASES-001: empty, no-candidate, no-reference and ordinary cases pass.\\n");
  }
  testAggregateMetricEdgeCases();

  function matchEdgesOneToOne(candidates, refs, close) {
    const matchedRef = new Set();
    let matchedCandidates = 0;
    for (const candidate of candidates) {
      const ends = [candidate.from, candidate.to];
      // Each reference edge can explain at most one candidate.
      const match = refs.find(({ edge, ends: refEnds }) => !matchedRef.has(edge.id) && (
        close(ends[0], refEnds[0]) && close(ends[1], refEnds[1]) ||
        close(ends[0], refEnds[1]) && close(ends[1], refEnds[0])));
      if (match) {
        matchedCandidates++;
        matchedRef.add(match.edge.id);
      }
    }
    return { matchedCandidates, matchedReferenceEdges: matchedRef.size, matchedReferenceIds: matchedRef };
  }

  function testOneToOneMetricMatching() {
    const close = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]) <= 1;
    const refs = [
      { edge: { id: "AB" }, ends: [[0,0],[10,0]] },
      { edge: { id: "BC" }, ends: [[10,0],[20,0]] }
    ];
    const edge = (from,to) => ({from,to});
    const duplicateAndMissing = matchEdgesOneToOne([
      edge([0,0],[10,0]), edge([0,0],[10,0]), edge([50,50],[60,60])
    ], refs, close);
    assert.equal(duplicateAndMissing.matchedCandidates, 1,
      "METRIC-ONE-TO-ONE-001: duplicate candidates must not both count as true positives");
    assert.equal(duplicateAndMissing.matchedReferenceEdges, 1,
      "METRIC-ONE-TO-ONE-001: only one reference edge is recovered");
    assert.equal(3 - duplicateAndMissing.matchedCandidates, 2,
      "METRIC-ONE-TO-ONE-001: duplicate and unrelated candidate are false positives");
    assert.equal(2 - duplicateAndMissing.matchedReferenceEdges, 1,
      "METRIC-ONE-TO-ONE-001: unmatched reference edge is a false negative");
    const reversed = matchEdgesOneToOne([edge([10,0],[0,0]), edge([20,0],[10,0])], refs, close);
    assert.equal(reversed.matchedCandidates, 2,
      "METRIC-ONE-TO-ONE-001: undirected geometric matching must tolerate endpoint order");
    assert.equal(reversed.matchedReferenceEdges, 2);
    process.stdout.write("METRIC-ONE-TO-ONE-001: duplicates, false positives, omissions and reversed endpoints scored correctly.\\n");
  }
  testOneToOneMetricMatching();

  function matchNodesOneToOne(candidates, refs, close) {
    const matchedReferenceIds = new Set();
    let matchedCandidates = 0;
    for (const candidate of candidates) {
      const match = refs.find(reference =>
        !matchedReferenceIds.has(reference.id) && close(candidate.center, reference.center));
      if (match) {
        matchedCandidates++;
        matchedReferenceIds.add(match.id);
      }
    }
    return { matchedCandidates, matchedReferenceCount: matchedReferenceIds.size, matchedReferenceIds };
  }

  function testNodeMetricMatching() {
    const close = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]) <= 2;
    const refs = [
      {id:"A",center:[0,0]}, {id:"B",center:[10,0]}, {id:"C",center:[20,0]}
    ];
    const node = (center) => ({center});
    const candidates = matchNodesOneToOne([
      node([0,0]), node([0,0]), node([90,90])
    ], refs, close);
    assert.equal(candidates.matchedCandidates, 1,
      "METRIC-NODE-ONE-TO-ONE-001: duplicate node candidates must not both count as true positives");
    assert.equal(candidates.matchedReferenceCount, 1,
      "METRIC-NODE-ONE-TO-ONE-001: only one reference node is recovered");
    assert.equal(3-candidates.matchedCandidates, 2,
      "METRIC-NODE-ONE-TO-ONE-001: duplicate and unrelated node candidates are false positives");
    assert.equal(3-candidates.matchedReferenceCount, 2,
      "METRIC-NODE-ONE-TO-ONE-001: two reference nodes are missed");
    const allCorrect = matchNodesOneToOne([
      node([0,0]), node([10,0]), node([20,0])
    ], refs, close);
    assert.equal(allCorrect.matchedCandidates, 3,
      "METRIC-NODE-ONE-TO-ONE-001: exact node candidates should all match");
    process.stdout.write("METRIC-NODE-ONE-TO-ONE-001: duplicate nodes, false positives and omissions scored correctly.\\n");
  }
  testNodeMetricMatching();

  function reportEdgeGeometry(name, result, endpointTolerance = 14) {
    const reference = referenceByFile.get(name);
    const endpoints = edge => [edge.polyline[0], edge.polyline[edge.polyline.length - 1]];
    const close = (a, b, tolerance = endpointTolerance) => Math.hypot(a[0] - b[0], a[1] - b[1]) <= tolerance;
    const refs = reference.edges.map(edge => ({ edge, ends: endpoints(edge) }));
    const candidates = result.edge_candidates || [];
    const matching = matchEdgesOneToOne(candidates, refs, close);
    const matchedCandidates = matching.matchedCandidates;
    const matchedRef = matching.matchedReferenceIds;
    const precision = candidates.length ? matchedCandidates / candidates.length : 0;
    const recall = refs.length ? matching.matchedReferenceEdges / refs.length : 0;
    process.stdout.write(name + ": edge candidate endpoints=" + JSON.stringify(candidates.map(edge => ({ from: edge.from, to: edge.to, support: edge.line_support_ratio }))) + "\\n");
    assert.ok(candidates.every(candidate => candidate.direction_status === "unresolved"),
      name + ": direction must remain explicitly unresolved until arrowhead classification is validated");
    const unresolved = candidates.filter(candidate => !candidate.direction || candidate.direction === "undetermined").length;
    assert.equal(candidates.length, refs.length,
      name + ": candidate count must match reference edge count before direction is evaluated");
    assert.equal(matchedRef.size, refs.length,
      name + ": every reference edge must have a geometric candidate before direction is evaluated");
    let arrowTipComparisons = 0, arrowTipWins = 0, arrowTipTies = 0;
    for (const { edge, ends: refEnds } of refs) {
      const candidate = candidates.find(item => {
        const direct = close(item.from, refEnds[0]) && close(item.to, refEnds[1]);
        const reverse = close(item.from, refEnds[1]) && close(item.to, refEnds[0]);
        return direct || reverse;
      });
      if (!candidate || !candidate.arrowhead_evidence) continue;
      const candidateStartsAtSource = close(candidate.from, refEnds[0]);
      const sourceEvidence = candidateStartsAtSource
        ? candidate.arrowhead_evidence.at_from : candidate.arrowhead_evidence.at_to;
      const targetEvidence = candidateStartsAtSource
        ? candidate.arrowhead_evidence.at_to : candidate.arrowhead_evidence.at_from;
      if (!sourceEvidence || !targetEvidence) continue;
      process.stdout.write(name + ": edge " + edge.id + " endpoint arrow evidence source=" +
        sourceEvidence.support_ratio.toFixed(3) + " target=" + targetEvidence.support_ratio.toFixed(3) +
        " (best angles " + sourceEvidence.angle_degrees + "deg/" + targetEvidence.angle_degrees + "deg).\\n");
      arrowTipComparisons++;
      if (targetEvidence.support_ratio > sourceEvidence.support_ratio) arrowTipWins++;
      else if (targetEvidence.support_ratio === sourceEvidence.support_ratio) arrowTipTies++;
    }
    process.stdout.write(name + ": arrow-tip evidence target>source=" + arrowTipWins + "/" +
      arrowTipComparisons + ", ties=" + arrowTipTies +
      ". Diagnostic only; direction inference remains disabled.\\n");
    const directionResolved = candidates.filter(candidate => candidate.direction && candidate.direction !== "undetermined").length;
    process.stdout.write(name + ": directed reference edges=" + refs.filter(({edge}) => edge.direction === "directed").length +
      ", candidates with resolved direction=" + directionResolved + "/" + candidates.length +
      ". Arrowhead/direction quality is not yet gated.\\n");
    process.stdout.write(name + ": edge candidate precision=" + precision.toFixed(3) +
      ", endpoint recall=" + recall.toFixed(3) + ", candidates=" + candidates.length +
      ", reference edges=" + refs.length + ".\\n");
    return { precision, recall, candidates: candidates.length, referenceEdges: refs.length,
      truePositives: matchedCandidates };
  }
  const evaluatedStructuralFixtures = [];
  function assertNodeGeometry(name, result) {
    const reference = referenceByFile.get(name);
    assert.ok(reference, name + ": reference annotation must exist");
    const unmatched = result.nodes.map((node, index) => index);
    let matched = 0;
    for (const expected of reference.nodes) {
      const at = unmatched.findIndex(index => {
        const center = result.nodes[index].center;
        return Math.hypot(center[0] - expected.center[0], center[1] - expected.center[1]) <= 12;
      });
      assert.notEqual(at, -1, name + ": expected node " + expected.id + " missing near " + expected.center.join(","));
      unmatched.splice(at, 1);
      matched++;
    }
    const precision = matched / result.nodes.length;
    const recall = matched / reference.nodes.length;
    assert.equal(recall, 1, name + ": all reference nodes must be recovered");
    assert.equal(unmatched.length, 0, name + ": false-positive node candidates are not allowed in this synthetic gate");
    if (name === "SYN-CROSSING-001.png") {
      assert.ok(!result.nodes.some(node => Math.hypot(node.center[0] - 160, node.center[1] - 90) <= 12),
        "crossing intersection must not be hallucinated as a node");
    }
    process.stdout.write(name + ": node precision=" + precision.toFixed(3) + ", recall=" + recall.toFixed(3) + ".\\n");
    return { precision, recall, candidates: result.nodes.length, referenceNodes: reference.nodes.length,
      truePositives: matched };
  }
  const colorVariants = [
    { name: "SYN-LINEAR-001.png", boxes: [[35,75,65,105],[145,75,175,105],[255,75,285,105]] },
    { name: "SYN-BRANCH-001.png", boxes: [[35,75,65,105],[145,30,175,60],[145,120,175,150],[255,75,285,105]] },
    { name: "SYN-CROSSING-001.png", boxes: [[35,30,65,60],[255,120,285,150],[35,120,65,150],[255,30,285,60]] }
  ];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const fixture of colorVariants) {
      const source = fs.readFileSync(path.join(root, "images", fixture.name));
      const dataUrl = "data:image/png;base64," + source.toString("base64");
      const coloredPng = await browser.newPage().then(async page => {
        const result = await page.evaluate(async ({ dataUrl, boxes }) => {
          const img = new Image(); img.src = dataUrl; await img.decode();
          const canvas = document.createElement("canvas"); canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
          const ctx = canvas.getContext("2d"); ctx.drawImage(img, 0, 0);
          const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const palette = [[205,232,255],[218,245,218],[255,235,190],[235,218,255]];
          boxes.forEach((box, index) => {
            const color = palette[index % palette.length];
            for (let y = box[1] + 2; y < box[3] - 1; y++) for (let x = box[0] + 2; x < box[2] - 1; x++) {
              const i = (y * canvas.width + x) * 4;
              if (pixels.data[i] > 210 && pixels.data[i+1] > 210 && pixels.data[i+2] > 210) {
                pixels.data[i] = color[0]; pixels.data[i+1] = color[1]; pixels.data[i+2] = color[2];
              }
            }
          });
          ctx.putImageData(pixels, 0, 0);
          return canvas.toDataURL("image/png").split(",")[1];
        }, { dataUrl, boxes: fixture.boxes });
        await page.close();
        return Buffer.from(result, "base64");
      });
      fs.writeFileSync(path.join(tempRoot, fixture.name), coloredPng);
    }
  } finally { await browser.close(); }
  // Controlled scale-robustness probe. Scale both raster pixels and reference
  // geometry together; do not treat this probe as a real-image quality claim.
  const scaleProbeName = "SYN-LINEAR-SCALE-150-PCT-001.png";
  const baseName = "SYN-LINEAR-001.png";
  const scaleFactor = 1.5;
  const baseBytes = fs.readFileSync(path.join(root, "images", baseName));
  const baseDataUrl = "data:image/png;base64," + baseBytes.toString("base64");
  const scaleBrowser = await chromium.launch({ headless: true });
  let scaledBytes;
  try {
    const page = await scaleBrowser.newPage();
    const encoded = await page.evaluate(async ({dataUrl, scaleFactor}) => {
      const img = new Image(); img.src = dataUrl; await img.decode();
      const canvas = document.createElement("canvas");
      canvas.width = Math.round(img.naturalWidth * scaleFactor);
      canvas.height = Math.round(img.naturalHeight * scaleFactor);
      const ctx = canvas.getContext("2d");
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      return canvas.toDataURL("image/png").split(",")[1];
    }, {dataUrl: baseDataUrl, scaleFactor});
    scaledBytes = Buffer.from(encoded, "base64");
    await page.close();
  } finally { await scaleBrowser.close(); }
  const scalePath = path.join(tempRoot, scaleProbeName);
  fs.writeFileSync(scalePath, scaledBytes);
  const baseReference = referenceByFile.get(baseName);
  const scaledReference = JSON.parse(JSON.stringify(baseReference));
  scaledReference.file = scaleProbeName;
  scaledReference.nodes = scaledReference.nodes.map(node => ({
    ...node, center: node.center.map(value => value * scaleFactor),
    ...(node.bbox ? {bbox: node.bbox.map(value => value * scaleFactor)} : {})
  }));
  scaledReference.edges = scaledReference.edges.map(edge => ({
    ...edge, polyline: edge.polyline.map(point => point.map(value => value * scaleFactor))
  }));
  referenceByFile.set(scaleProbeName, scaledReference);
  const scaledResult = await detectGraphCandidates(scalePath);
  assert.equal(scaledResult.status, "experimental-candidates-only",
    "SCALE-ROBUSTNESS-001: scaled raster remains provisional");
  assert.equal(scaledResult.image.width, 480, "SCALE-ROBUSTNESS-001: width reflects 150% scale");
  assert.equal(scaledResult.image.height, 270, "SCALE-ROBUSTNESS-001: height reflects 150% scale");
  assert.ok(scaledResult.nodes.length > 0, "SCALE-ROBUSTNESS-001: detector must find nodes at 150% scale");
  assert.ok(scaledResult.nodes.every(node => node.review_required === true),
    "SCALE-ROBUSTNESS-001: scaled candidates still require user review");
  const scaledNodeMetrics = assertNodeGeometry(scaleProbeName, scaledResult);
  // Scale the geometric matching tolerance with the raster so the metric
  // does not penalize the same pixel-localization error more harshly at 150%.
  const scaledEdgeMetrics = reportEdgeGeometry(scaleProbeName, scaledResult, 14 * scaleFactor);
  evaluatedStructuralFixtures.push({fixture: scaleProbeName, scale_factor: scaleFactor,
    node_candidates: scaledNodeMetrics.candidates, reference_nodes: scaledNodeMetrics.referenceNodes,
    node_precision: scaledNodeMetrics.precision, node_recall: scaledNodeMetrics.recall,
    node_true_positives: scaledNodeMetrics.truePositives,
    edge_candidates: scaledEdgeMetrics.candidates, reference_edges: scaledEdgeMetrics.referenceEdges,
    edge_precision: scaledEdgeMetrics.precision, edge_recall: scaledEdgeMetrics.recall,
    edge_true_positives: scaledEdgeMetrics.truePositives, direction_scored: false});
  for (const name of ["SYN-LINEAR-001.png", "SYN-BRANCH-001.png", "SYN-CROSSING-001.png"]) {
    const result = await detectGraphCandidates(path.join(root, "images", name));
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.equal(result.image.width, 320);
    assert.equal(result.image.height, 180);
    assert.ok(Array.isArray(result.nodes));
    assert.ok(Array.isArray(result.edge_candidates));
    if (result.nodes.length === 0) process.stderr.write(name + " diagnostics: " + JSON.stringify(result.diagnostics) + "\\n");
    assert.ok(result.nodes.length > 0, name + ": detector must find at least one provisional node box");
    assert.ok(result.limitations.length >= 3);
    assert.ok(result.nodes.every(n => n.review_required === true));
    const nodeMetrics = assertNodeGeometry(name, result);
    const edgeMetrics = reportEdgeGeometry(name, result);
    evaluatedStructuralFixtures.push({ fixture: name,
      node_candidates: nodeMetrics.candidates, reference_nodes: nodeMetrics.referenceNodes,
      node_precision: nodeMetrics.precision, node_recall: nodeMetrics.recall,
      node_true_positives: nodeMetrics.truePositives,
      edge_candidates: edgeMetrics.candidates, reference_edges: edgeMetrics.referenceEdges,
      edge_precision: edgeMetrics.precision, edge_recall: edgeMetrics.recall,
      edge_true_positives: edgeMetrics.truePositives,
      false_positive_nodes: nodeMetrics.candidates - Math.round(nodeMetrics.precision * nodeMetrics.candidates),
      missed_nodes: nodeMetrics.referenceNodes - Math.round(nodeMetrics.recall * nodeMetrics.referenceNodes),
      false_positive_edges: edgeMetrics.candidates - Math.round(edgeMetrics.precision * edgeMetrics.candidates),
      missed_edges: edgeMetrics.referenceEdges - Math.round(edgeMetrics.recall * edgeMetrics.referenceEdges),
      direction_scored: false });
    process.stdout.write(name + ": " + result.nodes.length + " provisional node candidates; " +
      result.edge_candidates.length + " horizontal stroke candidates.\n");
  }
  for (const fixture of colorVariants) {
    const coloredPath = path.join(tempRoot, fixture.name);
    const result = await detectGraphCandidates(coloredPath);
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.ok(result.nodes.length > 0, fixture.name + ": colored-node variant must yield provisional candidates");
    assert.ok(result.nodes.every(n => n.review_required === true));
    const nodeMetrics = assertNodeGeometry(fixture.name, result);
    const edgeMetrics = reportEdgeGeometry(fixture.name, result);
    evaluatedStructuralFixtures.push({ fixture: fixture.name,
      node_candidates: nodeMetrics.candidates, reference_nodes: nodeMetrics.referenceNodes,
      node_precision: nodeMetrics.precision, node_recall: nodeMetrics.recall,
      edge_candidates: edgeMetrics.candidates, reference_edges: edgeMetrics.referenceEdges,
      edge_precision: edgeMetrics.precision, edge_recall: edgeMetrics.recall,
      false_positive_nodes: nodeMetrics.candidates - Math.round(nodeMetrics.precision * nodeMetrics.candidates),
      missed_nodes: nodeMetrics.referenceNodes - Math.round(nodeMetrics.recall * nodeMetrics.referenceNodes),
      false_positive_edges: edgeMetrics.candidates - Math.round(edgeMetrics.precision * edgeMetrics.candidates),
      missed_edges: edgeMetrics.referenceEdges - Math.round(edgeMetrics.recall * edgeMetrics.referenceEdges),
      direction_scored: false });
    process.stdout.write(fixture.name + ": " + result.nodes.length + " provisional candidates on colored-node variant.\\n");
  }
  // Generated raster fixture: two outlined nodes connected by a plain line,
  // intentionally without arrowheads. This tests the no-arrow import case.
  const noArrowPath = path.join(tempRoot, "SYN-NO-ARROWS-001.png");
  const fixtureBrowser = await chromium.launch({ headless: true });
  try {
    const page = await fixtureBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2); ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(noArrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await fixtureBrowser.close(); }
  const noArrowResult = await detectGraphCandidates(noArrowPath);
  assert.equal(noArrowResult.status, "experimental-candidates-only");
  assert.ok(noArrowResult.nodes.length >= 2,
    "SYN-NO-ARROWS-001: both visible nodes should yield provisional candidates");
  assert.ok(noArrowResult.edge_candidates.length >= 1,
    "SYN-NO-ARROWS-001: plain connecting line should yield a provisional connection");
  assert.ok(noArrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-NO-ARROWS-001: no arrowheads must not produce an invented direction");
  process.stdout.write("SYN-NO-ARROWS-001: nodes=" + noArrowResult.nodes.length +
    ", connections=" + noArrowResult.edge_candidates.length +
    ", all directions unresolved; human review required.\\n");
  // Same topology with differently colored node fills: color must not create
  // an arrow or cause direction to be guessed.
  const coloredNoArrowPath = path.join(tempRoot, "SYN-NO-ARROWS-COLORED-001.png");
  const colorBrowser = await chromium.launch({ headless: true });
  try {
    const page = await colorBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      for (const [x, fill] of [[50, "#8ecae6"], [270, "#ffb703"]]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2); ctx.fillStyle = fill; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(coloredNoArrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await colorBrowser.close(); }
  const coloredNoArrowResult = await detectGraphCandidates(coloredNoArrowPath);
  assert.equal(coloredNoArrowResult.status, "experimental-candidates-only");
  assert.ok(coloredNoArrowResult.nodes.length >= 2,
    "SYN-NO-ARROWS-COLORED-001: both colored nodes should yield provisional candidates");
  assert.ok(coloredNoArrowResult.edge_candidates.length >= 1,
    "SYN-NO-ARROWS-COLORED-001: plain line should yield a provisional connection");
  assert.ok(coloredNoArrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-NO-ARROWS-COLORED-001: colored nodes without arrowheads must not produce an invented direction");
  process.stdout.write("SYN-NO-ARROWS-COLORED-001: nodes=" + coloredNoArrowResult.nodes.length +
    ", connections=" + coloredNoArrowResult.edge_candidates.length +
    ", all directions unresolved; human review required.\\n");
  // Visible arrowhead fixture. The detector must preserve the connection,
  // but must not claim a direction until a validated classifier exists.
  const arrowPath = path.join(tempRoot, "SYN-ARROW-CLEAR-001.png");
  const arrowBrowser = await chromium.launch({ headless: true });
  try {
    const page = await arrowBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      // Clear arrowhead pointing toward the right-hand node.
      ctx.beginPath(); ctx.moveTo(243, 82); ctx.lineTo(255, 90); ctx.lineTo(243, 98); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(arrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await arrowBrowser.close(); }
  const arrowResult = await detectGraphCandidates(arrowPath);
  assert.equal(arrowResult.status, "experimental-candidates-only");
  assert.ok(arrowResult.nodes.length >= 2, "SYN-ARROW-CLEAR-001: both nodes should be detected");
  assert.ok(arrowResult.edge_candidates.length >= 1, "SYN-ARROW-CLEAR-001: arrowed connection should be proposed");
  assert.ok(arrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-ARROW-CLEAR-001: direction remains provisional until validated classification is implemented");
  process.stdout.write("SYN-ARROW-CLEAR-001: nodes=" + arrowResult.nodes.length +
    ", connections=" + arrowResult.edge_candidates.length +
    ", arrow visible but direction remains provisional.\\n");
  // Two opposing arrowheads represent two directed transitions, not an
  // undirected line. Until the classifier is validated, both stay provisional.
  const bidirectionalPath = path.join(tempRoot, "SYN-BIDIRECTIONAL-001.png");
  const bidiBrowser = await chromium.launch({ headless: true });
  try {
    const page = await bidiBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(77, 82); ctx.lineTo(65, 90); ctx.lineTo(77, 98); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(243, 82); ctx.lineTo(255, 90); ctx.lineTo(243, 98); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(bidirectionalPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await bidiBrowser.close(); }
  const bidirectionalResult = await detectGraphCandidates(bidirectionalPath);
  assert.equal(bidirectionalResult.status, "experimental-candidates-only");
  assert.ok(bidirectionalResult.nodes.length >= 2, "SYN-BIDIRECTIONAL-001: both nodes should be detected");
  assert.ok(bidirectionalResult.edge_candidates.length >= 1, "SYN-BIDIRECTIONAL-001: connection should be proposed");
  assert.ok(bidirectionalResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-BIDIRECTIONAL-001: opposing arrows must remain provisional until direction classification is validated");
  process.stdout.write("SYN-BIDIRECTIONAL-001: nodes=" + bidirectionalResult.nodes.length +
    ", connections=" + bidirectionalResult.edge_candidates.length +
    ", opposing arrowheads present; direction classification provisional.\\n");
  // Crossing lines without a junction marker must not automatically be
  // interpreted as a graph node. The current detector is candidate-only, so
  // this fixture records the structural behavior for review.
  const crossingPath = path.join(tempRoot, "SYN-CROSSING-NO-JUNCTION-001.png");
  const crossBrowser = await chromium.launch({ headless: true });
  try {
    const page = await crossBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 220;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 220);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(32, 110); ctx.lineTo(288, 110); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(160, 32); ctx.lineTo(160, 188); ctx.stroke();
      for (const [x,y] of [[20,110],[300,110],[160,20],[160,200]]) {
        ctx.beginPath(); ctx.arc(x, y, 12, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(crossingPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await crossBrowser.close(); }
  const crossingResult = await detectGraphCandidates(crossingPath);
  assert.equal(crossingResult.status, "experimental-candidates-only");
  assert.equal(crossingResult.nodes.length, 4,
    "SYN-CROSSING-NO-JUNCTION-001: exactly four endpoint nodes should be proposed; extra candidates are topological false positives");
  assert.ok(crossingResult.nodes.every(node =>
    Math.hypot(node.center[0] - 160, node.center[1] - 110) > 18),
    "SYN-CROSSING-NO-JUNCTION-001: line intersection must not be proposed as a node");
  assert.equal(crossingResult.edge_candidates.length, 2,
    "SYN-CROSSING-NO-JUNCTION-001: exactly two intended line connections should be proposed; extra candidates are topological false positives");
  const crossingNodesById = new Map(crossingResult.nodes.map(node => [node.id, node]));
  assert.ok(crossingResult.edge_candidates.every(edge => {
    const source = crossingNodesById.get(edge.source_candidate_node_id);
    const target = crossingNodesById.get(edge.target_candidate_node_id);
    if (!source || !target) return false;
    const horizontal = Math.abs(source.center[1] - 110) <= 18 &&
      Math.abs(target.center[1] - 110) <= 18;
    const vertical = Math.abs(source.center[0] - 160) <= 18 &&
      Math.abs(target.center[0] - 160) <= 18;
    return horizontal || vertical;
  }), "SYN-CROSSING-NO-JUNCTION-001: every proposed connection must follow one of the two drawn lines, not a diagonal shortcut");
  assert.ok(crossingResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-CROSSING-NO-JUNCTION-001: crossing geometry must not invent edge direction");
  process.stdout.write("SYN-CROSSING-NO-JUNCTION-001: nodes=" + crossingResult.nodes.length +
    ", connections=" + crossingResult.edge_candidates.length +
    ", no automatic direction inference.\\n");
  // Three-node linear graph: A-B-C. The detector must propose A-B and B-C,
  // but must not add the shortcut A-C through the intervening node.
  const linearPath = path.join(tempRoot, "SYN-LINEAR-3-NODES-001.png");
  const linearBrowser = await chromium.launch({ headless: true });
  try {
    const page = await linearBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(45, 90); ctx.lineTo(315, 90); ctx.stroke();
      for (const x of [35, 180, 325]) {
        ctx.beginPath(); ctx.arc(x, 90, 13, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(linearPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await linearBrowser.close(); }
  const linearResult = await detectGraphCandidates(linearPath);
  assert.equal(linearResult.status, "experimental-candidates-only");
  assert.equal(linearResult.nodes.length, 3,
    "SYN-LINEAR-3-NODES-001: exactly three nodes should be proposed");
  assert.equal(linearResult.edge_candidates.length, 2,
    "SYN-LINEAR-3-NODES-001: exactly two adjacent connections should be proposed; no A-C shortcut");
  const linearNodes = [...linearResult.nodes].sort((a,b) => a.center[0] - b.center[0]);
  const linearPairs = new Set(linearResult.edge_candidates.map(edge => {
    const source = linearResult.nodes.find(node => node.id === edge.source_candidate_node_id);
    const target = linearResult.nodes.find(node => node.id === edge.target_candidate_node_id);
    if (!source || !target) return "invalid";
    return [Math.round(source.center[0]), Math.round(target.center[0])].sort((a,b)=>a-b).join("--");
  }));
  assert.deepEqual(linearPairs, new Set([
    [Math.round(linearNodes[0].center[0]), Math.round(linearNodes[1].center[0])].sort((a,b)=>a-b).join("--"),
    [Math.round(linearNodes[1].center[0]), Math.round(linearNodes[2].center[0])].sort((a,b)=>a-b).join("--")
  ]), "SYN-LINEAR-3-NODES-001: edges must connect adjacent nodes only");
  process.stdout.write("SYN-LINEAR-3-NODES-001: exactly 3 nodes and 2 adjacent connections; no shortcut.\\n");
  // Branched graph: a central node connected to three leaves. Expect one
  // edge per drawn branch and no leaf-to-leaf shortcuts.
  const branchPath = path.join(tempRoot, "SYN-BRANCH-3-LEAVES-001.png");
  const branchBrowser = await chromium.launch({ headless: true });
  try {
    const page = await branchBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath();
        ctx.moveTo(center[0] + dx/len*15, center[1] + dy/len*15);
        ctx.lineTo(x - dx/len*13, y - dy/len*13);
        ctx.stroke();
      }
      for (const [x,y] of [center,...leaves]) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(branchPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await branchBrowser.close(); }
  const branchResult = await detectGraphCandidates(branchPath);
  assert.equal(branchResult.status, "experimental-candidates-only");
  assert.equal(branchResult.nodes.length, 4,
    "SYN-BRANCH-3-LEAVES-001: exactly one center and three leaves should be proposed");
  assert.equal(branchResult.edge_candidates.length, 3,
    "SYN-BRANCH-3-LEAVES-001: exactly three drawn branch connections should be proposed");
  const branchNodes = new Map(branchResult.nodes.map(node => [node.id, node]));
  const centerNode = branchResult.nodes.find(node => Math.hypot(node.center[0]-180,node.center[1]-130) < 18);
  assert.ok(centerNode, "SYN-BRANCH-3-LEAVES-001: central node must be detected");
  assert.ok(branchResult.edge_candidates.every(edge => {
    const source = branchNodes.get(edge.source_candidate_node_id);
    const target = branchNodes.get(edge.target_candidate_node_id);
    return source && target && (source.id === centerNode.id || target.id === centerNode.id);
  }), "SYN-BRANCH-3-LEAVES-001: every edge must touch the center; no leaf-to-leaf shortcuts");
  process.stdout.write("SYN-BRANCH-3-LEAVES-001: exactly 4 nodes and 3 center-to-leaf connections.\\n");
  // Same branched topology with differently colored nodes. Color is visual
  // styling, not a reason to change the graph structure.
  const coloredBranchPath = path.join(tempRoot, "SYN-BRANCH-COLORED-NODES-001.png");
  const coloredBranchBrowser = await chromium.launch({ headless: true });
  try {
    const page = await coloredBranchBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath(); ctx.moveTo(center[0]+dx/len*15,center[1]+dy/len*15);
        ctx.lineTo(x-dx/len*13,y-dy/len*13); ctx.stroke();
      }
      const nodes = [{p:center,c:"#f4a261"},{p:leaves[0],c:"#8ecae6"},
        {p:leaves[1],c:"#90be6d"},{p:leaves[2],c:"#cdb4db"}];
      for (const {p:[x,y],c} of nodes) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle=c; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(coloredBranchPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await coloredBranchBrowser.close(); }
  const coloredBranchResult = await detectGraphCandidates(coloredBranchPath);
  assert.equal(coloredBranchResult.status, "experimental-candidates-only");
  assert.equal(coloredBranchResult.nodes.length, 4,
    "SYN-BRANCH-COLORED-NODES-001: node colors must not change the expected count");
  assert.equal(coloredBranchResult.edge_candidates.length, 3,
    "SYN-BRANCH-COLORED-NODES-001: node colors must not change the expected connection count");
  const coloredCenter = coloredBranchResult.nodes.find(node =>
    Math.hypot(node.center[0]-180,node.center[1]-130) < 18);
  assert.ok(coloredCenter, "SYN-BRANCH-COLORED-NODES-001: central colored node must be detected");
  const coloredNodeMap = new Map(coloredBranchResult.nodes.map(node => [node.id,node]));
  assert.ok(coloredBranchResult.edge_candidates.every(edge => {
    const source=coloredNodeMap.get(edge.source_candidate_node_id);
    const target=coloredNodeMap.get(edge.target_candidate_node_id);
    return source && target && (source.id===coloredCenter.id || target.id===coloredCenter.id);
  }), "SYN-BRANCH-COLORED-NODES-001: colored topology must retain center-to-leaf edges only");
  process.stdout.write("SYN-BRANCH-COLORED-NODES-001: color variation preserves 4-node, 3-edge branch topology.\\n");
  // Consolidated structural summary for the explicit synthetic topology fixtures.
  // Counts are fixture-level diagnostics; existing assertions above verify edge
  // incidence/topology for each graph and do not resolve edge direction.
  const structuralSummary = [
    { fixture: "SYN-CROSSING-NO-JUNCTION-001", expected_nodes: 4, expected_edges: 2, result: crossingResult },
    { fixture: "SYN-LINEAR-3-NODES-001", expected_nodes: 3, expected_edges: 2, result: linearResult },
    { fixture: "SYN-BRANCH-3-LEAVES-001", expected_nodes: 4, expected_edges: 3, result: branchResult },
    { fixture: "SYN-BRANCH-COLORED-NODES-001", expected_nodes: 4, expected_edges: 3, result: coloredBranchResult }
  ].map(({fixture, expected_nodes, expected_edges, result}) => ({
    fixture,
    expected_nodes,
    detected_nodes: result.nodes.length,
    node_count_error: result.nodes.length - expected_nodes,
    expected_edges,
    proposed_edges: result.edge_candidates.length,
    edge_count_error: result.edge_candidates.length - expected_edges,
    counts_match: result.nodes.length === expected_nodes && result.edge_candidates.length === expected_edges,
    direction_evaluation: "not_scored; direction remains unresolved"
  }));
  const structuralSummaryPath = path.join(tempRoot, "raster_graph_structural_summary.json");
  fs.writeFileSync(structuralSummaryPath, JSON.stringify({
    schema_version: "tgcv-raster-structural-summary-0.1",
    status: "synthetic-fixture-evaluation",
    interpretation: "Count metrics are not a substitute for full graph-isomorphism/topology scoring or real-image validation.",
    fixtures: structuralSummary
  }, null, 2) + "\\n");
  process.stdout.write("STRUCTURAL-SUMMARY: " + JSON.stringify(structuralSummary) + "\\n");
  const evaluationReport = {
    schema_version: "tgcv-raster-structural-evaluation-0.3",
    status: "synthetic-and-color-variant-fixtures",
    aggregate: (() => {
      const sum = (key) => evaluatedStructuralFixtures.reduce((total, item) => total + item[key], 0);
      const nodes = summarizeCounts(sum("node_candidates"), sum("reference_nodes"), sum("node_true_positives"));
      const edges = summarizeCounts(sum("edge_candidates"), sum("reference_edges"), sum("edge_true_positives"));
      return {
        fixture_count: evaluatedStructuralFixtures.length,
        node_candidates: nodes.candidates,
        reference_nodes: nodes.references,
        node_true_positives: nodes.true_positives,
        node_false_positives: nodes.false_positives,
        node_false_negatives: nodes.false_negatives,
        node_precision: nodes.precision,
        node_recall: nodes.recall,
        edge_candidates: edges.candidates,
        reference_edges: edges.references,
        edge_true_positives: edges.true_positives,
        edge_false_positives: edges.false_positives,
        edge_false_negatives: edges.false_negatives,
        edge_precision: edges.precision,
        edge_recall: edges.recall,
        direction_scored: false
      };
    })(),
    metrics: { edge_precision: "matched candidate edges / all proposed candidate edges",
      edge_recall: "matched reference edges / all reference edges",
      node_metrics: "asserted independently by geometric matching",
      direction: "not scored; inference disabled" },
    fixtures: evaluatedStructuralFixtures
  };
  const reportPath = path.join(tempRoot, "raster_graph_structural_evaluation.json");
  fs.writeFileSync(reportPath, JSON.stringify(evaluationReport, null, 2) + "\\n");
  process.stdout.write("STRUCTURAL-EVALUATION: " + JSON.stringify(evaluationReport) + "\\n");
  process.stdout.write("PASS: detector executes on baseline and colored-node raster fixtures; candidates remain provisional.\\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
