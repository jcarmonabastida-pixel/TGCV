"use strict";

const assert = require("node:assert/strict");
const { resolveArrowDirection } = require("./arrow_direction_resolver.cjs");
const { inferArrowheadPresenceFromEvidence } = require("./raster_graph_candidate_detector.cjs");

const score = (support_ratio, tested_samples = 40) => ({ support_ratio, tested_samples });
const edge = (at_from, at_to) => ({ arrowhead_evidence: { at_from, at_to } });

function testCanvasPresenceSignalMarksNoPairedVAsNotDetected() {
  const result = inferArrowheadPresenceFromEvidence({
    arrowhead_hypotheses: {
      at_from: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0, right_arm_support_ratio: 0,
        bilateral_off_axis_support_ratio: 0
      }}],
      at_to: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0, right_arm_support_ratio: 0,
        bilateral_off_axis_support_ratio: 0
      }}]
    }
  });
  assert.equal(result, false);
}
function testCanvasPresenceSignalDoesNotTreatMissingHypothesesAsAbsence() {
  assert.equal(inferArrowheadPresenceFromEvidence({
    arrowhead_hypotheses: { at_from: [], at_to: [] }
  }), null, "missing endpoint hypotheses are unknown, not evidence of no arrowhead");
  assert.equal(inferArrowheadPresenceFromEvidence({}), null,
    "missing arrowhead evidence must remain unknown");
}
function testCanvasPresenceSignalKeepsMalformedDiagnosticsUnknown() {
  assert.equal(inferArrowheadPresenceFromEvidence({
    arrowhead_hypotheses: {
      at_from: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0, right_arm_support_ratio: 0,
        bilateral_off_axis_support_ratio: 0
      }}],
      at_to: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0, right_arm_support_ratio: 0
        // Missing bilateral support: incomplete diagnostic, not evidence of absence.
      }}]
    }
  }), null, "incomplete V diagnostics must remain unknown");
  assert.equal(inferArrowheadPresenceFromEvidence({
    arrowhead_hypotheses: {
      at_from: [{ geometric_v_diagnostic: null }],
      at_to: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0, right_arm_support_ratio: 0,
        bilateral_off_axis_support_ratio: 0
      }}]
    }
  }), null, "missing geometric diagnostic must remain unknown");
}
function testCanvasPresenceSignalPreservesUncertainVAsPossible() {
  const result = inferArrowheadPresenceFromEvidence({
    arrowhead_hypotheses: {
      at_from: [{ geometric_v_diagnostic: {
        left_arm_support_ratio: 0.2, right_arm_support_ratio: 0.3,
        bilateral_off_axis_support_ratio: 0.1
      }}],
      at_to: []
    }
  });
  assert.equal(result, null, "uncertain/possible arrowhead evidence must not be labelled absent");
}
function testForwardArrow() {
  const result = resolveArrowDirection(edge(score(0.18), score(0.82)));
  assert.equal(result.direction, "source-to-target");
  assert.equal(result.direction_status, "candidate");
  assert.match(result.direction_reason, /human review required/);
}
function testReversedArrow() {
  const result = resolveArrowDirection(edge(score(0.88), score(0.21)));
  assert.equal(result.direction, "target-to-source");
  assert.equal(result.direction_status, "candidate");
}
function testAmbiguousEvidenceStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.61), score(0.58)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testStrokeWithoutArrowheadStaysUnresolved() {
  // A plain connector has no paired V-shaped tip evidence at either endpoint.
  const result = resolveArrowDirection(edge(score(0.09), score(0.09)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testArrowlessConnectorWithAsymmetricNoiseStaysUnresolved() {
  // Unequal endpoint scores alone must not invent a direction when geometry says no arrowhead exists.
  const result = resolveArrowDirection({
    arrowhead_evidence: {
      arrowhead_present: false,
      at_from: score(0.88),
      at_to: score(0.12)
    }
  });
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
  assert.match(result.direction_reason, /No arrowhead is detected/);
}
function testWeakEvidenceStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.49), score(0.12)));
  assert.equal(result.direction_status, "unresolved");
}
function testInsufficientSamplesStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.1, 5), score(0.9, 5)));
  assert.equal(result.direction_status, "unresolved");
}
function testMalformedEvidenceStaysUnresolved() {
  const result = resolveArrowDirection({ arrowhead_evidence: { at_from: null, at_to: score(0.9) } });
  assert.equal(result.direction_status, "unresolved");
}

function testEqualEndpointScoresStayUnresolved() {
  const result = resolveArrowDirection(edge(score(0.8), score(0.8)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testExactMinimumMarginStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.55), score(0.70)));
  assert.equal(result.direction_status, "unresolved",
    "margin equal to threshold must remain unresolved; a strict margin is required");
}
function testInsufficientSamplesAtOnlyOneEndpointStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.1, 40), score(0.9, 19)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testSupportAboveOneStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.2), score(1.01)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testNegativeSupportStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(-0.1), score(0.9)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testFractionalSampleCountStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(0.1, 40), score(0.9, 20.5)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}
function testNonFiniteSupportStaysUnresolved() {
  const result = resolveArrowDirection(edge(score(Number.NaN), score(0.9)));
  assert.equal(result.direction, "undetermined");
  assert.equal(result.direction_status, "unresolved");
}

testCanvasPresenceSignalMarksNoPairedVAsNotDetected();
testCanvasPresenceSignalPreservesUncertainVAsPossible();
testCanvasPresenceSignalKeepsMalformedDiagnosticsUnknown();
testCanvasPresenceSignalDoesNotTreatMissingHypothesesAsAbsence();
testForwardArrow();
testReversedArrow();
testAmbiguousEvidenceStaysUnresolved();
testStrokeWithoutArrowheadStaysUnresolved();
testArrowlessConnectorWithAsymmetricNoiseStaysUnresolved();
testWeakEvidenceStaysUnresolved();
testInsufficientSamplesStaysUnresolved();
testMalformedEvidenceStaysUnresolved();
testEqualEndpointScoresStayUnresolved();
testExactMinimumMarginStaysUnresolved();
testInsufficientSamplesAtOnlyOneEndpointStaysUnresolved();
testSupportAboveOneStaysUnresolved();
testNegativeSupportStaysUnresolved();
testFractionalSampleCountStaysUnresolved();
testNonFiniteSupportStaysUnresolved();
process.stdout.write("OCR-ARROW-DIRECTION-001: 19 resolver/integration-signal tests passed (Canvas no-V signal, Canvas uncertain-V preservation, malformed-diagnostic unknown handling, missing-hypothesis unknown handling, out-of-range support, negative support, fractional sample count, forward, reverse, ambiguous, no-arrow stroke, arrowless asymmetric-noise, weak, insufficient, malformed, tied, boundary-margin, one-endpoint-insufficient and non-finite evidence).\n");
