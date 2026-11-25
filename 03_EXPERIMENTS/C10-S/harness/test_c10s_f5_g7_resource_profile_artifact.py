from __future__ import annotations
import base64
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
import verify_c10s_f5_g7_resource_profile_artifact as verifier

class ResourceProfileArtifactVerificationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = Path(__file__).resolve().parents[1] / "fixtures" / "g7_resource_profile_v1_1"
        self.archive_bytes = base64.b64decode((self.fixture / "profile_artifact.zip.b64").read_text(encoding="ascii"))
        self.manifest = json.loads((self.fixture / "manifest.json").read_text(encoding="utf-8"))
        self.metadata = {"id": self.manifest["profile_artifact_id"], "name": self.manifest["profile_artifact_name"], "expired": False,
            "expires_at": self.manifest["profile_artifact_expires_at"],
            "digest": "sha256:" + self.manifest["profile_artifact_archive_sha256"],
            "workflow_run": {"id": self.manifest["profile_run_id"], "head_sha": self.manifest["profile_source_commit"],
                "repository_id": 1348691577, "head_repository_id": 1348691577,
                "head_repository": {"full_name": "jcarmonabastida-pixel/TGCV"}}}

    def run_fixture(self, archive_bytes=None, manifest=None, metadata=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive, manifest_path, metadata_path = root / "profile.zip", root / "manifest.json", root / "metadata.json"
            archive.write_bytes(self.archive_bytes if archive_bytes is None else archive_bytes)
            manifest_path.write_text(json.dumps(self.manifest if manifest is None else manifest), encoding="utf-8")
            effective_manifest = self.manifest if manifest is None else manifest
            effective_metadata = dict(self.metadata if metadata is None else metadata)
            if metadata is None:
                effective_metadata["digest"] = "sha256:" + effective_manifest["profile_artifact_archive_sha256"]
            metadata_path.write_text(json.dumps(effective_metadata), encoding="utf-8")
            return verifier.verify(archive, manifest_path, metadata_path, "jcarmonabastida-pixel/TGCV")[0]

    def test_accepts_original_immutable_profile_artifact(self):
        result = self.run_fixture()
        self.assertEqual(result["artifact_id"], self.manifest["profile_artifact_id"])
        self.assertEqual(result["run_id"], self.manifest["profile_run_id"])
        self.assertEqual(result["profile_member"], verifier.PROFILE_MEMBER)

    def test_rejects_archive_byte_tampering(self):
        altered = bytearray(self.archive_bytes); altered[-1] ^= 1
        with self.assertRaisesRegex(ValueError, "ARCHIVE_DIGEST_MISMATCH"): self.run_fixture(bytes(altered))

    def test_rejects_json_tampering_even_when_archive_is_repacked(self):
        with zipfile.ZipFile(io.BytesIO(self.archive_bytes)) as source: profile = source.read(verifier.PROFILE_MEMBER)
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as target: target.writestr(verifier.PROFILE_MEMBER, profile + b" ")
        manifest = dict(self.manifest, profile_artifact_archive_sha256=verifier.sha256(output.getvalue()))
        with self.assertRaisesRegex(ValueError, "JSON_DIGEST_MISMATCH"): self.run_fixture(output.getvalue(), manifest=manifest)

    def test_rejects_run_artifact_identity_mismatch(self):
        metadata = dict(self.metadata); metadata["workflow_run"] = dict(self.metadata["workflow_run"], id=123)
        with self.assertRaisesRegex(ValueError, "RUN_ID_MISMATCH"): self.run_fixture(metadata=metadata)

    def test_rejects_wrong_source_repository(self):
        metadata = dict(self.metadata); metadata["workflow_run"] = dict(self.metadata["workflow_run"], head_repository={"full_name": "attacker/other"})
        with self.assertRaisesRegex(ValueError, "REPOSITORY_MISMATCH"): self.run_fixture(metadata=metadata)

    def test_rejects_expired_artifact(self):
        metadata = dict(self.metadata, expired=True)
        with self.assertRaisesRegex(ValueError, "EXPIRED"): self.run_fixture(metadata=metadata)

    def test_rejects_unsafe_archive_path(self):
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as target:
            target.writestr(verifier.PROFILE_MEMBER, b"{}"); target.writestr("../escape.txt", b"bad")
        manifest = dict(self.manifest, profile_artifact_archive_sha256=verifier.sha256(output.getvalue()))
        with self.assertRaisesRegex(ValueError, "UNSAFE_PATH"): self.run_fixture(output.getvalue(), manifest=manifest)

    def test_rejects_github_artifact_digest_mismatch(self):
        metadata = dict(self.metadata, digest="sha256:" + "0" * 64)
        with self.assertRaisesRegex(ValueError, "GITHUB_ARTIFACT_DIGEST_MISMATCH"): self.run_fixture(metadata=metadata)

    def test_rejects_artifact_expiry_mismatch(self):
        metadata = dict(self.metadata, expires_at="2099-01-01T00:00:00Z")
        with self.assertRaisesRegex(ValueError, "ARTIFACT_EXPIRY_MISMATCH"): self.run_fixture(metadata=metadata)

    def test_rejects_repository_id_mismatch(self):
        run = dict(self.metadata["workflow_run"], head_repository_id=999)
        metadata = dict(self.metadata, workflow_run=run)
        with self.assertRaisesRegex(ValueError, "REPOSITORY_ID_MISMATCH"): self.run_fixture(metadata=metadata)

    def test_rejects_profile_source_commit_mismatch(self):
        with zipfile.ZipFile(io.BytesIO(self.archive_bytes)) as source: profile = json.loads(source.read(verifier.PROFILE_MEMBER))
        profile["source_commit"] = "0" * 40
        output = io.BytesIO()
        profile_bytes = json.dumps(profile).encode("utf-8")
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as target: target.writestr(verifier.PROFILE_MEMBER, profile_bytes)
        manifest = dict(self.manifest, profile_artifact_archive_sha256=verifier.sha256(output.getvalue()), profile_json_sha256=verifier.sha256(profile_bytes))
        with self.assertRaisesRegex(ValueError, "JSON_SOURCE_COMMIT_MISMATCH"): self.run_fixture(output.getvalue(), manifest=manifest)

    def test_rejects_duplicated_member(self):
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as target:
            target.writestr(verifier.PROFILE_MEMBER, b"{}"); target.writestr(verifier.PROFILE_MEMBER, b"{}")
        manifest = dict(self.manifest, profile_artifact_archive_sha256=verifier.sha256(output.getvalue()))
        with self.assertRaisesRegex(ValueError, "DUPLICATED"): self.run_fixture(output.getvalue(), manifest=manifest)

if __name__ == "__main__": unittest.main()
