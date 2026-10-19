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
  const rejected = ["finite_deterministic_graph", "relation_guarded_graph"].map(type =>
    pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); m['rule_profile']={'type':sys.argv[1],'version':'1'};\ntry: e.validate_model(m); print(json.dumps({'rejected':False}))\nexcept e.ModelValidationError as x: print(json.dumps({'rejected':True,'reason':str(x)}))",
      model
    )
  );
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
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const pkg = await page.evaluate(() => window.lastPackage);
    assert.ok(pkg && pkg.input && pkg.result, "browser must export an inspectable package");
    assert.equal(pkg.input.rule_profile.type, "temporal_prerequisite_graph");
    const invalid = {...loaded, rule_profile:{type:"relation_guarded_graph",version:"1"}};
    await page.locator("#model").fill(JSON.stringify(invalid));
    await page.locator("#run").click();
    assert.match(await page.locator("#status").innerText(), /Perfil retirado|no compatible|temporal_prerequisite_graph/i);
  } finally { await browser.close(); }
  process.stdout.write("PASS: profile-3-only browser/Python contract\n");
})().catch(error => { console.error(error); process.exit(1); });
