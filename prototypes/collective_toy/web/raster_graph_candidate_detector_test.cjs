"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");
const { detectGraphCandidates } = require("./raster_graph_candidate_detector.cjs");
const fs = require("node:fs");
const { chromium } = require("playwright");

(async () => {
  function testGraphReviewSummaryUiWiring() {
    const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
    for (const id of ["graph-review-summary", "graph-review-summary-text", "graph-review-warnings", "transition-review-list"]) {
      assert.match(html, new RegExp('id="' + id + '"'),
        "GRAPH-REVIEW-UI-WIRING-001: missing review UI element " + id);
    }
    assert.match(html, /function syncGraphEditor\(\)[\s\S]*?summaryText\.textContent=/,
      "GRAPH-REVIEW-UI-WIRING-001: graph editor must recompute the visible summary");
    assert.match(html, /function writeEditedModel\(m,message\)[\s\S]*?syncGraphEditor\(\)/,
      "GRAPH-REVIEW-UI-WIRING-001: model edits must refresh the review summary");
    assert.match(html, /\$\("transition-review-list"\)\.addEventListener\("click"[\s\S]*?writeEditedModel\(m,/,
      "GRAPH-REVIEW-UI-WIRING-001: removing a connection must refresh the summary");
    assert.match(html, /\$\("new-edge-add"\)\.addEventListener\("click"[\s\S]*?writeEditedModel\(m,/,
      "GRAPH-REVIEW-UI-WIRING-001: adding a connection must refresh the summary");
    assert.match(html, /\$\("graph-file"\)\.addEventListener\("change"[\s\S]*?syncGraphEditor\(\)/,
      "GRAPH-REVIEW-UI-WIRING-001: importing a graph must refresh the summary");
    assert.match(html, /No hay aceptación automática|No hay aceptaci[oó]n autom[aá]tica|No se acepta ning[uú]n grafo autom[aá]ticamente/,
      "GRAPH-REVIEW-UI-WIRING-001: interface must explicitly prevent automatic acceptance");
    process.stdout.write("GRAPH-REVIEW-UI-WIRING-001: review summary is present and wired to import/add/remove/edit paths.\\n");
  }
  testGraphReviewSummaryUiWiring();

  const root = path.join(__dirname, "fixtures", "ocr_graph_images");
  const tempRoot = path.join(require("node:os").tmpdir(), "tgcv-colored-node-fixtures");
  fs.mkdirSync(tempRoot, { recursive: true });
  const annotationFile = path.join(root, "synthetic_graph_image_annotations_v0.1.json");
  const annotations = JSON.parse(fs.readFileSync(annotationFile, "utf8"));
  const referenceByFile = new Map(annotations.images.map(item => [path.basename(item.file), item]));
  function summarizeCounts(candidateCount, referenceCount, truePositives) {
    return {
      candidates: candidateCount,
      references: referenceCount,
      true_positives: truePositives,
      false_positives: candidateCount - truePositives,
      false_negatives: referenceCount - truePositives,
      precision: candidateCount > 0 ? truePositives / candidateCount : 0,
      recall: referenceCount > 0 ? truePositives / referenceCount : 0
    };
  }

  function testAggregateMetricEdgeCases() {
    assert.deepEqual(summarizeCounts(0, 0, 0), {
      candidates: 0, references: 0, true_positives: 0,
      false_positives: 0, false_negatives: 0, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: empty graph metrics must be finite and explicit");
    assert.deepEqual(summarizeCounts(0, 3, 0), {
      candidates: 0, references: 3, true_positives: 0,
      false_positives: 0, false_negatives: 3, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: no candidates must yield zero precision and full omissions");
    assert.deepEqual(summarizeCounts(4, 0, 0), {
      candidates: 4, references: 0, true_positives: 0,
      false_positives: 4, false_negatives: 0, precision: 0, recall: 0
    }, "METRIC-AGGREGATE-EDGE-CASES-001: no references must penalize all proposed candidates");
    assert.deepEqual(summarizeCounts(5, 4, 3), {
      candidates: 5, references: 4, true_positives: 3,
      false_positives: 2, false_negatives: 1, precision: 0.6, recall: 0.75
    }, "METRIC-AGGREGATE-EDGE-CASES-001: ordinary aggregate ratios must be correct");
    process.stdout.write("METRIC-AGGREGATE-EDGE-CASES-001: empty, no-candidate, no-reference and ordinary cases pass.\\n");
  }
  testAggregateMetricEdgeCases();

  function scoreTopologyByNodeIdentity(candidateEdges, referenceEdges, nodeMatch) {
    const matchedReferenceIds = new Set();
    let matchedCandidates = 0;
    const key = (a,b) => [a,b].sort().join("|");
    const referenceByPair = new Map(referenceEdges.map(edge =>
      [key(edge.source, edge.target), edge]));
    for (const edge of candidateEdges) {
      const source = nodeMatch.get(edge.source_candidate_node_id);
      const target = nodeMatch.get(edge.target_candidate_node_id);
      if (!source || !target || source === target) continue;
      const reference = referenceByPair.get(key(source,target));
      if (reference && !matchedReferenceIds.has(reference.id)) {
        matchedReferenceIds.add(reference.id);
        matchedCandidates++;
      }
    }
    return {matchedCandidates, matchedReferenceIds, matchedReferenceCount: matchedReferenceIds.size};
  }

  function testTopologyUsesCorrectEndpoints() {
    const nodeMatch = new Map([["a","A"],["b","B"],["c","C"],["d","D"]]);
    const refs = [
      {id:"AB",source:"A",target:"B"},
      {id:"BC",source:"B",target:"C"}
    ];
    const edge = (source_candidate_node_id,target_candidate_node_id) =>
      ({source_candidate_node_id,target_candidate_node_id});
    const correct = scoreTopologyByNodeIdentity([edge("a","b"),edge("b","c")],refs,nodeMatch);
    assert.equal(correct.matchedCandidates,2,
      "TOPOLOGY-ENDPOINTS-001: correctly linked endpoints must match both reference edges");
    // Candidate labels/IDs are arbitrary: topology must be invariant under
    // one-to-one node renaming and endpoint order for undirected structure.
    const renamedNodeMatch = new Map([["x","B"],["y","A"],["z","C"],["w","D"]]);
    const renamed = scoreTopologyByNodeIdentity([
      edge("x","y"), edge("z","x")
    ], refs, renamedNodeMatch);
    assert.equal(renamed.matchedCandidates,2,
      "TOPOLOGY-ENDPOINTS-001: node renaming and reversed endpoint order must preserve undirected topology");
    const sameCountsWrongTopology = scoreTopologyByNodeIdentity([edge("a","c"),edge("b","d")],refs,nodeMatch);
    assert.equal(sameCountsWrongTopology.matchedCandidates,0,
      "TOPOLOGY-ENDPOINTS-001: equal edge counts with wrong endpoints must not score as correct topology");
    const duplicate = scoreTopologyByNodeIdentity([edge("a","b"),edge("a","b")],refs,nodeMatch);
    assert.equal(duplicate.matchedCandidates,1,
      "TOPOLOGY-ENDPOINTS-001: duplicate endpoint pairs must not inflate true positives");
    assert.equal(refs.length - duplicate.matchedReferenceCount,1,
      "TOPOLOGY-ENDPOINTS-001: missing reference endpoint pair must count as a false negative");
    process.stdout.write("TOPOLOGY-ENDPOINTS-001: endpoint identity, wrong topology, and duplicate links scored correctly.\\n");
  }
  testTopologyUsesCorrectEndpoints();

  function matchEdgesOneToOne(candidates, refs, close) {
    const matchedRef = new Set();
    let matchedCandidates = 0;
    for (const candidate of candidates) {
      const ends = [candidate.from, candidate.to];
      // Each reference edge can explain at most one candidate.
      const match = refs.find(({ edge, ends: refEnds }) => !matchedRef.has(edge.id) && (
        close(ends[0], refEnds[0]) && close(ends[1], refEnds[1]) ||
        close(ends[0], refEnds[1]) && close(ends[1], refEnds[0])));
      if (match) {
        matchedCandidates++;
        matchedRef.add(match.edge.id);
      }
    }
    return { matchedCandidates, matchedReferenceEdges: matchedRef.size, matchedReferenceIds: matchedRef };
  }

  function testOneToOneMetricMatching() {
    const close = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]) <= 1;
    const refs = [
      { edge: { id: "AB" }, ends: [[0,0],[10,0]] },
      { edge: { id: "BC" }, ends: [[10,0],[20,0]] }
    ];
    const edge = (from,to) => ({from,to});
    const duplicateAndMissing = matchEdgesOneToOne([
      edge([0,0],[10,0]), edge([0,0],[10,0]), edge([50,50],[60,60])
    ], refs, close);
    assert.equal(duplicateAndMissing.matchedCandidates, 1,
      "METRIC-ONE-TO-ONE-001: duplicate candidates must not both count as true positives");
    assert.equal(duplicateAndMissing.matchedReferenceEdges, 1,
      "METRIC-ONE-TO-ONE-001: only one reference edge is recovered");
    assert.equal(3 - duplicateAndMissing.matchedCandidates, 2,
      "METRIC-ONE-TO-ONE-001: duplicate and unrelated candidate are false positives");
    assert.equal(2 - duplicateAndMissing.matchedReferenceEdges, 1,
      "METRIC-ONE-TO-ONE-001: unmatched reference edge is a false negative");
    const reversed = matchEdgesOneToOne([edge([10,0],[0,0]), edge([20,0],[10,0])], refs, close);
    assert.equal(reversed.matchedCandidates, 2,
      "METRIC-ONE-TO-ONE-001: undirected geometric matching must tolerate endpoint order");
    assert.equal(reversed.matchedReferenceEdges, 2);
    process.stdout.write("METRIC-ONE-TO-ONE-001: duplicates, false positives, omissions and reversed endpoints scored correctly.\\n");
  }
  testOneToOneMetricMatching();

  function matchNodesOneToOne(candidates, refs, close) {
    const matchedReferenceIds = new Set();
    let matchedCandidates = 0;
    for (const candidate of candidates) {
      const match = refs.find(reference =>
        !matchedReferenceIds.has(reference.id) && close(candidate.center, reference.center));
      if (match) {
        matchedCandidates++;
        matchedReferenceIds.add(match.id);
      }
    }
    return { matchedCandidates, matchedReferenceCount: matchedReferenceIds.size, matchedReferenceIds };
  }

  function testNodeMetricMatching() {
    const close = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]) <= 2;
    const refs = [
      {id:"A",center:[0,0]}, {id:"B",center:[10,0]}, {id:"C",center:[20,0]}
    ];
    const node = (center) => ({center});
    const candidates = matchNodesOneToOne([
      node([0,0]), node([0,0]), node([90,90])
    ], refs, close);
    assert.equal(candidates.matchedCandidates, 1,
      "METRIC-NODE-ONE-TO-ONE-001: duplicate node candidates must not both count as true positives");
    assert.equal(candidates.matchedReferenceCount, 1,
      "METRIC-NODE-ONE-TO-ONE-001: only one reference node is recovered");
    assert.equal(3-candidates.matchedCandidates, 2,
      "METRIC-NODE-ONE-TO-ONE-001: duplicate and unrelated node candidates are false positives");
    assert.equal(3-candidates.matchedReferenceCount, 2,
      "METRIC-NODE-ONE-TO-ONE-001: two reference nodes are missed");
    const allCorrect = matchNodesOneToOne([
      node([0,0]), node([10,0]), node([20,0])
    ], refs, close);
    assert.equal(allCorrect.matchedCandidates, 3,
      "METRIC-NODE-ONE-TO-ONE-001: exact node candidates should all match");
    process.stdout.write("METRIC-NODE-ONE-TO-ONE-001: duplicate nodes, false positives and omissions scored correctly.\\n");
  }
  testNodeMetricMatching();

  function testTopologyReportRejectsWrongEndpoints() {
    const fixtureName = "SYN-TOPOLOGY-WRONG-ENDPOINTS-001";
    referenceByFile.set(fixtureName, {
      nodes: [
        {id:"A",center:[40,40]}, {id:"B",center:[100,40]},
        {id:"C",center:[160,40]}, {id:"D",center:[220,40]}
      ],
      edges: [
        {id:"AB",source_node_id:"A",target_node_id:"B"},
        {id:"BC",source_node_id:"B",target_node_id:"C"}
      ]
    });
    const candidate = {
      nodes: [
        {id:"a",center:[40,40]}, {id:"b",center:[100,40]},
        {id:"c",center:[160,40]}, {id:"d",center:[220,40]}
      ],
      // Same node and edge counts as the reference, deliberately wrong pairs.
      edge_candidates: [
        {source_candidate_node_id:"a",target_candidate_node_id:"c"},
        {source_candidate_node_id:"b",target_candidate_node_id:"d"}
      ]
    };
    const metrics = reportTopologyByNodeIdentity(fixtureName,candidate);
    assert.equal(metrics.matched_node_identities,4,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: all four node identities should match geometrically");
    assert.equal(metrics.topology_edge_true_positives,0,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: wrong endpoint pairs must yield zero true positives");
    assert.equal(metrics.topology_edge_false_positives,2,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: both incorrect candidate edges must be false positives");
    assert.equal(metrics.topology_edge_false_negatives,2,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: both reference edges must be reported missing");
    assert.equal(metrics.topology_edge_precision,0,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: precision must be zero for entirely wrong topology");
    assert.equal(metrics.topology_edge_recall,0,
      "TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: recall must be zero when no reference edge is recovered");
    referenceByFile.delete(fixtureName);
    process.stdout.write("TOPOLOGY-REPORT-WRONG-ENDPOINTS-001: report detects wrong topology despite matching counts.\\n");
  }

  function reportTopologyByNodeIdentity(name, result) {
    const reference = referenceByFile.get(name);
    const unmatchedRefs = new Set(reference.nodes.map(node => node.id));
    const candidateToReference = new Map();
    for (const candidate of result.nodes) {
      const nearest = reference.nodes
        .map(node => ({node, distance: Math.hypot(candidate.center[0]-node.center[0], candidate.center[1]-node.center[1])}))
        .filter(item => unmatchedRefs.has(item.node.id) && item.distance <= 12)
        .sort((a,b) => a.distance-b.distance)[0];
      if (nearest) {
        candidateToReference.set(candidate.id, nearest.node.id);
        unmatchedRefs.delete(nearest.node.id);
      }
    }
    const pairKey = (a,b) => [a,b].sort().join("|");
    const referencePairs = new Set(reference.edges.map(edge => pairKey(edge.source_node_id, edge.target_node_id)));
    const matchedPairs = new Set();
    let matchedCandidateEdges = 0;
    for (const edge of (result.edge_candidates || [])) {
      const source = candidateToReference.get(edge.source_candidate_node_id);
      const target = candidateToReference.get(edge.target_candidate_node_id);
      if (!source || !target || source === target) continue;
      const pair = pairKey(source,target);
      if (referencePairs.has(pair) && !matchedPairs.has(pair)) {
        matchedPairs.add(pair);
        matchedCandidateEdges++;
      }
    }
    const candidateCount = (result.edge_candidates || []).length;
    const referenceCount = reference.edges.length;
    return {
      matched_node_identities: candidateToReference.size,
      reference_nodes: reference.nodes.length,
      topology_edge_true_positives: matchedCandidateEdges,
      topology_edge_false_positives: candidateCount - matchedCandidateEdges,
      topology_edge_false_negatives: referenceCount - matchedPairs.size,
      topology_edge_precision: candidateCount ? matchedCandidateEdges / candidateCount : 0,
      topology_edge_recall: referenceCount ? matchedPairs.size / referenceCount : 0,
      topology_scoring: "undirected endpoint identity; node matches are geometric and one-to-one"
    };
  }

  function buildGraphReviewSummary(graphs) {
    const items = graphs.map(graph => ({
      graph_id: graph.graph_id,
      ...classifyGraphCandidate(graph.edges)
    }));
    return {
      graph_count: items.length,
      incomplete_graph_count: items.filter(item => item.graph_status === "incomplete").length,
      needs_review_graph_count: items.filter(item => item.graph_status === "needs_review").length,
      review_ready_graph_count: items.filter(item => item.graph_status === "review_ready").length,
      graphs: items,
      automatic_acceptance: false
    };
  }

  function testGraphReviewSummary() {
    const resolved = {topology_status:"detected",direction_status:"resolved",direction:"A_to_B",confidence:0.99,review_required:false};
    const ambiguous = {topology_status:"ambiguous",direction_status:"unresolved",confidence:0.55,review_required:true};
    const summary = buildGraphReviewSummary([
      {graph_id:"G1",edges:[resolved]},
      {graph_id:"G2",edges:[resolved,ambiguous]},
      {graph_id:"G3",edges:[]}
    ]);
    assert.equal(summary.graph_count,3);
    assert.equal(summary.review_ready_graph_count,1);
    assert.equal(summary.needs_review_graph_count,1);
    assert.equal(summary.incomplete_graph_count,1);
    assert.equal(summary.automatic_acceptance,false);
    assert.deepEqual(summary.graphs.map(g=>g.graph_id),["G1","G2","G3"],
      "GRAPH-REVIEW-SUMMARY-001: graph-specific review entries must preserve input order and identity");
    process.stdout.write("GRAPH-REVIEW-SUMMARY-001: summary lists each graph and counts review states without auto-acceptance.\\n");
  }
  testGraphReviewSummary();

  function classifyGraphCandidate(edges) {
    const classifications = edges.map(classifyEdgeCandidate);
    const reviewCount = classifications.filter(edge => edge.review_required).length;
    const ambiguousCount = classifications.filter(edge => edge.structural_status === "ambiguous").length;
    const unresolvedCount = classifications.filter(edge => edge.structural_status === "unresolved").length;
    const directionUnresolvedCount = classifications.filter(edge => edge.direction_status === "unresolved").length;
    let status = "review_ready";
    if (edges.length === 0 || unresolvedCount > 0) status = "incomplete";
    else if (reviewCount > 0 || ambiguousCount > 0) status = "needs_review";
    return {
      graph_status: status,
      edge_count: classifications.length,
      review_required_edge_count: reviewCount,
      ambiguous_edge_count: ambiguousCount,
      unresolved_edge_count: unresolvedCount,
      direction_unresolved_edge_count: directionUnresolvedCount,
      can_auto_accept: false,
      edge_classifications: classifications
    };
  }

  function testGraphCandidateClassification() {
    const detected = {topology_status:"detected",direction_status:"resolved",direction:"A_to_B",confidence:0.99,review_required:false};
    const unresolvedDirection = {topology_status:"detected",direction_status:"unresolved",confidence:0.98,review_required:false};
    const ambiguous = {topology_status:"ambiguous",direction_status:"unresolved",confidence:0.55,review_required:true};
    const unresolved = {topology_status:"unresolved",direction_status:"unresolved",confidence:null,review_required:true};
    const ready = classifyGraphCandidate([detected]);
    assert.equal(ready.graph_status,"review_ready",
      "GRAPH-REVIEW-STATE-001: graph with resolved candidates should be marked ready for human review");
    assert.equal(ready.can_auto_accept,false,
      "GRAPH-REVIEW-STATE-001: classification must never automatically accept a graph");
    const directionUnknown = classifyGraphCandidate([unresolvedDirection]);
    assert.equal(directionUnknown.graph_status,"needs_review",
      "GRAPH-REVIEW-STATE-001: unresolved direction must route graph to review");
    assert.equal(directionUnknown.direction_unresolved_edge_count,1);
    const needsReview = classifyGraphCandidate([detected,ambiguous]);
    assert.equal(needsReview.graph_status,"needs_review");
    assert.equal(needsReview.review_required_edge_count,1);
    assert.equal(needsReview.ambiguous_edge_count,1);
    const incomplete = classifyGraphCandidate([detected,unresolved]);
    assert.equal(incomplete.graph_status,"incomplete",
      "GRAPH-REVIEW-STATE-001: unresolved structural edge must mark graph incomplete");
    assert.equal(incomplete.unresolved_edge_count,1);
    assert.equal(classifyGraphCandidate([]).graph_status,"incomplete",
      "GRAPH-REVIEW-STATE-001: empty graph must not be marked ready");
    process.stdout.write("GRAPH-REVIEW-STATE-001: graph states combine edge uncertainty without auto-acceptance.\\n");
  }
  testGraphCandidateClassification();

  function classifyEdgeCandidate(edge) {
    const direction = edge.direction_status === "resolved" && edge.direction
      ? "resolved" : "unresolved";
    const confidence = Number.isFinite(edge.confidence) ? edge.confidence : null;
    const reviewRequired = edge.review_required !== false ||
      edge.topology_status === "ambiguous" || direction === "unresolved" ||
      confidence === null || confidence < 0.9;
    let structuralStatus = "detected";
    if (edge.topology_status === "ambiguous") structuralStatus = "ambiguous";
    else if (edge.topology_status === "unresolved") structuralStatus = "unresolved";
    return {
      structural_status: structuralStatus,
      direction_status: direction,
      confidence,
      review_required: reviewRequired
    };
  }

  function testEdgeCandidateClassification() {
    const certainUndirected = classifyEdgeCandidate({
      topology_status:"detected", direction_status:"unresolved",
      direction:"undetermined", confidence:0.97, review_required:false
    });
    assert.equal(certainUndirected.structural_status,"detected");
    assert.equal(certainUndirected.direction_status,"unresolved");
    assert.equal(certainUndirected.review_required,true,
      "EDGE-UNCERTAINTY-CLASSIFICATION-001: unresolved direction must remain reviewable");
    const ambiguous = classifyEdgeCandidate({
      topology_status:"ambiguous", direction_status:"unresolved",
      confidence:0.55, review_required:true
    });
    assert.equal(ambiguous.structural_status,"ambiguous");
    assert.equal(ambiguous.review_required,true);
    const missingConfidence = classifyEdgeCandidate({
      topology_status:"detected", direction_status:"unresolved"
    });
    assert.equal(missingConfidence.confidence,null);
    assert.equal(missingConfidence.review_required,true,
      "EDGE-UNCERTAINTY-CLASSIFICATION-001: missing confidence must not be treated as certainty");
    const directed = classifyEdgeCandidate({
      topology_status:"detected", direction_status:"resolved",
      direction:"A_to_B", confidence:0.99, review_required:false
    });
    assert.equal(directed.direction_status,"resolved");
    assert.equal(directed.review_required,false);
    process.stdout.write("EDGE-UNCERTAINTY-CLASSIFICATION-001: structural ambiguity, direction, confidence, and review remain separate.\\n");
  }
  testEdgeCandidateClassification();

  function reportEdgeGeometry(name, result, endpointTolerance = 14) {
    const reference = referenceByFile.get(name);
    const endpoints = edge => [edge.polyline[0], edge.polyline[edge.polyline.length - 1]];
    const close = (a, b, tolerance = endpointTolerance) => Math.hypot(a[0] - b[0], a[1] - b[1]) <= tolerance;
    const refs = reference.edges.map(edge => ({ edge, ends: endpoints(edge) }));
    const candidates = result.edge_candidates || [];
    const matching = matchEdgesOneToOne(candidates, refs, close);
    const matchedCandidates = matching.matchedCandidates;
    const matchedRef = matching.matchedReferenceIds;
    const precision = candidates.length ? matchedCandidates / candidates.length : 0;
    const recall = refs.length ? matching.matchedReferenceEdges / refs.length : 0;
    process.stdout.write(name + ": edge candidate endpoints=" + JSON.stringify(candidates.map(edge => ({ from: edge.from, to: edge.to, support: edge.line_support_ratio }))) + "\\n");
    assert.ok(candidates.every(candidate => candidate.direction_status === "unresolved"),
      name + ": direction must remain explicitly unresolved until arrowhead classification is validated");
    const unresolved = candidates.filter(candidate => !candidate.direction || candidate.direction === "undetermined").length;
    assert.equal(candidates.length, refs.length,
      name + ": candidate count must match reference edge count before direction is evaluated");
    assert.equal(matchedRef.size, refs.length,
      name + ": every reference edge must have a geometric candidate before direction is evaluated");
    let arrowTipComparisons = 0, arrowTipWins = 0, arrowTipTies = 0;
    for (const { edge, ends: refEnds } of refs) {
      const candidate = candidates.find(item => {
        const direct = close(item.from, refEnds[0]) && close(item.to, refEnds[1]);
        const reverse = close(item.from, refEnds[1]) && close(item.to, refEnds[0]);
        return direct || reverse;
      });
      if (!candidate || !candidate.arrowhead_evidence) continue;
      const candidateStartsAtSource = close(candidate.from, refEnds[0]);
      const sourceEvidence = candidateStartsAtSource
        ? candidate.arrowhead_evidence.at_from : candidate.arrowhead_evidence.at_to;
      const targetEvidence = candidateStartsAtSource
        ? candidate.arrowhead_evidence.at_to : candidate.arrowhead_evidence.at_from;
      if (!sourceEvidence || !targetEvidence) continue;
      process.stdout.write(name + ": edge " + edge.id + " endpoint arrow evidence source=" +
        sourceEvidence.support_ratio.toFixed(3) + " target=" + targetEvidence.support_ratio.toFixed(3) +
        " (best angles " + sourceEvidence.angle_degrees + "deg/" + targetEvidence.angle_degrees + "deg).\\n");
      arrowTipComparisons++;
      if (targetEvidence.support_ratio > sourceEvidence.support_ratio) arrowTipWins++;
      else if (targetEvidence.support_ratio === sourceEvidence.support_ratio) arrowTipTies++;
    }
    process.stdout.write(name + ": arrow-tip evidence target>source=" + arrowTipWins + "/" +
      arrowTipComparisons + ", ties=" + arrowTipTies +
      ". Diagnostic only; direction inference remains disabled.\\n");
    const directionResolved = candidates.filter(candidate => candidate.direction && candidate.direction !== "undetermined").length;
    process.stdout.write(name + ": directed reference edges=" + refs.filter(({edge}) => edge.direction === "directed").length +
      ", candidates with resolved direction=" + directionResolved + "/" + candidates.length +
      ". Arrowhead/direction quality is not yet gated.\\n");
    process.stdout.write(name + ": edge candidate precision=" + precision.toFixed(3) +
      ", endpoint recall=" + recall.toFixed(3) + ", candidates=" + candidates.length +
      ", reference edges=" + refs.length + ".\\n");
    return { precision, recall, candidates: candidates.length, referenceEdges: refs.length,
      truePositives: matchedCandidates };
  }
  const evaluatedStructuralFixtures = [];
  testTopologyReportRejectsWrongEndpoints();

  function assertNodeGeometry(name, result) {
    const reference = referenceByFile.get(name);
    assert.ok(reference, name + ": reference annotation must exist");
    const unmatched = result.nodes.map((node, index) => index);
    let matched = 0;
    for (const expected of reference.nodes) {
      const at = unmatched.findIndex(index => {
        const center = result.nodes[index].center;
        return Math.hypot(center[0] - expected.center[0], center[1] - expected.center[1]) <= 12;
      });
      assert.notEqual(at, -1, name + ": expected node " + expected.id + " missing near " + expected.center.join(","));
      unmatched.splice(at, 1);
      matched++;
    }
    const precision = matched / result.nodes.length;
    const recall = matched / reference.nodes.length;
    assert.equal(recall, 1, name + ": all reference nodes must be recovered");
    assert.equal(unmatched.length, 0, name + ": false-positive node candidates are not allowed in this synthetic gate");
    if (name === "SYN-CROSSING-001.png") {
      assert.ok(!result.nodes.some(node => Math.hypot(node.center[0] - 160, node.center[1] - 90) <= 12),
        "crossing intersection must not be hallucinated as a node");
    }
    process.stdout.write(name + ": node precision=" + precision.toFixed(3) + ", recall=" + recall.toFixed(3) + ".\\n");
    return { precision, recall, candidates: result.nodes.length, referenceNodes: reference.nodes.length,
      truePositives: matched };
  }
  const colorVariants = [
    { name: "SYN-LINEAR-001.png", boxes: [[35,75,65,105],[145,75,175,105],[255,75,285,105]] },
    { name: "SYN-BRANCH-001.png", boxes: [[35,75,65,105],[145,30,175,60],[145,120,175,150],[255,75,285,105]] },
    { name: "SYN-CROSSING-001.png", boxes: [[35,30,65,60],[255,120,285,150],[35,120,65,150],[255,30,285,60]] }
  ];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const fixture of colorVariants) {
      const source = fs.readFileSync(path.join(root, "images", fixture.name));
      const dataUrl = "data:image/png;base64," + source.toString("base64");
      const coloredPng = await browser.newPage().then(async page => {
        const result = await page.evaluate(async ({ dataUrl, boxes }) => {
          const img = new Image(); img.src = dataUrl; await img.decode();
          const canvas = document.createElement("canvas"); canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
          const ctx = canvas.getContext("2d"); ctx.drawImage(img, 0, 0);
          const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const palette = [[205,232,255],[218,245,218],[255,235,190],[235,218,255]];
          boxes.forEach((box, index) => {
            const color = palette[index % palette.length];
            for (let y = box[1] + 2; y < box[3] - 1; y++) for (let x = box[0] + 2; x < box[2] - 1; x++) {
              const i = (y * canvas.width + x) * 4;
              if (pixels.data[i] > 210 && pixels.data[i+1] > 210 && pixels.data[i+2] > 210) {
                pixels.data[i] = color[0]; pixels.data[i+1] = color[1]; pixels.data[i+2] = color[2];
              }
            }
          });
          ctx.putImageData(pixels, 0, 0);
          return canvas.toDataURL("image/png").split(",")[1];
        }, { dataUrl, boxes: fixture.boxes });
        await page.close();
        return Buffer.from(result, "base64");
      });
      fs.writeFileSync(path.join(tempRoot, fixture.name), coloredPng);
    }
  } finally { await browser.close(); }
  // Controlled scale-robustness probe. Scale both raster pixels and reference
  // geometry together; do not treat this probe as a real-image quality claim.
  const scaleProbeName = "SYN-LINEAR-SCALE-150-PCT-001.png";
  const baseName = "SYN-LINEAR-001.png";
  const scaleFactor = 1.5;
  const baseBytes = fs.readFileSync(path.join(root, "images", baseName));
  const baseDataUrl = "data:image/png;base64," + baseBytes.toString("base64");
  const scaleBrowser = await chromium.launch({ headless: true });
  let scaledBytes;
  try {
    const page = await scaleBrowser.newPage();
    const encoded = await page.evaluate(async ({dataUrl, scaleFactor}) => {
      const img = new Image(); img.src = dataUrl; await img.decode();
      const canvas = document.createElement("canvas");
      canvas.width = Math.round(img.naturalWidth * scaleFactor);
      canvas.height = Math.round(img.naturalHeight * scaleFactor);
      const ctx = canvas.getContext("2d");
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      return canvas.toDataURL("image/png").split(",")[1];
    }, {dataUrl: baseDataUrl, scaleFactor});
    scaledBytes = Buffer.from(encoded, "base64");
    await page.close();
  } finally { await scaleBrowser.close(); }
  const scalePath = path.join(tempRoot, scaleProbeName);
  fs.writeFileSync(scalePath, scaledBytes);
  const baseReference = referenceByFile.get(baseName);
  const scaledReference = JSON.parse(JSON.stringify(baseReference));
  scaledReference.file = scaleProbeName;
  scaledReference.nodes = scaledReference.nodes.map(node => ({
    ...node, center: node.center.map(value => value * scaleFactor),
    ...(node.bbox ? {bbox: node.bbox.map(value => value * scaleFactor)} : {})
  }));
  scaledReference.edges = scaledReference.edges.map(edge => ({
    ...edge, polyline: edge.polyline.map(point => point.map(value => value * scaleFactor))
  }));
  referenceByFile.set(scaleProbeName, scaledReference);
  const scaledResult = await detectGraphCandidates(scalePath);
  assert.equal(scaledResult.status, "experimental-candidates-only",
    "SCALE-ROBUSTNESS-001: scaled raster remains provisional");
  assert.equal(scaledResult.image.width, 480, "SCALE-ROBUSTNESS-001: width reflects 150% scale");
  assert.equal(scaledResult.image.height, 270, "SCALE-ROBUSTNESS-001: height reflects 150% scale");
  assert.ok(scaledResult.nodes.length > 0, "SCALE-ROBUSTNESS-001: detector must find nodes at 150% scale");
  assert.ok(scaledResult.nodes.every(node => node.review_required === true),
    "SCALE-ROBUSTNESS-001: scaled candidates still require user review");
  const scaledNodeMetrics = assertNodeGeometry(scaleProbeName, scaledResult);
  // Scale the geometric matching tolerance with the raster so the metric
  // does not penalize the same pixel-localization error more harshly at 150%.
  const scaledEdgeMetrics = reportEdgeGeometry(scaleProbeName, scaledResult, 14 * scaleFactor);
  const scaledTopologyMetrics = reportTopologyByNodeIdentity(scaleProbeName, scaledResult);
  evaluatedStructuralFixtures.push({fixture: scaleProbeName, scale_factor: scaleFactor,
    node_candidates: scaledNodeMetrics.candidates, reference_nodes: scaledNodeMetrics.referenceNodes,
    node_precision: scaledNodeMetrics.precision, node_recall: scaledNodeMetrics.recall,
    node_true_positives: scaledNodeMetrics.truePositives,
    edge_candidates: scaledEdgeMetrics.candidates, reference_edges: scaledEdgeMetrics.referenceEdges,
    edge_precision: scaledEdgeMetrics.precision, edge_recall: scaledEdgeMetrics.recall,
    edge_true_positives: scaledEdgeMetrics.truePositives,
    ...scaledTopologyMetrics, direction_scored: false});
  for (const name of ["SYN-LINEAR-001.png", "SYN-BRANCH-001.png", "SYN-CROSSING-001.png"]) {
    const result = await detectGraphCandidates(path.join(root, "images", name));
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.equal(result.image.width, 320);
    assert.equal(result.image.height, 180);
    assert.ok(Array.isArray(result.nodes));
    assert.ok(Array.isArray(result.edge_candidates));
    if (result.nodes.length === 0) process.stderr.write(name + " diagnostics: " + JSON.stringify(result.diagnostics) + "\\n");
    assert.ok(result.nodes.length > 0, name + ": detector must find at least one provisional node box");
    assert.ok(result.limitations.length >= 3);
    assert.ok(result.nodes.every(n => n.review_required === true));
    const nodeMetrics = assertNodeGeometry(name, result);
    const edgeMetrics = reportEdgeGeometry(name, result);
    const topologyMetrics = reportTopologyByNodeIdentity(name, result);
    evaluatedStructuralFixtures.push({ fixture: name,
      node_candidates: nodeMetrics.candidates, reference_nodes: nodeMetrics.referenceNodes,
      node_precision: nodeMetrics.precision, node_recall: nodeMetrics.recall,
      node_true_positives: nodeMetrics.truePositives,
      edge_candidates: edgeMetrics.candidates, reference_edges: edgeMetrics.referenceEdges,
      edge_precision: edgeMetrics.precision, edge_recall: edgeMetrics.recall,
      edge_true_positives: edgeMetrics.truePositives,
      ...topologyMetrics,
      false_positive_nodes: nodeMetrics.candidates - Math.round(nodeMetrics.precision * nodeMetrics.candidates),
      missed_nodes: nodeMetrics.referenceNodes - Math.round(nodeMetrics.recall * nodeMetrics.referenceNodes),
      false_positive_edges: edgeMetrics.candidates - Math.round(edgeMetrics.precision * edgeMetrics.candidates),
      missed_edges: edgeMetrics.referenceEdges - Math.round(edgeMetrics.recall * edgeMetrics.referenceEdges),
      direction_scored: false });
    process.stdout.write(name + ": " + result.nodes.length + " provisional node candidates; " +
      result.edge_candidates.length + " horizontal stroke candidates.\n");
  }
  for (const fixture of colorVariants) {
    const coloredPath = path.join(tempRoot, fixture.name);
    const result = await detectGraphCandidates(coloredPath);
    assert.equal(result.detector, "TGCV-RASTER-GRAPH-CANDIDATES-001");
    assert.equal(result.status, "experimental-candidates-only");
    assert.ok(result.nodes.length > 0, fixture.name + ": colored-node variant must yield provisional candidates");
    assert.ok(result.nodes.every(n => n.review_required === true));
    const nodeMetrics = assertNodeGeometry(fixture.name, result);
    const edgeMetrics = reportEdgeGeometry(fixture.name, result);
    const topologyMetrics = reportTopologyByNodeIdentity(fixture.name, result);
    evaluatedStructuralFixtures.push({ fixture: fixture.name,
      node_candidates: nodeMetrics.candidates, reference_nodes: nodeMetrics.referenceNodes,
      node_precision: nodeMetrics.precision, node_recall: nodeMetrics.recall,
      edge_candidates: edgeMetrics.candidates, reference_edges: edgeMetrics.referenceEdges,
      edge_precision: edgeMetrics.precision, edge_recall: edgeMetrics.recall,
      ...topologyMetrics,
      false_positive_nodes: nodeMetrics.candidates - Math.round(nodeMetrics.precision * nodeMetrics.candidates),
      missed_nodes: nodeMetrics.referenceNodes - Math.round(nodeMetrics.recall * nodeMetrics.referenceNodes),
      false_positive_edges: edgeMetrics.candidates - Math.round(edgeMetrics.precision * edgeMetrics.candidates),
      missed_edges: edgeMetrics.referenceEdges - Math.round(edgeMetrics.recall * edgeMetrics.referenceEdges),
      direction_scored: false });
    process.stdout.write(fixture.name + ": " + result.nodes.length + " provisional candidates on colored-node variant.\\n");
  }
  // Generated raster fixture: two outlined nodes connected by a plain line,
  // intentionally without arrowheads. This tests the no-arrow import case.
  const noArrowPath = path.join(tempRoot, "SYN-NO-ARROWS-001.png");
  const fixtureBrowser = await chromium.launch({ headless: true });
  try {
    const page = await fixtureBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2); ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(noArrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await fixtureBrowser.close(); }
  const noArrowResult = await detectGraphCandidates(noArrowPath);
  assert.equal(noArrowResult.status, "experimental-candidates-only");
  assert.ok(noArrowResult.nodes.length >= 2,
    "SYN-NO-ARROWS-001: both visible nodes should yield provisional candidates");
  assert.ok(noArrowResult.edge_candidates.length >= 1,
    "SYN-NO-ARROWS-001: plain connecting line should yield a provisional connection");
  assert.ok(noArrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-NO-ARROWS-001: no arrowheads must not produce an invented direction");
  process.stdout.write("SYN-NO-ARROWS-001: nodes=" + noArrowResult.nodes.length +
    ", connections=" + noArrowResult.edge_candidates.length +
    ", all directions unresolved; human review required.\\n");
  // Same topology with differently colored node fills: color must not create
  // an arrow or cause direction to be guessed.
  const coloredNoArrowPath = path.join(tempRoot, "SYN-NO-ARROWS-COLORED-001.png");
  const colorBrowser = await chromium.launch({ headless: true });
  try {
    const page = await colorBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      for (const [x, fill] of [[50, "#8ecae6"], [270, "#ffb703"]]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2); ctx.fillStyle = fill; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(coloredNoArrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await colorBrowser.close(); }
  const coloredNoArrowResult = await detectGraphCandidates(coloredNoArrowPath);
  assert.equal(coloredNoArrowResult.status, "experimental-candidates-only");
  assert.ok(coloredNoArrowResult.nodes.length >= 2,
    "SYN-NO-ARROWS-COLORED-001: both colored nodes should yield provisional candidates");
  assert.ok(coloredNoArrowResult.edge_candidates.length >= 1,
    "SYN-NO-ARROWS-COLORED-001: plain line should yield a provisional connection");
  assert.ok(coloredNoArrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-NO-ARROWS-COLORED-001: colored nodes without arrowheads must not produce an invented direction");
  process.stdout.write("SYN-NO-ARROWS-COLORED-001: nodes=" + coloredNoArrowResult.nodes.length +
    ", connections=" + coloredNoArrowResult.edge_candidates.length +
    ", all directions unresolved; human review required.\\n");
  // Visible arrowhead fixture. The detector must preserve the connection,
  // but must not claim a direction until a validated classifier exists.
  const arrowPath = path.join(tempRoot, "SYN-ARROW-CLEAR-001.png");
  const arrowBrowser = await chromium.launch({ headless: true });
  try {
    const page = await arrowBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      // Clear arrowhead pointing toward the right-hand node.
      ctx.beginPath(); ctx.moveTo(243, 82); ctx.lineTo(255, 90); ctx.lineTo(243, 98); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(arrowPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await arrowBrowser.close(); }
  const arrowResult = await detectGraphCandidates(arrowPath);
  assert.equal(arrowResult.status, "experimental-candidates-only");
  assert.ok(arrowResult.nodes.length >= 2, "SYN-ARROW-CLEAR-001: both nodes should be detected");
  assert.ok(arrowResult.edge_candidates.length >= 1, "SYN-ARROW-CLEAR-001: arrowed connection should be proposed");
  assert.ok(arrowResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-ARROW-CLEAR-001: direction remains provisional until validated classification is implemented");
  process.stdout.write("SYN-ARROW-CLEAR-001: nodes=" + arrowResult.nodes.length +
    ", connections=" + arrowResult.edge_candidates.length +
    ", arrow visible but direction remains provisional.\\n");
  // Two opposing arrowheads represent two directed transitions, not an
  // undirected line. Until the classifier is validated, both stay provisional.
  const bidirectionalPath = path.join(tempRoot, "SYN-BIDIRECTIONAL-001.png");
  const bidiBrowser = await chromium.launch({ headless: true });
  try {
    const page = await bidiBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(65, 90); ctx.lineTo(255, 90); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(77, 82); ctx.lineTo(65, 90); ctx.lineTo(77, 98); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(243, 82); ctx.lineTo(255, 90); ctx.lineTo(243, 98); ctx.stroke();
      for (const x of [50, 270]) {
        ctx.beginPath(); ctx.arc(x, 90, 15, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(bidirectionalPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await bidiBrowser.close(); }
  const bidirectionalResult = await detectGraphCandidates(bidirectionalPath);
  assert.equal(bidirectionalResult.status, "experimental-candidates-only");
  assert.ok(bidirectionalResult.nodes.length >= 2, "SYN-BIDIRECTIONAL-001: both nodes should be detected");
  assert.ok(bidirectionalResult.edge_candidates.length >= 1, "SYN-BIDIRECTIONAL-001: connection should be proposed");
  assert.ok(bidirectionalResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-BIDIRECTIONAL-001: opposing arrows must remain provisional until direction classification is validated");
  process.stdout.write("SYN-BIDIRECTIONAL-001: nodes=" + bidirectionalResult.nodes.length +
    ", connections=" + bidirectionalResult.edge_candidates.length +
    ", opposing arrowheads present; direction classification provisional.\\n");
  // Crossing lines without a junction marker must not automatically be
  // interpreted as a graph node. The current detector is candidate-only, so
  // this fixture records the structural behavior for review.
  const crossingPath = path.join(tempRoot, "SYN-CROSSING-NO-JUNCTION-001.png");
  const crossBrowser = await chromium.launch({ headless: true });
  try {
    const page = await crossBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 320; canvas.height = 220;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 320, 220);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(32, 110); ctx.lineTo(288, 110); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(160, 32); ctx.lineTo(160, 188); ctx.stroke();
      for (const [x,y] of [[20,110],[300,110],[160,20],[160,200]]) {
        ctx.beginPath(); ctx.arc(x, y, 12, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(crossingPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await crossBrowser.close(); }
  const crossingResult = await detectGraphCandidates(crossingPath);
  assert.equal(crossingResult.status, "experimental-candidates-only");
  assert.equal(crossingResult.nodes.length, 4,
    "SYN-CROSSING-NO-JUNCTION-001: exactly four endpoint nodes should be proposed; extra candidates are topological false positives");
  assert.ok(crossingResult.nodes.every(node =>
    Math.hypot(node.center[0] - 160, node.center[1] - 110) > 18),
    "SYN-CROSSING-NO-JUNCTION-001: line intersection must not be proposed as a node");
  assert.equal(crossingResult.edge_candidates.length, 2,
    "SYN-CROSSING-NO-JUNCTION-001: exactly two intended line connections should be proposed; extra candidates are topological false positives");
  const crossingNodesById = new Map(crossingResult.nodes.map(node => [node.id, node]));
  assert.ok(crossingResult.edge_candidates.every(edge => {
    const source = crossingNodesById.get(edge.source_candidate_node_id);
    const target = crossingNodesById.get(edge.target_candidate_node_id);
    if (!source || !target) return false;
    const horizontal = Math.abs(source.center[1] - 110) <= 18 &&
      Math.abs(target.center[1] - 110) <= 18;
    const vertical = Math.abs(source.center[0] - 160) <= 18 &&
      Math.abs(target.center[0] - 160) <= 18;
    return horizontal || vertical;
  }), "SYN-CROSSING-NO-JUNCTION-001: every proposed connection must follow one of the two drawn lines, not a diagonal shortcut");
  assert.ok(crossingResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" && edge.direction === "undetermined" && edge.review_required === true),
    "SYN-CROSSING-NO-JUNCTION-001: crossing geometry must not invent edge direction");
  process.stdout.write("SYN-CROSSING-NO-JUNCTION-001: nodes=" + crossingResult.nodes.length +
    ", connections=" + crossingResult.edge_candidates.length +
    ", no automatic direction inference.\\n");
  // Three-node linear graph: A-B-C. The detector must propose A-B and B-C,
  // but must not add the shortcut A-C through the intervening node.
  const linearPath = path.join(tempRoot, "SYN-LINEAR-3-NODES-001.png");
  const linearBrowser = await chromium.launch({ headless: true });
  try {
    const page = await linearBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 180;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 180);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(45, 90); ctx.lineTo(315, 90); ctx.stroke();
      for (const x of [35, 180, 325]) {
        ctx.beginPath(); ctx.arc(x, 90, 13, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(linearPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await linearBrowser.close(); }
  const linearResult = await detectGraphCandidates(linearPath);
  assert.equal(linearResult.status, "experimental-candidates-only");
  assert.equal(linearResult.nodes.length, 3,
    "SYN-LINEAR-3-NODES-001: exactly three nodes should be proposed");
  assert.equal(linearResult.edge_candidates.length, 2,
    "SYN-LINEAR-3-NODES-001: exactly two adjacent connections should be proposed; no A-C shortcut");
  const linearNodes = [...linearResult.nodes].sort((a,b) => a.center[0] - b.center[0]);
  const linearPairs = new Set(linearResult.edge_candidates.map(edge => {
    const source = linearResult.nodes.find(node => node.id === edge.source_candidate_node_id);
    const target = linearResult.nodes.find(node => node.id === edge.target_candidate_node_id);
    if (!source || !target) return "invalid";
    return [Math.round(source.center[0]), Math.round(target.center[0])].sort((a,b)=>a-b).join("--");
  }));
  assert.deepEqual(linearPairs, new Set([
    [Math.round(linearNodes[0].center[0]), Math.round(linearNodes[1].center[0])].sort((a,b)=>a-b).join("--"),
    [Math.round(linearNodes[1].center[0]), Math.round(linearNodes[2].center[0])].sort((a,b)=>a-b).join("--")
  ]), "SYN-LINEAR-3-NODES-001: edges must connect adjacent nodes only");
  process.stdout.write("SYN-LINEAR-3-NODES-001: exactly 3 nodes and 2 adjacent connections; no shortcut.\\n");
  // Branched graph: a central node connected to three leaves. Expect one
  // edge per drawn branch and no leaf-to-leaf shortcuts.
  const branchPath = path.join(tempRoot, "SYN-BRANCH-3-LEAVES-001.png");
  const branchBrowser = await chromium.launch({ headless: true });
  try {
    const page = await branchBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath();
        ctx.moveTo(center[0] + dx/len*15, center[1] + dy/len*15);
        ctx.lineTo(x - dx/len*13, y - dy/len*13);
        ctx.stroke();
      }
      for (const [x,y] of [center,...leaves]) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(branchPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await branchBrowser.close(); }
  const branchResult = await detectGraphCandidates(branchPath);
  assert.equal(branchResult.status, "experimental-candidates-only");
  assert.equal(branchResult.nodes.length, 4,
    "SYN-BRANCH-3-LEAVES-001: exactly one center and three leaves should be proposed");
  assert.equal(branchResult.edge_candidates.length, 3,
    "SYN-BRANCH-3-LEAVES-001: exactly three drawn branch connections should be proposed");
  const branchNodes = new Map(branchResult.nodes.map(node => [node.id, node]));
  const centerNode = branchResult.nodes.find(node => Math.hypot(node.center[0]-180,node.center[1]-130) < 18);
  assert.ok(centerNode, "SYN-BRANCH-3-LEAVES-001: central node must be detected");
  assert.ok(branchResult.edge_candidates.every(edge => {
    const source = branchNodes.get(edge.source_candidate_node_id);
    const target = branchNodes.get(edge.target_candidate_node_id);
    return source && target && (source.id === centerNode.id || target.id === centerNode.id);
  }), "SYN-BRANCH-3-LEAVES-001: every edge must touch the center; no leaf-to-leaf shortcuts");
  process.stdout.write("SYN-BRANCH-3-LEAVES-001: exactly 4 nodes and 3 center-to-leaf connections.\\n");
  // Controlled line-thickness probe: same topology and node geometry,
  // with only connector stroke width changed from 2 px to 5 px.
  const thickBranchPath = path.join(tempRoot, "SYN-BRANCH-THICK-LINES-001.png");
  const thickBranchBrowser = await chromium.launch({ headless: true });
  try {
    const page = await thickBranchBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 5;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath(); ctx.moveTo(center[0]+dx/len*15,center[1]+dy/len*15);
        ctx.lineTo(x-dx/len*13,y-dy/len*13); ctx.stroke();
      }
      for (const [x,y] of [center,...leaves]) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(thickBranchPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await thickBranchBrowser.close(); }
  const thickBranchResult = await detectGraphCandidates(thickBranchPath);
  assert.equal(thickBranchResult.status, "experimental-candidates-only",
    "SYN-BRANCH-THICK-LINES-001: thick-line result remains provisional");
  assert.equal(thickBranchResult.nodes.length, 4,
    "SYN-BRANCH-THICK-LINES-001: line thickness must preserve four-node count");
  assert.equal(thickBranchResult.edge_candidates.length, 3,
    "SYN-BRANCH-THICK-LINES-001: 5px lines must preserve three-connection count");
  const thickCenter = thickBranchResult.nodes.find(node =>
    Math.hypot(node.center[0]-180,node.center[1]-130) < 18);
  assert.ok(thickCenter, "SYN-BRANCH-THICK-LINES-001: center node must be detected");
  const thickNodes = new Map(thickBranchResult.nodes.map(node => [node.id,node]));
  assert.ok(thickBranchResult.edge_candidates.every(edge => {
    const source=thickNodes.get(edge.source_candidate_node_id);
    const target=thickNodes.get(edge.target_candidate_node_id);
    return source && target && (source.id===thickCenter.id || target.id===thickCenter.id);
  }), "SYN-BRANCH-THICK-LINES-001: thick lines must not introduce leaf-to-leaf shortcuts");
  process.stdout.write("SYN-BRANCH-THICK-LINES-001: 5px connector stroke preserves branch topology.\\n");
  // Controlled contrast probe: preserve geometry and 2px line width,
  // changing only connector/node outline color from #111111 to #555555.
  const lowContrastPath = path.join(tempRoot, "SYN-BRANCH-LOW-CONTRAST-001.png");
  const lowContrastBrowser = await chromium.launch({ headless: true });
  try {
    const page = await lowContrastBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#555555"; ctx.lineWidth = 2;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath(); ctx.moveTo(center[0]+dx/len*15,center[1]+dy/len*15);
        ctx.lineTo(x-dx/len*13,y-dy/len*13); ctx.stroke();
      }
      for (const [x,y] of [center,...leaves]) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(lowContrastPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await lowContrastBrowser.close(); }
  const lowContrastResult = await detectGraphCandidates(lowContrastPath);
  assert.equal(lowContrastResult.status, "experimental-candidates-only",
    "SYN-BRANCH-LOW-CONTRAST-001: low-contrast result remains provisional");
  assert.equal(lowContrastResult.nodes.length, 4,
    "SYN-BRANCH-LOW-CONTRAST-001: #555555 outlines must preserve four-node count");
  assert.equal(lowContrastResult.edge_candidates.length, 3,
    "SYN-BRANCH-LOW-CONTRAST-001: #555555 connectors must preserve three-edge count");
  process.stdout.write("SYN-BRANCH-LOW-CONTRAST-001: contrast change preserves expected candidate counts.\\n");
  // Controlled background-noise probe: fixed topology, stroke, and foreground;
  // deterministic sparse gray speckles are added to the white background.
  const noisyBackgroundPath = path.join(tempRoot, "SYN-BRANCH-SPARSE-NOISE-001.png");
  const noiseBrowser = await chromium.launch({ headless: true });
  try {
    const page = await noiseBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      // Fixed deterministic pattern; keep speckles away from the node/edge geometry.
      for (let i=0; i<180; i++) {
        const x = (i*47+19)%360, y = (i*83+31)%260;
        if ((x>25&&x<335&&y>25&&y<235) &&
            !((Math.abs(y-130)<18 && x>55 && x<285) ||
              (Math.abs((y-130) - (x-180)*(-85/120))<16 && x>190 && x<305) ||
              (Math.abs((y-130) - (x-180)*(85/120))<16 && x>190 && x<305) ||
              [[180,130],[45,130],[300,45],[300,215]].some(([nx,ny])=>Math.hypot(x-nx,y-ny)<20))) {
          ctx.fillStyle = i%2 ? "#dddddd" : "#bbbbbb";
          ctx.fillRect(x,y,1,1);
        }
      }
      ctx.strokeStyle="#111111"; ctx.lineWidth=2;
      const center=[180,130], leaves=[[45,130],[300,45],[300,215]];
      for(const [x,y] of leaves) {
        const dx=x-center[0],dy=y-center[1],len=Math.hypot(dx,dy);
        ctx.beginPath();ctx.moveTo(center[0]+dx/len*15,center[1]+dy/len*15);
        ctx.lineTo(x-dx/len*13,y-dy/len*13);ctx.stroke();
      }
      for(const [x,y] of [center,...leaves]) {
        ctx.beginPath();ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle="#ffffff";ctx.fill();ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(noisyBackgroundPath, Buffer.from(base64,"base64"));
    await page.close();
  } finally { await noiseBrowser.close(); }
  const noisyBackgroundResult = await detectGraphCandidates(noisyBackgroundPath);
  assert.equal(noisyBackgroundResult.status,"experimental-candidates-only",
    "SYN-BRANCH-SPARSE-NOISE-001: noisy-background result remains provisional");
  assert.equal(noisyBackgroundResult.nodes.length,4,
    "SYN-BRANCH-SPARSE-NOISE-001: sparse background noise must preserve four-node count");
  assert.equal(noisyBackgroundResult.edge_candidates.length,3,
    "SYN-BRANCH-SPARSE-NOISE-001: sparse background noise must preserve three-edge count");
  process.stdout.write("SYN-BRANCH-SPARSE-NOISE-001: sparse background noise preserves expected candidate counts.\\n");
  // Ambiguous junction probe: four arms meet at a shared central junction.
  // Expected topology is four center-to-leaf connections, never leaf-to-leaf shortcuts.
  const junctionPath = path.join(tempRoot, "SYN-CROSS-JUNCTION-001.png");
  const junctionBrowser = await chromium.launch({ headless: true });
  try {
    const page = await junctionBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas=document.createElement("canvas"); canvas.width=360; canvas.height=260;
      const ctx=canvas.getContext("2d");
      ctx.fillStyle="#ffffff";ctx.fillRect(0,0,360,260);
      ctx.strokeStyle="#111111";ctx.lineWidth=2;
      const center=[180,130], leaves=[[45,130],[315,130],[180,35],[180,225]];
      for(const [x,y] of leaves) {
        const dx=x-center[0],dy=y-center[1],len=Math.hypot(dx,dy);
        ctx.beginPath();ctx.moveTo(center[0]+dx/len*14,center[1]+dy/len*14);
        ctx.lineTo(x-dx/len*13,y-dy/len*13);ctx.stroke();
      }
      for(const [x,y] of [center,...leaves]) {
        ctx.beginPath();ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle="#ffffff";ctx.fill();ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(junctionPath,Buffer.from(base64,"base64"));
    await page.close();
  } finally { await junctionBrowser.close(); }
  const junctionResult=await detectGraphCandidates(junctionPath);
  assert.equal(junctionResult.status,"experimental-candidates-only",
    "SYN-CROSS-JUNCTION-001: junction candidates remain provisional");
  assert.equal(junctionResult.nodes.length,5,
    "SYN-CROSS-JUNCTION-001: shared junction must preserve five nodes");
  assert.equal(junctionResult.edge_candidates.length,4,
    "SYN-CROSS-JUNCTION-001: shared junction must yield four arms");
  const junctionNodes=new Map(junctionResult.nodes.map(node=>[node.id,node]));
  const centerCandidate=junctionResult.nodes.find(node=>
    Math.hypot(node.center[0]-180,node.center[1]-130)<18);
  assert.ok(centerCandidate,"SYN-CROSS-JUNCTION-001: central junction node must be detected");
  assert.ok(junctionResult.edge_candidates.every(edge=>{
    const source=junctionNodes.get(edge.source_candidate_node_id);
    const target=junctionNodes.get(edge.target_candidate_node_id);
    return source&&target&&(source.id===centerCandidate.id||target.id===centerCandidate.id);
  }),"SYN-CROSS-JUNCTION-001: junction must not create leaf-to-leaf shortcuts");
  assert.ok(junctionResult.edge_candidates.every(edge =>
    edge.direction_status === "unresolved" &&
    edge.direction === "undetermined" &&
    edge.review_required === true
  ), "SYN-CROSS-JUNCTION-001: junction geometry must not imply edge direction; every edge remains unresolved and reviewable");
  process.stdout.write("SYN-CROSS-JUNCTION-001: central four-arm junction preserves topology; direction remains unresolved.\\n");
  // Same branched topology with differently colored nodes. Color is visual
  // styling, not a reason to change the graph structure.
  const coloredBranchPath = path.join(tempRoot, "SYN-BRANCH-COLORED-NODES-001.png");
  const coloredBranchBrowser = await chromium.launch({ headless: true });
  try {
    const page = await coloredBranchBrowser.newPage();
    const base64 = await page.evaluate(() => {
      const canvas = document.createElement("canvas"); canvas.width = 360; canvas.height = 260;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, 360, 260);
      ctx.strokeStyle = "#111111"; ctx.lineWidth = 2;
      const center = [180, 130], leaves = [[45, 130], [300, 45], [300, 215]];
      for (const [x,y] of leaves) {
        const dx = x-center[0], dy = y-center[1], len = Math.hypot(dx,dy);
        ctx.beginPath(); ctx.moveTo(center[0]+dx/len*15,center[1]+dy/len*15);
        ctx.lineTo(x-dx/len*13,y-dy/len*13); ctx.stroke();
      }
      const nodes = [{p:center,c:"#f4a261"},{p:leaves[0],c:"#8ecae6"},
        {p:leaves[1],c:"#90be6d"},{p:leaves[2],c:"#cdb4db"}];
      for (const {p:[x,y],c} of nodes) {
        ctx.beginPath(); ctx.arc(x,y,13,0,Math.PI*2);
        ctx.fillStyle=c; ctx.fill(); ctx.stroke();
      }
      return canvas.toDataURL("image/png").split(",")[1];
    });
    fs.writeFileSync(coloredBranchPath, Buffer.from(base64, "base64"));
    await page.close();
  } finally { await coloredBranchBrowser.close(); }
  const coloredBranchResult = await detectGraphCandidates(coloredBranchPath);
  assert.equal(coloredBranchResult.status, "experimental-candidates-only");
  assert.equal(coloredBranchResult.nodes.length, 4,
    "SYN-BRANCH-COLORED-NODES-001: node colors must not change the expected count");
  assert.equal(coloredBranchResult.edge_candidates.length, 3,
    "SYN-BRANCH-COLORED-NODES-001: node colors must not change the expected connection count");
  const coloredCenter = coloredBranchResult.nodes.find(node =>
    Math.hypot(node.center[0]-180,node.center[1]-130) < 18);
  assert.ok(coloredCenter, "SYN-BRANCH-COLORED-NODES-001: central colored node must be detected");
  const coloredNodeMap = new Map(coloredBranchResult.nodes.map(node => [node.id,node]));
  assert.ok(coloredBranchResult.edge_candidates.every(edge => {
    const source=coloredNodeMap.get(edge.source_candidate_node_id);
    const target=coloredNodeMap.get(edge.target_candidate_node_id);
    return source && target && (source.id===coloredCenter.id || target.id===coloredCenter.id);
  }), "SYN-BRANCH-COLORED-NODES-001: colored topology must retain center-to-leaf edges only");
  process.stdout.write("SYN-BRANCH-COLORED-NODES-001: color variation preserves 4-node, 3-edge branch topology.\\n");
  // Consolidated structural summary for the explicit synthetic topology fixtures.
  // Counts are fixture-level diagnostics; existing assertions above verify edge
  // incidence/topology for each graph and do not resolve edge direction.
  const structuralSummary = [
    { fixture: "SYN-CROSSING-NO-JUNCTION-001", expected_nodes: 4, expected_edges: 2, result: crossingResult },
    { fixture: "SYN-LINEAR-3-NODES-001", expected_nodes: 3, expected_edges: 2, result: linearResult },
    { fixture: "SYN-BRANCH-3-LEAVES-001", expected_nodes: 4, expected_edges: 3, result: branchResult },
    { fixture: "SYN-BRANCH-COLORED-NODES-001", expected_nodes: 4, expected_edges: 3, result: coloredBranchResult }
  ].map(({fixture, expected_nodes, expected_edges, result}) => ({
    fixture,
    expected_nodes,
    detected_nodes: result.nodes.length,
    node_count_error: result.nodes.length - expected_nodes,
    expected_edges,
    proposed_edges: result.edge_candidates.length,
    edge_count_error: result.edge_candidates.length - expected_edges,
    counts_match: result.nodes.length === expected_nodes && result.edge_candidates.length === expected_edges,
    direction_evaluation: "not_scored; direction remains unresolved"
  }));
  const structuralSummaryPath = path.join(tempRoot, "raster_graph_structural_summary.json");
  fs.writeFileSync(structuralSummaryPath, JSON.stringify({
    schema_version: "tgcv-raster-structural-summary-0.1",
    status: "synthetic-fixture-evaluation",
    interpretation: "Count metrics are not a substitute for full graph-isomorphism/topology scoring or real-image validation.",
    fixtures: structuralSummary
  }, null, 2) + "\\n");
  process.stdout.write("STRUCTURAL-SUMMARY: " + JSON.stringify(structuralSummary) + "\\n");
  const evaluationReport = {
    schema_version: "tgcv-raster-structural-evaluation-0.3",
    status: "synthetic-and-color-variant-fixtures",
    aggregate: (() => {
      const sum = (key) => evaluatedStructuralFixtures.reduce((total, item) => total + item[key], 0);
      const nodes = summarizeCounts(sum("node_candidates"), sum("reference_nodes"), sum("node_true_positives"));
      const edges = summarizeCounts(sum("edge_candidates"), sum("reference_edges"), sum("edge_true_positives"));
      return {
        fixture_count: evaluatedStructuralFixtures.length,
        node_candidates: nodes.candidates,
        reference_nodes: nodes.references,
        node_true_positives: nodes.true_positives,
        node_false_positives: nodes.false_positives,
        node_false_negatives: nodes.false_negatives,
        node_precision: nodes.precision,
        node_recall: nodes.recall,
        edge_candidates: edges.candidates,
        reference_edges: edges.references,
        edge_true_positives: edges.true_positives,
        edge_false_positives: edges.false_positives,
        edge_false_negatives: edges.false_negatives,
        edge_precision: edges.precision,
        edge_recall: edges.recall,
        direction_scored: false
      };
    })(),
    reader_summary: {
      title: "Informe de reconstrucción estructural del grafo",
      scope: "Evaluación con fixtures sintéticos; no constituye validación con imágenes reales.",
      node_detection: "Se informa por separado cuántos nodos propuestos coinciden geométricamente con la referencia.",
      edge_topology: "Una conexión solo cuenta como acierto si enlaza el par correcto de nodos; los recuentos por sí solos no bastan.",
      direction: "No inferida por la geometría; permanece sin resolver.",
      required_user_action: "Revisar y confirmar los candidatos antes de aceptar el grafo.",
      limitations: [
        "Las correspondencias de nodos se basan en proximidad geométrica y tolerancias de fixture.",
        "Las métricas agregadas describen únicamente el conjunto de fixtures incluidos en esta ejecución.",
        "Los resultados sintéticos no demuestran rendimiento general en diagramas reales."
      ]
    },
    topology_aggregate: (() => {
      const sum = (key) => evaluatedStructuralFixtures.reduce((total, item) => total + (Number.isFinite(item[key]) ? item[key] : 0), 0);
      const truePositives = sum("topology_edge_true_positives");
      const falsePositives = sum("topology_edge_false_positives");
      const falseNegatives = sum("topology_edge_false_negatives");
      const candidates = truePositives + falsePositives;
      const references = truePositives + falseNegatives;
      return {
        true_positives: truePositives,
        false_positives: falsePositives,
        false_negatives: falseNegatives,
        precision: candidates ? truePositives / candidates : 0,
        recall: references ? truePositives / references : 0,
        interpretation: "Undirected endpoint identity; direction is not scored."
      };
    })(),
    metrics: { edge_precision: "matched candidate edges / all proposed candidate edges",
      edge_recall: "matched reference edges / all reference edges",
      node_metrics: "asserted independently by geometric matching",
      direction: "not scored; inference disabled" },
    fixture_level_interpretation: "Review each fixture independently; aggregate precision/recall must not be used to declare every individual graph correct.",
    graph_review_summary_contract: {
      per_graph_fields: ["graph_id","graph_status","review_required_edge_count","ambiguous_edge_count","unresolved_edge_count","direction_unresolved_edge_count","can_auto_accept"],
      aggregate_counts: ["graph_count","incomplete_graph_count","needs_review_graph_count","review_ready_graph_count"],
      automatic_acceptance: false,
      note: "The current test validates the review-summary contract with controlled examples; it does not claim the UI is already wired to live OCR candidates."
    },
    graph_review_policy: {
      graph_status_values: ["review_ready","needs_review","incomplete"],
      automatic_acceptance: false,
      meaning: {
        review_ready: "No unresolved structural edge or candidate review flag remains; human confirmation is still required.",
        needs_review: "At least one edge is ambiguous, direction-unresolved, low-confidence, or otherwise flagged for review.",
        incomplete: "The graph has no edges or contains at least one structurally unresolved edge."
      },
      note: "Provisional workflow policy; not a validated quality guarantee."
    },
    edge_candidate_review_policy: {
      structural_status_values: ["detected","ambiguous","unresolved"],
      direction_status_values: ["resolved","unresolved"],
      missing_confidence: "treated as unknown; requires review",
      review_rule: "ambiguous structure, unresolved direction, missing confidence, or confidence below 0.9 requires review",
      note: "Confidence here is candidate metadata, not a calibrated probability unless separately validated."
    },
    fixtures: evaluatedStructuralFixtures
  };
  // Validate per-fixture accounting and ensure aggregate topology metrics
  // are exactly the sums of the individual fixture metrics.
  for (const fixture of evaluatedStructuralFixtures) {
    assert.equal(fixture.topology_edge_true_positives + fixture.topology_edge_false_positives,
      fixture.edge_candidates,
      fixture.fixture + ": topology TP + FP must equal proposed edge candidates");
    assert.equal(fixture.topology_edge_true_positives + fixture.topology_edge_false_negatives,
      fixture.reference_edges,
      fixture.fixture + ": topology TP + FN must equal reference edges");
    const expectedPrecision = fixture.edge_candidates
      ? fixture.topology_edge_true_positives / fixture.edge_candidates : 0;
    const expectedRecall = fixture.reference_edges
      ? fixture.topology_edge_true_positives / fixture.reference_edges : 0;
    assert.ok(Math.abs(fixture.topology_edge_precision - expectedPrecision) < 1e-12,
      fixture.fixture + ": topology precision must agree with counts");
    assert.ok(Math.abs(fixture.topology_edge_recall - expectedRecall) < 1e-12,
      fixture.fixture + ": topology recall must agree with counts");
  }
  assert.ok(evaluationReport.fixtures.length > 0,
    "REPORT-PER-FIXTURE-VISIBILITY-001: report must retain individual fixture results");
  for (const fixture of evaluationReport.fixtures) {
    for (const field of ["topology_edge_true_positives","topology_edge_false_positives",
      "topology_edge_false_negatives","topology_edge_precision","topology_edge_recall"]) {
      assert.ok(Number.isFinite(fixture[field]),
        "REPORT-PER-FIXTURE-VISIBILITY-001: " + fixture.fixture + " must expose finite " + field);
    }
  }
  assert.match(evaluationReport.fixture_level_interpretation, /each fixture independently/i,
    "REPORT-PER-FIXTURE-VISIBILITY-001: report must warn against using aggregate metrics as per-graph guarantees");
  process.stdout.write("REPORT-PER-FIXTURE-VISIBILITY-001: per-fixture topology metrics remain visible beside aggregates.\\n");
  const topologySum = key => evaluatedStructuralFixtures.reduce((total,item)=>total+item[key],0);
  assert.equal(evaluationReport.topology_aggregate.true_positives,
    topologySum("topology_edge_true_positives"),
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate TP must equal per-fixture TP sum");
  assert.equal(evaluationReport.topology_aggregate.false_positives,
    topologySum("topology_edge_false_positives"),
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate FP must equal per-fixture FP sum");
  assert.equal(evaluationReport.topology_aggregate.false_negatives,
    topologySum("topology_edge_false_negatives"),
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate FN must equal per-fixture FN sum");
  const aggregate = evaluationReport.topology_aggregate;
  const aggregateCandidates = aggregate.true_positives + aggregate.false_positives;
  const aggregateReferences = aggregate.true_positives + aggregate.false_negatives;
  assert.ok(Number.isFinite(aggregate.precision) && aggregate.precision >= 0 && aggregate.precision <= 1,
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate precision must be finite and bounded");
  assert.ok(Number.isFinite(aggregate.recall) && aggregate.recall >= 0 && aggregate.recall <= 1,
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate recall must be finite and bounded");
  assert.ok(Math.abs(aggregate.precision - (aggregateCandidates ? aggregate.true_positives / aggregateCandidates : 0)) < 1e-12,
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate precision must agree with aggregate counts");
  assert.ok(Math.abs(aggregate.recall - (aggregateReferences ? aggregate.true_positives / aggregateReferences : 0)) < 1e-12,
    "REPORT-AGGREGATE-CONSISTENCY-001: aggregate recall must agree with aggregate counts");

  process.stdout.write("REPORT-AGGREGATE-CONSISTENCY-001: per-fixture and aggregate topology metrics reconcile.\\n");
  const reportPath = path.join(tempRoot, "raster_graph_structural_evaluation.json");
  fs.writeFileSync(reportPath, JSON.stringify(evaluationReport, null, 2) + "\\n");
  process.stdout.write("STRUCTURAL-EVALUATION: " + JSON.stringify(evaluationReport) + "\\n");
  process.stdout.write("PASS: detector executes on baseline and colored-node raster fixtures; candidates remain provisional.\\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
