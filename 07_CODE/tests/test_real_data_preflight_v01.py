from pathlib import Path
import zipfile
from rust_omega_u_real_data_preflight_v01 import (
    ARCHIVE_ROOT,DEPENDENCIES_MEMBER,EXPECTED_SHA256,REQUIRED_DEPENDENCIES,
    REQUIRED_VERSIONS,TEMPORAL_RULE,VERSIONS_MEMBER,run_preflight,
)
def make_zip(tmp_path):
    z=tmp_path/"rust.zip"
    with zipfile.ZipFile(z,"w") as f:
        f.writestr(ARCHIVE_ROOT,"")
        f.writestr(VERSIONS_MEMBER,",".join(REQUIRED_VERSIONS)+"\n")
        f.writestr(DEPENDENCIES_MEMBER,",".join(REQUIRED_DEPENDENCIES)+"\n")
    return z
def test_wrong_snapshot_hash_fails_closed(tmp_path):
    z=make_zip(tmp_path)
    r=run_preflight(z,Path(__file__).parents[1]/"src"/"omega_u_constructor_v01.py")
    assert r["status"]=="FAIL"
    assert r["checks"]["snapshot_sha256"]["pass"] is False
def test_contract_constants_are_bound():
    assert EXPECTED_SHA256=="823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
    assert TEMPORAL_RULE=="DR-035-v0.1-ADJACENT-CREATED-AT"
    assert VERSIONS_MEMBER.endswith("package_versions.csv")
    assert DEPENDENCIES_MEMBER.endswith("package_dependencies.csv")
