#!/usr/bin/env python3
"""Reproducible engineering benchmark for the synthetic Collective Toy engine.

Run from this directory with:
  python benchmark_collective_toy_engine_001.py --repeats 5
  python benchmark_collective_toy_engine_001.py --repeats 3 --sizes 100 250 500

The optional scale profile exercises the engine's full documented state and
transition bounds. This is a performance diagnostic, not a scientific TGCV
experiment. It reports raw timings and Python allocation peaks and imposes no
machine-dependent latency thresholds.
"""
from __future__ import annotations

import argparse
import json
import statistics
import time
import tracemalloc

from collective_toy_engine_001 import demo_model, run_model


MAX_STATES = 500
MAX_TRANSITIONS = 2000
MAX_FAN_OUT = 8


def make_model(kind: str, size: int, max_trajectories: int, max_depth: int) -> dict:
    model = demo_model()
    states = [f"s{i:03d}" for i in range(size)]
    transitions: list[dict[str, str]] = []

    def add(source: int, target: int, suffix: str) -> None:
        transitions.append({
            "id": f"t_{source:03d}_{target:03d}_{suffix}",
            "source": states[source],
            "target": states[target],
        })

    if kind == "chain":
        for i in range(size - 1):
            add(i, i + 1, "chain")
    elif kind in ("branching_dag", "cyclic_branching"):
        # Keep the fan-out bounded and spread it across every state so the
        # largest fixtures stay within the engine cap without leaving a tail
        # of states unconnected merely because an edge counter was exhausted.
        fan_out = min(MAX_FAN_OUT, max(1, MAX_TRANSITIONS // size), size - 1)
        for i in range(size):
            for offset in range(1, fan_out + 1):
                target = i + offset
                if kind == "branching_dag":
                    if target < size:
                        add(i, target, f"f{offset:02d}")
                else:
                    add(i, target % size, f"f{offset:02d}")
    else:
        raise ValueError(f"unsupported graph kind: {kind}")

    if len(states) > MAX_STATES or len(transitions) > MAX_TRANSITIONS:
        raise ValueError("benchmark fixture exceeds the engine's documented resource bounds")

    model["states"] = states
    model["initial_state"] = states[0]
    model["transitions"] = transitions
    model["relations"] = []
    model["rule_profile"] = {"type": "temporal_prerequisite_graph", "version": "1"}
    model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
    model["exploration"] = {
        "max_depth": min(max_depth, 100),
        "max_trajectories": min(max_trajectories, 10000),
    }
    return model


def measure(model: dict) -> dict:
    tracemalloc.start()
    started = time.perf_counter()
    try:
        result = run_model(model)
        elapsed_ms = (time.perf_counter() - started) * 1000
        _, peak_bytes = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    scenario = result["scenario_results"]["baseline"]
    return {
        "elapsed_ms": round(elapsed_ms, 3),
        "python_peak_alloc_bytes": peak_bytes,
        "states": len(model["states"]),
        "transitions": len(model["transitions"]),
        "max_depth": model["exploration"]["max_depth"],
        "max_trajectories": model["exploration"]["max_trajectories"],
        "trajectories_emitted": len(scenario["trajectories"]),
        "truncated": scenario["truncated"],
        "reachable_states": len(scenario["reachable_states"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--sizes", type=int, nargs="+", default=[25, 50, 100])
    parser.add_argument("--max-trajectories", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=100)
    args = parser.parse_args()
    if args.repeats < 1:
        parser.error("--repeats must be >= 1")
    if any(size < 2 or size > MAX_STATES for size in args.sizes):
        parser.error(f"--sizes must be between 2 and {MAX_STATES}")

    reports = []
    for kind in ("chain", "branching_dag", "cyclic_branching"):
        for size in args.sizes:
            model = make_model(kind, size, args.max_trajectories, args.max_depth)
            measure(model)  # warm-up, reported separately from timed repeats
            samples = [measure(model) for _ in range(args.repeats)]
            times = [sample["elapsed_ms"] for sample in samples]
            ordered = sorted(times)
            p95_index = max(0, min(len(ordered) - 1, int(0.95 * len(ordered) + 0.999) - 1))
            reports.append({
                "graph_kind": kind,
                "size": size,
                "states": len(model["states"]),
                "transitions": len(model["transitions"]),
                "warmup_excluded": True,
                "repeats": args.repeats,
                "median_elapsed_ms": round(statistics.median(times), 3),
                "p95_elapsed_ms": ordered[p95_index],
                "peak_alloc_bytes_max": max(s["python_peak_alloc_bytes"] for s in samples),
                "samples": samples,
            })

    print(json.dumps({
        "benchmark": "collective-toy-engine-engineering-v1",
        "scientific_execution": False,
        "latency_threshold_enforced": False,
        "resource_bounds": {"max_states": MAX_STATES, "max_transitions": MAX_TRANSITIONS},
        "reports": reports,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
