"use strict";

const assert = require("node:assert/strict");
const { candidateGraphToReviewDraft, resolveDirectionProposal } = require("./raster_graph_review_adapter.cjs");

function fixture(overrides = {}) {
  return {
    detector: "TGCV-RASTER-GRAPH-CANDIDATES-001",
    status: "experimental-candidates-only",
    image: { width: 320, height: 180 },
    nodes: [
      { id: "candidate-node-1", center: [30, 50] },
      { id: "candidate-node-2", center: [150, 50] },
      { id: "candidate-node-3", center: [270, 50] }
    ],
    edge_candidates: [
      { id: "candidate-edge-1", source_candidate_node_id: "candidate-node-1", target_candidate_node_id: "candidate-node-2", direction_status: "candidate", direction: "source-to-target" },
      { id: "candidate-edge-2", source_candidate_node_id: "candidate-node-2", target_candidate_node_id: "candidate-node-3", direction_status: "unresolved", direction: "undetermined" }
    ],
    ...overrides
  };
}

const result = candidateGraphToReviewDraft(fixture(), { sourceName: "diagram 01.png" });
assert.deepEqual(result.model.states, ["N001", "N002", "N003"]);
assert.equal(result.model.transitions.length, 2);
assert.equal(result.model.transitions[0].source, "N001");
assert.equal(result.model.transitions[0].target, "N002");
assert.deepEqual(result.unresolved_transition_ids, ["t_canvas_1", "t_canvas_2"],
  "even a detector direction proposal must remain unresolved until human review");
assert.equal(result.review.automatic_acceptance, false);

const score = (support_ratio, overrides = {}) => ({
  support_ratio, tested_samples: 40, left_support_ratio: 0.8,
  right_support_ratio: 0.8, off_axis_support_ratio: 0.8, ...overrides
});
const forward = resolveDirectionProposal({ arrowhead_evidence: {
  at_from: score(0.1), at_to: score(0.9)
}});
assert.equal(forward.direction, "source-to-target");
assert.equal(forward.direction_status, "candidate");
assert.match(forward.direction_reason, /human review required/);
const reverse = resolveDirectionProposal({ arrowhead_evidence: {
  at_from: score(0.9), at_to: score(0.1)
}});
assert.equal(reverse.direction, "target-to-source");
const weak = resolveDirectionProposal({ arrowhead_evidence: {
  at_from: score(0.48), at_to: score(0.4)
}});
assert.equal(weak.direction, "undetermined");
assert.equal(weak.direction_status, "unresolved");
const noArrow = resolveDirectionProposal({ arrowhead_evidence: {
  arrowhead_present: false, at_from: score(0.9), at_to: score(0.1)
}});
assert.equal(noArrow.direction_status, "unresolved");

const proposedDraft = candidateGraphToReviewDraft(fixture({
  edge_candidates: [{
    id: "candidate-edge-1",
    source_candidate_node_id: "candidate-node-1",
    target_candidate_node_id: "candidate-node-2",
    arrowhead_evidence: { at_from: score(0.1), at_to: score(0.9) }
  }]
}));
assert.deepEqual(proposedDraft.model.transitions, [{ id: "t_canvas_1", source: "N001", target: "N002" }]);
assert.deepEqual(proposedDraft.unresolved_transition_ids, ["t_canvas_1"],
  "direction proposal must never bypass human confirmation");
const reverseDraft = candidateGraphToReviewDraft(fixture({
  edge_candidates: [{
    id: "candidate-edge-1",
    source_candidate_node_id: "candidate-node-1",
    target_candidate_node_id: "candidate-node-2",
    arrowhead_evidence: { at_from: score(0.9), at_to: score(0.1) }
  }]
}));
assert.deepEqual(reverseDraft.model.transitions, [{ id: "t_canvas_1", source: "N002", target: "N001" }]);
assert.deepEqual(reverseDraft.unresolved_transition_ids, ["t_canvas_1"]);
assert.equal(result.model.schema_version, "collective-toy-input-001");
assert.equal(result.model.initial_state, "N001");
assert.equal(result.model.model_id, "canvas-review-diagram-01-png");

const duplicate = candidateGraphToReviewDraft(fixture({
  edge_candidates: [
    { source_candidate_node_id: "candidate-node-1", target_candidate_node_id: "candidate-node-2" },
    { source_candidate_node_id: "candidate-node-2", target_candidate_node_id: "candidate-node-1" }
  ]
}));
assert.equal(duplicate.model.transitions.length, 1, "duplicate undirected pairs must not create duplicate transitions");

assert.throws(() => candidateGraphToReviewDraft({ nodes: [], edge_candidates: [] }), /Expected TGCV Canvas/);
assert.throws(() => candidateGraphToReviewDraft(fixture({ nodes: [] })), /no node candidates/);
assert.throws(() => candidateGraphToReviewDraft(fixture({ edge_candidates: [] })), /no mappable edge candidates/);
assert.throws(() => candidateGraphToReviewDraft(fixture({ nodes: [{ id: "bad", center: [NaN, 2] }] })), /Malformed Canvas node/);

process.stdout.write("CANVAS-REVIEW-ADAPTER-001: model mapping, conservative direction proposals, human-review gating, duplicate suppression and fail-closed inputs passed.\n");
