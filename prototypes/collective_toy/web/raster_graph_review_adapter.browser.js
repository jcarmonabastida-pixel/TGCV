"use strict";

/**
 * Convert Canvas detector candidates into the existing browser editor's input
 * contract. This adapter deliberately does not infer missing edges or accept
 * directions. Every produced transition remains review-required; callers must
 * carry unresolved_transition_ids into the editor's review state.
 */
function resolveDirectionProposal(edge, options = {}) {
  const evidence = edge && edge.arrowhead_evidence;
  if (evidence && evidence.arrowhead_present === false) return {
    direction: "undetermined", direction_status: "unresolved",
    direction_reason: "No arrowhead is detected; connector direction must remain unresolved."
  };
  const from = evidence && evidence.at_from, to = evidence && evidence.at_to;
  const minSupport = options.minSupport ?? 0.50, minMargin = options.minMargin ?? 0.15;
  const minSamples = options.minSamples ?? 20;
  const valid = score => score && Number.isFinite(score.support_ratio) &&
    score.support_ratio >= 0 && score.support_ratio <= 1 &&
    Number.isInteger(score.tested_samples) && score.tested_samples >= minSamples;
  if (!valid(from) || !valid(to)) return { direction: "undetermined", direction_status: "unresolved",
    direction_reason: "Insufficient arrowhead evidence at one or both endpoints." };
  const fromScore = from.support_ratio, toScore = to.support_ratio;
  const margin = Math.abs(fromScore - toScore);
  if (Math.max(fromScore, toScore) < minSupport || margin < minMargin) return {
    direction: "undetermined", direction_status: "unresolved",
    direction_reason: "Arrowhead evidence is weak or the endpoint scores are too close.",
    direction_evidence: { at_from: fromScore, at_to: toScore, margin }
  };
  const winner = toScore > fromScore ? to : from;
  const minOffAxis = options.minBilateralOffAxisSupport ?? 0.25;
  const minArm = options.minArmSupport ?? 0.50;
  if (!Number.isFinite(winner.off_axis_support_ratio) || winner.off_axis_support_ratio < minOffAxis ||
      !Number.isFinite(winner.left_support_ratio) || winner.left_support_ratio < minArm ||
      !Number.isFinite(winner.right_support_ratio) || winner.right_support_ratio < minArm) return {
    direction: "undetermined", direction_status: "unresolved",
    direction_reason: "Winning endpoint lacks sufficient two-arm arrowhead geometry.",
    direction_evidence: { at_from: fromScore, at_to: toScore, margin }
  };
  return toScore > fromScore
    ? { direction: "source-to-target", direction_status: "candidate",
        direction_reason: "Arrowhead evidence is stronger at the target endpoint; human review required.",
        direction_evidence: { at_from: fromScore, at_to: toScore, margin } }
    : { direction: "target-to-source", direction_status: "candidate",
        direction_reason: "Arrowhead evidence is stronger at the source endpoint; human review required.",
        direction_evidence: { at_from: fromScore, at_to: toScore, margin } };
}

function candidateGraphToReviewDraft(detected, options = {}) {
  if (!detected || detected.detector !== "TGCV-RASTER-GRAPH-CANDIDATES-001") {
    throw new TypeError("Expected TGCV Canvas graph-candidate output.");
  }
  if (!Array.isArray(detected.nodes) || !Array.isArray(detected.edge_candidates)) {
    throw new TypeError("Canvas output must contain nodes and edge_candidates arrays.");
  }
  if (detected.nodes.length === 0) {
    throw new Error("Canvas produced no node candidates; no graph draft was created.");
  }
  if (detected.nodes.length > 500 || detected.edge_candidates.length > 2000) {
    throw new Error("Canvas candidate output exceeds the editor limits (500 nodes / 2000 edges).");
  }

  const usedIds = new Set();
  const nodeByCandidateId = new Map();
  const states = detected.nodes.map((node, index) => {
    if (!node || typeof node.id !== "string" || !Array.isArray(node.center) ||
        node.center.length !== 2 || !node.center.every(Number.isFinite)) {
      throw new TypeError("Malformed Canvas node candidate at index " + index + ".");
    }
    let id = "N" + String(index + 1).padStart(3, "0");
    while (usedIds.has(id)) id += "_";
    usedIds.add(id);
    nodeByCandidateId.set(node.id, id);
    return id;
  });

  const transitions = [];
  const unresolvedTransitionIds = [];
  const seenPairs = new Set();
  for (const edge of detected.edge_candidates) {
    if (!edge || !nodeByCandidateId.has(edge.source_candidate_node_id) ||
        !nodeByCandidateId.has(edge.target_candidate_node_id)) {
      // Do not silently connect an edge whose endpoints cannot be mapped.
      continue;
    }
    const a = nodeByCandidateId.get(edge.source_candidate_node_id);
    const b = nodeByCandidateId.get(edge.target_candidate_node_id);
    if (a === b) continue;
    const pair = [a, b].sort().join("\u0000");
    if (seenPairs.has(pair)) continue;
    seenPairs.add(pair);

    // Geometric direction is a proposal only; explicit human confirmation is
    // still required for every imported edge.
    const proposal = resolveDirectionProposal(edge);
    const fallback = edge.direction_status === "candidate" &&
      ["source-to-target", "target-to-source"].includes(edge.direction) ? edge.direction : "undetermined";
    const direction = proposal.direction_status === "candidate" ? proposal.direction : fallback;
    transitions.push({ id: "t_canvas_" + String(transitions.length + 1),
      source: direction === "target-to-source" ? b : a,
      target: direction === "target-to-source" ? a : b });
    unresolvedTransitionIds.push(transitions[transitions.length - 1].id);
  }

  if (transitions.length === 0) {
    throw new Error("Canvas produced no mappable edge candidates; no graph draft was created.");
  }

  const sourceName = String(options.sourceName || "canvas-image")
    .replace(/[^a-zA-Z0-9_-]/g, "-").slice(0, 50) || "canvas-image";
  const model = {
    schema_version: "collective-toy-input-001",
    model_id: "canvas-review-" + sourceName,
    initial_state: states[0],
    states,
    transitions,
    relations: [],
    rule_profile: { type: "temporal_prerequisite_graph", version: "1" },
    scenarios: [
      { id: "baseline", disabled_transitions: [] },
      { id: "import_check", disabled_transitions: [] }
    ],
    exploration: { max_depth: 100, max_trajectories: 10000 }
  };

  return {
    model,
    unresolved_transition_ids: unresolvedTransitionIds,
    candidate_mapping: Object.fromEntries(nodeByCandidateId),
    review: {
      status: "needs-human-review",
      detector_status: detected.status || "unknown",
      source_image: detected.image || null,
      automatic_acceptance: false,
      note: "Candidate geometry is provisional. Direction proposals are geometric hints only; every edge remains unresolved until explicit human confirmation. Inspect omissions, spurious candidates, crossings and endpoints against the source image."
    }
  };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { candidateGraphToReviewDraft };
} else {
  globalThis.TGCVRasterGraphReviewAdapter = { candidateGraphToReviewDraft, resolveDirectionProposal };
}

