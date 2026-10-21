const { chromium } = require("playwright");
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");

const root = path.resolve(__dirname, "..");
const enginePath = path.join(root, "collective_toy_engine_001.py");
const htmlPath = path.join(__dirname, "index.html");
const profile3 = { type: "temporal_prerequisite_graph", version: "1" };
const model = {
  schema_version: "collective-toy-input-001", model_id: "profile3-cross-runtime",
  initial_state: "A", states: ["A", "B", "C", "D"],
  transitions: [
    { id: "t_ab", source: "A", target: "B" },
    { id: "t_ac", source: "A", target: "C" },
    { id: "t_cd", source: "C", target: "D" }
  ],
  relations: [{ id: "r_cd_ab", type: "requires_prior_execution", transition_id: "t_cd", requires_transition_id: "t_ab" }],
  rule_profile: profile3,
  scenarios: [{ id: "baseline", disabled_transitions: [] }],
  exploration: { max_depth: 5, max_trajectories: 100 }
};
function pythonJson(source, input) {
  const run = spawnSync(process.env.PYTHON || "python", ["-c", source], {
    cwd: root, input: JSON.stringify(input), encoding: "utf8"
  });
  assert.equal(run.status, 0, "Python engine failed: " + run.stderr);
  return JSON.parse(run.stdout);
}
(async () => {
  assert.ok(fs.existsSync(enginePath));
  const engineRun = pythonJson(
    "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
    model
  );
  assert.equal(engineRun.input.rule_profile.type, "temporal_prerequisite_graph");
  assert.equal(engineRun.result.validation, "PASS");
  const rejected = ["finite_deterministic_graph", "relation_guarded_graph"].map(type => {
    const retiredModel = { ...model, rule_profile: { type, version: "1" } };
    const script = [
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin)",
      "try:",
      " e.validate_model(m)",
      " print(json.dumps({'rejected':False}))",
      "except e.ModelValidationError as x:",
      " print(json.dumps({'rejected':True,'reason':str(x)}))"
    ].join("\n");
    return pythonJson(script, retiredModel);
  });
  assert.ok(rejected.every(x => x.rejected), "retired profiles must fail closed");
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto("file://" + htmlPath);
    for (const selector of ["#profile-editor", "#guarded-transition", "#required-transition", "#add-relation", "#relation-list"]) {
      assert.equal(await page.locator(selector).count(), 0, "retired control must be absent: " + selector);
    }
    const loaded = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(loaded.rule_profile, profile3);
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(model));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const pkg = await page.evaluate(() => window.lastPackage);
    assert.ok(pkg && pkg.input && pkg.result, "browser must export an inspectable package");
    assert.equal(pkg.input.rule_profile.type, "temporal_prerequisite_graph");
    assert.deepEqual(pkg.result, engineRun.result, "browser and Python temporal-profile results must be identical");
    // Conditional transitions must survive the cross-runtime package contract,
    // while both runtimes block them because neither evaluates their condition.
    const conditionalModel = {
      ...model,
      schema_version: "collective-toy-input-002",
      model_id: "conditional-cross-runtime",
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "humidity is low" },
        { id: "t_ac", source: "A", target: "C" },
        { id: "t_cd", source: "C", target: "D" }
      ],
      relations: []
    };
    const conditionalEngineRun = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      conditionalModel
    );
    assert.equal(conditionalEngineRun.input.transitions[0].condition, "humidity is low");
    assert.ok(!conditionalEngineRun.result.scenario_results.baseline.reachable_states.includes("B"),
      "Python engine must not traverse an unevaluated conditional transition");
    assert.deepEqual(conditionalEngineRun.result.scenario_results.baseline.blocked_conditions, [{
      transition_id: "t_ab", source: "A", target: "B", condition: "humidity is low",
      status: "NOT_EVALUABLE", reason: "unsupported_expression"
    }], "Python must report unsupported conditions explicitly instead of silently dropping them");
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(conditionalModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const conditionalPkg = await page.evaluate(() => window.lastPackage);
    assert.equal(conditionalPkg.input.transitions[0].condition, "humidity is low",
      "browser package must preserve the conditional metadata");
    assert.ok(!conditionalPkg.result.scenario_results.baseline.reachable_states.includes("B"),
      "browser engine must not traverse an unevaluated conditional transition");
    assert.deepEqual(conditionalPkg.result.scenario_results.baseline.blocked_conditions, [{
      transition_id: "t_ab", source: "A", target: "B", condition: "humidity is low",
      status: "NOT_EVALUABLE", reason: "unsupported_expression"
    }], "browser must report unsupported conditions explicitly instead of silently dropping them");
    assert.deepEqual(conditionalPkg.result, conditionalEngineRun.result,
      "browser and Python conditional-transition results must be identical");

    // The shared bounded grammar must enable only TRUE predicates; FALSE and
    // NOT_EVALUABLE predicates remain blocked and produce identical records.
    const evaluatedCases = [
      { name: "true", condition: "humidity < 30", values: { humidity: 20 }, reachable: true, status: null, reason: null },
      { name: "false", condition: "humidity < 30", values: { humidity: 40 }, reachable: false, status: "FALSE", reason: null },
      { name: "boundary", condition: "humidity <= 30", values: { humidity: 30 }, reachable: true, status: null, reason: null },
      { name: "equal_true", condition: "humidity == 30", values: { humidity: 30 }, reachable: true, status: null, reason: null },
      { name: "not_equal_true", condition: "humidity != 30", values: { humidity: 20 }, reachable: true, status: null, reason: null },
      { name: "greater_equal_true", condition: "humidity >= 30", values: { humidity: 30 }, reachable: true, status: null, reason: null },
      { name: "greater_true", condition: "humidity > 30", values: { humidity: 31 }, reachable: true, status: null, reason: null },
      { name: "greater_false", condition: "humidity > 30", values: { humidity: 30 }, reachable: false, status: "FALSE", reason: null },
      { name: "missing", condition: "humidity < 30", values: {}, reachable: false, status: "NOT_EVALUABLE", reason: "missing_variable" },
      { name: "nonnumeric", condition: "humidity < 30", values: { humidity: "20" }, reachable: false, status: "NOT_EVALUABLE", reason: "variable_not_numeric" },
      { name: "boolean", condition: "humidity < 30", values: { humidity: true }, reachable: false, status: "NOT_EVALUABLE", reason: "variable_not_numeric" },
      { name: "unsupported", condition: "humidity ** 2", values: { humidity: 20 }, reachable: false, status: "NOT_EVALUABLE", reason: "unsupported_expression" }
    ];
    for (const item of evaluatedCases) {
      const caseModel = {
        ...conditionalModel,
        model_id: "conditional-evaluator-" + item.name,
        condition_values: item.values,
        transitions: [
          { id: "t_ab", source: "A", target: "B", condition: item.condition },
          { id: "t_ac", source: "A", target: "C" },
          { id: "t_cd", source: "C", target: "D" }
        ]
      };
      const pyCase = pythonJson(
        "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
        caseModel
      );
      await page.locator("#model").evaluate((el, value) => {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
      }, JSON.stringify(caseModel));
      await page.locator("#run").click();
      await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
      const browserCase = await page.evaluate(() => window.lastPackage);
      const pyScenario = pyCase.result.scenario_results.baseline;
      const browserScenario = browserCase.result.scenario_results.baseline;
      assert.equal(pyScenario.reachable_states.includes("B"), item.reachable, item.name + ": Python reachability");
      assert.equal(browserScenario.reachable_states.includes("B"), item.reachable, item.name + ": browser reachability");
      if (item.status === null) {
        assert.deepEqual(pyScenario.blocked_conditions, [], item.name + ": Python has no blocked condition");
        assert.deepEqual(browserScenario.blocked_conditions, [], item.name + ": browser has no blocked condition");
      } else {
        assert.equal(pyScenario.blocked_conditions[0].status, item.status, item.name + ": Python condition status");
        assert.equal(pyScenario.blocked_conditions[0].reason, item.reason, item.name + ": Python condition reason");
        assert.equal(browserScenario.blocked_conditions[0].status, item.status, item.name + ": browser condition status");
        assert.equal(browserScenario.blocked_conditions[0].reason, item.reason, item.name + ": browser condition reason");
      }
      assert.deepEqual(browserCase.result, pyCase.result, item.name + ": Python/browser outputs must match exactly");
    }

    // Domain-independent branching: complementary predicates must select
    // exactly the branch enabled by the explicit numeric input.
    for (const branchCase of [
      { name: "temperature_low", values: { temperature: 8 }, expected: ["A", "B"] },
      { name: "temperature_high", values: { temperature: 12 }, expected: ["A", "C"] }
    ]) {
      const branchingModel = {
        ...conditionalModel,
        model_id: "branching-" + branchCase.name,
        condition_values: branchCase.values,
        states: ["A", "B", "C"],
        transitions: [
          { id: "t_low", source: "A", target: "B", condition: "temperature < 10" },
          { id: "t_high", source: "A", target: "C", condition: "temperature >= 10" }
        ],
        relations: [],
        exploration: { max_depth: 3, max_trajectories: 20 }
      };
      const pyBranch = pythonJson(
        "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
        branchingModel
      );
      await page.locator("#model").evaluate((el, value) => {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
      }, JSON.stringify(branchingModel));
      await page.locator("#run").click();
      await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
      const browserBranch = await page.evaluate(() => window.lastPackage);
      const pyScenario = pyBranch.result.scenario_results.baseline;
      const browserScenario = browserBranch.result.scenario_results.baseline;
      assert.deepEqual(pyScenario.reachable_states, branchCase.expected.slice().sort(), branchCase.name + ": Python selects expected branch");
      assert.deepEqual(browserScenario.reachable_states, branchCase.expected.slice().sort(), branchCase.name + ": browser selects expected branch");
      assert.deepEqual(browserBranch.result, pyBranch.result, branchCase.name + ": branch outputs match exactly");
      assert.equal(pyScenario.blocked_conditions.length, 1, branchCase.name + ": Python blocks exactly one branch");
      assert.equal(browserScenario.blocked_conditions.length, 1, branchCase.name + ": browser blocks exactly one branch");
    }

    // Conditional return/cycle: an enabled edge back to the initial state
    // remains executable, while its false alternative is blocked identically.
    const returnModel = {
      ...conditionalModel,
      model_id: "conditional-return-cycle",
      states: ["A", "B", "C"],
      initial_state: "A",
      condition_values: { step: 1 },
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "step == 1" },
        { id: "t_ba", source: "B", target: "A", condition: "step >= 1" },
        { id: "t_ac", source: "A", target: "C", condition: "step > 1" }
      ],
      relations: [],
      exploration: { max_depth: 5, max_trajectories: 20 }
    };
    const pyReturn = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      returnModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(returnModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserReturn = await page.evaluate(() => window.lastPackage);
    const pyReturnScenario = pyReturn.result.scenario_results.baseline;
    const browserReturnScenario = browserReturn.result.scenario_results.baseline;
    assert.ok(pyReturnScenario.reachable_states.includes("A") && pyReturnScenario.reachable_states.includes("B"),
      "Python must preserve reachability across the enabled return cycle");
    assert.ok(browserReturnScenario.reachable_states.includes("A") && browserReturnScenario.reachable_states.includes("B"),
      "browser must preserve reachability across the enabled return cycle");
    assert.ok(!pyReturnScenario.reachable_states.includes("C"), "Python must block the false branch");
    assert.ok(!browserReturnScenario.reachable_states.includes("C"), "browser must block the false branch");
    assert.deepEqual(browserReturn.result, pyReturn.result, "conditional return/cycle outputs must match exactly");
    assert.deepEqual(pyReturnScenario.blocked_conditions.map(x => [x.transition_id,x.status]), [["t_ac","FALSE"]]);
    assert.deepEqual(browserReturnScenario.blocked_conditions.map(x => [x.transition_id,x.status]), [["t_ac","FALSE"]]);

    // Fail-closed chain: a true first condition reaches B, but a missing
    // variable on the next edge must prevent reaching C and remain auditable.
    const chainModel = {
      ...conditionalModel,
      model_id: "conditional-chain-missing-value",
      states: ["A", "B", "C"],
      initial_state: "A",
      condition_values: { gate: 1 },
      transitions: [
        { id: "chain_ab", source: "A", target: "B", condition: "gate == 1" },
        { id: "chain_bc", source: "B", target: "C", condition: "authorization_level >= 2" }
      ],
      relations: [],
      exploration: { max_depth: 5, max_trajectories: 20 }
    };
    const pyChain = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      chainModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(chainModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserChain = await page.evaluate(() => window.lastPackage);
    const pyChainScenario = pyChain.result.scenario_results.baseline;
    const browserChainScenario = browserChain.result.scenario_results.baseline;
    assert.ok(pyChainScenario.reachable_states.includes("B"), "Python reaches B through the true first condition");
    assert.ok(browserChainScenario.reachable_states.includes("B"), "browser reaches B through the true first condition");
    assert.ok(!pyChainScenario.reachable_states.includes("C"), "Python must not cross the missing-value condition");
    assert.ok(!browserChainScenario.reachable_states.includes("C"), "browser must not cross the missing-value condition");
    assert.deepEqual(browserChain.result, pyChain.result, "conditional chain outputs must match exactly");
    assert.deepEqual(pyChainScenario.blocked_conditions.map(x => [x.transition_id,x.status,x.reason]),
      [["chain_bc","NOT_EVALUABLE","missing_variable"]]);
    assert.deepEqual(browserChainScenario.blocked_conditions.map(x => [x.transition_id,x.status,x.reason]),
      [["chain_bc","NOT_EVALUABLE","missing_variable"]]);

    // Adversarial temporal dependency: t_ac must remain unavailable because
    // its prerequisite t_bd is executable only after leaving A, and no path returns to A.
    const dependencyModel = {
      ...conditionalModel,
      model_id: "conditional-prerequisite-not-executed-on-path",
      states: ["A", "B", "C", "D"],
      initial_state: "A",
      condition_values: { permit: 1 },
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "permit == 1" },
        { id: "t_ac", source: "A", target: "C", condition: "permit == 1" },
        { id: "t_bd", source: "B", target: "D" }
      ],
      relations: [
        { id: "r_ac_requires_bd", type: "requires_prior_execution", transition_id: "t_ac", requires_transition_id: "t_bd" }
      ],
      exploration: { max_depth: 5, max_trajectories: 20 }
    };
    const pyDependency = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      dependencyModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(dependencyModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserDependency = await page.evaluate(() => window.lastPackage);
    const pyDependencyScenario = pyDependency.result.scenario_results.baseline;
    const browserDependencyScenario = browserDependency.result.scenario_results.baseline;
    for (const [scenario, runtime] of [[pyDependencyScenario, "Python"], [browserDependencyScenario, "browser"]]) {
      assert.ok(scenario.reachable_states.includes("B"), runtime + " can reach B");
      assert.ok(scenario.reachable_states.includes("D"), runtime + " can execute prerequisite t_bd after reaching B");
      assert.ok(!scenario.reachable_states.includes("C"),
        runtime + " must not traverse t_ac before prerequisite t_bd has been executed");
    }
    assert.deepEqual(browserDependency.result, pyDependency.result,
      "temporal dependency outputs must match exactly");

    // Complementary case: the prerequisite is executed, the path returns to
    // the dependent transition's source, and only then may that transition fire.
    const satisfiedDependencyModel = {
      ...conditionalModel,
      model_id: "conditional-prerequisite-satisfied-on-path",
      states: ["A", "B", "D", "C"],
      initial_state: "A",
      condition_values: { permit: 1 },
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "permit == 1" },
        { id: "t_bd", source: "B", target: "D" },
        { id: "t_da", source: "D", target: "A" },
        { id: "t_ac", source: "A", target: "C", condition: "permit == 1" }
      ],
      relations: [
        { id: "r_ac_requires_bd", type: "requires_prior_execution", transition_id: "t_ac", requires_transition_id: "t_bd" }
      ],
      exploration: { max_depth: 6, max_trajectories: 30 }
    };
    const pySatisfiedDependency = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      satisfiedDependencyModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(satisfiedDependencyModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserSatisfiedDependency = await page.evaluate(() => window.lastPackage);
    const pySatisfiedScenario = pySatisfiedDependency.result.scenario_results.baseline;
    const browserSatisfiedScenario = browserSatisfiedDependency.result.scenario_results.baseline;
    assert.ok(pySatisfiedScenario.reachable_states.includes("C"),
      "Python must allow t_ac after t_bd has been executed and the path returns to A");
    assert.ok(browserSatisfiedScenario.reachable_states.includes("C"),
      "browser must allow t_ac after t_bd has been executed and the path returns to A");
    assert.deepEqual(browserSatisfiedDependency.result, pySatisfiedDependency.result,
      "satisfied temporal dependency outputs must match exactly");

    // All prerequisites are conjunctive: satisfying only one of two required
    // transitions must not enable the guarded transition.
    const multiplePrerequisitesModel = {
      ...conditionalModel,
      model_id: "conditional-multiple-prerequisites-conjunctive",
      states: ["A", "B", "D", "E", "C"],
      initial_state: "A",
      condition_values: { permit: 1 },
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "permit == 1" },
        { id: "t_bd", source: "B", target: "D" },
        { id: "t_de", source: "D", target: "E" },
        { id: "t_ea", source: "E", target: "A" },
        { id: "t_ac", source: "A", target: "C", condition: "permit == 1" }
      ],
      relations: [
        { id: "r_ac_requires_bd", type: "requires_prior_execution", transition_id: "t_ac", requires_transition_id: "t_bd" },
        { id: "r_ac_requires_de", type: "requires_prior_execution", transition_id: "t_ac", requires_transition_id: "t_de" }
      ],
      exploration: { max_depth: 7, max_trajectories: 40 }
    };
    const pyMultiplePrerequisites = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      multiplePrerequisitesModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(multiplePrerequisitesModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserMultiplePrerequisites = await page.evaluate(() => window.lastPackage);
    const pyMultipleScenario = pyMultiplePrerequisites.result.scenario_results.baseline;
    const browserMultipleScenario = browserMultiplePrerequisites.result.scenario_results.baseline;
    for (const [scenario, runtime] of [[pyMultipleScenario, "Python"], [browserMultipleScenario, "browser"]]) {
      assert.ok(scenario.reachable_states.includes("E"), runtime + " can execute both prerequisite transitions");
      assert.ok(scenario.reachable_states.includes("C"),
        runtime + " may traverse t_ac after both t_bd and t_de have been executed");
    }
    assert.deepEqual(browserMultiplePrerequisites.result, pyMultiplePrerequisites.result,
      "multiple temporal prerequisite outputs must match exactly");

    // Adversarial partial satisfaction: t_bd executes, but t_de is disabled.
    // The guarded transition t_ac requires BOTH; satisfying only t_bd must not enable it.
    const partialPrerequisiteModel = {
      ...multiplePrerequisitesModel,
      model_id: "conditional-multiple-prerequisites-partial-only",
      scenarios: [{ id: "baseline", disabled_transitions: ["t_de"] }]
    };
    const pyPartialPrerequisites = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      partialPrerequisiteModel
    );
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(partialPrerequisiteModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const browserPartialPrerequisites = await page.evaluate(() => window.lastPackage);
    const pyPartialScenario = pyPartialPrerequisites.result.scenario_results.baseline;
    const browserPartialScenario = browserPartialPrerequisites.result.scenario_results.baseline;
    for (const [scenario, runtime] of [[pyPartialScenario, "Python"], [browserPartialScenario, "browser"]]) {
      assert.ok(scenario.reachable_states.includes("D"), runtime + " executes the first prerequisite t_bd");
      assert.ok(!scenario.reachable_states.includes("E"), runtime + " cannot execute disabled prerequisite t_de");
      assert.ok(!scenario.reachable_states.includes("C"),
        runtime + " must not enable t_ac when only one of its two prerequisites has executed");
    }
    assert.deepEqual(browserPartialPrerequisites.result, pyPartialPrerequisites.result,
      "partial multiple-prerequisite outputs must match exactly");

    // Concrete execution must distinguish true, false, and non-evaluable conditions.
    const concreteConditionCases = [
      { name: "true", condition: "humidity < 30", values: { humidity: 20 }, expectedStatus: "COMPLETED", expectedReason: null, expectedSteps: 2 },
      { name: "false", condition: "humidity < 30", values: { humidity: 40 }, expectedStatus: "BLOCKED", expectedReason: "condition_false", expectedSteps: 0 },
      { name: "not-evaluable", condition: "humidity is low", values: {}, expectedStatus: "BLOCKED", expectedReason: "condition_not_evaluable", expectedSteps: 0 }
    ];
    for (const item of concreteConditionCases) {
      const sequenceModel = {
        ...model,
        schema_version: "collective-toy-input-002",
        model_id: "concrete-condition-" + item.name,
        initial_state: "A",
        states: ["A", "B", "C"],
        transitions: [
          { id: "t_ab", source: "A", target: "B", condition: item.condition },
          { id: "t_bc", source: "B", target: "C" }
        ],
        relations: [],
        condition_values: item.values,
        scenarios: [{ id: "baseline", disabled_transitions: [] }],
        exploration: { max_depth: 4, max_trajectories: 20 }
      };
      await page.locator("#model").evaluate((el, value) => {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
      }, JSON.stringify(sequenceModel));
      await page.locator("#run").click();
      await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
      await page.locator("#sequence-input").fill("t_ab, t_bc");
      await page.locator("#execute-sequence").click();
      const trace = await page.locator("#sequence-trace").evaluate(el => el._trace);
      assert.ok(trace, item.name + ": concrete trace must be retained");
      assert.equal(trace.status, item.expectedStatus, item.name + ": concrete execution status");
      assert.equal(trace.steps.length, item.expectedSteps, item.name + ": only executed steps belong in the trace");
      assert.equal(trace.blocked_step && trace.blocked_step.reason || null, item.expectedReason,
        item.name + ": the block reason must distinguish false from non-evaluable");
      assert.equal(trace.blocked_step && trace.blocked_step.index || null,
        item.expectedReason ? 1 : null, item.name + ": blocked index must identify the first attempted step");
      const exported = await page.evaluate(() => window.lastPackage);
      assert.ok(!Object.prototype.hasOwnProperty.call(exported, "outcome_record"),
        item.name + ": a newly executed/blocked trace must not reuse an unrelated outcome");
    }

    const invalid = {...model, rule_profile:{type:"relation_guarded_graph",version:"1"}};
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(invalid));
    await page.locator("#run").click();
    assert.match(await page.locator("#status").innerText(), /Perfil retirado|no compatible|temporal_prerequisite_graph/i);
  } finally { await browser.close(); }
  process.stdout.write("PASS: profile-3-only browser/Python contract\n");
})().catch(error => { console.error(error); process.exit(1); });
