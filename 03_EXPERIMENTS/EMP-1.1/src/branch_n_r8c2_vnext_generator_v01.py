from __future__ import annotations

import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parents[3]
OUTPUT_DIR = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "execution"
CORPUS_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"
TARGET_PAIRS = 5000
SEED = 582031

OPERATIONALISATION_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_OPERATIONALISATION_v0.1.md"
KEY_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_KEY_v0.1.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"
CONFIG_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1.json"
CONTRACT_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1.md"
EXPECTED_FROZEN_INPUT_SHAS = {
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
}


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_frozen_inputs() -> dict[str, bool]:
    paths = {
        "operationalisation": OPERATIONALISATION_PATH,
        "key": KEY_PATH,
        "ot": OT_PATH,
        "config": CONFIG_PATH,
        "contract": CONTRACT_PATH,
    }
    return {name: path.exists() and file_sha256(path) == EXPECTED_FROZEN_INPUT_SHAS[name] for name, path in paths.items()}


class State:
    def __init__(self, components: tuple[str, ...], edges: tuple[tuple[str, str], ...], resources: tuple[int, ...], objective: str):
        self.components = tuple(components)
        self.edges = tuple(edges)
        self.resources = tuple(resources)
        self.objective = objective

    def canonical(self) -> dict:
        return {
            "components": list(self.components),
            "edges": [list(e) for e in self.edges],
            "resources": list(self.resources),
            "objective": self.objective,
        }

    def sha256(self) -> str:
        return hashlib.sha256(canonical_json(self.canonical()).encode("utf-8")).hexdigest()


def canonical_state(components, edges, resources, objective):
    return State(tuple(sorted(components)), tuple(sorted(tuple(sorted(e)) for e in edges)), tuple(resources), objective)


def c2_vnext_key(state: State) -> tuple:
    """Frozen reconstructed C2-vNext key; deliberately excludes O_T."""
    return (
        len(state.components),
        tuple(state.components),
        tuple(sorted(state.edges)),
        tuple(state.resources),
        state.objective,
    )


def canonical_state_from_rng(rng: random.Random) -> State:
    component_count = rng.choice((4, 5, 6))
    components = tuple(sorted(rng.sample(("A1", "A2", "B1", "B2", "C1", "C2"), component_count)))
    edge_density = rng.choice((0.10, 0.25, 0.50, 0.75))
    possible = [(a, b) for a in components for b in components if a != b]
    edge_count = int(round(edge_density * len(possible)))
    edges = tuple(rng.sample(possible, edge_count)) if edge_count else ()
    resources = tuple(rng.randint(0, 3) for _ in components)
    objective = rng.choice(tuple(f"O{i:02d}" for i in range(1, 13)))
    return canonical_state(components, edges, resources, objective)


def generate_candidate(rng: random.Random) -> State:
    return canonical_state_from_rng(rng)


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

    # Frozen contract: accepted corpus records are emitted in
    # lexicographic (state_A_sha256, state_B_sha256) order.
    accepted.sort(key=lambda r: (r["state_a_sha256"], r["state_b_sha256"]))

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
    result = _generation_core(target_pairs=target_pairs, seed=seed, dry_run=False)
    corpus_sha = _write_corpus(result["records"])
    payload = manifest({"target_pair_count": target_pairs, "seed": seed}, result["frozen_input_checks"])
    payload.update({
        "status": "GENERATED",
        "corpus_generation": "COMPLETED",
        "scientific_execution": "NOT_PERFORMED",
        "accepted_pair_count": len(result["records"]),
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "corpus_sha256": corpus_sha,
        "generated_at_utc": _utc_now(),
    })
    payload["final_manifest_sha256"] = _final_manifest_hash(payload)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(canonical_json(payload) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    print(json.dumps(run_generation(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
