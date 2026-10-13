#!/usr/bin/env node
"use strict";

// Engineering-only browser benchmark. Phase timings come from the page's
// performance.now() instrumentation; Playwright wall time is kept separate.
const { chromium } = require("playwright");
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
      for (let offset = 1; offset <= 8 && transitions.length < 1900; offset++) {
        const j = kind === "branching_dag" ? i + offset : (i + offset) % size;
        if (j < size) add(i, j, "f" + String(offset).padStart(2, "0"));
      }
    }
  }
  if (transitions.length >= 2000) throw new Error("transition limit reached; fixture must stay below engine cap");
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
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
};
const percentile = (values, p) => {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.max(0, Math.ceil(sorted.length * p) - 1)];
};
const summarize = values => ({
  median_ms: Number(median(values).toFixed(3)),
  p95_ms: Number(percentile(values, 0.95).toFixed(3)),
  min_ms: Number(Math.min(...values).toFixed(3)),
  max_ms: Number(Math.max(...values).toFixed(3)),
  samples_ms: values.map(v => Number(v.toFixed(3)))
});

(async () => {
  const browser = await chromium.launch({ headless: true });
  const reports = [];
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.goto("file://" + path.resolve(__dirname, "index.html"));
    const phaseNames = ["parse_json_ms", "validate_and_engine_ms", "input_hash_ms", "result_hash_ms", "package_hash_ms", "render_dom_ms", "total_until_status_ms"];
    for (const kind of ["chain", "branching_dag", "cyclic_branching"]) {
      for (const size of [100, 250, 500]) {
        const model = makeModel(size, 10, kind);
        const json = JSON.stringify(model);
        const phaseSamples = Object.fromEntries(phaseNames.map(name => [name, []]));
        const engineSamples = [];
        const interactionSamples = [];
        const heartbeatGapSamples = [];
        const hashPhaseSamples = { canonicalize_ms: [], encode_utf8_ms: [], crypto_digest_ms: [], hex_encode_ms: [], hash_end_to_end_ms: [] };
        const observationHashOperations = Object.fromEntries(["input", "result", "package"].map(operation => [operation, Object.fromEntries(Object.keys(hashPhaseSamples).map(name => [name, []]))]));
        await page.evaluate(m => window.execute(m), model); // warm engine
        await page.locator("#model").evaluate((el, value) => { el.value = value; }, json);
        await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
        await page.locator("#status").getByText("Ejecución completada.", { exact: false }).waitFor(); // warm UI and hashes
        for (let i = 0; i < 15; i++) {
          const engineMs = await page.evaluate(m => {
            const start = performance.now();
            window.execute(m);
            return performance.now() - start;
          }, model);
          engineSamples.push(engineMs);
          await page.locator("#model").evaluate((el, value) => { el.value = value; }, json);
          await page.evaluate(() => {
            window.__toyHashPhaseSamples = { canonicalize_ms: [], encode_utf8_ms: [], crypto_digest_ms: [], hex_encode_ms: [], hash_end_to_end_ms: [], by_operation: { input: { canonicalize_ms: [], encode_utf8_ms: [], crypto_digest_ms: [], hex_encode_ms: [], hash_end_to_end_ms: [] }, result: { canonicalize_ms: [], encode_utf8_ms: [], crypto_digest_ms: [], hex_encode_ms: [], hash_end_to_end_ms: [] }, package: { canonicalize_ms: [], encode_utf8_ms: [], crypto_digest_ms: [], hex_encode_ms: [], hash_end_to_end_ms: [] } } };
            window.__toyHeartbeat = { last: performance.now(), maxGap: 0, running: true };
            const beat = () => {
              const h = window.__toyHeartbeat;
              if (!h || !h.running) return;
              const now = performance.now();
              h.maxGap = Math.max(h.maxGap, now - h.last);
              h.last = now;
              requestAnimationFrame(beat);
            };
            requestAnimationFrame(beat);
          });
          const start = process.hrtime.bigint();
          await page.getByRole("button", { name: "Ejecutar escenarios" }).click();
          await page.locator("#status").getByText("Ejecución completada.", { exact: false }).waitFor();
          const wallMs = Number(process.hrtime.bigint() - start) / 1e6;
          interactionSamples.push(wallMs);
          const observation = await page.evaluate(() => {
            window.__toyHeartbeat.running = false;
            return { phases: window.__toyPerfLastRun, hashPhases: window.__toyHashPhaseSamples, maxGap: window.__toyHeartbeat.maxGap };
          });
          for (const name of phaseNames) {
            if (typeof observation.phases?.[name] === "number") phaseSamples[name].push(observation.phases[name]);
          }
          heartbeatGapSamples.push(observation.maxGap);
          for (const name of Object.keys(hashPhaseSamples)) hashPhaseSamples[name].push(...(observation.hashPhases?.[name] || []));
          for (const operation of Object.keys(observation.hashPhases?.by_operation || {})) {
            for (const name of Object.keys(observation.hashPhases.by_operation[operation])) observationHashOperations[operation][name].push(...observation.hashPhases.by_operation[operation][name]);
          }
        }
        const phaseSummary = Object.fromEntries(phaseNames.filter(n => phaseSamples[n].length).map(n => [n, summarize(phaseSamples[n])]));
        reports.push({
          graph_kind: kind, states: size, transitions: model.transitions.length,
          max_depth: 100, max_trajectories: 10, repeats: 15,
          engine_median_ms: Number(median(engineSamples).toFixed(3)),
          engine_p95_ms: Number(percentile(engineSamples, 0.95).toFixed(3)),
          button_to_completed_median_ms: Number(median(interactionSamples).toFixed(3)),
          button_to_completed_p95_ms: Number(percentile(interactionSamples, 0.95).toFixed(3)),
          engine_samples_ms: engineSamples.map(v => Number(v.toFixed(3))),
          interaction_wall_ms: summarize(interactionSamples),
          phase_timings: phaseSummary,
          hash_subphase_timings: Object.fromEntries(Object.keys(hashPhaseSamples).map(name => [name, summarize(hashPhaseSamples[name])])),
          hash_operation_timings: Object.fromEntries(Object.entries(observationHashOperations).map(([operation, samples]) => [operation, Object.fromEntries(Object.entries(samples).map(([name, values]) => [name, summarize(values)]))])),
          main_thread_frame_gap: summarize(heartbeatGapSamples)
        });
      }
    }
    if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
    console.log(JSON.stringify({
      benchmark: "collective-toy-browser-phase-instrumentation-v2",
      scientific_execution: false,
      browser: "Chromium via Playwright",
      timing_method: "page phases use performance.now(); Playwright wall time uses Node hrtime.bigint(); frame-gap is an approximate rAF heartbeat gap, not a direct user-device latency guarantee.",
      note: "Hosted CI timings are comparative diagnostics, not user-device guarantees. P95 with 15 samples remains a coarse upper-tail diagnostic.",
      reports
    }, null, 2));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
