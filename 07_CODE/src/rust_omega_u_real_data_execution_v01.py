"""Governed real-data runner for Rust Omega U_t construction.
Reads only the two admitted CSV members from the retained historical ZIP.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, sqlite3, tempfile, zipfile
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
        reader = csv.DictReader((x.decode("utf-8") for x in f))
        for row in reader:
            yield row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    p=Path(a.zip_path)
    observed=sha256_file(p)
    if observed!=EXPECTED_SHA256:
        raise SystemExit(f"snapshot SHA-256 mismatch: {observed}")
    z=zipfile.ZipFile(p)
    names=set(z.namelist())
    for m in (VERSIONS_MEMBER,DEPENDENCIES_MEMBER):
        if m not in names:
            z.close()
            raise SystemExit(f"required member missing: {m}")
    with tempfile.TemporaryDirectory(prefix="tgcv-rust-omega-") as td:
        db_path=Path(td) / "versions.sqlite3"
        conn=sqlite3.connect(db_path)
        try:
            conn.execute("CREATE TABLE versions (id INTEGER PRIMARY KEY, package_id INTEGER NOT NULL, version_str TEXT NOT NULL, created_at TEXT NOT NULL)")
            conn.execute("CREATE INDEX idx_versions_pkg_time ON versions(package_id, created_at, id, version_str)")
            v_count=0
            cutoff=None
            for idx,row in enumerate(read_csv(z,VERSIONS_MEMBER)):
                try:
                    vid=int(row["id"]); package_id=int(row["package_id"])
                    version_str=str(row["version_str"]); created_at=str(row["created_at"])
                except (KeyError,TypeError,ValueError) as exc:
                    raise SystemExit(f"invalid package_versions row {idx}: {exc}") from exc
                if not created_at: raise SystemExit(f"missing created_at at row {idx}")
                conn.execute("INSERT INTO versions VALUES (?,?,?,?)",(vid,package_id,version_str,created_at))
                v_count+=1
                if cutoff is None or created_at>cutoff: cutoff=created_at
            conn.commit()
            if cutoff is None: raise SystemExit("no valid created_at values in package_versions.csv")
            versions=conn.execute("SELECT id,package_id,version_str,created_at FROM versions").fetchall()
            dependencies=read_csv(z,DEPENDENCIES_MEMBER)
            result=build_u_t(versions,dependencies,cutoff=cutoff,complete_target_packages=())
        finally:
            conn.close()
            z.close()
    result["status"]="PASS"
    result["execution_authorized"]=True
    result["scientific_execution_authorized"]=True
    result["snapshot_sha256"]=observed
    result["snapshot_path"]=str(p)
    result["implementation"]="07_CODE/src/omega_u_constructor_v01.py"
    result["implementation_version"]=CONSTRUCTION_VERSION
    result["dependency_processing"]="streaming"
    result["version_index"]="temporary_sqlite"
    result["temporal_rule"]=TEMPORAL_RULE_ID
    result["input_rows"]={"package_versions":v_count,"package_dependencies":len(dependencies)}
    result["cutoff_rule"]="max(created_at) over valid package_versions.csv records"
    result["complete_target_packages"]=[]
    result["real_data_execution"]="U_T_CONSTRUCTION_ONLY"
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","u_count":result["u_count"],"output":a.output,"output_sha256":result["output_sha256"]},indent=2))
if __name__=="__main__": main()
