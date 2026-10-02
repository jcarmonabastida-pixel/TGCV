"""Governed real-data runner for Rust Omega U_t construction.
Reads only the two admitted CSV members from the retained historical ZIP.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, zipfile
from pathlib import Path
from omega_u_constructor_v01 import build_u_t, CONSTRUCTION_VERSION, TEMPORAL_RULE_ID

EXPECTED_SHA256="823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
VERSIONS_MEMBER="rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER="rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"

def sha256_file(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def read_csv(z,m):
    with z.open(m) as f:
        return list(csv.DictReader((x.decode("utf-8") for x in f)))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    p=Path(a.zip_path)
    observed=sha256_file(p)
    if observed!=EXPECTED_SHA256:
        raise SystemExit(f"snapshot SHA-256 mismatch: {observed}")
    with zipfile.ZipFile(p) as z:
        names=set(z.namelist())
        for m in (VERSIONS_MEMBER,DEPENDENCIES_MEMBER):
            if m not in names: raise SystemExit(f"required member missing: {m}")
        versions=read_csv(z,VERSIONS_MEMBER)
        dependencies=read_csv(z,DEPENDENCIES_MEMBER)
    valid_times=[str(row["created_at"]) for row in versions if str(row.get("created_at",""))]
    if not valid_times: raise SystemExit("no valid created_at values in package_versions.csv")
    cutoff=max(valid_times)
    result=build_u_t(versions,dependencies,cutoff=cutoff,complete_target_packages=())
    result["status"]="PASS"
    result["execution_authorized"]=True
    result["scientific_execution_authorized"]=True
    result["snapshot_sha256"]=observed
    result["snapshot_path"]=str(p)
    result["implementation"]="07_CODE/src/omega_u_constructor_v01.py"
    result["implementation_version"]=CONSTRUCTION_VERSION
    result["temporal_rule"]=TEMPORAL_RULE_ID
    result["input_rows"]={"package_versions":len(versions),"package_dependencies":len(dependencies)}
    result["cutoff_rule"]="max(created_at) over valid package_versions.csv records"
    result["complete_target_packages"]=[]
    result["real_data_execution"]="U_T_CONSTRUCTION_ONLY"
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","u_count":result["u_count"],"output":a.output,"output_sha256":result["output_sha256"]},indent=2))
if __name__=="__main__": main()
