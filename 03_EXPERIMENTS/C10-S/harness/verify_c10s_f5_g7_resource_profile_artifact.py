"Verify immutable G7 resource profile artifact before planning."
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

PROFILE_MEMBER = "c10s-f5-g7-resource-profile.json"

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def verify(archive_path: Path, manifest_path: Path, metadata_path: Path, expected_repository: str) -> tuple[dict, bytes]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    archive_bytes = archive_path.read_bytes()
    if manifest.get("schema") != "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002":
        raise ValueError("PROFILE_MANIFEST_SCHEMA_MISMATCH")
    if metadata.get("id") != manifest.get("profile_artifact_id"):
        raise ValueError("PROFILE_ARTIFACT_ID_MISMATCH")
    if metadata.get("name") != manifest.get("profile_artifact_name"):
        raise ValueError("PROFILE_ARTIFACT_NAME_MISMATCH")
    if metadata.get("expired") is not False:
        raise ValueError("PROFILE_ARTIFACT_EXPIRED_OR_UNKNOWN")
    run = metadata.get("workflow_run") or {}
    if run.get("id") != manifest.get("profile_run_id"):
        raise ValueError("PROFILE_RUN_ID_MISMATCH")
    if run.get("head_sha") != manifest.get("profile_source_commit"):
        raise ValueError("PROFILE_SOURCE_COMMIT_MISMATCH")
    repository = (run.get("head_repository") or {}).get("full_name")
    if repository != expected_repository:
        raise ValueError("PROFILE_SOURCE_REPOSITORY_MISMATCH")
    actual_archive_sha = sha256(archive_bytes)
    if actual_archive_sha != manifest.get("profile_artifact_archive_sha256"):
        raise ValueError("PROFILE_ARCHIVE_DIGEST_MISMATCH")
    try:
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            if names.count(PROFILE_MEMBER) != 1:
                raise ValueError("PROFILE_MEMBER_MISSING_OR_DUPLICATED")
            for info in archive.infolist():
                name = info.filename
                parts = PurePosixPath(name).parts
                if PurePosixPath(name).is_absolute() or name.startswith("/") or "\\" in name or any(part == ".." for part in parts) or (parts and ":" in parts[0]):
                    raise ValueError("PROFILE_ARCHIVE_UNSAFE_PATH")
            unexpected = [name for name in names if name != PROFILE_MEMBER and not name.endswith("/")]
            if unexpected:
                raise ValueError("PROFILE_ARCHIVE_UNEXPECTED_MEMBER")
            profile_bytes = archive.read(PROFILE_MEMBER)
    except zipfile.BadZipFile as exc:
        raise ValueError("PROFILE_ARCHIVE_INVALID_ZIP") from exc
    actual_json_sha = sha256(profile_bytes)
    if actual_json_sha != manifest.get("profile_json_sha256"):
        raise ValueError("PROFILE_JSON_DIGEST_MISMATCH")
    profile = json.loads(profile_bytes)
    checks = (
        (profile.get("schema"), manifest.get("profile_schema"), "PROFILE_JSON_SCHEMA_MISMATCH"),
        (profile.get("scope"), manifest.get("profile_scope"), "PROFILE_SCOPE_MISMATCH"),
        (profile.get("seed_namespace"), manifest.get("seed_namespace"), "PROFILE_NAMESPACE_MISMATCH"),
        (profile.get("K_per_cell"), manifest.get("K_per_cell"), "PROFILE_K_MISMATCH"),
        (profile.get("C0_B"), manifest.get("C0_B"), "PROFILE_BOOTSTRAP_MISMATCH"),
        (profile.get("C5_B"), manifest.get("C5_B"), "PROFILE_BOOTSTRAP_MISMATCH"),
    )
    for actual, expected, error in checks:
        if actual != expected:
            raise ValueError(error)
    if profile.get("coverage_adjudication") != "NOT_PERFORMED":
        raise ValueError("PROFILE_SCOPE_VIOLATION")
    return ({
        "artifact_id": metadata["id"], "artifact_name": metadata["name"],
        "run_id": run["id"], "source_commit": run["head_sha"],
        "source_repository": repository, "archive_sha256": actual_archive_sha,
        "profile_json_sha256": actual_json_sha, "profile_member": PROFILE_MEMBER,
    }, profile_bytes)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--artifact-metadata", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--extract-profile", type=Path, required=True)
    parser.add_argument("--expected-repository", required=True)
    args = parser.parse_args()
    result, profile_bytes = verify(args.archive, args.manifest, args.artifact_metadata, args.expected_repository)
    args.extract_profile.parent.mkdir(parents=True, exist_ok=True)
    args.extract_profile.write_bytes(profile_bytes)
    args.output_json.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
