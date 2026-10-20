"use strict";

/**
 * Conservative arrowhead resolver for raster edge candidates.
 * Scores are geometric evidence, not proof; uncertain cases remain unresolved.
 */
function resolveArrowDirection(edge, options = {}) {
  const minSupport = options.minSupport ?? 0.55;
  const minMargin = options.minMargin ?? 0.15;
  const minSamples = options.minSamples ?? 20;
  const atFrom = edge?.arrowhead_evidence?.at_from;
  const atTo = edge?.arrowhead_evidence?.at_to;
  const valid = score => score &&
    Number.isFinite(score.support_ratio) &&
    Number.isFinite(score.tested_samples) &&
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
