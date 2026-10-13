"use strict";

const assert = require("node:assert/strict");
const { evaluateStructure, matchNodes } = require("./graph_structure_evaluator.cjs");

const reference = {
  nodes: [
    { id: "A", center: [20, 20] },
    { id: "B", center: [100, 20] },
    { id: "C", center: [60, 80] }
  ],
  edges: [
    { id: "e1", source_node_id: "A", target_node_id: "B" },
    { id: "e2", source_node_id: "A", target_node_id: "C" }
  ]
};
const exact = {
  nodes: [
    { id: "n1", center: [21, 20] },
    { id: "n2", center: [101, 20] },
    { id: "n3", center: [60, 81] }
  ],
  edges: [
    { id: "p1", source_node_id: "n1", target_node_id: "n2" },
    { id: "p2", source_node_id: "n1", target_node_id: "n3" }
  ]
};

const perfect = evaluateStructure(reference, exact);
assert.equal(perfect.node_matches, 3);
assert.equal(perfect.edge_f1, 1);
assert.equal(perfect.critical_topology_error_count, 0);

const crossingPhantom = evaluateStructure(reference, {
  nodes: [...exact.nodes, { id: "phantom-crossing", center: [60, 20] }],
  edges: exact.edges
});
assert.deepEqual(crossingPhantom.spurious_nodes, ["phantom-crossing"]);
assert.equal(crossingPhantom.critical_topology_error_count, 1);

const reversed = evaluateStructure(reference, {
  nodes: exact.nodes,
  edges: [
    { id: "p1", source_node_id: "n2", target_node_id: "n1" },
    { id: "p2", source_node_id: "n1", target_node_id: "n3" }
  ]
});
assert.equal(reversed.reversed_edges.length, 1);
assert.equal(reversed.reversed_edges[0].source, "B");
assert.equal(reversed.reversed_edges[0].target, "A");

const missing = evaluateStructure(reference, { nodes: exact.nodes, edges: [exact.edges[0]] });
assert.equal(missing.missing_edges.length, 1);
assert.equal(missing.missing_edges[0].id, "e2");

const spurious = evaluateStructure(reference, {
  nodes: exact.nodes,
  edges: [...exact.edges, { id: "extra", source_node_id: "n2", target_node_id: "n3" }]
});
assert.equal(spurious.spurious_edges.length, 1);
assert.equal(spurious.spurious_edges[0].id, "extra");

const duplicate = evaluateStructure(reference, {
  nodes: exact.nodes,
  edges: [...exact.edges, { id: "duplicate-e1", source_node_id: "n1", target_node_id: "n2" }]
});
assert.ok(duplicate.duplicate_edges.length >= 1, "duplicate edge must be surfaced");

const emptyReference = matchNodes([], []);
assert.equal(emptyReference.precision, 1);
assert.equal(emptyReference.recall, 1);

process.stdout.write("PASS: structural evaluator detects exact match, phantom node, reversed/missing/spurious/duplicate edges.\n");
