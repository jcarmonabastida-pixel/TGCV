const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");

(async () => {
  const htmlPath = path.resolve(__dirname, "index.html");
  assert.ok(fs.existsSync(htmlPath), "Collective Toy UI must exist");

  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto("file://" + htmlPath);

    // Keep the MVP's state-local graph semantics and non-scientific boundary visible.
    const notice = await page.locator(".notice").innerText();
    assert.match(notice, /grafo finito/i);
    assert.match(notice, /No procesa datos reales/i);
    assert.match(notice, /No es una validación científica/i);
    assert.match(notice, /ni implementa por sí solo Tacc de TGCV/i);

    // FC5-SEC-001/002: unkeyed SHA-256 is consistency/reproducibility evidence,
    // never proof of who produced a package or external origin authenticity.
    const securityFooter = await page.locator("footer").innerText();
    assert.match(securityFooter, /hashes apoyan la reproducibilidad/i);
    assert.match(securityFooter, /no certifican la integridad externa/i);
    assert.doesNotMatch(securityFooter, /SHA-?256.{0,50}(autentica|autenticidad|firma|origen autenticado)/i,
      "FC5-SEC-002: UI must not claim unkeyed SHA-256 authenticates a package or its origin");
    const importerSource = fs.readFileSync(htmlPath, "utf8");
    assert.match(importerSource, /esto no autentica el origen ni demuestra la corrección del resultado/i,
      "FC5-SEC-001: import/replay status must distinguish internal hash consistency from origin authenticity");

    // OCR image upload accepts supported formats, rejects unsupported/oversized files, and keeps OCR failures recoverable.
    const imageInput = page.locator("#image-file");
    await imageInput.setInputFiles({ name: "reference.png", mimeType: "image/png", buffer: Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jW5sAAAAASUVORK5CYII=", "base64") });
    await page.locator("#image-preview:not([hidden])").waitFor();
    assert.match(await page.locator("#image-status").innerText(), /OCR opcional|OCR/i);
    assert.equal(await page.locator("#clear-image").isEnabled(), true);
    assert.equal(await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).isEnabled(), true);
    // Stub the OCR engine to test the browser integration deterministically without network access.
    await page.evaluate(() => { window.Tesseract = { recognize: async (image, language) => { if (language !== "spa+eng") throw new Error("Unexpected OCR language"); if (!image || !String(image).startsWith("data:image/")) throw new Error("OCR did not receive the uploaded image data URL"); return { data: { text: "Nodo A\\nNodo B\\nA --> B" } }; } }; });
    await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).click();
    await page.locator("#image-status").filter({ hasText: /OCR completado/ }).waitFor();
    assert.match(await page.locator("#image-transcription").inputValue(), /A --> B/);
    // Empty OCR output must fail visibly and must not overwrite the last reviewed transcription.
    await page.evaluate(() => { window.Tesseract = { recognize: async () => ({ data: { text: "   " } }) }; });
    await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).click();
    await page.locator("#image-status").filter({ hasText: /No se pudo completar el OCR.*No se detectó texto legible/i }).waitFor();
    assert.match(await page.locator("#image-transcription").inputValue(), /A --> B/);
    // Library failure must also be surfaced to the user without a stuck disabled button.
    await page.evaluate(() => { window.Tesseract = { recognize: async () => { throw new Error("synthetic OCR failure"); } }; });
    await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).click();
    await page.locator("#image-status").filter({ hasText: /synthetic OCR failure/i }).waitFor();
    assert.equal(await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).isEnabled(), true);
    await page.getByRole("button", { name: "Quitar imagen" }).click();
    assert.equal(await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).isEnabled(), false);
    assert.equal(await page.locator("#image-preview").isVisible(), false);
    await imageInput.setInputFiles({ name: "reference.svg", mimeType: "image/svg+xml", buffer: Buffer.from("<svg xmlns=\"http://www.w3.org/2000/svg\"></svg>") });
    assert.match(await page.locator("#image-status").innerText(), /Formato no admitido/i);
    await imageInput.setInputFiles({ name: "oversized.png", mimeType: "image/png", buffer: Buffer.alloc(5 * 1024 * 1024 + 1, 0x20) });
    assert.match(await page.locator("#image-status").innerText(), /supera el límite de 5 MiB/i);

    // Preserve the canonical fixture: transcription import intentionally replaces the editor model.
    const modelBeforeTranscription = await page.locator("#model").inputValue();
    // Image transcription is user-supplied text, converted only into a reviewable draft.
    await page.locator("#image-transcription").fill("A --> B" + String.fromCharCode(10) + "B --> C");
    await page.getByRole("button", { name: "Convertir en borrador de grafo" }).click();
    await page.locator("#transcription-status").filter({ hasText: /Borrador creado: 3 estados y 2 conexiones/ }).waitFor();
    const transcriptionDraft = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(transcriptionDraft.states, ["A", "B", "C"]);
    assert.equal(transcriptionDraft.transitions.length, 2);
    assert.match(await page.locator("#transcription-status").innerText(), /Revisa el grafo/i);
    await page.locator("#image-transcription").fill("texto sin conexiones");
    await page.getByRole("button", { name: "Convertir en borrador de grafo" }).click();
    assert.match(await page.locator("#transcription-status").innerText(), /No se encontraron conexiones dirigidas/i);
    await page.getByRole("button", { name: "Borrar transcripción" }).click();
    assert.equal(await page.locator("#image-transcription").inputValue(), "");
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, modelBeforeTranscription);

    // Manual graph review: enumerate edges, remove an incorrect edge, and flag duplicate pairs.
    const reviewModel = JSON.parse(await page.locator("#model").inputValue());
    reviewModel.states = ["A", "B", "C", "D"];
    reviewModel.initial_state = "A";
    reviewModel.relations = [];
    reviewModel.scenarios = reviewModel.scenarios.map((scenario) => ({ ...scenario, disabled_transitions: [] }));
    reviewModel.transitions = [
      { id: "review_ab", source: "A", target: "B" },
      { id: "review_ab_duplicate", source: "A", target: "B" },
      { id: "review_bc", source: "B", target: "C" }
    ];
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, JSON.stringify(reviewModel, null, 2));
    await page.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión review_ab_duplicate/ }).click();
    const removalStatus = await page.locator("#graph-edit-status").innerText();
    assert.match(removalStatus, /Conexión eliminada: review_ab_duplicate/, "Edge removal must be accepted by model validation; status: " + removalStatus);
    let reviewed = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(reviewed.transitions.length, 2);
    assert.doesNotMatch(await page.locator("#graph-review-warnings").innerText(), /par\(es\).*duplicado/i);
    await page.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión review_bc/ }).click();
    reviewed = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(reviewed.transitions.length, 1);
    assert.match(await page.locator("#graph-review-warnings").innerText(), /solo hay una conexión/i);
    assert.match(await page.locator("#graph-review-warnings").innerText(), /estados aislados/i);

    // Output labels must not silently promote graph-local results to system-level TGCV claims.
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.getByText("Estados alcanzables en baseline", { exact: true }).waitFor();
    await page.getByText("Trayectorias enumeradas", { exact: true }).first().waitFor();
    await page.getByText("Límite alcanzado", { exact: true }).waitFor();
    await page.getByText("Escenario: baseline", { exact: true }).waitFor();

    const packageData = await page.evaluate(() => window.lastPackage);
    assert.ok(packageData, "A successful run must produce an inspectable package");
    assert.equal(
      packageData.result.scientific_interpretation,
      "NONE: synthetic model execution only; no empirical or TGCV validity claim."
    );
    assert.equal(packageData.input.rule_profile.type, "finite_deterministic_graph");

    // Exercise JSON model-file import, including validation feedback and relation-profile sync.
    const modelForFileImport = await page.locator("#model").inputValue();
    await page.locator("#json-file").setInputFiles({
      name: "collective-toy-model.json",
      mimeType: "application/json",
      buffer: Buffer.from(modelForFileImport)
    });
    await page.locator("#file-status").filter({ hasText: "Archivo cargado" }).waitFor();
    assert.deepEqual(
      JSON.parse(await page.locator("#model").inputValue()),
      JSON.parse(modelForFileImport),
      "Imported JSON model must be preserved in the editor"
    );
    await page.locator("#json-file").setInputFiles({
      name: "invalid-model.json",
      mimeType: "application/json",
      buffer: Buffer.from("{ invalid JSON")
    });
    await page.locator("#file-status").filter({ hasText: "No se pudo cargar el JSON" }).waitFor();

    // Layout selection must redraw the graph; zoom must change the SVG viewBox and fit must restore it.
    await page.locator("#layout-mode").selectOption("circular");
    await page.locator("#graph-note").filter({ hasText: "disposición circular" }).waitFor();
    const originalViewBox = (await page.locator("#graph").getAttribute("viewBox")).split(" ").map(Number);
    await page.getByRole("button", { name: "Acercar grafo" }).click();
    const zoomViewBox = (await page.locator("#graph").getAttribute("viewBox")).split(" ").map(Number);
    assert.ok(zoomViewBox[2] < originalViewBox[2], "Zoom-in must reduce the visible graph width");
    await page.getByRole("button", { name: "Encuadrar todo" }).click();
    assert.deepEqual(
      (await page.locator("#graph").getAttribute("viewBox")).split(" ").map(Number),
      originalViewBox,
      "Fit-to-view must restore the complete graph"
    );
    await page.locator("#layout-mode").selectOption("auto");

    // Profile 1 is the default; selecting profile 2 then returning to profile 1
    // must preserve the relation as metadata without silently retaining an operative profile.
    assert.equal(await page.locator("#profile-editor").inputValue(), "1");
    await page.locator("#profile-editor").selectOption("2");
    await page.locator("#profile-editor").selectOption("1");
    const model = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(model.rule_profile, { type: "finite_deterministic_graph", version: "1" });
    assert.match(await page.locator("#relation-help").innerText(), /metadatos|perfil 2/i);

    // Verify the real export button produces a readable package, not only window state.
    const downloadPromise = page.waitForEvent("download");
    await page.getByRole("button", { name: "Exportar entrada y resultados (JSON)" }).click();
    const download = await downloadPromise;
    assert.match(download.suggestedFilename(), /-run\.json$/);
    const exportedText = fs.readFileSync(await download.path(), "utf8");
    const exportedPackage = JSON.parse(exportedText);
    const expectedExport = structuredClone(packageData);
    expectedExport.value_assessment_status = "NOT_ASSESSED";
    delete expectedExport.package_sha256;
    delete exportedPackage.package_sha256;
    assert.deepEqual(exportedPackage, expectedExport,
      "Downloaded JSON must match the inspectable package plus explicit FC-4 NOT_ASSESSED status");
    assert.match(JSON.parse(exportedText).package_sha256, /^[0-9a-f]{64}$/,
      "FC-4 export must hash the complete exported package");
    assert.equal(exportedPackage.package_version, "collective-toy-browser-run-002",
      "FC-5: exports must use the explicitly versioned package schema");
    assert.equal(exportedPackage.package_stage, "EXPLORATION",
      "FC-5: a package without a concrete trace must identify the exploration stage");

    // Exercise the actual import UI with the package produced by the export button.
    await page.locator("#package-file").setInputFiles({
      name: download.suggestedFilename(),
      mimeType: "application/json",
      buffer: Buffer.from(exportedText)
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i);

    // A structurally valid, self-consistent package from an unknown engine is inspect-only.
    const unknownEnginePackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.engine_version = "collective-toy-engine-future-999";
      candidate.value_assessment_status = "NOT_ASSESSED";
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody);
      const packageBody = structuredClone(candidate);
      delete packageBody.package_sha256;
      candidate.package_sha256 = await window.hash(packageBody);
      return candidate;
    }, packageData);
    await page.locator("#package-file").setInputFiles({
      name: "unknown-engine-run.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownEnginePackage))
    });
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "idle");
    assert.match(await page.locator("#package-assessment").innerText(), /Archivo seleccionado/i);
    assert.doesNotMatch(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i);
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"inspect-only/replay-unavailable"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /no se ha intentado reproducir/i);
    assert.doesNotMatch(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i);

    // A changed result with stale package/result hashes must fail closed.
    const tamperedPackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment_status = "NOT_ASSESSED";
      candidate.result.scientific_interpretation += " tampered";
      candidate.result.semantic_sha256 = await window.hash(
        window.semanticResultProjection(candidate.result)
      );
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody);
      return candidate;
    }, packageData);
    await page.locator("#package-file").setInputFiles({
      name: "tampered-run.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(tamperedPackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /hash del paquete no coincide/i);


    // GT-05 replay-mismatch adversary: all hashes are internally consistent, but the result is not reproducible from the input.
    const selfConsistentDivergence = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment_status = "NOT_ASSESSED";
      candidate.result.scientific_interpretation += " divergent-but-rehashed";
      candidate.result.semantic_sha256 = await window.hash(window.semanticResultProjection(candidate.result));
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody);
      const packageBody = structuredClone(candidate);
      delete packageBody.package_sha256;
      candidate.package_sha256 = await window.hash(packageBody);
      return candidate;
    }, packageData);
    await page.locator("#package-file").setInputFiles({
      name: "self-consistent-replay-divergence.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(selfConsistentDivergence))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente difiere del resultado exportado/i,
      "GT-05/FC5-REPLAY-002: reject semantic replay divergence even when package and result digests are recomputed");

    // Reset to the canonical diamond fixture: prior graph-review assertions intentionally mutate the live model.
    const editedModel = {
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
    await page.locator("#model").evaluate((el, value) => { el.value = JSON.stringify(value, null, 2); el.dispatchEvent(new Event("input", { bubbles: true })); }, editedModel);
    editedModel.scenarios.find(s => s.id === "baseline").disabled_transitions = ["t_ac"];
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, JSON.stringify(editedModel, null, 2));
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => { const status = document.querySelector("#status"); return status && !/Validando y ejecutando/.test(status.textContent); });
    const executionStatus = await page.locator("#status").innerText();
    assert.match(executionStatus, /Ejecución completada/, "Edited model execution failed: " + executionStatus);
    const baselineOutput = await page.locator(".scenario").filter({ hasText: "Escenario: baseline" }).innerText();
    assert.match(baselineOutput, /Alcanzables: A, B, D/);
    assert.doesNotMatch(baselineOutput, /Alcanzables: A, B, C, D/);
    const editedPackage = await page.evaluate(() => window.lastPackage);
    const editedPathsToD = editedPackage.result.scenario_results.baseline.trajectories
      .filter(path => path[path.length - 1].state === "D")
      .map(path => path.map(step => step.state));
    assert.deepEqual(editedPathsToD, [["A", "B", "D"]]);
    assert.doesNotMatch(baselineOutput, /A → C → D/);

    // Exercise the visual relation editor in profile 2 and verify its operational effect.
    await page.locator("#profile-editor").selectOption("2");
    await page.locator("#guarded-transition").selectOption("t_cd");
    await page.locator("#required-transition").selectOption("t_ac");
    await page.getByRole("button", { name: "Añadir relación" }).click();
    const relationModel = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(relationModel.relations, [{
      id: "r_guard_1",
      type: "requires_transition_enabled",
      transition_id: "t_cd",
      requires_transition_id: "t_ac"
    }]);
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    const relationPackage = await page.evaluate(() => window.lastPackage);
    const baselineEffects = relationPackage.result.scenario_results.baseline.relation_effects;
    assert.equal(baselineEffects.length, 1);
    assert.equal(baselineEffects[0].status, "BLOCKED");
    assert.deepEqual(relationPackage.result.scenario_results.baseline.effective_disabled_transitions, ["t_ac", "t_cd"]);
    const guardedTrace = await page.locator(".scenario").filter({ hasText: "Escenario: baseline" }).innerText();
    assert.match(guardedTrace, /t_cd.*BLOQUEADA POR REGLA.*prerequisite_transition_disabled/i,
      "FC-2: guarded transition trace must expose the active guard and its blocking reason");
    const guardedRow = page.locator('.scenario').filter({ hasText: "Escenario: baseline" }).locator('[data-accessibility-transition="t_cd"]');
    assert.equal(await guardedRow.getAttribute("data-accessibility-status"), "BLOQUEADA POR REGLA",
      "FC-2: the per-transition trace row must classify the guarded transition as blocked");
    assert.match(await guardedRow.innerText(), /prerequisite_transition_disabled/i,
      "FC-2: the per-transition row must include the actual guard-blocking reason");

    // GT-05 compatibility matrix: a package produced by supported rule profile 2
    // must survive clean import and independent replay under the same supported engine.
    const profile2DownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const profile2Download = await profile2DownloadPromise;
    const profile2Package = JSON.parse(fs.readFileSync(await profile2Download.path(), "utf8"));
    assert.equal(profile2Package.input.rule_profile.type, "relation_guarded_graph");
    await page.locator("#package-file").setInputFiles({
      name: "supported-profile-2-relation-run.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(profile2Package))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor({ timeout: 10000 });
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-05/FC5-REPLAY-003: supported profile 2 package must independently replay, not merely parse");

    // H9 grouped guarded-rule adversaries: forge rule effects while refreshing every
    // enclosing result/package digest, so rejection must come from rule semantics.
    const forgedGuardedRuleEffects = await page.evaluate(async (pkg) => {
      const cases = [
        {
          name: "guard-effect-reason",
          mutate: candidate => { candidate.result.scenario_results.baseline.relation_effects[0].reason = "prerequisite_transition_not_disabled"; },
          expected: /relation_effects no coincide con los efectos que determinan las relaciones de entrada y las deshabilitaciones explícitas/i
        },
        {
          name: "effective-disabled-omits-guarded-transition",
          mutate: candidate => { candidate.result.scenario_results.baseline.effective_disabled_transitions = ["t_ac"]; },
          expected: /effective_disabled_transitions no coincide con las relaciones aplicadas/i
        }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        const projected = structuredClone(candidate.result);
        delete projected.delta_reach;
        delete projected.engine_version;
        delete projected.input_sha256;
        delete projected.result_sha256;
        delete projected.semantic_sha256;
        delete projected.semantic_identity_version;
        Object.keys(projected.scenario_results || {}).forEach(id => {
          const scenario = projected.scenario_results[id];
          if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
        });
        Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
          const intervention = projected.comparisons_to_baseline[id].intervention || {};
          if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
        });
        candidate.result.semantic_sha256 = await window.hash(projected, "result");
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, profile2Package);
    for (const guardedCase of forgedGuardedRuleEffects) {
      await page.locator("#package-file").setInputFiles({
        name: `h9-guarded-rule-${guardedCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(guardedCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(guardedCase.expected, "i"),
        `H9: reject forged relation-guard semantics after recomputing enclosing digests: ${guardedCase.name}`);
    }

    // Restore the genuine profile-2 package before the positive round-trip below.
    await page.locator("#package-file").setInputFiles({
      name: "supported-profile-2-relation-run.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(profile2Package))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor({ timeout: 10000 });

    // Removing the relation through the real UI must remove its effect on the next run.
    await page.getByRole("button", { name: "Eliminar relación r_guard_1" }).click();
    const relationRemovedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(relationRemovedModel.relations, []);
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    const removedRelationPackage = await page.evaluate(() => window.lastPackage);
    assert.deepEqual(removedRelationPackage.result.scenario_results.baseline.relation_effects, []);
    assert.deepEqual(removedRelationPackage.result.scenario_results.baseline.effective_disabled_transitions, ["t_ac"]);

    // In profile 1, arbitrary relation records remain descriptive metadata and cannot alter outputs.
    const descriptiveModel = structuredClone(packageData.input);
    descriptiveModel.relations = [{
      id: "r_descriptive_only",
      type: "descriptive-only",
      from: "A",
      to: "D"
    }];
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, JSON.stringify(descriptiveModel, null, 2));
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    const descriptivePackage = await page.evaluate(() => window.lastPackage);
    assert.deepEqual(descriptivePackage.input.rule_profile, packageData.input.rule_profile);
    assert.deepEqual(descriptivePackage.input.relations, descriptiveModel.relations);
    assert.deepEqual(
      descriptivePackage.result.scenario_results,
      packageData.result.scenario_results,
      "Profile-1 descriptive relation metadata must not change scenario outputs"
    );

    // Restore the exact example before testing fail-closed behavior.
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, JSON.stringify(packageData.input, null, 2));
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    assert.deepEqual(
      (await page.evaluate(() => window.lastPackage)).result.scenario_results,
      packageData.result.scenario_results
    );

    // Import a visual graph (Mermaid) without requiring the user to author JSON.
    await page.locator("#graph-file").setInputFiles({
      name: "sample-flow.mmd",
      mimeType: "text/plain",
      buffer: Buffer.from("flowchart TD\n  A --> B\n  B --> C\n")
    });
    await page.locator("#file-status").filter({ hasText: "3 estados y 2 conexiones" }).waitFor();
    let importedGraph = JSON.parse(await page.locator("#model").inputValue());
    assert.deepEqual(importedGraph.states, ["A", "B", "C"]);
    assert.equal(importedGraph.transitions.length, 2);
    assert.equal(importedGraph.initial_state, "A");

    // The visual editor can add a state, connect it, and select a new initial state.
    await page.locator("#new-state-id").fill("D");
    await page.locator("#new-state-add").click();
    await page.locator("#edge-source").selectOption("C");
    await page.locator("#edge-target").selectOption("D");
    await page.locator("#new-edge-add").click();
    await page.locator("#edge-source").selectOption("B");
    await page.locator("#set-initial").click();
    importedGraph = JSON.parse(await page.locator("#model").inputValue());
    assert.ok(importedGraph.states.includes("D"));
    assert.ok(importedGraph.transitions.some((edge) => edge.source === "C" && edge.target === "D"));
    assert.equal(importedGraph.initial_state, "B");

    // A failed run must not leave the previous successful package exposed as current.
    // Set the advanced editor value directly so this assertion is independent of <details> visibility.
    await page.locator("#model").evaluate((el) => {
      el.value = "{ invalid JSON";
      el.dispatchEvent(new Event("input", { bubbles: true }));
    });
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "No se ha podido ejecutar" }).waitFor();
    assert.equal(await page.locator("#export").isDisabled(), true);
    assert.equal(await page.evaluate(() => window.lastPackage), null);
    assert.match(await page.locator("#results").innerText(), /No se ha podido ejecutar/);

    // Malformed imported package text must fail closed in the import assessment.
    await page.locator("#package-file").setInputFiles({
      name: "malformed-package.json",
      mimeType: "application/json",
      buffer: Buffer.from("{ not valid JSON")
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /JSON válido/i);

    // The import size limit must be enforced before parsing or replay.
    await page.locator("#package-file").setInputFiles({
      name: "oversized-package.json",
      mimeType: "application/json",
      buffer: Buffer.alloc(5 * 1024 * 1024 + 1, 0x20)
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /supera el límite de 5 MiB/i);

    // The UI must recover normally after the user reloads the example.
    await page.getByRole("button", { name: "Cargar ejemplo" }).click();
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    assert.ok(await page.evaluate(() => window.lastPackage));

    // Order-independence regression: execute the canonical model first, then perform graph review on a fresh page.
    const orderPage = await browser.newPage();
    await orderPage.goto("file://" + htmlPath);
    await orderPage.getByRole("button", { name: "Cargar ejemplo" }).click();
    await orderPage.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await orderPage.locator("#status").filter({ hasText: "Ejecución completada" }).waitFor();
    const orderModel = JSON.parse(await orderPage.locator("#model").inputValue());
    orderModel.transitions = [
      { id: "order_ab", source: "A", target: "B" },
      { id: "order_ab_duplicate", source: "A", target: "B" },
      { id: "order_bc", source: "B", target: "C" }
    ];
    orderModel.relations = [];
    orderModel.scenarios = orderModel.scenarios.map((scenario) => ({ ...scenario, disabled_transitions: [] }));
    await orderPage.locator("#model").evaluate((el, value) => { el.value = JSON.stringify(value, null, 2); el.dispatchEvent(new Event("input", { bubbles: true })); }, orderModel);
    await orderPage.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión order_ab_duplicate/ }).click();
    assert.equal(JSON.parse(await orderPage.locator("#model").inputValue()).transitions.length, 2);
    assert.doesNotMatch(await orderPage.locator("#graph-review-warnings").innerText(), /par\(es\).*duplicado/i);
    await orderPage.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión order_bc/ }).click();
    assert.equal(JSON.parse(await orderPage.locator("#model").inputValue()).transitions.length, 1);
    assert.match(await orderPage.locator("#graph-review-warnings").innerText(), /solo hay una conexión/i);
    await orderPage.close();

    // FC-1 contract: browser UI exposes and executes the separately versioned temporal profile.
    await page.getByRole("button", { name: "Cargar ejemplo" }).click();
    const profileOptions = await page.locator("#profile-editor option").evaluateAll(options => options.map(option => ({ value: option.value, label: option.textContent.trim() })));
    assert.ok(profileOptions.some(option => option.value === "3" && /temporal|prerrequisito/i.test(option.label)),
      "FC-1: browser UI must expose profile 3 for temporal prerequisites without overloading profile 2");
    const temporalModel = structuredClone(await page.locator("#model").inputValue().then(JSON.parse));
    temporalModel.rule_profile = { type: "temporal_prerequisite_graph", version: "1" };
    temporalModel.relations = [{
      id: "r_temporal_1",
      type: "requires_prior_execution",
      transition_id: "t_cd",
      requires_transition_id: "t_ab"
    }];
    await page.locator("#model").evaluate((el, value) => { el.value = value; el.dispatchEvent(new Event("input", { bubbles: true })); }, JSON.stringify(temporalModel, null, 2));
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => /Ejecución completada|No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""), { timeout: 10000 });
    assert.match(await page.locator("#status").innerText(), /Ejecución completada/i,
      "FC-1: browser engine must execute temporal profile 3 rather than leave the run pending");
    assert.match(await page.locator("#results").innerText(), /t_cd.*t_ab|t_ab.*t_cd/i,
      "FC-1: browser results must expose t_cd blocked until t_ab occurred earlier in the same trajectory");
    assert.match(await page.locator("#results").innerText(), /t_cd.*CONDICIONADA POR SECUENCIA.*t_ab/i,
      "FC-2: temporal trace must label t_cd as sequence-conditioned and identify t_ab as its prerequisite");

    // GT-05 positive full-chain acceptance: one hand-checkable diamond model, temporal prerequisite,
    // baseline/intervention, delta_reach, candidate trajectory, concrete execution, outcome/value,
    // export/import and independent replay are verified as one connected scenario below.
    const gt05ExplorationPackage = await page.evaluate(() => structuredClone(window.lastPackage));
    assert.ok(gt05ExplorationPackage && gt05ExplorationPackage.input && gt05ExplorationPackage.result,
      "GT-05: scenario exploration must produce an inspectable input/result package");
    assert.deepEqual(gt05ExplorationPackage.input.states, ["A", "B", "C", "D"],
      "GT-05: the hand-checkable diamond model must retain all four states");
    assert.deepEqual(
      gt05ExplorationPackage.input.transitions.map(t => t.id).sort(),
      ["t_ab", "t_ac", "t_bd", "t_cd"],
      "GT-05: the model must contain both alternative routes from A to D");
    assert.deepEqual(gt05ExplorationPackage.input.relations, [{
      id: "r_temporal_1",
      type: "requires_prior_execution",
      transition_id: "t_cd",
      requires_transition_id: "t_ab"
    }], "GT-05: the temporal prerequisite must be part of the exported source model");
    assert.deepEqual(Object.keys(gt05ExplorationPackage.result.scenario_results).sort(), ["baseline", "block_ac"],
      "GT-05: baseline and intervention results must be present together");
    assert.deepEqual(gt05ExplorationPackage.result.scenario_results.baseline.reachable_states, ["A", "B", "C", "D"],
      "GT-05: baseline must expose the complete reachable state set");
    assert.deepEqual(gt05ExplorationPackage.result.scenario_results.block_ac.reachable_states, ["A", "B", "D"],
      "GT-05: intervention must remove C from the reachable state set");
    assert.ok(gt05ExplorationPackage.result.delta_reach.block_ac.reachable_states_removed.includes("C"),
      "GT-05: delta_reach must explicitly report the intervention's removed reachable state");
    assert.ok(gt05ExplorationPackage.result.comparisons_to_baseline.block_ac.trajectories_removed.length > 0,
      "GT-05: baseline comparison must identify trajectories removed by the intervention");
    assert.ok(gt05ExplorationPackage.result.scenario_results.baseline.trajectories.some(path =>
      path.map(step => step.state).join("->") === "A->B->D"),
      "GT-05: at least one candidate trajectory must be inspectable before concrete execution");


    // FC-2 contract-first: exploration must be distinguishable from an explicitly executed concrete sequence.
    assert.ok(await page.locator("#execute-sequence").count() === 1,
      "FC-2: UI must provide an explicit action to execute a selected trajectory");
    assert.ok(await page.locator("#sequence-select").count() === 1,
      "FC-2: UI must expose the candidate trajectory selected for execution");
    assert.ok(await page.locator("#sequence-trace").count() === 1,
      "FC-2: concrete execution must produce a separate auditable step trace");
    await page.locator("#sequence-select").selectOption({ index: 0 });
    await page.getByRole("button", { name: /Ejecutar secuencia seleccionada/i }).click();
    await page.locator("#sequence-trace").filter({ hasText: /Estado inicial|Paso 1/ }).waitFor();
    assert.match(await page.locator("#sequence-trace").innerText(), /Estado inicial/i,
      "FC-2: execution trace must identify the starting state");
    assert.match(await page.locator("#sequence-trace").innerText(), /Paso 1/i,
      "FC-2: execution trace must record ordered concrete steps");
    assert.match(await page.locator("#sequence-trace").innerText(), /Traza SHA-256/i,
      "FC-3: successful execution must expose a digest for its trace");
    // Submit a validly connected but temporally invalid sequence: t_ac reaches C, then t_cd lacks t_ab.
    await page.locator("#sequence-input").fill("t_ac, t_cd");
    assert.equal(await page.locator("#sequence-input").inputValue(), "t_ac, t_cd",
      "FC-3: manual attempted sequence must be present before execution");
    await page.getByRole("button", { name: /Ejecutar secuencia seleccionada/i }).click();
    await page.waitForFunction(() => document.querySelector("#sequence-trace")?.dataset.state === "blocked-trace-recorded" || document.querySelector("#sequence-trace")?.dataset.state === "rejected", { timeout: 3000 });
    await page.locator("#sequence-trace").waitFor();
    assert.equal(await page.locator("#sequence-trace").getAttribute("data-state"), "blocked-trace-recorded",
      "FC-3: blocked attempted sequence must be retained as an auditable trace");
    const blockedTraceText = await page.locator("#sequence-trace").innerText();
    assert.match(blockedTraceText, /Paso bloqueado 2: t_cd/i,
      "FC-3: trace must identify the exact blocked step and transition");
    assert.match(blockedTraceText, /temporal_prerequisite_not_satisfied/i,
      "FC-3: trace must state the temporal blocking reason");
    assert.match(blockedTraceText, /t_ab/i,
      "FC-3: trace must identify the missing prerequisite transition");
    assert.match(blockedTraceText, /Traza SHA-256/i,
      "FC-3: blocked attempt must have a trace digest");
    const blockedTraceIntegrity = await page.evaluate(() => {
      const trace = document.querySelector("#sequence-trace")._trace;
      const before = trace.trace_sha256;
      const originalReason = trace.blocked_step.reason;
      const mutationAccepted = Reflect.set(trace.blocked_step, "reason", "tampered");
      return {
        frozen: Object.isFrozen(trace) && Object.isFrozen(trace.blocked_step) &&
          Object.isFrozen(trace.steps) && Object.isFrozen(trace.steps[0]),
        mutationAccepted,
        reason: trace.blocked_step.reason,
        originalReason,
        digestUnchanged: trace.trace_sha256 === before
      };
    });
    assert.equal(blockedTraceIntegrity.frozen, true,
      "FC-3: attempted blocked trace and nested records must be immutable after digesting");
    assert.equal(blockedTraceIntegrity.mutationAccepted, false,
      "FC-3: mutation of a blocked trace reason must be rejected");
    assert.equal(blockedTraceIntegrity.reason, blockedTraceIntegrity.originalReason,
      "FC-3: attempted mutation must not alter the blocking reason");
    assert.equal(blockedTraceIntegrity.digestUnchanged, true,
      "FC-3: trace digest must remain attached to the immutable trace");

    // FC-5 approved policy A: blocked attempts round-trip as inspectable EXECUTION-stage packages.
    const blockedExportPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const blockedDownload = await blockedExportPromise;
    const blockedPackage = JSON.parse(fs.readFileSync(await blockedDownload.path(), "utf8"));
    assert.equal(blockedPackage.package_stage, "EXECUTION");
    assert.equal(blockedPackage.concrete_execution_trace.status, "BLOCKED");
    assert.equal(blockedPackage.value_assessment_status, "NOT_ASSESSED");
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-stage-package.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(blockedPackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "FC-5: a coherent BLOCKED trace must remain importable and inspectable");

    // A BLOCKED trace must never be accepted as the evidence for an explicit completed outcome.
    const blockedWithOutcome = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_stage = "OUTCOME";
      candidate.outcome_record = {
        outcome_schema: "collective-toy-outcome-001",
        outcome_id: "invalid-outcome-for-blocked-trace",
        execution_id: candidate.concrete_execution_trace.execution_id,
        execution_trace_sha256: candidate.concrete_execution_trace.trace_sha256,
        model_id: candidate.input.model_id,
        scenario_id: candidate.concrete_execution_trace.scenario_id,
        value: "must reject"
      };
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-with-outcome.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(blockedWithOutcome))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /requiere una traza COMPLETED/i,
      "FC-5: outcome linked to a BLOCKED trace must be rejected");

    await page.locator("#sequence-input").fill("");
    await page.getByRole("button", { name: /Ejecutar secuencia seleccionada/i }).click();
    await page.waitForFunction(() => document.querySelector("#sequence-trace")?.dataset.state === "replay-verified" || document.querySelector("#sequence-trace")?.dataset.state === "rejected", { timeout: 3000 });
    assert.equal(await page.locator("#sequence-trace").getAttribute("data-state"), "replay-verified",
      "FC-3: successful trace must be restored before export/replay assertions");

    // FC-3: the reproducibility package must contain the exact concrete trace, not only the explored paths.
    const traceDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const traceDownload = await traceDownloadPromise;
    const downloadedPath = await traceDownload.path();
    assert.ok(downloadedPath, "FC-3: evidence export must produce a downloadable JSON file");
    const evidencePackage = JSON.parse(fs.readFileSync(downloadedPath, "utf8"));
    assert.ok(evidencePackage.concrete_execution_trace,
      "FC-3: exported evidence package must include the concrete execution trace");
    assert.match(evidencePackage.concrete_execution_trace.trace_sha256, /^[a-f0-9]{64}$/i,
      "FC-3: exported trace must include its SHA-256 digest");
    assert.equal(evidencePackage.concrete_execution_trace.status, "COMPLETED",
      "FC-3: exported trace must preserve the execution status");

    // FC-3 replay contract: import the exact downloaded artifact and independently recompute its result.
    await page.locator("#package-file").setInputFiles(downloadedPath);
    await page.locator("#assess-package").click();
    await page.waitForFunction(() => /replay-verified|rejected|inspect-only\/replay-unavailable/.test(document.querySelector("#package-assessment")?.dataset.state || ""), { timeout: 10000 });
    const replayAssessment = await page.locator("#package-assessment").innerText();
    assert.equal(await page.locator("#package-assessment").getAttribute("data-state"), "replay-verified",
      "FC-3: a freshly exported package must pass independent import/replay; assessor reported: " + replayAssessment);
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "FC-3: replay result must explicitly report a matching independently recomputed result");

    // FC-4: outcome and contextual valuation are explicit, execution-linked, and never inferred.
    assert.match(await page.locator("#value-status").innerText(), /NOT_ASSESSED/i,
      "FC-4: absent valuation inputs must explicitly remain NOT_ASSESSED");
    assert.equal(await page.locator("#record-outcome").isEnabled(), true,
      "FC-4: outcome recording must be available after a completed concrete execution");
    await page.locator("#outcome-value").fill("illustrative outcome");
    await page.locator("#outcome-unit").fill("qualitative");
    await page.locator("#outcome-timing").fill("after execution");
    await page.locator("#outcome-uncertainty").fill("synthetic; not measured");
    await page.locator("#outcome-provenance").fill("synthetic acceptance fixture");
    await page.locator("#record-outcome").click();
    assert.equal(await page.locator("#outcome-status").getAttribute("data-state"), "recorded",
      "FC-4: explicitly entered outcome must be recorded");
    assert.match(await page.locator("#outcome-status").innerText(), /sequence-execution-/,
      "FC-4: outcome must display its linked execution ID");
    assert.equal(await page.locator("#assess-value").isEnabled(), true,
      "FC-4: contextual assessment is available only after an outcome exists");
    await page.locator("#assess-value").click();
    assert.equal(await page.locator("#value-status").getAttribute("data-state"), "not-assessed",
      "FC-4: missing observer/context/criterion/rule/rationale must remain NOT_ASSESSED");
    await page.locator("#value-observer").fill("fixture observer");
    await page.locator("#value-context").fill("synthetic test context");
    await page.locator("#value-criterion").fill("criterion alpha");
    await page.locator("#value-rule").fill("qualitative rule");
    await page.locator("#value-rationale").fill("explicit test-only rationale");
    await page.locator("#assess-value").click();
    await page.locator("#value-status[data-state=" + '"assessed"' + "]").waitFor();
    assert.equal(await page.locator("#value-status").getAttribute("data-state"), "assessed",
      "FC-4: complete contextual assessment must be linked and recorded");
    const fc4ExportPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const fc4Download = await fc4ExportPromise;
    const fc4Package = JSON.parse(fs.readFileSync(await fc4Download.path(), "utf8"));

    // GT-05 end-to-end linkage: the assessed export must preserve the exact explored model/result,
    // and its concrete submitted sequence must be one of the candidate trajectories from that run.
    assert.deepEqual(fc4Package.input, gt05ExplorationPackage.input,
      "GT-05: final assessed package must preserve the source model used for exploration");
    assert.deepEqual(fc4Package.result, gt05ExplorationPackage.result,
      "GT-05: final assessed package must preserve the explored baseline/intervention and delta_reach result");
    const executedTransitionIds = fc4Package.concrete_execution_trace.submitted_transition_ids;
    assert.ok(gt05ExplorationPackage.result.scenario_results.baseline.trajectories.some(path =>
      JSON.stringify(path.slice(1).map(step => step.transition)) === JSON.stringify(executedTransitionIds)),
      "GT-05: concrete execution must match one of the candidate trajectories explored from the same model");
    assert.equal(fc4Package.outcome_record.execution_id, fc4Package.concrete_execution_trace.execution_id,
      "FC-4: exported outcome must link to the exact exported execution");
    assert.equal(fc4Package.outcome_record.execution_trace_sha256, fc4Package.concrete_execution_trace.trace_sha256,
      "FC-4: outcome must retain the execution trace digest");
    assert.equal(fc4Package.value_assessment.outcome_id, fc4Package.outcome_record.outcome_id,
      "FC-4: value assessment must reference the exact outcome");
    assert.equal(fc4Package.value_assessment.status, "ASSESSED",
      "FC-4: exported complete assessment must be explicit");
    assert.equal(fc4Package.value_assessment_status, undefined,
      "FC-4: an assessed package must not also claim valuation is unassessed");

    // FC-6 grouped exported-artifact audit: verify the complete Full Chain envelope and digest.
    assert.deepEqual(Object.keys(fc4Package).sort(), [
      "concrete_execution_trace", "input", "outcome_record", "package_sha256",
      "package_stage", "package_version", "result", "value_assessment"
    ].sort(), "FC-6: assessed Full Chain export must contain exactly the contracted envelope fields");
    assert.equal(fc4Package.package_stage, "ASSESSMENT",
      "FC-6: complete outcome/value export must identify its package stage");
    assert.equal(fc4Package.result.validation, "PASS",
      "FC-6: exported successful result must retain PASS validation status");
    assert.equal(fc4Package.result.model_id, fc4Package.input.model_id,
      "FC-6: exported result model identity must match the input model");
    assert.equal(fc4Package.concrete_execution_trace.model_id, fc4Package.input.model_id,
      "FC-6: exported execution trace model identity must match the input model");
    assert.equal(fc4Package.concrete_execution_trace.scenario_id, fc4Package.outcome_record.scenario_id,
      "FC-6: exported outcome and execution trace must refer to the same scenario");
    assert.equal(fc4Package.value_assessment.execution_id, fc4Package.concrete_execution_trace.execution_id,
      "FC-6: exported valuation must link to the exact execution");
    assert.match(fc4Package.package_sha256 || "", /^[a-f0-9]{64}$/i,
      "FC-6: complete exported package must carry a well-formed SHA-256 digest");
    const exportedPackageDigest = await page.evaluate(async (pkg) => {
      const body = structuredClone(pkg);
      delete body.package_sha256;
      return window.hash(body, "package_export");
    }, fc4Package);
    assert.equal(exportedPackageDigest, fc4Package.package_sha256,
      "FC-6: complete exported package digest must recompute from the exported envelope");

    assert.ok(["value", "unit", "timing", "uncertainty_status", "provenance"].every(key =>
      typeof fc4Package.outcome_record[key] === "string" && fc4Package.outcome_record[key].trim().length > 0),
      "FC-6: artifact inventory must retain the complete non-empty outcome provenance fields");
    assert.ok(["observer", "context", "criterion", "valuation_rule", "rationale"].every(key =>
      typeof fc4Package.value_assessment[key] === "string" && fc4Package.value_assessment[key].trim().length > 0),
      "FC-6: artifact inventory must retain observer/context/criterion/rule/rationale provenance");
    const exportedOutcomeDigest = await page.evaluate(async (outcome) =>
      window.hash(outcome, "outcome_record"), fc4Package.outcome_record);
    assert.equal(fc4Package.value_assessment.outcome_sha256, exportedOutcomeDigest,
      "FC-6: assessment must carry the recomputable digest of the exact exported outcome");

    // FC-5 grouped package-integrity adversary: absent, malformed, and incorrect outer digest.
    const invalidPackageDigests = await page.evaluate(async (pkg) => {
      const missing = structuredClone(pkg);
      delete missing.package_sha256;
      const malformed = structuredClone(pkg);
      malformed.package_sha256 = "not-a-sha256";
      const incorrect = structuredClone(pkg);
      incorrect.package_sha256 = "0".repeat(64);
      return [
        { name: "missing", candidate: missing },
        { name: "malformed", candidate: malformed },
        { name: "incorrect", candidate: incorrect }
      ];
    }, fc4Package);
    for (const digestCase of invalidPackageDigests) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-package-digest-${digestCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(digestCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /hash|digest|sha-?256|integridad/i,
        `FC-5: importer must diagnose ${digestCase.name} package digest`);
    }

    // FC-5 grouped type-adversary: object-only package sections must reject non-object substitutes.
    const invalidPackageSectionTypes = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "trace-array", key: "concrete_execution_trace", value: [] },
        { name: "outcome-string", key: "outcome_record", value: "not-an-object" },
        { name: "assessment-null", key: "value_assessment", value: null }
      ];
      return Promise.all(cases.map(async (item) => {
        const candidate = structuredClone(pkg);
        candidate[item.key] = item.value;
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate };
      }));
    }, fc4Package);
    for (const sectionCase of invalidPackageSectionTypes) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-package-section-${sectionCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(sectionCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /paquete|traza|outcome|valoraci[oó]n|estructura|objeto|reproducci[oó]n/i,
        `FC-5: importer must diagnose non-object ${sectionCase.name} section`);
    }

    // GT-04 grouped lifecycle truth table: COMPLETED trace without outcome remains EXECUTION/NOT_ASSESSED.
    const completedWithoutOutcome = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.outcome_record;
      delete candidate.value_assessment;
      candidate.package_stage = "EXECUTION";
      candidate.value_assessment_status = "NOT_ASSESSED";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    assert.equal(completedWithoutOutcome.concrete_execution_trace.status, "COMPLETED");
    assert.equal(completedWithoutOutcome.package_stage, "EXECUTION");
    assert.equal(completedWithoutOutcome.value_assessment_status, "NOT_ASSESSED");
    await page.locator("#package-file").setInputFiles({
      name: "completed-trace-without-outcome.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(completedWithoutOutcome))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-04: COMPLETED trace without outcome must import/replay as EXECUTION, NOT_ASSESSED");

    // GT-04 adversary: a valuation cannot exist without its outcome, even with a recomputed package digest.
    const assessmentWithoutOutcome = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.outcome_record;
      candidate.package_stage = "ASSESSMENT";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "assessment-without-outcome.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(assessmentWithoutOutcome))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /la valoración requiere un resultado explícito/i,
      "GT-04: reject assessment without outcome independently of package digest");

    // GT-04 adversary: a package without valuation must not claim the ASSESSED status.
    const assessedStatusWithoutValuation = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.value_assessment;
      candidate.package_stage = "OUTCOME";
      candidate.value_assessment_status = "ASSESSED";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "assessed-status-without-valuation.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(assessedStatusWithoutValuation))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /value_assessment_status=NOT_ASSESSED/i,
      "GT-04: reject ASSESSED status when no valuation artifact exists");

    // GT-04 adversary: a complete valuation cannot coexist with an explicit NOT_ASSESSED status.
    const valuationWithNotAssessedStatus = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment_status = "NOT_ASSESSED";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "valuation-with-not-assessed-status.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(valuationWithNotAssessedStatus))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /un paquete evaluado no puede declarar NOT_ASSESSED/i,
      "GT-04: reject contradictory assessed artifact plus NOT_ASSESSED status");

    // H1 grouped input-schema adversaries. Refresh input and package digests so
    // each malformed nested input reaches the intended schema validator.
    const inputSchemaAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "input-schema-version-unknown-string", mutate: input => { input.schema_version = "collective-toy-input-999"; }, diagnostic: /schema_version no compatible/i },
        { name: "input-schema-version-missing", mutate: input => { delete input.schema_version; }, diagnostic: /schema_version no compatible/i },
        { name: "input-model-id-missing", mutate: input => { delete input.model_id; }, diagnostic: /model_id debe ser texto no vacío/i },
        { name: "input-model-id-wrong-type", mutate: input => { input.model_id = 17; }, diagnostic: /model_id debe ser texto no vacío/i },
        { name: "input-initial-state-missing", mutate: input => { delete input.initial_state; }, diagnostic: /initial_state debe ser un ID de estado declarado/i },
        { name: "input-initial-state-wrong-type", mutate: input => { input.initial_state = ["A"]; }, diagnostic: /initial_state debe ser un ID de estado declarado/i },
        { name: "input-relations-wrong-type", mutate: input => { input.relations = "not-an-array"; }, diagnostic: /relations debe ser una lista/i },
        { name: "input-scenario-element-wrong-type", mutate: input => { input.scenarios[0] = "not-an-object"; }, diagnostic: /Cada escenario debe ser un objeto/i },
        { name: "input-exploration-bound-wrong-type", mutate: input => { input.exploration.max_depth = "4"; }, diagnostic: /max_depth debe ser un entero entre 0 y 100/i },
        { name: "input-missing-states", mutate: input => { delete input.states; }, diagnostic: /states debe ser una lista no vacía/i },
        { name: "input-transitions-missing", mutate: input => { delete input.transitions; }, diagnostic: /transitions debe ser una lista/i },
        { name: "input-transitions-wrong-type", mutate: input => { input.transitions = { id: "not-an-array" }; }, diagnostic: /transitions debe ser una lista/i },
        { name: "input-transition-unknown-nested-key", mutate: input => { input.transitions[0].unreviewed_extension = true; }, diagnostic: /Transición contiene campos desconocidos/i },
        { name: "input-rule-profile-missing", mutate: input => { delete input.rule_profile; }, diagnostic: /rule_profile debe ser un objeto/i },
        { name: "input-scenarios-missing", mutate: input => { delete input.scenarios; }, diagnostic: /scenarios debe ser una lista no vacía/i },
        { name: "input-scenarios-wrong-type", mutate: input => { input.scenarios = "not-an-array"; }, diagnostic: /scenarios debe ser una lista no vacía/i },
        { name: "input-scenario-unknown-nested-key", mutate: input => { input.scenarios[0].unreviewed_extension = true; }, diagnostic: /Escenario contiene campos desconocidos/i },
        { name: "input-exploration-missing", mutate: input => { delete input.exploration; }, diagnostic: /exploration debe ser un objeto/i },
        { name: "input-exploration-wrong-type", mutate: input => { input.exploration = []; }, diagnostic: /exploration debe ser un objeto/i },
        { name: "input-exploration-unknown-nested-key", mutate: input => { input.exploration.unreviewed_extension = true; }, diagnostic: /exploration contiene campos desconocidos/i },
        { name: "input-rule-profile-unknown-key", mutate: input => { input.rule_profile.unreviewed_extension = true; }, diagnostic: /rule_profile contiene campos desconocidos/i },
        { name: "input-rule-profile-unknown-type", mutate: input => { input.rule_profile.type = "unreviewed_graph"; }, diagnostic: /rule_profile no compatible/i },
        { name: "input-rule-profile-unsupported-version", mutate: input => { input.rule_profile.version = "2"; }, diagnostic: /rule_profile no compatible/i },
        { name: "input-rule-profile-incompatible-type-version-pair", mutate: input => { input.rule_profile = { type: "relation_guarded_graph", version: "2" }; }, diagnostic: /rule_profile no compatible/i },
        { name: "input-relation-unknown-nested-key", mutate: input => { input.rule_profile = { type: "relation_guarded_graph", version: "1" }; input.relations = [{ id: "h1_relation", type: "requires_transition_enabled", transition_id: input.transitions[1].id, requires_transition_id: input.transitions[0].id, unreviewed_extension: true }]; }, diagnostic: /Relación contiene campos desconocidos/i },
        { name: "input-unknown-top-level-key", mutate: input => { input.unreviewed_extension = true; }, diagnostic: /El modelo contiene campos desconocidos/i }
      ];
      return await Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate.input);
        candidate.result.input_sha256 = await window.hash(candidate.input, "input");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, diagnostic: item.diagnostic.source };
      }));
    }, fc4Package);
    for (const inputCase of inputSchemaAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `h1-input-schema-${inputCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(inputCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(inputCase.diagnostic, "i"),
        `H1: reject malformed nested input predicate ${inputCase.name}`);
    }

    // FC5-RES-002..005 grouped result-envelope adversaries. Recompute semantic/result/package
    // digests so each case reaches the intended result-vs-input contract assertion.
    const resultEnvelopeAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "schema-version-mismatch", mutate: p => { p.result.schema_version = "unsupported-result-schema"; }, expected: /versión de esquema del resultado no coincide con la entrada/i },
        { name: "model-id-mismatch", mutate: p => { p.result.model_id = "forged-model-id"; }, expected: /model_id del resultado no coincide con la entrada/i },
        { name: "rule-profile-mismatch", mutate: p => { p.result.rule_profile = { type: "relation_guarded_graph", version: "1" }; }, expected: /perfil de reglas del resultado no coincide con la entrada/i },
        { name: "validation-not-pass", mutate: p => { p.result.validation = "FAIL"; }, expected: /resultado no declara validation=PASS/i }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        if (candidate.result.semantic_identity_version !== undefined) {
          const projected = structuredClone(candidate.result);
          delete projected.delta_reach;
          delete projected.engine_version;
          delete projected.input_sha256;
          delete projected.result_sha256;
          delete projected.semantic_sha256;
          delete projected.semantic_identity_version;
          Object.keys(projected.scenario_results || {}).forEach(id => {
            const scenario = projected.scenario_results[id];
            if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
          });
          Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
            const intervention = projected.comparisons_to_baseline[id].intervention || {};
            if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
          });
          candidate.result.semantic_sha256 = await window.hash(projected, "result");
        }
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const resultCase of resultEnvelopeAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `fc5-result-envelope-${resultCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(resultCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(resultCase.expected, "i"),
        `FC5: reject result-envelope contract violation ${resultCase.name} after recomputing enclosing digests`);
    }

    // FC5-RES-006/007 grouped exact-set adversaries. Refresh semantic and enclosing
    // digests so each rejection reaches the intended exact-set invariant.
    const exactScenarioSetAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        {
          name: "scenario-results-missing-intervention",
          mutate: p => { delete p.result.scenario_results.block_ac; },
          expected: /scenario_results no contiene todos los escenarios de la entrada/i
        },
        {
          name: "scenario-results-unexpected-key",
          mutate: p => {
            p.result.scenario_results.uncontracted_scenario = structuredClone(p.result.scenario_results.baseline);
            p.result.scenario_results.uncontracted_scenario.scenario_id = "uncontracted_scenario";
          },
          expected: /scenario_results contiene escenarios que no están en la entrada/i
        },
        {
          name: "comparisons-missing-intervention",
          mutate: p => { delete p.result.comparisons_to_baseline.block_ac; },
          expected: /Falta comparación baseline para block_ac/i
        },
        {
          name: "comparisons-unexpected-baseline",
          mutate: p => { p.result.comparisons_to_baseline.baseline = structuredClone(p.result.comparisons_to_baseline.block_ac); },
          expected: /comparisons_to_baseline contiene una clave de escenario no compatible/i
        }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        const projected = structuredClone(candidate.result);
        delete projected.delta_reach;
        delete projected.engine_version;
        delete projected.input_sha256;
        delete projected.result_sha256;
        delete projected.semantic_sha256;
        delete projected.semantic_identity_version;
        Object.keys(projected.scenario_results || {}).forEach(id => {
          const scenario = projected.scenario_results[id];
          if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
        });
        Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
          const intervention = projected.comparisons_to_baseline[id].intervention || {};
          if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
        });
        candidate.result.semantic_sha256 = await window.hash(projected, "result");
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const resultCase of exactScenarioSetAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `fc5-exact-scenario-set-${resultCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(resultCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(resultCase.expected, "i"),
        `FC5: reject exact-set violation ${resultCase.name} after refreshing semantic/result/package digests`);
    }

    // FC5-RES-008 grouped semantic identity conditional-pairing adversaries.
    // Preserve valid outer digests so each case reaches the intended conditional predicate.
    const semanticIdentityAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        {
          name: "version-without-semantic-hash",
          mutate: p => { p.result.semantic_identity_version = "collective-toy-semantic-identity-001"; delete p.result.semantic_sha256; },
          expected: /semantic_sha256 ausente o malformado/i
        },
        {
          name: "semantic-hash-without-version",
          mutate: p => { delete p.result.semantic_identity_version; },
          expected: /semantic_sha256 requiere una versión explícita/i
        },
        {
          name: "unsupported-semantic-identity-version",
          mutate: p => { p.result.semantic_identity_version = "unsupported-semantic-identity-version"; },
          expected: /versión de identidad semántica no admitida/i
        },
        {
          name: "malformed-semantic-hash",
          mutate: p => { p.result.semantic_sha256 = "not-a-sha256"; },
          expected: /semantic_sha256 ausente o malformado/i
        },
        {
          name: "semantic-hash-null",
          mutate: p => { p.result.semantic_sha256 = null; },
          expected: /semantic_sha256 ausente o malformado/i
        },
        {
          name: "semantic-hash-array",
          mutate: p => { p.result.semantic_sha256 = []; },
          expected: /semantic_sha256 ausente o malformado/i
        },
        {
          name: "semantic-hash-number",
          mutate: p => { p.result.semantic_sha256 = 17; },
          expected: /semantic_sha256 ausente o malformado/i
        },
        {
          name: "semantic-version-null",
          mutate: p => { p.result.semantic_identity_version = null; },
          expected: /versión de identidad semántica no admitida/i
        },
        {
          name: "semantic-version-number",
          mutate: p => { p.result.semantic_identity_version = 7; },
          expected: /versión de identidad semántica no admitida/i
        }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        if (candidate.result.semantic_identity_version !== undefined && candidate.result.semantic_sha256 !== undefined &&
            /^[0-9a-f]{64}$/.test(candidate.result.semantic_sha256)) {
          const projected = structuredClone(candidate.result);
          delete projected.delta_reach;
          delete projected.engine_version;
          delete projected.input_sha256;
          delete projected.result_sha256;
          delete projected.semantic_sha256;
          delete projected.semantic_identity_version;
          Object.keys(projected.scenario_results || {}).forEach(id => {
            const scenario = projected.scenario_results[id];
            if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
          });
          Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
            const intervention = projected.comparisons_to_baseline[id].intervention || {};
            if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
          });
          candidate.result.semantic_sha256 = await window.hash(projected, "result");
        }
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const resultCase of semanticIdentityAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `fc5-semantic-identity-${resultCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(resultCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(resultCase.expected, "i"),
        `FC5-RES-008: reject semantic identity pairing violation ${resultCase.name} after refreshing enclosing digests`);
    }

    // FC5-RES-009/010 grouped direct hash format and recomputation adversaries.
    // Refresh outer digests so validation reaches the intended input/result hash predicate.
    const directHashAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        {
          name: "input-hash-malformed",
          mutate: p => { p.result.input_sha256 = "not-a-sha256"; },
          expected: /input_sha256 ausente o malformado/i
        },
        {
          name: "input-hash-wrong-but-well-formed",
          mutate: p => { p.result.input_sha256 = "0".repeat(64); },
          expected: /El hash de la entrada no coincide/i
        },
        {
          name: "result-hash-malformed",
          mutate: p => { p.result.result_sha256 = "not-a-sha256"; },
          expected: /result_sha256 ausente o malformado/i
        },
        {
          name: "result-hash-wrong-but-well-formed",
          mutate: p => { p.result.result_sha256 = "0".repeat(64); },
          expected: /El hash del resultado no coincide/i
        },
        {
          name: "input-hash-missing",
          mutate: p => { delete p.result.input_sha256; },
          expected: /input_sha256 ausente o malformado/i
        },
        {
          name: "input-hash-null",
          mutate: p => { p.result.input_sha256 = null; },
          expected: /input_sha256 ausente o malformado/i
        },
        {
          name: "input-hash-number",
          mutate: p => { p.result.input_sha256 = 17; },
          expected: /input_sha256 ausente o malformado/i
        },
        {
          name: "result-hash-missing",
          mutate: p => { delete p.result.result_sha256; },
          expected: /result_sha256 ausente o malformado/i
        },
        {
          name: "result-hash-null",
          mutate: p => { p.result.result_sha256 = null; },
          expected: /result_sha256 ausente o malformado/i
        },
        {
          name: "result-hash-array",
          mutate: p => { p.result.result_sha256 = []; },
          expected: /result_sha256 ausente o malformado/i
        },
        {
          name: "result-hash-number",
          mutate: p => { p.result.result_sha256 = 17; },
          expected: /result_sha256 ausente o malformado/i
        }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const hashCase of directHashAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `fc5-direct-hash-${hashCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(hashCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(hashCase.expected, "i"),
        `FC5-RES-009/010: reject direct hash violation ${hashCase.name} after refreshing package digest`);
    }

    // H2 grouped scenario-result schema adversaries. Recompute semantic/result/package
    // digests so rejection is attributable to the nested scenario-result invariant.
    const scenarioResultAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "scenario-missing-reachable-states", mutate: p => { delete p.result.scenario_results.baseline.reachable_states; }, expected: /El campo reachable_states del escenario baseline debe ser una lista/i },
        { name: "scenario-missing-disabled-transitions", mutate: p => { delete p.result.scenario_results.baseline.disabled_transitions; }, expected: /El campo disabled_transitions del escenario baseline debe ser una lista/i },
        { name: "scenario-enabled-transitions-wrong-type", mutate: p => { p.result.scenario_results.baseline.enabled_transitions_at_initial_state = "not-an-array"; }, expected: /El campo enabled_transitions_at_initial_state del escenario baseline debe ser una lista/i },
        { name: "scenario-reachable-state-non-string", mutate: p => { p.result.scenario_results.baseline.reachable_states = [17]; }, expected: /Todos los elementos de reachable_states en baseline deben ser cadenas no vacías/i },
        { name: "scenario-trajectory-step-unknown-key", mutate: p => { p.result.scenario_results.baseline.trajectories = [[{ state: p.input.initial_state, extra: true }]]; }, expected: /trajectories del escenario baseline debe contener rutas válidas y transiciones coherentes con la entrada/i },
        { name: "scenario-exploration-bounds-missing-depth", mutate: p => { delete p.result.scenario_results.baseline.exploration_bounds.max_depth; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-negative-count", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_trajectories = -1; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-undeclared-reachable-state", mutate: p => { p.result.scenario_results.baseline.reachable_states = [...p.result.scenario_results.baseline.reachable_states, "STATE_NOT_DECLARED"]; }, expected: /reachable_states del escenario baseline debe contener solo IDs de estado declarados/i },
        { name: "scenario-trajectories-wrong-type", mutate: p => { p.result.scenario_results.baseline.trajectories = "not-an-array"; }, expected: /El campo trajectories del escenario baseline debe ser una lista/i },
        { name: "scenario-disconnected-trajectory", mutate: p => { p.result.scenario_results.baseline.trajectories = [[{ state: p.input.initial_state }, { state: "C", transition: "t_ab" }]]; }, expected: /trajectories del escenario baseline debe contener rutas válidas y transiciones coherentes con la entrada/i },
        { name: "scenario-unknown-key", mutate: p => { p.result.scenario_results.baseline.unreviewed_extension = true; }, expected: /El resultado del escenario baseline contiene campos desconocidos/i },
        { name: "scenario-id-key-mismatch", mutate: p => { p.result.scenario_results.baseline.scenario_id = "not-baseline"; }, expected: /scenario_id no coincide con la clave baseline/i },
        { name: "scenario-exploration-bounds-wrong-type", mutate: p => { p.result.scenario_results.baseline.exploration_bounds = []; }, expected: /exploration_bounds del escenario baseline debe ser un objeto/i },
        { name: "scenario-exploration-bounds-unknown-key", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.uncontracted_limit = 7; }, expected: /exploration_bounds contiene campos desconocidos/i },
        { name: "scenario-exploration-bounds-negative-depth", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_depth = -1; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-fractional-count", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_trajectories = 1.5; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-depth-over-maximum", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_depth = 101; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-count-over-maximum", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_trajectories = 10001; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-zero-count", mutate: p => { p.result.scenario_results.baseline.exploration_bounds.max_trajectories = 0; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-exploration-bounds-missing-count", mutate: p => { delete p.result.scenario_results.baseline.exploration_bounds.max_trajectories; }, expected: /exploration_bounds debe respetar max_depth entre 0 y 100 y max_trajectories entre 1 y 10000/i },
        { name: "scenario-truncated-wrong-type", mutate: p => { p.result.scenario_results.baseline.truncated = "false"; }, expected: /truncated del escenario baseline debe ser booleano/i },
        { name: "finite-profile-forged-relation-effects", mutate: p => { p.result.scenario_results.baseline.relation_effects = []; }, expected: /Un perfil sin guardas ni prerrequisitos temporales no debe exportar efectos de relaciones ni deshabilitaciones efectivas derivadas/i },
        { name: "finite-profile-forged-effective-disabled", mutate: p => { p.result.scenario_results.baseline.effective_disabled_transitions = []; }, expected: /Un perfil sin guardas ni prerrequisitos temporales no debe exportar efectos de relaciones ni deshabilitaciones efectivas derivadas/i },
        { name: "temporal-profile-missing-prerequisite-summary", mutate: p => { p.input.rule_profile = { type: "temporal_prerequisite_graph", version: "1" }; }, expected: /temporal_prerequisites no coincide con las relaciones temporales de entrada/i }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        if (candidate.result.semantic_identity_version !== undefined) {
          const projected = structuredClone(candidate.result);
          delete projected.delta_reach;
          delete projected.engine_version;
          delete projected.input_sha256;
          delete projected.result_sha256;
          delete projected.semantic_sha256;
          delete projected.semantic_identity_version;
          Object.keys(projected.scenario_results || {}).forEach(id => {
            const scenario = projected.scenario_results[id];
            if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
          });
          Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
            const intervention = projected.comparisons_to_baseline[id].intervention || {};
            if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
          });
          candidate.result.semantic_sha256 = await window.hash(projected, "result");
        }
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const scenarioCase of scenarioResultAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `h2-scenario-result-${scenarioCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(scenarioCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(scenarioCase.expected, "i"),
        `H2: reject malformed scenario-result predicate ${scenarioCase.name}`);
    }

    // H3 grouped comparison schema/semantic adversaries. Keep outer and semantic
    // digests consistent so each candidate reaches its targeted comparison invariant.
    const comparisonAdversaries = await page.evaluate(async (pkg) => {
      const comparisonId = Object.keys(pkg.result.comparisons_to_baseline || {})[0];
      if (!comparisonId) throw new Error("H3 fixture requires at least one baseline comparison.");
      const cases = [
        { name: "comparison-missing-added-list", mutate: cr => { delete cr.enabled_at_initial_added; }, expected: /El campo enabled_at_initial_added de la comparación .* debe ser una lista/i },
        { name: "comparison-removed-states-wrong-type", mutate: cr => { cr.reachable_states_removed = "not-an-array"; }, expected: /El campo reachable_states_removed de la comparación .* debe ser una lista/i },
        { name: "comparison-unknown-key", mutate: cr => { cr.unreviewed_extension = true; }, expected: /La comparación .* contiene campos desconocidos/i },
        { name: "comparison-truncated-wrong-type", mutate: cr => { cr.truncated = "false"; }, expected: /truncated de la comparación .* debe ser booleano/i },
        { name: "comparison-intervention-wrong-type", mutate: cr => { cr.intervention = []; }, expected: /intervention de la comparación .* debe ser un objeto/i },
        { name: "comparison-disabled-transitions-wrong-type", mutate: cr => { cr.intervention.disabled_transitions = "not-an-array"; }, expected: /disabled_transitions de intervention debe ser una lista/i },
        { name: "comparison-invalid-added-trajectory", mutate: cr => { cr.trajectories_added = [[{ state: pkg.input.initial_state }, { state: "STATE_NOT_DECLARED", transition: "TRANSITION_NOT_DECLARED" }]]; }, expected: /trajectories_added en .* debe contener rutas coherentes con las transiciones de entrada/i },
        { name: "comparison-disconnected-added-trajectory", mutate: cr => { cr.trajectories_added = [[{ state: "A" }, { state: "C", transition: "t_ab" }]]; }, expected: /trajectories_added en .* debe contener rutas coherentes con las transiciones de entrada/i }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate.result.comparisons_to_baseline[comparisonId]);
        if (candidate.result.semantic_identity_version !== undefined) {
          const projected = structuredClone(candidate.result);
          delete projected.delta_reach;
          delete projected.engine_version;
          delete projected.input_sha256;
          delete projected.result_sha256;
          delete projected.semantic_sha256;
          delete projected.semantic_identity_version;
          Object.keys(projected.scenario_results || {}).forEach(id => {
            const scenario = projected.scenario_results[id];
            if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
          });
          Object.keys(projected.comparisons_to_baseline || {}).forEach(id => {
            const intervention = projected.comparisons_to_baseline[id].intervention || {};
            if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
          });
          candidate.result.semantic_sha256 = await window.hash(projected, "result");
        }
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const comparisonCase of comparisonAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `h3-comparison-${comparisonCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(comparisonCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(comparisonCase.expected, "i"),
        `H3: reject malformed comparison predicate ${comparisonCase.name}`);
    }

    // H5 grouped numeric-limit adversaries: test lower/upper bounds, integer-only
    // constraints, and declared graph-size caps using correctly refreshed input digests.
    const numericLimitAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "max-depth-negative", mutate: input => { input.exploration.max_depth = -1; }, expected: /max_depth debe ser un entero entre 0 y 100/i },
        { name: "max-depth-over-limit", mutate: input => { input.exploration.max_depth = 101; }, expected: /max_depth debe ser un entero entre 0 y 100/i },
        { name: "max-depth-fractional", mutate: input => { input.exploration.max_depth = 1.5; }, expected: /contiene un número que no es un entero seguro|max_depth debe ser un entero entre 0 y 100/i },
        { name: "max-trajectories-zero", mutate: input => { input.exploration.max_trajectories = 0; }, expected: /max_trajectories debe ser un entero entre 1 y 10000/i },
        { name: "max-trajectories-over-limit", mutate: input => { input.exploration.max_trajectories = 10001; }, expected: /max_trajectories debe ser un entero entre 1 y 10000/i },
        { name: "max-trajectories-fractional", mutate: input => { input.exploration.max_trajectories = 1.5; }, expected: /contiene un número que no es un entero seguro|max_trajectories debe ser un entero entre 1 y 10000/i },
        { name: "states-over-limit", mutate: input => { input.states = input.states.concat(Array.from({ length: 501 - input.states.length }, (_, i) => "H5_EXTRA_STATE_" + i)); }, expected: /El modelo no puede superar 500 estados/i },
        { name: "transitions-over-limit", mutate: input => { input.transitions = input.transitions.concat(Array.from({ length: 2001 - input.transitions.length }, (_, i) => ({ id: "h5_extra_transition_" + i, source: input.initial_state, target: input.initial_state }))); }, expected: /El modelo no puede superar 2000 transiciones/i }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate.input);
        candidate.result.input_sha256 = await window.hash(candidate.input, "input");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const limitCase of numericLimitAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `h5-numeric-limit-${limitCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(limitCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(limitCase.expected, "i"),
        `H5: reject numeric or size limit violation ${limitCase.name}`);
    }

    // H5 inclusive-boundary positive checks use the live validator/engine path.
    // A tiny graph makes the maximum trajectory budget inexpensive while still
    // proving that every documented endpoint is accepted rather than rejected.
    const savedModelText = await page.locator("#model").inputValue();
    const acceptedBoundaryModels = [
      { name: "max-depth-lower-inclusive", max_depth: 0, max_trajectories: 1 },
      { name: "max-depth-upper-inclusive", max_depth: 100, max_trajectories: 1 },
      { name: "max-trajectories-lower-inclusive", max_depth: 0, max_trajectories: 1 },
      { name: "max-trajectories-upper-inclusive", max_depth: 0, max_trajectories: 10000 }
    ];
    for (const boundary of acceptedBoundaryModels) {
      const model = {
        schema_version: "collective-toy-input-001",
        model_id: "h5-boundary-" + boundary.name,
        initial_state: "S",
        states: ["S"],
        transitions: [],
        relations: [],
        rule_profile: { type: "finite_deterministic_graph", version: "1" },
        scenarios: [{ id: "baseline", disabled_transitions: [] }],
        exploration: { max_depth: boundary.max_depth, max_trajectories: boundary.max_trajectories }
      };
      await page.locator("#model").evaluate((el, value) => {
        el.value = JSON.stringify(value, null, 2);
        el.dispatchEvent(new Event("input", { bubbles: true }));
      }, model);
      await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
      await page.waitForFunction(() => {
        const status = document.querySelector("#status");
        return status && !/Validando y ejecutando/.test(status.textContent);
      });
      const boundaryStatus = await page.locator("#status").innerText();
      assert.match(boundaryStatus, /Ejecución completada/i,
        `H5: inclusive numeric boundary must be accepted: ${boundary.name}; got ${boundaryStatus}`);
    }
    await page.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, savedModelText);
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => {
      const status = document.querySelector("#status");
      return status && !/Validando y ejecutando/.test(status.textContent);
    });
    assert.match(await page.locator("#status").innerText(), /Ejecución completada/i,
      "H5: restore canonical model after inclusive-boundary checks");

    // Gate B exact inclusive size limits: call the contract validator directly
    // to isolate acceptance of the documented maxima from rendering/benchmark cost.
    const maximumSizeValidation = await page.evaluate(() => {
      const states = Array.from({ length: 500 }, (_, i) => "MAX_STATE_" + i);
      const transitions = Array.from({ length: 2000 }, (_, i) => ({
        id: "MAX_TRANSITION_" + i, source: "MAX_STATE_0", target: "MAX_STATE_0"
      }));
      const model = {
        schema_version: "collective-toy-input-001", model_id: "h5-inclusive-maximum-sizes",
        initial_state: "MAX_STATE_0", states, transitions, relations: [],
        rule_profile: { type: "finite_deterministic_graph", version: "1" },
        scenarios: [{ id: "baseline", disabled_transitions: [] }],
        exploration: { max_depth: 0, max_trajectories: 1 }
      };
      try { validate(model); return { accepted: true, error: null, states: states.length, transitions: transitions.length }; }
      catch (error) { return { accepted: false, error: String(error && error.message || error), states: states.length, transitions: transitions.length }; }
    });
    assert.equal(maximumSizeValidation.accepted, true,
      "H5: exact maximum sizes (500 states, 2000 transitions) must be accepted; " + maximumSizeValidation.error);
    assert.equal(maximumSizeValidation.states, 500);
    assert.equal(maximumSizeValidation.transitions, 2000);

    // Gate B namespace decision: IDs are unique within their typed collection,
    // not globally across state, transition and scenario namespaces.
    const crossNamespaceCollisionValidation = await page.evaluate(() => {
      const model = {
        schema_version: "collective-toy-input-001", model_id: "h6-cross-namespace-collisions",
        initial_state: "S", states: ["S", "baseline", "t_ab"],
        transitions: [{ id: "S", source: "S", target: "t_ab" }],
        relations: [], rule_profile: { type: "finite_deterministic_graph", version: "1" },
        scenarios: [{ id: "baseline", disabled_transitions: [] }, { id: "t_ab", disabled_transitions: ["S"] }],
        exploration: { max_depth: 1, max_trajectories: 2 }
      };
      try { validate(model); return { accepted: true, error: null }; }
      catch (error) { return { accepted: false, error: String(error && error.message || error) }; }
    });
    assert.equal(crossNamespaceCollisionValidation.accepted, true,
      "H6: equal text IDs across typed namespaces are permitted; " + crossNamespaceCollisionValidation.error);

    // H6 grouped identifier and multiplicity adversaries. Refresh input and package
    // digests to ensure each malformed ID reaches the structural validator.
    const identifierAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "duplicate-state-id", mutate: input => { input.states.push(input.states[0]); }, expected: /Hay IDs de estado duplicados/i },
        { name: "empty-state-id", mutate: input => { input.states[1] = ""; }, expected: /Cada estado debe tener un ID no vacío/i },
        { name: "duplicate-transition-id", mutate: input => { input.transitions[1].id = input.transitions[0].id; }, expected: /ID de transición duplicado/i },
        { name: "empty-transition-id", mutate: input => { input.transitions[0].id = ""; }, expected: /ID, origen y destino deben ser textos no vacíos/i },
        { name: "duplicate-scenario-id", mutate: input => { input.scenarios[1].id = input.scenarios[0].id; }, expected: /ID de escenario duplicado/i },
        { name: "duplicate-disabled-transition-id", mutate: input => { input.scenarios[1].disabled_transitions = [input.transitions[0].id, input.transitions[0].id]; }, expected: /repite un ID/i },
        { name: "unknown-disabled-transition-id", mutate: input => { input.scenarios[1].disabled_transitions = ["TRANSITION_NOT_DECLARED"]; }, expected: /Transición desconocida/i }
      ];
      return Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate.input);
        candidate.result.input_sha256 = await window.hash(candidate.input, "input");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, fc4Package);
    for (const idCase of identifierAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `h6-identifiers-${idCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(idCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), new RegExp(idCase.expected, "i"),
        `H6: reject malformed identifier or multiplicity ${idCase.name}`);
    }

    // FC-5: round-trip a fully assessed FC-4 package through the actual import UI.
    await page.locator("#package-file").setInputFiles({
      name: "assessed-fc4-roundtrip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(fc4Package))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();

    // GT-03 grouped trace metadata adversary: step prerequisites must be exactly those declared by the active rule profile.
    const forgedStepPrerequisites = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      const step = trace.steps.find(s => s.prerequisites.length === 0);
      if (!step) throw new Error("Fixture needs a step with no declared prerequisites");
      const unrelated = candidate.input.transitions.find(t => t.id !== step.transition_id);
      if (!unrelated) throw new Error("Fixture needs an unrelated known transition");
      step.prerequisites = [unrelated.id];
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace);
      candidate.outcome_record.execution_trace_sha256 = trace.trace_sha256;
      candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "trace-forged-step-prerequisites.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedStepPrerequisites))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /prerequisites del paso no coincide con las relaciones temporales declaradas para el perfil activo/i,
      "FC-5/FC-6: reject forged step prerequisite metadata even when trace/package digests are recomputed");

    // GT-03 grouped trace-context adversary: the trace initial state must be bound to the model's declared initial state.
    const forgedTraceInitialState = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      const alternate = candidate.input.states.find(state => state !== candidate.input.initial_state);
      if (!alternate) throw new Error("Fixture needs an alternate declared state");
      trace.initial_state = alternate;
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace);
      candidate.outcome_record.execution_trace_sha256 = trace.trace_sha256;
      candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "trace-forged-initial-state.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedTraceInitialState))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /initial_state de la traza no coincide con el estado inicial del modelo/i,
      "FC-5/FC-6: reject trace whose known initial state contradicts the declared model initial state despite recomputed dependent digests");

    // GT-05 grouped semantic trace adversary: a re-hashed trace must still follow the model's actual edges.
    const forgedTraceEdge = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (!trace.steps.length) throw new Error("Fixture needs at least one executed trace step");
      const first = trace.steps[0];
      const edge = candidate.input.transitions.find(t => t.id === first.transition_id);
      if (!edge) throw new Error("Fixture trace must reference an existing transition");
      const impossibleTarget = candidate.input.states.find(state => state !== edge.source && state !== edge.target);
      if (!impossibleTarget) throw new Error("Fixture needs a declared non-edge target state");
      first.state_after = impossibleTarget;
      // Recompute every enclosing digest so the importer must validate semantic trace coherence,
      // not merely detect a stale checksum.
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace);
      candidate.outcome_record.execution_trace_sha256 = trace.trace_sha256;
      candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "trace-forged-edge-with-recomputed-digests.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedTraceEdge))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /secuencia de estados\/transiciones de la traza no es coherente con la entrada/i,
      "GT-05/FC5-TRACE-012: reject a re-hashed trace step that does not follow its declared transition edge");

    // GT-03 grouped trace-contract adversaries: schema closure, trace metadata, ordered steps, and history.
    const traceContractAdversaries = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "unknown-trace-key", mutate: trace => { trace.uncontracted_field = "must-reject"; } },
        { name: "negative-candidate-index", mutate: trace => { trace.candidate_index = -1; } },
        { name: "unknown-submitted-transition", mutate: trace => { trace.submitted_transition_ids[0] = "TRANSITION_NOT_DECLARED"; } },
        { name: "wrong-type-submitted-transition-array", mutate: trace => { trace.submitted_transition_ids = "not-an-array"; } },
        { name: "non-string-submitted-transition-id", mutate: trace => { trace.submitted_transition_ids[0] = 7; } },
        { name: "unknown-initial-state", mutate: trace => { trace.initial_state = "STATE_NOT_DECLARED"; } },
        { name: "empty-execution-id", mutate: trace => { trace.execution_id = ""; } },
        { name: "missing-execution-id", mutate: trace => { delete trace.execution_id; } },
        { name: "wrong-type-model-id", mutate: trace => { trace.model_id = []; } },
        { name: "empty-scenario-id", mutate: trace => { trace.scenario_id = " "; } },
        { name: "wrong-type-execution-id", mutate: trace => { trace.execution_id = []; } },
        { name: "whitespace-execution-id", mutate: trace => { trace.execution_id = " "; } },
        { name: "missing-model-id", mutate: trace => { delete trace.model_id; } },
        { name: "whitespace-model-id", mutate: trace => { trace.model_id = " "; } },
        { name: "missing-scenario-id", mutate: trace => { delete trace.scenario_id; } },
        { name: "wrong-type-scenario-id", mutate: trace => { trace.scenario_id = []; } },
        { name: "unknown-final-state", mutate: trace => { trace.final_state = "STATE_NOT_DECLARED"; } },
        { name: "wrong-type-steps-array", mutate: trace => { trace.steps = "not-an-array"; } },
        { name: "out-of-order-step-index", mutate: trace => { trace.steps[0].step = 2; } },
        { name: "forged-prior-transition-history", mutate: trace => { trace.steps[1].prior_transitions = []; } },
        { name: "unknown-step-key", mutate: trace => { trace.steps[0].uncontracted_field = "must-reject"; } },
        { name: "wrong-type-step-prerequisites", mutate: trace => { trace.steps[0].prerequisites = "not-an-array"; } }
      ];
      return await Promise.all(cases.map(async item => {
        const candidate = structuredClone(pkg);
        const trace = candidate.concrete_execution_trace;
        if (!trace || trace.steps.length < 2) throw new Error("GT-03 trace fixture needs at least two completed steps");
        item.mutate(trace);
        delete trace.trace_sha256;
        trace.trace_sha256 = await window.hash(trace);
        candidate.outcome_record.execution_trace_sha256 = trace.trace_sha256;
        candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate };
      }));
    }, fc4Package);
    const traceContractDiagnostics = {
      "unknown-trace-key": /traza contiene campos desconocidos o ausentes/i,
      "negative-candidate-index": /candidate_index debe ser null o un entero no negativo/i,
      "unknown-submitted-transition": /submitted_transition_ids debe contener únicamente IDs de transiciones existentes/i,
      "wrong-type-submitted-transition-array": /submitted_transition_ids debe contener únicamente IDs de transiciones existentes/i,
      "non-string-submitted-transition-id": /submitted_transition_ids debe contener únicamente IDs de transiciones existentes/i,
      "unknown-initial-state": /estados inicial\/final de la traza deben existir en la entrada/i,
      "empty-execution-id": /resultado no está vinculado a la traza de ejecución exportada/i,
      "missing-execution-id": /resultado no está vinculado a la traza de ejecución exportada o requiere una traza COMPLETED/i,
      "wrong-type-model-id": /El model_id del resultado no coincide con la entrada y la traza exportadas/i,
      "empty-scenario-id": /El scenario_id del resultado no coincide con la traza exportada/i,
      "wrong-type-execution-id": /El resultado no está vinculado a la traza de ejecución exportada o requiere una traza COMPLETED/i,
      "whitespace-execution-id": /El resultado no está vinculado a la traza de ejecución exportada o requiere una traza COMPLETED/i,
      "missing-model-id": /El model_id del resultado no coincide con la entrada y la traza exportadas/i,
      "whitespace-model-id": /El model_id del resultado no coincide con la entrada y la traza exportadas/i,
      "missing-scenario-id": /El scenario_id del resultado no coincide con la traza exportada/i,
      "wrong-type-scenario-id": /El scenario_id del resultado no coincide con la traza exportada/i,
      "unknown-final-state": /estados inicial\/final de la traza deben existir en la entrada/i,
      "wrong-type-steps-array": /steps de la traza debe ser una lista/i,
      "out-of-order-step-index": /numeración o los tipos del paso son inválidos/i,
      "forged-prior-transition-history": /prior_transitions no coincide con el prefijo ejecutado/i,
      "unknown-step-key": /paso malformado o con campos desconocidos/i,
      "wrong-type-step-prerequisites": /prerequisites del paso contiene IDs inválidos/i
    };
    for (const traceCase of traceContractAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `gt03-trace-contract-${traceCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(traceCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), traceContractDiagnostics[traceCase.name],
        `GT-03: reject ${traceCase.name} after recomputing trace/outcome/assessment/package digests`);
    }

    // GT-05 historical profile: v1 package without semantic-identity fields uses only the documented legacy replay projection.
    const historicalV1 = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_version = "collective-toy-browser-run-001";
      delete candidate.package_stage;
      delete candidate.result.delta_reach;
      delete candidate.result.semantic_identity_version;
      delete candidate.result.semantic_sha256;
      delete candidate.package_sha256;
      delete candidate.result.result_sha256;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody);
      candidate.package_sha256 = await window.hash(candidate);
      return candidate;
    }, packageData);
    await page.locator("#package-file").setInputFiles({
      name: "historical-v1-without-semantic-identity.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(historicalV1))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.waitForFunction(() => {
      const state = document.querySelector("#package-assessment")?.dataset.state;
      return state && state !== "idle" && state !== "validating";
    }, { timeout: 30000 });
    const historicalAssessmentState = await page.locator("#package-assessment").getAttribute("data-state");
    const historicalAssessmentMessage = await page.locator("#package-assessment").innerText();
    assert.equal(historicalAssessmentState, "rejected",
      "GT-05/FC5-REPLAY-003: legacy-shaped package without explicit NOT_ASSESSED status must fail closed under the current envelope contract");
    assert.match(historicalAssessmentMessage, /value_assessment_status=NOT_ASSESSED/i,
      "GT-05/FC5-REPLAY-003: rejection must identify the missing explicit assessment status");

    // The explicitly declared legacy profile is replayable when its required lifecycle status is present.
    const historicalV1WithStatus = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_version = "collective-toy-browser-run-001";
      delete candidate.package_stage;
      delete candidate.result.delta_reach;
      delete candidate.result.semantic_identity_version;
      delete candidate.result.semantic_sha256;
      candidate.value_assessment_status = "NOT_ASSESSED";
      delete candidate.package_sha256;
      delete candidate.result.result_sha256;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody);
      candidate.package_sha256 = await window.hash(candidate);
      return candidate;
    }, packageData);
    await page.locator("#package-file").setInputFiles({
      name: "historical-v1-explicit-not-assessed.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(historicalV1WithStatus))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor({ timeout: 10000 });
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-05/FC5-REPLAY-003: explicitly supported historical v1 projection with NOT_ASSESSED must replay independently");

    // The preceding assertion is intentionally scoped to the successful assessed round-trip.
    // After the adversarial import, the package assessment is expected to be rejected.
    // FC-5: the same explicit outcome without a complete valuation must round-trip as NOT_ASSESSED.
    const unassessedOutcomePackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.value_assessment;
      candidate.package_stage = "OUTCOME";
      candidate.value_assessment_status = "NOT_ASSESSED";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "outcome-not-assessed-roundtrip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unassessedOutcomePackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.equal(unassessedOutcomePackage.value_assessment_status, "NOT_ASSESSED",
      "FC-5: outcome without complete contextual valuation must retain explicit NOT_ASSESSED");
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "FC-5: NOT_ASSESSED outcome package must replay after import");

    // FC-5 grouped status-enum adversary: reject unknown, null and non-string valuation states.
    const invalidAssessmentStatuses = await page.evaluate(async (pkg) => {
      const values = [
        { name: "unknown-string", value: "PENDING_REVIEW" },
        { name: "null", value: null },
        { name: "numeric", value: 1 },
        { name: "empty-string", value: "" },
        { name: "boolean", value: false },
        { name: "object", value: { status: "NOT_ASSESSED" } }
      ];
      return Promise.all(values.map(async (item) => {
        const candidate = structuredClone(pkg);
        candidate.value_assessment_status = item.value;
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate };
      }));
    }, unassessedOutcomePackage);
    for (const statusCase of invalidAssessmentStatuses) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-assessment-status-${statusCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(statusCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /value_assessment_status=NOT_ASSESSED/i,
        `FC-5: importer must diagnose invalid assessment status ${statusCase.name}`);
    }

    assert.equal(invalidAssessmentStatuses.length, 6,
      "FC-5 H4: status matrix must include unknown string, null, number, empty string, boolean and object");
    
    // FC-5 adversarial case: a forged outcome digest must be rejected even when package hash is recomputed.
    const forgedAssessmentDigest = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment.outcome_sha256 = "0".repeat(64);
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-assessment-outcome-digest.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedAssessmentDigest))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /hash del resultado de valoración no coincide/i,
      "FC-5: importer must reject a forged outcome digest despite a recomputed package hash");

    // FC-5: trace linkage must fail closed even if the outer package digest is recomputed.
    const forgedTraceLink = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.outcome_record.execution_trace_sha256 = "0".repeat(64);
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-outcome-trace-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedTraceLink))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /hash de traza del resultado no coincide/i,
      "FC-5: importer must reject a forged outcome-to-trace link");

    // FC-5: assessment-to-outcome linkage and required contextual fields must be enforced.
    const forgedAssessmentLink = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment.outcome_id = "outcome-not-in-package";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-assessment-outcome-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedAssessmentLink))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /no está vinculada al resultado y ejecución exportados/i,
      "FC-5: importer must reject an assessment linked to another outcome");

    const incompleteAssessment = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.value_assessment.criterion;
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "incomplete-contextual-assessment.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(incompleteAssessment))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /valoración está incompleta/i,
      "FC-5: importer must reject missing contextual assessment fields");

    // FC-5: reject unknown top-level package fields even when the package digest is recomputed.
    const unknownPackageField = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.uncontracted_extension = { injected: true };
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "unknown-package-field.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownPackageField))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /paquete contiene campos desconocidos/i,
      "FC-5: importer must reject unknown package fields despite a recomputed package digest");

    // FC-5: reject a missing required top-level input field, even with a recomputed package digest.
    const missingPackageInput = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.input;
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "missing-package-input.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(missingPackageInput))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /falta input o no es un objeto/i,
      "FC-5: importer must reject a missing required input field despite a recomputed package digest");

    // FC-5: reject a missing required result field, even with a recomputed package digest.
    const missingPackageResult = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.result;
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "missing-package-result.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(missingPackageResult))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /falta result o no es un objeto/i,
      "FC-5: importer must reject a missing required result field despite a recomputed package digest");

    // FC-5: a package with an outcome must include the concrete execution trace it references.
    const missingPackageTrace = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.concrete_execution_trace;
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "missing-package-trace.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(missingPackageTrace))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /resultado no está vinculado a la traza de ejecución exportada/i,
      "FC-5: importer must reject an outcome whose concrete execution trace is missing");

    // FC-5/FC-6 grouped trace-coherence adversary: blocked traces must not smuggle unknown IDs in the unexecuted suffix.
    const unknownBlockedTraceId = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      if (candidate.package_version !== "collective-toy-browser-run-002") {
        throw new Error("GT-03 requires the versioned package schema that supports BLOCKED traces");
      }
      const trace = candidate.concrete_execution_trace;
      trace.status = "BLOCKED";
      trace.submitted_transition_ids = [...trace.steps.map(step => step.transition_id), "transition-not-in-model"];
      trace.blocked_step = {
        index: trace.steps.length + 1,
        transition_id: "transition-not-in-model",
        reason: "adversarial unknown transition after valid executed prefix",
        required_transition_ids: []
      };
      delete candidate.outcome_record;
      delete candidate.value_assessment;
      candidate.value_assessment_status = "NOT_ASSESSED";
      candidate.package_stage = "EXECUTION";
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-unknown-submitted-id.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownBlockedTraceId))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /submitted_transition_ids debe contener únicamente IDs de transiciones existentes/i,
      "FC-5/FC-6: reject a BLOCKED trace whose unexecuted submitted suffix references an unknown transition despite recomputed trace/package digests");
    // GT-03 grouped trace-coherence adversary: a BLOCKED trace must preserve the exact submitted prefix that was executed.
    const mismatchedBlockedPrefix = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (trace.status !== "BLOCKED" || trace.steps.length < 1) throw new Error("Fixture must be a BLOCKED trace with a non-empty executed prefix");
      const executedFirst = trace.steps[0].transition_id;
      const blockedId = trace.blocked_step.transition_id;
      const alternate = candidate.input.transitions.find(t => t.id !== executedFirst && t.id !== blockedId);
      if (!alternate) throw new Error("Fixture needs another known transition ID for prefix tampering");
      trace.submitted_transition_ids[0] = alternate.id;
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-mismatched-submitted-prefix.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(mismatchedBlockedPrefix))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /traza BLOCKED debe coincidir con el prefijo de transiciones enviadas/i,
      "FC-5/FC-6: reject a BLOCKED trace whose executed steps differ from the submitted sequence prefix despite recomputed digests");

    // FC5-TRACE-005: a trace cannot refer to a scenario absent from its own exported input.
    const unknownTraceScenario = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.concrete_execution_trace.scenario_id = "scenario-not-declared";
      delete candidate.concrete_execution_trace.trace_sha256;
      candidate.concrete_execution_trace.trace_sha256 = await window.hash(candidate.concrete_execution_trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-unknown-scenario.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownTraceScenario))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /scenario_id de la traza no existe en la entrada/i,
      "FC5-TRACE-005: reject unknown trace scenario even after refreshing trace and package digests");

    // FC5-TRACE-017 grouped lifecycle coherence: block index and last valid state must match the executed prefix.
    const blockedLifecycleAdversaries = await page.evaluate(async (pkg) => {
      const makeCandidate = async (mutate) => {
        const candidate = structuredClone(pkg);
        const trace = candidate.concrete_execution_trace;
        if (trace.status !== "BLOCKED" || !trace.blocked_step || trace.steps.length < 1) {
          throw new Error("FC5-TRACE-017 fixture must be a BLOCKED trace with a non-empty valid prefix");
        }
        mutate(trace);
        delete trace.trace_sha256;
        trace.trace_sha256 = await window.hash(trace, "sequence_trace");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return candidate;
      };
      return [
        {
          name: "blocked-index-does-not-follow-prefix",
          candidate: await makeCandidate(trace => { trace.blocked_step.index = trace.steps.length + 2; }),
          diagnostic: /El paso bloqueado no es coherente con la secuencia intentada/i
        },
        {
          name: "blocked-final-state-disagrees-with-last-valid-state",
          candidate: await makeCandidate(trace => { trace.final_state = trace.initial_state; }),
          diagnostic: /final_state no coincide con el último estado válido de la traza/i
        },
        {
          name: "blocked-step-unknown-key",
          candidate: await makeCandidate(trace => { trace.blocked_step.uncontracted_field = "must-reject"; }),
          diagnostic: /Una traza BLOCKED debe conservar los metadatos del bloqueo/i
        },
        {
          name: "blocked-step-required-transition-ids-wrong-type",
          candidate: await makeCandidate(trace => { trace.blocked_step.required_transition_ids = "not-an-array"; }),
          diagnostic: /required_transition_ids del bloqueo contiene IDs inválidos/i
        }
      ];
    }, blockedPackage);
    for (const blockedCase of blockedLifecycleAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `blocked-lifecycle-${blockedCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(blockedCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), blockedCase.diagnostic,
        `FC5-TRACE-017: reject incoherent BLOCKED lifecycle predicate ${blockedCase.name}`);
    }

    // FC5-TRACE-016 grouped COMPLETED lifecycle adversaries: no blocked step and final state must match executed steps.
    const completedLifecycleAdversaries = await page.evaluate(async (pkg) => {
      const makeCandidate = async (mutate) => {
        const candidate = structuredClone(pkg);
        const trace = candidate.concrete_execution_trace;
        if (trace.status !== "COMPLETED" || trace.steps.length < 1) {
          throw new Error("FC5-TRACE-016 fixture must be a COMPLETED trace with at least one executed step");
        }
        mutate(trace);
        delete trace.trace_sha256;
        trace.trace_sha256 = await window.hash(trace, "sequence_trace");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return candidate;
      };
      return [
        {
          name: "completed-trace-has-blocked-step",
          candidate: await makeCandidate(trace => {
            trace.blocked_step = {
              index: trace.steps.length + 1,
              transition_id: trace.submitted_transition_ids[trace.steps.length] || trace.steps[trace.steps.length - 1].transition_id,
              reason: "forged-block",
              required_transition_ids: []
            };
          }),
          diagnostic: /Una traza COMPLETED no puede incluir blocked_step/i
        },
        {
          name: "completed-final-state-disagrees-with-executed-sequence",
          candidate: await makeCandidate(trace => { trace.final_state = trace.initial_state; }),
          diagnostic: /final_state no coincide con el último estado válido de la traza/i
        },
        {
          name: "executed-step-unknown-key",
          candidate: await makeCandidate(trace => { trace.steps[0].uncontracted_field = "must-reject"; }),
          diagnostic: /La traza contiene un paso malformado o con campos desconocidos/i
        },
        {
          name: "executed-step-prerequisites-wrong-type",
          candidate: await makeCandidate(trace => { trace.steps[0].prerequisites = "not-an-array"; }),
          diagnostic: /prerequisites del paso contiene IDs inválidos/i
        }
      ];
    }, evidencePackage);
    for (const completedCase of completedLifecycleAdversaries) {
      await page.locator("#package-file").setInputFiles({
        name: `completed-lifecycle-${completedCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(completedCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), completedCase.diagnostic,
        `FC5-TRACE-016: reject incoherent COMPLETED lifecycle predicate ${completedCase.name}`);
    }

    // GT-03 grouped semantic adversary: the blocked reason and missing-prerequisite list must be derived from model + executed history.
    const forgedBlockedPrerequisites = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (trace.blocked_step.reason !== "temporal_prerequisite_not_satisfied" || trace.blocked_step.required_transition_ids.length < 1) {
        throw new Error("Fixture must be blocked by at least one unsatisfied temporal prerequisite");
      }
      trace.blocked_step.required_transition_ids = [];
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-forged-prerequisites.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedBlockedPrerequisites))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /required_transition_ids del bloqueo no coincide con los prerrequisitos realmente ausentes/i,
      "FC-5/FC-6: reject a BLOCKED trace that omits required missing prerequisites despite recomputed trace/package digests");

    // GT-03 paired semantic adversary: a BLOCKED trace cannot forge its reason while keeping all IDs and digests structurally valid.
    const forgedBlockedReason = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (trace.blocked_step.reason !== "temporal_prerequisite_not_satisfied") throw new Error("Fixture must use a temporal-prerequisite block");
      trace.blocked_step.reason = "transition_source_mismatch";
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-forged-reason.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedBlockedReason))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /El motivo del bloqueo no coincide con el contexto del escenario de la traza, el estado y los prerrequisitos/i,
      "FC-5/FC-6: reject a forged blocked reason despite recomputed trace/package digests");




    // FC-5: reject an unsupported package schema version even if the package digest is recomputed.
    const unsupportedPackageVersion = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_version = "collective-toy-browser-run-999";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "unsupported-package-version.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unsupportedPackageVersion))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /esquema de paquete desconocido o no compatible/i,
      "FC-5: importer must reject an unsupported package schema version despite a recomputed digest");

    // FC-5: reject unknown result fields even when all enclosing package hashes are recomputed.
    const unknownResultField = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.uncontracted_result_extension = { injected: true };
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "unknown-result-field.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownResultField))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /el resultado contiene campos desconocidos/i,
      "FC-5: importer must reject unknown result fields despite recomputed result and package hashes");

    // FC-5: outcome execution identifier must match the exported concrete trace.
    const forgedOutcomeExecution = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.outcome_record.execution_id = "sequence-execution-not-in-trace";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-outcome-execution-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedOutcomeExecution))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /resultado no está vinculado a la traza de ejecución exportada/i,
      "FC-5: importer must reject an outcome execution ID that differs from its trace");

    // FC-5: assessment execution identifier must match both the outcome and exported trace.
    const forgedAssessmentExecution = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.value_assessment.execution_id = "sequence-execution-not-in-trace";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-assessment-execution-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedAssessmentExecution))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /valoración no está vinculada al resultado y ejecución exportados/i,
      "FC-5: importer must reject an assessment execution ID that differs from its outcome");

    // FC-5: explicit outcome model identity must match the exported input and trace.
    const forgedOutcomeModel = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.outcome_record.model_id = "model-not-in-package";
      candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-outcome-model-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedOutcomeModel))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /model_id del resultado no coincide con la entrada y la traza exportadas/i,
      "FC-5: importer must reject an outcome model ID that differs from the package input/trace");

    // FC-5: outcome scenario identity must match the exported concrete trace.
    const forgedOutcomeScenario = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.outcome_record.scenario_id = "scenario-not-in-trace";
      candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "forged-outcome-scenario-link.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedOutcomeScenario))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /scenario_id del resultado no coincide con la traza exportada/i,
      "FC-5: importer must reject an outcome scenario ID that differs from the trace");

    // FC5-TRACE-004/018: trace must bind to the exported input and its own digest must be well-formed and recomputed.
    const traceIntegrityCases = await page.evaluate(async (pkg) => {
      const wrongInput = structuredClone(pkg);
      wrongInput.concrete_execution_trace.input_sha256 = "e".repeat(64);
      delete wrongInput.concrete_execution_trace.trace_sha256;
      wrongInput.concrete_execution_trace.trace_sha256 = await window.hash(wrongInput.concrete_execution_trace, "sequence_trace");
      wrongInput.outcome_record.execution_trace_sha256 = wrongInput.concrete_execution_trace.trace_sha256;
      wrongInput.value_assessment.outcome_sha256 = await window.hash(wrongInput.outcome_record, "outcome_record");
      delete wrongInput.package_sha256;
      wrongInput.package_sha256 = await window.hash(wrongInput, "package_export");

      const malformedTraceDigest = structuredClone(pkg);
      malformedTraceDigest.concrete_execution_trace.trace_sha256 = "not-a-sha256";
      malformedTraceDigest.outcome_record.execution_trace_sha256 = malformedTraceDigest.concrete_execution_trace.trace_sha256;
      malformedTraceDigest.value_assessment.outcome_sha256 = await window.hash(malformedTraceDigest.outcome_record, "outcome_record");
      delete malformedTraceDigest.package_sha256;
      malformedTraceDigest.package_sha256 = await window.hash(malformedTraceDigest, "package_export");

      const incorrectTraceDigest = structuredClone(pkg);
      incorrectTraceDigest.concrete_execution_trace.trace_sha256 = "f".repeat(64);
      incorrectTraceDigest.outcome_record.execution_trace_sha256 = incorrectTraceDigest.concrete_execution_trace.trace_sha256;
      incorrectTraceDigest.value_assessment.outcome_sha256 = await window.hash(incorrectTraceDigest.outcome_record, "outcome_record");
      delete incorrectTraceDigest.package_sha256;
      incorrectTraceDigest.package_sha256 = await window.hash(incorrectTraceDigest, "package_export");

      return [
        { name: "trace-input-hash-mismatch", candidate: wrongInput, diagnostic: /input_sha256 de la traza no coincide con la entrada exportada/i },
        { name: "trace-digest-malformed", candidate: malformedTraceDigest, diagnostic: /trace_sha256 ausente o malformado/i },
        { name: "trace-digest-incorrect", candidate: incorrectTraceDigest, diagnostic: /hash de la traza concreta no coincide/i }
      ];
    }, fc4Package);
    for (const traceCase of traceIntegrityCases) {
      await page.locator("#package-file").setInputFiles({
        name: `forged-trace-integrity-${traceCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(traceCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), traceCase.diagnostic,
        `FC5-TRACE-004/018: reject ${traceCase.name} after refreshing dependent digests`);
    }

    // FC-5 grouped linkage integrity: trace digest, assessment outcome identity, and outcome digest.
    const forgedOutcomeAssessmentLinks = await page.evaluate(async (pkg) => {
      const traceDigest = structuredClone(pkg);
      traceDigest.outcome_record.execution_trace_sha256 = "f".repeat(64);
      traceDigest.value_assessment.outcome_sha256 = await window.hash(traceDigest.outcome_record, "outcome_record");
      delete traceDigest.package_sha256;
      traceDigest.package_sha256 = await window.hash(traceDigest, "package_export");

      const assessmentOutcome = structuredClone(pkg);
      assessmentOutcome.value_assessment.outcome_id = "outcome-not-in-package";
      delete assessmentOutcome.package_sha256;
      assessmentOutcome.package_sha256 = await window.hash(assessmentOutcome, "package_export");

      const assessmentDigest = structuredClone(pkg);
      assessmentDigest.value_assessment.outcome_sha256 = "a".repeat(64);
      delete assessmentDigest.package_sha256;
      assessmentDigest.package_sha256 = await window.hash(assessmentDigest, "package_export");

      return [
        { name: "outcome-trace-digest-mismatch", candidate: traceDigest, diagnostic: /hash de traza del resultado no coincide/i },
        { name: "assessment-outcome-id-mismatch", candidate: assessmentOutcome, diagnostic: /valoración no está vinculada al resultado y ejecución exportados/i },
        { name: "assessment-outcome-digest-mismatch", candidate: assessmentDigest, diagnostic: /hash del resultado de valoración no coincide/i }
      ];
    }, fc4Package);
    for (const linkCase of forgedOutcomeAssessmentLinks) {
      await page.locator("#package-file").setInputFiles({
        name: `forged-linkage-${linkCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(linkCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), linkCase.diagnostic,
        `FC-5: importer must reject linkage-integrity violation ${linkCase.name}`);
    }

    // FC-5 grouped type adversaries: outcome and assessment records must remain JSON objects.
    const invalidRecordTypes = await page.evaluate(async (pkg) => {
      const cases = [];
      for (const item of [
        { name: "outcome-null", key: "outcome_record", value: null },
        { name: "outcome-array", key: "outcome_record", value: [] },
        { name: "outcome-string", key: "outcome_record", value: "not-an-object" },
        { name: "outcome-number", key: "outcome_record", value: 7 },
        { name: "assessment-null", key: "value_assessment", value: null },
        { name: "assessment-array", key: "value_assessment", value: [] },
        { name: "assessment-string", key: "value_assessment", value: "not-an-object" },
        { name: "assessment-number", key: "value_assessment", value: 7 }
      ]) {
        const candidate = structuredClone(pkg);
        candidate[item.key] = item.value;
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        cases.push({ name: item.name, candidate });
      }
      return cases;
    }, fc4Package);
    for (const typeCase of invalidRecordTypes) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-record-type-${typeCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(typeCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /resultado|valoraci[oó]n|objeto|estructura|incomplet/i,
        `FC-5: importer must reject non-object record ${typeCase.name}`);
    }

    // FC-5 grouped per-field type adversaries for mandatory outcome and valuation context.
    const invalidRequiredFieldTypes = await page.evaluate(async (pkg) => {
      const cases = [];
      const invalidValues = [
        { suffix: "null", value: null },
        { suffix: "array", value: [] },
        { suffix: "number", value: 17 }
      ];
      for (const field of ["outcome_id", "value"]) {
        for (const invalid of invalidValues) {
          const candidate = structuredClone(pkg);
          candidate.outcome_record[field] = invalid.value;
          candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
          delete candidate.package_sha256;
          candidate.package_sha256 = await window.hash(candidate, "package_export");
          cases.push({ name: `outcome-${field}-${invalid.suffix}`, candidate });
        }
      }
      for (const field of ["observer", "context", "criterion", "valuation_rule", "rationale"]) {
        for (const invalid of invalidValues) {
          const candidate = structuredClone(pkg);
          candidate.value_assessment[field] = invalid.value;
          delete candidate.package_sha256;
          candidate.package_sha256 = await window.hash(candidate, "package_export");
          cases.push({ name: `assessment-${field}-${invalid.suffix}`, candidate });
        }
      }
      return cases;
    }, fc4Package);
    for (const fieldCase of invalidRequiredFieldTypes) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-required-field-type-${fieldCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(fieldCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /resultado|valoraci[oó]n|campo|incomplet|identificador|valor/i,
        `FC-5: importer must reject invalid required-field type ${fieldCase.name}`);
    }

    // GT-04 grouped enum/blank-field adversaries for outcome and contextual assessment.
    const invalidOutcomeAssessmentSemantics = await page.evaluate(async (pkg) => {
      const cases = [];
      for (const item of [
        { name: "outcome-invalid-source-kind", mutate: p => { p.outcome_record.source_kind = "inferred"; } },
        { name: "outcome-blank-unit", mutate: p => { p.outcome_record.unit = "  "; } },
        { name: "outcome-blank-timing", mutate: p => { p.outcome_record.timing = ""; } },
        { name: "outcome-blank-provenance", mutate: p => { p.outcome_record.provenance = " "; } },
        { name: "outcome-blank-id", mutate: p => { p.outcome_record.outcome_id = " "; p.value_assessment.outcome_id = " "; } },
        { name: "outcome-blank-value", mutate: p => { p.outcome_record.value = ""; } },
        { name: "outcome-unit-wrong-type", mutate: p => { p.outcome_record.unit = 17; } },
        { name: "outcome-timing-wrong-type", mutate: p => { p.outcome_record.timing = []; } },
        { name: "outcome-provenance-wrong-type", mutate: p => { p.outcome_record.provenance = null; } },
        { name: "assessment-invalid-status", mutate: p => { p.value_assessment.status = "NOT_ASSESSED"; } },
        { name: "assessment-blank-observer", mutate: p => { p.value_assessment.observer = " "; } },
        { name: "assessment-blank-context", mutate: p => { p.value_assessment.context = ""; } },
        { name: "assessment-blank-criterion", mutate: p => { p.value_assessment.criterion = " "; } },
        { name: "assessment-blank-valuation-rule", mutate: p => { p.value_assessment.valuation_rule = " "; } },
        { name: "assessment-blank-rationale", mutate: p => { p.value_assessment.rationale = ""; } },
        { name: "assessment-valuation-rule-wrong-type", mutate: p => { p.value_assessment.valuation_rule = []; } },
        { name: "assessment-rationale-wrong-type", mutate: p => { p.value_assessment.rationale = 7; } },
        { name: "outcome-value-wrong-type", mutate: p => { p.outcome_record.value = []; } },
        { name: "outcome-uncertainty-null", mutate: p => { p.outcome_record.uncertainty_status = null; } },
        { name: "outcome-uncertainty-array", mutate: p => { p.outcome_record.uncertainty_status = []; } }
      ]) {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        cases.push({ name: item.name, candidate });
      }
      return cases;
    }, fc4Package);
    const invalidOutcomeAssessmentDiagnostics = {
      "outcome-invalid-source-kind": /source_kind del resultado no es válido/i,
      "outcome-blank-unit": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-blank-timing": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-blank-provenance": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-blank-id": /El resultado explícito carece de identificador o valor/i,
      "outcome-blank-value": /El resultado explícito carece de identificador o valor/i,
      "outcome-unit-wrong-type": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-timing-wrong-type": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-provenance-wrong-type": /campos obligatorios vacíos o de tipo incorrecto/i,
      "assessment-invalid-status": /esquema o estado de valoración desconocido/i,
      "assessment-blank-observer": /valoración está incompleta/i,
      "assessment-blank-context": /valoración está incompleta/i,
      "assessment-blank-criterion": /valoración está incompleta/i,
      "assessment-blank-valuation-rule": /valoración está incompleta/i,
      "assessment-blank-rationale": /valoración está incompleta/i,
      "assessment-valuation-rule-wrong-type": /valoración está incompleta/i,
      "assessment-rationale-wrong-type": /valoración está incompleta/i,
      "outcome-value-wrong-type": /El resultado explícito carece de identificador o valor/i,
      "outcome-uncertainty-null": /campos obligatorios vacíos o de tipo incorrecto/i,
      "outcome-uncertainty-array": /campos obligatorios vacíos o de tipo incorrecto/i
    };
    for (const semanticCase of invalidOutcomeAssessmentSemantics) {
      await page.locator("#package-file").setInputFiles({
        name: `gt04-outcome-assessment-${semanticCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(semanticCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), invalidOutcomeAssessmentDiagnostics[semanticCase.name],
        `GT-04: reject ${semanticCase.name} after recomputing dependent digests`);
    }

    // FC-4 contract-first: baseline/intervention reachability delta must be explicit and auditable.
    await page.getByRole("button", { name: "Cargar ejemplo" }).click();
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => /Ejecución completada|No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""), { timeout: 10000 });
    assert.match(await page.locator("#status").innerText(), /Ejecución completada/i,
      "FC-4: baseline/intervention fixture must execute before delta assertions");
    const accessTrace = page.locator("#results [data-accessibility-transition]");
    assert.ok(await accessTrace.count() >= 8, "FC-2: each transition in each scenario must expose an accessibility trace row");
    for (const row of await accessTrace.all()) {
      const status = await row.getAttribute("data-accessibility-status");
      const text = await row.innerText();
      assert.ok(status, "FC-2: every transition trace row must expose a non-empty status");
      assert.match(text, /— .+\.$/, "FC-2: every transition trace row must expose a human-readable reason");
    }
    assert.match(await page.locator("#results").innerText(), /Trazabilidad de accesibilidad por transición/i,
      "FC-2: result panel must label the rule/accessibility trace");
    assert.match(await page.locator("#results").innerText(), /t_ab.*HABILITADA EN INICIO/i,
      "FC-2: trace must explain why an initially accessible transition is enabled");
    assert.match(await page.locator("#results").innerText(), /t_bd.*NO HABILITADA EN INICIO.*origen no es el estado inicial/i,
      "FC-2: trace must explain why a transition from a non-initial state is not initially enabled");
    assert.match(await page.locator("#results").innerText(), /t_ac.*DESHABILITADA.*explícitamente/i,
      "FC-2: trace must explain scenario-level transition disabling");
    const deltaDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const deltaDownload = await deltaDownloadPromise;
    const deltaPackage = JSON.parse(fs.readFileSync(await deltaDownload.path(), "utf8"));
    const delta = deltaPackage.result.delta_reach?.block_ac;
    assert.ok(delta, "FC-4: export must contain an explicit delta_reach artifact for the intervention");
    assert.match(delta.baseline_source_sha256 || "", /^[a-f0-9]{64}$/i,
      "FC-4: delta_reach must identify the baseline source by SHA-256");
    assert.match(delta.intervention_source_sha256 || "", /^[a-f0-9]{64}$/i,
      "FC-4: delta_reach must identify the intervention source by SHA-256");
    assert.deepEqual(delta.reachable_states_added, [], "FC-4: blocking A→C must not add reachable states");
    assert.deepEqual(delta.reachable_states_removed, ["C"], "FC-4: blocking A→C must remove only state C from reachability");
    assert.deepEqual(delta.enabled_at_initial_added, [], "FC-4: blocking A→C must not add initially enabled transitions");
    assert.deepEqual(delta.enabled_at_initial_removed, ["t_ac"], "FC-4: delta must identify t_ac as removed from initial accessibility");
    assert.equal(delta.truncated, false, "FC-4: delta must explicitly report whether either exploration was truncated");
    assert.equal(delta.baseline_truncated, false, "FC-4: baseline truncation status must be explicit");
    assert.equal(delta.intervention_truncated, false, "FC-4: intervention truncation status must be explicit");
 
    // FC-5/FC-6 grouped adversarial case: delta_reach is a closed, semantically linked artifact.
    const unknownDeltaField = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.uncontracted_extension = true;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "unknown-delta-field.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(unknownDeltaField))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /delta_reach de block_ac contiene campos ausentes o desconocidos/i,
      "FC-5: reject uncontracted delta_reach fields even when result/package hashes are recomputed");

    const forgedDeltaSemantics = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.reachable_states_removed = [];
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "forged-delta-semantics.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedDeltaSemantics))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /delta_reach de block_ac no coincide con la comparación baseline exportada/i,
      "FC-5/FC-6: reject semantically forged delta_reach despite recomputed enclosing hashes");





    // H8: jointly forge delta_reach and its exported comparison, then refresh all
    // enclosing hashes. Import must independently derive both from scenario results.
    const jointlyForgedDeltaAndComparison = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.reachable_states_removed = [];
      candidate.result.comparisons_to_baseline.block_ac.reachable_states_removed = [];
      const projected = structuredClone(candidate.result);
      delete projected.delta_reach;
      delete projected.engine_version;
      delete projected.input_sha256;
      delete projected.result_sha256;
      delete projected.semantic_sha256;
      delete projected.semantic_identity_version;
      Object.keys(projected.scenario_results || {}).forEach((id) => {
        const scenario = projected.scenario_results[id];
        if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
      });
      Object.keys(projected.comparisons_to_baseline || {}).forEach((id) => {
        const intervention = projected.comparisons_to_baseline[id].intervention || {};
        if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
      });
      candidate.result.semantic_sha256 = await window.hash(projected, "result");
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "jointly-forged-delta-and-comparison.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(jointlyForgedDeltaAndComparison))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /La comparación baseline de block_ac no coincide con la derivación independiente a partir de los resultados de escenario/i,
      "H8: reject jointly forged delta and comparison even after semantic, result, and package hashes are recomputed");

    const forgedDeltaSource = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.baseline_source_sha256 = "0".repeat(64);
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "forged-delta-source.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedDeltaSource))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /baseline_source_sha256 de delta_reach en block_ac no corresponde a la fuente/i,
      "FC-5/FC-6: reject a syntactically valid but forged source hash even when enclosing hashes are recomputed");

    // GT-02 grouped delta_reach schema adversaries: keep outer hashes valid so each case
    // exercises the specific nested invariant rather than package-integrity rejection.
    const deltaInvariantCases = await page.evaluate(async (pkg) => {
      const cases = [
        {
          name: "missing-intervention-entry",
          mutate: function (p) { delete p.result.delta_reach.block_ac; },
          expected: /delta_reach debe contener exactamente una entrada por escenario de intervención/i
        },
        {
          name: "unexpected-baseline-entry",
          mutate: function (p) { p.result.delta_reach.baseline = structuredClone(p.result.delta_reach.block_ac); },
          expected: /delta_reach debe contener exactamente una entrada por escenario de intervención/i
        },
        {
          name: "malformed-source-hash",
          mutate: function (p) { p.result.delta_reach.block_ac.baseline_source_sha256 = "not-a-sha256"; },
          expected: /baseline_source_sha256 de delta_reach en block_ac debe ser SHA-256 válido/i
        },
        {
          name: "undeclared-state-reference",
          mutate: function (p) { p.result.delta_reach.block_ac.reachable_states_removed = ["STATE_NOT_DECLARED"]; },
          expected: /reachable_states_removed de delta_reach en block_ac debe contener IDs de estado válidos/i
        },
        {
          name: "undeclared-added-state-reference",
          mutate: function (p) { p.result.delta_reach.block_ac.reachable_states_added = ["STATE_NOT_DECLARED"]; },
          expected: /reachable_states_added de delta_reach en block_ac debe contener IDs de estado válidos/i
        },
        {
          name: "added-states-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.reachable_states_added = "C"; },
          expected: /reachable_states_added de delta_reach en block_ac debe contener IDs de estado válidos/i
        },
        {
          name: "removed-states-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.reachable_states_removed = null; },
          expected: /reachable_states_removed de delta_reach en block_ac debe contener IDs de estado válidos/i
        },
        {
          name: "added-transitions-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.enabled_at_initial_added = "t_ac"; },
          expected: /enabled_at_initial_added de delta_reach en block_ac debe contener IDs de transición válidos/i
        },
        {
          name: "removed-transitions-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.enabled_at_initial_removed = null; },
          expected: /enabled_at_initial_removed de delta_reach en block_ac debe contener IDs de transición válidos/i
        },
        {
          name: "invalid-trajectory-edge",
          mutate: function (p) { p.result.delta_reach.block_ac.trajectories_removed = [[{ state: "A" }, { state: "D", transition: "t_ac" }]]; },
          expected: /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i
        },
        {
          name: "added-trajectories-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.trajectories_added = "not-an-array"; },
          expected: /trajectories_added de delta_reach en block_ac debe ser una lista/i
        },
        {
          name: "removed-trajectories-wrong-type",
          mutate: function (p) { p.result.delta_reach.block_ac.trajectories_removed = null; },
          expected: /trajectories_removed de delta_reach en block_ac debe ser una lista/i
        },
        {
          name: "added-trajectory-unknown-state",
          mutate: function (p) { p.result.delta_reach.block_ac.trajectories_added = [[{ state: "A" }, { state: "STATE_NOT_DECLARED", transition: "t_ac" }]]; },
          expected: /trajectories_added de delta_reach en block_ac debe contener trayectorias válidas/i
        },
        {
          name: "removed-trajectory-disconnected-edge",
          mutate: function (p) { p.result.delta_reach.block_ac.trajectories_removed = [[{ state: "A" }, { state: "C", transition: "t_ab" }]]; },
          expected: /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i
        },
        {
          name: "non-boolean-truncation",
          mutate: function (p) { p.result.delta_reach.block_ac.truncated = "false"; },
          expected: /truncated de delta_reach en block_ac debe ser booleano/i
        },
        {
          name: "aggregate-truncation-mismatch",
          mutate: function (p) { p.result.delta_reach.block_ac.truncated = true; },
          expected: /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i
        }
,
        {
          name: "undeclared-transition-added",
          mutate: function (p) { p.result.delta_reach.block_ac.enabled_at_initial_added = ["TRANSITION_NOT_DECLARED"]; },
          expected: /enabled_at_initial_added de delta_reach en block_ac debe contener IDs de transición válidos/i
        },
        {
          name: "undeclared-transition-removed",
          mutate: function (p) { p.result.delta_reach.block_ac.enabled_at_initial_removed = ["TRANSITION_NOT_DECLARED"]; },
          expected: /enabled_at_initial_removed de delta_reach en block_ac debe contener IDs de transición válidos/i
        },
        {
          name: "orphan-delta-without-comparison",
          mutate: function (p) { delete p.result.comparisons_to_baseline.block_ac; },
          expected: /Falta comparación baseline para block_ac/i,
          refreshSemanticIdentity: true
        }
      ];
      return Promise.all(cases.map(async (item) => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        if (item.refreshSemanticIdentity) {
          const projected = structuredClone(candidate.result);
          delete projected.delta_reach;
          delete projected.engine_version;
          delete projected.input_sha256;
          delete projected.result_sha256;
          delete projected.semantic_sha256;
          delete projected.semantic_identity_version;
          Object.keys(projected.scenario_results || {}).forEach((id) => {
            const scenario = projected.scenario_results[id];
            if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
          });
          Object.keys(projected.comparisons_to_baseline || {}).forEach((id) => {
            const intervention = projected.comparisons_to_baseline[id].intervention || {};
            if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
          });
          candidate.result.semantic_sha256 = await window.hash(projected, "result");
        }
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate, expected: item.expected.source };
      }));
    }, deltaPackage);
    const expectedDeltaDiagnostics = new Map([
      ["missing-intervention-entry", /delta_reach debe contener exactamente una entrada por escenario de intervención/i],
      ["unexpected-baseline-entry", /delta_reach debe contener exactamente una entrada por escenario de intervención/i],
      ["malformed-source-hash", /baseline_source_sha256 de delta_reach en block_ac debe ser SHA-256 válido/i],
      ["undeclared-state-reference", /reachable_states_removed de delta_reach en block_ac debe contener IDs de estado válidos/i],
      ["undeclared-added-state-reference", /reachable_states_added de delta_reach en block_ac debe contener IDs de estado válidos/i],
      ["added-states-wrong-type", /reachable_states_added de delta_reach en block_ac debe contener IDs de estado válidos/i],
      ["removed-states-wrong-type", /reachable_states_removed de delta_reach en block_ac debe contener IDs de estado válidos/i],
      ["added-transitions-wrong-type", /enabled_at_initial_added de delta_reach en block_ac debe contener IDs de transición válidos/i],
      ["removed-transitions-wrong-type", /enabled_at_initial_removed de delta_reach en block_ac debe contener IDs de transición válidos/i],
      ["invalid-trajectory-edge", /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i],
      ["added-trajectories-wrong-type", /trajectories_added de delta_reach en block_ac debe ser una lista/i],
      ["removed-trajectories-wrong-type", /trajectories_removed de delta_reach en block_ac debe ser una lista/i],
      ["added-trajectory-unknown-state", /trajectories_added de delta_reach en block_ac debe contener trayectorias válidas/i],
      ["removed-trajectory-disconnected-edge", /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i],
      ["non-boolean-truncation", /truncated de delta_reach en block_ac debe ser booleano/i],
      ["aggregate-truncation-mismatch", /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i]
,
      ["undeclared-transition-added", /enabled_at_initial_added de delta_reach en block_ac debe contener IDs de transición válidos/i],
      ["undeclared-transition-removed", /enabled_at_initial_removed de delta_reach en block_ac debe contener IDs de transición válidos/i],
      ["orphan-delta-without-comparison", /Falta comparación baseline para block_ac/i]
    ]);
    for (const deltaCase of deltaInvariantCases) {
      await page.locator("#package-file").setInputFiles({
        name: `delta-invariant-${deltaCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(deltaCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), expectedDeltaDiagnostics.get(deltaCase.name),
        `GT-02: reject ${deltaCase.name} by its nested delta_reach invariant after recomputing enclosing hashes`);
    }

    // FC-5 grouped conditional-envelope matrix: stage must match present artifacts and dependencies must hold.
    const invalidLifecycleCombinations = await page.evaluate(async (pkg) => {
      const cases = [
        { name: "assessment-with-outcome-stage", mutate: function (p) { p.package_stage = "OUTCOME"; } },
        { name: "assessment-with-exploration-stage", mutate: function (p) { p.package_stage = "EXPLORATION"; } },
        { name: "assessment-without-outcome", mutate: function (p) { delete p.outcome_record; } },
        { name: "outcome-without-trace", mutate: function (p) { delete p.concrete_execution_trace; } },
        { name: "trace-null", mutate: function (p) { p.concrete_execution_trace = null; } },
        { name: "trace-array", mutate: function (p) { p.concrete_execution_trace = []; } },
        { name: "trace-string", mutate: function (p) { p.concrete_execution_trace = "not-an-object"; } }
      ];
      return Promise.all(cases.map(async (item) => {
        const candidate = structuredClone(pkg);
        item.mutate(candidate);
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name: item.name, candidate };
      }));
    }, fc4Package);
    for (const lifecycleCase of invalidLifecycleCombinations) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-lifecycle-${lifecycleCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(lifecycleCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /package_stage|requiere|no coincide|resultado|traza|outcome|valoraci[oó]n|assessment/i,
        `FC-5: importer must reject inconsistent lifecycle combination ${lifecycleCase.name}`);
    }

    // FC-5 truth table: enumerate package_stage against every trace/outcome/assessment presence combination.
    const lifecycleTruthTable = await page.evaluate(async (pkg) => {
      const stages = ["EXPLORATION", "EXECUTION", "OUTCOME", "ASSESSMENT"];
      const rows = [];
      for (let mask = 0; mask < 8; mask++) {
        const hasTrace = Boolean(mask & 1);
        const hasOutcome = Boolean(mask & 2);
        const hasAssessment = Boolean(mask & 4);
        const expectedStage = hasAssessment ? "ASSESSMENT" : hasOutcome ? "OUTCOME" : hasTrace ? "EXECUTION" : "EXPLORATION";
        const dependenciesHold = (!hasOutcome || hasTrace) && (!hasAssessment || hasOutcome);
        for (const stage of stages) {
          const candidate = structuredClone(pkg);
          if (!hasTrace) delete candidate.concrete_execution_trace;
          if (!hasOutcome) delete candidate.outcome_record;
          if (!hasAssessment) delete candidate.value_assessment;
          candidate.package_stage = stage;
          if (hasAssessment) delete candidate.value_assessment_status;
          else candidate.value_assessment_status = "NOT_ASSESSED";
          delete candidate.package_sha256;
          candidate.package_sha256 = await window.hash(candidate, "package_export");
          const valid = dependenciesHold && stage === expectedStage;
          rows.push({ name: `stage-${stage}-trace-${hasTrace}-outcome-${hasOutcome}-assessment-${hasAssessment}`, candidate, valid });
        }
      }
      return rows;
    }, fc4Package);
    assert.equal(lifecycleTruthTable.length, 32, "FC-5 lifecycle truth table must enumerate all 4 stages x 8 artifact-presence combinations");
    assert.equal(lifecycleTruthTable.filter(row => row.valid).length, 4, "FC-5 lifecycle truth table must admit exactly the four contract-valid combinations");
    for (const lifecycleRow of lifecycleTruthTable) {
      await page.locator("#package-file").setInputFiles({
        name: `lifecycle-truth-${lifecycleRow.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(lifecycleRow.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      if (lifecycleRow.valid) {
        await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
      } else {
        await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
        assert.match(await page.locator("#package-assessment").innerText(), /package_stage|requiere|no coincide|resultado|traza|outcome|valoraci[oó]n|assessment/i,
          `FC-5: lifecycle truth-table row must reject ${lifecycleRow.name}`);
      }
    }

    // FC-5 closed-schema adversary: reject unknown fields inside outcome and assessment records.
    const unknownRecordFields = await page.evaluate(async (pkg) => {
      const outcomeExtra = structuredClone(pkg);
      outcomeExtra.outcome_record.uncontracted_field = "must-not-be-ignored";
      outcomeExtra.value_assessment.outcome_sha256 = await window.hash(outcomeExtra.outcome_record, "outcome_record");
      delete outcomeExtra.package_sha256;
      outcomeExtra.package_sha256 = await window.hash(outcomeExtra, "package_export");
      const assessmentExtra = structuredClone(pkg);
      assessmentExtra.value_assessment.uncontracted_field = "must-not-be-ignored";
      delete assessmentExtra.package_sha256;
      assessmentExtra.package_sha256 = await window.hash(assessmentExtra, "package_export");
      return [
        { name: "outcome", candidate: outcomeExtra },
        { name: "assessment", candidate: assessmentExtra }
      ];
    }, fc4Package);
    for (const recordCase of unknownRecordFields) {
      await page.locator("#package-file").setInputFiles({
        name: `unknown-record-field-${recordCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(recordCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /desconocidos|esquema|estructura|campos/i,
        `FC-5: importer must reject unknown ${recordCase.name} field`);
    }

    // FC-5 grouped outcome/assessment field contract: enums, IDs and required strings.
    const invalidOutcomeAndAssessmentFields = await page.evaluate(async (pkg) => {
      const cases = [];
      for (const item of [
        { name: "source-kind-unknown", key: "source_kind", value: "inferred" },
        { name: "source-kind-null", key: "source_kind", value: null },
        { name: "source-kind-number", key: "source_kind", value: 2 },
        { name: "unit-empty", key: "unit", value: "" },
        { name: "timing-null", key: "timing", value: null },
        { name: "uncertainty-number", key: "uncertainty_status", value: 1 },
        { name: "provenance-empty", key: "provenance", value: "   " }
      ]) {
        const candidate = structuredClone(pkg);
        candidate.outcome_record[item.key] = item.value;
        if (candidate.value_assessment) candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        cases.push({ name: item.name, candidate });
      }
      for (const item of [
        { name: "assessment-id-empty", value: "" },
        { name: "assessment-id-null", value: null },
        { name: "assessment-id-number", value: 7 }
      ]) {
        const candidate = structuredClone(pkg);
        candidate.value_assessment.assessment_id = item.value;
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        cases.push({ name: item.name, candidate });
      }
      return cases;
    }, fc4Package);
    for (const fieldCase of invalidOutcomeAndAssessmentFields) {
      await page.locator("#package-file").setInputFiles({
        name: `invalid-outcome-assessment-field-${fieldCase.name}.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(fieldCase.candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /source_kind|resultado|valoraci[oó]n|incomplet|identificador|campo|tipo|desconocido/i,
        `FC-5: importer must reject invalid outcome/assessment field ${fieldCase.name}`);
    }

    // GT-03 closure: scenario-context acceptance is retained in the prior C12 evidence.
    // Do not rerun its superseded adversarial harness here: it mutates the input/result
    // provenance without rebuilding the independent replay oracle, so it fails before
    // testing the GT-04 lifecycle contract. GT-04 tests above remain in the active suite.

    // GT-05-E2E-001: one scenario, UI-originated full chain, export and clean re-import/replay.
    const singleScenarioModel = {
      schema_version: "collective-toy-input-001",
      model_id: "gt05-single-scenario-e2e",
      initial_state: "A",
      states: ["A", "B"],
      transitions: [{ id: "t_ab", source: "A", target: "B" }],
      relations: [],
      rule_profile: { type: "finite_deterministic_graph", version: "1" },
      scenarios: [{ id: "baseline", disabled_transitions: [] }],
      exploration: { max_depth: 2, max_trajectories: 10 }
    };
    await page.locator("details").filter({ has: page.getByText("JSON avanzado (editable)") }).locator("summary").click();
    await page.locator("#model").fill(JSON.stringify(singleScenarioModel, null, 2));
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => /Ejecución completada|No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""), { timeout: 10000 });
    assert.match(await page.locator("#status").innerText(), /Ejecución completada/i, "GT-05: one-scenario exploration must execute from UI model input");
    assert.equal(await page.locator("#which option").count(), 1, "GT-05: UI must expose exactly one scenario");
    assert.equal(await page.locator("#sequence-select option").count(), 1, "GT-05: one candidate trajectory must be available");
    await page.getByRole("button", { name: "Ejecutar secuencia seleccionada" }).click();
    await page.locator("#sequence-trace[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#sequence-trace").innerText(), /Paso 1: t_ab.*A → B/i, "GT-05: concrete execution must preserve the ordered transition and state change");

    await page.locator("#outcome-value").fill("1");
    await page.locator("#outcome-unit").fill("synthetic-unit");
    await page.locator("#outcome-timing").fill("after execution");
    await page.locator("#outcome-uncertainty").fill("illustrative; not measured");
    await page.locator("#outcome-provenance").fill("GT-05 deterministic synthetic fixture");
    await page.getByRole("button", { name: "Registrar resultado" }).click();
    await page.locator("#outcome-status[data-state=" + '"recorded"' + "]").waitFor();
    await page.locator("#value-observer").fill("GT-05 test observer");
    await page.locator("#value-context").fill("synthetic test context");
    await page.locator("#value-criterion").fill("fixture criterion");
    await page.locator("#value-rule").fill("fixture rule");
    await page.locator("#value-rationale").fill("verify linkage only; no scientific interpretation");
    await page.getByRole("button", { name: "Registrar valoración contextual" }).click();
    await page.locator("#value-status[data-state=" + '"assessed"' + "]").waitFor();

    const singleScenarioDownloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const singleScenarioDownload = await singleScenarioDownloadPromise;
    const singleScenarioPackage = JSON.parse(fs.readFileSync(await singleScenarioDownload.path(), "utf8"));
    assert.equal(singleScenarioPackage.input.scenarios.length, 1, "GT-05: exported package must contain exactly one scenario");
    assert.equal(singleScenarioPackage.package_stage, "ASSESSMENT", "GT-05: full-chain package must declare ASSESSMENT stage");
    assert.equal(singleScenarioPackage.concrete_execution_trace.status, "COMPLETED", "GT-05: exported concrete trace must be completed");
    assert.deepEqual(singleScenarioPackage.concrete_execution_trace.submitted_transition_ids, ["t_ab"], "GT-05: exported trace must preserve the ordered submitted sequence");
    assert.equal(singleScenarioPackage.outcome_record.execution_id, singleScenarioPackage.concrete_execution_trace.execution_id, "GT-05: outcome must link to the concrete execution");
    assert.equal(singleScenarioPackage.outcome_record.execution_trace_sha256, singleScenarioPackage.concrete_execution_trace.trace_sha256, "GT-05: outcome must link to the exact trace digest");
    assert.equal(singleScenarioPackage.value_assessment.outcome_id, singleScenarioPackage.outcome_record.outcome_id, "GT-05: assessment must link to the exported outcome");
    assert.match(singleScenarioPackage.package_sha256, /^[a-f0-9]{64}$/i, "GT-05: exported package must carry a SHA-256 digest");

    // Clean import: feed only the downloaded package to the import control and require independent replay.
    await page.locator("#package-file").setInputFiles({
      name: "gt05-single-scenario-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(singleScenarioPackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor({ timeout: 10000 });
    assert.match(await page.locator("#package-assessment").innerText(), /reproducci[oó]n.*verificada|replay.*verified/i, "GT-05: clean import must independently verify deterministic replay");

    // GT-05 temporal success path: prerequisite and conditioned transition must occur in order
    // on the SAME concrete trajectory, then survive outcome/assessment and clean replay.
    const temporalPage = await browser.newPage();
    await temporalPage.goto("file://" + htmlPath);
    await temporalPage.getByRole("button", { name: "Cargar ejemplo" }).click();
    const temporalSuccessModel = JSON.parse(await temporalPage.locator("#model").inputValue());
    temporalSuccessModel.model_id = "gt05-temporal-success-path";
    temporalSuccessModel.initial_state = "A";
    temporalSuccessModel.states = ["A", "B", "C", "D", "X"];
    temporalSuccessModel.transitions = [
      { id: "t_ab", source: "A", target: "B" },
      { id: "t_bc", source: "B", target: "C" },
      { id: "t_cd", source: "C", target: "D" },
      { id: "t_ax", source: "A", target: "X" },
      { id: "t_xd", source: "X", target: "D" }
    ];
    temporalSuccessModel.rule_profile = { type: "temporal_prerequisite_graph", version: "1" };
    temporalSuccessModel.relations = [{
      id: "r_temporal_success",
      type: "requires_prior_execution",
      transition_id: "t_cd",
      requires_transition_id: "t_ab"
    }];
    temporalSuccessModel.scenarios = [
      { id: "baseline", disabled_transitions: [] },
      { id: "disable_alternative", disabled_transitions: ["t_ax"] }
    ];
    temporalSuccessModel.exploration = { max_depth: 5, max_trajectories: 30 };
    await temporalPage.locator("#model").evaluate((el, value) => {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, JSON.stringify(temporalSuccessModel, null, 2));
    await temporalPage.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await temporalPage.waitForFunction(() => /Ejecución completada|No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""), { timeout: 10000 });
    assert.match(await temporalPage.locator("#status").innerText(), /Ejecución completada/i,
      "GT-05 temporal: exploration must execute under temporal profile");
    const temporalResult = await temporalPage.evaluate(() => structuredClone(window.lastPackage));
    assert.ok(temporalResult.result.scenario_results.baseline.trajectories.some(path =>
      JSON.stringify(path.slice(1).map(step => step.transition)) === JSON.stringify(["t_ab", "t_bc", "t_cd"])),
      "GT-05 temporal: candidate trajectory must include prerequisite t_ab before conditioned t_cd");
    await temporalPage.locator("#sequence-input").fill("t_ab, t_bc, t_cd");
    await temporalPage.getByRole("button", { name: /Ejecutar secuencia seleccionada/i }).click();
    await temporalPage.waitForFunction(() => document.querySelector("#sequence-trace")?.dataset.state === "replay-verified" || document.querySelector("#sequence-trace")?.dataset.state === "blocked-trace-recorded" || document.querySelector("#sequence-trace")?.dataset.state === "rejected", { timeout: 5000 });
    assert.equal(await temporalPage.locator("#sequence-trace").getAttribute("data-state"), "replay-verified",
      "GT-05 temporal: valid prerequisite sequence must complete, not be blocked");
    const temporalTrace = await temporalPage.locator("#sequence-trace").evaluate(el => el._trace);
    assert.deepEqual(temporalTrace.submitted_transition_ids, ["t_ab", "t_bc", "t_cd"],
      "GT-05 temporal: completed trace must preserve prerequisite-before-conditioned order");
    assert.equal(temporalTrace.status, "COMPLETED");
    await temporalPage.locator("#outcome-value").fill("synthetic temporal path completed");
    await temporalPage.locator("#outcome-unit").fill("qualitative");
    await temporalPage.locator("#outcome-timing").fill("after temporal execution");
    await temporalPage.locator("#outcome-uncertainty").fill("synthetic; not measured");
    await temporalPage.locator("#outcome-provenance").fill("GT-05 temporal success fixture");
    await temporalPage.getByRole("button", { name: "Registrar resultado" }).click();
    await temporalPage.locator("#outcome-status[data-state=" + '"recorded"' + "]").waitFor();
    await temporalPage.locator("#value-observer").fill("GT-05 temporal observer");
    await temporalPage.locator("#value-context").fill("synthetic temporal context");
    await temporalPage.locator("#value-criterion").fill("ordered prerequisite completion");
    await temporalPage.locator("#value-rule").fill("test-only qualitative rule");
    await temporalPage.locator("#value-rationale").fill("verify lifecycle linkage only; no scientific interpretation");
    await temporalPage.getByRole("button", { name: "Registrar valoración contextual" }).click();
    await temporalPage.locator("#value-status[data-state=" + '"assessed"' + "]").waitFor();
    const temporalExportPromise = temporalPage.waitForEvent("download");
    await temporalPage.locator("#export").click();
    const temporalExport = await temporalExportPromise;
    const temporalPackage = JSON.parse(fs.readFileSync(await temporalExport.path(), "utf8"));
    assert.equal(temporalPackage.package_stage, "ASSESSMENT");
    assert.deepEqual(temporalPackage.concrete_execution_trace.submitted_transition_ids, ["t_ab", "t_bc", "t_cd"]);
    assert.equal(temporalPackage.input.rule_profile.type, "temporal_prerequisite_graph");
    assert.equal(temporalPackage.outcome_record.execution_trace_sha256, temporalPackage.concrete_execution_trace.trace_sha256);
    assert.equal(temporalPackage.value_assessment.outcome_id, temporalPackage.outcome_record.outcome_id);
    await temporalPage.locator("#package-file").setInputFiles({
      name: "gt05-temporal-success-round-trip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(temporalPackage))
    });
    await temporalPage.getByRole("button", { name: "Validar paquete importado" }).click();
    await temporalPage.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor({ timeout: 10000 });
    assert.match(await temporalPage.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-05 temporal: assessed package must independently replay after clean import");

    // Export the stronger temporal Full Chain fixture (ordered prerequisite path), not the earlier one-step fixture.
    assert.equal(temporalPackage.package_stage, "ASSESSMENT");
    assert.equal(temporalPackage.value_assessment.status, "ASSESSED");
    assert.equal(temporalPackage.outcome_record.execution_id, temporalPackage.concrete_execution_trace.execution_id);
    assert.equal(temporalPackage.outcome_record.execution_trace_sha256, temporalPackage.concrete_execution_trace.trace_sha256);
    assert.equal(temporalPackage.value_assessment.outcome_id, temporalPackage.outcome_record.outcome_id);
    const temporalPackageDigest = await temporalPage.evaluate(async (pkg) => {
      const body = structuredClone(pkg);
      delete body.package_sha256;
      return window.hash(body, "package_export");
    }, temporalPackage);
    assert.equal(temporalPackageDigest, temporalPackage.package_sha256,
      "FC-6: exported temporal Full Chain artifact must have a recomputable package digest");
    fs.mkdirSync("artifacts", { recursive: true });
    fs.writeFileSync(
      "artifacts/tgcv-full-chain-acceptance-package.json",
      `${JSON.stringify(temporalPackage, null, 2)}\n`,
      "utf8"
    );

    // H10 grouped temporal-history adversaries: keep outer hashes valid while
    // falsifying the execution prefix or the prerequisite evidence for t_cd.
    const temporalHistoryAdversaries = await temporalPage.evaluate(async (pkg) => {
      const makeCandidate = async (name, mutate) => {
        const candidate = structuredClone(pkg);
        mutate(candidate.concrete_execution_trace);
        delete candidate.concrete_execution_trace.trace_sha256;
        candidate.concrete_execution_trace.trace_sha256 = await window.hash(candidate.concrete_execution_trace, "sequence_trace");
        candidate.outcome_record.execution_trace_sha256 = candidate.concrete_execution_trace.trace_sha256;
        candidate.value_assessment.outcome_sha256 = await window.hash(candidate.outcome_record, "outcome_record");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return { name, candidate };
      };
      return [
        await makeCandidate("prior-history-skips-executed-prerequisite", trace => {
          trace.steps[2].prior_transitions = ["t_bc"];
        }),
        await makeCandidate("conditioned-step-omits-declared-prerequisite", trace => {
          trace.steps[2].prerequisites = [];
        })
      ];
    }, temporalPackage);
    const temporalHistoryExpectations = {
      "prior-history-skips-executed-prerequisite": /prior_transitions no coincide con el prefijo ejecutado/i,
      "conditioned-step-omits-declared-prerequisite": /prerequisites del paso no coincide con las relaciones temporales declaradas para el perfil activo/i
    };
    for (const temporalCase of temporalHistoryAdversaries) {
      await temporalPage.locator("#package-file").setInputFiles({
        name: `h10-temporal-history-${temporalCase.name}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(temporalCase.candidate))
      });
      await temporalPage.getByRole("button", { name: "Validar paquete importado" }).click();
      await temporalPage.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await temporalPage.locator("#package-assessment").innerText(), temporalHistoryExpectations[temporalCase.name],
        `H10: reject inconsistent temporal history despite recomputed trace and package digests: ${temporalCase.name}`);
    }

    // FC-5 grouped package-envelope adversaries: preserve a valid exploration package,
    // vary one envelope predicate at a time, and recompute package SHA where applicable.
    const explorationEnvelope = structuredClone(temporalResult);
    explorationEnvelope.package_version = "collective-toy-browser-run-002";
    explorationEnvelope.package_stage = "EXPLORATION";
    delete explorationEnvelope.concrete_execution_trace;
    delete explorationEnvelope.outcome_record;
    delete explorationEnvelope.value_assessment;
    explorationEnvelope.value_assessment_status = "NOT_ASSESSED";
    const assessEnvelopeRejection = async (candidate, expectedMessage, recalculateHash = true) => {
      const payload = structuredClone(candidate);
      if (recalculateHash) {
        delete payload.package_sha256;
        payload.package_sha256 = await temporalPage.evaluate(async value => window.hash(value), payload);
      }
      await temporalPage.locator("#package-file").setInputFiles({
        name: "fc5-envelope-adversary.json",
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(payload))
      });
      await temporalPage.getByRole("button", { name: "Validar paquete importado" }).click();
      await temporalPage.locator('#package-assessment[data-state="rejected"]').waitFor({ timeout: 10000 });
      assert.match(await temporalPage.locator("#package-assessment").innerText(), expectedMessage);
    };
    const missingPackageHash = structuredClone(explorationEnvelope);
    delete missingPackageHash.package_sha256;
    await assessEnvelopeRejection(missingPackageHash, /package_sha256 ausente o malformado/i, false);
    const malformedPackageHash = structuredClone(explorationEnvelope);
    malformedPackageHash.package_sha256 = "not-a-sha256";
    await assessEnvelopeRejection(malformedPackageHash, /package_sha256 ausente o malformado/i, false);
    const wrongTypeTrace = structuredClone(explorationEnvelope);
    wrongTypeTrace.concrete_execution_trace = "not-an-object";
    await assessEnvelopeRejection(wrongTypeTrace, /concrete_execution_trace debe ser un objeto/i);
    const wrongTypeOutcome = structuredClone(explorationEnvelope);
    wrongTypeOutcome.outcome_record = "not-an-object";
    await assessEnvelopeRejection(wrongTypeOutcome, /outcome_record debe ser un objeto/i);
    const wrongTypeAssessment = structuredClone(explorationEnvelope);
    wrongTypeAssessment.value_assessment = "not-an-object";
    await assessEnvelopeRejection(wrongTypeAssessment, /La valoración requiere un resultado explícito/i);
    const wrongTypeAssessmentStatus = structuredClone(explorationEnvelope);
    wrongTypeAssessmentStatus.value_assessment_status = ["NOT_ASSESSED"];
    await assessEnvelopeRejection(wrongTypeAssessmentStatus, /value_assessment_status=NOT_ASSESSED/i);

    // FC-5 grouped outcome/assessment contract adversaries: keep all unrelated
    // cross-links and digests internally consistent so the intended predicate fires.
    const assessLinkedPackageRejection = async (candidate, expectedMessage, recalculateAssessmentHash = true) => {
      const payload = structuredClone(candidate);
      if (recalculateAssessmentHash && payload.value_assessment && payload.outcome_record) {
        payload.value_assessment.outcome_sha256 = await temporalPage.evaluate(
          async outcome => window.hash(outcome, "outcome_record"), payload.outcome_record
        );
      }
      delete payload.package_sha256;
      payload.package_sha256 = await temporalPage.evaluate(async value => window.hash(value), payload);
      await temporalPage.locator("#package-file").setInputFiles({
        name: "fc5-linked-artifact-adversary.json",
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(payload))
      });
      await temporalPage.getByRole("button", { name: "Validar paquete importado" }).click();
      await temporalPage.locator('#package-assessment[data-state="rejected"]').waitFor({ timeout: 10000 });
      assert.match(await temporalPage.locator("#package-assessment").innerText(), expectedMessage);
    };
    const unknownOutcomeKey = structuredClone(temporalPackage);
    unknownOutcomeKey.outcome_record.unreviewed_extension = "must fail closed";
    await assessLinkedPackageRejection(unknownOutcomeKey, /El resultado contiene campos desconocidos/i);
    const wrongOutcomeValueType = structuredClone(temporalPackage);
    wrongOutcomeValueType.outcome_record.value = 17;
    await assessLinkedPackageRejection(wrongOutcomeValueType, /carece de identificador o valor/i);
    const invalidOutcomeSourceKind = structuredClone(temporalPackage);
    invalidOutcomeSourceKind.outcome_record.source_kind = "inferred";
    await assessLinkedPackageRejection(invalidOutcomeSourceKind, /source_kind del resultado no es válido/i);
    const unknownAssessmentKey = structuredClone(temporalPackage);
    unknownAssessmentKey.value_assessment.unreviewed_extension = true;
    await assessLinkedPackageRejection(unknownAssessmentKey, /La valoración contiene campos desconocidos/i);
    const blankAssessmentId = structuredClone(temporalPackage);
    blankAssessmentId.value_assessment.assessment_id = "  ";
    await assessLinkedPackageRejection(blankAssessmentId, /carece de un identificador válido/i);
    const wrongAssessmentContextType = structuredClone(temporalPackage);
    wrongAssessmentContextType.value_assessment.context = ["not", "a", "string"];
    await assessLinkedPackageRejection(wrongAssessmentContextType, /La valoración está incompleta/i);

    // FC-5 identity-link adversaries: re-hash the outer package and preserve or
    // recompute inner hashes intentionally so each test isolates one linkage rule.
    const wrongOutcomeTraceHash = structuredClone(temporalPackage);
    wrongOutcomeTraceHash.outcome_record.execution_trace_sha256 = "0".repeat(64);
    await assessLinkedPackageRejection(wrongOutcomeTraceHash, /El hash de traza del resultado no coincide/i);
    const wrongOutcomeScenario = structuredClone(temporalPackage);
    wrongOutcomeScenario.outcome_record.scenario_id = "undeclared-scenario";
    await assessLinkedPackageRejection(wrongOutcomeScenario, /scenario_id del resultado no coincide/i);
    const wrongAssessmentExecution = structuredClone(temporalPackage);
    wrongAssessmentExecution.value_assessment.execution_id = "unrelated-execution";
    await assessLinkedPackageRejection(wrongAssessmentExecution, /La valoración no está vinculada al resultado/i);
    const staleAssessmentOutcomeHash = structuredClone(temporalPackage);
    staleAssessmentOutcomeHash.value_assessment.outcome_sha256 = "0".repeat(64);
    await assessLinkedPackageRejection(staleAssessmentOutcomeHash, /El hash del resultado de valoración no coincide/i, false);
    await temporalPage.close();

    console.log("PASS: UI terminology, profile switching, relation add/remove, edit/run, fail-closed recovery, import/export, replay/tamper checks, and review/run order independence.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
