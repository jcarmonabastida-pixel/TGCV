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
        // Compare candidate tip coordinates against the annotated target tip.
        // tip_offset_px is relative to each candidate endpoint, so it cannot
        // establish proximity to the ground-truth arrow tip.
        const diagnosticReferenceTip = Array.isArray(ref.polyline) ? ref.polyline[ref.polyline.length - 1] : null;
        const candidatesNearReferenceTip = endpoint => endpoint
          .filter(item => diagnosticReferenceTip && Array.isArray(item.tip_candidate))
          .map(item => ({
            ...item,
            reference_tip_error_px: Math.hypot(
              item.tip_candidate[0] - diagnosticReferenceTip[0],
              item.tip_candidate[1] - diagnosticReferenceTip[1]
            )
          }))
          .filter(item => item.reference_tip_error_px <= 4)
          .reduce((current, item) => !current || item.support_ratio > current.support_ratio ? item : current, null);
        const nearFrom = candidatesNearReferenceTip(atFromCandidates);
        const nearTo = candidatesNearReferenceTip(atToCandidates);
        const nearTipDirectionDiagnostic = {
          at_candidate_from_support: nearFrom?.support_ratio ?? null,
          at_candidate_to_support: nearTo?.support_ratio ?? null,
          at_candidate_from_reference_error_px: nearFrom ? Number(nearFrom.reference_tip_error_px.toFixed(3)) : null,
          at_candidate_to_reference_error_px: nearTo ? Number(nearTo.reference_tip_error_px.toFixed(3)) : null,
          favored_endpoint: !nearFrom && !nearTo || (nearFrom && nearTo && nearFrom.support_ratio === nearTo.support_ratio)
            ? "inconclusive" : !nearTo || (nearFrom && nearFrom.support_ratio > nearTo.support_ratio)
              ? "candidate_from" : "candidate_to",
          diagnostic_only: true,
          uses_ground_truth_annotation: true
        };
        // Localization is evaluated separately from direction acceptance.
        // The annotation convention places the reference tip at the final
        // centerline point; compare only hypotheses at the annotated target node.
        const referenceTip = Array.isArray(ref.polyline) ? ref.polyline[ref.polyline.length - 1] : null;
        const targetEndpointHypotheses = to === ref.target_node_id ? atToCandidates :
          from === ref.target_node_id ? atFromCandidates : [];
        const tipErrors = targetEndpointHypotheses.filter(item => Array.isArray(item.tip_candidate))
          .map(item => ({
            error_px: Number(Math.hypot(item.tip_candidate[0] - referenceTip[0], item.tip_candidate[1] - referenceTip[1]).toFixed(3)),
            support_ratio: item.support_ratio,
            tip_offset_px: item.tip_offset_px,
            angle_degrees: item.angle_degrees,
            tip_candidate: item.tip_candidate
          })).sort((a, b) => a.error_px - b.error_px);
        const nearTipHypotheses = tipErrors.filter(item => item.error_px <= 4);
        const bestNearTip = nearTipHypotheses.reduce((current, item) =>
          !current || item.support_ratio > current.support_ratio ? item : current, null);
        const bestOverall = targetEndpointHypotheses.reduce((current, item) =>
          !current || item.support_ratio > current.support_ratio ? item : current, null);
        const summarize = item => ({
          support_ratio: item.support_ratio,
          tip_offset_px: item.tip_offset_px,
          angle_degrees: item.angle_degrees,
          left_support_ratio: item.left_support_ratio,
          right_support_ratio: item.right_support_ratio,
          off_axis_support_ratio: item.off_axis_support_ratio ?? null,
          left_off_axis_support_ratio: item.left_off_axis_support_ratio ?? null,
          right_off_axis_support_ratio: item.right_off_axis_support_ratio ?? null,
          geometric_v_diagnostic: item.geometric_v_diagnostic ?? null,
          tested_samples: item.tested_samples
        });
        return [{
          reference_edge: ref.id,
          expected_source: ref.source_node_id,
          expected_target: ref.target_node_id,
          candidate_status: edge.direction_status,
          candidate_direction: edge.direction,
          near_tip_direction_diagnostic: nearTipDirectionDiagnostic,
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
          reference_tip: referenceTip,
          target_endpoint_tip_localization: {
            hypotheses_evaluated: tipErrors.length,
            best_error_px: tipErrors[0]?.error_px ?? null,
            best_hypothesis: tipErrors[0] ?? null,
            near_tip_hypotheses_evaluated: nearTipHypotheses.length,
            best_near_tip_support_ratio: bestNearTip?.support_ratio ?? null,
            best_near_tip_angle_degrees: bestNearTip?.angle_degrees ?? null,
            best_near_tip_offset_px: bestNearTip?.tip_offset_px ?? null,
            best_overall_support_ratio: bestOverall?.support_ratio ?? null,
            best_overall_offset_px: bestOverall?.tip_offset_px ?? null
          },
          hypothesis_count_from: atFromCandidates.length,
          hypothesis_count_to: atToCandidates.length,
          top_hypotheses_from: atFromCandidates.map(summarize),
          top_hypotheses_to: atToCandidates.map(summarize),
          near_tip_endpoint_comparison: {
            offset_limit_px: 4,
            support_from: atFromCandidates.filter(item => Number.isFinite(item.tip_offset_px) && item.tip_offset_px <= 4)
              .reduce((best, item) => !best || item.support_ratio > best.support_ratio ? item.support_ratio : best, null),
            support_to: atToCandidates.filter(item => Number.isFinite(item.tip_offset_px) && item.tip_offset_px <= 4)
              .reduce((best, item) => !best || item.support_ratio > best.support_ratio ? item.support_ratio : best, null),
            direction_favored_by_near_tip_evidence: (() => {
              const score = endpoint => endpoint.filter(item => Number.isFinite(item.tip_offset_px) && item.tip_offset_px <= 4)
                .reduce((best, item) => !best || item.support_ratio > best ? item.support_ratio : best, null);
              const fromScore = score(atFromCandidates), toScore = score(atToCandidates);
              if (fromScore === null || toScore === null || fromScore === toScore) return "inconclusive";
              return fromScore > toScore ? "candidate_from" : "candidate_to";
            })(),
            off_axis_comparison: (() => {
              const score = endpoint => endpoint.filter(item => Number.isFinite(item.tip_offset_px) && item.tip_offset_px <= 4)
                .reduce((best, item) => !best || (item.off_axis_support_ratio ?? -1) > best ? item.off_axis_support_ratio : best, null);
              const fromScore = score(atFromCandidates), toScore = score(atToCandidates);
              return {
                support_from: fromScore,
                support_to: toScore,
                direction_favored_by_off_axis_evidence: fromScore === null || toScore === null || fromScore === toScore
                  ? "inconclusive"
                  : fromScore > toScore ? "candidate_from" : "candidate_to"
              };
            })(),
            geometric_v_comparison: (() => {
              const score = endpoint => endpoint.filter(item => Number.isFinite(item.tip_offset_px) && item.tip_offset_px <= 4)
                .reduce((best, item) => {
                  const v = item.geometric_v_diagnostic;
                  if (!v) return best;
                  const value = v.bilateral_off_axis_support_ratio;
                  return Number.isFinite(value) && (!best || value > best.score)
                    ? { score: value, vertex_support_ratio: v.vertex_support_ratio, arm_balance_ratio: v.arm_balance_ratio,
                        left_arm_support_ratio: v.left_arm_support_ratio, right_arm_support_ratio: v.right_arm_support_ratio,
                        angle_degrees: item.angle_degrees, tip_offset_px: item.tip_offset_px }
                    : best;
                }, null);
              const from = score(atFromCandidates), to = score(atToCandidates);
              return {
                candidate_from: from,
                candidate_to: to,
                direction_favored_by_geometric_v: !from || !to || from.score === to.score
                  ? "inconclusive"
                  : from.score > to.score ? "candidate_from" : "candidate_to",
                diagnostic_only: true
              };
            })()
          }
        }];
      })
    });
  }

  const localizationRows = rows.flatMap(row => row.matched_edge_evidence || [])
    .map(item => item.target_endpoint_tip_localization || {})
    .filter(item => Number.isFinite(item.best_error_px));
  const localizationErrors = localizationRows.map(item => item.best_error_px).sort((a, b) => a - b);
  const median = values => {
    if (!values.length) return null;
    const middle = Math.floor(values.length / 2);
    return Number((values.length % 2 ? values[middle] : (values[middle - 1] + values[middle]) / 2).toFixed(3));
  };
  const localizationSummary = {
    evaluated_reference_tips: localizationErrors.length,
    median_best_candidate_error_px: median(localizationErrors),
    max_best_candidate_error_px: localizationErrors.length ? localizationErrors[localizationErrors.length - 1] : null,
    within_2px: localizationErrors.filter(error => error <= 2).length,
    within_4px: localizationErrors.filter(error => error <= 4).length,
    note: "Best geometric localization among enumerated hypotheses, not the resolver's selected direction; diagnostic only."
  };
  const nearTipDiagnostics = rows.flatMap(row => row.matched_edge_evidence || [])
    .map(item => item.near_tip_direction_diagnostic || {});
  const nearTipDiagnosticSummary = {
    evaluated_matched_edges: nearTipDiagnostics.length,
    endpoint_from_favored: nearTipDiagnostics.filter(item => item.favored_endpoint === "candidate_from").length,
    endpoint_to_favored: nearTipDiagnostics.filter(item => item.favored_endpoint === "candidate_to").length,
    inconclusive: nearTipDiagnostics.filter(item => item.favored_endpoint === "inconclusive").length,
    note: "Diagnostic comparison using only hypotheses whose tip_candidate lies within 4 px of the annotated reference tip; uses ground truth and is not available to the operational resolver."
  };
  const report = {
    evaluator: "TGCV-OCR-ARROW-DIRECTION-REFERENCE-EVAL-001",
    dataset_id: annotations.dataset_id,
    dataset_version: annotations.dataset_version,
    scope: "synthetic development fixtures only; not real-world validation",
    direction_metrics_kind: "operational_resolver_direction_proposals_compared_with_synthetic_reference",
    direction_resolver_enabled: true,
    automatic_direction_acceptance_enabled: false,
    human_review_required: true,
    direction_proposals: proposed,
    correct_directions: correct,
    inverted_directions: inverted,
    unresolved_directions: unresolved,
    unmatched_or_duplicate_candidates: unmatched,
    direction_accuracy_when_proposed: proposed ? Number((correct / proposed).toFixed(4)) : null,
    target_endpoint_tip_localization_summary: localizationSummary,
    near_tip_direction_diagnostic_summary: nearTipDiagnosticSummary,
    per_fixture: rows,
    interpretation: "The detector invokes the operational resolver to produce direction proposals; this evaluator compares those proposals with non-adjudicated synthetic annotations. Proposals are not accepted directions: automatic acceptance remains disabled and every candidate requires human review. Unresolved directions are not counted as correct. This report measures only matched candidate edges; unmatched candidates are reported separately. The fixtures are synthetic development evidence, not real-world validation."
  };
  assert.equal(correct + inverted, proposed, "direction outcome accounting must balance");
  const clearArrowReferenceEdges = annotations.images.flatMap(fixture => fixture.edges || [])
    .filter(edge => edge.direction === "directed" && edge.arrow_status === "clear").length;
  assert.ok(clearArrowReferenceEdges > 0, "reference evaluation requires at least one explicitly clear directed edge");
  assert.ok(proposed > 0,
    "direction evaluation is inconclusive: all explicitly clear directed raster edges remained unresolved; do not report a green direction-evaluation gate");
  assert.equal(rows.length, annotations.images.length, "all annotated fixtures must be evaluated");
  assert.equal(localizationSummary.evaluated_reference_tips, clearArrowReferenceEdges,
    "every explicitly clear annotated arrow tip must contribute to the localization summary");
  assert.ok(localizationSummary.median_best_candidate_error_px !== null,
    "localization summary must report a median error");
  assert.ok(localizationSummary.max_best_candidate_error_px <= 2,
    "synthetic localization regression: maximum best-candidate tip error must remain <= 2 px");
  assert.equal(localizationSummary.within_2px, localizationSummary.evaluated_reference_tips,
    "synthetic localization regression: every annotated tip must have a candidate within 2 px");
  assert.ok(proposed > 0, "synthetic direction regression: at least one direction must remain evaluable");
  assert.equal(inverted, 0,
    "synthetic direction regression: no confidently proposed direction may contradict the annotated source/target");
  assert.equal(correct, proposed,
    "synthetic direction regression: every proposed direction must match the annotation; uncertain cases may remain unresolved");
  for (const row of rows) {
    const clearEdges = (annotations.images.find(fixture => fixture.image_id === row.fixture)?.edges || [])
      .filter(edge => edge.direction === "directed" && edge.arrow_status === "clear").length;
    const minimumFixtureCoverage = Math.ceil(clearEdges * 0.5);
    assert.ok(row.direction_proposals >= minimumFixtureCoverage,
      `synthetic per-fixture coverage regression for ${row.fixture}: expected at least ${minimumFixtureCoverage}/${clearEdges} proposals (50%); got ${row.direction_proposals}/${clearEdges}`);
    assert.equal(row.inverted_directions, 0,
      `synthetic per-fixture direction regression for ${row.fixture}: no inverted proposals permitted`);
  }
  const minimumProposalCoverage = Math.ceil(clearArrowReferenceEdges * 0.75);
  assert.ok(proposed >= minimumProposalCoverage,
    `synthetic direction coverage regression: expected at least ${minimumProposalCoverage}/${clearArrowReferenceEdges} clear arrows proposed (75%); got ${proposed}/${clearArrowReferenceEdges}`);
  assert.ok(unresolved <= clearArrowReferenceEdges - minimumProposalCoverage,
    "synthetic direction coverage regression: unresolved count exceeds the allowed 25% for this fixture set");
  process.stdout.write(JSON.stringify(report, null, 2) + "\\n");
})().catch(error => {
  console.error(error && error.stack || error);
  process.exitCode = 1;
});
