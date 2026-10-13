"use strict";
// Synthetic-only Chromium benchmark. Run: node browser_performance_benchmark.cjs --repeats 5
const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const arg = process.argv.indexOf("--repeats");
const REPEATS = Number(arg >= 0 ? process.argv[arg + 1] : 5);
const SIZES = [100, 250, 500];
const TOPOLOGIES = ["chain", "branching_dag", "branching_cyclic"];
const round = n => Number(n.toFixed(3));
function percentile(values, p) {
  const sorted = [...values].sort((a,b)=>a-b);
  return sorted[Math.min(sorted.length-1, Math.ceil(p*sorted.length)-1)];
}
function summary(values) {
  return {samples_ms:values.map(round),median_ms:round(percentile(values,.5)),p95_ms:round(percentile(values,.95)),min_ms:round(Math.min(...values)),max_ms:round(Math.max(...values))};
}
function fixture(topology,n,repeat) {
  const states=Array.from({length:n},(_,i)=>"s"+String(i).padStart(4,"0"));
  const transitions=[];
  const add=(i,j)=>transitions.push({id:"t"+String(transitions.length).padStart(5,"0"),source:states[i],target:states[j]});
  for(let i=0;i<n-1;i++) add(i,i+1);
  if(topology!=="chain") for(let i=0;i<n;i++) for(const d of [2,3,5]) if(i+d<n) add(i,i+d);
  if(topology==="branching_cyclic") for(let i=2;i<n;i+=7) add(i,i-2);
  return {schema_version:"collective-toy-input-001",model_id:"browser-perf-"+topology+"-"+n+"-"+repeat,
    initial_state:states[0],states,transitions,relations:[],
    rule_profile:{type:"finite_deterministic_graph",version:"1"},
    scenarios:[{id:"baseline",disabled_transitions:[]},{id:"disable_first",disabled_transitions:transitions.length?[transitions[0].id]:[]}],
    exploration:{max_depth:100,max_trajectories:100}};
}
(async()=>{
  if(!Number.isInteger(REPEATS)||REPEATS<3||REPEATS>20) throw new Error("--repeats must be an integer from 3 to 20");
  const browser=await chromium.launch({headless:true});
  const page=await browser.newPage({viewport:{width:1365,height:900}});
  const errors=[]; page.on("pageerror",e=>errors.push(String(e)));
  const reports=[];
  try {
    await page.goto("file://"+path.resolve(__dirname,"index.html"));
    for(const size of SIZES) for(const topology of TOPOLOGIES) {
      const samples=[]; let lastFixture;
      for(let repeat=1;repeat<=REPEATS;repeat++) {
        const model=fixture(topology,size,repeat); lastFixture=model;
        await page.locator("#model").fill(JSON.stringify(model));
        const wallStart=Date.now();
        await page.locator("#run").click();
        await page.waitForFunction(()=>{const s=document.querySelector("#status");return s&&(s.textContent.startsWith("Ejecución completada.")||s.textContent.startsWith("No se ha podido ejecutar:"));},{},{timeout:30000});
        const observed=await page.evaluate(()=>({status:document.querySelector("#status").textContent,perf:window.__toyPerfLastRun||null,
          svg_elements:document.querySelectorAll("#graph *").length}));
        if(!observed.status.startsWith("Ejecución completada.")) throw new Error(observed.status);
        if(!observed.perf||typeof observed.perf.total_until_status_ms!=="number") throw new Error("Instrumentation window.__toyPerfLastRun missing");
        samples.push({...observed.perf,wall_clock_ms:Date.now()-wallStart,svg_elements:observed.svg_elements});
      }
      const phases={};
      for(const k of ["parse_json_ms","validate_and_engine_ms","input_hash_ms","result_hash_ms","package_hash_ms","render_dom_ms","total_until_status_ms","wall_clock_ms"]) phases[k]=summary(samples.map(s=>s[k]));
      reports.push({topology,states:size,transitions:lastFixture.transitions.length,repeats:REPEATS,
        exploration_caps:{max_depth:100,max_trajectories:100},phases,
        svg_elements_median:percentile(samples.map(s=>s.svg_elements),.5),raw_samples:samples});
    }
  } finally { await browser.close(); }
  const output={benchmark:"collective-toy-browser-performance-001",scientific_execution:false,
    source_html:"prototypes/collective_toy/web/index.html",browser:"Chromium via Playwright",node_version:process.version,
    repeats:REPEATS,sizes:SIZES,topologies:TOPOLOGIES,page_errors:errors,reports};
  const out=path.resolve(process.cwd(),"browser-performance-results.json");
  fs.writeFileSync(out,JSON.stringify(output,null,2)+"\n");
  console.log(JSON.stringify({output:out,cases:reports.length,reports:reports.map(r=>({topology:r.topology,states:r.states,transitions:r.transitions,
    total_median_ms:r.phases.total_until_status_ms.median_ms,total_p95_ms:r.phases.total_until_status_ms.p95_ms,
    engine_median_ms:r.phases.validate_and_engine_ms.median_ms,render_median_ms:r.phases.render_dom_ms.median_ms}))},null,2));
  if(errors.length) throw new Error("Browser page errors: "+errors.join("; "));
})().catch(e=>{console.error(e);process.exit(1)});
