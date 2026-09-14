#!/usr/bin/env python3
"""TGCV C09 — KGFS / D178 automated acquisition and technical audit.

The Yale ISPS D178 archive page is the canonical public source. On the
Windows environment the rendered page and Dataverse global file-search API do
not reliably expose the D178Fxx inventory. The archive page's 74 public HDL
identifiers are therefore frozen here as a deterministic acquisition index;
individual HDL links are resolved to Dataverse fileIds and downloaded through
the public Dataverse API.

This audit is technical only and does not upgrade C09.
"""
from __future__ import annotations
import csv, hashlib, json, re, subprocess, sys
from pathlib import Path
from urllib.request import Request, urlopen

YALE_D178_PAGE = "https://isps.yale.edu/research/data/d178"
BASE_URL = "https://dataverse.yale.edu"
DATASET_PERSISTENT_ID = "hdl:10079/01cba7fe-86d8-4e82-b9a8-f3b69c71e84f"
VERIFIED_FILE_ID = 28737
VERIFIED_FILE_LABEL = "D178F10"
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
BASELINE = DATA / "baseline"
ENDLINE = DATA / "endline"
OUTPUT = ROOT / "output"
for p in (BASELINE, ENDLINE, OUTPUT): p.mkdir(parents=True, exist_ok=True)
TARGET_TERMS = ["hhid","memid","cont_s_id","occup","occupation","employ","employment","job","income","earn","wage","salary","business","enterprise","sales","profit","loan","borrow","lender","saving","savings","insurance","insur","asset","wealth","poverty","wellbeing","welfare"]

