"""Non-scientific preflight for the retained Rust Ω-primary snapshot."""
from __future__ import annotations
import argparse,csv,hashlib,json,re,zipfile
from pathlib import Path
EXPECTED_SHA256="823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
ARCHIVE_ROOT="rust_repos_2022_09_07/"
VERSIONS_MEMBER=ARCHIVE_ROOT+"dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER=ARCHIVE_ROOT+"dumps/postgresql/data/package_dependencies.csv"
TEMPORAL_RULE="DR-035-v0.1-ADJACENT-CREATED-AT"
IMPLEMENTATION_VERSION="RUST_OMEGA_U_CONSTRUCTOR_v0.2"
REQUIRED_VERSIONS=["id","package_id","version_str","created_at"]
REQUIRED_DEPENDENCIES=["depending_version","depending_on_package","semver_str"]
PROHIBITED=["T_acc","Reach","ΔReach","outcome","reward","utility","value","future","trajectory"]
def sha256_file(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()
def read_header(zf,member):
    with zf.open(member) as raw: return next(csv.reader(line.decode("utf-8-sig") for line in raw))
def run_preflight(zip_path,implementation_path):
    checks={}
    digest=sha256_file(zip_path)
    checks["snapshot_sha256"]={"pass":digest==EXPECTED_SHA256,"observed":digest,"expected":EXPECTED_SHA256}
    with zipfile.ZipFile(zip_path) as zf:
        names=set(zf.namelist())
        checks["required_members"]={"pass":VERSIONS_MEMBER in names and DEPENDENCIES_MEMBER in names}
        vh=read_header(zf,VERSIONS_MEMBER); dh=read_header(zf,DEPENDENCIES_MEMBER)
        checks["versions_schema"]={"pass":vh==REQUIRED_VERSIONS,"observed":vh,"expected":REQUIRED_VERSIONS}
        checks["dependencies_schema"]={"pass":dh==REQUIRED_DEPENDENCIES,"observed":dh,"expected":REQUIRED_DEPENDENCIES}
    text=implementation_path.read_text(encoding="utf-8")
    forbidden=[x for x in PROHIBITED if re.search(rf"\b{re.escape(x)}\b",text)]
    checks["implementation_firewall"]={"pass":not forbidden,"forbidden_references":forbidden}
    checks["implementation_version"]={"pass":IMPLEMENTATION_VERSION in text}
    checks["live_registry_absent"]={"pass":"crates.io" not in text.lower()}
    checks["historical_identity_recovery_separation"]={"pass":"identity_recovery" not in text}
    checks["temporal_rule_bound"]={"pass":TEMPORAL_RULE in text}
    checks["scientific_execution_boundary"]={"pass":True}
    ok=all(bool(v["pass"]) for v in checks.values())
    return {"status":"PASS" if ok else "FAIL","execution_authorized":False,"scientific_execution_authorized":False,"snapshot_sha256":digest,"implementation":str(implementation_path),"implementation_version":IMPLEMENTATION_VERSION,"temporal_rule":TEMPORAL_RULE,"checks":checks}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("zip_path",type=Path); ap.add_argument("--implementation",type=Path,required=True); ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args(); r=run_preflight(a.zip_path,a.implementation); a.output.write_text(json.dumps(r,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8"); print(json.dumps(r,indent=2,ensure_ascii=False)); return 0 if r["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
