#!/usr/bin/env node
"use strict";
const fs = require("node:fs");
const path = require("node:path");

function assertGraph(graph, label) {
  if (!graph || !Array.isArray(graph.nodes) || !Array.isArray(graph.edges)) throw new Error(label + " must contain nodes[] and edges[]");
  const ids = new Set();
  for (const node of graph.nodes) {
    if (!node || typeof node.id !== "string" || !node.id || typeof node.label !== "string") throw new Error(label + " contains an invalid node");
    if (ids.has(node.id)) throw new Error(label + " contains duplicate node id: " + node.id);
    ids.add(node.id);
  }
  for (const edge of graph.edges) {
    if (!edge || typeof edge.source !== "string" || typeof edge.target !== "string") throw new Error(label + " contains an invalid edge");
    if (!["directed", "undirected", "bidirectional", "unknown"].includes(edge.direction)) throw new Error(label + " contains invalid edge direction");
    if (typeof edge.label !== "string") throw new Error(label + " edge label must be a string");
  }
}
function edgeKey(edge) {
  const label = edge.label;
  if (edge.direction === "undirected") {
    const ends = [edge.source, edge.target].sort();
    return JSON.stringify([ends[0], ends[1], edge.direction, label]);
  }
  return JSON.stringify([edge.source, edge.target, edge.direction, label]);
}
function counts(tp, fp, fn) {
  const precision = tp + fp ? tp / (tp + fp) : (fn === 0 ? 1 : 0);
  const recall = tp + fn ? tp / (tp + fn) : (fp === 0 ? 1 : 0);
  return { tp, fp, fn, precision, recall, f1: precision + recall ? 2 * precision * recall / (precision + recall) : 0 };
}
function scoreGraph(reference, candidate) {
  assertGraph(reference, "reference");
  assertGraph(candidate, "candidate");
  const refNodes = new Map(reference.nodes.map(n => [n.id, n]));
  const gotNodes = new Map(candidate.nodes.map(n => [n.id, n]));
  let nodeTP = 0, nodeLabelErrors = 0, criticalIdentifierErrors = 0;
  for (const [id, n] of refNodes) {
    const got = gotNodes.get(id);
    if (got && got.label === n.label) nodeTP++;
    if (got && got.label !== n.label) nodeLabelErrors++;
    if (!got && (n.critical_identifier === true || /(?:^|[_-])(?:0|1|O|I|l)/.test(id))) criticalIdentifierErrors++;
  }
  let unknownEndpointEdges = 0;
  for (const edge of candidate.edges) {
    if (!gotNodes.has(edge.source) || !gotNodes.has(edge.target)) unknownEndpointEdges++;
  }
  const refEdgeKeys = reference.edges.map(edgeKey);
  const gotEdgeKeys = candidate.edges.map(edgeKey);
  const remaining = new Map();
  for (const k of refEdgeKeys) remaining.set(k, (remaining.get(k) || 0) + 1);
  let edgeTP = 0, edgeFP = 0;
  for (const k of gotEdgeKeys) {
    const n = remaining.get(k) || 0;
    if (n > 0) { edgeTP++; remaining.set(k, n - 1); }
    else edgeFP++;
  }
  const edgeFN = [...remaining.values()].reduce((a, b) => a + b, 0);
  const refDirectedPairs = new Set(reference.edges.filter(e => e.direction === "directed").map(e => JSON.stringify([e.source,e.target])));
  const gotDirectedPairs = new Set(candidate.edges.filter(e => e.direction === "directed").map(e => JSON.stringify([e.source,e.target])));
  let reversedEdges = 0;
  for (const e of candidate.edges) {
    if (e.direction !== "directed") continue;
    if (!refDirectedPairs.has(JSON.stringify([e.source,e.target])) && refDirectedPairs.has(JSON.stringify([e.target,e.source]))) reversedEdges++;
  }
  const nodeMetrics = counts(nodeTP, candidate.nodes.length - nodeTP, reference.nodes.length - nodeTP);
  const edgeMetrics = counts(edgeTP, edgeFP, edgeFN);
  const exactNodeLabels = nodeTP === reference.nodes.length && candidate.nodes.length === reference.nodes.length;
  const exactEdges = edgeTP === reference.edges.length && edgeFP === 0 && edgeFN === 0;
  const criticalFailures = [];
  if (reversedEdges) criticalFailures.push("directed_edge_reversal");
  if (edgeFP) criticalFailures.push("spurious_or_duplicate_edges");
  if (criticalIdentifierErrors) criticalFailures.push("critical_identifier_missing");
  if (unknownEndpointEdges) criticalFailures.push("edge_endpoint_missing");
  return {
    node_metrics: nodeMetrics,
    edge_metrics: edgeMetrics,
    node_label_errors: nodeLabelErrors,
    exact_node_labels: exactNodeLabels,
    exact_edge_match: exactEdges,
    reversed_directed_edges: reversedEdges,
    unknown_endpoint_edges: unknownEndpointEdges,
    critical_identifier_errors: criticalIdentifierErrors,
    critical_failures: criticalFailures,
    status: criticalFailures.length ? "CRITICAL_FAIL" : (exactNodeLabels && exactEdges ? "PASS" : "FAIL")
  };
}
function evaluateCases(cases) {
  return cases.map(c => {
    const metrics = scoreGraph(c.reference, c.candidate);
    return { id: c.id, expected_status: c.expected_status, ...metrics, expectation_met: metrics.status === c.expected_status };
  });
}
if (require.main === module) {
  const input = process.argv[2] || path.join(__dirname, "ocr_graph_evaluation_fixtures.json");
  const output = process.argv[3];
  const data = JSON.parse(fs.readFileSync(input, "utf8"));
  if (!Array.isArray(data.cases)) throw new Error("Fixture file must contain cases[]");
  const results = evaluateCases(data.cases);
  const report = {
    protocol_version: data.protocol_version,
    fixture_count: results.length,
    passed_expectations: results.filter(r => r.expectation_met).length,
    all_expectations_met: results.every(r => r.expectation_met),
    results
  };
  const serialized = JSON.stringify(report, null, 2) + "\n";
  if (output) fs.writeFileSync(output, serialized);
  process.stdout.write(serialized);
  if (!report.all_expectations_met) process.exitCode = 1;
}
module.exports = { assertGraph, scoreGraph, evaluateCases };
