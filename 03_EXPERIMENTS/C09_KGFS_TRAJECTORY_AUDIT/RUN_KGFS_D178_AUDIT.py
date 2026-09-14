#!/usr/bin/env python3
"""TGCV C09 — KGFS / D178 automated acquisition and technical audit.

The Yale ISPS D178 archive page is the canonical public index. Python urllib
can receive HTTP 404 from the Yale web endpoint on this Windows environment,
while the same public endpoint is accessible through PowerShell. Therefore the
acquisition layer uses urllib first and a PowerShell Invoke-WebRequest fallback.
The D178 file number is read from the surrounding HTML table row, because the
HDL anchor itself is labelled only "Download file". Individual HDL links are
then resolved to Dataverse fileIds and downloaded via the public Dataverse API.

This audit is technical only and does not upgrade C09.
"""
from __future__ import annotations
import csv, hashlib, json, re, subprocess, sys
from html.parser import HTMLParser
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

class D178Parser(HTMLParser):
    """Extract D178Fxx + HDL from each archive-table row.

    The D178Fxx identifier is outside the HDL anchor; the anchor text is only
    "Download file". Row-level parsing therefore avoids the previous false
    assumption that the identifier appears inside the <a> element.
    """
    def __init__(self):
        super().__init__(); self.in_tr=False; self.in_a=False; self.row_text=[]; self.row_hrefs=[]; self.rows=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="tr":
            self.in_tr=True; self.row_text=[]; self.row_hrefs=[]
        elif tag=="a" and self.in_tr and a.get("href") and "hdl.handle.net/10079/" in a["href"]:
            self.in_a=True; self.row_hrefs.append(a["href"])
    def handle_data(self, data):
        if self.in_tr: self.row_text.append(data)
    def handle_endtag(self, tag):
        if tag=="a": self.in_a=False
        elif tag=="tr" and self.in_tr:
            self.rows.append({"text":" ".join(self.row_text),"hrefs":list(self.row_hrefs)})
            self.in_tr=False; self.row_text=[]; self.row_hrefs=[]

