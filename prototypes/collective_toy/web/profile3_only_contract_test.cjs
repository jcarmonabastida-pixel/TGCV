#!/usr/bin/env node
"use strict";

// Grouped acceptance contract for the single-profile Full Chain demonstrator.
// This deliberately tests product + engine boundaries, not implementation internals.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { spawnSync } = require("node:child_process");

const root = path.resolve(__dirname, "..");
const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
const enginePath = path.join(root, "collective_toy_engine_001.py");

function testProductSurface() {
  for (const id of ["profile-editor", "guarded-transition", "required-transition", "add-relation", "relation-list"]) {
    assert.doesNotMatch(html, new RegExp('id="' + id + '"'), "obsolete profile/relation control remains in the product: " + id);
  }
  assert.doesNotMatch(html, /finite_deterministic_graph|relation_guarded_graph|requires_transition_enabled/,
    "the browser product must not expose or implement retired profiles");
  assert.match(html, /temporal_prerequisite_graph/,
    "the browser product must explicitly use the Full Chain temporal prerequisite profile");
  assert.match(html, /function modelFromEdges/,
    "graph import/transcription must continue to produce editable models");
  assert.match(html, /rule_profile:\{type:"temporal_prerequisite_graph",version:"1"\}/,
    "new example models must default to profile 3");
}

function testEngineBoundary() {
  const script = String.raw`
import copy, sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]).parent))
import collective_toy_engine_001 as engine

base = {
  "schema_version": "collective-toy-input-001",
  "model_id": "profile3-only-contract",
  "initial_state": "A",
  "states": ["A", "B", "C"],
  "transitions": [
    {"id": "t_ab", "source": "A", "target": "B"},
    {"id": "t_ac", "source": "A", "target": "C"},
    {"id": "t_bc", "source": "B", "target": "C"}
  ],
  "relations": [
    {"id": "r_bc_requires_ab", "type": "requires_prior_execution",
     "transition_id": "t_bc", "requires_transition_id": "t_ab"}
  ],
  "rule_profile": {"type": "temporal_prerequisite_graph", "version": "1"},
  "scenarios": [
    {"id": "baseline", "disabled_transitions": []},
    {"id": "disable_prerequisite", "disabled_transitions": ["t_ab"]}
  ],
  "exploration": {"max_depth": 10, "max_trajectories": 100}
}

engine.validate_model(base)
result = engine.run_model(base)
assert result["validation"] == "PASS"
assert result["rule_profile"] == base["rule_profile"]
assert "baseline" in result["scenario_results"]
assert "disable_prerequisite" in result["scenario_results"]

paths = result["scenario_results"]["baseline"]["trajectories"]
for path in paths:
    ids = [step["transition"] for step in path if "transition" in step]
    if "t_bc" in ids:
        assert "t_ab" in ids and ids.index("t_ab") < ids.index("t_bc"), "enumeration must enforce temporal prerequisites"

blocked = engine.execute_sequence(base, "baseline", ["t_ac", "t_bc"])
assert blocked["status"] == "BLOCKED"
assert blocked["blocked_step"]["index"] == 2
assert blocked["blocked_step"]["transition_id"] == "t_bc"
assert blocked["blocked_step"]["required_transition_id"] == "t_ab"
assert blocked["blocked_step"]["reason"] == "temporal_prerequisite_not_satisfied"

for retired in (
    {"type": "finite_deterministic_graph", "version": "1"},
    {"type": "relation_guarded_graph", "version": "1"},
):
    candidate = copy.deepcopy(base)
    candidate["rule_profile"] = retired
    try:
        engine.validate_model(candidate)
    except engine.ModelValidationError:
        pass
    else:
        raise AssertionError("retired rule profile must be rejected, not reinterpreted: " + retired["type"])

for invalid_relation in (
    {"id": "r_bad", "type": "requires_transition_enabled",
     "transition_id": "t_bc", "requires_transition_id": "t_ab"},
    {"id": "r_self", "type": "requires_prior_execution",
     "transition_id": "t_ab", "requires_transition_id": "t_ab"},
):
    candidate = copy.deepcopy(base)
    candidate["relations"] = [invalid_relation]
    try:
        engine.validate_model(candidate)
    except engine.ModelValidationError:
        pass
    else:
        raise AssertionError("invalid relation semantics must be rejected: " + invalid_relation["id"])

package = engine.export_run(base)
assert engine.assess_exported_package(package)["status"] == "replay-verified"
tampered = copy.deepcopy(package)
tampered["input"]["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
try:
    engine.assess_exported_package(tampered)
except engine.ModelValidationError:
    pass
else:
    raise AssertionError("package replay must reject a retired profile")
print("PASS: profile-3-only engine, temporal relations, and replay boundary")
`;
  const run = spawnSync("python", ["-c", script, enginePath], { encoding: "utf8" });
  assert.equal(run.status, 0, "Python engine contract failed:\n" + run.stdout + "\n" + run.stderr);
  process.stdout.write(run.stdout);
}

testProductSurface();
testEngineBoundary();
console.log("PASS: grouped profile-3-only Full Chain acceptance contract");
