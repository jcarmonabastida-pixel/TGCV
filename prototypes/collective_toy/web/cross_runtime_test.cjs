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
      { name: "missing", condition: "humidity < 30", values: {}, reachable: false, status: "NOT_EVALUABLE", reason: "missing_variable" },
      { name: "nonnumeric", condition: "humidity < 30", values: { humidity: "20" }, reachable: false, status: "NOT_EVALUABLE", reason: "variable_not_numeric" },
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
