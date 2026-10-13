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
    if (!ids.has(edge.source) || !ids.has(edge.target)) throw new Error(label + " edge references a missing node: " + edge.source + " -> " + edge.target);
  }
}
function counts(tp, fp, fn) {
  const precision = tp + fp ? tp / (tp + fp) : (fn === 0 ? 1 : 0);
  const recall = tp + fn ? tp / (tp + fn) : (fp === 0 ? 1 : 0);
  return { tp, fp, fn, precision, recall, f1: precision + recall ? 2 * precision * recall / (precision + recall) : 0 };
}
function pair(a, b) { return a < b ? [a, b] : [b, a]; }
function topologyKey(e) {
  if (e.direction === "undirected") return JSON.stringify([...pair(e.source, e.target), e.direction]);
  return JSON.stringify([e.source, e.target, e.direction]);
}
function labelledKey(e) { return JSON.stringify([topologyKey(e), e.label]); }
function compareMultisets(reference, candidate, keyFn) {
  const remaining = new Map();
  for (const e of reference) { const k = keyFn(e); remaining.set(k, (remaining.get(k) || 0) + 1); }
  let tp = 0, fp = 0;
  for (const e of candidate) {
    const k = keyFn(e), n = remaining.get(k) || 0;
    if (n) { tp++; remaining.set(k, n - 1); } else fp++;
  }
  const fn = [...remaining.values()].reduce((a, b) => a + b, 0);
  return { ...counts(tp, fp, fn), remaining };
}
function nodeProfile(graph, id) {
  const incident = graph.edges.filter(e => e.source === id || e.target === id);
  return JSON.stringify([
    incident.filter(e => e.direction === "directed" && e.target === id && e.source !== id).length,
    incident.filter(e => e.direction === "directed" && e.source === id && e.target !== id).length,
    incident.filter(e => e.direction === "undirected").length,
    incident.filter(e => e.direction === "bidirectional").length,
    incident.filter(e => e.direction === "unknown").length
  ]);
}
function findTopologyMapping(reference, candidate) {
  if (reference.nodes.length !== candidate.nodes.length) return null;
  const refIds = reference.nodes.map(n => n.id), candIds = candidate.nodes.map(n => n.id);
  const refProfiles = new Map(refIds.map(id => [id, nodeProfile(reference, id)]));
  const candProfiles = new Map(candIds.map(id => [id, nodeProfile(candidate, id)]));
  const refLabels = new Map(refIds.map(id => [id, reference.nodes.find(n => n.id === id).label]));
  const candLabels = new Map(candIds.map(id => [id, candidate.nodes.find(n => n.id === id).label]));
  const options = new Map(candIds.map(id => {
    const labelMatches = refIds.filter(rid => refLabels.get(rid) === candLabels.get(id));
    const structurallyCompatible = refIds.filter(rid => refProfiles.get(rid) === candProfiles.get(id));
    return [id, labelMatches.length === 1 ? labelMatches : structurallyCompatible];
  }));
  if ([...options.values()].some(a => a.length === 0)) return null;
  const order = [...candIds].sort((a, b) => options.get(a).length - options.get(b).length);
  const mapping = new Map(), used = new Set();
  function visit(i) {
    if (i === order.length) {
      const mappedEdges = candidate.edges.map(e => ({ ...e, source: mapping.get(e.source), target: mapping.get(e.target) }));
      const compared = compareMultisets(reference.edges, mappedEdges, topologyKey);
      return compared.fp === 0 && compared.fn === 0;
    }
    const cid = order[i];
    for (const rid of options.get(cid)) {
      if (used.has(rid)) continue;
      mapping.set(cid, rid); used.add(rid);
      if (visit(i + 1)) return true;
      mapping.delete(cid); used.delete(rid);
    }
    return false;
  }
  return visit(0) ? new Map(mapping) : null;
}
function scoreGraph(reference, candidate) {
  assertGraph(reference, "reference");
  assertGraph(candidate, "candidate");
  const nodeCountMatch = reference.nodes.length === candidate.nodes.length;
  const mapping = findTopologyMapping(reference, candidate);
  const mappedEdges = mapping ? candidate.edges.map(e => ({ ...e, source: mapping.get(e.source), target: mapping.get(e.target) })) : candidate.edges;
  const topology = mapping ? compareMultisets(reference.edges, mappedEdges, topologyKey) : counts(0, candidate.edges.length, reference.edges.length);
  const edgeLabels = mapping ? compareMultisets(reference.edges, mappedEdges, labelledKey) : counts(0, candidate.edges.length, reference.edges.length);
  const refById = new Map(reference.nodes.map(n => [n.id, n]));
  let nodeLabelErrors = 0;
  if (mapping) for (const n of candidate.nodes) if (refById.get(mapping.get(n.id)).label !== n.label) nodeLabelErrors++;
  let reversedEdges = 0;
  if (!mapping && nodeCountMatch) {
    const refIds = new Set(reference.nodes.map(n => n.id));
    if (candidate.nodes.every(n => refIds.has(n.id))) {
      const pairs = new Set(reference.edges.filter(e => e.direction === "directed").map(e => JSON.stringify([e.source, e.target])));
      reversedEdges = candidate.edges.filter(e => e.direction === "directed" && !pairs.has(JSON.stringify([e.source, e.target])) && pairs.has(JSON.stringify([e.target, e.source]))).length;
    }
  }
  const criticalFailures = [];
  if (!nodeCountMatch) criticalFailures.push("node_count_mismatch");
  if (reversedEdges) criticalFailures.push("directed_edge_reversal");
  if (topology.fp) criticalFailures.push("spurious_or_duplicate_edges");
  if (topology.fn) criticalFailures.push("missing_edges");
  if (!mapping && nodeCountMatch) criticalFailures.push("topology_correspondence_not_established");
  const exactTopology = Boolean(mapping) && topology.fp === 0 && topology.fn === 0;
  const exactNodeLabels = Boolean(mapping) && nodeLabelErrors === 0;
  const exactEdgeLabels = Boolean(mapping) && edgeLabels.fp === 0 && edgeLabels.fn === 0;
  return {
    topology_metrics: topology,
    edge_label_metrics: edgeLabels,
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
  const report = { protocol_version: data.protocol_version, fixture_count: results.length, passed_expectations: results.filter(r => r.expectation_met).length, all_expectations_met: results.every(r => r.expectation_met), results };
  const serialized = JSON.stringify(report, null, 2) + "\n";
  if (output) fs.writeFileSync(output, serialized);
  process.stdout.write(serialized);
  if (!report.all_expectations_met) process.exitCode = 1;
}
module.exports = { assertGraph, scoreGraph, evaluateCases };
