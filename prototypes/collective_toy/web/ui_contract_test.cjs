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
    assert.match(await page.locator("#package-assessment").innerText(), /El motivo del bloqueo no coincide con el estado, escenario y prerrequisitos de la traza/i,
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

    // GT-03 scenario-context adversary: the blocked reason must use trace.scenario_id, not baseline.
    const forgedBlockedScenarioContext = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      const trace = candidate.concrete_execution_trace;
      if (trace.status !== "BLOCKED" || trace.blocked_step.reason !== "temporal_prerequisite_not_satisfied") {
        throw new Error("Fixture must be a BLOCKED trace due to an unmet temporal prerequisite");
      }
      const baseline = candidate.input.scenarios.find(s => s.id === "baseline");
      const alternate = candidate.input.scenarios.find(s => s.id === "block_ac");
      if (!baseline || !alternate) throw new Error("Fixture needs baseline and block_ac scenarios");
      baseline.disabled_transitions = [...new Set([...(baseline.disabled_transitions || []), trace.blocked_step.transition_id])].sort();
      alternate.disabled_transitions = (alternate.disabled_transitions || []).filter(id => id !== trace.blocked_step.transition_id);
      trace.scenario_id = alternate.id;
      trace.input_sha256 = await window.hash(candidate.input);
      candidate.result.input_sha256 = trace.input_sha256;
      delete trace.trace_sha256;
      trace.trace_sha256 = await window.hash(trace, "sequence_trace");
      delete candidate.package_sha256;
      candidate.package_sha256 = await window.hash(candidate, "package_export");
      return candidate;
    }, blockedPackage);
    await page.locator("#package-file").setInputFiles({
      name: "blocked-trace-wrong-baseline-context.json", mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(forgedBlockedScenarioContext))
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
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
