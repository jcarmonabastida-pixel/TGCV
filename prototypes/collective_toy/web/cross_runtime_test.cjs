const { chromium } = require("playwright");
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const os = require("node:os");
const assert = require("node:assert/strict");
const crypto = require("node:crypto");

function fixtures() {
  const base = {
    schema_version: "collective-toy-input-001",
    model_id: "toy-diamond-001",
    initial_state: "A",
    states: ["A", "B", "C", "D"],
    transitions: [
      { id: "t_ab", source: "A", target: "B" },
      { id: "t_ac", source: "A", target: "C" },
      { id: "t_bd", source: "B", target: "D" },
      { id: "t_cd", source: "C", target: "D" }
    ],
    relations: [],
    rule_profile: { type: "finite_deterministic_graph", version: "1" },
    scenarios: [
      { id: "baseline", disabled_transitions: [] },
      { id: "block_ac", disabled_transitions: ["t_ac"] }
    ],
    exploration: { max_depth: 4, max_trajectories: 1000 }
  };
  const clone = x => JSON.parse(JSON.stringify(x));
  const cases = [{ name: "diamond-reference", model: clone(base) }];

  const unicodeMetadata = clone(base);
  unicodeMetadata.model_id = "unicode-metadata-canonical-order";
  unicodeMetadata.relations = [{ id: "descriptive", metadata: { "\uE000": "bmp", "𐀀": "supplementary", count: 9007199254740991 } }];
  cases.push({ name: "unicode-metadata-canonical-order", model: unicodeMetadata });

  const cycle = clone(base);
  cycle.model_id = "cycle";
  cycle.transitions.push({ id: "t_ba", source: "B", target: "A" });
  cycle.exploration.max_depth = 3;
  cases.push({ name: "cycle-depth-bound", model: cycle });

  const unreachable = clone(base);
  unreachable.model_id = "unreachable-state";
  unreachable.states.push("Z");
  cases.push({ name: "unreachable-state", model: unreachable });

  const terminal = clone(base);
  terminal.model_id = "initial-terminal";
  terminal.initial_state = "D";
  cases.push({ name: "initial-state-terminal", model: terminal });

  const zeroDepth = clone(base);
  zeroDepth.model_id = "zero-depth";
  zeroDepth.exploration.max_depth = 0;
  cases.push({ name: "depth-zero", model: zeroDepth });

  const capped = clone(base);
  capped.model_id = "trajectory-cap";
  capped.exploration.max_trajectories = 1;
  cases.push({ name: "trajectory-limit", model: capped });

  const multiple = clone(base);
  multiple.model_id = "multiple-interventions";
  multiple.scenarios.push(
    { id: "block_ab", disabled_transitions: ["t_ab"] },
    { id: "block_both", disabled_transitions: ["t_ab", "t_ac"] }
  );
  cases.push({ name: "multiple-interventions", model: multiple });
  const interventionOrderReference = clone(base);
  interventionOrderReference.model_id = "intervention-order-invariance";
  interventionOrderReference.rule_profile = { type: "relation_guarded_graph", version: "1" };
  interventionOrderReference.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  interventionOrderReference.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "intervention-order-reference", model: interventionOrderReference });

  const interventionOrderPermuted = clone(interventionOrderReference);
  interventionOrderPermuted.scenarios[1].disabled_transitions.reverse();
  cases.push({
    name: "intervention-order-permuted",
    model: interventionOrderPermuted,
    interventionPermutationOf: "intervention-order-reference"
  });


  const interventionComposition = clone(base);
  interventionComposition.model_id = "intervention-composition-order";
  interventionComposition.rule_profile = { type: "relation_guarded_graph", version: "1" };
  interventionComposition.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  interventionComposition.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] },
    { id: "disable_both_reversed", disabled_transitions: ["t_ac", "t_ab"] }
  ];
  cases.push({ name: "intervention-composition-order", model: interventionComposition });

  const scenarioOrderReference = clone(base);
  scenarioOrderReference.model_id = "scenario-order-invariance";
  scenarioOrderReference.rule_profile = { type: "relation_guarded_graph", version: "1" };
  scenarioOrderReference.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  scenarioOrderReference.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] }
  ];
  cases.push({ name: "scenario-order-reference", model: scenarioOrderReference });
  const scenarioOrderPermuted = clone(scenarioOrderReference);
  scenarioOrderPermuted.scenarios.reverse();
  cases.push({
    name: "scenario-order-permuted",
    model: scenarioOrderPermuted,
    scenarioPermutationOf: "scenario-order-reference"
  });

  const transitionOrderReference = clone(base);
  transitionOrderReference.model_id = "transition-order-invariance";
  cases.push({ name: "transition-order-reference", model: transitionOrderReference });
  const transitionOrderPermuted = clone(transitionOrderReference);
  transitionOrderPermuted.transitions.reverse();
  cases.push({
    name: "transition-order-permuted",
    model: transitionOrderPermuted,
    transitionPermutationOf: "transition-order-reference"
  });

  const stateOrderReference = clone(base);
  stateOrderReference.model_id = "state-order-invariance";
  cases.push({ name: "state-order-reference", model: stateOrderReference });
  const stateOrderPermuted = clone(stateOrderReference);
  stateOrderPermuted.states.reverse();
  cases.push({
    name: "state-order-permuted",
    model: stateOrderPermuted,
    statePermutationOf: "state-order-reference"
  });

  const singleSemanticGuard = clone(base);
  singleSemanticGuard.model_id = "single-semantic-guard";
  singleSemanticGuard.rule_profile = { type: "relation_guarded_graph", version: "1" };
  singleSemanticGuard.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  cases.push({ name: "single-semantic-guard", model: singleSemanticGuard });
  const duplicatedSemanticGuard = clone(singleSemanticGuard);
  duplicatedSemanticGuard.model_id = "duplicated-semantic-guard";
  duplicatedSemanticGuard.relations.push({
    id: "r_guard_bd_by_ab_duplicate", type: "requires_transition_enabled",
    transition_id: "t_bd", requires_transition_id: "t_ab"
  });
  cases.push({ name: "duplicated-semantic-guard", model: duplicatedSemanticGuard,
    duplicateSemanticGuardOf: "single-semantic-guard" });

  const conjunctiveGuards = clone(base);
  conjunctiveGuards.model_id = "same-target-conjunctive-guards";
  conjunctiveGuards.rule_profile = { type: "relation_guarded_graph", version: "1" };
  conjunctiveGuards.relations = [
    { id: "r_bd_requires_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_bd_requires_ac", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ac" }
  ];
  conjunctiveGuards.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "same-target-conjunctive-guards", model: conjunctiveGuards });

  const reversedConjunctiveGuards = clone(conjunctiveGuards);
  reversedConjunctiveGuards.relations.reverse();
  cases.push({ name: "same-target-conjunctive-guards-reversed",
    model: reversedConjunctiveGuards, relationOrderOf: "same-target-conjunctive-guards" });

  const disabledOrder = clone(base);
  disabledOrder.model_id = "disabled-transition-order";
  disabledOrder.rule_profile = { type: "relation_guarded_graph", version: "1" };
  disabledOrder.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  disabledOrder.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "disabled-transition-order", model: disabledOrder });
  const reversedDisabledOrder = clone(disabledOrder);
  // Preserve model identity so only disabled-transition serialization order differs.
  reversedDisabledOrder.model_id = disabledOrder.model_id;
  reversedDisabledOrder.scenarios[1].disabled_transitions.reverse();
  cases.push({ name: "disabled-transition-order-reversed", model: reversedDisabledOrder,
    disabledTransitionOrderOf: "disabled-transition-order" });

  const combinedInterventions = clone(base);
  combinedInterventions.model_id = "combined-disabling-interventions-monotonicity";
  combinedInterventions.rule_profile = { type: "relation_guarded_graph", version: "1" };
  combinedInterventions.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  combinedInterventions.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "combined-disabling-interventions-monotonicity", model: combinedInterventions,
    monotonicInterventions: true });

  const disconnectedReference = clone(base);
  disconnectedReference.model_id = "disconnected-component-reference";
  cases.push({ name: "disconnected-component-reference", model: disconnectedReference });
  const disconnectedAugmented = clone(disconnectedReference);
  disconnectedAugmented.model_id = "disconnected-component-augmented";
  disconnectedAugmented.states.push("X", "Y");
  disconnectedAugmented.transitions.push({ id: "t_xy", source: "X", target: "Y" });
  cases.push({ name: "disconnected-component-augmented", model: disconnectedAugmented,
    disconnectedComponentOf: "disconnected-component-reference" });

  const cappedDisconnectedReference = clone(base);
  cappedDisconnectedReference.model_id = "disconnected-component-capped-reference";
  cappedDisconnectedReference.transitions.push({ id: "t_ba", source: "B", target: "A" });
  cappedDisconnectedReference.exploration.max_depth = 3;
  cases.push({ name: "disconnected-component-capped-reference", model: cappedDisconnectedReference,
    expectedTruncation: true });
  const cappedDisconnectedAugmented = clone(cappedDisconnectedReference);
  cappedDisconnectedAugmented.model_id = "disconnected-component-capped-augmented";
  cappedDisconnectedAugmented.states.push("X", "Y");
  cappedDisconnectedAugmented.transitions.push({ id: "t_xy", source: "X", target: "Y" });
  cases.push({ name: "disconnected-component-capped-augmented", model: cappedDisconnectedAugmented,
    disconnectedComponentOf: "disconnected-component-capped-reference", expectedTruncation: true });

  const scenarioOrderIsolation = clone(base);
  scenarioOrderIsolation.model_id = "scenario-order-isolation";
  scenarioOrderIsolation.rule_profile = { type: "relation_guarded_graph", version: "1" };
  scenarioOrderIsolation.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  scenarioOrderIsolation.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] }
  ];
  cases.push({ name: "scenario-order-isolation", model: scenarioOrderIsolation });
  const reversedScenarioOrder = clone(scenarioOrderIsolation);
  reversedScenarioOrder.model_id = "scenario-order-isolation-reversed";
  reversedScenarioOrder.scenarios.reverse();
  cases.push({ name: "scenario-order-isolation-reversed", model: reversedScenarioOrder,
    scenarioOrderIsolationOf: "scenario-order-isolation" });

  const unguardedBaseline = clone(base);
  unguardedBaseline.model_id = "unguarded-baseline-neutrality";
  unguardedBaseline.scenarios = [{ id: "baseline", disabled_transitions: [] }];
  cases.push({ name: "unguarded-baseline-neutrality", model: unguardedBaseline });
  const guardedBaseline = clone(unguardedBaseline);
  guardedBaseline.model_id = "guarded-baseline-neutrality";
  guardedBaseline.rule_profile = { type: "relation_guarded_graph", version: "1" };
  guardedBaseline.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  cases.push({ name: "guarded-baseline-neutrality", model: guardedBaseline,
    guardNeutralityOf: "unguarded-baseline-neutrality" });

  const relationGuardLocality = clone(base);
  relationGuardLocality.model_id = "relation-guard-locality";
  relationGuardLocality.rule_profile = { type: "relation_guarded_graph", version: "1" };
  relationGuardLocality.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  relationGuardLocality.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] }
  ];
  cases.push({ name: "relation-guard-locality", model: relationGuardLocality });

  const singleGuardMonotonicity = clone(base);
  singleGuardMonotonicity.model_id = "single-guard-monotonicity";
  singleGuardMonotonicity.rule_profile = { type: "relation_guarded_graph", version: "1" };
  singleGuardMonotonicity.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  singleGuardMonotonicity.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_ac", disabled_transitions: ["t_ac"] },
    { id: "disable_both", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "single-guard-monotonicity", model: singleGuardMonotonicity });
  const extendedGuardMonotonicity = clone(singleGuardMonotonicity);
  extendedGuardMonotonicity.model_id = "extended-guard-monotonicity";
  extendedGuardMonotonicity.relations.push({
    id: "r_guard_cd_by_ac", type: "requires_transition_enabled",
    transition_id: "t_cd", requires_transition_id: "t_ac"
  });
  cases.push({ name: "extended-guard-monotonicity", model: extendedGuardMonotonicity,
    relationAdditionMonotonicityOf: "single-guard-monotonicity" });

  const relationGuardMonotonicity = clone(base);
  relationGuardMonotonicity.model_id = "relation-guard-intervention-monotonicity";
  relationGuardMonotonicity.rule_profile = { type: "relation_guarded_graph", version: "1" };
  relationGuardMonotonicity.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd_by_ac", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  relationGuardMonotonicity.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] }
  ];
  cases.push({ name: "relation-guard-intervention-monotonicity", model: relationGuardMonotonicity });

  const interventionMonotonicity = clone(base);
  interventionMonotonicity.model_id = "intervention-reachability-monotonicity";
  cases.push({ name: "intervention-reachability-monotonicity", model: interventionMonotonicity });

  const unreachableIntervention = clone(base);
  unreachableIntervention.model_id = "unreachable-transition-non-interference";
  unreachableIntervention.scenarios.push({
    id: "block_ac_and_cd",
    disabled_transitions: ["t_ac", "t_cd"]
  });
  cases.push({ name: "unreachable-transition-non-interference", model: unreachableIntervention });

  const directAndGuardChain = clone(base);
  directAndGuardChain.model_id = "direct-intervention-and-nonrecursive-guard-chain";
  directAndGuardChain.states = ["A", "B", "C", "D"];
  directAndGuardChain.initial_state = "A";
  directAndGuardChain.transitions = [
    { id: "t_ab", source: "A", target: "B" },
    { id: "t_bc", source: "B", target: "C" },
    { id: "t_cd", source: "C", target: "D" }
  ];
  directAndGuardChain.rule_profile = { type: "relation_guarded_graph", version: "1" };
  directAndGuardChain.relations = [
    { id: "r_bc_requires_ab", type: "requires_transition_enabled", transition_id: "t_bc", requires_transition_id: "t_ab" },
    { id: "r_cd_requires_bc", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_bc" }
  ];
  directAndGuardChain.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab", disabled_transitions: ["t_ab"] },
    { id: "disable_bc", disabled_transitions: ["t_bc"] },
    { id: "disable_cd", disabled_transitions: ["t_cd"] }
  ];
  cases.push({ name: "direct-intervention-and-nonrecursive-guard-chain", model: directAndGuardChain });

  const guarded = clone(base);
  guarded.model_id = "relation-guarded-availability";
  guarded.rule_profile = { type: "relation_guarded_graph", version: "1" };
  guarded.relations = [{
    id: "r_guard_bd",
    type: "requires_transition_enabled",
    transition_id: "t_bd",
    requires_transition_id: "t_ab"
  }];
  guarded.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_prerequisite", disabled_transitions: ["t_ab"] },
    { id: "block_ac", disabled_transitions: ["t_ac"] }
  ];
  cases.push({ name: "relation-guarded-availability", model: guarded });

  const multiGuard = clone(base);
  multiGuard.model_id = "multiple-relation-guards";
  multiGuard.rule_profile = { type: "relation_guarded_graph", version: "1" };
  multiGuard.relations = [
    { id: "r_guard_bd", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_cd", type: "requires_transition_enabled", transition_id: "t_cd", requires_transition_id: "t_ac" }
  ];
  multiGuard.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_both_prerequisites", disabled_transitions: ["t_ab", "t_ac"] }
  ];
  cases.push({ name: "multiple-relation-guards", model: multiGuard });

  const sameGuarded = clone(base);
  sameGuarded.model_id = "multiple-guards-same-transition";
  sameGuarded.rule_profile = { type: "relation_guarded_graph", version: "1" };
  sameGuarded.relations = [
    { id: "r_guard_bd_by_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" },
    { id: "r_guard_bd_by_ac", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ac" }
  ];
  sameGuarded.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab_only", disabled_transitions: ["t_ab"] }
  ];
  cases.push({ name: "multiple-guards-same-transition", model: sameGuarded });

  const cyclicGuards = clone(base);
  cyclicGuards.model_id = "cyclic-guard-relations-explicit-only";
  cyclicGuards.rule_profile = { type: "relation_guarded_graph", version: "1" };
  cyclicGuards.relations = [
    { id: "r_ab_requires_bd", type: "requires_transition_enabled", transition_id: "t_ab", requires_transition_id: "t_bd" },
    { id: "r_bd_requires_ab", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  cyclicGuards.scenarios = [
    { id: "baseline", disabled_transitions: [] },
    { id: "disable_ab_only", disabled_transitions: ["t_ab"] }
  ];
  cases.push({ name: "cyclic-guard-relations-explicit-only", model: cyclicGuards });

  const guardedCycle = clone(guarded);
  guardedCycle.model_id = "relation-guarded-cycle-and-bounds";
  guardedCycle.transitions.push({ id: "t_ba", source: "B", target: "A" });
  guardedCycle.relations = [
    { id: "r_guard_bd", type: "requires_transition_enabled", transition_id: "t_bd", requires_transition_id: "t_ab" }
  ];
  guardedCycle.exploration = { max_depth: 3, max_trajectories: 2 };
  cases.push({ name: "relation-guarded-cycle-and-bounds", model: guardedCycle });

  const depthBoundaryPending = clone(base);
  depthBoundaryPending.model_id = "depth-boundary-pending-transition";
  depthBoundaryPending.states = ["A", "B", "C"];
  depthBoundaryPending.initial_state = "A";
  depthBoundaryPending.transitions = [
    { id: "t_ab", source: "A", target: "B" },
    { id: "t_bc", source: "B", target: "C" }
  ];
  depthBoundaryPending.scenarios = [{ id: "baseline", disabled_transitions: [] }];
  depthBoundaryPending.exploration = { max_depth: 1, max_trajectories: 10 };
  cases.push({ name: "depth-boundary-pending-transition", model: depthBoundaryPending, expectedTruncation: true });

  const depthBoundaryTerminal = clone(depthBoundaryPending);
  depthBoundaryTerminal.model_id = "depth-boundary-terminal-after-one-more-level";
  depthBoundaryTerminal.exploration.max_depth = 2;
  cases.push({ name: "depth-boundary-terminal-after-one-more-level", model: depthBoundaryTerminal, expectedTruncation: false });

  const combinedCaps = clone(base);
  combinedCaps.model_id = "combined-depth-and-trajectory-caps";
  combinedCaps.states = ["A", "B", "C", "D", "E"];
  combinedCaps.initial_state = "A";
  combinedCaps.transitions = [
    { id: "t_ab", source: "A", target: "B" },
    { id: "t_bd", source: "B", target: "D" },
    { id: "t_ac", source: "A", target: "C" },
    { id: "t_ce", source: "C", target: "E" }
  ];
  combinedCaps.scenarios = [{ id: "baseline", disabled_transitions: [] }];
  combinedCaps.exploration = { max_depth: 1, max_trajectories: 1 };
  cases.push({ name: "combined-depth-and-trajectory-caps", model: combinedCaps, expectedTruncation: true });

  const trajectoryCapAfterDepthRelaxed = clone(combinedCaps);
  trajectoryCapAfterDepthRelaxed.model_id = "trajectory-cap-after-depth-relaxed";
  trajectoryCapAfterDepthRelaxed.exploration = { max_depth: 2, max_trajectories: 1 };
  cases.push({ name: "trajectory-cap-after-depth-relaxed", model: trajectoryCapAfterDepthRelaxed, expectedTruncation: true });

  const bothCapsRelaxed = clone(combinedCaps);
  bothCapsRelaxed.model_id = "both-exploration-caps-relaxed";
  bothCapsRelaxed.exploration = { max_depth: 2, max_trajectories: 2 };
  cases.push({ name: "both-exploration-caps-relaxed", model: bothCapsRelaxed, expectedTruncation: false });

  const exactTrajectoryCap = clone(base);
  exactTrajectoryCap.model_id = "exact-trajectory-cap-is-complete";
  exactTrajectoryCap.initial_state = "A";
  exactTrajectoryCap.states = ["A", "B"];
  exactTrajectoryCap.transitions = [{ id: "t_ab", source: "A", target: "B" }];
  exactTrajectoryCap.scenarios = [{ id: "baseline", disabled_transitions: [] }];
  exactTrajectoryCap.exploration = { max_depth: 4, max_trajectories: 1 };
  cases.push({ name: "exact-trajectory-cap-is-complete", model: exactTrajectoryCap });

  const terminalAtDepth = clone(exactTrajectoryCap);
  terminalAtDepth.model_id = "terminal-at-depth-boundary-is-complete";
  terminalAtDepth.exploration = { max_depth: 1, max_trajectories: 10 };
  cases.push({ name: "terminal-at-depth-boundary-is-complete", model: terminalAtDepth });

  return cases;
}

function generatedFixtures() {
  // Keep this helper local: fixtures() defines its own scoped clone helper.
  const clone = x => JSON.parse(JSON.stringify(x));
  // Deterministic pseudo-random generation: identical inputs on every CI run.
  let seed = 20261011;
  const random = () => {
    seed = (1664525 * seed + 1013904223) >>> 0;
    return seed / 4294967296;
  };
  const cases = [];
  const states = ["S0", "S1", "S2", "S3"];
  for (let n = 0; n < 12; n++) {
    const transitions = [];
    let id = 0;
    for (let i = 0; i < states.length - 1; i++) {
      transitions.push({ id: "g" + n + "_t" + id++, source: states[i], target: states[i + 1] });
    }
    for (let i = 0; i < states.length; i++) {
      for (let j = 0; j < states.length; j++) {
        if (random() < 0.22 && j !== i + 1) {
          transitions.push({ id: "g" + n + "_t" + id++, source: states[i], target: states[j] });
        }
      }
    }
    const disabled = transitions.length ? [transitions[Math.floor(random() * transitions.length)].id] : [];
    const model = {
      schema_version: "collective-toy-input-001",
      model_id: "generated-graph-" + String(n + 1).padStart(2, "0"),
      initial_state: "S0", states, transitions, relations: [],
      rule_profile: { type: "finite_deterministic_graph", version: "1" },
      scenarios: [
        { id: "baseline", disabled_transitions: [] },
        { id: "generated_intervention", disabled_transitions: disabled }
      ],
      exploration: { max_depth: 3 + (n % 3), max_trajectories: 20 + n }
    };
    cases.push({ name: model.model_id, model });

    // A paired profile-2 fixture exercises relation semantics on the same generated graph.
    const relationModel = clone(model);
    relationModel.model_id = "generated-relation-guard-" + String(n + 1).padStart(2, "0");
    relationModel.rule_profile = { type: "relation_guarded_graph", version: "1" };
    relationModel.relations = [{
      id: "generated_guard_" + n,
      type: "requires_transition_enabled",
      transition_id: transitions[1].id,
      requires_transition_id: transitions[0].id
    }];
    relationModel.scenarios = [
      { id: "baseline", disabled_transitions: [] },
      { id: "disable_prerequisite", disabled_transitions: [transitions[0].id] }
    ];
    cases.push({ name: relationModel.model_id, model: relationModel });

    // A second paired variant tests conjunction-like composition of two guards
    // on the same target transition; each guard observes explicit intervention.
    const multiGuardModel = clone(model);
    multiGuardModel.model_id = "generated-multi-guard-" + String(n + 1).padStart(2, "0");
    multiGuardModel.rule_profile = { type: "relation_guarded_graph", version: "1" };
    multiGuardModel.relations = [
      {
        id: "generated_multi_guard_a_" + n,
        type: "requires_transition_enabled",
        transition_id: transitions[2].id,
        requires_transition_id: transitions[0].id
      },
      {
        id: "generated_multi_guard_b_" + n,
        type: "requires_transition_enabled",
        transition_id: transitions[2].id,
        requires_transition_id: transitions[1].id
      }
    ];
    multiGuardModel.scenarios = [
      { id: "baseline", disabled_transitions: [] },
      { id: "disable_first_prerequisite", disabled_transitions: [transitions[0].id] },
      { id: "disable_second_prerequisite", disabled_transitions: [transitions[1].id] },
      { id: "disable_both_prerequisites", disabled_transitions: [transitions[0].id, transitions[1].id] }
    ];
    cases.push({ name: multiGuardModel.model_id, model: multiGuardModel });

    // Relation-dependency cycle: each guard targets the other transition.
    // Evaluation remains non-recursive and reads only explicit scenario disables.
    const cyclicGuardModel = clone(model);
    cyclicGuardModel.model_id = "generated-cyclic-guards-" + String(n + 1).padStart(2, "0");
    cyclicGuardModel.rule_profile = { type: "relation_guarded_graph", version: "1" };
    cyclicGuardModel.relations = [
      {
        id: "generated_cycle_guard_a_" + n,
        type: "requires_transition_enabled",
        transition_id: transitions[0].id,
        requires_transition_id: transitions[1].id
      },
      {
        id: "generated_cycle_guard_b_" + n,
        type: "requires_transition_enabled",
        transition_id: transitions[1].id,
        requires_transition_id: transitions[0].id
      }
    ];
    cyclicGuardModel.scenarios = [
      { id: "baseline", disabled_transitions: [] },
      { id: "disable_a", disabled_transitions: [transitions[0].id] },
      { id: "disable_b", disabled_transitions: [transitions[1].id] },
      { id: "disable_both", disabled_transitions: [transitions[0].id, transitions[1].id] }
    ];
    cases.push({ name: cyclicGuardModel.model_id, model: cyclicGuardModel });
    // Permuting relation declaration order must preserve semantic outputs and result hash.
    // Input hash must change because the serialized input array order changed.
    const permutedCycleModel = clone(cyclicGuardModel);
    permutedCycleModel.relations.reverse();
    cases.push({
      name: cyclicGuardModel.model_id + "-relation-order-permuted",
      model: permutedCycleModel,
      permutationOf: cyclicGuardModel.model_id
    });
  }
  return cases;
}

function invalidFixtures() {
  const base = {
    schema_version: "collective-toy-input-001",
    model_id: "invalid-base",
    initial_state: "A",
    states: ["A", "B"],
    transitions: [{ id: "t_ab", source: "A", target: "B" }],
    relations: [],
    rule_profile: { type: "finite_deterministic_graph", version: "1" },
    scenarios: [{ id: "baseline", disabled_transitions: [] }],
    exploration: { max_depth: 2, max_trajectories: 10 }
  };
  const clone = x => JSON.parse(JSON.stringify(x));
  const cases = [];
  let m = clone(base); m.model_id = "duplicate-state"; m.states.push("A");
  cases.push({ name: "duplicate-state", model: m });
  m = clone(base); m.model_id = "unknown-endpoint"; m.transitions[0].target = "Z";
  cases.push({ name: "unknown-endpoint", model: m });
  m = clone(base); m.model_id = "unknown-disabled-transition"; m.scenarios[0].disabled_transitions = ["nope"];
  cases.push({ name: "unknown-disabled-transition", model: m });
  m = clone(base); m.model_id = "missing-baseline"; m.scenarios = [{ id: "alt", disabled_transitions: [] }];
  cases.push({ name: "missing-baseline", model: m });
  m = clone(base); m.model_id = "negative-depth"; m.exploration.max_depth = -1;
  cases.push({ name: "negative-depth", model: m });
  m = clone(base); m.model_id = "duplicate-transition-id"; m.transitions.push({ id: "t_ab", source: "B", target: "A" });
  cases.push({ name: "duplicate-transition-id", model: m });
  const guarded = clone(base);
  guarded.rule_profile = { type: "relation_guarded_graph", version: "1" };
  guarded.relations = [{
    id: "r_bad",
    type: "requires_transition_enabled",
    transition_id: "t_ab",
    requires_transition_id: "missing"
  }];
  cases.push({ name: "unknown-relation-prerequisite", model: guarded });

  const badType = clone(base);
  badType.rule_profile = { type: "relation_guarded_graph", version: "1" };
  badType.relations = [{
    id: "r_bad", type: "unknown_relation",
    transition_id: "t_ab", requires_transition_id: "t_ab"
  }];
  cases.push({ name: "unknown-relation-type", model: badType });

  const duplicateRelation = clone(base);
  duplicateRelation.rule_profile = { type: "relation_guarded_graph", version: "1" };
  const relation = {
    id: "r_dup", type: "requires_transition_enabled",
    transition_id: "t_ab", requires_transition_id: "t_ab"
  };
  duplicateRelation.relations = [relation, { ...relation }];
  cases.push({ name: "duplicate-relation-id", model: duplicateRelation });

  const unknownGuarded = clone(base);
  unknownGuarded.rule_profile = { type: "relation_guarded_graph", version: "1" };
  unknownGuarded.relations = [{
    id: "r_unknown_guarded", type: "requires_transition_enabled",
    transition_id: "missing", requires_transition_id: "t_ab"
  }];
  cases.push({ name: "unknown-guarded-transition", model: unknownGuarded });

  const malformedRelation = clone(base);
  malformedRelation.rule_profile = { type: "relation_guarded_graph", version: "1" };
  malformedRelation.relations = [{
    id: "r_missing_field", type: "requires_transition_enabled", transition_id: "t_ab"
  }];
  cases.push({ name: "malformed-relation-fields", model: malformedRelation });

  const listInitialState = clone(base);
  listInitialState.initial_state = [];
  cases.push({ name: "initial-state-list", model: listInitialState });

  const objectInitialState = clone(base);
  objectInitialState.initial_state = {};
  cases.push({ name: "initial-state-object", model: objectInitialState });

  const invalidModelId = clone(base);
  invalidModelId.model_id = "   ";
  cases.push({ name: "blank-model-id", model: invalidModelId });

  const missingInitial = clone(base);
  delete missingInitial.initial_state;
  cases.push({ name: "missing-initial-state", model: missingInitial });

  const nonObjectTransition = clone(base);
  nonObjectTransition.transitions = [null];
  cases.push({ name: "non-object-transition", model: nonObjectTransition });

  const nonObjectScenario = clone(base);
  nonObjectScenario.scenarios = [null];
  cases.push({ name: "non-object-scenario", model: nonObjectScenario });

  const duplicateScenario = clone(base);
  duplicateScenario.scenarios.push({ id: "baseline", disabled_transitions: [] });
  cases.push({ name: "duplicate-scenario-id", model: duplicateScenario });

  const wrongDisabledType = clone(base);
  wrongDisabledType.scenarios[0].disabled_transitions = "t_ab";
  cases.push({ name: "disabled-transitions-not-list", model: wrongDisabledType });

  const wrongExploration = clone(base);
  wrongExploration.exploration = [];
  cases.push({ name: "exploration-not-object", model: wrongExploration });

  const booleanDepth = clone(base);
  booleanDepth.exploration.max_depth = true;
  cases.push({ name: "boolean-depth", model: booleanDepth });

  const zeroTrajectoryCap = clone(base);
  zeroTrajectoryCap.exploration.max_trajectories = 0;
  cases.push({ name: "zero-trajectory-cap", model: zeroTrajectoryCap });

  const depthOverCap = clone(base);
  depthOverCap.exploration.max_depth = 101;
  cases.push({ name: "depth-over-resource-cap", model: depthOverCap });

  const trajectoriesOverCap = clone(base);
  trajectoriesOverCap.exploration.max_trajectories = 10001;
  cases.push({ name: "trajectory-cap-over-resource-limit", model: trajectoriesOverCap });

  const tooManyStates = clone(base);
  tooManyStates.states = Array.from({ length: 501 }, (_, i) => "S" + i);
  tooManyStates.initial_state = "S0";
  tooManyStates.transitions = [];
  cases.push({ name: "state-count-over-resource-cap", model: tooManyStates });

  const tooManyTransitions = clone(base);
  tooManyTransitions.transitions = Array.from({ length: 2001 }, (_, i) => ({
    id: "t" + i, source: "A", target: "A"
  }));
  cases.push({ name: "transition-count-over-resource-cap", model: tooManyTransitions });

  const fractionalMetadata = clone(base);
  fractionalMetadata.relations = [{ id: "descriptive", metadata: { score: 1.5 } }];
  cases.push({ name: "fractional-metadata-number", model: fractionalMetadata });

  const unsafeIntegerMetadata = clone(base);
  unsafeIntegerMetadata.relations = [{ id: "descriptive", metadata: { count: 9007199254740992 } }];
  cases.push({ name: "unsafe-integer-metadata", model: unsafeIntegerMetadata });

  const unpairedSurrogateMetadata = clone(base);
  unpairedSurrogateMetadata.relations = [{ id: "descriptive", metadata: { label: "\ud800" } }];
  cases.push({ name: "unpaired-surrogate-metadata", model: unpairedSurrogateMetadata });

  const unknownTopLevel = clone(base); unknownTopLevel.unexpected_top_level = true;
  cases.push({ name: "unknown-top-level-field", model: unknownTopLevel });

  const unknownTransitionField = clone(base); unknownTransitionField.transitions[0].unexpected = true;
  cases.push({ name: "unknown-transition-field", model: unknownTransitionField });

  const unknownScenarioField = clone(base); unknownScenarioField.scenarios[0].unexpected = true;
  cases.push({ name: "unknown-scenario-field", model: unknownScenarioField });

  const unknownExplorationField = clone(base); unknownExplorationField.exploration.unexpected = true;
  cases.push({ name: "unknown-exploration-field", model: unknownExplorationField });

  const unknownProfileField = clone(base); unknownProfileField.rule_profile.unexpected = true;
  cases.push({ name: "unknown-rule-profile-field", model: unknownProfileField });

  const unknownRelationFieldNested = clone(base);
  unknownRelationFieldNested.rule_profile = { type: "relation_guarded_graph", version: "1" };
  unknownRelationFieldNested.transitions.push({ id: "t_ba", source: "B", target: "A" });
  unknownRelationFieldNested.relations = [{
    id: "r_schema", type: "requires_transition_enabled",
    transition_id: "t_ab", requires_transition_id: "t_ba", unexpected: true
  }];
  cases.push({ name: "unknown-relation-field", model: unknownRelationFieldNested });

  const selfGuard = clone(base);
  selfGuard.rule_profile = { type: "relation_guarded_graph", version: "1" };
  selfGuard.relations = [{
    id: "r_self", type: "requires_transition_enabled",
    transition_id: "t_ab", requires_transition_id: "t_ab"
  }];
  cases.push({ name: "self-referential-guard", model: selfGuard });

  // Systematic missing-required-field and wrong-container-type cases.
  for (const field of ["schema_version", "model_id", "states", "transitions",
                       "rule_profile", "scenarios", "exploration"]) {
    const missing = clone(base);
    missing.model_id = "missing-required-" + field;
    delete missing[field];
    cases.push({ name: "missing-required-" + field, model: missing });
  }
  const statesNotList = clone(base);
  statesNotList.states = "A";
  cases.push({ name: "states-not-list", model: statesNotList });

  const transitionsNotList = clone(base);
  transitionsNotList.transitions = {};
  cases.push({ name: "transitions-not-list", model: transitionsNotList });

  const profileNotObject = clone(base);
  profileNotObject.rule_profile = null;
  cases.push({ name: "rule-profile-not-object", model: profileNotObject });

  const relationsNotList = clone(base);
  relationsNotList.rule_profile = { type: "relation_guarded_graph", version: "1" };
  relationsNotList.relations = {};
  cases.push({ name: "relations-not-list", model: relationsNotList });

  const duplicateDisabled = clone(base);
  duplicateDisabled.scenarios[0].disabled_transitions = ["t_ab", "t_ab"];
  cases.push({ name: "duplicate-disabled-transition", model: duplicateDisabled });

  // Nested-field presence, non-empty identifiers, and numeric type boundaries.
  for (const field of ["id", "source", "target"]) {
    const missing = clone(base);
    delete missing.transitions[0][field];
    cases.push({ name: "missing-transition-" + field, model: missing });
  }
  for (const field of ["id", "source", "target"]) {
    const empty = clone(base);
    empty.transitions[0][field] = "";
    cases.push({ name: "empty-transition-" + field, model: empty });
  }

  const fractionalDepth = clone(base);
  fractionalDepth.exploration.max_depth = 1.5;
  cases.push({ name: "fractional-max-depth", model: fractionalDepth });

  const booleanTrajectories = clone(base);
  booleanTrajectories.exploration.max_trajectories = true;
  cases.push({ name: "boolean-max-trajectories", model: booleanTrajectories });

  const unknownProfileType = clone(base);
  unknownProfileType.rule_profile = { type: "unknown_graph", version: "1" };
  cases.push({ name: "unknown-rule-profile-type", model: unknownProfileType });

  const emptyDisabledId = clone(base);
  emptyDisabledId.scenarios[0].disabled_transitions = [""];
  cases.push({ name: "empty-disabled-transition-id", model: emptyDisabledId });

  // Nested relation/scenario/exploration field coverage.
  const validRelation = {
    id: "r_schema", type: "requires_transition_enabled",
    transition_id: "t_ab", requires_transition_id: "t_ba"
  };
  for (const field of ["id", "type", "transition_id", "requires_transition_id"]) {
    const missing = clone(base);
    missing.rule_profile = { type: "relation_guarded_graph", version: "1" };
    missing.transitions.push({ id: "t_ba", source: "B", target: "A" });
    const relation = clone(validRelation);
    delete relation[field];
    missing.relations = [relation];
    cases.push({ name: "missing-relation-" + field, model: missing });
  }

  for (const field of ["id", "transition_id", "requires_transition_id"]) {
    const empty = clone(base);
    empty.rule_profile = { type: "relation_guarded_graph", version: "1" };
    empty.transitions.push({ id: "t_ba", source: "B", target: "A" });
    const relation = clone(validRelation);
    relation[field] = "";
    empty.relations = [relation];
    cases.push({ name: "empty-relation-" + field, model: empty });
  }

  const nonObjectRelation = clone(base);
  nonObjectRelation.rule_profile = { type: "relation_guarded_graph", version: "1" };
  nonObjectRelation.transitions.push({ id: "t_ba", source: "B", target: "A" });
  nonObjectRelation.relations = [null];
  cases.push({ name: "non-object-relation", model: nonObjectRelation });

  const emptyScenarioId = clone(base);
  emptyScenarioId.scenarios[0].id = "";
  cases.push({ name: "empty-scenario-id", model: emptyScenarioId });

  const missingScenarioId = clone(base);
  delete missingScenarioId.scenarios[0].id;
  cases.push({ name: "missing-scenario-id", model: missingScenarioId });

  const nonStringDisabled = clone(base);
  nonStringDisabled.scenarios[0].disabled_transitions = [1];
  cases.push({ name: "non-string-disabled-transition-id", model: nonStringDisabled });

  for (const field of ["max_depth", "max_trajectories"]) {
    const missing = clone(base);
    delete missing.exploration[field];
    cases.push({ name: "missing-exploration-" + field, model: missing });
  }

  // Deterministic malformed-input mutation matrix mirrored by Python unit tests.
  const mutationCases = [];
  const addMutation = (name, mutate) => {
    const model = clone(base);
    mutate(model);
    mutationCases.push({ name, model });
  };
  addMutation("mutated-states-container", m => { m.states = {}; });
  addMutation("mutated-transitions-container", m => { m.transitions = null; });
  addMutation("mutated-transition-item", m => { m.transitions = [null]; });
  addMutation("mutated-transition-id-type", m => { m.transitions[0].id = 7; });
  addMutation("mutated-transition-source-type", m => { m.transitions[0].source = null; });
  addMutation("mutated-transition-target-type", m => { m.transitions[0].target = []; });
  addMutation("mutated-scenarios-container", m => { m.scenarios = {}; });
  addMutation("mutated-scenario-item", m => { m.scenarios = [null]; });
  addMutation("mutated-scenario-id-empty", m => { m.scenarios[0].id = ""; });
  addMutation("mutated-disabled-transition-item", m => { m.scenarios[0].disabled_transitions = [null]; });
  addMutation("mutated-exploration-container", m => { m.exploration = null; });
  addMutation("mutated-depth-type", m => { m.exploration.max_depth = "2"; });
  addMutation("mutated-trajectory-cap-negative", m => { m.exploration.max_trajectories = -1; });
  addMutation("mutated-relations-container", m => { m.relations = {}; });
  addMutation("mutated-relation-item", m => {
    m.rule_profile = { type: "relation_guarded_graph", version: "1" };
    m.relations = [null];
  });
  addMutation("mutated-relation-type", m => {
    m.rule_profile = { type: "relation_guarded_graph", version: "1" };
    m.relations = [{ id: "r_mut", type: "unknown", transition_id: "t_ab", requires_transition_id: "t_ac" }];
  });
  addMutation("mutated-relation-reference", m => {
    m.rule_profile = { type: "relation_guarded_graph", version: "1" };
    m.relations = [{ id: "r_mut", type: "requires_transition_enabled", transition_id: "missing", requires_transition_id: "t_ab" }];
  });
  addMutation("mutated-duplicate-scenario-id", m => { m.scenarios.push(clone(m.scenarios[0])); });
  addMutation("mutated-initial-state-boolean", m => { m.initial_state = false; });
  cases.push(...mutationCases);

  return cases;
}

function pythonRejects(engineDir, model) {
  const script = "import json, sys; from collective_toy_engine_001 import run_model; run_model(json.load(sys.stdin))";
  const result = spawnSync("python", ["-c", script], {
    cwd: engineDir, input: JSON.stringify(model), encoding: "utf8"
  });
  return result.status !== 0;
}

function runPython(engineDir, model) {
  const script = "import json, sys; from collective_toy_engine_001 import run_model; print(json.dumps(run_model(json.load(sys.stdin)), sort_keys=True, ensure_ascii=False))";
  const result = spawnSync("python", ["-c", script], {
    cwd: engineDir, input: JSON.stringify(model), encoding: "utf8"
  });
  assert.equal(result.status, 0, "Python engine failed: " + result.stderr);
  return JSON.parse(result.stdout.trim());
}

function compareCodePoints(a, b) {
  const aa = Array.from(a, ch => ch.codePointAt(0));
  const bb = Array.from(b, ch => ch.codePointAt(0));
  for (let i = 0; i < Math.min(aa.length, bb.length); i++) {
    if (aa[i] !== bb[i]) return aa[i] - bb[i];
  }
  return aa.length - bb.length;
}
function canonicalJson(value) {
  if (Array.isArray(value)) return "[" + value.map(canonicalJson).join(",") + "]";
  if (value !== null && typeof value === "object") {
    return "{" + Object.keys(value).sort(compareCodePoints).map(
      key => JSON.stringify(key) + ":" + canonicalJson(value[key])
    ).join(",") + "}";
  }
  return JSON.stringify(value);
}

function sha256Canonical(value) {
  return crypto.createHash("sha256").update(canonicalJson(value), "utf8").digest("hex");
}

function assertExportedPackageHashFailures(exportedPackage, label) {
  const alteredInput = structuredClone(exportedPackage);
  alteredInput.input.transitions[0].target = "__tampered_target__";
  assert.notEqual(sha256Canonical(alteredInput.input), alteredInput.result.input_sha256,
    label + ": input tampering did not invalidate input hash");
  const alteredInputPayload = structuredClone(alteredInput);
  delete alteredInputPayload.package_sha256;
  assert.notEqual(sha256Canonical(alteredInputPayload), alteredInput.package_sha256,
    label + ": input tampering did not invalidate package hash");

  const alteredResult = structuredClone(exportedPackage);
  alteredResult.result.scenario_results = {};
  const alteredResultPayload = structuredClone(alteredResult.result);
  delete alteredResultPayload.input_sha256;
  delete alteredResultPayload.result_sha256;
  assert.notEqual(sha256Canonical(alteredResultPayload), alteredResult.result.result_sha256,
    label + ": result tampering did not invalidate result hash");

  const alteredMetadata = structuredClone(exportedPackage);
  alteredMetadata.package_version = "tampered-version";
  const alteredMetadataPayload = structuredClone(alteredMetadata);
  delete alteredMetadataPayload.package_sha256;
  assert.notEqual(sha256Canonical(alteredMetadataPayload), alteredMetadata.package_sha256,
    label + ": package metadata tampering did not invalidate package hash");
}

function assertUnsupportedExportVersionsRejected(engineDir, exportedPackage, label) {
  const unsupportedPackage = structuredClone(exportedPackage);
  unsupportedPackage.package_version = "collective-toy-run-package-999";
  const unsupportedPayload = structuredClone(unsupportedPackage);
  delete unsupportedPayload.package_sha256;
  unsupportedPackage.package_sha256 = sha256Canonical(unsupportedPayload);
  assert.throws(() => verifyExportedPackage(engineDir, unsupportedPackage, label + " unsupported package version"),
    label + ": unsupported package version accepted with a recomputed valid package hash");

  const unsupportedEngine = structuredClone(exportedPackage);
  if (exportedPackage.package_version === "collective-toy-run-package-001") {
    unsupportedEngine.engine_version = "collective-toy-engine-999";
  } else {
    // Browser schema declares engine_version inside result, unlike the Python package.
    unsupportedEngine.result.engine_version = "collective-toy-engine-999";
    const resultPayload = structuredClone(unsupportedEngine.result);
    delete resultPayload.input_sha256;
    delete resultPayload.result_sha256;
    unsupportedEngine.result.result_sha256 = sha256Canonical(resultPayload);
  }
  const unsupportedEnginePayload = structuredClone(unsupportedEngine);
  delete unsupportedEnginePayload.package_sha256;
  unsupportedEngine.package_sha256 = sha256Canonical(unsupportedEnginePayload);
  assert.deepEqual(
    assessExportedPackage(engineDir, unsupportedEngine, label + " unknown engine"),
    {
      status: "inspect-only/replay-unavailable",
      integrity_verified: true,
      replay_verified: false,
      reason: "Unsupported exported package engine version"
    },
    label + ": intact package with unknown engine must be inspect-only"
  );
  assert.throws(() => verifyExportedPackage(engineDir, unsupportedEngine, label + " unsupported engine version"),
    label + ": unsupported engine version accepted for replay despite recomputed valid hashes");
}

function assertTruncatedPackagesRejected(engineDir, exportedPackage, label) {
  const requiredFields = ["package_version", "input", "result", "package_sha256"];
  if (exportedPackage.package_version === "collective-toy-run-package-001") {
    requiredFields.push("engine_version");
  }
  for (const field of requiredFields) {
    const incomplete = structuredClone(exportedPackage);
    delete incomplete[field];
    assert.throws(() => verifyExportedPackage(engineDir, incomplete, label + " missing " + field),
      label + ": incomplete package accepted when missing " + field);
  }
  const incompleteResult = structuredClone(exportedPackage);
  delete incompleteResult.result.result_sha256;
  const incompleteResultPayload = structuredClone(incompleteResult);
  delete incompleteResultPayload.package_sha256;
  incompleteResult.package_sha256 = sha256Canonical(incompleteResultPayload);
  assert.throws(() => verifyExportedPackage(engineDir, incompleteResult, label + " missing result hash"),
    label + ": incomplete result accepted without result_sha256");

  const incompleteInput = structuredClone(exportedPackage);
  delete incompleteInput.input.transitions;
  const incompleteInputPayload = structuredClone(incompleteInput);
  delete incompleteInputPayload.package_sha256;
  incompleteInput.package_sha256 = sha256Canonical(incompleteInputPayload);
  assert.throws(() => verifyExportedPackage(engineDir, incompleteInput, label + " missing input field"),
    label + ": incomplete input accepted without transitions");
}

function verifyExportedPackageIntegrity(exportedPackage, label) {
  assert.ok(exportedPackage && typeof exportedPackage === "object" && !Array.isArray(exportedPackage),
    label + ": exported package must be an object");
  const packageVersion = exportedPackage.package_version;
  assert.ok(
    ["collective-toy-run-package-001", "collective-toy-browser-run-001"].includes(packageVersion),
    label + ": unsupported package version"
  );
  const requiredFields = ["package_version", "input", "result", "package_sha256"];
  if (packageVersion === "collective-toy-run-package-001") requiredFields.push("engine_version");
  for (const field of requiredFields) {
    if (!Object.prototype.hasOwnProperty.call(exportedPackage, field)) {
      throw new Error(label + ": exported package is missing required field " + field);
    }
  }
  assert.ok(exportedPackage.input && typeof exportedPackage.input === "object" && !Array.isArray(exportedPackage.input),
    label + ": exported input must be an object");
  assert.ok(exportedPackage.result && typeof exportedPackage.result === "object" && !Array.isArray(exportedPackage.result),
    label + ": exported result must be an object");
  for (const field of ["input_sha256", "result_sha256"]) {
    assert.ok(Object.prototype.hasOwnProperty.call(exportedPackage.result, field),
      label + ": exported result is missing required field " + field);
  }
  const engineVersion = packageVersion === "collective-toy-run-package-001"
    ? exportedPackage.engine_version : exportedPackage.result.engine_version;
  assert.ok(typeof engineVersion === "string" && engineVersion.length > 0,
    label + ": engine version must be declared");
  const packagePayload = structuredClone(exportedPackage);
  delete packagePayload.package_sha256;
  assert.equal(sha256Canonical(packagePayload), exportedPackage.package_sha256,
    label + ": exported package SHA-256 does not verify");
  assert.equal(sha256Canonical(exportedPackage.input), exportedPackage.result.input_sha256,
    label + ": input SHA-256 does not verify");
  const resultPayload = structuredClone(exportedPackage.result);
  delete resultPayload.input_sha256;
  delete resultPayload.result_sha256;
  assert.equal(sha256Canonical(resultPayload), exportedPackage.result.result_sha256,
    label + ": result SHA-256 does not verify");
  return { packageVersion, engineVersion };
}

function assessExportedPackage(engineDir, exportedPackage, label) {
  const integrity = verifyExportedPackageIntegrity(exportedPackage, label);
  if (integrity.engineVersion !== "collective-toy-engine-001") {
    return {
      status: "inspect-only/replay-unavailable",
      integrity_verified: true,
      replay_verified: false,
      reason: "Unsupported exported package engine version"
    };
  }
  const replayed = runPython(engineDir, exportedPackage.input);
  assert.deepEqual(replayed, exportedPackage.result,
    label + ": independently replayed Python result differs from exported result");
  return {
    status: "replay-verified",
    integrity_verified: true,
    replay_verified: true,
    reason: null
  };
}

function recomputePackageHashes(exportedPackage) {
  const resultPayload = structuredClone(exportedPackage.result);
  delete resultPayload.input_sha256;
  delete resultPayload.result_sha256;
  exportedPackage.result.result_sha256 = sha256Canonical(resultPayload);
  const packagePayload = structuredClone(exportedPackage);
  delete packagePayload.package_sha256;
  exportedPackage.package_sha256 = sha256Canonical(packagePayload);
  return exportedPackage;
}

function assertEngineVersionDeclarationsRejected(exportedPackage, label) {
  const isPythonSchema = exportedPackage.package_version === "collective-toy-run-package-001";
  for (const invalidVersion of [undefined, null, "", 17]) {
    const malformed = structuredClone(exportedPackage);
    if (isPythonSchema) {
      if (invalidVersion === undefined) delete malformed.engine_version;
      else malformed.engine_version = invalidVersion;
    } else {
      if (invalidVersion === undefined) delete malformed.result.engine_version;
      else malformed.result.engine_version = invalidVersion;
    }
    recomputePackageHashes(malformed);
    assert.throws(
      () => verifyExportedPackageIntegrity(malformed, label + " malformed engine version"),
      label + ": malformed or missing engine version was accepted"
    );
  }
}

function assertReplayDivergenceRejected(engineDir, exportedPackage, label) {
  const divergent = structuredClone(exportedPackage);
  // Keep every hash internally valid so rejection exercises replay comparison.
  const baseline = divergent.result.scenario_results && divergent.result.scenario_results.baseline;
  assert.ok(baseline && Array.isArray(baseline.reachable_states),
    label + ": fixture lacks baseline reachable_states for divergence test");
  baseline.reachable_states.push("FORGED_STATE_NOT_IN_MODEL");
  recomputePackageHashes(divergent);
  assert.equal(
    verifyExportedPackageIntegrity(divergent, label + " divergent result").engineVersion,
    "collective-toy-engine-001",
    label + ": divergent fixture must retain valid integrity and supported engine"
  );
  assert.throws(
    () => assessExportedPackage(engineDir, divergent, label + " divergent result"),
    /independently replayed Python result differs from exported result/,
    label + ": validly hashed but divergent result was accepted as replay-verified"
  );
}

function verifyExportedPackage(engineDir, exportedPackage, label) {
  const assessment = assessExportedPackage(engineDir, exportedPackage, label);
  if (assessment.status !== "replay-verified") {
    throw new Error(label + ": " + assessment.reason);
  }
  assertExportedPackageHashFailures(exportedPackage, label);
  assertTruncatedPackagesRejected(engineDir, exportedPackage, label);
  assertUnsupportedExportVersionsRejected(engineDir, exportedPackage, label);
  assertEngineVersionDeclarationsRejected(exportedPackage, label);
  assertReplayDivergenceRejected(engineDir, exportedPackage, label);
  return true;
}
(async () => {
  const root = path.resolve(__dirname, "../../..");
  const htmlPath = path.join(root, "prototypes/collective_toy/web/index.html");
  const engineDir = path.join(root, "prototypes/collective_toy");
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ acceptDownloads: true });
  const outputPath = path.join(os.tmpdir(), "collective-toy-browser-" + process.pid + ".json");
  function reverseObjectKeyOrder(value) {
    if (Array.isArray(value)) return value.map(reverseObjectKeyOrder);
    if (value !== null && typeof value === "object") {
      return Object.fromEntries(Object.keys(value).reverse()
        .map(key => [key, reverseObjectKeyOrder(value[key])]));
    }
    return value;
  }
  const keyOrderFixture = fixtures()[0].model;
  const keyOrderPermuted = reverseObjectKeyOrder(keyOrderFixture);
  assert.equal(canonicalJson(keyOrderFixture), canonicalJson(keyOrderPermuted),
    "reordering JSON object keys changed canonical representation");
  const keyOrderOriginalResult = runPython(engineDir, keyOrderFixture);
  const keyOrderPermutedResult = runPython(engineDir, keyOrderPermuted);
  assert.equal(keyOrderOriginalResult.input_sha256, keyOrderPermutedResult.input_sha256,
    "reordering JSON object keys changed input SHA-256");
  assert.equal(keyOrderOriginalResult.result_sha256, keyOrderPermutedResult.result_sha256,
    "reordering JSON object keys changed result SHA-256");
  assert.deepEqual(keyOrderOriginalResult.scenario_results, keyOrderPermutedResult.scenario_results,
    "reordering JSON object keys changed scenario semantics");
  assert.deepEqual(keyOrderOriginalResult.comparisons_to_baseline, keyOrderPermutedResult.comparisons_to_baseline,
    "reordering JSON object keys changed baseline comparisons");

  const report = [];

  try {
    await page.goto("file://" + htmlPath);

    // Terminology acceptance: user-facing language must describe toy-local outputs,
    // not present them as system-level TGCV T_acc or as scientific validation.
    const notice = await page.locator(".notice").innerText();
    assert.match(notice, /grafo finito en el navegador/i,
      "UI must identify the implementation as a finite-graph demonstrator");
    assert.match(notice, /No procesa datos reales ni implementa por sí solo T[_]?acc de TGCV/i,
      "UI must explicitly preserve the boundary with system-level T_acc");
    assert.match(notice, /No es una validación científica/i,
      "UI must not imply scientific validation");
    assert.match(await page.locator("#metrics").innerText(), /Estados alcanzables/);
    assert.match(await page.locator("#metrics").innerText(), /Trayectorias enumeradas/);
    assert.match(await page.locator("#metrics").innerText(), /Exploración completa/);

    // UI acceptance: edit, execute, and remove a guarded relation; confirm profile 1 stays inert.
    await page.locator("#profile-editor").selectOption("2");
    await page.locator("#guarded-transition").selectOption("t_bd");
    await page.locator("#required-transition").selectOption("t_ac");
    await page.getByRole("button", { name: "Añadir relación" }).click();
    let editorModel = await page.locator("#model").inputValue();
    let editorParsed = JSON.parse(editorModel);
    assert.deepEqual(editorParsed.rule_profile, { type: "relation_guarded_graph", version: "1" });
    assert.equal(editorParsed.relations.length, 1, "visual editor should add exactly one relation");
    assert.deepEqual(
      { transition_id: editorParsed.relations[0].transition_id, requires_transition_id: editorParsed.relations[0].requires_transition_id },
      { transition_id: "t_bd", requires_transition_id: "t_ac" }
    );

    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.getByText(/Ejecución completada/).waitFor({ timeout: 5000 });
    let [guardedDownload] = await Promise.all([
      page.waitForEvent("download"),
      page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click()
    ]);
    await guardedDownload.saveAs(outputPath);
    let editorPackage = JSON.parse(fs.readFileSync(outputPath, "utf8"));
    fs.unlinkSync(outputPath);
    verifyExportedPackage(engineDir, editorPackage, "visual relation-editor profile 2 export");
    const guardedScenario = editorPackage.result.scenario_results.block_ac;
    assert.ok(guardedScenario.effective_disabled_transitions.includes("t_bd"),
      "profile 2 should block the guarded transition when its required transition is disabled");
    assert.equal(guardedScenario.relation_effects[0].status, "BLOCKED");
    const guardedPackageForImport = structuredClone(editorPackage);
    await page.locator("#which").selectOption("block_ac");
    assert.equal(
      await page.locator('#graph path[data-transition-id="t_bd"]').getAttribute("stroke-opacity"),
      "0.22",
      "graph should visually dim a relation-blocked transition in profile 2"
    );

    await page.locator("#profile-editor").selectOption("1");
    editorParsed = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(editorParsed.rule_profile, { type: "finite_deterministic_graph", version: "1" });
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.getByText(/Ejecución completada/).waitFor({ timeout: 5000 });
    let [profileOneDownload] = await Promise.all([
      page.waitForEvent("download"),
      page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click()
    ]);
    await profileOneDownload.saveAs(outputPath);
    editorPackage = JSON.parse(fs.readFileSync(outputPath, "utf8"));
    fs.unlinkSync(outputPath);
    verifyExportedPackage(engineDir, editorPackage, "visual relation-editor profile 1 export");
    const profileOneScenario = editorPackage.result.scenario_results.block_ac;
    assert.equal(profileOneScenario.effective_disabled_transitions, undefined,
      "profile 1 must not apply relation guards");
    assert.deepEqual(profileOneScenario.disabled_transitions, ["t_ac"],
      "profile 1 should preserve only the explicit scenario intervention");
    assert.equal(
      await page.locator('#graph path[data-transition-id="t_bd"]').getAttribute("stroke-opacity"),
      "0.72",
      "graph should not dim a transition because of inert metadata in profile 1"
    );

    await page.locator("#profile-editor").selectOption("2");
    await page.locator('[data-remove-relation="r_guard_1"]').click();
    editorParsed = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(editorParsed.relations.length, 0, "visual editor should remove selected relation");
    // Browser import lifecycle: native replay, inspect-only, malformed schema, hash failure, and semantic divergence.
    async function assessInBrowser(testPackage, expectedState, expectedMessage) {
      fs.writeFileSync(outputPath, JSON.stringify(testPackage, null, 2));
      await page.locator("#package-file").setInputFiles(outputPath);
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      const assessment = page.locator("#package-assessment");
      await page.waitForFunction(() => {
        const node = document.querySelector("#package-assessment");
        return !!node && !["idle", "validating"].includes(node.dataset.state);
      }, null, { timeout: 5000 });
      const actualMessage = await assessment.innerText();
      assert.ok(actualMessage.includes(expectedMessage),
        "unexpected browser import assessment; expected [" + expectedMessage + "], got [" + actualMessage + "]");
      assert.equal(await assessment.getAttribute("data-state"), expectedState,
        "unexpected browser import lifecycle state for " + expectedMessage + "; got [" + actualMessage + "]");
      return actualMessage;
    }
    const validImportedPackage = structuredClone(editorPackage);
    assert.match(await assessInBrowser(validImportedPackage, "replay-verified", "replay-verified"),
      /reproducción independiente coincidente/i);

    const inspectOnlyPackage = structuredClone(validImportedPackage);
    inspectOnlyPackage.result.engine_version = "collective-toy-engine-999";
    const inspectResultPayload = structuredClone(inspectOnlyPackage.result);
    delete inspectResultPayload.input_sha256;
    delete inspectResultPayload.result_sha256;
    inspectOnlyPackage.result.result_sha256 = sha256Canonical(inspectResultPayload);
    const inspectPackagePayload = structuredClone(inspectOnlyPackage);
    delete inspectPackagePayload.package_sha256;
    inspectOnlyPackage.package_sha256 = sha256Canonical(inspectPackagePayload);
    const inspectOnlyMessage = await assessInBrowser(inspectOnlyPackage, "inspect-only/replay-unavailable", "inspect-only/replay-unavailable");
    assert.match(inspectOnlyMessage, /Consistencia interna de hashes verificada/i);
    assert.match(inspectOnlyMessage, /no autentica el origen/i);
    assert.match(inspectOnlyMessage, /no se ha intentado reproducir/i);

    for (const inconsistent of [
      { label: "schema", mutate: pkg => { pkg.result.schema_version = "collective-toy-input-999"; }, message: "La versión de esquema del resultado no coincide con la entrada" },
      { label: "model", mutate: pkg => { pkg.result.model_id = "different-model"; }, message: "El model_id del resultado no coincide con la entrada" },
      { label: "profile", mutate: pkg => { pkg.result.rule_profile = { type: "unknown_profile", version: "1" }; }, message: "El perfil de reglas del resultado no coincide con la entrada" },
      { label: "validation", mutate: pkg => { pkg.result.validation = "UNKNOWN"; }, message: "El resultado no declara validation=PASS" }
    ]) {
      const inconsistentPackage = structuredClone(validImportedPackage);
      // Unsupported engine ensures consistency is checked before inspect-only fallback.
      inconsistentPackage.result.engine_version = "collective-toy-engine-999";
      inconsistent.mutate(inconsistentPackage);
      const resultBody = structuredClone(inconsistentPackage.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      inconsistentPackage.result.result_sha256 = sha256Canonical(resultBody);
      const packageBody = structuredClone(inconsistentPackage);
      delete packageBody.package_sha256;
      inconsistentPackage.package_sha256 = sha256Canonical(packageBody);
      await assessInBrowser(inconsistentPackage, "rejected", inconsistent.message);
    }

    const unsupportedEngineInvalidInput = structuredClone(validImportedPackage);
    unsupportedEngineInvalidInput.result.engine_version = "collective-toy-engine-999";
    delete unsupportedEngineInvalidInput.input.initial_state;
    unsupportedEngineInvalidInput.result.input_sha256 = sha256Canonical(unsupportedEngineInvalidInput.input);
    const unsupportedInvalidResultBody = structuredClone(unsupportedEngineInvalidInput.result);
    delete unsupportedInvalidResultBody.input_sha256;
    delete unsupportedInvalidResultBody.result_sha256;
    unsupportedEngineInvalidInput.result.result_sha256 = sha256Canonical(unsupportedInvalidResultBody);
    const unsupportedInvalidPackageBody = structuredClone(unsupportedEngineInvalidInput);
    delete unsupportedInvalidPackageBody.package_sha256;
    unsupportedEngineInvalidInput.package_sha256 = sha256Canonical(unsupportedInvalidPackageBody);
    await assessInBrowser(unsupportedEngineInvalidInput, "rejected", "initial_state debe ser un ID de estado");

    const unknownNestedResultField = structuredClone(validImportedPackage);
    unknownNestedResultField.result.engine_version = "collective-toy-engine-999";
    const nestedScenarioId = Object.keys(unknownNestedResultField.result.scenario_results)[0];
    unknownNestedResultField.result.scenario_results[nestedScenarioId].unrecognized_extension = "not in scenario result schema";
    const nestedResultBody = structuredClone(unknownNestedResultField.result);
    delete nestedResultBody.input_sha256;
    delete nestedResultBody.result_sha256;
    unknownNestedResultField.result.result_sha256 = sha256Canonical(nestedResultBody);
    const nestedPackageBody = structuredClone(unknownNestedResultField);
    delete nestedPackageBody.package_sha256;
    unknownNestedResultField.package_sha256 = sha256Canonical(nestedPackageBody);
    await assessInBrowser(unknownNestedResultField, "rejected", "contiene campos desconocidos");

    for (const malformedNested of [
      { label: "trajectory-step", mutate: pkg => {
          pkg.result.scenario_results[Object.keys(pkg.result.scenario_results)[0]].trajectories[0][0] = { state: 17, unknown: true };
        }, message: "trajectories del escenario" },
      { label: "negative-bound", mutate: pkg => {
          pkg.result.scenario_results[Object.keys(pkg.result.scenario_results)[0]].exploration_bounds.max_depth = -1;
        }, message: "límites enteros no negativos" }
    ]) {
      const malformedNestedPackage = structuredClone(validImportedPackage);
      malformedNestedPackage.result.engine_version = "collective-toy-engine-999";
      malformedNested.mutate(malformedNestedPackage);
      const nestedResultPayload = structuredClone(malformedNestedPackage.result);
      delete nestedResultPayload.input_sha256;
      delete nestedResultPayload.result_sha256;
      malformedNestedPackage.result.result_sha256 = sha256Canonical(nestedResultPayload);
      const nestedPackagePayload = structuredClone(malformedNestedPackage);
      delete nestedPackagePayload.package_sha256;
      malformedNestedPackage.package_sha256 = sha256Canonical(nestedPackagePayload);
      await assessInBrowser(malformedNestedPackage, "rejected", malformedNested.message);
    }

    for (const malformedRelationResult of [
      { label: "relation-effect-status", mutate: pkg => {
          const sid = Object.keys(pkg.result.scenario_results).find(id =>
            Array.isArray(pkg.result.scenario_results[id].relation_effects) &&
            pkg.result.scenario_results[id].relation_effects.length > 0);
          assert.ok(sid, "guarded fixture must contain relation effects");
          const effect = pkg.result.scenario_results[sid].relation_effects[0];
          effect.status = effect.status === "BLOCKED" ? "APPLIED" : "BLOCKED";
        }, message: "relation_effects no coincide con los efectos" },
      { label: "effective-disabled-transitions", mutate: pkg => {
          const sid = Object.keys(pkg.result.scenario_results).find(id =>
            Array.isArray(pkg.result.scenario_results[id].effective_disabled_transitions) &&
            pkg.result.scenario_results[id].effective_disabled_transitions.length > 0);
          assert.ok(sid, "guarded fixture must contain effective disabled transitions");
          pkg.result.scenario_results[sid].effective_disabled_transitions = [];
        }, message: "effective_disabled_transitions no coincide" },
      { label: "relation-effect-reason", mutate: pkg => {
          const sid = Object.keys(pkg.result.scenario_results).find(id =>
            Array.isArray(pkg.result.scenario_results[id].relation_effects) &&
            pkg.result.scenario_results[id].relation_effects.length > 0);
          assert.ok(sid, "guarded fixture must contain relation effects");
          const effect = pkg.result.scenario_results[sid].relation_effects[0];
          effect.reason = effect.reason === "prerequisite_transition_disabled"
            ? "prerequisite_transition_not_disabled"
            : "prerequisite_transition_disabled";
        }, message: "relation_effects no coincide con los efectos" }
    ]) {
      const malformedRelationPackage = structuredClone(guardedPackageForImport);
      malformedRelationPackage.result.engine_version = "collective-toy-engine-999";
      malformedRelationResult.mutate(malformedRelationPackage);
      const relationResultPayload = structuredClone(malformedRelationPackage.result);
      delete relationResultPayload.input_sha256;
      delete relationResultPayload.result_sha256;
      malformedRelationPackage.result.result_sha256 = sha256Canonical(relationResultPayload);
      const relationPackagePayload = structuredClone(malformedRelationPackage);
      delete relationPackagePayload.package_sha256;
      malformedRelationPackage.package_sha256 = sha256Canonical(relationPackagePayload);
      await assessInBrowser(malformedRelationPackage, "rejected", malformedRelationResult.message);
    }

    for (const malformedReference of [
      { label: "unknown-trajectory-state", mutate: pkg => {
          const sid = Object.keys(pkg.result.scenario_results)[0];
          pkg.result.scenario_results[sid].trajectories[0][0].state = "state-not-in-input";
        }, message: "rutas válidas y transiciones coherentes con la entrada" },
      { label: "unknown-comparison-state", mutate: pkg => {
          const sid = Object.keys(pkg.result.comparisons_to_baseline)[0];
          pkg.result.comparisons_to_baseline[sid].reachable_states_added = ["state-not-in-input"];
        }, message: "IDs de estado declarados" },
      { label: "trajectory-edge-mismatch", mutate: pkg => {
          const sid = Object.keys(pkg.result.scenario_results)[0];
          const paths = pkg.result.scenario_results[sid].trajectories;
          const path = paths.find(candidate => candidate.length > 1);
          assert.ok(path, "fixture must include a trajectory with an edge");
          const previous = path[0].state;
          const current = path[1].state;
          const incompatible = pkg.input.transitions.find(edge =>
            edge.id !== path[1].transition && !(edge.source === previous && edge.target === current));
          assert.ok(incompatible, "fixture must include an incompatible declared edge");
          path[1].transition = incompatible.id;
        }, message: "rutas válidas y transiciones coherentes con la entrada" }
    ]) {
      const malformedReferencePackage = structuredClone(validImportedPackage);
      malformedReferencePackage.result.engine_version = "collective-toy-engine-999";
      malformedReference.mutate(malformedReferencePackage);
      const referenceResultPayload = structuredClone(malformedReferencePackage.result);
      delete referenceResultPayload.input_sha256;
      delete referenceResultPayload.result_sha256;
      malformedReferencePackage.result.result_sha256 = sha256Canonical(referenceResultPayload);
      const referencePackagePayload = structuredClone(malformedReferencePackage);
      delete referencePackagePayload.package_sha256;
      malformedReferencePackage.package_sha256 = sha256Canonical(referencePackagePayload);
      await assessInBrowser(malformedReferencePackage, "rejected", malformedReference.message);
    }

    const malformedSchemaPackage = structuredClone(validImportedPackage);
    malformedSchemaPackage.package_version = "collective-toy-browser-run-999";
    const malformedSchemaPayload = structuredClone(malformedSchemaPackage);
    delete malformedSchemaPayload.package_sha256;
    malformedSchemaPackage.package_sha256 = sha256Canonical(malformedSchemaPayload);
    await assessInBrowser(malformedSchemaPackage, "rejected", "Esquema de paquete desconocido");

    for (const malformedVersion of [
      { label: "missing", mutate: pkg => { delete pkg.result.engine_version; } },
      { label: "null", mutate: pkg => { pkg.result.engine_version = null; } },
      { label: "blank", mutate: pkg => { pkg.result.engine_version = "   "; } },
      { label: "wrong-type", mutate: pkg => { pkg.result.engine_version = 7; } }
    ]) {
      const malformedVersionPackage = structuredClone(validImportedPackage);
      malformedVersion.mutate(malformedVersionPackage);
      const malformedVersionResult = structuredClone(malformedVersionPackage.result);
      delete malformedVersionResult.input_sha256;
      delete malformedVersionResult.result_sha256;
      malformedVersionPackage.result.result_sha256 = sha256Canonical(malformedVersionResult);
      const malformedVersionPayload = structuredClone(malformedVersionPackage);
      delete malformedVersionPayload.package_sha256;
      malformedVersionPackage.package_sha256 = sha256Canonical(malformedVersionPayload);
      await assessInBrowser(malformedVersionPackage, "rejected", "Declaración de versión del motor ausente o malformada");
    }

    const pythonSchemaPackage = structuredClone(validImportedPackage);
    pythonSchemaPackage.package_version = "collective-toy-run-package-001";
    const pythonSchemaPayload = structuredClone(pythonSchemaPackage);
    delete pythonSchemaPayload.package_sha256;
    pythonSchemaPackage.package_sha256 = sha256Canonical(pythonSchemaPayload);
    await assessInBrowser(pythonSchemaPackage, "rejected", "Esquema de paquete desconocido");

    const invalidInputHashPackage = structuredClone(validImportedPackage);
    invalidInputHashPackage.result.input_sha256 = "0".repeat(64);
    const invalidInputHashResult = structuredClone(invalidInputHashPackage.result);
    delete invalidInputHashResult.input_sha256;
    delete invalidInputHashResult.result_sha256;
    invalidInputHashPackage.result.result_sha256 = sha256Canonical(invalidInputHashResult);
    const invalidInputHashPayload = structuredClone(invalidInputHashPackage);
    delete invalidInputHashPayload.package_sha256;
    invalidInputHashPackage.package_sha256 = sha256Canonical(invalidInputHashPayload);
    await assessInBrowser(invalidInputHashPackage, "rejected", "El hash de la entrada no coincide");

    const invalidResultHashPackage = structuredClone(validImportedPackage);
    invalidResultHashPackage.result.result_sha256 = "0".repeat(64);
    const invalidResultHashPayload = structuredClone(invalidResultHashPackage);
    delete invalidResultHashPayload.package_sha256;
    invalidResultHashPackage.package_sha256 = sha256Canonical(invalidResultHashPayload);
    await assessInBrowser(invalidResultHashPackage, "rejected", "El hash del resultado no coincide");

    const unknownPackageField = structuredClone(validImportedPackage);
    unknownPackageField.unrecognized_extension = { meaning: "not part of the browser package schema" };
    const unknownPackagePayload = structuredClone(unknownPackageField);
    delete unknownPackagePayload.package_sha256;
    unknownPackageField.package_sha256 = sha256Canonical(unknownPackagePayload);
    await assessInBrowser(unknownPackageField, "rejected", "El paquete contiene campos desconocidos");

    const unknownResultField = structuredClone(validImportedPackage);
    unknownResultField.result.unrecognized_extension = "not in the result schema";
    const unknownResultBody = structuredClone(unknownResultField.result);
    delete unknownResultBody.input_sha256;
    delete unknownResultBody.result_sha256;
    unknownResultField.result.result_sha256 = sha256Canonical(unknownResultBody);
    const unknownResultPayload = structuredClone(unknownResultField);
    delete unknownResultPayload.package_sha256;
    unknownResultField.package_sha256 = sha256Canonical(unknownResultPayload);
    await assessInBrowser(unknownResultField, "rejected", "El resultado contiene campos desconocidos");

    const invalidHashPackage = structuredClone(validImportedPackage);
    invalidHashPackage.package_sha256 = "0".repeat(64);
    await assessInBrowser(invalidHashPackage, "rejected", "El hash del paquete no coincide");

    const divergentPackage = structuredClone(validImportedPackage);
    divergentPackage.result.scenario_results.baseline.reachable_states.push("FORGED_STATE_NOT_IN_MODEL");
    const divergentResultPayload = structuredClone(divergentPackage.result);
    delete divergentResultPayload.input_sha256;
    delete divergentResultPayload.result_sha256;
    divergentPackage.result.result_sha256 = sha256Canonical(divergentResultPayload);
    const divergentPackagePayload = structuredClone(divergentPackage);
    delete divergentPackagePayload.package_sha256;
    divergentPackage.package_sha256 = sha256Canonical(divergentPackagePayload);
    await assessInBrowser(divergentPackage, "rejected", "La reproducción independiente difiere");

    fs.writeFileSync(outputPath, "{ invalid JSON");
    await page.locator("#package-file").setInputFiles(outputPath);
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    const malformedJsonAssessment = page.locator("#package-assessment");
    await malformedJsonAssessment.getByText("El archivo no contiene JSON válido", { exact: false }).waitFor({ timeout: 5000 });
    assert.equal(await malformedJsonAssessment.getAttribute("data-state"), "rejected");

    fs.writeFileSync(outputPath, Buffer.alloc(5 * 1024 * 1024 + 1, 32));
    await page.locator("#package-file").setInputFiles(outputPath);
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    const oversizedAssessment = page.locator("#package-assessment");
    await oversizedAssessment.getByText("supera el límite de 5 MiB", { exact: false }).waitFor({ timeout: 5000 });
    assert.equal(await oversizedAssessment.getAttribute("data-state"), "rejected");

    // State must not remain verified after a failed assessment or a new file selection.
    await assessInBrowser(validImportedPackage, "replay-verified", "replay-verified");
    fs.writeFileSync(outputPath, "{ invalid JSON");
    await page.locator("#package-file").setInputFiles(outputPath);
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment").getByText("El archivo no contiene JSON válido", { exact: false }).waitFor({ timeout: 5000 });
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "rejected");
    const retryPath = outputPath + ".valid-retry.json";
    fs.writeFileSync(retryPath, JSON.stringify(validImportedPackage, null, 2));
    await page.locator("#package-file").setInputFiles(retryPath);
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "idle",
      "selecting a new package must clear any previous verification/rejection state");
    assert.match(await page.locator("#package-assessment").innerText(), /Archivo seleccionado/i);
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment").getByText("replay-verified", { exact: false }).waitFor({ timeout: 5000 });
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "replay-verified");

    fs.unlinkSync(outputPath);
    fs.unlinkSync(retryPath);
    console.log("PASS: browser import lifecycle verifies replay, inspect-only, schema/version/hash rejection, divergence, malformed/oversized imports, and stale-state clearing.");


    const validFixtures = [...fixtures(), ...generatedFixtures()];
    const semanticResults = new Map();
    for (const fixture of validFixtures) {
      const fixtureJson = JSON.stringify(fixture.model, null, 2);
      if ((fixture.model.transitions || []).length > 2000 || (fixture.model.states || []).length > 500) {
        // Set oversized fixtures without firing the editor's per-keystroke input handler.
        // Then exercise the same visible Run action and production validation path.
        await page.locator("#model").evaluate((el, value) => { el.value = value; }, fixtureJson);
      } else {
        await page.locator("#model").fill(fixtureJson, { timeout: 15000 });
      }
      await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
      await page.getByText(/Ejecución completada/).waitFor({ timeout: 5000 });

      const [download] = await Promise.all([
        page.waitForEvent("download"),
        page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click()
      ]);
      await download.saveAs(outputPath);
      const browserPackage = JSON.parse(fs.readFileSync(outputPath, "utf8"));
      fs.unlinkSync(outputPath);
      verifyExportedPackage(engineDir, browserPackage, fixture.name + " exported package");

      const pyResult = runPython(engineDir, fixture.model);
      assert.deepEqual(browserPackage.result.scenario_results, pyResult.scenario_results,
        fixture.name + ": scenario results differ");
      assert.deepEqual(browserPackage.result.comparisons_to_baseline, pyResult.comparisons_to_baseline,
        fixture.name + ": baseline comparisons differ");
      assert.equal(browserPackage.result.input_sha256, pyResult.input_sha256,
        fixture.name + ": input SHA-256 differs");
      assert.equal(browserPackage.result.result_sha256, pyResult.result_sha256,
        fixture.name + ": result SHA-256 differs");
      if (fixture.interventionPermutationOf) {
        const original = semanticResults.get(fixture.interventionPermutationOf);
        assert.ok(original, fixture.name + ": original intervention order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          fixture.name + ": reordering disabled transitions changed scenario semantics");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          fixture.name + ": reordering disabled transitions changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          fixture.name + ": reordering disabled transitions changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          fixture.name + ": reordering serialized disabled transitions should change input SHA-256");
      }
      if (fixture.name === "intervention-composition-order") {
        const scenarios = browserPackage.result.scenario_results;
        const ab = new Set(scenarios.disable_ab.effective_disabled_transitions);
        const ac = new Set(scenarios.disable_ac.effective_disabled_transitions);
        const both = new Set(scenarios.disable_both.effective_disabled_transitions);
        const reversed = new Set(scenarios.disable_both_reversed.effective_disabled_transitions);
        assert.deepEqual([...both].sort(), [...new Set([...ab, ...ac])].sort(),
          "combined intervention must equal the union of single-intervention effects");
        assert.deepEqual([...both].sort(), [...reversed].sort(),
          "reversing disabled-transition declaration order changed effective effects");
        const semanticView = value => Object.fromEntries(Object.entries(value)
          .filter(([key]) => key !== "scenario_id" && key !== "disabled_transitions"));
        assert.deepEqual(semanticView(scenarios.disable_both), semanticView(scenarios.disable_both_reversed),
          "reversing disabled-transition declaration order changed semantic scenario result");
      }
      if (fixture.name === "relation-guard-intervention-monotonicity") {
        const baseline = browserPackage.result.scenario_results.baseline;
        const intervention = browserPackage.result.scenario_results.disable_ab;
        assert.ok(
          intervention.reachable_states.every(state => baseline.reachable_states.includes(state)),
          "relation-guarded intervention expanded reachable states"
        );
        const encode = value => JSON.stringify(value);
        const baselinePaths = new Set(baseline.trajectories.map(encode));
        assert.ok(
          intervention.trajectories.every(path => baselinePaths.has(encode(path))),
          "relation-guarded intervention introduced a trajectory absent from baseline"
        );
      }
      if (fixture.name === "intervention-reachability-monotonicity") {
        const baseline = browserPackage.result.scenario_results.baseline;
        const intervention = browserPackage.result.scenario_results.block_ac;
        assert.ok(
          intervention.reachable_states.every(state => baseline.reachable_states.includes(state)),
          "disabling a transition expanded reachable states"
        );
        const encode = value => JSON.stringify(value);
        const baselinePaths = new Set(baseline.trajectories.map(encode));
        assert.ok(
          intervention.trajectories.every(path => baselinePaths.has(encode(path))),
          "disabling a transition introduced a trajectory absent from baseline"
        );
      }
      if (fixture.name === "unreachable-transition-non-interference") {
        const blockAc = browserPackage.result.scenario_results.block_ac;
        const blockAcAndCd = browserPackage.result.scenario_results.block_ac_and_cd;
        assert.deepEqual(blockAcAndCd.reachable_states, blockAc.reachable_states,
          "disabling unreachable t_cd changed reachable states when t_ac already blocks its branch");
        assert.deepEqual(blockAcAndCd.trajectories, blockAc.trajectories,
          "disabling unreachable t_cd changed trajectories when t_ac already blocks its branch");
        assert.deepEqual(
          blockAcAndCd.enabled_transitions_at_initial_state,
          blockAc.enabled_transitions_at_initial_state,
          "disabling unreachable t_cd changed initial enabled transitions"
        );
      }
      if (fixture.statePermutationOf) {
        const original = semanticResults.get(fixture.statePermutationOf);
        assert.ok(original, fixture.name + ": original state order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          fixture.name + ": reordering states changed scenario semantics");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          fixture.name + ": reordering states changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          fixture.name + ": reordering states changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          fixture.name + ": reordering serialized states should change input SHA-256");
      }
      if (fixture.transitionPermutationOf) {
        const original = semanticResults.get(fixture.transitionPermutationOf);
        assert.ok(original, fixture.name + ": original transition order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          fixture.name + ": reordering transitions changed scenario semantics");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          fixture.name + ": reordering transitions changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          fixture.name + ": reordering transitions changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          fixture.name + ": reordering serialized transitions should change input SHA-256");
      }
      if (fixture.name === "same-target-conjunctive-guards") {
        const scenarios = browserPackage.result.scenario_results;
        assert.ok(!scenarios.baseline.effective_disabled_transitions.includes("t_bd"),
          "target transition should remain enabled when both prerequisites are enabled");
        for (const scenarioId of ["disable_ab", "disable_ac", "disable_both"]) {
          assert.ok(scenarios[scenarioId].effective_disabled_transitions.includes("t_bd"),
            "either disabled prerequisite should disable the shared target transition in " + scenarioId);
        }
      }
      if (fixture.relationOrderOf) {
        const original = semanticResults.get(fixture.relationOrderOf);
        assert.ok(original, fixture.name + ": original relation order must run first");
        for (const scenarioId of Object.keys(original.scenario_results)) {
          for (const key of ["reachable_states", "trajectories", "effective_disabled_transitions"]) {
            assert.deepEqual(
              browserPackage.result.scenario_results[scenarioId][key],
              original.scenario_results[scenarioId][key],
              "relation order changed " + key + " in " + scenarioId
            );
          }
        }
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          "reversing serialized relation order should change input SHA-256");
      }
      if (fixture.disabledTransitionOrderOf) {
        const original = semanticResults.get(fixture.disabledTransitionOrderOf);
        assert.ok(original, fixture.name + ": original disabled-transition order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          "reordering disabled transitions changed scenario outcomes");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          "reordering disabled transitions changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          "reordering disabled transitions changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          "reordering serialized disabled transitions should change input SHA-256");
      }
      if (fixture.monotonicInterventions) {
        const scenarios = browserPackage.result.scenario_results;
        const combined = scenarios.disable_both;
        for (const id of ["disable_ab", "disable_ac"]) {
          const single = scenarios[id];
          assert.ok(combined.reachable_states.every(state => single.reachable_states.includes(state)),
            "combined interventions added a reachable state relative to " + id);
          // Edge removal may create new terminal paths; compare path edges, not terminal-list membership.
          const explicitlyDisabled = new Set(id === "disable_ab" ? ["t_ab"] : ["t_ac"]);
          const relationDisabled = new Set(fixture.model.relations
            .filter(relation => explicitlyDisabled.has(relation.requires_transition_id))
            .map(relation => relation.transition_id));
          const singleDisabled = new Set([...explicitlyDisabled, ...relationDisabled]);
          for (const path of combined.trajectories) {
            const pathTransitions = path.filter(step => Object.prototype.hasOwnProperty.call(step, "transition"))
              .map(step => step.transition);
            assert.ok(pathTransitions.every(transitionId => !singleDisabled.has(transitionId)),
              "combined trajectory used an edge disabled in " + id);
          }
        }
      }
      if (fixture.expectedTruncation) {
        for (const [scenarioId, outcome] of Object.entries(browserPackage.result.scenario_results)) {
          assert.equal(outcome.truncated, true, fixture.name + ": expected truncation in " + scenarioId);
        }
      }
      if (fixture.disconnectedComponentOf) {
        const reference = semanticResults.get(fixture.disconnectedComponentOf);
        assert.ok(reference, fixture.name + ": reference fixture must run first");
        for (const [scenarioId, expected] of Object.entries(reference.scenario_results)) {
          const actual = browserPackage.result.scenario_results[scenarioId];
          assert.deepEqual(actual.reachable_states, expected.reachable_states,
            "disconnected component changed reachable states for " + scenarioId);
          assert.deepEqual(actual.trajectories, expected.trajectories,
            "disconnected component changed trajectories for " + scenarioId);
          assert.equal(actual.truncated, expected.truncated,
            "disconnected component changed truncation status for " + scenarioId);
        }
        assert.notEqual(browserPackage.result.input_sha256, reference.input_sha256,
          "adding a disconnected component should change input SHA-256");
      }
      if (fixture.scenarioOrderIsolationOf) {
        const original = semanticResults.get(fixture.scenarioOrderIsolationOf);
        assert.ok(original, fixture.name + ": original scenario order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          "reordering scenarios changed per-scenario outcomes");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          "reordering scenarios changed baseline comparisons");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          "reordering serialized scenarios should change input SHA-256");
      }
      if (fixture.guardNeutralityOf) {
        const reference = semanticResults.get(fixture.guardNeutralityOf);
        const actual = browserPackage.result.scenario_results.baseline;
        const expected = reference.scenario_results.baseline;
        for (const key of ["reachable_states", "trajectories", "effective_disabled_transitions"]) {
          assert.deepEqual(actual[key] ?? [], expected[key] ?? [], `inactive guard changed baseline ${key}`);
        }
      }
      if (fixture.name === "relation-guard-locality") {
        const baseline = browserPackage.result.scenario_results.baseline;
        const intervention = browserPackage.result.scenario_results.disable_ab;
        assert.ok(intervention.reachable_states.every(state => baseline.reachable_states.includes(state)),
          "direct intervention expanded reachable states");
        const baselinePaths = new Set(baseline.trajectories.map(path => JSON.stringify(path)));
        assert.ok(intervention.trajectories.every(path => baselinePaths.has(JSON.stringify(path))),
          "direct intervention introduced a trajectory absent from baseline");
        const states = intervention.reachable_states;
        assert.ok(states.includes("D"), "guard on t_bd unexpectedly removed D despite alternate A-C-D path");
        const pathStates = scenario => new Set(scenario.trajectories.map(path => JSON.stringify(path.map(step => step.state))));
        assert.ok(pathStates(baseline).has(JSON.stringify(["A", "C", "D"])));
        assert.ok(pathStates(intervention).has(JSON.stringify(["A", "C", "D"])));
        assert.ok(!pathStates(intervention).has(JSON.stringify(["A", "B", "D"])));
      }
      if (fixture.monotonicInterventions) {
        const model = fixture.model;
        const outcomes = browserPackage.result.scenario_results;
        const combined = outcomes.disable_both;
        assert.ok(combined, "combined intervention scenario must exist");
        for (const singleId of ["disable_ab", "disable_ac"]) {
          const single = outcomes[singleId];
          assert.ok(single, "single intervention scenario must exist: " + singleId);
          assert.ok(combined.reachable_states.every(state => single.reachable_states.includes(state)),
            "combined interventions expanded reachable states relative to " + singleId);
          const disabled = new Set(model.scenarios.find(scenario => scenario.id === singleId).disabled_transitions);
          const enabledTransitions = new Set((model.transitions || [])
            .filter(transition => !disabled.has(transition.id))
            .filter(transition => (model.relations || []).every(relation =>
              relation.transition_id === transition.id || !disabled.has(relation.requires_transition_id)))
            .map(transition => transition.id));
          for (const path of combined.trajectories) {
            const pathTransitions = new Set(path.filter(step => Object.prototype.hasOwnProperty.call(step, "transition"))
              .map(step => step.transition));
            assert.ok([...pathTransitions].every(id => enabledTransitions.has(id)),
              "combined trajectory used a transition unavailable under " + singleId);
          }
        }
      }
      if (fixture.relationAdditionMonotonicityOf) {
        const reference = semanticResults.get(fixture.relationAdditionMonotonicityOf);
        for (const scenarioId of Object.keys(reference.scenario_results)) {
          const before = reference.scenario_results[scenarioId];
          const after = browserPackage.result.scenario_results[scenarioId];
          assert.ok(after.reachable_states.every(state => before.reachable_states.includes(state)),
            `adding a guard expanded reachable states in ${scenarioId}`);
          const beforePaths = new Set(before.trajectories.map(path => JSON.stringify(path)));
          assert.ok(after.trajectories.every(path => beforePaths.has(JSON.stringify(path))),
            `adding a guard introduced a trajectory in ${scenarioId}`);
        }
      }
      if (fixture.duplicateSemanticGuardOf) {
        const reference = semanticResults.get(fixture.duplicateSemanticGuardOf);
        for (const scenarioId of Object.keys(reference.scenario_results)) {
          for (const key of ["reachable_states", "trajectories", "effective_disabled_transitions"]) {
            assert.deepEqual(
              browserPackage.result.scenario_results[scenarioId][key],
              reference.scenario_results[scenarioId][key],
              `duplicate semantic guard changed ${key} in ${scenarioId}`
            );
          }
        }
      }
      if (fixture.scenarioPermutationOf) {
        const original = semanticResults.get(fixture.scenarioPermutationOf);
        assert.ok(original, fixture.name + ": original scenario order must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          fixture.name + ": reordering scenarios changed scenario semantics");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          fixture.name + ": reordering scenarios changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          fixture.name + ": reordering scenarios changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          fixture.name + ": reordering serialized scenarios should change input SHA-256");
      }
      if (fixture.permutationOf) {
        const original = semanticResults.get(fixture.permutationOf);
        assert.ok(original, fixture.name + ": original relation ordering must run first");
        assert.deepEqual(browserPackage.result.scenario_results, original.scenario_results,
          fixture.name + ": permuting relation order changed scenario semantics");
        assert.deepEqual(browserPackage.result.comparisons_to_baseline, original.comparisons_to_baseline,
          fixture.name + ": permuting relation order changed baseline comparisons");
        assert.equal(browserPackage.result.result_sha256, original.result_sha256,
          fixture.name + ": permuting relation order changed result SHA-256");
        assert.notEqual(browserPackage.result.input_sha256, original.input_sha256,
          fixture.name + ": permuting serialized relation order should change input SHA-256");
      } else if (fixture.model.rule_profile?.type === "relation_guarded_graph" &&
                 fixture.name.startsWith("generated-cyclic-guards-")) {
        semanticResults.set(fixture.model.model_id, browserPackage.result);
      }
      semanticResults.set(fixture.name, browserPackage.result);
      report.push(fixture.name + ": PASS");
    }
    const invalidReport = [];
    for (const fixture of invalidFixtures()) {
      const pythonReject = pythonRejects(engineDir, fixture.model);
      assert.equal(pythonReject, true, fixture.name + ": Python must reject invalid input");
      const fixtureJson = JSON.stringify(fixture.model, null, 2);
      if ((fixture.model.transitions || []).length > 2000 || (fixture.model.states || []).length > 500) {
        // Set oversized fixtures without firing the editor's per-keystroke input handler.
        await page.locator("#model").evaluate((el, value) => { el.value = value; }, fixtureJson);
      } else {
        await page.locator("#model").fill(fixtureJson, { timeout: 15000 });
      }
      await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
      await page.locator("#status").getByText(/No se ha podido ejecutar/).waitFor({ timeout: 5000 });
      const status = await page.locator("#status").innerText();
      assert.match(status, /No se ha podido ejecutar/, fixture.name + ": browser must reject invalid input");
      invalidReport.push(fixture.name + ": REJECTED in both runtimes");
    }
    console.log("PASS: " + report.length + " valid cross-runtime fixtures matched exactly.\n" +
      "PASS: " + invalidReport.length + " invalid fixtures rejected in both runtimes.\n" +
      report.join("\n") + "\n" + invalidReport.join("\n"));
  } finally {
    if (fs.existsSync(outputPath)) fs.unlinkSync(outputPath);
    await browser.close();
  }
})().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
