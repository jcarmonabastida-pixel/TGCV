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
    for (const fixture of fixtures()) {
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
