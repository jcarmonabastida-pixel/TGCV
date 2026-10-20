"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");

(async () => {
  const root = path.join(__dirname, "fixtures", "ocr_graph_images");
  const annotations = JSON.parse(fs.readFileSync(
    path.join(root, "synthetic_graph_image_annotations_v0.1.json"), "utf8"));
  for (const fixture of annotations.images) {
    const imagePath = path.join(root, fixture.file);
    assert.ok(fs.existsSync(imagePath), `OCR-FIXTURE-INTEGRITY-001: missing image ${fixture.file}`);
    const actualSha256 = crypto.createHash("sha256").update(fs.readFileSync(imagePath)).digest("hex");
    assert.equal(actualSha256, fixture.sha256,
      `OCR-FIXTURE-INTEGRITY-001: SHA-256 mismatch for ${fixture.image_id}`);
    assert.ok(Array.isArray(fixture.nodes) && fixture.nodes.length > 0,
      `OCR-FIXTURE-INTEGRITY-001: missing node annotations for ${fixture.image_id}`);
    assert.ok(Array.isArray(fixture.edges) && fixture.edges.length > 0,
      `OCR-FIXTURE-INTEGRITY-001: missing edge annotations for ${fixture.image_id}`);
    for (const edge of fixture.edges) {
      assert.ok(["clear", "ambiguous", "absent"].includes(edge.arrow_status),
        `OCR-FIXTURE-INTEGRITY-001: invalid arrow_status in ${fixture.image_id}/${edge.id}`);
      assert.ok(Array.isArray(edge.polyline) && edge.polyline.length >= 2,
        `OCR-FIXTURE-INTEGRITY-001: invalid centerline in ${fixture.image_id}/${edge.id}`);
    }
  }
  process.stdout.write(`OCR-FIXTURE-INTEGRITY-001: verified ${annotations.images.length} image hashes and annotation contracts.\\n`);
  const rows = [];
  let matched = 0, proposed = 0, correct = 0, inverted = 0, unresolved = 0, unmatched = 0;

  for (const fixture of annotations.images) {
    const result = await detectGraphCandidates(path.join(root, fixture.file));
    const refNodes = fixture.nodes;
    const candidateToReference = new Map();
    for (const candidate of result.nodes || []) {
      if (!candidate.center) continue;
      let best = null, distance = Infinity;
      for (const ref of refNodes) {
        const d = Math.hypot(candidate.center[0] - ref.center[0], candidate.center[1] - ref.center[1]);
        if (d < distance) { best = ref; distance = d; }
      }
      if (best && distance <= 18) candidateToReference.set(candidate.id, best.id);
    }
    const expected = new Map(fixture.edges.map(edge => {
      const key = [edge.source_node_id, edge.target_node_id].sort().join("--");
      return [key, edge];
    }));
    const seen = new Set();
    let fixtureMatched = 0, fixtureProposed = 0, fixtureCorrect = 0,
      fixtureInverted = 0, fixtureUnresolved = 0, fixtureUnmatched = 0;

    for (const edge of result.edge_candidates || []) {
      const from = candidateToReference.get(edge.source_candidate_node_id);
      const to = candidateToReference.get(edge.target_candidate_node_id);
      if (!from || !to) { fixtureUnmatched++; unmatched++; continue; }
      const key = [from, to].sort().join("--");
      const ref = expected.get(key);
      if (!ref || seen.has(key)) { fixtureUnmatched++; unmatched++; continue; }
      seen.add(key); fixtureMatched++; matched++;
      const predictedFrom = edge.direction === "source-to-target" ? from :
        edge.direction === "target-to-source" ? to : null;
      const predictedTo = edge.direction === "source-to-target" ? to :
        edge.direction === "target-to-source" ? from : null;
      const endpointScore = endpoint => {
        if (Array.isArray(endpoint)) {
          return endpoint.reduce((best, item) => !best || item.support_ratio > best.support_ratio ? item : best, null);
        }
        return endpoint || null;
      };
      const evidenceFrom = endpointScore(edge.arrowhead_evidence?.at_from);
      const evidenceTo = endpointScore(edge.arrowhead_evidence?.at_to);
      const evidenceSummary = {
        at_from_support: evidenceFrom?.support_ratio ?? null,
        at_to_support: evidenceTo?.support_ratio ?? null,
        support_margin: evidenceFrom && evidenceTo
          ? Number(Math.abs(evidenceFrom.support_ratio - evidenceTo.support_ratio).toFixed(4)) : null,
        at_from_samples: evidenceFrom?.tested_samples ?? 0,
        at_to_samples: evidenceTo?.tested_samples ?? 0
      };
      if (edge.direction_status !== "candidate" || !predictedFrom || !predictedTo) {
        fixtureUnresolved++; unresolved++;
      } else {
        fixtureProposed++; proposed++;
        if (predictedFrom === ref.source_node_id && predictedTo === ref.target_node_id) {
          fixtureCorrect++; correct++;
        } else {
          fixtureInverted++; inverted++;
        }
      }
    }
    rows.push({
      fixture: fixture.image_id,
      reference_edges: fixture.edges.length,
      matched_edge_candidates: fixtureMatched,
      direction_proposals: fixtureProposed,
      correct_directions: fixtureCorrect,
      inverted_directions: fixtureInverted,
      unresolved_directions: fixtureUnresolved,
      unmatched_or_duplicate_candidates: fixtureUnmatched,
      direction_accuracy_when_proposed: fixtureProposed ? Number((fixtureCorrect / fixtureProposed).toFixed(4)) : null,
      matched_edge_evidence: (result.edge_candidates || []).flatMap(edge => {
        const from = candidateToReference.get(edge.source_candidate_node_id);
        const to = candidateToReference.get(edge.target_candidate_node_id);
        if (!from || !to) return [];
        const key = [from, to].sort().join("--");
        const ref = expected.get(key);
        if (!ref) return [];
        const candidates = endpoint => Array.isArray(endpoint) ? endpoint : endpoint ? [endpoint] : [];
        const best = endpoint => candidates(endpoint)
          .reduce((current, item) => !current || item.support_ratio > current.support_ratio ? item : current, null);
        const atFromCandidates = candidates(edge.arrowhead_hypotheses?.at_from ?? edge.arrowhead_evidence?.at_from);
        const atToCandidates = candidates(edge.arrowhead_hypotheses?.at_to ?? edge.arrowhead_evidence?.at_to);
        const atFrom = best(atFromCandidates);
        const atTo = best(atToCandidates);
        const summarize = item => ({
          support_ratio: item.support_ratio,
          tip_offset_px: item.tip_offset_px,
          angle_degrees: item.angle_degrees,
          left_support_ratio: item.left_support_ratio,
          right_support_ratio: item.right_support_ratio,
          tested_samples: item.tested_samples
        });
        return [{
          reference_edge: ref.id,
          expected_source: ref.source_node_id,
          expected_target: ref.target_node_id,
          candidate_status: edge.direction_status,
          candidate_direction: edge.direction,
          endpoint_scores: {
            at_candidate_from: atFrom?.support_ratio ?? null,
            at_candidate_to: atTo?.support_ratio ?? null,
            absolute_margin: atFrom && atTo ? Number(Math.abs(atFrom.support_ratio - atTo.support_ratio).toFixed(4)) : null,
            at_from_tip_offset_px: atFrom?.tip_offset_px ?? null,
            at_to_tip_offset_px: atTo?.tip_offset_px ?? null,
            at_from_angle_degrees: atFrom?.angle_degrees ?? null,
            at_to_angle_degrees: atTo?.angle_degrees ?? null,
            at_from_left_support: atFrom?.left_support_ratio ?? null,
            at_from_right_support: atFrom?.right_support_ratio ?? null,
            at_to_left_support: atTo?.left_support_ratio ?? null,
            at_to_right_support: atTo?.right_support_ratio ?? null,
            tested_samples_from: atFrom?.tested_samples ?? 0,
            tested_samples_to: atTo?.tested_samples ?? 0
          },
          top_hypotheses_from: atFromCandidates.slice(0, 5).map(summarize),
          top_hypotheses_to: atToCandidates.slice(0, 5).map(summarize)
        }];
      })
    });
  }

  const report = {
    evaluator: "TGCV-OCR-ARROW-DIRECTION-REFERENCE-EVAL-001",
    dataset_id: annotations.dataset_id,
    dataset_version: annotations.dataset_version,
    scope: "synthetic development fixtures only; not real-world validation",
    direction_proposals: proposed,
    correct_directions: correct,
    inverted_directions: inverted,
    unresolved_directions: unresolved,
    unmatched_or_duplicate_candidates: unmatched,
    direction_accuracy_when_proposed: proposed ? Number((correct / proposed).toFixed(4)) : null,
    per_fixture: rows,
    interpretation: "Unresolved directions are not counted as correct. This report measures only matched candidate edges; unmatched candidates are reported separately. Synthetic fixtures are not adjudicated."
  };
  process.stdout.write(JSON.stringify(report, null, 2) + "\\n");
  assert.equal(correct + inverted, proposed, "direction outcome accounting must balance");
  const clearArrowReferenceEdges = annotations.images.flatMap(fixture => fixture.edges || [])
    .filter(edge => edge.direction === "directed" && edge.arrow_status === "clear").length;
  assert.ok(clearArrowReferenceEdges > 0, "reference evaluation requires at least one explicitly clear directed edge");
  assert.ok(proposed > 0,
    "direction evaluation is inconclusive: all explicitly clear directed raster edges remained unresolved; do not report a green direction-evaluation gate");
  assert.equal(rows.length, annotations.images.length, "all annotated fixtures must be evaluated");
})().catch(error => {
  console.error(error && error.stack || error);
  process.exitCode = 1;
});
