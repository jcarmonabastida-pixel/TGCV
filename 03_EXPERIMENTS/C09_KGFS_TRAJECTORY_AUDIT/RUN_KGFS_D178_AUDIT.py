#!/usr/bin/env python3
"""TGCV C09 — KGFS / D178 automated acquisition and technical audit.

The D178 dataset persistent identifier is taken explicitly from the public
Yale ISPS D178 archive page. The verified file identity remains 28737=D178F10.
This audit is technical only and does not upgrade C09.
"""
from __future__ import annotations
import csv, hashlib, json, re, shutil, subprocess, sys, zipfile
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE_URL = "https://dataverse.yale.edu"
DATASET_PERSISTENT_ID = "hdl:10079/01cba7fe-86d8-4e82-b9a8-f3b69c71e84f"
DATASET_PERSISTENT_ID_SOURCE = "Yale ISPS D178 public archive page"
VERIFIED_FILE_ID = 28737
VERIFIED_FILE_LABEL = "D178F10"
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
BASELINE = DATA / "baseline"
ENDLINE = DATA / "endline"
OUTPUT = ROOT / "output"
DOWNLOAD_DIR = ROOT / "download"
ZIP_PATH = DOWNLOAD_DIR / "KGFS_D178_ORIGINAL.zip"
EXTRACT = DOWNLOAD_DIR / "D178_EXTRACTED"
for p in (BASELINE, ENDLINE, OUTPUT, DOWNLOAD_DIR): p.mkdir(parents=True, exist_ok=True)
TARGET_TERMS = ["hhid","memid","cont_s_id","occup","occupation","employ","employment","job","income","earn","wage","salary","business","enterprise","sales","profit","loan","borrow","lender","saving","savings","insurance","insur","asset","wealth","poverty","wellbeing","welfare"]

