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

    // Candidate discovery must not duplicate user-declared correspondences.
    const reviewModel = {
      ...explicitlyMappedModel,
      tgcv_mapping: {...explicitlyMappedModel.tgcv_mapping, mappings: []}
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
    await page.locator("#correspondence-review-section summary").click();
    await page.locator("#tgcv-target-catalogue").fill(JSON.stringify({
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
    const persistedReview = await page.evaluate(() => Object.keys(localStorage).filter(k => k.startsWith("tgcv-correspondence-review-001:")).map(k => JSON.parse(localStorage.getItem(k))));
    assert.equal(persistedReview.length, 1, "review decision must be persisted in browser storage");
    assert.equal(Object.values(persistedReview[0].decisions)[0].decision, "ACCEPTED",
      "accepted decision must be retrievable with its model/catalogue scope");
    assert.equal(await page.locator("#tgcv-graph").textContent(), graphBeforeReview,
      "accepting a candidate must not apply it to the TGCV graph automatically");
    await page.locator("#derive-tgcv-correspondences").click();
    assert.match(await page.locator("#correspondence-review-list").textContent(), /Decisión: ACCEPTED/,
      "a persisted decision must be restored when regenerating candidates for the same model/catalogue");
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
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const visuallyEditedPackage = await page.evaluate(() => window.lastPackage);
    assert.ok(!visuallyEditedPackage.result.scenario_results.baseline.reachable_states.includes("B"),
      "a visually edited condition must remain blocked until re-evaluated");
    assert.match(await page.locator("#graph-note").textContent(), /t_ab \(NO EVALUADA\)/,
      "the graph note must show the edited condition as unevaluated");
    assert.doesNotMatch(await page.locator("#tgcv-graph").textContent(), /T_HUMIDITY/,
      "the old accepted mapping must not make a now-blocked transition accessible after its condition changes");

    // Clearing a condition must remove its metadata and stale evaluation, restoring an unconditional transition.
    await page.locator('#transition-review-list input[data-condition-text="t_ab"]').fill("");
    await page.locator('#transition-review-list button[data-save-condition="t_ab"]').click();
    const visuallyClearedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(visuallyClearedModel.transitions.find(t => t.id === "t_ab").condition, undefined,
      "clearing the visual condition must remove condition metadata");
    assert.equal(visuallyClearedModel.scenarios[0].condition_evaluations?.t_ab, undefined,
      "clearing the condition must also remove its scenario evaluation");
    await page.locator("#run").click();
    await page.locator("#status").filter({hasText:/completad/i}).waitFor({timeout:5000});
    const visuallyClearedPackage = await page.evaluate(() => window.lastPackage);
    assert.ok(visuallyClearedPackage.result.scenario_results.baseline.reachable_states.includes("B"),
      "a cleared condition must behave as an unconditional transition");
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
