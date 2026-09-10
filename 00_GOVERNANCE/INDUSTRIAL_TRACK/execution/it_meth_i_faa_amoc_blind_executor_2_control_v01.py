#!/usr/bin/env python3
"""IT-METH-I FAA AMOC Blind Executor-2 control harness v0.7.

DRY-RUN CONTROL ONLY. Uses canonical GitHub repository blob SHAs at HEAD
for package/evidence integrity; local checkout line-ending normalization
must not alter repository-level integrity verification.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ID = "IT-METH-I-AMOC-BLIND-EXEC-001"
CASE_ID = "IT-G1-I-AMOC-US-91-12-10-7K0-18-00734"
EXPECTED_PACKAGE_GIT_BLOB_SHA = "722e9150b0b8c337950d0978d9f8ffaf400a4b3c"
FORBIDDEN_TERMS = (
    "RECONSTRUCTION_001",
    "IT-G4_I_FAA_AMOC_UTILITY_EXECUTION_RESULT_001",
    "IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_001",
    "COMPARISON",
)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    h = hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode("utf-8"))
    h.update(data)
    return h.hexdigest()


def git_head_blob_sha(repo_root: Path, repo_path: str) -> str | None:
    """Return the canonical blob SHA stored at HEAD, independent of checkout filters."""
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", f"HEAD:{repo_path.replace(chr(92), '/') }"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def relative_repo_path(path: Path, repo_root: Path) -> str | None:
    try:
        return path.resolve(strict=False).relative_to(repo_root.resolve(strict=False)).as_posix()
    except ValueError:
        return None


def resolved(path: Path) -> Path:
    return path.resolve(strict=False)


def is_within(path: Path, root: Path) -> bool:
    try:
        resolved(path).relative_to(resolved(root))
        return True
    except ValueError:
        return False


def roots_disjoint(a: Path, b: Path) -> bool:
    return not is_within(a, b) and not is_within(b, a)


def scan_declared_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace").upper()
    except OSError:
        return []
    return [term for term in FORBIDDEN_TERMS if term in text]


def symlink_paths(root: Path) -> list[str]:
    if not root.exists() or not root.is_dir():
        return []
    return [str(p) for p in sorted(root.rglob("*")) if p.is_symlink()]


def read_declared_manifest(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("declared evidence manifest must be a non-empty JSON list")
    out: list[dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("manifest entries must be objects")
        allowed = {"repo_path", "git_blob_sha", "sha256", "source_role", "source_locator"}
        if not set(item).issubset(allowed) or "repo_path" not in item or "source_role" not in item:
            raise ValueError("manifest entries require repo_path and source_role")
        if not (item.get("git_blob_sha") or item.get("sha256")):
            raise ValueError("manifest entry requires git_blob_sha or sha256")
        repo_path = str(Path(item["repo_path"]))
        git_sha = str(item.get("git_blob_sha", "")).lower()
        sha256 = str(item.get("sha256", "")).lower()
        if git_sha and (len(git_sha) != 40 or any(c not in "0123456789abcdef" for c in git_sha)):
            raise ValueError(f"invalid git_blob_sha for {repo_path}")
        if sha256 and (len(sha256) != 64 or any(c not in "0123456789abcdef" for c in sha256)):
            raise ValueError(f"invalid sha256 for {repo_path}")
        out.append({"repo_path": repo_path, "git_blob_sha": git_sha, "sha256": sha256,
                    "source_role": str(item["source_role"]),
                    "source_locator": str(item.get("source_locator", ""))})
    paths = [e["repo_path"] for e in out]
    if len(set(paths)) != len(paths):
        raise ValueError("duplicate manifest repo_path")
    return sorted(out, key=lambda x: x["repo_path"])


def verify_manifest(entries: list[dict[str, str]], repo_root: Path, evidence_root: Path):
    errors: list[str] = []
    observed: list[dict[str, str]] = []
    for entry in entries:
        p = resolved(repo_root / entry["repo_path"])
        if not is_within(p, repo_root):
            errors.append(f"manifest path outside repository root: {p}")
            continue
        if not is_within(p, evidence_root):
            errors.append(f"manifest path outside evidence root: {p}")
            continue
        if p.is_symlink() or not p.is_file():
            errors.append(f"manifest file unavailable or symlinked: {p}")
            continue
        canonical_git = git_head_blob_sha(repo_root, entry["repo_path"])
        observed_local_git = git_blob_sha1(p)
        observed_sha = sha256_file(p)
        if canonical_git is None:
            errors.append(f"repository HEAD blob unavailable: {entry['repo_path']}")
        elif entry["git_blob_sha"] and canonical_git != entry["git_blob_sha"]:
            errors.append(f"canonical Git blob hash mismatch: {p}")
        if entry["sha256"] and observed_sha != entry["sha256"]:
            errors.append(f"sha256 mismatch: {p}")
        observed.append({"repo_path": entry["repo_path"],
                         "git_blob_sha_observed": canonical_git,
                         "local_checkout_blob_sha_observed": observed_local_git,
                         "sha256_observed": observed_sha,
                         "source_role": entry["source_role"],
                         "source_locator": entry["source_locator"]})
    return not errors, errors, observed


def dependency_inventory() -> list[str]:
    return sorted(f"{d.metadata['Name']}=={d.version}" for d in importlib.metadata.distributions()
                  if d.metadata.get("Name"))


def git_head() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
                                       stderr=subprocess.DEVNULL, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def control(args: argparse.Namespace) -> dict:
    package = resolved(args.package)
    repo_root = resolved(args.repo_root)
    evidence = resolved(args.evidence)
    output = resolved(args.output)
    manifest_path = resolved(args.evidence_manifest)
    sequence = [{"event": "control_start", "timestamp_utc": now()}]
    result: dict[str, object] = {
        "PACKAGE_ID": PACKAGE_ID,
        "CASE_ID": CASE_ID,
        "EXECUTION_MODE": "DRY_RUN_CONTROL",
        "CONTROL_SEQUENCE": sequence,
        "CONTROL_TIMESTAMP_UTC": sequence[0]["timestamp_utc"],
        "REPOSITORY_HEAD_OBSERVED": git_head(),
        "EXPECTED_PACKAGE_GIT_BLOB_SHA": EXPECTED_PACKAGE_GIT_BLOB_SHA,
    }

    package_repo_path = relative_repo_path(package, repo_root)
    package_git = git_head_blob_sha(repo_root, package_repo_path) if package_repo_path else None
    package_local_git = git_blob_sha1(package) if package.is_file() and not package.is_symlink() else None
    package_sha256 = sha256_file(package) if package.is_file() and not package.is_symlink() else None
    result["PACKAGE_REPO_PATH"] = package_repo_path
    result["PACKAGE_GIT_BLOB_SHA_OBSERVED"] = package_git
    result["PACKAGE_LOCAL_CHECKOUT_BLOB_SHA_OBSERVED"] = package_local_git
    result["PACKAGE_SHA256_OBSERVED"] = package_sha256
    result["PACKAGE_INTEGRITY"] = "PASS" if package_git == EXPECTED_PACKAGE_GIT_BLOB_SHA else "FAIL"
    result["PACKAGE_INTEGRITY_ANCHOR_TYPE"] = "GIT_BLOB_SHA1_CANONICAL_REPOSITORY_ANCHOR"
    result["PACKAGE_METADATA_ROLE"] = "OBSERVED_PACKAGE_METADATA_ONLY"

    try:
        declared = read_declared_manifest(manifest_path)
        manifest_ok, manifest_errors, observed = verify_manifest(declared, repo_root, evidence)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        declared, manifest_ok, manifest_errors, observed = [], False, [f"manifest validation error: {exc}"], []
    result["DECLARED_EVIDENCE_MANIFEST"] = declared
    result["OBSERVED_EVIDENCE_RECORDS"] = observed
    result["EVIDENCE_MANIFEST_STATUS"] = "PASS" if manifest_ok else "FAIL"
    result["EVIDENCE_MANIFEST_ERRORS"] = manifest_errors
    result["EVIDENCE_MODEL"] = "GITHUB_DOCUMENTARY_RECORDS_CHECKED_OUT_LOCALLY"

    evidence_symlinks = symlink_paths(evidence)
    package_hits = scan_declared_file(package) if package.is_file() else []
    evidence_hits = []
    for e in declared:
        hits = scan_declared_file(resolved(repo_root / e["repo_path"]))
        if hits:
            evidence_hits.append({"repo_path": e["repo_path"], "terms": hits})
    result["CONTENT_SCAN_SUPPLEMENTARY"] = {"package": package_hits, "evidence": evidence_hits}
    result["DECLARED_EVIDENCE_BOUNDARY_STATUS"] = "PASS" if manifest_ok and not evidence_symlinks else "FAIL"
    result["DECLARED_EVIDENCE_BOUNDARY_BASIS"] = "external manifest + exact GitHub documentary record anchors + canonical HEAD blob verification + symlink rejection"
    result["RUNTIME_FILESYSTEM_ISOLATION_STATUS"] = "NOT_VERIFIED"
    result["RECONSTRUCTION_001_ACCESS_STATUS"] = "NOT_VERIFIED"
    result["RECONSTRUCTION_001_ACCESS_EVIDENCE"] = "No global filesystem isolation claim is made by this harness."

    output_preexisting_symlink = output.is_symlink()
    result["OUTPUT_BOUNDARY_STATUS"] = "PASS" if (
        not output_preexisting_symlink and roots_disjoint(output, package) and roots_disjoint(output, evidence)
    ) else "FAIL"
    output.mkdir(parents=True, exist_ok=True)
    result["OUTPUT_PATH_IDENTITY_STATUS"] = "PASS" if resolved(output) == output else "FAIL"
    result["OUTPUT_PATH_IDENTITY"] = str(output)

    sequence.append({"event": "preseal_control", "timestamp_utc": now()})
    probe = output / ".it_meth_i_seal_capability_probe.tmp"
    probe_hash = None
    try:
        probe.write_text("IT-METH-I SEAL CAPABILITY PROBE\nPACKAGE_ID=" + PACKAGE_ID + "\n", encoding="utf-8")
        probe_hash = sha256_file(probe)
        seal_ok = len(probe_hash) == 64
    except OSError:
        seal_ok = False
    finally:
        if probe.exists():
            probe.unlink()
    sequence.append({"event": "seal_capability_probe_complete", "timestamp_utc": now()})
    result["SEAL_MECHANISM_CAPABILITY_STATUS"] = "PASS" if seal_ok else "FAIL"
    result["SEAL_MECHANISM_CAPABILITY_PROBE_SHA256"] = probe_hash
    result["ACTUAL_RECONSTRUCTION_SEAL_STATUS"] = "NOT_EXECUTED"

    sequence_ok = all(sequence[i]["timestamp_utc"] <= sequence[i + 1]["timestamp_utc"] for i in range(len(sequence) - 1))
    result["CONTROL_SEQUENCE_STATUS"] = "PASS" if sequence_ok else "FAIL"
    result["TEMPORAL_ORDERING_STATUS"] = result["CONTROL_SEQUENCE_STATUS"]

    config = {"package": str(package), "repo_root": str(repo_root), "evidence_root": str(evidence),
              "output": str(output), "manifest": str(manifest_path), "mode": args.mode}
    config_text = json.dumps(config, sort_keys=True).upper()
    config_hits = [t for t in FORBIDDEN_TERMS if t in config_text]
    manifest_path_hits = [t for t in FORBIDDEN_TERMS if any(t in e["repo_path"].upper() for e in declared)]
    result["COMPARISON_TARGET_DECLARATION_STATUS"] = "PASS" if not config_hits and not manifest_path_hits else "FAIL"
    result["COMPARISON_TARGET_VERIFICATION_BASIS"] = {"configuration_scan": config_hits,
                                                       "manifest_path_scan": manifest_path_hits,
                                                       "scope": "declared control inputs only; not global filesystem isolation"}
    result["COMPARISON_PRESEAL_STATUS"] = result["COMPARISON_TARGET_DECLARATION_STATUS"]

    result["ENVIRONMENT_FINGERPRINT"] = {
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "script_sha256": sha256_file(Path(__file__).resolve()),
        "local_dependency_inventory": dependency_inventory(),
        "dependency_inventory_role": "OBSERVATIONAL_HOST_METADATA_ONLY",
    }
    technical = [result["PACKAGE_INTEGRITY"] == "PASS", result["EVIDENCE_MANIFEST_STATUS"] == "PASS",
                 result["DECLARED_EVIDENCE_BOUNDARY_STATUS"] == "PASS", result["OUTPUT_BOUNDARY_STATUS"] == "PASS",
                 result["OUTPUT_PATH_IDENTITY_STATUS"] == "PASS", result["SEAL_MECHANISM_CAPABILITY_STATUS"] == "PASS",
                 result["CONTROL_SEQUENCE_STATUS"] == "PASS", result["COMPARISON_TARGET_DECLARATION_STATUS"] == "PASS"]
    result["OVERALL_CONTROL_STATUS"] = "PASS" if all(technical) else "BLOCKED"
    result["EXECUTOR_2_DISTINCT"] = "NOT_ESTABLISHED"
    result["GOVERNANCE_AUTHORIZATION_STATUS"] = "NOT_AUTHORIZED"
    result["INDEPENDENCE_STATUS"] = "NOT_DEMONSTRATED"
    result["RECONSTRUCTION_002_STATUS"] = "NOT_EXECUTED"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="IT-METH-I blind executor control harness")
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--evidence-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--mode", choices=("DRY_RUN_CONTROL", "EXECUTION"), default="DRY_RUN_CONTROL")
    args = parser.parse_args()
    if args.mode != "DRY_RUN_CONTROL":
        print("BLOCKED: EXECUTION mode is not implemented/authorized by v0.7.")
        return 2
    result = control(args)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    print(payload, end="")
    if args.result:
        args.result.parent.mkdir(parents=True, exist_ok=True)
        args.result.write_text(payload, encoding="utf-8")
    return 0 if result["OVERALL_CONTROL_STATUS"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
