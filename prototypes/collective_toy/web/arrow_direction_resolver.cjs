"use strict";

/**
 * Conservative arrowhead resolver for raster edge candidates.
 * Scores are geometric evidence, not proof; uncertain cases remain unresolved.
 */
function resolveArrowDirection(edge, options = {}) {
  const minSupport = options.minSupport ?? 0.50;
  const minMargin = options.minMargin ?? 0.15;
  const minSamples = options.minSamples ?? 20;
  const atFrom = edge?.arrowhead_evidence?.at_from;
  const atTo = edge?.arrowhead_evidence?.at_to;
  if (edge?.arrowhead_evidence?.arrowhead_present === false) {
    return { direction: "undetermined", direction_status: "unresolved",
      direction_reason: "No arrowhead is detected; connector direction must remain unresolved." };
  }
  const valid = score => score &&
    Number.isFinite(score.support_ratio) &&
    score.support_ratio >= 0 &&
    score.support_ratio <= 1 &&
    Number.isFinite(score.tested_samples) &&
    Number.isInteger(score.tested_samples) &&
    score.tested_samples >= minSamples;

  if (!valid(atFrom) || !valid(atTo)) {
    return { direction: "undetermined", direction_status: "unresolved",
      direction_reason: "Insufficient arrowhead evidence at one or both endpoints." };
  }
  const fromScore = atFrom.support_ratio;
  const toScore = atTo.support_ratio;
  const margin = Math.abs(fromScore - toScore);
  if (Math.max(fromScore, toScore) < minSupport || margin < minMargin) {
    return { direction: "undetermined", direction_status: "unresolved",
      direction_reason: "Arrowhead evidence is weak or the endpoint scores are too close.",
      direction_evidence: { at_from: fromScore, at_to: toScore, margin } };
  }

  // A high endpoint support ratio alone can be produced by nearby connector
  // strokes. Require a minimally plausible two-arm arrowhead at the winning
  // endpoint before proposing a direction. These are conservative geometric
  // gates, not calibrated probabilities; failures remain unresolved.
  const winner = toScore > fromScore ? atTo : atFrom;
  const minBilateralOffAxisSupport = options.minBilateralOffAxisSupport ?? 0.25;
  const minArmSupport = options.minArmSupport ?? 0.55;
  const leftArm = winner?.left_support_ratio;
  const rightArm = winner?.right_support_ratio;
  const offAxis = winner?.off_axis_support_ratio;
  if (!Number.isFinite(offAxis) || offAxis < minBilateralOffAxisSupport ||
      !Number.isFinite(leftArm) || leftArm < minArmSupport ||
      !Number.isFinite(rightArm) || rightArm < minArmSupport) {
    return { direction: "undetermined", direction_status: "unresolved",
      direction_reason: "Endpoint support is asymmetric, but the winning endpoint lacks sufficient two-arm arrowhead geometry.",
      direction_evidence: { at_from: fromScore, at_to: toScore, margin,
        winning_endpoint: toScore > fromScore ? "to" : "from",
        winning_off_axis_support: Number.isFinite(offAxis) ? offAxis : null,
        winning_left_arm_support: Number.isFinite(leftArm) ? leftArm : null,
        winning_right_arm_support: Number.isFinite(rightArm) ? rightArm : null } };
  }

  if (toScore > fromScore) {
    return { direction: "source-to-target", direction_status: "candidate",
      direction_reason: "Arrowhead evidence is stronger at the target endpoint; human review required.",
      direction_evidence: { at_from: fromScore, at_to: toScore, margin } };
  }
  return { direction: "target-to-source", direction_status: "candidate",
    direction_reason: "Arrowhead evidence is stronger at the source endpoint; human review required.",
    direction_evidence: { at_from: fromScore, at_to: toScore, margin } };
}

module.exports = { resolveArrowDirection };