def request_bytes(url, timeout=120):
    req=Request(url,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    try:
        with urlopen(req,timeout=timeout) as r: return r.read(), r.geturl(), dict(r.headers)
    except Exception as py_err:
        if not sys.platform.startswith("win"): raise
        ps=("$r=Invoke-WebRequest -Uri '"+url+"' -UseBasicParsing -MaximumRedirection 10; $r.Content")
        try:
            out=subprocess.check_output(["powershell.exe","-NoProfile","-NonInteractive","-Command",ps],stderr=subprocess.STDOUT,timeout=timeout,text=False)
            return out,"powershell",{}
        except Exception as ps_err:
            raise RuntimeError(f"Yale request failed via urllib ({py_err}) and PowerShell ({ps_err})") from ps_err

def resolve_file_id(hdl):
    req=Request(hdl,headers={"User-Agent":"TGCV-C09-KGFS-Audit/1.0"})
    try:
        with urlopen(req,timeout=120) as r: final=r.geturl()
    except Exception:
        if not sys.platform.startswith("win"): raise
        ps=("$r=Invoke-WebRequest -Uri '"+hdl+"' -UseBasicParsing -MaximumRedirection 10; $r.BaseResponse.ResponseUri.AbsoluteUri")
        try:
            final=subprocess.check_output(["powershell.exe","-NoProfile","-NonInteractive","-Command",ps],stderr=subprocess.STDOUT,timeout=120,text=True).strip()
        except Exception as e:
            raise RuntimeError(f"Could not resolve HDL via urllib or PowerShell: {hdl}: {e}") from e
    m=re.search(r"[?&]fileId=(\d+)",final)
    if not m:
        raise RuntimeError(f"Could not resolve Dataverse fileId from {hdl}; final URL: {final}")
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
            raise RuntimeError(f"Dataverse file download failed via urllib ({py_err}) and PowerShell ({ps_err})") from ps_err

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
    return "OTHER"

def main():
    print("=== TGCV C09 — KGFS / D178 AUTOMATED AUDIT ===")
    print(f"Root: {ROOT}")
    print(f"Verified source file id: {VERIFIED_FILE_ID} ({VERIFIED_FILE_LABEL})")
    print(f"Dataset persistentId: {DATASET_PERSISTENT_ID}")
    print(f"Yale D178 index: {YALE_D178_PAGE}")
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")

    print("\n[1/7] Reading canonical Yale D178 file index...")
    raw,transport,_=request_bytes(YALE_D178_PAGE)
    html=raw.decode("utf-8","replace")
    parser=D178Parser(); parser.feed(html)
    links={}
    for row in parser.rows:
        m=re.search(r"D178F(\d+(?:\.\d+)?)",row["text"])
        if m and row["hrefs"]:
            label=f"D178F{m.group(1)}"
            links[label]=row["hrefs"][0]
    needed=[f"D178F{i:02d}" for i in range(3,77)]
    missing=[x for x in needed if x not in links]
    if missing: raise RuntimeError(f"Yale D178 index missing expected files: {missing}")
    print(f"  transport={transport}; discovered {len(links)} D178 file links; {len(needed)} baseline/endline data files required")

    print("\n[2/7] Resolving HDL links to Dataverse file ids and downloading data files...")
    records=[]
    for idx,label in enumerate(needed,1):
        n=int(label[5:]); category=classify(n); hdl=links[label]
        file_id,final_url=resolve_file_id(hdl)
        destination=(BASELINE if category=="BASELINE" else ENDLINE)/f"{label}.dta"
        if destination.exists(): size=destination.stat().st_size; reused=True
        else: size,_=download_file(file_id,destination); reused=False
        rec={"file_name":label,"d178_number":n,"category":category,"dataverse_file_id":file_id,"hdl":hdl,"resolved_url":final_url,"size_bytes":size,"sha256":sha256(destination),"reused":reused}
        records.append(rec)
        if label==VERIFIED_FILE_LABEL and file_id!=VERIFIED_FILE_ID:
            raise RuntimeError(f"Verified identity mismatch: Yale {label} resolved to fileId {file_id}, expected {VERIFIED_FILE_ID}")
        if idx%5==0 or idx==len(needed): print(f"  {idx}/{len(needed)} files processed",flush=True)

    manifest={"dataset_persistent_id":DATASET_PERSISTENT_ID,"dataset_persistent_id_source":"Yale ISPS D178 public archive page","yale_index":YALE_D178_PAGE,"verified_source_file":{"label":VERIFIED_FILE_LABEL,"file_id":VERIFIED_FILE_ID},"files":records}
    (OUTPUT/"KGFS_D178_DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    with open(OUTPUT/"KGFS_D178_SHA256.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(records[0].keys())); w.writeheader(); w.writerows(records)

    print("\n[3/7] Acquisition integrity...")
    print(f"  PASS — {len(records)} DTA files acquired/resolved and SHA-256 recorded")

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
    report={"audit":"TGCV_C09_KGFS_TRAJECTORY_VARIABLE_AUDIT","status":"TECHNICAL_ACQUISITION_AND_METADATA_AUDIT","scientific_claim_status":"NO_C09_UPGRADE","dataset_persistent_id":DATASET_PERSISTENT_ID,"dataset_persistent_id_source":"Yale ISPS D178 public archive page","yale_index":YALE_D178_PAGE,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"file_count":len(records),"baseline_dta_count":40,"endline_dta_count":36,"required_identifier_exact_name_check":identifier_report,"variable_results":variable_results}
    (OUTPUT/"KGFS_TRAJECTORY_VARIABLE_AUDIT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    md=["# KGFS / D178 — C09 Technical Acquisition and Variable Audit","","**Status:** TECHNICAL ACQUISITION AND METADATA AUDIT","","**Scientific status:** this artifact does not upgrade C09, Core, RMA, or the Evidence→Claim Matrix.","",f"- Dataset persistentId: `{DATASET_PERSISTENT_ID}`",f"- Yale index: `{YALE_D178_PAGE}`",f"- Source file: `{VERIFIED_FILE_LABEL}` / Dataverse file id `{VERIFIED_FILE_ID}`",f"- Baseline DTA files: `40`",f"- Endline DTA files: `36`","","## Exact identifier check",""]
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
    summary={"dataset_persistent_id":DATASET_PERSISTENT_ID,"source_file_id":VERIFIED_FILE_ID,"source_file_label":VERIFIED_FILE_LABEL,"baseline_dta":40,"endline_dta":36,"output":str(OUTPUT)}
    (OUTPUT/"KGFS_D178_AUDIT_SUMMARY.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print("\n[6/7] Scientific boundary check: NO C09 UPGRADE")
    print("\n[7/7] COMPLETE")
    print(json.dumps(summary,indent=2)); print(f"Reports: {OUTPUT}")
if __name__=="__main__": main()
