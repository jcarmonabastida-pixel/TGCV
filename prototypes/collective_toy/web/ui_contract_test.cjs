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
        source_kind: "synthetic",
        value: "must reject",
        unit: "test-unit",
        timing: "test-only",
        uncertainty_status: "synthetic-fixture",
        provenance: "adversarial test fixture"
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

    // FC-5: round-trip a fully assessed FC-4 package through the actual import UI.
    await page.locator("#package-file").setInputFiles({
      name: "assessed-fc4-roundtrip.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(fc4Package))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-05: assessed package round-trip must confirm independently replayed semantic equivalence");
    assert.equal(fc4Package.package_stage, "ASSESSMENT",
      "GT-05: assessed package must export its lifecycle stage explicitly");
    const independentlyComputedOutcomeDigest = await page.evaluate(async outcome => await hash(outcome, "gt05_test_outcome_record"), fc4Package.outcome_record);
    assert.equal(fc4Package.value_assessment.outcome_sha256, independentlyComputedOutcomeDigest,
      "GT-05: assessment digest must equal an independently recomputed canonical digest of the exact recorded outcome");
    const firstAssessedReplay = await page.locator("#package-assessment").innerText();
    await page.locator("#package-file").setInputFiles({
      name: "assessed-fc4-roundtrip-repeat.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(fc4Package))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.waitForFunction(() => document.querySelector("#package-assessment")?.dataset.state === "replay-verified" &&
      /reproducción independiente coincidente/i.test(document.querySelector("#package-assessment")?.innerText || ""), { timeout: 10000 });
    assert.equal(await page.locator("#package-assessment").innerText(), firstAssessedReplay,
      "GT-05: replaying the same assessed artifact twice must yield the same semantic replay assessment");

    // GT-04 grouped adversarial outcome/assessment schema and boundary checks.
    async function rejectGt04Mutation(name, mutation, diagnostic) {
      const forged = await page.evaluate(async ({ pkg, mutation }) => {
        const candidate = structuredClone(pkg);
        if (mutation.startsWith("missing_outcome:")) delete candidate.outcome_record[mutation.slice("missing_outcome:".length)];
        else if (mutation.startsWith("missing_assessment:")) delete candidate.value_assessment[mutation.slice("missing_assessment:".length)];
        else if (mutation === "unknown_outcome") candidate.outcome_record.uncontracted = "forged";
        else if (mutation === "invalid_source_kind") candidate.outcome_record.source_kind = "estimated";
        else if (mutation === "unknown_assessment") candidate.value_assessment.uncontracted = "forged";
        else if (mutation === "empty_assessment_id") candidate.value_assessment.assessment_id = " ";
        else if (mutation === "empty_outcome_unit") candidate.outcome_record.unit = " ";
        else if (mutation === "outcome_array") candidate.outcome_record = [];
        else if (mutation === "outcome_null") candidate.outcome_record = null;
        else if (mutation === "outcome_string") candidate.outcome_record = "not-an-outcome-object";
        else if (mutation === "outcome_number") candidate.outcome_record = 17;
        else if (mutation === "outcome_boolean") candidate.outcome_record = false;
        else if (mutation === "assessment_array") candidate.value_assessment = [];
        else if (mutation === "assessment_null") candidate.value_assessment = null;
        else if (mutation === "assessment_string") candidate.value_assessment = "not-an-assessment-object";
        else if (mutation === "assessment_number") candidate.value_assessment = 17;
        else if (mutation === "assessment_boolean") candidate.value_assessment = false;
        else if (mutation === "invalid_assessment_status") candidate.value_assessment.status = "NOT_ASSESSED";
        else if (mutation === "assessed_package_not_assessed_status") candidate.value_assessment_status = "NOT_ASSESSED";
        else if (mutation === "missing_assessment_wrong_status") { delete candidate.value_assessment; candidate.value_assessment_status = "ASSESSED"; }
        else if (mutation === "missing_assessment_missing_status") { delete candidate.value_assessment; delete candidate.value_assessment_status; candidate.package_stage = "OUTCOME"; }
        else if (mutation === "outcome_value_number") candidate.outcome_record.value = 17;
        else if (mutation === "outcome_unit_number") candidate.outcome_record.unit = 17;
        else if (mutation === "outcome_timing_null") candidate.outcome_record.timing = null;
        else if (mutation === "outcome_uncertainty_boolean") candidate.outcome_record.uncertainty_status = false;
        else if (mutation === "outcome_uncertainty_empty") candidate.outcome_record.uncertainty_status = "";
        else if (mutation === "outcome_timing_empty") candidate.outcome_record.timing = "";
        else if (mutation === "outcome_provenance_object") candidate.outcome_record.provenance = { source: "forged" };
        else if (mutation === "outcome_provenance_empty") candidate.outcome_record.provenance = " ";
        else if (mutation === "assessment_observer_number") candidate.value_assessment.observer = 17;
        else if (mutation === "assessment_observer_empty") candidate.value_assessment.observer = "";
        else if (mutation === "assessment_context_null") candidate.value_assessment.context = null;
        else if (mutation === "assessment_context_empty") candidate.value_assessment.context = " ";
        else if (mutation === "assessment_criterion_number") candidate.value_assessment.criterion = 17;
        else if (mutation === "assessment_criterion_empty") candidate.value_assessment.criterion = "";
        else if (mutation === "assessment_valuation_rule_array") candidate.value_assessment.valuation_rule = [];
        else if (mutation === "assessment_rationale_boolean") candidate.value_assessment.rationale = false;
        else if (mutation === "assessment_rationale_whitespace") candidate.value_assessment.rationale = "   ";
        else if (mutation === "assessment_rationale_empty") candidate.value_assessment.rationale = "";
        else if (mutation === "unknown_status_without_assessment") { delete candidate.value_assessment; candidate.value_assessment_status = "PENDING"; }
        else if (mutation === "wrong_outcome_schema") candidate.outcome_record.outcome_schema = "collective-toy-outcome-999";
        else if (mutation === "empty_outcome_id") candidate.outcome_record.outcome_id = " ";
        else if (mutation === "wrong_assessment_schema") candidate.value_assessment.assessment_schema = "collective-toy-value-assessment-999";
        else if (mutation === "observer_number") candidate.value_assessment.observer = 23;
        else if (mutation === "valuation_rule_empty") candidate.value_assessment.valuation_rule = " ";
        else if (mutation === "outcome_execution_mismatch") candidate.outcome_record.execution_id = "forged-execution-id";
        else if (mutation === "outcome_trace_hash_malformed") candidate.outcome_record.execution_trace_sha256 = "not-a-sha256";
        else if (mutation === "outcome_model_mismatch") candidate.outcome_record.model_id = "forged-model-id";
        else if (mutation === "outcome_scenario_mismatch") candidate.outcome_record.scenario_id = "forged-scenario-id";
        else if (mutation === "assessment_outcome_mismatch") candidate.value_assessment.outcome_id = "forged-outcome-id";
        else if (mutation === "assessment_execution_mismatch") candidate.value_assessment.execution_id = "forged-execution-id";
        else if (mutation === "assessment_outcome_hash_mismatch") candidate.value_assessment.outcome_sha256 = "0".repeat(64);
        else if (mutation === "stage_exploration_with_trace") candidate.package_stage = "EXPLORATION";
        else if (mutation === "stage_execution_with_outcome") candidate.package_stage = "EXECUTION";
        else if (mutation === "stage_outcome_with_assessment") candidate.package_stage = "OUTCOME";
        else if (mutation === "stage_assessment_without_assessment") { delete candidate.value_assessment; candidate.value_assessment_status = "NOT_ASSESSED"; candidate.package_stage = "ASSESSMENT"; }
        else if (mutation === "outcome_without_trace") { delete candidate.concrete_execution_trace; candidate.package_stage = "EXPLORATION"; }
        else if (mutation === "assessment_without_outcome") { delete candidate.outcome_record; candidate.package_stage = "ASSESSMENT"; }
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return candidate;
      }, { pkg: fc4Package, mutation });
      await page.locator("#package-file").setInputFiles({
        name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(forged))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.waitForFunction((needle) => {
        const node = document.querySelector("#package-assessment");
        return node && node.dataset.state === "rejected" && node.innerText.includes(needle);
      }, diagnostic);
    }
    await rejectGt04Mutation("gt04-unknown-outcome-key.json", "unknown_outcome", "outcome_record contiene campos desconocidos");
    await rejectGt04Mutation("gt04-invalid-outcome-source-kind.json", "invalid_source_kind", "source_kind del resultado debe ser synthetic u observed");
    await rejectGt04Mutation("gt04-empty-outcome-unit.json", "empty_outcome_unit", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-unknown-assessment-key.json", "unknown_assessment", "value_assessment contiene campos desconocidos");
    await rejectGt04Mutation("gt04-empty-assessment-id.json", "empty_assessment_id", "assessment_id válido");
    await rejectGt04Mutation("gt04-outcome-array-substitution.json", "outcome_array", "outcome_record debe ser un objeto");
    await rejectGt04Mutation("gt04-outcome-null-substitution.json", "outcome_null", "outcome_record debe ser un objeto");
    await rejectGt04Mutation("gt04-outcome-string-substitution.json", "outcome_string", "outcome_record debe ser un objeto");
    await rejectGt04Mutation("gt04-outcome-number-substitution.json", "outcome_number", "outcome_record debe ser un objeto");
    await rejectGt04Mutation("gt04-outcome-boolean-substitution.json", "outcome_boolean", "outcome_record debe ser un objeto");
    await rejectGt04Mutation("gt04-assessment-array-substitution.json", "assessment_array", "La valoración requiere un resultado explícito");
    await rejectGt04Mutation("gt04-assessment-null-substitution.json", "assessment_null", "La valoración requiere un resultado explícito");
    await rejectGt04Mutation("gt04-assessment-string-substitution.json", "assessment_string", "La valoración requiere un resultado explícito");
    await rejectGt04Mutation("gt04-assessment-number-substitution.json", "assessment_number", "La valoración requiere un resultado explícito");
    await rejectGt04Mutation("gt04-assessment-boolean-substitution.json", "assessment_boolean", "La valoración requiere un resultado explícito");
    await rejectGt04Mutation("gt04-invalid-assessment-status.json", "invalid_assessment_status", "Esquema o estado de valoración desconocido");
    await rejectGt04Mutation("gt04-assessed-package-not-assessed-status.json", "assessed_package_not_assessed_status", "Un paquete evaluado no puede declarar NOT_ASSESSED");
    await rejectGt04Mutation("gt04-missing-assessment-wrong-status.json", "missing_assessment_wrong_status", "value_assessment_status=NOT_ASSESSED");
    await rejectGt04Mutation("gt04-missing-assessment-missing-status.json", "missing_assessment_missing_status", "value_assessment_status=NOT_ASSESSED");
    await rejectGt04Mutation("gt04-outcome-value-number.json", "outcome_value_number", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-unit-number.json", "outcome_unit_number", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-timing-null.json", "outcome_timing_null", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-timing-empty.json", "outcome_timing_empty", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-uncertainty-boolean.json", "outcome_uncertainty_boolean", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-uncertainty-empty.json", "outcome_uncertainty_empty", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-provenance-object.json", "outcome_provenance_object", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-outcome-provenance-empty.json", "outcome_provenance_empty", "unidad, momento, incertidumbre/estado y procedencia como cadenas no vacías");
    await rejectGt04Mutation("gt04-assessment-observer-number.json", "assessment_observer_number", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-observer-empty.json", "assessment_observer_empty", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-context-null.json", "assessment_context_null", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-context-empty.json", "assessment_context_empty", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-criterion-number.json", "assessment_criterion_number", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-criterion-empty.json", "assessment_criterion_empty", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-valuation-rule-array.json", "assessment_valuation_rule_array", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-rationale-boolean.json", "assessment_rationale_boolean", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-rationale-whitespace.json", "assessment_rationale_whitespace", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-assessment-rationale-empty.json", "assessment_rationale_empty", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-unknown-status-without-assessment.json", "unknown_status_without_assessment", "value_assessment_status=NOT_ASSESSED");
    await rejectGt04Mutation("gt04-wrong-outcome-schema.json", "wrong_outcome_schema", "Esquema de resultado desconocido o no compatible");
    await rejectGt04Mutation("gt04-empty-outcome-id.json", "empty_outcome_id", "outcome_id válido");

    // GT-04: enumerate every required key as absent, keeping each mutation in the same
    // grouped schema contract and recomputing package_sha256 in rejectGt04Mutation.
    for (const key of [
      "outcome_schema", "outcome_id", "execution_id", "execution_trace_sha256",
      "model_id", "scenario_id", "source_kind", "value", "unit", "timing",
      "uncertainty_status", "provenance"
    ]) {
      await rejectGt04Mutation(`gt04-outcome-missing-${key}.json`, `missing_outcome:${key}`,
        "outcome_record está incompleto");
    }
    for (const key of [
      "assessment_schema", "assessment_id", "outcome_id", "execution_id",
      "outcome_sha256", "observer", "context", "criterion", "valuation_rule",
      "rationale", "status"
    ]) {
      await rejectGt04Mutation(`gt04-assessment-missing-${key}.json`, `missing_assessment:${key}`,
        "value_assessment está incompleta");
    }
    await rejectGt04Mutation("gt04-wrong-assessment-schema.json", "wrong_assessment_schema", "Esquema o estado de valoración desconocido");
    await rejectGt04Mutation("gt04-observer-number.json", "observer_number", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-empty-valuation-rule.json", "valuation_rule_empty", "La valoración está incompleta");
    await rejectGt04Mutation("gt04-outcome-execution-mismatch.json", "outcome_execution_mismatch", "El resultado no está vinculado a la traza de ejecución exportada");
    await rejectGt04Mutation("gt04-outcome-trace-hash-malformed.json", "outcome_trace_hash_malformed", "El hash de traza del resultado no coincide con la traza exportada");
    await rejectGt04Mutation("gt04-outcome-model-mismatch.json", "outcome_model_mismatch", "El model_id del resultado no coincide con la entrada y la traza exportadas");
    await rejectGt04Mutation("gt04-outcome-scenario-mismatch.json", "outcome_scenario_mismatch", "El scenario_id del resultado no coincide con la traza exportada");
    await rejectGt04Mutation("gt04-assessment-outcome-mismatch.json", "assessment_outcome_mismatch", "La valoración no está vinculada al resultado y ejecución exportados");
    await rejectGt04Mutation("gt04-assessment-execution-mismatch.json", "assessment_execution_mismatch", "La valoración no está vinculada al resultado y ejecución exportados");
    await rejectGt04Mutation("gt04-assessment-outcome-hash-mismatch.json", "assessment_outcome_hash_mismatch", "El hash del resultado de valoración no coincide con outcome_record");
    await rejectGt04Mutation("gt04-stage-exploration-with-trace.json", "stage_exploration_with_trace", "package_stage no coincide con los artefactos presentes");
    await rejectGt04Mutation("gt04-stage-execution-with-outcome.json", "stage_execution_with_outcome", "package_stage no coincide con los artefactos presentes");
    await rejectGt04Mutation("gt04-stage-outcome-with-assessment.json", "stage_outcome_with_assessment", "package_stage no coincide con los artefactos presentes");
    await rejectGt04Mutation("gt04-stage-assessment-without-assessment.json", "stage_assessment_without_assessment", "package_stage no coincide con los artefactos presentes");
    await rejectGt04Mutation("gt04-outcome-without-trace.json", "outcome_without_trace", "outcome_record requiere concrete_execution_trace");
    await rejectGt04Mutation("gt04-assessment-without-outcome.json", "assessment_without_outcome", "package_stage no coincide con los artefactos presentes");

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
    assert.equal(unassessedOutcomePackage.package_stage, "OUTCOME",
      "GT-04: explicit outcome without valuation must use OUTCOME stage");
    assert.ok(unassessedOutcomePackage.concrete_execution_trace && unassessedOutcomePackage.outcome_record,
      "GT-04: OUTCOME row must preserve trace and outcome artifacts");
    assert.equal(unassessedOutcomePackage.value_assessment, undefined,
      "GT-04: OUTCOME row must omit value_assessment");

    // GT-04 lifecycle positive row: concrete execution trace without outcome or assessment.
    const executionOnlyPackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.outcome_record;
      delete candidate.value_assessment;
      candidate.value_assessment_status = "NOT_ASSESSED";
      candidate.package_stage = "EXECUTION";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    assert.ok(executionOnlyPackage.concrete_execution_trace,
      "GT-04: EXECUTION row must include a concrete trace");
    assert.equal(executionOnlyPackage.outcome_record, undefined);
    assert.equal(executionOnlyPackage.value_assessment, undefined);
    assert.equal(executionOnlyPackage.value_assessment_status, "NOT_ASSESSED");
    await page.locator("#package-file").setInputFiles({
      name: "execution-not-assessed-roundtrip.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(executionOnlyPackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-04: EXECUTION lifecycle row must import and replay successfully");

    // GT-04 lifecycle positive row: exploration without trace, outcome, or assessment.
    const explorationPackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.concrete_execution_trace;
      delete candidate.outcome_record;
      delete candidate.value_assessment;
      candidate.value_assessment_status = "NOT_ASSESSED";
      candidate.package_stage = "EXPLORATION";
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, fc4Package);
    assert.equal(explorationPackage.concrete_execution_trace, undefined);
    assert.equal(explorationPackage.outcome_record, undefined);
    assert.equal(explorationPackage.value_assessment, undefined);
    assert.equal(explorationPackage.value_assessment_status, "NOT_ASSESSED");
    await page.locator("#package-file").setInputFiles({
      name: "exploration-not-assessed-roundtrip.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(explorationPackage))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i,
      "GT-04: EXPLORATION lifecycle row must import and replay successfully");

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
    assert.match(await page.locator("#package-assessment").innerText(), /(?:value_assessment|valoración) está incompleta/i,
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

    // FC5-PKG-005: reject an absent package digest.
    const missingPackageDigest = await page.evaluate((pkg) => {
      const candidate = structuredClone(pkg);
      delete candidate.package_sha256;
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "missing-package-sha256.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(missingPackageDigest))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /package_sha256 ausente o malformado/i,
      "FC5-PKG-005: importer must reject a missing package digest");

    // FC5-PKG-006: reject a malformed package digest, independently of digest mismatch.
    const malformedPackageDigest = await page.evaluate((pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_sha256 = "not-a-sha256";
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "malformed-package-sha256.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(malformedPackageDigest))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /package_sha256 ausente o malformado/i,
      "FC5-PKG-006: importer must reject a malformed package digest");

    // FC5-PKG-007: a well-formed but incorrect digest must fail package integrity.
    // Deliberately do not recompute package_sha256: that is the condition under test.
    const incorrectPackageDigest = await page.evaluate((pkg) => {
      const candidate = structuredClone(pkg);
      candidate.package_sha256 = "0".repeat(64);
      return candidate;
    }, fc4Package);
    await page.locator("#package-file").setInputFiles({
      name: "incorrect-package-sha256.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(incorrectPackageDigest))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /El hash del paquete no coincide/i,
      "FC5-PKG-007: importer must reject a well-formed but incorrect package digest");

    // FC5-PKG-008: reject non-object concrete_execution_trace values with valid enclosing package digests.
    // Recompute package_sha256 in every case to isolate the trace type contract from package integrity.
    for (const [caseName, invalidTrace] of [
      ["null", null],
      ["array", []],
      ["string", "not-a-trace-object"],
      ["number", 7],
      ["boolean", false]
    ]) {
      const invalidTracePackage = await page.evaluate(async ({ pkg, invalidTrace }) => {
        const candidate = structuredClone(pkg);
        candidate.concrete_execution_trace = invalidTrace;
        // Use an exploration-stage package without an outcome: the outcome-link
        // invariant otherwise rejects first and masks the trace type diagnostic.
        delete candidate.outcome_record;
        delete candidate.value_assessment;
        candidate.value_assessment_status = "NOT_ASSESSED";
        candidate.package_stage = "EXPLORATION";
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return candidate;
      }, { pkg: fc4Package, invalidTrace });
      await page.locator("#package-file").setInputFiles({
        name: `invalid-trace-type-${caseName}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(invalidTracePackage))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), /concrete_execution_trace debe ser un objeto/i,
        `FC5-PKG-008: importer must reject concrete_execution_trace type ${caseName} independently of package digest integrity`);
    }

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
    assert.match(await page.locator("#package-assessment").innerText(), /El motivo del bloqueo no coincide con el (?:contexto del escenario de la traza, el estado y los prerrequisitos|estado, escenario y prerrequisitos de la traza)/i,
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
    // C12: duplicate raw JSON keys must be rejected before JSON.parse collapses them.
    const duplicateKeyJson = JSON.stringify(deltaPackage).replace(
      '"package_version":',
      '"package_version":"collective-toy-browser-run-002","package_version":'
    );
    assert.notEqual(duplicateKeyJson, JSON.stringify(deltaPackage),
      "C12 duplicate-key fixture must contain an injected duplicate key");
    await page.locator("#package-file").setInputFiles({
      name: "duplicate-package-key.json", mimeType: "application/json",
      buffer: Buffer.from(duplicateKeyJson)
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /clave de objeto duplicada: package_version/i,
      "FC-5 C12: detect duplicate raw JSON keys before object parsing");
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

    // FC-5 grouped adversaries: delta_reach must contain exactly the declared intervention IDs.
    for (const item of [
      { name: "delta-reach-missing-intervention-entry.json", mutate: (copy) => { delete copy.result.delta_reach.block_ac; },
        diagnostic: /delta_reach debe contener exactamente una entrada por escenario de intervención/i },
      { name: "delta-reach-extra-baseline-entry.json", mutate: (copy) => { copy.result.delta_reach.baseline = structuredClone(copy.result.delta_reach.block_ac); },
        diagnostic: /delta_reach debe contener exactamente una entrada por escenario de intervención/i }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, mutation }) => {
        const copy = structuredClone(pkg);
        if (mutation === "missing") delete copy.result.delta_reach.block_ac;
        else copy.result.delta_reach.baseline = structuredClone(copy.result.delta_reach.block_ac);
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, mutation: item.name.includes("missing") ? "missing" : "extra" });
      await page.locator("#package-file").setInputFiles({
        name: item.name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), item.diagnostic,
        "FC-5: reject missing intervention delta or extra baseline delta entry");
    }

    // C12: comparison entries must match the intervention scenario set too.
    for (const item of [
      { name: "comparison-missing-intervention.json", kind: "missing",
        diagnostic: /Falta comparación baseline para block_ac/i },
      { name: "comparison-extra-baseline.json", kind: "extra",
        diagnostic: /comparisons_to_baseline contiene una clave de escenario no compatible/i }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, kind }) => {
        const copy = structuredClone(pkg);
        if (kind === "missing") delete copy.result.comparisons_to_baseline.block_ac;
        else copy.result.comparisons_to_baseline.baseline = structuredClone(copy.result.comparisons_to_baseline.block_ac);
        const semanticProjection = structuredClone(copy.result);
        for (const key of ["delta_reach", "engine_version", "input_sha256", "result_sha256", "semantic_sha256", "semantic_identity_version"]) delete semanticProjection[key];
        for (const scenario of Object.values(semanticProjection.scenario_results || {})) if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
        for (const comparison of Object.values(semanticProjection.comparisons_to_baseline || {})) {
          const intervention = comparison.intervention || {};
          if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
        }
        copy.result.semantic_sha256 = await window.hash(semanticProjection, "result");
        delete copy.result.result_sha256;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, kind: item.kind });
      await page.locator("#package-file").setInputFiles({
        name: item.name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), item.diagnostic,
        "FC-5 C12: reject missing/extra comparison scenario entry after recomputing enclosing hashes");
    }

    // C12: each scenario_results payload must retain the scenario identity encoded by its map key.
    for (const scenarioId of Object.keys(deltaPackage.result.scenario_results).sort()) {
      const candidate = await page.evaluate(async ({ pkg, scenarioId }) => {
        const copy = structuredClone(pkg);
        copy.result.scenario_results[scenarioId].scenario_id = scenarioId + "__mismatched";
        const semanticProjection = structuredClone(copy.result);
        for (const key of ["delta_reach", "engine_version", "input_sha256", "result_sha256", "semantic_sha256", "semantic_identity_version"]) delete semanticProjection[key];
        for (const scenario of Object.values(semanticProjection.scenario_results || {})) if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
        for (const comparison of Object.values(semanticProjection.comparisons_to_baseline || {})) {
          const intervention = comparison.intervention || {};
          if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
        }
        copy.result.semantic_sha256 = await window.hash(semanticProjection, "result");
        delete copy.result.result_sha256;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, scenarioId });
      await page.locator("#package-file").setInputFiles({
        name: "scenario-results-" + scenarioId + "-identity-mismatch.json",
        mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(),
        new RegExp("scenario_id no coincide con la clave " + scenarioId, "i"),
        "FC-5 C12: reject scenario_results identity mismatch for " + scenarioId);
    }

    // C12: each delta source commitment must identify the matching baseline/intervention source for every intervention scenario.
    for (const scenarioId of Object.keys(deltaPackage.result.delta_reach).sort()) {
      for (const item of [
        { field: "baseline_source_sha256",
          diagnostic: new RegExp("baseline_source_sha256 de delta_reach en " + scenarioId + " no corresponde a la fuente del escenario baseline", "i") },
        { field: "intervention_source_sha256",
          diagnostic: new RegExp("intervention_source_sha256 de delta_reach en " + scenarioId + " no corresponde a la fuente del escenario de intervención", "i") }
      ]) {
        const candidate = await page.evaluate(async ({ pkg, field, scenarioId }) => {
          const copy = structuredClone(pkg);
          copy.result.delta_reach[scenarioId][field] = "0".repeat(64);
          const resultBody = structuredClone(copy.result);
          delete resultBody.input_sha256;
          delete resultBody.result_sha256;
          copy.result.result_sha256 = await window.hash(resultBody, "result");
          delete copy.package_sha256;
          copy.package_sha256 = await window.hash(copy, "package_export");
          return copy;
        }, { pkg: deltaPackage, field: item.field, scenarioId });
        await page.locator("#package-file").setInputFiles({
          name: "delta-" + scenarioId + "-" + item.field + "-source-mismatch.json",
          mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
        });
        await page.getByRole("button", { name: "Validar paquete importado" }).click();
        await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
        assert.match(await page.locator("#package-assessment").innerText(), item.diagnostic,
          "FC-5 C12: reject incorrect " + item.field + " source commitment for scenario " + scenarioId);
      }
    }

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





    // FC-5/FC-6: isolate validly typed removed-state and removed-transition
    // mismatches. Recompute enclosing digests so each case reaches C10 semantics.
    for (const item of [
      { field: "reachable_states_removed", value: [], name: "removed-states" },
      { field: "enabled_at_initial_removed", value: [], name: "removed-initial-transitions" }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, field, value }) => {
        const copy = structuredClone(pkg);
        copy.result.delta_reach.block_ac[field] = value;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, field: item.field, value: item.value });
      await page.locator("#package-file").setInputFiles({
        name: `delta-${item.name}-comparison-mismatch.json`,
        mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(),
        /delta_reach de block_ac no coincide con la comparación baseline exportada/i,
        `FC-5/FC-6 C10: reject validly typed ${item.field} mismatch after digest recomputation`);
    }

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

    const malformedInterventionSource = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.intervention_source_sha256 = "not-a-sha256";
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "malformed-intervention-source-hash.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(malformedInterventionSource))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /intervention_source_sha256 de delta_reach en block_ac debe ser SHA-256 válido/i,
      "FC-5: reject malformed intervention-source digest before checking source correspondence");

    const forgedInterventionSource = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.intervention_source_sha256 = "0".repeat(64);
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "forged-intervention-source-hash.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedInterventionSource))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /intervention_source_sha256 de delta_reach en block_ac no corresponde a la fuente/i,
      "FC-5/FC-6: reject a well-formed but forged intervention-source digest with enclosing hashes recomputed");

    // FC-5 grouped adversarial cases: delta_reach truncation fields must be typed and consistent.
    const wrongTruncationType = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.baseline_truncated = "false";
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "delta-baseline-truncated-wrong-type.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(wrongTruncationType))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /baseline_truncated de delta_reach en block_ac debe ser booleano/i,
      "FC-5: reject non-boolean baseline truncation flag");

    // Complete boolean type coverage: aggregate and intervention flags must also be actual booleans.
    for (const field of ["truncated", "intervention_truncated"]) {
      const wrongType = await page.evaluate(async (args) => {
        const candidate = structuredClone(args.pkg);
        candidate.result.delta_reach.block_ac[args.field] = "false";
        const resultBody = structuredClone(candidate.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        candidate.result.result_sha256 = await window.hash(resultBody, "result");
        delete candidate.package_sha256;
        candidate.package_sha256 = await window.hash(candidate, "package_export");
        return candidate;
      }, { pkg: deltaPackage, field });
      await page.locator("#package-file").setInputFiles({
        name: `delta-${field}-wrong-type.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(wrongType))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(),
        new RegExp(field + " de delta_reach en block_ac debe ser booleano", "i"),
        `FC-5: reject non-boolean ${field}`);
    }

    // Baseline-specific consistency: a forged baseline flag must not be masked by a valid aggregate OR.
    const inconsistentBaselineTruncation = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.baseline_truncated = true;
      candidate.result.delta_reach.block_ac.truncated = true;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "delta-baseline-truncation-inconsistent.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(inconsistentBaselineTruncation))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i,
      "FC-5: reject baseline truncation flag that disagrees with the baseline scenario");

    const inconsistentAggregateTruncation = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.truncated = true;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "delta-aggregate-truncation-inconsistent.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(inconsistentAggregateTruncation))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i,
      "FC-5: reject aggregate truncation flag inconsistent with baseline/intervention flags");

    const inconsistentInterventionTruncation = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.delta_reach.block_ac.intervention_truncated = true;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "delta-intervention-truncation-inconsistent.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(inconsistentInterventionTruncation))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i,
      "FC-5: reject intervention truncation flag that disagrees with the intervention scenario");

    // Exhaust all 8 claimed boolean triples against the scenario flags in this fixture.
    // Exactly the tuple matching both scenario results and their OR aggregate may be accepted.
    const truncationTruthTable = await page.evaluate((pkg) => {
      const delta = pkg.result.delta_reach.block_ac;
      const baseline = pkg.result.scenario_results.baseline.truncated;
      const intervention = pkg.result.scenario_results.block_ac.truncated;
      return { baseline, intervention, expectedAggregate: baseline || intervention };
    }, deltaPackage);
    for (let mask = 0; mask < 8; mask++) {
      const claimed = {
        baseline_truncated: Boolean(mask & 1),
        intervention_truncated: Boolean(mask & 2),
        truncated: Boolean(mask & 4)
      };
      const expectedAccepted =
        claimed.baseline_truncated === truncationTruthTable.baseline &&
        claimed.intervention_truncated === truncationTruthTable.intervention &&
        claimed.truncated === (claimed.baseline_truncated || claimed.intervention_truncated);
      // Preserve the original, known-valid export for the sole expected-accepted tuple.
      // Rehash only adversarial tuples; this keeps the positive control independent of mutation code.
      const candidate = await page.evaluate(async (args) => {
        const copy = structuredClone(args.pkg);
        if (!args.expectedAccepted) {
          Object.assign(copy.result.delta_reach.block_ac, args.claimed);
        } else {
          // The positive control must be self-consistent across the exported input and trace.
          const inputHash = await window.hash(copy.input, "input");
          copy.result.input_sha256 = inputHash;
          if (copy.concrete_execution_trace) {
            copy.concrete_execution_trace.input_sha256 = inputHash;
            const traceBody = structuredClone(copy.concrete_execution_trace);
            delete traceBody.trace_sha256;
            copy.concrete_execution_trace.trace_sha256 = await window.hash(traceBody, "sequence_trace");
            if (copy.outcome_record) {
              copy.outcome_record.execution_trace_sha256 = copy.concrete_execution_trace.trace_sha256;
              copy.outcome_record = structuredClone(copy.outcome_record);
              // If an assessment is present, refresh its digest over the updated outcome.
              if (copy.value_assessment) {
                copy.value_assessment.outcome_sha256 = await window.hash(copy.outcome_record, "outcome_record");
              }
            }
          }
        }
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, claimed, expectedAccepted });
      await page.locator("#package-file").setInputFiles({
        name: `delta-truncation-truth-table-${mask}.json`, mimeType: "application/json",
        buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state]").waitFor();
      // Valid imported packages use the UI's documented replay-verified state,
      // not a generic "accepted" state.
      const expectedState = expectedAccepted ? "replay-verified" : "rejected";
      try {
        await page.locator(`#package-assessment[data-state='${expectedState}']`).waitFor({ timeout: 5000 });
      } catch (error) {
        const diagnostic = await page.locator("#package-assessment").innerText();
        throw new Error(`FC-5 truth-table tuple ${mask}: expected ${expectedState}; actual assessment: ${diagnostic}`);
      }
      if (!expectedAccepted) {
        assert.match(await page.locator("#package-assessment").innerText(),
          /Los indicadores de truncamiento de delta_reach en block_ac no coinciden con los escenarios/i,
          `FC-5: truth-table tuple ${mask} rejected for scenario/aggregate inconsistency`);
      }
    }

    // FC-5 grouped adversarial cases: delta state/transition arrays must contain declared IDs.
    for (const item of [
      { name: "delta-reachable-states-added-wrong-type.json", field: "reachable_states_added", value: "C", diagnostic: /reachable_states_added de delta_reach en block_ac debe contener IDs de estado válidos/i },
      { name: "delta-reachable-states-removed-unknown-id.json", field: "reachable_states_removed", value: ["UNKNOWN_STATE"], diagnostic: /reachable_states_removed de delta_reach en block_ac debe contener IDs de estado válidos/i },
      { name: "delta-enabled-transitions-added-wrong-type.json", field: "enabled_at_initial_added", value: "t_ac", diagnostic: /enabled_at_initial_added de delta_reach en block_ac debe contener IDs de transición válidos/i },
      { name: "delta-enabled-transitions-removed-unknown-id.json", field: "enabled_at_initial_removed", value: ["unknown_transition"], diagnostic: /enabled_at_initial_removed de delta_reach en block_ac debe contener IDs de transición válidos/i }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, field, value }) => {
        const copy = structuredClone(pkg);
        copy.result.delta_reach.block_ac[field] = value;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, field: item.field, value: item.value });
      await page.locator("#package-file").setInputFiles({
        name: item.name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), item.diagnostic,
        "FC-5: reject malformed or unknown IDs in delta_reach field " + item.field);
    }

    // FC-5 grouped adversarial cases: delta trajectories must be ordered valid paths.
    for (const item of [
      { name: "delta-trajectories-added-wrong-type.json", field: "trajectories_added", value: "A->C", diagnostic: /trajectories_added de delta_reach en block_ac debe ser una lista/i },
      { name: "delta-trajectories-removed-unknown-state.json", field: "trajectories_removed", value: [[{ state: "A" }, { state: "UNKNOWN_STATE", transition: "t_ac" }]], diagnostic: /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i },
      { name: "delta-trajectories-removed-invalid-edge.json", field: "trajectories_removed", value: [[{ state: "A" }, { state: "C", transition: "t_bd" }]], diagnostic: /trajectories_removed de delta_reach en block_ac debe contener trayectorias válidas/i }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, field, value }) => {
        const copy = structuredClone(pkg);
        copy.result.delta_reach.block_ac[field] = value;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, field: item.field, value: item.value });
      await page.locator("#package-file").setInputFiles({
        name: item.name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(), item.diagnostic,
        "FC-5: reject malformed or non-applicable ordered path in delta_reach field " + item.field);
    }

    // FC-5 grouped adversarial cases: well-formed delta IDs/paths must still match baseline comparisons exactly.
    for (const item of [
      { name: "delta-valid-state-id-comparison-mismatch.json", field: "reachable_states_added", value: ["C"] },
      { name: "delta-valid-transition-id-comparison-mismatch.json", field: "enabled_at_initial_added", value: ["t_ac"] },
      { name: "delta-valid-trajectory-comparison-mismatch.json", field: "trajectories_added", value: [[{ state: "A" }, { state: "B", transition: "t_ab" }]] },
      { name: "delta-valid-removed-trajectory-comparison-mismatch.json", field: "trajectories_removed", value: [] }
    ]) {
      const candidate = await page.evaluate(async ({ pkg, field, value }) => {
        const copy = structuredClone(pkg);
        copy.result.delta_reach.block_ac[field] = value;
        const resultBody = structuredClone(copy.result);
        delete resultBody.input_sha256;
        delete resultBody.result_sha256;
        copy.result.result_sha256 = await window.hash(resultBody, "result");
        delete copy.package_sha256;
        copy.package_sha256 = await window.hash(copy, "package_export");
        return copy;
      }, { pkg: deltaPackage, field: item.field, value: item.value });
      await page.locator("#package-file").setInputFiles({
        name: item.name, mimeType: "application/json", buffer: Buffer.from(JSON.stringify(candidate))
      });
      await page.getByRole("button", { name: "Validar paquete importado" }).click();
      await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
      assert.match(await page.locator("#package-assessment").innerText(),
        /delta_reach de block_ac no coincide con la comparación baseline exportada/i,
        "FC-5: reject structurally valid delta field that differs from baseline comparison: " + item.field);
    }

    // C12: comparison intervention identity must match the declared input scenario.
    const forgedComparisonIntervention = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.comparisons_to_baseline.block_ac.intervention.disabled_transitions = [];
      const semanticProjection = structuredClone(candidate.result);
      for (const key of ["delta_reach","engine_version","input_sha256","result_sha256","semantic_sha256","semantic_identity_version"]) delete semanticProjection[key];
      for (const scenario of Object.values(semanticProjection.scenario_results || {})) if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
      for (const comparison of Object.values(semanticProjection.comparisons_to_baseline || {})) {
        const intervention = comparison.intervention || {};
        if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
      }
      candidate.result.semantic_sha256 = await window.hash(semanticProjection, "result");
      delete candidate.result.result_sha256;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, deltaPackage);
    await page.locator("#package-file").setInputFiles({
      name: "comparison-intervention-source-mismatch.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedComparisonIntervention))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(),
      /intervention\.disabled_transitions de la comparación block_ac no coincide con el escenario de entrada/i,
      "FC-5 C12: reject comparison intervention payload inconsistent with its input scenario");

    // GT-03 scenario-context adversary: the blocked reason must use trace.scenario_id, not baseline.
    const forgedBlockedScenarioContext = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (trace.status !== "BLOCKED" || trace.blocked_step.reason !== "temporal_prerequisite_not_satisfied") throw new Error("Fixture must be a BLOCKED trace due to an unmet temporal prerequisite");
      const baseline = candidate.input.scenarios.find(s => s.id === "baseline");
      const alternate = candidate.input.scenarios.find(s => s.id === "block_ac");
      if (!baseline || !alternate) throw new Error("Fixture needs baseline and block_ac scenarios");
      // Invert the context deliberately: baseline permits the transition, while the trace's
      // declared alternate scenario disables it. A validator that incorrectly consults baseline
      // would accept the stale temporal-prerequisite reason; the correct validator must reject it.
      baseline.disabled_transitions = (baseline.disabled_transitions || []).filter(id => id !== trace.blocked_step.transition_id);
      alternate.disabled_transitions = [...new Set([...(alternate.disabled_transitions || []), trace.blocked_step.transition_id])].sort();
      // Keep the comparison source identity aligned so this adversary isolates the BLOCKED-reason rule.
      candidate.result.comparisons_to_baseline.block_ac.intervention.disabled_transitions = [...alternate.disabled_transitions].sort();
      // Keep delta_reach source commitments coherent with the adversarially edited scenarios,
      // so validation reaches the intended BLOCKED-reason diagnostic.
      const sourceCommon = {
        schema_version: candidate.input.schema_version,
        model_id: candidate.input.model_id,
        initial_state: candidate.input.initial_state,
        states: candidate.input.states,
        transitions: candidate.input.transitions,
        relations: candidate.input.relations || [],
        rule_profile: candidate.input.rule_profile,
        exploration: candidate.input.exploration || {}
      };
      const baselineSource = candidate.input.scenarios.find(s => s.id === "baseline");
      for (const id of Object.keys(candidate.result.delta_reach || {})) {
        const interventionSource = candidate.input.scenarios.find(s => s.id === id);
        if (!interventionSource) throw new Error("Missing delta_reach intervention scenario: " + id);
        candidate.result.delta_reach[id].baseline_source_sha256 =
          await window.hash({...sourceCommon, scenario: baselineSource}, "delta_reach_baseline_source");
        candidate.result.delta_reach[id].intervention_source_sha256 =
          await window.hash({...sourceCommon, scenario: interventionSource}, "delta_reach_intervention_source");
      }
      trace.scenario_id = alternate.id;
      trace.input_sha256 = await window.hash(candidate.input, "input");
      candidate.result.input_sha256 = trace.input_sha256;
      // Recompute result semantic and integrity commitments after scenario-source edits.
      const semanticProjection = structuredClone(candidate.result);
      for (const key of ["delta_reach","engine_version","input_sha256","result_sha256","semantic_sha256","semantic_identity_version"]) delete semanticProjection[key];
      for (const scenario of Object.values(semanticProjection.scenario_results || {})) if (Array.isArray(scenario.disabled_transitions)) scenario.disabled_transitions.sort();
      for (const comparison of Object.values(semanticProjection.comparisons_to_baseline || {})) {
        const intervention = comparison.intervention || {};
        if (Array.isArray(intervention.disabled_transitions)) intervention.disabled_transitions.sort();
      }
      candidate.result.semantic_sha256 = await window.hash(semanticProjection, "result");
      delete candidate.result.result_sha256;
      const resultBody = structuredClone(candidate.result);
      delete resultBody.input_sha256;
      delete resultBody.result_sha256;
      candidate.result.result_sha256 = await window.hash(resultBody, "result");
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({name:"blocked-trace-wrong-baseline-context.json",mimeType:"application/json",buffer:Buffer.from(JSON.stringify(forgedBlockedScenarioContext))});
    await page.getByRole("button", {name:"Validar paquete importado"}).click();
    await page.locator("#package-assessment[data-state=" + '"rejected"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /contexto del escenario de la traza/i,
      "GT-03: blocked reason must be validated against trace.scenario_id, not baseline, with recomputed trace/package digests");

    console.log("PASS: UI terminology, profile switching, relation add/remove, edit/run, fail-closed recovery, import/export, replay/tamper checks, and review/run order independence.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