# Canonical public HDL inventory from the Yale D178 archive page, D178F03–F76.
# This is deliberately deterministic: no global Dataverse search/index is used.
D178_HDL = {
"D178F03":"https://hdl.handle.net/10079/191dd88b-35aa-4fad-886a-af05bfb2e93b",
"D178F04":"https://hdl.handle.net/10079/d9a3d10c-978d-4043-8949-8b1477d3f888",
"D178F05":"https://hdl.handle.net/10079/62384133-fb19-4c35-8706-278bc8e9e645",
"D178F06":"https://hdl.handle.net/10079/b8a9e804-293b-4f10-872b-64a0f1580fc9",
"D178F07":"https://hdl.handle.net/10079/3d54d801-3c02-4615-9868-0c9939691624",
"D178F08":"https://hdl.handle.net/10079/91a3df6c-862d-4c42-8476-4958c2fc4819",
"D178F09":"https://hdl.handle.net/10079/c51d256f-a22a-4e11-befe-214ae81416b0",
"D178F10":"https://hdl.handle.net/10079/c631885c-58d3-4735-ac8d-4612a670ce12",
"D178F11":"https://hdl.handle.net/10079/d3d29b1d-c4d5-4ce0-8687-c49982e7fc09",
"D178F12":"https://hdl.handle.net/10079/eff3818e-5352-4f3a-acb0-694f8a28e903",
"D178F13":"https://hdl.handle.net/10079/adcd92ec-9e6c-47de-bf78-63d01e596783",
"D178F14":"https://hdl.handle.net/10079/18f0cde8-462a-4eae-ad0a-80a27eb0ce80",
"D178F15":"https://hdl.handle.net/10079/b9f8f82e-0e9d-4b5e-b1b8-762a7021803a",
"D178F16":"https://hdl.handle.net/10079/6cb7ad92-24a9-430f-bcac-6a06542404ec",
"D178F17":"https://hdl.handle.net/10079/ed7df25d-fcef-49d3-b3ef-d4e62c2a7c9d",
"D178F18":"https://hdl.handle.net/10079/b0870c86-addd-4953-83c1-254497712c5a",
"D178F19":"https://hdl.handle.net/10079/7f4f0046-644b-46ea-97e9-de64495036aa",
"D178F20":"https://hdl.handle.net/10079/91b3189d-a2b5-4d67-ac9b-d3870e3f2ea5",
"D178F21":"https://hdl.handle.net/10079/f8fe46ec-295b-4bcc-9751-5413117b3a37",
"D178F22":"https://hdl.handle.net/10079/bacd67e8-f774-4025-94b8-8c952ef58a82",
"D178F23":"https://hdl.handle.net/10079/eae7c2ff-f4a8-4820-885b-319f37432f53",
"D178F24":"https://hdl.handle.net/10079/3e196189-b0d0-4ba2-a693-0aad6b624298",
"D178F25":"https://hdl.handle.net/10079/8a649841-57ec-48fb-a0a1-5102f473e5d1",
"D178F26":"https://hdl.handle.net/10079/48f78301-dbd2-4b66-861a-e4432437a360",
"D178F27":"https://hdl.handle.net/10079/c9d4114b-7d73-448b-9400-3c561e9648fb",
"D178F28":"https://hdl.handle.net/10079/dcdf3dff-124a-44d4-85ea-6d53dac0bd31",
"D178F29":"https://hdl.handle.net/10079/7cce9554-1e65-457e-a1ce-ab585ba0fa9c",
"D178F30":"https://hdl.handle.net/10079/2ce0c92d-21c6-48eb-bc72-a9b4018cef1a",
"D178F31":"https://hdl.handle.net/10079/d7f6dde7-6404-4d4d-b8e2-3d28a794cbe4",
"D178F32":"https://hdl.handle.net/10079/31267be6-cc72-4c6a-935f-ebd436888cc3",
"D178F33":"https://hdl.handle.net/10079/19006c90-de04-49c6-9d36-63e51ab21da5",
"D178F34":"https://hdl.handle.net/10079/630bbadf-1895-4948-bab0-09c341b5d75e",
"D178F35":"https://hdl.handle.net/10079/12c08cc9-e0f9-40b7-9b76-d8687f388636",
"D178F36":"https://hdl.handle.net/10079/5885f797-3900-4f74-89d5-75098739d159",
"D178F37":"https://hdl.handle.net/10079/1099f4b0-8894-4a0a-85ed-362a134d54cc",
"D178F38":"https://hdl.handle.net/10079/26602959-cfb7-4f5a-a7e9-65ed918f708a",
"D178F39":"https://hdl.handle.net/10079/b5ce1a08-dd70-41e4-bb3b-ccb39e94c2fc",
"D178F40":"https://hdl.handle.net/10079/5c5d7954-2efc-446d-ade5-9e48c1b72d07",
"D178F41":"https://hdl.handle.net/10079/78e60d9a-fa3d-4d27-a759-5a9d8f19772b",
"D178F42":"https://hdl.handle.net/10079/535625ff-7aeb-476e-855a-2e98c675602b",
"D178F43":"https://hdl.handle.net/10079/48800b1b-b9a7-4c4d-8f91-2de79a7971be",
"D178F44":"https://hdl.handle.net/10079/3a4e29c7-4eaf-4ead-b5a4-9fd0601d311d",
"D178F45":"https://hdl.handle.net/10079/4bb7b32d-26b5-4bca-b746-06a66e5f1b26",
"D178F46":"https://hdl.handle.net/10079/c6447c69-ef56-43a6-a987-c429212b24c4",
"D178F47":"https://hdl.handle.net/10079/b30836bc-5394-42dc-bbd0-2a527b665e04",
"D178F48":"https://hdl.handle.net/10079/215d78fd-081e-40c5-a417-2110624dd504",
"D178F49":"https://hdl.handle.net/10079/18b7470b-44a4-43d9-94ca-a1fad15aa270",
"D178F50":"https://hdl.handle.net/10079/1d30261e-42c1-4d2d-a36c-efe4b8df8bc5",
"D178F51":"https://hdl.handle.net/10079/2012aaa5-8497-4b25-aec4-c1cb52870c54",
"D178F52":"https://hdl.handle.net/10079/f943daeb-5aa5-48ce-b492-2747525e14aa",
"D178F53":"https://hdl.handle.net/10079/3a07d4a6-170a-4add-b30c-b06bdb8f2287",
"D178F54":"https://hdl.handle.net/10079/0241120c-a402-40de-8cce-95fef18b05e4",
"D178F55":"https://hdl.handle.net/10079/b19ab260-c6d4-482a-ae24-71eac320cf08",
"D178F56":"https://hdl.handle.net/10079/d6504679-7743-42db-951f-9e0b36686c49",
"D178F57":"https://hdl.handle.net/10079/12f24f3c-6927-459b-920e-236d225e6511",
"D178F58":"https://hdl.handle.net/10079/cf486b26-4f27-41d1-84c8-1a404f21e035",
"D178F59":"https://hdl.handle.net/10079/440adb8c-c37b-46a4-a58c-5c6813a27c50",
"D178F60":"https://hdl.handle.net/10079/0c216c9f-d9eb-4fb4-b966-e0b9e5c8540e",
"D178F61":"https://hdl.handle.net/10079/4a77c735-9e4e-451b-a6e1-031f40acb5e8",
"D178F62":"https://hdl.handle.net/10079/1389a201-ddc2-4586-93cc-cfa9e2ff977a",
"D178F63":"https://hdl.handle.net/10079/5de8c96d-c026-4357-a456-39cefc89eb29",
"D178F64":"https://hdl.handle.net/10079/b75020b7-f292-452c-928c-b6487bba377a",
"D178F65":"https://hdl.handle.net/10079/32f55cce-3008-4855-a9d9-e10cbb012bca",
"D178F66":"https://hdl.handle.net/10079/a4b6de34-a56c-4e45-a86f-8de7ac4b2720",
"D178F67":"https://hdl.handle.net/10079/18653de0-c666-48d7-8bd6-060161a16f69",
"D178F68":"https://hdl.handle.net/10079/79ca6aeb-8cd0-4fbc-b709-8bdade471c6b",
"D178F69":"https://hdl.handle.net/10079/4026a424-74cf-4cc2-8fde-f8d53bfb6c3e",
"D178F70":"https://hdl.handle.net/10079/a10c7ea9-62d2-405a-8848-847a560a6642",
"D178F71":"https://hdl.handle.net/10079/0701625c-346f-4531-8c74-ad679e1894e1",
"D178F72":"https://hdl.handle.net/10079/654f68df-fcfd-4c61-a410-13be8686ad0e",
"D178F73":"https://hdl.handle.net/10079/a2ceee6d-c809-46a3-badb-33755070c3f8",
"D178F74":"https://hdl.handle.net/10079/2423793c-e3ab-4842-97cc-e7b56f91b24f",
"D178F75":"https://hdl.handle.net/10079/03f54bc2-0d7e-43a0-9b3b-54cbcb3a015b",
"D178F76":"https://hdl.handle.net/10079/d7d8b729-1cc0-4fb6-bf36-9d14e7e5ee89",
}

