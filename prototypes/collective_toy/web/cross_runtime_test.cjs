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

async function assertStructuredTAccMatchesExecution(page, label) {
  const comparison = await page.evaluate(() => {
    const model = JSON.parse(document.querySelector("#model").value);
    const scenarioId = document.querySelector("#which").value;
    const scenarioResult = window.lastPackage?.result?.scenario_results?.[scenarioId];
    const demo = window.lastTgcvDemoResult;
    if (!scenarioResult) throw new Error("missing executed scenario result");
    const declared = model.tgcv_mapping;
    const byTransition = new Map();
    // Only the built-in illustrative fixture has an implicit tau_ mapping. Custom
    // models contribute to T_acc only through declared or reviewed-effective mappings.
    if (model.model_id === "toy-diamond-001" && !declared) {
      for (const transition of model.transitions || []) byTransition.set(transition.id, "tau_" + transition.id);
    } else {
      for (const mapping of declared?.mappings || []) byTransition.set(mapping.system_transition_id, mapping.tgcv_transformation_id);
    }
    for (const mapping of window.effectiveCorrespondenceState?.mappings || []) {
      if (mapping.status === "EFFECTIVE" && mapping.active !== false) {
        byTransition.set(mapping.system_transition_id, mapping.tgcv_transformation_id);
      }
    }
    const usedTransitions = new Set();
    for (const trajectory of scenarioResult.trajectories || []) {
      for (const step of trajectory) if (step.transition) usedTransitions.add(step.transition);
    }
    const expected = (model.transitions || [])
      .filter(transition => usedTransitions.has(transition.id) && byTransition.has(transition.id))
      .map(transition => byTransition.get(transition.id)).sort();
    return {
      scenario: scenarioId,
      expected,
      actual: [...(demo?.current?.transformations || [])].sort()
    };
  });
  assert.deepEqual(comparison.actual, comparison.expected,
    label + ": structured operational T_acc must equal the transformations mapped from transitions present in the selected scenario's enumerated trajectories");
}

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
    // Imported/replayed packages must validate and preserve correspondence-review decisions
    // as audit evidence, without applying them to the active TGCV graph or local storage.
    const reviewReplay = await page.evaluate(async pkg => {
      const transition = pkg.input.transitions[0];
      const catalogue = {
        schema:"tgcv-target-catalogue-001", version:"import-replay-contract-v1",
        transformations:[{id:"T_REPLAY_"+transition.id,source_state:transition.source,target_state:transition.target}]
      };
      const derived = await window.deriveTgcvCorrespondenceCandidates(pkg.input, catalogue);
      if (!derived.candidates.length || derived.candidates[0].status !== "PROPOSED") {
        throw new Error("Replay fixture did not produce a unique, reviewable candidate");
      }
      derived.candidates[0].decision = "ACCEPTED";
      const review = {
        schema:"tgcv-correspondence-review-001",
        source_model_sha256:await window.hash(pkg.input),
        catalogue_version:catalogue.version,
        catalogue_sha256:await window.hash(catalogue),
        candidates:derived.candidates
      };
      const imported = JSON.parse(JSON.stringify(pkg));
      imported.tgcv_correspondence_review = review;
      if (!imported.value_assessment && imported.value_assessment_status === undefined) imported.value_assessment_status = "NOT_ASSESSED";
      delete imported.package_sha256;
      imported.package_sha256 = await window.hash(imported);
      const assessment = await window.assessImportedBrowserPackage(imported);
      const tampered = JSON.parse(JSON.stringify(imported));
      tampered.tgcv_correspondence_review.source_model_sha256 = "0".repeat(64);
      delete tampered.package_sha256;
      tampered.package_sha256 = await window.hash(tampered);
      let tamperRejected = false;
      try { await window.assessImportedBrowserPackage(tampered); } catch (_error) { tamperRejected = true; }
      return {
        status:assessment.status, replay:assessment.replay,
        review:assessment.correspondence_review,
        message:assessment.message,
        snapshotPreserved:JSON.stringify(imported.tgcv_correspondence_review)===JSON.stringify(review),
        tamperRejected
      };
    }, pkg);
    assert.equal(reviewReplay.status, "replay-verified", "package replay must remain verified when a valid review snapshot is attached");
    assert.equal(reviewReplay.replay, true);
    assert.equal(reviewReplay.review.accepted_count, 1, "accepted decision must survive import/replay validation");
    assert.equal(reviewReplay.snapshotPreserved, true, "the imported review snapshot must remain byte-structure equivalent");
    assert.equal(reviewReplay.tamperRejected, true, "review/model linkage tampering must be rejected");
    assert.match(reviewReplay.message, /no se aplican al grafo TGCV/i, "replay must explicitly avoid applying accepted mappings");
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
    assert.doesNotMatch(await page.locator("#graph-note").textContent(), /t_ab/,
      "a TRUE condition must not be reported as blocked in the system graph note");
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
    assert.match(await page.locator("#graph-note").textContent(), /t_ab \(FALSA\)/,
      "a FALSE condition must be identified as blocked, not unevaluated");
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
    assert.match(await page.locator("#graph-note").textContent(), /t_ab \(DESCONOCIDA\)/,
      "an UNKNOWN condition must be distinguished from an unevaluated condition in the system graph note");

    const evaluatedPackageModel = {
      ...conditionalModel,
      scenarios: [{
        id: "baseline", disabled_transitions: [],
        condition_evaluations: { t_ab: { condition: "humidity is low", result: "TRUE" } }
      }]
    };
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(evaluatedPackageModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const stalePackageAssessment = await page.evaluate(async () => {
      const pkg = JSON.parse(JSON.stringify(window.lastPackage));
      pkg.input.transitions.find(t => t.id === "t_ab").condition = "humidity is high";
      pkg.result.input_sha256 = await window.hash(pkg.input, "input");
      const resultPayload = JSON.parse(JSON.stringify(pkg.result));
      delete resultPayload.input_sha256;
      delete resultPayload.result_sha256;
      pkg.result.result_sha256 = await window.hash(resultPayload, "result");
      delete pkg.package_sha256;
      pkg.package_sha256 = await window.hash(pkg, "package");
      try {
        await window.assessImportedBrowserPackage(pkg);
        return {rejected:false, reason:null};
      } catch (error) {
        return {rejected:true, reason:String(error && error.message || error)};
      }
    });
    assert.equal(stalePackageAssessment.rejected, true,
      "browser must reject a hash-consistent package with a stale condition evaluation");
    assert.match(stalePackageAssessment.reason, /evaluación de condición está obsoleta|texto ya cambió/i,
      "browser must identify stale condition evaluation, not merely package hash mismatch");

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

    // Exercise the actual JSON-file input route with both conditional and unconditional
    // transitions: TRUE must enable t_ab, while the unconditional A->C->D path remains available.
    const jsonMixedInputModel = {
      ...conditionalModel,
      scenarios: [{
        id:"baseline", disabled_transitions:[],
        condition_evaluations:{t_ab:{condition:"humidity is low",result:"TRUE"}}
      }]
    };
    await page.locator("#json-file").setInputFiles({
      name:"json-mixed-condition-input.json",
      mimeType:"application/json",
      buffer:Buffer.from(JSON.stringify(jsonMixedInputModel))
    });
    await page.waitForFunction(() => /Archivo cargado y validado: json-mixed-condition-input\.json/i.test(
      document.querySelector("#file-status")?.textContent || ""), null, {timeout:5000});
    await page.locator("#run").click();
    await page.waitForFunction(() => /Ejecución completada/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    const jsonMixedInputPackage = await page.evaluate(() => window.lastPackage);
    assert.ok(jsonMixedInputPackage.result.scenario_results.baseline.reachable_states.includes("B"),
      "JSON file import must preserve a matching TRUE condition evaluation and enable its transition");
    assert.ok(jsonMixedInputPackage.result.scenario_results.baseline.reachable_states.includes("C") &&
      jsonMixedInputPackage.result.scenario_results.baseline.reachable_states.includes("D"),
      "conditional evaluation must not block unrelated unconditional transitions imported from JSON");

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

    // Candidate discovery must not duplicate user-declared correspondences.
    const reviewModel = {
      ...explicitlyMappedModel,
      // An unmapped review fixture must not retain relations whose endpoints
      // belonged to the removed user-declared mappings.
      tgcv_mapping: {...explicitlyMappedModel.tgcv_mapping, mappings: [], relations: []}
    };
    const declaredCandidateCheck = await page.evaluate(async model => window.deriveTgcvCorrespondenceCandidates(model, {
      schema:"tgcv-target-catalogue-001",version:"declared-map-v1",transformations:[
        {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
        {id:"T_CD",source_state:"C",target_state:"D"}
      ]
    }), explicitlyMappedModel);
    assert.equal(declaredCandidateCheck.candidates.length, 0,
      "transitions and TGCV targets already covered by user-declared mappings must not be proposed again");

    // Candidate derivation is deterministic, evidence-bearing, and has no semantic side effects.
    const derivationSnapshot = await page.evaluate(async ({model, catalogue}) => {
      const before = JSON.stringify(model);
      const first = await window.deriveTgcvCorrespondenceCandidates(model, catalogue);
      const second = await window.deriveTgcvCorrespondenceCandidates(model, catalogue);
      return {before, after:JSON.stringify(model), first, second};
    }, {
      model: reviewModel,
      catalogue: {schema:"tgcv-target-catalogue-001",version:"fixture-v1",transformations:[
        {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
        {id:"T_CD",source_state:"C",target_state:"D"}
      ]}
    });
    assert.equal(derivationSnapshot.before, derivationSnapshot.after,
      "candidate derivation must not mutate the source model");
    assert.deepEqual(derivationSnapshot.first, derivationSnapshot.second,
      "candidate derivation must be deterministic for an unchanged model/catalogue");
    assert.equal(derivationSnapshot.first.candidates.length, 2,
      "only exact source/target matches in the declared catalogue should yield candidates");
    assert.ok(derivationSnapshot.first.candidates.every(c => c.status === "PROPOSED" && c.decision === null),
      "exact matches must remain proposals without user acceptance");
    assert.ok(derivationSnapshot.first.candidates.every(c => /^[0-9a-f]{64}$/.test(c.source_model_sha256) && /^tcand-[0-9a-f]{64}$/.test(c.candidate_id)),
      "candidates must be traceable to SHA-256 source and stable candidate IDs");
    const ambiguousCandidates = await page.evaluate(async model => window.deriveTgcvCorrespondenceCandidates(model, {
      schema:"tgcv-target-catalogue-001",version:"ambiguous-v1",transformations:[
        {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
        {id:"T_HUMIDITY_ALT",source_state:"A",target_state:"B"}
      ]
    }), reviewModel);
    assert.ok(ambiguousCandidates.candidates.length === 2 && ambiguousCandidates.candidates.every(c => c.status === "NEEDS_REVIEW"),
      "multiple exact targets for one transition must require review, never auto-accept");
    const noMatchCandidates = await page.evaluate(async model => window.deriveTgcvCorrespondenceCandidates(model, {
      schema:"tgcv-target-catalogue-001",version:"no-match-v1",transformations:[
        {id:"T_UNRELATED",source_state:"X",target_state:"Y"}
      ]
    }), reviewModel);
    assert.equal(noMatchCandidates.candidates.length, 0,
      "missing catalogue evidence must not invent correspondence candidates");

    // Effective materialization requires an accepted, exact-scope proposal; it is idempotent,
    // rejects conflicts with user-declared mappings, and never mutates the source model.
    const materialization = await page.evaluate(async model => {
      const unMapped = {...model, tgcv_mapping:{
        schema:"tgcv-explicit-mapping-001", mapping_rule:"user-declared-map-v1",
        provenance:"user-declared", mappings:[], relations:[]
      }};
      const catalogue = {schema:"tgcv-target-catalogue-001",version:"materialize-v1",
        transformations:[{id:"T_DERIVED_AB",source_state:"A",target_state:"B"}]};
      const before = JSON.stringify(unMapped);
      const derived = await window.deriveTgcvCorrespondenceCandidates(unMapped,catalogue);
      derived.candidates[0].decision = "ACCEPTED";
      const first = await window.validateAcceptedCorrespondenceCandidates(unMapped,catalogue,derived.candidates,[]);
      const second = await window.validateAcceptedCorrespondenceCandidates(unMapped,catalogue,derived.candidates,first.mappings);
      const conflictingModel = {...unMapped,tgcv_mapping:{
        schema:"tgcv-explicit-mapping-001",mapping_rule:"user-declared-map-v1",provenance:"user-declared",
        mappings:[{system_transition_id:"t_ab",tgcv_transformation_id:"T_DERIVED_AB"}],relations:[]
      }};
      // Simulate a proposal reviewed against the unmapped model, then introduce a
      // conflicting user-declared mapping before application; validation must reject it.
      const conflictCandidate = await window.deriveTgcvCorrespondenceCandidates(unMapped,catalogue);
      conflictCandidate.candidates[0].decision = "ACCEPTED";
      // Keep the candidate's exact evidence but bind it to the edited source snapshot so
      // this assertion reaches the declared-mapping conflict guard rather than failing
      // earlier at the source-hash freshness guard.
      conflictCandidate.candidates[0].source_model_sha256 = await hash(conflictingModel,"correspondence_source_model");
      const conflictingModelBefore = JSON.stringify(conflictingModel);
      const conflict = await window.validateAcceptedCorrespondenceCandidates(conflictingModel,catalogue,conflictCandidate.candidates,[]);
      const conflictingModelAfter = JSON.stringify(conflictingModel);
      const staleModel = {...unMapped,model_id:"changed-after-review"};
      const stale = await window.validateAcceptedCorrespondenceCandidates(staleModel,catalogue,derived.candidates,[]);
      return {before,after:JSON.stringify(unMapped),first,second,conflict,stale,conflictingModelBefore,conflictingModelAfter};
    }, explicitlyMappedModel);
    assert.equal(materialization.before, materialization.after, "materialization must not rewrite the input model");
    assert.equal(materialization.first.mappings.length, 1, "one accepted exact match should materialize as effective");
    assert.equal(materialization.first.mappings[0].status, "EFFECTIVE");
    assert.equal(materialization.first.mappings[0].provenance, "derived-and-accepted");
    assert.equal(materialization.second.mappings[0].mapping_id, materialization.first.mappings[0].mapping_id,
      "applying the same accepted candidate twice must be idempotent");
    assert.equal(materialization.conflict.mappings.length, 0, "declared mapping conflicts must never be overwritten");
    assert.equal(materialization.conflict.conflicts[0].code, "CONFLICT_NEEDS_REVIEW");
    assert.match(materialization.conflict.conflicts[0].message, /correspondencia declarada por el usuario/i,
      "the conflict report must explain that the user-declared mapping is the reason for abstention");
    assert.equal(materialization.conflictingModelBefore, materialization.conflictingModelAfter,
      "conflict validation must preserve the exact declared mapping and its provenance");
    const effectiveConflict = await page.evaluate(async () => {
      const model = {model_id:"effective-collision-test",states:[{id:"A"},{id:"B"},{id:"C"}],
        transitions:[{id:"t_ab",source:"A",target:"B"},{id:"t_ac",source:"A",target:"C"}],
        tgcv_mapping:{schema:"tgcv-explicit-mapping-001",mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",mappings:[],relations:[]}};
      const conflictCatalogue = {schema:"tgcv-target-catalogue-001",version:"effective-conflict-v1",transformations:[
        {id:"T_DERIVED_AB",source_state:"A",target_state:"B"},
        {id:"T_DERIVED_AC",source_state:"A",target_state:"C"}
      ]};
      const proposals = await window.deriveTgcvCorrespondenceCandidates(model,conflictCatalogue);
      const candidate = proposals.candidates.find(x => x.system_transition_id === "t_ac" && x.tgcv_transformation_id === "T_DERIVED_AC");
      if (!candidate) throw new Error("fixture must derive the intended candidate before testing the collision");
      candidate.decision = "ACCEPTED";
      const prior = [{candidate_id:"cand-prior-effective",status:"EFFECTIVE",
        system_transition_id:"t_ab",tgcv_transformation_id:"T_DERIVED_AC"}];
      return {candidate, result:await window.validateAcceptedCorrespondenceCandidates(model,conflictCatalogue,[candidate],prior)};
    });
    assert.equal(effectiveConflict.result.mappings.length, 0,
      "a candidate reusing a transformation already assigned by another effective mapping must not materialize");
    assert.equal(effectiveConflict.result.conflicts[0].code, "CONFLICT_NEEDS_REVIEW",
      "an effective-to-effective target collision must require explicit review");
    assert.match(effectiveConflict.result.conflicts[0].message, /otra correspondencia derivada efectiva/i,
      "the conflict must identify the already-effective mapping as the reason for abstention");

    // Two distinct source transitions can have the same exact boundary and compete
    // for one target transformation. The batch must abstain symmetrically rather
    // than materializing whichever candidate happens to appear first.
    const sameBatchConflict = await page.evaluate(async () => {
      const model = {model_id:"same-batch-collision",states:[{id:"A"},{id:"B"}],
        transitions:[
          {id:"t_ab_first",source:"A",target:"B"},
          {id:"t_ab_second",source:"A",target:"B"}
        ],
        tgcv_mapping:{schema:"tgcv-explicit-mapping-001",mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",mappings:[],relations:[]}};
      const catalogue = {schema:"tgcv-target-catalogue-001",version:"same-batch-conflict-v1",
        transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]};
      const derived = await window.deriveTgcvCorrespondenceCandidates(model,catalogue);
      if (derived.candidates.length !== 2) throw new Error("fixture must produce two exact candidates competing for one transformation");
      const accepted = derived.candidates.map(candidate => ({...candidate,decision:"ACCEPTED"}));
      const forward = await window.validateAcceptedCorrespondenceCandidates(model,catalogue,accepted,[]);
      const reverse = await window.validateAcceptedCorrespondenceCandidates(model,catalogue,[...accepted].reverse(),[]);
      return {forward,reverse};
    });
    for (const [direction,result] of Object.entries({forward:sameBatchConflict.forward,reverse:sameBatchConflict.reverse})) {
      assert.equal(result.mappings.length, 0,
        direction + " batch order must not arbitrarily activate one of two conflicting accepted mappings");
      assert.equal(result.conflicts.length, 2,
        direction + " batch order must mark both competing candidates as requiring review");
      assert.ok(result.conflicts.every(conflict => conflict.code === "CONFLICT_NEEDS_REVIEW" &&
        /misma operación/i.test(conflict.message)),
        direction + " batch conflicts must carry the expected review code and reason");
    }
    assert.deepEqual(
      sameBatchConflict.forward.conflicts.map(x => x.candidate_id).sort(),
      sameBatchConflict.reverse.conflicts.map(x => x.candidate_id).sort(),
      "conflict detection must be independent of accepted-candidate order");

    // Complementary same-batch conflict: one source transition has two exact
    // target candidates. Both must require review regardless of candidate order.
    const sameSourceConflict = await page.evaluate(async () => {
      const model = {model_id:"same-source-collision",states:[{id:"A"},{id:"B"}],
        transitions:[{id:"t_ab",source:"A",target:"B"}],
        tgcv_mapping:{schema:"tgcv-explicit-mapping-001",mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",mappings:[],relations:[]}};
      const catalogue = {schema:"tgcv-target-catalogue-001",version:"same-source-conflict-v1",
        transformations:[
          {id:"T_AB_PRIMARY",source_state:"A",target_state:"B"},
          {id:"T_AB_ALTERNATE",source_state:"A",target_state:"B"}
        ]};
      const derived = await window.deriveTgcvCorrespondenceCandidates(model,catalogue);
      if (derived.candidates.length !== 2) throw new Error("fixture must produce two exact target candidates for one source transition");
      // Because both targets share the same exact boundary, derivation must
      // classify both as NEEDS_REVIEW. Do not manufacture PROPOSED status to
      // force these ambiguous candidates through the acceptance validator.
      const accepted = derived.candidates.map(candidate => ({...candidate,decision:"ACCEPTED"}));
      const forward = await window.validateAcceptedCorrespondenceCandidates(model,catalogue,accepted,[]);
      const reverse = await window.validateAcceptedCorrespondenceCandidates(model,catalogue,[...accepted].reverse(),[]);
      return {derived,forward,reverse};
    });
    assert.ok(sameSourceConflict.derived.candidates.every(candidate => candidate.status === "NEEDS_REVIEW"),
      "same-source duplicate-boundary targets must be marked NEEDS_REVIEW at derivation");
    for (const [direction,result] of Object.entries({forward:sameSourceConflict.forward,reverse:sameSourceConflict.reverse})) {
      assert.equal(result.mappings.length, 0,
        direction + " ambiguous same-source candidates must not activate a transformation");
      assert.equal(result.conflicts.length, 2,
        direction + " ambiguous same-source candidates must remain blocked for review");
      assert.ok(result.conflicts.every(conflict => conflict.code === "CONFLICT_NEEDS_REVIEW" &&
        /estado PROPOSED/i.test(conflict.message)),
        direction + " ambiguous candidates must be blocked because their status is NEEDS_REVIEW: " + JSON.stringify(result.conflicts));
    }
    assert.deepEqual(
      sameSourceConflict.forward.conflicts.map(x => x.candidate_id).sort(),
      sameSourceConflict.reverse.conflicts.map(x => x.candidate_id).sort(),
      "same-source conflict handling must be independent of candidate order");
    assert.equal(materialization.stale.mappings.length, 0, "a proposal from a changed model must not materialize");
    assert.match(await page.locator("#tgcv-graph").textContent(), /T_CD/,
      "deriving proposals must not modify the currently rendered TGCV graph");

    // The UI must expose explicit correspondence review and persist decisions without applying mappings.
    await page.evaluate(model => {
      document.querySelector("#model").value = JSON.stringify(model, null, 2);
      document.querySelector("#model").dispatchEvent(new Event("input", {bubbles:true}));
      localStorage.clear();
    }, reviewModel);
    const catalogue = page.locator("#tgcv-target-catalogue");
    const catalogueDetails = page.locator("#correspondence-review-section details").filter({has: catalogue});
    if (!(await catalogueDetails.evaluate(el => el.open))) {
      await catalogueDetails.locator("summary").click();
    }
    await catalogue.waitFor({state: "visible"});
    await catalogue.fill(JSON.stringify({
      schema:"tgcv-target-catalogue-001",version:"ui-review-v1",transformations:[
        {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
        {id:"T_CD",source_state:"C",target_state:"D"}
      ]
    }, null, 2));
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "system must execute before correspondence review baseline is captured");
    const reachabilityBeforeReview = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.ok(reachabilityBeforeReview,
      "baseline execution must expose reachable states before review decisions");
    const executionBeforeReview = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.ok(Object.keys(executionBeforeReview).length,
      "baseline execution must expose structured scenario outcomes before review decisions");
    const graphBeforeReview = await page.locator("#tgcv-graph").textContent();
    await page.locator("#derive-tgcv-correspondences").click();
    await page.locator("#correspondence-review-list article").first().waitFor();
    assert.equal(await page.locator("#correspondence-review-list article").count(), 2,
      "review UI must show all exact-boundary candidates");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "deriving pending correspondence proposals must not modify the TGCV graph");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "pending-only correspondence proposals must leave the system executable");
    const executionWithPendingOnly = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.deepEqual(executionWithPendingOnly, executionBeforeReview,
      "pending-only proposals must preserve every scenario reachability and trajectory");
    await assertStructuredTAccMatchesExecution(page, "pending-only review");
    await page.locator("#correspondence-review-list article").nth(0).getByRole("button", {name:"Aceptar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-status").textContent(), /persistida/i,
      "acceptance must report that the decision was persisted");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "accepting a proposal must not activate or rewrite the TGCV graph before explicit application");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "accepted-but-not-applied correspondence must leave the system executable");
    const executionWithAcceptedNotApplied = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.deepEqual(executionWithAcceptedNotApplied, executionBeforeReview,
      "accepted-but-not-applied decisions must preserve every scenario reachability and trajectory");
    await page.locator("#correspondence-review-list article").nth(1).getByRole("button", {name:"Rechazar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
      "a rejected correspondence candidate must retain an explicit human decision");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "rejecting a candidate must not modify the TGCV graph");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "pending and rejected correspondence decisions must leave the system executable");
    const reachabilityAfterPendingAndRejected = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.deepEqual(reachabilityAfterPendingAndRejected, reachabilityBeforeReview,
      "pending and rejected correspondence proposals must not change system reachability");
    const executionAfterPendingAndRejected = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.deepEqual(executionAfterPendingAndRejected, executionBeforeReview,
      "pending and rejected correspondence proposals must preserve all scenario reachability and trajectories");
    await assertStructuredTAccMatchesExecution(page, "pending plus rejected review");
    const effectiveSetAfterPendingAndRejected = await page.evaluate(() =>
      (window.effectiveCorrespondenceState?.mappings || [])
        .filter(mapping => mapping.status === "EFFECTIVE")
        .map(mapping => mapping.tgcv_transformation_id).sort());
    assert.ok(!effectiveSetAfterPendingAndRejected.includes("T_HUMIDITY"),
      "accepted-but-not-applied and rejected proposals must not enter the structured effective correspondence set");
    const persistedReview = await page.evaluate(() => Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:")).map(k => JSON.parse(localStorage.getItem(k))));
    assert.equal(persistedReview.length, 1, "review decision must be persisted in browser storage");
    assert.equal(Object.values(persistedReview[0].decisions)[0].decision, "ACCEPTED",
      "accepted decision must be retrievable with its model/catalogue scope");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "accepting a candidate must not apply it to the TGCV graph automatically");
    await page.locator("#derive-tgcv-correspondences").click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: ACCEPTED/,
      "a persisted decision must be restored when regenerating candidates for the same model/catalogue");

    // Explicit application is a separate user action: it materializes the accepted
    // correspondence without writing the derived mapping back into the source model.
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "review fixture must execute before checking effective graph synchronization");
    const resultBeforeExplicitApplication = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.ok(resultBeforeExplicitApplication,
      "baseline execution must expose reachable states before applying accepted correspondence");
    await page.locator("#derive-tgcv-correspondences").click();
    await page.waitForFunction(() => /Decisión: ACCEPTED/.test(
      document.querySelector("#correspondence-review-list")?.textContent || ""), null, {timeout:5000});
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "accepted-but-not-applied correspondence must leave the system executable");
    const resultAfterReviewBeforeApplication = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.deepEqual(resultAfterReviewBeforeApplication, resultBeforeExplicitApplication,
      "deriving/restoring an accepted decision must not change system reachability before explicit application");
    await page.locator("#apply-accepted-tgcv-correspondences").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#effective-correspondence-status")?.textContent || "";
      return /Correspondencias efectivas activas:|No se aplicaron correspondencias:/i.test(status);
    }, null, {timeout:5000});
    assert.match(await page.locator("#effective-correspondence-status").textContent(),
      /Correspondencias efectivas activas: 1/i,
      "explicit application must activate exactly one accepted mapping; status: " +
        await page.locator("#effective-correspondence-status").textContent());
    const effectiveRecordAfterFirstApply = await page.evaluate(() => Object.keys(localStorage)
      .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
      .map(k => JSON.parse(localStorage.getItem(k))).find(record => (record.mappings || []).some(m => m.status === "EFFECTIVE")));
    const firstEffectiveMapping = effectiveRecordAfterFirstApply.mappings.find(m => m.status === "EFFECTIVE");
    assert.deepEqual(firstEffectiveMapping.decision_provenance && firstEffectiveMapping.decision_provenance.action, "ACCEPTED",
      "effective mapping must retain the explicit acceptance action provenance");
    assert.equal(firstEffectiveMapping.decision_provenance.actor, "local-user",
      "effective mapping must identify the local user action without inventing an account identity");
    assert.ok(firstEffectiveMapping.decision_provenance.decided_at,
      "effective mapping must retain the persisted decision timestamp");
    assert.equal(firstEffectiveMapping.decision_provenance.source, "tgcv-correspondence-review-001");
    await page.locator("#apply-accepted-tgcv-correspondences").click();
    await page.waitForFunction(() => /Correspondencias efectivas activas: 1/i.test(
      document.querySelector("#effective-correspondence-status")?.textContent || ""), null, {timeout:5000});
    const effectiveRecordAfterSecondApply = await page.evaluate(() => Object.keys(localStorage)
      .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
      .map(k => JSON.parse(localStorage.getItem(k))).find(record => (record.mappings || []).some(m => m.status === "EFFECTIVE")));
    assert.equal(effectiveRecordAfterSecondApply.mappings.filter(m => m.status === "EFFECTIVE").length, 1,
      "reapplying the same accepted candidate through the UI must not duplicate active mappings");
    assert.equal(effectiveRecordAfterSecondApply.mappings.find(m => m.status === "EFFECTIVE").mapping_id, firstEffectiveMapping.mapping_id,
      "reapplying must preserve the existing effective mapping identity");
    assert.match(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "explicitly applied accepted correspondence must be reflected in the TGCV graph");
    const modelAfterApplication = JSON.parse(await page.locator("#model").inputValue());
    assert.equal((modelAfterApplication.tgcv_mapping?.mappings || []).length, 0,
      "effective derived mappings must remain separate from the original model mapping declaration");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "system must execute with the explicitly applied effective mapping before testing staleness");
    const reachabilityWithEffectiveMapping = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.ok(reachabilityWithEffectiveMapping,
      "baseline execution must expose reachable states while the accepted mapping is effective");
    const executionSemanticsWithEffectiveMapping = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.ok(Object.keys(executionSemanticsWithEffectiveMapping).length,
      "execution result comparison must include scenario reachability and trajectories");
    await assertStructuredTAccMatchesExecution(page, "effective mapping active");
    const displayedTAccWithEffectiveMapping = await page.locator("#tgcv-demo-results").textContent();
    const structuredTAccWithEffectiveMapping = await page.evaluate(() => {
      const mappings = window.effectiveCorrespondenceState?.mappings || [];
      return mappings.filter(mapping => mapping.status === "EFFECTIVE").map(mapping => ({
        transition: mapping.system_transition_id,
        transformation: mapping.tgcv_transformation_id,
        sourceModel: mapping.source_model_sha256,
        catalogueVersion: mapping.catalogue_version,
        catalogueHash: mapping.catalogue_sha256
      })).sort((a, b) => a.transformation.localeCompare(b.transformation));
    });
    assert.ok(structuredTAccWithEffectiveMapping.some(mapping => mapping.transformation === "T_HUMIDITY"),
      "structured effective correspondence set must include T_HUMIDITY before invalidation");

    const originalCatalogue = JSON.parse(await page.locator("#tgcv-target-catalogue").inputValue());
    originalCatalogue.transformations.push({id:"T_EXTRA",source_state:"E",target_state:"F"});
    await page.locator("#tgcv-target-catalogue").fill(JSON.stringify(originalCatalogue, null, 2));
    await page.locator("#derive-tgcv-correspondences").click();
    await page.waitForFunction(() => /catálogo cambió.*histórico/i.test(
      document.querySelector("#correspondence-review-status").textContent), null, {timeout:5000});
    assert.match(await page.locator("#correspondence-review-status").textContent(), /catálogo cambió.*histórico/i,
      "catalogue content changes must explicitly invalidate prior review decisions");
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: PENDIENTE/,
      "a decision from a different catalogue content hash must not be reused, even if the version label is unchanged");
    const scopedReviewKeys = await page.evaluate(() => Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:")));
    assert.equal(scopedReviewKeys.length, 1,
      "the prior decision must remain archived under its original model/catalogue content scope");
    const effectiveHistoryAfterInvalidation = await page.evaluate(() => Object.keys(localStorage)
      .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
      .map(k => JSON.parse(localStorage.getItem(k)))
      .flatMap(record => [...(record.mappings || []), ...(record.history || [])]));
    assert.ok(effectiveHistoryAfterInvalidation.some(m => m.status === "STALE" && m.stale_reason),
      "catalogue changes must mark previously effective mappings stale while preserving their history");

    // Restoring an old catalogue hash must not silently reactivate the stale mapping or its old ACCEPTED decision.
    await page.locator("#tgcv-target-catalogue").fill(JSON.stringify({
      schema:"tgcv-target-catalogue-001",version:"ui-review-v1",transformations:[
        {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
        {id:"T_CD",source_state:"C",target_state:"D"}
      ]
    }, null, 2));
    await page.locator("#derive-tgcv-correspondences").click();
    await page.waitForFunction(() => /Generadas 2 propuestas/i.test(
      document.querySelector("#correspondence-review-status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: PENDIENTE/,
      "restoring a previous catalogue must not replay an ACCEPTED decision invalidated by an intervening scope change");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "model must execute after restoring catalogue scope");
    const reachabilityAfterStaleMapping = await page.evaluate(() => {
      const result = window.lastPackage?.result?.scenario_results?.baseline;
      return result ? [...(result.reachable_states || [])].sort() : null;
    });
    assert.deepEqual(reachabilityAfterStaleMapping, reachabilityWithEffectiveMapping,
      "invalidating a correspondence and restoring the catalogue must not change system reachability");
    const executionSemanticsAfterStaleMapping = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.deepEqual(executionSemanticsAfterStaleMapping, executionSemanticsWithEffectiveMapping,
      "invalidating a stale correspondence and restoring the catalogue must preserve execution reachability and trajectories");
    await assertStructuredTAccMatchesExecution(page, "effective mapping stale after catalogue change");
    const displayedTAccAfterStaleMapping = await page.locator("#tgcv-demo-results").textContent();
    assert.doesNotMatch(displayedTAccAfterStaleMapping, /T_HUMIDITY/,
      "T_acc display must exclude the transformation supplied only by the now-stale effective mapping");
    const structuredTAccAfterStaleMapping = await page.evaluate(() => {
      const mappings = window.effectiveCorrespondenceState?.mappings || [];
      return mappings.filter(mapping => mapping.status === "EFFECTIVE").map(mapping => ({
        transition: mapping.system_transition_id,
        transformation: mapping.tgcv_transformation_id,
        sourceModel: mapping.source_model_sha256,
        catalogueVersion: mapping.catalogue_version,
        catalogueHash: mapping.catalogue_sha256
      })).sort((a, b) => a.transformation.localeCompare(b.transformation));
    });
    assert.ok(!structuredTAccAfterStaleMapping.some(mapping => mapping.transformation === "T_HUMIDITY"),
      "structured effective correspondence set must exclude T_HUMIDITY after invalidation");
    assert.match(displayedTAccWithEffectiveMapping, /T_HUMIDITY/,
      "baseline T_acc display must include the transformation while its effective mapping is active");
    assert.doesNotMatch(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "a stale effective mapping must remain inactive when the old catalogue is restored");

    // Re-accept only after the catalogue rollback has been explicitly reviewed, then
    // prove that a source-model content change invalidates the newly effective mapping.
    await page.locator("#derive-tgcv-correspondences").click();
    await page.locator("#correspondence-review-list article").first().getByRole("button", {name:"Aceptar propuesta"}).click();
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "model must execute before reapplying after explicit review");
    await page.locator("#derive-tgcv-correspondences").click();
    await page.locator("#apply-accepted-tgcv-correspondences").click();
    await page.waitForFunction(() => /Correspondencias efectivas activas: 1/i.test(
      document.querySelector("#effective-correspondence-status")?.textContent || ""), null, {timeout:5000});
    // Preserve the exact reviewed source model so we can test rollback after invalidation.
    const reviewedSourceModelBeforeChange = JSON.parse(await page.locator("#model").inputValue());
    // Change the source model through its supported visual editor; the JSON textarea
    // is intentionally inside a collapsed advanced-details panel.
    await page.locator("#new-state-id").fill("StateForInvalidationCheck");
    await page.locator("#new-state-add").click();
    await page.waitForFunction(() => /Estado añadido: StateForInvalidationCheck/i.test(
      document.querySelector("#graph-edit-status")?.textContent || ""), null, {timeout:5000});
    await page.locator("#derive-tgcv-correspondences").click();
    // The derive handler is async. Do not accept the previous catalogue-change status as
    // evidence that the model-change invalidation has completed; wait for the persisted event.
    try {
      await page.waitForFunction(() => Object.keys(localStorage)
        .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
        .some(k => {
          try {
            const record = JSON.parse(localStorage.getItem(k));
            return [...(record.mappings || []), ...(record.history || [])]
              .some(m => m.status === "STALE" && /modelo de origen cambió/i.test(m.stale_reason || ""));
          } catch (_e) { return false; }
        }), null, {timeout:5000});
    } catch (error) {
      const diagnostic = await page.evaluate(() => ({
        model: (() => { try { return JSON.parse(document.querySelector("#model").value); } catch (e) { return {parseError: String(e)}; } })(),
        reviewStatus: document.querySelector("#correspondence-review-status")?.textContent,
        effectiveStatus: document.querySelector("#effective-correspondence-status")?.textContent,
        editStatus: document.querySelector("#graph-edit-status")?.textContent,
        records: Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:")).map(k => ({key:k,record:JSON.parse(localStorage.getItem(k))})),
      }));
      throw new Error("No apareció la invalidación por cambio de modelo. Diagnóstico: " + JSON.stringify(diagnostic) + "; espera: " + error.message);
    }
    const effectiveHistoryAfterModelChange = await page.evaluate(() => Object.keys(localStorage)
      .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
      .map(k => JSON.parse(localStorage.getItem(k)))
      .flatMap(record => [...(record.mappings || []), ...(record.history || [])]));
    assert.ok(effectiveHistoryAfterModelChange.some(m => m.status === "STALE" && /modelo de origen cambió/i.test(m.stale_reason || "")),
      "source model content changes must invalidate active mappings while preserving a reasoned history; observed records: " + JSON.stringify(effectiveHistoryAfterModelChange));
    assert.ok(effectiveHistoryAfterModelChange.some(m => m.status === "STALE" && /catálogo cambió/i.test(m.stale_reason || "")),
      "history must preserve the earlier catalogue invalidation as well as the later model invalidation");
    const effectiveScopesAfterModelChange = await page.evaluate(() => Object.keys(localStorage)
      .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
      .map(k => JSON.parse(localStorage.getItem(k))));
    assert.ok(effectiveScopesAfterModelChange.every(record => !(record.mappings || []).some(m => m.status === "EFFECTIVE" && m.active !== false)),
      "no stale effective mapping may remain active after source-model content changes");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "edited source model must still execute after effective mapping invalidation");
    const executionSemanticsAfterSourceModelChange = await page.evaluate(() => {
      const scenarios = window.lastPackage?.result?.scenario_results || {};
      return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
        reachable_states: [...(result.reachable_states || [])].sort(),
        trajectories: (result.trajectories || []).map(path => path.map(step => ({
          state: step.state, transition: step.transition || null
        })))
      }]));
    });
    assert.deepEqual(executionSemanticsAfterSourceModelChange, executionSemanticsWithEffectiveMapping,
      "a source-model inventory edit must not alter execution reachability or trajectories when the transition set is unchanged");
    await assertStructuredTAccMatchesExecution(page, "effective mapping stale after source-model change");
    const structuredTAccAfterSourceModelChange = await page.evaluate(() =>
      (window.effectiveCorrespondenceState?.mappings || [])
        .filter(mapping => mapping.status === "EFFECTIVE" && mapping.active !== false)
        .map(mapping => mapping.tgcv_transformation_id).sort());
    assert.ok(!structuredTAccAfterSourceModelChange.includes("T_HUMIDITY"),
      "structured effective mappings and operational T_acc must exclude the mapping invalidated by a source-model change");
    assert.doesNotMatch(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "a mapping invalidated by a source model change must not remain active in the TGCV graph");

    // A previously accepted correspondence review is scoped to the original model.
    // Exporting the changed model must not attach that now-stale human decision.
    const changedModelExportPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const changedModelExport = await changedModelExportPromise;
    const changedModelExportPath = await changedModelExport.path();
    assert.ok(changedModelExportPath, "changed source model must export a package for scope validation");
    const changedModelPackage = JSON.parse(fs.readFileSync(changedModelExportPath, "utf8"));
    const changedModelReview = changedModelPackage.tgcv_correspondence_review;
    assert.ok(changedModelReview,
      "the current model's newly derived correspondence proposals may be exported with their provenance");
    assert.ok(changedModelReview.candidates.every(candidate =>
      candidate.source_model_sha256 === changedModelReview.source_model_sha256 &&
      candidate.decision !== "ACCEPTED" && candidate.status !== "ACCEPTED"),
      "export must not carry ACCEPTED decisions from the prior source model; only current-scope pending proposals are allowed");

    // Rolling back the source model must not resurrect the prior ACCEPTED decision
    // after that decision's effective mapping was invalidated by the intervening edit.
    await page.locator("#model").evaluate((el, value) => {
      el.value = JSON.stringify(value, null, 2);
      el.dispatchEvent(new Event("input", {bubbles:true}));
    }, reviewedSourceModelBeforeChange);
    await page.locator("#derive-tgcv-correspondences").click();
    await page.waitForFunction(() => /Generadas 2 propuestas/i.test(
      document.querySelector("#correspondence-review-status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: PENDIENTE/,
      "restoring the exact prior source model must not silently restore an ACCEPTED decision invalidated by an intervening model change");
    assert.doesNotMatch(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "restoring the prior source model must not reactivate the stale effective mapping without a new explicit acceptance");

    // Isolated source-model invalidation regression: fresh browser context, no prior
    // catalogue/review decisions, and a correspondence materialized only through the UI.
    const staleContext = await browser.newContext();
    try {
      const stalePage = await staleContext.newPage();
      await stalePage.goto("file://" + htmlPath);
      await stalePage.locator("#load").click();
      await stalePage.evaluate(model => {
        localStorage.clear();
        const el = document.querySelector("#model");
        el.value = JSON.stringify(model, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const staleCatalogue = stalePage.locator("#tgcv-target-catalogue");
      const staleCatalogueDetails = stalePage.locator("#correspondence-review-section details").filter({has:staleCatalogue});
      if (!(await staleCatalogueDetails.evaluate(el => el.open))) {
        await staleCatalogueDetails.locator("summary").click();
      }
      await staleCatalogue.fill(JSON.stringify({
        schema:"tgcv-target-catalogue-001",version:"isolated-model-stale-v1",
        transformations:[
          {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
          {id:"T_CD",source_state:"C",target_state:"D"}
        ]
      }, null, 2));
      await stalePage.locator("#run").click();
      await stalePage.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      assert.match(await stalePage.locator("#status").textContent(), /ejecución completada/i,
        "isolated stale fixture baseline must execute successfully");
      await stalePage.locator("#derive-tgcv-correspondences").click();
      await stalePage.locator("#correspondence-review-list article").first().waitFor();
      await stalePage.locator("#correspondence-review-list article").first()
        .getByRole("button", {name:"Aceptar propuesta"}).click();
      await stalePage.locator("#apply-accepted-tgcv-correspondences").click();
      await stalePage.waitForFunction(() => /Correspondencias efectivas activas: 1/i.test(
        document.querySelector("#effective-correspondence-status")?.textContent || ""), null, {timeout:5000});
      const effectiveBeforeSourceEdit = await stalePage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false));
      assert.equal(effectiveBeforeSourceEdit.length, 1,
        "isolated stale fixture must materialize one active correspondence through the supported UI flow");
      await stalePage.locator("#new-state-id").fill("IsolatedSourceEdit");
      await stalePage.locator("#new-state-add").click();
      await stalePage.waitForFunction(() => /Estado añadido: IsolatedSourceEdit/i.test(
        document.querySelector("#graph-edit-status")?.textContent || ""), null, {timeout:5000});
      await stalePage.locator("#derive-tgcv-correspondences").click();
      await stalePage.waitForFunction(() => Object.keys(localStorage)
        .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
        .some(k => {
          try {
            const record = JSON.parse(localStorage.getItem(k));
            return [...(record.mappings || []), ...(record.history || [])]
              .some(m => m.status === "STALE" && /modelo de origen cambió/i.test(m.stale_reason || ""));
          } catch (_e) { return false; }
        }), null, {timeout:5000});
      const isolatedStaleHistory = await stalePage.evaluate(() => Object.keys(localStorage)
        .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
        .map(k => JSON.parse(localStorage.getItem(k)))
        .flatMap(record => [...(record.mappings || []), ...(record.history || [])]));
      assert.ok(isolatedStaleHistory.some(m => m.status === "STALE" && /modelo de origen cambió/i.test(m.stale_reason || "")),
        "source model edit must invalidate the applied mapping with a persisted reason");
      const currentIsolatedMappings = await stalePage.evaluate(() => Object.keys(localStorage)
        .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
        .map(k => JSON.parse(localStorage.getItem(k)))
        .flatMap(record => record.mappings || []));
      assert.ok(currentIsolatedMappings.every(m => !(m.status === "EFFECTIVE" && m.active !== false)),
        "no current mapping may remain active and effective after the isolated source model edit");
      assert.ok(currentIsolatedMappings.some(m => m.status === "STALE"),
        "the current mapping set must expose the invalidated mapping as STALE");
      await stalePage.locator("#run").click();
      await stalePage.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      assert.match(await stalePage.locator("#status").textContent(), /ejecución completada/i,
        "edited source model must remain executable after isolated invalidation");
      assert.doesNotMatch(await stalePage.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
        "isolated stale mapping must not remain in the TGCV graph");
      await stalePage.locator("#derive-tgcv-correspondences").click();
      assert.match(await stalePage.locator("#correspondence-review-list").textContent(), /Decisión: PENDIENTE/,
        "regenerated proposals for the edited source model must not resurrect the old accepted decision");
      await stalePage.locator("#correspondence-review-list article").first()
        .getByRole("button", {name:"Rechazar propuesta"}).click();
      assert.match(await stalePage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "a newly derived proposal after source-model invalidation must accept a new explicit rejection");
      await stalePage.locator("#derive-tgcv-correspondences").click();
      assert.match(await stalePage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "the new rejection must persist across regeneration after the prior mapping became stale");
      const postCycleState = await stalePage.evaluate(() => ({
        current: Object.keys(localStorage)
          .filter(k => k.startsWith("tgcv-effective-mappings-001:"))
          .map(k => JSON.parse(localStorage.getItem(k)))
          .flatMap(record => record.mappings || []),
        graph: document.querySelector("#tgcv-graph")?.textContent || ""
      }));
      assert.ok(postCycleState.current.every(m => !(m.status === "EFFECTIVE" && m.active !== false)),
        "the review cycle must not reactivate the old mapping after stale then rejected transitions");
      assert.doesNotMatch(postCycleState.graph, /T_HUMIDITY/,
        "the review cycle must keep the invalidated transformation out of the TGCV graph");
    } finally { await staleContext.close(); }

    // Shared acceptance matrix: all three entry routes must preserve condition metadata,
    // avoid fabricating evaluations, and keep the conditional target unreachable by default.
    const conditionEntryCoverage = [];

    // JSON import must preserve conditional metadata without fabricating an evaluation.
    const jsonConditionalModel = {
      ...model,
      schema_version: "collective-toy-input-002",
      transitions: model.transitions.map(t => t.id === "t_ab" ? {...t, condition:"authorization is valid"} : {...t}),
      scenarios: [{id:"baseline",disabled_transitions:[]}]
    };
    await page.locator("#json-file").setInputFiles({
      name:"conditional-model.json",
      mimeType:"application/json",
      buffer:Buffer.from(JSON.stringify(jsonConditionalModel))
    });
    await page.waitForFunction(() => /Archivo cargado y validado: conditional-model\.json/i.test(
      document.querySelector("#file-status")?.textContent || ""), null, {timeout:5000});
    const jsonImportedConditionalModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(jsonImportedConditionalModel.transitions.find(t => t.id === "t_ab").condition, "authorization is valid",
      "JSON import must preserve conditional text exactly");
    assert.equal(jsonImportedConditionalModel.scenarios[0].condition_evaluations?.t_ab, undefined,
      "JSON import must not invent an evaluation for a condition");
    assert.equal(jsonImportedConditionalModel.schema_version, "collective-toy-input-002",
      "JSON import must preserve the condition-capable schema version");
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada/i.test(document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    const jsonConditionalEntryPackage = await page.evaluate(() => window.lastPackage);
    conditionEntryCoverage.push({
      route:"JSON", condition:jsonImportedConditionalModel.transitions.find(t => t.id === "t_ab").condition,
      evaluation:jsonImportedConditionalModel.scenarios[0].condition_evaluations?.t_ab ?? null,
      targetReachable:jsonConditionalEntryPackage.result.scenario_results.baseline.reachable_states.includes("B")
    });

    // Spanish text transcription must preserve recognized conditions as metadata, not as an evaluation.
    await page.locator("details.relation-editor").filter({hasText:"Transcripción asistida de texto a grafo"}).locator("summary").click();
    await page.locator("#system-description").fill(
      "Si hay autorización, el sistema pasa de espera a acceso autorizado."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Borrador propuesto:/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const transcribedConditionalModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(transcribedConditionalModel.transitions.length, 1,
      "transcriber fixture should yield exactly one explicitly described transition");
    assert.equal(transcribedConditionalModel.transitions[0].condition, "hay autorización",
      "transcriber must preserve the recognized Spanish condition as transition metadata");
    assert.equal(transcribedConditionalModel.schema_version, "collective-toy-input-002",
      "transcribing a condition must use the condition-capable schema version");
    assert.equal(transcribedConditionalModel.scenarios[0].condition_evaluations?.[transcribedConditionalModel.transitions[0].id], undefined,
      "transcriber must not fabricate a condition evaluation");
    assert.match(await page.locator("#transcription-status").textContent(), /revisa el resultado/i,
      "transcribed graph remains a human-reviewable draft");

    // Review a correspondence derived from the transcribed graph and ensure its decision
    // remains bound to this exact source model when exported and replayed.
    const transcriberCatalogue = page.locator("#tgcv-target-catalogue");
    const transcriberCatalogueDetails = page.locator("#correspondence-review-section details").filter({has: transcriberCatalogue});
    if (!(await transcriberCatalogueDetails.evaluate(el => el.open))) {
      await transcriberCatalogueDetails.locator("summary").click();
    }
    await transcriberCatalogue.waitFor({state: "visible"});
    await transcriberCatalogue.fill(JSON.stringify({
      schema:"tgcv-target-catalogue-001",version:"transcriber-review-v1",
      transformations:transcribedConditionalModel.transitions.map(t => ({
        id:"T_TRANSCRIBED_"+t.id,source_state:t.source,target_state:t.target
      }))
    }, null, 2));
    await page.locator("#derive-tgcv-correspondences").click();
    const transcribedCandidateArticle = page.locator("#correspondence-review-list article").filter({hasText: "T_TRANSCRIBED_"}).first();
    await transcribedCandidateArticle.waitFor({state: "visible", timeout: 5000});
    const transcribedCandidate = await transcribedCandidateArticle.textContent();
    assert.match(transcribedCandidate || "", /hay autorización/,
      "correspondence derived from a transcribed model must retain the source transition condition as evidence");
    const transcribedCandidateRecord = await page.evaluate(() => window.correspondenceReviewState?.candidates?.[0] || null);
    assert.ok(transcribedCandidateRecord, "transcribed correspondence candidate must be available for review");
    assert.equal(transcribedCandidateRecord.source_model_sha256, await page.evaluate(model => window.hash(model), transcribedConditionalModel),
      "transcribed candidate provenance must match the exact transcribed source model");
    const declaredMappingBeforeAcceptance = await page.locator("#model").evaluate(el => {
      const parsed = JSON.parse(el.value);
      return JSON.parse(JSON.stringify(parsed.tgcv_mapping || null));
    });
    const effectiveMappingsBeforeAcceptance = await page.evaluate(() =>
      JSON.parse(JSON.stringify(window.effectiveCorrespondenceState?.mappings || [])));
    await transcribedCandidateArticle.getByRole("button", {name:"Aceptar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: ACCEPTED/,
      "human review decision for a transcribed candidate must be explicit");
    const declaredMappingAfterAcceptance = await page.locator("#model").evaluate(el => {
      const parsed = JSON.parse(el.value);
      return JSON.parse(JSON.stringify(parsed.tgcv_mapping || null));
    });
    const effectiveMappingsAfterAcceptance = await page.evaluate(() =>
      JSON.parse(JSON.stringify(window.effectiveCorrespondenceState?.mappings || [])));
    assert.deepEqual(declaredMappingAfterAcceptance, declaredMappingBeforeAcceptance,
      "explicitly accepting a derived proposal must not rewrite the user-declared TGCV mapping");
    assert.deepEqual(effectiveMappingsAfterAcceptance, effectiveMappingsBeforeAcceptance,
      "review acceptance alone must not activate a correspondence before the separate apply action");

    // Applying is a separate, explicit operation: only now should the accepted
    // proposal become effective, while the source model's declared mapping stays intact.
    const expectedEffectiveScope = await page.evaluate(() => ({
      sourceModelSha256: window.correspondenceReviewState?.sourceModelSha256,
      catalogueVersion: window.correspondenceReviewState?.catalogueVersion,
      catalogueSha256: window.correspondenceReviewState?.catalogueSha256
    }));
    assert.ok(expectedEffectiveScope.sourceModelSha256 && expectedEffectiveScope.catalogueSha256,
      "the apply fixture must have an explicit source-model and catalogue scope");
    await page.locator("#apply-accepted-tgcv-correspondences").click();
    // A generic status message may already be present from an earlier application.
    // Wait for this exact scope, the expected mapping, and its durable record instead.
    await page.waitForFunction(scope => {
      const state = window.effectiveCorrespondenceState;
      if (!state ||
          state.sourceModelSha256 !== scope.sourceModelSha256 ||
          state.catalogueVersion !== scope.catalogueVersion ||
          state.catalogueSha256 !== scope.catalogueSha256 ||
          !Array.isArray(state.mappings) ||
          state.mappings.length !== 1 ||
          state.mappings[0].status !== "EFFECTIVE" ||
          state.mappings[0].decision !== "ACCEPTED") return false;
      const key = "tgcv-effective-mappings-001:" + scope.sourceModelSha256 + ":" +
        scope.catalogueVersion + ":" + scope.catalogueSha256;
      try {
        const record = JSON.parse(localStorage.getItem(key) || "null");
        return record &&
          record.source_model_sha256 === scope.sourceModelSha256 &&
          record.catalogue_version === scope.catalogueVersion &&
          record.catalogue_sha256 === scope.catalogueSha256 &&
          Array.isArray(record.mappings) &&
          record.mappings.length === 1 &&
          record.mappings[0].status === "EFFECTIVE" &&
          record.mappings[0].decision === "ACCEPTED";
      } catch (_e) { return false; }
    }, expectedEffectiveScope, {timeout:5000});
    assert.match(await page.locator("#effective-correspondence-status").textContent(), /Correspondencias efectivas activas/i,
      "explicit apply action must report successful activation for a valid accepted proposal");
    const effectiveApplySnapshot = await page.evaluate(scope => {
      const state = JSON.parse(JSON.stringify(window.effectiveCorrespondenceState || {}));
      const key = "tgcv-effective-mappings-001:" + scope.sourceModelSha256 + ":" +
        scope.catalogueVersion + ":" + scope.catalogueSha256;
      return {state, persisted: JSON.parse(localStorage.getItem(key) || "null")};
    }, expectedEffectiveScope);
    const effectiveMappingsAfterApply = effectiveApplySnapshot.state.mappings || [];
    assert.equal(effectiveMappingsAfterApply.length, 1,
      "explicit apply action must activate exactly the accepted correspondence in this isolated fixture; status=" +
      (await page.locator("#effective-correspondence-status").textContent()) +
      "; persisted=" + JSON.stringify(effectiveApplySnapshot.persisted).slice(0,1800) +
      "; review=" + (await page.locator("#correspondence-review-list").textContent()).slice(0,1800));
    assert.equal(effectiveMappingsAfterApply[0].status, "EFFECTIVE",
      "applied correspondence must be explicitly marked EFFECTIVE");
    assert.equal(effectiveMappingsAfterApply[0].decision, "ACCEPTED",
      "applied correspondence must retain its human acceptance decision");
    const declaredMappingAfterApply = await page.locator("#model").evaluate(el => {
      const parsed = JSON.parse(el.value);
      return JSON.parse(JSON.stringify(parsed.tgcv_mapping || null));
    });
    assert.deepEqual(declaredMappingAfterApply, declaredMappingBeforeAcceptance,
      "applying a derived correspondence must not rewrite the user-declared TGCV mapping");

    // Carry the transcribed condition through execution and package replay, not just parsing.
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "transcribed conditional model must execute without requiring a fabricated evaluation");
    const transcribedPackage = await page.evaluate(() => window.lastPackage);
    assert.equal(transcribedPackage.input.transitions[0].condition, "hay autorización",
      "execution package must retain the exact condition produced by the transcriber");
    assert.ok(!transcribedPackage.result.scenario_results.baseline.reachable_states.includes("acceso autorizado"),
      "transcribed condition without an evaluation must not make its target reachable");
    conditionEntryCoverage.push({
      route:"Transcriptor español", condition:transcribedPackage.input.transitions[0].condition,
      evaluation:transcribedPackage.input.scenarios[0].condition_evaluations?.[transcribedPackage.input.transitions[0].id] ?? null,
      targetReachable:transcribedPackage.result.scenario_results.baseline.reachable_states.includes("acceso autorizado")
    });
    const transcribedDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const transcribedDownload = await transcribedDownloadPromise;
    const transcribedPackagePath = await transcribedDownload.path();
    assert.ok(transcribedPackagePath, "transcribed conditional export must produce a JSON package");
    const transcribedPackageText = fs.readFileSync(transcribedPackagePath, "utf8");
    const exportedTranscribedPackage = JSON.parse(transcribedPackageText);
    assert.ok(exportedTranscribedPackage.tgcv_correspondence_review,
      "export must preserve a correspondence review explicitly made for the transcribed source model");
    assert.equal(exportedTranscribedPackage.tgcv_correspondence_review.source_model_sha256,
      await page.evaluate(model => window.hash(model), transcribedConditionalModel),
      "exported correspondence review must retain the transcribed model's exact source hash");
    assert.equal(exportedTranscribedPackage.tgcv_correspondence_review.candidates[0].decision, "ACCEPTED",
      "export must preserve the human decision with its model provenance");
    assert.equal(exportedTranscribedPackage.tgcv_correspondence_review.candidates[0].evidence.condition, "hay autorización",
      "exported decision evidence must preserve the exact condition recognized by the transcriber");
    await page.locator("#package-file").setInputFiles({
      name: "transcribed-conditional-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(transcribedPackageText)
    });
    await page.locator("#assess-package").click();
    await page.waitForFunction(() => ["replay-verified", "rejected", "inspect-only/replay-unavailable"].includes(
      document.querySelector("#package-assessment")?.dataset.state
    ), null, {timeout:5000});
    const transcribedPackageAssessment = await page.locator("#package-assessment").textContent();
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "replay-verified",
      "transcribed conditional package must pass independent replay; validator said: " + transcribedPackageAssessment);

    // A negated transition clause must remain pending and must not become an edge.
    await page.locator("#system-description").fill(
      "El proceso pasa de reposo a ejecución. No pasa de ejecución a resultado."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Frases pendientes de interpretar/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const negationModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(negationModel.transitions.length, 1,
      "a negated unsupported transition must not be added to the graph");
    assert.ok(!negationModel.transitions.some(t => /ejecución/i.test(t.source) && /resultado/i.test(t.target)),
      "negated transition must not be simplified into an affirmative edge");
    assert.match(await page.locator("#transcription-status").textContent(), /No pasa de ejecución a resultado/i,
      "negated phrase must be explicitly reported for clarification");

    // Alternate negation forms must obey the same conservative parsing contract.
    const negatedTransitionPhrases = [
      "No se pasa de ejecución a resultado.",
      "La transición de ejecución a resultado no está permitida."
    ];
    for (const phrase of negatedTransitionPhrases) {
      await page.locator("#system-description").fill(
        "El proceso pasa de reposo a ejecución. " + phrase
      );
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Frases pendientes de interpretar/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const model = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(model.transitions.length, 1,
        "negated wording must not add a transition: " + phrase);
      assert.ok(!model.transitions.some(t => /ejecución/i.test(t.source) && /resultado/i.test(t.target)),
        "negated wording must not be converted to an affirmative edge: " + phrase);
      assert.match(await page.locator("#transcription-status").textContent(),
        /Frases pendientes de interpretar/i,
        "unsupported negation must remain visible for human clarification: " + phrase);
    }

    // Unsupported direction wording must remain pending, never be guessed or reversed.
    await page.locator("#system-description").fill(
      "El proceso pasa de reposo a ejecución. El acceso autorizado precede a la espera."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Borrador propuesto:/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const unsupportedDirectionModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(unsupportedDirectionModel.transitions.length, 1,
      "unsupported direction wording must not add a guessed or reversed transition");
    assert.equal(unsupportedDirectionModel.transitions[0].source, "reposo");
    assert.equal(unsupportedDirectionModel.transitions[0].target, "ejecución");
    assert.match(await page.locator("#transcription-status").textContent(),
      /El acceso autorizado precede a la espera/i,
      "unsupported direction phrase must be explicitly reported for clarification");

    // Negation inside a condition is not the same as negating the transition.
    // Preserve the complete condition as metadata; do not evaluate it or drop "no".
    await page.locator("#system-description").fill(
      "Si no hay autorización, el sistema pasa de espera a acceso autorizado."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Borrador propuesto:/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const negativeConditionModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(negativeConditionModel.transitions.length, 1,
      "a negative condition must preserve the explicit conditional edge");
    assert.equal(negativeConditionModel.transitions[0].source, "espera");
    assert.equal(negativeConditionModel.transitions[0].target, "acceso autorizado");
    assert.equal(negativeConditionModel.transitions[0].condition, "no hay autorización",
      "negation inside condition metadata must not be removed or rewritten");
    assert.equal(negativeConditionModel.scenarios[0].condition_evaluations, undefined,
      "transcription must not invent an evaluation for a negative condition");
    assert.ok(!negativeConditionModel.transitions[0].condition_evaluation,
      "condition metadata must remain separate from evaluation");

    const negativeConditionEngineRun = pythonJson(
      "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
      negativeConditionModel
    );
    assert.ok(!negativeConditionEngineRun.result.scenario_results.baseline.reachable_states.includes("acceso autorizado"),
      "Python engine must block the parsed negative condition until explicitly evaluated");
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(negativeConditionModel));
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const negativeConditionPackage = await page.evaluate(() => window.lastPackage);
    assert.equal(negativeConditionPackage.input.transitions[0].condition, "no hay autorización");
    assert.ok(!negativeConditionPackage.result.scenario_results.baseline.reachable_states.includes("acceso autorizado"),
      "browser execution must block the parsed negative condition until explicitly evaluated");
    assert.deepEqual(
      negativeConditionPackage.result,
      negativeConditionEngineRun.result,
      "browser and Python must agree on the parsed negative condition and its blocked reachability"
    );

    // Explicit evaluations apply to the exact transcribed condition text:
    // TRUE enables the edge; FALSE blocks it. This tests evaluation semantics,
    // not an automatic linguistic inference from the phrase itself.
    const negativeTransitionId = negativeConditionModel.transitions[0].id;
    for (const result of ["TRUE", "FALSE"]) {
      const evaluatedNegativeConditionModel = {
        ...negativeConditionModel,
        scenarios: [{
          ...negativeConditionModel.scenarios[0],
          condition_evaluations: {
            [negativeTransitionId]: {
              condition: "no hay autorización",
              result
            }
          }
        }]
      };
      const expectedNegativeConditionRun = pythonJson(
        "import json,sys; import collective_toy_engine_001 as e; m=json.load(sys.stdin); print(json.dumps(e.export_run(m),sort_keys=True))",
        evaluatedNegativeConditionModel
      );
      await page.locator("#model").evaluate((el, value) => {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
      }, JSON.stringify(evaluatedNegativeConditionModel));
      await page.locator("#run").click();
      await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
      const evaluatedNegativeConditionPackage = await page.evaluate(() => window.lastPackage);
      assert.equal(
        evaluatedNegativeConditionPackage.input.scenarios[0].condition_evaluations[negativeTransitionId].condition,
        "no hay autorización",
        "explicit evaluation must remain bound to the exact transcribed condition"
      );
      assert.equal(
        evaluatedNegativeConditionPackage.result.scenario_results.baseline.reachable_states.includes("acceso autorizado"),
        result === "TRUE",
        result + " evaluation must control reachability for the transcribed negative condition"
      );
      assert.deepEqual(
        evaluatedNegativeConditionPackage.result,
        expectedNegativeConditionRun.result,
        "browser and Python must agree for the transcribed negative condition evaluated as " + result
      );
    }

    // Editing a transcribed condition must reject an evaluation bound to its prior text.
    const staleNegativeConditionId = negativeConditionModel.transitions[0].id;
    const staleTranscribedConditionModel = {
      ...negativeConditionModel,
      transitions: negativeConditionModel.transitions.map(t => ({
        ...t,
        condition: "hay autorización"
      })),
      scenarios: [{
        ...negativeConditionModel.scenarios[0],
        condition_evaluations: {
          [staleNegativeConditionId]: {
            condition: "no hay autorización",
            result: "TRUE"
          }
        }
      }]
    };
    const staleEvaluationValidation = spawnSync(process.env.PYTHON || "python", ["-c", [
      "import json,sys",
      "import collective_toy_engine_001 as e",
      "m=json.load(sys.stdin)",
      "try:",
      " e.export_run(m)",
      " print(json.dumps({'rejected':False}))",
      "except e.ModelValidationError as exc:",
      " print(json.dumps({'rejected':True,'message':str(exc)}))"
    ].join("\n")], {
      cwd: root, input: JSON.stringify(staleTranscribedConditionModel), encoding: "utf8"
    });
    assert.equal(staleEvaluationValidation.status, 0, "stale evaluation validation probe must run");
    const staleEvaluationValidationResult = JSON.parse(staleEvaluationValidation.stdout);
    assert.equal(staleEvaluationValidationResult.rejected, true,
      "Python engine must reject an evaluation bound to the previous condition text");
    assert.match(staleEvaluationValidationResult.message, /does not match the current condition text/,
      "Python engine must identify the stale condition-evaluation binding");
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(staleTranscribedConditionModel));
    await page.locator("#run").click();
    await page.waitForFunction(() =>
      /No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""),
      { timeout: 10000 }
    );
    const staleConditionStatus = await page.locator("#status").innerText();
    assert.match(staleConditionStatus, /obsoleta|ya cambió|no corresponde|no coincide/i,
      "browser must surface rejection of the stale condition evaluation");
    assert.equal(await page.evaluate(() => window.lastPackage), null,
      "rejected stale input must not leave an older execution package exposed as current");

    // Equivalent Spanish formulations must produce the same directed conditional edge.
    const equivalentConditionPhrases = [
      {
        phrase: "Si hay autorización, el sistema pasa de espera a acceso autorizado.",
        label: "leading si clause"
      },
      {
        phrase: "El sistema pasa de espera a acceso autorizado cuando hay autorización.",
        label: "trailing cuando clause"
      },
      {
        phrase: "El sistema pasa de espera a acceso autorizado si hay autorización.",
        label: "trailing si clause"
      },
      {
        phrase: "Cuando hay autorización, el sistema pasa de espera a acceso autorizado.",
        label: "leading cuando clause"
      },
      {
        phrase: "El sistema transita de espera a acceso autorizado si hay autorización.",
        label: "transita verb with trailing si clause"
      },
      {
        phrase: "El sistema cambia de espera a acceso autorizado cuando hay autorización.",
        label: "cambia verb with trailing cuando clause"
      },
      {
        phrase: "La espera conduce a acceso autorizado cuando hay autorización.",
        label: "conduce formulation with trailing cuando clause"
      }
    ];
    const equivalentConditionGraphs = [];
    for (const fixture of equivalentConditionPhrases) {
      await page.locator("#system-description").fill(fixture.phrase);
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Borrador propuesto:/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const parsed = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(parsed.transitions.length, 1, fixture.label + ": expected exactly one edge");
      const edge = parsed.transitions[0];
      assert.equal(edge.source, "espera", fixture.label + ": source state must match");
      assert.equal(edge.target, "acceso autorizado", fixture.label + ": target state and direction must match");
      assert.equal(edge.condition, "hay autorización", fixture.label + ": condition must be preserved exactly");
      assert.equal(parsed.scenarios[0].condition_evaluations?.[edge.id], undefined,
        fixture.label + ": parsing must not invent a condition evaluation");
      equivalentConditionGraphs.push({
        states: parsed.states.map(state => state.id).sort(),
        transitions: parsed.transitions.map(t => ({source:t.source,target:t.target,condition:t.condition})),
        evaluation: parsed.scenarios[0].condition_evaluations?.[edge.id] ?? null
      });
    }
    for (let i = 1; i < equivalentConditionGraphs.length; i++) {
      assert.deepEqual(equivalentConditionGraphs[i], equivalentConditionGraphs[0],
        equivalentConditionPhrases[i].label + " must yield identical graph semantics to the baseline formulation");
    }

    // Semantically different conditions must not be collapsed just because their edge is identical.
    const negativeConditionPhrases = [
      "Si no hay autorización, el sistema pasa de espera a acceso autorizado.",
      "El sistema pasa de espera a acceso autorizado si no hay autorización.",
      "El sistema transita de espera a acceso autorizado si no hay autorización.",
      "La espera conduce a acceso autorizado cuando no hay autorización."
    ];
    const negativeConditionGraphs = [];
    for (const phrase of negativeConditionPhrases) {
      await page.locator("#system-description").fill(phrase);
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Borrador propuesto:/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const parsed = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(parsed.transitions.length, 1, "negative condition formulation must yield one explicit edge: " + phrase);
      const edge = parsed.transitions[0];
      assert.equal(edge.source, "espera", "negative condition must preserve the source state: " + phrase);
      assert.equal(edge.target, "acceso autorizado", "negative condition must preserve the target state: " + phrase);
      assert.equal(edge.condition, "no hay autorización", "negation in condition metadata must be preserved exactly: " + phrase);
      assert.equal(parsed.scenarios[0].condition_evaluations?.[edge.id], undefined,
        "negative condition parsing must not fabricate an evaluation: " + phrase);
      negativeConditionGraphs.push({
        states: parsed.states.map(state => state.id).sort(),
        transitions: parsed.transitions.map(t => ({source:t.source,target:t.target,condition:t.condition})),
        evaluation: parsed.scenarios[0].condition_evaluations?.[edge.id] ?? null
      });
    }
    for (let i = 1; i < negativeConditionGraphs.length; i++) {
      assert.deepEqual(negativeConditionGraphs[i], negativeConditionGraphs[0],
        "negated condition formulation " + (i + 1) + " must yield identical graph semantics to the baseline");
    }
    assert.equal(negativeConditionGraphs[0].transitions[0].condition, "no hay autorización");
    assert.notEqual(negativeConditionGraphs[0].transitions[0].condition,
      equivalentConditionGraphs[0].transitions[0].condition,
      "positive and negative conditions must remain semantically distinguishable even when edge endpoints match");

    // An uncertain condition is ambiguous; it must not be accepted as a normal conditional edge.
    await page.locator("#system-description").fill(
      "Si quizá hay autorización, el sistema pasa de espera a acceso autorizado."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /No se pudo proponer el grafo/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    assert.equal(await page.locator("#model").inputValue(), "",
      "ambiguous condition with no other explicit transition must not produce a graph");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /Si quizá hay autorización/i,
      "ambiguous conditional phrase must remain in the clarification queue");

    // Exception operators in leading and trailing position must remain pending rather than
    // silently becoming ordinary positive conditions.
    const unsupportedExceptionPhrases = [
      "Salvo que haya autorización, el sistema pasa de espera a acceso autorizado.",
      "El sistema pasa de espera a acceso autorizado salvo que haya autorización.",
      "El sistema pasa de espera a acceso autorizado excepto si hay autorización.",
      "El sistema pasa de espera a acceso autorizado a menos que haya autorización.",
      "A no ser que haya autorización, el sistema pasa de espera a acceso autorizado.",
      "El sistema pasa de espera a acceso autorizado excepto en caso de que haya autorización.",
      "El sistema pasa de espera a acceso autorizado salvo en el caso de que haya autorización.",
      "El sistema pasa de espera a acceso autorizado excepto que haya autorización."
    ];
    for (const phrase of unsupportedExceptionPhrases) {
      await page.locator("#system-description").fill(phrase);
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /No se pudo proponer el grafo/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      assert.equal(await page.locator("#model").inputValue(), "",
        "unsupported exception operator must not generate a potentially misinterpreted graph: " + phrase);
      assert.match(await page.locator("#transcription-clarification").inputValue(), /salvo que|excepto si|excepto que|a menos que|a no ser que|excepto cuando|excepto en caso de que|salvo en el caso de que/i,
        "unsupported exception operator must remain pending for human clarification: " + phrase);
    }

    // In a mixed description, preserve a clearly parsed transition but never add the
    // unsupported exception transition; the latter must remain visible for clarification.
    await page.locator("#system-description").fill(
      "El sistema pasa de inicio a espera. El sistema pasa de espera a acceso autorizado salvo que haya autorización."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#transcription-status")?.textContent || "";
      const model = document.querySelector("#model")?.value || "";
      return /grafo/i.test(status) && model.length > 0;
    }, null, {timeout:5000});
    const mixedModel = JSON.parse(await page.locator("#model").inputValue());
    const mixedTransitions = mixedModel.transitions || [];
    assert.equal(mixedTransitions.length, 1,
      "mixed description must retain only the explicitly supported transition");
    assert.match(JSON.stringify(mixedTransitions[0]), /inicio/i,
      "the explicit valid transition must be preserved");
    assert.doesNotMatch(JSON.stringify(mixedTransitions), /acceso autorizado/i,
      "unsupported exception transition must not be added to the graph");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /salvo que haya autorización/i,
      "unsupported exception sentence must remain pending even when another transition is valid");

    // Reverse the sentence order to ensure an unsupported exception sentence does not
    // prevent a later, explicit transition from being parsed.
    await page.locator("#system-description").fill(
      "El sistema pasa de espera a acceso autorizado salvo que haya autorización. El sistema pasa de inicio a espera."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#transcription-status")?.textContent || "";
      const model = document.querySelector("#model")?.value || "";
      return /grafo/i.test(status) && model.length > 0;
    }, null, {timeout:5000});
    const reverseMixedModel = JSON.parse(await page.locator("#model").inputValue());
    const reverseMixedTransitions = reverseMixedModel.transitions || [];
    assert.equal(reverseMixedTransitions.length, 1,
      "reverse-order mixed description must retain only the explicitly supported transition");
    assert.match(JSON.stringify(reverseMixedTransitions[0]), /inicio/i,
      "valid transition after an unsupported exception sentence must still be preserved");
    assert.doesNotMatch(JSON.stringify(reverseMixedTransitions), /acceso autorizado/i,
      "unsupported exception transition must not be added when it precedes a valid sentence");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /salvo que haya autorización/i,
      "unsupported exception sentence must remain pending when it precedes a valid transition");

    // The unsupported "a menos que" operator must also stay pending in a mixed
    // description, without suppressing a separately supported transition.
    await page.locator("#system-description").fill(
      "El sistema pasa de inicio a espera. El sistema pasa de espera a acceso autorizado a menos que haya autorización."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#transcription-status")?.textContent || "";
      const model = document.querySelector("#model")?.value || "";
      return /grafo/i.test(status) && model.length > 0;
    }, null, {timeout:5000});
    const aMenosQueMixedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(aMenosQueMixedModel.transitions.length, 1,
      "'a menos que' must not create an unsupported edge or discard the supported edge");
    assert.match(JSON.stringify(aMenosQueMixedModel.transitions[0]), /inicio/i,
      "the supported transition must survive beside an 'a menos que' sentence");
    assert.doesNotMatch(JSON.stringify(aMenosQueMixedModel.transitions), /acceso autorizado/i,
      "the 'a menos que' transition must not be silently interpreted as a normal conditional edge");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /a menos que haya autorización/i,
      "the unsupported 'a menos que' sentence must remain pending for human clarification");
    assert.equal(Object.keys(aMenosQueMixedModel.scenarios[0].condition_evaluations || {}).length, 0,
      "mixed parsing with 'a menos que' must not fabricate condition evaluations");

    // Complete the mixed-description matrix: each unsupported exception operator
    // must remain pending whether it appears before or after a supported transition.
    const mixedExceptionCases = [
      {operator:"salvo que", sentence:"El sistema pasa de espera a acceso autorizado salvo que haya autorización."},
      {operator:"excepto si", sentence:"El sistema pasa de espera a acceso autorizado excepto si hay autorización."},
      {operator:"excepto que", sentence:"El sistema pasa de espera a acceso autorizado excepto que haya autorización."},
      {operator:"a menos que", sentence:"El sistema pasa de espera a acceso autorizado a menos que haya autorización."},
      {operator:"a no ser que", sentence:"A no ser que haya autorización, el sistema pasa de espera a acceso autorizado."},
      {operator:"excepto cuando", sentence:"El sistema pasa de espera a acceso autorizado excepto cuando haya autorización."},
      {operator:"excepto en caso de que", sentence:"El sistema pasa de espera a acceso autorizado excepto en caso de que haya autorización."},
      {operator:"salvo en el caso de que", sentence:"El sistema pasa de espera a acceso autorizado salvo en el caso de que haya autorización."}
    ];
    for (const {operator, sentence} of mixedExceptionCases) {
      for (const description of [
        "El sistema pasa de inicio a espera. " + sentence,
        sentence + " El sistema pasa de inicio a espera."
      ]) {
        await page.locator("#system-description").fill(description);
        await page.locator("#generate-system-graph").click();
        await page.waitForFunction(() => {
          const status = document.querySelector("#transcription-status")?.textContent || "";
          const model = document.querySelector("#model")?.value || "";
          return /grafo/i.test(status) && model.length > 0;
        }, null, {timeout:5000});
        const exceptionMixedModel = JSON.parse(await page.locator("#model").inputValue());
        assert.equal((exceptionMixedModel.transitions || []).length, 1,
          "mixed description with '" + operator + "' must preserve only the supported transition: " + description);
        assert.match(JSON.stringify(exceptionMixedModel.transitions[0]), /inicio/i,
          "supported transition must survive exception operator '" + operator + "'");
        assert.doesNotMatch(JSON.stringify(exceptionMixedModel.transitions), /acceso autorizado/i,
          "exception operator '" + operator + "' must not create a false transition");
        assert.match(await page.locator("#transcription-clarification").inputValue(),
          /salvo que|excepto si|excepto que|a menos que|a no ser que|excepto cuando|excepto en caso de que|salvo en el caso de que/i,
          "exception operator '" + operator + "' must remain pending in either sentence order");
        assert.equal(Object.keys(exceptionMixedModel.scenarios?.[0]?.condition_evaluations || {}).length, 0,
          "exception operator '" + operator + "' must not fabricate condition evaluations");
      }
    }

    // Mixed positive and negative conditions must remain attached to their own edges,
    // independent of sentence order; parsing records metadata but never evaluates it.
    const mixedConditionDescriptions = [
      "El sistema pasa de inicio a espera si hay autorización. El sistema pasa de espera a acceso autorizado si no hay autorización.",
      "El sistema pasa de espera a acceso autorizado si no hay autorización. El sistema pasa de inicio a espera si hay autorización."
    ];
    const mixedConditionGraphs = [];
    for (const description of mixedConditionDescriptions) {
      await page.locator("#system-description").fill(description);
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Borrador propuesto:/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const parsed = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(parsed.transitions.length, 2,
        "mixed positive/negative description must preserve exactly two explicit transitions");
      const normalized = parsed.transitions.map(edge => ({
        source:edge.source, target:edge.target, condition:edge.condition
      })).sort((a,b) => (a.source+"|"+a.target).localeCompare(b.source+"|"+b.target));
      assert.deepEqual(normalized, [
        {source:"espera",target:"acceso autorizado",condition:"no hay autorización"},
        {source:"inicio",target:"espera",condition:"hay autorización"}
      ], "positive and negative conditions must stay attached to the correct directed edge");
      assert.equal(parsed.scenarios[0].condition_evaluations && Object.keys(parsed.scenarios[0].condition_evaluations).length || 0, 0,
        "mixed conditional parsing must not fabricate evaluations");
      assert.equal(await page.locator("#transcription-clarification").inputValue(), "",
        "fully explicit supported conditional sentences must not be left pending");
      mixedConditionGraphs.push(normalized);
    }
    assert.deepEqual(mixedConditionGraphs[1], mixedConditionGraphs[0],
      "reversing sentence order must not change mixed positive/negative graph semantics");

    // Unsupported exception wording must remain pending without discarding supported
    // positive/negative transitions elsewhere in the same description.
    await page.locator("#system-description").fill(
      "El sistema pasa de inicio a espera si hay autorización. El sistema pasa de espera a acceso autorizado si no hay autorización. El sistema pasa de acceso autorizado a final salvo que haya auditoría."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Borrador propuesto:/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const mixedWithPendingModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(mixedWithPendingModel.transitions.length, 2,
      "supported positive/negative transitions must survive beside an unsupported exception sentence");
    const mixedWithPendingEdges = mixedWithPendingModel.transitions.map(edge => ({
      source:edge.source, target:edge.target, condition:edge.condition
    })).sort((a,b) => (a.source+"|"+a.target).localeCompare(b.source+"|"+b.target));
    assert.deepEqual(mixedWithPendingEdges, [
      {source:"espera",target:"acceso autorizado",condition:"no hay autorización"},
      {source:"inicio",target:"espera",condition:"hay autorización"}
    ], "supported edge directions and condition polarity must be preserved");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /salvo que haya auditoría/i,
      "unsupported exception sentence must remain pending for clarification");
    assert.doesNotMatch(JSON.stringify(mixedWithPendingModel.transitions), /acceso autorizado.*final|final.*acceso autorizado/i,
      "unsupported exception transition must not be inserted into the graph");
    assert.equal(Object.keys(mixedWithPendingModel.scenarios[0].condition_evaluations || {}).length, 0,
      "parsing mixed supported and pending sentences must not fabricate evaluations");

    // The same mixed description must preserve supported transitions when the unsupported
    // exception sentence comes first, not only when it comes last.
    await page.locator("#system-description").fill(
      "El sistema pasa de acceso autorizado a final salvo que haya auditoría. El sistema pasa de espera a acceso autorizado si no hay autorización. El sistema pasa de inicio a espera si hay autorización."
    );
    await page.locator("#generate-system-graph").click();
    await page.waitForFunction(() => /Borrador propuesto:/i.test(
      document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
    const pendingFirstModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(pendingFirstModel.transitions.length, 2,
      "an unsupported exception sentence first must not suppress the two supported transitions");
    const pendingFirstEdges = pendingFirstModel.transitions.map(edge => ({
      source:edge.source, target:edge.target, condition:edge.condition
    })).sort((a,b) => (a.source+"|"+a.target).localeCompare(b.source+"|"+b.target));
    assert.deepEqual(pendingFirstEdges, [
      {source:"espera",target:"acceso autorizado",condition:"no hay autorización"},
      {source:"inicio",target:"espera",condition:"hay autorización"}
    ], "supported directions and positive/negative conditions must survive when the exception sentence comes first");
    assert.match(await page.locator("#transcription-clarification").inputValue(), /salvo que haya auditoría/i,
      "exception sentence at the start must remain pending for clarification");
    assert.doesNotMatch(JSON.stringify(pendingFirstModel.transitions), /acceso autorizado.*final|final.*acceso autorizado/i,
      "unsupported exception sentence at the start must not create an edge");
    assert.equal(Object.keys(pendingFirstModel.scenarios[0].condition_evaluations || {}).length, 0,
      "exception-first mixed parsing must not fabricate condition evaluations");

    // Exception formulations beyond "salvo que"/"excepto si" must not be misread
    // as part of a destination-state label or converted into a traversable edge.
    for (const exceptionPhrase of ["excepto cuando hay auditoría", "a menos que haya auditoría", "excepto en caso de auditoría"]) {
      await page.locator("#system-description").fill(
        "El sistema pasa de inicio a espera si hay autorización. El sistema pasa de acceso autorizado a final " + exceptionPhrase + "."
      );
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Borrador propuesto:/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const exceptionVariantModel = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(exceptionVariantModel.transitions.length, 1,
        "unsupported exception wording must not become a second transition: " + exceptionPhrase);
      assert.deepEqual(exceptionVariantModel.transitions.map(edge => ({
        source:edge.source, target:edge.target, condition:edge.condition
      })), [{source:"inicio",target:"espera",condition:"hay autorización"}],
        "only the explicit supported transition may remain: " + exceptionPhrase);
      assert.ok((await page.locator("#transcription-clarification").inputValue())
        .toLowerCase().includes(exceptionPhrase.toLowerCase()),
        "unsupported exception formulation must remain pending for clarification: " + exceptionPhrase);
      assert.equal(Object.keys(exceptionVariantModel.scenarios[0].condition_evaluations || {}).length, 0,
        "unsupported exception wording must not fabricate condition evaluations: " + exceptionPhrase);
    }

    // Reverse the mixed-order test for each unsupported exception variant: an
    // exception-first sentence must remain pending without suppressing the valid edge.
    for (const exceptionPhrase of ["excepto cuando hay auditoría", "a menos que haya auditoría", "excepto en caso de auditoría"]) {
      await page.locator("#system-description").fill(
        "El sistema pasa de acceso autorizado a final " + exceptionPhrase + ". El sistema pasa de inicio a espera si hay autorización."
      );
      await page.locator("#generate-system-graph").click();
      await page.waitForFunction(() => /Borrador propuesto:/i.test(
        document.querySelector("#transcription-status")?.textContent || ""), null, {timeout:5000});
      const exceptionFirstModel = JSON.parse(await page.locator("#model").inputValue());
      assert.equal(exceptionFirstModel.transitions.length, 1,
        "exception-first wording must not create an unsupported edge or suppress the supported edge: " + exceptionPhrase);
      assert.deepEqual(exceptionFirstModel.transitions.map(edge => ({
        source:edge.source, target:edge.target, condition:edge.condition
      })), [{source:"inicio",target:"espera",condition:"hay autorización"}],
        "the valid transition must survive each exception-first formulation: " + exceptionPhrase);
      assert.ok((await page.locator("#transcription-clarification").inputValue())
        .toLowerCase().includes(exceptionPhrase.toLowerCase()),
        "exception-first formulation must remain pending for clarification: " + exceptionPhrase);
      assert.equal(Object.keys(exceptionFirstModel.scenarios[0].condition_evaluations || {}).length, 0,
        "exception-first wording must not fabricate condition evaluations: " + exceptionPhrase);
    }

    // Restore the stable t_ab fixture after testing transcription, which replaces the current graph.
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", {bubbles:true}));
    }, JSON.stringify(model));
    await page.evaluate(() => syncGraphEditor());
    await page.locator('#transition-review-list input[data-condition-text="t_ab"]').waitFor({timeout:5000});

    // The visual editor must create/edit/clear condition metadata and invalidate old evaluations.
    const visualConditionInput = page.locator('#transition-review-list input[data-condition-text="t_ab"]');
    await visualConditionInput.fill("humidity is extremely low");
    await page.locator('#transition-review-list button[data-save-condition="t_ab"]').click();
    const visuallyEditedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(visuallyEditedModel.schema_version, "collective-toy-input-002",
      "adding/editing a visual condition must upgrade to schema v002");
    assert.equal(visuallyEditedModel.transitions.find(t => t.id === "t_ab").condition, "humidity is extremely low",
      "visual condition editor must persist the condition text");
    assert.equal(visuallyEditedModel.scenarios[0].condition_evaluations?.t_ab, undefined,
      "changing condition text must invalidate the previous scenario evaluation");
    await page.locator("#run").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#status")?.textContent || "";
      return /ejecución completada|no se ha podido ejecutar/i.test(status);
    }, null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "edited conditional model must execute; browser status: " + await page.locator("#status").textContent());
    const visuallyEditedPackage = await page.evaluate(() => window.lastPackage);
    assert.ok(!visuallyEditedPackage.result.scenario_results.baseline.reachable_states.includes("B"),
      "a visually edited condition must remain blocked until re-evaluated");
    conditionEntryCoverage.push({
      route:"Editor visual", condition:visuallyEditedPackage.input.transitions.find(t => t.id === "t_ab").condition,
      evaluation:visuallyEditedPackage.input.scenarios[0].condition_evaluations?.t_ab ?? null,
      targetReachable:visuallyEditedPackage.result.scenario_results.baseline.reachable_states.includes("B")
    });
    assert.match(await page.locator("#graph-note").textContent(), /t_ab \(NO EVALUADA\)/,
      "the graph note must show the edited condition as unevaluated");
    assert.doesNotMatch(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "the old accepted mapping must not make a now-blocked transition accessible after its condition changes");

    // Visual-editor condition must survive its own export/import/replay round trip.
    const visualConditionalDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const visualConditionalDownload = await visualConditionalDownloadPromise;
    const visualConditionalPath = await visualConditionalDownload.path();
    assert.ok(visualConditionalPath, "visual-editor conditional model must export a JSON package");
    const visualConditionalText = fs.readFileSync(visualConditionalPath, "utf8");
    const visualConditionalPackage = JSON.parse(visualConditionalText);
    assert.equal(visualConditionalPackage.input.transitions.find(t => t.id === "t_ab").condition,
      "humidity is extremely low", "visual editor's exact condition must be preserved in the exported source input");
    await page.locator("#package-file").setInputFiles({
      name: "visual-conditional-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(visualConditionalText)
    });
    await page.locator("#assess-package").click();
    await page.waitForFunction(() => ["replay-verified", "rejected", "inspect-only/replay-unavailable"].includes(
      document.querySelector("#package-assessment")?.dataset.state
    ), null, {timeout:5000});
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "replay-verified",
      "visual-editor conditional package must pass independent replay; validator said: " +
      await page.locator("#package-assessment").textContent());

    assert.deepEqual(conditionEntryCoverage.map(({route}) => route),
      ["JSON", "Transcriptor español", "Editor visual"],
      "the grouped condition-entry matrix must exercise all three supported input routes");
    for (const entry of conditionEntryCoverage) {
      assert.ok(typeof entry.condition === "string" && entry.condition.trim(), entry.route + ": condition text must be preserved");
      assert.equal(entry.evaluation, null, entry.route + ": an unevaluated condition must not gain a fabricated evaluation");
      assert.equal(entry.targetReachable, false, entry.route + ": an unevaluated conditional target must remain unreachable");
    }
    console.log("PASS: grouped condition-entry matrix — JSON, Spanish transcriber, visual editor preserve condition text without fabricated evaluation or reachability.");

    // Clearing a condition must remove its metadata and stale evaluation, restoring an unconditional transition.
    await page.locator('#transition-review-list input[data-condition-text="t_ab"]').fill("");
    await page.locator('#transition-review-list button[data-save-condition="t_ab"]').click();
    const visuallyClearedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(visuallyClearedModel.transitions.find(t => t.id === "t_ab").condition, undefined,
      "clearing the visual condition must remove condition metadata");
    assert.equal(visuallyClearedModel.scenarios[0].condition_evaluations?.t_ab, undefined,
      "clearing the condition must also remove its scenario evaluation");
    await page.locator("#run").click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#status")?.textContent || "";
      return /ejecución completada|no se ha podido ejecutar/i.test(status);
    }, null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "cleared conditional model must execute; browser status: " + await page.locator("#status").textContent());
    const visuallyClearedPackage = await page.evaluate(() => window.lastPackage);
    assert.ok(visuallyClearedPackage.result.scenario_results.baseline.reachable_states.includes("B"),
      "a cleared condition must behave as an unconditional transition");
    // Export/import/replay must preserve the conditional source model and verify the package independently.
    const roundTripModel = {
      ...model,
      schema_version: "collective-toy-input-002",
      transitions: model.transitions.map(t => t.id === "t_ab"
        ? {...t, condition: "authorization is valid"}
        : {...t}),
      scenarios: [{id:"baseline",disabled_transitions:[]}]
    };
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", {bubbles:true}));
    }, JSON.stringify(roundTripModel));
    await page.evaluate(() => syncGraphEditor());
    await page.locator("#derive-tgcv-correspondences").click();
    await page.waitForFunction(() => !/Sin propuestas generadas/i.test(
      document.querySelector("#correspondence-review-status")?.textContent || ""), null, {timeout:5000});
    await page.locator("#run").click();
    await page.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /ejecución completada/i,
      "conditional round-trip fixture must execute before export");
    const packageDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const packageDownload = await packageDownloadPromise;
    const packagePath = await packageDownload.path();
    assert.ok(packagePath, "export must produce a downloadable JSON package");
    const exportedPackageText = fs.readFileSync(packagePath, "utf8");
    const exportedPackage = JSON.parse(exportedPackageText);
    assert.equal(exportedPackage.input.transitions.find(t => t.id === "t_ab").condition,
      "authorization is valid", "export must preserve condition text in the source input");
    assert.equal(exportedPackage.result.input_sha256.length, 64,
      "export must preserve a SHA-256 provenance digest for the input");
    await page.locator("#package-file").setInputFiles({
      name: "conditional-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(exportedPackageText)
    });
    await page.locator("#assess-package").click();
    await page.waitForFunction(() =>
      ["replay-verified", "rejected", "inspect-only/replay-unavailable"].includes(
        document.querySelector("#package-assessment")?.dataset.state
      ), null, {timeout:5000});
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "replay-verified",
      "the exported conditional package must pass independent replay: " +
      await page.locator("#package-assessment").textContent());

    // UI lifecycle: a second source transition may not reuse a transformation
    // already activated for the first transition. The prior effective mapping must survive.
    const alreadyEffectiveConflictContext = await browser.newContext();
    try {
      const conflictUi = await alreadyEffectiveConflictContext.newPage();
      await conflictUi.goto("file://" + htmlPath);
      await conflictUi.locator("#load").click();
      await conflictUi.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-already-effective-conflict";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_first",source:"A",target:"B"},
          {id:"t_ab_second",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        parsed.scenarios = [{id:"baseline",disabled_transitions:[]}];
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const details = conflictUi.locator("#correspondence-review-section details").filter({
        has: conflictUi.locator("#tgcv-target-catalogue")
      });
      if (!(await details.evaluate(el => el.open))) await details.locator("summary").click();
      await conflictUi.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001",version:"ui-already-effective-conflict-v1",
          transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await conflictUi.locator("#derive-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const firstCandidate = conflictUi.locator("#correspondence-review-list article").filter({
        hasText:"t_ab_first"
      });
      await firstCandidate.getByRole("button", {name:"Aceptar propuesta"}).click();
      await conflictUi.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const secondCandidate = conflictUi.locator("#correspondence-review-list article").filter({
        hasText:"t_ab_second"
      });
      await secondCandidate.getByRole("button", {name:"Aceptar propuesta"}).click();
      await conflictUi.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "conflict-needs-review",
        null, {timeout:5000});
      const blockedConflict = await conflictUi.evaluate(() => ({
        status:document.querySelector("#effective-correspondence-status")?.textContent || "",
        mappings:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.match(blockedConflict.status, /CONFLICT_NEEDS_REVIEW/);
      assert.equal(blockedConflict.mappings.length, 0,
        "an unresolved apply-time collision must fail closed rather than retain a partially valid effective layer");
      await secondCandidate.getByRole("button", {name:"Rechazar propuesta"}).click();
      await conflictUi.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const activeAfterConflict = await conflictUi.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
          .sort((a,b) => a.system_transition_id.localeCompare(b.system_transition_id)));
      assert.deepEqual(activeAfterConflict, [{system_transition_id:"t_ab_first",tgcv_transformation_id:"T_SHARED_AB"}],
        "after explicitly rejecting the conflicting candidate, the originally selected mapping must be the only effective mapping");
      await conflictUi.locator("#run").click();
      await conflictUi.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      const beforeConflictReload = await conflictUi.evaluate(() => ({
        mappings:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
          .sort((a,b) => a.system_transition_id.localeCompare(b.system_transition_id)),
        scenarios:Object.fromEntries(Object.entries(window.lastPackage?.result?.scenario_results || {}).map(([id,result]) => [id,{
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({state:step.state,transition:step.transition || null})))
        }]))
      }));
      await assertStructuredTAccMatchesExecution(conflictUi, "already-effective mapping blocks second candidate");
      await conflictUi.reload();
      await conflictUi.locator("#load").click();
      await conflictUi.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-already-effective-conflict";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_first",source:"A",target:"B"},
          {id:"t_ab_second",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        parsed.scenarios = [{id:"baseline",disabled_transitions:[]}];
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const reloadDetails = conflictUi.locator("#correspondence-review-section details").filter({
        has: conflictUi.locator("#tgcv-target-catalogue")
      });
      if (!(await reloadDetails.evaluate(el => el.open))) await reloadDetails.locator("summary").click();
      await conflictUi.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001",version:"ui-already-effective-conflict-v1",
          transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await conflictUi.locator("#derive-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      await conflictUi.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictUi.waitForFunction(() =>
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const afterConflictReload = await conflictUi.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
          .sort((a,b) => a.system_transition_id.localeCompare(b.system_transition_id)));
      assert.deepEqual(afterConflictReload, beforeConflictReload.mappings,
        "the original effective mapping must persist after reload and conflict re-derivation");
      await conflictUi.locator("#run").click();
      await conflictUi.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      const afterConflictReloadExecution = await conflictUi.evaluate(() =>
        Object.fromEntries(Object.entries(window.lastPackage?.result?.scenario_results || {}).map(([id,result]) => [id,{
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({state:step.state,transition:step.transition || null})))
        }]))
      );
      assert.deepEqual(afterConflictReloadExecution, beforeConflictReload.scenarios,
        "conflict re-derivation after reload must preserve execution trajectories");
      await assertStructuredTAccMatchesExecution(conflictUi, "already-effective conflict after reload");
    } finally { await alreadyEffectiveConflictContext.close(); }

    // Package assessment/import must not mutate local human review decisions or activate
    // correspondences: use a separate context with an explicit rejected decision as baseline.
    const importIsolationContext = await browser.newContext();
    try {
      const importIsolationPage = await importIsolationContext.newPage();
      await importIsolationPage.goto("file://" + htmlPath);
      await importIsolationPage.locator("#load").click();
      await importIsolationPage.locator("#run").click();
      await importIsolationPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      await importIsolationPage.locator("#derive-tgcv-correspondences").click();
      await importIsolationPage.locator("#correspondence-review-list article").first().waitFor();
      await importIsolationPage.locator("#correspondence-review-list article").first()
        .getByRole("button", {name:"Rechazar propuesta"}).click();
      assert.match(await importIsolationPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "import-isolation fixture must start with an explicit human rejection");
      const reviewStateBeforeImport = await importIsolationPage.evaluate(() => Object.fromEntries(
        Object.keys(localStorage).filter(k => /tgcv-(?:effective-mappings|correspondence-review)-001:/.test(k))
          .sort().map(k => [k, localStorage.getItem(k)])
      ));
      const effectiveBeforeImport = await importIsolationPage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false));
      await importIsolationPage.locator("#package-file").setInputFiles({
        name: "isolated-import-assessment.json",
        mimeType: "application/json",
        buffer: Buffer.from(exportedPackageText)
      });
      await importIsolationPage.locator("#assess-package").click();
      await importIsolationPage.waitForFunction(() =>
        ["replay-verified", "rejected", "inspect-only/replay-unavailable"].includes(
          document.querySelector("#package-assessment")?.dataset.state
        ), null, {timeout:5000});
      assert.equal(await importIsolationPage.locator("#package-assessment").getAttribute("data-state"), "replay-verified",
        "valid package must be assessed successfully in the isolated context");
      const reviewStateAfterImport = await importIsolationPage.evaluate(() => Object.fromEntries(
        Object.keys(localStorage).filter(k => /tgcv-(?:effective-mappings|correspondence-review)-001:/.test(k))
          .sort().map(k => [k, localStorage.getItem(k)])
      ));
      assert.deepEqual(reviewStateAfterImport, reviewStateBeforeImport,
        "package assessment must not mutate persisted local human review decisions");
      const effectiveAfterImport = await importIsolationPage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false));
      assert.deepEqual(effectiveAfterImport, effectiveBeforeImport,
        "package assessment must not activate correspondences in the local model");
      assert.match(await importIsolationPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "package assessment must preserve the visible local rejection");
    } finally { await importIsolationContext.close(); }

    // Tampering with a condition after export must be rejected, never reported as verified replay.
    const tamperedPackage = JSON.parse(exportedPackageText);
    tamperedPackage.input.transitions.find(t => t.id === "t_ab").condition = "authorization is not valid";
    await page.locator("#package-file").setInputFiles({
      name: "tampered-conditional-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(tamperedPackage))
    });
    await page.locator("#assess-package").click();
    await page.waitForFunction(() => ["rejected", "inspect-only/replay-unavailable"].includes(
      document.querySelector("#package-assessment")?.dataset.state
    ), null, {timeout:5000});
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "rejected",
      "tampered conditional input must be rejected, not replay-verified");

    // JSON entry must reject an evaluation whose bound condition no longer matches the transition text.
    const staleJsonCondition = {
      ...roundTripModel,
      transitions: roundTripModel.transitions.map(t => t.id === "t_ab"
        ? {...t, condition: "authorization has been revoked"}
        : {...t}),
      scenarios: [{id:"baseline",disabled_transitions:[],condition_evaluations:{
        t_ab:{condition:"authorization is valid",result:"TRUE"}
      }}]
    };
    await page.locator("#model").evaluate((el, value) => {
      el.value = JSON.stringify(value);
      el.dispatchEvent(new Event("input", {bubbles:true}));
    }, staleJsonCondition);
    await page.locator("#run").click();
    await page.waitForFunction(() => /evaluación de condición está obsoleta/i.test(
      document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
    assert.match(await page.locator("#status").textContent(), /evaluación de condición está obsoleta/i,
      "JSON input must not reuse TRUE from a different condition string");

    // Isolated rejection regression: use a fresh browser context so no accepted/pending
    // review decision from the main scenario can influence this result.
    const rejectionContext = await browser.newContext();
    try {
      const rejectionPage = await rejectionContext.newPage();
      await rejectionPage.goto("file://" + htmlPath);
      await rejectionPage.locator("#load").click();
      await rejectionPage.locator("#run").click();
      await rejectionPage.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      assert.match(await rejectionPage.locator("#status").textContent(), /ejecución completada/i,
        "isolated rejection baseline must execute successfully");
      const declaredMappingBeforeRejection = await rejectionPage.locator("#model").evaluate(el => {
        const parsed = JSON.parse(el.value);
        return JSON.parse(JSON.stringify(parsed.tgcv_mapping || null));
      });
      const executionBeforeIsolatedRejection = await rejectionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      assert.ok(Object.keys(executionBeforeIsolatedRejection).length,
        "isolated rejection baseline must expose structured scenario results");
      await rejectionPage.locator("#derive-tgcv-correspondences").click();
      await rejectionPage.locator("#correspondence-review-list article").first().waitFor();
      assert.ok(await rejectionPage.locator("#correspondence-review-list article").count() >= 1,
        "isolated rejection fixture must expose at least one correspondence candidate to reject");
      // Revocation after materialization gets a clean model/catalogue scope.
      // The default demo may contain declared mappings, so it is not a valid fixture
      // for testing acceptance and subsequent revocation of a derived candidate.
      const revocationContext = await browser.newContext();
      try {
        const revocationPage = await revocationContext.newPage();
        await revocationPage.goto("file://" + htmlPath);
        await revocationPage.locator("#load").click();
        await revocationPage.locator("#model").evaluate((el, value) => {
          const parsed = JSON.parse(JSON.stringify(value));
          parsed.model_id = "ui-correspondence-revocation-isolated";
          parsed.initial_state = "A";
          parsed.states = ["A","B"];
          parsed.transitions = [{id:"t_ab_revocation",source:"A",target:"B"}];
          parsed.relations = [];
          delete parsed.tgcv_mapping;
          el.value = JSON.stringify(parsed, null, 2);
          el.dispatchEvent(new Event("input", {bubbles:true}));
          return parsed;
        }, model);
        const catalogueDetails = revocationPage.locator("#correspondence-review-section details").filter({
          has: revocationPage.locator("#tgcv-target-catalogue")
        });
        if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
        await revocationPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
          el.value = JSON.stringify(value, null, 2);
          el.dispatchEvent(new Event("input", {bubbles:true}));
          el.dispatchEvent(new Event("change", {bubbles:true}));
        }, {
          schema:"tgcv-target-catalogue-001", version:"ui-revocation-isolated-v1",
          transformations:[{id:"T_REVOCATION_AB",source_state:"A",target_state:"B"}]
        });
        await revocationPage.locator("#derive-tgcv-correspondences").click();
        await revocationPage.waitForFunction(() =>
          document.querySelectorAll("#correspondence-review-list article").length === 1,
          null, {timeout:5000});
        const candidate = revocationPage.locator("#correspondence-review-list article").first();
        await candidate.getByRole("button", {name:"Aceptar propuesta"}).click();
        await revocationPage.locator("#apply-accepted-tgcv-correspondences").click();
        await revocationPage.waitForFunction(() =>
          document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
          null, {timeout:5000});
        const beforeRevocation = await revocationPage.evaluate(() => ({
          mappings:(window.effectiveCorrespondenceState?.mappings || [])
            .filter(mapping => mapping.status === "EFFECTIVE" && mapping.active !== false),
          storage:Object.keys(localStorage).filter(key => key.startsWith("tgcv-effective-mappings-001:"))
            .map(key => JSON.parse(localStorage.getItem(key))).filter(Boolean)
        }));
        assert.equal(beforeRevocation.mappings.length, 1,
          "isolated accepted candidate must materialize before revocation");
        await candidate.getByRole("button", {name:"Rechazar propuesta"}).click();
        await revocationPage.locator("#apply-accepted-tgcv-correspondences").click();
        // Do not accept the previous replay-verified state as completion of this
        // async click; wait for the new, externally visible zero-active result.
        await revocationPage.waitForFunction(() => {
          const status = document.querySelector("#effective-correspondence-status");
          return status?.dataset.state === "replay-verified" &&
            /Correspondencias efectivas activas: 0\./.test(status.textContent || "");
        }, null, {timeout:5000});
        const afterRevocation = await revocationPage.evaluate(() => ({
          mappings:(window.effectiveCorrespondenceState?.mappings || [])
            .filter(mapping => mapping.status === "EFFECTIVE" && mapping.active !== false),
          storage:Object.keys(localStorage).filter(key => key.startsWith("tgcv-effective-mappings-001:"))
            .map(key => JSON.parse(localStorage.getItem(key))).filter(Boolean)
        }));
        assert.equal(afterRevocation.mappings.length, 0,
          "revoking an accepted candidate must remove it from the active effective set");
        assert.ok(afterRevocation.storage.some(record => (record.history || []).some(mapping =>
          mapping.candidate_id && mapping.status === "STALE" && mapping.active === false &&
          /decision is no longer accepted|ya no está aceptada/i.test(mapping.stale_reason || ""))),
          "revocation must preserve the former effective mapping as inactive audit history");

        // A subsequent application must not resurrect a revoked candidate or
        // duplicate its stale audit entry.
        await revocationPage.locator("#apply-accepted-tgcv-correspondences").click();
        await revocationPage.waitForFunction(() => {
          const status = document.querySelector("#effective-correspondence-status");
          return status?.dataset.state === "replay-verified" &&
            /Correspondencias efectivas activas: 0\./.test(status.textContent || "");
        }, null, {timeout:5000});
        const afterRepeatedApply = await revocationPage.evaluate(() => ({
          mappings:(window.effectiveCorrespondenceState?.mappings || [])
            .filter(mapping => mapping.status === "EFFECTIVE" && mapping.active !== false),
          storage:Object.keys(localStorage).filter(key => key.startsWith("tgcv-effective-mappings-001:"))
            .map(key => JSON.parse(localStorage.getItem(key))).filter(Boolean)
        }));
        assert.equal(afterRepeatedApply.mappings.length, 0,
          "reapplying after revocation must not resurrect the rejected mapping");
        assert.equal(afterRepeatedApply.storage.reduce((count, record) =>
          count + (record.history || []).filter(mapping =>
            mapping.candidate_id && mapping.status === "STALE" && mapping.active === false &&
            /decision is no longer accepted|ya no está aceptada/i.test(mapping.stale_reason || "")
          ).length, 0), 1,
          "repeated application must not duplicate the revocation audit entry");
      } finally { await revocationContext.close(); }
      await rejectionPage.locator("#correspondence-review-list article").first()
        .getByRole("button", {name:"Rechazar propuesta"}).click();
      assert.match(await rejectionPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "isolated rejection must persist an explicit rejected decision");
      await rejectionPage.locator("#run").click();
      await rejectionPage.waitForFunction(() => /ejecución completada|no se ha podido ejecutar/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      assert.match(await rejectionPage.locator("#status").textContent(), /ejecución completada/i,
        "a rejected-only correspondence decision must leave the system executable");
      const executionAfterIsolatedRejection = await rejectionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      assert.deepEqual(executionAfterIsolatedRejection, executionBeforeIsolatedRejection,
        "rejecting a proposal in isolation must preserve every scenario reachability and trajectory");
      const declaredMappingAfterRejection = await rejectionPage.locator("#model").evaluate(el => {
        const parsed = JSON.parse(el.value);
        return JSON.parse(JSON.stringify(parsed.tgcv_mapping || null));
      });
      assert.deepEqual(declaredMappingAfterRejection, declaredMappingBeforeRejection,
        "rejecting a derived proposal must preserve the exact user-declared TGCV mapping");
      const effectiveAfterIsolatedRejection = await rejectionPage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(mapping => mapping.status === "EFFECTIVE")
          .map(mapping => mapping.tgcv_transformation_id).sort());
      assert.ok(!effectiveAfterIsolatedRejection.includes("T_HUMIDITY"),
        "isolated rejected proposal must not appear in the structured effective correspondence set");
      await rejectionPage.locator("#derive-tgcv-correspondences").click();
      assert.match(await rejectionPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "isolated rejected decision must persist when proposals are regenerated");

      // A review-required ambiguous proposal can be explicitly rejected, and that
      // human decision must survive regeneration for the exact model/catalogue scope.
      const reviewCatalogue = {
        schema:"tgcv-target-catalogue-001", version:"human-conflict-review-v1",
        transformations:[
          {id:"T_REVIEW_AB_1",source_state:"A",target_state:"B"},
          {id:"T_REVIEW_AB_2",source_state:"A",target_state:"B"}
        ]
      };
      await rejectionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", {bubbles:true})); el.dispatchEvent(new Event("change", {bubbles:true})); }, JSON.stringify(reviewCatalogue));
      await rejectionPage.locator("#derive-tgcv-correspondences").click();
      const reviewRequired = rejectionPage.locator("#correspondence-review-list article").filter({hasText:"NEEDS_REVIEW"});
      await reviewRequired.first().waitFor();
      assert.equal(await reviewRequired.count(), 2,
        "duplicate exact-boundary targets must create review-required candidates");
      await reviewRequired.first().getByRole("button",{name:"Rechazar propuesta"}).click();
      assert.match(await rejectionPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "review-required proposal must accept an explicit human rejection");
      const rejectedReviewStorage = await rejectionPage.evaluate(() =>
        Object.fromEntries(Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:"))
          .sort().map(k => [k, localStorage.getItem(k)])));
      assert.ok(Object.values(rejectedReviewStorage).some(raw => raw && raw.includes('"decision":"REJECTED"')),
        "human rejection of a review-required candidate must be persisted");
      await rejectionPage.locator("#derive-tgcv-correspondences").click();
      assert.match(await rejectionPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
        "human rejection of a review-required candidate must survive proposal regeneration");
      const rejectedReviewStorageAfter = await rejectionPage.evaluate(() =>
        Object.fromEntries(Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:"))
          .sort().map(k => [k, localStorage.getItem(k)])));
      assert.deepEqual(rejectedReviewStorageAfter,rejectedReviewStorage,
        "regenerating review-required proposals must not rewrite the persisted human decision");
    } finally { await rejectionContext.close(); }

    // UI integration regression: the derivation UI must not propose a target already
    // reserved by a user-declared mapping, and must preserve that declaration unchanged.
    const declaredCollisionContext = await browser.newContext();
    try {
      const collisionPage = await declaredCollisionContext.newPage();
      await collisionPage.goto("file://" + htmlPath);
      await collisionPage.locator("#load").click();
      const declaredCollisionModel = await collisionPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        // Add a second A→C transition so the declared T_CONFLICT_AB target is
        // genuinely reserved against a distinct, otherwise matching candidate.
        parsed.transitions.push({id:"t_ac_unmapped",source:"A",target:"C"});
        parsed.tgcv_mapping = {
          schema:"tgcv-explicit-mapping-001", mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",
          mappings:[{system_transition_id:"t_ac",tgcv_transformation_id:"T_CONFLICT_AB"}],
          relations:[]
        };
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        return parsed;
      }, model);
      const declaredCollisionBefore = JSON.parse(JSON.stringify(declaredCollisionModel.tgcv_mapping));
      const catalogueDetails = collisionPage.locator("#correspondence-review-section details").filter({
        has: collisionPage.locator("#tgcv-target-catalogue")
      });
      if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
      await collisionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"ui-declared-conflict-v2",
        transformations:[{id:"T_CONFLICT_AB",source_state:"A",target_state:"C"}]
      });
      await collisionPage.locator("#derive-tgcv-correspondences").click();
      await collisionPage.waitForFunction(() =>
        /conflicto con correspondencias declaradas por el usuario/i.test(
          document.querySelector("#correspondence-review-status")?.textContent || ""
        ), null, {timeout:5000});
      const collisionSnapshot = await collisionPage.evaluate(() => ({
        status:document.querySelector("#correspondence-review-status")?.textContent || "",
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        proposalCount:document.querySelectorAll("#correspondence-review-list article").length,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
      }));
      assert.deepEqual(collisionSnapshot.declared, declaredCollisionBefore,
        "the real UI derivation flow must preserve the exact user-declared mapping");
      assert.equal(collisionSnapshot.proposalCount, 0,
        "the real UI must not offer a derived proposal that reuses a declared target");
      assert.equal(collisionSnapshot.effective.length, 0,
        "a declared-target collision must not create an effective derived mapping");
      assert.match(collisionSnapshot.status, /conflicto con correspondencias declaradas por el usuario/i,
        "the UI must report that no compatible proposals were generated");
    } finally { await declaredCollisionContext.close(); }

    // Same-transition conflict: an existing user declaration owns t_ac, so an
    // alternative exact-boundary target must be excluded, not offered as a derived proposal.
    const sameTransitionDeclaredContext = await browser.newContext();
    try {
      const sameTransitionPage = await sameTransitionDeclaredContext.newPage();
      await sameTransitionPage.goto("file://" + htmlPath);
      await sameTransitionPage.locator("#load").click();
      const sameTransitionModel = await sameTransitionPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.tgcv_mapping = {
          schema:"tgcv-explicit-mapping-001", mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",
          mappings:[{system_transition_id:"t_ac",tgcv_transformation_id:"T_CONFLICT_AB"}],
          relations:[]
        };
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        return parsed;
      }, model);
      const declaredBefore = JSON.parse(JSON.stringify(sameTransitionModel.tgcv_mapping));
      await sameTransitionPage.locator("#run").click();
      await sameTransitionPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const declaredConflictExecutionBaseline = await sameTransitionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state, transition:step.transition || null
          })))
        }]));
      });
      await assertStructuredTAccMatchesExecution(sameTransitionPage, "declared-transition conflict baseline");
      const catalogueDetails = sameTransitionPage.locator("#correspondence-review-section details").filter({
        has: sameTransitionPage.locator("#tgcv-target-catalogue")
      });
      if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
      await sameTransitionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"ui-same-transition-declared-conflict-v1",
        transformations:[
          {id:"T_CONFLICT_AB",source_state:"A",target_state:"C"},
          {id:"T_CONFLICT_AC",source_state:"A",target_state:"C"}
        ]
      });
      await sameTransitionPage.locator("#derive-tgcv-correspondences").click();
      await sameTransitionPage.waitForFunction(() =>
        /conflicto con correspondencias declaradas por el usuario/i.test(
          document.querySelector("#correspondence-review-status")?.textContent || ""
        ), null, {timeout:5000});
      const sameTransitionSnapshot = await sameTransitionPage.evaluate(() => ({
        status:document.querySelector("#correspondence-review-status")?.textContent || "",
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        proposalCount:document.querySelectorAll("#correspondence-review-list article").length,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.deepEqual(sameTransitionSnapshot.declared, declaredBefore,
        "an alternative candidate must not rewrite the exact same-transition user declaration");
      assert.equal(sameTransitionSnapshot.proposalCount, 0,
        "a transition already declared by the user must not receive an alternative derived proposal");
      assert.equal(sameTransitionSnapshot.effective.length, 0,
        "an alternative target for a declared transition must not materialize an effective mapping");
      assert.match(sameTransitionSnapshot.status, /conflicto con correspondencias declaradas por el usuario/i,
        "the UI must disclose that the declared mapping reserved the transition");
      await sameTransitionPage.locator("#run").click();
      await sameTransitionPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const declaredConflictExecutionAfterDerivation = await sameTransitionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state, transition:step.transition || null
          })))
        }]));
      });
      assert.deepEqual(declaredConflictExecutionAfterDerivation, declaredConflictExecutionBaseline,
        "a conflicting derived target must not alter reachable states or execution trajectories");
      await assertStructuredTAccMatchesExecution(sameTransitionPage, "declared-transition conflict unresolved");

      // Grouped order-invariance check for the declared↔derived conflict:
      // reverse the two same-boundary catalogue candidates and require the same
      // abstention, exact declaration, and empty effective/proposal sets.
      const reversedCatalogue = {
        schema:"tgcv-target-catalogue-001", version:"ui-same-transition-declared-conflict-reversed-v1",
        transformations:[
          {id:"T_CONFLICT_AC",source_state:"A",target_state:"C"},
          {id:"T_CONFLICT_AB",source_state:"A",target_state:"C"}
        ]
      };
      await sameTransitionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, reversedCatalogue);
      await sameTransitionPage.locator("#derive-tgcv-correspondences").click();
      await sameTransitionPage.waitForFunction(() =>
        /conflicto con correspondencias declaradas por el usuario/i.test(
          document.querySelector("#correspondence-review-status")?.textContent || ""
        ), null, {timeout:5000});
      const reversedSameTransitionSnapshot = await sameTransitionPage.evaluate(() => ({
        status:document.querySelector("#correspondence-review-status")?.textContent || "",
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        proposalCount:document.querySelectorAll("#correspondence-review-list article").length,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.deepEqual(reversedSameTransitionSnapshot.declared, declaredBefore,
        "reversing catalogue candidate order must preserve the declared mapping exactly");
      assert.equal(reversedSameTransitionSnapshot.proposalCount, 0,
        "reversing catalogue candidate order must not offer a derived proposal");
      assert.equal(reversedSameTransitionSnapshot.effective.length, 0,
        "reversing catalogue candidate order must not create an effective mapping");
      assert.match(reversedSameTransitionSnapshot.status,
        /conflicto con correspondencias declaradas por el usuario/i,
        "reversing catalogue candidate order must preserve declared-conflict abstention");
    } finally { await sameTransitionDeclaredContext.close(); }

    // Declared↔declared pairwise conflicts must be reported without rewriting declarations.
    const declaredMappingPairContext = await browser.newContext();
    try {
      const declaredPairPage = await declaredMappingPairContext.newPage();
      await declaredPairPage.goto("file://" + htmlPath);
      await declaredPairPage.locator("#load").click();
      const declaredPairModel = await declaredPairPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-declared-mapping-pair-conflicts";
        parsed.initial_state = "A";
        parsed.states = ["A","B","C"];
        parsed.transitions = [
          {id:"t_declared_ab_1",source:"A",target:"B"},
          {id:"t_declared_ab_2",source:"A",target:"B"},
          {id:"t_declared_ac",source:"A",target:"C"}
        ];
        parsed.relations = [];
        parsed.tgcv_mapping = {
          schema:"tgcv-explicit-mapping-001",
          mapping_rule:"user-declared-map-v1",
          provenance:"user-declared",
          mappings:[
            {system_transition_id:"t_declared_ab_1",tgcv_transformation_id:"T_SHARED_AB"},
            {system_transition_id:"t_declared_ab_1",tgcv_transformation_id:"T_SHARED_AB"},
            {system_transition_id:"t_declared_ab_2",tgcv_transformation_id:"T_SHARED_AB"},
            {system_transition_id:"t_declared_ac",tgcv_transformation_id:"T_AC_1"},
            {system_transition_id:"t_declared_ac",tgcv_transformation_id:"T_AC_2"}
          ],
          relations:[]
        };
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        return parsed;
      }, model);
      const declaredPairBefore = JSON.parse(JSON.stringify(declaredPairModel.tgcv_mapping));
      const pairDetails = declaredPairPage.locator("#correspondence-review-section details").filter({
        has: declaredPairPage.locator("#tgcv-target-catalogue")
      });
      if (!(await pairDetails.evaluate(el => el.open))) await pairDetails.locator("summary").click();
      await declaredPairPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001",version:"declared-pair-conflicts-v1",
        transformations:[
          {id:"T_SHARED_AB",source_state:"A",target_state:"B"},
          {id:"T_AC_1",source_state:"A",target_state:"C"},
          {id:"T_AC_2",source_state:"A",target_state:"C"}
        ]
      });
      await declaredPairPage.locator("#derive-tgcv-correspondences").click();
      await declaredPairPage.waitForFunction(() =>
        /conflictos entre mappings declarados/i.test(
          document.querySelector("#correspondence-review-status")?.textContent || ""
        ), null, {timeout:5000});
      const declaredPairSnapshot = await declaredPairPage.evaluate(() => ({
        status:document.querySelector("#correspondence-review-status")?.textContent || "",
        model:JSON.parse(document.querySelector("#model").value),
        proposals:document.querySelectorAll("#correspondence-review-list article").length,
        result:window.correspondenceReviewState || null
      }));
      assert.deepEqual(declaredPairSnapshot.model.tgcv_mapping, declaredPairBefore,
        "declared↔declared conflicts must preserve every original declaration");
      assert.equal(declaredPairSnapshot.proposals, 0,
        "declared mappings must not be converted into derived proposals to resolve their own conflict");
      assert.match(declaredPairSnapshot.status, /conflictos entre mappings declarados/i,
        "the UI must report conflicts between declared mappings instead of silently ignoring them");
      assert.match(declaredPairSnapshot.status, /duplicados exactos/i,
        "the UI must identify exact duplicate declarations as an issue");
      assert.equal(Number((declaredPairSnapshot.status.match(/detectaron (\d+) conflictos entre mappings declarados/i) || [])[1]), 3,
        "two structural conflict classes and one exact duplicate must be reported");

      // Reverse declaration order: conflict classification/count and non-mutation must be invariant.
      const reversedDeclaredPairModel = JSON.parse(JSON.stringify(declaredPairModel));
      reversedDeclaredPairModel.tgcv_mapping.mappings.reverse();
      await declaredPairPage.locator("#model").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, reversedDeclaredPairModel);
      await declaredPairPage.locator("#derive-tgcv-correspondences").click();
      await declaredPairPage.waitForFunction(() =>
        /conflictos entre mappings declarados/i.test(
          document.querySelector("#correspondence-review-status")?.textContent || ""
        ), null, {timeout:5000});
      const reversedDeclaredPairSnapshot = await declaredPairPage.evaluate(() => ({
        status:document.querySelector("#correspondence-review-status")?.textContent || "",
        model:JSON.parse(document.querySelector("#model").value),
        proposals:document.querySelectorAll("#correspondence-review-list article").length
      }));
      const conflictCount = value => Number((value.match(/detectaron (\d+) conflictos entre mappings declarados/i) || [])[1]);
      assert.equal(conflictCount(reversedDeclaredPairSnapshot.status), conflictCount(declaredPairSnapshot.status),
        "reversing declared mapping order must preserve the number of conflict classes reported");
      assert.deepEqual(reversedDeclaredPairSnapshot.model.tgcv_mapping,
        reversedDeclaredPairModel.tgcv_mapping,
        "reversing declaration order must not rewrite the declared mapping list");
      assert.equal(reversedDeclaredPairSnapshot.proposals, 0,
        "reversing declaration order must not create derived proposals");

      // Exhaustive grouped block: three pairwise combinations plus every unique
      // permutation of the five-row combined fixture (5! / 2! = 60).
      const conflictSignature = conflicts => conflicts.map(c => ({
        code:c.code,
        system_transition_id:c.system_transition_id || null,
        tgcv_transformation_id:c.tgcv_transformation_id || null,
        system_transition_ids:[...(c.system_transition_ids || [])].sort(),
        tgcv_transformation_ids:[...(c.tgcv_transformation_ids || [])].sort()
      })).sort((a,b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
      const setDeclaredMappings = async mappings => {
        const nextModel = JSON.parse(JSON.stringify(declaredPairModel));
        nextModel.tgcv_mapping.mappings = mappings;
        const transitionIds = [...new Set(mappings.map(m => m.system_transition_id))];
        nextModel.transitions = declaredPairModel.transitions.filter(t => transitionIds.includes(t.id));
        nextModel.model_id = "ui-declared-mapping-exhaustive-" + (++exhaustiveCase);
        await declaredPairPage.locator("#model").evaluate((el, value) => {
          el.value = JSON.stringify(value, null, 2);
          el.dispatchEvent(new Event("input", {bubbles:true}));
        }, nextModel);
        await declaredPairPage.locator("#derive-tgcv-correspondences").click();
        await declaredPairPage.waitForFunction(() => {
          const model = JSON.parse(document.querySelector("#model").value);
          const state = window.correspondenceReviewState;
          return !!state?.sourceModelSha256 && state.sourceModelCanonical !== null &&
            state.sourceModelCanonical.includes(model.model_id);
        }, null, {timeout:5000});
        return await declaredPairPage.evaluate(() => ({
          model:JSON.parse(document.querySelector("#model").value),
          proposals:document.querySelectorAll("#correspondence-review-list article").length,
          conflicts:window.correspondenceReviewState?.declaredMappingConflicts || []
        }));
      };
      let exhaustiveCase = 0;
      const rows = declaredPairModel.tgcv_mapping.mappings;
      const pairCases = [
        {id:"C12",rows:[rows[0],rows[1],rows[3],rows[4]]},
        {id:"C13",rows:[rows[0],rows[0],rows[1],rows[2]]},
        {id:"C23",rows:[rows[1],rows[2],rows[3],rows[4]]}
      ];
      for (const pairCase of pairCases) {
        const pairResult = await setDeclaredMappings(pairCase.rows);
        assert.deepEqual(pairResult.model.tgcv_mapping.mappings, pairCase.rows,
          pairCase.id + " must preserve declared mapping rows");
        assert.equal(pairResult.proposals, 0, pairCase.id + " must not derive proposals to resolve declared conflicts");
        const codes = new Set(pairResult.conflicts.map(c => c.code));
        assert(codes.has("DECLARED_MAPPING_DUPLICATE") === (pairCase.id !== "C23"),
          pairCase.id + " duplicate classification mismatch");
        assert(codes.has("DECLARED_TRANSITION_MULTIPLE_TARGETS") === (pairCase.id !== "C13"),
          pairCase.id + " multiple-target classification mismatch");
        assert(codes.has("DECLARED_TARGET_MULTIPLE_TRANSITIONS") === (pairCase.id !== "C12"),
          pairCase.id + " shared-target classification mismatch");
      }

      const uniquePermutations = [];
      const buildPermutations = (remaining, prefix) => {
        if (!remaining.length) { uniquePermutations.push(prefix); return; }
        const usedAtThisDepth = new Set();
        for (let index = 0; index < remaining.length; index++) {
          const key = JSON.stringify(remaining[index]);
          if (usedAtThisDepth.has(key)) continue;
          usedAtThisDepth.add(key);
          buildPermutations(
            remaining.filter((_, i) => i !== index),
            [...prefix, remaining[index]]
          );
        }
      };
      buildPermutations(rows, []);
      assert.equal(uniquePermutations.length, 60, "fixture must enumerate exactly 60 unique permutations");
      const baselineSignature = JSON.stringify(conflictSignature(declaredPairSnapshot.result?.declaredMappingConflicts || []));
      for (let index = 0; index < uniquePermutations.length; index++) {
        const permutation = uniquePermutations[index];
        const result = await setDeclaredMappings(permutation);
        assert.deepEqual(result.model.tgcv_mapping.mappings, permutation,
          "permutation " + index + " must preserve the exact input order");
        assert.equal(result.proposals, 0, "permutation " + index + " must not create derived proposals");
        assert.equal(JSON.stringify(conflictSignature(result.conflicts)), baselineSignature,
          "permutation " + index + " must preserve the normalized semantic conflict signature");
      }
    } finally { await declaredMappingPairContext.close(); }

    // Declared-mapping lifecycle: preserve the user's mapping and its execution semantics
    // across catalogue derivation and a page reload, without converting declarations into
    // derived-effective records or silently changing condition reachability.
    const declaredLifecycleContext = await browser.newContext();
    try {
      const declaredLifecyclePage = await declaredLifecycleContext.newPage();
      await declaredLifecyclePage.goto("file://" + htmlPath);
      await declaredLifecyclePage.locator("#load").click();
      const declaredLifecycleModel = JSON.parse(JSON.stringify(explicitlyMappedModel));
      const declaredLifecycleBefore = JSON.parse(JSON.stringify(declaredLifecycleModel.tgcv_mapping));
      await declaredLifecyclePage.locator("#model").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, declaredLifecycleModel);
      await declaredLifecyclePage.locator("#run").click();
      await declaredLifecyclePage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(declaredLifecyclePage, "user-declared mapping baseline");
      const declaredBaseline = await declaredLifecyclePage.evaluate(() => {
        const pkg = window.lastPackage;
        const model = JSON.parse(document.querySelector("#model").value);
        const result = pkg?.result?.scenario_results?.baseline || {};
        return {
          declared:model.tgcv_mapping,
          reachable:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          }))),
          graph:document.querySelector("#tgcv-graph")?.textContent || "",
          provenance:document.querySelector("#tgcv-provenance-note")?.textContent || ""
        };
      });
      assert.deepEqual(declaredBaseline.declared, declaredLifecycleBefore,
        "execution must preserve the exact user-declared mapping and provenance");
      assert.ok(declaredBaseline.reachable.includes("B") && declaredBaseline.reachable.includes("C") && declaredBaseline.reachable.includes("D"),
        "the declared mapping fixture must exercise both evaluated conditional and unconditional paths");

      const declaredDetails = declaredLifecyclePage.locator("#correspondence-review-section details").filter({
        has: declaredLifecyclePage.locator("#tgcv-target-catalogue")
      });
      if (!(await declaredDetails.evaluate(el => el.open))) await declaredDetails.locator("summary").click();
      await declaredLifecyclePage.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001",version:"declared-lifecycle-v1",
          transformations:[
            {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
            {id:"T_AC",source_state:"A",target_state:"C"},
            {id:"T_CD",source_state:"C",target_state:"D"}
          ]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await declaredLifecyclePage.locator("#derive-tgcv-correspondences").click();
      const declaredAfterDerive = await declaredLifecyclePage.locator("#model").evaluate(el =>
        JSON.parse(JSON.stringify(JSON.parse(el.value).tgcv_mapping))
      );
      assert.deepEqual(declaredAfterDerive, declaredLifecycleBefore,
        "catalogue derivation must never rewrite the declared mapping");
      const declaredEffectiveDerived = await declaredLifecyclePage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
      );
      assert.equal(declaredEffectiveDerived.length, 0,
        "user declarations must not be silently duplicated as derived-effective mappings");

      await declaredLifecyclePage.reload();
      const nativeRestoredDeclaredModel = await declaredLifecyclePage.locator("#model").evaluate(el => {
        try { return JSON.parse(el.value); } catch (_e) { return null; }
      });
      assert.deepEqual(nativeRestoredDeclaredModel?.tgcv_mapping, declaredLifecycleBefore,
        "native page reload must restore the exact declared mapping without manual model reinjection");
      assert.deepEqual(nativeRestoredDeclaredModel, declaredLifecycleModel,
        "native page reload must restore the complete source model snapshot");
      await declaredLifecyclePage.locator("#run").click();
      await declaredLifecyclePage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(declaredLifecyclePage, "user-declared mapping after reload");
      const declaredAfterReload = await declaredLifecyclePage.evaluate(() => {
        const pkg = window.lastPackage;
        const model = JSON.parse(document.querySelector("#model").value);
        const result = pkg?.result?.scenario_results?.baseline || {};
        return {
          declared:model.tgcv_mapping,
          reachable:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          }))),
          graph:document.querySelector("#tgcv-graph")?.textContent || "",
          provenance:document.querySelector("#tgcv-provenance-note")?.textContent || ""
        };
      });
      assert.deepEqual(declaredAfterReload.declared, declaredBaseline.declared,
        "the exact user-declared mapping must survive page reload and model restoration");
      assert.deepEqual(declaredAfterReload.reachable, declaredBaseline.reachable,
        "declared mapping execution reachability must be invariant across reload");
      assert.deepEqual(declaredAfterReload.trajectories, declaredBaseline.trajectories,
        "declared mapping execution trajectories must be invariant across reload");
      assert.equal(declaredAfterReload.graph, declaredBaseline.graph,
        "the declared TGCV graph must be unchanged across reload");
      assert.equal(declaredAfterReload.provenance, declaredBaseline.provenance,
        "declared mapping provenance must be unchanged across reload");
    } finally { await declaredLifecycleContext.close(); }

    // Cross-class integration: one immutable user-declared mapping coexists with
    // accepted derived mappings through execution, persistence, reload and replay.
    const declaredDerivedCrossContext = await browser.newContext();
    try {
      const crossPage = await declaredDerivedCrossContext.newPage();
      await crossPage.goto("file://" + htmlPath);
      await crossPage.locator("#load").click();
      const crossModel = JSON.parse(JSON.stringify(explicitlyMappedModel));
      crossModel.model_id = "ui-declared-derived-cross-lifecycle";
      crossModel.tgcv_mapping.mappings = [
        {system_transition_id:"t_ac",tgcv_transformation_id:"T_AC"}
      ];
      crossModel.tgcv_mapping.relations = [];
      const crossDeclaredBefore = JSON.parse(JSON.stringify(crossModel.tgcv_mapping));
      await crossPage.locator("#model").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, crossModel);
      await crossPage.locator("#run").click();
      await crossPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(crossPage, "declared-plus-derived baseline");
      const groupedBaseline = await crossPage.evaluate(() => {
        const model = JSON.parse(document.querySelector("#model").value);
        const result = window.lastPackage?.result?.scenario_results?.baseline || {};
        return {
          declared: model.tgcv_mapping,
          effective: (window.effectiveCorrespondenceState?.mappings || [])
            .filter(m => m.status === "EFFECTIVE" && m.active !== false)
            .map(m => [m.system_transition_id, m.tgcv_transformation_id]).sort(),
          tAcc: [...(window.lastTgcvDemoResult?.current?.transformations || [])].sort(),
          graph: document.querySelector("#tgcv-graph")?.textContent || "",
          reachable: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        };
      });

      const crossDetails = crossPage.locator("#correspondence-review-section details").filter({
        has: crossPage.locator("#tgcv-target-catalogue")
      });
      if (!(await crossDetails.evaluate(el => el.open))) await crossDetails.locator("summary").click();
      await crossPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"declared-derived-cross-lifecycle-v1",
        transformations:[
          {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
          {id:"T_AC",source_state:"A",target_state:"C"},
          {id:"T_CD",source_state:"C",target_state:"D"}
        ]
      });
      await crossPage.locator("#derive-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const groupedPending = await crossPage.evaluate(() => {
        const model = JSON.parse(document.querySelector("#model").value);
        const result = window.lastPackage?.result?.scenario_results?.baseline || {};
        return {
          declared: model.tgcv_mapping,
          effective: (window.effectiveCorrespondenceState?.mappings || [])
            .filter(m => m.status === "EFFECTIVE" && m.active !== false)
            .map(m => [m.system_transition_id, m.tgcv_transformation_id]).sort(),
          tAcc: [...(window.lastTgcvDemoResult?.current?.transformations || [])].sort(),
          graph: document.querySelector("#tgcv-graph")?.textContent || "",
          reachable: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        };
      });
      assert.deepEqual(groupedPending, groupedBaseline,
        "pending derived proposals must leave declared/effective mappings, T_acc, graph, reachability and trajectories unchanged");
      const crossCandidates = crossPage.locator("#correspondence-review-list article");
      for (const transitionId of ["t_ab", "t_cd"]) {
        const card = crossCandidates.filter({hasText:transitionId});
        await card.getByRole("button", {name:"Aceptar propuesta"}).click();
      }
      const crossPreApply = await crossPage.evaluate(() => ({
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        candidates:window.correspondenceReviewState?.candidates || []
      }));
      assert.deepEqual(crossPreApply.declared, crossDeclaredBefore,
        "derivation and accepting candidates must not rewrite the user-declared mapping");
      assert.equal(crossPreApply.candidates.filter(c => c.decision === "ACCEPTED").length, 2,
        "both non-conflicting derived candidates must have explicit ACCEPTED decisions");

      await crossPage.locator("#apply-accepted-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const crossApplied = await crossPage.evaluate(() => ({
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,
            tgcv_transformation_id:m.tgcv_transformation_id,provenance:m.provenance})),
        graph:document.querySelector("#tgcv-graph")?.textContent || "",
        provenance:document.querySelector("#tgcv-provenance-note")?.textContent || ""
      }));
      assert.deepEqual(crossApplied.declared, crossDeclaredBefore,
        "applying derived mappings must preserve the exact declared mapping and provenance");
      assert.deepEqual(crossApplied.effective.map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort(),
        [["t_ab","T_HUMIDITY"],["t_cd","T_CD"]].sort(),
        "only the two explicitly accepted, non-conflicting mappings must become effective");
      await crossPage.locator("#run").click();
      await crossPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(crossPage, "declared-plus-derived applied");
      const crossExecutionBeforeReload = await crossPage.evaluate(() => {
        const result = window.lastPackage?.result?.scenario_results?.baseline || {};
        return {
          reachable:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          }))),
          graph:document.querySelector("#tgcv-graph")?.textContent || "",
          provenance:document.querySelector("#tgcv-provenance-note")?.textContent || ""
        };
      });

      await crossPage.reload();
      const restoredCrossModel = await crossPage.locator("#model").evaluate(el => {
        try { return JSON.parse(el.value); } catch (_e) { return null; }
      });
      assert.deepEqual(restoredCrossModel?.tgcv_mapping, crossDeclaredBefore,
        "native reload must restore the exact declared mapping without manual model reinjection");
      assert.deepEqual(restoredCrossModel, crossModel,
        "native reload must restore the complete source model used by the cross-class lifecycle");
      const restoredCrossDetails = crossPage.locator("#correspondence-review-section details").filter({
        has: crossPage.locator("#tgcv-target-catalogue")
      });
      if (!(await restoredCrossDetails.evaluate(el => el.open))) await restoredCrossDetails.locator("summary").click();
      // The catalogue is test input, not part of the native model-draft persistence contract.
      // Restore the same catalogue scope, but do not re-inject the declared source model.
      await crossPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"declared-derived-cross-lifecycle-v1",
        transformations:[
          {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
          {id:"T_AC",source_state:"A",target_state:"C"},
          {id:"T_CD",source_state:"C",target_state:"D"}
        ]
      });
      await crossPage.locator("#derive-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      await crossPage.locator("#apply-accepted-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const crossAfterReloadApply = await crossPage.evaluate(() => ({
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort()
      }));
      assert.deepEqual(crossAfterReloadApply.declared, crossDeclaredBefore,
        "reapplying after reload must preserve the user-declared mapping");
      assert.deepEqual(crossAfterReloadApply.effective,
        [["t_ab","T_HUMIDITY"],["t_cd","T_CD"]].sort(),
        "the same two accepted derived mappings must be restored without duplication after reload");
      await crossPage.locator("#run").click();
      await crossPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(crossPage, "declared-plus-derived after reload");
      const crossExecutionAfterReload = await crossPage.evaluate(() => {
        const result = window.lastPackage?.result?.scenario_results?.baseline || {};
        return {
          reachable:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          }))),
          graph:document.querySelector("#tgcv-graph")?.textContent || "",
          provenance:document.querySelector("#tgcv-provenance-note")?.textContent || ""
        };
      });
      assert.deepEqual(crossExecutionAfterReload, crossExecutionBeforeReload,
        "cross-class mapping composition must preserve T_acc-related execution, reachability, trajectories, graph and provenance after reload");

      // Complete the grouped lifecycle in the same fixture: a catalogue-scope
      // change must stale the effective overlay, and restoring the old scope must
      // not replay the former ACCEPTED decisions without a new explicit review.
      const changedCatalogue = {
        schema:"tgcv-target-catalogue-001", version:"declared-derived-cross-lifecycle-v1",
        transformations:[
          {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
          {id:"T_AC",source_state:"A",target_state:"C"},
          {id:"T_CD",source_state:"C",target_state:"D"},
          {id:"T_SCOPE_EXTRA",source_state:"X",target_state:"Y"}
        ]
      };
      await crossPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, changedCatalogue);
      await crossPage.locator("#derive-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        /catálogo cambió.*histórico/i.test(document.querySelector("#correspondence-review-status")?.textContent || ""),
        null, {timeout:5000});
      const groupedStale = await crossPage.evaluate(() => ({
        effective: (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => [m.system_transition_id, m.tgcv_transformation_id]).sort(),
        history: Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:"))
          .map(k => JSON.parse(localStorage.getItem(k)))
          .flatMap(record => [...(record.mappings || []), ...(record.history || [])])
          .filter(m => m.status === "STALE" && m.active === false)
          .map(m => ({transition:m.system_transition_id, transformation:m.tgcv_transformation_id, reason:m.stale_reason}))
      }));
      assert.equal(groupedStale.effective.length, 0,
        "catalogue scope change must remove all cross-class mappings from the active effective overlay");
      assert.ok(groupedStale.history.length >= 2,
        "scope invalidation must preserve stale audit history for the former effective mappings");
      await crossPage.locator("#run").click();
      await crossPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(crossPage, "cross-class mappings after scope invalidation");
      const groupedAfterInvalidation = await crossPage.evaluate(() => {
        const result = window.lastPackage?.result?.scenario_results?.baseline || {};
        return {
          tAcc: [...(window.lastTgcvDemoResult?.current?.transformations || [])].sort(),
          reachable: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        };
      });
      assert.deepEqual(groupedAfterInvalidation.reachable, crossExecutionBeforeReload.reachable,
        "scope invalidation must not change system reachability");
      assert.deepEqual(groupedAfterInvalidation.trajectories, crossExecutionBeforeReload.trajectories,
        "scope invalidation must not change system trajectories");
      assert.ok(!groupedAfterInvalidation.tAcc.includes("T_HUMIDITY") &&
        !groupedAfterInvalidation.tAcc.includes("T_CD"),
        "T_acc must exclude transformations supplied only by stale cross-class mappings");

      await crossPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"declared-derived-cross-lifecycle-v1",
        transformations:[
          {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
          {id:"T_AC",source_state:"A",target_state:"C"},
          {id:"T_CD",source_state:"C",target_state:"D"}
        ]
      });
      await crossPage.locator("#derive-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      assert.match(await crossPage.locator("#correspondence-review-list").textContent(), /Decisión: PENDIENTE/,
        "restoring the prior catalogue scope must not resurrect old ACCEPTED decisions");
      await crossPage.locator("#apply-accepted-tgcv-correspondences").click();
      await crossPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const groupedRestored = await crossPage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => [m.system_transition_id, m.tgcv_transformation_id]).sort());
      assert.deepEqual(groupedRestored, [],
        "restoring the old catalogue and reapplying without fresh acceptance must not reactivate stale mappings");

      // Verify rejection invariance and idempotence in a clean browser context using
      // the same controlled source/catalogue fixture. This isolates the two assertions
      // from the preceding stale-scope lifecycle history while keeping them in this
      // single grouped CI block.
      const residualContext = await browser.newContext();
      try {
        const residualPage = await residualContext.newPage();
        await residualPage.goto("file://" + htmlPath);
        await residualPage.locator("#load").click();
        await residualPage.locator("#model").fill(JSON.stringify(crossModel, null, 2));
        await residualPage.locator("#tgcv-target-catalogue").fill(JSON.stringify({
          schema:"tgcv-target-catalogue-001", version:"declared-derived-cross-lifecycle-v1",
          transformations:[
            {id:"T_HUMIDITY",source_state:"A",target_state:"B"},
            {id:"T_AC",source_state:"A",target_state:"C"},
            {id:"T_CD",source_state:"C",target_state:"D"}
          ]
        }, null, 2));
        await residualPage.locator("#run").click();
        await residualPage.waitForFunction(() => /ejecución completada/i.test(
          document.querySelector("#status")?.textContent || ""), null, {timeout:5000});
        await residualPage.locator("#derive-tgcv-correspondences").click();
        await residualPage.waitForFunction(() =>
          document.querySelectorAll("#correspondence-review-list article").length === 2,
          null, {timeout:5000});
        const residualSnapshot = () => residualPage.evaluate(() => {
          const model = JSON.parse(document.querySelector("#model").value);
          const result = window.lastPackage?.result?.scenario_results?.baseline || {};
          return {
            declared:model.tgcv_mapping,
            effective:(window.effectiveCorrespondenceState?.mappings || [])
              .filter(m => m.status === "EFFECTIVE" && m.active !== false)
              .map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort(),
            tAcc:[...(window.lastTgcvDemoResult?.current?.transformations || [])].sort(),
            graph:document.querySelector("#tgcv-graph")?.textContent || "",
            reachable:[...(result.reachable_states || [])].sort(),
            trajectories:(result.trajectories || []).map(path => path.map(step => ({
              state:step.state,transition:step.transition || null
            })))
          };
        });
        const residualBaseline = await residualSnapshot();
        await residualPage.locator("#correspondence-review-list article").filter({hasText:"t_ab"})
          .getByRole("button", {name:"Rechazar propuesta"}).click();
        assert.match(await residualPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
          "grouped lifecycle must persist an explicit rejection");
        assert.deepEqual(await residualSnapshot(), residualBaseline,
          "rejecting a derived proposal must leave declared mapping, effective overlay, T_acc, graph, reachability and trajectories unchanged");
        const rejectedStorage = await residualPage.evaluate(() =>
          Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:"))
            .map(k => localStorage.getItem(k)).filter(Boolean));
        assert.ok(rejectedStorage.some(raw => raw.includes('"decision":"REJECTED"')),
          "grouped rejection decision must be persisted");

        await residualPage.locator("#correspondence-review-list article").filter({hasText:"t_cd"})
          .getByRole("button", {name:"Aceptar propuesta"}).click();
        await residualPage.locator("#apply-accepted-tgcv-correspondences").click();
        await residualPage.waitForFunction(() =>
          document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
          null, {timeout:5000});
        const residualAfterFirstApply = await residualPage.evaluate(() => ({
          effective:(window.effectiveCorrespondenceState?.mappings || [])
            .filter(m => m.status === "EFFECTIVE" && m.active !== false)
            .map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort(),
          storage:Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:"))
            .sort().map(k => [k,localStorage.getItem(k)])
        }));
        assert.deepEqual(residualAfterFirstApply.effective, [["t_cd","T_CD"]],
          "only the newly accepted non-rejected mapping may become effective");
        await residualPage.locator("#apply-accepted-tgcv-correspondences").click();
        await residualPage.waitForFunction(() =>
          document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
          null, {timeout:5000});
        const residualAfterSecondApply = await residualPage.evaluate(() => ({
          effective:(window.effectiveCorrespondenceState?.mappings || [])
            .filter(m => m.status === "EFFECTIVE" && m.active !== false)
            .map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort(),
          storage:Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:"))
            .sort().map(k => [k,localStorage.getItem(k)])
        }));
        assert.deepEqual(residualAfterSecondApply, residualAfterFirstApply,
          "reapplying the same accepted mapping must leave effective mappings and persisted storage byte-for-byte unchanged");
        assert.match(await residualPage.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
          "idempotent application must preserve the rejected decision alongside the accepted mapping");
      } finally { await residualContext.close(); }
    } finally { await declaredDerivedCrossContext.close(); }

    // Cross-class conflict: a user-declared mapping claims a TGCV target that
    // would otherwise match a second system transition. The declared mapping wins;
    // the derivator must exclude the conflicting candidate before it can be accepted.
    const declaredTargetCollisionContext = await browser.newContext();
    try {
      const declaredCollisionPage = await declaredTargetCollisionContext.newPage();
      await declaredCollisionPage.goto("file://" + htmlPath);
      await declaredCollisionPage.locator("#load").click();
      const declaredCollisionModel = JSON.parse(JSON.stringify(model));
      declaredCollisionModel.model_id = "ui-declared-target-collision";
      declaredCollisionModel.initial_state = "A";
      declaredCollisionModel.states = ["A","B","C"];
      declaredCollisionModel.transitions = [
        {id:"t_ab_declared",source:"A",target:"B"},
        {id:"t_ab_competing",source:"A",target:"B"},
        {id:"t_bc_control",source:"B",target:"C"}
      ];
      declaredCollisionModel.relations = [];
      declaredCollisionModel.tgcv_mapping = {
        schema:"tgcv-declared-mapping-001",version:"1",
        mappings:[{system_transition_id:"t_ab_declared",tgcv_transformation_id:"T_SHARED_AB"}],
        relations:[]
      };
      const declaredCollisionBefore = JSON.parse(JSON.stringify(declaredCollisionModel.tgcv_mapping));
      await declaredCollisionPage.locator("#model").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, declaredCollisionModel);
      // Derivation is a graph-correspondence operation; do not require an execution
      // of a deliberately conflicting source graph before reviewing its candidates.
      const declaredCollisionDetails = declaredCollisionPage.locator("#correspondence-review-section details").filter({
        has: declaredCollisionPage.locator("#tgcv-target-catalogue")
      });
      if (!(await declaredCollisionDetails.evaluate(el => el.open))) await declaredCollisionDetails.locator("summary").click();
      await declaredCollisionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001",version:"ui-declared-target-collision-v1",
        transformations:[
          {id:"T_SHARED_AB",source_state:"A",target_state:"B"},
          {id:"T_BC_CONTROL",source_state:"B",target_state:"C"}
        ]
      });
      await declaredCollisionPage.locator("#derive-tgcv-correspondences").click();
      await declaredCollisionPage.waitForFunction(() =>
        /Generadas \d+ propuestas/i.test(document.querySelector("#correspondence-review-status")?.textContent || ""),
        null, {timeout:5000});
      const declaredCollisionEvidence = await declaredCollisionPage.evaluate(() => ({
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        candidates:window.correspondenceReviewState?.candidates || [],
        reviewStatus:document.querySelector("#correspondence-review-status")?.textContent || "",
        cards:document.querySelectorAll("#correspondence-review-list article").length
      }));
      assert.deepEqual(declaredCollisionEvidence.declared, declaredCollisionBefore,
        "derivation must not rewrite the exact user-declared mapping when another transition collides with its target");
      assert.equal(declaredCollisionEvidence.candidates.some(c =>
        c.system_transition_id === "t_ab_competing" && c.tgcv_transformation_id === "T_SHARED_AB"), false,
        "a derived candidate must never claim a target already owned by a declared mapping");
      assert.match(declaredCollisionEvidence.reviewStatus, /excluido[s]? 2 coincidencias por conflicto con correspondencias declaradas/i,
        "the cross-class conflict must be explicit in the UI exclusion evidence, not silently disappear");
      assert.ok(declaredCollisionEvidence.candidates.some(c =>
        c.system_transition_id === "t_bc_control" && c.tgcv_transformation_id === "T_BC_CONTROL"),
        "an unrelated exact-boundary candidate must remain derivable");
      const controlCard = declaredCollisionPage.locator("#correspondence-review-list article").filter({hasText:"t_bc_control"});
      await controlCard.getByRole("button", {name:"Aceptar propuesta"}).click();
      await declaredCollisionPage.locator("#apply-accepted-tgcv-correspondences").click();
      await declaredCollisionPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const declaredCollisionApplied = await declaredCollisionPage.evaluate(() => ({
        declared:JSON.parse(document.querySelector("#model").value).tgcv_mapping,
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => [m.system_transition_id,m.tgcv_transformation_id]).sort()
      }));
      assert.deepEqual(declaredCollisionApplied.declared, declaredCollisionBefore,
        "applying a non-conflicting derived mapping must leave the declared mapping unchanged");
      assert.deepEqual(declaredCollisionApplied.effective, [["t_bc_control","T_BC_CONTROL"]],
        "only the unrelated, explicitly accepted derived mapping may become effective");
      // Persistence is asserted against the declared source model only. Execution
      // and trajectory invariants are already covered by the separate grouped lifecycle
      // case; this deliberately conflicting duplicate-edge fixture is not executable.
      await declaredCollisionPage.reload();
      const restoredDeclaredCollision = await declaredCollisionPage.locator("#model").evaluate(el => {
        try { return JSON.parse(el.value); } catch (_e) { return null; }
      });
      assert.deepEqual(restoredDeclaredCollision, declaredCollisionModel,
        "native reload must restore the full declared-conflict source model without reinjection");
      assert.deepEqual(restoredDeclaredCollision?.tgcv_mapping, declaredCollisionBefore,
        "native reload must preserve the original declared mapping verbatim");
    } finally { await declaredTargetCollisionContext.close(); }

    // Integrated conflict lifecycle: two distinct system transitions map to one TGCV target.
    // Both are individually valid exact-boundary proposals, but cannot both become effective.
    const applyConflictContext = await browser.newContext();
    try {
      const conflictPage = await applyConflictContext.newPage();
      await conflictPage.goto("file://" + htmlPath);
      await conflictPage.locator("#load").click();
      await conflictPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-apply-conflict-lifecycle";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_primary",source:"A",target:"B"},
          {id:"t_ab_duplicate",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        return parsed;
      }, model);
      // Block B/C grouped invariant: establish an execution baseline before conflict review.
      await conflictPage.locator("#run").click();
      await conflictPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(conflictPage, "conflict lifecycle baseline");
      const catalogueDetails = conflictPage.locator("#correspondence-review-section details").filter({
        has: conflictPage.locator("#tgcv-target-catalogue")
      });
      if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
      await conflictPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"ui-apply-conflict-lifecycle-v1",
        transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
      });
      await conflictPage.locator("#derive-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const primaryCard = conflictPage.locator("#correspondence-review-list article").filter({hasText:"t_ab_primary"});
      const duplicateCard = conflictPage.locator("#correspondence-review-list article").filter({hasText:"t_ab_duplicate"});
      await primaryCard.getByRole("button", {name:"Aceptar propuesta"}).click();
      await duplicateCard.getByRole("button", {name:"Aceptar propuesta"}).click();
      await conflictPage.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "conflict-needs-review",
        null, {timeout:5000});
      const conflictState = await conflictPage.evaluate(() => ({
        status:document.querySelector("#effective-correspondence-status")?.textContent || "",
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false),
        storage:Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:"))
          .map(k => JSON.parse(localStorage.getItem(k))).filter(Boolean)
      }));
      assert.match(conflictState.status, /CONFLICT_NEEDS_REVIEW/);
      assert.equal(conflictState.mappings.length, 0,
        "an unresolved apply-time target collision must fail closed and activate no mappings");
      assert.ok(conflictState.storage.every(record => (record.mappings || []).length === 0),
        "the persisted effective layer must contain no mappings while the conflict is unresolved");
      await conflictPage.locator("#run").click();
      await conflictPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(conflictPage, "unresolved conflict fails closed");

      await duplicateCard.getByRole("button", {name:"Rechazar propuesta"}).click();
      const persistedDecisions = await conflictPage.evaluate(() => Object.keys(localStorage)
        .filter(k => k.startsWith("tgcv-correspondence-review-001:"))
        .map(k => JSON.parse(localStorage.getItem(k)))
        .filter(Boolean)
        .flatMap(record => Object.values(record.decisions || {})));
      assert.ok(persistedDecisions.some(d => d.candidate_id && d.decision === "ACCEPTED"),
        "the selected correspondence decision must be persisted");
      assert.ok(persistedDecisions.some(d => d.candidate_id && d.decision === "REJECTED"),
        "the explicit conflict resolution must persist the rejected candidate decision");
      await conflictPage.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const resolvedState = await conflictPage.evaluate(() => ({
        status:document.querySelector("#effective-correspondence-status")?.textContent || "",
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.match(resolvedState.status, /conflictos: 0/);
      assert.equal(resolvedState.mappings.length, 1,
        "explicitly rejecting one conflicting proposal must leave only the selected mapping effective");
      assert.equal(resolvedState.mappings[0].system_transition_id, "t_ab_primary");
      await conflictPage.locator("#run").click();
      await conflictPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(conflictPage, "conflict resolved by explicit rejection");
      const resolvedExecutionBeforeReload = await conflictPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      // Reapplying the same accepted scope must be idempotent.
      await conflictPage.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified",
        null, {timeout:5000});
      const reappliedState = await conflictPage.evaluate(() => ({
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false),
        storage:Object.keys(localStorage).filter(k => k.startsWith("tgcv-effective-mappings-001:"))
          .map(k => JSON.parse(localStorage.getItem(k))).filter(Boolean)
      }));
      assert.equal(reappliedState.mappings.length, 1,
        "reapplying the same accepted mapping must not create duplicate effective entries");
      assert.ok(reappliedState.storage.every(record => (record.mappings || []).length === 1),
        "the persisted effective overlay must remain deduplicated after reapplication");

      // Reload the page and rebuild the exact same model/catalogue scope.
      // The explicit rejection must be restored, not silently forgotten.
      await conflictPage.reload();
      await conflictPage.locator("#load").click();
      await conflictPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-apply-conflict-lifecycle";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_primary",source:"A",target:"B"},
          {id:"t_ab_duplicate",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const reloadCatalogueDetails = conflictPage.locator("#correspondence-review-section details").filter({
        has: conflictPage.locator("#tgcv-target-catalogue")
      });
      if (!(await reloadCatalogueDetails.evaluate(el => el.open))) await reloadCatalogueDetails.locator("summary").click();
      await conflictPage.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001", version:"ui-apply-conflict-lifecycle-v1",
          transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await conflictPage.locator("#derive-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const reloadedDecisions = await conflictPage.evaluate(() => {
        const records = Object.keys(localStorage)
          .filter(key => key.startsWith("tgcv-correspondence-review-001:"))
          .map(key => JSON.parse(localStorage.getItem(key))).filter(Boolean);
        const decisions = records.flatMap(record => Object.values(record.decisions || {}));
        return {
          accepted:decisions.some(d => d.candidate_id && d.decision === "ACCEPTED"),
          rejected:decisions.some(d => d.candidate_id && d.decision === "REJECTED")
        };
      });
      assert.equal(reloadedDecisions.accepted, true,
        "the accepted decision must survive page reload in the same model/catalogue scope");
      assert.equal(reloadedDecisions.rejected, true,
        "the rejected conflict decision must survive page reload in the same model/catalogue scope");
      await conflictPage.locator("#apply-accepted-tgcv-correspondences").click();
      await conflictPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const afterReloadApply = await conflictPage.evaluate(() => ({
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.equal(afterReloadApply.mappings.length, 1,
        "reapplying after reload must keep exactly one effective mapping");
      assert.equal(afterReloadApply.mappings[0].system_transition_id, "t_ab_primary",
        "the rejected conflicting mapping must not become effective after reload");
      await conflictPage.locator("#run").click();
      await conflictPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const resolvedExecutionAfterReload = await conflictPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      assert.deepEqual(resolvedExecutionAfterReload, resolvedExecutionBeforeReload,
        "reloading and reapplying the persisted conflict resolution must preserve execution trajectories");
      await assertStructuredTAccMatchesExecution(conflictPage, "conflict resolution after reload");
    } finally { await applyConflictContext.close(); }

    // Symmetric UI conflict-resolution case: reverse which candidate is accepted
    // first and retained. This complements the direct validator order-invariance
    // checks with the user-facing apply/reject/persist/reload lifecycle.
    const reverseConflictContext = await browser.newContext();
    try {
      const reversePage = await reverseConflictContext.newPage();
      await reversePage.goto("file://" + htmlPath);
      await reversePage.locator("#load").click();
      await reversePage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-reverse-apply-conflict-lifecycle";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_primary",source:"A",target:"B"},
          {id:"t_ab_duplicate",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        parsed.scenarios = [{id:"baseline",disabled_transitions:[]}];
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      await reversePage.locator("#run").click();
      await reversePage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(reversePage, "reverse-order conflict baseline");
      const reverseDetails = reversePage.locator("#correspondence-review-section details").filter({
        has: reversePage.locator("#tgcv-target-catalogue")
      });
      if (!(await reverseDetails.evaluate(el => el.open))) await reverseDetails.locator("summary").click();
      await reversePage.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001",version:"ui-reverse-apply-conflict-v1",
          transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await reversePage.locator("#derive-tgcv-correspondences").click();
      await reversePage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const reversePrimary = reversePage.locator("#correspondence-review-list article").filter({hasText:"t_ab_primary"});
      const reverseDuplicate = reversePage.locator("#correspondence-review-list article").filter({hasText:"t_ab_duplicate"});
      await reverseDuplicate.getByRole("button", {name:"Aceptar propuesta"}).click();
      await reversePrimary.getByRole("button", {name:"Aceptar propuesta"}).click();
      await reversePage.locator("#apply-accepted-tgcv-correspondences").click();
      await reversePage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "conflict-needs-review",
        null, {timeout:5000});
      const reverseBlocked = await reversePage.evaluate(() => ({
        status:document.querySelector("#effective-correspondence-status")?.textContent || "",
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
      }));
      assert.match(reverseBlocked.status, /CONFLICT_NEEDS_REVIEW/);
      assert.equal(reverseBlocked.mappings.length, 0,
        "reversing candidate acceptance order must still fail closed on an unresolved collision");
      await reversePrimary.getByRole("button", {name:"Rechazar propuesta"}).click();
      await reversePage.locator("#apply-accepted-tgcv-correspondences").click();
      await reversePage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const reverseResolved = await reversePage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
      );
      assert.deepEqual(reverseResolved, [{system_transition_id:"t_ab_duplicate",tgcv_transformation_id:"T_SHARED_AB"}],
        "explicitly rejecting the primary candidate must leave the accepted duplicate as the only effective mapping");
      await reversePage.locator("#run").click();
      await reversePage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(reversePage, "reverse-order conflict resolved");
      const reverseExecutionBeforeReload = await reversePage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id,result]) => [id,{
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          })))
        }]));
      });
      await reversePage.reload();
      await reversePage.locator("#load").click();
      await reversePage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-reverse-apply-conflict-lifecycle";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [
          {id:"t_ab_primary",source:"A",target:"B"},
          {id:"t_ab_duplicate",source:"A",target:"B"}
        ];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        parsed.scenarios = [{id:"baseline",disabled_transitions:[]}];
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const reverseReloadDetails = reversePage.locator("#correspondence-review-section details").filter({
        has: reversePage.locator("#tgcv-target-catalogue")
      });
      if (!(await reverseReloadDetails.evaluate(el => el.open))) await reverseReloadDetails.locator("summary").click();
      await reversePage.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001",version:"ui-reverse-apply-conflict-v1",
          transformations:[{id:"T_SHARED_AB",source_state:"A",target_state:"B"}]
        }, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await reversePage.locator("#derive-tgcv-correspondences").click();
      await reversePage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      await reversePage.locator("#apply-accepted-tgcv-correspondences").click();
      await reversePage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const reverseAfterReload = await reversePage.evaluate(() =>
        (window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
      );
      assert.deepEqual(reverseAfterReload, reverseResolved,
        "reverse-order resolution must persist the selected mapping across reload");
      await reversePage.locator("#run").click();
      await reversePage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const reverseExecutionAfterReload = await reversePage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id,result]) => [id,{
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({
            state:step.state,transition:step.transition || null
          })))
        }]));
      });
      assert.deepEqual(reverseExecutionAfterReload, reverseExecutionBeforeReload,
        "reverse-order conflict resolution must preserve trajectories across reload");
      await assertStructuredTAccMatchesExecution(reversePage, "reverse-order conflict after reload");
    } finally { await reverseConflictContext.close(); }

    // Orthogonal ambiguity axis: one source transition with two exact-boundary
    // target matches must remain NEEDS_REVIEW; neither candidate may be accepted
    // or materialized while the target choice is ambiguous.
    const sourceCollisionContext = await browser.newContext();
    try {
      const sourceCollisionPage = await sourceCollisionContext.newPage();
      await sourceCollisionPage.goto("file://" + htmlPath);
      await sourceCollisionPage.locator("#load").click();
      await sourceCollisionPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-source-target-ambiguity";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [{id:"t_ab_single",source:"A",target:"B"}];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        return parsed;
      }, model);
      // Establish an execution baseline before exposing the ambiguous candidates.
      await sourceCollisionPage.locator("#run").click();
      await sourceCollisionPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const ambiguityBaselineExecution = await sourceCollisionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      await assertStructuredTAccMatchesExecution(sourceCollisionPage, "single-source ambiguity baseline");
      const catalogueDetails = sourceCollisionPage.locator("#correspondence-review-section details").filter({
        has: sourceCollisionPage.locator("#tgcv-target-catalogue")
      });
      if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
      await sourceCollisionPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"ui-source-target-ambiguity-v1",
        transformations:[
          {id:"T_SOURCE_AB_1",source_state:"A",target_state:"B"},
          {id:"T_SOURCE_AB_2",source_state:"A",target_state:"B"}
        ]
      });
      await sourceCollisionPage.locator("#derive-tgcv-correspondences").click();
      await sourceCollisionPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      const ambiguity = await sourceCollisionPage.evaluate(() => ({
        cards:[...document.querySelectorAll("#correspondence-review-list article")].map(card => ({
          text:card.textContent || "",
          acceptDisabled:!!card.querySelector('button[aria-label="Aceptar propuesta"]:disabled') ||
            [...card.querySelectorAll("button")].some(button => /Aceptar propuesta/.test(button.textContent || "") && button.disabled)
        })),
        effective:(window.effectiveCorrespondenceState?.mappings || [])
          .filter(mapping => mapping.status === "EFFECTIVE" && mapping.active !== false),
        persisted:Object.keys(localStorage).filter(key => key.startsWith("tgcv-effective-mappings-001:"))
          .map(key => JSON.parse(localStorage.getItem(key))).filter(Boolean)
      }));
      assert.equal(ambiguity.cards.length, 2,
        "one transition with two exact-boundary targets must expose both review candidates");
      assert.ok(ambiguity.cards.every(card => /NEEDS_REVIEW/.test(card.text)),
        "multiple exact-boundary targets for one transition must remain review-required");
      assert.ok(ambiguity.cards.every(card => card.acceptDisabled),
        "ambiguous candidates must not offer an enabled Accept action");
      assert.equal(ambiguity.effective.length, 0,
        "ambiguous source-transition candidates must not materialize as effective mappings");
      assert.ok(ambiguity.persisted.every(record => (record.mappings || []).length === 0),
        "ambiguous source-transition candidates must persist no active effective mapping");
      await sourceCollisionPage.locator("#run").click();
      await sourceCollisionPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const ambiguityExecutionAfterDerivation = await sourceCollisionPage.evaluate(() => {
        const scenarios = window.lastPackage?.result?.scenario_results || {};
        return Object.fromEntries(Object.entries(scenarios).map(([id, result]) => [id, {
          reachable_states: [...(result.reachable_states || [])].sort(),
          trajectories: (result.trajectories || []).map(path => path.map(step => ({
            state: step.state, transition: step.transition || null
          })))
        }]));
      });
      assert.deepEqual(ambiguityExecutionAfterDerivation, ambiguityBaselineExecution,
        "deriving unresolved single-source ambiguity must not alter reachable states or execution trajectories");
      await assertStructuredTAccMatchesExecution(sourceCollisionPage, "single-source ambiguity unresolved");
    } finally { await sourceCollisionContext.close(); }

    // Integrated resolution path: disambiguate by refining the declared target catalogue,
    // then explicitly accept/apply the unique candidate and verify execution + reload.
    const resolvedSourceAmbiguityContext = await browser.newContext();
    try {
      const resolvedPage = await resolvedSourceAmbiguityContext.newPage();
      await resolvedPage.goto("file://" + htmlPath);
      await resolvedPage.locator("#load").click();
      await resolvedPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-source-target-ambiguity-resolved";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [{id:"t_ab_single",source:"A",target:"B"}];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const catalogueDetails = resolvedPage.locator("#correspondence-review-section details").filter({
        has: resolvedPage.locator("#tgcv-target-catalogue")
      });
      if (!(await catalogueDetails.evaluate(el => el.open))) await catalogueDetails.locator("summary").click();
      const setCatalogue = async transformations => resolvedPage.locator("#tgcv-target-catalogue").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      }, {
        schema:"tgcv-target-catalogue-001", version:"ui-source-target-ambiguity-resolution-v1",
        transformations
      });
      await setCatalogue([
        {id:"T_SOURCE_AB_1",source_state:"A",target_state:"B"},
        {id:"T_SOURCE_AB_2",source_state:"A",target_state:"B"}
      ]);
      await resolvedPage.locator("#derive-tgcv-correspondences").click();
      await resolvedPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 2,
        null, {timeout:5000});
      assert.ok(await resolvedPage.locator("#correspondence-review-list").innerText().then(t => /NEEDS_REVIEW/.test(t)),
        "duplicate exact-boundary targets must initially require disambiguation");
      await setCatalogue([{id:"T_SOURCE_AB_1",source_state:"A",target_state:"B"}]);
      await resolvedPage.locator("#derive-tgcv-correspondences").click();
      await resolvedPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 1,
        null, {timeout:5000});
      const uniqueCandidate = resolvedPage.locator("#correspondence-review-list article").first();
      assert.match(await uniqueCandidate.innerText(), /PROPOSED/,
        "catalogue refinement to one exact-boundary target must produce one reviewable proposal");
      const acceptUnique = uniqueCandidate.getByRole("button", {name:"Aceptar propuesta"});
      assert.equal(await acceptUnique.isDisabled(), false,
        "the uniquely disambiguated candidate must permit explicit acceptance");
      await acceptUnique.click();
      await resolvedPage.locator("#apply-accepted-tgcv-correspondences").click();
      await resolvedPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      await resolvedPage.locator("#run").click();
      await resolvedPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      await assertStructuredTAccMatchesExecution(resolvedPage, "source ambiguity resolved by catalogue refinement");
      const resolvedBeforeReload = await resolvedPage.evaluate(() => ({
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id})),
        scenarios:Object.fromEntries(Object.entries(window.lastPackage?.result?.scenario_results || {}).map(([id, result]) => [id, {
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({state:step.state,transition:step.transition || null})))
        }]))
      }));
      await resolvedPage.reload();
      await resolvedPage.locator("#load").click();
      await resolvedPage.locator("#model").evaluate((el, value) => {
        const parsed = JSON.parse(JSON.stringify(value));
        parsed.model_id = "ui-source-target-ambiguity-resolved";
        parsed.initial_state = "A";
        parsed.states = ["A","B"];
        parsed.transitions = [{id:"t_ab_single",source:"A",target:"B"}];
        parsed.relations = [];
        delete parsed.tgcv_mapping;
        el.value = JSON.stringify(parsed, null, 2);
        el.dispatchEvent(new Event("input", {bubbles:true}));
      }, model);
      const reloadedDetails = resolvedPage.locator("#correspondence-review-section details").filter({
        has: resolvedPage.locator("#tgcv-target-catalogue")
      });
      if (!(await reloadedDetails.evaluate(el => el.open))) await reloadedDetails.locator("summary").click();
      await resolvedPage.locator("#tgcv-target-catalogue").evaluate(el => {
        el.value = JSON.stringify({
          schema:"tgcv-target-catalogue-001", version:"ui-source-target-ambiguity-resolution-v1",
          transformations:[{id:"T_SOURCE_AB_1",source_state:"A",target_state:"B"}]
        }, null, {bubbles:true});
        el.dispatchEvent(new Event("input", {bubbles:true}));
        el.dispatchEvent(new Event("change", {bubbles:true}));
      });
      await resolvedPage.locator("#derive-tgcv-correspondences").click();
      await resolvedPage.waitForFunction(() =>
        document.querySelectorAll("#correspondence-review-list article").length === 1,
        null, {timeout:5000});
      await resolvedPage.locator("#apply-accepted-tgcv-correspondences").click();
      await resolvedPage.waitForFunction(() =>
        document.querySelector("#effective-correspondence-status")?.dataset.state === "replay-verified" &&
        /Correspondencias efectivas activas: 1\./.test(document.querySelector("#effective-correspondence-status")?.textContent || ""),
        null, {timeout:5000});
      const resolvedAfterReload = await resolvedPage.evaluate(() => ({
        mappings:(window.effectiveCorrespondenceState?.mappings || []).filter(m => m.status === "EFFECTIVE" && m.active !== false)
          .map(m => ({system_transition_id:m.system_transition_id,tgcv_transformation_id:m.tgcv_transformation_id}))
      }));
      assert.deepEqual(resolvedAfterReload.mappings, resolvedBeforeReload.mappings,
        "the explicitly resolved mapping must remain effective after reload");
      await resolvedPage.locator("#run").click();
      await resolvedPage.waitForFunction(() => /ejecución completada/i.test(
        document.querySelector("#status")?.textContent || ""
      ), null, {timeout:5000});
      const executionAfterReload = await resolvedPage.evaluate(() =>
        Object.fromEntries(Object.entries(window.lastPackage?.result?.scenario_results || {}).map(([id, result]) => [id, {
          reachable_states:[...(result.reachable_states || [])].sort(),
          trajectories:(result.trajectories || []).map(path => path.map(step => ({state:step.state,transition:step.transition || null})))
        }]))
      );
      assert.deepEqual(executionAfterReload, resolvedBeforeReload.scenarios,
        "explicit ambiguity resolution must preserve execution trajectories after reload");
      await assertStructuredTAccMatchesExecution(resolvedPage, "resolved source ambiguity after reload");
    } finally { await resolvedSourceAmbiguityContext.close(); }

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
