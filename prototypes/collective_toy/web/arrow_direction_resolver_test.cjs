"use strict";

const assert = require("node:assert/strict");
const { resolveArrowDirection } = require("./arrow_direction_resolver.cjs");

const score = (support_ratio, tested_samples = 40) => ({ support_ratio, tested_samples });
const edge = (at_from, at_to) => ({ arrowhead_evidence: { at_from, at_to } });

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

testForwardArrow();
testReversedArrow();
testAmbiguousEvidenceStaysUnresolved();
testStrokeWithoutArrowheadStaysUnresolved();
testWeakEvidenceStaysUnresolved();
testInsufficientSamplesStaysUnresolved();
testMalformedEvidenceStaysUnresolved();
process.stdout.write("OCR-ARROW-DIRECTION-001: 7 resolver tests passed (forward, reverse, ambiguous, no-arrow stroke, weak, insufficient and malformed evidence).\n");