EXPECTED_SIZES = {
"D178F03":6668564,"D178F04":3112069,"D178F05":4580996,"D178F06":6592755,"D178F07":417926,"D178F08":336811,"D178F09":350112,"D178F10":1511206,"D178F11":336426,"D178F12":652745,"D178F13":379760,"D178F14":1131417,"D178F15":903641,"D178F16":1194349,"D178F17":2757938,"D178F18":2634933,"D178F19":1535526,"D178F20":683119,"D178F21":13817229,"D178F22":1676901,"D178F23":962574,"D178F24":230868,"D178F25":677077,"D178F26":1280500,"D178F27":1030141,"D178F28":252294,"D178F29":151265,"D178F30":891277,"D178F31":469392,"D178F32":4229345,"D178F33":4774709,"D178F34":1922203,"D178F35":2332189,"D178F36":512303,"D178F37":651430,"D178F38":3961272,"D178F39":640199,"D178F40":433339,"D178F41":7319501,"D178F42":1016399,"D178F43":8186607,"D178F44":8647733,"D178F45":477010,"D178F46":424842,"D178F47":477034,"D178F48":407322,"D178F49":854200,"D178F50":550388,"D178F51":789829,"D178F52":260560,"D178F53":285699,"D178F54":1161835,"D178F55":2183763,"D178F56":2084526,"D178F57":6742768,"D178F58":724360,"D178F59":1288305,"D178F60":1879463,"D178F61":171364,"D178F62":661671,"D178F63":1145797,"D178F64":3675030,"D178F65":215901,"D178F66":337396,"D178F67":1113233,"D178F68":608665,"D178F69":4209193,"D178F70":5661173,"D178F71":834636,"D178F72":1166216,"D178F73":5516291,"D178F74":1760469,"D178F75":468649,"D178F76":3932191,
}

