"use strict";

/**
 * TGCV raster-graph structural evaluator, development-only.
 * Evaluates a detector's proposed graph against fixture annotations.
 * It deliberately does not inspect labels or OCR text.
 */
function distance(a, b) {
  return Math.hypot(a[0] - b[0], a[1] - b[1]);
}

function matchNodes(referenceNodes, predictedNodes, tolerancePx = 12) {
  const candidates = [];
  for (let ri = 0; ri < referenceNodes.length; ri++) {
    for (let pi = 0; pi < predictedNodes.length; pi++) {
      const d = distance(referenceNodes[ri].center, predictedNodes[pi].center);
      if (d <= tolerancePx) candidates.push({ ri, pi, d });
    }
  }
  candidates.sort((a, b) => a.d - b.d);
  const usedR = new Set();
  const usedP = new Set();
  const pairs = [];
  for (const c of candidates) {
    if (usedR.has(c.ri) || usedP.has(c.pi)) continue;
    usedR.add(c.ri); usedP.add(c.pi); pairs.push(c);
  }
  return {
    pairs,
    missed: referenceNodes.filter((_, i) => !usedR.has(i)),
    spurious: predictedNodes.filter((_, i) => !usedP.has(i)),
    precision: predictedNodes.length ? pairs.length / predictedNodes.length : (referenceNodes.length ? 0 : 1),
    recall: referenceNodes.length ? pairs.length / referenceNodes.length : (predictedNodes.length ? 0 : 1)
  };
}

function evaluateStructure(reference, predicted, options = {}) {
  const tolerancePx = options.nodeCenterTolerancePx ?? 12;
  const nodeMatch = matchNodes(reference.nodes || [], predicted.nodes || [], tolerancePx);
  const refIndexToPredId = new Map();
  const predIndexToRefId = new Map();
  for (const pair of nodeMatch.pairs) {
    const refNode = reference.nodes[pair.ri];
    const predNode = predicted.nodes[pair.pi];
    refIndexToPredId.set(refNode.id, predNode.id);
    predIndexToRefId.set(predNode.id, refNode.id);
  }

  const key = (source, target) => source + "\\u0000" + target;
  const refEdges = (reference.edges || []).map(e => ({ source: e.source_node_id, target: e.target_node_id, id: e.id }));
  const predEdges = (predicted.edges || []).map(e => ({
    source: predIndexToRefId.get(e.source_node_id) ?? "UNMATCHED:" + e.source_node_id,
    target: predIndexToRefId.get(e.target_node_id) ?? "UNMATCHED:" + e.target_node_id,
    id: e.id
  }));

  const predictedCounts = new Map();
  for (const e of predEdges) {
    const k = key(e.source, e.target);
    predictedCounts.set(k, (predictedCounts.get(k) || 0) + 1);
  }
  const referenceCounts = new Map();
  for (const e of refEdges) {
    const k = key(e.source, e.target);
    referenceCounts.set(k, (referenceCounts.get(k) || 0) + 1);
  }

  const missingEdges = [];
  const duplicateEdges = [];
  const matchedPredEdgeIndexes = new Set();
  for (const edge of refEdges) {
    const k = key(edge.source, edge.target);
    const count = predictedCounts.get(k) || 0;
    const alreadyUsed = matchedPredEdgeIndexes.size;
    const match = predEdges.findIndex((p, i) => !matchedPredEdgeIndexes.has(i) && key(p.source, p.target) === k);
    if (match >= 0) matchedPredEdgeIndexes.add(match);
    else missingEdges.push(edge);
    if (count > 1) {
      const refs = referenceCounts.get(k) || 0;
      if (count > refs) duplicateEdges.push({ source: edge.source, target: edge.target, excess: count - refs });
      predictedCounts.set(k, 1);
    }
  }

  const reversedEdges = [];
  for (let i = 0; i < predEdges.length; i++) {
    if (matchedPredEdgeIndexes.has(i)) continue;
    const edge = predEdges[i];
    if (refEdges.some(r => r.source === edge.target && r.target === edge.source)) {
      reversedEdges.push({ id: edge.id, source: edge.source, target: edge.target });
      const reverseRef = refEdges.find(r => r.source === edge.target && r.target === edge.source);
      const refKey = key(reverseRef.source, reverseRef.target);
      const missingIndex = missingEdges.findIndex(e => key(e.source, e.target) === refKey);
      if (missingIndex >= 0) missingEdges.splice(missingIndex, 1);
      matchedPredEdgeIndexes.add(i);
    }
  }

  const spuriousEdges = predEdges.filter((_, i) => !matchedPredEdgeIndexes.has(i));
  const expectedEdgeCount = refEdges.length;
  const correctEdgeCount = refEdges.length - missingEdges.length;
  const edgePrecision = predEdges.length ? correctEdgeCount / predEdges.length : (expectedEdgeCount ? 0 : 1);
  const edgeRecall = expectedEdgeCount ? correctEdgeCount / expectedEdgeCount : (predEdges.length ? 0 : 1);
  const f1 = edgePrecision + edgeRecall ? 2 * edgePrecision * edgeRecall / (edgePrecision + edgeRecall) : 0;

  return {
    evaluator: "TGCV-GRAPH-STRUCTURE-EVALUATOR-001",
    status: "development-only-not-a-detector",
    reference_nodes: (reference.nodes || []).length,
    predicted_nodes: (predicted.nodes || []).length,
    node_matches: nodeMatch.pairs.length,
    missed_nodes: nodeMatch.missed.map(n => n.id),
    spurious_nodes: nodeMatch.spurious.map(n => n.id),
    node_precision: nodeMatch.precision,
    node_recall: nodeMatch.recall,
    reference_edges: expectedEdgeCount,
    predicted_edges: predEdges.length,
    correct_edges: correctEdgeCount,
    missing_edges: missingEdges,
    reversed_edges: reversedEdges,
    duplicate_edges: duplicateEdges,
    spurious_edges: spuriousEdges,
    edge_precision: edgePrecision,
    edge_recall: edgeRecall,
    edge_f1: f1,
    critical_topology_error_count: nodeMatch.missed.length + nodeMatch.spurious.length +
      missingEdges.length + reversedEdges.length + duplicateEdges.length + spuriousEdges.length
  };
}

module.exports = { evaluateStructure, matchNodes };
