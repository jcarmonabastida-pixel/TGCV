#!/usr/bin/env node
"use strict";

// Engineering-only browser benchmark. Measures synchronous JS engine time and
// user-visible execution-button latency in Chromium. No scientific claims.
const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

function makeModel(size, cap = 10, kind = "cyclic_branching") {
  const states = Array.from({ length: size }, (_, i) => "s" + String(i).padStart(3, "0"));
  const transitions = [];
  const add = (i, j, suffix) => transitions.push({
    id: "t_" + String(i).padStart(3, "0") + "_" + String(j).padStart(3, "0") + "_" + suffix,
    source: states[i], target: states[j]
  });
  if (kind === "chain") {
    for (let i = 0; i < size - 1; i++) add(i, i + 1, "chain");
  } else {
    for (let i = 0; i < size; i++) {
      for (let offset = 1; offset <= 8 && transitions.length < 2000; offset++) {
        const j = kind === "branching_dag" ? i + offset : (i + offset) % size;
        if (j < size) add(i, j, "f" + String(offset).padStart(2, "0"));
      }
    }
  }
  if (transitions.length > 2000) throw new Error("transition limit exceeded");
  return {
    schema_version: "collective-toy-input-001", model_id: "browser-benchmark-" + kind + "-" + size,
    initial_state: states[0], states, transitions, relations: [],
    rule_profile: { type: "finite_deterministic_graph", version: "1" },
    scenarios: [{ id: "baseline", disabled_transitions: [] }],
    exploration: { max_depth: 100, max_trajectories: cap }
  };
}

const median = values => {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length / 2)];
};
const p95 = values => {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.max(0, Math.ceil(sorted.length * 0.95) - 1)];
};

(async () => {
  const browser = await chromium.launch({ headless: true });
  const reports = [];
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    const fileUrl = "file://" + path.resolve(__dirname, "index.html");
    await page.goto(fileUrl);
    for (const kind of ["chain", "branching_dag", "cyclic_branching"]) {
      for (const size of [100, 250, 500]) {
        const model = makeModel(size, 10, kind);
        const json = JSON.stringify(model);
        const engineSamples = [];
        const interactionSamples = [];
        // Warm-up both the pure engine call and the full UI path.
        await page.evaluate(m => window.execute(m), model);
        for (let i = 0; i < 5; i++) {
          const engineMs = await page.evaluate(m => {
            const start = performance.now();
            window.execute(m);
            return performance.now() - start;
          }, model);
          engineSamples.push(engineMs);
          await page.locator("#model").evaluate((el, value) => { el.value = value; }, json);
          const start = Date.now();
          await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
          await page.locator("#status").getByText("Ejecución completada.", { exact: false }).waitFor();
          interactionSamples.push(Date.now() - start);
        }
        reports.push({
          graph_kind: kind, states: size, transitions: model.transitions.length,
          max_depth: 100, max_trajectories: 10, repeats: 5,
          engine_median_ms: Number(median(engineSamples).toFixed(3)),
          engine_p95_ms: Number(p95(engineSamples).toFixed(3)),
          button_to_completed_median_ms: median(interactionSamples),
          button_to_completed_p95_ms: p95(interactionSamples),
          engine_samples_ms: engineSamples,
          interaction_samples_ms: interactionSamples
        });
      }
    }
    if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
    console.log(JSON.stringify({
      benchmark: "collective-toy-browser-engineering-v1",
      scientific_execution: false,
      browser: "Chromium via Playwright",
      note: "Hosted CI timings are comparative diagnostics, not user-device guarantees.",
      reports
    }, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
