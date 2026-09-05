"""N-R8-C2 vNext production corpus audit gate.

This gate audits an already-generated corpus and manifest. It NEVER invokes
production generation and NEVER performs scientific EXT-1.1 execution.

The audit is intentionally strict: it verifies artifact hashes, frozen input
SHAs, record count, canonical ordering, pair/state hashes, exact K equality,
recorded O_T inequality, provenance/version fields, uniqueness, and manifest
integrity. Authoritative O_T signatures are recomputed for each distinct state
and compared with the recorded signatures.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
EXECUTION = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "execution"
CORPUS_PATH = EXECUTION / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST_PATH = EXECUTION / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"
OPS_PATH = SRC / "branch_n_r8_operationalisation_v01.py"
KEY_PATH = SRC / "branch_n_r8c2_vnext_key_v01.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"
CONFIG_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1.json"
CONTRACT_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1.md"
GENERATOR_PATH = SRC / "branch_n_r8c2_vnext_generator_v01.py"

TARGET_PAIRS = 5000
SEED = 582031
EXPECTED_CORPUS_SHA256 = "abff66d496c2ab5dadbf5adc0e05daf3c2992c18b1b6118b58c8c4d712910f3f"
EXPECTED_MANIFEST_SHA256 = "03caf7bb680b93b696dd2914dd06b4c30fe4340559c44698bb33fc9be124c323"
EXPECTED_BLOB_SHA = {
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
    "generator": "1cbffad8f14cb004b81e5ef1613e1f288d7962d1",
}
EXPECTED_GENERATOR_VERSION = "branch_n_r8c2_vnext_generator_v01"
EXPECTED_PROVENANCE = "DERIVED_RECONSTRUCTED"
EXPECTED_MANIFEST_ID = "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1"


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_sha(path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def load_ot_module():
    src_dir = str(SRC)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    spec = importlib.util.spec_from_file_location("tgcv_r8c2_ot_authoritative", OT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load authoritative O_T module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_state(ops, record: dict):
    s = record
    return ops.canonical_state(
        s["components"],
        [tuple(e) for e in s["edges"]],
        s["resources"],
        s["objective"],
    )


def pair_id_from_hashes(a_sha: str, b_sha: str) -> str:
    return hashlib.sha256(canonical_json(sorted((a_sha, b_sha))).encode("utf-8")).hexdigest()


def manifest_hash(payload: dict) -> str:
    basis = dict(payload)
    basis.pop("final_manifest_sha256", None)
    return hashlib.sha256(canonical_json(basis).encode("utf-8")).hexdigest()


def audit() -> dict:
    if not CORPUS_PATH.exists() or not MANIFEST_PATH.exists():
        raise RuntimeError("production corpus and manifest must both exist")

    corpus_sha = sha256_file(CORPUS_PATH)
    manifest_sha = sha256_file(MANIFEST_PATH)
    if corpus_sha != EXPECTED_CORPUS_SHA256:
        raise RuntimeError(f"corpus SHA mismatch: {corpus_sha}")
    if manifest_sha != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError(f"manifest SHA mismatch: {manifest_sha}")

    paths = {
        "operationalisation": OPS_PATH,
        "key": KEY_PATH,
        "ot": OT_PATH,
        "config": CONFIG_PATH,
        "contract": CONTRACT_PATH,
        "generator": GENERATOR_PATH,
    }
    frozen = {name: path.exists() and git_blob_sha(path) == sha for name, (path, sha) in
              zip(paths, [(p, EXPECTED_BLOB_SHA[n]) for n, p in paths.items()])}
    if not all(frozen.values()):
        raise RuntimeError(f"frozen input mismatch: {frozen}")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest_hash(manifest) != manifest.get("final_manifest_sha256"):
        raise RuntimeError("manifest self-hash mismatch")
    if manifest.get("corpus_sha256") != corpus_sha:
        raise RuntimeError("manifest corpus_sha256 does not match corpus")
    if manifest.get("accepted_pair_count") != TARGET_PAIRS:
        raise RuntimeError("manifest accepted_pair_count mismatch")
    if manifest.get("target_pair_count") != TARGET_PAIRS or manifest.get("seed") != SEED:
        raise RuntimeError("manifest target/seed mismatch")
    if manifest.get("corpus_generation") != "PERFORMED" or manifest.get("scientific_execution") != "NOT_PERFORMED":
        raise RuntimeError("manifest stage markers are invalid")
    if manifest.get("generator_version") != EXPECTED_GENERATOR_VERSION:
        raise RuntimeError("manifest generator_version mismatch")
    if manifest.get("frozen_input_shas") != dict(sorted(EXPECTED_BLOB_SHA.items())):
        raise RuntimeError("manifest frozen_input_shas mismatch")

    records = []
    with CORPUS_PATH.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if not line.strip():
                raise RuntimeError(f"blank corpus line at {line_no}")
            records.append(json.loads(line))
    if len(records) != TARGET_PAIRS:
        raise RuntimeError(f"corpus record count mismatch: {len(records)}")

    ops = load_ot_module()
    key_mod_spec = importlib.util.spec_from_file_location("tgcv_r8c2_key", KEY_PATH)
    if key_mod_spec is None or key_mod_spec.loader is None:
        raise RuntimeError("cannot load frozen K module")
    key_mod = importlib.util.module_from_spec(key_mod_spec)
    sys.modules[key_mod_spec.name] = key_mod
    key_mod_spec.loader.exec_module(key_mod)

    ot_ops = ops.load_modules()[0]
    state_cache = {}
    ot_cache = {}
    pair_ids = set()
    ordered_keys = []
    failures = []

    for idx, rec in enumerate(records, 1):
        try:
            required = {
                "pair_id", "state_a", "state_b", "state_a_sha256", "state_b_sha256",
                "key_c2_vnext", "key_c2_vnext_sha256", "o_t_a_signature", "o_t_b_signature",
                "provenance", "generator_version", "input_manifest_id",
            }
            missing = required - set(rec)
            if missing:
                raise ValueError(f"missing fields {sorted(missing)}")
            a = load_state(ops, rec["state_a"])
            b = load_state(ops, rec["state_b"])
            a_sha, b_sha = a.sha256(), b.sha256()
            if (a_sha, b_sha) != (rec["state_a_sha256"], rec["state_b_sha256"]):
                raise ValueError("state hash mismatch")
            if not a_sha < b_sha:
                raise ValueError("state hash order violation")
            if rec["pair_id"] != pair_id_from_hashes(a_sha, b_sha):
                raise ValueError("pair_id mismatch")
            if rec["pair_id"] in pair_ids:
                raise ValueError("duplicate pair_id")
            pair_ids.add(rec["pair_id"])

            ka = key_mod.c2_vnext_key(a)
            kb = key_mod.c2_vnext_key(b)
            if ka != kb:
                raise ValueError("K inequality")
            if list(ka) != rec["key_c2_vnext"]:
                raise ValueError("recorded K mismatch")
            if hashlib.sha256(canonical_json(list(ka)).encode("utf-8")).hexdigest() != rec["key_c2_vnext_sha256"]:
                raise ValueError("K hash mismatch")

            for state, sha in ((a, a_sha), (b, b_sha)):
                if sha not in ot_cache:
                    graph = ops.transformation_organisation_graph(state, ot_ops)
                    ot_cache[sha] = ops.graph_signature(graph)
            if ot_cache[a_sha] != tuple(rec["o_t_a_signature"]):
                raise ValueError("O_T(A) signature mismatch")
            if ot_cache[b_sha] != tuple(rec["o_t_b_signature"]):
                raise ValueError("O_T(B) signature mismatch")
            if rec["o_t_a_signature"] == rec["o_t_b_signature"]:
                raise ValueError("O_T inequality violation")
            if rec["provenance"] != EXPECTED_PROVENANCE:
                raise ValueError("provenance mismatch")
            if rec["generator_version"] != EXPECTED_GENERATOR_VERSION:
                raise ValueError("generator_version mismatch")
            if rec["input_manifest_id"] != EXPECTED_MANIFEST_ID:
                raise ValueError("input_manifest_id mismatch")
            ordered_keys.append((a_sha, b_sha))
            state_cache[a_sha] = a
            state_cache[b_sha] = b
        except Exception as exc:
            failures.append({"record": idx, "error": str(exc)})
            if len(failures) >= 10:
                break

    if failures:
        raise RuntimeError(f"corpus semantic audit failed: {failures}")
    if ordered_keys != sorted(ordered_keys):
        raise RuntimeError("corpus records are not lexicographically ordered")

    return {
        "gate": "N-R8-C2_vNEXT_CORPUS_AUDIT_v0.1",
        "status": "PASS",
        "decision": "CORPUS_AUDITED_READY_FOR_FREEZE",
        "corpus_generation": "PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
        "target_pair_count": TARGET_PAIRS,
        "audited_pair_count": len(records),
        "distinct_state_count": len(state_cache),
        "distinct_ot_states_verified": len(ot_cache),
        "corpus_sha256": corpus_sha,
        "manifest_sha256": manifest_sha,
        "manifest_self_hash": manifest.get("final_manifest_sha256"),
        "frozen_input_checks": frozen,
    }


def main() -> None:
    print(json.dumps(audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
