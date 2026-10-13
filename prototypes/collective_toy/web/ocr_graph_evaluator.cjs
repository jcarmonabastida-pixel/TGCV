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
    if (![ "directed", "undirected", "bidirectional", "unknown" ].includes(edge.direction)) throw new Error(label + " contains invalid edge direction");
    if (typeof edge.label !== "string") throw new Error(label + " edge label must be a string");
    if (!ids.has(edge.source) || !ids.has(edge.target)) throw new Error(label + " edge references a missing node: " + edge.source + " -> " + edge.target);
  }
}
function counts(tp, fp, fn) {
  const precision = tp + fp ? tp / (tp + fp) : (fn === 0 ? 1 : 0);
  const recall = tp + fn ? tp / (tp + fn) : (fp === 0 ? 1 : 0);
  return { tp, fp, fn, precision, recall, f1: precision + recall ? 2 * precision * recall / (precision + recall) : 0 };
}
function unorderedPair(a, b) { return a < b ? [a, b] : [b, a]; }
function edgeTopologyKey(edge, map) {
  const s = map.get(edge.source), t = map.get(edge.target);
  if (edge.direction === "undirected") return JSON.stringify([ ...unorderedPair(s, t), edge.direction ]);
  return JSON.stringify([s, t, edge.direction]);
}
function edgeLabelKey(edge, map) {
  return JSON.stringify([edgeTopologyKey(edge, map), edge.label]);
}
function nodeProfile(graph, nodeId) {
  const incoming = graph.edges.filter(e => e.target === nodeId && e.direction === "directed").length;
  const outgoing = graph.edges.filter(e => e.source === nodeId && e.direction === "directed").length;
  const undirected = graph.edges.filter(e => e.direction === "undirected" && (e.source === nodeId || e.target === nodeId)).length;
  const bidirectional = graph.edges.filter(e => e.direction === "bidirectional" && (e.source === nodeId || e.target === nodeId)).length;
  const unknown = graph.edges.filter(e => e.direction === "unknown" && (e.source === nodeId || e.target === nodeId)).length;
  return [incoming, outgoing, undirected, bidirectional, unknown].join(":");
}
function multisetKeys(edges, keyFn) {
  const map = new Map();
  for (const e of edges) { const k = keyFn(e); map.set(k, (map.get(k) || 0) + 1); }
  return map;
}
function multisetCompare(reference, candidate, keyFn) {
  const remaining = multisetKeys(reference, keyFn);
  let tp = 0, fp = 0;
  for (const e of candidate) {
    const k = keyFn(e), n = remaining.get(k) || 0;
    if (n > 0) { tp++; remaining.set(k, n - 1); } else fp++;
  }
  const fn = [...remaining.values()].reduce((a, b) => a + b, 0);
  return { ...counts(tp, fp, fn), remaining };
}
function findTopologyMapping(reference, candidate) {
  if (reference.nodes.length !== candidate.nodes.length) return null;
  const refIds = reference.nodes.map(n => n.id);
  const candIds = candidate.nodes.map(n => n.id);
  const refProfiles = new Map(refIds.map(id => [id, nodeProfile(reference, id)]));
  const candProfiles = new Map(candIds.map(id => [id, nodeProfile(candidate, id)]));
  const candidatesFor = new Map(candIds.map(id => [id, refIds.filter(rid => refProfiles.get(rid) === candProfiles.get(id))]));
  if ([...candidatesFor.values()].some(xs => xs.length === 0)) return null;
  const ordered = [...candIds].sort((a, b) => candidatesFor.get(a).length - candidatesFor.get(b).length);
  const mapping = new Map(), used = new Set();
  function consistent(candId, refId) {
    for (const [otherCand, otherRef] of mapping) {
      const candidatePair = multisetCompare(
        candidate.edges.filter(e => (e.source === candId && e.target === otherCand) || (e.source === otherCand && e.target === candId)),
        reference.edges.filter(e => (e.source === refId && e.target === otherRef) || (e.source === otherRef && e.target === refId)),
        e => {
          let s = e.source === candId || e.source === refId ? "X" : "Y";
          let t = e.target === candId || e.target === refId ? "X" : "Y";
          if (e.direction === "undirected") { const p = unorderedPair(s, t); return JSON.stringify([p, e.direction]); }
          return JSON.stringify([s, t, e.direction]);
        }
      );
      if (candidatePair.fp || candidatePair.fn) return false;
    }
    return true;
  }
  function visit(index) {
    if (index === ordered.length) {
      const candidateKeys = multisetCompare(reference.edges, candidate.edges, e => edgeTopologyKey(e, mapping));
      return candidateKeys.fp === 0 && candidateKeys.fn === 0;
    }
    const candId = ordered[index];
    for (const refId of candidatesFor.get(candId)) {
      if (used.has(refId) || !consistent(candId, refId)) continue;
      mapping.set(candId, refId); used.add(refId);
      if (visit(index + 1)) return true;
      mapping.delete(candId); used.delete(refId);
    }
    return false;
  }
  return visit(0) ? new Map(mapping) : null;
}
function scoreGraph(reference, candidate) {
  assertGraph(reference, "reference");
  assertGraph(candidate, "candidate");
  const mapping = findTopologyMapping(reference, candidate);
  const nodeCountMatch = reference.nodes.length === candidate.nodes.length;
  const topology = mapping
    ? multisetCompare(reference.edges, candidate.edges, e => edgeTopologyKey(e, mapping))
    : counts(0, candidate.edges.length, reference.edges.length);
  let reversedEdges = 0;
  if (!mapping) {
    const refIds = new Set(reference.nodes.map(n => n.id));
    const gotIds = new Set(candidate.nodes.map(n => n.id));
    if ([...refIds].every(id => gotIds.has(id))) {
      const refPairs = new Set(reference.edges.filter(e => e.direction === "directed").map(e => JSON.stringify([e.source, e.target])));
      reversedEdges = candidate.edges.filter(e => e.direction === "directed" &&
        !refPairs.has(JSON.stringify([e.source, e.target])) &&
        refPairs.has(JSON.stringify([e.target, e.source]))).length;
    }
  }
  const mapped = mapping || new Map(candidate.nodes.map(n => [n.id, n.id]));
  const labels = mapping
    ? multisetCompare(reference.edges, candidate.edges, e => edgeLabelKey(e, mapped))
    : counts(0, candidate.edges.length, reference.edges.length);
  const refById = new Map(reference.nodes.map(n => [n.id, n]));
  let nodeLabelErrors = 0;
  if (mapping) for (const n of candidate.nodes) {
    const refNode = refById.get(mapping.get(n.id));
    if (refNode && refNode.label !== n.label) nodeLabelErrors++;
  }
  const criticalFailures = [];
  if (!nodeCountMatch) criticalFailures.push("node_count_mismatch");
  if (reversedEdges) criticalFailures.push("directed_edge_reversal");
  if (topology.fp) criticalFailures.push("spurious_or_duplicate_edges");
  if (topology.fn) criticalFailures.push("missing_edges");
  if (!mapping && nodeCountMatch) criticalFailures.push("topology_correspondence_not_established");
  const exactTopology = Boolean(mapping) && topology.fp === 0 && topology.fn === 0;
  const exactNodeLabels = Boolean(mapping) && nodeLabelErrors === 0;
  const exactEdgeLabels = Boolean(mapping) && labels.fp === 0 && labels.fn === 0;
  return {
    topology_metrics: topology,
    edge_label_metrics: labels,
    node_label_errors: nodeLabelErrors,
    node_count_match: nodeCountMatch,
    topology_match: exactTopology,
    exact_node_labels: exactNodeLabels,
    exact_edge_labels: exactEdgeLabels,
    exact_edge_match: exactEdgeLabels,
    reversed_directed_edges: reversedEdges,
    critical_failures: criticalFailures,
    status: criticalFailures.length ? "CRITICAL_FAIL" : (exactTopology ? "PASS" : "FAIL"),
    semantic_review_required: !exactNodeLabels || !exactEdgeLabels
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
