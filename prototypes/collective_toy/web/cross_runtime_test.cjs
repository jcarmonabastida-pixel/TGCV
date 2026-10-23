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
      const conflict = await window.validateAcceptedCorrespondenceCandidates(conflictingModel,catalogue,conflictCandidate.candidates,[]);
      const staleModel = {...unMapped,model_id:"changed-after-review"};
      const stale = await window.validateAcceptedCorrespondenceCandidates(staleModel,catalogue,derived.candidates,[]);
      return {before,after:JSON.stringify(unMapped),first,second,conflict,stale};
    }, explicitlyMappedModel);
    assert.equal(materialization.before, materialization.after, "materialization must not rewrite the input model");
    assert.equal(materialization.first.mappings.length, 1, "one accepted exact match should materialize as effective");
    assert.equal(materialization.first.mappings[0].status, "EFFECTIVE");
    assert.equal(materialization.first.mappings[0].provenance, "derived-and-accepted");
    assert.equal(materialization.second.mappings[0].mapping_id, materialization.first.mappings[0].mapping_id,
      "applying the same accepted candidate twice must be idempotent");
    assert.equal(materialization.conflict.mappings.length, 0, "declared mapping conflicts must never be overwritten");
    assert.equal(materialization.conflict.conflicts[0].code, "CONFLICT_NEEDS_REVIEW");
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
    const graphBeforeReview = await page.locator("#tgcv-graph").textContent();
    await page.locator("#derive-tgcv-correspondences").click();
    await page.locator("#correspondence-review-list article").first().waitFor();
    assert.equal(await page.locator("#correspondence-review-list article").count(), 2,
      "review UI must show all exact-boundary candidates");
    await page.locator("#correspondence-review-list article").nth(0).getByRole("button", {name:"Aceptar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-status").textContent(), /persistida/i,
      "acceptance must report that the decision was persisted");
    await page.locator("#correspondence-review-list article").nth(1).getByRole("button", {name:"Rechazar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: REJECTED/,
      "a rejected correspondence candidate must retain an explicit human decision");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "rejecting a candidate must not modify the TGCV graph");
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
    await page.locator("#derive-tgcv-correspondences").click();
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
    await page.locator("#correspondence-review-list article").first().getByRole("button", {name:"Aceptar propuesta"}).click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: ACCEPTED/,
      "human review decision for a transcribed candidate must be explicit");

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