def http_json(url):
    req=Request(url,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    with urlopen(req,timeout=120) as r: return json.loads(r.read().decode("utf-8"))

def download(url,destination):
    req=Request(url,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    with urlopen(req,timeout=600) as r, open(destination,"wb") as f:
        total=0
        while True:
            chunk=r.read(1024*1024)
            if not chunk: break
            f.write(chunk); total+=len(chunk)
            if total%(10*1024*1024)<len(chunk): print(f"  downloaded {total:,} bytes",flush=True)
    return total

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def ensure_pyreadstat():
    try:
        import pyreadstat
        return True
    except Exception: pass
    print("pyreadstat not installed; attempting user-level installation...")
    try:
        subprocess.run([sys.executable,"-m","pip","install","--user","pyreadstat"],check=True)
        import pyreadstat
        return True
    except Exception as e:
        print(f"WARNING: pyreadstat unavailable: {e}"); return False

def classify(name):
    m=re.search(r"D178F(\d+)",name,re.I)
    if not m: return None,None
    n=int(m.group(1))
    if 3<=n<=40:return n,"BASELINE"
    if 41<=n<=76:return n,"ENDLINE"
    if n==77:return n,"BASELINE_CODEBOOK"
    if n==78:return n,"ENDLINE_CODEBOOK"
    if n==79:return n,"CODEBOOK_DO"
    if n==90:return n,"DDI"
    return n,"OTHER"

def main():
    print("=== TGCV C09 — KGFS / D178 AUTOMATED AUDIT ===")
    print(f"Root: {ROOT}")
    print(f"Verified source file id: {VERIFIED_FILE_ID} ({VERIFIED_FILE_LABEL})")
    print(f"Dataset persistentId: {DATASET_PERSISTENT_ID}")
    print(f"PersistentId source: {DATASET_PERSISTENT_ID_SOURCE}")
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    print("\n[1/7] Using verified public Yale D178 dataset identifier...")
    pid=DATASET_PERSISTENT_ID
    print(f"  persistentId = {pid}")
    print("\n[2/7] Downloading complete D178 dataset in original format...")
    encoded=quote(pid,safe="")
    dataset_url=f"{BASE_URL}/api/access/dataset/:persistentId/?persistentId={encoded}&format=original"
    if ZIP_PATH.exists(): print(f"  Reusing existing archive: {ZIP_PATH}")
    else: print(f"  archive bytes = {download(dataset_url,ZIP_PATH):,}")
    if ZIP_PATH.stat().st_size<10000: raise RuntimeError("Downloaded archive is suspiciously small.")
    zip_sha=sha256(ZIP_PATH); print(f"  archive SHA-256 = {zip_sha}")
    print("\n[3/7] Extracting archive...")
    if EXTRACT.exists(): shutil.rmtree(EXTRACT)
    EXTRACT.mkdir(parents=True)
    with zipfile.ZipFile(ZIP_PATH) as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f"Corrupt ZIP member: {bad}")
        z.extractall(EXTRACT)
    print("\n[4/7] Inventorying files and building canonical data folders...")
    records=[]
    for path in sorted(p for p in EXTRACT.rglob("*") if p.is_file()):
        n,category=classify(path.name)
        rec={"file_name":path.name,"d178_number":n,"category":category,"size_bytes":path.stat().st_size,"sha256":sha256(path),"extracted_path":str(path)}
        records.append(rec)
        if category=="BASELINE" and path.suffix.lower()==".dta": shutil.copy2(path,BASELINE/path.name)
        elif category=="ENDLINE" and path.suffix.lower()==".dta": shutil.copy2(path,ENDLINE/path.name)
        elif category in {"BASELINE_CODEBOOK","ENDLINE_CODEBOOK","CODEBOOK_DO","DDI"}: shutil.copy2(path,DATA/path.name)
    (OUTPUT/"KGFS_D178_DOWNLOAD_MANIFEST.json").write_text(json.dumps({"dataset_persistent_id":pid,"dataset_persistent_id_source":DATASET_PERSISTENT_ID_SOURCE,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"archive":str(ZIP_PATH),"archive_sha256":zip_sha,"files":records},indent=2,ensure_ascii=False),encoding="utf-8")
    with open(OUTPUT/"KGFS_D178_SHA256.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["file_name","d178_number","category","size_bytes","sha256","extracted_path"]); w.writeheader(); w.writerows(records)
    print("\n[5/7] Auditing Stata metadata/variables...")
    variable_results=[]; pyreadstat_ok=ensure_pyreadstat()
    if pyreadstat_ok:
        import pyreadstat
        for round_name,folder in (("baseline",BASELINE),("endline",ENDLINE)):
            for path in sorted(folder.glob("*.dta")):
                try:
                    _,meta=pyreadstat.read_dta(str(path),metadataonly=True); vars_=list(meta.column_names); labels=list(meta.column_labels); hits=[]
                    for i,name in enumerate(vars_):
                        label=labels[i] if i<len(labels) else ""; text=f"{name} {label}".lower(); matched=[t for t in TARGET_TERMS if t in text]
                        if matched: hits.append({"name":name,"label":label,"matched_terms":matched})
                    variable_results.append({"round":round_name,"file":path.name,"status":"PASS","n_columns":len(vars_),"candidate_variables":hits})
                except Exception as e: variable_results.append({"round":round_name,"file":path.name,"status":"READ_FAIL","error":str(e)})
    else: variable_results.append({"status":"OPEN","reason":"pyreadstat unavailable; file acquisition/hash audit remains valid"})
    identifier_report={}
    if pyreadstat_ok:
        import pyreadstat
        for round_name,folder in (("baseline",BASELINE),("endline",ENDLINE)):
            names=set()
            for path in folder.glob("*.dta"):
                try:
                    _,meta=pyreadstat.read_dta(str(path),metadataonly=True); names.update(meta.column_names)
                except Exception: pass
            identifier_report[round_name]={k:(k in names) for k in ("hhid","memid","cont_s_id")}
    print("\n[6/7] Writing reports...")
    report={"audit":"TGCV_C09_KGFS_TRAJECTORY_VARIABLE_AUDIT","status":"TECHNICAL_ACQUISITION_AND_METADATA_AUDIT","scientific_claim_status":"NO_C09_UPGRADE","dataset_persistent_id":pid,"dataset_persistent_id_source":DATASET_PERSISTENT_ID_SOURCE,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"archive_sha256":zip_sha,"file_count":len(records),"dta_count":sum(r["file_name"].lower().endswith(".dta") for r in records),"baseline_dta_count":sum(r["category"]=="BASELINE" and r["file_name"].lower().endswith(".dta") for r in records),"endline_dta_count":sum(r["category"]=="ENDLINE" and r["file_name"].lower().endswith(".dta") for r in records),"required_identifier_exact_name_check":identifier_report,"variable_results":variable_results}
    (OUTPUT/"KGFS_TRAJECTORY_VARIABLE_AUDIT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    md=["# KGFS / D178 — C09 Technical Acquisition and Variable Audit","","**Status:** TECHNICAL ACQUISITION AND METADATA AUDIT","","**Scientific status:** this artifact does not upgrade C09, Core, RMA, or the Evidence→Claim Matrix.","",f"- Dataset persistentId: `{pid}`",f"- PersistentId source: `{DATASET_PERSISTENT_ID_SOURCE}`",f"- Source file: `{VERIFIED_FILE_LABEL}` / file id `{VERIFIED_FILE_ID}`",f"- Archive SHA-256: `{zip_sha}`",f"- Files inventoried: `{len(records)}`",f"- DTA files: `{report['dta_count']}`",f"- Baseline DTA: `{report['baseline_dta_count']}`",f"- Endline DTA: `{report['endline_dta_count']}`","","## Exact identifier check",""]
    if identifier_report:
        for rnd,vals in identifier_report.items():
            md.append(f"### {rnd}")
            for k,ok in vals.items(): md.append(f"- `{k}`: {'PASS' if ok else 'OPEN'}")
    else: md.append("- OPEN — pyreadstat unavailable.")
    md += ["","## Candidate variable discovery",""]
    for r in variable_results:
        if r.get("status")!="PASS": md.append(f"- `{r.get('file','n/a')}`: `{r.get('status')}`"); continue
        if not r["candidate_variables"]: continue
        md.append(f"### {r['round']} / {r['file']}")
        for v in r["candidate_variables"]: md.append(f"- `{v['name']}` — {v['label']} — matched `{', '.join(v['matched_terms'])}`")
    (OUTPUT/"KGFS_TRAJECTORY_VARIABLE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    summary={"dataset_persistent_id":pid,"dataset_persistent_id_source":DATASET_PERSISTENT_ID_SOURCE,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"archive_sha256":zip_sha,"files":len(records),"dta":report["dta_count"],"baseline_dta":report["baseline_dta_count"],"endline_dta":report["endline_dta_count"],"output":str(OUTPUT)}
    (OUTPUT/"KGFS_D178_AUDIT_SUMMARY.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print("\n[7/7] COMPLETE"); print(json.dumps(summary,indent=2)); print(f"Reports: {OUTPUT}")
if __name__=="__main__": main()
