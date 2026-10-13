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
  function reportEdgeGeometry(name, result) {
    const reference = referenceByFile.get(name);
    const endpoints = edge => [edge.polyline[0], edge.polyline[edge.polyline.length - 1]];
    const close = (a, b, tolerance = 14) => Math.hypot(a[0] - b[0], a[1] - b[1]) <= tolerance;
    const refs = reference.edges.map(edge => ({ edge, ends: endpoints(edge) }));
    const candidates = result.edge_candidates || [];
    const matchedRef = new Set();
    let matchedCandidates = 0;
    for (const candidate of candidates) {
      const ends = [candidate.from, candidate.to];
      const match = refs.find(({ edge, ends: refEnds }) =>
        close(ends[0], refEnds[0]) && close(ends[1], refEnds[1]) ||
        close(ends[0], refEnds[1]) && close(ends[1], refEnds[0]));
      if (match) {
        matchedCandidates++;
        matchedRef.add(match.edge.id);
      }
    }
    const precision = candidates.length ? matchedCandidates / candidates.length : 0;
    const recall = refs.length ? matchedRef.size / refs.length : 0;
    process.stdout.write(name + ": edge candidate endpoints=" + JSON.stringify(candidates.map(edge => ({ from: edge.from, to: edge.to, support: edge.line_support_ratio }))) + "\\n");
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
    return { precision, recall, candidates: candidates.length, referenceEdges: refs.length };
  }
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
    assertNodeGeometry(name, result);
    reportEdgeGeometry(name, result);
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
    assertNodeGeometry(fixture.name, result);
    reportEdgeGeometry(fixture.name, result);
    process.stdout.write(fixture.name + ": " + result.nodes.length + " provisional candidates on colored-node variant.\\n");
  }
  process.stdout.write("PASS: detector executes on baseline and colored-node raster fixtures; candidates remain provisional.\\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
