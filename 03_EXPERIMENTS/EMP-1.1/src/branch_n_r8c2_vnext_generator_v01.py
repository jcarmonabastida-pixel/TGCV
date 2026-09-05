"""N-R8-C2 vNext prospective corpus generator.

Preparation-stage implementation. Candidate construction is result-blind:
K_C2_vNext is computed before any O_T evaluation. O_T is imported only through
the authoritative identifiability implementation and evaluated post hoc.

The module is intentionally usable in two modes:
- ``dry_run`` exercises the generation boundary without writing the corpus;
- ``main`` performs the contracted 5,000-pair corpus generation when explicitly
  invoked by the operator.

Importing this module never generates a corpus and never performs scientific
EXT-1.1 execution.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_key_v01 import c2_vnext_key

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
OUTPUT_DIR = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "execution"
CORPUS_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"
OPS_PATH = SRC / "branch_n_r8_operationalisation_v01.py"
KEY_PATH = SRC / "branch_n_r8c2_vnext_key_v01.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"
CONFIG_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1.json"
CONTRACT_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1.md"

TARGET_PAIRS = 5000
SEED = 582031
COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))
# These are Git blob SHAs, not SHA-256 digests. Verification therefore uses
# `git hash-object`, matching the SHAs reported by the GitHub Contents API.
EXPECTED_BLOB_SHA = {
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
}
EXPECTED_SHA256 = EXPECTED_BLOB_SHA


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_sha(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "hash-object", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"cannot compute Git blob SHA for {path}") from exc
    return result.stdout.strip()


def verify_frozen_inputs() -> dict[str, bool]:
    paths = {
        "operationalisation": OPS_PATH,
        "key": KEY_PATH,
        "ot": OT_PATH,
        "config": CONFIG_PATH,
        "contract": CONTRACT_PATH,
    }
    return {
        name: path.exists() and git_blob_sha(path) == EXPECTED_BLOB_SHA[name]
        for name, path in paths.items()
    }


def load_ot_module():
    src_dir = str(SRC)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    spec = importlib.util.spec_from_file_location("tgcv_r8c2_ot_authoritative", OT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load authoritative O_T: {OT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_state_from_rng(rng: random.Random):
    """Result-blind candidate construction from frozen state variables only."""
    n = rng.choice((4, 5, 6))
    components = rng.sample(list(COMPONENTS), n)
    possible = [(a, b) for a in components for b in components if a != b]
    density = rng.choice((0.10, 0.25, 0.50, 0.75))
    k = round(density * len(possible))
    edges = rng.sample(possible, k)
    resources = tuple(rng.randrange(4) for _ in range(3))
    objective = rng.choice(OBJECTIVES)
    return canonical_state(components, edges, resources, objective)


def generate_candidate(rng: random.Random):
    return canonical_state_from_rng(rng)


def build_candidate_buckets(candidates: Iterable) -> dict[tuple, list]:
    """Bucket solely by frozen K; O_T is absent from this construction stage."""
    buckets: dict[tuple, list] = {}
    for state in candidates:
        key = c2_vnext_key(state)
        buckets.setdefault(key, []).append(state)
    return buckets


def ordered_pairs(bucket: list):
    states = sorted(bucket, key=lambda s: s.sha256())
    for i, a in enumerate(states):
        for b in states[i + 1:]:
            yield a, b


def evaluate_ot_after_key_equality(state_a, state_b):
    """Evaluate authoritative O_T only after exact K equality has been checked."""
    if c2_vnext_key(state_a) != c2_vnext_key(state_b):
        raise ValueError("O_T evaluation forbidden before key equality")
    ot = load_ot_module()
    ops = ot.load_modules()[0]
    ga = ot.transformation_organisation_graph(state_a, ops)
    gb = ot.transformation_organisation_graph(state_b, ops)
    return ot.graph_signature(ga), ot.graph_signature(gb)


def pair_id(state_a, state_b) -> str:
    hashes = sorted((state_a.sha256(), state_b.sha256()))
    return hashlib.sha256(canonical_json(hashes).encode("utf-8")).hexdigest()


def state_record(state) -> dict:
    return {
        "components": list(state.components),
        "edges": [list(e) for e in state.edges],
        "resources": list(state.resources),
        "objective": state.objective,
    }


def _pair_record(state_a, state_b, ot_a, ot_b) -> dict:
    key = c2_vnext_key(state_a)
    if key != c2_vnext_key(state_b):
        raise RuntimeError("accepted pair violates exact key equality")
    if ot_a == ot_b:
        raise RuntimeError("accepted pair does not establish O_T inequality")
    return {
        "pair_id": pair_id(state_a, state_b),
        "state_a": state_record(state_a),
        "state_b": state_record(state_b),
        "state_a_sha256": state_a.sha256(),
        "state_b_sha256": state_b.sha256(),
        "key_c2_vnext": list(key),
        "key_c2_vnext_sha256": hashlib.sha256(canonical_json(list(key)).encode("utf-8")).hexdigest(),
        "o_t_a_signature": ot_a,
        "o_t_b_signature": ot_b,
        "provenance": "DERIVED_RECONSTRUCTED",
        "generator_version": "branch_n_r8c2_vnext_generator_v01",
        "input_manifest_id": "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1",
    }


def _generation_core(target_pairs: int = TARGET_PAIRS, seed: int = SEED, dry_run: bool = False):
    """Deterministically construct accepted pairs; optionally return them in-memory."""
    frozen = verify_frozen_inputs()
    if not all(frozen.values()):
        raise RuntimeError(f"frozen input verification failed: {frozen}")
    if target_pairs < 1:
        raise ValueError("target_pairs must be positive")

    rng = random.Random(seed)
    buckets: dict[tuple, list] = {}
    seen_pair_ids: set[str] = set()
    accepted: list[dict] = []
    equal_key_pairs_examined = 0
    rejected_equal_ot = 0
    candidate_count = 0
    ot_cache: dict[str, tuple] = {}

    while len(accepted) < target_pairs:
        state = generate_candidate(rng)
        candidate_count += 1
        key = c2_vnext_key(state)
        bucket = buckets.setdefault(key, [])

        # Only states already in the exact-K bucket can reach O_T.
        for other in sorted(bucket, key=lambda s: s.sha256()):
            equal_key_pairs_examined += 1
            a, b = sorted((other, state), key=lambda s: s.sha256())
            a_sha, b_sha = a.sha256(), b.sha256()
            pid = pair_id(a, b)
            if pid in seen_pair_ids:
                raise RuntimeError(f"duplicate pair_id: {pid}")

            if a_sha not in ot_cache:
                ot_cache[a_sha] = evaluate_ot_after_key_equality(a, a)
            if b_sha not in ot_cache:
                ot_cache[b_sha] = evaluate_ot_after_key_equality(b, b)
            ot_a, ot_b = ot_cache[a_sha], ot_cache[b_sha]
            if ot_a == ot_b:
                rejected_equal_ot += 1
                continue

            record = _pair_record(a, b, ot_a, ot_b)
            seen_pair_ids.add(pid)
            accepted.append(record)
            if len(accepted) >= target_pairs:
                break
        bucket.append(state)

    return {
        "records": accepted,
        "candidate_count": candidate_count,
        "equal_key_pairs_examined": equal_key_pairs_examined,
        "rejected_equal_ot": rejected_equal_ot,
        "frozen_input_checks": frozen,
    }


def dry_run(sample_pairs: int = 1, seed: int = SEED) -> dict:
    """Exercise the full pairing boundary without writing corpus artifacts."""
    result = _generation_core(target_pairs=sample_pairs, seed=seed, dry_run=True)
    return {
        "status": "PASS",
        "dry_run": True,
        "accepted_pair_count": len(result["records"]),
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }


def manifest(config: dict, input_shas: dict[str, str]) -> dict:
    return {
        "contract_version": "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1",
        "generator_version": "branch_n_r8c2_vnext_generator_v01",
        "seed": SEED,
        "target_pair_count": TARGET_PAIRS,
        "frozen_input_shas": dict(sorted(input_shas.items())),
        "configuration": config,
        "status": "PREPARATION_ONLY",
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _write_corpus(records: list[dict]) -> str:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with CORPUS_PATH.open("w", encoding="utf-8", newline="\n") as fh:
        for record in records:
            fh.write(canonical_json(record) + "\n")
    return file_sha256(CORPUS_PATH)


def _final_manifest_hash(payload: dict) -> str:
    basis = dict(payload)
    basis.pop("final_manifest_sha256", None)
    return hashlib.sha256(canonical_json(basis).encode("utf-8")).hexdigest()


def run_generation(target_pairs: int = TARGET_PAIRS, seed: int = SEED) -> dict:
    """Execute the contracted prospective corpus generation only."""
    if target_pairs != TARGET_PAIRS:
        raise ValueError(f"contract fixes target_pair_count={TARGET_PAIRS}")
    if seed != SEED:
        raise ValueError(f"contract fixes seed={SEED}")

    started = _utc_now()
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    input_shas = {
        "operationalisation": git_blob_sha(OPS_PATH),
        "key": git_blob_sha(KEY_PATH),
        "ot": git_blob_sha(OT_PATH),
        "config": git_blob_sha(CONFIG_PATH),
        "contract": git_blob_sha(CONTRACT_PATH),
        "generator": git_blob_sha(Path(__file__)),
    }
    result = _generation_core(target_pairs=target_pairs, seed=seed)
    corpus_sha = _write_corpus(result["records"])
    ended = _utc_now()

    payload = {
        "contract_version": "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1",
        "generator_version": "branch_n_r8c2_vnext_generator_v01",
        "seed": seed,
        "target_pair_count": target_pairs,
        "accepted_pair_count": len(result["records"]),
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "frozen_input_shas": dict(sorted(input_shas.items())),
        "deterministic_rerun_result": "NOT_CHECKED",
        "start_utc": started,
        "end_utc": ended,
        "corpus_sha256": corpus_sha,
        "status": "PASS",
        "corpus_generation": "PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }
    payload["final_manifest_sha256"] = _final_manifest_hash(payload)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(canonical_json(payload) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    result = run_generation()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
