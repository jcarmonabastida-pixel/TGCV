import hashlib
import json
import sys
import zipfile
from pathlib import Path

import rust_omega_u_real_data_execution_v01 as runner

VERSIONS_MEMBER = runner.VERSIONS_MEMBER
DEPENDENCIES_MEMBER = runner.DEPENDENCIES_MEMBER

def make_zip(tmp_path):
    z = tmp_path / "synthetic-rust.zip"
    versions = (
        "id,package_id,version_str,created_at\n"
        "1,10,1.0.0,2022-08-01T00:00:00Z\n"
        "2,20,1.0.0,2022-08-02T00:00:00Z\n"
    ).encode()
    deps = "depending_version,depending_on_package,semver_str\n1,20,^1.0.0\n".encode()
    with zipfile.ZipFile(z, "w", compression=zipfile.ZIP_DEFLATED) as f:
        f.writestr(VERSIONS_MEMBER, versions)
        f.writestr(DEPENDENCIES_MEMBER, deps)
    return z

def test_runner_consumes_stream_before_zip_close(tmp_path, monkeypatch):
    z = make_zip(tmp_path)
    digest = hashlib.sha256(z.read_bytes()).hexdigest()
    out = tmp_path / "result.json"
    monkeypatch.setattr(runner, "EXPECTED_SHA256", digest)
    monkeypatch.setattr(
        sys,
        "argv",
        ["runner", str(z), "--output", str(out)],
    )
    runner.main()
    result = json.loads(out.read_text(encoding="utf-8"))
    assert result["status"] == "PASS"
    assert result["u_count"] == 1
    assert result["dependency_processing"] == "streaming"
    assert result["complete_target_packages"] == []
    assert result["cutoff"] == "2022-08-02T00:00:00Z"
    assert result["U_t"][0]["provenance"][0] == "package_versions.csv:id:1"