def resolve_file_id(hdl):
    req=Request(hdl,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    try:
        with urlopen(req,timeout=120) as r: final=r.geturl()
    except Exception:
        if not sys.platform.startswith("win"): raise
        ps=("$r=Invoke-WebRequest -Uri '"+hdl+"' -UseBasicParsing -MaximumRedirection 10; $r.BaseResponse.ResponseUri.AbsoluteUri")
        final=subprocess.check_output(["powershell.exe","-NoProfile","-NonInteractive","-Command",ps],stderr=subprocess.STDOUT,timeout=120,text=True).strip()
    m=re.search(r"[?&]fileId=(\d+)",final)
    if not m: raise RuntimeError(f"Could not resolve Dataverse fileId from {hdl}; final URL: {final}")
    return int(m.group(1)), final

def download_file(file_id,destination):
    url=f"{BASE_URL}/api/access/datafile/{file_id}?format=original"
    req=Request(url,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    try:
        with urlopen(req,timeout=600) as r, open(destination,"wb") as f:
            total=0
            while True:
                chunk=r.read(1024*1024)
                if not chunk: break
                f.write(chunk); total+=len(chunk)
        return total,url
    except Exception as py_err:
        if not sys.platform.startswith("win"): raise
        ps=("$wc=New-Object System.Net.WebClient; $wc.Headers['User-Agent']='TGCV-C09-KGFS-Audit/1.0'; $wc.DownloadFile('"+url+"','"+str(destination).replace("'","''")+"')")
        try:
            subprocess.check_call(["powershell.exe","-NoProfile","-NonInteractive","-Command",ps],timeout=600)
            return destination.stat().st_size,url
        except Exception as ps_err:
            raise RuntimeError(f"Dataverse download failed via urllib ({py_err}) and PowerShell ({ps_err})") from ps_err

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def ensure_pyreadstat():
    try:
        import pyreadstat; return True
    except Exception: pass
    print("pyreadstat not installed; attempting user-level installation...")
    try:
        subprocess.run([sys.executable,"-m","pip","install","--user","pyreadstat"],check=True)
        import pyreadstat; return True
    except Exception as e:
        print(f"WARNING: pyreadstat unavailable: {e}"); return False

def classify(n):
    if 3<=n<=40:return "BASELINE"
    if 41<=n<=76:return "ENDLINE"
    raise ValueError(n)

def main():
    print("=== TGCV C09 — KGFS / D178 AUTOMATED AUDIT ===")
    print(f"Root: {ROOT}")
    print(f"Verified source file id: {VERIFIED_FILE_ID} ({VERIFIED_FILE_LABEL})")
    print(f"Dataset persistentId: {DATASET_PERSISTENT_ID}")
    print(f"Yale D178 index: {YALE_D178_PAGE}")
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    needed=[f"D178F{i:02d}" for i in range(3,77)]
    if set(needed)!=set(D178_HDL): raise RuntimeError("Canonical D178 HDL inventory is incomplete or inconsistent")
    if len(needed)!=74: raise RuntimeError(f"Expected 74 DTA files, got {len(needed)}")

    print("\n[1/7] Discovering canonical D178 file inventory...")
    print("  source=Yale ISPS D178 archive page; frozen HDL inventory")
    print(f"  canonical inventory: {len(D178_HDL)}/74 files")
    print("  composition: baseline=38 (D178F03–F40); endline=36 (D178F41–F76)")

    print("\n[2/7] Resolving HDL links to Dataverse file ids and downloading data files...")
    records=[]
    for idx,label in enumerate(needed,1):
        n=int(label[5:]); category=classify(n); hdl=D178_HDL[label]
        file_id,final_url=resolve_file_id(hdl)
        destination=(BASELINE if category=="BASELINE" else ENDLINE)/f"{label}.dta"
        if destination.exists(): size=destination.stat().st_size; reused=True
        else: size,_=download_file(file_id,destination); reused=False
        expected=EXPECTED_SIZES[label]
        size_status="PASS" if size==expected else "FAIL"
        if size_status=="FAIL": raise RuntimeError(f"Published size mismatch {label}: local={size}, expected={expected}")
        rec={"file_name":label,"d178_number":n,"category":category,"dataverse_file_id":file_id,"hdl":hdl,"resolved_url":final_url,"expected_size_bytes":expected,"size_bytes":size,"size_check":"PASS","sha256":sha256(destination),"reused":reused}
        records.append(rec)
        if label==VERIFIED_FILE_LABEL and file_id!=VERIFIED_FILE_ID: raise RuntimeError(f"Verified identity mismatch: {label} -> fileId {file_id}, expected {VERIFIED_FILE_ID}")
        if idx%5==0 or idx==len(needed): print(f"  {idx}/{len(needed)} files processed",flush=True)

    manifest={"dataset_persistent_id":DATASET_PERSISTENT_ID,"dataset_persistent_id_source":"Yale ISPS D178 public archive page","yale_index":YALE_D178_PAGE,"inventory_source":"frozen Yale D178 HDL inventory","verified_source_file":{"label":VERIFIED_FILE_LABEL,"file_id":VERIFIED_FILE_ID},"file_count":len(records),"baseline_dta_count":38,"endline_dta_count":36,"files":records}
    (OUTPUT/"KGFS_D178_DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    with open(OUTPUT/"KGFS_D178_SHA256.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(records[0].keys())); w.writeheader(); w.writerows(records)

    print("\n[3/7] Acquisition integrity...")
    print(f"  PASS — {len(records)} DTA files acquired/resolved; published sizes and SHA-256 recorded")
    print("\n[4/7] Auditing Stata metadata/variables...")
    variable_results=[]; identifier_report={}; pyreadstat_ok=ensure_pyreadstat()
    if pyreadstat_ok:
        import pyreadstat
        for round_name,folder in (("baseline",BASELINE),("endline",ENDLINE)):
            names=set()
            for path in sorted(folder.glob("*.dta")):
                try:
                    _,meta=pyreadstat.read_dta(str(path),metadataonly=True); vars_=list(meta.column_names); labels=list(meta.column_labels); names.update(vars_); hits=[]
                    for i,name in enumerate(vars_):
                        label=labels[i] if i<len(labels) else ""; text=f"{name} {label}".lower(); matched=[t for t in TARGET_TERMS if t in text]
                        if matched: hits.append({"name":name,"label":label,"matched_terms":matched})
                    variable_results.append({"round":round_name,"file":path.name,"status":"PASS","n_columns":len(vars_),"candidate_variables":hits})
                except Exception as e: variable_results.append({"round":round_name,"file":path.name,"status":"READ_FAIL","error":str(e)})
            identifier_report[round_name]={k:(k in names) for k in ("hhid","memid","cont_s_id")}
    else: variable_results.append({"status":"OPEN","reason":"pyreadstat unavailable; acquisition/hash audit remains valid"})

    print("\n[5/7] Writing technical reports...")
    report={"audit":"TGCV_C09_KGFS_TRAJECTORY_VARIABLE_AUDIT","status":"TECHNICAL_ACQUISITION_AND_METADATA_AUDIT","scientific_claim_status":"NO_C09_UPGRADE","dataset_persistent_id":DATASET_PERSISTENT_ID,"yale_index":YALE_D178_PAGE,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"file_count":len(records),"baseline_dta_count":38,"endline_dta_count":36,"required_identifier_exact_name_check":identifier_report,"variable_results":variable_results}
    (OUTPUT/"KGFS_TRAJECTORY_VARIABLE_AUDIT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    md=["# KGFS / D178 — C09 Technical Acquisition and Variable Audit","","**Status:** TECHNICAL ACQUISITION AND METADATA AUDIT","","**Scientific status:** this artifact does not upgrade C09, Core, RMA, or the Evidence→Claim Matrix.","",f"- Dataset persistentId: `{DATASET_PERSISTENT_ID}`",f"- Yale index: `{YALE_D178_PAGE}`",f"- Source file: `{VERIFIED_FILE_LABEL}` / Dataverse file id `{VERIFIED_FILE_ID}`",f"- DTA files: `74` (`38` baseline + `36` endline)","","## Exact identifier check",""]
    for rnd,vals in identifier_report.items():
        md.append(f"### {rnd}")
        for k,ok in vals.items(): md.append(f"- `{k}`: {'PASS' if ok else 'OPEN'}")
    md += ["","## Candidate variable discovery",""]
    for r in variable_results:
        if r.get("status")!="PASS": md.append(f"- `{r.get('file','n/a')}`: `{r.get('status')}`"); continue
        if not r["candidate_variables"]: continue
        md.append(f"### {r['round']} / {r['file']}")
        for v in r["candidate_variables"]: md.append(f"- `{v['name']}` — {v['label']} — matched `{', '.join(v['matched_terms'])}`")
    (OUTPUT/"KGFS_TRAJECTORY_VARIABLE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    summary={"dataset_persistent_id":DATASET_PERSISTENT_ID,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"file_count":74,"baseline_dta":38,"endline_dta":36,"output":str(OUTPUT)}
    (OUTPUT/"KGFS_D178_AUDIT_SUMMARY.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print("\n[6/7] Scientific boundary check: NO C09 UPGRADE")
    print("\n[7/7] COMPLETE")
    print(json.dumps(summary,indent=2)); print(f"Reports: {OUTPUT}")

if __name__=="__main__": main()
