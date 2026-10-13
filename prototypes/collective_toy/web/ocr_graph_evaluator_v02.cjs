#!/usr/bin/env node
"use strict";
const fs = require("node:fs");
const path = require("node:path");

function assertGraph(graph, name) {
  if (!graph || !Array.isArray(graph.nodes) || !Array.isArray(graph.edges)) throw new Error(name + " must contain nodes[] and edges[]");
  const ids = new Set();
  for (const node of graph.nodes) {
    if (!node || typeof node.id !== "string" || !node.id || typeof node.label !== "string") throw new Error(name + " contains an invalid node");
    if (ids.has(node.id)) throw new Error(name + " contains duplicate node id: " + node.id);
    ids.add(node.id);
  }
  for (const edge of graph.edges) {
    if (!edge || typeof edge.source !== "string" || typeof edge.target !== "string") throw new Error(name + " contains an invalid edge");
    if (!["directed", "undirected", "bidirectional"].includes(edge.direction)) throw new Error(name + " contains invalid/unknown edge direction");
    if (typeof edge.label !== "string") throw new Error(name + " edge label must be a string");
  }
}
function counts(tp, fp, fn) {
  const precision = tp + fp ? tp / (tp + fp) : (fn === 0 ? 1 : 0);
  const recall = tp + fn ? tp / (tp + fn) : (fp === 0 ? 1 : 0);
  return { tp, fp, fn, precision, recall, f1: precision + recall ? 2 * precision * recall / (precision + recall) : 0 };
}
function edgeKey(edge, includeLabel) {
  const ends = edge.direction === "undirected" ? [edge.source, edge.target].sort() : [edge.source, edge.target];
  return JSON.stringify(includeLabel ? [...ends, edge.direction, edge.label] : [...ends, edge.direction]);
}
function multisetCompare(referenceItems, candidateItems, keyFn) {
  const remaining = new Map();
  for (const item of referenceItems) {
    const key = keyFn(item);
    remaining.set(key, (remaining.get(key) || 0) + 1);
  }
  let tp = 0, fp = 0;
  for (const item of candidateItems) {
    const key = keyFn(item), count = remaining.get(key) || 0;
    if (count) { tp++; remaining.set(key, count - 1); } else fp++;
  }
  const fn = [...remaining.values()].reduce((a, b) => a + b, 0);
  return { ...counts(tp, fp, fn), remaining };
}
function scoreGraph(reference, candidate) {
  assertGraph(reference, "reference");
  assertGraph(candidate, "candidate");
  const refNodes = new Map(reference.nodes.map(n => [n.id, n]));
  const gotNodes = new Map(candidate.nodes.map(n => [n.id, n]));
  const nodeTopology = counts(
    [...refNodes.keys()].filter(id => gotNodes.has(id)).length,
    [...gotNodes.keys()].filter(id => !refNodes.has(id)).length,
    [...refNodes.keys()].filter(id => !gotNodes.has(id)).length
  );
  let nodeLabelMatches = 0, nodeLabelErrors = 0, provisionalLabels = 0;
  for (const [id, ref] of refNodes) {
    const got = gotNodes.get(id);
    if (!got) continue;
    if (got.label === ref.label) nodeLabelMatches++;
    else nodeLabelErrors++;
    if (got.provisional_label === true) provisionalLabels++;
  }
  const refEdges = reference.edges;
  const gotEdges = candidate.edges;
  const edgeTopology = multisetCompare(refEdges, gotEdges, e => edgeKey(e, false));
  const edgeLabels = multisetCompare(refEdges, gotEdges, e => edgeKey(e, true));
  let reversedEdges = 0;
  const refDirected = new Set(refEdges.filter(e => e.direction === "directed").map(e => JSON.stringify([e.source, e.target])));
  for (const e of gotEdges) {
    if (e.direction === "directed" && !refDirected.has(JSON.stringify([e.source, e.target])) && refDirected.has(JSON.stringify([e.target, e.source]))) reversedEdges++;
  }
  const unknownEndpointEdges = gotEdges.filter(e => !gotNodes.has(e.source) || !gotNodes.has(e.target)).length;
  const duplicateEdges = Math.max(0, gotEdges.length - new Set(gotEdges.map(e => edgeKey(e, false))).size);
  const missingNodes = nodeTopology.fn;
  const extraNodes = nodeTopology.fp;
  const criticalFailures = [];
  if (reversedEdges) criticalFailures.push("directed_edge_reversal");
  if (unknownEndpointEdges) criticalFailures.push("edge_endpoint_missing");
  if (duplicateEdges) criticalFailures.push("duplicate_edges");
  if (missingNodes || extraNodes) criticalFailures.push("node_set_mismatch");
  const exactTopology = nodeTopology.fp === 0 && nodeTopology.fn === 0 && edgeTopology.fp === 0 && edgeTopology.fn === 0;
  const status = criticalFailures.length ? "CRITICAL_FAIL" : (exactTopology ? "STRUCTURE_PASS" : "STRUCTURE_FAIL");
  return {
    structural_metrics: {
      node_detection: nodeTopology,
      edge_topology: { tp: edgeTopology.tp, fp: edgeTopology.fp, fn: edgeTopology.fn, precision: edgeTopology.precision, recall: edgeTopology.recall, f1: edgeTopology.f1 },
      exact_topology_match: exactTopology,
      missing_nodes: missingNodes,
      extra_nodes: extraNodes,
      missing_edges: edgeTopology.fn,
      extra_edges: edgeTopology.fp,
      duplicate_edges: duplicateEdges,
      reversed_directed_edges: reversedEdges,
      unknown_endpoint_edges: unknownEndpointEdges
    },
    text_metrics: {
      matched_node_count: nodeTopology.tp,
      node_label_exact_matches: nodeLabelMatches,
      node_label_errors: nodeLabelErrors,
      node_label_exact_match_rate: nodeTopology.tp ? nodeLabelMatches / nodeTopology.tp : 1,
      matched_edge_topology_count: edgeTopology.tp,
      edge_label_exact_matches: edgeLabels.tp,
      edge_label_errors: edgeLabels.fp + edgeLabels.fn,
      provisional_labels_on_matched_nodes: provisionalLabels
    },
    critical_failures: criticalFailures,
    status
  };
}
function evaluateCases(cases) {
  return cases.map(c => {
    const metrics = scoreGraph(c.reference, c.candidate);
    return { id: c.id, expected_status: c.expected_status, ...metrics, expectation_met: metrics.status === c.expected_status };
  });
}
if (require.main === module) {
  const input = process.argv[2] || path.join(__dirname, "ocr_graph_evaluation_fixtures_v02.json");
  const output = process.argv[3];
  const data = JSON.parse(fs.readFileSync(input, "utf8"));
  if (!Array.isArray(data.cases)) throw new Error("Fixture file must contain cases[]");
  const results = evaluateCases(data.cases);
  const report = { protocol_version: data.protocol_version, fixture_count: results.length, passed_expectations: results.filter(r => r.expectation_met).length, all_expectations_met: results.every(r => r.expectation_met), results };
  const serialized = JSON.stringify(report, null, 2) + "\n";
  if (output) fs.writeFileSync(output, serialized);
  process.stdout.write(serialized);
  if (!report.all_expectations_met) process.exitCode = 1;
}
module.exports = { assertGraph, scoreGraph, evaluateCases };
