"""Bind the immutable resource profile JSON to its GitHub artifact archive."""
from __future__ import annotations

import hashlib
import json
import os
import urllib.request
from pathlib import Path


def request(url: str, token: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def create(profile: Path, output: Path) -> dict:
    token = os.environ["GITHUB_TOKEN"]
    repository = os.environ["GITHUB_REPOSITORY"]
    repository_id = int(os.environ["GITHUB_REPOSITORY_ID"])
    run_id = int(os.environ["GITHUB_RUN_ID"])
    run_url = f"https://github.com/{repository}/actions/runs/{run_id}"
    artifacts_url = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}/artifacts"
    listing = json.loads(request(artifacts_url, token))
    matches = [
        item for item in listing.get("artifacts", [])
        if item.get("name") == "c10s-f5-g7-resource-profile-v1-1" and not item.get("expired")
    ]
    if len(matches) != 1:
        raise ValueError("RESOURCE_PROFILE_ARTIFACT_NOT_UNIQUE")
    artifact = matches[0]
    archive_digest = artifact.get("digest")
    if not isinstance(archive_digest, str) or not archive_digest.startswith("sha256:"):
        raise ValueError("RESOURCE_PROFILE_ARTIFACT_DIGEST_MISSING")
    profile_bytes = profile.read_bytes()
    profile_data = json.loads(profile_bytes)
    source_commit = profile_data.get("source_commit")
    if not isinstance(source_commit, str) or len(source_commit) != 40:
        raise ValueError("RESOURCE_PROFILE_SOURCE_COMMIT_MISSING")
    manifest = {
        "schema": "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-003",
        "profile_repository_full_name": repository,
        "profile_repository_id": repository_id,
        "profile_run_id": run_id,
        "profile_run_url": run_url,
        "profile_artifact_id": int(artifact["id"]),
        "profile_artifact_name": artifact["name"],
        "profile_artifact_archive_sha256": archive_digest.removeprefix("sha256:"),
        "profile_artifact_expires_at": artifact.get("expires_at"),
        "profile_source_commit": source_commit,
        "profile_json_sha256": hashlib.sha256(profile_bytes).hexdigest(),
        "profile_schema": profile_data.get("schema"),
        "profile_scope": profile_data.get("scope"),
        "seed_namespace": profile_data.get("seed_namespace"),
        "K_per_cell": profile_data.get("K_per_cell"),
        "C0_B": profile_data.get("C0_B"),
        "C5_B": profile_data.get("C5_B"),
        "coverage_adjudication": profile_data.get("coverage_adjudication"),
    }
    output.write_text(json.dumps(manifest, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(create(args.profile, args.output), sort_keys=True))
