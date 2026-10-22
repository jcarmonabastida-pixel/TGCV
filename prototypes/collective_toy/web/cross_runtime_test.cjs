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
    assert.equal(await page.locator("#model").inputValue(), "", "both graph models must start empty until the example is requested");
    assert.equal(await page.locator("#graph rect").count(), 0, "system graph must start blank");
    assert.equal(await page.locator("#tgcv-graph circle").count(), 0, "TGCV graph must start blank");
    await page.locator("#load").click();
    assert.equal(await page.locator("#graph rect").count(), 4, "loading the example must populate the system graph");
    assert.equal(await page.locator("#tgcv-graph circle").count(), 4, "loading the example must populate the TGCV graph");
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
    assert.deepEqual(conditionalPkg.result, conditionalEngineRun.result,
      "browser and Python conditional-transition results must be identical");

    // The evaluator UI must drive actual exploration, not merely store a label.
    const trueModel = {
      ...conditionalModel,
      scenarios: [{
        id: "baseline", disabled_transitions: [],
        condition_evaluations: { t_ab: { condition: "humidity is low", result: "TRUE" } }
      }]
    };
    const trueEngineRun = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      trueModel
    );
    const evaluator = page.locator('#transition-review-list select[data-condition-evaluation="t_ab"]');
    await evaluator.selectOption("TRUE");
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const truePkg = await page.evaluate(() => window.lastPackage);
    assert.ok(truePkg.result.scenario_results.baseline.reachable_states.includes("B"),
      "TRUE evaluation must enable the conditional transition in the browser");
    assert.deepEqual(truePkg.result, trueEngineRun.result,
      "browser and Python results must agree when the condition is TRUE");
    assert.match(await page.locator("#graph").textContent(), /VERDADERA: humidity is low/,
      "the system graph must display the active TRUE condition evaluation");
    assert.match(await page.locator("#tgcv-provenance-note").innerText(), /no declara una correspondencia TGCV explícita/i,
      "a custom model without an explicit TGCV mapping must explain why the TGCV graph is not inferred");
    assert.equal((await page.locator("#tgcv-graph").locator("g").count()), 0,
      "a custom model without an explicit TGCV mapping must not fabricate TGCV graph nodes");

    const falseModel = {
      ...conditionalModel,
      scenarios: [{
        id: "baseline", disabled_transitions: [],
        condition_evaluations: { t_ab: { condition: "humidity is low", result: "FALSE" } }
      }]
    };
    const falseEngineRun = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      falseModel
    );
    await page.locator('#transition-review-list select[data-condition-evaluation="t_ab"]').selectOption("FALSE");
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const falsePkg = await page.evaluate(() => window.lastPackage);
    assert.ok(!falsePkg.result.scenario_results.baseline.reachable_states.includes("B"),
      "FALSE evaluation must keep the conditional transition blocked");
    assert.deepEqual(falsePkg.result, falseEngineRun.result,
      "browser and Python results must agree when the condition is FALSE");
    assert.match(await page.locator("#graph").textContent(), /FALSA: humidity is low/,
      "the system graph must display the active FALSE condition evaluation");
    assert.match(await page.locator("#tgcv-provenance-note").innerText(), /no declara una correspondencia TGCV explícita/i,
      "the TGCV graph must remain explicitly unavailable for an unmapped custom model after FALSE evaluation");

    const unknownModel = {
      ...conditionalModel,
      scenarios: [{
        id: "baseline", disabled_transitions: [],
        condition_evaluations: { t_ab: { condition: "humidity is low", result: "UNKNOWN" } }
      }]
    };
    const unknownEngineRun = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      unknownModel
    );
    await page.locator('#transition-review-list select[data-condition-evaluation="t_ab"]').selectOption("UNKNOWN");
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const unknownPkg = await page.evaluate(() => window.lastPackage);
    assert.ok(!unknownPkg.result.scenario_results.baseline.reachable_states.includes("B"),
      "UNKNOWN evaluation must keep the conditional transition blocked");
    assert.deepEqual(unknownPkg.result, unknownEngineRun.result,
      "browser and Python results must agree when the condition is UNKNOWN");

    const staleEvaluationModel = {
      ...conditionalModel,
      transitions: [
        { id: "t_ab", source: "A", target: "B", condition: "humidity is high" },
        ...conditionalModel.transitions.slice(1)
      ],
      scenarios: [{
        id: "baseline", disabled_transitions: [],
        condition_evaluations: { t_ab: { condition: "humidity is low", result: "TRUE" } }
      }]
    };
    const staleEngineCheck = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); exec('try:\\n e.validate_model(m)\\n print(json.dumps({\\'rejected\\':False}))\\nexcept e.ModelValidationError as x:\\n print(json.dumps({\\'rejected\\':True,\\'reason\\':str(x)}))')",
      staleEvaluationModel
    );
    assert.equal(staleEngineCheck.rejected, true,
      "Python must reject an evaluation whose stored condition text is stale");
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(staleEvaluationModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/obsoleta|ya cambió/i}).waitFor({timeout:5000});

    // Explicit custom mapping: evaluator state must propagate to the declared TGCV transformation.
    const explicitlyMappedModel = {
      ...conditionalModel,
      tgcv_mapping: {
        schema: "tgcv-explicit-mapping-001",
        mapping_rule: "user-declared-transition-transformation-map-v1",
        provenance: "user-declared",
        mappings: [
          {system_transition_id:"t_ab",tgcv_transformation_id:"T_HUMIDITY"},
          {system_transition_id:"t_ac",tgcv_transformation_id:"T_AC"},
          {system_transition_id:"t_cd",tgcv_transformation_id:"T_CD"}
        ],
        relations: [["T_AC","T_CD"],["T_HUMIDITY","T_CD"]]
      },
      scenarios: [{
        id:"baseline",disabled_transitions:[],
        condition_evaluations:{t_ab:{condition:"humidity is low",result:"TRUE"}}
      }]
    };
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(explicitlyMappedModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    assert.match(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "an explicitly mapped transformation must appear when its system transition is reachable");
    assert.match(await page.locator("#tgcv-provenance-note").innerText(), /user-declared/,
      "the TGCV view must preserve the declared mapping provenance");
    assert.match(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY.*T_CD|T_CD.*T_HUMIDITY/,
      "the TGCV graph must display the declared relation when both mapped transformations are accessible");

    for (const evaluation of ["FALSE", "UNKNOWN"]) {
      await page.locator('#transition-review-list select[data-condition-evaluation="t_ab"]').selectOption(evaluation);
      await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
      const currentTgcvText = await page.locator("#tgcv-graph").textContent();
      assert.doesNotMatch(currentTgcvText, /T_HUMIDITY/,
        evaluation + " must remove the explicitly mapped transformation from the current TGCV graph");
      assert.doesNotMatch(currentTgcvText, /T_HUMIDITY\\s*→\\s*T_CD/,
        evaluation + " must remove relations whose transformation endpoint is no longer accessible");
      assert.match(currentTgcvText, /T_CD/,
        evaluation + " must retain unrelated accessible TGCV transformations");
      assert.match(await page.locator("#graph").textContent(), new RegExp(evaluation === "FALSE" ? "FALSA: humidity is low" : "DESCONOCIDA: humidity is low"),
        evaluation + " must remain visible on the system graph");
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
