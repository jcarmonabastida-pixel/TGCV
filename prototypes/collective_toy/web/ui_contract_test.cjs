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
    page.on("pageerror", error => console.error("[ui-contract pageerror]", error.stack || error.message));
    page.on("console", message => { if (message.type() === "error") console.error("[ui-contract console]", message.text()); });
    await page.goto("file://" + htmlPath);

    // Keep the MVP's state-local graph semantics and non-scientific boundary visible.
    const notice = await page.locator(".notice").innerText();
    assert.match(notice, /grafo finito/i);
    assert.match(notice, /No procesa datos reales/i);
    assert.match(notice, /No es una validación científica/i);
    assert.match(notice, /ni implementa por sí solo Tacc de TGCV/i);

    // OCR image upload accepts supported formats, rejects unsupported/oversized files, and keeps OCR failures recoverable.
    const imageInput = page.locator("#image-file");
    await imageInput.setInputFiles({ name: "reference.png", mimeType: "image/png", buffer: Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR4nGP8//8/AwMDEwMDAwMDAwAkBgMB/DXemwAAAABJRU5ErkJggg==", "base64") });
    try {
      await page.locator("#image-preview:not([hidden])").waitFor({ timeout: 5000 });
    } catch (error) {
      const diagnostics = await page.evaluate(() => {
        const preview = document.querySelector("#image-preview");
        const input = document.querySelector("#image-file");
        return {
          imageStatus: document.querySelector("#image-status")?.textContent,
          previewHidden: preview?.hidden,
          previewDisplay: preview ? getComputedStyle(preview).display : null,
          previewSrcPresent: Boolean(preview?.getAttribute("src")),
          previewComplete: preview?.complete,
          previewNaturalWidth: preview?.naturalWidth,
          previewNaturalHeight: preview?.naturalHeight,
          clearImageDisabled: document.querySelector("#clear-image")?.disabled,
          runOcrDisabled: document.querySelector("#run-ocr")?.disabled,
          fileInputValueAfterChange: input?.value
        };
      });
      console.error("[ui-contract image-preview diagnostics]", JSON.stringify(diagnostics));
      throw error;
    }
    assert.match(await page.locator("#image-status").innerText(), /OCR opcional|OCR/i);
    assert.equal(await page.locator("#clear-image").isEnabled(), true);
    assert.equal(await page.getByRole("button", { name: /Reconocer texto \(OCR\)/ }).isEnabled(), true);
    // Stub the OCR engine to test the browser integration deterministically without network access.
    await page.evaluate(() => { window.Tesseract = { recognize: async (image, language) => { if (language !== "spa+eng") throw new Error("Unexpected OCR language"); if (!image || !String(image).startsWith("data:image/")) throw new Error("OCR did not receive the uploaded image data URL"); return { data: { text: "Nodo A\nNodo B\nA --> B" } }; } }; });
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
    // Transition labels/conditions must not be silently dropped during text-to-graph conversion.
    await page.locator("#image-transcription").fill("A -->|si x > 0| B");
    await page.getByRole("button", { name: "Convertir en borrador de grafo" }).click();
    assert.match(await page.locator("#transcription-status").innerText(), /posible etiqueta o condición de transición.*No se importó automáticamente/i);
    await page.locator("#image-transcription").fill("T1: A -> B");
    await page.getByRole("button", { name: "Convertir en borrador de grafo" }).click();
    assert.match(await page.locator("#transcription-status").innerText(), /posible etiqueta o condición de transición.*No se importó automáticamente/i);
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
    const tamperedPackage = structuredClone(packageData);
    tamperedPackage.result.scientific_interpretation += " tampered";
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
    assert.match(await orderPage.locator("#graph-review-summary-text").innerText(), /Conexiones: 1/);
    assert.equal(await orderPage.locator("#graph-review-summary").getAttribute("data-state"), "needs-review");

    // Exercise the live review summary through actual browser controls: duplicate, isolated state, and empty graph.
    await orderPage.locator("#edge-source").selectOption("A");
    await orderPage.locator("#edge-target").selectOption("B");
    await orderPage.locator("#new-edge-add").click();
    assert.match(await orderPage.locator("#graph-review-warnings").innerText(), /duplicado/i);
    assert.match(await orderPage.locator("#graph-review-summary-text").innerText(), /Conexiones: 2/);
    await orderPage.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión t_visual_1/ }).click();
    assert.doesNotMatch(await orderPage.locator("#graph-review-warnings").innerText(), /duplicado/i);

    await orderPage.locator("#new-state-id").fill("ISOLATED_TEST_STATE");
    await orderPage.locator("#new-state-add").click();
    assert.match(await orderPage.locator("#graph-review-warnings").innerText(), /estados aislados/i);
    assert.match(await orderPage.locator("#graph-review-summary-text").innerText(), /Estados: 5/);

    await orderPage.locator("#transition-review-list").getByRole("button", { name: /Eliminar conexión order_ab/ }).click();
    assert.equal(await orderPage.locator("#transition-review-list li").count(), 0);
    assert.equal(await orderPage.locator("#graph-review-summary").getAttribute("data-state"), "needs-review");
    assert.match(await orderPage.locator("#graph-review-summary-text").innerText(), /Conexiones: 0/);
    assert.match(await orderPage.locator("#graph-review-summary-text").innerText(), /No hay aceptación automática/i);
    await orderPage.close();

    // OCR interpretation is a separate, non-destructive layer: suggestions never alter raw OCR or the primary transcription automatically.
    const rawOCR = "Condición: x > O\nCc";
    await page.evaluate((raw) => {
      document.querySelector("#ocr-raw-text").value = raw;
      document.querySelector("#image-transcription").value = raw; // mirrors the normal OCR-completion path; suggestions themselves must not edit it
      window.renderOcrInterpretation(raw, 87.5);
    }, rawOCR);
    assert.equal(await page.locator("#ocr-raw-text").inputValue(), rawOCR);
    assert.equal(await page.locator("#image-transcription").inputValue(), rawOCR, "OCR may populate the transcription; rendering suggestions must not change it");
    assert.match(await page.locator("#ocr-engine-confidence").innerText(), /87.5%/);
    assert.equal(await page.locator("#ocr-suggestions li").count(), 2);
    assert.match(await page.locator("#ocr-suggestions").innerText(), /«O» → posible «0»/);
    assert.match(await page.locator("#ocr-suggestions").innerText(), /«Cc» → posible «C»/);
    assert.match(await page.locator("#ocr-suggestions").innerText(), /Confianza de la sugerencia: no disponible/);
    await page.locator("#ocr-suggestions li").nth(0).getByRole("button", { name: /Aplicar esta alternativa manualmente/ }).click();
    assert.equal(await page.locator("#image-transcription").inputValue(), "Condición: x > 0\nCc");
    assert.equal(await page.locator("#ocr-raw-text").inputValue(), rawOCR, "manual interpretation must not mutate raw OCR");
    await page.locator("#ocr-suggestions li").nth(1).getByRole("button", { name: /Aplicar esta alternativa manualmente/ }).click();
    assert.equal(await page.locator("#image-transcription").inputValue(), "Condición: x > 0\nC");
    assert.equal(await page.locator("#ocr-raw-text").inputValue(), rawOCR, "raw OCR must remain unchanged after all manual suggestions");
    assert.match(await page.locator("#ocr-interpretation-status").innerText(), /aplicada manualmente/);
    await page.evaluate(() => window.renderOcrInterpretation("Etiqueta O normal", null));
    assert.equal(await page.locator("#ocr-suggestions li").count(), 1, "heuristics must be bounded and must not invent an interpretation for arbitrary O");
    assert.match(await page.locator("#ocr-engine-confidence").innerText(), /no disponible/i);
    // Arrowless diagram connectors must remain direction-unknown rather than becoming inferred arrows.
    await page.locator("#image-transcription").fill("graph LR\n  X --- Y");
    await page.locator("#convert-transcription").click();
    const undirectedModel = JSON.parse(await page.locator("#model").inputValue());
    assert.equal(undirectedModel.transitions.length, 1);
    assert.equal(undirectedModel.transitions[0].source, "X");
    assert.equal(undirectedModel.transitions[0].target, "Y");
    assert.equal(Object.hasOwn(undirectedModel.transitions[0], "direction_status"), false,
      "Arrowless-import review metadata must not alter the canonical input schema.");
    assert.match(await page.locator("#graph-review-warnings").innerText(), /sin dirección explícita/i);
    assert.match(await page.locator("#graph-review-summary-text").innerText(), /Direcciones pendientes: 1/);
    assert.match(await page.locator("#transition-review-list").innerText(), /dirección sin resolver/i);
    // Conversion creates a reviewed draft; graph paths exist only after explicit execution.
    await page.locator("#run").click();
    await page.locator('#graph path[data-transition-id="t_import_1"]').waitFor({ state: "attached" });
    assert.equal(await page.locator('#graph path[data-transition-id="t_import_1"]').getAttribute("marker-end"), "none");
    console.log("PASS: UI terminology, profile switching, relation add/remove, edit/run, fail-closed recovery, import/export, replay/tamper checks, and review/run order independence.");
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
