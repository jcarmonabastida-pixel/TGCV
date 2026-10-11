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


  const scenarioOrderReference = clone(base);
  scenarioOrderReference.model_id = "scenario-order-invariance";
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

  const relationGuardMonotonicity = clone(base);
  relationGuardMonotonicity.model_id = "relation-guard-intervention-monotonicity";
  relationGuardMonotonicity.rule_profile = { type: "relation_guarded_graph", version: "2" };
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

function verifyExportedPackage(engineDir, exportedPackage, label) {
  assert.ok(
    ["collective-toy-run-package-001", "collective-toy-browser-run-001"].includes(exportedPackage.package_version),
    label + ": unsupported package version"
  );
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

  const replayed = runPython(engineDir, exportedPackage.input);
  assert.deepEqual(replayed, exportedPackage.result,
    label + ": independently replayed Python result differs from exported result");
  return true;
}

(async () => {
  const root = path.resolve(__dirname, "../../..");
  const htmlPath = path.join(root, "prototypes/collective_toy/web/index.html");
  const engineDir = path.join(root, "prototypes/collective_toy");
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ acceptDownloads: true });
  const outputPath = path.join(os.tmpdir(), "collective-toy-browser-" + process.pid + ".json");
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
    console.log("PASS: relation editor profile switching, add/remove, profile 2 execution, profile 1 inertness, and independent export replay.");

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
