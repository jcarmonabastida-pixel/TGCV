"use strict";

/**
 * Convert Canvas detector candidates into the existing browser editor's input
 * contract. This adapter deliberately does not infer missing edges or accept
 * directions. Every produced transition remains review-required; callers must
 * carry unresolved_transition_ids into the editor's review state.
 */
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

    const id = "t_canvas_" + String(transitions.length + 1);
    // The detector's source/target fields are geometric ordering, not validated
    // arrow direction. Preserve the pair but mark it unresolved in editor state.
    transitions.push({ id, source: a, target: b });
    unresolvedTransitionIds.push(id);
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
    rule_profile: { type: "finite_deterministic_graph", version: "1" },
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
      note: "Candidate geometry is provisional. All edge directions remain unresolved; inspect omissions, spurious candidates, crossings and endpoints against the source image."
    }
  };
}

if (typeof module !== "undefined" && module.exports) if (typeof module !== "undefined" && module.exports) module.exports = { candidateGraphToReviewDraft };
else globalThis.TGCVRasterGraphReviewAdapter = { candidateGraphToReviewDraft };
