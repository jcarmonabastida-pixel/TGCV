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
    assert.deepEqual(exportedPackage, packageData, "Downloaded JSON must match the inspectable browser package");

    // Exercise the actual import UI with the package produced by the export button.
    await page.locator("#package-file").setInputFiles({
      name: download.suggestedFilename(),
      mimeType: "application/json",
      buffer: Buffer.from(exportedText)
    });
    await page.getByRole("button", { name: "Validar paquete importado" }).click();
    await page.locator("#package-assessment[data-state=" + '"replay-verified"' + "]").waitFor();
    assert.match(await page.locator("#package-assessment").innerText(), /reproducción independiente coincidente/i);

    // A structurally valid, self-consistent package from an unknown engine is inspect-only.
    const unknownEnginePackage = await page.evaluate(async (pkg) => {
      const candidate = structuredClone(pkg);
      candidate.result.engine_version = "collective-toy-engine-future-999";
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

    // FC-4 contract-first: baseline/intervention reachability delta must be explicit and auditable.
    await page.getByRole("button", { name: "Cargar ejemplo" }).click();
    await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
    await page.waitForFunction(() => /Ejecución completada|No se ha podido ejecutar/.test(document.querySelector("#status")?.innerText || ""), { timeout: 10000 });
    assert.match(await page.locator("#status").innerText(), /Ejecución completada/i,
      "FC-4: baseline/intervention fixture must execute before delta assertions");
    const accessTrace = page.locator("#results [data-accessibility-transition]");
    assert.ok(await accessTrace.count() >= 8, "FC-2: each transition in each scenario must expose an accessibility trace row");
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





    console.log("PASS: UI terminology, profile switching, relation add/remove, edit/run, fail-closed recovery, import/export, replay/tamper checks, and review/run order independence.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
