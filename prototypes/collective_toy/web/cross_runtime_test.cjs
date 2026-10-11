const { chromium } = require("playwright");
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const os = require("node:os");
const assert = require("node:assert/strict");

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

  return cases;
}

function generatedFixtures() {
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
    console.log("PASS: relation editor profile switching, add/remove, profile 2 execution, and profile 1 inertness.");

    const validFixtures = [...fixtures(), ...generatedFixtures()];
    for (const fixture of validFixtures) {
      await page.locator("#model").fill(JSON.stringify(fixture.model, null, 2));
      await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
      await page.getByText(/Ejecución completada/).waitFor({ timeout: 5000 });

      const [download] = await Promise.all([
        page.waitForEvent("download"),
        page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click()
      ]);
      await download.saveAs(outputPath);
      const browserPackage = JSON.parse(fs.readFileSync(outputPath, "utf8"));
      fs.unlinkSync(outputPath);

      const pyResult = runPython(engineDir, fixture.model);
      assert.deepEqual(browserPackage.result.scenario_results, pyResult.scenario_results,
        fixture.name + ": scenario results differ");
      assert.deepEqual(browserPackage.result.comparisons_to_baseline, pyResult.comparisons_to_baseline,
        fixture.name + ": baseline comparisons differ");
      assert.equal(browserPackage.result.input_sha256, pyResult.input_sha256,
        fixture.name + ": input SHA-256 differs");
      assert.equal(browserPackage.result.result_sha256, pyResult.result_sha256,
        fixture.name + ": result SHA-256 differs");
      report.push(fixture.name + ": PASS");
    }
    const invalidReport = [];
    for (const fixture of invalidFixtures()) {
      const pythonReject = pythonRejects(engineDir, fixture.model);
      assert.equal(pythonReject, true, fixture.name + ": Python must reject invalid input");
      await page.locator("#model").fill(JSON.stringify(fixture.model, null, 2));
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
